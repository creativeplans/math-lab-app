# Logic collection: validation report

Collection LOGIC version 1.0.0 (2026-10-25). 54 sets, 1170 questions, 108 figures.

Question types: grid 25, mark 22, mc 397, order 39, sa 234, tf 335, truth_table 23, values 95.

Questions whose key was confirmed by code during the build (enumeration, search, a check function or a recomputed answer): 747 of 1170. The rest (mostly reading, fallacy and argument questions) were solved by the author, and every wrong choice carries a written reason.

## Required checks

| Check | Result | Detail |
|---|---|---|
| Every section (MAIN, each backward branch, FORWARD 1, FORWARD 2) has exactly 5 questions | PASS | 234 sections checked; wrong sizes: none |
| Every set has MAIN, at least one backward branch, FORWARD 1 and FORWARD 2 | PASS | 54 sets; missing parts: none |
| Every backward branch is guided_strategy or prerequisite | PASS | {'guided_strategy': 150, 'prerequisite': 210} |
| Every guided-strategy branch has a lesson with a worked example | PASS | all present |
| At least half of the MAIN sets are puzzles | PASS | 27 puzzle, 27 formal |
| Set 1 is a puzzle and at least 6 of the first 10 sets are puzzles | PASS | 6 of the first 10 |
| Never more than 2 formal sets in a row | PASS | longest formal run: 2 |
| At least 10 puzzle genres | PASS | 27 genres |
| Direct standard alignment only on HSA-REI.A.1 (set 39) and HSG-CO.C.9 (set 43) | PASS | [(39, 'HSA-REI.A.1'), (43, 'HSG-CO.C.9')] |
| Supporting practices are only MP1, MP2, MP3, MP6, MP7, MP8 | PASS | all valid |
| Every multiple-choice question has 4 different choices | PASS | 397 checked; problems: none |
| Every multiple-choice key letter is one of its choices | PASS | all valid |
| Multiple-choice key letters are balanced (largest minus smallest count at most 4% of MC items) | PASS | {'A': 100, 'B': 99, 'C': 99, 'D': 99} |
| True/false answers are balanced (within 10%) | PASS | True 180, False 155 |
| No placeholder or unfinished text in prompts, choices, solutions or wrong-choice reasons | PASS | none |
| Every question stands alone (no reference to another question or "the puzzle above") | PASS | none |
| No two questions have the same prompt | PASS | none |
| Lesson worked examples are different from every scored question | PASS | none |
| Every question has a written solution | PASS | all present |
| Every wrong multiple-choice option has a reason it is wrong | PASS | all present |
| The import package has one set file per set | PASS | 54 files |
| Every figure file exists and has a text description | PASS | 108 figures; problems: none |
| All figures are grayscale | PASS | all grayscale |

## Balance and style checks

| Check | Result | Detail |
|---|---|---|
| No run of 4 or more identical key letters in collection order | PASS | 0 runs |
| No section has 3 identical key letters in a row | PASS | none |
| Length cue: the key is the unique longest choice in at most 40% of text multiple-choice items | PASS | 126 of 388 (32%; 25% would be chance) |

## What the build itself verified

- Every ordering question: all orderings of its items were enumerated; every valid ordering is accepted.
- Every grid question: all assignments were enumerated; puzzles marked unique have exactly one solution.
- Every truth table and Venn diagram: each cell or region was computed from the formula or condition.
- Every rule-checked answer (values): the example passes the rule and the listed tempting mistakes fail it; where a finite domain is stated, every valid answer in it was counted.
- Multiple-choice items with a check function: the function accepts the keyed choice and rejects all others.
- Short answers with a compute function: the key was recomputed by code.

The game-side checks (tools/game_checks.ts, which runs every key and wrong answer through the game's own response checkers) and the importer check are reported in the README.
