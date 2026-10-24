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
VERSION = '1.1.0'
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
EXTRA_GRADING_RULES = [
    'Algebra II answer forms: the grading_note of every written answer begins with "Form required:" or with "Any" '
    '(for example "Any equivalent form"), which says what else is accepted. "Exact" means an exact '
    'value (fractions, radicals, logarithms, π, i); a decimal approximation alone is not full credit. When rounding is '
    'allowed the note names the precision; an answer within half a unit of the last required place is correct.',
    'Solutions: a question says whether solutions are real or may be complex. A solution set must contain every solution '
    '(with multiplicity when the question asks for it); an extraneous value listed as a solution is an error. "No real '
    'solution" is an answer when the key says so. Complex numbers are written a + bi with real a and b unless a form is named.',
    'Domains: logarithms are real only for positive arguments and bases b > 0, b ≠ 1; √(x²) = |x| over the reals; a rational '
    'expression keeps the exclusions of its original denominator after cancelling. Trigonometric questions state degrees or '
    'radians and an interval, and "all solutions" means every solution in that interval.',
    'Proofs, derivations and explanations are multiple choice (no question needs a person to grade): the keyed choice is a '
    'complete, valid argument; each other choice is a flawed one (checking a few values, an invalid algebra step, assuming the '
    'result, a false fact, or the wrong direction or reflection), and grading_note says what is wrong with each.',
    'Graphs are multiple choice (no question needs a drawing surface): the figure shows four candidate graphs labeled A to D '
    'on the same window, with asymptotes and midlines dashed and holes as open circles, and the choices are "Graph A" to '
    '"Graph D". grading_note lists the features of the correct graph and what each other graph shows.',
    'Technology: a question that needs a calculator says so and names the capability (logarithms, normal cumulative '
    'probability, trigonometric values in radians or degrees). Simulation questions supply the simulated results; any '
    'answer that reads them correctly within the stated tolerance is accepted.',
    'Every question has an explanation in its grading_note after the form rule; for numeric questions it shows the '
    'verified exact value and the work.',
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

Question types used: `sa`, `mc`, and `tf` only. No question needs a person or a drawing surface to grade: since version 1.1.0
the former shown-work items (proofs, derivations, explanations, divisions) and drawing items are multiple choice. A graphing
question shows four candidate graphs labeled A to D in one figure (`figure` in the set file, described in
`figure.description`) and its choices are "Graph A" to "Graph D". The game importer's `--check` mode was run on this package
(see the collection README for the result). Nothing here has been tested in the live game or with the AI grader.
'''
