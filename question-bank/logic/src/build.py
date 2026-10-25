"""Build the Logic collection from its single source (plan.py + data_*.py).

    python3 question-bank/logic/src/build.py

Writes
  question-bank/nexus/logic/                    the Untangle The Nexus import package (index.json, sets/, assets/,
                                                pdf/ volumes, README.md, MANIFEST.json)
  question-bank/logic/Logic_Answer_Key.json/csv the private key: every question with its answer, full reasoning, why each
                                                wrong choice fails, accepted alternatives and how the key was verified
  question-bank/logic/Logic_Question_Collection.pdf, Logic_Answer_Key.pdf, Logic_Strategy_Guide.pdf
  question-bank/logic/src/choice_plan.json      frozen multiple-choice letters (later corrections keep them)
Reports (VALIDATION.md, COVERAGE.md, ...) are written by validate.py and report.py.
"""
import csv
import glob
import hashlib
import html
import importlib
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402

ROOT = os.path.dirname(HERE)                       # question-bank/logic
QB = os.path.dirname(ROOT)                         # question-bank
PKG = os.path.join(QB, 'nexus', 'logic')
VERSION = '1.0.0'
DATE = '2026-10-25'
TITLE = 'Logic: High School Logic and Reasoning Puzzles'
SECTION_NAME = {'M': 'MAIN', 'F1': 'FORWARD 1: ADVANCED APPLICATION', 'F2': 'FORWARD 2: EXPERT CHALLENGE'}
PLAN_FILE = os.path.join(HERE, 'choice_plan.json')


def load_sets():
    sets = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py'))):
        mod = importlib.import_module(os.path.basename(f)[:-3])
        for s in mod.SETS:
            assert s['num'] not in sets, 'set %d defined twice' % s['num']
            assert s['num'] in plan.SETS, 'set %d is not in the plan' % s['num']
            sets[s['num']] = s
    return dict(sorted(sets.items()))


def sections(s):
    """(code, relation, record) for MAIN, B1.., F1, F2."""
    out = [('M', 'main', dict(skill=s['skill'], qs=s['main']))]
    for i, b in enumerate(s['back'], 1):
        out.append(('B%d' % i, 'backward', b))
    out.append(('F1', 'forward1', s['f1']))
    out.append(('F2', 'forward2', s['f2']))
    return out


