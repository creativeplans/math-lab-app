# Financial Literacy — independent review and Claude Code correction handoff

Reviewed October 15, 2026. Package: `FinancialLiteracy_Nexus_Import_v1.0.0.zip` and its accompanying PDFs, JSON, CSV, and seven Markdown reports.

**Decision: revise before importing into the game.** The package is internally consistent, but the content is not ready for final approval. There are incorrect or outdated rules, incorrect numerical wording/results, ambiguous choices, missing givens, and unresolved branch integration requirements. The author’s warning about unverified official sources was substantive.

This is a full-bank content read-through, not a sample of questions. It does not certify that the running Nexus importer, progress system, or cross-course question renderer works: those application files were not supplied. It also does not establish originality against every external question bank. Official-source checks resolve the specific issues below; they do not turn every original source claim into a verified claim automatically.

## Instructions to Claude Code

Implement all required corrections below and report the disposition of every numbered finding. Apply wording, choices, key, teaching, feedback, misconception-note, source, and metadata changes together. Preserve existing question IDs for corresponding revised questions. Do not silently overwrite a deployed course; prepare a revised version for review before import.

Keep the beginner-friendly written teaching, easy multiple choice, conceptual backward help, existing math references where valid, and optional Go Deeper structure. Do not add recording requirements or outside paid tools. Keep legal and financial language simple while stating the conditions needed for a unique answer.

A “required correction” means the current item or claim needs repair. It does not always mean the keyed letter is wrong. Many intended answers become valid once a missing condition is supplied. Recommendations are separate and do not have the same status.

## 1. What passed

| Check | Result |
|---|---|
| Scope | 113 sets across 19 units; 2,130 questions |
| Local question sections | 565 MAIN; 565 concept-backward; 1,000 Go Deeper |
| Question identifiers | All 2,130 unique; package/index/key IDs agree |
| Local structure | Every local question section has five questions and four choices |
| JSON/key/CSV consistency | Compared prompts, teaching where present, answer choices, keys, feedback, pages, and relevant exports; CSV choices and all misconception fields match the answer JSON |
| Correct positions | A 532; B 533; C 533; D 532 |
| Full PDFs | Question and key PDFs each have 2,243 pages; the 113 additional pages are set overviews |
| PDF content | Extracted question/intro/choice and key/feedback text agrees with the supplied JSON at the referenced pages |
| Split PDFs | Each split sequence is 800 + 800 + 643 pages and preserves the full document text in order |
| Manifest | All 127 listed files match their supplied byte counts and SHA-256 hashes |
| Supporting reports | The seven uploaded Markdown reports match their packaged copies |
| Page bounds/layout | No extracted text outside page bounds across either full PDF; 21 question pages and 10 key pages visually inspected without a visible clipping/layout problem |

The numerical review included independent evaluation of printed arithmetic and compound-growth formulas, and independent loan-payment/payoff simulations. A simple expression scanner examined 870 candidate equation segments; its raw flags included harmless partial expressions and notation differences, so they were manually triaged rather than counted as 27 content errors. Examples independently confirmed include the mortgage payments, refinance payments, extra-$200 mortgage payoff (262 months), and the minimum-payment model once its missing $25 floor is supplied.

The 869 numeric `calc` values in the answer JSON are stored results, not executable recomputation formulas. The author’s build engine was not in the supplied ZIP. Matching a stored result to a choice is useful consistency checking, but does not independently establish that all assumptions and calculations are correct. Do not claim this review independently reproduced 869 complete solution models.

## 2. Required question and teaching corrections — 73 findings

Pages refer to the supplied full question PDF and matching full answer PDF, not restarted page numbers in split files. Recalculate page references after rebuilding.

### R01 — `S5-F1-Q2` (p. 97)

**Issue:** The keyed claim that purchases under $10 each cost over $40 after a $34 fee does not follow. A $1 purchase costs $35.

**Required edit:** Specify a $9 purchase, producing $43, or use the correct expression: purchase price plus $34. Update feedback and misconception notes.

### R02 — `S26-F1-Q4` (p. 540)

**Issue:** The Rule of 72 answer is rounded incorrectly. $500 × 2^(48×7/72) = $12,699.208…, so the requested nearest hundred is $12,700, absent from the choices. The feedback also approximates the exact compound result incorrectly.

**Required edit:** Replace the keyed $13,000 with $12,700; avoid rounding the number of doublings before exponentiating. Exact annual compounding gives $12,864.45, or $12,900 to the nearest hundred. Rebuild choices, calc, and feedback.

### R03 — `S83-F2-Q5` (p. 1743)

**Issue:** The question asks for the highest TOTAL cost, but B has the highest interest cost, not the highest total repayment.

**Required edit:** Prefer asking for the highest total INTEREST cost. Then B remains correct: $3,960.48 interest. Total repayments are A $22,099.80; B $18,960.48; C $21,903.84; D $21,385.20. If asking total repayment, key A instead.

### R04 — `S109-M-Q4` (p. 2168)

**Issue:** The answer denying a separate charitable deduction to someone taking the standard deduction is outdated for tax year 2026. A date stamp alone does not fix this.

**Required edit:** Use an explicitly stated tax year, filing status, and eligible cash donations. Beginning in 2026, eligible nonitemizers may deduct up to $1,000, or $2,000 married filing jointly. Replace the answer choices and explanation. Also update the S109 source claim and related S66 teaching. See source A1.

### R05 — `S93-M-Q2` (p. 1905); `S93-F1-Q1` (p. 1914)

**Issue:** These teach that unpaid Direct Unsubsidized Loan interest is capitalized when repayment first begins. That is not the general current rule.

**Required edit:** Use a clearly labeled hypothetical private loan whose contract provides for capitalization, or a current qualifying federal capitalization event. Preserve the distinction between accrued interest still owed and interest added to principal. Do not present $6,820 as the automatic new federal principal on entering repayment. See A2.

### R06 — `S87-F1-Q4` (p. 1816)

**Issue:** A $500 deductible alone is insufficient to establish HSA contribution ineligibility under 2026 rules. The question also asks about opening an account rather than eligibility to contribute.

**Required edit:** Ask whether Ana may CONTRIBUTE for that period. Specify that her plan is not HSA-compatible and is neither an eligible bronze nor catastrophic plan. Explain that these plans became HSA-compatible in 2026; avoid teaching the old HDHP-only rule without the exception. See A1.

### R07 — `S34-B1-Q4` (p. 703)

**Issue:** A $35 credit-card late fee on a $25 required minimum payment is presented as an ordinary lawful example. Regulation Z caps the late fee at the associated minimum payment.

**Required edit:** Use a lawful fee, for example $20 on a $25 minimum: 80%. Alternatively explicitly ask students to identify the unlawful fee. Change the calculation and all answer materials. See A3.

### R08 — `S2-F2-Q3` (p. 40)

