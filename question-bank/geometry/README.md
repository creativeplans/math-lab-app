# Geometry — Question Collection (version 1.0.0)

The High School Geometry collection for Untangle the Nexus. Geometry is a course, not a grade, so the collection has no
grade level. Everything is generated from one source, the data in `src/`, by `question-bank/engine/`. The collection has
its own directory and its own ID namespace (`GEO`), and it does not depend on any Algebra I file. Algebra I standards appear
only as standard codes in backward branches.

| File | Contents |
|---|---|
| `Geometry_Question_Collection.pdf` | The questions, one per page (3,601 pages including set and branch title pages) |
| `Geometry_Answer_Key.pdf` | Same page numbers; each page shows a reduced copy of the question, its answer, and its grading note |
| `Geometry_Answer_Key.json` / `.csv` | Machine-readable key, one record per question, keyed by `uid` (for example `GEO:S24-M-Q1`) |
| `COVERAGE.md` | Every standard (core and (+)), every subskill with its set and MAIN IDs, every set's branches, distributions, and known gaps |
| `VALIDATION.md` | The 17 automatic checks and their results |
| `CHANGELOG.md` | Changes by question ID |
| `PLAN.md` | The authoring plan: the 96 sets by batch |
| `src/` | The single source: `standards.py` (inventory and subskills), `data_*.py` (sets), `grade.py` (course settings and grading rules), `validate.py`, `resolve.py`, `coverage_reqs.py`, `choice_plan.json` (frozen MC letters), `history/` (the v1 snapshot later versions are compared with) |

The Untangle The Nexus import package is `question-bank/nexus/geometry/`, zipped as
`question-bank/nexus/Geometry_Nexus_Import_v1.0.0.zip`. Its README describes every field. The split PDFs are in its `pdf/`
folder, and `MANIFEST.json` lists every file with its SHA-256 hash.

## Contents

- **96 question sets, 2,915 questions.**
  - **Core strand (sets 1-87):** all 38 non-(+) HSG standards (G-CO, G-SRT, G-C, G-GPE, G-GMD, G-MG).
  - **ADVANCED EXTENSION strand (sets 88-96):** all six (+) standards (SRT.D.9, SRT.D.10, SRT.D.11, C.A.4, GPE.A.3, GMD.A.2).
    The `strand` field marks them, and no core set uses them as a prerequisite.
- **Subparts and distinct demands.** Each standard is split into the subskills its wording names (102 in all). Examples are
  the five definitions in CO.A.1; SAS, ASA, and SSS in CO.B.8; and each construction in CO.D.12. Every subskill is the
  declared focus (`covers`) of a set whose five MAIN questions test it. Subskills whose verb is prove, derive, explain, or
  construct have MAIN questions that require that product: a proof or derivation in a work box, or a construction on the
  figure. `COVERAGE.md` section 3 lists each subskill with its set, IDs, and page.
- **Set structure.**
  - **MAIN:** five parallel questions on one target skill (`target_skill`).
  - **BACKWARD 1..N:** 2-4 per set, 295 in all. Each is a diagnostic branch with easy numbers and one idea per question.
    Its teacher metadata gives the obstacle, why it blocks MAIN, the evidence the five questions collect, and whether the
    standard is an **exact** prerequisite (222) or the closest **supporting** standard (73).
  - **FORWARD 1 and FORWARD 2:** each states its progression type and its one new demand:
    - same-course deepening (97)
    - cross-standard extension (89)
    - later-course extension (6)

    Each is marked direct or NEAREST RELATED; every branch in this release is direct. FORWARD 2 states how it builds on
    FORWARD 1, or why it is a separate extension of MAIN.
- **No circular prerequisites.** A backward standard is a Grade K-8 standard, an Algebra I standard, or the MAIN standard of an
  *earlier* Geometry set. The build stops on anything else, so routing always goes to material taught earlier.
