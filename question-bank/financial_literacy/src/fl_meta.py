"""Collection-wide metadata for Financial Literacy: version, branching rules, standards references."""
VERSION = '1.1.0'
DATE = '2026-10-15'

SOURCE_STATUS = ('Not re-verified online: the authoring environment could not open this site on 2026-10-12. '
                 'A reviewer must confirm the claim against the source before import.')

# 2021 National Standards for Personal Financial Education (Council for Economic Education and Jump$tart Coalition).
# Six topics; learning outcomes are coded by grade and number (12-1a, ...). Codes repeat across topics, so every code
# is qualified by its topic. Status says how each code and wording was checked; the official PDF could not be opened
# from the authoring environment (blocked network), so nothing here is marked as checked against it by the author.
NATIONAL_TOPICS = ['Earning Income', 'Spending', 'Saving', 'Investing', 'Managing Credit', 'Managing Risk']
SEARCH = 'wording from search-indexed text of the official document; not re-checked against the PDF by the author'
REVIEWER = 'code assigned by the independent reviewer from the official PDF (A20); wording paraphrased, not re-checked by the author'
NATIONAL_CODES = {
    ('Earning Income', '12-1a'): ('research potential income and employee benefit packages likely to be offered to new employees by various companies, government agencies, or not-for-profit organizations', SEARCH),
    ('Earning Income', '12-5a'): ('how labor market conditions affect income', SEARCH),
    ('Earning Income', '12-5b'): ('how technology affects employment and income', SEARCH),
    ('Earning Income', '12-6a'): ('calculate the taxes likely to be withheld from pay', SEARCH),
    ('Earning Income', '12-6b'): ('types of taxes (paraphrase)', REVIEWER),
    ('Earning Income', '12-6c'): ('purposes of taxes and how government uses them (paraphrase)', REVIEWER),
    ('Earning Income', '12-8a'): ('distinguish earned from unearned income', SEARCH),
    ('Earning Income', '12-11a'): ('benefits and costs of gig employment', SEARCH),
    ('Investing', '12-8b'): ('tax-deferred versus taxable investing (paraphrase)', REVIEWER),
}

# New Jersey Student Learning Standards — Career Readiness, Life Literacies, and Key Skills (adopted June 3, 2020),
# Standard 9.1 Personal Financial Literacy, grade-12 performance expectations (9.1.12.<strand>.<n>).
NJ_STRANDS = {
    'CFR': 'Civic Financial Responsibility',
    'CDM': 'Credit and Debt Management',
    'CP': 'Credit Profile',
    'EG': 'Economic and Government Influences',
    'FI': 'Financial Institutions',
    'FP': 'Financial Psychology',
    'PB': 'Planning and Budgeting',
    'RM': 'Risk Management and Insurance',
}


def alignment(s):
    topic, target = s['nat']
    assert topic in NATIONAL_TOPICS, (s['num'], topic)
    for c in s['nj']:
        assert c in NJ_STRANDS, (s['num'], c)
    import re as _re
    codes = [c for c in _re.findall(r'\b12-\d+[a-z]\b', target)]
    for c in codes:
        assert (topic, c) in NATIONAL_CODES, (s['num'], topic, c)
    return dict(
        national=dict(document='2021 National Standards for Personal Financial Education (CEE and Jump$tart)', topic=topic,
                      learning_target=target, grade_band='9-12',
                      outcome_codes=['%s %s' % (topic, c) for c in codes],
                      outcome_code_status=[NATIONAL_CODES[(topic, c)][1] for c in codes] or
                      'topic-level only; no 12th-grade outcome code assigned yet'),
        new_jersey=dict(document='NJSLS-CLKS 2020, Standard 9.1 Personal Financial Literacy (grade 12)',
                        strands=['9.1.12.%s (%s)' % (c, NJ_STRANDS[c]) for c in s['nj']],
                        performance_expectation_status='strand-level alignment; individual 9.1.12 performance expectations to verify'),
        local_identifier='FL.%s.%02d is a course identifier, not an official national or New Jersey code' % (s['unit']['code'], s['num']),
        claim='Alignment shows what the set teaches toward; it does not claim full mastery of any standard.',
    )


BRANCHING = dict(
    main_attempt='5 questions',
    backward_trigger='3 or fewer correct out of 5 (the game\'s Financial Literacy setting backwardWhenIncorrectAtLeast: 2). '
                     'This package does not change the threshold; it is enforced by the game.',
    on_trigger='The student works every backward section of the set in package order (B1, B2, ...), each passed with '
               '5 correct in a row (existing rule), then returns to a fresh MAIN attempt.',
    four_correct='a fresh set of the same skill (existing rule)',
    five_correct='mastered; Go Deeper sections unlock (forward chain F1 -> F2 -> ...)',
    backward_kinds={'concept': 'the course\'s own five questions on a simpler money idea',
                    'math': 'a link to an existing math MAIN skill in the game (no questions in this package)'},
    forward_label='Go Deeper',
)

GRADING_RULES = ['Every question is multiple choice with four choices, A-D, and exactly one correct letter.',
                 'The game may shuffle the choices; feedback and misconception notes never refer to a letter.',
                 'intro is shown above the question on the same screen before answering; feedback only after answering.',
                 'Questions without intro are knowledge checks of ideas taught earlier.']

STANDARDS_NOTE = ('Alignment: 2021 National Standards for Personal Financial Education (topic level; 12th-grade outcome codes, '
                  'qualified by topic, only where assigned) and NJSLS-CLKS 2020 Standard 9.1 (grade-12 strand level, with known '
                  'gaps listed in COVERAGE.md). Codes such as FL.SAVE.24 are local course identifiers, not official codes. '
                  'Section roles: MAIN = direct alignment; backward = supporting prerequisite; Go Deeper = related enrichment. '
                  'The package does not claim full mastery of either standard.')

SECTION_ROLE = {'main': 'direct', 'backward': 'supporting prerequisite', 'forward': 'related enrichment'}

# NJSLS 9.1.12 areas with no or incomplete coverage in this course (disclosed, not hidden). From the independent
# review of the official PDF (A21); the author could not open that PDF.
NJ_GAPS = [
    ('9.1.12.CFR.5', 'Estate-planning documents (wills, powers of attorney, beneficiaries)', 'not covered'),
    ('9.1.12.CFR.3', 'Corporate governance, social responsibility, and human rights in financial decisions', 'not covered'),
    ('9.1.12.CFR.4 / FP.6', 'Cross-cultural and family financial patterns', 'not covered'),
    ('9.1.12.FP.4', 'Money scripts and personal beliefs about money', 'partial: behavioral biases in S20 and S55 only'),
    ('9.1.12.EG.3', 'How government policy influences the economy and personal finance', 'partial: S102-S104 cover inflation, Fed rates, and economic conditions'),
    ('9.1.12.RM.4', 'Government versus private insurance', 'partial: S89 touches Social Security disability; no full comparison'),
    ('9.1.12.CDM.8', 'Create an amortization table with business tools (spreadsheet)', 'partial: students read and calculate rows (S31, S80) but do not build a table'),
]