**Issue:** The bank makes only $225 of an ordinary $600 Monday check deposit available Tuesday and the rest Thursday, without explaining a lawful hold exception. $225 is the old next-day minimum.

**Required edit:** For a normal covered check deposited before cutoff into an established account, use at least $275 Tuesday and the usual applicable remaining-funds schedule. If teaching an exception or a mobile-deposit policy, identify it explicitly and source the rules. Update all related amounts; do not merely change the answer letter. See A4.

### R09 — `S70-B1-Q1` (p. 1456)

**Issue:** April 15 on Saturday does not support the keyed Monday federal tax deadline: Monday April 17 is the observed D.C. Emancipation Day holiday in that calendar.

**Required edit:** Use an actual calendar with the holidays included; the general federal deadline in that case is Tuesday April 18. Alternatively make this a generic office deadline with an explicitly holiday-free Monday. Correct the weekday/date distractor too. See A5.

### R10 — `S100-M-Q5` (p. 2025)

**Issue:** The FTC explanation incorrectly uses the $25 threshold for temporary-location sales and calls the cancellation window simply three days.

**Required edit:** Teach covered home sales of $25 or more versus temporary-location sales of $130 or more, subject to exceptions. Key THREE BUSINESS DAYS. Saturday counts; Sunday and federal holidays do not. The $400 home-sale example can remain. See A6.

### R11 — `S100-F1-Q2` (p. 2032)

**Issue:** The debt-validation deadline is measured from first contact in the stem. The relevant validation period follows receipt, or assumed receipt, of validation information.

**Required edit:** Replace first contact with receipt of the validation notice/information and accurately describe the 30-day written-dispute right. Keep the right distinct from a general ability to dispute a debt later. See A7.

### R12 — `S100-M-Q2` (p. 2022)

**Issue:** The stem says Rosa waits ten days without identifying whether that is after theft or after she discovered the loss. Federal debit-card liability uses discovery.

**Required edit:** State ten days after learning the card was stolen, including more than two business days, and within the applicable statement window. Audit related Reg E summaries: the possible liability for later transfers after 60 days is not a blanket retroactive removal of protection for all earlier transactions. See A8.

### R13 — `S100-F1-Q1` (p. 2031)

**Issue:** FCBA teaching says a written dispute can simply be mailed within sixty days. The statutory notice must be received within the applicable period.

**Required edit:** Say the issuer receives her written billing-error notice at its designated billing-inquiries address on June 15, within 60 days after transmitting the statement. The intended yes answer can remain. See A9.

### R14 — `S35-M-Q5` (p. 720)

**Issue:** The under-21 rule omits independently available assets as an ability-to-pay source. No income does not by itself rule out independent qualification.

**Required edit:** Include independent income OR assets sufficient for minimum payments, or an eligible cosigner/joint applicant age 21 or older with ability to pay if the issuer permits that arrangement. If the scenario needs the cosigner route, state no qualifying independent assets. See A10.

### R15 — `S35-M-Q3` (p. 718); `S35-F1-Q3` (p. 728); `S36-M-Q1` (p. 737); `S36-F2-Q4` (p. 755); `S42-F1-Q5` (p. 877)

**Issue:** Paying a statement balance in full is treated too broadly as eliminating interest; S36-F2-Q4 promises autopay guarantees no late fees and no interest.

**Required edit:** For purchase-interest examples state an offered, currently available purchase grace period, no interest-bearing cash advances or other excluded balances, and full timely payment. Replace the autopay guarantee with a risk-reduction statement, or explicitly assume adequate funds and successful on-time processing. Check every repetition. See A11.

### R16 — `S11-F1-Q1` (p. 222); `S69-M-Q3` (p. 1432); `S69-M-Q4` (p. 1433); `S69-M-Q5` (p. 1434); `S69-B1-Q4` (p. 1438); `S69-F1-Q2` (p. 1441)

**Issue:** Refunds are repeatedly taught as proof of excess withholding. Refundable credits and other payments can also produce refunds.

**Required edit:** Scope the fictional examples to refunds entirely from overwithholding, with no refundable credits or other payments. Rewrite general teaching so it includes those other sources; S69 liability = withholding − refund is only valid under its stated simplified assumptions. Do not undo the correct refundable-credit teaching in S68.

### R17 — `S11-F2-Q5` (p. 231)

**Issue:** An earned-income amount alone does not establish an expected federal income-tax liability for the W-4 exemption test. Filing status, deductions, and credits matter.

**Required edit:** State explicitly that Jamal expects a positive federal income-tax liability this year, or provide enough tax facts to calculate it. Keep tax liability separate from a balance due when filing.

### R18 — `S12-B1-Q5` (p. 242)

**Issue:** Job X merely offers health insurance; its employee premium is not given. The $3,600 comparison assumes that coverage is free to the employee.

**Required edit:** State Job X pays the entire premium for the same coverage that costs $300 per month at Job Y. Then $3,600 is supported.

### R19 — `S17-F2-Q5` (p. 357)

**Issue:** The data show eating-out overspending in all three months, yet the keyed explanation describes one unusual month and an otherwise close plan.

**Required edit:** Change the answer to repeated overspending requiring review of actual habits and budget assumptions, or change the scenario so only one month is over budget and explain its unusual expense.

### R20 — `S20-B1-Q2` (p. 407)

**Issue:** Several choices can be legitimate phone-plan decision criteria: price, a free case, and friends using a carrier. The question does not specify the decision goal.

**Required edit:** Ask specifically for a recurring-cost criterion, or provide Sam’s explicit criteria. Make every remaining distractor wrong under the stated goal.

### R21 — `S7-M-Q3` (p. 130)

**Issue:** The keyed answer concerns reversibility of an authorized payment, but another option says the seller must legally deliver the tickets, also generally true of an enforceable sale.

**Required edit:** Ask which statement is most accurate about reversing or recovering the app payment. Replace the contractual-obligation distractor. Avoid treating all fraud-induced payments as legally identical to unauthorized account takeovers.

### R22 — `S1-M-Q3` (p. 4)

**Issue:** A Teachers credit-union name does not establish its actual membership rules or whether Jordan qualifies.

**Required edit:** State the credit union’s field-of-membership rule in the scenario. Then ask whether Jordan meets it or which step he should take to verify eligibility.

### R23 — `S2-B1-Q1` (p. 28); `S2-B1-Q4` (p. 31); `S2-B1-Q5` (p. 32)

**Issue:** The teaching defines credit universally as borrowing and implies debit can never create debt or overspending. Elsewhere the course teaches debit overdrafts.

**Required edit:** Use CREDIT CARD when describing borrowing. State a debit purchase uses available deposits when there is no overdraft, and specify overdraft disabled/decline behavior if a question promises a spending limit. Preserve the distinction from statement credits in S4.

### R24 — `S5-B1-Q5` (p. 95)

**Issue:** Checking a balance alone cannot prevent an overdraft if the student still makes an unaffordable purchase.

