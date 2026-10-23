"""Geometry configuration: a course collection (no grade is assigned; students take Geometry in Grade 8, 9, 10, or later).

MAIN questions use the standards of the Common Core traditional-pathway Geometry course (engine/hs_courses.py GEOMETRY).
The HSG standards marked (+) form a separate ADVANCED EXTENSION strand (strand='advanced'): enrichment, not core mastery.
Backward branches use Grade K-8 standards, Algebra I standards, or the MAIN standard of an EARLIER Geometry set.
Forward branches may stay in Geometry (the same standard is allowed when the demand advances) or use a later course.
Rules are checked by engine/qb.py (_check_geometry_set).
"""
COURSE = dict(id='GEO', name='Geometry', file='Geometry', seed=102, rules='geometry')
VERSION = '1.0.0'
VERSION_DATE = '2026-10-23'
BALANCE_MC = True
STRICT_BACKWARD = True
DOMAINS = [
    ('Congruence: Definitions and Transformations', 'data_co_a'),
    ('Congruence: Rigid Motions and Triangle Congruence', 'data_co_b'),
    ('Congruence: Proving Theorems', 'data_co_c'),
    ('Congruence: Constructions', 'data_co_d'),
    ('Similarity, Right Triangles, and Trigonometry', 'data_srt'),
    ('Circles', 'data_c'),
    ('Expressing Geometric Properties with Equations', 'data_gpe'),
    ('Geometric Measurement and Dimension', 'data_gmd'),
    ('Modeling with Geometry', 'data_mg'),
    ('Advanced Extension (+)', 'data_adv'),
]
EXTRA_GRADING_RULES = [
    'Geometry answer forms: the grading_note of every written answer begins with "Form required:" or with "Any" '
    '(for example "Any equivalent form" or "Any valid proof"), which says what else is accepted. "Exact" means an exact '
    'value (radicals, π, fractions); a decimal approximation alone is not full credit. When rounding is allowed the note '
    'names the precision; an answer within half a unit of the last required place is correct. Units are required only '
    'when the question asks for them or the note says so.',
    'Proofs and explanations (type work, and written answers that ask why): grade the logic, not the wording or the format. '
    'A paragraph, two-column, flow, or diagram-based argument is accepted unless the question names a format. '
    'grading_note lists the ESSENTIAL steps (every one must appear, with a valid reason), accepted alternative approaches, '
    'and common INVALID arguments (each earns no credit for that step): reasoning from how the diagram looks, measuring a '
    'drawing as proof of a general theorem, assuming what is to be proved (circular reasoning), or citing a theorem that '
    'depends on the result being proved.',
    'Constructions (type plot): the construction must show its evidence: compass arcs and straightedge lines (or the folds, '
    'string marks, or software steps the question allows). A figure that only looks right, with no construction marks, is '
    'not full credit. Drawing tolerance: points within about 2 mm and angles within about 2° of the exact construction.',
    'Drawings and graphs: correct_answer (or drawing_answer) states the geometric relationships a correct drawing must show '
    '(image vertices, lines, marks). Accept any drawing with those relationships; exact pencil position is not graded.',
    'Every question has an explanation in its grading_note after the form rule; for numeric questions it shows the '
    'verified exact value and the work.',
]
