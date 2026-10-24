# Probability & Statistics — Question Collection (version 1.0.0)

The High School Probability & Statistics collection for Untangle the Nexus. Probability & Statistics is a course, not a
grade (students usually take it in grade 10, 11 or 12), so the collection uses course-placement labels, not grade
levels. Everything is generated from one source, the data in `src/`, by `question-bank/engine/`. The collection has its
own directory and its own ID namespace (`PS`). It does not edit, import or depend on any Algebra I, Geometry or Algebra II
file; those courses appear only as standard codes in backward branches.

**Every question is graded automatically by the game.** Question types are short answer, multiple choice and
true/false only, and every short-answer key was run through the game's own answer checker.

This release is for independent review before import. It has not been pushed, merged, published, or tried in the live
game.

| File | Contents |
|---|---|
| `Probability_Statistics_Question_Collection.pdf` | The questions, one per page (1,781 pages including set and branch title pages) |
| `Probability_Statistics_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Probability_Statistics_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `PS:S12-B2-Q3`). Questions with a figure also carry `figure_svg`, `figure_png`, `figure_description`, and `figure_data` |
| `COVERAGE.md` | The course profile, the overlap with the Algebra I, Geometry and Algebra II collections, a matrix of every standard and subskill with its MAIN sets, pages and **assessed response**, the branch map, and response types |
| `DATASETS.md` | Every dataset used: values, size, units, context. All are synthetic (written for this collection) |
| `VALIDATION.md` | The 26 automatic checks, each with its result and its actual scope, plus the manual review record |
| `CHANGELOG.md` | Version history by question ID (1.0.0 is the first release) |
| `PLAN.md` | The set list by authoring batch |
| `src/` | The single source: `standards.py` (inventory and subskills), `data_*.py` (sets), `datasets.py` (dataset registry), `common.py` (statistics and figure helpers), `grade.py` (course settings and grading rules), `resolve.py` (independent re-solve), `validate.py`, `tools/checker_contract.ts` (runs the game's answer checker), `review_log.py`, `coverage_report.py`, `choice_plan.json` (frozen multiple-choice letters), `history/` (the 1.0.0 snapshot for future revision tracking) |

The Untangle The Nexus import package is `question-bank/nexus/probability_statistics/`, zipped as
`question-bank/nexus/Probability_Statistics_Nexus_Import_v1.0.0.zip`. Its README describes every field. The split PDFs
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
- **Question types:** short answer 573; multiple choice 433 (A 111, B 107, C 110, D 105); true/false 429 (227 True,
  202 False), none in MAIN. 190 questions carry a figure: 125 tables (data tables, two-way tables, normal tables,
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
  nearest tenth", "four decimal places"). A rounded answer must be given to exactly that precision.
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

## Verification actually run

- **Game answer checker (validation check 21).** Every one of the 573 short-answer keys was run through the game's own
  checker code (`packages/curriculum/src/answers.ts`, read-only) with `src/tools/checker_contract.ts`. All 573 are
  automatically checkable and accepted. The same answer written without spaces, or with its terms in reverse order, is
  also accepted.
- **Importer, check mode.** `npx tsx tools/import-collection/import.ts --check <unzipped package> <scratch folder>`
  resolved the course to the game's existing Probability & Statistics course (code 104) and read 54 sets and 1,435
  questions: 0 invalid, 0 warnings, 0 drawn or interactive items (sa→short 573, mc 433, tf 429). It reported "CHECK ONLY:
  the bank is valid. Nothing was changed."
- **Importer, real run into a scratch folder** outside both repositories. The importer's own key conversion (`bankKey`)
  and the game checker were then applied to every imported short answer: all 573 are auto-checkable and accept their own
  key (98 carry the form "simplified", from questions that ask for lowest terms), and no rewrite (no spaces, reversed
  terms) was rejected. The game repository was left unchanged (`git status` clean).
- **Automatic checks.** `src/validate.py`: 26 of 26 PASS. Among them: structure and IDs, coverage of every standard and
  subskill, branch rules, answer-key completeness, balance, duplicates, stand-alone questions, PDF pages, labels, the game
  checker (21), clean keys (22), multiple-choice length cue (23), statistics conventions on the page (24), fractions in
  lowest terms and probabilities in [0, 1] (25), datasets documented (26).
- **Independent re-solve.** `src/resolve.py` recomputes 158 questions (243 values) from the givens with Python's
  statistics, fractions and math modules, typed in again (no data-module code or key strings reused): 0 disagreements.
- **Hand work.** The author re-solved all 1,435 questions in one read-through after the build, checking every
  multiple-choice option and every true/false statement. The problems found and fixed are listed in `VALIDATION.md`.
- **Figures.** All 190 figure pages were rendered and inspected; layout fixes were made and the changed pages
  inspected again.
- **Letters.** Every multiple-choice letter is frozen in `src/choice_plan.json` (the rebuild with the plan is identical),
  so future revisions will not move unchanged items.
- **Other collections.** The engine changed in small ways (the Probability & Statistics placement rules in
  `engine/hs_courses.py`; an optional title, outliers and a compact mode for box plots and histograms in
  `engine/render.py`; `DATASETS.md` in the export). All nine other engine-built collections (Grades 3-8, Algebra I,
  Geometry, Algebra II) were rebuilt: their answer keys (JSON and CSV) are byte-identical to the committed files, and
  their PDFs have the same page text and drawings as the committed PDFs, except Grade 6 (3 pages, drawings) and Grade 8
  (5 pages, text). Those two were also rebuilt with the engine from before this work, and that build matches today's
  build page for page, so the difference is in the older committed PDFs, not in this change. The committed files were
  left as they were. Financial Literacy uses its own builder, which does not use the changed modules.
- **Package.** `engine/verify_package.py` checks the ZIP against `MANIFEST.json`: OK.

**Not done:** no test in the live game, no test with the AI grader, and no second human reviewer. The checks above show
what the content files and the game's checker code do with each key. They do not show how every possible student
wording will be graded.

## Assumptions and limitations

- **Choosing is not producing.** See "How construct, design, explain and simulate demands are assessed".
- **Student wording.** The checker accepts equivalent numbers. It was not tested on every way a student might write an
  answer, only on the key, the key without spaces, and the key with terms reversed.
- **Standards wording** was written from the published Common Core standards as recalled (the official site could not be
  opened from the authoring environment) and should be spot-checked.
- **Datasets** are synthetic, chosen to show the intended feature; they are not real measurements (`DATASETS.md`).
- **Supplied simulation results** (tables of simulated sets, re-randomization counts) are chosen to be close to the
  theoretical distribution; they were not produced by a simulation run.
- **No game changes.** This release is content only. The game, grading engine, routing rules, database, UI and
  deployment were not changed. The game repository was only read.

## Rebuild

```
python3 question-bank/engine/build.py probability_statistics        # PDFs, JSON, CSV
python3 question-bank/engine/coverage.py probability_statistics     # COVERAGE.md
python3 question-bank/probability_statistics/src/validate.py         # VALIDATION.md and DATASETS.md (exit 1 on any failure; check 21 needs the game repository, NEXUS_DIR)
python3 question-bank/probability_statistics/src/resolve.py          # independent re-solve only
python3 question-bank/engine/export.py probability_statistics       # nexus/probability_statistics/ (sets, assets, PDFs in parts, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/Probability_Statistics_Nexus_Import_v1.0.0.zip
```