**Required edit:** Key checking available funds AND postponing or reducing the purchase, or adding cleared funds first. Mention pending transactions where relevant.

### R25 — `S8-M-Q2` (p. 150); `S8-F1-Q3` (p. 161)

**Issue:** Overtime examples need the covered, nonexempt employee condition; being hourly alone is not enough.

**Required edit:** State covered nonexempt status and hours in one workweek locally in each graded overtime scenario. For S8-F2-Q4, call the $15 figure the applicable state minimum rather than suggesting the federal dollar minimum is $15. See A12.

### R26 — `S19-M-Q4` (p. 383)

**Issue:** The intro says sales tax is always computed after a discount. Coupon treatment depends on the kind of discount and jurisdiction.

**Required edit:** Specify a retailer-funded discount and a scenario where tax applies to the discounted selling price. Keep the stated calculation; remove the universal legal claim.

### R27 — `S27-F2-Q5` (p. 567)

**Issue:** The intro groups savings bonds with marketable Treasuries as purchasable through banks or brokers.

**Required edit:** Distinguish new electronic savings bonds purchased through TreasuryDirect from marketable Treasury bills, notes, and bonds that can be purchased through banks/brokers. The TreasuryDirect keyed option can remain. See A13.

### R28 — `S29-M-Q1` (p. 590); `S29-F1-Q1` (p. 600); `S29-F1-Q2` (p. 601); `S29-F1-Q3` (p. 602); `S76-F1-Q1` (p. 1587); `S76-F1-Q2` (p. 1588)

**Issue:** The course defines APR as including certain fees, then uses it as the contractual interest rate in interest, APY, and mortgage-payment formulas. These quantities need not be equal.

**Required edit:** Use the annual NOTE INTEREST RATE in periodic-interest and amortization formulas. If using APR as that rate in a simplified loan, explicitly state no additional finance charges and that APR equals the nominal note rate. Audit S29–31, S76, and other loan calculations consistently. See A14.

### R29 — `S29-M-Q3` (p. 592); `S29-F1-Q5` (p. 604)

**Issue:** The one-year loan cost/APR calculations lack a repayment schedule and fee timing. Monthly amortization or deducting a fee from proceeds changes the result.

**Required edit:** For the intended simple calculations state full principal received at the start, no interim repayment, and all principal, interest, and the stated additional fee paid at year end. Otherwise calculate the appropriate cash-flow APR. Do not silently equate interest rate plus fee percentage to APR for an amortizing loan.

### R30 — `S31-M-Q1` (p. 632)

**Issue:** The intro says early payments are mostly interest, but its own $10,000, 6%, 60-month example begins with $50 interest and $143.33 principal.

**Required edit:** Say the interest share is higher early and declines as the balance falls; do not claim it must exceed half the payment. Qualify similar general statements elsewhere; the 30-year mortgage example really is mostly interest.

### R31 — `S31-M-Q2` (p. 633); `S37-F2-Q2` (p. 774); `S49-F1-Q3` (p. 1022); `S80-F1-Q2` (p. 1672); `S81-F1-Q2` (p. 1693); `S95-F1-Q4` (p. 1949); `S110-F1-Q2` (p. 2192)

**Issue:** These questions need numerical givens from another question even though the package says section questions are shuffled.

**Required edit:** Restate locally: S31 initial $10,000; S37 the $1,000 at 0% and $500 at 22%, plus relevant payment-allocation assumptions; S49 current stocks $7,200; S80 monthly savings $137.45; S81 starting 5.5% and first-adjustment cap two percentage points; S95 $20 price/$8 variable cost; S110 $1,600 annual raise. Audit all sibling references, not only these examples.

### R32 — `S38-M-Q1` (p. 779); `S38-M-Q3` (p. 781); `S38-M-Q4` (p. 782)

**Issue:** The stated minimum-payment formula has no dollar floor, but the 176-month/$6,983.44 payoff result requires one. Without a floor, a 1%-of-balance principal payment never fully repays the balance in finite months.

**Required edit:** State the minimum is the greater of $25 OR 1% of balance plus monthly interest, capped at the final payoff amount, using the assumed monthly-interest model. Independent simulation with that $25 floor gives 176 months and $6,983.443…; the quoted result is supported only after adding this rule.

### R33 — `S34-F2-Q1` (p. 710)

**Issue:** Three years since an account was reported is not necessarily three years since the delinquency that started its credit-reporting period.

**Required edit:** Give the original delinquency/reporting-period start facts, not just the date it first appeared on a report. Label the seven-year calculation an approximation under the stated reporting rule; do not imply sale to a collector restarts the clock.

### R34 — `S34-F2-Q3` (p. 712)

**Issue:** Accurate negative information is said categorically to be impossible to remove early. A consumer generally cannot compel deletion just because information is unfavorable, but voluntary deletion is possible.

**Required edit:** Teach no legal right to demand removal of accurate current information and no legitimate guarantee of paid credit repair removing it. Keep disputes of inaccurate information distinct.

### R35 — `S39-B1-Q5` (p. 809)

**Issue:** No foreign travel does not establish no foreign-transaction fees: online purchases processed internationally can incur them.

**Required edit:** Specify no foreign-currency or foreign-processed transactions, or explain that these fees can apply without leaving the country.

### R36 — `S42-F1-Q2` (p. 874)

**Issue:** Charging $30 monthly and paying in full does not establish that the reported balance is $30. Utilization depends on the reported balance and limit.

**Required edit:** State that $30 is the reported statement balance on a $300 limit, with no other balances. Then 10% utilization follows.

### R37 — `S44-F1-Q2` (p. 916); `S45-M-Q3` (p. 928); `S45-M-Q4` (p. 929); `S45-B1-Q3` (p. 933); `S45-B1-Q5` (p. 935); `S60-M-Q1` (p. 1241); `S60-B1-Q1` (p. 1246)

**Issue:** Cash is repeatedly described as never invested even though the course explicitly allows an automatic money-market fund core position. A money-market mutual fund is an investment.

**Required edit:** Distinguish bank-sweep/uninvested cash from money-market fund shares. If the target is choosing a long-term stock/bond allocation, say the student has not bought the intended long-term investment. Do not mark every automatic fund purchase as no investment.

### R38 — `S47-F2-Q1` (p. 983)

**Issue:** The question asks how much is received at maturity; both $1,000 principal and $1,020 including a final annual coupon can be defended.

**Required edit:** Ask for PRINCIPAL REPAYMENT ONLY, excluding any final interest payment, and assume no default. Then $1,000 is unique.

### R39 — `S47-F1-Q5` (p. 982)

**Issue:** Holding hundreds of bonds does not establish holding hundreds of different issuers.

**Required edit:** State the fund holds bonds from many independent issuers if issuer diversification is the reason for the answer. Hundreds of Treasuries can all share the same issuer.

### R40 — `S48-B1-Q2` (p. 995)

