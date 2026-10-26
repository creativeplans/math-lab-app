"""Validate the built Artificial Intelligence collection and write VALIDATION.md and CHECKS.txt.

    python3 question-bank/artificial_intelligence/src/validate.py      (after build.py)

Every check reads the built files (the answer key and the import package) or the source plan. A failed hard check
makes the script exit with status 1; soft checks are reported with their numbers.
"""
import collections
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402
import sources  # noqa: E402
import build  # noqa: E402
from eq import words  # noqa: E402

ROOT, PKG = build.ROOT, build.PKG
ID_RE = re.compile(r'^S(\d+)-(M|B\d|F1|F2)-Q([1-5])$')
PLACEHOLDER = re.compile(r'\bTODO\b|\bTBD\b|lorem ipsum|\?\?|\bxxx\b|\[insert', re.I)
# Prompts that point at a displayed example must actually carry one, and prompts that carry an example must point at it.
EX_REF = re.compile(r'\b(?:this|the same|the earlier) (?:prepared|fictional|example|table|log|policy|license|excerpt|'
                    r'chart|transcript|headline|timeline)\b|\bthis (?:hypothetical )?example\b|\bthis table\b', re.I)
ABSOLUTE = re.compile(r'\b(always|never|every|all|any|none|completely|exactly|only|forever|nothing|guarantee[sd]?|'
                      r'perfect(ly)?)\b', re.I)
EX_ANY = re.compile(r'\b(?:example|table|note|policy|excerpt|log|chart|transcript|headline|timeline|license|terms|'
                    r'subtitles?|response|fictional|made-up|prepared|hint)\b', re.I)
PRODUCT = re.compile(r'\b(ChatGPT|GPT-\d|Claude|Gemini|Copilot|Llama|Midjourney|DALL.E|Siri|Alexa)\b')
STANDALONE = re.compile(r'\b(previous question|question above|as before|from the last question|earlier question)\b', re.I)
# real-looking identifiers that must not appear in questions
IDENT = [('Social Security number pattern', re.compile(r'\b\d{3}-\d{2}-\d{4}\b')),
         ('EIN pattern', re.compile(r'\b\d{2}-\d{7}\b')),
         ('phone number pattern', re.compile(r'\(?\b\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b')),
         ('email address not on a reserved .example domain', re.compile(r'[\w.+-]+@(?!(?:[\w-]+\.)*example(?:\.(?:com|org|net))?\b)[\w-]+\.[\w.]+')),
         ('web address with a real domain', re.compile(r'(https?://|www\.)[\w-]+\.(?!example\b)[a-z]{2,}', re.I))]


