"""Disposition of every finding in the independent review of v1.0.0 (ChatGPT), applied in v1.1.0.

R = required corrections, C = recommendations, P = package requirements. Question IDs named by the reviewer are read
from the review file; EXTRA lists the other questions changed for the same finding (repetitions, sibling questions).
The build turns this into REVIEW_RESPONSE.md and CHANGES.md / CHANGES.json.
"""

R = {
    'R01': 'Stem now gives the purchase ($9 each time); key is the computed true cost, $43 ($9 + $34).',
    'R02': 'Key changed to $12,700 (Rule of 72 estimate, nearest hundred); feedback gives the exact compound result $12,864.45 separately.',
    'R03': 'Stem now asks which loan has the highest TOTAL INTEREST, which is what the keyed loan has.',
    'R04': 'Rewritten for tax year 2026 with filing status and eligible cash gifts stated: a single nonitemizer may deduct up to $1,000 ($2,000 married filing jointly). Choices, feedback, S109 source claim, and S66 teaching updated (source A1).',
    'R05': 'Now a clearly labeled hypothetical private loan whose contract capitalizes interest at repayment; intro states that Direct Loans no longer capitalize interest on entering repayment. Accrued interest still owed is kept distinct from interest added to principal (source A2).',
    'R06': 'Asks whether Ana may CONTRIBUTE to an HSA; states her plan is not HSA-compatible and is not a bronze or catastrophic plan; intro explains that bronze and catastrophic plans became HSA-compatible in 2026 (source A1).',
    'R07': 'Uses a lawful $20 fee on a $25 minimum payment: 80%. Calculation, choices, and feedback updated (source A3).',
    'R08': 'Normal check deposited Monday before cutoff into an established account: at least $275 available Tuesday, the rest by the regular schedule (Wednesday in this example). All amounts updated (source A4).',
    'R09': 'Calendar now includes the Monday April 17 Emancipation Day observance; key is Tuesday April 18; weekday distractor corrected (source A5).',
    'R10': 'Teaches $25+ home sales vs $130+ temporary-location sales, subject to exceptions; key is THREE BUSINESS DAYS; Saturday counts, Sundays and federal holidays do not (source A6).',
    'R11': 'Deadline now runs 30 days from receipt of the validation information, and the written-dispute right is kept distinct from disputing later (source A7).',
    'R12': 'States Rosa reports ten days after LEARNING the card was stolen (more than two business days) and within the statement window; Reg E summaries no longer imply blanket loss of earlier protection after 60 days (source A8).',
    'R13': 'The issuer RECEIVES her written billing-error notice at its billing-inquiries address on June 15, within 60 days after transmitting the statement (source A9).',
    'R14': 'Under-21 rule now: independent income OR assets enough for the payments, or an eligible cosigner/joint applicant 21+ if the issuer allows; the scenario states no qualifying income or assets (source A10).',
    'R15': 'Purchase-interest examples now state the card offers a grace period, no cash advances or other excluded balances, and full on-time payment (shared statement text and every repetition). Autopay is a risk reducer, assuming enough money in checking (source A11).',
    'R16': 'Refunds taught as payments (withholding, estimated tax) plus refundable credits exceeding tax; stems that key a withholding conclusion now state no refundable credits or other payments. S69-B1-Q4 key: overpaid tax or refundable credits.',
    'R17': 'Stem no longer infers liability from earnings: it states Jamal expects a positive federal income tax liability this year.',
    'R18': 'Givens stated: Job X pays the entire premium; Job Y offers none, so the worker buys the same coverage for $300 a month.',
    'R19': 'Explanation now describes repeated eating-out overspending in all three months and keys adjusting the category or behavior.',
    'R20': 'Decision goal stated (Sam wants the lowest ongoing cost), so the monthly price is the only fitting criterion.',
    'R21': 'Stem now asks specifically about getting the payment back, so the keyed reversibility idea is the only answer; feedback adds reporting quickly.',
    'R22': "States the credit union's membership rule (employees of local schools and their families) and that Jordan meets neither; key changed to a definite conclusion.",
    'R23': 'Credit defined as borrowing to repay later; debit draws on your own money but can still overdraw (with fees) and overspend. All three items reworded.',
    'R24': 'Key: checking the available balance AND skipping or shrinking the purchase; intro says checking helps only if you act on it.',
    'R25': 'Each overtime scenario states a covered, nonexempt employee and hours in one workweek; S8-F2-Q4 calls $15 "the applicable state minimum wage" (source A12).',
    'R26': 'Discount is a store-funded discount, and the intro says tax treatment of coupons depends on the type of discount and the state.',
    'R27': 'Intro separates new electronic savings bonds (TreasuryDirect) from marketable Treasuries (also via banks and brokers); keyed TreasuryDirect option kept (source A13).',
    'R28': 'Loan math now uses the note interest rate. Every simplified loan states "X% interest (APR X%; no other finance charges)" (S5, S29-S31, S33, S76, S83); S29-M-Q1 is now a credit card with no fees; S29-F1-Q3 states the card APR is its periodic rate x 365 with no other finance charges (source A14).',
    'R29': 'States the full $5,000 / $1,000 is received at the start and everything, including the fee, is repaid at year end; intro says monthly repayment or up-front fees need a fuller APR calculation.',
    'R30': "Intro qualified: the interest share is largest at the start and shrinks as the balance falls (not 'mostly interest').",
    'R31': 'Every listed question restates the numbers it needs (balance, rate, term, payment); the same check was run across the bank (see P4).',
    'R32': 'Formula states a $25 minimum-payment floor; results verified at 176 months and $6,983.44 total paid, $3,679.82 interest.',
    'R33': 'Stem dates the original delinquency (3 years ago, later sent to collections); the 7-year period is measured from it.',
    'R34': 'Stem limited to accurate, current information; key: no one can legally force its removal; intro notes a creditor may choose to update or remove it.',
    'R35': 'Stem: no purchases in foreign currency or processed by foreign merchants, in person or online; intro explains online foreign fees.',
    'R36': 'States a $300 limit and that each statement reports a $30 balance, with no other cards.',
    'R37': 'Uninvested cash may sit in a bank sweep or a money market fund core position; items now distinguish that from buying chosen investments.',
    'R38': 'Stem asks for the PRINCIPAL repaid at maturity (not counting the final interest payment): $1,000.',
    'R39': 'States the fund holds bonds from hundreds of different issuers.',
    'R40': 'States 400 stocks in equal amounts (0.25% each) and that the others do not change.',
    'R41': 'Replaced the semantic-duplicate distractors with distinct misconceptions.',
    'R42': 'States the stand sells only bananas and cannot get any during the shortage, so it cannot make sales.',
    'R43': 'Feedback computes 65.45...% and rounds to the nearest whole percent (65%) in one step.',
    'R44': 'Rollovers are pre-tax plan to traditional IRA; a pre-tax-to-Roth rollover is taxable; withheld 20% is credited toward that year\'s tax, not automatically refunded.',
    'R45': 'States the traditional IRA holds only pre-tax (deductible) money with no after-tax basis; general text says "generally taxable" (source A15).',
    'R46': 'Uses taxable compensation; notes the spousal IRA exception; no-job examples are unmarried; one limit covers traditional and Roth combined (source A16).',
    'R47': 'Ordering taught as regular contributions, then conversions/rollovers, then earnings; beginner examples scoped to regular contributions only; conversion five-year rule kept separate (source A15).',
    'R48': 'Withdrawable basis = contributions minus earlier withdrawals, and no more than the current account value.',
    'R49': 'Feedback says selling after a drop locks in the loss for that money and a drop is not guaranteed to be temporary.',
    'R50': 'States the W-2 is correct and gives the $1,500 pre-tax 401(k) contribution, so the pre-tax answer is the only explanation.',
    'R51': 'Intro: a dependent\'s standard deduction may be limited (earned income plus a small amount, up to the regular amount); S65-F2-Q1 intro aligned.',
    'R52': 'Asks how filing status affects the calculation of the final tax on the return (standard deduction and brackets); intro separates the W-4 status used for withholding.',
    'R53': 'S66-M-Q1 states its hypothetical standard deduction and no other deductions; intro mentions newer deductions available without itemizing; S66-F1-Q3 is explicitly scoped to pre-2026 rules; S66-F2-Q3 says Roth limits use modified AGI.',
    'R54': 'Credit stated to have no carryforward in this example; intro notes some credits carry forward.',
    'R55': 'IP PIN: an e-filed return without the correct IP PIN is rejected; a paper return is delayed for identity checks.',
    'R56': "Actual cash value = today's replacement cost ($1,000 for a similar new TV) minus depreciation.",
    'R57': 'Both homes are stated to be assessed at $350,000; intro separates assessed value from purchase price.',
    'R58': 'Business-day definitions separated: Loan Estimate (days the lender is open) vs Closing Disclosure (all days except Sundays and federal holidays, so Saturday counts); S78-M-Q2/Q3 givens stated (source A17).',
    'R59': 'Says adding 1/12 of a payment monthly pays the same extra amount each year for a similar payoff benefit; exact interest saved can differ.',
    'R60': 'Scoped to a fully amortizing loan whose payment is recalculated with the same balance and remaining term.',
    'R61': 'States the $2,000 at signing is separate from the 36 payments; intro warns not to double-count the first payment.',
    'R62': 'Key: you pay expected depreciation plus a finance (rent) charge, not the full price; feedback consistent with the course\'s lease explanation.',
    'R63': 'Each health-plan calculation states allowed in-network charges, deductible progress (nothing spent yet), and coinsurance after the deductible.',
    'R64': 'States June cash collected ($900) and cash paid ($1,100), with no other cash in or out.',
    'R65': 'States each item brings in $6 after its own costs, before the booth fee.',
    'R66': 'A freeze limits access to the credit report so most lenders cannot approve new credit; it does not protect existing accounts or stop every kind of identity theft.',
    'R67': 'States Rosa deposits the check, ships the bike, and sends $1,200; the bank reverses the $1,500.',
    'R68': 'Gives the TV\'s current resale value ($800); key is a $200 drop in net worth.',
    'R69': 'States the plan feature raises the contribution automatically by one percentage point of salary each year.',
    'R70': 'States the roommates split both rent and utilities equally.',
    'R71': 'Stem asks which benefit adds employer money to retirement savings, leaving the match as the only answer.',
    'R72': 'Names a diversified fund and keys that regular investing CAN help build wealth over time while losses remain possible.',
    'R73': 'Removed unsupported frequency/ranking claims ("most losses", "blocks most takeovers", "most common reason", unnamed studies); S55-F2-Q3 is now a present-bias scenario; S46-F2-Q3 teaches fee and diversification reasoning without citing a study. Related "most" claims in the defaults and Ponzi intros were softened too.',
}