**Issue:** A fund with 400 stocks does not establish the weight of the one that falls or what happens to the others.

**Required edit:** Give equal weights, or the stock’s specific portfolio weight, and hold other prices constant. Then the limited effect on the entire fund follows.

### R41 — `S28-M-Q4` (p. 572); `S48-F2-Q1` (p. 1004); `S49-B1-Q2` (p. 1016); `S50-F1-Q5` (p. 1045)

**Issue:** Wrong-answer options are textually different but semantically duplicate: larger unsecured loans; higher fees supposedly proving better management; the whole business suffering equally; and stop versus stop-loss orders.

**Required edit:** Replace one option in each repeated pair with a distinct plausible misconception. The exact pairs are B/C in S28, A/D in S48, B/D in S49, and B/C in S50. Recheck misconception notes and shuffled choices.

### R42 — `S49-B1-Q1` (p. 1015)

**Issue:** A banana shortage alone does not prove the whole banana-only business suffers: its inventory, pricing, and contracts are unspecified.

**Required edit:** State the seller cannot obtain bananas and therefore cannot make sales, while a diversified seller still has other products to sell.

### R43 — `S49-F1-Q1` (p. 1020)

**Issue:** The answer 65% is correct, but feedback rounds 65.4545… to 65.5 and then says to round down. That is a misleading rounding method.

**Required edit:** Write $7,200 ÷ $11,000 × 100 = 65.4545…%, which rounds directly to 65% to the nearest whole percent. Avoid intermediate rounding.

### R44 — `S56-M-Q5` (p. 1161); `S56-F1-Q1` (p. 1167); `S56-F1-Q3` (p. 1169)

**Issue:** Direct rollover teaching guarantees tax deferral without specifying compatible pretax accounts; a pretax-to-Roth rollover is generally taxable. Feedback also promises withheld money comes back at tax time.

**Required edit:** Scope to an eligible pretax distribution directly rolled to a traditional IRA or another accepting pretax plan. Explain that withholding is credited on the tax return and can offset tax liability; it is not guaranteed to arrive as a separate refund.

### R45 — `S57-M-Q4` (p. 1181); `S61-F1-Q1` (p. 1272); `S61-F1-Q2` (p. 1273)

**Issue:** Traditional IRA withdrawal examples treat the entire distribution as taxable without ruling out nondeductible contribution basis.

**Required edit:** State the traditional IRA consists entirely of pretax amounts and has no after-tax basis. Otherwise apply the relevant pro-rata taxation rule. Keep general descriptions qualified as generally taxable. See A15.

### R46 — `S58-M-Q1` (p. 1199); `S58-M-Q2` (p. 1200); `S58-F2-Q4` (p. 1217); `S61-F2-Q1` (p. 1277); `S61-F2-Q3` (p. 1279)

**Issue:** The rule requiring the individual’s own earned income is stated universally and can incorrectly exclude an eligible nonworking spouse on a joint return.

**Required edit:** Use eligible compensation and explain the spousal IRA exception briefly. For the no-job/low-compensation examples specify unmarried status or no qualifying spousal compensation. Also distinguish aggregate traditional-plus-Roth contribution limits from a separate limit per account. See A16.

### R47 — `S61-M-Q1` (p. 1262); `S61-B1-Q4` (p. 1270); `S61-B1-Q5` (p. 1271)

**Issue:** Roth ordering rules omit conversion and rollover amounts between regular contributions and earnings. Ten-percent additional tax is also described only in terms of taxable amounts, overlooking conversion recapture.

**Required edit:** Teach regular contributions, then conversions/rollovers under their rules, then earnings; or explicitly scope the beginner examples to regular contributions only, no conversions or rollovers. Keep conversion-specific rules separate from the qualified-distribution five-year clock. See A15.

### R48 — `S59-F2-Q4` (p. 1238); `S60-F2-Q3` (p. 1258)

**Issue:** The amount available as regular-contribution basis is described as total lifetime contributions, without subtracting amounts already withdrawn. It is also limited by current funds available.

**Required edit:** For the calculation specify no prior distributions, conversions, or corrections. In general teaching say remaining undistributed regular-contribution basis across the owner’s Roth IRAs, subject to funds available. Do not promise lifetime contributions can be withdrawn repeatedly.

### R49 — `S60-F2-Q4` (p. 1259)

**Issue:** Feedback says selling in a panic turns a temporary drop into a permanent loss. A decline is not guaranteed temporary, and selling does not prevent all later reinvestment.

**Required edit:** Say panic selling realizes a current loss and may cause the investor to miss a recovery. Preserve the risk-aware, long-term diversified-investing lesson without a guaranteed recovery.

### R50 — `S64-F1-Q1` (p. 1335)

**Issue:** Why Box 1 MIGHT be lower than Box 3 has both the intended pretax-contribution answer and an employer-error answer. An error is possible.

**Required edit:** State that the W-2 is accurate and the worker made the specified pretax contribution, or replace the employer-error option with an actually incorrect explanation.

### R51 — `S65-M-Q3` (p. 1348)

**Issue:** The intro says dependents get a smaller standard deduction as a universal result. Some reach the same regular cap as comparable nondependents.

**Required edit:** Say a dependent’s deduction MAY be limited, often using earned income and an annual cap. Keep the explicitly hypothetical arithmetic in F2, but remove categorical smaller-deduction claims.

### R52 — `S65-F1-Q2` (p. 1357)

**Issue:** Filing status affects both tax brackets/deductions and payroll withholding settings, making the withholding distractor potentially defensible.

**Required edit:** Ask specifically how filing status affects calculation of the final tax on the return, or replace the withholding distractor.

### R53 — `S66-M-Q1` (p. 1367); `S66-F1-Q3` (p. 1379); `S66-F2-Q3` (p. 1384)

**Issue:** Simplified taxable-income teaching omits newer additional deductions available without itemizing, and one intro implies ordinary AGI directly determines Roth eligibility.

**Required edit:** Label the examples as having no other adjustments or additional deductions. Account for 2026 charitable rules where relevant; explain that Roth eligibility uses modified AGI, not necessarily plain AGI. Do not treat a simplified equation as the entire current federal tax system.

### R54 — `S68-M-Q3` (p. 1411)

**Issue:** Feedback says an unused nonrefundable credit is simply lost. Some credits have carryforward rules.

**Required edit:** Say the unused amount is not refunded this year; whether it can be carried to another year depends on the specific credit. If the intended result is permanent loss, state the hypothetical credit has no carryforward.

### R55 — `S70-F1-Q2` (p. 1462)

**Issue:** The IP PIN explanation says all returns without it are rejected. That describes e-file behavior too broadly for paper returns.

**Required edit:** Specify that an e-filed return lacking the correct required IP PIN is rejected. Paper returns may require additional verification and processing. Do not claim that a PIN makes identity fraud impossible.

