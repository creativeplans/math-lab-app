# Artificial Intelligence collection: validation

Version 1.0.0, run on 2026-10-26 by `src/validate.py` against the built answer key and import package.

## Hard checks (a failure stops the release)

| Check | Result | Detail |
|---|---|---|
| Every section has exactly 5 questions | PASS | 612 sections; wrong sizes: none |
| Every planned set is built with MAIN, at least one backward branch, F1 and F2 | PASS | 153 of 153 sets built; incomplete: none |
| At least 100 MAIN sets | PASS | 153 sets |
| Backward branches per set are between 1 and 7 | PASS | {1: 153} |
| Every backward branch is concept_simplification or underlying_skill and states its diagnostic reason | PASS | {'concept_simplification': 114, 'underlying_skill': 39}; missing reason: none |
| Forward sections are titled "Apply it" (F1) and "Handle the complications" (F2) | PASS | [('forward1', 'Apply it'), ('forward2', 'Handle the complications')] |
| Question IDs are unique and follow S<set>-<section>-Q<n> (stored as AI:<id>) | PASS | 3060 IDs; duplicates none; malformed none |
| Every question is multiple choice with 4 distinct choices A-D, one correct letter matching the key, a teaching passage and feedback | PASS | 3060 questions; problems: none |
| Every wrong choice has a written reason in the private key | PASS | 3060 x 3 reasons |
| Every teaching passage is 55-125 words | PASS | min 56, max 111, mean 86 words |
| No placeholder text | PASS | none found |
| Questions stand alone (no references to other questions) | PASS | none found |
| Every prompt that points at a prepared example ("this example", "this table"...) carries that example | PASS | 97 questions carry an example; missing: none |
| Questions that carry a non-code example refer to it in the prompt | PASS | none |
| Every example is labeled as prepared or fictional (no simulated output is presented as a real transcript) | PASS | none |
| Every simulated prompt and response says it is not a real AI output | PASS | none |
| No fictional (simulated) output is attributed to a real AI product | PASS | none |
| Every complete code example states its language and was executed at build time with its printed output checked (fragments are labeled as fragments) | PASS | 18 questions with code; 17 executed and checked; unchecked: none |
| No real-looking identifiers (SSN, EIN, phone numbers, real email addresses, web addresses) in questions | PASS | none found |
| No question repeated word for word (same prompt and same key) | PASS | none |
| No prompt repeated inside a section | PASS | none |
| Correct letters balanced across A-D (each 23-27 percent) | PASS | A 765 (25.0%), B 765 (25.0%), C 765 (25.0%), D 765 (25.0%) |
| No section has the same correct letter for all 5 questions | PASS | 0 sections |
| The correct answer is never conspicuously longest (more than 20 percent and at least 7 characters longer than every wrong choice) | PASS | none |
| The five required paths exist | PASS | ['everyday', 'creative', 'coding', 'work', 'society'] |
| Every set is in exactly one module | PASS | 21 modules |
| Module kinds are foundation, path or specialty; path modules name a path; specialty modules are optional | PASS | {'foundation': 6, 'specialty': 1, 'path': 14}; problems: none |
| Prerequisites ("requires") point only to earlier sets, so there are no loops | PASS | 154 prerequisite links; problems: none |
| Suggested reading is kept separate from prerequisites | PASS | 11 sets have suggested reading; overlaps: none |
| Every time-sensitive set lists sources (https URL, claim, date checked), a review interval and a jurisdiction | PASS | 38 time-sensitive sets, 115 stable; problems: none |
| Stable sets carry no time-sensitive source list | PASS | none |
| Every sourced law set cites sources with a jurisdiction and an effective year | PASS | 12 law sets; problems: none |
| Sets about disputed legal or philosophical questions say in MAIN teaching that the question is open | PASS | 8 sets checked; problems: none |

## Reported numbers (for review)

| Item | Detail |
|---|---|
| Teaching passages within the contract's "about 60-120 words" | 35 of 3060 questions use a passage of 55-59 words (none exceed 120) |
| Share of questions where the correct answer is the single longest choice | 855 of 3060 (27.9%; 25% would be chance). Reported for review; none is conspicuously longest. |
| Known limitation: a wrong choice is conspicuously longest | 1040 of 3060 questions (34%). These are padded misconceptions; the length pattern points AWAY from the key and is listed for the round-2 balancing edit. |
| Known limitation: absolute words (always, never, every, only...) in choices | correct answers 5%, wrong choices 28%; listed for the round-2 balancing edit |
| Every question with arithmetic in the key has a code check that passed at build time | 106 questions carry a code check (build.py stops if any check fails) |
| Sources not confirmed from the official page itself (secondary sources, search excerpts or a statute citation; flagged in SOURCES.md for review) | 22 of 42 sources: case_mata, energy_iea, hist_alexnet, hist_chatgpt, hist_eliza, law_bartz_kadrey, law_colorado, law_elvis, law_eo14365, law_euaiact, law_fcc_voice, law_ftc_aicomply, law_gdpr22, law_illinois, law_moffatt, law_thaler, law_usco_guidance, law_usco_part2, law_usco_part3, media_c2pa, sec_owasp, tech_osaid |
