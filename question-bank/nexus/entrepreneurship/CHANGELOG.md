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

## Version 1.0.1 (2026-10-25)

Correction release after an outside review. Question IDs, answer letters and set structure are unchanged (every
correct answer is on the same letter as in 1.0.0, checked against the 1.0.0 key); 156 sets
and 3,125 questions as before. Each change below updated the prompt, the choices, the key, the feedback and the
why-wrong notes together.

### 1. Substantive corrections

| Finding | Question IDs and passages | What changed |
|---|---|---|
| 1.1 Owner draws | DRAW passage (set 36); S36-M-Q1, S36-M-Q2, S36-F1-Q2, S36-F2-Q4, S60-F2-Q4; distractors in S58-M-Q2, S59-M-Q2, S60-M-Q4, S60-F1-Q4 | A draw is "an owner withdrawal for personal use"; it lowers cash but not profit. S36-F1-Q2 now asks about cash (5,000 - 1,500 = 3,500). S36-F2-Q4 now says a loan is a debt to repay and a contribution adds to equity; it no longer says a contribution can never be returned. S60-F2-Q4 states "no new owner contributions or other equity changes". |
| 1.2 Label cost | S46-F2-Q2 | Asks for the purchase cost per label: 50 / 500 = 0.10 dollars; feedback adds that the 100 used cost 10 dollars. |
| 1.3 Raised money | RAISED passage (set 129); S129-M-Q2, S129-F2-Q1, S129-F2-Q5 | Cash received is not automatically profit; loans and owner or investor money are financing; grants and crowdfunding are classified by their terms; profit = recognized income minus expenses. M-Q2 no longer offers "winning a grant" (the choices are a loan, investor money and an owner contribution). F2-Q1 says reward crowdfunding. F2-Q5 key: "Loans and investor money add cash but are financing, not profit." |
| 1.4 Unit economics | S130-B1 passage, S130-B1-Q3, S130-F1-Q2, S130-F2-Q5 | B1-Q3 now asks what is left after the 1-dollar referral cost: 3 x 0.50 - 1 = 0.50. F1-Q2 uses expected (average) contribution. F2-Q5 key: "Growth is more likely to help when contribution per customer exceeds CAC." |
| 1.5 Overpayment check | SCAM passage (set 75); S75-M-Q4, S75-F2-Q4 | The passage no longer says to wait for funds to clear; it says never to send back an overpayment, because a check can be returned as fake weeks after funds are made available. M-Q4 key: "Do not send the 1,000; check with your bank at a trusted number". F2-Q4 says "the bank made the funds available". Source added: `ftc_fakecheck`. |
| 1.6 Insurance | INS passage (set 113); S113-F1-Q3 | "Policy terms can include" limits, a deductible on a covered claim and exclusions. F1-Q3 states one covered 5,000-dollar loss, adequate limits and no other costs. S113-F1-Q2 kept at 4,000 dollars as instructed. |
| 1.7 Ownership | EQUITY passage and S128-B1 passage; S128-M-Q2, S128-B1-Q1 to Q5, S128-F1-Q1, S128-F1-Q2 | B1-Q4 says she sells 25 percentage points of the whole company from her existing shares, with no new shares issued (55 percent). The B1 passage now teaches new-share dilution separately (80 x 0.75 = 60). Implied values are called post-money values; F1-Q2 says the investor's shares are new shares. |
| 1.8 Test groups | S13-F2-Q3 | 5 friends became 10; "strangers" became independently recruited prospective target customers asked the same neutral question under comparable conditions. |
| 1.9 Laundry test | S6-F2-Q3 | The prompt says the dorm has no convenient laundry in the building; the key says "lack easy laundry" instead of "lack washers". |
| 1.10 Capacity | CAP passage and S52-B1 passage; S52-M-Q5 | Key: "Get qualified help or improve the process." Raising prices is taught as a separate choice that manages demand but adds no capacity. |
| 1.11 Conversion | MEASURE passage and S83-B1 passage; S83-M-Q2, S83-M-Q3, S83-B1-Q1 to Q5, S83-F1-Q1 | Conversion rate = visits that included at least one useful action / total visits, with consistent units ("30 of 1,200 visits included an order"). The 100 percent cap in B1-Q4 is stated for this metric only. |
| 1.12 Copyright | ORIG passage (set 151), S151-B1 passage, RIGHTS passage (set 117); S117-F2-Q5, S151-M-Q1, S151-B1-Q4, S17-F2-Q1 | Teaches a valid legal basis: own work, permission or license, public domain, or a legal exception such as fair use (case by case); credit alone is not one. S17-F2-Q1 separates the store's copyrighted photos from lawful resale of genuine shoes. Sources added: `copyright_fairuse` (17 U.S.C. 107), `usc_109`. |
| 1.13 Tax credits | DED passage (set 63); S63-M-Q4, S63-F1-Q2, S63-F2-Q3 | States that the credit is fully eligible and usable and a flat made-up rate applies; adds that some credits cannot reduce tax below zero; F2-Q3 is limited to those assumptions. Source added: `irs_credits`. |
| 1.14 EIN order | APPLY passage (set 31); `irs_ein` claim | "If the business will be an LLC or corporation, form it with the state first" (partnership removed). |
| 1.15 HTTPS sign | SAFE passage (set 81); S81-M-Q5 | No longer teaches the padlock as universal: check "https://" or the browser's site information; Chrome replaced its padlock. Source added: `chromium_lock`. |
| 1.16 Duplicate subscription | S106-F2-Q3 | States an accidental, unused duplicate, one license needed and one 15-dollar charge cancellable: 180 dollars a year. |
| 1.17 Activation | S149-F2-Q1 | Says "activation rate"; key: the number reaching activation stayed the same while more sign-ups did not activate; investigate why. All three distractors rewritten. |

