"""Algebra II configuration: a course collection (no grade is assigned; students take Algebra II in Grade 9, 10, 11, or later).

MAIN questions use the Algebra II course profile in engine/hs_courses.py:
  - CORE strand: every standard of the Common Core traditional-pathway Algebra II course (CCSS Appendix A), including the
    (+) standards that the pathway lists and the codes it shares with Algebra I (revisited with new function families).
  - ADVANCED EXTENSION strand: a small, stated set of further (+) standards (enrichment, not core mastery).
Backward branches use Grade K-8 standards, Algebra I or Geometry standards, or the MAIN standard of an EARLIER Algebra II set.
Forward branches stay in Algebra II (a same-standard branch must add a new demand) or go to a later course.
The rules are checked by engine/qb.py (profile mode, shared with Geometry).
"""
COURSE = dict(id='A2', name='Algebra II', file='Algebra2', seed=103, rules='profile')
VERSION = '1.2.0'
VERSION_DATE = '2026-10-24'
BALANCE_MC = True
STRICT_BACKWARD = True
DOMAINS = [
    ('The Complex Number System', 'data_cn'),
    ('Seeing Structure in Expressions', 'data_sse'),
    ('Arithmetic with Polynomials and Rational Expressions', 'data_apr'),
    ('Creating Equations and Reasoning with Equations', 'data_eq'),
    ('Trigonometric Functions', 'data_tf'),
    ('Interpreting Functions', 'data_if'),
    ('Building Functions and Exponential and Logarithmic Models', 'data_bf'),
    ('Statistics, Inference, and Decisions', 'data_stat'),
    ('Advanced Extension (+)', 'data_adv'),
]
# Algebra II replaces the engine's base rules: since 1.2.0 every question is checked automatically by the game, so the
# engine's rules for drawings, shown work, partial credit and free-form explanations do not apply to this collection.
BASE_GRADING_RULES = [
    'Match each student response to its key record by the question ID printed on the question page '
    '(for example S40-F2-Q3). The page number is the same in the Question Collection and the Answer Key. '
    'IDs are unique within one collection; across collections use uid (for example A2:S40-F2-Q3).',
    'Every question is graded automatically; no question needs a person, a drawing surface, or a judgment of wording. '
    'Question types are mc, tf and sa only. There is no partial credit: a response is correct or not.',
    'Multiple choice and true/false: the response is correct when the chosen letter equals correct_letter.',
    'Short answer: the response is checked against correct_answer by the game\'s answer checker. Mathematically '
    'equivalent numbers (fractions, decimals, "x = 5" or "5") and equivalent polynomial or rational expressions are '
    'accepted unless the question names a form. When an answer has several parts (one per answer line), every part '
    'must be correct. A list of values (solutions, excluded values) may be given in any order unless the question says '
    '"in that order".',
    'A word answer is used only when the question lists the allowed words (for example "Answer Yes or No", '
    '"Answer Positive or Negative", "enter none if there are none"); the response must be one of those words.',
    'grading_note gives the accepted form, the work behind the answer and, for multiple choice, what is wrong with each '
    'other choice. It is guidance for teachers, not for students.',
]
EXTRA_GRADING_RULES = [
    'Algebra II answer forms: the grading_note of every written answer begins with "Form required:" or with "Any" '
    '(for example "Any equivalent form"), which says what else is accepted. "Exact" means an exact value (fractions, '
    'radicals, π, i); a decimal approximation of an exact answer is not accepted. When a question asks for rounding it '
    'names the precision (for example "to the nearest hundredth"), and the answer must be given to exactly that '
    'precision. Answers whose accepted forms the checker cannot compare reliably (radical, logarithmic, trigonometric or '
    'inverse-function formulas, interval statements, interpretations) are multiple choice.',
    'Solutions: a question says whether solutions are real or may be complex. A solution set must contain every solution '
    '(with multiplicity when the question asks for it) and no extraneous value. Complex numbers are written a + bi with '
    'real a and b unless a form is named.',
    'Domains: logarithms are real only for positive arguments and bases b > 0, b ≠ 1; √(x²) = |x| over the reals; a rational '
    'expression keeps the exclusions of its original denominator after cancelling. Trigonometric questions state degrees or '
    'radians and an interval, and "all solutions" means every solution in that interval.',
    'Proofs, derivations and explanations are multiple choice: the keyed choice is a complete, valid argument; each other '
    'choice is a flawed one (checking a few values, an invalid algebra step, assuming the result, a false fact, or the '
    'wrong direction or reflection), and grading_note says what is wrong with each.',
    'Graphs are multiple choice: the figure shows four candidate graphs labeled A to D on the same window, with asymptotes '
    'and midlines dashed, holes and excluded endpoints as open circles and included endpoints as closed dots, and the '
    'choices are "Graph A" to "Graph D". grading_note lists the features of the correct graph and what each other graph shows.',
    'Statistics: every question states its own model and conventions: the null model and the tail direction of a '
    'simulation count, the 5% cutoff for "unusual", the margin of error as 2 standard deviations of the simulated statistic '
    '(a 95% range), independence of repeated events, and fair, equally likely devices. A result that is not unusual is '
    'described as consistent with the model, never as proof that the model is true; an unusual result is evidence against '
    'it, not proof.',
    'Technology: a question that needs a calculator says so. Simulation questions supply the simulated results as a '
    'histogram or as counts.',
    'Every question has an explanation in its grading_note; for numeric questions it shows the verified exact value and the work.',
]

