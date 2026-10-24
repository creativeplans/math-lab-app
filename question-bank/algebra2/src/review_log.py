"""Manual review record for Algebra II 1.0.0, printed into VALIDATION.md by validate.py.

Everything here was done by reading, drawing, or computing by the author of this release. It is NOT an automatic check,
and no second person has reviewed it.
"""

READ_THROUGH = (
    'All 2525 questions were listed in one compact file (question text, choices with the keyed letter, key) after the build, '
    'and the author re-solved every one by hand or with a separate calculator script, in set order S1 to S84. Numeric '
    'answers that need technology (logarithms, trigonometric inverses, compound interest, root approximations) were '
    'recomputed with Python written separately from the data modules.'
)

# Errors found while writing or in the read-through, all fixed before release.
FIXES = [
    ('S12-F1-Q1', 'Key gave too few deposits; recomputed: 68 deposits (67 give $19,838.70, 68 give $20,187.89).'),
    ('S12-F2-Q2', 'Comparison values recomputed (16,875.11 and 18,725.12) and the month corrected.'),
    ('S18-F2-Q5', 'Stated y-intercept (-4) contradicted the end behavior; changed to 4 so 2(x + 2)(x - 1)² fits all conditions.'),
    ('S21-F1-Q4', 'Keyed option was +10x⁴; the correct term is -10x⁴. Options reordered so the correct one is keyed.'),
    ('S22-F1-Q1', 'Key a = -1 was wrong for the original dividend; dividend changed to x³ + ax² + 2x + 4 (a = -2, remainder 5) and re-checked.'),
    ('S26-F1-Q5', 'Grading note contained an abandoned calculation; replaced with the correct equation x² - 2.8x - 4.8 = 0.'),
    ('S45-F2-Q4', 'Keyed option said the rates were equal; h has rate 20 and k has rate 10, so "a greater rate for h" is keyed.'),
    ('S45-B2-Q4', 'A distractor (24/72) was equal to the key (1/3); replaced with 72/24.'),
    ('S48-F2-Q2', 'Profit interval key used rounded endpoints inconsistently; restated with exact endpoints (9 ± √21)/2.'),
    ('S60-F1-Q4/Q5', 'Unfinished note and an unclear stem rewritten.'),
    ('S64-B2-Q2', 'Key described an unworkable digit scheme; stem now uses two-digit numbers 00-99 (00-24 = red).'),
    ('S74-F1-Q3', 'Note contained a wrong example; replaced with y = x/(x² + 1).'),
    ('S75-F2-Q5', 'Key -5 was wrong; (x + 3)/(x + 1) = 2 gives x = 1, which is allowed.'),
    ('71 branch and MAIN items', 'Stems that relied on another question ("this branch", "the same model", "the depth table", '
                                 '"the diet experiment" and similar) were rewritten to restate their own givens (validation check 16 '
                                 'and a wider phrase search; examples S7-F1-Q5, S12-F2-Q2, S43-B2-Q1, S61-M-Q2, S66-F2-Q1, S78-B2-Q1).'),
    ('127 true/false items', 'The first draft had 334 True and 90 False keys. 127 true statements were rewritten as false '
                             'statements, each with a grading note that gives the correct fact (now 207 True, 217 False).'),
    ('S74-B1-Q5', 'The game importer (check mode) rejected the key 2x/((x - 2)(x + 2)) under "Form required: factored"; '
                  'the item now asks to factor the denominator x² - 4.'),
]

FIGURES = (
    'All 106 question pages that carry a figure (78 coordinate graphs or grids, 15 histograms, 13 tables) were rendered from the '
    'question PDF and inspected by eye: curves against their equations (intercepts, asymptotes, extrema), dashed asymptotes and '
    'midlines, open circles at holes, labels, and axis numbers. Fixes after inspection: crowded axis numbers on S43-M-Q3/Q5, '
    'S46-M-Q4/Q5, S46-F1-Q1, S51-M-Q4, S53-M-Q2/Q5, S74-M-Q3/Q5, S78-M-Q4 (label spacing); axis titles overlapping 4- and 5-digit '
    'numbers on S28-M-Q1/Q4 (rescaled: rabbits 5·2ᵗ; car value in thousands of dollars); S28-M-Q5 x spacing; long histogram axis '
    'title on the re-randomization figures; a mid-factor line break in S18-M-Q4. The changed pages were rendered again and inspected.'
)

PROOFS = (
    'All 53 work (shown-work) questions were checked step by step against their rubrics: derivations (S11), the Fundamental '
    'Theorem of Algebra arguments (S6), the Remainder Theorem proof (S15-F2-Q1), identity proofs (S19, S40), polynomial divisions '
    '(S22), unit-circle explanations (S37, S82), composition verifications (S77), special-triangle derivations (S81), and the '
    'even/odd proofs (S57-F1). Each rubric lists the essential steps; the derivations use no result that depends on the claim.'
)

SIMULATIONS = (
    'The histograms of S64 (model consistency), S67 (sample proportions), S68 (resampled means) and S69 (re-randomized '
    'differences) were produced by the seeded script algebra2/src/simulations.py; the counts in the figures and keys were copied '
    'from its output and re-read. Other simulation summaries stated in text (for example "62 of 200 re-randomizations") are '
    'supplied data chosen to be plausible; they were not produced by a simulation run.'
)


def markdown(cases, recs):
    ids = [c[0] for c in cases]
    L = ['## Manual review (author)', '',
         '- **Read-through and re-solve of every question:** ' + READ_THROUGH,
         '- **Automatic re-solve (check 17), %d questions:** %s.' % (len(ids), ', '.join(ids)),
         '- **Shown-work items:** ' + PROOFS,
         '- **Figures:** ' + FIGURES,
         '- **Simulations:** ' + SIMULATIONS, '',
         '### Errors found and fixed before release', '', '| Question | Problem and fix |', '|---|---|']
    L += ['| %s | %s |' % f for f in FIXES]
    L += ['', 'No second reviewer has checked this collection, and no question has been tried in the live game or with the AI grader.', '']
    return L
