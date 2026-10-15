"""Reports for the Financial Literacy collection (written by fl_build.py on a full build):

    COVERAGE.md          national and New Jersey standards, the 20 content areas, the required progressions,
                         practical skills, prerequisite and Go Deeper counts, question counts and difficulty
    MATH_BRANCHES.md     every math prerequisite link and the game skill it points to
    CONCEPT_BRANCHES.md  every financial-concept prerequisite branch
    GO_DEEPER.md         every Go Deeper chain
    HOW_TO.md            practical how-to coverage, including the five required walkthroughs
    QUALITY_AUDIT.md     question and distractor checks
    README.md            architecture, schema, sources, limitations, how to rebuild and import

finish_package() copies the README and reports into the import package, writes MANIFEST.json, and zips it.
"""
import collections
import hashlib
import json
import os
import re
import shutil
import zipfile

import fl_build as B
import fl_dsl as D
import fl_meta as META
import fl_ledger as LEDGER

REPORTS = ['COVERAGE.md', 'MATH_BRANCHES.md', 'CONCEPT_BRANCHES.md', 'GO_DEEPER.md', 'HOW_TO.md', 'QUALITY_AUDIT.md',
           'SOURCE_LEDGER.md', 'SOURCE_LEDGER.json', 'RUNTIME_CHECK.json', 'MATH_REF_VALIDATION.json',
           'REVIEW_RESPONSE.md', 'CHANGES.md', 'CHANGES.json', 'EXPORT_CROSSCHECK.json']
ZIP_NAME = 'FinancialLiteracy_Nexus_Import_v%s.zip' % B.VERSION

AREAS = ['Money, Banking, and Financial Institutions', 'Earning Income, Employment, and Paychecks',
         'Budgeting and Managing Expenses', 'Saving and Emergency Funds', 'Interest, Borrowing, and Debt',
         'Credit Cards and Credit Scores', 'Investing and Brokerage Accounts',
         'Stocks, Bonds, Mutual Funds, ETFs, and Index Funds',
         'Retirement Accounts (Roth and Traditional IRAs, 401(k)s, 403(b)s)', 'Taxes and Tax Filing',
         'Renting and Leasing', 'Mortgages and Homeownership', 'Vehicles', 'Insurance', 'College Financing',
         'Entrepreneurship', 'Consumer Protection and Fraud', 'Inflation, Purchasing Power, and Economic Decisions',
         'Contracts and Fees', 'Integrated Decisions']

AREA_SETS = {7: [43, 44, 45, 50, 51, 52, 53, 54], 8: [46, 47, 48, 49]}

# The assignment's required progressions, each step mapped to the question(s) that teach it.
PROGRESSIONS = {
    'Brokerage accounts (assignment Part 4, steps 1-20)': [
        ('What is a bank?', ['S1-M-Q1']), ('What is a checking account?', ['S2-M-Q1']),
        ('What is a savings account?', ['S6-M-Q1']), ('What is a brokerage firm?', ['S44-M-Q2']),
        ('Examples of brokerage firms: Charles Schwab, Fidelity, E*TRADE', ['S44-M-Q3', 'S45-F1-Q5']),
        ('What is a brokerage account?', ['S44-M-Q1', 'S44-B1-Q1']),
        ('What investments can brokerage accounts hold?', ['S44-F1-Q1']),
        ('Bank deposit vs investment', ['S44-M-Q4', 'S44-B1-Q4']),
        ('Deposit insurance vs brokerage customer protection (FDIC vs SIPC)', ['S44-M-Q5', 'S44-F2-Q1', 'S44-F2-Q5']),
        ('Information required to open a brokerage account', ['S45-M-Q1']),
        ('Depositing money into a brokerage account', ['S45-B1-Q1', 'S45-B1-Q4']),
        ('Funding the account vs buying an investment', ['S45-M-Q3', 'S45-B1-Q3']),
        ('What is a stock?', ['S46-M-Q1']), ('What is an ETF?', ['S48-M-Q2']), ('What is a mutual fund?', ['S48-M-Q1']),
        ('What is an index fund?', ['S48-M-Q3']), ('Placing a basic investment order', ['S45-M-Q4']),
        ('What is a market order?', ['S50-M-Q1']), ('What is a limit order?', ['S50-M-Q2']),
        ('How fees and investment risks affect decisions', ['S51-M-Q5', 'S43-M-Q3']),
    ],
    'Roth IRA (assignment Part 4, steps 1-25)': [
        ('Why people save for retirement', ['S55-M-Q1']), ('What an IRA is', ['S57-M-Q1']),
        ('What makes an IRA a retirement account', ['S57-M-Q2']), ('What a Roth IRA is', ['S57-M-Q3']),
        ('What a traditional IRA is', ['S57-M-Q4']), ('Differences in tax treatment', ['S57-B1-Q1', 'S57-B1-Q2']),
        ('Earned income and eligibility', ['S58-M-Q1']), ('Contribution limits and income restrictions', ['S58-M-Q3', 'S58-M-Q4']),
        ('Where someone can open a Roth IRA', ['S59-M-Q2']), ('Examples of providers', ['S59-M-Q2']),
        ('How to compare providers', ['S59-M-Q3']), ('Information generally required', ['S59-M-Q4']),
        ('How account opening works', ['S59-F1-Q1']), ('How a minor\'s account may differ', ['S58-F1-Q1']),
        ('How money is contributed', ['S59-F1-Q2', 'S59-F1-Q3']),
        ('Why deposited cash is not necessarily invested', ['S60-M-Q1', 'S60-B1-Q1']),
        ('How investments are selected within the IRA', ['S60-M-Q2']),
        ('Examples of investments an IRA may hold', ['S59-B1-Q3']), ('What investment fees are', ['S60-F1-Q1']),
        ('How investment returns and losses work', ['S60-M-Q4']), ('How compounding affects outcomes', ['S60-M-Q5']),
        ('Contributions vs earnings', ['S60-M-Q3']), ('General withdrawal rules', ['S61-M-Q1']),
        ('Qualified distributions', ['S61-M-Q3']), ('Common misconceptions and mistakes', ['S61-M-Q5', 'S60-B1-Q5']),
    ],
    'Mortgages (assignment Part 4, steps 1-23)': [
        ('Renting versus owning', ['S75-M-Q3']), ('What a mortgage is', ['S75-M-Q1']), ('Principal', ['S75-B1-Q1']),
        ('Interest', ['S76-M-Q2']), ('Down payments', ['S75-M-Q2']), ('Loan terms', ['S76-M-Q3']),
        ('Fixed versus adjustable rates', ['S81-M-Q1', 'S81-M-Q2']),
        ('Monthly principal-and-interest payments', ['S76-F1-Q2']), ('Property taxes', ['S77-M-Q1']),
        ('Homeowners insurance', ['S77-M-Q2']), ('Mortgage insurance', ['S77-M-Q3']), ('Closing costs', ['S78-M-Q1']),
        ('Escrow', ['S77-M-Q5']), ('Loan estimates', ['S78-M-Q2']), ('Preapproval', ['S79-M-Q1']),
        ('Creditworthiness', ['S79-M-Q4']), ('Debt-to-income ratios', ['S79-M-Q2', 'S79-M-Q3']),
        ('Amortization', ['S80-M-Q1', 'S80-M-Q2']), ('Total interest over the loan term', ['S76-M-Q2']),
        ('Additional principal payments', ['S80-M-Q3']), ('Refinancing', ['S80-M-Q4']),
        ('Maintenance costs', ['S81-M-Q4']), ('Affordability versus lender approval', ['S79-F1-Q4', 'S81-F2-Q4']),
    ],
}

