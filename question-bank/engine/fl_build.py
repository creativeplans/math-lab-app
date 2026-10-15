"""Build the Financial Literacy collection: validate, assign answer letters, write the keys, PDFs, the Untangle The
Nexus import package, and the reports.

    python3 question-bank/engine/fl_build.py            # everything
    python3 question-bank/engine/fl_build.py --quick    # validate and write keys/package only (no PDFs)
"""
import csv
import glob
import hashlib
import importlib
import json
import os
import re
import shutil
import sys

ENGINE = os.path.dirname(os.path.abspath(__file__))
QB = os.path.dirname(ENGINE)
COL = os.path.join(QB, 'financial_literacy')
SRC = os.path.join(COL, 'src')
OUT_PKG = os.path.join(QB, 'nexus', 'financial_literacy')
sys.path[:0] = [ENGINE, SRC]

import fl_dsl as D  # noqa: E402
import fl_meta as META  # noqa: E402
import fl_ledger as LEDGER  # noqa: E402

VERSION = META.VERSION
CATALOG = json.load(open(os.path.join(ENGINE, 'fl_math_catalog.json')))['skills']
COURSE_PREFIX = {'grade_3': 'G3', 'grade_4': 'G4', 'grade_5': 'G5', 'grade_6': 'G6', 'grade_7': 'G7', 'grade_8': 'G8',
                 'algebra_1': 'ALG1'}
L = 'ABCD'
NUM_RE = re.compile(r'^[−-]?\$?[−-]?\d[\d,]*(\.\d+)?%?$')


def load():
    for f in sorted(glob.glob(os.path.join(SRC, 'u[0-9][0-9]*.py'))):
        importlib.import_module(os.path.basename(f)[:-3])
    return D.SETS


def num_of(text, pick=0):
    ms = list(re.finditer(r'[−-]?\$?[−-]?(\d[\d,]*(?:\.\d+)?)', text))
    if not ms:
        return None, 0
    m = ms[pick] if -len(ms) <= pick < len(ms) else ms[0]
    s = m.group(1).replace(',', '')
    v = float(s)
    if re.match(r'[−-]', m.group(0)) or '$-' in m.group(0) or '$−' in m.group(0):
        v = -v
    return v, len(s.split('.')[1]) if '.' in s else 0


def is_numeric(texts):
    return all(NUM_RE.match(t) for t in texts)


# ------------------------------------------------------------------ validation
PROBLEMS = []


def check_calc(qid, qd):
    if qd['calc'] is None:
        return
    rv, dp = num_of(qd['right'], qd['pick'])
    if rv is None:
        PROBLEMS.append(f'{qid}: calc given but the correct choice shows no number')
        return
    tol = qd['tol'] if qd['tol'] is not None else 0.5 * 10 ** (-dp) + 1e-9
    if abs(qd['calc'] - rv) > tol:
        PROBLEMS.append(f'{qid}: correct choice {qd["right"]!r} does not match the recomputed value {qd["calc"]}')
    for w, _ in ([] if qd['shared'] else qd['wrong']):
        wv, wdp = num_of(w, qd['pick'])
        if wv is not None and abs(qd['calc'] - wv) <= (qd['tol'] if qd['tol'] is not None else 0.5 * 10 ** (-wdp) + 1e-9):
            PROBLEMS.append(f'{qid}: wrong choice {w!r} also equals the recomputed value {qd["calc"]}')


def validate(sets):
    nums = [s['num'] for s in sets]
    assert len(nums) == len(set(nums)), 'duplicate set numbers'
    prompts = {}
    for s in sets:
        for sec_code, sec in sections(s):
            if sec.get('kind') == 'math':
                r = sec['ref']
                sid = '%s-S%02d-M' % (COURSE_PREFIX[r['course']], r['set'])
                if sid not in CATALOG:
                    PROBLEMS.append(f'S{s["num"]} {sec_code}: math link {sid} is not a MAIN skill in the game')
                continue
            for i, qd in enumerate(sec['qs'], 1):
                qid = f'S{s["num"]}-{sec_code}-Q{i}'
                check_calc(qid, qd)
                key = re.sub(r'\s+', ' ', qd['stem'].lower())
                if key in prompts:
                    PROBLEMS.append(f'{qid}: same question text as {prompts[key]}')
                prompts[key] = qid
    # a math link may appear only once per set
    for s in sets:
        refs = [(b['ref']['course'], b['ref']['set']) for b in s['back'] if b['kind'] == 'math']
        if len(refs) != len(set(refs)):
            PROBLEMS.append(f'S{s["num"]}: the same math link is listed twice')


