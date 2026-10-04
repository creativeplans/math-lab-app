# Grade 5 Common Core Math — Question Collection

Generated from the data in `src/` by `question-bank/engine/`:

| File | Contents |
|---|---|
| `Grade5_Question_Collection.pdf` | The questions, one per page |
| `Grade5_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question and its answer |
| `Grade5_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID |

The Untangle The Nexus import package is in `question-bank/nexus/grade5/`.

- 57 focused question sets (1,580 questions) covering every Grade 5 standard (OA, NBT, NF, MD, G). Standards with
  distinct parts get one set per part (for example, multiplying a decimal by 10 vs. placing the decimal point;
  making a line plot vs. using line-plot data; finding volume vs. finding a missing dimension).
- Each set: MAIN (Grade 5, 5 variations), numbered BACKWARD branches (Grade 4 and earlier, 5 quick questions
  each), FORWARD 1 (Grade 6, 5 variations), FORWARD 2 (Grade 7, 5 variations).
- Forward 2 branches marked "NEAREST RELATED" have no Grade 7 standard that directly continues the skill (powers
  of 10 and expanded form with exponents); they use the closest related Grade 7 standard.
- Students plot, graph, or draw where a standard calls for it (graphing pattern pairs, line plots, plotting points).
- True/false answers are balanced (182 true, 203 false), and multiple-choice answers are spread evenly across A–D.

## Checks

Every answer was solved when written and checked again. `engine/autocheck.py grade5` recomputes the 461 arithmetic
answers it can parse; the other 1,119 (word problems, drawings, concepts, figures) were re-solved by hand.

## Rebuild

```
python3 question-bank/engine/build.py grade5
python3 question-bank/engine/autocheck.py grade5
python3 question-bank/engine/export.py grade5
```