WALKTHROUGHS = {
    'Opening a Roth IRA': [('Reasonable first step (the assignment\'s Jordan example)', ['S59-M-Q1']),
                           ('Selecting a provider', ['S59-M-Q3']), ('Identifying the correct account type', ['S59-M-Q5']),
                           ('Understanding account requirements', ['S59-M-Q4']), ('Funding the account', ['S59-F1-Q2']),
                           ('Selecting an investment', ['S60-M-Q2']), ('Verifying transactions', ['S59-F1-Q4']),
                           ('Cash is not an investment (the assignment\'s Taylor knowledge check)', ['S60-M-Q1'])],
    'Opening a checking account': [('Comparing banks and credit unions', ['S1-M-Q2', 'S1-F2-Q1']),
                                   ('Checking account fees', ['S3-M-Q3']), ('Minimum balance requirements', ['S3-B1-Q3']),
                                   ('Opening procedures', ['S3-M-Q2']), ('Debit cards', ['S2-M-Q2']),
                                   ('Direct deposit', ['S3-M-Q4']), ('Overdrafts', ['S5-M-Q1']),
                                   ('Account statements', ['S4-M-Q2'])],
    'Renting an apartment': [('Searching for legitimate listings', ['S71-M-Q2']),
                             ('Comparing total monthly expenses', ['S71-M-Q3']), ('Rental applications', ['S72-M-Q4']),
                             ('Security deposits', ['S73-M-Q2']), ('Reading a lease', ['S73-M-Q5', 'S73-B1-Q5']),
                             ('Tenant responsibilities', ['S74-M-Q3']), ('Avoiding rental scams', ['S71-M-Q1'])],
    'Buying a car': [('Comparing purchase prices', ['S82-M-Q2', 'S82-M-Q3']), ('Loan terms', ['S83-M-Q2']),
                     ('APR', ['S83-B1-Q4']), ('Total financing costs', ['S83-M-Q1']), ('Insurance', ['S88-M-Q1']),
                     ('Registration', ['S82-M-Q2']), ('Maintenance', ['S84-M-Q5']), ('Depreciation', ['S84-M-Q2']),
                     ('Leasing versus buying', ['S85-F2-Q3'])],
    'Filing taxes': [('W-2 and 1099 forms', ['S64-M-Q1', 'S64-M-Q2']), ('Withholding', ['S64-M-Q4']),
                     ('Taxable income', ['S66-M-Q3']), ('Filing requirements', ['S65-M-Q1']),
                     ('Filing status', ['S65-M-Q2']), ('Deductions and credits', ['S68-M-Q1']),
                     ('Filing methods', ['S70-M-Q2']), ('Tax refunds versus actual tax liability', ['S69-M-Q5'])],
}

ASSIGNMENT_EXAMPLES = [('Brokerage account (Schwab, Fidelity, E*TRADE)', 'S44-M-Q1'),
                       ('Jordan opening a Roth IRA (answer: compare eligible institutions)', 'S59-M-Q1'),
                       ('Taylor\'s $500 in the cash position (knowledge check; answer: purchased an investment)', 'S60-M-Q1'),
                       ('Simple interest: $2,400 at 5% for 3 years = $360', 'S23-M-Q1'),
                       ('Sales tax: $80 at 6.5% = $85.20 total', 'S19-M-Q3'),
                       ('Compound growth: $1,000 at 10% for 2 years = $1,210', 'S24-M-Q1')]

# Intros that name the correct term after defining several, reviewed by hand: the student must match a scenario to
# a definition (Learn and Apply), so these are not the answer handed over.
CLASSIFY_REVIEWED = {'S2-B1-Q1', 'S7-F1-Q1', 'S20-M-Q3', 'S25-F2-Q5', 'S27-F1-Q1', 'S41-M-Q1', 'S41-B1-Q5', 'S65-F1-Q1',
                     'S66-F1-Q2', 'S67-F1-Q4', 'S70-F1-Q1', 'S88-M-Q4', 'S93-F1-Q5', 'S97-M-Q1', 'S98-F1-Q1'}

TIME_HOSTS = ('nj.gov, njconsumeraffairs.gov, jumpstart.org, councilforeconed.org, irs.gov, consumerfinance.gov, fdic.gov, '
              'econedlink.org and similar sites')


# ------------------------------------------------------------------ helpers
def qmap(recs):
    return {r['id']: r for r in recs}


def sec_list(s):
    return [(c, sec) for c, sec in B.sections(s)]


def md_table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '|' + '|'.join('---' for _ in head) + '|']
    for r in rows:
        out.append('| ' + ' | '.join(str(x).replace('|', '\\|').replace('\n', ' ') for x in r) + ' |')
    return '\n'.join(out)


def write(name, text):
    with open(os.path.join(B.COL, name), 'w', encoding='utf-8') as f:
        f.write(text.rstrip() + '\n')


def counts_for(s):
    back = [b for b in s['back']]
    return dict(math=sum(1 for b in back if b['kind'] == 'math'), concept=sum(1 for b in back if b['kind'] == 'concept'),
                deeper=len(s['go']), questions=5 + 5 * sum(1 for b in back if b['kind'] == 'concept') + 5 * len(s['go']))


def check_ids(groups, by_id):
    missing = [q for steps in groups.values() for _, ids in steps for q in ids if q not in by_id]
    assert not missing, ('progression/walkthrough IDs not found', missing)