- **Question types:**
  - short answer 1,285
  - multiple choice 571 (A 146, B 145, C 142, D 138)
  - true/false 831 (409 True, 422 False)
  - shown work 168 (proofs, derivations, explanations)
  - drawing or construction 60 (49 compass-and-straightedge constructions)
  - 154 questions have geometry diagrams; every diagram has a text description.

## Answer forms and grading

- **Numeric answers** state the exact value, the units, and the precision. The grading note says "Form required" (exact,
  rounded to a stated place, or an equation form) or "Any equivalent form". Rounded answers allow a tolerance of half a unit
  in the stated place.
- **Proofs and derivations** (`work`) have a sample conclusion in `correct_answer` and a method in `required_method`. The
  grading note gives the essential criteria, valid alternatives (paragraph, two-column, flow, coordinate, transformation),
  and arguments that do not count (for example "it looks like a rhombus" or checking one example for a general claim).
- **Constructions** (`plot`) state the tools on the page ("Compass and straightedge only; leave all arcs"). The grading note
  lists the construction marks to check, not only the final figure.
- **Diagrams** show only what is given. Figures whose labeled measures are not to scale say "Not drawn to scale", and solids
  are oblique sketches with hidden edges dashed.
- **Multiple choice** has exactly one correct answer. Letters are dealt evenly by a seeded plan, now frozen in
  `src/choice_plan.json` so later revisions keep published letters.

## Assumptions and honest limitations (also in `COVERAGE.md` section 8)

- **Standards text.** The official standards site (thecorestandards.org) could not be opened from the authoring environment
  because of its network policy. The inventory in `src/standards.py` was written from the published standards and should be
  spot-checked against the official wording.
- **Course placement.**
  - Backward standards come from Grades K-8, Algebra I, or earlier Geometry sets.
  - Forward standards outside Geometry are labeled with the course this bank places them in (`engine/hs_courses.py`):
    Algebra II, Probability & Statistics, or Precalculus.
  - Within this collection, the (+) standards are placed in Geometry's ADVANCED EXTENSION strand. Earlier collections
    placed (+) standards in Precalculus.
- **Forward branches that apply an earlier-taught standard (15).** Some forward branches use a Geometry standard that is the
  MAIN of an earlier set, at a higher demand. An example is justifying a construction with a congruence proof. They are
  labeled cross-standard extension, and `VALIDATION.md` lists them.
- **Grading support.** Proofs, constructions, and drawings need a person or a drawing surface. Equivalent-form answers need a
  checker that accepts equivalent expressions.
- **Verification limits.** `src/resolve.py` independently recomputes 239 numeric and exact answers. Proofs, explanations,
  classifications, and constructions were checked by reading and by rendering the pages. Diagrams were render-inspected by
  sample (several per batch), not every page.
- **Game functionality is unchanged.** This release is content only. The import package uses the existing types (`sa`, `mc`,
  `tf`, `work`, `plot`) and adds fields, which the importer ignores.

## Checks

`python3 question-bank/geometry/src/validate.py` writes `VALIDATION.md` and exits non-zero on any failure. It checks:

- structure: five questions per section, 2-7 backward branches
- IDs and uids
- coverage of every standard and subskill
- the verb check
- branch rules and metadata
- answer-key completeness, MC and T/F balance, and proof criteria
- construction evidence
- duplicates and unfinished text
- diagram descriptions
- JSON/CSV agreement
- every ID on its recorded page in both PDFs
- stand-alone wording
- the independent re-solve

The build itself also stops on rule violations, such as a backward standard that is not earlier, a missing branch
metadata field, or a figure without a description.

## Rebuild

```
python3 question-bank/engine/build.py geometry        # PDFs, JSON, CSV
python3 question-bank/geometry/src/validate.py         # VALIDATION.md (exit 1 on any failure)
python3 question-bank/engine/coverage.py geometry     # COVERAGE.md
python3 question-bank/engine/export.py geometry       # nexus/geometry/ (sets, assets, PDFs in parts, BRANCH_MAP.json, MANIFEST.json)
python3 question-bank/engine/verify_package.py question-bank/nexus/geometry
```
