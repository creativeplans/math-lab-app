"""Revision map between a published collection and the current source.

A grade that has been published keeps a snapshot of every question in
src/history/v<N>_records.json and explains each change in src/changes.py:

    VERSION_FROM = '1.0.0'
    FINDINGS = {'C01': 'Juice units', ...}            # review finding codes and titles
    CHANGES = [
        (['S42-F1-Q4'], 'C01', 'revised', 'Context changed to a 24-ounce bag of rice (mass ounces).'),
        (['S7-B2-*'], 'B01', 'retired', 'Branch used a Grade 5 standard; replaced by S7-B4.'),
        ...
    ]

Statuses:
    unchanged  same prompt, choices, answer, note and figure as the published version
    revised    same ID, same skill and standard; wording, values, figure, answer or grading corrected
    retired    the ID no longer exists and is never reused (its replacement has a new ID)
    new        an ID that did not exist in the published version

export.py checks every question against the snapshot. A question whose content changed without an
entry in CHANGES stops the build, so nothing changes silently.
"""
import fnmatch
import importlib
import json
import os

import answers as A


def snapshot(qd, rec, std, skill, nearest=False):
    """The comparable content of one question, in the shape of the history files."""
    fig = qd.get('fig')
    return dict(standard=std, skill=skill, type=rec['type'], prompt=qd['stem'],
                choices=[c['text'] for c in rec['choices']], correct_letter=rec['correct_letter'],
                correct_answer=rec['correct_answer'], grading_note=rec['grading_note'],
                figure=fig, drawing_answer=rec.get('drawing_answer'), required_method=rec.get('required_method'),
                nearest_related=bool(nearest))


# compared only when the history file records them (older snapshots predate these fields)
OPTIONAL = ('drawing_answer', 'required_method', 'nearest_related')


def _norm(v):
    return json.loads(json.dumps(v, ensure_ascii=False, default=list)) if v is not None else None


def differences(old, new):
    out = []
    for k in ('standard', 'type', 'prompt', 'choices', 'correct_letter', 'correct_answer', 'grading_note'):
        if _norm(old.get(k)) != _norm(new.get(k)):
            out.append(k)
    of, nf = _norm(old.get('figure')), _norm(new.get('figure'))
    if of != nf:
        out.append('figure')
    if 'skill' in old and old['skill'] != new['skill'] and 'standard' not in out:
        out.append('skill')
    for k in OPTIONAL:
        if k in old and _norm(old[k]) != _norm(new.get(k)):
            out.append(k)
    return out


def axis_only(old, new):
    """True when the only change to a figure is adding x/y axis names to a coordinate grid."""
    def strip(f):
        if isinstance(f, dict):
            return {k: strip(v) for k, v in f.items() if k not in ('xlabel', 'ylabel', 'axisnames')}
        if isinstance(f, list):
            return [strip(v) for v in f]
        return f
    return strip(_norm(old.get('figure'))) == strip(_norm(new.get('figure')))