# ------------------------------------------------------------------ COVERAGE
def coverage(sets, recs):
    by_id = qmap(recs)
    check_ids(PROGRESSIONS, by_id)
    L = ['# Financial Literacy — Coverage Report', '',
         'Version %s, %s. %d sets, %d questions. **Status: not yet approved; awaiting independent review.**' % (
             B.VERSION, META.DATE, len(sets), len(recs)), '',
         '## How alignment was done', '',
         '- **National:** 2021 National Standards for Personal Financial Education (Council for Economic Education and '
         'Jump$tart Coalition), six topics: %s. Every set names its topic and a learning target. Outcome codes repeat '
         'across topics, so every code is written with its topic (for example "Earning Income 12-6a"). Codes are assigned '
         'only to the sets listed in the code table below; all other sets are aligned at topic level only. The author '
         'could not open the official PDF; each code says whether its wording came from search-indexed text or from the '
         'independent reviewer\'s reading of the PDF.' % ', '.join(META.NATIONAL_TOPICS),
         '- **New Jersey:** NJSLS — Career Readiness, Life Literacies, and Key Skills (adopted June 3, 2020), Standard 9.1 '
         'Personal Financial Literacy, grade 12 (9.1.12). Alignment is at the strand level (%s). Strand tags do not show '
         'coverage of all 55 grade-12 performance expectations; known gaps are listed in section 3a.' % ', '.join('%s %s' % kv for kv in META.NJ_STRANDS.items()),
         '- **Local identifiers:** codes such as FL.SAVE.24 are course identifiers, not official national or New Jersey codes.',
         '- **Section roles:** MAIN sections are the direct alignment; backward sections (concept and math) are supporting '
         'prerequisites; Go Deeper sections are related enrichment. The package does not claim full mastery of either standard.',
         '- **Verification limit:** the authoring environment could not open the official sites (%s); only web search '
         'results were available.' % TIME_HOSTS, '']
    # content areas
    L += ['## 1. The 20 required content areas', '']
    rows = []
    unit_sets = collections.defaultdict(list)
    for s in sets:
        unit_sets[s['unit']['code']].append(s)
    for i, a in enumerate(AREAS, 1):
        us = [u for u in D.UNITS if u['area'][0].split(' ', 1)[0] == str(i)]  # the unit whose main area this is
        if i in AREA_SETS:  # the Investing unit covers two required areas
            us = [u for u in D.UNITS if u['code'] == 'INVEST']
            ss = [s for s in sets if s['num'] in AREA_SETS[i]]
        else:
            ss = [s for u in us for s in unit_sets[u['code']]]
        rows.append([i, a, ', '.join('%s (%s)' % (u['title'], u['code']) for u in us) or '—',
                     ', '.join('S%d' % s['num'] for s in ss), sum(counts_for(s)['questions'] for s in ss)])
    L += [md_table(['#', 'Required area', 'Unit(s)', 'Sets', 'Questions'], rows), '',
          'Areas 5 and 18 are also reinforced inside other units: interest calculations in Saving (S23-S27) and economic '
          'decision-making in Budgeting (S19-S20).', '']
    # national matrix
    L += ['## 2. National Standards matrix (topic level)', '']
    rows = []
    for t in META.NATIONAL_TOPICS:
        ss = [s for s in sets if s['nat'][0] == t]
        rows.append([t, len(ss), sum(counts_for(s)['questions'] for s in ss), ', '.join('S%d' % s['num'] for s in ss)])
    L += [md_table(['Topic', 'Set count', 'Questions', 'Sets'], rows), '']
    rows = [['%s %s' % (tp, c), d, st, ', '.join('S%d' % s['num'] for s in sets if s['nat'][0] == tp and c in s['nat'][1]) or '—']
            for (tp, c), (d, st) in sorted(META.NATIONAL_CODES.items())]
    L += ['Assigned 12th-grade outcome codes (topic-qualified):', '',
          md_table(['Code', 'Outcome', 'How checked', 'Sets'], rows), '']
    # NJ matrix
    L += ['## 3. New Jersey 9.1.12 strand matrix', '']
    rows = []
    for c, name in META.NJ_STRANDS.items():
        ss = [s for s in sets if c in s['nj']]
        rows.append(['9.1.12.%s' % c, name, len(ss), ', '.join('S%d' % s['num'] for s in ss)])
    L += [md_table(['Strand', 'Name', 'Set count', 'Sets'], rows), '']
    L += ['### 3a. Known New Jersey gaps (disclosed)', '',
          'From the independent review of the official 9.1 PDF. These are outside or only partly inside this course; '
          'the course does not claim them.', '',
          md_table(['Expectation', 'Topic', 'Coverage'], [list(g) for g in META.NJ_GAPS]), '']
    # per set
    L += ['## 4. Set-by-set alignment and counts', '']
    rows = []
    for s in sets:
        c = counts_for(s)
        rows.append(['S%d' % s['num'], s['title'], s['nat'][0], ', '.join(s['nj']), c['concept'], c['math'], c['deeper'],
                     c['questions'], 'time-sensitive' if s['status'] == 'time_sensitive' else 'stable'])
    L += [md_table(['Set', 'Title', 'National topic', 'NJ strands', 'Concept branches', 'Math links', 'Go Deeper',
                    'Questions', 'Content'], rows), '']
    # progressions
    L += ['## 5. Required progressions (assignment Part 4)', '',
          'Each step of the assignment\'s detailed progressions, with the question(s) that teach it. Questions are '
          'listed by ID (see the answer key).', '']
    for title, steps in PROGRESSIONS.items():
        L += ['### ' + title, '', md_table(['Step', 'Topic', 'Question(s)', 'Question text (first)'],
                                           [[i, t, ', '.join(ids), by_id[ids[0]]['question'][:110]]
                                            for i, (t, ids) in enumerate(steps, 1)]), '']
    L += ['### The assignment\'s worked examples', '',
          md_table(['Example', 'Question', 'Correct answer'],
                   [[e, q, by_id[q]['correct_answer']] for e, q in ASSIGNMENT_EXAMPLES]), '']
    # practical skills
    L += ['## 6. Practical skills beyond the standards', '']
    rows = [['S%d' % s['num'], s['title'], '; '.join(s['extra'])] for s in sets if s['extra']]
    L += [md_table(['Set', 'Title', 'Practical skills'], rows), '']
    # prerequisites summary
    nm = sum(counts_for(s)['math'] for s in sets)
    nc = sum(counts_for(s)['concept'] for s in sets)
    nd = sum(counts_for(s)['deeper'] for s in sets)
    L += ['## 7. Prerequisites and enrichment (summary)', '',
          '- Math prerequisite links: %d (to %d distinct game skills). See MATH_BRANCHES.md.' % (
              nm, len({(b['ref']['course'], b['ref']['set']) for s in sets for b in s['back'] if b['kind'] == 'math'})),
          '- Financial-concept prerequisite branches: %d. See CONCEPT_BRANCHES.md.' % nc,
          '- Go Deeper sections: %d (chains of 1 to %d). See GO_DEEPER.md.' % (nd, max(len(s['go']) for s in sets)), '']
    # difficulty
    kinds = collections.Counter(r['section_kind'] for r in recs)
    types = collections.Counter(r['question_type'] for r in recs)
    L += ['## 8. Question counts and difficulty', '',
          md_table(['Level', 'Where', 'Questions'],
                   [['Foundational', 'Concept prerequisite branches (B)', kinds['concept']],
                    ['Core', 'MAIN sections (M)', kinds['main']],
                    ['Deeper', 'Go Deeper sections (F1, F2, ...)', kinds['go_deeper']]]), '',
          md_table(['Question type', 'Questions'], [['Learn and Apply (intro + question)', types['instruction']],
                                                     ['Knowledge Check (no intro)', types['knowledge_check']],
                                                     ['Practical how-to (subset)', sum(1 for r in recs if r['how_to'])],
                                                     ['Computed answers checked by the build (calc)',
                                                      sum(1 for r in recs if r['calc'] is not None)]]), '']
    write('COVERAGE.md', '\n'.join(L))


