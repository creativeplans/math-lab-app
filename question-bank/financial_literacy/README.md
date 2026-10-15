# Untangle The Nexus — High School Financial Literacy (FL) v1.1.0

**Review status: NOT APPROVED. Release pending recheck.** Version 1.0.0 was independently reviewed (ChatGPT). This version 1.1.0 applies that review: every finding and its fix is in `REVIEW_RESPONSE.md`, and every changed question is in `CHANGES.md`. Passing the build checks does not mean the content is fact-checked. The revised package must be rechecked and approved by the owner before import; do not overwrite a live course with it. The game keeps the course "coming soon" until then.

## What is here

| # | Deliverable | File |
|---|---|---|
| 1 | Question PDF | FinancialLiteracy_Question_Collection.pdf (and pdf/ parts in the package) |
| 2 | Answer key PDF | FinancialLiteracy_Answer_Key.pdf |
| 3 | JSON answer key | FinancialLiteracy_Answer_Key.json |
| 4 | CSV answer key | FinancialLiteracy_Answer_Key.csv |
| 5 | Nexus import ZIP | nexus/FinancialLiteracy_Nexus_Import_v1.1.0.zip |
| 6 | Standards coverage report | COVERAGE.md |
| 7 | Math prerequisite branch report | MATH_BRANCHES.md |
| 8 | Concept prerequisite branch report | CONCEPT_BRANCHES.md |
| 9 | Go Deeper report | GO_DEEPER.md |
| 10 | How-to coverage report | HOW_TO.md |
| 11 | Question and distractor quality audit | QUALITY_AUDIT.md |
| 12 | This README | README.md |
| 13 | Response to the independent review (every R, C, P item) | REVIEW_RESPONSE.md |
| 14 | Change log by question ID (old/new key, reason, source) | CHANGES.md, CHANGES.json |
| 15 | Claim-level source ledger | SOURCE_LEDGER.md, SOURCE_LEDGER.json |
| 16 | Math links checked in the installed game | MATH_REF_VALIDATION.json |
| 17 | Import and play-through test in the real game server | RUNTIME_CHECK.json |
| 18 | Cross-export consistency check | EXPORT_CROSSCHECK.json |

## Size

19 units, 113 sets, 2130 questions: 113 MAIN sections, 113 concept prerequisite branches, 178 math prerequisite links, and 200 Go Deeper sections.

| Unit | Title | Sets |
|---|---|---|
| BANK | Money, Banking, and Financial Institutions | S1, S2, S3, S4, S5, S6, S7 |
| INCOME | Earning Income, Employment, and Paychecks | S8, S9, S10, S11, S12, S13, S14 |
| BUDGET | Budgeting and Managing Expenses | S15, S16, S17, S18, S19, S20 |
| SAVE | Saving, Emergency Funds, and Interest | S21, S22, S23, S24, S25, S26, S27 |
| DEBT | Interest, Borrowing, and Debt | S28, S29, S30, S31, S32, S33, S34 |
| CREDIT | Credit Cards and Credit Scores | S35, S36, S37, S38, S39, S40, S41, S42 |
| INVEST | Investing, Brokerage Accounts, and Investment Products | S43, S44, S45, S46, S47, S48, S49, S50, S51, S52, S53, S54 |
| RETIRE | Retirement Accounts: IRAs, Roth IRAs, 401(k)s, and 403(b)s | S55, S56, S57, S58, S59, S60, S61, S62 |
| TAX | Taxes and Tax Filing | S63, S64, S65, S66, S67, S68, S69, S70 |
| RENT | Renting and Leasing a Home | S71, S72, S73, S74 |
| HOME | Mortgages and Homeownership | S75, S76, S77, S78, S79, S80, S81 |
| CAR | Buying, Financing, and Owning a Vehicle | S82, S83, S84, S85 |
| INS | Managing Risk with Insurance | S86, S87, S88, S89, S90 |
| COLLEGE | Paying for College and Training | S91, S92, S93, S94 |
| BIZ | Entrepreneurship and Self-Employment | S95, S96, S97 |
| PROTECT | Consumer Protection, Fraud, and Digital Security | S98, S99, S100, S101 |
| ECON | Inflation, Interest Rates, and the Economy | S102, S103, S104 |
| CONTRACT | Contracts, Subscriptions, and Fees | S105, S106, S107 |
| LIFE | Integrated Financial Decisions | S108, S109, S110, S111, S112, S113 |

## How it fits the game (existing rules, unchanged)

- Course `financial_literacy` (prefix FL), already registered in the game as "coming soon," multiple choice only (`responseMode: choice`): no video recording and no "Show Me How."
- A set is one MAIN skill. A student answers 5 MAIN questions.
  - 5 correct: mastered; the Go Deeper chain unlocks.
  - 4 correct: a fresh MAIN attempt.
  - **3 or fewer correct: backward branches.** This is the game's Financial Literacy setting `backwardWhenIncorrectAtLeast: 2` (2 or more wrong); this package does not change it. The student works every backward section of the set in package order, each passed with 5 correct in a row, then returns to a fresh MAIN.
