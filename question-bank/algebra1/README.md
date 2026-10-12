# Algebra I — Question Collection (version 2.0.0)

The first high-school course collection for Untangle the Nexus. Algebra I is a course, not a grade: students take it
in Grade 7, 8, 9, or later, so the collection has no grade level. Generated from the data in `src/` by
`question-bank/engine/`, with the same structure, file formats, and checks as the Grade 3-8 collections.

| File | Contents |
|---|---|
| `Algebra1_Question_Collection.pdf` | The questions, one per page (2,610 pages) |
| `Algebra1_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Algebra1_Answer_Key.json` / `.csv` | Machine-readable key, one record per question ID (with `uid`, for example `ALG1:S24-M-Q1`) |
| `CORRECTIONS.md` | Every finding of the v1.0.0 review (54 codes) and how it was fixed, with the question IDs changed |
| `CHANGELOG.md` | One row per question ID that changed from v1.0.0 (revised or new); unchanged IDs are omitted |
| `COVERAGE.md` | Coverage report: every Algebra I standard with question counts, the performance each set tests, difficulty distribution, prerequisite and forward relationships, questions that need drawing, figures, or a calculator, and known gaps and limitations |

The Untangle The Nexus import package is `question-bank/nexus/algebra1/`, zipped as
`question-bank/nexus/Algebra1_Nexus_Import_v2.0.0.zip`. Its own README describes every field.

## Contents

- **84 question sets, 2,100 questions**, covering all 60 standards of the Common Core traditional-pathway Algebra I
  course (CCSS Appendix A), listed in `engine/hs_courses.py`:
  - N-RN, N-Q
  - A-SSE, A-APR.A.1, A-CED, A-REI
  - F-IF, F-BF, F-LE
  - S-ID (except S-ID.A.4)

  Large standards have more than one set: N-RN.B.3, A-SSE.A.2, A-REI.C.6, F-IF.C.7.b, and S-ID.A.1 (3 each);
  A-APR.A.1, A-CED.A.1, A-REI.B.3, A-REI.B.4.a, A-REI.B.4.b, A-REI.C.5, A-REI.C.7, F-IF.B.4, F-IF.B.6, F-IF.C.7.a,
  F-BF.A.1.a, F-BF.A.2, F-BF.B.3, and S-ID.B.6.a (2 each).
- **New in 2.0.0: sets S69-S84** (16 sets, 400 questions), added for review findings:
  - S69, S70: irrationality proofs (3√7, ax) and closure of the rational numbers (N-RN.B.3)
  - S71: deriving the quadratic formula (A-REI.B.4.a); S72: proving the elimination equivalence (A-REI.C.5)
  - S73: graphing line-parabola and line-circle systems (A-REI.C.7); S84: solving linear systems by graphing (A-REI.C.6)
  - S74: square root and cube root graphs; S75: piecewise and step functions (F-IF.C.7.b)
  - S76: histograms from raw data; S77: box plots from raw data (S-ID.A.1)
  - S78: sketching graphs from verbal descriptions (F-IF.B.4); S79: average rate of change from graphs (F-IF.B.6)
  - S80: quadratic models (F-BF.A.1.a); S81: recursive and explicit rules (F-BF.A.2); S82: graphing transformations
    (F-BF.B.3); S83: scatter plots from paired data (S-ID.B.6.a)

  S3 now focuses on the sum proof and S43 on absolute value graphs. Existing question IDs were kept; the new sets
  have new IDs.
- **Each set** has:
  - MAIN: five Algebra I questions.
  - Two backward branches: Grade K-8 standards (mostly Grades 6-8), or an Algebra I standard that an earlier set
    teaches.
  - FORWARD 1 and FORWARD 2: standards of Geometry, Algebra II, Probability & Statistics, or Precalculus.

  Every branch has five questions.
- **Standard labels.**
  - Forward standards are labeled with the course this bank places them in, for example
    "High School — Algebra II (course placement in this bank)". They are never labeled as Algebra I standards.
  - Those collections do not exist yet, so a forward branch carries only its standard code and course name, with no
    reference to a missing file.
- **Response types:**

  | Type | Questions |
  |---|---:|
  | Short answer | 836 |
  | Multiple choice | 420 |
  | True/false | 743 |
  | Answer with required work | 36 |
  | Drawing | 49 |
  | Drawing + written answer | 16 |

  True/false keys: 372 true and 371 false. Multiple-choice correct letters: A 104, B 106, C 103, D 107.
- **Difficulty.** There is no difficulty field, as in Grades 3-8. Difficulty follows the section:

  backward review < MAIN < FORWARD 1 ≤ FORWARD 2

  FORWARD 2 is never in an earlier course than FORWARD 1, and the build enforces this.
- **Nearest related branches.** A forward branch that does not directly continue its MAIN skill is marked "nearest
  related" (`nearest_related: true`, 80 questions in 16 branches). Its heading page and the new branch field
  `nearest_connection` state how it connects to the MAIN skill; `COVERAGE.md` Section 5 lists them.
- **Algebra I depth.** The MAIN sections include:
  - multistep and literal equations, and compound inequalities
  - systems with zero, one, or infinitely many solutions
  - line-parabola and line-circle systems
  - completing the square and deriving the quadratic formula
  - the discriminant
  - rational exponents and irrationality proofs
  - residuals and correlation
  - written proofs (elimination, equal differences and equal factors)

## Answer forms and grading

Every written answer's `grading_note` begins with one of two kinds of statement:

- **"Form required: …"** (417 questions). Only the stated form earns full credit, and the question says which form:
  - expand, or factor completely
  - standard, vertex, or slope-intercept form
  - a + bi
  - exact, or rounded to a stated place
  - both solutions
  - an equation and its solution
