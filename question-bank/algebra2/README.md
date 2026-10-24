# Algebra II — Question Collection (version 1.1.0)

The High School Algebra II collection for Untangle the Nexus. Algebra II is a course, not a grade, so the collection uses
course-placement labels, not grade levels. Everything is generated from one source, the data in `src/`, by
`question-bank/engine/`. The collection has its own directory and its own ID namespace (`A2`). It does not edit or depend
on any Algebra I or Geometry file; those courses appear only as standard codes in backward branches.

**What changed in 1.1.0:** no question needs a person or a drawing surface to grade. The 108 questions of that kind in
1.0.0 are now multiple choice: 53 shown-work items (proofs, derivations, explanations, divisions), 50 drawing items, and 5
drawing-plus-equation items. Their IDs are unchanged. `CHANGELOG.md` lists every one, and `revisions.json` in the import
package maps all 2,525 IDs.

This release is for independent review before import. It has not been pushed, merged, published, or tried in the live game.

| File | Contents |
|---|---|
| `Algebra2_Question_Collection.pdf` | The questions, one per page (3,120 pages including set and branch title pages) |
| `Algebra2_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Algebra2_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `A2:S24-M-Q1`). Questions with a figure also carry `figure_svg`, `figure_png`, `figure_description`, and `figure_data` |
| `COVERAGE.md` | Course profile, inclusion/exclusion table, a matrix of every standard, subpart, and subskill with its MAIN sets and pages, the branch map of every set, and response types |
| `VALIDATION.md` | The 20 automatic checks, each with its result and its actual scope, plus the manual review record (read-through, fixes, figures, proofs, simulations) |
| `CHANGELOG.md` | Version 1.1.0 by question ID, followed by the 1.0.0 release notes |
| `PLAN.md` | The set list by authoring batch |
| `src/` | The single source: `standards.py` (inventory and subskills), `data_*.py` (sets), `common.py` (graph helpers, including the four-graph choice figure), `grade.py` (course settings and grading rules), `simulations.py` (seeded simulations behind the histograms), `resolve.py` (independent re-solve), `validate.py`, `review_log.py` (manual review record), `coverage_report.py`, `changes.py` (the 1.1.0 revision map), `choice_plan.json` (frozen multiple-choice letters, so published letters do not move), `history/` (the 1.0.0 snapshot and release notes) |

The Untangle The Nexus import package is `question-bank/nexus/algebra2/`, zipped as
`question-bank/nexus/Algebra2_Nexus_Import_v1.1.0.zip` (the 1.0.0 ZIP is kept next to it). Its README describes every
field. The split PDFs (four parts of at most 800 pages each) are in its `pdf/` folder with `PART_INDEX.md`, and
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
  - **MAIN:** five parallel questions on one target skill (`target_skill`). No MAIN has a true/false item. In sets whose
    subskill says prove, derive, or explain, MAIN questions are multiple choice between a valid argument and flawed ones (or
    short answers). In sets whose subskill says graph, all five MAIN questions show four candidate graphs labeled A to D.
  - **BACKWARD 1..N:** 253 branches (83 sets have 3, one set has 4). Each branch has teacher metadata: the obstacle, why it
    blocks MAIN, the evidence its five questions collect, and whether its standard is an **exact** prerequisite (182) or the
    closest **supporting** standard (71).
  - **FORWARD 1 and FORWARD 2:** each states its progression type and its one new demand, and is marked direct or NEAREST
    RELATED (every forward branch in this release is direct). FORWARD 2 states how it builds on FORWARD 1.
    - FORWARD 1: same-course deepening 79, cross-standard extension 5
    - FORWARD 2: cross-standard extension 69, same-course deepening 8, later-course extension 7
- **No circular prerequisites.** A backward standard is a Grade K-8 standard, an Algebra I or Geometry standard, or the MAIN
  standard of an *earlier* Algebra II set. The build stops on anything else.
- **Question types (no type needs a person or a drawing surface to grade):**
  - short answer 1,572
  - multiple choice 529 (A 132, B 133, C 132, D 132)
  - true/false 424 (207 True, 217 False), none in MAIN
  - 106 questions carry a figure: 55 four-graph choice figures, 23 other coordinate graphs, 15 histograms, 13 tables. Every
    figure has a text description; the descriptions of the four-graph figures describe each graph by its features, not by its
    equation, so they do not give the answer away.

## Answer forms and grading

- **Expressions and numbers** (short answer) state the exact value or the precision. The grading note says "Form required"
  (for example factored, exact, a + bi, or rounded to a stated place) or "Any equivalent form". The game importer maps
  "Form required: factored" to its factored-form check.
- **Domains and extraneous solutions.** Keys of rational and radical items state excluded values and name any extraneous
  solution (or say none is extraneous).
- **Proofs, derivations, explanations** are multiple choice. The keyed choice is a complete, valid argument; each other choice
  is a flawed argument (checking a few values, an invalid algebra step, assuming the result, a false fact, the wrong
  reflection). The grading note says what is wrong with each other choice.
- **Graphs** are multiple choice. One figure shows four graphs labeled A to D on the same window (asymptotes and midlines
  dashed, holes and excluded endpoints as open circles); the choices are "Graph A" to "Graph D". The other graphs show common
  errors (shift direction, reflection, multiplicity, asymptote, period, endpoint circles), and the note names them.
- **Multiple choice** has exactly one correct option. Letters are balanced; the "Graph A-D" letters were placed by hand, and
  all other letters are dealt by the engine from a plan frozen in `src/choice_plan.json`.
- **Simulations.** The histograms of S64, S67, S68, and S69 come from the seeded script `src/simulations.py`.

## Verification actually run

- **Hand read-through.** In 1.0.0, all 2,525 questions were listed with their keys and re-solved by the author, set by set.
  In 1.1.0, the 108 rewritten questions were solved again in their final form: the keyed choice confirmed correct and every
  other choice confirmed wrong for the reason its note names. This found one error in 1.0.0 (S42-F1-Q2 asked for an
  impossible cubic), now corrected.
- **Independent re-solve.** `src/resolve.py` recomputes 265 questions (281 values) with sympy, from the givens, in code
  separate from the data modules: 0 disagreements.
- **Automatic checks.** `src/validate.py`: 20 of 20 PASS, including the new check that every question is short answer,
  multiple choice, or true/false. Each row of `VALIDATION.md` states what the check covers and what it cannot show.
- **Figures.** All 106 figure pages were rendered from the question PDF and inspected by eye. For the 55 four-graph
  figures, every panel was checked against its own equation and the keyed panel against the question.
- **Importer check mode.** The Untangle The Nexus importer was run read-only, in check mode, on the unzipped 1.1.0 package
  (`npx tsx tools/import-collection/import.ts --check <package> <scratch folder>`): 2,525 questions read, 0 invalid (1,572 short answer, 529 multiple choice, 424 true/false; 0 drawn or interactive-graph items), "CHECK ONLY: the bank is valid. Nothing was changed."
  This shows the files pass the importer's checks. It is **not** a test in the live game or with the AI grader; neither was
  done.
- **Package.** `engine/verify_package.py` checks the ZIP against `MANIFEST.json` (every file present, every SHA-256 equal).

## Assumptions and limitations

- **Choosing is not producing.** A multiple-choice proof or graph shows that a student can recognize a valid argument or the
  correct graph among likely errors. It is weaker evidence than writing the proof or drawing the graph unaided. This is the
  trade-off for grading every question without a person.
- **Short answers** still need a checker that accepts equivalent forms (for example 2√3 and √12). Explanations that remain
  short answer (for example in S33 and S66) are graded against the key's essential points.
- **Standards wording and placement.** The official standards site could not be opened from the authoring environment
  because of its network policy. The standards text in `src/standards.py` and the Appendix A placement were written from the
  published standards as recalled. They should be spot-checked against the official documents.
- **Course placement of related standards.** Forward standards outside Algebra II are labeled with the course this bank
  places them in (`engine/hs_courses.py`): Probability & Statistics (S-CP, S-MD.A) or Precalculus. Appendix A places S-CP in
  Geometry; this bank does not (see `COVERAGE.md` section 2).
- **Supplied data.** Some simulation summaries stated in text (for example "62 of 200 re-randomizations") are supplied data
  chosen to be plausible, not output of a simulation run. The histogram figures are simulation output.
- **Review.** All review was done by the author. No second person has checked the questions or keys.
- **No game changes.** This release is content only. The game, routing rules, database, UI, and deployment were not changed.
  Two small additions were made to this repository's own PDF engine for the new figures (a panel letter and a title above a
  coordinate grid, used only when a figure asks for them, and one fixed choice order, Graph A-D). All eight other collections (Grades 3-8, Algebra I, Geometry) were rebuilt with the changed engine: their answer keys are byte-identical to the committed files, and every PDF page has the same text and drawings as a build with the previous engine.

## Rebuild

```
python3 question-bank/engine/build.py algebra2        # PDFs, JSON, CSV
python3 question-bank/engine/coverage.py algebra2     # COVERAGE.md
python3 question-bank/algebra2/src/validate.py         # VALIDATION.md (exit 1 on any failure)
python3 question-bank/algebra2/src/resolve.py          # independent re-solve only
python3 question-bank/engine/export.py algebra2       # nexus/algebra2/ (sets, assets, PDFs in parts, revisions.json, CHANGELOG.md, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/Algebra2_Nexus_Import_v1.1.0.zip
```
