# Logic: High School Logic and Reasoning Puzzles

Untangle The Nexus question collection `LOGIC`, version 1.0.0 (2026-10-25). 54 sets, 1170 questions, 108 figure
files. Generated from `question-bank/logic/src` (plan.py and data_*.py) by build.py, validate.py and report.py.
Regenerate there rather than editing these files by hand.

## What is in this collection

- 54 sets in a fixed order: 27 puzzle sets and 27 formal-logic sets. Set 1 is a puzzle, 6 of the first 10 sets
  are puzzles, and there are never more than 2 formal sets in a row.
- Every set: MAIN (5 questions), at least one backward branch (a guided-strategy lesson with a worked example of a
  different puzzle and 5 practice problems, or a 5-question prerequisite check), FORWARD 1 (advanced application,
  5 questions) and FORWARD 2 (expert challenge, 5 questions).
- Each question states its own conventions and supplies any word list it needs. Figures are exact grayscale SVG drawings
  with a text description.
- Outcomes are local (listed in `index.json`). Sets 39 (HSA-REI.A.1) and 43 (HSG-CO.C.9) align directly to a Common
  Core standard; Standards for Mathematical Practice MP1, MP2, MP3, MP6, MP7 and MP8 are listed as supporting practices.

## Files

| Path | Contents |
|---|---|
| `index.json` | Collection id and version, every outcome, the practices, and every set with its file |
| `sets/Sxx.json` | One file per set: sections (M, B1..., F1, F2) with relation, skill, branch mode, lesson and 5 questions each |
| `assets/*.svg` | Figures, referenced by the questions that use them |
| `COVERAGE.md` | Every set with kind, genre, outcome, practices, standard and branches; the structure rules; question types |
| `SOURCE_MAP.md` | Each deck puzzle genre and the sets that teach it (all questions are original) |
| `VALIDATION.md` | Every validation check and its result |
| `pdf/` | The question collection and the answer key in 3 parts each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

## Question types and how they are graded

All 1170 questions are graded automatically by the game:

- multiple choice (`mc`): 397
- true/false (`tf`): 335
- short answer (`sa`): 234
- answer checked by a rule (`values`): 95
- put in order (`order`): 39
- logic grid (`grid`): 25
- truth table (`truth_table`): 23
- mark cells or regions (`mark`): 22

Multiple choice and true/false compare letters. Ordering, logic-grid, truth-table and mark questions are checked by the
game against every accepted answer. Rule-checked answers (`values`) are checked by the game's rule language, so any
answer that meets the rule is accepted, not only the example. Short answers are checked by the game's answer evaluator
against `correct_answer`.

## Checks run for this version

- Validator (src/validate.py): 23 required checks, all PASS; 3 balance and style checks, all PASS. Details in VALIDATION.md.
- Game importer, check-only mode (tools/import-collection/import.ts --check): 54 sets, 1170 questions, 0 invalid, 0 warnings: "the bank is valid".
- Game response checks (src/tools/game_checks.ts, using the game's own response checkers): 204 interactive questions (order, grid, truth table, mark, values), 617 keyed and wrong responses, 0 problems.
- Build-time solvers: every ordering and grid enumerated, every truth table and Venn region computed, every rule-checked answer tested with its example and listed mistakes, and every check or compute function re-run on each build.

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 written questions. Nothing is generated at play time, so a student who
  repeats a section sees the same questions.
- Questions about arguments, fallacies, assumptions and evidence were solved by the author; they have no computer
  check, but every wrong choice has a written reason.
