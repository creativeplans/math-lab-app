# Grade 8 Common Core Math — Question Collection (version 1.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade8_Question_Collection.pdf` | The questions, one per page (1,803 pages) |
| `Grade8_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade8_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G8:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 8 requirement, the set that focuses on it, and the performance its MAIN questions test |

The Untangle The Nexus import package is `question-bank/nexus/grade8/` (it includes `COVERAGE.md`), also zipped as
`question-bank/nexus/Grade8_Nexus_Import_v1.0.0.zip`.

- 58 focused question sets (1,450 questions) covering every Grade 8 standard code (all 33 lettered and unlettered
  standards, plus 8.EE.C.7, 8.EE.C.8, and 8.G.A.1 as wholes). `COVERAGE.md` lists the performance each set's MAIN
  questions actually test.
- Each set: MAIN (Grade 8, 5 variations), two backward branches (Grade 7 or earlier only), FORWARD 1, and FORWARD 2.
- **Both forward branches use Common Core high-school standards**, and they extend the Grade 8 skill into algebra,
  functions, geometry, number, and statistics. Examples:
  - Systems by graphing (S19) go on to `HSA-REI.D.11` and then to graphing systems of inequalities (`HSA-REI.D.12`).
  - Parallel lines and a transversal (S42) go on to proving theorems about lines and angles (`HSG-CO.C.9`) and then to
    slopes of parallel and perpendicular lines (`HSG-GPE.B.5`).
  - Volume of a cone (S50) goes on to volume formulas (`HSG-GMD.A.1`) and then to volume problems (`HSG-GMD.A.3`).
  - Two-way tables (S57) go on to relative frequencies (`HSS-ID.B.5`) and then to conditional probability and
    independence (`HSS-CP.A.4`).
- Common Core does not assign high-school standards to a grade. This bank places FORWARD 1 at Grade 9 and FORWARD 2
  at Grade 10 as an instructional choice:
  - The PDFs label them "High School (Grade 9 in this bank)" and "High School (Grade 10 in this bank)".
  - In the import package, `standard_grade` is 9 or 10, and every high-school record has a `standard_level` field
    that says so.
  - Each high-school code is used in only one of the two slots, so a code always has the same placement.
- No branch is marked NEAREST RELATED. Every forward branch uses a high-school standard that directly continues the
  set's skill.
- Students do the drawing, not just describe it:
  - irrational numbers plotted on number lines (S4)
  - proportional graphs, systems, and functions graphed (S13, S19, S24)
  - graphs sketched from descriptions (S31)
  - translations, reflections, rotations, and dilations drawn on the coordinate plane (S32–S34, S36–S39)
  - right triangles drawn on a grid to find a distance (S48)
  - scatter plots and lines of fit drawn (S53, S55)
  - two-way tables completed from survey counts and from raw paired answers (S57)
- Grading rules:
  - Write-and-solve questions require both a valid equation (or system or inequality) and its solution.
  - Equations with two roots require both roots.
  - Proofs and explanations require reasons.
  - Exact answers (in terms of π or with radicals) or rounded answers are stated in the question.
  - Coins and number cubes are fair, and repeated trials are independent, as stated in each question.
  - Drawing answers accept any correct drawing. A line of fit is accepted when it follows the trend with points on
    both sides, and the equation or estimate must match the student's own line.
  - Work answers accept any valid method.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer
  (`plot_text`, both parts graded), and answer with required work (`work`).
- Figures:
  - number lines and coordinate grids, including transformations and function graphs
  - tables and two-way tables (some blank to fill in)
  - parallel lines cut by a transversal, triangles with exterior angles, and similar triangles
  - the square-in-a-square proof figure of the Pythagorean theorem, right triangles, and boxes
  - cylinders, cones, and spheres
  - scatter plots, dot plots, and a bar graph
- True/false: 266 true, 266 false. Multiple choice: A 74, B 72, C 70, D 72.

This collection is not yet approved for the live game. In a staging copy, check:
- how the game grades `work`, `plot`, and `plot_text` responses
- answers with two required parts (equation and solution) and two-root answers
- exact forms (π, radicals) and rounded answers
- that the `G8:` UIDs survive import

## Checks

These are checks of the exported bank, not of the live game.

- `engine/autocheck.py grade8` recomputes the 109 arithmetic answers it can parse; all agree.
- Every equation and every "x = … is the solution of …" statement was checked again with a computer algebra system,
  and the remaining answers were solved again by hand. This found and fixed one wrong true/false statement.
- Every multiple-choice question has exactly one correct choice and no repeated choices. No two questions are the
  same (same text and figure).
- Every backward branch uses a Grade 7 or earlier standard; the build stops otherwise.
- Earlier-grade questions use their grade's numbers (the Grade 3 and Grade 4 branches use no fractions).
- Every figure was checked visually in the question PDF. No text runs outside the page margins.
- `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields; it passes.
- `src/history/v1_records.json` is this version's snapshot. Any later revision must explain every difference from it
  in `src/changes.py`; the export stops otherwise. `src/choice_plan.json` freezes the multiple-choice letters.

## Rebuild

```
python3 question-bank/engine/build.py grade8
python3 question-bank/engine/autocheck.py grade8
python3 question-bank/engine/export.py grade8
python3 question-bank/engine/coverage.py grade8
cd question-bank/nexus && zip -qr Grade8_Nexus_Import_v1.0.0.zip grade8 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade8_Nexus_Import_v1.0.0.zip
```
