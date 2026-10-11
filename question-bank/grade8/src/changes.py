"""Grade 8 revision 2.0.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is
    (ID patterns, finding code, status, reason)
status: 'revised' (ID kept), 'retired' (ID removed, never reused), 'new', or 'layout'.
Finding codes are those of Grade8_Complete_Review.md.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'ded5025'

FINDINGS = {
    'C01': 'Only one choice is 5 units from (1, 1): (6, 1) was replaced by (7, 1) (S48-F1-Q3)',
    'C02': 'The maximum statement names a specific function that decreases after its maximum (S31-F1-Q4)',
    'C03': 'The birth-month rule names individual students as outputs and two students who share a month (S23-M-Q5)',
    'C04': 'The slope-triangle item describes a translation followed by a dilation, with the center and scale factor (S15-F1-Q2)',
    'C05': 'The y ÷ x argument excludes the origin (x ≠ 0) and checks it separately (moved to S60-M-Q1)',
    'C06': 'Altitude questions repeat the triangle setup on each page (S44-F1-Q2/Q3)',
    'C07': 'Points are off the mirror line or distinct from the center, translations are nonzero, the rotation angle is defined, and the parallel-slope statement says distinct lines',
    'C08': 'The side-splitter item names D on AB, E on AC, and the parts AD, DB, AE, EC (S39-F2-Q3)',
    'C09': 'The drawing rubric accepts every right triangle with AB as its hypotenuse (S48-M-Q4)',
    'C10': 'Exact-answer rules agree in every format (S51-F1-Q1, S4-F2-Q1, S14-F2-Q1)',
    'C11': 'The ice-cream item asks whether the data show a cause; the key treats weather as a possible explanation (S54-F1-Q1)',
    'C12': 'The proportional-graph statement no longer says a unit rate can only be read at x = 1 (S56-B1-Q5)',
    'C13': 'The two-way table statement says there are exactly two exhaustive rows (S57-M-Q5)',
    'C14': 'The hike gives steady elevation-gain rates (S31-M-Q5)',
    'C15': 'The interior angle is named, and the cone item is a right circular cone volume task (S34-F1-Q2, S50-F2-Q3)',
    'C16': 'Required work is collected and graded: completed square, both-sides table, and table plus graph (S8-F2-Q2, S19-F1-Q2, S19-B1-Q1)',
    'B01': 'Grade 4 rounding stays within 1,000,000 (S9-B2-Q1)',
    'B02': 'The mislabeled S43-B2 branch is retired; S43-B3 (7.G.A.2) asks which three angle measures make a triangle and whether they fix one triangle',
    'V01': 'New set S59: estimate the values of expressions with irrational numbers',
    'V02': 'S15 is slope invariance only; new sets derive y = mx (S60) and y = mx + b (S61)',
    'V03': 'New set S62: write examples with one, no, or infinitely many solutions and transform them',
    'V04': 'S32-S34 MAIN questions compute or measure lengths, angles, and slopes before and after each rigid motion',
    'V05': 'New sets give the informal arguments: triangle angle sum (S63), parallel lines and a transversal (S64), and AA (S65)',
    'F01': 'Forward branches that repeated Grade 8 procedures now add a high-school demand (S2-F1, S16-F1, S18-F1, S21-F1, S28-F1, S29-F1, S30-F1, S40-F1, S43-F2)',
    'F02': 'Accuracy items choose a reporting precision from the measuring tool (S9-F1-Q2/Q3)',
    'F03': 'Modeling items define quantities, meanings, and units (S12-F2-Q2 to Q5)',
    'F04': 'Equation-modeling branches have students graph with labels and scales and include quadratic models (S14-F1, S22-F1)',
    'F05': 'The elimination branch proves both directions of the equivalence (S20-F1)',
    'F06': 'SAS, ASA, and SSS are explained with rigid motions (S35-F2)',
    'F07': 'S45-F1 proves the converse of the Pythagorean theorem with SSS',
    'F08': 'Right-triangle branches use trigonometric ratios with the Pythagorean theorem (S46-F1-Q2/Q3, S47-F1, S48-F1)',
    'F09': 'Design branch makes decisions under constraints (S46-F2)',
    'F10': 'Scatter-plot branches compare models, use technology, and compare residuals (S53-F1, S55-F1)',
    'F11': 'Linear-quadratic systems include a student graph with an algebraic check (S20-F2)',
    'F12': 'The AA explanation includes the dilation and rigid motions that match the third vertex (S43-F1-Q2)',
    'F13': 'Branches without a direct high-school continuation are marked NEAREST RELATED (S3-F2, S11-F2, S33-F2, S36-F2, S38-F2, S41-F2, S47-F2)',
    'R01': 'Answer-key pages no longer use transparency, so no embedded page is missing a graphics resource',
    'D01': 'Version 2.0.0 with this change log, CORRECTIONS.md, and revised README and COVERAGE',
    'P01': 'An original nonlinear example (handshakes) replaces the square-area example (S26-M-Q3)',
    'P02': 'Rigid-motion reasons for corresponding parts, and a derivation of the circle equation (S35-F1-Q1, S44-F2-Q2)',
    'P03': 'Irrationality is explained, rational exponents are justified by the exponent laws, and logarithms solve exponential equations (S1-F1, S6-F1, S9-F2)',
    'P04': 'r is computed with technology, and students plot residuals (S54-F2-Q1, S55-F2-Q2/Q3)',
    'P05': 'Clock times in the theater rubric, a qualified interpolation, a straight-sided container, and fixed dimensions in doubling items',
    'P06': 'Constant-ratio tables in S40-B2, quadratic and exponential comparisons in S13-F2, and scaling in S7-F2',
}

BRANCH_REPLACEMENTS = [('S43-B2', 'S43-B3')]

NEW_SETS = {
    'S59': ('V01', '8.NS.A.2 — estimate the values of expressions that contain irrational numbers.'),
    'S60': ('V02', '8.EE.B.6 — derive y = mx for a line through the origin with similar triangles.'),
    'S61': ('V02', '8.EE.B.6 — derive y = mx + b for a line that crosses the y-axis at b.'),
    'S62': ('V03', '8.EE.C.7.a — give examples of equations with one, no, or infinitely many solutions and transform them.'),
    'S63': ('V05', '8.G.A.5 — informal arguments for the triangle angle sum and the exterior angle.'),
    'S64': ('V05', '8.G.A.5 — informal arguments for angles formed by parallel lines and a transversal.'),
    'S65': ('V05', '8.G.A.5 — informal argument for the angle-angle criterion.'),
}


def _new_sets():
    return [([s + '-*'], code, 'new', 'New focused set: ' + text) for s, (code, text) in NEW_SETS.items()]


CHANGES = _new_sets() + [
    # ---- content and grading
    (['S48-F1-*'], 'C01', 'revised', 'Q3: the choice (6, 1) is now (7, 1), so only (4, 5) is 5 units from (1, 1). The branch also adds trigonometric applications (F08).'),
    (['S48-F1-*'], 'F08', 'revised', 'Distances with angles from tangent values, an angle of elevation, and a 45° check; branch title updated.'),
    (['S31-F1-Q4'], 'C02', 'revised', 'Names f(x) = -(x - 3)² + 5, which has its maximum at x = 3 and decreases for every x > 3; still True.'),
    (['S23-M-Q5'], 'C03', 'revised', 'The output is one student; Ana and Ben share January, so the rule is not a function; still False.'),
    (['S15-F1-Q2'], 'C04', 'revised', 'Gives two slope triangles on one line and asks for a translation followed by a dilation (center (3, 3), scale factor 2).'),
    (['S15-M-*'], 'V02', 'revised', 'S15 now tests only why the slope is the same between any two points (similar slope triangles). The y = mx item, with x ≠ 0 stated (C05), moved to the new set S60; y = mx + b moved to S61. Set title updated.'),
    (['S44-F1-Q2', 'S44-F1-Q3'], 'C06', 'revised', 'Each page states: ABC is right at C, and D is the foot of the altitude from C to hypotenuse AB.'),
    (['S32-F1-Q1', 'S32-F1-Q2', 'S32-F1-Q3', 'S38-F1-Q1', 'S38-F1-Q3', 'S42-F2-Q4'], 'C07', 'revised',
     'States P not on the mirror line, the point distinct from the center, a nonzero translation, the rotation angle θ (0° < θ ≤ 180°), and distinct non-vertical lines.'),
    (['S39-F2-Q3'], 'C08', 'revised', 'Names D on AB and E on AC with DE ∥ BC, AD = 3, DB = 6, AE = 4; EC is still 8.'),
    (['S48-M-Q4'], 'C09', 'revised', 'The rubric accepts any right triangle with hypotenuse AB, for example the right angle at (4, -1), (-2, 7), or (5, 0); AB = 10.'),
    (['S51-F1-Q1'], 'C10', 'revised', 'Asks for the volume in terms of π and accepts only the exact 256π/3; the "about 268" note was removed.'),
    (['S4-F2-Q1'], 'C10', 'revised', 'The note says the exact perimeter 4 + 2√2 is required; a decimal alone is not accepted.'),
    (['S14-F2-Q1'], 'C10', 'revised', 'The key gives the exact g(5) = 759.375 and says exact values are required.'),
    (['S54-F1-Q1'], 'C11', 'revised', 'Asks whether the data show that ice cream causes sunburn; the key says no, and names weather as a possible explanation.'),
    (['S56-B1-Q5'], 'C12', 'revised', 'Now: the point (2, 18) means one ticket costs $18 (False; one ticket costs $9).'),
    (['S57-M-Q5'], 'C13', 'revised', 'States exactly two exhaustive rows, so the row totals must add to 60; still False.'),
    (['S31-M-Q5'], 'C14', 'revised', 'Gives steady rates of 200 and 80 meters per hour and a rest; the axis is elevation gain in hundreds of meters.'),
    (['S34-F1-Q2'], 'C15', 'revised', 'Names the 72° angle as an interior angle and asks for the other interior angle on the same side; still 108°.'),
    (['S50-F2-Q3'], 'C15', 'revised', 'Now a volume task: a right circular cone with radius 6 and slant height 10 has height 8 and volume 96π.'),
    (['S8-F2-Q2'], 'C16', 'revised', 'Answer with required work: the completed square (x + 2)² = 5 and both exact roots.'),
    (['S19-F1-Q2'], 'C16', 'revised', 'Answer with required work: the table of both sides for x = 0 to 3, and x = 2.'),
    (['S19-B1-Q1'], 'C16', 'revised', 'Drawing + written answer: the student writes the table and graphs the points; both are graded.'),
    # ---- backward branches
    (['S9-B2-Q1'], 'B01', 'revised', 'Rounds 412,000 to the nearest hundred thousand (400,000), within the Grade 4 range.'),
    (['S43-B2-*'], 'B02', 'retired', 'The triangle-angle-sum branch was labeled 7.G.B.5, which does not cover the triangle angle sum. It is retired and replaced by S43-B3.'),
    (['S43-B3-*'], 'B02', 'new', 'Replacement branch (7.G.A.2): whether three angle measures can be a triangle\'s angles and whether they fix one triangle.'),
    (['S40-B2-*'], 'P06', 'revised', 'Pairs are judged inside tables for a constant ratio (7.RP.A.2.a); branch title updated.'),
    # ---- MAIN coverage
    (['S32-M-Q2', 'S32-M-Q3', 'S32-M-Q4', 'S32-M-Q5', 'S33-M-*', 'S34-M-Q1', 'S34-M-Q2', 'S34-M-Q3', 'S34-M-Q5'], 'V04', 'revised',
     'Students compute or measure the lengths, angles, or slopes before and after the rigid motion; drawing items also ask for the comparison.'),
    # ---- forward branches
    (['S2-F1-*'], 'F01', 'revised', 'Letter coefficients from repeating decimals (x = d/9, x = n/99) and a parameter condition; branch title updated.'),
    (['S16-F1-*'], 'F01', 'revised', 'Parameter values that give a system no, one, or infinitely many solutions; branch title updated.'),
    (['S18-F1-*'], 'F01', 'revised', 'Mixture and rate systems, and judging whether a solution makes sense; branch title updated.'),
    (['S21-F1-*'], 'F01', 'revised', 'Elimination giving 0 = 9 or 0 = 0, and a system with letter coefficients; branch title updated.'),
    (['S28-F1-*'], 'F01', 'revised', 'Functions with thresholds, fees, and restricted domains; branch title updated.'),
    (['S29-F1-*'], 'F01', 'revised', 'Interpreting slope and intercept when units or the starting year change; branch title updated.'),
    (['S30-F1-*'], 'F01', 'revised', 'Key features of a curved ball-height graph: maximum, intervals, intercept; branch title updated.'),
    (['S40-F1-*'], 'F01', 'revised', 'Uses the definition of similarity transformations to prove equal angles and proportional sides; branch title updated.'),
    (['S43-F2-*'], 'F01', 'revised', 'Multistep similarity: altitude to the hypotenuse, parallel segments, and a mirror problem; branch title updated.'),
    (['S9-F1-Q2', 'S9-F1-Q3'], 'F02', 'revised', 'Choose a reporting precision from a scale\'s and a stopwatch\'s resolution.'),
    (['S12-F2-Q2', 'S12-F2-Q3', 'S12-F2-Q4', 'S12-F2-Q5'], 'F03', 'revised', 'Define the quantities, meanings, and units a model needs.'),
    (['S14-F1-*', 'S22-F1-*'], 'F04', 'revised', 'Students graph two-variable equations with labels and scales; quadratic area and revenue models; branch titles updated.'),
    (['S20-F1-*'], 'F05', 'revised', 'Proves that the elimination step keeps the solution set, in both directions; branch title updated.'),
    (['S35-F2-*'], 'F06', 'revised', 'Explains SAS, ASA, and SSS by following rigid motions; branch title updated.'),
    (['S45-F1-*'], 'F07', 'revised', 'Proves the converse of the Pythagorean theorem with a constructed right triangle and SSS; branch title updated.'),
    (['S46-F1-Q2', 'S46-F1-Q3'], 'F08', 'revised', 'Ramp and kite problems use given sine values.'),
    (['S47-F1-*'], 'F08', 'revised', 'Three-dimensional problems with tangent and sine values; branch title updated.'),
    (['S46-F2-*'], 'F09', 'revised', 'Design decisions under constraints: ramp slope rule, cabinet fit, cable placement, ladder safety; branch title updated.'),
    (['S53-F1-*'], 'F10', 'revised', 'Compares linear, quadratic, and exponential models and finds a least-squares line with technology; branch title updated.'),
    (['S55-F1-*'], 'F10', 'revised', 'Least-squares line with technology and comparing lines by squared residuals; branch title updated.'),
    (['S20-F2-*'], 'F11', 'revised', 'Q2 is a student graph of y = x² - 1 and y = x + 1 with an algebraic check; branch title updated.'),
    (['S43-F1-Q2'], 'F12', 'revised', 'The explanation adds the dilation and rigid motions that put the third vertex on F.'),
    (['S3-F2-*', 'S11-F2-*', 'S33-F2-*', 'S36-F2-*', 'S38-F2-*', 'S41-F2-*', 'S47-F2-*'], 'F13', 'revised',
     'Marked NEAREST RELATED: no high-school standard directly continues the set\'s skill at this step. Questions unchanged.'),
    # ---- recommended
    (['S26-M-Q3'], 'P01', 'revised', 'Original nonlinear example: handshakes h = n(n - 1) ÷ 2 with n = 2, 3, 4; still not linear.'),
    (['S35-F1-Q1'], 'P02', 'revised', 'Asks for the reason with rigid motions: they map AB onto DE and angle B onto angle E and keep measures.'),
    (['S44-F2-Q2'], 'P02', 'revised', 'Answer with required work: derive the circle equation from a right triangle and the Pythagorean theorem.'),
    (['S1-F1-Q1'], 'P03', 'revised', 'Explain why 4 + √3 is irrational (assume it is rational and reach a contradiction).'),
    (['S6-F1-*'], 'P03', 'revised', 'Q1 and Q2 explain why 5^(1/2) = √5 and 8^(1/3) = 2 follow from the power-of-a-power property; branch title updated.'),
    (['S9-F2-*'], 'P03', 'revised', 'Q1 and Q2 solve exponential equations with logarithms (with a calculator for one); branch title updated.'),
    (['S54-F2-Q1'], 'P04', 'revised', 'Compute r for given data with a calculator or spreadsheet (r ≈ 0.85) and describe it.'),
    (['S55-F2-Q2'], 'P04', 'revised', 'Students find four residuals and plot them on a residual grid.'),
    (['S55-F2-Q3'], 'P04', 'revised', 'Small, patternless residuals suggest a linear model is appropriate (not "good fit").'),
    (['S31-M-Q4'], 'P05', 'revised', 'The rubric keeps the clock times 7:00, 9:30, and 10:00.'),
    (['S56-F2-Q2'], 'P05', 'revised', 'States that the data lie close to the line; the key notes the fit as well as the range.'),
    (['S52-M-Q4'], 'P05', 'revised', 'States a straight-sided container, its inside radius, and no spilling; still 1.44 cm.'),
    (['S49-M-Q5', 'S50-F2-Q4', 'S50-F2-Q5'], 'P05', 'revised', 'States which dimension stays the same when the other doubles.'),
    (['S13-F2-Q1', 'S13-F2-Q2'], 'P06', 'revised', 'Compare a linear function with a quadratic table and with an exponential function.'),
    (['S7-F2-Q1'], 'P06', 'revised', 'A scaling question: a cube\'s volume is multiplied by 27, so each edge is multiplied by 3.'),
]