class Tracker:
    def __init__(self, grade_dir, collection):
        self.collection = collection
        src = os.path.join(grade_dir, 'src')
        self.active = os.path.exists(os.path.join(src, 'changes.py'))
        self.seen = {}
        if not self.active:
            return
        ch = importlib.import_module('changes')
        self.cfg = ch
        hist = json.load(open(os.path.join(src, 'history', 'v%s_records.json' % ch.VERSION_FROM.split('.')[0]),
                              encoding='utf-8'))
        self.old = hist['questions']
        self.rules = []
        for pats, code, status, text in ch.CHANGES:
            self.rules.append((pats, code, status, text))
        self.used = set()

    def _rules_for(self, qid):
        out = []
        for i, (pats, code, status, text) in enumerate(self.rules):
            if any(fnmatch.fnmatchcase(qid, p) for p in pats):
                out.append((i, code, status, text))
        return out

    def check(self, qid, snap):
        """Record one current question; return its revision entry."""
        if not self.active:
            return dict(id=qid, status='unchanged')
        rules = self._rules_for(qid)
        for i, *_ in rules:
            self.used.add(i)
        old = self.old.get(qid)
        if old is None:
            entry = dict(status='new')
            if not rules:
                raise ValueError('%s is new but has no entry in changes.py' % qid)
        else:
            diff = differences(old, snap)
            if not diff and any(r[2] == 'layout' for r in rules):
                entry = dict(status='revised', changed=['answer key PDF layout'])
            elif not diff:
                if rules:
                    raise ValueError('%s has an entry in changes.py but did not change' % qid)
                entry = dict(status='unchanged')
            else:
                entry = dict(status='revised', changed=diff)
                if not rules:
                    if diff == ['figure'] and axis_only(old, snap):
                        rules = [(None, 'F08', 'revised', 'Coordinate grid now names its axes x and y.')]
                    else:
                        raise ValueError('%s changed (%s) but has no entry in changes.py' % (qid, ', '.join(diff)))
            if old['standard'] != snap['standard']:
                raise ValueError('%s: standard changed %s -> %s; retire the ID and add a new one'
                                 % (qid, old['standard'], snap['standard']))
        if rules:
            entry['findings'] = sorted({r[1] for r in rules if r[1]})
            entry['reason'] = ' '.join(r[3] for r in rules)
        if entry['status'] == 'unchanged':
            entry.pop('findings', None)
            entry.pop('reason', None)
        entry = dict(id=qid, uid='%s:%s' % (self.collection['id'], qid), **entry)
        self._links(entry)
        self.seen[qid] = entry
        return entry

    def _links(self, e):
        for old, new in getattr(self.cfg, 'MOVES', []):
            if e['id'] == new:
                e['moved_from'] = old
            if e['id'] == old:
                e['moved_to'] = new
        for old, new in getattr(self.cfg, 'BRANCH_REPLACEMENTS', []):
            if e['id'].startswith(old + '-'):
                e['replaced_by_branch'] = new
            if e['id'].startswith(new + '-'):
                e['replaces_branch'] = old

    def document(self):
        if not self.active:
            return None
        entries = []
        for qid in self.old:
            if qid not in self.seen:
                rules = self._rules_for(qid)
                for i, *_ in rules:
                    self.used.add(i)
                if not rules or not any(r[2] == 'retired' for r in rules):
                    raise ValueError('%s was removed but is not marked retired in changes.py' % qid)
                e = dict(id=qid, uid='%s:%s' % (self.collection['id'], qid), status='retired',
                         findings=sorted({r[1] for r in rules if r[1]}), reason=' '.join(r[3] for r in rules))
                self._links(e)
                entries.append(e)
        unused = [self.rules[i][0] for i in range(len(self.rules)) if i not in self.used]
        if unused:
            raise ValueError('changes.py entries matched no question: %s' % unused)
        allq = list(self.seen.values()) + entries
        allq.sort(key=sort_key)
        counts = {}
        for e in allq:
            counts[e['status']] = counts.get(e['status'], 0) + 1
        return dict(collection=self.collection, previous_version=self.cfg.VERSION_FROM,
                    previous_commit=getattr(self.cfg, 'COMMIT_FROM', None),
                    summary=counts, findings=self.cfg.FINDINGS,
                    rules=['IDs of corrected questions are kept (status revised).',
                           'An ID whose skill or standard changes is retired and never reused; the replacement '
                           'questions get new IDs (status new).',
                           'Sets added after publication take the next free set number; branches added to an '
                           'existing set take the next free branch number. Numbers need not be consecutive.'],
                    entries=allq)


def sort_key(e):
    s, sec, q = e['id'].split('-')
    order = {'M': 0, 'F1': 900, 'F2': 901}
    return (int(s[1:]), order.get(sec, int(sec[1:]) if sec[0] == 'B' else 999), int(q[1:]))


def write_changelog(doc, path, title):
    if not doc:
        return
    lines = ['# %s — change log' % title, '',
             'Version %s (previous %s%s). One row per question ID that changed. Unchanged IDs are omitted; '
             'the full map, including unchanged IDs, is `revisions.json` in the import package.' % (
                 doc['collection']['version'], doc['previous_version'],
                 ', commit %s' % doc['previous_commit'] if doc['previous_commit'] else ''), '',
             '| Status | Count |', '|---|---:|']
    for k in ('unchanged', 'revised', 'retired', 'new'):
        lines.append('| %s | %d |' % (k, doc['summary'].get(k, 0)))
    lines += ['', 'Rules: ' + ' '.join(doc['rules']), '', '## Review findings', '', '| Code | Finding |', '|---|---|']
    for k, v in doc['findings'].items():
        lines.append('| %s | %s |' % (k, v))
    lines += ['', '## ID map', '',
              'Questions that moved keep their content under a new ID; the old ID is retired or now holds the corrected '
              'question for the narrower skill, as the Status column says.', '',
              '| Old ID | New ID | Old ID status |', '|---|---|---|']
    status = {e['id']: e['status'] for e in doc['entries']}
    for e in doc['entries']:
        if e.get('moved_from'):
            lines.append('| %s | %s | %s |' % (e['moved_from'], e['id'], status.get(e['moved_from'], '')))
    lines += ['', 'Retired backward branches and their replacements:', '', '| Retired branch | Replacement branch |', '|---|---|']
    seen = set()
    for e in doc['entries']:
        b = e.get('replaced_by_branch')
        if b and b not in seen:
            seen.add(b)
            lines.append('| %s | %s |' % (e['id'].rsplit('-', 1)[0], b))
    lines += ['', '## Changes by question ID', '', '| ID | Status | Findings | What changed | Reason |', '|---|---|---|---|---|']
    for e in doc['entries']:
        if e['status'] == 'unchanged':
            continue
        lines.append('| %s | %s | %s | %s | %s |' % (
            e['id'], e['status'], ', '.join(e.get('findings', [])), ', '.join(e.get('changed', [])),
            e.get('reason', '').replace('|', '\\|')))
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
