"""Geometry collection validation: writes geometry/VALIDATION.md and exits 1 if any check fails.

    python3 question-bank/geometry/src/validate.py

Run after engine/build.py geometry. Checks the source sets (structure, coverage, branch rules, metadata, figures) and the
generated files (answer key JSON and CSV, both PDFs page by page).
"""
import collections
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'engine')
sys.path.insert(0, ENGINE)
import build  # noqa: E402
import hs_courses  # noqa: E402
import qb  # noqa: E402

build.load_grade('geometry')
import standards  # noqa: E402  (geometry/src, on the path after load_grade)

SETS = list(build.all_sets())
P = build.out_paths()
DATA = json.load(open(P['data'] + '.json', encoding='utf-8'))
RECS = DATA['questions']
results = []  # (check, ok, detail)


def check(name, problems, detail_ok=''):
    results.append((name, not problems, detail_ok if not problems else '; '.join(problems[:25]) + (' …(%d)' % len(problems) if len(problems) > 25 else '')))


def norm(s):
    return re.sub(r'\s+', ' ', s.strip().lower())


# ---------------------------------------------------------------- 1. structure
prob = []
nback = collections.Counter()
for st in SETS:
    if len(st['main']) != 5:
        prob.append('S%d MAIN has %d questions' % (st['num'], len(st['main'])))
    nback[len(st['back'])] += 1
    if not 2 <= len(st['back']) <= 7:
        prob.append('S%d has %d backward branches' % (st['num'], len(st['back'])))
    for key, _, _, qs, _ in build.sections(st):
        if len(qs) != 5:
            prob.append('S%d %s has %d questions' % (st['num'], key, len(qs)))
check('Every set: MAIN + 2-7 backward + FORWARD 1 + FORWARD 2, five questions each', prob,
      '%d sets; backward branches per set: %s' % (len(SETS), ', '.join('%d sets with %d' % (v, k) for k, v in sorted(nback.items()))))

prob = []
ids = [r['id'] for r in RECS]
uids = [r['uid'] for r in RECS]
for dup in [k for k, v in collections.Counter(ids).items() if v > 1]:
    prob.append('duplicate id ' + dup)
for dup in [k for k, v in collections.Counter(uids).items() if v > 1]:
    prob.append('duplicate uid ' + dup)
pat = re.compile(r'^S(\d+)-(M|B\d|F1|F2)-Q([1-5])$')
for r in RECS:
    m = pat.match(r['id'])
    if not m or int(m.group(1)) != r['set'] or r['uid'] != 'GEO:' + r['id']:
        prob.append('bad id ' + r['id'])
expected = sum(5 * len(build.sections(st)) for st in SETS)
if len(RECS) != expected:
    prob.append('records %d, expected %d' % (len(RECS), expected))
check('IDs unique, well formed, namespaced (GEO:), one record per question', prob, '%d questions, %d unique IDs' % (len(RECS), len(set(ids))))

# ---------------------------------------------------------------- 2. coverage
prob = []
core_main = collections.defaultdict(list)
for st in SETS:
    core_main[st['std']].append(st['num'])
    plus = st['std'] in hs_courses.GEOMETRY_PLUS
    if plus != (st.get('strand') == 'advanced'):
        prob.append('S%d strand %s does not match %s' % (st['num'], st.get('strand'), st['std']))
for code in hs_courses.GEOMETRY + hs_courses.GEOMETRY_PLUS:
    if not core_main.get(code):
        prob.append('no MAIN set for ' + code)
check('Every Geometry standard has a MAIN set; (+) standards only in the ADVANCED EXTENSION strand', prob,
      '%d core standards and %d (+) standards, each with at least one MAIN set' % (len(hs_courses.GEOMETRY), len(hs_courses.GEOMETRY_PLUS)))

prob = []
covered = collections.defaultdict(list)
valid = {sid: code for code, (_, subs) in standards.STANDARDS.items() for sid, _ in subs}
for st in SETS:
    if not st.get('covers'):
        prob.append('S%d has no covers=' % st['num'])
    for sid in st.get('covers', []):
        if sid not in valid:
            prob.append('S%d covers unknown %s' % (st['num'], sid))
        elif valid[sid] != st['std']:
            prob.append('S%d covers %s of %s' % (st['num'], sid, valid[sid]))
        covered[sid].append(st['num'])
