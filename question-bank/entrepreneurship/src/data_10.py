"""Entrepreneurship sets 50-56: Foundation 7 (continued), fees, discounts, capacity, cash timing; HP case.
All prices, fees and rates are hypothetical assumptions for practice, not quotes from any provider."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 50: payment-processing fees
FEE = ('When customers pay by card or app, the payment processor keeps a fee. A common structure is a percentage of the '
       'sale plus a fixed amount per transaction, for example (an assumption, not a real quote) 2.9 percent + 0.30 '
       'dollars. On a 40-dollar sale that is 0.029 x 40 + 0.30 = 1.46 dollars, so the business receives 38.54 dollars. '
       'The fixed part hurts small sales most: on a 3-dollar sale, 0.30 dollars alone is 10 percent. Include fees in '
       'cost per sale when setting prices.')

s50 = SET('ENT.PRICE.04',
    M=sec('Calculate processing fees and include them in pricing', FEE, [
        Q('Using 2.9 percent + 0.30 dollars, what is the fee on a 100-dollar sale?', '3.20 dollars',
          ('2.90 dollars', 'left out the fixed part'), ('3.00 dollars', 'used 3 percent'), ('0.30 dollars', 'fixed part only'),
          '0.029 x 100 + 0.30 = 3.20.', calc=lambda: round(0.029 * 100 + 0.30, 2) == 3.20),
        Q('Using the same fee, how much does the business receive from a 100-dollar sale?', '96.80 dollars',
          ('97.10 dollars', 'left out the fixed part'), ('100.00 dollars', 'ignored the fee'), ('99.70 dollars', 'fixed part only'),
          '100 - 3.20 = 96.80.', calc=lambda: round(100 - 3.20, 2) == 96.80),
        Q('Why does the fixed part hurt small sales most?', 'It is a larger share of a small price',
          ('It is charged only on large sales', 'it applies to every sale'),
          ('Small sales have no percentage fee', 'they do'),
          ('Processors waive fees on large sales', 'not stated'), 'A fixed amount is a bigger percent of a small sale.'),
        Q('On a 3-dollar sale, what percent of the price is the 0.30-dollar fixed part?', '10 percent',
          ('3 percent', 'used the percentage rate'), ('30 percent', 'used cents as percent'), ('1 percent', 'moved decimal'),
          '0.30 / 3 = 0.10.', calc=lambda: round(0.30 / 3, 2) == 0.10),
        Q('Where should processing fees appear when setting prices?', 'In the cost of each sale',
          ('Nowhere, because customers pay them separately', 'the business pays'),
          ('Only in the yearly tax return', 'they affect each sale'),
          ('Only in the owner\'s personal budget', 'business cost'), 'Fees reduce what each sale brings in.'),
    ]),
    B=[mathb('Percent of an amount plus a fixed amount', 'Many fees follow "rate x amount + fixed." Change the percent to a '
             'decimal, multiply by the amount, then add the fixed part. Example: 3 percent of 50 plus 0.25: 0.03 x 50 = '
             '1.50, then 1.50 + 0.25 = 1.75. A common mistake is forgetting the fixed part or using 3 instead of 0.03. '
             'Check: the fee should be much smaller than the sale.', [
        Q('What is 0.03 x 50 + 0.25?', '1.75', ('1.50', 'forgot fixed part'), ('150.25', 'used 3 not 0.03'),
          ('0.28', 'added rates'), '1.50 + 0.25 = 1.75.', calc=lambda: round(0.03 * 50 + 0.25, 2) == 1.75),
        Q('2 percent as a decimal is what?', '0.02', ('0.2', 'one place'), ('2.0', 'not converted'), ('0.002', 'three places'),
          '2 / 100 = 0.02.'),
        Q('What is 0.02 x 80 + 0.10?', '1.70', ('1.60', 'forgot fixed part'), ('160.10', 'used 2'), ('0.12', 'added rates'),
          '1.60 + 0.10 = 1.70.', calc=lambda: round(0.02 * 80 + 0.10, 2) == 1.70),
        Q('A fee of 25 dollars on a 20-dollar sale suggests what?', 'The percent was not converted to a decimal',
          ('The fee is correct', 'too large'), ('The sale was 2,000 dollars', 'no'), ('The fixed part of the fee was forgotten entirely', 'opposite'),
          'Check that fees are small compared with the sale.'),
        Q('What is 0.04 x 25 + 0.50?', '1.50', ('1.00', 'forgot fixed part'), ('100.50', 'used 4'), ('0.54', 'added rates'),
          '1.00 + 0.50 = 1.50.', calc=lambda: round(0.04 * 25 + 0.50, 2) == 1.50),
    ], why='A learner who misses MAIN may mis-handle the percent-plus-fixed formula; this practices it step by step.')],
    F1=sec('Apply it: price with fees included', FEE, [
        Q('A seller\'s cost per item is 12 dollars and she charges 20 dollars. Fee is 2.9 percent + 0.30 dollars. What does '
          'each sale contribute after the fee?', '7.12 dollars', ('8.00 dollars', 'ignored the fee'), ('7.42 dollars', 'left out 0.30'),
          ('7.70 dollars', 'only 0.30'), 'Fee 0.88; 20 - 12 - 0.88 = 7.12.', calc=lambda: round(20 - 12 - (0.029 * 20 + 0.30), 2) == 7.12),
        Q('A café sells 2-dollar cookies by card. Same fee. What is the fee per cookie?', '0.36 dollars',
          ('0.06 dollars', 'left out fixed part'), ('0.30 dollars', 'only the fixed part'), ('0.58 dollars', 'used 29 percent'),
          '0.058 + 0.30 = 0.358, about 0.36.', calc=lambda: round(0.029 * 2 + 0.30, 2) == 0.36),
        Q('To reduce the fee share on small items, which option fits?', 'Encourage bundles, like 3 cookies for one payment',
          ('Raise the fixed fee by choosing a new processor', 'worse'), ('Split every sale into smaller payments', 'worse'),
          ('Hide the fee from her records', 'inaccurate'), 'One payment for several items shares the fixed part.'),
        Q('Monthly card sales are 4,000 dollars over 200 sales. Same fee. What are total fees?', '176 dollars',
          ('116 dollars', 'left out fixed parts'), ('60 dollars', 'fixed parts only'), ('1,160 dollars', 'used 29 percent'),
          '0.029 x 4,000 + 0.30 x 200 = 116 + 60 = 176.', calc=lambda: round(0.029 * 4000 + 0.30 * 200, 2) == 176),
        Q('Processor A: 2.6 percent + 0.10 dollars. Processor B: 2.9 percent + 0.30 dollars. Which is cheaper for a 20-dollar sale?',
          'A, at 0.62 dollars', ('B, at 0.88 dollars', 'B is higher'), ('They cost the same', 'they differ'),
          ('A, at 0.52 dollars', 'left out fixed part'), 'A: 0.52 + 0.10 = 0.62; B: 0.58 + 0.30 = 0.88.',
          calc=lambda: round(0.026 * 20 + 0.10, 2) == 0.62 and round(0.029 * 20 + 0.30, 2) == 0.88),
    ]),
    F2=sec('Handle the complications: extra fees and surcharges', FEE, [
        Q('A processor also charges 15 dollars a month. A seller has 30 sales a month. How much does this add per sale?',
          '0.50 dollars', ('15.00 dollars', 'not divided'), ('2.00 dollars', 'divided 30 by 15'), ('0.15 dollars', 'moved decimal'),
          '15 / 30 = 0.50.', calc=lambda: 15 / 30 == 0.5),
        Q('An owner wants to add a card surcharge to customers. What should she check first?', 'Laws and processor rules on surcharges',
          ('Whether her competitors like the idea', 'not the rule'), ('Only whether customers will notice', 'not the rule'),
          ('Nothing; surcharges are always allowed', 'rules vary'), 'Surcharge rules vary by place and processor.'),
        Q('An invoice of 1,000 dollars is paid by card at 2.9 percent + 0.30. What is received?', '970.70 dollars',
          ('971.00 dollars', 'left out 0.30'), ('1,000.00 dollars', 'ignored fee'), ('999.70 dollars', 'only 0.30'),
          '1,000 - 29.30 = 970.70.', calc=lambda: round(1000 - (0.029 * 1000 + 0.30), 2) == 970.70),
        Q('A seller compares processors only on the percentage. What might she miss?', 'Fixed and monthly fees',
          ('Her own logo colors', 'irrelevant'), ('Her customers\' names', 'irrelevant'), ('The weather', 'irrelevant'),
          'All parts of the fee matter.'),
        Q('Which statement is accurate?', 'Fees vary by provider and plan, so read current terms.',
          ('Every payment processor charges exactly 2.9 percent plus 0.30 dollars.', 'example only'), ('Fees never change.', 'they can'),
          ('Fees only apply to large businesses.', 'not true'), 'The rates in this course are assumptions.'),
    ]))

# ------------------------------------------------------------------ Set 51: refunds and discounts
DISC = ('Discounts and refunds reduce what a sale brings in, often more than people expect. A 20 percent discount on a '
        '25-dollar item with a 15-dollar cost cuts the contribution from 10 dollars to 5 dollars: half the money from '
        'that sale. A REFUND gives money back; the item may come back damaged or not at all, and some processors do not '
        'return their fee. Write a clear refund policy (time limit, condition of returns, who pays shipping) and post it '
        'before customers buy.')

s51 = SET('ENT.PRICE.05',
    M=sec('Calculate how discounts and refunds change contribution and write a policy', DISC, [
        Q('A 25-dollar item costs 15 dollars. With a 20 percent discount, what is the new price?', '20 dollars',
          ('5 dollars', 'only the discount'), ('24.80 dollars', 'subtracted 0.20'), ('30 dollars', 'added'),
          '25 x 0.80 = 20.', calc=lambda: 25 * 0.8 == 20),
        Q('Same item. What is the contribution after the discount?', '5 dollars', ('10 dollars', 'before discount'),
          ('20 dollars', 'the price'), ('15 dollars', 'the cost'), '20 - 15 = 5.', calc=lambda: 25 * 0.8 - 15 == 5),
        Q('What should a refund policy state?', 'The time limit, return condition and who pays shipping',
          ('Only the owner\'s favorite products', 'not policy terms'), ('Only the store\'s opening date', 'not policy terms'),
          ('Nothing at all, because written policies only confuse customers', 'clear policies help'), 'Clear terms prevent disputes.'),
        Q('When should a refund policy be shown?', 'Before customers buy', ('Only after a complaint', 'too late'),
          ('Only once a year in an email', 'not reliable'), ('Never', 'customers need it'), 'Posting it first sets expectations.'),
        Q('A 10-dollar discount on an item with a 12-dollar contribution leaves what contribution?', '2 dollars',
          ('22 dollars', 'added'), ('10 dollars', 'the discount'), ('12 dollars', 'ignored discount'), '12 - 10 = 2.',
          calc=lambda: 12 - 10 == 2),
    ]),
    B=[mathb('Applying a percent decrease', 'To take a percent off, multiply by (1 - the decimal). 20 percent off means '
             'multiply by 0.80; 15 percent off means multiply by 0.85. Example: 40 dollars with 25 percent off: 40 x 0.75 '
             '= 30 dollars. Or find the discount first: 0.25 x 40 = 10, then 40 - 10 = 30. Both ways give the same '
             'answer.', [
        Q('What is 50 with 20 percent off?', '40', ('30', 'took 20 off'), ('10', 'only the discount'), ('49.80', 'subtracted 0.20'),
          '50 x 0.80 = 40.', calc=lambda: 50 * 0.8 == 40),
        Q('15 percent off means multiply by what?', '0.85', ('0.15', 'that is the discount'), ('1.15', 'that is an increase'),
          ('85', 'not a decimal'), '1 - 0.15 = 0.85.'),
        Q('What is 60 with 25 percent off?', '45', ('15', 'only the discount'), ('35', 'took 25 off'), ('75', 'added'),
          '60 x 0.75 = 45.', calc=lambda: 60 * 0.75 == 45),
        Q('What is 10 percent of 30?', '3', ('0.3', 'moved too far'), ('27', 'subtracted'), ('300', 'multiplied by 10'),
          '0.10 x 30 = 3.', calc=lambda: round(0.10 * 30, 2) == 3),
        Q('What is 80 with 10 percent off?', '72', ('70', 'took 10 off'), ('8', 'only the discount'), ('88', 'added'),
          '80 x 0.90 = 72.', calc=lambda: round(80 * 0.9, 2) == 72),
    ], why='A learner who misses MAIN may not compute a percent decrease; this practices it two ways.')],
    F1=sec('Apply it: evaluate a sale or refund', DISC, [
        Q('A shop sells 100 shirts a month at 30 dollars with a 18-dollar cost. A 25 percent sale is planned. How many shirts '
          'must sell during the sale to earn the same total contribution, rounded up?', '267 shirts', ('100 shirts', 'ignored discount'),
          ('125 shirts', 'added 25 percent'), ('200 shirts', 'guessed double'),
          'Old: 100 x 12 = 1,200. New price 22.50; contribution 4.50; 1,200 / 4.50 = 266.7, up to 267.',
          calc=lambda: 30 * 0.75 == 22.5 and math.ceil(100 * (30 - 18) / (22.5 - 18)) == 267),
        Q('A customer returns a 50-dollar item for a full refund. The processor kept a 1.75-dollar fee and does not return it. '
          'The item can be resold. What did the return cost the business?', '1.75 dollars', ('50 dollars', 'item resold'),
          ('0 dollars', 'fee kept'), ('51.75 dollars', 'item resold'), 'Only the kept fee is lost.'),
        Q('A returned item arrives damaged and cannot be resold. Its cost was 18 dollars. The refund was 30 dollars. What is '
          'the loss compared with no sale?', '18 dollars', ('30 dollars', 'the refund was money received first'),
          ('12 dollars', 'the contribution'), ('48 dollars', 'added'), 'The money returned evens out; the item cost is lost.'),
        Q('Which refund policy is clearest?', '"Returns within 30 days, unused, buyer pays return shipping."',
          ('"Returns are maybe possible, depending on my mood that week."', 'unclear'), ('"No questions, no answers, contact us someday."', 'unclear'),
          ('"Ask a friend about our return rules."', 'unclear'), 'Specific terms avoid disputes.'),
        Q('A 10 percent discount for first-time buyers brings 40 new customers who keep buying later. Why might it be worth '
          'it?', 'Repeat purchases can outweigh the one-time discount', ('Discounts always increase profit on every single sale', 'not always'),
          ('First-time buyers never return', 'not stated'), ('Discounts remove all costs', 'no'),
          'The value depends on what happens after the discount.'),
    ]),
    F2=sec('Handle the complications: stacking and abuse', DISC, [
        Q('A customer uses a 20 percent coupon on top of a 20 percent sale. What total discount does she get on a 50-dollar '
          'item, applied one after the other?', '36 percent', ('40 percent', 'added'), ('20 percent', 'only one'),
          ('4 percent', 'multiplied percents'), '50 x 0.8 x 0.8 = 32; 18 / 50 = 0.36.', calc=lambda: round(1 - 0.8 * 0.8, 2) == 0.36),
        Q('Many customers return items after wearing them once. What should the owner change?', 'Add a clear "unused" condition to the policy',
          ('Accept every return forever, in any condition', 'continues losses'), ('Stop selling online', 'too extreme'),
          ('Accuse customers publicly', 'harmful'), 'Clear conditions limit abuse.'),
        Q('A store says "all sales final" but the law where it sells may require some refunds. What should it check?',
          'Local consumer protection rules', ('Only competitors\' policies', 'not the law'), ('Nothing; the store decides alone', 'laws may apply'),
          ('Only its logo', 'irrelevant'), 'Policies must follow applicable law.'),
        Q('A 20-dollar item has a 6-dollar contribution, so its cost is 14 dollars. The owner offers 30 percent off. What is '
          'the contribution per sale now?', '0 dollars', ('6 dollars', 'ignores the discount'), ('12 dollars', 'added'),
          ('14 dollars', 'that is the cost'), '20 x 0.70 = 14; 14 - 14 = 0. Every sale now only covers its cost.',
          calc=lambda: round(20 * 0.70 - 14, 2) == 0),
        Q('Which statement is accurate?', 'Discounts should be checked against contribution before offering them.',
          ('Discounts are always free marketing.', 'they cost money'), ('Refund policies are optional for online stores, so no one needs to post one.', 'needed'),
          ('Bigger discounts always mean more profit.', 'not always'), 'Check the math first.'),
    ]))

# ------------------------------------------------------------------ Set 52: owner time and capacity
CAP = ('An owner\'s time is limited, so it has a cost. CAPACITY is the most work the business can do in a period. If an '
       'owner can work 30 hours a week on paid tasks, that is her capacity. To find an effective HOURLY RATE, divide '
       'profit from a job by the total hours it takes, including travel, emails, invoices and setup, not just the '
       'visible work. A price that looks high can become a low hourly rate. When capacity is full, more customers '
       'cannot be served without raising prices, getting help, or working more.')

s52 = SET('ENT.PRICE.06',
    M=sec('Compute effective hourly rates and recognize capacity limits', CAP, [
        Q('A job earns 120 dollars of profit and takes 4 hours in total. What is the effective hourly rate?', '30 dollars an hour',
          ('480 dollars an hour', 'multiplied'), ('124 dollars an hour', 'added'), ('40 dollars an hour', 'used 3 hours'),
          '120 / 4 = 30.', calc=lambda: 120 / 4 == 30),
        Q('What is capacity?', 'The most work the business can do in a period',
          ('The number of followers on social media', 'not capacity'), ('The size of the logo file', 'not capacity'),
          ('The amount of money in savings', 'not capacity'), 'Capacity is a work limit.'),
        Q('Which hidden time should be counted for a house-cleaning job?', 'Travel and invoicing time',
          ('Time the owner spends on a personal hobby', 'not the job'), ('Time a customer spends at work', 'not her time'),
          ('Time spent sleeping at night', 'not the job'), 'All time the job requires counts.'),
        Q('A job pays 200 dollars of profit for 5 hours of work plus 3 hours of travel and email. What is the true hourly rate?',
          '25 dollars an hour', ('40 dollars an hour', 'ignored hidden time'), ('66.67 dollars an hour', 'used only hidden time'),
          ('1,600 dollars an hour', 'multiplied'), '200 / 8 = 25.', calc=lambda: 200 / (5 + 3) == 25),
        Q('Capacity is full. Which option allows more customers?', 'Get help or raise prices to manage demand',
          ('Take every new job and skip quality checks', 'hurts quality'), ('Ignore all new requests silently', 'loses goodwill'),
          ('Work 20 hours a day indefinitely', 'unsustainable'), 'Options include help, prices or more hours.'),
    ]),
    B=[cs('Seats on a bus', 'A bus has a fixed number of seats. Once they are full, no more people can ride that trip, no '
          'matter how many wait. An owner\'s week is like the bus: it has a fixed number of working hours. Each job takes '
          'some seats, including the "hidden" seats for travel and paperwork. When the hours are full, the choices are a '
          'bigger bus (help), a pricier ticket (higher prices), or more trips (more hours).', [
        Q('A full bus is like what?', 'A full work week', ('A big savings account', 'no'), ('An empty calendar', 'opposite'),
          ('A new logo', 'no'), 'Capacity is limited.'),
        Q('The "hidden seats" are like what?', 'Travel and paperwork time', ('Extra profit', 'no'), ('Customer reviews online', 'no'),
          ('Free time', 'no'), 'Hidden tasks take hours.'),
        Q('A bigger bus is like what choice?', 'Getting help', ('Raising prices', 'pricier ticket'), ('Working more hours', 'more trips'),
          ('Doing nothing', 'no change'), 'Help adds capacity.'),
        Q('A pricier ticket is like what choice?', 'Raising prices', ('Getting help', 'bigger bus'), ('More trips', 'more hours'),
          ('Lowering quality', 'not the picture'), 'Higher prices manage demand.'),
        Q('Can more riders fit once all seats are full?', 'No, not on that trip', ('Yes, always', 'seats are full'),
          ('Only on weekends', 'no'), ('Only if they stand on the roof', 'unsafe'), 'Full means full.'),
    ], why='A learner who misses MAIN may not picture a time limit; a full bus makes capacity concrete.')],
    F1=sec('Apply it: compare jobs by true hourly rate', CAP, [
        Q('Job A: 150 dollars profit, 3 hours total. Job B: 240 dollars profit, 6 hours total. Which pays more per hour?',
          'A, at 50 dollars an hour', ('B, at 40 dollars an hour', 'B is lower'), ('B, at 240 dollars', 'not per hour'),
          ('They pay the same', 'they differ'), 'A: 50; B: 40.', calc=lambda: 150 / 3 == 50 and 240 / 6 == 40),
        Q('A tutor can work 25 hours a week. Each student takes 1.5 hours including prep. What is the most students per week, '
          'rounded down?', '16 students', ('17 students', 'rounded up'), ('25 students', 'ignored prep'), ('37 students', 'multiplied'),
          '25 / 1.5 = 16.7, so 16 whole students.', calc=lambda: math.floor(25 / 1.5) == 16),
        Q('A baker charges 60 dollars for a custom cake with 20 dollars of ingredients. It takes 5 hours. What is the hourly '
          'rate on profit?', '8 dollars an hour', ('12 dollars an hour', 'ignored ingredients'), ('40 dollars an hour', 'not per hour'),
          ('4 dollars an hour', 'used 10 hours'), '(60 - 20) / 5 = 8.', calc=lambda: (60 - 20) / 5 == 8),
        Q('The baker wants at least 20 dollars an hour on that cake. What price is needed?', '120 dollars', ('100 dollars', 'left out ingredients'),
          ('80 dollars', 'too low'), ('25 dollars', 'per hour plus 5'), '20 x 5 + 20 = 120.', calc=lambda: 20 * 5 + 20 == 120),
        Q('A photographer is fully booked for 2 months. What does this suggest?', 'Prices may be too low for the demand',
          ('She should lower prices further', 'demand already exceeds capacity'), ('She should stop marketing forever', 'too extreme'),
          ('Nothing; bookings never matter', 'they signal demand'), 'Full capacity can support a price increase.'),
    ]),
    F2=sec('Handle the complications: burnout and hidden work', CAP, [
        Q('An owner works 70 hours a week to meet demand and feels exhausted. What is the main risk?', 'Mistakes and burnout that hurt the business',
          ('More profit with no downside', 'ignores risk'), ('Customers will pay double automatically', 'not stated'),
          ('Capacity grows by itself', 'no'), 'Overwork harms quality and health.'),
        Q('A job seems to pay 50 dollars an hour, but the client asks for many unpaid revisions, doubling the time. What is the '
          'real rate?', '25 dollars an hour', ('50 dollars an hour', 'ignored revisions'), ('100 dollars an hour', 'wrong direction'),
          ('75 dollars an hour', 'averaged wrongly'), 'Double the time halves the rate.', calc=lambda: 50 / 2 == 25),
        Q('What helps prevent unpaid revisions?', 'Stating how many revisions the price includes', ('Never talking about revisions', 'causes confusion'),
          ('Offering unlimited free changes', 'causes the problem'), ('Charging nothing at all for the first job with a client', 'unrelated'),
          'Clear scope protects time.'),
        Q('A helper costs 20 dollars an hour and lets the owner take jobs earning 45 dollars an hour of profit before paying help. '
          'Ignoring other costs, what is left per helper hour?', '25 dollars', ('45 dollars', 'ignored helper cost'),
          ('65 dollars', 'added'), ('20 dollars', 'helper cost'), '45 - 20 = 25.', calc=lambda: 45 - 20 == 25),
        Q('Which statement is accurate?', 'Owner time is a real cost even when no one sends a bill for it.',
          ('Owner time is always free.', 'it has value'), ('Capacity never limits small businesses, because owners can always work more.', 'it does'),
          ('Hidden tasks take no time.', 'they do'), 'Count all hours.'),
    ]))

# ------------------------------------------------------------------ Set 53: reviewing and raising prices
RAISE = ('Prices should be reviewed regularly, for example every 6 or 12 months, or when costs change. Signs a price may be '
         'too low: costs have risen, you are fully booked, or your hourly rate is below what you need. To raise prices '
         'well, give current customers notice, explain briefly (for example, higher material costs), and consider '
         'keeping old prices for a short time for loyal clients. Some customers may leave; check whether the remaining '
         'sales bring in more total contribution.')

s53 = SET('ENT.PRICE.07',
    M=sec('Decide when to raise prices and communicate the change', RAISE, [
        Q('Which is a sign a price may be too low?', 'The owner is fully booked months ahead',
          ('Customers sometimes compliment the product', 'not a pricing signal'),
          ('The logo was redesigned recently', 'unrelated'), ('The owner bought a new phone', 'unrelated'),
          'Full demand can support higher prices.'),
        Q('Supplies rise from 4 to 5 dollars per item and price stays 12 dollars. What is the new contribution?', '7 dollars',
          ('8 dollars', 'old contribution'), ('17 dollars', 'added'), ('1 dollar', 'the cost change'), '12 - 5 = 7.',
          calc=lambda: 12 - 5 == 7),
        Q('What is a respectful way to raise prices?', 'Give notice and a short reason',
          ('Change prices without telling anyone', 'surprises customers'), ('Raise prices every week', 'confusing'),
          ('Blame customers for the change', 'harmful'), 'Notice and honesty keep trust.'),
        Q('How often might a small business review prices?', 'Every 6 or 12 months, or when costs change',
          ('Only once, on opening day', 'too rare'), ('Never, because prices are set permanently at opening', 'not true'),
          ('Every hour', 'impractical'), 'Regular reviews keep prices current.'),
        Q('After a raise, some customers leave. What should the owner check?', 'Whether total contribution went up or down',
          ('Only whether anyone complained about the new price', 'not the full picture'), ('Only the number of customers', 'not enough'),
          ('Only competitors\' logos', 'irrelevant'), 'Fewer customers can still mean more money.'),
    ]),
    B=[mathb('Percent increase', 'To raise a price by a percent, multiply by (1 + the decimal). A 10 percent raise is x 1.10; '
             'a 15 percent raise is x 1.15. Example: 40 dollars raised 15 percent is 40 x 1.15 = 46 dollars. To find the '
             'percent change between two prices, divide the change by the OLD price: from 40 to 46 is 6 / 40 = 0.15 = 15 '
             'percent.', [
        Q('What is 50 raised by 10 percent?', '55', ('60', 'added 10'), ('5', 'only the raise'), ('50.10', 'added 0.10'),
          '50 x 1.10 = 55.', calc=lambda: round(50 * 1.10, 2) == 55),
        Q('From 20 to 25 dollars is what percent increase?', '25 percent', ('20 percent', 'used new price'), ('5 percent', 'dollar change'),
          ('125 percent', 'ratio'), '5 / 20 = 0.25.', calc=lambda: (25 - 20) / 20 == 0.25),
        Q('A 15 percent raise means multiply by what?', '1.15', ('0.15', 'only the raise'), ('0.85', 'a decrease'),
          ('15', 'not a decimal'), '1 + 0.15 = 1.15.'),
        Q('What is 80 raised by 5 percent?', '84', ('85', 'added 5'), ('4', 'only the raise'), ('80.05', 'added 0.05'),
          '80 x 1.05 = 84.', calc=lambda: round(80 * 1.05, 2) == 84),
        Q('To find a percent change, divide the change by which price?', 'The old price', ('The new price', 'wrong base'),
          ('Any price', 'base matters'), ('The cost', 'not the base'), 'Percent change uses the original value.'),
    ], why='A learner who misses MAIN may not compute a price increase or percent change; this practices both.')],
    F1=sec('Apply it: test a price increase', RAISE, [
        Q('A dog groomer has 50 clients at 40 dollars with a 15-dollar cost each. She raises the price to 48 dollars and 5 '
          'clients leave. What is the new total contribution?', '1,485 dollars', ('1,250 dollars', 'old total'),
          ('1,650 dollars', 'no clients lost'), ('2,160 dollars', 'used price not contribution'),
          'Old: 50 x 25 = 1,250. New: 45 x 33 = 1,485.', calc=lambda: 45 * (48 - 15) == 1485 and 50 * 25 == 1250),
        Q('Using the groomer numbers, did the raise help?', 'Yes, contribution rose by 235 dollars', ('No, because she lost 5 of her clients', 'but earns more'),
          ('No, contribution fell', 'it rose'), ('It made no difference', 'it changed'), '1,485 - 1,250 = 235.',
          calc=lambda: 1485 - 1250 == 235),
        Q('Which notice is best?', '"From March 1, prices rise to 48 dollars due to higher supply costs."',
          ('"Prices are higher now. Deal with it."', 'disrespectful'), ('No notice at all; she should just charge more at checkout from now on', 'surprises'),
          ('"Prices might change sometime, maybe."', 'unclear'), 'Date, amount and reason.'),
        Q('A 40-dollar price raised by 12.5 percent becomes what?', '45 dollars', ('52.50 dollars', 'added 12.5'),
          ('5 dollars', 'only the raise'), ('40.13 dollars', 'added 0.125'), '40 x 1.125 = 45.', calc=lambda: 40 * 1.125 == 45),
        Q('A loyal client has booked monthly for 3 years. What is a thoughtful option during a raise?', 'Keep the old price for a short grace period',
          ('Raise her price more than everyone else\'s price', 'unfair'), ('Hide the raise from her', 'dishonest'),
          ('Drop her as a client', 'unnecessary'), 'Grace periods reward loyalty.'),
    ]),
    F2=sec('Handle the complications: fear and competitors', RAISE, [
        Q('An owner fears that any raise will lose all customers. What evidence would help?', 'Testing a modest raise and tracking results',
          ('Assuming the worst and never changing', 'no evidence'), ('Copying a random competitor\'s price', 'not her costs'),
          ('Asking only family', 'biased'), 'A small test produces data.'),
        Q('A competitor charges less. The owner\'s costs are higher because she uses better materials. What fits?',
          'Explain the value and price to cover her costs', ('Match the competitor\'s lower price, even if she loses money', 'unsustainable'),
          ('Use worse materials secretly', 'dishonest'), ('Ignore costs entirely', 'risky'), 'Price must cover costs; value explains it.'),
        Q('Prices rose 20 percent but sales fell 40 percent. Contribution per sale went from 10 to 14 dollars. Was it a gain? '
          '(Start with 100 sales.)', 'No, contribution fell from 1,000 to 840 dollars', ('Yes, contribution rose from 1,000 to 1,400 dollars', 'ignored lost sales'),
          ('Yes, from 1,000 to 1,200 dollars', 'miscalculated'), ('No change at all', 'it changed'),
          '60 x 14 = 840 < 1,000.', calc=lambda: 60 * 14 == 840 and 100 * 10 == 1000),
        Q('Costs rose 10 percent but the owner has not reviewed prices in 3 years. What should she do?', 'Recalculate costs and review prices now',
          ('Wait another 3 years', 'costs keep rising'), ('Cut quality quietly to avoid any price raise', 'may lose customers'),
          ('Stop tracking costs', 'harmful'), 'Regular review prevents shrinking margins.'),
        Q('Which statement is accurate?', 'A price increase can raise total contribution even if some customers leave.',
          ('Losing any customer at all always means the business loses money overall.', 'not always'), ('Prices should never change.', 'not true'),
          ('Raises always double profit.', 'not true'), 'Check the totals.'),
    ]))

# ------------------------------------------------------------------ Set 54: cash timing, invoices, deposits
TIMING = ('Cash often arrives later than work is done. An INVOICE is a bill sent to a customer; "Net 30" means payment is '
          'due 30 days after the invoice date. Meanwhile, the business may have to pay for materials and its own bills. '
          'A DEPOSIT is money paid up front before work starts; it reduces risk and helps buy materials. Track unpaid '
          'invoices (accounts receivable), send reminders on the due date, and set clear terms in writing, such as a '
          'late fee if allowed where you operate.')

s54 = SET('ENT.CASH.02',
    M=sec('Plan for invoice timing, deposits and overdue payments', TIMING, [
        Q('What does "Net 30" mean?', 'Payment is due 30 days after the invoice date',
          ('A 30 percent discount for paying early', 'not the meaning'), ('The customer may pay any time in the year', 'not the meaning'),
          ('The business must pay 30 dollars', 'not the meaning'), 'Net 30 sets the due date.'),
        Q('What is a deposit?', 'Money paid up front before work starts', ('A refund paid after a customer complaint', 'not a deposit'),
          ('A tax paid to the state', 'not a deposit'), ('A bonus paid to employees', 'not a deposit'), 'Deposits come first.'),
        Q('An invoice dated June 1 is Net 30. When is it due?', 'July 1', ('June 30 of next year', 'too late'),
          ('June 2', 'too early'), ('August 1', 'Net 60'), 'June has 30 days: June 1 + 30 days = July 1.'),
        Q('What are accounts receivable?', 'Money customers owe the business', ('Money the business owes suppliers', 'payables'),
          ('Cash in the owner\'s wallet', 'not receivable'), ('The value of equipment', 'assets, not receivables'),
          'Receivables are unpaid invoices.'),
        Q('Why ask for a deposit on a large custom order?', 'It reduces risk and helps pay for materials',
          ('It guarantees the customer will love the order', 'no guarantee'), ('It replaces the need for an invoice', 'still invoice'),
          ('It lowers the business\'s taxes', 'not the purpose'), 'Deposits protect cash.'),
    ]),
    B=[cs('Waiting for allowance', 'Imagine doing chores all month but receiving your allowance only at the end of the next '
          'month. Meanwhile, you still need money for lunch. Businesses face the same gap: they do the work, send an '
          'invoice, and wait for payment while bills keep coming. A deposit is like getting part of the allowance before '
          'you start the chores.', [
        Q('Doing chores before being paid is like what?', 'Working before an invoice is paid', ('Getting a deposit up front from the customer', 'paid first'),
          ('Paying taxes', 'no'), ('Buying supplies', 'no'), 'Work comes before cash.'),
        Q('Needing lunch money while waiting is like what?', 'Bills due before payment arrives', ('Extra profit for the whole month', 'no'),
          ('A refund', 'no'), ('A discount code for next time', 'no'), 'The cash gap.'),
        Q('Getting part of the allowance first is like what?', 'A deposit', ('An invoice', 'a bill'), ('A refund', 'no'),
          ('A fee', 'no'), 'Money before work.'),
        Q('What makes the waiting harder?', 'Longer payment terms', ('Shorter payment terms', 'easier'),
          ('Deposits', 'easier'), ('Reminders', 'help'), 'Longer waits widen the gap.'),
        Q('What helps close the gap?', 'Deposits and prompt invoicing', ('Waiting longer to invoice', 'worse'),
          ('Never sending reminders', 'worse'), ('Offering longer terms', 'worse'), 'Get paid sooner.'),
    ], why='A learner who misses MAIN may not feel the timing gap; waiting for an allowance makes it familiar.')],
    F1=sec('Apply it: plan cash around invoices', TIMING, [
        Q('A designer finishes a 2,000-dollar project and invoices Net 30. Her rent of 900 dollars is due in 10 days. She has '
          '500 dollars. What is the problem?', 'She is 400 dollars short for rent before the invoice is due',
          ('She has plenty of cash right now to cover the rent easily', 'only 500 dollars'), ('The invoice is already overdue', 'not yet due'),
          ('Rent is not her concern', 'it is due'), '900 - 500 = 400 short.', calc=lambda: 900 - 500 == 400),
        Q('Which change would help her most on future projects?', 'Ask for a 50 percent deposit at the start',
          ('Offer Net 90 payment terms to all clients', 'makes it worse'), ('Invoice only after 2 months', 'makes it worse'),
          ('Stop sending invoices', 'no payment'), 'Deposits bring cash earlier.'),
        Q('A 50 percent deposit on a 2,000-dollar project is how much?', '1,000 dollars', ('500 dollars', '25 percent'),
          ('2,000 dollars', 'full price'), ('1,500 dollars', '75 percent'), '0.50 x 2,000 = 1,000.', calc=lambda: 0.5 * 2000 == 1000),
        Q('An invoice was due 15 days ago and is unpaid. What is a sensible first step?', 'Send a polite reminder with the invoice attached',
          ('Post the client\'s name online as a late payer', 'harmful'), ('Ignore it forever', 'loses money'), ('Start a lawsuit today', 'too early'),
          'A reminder often solves it.'),
        Q('A business has receivables of 6,000 dollars, of which 1,500 dollars is over 60 days late. What fraction is very late?',
          '1/4', ('1/2', 'miscalculated'), ('3/4', 'reversed'), ('1/6', 'miscalculated'), '1,500 / 6,000 = 0.25.',
          calc=lambda: 1500 / 6000 == 0.25),
    ]),
    F2=sec('Handle the complications: late payers and big clients', TIMING, [
        Q('A large client insists on Net 60 terms. The order is 10,000 dollars of materials and labor. What should the owner '
          'check?', 'Whether she has cash to cover costs for 60 days', ('Only whether the client is famous', 'not enough'),
          ('Whether the logo will be on the client\'s site', 'not the issue'), ('Nothing; big clients always pay early', 'not guaranteed'),
          'Long terms need cash to cover the wait.'),
        Q('A client has missed three payment dates. What protects the business on future work?', 'Require payment or a deposit before starting',
          ('Offer even longer payment terms to be kind', 'more risk'), ('Do more work on credit', 'more risk'), ('Remove invoices', 'no record'),
          'Upfront payment reduces risk.'),
        Q('A contract allows a 1.5 percent monthly late fee where permitted. A 2,000-dollar invoice is one month late. What is '
          'the fee?', '30 dollars', ('300 dollars', 'used 15 percent'), ('3 dollars', 'moved decimal'), ('1.50 dollars', 'not percent'),
          '0.015 x 2,000 = 30.', calc=lambda: round(0.015 * 2000, 2) == 30),
        Q('Before adding late fees, what should an owner check?', 'Whether local law allows them and the contract states them',
          ('Only whether competitors in her area use late fees', 'not the rule'), ('Nothing; any fee is allowed', 'rules vary'),
          ('Only the invoice font', 'irrelevant'), 'Fees must be legal and agreed.'),
        Q('Which statement is accurate?', 'Clear written terms and early reminders reduce late payments.',
          ('Customers always pay on time without any reminders or written terms.', 'not always'), ('Deposits are illegal.', 'not true'),
          ('Invoices are optional for businesses.', 'records needed'), 'Systems help cash flow.'),
    ]))

# ------------------------------------------------------------------ Set 55: cash reserve
RES = ('A CASH RESERVE (emergency fund) is money the business keeps aside for slow months, repairs or late payments. A '
       'common planning approach is to save enough to cover a set number of months of essential expenses, such as 2 to '
       '3 months; this is a planning assumption, not a rule. Build it gradually, for example by moving a percentage of '
       'each sale into a separate savings account. Use it only for real emergencies, then refill it. Without a reserve, '
       'one surprise can force expensive borrowing.')

s55 = SET('ENT.CASH.03',
    M=sec('Size and build a business cash reserve', RES, [
        Q('What is a cash reserve?', 'Money set aside for slow months and surprises',
          ('Money spent on advertising and promotions each month', 'not a reserve'), ('Money owed to suppliers', 'not a reserve'),
          ('Money used for the owner\'s vacation', 'not a reserve'), 'It is a safety buffer.'),
        Q('Essential expenses are 1,500 dollars a month. What is a 3-month reserve?', '4,500 dollars',
          ('1,500 dollars', 'one month'), ('500 dollars', 'divided'), ('3,000 dollars', 'two months'), '1,500 x 3 = 4,500.',
          calc=lambda: 1500 * 3 == 4500),
        Q('How can a reserve be built gradually?', 'Move a percentage of each sale into savings',
          ('Wait until a big emergency happens, then start saving', 'too late'), ('Borrow the full amount at once', 'adds debt'),
          ('Spend everything and hope', 'no reserve'), 'Small regular amounts add up.'),
        Q('When should the reserve be used?', 'For real emergencies, then refilled', ('For any purchase the owner wants', 'not emergencies'),
          ('Never, even in emergencies', 'defeats the purpose'), ('Only to pay owner bonuses', 'not emergencies'),
          'Use it for its purpose and rebuild it.'),
        Q('What can happen without a reserve?', 'A surprise may force expensive borrowing', ('Profits always double', 'no'),
          ('Taxes disappear', 'no'), ('Nothing ever goes wrong for the business', 'not realistic'), 'Reserves reduce risk.'),
    ]),
    B=[mathb('Saving a percent until a goal', 'To see how long a savings goal takes, find how much you save each period, '
             'then divide the goal by that amount. Example: save 10 percent of 2,000 dollars of monthly sales = 200 dollars '
             'a month. A 1,200-dollar goal takes 1,200 / 200 = 6 months. If the answer is not whole, round up to the next '
             'full month.', [
        Q('10 percent of 3,000 dollars is what?', '300 dollars', ('30 dollars', 'moved too far'), ('3,300 dollars', 'added'),
          ('2,700 dollars', 'subtracted'), '0.10 x 3,000 = 300.', calc=lambda: round(0.10 * 3000, 2) == 300),
        Q('Saving 250 dollars a month, how long to reach 1,000 dollars?', '4 months', ('3 months', 'too few'),
          ('250 months', 'confused'), ('40 months', 'moved decimal'), '1,000 / 250 = 4.', calc=lambda: 1000 / 250 == 4),
        Q('Saving 300 dollars a month, how long to reach 1,000 dollars, rounded up?', '4 months', ('3 months', 'rounded down'),
          ('3.3 months', 'not rounded'), ('5 months', 'too many'), '1,000 / 300 = 3.33, up to 4.', calc=lambda: math.ceil(1000 / 300) == 4),
        Q('5 percent of 4,000 dollars is what?', '200 dollars', ('20 dollars', 'moved too far'), ('800 dollars', 'divided by 5'),
          ('4,005 dollars', 'added'), '0.05 x 4,000 = 200.', calc=lambda: 0.05 * 4000 == 200),
        Q('Why round up the number of months?', 'A partial month does not reach the goal', ('Rounding down is always better for savings goals', 'falls short'),
          ('Months cannot be counted', 'they can'), ('It does not matter', 'it does'), 'Round up to fully reach the goal.'),
    ], why='A learner who misses MAIN may not compute how long saving takes; this practices percent and division.')],
    F1=sec('Apply it: plan a reserve', RES, [
        Q('A shop\'s essential costs are 2,000 dollars a month. It wants a 2-month reserve and saves 8 percent of 5,000 dollars '
          'of monthly sales. How many months to reach the goal?', '10 months', ('8 months', 'miscalculated'),
          ('5 months', 'used one month of costs'), ('25 months', 'used 4 percent'), 'Goal 4,000; saving 400 a month; 10 months.',
          calc=lambda: (2000 * 2) / (0.08 * 5000) == 10),
        Q('Which account fits a reserve best?', 'A separate business savings account', ('The owner\'s personal checking account', 'mixed'),
          ('A shoebox under the counter', 'unsafe'), ('A friend\'s account', 'not controlled'), 'Separate and safe.'),
        Q('The reserve is 3,000 dollars. An oven repair costs 1,200 dollars. What remains to refill?', '1,200 dollars',
          ('1,800 dollars', 'what remains, not refill'), ('3,000 dollars', 'full amount'), ('4,200 dollars', 'added'),
          '1,800 remains; refill the 1,200 used.', calc=lambda: 3000 - (3000 - 1200) == 1200),
        Q('A seasonal ice cream stand earns most money in summer. What does that suggest for its reserve?', 'Save more in summer to cover winter',
          ('Spend all summer income right away', 'risky'), ('Ignore winter costs', 'they continue'),
          ('Borrow every winter as a plan', 'costly'), 'Seasonal businesses need bigger buffers.'),
        Q('An owner uses the reserve to buy a new logo design. What is the problem?', 'It is not an emergency', ('Logos are illegal', 'no'),
          ('Reserves must never be used', 'they can be used for emergencies'), ('There is no problem', 'misuse'),
          'Reserves are for emergencies.'),
    ]),
    F2=sec('Handle the complications: competing needs', RES, [
        Q('An owner can either pay down a high-interest credit card or build a reserve. What is a balanced approach?',
          'Build a small starter reserve, then focus on the debt', ('Ignore both', 'risky'), ('Take on more debt', 'worse'),
          ('Spend on extras first and decide about debt later', 'risky'), 'Balance protection and cost.'),
        Q('Sales drop 30 percent for 2 months. Essential costs stay 2,000 dollars and income falls to 1,400 dollars. How much '
          'reserve is used over both months?', '1,200 dollars', ('600 dollars', 'one month'), ('4,000 dollars', 'all costs'),
          ('2,800 dollars', 'income'), '(2,000 - 1,400) x 2 = 1,200.', calc=lambda: (2000 - 1400) * 2 == 1200),
        Q('A business has a 6-month reserve but keeps adding to it while equipment is failing. What should it consider?',
          'Whether part of the reserve should fund needed equipment', ('Never touching the reserve, even for needed equipment', 'may harm operations'),
          ('Selling the equipment', 'not stated'), ('Closing the business', 'too extreme'), 'Reserves should match real needs.'),
        Q('A reserve sits in an account the owner also uses for daily spending. What is the risk?', 'It gets spent without noticing',
          ('It grows faster', 'no'), ('It becomes taxable twice each year', 'no'), ('Nothing at all', 'mixing risk'), 'Keep it separate.'),
        Q('Which statement is accurate?', 'The right reserve size depends on the business; months of expenses is a planning guide.',
          ('Every business needs exactly 3 months of expenses saved, no matter its risks or seasons.', 'not a rule'), ('Reserves are only for big companies.', 'all benefit'),
          ('A reserve replaces insurance.', 'both help'), 'Tailor to risk.'),
    ]))

# ------------------------------------------------------------------ Set 56: HP case
HP = ('Documented history (HP\'s own history pages): Bill Hewlett and Dave Packard began part-time work in a garage in '
      'Palo Alto, California, with 538 dollars in working capital. Their first product was the HP 200A audio oscillator, '
      'an instrument used to test sound equipment. Walt Disney Studios asked for changes and ordered eight of the '
      'modified model, the 200B, for the film Fantasia. Lesson drawn by this course (an interpretation): start with '
      'little capital, solve a specific problem for professional users, and adapt to a serious customer\'s request. '
      'One success story does not guarantee the same result for another business.')

s56 = SET('ENT.CASE.05',
    M=sec('Apply a documented early decision: solve a specific need and adapt for a key customer', HP, [
        Q('According to the passage, how much working capital did they start with?', '538 dollars',
          ('5,380 dollars', 'not the documented figure'), ('53,800 dollars', 'not the documented figure'),
          ('No money at all', 'they had 538 dollars'), 'The passage gives 538 dollars.'),
        Q('What was their first product?', 'An audio oscillator for testing sound equipment',
          ('A home computer for families and schools', 'not their first product'), ('A printer for offices', 'not their first product'),
          ('A film camera for studios', 'not their first product'), 'The HP 200A was an audio oscillator.'),
        Q('What did Walt Disney Studios do?', 'Asked for changes and ordered eight of the modified model',
          ('Bought the whole company outright in its first year', 'not stated'), ('Refused to buy any product', 'they ordered'),
          ('Designed the product for HP', 'HP made the changes'), 'Disney ordered eight 200B units.'),
        Q('Which lesson does this course draw?', 'Solve a specific need and adapt to a serious customer',
          ('Always start with a large investment', 'they started with little'),
          ('Never change a product, even for a serious customer', 'they did adapt'),
          ('Only sell to the general public', 'they sold to professionals'), 'Adapting for a key customer is the lesson drawn.'),
        Q('Which statement about this case is accurate?', 'It is one example and does not guarantee the same result.',
          ('It proves every business started in a garage will succeed.', 'one case proves nothing'), ('It shows a big customer is never risky.', 'not stated'),
          ('It shows capital never matters.', 'not the lesson'), 'One story teaches; it does not promise.'),
    ]),
    B=[cs('Facts versus the lesson', 'A case passage has two parts. The documented history is what records show: an amount '
          'of money, a first product, a customer order. The lesson drawn is this course\'s interpretation: an idea you '
          'might apply. Keep them separate. A later reputation does not prove each early step caused the success; it '
          'only shows what happened in that one case.', [
        Q('"They started with 538 dollars" is which part?', 'Documented history', ('The lesson drawn', 'interpretation'),
          ('A rumor with no source', 'it is sourced'), ('A guarantee', 'not a promise'), 'It is a recorded fact.'),
        Q('"Adapt to a serious customer\'s request" is which part?', 'The lesson drawn by the course', ('Documented history from HP', 'interpretation'),
          ('A legal rule for all businesses', 'no'), ('A tax fact', 'no'), 'It is an interpretation.'),
        Q('Does later fame prove each early step caused success?', 'No', ('Yes, always', 'not proof'), ('Only for HP', 'not proof'),
          ('Only in California', 'not proof'), 'Correlation is not proof.'),
        Q('Why keep facts and lessons separate?', 'So you know what is recorded and what is opinion', ('To confuse readers', 'no'),
          ('Because lessons drawn from cases are always wrong', 'not always'), ('Because facts never matter', 'they do'), 'Clarity about evidence.'),
        Q('"Disney ordered eight units" is which part?', 'Documented history', ('The lesson drawn', 'it is a record'), ('A guess with no record', 'documented'),
          ('A promise', 'not a promise'), 'It is recorded.'),
    ], why='A learner who misses MAIN may blur recorded facts with interpretation; this separates them.')],
    F1=sec('Apply it: adapt for a serious customer', HP, [
        Q('Lena makes a sound-testing app for audio studios. A large studio asks for two specific features and offers to buy '
          '10 licenses. Applying the lesson, what fits?', 'Check the cost of the changes and consider adapting for the order',
          ('Refuse the order, because a product must never change after launch', 'opposite of lesson'), ('Promise any feature without checking cost', 'risky'),
          ('Ignore the studio and target everyone', 'misses a real buyer'), 'Adapt when a serious customer commits, after checking cost.'),
        Q('Raj has 600 dollars to start. Which first step best follows the lesson?', 'Build a simple tool for one specific professional need',
          ('Rent a large factory first', 'needs much capital'), ('Design ten products for everyone', 'unfocused'),
          ('Wait until he has saved 100,000 dollars before starting', 'the case started small'), 'Start small and specific.'),
        Q('A customer asks for changes that would cost 2,000 dollars, and offers an order worth 1,500 dollars of contribution. '
          'What does the math suggest?', 'The order alone does not cover the change', ('It is clearly profitable', 'costs more'),
          ('Costs do not matter', 'they do'), ('Accept the order and ignore the cost of changes', 'loses money'), '1,500 < 2,000.', calc=lambda: 1500 < 2000),
        Q('In the same situation, what could make the change worthwhile?', 'Other customers also wanting the improved version',
          ('A nicer logo', 'irrelevant'), ('Never telling anyone', 'irrelevant'), ('Lowering the price of the studio\'s order further', 'worse'),
          'Wider demand can spread the cost.'),
        Q('Which detail is documented in the HP case and which is the course\'s lesson?', 'Eight units ordered is documented; "adapt for a key customer" is the lesson',
          ('Both are documented quotes from the founders', 'the lesson is an interpretation'),
          ('Both are guesses with no source', 'one is documented'),
          ('The lesson is documented by HP; the eight-unit order is only a guess', 'reversed'), 'Separate record from interpretation.'),
    ]),
    F2=sec('Handle the complications: depending on one big customer', HP, [
        Q('A small maker gets 80 percent of its sales from one customer. What is the main risk?', 'Losing that customer would cut most sales',
          ('No risk at all, since one customer is simpler to serve', 'concentration risk'), ('Taxes will double', 'unrelated'), ('Costs disappear', 'no'),
          'Concentration creates risk.'),
        Q('A big customer asks for a custom version at a discount. What should the owner check?', 'Whether the price still covers costs and time',
          ('Only whether the customer is famous in the industry', 'not enough'), ('Nothing; big orders are always good', 'not always'),
          ('Only the logo placement', 'irrelevant'), 'Check the math.'),
        Q('After adapting for one studio, the owner hopes others will buy. What should she do next?', 'Test whether other customers want the new version',
          ('Assume all studios will buy', 'untested'), ('Stop selling the old version immediately to every customer', 'premature'),
          ('Raise prices tenfold', 'untested'), 'Test before assuming.'),
        Q('Someone says, "HP started in a garage, so I need a garage to succeed." What is wrong?', 'The location is a detail, not the cause',
          ('Nothing; garages guarantee success', 'not true'), ('Garages are illegal for businesses', 'not true'),
          ('HP never used a garage', 'it did'), 'Do not copy surface details.'),
        Q('Which statement is accurate?', 'The case shows one path; other businesses face different conditions.',
          ('Every business should copy HP exactly.', 'not true'), ('Starting with small capital guarantees that a business will succeed.', 'not true'),
          ('Big customers never cause problems.', 'not true'), 'Learn the principle, not a promise.'),
    ]))

SETS = [s50, s51, s52, s53, s54, s55, s56]
