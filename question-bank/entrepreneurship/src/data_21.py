"""Entrepreneurship sets 136-145: Services path, Airbnb case, Products path.
Rates, prices and times are practice assumptions. Names are fictional."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 136: estimating a service job
EST = ('To estimate a service job, list every part of the work and estimate time for each, including setup, travel, '
       'cleanup and communication. Multiply total hours by your hourly rate, add materials, and add a small CONTINGENCY for '
       'surprises (for example 10 percent). Example: 6 hours at 45 dollars = 270, plus 60 dollars of materials = 330, plus '
       '10 percent = 363 dollars. Afterward, compare actual time with the estimate and adjust future estimates.')

s136 = SET('ENT.SVC.01',
    M=sec('Build a service estimate from time, rate, materials and contingency', EST, [
        Q('Which time should be included in an estimate?', 'All of it: setup, travel, cleanup, messages and the work',
          ('Only the minutes spent doing the main task itself', 'misses hidden time'),
          ('Only the time the customer can see you working', 'misses hidden time'),
          ('Only travel, since the work is the easy part', 'misses work'), 'All time.'),
        Q('5 hours at 40 dollars plus 50 dollars of materials. What is the subtotal?', '250 dollars', ('200 dollars', 'no materials'),
          ('95 dollars', 'added'), ('2,050 dollars', 'multiplied wrongly'), '5 x 40 + 50 = 250.', calc=lambda: 5 * 40 + 50 == 250),
        Q('Add 10 percent contingency to 250 dollars. What is the estimate?', '275 dollars', ('260 dollars', 'added 10 dollars'),
          ('250 dollars', 'no contingency'), ('25 dollars', 'contingency only'), '250 x 1.10 = 275.', calc=lambda: round(250 * 1.1, 2) == 275),
        Q('Why compare actual time with the estimate afterward?', 'To improve future estimates', ('To charge the customer extra secretly', 'improper'),
          ('Because estimates never matter', 'they do'), ('To delete old records', 'no'), 'Learn and adjust.'),
        Q('What is contingency in an estimate?', 'A small extra amount for surprises', ('A separate fee charged for travel only', 'part of time'),
          ('The customer\'s tip', 'no'), ('The materials cost', 'separate'), 'Buffer.'),
    ]),
    B=[mathb('Hours times rate plus extras', 'An estimate combines multiplication and addition: (hours x rate) + materials, then '
             'add the contingency percent. Example: 3 hours at 50 = 150; + 30 materials = 180; x 1.10 = 198. Do the steps in '
             'order. A common mistake is applying the percent before adding materials, which leaves the materials uncovered by '
             'the buffer. Checking each step on paper avoids that slip.', [
        Q('4 hours at 35 dollars. What is the labor cost?', '140', ('39', 'added'), ('8.75', 'divided'), ('35', 'rate'),
          '4 x 35 = 140.', calc=lambda: 4 * 35 == 140),
        Q('Labor 140 plus materials 40. What is the subtotal?', '180', ('100', 'subtracted'), ('5,600', 'multiplied'),
          ('140', 'labor only'), '140 + 40 = 180.', calc=lambda: 140 + 40 == 180),
        Q('180 plus 10 percent. What is the total?', '198', ('190', 'added 10'), ('18', 'percent only'), ('180', 'none'),
          '180 x 1.10 = 198.', calc=lambda: round(180 * 1.1, 2) == 198),
        Q('Which order is correct?', 'Labor, then add materials, then add the percent', ('Percent first, then labor, then materials last', 'wrong'),
          ('Materials times rate', 'wrong'), ('Add hours to rate', 'wrong'), 'Order matters.'),
        Q('2.5 hours at 60 dollars. What is the labor cost?', '150', ('62.5', 'added'), ('120', '2 hours'), ('24', 'divided'),
          '2.5 x 60 = 150.', calc=lambda: 2.5 * 60 == 150),
    ], why='A learner who misses MAIN may combine the parts in the wrong order; this practices the steps.')],
    F1=sec('Apply it: estimate real jobs', EST, [
        Q('A painter estimates 7 hours of painting, 1 hour of setup, 1 hour of cleanup and 1 hour of travel at 45 dollars, plus 120 '
          'dollars of paint. What is the subtotal before contingency?', '570 dollars', ('435 dollars', 'painting only'),
          ('450 dollars', 'labor only'), ('165 dollars', 'added rate'), '10 x 45 + 120 = 570.', calc=lambda: 10 * 45 + 120 == 570),
        Q('With 10 percent contingency, what is the estimate?', '627 dollars', ('580 dollars', 'added 10'), ('570 dollars', 'none'),
          ('57 dollars', 'contingency only'), '570 x 1.10 = 627.', calc=lambda: round(570 * 1.1, 2) == 627),
        Q('The job actually took 12 hours instead of 10. What is the labor overrun at 45 dollars an hour?', '90 dollars', ('45 dollars', 'one hour'),
          ('540 dollars', 'all hours'), ('2 dollars', 'hours'), '2 x 45 = 90.', calc=lambda: 2 * 45 == 90),
        Q('Did the 57-dollar contingency cover that overrun?', 'No, it fell 33 dollars short', ('Yes, with 33 dollars to spare', 'reversed'),
          ('Yes, exactly', 'no'), ('Cannot tell', 'can'), '90 - 57 = 33.', calc=lambda: 90 - 57 == 33),
        Q('What should the painter do on future similar jobs?', 'Estimate more time for this kind of job', ('Keep the same estimate for the next job', 'ignores data'),
          ('Remove the contingency', 'worse'), ('Stop tracking time', 'no learning'), 'Adjust.'),
    ]),
    F2=sec('Handle the complications: unknowns and pressure', EST, [
        Q('A job has unknowns, such as hidden water damage. What is a fair way to estimate?', 'Give a range and explain what could change it',
          ('Give one low number and hope', 'risky'), ('Refuse to estimate any job', 'loses work'), ('Promise no changes to the price no matter what', 'risky'),
          'Ranges with assumptions.'),
        Q('A client says another provider quoted much lower. What should the owner check first?', 'Whether the other quote includes the same work',
          ('Nothing, because she should match the lower quote instantly', 'may lose money'), ('Only the other provider\'s logo', 'irrelevant'),
          ('Only how friendly the client is', 'not enough'), 'Compare scope.'),
        Q('Over 5 jobs, actual hours were 10 percent above estimates on average. Next job estimates 20 hours. What adjusted estimate fits?',
          '22 hours', ('20 hours', 'unadjusted'), ('30 hours', 'added 10 hours'), ('18 hours', 'wrong direction'), '20 x 1.10 = 22.',
          calc=lambda: round(20 * 1.1, 2) == 22),
        Q('An owner never counts travel time in estimates. What happens over many jobs?', 'She works many unpaid hours', ('Nothing at all', 'hidden cost'),
          ('Her rate rises automatically', 'no'), ('Customers pay extra anyway', 'not if unbilled'), 'Hidden time adds up.'),
        Q('Which statement is accurate?', 'Good estimates include all time, materials and a buffer.',
          ('Estimates should only count the visible work done on site.', 'not true'), ('Contingency is dishonest.', 'not true'),
          ('Estimates never need adjusting.', 'they do'), 'Complete and learning.'),
    ]))

# ------------------------------------------------------------------ Set 137: appointment capacity and travel time
APPT = ('A service business sells time, so CAPACITY depends on how many appointments fit in a day. Count appointment length, '
        'TRAVEL between appointments, and a small BUFFER for delays. Example: a 9-hour day with 1.5-hour appointments plus 30 '
        'minutes of travel each fits 9 / 2 = 4.5, so 4 appointments. Grouping clients by area (ROUTING) reduces travel and '
        'increases capacity. Track no-shows and late cancellations, which waste capacity.')

s137 = SET('ENT.SVC.02',
    M=sec('Calculate daily appointment capacity including travel', APPT, [
        Q('A day has 8 hours. Each appointment is 1 hour plus 30 minutes of travel. How many full appointments fit?', '5',
          ('8', 'ignored travel'), ('6', 'rounded up'), ('4', 'too few'), '8 / 1.5 = 5.33, so 5.', calc=lambda: math.floor(8 / 1.5) == 5),
        Q('What is routing?', 'Grouping clients by area to reduce travel', ('Charging more for far-away clients only', 'different'),
          ('A computer network for the office', 'pun'), ('Cancelling clients who live far away', 'no'), 'Efficient travel.'),
        Q('Why include a buffer?', 'To handle delays without making later clients wait', ('To charge for unused time', 'no'),
          ('Because buffers are required by law for services', 'no'), ('To take more appointments', 'opposite'), 'Absorb delays.'),
        Q('What wastes capacity?', 'No-shows and late cancellations', ('Clients who arrive on time', 'no'), ('Accurate scheduling', 'no'),
          ('Grouping by area', 'helps'), 'Lost slots.'),
        Q('Cutting travel from 30 to 15 minutes per appointment in an 8-hour day with 1-hour appointments allows how many?', '6',
          ('5', 'old'), ('8', 'no travel'), ('7', 'rounded up'), '8 / 1.25 = 6.4, so 6.', calc=lambda: math.floor(8 / 1.25) == 6),
    ]),
    B=[mathb('Dividing the day into slots', 'To find how many appointments fit, divide the available hours by the time each one '
             'takes, including travel. Then round DOWN, because a partial appointment cannot be sold. Example: 7 hours / 1.25 hours '
             '= 5.6, so 5 appointments. Convert minutes to hours first: 45 minutes = 0.75 hours, 30 minutes = 0.5 hours, 15 '
             'minutes = 0.25 hours. Then add the parts before dividing.', [
        Q('45 minutes is how many hours?', '0.75', ('0.45', 'not converted'), ('1.5', 'no'), ('0.25', 'no'), '45 / 60 = 0.75.',
          calc=lambda: 45 / 60 == 0.75),
        Q('6 hours / 1.5 hours per slot. How many slots?', '4', ('9', 'multiplied'), ('4.5', 'not whole'), ('7.5', 'added'),
          '6 / 1.5 = 4.', calc=lambda: 6 / 1.5 == 4),
        Q('7 hours / 1.25 hours, rounded down?', '5', ('6', 'rounded up'), ('5.6', 'not rounded'), ('8.75', 'multiplied'),
          '7 / 1.25 = 5.6, so 5.', calc=lambda: math.floor(7 / 1.25) == 5),
        Q('Why round down?', 'A partial appointment cannot be sold', ('Rounding up is always better for the owner', 'no'), ('Hours are fake', 'no'),
          ('It does not matter', 'it does'), 'Whole slots only.'),
        Q('1 hour plus 15 minutes travel is how many hours?', '1.25', ('1.15', 'not converted'), ('16', 'added minutes'),
          ('0.75', 'subtracted'), '1 + 0.25 = 1.25.', calc=lambda: 1 + 15 / 60 == 1.25),
    ], why='A learner who misses MAIN may mishandle minutes and rounding; this practices slot math.')],
    F1=sec('Apply it: plan a mobile service day', APPT, [
        Q('A mobile groomer works 9 hours. Each groom is 1.5 hours with 30 minutes of driving. How many grooms fit?', '4',
          ('6', 'ignored driving'), ('5', 'rounded up'), ('3', 'too few'), '9 / 2 = 4.5, so 4.', calc=lambda: math.floor(9 / 2) == 4),
        Q('Routing cuts driving to 15 minutes each. How many grooms fit now?', '5', ('4', 'old'), ('6', 'ignored driving'),
          ('7', 'miscalculated'), '9 / 1.75 = 5.14, so 5.', calc=lambda: math.floor(9 / 1.75) == 5),
        Q('Each groom earns 70 dollars. How much more per day does routing allow?', '70 dollars', ('350 dollars', 'new total'),
          ('280 dollars', 'old total'), ('140 dollars', 'two grooms'), '5 x 70 - 4 x 70 = 70.', calc=lambda: 5 * 70 - 4 * 70 == 70),
        Q('Two no-shows a week at 70 dollars each cost how much over 4 weeks?', '560 dollars', ('140 dollars', 'one week'),
          ('280 dollars', 'two weeks'), ('70 dollars', 'one'), '2 x 70 x 4 = 560.', calc=lambda: 2 * 70 * 4 == 560),
        Q('Which policy helps reduce no-shows?', 'Reminder messages and a deposit for bookings', ('No reminders at all', 'more no-shows'),
          ('Booking clients across the whole state each day', 'more travel'), ('Removing the cancellation policy', 'worse'), 'Reduce waste.'),
    ]),
    F2=sec('Handle the complications: overbooking and long days', APPT, [
        Q('An owner books 6 appointments in a day that fits 4 with travel. What is the likely result?', 'Late arrivals and rushed work',
          ('Everything goes perfectly on time', 'unlikely'), ('More free time', 'no'), ('Lower costs', 'no'), 'Overbooking hurts.'),
        Q('Clients across town request the same day. What helps?', 'Assign days to areas so routes stay short', ('Drive back and forth across town all day', 'wasteful'),
          ('Refuse all far clients forever', 'loses work'), ('Charge nothing for travel', 'loses money'), 'Area days.'),
        Q('A 10-hour day fits 5 appointments at 2 hours each with no buffer. Adding a 20-minute buffer to each, how many fit?', '4',
          ('5', 'ignored buffer'), ('6', 'miscalculated'), ('3', 'too few'), '10 / 2.33 = 4.29, so 4.', calc=lambda: math.floor(10 / (2 + 20 / 60)) == 4),
        Q('Fewer appointments with buffers earn less per day. What can offset that?', 'Fewer delays, happier clients and fewer cancellations',
          ('Nothing, because buffers are always wasted time', 'not always'), ('Skipping lunch daily', 'unsustainable'), ('Lower prices', 'worse'),
          'Reliability has value.'),
        Q('Which statement is accurate?', 'Capacity depends on length, travel and buffers.',
          ('Travel time does not affect capacity.', 'it does'), ('More bookings always mean more income, even if overbooked.', 'not if overbooked'),
          ('Buffers are never useful.', 'they are'), 'Plan the day.'),
    ]))

# ------------------------------------------------------------------ Set 138: service scope and deposits
SSCOPE = ('Service jobs go wrong when SCOPE is vague. Before starting, write what is included (for example "deep clean of '
          'kitchen and 2 bathrooms"), what is not ("windows and inside the oven are extra"), how many visits or revisions are '
          'included, and what happens with extras. Take a DEPOSIT for bookings or custom work, especially if you buy '
          'materials or reserve a date; state whether it is refundable. Confirm changes in writing before doing extra work.')

s138 = SET('ENT.SVC.03',
    M=sec('Define service scope, extras and deposits in writing', SSCOPE, [
        Q('Which scope statement is clearest?', '"Deep clean of kitchen and 2 bathrooms; windows extra"', ('"Clean the house nicely"', 'vague'),
          ('"Do whatever needs doing around the whole house"', 'unlimited'), ('"Cleaning, more or less"', 'vague'), 'Specific and excludes extras.'),
        Q('Why take a deposit for a reserved date?', 'It protects the business if the client cancels', ('It is a tip for good service', 'no'),
          ('It replaces the final payment', 'not usually'), ('It is always fully refundable by law in every case', 'not always'), 'Commitment.'),
        Q('What should be stated about a deposit?', 'Whether it is refundable', ('Nothing at all', 'needed'), ('Only its color', 'irrelevant'),
          ('Only the owner\'s name', 'incomplete'), 'Terms.'),
        Q('A client asks for an extra room during the job. What should happen first?', 'Confirm the extra and its price in writing',
          ('Do it free without mention', 'scope creep'), ('Refuse to discuss it', 'inflexible'), ('Add it to the final bill later as a surprise', 'unfair'),
          'Agree first.'),
        Q('How many revisions does a scope usually need to state?', 'How many are included in the price', ('None are ever allowed', 'too rigid'),
          ('Unlimited revisions, always, for any price', 'creep'), ('It never matters', 'it does'), 'Limits.'),
    ]),
    B=[cs('A haircut menu', 'A salon menu might say "Cut and style, 45 dollars; coloring extra; one free touch-up within 7 days." '
          'You know what you get and what costs more. If the stylist added coloring without asking and charged you, you would '
          'be upset. A service scope is the menu for one job: included work, extras, limits, and agreement before anything '
          'extra is done.', [
        Q('"Coloring extra" is like what in a scope?', 'An excluded item that costs more', ('An item already included in the price', 'no'), ('A tip', 'no'),
          ('A tax', 'no'), 'Extras.'),
        Q('"One free touch-up within 7 days" is like what?', 'A stated limit on included revisions', ('Unlimited free work', 'no'),
          ('A cancellation fee for no-shows', 'no'), ('A discount code', 'no'), 'Limits.'),
        Q('Adding coloring without asking is like what?', 'Doing extra work without agreement', ('A normal service that is included', 'no'),
          ('A refund', 'no'), ('A deposit', 'no'), 'Needs agreement.'),
        Q('Why do you know what you get?', 'The menu lists it clearly', ('The salon guesses what you want', 'no'), ('You read minds', 'no'),
          ('Prices are hidden', 'no'), 'Clarity.'),
        Q('A service scope is like what for one job?', 'The menu', ('The chair', 'no'), ('The mirror', 'no'), ('The parking lot', 'no'),
          'A written list.'),
    ], why='A learner who misses MAIN may not picture a clear scope; a salon menu makes it concrete.')],
    F1=sec('Apply it: write scope and deposit terms', SSCOPE, [
        Q('A photographer books a 4-hour wedding for 1,600 dollars with a 25 percent nonrefundable deposit. What is the deposit?', '400 dollars',
          ('1,600 dollars', 'all'), ('25 dollars', 'percent as dollars'), ('1,200 dollars', 'balance'), '0.25 x 1,600 = 400.',
          calc=lambda: 0.25 * 1600 == 400),
        Q('Extra hours cost 300 dollars each. The client asks for 1.5 extra hours. What is the extra charge?', '450 dollars',
          ('300 dollars', 'one hour'), ('600 dollars', 'two hours'), ('301.5 dollars', 'added'), '1.5 x 300 = 450.', calc=lambda: 1.5 * 300 == 450),
        Q('Which scope line prevents a common dispute?', '"Includes 200 edited photos delivered within 3 weeks"', ('"Includes lots of photos, delivered eventually"', 'vague'),
          ('"Photos as needed"', 'vague'), ('"Some pictures, we will see"', 'vague'), 'Numbers and timing.'),
        Q('The client cancels 2 months before. The deposit is nonrefundable as agreed. What should happen?', 'Keep the deposit as the signed terms say',
          ('Refund it secretly and also charge more', 'contradictory'), ('Charge the full 1,600 dollars', 'not agreed'),
          ('Ignore the client', 'poor service'), 'Follow terms.'),
        Q('A cleaner\'s scope says "kitchen and 2 bathrooms." The client asks for the garage. What should she do?', 'Offer the garage as a priced extra',
          ('Clean it free and say nothing', 'creep'), ('Refuse to speak about it', 'unhelpful'), ('Clean it and surprise-bill double', 'unfair'),
          'Price extras.'),
    ]),
    F2=sec('Handle the complications: disputes over what was included', SSCOPE, [
        Q('A client insists windows were included, but the written scope says they were extra. What helps resolve it?', 'Pointing calmly to the written scope',
          ('Arguing loudly on social media', 'harmful'), ('Doing the windows free to avoid talking', 'sets precedent'),
          ('Refusing to finish the job', 'escalates'), 'Written terms.'),
        Q('A deposit was taken but the scope never said whether it was refundable. What problem arises?', 'A dispute about returning it',
          ('No problem; deposits are always kept', 'not clear'), ('The deposit doubles', 'no'), ('The job is free', 'no'), 'State terms.'),
        Q('Materials of 220 dollars must be bought before a job. The deposit is 150 dollars. How much must the owner front?', '70 dollars',
          ('220 dollars', 'all'), ('150 dollars', 'deposit'), ('370 dollars', 'added'), '220 - 150 = 70.', calc=lambda: 220 - 150 == 70),
        Q('A client adds small extras every visit. What is a fair approach?', 'Track extras and agree on how they are priced',
          ('Ignore all extras forever', 'creep'), ('Refuse all requests', 'inflexible'), ('Raise all prices later without explanation', 'unfair'),
          'Clarity.'),
        Q('Which statement is accurate?', 'Clear scope and deposit terms prevent many disputes.',
          ('A vague scope protects the business from disputes.', 'not true'), ('Deposits never need terms.', 'they do'),
          ('Extras should always be free.', 'not true'), 'Write it down.'),
    ]))

# ------------------------------------------------------------------ Set 139: repeat clients and scheduling
RECUR = ('Many service businesses grow through REPEAT CLIENTS: weekly cleaning, monthly lawn care, regular tutoring. Recurring '
         'clients make income more predictable and reduce marketing effort. Offer a simple recurring schedule, book the next '
         'visit before leaving, send reminders, and keep notes on each client\'s preferences. Plan capacity so regulars get '
         'reliable slots, and decide how far ahead to book and how to handle holidays.')

s139 = SET('ENT.SVC.04',
    M=sec('Build and schedule a base of repeat service clients', RECUR, [
        Q('Why are recurring clients valuable?', 'Income is steadier and less marketing is needed',
          ('They never need any reminders or attention at all', 'not true'), ('They pay twice as much automatically', 'no'),
          ('They replace the need for quality', 'no'), 'Steady income.'),
        Q('Which habit helps keep regulars?', 'Booking the next visit before leaving', ('Waiting for clients to remember to call', 'risky'),
          ('Changing their time every week randomly', 'unreliable'), ('Forgetting their preferences', 'poor service'), 'Book ahead.'),
        Q('A cleaner has 12 weekly clients at 90 dollars. What is weekly recurring revenue?', '1,080 dollars', ('102 dollars', 'added'),
          ('90 dollars', 'one'), ('7.50 dollars', 'divided'), '12 x 90 = 1,080.', calc=lambda: 12 * 90 == 1080),
        Q('Why keep notes on each client?', 'To remember preferences and serve them well', ('To share them publicly', 'privacy'),
          ('To raise prices secretly', 'no'), ('Because client notes are required by law', 'not the reason'), 'Personal service.'),
        Q('What should be decided about holidays?', 'How regular visits move when a holiday falls on them',
          ('Nothing, because holidays never affect service schedules', 'they do'), ('Only the owner\'s vacation photos', 'irrelevant'),
          ('Cancel all clients for the month', 'drastic'), 'Plan exceptions.'),
    ]),
    B=[cs('A newspaper delivery route', 'A newspaper carrier delivers to the same houses on the same days. Because the route is '
          'regular, the carrier knows the income, plans the time, and only needs new customers when someone moves away. A '
          'service business with recurring clients works like a route: predictable, efficient, and built on reliability. Keeping the route is easier than building a new one.', [
        Q('Why does the carrier know the income?', 'The same houses are served regularly', ('Papers are free', 'no'),
          ('Income changes randomly each week', 'no'), ('Nobody pays', 'no'), 'Recurring.'),
        Q('When does the carrier need new customers?', 'When someone moves away', ('Every single day, nonstop', 'no'), ('Never', 'no'),
          ('Only in summer', 'no'), 'Replacement only.'),
        Q('A route is like what for a service business?', 'A set of recurring clients', ('A one-time job for a stranger', 'no'), ('A single ad', 'no'),
          ('A tax form', 'no'), 'Regular base.'),
        Q('What makes the route work?', 'Reliability', ('Skipping houses', 'no'), ('Changing days randomly', 'no'), ('Late papers', 'no'),
          'Consistency.'),
        Q('Why is the route efficient?', 'The carrier can plan time and travel', ('It has no plan', 'no'), ('It changes daily without a plan', 'no'),
          ('It is random', 'no'), 'Planning.'),
    ], why='A learner who misses MAIN may not see the value of recurring work; a delivery route makes it concrete.')],
    F1=sec('Apply it: grow a recurring base', RECUR, [
        Q('A lawn service has 20 monthly clients at 60 dollars and adds 5 more. What is the new monthly recurring revenue?', '1,500 dollars',
          ('1,200 dollars', 'old'), ('300 dollars', 'new only'), ('85 dollars', 'added'), '25 x 60 = 1,500.', calc=lambda: 25 * 60 == 1500),
        Q('A tutor books the next session before each lesson ends. What is the main benefit?', 'Fewer gaps and more predictable income',
          ('Clients never cancel', 'not guaranteed'), ('Lessons become free', 'no'), ('No need for any reminders ever again', 'still useful'),
          'Predictability.'),
        Q('Weekly clients: 15 at 80 dollars. Two leave and three join. What is the new weekly revenue?', '1,280 dollars',
          ('1,200 dollars', 'old'), ('1,360 dollars', 'only joins'), ('1,040 dollars', 'only leaves'), '16 x 80 = 1,280.',
          calc=lambda: (15 - 2 + 3) * 80 == 1280),
        Q('A regular prefers no strong cleaning scents. Where should this be kept?', 'In the client\'s notes', ('Nowhere; memory is enough', 'unreliable'),
          ('On public social media', 'privacy'), ('In a random notebook', 'disorganized'), 'Client notes.'),
        Q('Regulars fill 30 of 35 weekly slots. How many slots remain for new clients?', '5', ('30', 'filled'), ('35', 'total'),
          ('65', 'added'), '35 - 30 = 5.', calc=lambda: 35 - 30 == 5),
    ]),
    F2=sec('Handle the complications: dependence and holidays', RECUR, [
        Q('One client is 40 percent of all revenue. What is the risk?', 'Losing that client would cut income sharply',
          ('No risk, because big clients never leave', 'they can'), ('Revenue doubles', 'no'), ('Taxes vanish', 'no'), 'Concentration.'),
        Q('A holiday falls on Thursday, a regular\'s day. What is a good approach?', 'Offer a nearby day in advance', ('Skip without telling them', 'poor service'),
          ('Charge double for the week', 'unfair'), ('Cancel them permanently', 'drastic'), 'Communicate early.'),
        Q('Regulars fill every slot and new inquiries keep coming. What could the owner consider?', 'A waitlist, a price increase or adding help',
          ('Overbooking regular slots', 'harms quality'), ('Turning away all the regular clients', 'drastic'), ('Lowering prices', 'worse'),
          'Manage demand.'),
        Q('Monthly churn of regulars is 5 percent of 40 clients. About how many leave each month?', '2', ('5', 'percent as count'),
          ('8', 'miscalculated'), ('20', 'half'), '0.05 x 40 = 2.', calc=lambda: round(0.05 * 40) == 2),
        Q('Which statement is accurate?', 'Recurring clients help, but avoid depending on one.',
          ('Recurring clients never leave.', 'they can'), ('One big client is always safest.', 'risky'),
          ('Scheduling does not matter for regular clients at all.', 'it does'), 'Balance.'),
    ]))

# ------------------------------------------------------------------ Set 140: Airbnb case
AIR = ('Documented history (Wharton/Knowledge at Wharton): In 2007 Brian Chesky and Joe Gebbia rented air mattresses in their '
       'San Francisco apartment to people attending a design conference when hotels were booked. The idea was first called '
       'AirBed & Breakfast, and Nathan Blecharczyk joined as a cofounder to build the website. Lesson drawn by this course '
       '(an interpretation): test a service idea first with resources you already have, during a moment of clear demand, '
       'before investing heavily. One success story does not guarantee the same result for another business.')

s140 = SET('ENT.CASE.10',
    M=sec('Apply a documented early decision: test a service with what you already have', AIR, [
        Q('According to the passage, what did the founders first rent out?', 'Air mattresses in their own apartment',
          ('A chain of hotels they had bought', 'not stated'), ('Office space downtown', 'not stated'),
          ('Cars to conference visitors', 'not stated'), 'Air mattresses.'),
        Q('Why was there demand at that moment?', 'Hotels were booked during a design conference', ('Rent was free that week', 'not stated'),
          ('A law required it', 'no'), ('They advertised heavily on national television', 'not stated'), 'Timing of demand.'),
        Q('What was the idea first called?', 'AirBed & Breakfast', ('HotelShare Rooms', 'not stated'), ('RoomNow', 'not stated'),
          ('CouchCity', 'not stated'), 'Original name.'),
        Q('Which lesson does this course draw?', 'Test with what you have during clear demand',
          ('Buy many properties first, before running any test', 'opposite'), ('Avoid moments of high demand', 'opposite'),
          ('Never use your own space', 'opposite'), 'Low-cost test.'),
        Q('Which statement about the Airbnb case is accurate?', 'It shows one test, not proof that every rental idea will work.',
          ('It proves every rental idea will grow into a huge company.', 'one case'), ('It shows conferences always create businesses.', 'overstated'),
          ('It shows websites are unnecessary.', 'they built one'), 'One story.'),
    ]),
    B=[cs('Selling umbrellas when it rains', 'If you notice a sudden rainstorm outside a busy station, you might sell a few '
          'spare umbrellas you already own. You test demand without buying a shop. The documented Airbnb facts are the '
          'conference, the air mattresses and the original name. Comparing it to umbrellas in the rain is this course\'s '
          'explanation of why the timing and low cost mattered.', [
        Q('Selling spare umbrellas you own is like what?', 'Testing with resources you already have', ('Buying a whole umbrella factory first', 'no'),
          ('Ignoring demand', 'no'), ('Waiting for sunshine', 'no'), 'Low-cost test.'),
        Q('The rainstorm is like what in the case?', 'The booked-up conference week', ('A slow season with no visitors', 'no'), ('A tax deadline', 'no'),
          ('A holiday sale', 'no'), 'Clear demand moment.'),
        Q('"They rented air mattresses in 2007" is which kind of statement?', 'Documented fact', ('Course explanation', 'documented'),
          ('A rumor', 'sourced'), ('A guarantee', 'no'), 'Recorded.'),
        Q('The umbrella comparison is which kind?', 'The course\'s explanation', ('A documented fact from records', 'no'), ('A law', 'no'),
          ('A contract', 'no'), 'Interpretation.'),
        Q('Why test without buying a shop?', 'To learn about demand cheaply', ('Shops are illegal', 'no'), ('Umbrellas are free to everyone', 'no'),
          ('Rain never stops', 'no'), 'Cheap learning.'),
    ], why='A learner who misses MAIN may not see why the test was cheap and well timed; selling umbrellas in the rain explains it.')],
    F1=sec('Apply it: design a low-cost service test', AIR, [
        Q('A town hosts a large marathon and hotels fill up. Ana has a spare room. Applying the lesson, what fits?', 'Offer the room to visitors that weekend as a test',
          ('Buy three apartments before the race weekend', 'large investment'), ('Ignore the event', 'missed test'),
          ('Wait for next year without testing', 'missed'), 'Test with what you have.'),
        Q('She charges 80 dollars a night for 3 nights and spends 30 dollars on cleaning supplies. What is her profit?', '210 dollars',
          ('240 dollars', 'ignored costs'), ('110 dollars', 'one night'), ('30 dollars', 'costs'), '3 x 80 - 30 = 210.', calc=lambda: 3 * 80 - 30 == 210),
        Q('Before renting, what should Ana check?', 'Local rules, her lease or HOA, and insurance', ('Nothing, because short rentals are always allowed', 'may be restricted'),
          ('Only the room\'s paint color', 'irrelevant'), ('Only competitors\' photos', 'not enough'), 'Rules apply.'),
        Q('A dog owner sees many neighbors asking for pet sitting during a holiday week. Which test fits the lesson?', 'Pet-sit a few pets that week from home',
          ('Lease a large kennel building first', 'large investment'), ('Advertise nationally', 'too broad'), ('Do nothing', 'missed'),
          'Small test.'),
        Q('Which detail from the case is documented?', 'The idea was first called AirBed & Breakfast', ('Testing small always works', 'interpretation'),
          ('Every founder should rent out air mattresses', 'not documented'), ('Conferences guarantee success', 'not documented'), 'Recorded.'),
    ]),
    F2=sec('Handle the complications: one busy week is not a market', AIR, [
        Q('Ana\'s room was full for the marathon weekend but empty for the next 6 weeks. What should she conclude?', 'One busy weekend does not prove steady demand',
          ('Demand is now guaranteed every week of the year', 'not shown'), ('She should buy more property today', 'premature'),
          ('Rentals never work', 'not shown'), 'Keep testing.'),
        Q('Someone says, "Airbnb used air mattresses, so I should too." What is wrong?', 'The lesson is a cheap test, not the mattress',
          ('Nothing, because air mattresses are the secret', 'surface detail'), ('Airbnb never used mattresses', 'it did'),
          ('Mattresses are illegal', 'no'), 'Copy the principle.'),
        Q('A guest damages property worth 150 dollars. What would have reduced the risk?', 'A deposit, clear rules and checking insurance',
          ('No rules at all', 'risky'), ('Hiding the room\'s condition from guests', 'no'), ('Charging nothing', 'irrelevant'), 'Plan for risk.'),
        Q('Over 10 weekends, the room is booked 3. What is the occupancy rate?', '30 percent', ('3 percent', 'count'),
          ('70 percent', 'empty'), ('10 percent', 'weekends'), '3 / 10 = 0.3.', calc=lambda: 3 / 10 == 0.3),
        Q('Which statement is accurate?', 'Test cheaply, then confirm demand over time.',
          ('One busy event proves a business will work.', 'not true'), ('Testing is unnecessary.', 'not true'), ('Every rental succeeds.', 'not true'),
          'Test and confirm.'),
    ]))

# ------------------------------------------------------------------ Set 141: suppliers, samples, reliability
SUPPLY = ('A product business depends on SUPPLIERS. Before a big order, request SAMPLES to check quality, compare at least two '
          'or three suppliers, and ask about minimum order quantity, price breaks, lead time, defect policy and payment terms. '
          'Start with a small order to test RELIABILITY: did it arrive on time, as described, with few defects? Keep a backup '
          'supplier for key items. The cheapest supplier is not always the best value if quality or delivery is poor.')

s141 = SET('ENT.PROD.01',
    M=sec('Evaluate suppliers with samples, small orders and backups', SUPPLY, [
        Q('Why request samples before a big order?', 'To check quality before committing', ('To get free products forever', 'not the purpose'),
          ('Because samples replace contracts', 'no'), ('To avoid paying for anything', 'no'), 'Quality check.'),
        Q('What should be asked about a supplier\'s defects?', 'Their policy for defective items', ('Their favorite color', 'irrelevant'),
          ('Their office decor', 'irrelevant'), ('Nothing; defects never happen', 'they do'), 'Defect policy.'),
        Q('Why start with a small order?', 'To test reliability before larger commitments', ('Small orders are always cheaper per item', 'often not'),
          ('Large orders are illegal at first', 'no'), ('To confuse the supplier', 'no'), 'Test reliability.'),
        Q('Why keep a backup supplier?', 'So a key item can still be sourced if the main one fails', ('To pay twice for everything', 'no'),
          ('Because having one supplier is illegal for shops', 'no'), ('To avoid all contracts', 'no'), 'Resilience.'),
        Q('Supplier A sells at 4.00 with 10 percent defects; B at 4.30 with 1 percent defects. Which is cheaper per good item?', 'B, about 4.34',
          ('A, about 4.44', 'A is higher'), ('A, at 4.00 exactly', 'ignores defects'), ('They are equal', 'differ'),
          'A: 4.00 / 0.90 = 4.44; B: 4.30 / 0.99 = 4.34.', calc=lambda: round(4 / 0.9, 2) == 4.44 and round(4.3 / 0.99, 2) == 4.34),
    ]),
    B=[mathb('Cost per good item', 'If some items arrive defective, the real cost of each usable item is higher. Cost per good item '
             '= price per item / share that is good. Example: 5 dollars each with 20 percent defective means 80 percent good: '
             '5 / 0.80 = 6.25 dollars per good item. Compare suppliers using this number, not just the listed price. The lowest sticker price can hide the highest real cost.', [
        Q('10 percent defective means what share is good?', '90 percent', ('10 percent', 'defective'), ('100 percent', 'no'),
          ('80 percent', 'miscalculated'), '100 - 10 = 90.', calc=lambda: 100 - 10 == 90),
        Q('6 dollars each, 75 percent good. What is the cost per good item?', '8 dollars', ('6 dollars', 'listed'), ('4.50 dollars', 'multiplied'),
          ('7.50 dollars', 'miscalculated'), '6 / 0.75 = 8.', calc=lambda: 6 / 0.75 == 8),
        Q('5 dollars each, 80 percent good. What is the cost per good item?', '6.25 dollars', ('5.00 dollars', 'listed'),
          ('4.00 dollars', 'multiplied'), ('5.80 dollars', 'added'), '5 / 0.8 = 6.25.', calc=lambda: 5 / 0.8 == 6.25),
        Q('Why divide by the good share?', 'Only good items can be sold, so they carry the cost', ('To make prices look lower', 'no'),
          ('Because defective items are free to replace', 'no'), ('It is a tax rule', 'no'), 'Spread cost over usable items.'),
        Q('Which is cheaper per good item: 3.00 at 60 percent good or 4.00 at 100 percent good?', '4.00 at 100 percent good',
          ('3.00 at 60 percent good', '5.00 per good'), ('They are equal', 'differ'), ('Cannot tell', 'can'),
          '3 / 0.6 = 5.00 > 4.00.', calc=lambda: 3 / 0.6 == 5 and 5 > 4),
    ], why='A learner who misses MAIN may compare only listed prices; this practices cost per usable item.')],
    F1=sec('Apply it: choose and test a supplier', SUPPLY, [
        Q('A candle maker gets samples from three jar suppliers. One sample cracked in shipping. What should she do?', 'Ask about packaging and test a small order first',
          ('Order 5,000 jars immediately to get the lowest price', 'risky'), ('Ignore the crack', 'risk'), ('Choose based only on price', 'incomplete'),
          'Test more.'),
        Q('Minimum order is 500 jars at 1.20 dollars. What is the minimum spend?', '600 dollars', ('500 dollars', 'count'),
          ('1.20 dollars', 'unit'), ('120 dollars', 'moved decimal'), '500 x 1.20 = 600.', calc=lambda: round(500 * 1.2, 2) == 600),
        Q('A small first order of 50 arrives 10 days late and 6 are cracked. What fraction is defective?', '12 percent',
          ('6 percent', 'count as percent'), ('50 percent', 'total'), ('10 percent', 'days'), '6 / 50 = 0.12.', calc=lambda: 6 / 50 == 0.12),
        Q('Which question matters most before relying on a supplier for a holiday rush?', 'Can you deliver this quantity by this date?',
          ('What music do you play in your office?', 'irrelevant'), ('Do you like my logo?', 'irrelevant'), ('How old is your website?', 'minor'),
          'Capacity and timing.'),
        Q('A key supplier is reliable but the only source. What is the next step?', 'Find and test a backup supplier', ('Do nothing; it will always be fine', 'risk'),
          ('Cancel the reliable supplier', 'unnecessary'), ('Stockpile a year of inventory regardless of cash', 'cash risk'), 'Resilience.'),
    ]),
    F2=sec('Handle the complications: quality drift and price changes', SUPPLY, [
        Q('A supplier\'s quality drops after 6 months. What should the owner do first?', 'Document the issue and raise it with the supplier',
          ('Say nothing and keep selling defects', 'harms customers'), ('Cancel all orders instantly without talking', 'drastic first'),
          ('Hide defects from customers', 'dishonest'), 'Communicate with evidence.'),
        Q('A supplier raises prices 15 percent from 8 dollars. What is the new price?', '9.20 dollars', ('8.15 dollars', 'added 0.15'),
          ('1.20 dollars', 'increase only'), ('23 dollars', 'added 15'), '8 x 1.15 = 9.20.', calc=lambda: round(8 * 1.15, 2) == 9.2),
        Q('The cheapest supplier is often late, causing refunds. What is the real issue?', 'Low price can cost more through late orders',
          ('There is no issue, because cheapest is always best', 'not always'), ('Refunds are free', 'they cost'), ('Customers never notice delays', 'they do'),
          'Total value.'),
        Q('A sample was excellent, but production items differ. What lesson applies?', 'Check production quality, not just samples',
          ('Samples always match the production items exactly', 'not always'), ('Never order samples', 'useful'), ('Quality never changes', 'it can'),
          'Verify ongoing.'),
        Q('Which statement is accurate?', 'Judge suppliers on quality, reliability and total cost.',
          ('The lowest listed price is always the best value overall.', 'not always'), ('One supplier is always enough.', 'risky'),
          ('Samples guarantee every future order.', 'not guaranteed'), 'Balanced evaluation.'),
    ]))

# ------------------------------------------------------------------ Set 142: packaging and damage
PACK = ('PACKAGING protects products in shipping and shapes the customer\'s first impression. Match packaging to the item: '
        'fragile items need cushioning and a sturdy box; flat items need stiff mailers. Test by packing a few items and '
        'shipping them to yourself or a friend. Include packaging cost (box, filler, tape, labels) in cost per item. Track '
        'DAMAGE RATE: damaged orders / total orders. A small increase in packaging cost can be worth it if it cuts expensive '
        'replacements.')

s142 = SET('ENT.PROD.02',
    M=sec('Choose protective packaging and track damage rate', PACK, [
        Q('What does packaging do besides protect the item?', 'Shapes the customer\'s first impression', ('Lowers all taxes owed', 'no'),
          ('Replaces the product description', 'no'), ('Removes shipping costs', 'no'), 'Impression.'),
        Q('Which is a good packaging test?', 'Ship a few packed items to yourself or a friend', ('Never test; just ship', 'risky'),
          ('Shake the empty box', 'not a test'), ('Ask a box supplier\'s opinion and nothing else', 'incomplete'), 'Real-world test.'),
        Q('What is damage rate?', 'Damaged orders divided by total orders', ('Total orders minus refunds given', 'no'),
          ('The cost of one box', 'no'), ('The shipping speed', 'no'), 'A ratio.'),
        Q('8 of 400 orders arrive damaged. What is the damage rate?', '2 percent', ('8 percent', 'count'), ('50 percent', 'misdivided'),
          ('0.2 percent', 'moved decimal'), '8 / 400 = 0.02.', calc=lambda: 8 / 400 == 0.02),
        Q('Which costs belong in packaging cost per item?', 'Box, filler, tape and labels', ('Only the box', 'incomplete'),
          ('Only the product', 'separate'), ('Only the owner\'s time on social media', 'unrelated'), 'All materials.'),
    ]),
    B=[mathb('Damage rate and replacement cost', 'Damage rate = damaged orders / total orders. Cost of damage = damaged orders x '
             'replacement cost. Example: 300 orders with 12 damaged is 12 / 300 = 4 percent; at 18 dollars to replace each, damage '
             'costs 12 x 18 = 216 dollars. Compare this with the extra cost of better packaging across all orders. The cheaper total wins, and fewer unhappy customers is a bonus.', [
        Q('15 damaged of 500. What is the damage rate?', '3 percent', ('15 percent', 'count'), ('33 percent', 'reversed'),
          ('0.3 percent', 'moved decimal'), '15 / 500 = 0.03.', calc=lambda: 15 / 500 == 0.03),
        Q('15 damaged at 20 dollars each. What is the damage cost?', '300 dollars', ('35 dollars', 'added'), ('20 dollars', 'one'),
          ('0.75 dollars', 'divided'), '15 x 20 = 300.', calc=lambda: 15 * 20 == 300),
        Q('Better packaging costs 0.50 more on 500 orders. What is the extra cost?', '250 dollars', ('0.50 dollars', 'one'),
          ('500.50 dollars', 'added'), ('1,000 dollars', 'doubled'), '0.50 x 500 = 250.', calc=lambda: 0.5 * 500 == 250),
        Q('If better packaging cuts damage cost from 300 to 40, what is the net saving after 250 extra?', '10 dollars',
          ('260 dollars', 'ignored packaging cost'), ('250 dollars', 'packaging'), ('290 dollars', 'added'),
          '(300 - 40) - 250 = 10.', calc=lambda: (300 - 40) - 250 == 10),
        Q('Which number shows how often damage happens?', 'Damage rate', ('Box price', 'no'), ('Number of tape rolls', 'no'),
          ('Shipping speed', 'no'), 'Frequency.'),
    ], why='A learner who misses MAIN may not weigh packaging against damage; this practices both costs.')],
    F1=sec('Apply it: improve packaging decisions', PACK, [
        Q('A ceramic mug shop has 20 damaged of 400 orders. Replacing each costs 22 dollars. What does damage cost?', '440 dollars',
          ('22 dollars', 'one'), ('20 dollars', 'count'), ('8,800 dollars', 'multiplied wrong'), '20 x 22 = 440.', calc=lambda: 20 * 22 == 440),
        Q('Double-boxing adds 0.80 dollars per order and cuts damage to 4 orders. What is the new total of packaging extra plus damage?',
          '408 dollars', ('440 dollars', 'old damage'), ('320 dollars', 'packaging only'), ('88 dollars', 'damage only'),
          '400 x 0.80 + 4 x 22 = 320 + 88 = 408.', calc=lambda: round(400 * 0.8 + 4 * 22, 2) == 408),
        Q('Is double-boxing worth it on cost alone?', 'Yes, slightly: 408 is less than 440', ('No, it costs more', 'reversed'),
          ('It is exactly equal either way', 'no'), ('Cannot tell', 'can'), '408 < 440.', calc=lambda: 408 < 440),
        Q('Besides cost, what else does fewer damaged orders improve?', 'Customer experience and reviews', ('Nothing else at all improves', 'not true'),
          ('Only the logo', 'irrelevant'), ('Taxes owed', 'not directly'), 'Reputation.'),
        Q('A flat art print arrives bent in a soft envelope. Which change fits?', 'A stiff mailer with a backing board', ('A bigger soft envelope with tape', 'still bends'),
          ('No packaging', 'worse'), ('Faster shipping only', 'still bends'), 'Match packaging to item.'),
    ]),
    F2=sec('Handle the complications: tradeoffs and sustainability', PACK, [
        Q('Customers ask for less plastic. What should the owner check before switching?', 'That new materials still protect items, by testing',
          ('Nothing, because any paper packaging works fine', 'may not protect'), ('Only the color of the paper', 'irrelevant'), ('Only competitors\' choices', 'not enough'),
          'Test alternatives.'),
        Q('A carrier crushed boxes several times. Besides packaging, what can help?', 'Filing claims and reviewing carrier options', ('Ignoring the pattern', 'continues'),
          ('Never shipping again', 'drastic'), ('Blaming customers for all of the damage', 'unfair'), 'Address the cause.'),
        Q('Packaging is 1.50 per order and the item contributes 6 dollars before packaging. What is contribution after packaging?', '4.50 dollars',
          ('6.00 dollars', 'ignored'), ('7.50 dollars', 'added'), ('1.50 dollars', 'packaging'), '6 - 1.50 = 4.50.', calc=lambda: 6 - 1.5 == 4.5),
        Q('Fancy packaging doubles cost but customers do not notice. What should the owner consider?', 'Whether the extra cost adds real value',
          ('Fancier is always better', 'not always'), ('Packaging cost never matters to profit', 'it does'), ('Remove all packaging', 'risky'),
          'Value for cost.'),
        Q('Which statement is accurate?', 'Good packaging balances protection and cost.',
          ('The cheapest packaging is always best.', 'not always'), ('Damage rate does not matter.', 'it does'),
          ('Testing packaging wastes time.', 'it helps'), 'Balance.'),
    ]))

# ------------------------------------------------------------------ Set 143: returns and fulfillment
FULFILL = ('FULFILLMENT is everything from order to delivery: picking the item, packing, labeling, shipping and confirming. '
           'Set a clear processing time (for example "ships in 2 business days") and meet it. RETURNS need a clear process: '
           'how customers request a return, the time limit, the condition required, who pays return shipping, and how quickly '
           'refunds are issued. Inspect returned items, restock what is sellable, and track return reasons to fix causes.')

s143 = SET('ENT.PROD.03',
    M=sec('Run a clear fulfillment and returns process', FULFILL, [
        Q('What is fulfillment?', 'Everything from order to delivery', ('Only the marketing before an order', 'no'),
          ('Only the tax filing after a sale', 'no'), ('Only the product photo', 'no'), 'Order to door.'),
        Q('What should a returns process state?', 'Request steps, time limit, condition, shipping and refund timing',
          ('Only the owner\'s phone number', 'incomplete'), ('Only that returns are possible', 'vague'),
          ('Nothing; returns are handled case by case, in secret, by the owner', 'unclear'), 'Full terms.'),
        Q('Why track return reasons?', 'To fix the causes of returns', ('To argue with customers', 'no'), ('To raise prices secretly', 'no'),
          ('Because reasons never matter', 'they do'), 'Improve.'),
        Q('What should happen to sellable returned items?', 'Inspect and restock them', ('Throw them all away', 'waste'),
          ('Sell them as new without checking', 'risky'), ('Keep them forever unopened', 'waste'), 'Recover value.'),
        Q('"Ships in 2 business days" is what kind of promise?', 'A processing time', ('A delivery guarantee from the carrier', 'different'),
          ('A refund policy', 'no'), ('A discount', 'no'), 'Handling time.'),
    ]),
    B=[cs('A library\'s checkout and return desk', 'A library has a clear checkout process and a clear return process: due dates, '
          'condition expectations, and what happens to books that come back damaged. Returned books are checked and put back '
          'on shelves. A product business needs the same two desks: one for getting orders out correctly and one for handling '
          'what comes back.', [
        Q('The checkout desk is like what?', 'Fulfillment', ('The return desk', 'other desk'), ('Marketing', 'no'), ('Taxes', 'no'),
          'Getting orders out.'),
        Q('The return desk is like what?', 'The returns process', ('Fulfillment of orders', 'other desk'), ('Hiring', 'no'), ('Pricing', 'no'),
          'Handling returns.'),
        Q('What happens to returned books?', 'They are checked and reshelved', ('They are thrown away at once', 'no'), ('They are hidden', 'no'),
          ('They are sold', 'no'), 'Inspect and restock.'),
        Q('Due dates are like what in returns?', 'The return time limit', ('The price', 'no'), ('The shipping label', 'no'),
          ('The product photo', 'no'), 'Time limit.'),
        Q('Why have clear rules at both desks?', 'So everyone knows what to expect', ('To confuse readers', 'no'), ('To charge late fines to readers only', 'no'),
          ('Rules are decoration', 'no'), 'Clarity.'),
    ], why='A learner who misses MAIN may not see both halves of the process; a library\'s two desks make it concrete.')],
    F1=sec('Apply it: improve fulfillment and returns', FULFILL, [
        Q('A shop promises 2-day processing but ships in 5. What should it change?', 'Meet the promise or change it to a realistic time',
          ('Keep the false promise', 'misleading'), ('Remove all shipping information from the site', 'unclear'), ('Blame the carrier always', 'not the cause'),
          'Honest processing time.'),
        Q('Of 60 returns, 36 say "too small." What percent cite size?', '60 percent', ('36 percent', 'count'), ('40 percent', 'others'),
          ('24 percent', 'difference'), '36 / 60 = 0.6.', calc=lambda: 36 / 60 == 0.6),
        Q('What fix best addresses "too small" returns?', 'A clearer size chart with measurements', ('Removing the return option entirely', 'harms trust'),
          ('Charging for every return', 'not the cause'), ('Ignoring the reason', 'no change'), 'Fix the cause.'),
        Q('Returned items: 40, of which 30 are sellable at 25 dollars. What value is recovered?', '750 dollars', ('1,000 dollars', 'all 40'),
          ('250 dollars', '10 items'), ('25 dollars', 'one'), '30 x 25 = 750.', calc=lambda: 30 * 25 == 750),
        Q('A customer asks where her order is. What step in fulfillment helps most?', 'Sending tracking when the order ships', ('Hiding tracking numbers', 'opposite'),
          ('Shipping without labels', 'impossible'), ('Waiting for her to ask a second time', 'slow'), 'Confirmations.'),
    ]),
    F2=sec('Handle the complications: peaks and abuse', FULFILL, [
        Q('Holiday orders triple and processing time slips. What should the shop do?', 'Update the stated processing time and add help',
          ('Keep the old promise and simply miss it', 'broken promise'), ('Stop taking orders without notice', 'abrupt'),
          ('Ship incomplete orders', 'poor'), 'Adjust and communicate.'),
        Q('Some customers return items clearly used. What should the policy include?', 'A condition requirement such as "unused, with tags"',
          ('No conditions at all', 'invites abuse'), ('A ban on all returns of any kind, for any reason', 'harms trust'), ('Public shaming', 'harmful'),
          'Clear condition.'),
        Q('Return shipping costs the shop 7 dollars per return on 50 returns. What is the total?', '350 dollars', ('57 dollars', 'added'),
          ('7 dollars', 'one'), ('3,500 dollars', 'extra zero'), '50 x 7 = 350.', calc=lambda: 50 * 7 == 350),
        Q('Refunds take 4 weeks and customers complain. What is a better practice?', 'Refund promptly after inspection, within a stated time',
          ('Take even longer', 'worse'), ('Refund only if customers complain at least twice', 'unfair'), ('Stop offering refunds secretly', 'deceptive'),
          'Prompt refunds.'),
        Q('Which statement is accurate?', 'Clear shipping and return rules build trust.',
          ('Return reasons are not useful.', 'they are'), ('Processing time promises can be ignored.', 'not true'),
          ('Returned items are always worthless.', 'often sellable'), 'Systems help.'),
    ]))

# ------------------------------------------------------------------ Set 144: choosing selling channels
SELL = ('A product can be sold through different CHANNELS: your own website, an online marketplace, local markets and fairs, '
        'wholesale to shops, or consignment. Each has different fees, reach and control. A marketplace may bring buyers but '
        'charges fees and sets rules; your own site gives control but you must bring the visitors; WHOLESALE sells in bulk at a '
        'lower price (often around half of retail) to stores that resell. Compare contribution per sale after channel costs.')

s144 = SET('ENT.PROD.04',
    M=sec('Compare selling channels by fees, reach and contribution', SELL, [
        Q('What is wholesale?', 'Selling in bulk at a lower price to stores that resell', ('Selling one item at full price online to a shopper', 'retail'),
          ('Giving items away for free', 'no'), ('Selling only at farmers markets', 'local retail'), 'Bulk to resellers.'),
        Q('What does an online marketplace usually provide?', 'Access to buyers, with fees and rules', ('Free sales with no rules', 'not true'),
          ('Full control of all customer data', 'not usually'), ('Guaranteed profits', 'no'), 'Reach with costs.'),
        Q('What is a tradeoff of your own website?', 'More control, but you must bring visitors', ('No control at all', 'opposite'),
          ('Visitors arrive automatically, with no work', 'not true'), ('No costs of any kind', 'not true'), 'Control versus reach.'),
        Q('A 40-dollar retail item sells wholesale at about half. What is the wholesale price?', '20 dollars', ('40 dollars', 'retail'),
          ('80 dollars', 'doubled'), ('10 dollars', 'quarter'), '40 / 2 = 20.', calc=lambda: 40 / 2 == 20),
        Q('What should be compared across channels?', 'Contribution per sale after channel costs', ('Only the logo on each channel', 'irrelevant'),
          ('Only how popular each channel is with sellers', 'incomplete'), ('Only the color scheme', 'irrelevant'), 'Money per sale.'),
    ]),
    B=[mathb('Contribution after channel fees', 'For each channel, contribution = price - product cost - channel fees. Fees may be a '
             'percent (marketplace commission) or a fixed amount (booth fee per item). Example: price 30, cost 12, marketplace fee '
             '15 percent (4.50): 30 - 12 - 4.50 = 13.50. Wholesale at 15 with cost 12: 3 dollars per unit but many units at once. Multiply by units to compare totals.', [
        Q('15 percent of 30 is what?', '4.50', ('15', 'percent'), ('0.45', 'moved decimal'), ('34.50', 'added'), '0.15 x 30 = 4.50.',
          calc=lambda: round(0.15 * 30, 2) == 4.5),
        Q('Price 30, cost 12, fee 4.50. What is the contribution?', '13.50', ('18.00', 'no fee'), ('25.50', 'no cost'), ('4.50', 'fee'),
          '30 - 12 - 4.50 = 13.50.', calc=lambda: round(30 - 12 - 4.5, 2) == 13.5),
        Q('Wholesale price 15, cost 12. What is the contribution per unit?', '3', ('15', 'price'), ('27', 'added'), ('12', 'cost'),
          '15 - 12 = 3.', calc=lambda: 15 - 12 == 3),
        Q('200 wholesale units at 3 dollars contribution. What is the total?', '600', ('203', 'added'), ('3', 'one'), ('66.67', 'divided'),
          '200 x 3 = 600.', calc=lambda: 200 * 3 == 600),
        Q('Price 25, cost 10, fee 20 percent. What is the contribution?', '10', ('15', 'no fee'), ('5', 'fee'), ('20', 'percent'),
          '25 - 10 - 5 = 10.', calc=lambda: 25 - 10 - 0.2 * 25 == 10),
    ], why='A learner who misses MAIN may compare channels by price alone; this practices contribution after fees.')],
    F1=sec('Apply it: compare channels for one product', SELL, [
        Q('A soap costs 3 dollars to make. Own site: price 10, fees 0.60. Marketplace: price 10, fees 1.80. What is the own-site contribution?',
          '6.40 dollars', ('5.20 dollars', 'marketplace'), ('7.00 dollars', 'no fees'), ('10.00 dollars', 'price'), '10 - 3 - 0.60 = 6.40.',
          calc=lambda: round(10 - 3 - 0.6, 2) == 6.4),
        Q('The own site sells 40 a month; the marketplace sells 150. Which brings more total contribution?', 'The marketplace, at 780 dollars',
          ('The own site, at 256 dollars', 'lower'), ('They are equal', 'differ'), ('The own site, at 400 dollars', 'miscalculated'),
          'Own: 40 x 6.40 = 256; marketplace: 150 x 5.20 = 780.', calc=lambda: round(40 * 6.4) == 256 and round(150 * 5.2) == 780),
        Q('A shop wants 300 soaps wholesale at 5 dollars each. What is the total contribution?', '600 dollars', ('1,500 dollars', 'revenue'),
          ('900 dollars', 'cost'), ('2,100 dollars', 'added'), '300 x (5 - 3) = 600.', calc=lambda: 300 * (5 - 3) == 600),
        Q('Which is a risk of relying only on one marketplace?', 'A rule or fee change can hurt sales suddenly', ('No risk, because marketplaces never change rules', 'they do'),
          ('Sales are guaranteed forever', 'no'), ('Fees always fall', 'no'), 'Platform risk.'),
        Q('A craft fair booth costs 80 dollars and she expects 40 sales at 7 dollars contribution each. What is the net?', '200 dollars',
          ('280 dollars', 'ignored booth'), ('80 dollars', 'booth'), ('360 dollars', 'added'), '40 x 7 - 80 = 200.', calc=lambda: 40 * 7 - 80 == 200),
    ]),
    F2=sec('Handle the complications: channel conflict and capacity', SELL, [
        Q('A store buying wholesale asks the maker not to sell cheaper online. What should she consider?', 'Keeping prices consistent across channels',
          ('Undercutting the store online anyway', 'harms partner'), ('Ignoring the request', 'damages relationship'),
          ('Raising wholesale prices secretly', 'unfair'), 'Channel consistency.'),
        Q('A large wholesale order would use all production for a month. What should she check?', 'Whether she can still serve her other channels',
          ('Nothing, because bigger orders are always better', 'not always'), ('Only the logo', 'irrelevant'), ('Only the store\'s decor', 'irrelevant'),
          'Capacity.'),
        Q('Marketplace fees rise from 12 to 18 percent on a 20-dollar item. How much more per sale in fees?', '1.20 dollars',
          ('6.00 dollars', 'percent as dollars'), ('3.60 dollars', 'new fee'), ('2.40 dollars', 'old fee'), '0.06 x 20 = 1.20.',
          calc=lambda: round(0.18 * 20 - 0.12 * 20, 2) == 1.2),
        Q('Consignment means the shop pays only when items sell. What is the main risk?', 'Unsold items tie up stock and cash', ('No risk at all', 'there is'),
          ('The shop pays twice', 'no'), ('Consigned items always sell instantly', 'no'), 'Delayed payment.'),
        Q('Which statement is accurate?', 'Channels differ in fees, reach and control, so compare them.',
          ('All channels earn the same per sale.', 'not true'), ('One channel is always enough.', 'risky'),
          ('Wholesale buyers always pay the full retail price.', 'not true'), 'Compare.'),
    ]))

# ------------------------------------------------------------------ Set 145: shipping costs and return addresses
SHIPC = ('Shipping cost depends on weight, package size (carriers may charge by DIMENSIONAL WEIGHT for large, light boxes), '
         'distance and speed. Weigh and measure packed items, compare carriers and services, and decide how to charge: '
         'customer pays actual shipping, a flat rate, free shipping built into prices, or free over a minimum order. Use a '
         'reliable RETURN ADDRESS on labels; a PO Box can work as a return address, while some carriers that need a street '
         'address may use a PO Box Street Addressing option where available.')

s145 = SET('ENT.PROD.05',
    M=sec('Estimate shipping costs, choose a pricing approach and set a return address', SHIPC, [
        Q('What can make a large, light box cost more to ship?', 'Dimensional weight pricing', ('Using a darker color tape', 'irrelevant'),
          ('Shipping on a Monday', 'not the factor'), ('Having a logo on the box', 'irrelevant'), 'Size-based pricing.'),
        Q('What is "free shipping built into prices"?', 'Raising product prices to cover shipping', ('The carrier ships for free', 'no'),
          ('Customers pay twice', 'no'), ('Shipping is removed from the business\'s costs', 'still a cost'), 'Cost is still paid.'),
        Q('Free shipping over 50 dollars. An order is 42 dollars. How much more to qualify?', '8 dollars', ('50 dollars', 'threshold'),
          ('42 dollars', 'order'), ('92 dollars', 'added'), '50 - 42 = 8.', calc=lambda: 50 - 42 == 8),
        Q('Can a PO Box be used as a return address?', 'Yes, it can work as a return address', ('No, never, under any carrier\'s rules', 'it can'),
          ('Only for international mail', 'no'), ('Only for large boxes', 'no'), 'Return addresses can be boxes.'),
        Q('Why weigh and measure packed items?', 'To estimate shipping cost accurately', ('To decorate the box', 'no'), ('Because carriers require photos', 'no'),
          ('To avoid any packaging', 'no'), 'Accurate costs.'),
    ]),
    B=[cs('Mailing a pillow versus a book', 'A pillow is light but big; a book is small but heavy. Carriers care about both, so a '
          'big pillow box can cost more than you expect. Choosing the smallest box that protects the item can lower cost. And '
          'the return address is like the "return to sender" note: it should go somewhere you reliably check.', [
        Q('Why can the pillow box cost a lot?', 'It is big even though it is light', ('Pillows are illegal to mail in boxes', 'no'),
          ('Pillows are heavy', 'no'), ('It has no address', 'no'), 'Size matters.'),
        Q('What can lower shipping cost?', 'The smallest box that still protects the item', ('The biggest box possible, for extra room', 'worse'),
          ('No box at all', 'risky'), ('Extra empty space', 'worse'), 'Right-size.'),
        Q('The book is small but what?', 'Heavy', ('Free', 'no'), ('Huge', 'no'), ('Light', 'no'), 'Weight matters.'),
        Q('The return address should go where?', 'Somewhere you reliably check', ('A random address you never visit', 'no'), ('Nowhere', 'no'),
          ('A competitor\'s shop', 'no'), 'Reliable returns.'),
        Q('Carriers price by what two things here?', 'Size and weight', ('Color and font', 'no'), ('Day and mood', 'no'),
          ('Logo and price', 'no'), 'Physical factors.'),
    ], why='A learner who misses MAIN may not see why size matters; mailing a pillow versus a book makes it concrete.')],
    F1=sec('Apply it: set shipping prices', SHIPC, [
        Q('Average shipping costs 7 dollars per order. Product price is 28. With free shipping built in, what price covers it?', '35 dollars',
          ('28 dollars', 'not covered'), ('21 dollars', 'subtracted'), ('7 dollars', 'shipping'), '28 + 7 = 35.', calc=lambda: 28 + 7 == 35),
        Q('A flat rate of 6 dollars is charged but average cost is 8.50. How much is lost per order?', '2.50 dollars', ('6.00 dollars', 'charged'),
          ('8.50 dollars', 'cost'), ('14.50 dollars', 'added'), '8.50 - 6 = 2.50.', calc=lambda: 8.5 - 6 == 2.5),
        Q('Over 300 orders, what does that shortfall cost?', '750 dollars', ('2.50 dollars', 'one'), ('302.50 dollars', 'added'),
          ('120 dollars', 'divided'), '300 x 2.50 = 750.', calc=lambda: 300 * 2.5 == 750),
        Q('A box measures large but the item is light. What could cut costs?', 'A smaller box that still protects it', ('A larger box with more space for safety', 'worse'),
          ('Adding weight', 'worse'), ('Removing the label', 'impossible'), 'Right-size.'),
        Q('A carrier needs a street address for returns, but the owner uses a PO Box. What might help where available?', 'PO Box Street Addressing',
          ('Using a fake street address', 'false'), ('Using a neighbor\'s address without asking', 'improper'),
          ('No return address at all', 'returns lost'), 'Official option.'),
    ]),
    F2=sec('Handle the complications: zones and rate changes', SHIPC, [
        Q('Shipping to far zones costs much more than nearby ones. What pricing approach handles this?', 'Charge actual shipping or zone-based rates',
          ('One tiny flat rate for every distance', 'loses money far'), ('Free shipping everywhere with no price change', 'loses money'),
          ('Refuse all far orders', 'loses sales'), 'Match cost.'),
        Q('Carrier rates rise 8 percent on an average 9-dollar label. What is the new average?', '9.72 dollars', ('9.08 dollars', 'added 0.08'),
          ('0.72 dollars', 'increase'), ('17 dollars', 'added 8'), '9 x 1.08 = 9.72.', calc=lambda: round(9 * 1.08, 2) == 9.72),
        Q('Free-over-50 raised average order size from 38 to 52 dollars. Shipping costs 8. What changed in revenue per order before shipping?', '14 dollars more',
          ('8 dollars more', 'shipping'), ('52 dollars more', 'new total'), ('No change', 'it rose'), '52 - 38 = 14.', calc=lambda: 52 - 38 == 14),
        Q('Returns arrive at an old address the owner no longer checks. What should she do?', 'Update the return address on labels and accounts',
          ('Ignore lost returns', 'harms customers'), ('Stop accepting any returns from customers', 'harms trust'), ('Use a fake address', 'false'),
          'Keep it current.'),
        Q('Which statement is accurate?', 'Size, weight, distance and speed set shipping costs.',
          ('Shipping is always free for sellers.', 'not true'), ('Box size never affects the shipping cost at all.', 'it can'),
          ('Return addresses do not matter.', 'they do'), 'Plan shipping.'),
    ]))

SETS = [s136, s137, s138, s139, s140, s141, s142, s143, s144, s145]
