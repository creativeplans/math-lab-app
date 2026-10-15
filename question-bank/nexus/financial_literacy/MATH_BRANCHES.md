# Financial Literacy — Math Prerequisite Branches

A math branch is a backward section with `"kind": "math"` and a `ref` to a MAIN skill that is already in Untangle The Nexus. It has no questions of its own; the game sends the student to that skill. The package writes the section as `M`; the game's importer maps it to the skill ID `<course>-S<set>-M` (for example `G6-S40-M`), which is the MAIN section that the math answer keys call `MAIN`.

The branch fires only under the game's existing rule: **3 or fewer correct out of 5** on MAIN (`backwardWhenIncorrectAtLeast: 2`). The student then works every backward section of the set in order. This package does not change that rule.

## 1. Checked against the installed game (not just the catalog)

- **Every link resolved in the live game content.** 178 links to 38 distinct skills were checked with the game's own code (`COURSES`, `bankKey`, `isAutoCheckable`) against `untangle-the-nexus` commit 4b77e64: ok: 178. All links in this version were re-checked.
- **The reviewer's "absent target" list.** Grade 7 sets 63, 65, and 66 exist in the installed Grade 7 bank (bank version 2.0.0, standard 7.RP.A.3); the reviewer's copies were older uploads. The Algebra I set 75 link (S67) was removed in v1.1 because a step function is not a real obstacle to the marginal-rate skill.
- **What the student sees.** In backward mode the game serves only auto-checkable questions from the target skill (`requireAutoCheck`): multiple choice, true/false, and short typed numeric answers. It never asks for a written or recorded explanation there (`requiresExplanation` is false for backward work). Short typed answers are the target skill's own supported format; they are not multiple choice. **Owner decision needed:** accept typed numeric answers inside math remediation, or ask the game team for a choice-only filter. This package does not substitute unrelated multiple-choice questions.
- **Repeats.** 9 target skills have fewer than 5 auto-checkable MAIN questions (ALG1-S20-M 2 of 5, ALG1-S46-M 4 of 5, ALG1-S55-M 2 of 5, ALG1-S60-M 3 of 5, G4-S18-M 4 of 5, G7-S31-M 4 of 5, G7-S34-M 3 of 5, G8-S18-M 3 of 5, G8-S22-M 3 of 5). Because a branch needs 5 correct in a row, the game repeats some of those items. This is existing game behavior.
- **Runtime test (real importer and game server, PostgreSQL).** The full package imported with 113 sets, 2130 questions, 0 invalid, 0 warnings. On S24, 3 of 5 correct sent the student through FL-S24-B1 -> G6-S40-M -> G5-S01-M -> ALG1-S55-M -> G6-S10-M in that order (kinds mc, short, short, tf, short), matching the curriculum's backward edges, with no explanation required; afterwards the student returned to FL-S24-M. Then 5 of 5 recorded mastery (1) with the normal reward of 300 seconds, and Go Deeper FL-S24-F1 became available; Go Deeper questions showed their intro exactly when the bank has one. Details: `RUNTIME_CHECK.json`.
- **Grade 6** was imported into the game from PDFs and has no bank version number, so its links are identified by skill ID and a hash of its question file (in `MATH_REF_VALIDATION.json`).

## 2. Links by course

| Course | Links |
|---|---|
| algebra_1 | 7 |
| grade_4 | 1 |
| grade_5 | 8 |
| grade_6 | 99 |
| grade_7 | 60 |
| grade_8 | 3 |

## 3. Every link

