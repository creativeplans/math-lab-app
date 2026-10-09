"""Grade 4 revision 2.0.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is
    (ID patterns, finding code, status, reason)
status: 'revised' (ID kept), 'retired' (ID removed, never reused), 'new', or 'layout'
(the record is unchanged; only the PDF answer page was corrected).
Finding codes are those of Grade4_Complete_Review.md.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'c61ef76'

FINDINGS = {
    'C01': 'Denominator 100 required, but another form accepted (S28-F2-Q4)',
    'C02': 'Hours-and-minutes form required, but minutes alone accepted (S45-M-Q5)',
    'C03': 'Equivalent options made the intended multiple-choice transformation ambiguous (S28-F1-Q2)',
    'C04': 'Same unstated transformation convention in a short answer (S28-F1-Q3)',
    'C05': 'A rotated right triangle could be rejected (S62-M-Q5)',
    'C06': 'Required-work rubric narrower than the permitted methods (S24-M-Q4, S26-M-Q4)',
    'C07': 'Remaining-length bar did not necessarily show the requested cut (S47-M-Q5)',
    'C08': 'Non-rectangle example needed a clear non-square condition (S60-B2-Q5)',
    'C09': 'Non-square rectangle example needed a clear condition (S59-B2-Q5)',
    'C10': 'Triangle symmetry wording now excludes an equilateral triangle (S64-M-Q3)',
    'C11': 'Fraction response convention stated: fraction or mixed number (S33-B2-Q1, Q4)',
    'C12': 'Approximation wording made exact (S8-F2-Q3)',
    'B01': 'Grade 2 parity items use numbers up to 20',
    'B02': 'Grade 3 fraction distractors use denominators 2, 3, 4, 6, and 8',
    'B03': 'Hundred-as-ten-tens branches (2.NBT.A.1.a) rebuilt around that idea',
    'B04': 'Backward branch solved the whole two-step problem; replaced by one-step diagnosis (S6)',
    'B05': 'Unknown-perimeter backward items are one step each',
    'B06': 'Composite-area backward item gives the two areas (S56-B2-Q3)',
    'B07': 'Multiplication branch contained division questions (S3-B1)',
    'B08': 'Unknown-factor branch connects each division to its unknown-factor equation (S9-B1)',
    'B09': 'Word-problem label now has word problems (S57-B1)',
    'B10': 'Parallel/perpendicular diagnosis uses square corners and same-direction sides instead of counting arrays (S60)',
    'F01': 'Scaling comparison without computing (S1-F1-Q3)',
    'F02': 'Grade 5 branch advances to a fraction of a fractional amount (S36-F1)',
    'F03': 'Real-world Grade 5 variations use fractional starting lengths (S38-F1-Q2, Q5)',
    'F04': 'Recipe ratio replaced by an actual unit conversion (S43-F2-Q4)',
    'F05': 'Polygon branch is about drawing polygons from vertices and side lengths (S64-F2)',
    'F06': 'Related extensions marked NEAREST RELATED (S53-F1, S53-F2, S56-F1)',
    'F07': 'First-quadrant branch solves problems with the plotted points (S55-F1)',
    'F08': 'Computation-and-rounding branch item now rounds (S19-F2-Q2)',
    'V01': 'Multistep remainder problems now assessed (new set S65)',
    'V02': 'Area and perimeter split into focused sets (S48/S68, S49/S69)',
    'V03': 'Drawing of every 4.G.A.1 object and identification inside figures (new sets S70-S73)',
    'V04': 'Fraction visual explanation includes part size (S27-M-Q1)',
    'V05': 'Minutes/seconds, liters/milliliters, and kilometers/meters conversions in MAIN (S43, S44)',
    'V06': 'Visual circle-and-arc task for angle measure (S52)',
    'V07': 'Mixed sections normalized to one skill each',
    'OPT': 'Optional review improvement: 1 is neither prime nor composite (S11)',
}

# old ID -> new ID for questions that moved to a new set or branch unchanged (or with the listed correction)
MOVES = [
    ('S35-M-Q2', 'S66-M-Q1'), ('S35-M-Q4', 'S66-M-Q2'), ('S35-M-Q5', 'S66-M-Q3'),
    ('S35-B1-Q1', 'S66-B1-Q1'), ('S35-B1-Q4', 'S66-B1-Q2'), ('S35-B1-Q5', 'S66-B1-Q3'),
    ('S35-F1-Q2', 'S66-F1-Q1'), ('S35-F1-Q4', 'S66-F1-Q2'),
    ('S39-M-Q2', 'S67-M-Q1'), ('S39-M-Q3', 'S67-M-Q2'), ('S39-M-Q5', 'S67-M-Q3'),
    ('S48-M-Q2', 'S68-M-Q1'), ('S48-M-Q4', 'S68-M-Q2'),
    ('S48-B2-Q1', 'S68-B1-Q1'), ('S48-B2-Q2', 'S68-B1-Q2'), ('S48-B2-Q3', 'S68-B1-Q3'),
    ('S48-B2-Q4', 'S68-B1-Q4'), ('S48-B2-Q5', 'S68-B1-Q5'),
    ('S49-M-Q2', 'S69-M-Q1'), ('S49-M-Q4', 'S69-M-Q2'),
    ('S49-B1-Q1', 'S69-B1-Q1'), ('S49-B1-Q2', 'S69-B1-Q2'), ('S49-B1-Q3', 'S69-B1-Q3'),
    ('S49-B1-Q4', 'S69-B1-Q4'), ('S49-B1-Q5', 'S69-B1-Q5'),
    ('S58-M-Q4', 'S70-M-Q1'), ('S59-M-Q4', 'S71-M-Q1'), ('S60-M-Q4', 'S72-M-Q1'),
]

NEW_SETS = {
    'S65': '4.OA.A.3 — multistep word problems in which a remainder must be interpreted (V01).',
    'S66': '4.NF.B.3.d — word problems that subtract fractions and mixed numbers, split from S35 (S35 is now addition only) (V07).',
    'S67': '4.NF.C.5 — add two fractions with denominators 10 and 100, split from S39 (S39 is now tenths as hundredths only) (V07).',
    'S68': '4.MD.A.3 — the perimeter formula for rectangles, split from S48 (S48 is now area only) (V02).',
    'S69': '4.MD.A.3 — an unknown side from the perimeter of a rectangle, split from S49 (S49 is now from the area only) (V02).',
    'S70': '4.G.A.1 — draw points, lines, line segments, and rays (V03).',
    'S71': '4.G.A.1 — draw right, acute, and obtuse angles (V03).',
    'S72': '4.G.A.1 — draw perpendicular and parallel lines (V03).',
    'S73': '4.G.A.1 — identify segments, angles, and perpendicular and parallel sides in two-dimensional figures (V03).',
}


def _moves():
    out = []
    for old, new in MOVES:
        out.append(([new], 'V07' if new[:3] in ('S66', 'S67') else 'V02' if new[:3] in ('S68', 'S69') else 'V03', 'new',
                    'Moved from %s.' % old))
    return out


def _new_sets():
    return [([s + '-*'], 'V01' if s == 'S65' else 'V07' if s in ('S66', 'S67') else 'V02' if s in ('S68', 'S69') else 'V03',
             'new', 'New focused set: ' + text) for s, text in NEW_SETS.items()]


CHANGES = _moves() + _new_sets() + [
    # ---- section 1: response and grading defects
    (['S28-F2-Q4'], 'C01', 'revised', 'The grading note no longer accepts 7/20: the denominator must be 100, as the question asks.'),
    (['S45-M-Q5'], 'C02', 'revised', 'Only the hours-and-minutes form (1 hour 30 minutes) is full credit; 90 minutes alone is no longer accepted.'),
    (['S28-F1-Q2'], 'C03', 'revised',
     'Now asks by which whole number both the numerator and the denominator of 2/5 are multiplied to write 6/15; choices 3, 5, 15, 6; answer 3.'),
    (['S28-F1-Q3'], 'C04', 'revised', 'Now asks for the whole number that multiplies both parts of 5/8 to write 20/32; answer 4.'),
    (['S62-M-Q5'], 'C05', 'revised', 'Any right triangle in any orientation, with the right angle marked, is correct; the axis-aligned triangle is only an example.'),
    (['S24-M-Q4', 'S26-M-Q4'], 'C06', 'revised',
     'The required work accepts any valid area model or chain of equations; the place-value decomposition is kept as one example, '
     'and a compensation (S24) or repeated-halving (S26) example is added.'),
    (['S47-M-Q5'], 'C07', 'revised',
     'The drawing must show the removed 1/2 meter (a jump from 3 to 2 1/2, or the interval from 2 1/2 to 3 marked as cut off); '
     'a bar from 0 to 2 1/2 alone is not accepted. Drawing answer and grading note agree.'),
    (['S60-B2-Q5'], 'C08', 'revised', 'Keyed example is "a rhombus that is not a square"; squares are explicitly rejected.'),
    (['S59-B2-Q5'], 'C09', 'revised', 'Keyed example is "a rectangle whose length and width are different"; a square is not accepted.'),
    (['S64-M-Q3'], 'C10', 'revised', 'States that the triangle has exactly two sides of equal length and a base of a different length.'),
    (['S33-B2-Q1', 'S33-B2-Q4'], 'C11', 'revised', 'Asks for "a fraction or a mixed number", matching the accepted answers.'),
    (['S8-F2-Q3'], 'C12', 'revised', 'Says 46 ÷ 4 "equals 11.5" instead of "is about 11"; same correct choice.'),
    # ---- section 2: earlier-grade standards and diagnostic branches
    (['S10-B2-Q2', 'S10-B2-Q3', 'S13-B2-Q1', 'S13-B2-Q2', 'S13-B2-Q3'], 'B01', 'revised', 'Numbers and choices are 20 or less (Grade 2 range).'),
    (['S32-B1-Q3', 'S34-B1-Q3', 'S36-B1-Q3', 'S37-B2-Q3'], 'B02', 'revised',
     'Distractors use only Grade 3 denominators (2, 3, 4, 6, 8); exactly one choice is correct.'),
    (['S15-B1-Q2', 'S15-B1-Q3', 'S15-B1-Q4', 'S15-B1-Q5', 'S39-B2-Q2', 'S39-B2-Q3', 'S39-B2-Q4'], 'B03', 'revised',
     'Rebuilt around the idea that a hundred is a bundle of ten tens (2.NBT.A.1.a).'),
    (['S6-B1-*'], 'B04', 'retired', 'Retired: every item solved a whole two-step problem. Replaced by S6-B3 (one step each).'),
    (['S6-B3-*'], 'B04', 'new', 'Replaces S6-B1: one-step equal-groups problems with a symbol for the unknown (3.OA.A.3).'),
    (['S69-B1-Q1', 'S69-B1-Q3', 'S69-B1-Q4'], 'B05', 'new',
     'One step each: the sum of the known sides is given and one missing side is asked for.'),
    (['S56-B2-Q3'], 'B06', 'revised', 'Gives the two areas (12 and 6 square units) and asks for their sum.'),
    (['S3-B1-Q2', 'S3-B1-Q5'], 'B07', 'revised', 'Rewritten as one-step multiplication word problems.'),
    (['S3-B1-*'], 'B07', 'revised', 'Branch title is now "Multiplication word problems within 100".'),
    (['S9-B1-*'], 'B08', 'revised', 'Each item connects a division to its unknown-factor equation; branch title updated.'),
    (['S57-B1-*'], 'B09', 'revised', 'Bare equations replaced by one-step Grade 2 word problems with an unknown; branch title updated.'),
    (['S60-B1-*'], 'B10', 'retired',
     'Retired: counting squares in rows and columns did not diagnose line direction. Replaced by S60-B3.'),
    (['S60-B3-*'], 'B10', 'new', 'Replaces S60-B1: square corners and sides that run the same way in a rectangle (3.G.A.1).'),
    # ---- section 3: forward branches
    (['S1-F1-Q3'], 'F01', 'revised', 'Compares a rope 2 1/2 times as long with the first rope without multiplying, and explains why.'),
    (['S36-F1-*'], 'F02', 'revised', 'Every item finds a fraction of a fractional amount (for example 2/3 of 3/4); branch title updated.'),
    (['S38-F1-Q2', 'S38-F1-Q5'], 'F03', 'revised', 'Mixed-number starting lengths (7 1/2 m; a 4 1/2-mile trail).'),
    (['S43-F2-Q4'], 'F04', 'revised', 'Replaced the recipe ratio with a conversion: 15 cups to pints (2 cups in 1 pint); answer 7 1/2 pints.'),
    (['S64-F2-*'], 'F05', 'revised',
     'Branch is now drawing polygons from their vertices and finding side lengths (6.G.A.3); reflection items replaced.'),
    (['S53-F1-*', 'S53-F2-*', 'S56-F1-*'], 'F06', 'revised', 'Marked nearest_related = true (volume is a related extension of angle measure).'),
    (['S55-F1-*'], 'F07', 'revised', 'Items solve map, growth, and filling problems with plotted first-quadrant points; branch title updated.'),
    (['S19-F2-Q2'], 'F08', 'revised', 'Now 7.25 × 4.2 rounded to the nearest whole number (30).'),
    # ---- section 4: coverage
    (['S27-M-Q1'], 'V04', 'revised', 'The key and note require explaining that each new part is 1/4 the size of a third, not only the part counts.'),
    (['S43-M-Q3'], 'V05', 'revised', 'Now converts 5 kilometers to meters.'),
    (['S44-M-Q3', 'S44-M-Q4', 'S44-M-Q5'], 'V05', 'revised',
     'Minutes to seconds (Q3) and liters to milliliters (Q4 and the table in Q5).'),
    (['S52-M-Q1', 'S52-M-Q4'], 'V06', 'revised',
     'Visual tasks: two rays with a circle centered at their endpoint and a marked arc (1/6 and 3/8 of the circle); Q1 also asks for the one-degree case.'),
    (['S48-M-Q2', 'S48-M-Q4', 'S48-M-Q5'], 'V02', 'revised', 'S48 is area only: perimeter items moved to S68; Q5 asks only for the area.'),
    (['S48-B2-*'], 'V02', 'retired', 'Moved to S68-B1 (perimeter prerequisite for the new perimeter set).'),
    (['S48-B3-*'], 'V02', 'new', 'Area prerequisite for S48: find area by tiling with unit squares (3.MD.C.7.a).'),
    (['S49-M-Q2', 'S49-M-Q4'], 'V02', 'revised', 'S49 is the unknown side from the area only; perimeter items moved to S69.'),
    (['S49-B1-*'], 'V02', 'retired', 'Moved to S69-B1 (perimeter prerequisite), with each item made one step (B05).'),
    (['S49-B3-*'], 'V02', 'new', 'Area prerequisite for S49: find the area of a rectangle by multiplying its side lengths (3.MD.C.7.b).'),
    (['S58-M-Q4', 'S59-M-Q4', 'S60-M-Q4'], 'V03', 'revised',
     'S58-S60 now identify; their drawing items moved to S70-S72, and each is replaced by an identification item.'),
    # ---- section 5: one skill per section
    (['S6-B2-*'], 'V07', 'revised', 'Branch is subtraction within 1000 only (Q1 and Q3 rewritten as subtraction).'),
    (['S9-F1-Q4'], 'V07', 'revised', 'Rewrite 1/2 and 1/3 with a common denominator (the completed addition is removed).'),
    (['S27-F1-*'], 'V07', 'revised', 'Branch is addition only (Q4 now 5/6 + 1/12).'),
    (['S31-F1-*'], 'V07', 'revised', 'Branch is addition only (Q2 and Q4 rewritten as sums).'),
    (['S32-F1-*'], 'V07', 'revised', 'Branch is mixed-number addition only (Q2 and Q4 rewritten as sums).'),
    (['S35-M-Q2', 'S35-M-Q4', 'S35-M-Q5'], 'V07', 'revised', 'S35 is addition word problems only; subtraction items moved to S66.'),
    (['S35-B1-*'], 'V07', 'revised', 'Branch is addition word problems only; its subtraction items moved to S66-B1.'),
    (['S35-F1-*'], 'V07', 'revised', 'Branch is addition word problems only; its subtraction items moved to S66-F1.'),
    (['S39-M-Q2', 'S39-M-Q3', 'S39-M-Q5'], 'V07', 'revised', 'S39 is tenths as equivalent hundredths only; addition items moved to S67.'),
    (['S39-F2-Q3'], 'V07', 'revised', 'Now writes 3/10 as a percent (the sum was removed).'),
    (['S50-F1-*'], 'V07', 'revised', 'Branch is making line plots of data in halves, fourths, and eighths together; branch title updated.'),
    (['S11-M-Q1'], 'OPT', 'revised', 'Asks which number is neither prime nor composite (1).'),
    # ---- set titles that now name one skill (the skill field of every MAIN question in the set changes)
    (['S35-M-*', 'S39-M-*'], 'V07', 'revised', 'Set title now names its single skill.'),
    (['S48-M-*', 'S49-M-*'], 'V02', 'revised', 'Set title now names its single skill.'),
    (['S58-M-*', 'S59-M-*', 'S60-M-*'], 'V03', 'revised', 'Set title now says "identify"; drawing is assessed in S70-S72.'),
]
