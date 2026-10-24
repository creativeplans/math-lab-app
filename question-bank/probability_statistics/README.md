# Probability & Statistics — Question Collection (version 1.1.0)

The High School Probability & Statistics collection for Untangle the Nexus. Probability & Statistics is a course, not a
grade (students usually take it in grade 10, 11 or 12), so the collection uses course-placement labels, not grade
levels. Everything is generated from one source, the data in `src/`, by `question-bank/engine/`. The collection has its
own directory and its own ID namespace (`PS`). It does not edit, import or depend on any Algebra I, Geometry or Algebra II
file; those courses appear only as standard codes in backward branches.

**Every question is graded automatically by the game.** Question types are short answer, multiple choice and
true/false only, and every short-answer key was run through the game's own answer checker.

**What changed in 1.1.0.** This version answers an external review of 1.0.0. Question IDs are kept: 206 questions
were revised, 1,229 are unchanged, none were added or retired, and no unchanged multiple-choice item changed its letter.
`CHANGELOG.md` lists every changed ID with its finding (R01-R09):

- **One correct answer per item (R01).** Two histogram items had two identical correct panels (S2-M-Q2, S2-M-Q4); each
  extra panel now shows a specific error. A strategy item with a tie (S54-F1-Q3) and a random-digit count with more than
  one defensible answer (S52-F1-Q4) were rewritten.
- **Statistical statements (R02).** Overlap is judged from standardized gaps or a stated normal model. Random assignment
  "tends to" balance groups. Least squares balances residuals, not counts of points. A conclusion names the population it
  applies to.
- **Simulation decisions (R03).** Every decision rule states the model, the tail counted (one-sided or two-sided) and
  the 5% cutoff. Supplied simulation results are labeled hypothetical (R09).
- **Local givens and forms (R04).** Each question restates what it uses. Fraction answers are asked for and keyed as
  fractions (5/4, not 1.25).
- **Probability models, bank-wide (R05).** Fair devices, independent trials, cards drawn at random from a standard
  52-card deck with the replacement rule, the guessing model, and the payoff when an event does not happen. This was
  applied to every item the new check 28 finds, not only the review's examples (127 questions).
- **Precision and wording (R06-R08).** Keys are written to the stated precision (2.00, 0.10, 44.10, 2.50). Overstated
  claims were narrowed. A MAIN item that only repeated its givens (S54-M-Q1) now asks for a computation.
- **New permanent checks.** Check 27 recomputes every four-graph item from its question and requires exactly one
  matching panel. Check 28 looks for a stated probability model. Check 29 compares the stated precision with the key.
  Check 30 runs 37 fixed right and wrong responses through the game's checker. Run on the 1.0.0 answer key, the rules of checks 27 and 29
  flag the review's findings (S2-M-Q2, S2-M-Q4; S5-F1-Q3, S14-F2-Q1, S49-F1-Q1).

This release is for independent review before import. It has not been pushed, merged, published, or tried in the live
game.

