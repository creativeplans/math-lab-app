"""Manual review record for Geometry 1.1.0, printed into VALIDATION.md by validate.py.

Everything here was done by reading, drawing, or computing by the author of this release. It is NOT an automatic check,
and no second person has reviewed it. The lists say exactly which questions each review covered, so a reader can see what
was and was not looked at.
"""

# Proof-dependency review (correction report R05). Each row: the theorem set, what its MAIN proofs and rubrics may cite.
# The author re-read every MAIN proof and rubric in these sets and confirmed that it cites only the listed results.
DEPENDENCIES = [
    ('S13 CO.B.7', 'definitions of rigid motions and congruence', 'triangle congruence ⇔ corresponding parts congruent'),
    ('S14 CO.B.8 SAS', 'rigid motions (reflection, rotation, translation), S13', 'SAS'),
    ('S15 CO.B.8 ASA', 'rigid motions, S13', 'ASA (AAS follows in its FORWARD 1)'),
    ('S16 CO.B.8 SSS', 'SAS (S14) and the angle bisector of the apex of an isosceles triangle formed by the two copies; '
                       'NOT the perpendicular-bisector converse (S19) and NOT SSS itself', 'SSS'),
    ('S17 CO.C.9 vertical angles', 'linear pairs (supplementary), algebra', 'vertical angles are congruent'),
    ('S18 CO.C.9 parallel lines', 'translation along the transversal (rigid motion) for corresponding angles first; '
                                  'then vertical angles (S17) and linear pairs for the other pairs', 'angle-pair theorems'),
    ('S19 CO.C.9 perpendicular bisector', 'SAS (S14) for the theorem; SAS with the angle bisector, or SSS (S16), for the converse; '
                                          'S16 does not use S19, so there is no cycle', 'perpendicular bisector theorem and converse'),
    ('S20 CO.C.10 angle sum', 'a parallel through a vertex (S18 alternate interior angles)', 'triangle angle sum, exterior angle'),
    ('S21 CO.C.10 isosceles', 'SAS (S14) or a reflection', 'base angles congruent'),
    ('S24 / S101 CO.C.11 parallelograms', 'ASA / SAS (S14, S15) with alternate interior angles (S18)', 'opposite sides; opposite angles'),
    ('S41 SRT.A.3 AA', 'dilations preserve angles (S37, S38) and ASA (S15)', 'AA similarity'),
    ('S42 / S43 SRT.B.4 proportionality', 'AA (S41), SAS similarity, corresponding angles (S18)', 'theorem and converse'),
    ('S44 SRT.B.4 Pythagorean Theorem', 'AA (S41) only; the distance formula is excluded in the rubric (it depends on the theorem)',
     'a² + b² = c²'),
    ('S54 C.A.2 inscribed angle', 'isosceles base angles (S21) and the exterior angle (S20)', 'inscribed angle = ½ intercepted arc'),
    ('S56 C.A.2 tangent', 'the perpendicular is the shortest segment (hypotenuse longest, S44)', 'radius ⊥ tangent'),
    ('S61 C.A.3 cyclic quadrilateral', 'inscribed angle theorem (S54)', 'opposite angles supplementary'),
    ('S64 GPE.A.1 circle equation', 'Pythagorean Theorem (S44)', '(x - h)² + (y - k)² = r²'),
    ('S69 GPE.B.5 slope criteria', 'a 90° rotation (CO.A) and the converse of the Pythagorean Theorem; not the slope criteria themselves',
     'parallel ⇔ equal slopes; perpendicular ⇔ product -1'),
    ('S88-S90 SRT.D.9-10', 'right-triangle trigonometry (S48-S50), the Pythagorean Theorem (S44), sin(180° - x) = sin x stated as a '
                           'fact for the obtuse case', 'area formula; Laws of Sines and Cosines'),
]