### R56 — `S74-F1-Q3` (p. 1547)

**Issue:** Actual-cash-value teaching subtracts depreciation from a TV’s original $1,000 price, rather than explicitly using current replacement cost.

**Required edit:** State current replacement cost is $1,000 and the policy’s depreciation is 60%, so actual cash value before deductible is $400.

### R57 — `S77-F1-Q2` (p. 1609)

**Issue:** The question uses two homes’ $350,000 prices as assessed values, although it teaches assessment-based property tax.

**Required edit:** Specify both homes are assessed at $350,000 for these tax calculations. Otherwise purchase price alone cannot determine the tax difference.

### R58 — `S78-B1-Q4` (p. 1627)

**Issue:** The mortgage section teaches business days as excluding all weekends. For the Closing Disclosure waiting period, Saturday generally counts; the Loan Estimate delivery rule uses a different business-day definition.

**Required edit:** Make this a generic office open Monday–Friday arithmetic example, or teach the two relevant mortgage definitions accurately. Keep the Monday/Thursday and Friday/Tuesday examples only with appropriate receipt/delivery assumptions. See A17.

### R59 — `S80-F2-Q5` (p. 1680)

**Issue:** Adding one-twelfth of a payment monthly is said to give the same result as biweekly half-payments. It gives the same extra annual amount but not necessarily identical interest or payoff timing.

**Required edit:** Say similar payoff benefits or the same extra annual payment amount. Explain application timing and servicer handling rather than claiming exact equivalence.

### R60 — `S81-B1-Q2` (p. 1688)

**Issue:** A rate increase is said to always raise the loan payment. Some loan arrangements keep the payment while changing amortization or have different reset mechanics.

**Required edit:** Scope to a fully amortizing loan whose payment is recalculated at the higher rate with the same balance and remaining term.

### R61 — `S85-M-Q4` (p. 1769)

**Issue:** The $2,000 due at signing may include the first $399 payment, in which case adding all 36 payments double-counts it.

**Required edit:** State $2,000 is an upfront charge separate from all 36 payments, with no other charges included in this simplified total. Then $16,364 is supported.

### R62 — `S85-F2-Q4` (p. 1784)

**Issue:** The keyed explanation says a lease payment covers ONLY expected depreciation, contradicting the course’s own finance-charge and tax explanation.

**Required edit:** Use depreciation plus rent/finance charges and applicable taxes/fees, rather than paying the full purchase principal. Keep the comparison simplified and scoped.

### R63 — `S87-M-Q1` (p. 1803); `S87-M-Q2` (p. 1804); `S87-F1-Q2` (p. 1814); `S87-F1-Q3` (p. 1815)

**Issue:** Health-plan calculations need the applicable allowed in-network charges and deductible/out-of-pocket progress. Coverage alone does not determine those figures.

**Required edit:** Specify allowed in-network amounts, no earlier spending in the plan year, and that these services follow the stated deductible and coinsurance rules. If examples are independent, say so; a second bill after the first changes year-to-date spending.

### R64 — `S95-F2-Q1` (p. 1951)

**Issue:** June sales are not necessarily June cash received, so $900 in sales minus $1,100 paid is not necessarily cash flow.

**Required edit:** State Dev COLLECTED $900 in June and paid $1,100 in June, with no other cash flows in the example. Then −$200 is correct. Preserve the distinction from accounts receivable.

### R65 — `S97-F1-Q4` (p. 1986)

**Issue:** Earning $6 per item does not establish how much is available to cover the booth rent if that is gross revenue or net profit after rent.

**Required edit:** Say each item contributes $6 after all per-item variable costs and before the $150 booth charge. Then 25 items cover the booth.

### R66 — `S98-M-Q3` (p. 1991)

**Issue:** A credit freeze is described as stopping all new accounts. It restricts access to certain credit reports and does not block every type of identity theft or account opening.

**Required edit:** Say it helps prevent new credit fraud by limiting access to the frozen credit reports. Avoid a guarantee covering bank deposits, services, existing accounts, or every lender. Keep the recommendation to freeze all three major bureaus.

### R67 — `S99-M-Q2` (p. 2006)

**Issue:** The keyed fake-check loss assumes Rosa shipped the bike and sent $1,200, neither action being explicitly stated in the question.

**Required edit:** Add both completed actions and state the $300 remainder from the deposit is still in her account when the check is reversed. Then the net loss is $1,200 plus the bike, excluding any separately stated fees.

### R68 — `S108-F1-Q5` (p. 2163)

**Issue:** Buying a TV on a card is said to immediately reduce net worth by unspecified resale depreciation. The current asset value is not given.

**Required edit:** Supply the TV’s immediate resale/market value, for example $800 with $1,000 new debt, producing a $200 decrease. Do not teach that every asset purchased with debt automatically has an immediate specified loss.

### R69 — `S110-F1-Q3` (p. 2193)

**Issue:** Increasing a contribution rate annually is labeled AUTOMATIC escalation without saying it is automatic, and 1% can be confused with one percentage point of pay.

**Required edit:** State Nia enables the plan to automatically increase her contribution rate by one percentage point of salary each year.

### R70 — `S111-M-Q3` (p. 2199)

**Issue:** The roommate split is keyed as equal without stating equal shares.

**Required edit:** Say the two roommates split both rent and the stated utilities equally. Then $1,140 per person follows.

### R71 — `S112-B1-Q3` (p. 2220)

**Issue:** A free mug also has monetary value, so the stem asking for a benefit worth money has more than one defensible answer.

**Required edit:** Ask for a retirement-savings benefit that adds employer contributions, or replace the mug with a clearly nonfinancial distractor.

### R72 — `S113-M-Q4` (p. 2232)

**Issue:** Regular investing is presented as building wealth without identifying diversified holdings or keeping the result conditional.

**Required edit:** State a diversified investment and key that regular investing CAN help build wealth over time while losses remain possible. A recurring purchase by itself does not establish a sound investment.

### R73 — `S7-F2-Q5` (p. 147); `S59-F2-Q1` (p. 1235); `S71-M-Q2` (p. 1473); `S55-F2-Q3` (p. 1153); `S46-F2-Q3` (p. 964)

**Issue:** Several explanations use unsupported empirical claims: verification prevents most losses/scams; MFA blocks most takeovers; the most common reason young workers do not save; and unnamed fund-manager studies.

**Required edit:** Remove unsupported frequency/ranking claims or cite a specific credible primary study with population, date, and relevant horizon. Prefer which scenario illustrates present bias for S55. For the fund comparison specify the benchmark and period, or teach the fee/diversification reasoning without claiming an unnamed study proves it.

## 3. Recommendations and precision improvements

**C01 — `S1-F2-Q1` (p. 17); `S3-M-Q5` (p. 48); `S5-F1-Q1` (p. 96):** For exact annual or six-month fee totals, replace usually/about with explicit fee-triggering conditions for every billing period.

