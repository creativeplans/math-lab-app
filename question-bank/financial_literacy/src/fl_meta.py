"""Collection-wide metadata for Financial Literacy: version, branching rules, standards references."""
VERSION = '1.0.0'
DATE = '2026-10-12'

SOURCE_STATUS = ('Not re-verified online: the authoring environment could not open this site on 2026-10-12. '
                 'A reviewer must confirm the claim against the source before import.')

# 2021 National Standards for Personal Financial Education (Council for Economic Education and Jump$tart Coalition).
# Six topics; learning outcomes are coded by grade band and number (12-1a, ...). Only the 12th-grade codes listed in
# VERIFIED_NATIONAL were confirmed from search-indexed text of the official document; the others are left to verify.
NATIONAL_TOPICS = ['Earning Income', 'Spending', 'Saving', 'Investing', 'Managing Credit', 'Managing Risk']
VERIFIED_NATIONAL = {
    '12-1a': 'Earning Income: research potential income and employee benefit packages likely to be offered to new employees by various companies, government agencies, or not-for-profit organizations',
    '12-5a': 'Earning Income: how labor market conditions affect income',
    '12-5b': 'Earning Income: how technology affects employment and income',
    '12-6a': 'Earning Income: calculate the taxes likely to be withheld from pay',
    '12-8a': 'Earning Income: distinguish earned from unearned income',
    '12-8b': 'Earning Income: compare tax rates on earned income, interest, and capital gains',
    '12-11a': 'Earning Income: benefits and costs of gig employment',
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
    codes = [c for c in VERIFIED_NATIONAL if c in target]
    return dict(
        national=dict(document='2021 National Standards for Personal Financial Education (CEE and Jump$tart)', topic=topic,
                      learning_target=target, grade_band='9-12',
                      outcome_codes=codes, outcome_code_status='verified' if codes else 'to verify against the official document'),
        new_jersey=dict(document='NJSLS-CLKS 2020, Standard 9.1 Personal Financial Literacy (grade 12)',
                        strands=['9.1.12.%s (%s)' % (c, NJ_STRANDS[c]) for c in s['nj']],
                        performance_expectation_status='strand-level alignment; individual 9.1.12 performance expectations to verify'),
        alignment='supporting' if s['unit']['code'] not in ('LIFE',) else 'integrating',
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

STANDARDS_NOTE = ('Alignment: 2021 National Standards for Personal Financial Education (topic level; 12th-grade outcome codes '
                  'only where verified) and NJSLS-CLKS 2020 Standard 9.1 (grade-12 strand level). See COVERAGE.md.')
