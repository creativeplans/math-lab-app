# Entrepreneurship collection: change log

## Version policy

- `bank_version` in `index.json` follows MAJOR.MINOR.PATCH. A correction to wording, a choice or a key raises the
  PATCH or MINOR number; adding or retiring sets raises MINOR; a new structure raises MAJOR. The game refuses the
  same version number with different questions, so every change to questions needs a new number.
- Question IDs (`S<set>-<section>-Q<n>`, stored as `ENT:<id>`) never change meaning. A retired question keeps its ID
  out of use; a replacement gets a new ID.
- Answer letters are frozen in `src/choice_plan.json`, so later corrections keep each correct choice on its letter.
- Time-sensitive sets are rechecked by their review date (see `SOURCES.md`); a recheck that changes a claim is a
  correction and gets a new version.

## Version 1.0.0 (2026-10-25)

First complete version.

- 156 focused sets: a foundation of 15 modules, an optional specialty module (funding, growth and closing), and four
  paths (services; physical products; digital products; content creation). 12 founder cases are placed through the
  course.
- Every set: MAIN (5 questions), 1 backward branch (2 in set 48) (concept simplification or math prerequisite, each with a
  diagnostic reason), F1 "Apply it" (5) and F2 "Handle the complications" (5). 3,125 questions, all multiple choice
  with 4 choices.
- 48 time-sensitive sets carry sources (URL, claim, date checked), a review interval and a jurisdiction.
- Arithmetic in 612 answers is checked by code at build time.