**C02 — `S5-M-Q2` (p. 87):** The $70 fee count is correct. Explain the full running balance including charged fees if showing balances: the ending amount after all listed purchases and both fees is −$85.

**C03 — `S8-F2-Q3` (p. 166):** Keep the reporting lesson, but distinguish cash/charged tips, the $20-per-month-per-employer reporting threshold, and noncash tips. Explain that reportable income and a possible qualified-tip income-tax deduction are different; payroll taxes can still apply. Do not incorrectly conclude tips no longer need reporting. See A18.

**C04 — `S13-M-Q3` (p. 256); `S96-M-Q2` (p. 1958):** Use 92.35% of NET PROFIT to obtain net earnings generally subject to SE tax. State no other wages reaching the Social Security wage base and no Additional Medicare Tax in these simplified examples.

**C05 — `S13-F2-Q3` (p. 271); `S96-M-Q3` (p. 1959):** Estimated-tax teaching should mention withholding/credits and current/prior-year safe harbors. Expected balance due of $1,000 alone is not the complete underpayment-penalty test.

**C06 — `S22-B1-Q4` (p. 451):** The backward branch’s multistep interest estimate is harder than a quick conceptual emergency-fund diagnostic. Consider moving it deeper and using a simpler one-idea remedial item.

**C07 — `S33-F1-Q1` (p. 684):** Two debts share the highest 22% rate. State that the avalanche method breaks equal-rate ties by the smaller balance if a unique first debt is expected.

**C08 — `S39-M-Q2` (p. 801); `S39-F2-Q4` (p. 818):** Match payoff schedules when comparing transfer fees and interest savings. A constant old balance versus an amortizing promotional balance is only an explicitly rough estimate, not a full like-for-like comparison.

**C09 — `S48-B1-Q5` (p. 998):** Scope instant diversification to the diversified broad funds being discussed; not every sector, single-stock, leveraged, or narrowly concentrated fund provides it.

**C10 — `S57-M-Q1` (p. 1178); `S57-F2-Q1` (p. 1193):** Distinguish personal traditional/Roth IRAs from employer-established SEP/SIMPLE IRA arrangements when saying IRAs are never through an employer.

**C11 — `S58-F2-Q3` (p. 1216):** Explain that timely return of excess IRA contributions and attributable earnings can use the return deadline INCLUDING extensions and applicable relief. Do not confuse this with the ordinary contribution deadline, which generally excludes extensions.

**C12 — `S64-B1-Q5` (p. 1334):** Say W-2s are generally furnished by January 31, or the next business day when applicable, and propagate that qualifier to S11/source claims.

**C13 — `S72-B1-Q5` (p. 1502):** Distinguish a rent-only rule of thumb from the formal housing-cost-burden measure, which generally includes utilities in housing costs.

**C14 — `S77-F1-Q4` (p. 1611):** Specify no escrow shortage recovery, surplus, insurance change, or other adjustment when deriving exactly $50 more monthly from a $600 yearly tax increase.

**C15 — `S78-F1-Q3` (p. 1631):** A rate lock is conditional on its terms and unchanged qualifying loan/borrower facts, not an unconditional guarantee of any loan at the old quote.

**C16 — `S80-M-Q5` (p. 1665); `S80-F1-Q2` (p. 1672); `S80-F1-Q3` (p. 1673):** Call closing-cost/payment-savings calculations a simple CASH-FLOW break-even. A complete refinance comparison also considers loan term, principal balances, rolled-in costs, and the planned exit date.

**C17 — `S84-F2-Q5` (p. 1764):** For the check-engine question specify a steady light with no urgent symptoms; do not suggest continued driving for every flashing-light or severe-symptom situation. Replace guarantees that diagnosis keeps every repair small.

**C18 — `S87-F2-Q1` (p. 1818):** Ask for expected patient responsibility on the EOB, not an instruction to pay the EOB itself. Confirm the actual provider bill and any errors before payment.

**C19 — `S90-M-Q5` (p. 1860); `S90-F1-Q1` (p. 1866); `S90-F1-Q5` (p. 1870):** Specify at most one claim in the simple deductible expected-value example. Qualify the large-group predictability lesson: correlated catastrophes do not disappear merely because many properties are insured.

**C20 — `S96-B1-Q2` (p. 1963):** The word might makes the $900/1099-NEC identification answer possible, not inherently wrong. Nevertheless specify tax year and business payer, and avoid implying $900 requires a form in 2026: the general reporting threshold became $2,000. Income may be reportable without a form. See A19.

**C21 — `S98-F1-Q1` (p. 1999):** An already-filed SSN rejection can indicate identity theft or a filing/data error. Ask what it MAY indicate and direct the learner to investigate rather than treating fraud as proved.

**C22 — `S104-M-Q5` (p. 2089):** Specify a broadly diversified market fund and a sourced historical context; no unspecified stock index is guaranteed to recover.

**C23 — `S104-F1-Q1` (p. 2095):** If using the economic term public good technically, distinguish it from a tax-funded public service. Roads can be congestible or restricted; national defense is a cleaner nonrival/nonexcludable example.

**C24 — `S112-M-Q2` (p. 2214):** Make the opportunity-cost answer and feedback consistent: the full value of the forgone investment alternative versus just its incremental growth are different quantities.

**C25 — `S113-M-Q1` (p. 2229):** Give enough context for a priority decision: essential bills and debt minimums are covered, a starter cushion exists, and enough cash flow is available to capture the match. Do not teach a universal ranking independent of those conditions.

**C26 — `S53-M-Q2` (p. 1095), `S53-M-Q4` (p. 1097):** Scope the capital-gains and taxable-account intros to ordinary taxable stock/fund investments and use generally. Not every long-term gain uses only the standard 0%/15%/20% schedule; special asset rules exist, and some interest is exempt. The qualified “usually” in S53-M-Q2’s keyed choice is better than its absolute intro/feedback. See IRS Topic 409: https://www.irs.gov/taxtopics/tc409.

## 4. Required package, standards, and branch work

### P1 — Replace blanket source verification with claim-level evidence

The package contains 100 distinct source URLs, and its original source records are still marked unverified. This review attempted all 100 links: 85 returned HTTP 200; 11 returned 404; four returned 403. A successful fetch does not establish that the page supports its attached claim, and a 403 is an access limitation, not proof the claim is wrong. Some “200” pages also require JavaScript or offer only broad navigation.

Create a source ledger with question/set IDs, the precise claim, direct primary URL, document version, section/page or heading, applicable jurisdiction, tax/effective year, and actual verification date. Record inaccessible and unresolved claims honestly. Broad pages are inadequate for unrelated attached statements: S1’s deposit-insurance citations do not prove membership eligibility or every claim about bank operations; an I-bond page does not establish all T-bill purchase rules; a generic 401(k) page does not by itself document every 403(b) rule. Fix both the question text and the repeated `sources` strings when necessary.