def sections(s):
    """(code, section) in package order: M, B1..Bn (backward, in the order a student works them), F1..Fn."""
    out = [('M', dict(skill=s['skill'], qs=s['main']))]
    out += [('B%d' % i, b) for i, b in enumerate(s['back'], 1)]
    out += [('F%d' % i, f) for i, f in enumerate(s['go'], 1)]
    return out


# ------------------------------------------------------------------ answer letters
_F = json.load(open(os.path.join(SRC, 'review', 'choice_order_v1.0.0.json')))
FROZEN = _F['order']
FROZEN_RIGHT = {r['id']: r['correct_answer'] for r in json.load(open(os.path.join(SRC, 'review', 'key_v1.0.0_full.json')))}


def assign_letters(sets):
    """Numeric choices are shown in increasing order (their letter follows from the values). Other questions place
    the correct choice in the least-used letter so far (ties broken by a hash of the id), so the key is balanced."""
    counts = dict.fromkeys(L, 0)
    plan = {}
    allq = [(f'S{s["num"]}-{c}-Q{i}', qd) for s in sets for c, sec in sections(s) if sec.get('kind') != 'math'
            for i, qd in enumerate(sec['qs'], 1)]
    for qid, qd in allq:
        texts = [qd['right']] + [w for w, _ in qd['wrong']]
        if is_numeric(texts) and not qd['keep_order']:
            order = sorted(texts, key=lambda t: num_of(t)[0])
            plan[qid] = order
            counts[L[order.index(qd['right'])]] += 1
    for qid, qd in allq:
        if qid in plan:
            continue
        wrongs = [w for w, _ in qd['wrong']]
        old = FROZEN.get(qid)
        if old and not qd['keep_order']:
            # Keep v1.0.0 positions: same choices -> same order; changed choices -> correct answer keeps its letter.
            if sorted(old) == sorted([qd['right']] + wrongs):
                order = old
            else:
                pos = next((i for i, t in enumerate(old) if t == FROZEN_RIGHT[qid]), 0)
                order = wrongs[:pos] + [qd['right']] + wrongs[pos:]
        elif qd['keep_order']:
            order = [qd['right']] + wrongs
        else:
            h = int(hashlib.md5(qid.encode()).hexdigest(), 16)
            low = min(counts.values())
            cands = [x for x in L if counts[x] == low]
            pos = L.index(cands[h % len(cands)])
            order = wrongs[:pos] + [qd['right']] + wrongs[pos:]
        plan[qid] = order
        counts[L[order.index(qd['right'])]] += 1
    return plan, counts


# ------------------------------------------------------------------ records
def build_records(sets, plan):
    recs, page = [], 0
    set_pages = {}
    for s in sets:
        page += 1  # set overview page
        set_pages[s['num']] = page
        for code, sec in sections(s):
            if sec.get('kind') == 'math':
                continue
            for i, qd in enumerate(sec['qs'], 1):
                page += 1
                qid = f'S{s["num"]}-{code}-Q{i}'
                order = plan[qid]
                letter = L[order.index(qd['right'])]
                mis = {L[order.index(w)]: m for w, m in qd['wrong']}
                rel = 'main' if code == 'M' else 'backward' if code[0] == 'B' else 'forward%s' % code[1:]
                recs.append(dict(
                    id=qid, uid='FL:' + qid, page=page, set=s['num'], set_title=s['title'], unit=s['unit']['code'],
                    unit_title=s['unit']['title'], section=code, relation=rel,
                    section_kind='main' if code == 'M' else ('concept' if code[0] == 'B' else 'go_deeper'),
                    section_skill=sec['skill'], number=i,
                    question_type='instruction' if qd['intro'] else 'knowledge_check',
                    how_to=bool(qd['how']), subtopic=qd['sub'] or sec['skill'],
                    intro=qd['intro'], question=qd['stem'],
                    choices=[dict(letter=L[j], text=t) for j, t in enumerate(order)],
                    correct_letter=letter, correct_answer=qd['right'], misconceptions=mis, feedback=qd['fb'],
                    calc=qd['calc'], effective_date=qd['eff'], standard=outcome_code(s)))
    return recs, set_pages