for sid in valid:
    if not covered[sid]:
        prob.append('subskill %s not covered' % sid)
check('Every subpart / distinct demand (subskill) is the focus of a MAIN set', prob, '%d subskills, all covered' % len(valid))

prob = []
nverb = 0
sets_by_num = {st['num']: st for st in SETS}
for code, (_, subs) in standards.STANDARDS.items():
    for sid, desc in subs:
        verb = desc.split()[0].lower()
        need = 'plot' if verb == 'construct' else ('work' if verb in ('prove', 'derive', 'explain', 'informal', 'give') or 'argument' in desc.lower() else None)
        if not need:
            continue
        nverb += 1
        types = {r['type'] for r in RECS if r['set'] in covered[sid] and r['section'] == 'MAIN'}
        if need not in types:
            prob.append('%s (%s) MAIN has no %s question' % (sid, desc, need))
check('Verb check: subskills that say prove / derive / explain / give an argument have MAIN proof or explanation (shown-work) questions; '
      '"construct" subskills have MAIN construction questions', prob, '%d verb subskills checked' % nverb)

# ---------------------------------------------------------------- 3. branches
prob = []
main_before = {}
applied = []
seen = set()
for st in SETS:
    main_before[st['num']] = set(seen)
    seen.add(st['std'])
for st in SETS:
    for i, b in enumerate(st['back'], 1):
        m = b.get('meta', {})
        code = b['std']
        if not m.get('why') or m.get('align') not in ('exact', 'supporting'):
            prob.append('S%d B%d metadata' % (st['num'], i))
        if code.startswith('HSG') or code in hs_courses.GEOMETRY_PLUS:
            if code not in main_before[st['num']]:
                prob.append('S%d B%d %s is not the MAIN of an earlier set' % (st['num'], i, code))
        elif code.startswith('HS'):
            if hs_courses.course_of(code) != 'Algebra I':
                prob.append('S%d B%d %s is not an earlier course' % (st['num'], i, code))
        elif not re.match(r'^[K1-8]\.', code):
            prob.append('S%d B%d %s unknown source' % (st['num'], i, code))
    for key in ('f1', 'f2'):
        b = st[key]
        m = b.get('meta', {})
        if m.get('prog') not in qb.PROGRESSIONS or not m.get('demand'):
            prob.append('S%d %s prog/demand' % (st['num'], key))
        if key == 'f2' and not m.get('builds'):
            prob.append('S%d F2 builds' % st['num'])
        if b['std'] in main_before[st['num']] and b['std'] != st['std']:
            if m.get('prog') != 'cross-standard extension':
                prob.append('S%d %s %s is an earlier MAIN but not labeled cross-standard extension' % (st['num'], key, b['std']))
            else:
                applied.append((st['num'], key.upper(), b['std'], b['title'], m.get('demand')))
        if not b['std'].startswith('HS'):
            prob.append('S%d %s K-8 standard' % (st['num'], key))
        elif hs_courses.RANK[hs_courses.course_of(b['std'])] < hs_courses.RANK['Geometry']:
            prob.append('S%d %s %s earlier course' % (st['num'], key, b['std']))
check('Backward branches: metadata (obstacle, why, evidence; exact/supporting) and no circular prerequisites '
      '(K-8, Algebra I, or the MAIN of an EARLIER Geometry set)', [p for p in prob if ' B' in p or 'metadata' in p],
      'every backward standard points to an earlier course or an earlier set, so the prerequisite graph has no cycles')
check('Forward branches: progression type, new demand, FORWARD 2 relationship; never an earlier course or earlier MAIN',
      [p for p in prob if ' f1' in p or ' f2' in p or 'F2' in p], 'all FORWARD 1 / FORWARD 2 branches carry prog, demand (and builds for F2)')
progs = collections.Counter((k, st[k]['meta']['prog']) for st in SETS for k in ('f1', 'f2'))

# ---------------------------------------------------------------- 4. answer key
prob = []
for r in RECS:
    if not (r['correct_answer'] or '').strip():
        prob.append(r['id'] + ' empty answer')
    if not (r['grading_note'] or '').strip():
        prob.append(r['id'] + ' empty note')
    if r['type'] == 'mc':
        texts = [c['text'] for c in r['choices']]
        if len(texts) != 4 or len(set(map(norm, texts))) != 4:
            prob.append(r['id'] + ' choices')
        if r['correct_letter'] not in 'ABCD' or texts['ABCD'.index(r['correct_letter'])] != r['correct_answer']:
            prob.append(r['id'] + ' correct letter')
    if r['type'] == 'tf' and r['correct_answer'] not in ('True', 'False'):
        prob.append(r['id'] + ' tf')
    if r['type'] == 'work' and not r['required_method']:
        prob.append(r['id'] + ' work without method')