# ------------------------------------------------------------------ MATH
def math_report(sets):
    val = json.load(open(os.path.join(B.COL, 'MATH_REF_VALIDATION.json')))
    live = {(x['fl_set'], x['section']): x for x in val['rows']}
    run = json.load(open(os.path.join(B.COL, 'RUNTIME_CHECK.json')))
    rows, by_course, missing = [], collections.Counter(), []
    for s in sets:
        for i, b in enumerate(s['back'], 1):
            if b['kind'] != 'math':
                continue
            r = b['ref']
            sid = '%s-S%02d-M' % (B.COURSE_PREFIX[r['course']], r['set'])
            c = B.CATALOG[sid]
            by_course[r['course']] += 1
            v = live.get((s['num'], 'B%d' % i))
            if not v or v.get('skill_id') != sid:
                missing.append('S%d B%d' % (s['num'], i))
                check = 'NOT RE-CHECKED'
            else:
                check = '%s; %d of %d auto-checkable (%s)' % (v['status'], v['auto_checkable'], v['main_questions'],
                                                             ', '.join('%s %d' % kv for kv in sorted(v['types'].items())))
            rows.append(['S%d' % s['num'], 'B%d' % i, sid, c['ccss'], c['name'], b['why'], check])
    few = val['targets_with_fewer_than_5_auto_checkable']
    s24 = run['s24']
    L = ['# Financial Literacy — Math Prerequisite Branches', '',
         'A math branch is a backward section with `"kind": "math"` and a `ref` to a MAIN skill that is already in Untangle '
         'The Nexus. It has no questions of its own; the game sends the student to that skill. The package writes the '
         'section as `M`; the game\'s importer maps it to the skill ID `<course>-S<set>-M` (for example `G6-S40-M`), '
         'which is the MAIN section that the math answer keys call `MAIN`.', '',
         'The branch fires only under the game\'s existing rule: **3 or fewer correct out of 5** on MAIN '
         '(`backwardWhenIncorrectAtLeast: 2`). The student then works every backward section of the set in order. '
         'This package does not change that rule.', '',
         '## 1. Checked against the installed game (not just the catalog)', '',
         '- **Every link resolved in the live game content.** %d links to %d distinct skills were checked with the game\'s '
         'own code (`COURSES`, `bankKey`, `isAutoCheckable`) against `untangle-the-nexus` commit %s: %s. %s' % (
             val['links'], val['distinct_targets'], val['game_commit'],
             ', '.join('%s: %d' % kv for kv in val['status'].items()),
             'All links in this version were re-checked.' if not missing else 'Not re-checked: ' + ', '.join(missing)),
         '- **The reviewer\'s "absent target" list.** Grade 7 sets 63, 65, and 66 exist in the installed Grade 7 bank '
         '(bank version 2.0.0, standard 7.RP.A.3); the reviewer\'s copies were older uploads. The Algebra I set 75 link '
         '(S67) was removed in v1.1 because a step function is not a real obstacle to the marginal-rate skill.',
         '- **What the student sees.** In backward mode the game serves only auto-checkable questions from the target '
         'skill (`requireAutoCheck`): multiple choice, true/false, and short typed numeric answers. It never asks for a '
         'written or recorded explanation there (`requiresExplanation` is false for backward work). Short typed answers '
         'are the target skill\'s own supported format; they are not multiple choice. **Owner decision needed:** accept '
         'typed numeric answers inside math remediation, or ask the game team for a choice-only filter. This package does '
         'not substitute unrelated multiple-choice questions.',
         '- **Repeats.** %d target skills have fewer than 5 auto-checkable MAIN questions (%s). Because a branch needs 5 '
         'correct in a row, the game repeats some of those items. This is existing game behavior.' % (
             len(few), ', '.join('%s %d of %d' % (k, v['auto_checkable'], v['main']) for k, v in few)),
         '- **Runtime test (real importer and game server, PostgreSQL).** The full package imported with %d sets, %d '
         'questions, %d invalid, %d warnings. On S24, 3 of 5 correct sent the student through %s in that order (kinds %s), '
         'matching the curriculum\'s backward edges, with no explanation required; afterwards the student returned to %s. '
         'Then 5 of 5 recorded mastery (%d) with the normal reward of %d seconds, and Go Deeper %s became available; Go '
         'Deeper questions showed their intro exactly when the bank has one. Details: `RUNTIME_CHECK.json`.' % (
             run['import']['sets'], run['import']['questions'], len(run['import']['invalid']), len(run['import']['warnings']),
             ' -> '.join(s24['seen']), ', '.join(s24['kinds']), s24['returnedTo'][1], run['mastery']['mastered'],
             run['mastery']['award'], ', '.join(run['mastery']['forwardAvailable'])),
         '- **Grade 6** was imported into the game from PDFs and has no bank version number, so its links are identified '
         'by skill ID and a hash of its question file (in `MATH_REF_VALIDATION.json`).', '',
         '## 2. Links by course', '', md_table(['Course', 'Links'], sorted(by_course.items())), '',
         '## 3. Every link', '',
         md_table(['Set', 'Section', 'Game skill', 'Standard', 'Skill name', 'Why it is needed', 'Live game check'], rows)]
    write('MATH_BRANCHES.md', '\n'.join(L))


# ------------------------------------------------------------------ CONCEPT
def concept_report(sets, recs):
    by_id = qmap(recs)
    rows = []
    for s in sets:
        for i, b in enumerate(s['back'], 1):
            if b['kind'] != 'concept':
                continue
            ids = ['S%d-B%d-Q%d' % (s['num'], i, k) for k in range(1, 6)]
            rows.append(['S%d' % s['num'], 'B%d' % i, b['skill'], b['why'],
                         '; '.join(by_id[q]['subtopic'] for q in ids)])
    L = ['# Financial Literacy — Concept Prerequisite Branches', '',
         'A concept branch is a backward section with `"kind": "concept"`: five simpler questions about a money idea the '
         'MAIN skill rests on. They carry their own questions because the importer does not resolve links between sets '
         'of the same course. Concept branches never link to other sets, so there are no circular or broken references. '
         'Each set lists its concept branch first and its math links after it, so a student reviews the money idea and '
         'then the arithmetic.', '', md_table(['Set', 'Section', 'Branch skill', 'Why it is needed', 'Subtopics'], rows)]
    write('CONCEPT_BRANCHES.md', '\n'.join(L))


# ------------------------------------------------------------------ GO DEEPER
def deeper_report(sets):
    rows = [['S%d' % s['num'], s['title'], len(s['go']),
             ' → '.join('F%d %s' % (i, g['skill']) for i, g in enumerate(s['go'], 1))] for s in sets]
    L = ['# Financial Literacy — Go Deeper Chains', '',
         'Forward sections are labeled **Go Deeper** (`display_label`) and unlock after MAIN is mastered (5 of 5). They '
         'stay on the same topic and form a chain F1 → F2 → … Each has five questions. Total: %d sections.' % sum(
             len(s['go']) for s in sets), '', md_table(['Set', 'Topic', 'Sections', 'Chain'], rows)]
    write('GO_DEEPER.md', '\n'.join(L))