Do not erase all “to verify” flags just because this report accessed the IRS or standards PDFs. Promote a source claim only after confirming that exact claim. Distinguish `verified_on`, `effective_from`, `tax_year`, and `hypothetical` instead of using one authoring date for all meanings.

### P2 — Finish and correct the standards crosswalk

The official 2021 CEE/Jump$tart standards PDF and the official 2020 NJSLS 9.1 PDF were accessible during review. Uploading those authoritative PDFs to the authoring repository is a reasonable solution to Claude’s earlier access problem. References are A20 and A21 below.

Only eight sets currently carry nonempty national outcome codes; the rest have topic-level descriptions. That is not a complete benchmark-by-benchmark crosswalk. Qualify every national code by TOPIC as well as grade, since codes such as 12-8b repeat across topics.

Specific corrections:

- S53 labels its topic Investing and cites 12-8b, but its learning-target description starts with the Earning Income 12-8b concept. Investing 12-8b concerns tax-deferred versus taxable investing, which can support this set; use the correct description and add the appropriate investing capital-gains outcome where supported.
- S63 uses Earning Income 12-8b for types/purposes of taxes. Align its main government-tax content to Earning Income 12-6b/12-6c, with 12-6a for supported calculations. Do not call a code verified merely because it exists.
- For each backward/deeper section distinguish direct alignment, supporting prerequisite, and related enrichment. A local code such as `FL.RETIRE.58` is a course identifier, not an official national standard.

New Jersey’s grade-12 document has 55 performance expectations. Current strand tags do not demonstrate complete coverage. Clear missing or incomplete areas include estate-planning documents (CFR.5), corporate governance/human rights (CFR.3), cross-cultural financial patterns (CFR.4/FP.6), money scripts (FP.4), government-policy influence (EG.3), and government-versus-private insurance (RM.4). Reading an amortization table also does not demonstrate creating one with business tools (CDM.8). Either add focused coverage within the approved course scope or explicitly disclose gaps; do not advertise full standards mastery from strand labels alone.

Retain simple learner-facing local labels. If exact official alignment is displayed, ensure it is accurate per question and identifiable in exports; avoid presenting a broad strand as an exact assessed performance expectation.

### P3 — Resolve math branches against the actual installed game

There are **179 math references to 42 distinct external target skills**. These are pointers, with no local remedial questions. They cannot be fully validated from the Financial Literacy ZIP alone. The author’s catalog is not a substitute for the installed curriculum and renderer.

The previously supplied Grade 4/5/7/8 and Algebra I answer files allow comparison of 83 references. Seventy-four match a target MAIN section and expected standard in those supplied versions. Nine reference occurrences point to target sets absent from those older uploaded versions:

| Financial Literacy source | Referenced target |
|---|---|
| S13 B3; S32 B2; S39 B2; S82 B3; S107 B2 | Grade 7 set 65 MAIN |
| S19 B3; S82 B2 | Grade 7 set 63 MAIN |
| S19 B4 | Grade 7 set 66 MAIN |
| S67 B2 | Algebra I set 75 MAIN |

This is a version discrepancy requiring verification, **not proof those targets are absent from the live repository**. Grade 6 accounts for the other 96 references, and that course’s source bank was not supplied here.

All 74 resolvable reference occurrences point to MAIN sections containing short-answer questions; many also contain true/false. They are not uniformly multiple-choice. Before release, demonstrate how these references preserve Financial Literacy’s choice-only/no-recording behavior, or provide an explicit supported remediation rendering path. Do not silently substitute unrelated easy MC questions or route an adult into an incompatible recording flow.

Validate every reference with the actual game schema, course ID, set ID, section identifier, target standard, supported response type, question availability, and a content version/hash. Confirm that returning from remediation resumes the right Financial Literacy set and preserves its progress/rewards. The package uses `M` as the reference section, while supplied answer keys call it `MAIN`; confirm the importer’s supported mapping rather than blindly changing either format.

### P4 — Check the educational fit of backward branches and shuffle behavior

The package says a MAIN score of three or fewer out of five triggers every backward section, and each branch requires five consecutive correct. Verify this is the intended existing behavior. Four correct repeats MAIN; five unlocks Go Deeper. Do not change these thresholds without an approved architecture decision.

The local five-question concept branches are present. Some external math targets are multi-step full-grade MAIN sets, so calling them five quick one-idea diagnostic questions is not established. Check that each targets a real obstacle to the MAIN skill rather than only a hard forward example: for instance S14’s systems-of-equations reference and S67’s Algebra I step-function reference warrant this check. Keep adult-facing wording respectful and explain the skill without requiring a grade-based detour to feel like failure.

Shuffling is a confirmed package design, so every item must work independently. Repair the listed missing givens and review sibling pronouns throughout the bank. Do not claim global self-containment in `QUALITY_AUDIT.md` until that check actually passes.

### P5 — Make the teaching and practical walkthrough claims accurate

There are 1,440 questions with intros and 690 explicitly classified as knowledge checks without them. The latter include 125 MAIN and 267 concept-backward questions. That is not automatically a defect: self-contained practice can be appropriate. However, if the agreed product promises teaching before each new skill, verify that no learner needs a shuffled sibling’s intro or a prior outside course to learn an unintroduced concept.

Audit the 258 `how_to` flags for actual actionable steps, not merely an isolated recognition question. Opening an account and opening/funding a Roth IRA contain useful ordered steps; tax filing, renting, and vehicle buying should similarly expose the steps needed before the relevant checks. Keep the existing short-teach/easy-MC model rather than turning this into lengthy reading or outside assignments.

### P6 — Regenerate the complete package and correct the audit claims

Rebuild from one canonical source. Regenerate full and split question PDFs, full and split answer PDFs, standalone JSON, CSV, per-set/index JSON, all seven reports, manifest, and a new versioned import ZIP. Verify that an answer in the JSON corresponds to the same question ID, choices, and page in every other export.

Revise `QUALITY_AUDIT.md`: exact-string uniqueness is not semantic uniqueness; `calc` agreement is not a proof of a complete solution; a catalog check is not proof of runtime compatibility; and the current bank has missing sibling givens. Report which checks actually ran and what remains unresolved.

If changes affect scoring or meanings, document migration behavior for any existing progress. Prefer reviewing the revised package before any production import. Keep a change log by original question ID, with old/new key, content reason, source, and whether the change alters the answer or only improves wording.

## 5. Source references for the corrections

These are primary-source references consulted for the specific topics stated. Use the exact relevant section, not the homepage, in the revised ledger. A source being listed here does not approve all claims attached to it in the original package.

