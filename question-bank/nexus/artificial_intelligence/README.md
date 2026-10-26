# Artificial Intelligence: Understanding and Using AI Wisely

Untangle The Nexus question collection `AI` (course `artificial_intelligence`, category Adults & HS Students),
version 1.0.1 (2026-10-26). 153 focused sets (153 MAIN sets, 153 backward branches, 153 F1 and 153 F2
sections), 3060 multiple-choice questions. Generated from `question-bank/artificial_intelligence/src` (plan.py,
sources.py and data_*.py) by build.py, validate.py and report.py. Regenerate there rather than editing these files
by hand.

Course scope: general education for adults and high-school students, not legal, medical or financial advice. No AI tool, account, download or paid service is needed: every example is prepared in advance and shown as text, and nothing runs. Examples labeled "fictional" were written for this course and are not real outputs of any named product. Laws, products and prices change; dated lessons say what to check. People and organizations in scenarios are fictional unless a lesson names a real case.

**No live AI lab, no external account, no paid service and no creation task.** Learners read a teaching passage and
answer a four-choice question. Every prompt, response, code snippet, table and log is a prepared example written for
this course and labeled as such; nothing is generated or executed by the learner.

## What is in this collection

- A shared foundation of 6 modules (what AI is; how a model learns; large language models; asking for what you
  need; checking results; privacy and security basics), an optional specialty module (kinds of learning,
  reinforcement learning, transformers), and five selectable paths: Everyday use; Creative work; Coding & automation;
  Work & careers; Society, law & philosophy. Shared skills are taught once and referenced by `requires`; optional
  connections are listed separately as `suggested`.
- Every set: MAIN (5 questions), at least one backward branch (153 in total; concept simplification or underlying
  skill, each with its diagnostic reason), F1 "Apply it" (5) and F2 "Handle the complications" (5).
- Every question has its own teaching passage (55-125 words), a scenario question, 4 choices with one correct answer,
  feedback, and (in the private key) a reason for every wrong choice. 97 questions show a prepared example
  (18 with Python 3 code; every complete program was executed at build time and its printed output checked).
- 38 time-sensitive sets (law, policy, provider facts, careers, history, energy) carry sources with a jurisdiction,
  effective year, date checked and review interval; the rest are stable concepts.
- Disputed questions (who owns AI output, training-data copyright, fairness goals, the Turing test, the Chinese Room,
  machine consciousness, alignment, general intelligence) are taught as open; no key settles them.

## Files

| Path | Contents |
|---|---|
| `index.json` | Course, bank version, category, scope note, outcomes, the five paths, the modules and every set with its file |
| `sets/Sxxx.json` | One file per set: prerequisites, suggested reading, sources, and sections M, B1..., F1, F2 with 5 questions each |
| `COVERAGE.md` | Domains A-T mapped to sets, modules and paths, and every set with its branches and diagnostic reasons |
| `SOURCES.md` | Every source with its claim, jurisdiction, date checked, review interval and next review date |
| `VALIDATION.md` | Every validation check, its result, and the known limitations |
| `CHANGELOG.md` | Version policy and what changed |
| `pdf/` | The question collection and the answer key in 7 volumes each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

The full PDFs (`AI_Question_Collection.pdf`, 3213 pages, one question per page; `AI_Answer_Key.pdf`, 1616 pages) and
the answer key as JSON and CSV (`AI_Answer_Key.json`, `AI_Answer_Key.csv`, with `question_page` for every ID) are in
`question-bank/artificial_intelligence/`.

## Decisions where the contract overrides the request

- **Question IDs.** The request suggested `AI-S001-M-Q01`. The importer contract (COURSE-BANKS.md) requires
  `S<set>-<section>-Q<n>`, stored by the game as `AI:S1-M-Q1`. The bank uses the contract format; the mapping is
  one-to-one (`AI-S001-M-Q01` = `AI:S1-M-Q1`).
- **Routing.** The request said 5/5 mastered, 4/5 fresh MAIN, 0-3/5 backward. The owner's rule for every course
  (COURSE-BANKS.md, decision of 2026-10-22) is 5/5 mastered; 3-4/5 a fresh MAIN set; 0-2/5 all backward branches,
  then a fresh MAIN set. The game applies the owner's rule.
- **Reserve pools.** The importer (`tools/import-collection/v2.ts`) accepts exactly 5 questions per section, so no
  reserve or variant questions can be imported. When a learner has seen a whole pool, the game reuses the
  least-recently-seen question (exhaustion behavior). No template generation is used.

## How it is graded