### 2. Local givens (each question now shows the numbers it needs)

S35-F1-Q2, S43-F1-Q4, S44-F1-Q2, S45-F1-Q2, S47-F1-Q2, S49-F1-Q2, S49-F1-Q3, S49-F1-Q4, S49-F1-Q5, S52-F1-Q4,
S53-F1-Q2, S56-F1-Q4, S58-F1-Q2, S61-F1-Q3, S61-F1-Q4, S63-F1-Q2, S67-F1-Q2, S71-F1-Q2, S77-F1-Q4, S85-F1-Q4,
S92-F1-Q2, S95-F1-Q3, S96-F1-Q3, S97-F1-Q3, S106-M-Q4, S106-F1-Q3, S113-F1-Q4, S119-F1-Q3, S121-F2-Q3,
S123-F2-Q4, S126-M-Q3, S126-F1-Q2, S126-F1-Q3, S128-F1-Q2, S130-F1-Q2, S130-F1-Q3, S130-F1-Q4, S132-F1-Q3,
S136-F1-Q2, S136-F1-Q4, S137-F1-Q3, S142-F1-Q2, S142-F1-Q3, S144-F1-Q2, S144-F1-Q3, S145-F1-Q3, S146-F1-Q2,
S148-F1-Q2, S153-F1-Q3, S155-F1-Q4, S156-F1-Q3.

Found by the new check and fixed the same way: S7-B1-Q2, S63-M-Q4, S104-F2-Q4, S119-F1-Q2, S83-F1-Q1.

Left as they were (the reviewer's false positives; the facts are in the prompt or in the teaching passage shown
with the question): S19-M-Q2, S44-M-Q3, S44-M-Q4, S50-M-Q2, S50-F1-Q2, S50-F1-Q4, S51-M-Q2, S61-M-Q4, S137-F1-Q2.

`validate.py` has a new hard check: every prompt that uses a referring phrase ("same", "that total", "after
commission", "if she" and similar) must be listed with the reason it is answerable from its own displayed content.
Unlisted matches and stale entries both fail the check.

### 3. Precision

| IDs or passage | Change |
|---|---|
| S7-M-Q1, S7-B1-Q4 | Removed the "injury-free" and "never run out" promises. |
| MARK passage (set 48), S48-M-Q4 | "For an item with a positive cost sold above cost, the markup percentage is greater than the margin percentage." |
| S47-F1-Q1, S47-F2-Q3 | F1-Q1 uses accrual and says the work was earned in May. F2-Q3 says the profit was all received in cash, the equipment was paid in cash, and there were no other adjustments. |
| RES passage (set 55), S55-M-Q4, S55-F1-Q3 | The reserve is for planned shortfalls and unexpected needs. F1-Q3 asks how much must be added to bring the reserve back to its target (1,200). |
| S76-F1-Q5 | States that delivery, and so customer payment, happens before day 30. |
| S26-F1-Q4 | States the 15-year window: the first filing now plus renewals at years 5 and 10. |
| NAME passage and S19-B1 passage | Legal identity versus a separate legal entity: a sole proprietorship is not separate from its owner, and an LLC is. |
| FREE passage (set 124), S124-M-Q3 | Tax decisions go to a CPA, an enrolled agent or another qualified tax professional. |
| BRS passage (set 95), `case_nike` | Blue Ribbon Sports formed in 1964; the Nike brand and Swoosh appeared in 1971 and the company later took the Nike name; accounts of the break with Onitsuka differ. The text no longer states a settled 1971 split or rename. |

### 4. Sources

- `chargeback`: added a merchant-side source, `stripe_disputes`, labeled as a provider-specific example.
- `dol_contractor`: says the February 2026 Department of Labor item is a proposal, not a final rule.
- `ftc_reviews`: the final rule took effect October 21, 2024; incentives conditioned on a particular sentiment are
  distinguished from other incentives.
- `sba_counsel`: now cites the SBA Resource Partners page directly; the SCORE FAQ is kept as corroboration.
- `usps_1583`: the claim now says the applicant signs in the physical or virtual presence of the agent, or has the
  signature acknowledged by a notary.
- `uspto_name`: adds that rights can also come from use of a mark.
- New: `ftc_fakecheck`, `irs_credits`, `copyright_fairuse`, `usc_109`, `chromium_lock`, `stripe_disputes`.

### Where this release differs from the review's recommendations

- `usps_1583` keeps the USPS forms page as its URL. A search did not return the current Form 1583 PDF, so it was not
  cited. The signing rule comes from the USPS Federal Register notice returned by search, and the entry stays flagged
  for a direct check.
- `ftc_endorse`, `irs_estimated`, `irs_se` and `uspto_name`: the review reports that the official pages support the
  claims. These pages could not be opened from the authoring environment, so the entries stay flagged "needs direct
  check", and each note records the review's finding.
- `usc_109` (statute text), `chromium_lock` (only the blog's month archive came back from search) and
  `ftc_fakecheck` (FTC excerpts only) are new and are flagged the same way.
- Some keys are worded more briefly than the review's suggestion, so that the correct answer does not stand out by
  length. Examples: S75-M-Q4 "Do not send the 1,000; check with your bank at a trusted number"; S83-M-Q2
  "Converting visits divided by all visits".
- The review's recommended page for IRS credits was "Credits and deductions for individuals". This release cites the
  IRS "Refundable tax credits" page, which search returned and which states that most credits reduce tax only to
  zero. The newsroom page "Tax credits and deductions for individuals" is listed as corroboration.

### Builder

- `build.py`: when a question's choices are corrected, its correct answer now stays on the letter it had before. In
  this release, 18 rewritten questions had first been given new letters; that was caught before release and undone.