- Backward sections are of two kinds: `"kind": "concept"` (five simpler money questions in this package) and `"kind": "math"` (a `ref` to an existing math MAIN skill in Grades 3-8 or Algebra I; no questions).
- Forward sections F1, F2, … are labeled "Go Deeper" and stay on the same topic.
- Teaching text is the question's `intro`, shown above the question on the same screen. The explanation after answering is `feedback`. Questions with an intro are "Learn and Apply"; questions without one are "Knowledge Checks."
- The game serves a section's five questions in shuffled order and may shuffle the choices, so every question stands alone and no text refers to a letter.

## Package format

Same as the Grade 3-8 packages (format_version 1): `index.json` (with `"course": "financial_literacy"` and `bank_version`) plus `sets/S01.json` … `sets/S113.json`. IDs are `S<set>-<section>-Q<n>`; uids add `FL:`.

Fields this package adds (all optional in the game, stored as-is):

| Where | Field | Meaning |
|---|---|---|
| question | intro | Short teaching passage shown before answering |
| question | feedback | Explanation shown after answering |
| question | question_type | "instruction" (Learn and Apply) or "knowledge_check" |
| question | topic, subtopic | Set title and the question's specific idea |
| question | misconceptions | {letter: misconception} for each wrong choice |
| question | practical_how_to | true for practical how-to questions |
| question | sources, effective_date | Sources for changing rules and the date they are stated as of |
| question | page | Page in the question and answer PDFs |
| set | alignment | National topic, learning target, topic-qualified outcome codes with how each was checked; NJ 9.1.12 strands; local identifier note |
| set | content_status | "stable" or "time_sensitive" |
| set | sources | Organization, URL, claim, effective date, and verification status |
| set | practical_skills | Practical skills beyond the standards |
| section | kind, relationship | Backward branch type and why it is needed |
| section | ref, ref_skill | Math link target and its standard and name |
| section | display_label, difficulty | "Go Deeper n" and "deeper" on forward sections |

Not supported by the importer, so not used: links from one Financial Literacy set to another (a concept branch always carries its own five questions).

## Standards

Alignment: 2021 National Standards for Personal Financial Education (topic level; 12th-grade outcome codes, qualified by topic, only where assigned) and NJSLS-CLKS 2020 Standard 9.1 (grade-12 strand level, with known gaps listed in COVERAGE.md). Codes such as FL.SAVE.24 are local course identifiers, not official codes. Section roles: MAIN = direct alignment; backward = supporting prerequisite; Go Deeper = related enrichment. The package does not claim full mastery of either standard. Details and the full matrix are in COVERAGE.md.

## Sources and changing rules

Sources are federal and state agencies and regulators: IRS, CFPB, FDIC, NCUA, SEC, FINRA, SIPC, Federal Student Aid, FTC, NHTSA, Social Security Administration, Federal Reserve, BLS, HealthCare.gov, and New Jersey agencies (Division of Taxation, Division of Consumer Affairs, DOBI, HESAA, Get Covered New Jersey). Each time-sensitive set lists its sources with the claim used. Amounts that change often (IRA and 401(k) limits, tax brackets, standard deductions, Roth income limits, mileage rates) are given as stated hypothetical amounts so the questions stay correct; real figures are stated "as of" a date.

**Verification limit:** the authoring environment's network policy blocked the official sites (nj.gov, njconsumeraffairs.gov, jumpstart.org, councilforeconed.org, irs.gov, consumerfinance.gov, fdic.gov, econedlink.org and similar sites). Claims were written from knowledge and checked against web search results only. Each source in the package carries `verification` (reviewer-checked topic, search-corroborated, or unverified), `verification_detail`, and `verified_on: null`; the claim-level list is `SOURCE_LEDGER.md` / `.json`. To let a future session verify them, allow those hosts in the environment's network settings, or upload the official PDFs (the National Standards, NJSLS 9.1) to the repository.

## Known limitations

- National outcome codes are assigned to a few sets only, written with their topic, and none was checked by the author against the official PDF. NJ alignment is at the strand level, and known NJ gaps are listed in COVERAGE.md section 3a. The course does not claim full mastery of either standard.
- Math remediation uses the target skill's own question types (multiple choice, true/false, typed numbers); see MATH_BRANCHES.md.
- Source claims and effective dates need a reviewer's confirmation (see above). Some federal rules changed in 2025-2026 (for example, student loan repayment plans); those questions say to check the official site.
- Real company names (Charles Schwab, Fidelity, E*TRADE, Vanguard, Experian, and others) appear as examples only, never as endorsements.
- Misconception notes are stored for future use; the game does not route by them today.

## Rebuild and check

```
python3 question-bank/engine/fl_build.py          # validate, keys, package, PDFs, reports, ZIP
python3 question-bank/engine/fl_build.py --quick  # validate, keys, package only
cd untangle-the-nexus && npx tsx tools/import-collection/import.ts --check <path to the ZIP>
```

Source files: `question-bank/financial_literacy/src/u*.py` (one module per unit); constructors in `engine/fl_dsl.py`; metadata in `financial_literacy/src/fl_meta.py`.

## Importing into the game (after approval only)

Follow the game's docs/FINANCIAL-LITERACY.md, Phase C: upload the ZIP to the work branch, run the importer, confirm 0 invalid and review warnings, run the tests, play it as the creator, and only then ask the owner before setting the course to available.
