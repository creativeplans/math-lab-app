# Grade 4 Common Core Math — Question Collection (version 1.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade4_Question_Collection.pdf` | The questions, one per page (1,989 pages) |
| `Grade4_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade4_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G4:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 4 requirement and the set that focuses on it |

The Untangle The Nexus import package is `question-bank/nexus/grade4/`, also zipped as
`question-bank/nexus/Grade4_Nexus_Import_v1.0.0.zip`.

- 64 focused question sets (1,600 questions) covering all 34 Grade 4 standards. Each distinct requirement has its
  own set: for example, factor pairs, multiples, and prime or composite are separate sets under 4.OA.B.4, and adding
  and subtracting mixed numbers are separate sets under 4.NF.B.3.c.
- Each set: MAIN (Grade 4, 5 variations), two BACKWARD branches (Grade 3 or earlier only; the build stops if a backward
  branch uses a Grade 4 standard), FORWARD 1 (Grade 5), and FORWARD 2 (Grade 6). Forward 2 branches marked
  "NEAREST RELATED" have no Grade 6 standard that directly continues the skill (angles, rounding, reading numbers).
- Built to the Grade 5 review's corrections from the start:
  - Grade 3 fractions use only denominators 2, 3, 4, 6, and 8.
  - Grade 2 arrays have at most 5 rows and 5 columns.
  - 4.NBT multiplication and division stay within the standard's sizes.
  - Estimation questions state the rounding to use.
  - Multiples are "positive multiples."
  - Ounces always measure weight.
  - Generic coordinate grids name their axes x and y.
  - Forward branches each test one skill.
  - No official examples are reused.
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer (`plot_text`,
  both parts graded), and answer with required work (`work`: the standard algorithm or a model is graded, not only
  the final number). Drawing questions include protractors, number lines, line plots, grids, and lines of symmetry.
- True/false: 292 true, 293 false. Multiple choice: A 85, B 82, C 82, D 82.

## Checks

- `engine/autocheck.py grade4` recomputes the 321 arithmetic answers it can parse; all agree. Every other answer was
  solved when written and re-checked by hand.
- `engine/verify_package.py` checks the ZIP for broken references; it passes.
- No text runs outside the page margins in either PDF.
- `src/history/v1_records.json` and `src/choice_plan.json` record this version, so later corrections are tracked by
  question ID (see `grade5/` for an example).

## Rebuild

```
python3 question-bank/engine/build.py grade4
python3 question-bank/engine/autocheck.py grade4
python3 question-bank/engine/export.py grade4
python3 question-bank/engine/coverage.py grade4
cd question-bank/nexus && zip -qr Grade4_Nexus_Import_v1.0.0.zip grade4 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade4_Nexus_Import_v1.0.0.zip
```
