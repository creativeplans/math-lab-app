# Common Core Math Question Bank

| Folder | Contents |
|---|---|
| `grade5/` | Grade 5 collection: 57 question sets, 1,580 questions |
| `grade6/` | Grade 6 collection: 82 question sets, 2,465 questions |
| `nexus/grade5/`, `nexus/grade6/` | Import packages for Untangle The Nexus (JSON per set, index, figure files, PDFs). Each has its own README. |
| `engine/` | Shared code that builds the PDFs, answer keys, and Nexus packages |

Every set has a MAIN section (5 questions at the set's grade), BACKWARD branches (prerequisite skills from
earlier grades, 5 quick questions each), FORWARD 1 (5 questions, next grade), and FORWARD 2 (5 questions,
two grades up). Every question has an ID such as `S40-F2-Q3` that is printed on its page and used in all keys.

## Build

```
pip install reportlab pymupdf
python3 question-bank/engine/build.py grade5      # PDFs + answer key JSON/CSV in grade5/
python3 question-bank/engine/autocheck.py grade5  # recompute every arithmetic answer and compare with the key
python3 question-bank/engine/export.py grade5     # Nexus package in nexus/grade5/
```

Replace `grade5` with `grade6` for Grade 6. Run `build.py` before `export.py`.

## Adding a grade

Create `<gradeN>/src/grade.py` (`GRADE` and the ordered `DOMAINS` list) and `data_*.py` modules built with
`engine/qb.py` (`S`, `B`, `sa`, `mc`, `tf`, `plot`, figure helpers). Put each answer on its question: `key=` text for
written and drawing questions, `key=True`/`False` for true/false; for multiple choice, write the correct choice first.
`BALANCE_MC = True` in `grade.py` spreads multiple-choice answers evenly across A–D.