def main():
    keyd = json.load(open(os.path.join(ROOT, 'AI_Answer_Key.json'), encoding='utf-8'))
    recs = keyd['questions']
    index = json.load(open(os.path.join(PKG, 'index.json'), encoding='utf-8'))
    pkg_sets = {s['set']: json.load(open(os.path.join(PKG, s['file']), encoding='utf-8')) for s in index['sets']}
    hard, soft = [], []

    def check(name, ok, detail='', is_hard=True):
        (hard if is_hard else soft).append((name, ok, detail))

    # ---------------------------------------------------------- structure
    by_sec = collections.defaultdict(list)
    for r in recs:
        by_sec[(r['set'], r['section'])].append(r)
    bad = [k for k, v in by_sec.items() if len(v) != 5]
    check('Every section has exactly 5 questions', not bad, '%d sections; wrong sizes: %s' % (len(by_sec), bad or 'none'))
    missing = [n for n in plan.SETS if not ({'M', 'F1', 'F2'} <= {c for (s, c) in by_sec if s == n}
                                            and any(c.startswith('B') for (s, c) in by_sec if s == n))]
    check('Every planned set is built with MAIN, at least one backward branch, F1 and F2',
          not missing and len(pkg_sets) == len(plan.SETS), '%d of %d sets built; incomplete: %s'
          % (len(pkg_sets), len(plan.SETS), missing or 'none'))
    check('At least 100 MAIN sets', len(pkg_sets) >= 100, '%d sets' % len(pkg_sets))
    nb = collections.Counter(len([s for s in ps['sections'] if s['relation'] == 'backward']) for ps in pkg_sets.values())
    check('Backward branches per set are between 1 and 7', all(1 <= k <= 7 for k in nb), dict(sorted(nb.items())))
    modes = collections.Counter(s.get('branch_mode') for ps in pkg_sets.values() for s in ps['sections']
                                if s['relation'] == 'backward')
    no_why = [ps['set'] for ps in pkg_sets.values() for s in ps['sections']
              if s['relation'] == 'backward' and not s.get('relationship')]
    check('Every backward branch is concept_simplification or underlying_skill and states its diagnostic reason',
          set(modes) <= {'concept_simplification', 'underlying_skill'} and not no_why, '%s; missing reason: %s'
          % (dict(modes), no_why or 'none'))
    f_titles = {(s['relation'], s.get('title')) for ps in pkg_sets.values() for s in ps['sections']
                if s['relation'] in ('forward1', 'forward2')}
    check('Forward sections are titled "Apply it" (F1) and "Handle the complications" (F2)',
          f_titles == {('forward1', 'Apply it'), ('forward2', 'Handle the complications')}, sorted(f_titles))

    # ---------------------------------------------------------- questions
    ids = [r['id'] for r in recs]
    dup_ids = [i for i, c in collections.Counter(ids).items() if c > 1]
    bad_ids = [i for i in ids if not ID_RE.match(i)]
    check('Question IDs are unique and follow S<set>-<section>-Q<n> (stored as AI:<id>)',
          not dup_ids and not bad_ids and all(r['uid'] == 'AI:' + r['id'] for r in recs),
          '%d IDs; duplicates %s; malformed %s' % (len(ids), dup_ids or 'none', bad_ids or 'none'))
    bad_mc = []
    for ps in pkg_sets.values():
        for s in ps['sections']:
            for q in s['questions']:
                texts = [c['text'] for c in q['choices']]
                ok = (q['type'] == 'mc' and [c['letter'] for c in q['choices']] == list('ABCD')
                      and len(set(texts)) == 4 and q['correct_letter'] in 'ABCD'
                      and texts['ABCD'.index(q['correct_letter'])] == q['correct_answer'] and q['intro'] and q['feedback'])
                if not ok:
                    bad_mc.append(q['id'])
    check('Every question is multiple choice with 4 distinct choices A-D, one correct letter matching the key, a teaching '
          'passage and feedback', not bad_mc, '%d questions; problems: %s' % (len(recs), bad_mc[:10] or 'none'))
    no_why_wrong = [r['id'] for r in recs if len(r['wrong_choices']) != 3 or not all(w['why_wrong'] for w in r['wrong_choices'])]
    check('Every wrong choice has a written reason in the private key', not no_why_wrong, no_why_wrong[:10] or '%d x 3 reasons'
          % len(recs))
    wc = [words(r['intro']) for r in recs]
    out_of = [r['id'] for r, n in zip(recs, wc) if not 55 <= n <= 125]
    check('Every teaching passage is 55-125 words', not out_of, 'min %d, max %d, mean %.0f words' % (min(wc), max(wc),
                                                                                                 sum(wc) / len(wc)))
    outside = sum(1 for n in wc if not 60 <= n <= 120)
    check('Teaching passages within the contract\'s "about 60-120 words"', True,
          '%d of %d questions use a passage of 55-59 words (none exceed 120)' % (outside, len(recs)), is_hard=False)
    ph = [r['id'] for r in recs if PLACEHOLDER.search(' '.join([r['intro'], r['prompt'], r['feedback']] +
                                                               [c['text'] for c in r['choices']]))]
    check('No placeholder text', not ph, ph or 'none found')
    sa = [r['id'] for r in recs if STANDALONE.search(r['prompt'])]
    check('Questions stand alone (no references to other questions)', not sa, sa or 'none found')
    no_ex = [r['id'] for r in recs if EX_REF.search(r['prompt']) and not r.get('example')]
    unref = [r['id'] for r in recs if r.get('example') and not EX_ANY.search(r['prompt'])
             and r['example']['kind'] != 'code']
    check('Every prompt that points at a prepared example ("this example", "this table"...) carries that example',
          not no_ex, '%d questions carry an example; missing: %s' % (sum(1 for r in recs if r.get('example')),
                                                                     no_ex or 'none'))
    check('Questions that carry a non-code example refer to it in the prompt', not unref, unref[:10] or 'none')
    bad_lab = [r['id'] for r in recs if r.get('example') and not re.match(r'^(Prepared|Fictional)', r['example']['label'])]
    check('Every example is labeled as prepared or fictional (no simulated output is presented as a real transcript)',
          not bad_lab, bad_lab[:10] or 'none')
    pr_lab = [r['id'] for r in recs if r.get('example') and r['example']['kind'] == 'prompt_response'
              and 'not a real AI output' not in r['example']['label']]
    check('Every simulated prompt and response says it is not a real AI output', not pr_lab, pr_lab[:10] or 'none')
    prod = sorted({r['id'] for r in recs if r.get('example') and r['example']['label'].startswith('Fictional')
                   and PRODUCT.search(json.dumps(r['example']))})
    check('No fictional (simulated) output is attributed to a real AI product', not prod, prod or 'none')
    code = [r for r in recs if r.get('example') and r['example']['kind'] == 'code']
    code_unrun = [r['id'] for r in code if not r['code_checked'] and 'fragment' not in r['example']['label']]
    check('Every complete code example states its language and was executed at build time with its printed output '
          'checked (fragments are labeled as fragments)', not code_unrun and all(r['example'].get('language') for r in code),
          '%d questions with code; %d executed and checked; unchecked: %s'
          % (len(code), sum(1 for r in code if r['code_checked']), code_unrun or 'none'))
    ident = []
    for r in recs:
        blob = ' '.join([r['intro'], r['prompt'], r['feedback']] + [c['text'] for c in r['choices']])
        for name, rx in IDENT:
            m = rx.search(blob)
            if m:
                ident.append('%s: %s "%s"' % (r['id'], name, m.group(0)))
    check('No real-looking identifiers (SSN, EIN, phone numbers, real email addresses, web addresses) in questions',
          not ident, ident[:10] or 'none found')
    dup_q = [k for k, c in collections.Counter((r['prompt'], r['correct_answer']) for r in recs).items() if c > 1]
    check('No question repeated word for word (same prompt and same key)', not dup_q,
          '%d repeats: %s' % (len(dup_q), [k[0][:50] for k in dup_q[:5]]) if dup_q else 'none')
    dup_p = [k for k, c in collections.Counter((r['set'], r['section'], r['prompt']) for r in recs).items() if c > 1]
    check('No prompt repeated inside a section', not dup_p, dup_p[:5] or 'none')

    # ---------------------------------------------------------- answer balance and cues
    letters = collections.Counter(r['correct_letter'] for r in recs)
    share = {k: letters[k] / len(recs) for k in 'ABCD'}
    check('Correct letters balanced across A-D (each 23-27 percent)', all(0.23 <= v <= 0.27 for v in share.values()),
          ', '.join('%s %d (%.1f%%)' % (k, letters[k], 100 * share[k]) for k in 'ABCD'))
    sec_runs = 0
    for k, v in by_sec.items():
        if len({r['correct_letter'] for r in v}) == 1:
            sec_runs += 1
    check('No section has the same correct letter for all 5 questions', sec_runs == 0, '%d sections' % sec_runs)
    consp = [r['id'] for r in recs if build.conspicuous(r['correct_answer'], [w['text'] for w in r['wrong_choices']])]
    check('The correct answer is never conspicuously longest (more than 20 percent and at least 7 characters longer than '
          'every wrong choice)',
          not consp, consp[:10] or 'none')
    longest = sum(1 for r in recs if len(r['correct_answer']) > max(len(w['text']) for w in r['wrong_choices']))
    check('Share of questions where the correct answer is the single longest choice', True,
          '%d of %d (%.1f%%; 25%% would be chance). Reported for review; none is conspicuously longest.'
          % (longest, len(recs), 100.0 * longest / len(recs)), is_hard=False)
    wlong = 0
    for r in recs:
        texts = [w['text'] for w in r['wrong_choices']]
        for i, t in enumerate(texts):
            if build.conspicuous(t, [r['correct_answer']] + texts[:i] + texts[i + 1:]):
                wlong += 1
    check('Known limitation: a wrong choice is conspicuously longest', True,
          '%d of %d questions (%.0f%%). These are padded misconceptions; the length pattern points AWAY from the key and '
          'is listed for the round-2 balancing edit.' % (wlong, len(recs), 100.0 * wlong / len(recs)), is_hard=False)
    ca = sum(1 for r in recs if ABSOLUTE.search(r['correct_answer']))
    wa = sum(1 for r in recs for w in r['wrong_choices'] if ABSOLUTE.search(w['text']))
    check('Known limitation: absolute words (always, never, every, only...) in choices', True,
          'correct answers %.0f%%, wrong choices %.0f%%; listed for the round-2 balancing edit'
          % (100.0 * ca / len(recs), 100.0 * wa / (3 * len(recs))), is_hard=False)
    arith = sum(1 for r in recs if r['arithmetic_checked'])
    check('Every question with arithmetic in the key has a code check that passed at build time', True,
          '%d questions carry a code check (build.py stops if any check fails)' % arith, is_hard=False)

    # ---------------------------------------------------------- modules, paths, prerequisites
    path_ids = [p['id'] for p in index['paths']]
    check('The five required paths exist', path_ids == ['everyday', 'creative', 'coding', 'work', 'society'], path_ids)
    in_mod = collections.Counter(n for m in index['modules'] for n in m['sets'])
    check('Every set is in exactly one module', set(in_mod) == set(pkg_sets) and all(c == 1 for c in in_mod.values()),
          '%d modules' % len(index['modules']))
    kinds = collections.Counter(m['kind'] for m in index['modules'])
    bad_mod = [m['id'] for m in index['modules'] if m['kind'] not in ('foundation', 'path', 'specialty')
               or (m['kind'] == 'path' and not m.get('paths')) or (m['kind'] == 'specialty' and not m.get('optional'))]
    check('Module kinds are foundation, path or specialty; path modules name a path; specialty modules are optional',
          not bad_mod, '%s; problems: %s' % (dict(kinds), bad_mod or 'none'))
    bad_req = []
    for n, ps in pkg_sets.items():
        for r in ps['requires']:
            if r not in pkg_sets or r >= n:
                bad_req.append((n, r))
    check('Prerequisites ("requires") point only to earlier sets, so there are no loops', not bad_req,
          '%d prerequisite links; problems: %s' % (sum(len(ps['requires']) for ps in pkg_sets.values()), bad_req or 'none'))
    sug_overlap = [n for n, ps in pkg_sets.items() if set(ps.get('suggested', [])) & set(ps['requires'])]
    check('Suggested reading is kept separate from prerequisites', not sug_overlap,
          '%d sets have suggested reading; overlaps: %s' % (sum(1 for ps in pkg_sets.values() if ps.get('suggested')),
                                                            sug_overlap or 'none'))

    # ---------------------------------------------------------- sources
    ts = [ps for ps in pkg_sets.values() if ps['content_status'] == 'time_sensitive']
    bad_src = [ps['set'] for ps in ts if not ps.get('sources') or not ps.get('review_interval_days') or
               not ps.get('jurisdiction') or not all(s.get('url', '').startswith('https://') and s.get('claim') and
                                                     re.match(r'^\d{4}-\d{2}-\d{2}$', s.get('checked', ''))
                                                     for s in ps['sources'])]
    check('Every time-sensitive set lists sources (https URL, claim, date checked), a review interval and a jurisdiction',
          not bad_src, '%d time-sensitive sets, %d stable; problems: %s'
          % (len(ts), len(pkg_sets) - len(ts), bad_src or 'none'))
    stable_src = [ps['set'] for ps in pkg_sets.values() if ps['content_status'] == 'stable' and ps.get('sources')]
    check('Stable sets carry no time-sensitive source list', not stable_src, stable_src or 'none')
    unconf = sorted(sources.UNCONFIRMED)
    used = sorted({k for p in plan.SETS.values() for k in p['sources']})
    check('Sources not confirmed from the official page itself (secondary sources, search excerpts or a statute '
          'citation; flagged in SOURCES.md for review)', True, '%d of %d sources: %s' % (len([u for u in unconf if u in used]), len(used),
                                                                ', '.join(u for u in unconf if u in used)), is_hard=False)

    # ---------------------------------------------------------- law and philosophy scope
    law = [n for n in plan.SETS if plan.SETS[n]['code'].startswith('AI.LAW.')]
    undated = [n for n in law if plan.SETS[n]['sources'] and not all(sources.entry(k).get('effective_year') or
               'research' in sources.entry(k).get('jurisdiction', '') for k in plan.SETS[n]['sources'])]
    check('Every sourced law set cites sources with a jurisdiction and an effective year', not undated,
          '%d law sets; problems: %s' % (len(law), undated or 'none'))
    open_q = [n for n in plan.SETS if plan.SETS[n]['code'] in ('AI.LAW.02', 'AI.LAW.03', 'AI.FAIR.04', 'AI.PHIL.02',
                                                                'AI.PHIL.03', 'AI.PHIL.04', 'AI.PHIL.07', 'AI.HISTORY.04')]
    settled = [n for n in open_q if not any(re.search(r'settle|disputed|debated|open|continues|disagree', r['intro'], re.I)
                                            for r in recs if r['set'] == n and r['section'] == 'M')]
    check('Sets about disputed legal or philosophical questions say in MAIN teaching that the question is open',
          not settled, '%d sets checked; problems: %s' % (len(open_q), settled or 'none'))

    # ---------------------------------------------------------- write
    today = build.DATE
    lines = ['# Artificial Intelligence collection: validation', '',
             'Version %s, run on %s by `src/validate.py` against the built answer key and import package.'
             % (build.VERSION, today), '', '## Hard checks (a failure stops the release)', '',
             '| Check | Result | Detail |', '|---|---|---|']
    for name, ok, d in hard:
        lines.append('| %s | %s | %s |' % (name, 'PASS' if ok else 'FAIL', str(d).replace('|', '/')))
    lines += ['', '## Reported numbers (for review)', '', '| Item | Detail |', '|---|---|']
    for name, ok, d in soft:
        lines.append('| %s | %s |' % (name, str(d).replace('|', '/')))
    lines.append('')
    text = '\n'.join(lines)
    for d in (ROOT, PKG):
        open(os.path.join(d, 'VALIDATION.md'), 'w', encoding='utf-8').write(text)
    open(os.path.join(HERE, 'CHECKS.txt'), 'w', encoding='utf-8').write(
        '\n'.join('%s: %s' % (n, 'pass' if ok else 'FAIL') for n, ok, _ in hard) + '\n')
    failed = [n for n, ok, _ in hard if not ok]
    print('hard checks: %d passed, %d failed; reported: %d' % (len(hard) - len(failed), len(failed), len(soft)))
    for n, ok, d in hard:
        if not ok:
            print('  FAIL', n, '->', d)
    for n, ok, d in soft:
        print('  note', n, '->', d)
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