C = {
    'C01': ('Adopted', 'Fee totals now state the fee-triggering condition for every billing period.'),
    'C02': ('Adopted', 'Feedback shows the running balance including fees, ending at -$85.'),
    'C03': ('Adopted', 'Distinguishes the $20-per-month-per-employer reporting rule (cash and charged tips), noncash tips, and the separate qualified-tip income-tax deduction; payroll taxes still apply (source A18).'),
    'C04': ('Adopted', 'Uses 92.35% of net profit; states no other wages near the Social Security wage base and no Additional Medicare Tax.'),
    'C05': ('Adopted', 'Mentions withholding and credits and the current/prior-year safe harbors.'),
    'C06': ('Adopted', 'Replaced S22-B1-Q4 with a one-idea emergency-fund item; the multistep interest estimate was dropped from the backward branch.'),
    'C07': ('Adopted', 'States the avalanche tie-break (smaller balance first when rates are equal).'),
    'C08': ('Adopted', 'Comparisons labeled as rough estimates with the payoff assumption stated.'),
    'C09': ('Adopted', 'Scoped to broadly diversified funds.'),
    'C10': ('Adopted', 'Notes that employers can set up SEP and SIMPLE IRAs; personal traditional/Roth IRAs are opened by the individual.'),
    'C11': ('Adopted', 'Excess contributions can be withdrawn by the due date including extensions; ordinary contribution deadline excludes extensions.'),
    'C12': ('Adopted', 'W-2 "generally by January 31, or the next business day"; propagated to S11 and the source claim.'),
    'C13': ('Adopted', 'Separates the rent-only rule of thumb from the housing-cost-burden measure (which includes utilities).'),
    'C14': ('Adopted', 'States no escrow shortage, surplus, or other change.'),
    'C15': ('Adopted', 'Rate lock described as conditional on its terms and unchanged loan and borrower facts.'),
    'C16': ('Adopted', 'Called a simple cash-flow break-even; notes term, balance, rolled-in costs, and exit date matter for a full comparison.'),
    'C17': ('Adopted', 'Specifies a steady light with no urgent symptoms; removed the guarantee that diagnosis keeps repairs small.'),
    'C18': ('Adopted', 'Asks for expected patient responsibility on the EOB and to compare it with the provider bill before paying.'),
    'C19': ('Adopted', 'At most one claim in the expected-value example; large-group lesson notes correlated catastrophes.'),
    'C20': ('Adopted', 'Tax year 2026, business payer, $2,500 paid vs the $2,000 1099-NEC threshold; income is reportable without a form (source A19).'),
    'C21': ('Adopted', 'Asks what a rejected e-file MAY indicate and keys investigating.'),
    'C22': ('Adopted', 'Specifies a broadly diversified U.S. stock market fund and states past recoveries are not guaranteed.'),
    'C23': ('Adopted', 'Public-good example changed to national defense; tax-funded services distinguished.'),
    'C24': ('Adopted', 'Answer and feedback both use the full value of the forgone alternative.'),
    'C25': ('Adopted', 'Context added: bills and debt minimums covered, starter cushion in place, cash flow allows the match.'),
    'C26': ('Adopted', 'Capital-gains and taxable-account intros scoped to ordinary taxable stock and fund investments, using "generally"; special asset rules and tax-exempt interest noted.'),
}

