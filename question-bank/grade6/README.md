# Grade 6 Common Core Math — Question Collection

`Grade6_Question_Collection.pdf` is generated from the question data in `src/`.

- 82 focused question sets (2,465 questions) covering every Grade 6 standard. Each set's five MAIN questions are
  variations of one skill; standards with several distinct parts (e.g., tables vs. plotting vs. comparing ratios)
  get one set per part, and "display" standards include questions where students plot, graph, or draw.
- Each set: MAIN (Grade 6, 5 variations), numbered BACKWARD branches (5 quick-hit questions each),
  FORWARD 1 (Grade 7, 5 variations), FORWARD 2 (Grade 8, 5 variations).
- One question per page; the standard label sits in a separate reference box at the bottom.

## Rebuild

```
pip install reportlab
python3 question-bank/grade6/src/build.py
```

Question content lives in `src/data_rp.py`, `data_ns.py`, `data_ee.py`, `data_g.py`, `data_sp.py`.
Text markup: `{a/b}` renders a stacked fraction.

Forward 2 branches marked "NEAREST RELATED" (on the set overview, the branch divider page, and each card's
label) have no Grade 8 standard that directly continues the skill; they use the closest related Grade 8 standard.