# ------------------------------------------------------------------ HOW-TO
def howto_report(sets, recs):
    by_id = qmap(recs)
    check_ids(WALKTHROUGHS, by_id)
    L = ['# Financial Literacy — Practical How-To Coverage', '',
         'How-to instruction is inside the regular questions (no separate "Show Me How" feature, no videos). The short '
         'explanation is the question\'s `intro`, shown on the same screen. All people, accounts, and numbers are '
         'fictional; no question asks a student for real personal or account information. Real firms are named only as '
         'examples, never as recommendations (see S45-F1-Q5).', '', '## The five required walkthroughs', '']
    for title, steps in WALKTHROUGHS.items():
        L += ['### ' + title, '', md_table(['Step', 'Question(s)', 'Question text'],
                                           [[t, ', '.join(ids), by_id[ids[0]]['question'][:120]] for t, ids in steps]), '']
    L += ['## Every how-to question (%d)' % sum(1 for r in recs if r['how_to']), '']
    rows = [[r['id'], r['unit'], r['subtopic'], r['question'][:110]] for r in recs if r['how_to']]
    L += [md_table(['ID', 'Unit', 'Subtopic', 'Question'], rows)]
    write('HOW_TO.md', '\n'.join(L))


# ------------------------------------------------------------------ QUALITY
def quality_report(sets, recs):
    a = B.audit(recs)
    global SIB
    SIB = B.sibling_scan(recs)
    letters = collections.Counter(r['correct_letter'] for r in recs)
    L = ['# Financial Literacy — Question and Distractor Quality Audit', '',
         'Automatic checks run on every build (`engine/fl_build.py`). A build with any failure stops and writes nothing.', '',
         '## Enforced on every question', '',
         '- Four choices (A-D), exactly one correct; the three wrong choices are distinct from each other and from the '
         'correct one.',
         '- Every wrong choice has a written misconception (%d notes in all).' % sum(len(r['misconceptions']) for r in recs),
         '- No "all of the above", "none of the above", "both of these", and no text naming a letter (the game shuffles '
         'choices, and such wording would switch shuffling off).',
         '- Every question has feedback. Exactly repeated question stems are refused. This is an exact-text check: it '
         'does not prove that two differently worded questions test different things.',
         '- Every computed answer (%d questions) has a recomputation (`calc`). The build checks that the correct choice '
         'shows that value at the precision printed and that no wrong choice shows the same value (except labeled '
         'comparisons such as "Job A, by $17.50"). This only proves the stored answer matches the stored formula. It does '
         'not prove the question states every given a student needs, or that the formula models the situation correctly; '
         'those were read by hand and by the independent reviewer.' % sum(1 for r in recs if r['calc'] is not None),
         '- Every math link exists in `engine/fl_math_catalog.json`. A catalog match is not proof that the game can serve '
         'it; the links were also checked in the installed game and in a real import and play-through (see '
         '`MATH_BRANCHES.md`, `MATH_REF_VALIDATION.json`, `RUNTIME_CHECK.json`).',
         '- Every set has at least one backward branch and one Go Deeper section; time-sensitive sets cite sources '
         '(claim-level status in `SOURCE_LEDGER.md`).', '',
         '## Answer positions', '',
         md_table(['Letter', 'Correct answers'], sorted(letters.items())), '',
         'Numeric choices are listed in increasing order, so their letter follows from the value. Other questions put the '
         'correct choice in the least-used letter so far, with ties broken by a hash of the ID.', '',
         '## Length cues', '',
         'For the %d questions whose choices are text (not plain numbers):' % a['text_items'], '',
         '- Correct answer is the unique longest choice: %d (%.0f%%; a random position would give about 25%%).' % (
             len(a['longest']), 100 * len(a['longest']) / a['text_items']),
         '- Correct answer is the unique shortest choice: %d (%.0f%%).' % (len(a['shortest']), 100 * len(a['shortest']) / a['text_items']),
         '', 'By unit:', '']
    longest = set(a['longest'])
    tot, fl = collections.Counter(), collections.Counter()
    for r in recs:
        if not B.is_numeric([c['text'] for c in r['choices']]):
            tot[r['unit']] += 1
            fl[r['unit']] += r['id'] in longest
    L += [md_table(['Unit', 'Text questions', 'Correct is longest', 'Share'],
                   [[u, tot[u], fl[u], '%.0f%%' % (100 * fl[u] / tot[u])] for u in tot]), '']
    echoed = a['echoed']
    L += ['## Intros', '',
          '- Learn and Apply questions: %d; intro length %s words (min, median, max).' % (a['instruction'], a['intro_words']),
          '- Knowledge checks (no intro): %d. They test earlier sets, the same set\'s MAIN skill (from a Go Deeper section), '
          'or information given in the question itself.' % a['knowledge_check'],
          '- Intros never state the answer to a recall question. %d intros contain the correct choice\'s wording; each was '
          'reviewed by hand and is a classification item, where the intro defines several terms and the student must '
          'match a scenario to one: %s.' % (len(echoed), ', '.join(echoed)),
          '- Unreviewed echoes: %s.' % (', '.join(sorted(set(echoed) - CLASSIFY_REVIEWED)) or 'none'), '',
          '## Self-containment (shuffled questions)', '',
          'The game serves the five questions of a section in shuffled order, so every question must stand alone. The '
          'v1.0.0 audit claimed this without a working check, and the reviewer found missing givens in the questions '
          'listed under R18, R29, and R31. What was done for v1.1:', '',
          '- Every question the reviewer listed was rewritten to restate its own numbers and conditions.',
          '- A broader hand read of 127 candidate stems (those with he/she/her/his, "the", or a number that could come '
          'from a sibling) during the v1.1 corrections.',
          '- An automatic scan on every build (`sibling_scan` in `engine/fl_build.py`) for stems that point at another '
          'question ("the same loan", "above", "as before") or use he/she/her/his with no named person. Result this '
          'build: %d flagged, %d reviewed as fine (the comparison is inside the question), %d open.' % (
              len(SIB['flagged']), len(SIB['flagged']) - len(SIB['open']), len(SIB['open'])),
          '- Limits: the scan is a pattern search, not a reading test. It cannot catch a question that silently relies '
          'on an idea defined only in a sibling\'s intro. That still needs a human spot-check.', '',
          '## Distractor review', '',
          'Wrong choices were rewritten so that each represents a real misunderstanding (for example: confusing a bank '
          'account with a brokerage account, funding with investing, simple with compound interest, APR with a monthly rate, '
          'gross with net income, a refund with extra income, a premium with a deductible, preapproval with final approval, '
          'or diversification with a guarantee). A few safety questions keep a clearly unsafe action as a choice on purpose '
          '(for example, sharing a bank login with a lender); their notes say "Unsafe."', '',
          '## Time-sensitive content', '',
          'Rules that change are stated as of a date or as a hypothetical amount (for example, "Assume a $7,000 IRA limit"). '
          'Sets marked time-sensitive, with their sources:', '']
    rows = [['S%d' % s['num'], s['title'], '; '.join('%s (%s)' % (x['org'], x['url']) for x in s['sources'])]
            for s in sets if s['status'] == 'time_sensitive']
    L += [md_table(['Set', 'Title', 'Sources'], rows), '',
          '## Checks that actually ran for v1.1', '',
          '- Build validators above (every build).',
          '- Game importer `--check` on the package and a full import into a test database (`RUNTIME_CHECK.json`).',
          '- Math links re-checked against the installed game with its own code (`MATH_REF_VALIDATION.json`).',
          '- Package check (`engine/verify_package.py`) and cross-export check (`engine/fl_crosscheck.py`, result in '
          '`EXPORT_CROSSCHECK.json`): every question has the same ID, choices, key, and page in the package JSON, the '
          'answer-key JSON and CSV, the full question and answer PDFs, and the split part PDFs.',
          '- Sibling scan (above).', '',
          '## What still needs a human reviewer', '',
          '- Confirm national outcome codes and New Jersey performance expectations against the official documents.',
          '- Confirm each source claim and effective date: %d of %d claim rows in `SOURCE_LEDGER.md` are still '
          '"unverified" (the build environment could not open the official sites).' % (
              sum(1 for r in LEDGER.rows(sets) if r['verification_level'] == 'unverified'), len(LEDGER.rows(sets))),
          '- Semantic duplicates: no automatic check finds two questions that test the same thing in different words.',
          '- Read the explanations for tone and reading level, and judge whether any distractor is still too easy.',
          '- Spot-check the knowledge checks for anything not yet taught at that point in the pathway.']
    write('QUALITY_AUDIT.md', '\n'.join(L))