P = {
    'P1': ('Done, with stated limits',
           'Claim-level SOURCE_LEDGER.md / .json: 149 claim rows across 111 URLs. Each row lists set, the question IDs that depend on '
           'the exact claim, claim text, URL and section, jurisdiction, effective_from / tax_year / stated_as_of, a hypothetical '
           'flag, and verification status. All 11 dead links replaced with direct official pages; the 4 HTTP-403 links kept and '
           'marked as access limits (CISA moved to the direct passwords page). Broad pages no longer carry unrelated claims '
           '(FDIC page limited to insurance; I-bond page no longer cites T-bill rules; 403(b) has its own IRS page). New '
           'claim-specific sources added for every corrected rule (A1-A19, A22, A23). The author still could not open any '
           'official site, so nothing is marked author-verified; verified_on stays null.'),
    'P2': ('Done, with disclosed gaps',
           'Every national code is now written with its topic (e.g., "Earning Income 12-6a"). S53 moved to Investing 12-8b '
           '(tax-deferred vs taxable). S63 moved to Earning Income 12-6b/12-6c with 12-6a for calculations. Each section '
           'carries alignment_role: MAIN = direct, backward = supporting prerequisite, Go Deeper = related enrichment. '
           'FL.X.n is labeled a local identifier. COVERAGE.md 3a lists the NJ gaps (CFR.5, CFR.3, CFR.4/FP.6, FP.4, EG.3, '
           'RM.4, CDM.8) with partial coverage noted; no full-mastery claim. The official PDFs could not be opened here, '
           'so most sets remain topic-level only and the code wording is marked by how it was checked.'),
    'P3': ('Done; one owner decision',
           'All 178 math links (38 target skills) checked with the game\'s own code against the installed content '
           '(MATH_REF_VALIDATION.json: skill ID, course release, bank version or file hash, question types, auto-checkable '
           'count). Grade 7 sets 63/65/66 exist in the live Grade 7 v2.0.0 bank. The ALG1-S75 link was removed. A real '
           'import and play-through (RUNTIME_CHECK.json) confirmed routing in order, no explanation or recording required, '
           'return to the FL set, mastery, the 300-second reward, and Go Deeper unlock. Remediation serves the target '
           'skill\'s auto-checkable items, which include typed numeric answers; whether that is acceptable for a '
           'choice-only course is the owner\'s decision (MATH_BRANCHES.md).'),
    'P4': ('Done',
           'Thresholds unchanged (3 or fewer of 5 -> backward; 4 -> repeat MAIN; 5 -> Go Deeper), confirmed in the game '
           'config and runtime test. Branch fit reviewed: S14 now links Grade 7 set 29 instead of systems of equations; '
           'S25/S26 link Grade 6 percent and exponent skills instead of Algebra I; S67\'s step-function link removed. All '
           'listed missing givens fixed, plus a bank-wide sibling scan added to every build (2 more questions fixed: '
           'S70-F2-Q3, S113-F1-Q5). QUALITY_AUDIT.md no longer claims global self-containment beyond what the checks show.'),
    'P5': ('Done',
           'how_to flags audited: 18 recognition-only questions unflagged (240 flagged now). Ordered steps exist for '
           'opening an account, opening and funding a Roth IRA, filing taxes, renting, and buying a car (HOW_TO.md '
           'walkthroughs). Intro / knowledge-check counts reported in QUALITY_AUDIT.md; the short-teach, easy-MC model '
           'is unchanged.'),
    'P6': ('Done',
           'Rebuilt everything from one source: question and answer PDFs (full and parts), JSON, CSV, per-set and index '
           'JSON, reports, manifest, and FinancialLiteracy_Nexus_Import_v1.1.0.zip. fl_crosscheck.py confirms every '
           'question has the same ID, choices, key, and page in the package JSON, JSON/CSV keys, and full and split PDFs '
           '(EXPORT_CROSSCHECK.json: 0 problems). QUALITY_AUDIT.md rewritten (exact-text '
           'uniqueness, calc limits, catalog vs runtime, sibling scan). CHANGES.md / .json list every changed question by '
           'original ID with old/new key, reason, source, and whether the answer changed. Question IDs are unchanged and '
           'unchanged questions keep their v1.0.0 answer letters. The course has never been released, so no student '
           'progress needs migrating; if a test import exists, re-import v1.1.0 over it only after review.'),
}