RELATIONS = dict(
    main='the Algebra II skill the set is built around (strand: core, or advanced extension (+))',
    backward='a prerequisite obstacle to check when a student misses MAIN questions: a Grade K-8, Algebra I or Geometry '
             'standard, or the MAIN standard of an earlier Algebra II set; branch.alignment is exact or supporting',
    forward1='the next demand after MAIN; branch.progression is same-course deepening, cross-standard extension, or '
             'later-course extension, and branch.new_demand states what it adds',
    forward2='a further demand; branch.builds_on says how it builds on FORWARD 1 (or why it is a separate extension of MAIN)',
    nearest_related='true marks a forward branch that no standard directly continues; it uses the nearest related standard')

PACKAGE_README_EXTRA = '''
## Algebra II additions

| Path or field | Contents |
|---|---|
| `BRANCH_MAP.json` | Every set's MAIN target skill, the subskills it covers, and each branch's teacher metadata (also in each set file as `sections[].branch`). |
| `COVERAGE.md` | The course profile (inclusion and exclusion table), every standard and subskill with its set and MAIN IDs, and each set's branches. |
| `VALIDATION.md` | The automatic checks run on this release, each with its scope, and the manual reviews. |
| `CHANGELOG.md` | Changes by question ID. |
| set file `strand`, `target_skill`, `covers` | `core` (the Appendix A Algebra II pathway) or `advanced` (further (+) standards, optional); the one skill MAIN measures; subskill IDs. |
| question `strand`, `set_target`, `target_skill`, `alignment_type`, `course_level` | Strand (`core` or `advanced extension (+)`); the set's target; the skill this section measures; how the section's standard relates to it; the course-placement label (for example "High School — Algebra II, revisits an Algebra I standard", "High School — Algebra II, Advanced Extension (+)", or a K-8 grade-level standard's own grade for a prerequisite). |
| question `question_page`, `answer_key_page` | Page in each PDF (always equal). |
| `sections[].branch` | Backward: `alignment` (exact or supporting), `rationale` (obstacle, why it matters, evidence collected), `source`. Forward: `progression`, `connection` (direct or nearest related), `new_demand`, `course`, and for FORWARD 2 `builds_on`. Every section: `plus_standard` (true for an official Common Core (+) standard). |

Question types used: `sa`, `mc`, and `tf` only. Every question is graded automatically: since version 1.1.0 the former
shown-work and drawing items are multiple choice, and since version 1.2.0 every short answer has a key that the game's
answer checker accepts (checked against the checker code itself; see VALIDATION.md), and every explanation or
interpretation is multiple choice. A graphing
question shows four candidate graphs labeled A to D in one figure (`figure` in the set file, described in
`figure.description`) and its choices are "Graph A" to "Graph D". The game importer's `--check` mode was run on this package
(see the collection README for the result). Nothing here has been tested in the live game or with the AI grader.
'''
