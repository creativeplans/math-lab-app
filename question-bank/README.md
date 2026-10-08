# Common Core Math Question Bank

| Folder | Contents |
|---|---|
| `grade4/` | Grade 4 collection, version 1.0.0: 64 question sets, 1,600 questions (see its COVERAGE) |
| `grade5/` | Grade 5 collection, version 2.0.0: 71 question sets, 1,930 questions (see its CHANGELOG and COVERAGE) |
| `grade6/` | Grade 6 collection: 82 question sets, 2,465 questions |
| `nexus/grade4/`, `nexus/grade5/`, `nexus/grade6/` | Import packages for Untangle The Nexus (JSON per set, index, figure files, PDFs, manifest). Each has its own README. `nexus/Grade4_Nexus_Import_v1.0.0.zip` and `nexus/Grade5_Nexus_Import_v2.0.0.zip` are the packages zipped. |
| `engine/` | Shared code that builds the PDFs, answer keys, and Nexus packages |

Every set has a MAIN section (5 questions at the set's grade), BACKWARD branches (prerequisite skills from
earlier grades, 5 quick questions each), FORWARD 1 (5 questions, next grade), and FORWARD 2 (5 questions,
two grades up). Every question has an ID such as `S40-F2-Q3` that is printed on its page and used in all keys;
across grades use `uid`, which adds the collection (`G5:S40-F2-Q3`).

## Build

```
pip install reportlab pymupdf
python3 question-bank/engine/build.py grade5      # PDFs + answer key JSON/CSV in grade5/
python3 question-bank/engine/autocheck.py grade5  # recompute every arithmetic answer and compare with the key
python3 question-bank/engine/export.py grade5     # Nexus package in nexus/grade5/ (+ CHANGELOG.md)
python3 question-bank/engine/coverage.py grade5   # COVERAGE.md
python3 question-bank/engine/verify_package.py question-bank/nexus/grade5   # check the package
```

Replace `grade5` with `grade4` or `grade6` for the other grades. Run `build.py` before `export.py`.

## Adding a grade

Create `<gradeN>/src/grade.py` (`GRADE` and the ordered `DOMAINS` list) and `data_*.py` modules built with
`engine/qb.py` (`S`, `B`, `sa`, `mc`, `tf`, `plot`, figure helpers). Put each answer on its question: `key=` text for
written and drawing questions, `key=True`/`False` for true/false; for multiple choice, write the correct choice first.
`BALANCE_MC = True` in `grade.py` spreads multiple-choice answers evenly across A–D.

`S(..., num=N)` and `B(..., num=N)` fix a set or branch number so that IDs never move when sets are added later.
`draw_write(...)` makes a drawing + written question, and `work(..., method=...)` an answer with required work.
After a collection is published, keep a snapshot in `src/history/` and record every change in `src/changes.py`;
the export stops if a question changes without an entry there.