Every question is multiple choice (`"type": "mc"`); the game's grader compares the chosen letter with
`correct_letter`. No free-text or AI grading is needed.

## Installing (the owner uploads the ZIP; Claude runs the commands)

1. Put `Artificial_Intelligence_Nexus_Import_v1.0.1.zip` on the work branch under `content-src/artificial_intelligence/`.
2. Check only: `npx tsx tools/import-collection/import.ts --check content-src/artificial_intelligence/Artificial_Intelligence_Nexus_Import_v1.0.1.zip`
3. Install: `npx tsx tools/import-collection/import.ts content-src/artificial_intelligence/Artificial_Intelligence_Nexus_Import_v1.0.1.zip`
4. Roll back if needed: `npx tsx tools/import-collection/import.ts --rollback <course dir>`.
5. Release (`release: 'available'` in `packages/curriculum/src/courses.ts`) only after the owner approves.

Result of the check-only import run for this version: PASS on 2026-10-26 (v1.0.1): `import.ts --check` (importer v2 from creativeplans/untangle-the-nexus, branch claude/compassionate-hypatia-qh29lj) read 153 sets and 3,060 questions (all multiple choice), 0 invalid, 0 warnings, 38 time-sensitive sets in the review list: "CHECK ONLY: the bank is valid. Nothing was changed." The same check was run on the ZIP.

## Checks run for this version

- Every section has exactly 5 questions: pass
- Every planned set is built with MAIN, at least one backward branch, F1 and F2: pass
- At least 100 MAIN sets: pass
- Backward branches per set are between 1 and 7: pass
- Every backward branch is concept_simplification or underlying_skill and states its diagnostic reason: pass
- Forward sections are titled "Apply it" (F1) and "Handle the complications" (F2): pass
- Question IDs are unique and follow S<set>-<section>-Q<n> (stored as AI:<id>): pass
- Every question is multiple choice with 4 distinct choices A-D, one correct letter matching the key, a teaching passage and feedback: pass
- Every wrong choice has a written reason in the private key: pass
- Every teaching passage is 55-125 words: pass
- No placeholder text: pass
- Questions stand alone (no references to other questions): pass
- Every prompt that points at a prepared example ("this example", "this table"...) carries that example: pass
- Questions that carry a non-code example refer to it in the prompt: pass
- Every example is labeled as prepared or fictional (no simulated output is presented as a real transcript): pass
- Every simulated prompt and response says it is not a real AI output: pass
- No fictional (simulated) output is attributed to a real AI product: pass
- Every complete code example states its language and was executed at build time with its printed output checked (fragments are labeled as fragments): pass
- No real-looking identifiers (SSN, EIN, phone numbers, real email addresses, web addresses) in questions: pass
- No question repeated word for word (same prompt and same key): pass
- No prompt repeated inside a section: pass
- Correct letters balanced across A-D (each 23-27 percent): pass
- No section has the same correct letter for all 5 questions: pass
- The correct answer is never conspicuously longest (more than 20 percent and at least 7 characters longer than every wrong choice): pass
- The five required paths exist: pass
- Every set is in exactly one module: pass
- Module kinds are foundation, path or specialty; path modules name a path; specialty modules are optional: pass
- Prerequisites ("requires") point only to earlier sets, so there are no loops: pass
- Suggested reading is kept separate from prerequisites: pass
- Every time-sensitive set lists sources (https URL, claim, date checked), a review interval and a jurisdiction: pass
- Stable sets carry no time-sensitive source list: pass
- Every sourced law set cites sources with a jurisdiction and an effective year: pass
- Sets about disputed legal or philosophical questions say in MAIN teaching that the question is open: pass

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 questions (see "Reserve pools" above).
- Sources were checked through web-search results for the pages on 2026-10-26; pages were not opened directly.
  8 sources could not be confirmed from the primary page itself and are marked in `SOURCES.md` for a direct
  check at the first review. Law sets teach dated facts and what to check; they are general information, not legal
  advice.
- All prices and rates are hypothetical. All people, companies, prompts and AI responses are fictional; email
  addresses use reserved example domains.
- Explanations, wrong-choice reasons and keys were written and reviewed by the author; arithmetic in 107 answers
  and every complete code example are checked by code.
- Answer-length balance: the correct answer is never conspicuously the longest choice and is the single longest in
  about 28% of questions (25% would be chance). Many wrong choices are padded misconceptions: in 34% of
  questions one wrong choice is noticeably longer than the rest, and absolute words (always, never, every...) appear
  far more often in wrong choices than in correct ones. Both patterns point away from the key; they are listed in
  `VALIDATION.md` for the round-2 balancing edit.