# ------------------------------------------------------------------ README
def readme(sets, recs):
    n_concept = sum(1 for s in sets for b in s['back'] if b['kind'] == 'concept')
    n_math = sum(1 for s in sets for b in s['back'] if b['kind'] == 'math')
    n_f = sum(len(s['go']) for s in sets)
    L = ['# Untangle The Nexus — High School Financial Literacy (FL) v%s' % B.VERSION, '',
         '**Review status: NOT APPROVED. Release pending recheck.** Version 1.0.0 was independently reviewed (ChatGPT). '
         'This version 1.1.0 applies that review: every finding and its fix is in `REVIEW_RESPONSE.md`, and every changed '
         'question is in `CHANGES.md`. Passing the build checks does not mean the content is fact-checked. The revised '
         'package must be rechecked and approved by the owner before import; do not overwrite a live course with it. The '
         'game keeps the course "coming soon" until then.', '',
         '## What is here', '',
         md_table(['#', 'Deliverable', 'File'], [
             [1, 'Question PDF', 'FinancialLiteracy_Question_Collection.pdf (and pdf/ parts in the package)'],
             [2, 'Answer key PDF', 'FinancialLiteracy_Answer_Key.pdf'],
             [3, 'JSON answer key', 'FinancialLiteracy_Answer_Key.json'],
             [4, 'CSV answer key', 'FinancialLiteracy_Answer_Key.csv'],
             [5, 'Nexus import ZIP', 'nexus/' + ZIP_NAME],
             [6, 'Standards coverage report', 'COVERAGE.md'],
             [7, 'Math prerequisite branch report', 'MATH_BRANCHES.md'],
             [8, 'Concept prerequisite branch report', 'CONCEPT_BRANCHES.md'],
             [9, 'Go Deeper report', 'GO_DEEPER.md'],
             [10, 'How-to coverage report', 'HOW_TO.md'],
             [11, 'Question and distractor quality audit', 'QUALITY_AUDIT.md'],
             [12, 'This README', 'README.md'],
             [13, 'Response to the independent review (every R, C, P item)', 'REVIEW_RESPONSE.md'],
             [14, 'Change log by question ID (old/new key, reason, source)', 'CHANGES.md, CHANGES.json'],
             [15, 'Claim-level source ledger', 'SOURCE_LEDGER.md, SOURCE_LEDGER.json'],
             [16, 'Math links checked in the installed game', 'MATH_REF_VALIDATION.json'],
             [17, 'Import and play-through test in the real game server', 'RUNTIME_CHECK.json'],
             [18, 'Cross-export consistency check', 'EXPORT_CROSSCHECK.json']]), '',
         '## Size', '',
         '%d units, %d sets, %d questions: %d MAIN sections, %d concept prerequisite branches, %d math prerequisite links, '
         'and %d Go Deeper sections.' % (len(D.UNITS), len(sets), len(recs), len(sets), n_concept, n_math, n_f), '',
         md_table(['Unit', 'Title', 'Sets'], [[u['code'], u['title'], ', '.join('S%d' % s['num'] for s in sets
                                                                              if s['unit']['code'] == u['code'])]
                                             for u in D.UNITS]), '',
         '## How it fits the game (existing rules, unchanged)', '',
         '- Course `financial_literacy` (prefix FL), already registered in the game as "coming soon," multiple choice only '
         '(`responseMode: choice`): no video recording and no "Show Me How."',
         '- A set is one MAIN skill. A student answers 5 MAIN questions.',
         '  - 5 correct: mastered; the Go Deeper chain unlocks.',
         '  - 4 correct: a fresh MAIN attempt.',
         '  - **3 or fewer correct: backward branches.** This is the game\'s Financial Literacy setting '
         '`backwardWhenIncorrectAtLeast: 2` (2 or more wrong); this package does not change it. The student works every '
         'backward section of the set in package order, each passed with 5 correct in a row, then returns to a fresh MAIN.',
         '- Backward sections are of two kinds: `"kind": "concept"` (five simpler money questions in this package) and '
         '`"kind": "math"` (a `ref` to an existing math MAIN skill in Grades 3-8 or Algebra I; no questions).',
         '- Forward sections F1, F2, … are labeled "Go Deeper" and stay on the same topic.',
         '- Teaching text is the question\'s `intro`, shown above the question on the same screen. The explanation after '
         'answering is `feedback`. Questions with an intro are "Learn and Apply"; questions without one are "Knowledge '
         'Checks."',
         '- The game serves a section\'s five questions in shuffled order and may shuffle the choices, so every question '
         'stands alone and no text refers to a letter.', '',
         '## Package format', '',
         'Same as the Grade 3-8 packages (format_version 1): `index.json` (with `"course": "financial_literacy"` and '
         '`bank_version`) plus `sets/S01.json` … `sets/S%d.json`. IDs are `S<set>-<section>-Q<n>`; uids add `FL:`.' % len(sets), '',
         'Fields this package adds (all optional in the game, stored as-is):', '',
         md_table(['Where', 'Field', 'Meaning'], [
             ['question', 'intro', 'Short teaching passage shown before answering'],
             ['question', 'feedback', 'Explanation shown after answering'],
             ['question', 'question_type', '"instruction" (Learn and Apply) or "knowledge_check"'],
             ['question', 'topic, subtopic', 'Set title and the question\'s specific idea'],
             ['question', 'misconceptions', '{letter: misconception} for each wrong choice'],
             ['question', 'practical_how_to', 'true for practical how-to questions'],
             ['question', 'sources, effective_date', 'Sources for changing rules and the date they are stated as of'],
             ['question', 'page', 'Page in the question and answer PDFs'],
             ['set', 'alignment', 'National topic, learning target, topic-qualified outcome codes with how each was checked; NJ 9.1.12 strands; local identifier note'],
             ['set', 'content_status', '"stable" or "time_sensitive"'],
             ['set', 'sources', 'Organization, URL, claim, effective date, and verification status'],
             ['set', 'practical_skills', 'Practical skills beyond the standards'],
             ['section', 'kind, relationship', 'Backward branch type and why it is needed'],
             ['section', 'ref, ref_skill', 'Math link target and its standard and name'],
             ['section', 'display_label, difficulty', '"Go Deeper n" and "deeper" on forward sections']]), '',
         'Not supported by the importer, so not used: links from one Financial Literacy set to another (a concept branch '
         'always carries its own five questions).', '',
         '## Standards', '', META.STANDARDS_NOTE + ' Details and the full matrix are in COVERAGE.md.', '',
         '## Sources and changing rules', '',
         'Sources are federal and state agencies and regulators: IRS, CFPB, FDIC, NCUA, SEC, FINRA, SIPC, Federal Student '
         'Aid, FTC, NHTSA, Social Security Administration, Federal Reserve, BLS, HealthCare.gov, and New Jersey agencies '
         '(Division of Taxation, Division of Consumer Affairs, DOBI, HESAA, Get Covered New Jersey). Each time-sensitive set '
         'lists its sources with the claim used. Amounts that change often (IRA and 401(k) limits, tax brackets, standard '
         'deductions, Roth income limits, mileage rates) are given as stated hypothetical amounts so the questions stay '
         'correct; real figures are stated "as of" a date.', '',
         '**Verification limit:** the authoring environment\'s network policy blocked the official sites (%s). Claims were '
         'written from knowledge and checked against web search results only. Each source in the package carries '
         '`verification` (reviewer-checked topic, search-corroborated, or unverified), `verification_detail`, and '
         '`verified_on: null`; the claim-level list is `SOURCE_LEDGER.md` / `.json`. To let a future session verify them, allow those hosts in the '
         'environment\'s network settings, or upload the official PDFs (the National Standards, NJSLS 9.1) to the '
         'repository.' % TIME_HOSTS, '',
         '## Known limitations', '',
         '- National outcome codes are assigned to a few sets only, written with their topic, and none was checked by the '
         'author against the official PDF. NJ alignment is at the strand level, and known NJ gaps are listed in '
         'COVERAGE.md section 3a. The course does not claim full mastery of either standard.',
         '- Math remediation uses the target skill\'s own question types (multiple choice, true/false, typed numbers); '
         'see MATH_BRANCHES.md.',
         '- Source claims and effective dates need a reviewer\'s confirmation (see above). Some federal rules changed in '
         '2025-2026 (for example, student loan repayment plans); those questions say to check the official site.',
         '- Real company names (Charles Schwab, Fidelity, E*TRADE, Vanguard, Experian, and others) appear as examples only, '
         'never as endorsements.',
         '- Misconception notes are stored for future use; the game does not route by them today.', '',
         '## Rebuild and check', '', '```',
         'python3 question-bank/engine/fl_build.py          # validate, keys, package, PDFs, reports, ZIP',
         'python3 question-bank/engine/fl_build.py --quick  # validate, keys, package only',
         'cd untangle-the-nexus && npx tsx tools/import-collection/import.ts --check <path to the ZIP>', '```', '',
         'Source files: `question-bank/financial_literacy/src/u*.py` (one module per unit); constructors in '
         '`engine/fl_dsl.py`; metadata in `financial_literacy/src/fl_meta.py`.', '',
         '## Importing into the game (after approval only)', '',
         'Follow the game\'s docs/FINANCIAL-LITERACY.md, Phase C: upload the ZIP to the work branch, run the importer, '
         'confirm 0 invalid and review warnings, run the tests, play it as the creator, and only then ask the owner '
         'before setting the course to available.']
    write('README.md', '\n'.join(L))


