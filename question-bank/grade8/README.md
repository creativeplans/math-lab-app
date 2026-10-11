# Grade 8 Common Core Math — Question Collection (version 2.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade8_Question_Collection.pdf` | The questions, one per page (2,020 pages) |
| `Grade8_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade8_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G8:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 8 requirement, the set that focuses on it, and the performance its MAIN questions test |
| `CHANGELOG.md` | Every change since version 1.0.0, keyed by question ID |
| `CORRECTIONS.md` | Checklist of every Grade 8 review finding code with the question IDs it changed |

The Untangle The Nexus import package is `question-bank/nexus/grade8/` (it includes `revisions.json`, `CHANGELOG.md`,
`CORRECTIONS.md`, and `COVERAGE.md`), also zipped as `question-bank/nexus/Grade8_Nexus_Import_v2.0.0.zip`.

- 65 focused question sets (1,625 questions) covering every Grade 8 standard code (all 33 lettered and unlettered
  standards, plus 8.EE.C.7, 8.EE.C.8, and 8.G.A.1 as wholes). `COVERAGE.md` lists the performance each set's MAIN
  questions actually test.
- Each set: MAIN (Grade 8, 5 variations), two backward branches (Grade 7 or earlier only), FORWARD 1, and FORWARD 2.
- **Both forward branches use Common Core high-school standards**, and each one adds a high-school demand beyond the
  Grade 8 skill: letter coefficients and parameter conditions, proofs (elimination, the converse of the Pythagorean
  theorem, SAS/ASA/SSS by rigid motions, triangle proportionality), trigonometric ratios, quadratic and exponential
  models, technology-based regression and correlation, residual plots, and a compass-and-straightedge construction.
- Common Core does not assign high-school standards to a grade. This bank places FORWARD 1 at Grade 9 and FORWARD 2
  at Grade 10 as an instructional choice:
  - The PDFs label them "High School (Grade 9 in this bank)" and "High School (Grade 10 in this bank)".
  - In the import package, `standard_grade` is 9 or 10, and every high-school record has a `standard_level` field
    that says so.
  - Each high-school code is used in only one of the two slots, so a code always has the same placement.
- Seven FORWARD 2 branches are marked NEAREST RELATED (S3, S11, S33, S36, S38, S41, S47): no high-school standard
  directly continues the set's skill at that step, so the branch uses the nearest related one. The note and the
  import flag `nearest_related` say so.
- Students do the drawing and the arguing, not just describe them: number lines, graphs, transformations with
  before-and-after measurements (S32–S34), triangles drawn with a protractor (S65), scatter plots, lines of fit,
  residual plots, completed two-way tables, informal arguments for the angle facts of 8.G.A.5 (S63–S65), and their
  own equation examples (S62).
- Grading rules:
  - Write-and-solve questions require both a valid equation (or system or inequality) and its solution.
  - Equations with two roots require both roots.
  - Proofs and explanations require reasons; `work` answers grade the required method (for example the completed
    square, or the table of both sides).
  - Exact answers (in terms of π or with radicals) or rounded answers are stated in the question.
  - Coins and number cubes are fair, repeated trials are independent, and needed conditions (x ≠ 0, a point not on
    the mirror line, distinct lines, which dimension stays fixed) are stated.
  - Drawing answers accept any correct drawing; lines of fit and student measurements are graded against the
    student's own line or measurements.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer
  (`plot_text`, both parts graded), and answer with required work (`work`).
- True/false: 296 true, 297 false. Multiple choice: A 83, B 79, C 80, D 81.

## Version 2.0.0

Applies every finding of the Grade 8 review (C01–C16, B01–B02, V01–V05, F01–F13, R01, D01: 38 required; P01–P06:
6 recommended); none was deferred (see `CORRECTIONS.md`). IDs of corrected questions are kept. New sets and branch:
- S59 estimating expressions with irrational numbers; S60 deriving y = mx; S61 deriving y = mx + b (S15 now focuses
  on why the slope is the same between any two points); S62 writing and transforming equation examples; S63, S64,
  and S65 the informal arguments for the triangle angle sum, parallel lines cut by a transversal, and AA.
- S43-B3 replaces S43-B2, which used a standard (7.G.B.5) that does not cover the triangle angle sum. S43-B2 is
  retired and its IDs will not be reused.

The engine no longer uses transparency for shaded polygons, so the answer key's embedded question pages have no
missing graphics resources (R01). Summary: 1,226 unchanged, 219 revised, 180 new, 5 retired.

This revision is not yet approved for the live game. In a staging copy, check:
- how the game grades `work`, `plot`, and `plot_text` responses, constructions, and student-measured drawings
- answers with two required parts and two-root answers
- exact forms (π, radicals) and rounded answers
- NEAREST RELATED routing
- that the `G8:` UIDs survive import

## Checks

These are checks of the exported bank, not of the live game.

- `engine/autocheck.py grade8` recomputes the 117 arithmetic answers it can parse; all agree. Every equation and
  every "x = … is the solution of …" statement was checked again with a computer algebra system.
- Every new or revised question was solved by hand, and every new or revised multiple-choice item was checked
  choice by choice for exactly one correct answer. Questions unchanged since 1.0.0 were not solved again in this round.
- No two questions are the same (same text and figure). Every backward branch uses a Grade 7 or earlier standard;
  the build stops otherwise. The Grade 3 and Grade 4 branches use no fractions.
- New and changed figures were checked visually in the question PDF, along with sample answer-key pages. Both PDFs
  render with no missing-resource warnings, and no text runs outside the page margins.
- `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields; it passes.
- `src/history/v1_records.json` is the published 1.0.0 snapshot; `src/changes.py` explains every difference from it,
  and the export stops if any question changed without an entry. `src/history/v2_records.json` is this version's
  snapshot, and `src/choice_plan.json` freezes the multiple-choice letters.

## Rebuild

```
python3 question-bank/engine/build.py grade8
python3 question-bank/engine/autocheck.py grade8
python3 question-bank/engine/export.py grade8
python3 question-bank/engine/coverage.py grade8
cd question-bank/nexus && zip -qr Grade8_Nexus_Import_v2.0.0.zip grade8 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade8_Nexus_Import_v2.0.0.zip
```