check('Answer key: every record has an answer and a grading note; MC has 4 distinct choices and one keyed letter; '
      'work items state the required method', prob, 'all %d records complete' % len(RECS))

tfc = collections.Counter(r['correct_answer'] for r in RECS if r['type'] == 'tf')
mcc = collections.Counter(r['correct_letter'] for r in RECS if r['type'] == 'mc')
prob = []
if abs(tfc['True'] - tfc['False']) > 0.1 * sum(tfc.values()):
    prob.append('T/F %s' % dict(tfc))
if max(mcc.values()) - min(mcc.values()) > 15:
    prob.append('MC %s' % dict(mcc))
check('Balance: True/False within 10%; MC letters A-D within 15 of each other', prob,
      'T/F: %d True, %d False. MC: %s' % (tfc['True'], tfc['False'], ', '.join('%s %d' % kv for kv in sorted(mcc.items()))))

prob = []
proof_like = [r for r in RECS if r['type'] == 'work' and r['answer_lines'] is not None and
              any(w in r['question'] for w in ('Prove', 'prove', 'Derive', 'derive'))]
for r in proof_like:
    if 'Essential' not in r['grading_note']:
        prob.append(r['id'] + ' proof note lacks Essential criteria')
check('Proofs and derivations: grading note lists essential criteria (and alternatives / invalid arguments where relevant)', prob,
      '%d proof or derivation questions' % len(proof_like))

prob = []
cons = [r for r in RECS if r['type'] == 'plot' and 'Compass and straightedge' in r['question']]
for r in cons:
    if 'construction marks' not in r['grading_note']:
        prob.append(r['id'])
check('Constructions: tools stated on the page and construction evidence graded', prob, '%d construction questions' % len(cons))

# ---------------------------------------------------------------- 5. duplicates and text
prob = []
by_set = collections.defaultdict(list)
for r in RECS:
    by_set[r['set']].append(r)
for n, rs in by_set.items():
    c = collections.Counter(norm(r['question']) for r in rs)
    for k, v in c.items():
        if v > 1:
            prob.append('S%d repeats "%s"' % (n, k[:60]))
glob_dups = [k for k, v in collections.Counter(norm(r['question']) for r in RECS).items() if v > 1]
bad_text = [r['id'] for r in RECS if '...' in r['question'] or '…' in r['question'] or '...' in (r['correct_answer'] or '')]
prob += ['text with ellipsis: ' + i for i in bad_text]
check('No repeated question within a set; no unfinished text', prob,
      'no repeats within a set; %d stems recur across different sets (review prompts reused as prerequisites)' % len(glob_dups))

prob = []
nfig = 0
for st in SETS:
    for key, _, _, qs, _ in build.sections(st):
        for i, q in enumerate(qs, 1):
            f = q.get('fig')
            if f and f.get('k') == 'gd':
                nfig += 1
                if not f.get('desc'):
                    prob.append('S%d %s Q%d' % (st['num'], key, i))
check('Every geometry diagram has a text description (accessibility and export)', prob, '%d geometry diagrams' % nfig)

# ---------------------------------------------------------------- 6. files agree
prob = []
rows = list(csv.DictReader(open(P['data'] + '.csv', encoding='utf-8-sig')))
if len(rows) != len(RECS):
    prob.append('CSV rows %d vs JSON %d' % (len(rows), len(RECS)))
for row, r in zip(rows, RECS):
    for k in ('uid', 'id', 'type', 'correct_answer', 'correct_letter', 'standard', 'section'):
        a = '' if r[k] is None else str(r[k])
        if row[k] != a:
            prob.append('%s %s' % (r['id'], k))
            break
check('Answer key JSON and CSV agree record by record', prob, '%d records' % len(rows))

