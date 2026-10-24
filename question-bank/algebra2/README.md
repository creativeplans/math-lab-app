# Algebra II — Question Collection (version 1.2.0)

The High School Algebra II collection for Untangle the Nexus. Algebra II is a course, not a grade, so the collection uses
course-placement labels, not grade levels. Everything is generated from one source, the data in `src/`, by
`question-bank/engine/`. The collection has its own directory and its own ID namespace (`A2`). It does not edit or depend
on any Algebra I or Geometry file; those courses appear only as standard codes in backward branches.

**What changed in 1.2.0:** every question, MAIN and every branch, is graded automatically by the game.

- 454 short answers that only a person (or exact wording) could grade are now multiple choice or true/false. Explanations,
  interpretations, study designs and evaluations of claims became "choose the valid argument" items, whose other choices
  are specific flaws named in the grading note.
- The other 418 changed short answers got a checkable contract: one answer line per part, the precision or form stated in
  the question, and a key with no commentary. Every short-answer key was run through the game's own answer checker.
- The reviewer's corrections were applied: statistics conventions stated in each question, specific mathematical fixes,
  and missing givens added.
- A new focused set, **S85 Graph step functions** (HSF-IF.C.7.b), was added with a fixed number, so no earlier ID moved.
- The engine's rules for drawings, shown work, partial credit and "any reasonable wording" no longer apply to this
  collection; `src/grade.py` supplies its own grading rules.

`CHANGELOG.md` lists every changed ID (910 revised, 30 new, 0 retired) with the finding behind it. The permanent authoring
rule is in `question-bank/AUTO_GRADING_RULES.md`; it also applies to future Geometry work.

This release is for independent review before import. It has not been pushed, merged, published, or tried in the live game.

