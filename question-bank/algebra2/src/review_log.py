"""Manual review record for Algebra II (1.0.0, 1.1.0 and 1.2.0), printed into VALIDATION.md by validate.py.

Everything here was done by reading, drawing, or computing by the author of this release. It is NOT an automatic check,
and no second person has reviewed it.
"""

READ_THROUGH = (
    'All 2525 questions were listed in one compact file (question text, choices with the keyed letter, key) after the build, '
    'and the author re-solved every one by hand or with a separate calculator script, in set order S1 to S84. Numeric '
    'answers that need technology (logarithms, trigonometric inverses, compound interest, root approximations) were '
    'recomputed with Python written separately from the data modules. Version 1.1.0: the 108 rewritten multiple-choice '
    'items were solved again in their final form; for each, the keyed choice was confirmed correct and every other choice '
    'was confirmed wrong for the reason named in its grading note (computed values were recomputed in Python). '
    'Version 1.2.0: the 910 revised and 30 new questions were solved by the author while rewriting them (computed values, '
    'such as 95/590 ≈ 0.161, 4.318, 14.21 and 3.4, recomputed in Python); every question named in the review\'s '
    'correction report was re-read in its final form. There was no separate second read-through of all 2555 questions in '
    '1.2.0. Every short-answer key was run through the game\'s own answer checker (check 21).'
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
    ('S42-F1-Q2 (1.1.0)', 'The 1.0.0 drawing item asked for a cubic with zeros -1 and 3 only, a positive y-intercept, falling to '
                          'the right and touching the x-axis at 3; no cubic has all of these. Found while redesigning it as '
                          'multiple choice; the condition is now a negative y-intercept (keyed graph y = -(x + 1)(x - 3)²/3).'),
    ('39 proof and explanation choices (1.1.0)', 'In the first multiple-choice draft the correct argument was the longest choice '
                          'in 39 of 53 rewritten items. Distractors were rewritten as fully worded flawed arguments; now 3 of 53 '
                          'have the correct choice longest, each by at most 2 characters.'),
    ('S2-B1-Q1/Q2/Q5, S13-B2-Q2 (1.2.0)', 'The game checker rejected a correct answer written in the other order when the key began '
                          'with a negative constant (key -4 + 7x rejected 7x - 4). Keys are now in standard order (7x - 4), '
                          'which the checker accepts in either order; check 21 now tests reversed term order on every key.'),
    ('Radical, logarithmic and decimal-coefficient expression keys (1.2.0)', 'The checker compared keys such as 3 - √x, '
                          '(A/P)^(1/t) - 1 and 20 - 1.95t only as text, so an equivalent rewrite (√x written as sqrt(x), terms '
                          'reordered) was marked wrong. These items are now multiple choice or ask for numeric parameters.'),
    ('S16-M-Q1/Q2/Q3 (1.2.0)', 'A numeric answer line (p(2) = 0) next to a factored line failed, because the checker applies '
                          '"factor" to every line of a question. The check value now appears in the question.'),
    ('S25-B2-Q1 (1.2.0)', 'Two answers shared one answer line; now one line each.'),
    ('37 unchanged multiple-choice items (1.2.0)', 'Adding new multiple-choice items moved the letters of 37 unchanged 1.1.0 items. '
                          'Their 1.1.0 letters were restored, and every current letter is now frozen in choice_plan.json.'),
    ('146 multiple-choice items (1.2.0)', 'The correct choice was much longer than every other choice in 146 items (and the '
                          'uniquely longest in 40% of text items). Distractors were rewritten with specific errors; check 23 '
                          'now finds no strong length cue, and the correct choice is the uniquely longest in 33% (25% is chance).'),
]

FIGURES = (
    'All 106 question pages that carry a figure (78 coordinate graphs or grids, 15 histograms, 13 tables) were rendered from the '
    'question PDF and inspected by eye: curves against their equations (intercepts, asymptotes, extrema), dashed asymptotes and '
    'midlines, open circles at holes, labels, and axis numbers. Fixes after inspection: crowded axis numbers on S43-M-Q3/Q5, '
    'S46-M-Q4/Q5, S46-F1-Q1, S51-M-Q4, S53-M-Q2/Q5, S74-M-Q3/Q5, S78-M-Q4 (label spacing); axis titles overlapping 4- and 5-digit '
    'numbers on S28-M-Q1/Q4 (rescaled: rabbits 5·2ᵗ; car value in thousands of dollars); S28-M-Q5 x spacing; long histogram axis '
    'title on the re-randomization figures; a mid-factor line break in S18-M-Q4. The changed pages were rendered again and inspected. '
    'Version 1.1.0: all 55 four-graph figures (graphing items now multiple choice) were rendered and inspected: each panel '
    'against its own equation (zeros, multiplicity, asymptotes, holes, open and closed endpoints, period, midline, title), '
    'the keyed panel against the question, and the labels A-D. Layout fixes after inspection: panel letters moved out of the '
    'grid, axis numbers spaced out, choices on one line, axis names removed from the titled S28 panels. Version 1.2.0: the five '
    'step-function figures of S85-M (pages 1754-1758) were rendered and inspected: step heights, step widths, open and closed '
    'endpoints of every panel, the keyed panel against the question, and the ⌊ ⌋ and ⌈ ⌉ symbols in the text. Figures '
    'of other changed questions were reused unchanged.'
)

PROOFS = (
    'In 1.0.0 the 53 shown-work questions were checked step by step against their rubrics. Since 1.1.0 they are multiple '
    'choice: derivation steps (S11), the Fundamental Theorem of Algebra arguments (S6), the Remainder Theorem proof '
    '(S15-F2-Q1), identity proofs (S19, S40), polynomial divisions (S22), unit-circle explanations (S37, S82), composition '
    'verifications (S77), special-triangle derivations (S81), and the even/odd proofs (S57-F1). For each, the keyed argument was '
    'read step by step (it uses no result that depends on the claim), and each other choice was checked to contain the flaw '
    'its note names (an example check, an invalid step, circular reasoning, a false fact).'
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
         '- **Former shown-work items:** ' + PROOFS,
         '- **Figures:** ' + FIGURES,
         '- **Simulations:** ' + SIMULATIONS, '',
         '### Errors found and fixed before release', '', '| Question | Problem and fix |', '|---|---|']
    L += ['| %s | %s |' % f for f in FIXES]
    L += ['', 'No second reviewer has checked this collection, and no question has been tried in the live game or with the AI grader.', '']
    return L