# Changed questions the reviewer did not name, mapped to the finding they belong to.
EXTRA = {
    'S5-F2-Q1': 'R28', 'S30-M-Q1': 'R28', 'S30-M-Q3': 'R28', 'S30-F1-Q1': 'R28', 'S30-F1-Q3': 'R28', 'S30-F1-Q4': 'R28',
    'S30-F1-Q5': 'R28', 'S30-F2-Q3': 'R28', 'S31-M-Q3': 'R28', 'S31-F2-Q3': 'R28', 'S31-F2-Q4': 'R28', 'S33-F2-Q1': 'R28',
    'S83-M-Q1': 'R28', 'S83-F1-Q2': 'R28',
    'S8-F2-Q4': 'R25', 'S11-M-Q4': 'C12',
    'S36-M-Q2': 'R15', 'S36-M-Q3': 'R15', 'S36-M-Q4': 'R15', 'S42-M-Q5': 'R15', 'S42-F2-Q1': 'R15',
    'S32-B1-Q3': 'R31', 'S37-M-Q4': 'R31', 'S56-B1-Q3': 'R31', 'S65-F2-Q4': 'R31', 'S80-M-Q3': 'R31',
    'S54-M-Q2': 'R73', 'S54-F2-Q4': 'R73', 'S56-F2-Q1': 'R73',
    'S65-F2-Q1': 'R51', 'S78-M-Q2': 'R58', 'S78-M-Q3': 'R58',
    'S70-F2-Q3': 'P4', 'S113-F1-Q5': 'P4', 'S113-F1-Q4': 'P4',
    'S10-M-Q1': 'P5', 'S13-F2-Q4': 'P5', 'S16-F1-Q3': 'P5', 'S16-F1-Q4': 'P5', 'S20-F2-Q5': 'P5', 'S21-F2-Q3': 'P5',
    'S29-F2-Q1': 'P5', 'S39-F1-Q3': 'P5', 'S40-F1-Q5': 'P5', 'S59-F1-Q5': 'P5', 'S60-B1-Q4': 'P5', 'S87-M-Q5': 'P5',
    'S96-F1-Q5': 'P5', 'S101-M-Q2': 'P5', 'S101-F1-Q3': 'P5',
}

# Source reference (review section 5) per finding, for the change log.
SOURCE_REF = {'R04': 'A1', 'R05': 'A2', 'R06': 'A1', 'R07': 'A3', 'R08': 'A4', 'R09': 'A5', 'R10': 'A6', 'R11': 'A7',
              'R12': 'A8', 'R13': 'A9', 'R14': 'A10', 'R15': 'A11', 'R25': 'A12', 'R27': 'A13', 'R28': 'A14',
              'R44': 'A15', 'R45': 'A15', 'R46': 'A16', 'R47': 'A15', 'R58': 'A17', 'C03': 'A18', 'C11': 'A16',
              'C20': 'A19', 'C26': 'IRS Topic 409', 'R53': 'A1'}
