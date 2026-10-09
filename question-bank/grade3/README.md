# Grade 3 Common Core Math — Question Collection (version 1.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade3_Question_Collection.pdf` | The questions, one per page (1,896 pages) |
| `Grade3_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade3_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G3:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 3 requirement and the set that focuses on it |

The Untangle The Nexus import package is `question-bank/nexus/grade3/`, also zipped as
`question-bank/nexus/Grade3_Nexus_Import_v1.0.0.zip`.

- 61 focused question sets (1,525 questions) covering all 33 Grade 3 standards. Each distinct requirement has its own
  set: for example, the commutative, associative, and distributive properties are separate sets under 3.OA.B.5;
  comparing fractions with the same denominator, with the same numerator, and only for the same whole are separate
  sets under 3.NF.A.3.d; and area by tiling, area by multiplying, the distributive property with tiling, and areas of
  rectilinear figures each have their own set under 3.MD.C.7.
- Each set: MAIN (Grade 3, 5 variations), two BACKWARD branches (Grade 2, Grade 1, or Kindergarten only; the build
  stops if a backward branch uses a Grade 3 standard), FORWARD 1 (Grade 4), and FORWARD 2 (Grade 5). Forward branches
  marked "NEAREST RELATED" have no standard in their grade that directly continues the skill (for example area
  continued by volume, or picture and bar graphs continued by graphing points); the note names the branch's own grade.
- Built to the Grade 4 and Grade 5 reviews' corrections from the start:
  - Every section tests one skill; addition and subtraction, area and perimeter, and making and using a display are
    never mixed in one section.
  - Backward items are one step each and stay inside their standard's range (odd and even up to 20, arrays up to 5 by 5,
    Grade 2 adding and subtracting within 100 or with models within 1000, halves, thirds, and fourths of shapes).
  - Grade 3 fractions use only denominators 2, 3, 4, 6, and 8, including the wrong choices.
  - When a question asks for a form (hours and minutes, fourths, a fraction or a mixed number), the grading note asks
    for the same form.
  - Required-work questions accept any valid strategy and give examples; drawing answers accept any correct drawing.
  - Geometry examples are exact: "a rectangle whose length and width are different", "a rhombus that is not a square".
  - Multiple-choice questions have exactly one correct choice.
  - Generic coordinate grids name their axes x and y.
  - No official standards examples are reused.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer (`plot_text`,
  both parts graded), and answer with required work (`work`). Figures include clocks to draw hands on, inch rulers
  with objects to measure, measuring containers, picture graphs and scaled bar graphs (blank ones to complete), time
  number lines, fraction number lines and bars, unit-square figures, and labeled rectilinear shapes.
- True/false: 298 true, 299 false. Multiple choice: A 78, B 77, C 76, D 76.

## Checks

- `engine/autocheck.py grade3` recomputes the 241 arithmetic answers it can parse; all agree. Every other answer was
  solved when written and re-checked by hand, and every figure type was checked visually in both PDFs.
- No duplicate questions; every multiple-choice question has four different choices.
- `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields; it passes.
- No text runs outside the page margins in either PDF.
- `src/history/v1_records.json` and `src/choice_plan.json` record this version, so later corrections are tracked by
  question ID (see `grade4/` and `grade5/` for examples).

## Rebuild

```
python3 question-bank/engine/build.py grade3
python3 question-bank/engine/autocheck.py grade3
python3 question-bank/engine/export.py grade3
python3 question-bank/engine/coverage.py grade3
cd question-bank/nexus && zip -qr Grade3_Nexus_Import_v1.0.0.zip grade3 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade3_Nexus_Import_v1.0.0.zip
```