- **A1:** [IRS — Working Families Tax Cuts: 2026 nonitemizer charitable deduction and HSA-compatible bronze/catastrophic coverage](https://www.irs.gov/newsroom/working-families-tax-cuts).
- **A2:** [Department of Education — 2022 final regulations, including interest-capitalization changes effective July 2023](https://fsapartners.ed.gov/fsa-print/publication/1004279).
- **A3:** [CFPB Regulation Z, 1026.52(b)(2)(i): late-fee cap tied to minimum payment](https://www.consumerfinance.gov/rules-policy/regulations/1026/52/).
- **A4:** [CFPB — Regulation CC thresholds effective July 1, 2025](https://www.consumerfinance.gov/rules-policy/final-rules/availability-funds-and-collection-checks-regulation-cc-threshold-adjustments/).
- **A5:** [IRS Notice 2011-17: Emancipation Day and the April filing deadline](https://www.irs.gov/pub/irs-drop/n-11-17.pdf).
- **A6:** [FTC — Cooling-Off Rule thresholds, exceptions, and business-day counting](https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help).
- **A7:** [CFPB Regulation F, 1006.34: validation period and notice](https://www.consumerfinance.gov/rules-policy/regulations/1006/34/).
- **A8:** [CFPB Regulation E, 1005.6: unauthorized-transfer liability and timing](https://www.consumerfinance.gov/rules-policy/regulations/1005/6/).
- **A9:** [CFPB Regulation Z, 1026.13: billing-error notice receipt](https://www.consumerfinance.gov/rules-policy/regulations/1026/13/).
- **A10:** [CFPB Regulation Z, 1026.51: ability to pay and consumers under 21](https://www.consumerfinance.gov/rules-policy/regulations/1026/51/).
- **A11:** [CFPB — Credit-card grace periods](https://www.consumerfinance.gov/ask-cfpb/what-is-a-grace-period-for-a-credit-card-en-47/).
- **A12:** [U.S. Department of Labor — Overtime pay](https://www.dol.gov/agencies/whd/overtime).
- **A13:** [TreasuryDirect — Buying savings bonds](https://www.treasurydirect.gov/savings-bonds/buy-a-bond/).
- **A14:** [CFPB — Interest rate versus APR](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/).
- **A15:** [IRS Publication 590-B — Traditional IRA distributions and Roth ordering rules](https://www.irs.gov/publications/p590b).
- **A16:** [IRS Publication 590-A — Compensation, spousal IRAs, contribution limits, and excess contributions](https://www.irs.gov/publications/p590a).
- **A17:** [CFPB Regulation Z, 1026.2(a)(6): business-day definitions](https://www.consumerfinance.gov/rules-policy/regulations/1026/2/).
- **A18:** [IRS — Qualified-tip deduction, distinct from tip reporting](https://www.irs.gov/newsroom/what-the-no-tax-on-tips-deduction-means-for-you).
- **A19:** [IRS — Information returns and the 2026 1099-NEC threshold](https://www.irs.gov/businesses/small-businesses-self-employed/am-i-required-to-file-a-form-1099-or-other-information-return).
- **A20:** [CEE/Jump$tart — 2021 National Standards for Personal Financial Education](https://www.councilforeconed.org/wp-content/uploads/2021/10/2021-National-Standards-for-Personal-Financial-Education.pdf).
- **A21:** [NJDOE — 2020 NJSLS 9.1 official PDF](https://www.nj.gov/education/standards/clicks/Docs/2020NJSLS-9.1FinancialLiteracy.pdf).
- **A22:** [New Jersey DCA — Truth in Renting, deposits and tenancy rules](https://www.nj.gov/dca/codes/publications/pdf_lti/t_i_r.pdf).
- **A23:** [FTC — Rule on Unfair or Deceptive Fees, ticketing and lodging, effective May 12, 2025](https://www.ftc.gov/news-events/news/press-releases/2025/05/ftc-rule-unfair-or-deceptive-fees-take-effect-may-12-2025).

The deposit-insurance, SIPC, FICO factor-weight, Treasury holding-period, and core wage-tax concepts were also checked against the applicable agency/issuer materials and the supplied scenarios. No finding here changes a correctly labeled hypothetical IRA limit, tax bracket, or tax rate merely because it differs from the current real-world amount. A hypothetical rule should be clearly identified locally and should not be confused with an actual consumer right or obligation.

### Original source URLs that did not fetch successfully

Recheck these in the authoring environment and replace genuine dead links with direct official pages. Access failures must remain distinguished from content errors.

| Original URL | Review fetch result |
|---|---|
| https://business.nj.gov/ | HTTP Error 403: Forbidden |
| https://consumer.ftc.gov/articles/automatic-renewals-and-subscriptions | HTTP Error 404: Not Found |
| https://consumer.ftc.gov/articles/donating-wisely-avoiding-charity-scams | HTTP Error 404: Not Found |
| https://www.cisa.gov/secure-our-world | HTTP Error 403: Forbidden |
| https://www.consumerfinance.gov/about-us/blog/cfpb-warns-consumers-about-deferred-interest-promotions/ | HTTP Error 404: Not Found |
| https://www.consumerfinance.gov/ask-cfpb/what-is-my-liability-for-unauthorized-credit-card-charges-en-24/ | HTTP Error 404: Not Found |
| https://www.fdic.gov/resources/deposit-insurance | HTTP Error 403: Forbidden |
| https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance | HTTP Error 403: Forbidden |
| https://www.ftc.gov/legal-library/browse/rules/rule-unfair-or-deceptive-fees | HTTP Error 404: Not Found |
| https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/opening-brokerage-account | HTTP Error 404: Not Found |
| https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs | HTTP Error 404: Not Found |
| https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/saving-investing | HTTP Error 404: Not Found |
| https://www.investor.gov/introduction-investing/investing-basics/understanding-fees | HTTP Error 404: Not Found |
| https://www.irs.gov/filing/check-if-you-need-to-file-a-tax-return | HTTP Error 404: Not Found |
| https://www.nj.gov/treasury/taxation/su_over.shtml | HTTP Error 404: Not found |

## 6. Review coverage and next handoff

All sets S1–S113 were read for question, teaching where present, choice/key, and feedback meaning. Structural checks covered all local records and both complete PDFs. The visual PDF check was sampled, not a visual inspection of all 4,486 pages. All CSV misconception fields were cross-checked for export agreement; this report does not claim a separate line-by-line semantic approval of all 6,390 misconception notes. Those notes must change wherever an underlying distractor or rule changes.

A set absent from the findings list is not exempt from global corrections, standards/source completion, or integration checks. Conversely, do not rewrite correct content solely because it shares a unit with a flagged question.

Return these items for the next review:

1. Revised complete package and matching standalone files.
2. A response table for every R finding and P requirement, with affected question IDs and the exact fix or evidence for a different resolution.
3. A decision for every C recommendation.
4. Claim-level source ledger with actual verification results and remaining limitations.
5. Results from running the actual application’s importer, math-branch routing, supported response rendering, remediation return, mastery, Go Deeper, and reward checks.

**Release status remains pending corrections and recheck.** Do not describe the original version as fact-checked and ready to load based solely on passing file-consistency tests.
