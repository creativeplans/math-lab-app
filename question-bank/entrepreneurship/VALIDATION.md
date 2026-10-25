# Entrepreneurship collection: validation

Version 1.0.1, run on 2026-10-25 by `src/validate.py` against the built answer key and import package.

## Hard checks (a failure stops the release)

| Check | Result | Detail |
|---|---|---|
| Every section has exactly 5 questions | PASS | 625 sections; wrong sizes: none |
| Every planned set is built with MAIN, at least one backward branch, F1 and F2 | PASS | 156 of 156 sets built; incomplete: none |
| At least 100 MAIN sets | PASS | 156 sets |
| Backward branches per set are between 1 and 7 | PASS | {1: 155, 2: 1} |
| Every backward branch is concept_simplification or math_prerequisite and states its diagnostic reason | PASS | {'concept_simplification': 123, 'math_prerequisite': 34}; missing reason: none |
| Forward sections are titled "Apply it" (F1) and "Handle the complications" (F2) | PASS | [('forward1', 'Apply it'), ('forward2', 'Handle the complications')] |
| Question IDs are unique and follow S<set>-<section>-Q<n> (stored as ENT:<id>) | PASS | 3125 IDs; duplicates none; malformed none |
| Every question is multiple choice with 4 distinct choices A-D, one correct letter matching the key, a teaching passage and feedback | PASS | 3125 questions; problems: none |
| Every wrong choice has a written reason in the private key | PASS | 3125 x 3 reasons |
| Every teaching passage is 55-125 words | PASS | min 55, max 114, mean 79 words |
| No placeholder text | PASS | none found |
| Questions stand alone (no references to other questions) | PASS | none found |
| Questions that use referring phrases ("same", "that total", "after commission"...) are answerable from their own displayed content (each one reviewed and listed in LOCAL_REVIEWED) | PASS | 23 matched and reviewed; unreviewed: none; stale entries: none |
| No real-looking identifiers (SSN, EIN, phone numbers, real email addresses, web addresses) in questions | PASS | none found |
| No question repeated word for word (same prompt and same key) | PASS | none |
| No prompt repeated inside a section | PASS | none |
| Correct letters balanced across A-D (each 23-27 percent) | PASS | A 782 (25.0%), B 781 (25.0%), C 781 (25.0%), D 781 (25.0%) |
| No section has the same correct letter for all 5 questions | PASS | 0 sections |
| The correct answer is never conspicuously longest (more than 20 percent longer than every wrong choice) | PASS | none |
| The four required paths exist | PASS | ['services', 'products', 'digital', 'content'] |
| Every set is in exactly one module | PASS | 20 modules |
| Module kinds are foundation, path or specialty; path modules name a path; specialty modules are optional | PASS | {'foundation': 15, 'specialty': 1, 'path': 4}; problems: none |
| Prerequisites ("requires") point only to earlier sets, so there are no loops | PASS | 160 prerequisite links; problems: none |
| Suggested reading is kept separate from prerequisites | PASS | 5 sets have suggested reading; overlaps: none |
| Every time-sensitive set lists sources (https URL, claim, date checked), a review interval and a jurisdiction | PASS | 52 time-sensitive sets, 104 stable; problems: none |
| Stable sets carry no time-sensitive source list | PASS | none |
| At least 12 founder cases, each sourced, separating documented history from the course's interpretation, spread through the course | PASS | 12 cases at sets [4, 9, 17, 18, 56, 84, 95, 96, 135, 140, 150, 156] across 10 modules (largest gap 39 sets); problems: none |

## Reported numbers (for review)

| Item | Detail |
|---|---|
| Teaching passages within the contract's "about 60-120 words" | 285 of 3125 questions use a passage of 55-59 words (none exceed 120) |
| Share of questions where the correct answer is the single longest choice | 988 of 3125 (31.6%; 25% would be chance). Reported for review; none is conspicuously longest. |
| Every question with arithmetic in the key has a code check that passed at build time | 613 questions carry a code check (build.py stops if any check fails) |
| Sources not confirmed from the official page itself (secondary sources, search excerpts or a statute citation; flagged in SOURCES.md for review) | 11 of 37 sources: chargeback, chromium_lock, dol_contractor, ftc_endorse, ftc_fakecheck, ftc_reviews, irs_estimated, irs_se, usc_109, usps_1583, uspto_name |
