# Financial Literacy — Question and Distractor Quality Audit

Automatic checks run on every build (`engine/fl_build.py`). A build with any failure stops and writes nothing.

## Enforced on every question

- Four choices (A-D), exactly one correct; the three wrong choices are distinct from each other and from the correct one.
- Every wrong choice has a written misconception (6390 notes in all).
- No "all of the above", "none of the above", "both of these", and no text naming a letter (the game shuffles choices, and such wording would switch shuffling off).
- Every question has feedback. Duplicate question stems are refused.
- Every computed answer (869 questions) has an independent recomputation (`calc`). The build checks that the correct choice shows that value at the precision printed and that no wrong choice shows the same value (except labeled comparisons such as "Job A, by $17.50").
- Every math link resolves to a real game skill; every set has at least one backward branch and one Go Deeper section; time-sensitive sets cite sources.

## Answer positions

| Letter | Correct answers |
|---|---|
| A | 532 |
| B | 533 |
| C | 533 |
| D | 532 |

Numeric choices are listed in increasing order, so their letter follows from the value. Other questions put the correct choice in the least-used letter so far, with ties broken by a hash of the ID.

## Length cues

For the 1408 questions whose choices are text (not plain numbers):

- Correct answer is the unique longest choice: 225 (16%; a random position would give about 25%).
- Correct answer is the unique shortest choice: 232 (16%).

By unit:

| Unit | Text questions | Correct is longest | Share |
|---|---|---|---|
| BANK | 106 | 9 | 8% |
| INCOME | 89 | 25 | 28% |
| BUDGET | 74 | 9 | 12% |
| SAVE | 85 | 19 | 22% |
| DEBT | 83 | 6 | 7% |
| CREDIT | 106 | 7 | 7% |
| INVEST | 181 | 34 | 19% |
| RETIRE | 121 | 32 | 26% |
| TAX | 118 | 31 | 26% |
| RENT | 56 | 8 | 14% |
| HOME | 82 | 8 | 10% |
| CAR | 39 | 0 | 0% |
| INS | 51 | 1 | 2% |
| COLLEGE | 33 | 7 | 21% |
| BIZ | 29 | 2 | 7% |
| PROTECT | 51 | 7 | 14% |
| ECON | 27 | 5 | 19% |
| CONTRACT | 25 | 2 | 8% |
| LIFE | 52 | 13 | 25% |

## Intros

- Learn and Apply questions: 1440; intro length (5, 20, 64) words (min, median, max).
- Knowledge checks (no intro): 690. They test earlier sets, the same set's MAIN skill (from a Go Deeper section), or information given in the question itself.
- Intros never state the answer to a recall question. 15 intros contain the correct choice's wording; each was reviewed by hand and is a classification item, where the intro defines several terms and the student must match a scenario to one: S2-B1-Q1, S7-F1-Q1, S20-M-Q3, S25-F2-Q5, S27-F1-Q1, S41-M-Q1, S41-B1-Q5, S65-F1-Q1, S66-F1-Q2, S67-F1-Q4, S70-F1-Q1, S88-M-Q4, S93-F1-Q5, S97-M-Q1, S98-F1-Q1.
- Unreviewed echoes: none.

## Self-containment

The game serves the five questions of a section in shuffled order (least recently seen first). So every question restates its own numbers, no question refers to "the same" account or "the plan above," and an idea taught only in a sibling question's intro is taught again where it is needed.

## Distractor review

Wrong choices were rewritten so that each represents a real misunderstanding (for example: confusing a bank account with a brokerage account, funding with investing, simple with compound interest, APR with a monthly rate, gross with net income, a refund with extra income, a premium with a deductible, preapproval with final approval, or diversification with a guarantee). A few safety questions keep a clearly unsafe action as a choice on purpose (for example, sharing a bank login with a lender); their notes say "Unsafe."

## Time-sensitive content

