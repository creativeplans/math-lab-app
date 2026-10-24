"""Algebra II collection validation: writes algebra2/VALIDATION.md and exits 1 if any check fails.

    python3 question-bank/algebra2/src/validate.py

Run after engine/build.py algebra2. Checks the source sets (structure, coverage, branch rules, metadata, figures) and the
generated files (answer key JSON and CSV, both PDFs page by page), then runs the independent re-solve.
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

build.load_grade('algebra2')
import standards  # noqa: E402  (algebra2/src, on the path after load_grade)

HOME = 'Algebra II'
CORE, ADV = hs_courses.ALGEBRA_II_CORE, hs_courses.ALGEBRA_II_ADVANCED
SETS = list(build.all_sets())
P = build.out_paths()
DATA = json.load(open(P['data'] + '.json', encoding='utf-8'))
RECS = DATA['questions']
results = []


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
for dup in [k for k, v in collections.Counter(ids).items() if v > 1]:
    prob.append('duplicate id ' + dup)
for dup in [k for k, v in collections.Counter(r['uid'] for r in RECS).items() if v > 1]:
    prob.append('duplicate uid ' + dup)
pat = re.compile(r'^S(\d+)-(M|B\d|F1|F2)-Q([1-5])$')
for r in RECS:
    m = pat.match(r['id'])
    if not m or int(m.group(1)) != r['set'] or r['uid'] != 'A2:' + r['id']:
        prob.append('bad id ' + r['id'])
if len(RECS) != sum(5 * len(build.sections(st)) for st in SETS):
    prob.append('record count')
check('IDs unique, well formed, namespaced (A2:), one record per question', prob, '%d questions, %d unique IDs' % (len(RECS), len(set(ids))))

# ---------------------------------------------------------------- 2. coverage
prob = []
main_codes = collections.defaultdict(list)
for st in SETS:
    main_codes[st['std']].append(st['num'])
    if (st['std'] in ADV) != (st.get('strand') == 'advanced'):
        prob.append('S%d strand %s does not match %s' % (st['num'], st.get('strand'), st['std']))
    if st['std'] not in CORE + ADV:
        prob.append('S%d MAIN %s is not in the course profile' % (st['num'], st['std']))
for code in CORE + ADV:
    if not main_codes.get(code):
        prob.append('no MAIN set for ' + code)
    if code not in standards.STANDARDS:
        prob.append(code + ' missing from the standards inventory')
check('Every profile standard (CORE and ADVANCED EXTENSION) has a MAIN set; strand matches the profile', prob,
      '%d CORE and %d ADVANCED standards, each with at least one MAIN set' % (len(CORE), len(ADV)))

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

# MAIN response types follow the verb of the subskill
prob, verbs = [], []
subs_all = {sid: d for _c, (_t, ss) in standards.STANDARDS.items() for sid, d in ss}
main_types = collections.defaultdict(list)
for r in RECS:
    if r['section'] == 'MAIN':
        main_types[r['set']].append(r['type'])
for st in SETS:
    types = main_types[st['num']]
    if 'tf' in types:
        prob.append('S%d MAIN has a true/false item' % st['num'])
    desc = ' '.join(subs_all[c] for c in st['covers']).replace('REVISIT with nonlinear families: ', '').replace('REVISIT: ', '')
    verb = desc.split()[0].lower()
    mains = [r for r in RECS if r['section'] == 'MAIN' and r['set'] == st['num']]
    if verb in ('prove', 'derive', 'explain', 'choose'):
        # reasoning sets: selected or short written responses only; every multiple-choice item weighs a valid argument
        # against flawed ones, and its note says what is wrong with the others
        for r in mains:
            if r['type'] not in ('mc', 'sa'):
                prob.append('%s %s set item is %s' % (r['id'], verb, r['type']))
            elif r['type'] == 'mc' and 'The others' not in r['grading_note']:
                prob.append('%s note does not explain the other choices' % r['id'])
    if verb == 'graph' or desc.lower().startswith('graph'):
        # graph sets: five "Which graph" items, each with four candidate graphs (A-D) in one figure
        for r in mains:
            fd = r['figure_data'] or {}
            panels = [g for row in fd.get('figs', []) for g in row.get('figs', [])]
            if r['type'] != 'mc' or not r['correct_answer'].startswith('Graph ') or [g.get('tag') for g in panels] != list('ABCD'):
                prob.append('%s graph set item is not a four-graph choice' % r['id'])
    if verb in ('prove', 'derive', 'explain', 'choose', 'graph'):
        verbs.append('S%d %s: %s' % (st['num'], verb, '/'.join(types)))
check('MAIN response types: no true/false in any MAIN; "prove", "derive", "explain" and "choose" sets use only multiple choice '
      '(a valid argument against flawed ones, with every other choice explained in the note) or short answers; "graph" sets use '
      'five "Which graph" items with four labeled candidate graphs', prob,
      '%d sets checked; verb sets: %s' % (len(SETS), '; '.join(verbs)))

# ---------------------------------------------------------------- 3. branches
prob = []
seen, main_before = set(), {}
applied = []
for st in SETS:
    main_before[st['num']] = set(seen)
    seen.add(st['std'])
rank = hs_courses.RANK
for st in SETS:
    for i, b in enumerate(st['back'], 1):
        m, code = b.get('meta', {}), b['std']
        if not m.get('why') or m.get('align') not in ('exact', 'supporting') or not all(w in m['why'] for w in ('Obstacle', 'Why it matters', 'Evidence')):
            prob.append('S%d B%d metadata' % (st['num'], i))
        if code.startswith('HS'):
            crs = hs_courses.placement(code, 'backward')
            if crs == HOME:
                if code not in main_before[st['num']]:
                    prob.append('S%d B%d %s is not the MAIN of an earlier set' % (st['num'], i, code))
            elif rank[crs] > rank[HOME]:
                prob.append('S%d B%d %s is a later course (%s)' % (st['num'], i, code, crs))
        elif not re.match(r'^([K1-8])\.', code):
            prob.append('S%d B%d %s unknown source' % (st['num'], i, code))
    for key in ('f1', 'f2'):
        b = st[key]
        m = b.get('meta', {})
        if m.get('prog') not in qb.PROGRESSIONS or not m.get('demand'):
            prob.append('S%d %s prog/demand' % (st['num'], key))
        if key == 'f2' and not m.get('builds'):
            prob.append('S%d F2 builds' % st['num'])
        crs = hs_courses.placement(b['std'], 'forward') if b['std'].startswith('HS') else None
        if crs is None or rank[crs] < rank[HOME]:
            prob.append('S%d %s %s is not Algebra II or later' % (st['num'], key, b['std']))
        if b['std'] == st['std'] and m.get('prog') != 'same-course deepening':
            prob.append('S%d %s same standard but %s' % (st['num'], key, m.get('prog')))
        if crs and crs != HOME and m.get('prog') != 'later-course extension':
            prob.append('S%d %s %s is %s but labeled %s' % (st['num'], key, b['std'], crs, m.get('prog')))
        if b['std'] in main_before[st['num']] and b['std'] != st['std']:
            applied.append((st['num'], key.upper(), b['std'], b['title'], m.get('demand')))
check('Backward branches: metadata (obstacle, why it matters, evidence; exact/supporting) and no circular prerequisites '
      '(K-8, Algebra I, Geometry, or the MAIN of an EARLIER Algebra II set)', [p_ for p_ in prob if ' B' in p_ or 'metadata' in p_],
      'every backward standard points to an earlier course or an earlier set, so the prerequisite graph has no cycles')
check('Forward branches: progression type consistent with placement (same standard = same-course deepening; later course = '
      'later-course extension), new demand stated, FORWARD 2 states how it builds on FORWARD 1; never an earlier course',
      [p_ for p_ in prob if ' f1' in p_ or ' f2' in p_ or 'F2' in p_], 'all forward branches consistent')
progs = collections.Counter((k, st[k]['meta']['prog']) for st in SETS for k in ('f1', 'f2'))

# ---------------------------------------------------------------- 4. answer key
prob = []
for r in RECS:
    if not (r['correct_answer'] or r['drawing_answer'] or '').strip():
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
reasoning = [r for r in RECS if r['type'] == 'mc' and re.match(r'(Which (argument|derivation|work verifies|explanation|statement correctly '
                                                               r'explains|unit-circle)|Why |How does|Is .* an identity)', r['question'])]
for r in reasoning:
    if 'The others' not in r['grading_note']:
        prob.append(r['id'])
check('Proofs, derivations, verifications and explanations (as multiple choice): the grading note says why the keyed argument is '
      'valid and what is wrong with each other choice', prob, '%d such questions' % len(reasoning))

prob = []
need_excl = [r for r in RECS if r['section'] == 'MAIN' and re.search(r'excluded values', r['question'])]
for r in need_excl:
    lines = [l for l in r['answer_lines'] or [] if 'xcluded' in l]
    parts = r['correct_answer'].split(';')
    if lines and len(parts) == len(r['answer_lines']):  # a labeled "Excluded values:" line: its key part must list them
        part = parts[r['answer_lines'].index(lines[0])].strip()
        if not re.fullmatch(r'\{[^{}]+\}|-?[\d/]+|none', part):
            prob.append(r['id'])
    elif not re.search(r'x ≠|no excluded|none', r['correct_answer']):
        prob.append(r['id'])
ext = [r for r in RECS if re.search(r'extraneous', r['question'], re.I) and r['section'] == 'MAIN']
for r in ext:
    if 'extraneous' not in (r['correct_answer'] + ' '.join(r['answer_lines'] or [])).lower():
        prob.append(r['id'] + ' extraneous not addressed')
check('Domains: MAIN items that ask for excluded values state them in the key; MAIN items that ask about extraneous solutions '
      'name them (or "none extraneous")', prob, '%d excluded-value items, %d extraneous-solution items' % (len(need_excl), len(ext)))

# ---------------------------------------------------------------- 5. duplicates and text
prob = []
by_set = collections.defaultdict(list)
for r in RECS:
    by_set[r['set']].append(r)
for nset, rs in by_set.items():
    for k_, v_ in collections.Counter(norm(r['question']) for r in rs).items():
        if v_ > 1:
            prob.append('S%d repeats "%s"' % (nset, k_[:60]))
glob_dups = [k_ for k_, v_ in collections.Counter(norm(r['question']) for r in RECS).items() if v_ > 1]
SERIES = re.compile(r'\+ \.\.\.|\.\.\. \+|, \.\.\.')
prob += ['text with ellipsis: ' + r['id'] for r in RECS if '…' in r['question'] or '…' in (r['correct_answer'] or '')
         or any('...' in t_ and not SERIES.search(t_) for t_ in (r['question'], r['correct_answer'] or ''))]
check('No repeated question within a set; no unfinished text (series written "a + ar + ..." are allowed)', prob,
      'no repeats within a set; %d stems recur across different sets (review prompts reused as prerequisites)' % len(glob_dups))

prob = []
nfig = 0
for st in SETS:
    for key, _, _, qs, _ in build.sections(st):
        for i, q in enumerate(qs, 1):
            f = q.get('fig')
            if f and f.get('k') in ('coord', 'hist'):
                nfig += 1
                if f.get('k') == 'coord' and not f.get('desc'):
                    prob.append('S%d %s Q%d' % (st['num'], key, i))
check('Every coordinate graph or grid has a text description (accessibility and export)', prob, '%d graphs, grids, and histograms' % nfig)

# ---------------------------------------------------------------- 6. files agree
prob = []
rows = list(csv.DictReader(open(P['data'] + '.csv', encoding='utf-8-sig')))
if len(rows) != len(RECS):
    prob.append('CSV rows %d vs JSON %d' % (len(rows), len(RECS)))
for row, r in zip(rows, RECS):
    for k_ in ('uid', 'id', 'type', 'correct_answer', 'correct_letter', 'standard', 'section'):
        a_ = '' if r[k_] is None else str(r[k_])
        if row[k_] != a_:
            prob.append('%s %s' % (r['id'], k_))
            break
check('Answer key JSON and CSV agree record by record', prob, '%d records' % len(rows))

prob = []
import fitz  # noqa: E402  (PyMuPDF)
qd, kd = fitz.open(P['questions']), fitz.open(P['key'])
if qd.page_count != kd.page_count:
    prob.append('page counts %d vs %d' % (qd.page_count, kd.page_count))
for r in RECS:
    if 'ID %s' % r['id'] not in qd[r['question_page'] - 1].get_text().replace('\n', ' '):
        prob.append('question page lacks %s' % r['id'])
    if 'ID %s' % r['id'] not in kd[r['answer_key_page'] - 1].get_text().replace('\n', ' '):
        prob.append('key page lacks %s' % r['id'])
check('PDFs: one question per page; each ID is printed on its recorded question page and the matching answer-key page', prob,
      '%d pages in each PDF; all %d IDs found on their pages' % (qd.page_count, len(RECS)))

# ---------------------------------------------------------------- 7. stand-alone questions and re-solved answers
prob = []
ctx = re.compile(r'\b(previous (question|problem)|(problem|question) above|in Q\d|from Q\d|in this branch)\b', re.I)
for r in RECS:
    if ctx.search(r['question']):
        prob.append(r['id'])
    if re.search(r'\b(is shown|are shown|the (graph|table|histogram|figure) (shows|below|above))\b', r['question'], re.I) and not r['has_figure']:
        prob.append(r['id'] + ' (mentions a figure or table it does not have)')
check('Every question stands alone (no reference to another question; every "shown" graph, table, or histogram is on the page)', prob,
      'no cross-question references found')

import resolve  # noqa: E402
nq, nv, bad = resolve.run()
check('Independent re-solve: computable answers recomputed from the givens with separate code (resolve.py, sympy)', bad,
      '%d questions (%d values) recomputed; all agree with the key' % (nq, nv))

prob = []
for r in RECS:
    if r['strand'] not in ('core', 'advanced extension (+)'):
        prob.append(r['id'] + ' strand')
    if r['section'] == 'MAIN' and r['set_standard'] in ADV and 'Advanced Extension' not in r['course_level']:
        prob.append(r['id'] + ' advanced label')
    if r['standard'].startswith('HS') and (re.search(r'\bGrade\b', r['course_level'] or '') or re.search(r'\bGrade \d', r['grade'] or '')):
        prob.append(r['id'] + ' grade label')
check('Labels: every record has strand core/advanced, the MAIN records of ADVANCED EXTENSION sets are labeled as such, and course-placement labels '
      '(high-school codes never carry a grade level; K-8 prerequisite codes keep their official grade-level standard label)', prob, 'all records labeled by course placement')

prob = [r['id'] + ' ' + r['type'] for r in RECS if r['type'] not in ('sa', 'mc', 'tf')]
check('No question needs a person or a drawing surface to grade: every item is short answer, multiple choice, or true/false '
      '(no shown-work, drawing, or drawing-plus-writing items)', prob,
      'all %d questions: %s' % (len(RECS), ', '.join('%s %d' % kv for kv in sorted(collections.Counter(r['type'] for r in RECS).items()))))

prob = []
by_sec = collections.Counter(r['section'].split()[0] for r in RECS)
if by_sec['MAIN'] != 5 * len(SETS) or by_sec['FORWARD'] != 10 * len(SETS) or DATA['question_count'] != len(RECS):
    prob.append('totals %s' % dict(by_sec))
check('Totals recalculated three ways (source sets, key records, key header) and by section', prob,
      '%d questions = %d sets × 5 MAIN + %d backward branches × 5 + %d sets × 10 forward' % (
          len(RECS), len(SETS), sum(len(st['back']) for st in SETS), len(SETS)))

# ---------------------------------------------------------------- 9. game answer checker contract
# Runs the Untangle The Nexus short-answer checker (its own code, packages/curriculum/src/answers.ts) on every short answer.
# NEXUS_DIR names the game repository (default /home/user/untangle-the-nexus); without it the check fails as NOT RUN.
import subprocess  # noqa: E402
import tempfile  # noqa: E402
NEXUS = os.environ.get('NEXUS_DIR', '/home/user/untangle-the-nexus')
# Rewrites the checker rejects on purpose: the question names a form, so the other order is not that form.
REWRITE_OK = {'S1-M-Q4': 'the question asks for the form a + bi, so (5√3/2)i - 2 is not in that form'}
prob, contract = [], None
if os.path.exists(os.path.join(NEXUS, 'packages', 'curriculum', 'src', 'answers.ts')):
    out = os.path.join(tempfile.mkdtemp(), 'contract.json')
    run = subprocess.run(['npx', 'tsx', os.path.join(HERE, 'tools', 'checker_contract.ts'), P['data'] + '.json', out],
                         cwd=NEXUS, capture_output=True, text=True)
    if run.returncode or not os.path.exists(out):
        prob.append('NOT RUN: checker script failed: ' + run.stderr.strip()[-300:])
    else:
        contract = json.load(open(out, encoding='utf-8'))
        for r_ in contract:
            if not r_['auto']:
                prob.append(r_['id'] + ' not automatically checkable')
            elif not r_['self']:
                prob.append(r_['id'] + ' key not accepted by the checker')
            elif r_['rejected'] and r_['id'] not in REWRITE_OK:
                prob.append(r_['id'] + ' equivalent rewrite rejected: ' + '; '.join(r_['rejected']))
else:
    prob.append('NOT RUN: game repository not found (set NEXUS_DIR)')
check('Game answer checker: every short answer is automatically checkable by the Untangle The Nexus checker, its key is accepted '
      'as a response, and the same answer without spaces or with its terms in reverse order is accepted', prob,
      '%d short answers checked with the game\'s answer checker; documented form exceptions: %s' % (
          len(contract or []), '; '.join('%s (%s)' % kv for kv in REWRITE_OK.items())))

# ---------------------------------------------------------------- 10. word answers and clean keys
WORDS = {'yes', 'no', 'none', 'positive', 'negative', 'odd', 'even', 'neither', 'open', 'closed', 'clockwise',
         'counterclockwise', 'touches', 'crosses', 'growth', 'decay', 'i', 'ii', 'iii', 'iv'}
prob = []
for r in RECS:
    if r['type'] != 'sa':
        continue
    parts = [p_.strip() for p_ in r['correct_answer'].split(';')]
    text = r['question'] + ' ' + ' '.join(r['answer_lines'] or [])
    if len(parts) > 1 and len(parts) != len(r['answer_lines'] or []):
        prob.append(r['id'] + ' parts do not match answer lines')
    for p_ in parts:
        if re.search(r'≈|\babout\b|for example|\(that is|\be\.g\.', p_, re.I):
            prob.append('%s key part "%s" contains commentary' % (r['id'], p_))
        if re.fullmatch(r'[A-Za-z]+', p_) and len(p_) > 1 or p_.lower() in WORDS:
            if p_.lower() not in WORDS:
                prob.append('%s word key "%s" is not an allowed word answer' % (r['id'], p_))
            elif not (re.search(r'\b%s\b' % re.escape(p_), text, re.I) and re.search(r'\bor\b|enter none', text)):
                prob.append('%s word key "%s" is not listed as an option in the question' % (r['id'], p_))
check('Short-answer keys: no commentary inside a key; one key part per answer line; a word answer is one of a closed set of words '
      'that the question itself lists as the options', prob, 'all %d short answers' % sum(1 for r in RECS if r['type'] == 'sa'))

# ---------------------------------------------------------------- 11. length cue in multiple choice
prob, longest, textmc = [], 0, 0
for r in RECS:
    if r['type'] != 'mc' or r['choices'][0]['text'] == 'Graph A':
        continue
    textmc += 1
    lens = [len(c['text']) for c in r['choices']]
    k = 'ABCD'.index(r['correct_letter'])
    srt = sorted(lens)
    if lens[k] == max(lens) and lens.count(max(lens)) == 1:
        longest += 1
        if srt[-1] > 1.3 * srt[-2] and srt[-1] >= 40:
            prob.append('%s correct choice %d characters, next longest %d' % (r['id'], srt[-1], srt[-2]))
check('Multiple choice length cue: the correct choice is never much longer than every other choice (more than 30% longer, '
      'for choices of 40 characters or more)', prob,
      'no strong length cue; the correct choice is the uniquely longest in %d of %d text multiple-choice items (%.0f%%; 25%% '
      'would be chance)' % (longest, textmc, 100.0 * longest / max(textmc, 1)))

SCOPE = [
    'Automatic, every set: counts sections and questions in the source.',
    'Automatic, every record: ID pattern, uniqueness, uid prefix.',
    'Automatic: standard codes against the course profile. Does not judge whether a question fits its standard.',
    'Automatic: covers= tags against the subskill list. Whether the questions measure the subskill was judged by reading.',
    'Automatic: MAIN question types and figures against the subskill verb. Whether a choice item measures the reasoning or graphing skill, and the comparability of difficulty, were judged by reading.',
    'Automatic: placement of backward codes, so the routing graph is acyclic. Logical dependencies inside proofs were reviewed by hand.',
    'Automatic: metadata present and consistent with placement. The quality of the stated new demand was judged by reading.',
    'Automatic: fields present and well formed. Correctness is covered by check 17 and by the manual read-through.',
    'Automatic counts.',
    'Automatic: looks for "The others" in the notes of reasoning items. That each keyed argument is valid and each other choice is flawed was checked by reading.',
    'Automatic pattern search on MAIN stems and keys; other sections were read by hand.',
    'Automatic: exact-text repeats within a set and unfinished text.',
    'Automatic: every coordinate figure has desc text. Whether the picture matches the text was checked by rendering every figure page.',
    'Automatic, every record and listed field.',
    'Automatic: searches each PDF page\'s text for its ID. Layout quality was checked by rendering every figure page.',
    'Automatic phrase search. Missing givens that the phrases do not catch were looked for in the read-through.',
    'Automatic, %d of %d questions: recomputes listed answers with separate code. All other questions were solved by hand by the author '
    '(see Manual review for what was re-read in each version).' % (nq, len(RECS)),
    'Automatic, every record.',
    'Automatic, every record: response type. Whether the game accepts each short answer is check 21.',
    'Automatic arithmetic on the generated files.',
    'Automatic, every short answer, using the game\'s own checker code (algebra2/src/tools/checker_contract.ts). It does not '
    'cover every way a student might write an answer; it is not a test in the live game.',
    'Automatic pattern rules on every short-answer key and its question text.',
    'Automatic, every multiple-choice item except the four-graph items (whose choices are the fixed labels Graph A to D).',
]
assert len(SCOPE) == len(results), (len(SCOPE), len(results))

fails = [x_ for x_ in results if not x_[1]]
types = collections.Counter(r['type'] for r in RECS)
secs = collections.Counter(('BACKWARD' if r['section'].startswith('BACKWARD') else r['section']) for r in RECS)
strands = collections.Counter(st.get('strand') for st in SETS)
align = collections.Counter(b['meta']['align'] for st in SETS for b in st['back'])
L = ['# Algebra II validation results', '',
     'Generated by `algebra2/src/validate.py` from the source sets and the generated files (version %s, %s).' % (
         DATA['collection']['version'], DATA['collection']['date']), '',
     '**Result: %s** (%d checks, %d failed).' % ('PASS' if not fails else 'FAIL', len(results), len(fails)), '',
     'PASS means only that the automatic test found no problem within the scope stated in its row. These checks ran on the content '
     'files. They are not a test in the live game or with the AI grader.', '',
     '| # | Check | Result | Detail | Scope (what the check covers) |', '|---:|---|---|---|---|']
for i, ((nm, ok, dt), sc) in enumerate(zip(results, SCOPE), 1):
    L.append('| %d | %s | %s | %s | %s |' % (i, nm, 'PASS' if ok else '**FAIL**', dt.replace('|', '/'), sc))
L += ['', '## Counts', '',
      '- Sets: %d (%d core, %d advanced extension (+))' % (len(SETS), strands['core'], strands['advanced']),
      '- Questions: %d — MAIN %d, BACKWARD %d, FORWARD 1 %d, FORWARD 2 %d' % (len(RECS), secs['MAIN'], secs['BACKWARD'], secs['FORWARD 1'], secs['FORWARD 2']),
      '- Backward branches: %d (%d exact, %d supporting)' % (sum(align.values()), align['exact'], align['supporting']),
      '- Question types: ' + ', '.join('%s %d' % kv for kv in sorted(types.items())),
      '- Forward progression types: ' + '; '.join('%s %s: %d' % (k_.upper(), p_, v_) for (k_, p_), v_ in sorted(progs.items())),
      '- Figures: %d questions' % sum(1 for r in RECS if r['has_figure']), '',
      '## Forward branches that apply a standard taught in an earlier set', '',
      '| Set | Branch | Standard | Branch title | New demand |', '|---|---|---|---|---|'] + [
      '| S%d | %s | %s | %s | %s |' % a_ for a_ in applied] + ['']
import review_log  # noqa: E402
L += review_log.markdown(resolve.CASES, RECS)
out = os.path.join(build.GRADE_DIR, 'VALIDATION.md')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('\n'.join(L[:40]))
sys.exit(1 if fails else 0)
