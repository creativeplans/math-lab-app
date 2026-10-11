# Grade 7 Common Core Math — Question Collection (version 2.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade7_Question_Collection.pdf` | The questions, one per page (2,182 pages) |
| `Grade7_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade7_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G7:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 7 requirement, the set that focuses on it, and the performance its MAIN questions test |
| `CHANGELOG.md` | Every change since version 1.0.0, keyed by question ID, with the old → new ID map |
| `CORRECTIONS.md` | Checklist of every Grade 7 review finding code with the question IDs it changed |

The Untangle The Nexus import package is `question-bank/nexus/grade7/` (it includes `revisions.json`, `CHANGELOG.md`,
`CORRECTIONS.md`, and `COVERAGE.md`), also zipped as `question-bank/nexus/Grade7_Nexus_Import_v2.0.0.zip`.

- 70 focused question sets (1,755 questions) covering every Grade 7 standard code (all 37 lettered and unlettered
  standards, plus 7.SP.C.7 as a whole). `COVERAGE.md` lists the performance each set's MAIN questions actually test.
- Each set: MAIN (Grade 7, 5 variations), backward branches (Grade 6 or earlier only; most sets have two, S18 has
  three), FORWARD 1 (Grade 8), and FORWARD 2 (high school).
- **FORWARD 2 uses Common Core high-school standards** (Algebra, Functions, Geometry, Number & Quantity, and
  Statistics & Probability codes such as `HSA-REI.B.3`, `HSG-CO.C.9`, `HSF-LE.A.1.c`, `HSS-CP.A.4`). Common Core does
  not assign these standards to a grade; this bank places them at Grade 9 as an instructional choice. The PDFs label
  them "High School (Grade 9 in this bank)", the import package's `standard_grade` is 9, and every high-school record
  there has a `standard_level` field that says so. Advanced statistics branches are scaffolded with given
  simulations and margins.
- 21 FORWARD 1 branches are marked "NEAREST RELATED": Grade 8 has no standard that directly continues the skill (for
  example percent change, inequalities, surface area, sampling, and probability). The note names Grade 8, and the
  branch uses the closest Grade 8 standard.
- Drawing, construction, sampling, data collection, and simulation are done, not just described: scale redrawings and
  triangle drawings on grids (S37, S38), inequality graphs in context (S35), sample-space lists, tables, and tree
  diagrams (S60), simulations run with given random digits (S61), random samples generated with random digits (S69),
  chance data collected (S70), compass-and-straightedge constructions (S38-F2), and two-way tables filled in from
  survey counts (S57-F1, S60-F1).
- Grading rules: write-and-solve questions require both a valid equation (or inequality) and its solution; equations
  with two roots require both; proofs require reasons; exact or rounded answers are stated in the question; drawing
  answers accept any correct drawing; work answers accept any valid method; a student's own experimental data is
  graded on the recording and the calculation, not on a preset result.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer (`plot_text`,
  both parts graded), and answer with required work (`work`). Figures include number lines and inequality graphs,
  coordinate grids, ratio and two-way tables (some blank to fill in), circles, a circle cut into wedges and
  rearranged, spinners, angle figures with labeled expressions, parallel lines cut by a transversal, composite
  figures, prisms and solids made of prisms, paired dot plots, simulation dot plots, box plots, and bar graphs.
- True/false: 339 true, 341 false. Multiple choice: A 86, B 85, C 88, D 86.

## Version 2.0.0

Applies every finding of the Grade 7 review (C01–C13, B01–B05, F01–F14, V01–V14, D01–D02: 39 required and 9
recommended); none was deferred (see `CORRECTIONS.md`). IDs of corrected questions are kept. Six questions moved to
new sets and got new IDs; `CHANGELOG.md` lists each move. No ID was retired. New sets and branch:
- S62 tips, S63 sales tax, S64 commissions, S65 fees, S66 combined multistep percent problems (S9 is now markup and
  markdown only, and S10 simple interest only).
- S67 volume and S68 exterior surface area of solids made of right prisms.
- S69 generating random samples with random digits, and S70 collecting data from a chance process.
- S18-B3: regrouping addends within 100 (Grade 2), as a numerical diagnostic for the properties set.

The engine gained a 3-D figure for solids made of prisms and a figure of a circle cut into wedges and rearranged.
Summary: 1,280 unchanged, 245 revised, 230 new, 0 retired.

This revision is not yet approved for the live game. In a staging copy, check the game's grading of `work`, `plot`,
and `plot_text` responses, of answers with two required parts (equation and solution), of two-root answers, of
equivalent fraction and decimal forms, of rounded answers, and of student-generated data (S70-M-Q3), and check that
the `G7:` UIDs survive import.

## Checks

These are checks of the exported bank, not of the live game.

- `engine/autocheck.py grade7` recomputes the 152 arithmetic answers it can parse; all agree. Every equation and every
  "x = … is the solution of …" statement was checked again with a computer algebra system, and every other revised or
  new answer was re-solved by hand.
- Every multiple-choice question has exactly one correct choice and no repeated choices. No two questions are the
  same (same text and figure).
- Earlier-grade fractions, including wrong choices, use their grade's denominators (Grade 3: 2, 3, 4, 6, 8; Grade 4
  adds 5, 10, 12, 100).
- Paired dot plots use data whose means and MADs equal the stated values; simulation plots, composite solids, and
  every new figure were checked visually in both PDFs. No text runs outside the page margins.
- `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields; it passes.
- `src/history/v1_records.json` is the published 1.0.0 snapshot; `src/changes.py` explains every difference from it,
  and the export stops if any question changed without an entry. `src/history/v2_records.json` is this version's
  snapshot, and `src/choice_plan.json` freezes the multiple-choice letters.

## Rebuild

```
python3 question-bank/engine/build.py grade7
python3 question-bank/engine/autocheck.py grade7
python3 question-bank/engine/export.py grade7
python3 question-bank/engine/coverage.py grade7
cd question-bank/nexus && zip -qr Grade7_Nexus_Import_v2.0.0.zip grade7 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade7_Nexus_Import_v2.0.0.zip
```