| Set | Section | Game skill | Standard | Skill name | Why it is needed | Live game check |
|---|---|---|---|---|---|---|
| S2 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Every balance question subtracts amounts in dollars and cents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S2 | B3 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | Deposits are added to the balance in dollars and cents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S3 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Comparing accounts means multiplying monthly fees by months and comparing dollar totals. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S4 | B2 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | Deposits are added in dollars and cents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S4 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Purchases and payments are subtracted in dollars and cents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S4 | B4 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | An overdrawn account has a negative balance; students must read and compute with negative amounts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S5 | B2 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | Overdraft problems require adding and subtracting with negative balances. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S5 | B3 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Multi-step fee problems combine several operations with money amounts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S6 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Interest for a year is a percent of the balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S6 | B3 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Rates written as decimals are multiplied by balances. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S7 | B2 | G5-S12-M | 5.NBT.A.3.a | Read and write decimals to thousandths using numerals and words | Writing check amounts requires reading decimals and writing cents as hundredths. | ok; 5 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S8 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Gross pay multiplies a decimal wage by decimal hours. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S8 | B3 | G6-S03-M | 6.RP.A.2 | Find and describe a unit rate | An hourly wage is a unit rate (dollars per hour). | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S9 | B2 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Pay-per-period problems divide yearly pay by the number of paychecks. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S9 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | Converting between hourly, weekly, monthly, and yearly pay chains several rates. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S10 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | FICA and other deductions are percents of gross pay. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S10 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Net pay is gross pay minus deductions in dollars and cents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S11 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Yearly withholding totals multiply per-paycheck amounts by the number of pay periods. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S12 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Employer match and contribution rates are percents of salary. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S12 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | Comparing offers combines monthly and yearly amounts and percents. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S13 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Self-employment tax and set-aside amounts are percents of earnings. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S13 | B3 | G7-S65-M | 7.RP.A.3 | Find a percent fee and the total with the fee | Gig platforms deduct percent-based fees from earnings. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S14 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Comparing career paths multiplies yearly pay by years and subtracts totals. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S14 | B3 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Multi-year earnings multiply yearly pay by years. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S15 | B2 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | Budget totals add many expenses. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S15 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Money left subtracts total expenses from income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S16 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Budget results subtract planned spending from income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S16 | B3 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | A deficit is a negative result that must be understood and fixed. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S17 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Each budget share is a percent of take-home pay. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S17 | B3 | G6-S11-M | 6.RP.A.3.c | Find the whole, given a part and the percent | Finding income needed for a target share works backward from a percent. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S18 | B2 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Set-asides divide totals by months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S18 | B3 | G6-S03-M | 6.RP.A.2 | Find and describe a unit rate | A monthly set-aside is a rate (dollars per month). | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S19 | B2 | G6-S09-M | 6.RP.A.3.b | Compare unit rates to find the better buy or the faster rate | Unit price comparisons are unit-rate comparisons. | ok; 5 of 5 auto-checkable (mc 5) |
| S19 | B3 | G7-S63-M | 7.RP.A.3 | Find sales tax and the final cost with tax | Total cost includes tax as a percent of the price. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S19 | B4 | G7-S66-M | 7.RP.A.3 | Solve multistep percent problems that combine a discount with tax or a tip | Sale-and-tax totals apply two percents in order. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S21 | B2 | G6-S52-M | 6.EE.B.7 | Solve one-step equations of the form px = q | Monthly saving × months = goal is a one-step equation. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S21 | B3 | G7-S31-M | 7.EE.B.4.a | Solve word problems that lead to equations of the form px + q = r | Goals with a starting balance lead to px + q = r. | ok; 4 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S22 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Fund targets multiply monthly expenses by months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S22 | B3 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Months covered divides the fund by monthly expenses. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S23 | B2 | G7-S10-M | 7.RP.A.3 | Find simple interest | This set applies the Grade 7 simple interest skill. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S23 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Interest for one year is a percent of the principal. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S23 | B4 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | I = Prt multiplies three factors, including a decimal rate. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S23 | B5 | G6-S44-M | 6.EE.A.2.c | Evaluate expressions and formulas for given values | Simple interest substitutes values into a formula. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S24 | B2 | G6-S40-M | 6.EE.A.1 | Evaluate numerical expressions with whole-number exponents | A = P(1 + r)^t requires evaluating a power. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S24 | B3 | G5-S01-M | 5.OA.A.1 | Evaluate expressions that use parentheses | The order of operations matters: compute 1 + r first, then the power, then multiply. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S24 | B4 | ALG1-S55-M | HSF-LE.A.1.c | Recognize situations in which a quantity grows or decays by a constant percent rate per unit interval | Compound interest is growth by a constant percent per year. | ok; 2 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S24 | B5 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Each year's interest is a percent of the balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S25 | B2 | G6-S40-M | 6.EE.A.1 | Evaluate numerical expressions with whole-number exponents | Compound interest formulas raise a growth factor to a power. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S25 | B3 | ALG1-S46-M | HSF-IF.C.8.b | Use the properties of exponents to interpret growth and decay rates | APY compares yearly growth factors from different compounding periods. | ok; 4 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S25 | B4 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Periodic rates divide the annual rate by the number of periods. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S26 | B2 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | The Rule of 72 divides 72 by the rate (or by the years). | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S26 | B3 | G6-S40-M | 6.EE.A.1 | Evaluate numerical expressions with whole-number exponents | Repeated doubling is a power of 2. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S27 | B2 | G7-S10-M | 7.RP.A.3 | Find simple interest | CD interest and penalties use simple interest over part of a year. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S28 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Interest is the difference between the total repaid and the principal. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S29 | B2 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Periodic rates divide the APR by 12 or 365. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S29 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Interest for a period is a percent of the balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S29 | B4 | G7-S01-M | 7.RP.A.1 | Compute unit rates associated with ratios of fractions | A periodic rate is a rate per unit of time. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S30 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Total cost multiplies a decimal payment by many months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S30 | B3 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Comparing loans subtracts and multiplies money amounts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S31 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Each month's interest is a percent of the remaining balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S31 | B3 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Amortization repeats multiply, subtract, and update steps. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S32 | B2 | G7-S65-M | 7.RP.A.3 | Find a percent fee and the total with the fee | High-cost credit charges fees that are percents of the amount borrowed. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S32 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | Converting a two-week fee into a yearly rate scales a ratio. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S33 | B2 | G6-S01-M | 6.RP.A.1 | Write a ratio that describes the relationship between two quantities | DTI is a ratio of debt payments to income. | ok; 5 of 5 auto-checkable (short 5) |
| S33 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | DTI limits are percents of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S34 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Comparing fees and payments uses percents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S35 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Available credit subtracts the balance from the limit. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S36 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Carried balances subtract payments from the statement balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S37 | B2 | G6-S77-M | 6.SP.B.5.c | Find the mean of a data set | Average daily balance is a (weighted) mean of daily balances. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S37 | B3 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | The daily periodic rate divides the APR by 365. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S37 | B4 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Interest multiplies the ADB, the daily rate, and the days. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S38 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Minimum payments combine percent, interest, and subtraction steps. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S38 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Minimums and interest are percents of the balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S39 | B2 | G7-S65-M | 7.RP.A.3 | Find a percent fee and the total with the fee | Transfer, cash advance, and foreign transaction fees are percent fees. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S39 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | Comparing a transfer requires interest over months and a fee. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S41 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Score factors and rates are percents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S41 | B3 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Comparing loan offers multiplies payment differences by months. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S42 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Utilization targets are percents of a limit. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S42 | B3 | G6-S11-M | 6.RP.A.3.c | Find the whole, given a part and the percent | Finding the limit or balance for a target utilization works backward from a percent. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S43 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Investment returns are percent changes. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S46 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Stock returns are percent changes in price. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S46 | B3 | G7-S20-M | 7.NS.A.2.a | Interpret products of rational numbers in real-world situations | Gains and losses multiply a per-share change (possibly negative) by the number of shares. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S47 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Coupon interest is a percent of face value. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S48 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | A holding's effect on a fund is its percent weight times its change. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S48 | B3 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | NAV per share divides net assets by shares outstanding. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S49 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Allocations are percents of a portfolio. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S49 | B3 | G6-S77-M | 6.SP.B.5.c | Find the mean of a data set | A portfolio return is a weighted mean of its parts' returns. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S50 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Order costs multiply share prices by numbers of shares. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S50 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | The spread is the difference between ask and bid. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S51 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Fees are percents of the amount invested. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S51 | B3 | ALG1-S55-M | HSF-LE.A.1.c | Recognize situations in which a quantity grows or decays by a constant percent rate per unit interval | Fees lower the yearly growth factor, which compounds over time. | ok; 2 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S52 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Returns are percent changes from a starting value. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S52 | B3 | ALG1-S60-M | HSS-ID.A.2 | Compare the center and spread of two or more data sets | Volatility compares how spread out two sets of returns are. | ok; 3 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S53 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Taxes on gains are a percent of the gain. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S54 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Judging claimed returns requires comparing percent gains. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S55 | B2 | ALG1-S55-M | HSF-LE.A.1.c | Recognize situations in which a quantity grows or decays by a constant percent rate per unit interval | Long-term retirement growth is exponential growth at a percent rate. | ok; 2 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S55 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Replacement goals and Social Security estimates are percents of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S56 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Contributions and matches are percents of pay. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S56 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | Match calculations apply two percents in sequence. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S57 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Comparing accounts applies tax rates to contributions or withdrawals. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S57 | B3 | G7-S07-M | 7.RP.A.3 | Solve multistep ratio problems | The comparison chains tax and growth factors. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S58 | B2 | G7-S34-M | 7.EE.B.4.b | Solve word problems that lead to inequalities of the form px + q > r or px + q < r | Contribution rules are inequalities: contribution ≤ the limit and ≤ earned income. | ok; 3 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S58 | B3 | G4-S18-M | 4.NBT.A.2 | Compare multi-digit whole numbers using >, =, and < | "The lesser of" two amounts requires comparing numbers. | ok; 4 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S59 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Comparing providers adds account fees and fund costs. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S60 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Earnings are the balance minus contributions. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S60 | B3 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Gains and losses in an IRA are percent changes. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S61 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Separating contributions from earnings subtracts amounts. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S61 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Taxes and the additional tax are percents of a withdrawal. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S62 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Benefit reductions and increases are percents of a benefit. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S63 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Taxes are percents of a price, income, or value. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S64 | B2 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | Totaling income from several forms adds amounts. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S65 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Refunds and balances due compare amounts withheld and owed. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S66 | B2 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | AGI and taxable income come from subtracting adjustments and deductions. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S66 | B3 | G8-S18-M | 8.EE.C.7.b | Write and solve linear equations with rational coefficients for real-world problems | Taxable income = income − adjustments − deduction is a linear relationship. | ok; 3 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S67 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Each bracket's tax is a percent of the income in it. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S67 | B3 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Bracket calculations combine several subtraction and percent steps. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S68 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | A deduction's value is the deduction times the tax rate. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S68 | B3 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | Refundable credits can push tax below zero, producing a refund. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S69 | B2 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | A refund is a positive result and a balance due a negative one. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S69 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Refunds and balances compare two amounts. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S71 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Comparing rentals adds rent, utilities, and fees. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S72 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Affordability guidelines are percents of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S72 | B3 | G6-S52-M | 6.EE.B.7 | Solve one-step equations of the form px = q | Finding maximum rent from "40 × rent ≤ income" solves a one-step equation. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S73 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Deposit caps and fees multiply rent by factors like 1.5. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S74 | B2 | G5-S22-M | 5.NBT.B.7 | Solve real-world problems with decimal operations | Claim payments subtract deductibles; premiums multiply by months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S75 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Down payments are percents of the price. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S75 | B3 | G6-S17-M | 6.NS.B.3 | Subtract multi-digit decimals | Loan amounts and equity are differences. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S76 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Totals multiply a decimal payment by the number of payments. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S76 | B3 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Comparing loans subtracts and multiplies money amounts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S77 | B2 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Yearly taxes and insurance are divided into monthly amounts. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S77 | B3 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | PITI adds several monthly costs. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S78 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Closing costs are often estimated as percents of the loan. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S79 | B2 | G6-S01-M | 6.RP.A.1 | Write a ratio that describes the relationship between two quantities | DTI is a ratio of payments to income. | ok; 5 of 5 auto-checkable (short 5) |
| S79 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Limits are percents of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S79 | B4 | G7-S34-M | 7.EE.B.4.b | Solve word problems that lead to inequalities of the form px + q > r or px + q < r | Affordability rules are inequalities (payments ≤ a percent of income). | ok; 3 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S80 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Monthly interest is a percent of the balance. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S80 | B3 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Amortization steps repeat multiply-subtract-update. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S81 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Maintenance budgets and rate changes are percents. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S81 | B3 | G6-S16-M | 6.NS.B.3 | Add multi-digit decimals | Total cost of owning adds many monthly costs. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S82 | B2 | G7-S63-M | 7.RP.A.3 | Find sales tax and the final cost with tax | Sales tax on a car is a percent of the price. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S82 | B3 | G7-S65-M | 7.RP.A.3 | Find a percent fee and the total with the fee | Fees and taxes are added to the price to get the out-the-door total. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S83 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Total paid is a decimal payment times the number of months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S83 | B3 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Finding interest and comparing loans takes several steps. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S84 | B2 | G7-S01-M | 7.RP.A.1 | Compute unit rates associated with ratios of fractions | Fuel economy and cost per mile are unit rates. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S84 | B3 | ALG1-S55-M | HSF-LE.A.1.c | Recognize situations in which a quantity grows or decays by a constant percent rate per unit interval | Depreciation is often modeled as a constant percent decrease each year. | ok; 2 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S85 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Lease costs combine payments, fees, and charges. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S85 | B3 | G6-S20-M | 6.NS.B.3 | Divide multi-digit decimals | Lease payments spread a dollar amount over months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S86 | B2 | G7-S54-M | 7.SP.C.5 | Understand probability as a number from 0 to 1 that shows how likely an event is | Risk is described with probabilities. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S87 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Coinsurance is a percent of the bill. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S87 | B3 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Out-of-pocket costs combine a deductible, a percent, and a cap. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S88 | B2 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Coverage questions subtract deductibles and compare amounts with limits. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S89 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Benefits are often a percent of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S90 | B2 | G7-S55-M | 7.SP.C.6 | Estimate a probability from relative frequency and make predictions | Insurers estimate probabilities from claim data. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S90 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Expected loss multiplies an amount by a percent probability. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S91 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | COA and net price add costs and subtract aid. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S93 | B2 | G7-S10-M | 7.RP.A.3 | Find simple interest | In-school interest on unsubsidized loans is simple interest. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S94 | B2 | G6-S19-M | 6.NS.B.3 | Multiply multi-digit decimals | Total paid is a payment times the number of months. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S94 | B3 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Payment-to-income compares a payment with income as a percent. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S95 | B2 | G8-S22-M | 8.EE.C.8.c | Write and solve systems of linear equations for real-world problems | Break-even is where the revenue line meets the cost line. | ok; 3 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S95 | B3 | ALG1-S20-M | HSA-CED.A.1 | Create linear equations and inequalities in one variable and use them to solve problems | Profit goals lead to equations such as 12x − 600 = 360. | ok; 2 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S96 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Self-employment tax is a percent of a percent of profit. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S97 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Markup is a percent increase on cost. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S98 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Losses and liability limits compare amounts step by step. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S99 | B2 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Scam losses add up the money sent and the goods lost. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S100 | B2 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Liability questions compare a loss with a legal limit. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S101 | B2 | G6-S40-M | 6.EE.A.1 | Evaluate numerical expressions with whole-number exponents | Counting possible passwords uses powers. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S102 | B2 | G7-S08-M | 7.RP.A.3 | Find a percent increase or a percent decrease | Inflation is a percent increase in prices. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S103 | B2 | G7-S25-M | 7.NS.A.3 | Solve real-world problems with the four operations on rational numbers | Real rates subtract one percent from another, including negatives. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S104 | B2 | G6-S11-M | 6.RP.A.3.c | Find the whole, given a part and the percent | Unemployment and other rates are percents of a whole. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S105 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | Total contract cost adds monthly, one-time, and yearly charges. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S106 | B2 | G8-S22-M | 8.EE.C.8.c | Write and solve systems of linear equations for real-world problems | Comparing two plans finds where two costs are equal. | ok; 3 of 5 auto-checkable (mc 1, short 3, tf 1) |
| S107 | B2 | G7-S65-M | 7.RP.A.3 | Find a percent fee and the total with the fee | Fees are often a percent of the price added to the total. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S108 | B2 | G7-S15-M | 7.NS.A.1.b | Interpret sums of rational numbers in real-world situations | Net worth combines positive assets and negative debts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S109 | B2 | G6-S10-M | 6.RP.A.3.c | Find a percent of a quantity as a rate per 100 | Giving plans are often a percent of income. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S110 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | A first-job plan combines percents, totals, and time to goals. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S111 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | A moving-out budget adds and subtracts many amounts. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
| S112 | B2 | G6-S44-M | 6.EE.A.2.c | Evaluate expressions and formulas for given values | Decision matrices and growth formulas are evaluated with numbers. | ok; 5 of 5 auto-checkable (mc 1, short 4) |
| S113 | B2 | G7-S29-M | 7.EE.B.3 | Solve multistep problems with positive and negative rational numbers in any form | The checkup combines percents and differences across topics. | ok; 5 of 5 auto-checkable (mc 1, short 2, tf 2) |