| File | Contents |
|---|---|
| `Algebra2_Question_Collection.pdf` | The questions, one per page (3,157 pages including set and branch title pages) |
| `Algebra2_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Algebra2_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `A2:S24-M-Q1`). Questions with a figure also carry `figure_svg`, `figure_png`, `figure_description`, and `figure_data` |
| `COVERAGE.md` | The declared course profile, the inclusion/exclusion table, a matrix of every standard and subskill with its MAIN sets, pages and **assessed response** (typed answer, graph choice, other multiple choice), the branch map, and response types |
| `VALIDATION.md` | The 23 automatic checks, each with its result and its actual scope, plus the manual review record |
| `CHANGELOG.md` | Version 1.2.0 by question ID, followed by the 1.1.0 and 1.0.0 release notes |
| `PLAN.md` | The set list by authoring batch |
| `src/` | The single source: `standards.py`, `data_*.py` (sets), `common.py` (graph helpers), `grade.py` (course settings and grading rules), `simulations.py`, `resolve.py` (independent re-solve), `validate.py`, `tools/checker_contract.ts` (runs the game's answer checker), `review_log.py`, `coverage_report.py`, `changes.py` (the 1.2.0 revision map), `choice_plan.json` (frozen multiple-choice letters), `history/` (the 1.0.0 and 1.1.0 snapshots and earlier release notes) |

The Untangle The Nexus import package is `question-bank/nexus/algebra2/`, zipped as
`question-bank/nexus/Algebra2_Nexus_Import_v1.2.0.zip` (the 1.0.0 and 1.1.0 ZIPs are kept next to it). Its README describes
every field. The split PDFs (four parts of at most 800 pages each) are in its `pdf/` folder with `PART_INDEX.md`, and
`MANIFEST.json` lists every file with its SHA-256 hash.

## Contents

- **85 question sets, 2,555 questions.**
  - **CORE strand (sets 1-72 and 85, 2,195 questions):** the 47 standards of the Common Core traditional-pathway Algebra II
    course (CCSS Mathematics, Appendix A), including the (+) standards the pathway lists itself (N-CN.8, N-CN.9, A-APR.5,
    A-APR.7, S-MD.6, S-MD.7).
  - **ADVANCED EXTENSION strand (sets 73-84, 360 questions):** 11 further official (+) standards. This strand is optional and
    is a decision of this bank, not an official placement. Every record carries `strand`.
  - **Declared course profile.** The collection covers the course profile declared in `COVERAGE.md`, not every possible
    Algebra II course. Which standards a school teaches in Algebra II, and in what order, is a program decision.
    HSF-IF.C.8.a (completing the square for quadratics) is excluded from Algebra II MAIN sets in this profile; the exclusion
    is listed in `COVERAGE.md` section 2.
- **Subskills.** Each standard is split into the distinct demands its wording names (85 subskills). Each one is the focus of
  a set whose five MAIN questions test it.
- **Set structure.**
  - **MAIN:** five parallel questions on one target skill. No MAIN has a true/false item.
  - **BACKWARD 1..N:** 256 branches (84 sets have 3, one has 4), each with teacher metadata; 183 exact and 73 supporting
    prerequisites.
  - **FORWARD 1 and FORWARD 2:** each states its progression type and new demand; FORWARD 2 states how it builds on FORWARD 1.
- **No circular prerequisites.** A backward standard is a K-8, Algebra I or Geometry standard, or the MAIN standard of an
  *earlier* Algebra II set. The build stops on anything else.
- **Question types:**
  - short answer 1,128
  - multiple choice 996 (A 249, B 248, C 253, D 246)
  - true/false 431 (213 True, 218 False), none in MAIN
  - 111 questions carry a figure: 60 four-graph choice figures, 23 other coordinate graphs, 15 histograms, 13 tables.

## How each question is graded (the contract with the game)

- **Multiple choice and true/false:** the chosen letter is compared with `correct_letter`. Each multiple-choice item has
  exactly one correct option; its grading note says what is wrong with each other option.
- **Short answer:** the game's answer checker compares the response with `correct_answer`. Each question has one answer
  line per part. It states the form (exact, a + bi, factored, fraction) and the precision ("to the nearest hundredth"); a
  rounded answer must be given to exactly that precision. Lists of values use set keys, so any order is accepted.
- **Word answers** appear only when the question lists the allowed words ("Answer Yes or No", "Answer Positive or
  Negative", "enter none if there are none").
- **Formulas the checker cannot compare reliably** are multiple choice, or the question asks for numeric parameters. This
  covers radical, logarithmic, trigonometric and inverse-function formulas, intervals, and interpretations.
- **Graphs** are multiple choice: four candidate graphs labeled A to D on one window.
- **Statistics** questions state their own model and conventions: the null model, the tail counted, the 5% cutoff, the
  margin of error as 2 standard deviations, independence, and fair devices. A common result is called consistent with the
  model, never proof.

## Verification actually run for 1.2.0

- **Game answer checker (validation check 21).** Every one of the 1,128 short-answer keys was run through the game's own
  checker code (`packages/curriculum/src/answers.ts`, read-only) with `src/tools/checker_contract.ts`. All 1,128 are
  automatically checkable and accepted. The same answer written without spaces, or with its terms in reverse order, is also
  accepted. The one documented exception is S1-M-Q4, which requires the a + bi order.
- **Importer, check mode.** `npx tsx tools/import-collection/import.ts --check <unzipped 1.2.0 package> <scratch folder>`
  read 85 sets and 2,555 questions: 0 invalid, 0 warnings, 0 drawn or interactive items (sa→short 1,128, mc 996, tf 431).
  It reported "CHECK ONLY: the bank is valid. Nothing was changed."
- **Importer, real run into a scratch folder.** The same package was imported into a scratch folder outside both
  repositories. The game repository was left unchanged.
  - The importer's own key conversion (`bankKey`) and the game checker were then applied to every imported short answer.
    All 1,128 are auto-checkable and accept their own key.
  - Rewrite test: the same answer without spaces or with terms reversed was rejected only for S1-M-Q4 (as above).
- **Automatic checks.** `src/validate.py`: 23 of 23 PASS. New in 1.2.0:
  - check 21: the game checker
  - check 22: clean keys, one key part per answer line, and word answers only from options the question lists
  - check 23: the correct choice is never much longer than the others. It is still the uniquely longest choice in 33% of
    text multiple-choice items, where 25% would be chance.
- **Independent re-solve.** `src/resolve.py` recomputes 261 questions (281 values) with sympy from the givens: 0
  disagreements. The cases for questions whose answer format changed were updated to the new format and still compute the
  value from the givens.
- **Hand work.** The author solved the 910 revised and 30 new questions while rewriting them, and recomputed computed values
  in Python. Every question named in the review's correction report was re-read in its final form. There was **no**
  separate second read-through of all 2,555 questions in 1.2.0.
- **Figures.** The five new step-function figures (S85-M, pages 1754-1758) were rendered and inspected. Other figures are
  unchanged from 1.1.0, where all were inspected.
- **Unchanged letters.** No multiple-choice item whose choices are unchanged since 1.1.0 changed its letter. Every
  current letter is frozen in `src/choice_plan.json`.
- **Other collections.** The engine changed in two small ways:
  - a collection may supply its own base grading rules
  - the revision tracker can compare with a snapshot of any earlier version

  All eight other built collections (Grades 3-8, Algebra I, Geometry) were rebuilt. Their answer keys are byte-identical to
  the committed files, and their PDFs have the same page text and drawings as builds with the previous engine. The committed
  Grade 6 and Grade 8 PDFs differ from both builds, because they were made with an older engine version; this predates this
  release. They were left as committed.
- **Package.** `engine/verify_package.py` checks the ZIP against `MANIFEST.json`.

**Not done:** no test in the live game, no test with the AI grader, and no second human reviewer. The checks above show
what the content files and the game's checker code do with each key. They do not show how every possible student wording
will be graded.

## Assumptions and limitations

- **Choosing is not producing.** Where a standard asks students to construct, sketch, prove or explain, the questions ask
  them to choose the correct graph or the valid argument. `COVERAGE.md` records this as the assessed response
  ("recognition") for each subskill.
- **Student wording.** The checker accepts equivalent numbers and polynomial or rational expressions. It was not tested on
  every way a student might write an answer, only on the key, the key without spaces, and the key with terms reversed.
- **Standards wording and placement** were written from the published standards as recalled (the official site could not
  be opened from the authoring environment) and should be spot-checked.
- **Supplied data.** Some simulation summaries stated in text are supplied data chosen to be plausible; the histograms are
  simulation output (`src/simulations.py`).
- **No game changes.** This release is content only. The game, grading engine, routing rules, database, UI and deployment
  were not changed. The game repository was only read.

## Rebuild

```
python3 question-bank/engine/build.py algebra2        # PDFs, JSON, CSV
python3 question-bank/engine/coverage.py algebra2     # COVERAGE.md
python3 question-bank/algebra2/src/validate.py         # VALIDATION.md (exit 1 on any failure; check 21 needs the game repository, NEXUS_DIR)
python3 question-bank/algebra2/src/resolve.py          # independent re-solve only
python3 question-bank/engine/export.py algebra2       # nexus/algebra2/ (sets, assets, PDFs in parts, revisions.json, CHANGELOG.md, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/Algebra2_Nexus_Import_v1.2.0.zip
```