prob = []
try:
    import fitz
    qd, kd = fitz.open(P['questions']), fitz.open(P['key'])
    if qd.page_count != kd.page_count:
        prob.append('page counts %d vs %d' % (qd.page_count, kd.page_count))
    for r in RECS:
        p = r['question_page'] - 1
        if 'ID %s' % r['id'] not in qd[p].get_text().replace('\n', ' '):
            prob.append('question page %d lacks %s' % (p + 1, r['id']))
        if 'ID %s' % r['id'] not in kd[r['answer_key_page'] - 1].get_text().replace('\n', ' '):
            prob.append('key page lacks %s' % r['id'])
    pages = qd.page_count
except ImportError:
    prob.append('pymupdf not installed')
    pages = 0
check('PDFs: one question per page; each ID is printed on its recorded question page and the matching answer-key page', prob,
      '%d pages in each PDF; all %d IDs found on their pages' % (pages, len(RECS)))

# ---------------------------------------------------------------- 7. stand-alone questions and re-solved answers
prob = []
ctx = re.compile(r'\b(the same (triangle|situation|circles?|figure|box|rectangle|tank)|(problem|question|figure|trunk|pile) above|'
                 r'previous (question|problem)|in Q\d|from Q\d|(in|for) the (ship|lighthouse|two-observer|dance floor) problem)\b', re.I)
for r in RECS:
    if ctx.search(r['question']):
        prob.append(r['id'])
    if re.search(r'\b(in the figure|as shown|shown in the|the diagram)\b', r['question'], re.I) and not r['has_figure']:
        prob.append(r['id'] + ' (mentions a figure it does not have)')
check('Every question stands alone (no reference to another question; no figure reference without a figure)', prob,
      'no cross-question references found')

import resolve  # noqa: E402
nq, nv, bad = resolve.run()
check('Independent re-solve: numeric and exact answers recomputed from the givens with separate code (resolve.py)', bad,
      '%d questions (%d values) recomputed; all agree with the key' % (nq, nv))

# ---------------------------------------------------------------- report
fails = [x for x in results if not x[1]]
types = collections.Counter(r['type'] for r in RECS)
secs = collections.Counter(('BACKWARD' if r['section'].startswith('BACKWARD') else r['section']) for r in RECS)
strands = collections.Counter(st.get('strand') for st in SETS)
align = collections.Counter(b['meta']['align'] for st in SETS for b in st['back'])
L = ['# Geometry validation results', '',
     'Generated by `geometry/src/validate.py` from the source sets and the generated files (version %s, %s).' % (
         DATA['collection']['version'], DATA['collection']['date']), '',
     '**Result: %s** (%d checks, %d failed).' % ('PASS' if not fails else 'FAIL', len(results), len(fails)), '',
     '| # | Check | Result | Detail |', '|---:|---|---|---|']
for i, (n, ok, d) in enumerate(results, 1):
    L.append('| %d | %s | %s | %s |' % (i, n, 'PASS' if ok else '**FAIL**', d.replace('|', '/')))
L += ['', '## Counts', '',
      '- Sets: %d (%d core, %d advanced extension (+))' % (len(SETS), strands['core'], strands['advanced']),
      '- Questions: %d — MAIN %d, BACKWARD %d, FORWARD 1 %d, FORWARD 2 %d' % (len(RECS), secs['MAIN'], secs['BACKWARD'], secs['FORWARD 1'], secs['FORWARD 2']),
      '- Backward branches: %d (%d exact, %d supporting)' % (sum(align.values()), align['exact'], align['supporting']),
      '- Question types: ' + ', '.join('%s %d' % kv for kv in sorted(types.items())),
      '- Forward progression types: ' + '; '.join('%s %s: %d' % (k.upper(), p, v) for (k, p), v in sorted(progs.items())),
      '- Geometry diagrams: %d' % nfig, '',
      '## Forward branches that apply a standard taught in an earlier set', '',
      'These branches use a Geometry standard that is the MAIN of an earlier set, at a higher demand (justifying a construction '
      'with a congruence or parallel-line proof, or applying a result in a modeling standard). They are labeled cross-standard '
      'extension, and the new demand is stated. The validator accepts this only with that label.', '',
      '| Set | Branch | Standard | Branch title | New demand |', '|---|---|---|---|---|'] + [
      '| S%d | %s | %s | %s | %s |' % a for a in applied] + ['']
out = os.path.join(build.GRADE_DIR, 'VALIDATION.md')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('\n'.join(L))
sys.exit(1 if fails else 0)
