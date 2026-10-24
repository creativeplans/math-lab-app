"""Manual review record for Probability & Statistics 1.0.0, printed into VALIDATION.md by validate.py.

Everything here was done by reading, drawing or computing by the author of this release. It is NOT an automatic check,
and no second person has reviewed it.
"""

READ_THROUGH = (
    'After the build, all 1435 questions were listed in one compact file (question text, choices with the keyed letter, key, '
    'grading note) and the author re-solved every one in set order S1 to S54: computed answers by hand or with Python written '
    'separately from the data modules, every multiple-choice option checked (the keyed choice correct, each other choice wrong '
    'for the reason its note gives), and every true/false statement checked against its note. Simulation keys were recounted '
    'from the printed random digits. Datasets were summarized again (quartiles by the stated rule, population or sample '
    'standard deviation as stated, least-squares coefficients and r from exact fractions). Every short-answer key was run '
    'through the game\'s own answer checker (check 21).'
)

# Errors found while writing or in the read-through, all fixed before release.
FIXES = [
    ('S2 dataset PAGES', 'Two bins tied for the tallest bar, so "which bin has the most values" had two answers; 245 changed to 255.'),
    ('S1-F2-Q5, S2-F2-Q3', 'True/false notes gave a wrong example (five-number summaries; histogram counts); corrected and re-checked.'),
    ('S10 histograms', 'The flat ("uniform") histogram summed to 42, not the stated 40; counts changed to 6, 6, 6, 5, 6, 6, 5.'),
    ('S9-F2-Q2', 'The stem contained an unfinished instruction ("Use these: ..."); rewritten with the table values stated.'),
    ('S23-M-Q4, S23-F1-Q4', 'Line 2 of the digit table contained no red spins and no line had 7 or more heads, which made the '
                            'keys 0; the questions now use line 5 and "3 or fewer heads" (keys 2 and 4).'),
    ('S23-F1-Q1', 'Two choices were correct (00-34 and "01-35 with 00 failure"); choices rewritten so exactly one assignment has '
                  'probability 0.35.'),
    ('S49-F1-Q2', 'The die counts gave an empirical mean of 209/60, not the keyed 3.5; counts changed to 7, 13, 9, 11, 14, 6 '
                  '(210/60 = 3.5).'),
    ('S29-M-Q1', 'The data table printed the two group means, which were the answers; the mean column was removed.'),
    ('S4-B3-Q1, S23-B1-Q1, S24-M-Q2, S6-F2-Q3', 'Grading notes referred to choices by position ("the second", "the last"), which '
                                                'the letter shuffle changes; notes now name the choices by content.'),
    ('S17-M-Q1/Q2', 'Notes mixed the letters of y = a + bx and y = mx + b; now give m and b with exact fractions.'),
    ('S15-F2-Q2, S16-M-Q2, S16-F1-Q1, S3-B2-Q4/Q5', 'Residual and quartile questions did not state the convention on the page; '
                                                     '"observed minus predicted" and "medians of the halves" added (check 24).'),
    ('S29-M-Q2/Q4, S29-B2-Q2, S37-F2-Q5, S52-M-Q2', 'Stems relied on another question ("the 10 results", "the plants") or were '
                                                    'unclear; each now restates its own givens.'),
    ('S40-F2, S46-F2, S47-F2, S49-F2, S50-F2, S51-F2, S52-F2', 'FORWARD 2 questions repeated the next set\'s MAIN questions word for '
                                                               'word; rewritten with new numbers and contexts.'),
    ('S51-M-Q3/Q4, S54-M-Q3/Q4, S16-M-Q5', 'Repeated an earlier branch or another MAIN question in the same set; new numbers '
                                           'and stems.'),
    ('S47-B1-Q5, S54-F1-Q3', 'A true/false item duplicated the one before it; two choices were equivalent ("never guess" and '
                             '"leave every question blank"). Both rewritten.'),
    ('S2-M-Q4', 'The axis sentence added to histogram choices lowercased "°F"; the label is now kept as written.'),
    ('47 multiple-choice items', 'The correct choice was much longer than every other choice; distractors were rewritten '
                                        'with specific errors (check 23 finds no strong length cue).'),
    ('Notes of 8 explanation items', 'Notes of "why" and design items did not say what is wrong with the other choices '
                                      '(checks 5 and 10); added.'),
]

FIGURES = (
    'All 190 question pages that carry a figure (dot plots, histograms, box plots, scatter and residual plots, tables and '
    'random-digit tables, and the four-panel choice figures) were rendered from the question PDF and inspected by eye: data '
    'against the stem (dot counts, bin counts, five-number summaries, plotted points, fitted lines), keyed panel against the '
    'key, panel labels A-D, axis numbers and titles. Fixes after inspection: histogram choice panels were too flat to read '
    '(compact panels with the axis titles moved into the question text; S2-M-Q2/Q4, S10-M-Q1, S46-M-Q3); random-digit tables '
    'were printed in small type (now two side-by-side halves of four lines); box-plot titles overlapped the first box; two '
    'choice rows were split into two columns (S24-F1-Q2, S38-M-Q4). Changed pages were rendered again and inspected.'
)

SIMULATIONS = (
    'Every simulation that students carry out uses the eight lines of random digits printed on the page (DATASETS.md, "S23 '
    'random digits"; generated once and fixed), so each key is a count anyone can repeat. Simulation results described in a '
    'question (for example the 100 simulated sets of 10 coin flips, or "differences of 3 or more occurred 4 times in 200 '
    're-randomizations") are supplied data chosen to be close to the theoretical distribution; they were not produced by a '
    'simulation run, and the questions never ask what a new random run would give.'
)


def markdown(cases, recs):
    ids = [c[0] for c in cases]
    L = ['## Manual review (author)', '',
         '- **Read-through and re-solve of every question:** ' + READ_THROUGH,
         '- **Automatic re-solve (check 17), %d questions:** %s.' % (len(ids), ', '.join(ids)),
         '- **Figures:** ' + FIGURES,
         '- **Simulations:** ' + SIMULATIONS, '',
         '### Errors found and fixed before release', '', '| Question | Problem and fix |', '|---|---|']
    L += ['| %s | %s |' % f for f in FIXES]
    L += ['', 'No second reviewer has checked this collection, and no question has been tried in the live game or with the AI grader.', '']
    return L
