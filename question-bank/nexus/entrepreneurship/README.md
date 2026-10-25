# Entrepreneurship: Starting and Running a Small Business

Untangle The Nexus question collection `ENT` (course `entrepreneurship`, category Adults & HS Students), version
1.0.0 (2026-10-25). 156 focused sets, 3125 multiple-choice questions. Generated from
`question-bank/entrepreneurship/src` (plan.py, sources.py and data_*.py) by build.py, validate.py and report.py.
Regenerate there rather than editing these files by hand.

Course scope: general education for US learners, not legal, tax or financial advice. Rules, fees and platform policies change and vary by state and city; each lesson says what to check and where. All businesses and people in the questions are fictional unless a lesson names a real company.

## What is in this collection

- A foundation of 15 modules every learner takes (start here, customers, testing demand, names and legal structure,
  EIN and banking, addresses and contact details, costs and pricing, bookkeeping and taxes, getting paid, website,
  marketing, AI as a helper, operations, risk, getting help), an optional specialty module (funding, growth and
  closing), and four paths: services; physical products; digital products; content creation. Shared skills are taught
  once and referenced by `requires`.
- 12 founder cases spread through the course. Each separates the documented history (with its source) from the
  lesson this course draws, and says that one story does not guarantee the same result.
- Every set: MAIN (5 questions), backward branches (157 in total; concept simplification or math prerequisite, each
  with its diagnostic reason), F1 "Apply it" (5) and F2 "Handle the complications" (5).
- Every question has its own teaching passage (55-125 words), a scenario question, 4 choices with one best answer,
  feedback, and (in the private key) a reason for every wrong choice.
- 48 time-sensitive sets carry sources, a review interval and a jurisdiction; the rest are stable.

## Files

| Path | Contents |
|---|---|
| `index.json` | Course, bank version, category, scope note, outcomes, the four paths, the modules and every set with its file |
| `sets/Sxxx.json` | One file per set: prerequisites, suggested reading, sources, and sections M, B1..., F1, F2 with 5 questions each |
| `COVERAGE.md` | Modules and paths, a checklist of what first-time owners forget mapped to sets, the founder cases, and every set with its branches |
| `SOURCES.md` | Every source with its claim, jurisdiction, date checked, review interval and next review date |
| `VALIDATION.md` | Every validation check and its result |
| `CHANGELOG.md` | Version policy and what changed |
| `pdf/` | The question collection and the answer key in 7 volumes each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

The full PDFs (`Entrepreneurship_Question_Collection.pdf`, 3281 pages; `Entrepreneurship_Answer_Key.pdf`, 1206 pages)
and the answer key as JSON and CSV are in `question-bank/entrepreneurship/`.

## How it is graded

Every question is multiple choice (`"type": "mc"`), so the game's automatic grader compares the chosen letter with
`correct_letter`. No free-text or AI grading is needed.

## How the game routes a learner

Under the owner's rule for every course (COURSE-BANKS.md, decision of 2026-10-22): 5/5 on MAIN = mastered and the
F1/F2 challenges unlock; 3-4/5 = a fresh MAIN set of the same skill; 0-2/5 = all backward branches, then a fresh MAIN
set. A course prompt that says "three or fewer correct" is read as this rule.

## Installing (the owner uploads the ZIP; Claude runs the commands)

1. Put `Entrepreneurship_Nexus_Import_v1.0.0.zip` on the work branch under `content-src/entrepreneurship/`.
2. Check only: `npx tsx tools/import-collection/import.ts --check content-src/entrepreneurship/Entrepreneurship_Nexus_Import_v1.0.0.zip`
3. Install: `npx tsx tools/import-collection/import.ts content-src/entrepreneurship/Entrepreneurship_Nexus_Import_v1.0.0.zip`
4. Roll back if needed: `npx tsx tools/import-collection/import.ts --rollback <course dir>`.
5. Release (`release: 'available'` in `packages/curriculum/src/courses.ts`) only after the owner approves.

Result of the check-only import run for this version: CHECK ONLY: the bank is valid. 156 sets, 3125 questions (all mc), 0 invalid, 0 warnings; 48 time-sensitive sets on the review list. (Untangle The Nexus tools/import-collection/import.ts --check, run on the package folder for version 1.0.0.)

## Checks run for this version

- Every section has exactly 5 questions: pass
- Every planned set is built with MAIN, at least one backward branch, F1 and F2: pass
- At least 100 MAIN sets: pass
- Backward branches per set are between 1 and 7: pass
- Every backward branch is concept_simplification or math_prerequisite and states its diagnostic reason: pass
- Forward sections are titled "Apply it" (F1) and "Handle the complications" (F2): pass
- Question IDs are unique and follow S<set>-<section>-Q<n> (stored as ENT:<id>): pass
- Every question is multiple choice with 4 distinct choices A-D, one correct letter matching the key, a teaching passage and feedback: pass
- Every wrong choice has a written reason in the private key: pass
- Every teaching passage is 55-125 words: pass
- No placeholder text: pass
- Questions stand alone (no references to other questions): pass
- No real-looking identifiers (SSN, EIN, phone numbers, real email addresses, web addresses) in questions: pass
- No question repeated word for word (same prompt and same key): pass
- No prompt repeated inside a section: pass
- Correct letters balanced across A-D (each 23-27 percent): pass
- No section has the same correct letter for all 5 questions: pass
- The correct answer is never conspicuously longest (more than 20 percent longer than every wrong choice): pass
- The four required paths exist: pass
- Every set is in exactly one module: pass
- Module kinds are foundation, path or specialty; path modules name a path; specialty modules are optional: pass
- Prerequisites ("requires") point only to earlier sets, so there are no loops: pass
- Suggested reading is kept separate from prerequisites: pass
- Every time-sensitive set lists sources (https URL, claim, date checked), a review interval and a jurisdiction: pass
- Stable sets carry no time-sensitive source list: pass
- At least 12 founder cases, each sourced, separating documented history from the course's interpretation, spread through the course: pass

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 written questions; no extra variant questions are provided. The game
  reuses the least-recently-seen question when a learner has seen the whole pool, so a learner who repeats a section
  sees the same questions.
- Sources were checked through web-search results for the official pages on 2026-10-25 (pages were not opened
  directly). Nine claims were confirmed only through secondary sources; they are marked in `SOURCES.md` for a direct
  check at the first review. The course teaches principles and what to check, not current rates, thresholds or
  penalties.
- Laws and fees vary by state and city; examples that name a state (for example Washington's registered-agent rule)
  are labeled as examples.
- All prices, fees, rates and wages in questions are practice assumptions. All people and businesses in scenarios are
  fictional; email addresses use the reserved `.example` domain.
- Explanations, wrong-choice reasons and answer keys were written by the author; arithmetic in 612 answers is
  checked by code, and the rest was reviewed by the author without a computer check.
- The correct answer is never conspicuously the longest choice, but it is the single longest choice in about
  32% of questions (25% would be chance). This is reported in `VALIDATION.md` for review.
