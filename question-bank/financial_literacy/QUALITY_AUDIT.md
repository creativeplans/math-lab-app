# Financial Literacy — Question and Distractor Quality Audit

Automatic checks run on every build (`engine/fl_build.py`). A build with any failure stops and writes nothing.

## Enforced on every question

- Four choices (A-D), exactly one correct; the three wrong choices are distinct from each other and from the correct one.
- Every wrong choice has a written misconception (6390 notes in all).
- No "all of the above", "none of the above", "both of these", and no text naming a letter (the game shuffles choices, and such wording would switch shuffling off).
- Every question has feedback. Exactly repeated question stems are refused. This is an exact-text check: it does not prove that two differently worded questions test different things.
- Every computed answer (871 questions) has a recomputation (`calc`). The build checks that the correct choice shows that value at the precision printed and that no wrong choice shows the same value (except labeled comparisons such as "Job A, by $17.50"). This only proves the stored answer matches the stored formula. It does not prove the question states every given a student needs, or that the formula models the situation correctly; those were read by hand and by the independent reviewer.
- Every math link exists in `engine/fl_math_catalog.json`. A catalog match is not proof that the game can serve it; the links were also checked in the installed game and in a real import and play-through (see `MATH_BRANCHES.md`, `MATH_REF_VALIDATION.json`, `RUNTIME_CHECK.json`).
- Every set has at least one backward branch and one Go Deeper section; time-sensitive sets cite sources (claim-level status in `SOURCE_LEDGER.md`).

## Answer positions

| Letter | Correct answers |
|---|---|
| A | 530 |
| B | 533 |
| C | 534 |
| D | 533 |

Numeric choices are listed in increasing order, so their letter follows from the value. Other questions put the correct choice in the least-used letter so far, with ties broken by a hash of the ID.

## Length cues

For the 1407 questions whose choices are text (not plain numbers):

- Correct answer is the unique longest choice: 234 (17%; a random position would give about 25%).
- Correct answer is the unique shortest choice: 231 (16%).

By unit:

| Unit | Text questions | Correct is longest | Share |
|---|---|---|---|
| BANK | 105 | 10 | 10% |
| INCOME | 89 | 25 | 28% |
| BUDGET | 74 | 10 | 14% |
| SAVE | 85 | 18 | 21% |
| DEBT | 83 | 7 | 8% |
| CREDIT | 106 | 7 | 7% |
| INVEST | 181 | 35 | 19% |
| RETIRE | 121 | 33 | 27% |
| TAX | 118 | 31 | 26% |
| RENT | 56 | 8 | 14% |
| HOME | 82 | 9 | 11% |
| CAR | 39 | 1 | 3% |
| INS | 51 | 1 | 2% |
| COLLEGE | 33 | 7 | 21% |
| BIZ | 29 | 2 | 7% |
| PROTECT | 52 | 8 | 15% |
| ECON | 27 | 6 | 22% |
| CONTRACT | 25 | 2 | 8% |
| LIFE | 51 | 14 | 27% |

## Intros

- Learn and Apply questions: 1462; intro length (5, 21, 80) words (min, median, max).
- Knowledge checks (no intro): 668. They test earlier sets, the same set's MAIN skill (from a Go Deeper section), or information given in the question itself.
- Intros never state the answer to a recall question. 15 intros contain the correct choice's wording; each was reviewed by hand and is a classification item, where the intro defines several terms and the student must match a scenario to one: S2-B1-Q1, S7-F1-Q1, S20-M-Q3, S25-F2-Q5, S27-F1-Q1, S41-M-Q1, S41-B1-Q5, S65-F1-Q1, S66-F1-Q2, S67-F1-Q4, S70-F1-Q1, S88-M-Q4, S93-F1-Q5, S97-M-Q1, S100-M-Q5.
- Unreviewed echoes: S100-M-Q5.

## Self-containment (shuffled questions)

The game serves the five questions of a section in shuffled order, so every question must stand alone. The v1.0.0 audit claimed this without a working check, and the reviewer found missing givens in the questions listed under R18, R29, and R31. What was done for v1.1:

- Every question the reviewer listed was rewritten to restate its own numbers and conditions.
- A broader hand read of 127 candidate stems (those with he/she/her/his, "the", or a number that could come from a sibling) during the v1.1 corrections.
- An automatic scan on every build (`sibling_scan` in `engine/fl_build.py`) for stems that point at another question ("the same loan", "above", "as before") or use he/she/her/his with no named person. Result this build: 4 flagged, 4 reviewed as fine (the comparison is inside the question), 0 open.
- Limits: the scan is a pattern search, not a reading test. It cannot catch a question that silently relies on an idea defined only in a sibling's intro. That still needs a human spot-check.

## Distractor review

Wrong choices were rewritten so that each represents a real misunderstanding (for example: confusing a bank account with a brokerage account, funding with investing, simple with compound interest, APR with a monthly rate, gross with net income, a refund with extra income, a premium with a deductible, preapproval with final approval, or diversification with a guarantee). A few safety questions keep a clearly unsafe action as a choice on purpose (for example, sharing a bank login with a lender); their notes say "Unsafe."

## Time-sensitive content

Rules that change are stated as of a date or as a hypothetical amount (for example, "Assume a $7,000 IRA limit"). Sets marked time-sensitive, with their sources:

| Set | Title | Sources |
|---|---|---|
| S1 | Banks, credit unions, and what they do | FDIC (https://www.fdic.gov/resources/deposit-insurance); NCUA (https://ncua.gov/consumers/share-insurance-coverage) |
| S2 | Checking accounts and debit cards | CFPB (Regulation E, 12 CFR 1005.6) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/); CFPB (Regulation CC threshold adjustments) (https://www.consumerfinance.gov/rules-policy/final-rules/availability-funds-and-collection-checks-regulation-cc-threshold-adjustments/) |
| S3 | Opening a checking account | FinCEN / federal banking agencies (Customer Identification Program rule, 31 CFR 1020.220) (https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-B/section-1020.220); CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-checking-account-screening-company-en-1083/) |
| S4 | Account registers and bank statements | CFPB (Regulation E, 12 CFR 1005.6) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) |
| S5 | Overdrafts and bank fees | CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-overdraft-coverage-en-1015/) |
| S6 | Savings accounts and deposit insurance | FDIC (https://www.fdic.gov/resources/deposit-insurance) |
| S7 | Checks, transfers, and payment apps | CFPB (Regulation E, 12 CFR 1005.6) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) |
| S8 | Hourly wages and overtime | U.S. Department of Labor (https://www.dol.gov/agencies/whd/overtime); IRS (Publication 531) (https://www.irs.gov/publications/p531); IRS (No tax on tips deduction) (https://www.irs.gov/newsroom/what-the-no-tax-on-tips-deduction-means-for-you) |
| S10 | Reading a pay stub | IRS (Topic 751) (https://www.irs.gov/taxtopics/tc751) |
| S11 | Form W-4, withholding, and Form W-2 | IRS (Form W-4) (https://www.irs.gov/forms-pubs/about-form-w-4); IRS (Form W-2) (https://www.irs.gov/forms-pubs/about-form-w-2) |
| S13 | Gig work and independent contractors | IRS (Self-Employment Tax, Topic 554) (https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); IRS (Gig Economy Tax Center) (https://www.irs.gov/businesses/gig-economy-tax-center); IRS (Am I required to file a Form 1099?) (https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return) |
| S14 | Education, careers, and lifetime income | U.S. Bureau of Labor Statistics (Employment Projections) (https://www.bls.gov/emp/chart-unemployment-earnings-education.htm) |
| S19 | Smart shopping: unit prices, discounts, and sales tax | New Jersey Division of Taxation (Sales and Use Tax) (https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml) |
| S27 | Savings options: high-yield savings, CDs, and money market accounts | FDIC (https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance); TreasuryDirect (I bonds) (https://www.treasurydirect.gov/savings-bonds/i-bonds/); TreasuryDirect (Buying savings bonds) (https://www.treasurydirect.gov/savings-bonds/buy-a-bond/) |
| S29 | APR and periodic interest rates | CFPB (Truth in Lending, Regulation Z) (https://www.consumerfinance.gov/rules-policy/regulations/1026/); CFPB (Interest rate vs. APR) (https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/) |
| S32 | High-cost credit: payday loans, title loans, rent-to-own, and buy now, pay later | CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-payday-loan-en-1567/); CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-car-title-loan-en-831/) |
| S34 | When debt goes wrong: late payments, collections, and bankruptcy | CFPB (Regulation F, 12 CFR 1006.34) (https://www.consumerfinance.gov/rules-policy/regulations/1006/34/); CFPB (https://www.consumerfinance.gov/ask-cfpb/how-long-does-negative-information-remain-on-my-credit-report-en-323/); CFPB (Regulation Z, 12 CFR 1026.52(b)) (https://www.consumerfinance.gov/rules-policy/regulations/1026/52/) |
| S35 | What a credit card is | CFPB (Credit card key terms) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/); CFPB (Regulation Z, 12 CFR 1026.51) (https://www.consumerfinance.gov/rules-policy/regulations/1026/51/); CFPB (Credit card grace period) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/) |
| S36 | Reading a credit card statement | CFPB (Credit card key terms) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/); CFPB (Credit card grace period) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/) |
| S37 | How credit card interest is calculated | CFPB (Credit card key terms) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/); CFPB (Credit card grace period) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/) |
| S39 | Card fees, balance transfers, and promotional offers | CFPB (Understanding special promotional financing offers) (https://www.consumerfinance.gov/archive/blog/how-understand-special-promotional-financing-offers-credit-cards/) |
| S40 | Credit reports | AnnualCreditReport.com (authorized by federal law) / FTC (https://www.annualcreditreport.com); FTC (https://consumer.ftc.gov/articles/what-know-about-credit-freezes-fraud-alerts) |
| S41 | Credit scores | myFICO (Fair Isaac Corporation) (https://www.myfico.com/credit-education/whats-in-your-credit-score) |
| S42 | Building credit responsibly | myFICO (Fair Isaac Corporation) (https://www.myfico.com/credit-education/whats-in-your-credit-score); AnnualCreditReport.com (authorized by federal law) / FTC (https://www.annualcreditreport.com); CFPB (Credit card grace period) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/) |
| S44 | Brokerage firms and brokerage accounts | SIPC (https://www.sipc.org/for-investors/what-sipc-protects); SEC Investor.gov (Save and invest) (https://www.investor.gov/introduction-investing/investing-basics/save-and-invest) |
| S45 | Opening and funding a brokerage account | SEC Investor.gov (Investor Bulletin: Opening a brokerage account) (https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-43); SEC (https://www.sec.gov/newsroom/press-releases/2023-29) |
| S53 | Taxes on investments | IRS (Topic 409, Capital Gains and Losses) (https://www.irs.gov/taxtopics/tc409) |
| S54 | Speculation, crypto assets, and investment fraud | SEC Investor.gov (https://www.investor.gov/protect-your-investments/fraud/types-fraud); SEC Investor.gov (https://www.investor.gov/additional-resources/spotlight/crypto-assets) |
| S56 | 401(k) and 403(b) plans at work | IRS (401(k) resource guide) (https://www.irs.gov/retirement-plans/401k-plans); IRS (403(b) plans) (https://www.irs.gov/retirement-plans/irc-403b-tax-sheltered-annuity-plans); IRS (Publication 590-B) (https://www.irs.gov/publications/p590b) |
| S57 | IRAs: traditional and Roth | IRS (Publication 590-A) (https://www.irs.gov/publications/p590a); IRS (Publication 590-B) (https://www.irs.gov/publications/p590b) |
| S58 | Roth IRA eligibility and contribution rules | IRS (Publication 590-A) (https://www.irs.gov/publications/p590a); IRS (Retirement topics: IRA contribution limits) (https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits); IRS (Publication 590-A) (https://www.irs.gov/publications/p590a) |
| S59 | Opening a Roth IRA | IRS (Individual retirement arrangements) (https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras) |
| S61 | Roth IRA withdrawals and qualified distributions | IRS (Publication 590-B) (https://www.irs.gov/publications/p590b); IRS (Publication 590-A) (https://www.irs.gov/publications/p590a) |
| S62 | Social Security and retirement income | Social Security Administration (https://www.ssa.gov/benefits/retirement/planner/agereduction.html) |
| S63 | Types of taxes and how they work | New Jersey Division of Taxation (Income tax) (https://www.nj.gov/treasury/taxation/njit25.shtml) |
| S64 | Tax forms: W-2, 1099s, and Form 1040 | IRS (https://www.irs.gov/forms-instructions) |
| S65 | Filing requirements, filing status, and dependents | IRS (Interactive Tax Assistant: Do I need to file?) (https://www.irs.gov/help/ita/do-i-need-to-file-a-tax-return) |
| S66 | From gross income to taxable income | IRS (Federal income tax rates and brackets) (https://www.irs.gov/filing/federal-income-tax-rates-and-brackets); IRS (Working Families Tax Cuts) (https://www.irs.gov/newsroom/working-families-tax-cuts) |
| S67 | Marginal and effective tax rates | IRS (Federal income tax rates and brackets) (https://www.irs.gov/filing/federal-income-tax-rates-and-brackets) |
| S68 | Deductions and credits | IRS (Credits and deductions for individuals) (https://www.irs.gov/credits-deductions-for-individuals) |
| S69 | Refund or balance due | IRS (https://www.irs.gov/filing) |
| S70 | Filing a return: methods, deadlines, and scams | IRS (https://www.irs.gov/filing); IRS (Tax scams) (https://www.irs.gov/newsroom/tax-scams-consumer-alerts); IRS (Notice 2011-17) (https://www.irs.gov/pub/irs-drop/n-11-17.pdf) |
| S71 | Finding a rental and avoiding rental scams | FTC (https://consumer.ftc.gov/articles/rental-listing-scams) |
| S72 | Rental applications and affordability | HUD (Fair Housing Act) (https://www.hud.gov/program_offices/fair_housing_equal_opp/fair_housing_act_overview) |
| S73 | Reading a lease and security deposits | New Jersey Department of Community Affairs (Truth in Renting) (https://www.nj.gov/dca/codes/publications/pdf_lti/t_i_r.pdf) |
| S74 | Tenant responsibilities, rights, and renters insurance | New Jersey Department of Community Affairs (Truth in Renting) (https://www.nj.gov/dca/codes/publications/pdf_lti/t_i_r.pdf) |
| S77 | Property taxes, insurance, PMI, and escrow | CFPB (Buying a House) (https://www.consumerfinance.gov/owning-a-home/) |
| S78 | Closing costs, the Loan Estimate, and the Closing Disclosure | CFPB (Loan Estimate and Closing Disclosure) (https://www.consumerfinance.gov/owning-a-home/loan-estimate/) |
| S79 | Preapproval, creditworthiness, and debt-to-income | CFPB (https://www.consumerfinance.gov/ask-cfpb/whats-the-difference-between-a-prequalification-letter-and-a-preapproval-letter-en-127/) |
| S81 | Fixed or adjustable rates, and the true cost of owning | CFPB (Adjustable-rate mortgages) (https://www.consumerfinance.gov/ask-cfpb/what-is-an-adjustable-rate-mortgage-arm-en-100/) |
| S82 | The total cost of buying a car | New Jersey Division of Taxation (https://www.nj.gov/treasury/taxation/); FTC (Buying a used car from a dealer) (https://consumer.ftc.gov/articles/buying-used-car-dealer); NHTSA (Recalls) (https://www.nhtsa.gov/recalls) |
| S83 | Auto loans | CFPB (Auto loans) (https://www.consumerfinance.gov/consumer-tools/auto-loans/) |
| S87 | Health insurance | HealthCare.gov (Glossary) (https://www.healthcare.gov/glossary/); HealthCare.gov (Young adults) (https://www.healthcare.gov/young-adults/children-under-26/); Get Covered New Jersey (https://nj.gov/getcoverednj/); IRS (Working Families Tax Cuts) (https://www.irs.gov/newsroom/working-families-tax-cuts) |
| S88 | Auto insurance | New Jersey Department of Banking and Insurance (https://www.nj.gov/dobi/); NAIC (Consumer insurance guides) (https://content.naic.org/consumer) |
| S92 | The FAFSA and financial aid | Federal Student Aid (FAFSA) (https://studentaid.gov/h/apply-for-aid/fafsa); New Jersey Higher Education Student Assistance Authority (HESAA) (https://www.hesaa.org/) |
| S93 | Student loans: federal, private, and interest | Federal Student Aid (Loan types) (https://studentaid.gov/understand-aid/types/loans); CFPB (Private student loans) (https://www.consumerfinance.gov/consumer-tools/student-loans/); U.S. Department of Education (2022 final rule, interest capitalization) (https://fsapartners.ed.gov/fsa-print/publication/1004279) |
| S94 | Repaying loans and return on investment | Federal Student Aid (Repayment) (https://studentaid.gov/manage-loans/repayment) |
| S96 | Self-employment taxes | IRS (Self-employment tax) (https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); IRS (Estimated taxes) (https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes); IRS (Am I required to file a Form 1099?) (https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return) |
| S97 | Business structures, pricing, and getting started | U.S. Small Business Administration (Choose a business structure) (https://www.sba.gov/business-guide/launch-your-business/choose-business-structure); New Jersey Business Portal (https://business.nj.gov/) |
| S98 | Identity theft: prevention and recovery | FTC (IdentityTheft.gov) (https://www.identitytheft.gov/); CFPB (Lost or stolen credit cards) (https://www.consumerfinance.gov/ask-cfpb/am-i-responsible-for-unauthorized-charges-if-my-credit-cards-are-lost-or-stolen-en-29/) |
| S99 | Recognizing and avoiding scams | FTC (Scams) (https://consumer.ftc.gov/features/scam-alerts); FTC (Fake check scams) (https://consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-check-scams); New Jersey Division of Consumer Affairs (https://www.njconsumeraffairs.gov/) |
| S100 | Consumer rights and where to get help | CFPB (Regulation E, 12 CFR 1005.6) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/); CFPB (Lost or stolen credit cards) (https://www.consumerfinance.gov/ask-cfpb/am-i-responsible-for-unauthorized-charges-if-my-credit-cards-are-lost-or-stolen-en-29/); CFPB (Submit a complaint) (https://www.consumerfinance.gov/complaint/); FTC (Cooling-Off Rule) (https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help); New Jersey Division of Consumer Affairs (https://www.njconsumeraffairs.gov/); CFPB (Regulation Z, 12 CFR 1026.13) (https://www.consumerfinance.gov/rules-policy/regulations/1026/13/); CFPB (Regulation F, 12 CFR 1006.34) (https://www.consumerfinance.gov/rules-policy/regulations/1006/34/) |
| S103 | Real returns and interest rates | Federal Reserve (Monetary policy) (https://www.federalreserve.gov/monetarypolicy.htm) |
| S106 | Subscriptions, free trials, and phone plans | FTC (Free trials, auto-renewals, and subscriptions) (https://consumer.ftc.gov/articles/getting-and-out-free-trials-auto-renewals-and-negative-option-subscriptions) |
| S107 | Fees, warranties, and the true price | FTC (Rule on Unfair or Deceptive Fees takes effect) (https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025); FTC (Warranties) (https://consumer.ftc.gov/articles/warranties); CFPB (Buy now, pay later) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-buy-now-pay-later-bnpl-loan-en-2108/) |
| S109 | Charitable giving and civic responsibility | IRS (Tax Exempt Organization Search) (https://apps.irs.gov/app/eos/); IRS (Charitable contribution deductions) (https://www.irs.gov/charities-non-profits/charitable-organizations/charitable-contribution-deductions); New Jersey Division of Consumer Affairs (Charities Registration) (https://www.njconsumeraffairs.gov/charities/); FTC (How to donate wisely and avoid charity scams) (https://consumer.ftc.gov/features/how-donate-wisely-and-avoid-charity-scams); IRS (Working Families Tax Cuts) (https://www.irs.gov/newsroom/working-families-tax-cuts) |
| S111 | Moving out: the first-apartment budget | New Jersey Department of Community Affairs (Truth in Renting) (https://www.nj.gov/dca/codes/publications/pdf_lti/t_i_r.pdf) |

## Checks that actually ran for v1.1

- Build validators above (every build).
- Game importer `--check` on the package and a full import into a test database (`RUNTIME_CHECK.json`).
- Math links re-checked against the installed game with its own code (`MATH_REF_VALIDATION.json`).
- Package check (`engine/verify_package.py`) and cross-export check (`engine/fl_crosscheck.py`, result in `EXPORT_CROSSCHECK.json`): every question has the same ID, choices, key, and page in the package JSON, the answer-key JSON and CSV, the full question and answer PDFs, and the split part PDFs.
- Sibling scan (above).

## What still needs a human reviewer

- Confirm national outcome codes and New Jersey performance expectations against the official documents.
- Confirm each source claim and effective date: 95 of 149 claim rows in `SOURCE_LEDGER.md` are still "unverified" (the build environment could not open the official sites).
- Semantic duplicates: no automatic check finds two questions that test the same thing in different words.
- Read the explanations for tone and reading level, and judge whether any distractor is still too easy.
- Spot-check the knowledge checks for anything not yet taught at that point in the pathway.