def outcome_code(s):
    return 'FL.%s.%02d' % (s['unit']['code'], s['num'])


# ------------------------------------------------------------------ keys
def write_keys(recs):
    os.makedirs(COL, exist_ok=True)
    key = dict(title='Financial Literacy — Answer Key', collection=dict(id='FL', course='Financial Literacy', version=VERSION,
               date=META.DATE), question_count=len(recs),
               id_format='S<set>-<section>-Q<n>; section M = MAIN, B<n> = backward concept branch, F<n> = Go Deeper <n>. '
                         'uid = "FL:" + id.', questions=recs)
    json.dump(key, open(os.path.join(COL, 'FinancialLiteracy_Answer_Key.json'), 'w'), indent=1, ensure_ascii=False)
    cols = ['id', 'uid', 'page', 'set', 'set_title', 'unit', 'section', 'relation', 'section_skill', 'number',
            'question_type', 'how_to', 'correct_letter', 'correct_answer', 'A', 'B', 'C', 'D', 'misconception_A',
            'misconception_B', 'misconception_C', 'misconception_D', 'feedback', 'effective_date']
    with open(os.path.join(COL, 'FinancialLiteracy_Answer_Key.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in recs:
            ch = {c['letter']: c['text'] for c in r['choices']}
            w.writerow([r['id'], r['uid'], r['page'], r['set'], r['set_title'], r['unit'], r['section'], r['relation'],
                        r['section_skill'], r['number'], r['question_type'], 'yes' if r['how_to'] else '',
                        r['correct_letter'], r['correct_answer'], ch['A'], ch['B'], ch['C'], ch['D'],
                        *[r['misconceptions'].get(x, '') for x in L], r['feedback'], r['effective_date'] or ''])


# ------------------------------------------------------------------ package
def src_strings(s):
    return ['%s: %s (%s)' % (x['org'], x['claim'], x['url']) for x in s['sources']]


def write_package(sets, recs, set_pages):
    if os.path.isdir(OUT_PKG):
        shutil.rmtree(OUT_PKG)
    os.makedirs(os.path.join(OUT_PKG, 'sets'))
    by_id = {r['id']: r for r in recs}
    index_sets = []
    for s in sets:
        std = outcome_code(s)
        secs = []
        for code, sec in sections(s):
            rel = 'main' if code == 'M' else 'backward' if code[0] == 'B' else 'forward%s' % code[1:]
            base = dict(section=code, section_code=code, relation=rel, skill=sec['skill'], standard=std, nearest_related=False,
                        alignment_role=META.SECTION_ROLE[rel.rstrip('0123456789')])
            if sec.get('kind') == 'math':
                r = sec['ref']
                sid = '%s-S%02d-M' % (COURSE_PREFIX[r['course']], r['set'])
                c = CATALOG[sid]
                secs.append(dict(base, kind='math', relationship=sec['why'], ref=dict(course=r['course'], set=r['set'], section='M'),
                                 ref_skill=dict(skill_id=sid, standard=c['ccss'], name=c['name']), questions=[]))
                continue
            qs = []
            for i in range(1, 6):
                r = by_id[f'S{s["num"]}-{code}-Q{i}']
                qq = dict(id=r['id'], uid=r['uid'], collection='FL', number=i, type='mc', standard=std, standard_grade='HS',
                          standard_course='Financial Literacy', domain=s['unit']['title'], prompt=r['question'],
                          choices=r['choices'], correct_letter=r['correct_letter'], correct_answer=r['correct_answer'],
                          answer_lines=[], grading_note='', figure=None)
                if r['intro']:
                    qq['intro'] = r['intro']
                qq.update(feedback=r['feedback'], question_type=r['question_type'], topic=s['title'], subtopic=r['subtopic'],
                          misconceptions=r['misconceptions'], practical_how_to=r['how_to'],
                          sources=src_strings(s) or ['Hypothetical example; no changing rule is used.'],
                          effective_date=r['effective_date'] or (META.DATE if s['status'] == 'time_sensitive' else None),
                          page=r['page'])
                qs.append(qq)
            if code == 'M':
                secs.append(dict(base, questions=qs))
            elif code[0] == 'B':
                secs.append(dict(base, kind='concept', relationship=sec['why'], questions=qs))
            else:
                secs.append(dict(base, display_label='Go Deeper %s' % code[1:], difficulty='deeper', questions=qs))
        setfile = dict(format_version=1, set=s['num'], set_id='S%d' % s['num'], standard=std, title=s['title'],
                       domain=s['unit']['title'], unit=s['unit']['code'], unit_title=s['unit']['title'],
                       alignment=META.alignment(s), content_status=s['status'],
                       sources=[dict(x, **LEDGER.package_fields(x)) for x in s['sources']],
                       practical_skills=s['extra'], page=set_pages[s['num']], sections=secs)
        if s['note']:
            setfile['note'] = s['note']
        fn = 'sets/S%02d.json' % s['num']
        json.dump(setfile, open(os.path.join(OUT_PKG, fn), 'w'), indent=1, ensure_ascii=False)
        index_sets.append(dict(set=s['num'], file=fn, title=s['title'], standard=std, unit=s['unit']['code'],
                               sections=[dict(section_code=x['section_code'], relation=x['relation'], skill=x['skill'],
                                              **({'kind': x['kind']} if 'kind' in x else {}),
                                              **({'ref': x['ref']} if 'ref' in x else {'question_ids': [y['id'] for y in x['questions']]}))
                                         for x in secs]))
    index = dict(format_version=1, course='financial_literacy', bank_version=VERSION,
                 title='Untangle The Nexus — High School Financial Literacy',
                 collection=dict(id='FL', course='Financial Literacy', version=VERSION, date=META.DATE),
                 grade=None, question_count=len(recs), units=[dict(code=u['code'], title=u['title'], areas=u['area'],
                 sets=[s['num'] for s in sets if s['unit']['code'] == u['code']]) for u in D.UNITS],
                 sets=index_sets, branching=META.BRANCHING, id_format='S<set>-<section>-Q<n>; uid = "FL:" + id',
                 grading_rules=META.GRADING_RULES, standards=META.STANDARDS_NOTE)
    json.dump(index, open(os.path.join(OUT_PKG, 'index.json'), 'w'), indent=1, ensure_ascii=False)


def norm(t):
    return re.sub(r'[^a-z0-9$%. ]', '', t.lower()).strip()


def audit(recs):
    """Style checks on the multiple-choice items (numbers in QUALITY_AUDIT.md)."""
    text_items = [r for r in recs if not is_numeric([c['text'] for c in r['choices']])]
    longest = [r['id'] for r in text_items
               if (lambda L, i: L[i] == max(L) and L.count(max(L)) == 1)([len(c['text']) for c in r['choices']],
                                                                         'ABCD'.index(r['correct_letter']))]
    shortest = [r['id'] for r in text_items
                if (lambda L, i: L[i] == min(L) and L.count(min(L)) == 1)([len(c['text']) for c in r['choices']],
                                                                          'ABCD'.index(r['correct_letter']))]
    echoed = [r['id'] for r in recs if r['intro'] and len(r['correct_answer'].split()) >= 3
              and norm(r['correct_answer']) in norm(r['intro'])]
    words = [len(r['intro'].split()) for r in recs if r['intro']]
    return dict(text_items=len(text_items), longest=longest, shortest=shortest, echoed=echoed,
                intro_words=(min(words), sorted(words)[len(words) // 2], max(words)) if words else None,
                instruction=sum(1 for r in recs if r['intro']), knowledge_check=sum(1 for r in recs if not r['intro']),
                how_to=sum(1 for r in recs if r['how_to']))


SIBLING_PHRASES = re.compile(r"\b(the same (?:account|loan|card|plan|bond|car|house|budget|job|policy|fund|student|person)|"
                             r"(?:shown|listed|described) above|from above|previous question|earlier question|last question|"
                             r"the plan above|this (?:plan|loan|card|account) again|as before)\b", re.I)
# Reviewed by hand: the phrase compares two options inside the same question, so nothing is missing.
SIBLING_OK = {'S30-B1-Q4', 'S76-B1-Q5', 'S85-F2-Q4',
              'S56-F1-Q3'}  # "A worker ... she": the person is introduced in the stem
NOT_NAMES = set('''A An The What Which How If In On At For After Before When Why Is Are Does Do Your You Federal New Jersey IRS
Roth Social Security Medicare April January June May July Monday Tuesday Wednesday Thursday Friday Saturday Sunday Bank
Card Job Option Plan Loan Store Fund Company True Under To By With Assume During Each Every One Two Three Four Five Over
Year About Suppose Since As Its It This That These Those From Of Credit Form Treasury State Most Some Many Both'''.split())


def sibling_scan(recs):
    """Questions are shuffled, so each must stand alone. Flags stems that point at another question ("the same loan",
    "above", "as before") and he/she/her/his with no named person in the stem or its intro."""
    hits = []
    for r in recs:
        st = r['question']
        m = SIBLING_PHRASES.search(st)
        if m:
            hits.append((r['id'], m.group(0)))
        elif re.search(r"\b(she|he|her|his)\b", st, re.I):
            names = [w for w in re.findall(r"\b[A-Z][a-z]+\b", st + ' ' + (r['intro'] or '')) if w not in NOT_NAMES]
            if not names:
                hits.append((r['id'], 'pronoun with no named person'))
    return dict(flagged=hits, open=[h for h in hits if h[0] not in SIBLING_OK])


def main():
    sets = load()
    validate(sets)
    if PROBLEMS:
        print('\n'.join(PROBLEMS))
        sys.exit('%d problem(s)' % len(PROBLEMS))
    plan, counts = assign_letters(sets)
    recs, set_pages = build_records(sets, plan)
    write_keys(recs)
    write_package(sets, recs, set_pages)
    if '--quick' not in sys.argv:
        import fl_pdf
        fl_pdf.write_pdfs(sets, recs, set_pages)
        import fl_reports
        fl_reports.write_all(sets, recs)
        fl_pdf.copy_into_package(OUT_PKG)
        import subprocess
        subprocess.run([sys.executable, os.path.join(ENGINE, 'fl_crosscheck.py')], check=True)
        fl_reports.finish_package(OUT_PKG)
    elif '--reports' in sys.argv:
        import fl_reports
        fl_reports.write_all(sets, recs)
    print('%d sets, %d questions, letters %s' % (len(sets), len(recs), counts))
    a = audit(recs)
    print('correct is the unique longest choice: %d of %d text items (%.0f%%); unique shortest %d; intro repeats the '
          'correct choice: %d; intro words min/median/max %s; instruction %d, knowledge check %d, how-to %d'
          % (len(a['longest']), a['text_items'], 100 * len(a['longest']) / max(1, a['text_items']), len(a['shortest']),
             len(a['echoed']), a['intro_words'], a['instruction'], a['knowledge_check'], a['how_to']))
    sib = sibling_scan(recs)
    print('sibling scan: %d flagged, %d open %s' % (len(sib['flagged']), len(sib['open']), sib['open'] or ''))
    if '--show' in sys.argv:
        print('longest:', ' '.join(a['longest']))
        print('echoed:', ' '.join(a['echoed']))


if __name__ == '__main__':
    main()
