"""Grade 5 revision 2.0.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is
    (ID patterns, finding code, status, reason)
status: 'revised' (ID kept), 'retired' (ID removed, never reused), 'new', or 'layout'
(the record is unchanged; only the PDF answer page was corrected).
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'aa3ca86'

FINDINGS = {
    'C01': 'Juice units (S42-F1-Q4)',
    'C02': 'Remainder form (S17-M-Q5)',
    'C03': 'Clipped expanded form in the answer key PDF (S13-M-Q1)',
    'C04': 'Clipped choice explanation in the answer key PDF (S13-M-Q3)',
    'C05': 'Clipped powers-of-ten answer in the answer key PDF (S13-F1-Q1)',
    'C06': 'Plot plus written answer: combined drawing + written response',
    'C07': 'Required model/equation omitted from grading (S18-M-Q4)',
    'C08': 'Tank capacity versus starting amount (S35-F2-Q4)',
    'C09': 'Zero excluded from the equivalent-fraction rule (S34-B1-Q1)',
    'C10': 'Positive multiples',
    'C11': 'Cube edge length (S48-F1-Q3)',
    'C12': 'Geometry definitions (isosceles, kite)',
    'C13': 'Estimation grading: rounding strategy stated',
    'B01': 'Backward branch used a Grade 5 standard; rebuilt from a Grade 4-or-earlier prerequisite',
    'B02': 'Grade 3 fraction scope (denominators 2, 3, 4, 6, 8)',
    'B03': 'Grade 2 array size (at most 5 by 5)',
    'B04': 'Grade 4 multiplication size (S17-B2-Q2)',
    'B05': 'Scaled bar graph label: questions now use a scaled bar graph',
    'B06': 'Main real-world label: S36 main questions are real-world problems',
    'B07': 'Backward quick hits: one step each (S51-B1)',
    'F01': 'Actual constructions for 7.G.A.2',
    'F02': 'Grade 7 angle progression: unknown-angle equations with diagrams',
    'F03': 'Grade 7 statistics progression: difference in centers compared with variability',
    'F04': 'Sample inference for 7.SP.B.4 (S44-F2-Q5)',
    'F05': 'Grade 6 progression: area by decomposition (S56-F1-Q3)',
    'F06': 'Proportional graph context stated (S52-F2-Q5)',
    'F07': 'Branches mixed distinct skills; each now has one skill',
    'F08': 'Coordinate grids name their axes x and y',
    'O01': 'Official-example reuse replaced with original values or contexts',
    'COV': 'Coverage: focused section added or split so each Grade 5 requirement has its own five variations',
    'M01': 'A question that asks for a method (standard algorithm, long division) now grades the method',
}

# old ID -> new ID for questions that moved to a new set or branch unchanged (or with the listed correction)
MOVES = [
    ('S19-M-Q2', 'S61-M-Q1'), ('S19-M-Q4', 'S61-M-Q2'), ('S19-M-Q5', 'S61-M-Q3'),
    ('S19-B1-Q2', 'S61-B1-Q1'), ('S19-B1-Q4', 'S61-B1-Q2'), ('S19-B1-Q5', 'S61-B1-Q3'),
    ('S19-F1-Q2', 'S61-F1-Q1'), ('S19-F1-Q4', 'S61-F1-Q2'), ('S19-F1-Q5', 'S61-F1-Q3'),
    ('S19-F2-Q2', 'S61-F2-Q1'), ('S19-F2-Q4', 'S61-F2-Q2'),
    ('S25-M-Q2', 'S65-M-Q1'), ('S25-M-Q3', 'S65-M-Q2'), ('S25-M-Q5', 'S65-M-Q3'),
    ('S25-B1-Q2', 'S65-B1-Q1'), ('S25-B1-Q4', 'S65-B1-Q2'),
    ('S34-M-Q3', 'S68-M-Q1'),
    ('S34-B1-Q1', 'S68-B1-Q1'), ('S34-B1-Q2', 'S68-B1-Q2'), ('S34-B1-Q3', 'S68-B1-Q3'),
    ('S34-B1-Q4', 'S68-B1-Q4'), ('S34-B1-Q5', 'S68-B1-Q5'),
]

# retired branch -> the new branch that replaces it in the same set (B01)
BRANCH_REPLACEMENTS = [
    ('S7-B2', 'S7-B4'), ('S20-B3', 'S20-B4'), ('S21-B3', 'S21-B4'), ('S26-B3', 'S26-B4'),
    ('S32-B3', 'S32-B4'), ('S35-B3', 'S35-B4'), ('S36-B2', 'S36-B4'), ('S37-B3', 'S37-B4'),
    ('S39-B2', 'S39-B3'), ('S40-B3', 'S40-B4'), ('S41-B3', 'S41-B4'), ('S44-B2', 'S44-B4'),
    ('S44-B3', 'S44-B5'), ('S51-B2', 'S51-B3'), ('S53-B1', 'S53-B3'), ('S54-B1', 'S54-B3'),
]

NEW_SETS = {
    'S58': '5.OA.B.3 — explain why two patterns have the relationship they do (S6 covered only generating and comparing terms).',
    'S59': '5.NBT.A.2 — explain the patterns in the number of zeros and the placement of the decimal point (S10–S11 only computed).',
    'S60': '5.NBT.B.6 — draw division models and explain the strategy (S18 added to; representations graded).',
    'S61': '5.NBT.B.7 — subtract decimals, split from S19 (S19 is now addition only).',
    'S62': '5.NBT.B.7 — place-value models and explanations for adding and subtracting decimals.',
    'S63': '5.NBT.B.7 — models and place-value explanations for multiplying decimals.',
    'S64': '5.NBT.B.7 — models and place-value explanations for dividing decimals.',
    'S65': '5.NF.A.1 — subtract mixed numbers, split from S25 (S25 is now addition only).',
    'S66': '5.NF.B.4.a — interpret fraction products with tape diagrams and area models.',
    'S67': '5.NF.B.4.b — tile a rectangle with unit-fraction squares and connect the tiling to the area.',
    'S68': '5.NF.B.5.b — explain equivalent fractions as multiplying by 1, split from S34 (S34 is now size-change reasoning).',
    'S69': '5.NF.B.7.a — division models and the multiplication check for a unit fraction divided by a whole number.',
    'S70': '5.NF.B.7.b — division models and the multiplication check for a whole number divided by a unit fraction.',
    'S71': '5.G.B.4 — triangles in a hierarchy of categories and subcategories.',
}


def _moves():
    out = []
    for old, new in MOVES:
        out.append(([new], 'COV', 'new', 'Moved from %s.' % old))
    return out


def _branches():
    out = []
    for old, new in BRANCH_REPLACEMENTS:
        out.append(([old + '-*'], 'B01', 'retired', 'Retired: the branch used a Grade 5 standard. Replaced by %s.' % new))
        out.append(([new + '-*'], 'B01', 'new', 'Replaces %s with a Grade 4-or-earlier prerequisite.' % old))
    return out


def _new_sets():
    return [([s + '-*'], 'COV', 'new', 'New focused set: ' + text) for s, text in NEW_SETS.items()]


CHANGES = _moves() + _branches() + _new_sets() + [
    # ---- section 1
    (['S42-F1-Q4'], 'C01', 'revised', 'Context changed to a 24-ounce bag of rice, so ounces measure weight; answer still $2 per pound.'),
    (['S17-M-Q5'], 'C02', 'revised', 'Only quotient 31 and remainder 8 are accepted; the mixed number and decimal were removed from the grading note.'),
    (['S13-M-Q1'], 'C03', 'layout', 'The answer key PDF now wraps the full expanded form instead of clipping it.'),
    (['S13-M-Q3'], 'C04', 'revised', 'The answer key PDF shows the full choice; its plain text groups fractions: 6 × 1 + 4 × (1/100) + 5 × (1/1000).'),
    (['S13-F1-Q1'], 'C05', 'layout', 'The answer key PDF now wraps the full answer 5 × 10³ + 3 × 10² + 2 × 10¹ + 7.'),
    (['S7-F2-Q3', 'S53-M-Q5', 'S53-F2-Q1', 'S53-F2-Q2', 'S53-F2-Q5'], 'C06', 'revised',
     'Now a drawing + written response: the plotted points and the written conclusion are both graded.'),
    (['S55-F1-Q1', 'S55-F1-Q2'], 'C06', 'revised',
     'Now a drawing + written response that asks for the most specific polygon name (rectangle; square).'),
    (['S18-M-Q4'], 'C07', 'revised', 'Requires and grades an area model or equations as well as the quotient 78.'),
    (['S35-F2-Q4'], 'C08', 'revised', 'The tank "contains" 12 1/2 gallons, so the starting amount is stated.'),
    (['S68-B1-Q1'], 'C09', 'new', 'Multiplying numerator and denominator by the same nonzero whole number (zero excluded).'),
    (['S23-B3-Q1', 'S23-B3-Q4', 'S24-B3-Q1', 'S24-B3-Q4'], 'C10', 'revised', 'Asks for positive multiples.'),
    (['S48-F1-Q3'], 'C11', 'revised', 'Says "cubes that have edges 1/2 unit long".'),
    (['S57-M-Q3'], 'C12', 'revised', 'States that isosceles means at least two sides of equal length.'),
    (['S56-B1-Q5'], 'C12', 'revised', 'Keyed example is a trapezoid with exactly one pair of parallel sides; a kite with no parallel sides is accepted; parallelograms are rejected.'),
    (['S15-F2-Q1', 'S15-F2-Q4', 'S27-F2-Q1', 'S27-F2-Q4', 'S27-F2-Q5'], 'C13', 'revised',
     'The rounding strategy is stated and both the rounded values and the estimate are graded.'),
    # ---- section 2
    (['S9-B2-*'], 'B02', 'revised', 'Unit fractions now use Grade 3 denominators (eighths, sixths, fourths, halves) instead of tenths.'),
    (['S28-B1-Q3'], 'B02', 'revised', 'The bar shows eighths instead of fifths.'),
    (['S29-B2-Q3'], 'B02', 'revised', 'Choices use halves and sixths instead of fourths and twelfths.'),
    (['S30-B2-Q5'], 'B02', 'revised', 'Uses fourths instead of fifths.'),
    (['S34-B2-Q3', 'S34-B2-Q4'], 'B02', 'revised', 'Uses eighths and sixths instead of ninths and fifths.'),
    (['S37-B1-Q2'], 'B02', 'revised', 'Unit fractions use Grade 3 denominators (2, 3, 6, 8).'),
    (['S38-B2-Q3'], 'B02', 'revised', 'Uses sixths instead of fifths.'),
    (['S46-B2-Q2', 'S46-B2-Q3'], 'B03', 'revised', 'Arrays are at most 5 by 5.'),
    (['S17-B2-Q2'], 'B04', 'revised', 'Two-digit by two-digit check (24 × 84) instead of 45 × 174.'),
    (['S7-B3-*', 'S53-B2-*'], 'B05', 'revised', 'Every question now reads a scaled bar graph.'),
    (['S36-M-*'], 'B06', 'revised', 'Bare mixed-number products replaced by real-world problems; set title updated.'),
    (['S51-B1-Q1', 'S51-B1-Q3', 'S51-B1-Q4', 'S51-B1-Q5'], 'B07', 'revised',
     'One step each: the component areas are given, or one rectangle is asked for, or the student chooses add or subtract.'),
    # ---- section 4
    (['S55-F2-*', 'S56-F2-*'], 'F01', 'revised',
     'Students draw the shapes on a grid (drawing + written response) for possible cases and explain impossible cases.'),
    (['S57-F2-*'], 'F02', 'revised', 'Unknown-angle problems with diagrams; the equation and the solution are both graded.'),
    (['S43-F2-*'], 'F03', 'revised', 'Compares the difference in means with the mean absolute deviation; range-only questions removed.'),
    (['S44-F2-Q5'], 'F04', 'revised', 'Random samples from two schools with an inference about the populations, matching 7.SP.B.4.'),
    (['S56-F1-Q3'], 'F05', 'revised', 'Area of a trapezoid by decomposing it into a rectangle and two triangles.'),
    (['S52-F2-Q5'], 'F06', 'revised', 'States that the graph shows a proportional relationship.'),
    (['S36-F2-*'], 'F07', 'revised', 'Branch is now surface area only (volume items replaced).'),
    (['S49-F2-*'], 'F07', 'revised', 'Branch is now volume only (the surface-area item replaced).'),
    (['S53-F1-*'], 'F07', 'revised', 'Branch is now reflections across the axes only (plotting and quadrant items replaced).'),
    # ---- section 5
    (['S6-M-Q1'], 'O01', 'revised', 'Patterns now add 6 and 18.'),
    (['S27-M-Q1'], 'O01', 'revised', 'New error example: 3/4 + 1/6 = 4/10.'),
    (['S31-M-Q1'], 'O01', 'revised', 'Now 3/4 × 2/7.'),
    (['S37-M-Q1'], 'O01', 'revised', 'Now 1/7 ÷ 2.'),
    (['S38-M-Q1'], 'O01', 'revised', 'Now 6 ÷ 1/5.'),
    (['S39-M-Q1'], 'O01', 'revised', 'New context: 1/4-cup scoops of birdseed in 3 cups.'),
    (['S39-M-Q2'], 'O01', 'revised', 'New context: 4 students share 1/3 liter of paint.'),
    (['S55-M-Q1'], 'O01', 'revised', 'New example: parallelogram and rhombus attributes.'),
    # ---- section 3 (coverage) and method grading
    (['S16-M-*'], 'COV', 'revised', 'The standard algorithm is required and graded (answer with required work); Q3 asks for a missing partial product.'),
    (['S19-M-*', 'S19-B1-*', 'S19-F1-*', 'S19-F2-*'], 'COV', 'revised',
     'S19 now assesses addition only; its subtraction items moved to S61.'),
    (['S25-M-*', 'S25-B1-*'], 'COV', 'revised', 'S25 now assesses addition of mixed numbers only; its subtraction items moved to S65.'),
    (['S34-M-Q3'], 'COV', 'revised', 'Now a size-change explanation; the equivalent-fraction explanation moved to S68-M-Q1.'),
    (['S34-B1-*'], 'COV', 'retired', 'Moved to S68-B1 (equivalent fractions support S68, not size-change reasoning).'),
    (['S34-B3-*'], 'COV', 'new', 'Size-change prerequisite: multiply a whole number by a fraction (4.NF.B.4.b).'),
    (['S9-F2-Q1', 'S9-F2-Q2', 'S9-F2-Q4', 'S12-F2-Q1', 'S12-F2-Q2', 'S12-F2-Q4', 'S13-F2-Q2', 'S13-F2-Q4', 'S28-F2-Q2'], 'M01', 'revised',
     'The long division is required and graded (answer with required work).'),
    (['S17-F1-Q1', 'S17-F1-Q2', 'S17-F1-Q4'], 'M01', 'revised', 'The standard division algorithm is required and graded.'),
    (['S17-F1-Q3'], 'M01', 'revised', 'A multiple-choice item cannot show a method, so it now just says "Divide."'),
]
