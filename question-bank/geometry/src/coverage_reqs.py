"""Geometry coverage notes (for COVERAGE.md). The coverage tables themselves are generated from the sets' covers= lists
and standards.py by engine/coverage.py (run_geometry)."""

NOTES = [
    '- **Standards text.** The standards and their wording (`src/standards.py`) were written from the Common Core State Standards '
    'for High School Geometry as published. The official site (thecorestandards.org) could not be opened from the authoring '
    'environment because of its network policy, so a reviewer should spot-check the wording against the official page.',
    '- **Subskills.** Each standard is split by its subparts, its listed objects (for example the five definitions in CO.A.1), and '
    'its verbs (prove, construct, derive, explain). The split is this bank\'s reading of the standard; a reviewer may split '
    'differently. Every subskill has a set whose five MAIN questions test it, and subskills whose verb is prove, derive, explain, '
    'construct, or give an argument have MAIN questions that require that product (checked by `src/validate.py`).',
    '- **(+) standards.** The six (+) standards (SRT.D.9-11, C.A.4, GPE.A.3, GMD.A.2) form the ADVANCED EXTENSION strand '
    '(sets 88-96, `strand` = advanced extension (+)). They never appear as prerequisites of core sets.',
    '- **Forward standards in later courses** are labeled with the course this bank places them in (`engine/hs_courses.py`: Algebra II, '
    'Probability & Statistics, Precalculus). Those collections do not exist yet; forward branches carry the standard code only.',
    '- **Forward branches that apply an earlier-taught standard.** Fifteen forward branches use a Geometry standard that is the MAIN '
    'of an earlier set (for example a construction justified with a congruence proof, or a (+) result applied in a modeling '
    'standard). They are labeled cross-standard extension and state the new demand; VALIDATION.md lists them.',
    '- **Backward branch counts.** Sets have 2-4 backward branches (most have 3). The prompt allows 2-7; more branches were not '
    'added where no further distinct prerequisite obstacle exists.',
    '- **Proofs, constructions, and drawings** (types `work` and `plot`) need teacher grading or a drawing surface. Their grading '
    'notes give essential criteria, valid alternatives, and invalid arguments (proofs), or the construction marks to look for '
    '(constructions). The game\'s answer checker cannot grade these automatically.',
    '- **Diagrams.** Figures show only given information. Figures whose labeled measures are not to scale say "Not drawn to scale". '
    'Three-dimensional solids are oblique sketches with hidden edges dashed, always marked not to scale.',
    '- **Answer checking.** Questions marked "Any equivalent form" need a checker that accepts equivalent expressions (for example '
    '2√5 and √20) or a person; "Form required" questions accept only the stated form (exact, rounded, equation form).',
    '- **Verification limits.** `src/resolve.py` recomputes 239 numeric and exact answers with separate code; the other answers '
    '(proofs, explanations, classifications, constructions) were checked by reading, not by program. Thirteen review stems '
    'recur in different sets\' backward branches; no stem repeats within a set.',
    '- **No difficulty or hint fields**, as in the other collections: difficulty is carried by the section, and the grading note '
    'can be shown as feedback after grading.',
]
