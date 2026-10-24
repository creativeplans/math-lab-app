"""Probability & Statistics configuration: a course collection (no grade is assigned; students take it in Grade 10, 11,
12, or later).

MAIN questions use the Probability & Statistics course profile in engine/hs_courses.py:
  - CORE strand: every High School Statistics & Probability (HSS) standard that is not marked (+).
  - ADVANCED EXTENSION strand: every HSS standard officially marked (+): S-CP.B.8, S-CP.B.9 and all of S-MD.
Backward branches use Grade K-8 standards, Algebra I or Geometry standards, or the MAIN standard of an EARLIER set of this
course. Forward branches stay in the course (a same-standard branch must add a new demand) or go to a later course.
The rules are checked by engine/qb.py (profile mode, shared with Geometry and Algebra II).

Every question is graded automatically by the game (question-bank/AUTO_GRADING_RULES.md): multiple choice, true/false,
or a short answer that the game's answer checker accepts.
"""
COURSE = dict(id='PS', name='Probability & Statistics', file='Probability_Statistics', seed=104, rules='profile')
VERSION = '1.1.0'
VERSION_DATE = '2026-10-24'
BALANCE_MC = True
STRICT_BACKWARD = True
DOMAINS = [
    ('Interpreting Categorical and Quantitative Data', 'data_id'),
    ('Making Inferences and Justifying Conclusions', 'data_ic'),
    ('Conditional Probability and the Rules of Probability', 'data_cp'),
    ('Using Probability to Make Decisions (+)', 'data_md'),
]
BASE_GRADING_RULES = [
    'Match each student response to its key record by the question ID printed on the question page '
    '(for example S12-B2-Q3). The page number is the same in the Question Collection and the Answer Key. '
    'IDs are unique within one collection; across collections use uid (for example PS:S12-B2-Q3).',
    'Every question is graded automatically; no question needs a person, a drawing surface, or a judgment of wording. '
    'Question types are mc, tf and sa only. There is no partial credit: a response is correct or not.',
    'Multiple choice and true/false: the response is correct when the chosen letter equals correct_letter.',
    'Short answer: the response is checked against correct_answer by the game\'s answer checker. Mathematically '
    'equivalent numbers (fractions, decimals, percents where the question asks for a percent, "x = 5" or "5") are accepted '
    'unless the question names a form. When an answer has several parts (one per answer line), every part must be correct. '
    'A list of values may be given in any order unless the question says "in that order".',
    'A word answer is used only when the question lists the allowed words (for example "Answer Yes or No"); the response '
    'must be one of those words.',
    'grading_note gives the accepted form, the work behind the answer and, for multiple choice, what is wrong with each '
    'other choice. It is guidance for teachers, not for students.',
]
EXTRA_GRADING_RULES = [
    'Precision: a question that asks for rounding names the precision ("to the nearest hundredth", "as a percent to one '
    'decimal place"), and the answer must be given to exactly that precision. A probability may be given as a fraction or a '
    'decimal unless the question names one form; a fraction need not be in lowest terms unless the question says so.',
    'Conventions stated on the page: quartiles are the medians of the lower and upper halves (the median left out of both '
    'halves when n is odd); an outlier lies more than 1.5·IQR beyond a quartile; each question says whether a standard '
    'deviation is the population (divide by n) or sample (divide by n - 1) value; histogram bins include their left '
    'endpoint and exclude their right endpoint unless stated otherwise; residual = observed - predicted.',
    'Probability models: every question states the sample space or the process (fair, equally likely, with or without '
    'replacement, order matters or not, independent trials), and "or" is inclusive unless stated otherwise.',
    'Simulation: a question that asks students to carry out a simulation supplies the random digits and the rule for using '
    'them, so every correct procedure gives the same result. A question about a simulation run by someone else supplies its '
    'results. Every inference states the null model, the outcomes counted (one or two tails) and the cutoff; a rare result '
    'is evidence against a model, not proof, and a common result is consistent with the model, not proof that it is true.',
    'Skills that ask students to construct a display, design a study or explain a conclusion are assessed by what the game '
    'can check: the numbers that define the display (counts, quartiles, residuals), a choice among candidate plots, designs '
    'or arguments whose other choices are specific errors, or the conclusion that follows from supplied evidence. '
    'COVERAGE.md records which subskills are assessed by recognition.',
    'Technology: a question that needs a calculator or spreadsheet says so and names the capability (mean and standard '
    'deviation, least-squares line, correlation, normal area). A normal table is printed on the page when a question uses one.',
    'Every question has an explanation in its grading_note; for numeric questions it shows the work and the exact value.',
]

RELATIONS = dict(
    main='the Probability & Statistics skill the set is built around (strand: core, or advanced extension (+))',
    backward='a prerequisite obstacle to check when a student misses MAIN questions: a Grade K-8, Algebra I or Geometry '
             'standard, or the MAIN standard of an earlier set of this course; branch.alignment is exact or supporting',
    forward1='the next demand after MAIN; branch.progression is same-course deepening, cross-standard extension, or '
             'later-course extension, and branch.new_demand states what it adds',
    forward2='a further demand; branch.builds_on says how it builds on FORWARD 1 (or why it is a separate extension of MAIN)',
    nearest_related='true marks a forward branch that no standard directly continues; it uses the nearest related standard')

PACKAGE_README_EXTRA = '''
## Probability & Statistics additions

| Path or field | Contents |
|---|---|
| `BRANCH_MAP.json` | Every set's MAIN target skill, the subskills it covers, and each branch's teacher metadata (also in each set file as `sections[].branch`). |
| `COVERAGE.md` | The course profile, every standard and subskill with its MAIN sets and assessed response, and each set's branches. |
| `DATASETS.md` | Every dataset used, with its values, sample size, units and provenance (all synthetic, written for this collection). |
| `VALIDATION.md` | The automatic checks run on this release, each with its scope, and the manual reviews. |
| `CHANGELOG.md` | Changes by question ID. |
| set file `strand`, `target_skill`, `covers` | `core` (every HSS standard not marked (+)) or `advanced` (every HSS standard marked (+)); the one skill MAIN measures; subskill IDs. |
| question `course_level` | Course placement label, for example "High School — Probability & Statistics", "High School — Probability & Statistics, Advanced Extension (+)", or a K-8 grade-level standard's own grade for a prerequisite. This is the bank's course placement, not an official Common Core grade assignment. |

Question types used: `sa`, `mc`, and `tf` only. Every question is graded automatically: every short-answer key was run
through the game's answer checker (see VALIDATION.md), and explanations, study designs and plot choices are multiple
choice. Nothing here has been tested in the live game or with the AI grader.
'''