Rules that change are stated as of a date or as a hypothetical amount (for example, "Assume a $7,000 IRA limit"). Sets marked time-sensitive, with their sources:

| Set | Title | Sources |
|---|---|---|
| S1 | Banks, credit unions, and what they do | FDIC (https://www.fdic.gov/resources/deposit-insurance); NCUA (https://ncua.gov/consumers/share-insurance-coverage) |
| S2 | Checking accounts and debit cards | CFPB (Regulation E) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) |
| S3 | Opening a checking account | FinCEN / federal banking agencies (Customer Identification Program rule, 31 CFR 1020.220) (https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1020/subpart-B/section-1020.220); CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-checking-account-screening-company-en-1083/) |
| S4 | Account registers and bank statements | CFPB (Regulation E) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) |
| S5 | Overdrafts and bank fees | CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-overdraft-coverage-en-1015/) |
| S6 | Savings accounts and deposit insurance | FDIC (https://www.fdic.gov/resources/deposit-insurance) |
| S7 | Checks, transfers, and payment apps | CFPB (Regulation E) (https://www.consumerfinance.gov/rules-policy/regulations/1005/6/) |
| S8 | Hourly wages and overtime | U.S. Department of Labor (https://www.dol.gov/agencies/whd/overtime); IRS (Publication 531) (https://www.irs.gov/publications/p531) |
| S10 | Reading a pay stub | IRS (Topic 751) (https://www.irs.gov/taxtopics/tc751) |
| S11 | Form W-4, withholding, and Form W-2 | IRS (Form W-4) (https://www.irs.gov/forms-pubs/about-form-w-4); IRS (Form W-2) (https://www.irs.gov/forms-pubs/about-form-w-2) |
| S13 | Gig work and independent contractors | IRS (Self-Employment Tax, Topic 554) (https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); IRS (Gig Economy Tax Center) (https://www.irs.gov/businesses/gig-economy-tax-center) |
| S14 | Education, careers, and lifetime income | U.S. Bureau of Labor Statistics (Employment Projections) (https://www.bls.gov/emp/chart-unemployment-earnings-education.htm) |
| S19 | Smart shopping: unit prices, discounts, and sales tax | New Jersey Division of Taxation (https://www.nj.gov/treasury/taxation/su_over.shtml) |
| S27 | Savings options: high-yield savings, CDs, and money market accounts | FDIC (https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance); TreasuryDirect (U.S. Department of the Treasury) (https://www.treasurydirect.gov/savings-bonds/i-bonds/) |
| S29 | APR and periodic interest rates | CFPB (Truth in Lending, Regulation Z) (https://www.consumerfinance.gov/rules-policy/regulations/1026/) |
| S32 | High-cost credit: payday loans, title loans, rent-to-own, and buy now, pay later | CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-payday-loan-en-1567/); CFPB (https://www.consumerfinance.gov/ask-cfpb/what-is-a-car-title-loan-en-831/) |
| S34 | When debt goes wrong: late payments, collections, and bankruptcy | CFPB (Fair Debt Collection Practices Act, Regulation F) (https://www.consumerfinance.gov/rules-policy/regulations/1006/); CFPB (https://www.consumerfinance.gov/ask-cfpb/how-long-does-negative-information-remain-on-my-credit-report-en-323/) |
| S35 | What a credit card is | CFPB (Credit CARD Act / Regulation Z) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/) |
| S36 | Reading a credit card statement | CFPB (Credit CARD Act / Regulation Z) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/) |
| S37 | How credit card interest is calculated | CFPB (Credit CARD Act / Regulation Z) (https://www.consumerfinance.gov/consumer-tools/credit-cards/answers/key-terms/) |
| S39 | Card fees, balance transfers, and promotional offers | CFPB (https://www.consumerfinance.gov/about-us/blog/cfpb-warns-consumers-about-deferred-interest-promotions/) |
| S40 | Credit reports | AnnualCreditReport.com (authorized by federal law) / FTC (https://www.annualcreditreport.com); FTC (https://consumer.ftc.gov/articles/what-know-about-credit-freezes-fraud-alerts) |
| S41 | Credit scores | myFICO (Fair Isaac Corporation) (https://www.myfico.com/credit-education/whats-in-your-credit-score) |
| S42 | Building credit responsibly | myFICO (Fair Isaac Corporation) (https://www.myfico.com/credit-education/whats-in-your-credit-score); AnnualCreditReport.com (authorized by federal law) / FTC (https://www.annualcreditreport.com) |
| S44 | Brokerage firms and brokerage accounts | SIPC (https://www.sipc.org/for-investors/what-sipc-protects); SEC Investor.gov (https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/saving-investing) |
| S45 | Opening and funding a brokerage account | SEC Investor.gov (https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/opening-brokerage-account); SEC (https://www.sec.gov/newsroom/press-releases/2023-29) |
| S53 | Taxes on investments | IRS (Topic 409, Capital Gains and Losses) (https://www.irs.gov/taxtopics/tc409) |
| S54 | Speculation, crypto assets, and investment fraud | SEC Investor.gov (https://www.investor.gov/protect-your-investments/fraud/types-fraud); SEC Investor.gov (https://www.investor.gov/additional-resources/spotlight/crypto-assets) |
| S56 | 401(k) and 403(b) plans at work | IRS (401(k) resource guide) (https://www.irs.gov/retirement-plans/401k-plans) |
| S57 | IRAs: traditional and Roth | IRS (Publication 590-A and 590-B) (https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras) |
| S58 | Roth IRA eligibility and contribution rules | IRS (Publication 590-A and 590-B) (https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras); IRS (Retirement topics: IRA contribution limits) (https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits); IRS (Publication 590-A) (https://www.irs.gov/publications/p590a) |
| S59 | Opening a Roth IRA | IRS (Individual retirement arrangements) (https://www.irs.gov/retirement-plans/individual-retirement-arrangements-iras) |
| S61 | Roth IRA withdrawals and qualified distributions | IRS (Publication 590-B) (https://www.irs.gov/publications/p590b) |
| S62 | Social Security and retirement income | Social Security Administration (https://www.ssa.gov/benefits/retirement/planner/agereduction.html) |
| S63 | Types of taxes and how they work | New Jersey Division of Taxation (https://www.nj.gov/treasury/taxation/njit25.shtml) |
| S64 | Tax forms: W-2, 1099s, and Form 1040 | IRS (https://www.irs.gov/forms-instructions) |
| S65 | Filing requirements, filing status, and dependents | IRS (Publication 501 / Do I need to file?) (https://www.irs.gov/filing/check-if-you-need-to-file-a-tax-return) |
| S66 | From gross income to taxable income | IRS (Federal income tax rates and brackets) (https://www.irs.gov/filing/federal-income-tax-rates-and-brackets) |
| S67 | Marginal and effective tax rates | IRS (Federal income tax rates and brackets) (https://www.irs.gov/filing/federal-income-tax-rates-and-brackets) |
| S68 | Deductions and credits | IRS (Credits and deductions for individuals) (https://www.irs.gov/credits-deductions-for-individuals) |
| S69 | Refund or balance due | IRS (https://www.irs.gov/filing) |
| S70 | Filing a return: methods, deadlines, and scams | IRS (https://www.irs.gov/filing); IRS (Tax scams) (https://www.irs.gov/newsroom/tax-scams-consumer-alerts) |
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
| S87 | Health insurance | HealthCare.gov (Glossary) (https://www.healthcare.gov/glossary/); HealthCare.gov (Young adults) (https://www.healthcare.gov/young-adults/children-under-26/); Get Covered New Jersey (https://nj.gov/getcoverednj/) |
| S88 | Auto insurance | New Jersey Department of Banking and Insurance (https://www.nj.gov/dobi/); NAIC (Consumer insurance guides) (https://content.naic.org/consumer) |
| S92 | The FAFSA and financial aid | Federal Student Aid (FAFSA) (https://studentaid.gov/h/apply-for-aid/fafsa); New Jersey Higher Education Student Assistance Authority (HESAA) (https://www.hesaa.org/) |
| S93 | Student loans: federal, private, and interest | Federal Student Aid (Loan types) (https://studentaid.gov/understand-aid/types/loans); CFPB (Private student loans) (https://www.consumerfinance.gov/consumer-tools/student-loans/) |
| S94 | Repaying loans and return on investment | Federal Student Aid (Repayment) (https://studentaid.gov/manage-loans/repayment) |
| S96 | Self-employment taxes | IRS (Self-employment tax) (https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes); IRS (Estimated taxes) (https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes) |
| S97 | Business structures, pricing, and getting started | U.S. Small Business Administration (Choose a business structure) (https://www.sba.gov/business-guide/launch-your-business/choose-business-structure); New Jersey Business Portal (https://business.nj.gov/) |
| S98 | Identity theft: prevention and recovery | FTC (IdentityTheft.gov) (https://www.identitytheft.gov/); CFPB (Credit card fraud liability) (https://www.consumerfinance.gov/ask-cfpb/what-is-my-liability-for-unauthorized-credit-card-charges-en-24/) |
| S99 | Recognizing and avoiding scams | FTC (Scams) (https://consumer.ftc.gov/features/scam-alerts); FTC (Fake check scams) (https://consumer.ftc.gov/articles/how-spot-avoid-and-report-fake-check-scams); New Jersey Division of Consumer Affairs (https://www.njconsumeraffairs.gov/) |
| S100 | Consumer rights and where to get help | CFPB (Regulation E: lost or stolen debit cards) (https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-my-money-back-after-a-debit-card-theft-en-1017/); CFPB (Credit card fraud liability) (https://www.consumerfinance.gov/ask-cfpb/what-is-my-liability-for-unauthorized-credit-card-charges-en-24/); CFPB (Submit a complaint) (https://www.consumerfinance.gov/complaint/); FTC (Cooling-Off Rule) (https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help); New Jersey Division of Consumer Affairs (https://www.njconsumeraffairs.gov/) |
| S103 | Real returns and interest rates | Federal Reserve (Monetary policy) (https://www.federalreserve.gov/monetarypolicy.htm) |
| S106 | Subscriptions, free trials, and phone plans | FTC (Negative option and automatic renewal offers) (https://consumer.ftc.gov/articles/automatic-renewals-and-subscriptions) |
| S107 | Fees, warranties, and the true price | FTC (Unfair or deceptive fees rule) (https://www.ftc.gov/legal-library/browse/rules/rule-unfair-or-deceptive-fees); FTC (Warranties) (https://consumer.ftc.gov/articles/warranties); CFPB (Buy now, pay later) (https://www.consumerfinance.gov/ask-cfpb/what-is-a-buy-now-pay-later-bnpl-loan-en-2108/) |
| S109 | Charitable giving and civic responsibility | IRS (Tax Exempt Organization Search) (https://apps.irs.gov/app/eos/); IRS (Charitable contributions) (https://www.irs.gov/charities-non-profits/charitable-organizations/charitable-contribution-deductions); New Jersey Division of Consumer Affairs (Charities Registration) (https://www.njconsumeraffairs.gov/charities/); FTC (Donating wisely) (https://consumer.ftc.gov/articles/donating-wisely-avoiding-charity-scams) |
| S111 | Moving out: the first-apartment budget | New Jersey Division of Consumer Affairs (Security deposits) (https://www.nj.gov/dca/codes/publications/) |

## What still needs a human reviewer

- Confirm national outcome codes and New Jersey performance expectations against the official documents.
- Confirm each source claim and effective date (the build environment could not open the official sites).
- Read the explanations for tone and reading level, and judge whether any distractor is still too easy.
- Spot-check the knowledge checks for anything not yet taught at that point in the pathway.
