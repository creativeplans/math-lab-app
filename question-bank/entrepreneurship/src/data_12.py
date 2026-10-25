"""Entrepreneurship sets 63-68: Foundation 8 (continued), tax concepts.
The course teaches concepts only; no current tax rates or thresholds are taught. Any percentage used for
setting money aside is labeled as a practice assumption, not tax advice."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 63: deductions versus credits
DED = (('Two tax words are often confused. A DEDUCTION lowers the income that tax is calculated on (taxable income). '
       'A CREDIT lowers the tax itself, dollar for dollar. Example with a made-up 20 percent rate: a 1,000-dollar '
       'deduction lowers taxable income by 1,000 and saves about 0.20 x 1,000 = 200 dollars of tax; a 1,000-dollar '
       'credit cuts the tax by 1,000 dollars. A credit applies only if the business is eligible, and some credits '
       'cannot reduce the tax below zero. Business expenses that are ordinary and necessary for the business are '
       'commonly deductible; which credits apply depends on current law, so check with a tax professional.'))

s63 = SET('ENT.TAX.01',
    M=sec('Explain how deductions and credits differ', DED, [
        Q('What does a deduction lower?', 'The income that tax is calculated on',
          ('The tax itself, dollar for dollar, after it is calculated', 'that is a credit'),
          ('The price customers pay for each product', 'unrelated'),
          ('The interest rate on a business loan', 'unrelated'), 'Deductions reduce taxable income.'),
        Q('What does a credit lower?', 'The tax itself, dollar for dollar',
          ('Only the income that tax is calculated on', 'that is a deduction'),
          ('Only the number of receipts the owner must keep', 'unrelated'),
          ('Only the sales tax collected from customers', 'different tax'), 'Credits cut the tax directly.'),
        Q('With a made-up 20 percent rate, how much tax does a 500-dollar deduction save?', '100 dollars',
          ('500 dollars', 'treated as credit'), ('20 dollars', 'used rate as dollars'), ('400 dollars', 'subtracted'),
          '0.20 x 500 = 100.', calc=lambda: round(0.20 * 500, 2) == 100),
        Q('With a made-up 20 percent rate, assume a 500-dollar credit is fully eligible and usable. How much tax does it save?',
          '500 dollars',
          ('100 dollars', 'treated as deduction'), ('20 dollars', 'used rate'),
          ('2,500 dollars', 'divided by rate'),
          'A credit saves its full amount.'),
        Q('Which expenses are commonly deductible for a business?', 'Ordinary and necessary business expenses',
          ('Any personal purchase the owner makes during the year', 'personal is not business'),
          ('Only expenses paid in cash with no receipt', 'records matter'),
          ('Only expenses over 10,000 dollars each', 'not a rule'), 'The business purpose matters.'),
    ]),
    B=[cs('A coupon on the price versus a coupon on the bill', 'Imagine two coupons. One lowers the price of the item before '
          'tax is added; the other takes money straight off the final bill. A deduction is like the first coupon: it '
          'shrinks the amount that tax is figured on. A credit is like the second: it comes straight off what you owe. '
          'For the same dollar amount, the second coupon usually saves you more.', [
        Q('A deduction is like which coupon?', 'One that lowers the amount tax is figured on', ('One that comes straight off the final bill', 'that is a credit'),
          ('One that adds a fee', 'no'), ('One that expired', 'no'), 'It shrinks the base.'),
        Q('A credit is like which coupon?', 'One straight off the final bill', ('One that lowers the base', 'deduction'),
          ('One for a free gift', 'no'), ('One that raises the final bill', 'no'), 'It cuts what you owe.'),
        Q('For the same dollar amount, which usually saves more?', 'The credit', ('The deduction', 'saves only part'),
          ('They always save the same', 'not usually'), ('Neither saves anything', 'both save'), 'Credits save dollar for dollar.'),
        Q('What does "the amount tax is figured on" mean here?', 'Taxable income', ('The final bill', 'tax owed'),
          ('The coupon\'s color', 'no'), ('The store\'s name', 'no'), 'The base is taxable income.'),
        Q('"Straight off what you owe" describes what?', 'A credit', ('A deduction', 'base, not bill'), ('A fee', 'no'),
          ('A refund policy', 'no'), 'Credits cut tax owed.'),
    ], why='A learner who misses MAIN may confuse the two; two coupons show where each one applies.')],
    F1=sec('Apply it: compare tax effects with a stated assumption', DED, [
        Q('Assume a 25 percent rate (an assumption for practice). A 2,000-dollar business expense is deductible. About how '
          'much tax does it save?', '500 dollars', ('2,000 dollars', 'treated as credit'), ('25 dollars', 'used rate as dollars'),
          ('1,500 dollars', 'subtracted'), '0.25 x 2,000 = 500.', calc=lambda: 0.25 * 2000 == 500),
        Q('Assume a flat made-up 25 percent rate and that the credit is fully eligible and usable. Which saves more: a 1,000-dollar deduction or a 400-dollar credit?',
          'The 400-dollar credit',
          ('The 1,000-dollar deduction, since it is a bigger number', 'saves only 250'), ('They save exactly the same amount of tax', 'they differ'),
          ('Neither one changes the tax owed', 'both do'),
          'Deduction: 0.25 x 1,000 = 250 dollars. Credit: 400 dollars.',
          calc=lambda: 0.25 * 1000 == 250 and 400 > 250),
        Q('An owner says, "Buying anything is free because it\'s a deduction." What is wrong?', 'A deduction saves only part of the cost',
          ('Nothing; deductions refund the whole price', 'not true'), ('Deductions are always illegal', 'not true'),
          ('Purchases cannot be deducted ever', 'business expenses can be'), 'You still pay most of the cost.'),
        Q('With a 25 percent assumed rate, a 600-dollar printer that is fully deductible really costs the owner about how much '
          'after tax savings?', '450 dollars', ('600 dollars', 'ignores savings'), ('150 dollars', 'only the savings'),
          ('0 dollars', 'not free'), '600 - 150 = 450.', calc=lambda: 600 - 0.25 * 600 == 450),
        Q('Which is the best source to confirm which credits a business qualifies for?', 'A tax professional or official tax agency guidance',
          ('A product advertisement promising "tax-free" purchases', 'marketing'),
          ('A friend\'s guess based on a different year', 'outdated'),
          ('A social media post with no source listed', 'unreliable'), 'Credits depend on current law.'),
    ]),
    F2=sec('Handle the complications: claims that sound too good', DED, [
        Q('A seller claims a gadget "pays for itself through tax write-offs." What should a buyer understand?',
          'A write-off reduces taxable income; it does not refund the price', ('The government reimburses the full price of the gadget to the buyer', 'not true'),
          ('Write-offs work for personal items too', 'business use matters'), ('Tax savings always exceed cost', 'not true'),
          'Deductions save a fraction of the cost.'),
        Q('An owner deducts a family vacation as a business trip. What is the problem?', 'Personal expenses are not business deductions',
          ('No problem as long as she brings a laptop', 'not enough'), ('Vacations are always deductible', 'not true'),
          ('Deductions do not need a business purpose', 'they do'), 'Deductions require genuine business purpose.'),
        Q('The owner does not know her flat marginal rate, only that it is below 100 percent. Both items are fully eligible and the credit is fully usable. Can she still compare a deduction and a credit of the same size?',
          'Yes; under these assumptions the credit saves at least as much',
          ('No, never without the exact rate', 'logic works'), ('Yes; the deduction always saves more than a credit of the same size', 'not true'),
          ('Only if the rate is zero', 'not needed'),
          'A deduction saves rate x amount, which is less than the amount when the rate is below 100 percent; a fully usable credit saves the whole amount.'),
        Q('Credits and deductions available last year may have changed. What should the owner do?', 'Check current rules each year',
          ('Assume tax law never changes', 'it changes'), ('Copy last year\'s return exactly', 'risky'),
          ('Skip deductions to be safe', 'may overpay'), 'Rules change.'),
        Q('Which statement is accurate for this course?', 'It teaches the idea, not current rates or credit amounts.',
          ('It lists every current tax credit and rate.', 'not taught'), ('The 25 percent rate is the real rate for everyone.', 'assumption'),
          ('Deductions and credits are the same thing.', 'different'), 'Rates in questions are assumptions.'),
    ]))

# ------------------------------------------------------------------ Set 64: business use versus personal use
USE = ('Some items are used for both business and personal life: a car, a phone, a home internet plan, or part of a home. '
       'Generally only the BUSINESS-USE PORTION can be treated as a business expense. Keep evidence of the split: a '
       'mileage log for a car, or a reasonable record of phone use. Example: if a phone bill is 60 dollars and 40 percent '
       'of use is for business, the business portion is 0.40 x 60 = 24 dollars. Home office rules are specific; check '
       'official guidance or a tax professional.')

s64 = SET('ENT.TAX.02',
    M=sec('Split mixed-use costs and keep evidence', USE, [
        Q('A phone bill is 80 dollars and 25 percent of use is for business. What is the business portion?', '20 dollars',
          ('80 dollars', 'the whole bill'), ('60 dollars', 'personal part'), ('25 dollars', 'used percent as dollars'),
          '0.25 x 80 = 20.', calc=lambda: 0.25 * 80 == 20),
        Q('What evidence supports business use of a car?', 'A mileage log', ('A photo of the car\'s paint color', 'not evidence of use'),
          ('The car\'s brand name on a website', 'not evidence of use'), ('A guess written at year end', 'unreliable'),
          'Logs record business trips.'),
        Q('Which item is most likely mixed-use?', 'A cell phone used for clients and family',
          ('Packaging bought only for customer orders', 'business only'),
          ('A family birthday cake for the owner\'s child', 'personal only'),
          ('Booth rent at a craft fair for selling', 'business only'), 'Mixed use needs a split.'),
        Q('Generally, which part of a mixed-use cost may be a business expense?', 'The business-use portion',
          ('The whole cost, always, with no split needed', 'not usually'), ('None of it, ever', 'business portion may be'),
          ('Double the business portion', 'not allowed'), 'Only the business share.'),
        Q('Where should an owner check home office rules?', 'Official guidance or a tax professional',
          ('A neighbor\'s opinion over the fence', 'not authoritative'), ('A furniture store ad', 'marketing'),
          ('A video comment from a stranger', 'unreliable'), 'Home office rules are specific.'),
    ]),
    B=[mathb('Finding a percent of a bill', 'To find the business share of a bill, change the business-use percent to a decimal '
             'and multiply by the bill. 30 percent = 0.30; 0.30 x 90 = 27 dollars. The personal share is the rest: 90 - 27 '
             '= 63. Check: the two shares add back to the bill, 27 + 63 = 90. If business use is given as a fraction, like '
             '3 of 10 trips, that is 30 percent.', [
        Q('What is 30 percent of 50?', '15', ('35', 'subtracted'), ('1.5', 'moved decimal'), ('20', 'subtracted 30'),
          '0.30 x 50 = 15.', calc=lambda: round(0.30 * 50, 2) == 15),
        Q('Business share is 15 of a 50-dollar bill. What is the personal share?', '35', ('15', 'business share'),
          ('65', 'added'), ('50', 'whole bill'), '50 - 15 = 35.', calc=lambda: 50 - 15 == 35),
        Q('4 of 10 trips were for business. What percent is that?', '40 percent', ('4 percent', 'not converted'),
          ('60 percent', 'personal share'), ('14 percent', 'added'), '4 / 10 = 0.40.', calc=lambda: 4 / 10 == 0.4),
        Q('What is 60 percent of 120?', '72', ('60', 'used percent as number'), ('48', 'the other 40 percent'),
          ('180', 'added'), '0.60 x 120 = 72.', calc=lambda: round(0.60 * 120, 2) == 72),
        Q('How do you check a business and personal split?', 'The two shares add back to the bill', ('They must be equal', 'not required'),
          ('The business share must be bigger', 'not required'), ('They should multiply to the bill', 'no'),
          'Shares sum to the total.'),
    ], why='A learner who misses MAIN may not compute the business share; this practices percent of a bill.')],
    F1=sec('Apply it: calculate business portions with records', USE, [
        Q('A mileage log shows 3,000 business miles out of 12,000 total. What percent is business use?', '25 percent',
          ('75 percent', 'personal share'), ('4 percent', 'divided wrongly'), ('30 percent', 'used thousands'),
          '3,000 / 12,000 = 0.25.', calc=lambda: 3000 / 12000 == 0.25),
        Q('Home internet is 70 dollars a month; a reasonable record shows 50 percent business use. What is the yearly business '
          'portion?', '420 dollars', ('840 dollars', 'whole bill yearly'), ('35 dollars', 'one month'), ('70 dollars', 'one bill'),
          '0.50 x 70 x 12 = 420.', calc=lambda: 0.5 * 70 * 12 == 420),
        Q('An owner claims 100 percent business use of a car she also drives to the grocery store. What is the issue?',
          'The claim does not match her actual mixed use', ('No issue, because any business-use percent is allowed', 'must be accurate'),
          ('Grocery trips are business trips', 'personal'), ('Cars are never business assets', 'they can be'),
          'Claims should match records.'),
        Q('Which record best supports a phone business-use percent?', 'A sample of call and data logs showing business use',
          ('A photo of the phone\'s case and screen taken at tax time', 'not use'), ('The phone\'s purchase box', 'not use'),
          ('A guess made at tax time', 'not evidence'), 'Usage records support the split.'),
        Q('A laptop costing 900 dollars is used 80 percent for business. What is the business portion?', '720 dollars',
          ('900 dollars', 'whole cost'), ('180 dollars', 'personal share'), ('80 dollars', 'percent as dollars'),
          '0.80 x 900 = 720.', calc=lambda: 0.8 * 900 == 720),
    ]),
    F2=sec('Handle the complications: changing use and missing logs', USE, [
        Q('An owner forgot to keep a mileage log for six months. What is a sensible step now?', 'Start a log now and reconstruct carefully from calendars',
          ('Make up a full log now using round numbers for each week', 'false record'), ('Claim 100 percent business use', 'unsupported'),
          ('Skip records from now on too', 'worse'), 'Honest reconstruction plus a current log.'),
        Q('Business use of a phone rises from 30 to 60 percent mid-year. What should records show?', 'The change and when it happened',
          ('Only the higher percent for the whole year', 'inaccurate'), ('Only the lower percent', 'inaccurate'),
          ('No percent at all', 'unsupported'), 'Records should reflect reality.'),
        Q('A family member also uses the business laptop. What should the owner consider?', 'Whether the business-use percent should be lower',
          ('Nothing, because family use never matters for business items', 'it matters'), ('Raising the business percent', 'wrong direction'),
          ('Hiding the family use', 'dishonest'), 'Personal use reduces the business share.'),
        Q('Rules for home offices are detailed. What is the safest approach?', 'Read official guidance or ask a tax professional',
          ('Claim the whole home as an office', 'likely wrong'), ('Copy a friend\'s home office claim from last year', 'different facts'),
          ('Assume any room counts', 'not true'), 'Get qualified advice for specifics.'),
        Q('Which statement is accurate?', 'Mixed-use costs are split, and the split needs evidence.',
          ('Every purchase by an owner is fully deductible.', 'not true'), ('Records are optional for mixed-use items.', 'needed'),
          ('Personal use never matters.', 'it does'), 'Split and document.'),
    ]))

# ------------------------------------------------------------------ Set 65: sales tax versus income tax
SALES = ('SALES TAX is charged to customers on certain sales; the business collects it and sends it to the state or local '
         'government. It is not the business\'s money. Rules vary: some states have no general sales tax, and some items '
         'or services may be exempt. A business may need a permit or account before collecting. INCOME TAX is a tax on '
         'the business\'s profit (for many small businesses, reported on the owner\'s return). Keep collected sales tax '
         'separate so it is not spent by accident.')

s65 = SET('ENT.TAX.03',
    M=sec('Distinguish sales tax from income tax and handle collected tax', SALES, [
        Q('Who pays sales tax in the end?', 'The customer, collected by the business',
          ('The business, out of its own profit', 'collected from customers'),
          ('The supplier, before the item is shipped', 'not usually'),
          ('Nobody; it is optional for every sale', 'often required'), 'Customers pay; businesses collect.'),
        Q('What is income tax based on?', 'Profit', ('Each customer\'s sales tax amount', 'different tax'),
          ('The number of employees only', 'not the base'), ('The size of the store sign', 'irrelevant'),
          'Income tax is on profit.'),
        Q('A 50-dollar taxable sale with a 6 percent sales tax (example rate). How much tax is collected?', '3 dollars',
          ('6 dollars', 'used percent as dollars'), ('0.30 dollars', 'moved decimal'), ('53 dollars', 'total with tax'),
          '0.06 x 50 = 3.', calc=lambda: round(0.06 * 50, 2) == 3),
        Q('Why keep collected sales tax separate?', 'It belongs to the government, not the business',
          ('It is extra profit the business can spend', 'not profit'), ('It doubles if kept in savings', 'no'),
          ('It must be given back to customers each week', 'not usually'), 'It must be sent to the tax agency.'),
        Q('Do all states have the same sales tax rules?', 'No; rules vary', ('Yes; every state is identical', 'not true'),
          ('Yes; federal law sets one rate', 'no federal sales tax rate'), ('No state has sales tax', 'many do'),
          'Check the specific state and locality.'),
    ]),
    B=[cs('Holding money for someone else', 'Imagine a friend gives you 5 dollars to pass to the coach. That money is in your '
          'pocket, but it is not yours. Sales tax is like that: customers give it to you to pass to the government. Income '
          'tax is different: it is a tax on what you yourself earned as profit. Mixing the coach\'s 5 dollars with your own '
          'money can lead to spending it by mistake.', [
        Q('The coach\'s 5 dollars is like what?', 'Sales tax collected from customers', ('The business\'s own profit for the day', 'not yours'),
          ('An owner draw', 'no'), ('A refund', 'no'), 'You hold it for someone else.'),
        Q('Whose money is the coach\'s 5 dollars?', 'The coach\'s', ('Yours', 'you only hold it'), ('The friend\'s forever', 'meant for coach'),
          ('Nobody\'s', 'it belongs to someone'), 'It belongs to the coach.'),
        Q('Income tax is a tax on what?', 'What you earned as profit', ('Money held for others', 'sales tax'),
          ('Your shoes', 'no'), ('Your friend\'s money', 'no'), 'Income tax is on your profit.'),
        Q('What is the risk of mixing the 5 dollars with your own money?', 'Spending it by mistake', ('It grows', 'no'),
          ('It disappears legally', 'no'), ('Nothing at all', 'risk exists'), 'Separation prevents mistakes.'),
        Q('In this picture, the government is like whom?', 'The coach', ('The friend', 'customer'), ('You', 'the business'),
          ('The store', 'no'), 'The government receives the tax.'),
    ], why='A learner who misses MAIN may think collected sales tax is income; holding money for someone else shows it is not.')],
    F1=sec('Apply it: collect and set aside sales tax', SALES, [
        Q('A shop sells 2,000 dollars of taxable goods in a month at a 7 percent example rate. How much sales tax should it '
          'set aside?', '140 dollars', ('70 dollars', 'half'), ('14 dollars', 'moved decimal'), ('2,140 dollars', 'total'),
          '0.07 x 2,000 = 140.', calc=lambda: round(0.07 * 2000, 2) == 140),
        Q('Customers paid 1,060 dollars including 6 percent tax. How much was the sale before tax?', '1,000 dollars',
          ('996.40 dollars', 'subtracted 6 percent of total'), ('1,060 dollars', 'included tax'), ('63.60 dollars', 'tax only'),
          '1,060 / 1.06 = 1,000.', calc=lambda: round(1060 / 1.06, 2) == 1000),
        Q('A new seller plans to start collecting sales tax. What should she do first?', 'Check whether she needs a permit or account in her state',
          ('Collect it right away and keep it as business profit', 'not hers'), ('Pick any rate she likes', 'set by law'),
          ('Wait to see if anyone complains', 'risky'), 'Registration often comes first.'),
        Q('A seller collected 300 dollars of sales tax and spent it on supplies. What problem does she face?', 'She still owes 300 dollars to the tax agency',
          ('None; collected tax is hers to spend', 'not hers'), ('The tax is cancelled automatically', 'no'),
          ('She owes nothing because she spent it on business', 'still owed'), 'Collected tax must be paid.'),
        Q('Which statement correctly separates the two taxes?', 'Sales tax is collected on sales; income tax is on profit',
          ('Both taxes are really the same thing with two different names', 'different'), ('Income tax is collected from each customer', 'reversed'),
          ('Sales tax is calculated from profit', 'reversed'), 'Different bases.'),
    ]),
    F2=sec('Handle the complications: exemptions and multiple places', SALES, [
        Q('A seller ships to customers in several states. What should she check?', 'Each state\'s rules on when sales tax applies',
          ('Only her own state, since others never apply', 'may apply'), ('Nothing; online sales are never taxed', 'not true'),
          ('Only the shipping company\'s policy', 'not the law'), 'Multi-state rules can apply.'),
        Q('A service business wonders whether its services are taxable. What should it do?', 'Check the state\'s rules for that service',
          ('Assume no services are ever taxable', 'varies'), ('Assume every service is taxable', 'varies'),
          ('Ask a customer to decide', 'not their role'), 'Taxability varies by service and state.'),
        Q('A customer claims to be tax-exempt. What should the business usually ask for?', 'The documentation the state requires',
          ('Nothing; a verbal claim is always enough', 'usually not'), ('A higher price instead', 'not appropriate'),
          ('The customer\'s bank password', 'never'), 'Exemptions usually need proof.'),
        Q('Sales tax of 450 dollars was collected but filed late. What might result?', 'Penalties or interest under state rules',
          ('A bonus refund from the state for paying at all', 'no'), ('Nothing at all, ever', 'late filing has consequences'),
          ('The tax is forgiven', 'not usually'), 'File on time.'),
        Q('Which statement is accurate?', 'Sales tax rules depend on the place and the item or service, so check officially.',
          ('There is one national sales tax rate.', 'no'), ('Sales tax is always the seller\'s profit.', 'no'),
          ('Income tax and sales tax are filed together on one form in every state.', 'not necessarily'), 'Check the jurisdiction.'),
    ]))

# ------------------------------------------------------------------ Set 66: self-employment tax and estimated payments
SE = ('An employee usually has taxes WITHHELD (taken out) from each paycheck. A self-employed person usually does not, so '
      'two ideas matter. SELF-EMPLOYMENT TAX covers Social Security and Medicare on net earnings from self-employment; '
      'an employer would normally pay part of these for an employee, but a self-employed person pays them. ESTIMATED '
      'TAX PAYMENTS: because tax is pay-as-you-go, a self-employed person may need to send payments during the year '
      'instead of waiting until the return. This course teaches the ideas; rates and deadlines change, so check the IRS.')

s66 = SET('ENT.TAX.04',
    M=sec('Explain self-employment tax and why estimated payments exist', SE, [
        Q('What does withheld mean for an employee\'s paycheck?', 'Taxes are taken out before she is paid',
          ('Her paycheck is held by the bank for a month', 'not the meaning'),
          ('Her boss keeps her bonus as a reward', 'not the meaning'),
          ('Her taxes are cancelled for the year', 'not the meaning'), 'Withholding pays tax during the year.'),
        Q('What does self-employment tax cover?', 'Social Security and Medicare on net earnings',
          ('Sales tax collected from every customer', 'different tax'), ('Property tax on the owner\'s home', 'different tax'),
          ('Import fees on goods from abroad', 'different tax'), 'It covers Social Security and Medicare.'),
        Q('Why might a self-employed person make estimated payments?', 'Tax is pay-as-you-go and nothing is withheld',
          ('To earn interest from the tax agency on the money', 'not the purpose'), ('Because they are optional gifts', 'not gifts'),
          ('To avoid keeping records', 'records still needed'), 'Payments during the year replace withholding.'),
        Q('Is self-employment tax based on total sales or net earnings?', 'Net earnings', ('Total sales before costs', 'not the base'),
          ('The number of customers', 'not the base'), ('The owner\'s age', 'not the base'), 'Net earnings after expenses.'),
        Q('Where should a person check current rates and deadlines?', 'The IRS', ('A random blog from years ago', 'outdated'),
          ('A competitor', 'not authoritative'), ('A customer', 'not authoritative'), 'Rates and dates change.'),
    ]),
    B=[cs('Paying as you go', 'Think of a bus pass you top up every month versus waiting to pay for a whole year of rides at '
          'once. An employee\'s taxes are topped up every paycheck by the employer. A self-employed person has no one doing '
          'that, so they top up themselves with estimated payments during the year. Waiting until the end can mean a large '
          'bill all at once.', [
        Q('An employee\'s taxes are like what?', 'A pass topped up every paycheck by the employer', ('A pass never paid', 'no'),
          ('A free pass', 'not free'), ('A pass that customers pay for on her behalf', 'no'), 'Withholding tops up taxes.'),
        Q('Who tops up for a self-employed person?', 'The person themselves', ('Their employer', 'they have none'),
          ('Their regular customers', 'no'), ('The bank', 'no'), 'They make estimated payments.'),
        Q('What can happen if a self-employed person waits until the end?', 'A large bill all at once', ('A free year', 'no'),
          ('The bill simply vanishes', 'no'), ('A smaller bill', 'not usually'), 'Waiting builds a big balance.'),
        Q('Estimated payments are like what?', 'Topping up the pass during the year', ('Skipping payments', 'no'),
          ('A refund', 'no'), ('A fee charged to every customer', 'no'), 'Pay as you go.'),
        Q('Why does the employee not need to top up alone?', 'The employer withholds taxes from pay', ('Employees pay no tax', 'they do'),
          ('Customers pay their taxes for them', 'no'), ('Taxes are optional', 'no'), 'Withholding handles it.'),
    ], why='A learner who misses MAIN may not see why estimated payments exist; a top-up pass explains pay-as-you-go.')],
    F1=sec('Apply it: recognize when payments are needed', SE, [
        Q('Ana left a job with withholding and now freelances full time. What changed about her taxes?', 'Nobody withholds tax, so she may need estimated payments',
          ('Freelancers never owe any tax at all', 'not true'), ('Her old employer still withholds tax for her each month', 'not anymore'),
          ('Her clients must pay her taxes for her', 'not usually'), 'She must plan payments herself.'),
        Q('Ben\'s side business earns net profit. He also has a job with withholding. What should he check?', 'Whether his withholding covers the extra tax',
          ('Nothing, because side income is never taxed at all', 'it is'), ('Only his job\'s vacation policy', 'irrelevant'),
          ('Only his customers\' tax situations', 'irrelevant'), 'Side income can create extra tax.'),
        Q('Sales are 30,000 dollars and business expenses are 12,000 dollars. What are net earnings (ignoring other '
          'adjustments)?', '18,000 dollars', ('30,000 dollars', 'total sales'), ('42,000 dollars', 'added'), ('12,000 dollars', 'expenses'),
          '30,000 - 12,000 = 18,000.', calc=lambda: 30000 - 12000 == 18000),
        Q('A freelancer plans to pay all tax once, at filing time, after a profitable year. What risk does she face?',
          'A large bill and possible penalties for not paying during the year', ('No risk at all', 'there is risk'),
          ('A guaranteed refund', 'no'), ('Lower taxes than everyone else who pays during the year', 'no'), 'Pay-as-you-go rules may apply.'),
        Q('Which record helps calculate net earnings?', 'A ledger of sales and expenses', ('A list of social media followers', 'irrelevant'),
          ('A logo file', 'irrelevant'), ('A photo of the workspace', 'irrelevant'), 'Records support the calculation.'),
    ]),
    F2=sec('Handle the complications: uneven income and missed payments', SE, [
        Q('Income is very uneven: big in summer, small in winter. What helps with estimated payments?', 'Tracking income each quarter and adjusting',
          ('Paying a random amount once a year in December', 'not tied to income'), ('Ignoring payments in good months', 'risky'),
          ('Stopping record keeping in winter', 'harmful'), 'Adjust to actual income.'),
        Q('A freelancer missed an estimated payment. What is a sensible step?', 'Pay as soon as possible and check IRS guidance',
          ('Wait several years until someone from the IRS asks', 'worse'), ('Assume it is forgiven automatically', 'not usually'),
          ('Stop working to avoid taxes', 'not a solution'), 'Act promptly.'),
        Q('A friend tells her a specific self-employment tax rate from memory. What should she do?', 'Confirm it with the current IRS page',
          ('Use it without checking', 'may be outdated'), ('Ignore self-employment taxes altogether', 'harmful'), ('Ask a customer', 'not authoritative'),
          'Rates and thresholds change.'),
        Q('Which situation most clearly needs a tax professional\'s help?', 'Several income sources and big swings in profit',
          ('Choosing a font for invoices', 'not tax'), ('Picking a business email name for clients', 'not tax'),
          ('Deciding on a logo color', 'not tax'), 'Complex situations benefit from help.'),
        Q('Which statement is accurate for this course?', 'It teaches why these taxes exist, not current rates or dates.',
          ('It gives the exact current tax rate.', 'not taught'), ('Self-employed people never pay Social Security or Medicare taxes.', 'they do'),
          ('Estimated payments are only for corporations.', 'not only'), 'Check current IRS rules.'),
    ]))

# ------------------------------------------------------------------ Set 67: setting money aside for taxes
ASIDE = ('Because taxes for the self-employed are not withheld, a simple habit is to move a set percentage of each payment '
         'into a separate tax savings account. The right percentage depends on your situation; this course uses '
         'percentages like 25 or 30 percent only as PRACTICE ASSUMPTIONS, not as advice. Example with a 25 percent '
         'assumption: a 2,000-dollar payment means moving 500 dollars to tax savings. Check the amount with a tax '
         'professional or IRS tools, and adjust when income changes.')

s67 = SET('ENT.TAX.05',
    M=sec('Set aside a planned share of income for taxes', ASIDE, [
        Q('With a 25 percent assumption, how much of a 1,200-dollar payment goes to tax savings?', '300 dollars',
          ('25 dollars', 'used percent as dollars'), ('900 dollars', 'what remains'), ('1,200 dollars', 'all'),
          '0.25 x 1,200 = 300.', calc=lambda: 0.25 * 1200 == 300),
        Q('Why use a separate tax savings account?', 'So tax money is not spent by mistake',
          ('Because it earns guaranteed high returns', 'not guaranteed'),
          ('Because tax agencies require a special account', 'not a rule'),
          ('Because it lowers the tax owed automatically', 'no'), 'Separation protects the money.'),
        Q('What does this course say about the 25 or 30 percent figures?', 'They are practice assumptions, not advice',
          ('They are the official rate for every person', 'not true'), ('They are required by law', 'not true'),
          ('They never need checking', 'should be checked'), 'Use them for practice only.'),
        Q('With a 30 percent assumption, how much of a 500-dollar payment is set aside?', '150 dollars',
          ('30 dollars', 'percent as dollars'), ('350 dollars', 'remainder'), ('170 dollars', 'arithmetic slip'),
          '0.30 x 500 = 150.', calc=lambda: round(0.30 * 500, 2) == 150),
        Q('When should the percentage be reviewed?', 'When income or circumstances change', ('Never; set it once and keep it forever', 'should adjust'),
          ('Only when a customer asks', 'not related'), ('Only every ten years', 'too rare'), 'Adjust as things change.'),
    ]),
    B=[mathb('Taking a share and keeping the rest', 'If you set aside a share of a payment, you keep the rest. Set aside = '
             'percent x payment; keep = payment - set aside. With 25 percent of 800: set aside 0.25 x 800 = 200, keep 800 - '
             '200 = 600. Shortcut: keep = payment x (1 - percent) = 800 x 0.75 = 600. Check: 200 + 600 = 800. The two parts always add back to the full payment.', [
        Q('Set aside 20 percent of 1,000. How much is set aside?', '200', ('800', 'kept'), ('20', 'percent as number'),
          ('1,200', 'added'), '0.20 x 1,000 = 200.', calc=lambda: round(0.20 * 1000, 2) == 200),
        Q('Set aside 20 percent of 1,000. How much is kept?', '800', ('200', 'set aside'), ('980', 'subtracted 20'),
          ('1,020', 'added'), '1,000 - 200 = 800.', calc=lambda: 1000 - 200 == 800),
        Q('Keep = payment x (1 - percent). For 30 percent, multiply by what?', '0.70', ('0.30', 'set-aside share'),
          ('1.30', 'increase'), ('70', 'not decimal'), '1 - 0.30 = 0.70.'),
        Q('Set aside 25 percent of 400. How much is set aside?', '100', ('300', 'kept'), ('25', 'percent as number'),
          ('425', 'added'), '0.25 x 400 = 100.', calc=lambda: 0.25 * 400 == 100),
        Q('How do you check the split?', 'Set-aside plus kept equals the payment', ('They must be equal', 'not required'),
          ('Kept must be zero', 'no'), ('Multiply the two parts together to check', 'no'), 'Parts add back to the whole.'),
    ], why='A learner who misses MAIN may not split a payment into set-aside and kept parts; this practices it.')],
    F1=sec('Apply it: plan tax savings for a month', ASIDE, [
        Q('A freelancer receives 1,500, 900 and 2,100 dollars in a month. With a 25 percent assumption, how much goes to tax '
          'savings?', '1,125 dollars', ('4,500 dollars', 'total income'), ('375 dollars', 'only one payment'), ('3,375 dollars', 'kept'),
          '(1,500 + 900 + 2,100) x 0.25 = 1,125.', calc=lambda: (1500 + 900 + 2100) * 0.25 == 1125),
        Q('A freelancer receives 1,500, 900 and 2,100 dollars in a month and sets aside 25 percent for taxes. How much is left for business and personal use?',
          '3,375 dollars',
          ('1,125 dollars', 'set aside'), ('4,500 dollars', 'total'),
          ('2,250 dollars', 'half'),
          '4,500 - 1,125 = 3,375.',
          calc=lambda: 4500 - 1125 == 3375),
        Q('Which habit is most reliable?', 'Move the tax share as soon as each payment arrives',
          ('Move whatever is left at the end of the year', 'often nothing left'),
          ('Wait until the tax bill arrives to look for money', 'risky'),
          ('Keep tax money in the everyday spending account', 'easy to spend'), 'Immediate transfers work best.'),
        Q('A seller sets aside 25 percent of each sale\'s full price, but much of the price is sales tax and costs. What '
          'should she reconsider?', 'Basing the set-aside on profit, with sales tax handled separately',
          ('Setting aside 100 percent of every sale\'s full price for taxes', 'excessive'), ('Setting aside nothing at all', 'risky'),
          ('Mixing sales tax into her own savings', 'confusing'), 'Income tax relates to profit; sales tax is separate.'),
        Q('Tax savings hold 2,400 dollars and an estimated payment of 1,800 dollars is due. What remains in savings?', '600 dollars',
          ('4,200 dollars', 'added'), ('1,800 dollars', 'payment'), ('2,400 dollars', 'no payment'), '2,400 - 1,800 = 600.',
          calc=lambda: 2400 - 1800 == 600),
    ]),
    F2=sec('Handle the complications: tempting balances and changes', ASIDE, [
        Q('A slow month tempts the owner to use the tax savings for rent. What is the risk?', 'She may not have money when tax is due',
          ('None; tax savings are just extra money', 'not extra'), ('The tax bill shrinks automatically', 'no'),
          ('Rent counts as a tax payment', 'no'), 'Borrowing from tax savings creates a later gap.'),
        Q('Profit doubled this year. What should happen to the tax savings plan?', 'Review it, since tax may also rise',
          ('Keep the same dollar amount as before', 'may be too low'), ('Stop saving because profit is high', 'risky'),
          ('Spend the extra profit first', 'risky'), 'Higher profit can mean higher tax.'),
        Q('Using a 30 percent assumption on 18,000 dollars of profit gives what set-aside?', '5,400 dollars', ('540 dollars', 'moved decimal'),
          ('12,600 dollars', 'kept'), ('18,000 dollars', 'all'), '0.30 x 18,000 = 5,400.', calc=lambda: round(0.30 * 18000, 2) == 5400),
        Q('An owner is unsure whether 25 percent is enough for her situation. What is the best next step?', 'Check with a tax professional or IRS tools',
          ('Pick 5 percent instead, so she keeps more money', 'may be too low'), ('Guess and never revisit it', 'risky'),
          ('Ask her customers', 'not qualified'), 'Personalized guidance is needed.'),
        Q('Which statement is accurate?', 'A set-aside habit is a plan; the right amount depends on the person.',
          ('25 percent is always exactly right.', 'assumption only'), ('Setting money aside is illegal.', 'not true'),
          ('Self-employed people never owe tax on their business profit.', 'they can'), 'Plan, then verify.'),
    ]))

# ------------------------------------------------------------------ Set 68: records, forms and professional help
KEEP = ('Keep records that support income, deductions or credits until the period of limitations for that tax return runs '
        'out. The IRS says this is generally 3 years, with longer periods in some situations, such as certain errors or '
        'employment tax records. Keep receipts, invoices, bank statements, mileage logs and copies of filed returns, '
        'stored safely (for example, scanned with a backup). Tax forms depend on the business structure. Ask a tax '
        'professional when your situation is complex or you are unsure which forms apply.')

s68 = SET('ENT.TAX.06',
    M=sec('Keep tax records for the right time and know when to get help', KEEP, [
        Q('What does the IRS say is the general period for keeping supporting records?', '3 years, with longer periods in some situations',
          ('1 month, after which records can be thrown away', 'too short'),
          ('Forever, for every single receipt in every case', 'not the general rule'),
          ('Only until the money is spent', 'not the rule'), 'Generally 3 years, sometimes longer.'),
        Q('Which records should be kept?', 'Receipts, invoices, bank statements and mileage logs',
          ('Only the owner\'s favorite receipts', 'incomplete'), ('Only records of sales over 1,000 dollars each, and nothing else', 'incomplete'),
          ('Only social media posts about sales', 'not records'), 'Supporting documents matter.'),
        Q('Which is a safe way to store records?', 'Scanned copies with a backup', ('One paper pile in a damp garage', 'risky'),
          ('Only in a phone with no backup', 'risky'), ('Thrown away after filing', 'too early'), 'Backups protect records.'),
        Q('What do tax forms depend on?', 'The business structure', ('The owner\'s favorite color', 'irrelevant'),
          ('The number of social media posts', 'irrelevant'), ('The shop\'s paint', 'irrelevant'), 'Structure determines forms.'),
        Q('When should an owner ask a tax professional?', 'When the situation is complex or unclear', ('Never, under any circumstance at all', 'help can be needed'),
          ('Only after a penalty arrives', 'too late'), ('Only to choose a logo', 'not tax'), 'Get help when unsure.'),
    ]),
    B=[cs('A file box with labeled years', 'Picture a file box with one folder for each year. Each folder holds that year\'s '
          'receipts, invoices, bank statements and a copy of the tax return. When a folder is old enough that the period for '
          'that return has passed (generally 3 years, sometimes longer), it may be cleared out. Until then, it stays. A '
          'scanned copy is like a spare box kept somewhere else, in case the first one is lost.', [
        Q('Each folder in the box is for what?', 'One year', ('One customer', 'no'), ('One product', 'no'), ('One month only', 'year'),
          'Folders are organized by year.'),
        Q('What goes in a folder?', 'That year\'s receipts, statements and return copy', ('Only photos', 'no'),
          ('Only empty pages and blank tax forms from a store', 'no'), ('Only ads', 'no'), 'Supporting documents.'),
        Q('When may a folder be cleared out?', 'After the period for that return has passed', ('The next day', 'too early'),
          ('Never', 'eventually allowed'), ('Whenever the box gets full of papers', 'not the rule'), 'Follow the period.'),
        Q('A scanned copy is like what?', 'A spare box kept elsewhere', ('A recycling bin for paper', 'no'), ('A new receipt', 'no'),
          ('A tax bill', 'no'), 'Backups protect against loss.'),
        Q('What is the general period mentioned?', '3 years', ('3 days', 'too short'), ('30 years', 'too long'),
          ('3 months', 'too short'), 'Generally 3 years, sometimes longer.'),
    ], why='A learner who misses MAIN may not picture organized record keeping; a labeled file box shows it.')],
    F1=sec('Apply it: decide what to keep and when to ask', KEEP, [
        Q('It is 2026. An owner wants to throw out receipts that support her 2025 return. What does the general rule suggest?',
          'Keep them; the general period has not passed', ('Throw them out now', 'too soon'), ('Keep only half', 'not the rule'),
          ('Throw out the copy of the 2025 return too', 'too soon'), 'Generally 3 years after filing.'),
        Q('A flood destroys an owner\'s paper records. Which habit would have helped most?', 'Scanned copies stored with a backup',
          ('Keeping records in the same basement', 'still lost'), ('Writing totals on a sticky note', 'not proof'),
          ('Remembering amounts', 'not proof'), 'Backups protect against disasters.'),
        Q('Which situation most needs a tax professional?', 'Hiring first employees and changing to an LLC in the same year',
          ('Ordering new business cards with the LLC name on them', 'not tax'), ('Updating the website photo', 'not tax'), ('Choosing a coffee supplier', 'not tax'),
          'Multiple changes create complexity.'),
        Q('An owner has 3 years of records with about 400 receipts per year. How many receipts is that?', '1,200 receipts',
          ('403 receipts', 'added'), ('133 receipts', 'divided'), ('400 receipts', 'one year'), '3 x 400 = 1,200.',
          calc=lambda: 3 * 400 == 1200),
        Q('Which file name helps find records later?', '"2026-03 receipts - supplies"', ('"stuff"', 'vague'), ('"scan1"', 'vague'),
          ('"misc final final v2 (new)"', 'vague'), 'Clear names save time.'),
    ]),
    F2=sec('Handle the complications: longer periods and lost records', KEEP, [
        Q('Some records need to be kept longer than 3 years. What should an owner do if unsure?', 'Check IRS guidance or ask a tax professional',
          ('Throw everything out after exactly 3 years', 'may be too soon'), ('Keep nothing', 'risky'), ('Ask a customer', 'not qualified'),
          'Some situations have longer periods.'),
        Q('Records for equipment the business still uses were bought 6 years ago. Why might they still matter?', 'They may support later tax items for that equipment',
          ('They never matter after purchase', 'may matter'), ('Equipment records are illegal to keep after five years', 'no'),
          ('They only matter for customers', 'no'), 'Property records can matter longer.'),
        Q('A tax agency asks about a year with missing receipts. What can help?', 'Bank statements and other records for that year',
          ('New receipts created today for that year', 'false'), ('A guess', 'not proof'), ('Nothing at all', 'some records help'),
          'Other records can support claims.'),
        Q('An owner\'s accountant moves away and the owner has no copies of past returns. What lesson applies?', 'Keep your own copies of filed returns',
          ('Accountants must keep records forever for you', 'not guaranteed'), ('Returns are never needed again', 'they can be'),
          ('Copies are illegal to keep', 'no'), 'Owners should hold their own copies.'),
        Q('Which statement is accurate?', 'Keep records at least for the general period, and longer when rules require it.',
          ('All records can be thrown out the day after the tax return is filed.', 'too soon'), ('Only paper records count.', 'scans can work'),
          ('Professionals are never needed for taxes.', 'sometimes needed'), 'Follow the rules and get help when unsure.'),
    ]))

SETS = [s63, s64, s65, s66, s67, s68]