# Questions added or rewritten in 1.1.0 whose numeric or exact answers the author recomputed with a separate calculator
# script while writing them (in addition to the automatic re-solve list).
HAND_SOLVED = (
    'S37-M-Q1..Q5, S38-M-Q4/Q5, S39-M-Q4/Q5, S40-M-Q4/Q5, S41-M-Q2, S42-M-Q4, S43-M-Q5, S44-M-Q2..Q5, S45-M-Q4/Q5, S48-M-Q4/Q5, '
    'S49-M-Q5, S50-B2-Q2, S50-F2-Q1/Q2/Q4/Q5, S53-M-Q3, S54-M-Q5, S55-M-Q4/Q5, S56-M-Q4/Q5, S57-M-Q4/Q5, S58-M-Q5, S61-M-Q3, '
    'S63-M-Q2..Q5, S64-M-Q2..Q5, S65-M-Q1/Q2/Q4/Q5, S66-M-Q2..Q5, S67-M-Q4/Q5, S68-M-Q1..Q3/Q5, S69-M-Q5, S73-F1-Q4/Q5, '
    'S75-M-Q1/Q3/Q5, S75-F1-Q1..Q5, S75-F2-Q1/Q4, S77-M-Q4/Q5, S77-F2-Q2/Q5, S80-F1-Q1/Q2, S80-F2-Q2, S83-F2-Q1, S84-F2-Q2, '
    'S87-M-Q4/Q5, S87-F1-Q2, S87-F2-Q2, S88-M-Q5, S90-M-Q3, S94-M-Q2..Q5, S95-M-Q2..Q5, S96-M-Q2, S96-F2-Q2, S103-M-Q4/Q5, '
    'S104-M-Q4, S104-F1-Q1/Q2/Q4, S104-F2-Q1/Q5, S105-M-Q4/Q5, S105-F1-Q4/Q5, S105-F2-Q1/Q2'
)

# Proofs written or rewritten in 1.1.0 that the author checked step by step against the rubric (validity, givens used,
# no circular step). Listed by set; MAIN items unless stated.
PROOFS_READ = (
    'S13-S27 (all MAIN proofs), S41-S47, S53, S54 (MAIN and F1 inscribed-angle cases), S58, S61, S63-S69, S76, S77 (Q1 general '
    'argument), S88-S90 (acute and obtuse cases), S94-S96, S103, S104'
)

# Figures rendered and inspected by eye in this release.
FIGURES = (
    'All 25 coordinate figures whose point list is empty (the R08 case): S28-F1-Q1, S32-M-Q5, S34-M-Q5, S35-M-Q4, S36-M-Q5, '
    'S76-M-Q1, S77-M-Q1, S78-M-Q1..Q4, S79-M-Q1/Q3, S81-M-Q1/Q2, S82-M-Q1..Q4, S86-M-Q1, S96-M-Q1/Q2, S103-M-Q1, S104-M-Q1, '
    'S105-M-Q1, each re-rendered with the fixed crop and checked for clipped segments, labels, and axes. New or changed '
    'figures: S39-M-Q4/Q5 (grids), S59-M-Q4/Q5 and S60-M-Q2/Q4/Q5 (triangles; S60-M-Q2 was acute although described as obtuse, '
    'now fixed), S93-M-Q3..Q5 (circles with external points).'
)


def markdown(cases, recs):
    ids = [c[0] for c in cases]
    L = ['## Proof-dependency review (manual)', '',
         'The automatic check 6 shows only that branch routing has no cycles. Whether a proof uses a result that is itself '
         'proved later (a logical cycle) cannot be checked by a script. The author re-read the MAIN proofs and rubrics of the '
         'sets below and confirmed that each cites only the listed results. This is the author\'s own review, not an '
         'independent one.', '',
         '| Set | May cite | Establishes |', '|---|---|---|']
    L += ['| %s | %s | %s |' % row for row in DEPENDENCIES]
    L += ['', '## Independently solved questions', '',
          '- **Automatic (check 17), %d questions:** %s.' % (len(ids), ', '.join(ids)),
          '- **Recomputed by the author while writing 1.1.0 (separate calculator script, not resolve.py):** ' + HAND_SOLVED + '.',
          '- **Proofs checked step by step against their rubrics:** ' + PROOFS_READ + '.',
          '- **Not independently solved:** every other question. They were written with their keys and read once by the '
          'author; %d of %d questions are covered by the automatic re-solve.' % (len(ids), len(recs)), '',
          '## Figures inspected (manual)', '', FIGURES, '']
    return L
