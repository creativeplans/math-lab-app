"""Grade 7 revision 2.0.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is
    (ID patterns, finding code, status, reason)
status: 'revised' (ID kept), 'retired' (ID removed, never reused), 'new', or 'layout'.
Finding codes are those of Grade7_Complete_Review.md.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'b0a5f7a'

FINDINGS = {
    'C01': 'Maximum percent error: the actual length is now stated, so 0.5% is exact (S11-F2-Q3)',
    'C02': 'Battery drops by percentage points of full capacity, a linear change (S20-F2-Q1)',
    'C03': 'Slant height asks about a RIGHT square pyramid (S48-F1-Q3)',
    'C04': 'The parallelogram cut is perpendicular to the base, and the slide is described (S43-B1-Q3)',
    'C05': 'The coin is "claimed to be fair," so doubt about the model is a valid answer (S58-M-Q2)',
    'C06': 'Treatment questions state random assignment and a no-effect simulation; the key gives evidence, not proof (S61-F2-Q1/Q2)',
    'C07': 'Overlap questions show paired dot plots whose means and MADs were verified (S52-M)',
    'C08': 'Write-and-solve questions require both a valid equation (or inequality) and its solution',
    'C09': 'Equations with two roots require both roots (S32-F2-Q1/Q2, S43-F1-Q1)',
    'C10': 'Exact or rounded answers are stated explicitly (S29-M-Q2, S53-F2-Q2)',
    'C11': 'Fair devices, numbered cubes, independent trials, and P(B) > 0 are stated',
    'C12': 'Formula rearrangements state nonzero divisors; the square-root item states x ≥ 0',
    'C13': 'Different triangles means noncongruent; slicing planes cut through the solid\'s interior',
    'B01': 'Earlier-grade fractions (and distractors) use their grade\'s denominators (S56-B1, S56-B2, S61-B2)',
    'B02': 'Grade 4 branch checks answers to two-step word problems by rounding (S30-B2)',
    'B03': 'Unit-fraction division items are word problems (S22-B2-Q4/Q5)',
    'B04': 'Combination counts are built on arrays with one row per first choice (S59-B2)',
    'B05': 'New numerical addition-property branch: regroup addends within 100 (S18-B3)',
    'F01': 'Grade 8 equation branches use variables on both sides and rational coefficients (S9-F1, S20-F1, S23-F1)',
    'F02': 'Grade 8 branch applies the properties of integer exponents with negative bases (S19-F1)',
    'F03': 'High-school equation branches: justified chains, invalid steps, and letter coefficients (S12-F2, S14-F2, S33-F2)',
    'F04': 'Expression-interpretation branch interprets terms and factors in context (S26-F2)',
    'F05': 'Growth-factor branch is percent growth only; the quadratic items were removed (S28-F2)',
    'F06': 'Modeling branch defines the quantities a model needs (S30-F2-Q1/Q2)',
    'F07': 'Construction branch performs actual compass-and-straightedge constructions (S38-F2)',
    'F08': 'Congruence branch explains the criteria with rigid motions (S39-F2)',
    'F09': 'Proof branches ask for justified chains of reasoning (S44-F2, S45-F2)',
    'F10': 'Event branch uses unions, intersections, and complements of overlapping events (S54-F2)',
    'F11': 'Two-way-table branches have students fill in blank tables (S57-F1, S60-F1)',
    'F12': 'Model-consistency branch judges results against a simulated distribution (S58-F2)',
    'F13': 'Forward branches strengthened (S2-F2, S4-F2, S25-F2, S46-F2, S56-F1)',
    'F14': 'Circle forward branches add a derivation item (S41-F2-Q4, S42-F2-Q4)',
    'V01': 'Focused sets: markup/markdown (S9), simple interest (S10), tips (S62), tax (S63), commissions (S64), fees (S65), combined (S66)',
    'V02': 'Scale-reproduction (S37) and triangle-drawing (S38) sets are all actual drawings',
    'V03': 'Signed-fraction addition (S13, S15) and division in context (S22)',
    'V04': 'Properties applied to subtraction (S18) and division (S23)',
    'V05': 'S33 asks for an arithmetic solution, an algebraic solution, and a comparison of the steps',
    'V06': 'S34 is five inequality word problems; S35 is five graph-and-interpret problems in context',
    'V07': 'Angle sets write and solve equations from labeled figures (S44, S45)',
    'V08': 'New composite-prism sets: volume (S67) and exterior surface area (S68)',
    'V09': 'New sets in which students generate random samples (S69) and collect chance data (S70)',
    'V10': 'S60 has students produce lists, tables, and tree diagrams of sample spaces',
    'V11': 'S61 runs simulations with given random digits, alongside a design task',
    'V12': 'Items that drifted from their set\'s skill were rewritten (S2-M-Q4, S7-M-Q1/Q4, S46-M-Q3, S58-M-Q1)',
    'V13': 'Population comparisons use both center and spread (S53-M)',
    'V14': 'S43 asks for the complete wedge argument, with a diagram of the rearranged wedges',
    'D01': 'High-school standards are labeled as this bank\'s Grade 9 placement, not an official grade (standard_level field, README)',
    'D02': 'Coverage and README describe the performances actually tested; CORRECTIONS.md and revisions.json are included',
}

# old ID -> new ID for questions that moved unchanged to a new focused set (the old ID now holds a new question
# for its set's narrower skill)
MOVES = [
    ('S9-M-Q1', 'S62-M-Q1'), ('S9-M-Q5', 'S63-M-Q5'), ('S10-M-Q2', 'S64-M-Q1'),
    ('S10-M-Q3', 'S65-M-Q1'), ('S10-M-Q5', 'S65-M-Q5'), ('S9-M-Q2', 'S66-M-Q1'),
]
MOVE_FINDING = {'S62': 'V01', 'S63': 'V01', 'S64': 'V01', 'S65': 'V01', 'S66': 'V01'}

NEW_SETS = {
    'S62': ('V01', '7.RP.A.3 — find a tip and the total cost with the tip.'),
    'S63': ('V01', '7.RP.A.3 — find sales tax and the final cost with tax.'),
    'S64': ('V01', '7.RP.A.3 — find a commission and pay that includes a commission.'),
    'S65': ('V01', '7.RP.A.3 — find a percent fee and the total with the fee.'),
    'S66': ('V01', '7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip.'),
    'S67': ('V08', '7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams.'),
    'S68': ('V08', '7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted).'),
    'S69': ('V09', '7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary.'),
    'S70': ('V09', '7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student\'s own rolls) and estimate a probability.'),
}


def _moves():
    return [([new], MOVE_FINDING[new.split('-')[0]], 'new', 'Moved unchanged from %s.' % old) for old, new in MOVES]


def _new_sets():
    return [([s + '-*'], code, 'new', 'New focused set: ' + text) for s, (code, text) in NEW_SETS.items()]


CHANGES = _moves() + _new_sets() + [
    # ---- content and grading
    (['S11-F2-Q3'], 'C01', 'revised', 'States that the actual length is 400 m and the measurement is off by at most 2 m, so the greatest percent error is exactly 0.5%.'),
    (['S20-F2-Q1'], 'C02', 'revised', 'The battery drops by 6 percentage points of its full capacity each hour; the equation 90 - 6h = 30 is unchanged.'),
    (['S48-F1-Q3'], 'C03', 'revised', 'Says the pyramid is a right square pyramid with its top vertex above the center of the base; still 5 m.'),
    (['S43-B1-Q3'], 'C04', 'revised', 'The cut runs from a top corner straight down to the base at a right angle, and the triangle slides to the other end; the answer is a rectangle.'),
    (['S58-M-Q2'], 'C05', 'revised', 'The coin is claimed to be fair, so chance variation or an unfair coin are both valid explanations.'),
    (['S61-F2-Q1', 'S61-F2-Q2'], 'C06', 'revised',
     'States that similar plants were randomly assigned to plant food or none and that the re-randomizations simulate no effect; the key says evidence, not proof.'),
    (['S52-M-*'], 'C07', 'revised',
     'Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified.'),
    (['S7-F2-Q1', 'S7-F2-Q2', 'S20-F2-Q1', 'S20-F2-Q2', 'S31-M-Q1', 'S32-M-Q1', 'S34-M-Q1', 'S44-M-Q2'], 'C08', 'revised',
     'The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted.'),
    (['S32-F2-Q1', 'S32-F2-Q2', 'S43-F1-Q1'], 'C09', 'revised', 'Asks for all solutions; the key lists both roots and says both are required (either order or set notation).'),
    (['S29-M-Q2'], 'C10', 'revised', 'Exact answer 1 11/12 feet (or 23/12); a rounded decimal is no longer listed as correct.'),
    (['S53-F2-Q2'], 'C10', 'revised', 'Says to round a mean that does not end to the nearest tenth: 11.2 and 5.4; exact 67/6 and 27/5 accepted.'),
    (['S55-M-Q4', 'S56-M-Q1', 'S56-F2-Q3', 'S59-M-*', 'S59-F2-Q2', 'S59-F2-Q3', 'S60-F2-Q2', 'S60-F2-Q3', 'S61-M-Q1', 'S61-M-Q3'], 'C11', 'revised',
     'States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials.'),
    (['S60-F2-Q4'], 'C11', 'revised', 'States P(B) > 0 for the conditional-probability rule.'),
    (['S31-F2-Q2', 'S31-F2-Q3', 'S31-F2-Q4', 'S23-F2-Q2'], 'C12', 'revised', 'States m ≠ 0, b > 0, r > 0, or real x ≥ 0 as needed.'),
    (['S39-M-Q1', 'S39-M-Q2', 'S39-M-Q3', 'S39-M-Q5'], 'C13', 'revised', 'Defines different triangles as noncongruent triangles; position and orientation do not matter.'),
    (['S40-M-Q2', 'S40-M-Q4', 'S40-F2-Q1', 'S40-F2-Q2', 'S40-F2-Q3'], 'C13', 'revised',
     'Each plane cuts through the solid\'s interior (strictly between base and apex; through the axis of a right circular cone).'),
    # ---- backward branches
    (['S56-B1-Q2'], 'B01', 'revised', 'Uses 8/12 (Grade 4 denominators) instead of 10/15; still 2/3.'),
    (['S56-B2-Q3'], 'B01', 'revised', 'The distractor 3/7 is now 3/6 (Grade 3 denominators).'),
    (['S56-B2-Q4'], 'B01', 'revised', 'One of 6 equal parts is 1/6 (Grade 3 denominators); still True.'),
    (['S61-B2-Q5'], 'B01', 'revised', 'Compares 3/8 and 4/8 (Grade 3 denominators); still False.'),
    (['S30-B2-*'], 'B02', 'revised', 'Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated.'),
    (['S22-B2-Q4', 'S22-B2-Q5'], 'B03', 'revised', 'The same divisions are now word problems (1/5-pound bags; sharing 1/8 pound).'),
    (['S59-B2-*'], 'B04', 'revised', 'Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated.'),
    (['S18-B3-*'], 'B05', 'new', 'New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch.'),
    # ---- forward branches
    (['S9-F1-*', 'S20-F1-*', 'S23-F1-*'], 'F01', 'revised', 'Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated.'),
    (['S19-F1-*'], 'F02', 'revised', 'Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated.'),
    (['S12-F2-*', 'S33-F2-*'], 'F03', 'revised', 'A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated.'),
    (['S14-F2-*'], 'F03', 'revised', 'Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated.'),
    (['S26-F2-*'], 'F04', 'revised', 'Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated.'),
    (['S28-F2-*'], 'F05', 'revised', 'All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated.'),
    (['S30-F2-Q1', 'S30-F2-Q2'], 'F06', 'revised', 'Students name the quantities and units a model needs instead of computing or naming a unit.'),
    (['S38-F2-Q1', 'S38-F2-Q2', 'S38-F2-Q3', 'S38-F2-Q4'], 'F07', 'revised',
     'Actual constructions on a given segment or angle: perpendicular bisector, equilateral triangle, angle bisector, and copying a segment.'),
    (['S38-F2-Q5'], 'F07', 'revised', 'Says "in a compass-and-straightedge construction"; still False.'),
    (['S39-F2-*'], 'F08', 'revised', 'Explains SAS, SSS, and ASA by following rigid motions; branch title updated.'),
    (['S44-F2-*'], 'F09', 'revised', 'Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated.'),
    (['S45-F2-Q2', 'S45-F2-Q3', 'S45-F2-Q4', 'S45-F2-Q5'], 'F09', 'revised', 'Proofs with reasons that vertical angles are congruent, built from linear pairs.'),
    (['S54-F2-*'], 'F10', 'revised', 'Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated.'),
    (['S57-F1-*', 'S60-F1-*'], 'F11', 'revised', 'Students fill in a blank two-way table from survey counts (five constructions); branch title updated.'),
    (['S58-F2-*'], 'F12', 'revised', 'Results are judged against a dot plot of 50 simulated results under the model; branch title updated.'),
    (['S2-F2-*'], 'F13', 'revised', 'Tells equal differences from equal factors with evidence from tables; branch title updated.'),
    (['S4-F2-*'], 'F13', 'revised', 'Constructs functions from two input-output pairs, a sequence, or a description; branch title updated.'),
    (['S25-F2-Q1', 'S25-F2-Q2', 'S25-F2-Q3'], 'F13', 'revised', 'Units are carried through each step of a multistep rate problem.'),
    (['S46-F2-Q1', 'S46-F2-Q3', 'S46-F2-Q4', 'S46-F2-Q5'], 'F13', 'revised', 'Modeling items estimate with a model and judge whether the model fits.'),
    (['S56-F1-*'], 'F13', 'revised', 'Uses a probability model as a function from outcomes to probabilities; branch title updated.'),
    (['S41-F2-Q4', 'S42-F2-Q4'], 'F14', 'revised', 'Explain why an arc length or sector area is n/360 of the whole circle\'s circumference or area.'),
    # ---- coverage and focus
    (['S9-M-*'], 'V01', 'revised', 'S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66.'),
    (['S10-M-*'], 'V01', 'revised', 'S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65.'),
    (['S10-F1-Q2', 'S10-F1-Q5'], 'V01', 'revised', 'Models an interest-bearing loan instead of a commission, to match the simple-interest set.'),
    (['S37-M-Q1', 'S37-M-Q3', 'S37-M-Q4', 'S37-M-Q5'], 'V02', 'revised', 'An actual redrawing at a new scale on the grid, so all five items reproduce a scale drawing.'),
    (['S38-M-Q3', 'S38-M-Q5'], 'V02', 'revised', 'An actual triangle drawing on the grid; triangle existence stays in S39.'),
    (['S13-M-Q2', 'S13-M-Q5', 'S15-M-Q2', 'S15-M-Q4'], 'V03', 'revised', 'Adds signed fractions and mixed numbers (on a number line or in context).'),
    (['S22-M-Q1', 'S22-M-Q3', 'S22-M-Q5'], 'V03', 'revised', 'Divides signed fractions and mixed numbers in context.'),
    (['S18-M-Q2'], 'V04', 'revised', 'Rewrites subtraction as adding the opposite, then regroups (required work).'),
    (['S23-M-Q2', 'S23-M-Q5'], 'V04', 'revised', 'Rewrites division as multiplying by a reciprocal; shows that division itself is not associative.'),
    (['S33-M-*'], 'V05', 'revised', 'Arithmetic and algebraic solutions of the same problem, with the steps compared.'),
    (['S34-M-Q2', 'S34-M-Q3', 'S34-M-Q4', 'S34-M-Q5'], 'V06', 'revised', 'An inequality word problem with a solution stated in context.'),
    (['S34-M-Q1'], 'V06', 'revised', 'The solution is stated as whole numbers of pairs from 0 to 8.'),
    (['S35-M-*'], 'V06', 'revised', 'Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count).'),
    (['S44-M-Q1', 'S44-M-Q2', 'S44-M-Q4', 'S44-M-Q5'], 'V07', 'revised', 'Writes and solves an equation from a labeled angle figure.'),
    (['S45-M-Q2', 'S45-M-Q3', 'S45-M-Q4', 'S45-M-Q5'], 'V07', 'revised', 'Writes and solves an equation from a labeled figure of intersecting lines.'),
    (['S60-M-Q2', 'S60-M-Q3', 'S60-M-Q4', 'S60-M-Q5'], 'V10', 'revised', 'Students make a complete organized list, tree diagram, or table, and identify an event in it.'),
    (['S61-M-Q2', 'S61-M-Q4', 'S61-M-Q5'], 'V11', 'revised', 'Runs a simulation with given random digits: group the digits into trials, count successes, and estimate the probability.'),
    (['S2-M-Q4'], 'V12', 'revised', 'Decides whether the table is proportional, with ratio evidence, instead of filling in values.'),
    (['S7-M-Q1', 'S7-M-Q4'], 'V12', 'revised', 'A genuinely multistep ratio problem (three-part ratio; map distance then travel time).'),
    (['S46-M-Q3'], 'V12', 'revised', 'A composite rectangle-and-triangle area replaces a single trapezoid.'),
    (['S58-M-Q1'], 'V12', 'revised', 'Gives an observed count (14 fives) and asks for the comparison with the expected 10.'),
    (['S53-M-Q1', 'S53-M-Q2', 'S53-M-Q4', 'S53-M-Q5'], 'V13', 'revised', 'Draws a population inference from both center and spread, stated as a tendency.'),
    (['S43-M-Q1', 'S43-M-Q2'], 'V14', 'revised', 'Shows the circle cut into wedges and rearranged; Q2 asks for the complete argument that the area is πr².'),
]