def write_all(sets, recs):
    coverage(sets, recs)
    math_report(sets)
    concept_report(sets, recs)
    deeper_report(sets)
    howto_report(sets, recs)
    quality_report(sets, recs)
    by_id = qmap(recs)
    bad = [(s['num'], q) for s in sets for x in s['sources'] for q in x.get('qids', []) if q not in by_id]
    assert not bad, ('source qids not found', bad)
    LEDGER.write(sets, B.COL, md_table)
    review_and_changes(sets, recs)
    readme(sets, recs)


# ------------------------------------------------------------------ package
def finish_package(pkg):
    for name in REPORTS + ['README.md']:
        shutil.copy(os.path.join(B.COL, name), os.path.join(pkg, name))
    files = []
    for root, _, names in os.walk(pkg):
        for n in sorted(names):
            p = os.path.join(root, n)
            rel = os.path.relpath(p, pkg).replace(os.sep, '/')
            if rel == 'MANIFEST.json':
                continue
            data = open(p, 'rb').read()
            files.append(dict(path=rel, bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    files.sort(key=lambda f: f['path'])
    json.dump(dict(collection='FL', course='financial_literacy', version=B.VERSION, file_count=len(files), files=files),
              open(os.path.join(pkg, 'MANIFEST.json'), 'w'), indent=1)
    zpath = os.path.join(os.path.dirname(pkg), ZIP_NAME)
    base = os.path.basename(pkg)
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, names in os.walk(pkg):
            dirs.sort()
            rel_root = os.path.relpath(root, os.path.dirname(pkg))
            z.write(root, rel_root + '/')
            for n in sorted(names):
                z.write(os.path.join(root, n), os.path.join(rel_root, n))
    print('wrote', zpath)


# ------------------------------------------------------------------ REVIEW RESPONSE + CHANGES
def _review():
    import importlib.util
    d = os.path.join(B.SRC, 'review')
    spec = importlib.util.spec_from_file_location('response_v1_1', os.path.join(d, 'response_v1_1.py'))
    resp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resp)
    text = open(os.path.join(d, 'independent_review_v1.0.0.md'), encoding='utf-8').read()
    named = collections.OrderedDict()
    for m in re.finditer(r'^(?:### |\*\*)([RC]\d\d) — (.*)$', text, re.M):
        named[m.group(1)] = re.findall(r'`(S\d+-[A-Z0-9]+-Q\d)`', m.group(2))
    issues = {}
    for m in re.finditer(r'^### (R\d\d) — .*\n\n\*\*Issue:\*\* (.*)$', text, re.M):
        issues[m.group(1)] = m.group(2)
    for m in re.finditer(r'^\*\*(C\d\d) — [^*]*\*\* ?(.*)$', text, re.M):
        issues[m.group(1)] = m.group(2)
    old = {r['id']: r for r in json.load(open(os.path.join(B.SRC, 'review', 'key_v1.0.0_full.json')))}
    oldorder = json.load(open(os.path.join(B.SRC, 'review', 'choice_order_v1.0.0.json')))['order']
    return resp, named, issues, old, oldorder


def _diff(o, oo, n):
    """Fields that changed between v1.0.0 (o: key record, oo: choice order) and v1.1.0 (n)."""
    f = []
    if o['question'] != n['question']:
        f.append('question')
    if sorted(oo) != sorted(c['text'] for c in n['choices']):
        f.append('choices')
    if o['correct_answer'] != n['correct_answer']:
        f.append('correct answer')
    if o['correct_letter'] != n['correct_letter']:
        f.append('letter')
    return f


def review_and_changes(sets, recs):
    resp, named, issues, old, oldorder = _review()
    by_id = qmap(recs)
    owner = collections.defaultdict(list)
    for k, ids in named.items():
        for q in ids:
            owner[q].append(k)
    for q, k in resp.EXTRA.items():
        owner[q].append(k)
    # fields beyond question/choices/answer come from comparing the full v1.0.0 key kept in git history
    full_old = {r['id']: r for r in json.load(open(os.path.join(B.SRC, 'review', 'key_v1.0.0_full.json')))}
    rows = []
    for r in recs:
        o, n = full_old[r['id']], r
        f = _diff(old[r['id']], oldorder[r['id']], n)
        for k, label in (('intro', 'intro'), ('feedback', 'feedback'), ('how_to', 'how-to flag'), ('misconceptions', 'misconception notes')):
            if (o.get(k) or '') != (n.get(k) or ''):
                f.append(label)
        if not f:
            continue
        fnd = owner.get(r['id'], [])
        assert fnd, ('changed question with no finding', r['id'], f)
        answer_changed = o['correct_answer'] != n['correct_answer']
        rows.append(dict(id=r['id'], findings=fnd, fields=f,
                         old_key='%s: %s' % (o['correct_letter'], o['correct_answer']),
                         new_key='%s: %s' % (n['correct_letter'], n['correct_answer']),
                         change_type='answer changed' if answer_changed else
                                     ('key letter moved (numeric choices re-sorted), same answer' if 'letter' in f else
                                      'wording, givens, or teaching only; same answer'),
                         reason='; '.join('%s: %s' % (k, (resp.R.get(k) or (resp.C[k][1] if k in resp.C else resp.P[k][1]))[:220]) for k in fnd),
                         source=', '.join(resp.SOURCE_REF[k] for k in fnd if k in resp.SOURCE_REF) or None))
    json.dump(dict(from_version='1.0.0', to_version=B.VERSION, question_ids_preserved=True, changed=len(rows),
                   note='Unchanged questions keep their v1.0.0 choice order and answer letter.', changes=rows),
              open(os.path.join(B.COL, 'CHANGES.json'), 'w'), indent=1, ensure_ascii=False)
    cnt = collections.Counter(x['change_type'] for x in rows)
    L = ['# Financial Literacy — Changes from v1.0.0 to v%s (by question ID)' % B.VERSION, '',
         'Every question whose text, choices, key, intro, feedback, how-to flag, or misconception notes changed. Question '
         'IDs are unchanged. Unchanged questions keep their v1.0.0 choice order and answer letter. Machine-readable: '
         '`CHANGES.json`.', '',
         '%d questions changed: %s.' % (len(rows), ', '.join('%s %d' % kv for kv in cnt.most_common())), '',
         md_table(['Question', 'Finding', 'Changed', 'Old key', 'New key', 'Type', 'Source'],
                  [[x['id'], ', '.join(x['findings']), ', '.join(x['fields']), x['old_key'], x['new_key'], x['change_type'],
                    x['source'] or '—'] for x in rows]), '']
    write('CHANGES.md', '\n'.join(L))
    # response table
    by_f = collections.defaultdict(list)
    for x in rows:
        for k in x['findings']:
            by_f[k].append(x['id'])
    L = ['# Financial Literacy v%s — Response to the Independent Review' % B.VERSION, '',
         '**Release status: pending recheck.** Every R finding, C recommendation, and P requirement in '
         '`independent_review_v1.0.0.md` is listed below with the questions affected and what was done. Per-question '
         'detail (old and new key, fields changed) is in `CHANGES.md`. Nothing in this table claims the content is now '
         'fact-checked; source status is in `SOURCE_LEDGER.md`.', '',
         '## Summary', '',
         '- R findings: %d of %d fixed (no finding rejected).' % (len(resp.R), len([k for k in named if k[0] == 'R'])),
         '- C recommendations: %d of %d adopted.' % (sum(1 for v in resp.C.values() if v[0] == 'Adopted'),
                                                    len([k for k in named if k[0] == 'C'])),
         '- P requirements: all 6 addressed; limits are stated in each row.',
         '- %d questions changed in all; %d of them have a different correct answer.' % (
             len(rows), cnt['answer changed']), '',
         '## R — required corrections', '',
         md_table(['Finding', 'Questions named', 'Also changed', 'Reviewer issue (short)', 'What was done'],
                  [[k, ', '.join(named[k]), ', '.join(q for q in by_f[k] if q not in named[k]) or '—',
                    (issues.get(k, '')[:180] + ('…' if len(issues.get(k, '')) > 180 else '')), resp.R[k]]
                   for k in named if k[0] == 'R']), '',
         '## C — recommendations', '',
         md_table(['Item', 'Questions', 'Decision', 'What was done'],
                  [[k, ', '.join(named[k] + [q for q in by_f[k] if q not in named[k]]), resp.C[k][0], resp.C[k][1]]
                   for k in named if k[0] == 'C']), '',
         '## P — package, standards, and branch requirements', '',
         md_table(['Item', 'Status', 'Response and evidence'],
                  [[k, v[0], v[1]] for k, v in resp.P.items()]), '',
         '## Questions the reviewer named that did not change', '']
    unchanged = [q for k in named for q in named[k] if q not in {x['id'] for x in rows}]
    L += [('- ' + ', '.join(unchanged)) if unchanged else '- None: every named question was revised.', '',
          '## Return items requested by the reviewer', '',
          md_table(['#', 'Item', 'Where'], [
              [1, 'Revised complete package and matching standalone files', 'nexus/' + ZIP_NAME + '; PDFs, JSON, CSV in this folder'],
              [2, 'Response table for every R finding and P requirement', 'this file'],
              [3, 'Decision for every C recommendation', 'this file, section C'],
              [4, 'Claim-level source ledger', 'SOURCE_LEDGER.md / SOURCE_LEDGER.json'],
              [5, 'Importer, math-branch routing, rendering, remediation return, mastery, Go Deeper, reward checks',
               'RUNTIME_CHECK.json, MATH_REF_VALIDATION.json, MATH_BRANCHES.md section 1']]), '']
    write('REVIEW_RESPONSE.md', '\n'.join(L))
    return rows
