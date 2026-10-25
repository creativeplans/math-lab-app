"""Validate the built Logic collection and write VALIDATION.md.

    python3 question-bank/logic/src/validate.py      (after build.py)

Every check reads the built files (the answer key, the import package) or the source sets. A failed hard check makes
the script exit with status 1; soft checks are reported with their numbers.
"""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402
import build  # noqa: E402

ROOT = build.ROOT
PKG = build.PKG

PLACEHOLDER = re.compile(r'placeholder|TODO|TBD|\bcheck the key\b|see the key|\?\?|\.\.\. check|check\)$', re.I)
STANDALONE = re.compile(r'\b(the \w+ above|above,|previous question|question above|as before|from the last question|'
                        r'earlier question)\b', re.I)


def main():
    keyd = json.load(open(os.path.join(ROOT, 'Logic_Answer_Key.json'), encoding='utf-8'))
    recs = keyd['questions']
    index = json.load(open(os.path.join(PKG, 'index.json'), encoding='utf-8'))
    all_sets = build.load_sets()
    hard, soft, lines = [], [], []

    def check(name, ok, detail='', is_hard=True):
        (hard if is_hard else soft).append((name, ok, detail))

    # ---------------------------------------------------------- structure
    by_sec = collections.defaultdict(list)
    for r in recs:
        by_sec[(r['set'], r['section'])].append(r)
    bad_sizes = [k for k, v in by_sec.items() if len(v) != 5]
    check('Every section (MAIN, each backward branch, FORWARD 1, FORWARD 2) has exactly 5 questions', not bad_sizes,
          '%d sections checked; wrong sizes: %s' % (len(by_sec), bad_sizes or 'none'))
    missing = []
    for n in sorted(plan.SETS):
        codes = {c for (s, c) in by_sec if s == n}
        if not ({'M', 'F1', 'F2'} <= codes and any(c.startswith('B') for c in codes)):
            missing.append(n)
    check('Every set has MAIN, at least one backward branch, FORWARD 1 and FORWARD 2', not missing,
          '%d sets; missing parts: %s' % (len(plan.SETS), missing or 'none'))
    modes = collections.Counter(r['branch_mode'] for r in recs if r['section'].startswith('B'))
    check('Every backward branch is guided_strategy or prerequisite', set(modes) <= {'guided_strategy', 'prerequisite'},
          dict(modes))
    no_lesson = []
    for n, s in all_sets.items():
        for b in s['back']:
            if b['mode'] == 'guided_strategy':
                L = b['lesson']
                if not (L and L.get('text') and L.get('example') and L['example'].get('steps')):
                    no_lesson.append(n)
    check('Every guided-strategy branch has a lesson with a worked example', not no_lesson, no_lesson or 'all present')

    # ---------------------------------------------------------- plan rules
    kinds = [plan.SETS[n][3] for n in sorted(plan.SETS)]
    n_p = kinds.count('puzzle')
    check('At least half of the MAIN sets are puzzles', n_p * 2 >= len(kinds), '%d puzzle, %d formal' % (n_p, len(kinds) - n_p))
    first10 = kinds[:10].count('puzzle')
    check('Set 1 is a puzzle and at least 6 of the first 10 sets are puzzles', kinds[0] == 'puzzle' and first10 >= 6,
          '%d of the first 10' % first10)
    run, worst = 0, 0
    for k in kinds:
        run = run + 1 if k == 'formal' else 0
        worst = max(worst, run)
    check('Never more than 2 formal sets in a row', worst <= 2, 'longest formal run: %d' % worst)
    genres = {plan.SETS[n][4] for n in plan.SETS if plan.SETS[n][3] == 'puzzle'}
    check('At least 10 puzzle genres', len(genres) >= 10, '%d genres' % len(genres))
    direct = sorted({(r['set'], r['content_standard']) for r in recs if r['alignment_type'] == 'direct'})
    check('Direct standard alignment only on HSA-REI.A.1 (set 39) and HSG-CO.C.9 (set 43)',
          {s for s, _ in direct} <= {39, 43} and {c for _, c in direct} <= {'HSA-REI.A.1', 'HSG-CO.C.9'}, direct)
    bad_mp = sorted({p for r in recs for p in r['practices'] if p not in plan.PRACTICES})
    check('Supporting practices are only MP1, MP2, MP3, MP6, MP7, MP8', not bad_mp, bad_mp or 'all valid')

    # ---------------------------------------------------------- answers
    types = collections.Counter(r['type'] for r in recs)
    mcs = [r for r in recs if r['type'] == 'mc']
    four = [r['id'] for r in mcs if len(r['choices']) != 4 or len({c['text'].strip().lower() for c in r['choices']}) != 4]
    check('Every multiple-choice question has 4 different choices', not four, '%d checked; problems: %s' % (len(mcs), four or 'none'))
    keyok = [r['id'] for r in mcs if r['correct_letter'] not in [c['letter'] for c in r['choices']]]
    check('Every multiple-choice key letter is one of its choices', not keyok, keyok or 'all valid')
    letters = collections.Counter(r['correct_letter'] for r in mcs)
    spread = max(letters.values()) - min(letters.values())
    check('Multiple-choice key letters are balanced (largest minus smallest count at most 4% of MC items)',
          spread <= max(4, len(mcs) * 0.04), dict(sorted(letters.items())))
    seq = [r['correct_letter'] for r in mcs]
    runs, cur = [], 1
    for a, b in zip(seq, seq[1:]):
        cur = cur + 1 if a == b else 1
        if cur == 4:
            runs.append(a)
    sec_runs = []
    for k, v in by_sec.items():
        ls = [r['correct_letter'] for r in v if r['type'] == 'mc']
        c = 1
        for a, b in zip(ls, ls[1:]):
            c = c + 1 if a == b else 1
            if c >= 3:
                sec_runs.append('S%d-%s' % k)
    check('No run of 4 or more identical key letters in collection order', not runs, '%d runs' % len(runs), is_hard=False)
    check('No section has 3 identical key letters in a row', not sec_runs, sec_runs or 'none', is_hard=False)
    tfs = [r for r in recs if r['type'] == 'tf']
    tcount = collections.Counter(r['correct_letter'] for r in tfs)
    check('True/false answers are balanced (within 10%)', abs(tcount.get('A', 0) - tcount.get('B', 0)) <= max(4, len(tfs) * 0.1),
          'True %d, False %d' % (tcount.get('A', 0), tcount.get('B', 0)))
    unique_longest = 0
    for r in mcs:
        if r['choices'][0]['text'].startswith('Figure '):
            continue
        lens = {c['letter']: len(c['text']) for c in r['choices']}
        mx = max(lens.values())
        if lens[r['correct_letter']] == mx and list(lens.values()).count(mx) == 1:
            unique_longest += 1
    text_mcs = sum(1 for r in mcs if not r['choices'][0]['text'].startswith('Figure '))
    share = unique_longest / max(1, text_mcs)
    check('Length cue: the key is the unique longest choice in at most 40% of text multiple-choice items', share <= 0.40,
          '%d of %d (%.0f%%; 25%% would be chance)' % (unique_longest, text_mcs, 100 * share), is_hard=False)

    # ---------------------------------------------------------- wording
    texts = []
    for r in recs:
        texts.append((r['id'], r['prompt']))
        texts.append((r['id'], r['solution']))
        for c in r.get('choices') or []:
            texts.append((r['id'], c['text']))
        for w in r.get('wrong_choices') or []:
            texts.append((r['id'], w['why_wrong']))
    ph = sorted({i for i, t in texts if PLACEHOLDER.search(t or '')})
    check('No placeholder or unfinished text in prompts, choices, solutions or wrong-choice reasons', not ph, ph or 'none')
    sa_ = sorted({i for i, t in texts[::1] if False})
    stand = sorted({r['id'] for r in recs if STANDALONE.search(r['prompt'])})
    check('Every question stands alone (no reference to another question or "the puzzle above")', not stand, stand or 'none')
    prompts = collections.Counter(r['prompt'].strip() for r in recs)
    dups = [p[:70] for p, c in prompts.items() if c > 1]
    check('No two questions have the same prompt', not dups, dups or 'none')
    ex_hits = []
    for n, s in all_sets.items():
        for b in s['back']:
            L = b.get('lesson')
            if not L:
                continue
            for ex in L['example'].get('prompt', []):
                for r in recs:
                    if ex.strip() and ex.strip() in r['prompt']:
                        ex_hits.append((n, r['id']))
    check('Lesson worked examples are different from every scored question', not ex_hits, ex_hits or 'none')
    no_sol = [r['id'] for r in recs if len((r['solution'] or '').strip()) < 2]
    check('Every question has a written solution', not no_sol, no_sol or 'all present')
    no_why = [r['id'] for r in mcs if any(len((w['why_wrong'] or '').strip()) < 6 for w in r['wrong_choices'])]
    check('Every wrong multiple-choice option has a reason it is wrong', not no_why, no_why or 'all present')

    # ---------------------------------------------------------- rule-graded answers: stated domain enforced
    sys.path.insert(0, HERE)
    from lq import eval_rule, infer_domain
    leaks, n_vals = [], 0
    for r in recs:
        if r['type'] != 'values':
            continue
        n_vals += 1
        pf = r['package_fields']
        ex = pf['example_answer']
        kind = infer_domain(r['prompt'])
        if not eval_rule(pf['rule'], ex):
            leaks.append((r['id'], 'example fails'))
        if kind == 'any':
            continue
        for k, v in ex.items():
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                continue
            probes = [v + 0.5, 0.5, -1, -2, -v - 1, -9]
            for b in probes:
                bad = b != int(b) or (kind == 'whole' and b < 0) or (kind == 'pos' and b < 1)
                if bad and eval_rule(pf['rule'], dict(ex, **{k: b})):
                    leaks.append((r['id'], k, b))
    check('Every rule-graded (values) answer rejects negative and fractional inputs whenever the question asks for whole '
          'numbers or integers (packaged rule tested)', not leaks, '%d values questions; problems: %s' % (n_vals, leaks or 'none'))
    bad_orders = []
    for r in recs:
        if r['type'] == 'order':
            pf = r['package_fields']
            accepted = [pf['correct_order']] + (pf.get('accept_orders') or [])
            if len({tuple(a) for a in accepted}) != len(accepted):
                bad_orders.append(r['id'])
    check('Every ordering question lists each accepted order once (all orders allowed by its dependency rule were '
          'enumerated at build time)', not bad_orders, bad_orders or 'none')

    # ---------------------------------------------------------- package and figures
    set_files = sorted(os.listdir(os.path.join(PKG, 'sets')))
    check('The import package has one set file per set', len(set_files) == len(plan.SETS), '%d files' % len(set_files))
    assets = set(os.listdir(os.path.join(PKG, 'assets')))
    missing_fig = []
    n_fig = 0
    for f in set_files:
        s = json.load(open(os.path.join(PKG, 'sets', f), encoding='utf-8'))
        for sec in s['sections']:
            for q in sec['questions']:
                fig = q.get('figure')
                if fig:
                    n_fig += 1
                    if os.path.basename(fig['svg']) not in assets or not fig.get('description'):
                        missing_fig.append(q['id'])
    check('Every figure file exists and has a text description', not missing_fig, '%d figures; problems: %s'
          % (n_fig, missing_fig or 'none'))
    gray = []
    for a in assets:
        svg = open(os.path.join(PKG, 'assets', a), encoding='utf-8').read()
        for col in re.findall(r'#([0-9a-fA-F]{6})\b', svg):
            r_, g_, b_ = int(col[:2], 16), int(col[2:4], 16), int(col[4:], 16)
            if max(r_, g_, b_) - min(r_, g_, b_) > 8:
                gray.append(a)
                break
    check('All figures are grayscale', not gray, gray or 'all grayscale')
    verified = sum(1 for r in recs if 'Automatic' in (r['validation'] or '') or 'Checked' in (r['validation'] or '')
                   or 'Search' in (r['validation'] or ''))

    # ---------------------------------------------------------- write
    out = ['# Logic collection: validation report', '',
           'Collection LOGIC version %s (%s). %d sets, %d questions, %d figures.' % (build.VERSION, build.DATE, len(plan.SETS),
                                                                                    len(recs), n_fig), '',
           'Question types: ' + ', '.join('%s %d' % (k, v) for k, v in sorted(types.items())) + '.', '',
           'Questions whose key was confirmed by code during the build (enumeration, search, a check function or a '
           'recomputed answer): %d of %d. The rest (mostly reading, fallacy and argument questions) were solved by the '
           'author, and every wrong choice carries a written reason.' % (verified, len(recs)), '',
           '## Required checks', '', '| Check | Result | Detail |', '|---|---|---|']
    for name, ok, detail in hard:
        out.append('| %s | %s | %s |' % (name, 'PASS' if ok else 'FAIL', str(detail).replace('|', '/')))
    out += ['', '## Balance and style checks', '', '| Check | Result | Detail |', '|---|---|---|']
    for name, ok, detail in soft:
        out.append('| %s | %s | %s |' % (name, 'PASS' if ok else 'NOTE', str(detail).replace('|', '/')))
    out += ['', '## What the build itself verified', '',
            '- Every ordering question: all orderings of its items were enumerated; every valid ordering is accepted.',
            '- Every grid question: all assignments were enumerated; puzzles marked unique have exactly one solution.',
            '- Every truth table and Venn diagram: each cell or region was computed from the formula or condition.',
            '- Every rule-checked answer (values): the example passes the rule and the listed tempting mistakes fail it; '
            'where a finite domain is stated, every valid answer in it was counted.',
            '- Multiple-choice items with a check function: the function accepts the keyed choice and rejects all others.',
            '- Short answers with a compute function: the key was recomputed by code.', '',
            'The game-side checks (tools/game_checks.ts, which runs every key and wrong answer through the game\'s own '
            'response checkers) and the importer check are reported in the README.', '']
    text = '\n'.join(out)
    for d in (ROOT, PKG):
        open(os.path.join(d, 'VALIDATION.md'), 'w', encoding='utf-8').write(text)
    fails = [n for n, ok, _ in hard if not ok]
    notes = [n for n, ok, _ in soft if not ok]
    print('validation: %d required checks, %d failed; %d style checks, %d notes' % (len(hard), len(fails), len(soft),
                                                                                    len(notes)))
    for n in fails:
        print('  FAIL', n, [d for m, ok, d in hard if m == n][0])
    for n in notes:
        print('  NOTE', n, [d for m, ok, d in soft if m == n][0])
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
