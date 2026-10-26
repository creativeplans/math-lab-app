# Artificial Intelligence collection: changelog

## Version policy

- Versions use MAJOR.MINOR.PATCH (`bank_version` in `index.json`, `VERSION` in `src/build.py`).
- PATCH: wording, feedback or source corrections inside existing questions. Question IDs, set numbers and section
  structure do not change, so learner progress keeps its meaning.
- MINOR: new sets added at the end of a module's range, new branches, or a refreshed source review. Existing IDs keep
  their meaning; a retired question is replaced in place only when its skill is unchanged.
- MAJOR: renumbered sets, removed sets or changed outcomes. A MAJOR release needs the owner's approval and an
  import-time migration note.
- Every release reruns `build.py`, `validate.py` (all hard checks must pass) and the importer's `--check`, and
  regenerates `MANIFEST.json` checksums. Correct choices keep their letters when a question is edited
  (`src/choice_plan.json` is frozen), so the PDFs, keys and import files always agree.
- Time-sensitive sets are re-checked by the dates in `SOURCES.md`; a source change that alters a fact is a PATCH
  release with a note here.

## 1.0.0 (2026-10-26)

- First complete bank for review: 153 focused sets in 21 modules (6 foundation, 1 optional specialty, 14 path
  modules across five paths), 3,060 multiple-choice questions.
- Every set has MAIN, at least one backward branch, F1 "Apply it" and F2 "Handle the complications".
- 42 sources recorded with claim, jurisdiction, effective year, checked date and review interval.
- Balancing pass: padded wrong choices trimmed at clause boundaries in about 1,050 questions so that length is a
  weaker cue; remaining patterns are reported in `VALIDATION.md` for the round-2 edit.