| File | Contents |
|---|---|
| `Probability_Statistics_Question_Collection.pdf` | The questions, one per page (1,781 pages including set and branch title pages) |
| `Probability_Statistics_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Probability_Statistics_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `PS:S12-B2-Q3`). Questions with a figure also carry `figure_svg`, `figure_png`, `figure_description`, and `figure_data` |
| `COVERAGE.md` | The course profile, the overlap with the Algebra I, Geometry and Algebra II collections, a matrix of every standard and subskill with its MAIN sets, pages and **assessed response**, the branch map, and response types |
| `DATASETS.md` | Every dataset used: values, size, units, context. All are synthetic (written for this collection) |
| `VALIDATION.md` | The 30 automatic checks, each with its result and its actual scope, plus the table of fixed checker responses and the manual review record |
| `CHANGELOG.md` | Version 1.1.0 by question ID, followed by the 1.0.0 release notes |
| `PLAN.md` | The set list by authoring batch |
| `src/` | The single source: `standards.py` (inventory and subskills), `data_*.py` (sets), `datasets.py` (dataset registry), `common.py` (statistics and figure helpers), `grade.py` (course settings and grading rules), `resolve.py` (independent re-solve), `validate.py`, `tools/checker_contract.ts` (runs the game's answer checker on every key), `tools/checker_cases.ts` with `checker_cases.json` (fixed right and wrong responses), `review_log.py`, `coverage_report.py`, `changes.py` (the 1.1.0 revision map), `choice_plan.json` (frozen multiple-choice letters), `history/` (the 1.0.0 and 1.1.0 snapshots and the 1.0.0 release notes) |

The Untangle The Nexus import package is `question-bank/nexus/probability_statistics/`, zipped as
`question-bank/nexus/Probability_Statistics_Nexus_Import_v1.1.0.zip` (the 1.0.0 ZIP is kept next to it). Its README describes every field. The split PDFs
(three parts of at most 800 pages each) are in its `pdf/` folder with `PART_INDEX.md` (the page and question-ID range of
each part), and `MANIFEST.json` lists every file with its SHA-256 hash.

## Contents

- **54 question sets, 1,435 questions.**
  - **CORE strand (41 sets, 1,100 questions):** every Common Core High School Statistics & Probability (HSS) standard not
    marked (+): all of S-ID (HSS-ID.B.6 and its parts a, b and c separately), S-IC, and S-CP.A.1-5, S-CP.B.6-7. That is
    25 standards.
  - **ADVANCED EXTENSION strand (13 sets, 335 questions):** every HSS standard marked (+): HSS-CP.B.8, HSS-CP.B.9 and all
    of HSS-MD (MD.A.1-4, MD.B.5.a, MD.B.5.b, MD.B.6, MD.B.7). That is 10 standards. MD.B.5.a and MD.B.5.b have separate
    sets. Every record carries `strand`, and the MAIN records of these sets say "Advanced Extension (+)" in `course_level`.
- **Subskills.** Each standard is split into the distinct demands its wording names (54 subskills, listed in
  `COVERAGE.md` section 3). Each one is the focus of a set whose five MAIN questions test it. For example HSS-ID.A.1 has
  three sets (dot plots, histograms, box plots), HSS-CP.B.9 three (permutations, combinations, probability by counting).
- **Set structure.**
  - **MAIN:** five parallel questions on one target skill. No MAIN has a true/false item.
  - **BACKWARD 1..N:** 125 branches (37 sets have 2, 17 have 3), each diagnosing one obstacle, with teacher metadata
    (obstacle, why it matters, evidence of mastery; 77 exact and 48 supporting prerequisites).
  - **FORWARD 1 and FORWARD 2:** each states its progression type (same-course deepening or cross-standard extension),
    whether it is the direct next standard or the nearest related one, and its new demand; FORWARD 2 states how it builds
    on FORWARD 1.
- **No circular prerequisites.** A backward standard is a K-8 standard, an Algebra I standard (S-ID codes and function
  skills used as prerequisites are labeled Algebra I), or the MAIN standard of an *earlier* set of this collection. The
  build stops on anything else.
- **Every question stands alone.** IDs are printed in a separate reference box on each page, not in the question.
- **Question types:** short answer 573; multiple choice 433 (A 111, B 107, C 110, D 105); true/false 429 (226 True,
  203 False), none in MAIN. 190 questions carry a figure: 125 tables (data tables, two-way tables, normal tables,
  random-digit tables), 27 scatter or residual plots, 10 box plots, 9 dot plots, 6 histograms, and 13 four-panel
  "Graph A-D" choice figures.

## Overlap with Algebra I, Geometry and Algebra II

The Common Core traditional pathway spreads statistics over Algebra I (S-ID), Geometry (S-CP) and Algebra II (S-ID.A.4,
S-IC, S-MD.B.6-7). In this bank, the Algebra I collection assesses the S-ID standards and the Algebra II collection
assesses S-ID.A.4, all of S-IC and S-MD.B.6-7 in MAIN sets; the Geometry collection does not assess S-CP in MAIN sets.
This collection covers all of them again, with new questions and datasets, as one self-contained course. The table in
`COVERAGE.md` section 2 lists each shared code. A school that uses several of these collections can assign the
overlapping sets once, in the course where it teaches them.

## How each question is graded (the contract with the game)

- **Multiple choice and true/false:** the chosen letter is compared with `correct_letter`. Each multiple-choice item has
  exactly one correct option; its grading note says what is wrong with the other options.
- **Short answer:** the game's answer checker compares the response with `correct_answer`. Each question has one answer
  line per part, names the form ("a fraction in lowest terms", "a decimal", "as a percent") and the precision ("to the
  nearest tenth", "four decimal places"), and the key is written to that precision (2.00, 0.10).
  The checker compares values, so 2, 2.0 and 2.00 are all accepted, while 1.633 or 1.6 for 1.63 is rejected. It also
  accepts an equal decimal or mixed number for a fraction (1.25 or 1 1/4 for 5/4). Check 30 records this behavior.
- **Word answers** appear only when the question lists the allowed words (yes or no; positive or negative; a letter A, B,
  C or D; "skip").
- **Conventions stated on the page** (validation check 24): quartiles are the medians of the lower and upper halves, the
  median left out of both halves when n is odd; an outlier lies more than 1.5·IQR beyond a quartile; each standard
  deviation question says population (divide by n) or sample (divide by n - 1); histogram bins include their left
  endpoint and exclude their right endpoint; residual = observed - predicted; margin of error = 2 × the standard
  deviation of the simulated values.
- **Probability models** state the sample space or process: fair, equally likely, with or without replacement, order
  matters or not, independent trials. "Or" is inclusive. Conditional probability is written "P(A given B)", and no
  question reverses it silently; questions that are about the reversal say so.
- **Simulations:** students never report one random run. A simulation they carry out uses the random digits printed on
  the page, so every correct procedure gives the same count. A simulation run by someone else is given as a table of
  results. Every decision states the model, what counts as "at least as extreme" (one tail or both), and the 5% threshold.
  A rare result is evidence against the model, not proof; a common result is consistent with it, not proof that it is
  true.
- **Technology:** a question that needs a calculator or spreadsheet says so ("A calculator or spreadsheet may be used")
  and names what to compute (mean and standard deviation, least-squares line, correlation). Normal-curve areas come from
  a table printed on the page; the key uses the table's four-decimal values.

## How construct, design, explain and simulate demands are assessed

Some standards ask students to construct a plot, design a study, explain a conclusion or run a simulation. Each of these
is assessed through something the game can check, and `COVERAGE.md` labels it honestly:

- **Constructing displays:** the numbers that define the display (dot counts, bin counts with the stated endpoint rule,
  five-number summaries, residuals), or a choice among four candidate plots whose wrong panels show specific errors
  (wrong endpoint rule, quartiles from the wrong halves, swapped coordinates).
- **Designing studies and choosing methods:** a choice among designs, samples or assignments, each wrong option a
  specific flaw (voluntary response, no random assignment, wrong scope of conclusion), or carrying out a random
  selection with printed digits.
- **Explaining and evaluating:** a choice among conclusions, where the other options are named errors (correlation as
  cause, reversing a condition, counts instead of rates, a truncated axis).
- **Simulating:** counting outcomes from printed digits, and deciding from supplied simulation results.

Where the MAIN questions are choices, the set measures recognition (choosing the correct plot, design or conclusion),
not producing a drawing, a design or a written argument. The "Assessed response" column of `COVERAGE.md` says which
sets these are.

## Verification actually run for 1.1.0

- **Game answer checker (validation check 21).** All 573 short-answer keys were run through the game's own checker code
  (`packages/curriculum/src/answers.ts`, read-only) with `src/tools/checker_contract.ts`. All 573 are automatically
  checkable and accepted. The same answer without spaces, or with its terms reversed, is also accepted.
- **Fixed right and wrong responses (check 30).** 37 typed responses were run through the same checker. All 37 got the
  expected result (21 accepted, 16 rejected). These are the review's tests:
  - S1-M-Q1 "3; 5; 4" is rejected.
  - S15-M-Q1 with a and b swapped is rejected.
  - S26-M-Q1 with the selections reversed is rejected.
  - S48-F1-Q1 with P(X = 0) and P(X = 3) swapped is rejected.
  - S34-M-Q1 ".2; no" is rejected.
  - 5/4 is accepted and 4/5 rejected.

  The rest show how rounding and trailing zeros are handled. `VALIDATION.md` lists every response.
- **Importer, check mode.** `npx tsx tools/import-collection/import.ts --check <unzipped 1.1.0 package> <scratch folder>`
  read 54 sets and 1,435 questions: 0 invalid, 0 warnings, 0 drawn or interactive items (sa→short 573, mc 433, tf 429).
  It reported "CHECK ONLY: the bank is valid. Nothing was changed."
- **Importer, real run into a scratch folder** outside both repositories. It installed "Probability & Statistics bank
  version 1.1.0". The importer's own key conversion (`bankKey`) and the game checker were then applied to every imported
  short answer. All 573 are auto-checkable and accept their own key (98 with the form "simplified"), and no rewrite was
  rejected. The game repository was left unchanged (`git status` clean).
- **Automatic checks.** `src/validate.py`: 30 of 30 PASS. New in 1.1.0:
  - check 27: four-graph panels. 12 items are recomputed from the question text; S10-M-Q1 is checked for distinct panels
    only.
  - check 28: probability models stated, on 202 questions with a chance device, cards, guessing, payoffs or random
    selection
  - check 29: precision, on 20 short answers
  - check 30: fixed checker responses

  The multiple-choice length check (23) finds no strong cue, but the correct choice is still the uniquely longest in 162 of
  420 text items (39%; 25% would be chance).
- **Independent re-solve.** `src/resolve.py` recomputes 160 questions (246 values) from the givens with separate code: 0
  disagreements. S54-M-Q1 and S52-F1-Q4 were added for 1.1.0.
- **Hand work.** The author re-read and re-solved all 206 revised questions in their final form (`VALIDATION.md`,
  "Manual review", lists what that turned up). The 1,229 unchanged questions were **not** read again in 1.1.0; they were
  read in full for 1.0.0.
- **Figures.** The two changed figure pages (S2-M-Q2, S2-M-Q4) were rendered and inspected. Other figures are unchanged
  from 1.0.0, where all 190 were inspected.
- **Revision tracking.** The export compares every question with the 1.0.0 snapshot and stops on any change without an
  entry in `src/changes.py`. It reported 206 revised, 1,229 unchanged.
- **Letters.** No multiple-choice item changed its letter. All letters remain frozen in `src/choice_plan.json`.
- **Other collections.** The engine was not changed in 1.1.0, so no other collection was rebuilt.
- **Package.** `engine/verify_package.py` checks the 1.1.0 ZIP against `MANIFEST.json`: OK.

**Not done:** no test in the live game, no test with the AI grader, and no second human reviewer. The checks above show
what the content files and the game's checker code do with each key. They do not show how every possible student
wording will be graded.

## Assumptions and limitations

- **Choosing is not producing.** See "How construct, design, explain and simulate demands are assessed".
- **Student wording.** The checker accepts equivalent numbers. It was not tested on every way a student might write an
  answer, only on the key, the key without spaces, the key with terms reversed, and the 37 fixed responses of check 30.
- **Standards wording** was written from the published Common Core standards as recalled (the official site could not be
  opened from the authoring environment) and should be spot-checked.
- **Datasets** are synthetic, chosen to show the intended feature; they are not real measurements (`DATASETS.md`).
- **Supplied simulation results** (tables of simulated sets, re-randomization counts) are hypothetical, chosen to be
  close to the theoretical distribution. They were not produced by a simulation run. Questions that state such results
  say "(Hypothetical simulation results.)".
- **No game changes.** This release is content only. The game, grading engine, routing rules, database, UI and
  deployment were not changed. The game repository was only read.

## Rebuild

```
python3 question-bank/engine/build.py probability_statistics        # PDFs, JSON, CSV
python3 question-bank/engine/coverage.py probability_statistics     # COVERAGE.md
python3 question-bank/probability_statistics/src/validate.py         # VALIDATION.md and DATASETS.md (exit 1 on any failure; check 21 needs the game repository, NEXUS_DIR)
python3 question-bank/probability_statistics/src/resolve.py          # independent re-solve only
python3 question-bank/engine/export.py probability_statistics       # nexus/probability_statistics/ (sets, assets, PDFs in parts, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/Probability_Statistics_Nexus_Import_v1.1.0.zip
```
