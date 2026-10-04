# Grade 6 Common Core Math — Question Collection

Generated from the data in `src/`:

| File | Contents |
|---|---|
| `Grade6_Question_Collection.pdf` | The questions, one per page |
| `Grade6_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade6_Answer_Key.json` | Machine-readable key for AI grading: grading rules plus one record per question |
| `Grade6_Answer_Key.csv` | The same key as a spreadsheet |

- 82 focused question sets (2,465 questions) covering every Grade 6 standard. Each set's five MAIN questions are
  variations of one skill; standards with several distinct parts (e.g., tables vs. plotting vs. comparing ratios)
  get one set per part, and "display" standards include questions where students plot, graph, or draw.
- Each set: MAIN (Grade 6, 5 variations), numbered BACKWARD branches (5 quick-hit questions each),
  FORWARD 1 (Grade 7, 5 variations), FORWARD 2 (Grade 8, 5 variations).
- One question per page; the standard label sits in a separate reference box at the bottom.

## Question IDs and the answer key

Every question page shows an ID such as `S40-F2-Q3` (Set 40, FORWARD 2, question 3) in its reference box.
Sections are `M` (main), `B1`, `B2`, ... (backward branches), `F1` and `F2` (forward branches). The same ID heads
the answer page and the JSON/CSV record, so a response can be matched by ID or by page number.

Each JSON record has the question text, the displayed choices, `correct_letter` (multiple choice and true/false;
true/false shows A. True, B. False), `correct_answer`, and a `grading_note` with accepted alternatives or what an
explanation must include. The file's `grading_rules` explain how to grade equivalent forms, multi-part answers,
drawings, and explanations.

Answers are kept in `src/answers/key_*.txt`, one line per section. Multiple-choice answers there refer to the
authored choice order; `engine/answers.py` sets the order students see (numbers ascending, short lists in a natural
order, other lists in a fixed shuffle seeded by the question ID) and converts each answer to its displayed letter.
The build stops if any answer does not fit its question type.

## Rebuild

```
pip install reportlab pymupdf
python3 question-bank/engine/build.py grade6
python3 question-bank/engine/export.py grade6     # Untangle The Nexus package in question-bank/nexus/grade6/
```

Question content lives in `src/data_rp.py`, `data_ns.py`, `data_ee.py`, `data_g.py`, `data_sp.py`; the shared
builder is in `question-bank/engine/`.
Text markup: `{a/b}` renders a stacked fraction.

Forward 2 branches marked "NEAREST RELATED" (on the set overview, the branch divider page, and each card's
label) have no Grade 8 standard that directly continues the skill; they use the closest related Grade 8 standard.
