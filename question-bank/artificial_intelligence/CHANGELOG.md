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

## 1.0.1 (2026-10-26): corrections from the first independent review

All question IDs, sets, sections and branch relationships are unchanged. In every repaired question the teaching
passage, example, prompt, choices, key, feedback and wrong-choice reasons were changed together.

Required content corrections
- A1 S22 F2 passage, S22-F2-Q1: the "plain language for my grandmother, in full legal detail" example was not a real
  conflict. Replaced with two length rules that cannot both hold (exactly 200 words and under 100 words).
- A2 S38 prepared example, S38 passage, S38-M-Q1: Riverside now opens "at 6 a.m. on weekdays" and "at 7 a.m. on
  weekdays", so the contradiction is real; the passage's store example now says "on Mondays" in both places.
- A3 S59 passage, S59-M-Q4: a calculator "follows a defined calculation" (check the numbers, formula and rounding),
  not "computes exactly every time".
- A4 S62 passage, S62-M-Q3: the failure is a conclusion the sources do not support even taken together; a valid,
  labeled inference from several sources is fine.
- A5 S72 F2 passage and Q4; S82 F2 passage and Q5: the rule now targets deception, missing consent and unapproved
  endorsements, consistent with S80 and S132, instead of banning every synthetic depiction.
- A6 S77 F2 passage and Q4: some screen readers can recognize text in images, but not reliably; publishers should
  give real text or alt text. Joke distractor removed.
- A7 S91 passage, backward passage and B1-Q3, F1-Q1: restoring (back to a saved version) is now distinguished from
  reverting (a new commit undoing a committed change). F1-Q1 restores from the last commit after an uncommitted edit.
- A8 S95-F1-Q3 states that the system chooses and adjusts its own steps; S95-F2-Q3 keys "it depends on who chooses
  the next steps" (read-only agents exist). A broken distractor was repaired.
- A9 S102 passages, F1-Q1, F2-Q3; sources work_wef, work_bls_ds: the WEF totals cover several trends, not AI alone;
  the BLS projection is updated to about 35 percent for 2025-2035.
- A10 S107-F1-Q1: key is "use a tool approved for that data, sharing only what is needed"; removing details does not
  approve a tool (now a distractor).
- A11 S109-F2-Q3: concrete hypothetical token counts with the same input; S109 F2 passage, Q1 and Q2 qualified (some
  products trim or discount repeated text; attachments count for the text processed).
- A12 S115-F1-Q1 defines YES as "qualified to advance"; S115-F2-Q1 and S84-F2-Q1/Q2 also state the positive class.
- A13 S119 F2 passage and Q5: fatigue lowers care and consistency; leniency is one possible pattern.
- A14 S123-F2-Q4 asks for a first check for unequal outcomes; comparing outcomes does not by itself prove a proxy.
- A15 S134 passage, M-Q5, F1-Q2, F2-Q2; source law_cfpb: taught from Regulation B (12 CFR 1002.9); Circular 2023-03 is
  identified as withdrawn on May 12, 2025, which did not repeal the regulation.
- A16 S80 and S132 passages, S80-M-Q5, S80-F1-Q5, S132-M-Q3, S132-F1-Q2; source law_fcc_voice: AI voices count as
  "artificial" voices, so covered calls follow the existing rules and their exceptions; the test scenarios now name
  non-emergency calls to cellphones.

Local facts
- S108-F1-Q3, S140-F1-Q2, S140-F1-Q3, S117-F2-Q2, S117-F1-Q1 ("this table"), S136-F1-Q1 (approved tool) are now
  answerable from their own display. S129-F1-Q4 asks about the human-contribution principle taught in its passage and
  mentions Zarya of the Dawn in the feedback.

Precision repairs
- S15-M-Q2 (no parenthetical hints; similar-length words), S45-F1-Q3, S89 passage and M-Q5 (relevant error text with
  secrets removed), S46-F2-Q1 (code word makes impersonation harder; callback is stronger), S47 passage and M-Q1
  (direct and indirect injection; visible or hidden), S98 F2 passage, S49 passage (RLHF follows training on
  demonstrations), S50 passage and B1-Q3 (attention to earlier tokens), S65 passage, M-Q2, F1-Q1 (private chat; shared
  projects may expose stored files), S67-M-Q2 (absent versus unfinished steps), S69 F2 passage and Q4 (chat history is
  not a reliable versioned backup), S75 backward passage (same scale starting at 0), S84 passage and M-Q5 (detector
  scores, not calibrated probabilities), S99 F2 passage and Q4 (recall is limited), S103 F2 passage and Q2 (required
  versus preferred skills), S124 passage, M-Q1, F1-Q2 (equal false-positive rates), S153 F2 passage and Q1
  (electricity source affects emissions, not electricity use), S44-F2-Q4 and S98-F2-Q4 (softened absolute keys).
- Joke distractors replaced in the repaired items (S65-M-Q2, S69-F2-Q4, S77-F2-Q4).

Sources
- law_cfpb now points to Regulation B; law_ftc_aicomply records that the Rytr order was set aside on
  December 22, 2025 (S135 passage notes it); law_euaiact names Regulation (EU) 2026/1744 per the Commission record.
- Primary records the independent reviewer opened are recorded as the reviewer's verification in `SOURCES.md`; the
  authoring environment has no direct web access. Sources still needing a direct check: 8 (was 22).

Build and PDFs
- Found while rebuilding: laying out the whole answer key as one flow could silently drop text where an example box
  met a page break (seen at S30-M-Q2 to Q4 with the current PDF library). Each key entry is now laid out separately,
  and the build stops unless every question ID, prompt and correct answer appears in the text of both PDFs. The answer
  key is now 1,616 pages.

Not changed, by the owner's instruction: no bank-wide rewrite for answer-length or absolute-word statistics.

## 1.0.0 (2026-10-26)

- First complete bank for review: 153 focused sets in 21 modules (6 foundation, 1 optional specialty, 14 path
  modules across five paths), 3,060 multiple-choice questions.
- Every set has MAIN, at least one backward branch, F1 "Apply it" and F2 "Handle the complications".
- 42 sources recorded with claim, jurisdiction, effective year, checked date and review interval.
- Balancing pass: padded wrong choices trimmed at clause boundaries in about 1,050 questions so that length is a
  weaker cue; remaining patterns are reported in `VALIDATION.md` for the round-2 edit.
