"""Entrepreneurship sets 43-49: Foundation 7, costs, unit pricing, profit and break-even.
All prices, costs and rates are hypothetical assumptions for practice, not market data."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 43: one-time and recurring costs
ONE = ('Business costs come in two timing types. A ONE-TIME (startup) cost is paid once to get going: equipment, a '
       'first batch of supplies, a state filing fee, or a website design. A RECURRING cost repeats on a schedule: rent, '
       'software subscriptions, insurance, phone service, or a yearly license renewal. To compare them, convert '
       'recurring costs to the same period, such as per month or per year. In this course, all prices in questions are '
       'example assumptions, not real market prices.')

s43 = SET('ENT.COST.01',
    M=sec('Sort costs into one-time and recurring and convert periods', ONE, [
        Q('Which is a one-time cost?', 'Buying a used oven to start a bakery',
          ('Paying the monthly rent for the bakery space', 'repeats monthly'),
          ('Paying for a website hosting plan each month', 'repeats monthly'),
          ('Renewing the business license every year', 'repeats yearly'), 'Equipment bought once to start is one-time.'),
        Q('Which is a recurring cost?', 'A software subscription paid monthly',
          ('A single state filing fee to form the LLC', 'paid once'),
          ('A logo designed once by a freelancer', 'paid once'),
          ('A sewing machine bought on opening day', 'paid once'), 'Subscriptions repeat.'),
        Q('A phone plan costs 30 dollars a month. What is the yearly cost?', '360 dollars',
          ('300 dollars', 'used 10 months'), ('390 dollars', 'used 13 months'), ('30 dollars', 'one month only'),
          '30 x 12 = 360 dollars.', calc=lambda: 30 * 12 == 360),
        Q('Insurance costs 600 dollars a year. What is that per month?', '50 dollars',
          ('60 dollars', 'divided by 10'), ('600 dollars', 'not converted'), ('7,200 dollars', 'multiplied by 12'),
          '600 / 12 = 50 dollars.', calc=lambda: 600 / 12 == 50),
        Q('Why convert recurring costs to the same period?', 'To compare and add them fairly',
          ('To make every cost look smaller than it is', 'not the purpose'),
          ('Because yearly costs are not real costs', 'they are real'),
          ('Because one-time costs never matter', 'they do'), 'Same periods allow fair comparison.'),
    ]),
    B=[mathb('Converting between months and years', 'A year has 12 months. To turn a monthly amount into a yearly amount, '
             'multiply by 12. To turn a yearly amount into a monthly amount, divide by 12. Example: 25 dollars a month '
             'is 25 x 12 = 300 dollars a year, and 240 dollars a year is 240 / 12 = 20 dollars a month. Check: the '
             'yearly number should always be bigger than the monthly number.', [
        Q('How many months are in a year?', '12', ('10', 'too few'), ('7', 'days in a week'), ('52', 'weeks in a year'),
          'There are 12 months.'),
        Q('20 dollars a month is how much per year?', '240 dollars', ('200 dollars', 'used 10'), ('32 dollars', 'added 12'),
          ('120 dollars', 'used 6'), '20 x 12 = 240.', calc=lambda: 20 * 12 == 240),
        Q('120 dollars a year is how much per month?', '10 dollars', ('12 dollars', 'divided by 10'),
          ('1,440 dollars', 'multiplied'), ('108 dollars', 'subtracted 12'), '120 / 12 = 10.', calc=lambda: 120 / 12 == 10),
        Q('To change a monthly amount to yearly, you do what?', 'Multiply by 12', ('Divide by 12', 'that is yearly to monthly'),
          ('Add 12', 'not a conversion'), ('Subtract 12', 'not a conversion'), 'Multiply monthly by 12.'),
        Q('15 dollars a month is how much per year?', '180 dollars', ('150 dollars', 'used 10'), ('27 dollars', 'added 12'),
          ('165 dollars', 'used 11'), '15 x 12 = 180.', calc=lambda: 15 * 12 == 180),
    ], why='A learner who misses MAIN may have trouble changing monthly amounts to yearly ones; this practices that step.')],
    F1=sec('Apply it: list and total first-year costs', ONE, [
        Q('Startup: a 400-dollar laptop and a 100-dollar filing fee. Recurring: 20 dollars a month for software. What is '
          'the total for the first year?', '740 dollars', ('520 dollars', 'one month of software'),
          ('500 dollars', 'no software'), ('240 dollars', 'software only'), '400 + 100 + 20 x 12 = 740 dollars.',
          calc=lambda: 400 + 100 + 20 * 12 == 740),
        Q('Which cost will continue in year two?', 'Monthly booth rent at a market', ('The first sign printed for opening', 'one-time'),
          ('The LLC formation fee', 'one-time'), ('The starter set of tools', 'one-time'), 'Recurring costs continue.'),
        Q('Website A costs 300 dollars once plus 10 dollars a month. Website B costs 25 dollars a month with no setup fee. '
          'Which costs less over the first year?', 'B, at 300 dollars', ('A, at 300 dollars', 'forgot A\'s monthly fee'),
          ('A, at 420 dollars', 'A costs more'), ('They cost the same', 'they differ'),
          'A: 300 + 120 = 420; B: 25 x 12 = 300.', calc=lambda: 300 + 10 * 12 == 420 and 25 * 12 == 300),
        Q('Website A costs 300 dollars once plus 10 dollars a month. Website B costs 25 dollars a month with no setup fee. Which costs less over 3 years (36 months)?',
          'A, at 660 dollars',
          ('B, at 900 dollars', 'B costs more by year 3'), ('B, at 300 dollars', 'only one year'),
          ('They cost the same', 'they differ'),
          'A: 300 + 10 x 36 = 660; B: 25 x 36 = 900.',
          calc=lambda: 300 + 10 * 36 == 660 and 25 * 36 == 900),
        Q('A tutor lists costs: whiteboard (once), monthly ads, yearly license, textbooks (once). How many are recurring?',
          '2', ('1', 'missed one'), ('3', 'counted a one-time cost'), ('4', 'counted all'),
          'Monthly ads and yearly license recur.', calc=lambda: 2 == 2),
    ]),
    F2=sec('Handle the complications: hidden recurring costs', ONE, [
        Q('A "free" app charges 15 dollars a month after a 3-month trial. What is the cost in the first year?', '135 dollars',
          ('180 dollars', 'ignored the trial'), ('0 dollars', 'ignored charges after the trial'), ('45 dollars', 'counted trial months'),
          '9 paid months x 15 = 135 dollars.', calc=lambda: (12 - 3) * 15 == 135),
        Q('An owner budgets the startup laptop but forgets a yearly antivirus renewal. What kind of cost was missed?',
          'A recurring cost', ('A one-time cost', 'it repeats yearly'), ('A customer refund', 'not a refund'),
          ('An owner draw', 'not a draw'), 'Renewals recur.'),
        Q('A piece of equipment lasts about 3 years and costs 900 dollars. To plan for replacing it, about how much should '
          'be set aside each month?', '25 dollars', ('300 dollars', 'per year, not per month'), ('75 dollars', 'divided by 12 only'),
          ('900 dollars', 'not spread out'), '900 / 36 months = 25 dollars.', calc=lambda: 900 / 36 == 25),
        Q('Which item is easiest to forget when listing recurring costs?', 'Small subscriptions that renew automatically',
          ('The rent check the owner writes on the first of every month', 'usually remembered'), ('The large oven bought on day one', 'one-time'),
          ('The first batch of business cards', 'one-time'), 'Auto-renewals hide easily.'),
        Q('Which statement is accurate?', 'A one-time cost today can lead to recurring costs later, like repairs.',
          ('One-time costs never lead to other costs.', 'not always'), ('Recurring costs can safely be ignored by small businesses that are new.', 'not true'),
          ('All costs are recurring.', 'not true'), 'Plan for follow-on costs.'),
    ]))

# ------------------------------------------------------------------ Set 44: fixed and variable costs
FIX = ('A FIXED cost stays about the same no matter how much you sell in a period: rent, insurance, a software plan. A '
       'VARIABLE cost goes up as you sell more: ingredients, packaging, shipping, or payment fees on each sale. Example: '
       'a candle maker pays 500 dollars of rent a month (fixed) and 4 dollars of wax and jar for each candle '
       '(variable). Making 100 candles costs 500 + 4 x 100 = 900 dollars. Knowing which is which helps you plan '
       'prices and see what happens when sales change.')

s44 = SET('ENT.COST.02',
    M=sec('Classify fixed and variable costs and compute total cost', FIX, [
        Q('Which is a variable cost for a bakery?', 'Flour used for each batch of bread',
          ('Monthly rent for the bakery building', 'fixed'), ('Yearly insurance for the shop', 'fixed'),
          ('The monthly accounting software plan', 'fixed'), 'Ingredients rise with sales.'),
        Q('Which is a fixed cost for an online T-shirt shop?', 'A monthly website plan',
          ('Blank shirts bought for each order', 'variable'), ('Shipping paid on each package', 'variable'),
          ('Payment fees taken from each sale', 'variable'), 'The plan stays the same each month.'),
        Q('Using the candle example, what does it cost to make 50 candles in a month?', '700 dollars',
          ('200 dollars', 'left out rent'), ('500 dollars', 'left out wax and jars'), ('900 dollars', 'used 100 candles'),
          '500 + 4 x 50 = 700 dollars.', calc=lambda: 500 + 4 * 50 == 700),
        Q('If the candle maker sells nothing in a month, what is the total cost?', '500 dollars',
          ('0 dollars', 'rent is still due'), ('4 dollars', 'one candle'), ('504 dollars', 'added one candle'),
          'Fixed costs remain even with no sales.', calc=lambda: 500 + 4 * 0 == 500),
        Q('What happens to variable costs when sales double?', 'They roughly double',
          ('They stay exactly the same', 'that describes fixed'), ('They fall to zero', 'no'),
          ('They are cut in half', 'no'), 'Variable costs follow volume.'),
    ]),
    B=[mathb('Evaluating "fixed + rate x quantity"', 'Total cost often follows one pattern: total = fixed + (cost per item x '
             'number of items). Do the multiplication first, then add. Example: fixed 200, cost per item 3, items 40: '
             '3 x 40 = 120, then 200 + 120 = 320. A common mistake is adding first: (200 + 3) x 40 is wrong. Check that the total is never less than the fixed cost.', [
        Q('Fixed 100, cost per item 2, items 30. What is the total?', '160', ('3,060', 'added first'), ('132', 'added all three'),
          ('60', 'left out fixed'), '100 + 2 x 30 = 160.', calc=lambda: 100 + 2 * 30 == 160),
        Q('Which step comes first in "fixed + rate x quantity"?', 'Multiply rate by quantity', ('Add the fixed cost and the rate', 'wrong order'),
          ('Subtract quantity', 'not a step'), ('Divide by fixed', 'not a step'), 'Multiplication before addition.'),
        Q('Fixed 300, cost per item 5, items 20. What is the total?', '400', ('6,100', 'added first'), ('325', 'added all'),
          ('100', 'left out fixed'), '300 + 5 x 20 = 400.', calc=lambda: 300 + 5 * 20 == 400),
        Q('Fixed 50, cost per item 10, items 0. What is the total?', '50', ('0', 'fixed remains'), ('60', 'added rate'),
          ('500', 'multiplied fixed'), '50 + 10 x 0 = 50.', calc=lambda: 50 + 10 * 0 == 50),
        Q('Fixed 250, cost per item 1.50, items 100. What is the total?', '400', ('351.50', 'added the rate to items'),
          ('150', 'left out fixed'), ('25,150', 'added first'), '250 + 1.50 x 100 = 400.', calc=lambda: 250 + 1.5 * 100 == 400),
    ], why='A learner who misses MAIN may compute total cost in the wrong order; this practices fixed plus rate times quantity.')],
    F1=sec('Apply it: estimate monthly cost at different sales levels', FIX, [
        Q('A soap maker pays 300 dollars a month for a studio and 2 dollars of supplies per bar. What is the cost for 200 '
          'bars?', '700 dollars', ('400 dollars', 'left out rent'), ('302 dollars', 'one bar'), ('500 dollars', 'used 100 bars'),
          '300 + 2 x 200 = 700 dollars.', calc=lambda: 300 + 2 * 200 == 700),
        Q('A soap maker pays 300 dollars a month for a studio, which does not change with output, and 2 dollars of supplies per bar. How much more does it cost to make 300 bars than 200 bars?',
          '200 dollars',
          ('300 dollars', 'added rent again'), ('100 dollars', 'used 1 dollar per bar'),
          ('900 dollars', 'total for 300'),
          'Only variable cost changes: 2 x 100 = 200 dollars.',
          calc=lambda: (300 + 2 * 300) - (300 + 2 * 200) == 200),
        Q('Which cost is variable for a mobile car wash?', 'Soap and water used per car', ('The van loan payment', 'fixed'),
          ('Monthly phone plan', 'fixed'), ('Yearly business license', 'fixed'), 'Supplies rise with each wash.'),
        Q('A dog walker has 60 dollars a month of fixed costs and 1 dollar of variable cost per walk. In a month with 80 '
          'walks, what is the average cost per walk?', '1.75 dollars', ('1.00 dollar', 'ignored fixed costs'),
          ('0.75 dollars', 'only fixed per walk'), ('140 dollars', 'total cost'), '(60 + 80) / 80 = 1.75 dollars.',
          calc=lambda: (60 + 1 * 80) / 80 == 1.75),
        Q('When sales rise, what happens to the fixed cost per item?', 'It goes down', ('It goes up', 'spread over more items'),
          ('It stays exactly the same', 'per-item share changes'), ('It becomes variable', 'still fixed'),
          'The same fixed cost is shared by more items.'),
    ]),
    F2=sec('Handle the complications: costs that do not fit neatly', FIX, [
        Q('A baker\'s rent is fixed, but if sales triple she must rent a second oven. What does this show?',
          'Fixed costs can step up at higher volumes', ('Fixed costs never change at all', 'they can step up'),
          ('Ovens are variable costs that rise with each loaf', 'not per loaf'), ('Rent is a variable cost', 'still fixed'),
          'Capacity limits create steps.'),
        Q('A shipping service charges 5 dollars per package up to 100 packages, then 4 dollars per package after that. What is '
          'the cost for 150 packages?', '700 dollars', ('750 dollars', 'used 5 dollars for all'), ('600 dollars', 'used 4 dollars for all'),
          ('200 dollars', 'only the extra'), '100 x 5 + 50 x 4 = 700 dollars.', calc=lambda: 100 * 5 + 50 * 4 == 700),
        Q('An owner counts her own hours as free. What cost is missing?', 'The value of her time', ('Rent', 'counted'),
          ('Supplies used for each item', 'counted'), ('Shipping', 'counted'), 'Owner time has value even if unpaid.'),
        Q('A phone bill is 40 dollars a month plus overage charges in busy months. How should it be planned?', 'As mostly fixed with a variable part',
          ('As a fully variable cost for each sale', 'mostly fixed'), ('As a one-time cost', 'recurring'), ('As free', 'it costs money'),
          'Some costs are mixed.'),
        Q('Which statement is accurate?', 'Classifying costs is an estimate that helps planning, not an exact law.',
          ('Every single cost is either perfectly fixed or perfectly variable, always.', 'some are mixed'),
          ('Variable costs never matter for small sellers.', 'they matter'),
          ('Fixed costs are always larger than variable costs.', 'depends'), 'Use classification as a tool.'),
    ]))

# ------------------------------------------------------------------ Set 45: realistic startup budget
BUD = ('A STARTUP BUDGET lists what you expect to spend before and during the first months. List one-time costs (equipment, '
       'filing fees, first inventory) and recurring costs for several months, because sales often start slowly. Add a '
       'CONTINGENCY: an extra amount, often a percentage, for surprises such as a repair or a price increase. Write down '
       'your ASSUMPTIONS (for example, "rent stays 400 dollars a month") so you can check them later. Compare the '
       'total with the money available.')

s45 = SET('ENT.COST.03',
    M=sec('Build a startup budget with assumptions and contingency', BUD, [
        Q('What is a contingency in a budget?', 'Extra money set aside for surprises',
          ('Money owed to customers for refunds', 'not the meaning'),
          ('The owner\'s profit for the first year', 'not the meaning'),
          ('A tax paid to the state each month', 'not the meaning'), 'It covers unexpected costs.'),
        Q('Why include several months of recurring costs?', 'Sales often start slowly',
          ('Recurring costs are paid only once', 'they repeat'),
          ('Banks require exactly twelve months listed', 'not a rule'),
          ('It makes the budget look smaller', 'it makes it larger'), 'Early months may not cover costs.'),
        Q('One-time costs are 2,000 dollars and 3 months of recurring costs are 900 dollars. A 10 percent contingency is '
          'added. What is the total budget?', '3,190 dollars', ('2,900 dollars', 'no contingency'),
          ('3,100 dollars', 'contingency on one-time only'), ('2,990 dollars', 'added 90 only'),
          '2,900 x 1.10 = 3,190 dollars.', calc=lambda: round((2000 + 900) * 1.10, 2) == 3190),
        Q('What is an assumption in a budget?', 'A stated guess, like "rent stays 400 dollars a month"',
          ('A cost the owner has already paid in full to a supplier', 'not a guess'), ('A receipt from a supplier', 'a record'),
          ('A tax form filed with the IRS', 'a filing'), 'Assumptions can be checked later.'),
        Q('A budget totals 5,000 dollars and the owner has 4,200 dollars. What is the gap?', '800 dollars',
          ('9,200 dollars', 'added'), ('4,200 dollars', 'money available'), ('5,000 dollars', 'the budget'),
          '5,000 - 4,200 = 800 dollars.', calc=lambda: 5000 - 4200 == 800),
    ]),
    B=[mathb('Finding a percent of an amount', 'To find a percent of an amount, change the percent to a decimal and '
             'multiply. 10 percent = 0.10, 15 percent = 0.15, 5 percent = 0.05. Example: 10 percent of 3,000 is '
             '0.10 x 3,000 = 300. To ADD a percent, multiply by 1 plus the decimal: 3,000 x 1.10 = 3,300. Check: 10 '
             'percent is one tenth, so move the decimal point one place.', [
        Q('What is 10 percent of 500?', '50', ('5', 'moved two places'), ('510', 'added 10'), ('5,000', 'multiplied by 10'),
          '0.10 x 500 = 50.', calc=lambda: 0.10 * 500 == 50),
        Q('15 percent as a decimal is what?', '0.15', ('1.5', 'one place'), ('15.0', 'not converted'), ('0.015', 'three places'),
          '15 / 100 = 0.15.'),
        Q('What is 500 increased by 10 percent?', '550', ('510', 'added 10'), ('50', 'only the percent'), ('5,000', 'multiplied by 10'),
          '500 x 1.10 = 550.', calc=lambda: round(500 * 1.10, 2) == 550),
        Q('What is 5 percent of 2,000?', '100', ('10', 'moved too far'), ('400', 'divided by 5'), ('2,005', 'added 5'),
          '0.05 x 2,000 = 100.', calc=lambda: 0.05 * 2000 == 100),
        Q('What is 20 percent of 150?', '30', ('3', 'moved too far'), ('170', 'added 20'), ('7.5', 'divided by 20'),
          '0.20 x 150 = 30.', calc=lambda: round(0.20 * 150, 2) == 30),
    ], why='A learner who misses MAIN may struggle to add a contingency percentage; this practices percent of an amount.')],
    F1=sec('Apply it: check a draft budget', BUD, [
        Q('Ida\'s budget: equipment 1,500, first inventory 800, 3 months of rent at 350, no contingency. What is missing?',
          'A contingency for surprises', ('The equipment cost', 'listed'), ('The cost of the first inventory', 'listed'), ('Rent', 'listed'),
          'No buffer is included.'),
        Q("Ida's budget: equipment 1,500 dollars, first inventory 800 dollars, and 3 months of rent at 350 dollars. What is the total before any contingency?",
          '3,350 dollars',
          ('2,650 dollars', 'one month of rent'), ('2,300 dollars', 'no rent'),
          ('4,400 dollars', 'six months of rent'),
          '1,500 + 800 + 3 x 350 = 3,350 dollars.',
          calc=lambda: 1500 + 800 + 3 * 350 == 3350),
        Q('If Ida adds a 15 percent contingency to 3,350 dollars, what is the new total?', '3,852.50 dollars',
          ('3,365 dollars', 'added 15'), ('3,850 dollars', 'rounded too early'), ('502.50 dollars', 'only the contingency'),
          '3,350 x 1.15 = 3,852.50 dollars.', calc=lambda: round(3350 * 1.15, 2) == 3852.50),
        Q('An assumption says "supplies cost 2 dollars per unit." The supplier now charges 2.40 dollars. What should Ida do?',
          'Update the assumption and recalculate', ('Keep the old number; budgets never change', 'outdated'),
          ('Delete the supplies line', 'cost still exists'), ('Double every cost to be safe', 'not justified'),
          'Budgets improve when assumptions are checked.'),
        Q('Which budget is most realistic for a new café?', 'One with equipment, several months of costs and a buffer',
          ('One listing only the espresso machine', 'incomplete'), ('One assuming full sales on day one', 'unrealistic'),
          ('One with no rent listed, because the first rent is due later', 'still due'), 'Completeness and buffers matter.'),
    ]),
    F2=sec('Handle the complications: tight money and changing plans', BUD, [
        Q('A budget needs 6,000 dollars; the owner has 4,500. Which option keeps risk lowest?', 'Start smaller and cut nonessential costs',
          ('Borrow at a high rate without a repayment plan', 'adds risk'), ('Remove the contingency and hope', 'adds risk'),
          ('Skip rent payments for a while', 'harmful'), 'Reducing scope fits the available money.'),
        Q('An owner\'s contingency is 5 percent but her equipment is old and breaks often. What should she consider?',
          'A larger contingency', ('No contingency at all', 'adds risk'), ('Removing equipment from the budget', 'still needed'),
          ('Assuming nothing will break', 'unrealistic'), 'Risky situations need bigger buffers.'),
        Q('A budget used last year\'s prices. Prices rose about 8 percent. A 2,500-dollar line becomes about how much?', '2,700 dollars',
          ('2,508 dollars', 'added 8'), ('200 dollars', 'only the increase'), ('3,300 dollars', 'added 800'),
          '2,500 x 1.08 = 2,700 dollars.', calc=lambda: round(2500 * 1.08, 2) == 2700),
        Q('Which mistake makes a budget look better than reality?', 'Leaving out the owner\'s living costs while sales are slow',
          ('Writing down each assumption clearly', 'helpful'), ('Including a buffer', 'helpful'),
          ('Listing recurring costs for several months ahead of time', 'helpful'), 'Personal needs affect how long the owner can last.'),
        Q('Which statement is accurate?', 'A budget is a plan to update as real numbers arrive.',
          ('A budget is fixed and never changes.', 'should be updated'), ('A budget guarantees profit.', 'no'),
          ('Budgets are only useful for large companies with many staff.', 'all benefit'), 'Update as you learn.'),
    ]))

# ------------------------------------------------------------------ Set 46: price and cost per item
UNIT = ('COST PER ITEM (unit cost) is what it costs you to make or buy one item. If a batch of 40 cookies uses 20 '
        'dollars of ingredients and 4 dollars of bags, the cost per cookie is (20 + 4) / 40 = 0.60 dollars. PRICE is '
        'what the customer pays. The difference, price minus cost per item, is what each sale contributes toward '
        'fixed costs and profit. A price below the cost per item loses money on every sale. Include everything the '
        'item uses, such as packaging and labels, not just the main material.')

s46 = SET('ENT.PRICE.01',
    M=sec('Compute cost per item and compare it with price', UNIT, [
        Q('A batch of 50 bracelets uses 75 dollars of beads and string. What is the cost per bracelet?', '1.50 dollars',
          ('3.75 dollars', 'divided wrongly'), ('0.67 dollars', 'divided 50 by 75'), ('75.00 dollars', 'not divided'),
          '75 / 50 = 1.50 dollars.', calc=lambda: 75 / 50 == 1.5),
        Q('The cookie cost per item is 0.60 dollars. The price is 1.50 dollars. What does each sale contribute?', '0.90 dollars',
          ('2.10 dollars', 'added'), ('0.60 dollars', 'the cost'), ('1.50 dollars', 'the price'),
          '1.50 - 0.60 = 0.90 dollars.', calc=lambda: round(1.50 - 0.60, 2) == 0.90),
        Q('What happens if the price is below the cost per item?', 'Each sale loses money',
          ('Each sale makes more profit than before', 'not true'), ('Fixed costs disappear', 'no'),
          ('Nothing changes at all', 'losses grow'), 'Price must exceed unit cost.'),
        Q('Which should be included in cost per item for a candle?', 'Wax, wick, jar and label',
          ('Only the wax, since it is the main material', 'incomplete'),
          ('Only the label, since customers see it', 'incomplete'),
          ('The owner\'s personal groceries', 'not a business cost'), 'Include everything the item uses.'),
        Q('A batch of 20 cards costs 8 dollars of paper and 2 dollars of envelopes. What is the cost per card?', '0.50 dollars',
          ('0.40 dollars', 'paper only'), ('0.10 dollars', 'envelopes only'), ('10.00 dollars', 'not divided'),
          '(8 + 2) / 20 = 0.50 dollars.', calc=lambda: (8 + 2) / 20 == 0.5),
    ]),
    B=[mathb('Dividing a total among items', 'To find the cost of one item from a batch, add up everything the batch '
             'cost, then divide by the number of items. Example: 30 dollars for 12 items: 30 / 12 = 2.50 dollars '
             'each. Check by multiplying back: 2.50 x 12 = 30. If the answer is bigger than the total, you probably '
             'divided the wrong way.', [
        Q('24 dollars for 8 items. What is the cost per item?', '3 dollars', ('0.33 dollars', 'divided 8 by 24'),
          ('192 dollars', 'multiplied'), ('16 dollars', 'subtracted'), '24 / 8 = 3.', calc=lambda: 24 / 8 == 3),
        Q('How do you check 2.50 dollars per item for 12 items?', 'Multiply 2.50 by 12 to get 30', ('Add 2.50 and 12', 'not a check'),
          ('Divide 12 by 2.50', 'not a check'), ('Subtract 12 from 30 and compare', 'not a check'), 'Multiplying back checks the division.'),
        Q('45 dollars for 10 items. What is the cost per item?', '4.50 dollars', ('0.22 dollars', 'divided wrong way'),
          ('35 dollars', 'subtracted'), ('450 dollars', 'multiplied'), '45 / 10 = 4.50.', calc=lambda: 45 / 10 == 4.5),
        Q('12 dollars of ingredients plus 3 dollars of boxes for 30 items. What is the cost per item?', '0.50 dollars',
          ('0.40 dollars', 'ingredients only'), ('0.10 dollars', 'boxes only'), ('15 dollars', 'not divided'),
          '(12 + 3) / 30 = 0.50.', calc=lambda: (12 + 3) / 30 == 0.5),
        Q('A result of 240 dollars per item from a 60-dollar batch of 4 is a sign of what?', 'Multiplying instead of dividing',
          ('A correct answer for the batch', '60 / 4 = 15'), ('A cheap batch', 'no'), ('A missing item', 'no'), '60 x 4 = 240 is the mistake.',
          calc=lambda: 60 * 4 == 240 and 60 / 4 == 15),
    ], why='A learner who misses MAIN may not divide the batch cost correctly; this practices division and checking.')],
    F1=sec('Apply it: set a price that covers cost', UNIT, [
        Q('A tote bag costs 6 dollars to make. Which price at least covers the cost per item?', '9 dollars',
          ('5 dollars', 'below cost'), ('4 dollars', 'below cost'), ('5.50 dollars', 'below cost'), '9 > 6.',
          calc=lambda: 9 > 6),
        Q('A baker makes 24 muffins with 18 dollars of ingredients and 6 dollars of liners and boxes. She prices muffins at '
          '2 dollars. What does each muffin contribute?', '1.00 dollar', ('1.25 dollars', 'ingredients only'),
          ('0.75 dollars', 'cost per item'), ('2.00 dollars', 'the price'), 'Cost = 24 / 24 = 1.00; 2.00 - 1.00 = 1.00.',
          calc=lambda: 2 - (18 + 6) / 24 == 1.0),
        Q('A printer charges 0.80 dollars per sticker plus 10 dollars per order. An order of 100 stickers costs how much per sticker?',
          '0.90 dollars', ('0.80 dollars', 'left out order fee'), ('0.10 dollars', 'only the order fee'), ('90 dollars', 'total cost'),
          '(0.80 x 100 + 10) / 100 = 0.90 dollars.', calc=lambda: (0.80 * 100 + 10) / 100 == 0.90),
        Q('A seller forgot the 0.30-dollar label on each 2-dollar item. What is the true cost per item?', '2.30 dollars',
          ('2.00 dollars', 'forgot the label'), ('1.70 dollars', 'subtracted'), ('0.30 dollars', 'label only'),
          '2.00 + 0.30 = 2.30 dollars.', calc=lambda: round(2.00 + 0.30, 2) == 2.30),
        Q('Two suppliers: A sells 100 jars for 120 dollars; B sells 60 jars for 66 dollars. Which is cheaper per jar?',
          'B, at 1.10 dollars', ('A, at 1.20 dollars', 'A is higher'), ('A, at 1.10 dollars', 'mixed up'), ('They cost the same', 'they differ'),
          'A: 1.20; B: 66 / 60 = 1.10.', calc=lambda: 120 / 100 == 1.2 and 66 / 60 == 1.1),
    ]),
    F2=sec('Handle the complications: waste, minimums and changing costs', UNIT, [
        Q('A baker makes 40 cookies but 4 break and cannot be sold. Ingredients cost 20 dollars. What is the cost per SOLD '
          'cookie, to the nearest cent?', '0.56 dollars', ('0.50 dollars', 'divided by 40'), ('0.45 dollars', 'divided by 44'),
          ('5.00 dollars', 'divided by 4'), '20 / 36 = 0.555... about 0.56.', calc=lambda: round(20 / 36, 2) == 0.56),
        Q('A supplier requires a minimum order of 500 labels for 50 dollars, but the owner needs only 100 this month. What is the purchase cost per label?',
          '0.10 dollars',
          ('0.50 dollars', 'divided by the 100 used, not the 500 bought'), ('5.00 dollars', 'divided 50 by 10'),
          ('50 dollars', 'did not divide'),
          '50 / 500 = 0.10 dollars per label. The 100 labels used this month cost 100 x 0.10 = 10 dollars; the other 400 stay in stock.',
          calc=lambda: 50 / 500 == 0.1 and 100 * 0.1 == 10),
        Q('Ingredient prices rose 10 percent, raising cost per item from 2.00 to 2.20 dollars. Price stays 3.00 dollars. What '
          'is the new contribution per item?', '0.80 dollars', ('1.00 dollar', 'old contribution'), ('0.20 dollars', 'the increase'),
          ('2.20 dollars', 'the new cost'), '3.00 - 2.20 = 0.80 dollars.', calc=lambda: round(3.00 - 2.20, 2) == 0.80),
        Q('A seller computes cost per item but forgets shipping supplies used on every order. What happens?',
          'The price may look profitable when it is not', ('Nothing changes', 'costs are missing'),
          ('Costs are overestimated by the seller', 'underestimated'), ('Taxes disappear', 'no'), 'Missing costs inflate apparent margin.'),
        Q('Which statement is accurate?', 'Cost per item should be rechecked when supplier prices or waste change.',
          ('Cost per item is calculated once at the start and never changes after that.', 'it can change'), ('Only fixed costs matter for price.', 'unit cost matters'),
          ('Waste never affects cost.', 'it does'), 'Recalculate when inputs change.'),
    ]))

# ------------------------------------------------------------------ Set 47: revenue, profit and cash
RPC = ('Three words get mixed up. REVENUE (sales) is all the money earned from customers before costs. PROFIT is revenue '
       'minus all expenses for the same period. CASH is the money actually in the bank right now. They can differ: a '
       'business can have revenue but no profit if costs are high; it can show a profit but little cash if customers '
       'have not paid yet or if money went into inventory. Watching all three tells the real story.')

s47 = SET('ENT.CASH.01',
    M=sec('Distinguish revenue, profit and cash', RPC, [
        Q('What is revenue?', 'Money earned from customers before costs',
          ('Money left after paying every expense', 'that is profit'),
          ('Money sitting in the bank right now', 'that is cash'),
          ('Money borrowed from a bank loan', 'not earned'), 'Revenue is total sales.'),
        Q('Revenue is 4,000 dollars and expenses are 3,100 dollars. What is the profit?', '900 dollars',
          ('7,100 dollars', 'added'), ('4,000 dollars', 'revenue'), ('3,100 dollars', 'expenses'),
          '4,000 - 3,100 = 900 dollars.', calc=lambda: 4000 - 3100 == 900),
        Q('How can a business show a profit but have little cash?', 'Customers have not paid their invoices yet',
          ('Profit always equals cash in the bank', 'not always'), ('Revenue is always zero', 'no'),
          ('Expenses are counted twice', 'not the reason'), 'Unpaid invoices and inventory tie up cash.'),
        Q('What is cash?', 'Money actually available in the account', ('All sales ever made', 'revenue'),
          ('Sales minus costs on paper for the month', 'profit'), ('The value of the logo', 'not cash'), 'Cash is what you can spend now.'),
        Q('Revenue is 2,000 dollars and expenses are 2,300 dollars. What is the result?', 'A loss of 300 dollars',
          ('A profit of 300 dollars', 'wrong sign'), ('A profit of 4,300 dollars', 'added'), ('A loss of 2,000 dollars', 'revenue only'),
          '2,000 - 2,300 = -300.', calc=lambda: 2000 - 2300 == -300),
    ]),
    B=[cs('A lemonade stand\'s day', 'A lemonade stand sells 30 cups at 1 dollar: revenue is 30 dollars. Lemons, sugar and '
          'cups cost 18 dollars: profit is 30 - 18 = 12 dollars. But if a neighbor bought 5 cups and promised to pay '
          'tomorrow, the cash box has only 25 dollars from sales today. Revenue is what you sold, profit is what is '
          'left after costs, and cash is what is in the box.', [
        Q('The stand\'s revenue is what?', '30 dollars', ('12 dollars', 'profit'), ('25 dollars', 'cash from sales'),
          ('18 dollars', 'costs'), '30 cups x 1 dollar.', calc=lambda: 30 * 1 == 30),
        Q('The stand\'s profit is what?', '12 dollars', ('30 dollars', 'revenue'), ('18 dollars', 'costs'),
          ('48 dollars', 'added'), '30 - 18 = 12.', calc=lambda: 30 - 18 == 12),
        Q('Why is there only 25 dollars of sales cash?', 'A neighbor will pay tomorrow', ('Lemons were free', 'no'),
          ('Profit for the day was negative', 'no'), ('Cups were stolen', 'not stated'), 'An unpaid sale is not yet cash.'),
        Q('"What is in the box" means which word?', 'Cash', ('Revenue', 'sold'), ('Profit', 'after costs'),
          ('Expenses', 'costs'), 'Cash is what you hold.'),
        Q('"What is left after costs" means which word?', 'Profit', ('Revenue', 'before costs'), ('Cash', 'in the box'),
          ('Sales', 'revenue'), 'Profit is after costs.'),
    ], why='A learner who misses MAIN may blur the three words; a lemonade stand shows each one with small numbers.')],
    F1=sec('Apply it: read a month\'s results', RPC, [
        Q('A photographer did and billed 5,000 dollars of work in May. May expenses were 2,200 dollars. Clients have paid 3,500 dollars so far. Using accrual accounting (income counted when earned), what is the May profit?',
          '2,800 dollars',
          ('1,300 dollars', 'used cash received'), ('5,000 dollars', 'revenue'),
          ('3,500 dollars', 'cash received'),
          '5,000 - 2,200 = 2,800 dollars.',
          calc=lambda: 5000 - 2200 == 2800),
        Q('The photographer collected 3,500 dollars from clients and paid 2,200 dollars of expenses in May. What is cash received minus expenses paid?',
          '1,300 dollars',
          ('2,800 dollars', 'profit'), ('5,700 dollars', 'added'),
          ('1,500 dollars', 'unpaid invoices'),
          '3,500 - 2,200 = 1,300 dollars.',
          calc=lambda: 3500 - 2200 == 1300),
        Q('A shop spends 3,000 dollars on inventory it will sell next month. This month\'s cash drops. What happened to the money?',
          'It turned into goods waiting to be sold', ('It became profit for the month right away', 'not yet sold'), ('It disappeared', 'it became inventory'),
          ('It was paid as taxes', 'not stated'), 'Inventory ties up cash.'),
        Q('Which month shows revenue but a loss?', 'Revenue 1,800, expenses 2,100', ('Revenue 1,800, expenses 1,200', 'profit'),
          ('Revenue 0, expenses 0', 'no revenue'), ('Revenue 2,500, expenses 2,000', 'profit'), '1,800 - 2,100 = -300.',
          calc=lambda: 1800 - 2100 < 0),
        Q('An owner says "We sold 10,000 dollars, so we have 10,000 dollars." What is wrong?', 'Sales are not cash or profit',
          ('Nothing; revenue always equals cash', 'not true'), ('Sales should be doubled', 'no'), ('Revenue is a cost', 'no'),
          'Costs and timing differ.'),
    ]),
    F2=sec('Handle the complications: growth that runs out of cash', RPC, [
        Q('Sales are rising fast, but the owner must buy materials 60 days before customers pay. What risk grows?',
          'Running out of cash despite profits', ('Too much cash piling up in the bank', 'opposite'), ('Revenue falling to zero', 'not implied'),
          ('Taxes vanishing', 'no'), 'Fast growth can drain cash.'),
        Q('A business is profitable on paper but cannot pay rent this week. Which action helps soonest?', 'Collect overdue invoices',
          ('Buy more inventory today', 'uses more cash'), ('Lower all prices', 'not immediate'), ('Ignore the rent notice', 'harmful'),
          'Collecting payments brings cash in.'),
        Q('A business made 12,000 dollars of profit this year, all received in cash. The owner took 9,000 dollars in draws and paid 4,000 dollars in cash for equipment. With no other adjustments, how did cash change?',
          'Down 1,000 dollars',
          ('Up 12,000 dollars', 'ignored uses'), ('Up 3,000 dollars', 'ignored equipment'),
          ('Down 13,000 dollars', 'ignored profit'),
          '12,000 - 9,000 - 4,000 = -1,000.',
          calc=lambda: 12000 - 9000 - 4000 == -1000),
        Q('Which number should an owner check before promising to pay a supplier on Friday?', 'Cash expected by Friday',
          ('Total revenue for the year', 'not timing'), ('Profit last year', 'not timing'), ('Number of followers', 'irrelevant'),
          'Bills are paid with cash.'),
        Q('Which statement is accurate?', 'A business needs profit over time and cash at every moment.',
          ('Profit and cash are always identical.', 'not true'), ('Revenue is the only number that matters.', 'not true'),
          ('Cash never matters for businesses that are profitable on paper.', 'not true'), 'Track both.'),
    ]))

# ------------------------------------------------------------------ Set 48: markup and margin
MARK = (('MARKUP and MARGIN both describe the gap between cost and price, but they use different bases. MARKUP is the '
        'gap as a percent of COST: (price - cost) / cost. MARGIN is the gap as a percent of PRICE: (price - cost) / '
        'price. Example: cost 6 dollars, price 10 dollars. The gap is 4. Markup = 4 / 6, about 67 percent. Margin = 4'
        ' / 10 = 40 percent. For an item with a positive cost sold above cost, the markup percentage is greater than '
        'the margin percentage. Mixing them up can lead to prices that are too low.'))

s48 = SET('ENT.PRICE.02',
    M=sec('Compute markup and margin and tell them apart', MARK, [
        Q('Cost 5 dollars, price 8 dollars. What is the markup?', '60 percent', ('37.5 percent', 'that is margin'),
          ('3 percent', 'the dollar gap'), ('160 percent', 'price over cost'), '3 / 5 = 0.60.', calc=lambda: (8 - 5) / 5 == 0.6),
        Q('Cost 5 dollars, price 8 dollars. What is the margin?', '37.5 percent', ('60 percent', 'that is markup'),
          ('3 percent', 'the dollar gap'), ('62.5 percent', 'cost over price'), '3 / 8 = 0.375.', calc=lambda: (8 - 5) / 8 == 0.375),
        Q('Markup uses which base?', 'The cost', ('The price', 'that is margin'), ('The number sold', 'not the base'),
          ('The tax rate', 'not the base'), 'Markup divides by cost.'),
        Q('For an item with a positive cost sold above cost, which percentage is larger?',
          'Markup',
          ('Margin', 'smaller base wins'), ('They are always equal', 'not equal'),
          ('It depends on the tax rate', 'not related'),
          'Dividing by the smaller cost gives a larger percent.'),
        Q('Cost 20 dollars, a 50 percent markup. What is the price?', '30 dollars', ('40 dollars', '100 percent markup'),
          ('25 dollars', '25 percent markup'), ('10 dollars', 'the markup alone'), '20 x 1.50 = 30.', calc=lambda: 20 * 1.5 == 30),
    ]),
    B=[mathb('Writing a part as a percent of a whole', 'To find what percent one number is of another, divide the part by '
             'the whole and multiply by 100. Example: 3 out of 12 is 3 / 12 = 0.25 = 25 percent. The number you divide '
             'BY is the base. Changing the base changes the answer: 3 / 4 = 75 percent, but 3 / 12 = 25 percent. Always '
             'ask, "percent OF what?"', [
        Q('What percent is 2 of 8?', '25 percent', ('4 percent', 'divided 8 by 2'), ('400 percent', 'reversed'),
          ('2 percent', 'not divided'), '2 / 8 = 0.25.', calc=lambda: 2 / 8 == 0.25),
        Q('What percent is 6 of 10?', '60 percent', ('6 percent', 'not converted'), ('16 percent', 'added'),
          ('167 percent', 'reversed'), '6 / 10 = 0.60.', calc=lambda: 6 / 10 == 0.6),
        Q('In "3 is what percent of 12?", which number is the base?', '12', ('3', 'the part'), ('15', 'added'),
          ('100', 'not the base'), 'The base is "of what."'),
        Q('What percent is 5 of 20?', '25 percent', ('4 percent', 'reversed'), ('5 percent', 'not divided'),
          ('20 percent', 'not divided'), '5 / 20 = 0.25.', calc=lambda: 5 / 20 == 0.25),
        Q('Why do 3 / 4 and 3 / 12 give different percents?', 'The base is different', ('The part is different', 'same part'),
          ('One is wrong', 'both correct'), ('Percents are random', 'no'), 'Different bases give different percents.'),
    ], why='A learner who misses MAIN may not see why the base matters; this practices part-over-whole percents.'),
       cs('Markup looks back at cost; margin looks at the price tag', 'Picture a price tag of 10 dollars on an item that cost '
          '6 dollars. Markup asks, "How much did I add compared with what I paid?" (4 compared with 6). Margin asks, '
          '"How much of the price tag do I keep?" (4 out of 10). Same 4 dollars, different comparison. Remember: '
          'Markup looks at what you paid; Margin looks at the price tag.', [
        Q('Markup compares the gap with what?', 'What you paid', ('The price tag', 'margin'), ('The customer', 'no'),
          ('The tax', 'no'), 'Markup uses cost.'),
        Q('Margin compares the gap with what?', 'The price tag', ('What you paid', 'markup'), ('The weather', 'no'),
          ('The rent', 'no'), 'Margin uses price.'),
        Q('In the example, what is the dollar gap?', '4 dollars', ('6 dollars', 'cost'), ('10 dollars', 'price'),
          ('16 dollars', 'added'), '10 - 6 = 4.', calc=lambda: 10 - 6 == 4),
        Q('"How much of the price tag do I keep?" is which idea?', 'Margin', ('Markup', 'uses cost'), ('Revenue', 'total sales'),
          ('Cash', 'money on hand'), 'Margin is the share of price kept.'),
        Q('Does the dollar gap change between markup and margin?', 'No, only the comparison changes', ('Yes, it doubles', 'no'),
          ('Yes, it halves', 'no'), ('Yes, it becomes zero for margin', 'no'), 'The base changes, not the gap.'),
    ], why='A learner who knows percents but still mixes the terms needs the meaning of each base explained in words.')],
    F1=sec('Apply it: price with a target markup or margin', MARK, [
        Q('A reseller buys mugs for 8 dollars and wants a 40 percent margin. What price works, to the nearest cent?', '13.33 dollars',
          ('11.20 dollars', 'used 40 percent markup'), ('12.00 dollars', 'added 4'), ('3.20 dollars', 'the markup'),
          'Price = cost / (1 - 0.40) = 8 / 0.60 = 13.33.', calc=lambda: round(8 / 0.60, 2) == 13.33),
        Q('An owner adds a 40 percent markup to a cost of 8 dollars, thinking it gives a 40 percent margin. What margin '
          'does she actually get, to one decimal place?', '28.6 percent', ('40 percent', 'the mistake'), ('11.2 percent', 'price as percent'),
          ('60 percent', 'one minus 40'), 'Price 11.20; gap 3.20; 3.20 / 11.20 = 0.286.',
          calc=lambda: round((8 * 1.4 - 8) / (8 * 1.4), 3) == 0.286),
        Q('Cost 12 dollars, price 20 dollars. What is the margin?', '40 percent', ('67 percent', 'markup'),
          ('8 percent', 'the dollar gap'), ('60 percent', 'cost over price'), '8 / 20 = 0.40.', calc=lambda: (20 - 12) / 20 == 0.4),
        Q('A supplier says "Industry margin is 50 percent." Item cost is 15 dollars. What price gives a 50 percent margin?',
          '30 dollars', ('22.50 dollars', '50 percent markup'), ('15 dollars', 'no margin'), ('7.50 dollars', 'half of cost'),
          '15 / 0.50 = 30.', calc=lambda: 15 / 0.5 == 30),
        Q('Which statement is correct for cost 6, price 10?', 'Markup is about 67 percent and margin is 40 percent',
          ('Markup is 40 percent and margin is about 67 percent', 'reversed'), ('Both are 40 percent', 'not equal'),
          ('Both are 4 percent', 'dollars, not percent'), 'Markup 4/6; margin 4/10.',
          calc=lambda: round(4 / 6, 2) == 0.67 and 4 / 10 == 0.4),
    ]),
    F2=sec('Handle the complications: discounts, fees and mixed terms', MARK, [
        Q('An item costs 10 dollars and sells for 20 dollars (50 percent margin). A 20 percent discount is offered. What is '
          'the new margin?', '37.5 percent', ('30 percent', 'subtracted 20 points'), ('50 percent', 'ignored discount'),
          ('20 percent', 'the discount'), 'New price 16; gap 6; 6 / 16 = 0.375.', calc=lambda: (20 * 0.8 - 10) / (20 * 0.8) == 0.375),
        Q('A payment fee takes 3 percent of a 50-dollar price. Item cost is 30 dollars. What is the margin after the fee?',
          '37 percent', ('40 percent', 'ignored fee'), ('43 percent', 'added the fee'), ('3 percent', 'only the fee'),
          'Gap = 50 - 30 - 1.50 = 18.50; 18.50 / 50 = 0.37.', calc=lambda: round((50 - 30 - 0.03 * 50) / 50, 2) == 0.37),
        Q('A business partner says "our markup is 25 percent" but means margin. Why does it matter?', 'Prices set from the wrong term can be too low',
          ('It never matters which word is used', 'it changes price'), ('Markup and margin are legally identical', 'not the issue'),
          ('Margin is only for taxes', 'not true'), 'Confirm which base is meant.'),
        Q('Which mistake leads to a lower price than intended?', 'Using a markup percent when a margin percent was intended',
          ('Using a margin percent when a margin percent was intended', 'correct'), ('Writing down the cost carefully', 'helpful'),
          ('Including packaging in cost', 'helpful'), 'Markup of the same percent gives a lower price.'),
        Q('Which statement is accurate?', 'Always state whether a percent is markup or margin.',
          ('Markup and margin always give the same price.', 'not true'), ('Only margin is ever used in business.', 'both used'),
          ('Percents never need a base.', 'they do'), 'Clarity prevents pricing errors.'),
    ]))

# ------------------------------------------------------------------ Set 49: break-even
BE = ('The BREAK-EVEN point is the number of sales at which total revenue equals total cost, so profit is zero. Each sale '
      'contributes (price - variable cost per item) toward fixed costs. Break-even units = fixed costs / (price - '
      'variable cost). Example (assumptions): fixed costs 600 dollars a month, price 15 dollars, variable cost 5 dollars: '
      '600 / 10 = 60 sales. Sales above break-even create profit; sales below create a loss. Write down the assumptions; '
      'if any change, recalculate. Round UP, because you cannot sell part of an item.')

s49 = SET('ENT.PRICE.03',
    M=sec('Calculate break-even from stated assumptions', BE, [
        Q('Fixed costs 800 dollars, price 20 dollars, variable cost 10 dollars. What is break-even?', '80 sales',
          ('40 sales', 'divided by price'), ('27 sales', 'divided by price plus cost'), ('8,000 sales', 'multiplied'),
          '800 / (20 - 10) = 80.', calc=lambda: 800 / (20 - 10) == 80),
        Q('What is profit exactly at break-even?', 'Zero', ('Equal to fixed costs', 'covered, not profit'),
          ('Equal to revenue', 'costs are subtracted'), ('Negative', 'that is below break-even'), 'Revenue equals cost.'),
        Q('What does each sale contribute toward fixed costs?', 'Price minus variable cost', ('Price plus variable cost', 'wrong sign'),
          ('Fixed cost divided by price', 'not contribution'), ('The whole price', 'ignores variable cost'),
          'Contribution = price - variable cost.'),
        Q('Fixed costs 500 dollars, contribution 3 dollars per sale. What is break-even, rounded up?', '167 sales',
          ('166 sales', 'rounded down'), ('1,500 sales', 'multiplied'), ('503 sales', 'added'),
          '500 / 3 = 166.67, rounded up to 167.', calc=lambda: math.ceil(500 / 3) == 167),
        Q('If the price drops and costs stay the same, what happens to break-even?', 'It rises', ('It falls', 'smaller contribution'),
          ('It stays the same', 'contribution changed'), ('It becomes zero', 'no'), 'Less contribution means more sales needed.'),
    ]),
    B=[mathb('Dividing and rounding up', 'Break-even is a division: fixed costs divided by contribution per sale. If the '
             'answer is not a whole number, round UP to the next whole number, because a partial sale is not possible '
             'and rounding down would leave you short. Example: 250 / 6 = 41.67, so 42 sales. Check: 42 x 6 = 252, which '
             'covers 250; 41 x 6 = 246, which does not.', [
        Q('What is 300 / 7, rounded up?', '43', ('42', 'rounded down'), ('44', 'too high'), ('2,100', 'multiplied'),
          '300 / 7 = 42.86, up to 43.', calc=lambda: math.ceil(300 / 7) == 43),
        Q('Why round break-even UP?', 'Rounding down leaves costs uncovered', ('Rounding up always gives the wrong answer', 'no'),
          ('Partial sales are common', 'not possible'), ('Rounding does not matter', 'it does'), 'Round up to cover costs.'),
        Q('What is 400 / 8?', '50', ('32', 'subtracted'), ('3,200', 'multiplied'), ('408', 'added'), '400 / 8 = 50.',
          calc=lambda: 400 / 8 == 50),
        Q('Does 41 x 6 cover 250?', 'No, it is 246', ('Yes, it is 256', 'miscalculated'), ('Yes, it is 250', 'miscalculated'),
          ('No, it is 206', 'miscalculated'), '41 x 6 = 246 < 250.', calc=lambda: 41 * 6 == 246),
        Q('What is 1,000 / 9, rounded up?', '112', ('111', 'rounded down'), ('110', 'too low'), ('9,000', 'multiplied'),
          '1,000 / 9 = 111.1, up to 112.', calc=lambda: math.ceil(1000 / 9) == 112),
    ], why='A learner who misses MAIN may divide correctly but round the wrong way; this practices division with rounding up.')],
    F1=sec('Apply it: test a plan with break-even', BE, [
        Q('A food truck has fixed costs of 2,400 dollars a month. Each meal sells for 12 dollars and costs 4 dollars to make. '
          'How many meals per month to break even?', '300 meals', ('200 meals', 'divided by price'), ('600 meals', 'divided by cost'),
          ('150 meals', 'divided by 16'), '2,400 / 8 = 300.', calc=lambda: 2400 / (12 - 4) == 300),
        Q('A food truck needs 300 meals a month to break even (2,400 dollars of fixed costs, a 12-dollar price, a 4-dollar cost per meal). It is open 25 days a month. About how many meals per day does it need to break even?',
          '12 meals',
          ('8 meals', 'used price'), ('25 meals', 'used days'),
          ('300 meals', 'per month'),
          '300 / 25 = 12.',
          calc=lambda: 300 / 25 == 12),
        Q('The food truck must sell 12 meals a day for 25 days to break even (2,400 dollars of fixed costs, 12-dollar price, 4-dollar cost per meal). The owner expects 9 meals a day. What does that mean?',
          'The plan loses money unless something changes',
          ('The plan makes a large profit', 'below break-even'), ('Break-even does not matter', 'it does'),
          ('Costs will fall automatically as the truck gets busier', 'not stated'),
          '9 x 25 = 225 meals; 225 x 8 = 1,800 dollars of contribution against 2,400 of fixed costs, a 600-dollar loss.',
          calc=lambda: 9 * 25 == 225 and 225 * 8 - 2400 == -600),
        Q('The food truck has 2,400 dollars of fixed costs a month and a 4-dollar cost per meal. If it raises its price from 12 to 14 dollars, what is the new break-even per month?',
          '240 meals',
          ('300 meals', 'old price'), ('172 meals', 'divided by price'),
          ('400 meals', 'subtracted wrong'),
          '2,400 / (14 - 4) = 240.',
          calc=lambda: 2400 / (14 - 4) == 240),
        Q("Which assumption should be written down with the food truck's break-even (2,400 dollars of fixed costs, 12-dollar price, 4-dollar cost per meal)?",
          'Meal cost stays 4 dollars',
          ('The logo stays the same', 'irrelevant'), ('The truck color', 'irrelevant'),
          ("The owner's favorite meal", 'irrelevant'),
          'Costs and prices drive the result.'),
    ]),
    F2=sec('Handle the complications: changing assumptions', BE, [
        Q('A studio\'s break-even was 50 classes using a 30-dollar price and 10-dollar cost (1,000 dollars fixed). Rent rises '
          'by 200 dollars. What is the new break-even?', '60 classes', ('50 classes', 'old'), ('70 classes', 'added 20'),
          ('40 classes', 'subtracted'), '1,200 / 20 = 60.', calc=lambda: 1200 / (30 - 10) == 60),
        Q('A seller forgot payment fees of 1 dollar per sale. Price 15, variable cost 5, fixed 600. What is the corrected '
          'break-even, rounded up?', '67 sales', ('60 sales', 'ignored fee'), ('55 sales', 'added fee to price'),
          ('40 sales', 'divided by price'), '600 / (15 - 5 - 1) = 66.7, up to 67.', calc=lambda: math.ceil(600 / 9) == 67),
        Q('Break-even is 200 units, but the market research suggests only about 120 buyers. What is the best response?',
          'Rethink price, costs or the plan before launching', ('Launch anyway and hope that more buyers appear later', 'risky'), ('Ignore the research', 'risky'),
          ('Double the fixed costs', 'worse'), 'A gap signals the plan needs work.'),
        Q('Variable cost is 0 dollars for a digital download. Fixed costs are 900 dollars and price is 15 dollars. What is '
          'break-even?', '60 sales', ('0 sales', 'fixed costs remain'), ('900 sales', 'used 1 dollar'), ('13,500 sales', 'multiplied'),
          '900 / 15 = 60.', calc=lambda: 900 / (15 - 0) == 60),
        Q('Which statement is accurate?', 'Break-even is only as good as its assumptions.',
          ('Break-even guarantees the business will succeed.', 'no'), ('Break-even never changes once found.', 'it can'),
          ('Break-even ignores fixed costs.', 'it uses them'), 'Recalculate when assumptions change.'),
    ]))

SETS = [s43, s44, s45, s46, s47, s48, s49]
