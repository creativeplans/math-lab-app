# Common Core Math Question Bank

| Folder | Contents |
|---|---|
| `grade3/` | Grade 3 collection, version 2.0.0: 69 question sets, 1,725 questions (see its CHANGELOG and COVERAGE) |
| `grade4/` | Grade 4 collection, version 2.0.0: 73 question sets, 1,825 questions (see its CHANGELOG and COVERAGE) |
| `grade5/` | Grade 5 collection, version 2.0.0: 71 question sets, 1,930 questions (see its CHANGELOG and COVERAGE) |
| `grade6/` | Grade 6 collection: 82 question sets, 2,465 questions |
| `grade7/` | Grade 7 collection, version 2.0.0: 70 question sets, 1,755 questions; FORWARD 2 uses Common Core high-school standards, which this bank places at Grade 9 (see its CHANGELOG, CORRECTIONS, and COVERAGE) |
| `grade8/` | Grade 8 collection, version 2.0.0: 65 question sets, 1,625 questions; both forward branches use Common Core high-school standards, which this bank places at Grade 9 (FORWARD 1) and Grade 10 (FORWARD 2) (see its CHANGELOG, CORRECTIONS, and COVERAGE) |
| `algebra1/` | Algebra I course collection, version 2.0.0: 84 question sets, 2,100 questions, covering the 60 standards of the Common Core traditional-pathway Algebra I course. No grade is assigned; forward branches use Geometry, Algebra II, Probability & Statistics, and Precalculus standards (see its README and COVERAGE) |
| `nexus/grade3/`, `nexus/grade4/`, `nexus/grade5/`, `nexus/grade6/`, `nexus/grade7/`, `nexus/grade8/` | Import packages for Untangle The Nexus (JSON per set, index, figure files, PDFs, manifest). Each has its own README. `nexus/Grade3_Nexus_Import_v2.0.0.zip`, `nexus/Grade4_Nexus_Import_v2.0.0.zip`, `nexus/Grade5_Nexus_Import_v2.0.0.zip`, `nexus/Grade7_Nexus_Import_v2.0.0.zip`, and `nexus/Grade8_Nexus_Import_v2.0.0.zip` are the packages zipped. `nexus/algebra1/` and `nexus/Algebra1_Nexus_Import_v2.0.0.zip` are the Algebra I package. |
| `engine/` | Shared code that builds the PDFs, answer keys, and Nexus packages |

Every set has a MAIN section (5 questions at the set's grade), BACKWARD branches (prerequisite skills from
earlier grades, 5 quick questions each), FORWARD 1 (5 questions, next grade), and FORWARD 2 (5 questions,
two grades up). Common Core does not assign high-school standards to a grade, so this bank places them: for Grade 7,
FORWARD 2 uses high-school standards such as `HSA-REI.B.3` placed at Grade 9; for Grade 8, FORWARD 1 uses high-school
standards placed at Grade 9 and FORWARD 2 uses high-school standards placed at Grade 10. Every question has an ID such as `S40-F2-Q3` that is printed on its page and used in all keys;
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

Replace `grade5` with `grade3`, `grade4`, `grade6`, `grade7`, `grade8`, or `algebra1` for the other collections. Run `build.py` before `export.py`.

## Course collections (high school)

High-school courses are collections without a grade. `<course>/src/grade.py` sets `COURSE` (id, name, file stem, seed)
instead of `GRADE`, and `engine/hs_courses.py` lists each course's standards and places every other high-school standard
in a course (Algebra I, Geometry, Algebra II, Probability & Statistics, Precalculus). In course mode the build checks that
MAIN uses the course's standards, backward branches use Grade K-8 standards or a standard taught in an earlier set,
forward branches use later courses, and every question has an explanation. See `algebra1/README.md`.

## Adding a grade

Create `<gradeN>/src/grade.py` (`GRADE` and the ordered `DOMAINS` list) and `data_*.py` modules built with
`engine/qb.py` (`S`, `B`, `sa`, `mc`, `tf`, `plot`, figure helpers). Put each answer on its question: `key=` text for
written and drawing questions, `key=True`/`False` for true/false; for multiple choice, write the correct choice first.
`BALANCE_MC = True` in `grade.py` spreads multiple-choice answers evenly across A–D.

`S(..., num=N)` and `B(..., num=N)` fix a set or branch number so that IDs never move when sets are added later.
`draw_write(...)` makes a drawing + written question, and `work(..., method=...)` an answer with required work.
After a collection is published, keep a snapshot in `src/history/` and record every change in `src/changes.py`;
the export stops if a question changes without an entry there.
