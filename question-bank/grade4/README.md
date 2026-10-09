# Grade 4 Common Core Math — Question Collection (version 2.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade4_Question_Collection.pdf` | The questions, one per page (2,269 pages) |
| `Grade4_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade4_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G4:S40-F2-Q3`) |
| `COVERAGE.md` | Each distinct Grade 4 requirement and the set that focuses on it |
| `CHANGELOG.md` | Every change since version 1.0.0, keyed by question ID, with the old → new ID map |

The Untangle The Nexus import package is `question-bank/nexus/grade4/`, also zipped as
`question-bank/nexus/Grade4_Nexus_Import_v2.0.0.zip`.

- 73 focused question sets (1,825 questions) covering all 34 Grade 4 standards. Each distinct requirement has its
  own set: for example, factor pairs, multiples, and prime or composite are separate sets under 4.OA.B.4, and adding
  and subtracting mixed numbers are separate sets under 4.NF.B.3.c.
- Each set: MAIN (Grade 4, 5 variations), two BACKWARD branches (Grade 3 or earlier only; the build stops if a backward
  branch uses a Grade 4 standard), FORWARD 1 (Grade 5), and FORWARD 2 (Grade 6). Forward branches marked
  "NEAREST RELATED" have no standard in their grade that directly continues the skill (for example angle measure
  continued by volume, rounding, reading numbers); the note names the branch's own grade.
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
- True/false: 333 true, 330 false. Multiple choice: A 96, B 94, C 93, D 94.

## Version 2.0.0

Applies every finding of the Grade 4 review (C01–C12, B01–B10, F01–F08, V01–V07, and the optional S11 item). IDs of
corrected questions are kept. Content that moved to a new set got a new ID; its old ID and the move are listed in
`CHANGELOG.md`. Three backward branches were retired and replaced (S6-B1 → S6-B3, S60-B1 → S60-B3) or moved
(S48-B2 → S68-B1, S49-B1 → S69-B1). Retired IDs are never reused. New sets: S65 (multistep remainders), S66 (subtract
fractions in word problems), S67 (add tenths and hundredths), S68 (perimeter formula), S69 (unknown side from the
perimeter), S70–S72 (draw points/lines/segments/rays, angles, perpendicular and parallel lines), S73 (identify them in
two-dimensional figures). Summary: 1,419 unchanged, 161 revised, 245 new, 20 retired.

This revision is not yet approved for the live game: recheck the regenerated files (and the game's grading of
`work`, `plot`, and `plot_text` responses) in a staging copy first.

## Checks

- `engine/autocheck.py grade4` recomputes the 345 arithmetic answers it can parse; all agree. Every other answer was
  solved when written and re-checked by hand.
- `engine/verify_package.py` checks the ZIP for broken references; it passes.
- No text runs outside the page margins in either PDF.
- `src/history/v1_records.json` is the published 1.0.0 snapshot; `src/changes.py` explains every difference from it,
  and the export stops if any question changed without an entry.

## Rebuild

```
python3 question-bank/engine/build.py grade4
python3 question-bank/engine/autocheck.py grade4
python3 question-bank/engine/export.py grade4
python3 question-bank/engine/coverage.py grade4
cd question-bank/nexus && zip -qr Grade4_Nexus_Import_v2.0.0.zip grade4 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade4_Nexus_Import_v2.0.0.zip
```
