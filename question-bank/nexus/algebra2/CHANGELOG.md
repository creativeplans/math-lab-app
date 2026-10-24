# Algebra II question collection — change log

## 1.0.0 (initial release, for independent review before import)

- First release: 84 sets (72 CORE, 12 ADVANCED EXTENSION), 2,525 questions, IDs `A2:S<set>-<section>-Q<n>`.
- Snapshot for later revisions: `src/history/v1_records.json`. Later versions will list changes by question ID above this entry.
- Not yet tried in the live game or with the AI grader; the importer was run in check mode only (see README).

### Errors found and fixed before release

| Question | Problem and fix |
|---|---|
| S12-F1-Q1 | Key gave too few deposits; recomputed: 68 deposits (67 give $19,838.70, 68 give $20,187.89). |
| S12-F2-Q2 | Comparison values recomputed (16,875.11 and 18,725.12) and the month corrected. |
| S18-F2-Q5 | Stated y-intercept (-4) contradicted the end behavior; changed to 4 so 2(x + 2)(x - 1)² fits all conditions. |
| S21-F1-Q4 | Keyed option was +10x⁴; the correct term is -10x⁴. Options reordered so the correct one is keyed. |
| S22-F1-Q1 | Key a = -1 was wrong for the original dividend; dividend changed to x³ + ax² + 2x + 4 (a = -2, remainder 5) and re-checked. |
| S26-F1-Q5 | Grading note contained an abandoned calculation; replaced with the correct equation x² - 2.8x - 4.8 = 0. |
| S45-F2-Q4 | Keyed option said the rates were equal; h has rate 20 and k has rate 10, so "a greater rate for h" is keyed. |
| S45-B2-Q4 | A distractor (24/72) was equal to the key (1/3); replaced with 72/24. |
| S48-F2-Q2 | Profit interval key used rounded endpoints inconsistently; restated with exact endpoints (9 ± √21)/2. |
| S60-F1-Q4/Q5 | Unfinished note and an unclear stem rewritten. |
| S64-B2-Q2 | Key described an unworkable digit scheme; stem now uses two-digit numbers 00-99 (00-24 = red). |
| S74-F1-Q3 | Note contained a wrong example; replaced with y = x/(x² + 1). |
| S75-F2-Q5 | Key -5 was wrong; (x + 3)/(x + 1) = 2 gives x = 1, which is allowed. |
| 71 branch and MAIN items | Stems that relied on another question ("this branch", "the same model", "the depth table", "the diet experiment" and similar) were rewritten to restate their own givens (validation check 16 and a wider phrase search; examples S7-F1-Q5, S12-F2-Q2, S43-B2-Q1, S61-M-Q2, S66-F2-Q1, S78-B2-Q1). |
| 127 true/false items | The first draft had 334 True and 90 False keys. 127 true statements were rewritten as false statements, each with a grading note that gives the correct fact (now 207 True, 217 False). |
| S74-B1-Q5 | The game importer (check mode) rejected the key 2x/((x - 2)(x + 2)) under "Form required: factored"; the item now asks to factor the denominator x² - 4. |

Figure layout fixes found by render inspection are listed in `VALIDATION.md` (Manual review, Figures).