- **"Any …"** (526 questions). For example "Any equivalent form", "Any equivalent wording", or "Any correct graph". It
  says what else is accepted, for example the units or rounding allowed.

After this statement comes the explanation, which can be shown to the student as feedback.

The extra Algebra I grading rules in `index.json` also cover:

- solution sets: every root, in any order
- inequalities written either way round
- systems answered as an ordered pair or as x = …, y = …
- "no solution" and "all real numbers"

**Known limitation: the game's answer checker has not been seen.** Questions marked "Any equivalent form" need a checker
that recognizes equivalent expressions (2.5 and 5/2; 4(0.5)^x and 4(1/2)^x) or a teacher. Do not assume symbolic
checking until it is tested. Questions answered by multiple choice or true/false need no such support.

## Changes to the format (all additive)

Nothing in the Grade 3-8 schema was removed or renamed, and the Grade 3-8 keys and packages are unchanged.

- **Course identity.** `collection` gains `course` (`"Algebra I"`) and `grade` is `null`. IDs are `ALG1:S…`.
- **High-school standard fields.** For high-school standards, `standard_grade` is `"HS"` and the new field
  `standard_course` names the course placement. The old fields could not say this: the Grade 7-8 packages placed
  high-school standards at "Grade 9/10".
- **Nearest connection (2.0.0).** In the import package, forward branches marked nearest related carry
  `nearest_connection`, one sentence naming the link to the MAIN skill. Other branches do not have the field.
- **Exponents.** Course PDFs typeset `x^(1/2)` and `5^(t/5)` as raised exponents. The JSON keeps the `^` text.
- **Build checks (course mode).** The build stops if:
  - a MAIN standard is not an Algebra I standard
  - a backward branch uses a high-school standard that no earlier set teaches
  - a forward branch uses an Algebra I standard
  - FORWARD 2 is in an earlier course than FORWARD 1
  - a question has no explanation

## Known limitations (also in `COVERAGE.md`)

- **Standards list.**
  - CCSS Appendix A could not be downloaded during authoring. The 60-standard list was built from Appendix A as
    published and checked against district Algebra I maps.
  - Please confirm it against your adopted Algebra I course.
  - Course placements are a bank choice: S-IC, S-CP, S-MD, and S-ID.A.4 go to Probability & Statistics, and (+)
    standards to Precalculus. They can be changed in one file.
- **Drawing.**
  - Graphing questions (`plot`, `plot_text`) need a drawing surface in the game or teacher grading.
  - The figure renderer draws solid lines only. Inequality boundaries are drawn by students, and one question describes
    a boundary line in words.
- **Complex numbers.** Complex solutions are left to Algebra II, as Appendix A does: MAIN questions answer "no real
  solution", and complex solutions appear only in forward branches.
- **A-REI.D.11.** The MAIN questions use quadratic, linear, absolute value, and exponential functions. Logarithmic and
  rational cases are in forward branches.
- **Calculator.** 42 questions expect a calculator (logarithms, rounded roots, correlation).

## Checks

These are checks of the exported bank, not of the live game.

- **Hand checks.**
  - Every question was solved by hand while it was written.
  - Every multiple-choice item was checked choice by choice for exactly one correct answer.
- **Computer algebra checks (sympy).** An independent check substituted the keyed solutions into the equations of 67
  "Solve …" questions (single equations, systems, and literal equations): all agree.
  - It compared 42 factor, expand, simplify, and add or subtract keys with the given expression: 41 are equivalent, and the
    one flag (√50 · √2 = 10) was a parsing error; that key is correct.
  - It checked the "Solve" multiple-choice items for exactly one correct choice. The parser could not read some choices
    (logarithms, complex numbers, "no real solution"); those choices were checked by hand.
  - `engine/autocheck.py algebra1` recomputes the 27 arithmetic answers it can parse; all agree.
- **Numerical checks.** Statistics answers were recomputed with Python: regression lines, correlation coefficients,
  standard deviations, and the residuals.
- **Structure checks.**
  - No two questions are the same (same text and figure).
  - Every written answer's grading note states its form rule. A keyword check found no required form (expanded, factored,
    standard form, vertex form, exact, rounded, a + bi, simplest form) that its question leaves unstated.
- **PDF checks.**
  - Both PDFs have no text outside the page margins.
  - The figures were checked visually.
- **Package check.** `engine/verify_package.py` checks the ZIP for broken references, hashes, and response fields.
- **Snapshot.** `src/history/v2_records.json` is this version's snapshot (`v1_records.json` is kept for
  the 1.0.0 comparison), and `src/choice_plan.json` freezes the
  multiple-choice letters for later revisions.

This version is not yet approved for the live game; it is ready for external review.

## Rebuild

```
python3 question-bank/engine/build.py algebra1
python3 question-bank/engine/autocheck.py algebra1
python3 question-bank/engine/export.py algebra1
python3 question-bank/engine/coverage.py algebra1
cd question-bank/nexus && zip -qr Algebra1_Nexus_Import_v2.0.0.zip algebra1 && cd -
python3 question-bank/engine/verify_package.py question-bank/nexus/Algebra1_Nexus_Import_v2.0.0.zip
```

## Later courses

The engine is ready for the next courses in order:

1. Geometry
2. Algebra II
3. Probability & Statistics
4. Precalculus (possible)

To add one, add its standards list to `engine/hs_courses.py` and its `COURSE` in `<course>/src/grade.py`. Backward
branches can then point to Algebra I standards, and forward branches to later courses.
