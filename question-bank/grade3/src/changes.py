"""Grade 3 revision 2.0.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is
    (ID patterns, finding code, status, reason)
status: 'revised' (ID kept), 'retired' (ID removed, never reused), 'new', or 'layout'.
Finding codes are those of Grade3_Complete_Review.md.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'b90ef11'

FINDINGS = {
    'C01': '"Round each number" changed the keyed estimate (S19-F1-Q3)',
    'C02': 'A triangle with sides 1/2, 1/3, and 1/6 cannot exist (S55-F2-Q2)',
    'C03': '"Can be used" made the unit-cube choice ambiguous (S48-F2-Q2)',
    'C04': 'A generic diagram request had a narrow drawing key (S7-M-Q4)',
    'C05': 'Partition rubrics imposed line counts the prompts did not ask for (S60-M, S61-M-Q4)',
    'C06': 'Different prisms: whole-number and noncongruence conditions stated (S57-F2-Q1)',
    'C07': 'Different-whole explanation now concerns physical amounts (S37-M-Q2)',
    'C08': 'An optional model is no longer required by the rubric (S33-M-Q5)',
    'C09': 'Required number-line work now has a drawing field (S40-F1-Q1)',
    'C10': 'Composite figures and solids state that the parts do not overlap (S54-F1, S54-F2)',
    'C11': 'Grid rectangles: whole-number sides and different length-width pairs stated (S57-M-Q1)',
    'B01': 'Grade 2 array kept to at most 5 rows and 5 columns (S57-B2-Q1, now S67-B1-Q1)',
    'B02': 'Estimation branch now estimates lengths with numbers and units (S50-B2)',
    'B03': 'Unit-iteration items replace length arithmetic (S46-B2, S49-B1)',
    'B04': 'Perimeter prerequisite added for S57 (S57-B3)',
    'B05': 'Division fluency diagnosed with equal rows of arrays (S15-B3 replaces S15-B1)',
    'F01': 'Grade 5 fraction branches use fractional quantities (S1-F2, S7-F2, S10-F2, S29-F2)',
    'F02': 'Unit-fraction division items are real-world problems (S4-F2)',
    'F03': 'Expression branch writes and interprets expressions instead of evaluating (S17-F2)',
    'F04': 'S19 checks the reasonableness of answers to two-step word problems',
    'F05': 'Grade 4 reasonableness branch is multistep throughout, with explicit rounding (S19-F1)',
    'F06': 'Grade 4 remainder branch uses multistep problems (S4-F1)',
    'F07': 'Fractions use the grade\'s denominators (Grade 3: 2, 3, 4, 6, 8; Grade 4: 2, 3, 4, 5, 6, 8, 10, 12, 100)',
    'F08': 'Grade 4 mixed-number addition uses like denominators (S46-F1)',
    'F09': 'Contextual graph item replaces an axis fact (S44-F2-Q5)',
    'F10': 'Volume item counts unit-cube layers (S51-F2-Q4)',
    'F11': 'Grade 5 branch is the standard multiplication algorithm throughout (S53-F2)',
    'F12': 'Fractional-side-area branch uses fractional dimensions and tiles (S60-F2)',
    'F13': 'Product is compared with one of its factors (S36-F2-Q4)',
    'F14': 'Parallel and perpendicular sides identified in labeled diagrams (S59-F1)',
    'V01': 'Two-step comparisons from scaled bar graphs (new set S62)',
    'V02': 'Numerical mass and liquid-volume measurement (new sets S63, S64); S41 is estimation only',
    'V03': 'Graph-making sets and branches are five actual constructions (S43, S44, S47); reading moved to S65, S66',
    'V04': 'Same perimeter (S57) and same area (new S67) are separate sets',
    'V05': 'Branches focused on one skill (S28-F1, S37-F1, S61-F1, S61-F2)',
    'V06': 'Different-size wholes (S37) and model justification (new S68) are separate sets',
    'V07': 'Measure several objects and plot the measurements (new set S69)',
    'V08': 'Grade 3 two-step problem uses equal groups instead of "times as many" (S17-M-Q5)',
}

# old ID -> new ID for questions that moved to a new set or branch unchanged (or with the listed correction)
MOVES = [
    ('S41-M-Q1', 'S64-M-Q1'), ('S41-M-Q5', 'S64-M-Q2'),
    ('S43-M-Q2', 'S65-M-Q1'), ('S43-M-Q3', 'S65-M-Q2'), ('S43-M-Q4', 'S65-M-Q3'), ('S43-M-Q5', 'S65-M-Q4'),
    ('S43-B1-Q3', 'S65-B1-Q1'), ('S43-B1-Q4', 'S65-B1-Q2'), ('S43-B1-Q5', 'S65-B1-Q3'), ('S43-B1-Q2', 'S65-B1-Q4'),
    ('S44-M-Q2', 'S66-M-Q1'), ('S44-M-Q3', 'S66-M-Q2'), ('S44-M-Q4', 'S66-M-Q3'), ('S44-M-Q5', 'S66-M-Q4'),
    ('S44-B1-Q2', 'S66-B1-Q1'), ('S44-B1-Q3', 'S66-B1-Q2'), ('S44-B1-Q4', 'S66-B1-Q3'), ('S44-B1-Q5', 'S66-B1-Q4'),
    ('S57-M-Q2', 'S67-M-Q1'), ('S57-M-Q3', 'S67-M-Q2'), ('S57-M-Q4', 'S67-M-Q3'),
    ('S57-B2-Q1', 'S67-B1-Q1'), ('S57-B2-Q2', 'S67-B1-Q2'), ('S57-B2-Q3', 'S67-B1-Q3'), ('S57-B2-Q4', 'S67-B1-Q4'), ('S57-B2-Q5', 'S67-B1-Q5'),
    ('S37-M-Q3', 'S68-M-Q1'), ('S37-M-Q4', 'S68-M-Q2'),
]
MOVE_FINDING = {'S64': 'V02', 'S65': 'V03', 'S66': 'V03', 'S67': 'V04', 'S68': 'V06'}

# retired branch -> the new branch that replaces it in the same set
BRANCH_REPLACEMENTS = [('S15-B1', 'S15-B3'), ('S57-B2', 'S57-B3')]

NEW_SETS = {
    'S62': ('V01', '3.MD.B.3 — two-step "how many more" and "how many fewer" problems using scaled bar graphs.'),
    'S63': ('V02', '3.MD.A.2 — measure mass in grams and kilograms with a scale.'),
    'S64': ('V02', '3.MD.A.2 — measure liquid volume in liters with a marked container (S41 is now estimation only).'),
    'S65': ('V03', '3.MD.B.3 — use the key of a scaled picture graph; the reading items moved here from S43.'),
    'S66': ('V03', '3.MD.B.3 — read the scale of a scaled bar graph and choose a scale; the reading items moved here from S44.'),
    'S67': ('V04', '3.MD.D.8 — rectangles with the same area and different perimeters, split from S57.'),
    'S68': ('V06', '3.NF.A.3.d — justify a comparison of two fractions of the same whole with a visual model, split from S37.'),
    'S69': ('V07', '3.MD.B.4 — measure several objects to the nearest half or quarter inch, then make a line plot of the measurements.'),
}


def _moves():
    return [([new], MOVE_FINDING[new.split('-')[0]], 'new', 'Moved from %s.' % old) for old, new in MOVES]


def _new_sets():
    return [([s + '-*'], code, 'new', 'New focused set: ' + text) for s, (code, text) in NEW_SETS.items()]


CHANGES = _moves() + _new_sets() + [
    # ---- section 2: content, wording, and grading
    (['S19-F1-Q3'], 'C01', 'revised', 'Says to keep 4 unchanged and round 39 and 52 to the nearest ten; still 210, now in a multistep word problem.'),
    (['S55-F2-Q2'], 'C02', 'revised', 'Sides are now 1/2 m, 1/3 m, and 1/4 m (a real triangle); the perimeter is 1 1/12 m; still True.'),
    (['S48-F2-Q2'], 'C03', 'revised', 'Asks which object has a volume of exactly 1 cubic unit; the only correct choice is a cube with edges 1 unit long.'),
    (['S7-M-Q4'], 'C04', 'revised', 'Any valid diagram of a 20-foot total made of five equal 4-foot pieces is accepted, including labeled pieces.'),
    (['S60-M-Q1', 'S60-M-Q2', 'S61-M-Q4'], 'C05', 'revised',
     'Any partition into the requested number of equal-area parts is accepted; the straight-line splits are examples only.'),
    (['S57-F2-Q1'], 'C06', 'revised', 'Asks for two noncongruent prisms with positive whole-number edge lengths; reordered dimensions are not different.'),
    (['S37-M-Q2'], 'C07', 'revised', 'Accepts any explanation that the amount depends on the sizes of the wholes; no blanket rule is required.'),
    (['S33-M-Q5'], 'C08', 'revised', 'A sound verbal explanation, a labeled model, or a number line is accepted; a drawing is not required.'),
    (['S40-F1-Q1'], 'C09', 'revised', 'Now a drawing + written answer on a 9:00 a.m. to 1:00 p.m. number line; the jumps and the duration are both graded.'),
    (['S54-F1-Q1', 'S54-F1-Q2', 'S54-F1-Q4', 'S54-F1-Q5', 'S54-F2-Q2', 'S54-F2-Q3', 'S54-F2-Q4'], 'C10', 'revised',
     'States that the parts are joined without overlapping (face to face for the prisms).'),
    (['S57-M-Q1'], 'C11', 'revised', 'Requires rectangles along grid lines with whole-number sides and different length-and-width pairs.'),
    # ---- section 3: earlier-grade diagnosis
    (['S67-B1-Q1'], 'B01', 'new', 'Uses arrays of 2 rows of 5 and 5 rows of 2 (both at most 5 by 5) instead of 2 rows of 6.'),
    (['S50-B2-*'], 'B02', 'revised', 'Every item estimates a length with a number and a unit.'),
    (['S46-B2-Q3', 'S46-B2-Q4', 'S49-B1-Q4'], 'B03', 'revised', 'Unit iteration (same-size units end to end, no gaps or overlaps) replaces length arithmetic.'),
    (['S57-B2-*'], 'B04', 'retired', 'Moved to S67-B1 (equal-total arrays support the same-area set). Replaced in S57 by S57-B3.'),
    (['S57-B3-*'], 'B04', 'new', 'Perimeter prerequisite for S57: add the four side lengths of a rectangle (2.NBT.B.6).'),
    (['S15-B1-*'], 'B05', 'retired', 'Retired: general subtraction did not isolate equal grouping. Replaced by S15-B3.'),
    (['S15-B3-*'], 'B05', 'new', 'Replaces S15-B1: equal rows in arrays up to 5 by 5 (2.OA.C.4).'),
    # ---- section 4: forward branches
    (['S1-F2-*', 'S7-F2-*', 'S10-F2-*', 'S29-F2-*'], 'F01', 'revised', 'Uses fractional quantities as well as fractional multipliers; branch title updated.'),
    (['S4-F2-Q2', 'S4-F2-Q4', 'S4-F2-Q5'], 'F02', 'revised', 'Bare calculations rewritten as real-world unit-fraction grouping problems.'),
    (['S17-F2-Q4', 'S17-F2-Q5'], 'F03', 'revised', 'Q4 writes an expression for a multistep calculation; Q5 judges whether an expression matches words, without evaluating.'),
    (['S19-M-*'], 'F04', 'revised', 'Each item checks the reasonableness of an answer to a two-step word problem, with the numbers to round stated; set title updated.'),
    (['S19-F1-*'], 'F05', 'revised', 'Every item checks a proposed answer to a multistep word problem, with explicit rounding targets; branch title updated.'),
    (['S4-F1-*'], 'F06', 'revised', 'Five multistep remainder problems (complete groups, leftovers, and rounding up); branch title updated.'),
    (['S28-M-Q2', 'S29-M-Q5', 'S30-M-Q5', 'S31-F1-Q3', 'S33-F1-Q1', 'S33-F1-Q5', 'S35-F1-Q4', 'S36-F1-Q2', 'S36-F1-Q4', 'S37-F1-Q3'], 'F07', 'revised',
     'Fractions use the grade\'s denominators; exactly one choice is still correct.'),
    (['S46-F1-Q2', 'S46-F1-Q4'], 'F08', 'revised', 'Like denominators: 2 2/4 + 1 3/4 = 4 1/4 and 2/4 + 3/4 + 1/4 = 1 2/4.'),
    (['S44-F2-Q5'], 'F09', 'revised', 'False interpretation of a point on a days-and-hats graph instead of an axis fact.'),
    (['S51-F2-Q4'], 'F10', 'revised', 'Counts unit-cube layers (6 cubes in each of 2 layers, 12 cubic units) instead of base area times height.'),
    (['S53-F2-*'], 'F11', 'revised', 'Every item is multi-digit multiplication with the standard algorithm; branch title updated.'),
    (['S60-F2-Q1', 'S60-F2-Q3', 'S60-F2-Q5'], 'F12', 'revised', 'Fractional side lengths tiled with unit-fraction tiles.'),
    (['S36-F2-Q4'], 'F13', 'revised', 'Compares 1/3 × 9 with its factor 9 (less than 9).'),
    (['S59-F1-Q3', 'S59-F1-Q4', 'S59-F1-Q5'], 'F14', 'revised', 'Identify parallel and perpendicular sides in labeled quadrilateral diagrams.'),
    # ---- section 5: coverage and focused sets
    (['S41-M-*'], 'V02', 'revised', 'S41 is estimation only (set title updated); its reading items moved to S64.'),
    (['S43-M-Q2', 'S43-M-Q3', 'S43-M-Q4', 'S43-M-Q5', 'S44-M-Q2', 'S44-M-Q3', 'S44-M-Q4', 'S44-M-Q5', 'S47-M-Q2', 'S47-M-Q3', 'S47-M-Q4'],
     'V03', 'revised', 'Now an actual graph construction with new data on a blank graph; the reading items moved to S65 and S66.'),
    (['S43-B1-*', 'S44-B1-*'], 'V03', 'revised', 'The drawing branch is now five actual constructions; branch title updated.'),
    (['S43-F1-Q2', 'S43-F1-Q3', 'S43-F1-Q4', 'S43-F1-Q5', 'S47-F1-Q2', 'S47-F1-Q3', 'S47-F1-Q5'], 'V03', 'revised',
     'Now an actual line-plot construction, so all five items in the branch make a line plot.'),
    (['S57-M-*'], 'V04', 'revised', 'S57 is same perimeter, different areas only (set title updated); same-area items moved to S67.'),
    (['S57-F1-*'], 'V04', 'revised', 'Branch compares areas of rectangles with the same perimeter; branch title updated.'),
    (['S28-F1-Q4', 'S37-F1-Q4', 'S61-F1-Q4', 'S61-F2-Q5'], 'V05', 'revised',
     'Rewritten to match the branch skill (unit-fraction decomposition; benchmark comparison; joining parts; adding portions).'),
    (['S37-M-*'], 'V06', 'revised', 'S37 is the amounts named by fractions of different-size wholes (set title updated); model items moved to S68.'),
    (['S17-M-Q5'], 'V08', 'revised', 'Uses equal groups ("4 sections of 8 pages") instead of "4 times as many".'),
]
