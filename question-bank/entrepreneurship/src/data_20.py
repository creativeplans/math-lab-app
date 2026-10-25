"""Entrepreneurship sets 125-135: Specialty module, funding and growth; Wrigley case.
Interest rates, amounts and percentages are practice assumptions, not offers or market data."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 125: bootstrapping and savings
BOOT = ('BOOTSTRAPPING means starting and growing with your own money and the business\'s own sales, without loans or '
        'investors. It keeps you in control and avoids debt, but growth may be slower. If you use personal SAVINGS, decide in '
        'advance how much you can afford to lose without harming your household, such as rent, food and an emergency fund. '
        'Start with the smallest version that can test demand, and reinvest early profits rather than spending them.')

s125 = SET('ENT.FUND.01',
    M=sec('Decide how much of your own money to risk and grow from sales', BOOT, [
        Q('What does bootstrapping mean?', 'Growing with your own money and sales, without loans or investors',
          ('Borrowing as much as possible from several banks at once', 'opposite'),
          ('Selling part of the business to investors on day one', 'opposite'),
          ('Buying expensive boots for every employee in the shop', 'pun'), 'Self-funded growth.'),
        Q('What is a benefit of bootstrapping?', 'You keep control and avoid debt',
          ('Growth is always faster than with any outside money', 'often slower'),
          ('You never need to make a single sale to survive', 'sales are needed'),
          ('Your personal savings can never be at risk at all', 'they can'), 'Control, no debt.'),
        Q('What should an owner decide before using savings?', 'How much she can afford to lose without harming her household',
          ('How much her neighbors spent on their own businesses', 'irrelevant'),
          ('How quickly she can spend every dollar she has saved', 'risky'),
          ('Which bank has the nicest-looking logo and branches', 'irrelevant'), 'Set a limit.'),
        Q('An owner has 12,000 dollars in savings and keeps 7,000 for a household emergency fund. How much could she put in?',
          '5,000 dollars', ('12,000 dollars', 'all savings'), ('7,000 dollars', 'emergency fund'), ('19,000 dollars', 'added'),
          '12,000 - 7,000 = 5,000.', calc=lambda: 12000 - 7000 == 5000),
        Q('What should happen with early profits when bootstrapping?', 'Reinvest them in the business',
          ('Spend them all on personal luxuries right away', 'slows growth'),
          ('Hide them so no records show them', 'improper'), ('Give them to competitors', 'no'), 'Fuel growth.'),
    ]),
    B=[mathb('Keeping a safety amount', 'Before risking savings, subtract what must stay safe. Safe amount = monthly household '
             'costs x number of months you want covered. Example: costs of 2,000 a month for 4 months = 8,000. If savings are '
             '11,000, the amount you could risk is 11,000 - 8,000 = 3,000. If savings are less than the safe amount, there is '
             'nothing to risk yet.', [
        Q('Monthly costs 1,500 for 3 months. What is the safe amount?', '4,500', ('1,500', 'one month'), ('4,500 per month', 'wrong unit'),
          ('500', 'divided'), '1,500 x 3 = 4,500.', calc=lambda: 1500 * 3 == 4500),
        Q('Savings 10,000, safe amount 6,000. How much could be risked?', '4,000', ('16,000', 'added'), ('6,000', 'safe amount'),
          ('10,000', 'all'), '10,000 - 6,000 = 4,000.', calc=lambda: 10000 - 6000 == 4000),
        Q('Savings 5,000, safe amount 6,000. How much could be risked?', 'Nothing yet', ('1,000 (the difference)', 'negative'), ('5,000', 'all'),
          ('11,000', 'added'), 'Savings are below the safe amount.', calc=lambda: 5000 - 6000 < 0),
        Q('Monthly costs 2,200 for 6 months. What is the safe amount?', '13,200', ('2,200', 'one month'), ('8,200', 'added'),
          ('366.67', 'divided'), '2,200 x 6 = 13,200.', calc=lambda: 2200 * 6 == 13200),
        Q('Which step comes first?', 'Find the safe amount, then subtract it from savings', ('Spend first, then count', 'risky'),
          ('Add costs to savings', 'wrong'), ('Divide savings by monthly costs, and stop there', 'incomplete'), 'Protect first.'),
    ], why='A learner who misses MAIN may not compute how much is safe to risk; this practices the safety calculation.')],
    F1=sec('Apply it: plan a bootstrapped start', BOOT, [
        Q('A tutor needs 300 dollars for materials and a simple website. She has 900 dollars she can afford to lose. What fits best?',
          'Start small with 300 dollars and test demand', ('Borrow 20,000 dollars to start big', 'too large'),
          ('Spend all 900 dollars on ads on day one', 'untested'), ('Wait years until she can afford an office', 'unnecessary'),
          'Smallest test.'),
        Q('Month 1 profit is 400 dollars. She reinvests 75 percent. How much is reinvested?', '300 dollars', ('400 dollars', 'all'),
          ('100 dollars', 'kept'), ('75 dollars', 'percent as dollars'), '0.75 x 400 = 300.', calc=lambda: 0.75 * 400 == 300),
        Q('Bootstrapping limits her to 5 clients now. A loan would allow 15. What is the main tradeoff?', 'Slower growth versus avoiding debt',
          ('No tradeoff exists between the two choices', 'there is'), ('Loans never need repaying', 'they do'), ('Bootstrapping is illegal', 'no'),
          'Speed versus risk.'),
        Q('Her household needs 1,800 a month and she wants 3 months covered. Savings are 7,000. How much could she risk?', '1,600 dollars',
          ('7,000 dollars', 'all'), ('5,400 dollars', 'safe amount'), ('3,600 dollars', 'two months'), '7,000 - 5,400 = 1,600.',
          calc=lambda: 7000 - 1800 * 3 == 1600),
        Q('Which purchase best fits a bootstrapped start?', 'Used equipment that covers the basic need', ('The newest top-model equipment on credit', 'debt'),
          ('A large office before any clients', 'premature'), ('Custom uniforms for future staff', 'premature'), 'Lean spending.'),
    ]),
    F2=sec('Handle the complications: draining savings', BOOT, [
        Q('After 6 months, the owner has used her whole emergency fund on the business. What is the risk?', 'A household emergency could force bad decisions',
          ('No risk, because the business will surely succeed', 'not certain'), ('Her taxes will go to zero', 'no'),
          ('Her business automatically becomes an LLC', 'no'), 'Household safety matters.'),
        Q('The business needs 2,000 dollars more but she set a loss limit she has reached. What is a sensible step?', 'Pause and reassess before spending more',
          ('Spend the rent money too', 'harms household'), ('Max out personal credit cards without a plan', 'risky'),
          ('Ignore the limit she set', 'defeats the purpose'), 'Respect the limit.'),
        Q('Sales grow 10 percent a month from 1,000 dollars. About what are sales in month 3 (two increases)?', '1,210 dollars',
          ('1,200 dollars', 'added 10 percent of original twice'), ('1,100 dollars', 'one increase'), ('1,300 dollars', 'three'),
          '1,000 x 1.1 x 1.1 = 1,210.', calc=lambda: round(1000 * 1.1 * 1.1, 2) == 1210),
        Q('A friend says bootstrapping is "too slow to work." What is a balanced reply?', 'It can be slower but keeps control and avoids debt',
          ('It is always faster than borrowing or investors', 'not always'), ('It never works for anyone', 'not true'),
          ('It requires investors at the start', 'opposite'), 'Tradeoffs.'),
        Q('Which statement is accurate?', 'Set a loss limit and grow from sales where possible.',
          ('All savings should be risked at once to grow faster.', 'risky'), ('Bootstrapping means no sales are needed.', 'not true'),
          ('Debt is required to start any business.', 'not true'), 'Plan the risk.'),
    ]))

# ------------------------------------------------------------------ Set 126: loans
LOAN = ('A LOAN gives money now that must be repaid with INTEREST (the cost of borrowing) over a set TERM. Compare loans by '
        'the total cost, not just the monthly payment: total repaid = monthly payment x number of payments. A longer term '
        'usually lowers the monthly payment but raises total interest. Lenders may require a PERSONAL GUARANTEE or '
        'COLLATERAL (property the lender can take if you do not repay). Borrow only for a plan that can realistically '
        'repay from cash flow.')

s126 = SET('ENT.FUND.02',
    M=sec('Compare loans by total cost, term and guarantees', LOAN, [
        Q('What is interest?', 'The cost of borrowing money', ('A discount the lender gives for borrowing', 'opposite'),
          ('The owner\'s personal hobby or passion', 'pun'), ('A tax the state charges on all sales', 'different'), 'Borrowing cost.'),
        Q('A loan has 24 payments of 250 dollars. What is the total repaid?', '6,000 dollars', ('250 dollars', 'one payment'),
          ('274 dollars', 'added'), ('5,000 dollars', '20 payments'), '24 x 250 = 6,000.', calc=lambda: 24 * 250 == 6000),
        Q('If 5,000 dollars was borrowed, how much interest was paid?', '1,000 dollars', ('6,000 dollars', 'total repaid'),
          ('250 dollars', 'one payment'), ('11,000 dollars', 'added'), '6,000 - 5,000 = 1,000.', calc=lambda: 6000 - 5000 == 1000),
        Q('What usually happens with a longer term?', 'Lower monthly payments but more total interest',
          ('Higher monthly payments and less total interest', 'reversed'), ('No interest is charged at all', 'not true'),
          ('The loan never needs repaying', 'not true'), 'Tradeoff.'),
        Q('What is collateral?', 'Property the lender can take if the loan is not repaid', ('A coworker who helps the owner with the loan paperwork', 'pun'),
          ('A discount on the interest rate', 'no'), ('A free gift from the bank', 'no'), 'Security for the loan.'),
    ]),
    B=[mathb('Total repaid and interest', 'To find what a loan really costs, multiply the monthly payment by the number of '
             'payments to get the total repaid. Then subtract the amount borrowed to find the interest. Example: 36 payments of '
             '150 = 5,400 total; borrowed 4,500; interest = 900. Comparing two loans by total repaid shows which costs more, '
             'even if one has a lower monthly payment.', [
        Q('12 payments of 100. What is the total repaid?', '1,200', ('112', 'added'), ('100', 'one'), ('1,000', 'ten'),
          '12 x 100 = 1,200.', calc=lambda: 12 * 100 == 1200),
        Q('Total repaid 1,200; borrowed 1,000. What is the interest?', '200', ('1,200', 'total'), ('2,200', 'added'),
          ('1,000', 'borrowed'), '1,200 - 1,000 = 200.', calc=lambda: 1200 - 1000 == 200),
        Q('36 payments of 150. What is the total repaid?', '5,400', ('186', 'added'), ('4,500', '30'), ('150', 'one'),
          '36 x 150 = 5,400.', calc=lambda: 36 * 150 == 5400),
        Q('Loan A total 5,400; Loan B total 5,100. Which costs less?', 'Loan B', ('Loan A', 'higher'), ('They are equal', 'differ'),
          ('Cannot tell', 'can'), 'Lower total.', calc=lambda: 5100 < 5400),
        Q('Why compare total repaid rather than monthly payment alone?', 'A lower payment can hide a higher total cost',
          ('Monthly payment always shows total cost', 'not always'), ('Totals are not real money', 'they are'),
          ('Lenders forbid it', 'no'), 'Total cost matters.'),
    ], why='A learner who misses MAIN may not compute total cost; this practices total repaid and interest.')],
    F1=sec('Apply it: choose between two loans', LOAN, [
        Q('Loan A: 12 payments of 450. Loan B: 24 payments of 240. Both lend 5,000. Which has the lower total cost?', 'A, at 5,400 total',
          ('B, at 5,760 total', 'higher'), ('B, because its payment is lower', 'payment is not total'), ('They are equal', 'differ'),
          'A: 5,400; B: 5,760.', calc=lambda: 12 * 450 == 5400 and 24 * 240 == 5760),
        Q('The owner\'s cash flow can safely cover only 300 dollars a month. Which loan fits her cash flow?', 'B, at 240 a month',
          ('A, at 450 a month', 'too high'), ('Both fit easily', 'A does not'), ('Neither could ever fit', 'B fits'),
          'Affordability.', calc=lambda: 240 <= 300 < 450),
        Q('How much more interest does B cost than A?', '360 dollars', ('760 dollars', 'B interest'), ('400 dollars', 'A interest'),
          ('210 dollars', 'payment difference'), '760 - 400 = 360.', calc=lambda: (24 * 240 - 5000) - (12 * 450 - 5000) == 360),
        Q('A lender requires a personal guarantee. What does it mean for the owner?', 'She may have to repay personally if the business cannot',
          ('Nothing, because an LLC always protects her from it', 'guarantee bypasses'), ('The loan becomes free', 'no'),
          ('The lender guarantees her profit', 'no'), 'Personal liability.'),
        Q('What is the best use of a loan?', 'A plan that can realistically repay from cash flow', ('Covering ongoing losses with no plan to fix them', 'risky'),
          ('Personal vacations', 'not business'), ('Buying things that do not help sales', 'wasteful'), 'Repayable plans.'),
    ]),
    F2=sec('Handle the complications: tempting offers', LOAN, [
        Q('An online lender offers "fast cash, small daily payments" with no clear total cost. What should the owner do?', 'Ask for the total repaid and the rate before deciding',
          ('Accept quickly before the fast-cash offer ends', 'pressure'), ('Assume small payments mean low cost', 'not necessarily'),
          ('Sign without reading', 'risky'), 'Know the total.'),
        Q('Daily payments of 40 dollars for 150 business days on a 5,000-dollar advance. What is the total repaid?', '6,000 dollars',
          ('5,000 dollars', 'borrowed'), ('190 dollars', 'added'), ('4,000 dollars', '100 days'), '40 x 150 = 6,000.', calc=lambda: 40 * 150 == 6000),
        Q('A loan would cover a slow season, but sales have been falling for a year with no plan to fix it. What is the concern?',
          'The loan may only delay a bigger problem', ('No concern; loans fix falling sales', 'not alone'), ('Interest will be negative', 'no'),
          ('The bank pays the debt', 'no'), 'Fix the cause.'),
        Q('A 6,000-dollar loan at 8 percent simple interest for one year costs how much interest?', '480 dollars', ('80 dollars', 'percent as dollars'),
          ('6,480 dollars', 'total'), ('4,800 dollars', 'moved decimal'), '0.08 x 6,000 = 480.', calc=lambda: round(0.08 * 6000, 2) == 480),
        Q('Which statement is accurate?', 'Compare total cost; borrow only what cash flow can repay.',
          ('The lowest monthly payment is always the cheapest loan.', 'not always'), ('Loans never need guarantees.', 'often do'),
          ('Borrowing more fixes almost any business problem.', 'not true'), 'Careful borrowing.'),
    ]))

# ------------------------------------------------------------------ Set 127: grants
GRANT = ('A GRANT is money that does not have to be repaid, usually from a government agency, foundation or company, for '
         'specific purposes. Grants for starting a general small business are less common than many people think; many '
         'target research, specific industries, places or groups. Applications take time, have deadlines and rules about how '
         'money is spent, and may require reports. Be wary of offers that charge a fee to "guarantee" a grant. Free help '
         'finding real programs is available from SBDCs and similar organizations.')

s127 = SET('ENT.FUND.03',
    M=sec('Understand what grants are and their limits', GRANT, [
        Q('What is a grant?', 'Money for specific purposes that is not repaid',
          ('A loan with a very low interest rate from a bank', 'must be repaid'),
          ('An investment that buys part of the business', 'equity'),
          ('A tax that small businesses must pay each year', 'no'), 'Non-repayable funding.'),
        Q('Are grants for starting any general small business common?', 'Less common than many people think',
          ('Yes, every new business gets one automatically', 'not true'), ('Yes, if you pay a fee to a website', 'scam risk'),
          ('No grants exist anywhere at all', 'not true'), 'Many are targeted.'),
        Q('What do grants often require?', 'Following rules on spending and sending reports', ('Nothing at all after receiving the money', 'often rules'),
          ('Repaying the full amount with interest', 'that is a loan'), ('Giving up ownership of the business', 'that is equity'),
          'Conditions apply.'),
        Q('A website charges 199 dollars to "guarantee" a grant. What should the owner do?', 'Be wary; real programs do not sell guarantees',
          ('Pay quickly to secure the grant', 'scam risk'), ('Pay twice for a bigger grant', 'scam risk'),
          ('Give the site her bank login to speed things up', 'unsafe'), 'Guarantee offers are red flags.'),
        Q('Where can an owner get free help finding real programs?', 'An SBDC or similar organization', ('A paid "guaranteed grant" website', 'risk'),
          ('A random social media ad', 'unreliable'), ('A competitor', 'unlikely'), 'Free assistance.'),
    ]),
    B=[cs('A scholarship for a business', 'A grant is like a scholarship: free money, but only for people who fit the rules, '
          'apply on time, and use it as promised. Not every student gets a scholarship, and you would be suspicious of anyone '
          'who charged you to "guarantee" one. Grants work the same way for businesses: real, but limited, with rules to follow.', [
        Q('A grant is like what?', 'A scholarship', ('A loan from a friend', 'repaid'), ('A paycheck from work', 'earned'),
          ('A parking ticket', 'no'), 'Free money with rules.'),
        Q('Who gets a scholarship?', 'Those who fit the rules and apply on time', ('Everyone automatically, without applying', 'no'),
          ('Whoever pays a fee', 'no'), ('Nobody ever', 'no'), 'Eligibility and deadlines.'),
        Q('Someone charging to "guarantee" a scholarship is what?', 'Suspicious', ('Normal and helpful', 'no'), ('Required by schools', 'no'),
          ('A government rule', 'no'), 'Red flag.'),
        Q('Must the scholarship be used as promised?', 'Yes', ('No, any use is fine', 'rules apply'), ('Only in summer', 'no'),
          ('Only if asked', 'no'), 'Conditions.'),
        Q('Does every student get a scholarship?', 'No', ('Yes, always', 'no'), ('Only if they ask nicely', 'no'), ('Only seniors', 'no'),
          'Competitive and targeted.'),
    ], why='A learner who misses MAIN may think grants are easy money; a scholarship comparison shows the rules.')],
    F1=sec('Apply it: evaluate a grant opportunity', GRANT, [
        Q('A grant funds "rural food businesses" up to 5,000 dollars. A city tech startup applies. What is the likely issue?', 'It does not fit the grant\'s purpose',
          ('No issue; grants fit everyone', 'targeted'), ('The amount is too small to matter', 'not the issue'),
          ('Grants never fund food', 'this one does'), 'Eligibility.'),
        Q('Preparing an application takes 20 hours. The owner values her time at 30 dollars an hour. What is the time cost?', '600 dollars',
          ('50 dollars', 'added'), ('30 dollars', 'one hour'), ('20 dollars', 'hours'), '20 x 30 = 600.', calc=lambda: 20 * 30 == 600),
        Q('The grant is 5,000 dollars with a 1-in-10 chance of winning. What is the expected value?', '500 dollars', ('5,000 dollars', 'full'),
          ('50 dollars', 'moved decimal'), ('10 dollars', 'odds'), '5,000 x 0.1 = 500.', calc=lambda: round(5000 * 0.1, 2) == 500),
        Q('Comparing 500 dollars of expected value with 600 dollars of time cost, what does the math suggest alone?', 'The expected value is lower than the time cost',
          ('The grant is a guaranteed gain for her time', 'not guaranteed'), ('Time has no value', 'it does'), ('The odds are 100 percent', 'no'),
          '500 < 600.', calc=lambda: 500 < 600),
        Q('A grant requires spending only on equipment, with receipts. The owner wants to pay rent with it. What should she do?', 'Follow the spending rules',
          ('Spend it on rent and hope', 'violates'), ('Hide the receipts', 'improper'), ('Ignore the reports', 'improper'), 'Comply.'),
    ]),
    F2=sec('Handle the complications: dependence and scams', GRANT, [
        Q('An owner plans her whole launch around winning a grant she has not received. What is the risk?', 'The plan fails if the grant does not come',
          ('No risk, because grants are certain once applied for', 'not certain'), ('Grants arrive instantly', 'not always'), ('She must repay it twice', 'no'),
          'Do not depend on uncertain money.'),
        Q('A caller says she "won a federal business grant" but must pay a processing fee first. What should she do?', 'Treat it as a likely scam and verify independently',
          ('Pay the fee quickly so she can receive the grant', 'scam'), ('Give her bank login', 'scam'), ('Share her SSN', 'scam'), 'Red flags.'),
        Q('A grant requires a 25 percent matching contribution on 8,000 dollars. How much must the owner contribute?', '2,000 dollars',
          ('8,000 dollars', 'grant'), ('25 dollars', 'percent as dollars'), ('10,000 dollars', 'total'), '0.25 x 8,000 = 2,000.',
          calc=lambda: 0.25 * 8000 == 2000),
        Q('A grant\'s report is due but the owner lost receipts. What could happen?', 'She may have to repay or lose future eligibility',
          ('Nothing, because grant reports are always optional', 'often required'), ('The grant doubles', 'no'), ('Receipts are never needed', 'needed'),
          'Keep records.'),
        Q('Which statement is accurate?', 'Grants are targeted and should not be the only plan.',
          ('Every business qualifies for free startup grants.', 'not true'), ('Paying a fee guarantees a grant.', 'scam'),
          ('Grants never require reports.', 'often do'), 'Realistic expectations.'),
    ]))

# ------------------------------------------------------------------ Set 128: investors and crowdfunding
EQUITY = ('INVESTORS give money in exchange for EQUITY: a share of ownership, and often a say in decisions. If an investor '
          'pays 20,000 dollars for 20 percent, the business is valued at 100,000 dollars and the founder now owns less of '
          'it (DILUTION). Investors expect a return, usually from growth. CROWDFUNDING raises money from many people online; '
          'reward crowdfunding gives backers a product or perk, and backers expect delivery. Equity crowdfunding sells '
          'ownership and has legal rules. Read terms carefully and get advice.')

s128 = SET('ENT.FUND.04',
    M=sec('Understand equity, dilution and the main types of crowdfunding', EQUITY, [
        Q('What do investors usually receive?', 'A share of ownership (equity)', ('Repayment with fixed interest only', 'that is a loan'),
          ('Nothing at all in return', 'they expect a return'), ('The founder\'s personal home', 'no'), 'Equity.'),
        Q('An investor pays 20,000 dollars for 20 percent. What is the implied value of the business?', '100,000 dollars',
          ('20,000 dollars', 'investment'), ('400,000 dollars', 'multiplied wrong'), ('4,000 dollars', 'percent of investment'),
          '20,000 / 0.20 = 100,000.', calc=lambda: round(20000 / 0.2) == 100000),
        Q('What is dilution?', 'The founder owning a smaller share after selling equity', ('Adding water to a product', 'pun'),
          ('Paying off a business loan earlier than planned', 'no'), ('Getting a grant', 'no'), 'Ownership shrinks.'),
        Q('What do reward crowdfunding backers expect?', 'Delivery of the product or perk promised', ('Ownership shares in the company they backed', 'equity crowdfunding'),
          ('Interest payments every month', 'loan'), ('Nothing at all', 'they expect delivery'), 'Rewards.'),
        Q('Why is equity crowdfunding more complex?', 'It sells ownership and has legal rules', ('It is always free of any legal rules at all', 'not true'),
          ('It only sells T-shirts', 'that is rewards'), ('It requires no paperwork', 'not true'), 'Securities rules.'),
    ]),
    B=[mathb('Ownership percentages after investment', 'If a founder owns 100 percent and sells 25 percent to an investor, the '
             'founder keeps 100 - 25 = 75 percent. If later she sells 20 percent of the company to another investor, both '
             'earlier owners are diluted. Value implied by an investment = amount invested / percent sold. Example: 30,000 for 15 '
             'percent means 30,000 / 0.15 = 200,000.', [
        Q('A founder owns 100 percent and sells 30 percent. What does she keep?', '70 percent', ('30 percent', 'sold'), ('130 percent', 'added'),
          ('100 percent', 'unchanged'), '100 - 30 = 70.', calc=lambda: 100 - 30 == 70),
        Q('10,000 dollars buys 10 percent. What is the implied value?', '100,000', ('10,000', 'investment'), ('1,000', 'percent'),
          ('110,000', 'added'), '10,000 / 0.10 = 100,000.', calc=lambda: round(10000 / 0.1) == 100000),
        Q('30,000 dollars buys 15 percent. What is the implied value?', '200,000', ('45,000', 'added'), ('4,500', 'multiplied'),
          ('30,000', 'investment'), '30,000 / 0.15 = 200,000.', calc=lambda: round(30000 / 0.15) == 200000),
        Q('A founder owns 80 percent and sells 25 percent of the company. What does she keep?', '55 percent', ('80 percent', 'unchanged'),
          ('25 percent', 'sold'), ('105 percent', 'added'), '80 - 25 = 55 (if all new shares come from her stake).', calc=lambda: 80 - 25 == 55),
        Q('Implied value is found by dividing the investment by what?', 'The percent sold, as a decimal', ('The founder\'s age', 'no'),
          ('The number of employees on payroll', 'no'), ('The interest rate', 'no'), 'Amount / share.'),
    ], why='A learner who misses MAIN may not compute ownership or value; this practices percentages of ownership.')],
    F1=sec('Apply it: read an investment offer', EQUITY, [
        Q('An investor offers 50,000 dollars for 25 percent. What value does this imply?', '200,000 dollars', ('50,000 dollars', 'investment'),
          ('12,500 dollars', 'multiplied'), ('75,000 dollars', 'added'), '50,000 / 0.25 = 200,000.', calc=lambda: round(50000 / 0.25) == 200000),
        Q('After that deal, what percent does a founder who owned 100 percent keep?', '75 percent', ('25 percent', 'sold'),
          ('50 percent', 'guessed'), ('100 percent', 'unchanged'), '100 - 25 = 75.', calc=lambda: 100 - 25 == 75),
        Q('The investor also wants a vote on all big decisions. What should the founder consider?', 'Whether she is comfortable sharing control',
          ('Nothing; investors never affect decisions', 'they can'), ('Only the investor\'s car', 'irrelevant'),
          ('Only the logo', 'irrelevant'), 'Control matters.'),
        Q('A reward campaign promises 300 backers a lamp each. Making and shipping each lamp costs 32 dollars. What is the total cost?', '9,600 dollars',
          ('332 dollars', 'added'), ('960 dollars', 'moved decimal'), ('32 dollars', 'one lamp'), '300 x 32 = 9,600.', calc=lambda: 300 * 32 == 9600),
        Q('The campaign raised 12,000 dollars and the platform keeps 5 percent. How much does the owner receive?', '11,400 dollars',
          ('12,000 dollars', 'ignored fee'), ('600 dollars', 'fee'), ('11,950 dollars', 'subtracted 50'), '12,000 x 0.95 = 11,400.',
          calc=lambda: round(12000 * 0.95) == 11400),
    ]),
    F2=sec('Handle the complications: promises and control', EQUITY, [
        Q('After fees, the campaign leaves 11,400 dollars but lamps cost 9,600 to deliver. How much is left for everything else?', '1,800 dollars',
          ('11,400 dollars', 'ignored costs'), ('9,600 dollars', 'costs'), ('21,000 dollars', 'added'), '11,400 - 9,600 = 1,800.',
          calc=lambda: 11400 - 9600 == 1800),
        Q('Manufacturing costs rise and lamps will be late. What should the owner do?', 'Update backers honestly with a new timeline',
          ('Stay silent and hope', 'harms trust'), ('Cancel without refunds', 'improper'), ('Launch another campaign to cover it secretly', 'risky'),
          'Honest updates.'),
        Q('A founder sells 30 percent, then later another 30 percent of the company from her shares. What does she own now?', '40 percent',
          ('70 percent', 'one sale'), ('60 percent', 'sold'), ('0 percent', 'no'), '100 - 30 - 30 = 40.', calc=lambda: 100 - 30 - 30 == 40),
        Q('An equity crowdfunding platform requires disclosures. Why?', 'Selling ownership is regulated to protect investors',
          ('Disclosures are optional decoration for the page', 'required'), ('To make campaigns slower for fun', 'not the reason'),
          ('Because rewards are illegal', 'no'), 'Investor protection.'),
        Q('Which statement is accurate?', 'Investors buy ownership; crowdfunding promises must be kept.',
          ('Investors never expect a return.', 'they do'), ('Selling equity never reduces the founder\'s ownership share.', 'it does'),
          ('Backers expect nothing in return.', 'they do'), 'Know the trade.'),
    ]))

# ------------------------------------------------------------------ Set 129: money raised is not profit
RAISED = ('Money from a loan, investor, grant or crowdfunding campaign increases CASH, but it is not PROFIT. Loans must be '
          'repaid; investors own part of the business; crowdfunding backers are owed products. Profit comes only from '
          'selling for more than your costs. A business can raise a lot of money and still lose money on every sale. Track '
          'BURN RATE (how much cash the business uses each month) and RUNWAY (months until cash runs out = cash / monthly burn).')

s129 = SET('ENT.FUND.05',
    M=sec('Separate money raised from profit and compute runway', RAISED, [
        Q('Is a 30,000-dollar loan profit?', 'No, it must be repaid', ('Yes, all cash received is profit', 'not true'),
          ('Yes, if spent within a month', 'no'), ('Only if the bank is local', 'no'), 'Debt is not profit.'),
        Q('Where does profit come from?', 'Selling for more than costs', ('Raising money from investors', 'not profit'),
          ('Borrowing from a bank', 'not profit'), ('Winning a grant', 'not operating profit'), 'Operations.'),
        Q('What is burn rate?', 'How much cash the business uses each month', ('The temperature of the oven', 'pun'),
          ('The interest rate charged on a business loan', 'no'), ('The tax rate on profit', 'no'), 'Monthly cash use.'),
        Q('Cash is 24,000 and monthly burn is 3,000. What is the runway?', '8 months', ('3 months', 'burn'), ('72,000 months', 'multiplied'),
          ('21,000 months', 'subtracted'), '24,000 / 3,000 = 8.', calc=lambda: 24000 / 3000 == 8),
        Q('A business raised 50,000 dollars but loses 2 dollars on every sale. What is true?', 'It still loses money on each sale',
          ('It is profitable because it raised money', 'not true'), ('Losses disappear with funding', 'no'),
          ('Each sale now makes money', 'no'), 'Funding does not fix unit losses.'),
    ]),
    B=[mathb('Runway by division', 'Runway = cash / monthly burn. Example: 18,000 cash with 2,000 burned per month gives 18,000 / '
             '2,000 = 9 months. If the result is not whole, round DOWN, because a partial month of cash will not cover a full '
             'month: 10,000 / 3,000 = 3.33, so about 3 full months. If burn rises, runway falls; if burn drops, runway grows.', [
        Q('15,000 cash, 3,000 burn. What is the runway?', '5 months', ('3 months', 'burn'), ('12,000 months', 'subtracted'),
          ('45,000 months', 'multiplied'), '15,000 / 3,000 = 5.', calc=lambda: 15000 / 3000 == 5),
        Q('10,000 cash, 3,000 burn. How many full months?', '3', ('4', 'rounded up'), ('3.33', 'not whole'), ('7', 'subtracted'),
          '10,000 / 3,000 = 3.33, so 3 full months.', calc=lambda: math.floor(10000 / 3000) == 3),
        Q('Why round runway down?', 'A partial month of cash will not cover a full month', ('Rounding up is always the safer choice here', 'not here'),
          ('Months cannot be counted', 'they can'), ('It does not matter', 'it does'), 'Be conservative.'),
        Q('If burn rises, what happens to runway?', 'It falls', ('It rises', 'opposite'), ('It stays the same', 'no'), ('It doubles', 'no'),
          'More burn, less time.'),
        Q('20,000 cash, 2,500 burn. What is the runway?', '8 months', ('2.5 months', 'burn'), ('17,500 months', 'subtracted'),
          ('50,000 months', 'multiplied'), '20,000 / 2,500 = 8.', calc=lambda: 20000 / 2500 == 8),
    ], why='A learner who misses MAIN may not compute runway; this practices the division and rounding down.')],
    F1=sec('Apply it: read cash versus profit', RAISED, [
        Q('A startup has 40,000 dollars from investors and loses 5,000 a month. How many months of runway?', '8 months',
          ('5 months', 'burn in thousands'), ('35,000 months', 'subtracted'), ('200,000 months', 'multiplied'), '40,000 / 5,000 = 8.',
          calc=lambda: 40000 / 5000 == 8),
        Q('The founder says, "We have 40,000, so we are profitable." What is wrong?', 'Raised money is not profit; it loses money monthly',
          ('Nothing; cash always means profit', 'not true'), ('Investors always guarantee profit to the founders', 'no'), ('Losses are a type of profit', 'no'),
          'Cash versus profit.'),
        Q('If burn is cut from 5,000 to 4,000 a month, what is the new runway on 40,000?', '10 months', ('8 months', 'old'),
          ('9 months', 'miscalculated'), ('4 months', 'burn'), '40,000 / 4,000 = 10.', calc=lambda: 40000 / 4000 == 10),
        Q('A shop sells an item for 15 dollars that costs 18 dollars to make and ship. Raising more money will do what?', 'Fund more losses unless price or cost changes',
          ('Make each sale profitable', 'no'), ('Remove the costs', 'no'), ('Turn the loss on each sale into a profit', 'no'), 'Fix unit economics.'),
        Q('A 25,000-dollar loan arrives and the bank balance rises. What should the books show?', 'Cash up and a loan owed, with no profit from it',
          ('25,000 dollars of profit earned for the month', 'not profit'), ('25,000 dollars of sales', 'not sales'), ('Nothing at all', 'must record'),
          'Record properly.'),
    ]),
    F2=sec('Handle the complications: celebrating the wrong number', RAISED, [
        Q('A crowdfunding campaign raised 20,000 dollars, and the owner wants to spend it on a launch party. What is the problem?',
          'The money is owed to backers as products', ('No problem, because campaign money is profit', 'not profit'), ('Parties are always tax free', 'irrelevant'),
          ('Backers expect nothing', 'they expect rewards'), 'Obligations first.'),
        Q('Runway is 6 months. When should the owner act to raise more or cut costs?', 'Well before cash runs out', ('In the last week', 'too late'),
          ('Never; it will work out', 'risky'), ('After cash hits zero', 'too late'), 'Plan ahead.'),
        Q('Burn is 6,000 a month, cash is 30,000, and sales add 1,500 a month of net cash. What is the runway using net burn?', '6 full months',
          ('5 full months', 'gross burn'), ('20 months', 'divided by sales'), ('4 months', 'miscalculated'), '30,000 / (6,000 - 1,500) = 6.67, so 6 full months.',
          calc=lambda: math.floor(30000 / (6000 - 1500)) == 6),
        Q('Investors ask for a profit plan. What should it show?', 'How sales will exceed costs over time', ('How much more money to raise forever', 'not profit'),
          ('Only the logo and website', 'irrelevant'), ('Only the founder\'s salary', 'incomplete'), 'Path to profit.'),
        Q('Which statement is accurate?', 'Raised money adds cash; only selling above cost adds profit.',
          ('Raising money is the same as earning it from customers.', 'not true'), ('Runway grows when burn increases.', 'opposite'),
          ('Loans count as profit.', 'not true'), 'Know the difference.'),
    ]))

# ------------------------------------------------------------------ Set 130: unit economics
UNIT = ('UNIT ECONOMICS looks at whether one sale (or one customer) makes money. For one order: price minus all costs that '
        'come with that order (product, packaging, shipping, payment fees, and any discount) gives the CONTRIBUTION per order. '
        'If you pay to get customers, compare CUSTOMER ACQUISITION COST (CAC: marketing spend / new customers) with how much '
        'contribution a customer brings over time. Growing a business with negative unit economics grows the losses.')

s130 = SET('ENT.GROW.01',
    M=sec('Compute contribution per order and compare it with acquisition cost', UNIT, [
        Q('Price 40; product 15, packaging 2, shipping 8, fees 1.50. What is the contribution per order?', '13.50 dollars',
          ('25.00 dollars', 'only product cost'), ('40.00 dollars', 'price'), ('26.50 dollars', 'total costs'),
          '40 - 15 - 2 - 8 - 1.50 = 13.50.', calc=lambda: round(40 - 15 - 2 - 8 - 1.5, 2) == 13.5),
        Q('What is customer acquisition cost?', 'Marketing spend divided by new customers', ('Price minus cost per item', 'contribution'),
          ('Total sales for the year', 'revenue'), ('The cost of shipping each order to customers', 'one cost'), 'CAC.'),
        Q('Marketing spend 600 dollars brings 20 new customers. What is CAC?', '30 dollars', ('620 dollars', 'added'),
          ('12,000 dollars', 'multiplied'), ('20 dollars', 'count'), '600 / 20 = 30.', calc=lambda: 600 / 20 == 30),
        Q('What happens when a business grows with negative unit economics?', 'Its losses grow', ('Its losses shrink automatically', 'no'),
          ('It becomes profitable from size alone', 'not necessarily'), ('Costs disappear', 'no'), 'Scale magnifies losses.'),
        Q('A customer brings 13.50 per order and orders once. CAC is 30. Does the first order cover CAC?', 'No, it falls short by 16.50',
          ('Yes, with 16.50 left over', 'reversed'), ('It breaks exactly even', 'no'), ('Cannot be known', 'can'), '13.50 - 30 = -16.50.',
          calc=lambda: round(13.5 - 30, 2) == -16.5),
    ]),
    B=[cs('A lemonade stand that pays people to stop by', 'Imagine a lemonade stand earning 50 cents of profit per cup but '
          'paying a friend 1 dollar for every new customer he brings. If each customer buys only one cup, the stand loses 50 '
          'cents per customer, and the busier it gets, the more it loses. If customers come back for 3 cups, the stand earns '
          '1.50 per customer and the deal works.', [
        Q('The 1 dollar paid per new customer is like what?', 'Customer acquisition cost', ('The price per cup of lemonade', 'no'),
          ('The lemon cost', 'no'), ('A tax', 'no'), 'Cost to gain a customer.'),
        Q('With one cup per customer, what happens?', 'The stand loses 50 cents per customer', ('It earns 50 cents for each new customer', 'reversed'),
          ('It breaks even', 'no'), ('It earns 1 dollar', 'no'), '0.50 - 1.00 = -0.50.', calc=lambda: 0.5 - 1.0 == -0.5),
        Q('With three cups per customer, what is earned per customer?', '1.50 dollars', ('0.50 dollars', 'one cup'), ('3.00 dollars', 'cups'),
          ('1.00 dollar', 'CAC'), '3 x 0.50 = 1.50.', calc=lambda: 3 * 0.5 == 1.5),
        Q('If one-cup customers keep coming, what happens as the stand gets busier?', 'It loses more', ('It earns more', 'no'),
          ('Nothing changes', 'no'), ('Lemons get cheaper', 'not stated'), 'Losses scale.'),
        Q('What makes the deal work?', 'Customers coming back for more', ('Paying the friend more per customer', 'worse'), ('Fewer cups', 'worse'),
          ('Charging nothing', 'worse'), 'Repeat purchases.'),
    ], why='A learner who misses MAIN may not see how acquisition cost interacts with profit; a lemonade stand makes it concrete.')],
    F1=sec('Apply it: test unit economics', UNIT, [
        Q('A subscription box earns 9 dollars of contribution per month. Customers stay 6 months on average. What is contribution per customer?',
          '54 dollars', ('9 dollars', 'one month'), ('15 dollars', 'added'), ('1.50 dollars', 'divided'), '9 x 6 = 54.', calc=lambda: 9 * 6 == 54),
        Q('CAC is 40 dollars. Is each customer worth acquiring?', 'Yes, 54 is more than 40', ('No, 40 is more than 54', 'reversed'),
          ('They are equal', 'differ'), ('Cannot tell', 'can'), '54 > 40.', calc=lambda: 54 > 40),
        Q('By how much does contribution exceed CAC per customer?', '14 dollars', ('94 dollars', 'added'), ('54 dollars', 'contribution'),
          ('40 dollars', 'CAC'), '54 - 40 = 14.', calc=lambda: 54 - 40 == 14),
        Q('Shipping rises by 3 dollars per box. What is the new monthly contribution?', '6 dollars', ('9 dollars', 'old'), ('12 dollars', 'added'),
          ('3 dollars', 'the rise'), '9 - 3 = 6.', calc=lambda: 9 - 3 == 6),
        Q('With 6 dollars a month for 6 months and CAC 40, what happens?', 'Each customer now loses 4 dollars', ('Each still earns 14 dollars, as before', 'old'),
          ('Each earns 36 dollars', 'ignored CAC'), ('It breaks exactly even', 'no'), '36 - 40 = -4.', calc=lambda: 6 * 6 - 40 == -4),
    ]),
    F2=sec('Handle the complications: hidden costs and averages', UNIT, [
        Q('Contribution per order ignores returns. 10 percent of orders return and lose 20 dollars each. What is the average return cost per order?',
          '2 dollars', ('20 dollars', 'per return'), ('10 dollars', 'percent'), ('0.20 dollars', 'moved decimal'), '0.10 x 20 = 2.',
          calc=lambda: round(0.10 * 20, 2) == 2),
        Q('An owner plans to "make it up on volume" while losing money on each sale. What is wrong?', 'More volume multiplies the loss',
          ('Nothing; volume always fixes losses', 'not true'), ('Volume lowers taxes to zero', 'no'), ('Losses become profit after 100 sales', 'no'),
          'Fix per-unit first.'),
        Q('CAC from ads is 25 dollars, but referrals bring customers at 8 dollars. Overall CAC averages 18. What should the owner study?',
          'Which channels bring profitable customers', ('Only the overall average', 'hides differences'), ('Only the logo', 'irrelevant'),
          ('Nothing, because averages tell everything needed', 'not always'), 'Channel-level CAC.'),
        Q('Free shipping raised orders but cut contribution per order to 1 dollar. What should the owner check?', 'Whether total contribution actually rose',
          ('Only the number of orders', 'incomplete'), ('Only customer compliments', 'incomplete'), ('Nothing; more orders is always better', 'not always'),
          'Look at totals.'),
        Q('Which statement is accurate?', 'Growth helps only when each sale makes money after costs.',
          ('Growth always fixes losses.', 'not true'), ('CAC never matters for small shops.', 'it does'),
          ('Shipping and payment fees can safely be ignored.', 'they count'), 'Unit economics first.'),
    ]))

# ------------------------------------------------------------------ Set 131: getting, keeping and repeat customers
REPEAT = ('Getting a new customer usually costs more effort than keeping one. RETENTION is the share of customers who come '
          'back. REPEAT SALES come from good products, reliable service, easy reordering, and staying in touch with permission '
          '(an email list, a loyalty card, a reminder when a refill is due). A business that loses most customers after one '
          'purchase must keep finding new ones. Track how many customers buy again within a set period, such as 90 days.')

s131 = SET('ENT.GROW.02',
    M=sec('Track retention and build repeat sales', REPEAT, [
        Q('What is retention?', 'The share of customers who come back', ('The number of new ads placed each month', 'no'),
          ('Holding back an employee\'s pay', 'no'), ('A type of business loan', 'no'), 'Returning customers.'),
        Q('Of 200 customers, 60 buy again within 90 days. What is the 90-day repeat rate?', '30 percent', ('60 percent', 'count'),
          ('3 percent', 'moved decimal'), ('70 percent', 'non-repeat'), '60 / 200 = 0.3.', calc=lambda: 60 / 200 == 0.3),
        Q('Which habit encourages repeat sales?', 'A reminder when a refill is due, sent with permission', ('Making reordering harder so customers try new things', 'opposite'),
          ('Ignoring past customers', 'opposite'), ('Changing quality randomly', 'opposite'), 'Stay in touch.'),
        Q('Why does retention matter?', 'Keeping customers usually costs less than finding new ones', ('New customers are always free', 'not true'),
          ('Retention lowers product quality', 'no'), ('It replaces the need for any new sales or marketing at all', 'no'), 'Efficiency.'),
        Q('A business loses most customers after one purchase. What must it do?', 'Keep finding new customers constantly', ('Nothing different', 'no'),
          ('Raise prices for the few customers left', 'not the point'), ('Stop marketing', 'worse'), 'Low retention is costly.'),
    ]),
    B=[cs('A favorite barber', 'Many people return to the same barber for years because the cut is good, booking is easy, and '
          'the barber remembers them. The barber does not need to find a brand-new customer every time. Each happy, returning '
          'customer saves the effort and cost of attracting someone new, and may bring friends. Over years, that loyalty adds up to a steady business.', [
        Q('Why do people return to the barber?', 'Good cuts, easy booking and being remembered', ('The shop is far away', 'no'),
          ('Prices change a lot at every single visit', 'no'), ('The barber is rude', 'no'), 'Reasons to return.'),
        Q('What does a returning customer save the barber?', 'The cost of attracting someone new', ('Rent', 'no'),
          ('The cost of buying new scissors', 'no'), ('Taxes', 'no'), 'Acquisition cost.'),
        Q('Easy booking is like what in business?', 'Easy reordering', ('A complicated form', 'no'), ('A hidden phone number', 'no'),
          ('A long wait', 'no'), 'Low friction.'),
        Q('Being remembered is like what?', 'Staying in touch with customers', ('Forgetting customers after one visit', 'no'), ('Raising prices', 'no'),
          ('Ignoring complaints', 'no'), 'Relationship.'),
        Q('What extra benefit can happy regulars bring?', 'Referrals of friends', ('Higher rent for the shop', 'no'), ('More complaints', 'no'),
          ('Lower quality', 'no'), 'Word of mouth.'),
    ], why='A learner who misses MAIN may undervalue returning customers; a favorite barber shows why.')],
    F1=sec('Apply it: improve repeat sales', REPEAT, [
        Q('A coffee bean seller\'s customers run out in about 30 days. Which step encourages reorders?', 'A reminder email around day 25, with permission',
          ('No contact after the first sale', 'missed'), ('A reminder at day 120', 'too late'), ('Making the reorder page hard to find on the site', 'opposite'),
          'Timely reminder.'),
        Q('Repeat rate rises from 20 to 35 percent of 400 customers. How many more customers buy again?', '60', ('140', 'new count'),
          ('80', 'old count'), ('15', 'percent difference'), '140 - 80 = 60.', calc=lambda: round(0.35 * 400) - round(0.20 * 400) == 60),
        Q('Each repeat order brings 12 dollars of contribution. What do those 60 extra repeat orders bring?', '720 dollars', ('60 dollars', 'count'),
          ('72 dollars', 'added'), ('12 dollars', 'one'), '60 x 12 = 720.', calc=lambda: 60 * 12 == 720),
        Q('A loyalty card gives the 10th coffee free at 4 dollars. What is the discount spread over 10 coffees, per coffee?', '0.40 dollars',
          ('4.00 dollars', 'whole'), ('0.04 dollars', 'moved decimal'), ('40 dollars', 'multiplied'), '4 / 10 = 0.40.', calc=lambda: 4 / 10 == 0.4),
        Q('Customers say reordering requires creating a new account each time. What should change?', 'Make reordering easy',
          ('Add more steps', 'worse'), ('Remove the reorder option', 'worse'), ('Ignore the feedback', 'loses sales'), 'Reduce friction.'),
    ]),
    F2=sec('Handle the complications: discounts and declining quality', REPEAT, [
        Q('Repeat sales fall after the owner switched to a cheaper supplier. What should she check?', 'Whether quality dropped',
          ('Nothing; price is all customers notice', 'not true'), ('Only the logo', 'irrelevant'), ('Only competitors\' ads', 'not first'),
          'Quality drives retention.'),
        Q('A loyalty discount is so big that repeat orders barely break even. What should the owner do?', 'Adjust the reward so repeat orders stay profitable',
          ('Increase the discount further to win more loyalty', 'worse'), ('Remove all contact with customers', 'worse'), ('Ignore the math', 'risky'),
          'Profitable loyalty.'),
        Q('An email list sends daily promotions and many unsubscribe. What might help?', 'Fewer, more useful messages',
          ('Even more daily emails', 'worse'), ('Buying a new list', 'no consent'), ('Hiding the unsubscribe link', 'improper'),
          'Respect attention.'),
        Q('Of 500 customers last quarter, 150 returned this quarter. What percent did not return?', '70 percent', ('30 percent', 'returned'),
          ('150 percent', 'count'), ('35 percent', 'miscalculated'), '350 / 500 = 0.7.', calc=lambda: (500 - 150) / 500 == 0.7),
        Q('Which statement is accurate?', 'Repeat customers lower the effort and cost of growth.',
          ('New customers are always cheaper to get.', 'not usually'), ('Retention never matters for small shops.', 'it does'),
          ('Bigger discounts always build loyalty profitably.', 'not always'), 'Keep customers.'),
    ]))

# ------------------------------------------------------------------ Set 132: growing after evidence
EVID = ('Grow AFTER evidence, not before. Signs a business is ready to grow: steady demand you are turning away, positive '
        'unit economics, reliable processes, and enough cash to handle the step. Grow in small steps, such as one helper, one '
        'new product or one new location, and measure the result. Protect QUALITY: if growth causes late orders, mistakes or '
        'unhappy customers, slow down and fix the process. Growing too fast can break what made the business work.')

s132 = SET('ENT.GROW.03',
    M=sec('Grow in measured steps after evidence while protecting quality', EVID, [
        Q('Which is a sign a business is ready to grow?', 'Steady demand it is turning away', ('One very good day last year', 'not steady'),
          ('A competitor growing quickly', 'not your evidence'), ('A friend saying it should grow', 'opinion'), 'Evidence of demand.'),
        Q('What does growing in small steps mean?', 'Adding one helper, product or location and measuring',
          ('Opening five locations at once with no testing', 'big leap'), ('Doubling everything overnight', 'big leap'),
          ('Never changing anything', 'no growth'), 'Measured steps.'),
        Q('What should happen if growth causes many late orders?', 'Slow down and fix the process', ('Grow even faster to catch up', 'worse'),
          ('Ignore the complaints', 'harmful'), ('Lower quality further', 'worse'), 'Protect quality.'),
        Q('Which is NOT a sign of readiness?', 'Losing money on each sale', ('Reliable processes', 'sign'), ('Enough cash for the step', 'sign'),
          ('Steady unmet demand', 'sign'), 'Negative unit economics.'),
        Q('Why can growing too fast hurt?', 'It can break what made the business work', ('Fast growth is always safe for small businesses', 'not always'),
          ('Customers prefer chaos', 'no'), ('Quality never changes', 'it can'), 'Strain.'),
    ]),
    B=[cs('Adding floors to a building', 'A builder does not add a fifth floor before checking that the foundation can hold it. '
          'Each floor is added after the ones below are solid. A business grows the same way: each step rests on proven demand, '
          'working processes and enough cash. Adding floors on a weak foundation risks the whole building, including the floors that were already safe.', [
        Q('The foundation is like what in business?', 'Proven demand, processes and cash', ('A new logo', 'no'), ('A big opening party for friends', 'no'),
          ('A competitor', 'no'), 'What growth rests on.'),
        Q('Adding a floor is like what?', 'A growth step', ('A tax filing', 'no'), ('A refund', 'no'), ('A complaint', 'no'),
          'Expansion.'),
        Q('What does the builder check first?', 'Whether the foundation can hold the floor', ('The paint color', 'no'),
          ('The view from the new roof deck', 'no'), ('The neighbor\'s opinion', 'no'), 'Readiness.'),
        Q('What happens with a weak foundation?', 'The whole building is at risk', ('Nothing at all', 'no'), ('It grows stronger with each floor', 'no'),
          ('Rent goes down', 'no'), 'Fragile growth.'),
        Q('When is each floor added?', 'After the ones below are solid', ('All at once, on the very first day', 'no'), ('Before planning', 'no'),
          ('Randomly', 'no'), 'Step by step.'),
    ], why='A learner who misses MAIN may rush growth; adding floors to a building shows why order matters.')],
    F1=sec('Apply it: decide on a growth step', EVID, [
        Q('A bakery turns away about 30 custom-cake orders a month, has positive contribution and 3 months of cash. Which step fits?',
          'Hire one part-time baker and measure results', ('Open three new shops at once across town', 'too big'), ('Do nothing despite demand', 'missed'),
          ('Cut quality to bake faster', 'harms brand'), 'Measured step.'),
        Q('Each custom cake brings 25 dollars of contribution. 30 extra cakes would bring how much a month?', '750 dollars', ('25 dollars', 'one'),
          ('55 dollars', 'added'), ('300 dollars', 'miscalculated'), '30 x 25 = 750.', calc=lambda: 30 * 25 == 750),
        Q('The part-time baker costs 600 dollars a month. What is the net gain if all 30 cakes are made?', '150 dollars', ('750 dollars', 'gross'),
          ('600 dollars', 'cost'), ('1,350 dollars', 'added'), '750 - 600 = 150.', calc=lambda: 750 - 600 == 150),
        Q('After hiring, late orders rise from 2 to 9 a month. What should the owner do?', 'Pause growth and fix training or scheduling',
          ('Hire three more bakers immediately to catch up', 'more strain'), ('Ignore the late orders', 'harms trust'), ('Raise prices to hide it', 'not a fix'),
          'Protect quality.'),
        Q('Which evidence is strongest before opening a second location?', 'A waiting list of customers near that area', ('A dream about expansion', 'no evidence'),
          ('A cousin\'s encouragement', 'opinion'), ('A cheap lease offer in that area, alone', 'not demand'), 'Demand evidence.'),
    ]),
    F2=sec('Handle the complications: pressure to grow', EVID, [
        Q('An investor pushes the owner to open 5 stores this year, but the first store is barely profitable. What should she weigh?',
          'Whether the first store\'s results support expansion', ('Only the investor\'s excitement about growing fast', 'not evidence'),
          ('Only the store colors', 'irrelevant'), ('Nothing; growth is always right', 'not always'), 'Evidence first.'),
        Q('A big retailer offers a large order that would need all production for 3 months, stopping regular customers. What is the risk?',
          'Losing regular customers and depending on one buyer', ('No risk, because big orders are always good news', 'not always'),
          ('Regular customers never leave', 'they can'), ('Production capacity is unlimited', 'not true'), 'Concentration and quality risk.'),
        Q('A growth step costs 4,000 dollars and adds 500 dollars a month of contribution. How many months to recover the cost?', '8 months',
          ('4 months', 'miscalculated'), ('500 months', 'confused'), ('12 months', 'guessed'), '4,000 / 500 = 8.', calc=lambda: 4000 / 500 == 8),
        Q('Customer complaints doubled after growth. What is the lesson?', 'Growth strained quality and needs fixing', ('Complaints are always fine', 'no'),
          ('Grow faster so complaints become a smaller share', 'worse'), ('Stop reading complaints', 'harmful'), 'Listen to signals.'),
        Q('Which statement is accurate?', 'Grow in steps after evidence; slow down if quality slips.',
          ('Bigger leaps are always safer.', 'riskier'), ('Quality does not matter during growth.', 'it does'),
          ('Evidence is unnecessary before deciding to grow.', 'needed'), 'Careful growth.'),
    ]))

# ------------------------------------------------------------------ Set 133: burnout and a sustainable pace
PACE = ('Owners often work long hours without breaks, which can lead to BURNOUT: exhaustion, mistakes and loss of motivation. '
        'A burned-out owner is a risk to the business. A SUSTAINABLE PACE means planning work hours the owner can keep up, '
        'protecting sleep and days off, saying no to work that does not fit, raising prices when demand exceeds capacity, '
        'and getting help. Watch warning signs such as constant tiredness, more mistakes, and dreading work, and act early.')

s133 = SET('ENT.GROW.04',
    M=sec('Recognize burnout signs and plan a sustainable pace', PACE, [
        Q('What is burnout?', 'Exhaustion and mistakes from overwork', ('A kitchen fire in the shop', 'pun'),
          ('A tax penalty for late filing', 'no'), ('A marketing strategy for fast growth', 'no'), 'Overwork harm.'),
        Q('Which is a warning sign?', 'More mistakes and constant tiredness', ('Feeling rested after time off', 'healthy'),
          ('Enjoying most days of work and rest', 'healthy'), ('Steady, kept schedules', 'healthy'), 'Act early.'),
        Q('Which choice supports a sustainable pace?', 'Protecting days off', ('Answering messages at 3 a.m. every night', 'unsustainable'),
          ('Never taking a break for months', 'unsustainable'), ('Saying yes to every request', 'overload'), 'Rest.'),
        Q('Demand exceeds capacity. Which option helps both income and pace?', 'Raising prices', ('Working 20 hours a day', 'unsustainable'),
          ('Lowering prices to attract more work', 'worse'), ('Skipping sleep', 'harmful'), 'Manage demand.'),
        Q('Why is a burned-out owner a business risk?', 'Mistakes and poor decisions become more likely', ('Burnout increases profit', 'no'),
          ('Customers prefer tired, overworked owners', 'no'), ('It has no effect', 'it does'), 'Owner health matters.'),
    ]),
    B=[cs('A phone battery', 'A phone works well when charged, but if you never charge it, it slows down and shuts off at the '
          'worst moment. An owner is like that battery: work drains energy, and rest recharges it. Running on 1 percent all the '
          'time leads to mistakes and sudden shutdowns. Planning regular charging is not laziness; it keeps the phone, and the '
          'business, working.', [
        Q('What recharges the owner?', 'Rest', ('More work without breaks', 'drains'), ('Skipping meals', 'drains'),
          ('Late-night emails', 'drains'), 'Recovery.'),
        Q('Running on 1 percent is like what?', 'Working while exhausted', ('Being well rested and alert', 'opposite'), ('A day off', 'opposite'),
          ('A vacation', 'opposite'), 'Low energy.'),
        Q('What happens if the phone is never charged?', 'It shuts off at a bad moment', ('It works faster than before', 'no'),
          ('It charges itself', 'no'), ('Nothing', 'no'), 'Burnout.'),
        Q('Is planned charging laziness?', 'No, it keeps things working', ('Yes, always', 'no'), ('Only on weekends', 'no'),
          ('Only for big businesses', 'no'), 'Maintenance.'),
        Q('The owner is like what in the picture?', 'The phone battery', ('The charger cable', 'no'), ('The phone case', 'no'),
          ('The screen', 'no'), 'Energy source.'),
    ], why='A learner who misses MAIN may see rest as optional; a phone battery shows why recharging matters.')],
    F1=sec('Apply it: rebalance a week', PACE, [
        Q('An owner works 70 hours a week and makes 4 order mistakes a week. Which change fits first?', 'Cut hours by declining poor-fit work or getting help',
          ('Add 10 more hours each week to fix the mistakes', 'worse'), ('Ignore the mistakes', 'harmful'), ('Stop sleeping to catch up', 'harmful'),
          'Reduce load.'),
        Q('She wants to cut from 70 to 50 hours a week. How many hours must be removed or delegated?', '20', ('50', 'target'),
          ('70', 'current'), ('120', 'added'), '70 - 50 = 20.', calc=lambda: 70 - 50 == 20),
        Q('A price increase of 15 percent on 3,000 dollars of weekly sales with 10 percent fewer jobs. Assuming revenue scales with jobs, '
          'what is the new weekly revenue?', '3,105 dollars', ('3,450 dollars', 'no fewer jobs'), ('2,700 dollars', 'no price rise'),
          ('3,000 dollars', 'unchanged'), '3,000 x 1.15 x 0.90 = 3,105.', calc=lambda: round(3000 * 1.15 * 0.9) == 3105),
        Q('Which boundary is realistic for a solo owner?', '"Messages answered 9 a.m. to 6 p.m. on weekdays."', ('"I reply instantly at any hour, every day."', 'unsustainable'),
          ('"I never reply to anyone."', 'harmful'), ('"Replies whenever I remember."', 'unreliable'), 'Clear hours.'),
        Q('A client always demands rush work at night for normal prices. What is a reasonable step?', 'Set rush fees or decline poor-fit requests',
          ('Always accept the rush work for free', 'unsustainable'), ('Ignore the client entirely', 'harsh'), ('Work every night forever', 'burnout'),
          'Protect time.'),
    ]),
    F2=sec('Handle the complications: guilt and growth', PACE, [
        Q('An owner feels guilty taking a day off. What perspective helps?', 'Rest prevents mistakes and keeps the business running',
          ('Days off always harm a small business and its customers', 'not true'), ('Guilt proves she is right', 'no'), ('Rest is only for employees', 'no'),
          'Rest is maintenance.'),
        Q('Burnout signs appear during a growth push. What should she do?', 'Slow the push and add support before continuing',
          ('Push harder to finish the growth push faster', 'worse'), ('Hide the signs from everyone', 'harmful'), ('Quit without a plan', 'drastic'),
          'Act early.'),
        Q('A helper costs 400 dollars a month and frees 25 hours. What is the cost per freed hour?', '16 dollars', ('400 dollars', 'total'),
          ('25 dollars', 'hours'), ('10,000 dollars', 'multiplied'), '400 / 25 = 16.', calc=lambda: 400 / 25 == 16),
        Q('An owner says, "I\'ll rest after the business succeeds." What is the risk?', 'Burnout may arrive before success does',
          ('No risk; success always comes first', 'not guaranteed'), ('Rest is never needed', 'it is'), ('Success removes all stress', 'not true'),
          'Sustainable now.'),
        Q('Which statement is accurate?', 'A sustainable pace protects the owner and the business.',
          ('Longer hours always mean more success for owners.', 'not always'), ('Burnout only affects big companies.', 'not true'),
          ('Warning signs should be ignored.', 'harmful'), 'Pace matters.'),
    ]))

# ------------------------------------------------------------------ Set 134: winding down honestly
WIND = ('Sometimes the right decision is to CLOSE or pause a business. Winding down honestly means: finish or refund '
        'customer orders and prepaid services; tell customers and suppliers clearly; pay what you owe as far as possible; '
        'cancel subscriptions and licenses; file final tax returns and any state DISSOLUTION papers for an LLC or '
        'corporation; and keep records for the required period. Closing well protects your reputation and your future '
        'options.')

s134 = SET('ENT.GROW.05',
    M=sec('Close or pause a business responsibly', WIND, [
        Q('What should happen to prepaid orders when closing?', 'Fulfill them or refund the customers',
          ('Keep the money and say nothing to anyone', 'improper'), ('Ship empty boxes to close the orders', 'dishonest'),
          ('Ask customers to forget the orders', 'improper'), 'Honor obligations.'),
        Q('What is dissolution?', 'The state filing that formally ends an LLC or corporation', ('A sale of all remaining inventory at a big discount', 'not the term'),
          ('Mixing a drink with water', 'pun'), ('A new business license', 'no'), 'Formal ending.'),
        Q('Which step belongs in winding down?', 'Filing final tax returns', ('Opening new subscriptions', 'opposite'),
          ('Deleting all records immediately', 'keep records'), ('Ignoring supplier bills', 'improper'), 'Close properly.'),
        Q('Why keep records after closing?', 'They may be needed for the required period', ('Records are never needed after closing', 'not true'),
          ('To restart secretly', 'no'), ('Because records are profitable', 'no'), 'Retention rules.'),
        Q('Why does closing well matter?', 'It protects reputation and future options', ('It guarantees a refund from the state', 'no'),
          ('It cancels all debts automatically', 'not true'), ('It has no benefits', 'it does'), 'Integrity.'),
    ]),
    B=[cs('Moving out of an apartment the right way', 'When you move out, you give notice, pay the last rent, return the keys, '
          'clean up, and forward your mail. If you just disappear, the landlord is stuck, you may lose your deposit, and it '
          'is harder to rent next time. Closing a business is similar: notice, payments, paperwork and records, so you leave '
          'on good terms.', [
        Q('Giving notice is like what in a business?', 'Telling customers and suppliers', ('Hiding the closure from everyone', 'no'),
          ('Opening a new store', 'no'), ('Raising prices', 'no'), 'Communication.'),
        Q('Paying the last rent is like what?', 'Paying what the business owes', ('Ignoring the final bills that arrive', 'no'), ('A refund to yourself', 'no'),
          ('Buying inventory', 'no'), 'Settling debts.'),
        Q('Returning the keys is like what?', 'Cancelling licenses and accounts', ('Keeping every account open just in case', 'no'),
          ('Making copies', 'no'), ('Selling keys', 'no'), 'Closing access.'),
        Q('What happens if you just disappear?', 'Others are stuck and future options suffer', ('Nothing happens', 'no'),
          ('You get a bonus', 'no'), ('Rent becomes free for everyone involved', 'no'), 'Consequences.'),
        Q('Forwarding your mail is like what?', 'Making sure final notices still reach you', ('Ignoring mail', 'no'),
          ('Throwing mail away', 'no'), ('Changing your name to avoid the mail', 'no'), 'Stay reachable.'),
    ], why='A learner who misses MAIN may not see the steps of closing; moving out of an apartment shows them.')],
    F1=sec('Apply it: plan a closure', WIND, [
        Q('A shop closing has 12 prepaid orders it cannot fulfill, averaging 45 dollars. How much must be refunded?', '540 dollars',
          ('45 dollars', 'one'), ('57 dollars', 'added'), ('450 dollars', '10 orders'), '12 x 45 = 540.', calc=lambda: 12 * 45 == 540),
        Q('Which closing message to customers is best?', '"Closing June 30. Orders ship by June 20; others get refunds."',
          ('No message at all; the website just quietly goes offline', 'silence'), ('"Closed. Good luck."', 'unclear'), ('"We may be back, maybe, eventually."', 'vague'),
          'Clear and honest.'),
        Q('The business is an LLC. What state step is often needed?', 'Filing dissolution papers', ('Nothing at all', 'often needed'),
          ('Registering a new trademark', 'unrelated'), ('Applying for a new EIN', 'unrelated'), 'Formal ending.'),
        Q('Subscriptions cost 18, 25 and 40 dollars a month. If not cancelled, what would they cost over 6 months?', '498 dollars',
          ('83 dollars', 'one month'), ('415 dollars', '5 months'), ('996 dollars', '12 months'), '(18 + 25 + 40) x 6 = 498.',
          calc=lambda: (18 + 25 + 40) * 6 == 498),
        Q('Cash is 2,000 dollars and supplier bills are 2,600 dollars. What is a responsible step?', 'Contact suppliers about a payment plan',
          ('Ignore the bills', 'improper'), ('Pay one supplier and hide from others', 'unfair'), ('Spend the cash on new inventory', 'worse'),
          'Communicate.'),
    ]),
    F2=sec('Handle the complications: pausing and personal liability', WIND, [
        Q('An owner wants to pause for a year, not close. What should she check?', 'Which filings and fees continue while paused',
          ('Nothing; paused businesses have no duties', 'may continue'), ('Only the logo', 'irrelevant'), ('Only her email signature', 'irrelevant'),
          'Ongoing obligations.'),
        Q('A sole proprietor closes with unpaid business debts. What should she understand?', 'She may still be personally responsible',
          ('All debts vanish when she closes', 'not true'), ('Closing the business cancels any taxes owed', 'not true'), ('Suppliers cannot ask for payment', 'they can'),
          'Personal liability.'),
        Q('An owner deletes all records the day she closes. What problem could arise?', 'She may need them for taxes or questions later',
          ('None; records are useless after closing', 'not true'), ('It speeds up refunds', 'no'), ('It is required by law', 'no'),
          'Keep records.'),
        Q('Final payroll, taxes and reports are due. Who can help with complex final filings?', 'An accountant or tax professional',
          ('A random forum post about taxes', 'unreliable'), ('A customer', 'not qualified'), ('Nobody; skip them', 'risky'), 'Professional help.'),
        Q('Which statement is accurate?', 'Closing well means honoring orders, paying debts and filing.',
          ('Closing a business cancels all of its obligations at once.', 'not true'), ('Customers do not need notice.', 'they do'),
          ('Records can be deleted immediately.', 'keep them'), 'Responsible closure.'),
    ]))

# ------------------------------------------------------------------ Set 135: Wrigley case
WRIG = ('Documented history (Britannica): William Wrigley Jr. moved to Chicago in 1891 selling soap and offered baking powder as '
        'a premium (a free extra). Baking powder proved more popular, so he switched to selling it and offered chewing gum as '
        'a premium. The gum proved more popular, and he turned to selling chewing gum. (Exact years of each switch differ '
        'between sources.) Lesson drawn by this course (an interpretation): watch what customers actually prefer and be '
        'willing to change your main product. One success story does not guarantee the same result for another business.')

s135 = SET('ENT.CASE.09',
    M=sec('Apply a documented early decision: follow what customers actually choose', WRIG, [
        Q('According to the passage, what did Wrigley first sell in Chicago?', 'Soap', ('Chewing gum from the very start', 'came later'),
          ('Candy bars and chocolate', 'not stated'), ('Newspapers and magazines', 'not stated'), 'He started with soap.'),
        Q('What was a premium in this story?', 'A free extra given with a purchase', ('A higher price for luxury buyers', 'different meaning'),
          ('An insurance payment', 'different meaning'), ('A tax on gum', 'no'), 'An extra.'),
        Q('Why did he switch from soap to baking powder?', 'Baking powder proved more popular', ('Soap became illegal to sell', 'not stated'),
          ('Baking powder was free to make', 'not stated'), ('A competitor forced him', 'not stated'), 'Customer preference.'),
        Q('Which lesson does this course draw?', 'Watch what customers prefer and be willing to change', ('Never change your first product', 'opposite'),
          ('Give away your main product for free forever', 'not the lesson'), ('Ignore which extras customers like', 'opposite'),
          'Follow evidence.'),
        Q('What does the passage say about the exact years?', 'They differ between sources', ('They are certain and agreed everywhere', 'not stated'),
          ('They were all in 1891', 'not stated'), ('They are secret', 'no'), 'Uncertainty noted.'),
    ]),
    B=[cs('Following what people actually pick', 'At a school bake sale, you might bring cookies but notice everyone asks for the '
          'lemonade you brought as an extra. Next time, you bring more lemonade. That is following evidence: what people '
          'actually choose matters more than what you planned. The documented Wrigley facts are the switches; the lesson about '
          'following evidence is this course\'s interpretation.', [
        Q('What did people keep asking for at the bake sale?', 'The lemonade extra', ('The cookies only', 'not the point'),
          ('Nothing at all', 'no'), ('The table', 'no'), 'The extra was preferred.'),
        Q('What do you do next time?', 'Bring more lemonade', ('Bring only cookies again', 'ignores evidence'), ('Bring nothing', 'no'),
          ('Hide the lemonade', 'no'), 'Follow demand.'),
        Q('"Wrigley switched to baking powder" is which kind of statement?', 'Documented fact', ('Course interpretation', 'documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'Recorded.'),
        Q('"Follow what customers choose" is which kind?', 'The course\'s interpretation', ('A documented quote from Wrigley', 'no'),
          ('A tax rule', 'no'), ('A law', 'no'), 'Lesson drawn.'),
        Q('What matters more than your plan?', 'What people actually choose', ('Your first idea, always', 'no'), ('Your logo', 'no'),
          ('Your table color', 'no'), 'Evidence.'),
    ], why='A learner who misses MAIN may not see the lesson; a bake sale extra shows following customer choices.')],
    F1=sec('Apply it: notice the product customers prefer', WRIG, [
        Q('A candle shop gives a small free wax melt with each candle. Customers keep asking to buy the melts. What fits the lesson?',
          'Test selling melts as a main product', ('Stop giving melts so people focus on candles', 'ignores evidence'),
          ('Raise candle prices only', 'ignores melts'), ('Ignore the requests', 'ignores evidence'), 'Follow demand.'),
        Q('Last month: 120 candles sold and 300 people asked about melts. What is the ratio of melt requests to candle sales?', '2.5 to 1',
          ('1 to 2.5', 'reversed'), ('180 to 1', 'difference'), ('420 to 1', 'added'), '300 / 120 = 2.5.', calc=lambda: 300 / 120 == 2.5),
        Q('Melts cost 1 dollar to make and could sell for 4 dollars. What is the contribution per melt?', '3 dollars', ('4 dollars', 'price'),
          ('5 dollars', 'added'), ('1 dollar', 'cost'), '4 - 1 = 3.', calc=lambda: 4 - 1 == 3),
        Q('Before switching fully, what should the owner do?', 'Run a small test sale of melts and measure', ('Close the candle line immediately and switch', 'premature'),
          ('Order 10,000 melts at once', 'risky'), ('Ask only her family', 'biased'), 'Test first.'),
        Q('Which detail is documented, not interpreted?', 'Wrigley offered baking powder as a premium with soap', ('Following customer evidence always guarantees success', 'interpretation'),
          ('Every switch makes money', 'not documented'), ('Gum is always the best product', 'not documented'), 'Recorded fact.'),
    ]),
    F2=sec('Handle the complications: chasing every request', WRIG, [
        Q('Three customers ask for very different products. What should the owner do?', 'Look for patterns across many customers before changing',
          ('Switch products for each individual customer request', 'chasing noise'), ('Ignore all customers forever', 'misses evidence'),
          ('Ask only one customer', 'too few'), 'Patterns, not one-offs.'),
        Q('The new product is popular but earns less contribution than the old one. What should the owner weigh?', 'Total contribution, not just popularity',
          ('Only popularity', 'incomplete'), ('Only the logo', 'irrelevant'), ('Nothing; popular means profitable', 'not always'),
          'Look at the money.'),
        Q('Someone says, "Wrigley switched products, so I should change mine every month." What is wrong?', 'Follow clear evidence; do not change constantly',
          ('Nothing, because constant change always works for businesses', 'not true'), ('Wrigley never switched', 'he did'), ('Changes are illegal', 'no'),
          'Evidence-based change.'),
        Q('Free extras cost 0.50 dollars each across 400 sales. What do the extras cost in total?', '200 dollars', ('400 dollars', 'count'),
          ('0.50 dollars', 'one'), ('800 dollars', 'doubled'), '400 x 0.50 = 200.', calc=lambda: 400 * 0.5 == 200),
        Q('Which statement is accurate?', 'The case suggests following evidence; test your own market.',
          ('Gum is the right product for every new business owner.', 'not true'), ('Free premiums always cause a business to succeed.', 'not true'),
          ('Original plans should never change.', 'opposite'), 'Test and adapt.'),
    ]))

SETS = [s125, s126, s127, s128, s129, s130, s131, s132, s133, s134, s135]
