# Grade 7 Common Core Math — Question Collection (version 1.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade7_Question_Collection.pdf` | The questions, one per page (1,896 pages) |
| `Grade7_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade7_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G7:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 7 requirement and the set that focuses on it |

The Untangle The Nexus import package is `question-bank/nexus/grade7/`, also zipped as
`question-bank/nexus/Grade7_Nexus_Import_v1.0.0.zip`.

- 61 focused question sets (1,525 questions) covering every Grade 7 standard (all 37 lettered and unlettered
  standards, plus 7.SP.C.7 as a whole for comparing a model with observed results). Each distinct requirement has its
  own set: for example, 7.RP.A.3 has separate sets for multistep ratios, percent increase and decrease, markups and
  discounts, interest and commissions, and percent error; 7.NS.A.1.b has separate sets for number-line sums, additive
  inverses, and sums in context; and 7.G.B.4 has separate sets for circumference, area, and the relationship between them.
- Each set: MAIN (Grade 7, 5 variations), two BACKWARD branches (Grade 6 or earlier only; the build stops if a backward
  branch uses a Grade 7 standard), FORWARD 1 (Grade 8), and FORWARD 2 (Grade 9).
- **FORWARD 2 uses high-school standards** (Algebra I, Geometry, Functions, Number & Quantity, and Statistics &
  Probability codes such as `HSA-REI.B.3`, `HSG-CO.C.9`, `HSF-LE.A.1.c`, `HSS-CP.A.4`). In the PDFs, JSON, and CSV these
  branches are labeled "Grade 9 (High School)" with the high-school domain name, and `grade` is 9.
- 18 FORWARD 1 branches are marked "NEAREST RELATED": Grade 8 has no standard that directly continues the skill (for
  example percent change, inequalities, surface area, and the probability sets). The note names Grade 8, and the branch
  uses the closest Grade 8 standard (scientific notation, multistep equations, the Pythagorean theorem in three
  dimensions, two-way tables, scatter plots, or functions).
- Built to the Grade 3, 4, and 5 reviews' corrections from the start:
  - Every section tests one skill; backward items are one step each and stay inside their own grade's range.
  - Forward branches truly move ahead (proportional → linear functions → average rate of change; one-step equations →
    systems → quadratics; angles → parallel lines → proofs; probability → two-way tables → conditional probability).
  - When a question asks for a form (a fraction or a mixed number, in terms of π, scientific notation), the grading
    note asks for the same form and lists accepted equivalent forms.
  - Required-work questions accept any valid method and give an example; drawing answers describe every correct
    drawing ("any position or orientation"), and optional parts are never required.
  - Multiple-choice questions have exactly one correct choice; every triangle with given sides satisfies the triangle
    inequality; composite-figure questions say that the parts do not overlap; rounding instructions name the place.
  - Generic coordinate grids name their axes x and y. No official standards examples are reused.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer (`plot_text`,
  both parts graded), and answer with required work (`work`). Figures include integer and fraction number lines,
  inequality graphs with open and closed circles, coordinate grids in one and four quadrants, ratio tables, two-way
  tables, circles with a labeled radius or diameter, spinners, intersecting lines, composite figures, prisms, dot plots,
  box plots (single and paired), and bar graphs. Drawing questions use blank grids, number lines, and dot plots.
- True/false: 304 true, 302 false. Multiple choice: A 77, B 75, C 78, D 75.

This collection is not yet approved for the live game: check the files, and the game's grading of `work`, `plot`, and
`plot_text` responses, in a staging copy first.

## Checks

- `engine/autocheck.py grade7` recomputes the 136 arithmetic answers it can parse; all agree. Every other answer was
  solved when written and re-checked by hand, and every figure type was checked visually in both PDFs.
- No duplicate questions; every multiple-choice question has different choices.
- `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields; it passes.
- No text runs outside the page margins in either PDF.
- `src/history/v1_records.json` is the 1.0.0 snapshot and `src/choice_plan.json` freezes the multiple-choice letters, so
  later versions can keep IDs stable and explain every change.

## Rebuild

```
python3 question-bank/engine/build.py grade7
python3 question-bank/engine/autocheck.py grade7
python3 question-bank/engine/export.py grade7
python3 question-bank/engine/coverage.py grade7
cd question-bank/nexus && zip -qr Grade7_Nexus_Import_v1.0.0.zip grade7 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade7_Nexus_Import_v1.0.0.zip
```
