# Algebra II — Question Collection (version 1.0.0)

The High School Algebra II collection for Untangle the Nexus. Algebra II is a course, not a grade, so the collection uses
course-placement labels, not grade levels. Everything is generated from one source, the data in `src/`, by
`question-bank/engine/`. The collection has its own directory and its own ID namespace (`A2`). It does not edit or depend
on any Algebra I or Geometry file; those courses appear only as standard codes in backward branches.

This release is for independent review before import. It has not been pushed, merged, published, or tried in the live game.

| File | Contents |
|---|---|
| `Algebra2_Question_Collection.pdf` | The questions, one per page (3,120 pages including set and branch title pages) |
| `Algebra2_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Algebra2_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `A2:S24-M-Q1`). Questions with a figure also carry `figure_svg`, `figure_png`, `figure_description`, and `figure_data` |
| `COVERAGE.md` | Course profile, inclusion/exclusion table, a matrix of every standard, subpart, and subskill with its MAIN sets and pages, the branch map of every set, and response types |
| `VALIDATION.md` | The 19 automatic checks, each with its result and its actual scope, plus the manual review record (read-through, fixes, figures, proofs, simulations) |
| `CHANGELOG.md` | Version 1.0.0 and the errors found and fixed before release |
| `PLAN.md` | The set list by authoring batch |
| `src/` | The single source: `standards.py` (inventory and subskills), `data_*.py` (sets), `grade.py` (course settings and grading rules), `simulations.py` (seeded simulations behind the histograms), `resolve.py` (independent re-solve), `validate.py`, `review_log.py` (manual review record), `coverage_report.py`, `history/` (the 1.0.0 snapshot that later revisions are compared with) |

The Untangle The Nexus import package is `question-bank/nexus/algebra2/`, zipped as
`question-bank/nexus/Algebra2_Nexus_Import_v1.0.0.zip`. Its README describes every field. The split PDFs (four parts of at
most 800 pages each) are in its `pdf/` folder with `PART_INDEX.md` (page and question ranges of each part), and
`MANIFEST.json` lists every file with its SHA-256 hash.

## Contents

- **84 question sets, 2,525 questions.**
  - **CORE strand (sets 1-72, 2,165 questions):** the 47 standards of the Common Core traditional-pathway Algebra II course
    (CCSS Mathematics, Appendix A), including the (+) standards the pathway lists itself (N-CN.8, N-CN.9, A-APR.5, A-APR.7,
    S-MD.6, S-MD.7). Their (+) marks are kept in `COVERAGE.md`.
  - **ADVANCED EXTENSION strand (sets 73-84, 360 questions):** 11 further official (+) standards that continue Algebra II
    topics (N-CN.3, F-IF.7d, F-BF.1c, F-BF.4b-d, F-BF.5, F-TF.3, F-TF.4, F-TF.6, F-TF.7). This strand is optional and is a
    decision of this bank, not an official placement. Every record carries `strand` = `core` or `advanced extension (+)`.
  - **Revisited Algebra I codes.** Some pathway codes are shared with Algebra I (for example A-SSE.2, A-CED.1, F-IF.4). Their
    Algebra II sets assess the new Algebra II demand (polynomial, rational, radical, exponential, logarithmic, and
    trigonometric cases), stated as REVISIT in the coverage matrix. When such a code is used as a backward branch, it is
    labeled Algebra I.
- **Subparts and subskills.** Each standard is split into the distinct demands its wording names (84 subskills). Each one is
  the declared focus (`covers`) of a set whose five MAIN questions test it. `COVERAGE.md` section 3 lists every subskill
  with its set and page. No standard or subskill is without a MAIN set.
- **Set structure.**
  - **MAIN:** five parallel questions on one target skill (`target_skill`). No MAIN has a true/false item. Sets whose
    subskill says prove or derive have shown-work MAIN items; sets whose subskill says graph have drawing MAIN items.
  - **BACKWARD 1..N:** 253 branches (83 sets have 3, one set has 4). Each branch has teacher metadata: the obstacle, why it
    blocks MAIN, the evidence its five questions collect, and whether its standard is an **exact** prerequisite (182) or the
    closest **supporting** standard (71).
  - **FORWARD 1 and FORWARD 2:** each states its progression type and its one new demand, and is marked direct or NEAREST
    RELATED (every forward branch in this release is direct). FORWARD 2 states how it builds on FORWARD 1.
    - FORWARD 1: same-course deepening 79, cross-standard extension 5
    - FORWARD 2: cross-standard extension 69, same-course deepening 8, later-course extension 7
- **No circular prerequisites.** A backward standard is a Grade K-8 standard, an Algebra I or Geometry standard, or the MAIN
  standard of an *earlier* Algebra II set. The build stops on anything else.
- **Question types:**
  - short answer 1,572
  - multiple choice 421 (A 106, B 105, C 105, D 105)
  - true/false 424 (207 True, 217 False), none in MAIN
  - shown work 53 (proofs, derivations, divisions, explanations)
  - drawing on a blank grid 50, drawing plus a written answer 5
  - 106 questions carry a figure (78 coordinate graphs or grids, 15 histograms, 13 tables); every figure has a text description.

## Answer forms and grading

- **Expressions and numbers** state the exact value or the precision. The grading note says "Form required" (for example
  factored, exact, a + bi, or rounded to a stated place) or "Any equivalent form". The game importer maps
  "Form required: factored" to its factored-form check.
- **Domains and extraneous solutions.** Keys of rational and radical items state excluded values and name any extraneous
  solution (or say none is extraneous).
- **Shown work** (`work`) has a sample answer in `correct_answer`, the method in `required_method`, and essential steps in the
  grading note.
- **Drawings** (`plot`, `plot_text`) list the features to check (intercepts, asymptotes, midline, period, end behavior,
  open or closed endpoints).
- **Multiple choice** has exactly one correct option; letters are dealt evenly by the engine.
- **Simulations.** The histograms of S64, S67, S68, and S69 come from the seeded script `src/simulations.py`.

## Verification actually run

- **Hand read-through.** All 2,525 questions were listed with their keys and re-solved by the author, set by set. After the
  stand-alone rewrites and the true/false rewrites, the 217 false-keyed statements and the rewritten stems were read again
  in their final form.
- **Independent re-solve.** `src/resolve.py` recomputes 265 questions (281 values) with sympy, from the givens, in code
  separate from the data modules: 0 disagreements.
- **Automatic checks.** `src/validate.py`: 19 of 19 PASS. Each row of `VALIDATION.md` states what the check covers and what
  it cannot show.
- **Figures.** All 106 figure pages were rendered from the question PDF and inspected by eye; pages changed after
  inspection were rendered and inspected again.
- **Importer check mode.** The Untangle The Nexus importer was run read-only, in check mode, on the exported package
  (`npx tsx tools/import-collection/import.ts --check <package> <scratch folder>`): 2,525 questions read, 0 invalid,
  "CHECK ONLY: the bank is valid. Nothing was changed." This shows the files pass the importer's checks. It is **not** a
  test in the live game or with the AI grader; neither was done.
- **Package.** `engine/verify_package.py` checks the ZIP against `MANIFEST.json` (every file present, every SHA-256 equal).

## Assumptions and limitations

- **Standards wording and placement.** The official standards site could not be opened from the authoring environment
  because of its network policy. The standards text in `src/standards.py` and the Appendix A placement were written from the
  published standards as recalled. They should be spot-checked against the official documents.
- **Course placement of related standards.** Forward standards outside Algebra II are labeled with the course this bank
  places them in (`engine/hs_courses.py`): Probability & Statistics (S-CP, S-MD.A) or Precalculus. Appendix A places S-CP in
  Geometry; this bank does not (see `COVERAGE.md` section 2).
- **Supplied data.** Some simulation summaries stated in text (for example "62 of 200 re-randomizations") are supplied data
  chosen to be plausible, not output of a simulation run. The histogram figures are simulation output.
- **Review.** All review was done by the author. No second person has checked the questions or keys.
- **Grading support.** Shown work and drawings need a person or a drawing surface. Equivalent-form answers need a checker
  that accepts equivalent expressions.
- **No game changes.** This release is content only. The engine, routing rules, database, UI, and deployment were not
  changed.

## Rebuild

```
python3 question-bank/engine/build.py algebra2        # PDFs, JSON, CSV
python3 question-bank/engine/coverage.py algebra2     # COVERAGE.md
python3 question-bank/algebra2/src/validate.py         # VALIDATION.md (exit 1 on any failure)
python3 question-bank/algebra2/src/resolve.py          # independent re-solve only
python3 question-bank/engine/export.py algebra2       # nexus/algebra2/ (sets, assets, PDFs in parts, BRANCH_MAP.json, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/Algebra2_Nexus_Import_v1.0.0.zip
```
