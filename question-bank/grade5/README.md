# Grade 5 Common Core Math — Question Collection (version 2.0.0)

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade5_Question_Collection.pdf` | The questions, one per page (2,393 pages) |
| `Grade5_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade5_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, e.g. `G5:S40-F2-Q3`) |
| `CHANGELOG.md` | Every change since version 1.0.0, keyed by question ID, with the old → new ID map |
| `COVERAGE.md` | Each distinct Grade 5 requirement and the set that focuses on it |

The Untangle The Nexus import package is `question-bank/nexus/grade5/`, also zipped as
`question-bank/nexus/Grade5_Nexus_Import_v2.0.0.zip`.

- 71 focused question sets (1,930 questions) covering every Grade 5 standard. Each distinct requirement
  has its own set (69 requirements, see `COVERAGE.md`).
- Each set: MAIN (Grade 5, 5 variations), BACKWARD branches (Grade 4 and earlier only; the build stops if a backward
  branch uses a Grade 5 standard), FORWARD 1 (Grade 6), FORWARD 2 (Grade 7).
- Response types: multiple choice, true/false, short answer, drawing (`plot`), drawing + written answer
  (`plot_text`, both parts graded), and answer with required work (`work`: the standard algorithm, long division,
  or a model is graded, not just the final number).
- Generic coordinate grids name their axes x and y; situation graphs keep their own axis names.
- True/false: 255 true, 248 false. Multiple choice: A 106, B 104, C 102, D 99. Questions kept from version 1.0.0
  keep their answer letters.

## Version 2.0.0

Applies every finding of the Grade 5 review (C01–C13, B01–B07, F01–F08, O01, coverage, import). IDs of corrected
questions are kept. Content that moved got a new ID and its old ID is listed in `CHANGELOG.md`. A branch rebuilt with
a different standard was retired, and its replacement has a new branch number (for example, S7-B2 was retired and
replaced by S7-B4). Retired IDs are never reused. Summary: 1,329 unchanged, 166 revised, 435 new, 85 retired.

## Checks

`engine/autocheck.py grade5` recomputes the 556 arithmetic answers it can parse (all agree); every other new or
revised answer was re-solved by hand. `engine/verify_package.py` checks the ZIP: manifest checksums, index ↔ set files,
unique IDs and uids, every figure asset, answer letters, grading fields for the new response types, and the revision map.
All PDF pages were scanned for text outside the page margins (none).

## Rebuild

```
python3 question-bank/engine/build.py grade5
python3 question-bank/engine/autocheck.py grade5
python3 question-bank/engine/export.py grade5
python3 question-bank/engine/coverage.py grade5
cd question-bank/nexus && zip -qr Grade5_Nexus_Import_v2.0.0.zip grade5 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Grade5_Nexus_Import_v2.0.0.zip
```
