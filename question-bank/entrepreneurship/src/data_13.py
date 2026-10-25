"""Entrepreneurship sets 69-76: Foundation 9, getting paid and handling payment problems.
All names are fictional; prices are practice assumptions."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 69: quotes and proposals
QUOTE = ('A QUOTE (or estimate) tells a customer what a job will cost before work begins. A PROPOSAL adds more detail: '
         'the problem, what you will deliver, the timeline, the price and the terms. A clear quote lists what IS '
         'included and what is NOT, how long the price is valid (for example 30 days), and any deposit required. Build '
         'the price from your costs and time, not from a guess. Vague quotes ("about 500, maybe more") lead to arguments '
         'later.')

s69 = SET('ENT.PAY.01',
    M=sec('Write a clear quote with inclusions, exclusions and validity', QUOTE, [
        Q('What does a quote tell a customer?', 'What a job will cost before work begins',
          ('How much the business paid for its last tax return', 'unrelated'),
          ('Which competitor charges the lowest price nearby', 'not a quote'),
          ('How many hours the owner slept last week', 'unrelated'), 'A quote prices the job in advance.'),
        Q('What should a clear quote state about scope?', 'What is included and what is not',
          ('Only the price, with no description of the work at all', 'too vague'),
          ('Only the owner\'s years of experience in the field', 'not scope'),
          ('A promise that every extra will be free of charge', 'risky'), 'Scope prevents disputes.'),
        Q('What does "valid for 30 days" mean on a quote?', 'The price holds for 30 days',
          ('The work must be finished within 30 minutes', 'not the meaning'),
          ('The customer pays 30 percent more after accepting', 'not the meaning'),
          ('The quote can never be accepted after the first day', 'not the meaning'), 'Validity sets a time limit.'),
        Q('How should the price in a quote be built?', 'From costs and time', ('From a quick guess on the spot', 'unreliable'),
          ('From whatever a friend charged years ago', 'unrelated costs'), ('From the customer\'s budget alone', 'may not cover costs'),
          'Costs and time drive price.'),
        Q('What does a proposal usually add beyond a quote?', 'The problem, deliverables and timeline',
          ('A list of the owner\'s favorite hobbies and interests', 'irrelevant'),
          ('A copy of the owner\'s personal bank statements', 'private'),
          ('Nothing at all; they are always identical', 'proposals add detail'), 'Proposals give fuller detail.'),
    ]),
    B=[cs('A restaurant menu with a clear price', 'A good menu says "Burger with fries, 12 dollars; cheese is 1 dollar extra." '
          'You know what you get and what costs more. A bad menu says "Food, about 10, maybe more." A quote should read '
          'like the good menu: what is included, what is extra, and the price, so nobody is surprised when the bill '
          'arrives.', [
        Q('Which menu line is clearer?', '"Burger with fries, 12 dollars; cheese 1 dollar extra"', ('"Food, about 10 dollars, maybe more, depending on the day"', 'vague'),
          ('"Ask the cook what it costs"', 'vague'), ('"Prices change every hour"', 'vague'), 'Clear items and prices.'),
        Q('"Cheese 1 dollar extra" is like what in a quote?', 'An item not included in the base price',
          ('A free gift for every customer who orders', 'not free'), ('A tax on all food', 'not tax'), ('A discount', 'not a discount'),
          'Extras are listed separately.'),
        Q('Why is "about 10, maybe more" a problem?', 'The customer cannot know the final price', ('It is always cheaper', 'not known'),
          ('It is required by law', 'no'), ('It makes the cooking go faster in the kitchen', 'unrelated'), 'Vague prices cause disputes.'),
        Q('A clear quote should read like what?', 'The good menu', ('The bad menu', 'vague'), ('A blank page', 'empty'),
          ('A shopping list', 'not priced'), 'Clear and specific.'),
        Q('What does a clear menu prevent?', 'Surprises when the bill arrives', ('Customers ordering food at all', 'no'),
          ('The cook working', 'no'), ('Taxes being paid', 'no'), 'Clarity prevents surprises.'),
    ], why='A learner who misses MAIN may not see what makes a quote clear; a good and bad menu show the difference.')],
    F1=sec('Apply it: build and improve a quote', QUOTE, [
        Q('A painter estimates 12 hours at 40 dollars an hour plus 180 dollars of paint. What should the quote total be?',
          '660 dollars', ('480 dollars', 'labor only'), ('220 dollars', 'added hours and rate'), ('180 dollars', 'paint only'),
          '12 x 40 + 180 = 660.', calc=lambda: 12 * 40 + 180 == 660),
        Q('Which quote is clearest?', '"Paint 2 bedrooms, walls only, 660 dollars, valid 30 days"',
          ('"Painting, around 600 or so, and we will see about the rest later"', 'vague'),
          ('"Whatever you think is fair for the painting"', 'no price'),
          ('"Rooms painted, price depends on my mood"', 'vague'), 'Scope, price and validity.'),
        Q('A client asks whether ceilings are included. The quote said "walls only." What does the quote show?', 'Ceilings are not included',
          ('Ceilings are included at no extra charge', 'quote says walls only'), ('The whole house is included', 'not stated'),
          ('The quote is no longer valid', 'still valid'), 'Exclusions answer the question.'),
        Q('A quote requires a 30 percent deposit on 660 dollars. How much is the deposit?', '198 dollars', ('30 dollars', 'percent as dollars'),
          ('462 dollars', 'remainder'), ('220 dollars', 'one third'), '0.30 x 660 = 198.', calc=lambda: round(0.30 * 660, 2) == 198),
        Q('A customer accepts a quote 45 days after it was sent; it was valid for 30 days and paint prices rose. What may the '
          'owner do?', 'Update the quote, since the validity period passed', ('Honor any old price forever', 'validity expired'),
          ('Refuse to speak to the customer', 'unnecessary'), ('Double the price without any explanation to the customer', 'unfair'),
          'Validity periods allow updating.'),
    ]),
    F2=sec('Handle the complications: underquoting and pressure', QUOTE, [
        Q('An owner quoted 400 dollars, then realized the job will take twice as long as planned. What is a fair approach?',
          'Explain early and agree on any change before doing extra work', ('Quietly do half the work', 'dishonest'),
          ('Charge 800 dollars at the end without any warning to the client', 'surprise'), ('Abandon the job without notice', 'harmful'),
          'Communicate before proceeding.'),
        Q('A client pressures for a quote on the spot without details. What is the best response?', 'Ask questions or give a range with clear assumptions',
          ('Give a firm low number right away just to win the job', 'risky'), ('Refuse to ever quote', 'loses business'),
          ('Promise unlimited work for one price', 'risky'), 'Assumptions protect both sides.'),
        Q('A quote omitted travel time; travel adds 3 hours at 40 dollars. How much was underquoted?', '120 dollars',
          ('43 dollars', 'added'), ('40 dollars', 'one hour'), ('13 dollars', 'divided'), '3 x 40 = 120.', calc=lambda: 3 * 40 == 120),
        Q('Two quotes for the same job: one 30 percent cheaper with no scope listed. What should a customer consider?', 'What is actually included',
          ('Only the lower number', 'ignores scope'), ('Only the company logo', 'irrelevant'), ('Nothing else', 'scope matters'),
          'Price without scope is hard to compare.'),
        Q('Which statement is accurate?', 'A clear quote protects both the customer and the business.',
          ('Vague quotes help businesses charge more fairly in the long run.', 'cause disputes'), ('Quotes are never binding in any way.', 'can be relied on'),
          ('Exclusions should be hidden.', 'should be clear'), 'Clarity builds trust.'),
    ]))

# ------------------------------------------------------------------ Set 70: payment terms in writing
TERMS = ('PAYMENT TERMS say when and how the customer will pay. Write them in the quote or contract before work starts: '
         'the deposit amount, when the balance is due (for example "due on completion" or "Net 15"), accepted payment '
         'methods, and any late fee if allowed where you operate. For larger jobs, MILESTONE payments split the price into '
         'parts paid at stages, such as 30 percent to start, 40 percent at the midpoint, 30 percent at the end.')

s70 = SET('ENT.PAY.02',
    M=sec('Set payment terms and milestone payments in writing', TERMS, [
        Q('When should payment terms be written down?', 'Before work starts', ('After the customer refuses to pay', 'too late'),
          ('Only if the job is under 10 dollars', 'all jobs benefit'), ('Never; spoken promises are always enough', 'risky'),
          'Agree terms up front.'),
        Q('What are milestone payments?', 'Payments split into parts at stages of a job',
          ('A single payment made a year after the job', 'not milestones'),
          ('A fee for driving past a mile marker', 'pun'),
          ('A discount for paying in cash only', 'not milestones'), 'Milestones split the price.'),
        Q('A 5,000-dollar job uses 30/40/30 milestones. How much is due at the midpoint?', '2,000 dollars',
          ('1,500 dollars', 'first or last part'), ('3,000 dollars', 'too much'), ('5,000 dollars', 'all'),
          '0.40 x 5,000 = 2,000.', calc=lambda: 0.40 * 5000 == 2000),
        Q('Which item belongs in payment terms?', 'Accepted payment methods', ('The owner\'s favorite song', 'irrelevant'),
          ('The customer\'s home décor style', 'irrelevant'), ('A list of competitors', 'irrelevant'), 'Methods are part of terms.'),
        Q('Before adding a late fee to terms, what should be checked?', 'Whether it is allowed where you operate',
          ('Whether customers will like it', 'not the rule'), ('Whether it rhymes with the business name', 'irrelevant'),
          ('Nothing; any fee is always allowed', 'rules vary'), 'Late fees must be lawful.'),
    ]),
    B=[mathb('Splitting a total by percentages', 'To split a total into milestone payments, multiply the total by each '
             'percent. The percents must add up to 100. Example: 2,000 dollars at 25/50/25 gives 0.25 x 2,000 = 500, '
             '0.50 x 2,000 = 1,000, and 500. Check: 500 + 1,000 + 500 = 2,000. If the parts do not add up to the total, '
             'a percent is wrong.', [
        Q('What is 25 percent of 4,000?', '1,000', ('250', 'moved decimal'), ('3,000', 'remainder'), ('4,025', 'added'),
          '0.25 x 4,000 = 1,000.', calc=lambda: 0.25 * 4000 == 1000),
        Q('Do 30, 40 and 30 percent add to 100?', 'Yes', ('No, they add to 90', 'miscounted'), ('No, they add to 110', 'miscounted'),
          ('No, they add to 70', 'miscounted'), '30 + 40 + 30 = 100.', calc=lambda: 30 + 40 + 30 == 100),
        Q('1,200 at 50/50. What is each payment?', '600', ('1,200', 'all'), ('500', 'guessed'), ('50', 'percent as number'),
          '0.50 x 1,200 = 600.', calc=lambda: 0.5 * 1200 == 600),
        Q('A plan says 20/30/40 percent. What is wrong?', 'The parts add to only 90 percent', ('Nothing is wrong at all', 'missing 10'),
          ('The parts add to 110 percent', 'miscounted'), ('Percents cannot be used', 'they can'), '20 + 30 + 40 = 90.',
          calc=lambda: 20 + 30 + 40 == 90),
        Q('3,000 at 40/60. What is the second payment?', '1,800', ('1,200', 'first payment'), ('600', 'difference'),
          ('3,000', 'all'), '0.60 x 3,000 = 1,800.', calc=lambda: 0.6 * 3000 == 1800),
    ], why='A learner who misses MAIN may not split a total by percentages; this practices it with a check.')],
    F1=sec('Apply it: choose terms for a job', TERMS, [
        Q('A web designer takes an 8-week, 6,000-dollar project and must buy software licenses at the start. Which terms fit?',
          'A deposit up front with milestone payments', ('Full payment 90 days after finishing', 'cash strain'),
          ('No written terms, just trust', 'risky'), ('Payment only if the client is fully happy, someday', 'vague'),
          'Deposits and milestones match costs to timing.'),
        Q('Terms: 25 percent deposit, balance due on completion, for a 2,400-dollar job. What is the balance?', '1,800 dollars',
          ('600 dollars', 'deposit'), ('2,400 dollars', 'all'), ('2,375 dollars', 'subtracted 25'), '2,400 - 600 = 1,800.',
          calc=lambda: 2400 - 0.25 * 2400 == 1800),
        Q('A client wants to pay by a method the business does not accept. What helps avoid this?', 'Listing accepted methods in the terms',
          ('Accepting any method a stranger suggests', 'risky'), ('Refusing to say how to pay', 'confusing'),
          ('Changing methods after the work is done', 'confusing'), 'Clear methods up front.'),
        Q('Which written term is clearest?', '"Balance due within 15 days of the invoice date by bank transfer or card"',
          ('"Pay whenever you can, I guess, by however works best for you"', 'vague'), ('"Payment expected at some point soon"', 'vague'),
          ('"We will talk about money later on"', 'vague'), 'Specific timing and method.'),
        Q('A 3,000-dollar project at 30/40/30: the client paid the deposit and the midpoint. How much is still owed?', '900 dollars',
          ('2,100 dollars', 'amount paid'), ('1,200 dollars', 'midpoint'), ('3,000 dollars', 'all'), '0.30 x 3,000 = 900.',
          calc=lambda: 3000 - (900 + 1200) == 900),
    ]),
    F2=sec('Handle the complications: unpaid milestones and changing terms', TERMS, [
        Q('A client has not paid the midpoint milestone but wants the next phase started. What does good practice suggest?',
          'Pause the next phase until the milestone is paid, as the terms say', ('Start the next phase anyway and simply hope the missing payment comes later', 'risky'),
          ('Delete the client\'s files', 'harmful'), ('Double the price as punishment', 'unfair'), 'Follow agreed terms.'),
        Q('A client asks to change terms from Net 15 to Net 60 after signing. What should the owner do?', 'Decide whether to agree, and put any change in writing',
          ('Agree verbally and change nothing in the written terms', 'unclear'), ('Accept every request automatically', 'may harm cash'),
          ('Stop all communication', 'harmful'), 'Written changes avoid confusion.'),
        Q('Terms say a 1.5 percent monthly late fee (where allowed). A 1,000-dollar balance is 2 months late. What is the simple '
          'total of the fees?', '30 dollars', ('15 dollars', 'one month'), ('300 dollars', 'used 15 percent'), ('3 dollars', 'moved decimal'),
          '0.015 x 1,000 x 2 = 30.', calc=lambda: round(0.015 * 1000 * 2, 2) == 30),
        Q('An owner forgot to write terms and the client pays 75 days later. What lesson applies?', 'Put terms in writing before starting',
          ('Never work for clients again', 'overreaction'), ('Clients always pay on time', 'not true'),
          ('Terms only matter for big companies', 'all benefit'), 'Written terms set expectations.'),
        Q('Which statement is accurate?', 'Clear written terms make late payments less likely and easier to address.',
          ('Written terms guarantee that every single client will always pay early.', 'no guarantee'), ('Milestones are illegal for small jobs.', 'not true'),
          ('Late fees are allowed everywhere.', 'rules vary'), 'Terms help but do not guarantee.'),
    ]))

# ------------------------------------------------------------------ Set 71: cancellations, refunds, expectations
CANCEL = ('A CANCELLATION POLICY says what happens if a customer cancels: for example, "full refund if cancelled 7 days '
          'before; 50 percent refund within 7 days; no refund within 24 hours." Policies protect your time, because a '
          'last-minute cancellation leaves a slot you may not fill. Set EXPECTATIONS too: what the customer will receive, '
          'when, and how to contact you. Share the policy before booking, apply it consistently, and allow exceptions '
          'only on purpose, such as emergencies.')

s71 = SET('ENT.PAY.03',
    M=sec('Write and apply a fair cancellation policy', CANCEL, [
        Q('Why have a cancellation policy?', 'Last-minute cancellations leave slots you may not fill',
          ('To stop customers from ever booking again', 'not the purpose'),
          ('Because the law requires the same policy everywhere', 'not a rule'),
          ('To avoid writing any expectations at all', 'opposite'), 'It protects the owner\'s time.'),
        Q('Using the example policy, a 200-dollar booking is cancelled 3 days before. What is refunded?', '100 dollars',
          ('200 dollars', 'full refund window'), ('0 dollars', 'within 24 hours only'), ('50 dollars', 'quarter'),
          '50 percent of 200 = 100.', calc=lambda: 0.5 * 200 == 100),
        Q('When should the policy be shared?', 'Before booking', ('Only after a cancellation happens', 'too late'),
          ('Only to customers who complain', 'inconsistent'), ('Never; it is private', 'customers need it'), 'Share it first.'),
        Q('What does applying a policy consistently mean?', 'Treating similar cases the same way',
          ('Changing the rules for every customer randomly', 'inconsistent'),
          ('Ignoring the policy whenever it is inconvenient', 'inconsistent'),
          ('Applying it only to new customers', 'inconsistent'), 'Consistency is fair.'),
        Q('Which is a reasonable planned exception?', 'A documented emergency', ('A customer who is simply bored', 'not an emergency'),
          ('A friend of a friend asking nicely', 'not planned'), ('Anyone who complains loudly', 'not planned'),
          'Exceptions should be deliberate.'),
    ]),
    B=[cs('Saving a seat at a show', 'When you buy a theater ticket, the theater holds a seat for you and turns other people '
          'away. If you cancel an hour before, the seat is probably empty. That is why tickets often have rules about '
          'refunds. A service business is similar: an appointment holds a slot of the owner\'s time. A cancellation policy '
          'is the ticket rules for that slot.', [
        Q('A booked appointment is like what?', 'A seat held at a show', ('A free gift for coming', 'no'), ('A tax', 'no'), ('A coupon', 'no'),
          'It reserves a slot.'),
        Q('Why do late cancellations hurt the theater?', 'The seat is probably left empty', ('The empty seat gets bigger', 'no'),
          ('The show gets longer', 'no'), ('Tickets become free', 'no'), 'Lost sales.'),
        Q('A cancellation policy is like what?', 'Ticket refund rules', ('A menu', 'no'), ('A map', 'no'), ('A cooking recipe', 'no'),
          'Rules for refunds.'),
        Q('What does the theater do when it holds your seat?', 'Turns other people away', ('Sells it twice to two people', 'no'),
          ('Gives it away', 'no'), ('Closes early', 'no'), 'Holding a seat has a cost.'),
        Q('For a service business, the "seat" is what?', 'A slot of the owner\'s time', ('A chair in the waiting lobby', 'too literal'),
          ('A product on a shelf', 'no'), ('A parking spot', 'no'), 'Time is the reserved resource.'),
    ], why='A learner who misses MAIN may not see why cancellations cost money; a held theater seat shows it.')],
    F1=sec('Apply it: apply the policy to cases', CANCEL, [
        Q('Policy: full refund 7+ days before; 50 percent within 7 days; none within 24 hours. A 300-dollar session is cancelled '
          '12 hours before. What is refunded?', '0 dollars', ('150 dollars', '50 percent window'), ('300 dollars', 'full window'),
          ('75 dollars', 'quarter'), 'Within 24 hours: no refund.', calc=lambda: 300 * 0 == 0),
        Q('Policy: full refund 7+ days before; 50 percent within 7 days; none within 24 hours. A 300-dollar booking is cancelled 10 days before. What is refunded?',
          '300 dollars',
          ('150 dollars', '50 percent window'), ('0 dollars', 'too late window'),
          ('30 dollars', 'misread'),
          '7+ days: full refund.'),
        Q('A photographer loses 4 late-cancelled sessions a month at 150 dollars each. How much income is at risk without a '
          'policy?', '600 dollars', ('150 dollars', 'one session'), ('154 dollars', 'added'), ('37.50 dollars', 'divided'),
          '4 x 150 = 600.', calc=lambda: 4 * 150 == 600),
        Q('Which expectation statement is clearest?', '"You will receive 20 edited photos within 10 days by email."',
          ('"You will get some photos at some point."', 'vague'), ('"Photos come whenever they are ready, eventually, by some method."', 'vague'),
          ('"Ask me later about what you get."', 'vague'), 'Specific deliverables and timing.'),
        Q('A customer cancels because of a hospital emergency 6 hours before. The policy allows emergency exceptions. What fits?',
          'Apply the planned exception', ('Refuse because rules are rules', 'policy allows exception'),
          ('Charge double for the trouble', 'unfair'), ('Ignore the message', 'harmful'), 'Use the planned exception.'),
    ]),
    F2=sec('Handle the complications: disputes and repeat cancellations', CANCEL, [
        Q('A customer says she never saw the policy. What prevents this next time?', 'Requiring a checkbox or signature showing the policy was read',
          ('Hiding the policy in tiny text at the very bottom of the site', 'worse'), ('Never having a policy at all', 'no protection'),
          ('Changing the policy after booking', 'unfair'), 'Proof of agreement.'),
        Q('One client cancels late every month. What is a reasonable step?', 'Require a nonrefundable deposit for that client\'s bookings',
          ('Keep giving that client full refunds forever, no matter what', 'continued losses'), ('Insult the client online', 'harmful'),
          ('Stop working entirely', 'overreaction'), 'Deposits protect the slot.'),
        Q('A 50 percent refund was promised but the owner refunds only 30 percent of 200 dollars. How much is still owed to the '
          'customer?', '40 dollars', ('60 dollars', 'what was refunded'), ('100 dollars', 'promised amount'), ('140 dollars', 'remainder'),
          'Promised 100; refunded 60; owed 40.', calc=lambda: 0.5 * 200 - 0.3 * 200 == 40),
        Q('Local consumer rules may override parts of a policy. What should the owner do?', 'Check the rules where she operates',
          ('Assume her policy always wins', 'may not'), ('Copy another state\'s policy', 'different rules'),
          ('Ignore the rules', 'risky'), 'Policies must follow law.'),
        Q('Which statement is accurate?', 'A clear policy shared in advance prevents many disputes.',
          ('Policies cause more disputes than they prevent.', 'not usually'), ('Exceptions should be random.', 'should be planned'),
          ('Refunds are never required.', 'rules vary'), 'Clarity reduces conflict.'),
    ]))

# ------------------------------------------------------------------ Set 72: scope changes
SCOPE = ('SCOPE is the work agreed in the quote or contract. SCOPE CREEP happens when extra requests keep being added '
         'without changing the price or timeline. Handle changes with a short CHANGE ORDER: a written note describing the '
         'new request, its added cost and time, approved by the customer before you start it. Small favors can be fine, '
         'but decide on purpose. Uncontrolled scope creep turns a profitable job into a loss.')

s72 = SET('ENT.PAY.04',
    M=sec('Recognize scope creep and handle changes with a change order', SCOPE, [
        Q('What is scope creep?', 'Extra requests added without changing price or time',
          ('A slow increase in the business\'s advertising budget', 'not scope creep'),
          ('A customer paying an invoice a little early', 'not scope creep'),
          ('A supplier raising prices every year', 'not scope creep'), 'Unpriced extras pile up.'),
        Q('What is a change order?', 'A written note of a new request with its cost and time',
          ('A new order of supplies placed with a wholesaler', 'not this meaning'),
          ('A refund paid when a customer cancels', 'not this meaning'),
          ('An order to change the company name', 'not this meaning'), 'It records approved changes.'),
        Q('When should the customer approve a change order?', 'Before the extra work starts', ('After the work is finished', 'too late'),
          ('Never; approval is not needed', 'needed'), ('Only if the change is free', 'all changes'), 'Approve first.'),
        Q('A 1,000-dollar job took 20 hours. Scope creep added 10 unpaid hours. What happened to the hourly earnings?', 'They fell by one third',
          ('They doubled because more work was done', 'no extra pay'), ('They stayed exactly the same', 'more hours'),
          ('They rose by 10 dollars an hour', 'no'), '50 an hour before; about 33 an hour after.',
          calc=lambda: round(1000 / 30, 2) == 33.33 and 1000 / 20 == 50),
        Q('Are small favors ever acceptable?', 'Yes, when decided on purpose', ('No, never under any circumstances', 'can be fine'),
          ('Yes, always, for every request', 'creep'), ('Only for strangers', 'arbitrary'), 'Intentional favors are a choice.'),
    ]),
    B=[cs('Adding rooms to a house plan', 'Imagine hiring a builder for a 2-room addition. Halfway through, you ask for a third '
          'room "while you\'re at it." A good builder writes down the extra room, its extra cost and extra time, and asks '
          'you to sign before starting. Without that note, the builder works for free or you get a surprise bill. A change '
          'order is that signed note.', [
        Q('The third room is like what?', 'A scope change', ('The original plan', 'no'), ('A discount', 'no'), ('A tax', 'no'),
          'It is extra work.'),
        Q('What does a good builder write down?', 'The extra room, cost and time', ('Nothing', 'no'), ('Only the color', 'incomplete'),
          ('Only the start date of the room', 'incomplete'), 'A change order captures it.'),
        Q('Without a written note, what can happen?', 'Free work or a surprise bill', ('Nothing at all', 'problems'),
          ('Faster building by the crew', 'no'), ('Lower taxes', 'no'), 'Unclear changes cause conflict.'),
        Q('When does the customer sign?', 'Before the extra room is started', ('After it is built', 'too late'),
          ('Never', 'needed'), ('Only when it rains on the site', 'no'), 'Approve first.'),
        Q('The signed note is called what?', 'A change order', ('A store receipt', 'no'), ('A license', 'no'), ('A deed', 'no'),
          'It authorizes the change.'),
    ], why='A learner who misses MAIN may not picture how a change is handled; adding a room to a plan shows the steps.')],
    F1=sec('Apply it: write change orders', SCOPE, [
        Q('A designer agreed to 3 logo concepts for 900 dollars. The client asks for 2 more. Each concept takes 4 hours at 50 '
          'dollars. What should the change order add?', '400 dollars', ('200 dollars', 'one concept'), ('900 dollars', 'original'),
          ('100 dollars', 'hours only'), '2 x 4 x 50 = 400.', calc=lambda: 2 * 4 * 50 == 400),
        Q('Which change order is clearest?', '"Add 2 logo concepts, 400 dollars, 4 extra days. Approved: ____"',
          ('"Some more stuff added, and we will figure out the cost later"', 'vague'), ('"Extra work, maybe extra money, maybe not"', 'vague'),
          ('"Will do it, do not worry about cost"', 'unpriced'), 'Specific, priced and approved.'),
        Q('A client says "Can you just quickly add a page?" to a website contract. What is the best first step?', 'Explain it is outside scope and offer a change order',
          ('Add it silently for free each time the client asks', 'creep'), ('Refuse to talk about it', 'unhelpful'),
          ('Charge without telling the client', 'surprise'), 'Name the change and price it.'),
        Q('An original job is 2,000 dollars and change orders add 300 and 150 dollars. What is the new total?', '2,450 dollars',
          ('2,300 dollars', 'missed one'), ('2,150 dollars', 'missed one'), ('450 dollars', 'changes only'),
          '2,000 + 300 + 150 = 2,450.', calc=lambda: 2000 + 300 + 150 == 2450),
        Q('A tiny change takes 5 minutes, and the owner chooses to do it free. What makes this healthy rather than creep?',
          'She decided on purpose and tells the client it is a courtesy', ('She hides it and hopes', 'unclear'),
          ('She does every request the client makes for free, always', 'creep'), ('She charges double later', 'surprise'), 'Intentional and communicated.'),
    ]),
    F2=sec('Handle the complications: blurred lines and pushback', SCOPE, [
        Q('A contract says "website design" with no details. Every request seems in scope to the client. What was missing?',
          'A clear list of what is included', ('A bigger logo on the contract', 'irrelevant'), ('A lower price', 'not the issue'),
          ('A longer timeline only', 'not the issue'), 'Vague scope invites creep.'),
        Q('A client refuses to pay for a change order she approved in writing. What supports the owner?', 'The signed change order',
          ('A memory of a phone call', 'weak'), ('A social media post', 'weak'), ('Nothing; approvals do not matter', 'they do'),
          'Written approval is evidence.'),
        Q('Scope creep added 15 hours to a job priced for 30 hours at an effective 40 dollars an hour. What is the new effective '
          'rate, to the nearest cent?', '26.67 dollars an hour', ('40.00 dollars an hour', 'ignored creep'),
          ('20.00 dollars an hour', 'doubled hours'), ('60.00 dollars an hour', 'wrong direction'), '1,200 / 45 = 26.67.',
          calc=lambda: round(30 * 40 / 45, 2) == 26.67),
        Q('A request changes the deadline but not the work. Does it need a change order?', 'Yes, timeline changes should be written too',
          ('No, only changes to the price ever matter', 'time matters'), ('No, deadlines never change', 'they can'),
          ('Only if the client is new', 'all clients'), 'Scope includes time.'),
        Q('Which statement is accurate?', 'Written change orders protect profit and the relationship.',
          ('Change orders insult clients.', 'they clarify'), ('Scope creep always helps profit.', 'hurts it'),
          ('Only large companies with big contracts need change orders.', 'all benefit'), 'Clarity helps everyone.'),
    ]))

# ------------------------------------------------------------------ Set 73: subscriptions and recurring billing
SUB = ('A SUBSCRIPTION charges a customer on a schedule, such as monthly, until cancelled. Clear subscription terms state '
       'the price, how often it is charged, when renewal happens, how to cancel, and what happens after a free trial. '
       'Make cancelling easy and honest; hidden or difficult cancellation can break consumer rules and destroys trust. '
       'Plan for FAILED PAYMENTS (expired cards) with reminders. CHURN is the share of subscribers who cancel in a '
       'period; high churn means you must keep finding new customers.')

s73 = SET('ENT.PAY.05',
    M=sec('Set clear subscription terms and read churn', SUB, [
        Q('What should subscription terms state?', 'Price, frequency, renewal and how to cancel',
          ('Only the price, with no word about cancelling', 'incomplete'),
          ('Only the company\'s history and mission', 'not terms'),
          ('Only the founder\'s name and photo', 'not terms'), 'Complete terms build trust.'),
        Q('What is churn?', 'The share of subscribers who cancel in a period',
          ('The number of new products launched each year', 'not churn'),
          ('The speed of the website checkout page', 'not churn'),
          ('The price increase each month', 'not churn'), 'Churn measures cancellations.'),
        Q('A service has 200 subscribers and 10 cancel this month. What is the monthly churn?', '5 percent',
          ('10 percent', 'used count as percent'), ('20 percent', 'divided wrongly'), ('2 percent', 'moved decimal'),
          '10 / 200 = 0.05.', calc=lambda: 10 / 200 == 0.05),
        Q('Why make cancelling easy?', 'Hard cancellation can break rules and destroys trust',
          ('Easy cancelling always doubles the number of subscribers', 'not guaranteed'),
          ('Because subscriptions are illegal', 'they are legal'), ('To avoid ever sending reminders', 'unrelated'),
          'Honest cancellation is expected.'),
        Q('What is a common cause of failed payments?', 'Expired cards', ('Customers liking the product too much', 'no'),
          ('Too many reminders being sent', 'no'), ('The logo changing color', 'no'), 'Cards expire.'),
    ]),
    B=[mathb('Monthly totals and percent lost', 'Recurring revenue = subscribers x monthly price. If you have 150 subscribers '
             'at 12 dollars, that is 150 x 12 = 1,800 dollars a month. Churn percent = cancellations / starting subscribers. '
             'If 6 of 150 cancel, 6 / 150 = 0.04 = 4 percent. Losing subscribers lowers next month\'s revenue: 144 x 12 = 1,728. That is 72 dollars less every month.', [
        Q('100 subscribers at 15 dollars. What is monthly revenue?', '1,500', ('115', 'added'), ('150', 'moved decimal'),
          ('15,000', 'extra zero'), '100 x 15 = 1,500.', calc=lambda: 100 * 15 == 1500),
        Q('8 of 200 cancel. What is churn?', '4 percent', ('8 percent', 'count'), ('25 percent', 'reversed'), ('0.4 percent', 'moved decimal'),
          '8 / 200 = 0.04.', calc=lambda: 8 / 200 == 0.04),
        Q('After 6 of 150 cancel, how many remain?', '144', ('156', 'added'), ('6', 'cancelled'), ('150', 'start'),
          '150 - 6 = 144.', calc=lambda: 150 - 6 == 144),
        Q('144 subscribers at 12 dollars. What is revenue?', '1,728', ('1,800', 'old count'), ('156', 'added'), ('12', 'price'),
          '144 x 12 = 1,728.', calc=lambda: 144 * 12 == 1728),
        Q('Churn is calculated by dividing cancellations by what?', 'Starting subscribers', ('New subscribers that month', 'wrong base'),
          ('The price', 'wrong base'), ('Revenue', 'wrong base'), 'Use the starting count.'),
    ], why='A learner who misses MAIN may not compute churn or recurring revenue; this practices both.')],
    F1=sec('Apply it: evaluate a subscription plan', SUB, [
        Q('A box costs 25 dollars a month; 300 subscribers; 6 percent churn. About how many cancel this month?', '18',
          ('6', 'percent as count'), ('50', 'divided wrongly'), ('282', 'remaining'), '0.06 x 300 = 18.', calc=lambda: round(0.06 * 300) == 18),
        Q('Which terms are clearest?', '"14 dollars a month, renews monthly, cancel anytime in your account."',
          ('"Small monthly fee, terms may apply somewhere."', 'vague'), ('"Free! (Charges later, see fine print.)"', 'hidden'),
          ('"Call us during weekday business hours to discuss cancelling your plan."', 'harder than needed'), 'Price, renewal, cancel method.'),
        Q('A free 7-day trial converts to 20 dollars a month. What must customers be told before signing up?', 'That they will be charged after the trial unless they cancel',
          ('Nothing, because surprise charges are good for sales', 'harms trust'), ('Only the trial length', 'incomplete'),
          ('Only the company\'s address', 'incomplete'), 'Disclose post-trial charges.'),
        Q('40 payments fail each month from expired cards. What helps recover them?', 'Reminders asking customers to update their card',
          ('Cancelling those customers\' accounts immediately', 'loses customers'), ('Charging a random other card', 'not allowed'),
          ('Ignoring the failures', 'lost revenue'), 'Reminders recover payments.'),
        Q('A subscription has 500 members at 10 dollars and churn rises from 3 to 8 percent. How many more members are lost per '
          'month?', '25', ('40', 'new churn count'), ('15', 'old churn count'), ('5', 'percent difference'),
          '0.08 x 500 - 0.03 x 500 = 40 - 15 = 25.', calc=lambda: round(0.08 * 500 - 0.03 * 500) == 25),
    ]),
    F2=sec('Handle the complications: dark patterns and price changes', SUB, [
        Q('A competitor makes cancellation require a phone call during limited hours. Why should a new business avoid copying this?',
          'It can break consumer rules and drives away trust', ('It always increases loyalty', 'not true'),
          ('Phones are illegal for businesses', 'no'), ('Customers actually prefer a difficult cancellation process', 'no'), 'Easy, honest exits.'),
        Q('A subscription price will rise next month. What should the business do?', 'Give advance notice with the new price and date',
          ('Raise it silently', 'surprise'), ('Raise it quietly for loyal long-time members only', 'unfair'), ('Hide it in a long email footer', 'unclear'),
          'Notice keeps trust.'),
        Q('A customer is charged after cancelling because of a system error. What is the right fix?', 'Refund the charge promptly and fix the system',
          ('Keep the money since it was an accident', 'not fair'), ('Ask the customer to prove it twice', 'burdensome'),
          ('Charge again to test', 'harmful'), 'Correct mistakes quickly.'),
        Q('Churn is 10 percent a month. Starting with 1,000 members and no new sign-ups, about how many remain after 2 months?',
          '810', ('800', 'subtracted 10 percent of start twice'), ('900', 'one month'), ('980', 'used 1 percent'),
          '1,000 x 0.9 x 0.9 = 810.', calc=lambda: round(1000 * 0.9 * 0.9) == 810),
        Q('Which statement is accurate?', 'Clear terms and easy cancellation support long-term subscriptions.',
          ('Hiding the cancellation option is a good long-term growth tactic.', 'harms trust'), ('Churn does not matter if prices are high.', 'it matters'),
          ('Trials never need disclosure.', 'they do'), 'Honesty sustains subscriptions.'),
    ]))

# ------------------------------------------------------------------ Set 74: chargebacks and disputes
CHARGE = ('A CHARGEBACK happens when a card customer disputes a charge with their card issuer (their bank). The merchant '
          'may lose the payment and pay a fee, but can usually respond with EVIDENCE by the deadline on the dispute '
          'notice; deadlines depend on the card network and reason. Useful evidence includes receipts, delivery tracking, '
          'signed agreements and messages. Prevent disputes with clear descriptions, a recognizable business name on card '
          'statements, fast responses to complaints, and a fair refund policy.')

s74 = SET('ENT.PAY.06',
    M=sec('Prevent chargebacks and respond with evidence', CHARGE, [
        Q('What is a chargeback?', 'A customer disputing a card charge with their bank',
          ('A refund the business chooses to give on its own', 'not a dispute'),
          ('A fee the business pays to open a bank account', 'not this'),
          ('A coupon the customer uses at checkout', 'not this'), 'The card issuer handles the dispute.'),
        Q('What can a merchant usually do in response?', 'Submit evidence by the deadline',
          ('Ignore it, since disputes always resolve for merchants', 'not true'),
          ('Charge the customer again right away', 'not allowed'),
          ('Post the customer\'s card number online', 'harmful'), 'Respond with evidence in time.'),
        Q('Which is useful evidence for a shipped order?', 'Delivery tracking showing it arrived',
          ('A photo of the owner smiling at the shop', 'not evidence'),
          ('A list of other happy customers', 'not this order'),
          ('The business\'s logo file', 'not evidence'), 'Tracking shows delivery.'),
        Q('Which habit helps prevent disputes?', 'A recognizable business name on card statements',
          ('A confusing name customers do not recognize', 'causes disputes'),
          ('Slow replies to complaints', 'causes disputes'),
          ('Hiding the refund policy', 'causes disputes'), 'Recognition prevents "I don\'t know this charge."'),
        Q('What sets the response deadline?', 'The dispute notice, based on card network and reason',
          ('The merchant\'s own preferred schedule for replying', 'not merchant\'s choice'),
          ('The customer\'s birthday', 'irrelevant'), ('There is never a deadline', 'there is'), 'Check the notice.'),
    ]),
    B=[cs('A referee for payments', 'Think of a sports referee. When one player says a goal should not count, the referee looks '
          'at the replay before deciding. In a chargeback, the customer\'s bank is like the referee. The customer says the '
          'charge should not count; the business shows its "replay": receipts, tracking and messages. Without a replay, the '
          'referee usually sides with the complaint.', [
        Q('In a chargeback, who is like the referee?', 'The customer\'s card issuer', ('The business owner', 'a party'),
          ('The customer', 'a party'), ('The shipping company that delivered', 'not the decider'), 'The issuer decides.'),
        Q('The business\'s "replay" is what?', 'Receipts, tracking and messages', ('A logo', 'no'), ('A song', 'no'),
          ('A discount code for later use', 'no'), 'Evidence.'),
        Q('Without a replay, what usually happens?', 'The referee sides with the complaint', ('The business wins automatically', 'no'),
          ('The game is cancelled', 'no'), ('Nothing happens', 'a decision is made'), 'Evidence matters.'),
        Q('The customer saying a charge should not count is like what?', 'A player disputing a goal', ('A fan cheering', 'no'),
          ('A coach resting on the bench', 'no'), ('A ticket sale', 'no'), 'It is a dispute.'),
        Q('What helps the business most in a dispute?', 'Clear evidence', ('Getting angry', 'no'), ('Ignoring it', 'no'),
          ('Guessing', 'no'), 'Evidence wins disputes.'),
    ], why='A learner who misses MAIN may not see how disputes are decided; a referee reviewing a replay shows it.')],
    F1=sec('Apply it: respond to a dispute', CHARGE, [
        Q('A customer disputes a 120-dollar order as "not received." The owner has tracking showing delivery to the customer\'s '
          'address. What should she send?', 'The tracking record and order receipt by the deadline',
          ('Nothing; disputes always go her way', 'not true'), ('An angry message to the customer\'s employer about the dispute', 'harmful'),
          ('A new charge to the same card', 'not allowed'), 'Evidence answers the claim.'),
        Q('The card statement shows "XQZ HOLDINGS 4471," but customers know the shop as "Maple Candle Co." What risk does this '
          'create?', 'Customers may not recognize the charge and dispute it', ('No risk at all, because statement names never matter', 'they do'),
          ('Higher sales automatically', 'no'), ('Lower card fees', 'no'), 'Use a recognizable name.'),
        Q('A chargeback of 80 dollars is lost and the processor charges a 15-dollar dispute fee (example amount). What is the '
          'total cost?', '95 dollars', ('80 dollars', 'missed fee'), ('15 dollars', 'missed sale'), ('65 dollars', 'subtracted'),
          '80 + 15 = 95.', calc=lambda: 80 + 15 == 95),
        Q('A customer emails a complaint before disputing. What response best prevents a chargeback?', 'Reply quickly and offer a fair fix',
          ('Wait two weeks to reply', 'slow'), ('Tell them to contact their bank', 'invites dispute'),
          ('Block their email', 'escalates'), 'Fast, fair responses prevent disputes.'),
        Q('Which record helps most for a service dispute?', 'The signed agreement and messages confirming the work',
          ('A picture of the office plant', 'irrelevant'), ('The company\'s mission statement and values page', 'irrelevant'),
          ('A competitor\'s price list', 'irrelevant'), 'Documents show what was agreed and done.'),
    ]),
    F2=sec('Handle the complications: fraud and repeat disputes', CHARGE, [
        Q('An order uses a card that the real cardholder says was stolen. What does this show?', 'Fraud can cause chargebacks even when the item shipped',
          ('The customer must always be lying', 'not necessarily'), ('Shipping guarantees payment', 'not always'),
          ('Chargebacks only happen when the service was poor', 'not only'), 'Fraud is a dispute reason.'),
        Q('A shop has many disputes from orders shipped to addresses that do not match billing. What precaution fits?',
          'Review mismatched high-risk orders before shipping', ('Ship faster to everyone', 'not a fix'),
          ('Stop recording customers\' shipping addresses', 'worse'), ('Refuse all card payments', 'overreaction'), 'Screen risky orders.'),
        Q('A business receives 4 disputes on 400 orders. What is the dispute rate?', '1 percent', ('4 percent', 'count'),
          ('10 percent', 'misdivided'), ('0.1 percent', 'moved decimal'), '4 / 400 = 0.01.', calc=lambda: 4 / 400 == 0.01),
        Q('The deadline on a dispute notice is close. The owner is missing some evidence. What should she do?', 'Submit the evidence she has before the deadline',
          ('Wait until everything is perfect, even past the deadline', 'misses deadline'),
          ('Ignore the notice', 'loses by default'), ('Create fake receipts', 'fraud'), 'Respond on time with real evidence.'),
        Q('Which statement is accurate?', 'Rules and deadlines differ by card network, so read each notice.',
          ('Every dispute has the same deadline.', 'not true'), ('Merchants can never respond.', 'they can'),
          ('Chargebacks are always just small fees, with no lost sale.', 'sale can be lost'), 'Read the specifics.'),
    ]))

# ------------------------------------------------------------------ Set 75: invoice and payment scams
SCAM = (('Small businesses are common targets for payment scams. FAKE INVOICES bill for things you never ordered, such'
        ' as directory listings. CHANGED BANK DETAILS scams send an email that looks like a real supplier asking you '
        'to pay a new account. OVERPAYMENT scams send too much money (often by a check that later bounces) and ask '
        'you to send back the difference. Protection: match invoices to orders, confirm any bank-detail change by '
        'calling a known number (not one in the email), and never send back an "overpayment." A bank may make check '
        'funds available within days, yet the check can still be returned as fake weeks later, and the depositor owes'
        ' the money.'))

s75 = SET('ENT.PAY.07',
    M=sec('Recognize payment scams and verify before paying', SCAM, [
        Q('An email from "your supplier" says their bank account changed. What should you do?', 'Call the supplier at a number you already know',
          ('Pay the new account right away to avoid late fees', 'risky'),
          ('Reply to the same email asking if it is real', 'scammer may answer'),
          ('Call the phone number listed in that email', 'may be the scammer'), 'Verify through a known channel.'),
        Q('What is an overpayment scam?', 'Someone sends too much and asks for the difference back',
          ('A customer paying exactly the invoiced amount on time', 'normal'),
          ('A supplier offering a bulk discount', 'normal'),
          ('A bank charging a monthly fee', 'normal'), 'The original payment often bounces later.'),
        Q('How can a business catch fake invoices?', 'Match each invoice to a real order', ('Pay every invoice that looks official', 'risky'),
          ('Pay invoices under 100 dollars without checking', 'still risky'), ('Ignore all invoices', 'misses real bills'),
          'Matching reveals fakes.'),
        Q("A customer's check for 1,500 dollars arrives for a 500-dollar order with a request to send back 1,000. What should the owner do?",
          'Do not send the 1,000; check with your bank at a trusted number',
          ('Send the 1,000 dollars back today, as the customer asks', 'classic overpayment scam'), ('Deposit the check and spend all 1,500 dollars right away', 'the check may be fake'),
          ('Give the customer the business bank login to sort it out', 'never share logins'),
          'Overpayment requests are a common scam: the check can be returned as fake after the funds appear, and the owner would owe the money. Send nothing back; contact the bank at a number you already trust.'),
        Q('Why not use the phone number in a suspicious email?', 'It may lead to the scammer', ('Phones never work for business', 'no'),
          ('It is always the correct number', 'not always'), ('Calling is illegal', 'no'), 'Use known contact details.'),
    ]),
    B=[cs('A stranger at the door in a uniform', 'Imagine someone in a uniform knocks and says, "I\'m from the water company; '
          'pay me the bill in cash today." The uniform looks real, but you would call the water company at the number on '
          'your last bill before handing over money. Payment scams work the same way: an email or invoice can look official. '
          'Check through a channel you already trust.', [
        Q('Why call the water company before paying?', 'The uniform might be fake', ('Uniforms are illegal to wear', 'no'),
          ('Water is free', 'no'), ('Cash is always best', 'no'), 'Appearance is not proof.'),
        Q('Which number should you call?', 'The one on your last real bill', ('The one the stranger gives', 'may be fake'),
          ('A random number', 'no'), ('No number', 'verify'), 'Use a known number.'),
        Q('An official-looking email is like what?', 'The uniform at the door', ('A contract you signed', 'not proof'),
          ('A bank deposit', 'no'), ('A receipt', 'no'), 'Looks are not proof.'),
        Q('What should you do before paying a surprise bill?', 'Check through a trusted channel', ('Pay quickly', 'risky'),
          ('Ignore all bills', 'misses real ones'), ('Ask the stranger if he is real', 'not independent'), 'Verify independently.'),
        Q('What is the main lesson?', 'Verify before paying', ('Never pay any bill', 'too extreme'), ('Trust uniforms', 'risky'),
          ('Pay in cash', 'not the lesson'), 'Independent verification.'),
    ], why='A learner who misses MAIN may trust official-looking messages; a stranger in a uniform shows why to verify.')],
    F1=sec('Apply it: check suspicious requests', SCAM, [
        Q('An invoice for 349 dollars arrives for an "online business directory listing" no one ordered. What should the owner do?',
          'Check records; if there is no order, do not pay it', ('Pay it, because it looks official and has a logo', 'risky'),
          ('Pay half to be safe', 'still paying a scam'), ('Forward it to every customer', 'unhelpful'), 'No order, no payment.'),
        Q('A supplier\'s email asks to send this month\'s 4,200-dollar payment to a new account "urgently." What is the safest '
          'response?', 'Confirm by calling the supplier\'s known number first', ('Send it now because it is urgent', 'urgency is a red flag'),
          ('Split it between the old and new accounts to be safe', 'still risky'), ('Reply asking for proof by email', 'scammer may reply'),
          'Verify by phone.'),
        Q('A buyer sends a 900-dollar check for a 300-dollar item and asks for 600 dollars back by gift card. What red flags '
          'appear?', 'Overpayment and a request for gift cards', ('None; this is a normal sale', 'red flags'),
          ('Only that the item is cheap', 'not the flag'), ('Only that checks are old-fashioned', 'not the flag'),
          'Overpayment plus gift cards is a scam pattern.', calc=lambda: 900 - 300 == 600),
        Q('Which internal rule reduces scam risk most?', 'Two people approve any bank-detail change', ('Anyone can change bank details', 'risky'),
          ('Bank details can be changed by email request only', 'risky'), ('Never record bank details', 'unworkable'), 'Dual approval adds a check.'),
        Q('An email "from the owner" asks the bookkeeper to buy gift cards urgently. What should the bookkeeper do?', 'Confirm with the owner in person or by a known number',
          ('Buy them right away', 'scam'), ('Reply to the email with the gift card codes right away', 'scam'), ('Ignore the owner forever', 'overreaction'),
          'Impersonation scams use urgency.'),
    ]),
    F2=sec('Handle the complications: after a mistake', SCAM, [
        Q('An owner realizes she paid a fake invoice an hour ago. What is the first step?', 'Contact her bank immediately',
          ('Wait a week to see what happens', 'delay hurts'), ('Pay another invoice to balance it', 'no'),
          ('Delete the email and forget it', 'loses evidence'), 'Fast action can help recovery.'),
        Q('After a scam, what else should the owner do?', 'Report it and tighten payment checks', ('Keep it secret from staff', 'repeats risk'),
          ('Blame the bank only', 'not a fix'), ('Stop using email entirely for the business', 'impractical'), 'Learn and report.'),
        Q('A real supplier truly changed banks. How should the change be confirmed?', 'By calling a known contact before updating records',
          ('By trusting the email because it is real this time', 'cannot tell'), ('By paying a test amount to the new account', 'still risky'),
          ('By asking a customer', 'unrelated'), 'Same verification every time.'),
        Q('The bank made the funds from a check available in 2 days, but later says the check was fake and reverses the deposit. What lesson does this teach?',
          'Funds can be made available before a check is proven good',
          ('Banks never reverse a deposit after the funds are available', 'they can'), ('Checks always clear for good in exactly 2 days', 'not always'),
          ('Deposits are guaranteed once they show in the account', 'not guaranteed'),
          'Available funds do not prove a check is good; the depositor owes the money if it is fake.'),
        Q('Which statement is accurate?', 'Urgency, new bank details and overpayments are common scam signs.',
          ('Scammers only target large companies.', 'small too'), ('Official-looking invoices are always real.', 'not always'),
          ('Gift card payments are a normal way to pay supplier invoices.', 'red flag'), 'Know the patterns.'),
    ]))

# ------------------------------------------------------------------ Set 76: supplier terms and communicating delays
SUPP = ('Suppliers have terms too: minimum order quantities, lead time (how long from order to delivery), payment terms, '
        'and return rules. Plan orders so supplies arrive before you need them. When something will be late, from your '
        'supplier or from you, COMMUNICATE EARLY: tell the customer what happened, the new expected date, and what you will '
        'do (for example, offer a choice to wait or cancel). Silence makes customers assume the worst; honest updates keep '
        'trust.')

s76 = SET('ENT.PAY.08',
    M=sec('Plan around supplier terms and communicate delays early', SUPP, [
        Q('What is lead time?', 'How long from order to delivery', ('The time a customer spends reading an ad', 'not lead time'),
          ('The length of a business meeting', 'not lead time'), ('The time until a loan is repaid', 'not lead time'),
          'Lead time is the delivery wait.'),
        Q('What is a minimum order quantity?', 'The smallest amount a supplier will sell in one order',
          ('The fewest customers a business may serve each day', 'not this'),
          ('The lowest price a shop may charge', 'not this'), ('The smallest box size available', 'not this'),
          'Suppliers set minimums.'),
        Q('A supplier\'s lead time is 3 weeks. When should an owner order for a sale starting June 22?', 'By June 1',
          ('By June 21', 'too late'), ('By June 15', 'too late'), ('On June 22', 'too late'), 'June 22 - 21 days = June 1.',
          calc=lambda: 22 - 21 == 1),
        Q('An order will be late. When should the customer be told?', 'As soon as the owner knows', ('On the original delivery day', 'late'),
          ('Only if the customer asks', 'passive'), ('Never, to avoid awkwardness', 'harms trust'), 'Early updates keep trust.'),
        Q('What should a delay message include?', 'What happened, the new date and options', ('Only an apology, with no new date or options', 'incomplete'),
          ('Blame on the customer', 'harmful'), ('A promise with no plan', 'incomplete'), 'Complete, honest updates.'),
    ]),
    B=[cs('A friend running late', 'If a friend is going to be 30 minutes late for dinner, a text saying "Running 30 minutes '
          'late, traffic, still coming—want to order without me?" feels fine. A friend who just never shows up and says '
          'nothing feels terrible. Businesses work the same way: a delay with an early, honest message keeps trust; '
          'silence breaks it.', [
        Q('Which message keeps trust?', '"Running 30 minutes late, still coming"', ('No message at all', 'silence'),
          ('"Maybe I\'ll come, maybe not, we\'ll see"', 'vague'), ('A message after dinner ends', 'too late'), 'Early and specific.'),
        Q('What does silence make people assume?', 'The worst', ('The best', 'no'), ('Nothing', 'no'), ('A gift is coming', 'no'),
          'Silence breeds worry.'),
        Q('"Want to order without me?" is like what in business?', 'Offering the customer options', ('Charging more', 'no'),
          ('Hiding the delay', 'no'), ('Cancelling the order silently', 'no'), 'Options respect the customer.'),
        Q('When should the late friend text?', 'As soon as they know', ('After dinner ends', 'too late'), ('Never', 'no'),
          ('Next week', 'no'), 'Early notice.'),
        Q('"Traffic" in the message is like what?', 'Explaining what happened', ('Blaming the customer', 'no'), ('A discount', 'no'),
          ('A new price', 'no'), 'Brief honest reason.'),
    ], why='A learner who misses MAIN may not see why early notice matters; a friend running late is familiar.')],
    F1=sec('Apply it: order on time and write a delay notice', SUPP, [
        Q('A shop sells 40 mugs a week. The supplier\'s lead time is 2 weeks. About how many mugs must be on hand when ordering '
          'to avoid running out before delivery?', '80 mugs', ('40 mugs', 'one week'), ('20 mugs', 'half week'), ('42 mugs', 'added'),
          '40 x 2 = 80.', calc=lambda: 40 * 2 == 80),
        Q('A supplier\'s minimum order is 200 labels; the owner uses 50 a month. How many months will one order last?', '4 months',
          ('2 months', 'miscalculated'), ('50 months', 'confused'), ('200 months', 'confused'), '200 / 50 = 4.', calc=lambda: 200 / 50 == 4),
        Q('Which delay notice is best?', '"Your order is delayed by our supplier; new ship date May 9. Reply to cancel for a full refund."',
          ('"There may be issues. We\'ll see."', 'vague'), ('"Not our fault. Wait."', 'blames, no date'),
          ('No notice at all; just ship the order whenever the supplier\'s stock finally arrives', 'silence'), 'Reason, date and options.'),
        Q('A supplier misses a delivery. The owner promised customers Friday. What is the first step?', 'Tell affected customers right away with a new estimate',
          ('Wait until Friday and say nothing to the customers', 'too late'), ('Ship empty boxes on time', 'dishonest'),
          ('Cancel all orders without asking', 'overreaction'), 'Early notice.'),
        Q('Supplier terms are Net 30, and customers pay on delivery, which happens before day 30. Why does this help cash flow?',
          'Customer money arrives before the supplier bill is due',
          ('It means the supplier never needs to be paid for the goods', 'still owed'), ('It doubles sales', 'no'),
          ('It removes all costs', 'no'),
          'Timing favors the business.'),
    ]),
    F2=sec('Handle the complications: repeat delays and backup plans', SUPP, [
        Q('A key supplier has been late 4 times in 6 months. What should the owner consider?', 'Finding a backup supplier',
          ('Promising customers faster delivery anyway', 'unrealistic'), ('Ignoring the pattern', 'risky'),
          ('Stopping all sales', 'overreaction'), 'Backups reduce dependence.'),
        Q('A backup supplier costs 10 percent more. A 500-dollar order would cost how much more?', '50 dollars',
          ('10 dollars', 'percent as dollars'), ('550 dollars', 'total'), ('5 dollars', 'moved decimal'), '0.10 x 500 = 50.',
          calc=lambda: round(0.10 * 500, 2) == 50),
        Q('A customer wants a firm date during a supplier delay. The owner is unsure. What is honest?', 'Give a range and promise an update by a set day',
          ('Promise a firm date she cannot be sure of meeting', 'may break promise'), ('Refuse to answer at all', 'unhelpful'),
          ('Make up a tracking number', 'dishonest'), 'Honest uncertainty with a follow-up.'),
        Q('Ordering more stock to avoid delays ties up cash. What balance should the owner find?', 'Enough safety stock without draining cash',
          ('Order a year of stock at once regardless', 'drains cash'), ('Never keep any stock', 'risk of running out'),
          ('Order only after customers complain', 'too late'), 'Balance risk and cash.'),
        Q('Which statement is accurate?', 'Early, honest updates keep trust even when delays happen.',
          ('Delays always destroy a business.', 'not always'), ('Customers prefer silence to hearing any bad news about orders.', 'not usually'),
          ('Suppliers never change terms.', 'they can'), 'Communication matters.'),
    ]))

SETS = [s69, s70, s71, s72, s73, s74, s75, s76]