# ------------------------------------------------------------------ multiple-choice letters (balanced, then frozen)
def assign_letters(all_sets):
    try:
        frozen = json.load(open(PLAN_FILE, encoding='utf-8'))
    except FileNotFoundError:
        frozen = {}
    counts = {L: 0 for L in 'ABCD'}
    out = {}
    pending = []
    for n, s in all_sets.items():
        for code, rel, sec in sections(s):
            for i, q in enumerate(sec['qs'], 1):
                if q['type'] != 'mc':
                    continue
                qid = 'S%d-%s-Q%d' % (n, code, i)
                texts = [q['_correct']] + [w[0] for w in q['_wrong']]
                if '_panels' in q:
                    order = ['Figure %s' % L for L in q['_panels']]
                    out[qid] = order
                elif q.get('_fixed_key'):
                    raise ValueError('%s: a fixed key needs figure panels' % qid)
                elif qid in frozen and sorted(frozen[qid]) == sorted(texts):
                    out[qid] = frozen[qid]
                else:
                    pending.append((qid, q, texts))
                    continue
                k = out[qid].index(q['_correct'])
                if k < 4:
                    counts['ABCD'[k]] += 1
    prev_letter = {}
    for qid, q, texts in pending:
        n = len(texts)
        h = int(hashlib.sha1(qid.encode()).hexdigest(), 16)
        cand = sorted('ABCD'[:n], key=lambda L: (counts[L], (h >> (ord(L) - 65) * 3) & 7))
        sec = qid.rsplit('-', 1)[0]
        pick = cand[0]
        if prev_letter.get(sec) == pick and len(cand) > 1 and counts[cand[1]] <= counts[pick] + 2:
            pick = cand[1]
        prev_letter[sec] = pick
        counts[pick] += 1
        others = [t for t in texts[1:]]
        # deterministic shuffle of the wrong choices
        others.sort(key=lambda t: hashlib.sha1((qid + t).encode()).hexdigest())
        k = 'ABCD'.index(pick)
        out[qid] = others[:k] + [texts[0]] + others[k:]
    json.dump(out, open(PLAN_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    return out


# ------------------------------------------------------------------ records
def outcome_of(n, code, sec):
    p = plan.SETS[n]
    if code.startswith('B') and sec.get('outcome'):
        return sec['outcome']
    return p[1]


def build_records(all_sets, letters):
    recs, sets_pkg, figs_out = [], [], {}
    outcomes = {}
    for n, s in all_sets.items():
        p = plan.SETS[n]
        title, oid, otitle, kind, genre, family, practices, std, refs = p
        outcomes[oid] = dict(title=otitle, alignment='direct' if std else 'local', practices=practices,
                             **({'standard': std} if std else {}))
        pkg_secs = []
        codes = [c for c, _, _ in sections(s)]
        assert codes[0] == 'M' and 'F1' in codes and 'F2' in codes and any(c.startswith('B') for c in codes)
        for code, rel, sec in sections(s):
            qs = sec['qs']
            assert len(qs) == 5, 'S%d %s has %d questions (needs 5)' % (n, code, len(qs))
            sec_out = oid if rel != 'backward' else outcome_of(n, code, sec)
            ps = {'section': code, 'section_code': code, 'relation': rel, 'skill': sec['skill'], 'outcome': sec_out}
            if rel == 'backward':
                ps['branch_mode'] = sec['mode']
                ps['relationship'] = sec['relationship']
                ps['author_note'] = sec['why_helps']
                if sec['lesson']:
                    ps['lesson'] = sec['lesson']
            elif rel.startswith('forward'):
                ps['relationship'] = sec['relationship']
                ps['difficulty'] = 'harder' if rel == 'forward1' else 'expert'
                ps['label'] = 'ADVANCED APPLICATION' if rel == 'forward1' else 'EXPERT CHALLENGE'
                if sec.get('nearest'):
                    ps['nearest_related'] = True
                    ps['nearest_connection'] = sec['nearest']
            pq = []
            for i, q in enumerate(qs, 1):
                qid = 'S%d-%s-Q%d' % (n, code, i)
                out = {'id': qid, 'number': i, 'standard': std if (std and rel != 'backward') else '', 'domain': genre,
                       'type': q['type'], 'prompt': q['prompt'], 'outcome': sec_out}
                for k in ('intro', 'feedback'):
                    if q.get(k):
                        out[k] = q[k]
                key_text, accept = '', []
                if q['type'] == 'mc':
                    order = letters[qid]
                    out['choices'] = [{'letter': 'ABCD'[j], 'text': t} for j, t in enumerate(order)]
                    out['correct_letter'] = 'ABCD'[order.index(q['_correct'])]
                    out['correct_answer'] = q['_correct']
                    if '_panels' in q:
                        out['no_shuffle'] = True
                    key_text = '%s. %s' % (out['correct_letter'], q['_correct'])
                elif q['type'] == 'tf':
                    out['choices'] = [{'letter': 'A', 'text': 'True'}, {'letter': 'B', 'text': 'False'}]
                    out['correct_letter'] = 'A' if q['_key'] else 'B'
                    out['correct_answer'] = 'True' if q['_key'] else 'False'
                    out['no_shuffle'] = True
                    key_text = out['correct_answer']
                else:
                    for k, v in q.items():
                        if not k.startswith('_') and k not in ('type', 'prompt', 'intro', 'feedback'):
                            out[k] = v
                    if q['type'] == 'sa':
                        key_text = q['correct_answer']
                    elif q['type'] == 'order':
                        t = {it['key']: it['text'] for it in q['items']}
                        key_text = ' → '.join(t[k] for k in q['correct_order'])
                        accept = [' → '.join(t[k] for k in o) for o in q.get('accept_orders', [])]
                    elif q['type'] == 'grid':
                        key_text = '; '.join('%s: %s' % (r, q['correct_assignment'][r]) for r in q['rows'])
                        accept = ['; '.join('%s: %s' % (r, a[r]) for r in q['rows']) for a in q.get('accept_assignments', [])]
                    elif q['type'] == 'truth_table':
                        key_text = ' / '.join(' '.join(r) for r in q['correct'])
                    elif q['type'] == 'mark':
                        key_text = ', '.join(q['correct_marks'])
                        accept = [', '.join(a) for a in q.get('accept_marks', [])]
                    elif q['type'] == 'values':
                        key_text = 'any values that satisfy: %s (example: %s)' % (
                            q['rule'], ', '.join('%s = %s' % kv for kv in q['example_answer'].items()))
                    out['correct_answer'] = key_text
                if '_fig' in q:
                    svg, desc = q['_fig']
                    fname = 'assets/%s.svg' % qid
                    figs_out[fname] = svg
                    out['figure'] = {'svg': fname, 'description': desc}
                pq.append(out)
                rec = dict(id=qid, uid='LOGIC:' + qid, set=n, set_title=title, section=code, relation=rel,
                           section_skill=sec['skill'], number=i, type=q['type'], outcome=sec_out,
                           outcome_title=outcomes.get(sec_out, {}).get('title') or plan_outcome_title(sec_out),
                           practices=practices, content_standard=out['standard'],
                           alignment_type=('direct' if out['standard'] else 'local'), kind=kind, genre=genre,
                           family=family, prompt=q['prompt'], choices=out.get('choices', []),
                           correct_letter=out.get('correct_letter', ''), correct_answer=key_text,
                           accepted_alternatives=accept, solution=q['_why'], validation=q['_method'],
                           wrong_choices=[{'text': t, 'why_wrong': r} for t, r in q.get('_wrong', [])],
                           wrong_values_rejected=q.get('_wrong_values', []),
                           figure=out.get('figure', {}).get('svg', ''),
                           figure_description=out.get('figure', {}).get('description', ''),
                           package_fields={k: v for k, v in out.items() if k not in ('id', 'number', 'prompt', 'choices',
                                                                                     'figure', 'standard', 'domain')})
                if rel == 'backward':
                    rec['branch_mode'] = sec['mode']
                recs.append(rec)
            ps['questions'] = pq
            pkg_secs.append(ps)
        sets_pkg.append({'set': n, 'title': title, 'outcome': oid, 'genre': genre, 'kind': kind, 'family': family,
                         'practices': practices, 'sections': pkg_secs})
    return recs, sets_pkg, figs_out, outcomes


def plan_outcome_title(oid):
    for p in plan.SETS.values():
        if p[1] == oid:
            return p[2]
    return ''


# ------------------------------------------------------------------ package
def write_package(recs, sets_pkg, figs_out, outcomes):
    if os.path.exists(PKG):
        shutil.rmtree(PKG)
    os.makedirs(os.path.join(PKG, 'sets'))
    os.makedirs(os.path.join(PKG, 'assets'))
    for o in {r['outcome'] for r in recs}:
        if o not in outcomes:
            for p in plan.SETS.values():
                if p[1] == o:
                    outcomes[o] = dict(title=p[2], alignment='direct' if p[7] else 'local', practices=p[6],
                                       **({'standard': p[7]} if p[7] else {}))
    index = {'format_version': 1, 'course': 'logic', 'bank_version': VERSION, 'title': TITLE,
             'collection': {'id': 'LOGIC', 'version': VERSION, 'date': DATE},
             'outcomes': dict(sorted(outcomes.items())),
             'practices': plan.PRACTICES,
             'sets': [{'set': s['set'], 'file': 'sets/S%02d.json' % s['set'], 'title': s['title'], 'outcome': s['outcome'],
                       'kind': s['kind'], 'genre': s['genre']} for s in sets_pkg]}
    json.dump(index, open(os.path.join(PKG, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for s in sets_pkg:
        json.dump(s, open(os.path.join(PKG, 'sets', 'S%02d.json' % s['set']), 'w', encoding='utf-8'), ensure_ascii=False,
                  indent=1)
    for f, svg in figs_out.items():
        open(os.path.join(PKG, f), 'w', encoding='utf-8').write(svg)


# ------------------------------------------------------------------ PDFs
CSS = ('body{font-family:sans-serif;font-size:15px;color:#111;line-height:1.35}'
       'h1{font-size:22px;margin:0 0 8px 0}h2{font-size:17px;margin:6px 0}'
       'table{border-collapse:collapse}td,th{border:1px solid #444;padding:3px 8px;font-size:13px}'
       '.ch{margin:2px 0 2px 14px}.small{font-size:12px;color:#333}.lab{font-weight:bold}')


def esc(s):
    return html.escape(str(s)).replace('\n', '<br>')


def interaction_html(r):
    pf = r['package_fields']
    t = r['type']
    if t in ('mc', 'tf'):
        return ''.join('<p class="ch"><b>%s.</b> %s</p>' % (c['letter'], esc(c['text'])) for c in r['choices'])
    if t == 'sa':
        return ''.join('<p class="ch">%s ____________________</p>' % esc(l) for l in pf['answer_lines'])
    if t == 'values':
        return ''.join('<p class="ch">%s ____________</p>' % esc(f['label']) for f in pf['fields'])
    if t == 'order':
        return ('<p class="small">Put these in order:</p>' +
                ''.join('<p class="ch"><b>%s</b> %s</p>' % (esc(i['key']), esc(i['text'])) for i in pf['items']))
    if t == 'grid':
        head = '<tr><th></th>' + ''.join('<th>%s</th>' % esc(c) for c in pf['columns']) + '</tr>'
        body = ''.join('<tr><td><b>%s</b></td>%s</tr>' % (esc(rw), '<td>&nbsp;</td>' * len(pf['columns'])) for rw in pf['rows'])
        note = ' Each column is used once.' if pf.get('distinct_columns') else ''
        return '<p class="small">Choose one column for each row.%s</p><table>%s%s</table>' % (note, head, body)
    if t == 'truth_table':
        head = '<tr>' + ''.join('<th>%s</th>' % esc(v) for v in pf['variables']) + ''.join(
            '<th>%s</th>' % esc(c) for c in pf['columns']) + '</tr>'
        body = ''.join('<tr>' + ''.join('<td>%s</td>' % v for v in row) + '<td>&nbsp;</td>' * len(pf['columns']) + '</tr>'
                       for row in pf['rows'])
        return '<p class="small">Fill in T or F in every empty cell.</p><table>%s%s</table>' % (head, body)
    if t == 'mark':
        if pf['layout'].startswith('venn'):
            return '<p class="small">Mark the regions on the Venn diagram of %s (on screen: click each region).</p>' % esc(
                ', '.join(pf['sets']))
        return '<p class="small">Mark cells on the %d × %d grid (on screen: click each cell; cells are named row,column).</p>' % (
            pf['rows'], pf['cols'])
    return ''


def ref_box(r, title):
    sec = SECTION_NAME.get(r['section'], 'BACKWARD %s' % r['section'][1:])
    mode = ' (%s)' % r['branch_mode'].replace('_', ' ') if r.get('branch_mode') else ''
    return ('<div style="border:1px solid #888;padding:5px;margin-top:8px;background:#eef3f8">'
            '<span class="small"><b>REFERENCE LABEL: NOT PART OF THE QUESTION</b> &nbsp; <b>ID %s</b><br>'
            'Logic, Set %d: %s · %s%s · Q%d/5 · Outcome %s (local) · %s</span></div>'
            % (r['id'], r['set'], esc(title), sec, mode, r['number'], r['outcome'], ', '.join(r['practices'])))


def make_question_pdf(recs, all_sets, path):
    import pymupdf
    doc = pymupdf.open()
    arch = pymupdf.Archive(PKG)
    W, H = 792, 612
    page_of = {}
    cur_set = None
    for r in recs:
        if r['set'] != cur_set:
            cur_set = r['set']
            p = plan.SETS[cur_set]
            pg = doc.new_page(width=W, height=H)
            secs = [x for x in sections(all_sets[cur_set])]
            lines = ''.join('<p class="ch">%s: %s</p>' % (esc(SECTION_NAME.get(c, 'BACKWARD ' + c[1:])), esc(sec['skill']))
                            for c, _, sec in secs)
            pg.insert_htmlbox(pymupdf.Rect(50, 60, W - 50, H - 50),
                              '<h1>Set %d: %s</h1><p>Local outcome %s: %s</p><p class="small">%s · genre: %s · %s</p>%s'
                              % (cur_set, esc(p[0]), p[1], esc(p[2]), 'Puzzle set' if p[3] == 'puzzle' else 'Formal logic set',
                                 esc(p[4]), ', '.join(p[6]), lines), css=CSS)
        pg = doc.new_page(width=W, height=H)
        body = '<p>%s</p>' % esc(r['prompt'])
        if r['figure']:
            body += '<p><img src="%s" style="max-width:640px;max-height:280px"></p>' % r['figure']
        body += interaction_html(r)
        pg.insert_htmlbox(pymupdf.Rect(40, 34, W - 40, H - 92), body, css=CSS, archive=arch, scale_low=0.5)
        pg.insert_htmlbox(pymupdf.Rect(40, H - 88, W - 40, H - 22), ref_box(r, r['set_title']), css=CSS)
        pg.insert_text((W - 60, H - 10), str(len(doc)), fontsize=9)
        page_of[r['id']] = len(doc)
    doc.save(path, garbage=3, deflate=True)
    return page_of


def make_key_pdf(recs, path):
    import pymupdf
    doc = pymupdf.open()
    W, H = 612, 792
    story_html = ['<h1>Logic answer key (version %s)</h1><p class="small">Private grading material. Each entry gives the '
                  'question ID, its page in the question collection, the correct response, the full reasoning, why each wrong '
                  'choice fails, accepted alternatives, the grading rule and how the key was verified.</p>' % VERSION]
    for r in recs:
        alt = ('<p><b>Also accepted:</b> %s</p>' % esc(' | '.join(r['accepted_alternatives']))) if r['accepted_alternatives'] else ''
        wr = ''.join('<p class="ch">✗ %s: %s</p>' % (esc(w['text']), esc(w['why_wrong'])) for w in r['wrong_choices'])
        rej = ''
        if r['wrong_values_rejected']:
            rej = '<p class="small">Tempting answers the rule rejects: %s</p>' % esc(
                '; '.join(', '.join('%s = %s' % kv for kv in w.items()) for w in r['wrong_values_rejected']))
        grading = GRADING.get(r['type'], '')
        story_html.append(
            '<div style="border-top:1px solid #999;margin-top:6px;padding-top:4px"><h2>%s · question page %d</h2>'
            '<p class="small">%s · %s</p><p class="small">%s</p><p><b>Answer:</b> %s</p>%s<p><b>Reasoning:</b> %s</p>%s%s'
            '<p class="small"><b>Grading:</b> %s</p><p class="small"><b>Verified:</b> %s</p></div>'
            % (r['id'], r['question_page'], r['outcome'], esc(r['section_skill']), esc(r['prompt'][:400]),
               esc(r['correct_answer']), alt, esc(r['solution']), wr, rej, grading, esc(r['validation'])))
    story = pymupdf.Story('<html><body>%s</body></html>' % ''.join(story_html), user_css=CSS)
    writer = pymupdf.DocumentWriter(path)
    more = 1
    while more:
        dev = writer.begin_page(pymupdf.Rect(0, 0, W, H))
        more, _ = story.place(pymupdf.Rect(45, 45, W - 45, H - 45))
        story.draw(dev)
        writer.end_page()
    writer.close()


GRADING = {
    'mc': 'The chosen letter must equal the keyed letter.',
    'tf': 'The chosen True/False must equal the key.',
    'sa': "The game's answer checker compares the typed value with the key (equivalent number forms accepted).",
    'order': 'The learner\'s order must equal the key or an accepted alternative.',
    'grid': 'The learner\'s complete assignment must equal the key or an accepted alternative.',
    'truth_table': 'Every output cell must match (T/F, true/false or 1/0).',
    'mark': 'The set of marked regions or cells must equal the key or an accepted alternative.',
    'values': 'The learner\'s values are put into the rule; ANY values that make the rule true are correct.',
}


def make_strategy_pdf(all_sets, path):
    import pymupdf
    parts = ['<h1>Logic strategy guide (version %s)</h1><p class="small">The ungraded lessons shown at the start of each '
             'guided-strategy backward branch, by branch ID. Each worked example is a different puzzle from every scored '
             'question.</p>' % VERSION]
    for n, s in all_sets.items():
        for code, rel, sec in sections(s):
            if rel == 'backward' and sec.get('lesson'):
                L = sec['lesson']
                parts.append('<div style="border-top:1px solid #999;margin-top:8px"><h2>S%d-%s · %s</h2><p class="small">%s</p>'
                             % (n, code, esc(L['title']), esc(sec['skill'])) +
                             ''.join('<p>%s</p>' % esc(t) for t in L['text']) +
                             '<p><b>%s</b></p>' % esc(L['example']['title']) +
                             ''.join('<p>%s</p>' % esc(t) for t in L['example']['prompt']) +
                             '<ol>' + ''.join('<li>%s</li>' % esc(t) for t in L['example']['steps']) + '</ol></div>')
    story = pymupdf.Story('<html><body>%s</body></html>' % ''.join(parts), user_css=CSS)
    writer = pymupdf.DocumentWriter(path)
    more = 1
    while more:
        dev = writer.begin_page(pymupdf.Rect(0, 0, 612, 792))
        more, _ = story.place(pymupdf.Rect(45, 45, 567, 747))
        story.draw(dev)
        writer.end_page()
    writer.close()


# ------------------------------------------------------------------ answer key files
KEY_FIELDS = ['uid', 'id', 'set', 'set_title', 'section', 'relation', 'branch_mode', 'section_skill', 'number', 'type',
              'outcome', 'outcome_title', 'alignment_type', 'practices', 'content_standard', 'kind', 'genre', 'family',
              'question_page', 'prompt', 'choices', 'correct_letter', 'correct_answer', 'accepted_alternatives', 'solution',
              'wrong_choices', 'wrong_values_rejected', 'validation', 'figure', 'figure_description', 'package_fields']


def write_key(recs):
    data = {'collection': {'id': 'LOGIC', 'course': 'logic', 'title': TITLE, 'version': VERSION, 'date': DATE},
            'questions': [{k: r.get(k, '') for k in KEY_FIELDS} for r in recs]}
    json.dump(data, open(os.path.join(ROOT, 'Logic_Answer_Key.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(ROOT, 'Logic_Answer_Key.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_MINIMAL)
        w.writerow(KEY_FIELDS)
        for r in recs:
            row = []
            for k in KEY_FIELDS:
                v = r.get(k, '')
                if k == 'choices':
                    v = ' | '.join('%s. %s' % (c['letter'], c['text']) for c in v)
                elif k == 'wrong_choices':
                    v = ' | '.join('%s: %s' % (x['text'], x['why_wrong']) for x in v)
                elif isinstance(v, (list, dict)):
                    v = json.dumps(v, ensure_ascii=False)
                row.append(v)
            w.writerow(row)


def shrink_pdf(path):
    """Subset the embedded fonts (each page otherwise carries whole font files) and rewrite compactly."""
    import pymupdf
    doc = pymupdf.open(path)
    doc.subset_fonts()
    tmp = path + '.tmp'
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)


def main(pdf=True):
    all_sets = load_sets()
    letters = assign_letters(all_sets)
    recs, sets_pkg, figs_out, outcomes = build_records(all_sets, letters)
    write_package(recs, sets_pkg, figs_out, outcomes)
    if pdf:
        qpath = os.path.join(ROOT, 'Logic_Question_Collection.pdf')
        page_of = make_question_pdf(recs, all_sets, qpath)
        for r in recs:
            r['question_page'] = page_of[r['id']]
        make_key_pdf(recs, os.path.join(ROOT, 'Logic_Answer_Key.pdf'))
        make_strategy_pdf(all_sets, os.path.join(ROOT, 'Logic_Strategy_Guide.pdf'))
        for f in ('Logic_Question_Collection.pdf', 'Logic_Answer_Key.pdf', 'Logic_Strategy_Guide.pdf'):
            shrink_pdf(os.path.join(ROOT, f))
    else:
        for r in recs:
            r['question_page'] = 0
    write_key(recs)
    print('Logic: %d sets, %d questions, %d figures' % (len(all_sets), len(recs), len(figs_out)))
    return all_sets, recs


if __name__ == '__main__':
    main(pdf='--nopdf' not in sys.argv)
