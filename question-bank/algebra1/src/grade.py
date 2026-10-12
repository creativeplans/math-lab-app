"""Algebra I configuration: a course collection (no grade is assigned; students take Algebra I in Grade 7, 8, 9, or later).

MAIN questions use the standards of the Common Core traditional-pathway Algebra I course (engine/hs_courses.py).
Backward branches use Grade K-8 standards or an Algebra I standard that is the MAIN standard of an earlier set.
Forward branches use standards of later courses (Geometry, Algebra II, Probability & Statistics, Precalculus).
"""
COURSE = dict(id='ALG1', name='Algebra I', file='Algebra1', seed=101)
VERSION = '1.0.0'
VERSION_DATE = "2026-10-11"
# Deal the correct letter of four-choice questions evenly across A-D.
BALANCE_MC = True
STRICT_BACKWARD = True
DOMAINS = [
    ('Number & Quantity', 'data_nq'),
    ('Seeing Structure in Expressions & Arithmetic with Polynomials', 'data_sse'),
    ('Creating Equations & Reasoning with Equations and Inequalities', 'data_eq'),
    ('Interpreting Functions', 'data_if'),
    ('Building Functions & Linear, Quadratic, and Exponential Models', 'data_bf'),
    ('Interpreting Categorical & Quantitative Data', 'data_id'),
]
EXTRA_GRADING_RULES = [
    'Algebra I answer forms: the grading_note of every written answer begins with "Form required:" or with "Any" '
    '(for example "Any equivalent form", "Any equivalent wording", or "Any correct graph"), which says what else is accepted. '
    'When a form is required (for example expanded, factored completely, simplest radical form, slope-intercept form, '
    'vertex form, exact value, or a stated rounding), an answer in another form is not full credit even if it is equivalent.',
    'Equations, inequalities, and systems: "x = 3" and "3" are the same answer; a solution set must contain every solution '
    '(both roots of a quadratic, in any order); "no solution" and "all real numbers" are answers when the key says so; an '
    'inequality may be written either way round (x > 2 or 2 < x) unless a notation is asked for; a solution of a system may '
    'be written as an ordered pair or as x = ..., y = ....',
    'Every question has an explanation in its grading_note, after the form rule. It shows why the key is correct and can be '
    'shown to the student as feedback after grading.',
]
