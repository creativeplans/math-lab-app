"""Entrepreneurship sets 146-156: Digital path, Microsoft case, Content path, Craigslist case.
Prices, fees and rates are practice assumptions. Platform thresholds are not taught as numbers. Names are fictional."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 146: support and updates for digital products
SUPPORT = ('Digital products (apps, templates, online courses, software tools) are not "make once and forget." Customers need '
           'SUPPORT: answers when something does not work, clear instructions, and a way to contact you. Products also need '
           'UPDATES when devices, browsers or platforms change, and to fix bugs (errors). Budget time for support and '
           'updates, state what support is included (for example "email replies within 2 business days"), and keep a list of '
           'common questions to turn into a help page.')

s146 = SET('ENT.DIG.01',
    M=sec('Plan support and updates for a digital product', SUPPORT, [
        Q('Why is a digital product not "make once and forget"?', 'Customers need support and the product needs updates',
          ('Digital products never have errors once launched', 'they can'),
          ('Devices and platforms never change over time', 'they change'),
          ('Customers never have questions about software', 'they do'), 'Ongoing work.'),
        Q('What is a bug?', 'An error in a digital product', ('A paid feature added later', 'no'), ('A type of marketing email', 'no'),
          ('A customer review', 'no'), 'An error.'),
        Q('Which support statement is clearest?', '"Email replies within 2 business days"', ('"We reply eventually, maybe, by some method"', 'vague'),
          ('"Support depends on our mood"', 'vague'), ('"Contact us somehow"', 'vague'), 'Specific promise.'),
        Q('What can common questions become?', 'A help page', ('A secret file nobody reads', 'wasted'), ('A reason to raise prices', 'no'),
          ('A list of complaints to ignore', 'wasted'), 'Self-service help.'),
        Q('Why budget time for updates?', 'Devices, browsers and platforms change', ('Updates are never needed', 'they are'),
          ('Updates only matter for big companies', 'all products'), ('Customers prefer outdated products', 'no'), 'Change happens.'),
    ]),
    B=[cs('Owning a car, not just buying it', 'Buying a car is not the end of the cost: it needs oil changes, repairs and new tires. '
          'A digital product is similar. Launching it is like buying the car; support and updates are the ongoing maintenance. '
          'Skip the maintenance and the car, or the product, eventually stops working for the people who rely on it.', [
        Q('Launching a digital product is like what?', 'Buying the car', ('Selling the car', 'no'), ('Painting the car', 'no'),
          ('Parking the car', 'no'), 'The start.'),
        Q('Support and updates are like what?', 'Ongoing car maintenance', ('A one-time purchase, then nothing', 'no'), ('A car wash once', 'no'),
          ('A new license plate', 'no'), 'Maintenance.'),
        Q('What happens if maintenance is skipped?', 'It eventually stops working well', ('It runs better and better forever', 'no'),
          ('It becomes free', 'no'), ('Nothing ever', 'no'), 'Neglect fails.'),
        Q('An oil change is like what for an app?', 'A routine update', ('A refund', 'no'), ('A change to the logo', 'no'), ('An ad', 'no'),
          'Routine care.'),
        Q('Who relies on the product working?', 'The customers who use it', ('Only the owner, nobody else', 'no'), ('Nobody', 'no'),
          ('Only competitors', 'no'), 'Users depend on it.'),
    ], why='A learner who misses MAIN may think digital products need no upkeep; owning a car shows ongoing maintenance.')],
    F1=sec('Apply it: budget support time', SUPPORT, [
        Q('A template shop sells 200 templates a month; 5 percent of buyers email for help. How many emails a month?', '10',
          ('5', 'percent as count'), ('20', 'misdivided'), ('100', 'half'), '0.05 x 200 = 10.', calc=lambda: round(0.05 * 200) == 10),
        Q('Each email takes 15 minutes. How much support time is that per month?', '150 minutes', ('15 minutes', 'one'),
          ('25 minutes', 'added'), ('1.5 minutes', 'divided'), '10 x 15 = 150.', calc=lambda: 10 * 15 == 150),
        Q('Half the emails ask the same question about fonts. What should the owner do?', 'Add a clear help page about fonts',
          ('Keep answering each one separately forever', 'inefficient'), ('Stop answering font emails', 'poor service'),
          ('Remove fonts from the templates', 'overreaction'), 'Self-service.'),
        Q('A browser update breaks a course video player. What is the first step?', 'Fix or update the player and tell affected customers',
          ('Ignore it until refund requests start to pile up', 'harmful'), ('Blame customers\' browsers', 'unhelpful'), ('Delete the course', 'drastic'),
          'Fix and communicate.'),
        Q('A one-time 30-dollar product promises "lifetime support." What should the owner consider?', 'Whether that promise is sustainable at that price',
          ('Nothing; lifetime support is always free to give', 'costs time'), ('Only the product color', 'irrelevant'),
          ('Only competitor prices', 'incomplete'), 'Sustainable promises.'),
    ]),
    F2=sec('Handle the complications: growing support load', SUPPORT, [
        Q('Sales double and support emails double. The owner has no more time. What helps?', 'Better help pages, plus paid help if needed',
          ('Stop replying to everyone who writes in', 'poor service'), ('Hide the contact address', 'poor service'), ('Lower prices further', 'worse'),
          'Scale support.'),
        Q('Support takes 20 hours a month valued at 30 dollars an hour. What is the monthly cost?', '600 dollars', ('50 dollars', 'added'),
          ('30 dollars', 'rate'), ('1.50 dollars', 'divided'), '20 x 30 = 600.', calc=lambda: 20 * 30 == 600),
        Q('An old product version no longer works on new phones and few people use it. What is a fair approach?', 'Announce an end-of-support date in advance',
          ('Stop it overnight with no notice to anyone', 'unfair'), ('Pretend it still works', 'misleading'), ('Charge extra to old users secretly', 'unfair'),
          'Clear notice.'),
        Q('A bug fix introduces a new bug. What habit would help?', 'Testing updates before releasing them', ('Releasing faster without checks', 'worse'),
          ('Never updating anything', 'other risks'), ('Hiding updates', 'no'), 'Test first.'),
        Q('Which statement is accurate?', 'Digital products need ongoing support and updates.',
          ('Digital products never need maintenance.', 'not true'), ('Support is optional for paid digital products.', 'customers expect it'),
          ('Updates never cause new problems.', 'they can'), 'Plan upkeep.'),
    ]))

# ------------------------------------------------------------------ Set 147: access, accounts, licensing
LIC = ('Digital products are usually sold as a LICENSE: permission to use them under stated terms, not ownership of the '
       'product itself. A license states who may use it (one person, a team, a business), how many devices or projects, '
       'whether it may be resold or shared, and how long it lasts. Customer ACCESS is often managed by accounts or download '
       'links. Write the license in plain words, show it before purchase, and decide what happens to access if a customer '
       'cancels or requests a refund.')

s147 = SET('ENT.DIG.02',
    M=sec('Write plain license terms and manage customer access', LIC, [
        Q('What does a customer usually buy with a digital product?', 'A license to use it under stated terms',
          ('Full ownership of the product and its code', 'not usually'), ('The right to resell unlimited copies', 'not usually'),
          ('The company that made it', 'no'), 'Permission to use.'),
        Q('Which item belongs in license terms?', 'How many people or devices may use it', ('The owner\'s birthday', 'irrelevant'),
          ('The logo\'s colors', 'irrelevant'), ('The founder\'s hobbies and interests', 'irrelevant'), 'Usage limits.'),
        Q('When should license terms be shown?', 'Before purchase', ('Only after a complaint', 'too late'), ('Never', 'needed'),
          ('Only to resellers', 'all buyers'), 'Up front.'),
        Q('What should be decided about refunds?', 'What happens to access if a refund is given', ('Nothing, because access stays forever anyway', 'unclear'),
          ('Refunds are never allowed anywhere', 'not necessarily'), ('Access doubles', 'no'), 'Access rules.'),
        Q('Why write the license in plain words?', 'So customers understand what they may do', ('So it sounds more legal', 'not the goal'),
          ('So nobody reads it', 'opposite'), ('Because plain words are required everywhere', 'not the reason'), 'Clarity.'),
    ]),
    B=[cs('A movie ticket, not the movie', 'A movie ticket lets you watch the film in that theater at that time. It does not let '
          'you copy the film or sell screenings. A digital license works the same way: the buyer gets permission to use the '
          'product in stated ways, not ownership of the product itself. The ticket\'s rules are printed so everyone knows '
          'them.', [
        Q('A movie ticket gives you what?', 'Permission to watch under certain rules', ('Full ownership of the whole film and its copies', 'no'),
          ('The right to copy it', 'no'), ('The theater building', 'no'), 'Permission.'),
        Q('A digital license is like what?', 'The ticket', ('The film itself', 'no'), ('The projector', 'no'), ('The popcorn', 'no'),
          'Permission to use.'),
        Q('Can a ticket holder sell copies of the film?', 'No', ('Yes, always', 'no'), ('Only on weekends', 'no'), ('Only online', 'no'),
          'Not permitted.'),
        Q('Why are ticket rules printed?', 'So everyone knows them', ('To hide them', 'no'), ('For decoration', 'no'), ('To confuse the viewers', 'no'),
          'Transparency.'),
        Q('What does the buyer of a digital product usually not get?', 'Ownership of the product itself', ('Permission to use it as stated', 'they get that'),
          ('Access to it', 'they get that'), ('The stated terms', 'they get those'), 'License, not ownership.'),
    ], why='A learner who misses MAIN may think buyers own digital products; a movie ticket shows a license.')],
    F1=sec('Apply it: set license tiers', LIC, [
        Q('A designer sells a font: personal license 20 dollars, business license 60 dollars. A company uses the personal version on '
          'its packaging. What is the issue?', 'Its use goes beyond the personal license terms', ('No issue, because any license covers any use', 'not true'),
          ('The font changes color', 'irrelevant'), ('The company owns the font now', 'no'), 'Match license to use.'),
        Q('A team license covers 5 users at 120 dollars. What is the cost per user?', '24 dollars', ('120 dollars', 'total'),
          ('600 dollars', 'multiplied'), ('115 dollars', 'subtracted'), '120 / 5 = 24.', calc=lambda: 120 / 5 == 24),
        Q('A course is sold with account access. A customer gets a refund. What should the terms say?', 'Whether access ends after the refund',
          ('Nothing; access always stays', 'unclear'), ('The customer gets a second account', 'no'), ('Refunds double access', 'no'),
          'Access rules.'),
        Q('Which license line is clearest?', '"For 1 person, up to 3 devices, no resale or sharing."', ('"Use it however you like, more or less, on anything."', 'vague'),
          ('"Some sharing may be fine."', 'vague'), ('"Rules apply, ask us."', 'vague'), 'Specific terms.'),
        Q('20 personal licenses at 20 dollars and 8 business licenses at 60 dollars sell. What is total revenue?', '880 dollars',
          ('400 dollars', 'personal only'), ('480 dollars', 'business only'), ('80 dollars', 'added prices'),
          '20 x 20 + 8 x 60 = 400 + 480 = 880.', calc=lambda: 20 * 20 + 8 * 60 == 880),
    ]),
    F2=sec('Handle the complications: sharing and piracy', LIC, [
        Q('A customer posts the download link publicly. What could the owner have used?', 'Account-based access or expiring links',
          ('Nothing could help', 'options exist'), ('A bigger logo printed on the file', 'irrelevant'), ('A lower price', 'not prevention'),
          'Access controls.'),
        Q('An owner finds her product shared on a piracy site. What is a reasonable step?', 'Request removal through the site\'s process',
          ('Do nothing ever', 'passive'), ('Post angry messages everywhere about it', 'unhelpful'), ('Stop selling entirely', 'overreaction'),
          'Use takedown processes.'),
        Q('Strict copy protection annoys honest customers. What should the owner weigh?', 'Protection against ease of use for paying customers',
          ('Only maximum protection, always, whatever the cost', 'hurts honest users'), ('No terms at all', 'no protection'),
          ('Only competitor choices', 'incomplete'), 'Balance.'),
        Q('A license says "lifetime access," but the owner plans to close the platform in 2 years. What problem arises?', 'The promise may not be kept',
          ('No problem; lifetime means 2 years', 'misleading'), ('Customers will not notice', 'they will'), ('It is always legal', 'risky'),
          'Promise only what you can keep.'),
        Q('Which statement is accurate?', 'Digital buyers usually get a license, not ownership.',
          ('Buyers always own the product and all of its code.', 'not usually'), ('License terms can be hidden.', 'should be shown'),
          ('Sharing is always allowed.', 'depends on terms'), 'Know the license.'),
    ]))

# ------------------------------------------------------------------ Set 148: recurring costs of digital businesses
DCOST = ('Digital businesses can look cheap to run but have RECURRING COSTS: hosting, domain, email service, software '
         'subscriptions, payment and platform fees, storage, design tools and app store fees. Many costs grow with users, '
         'such as storage or email sending limits. List every recurring cost, convert to a monthly total, and compare with '
         'monthly revenue. A product with low marginal cost (the cost of one more sale) can still lose money if fixed '
         'monthly costs are high.')

s148 = SET('ENT.DIG.03',
    M=sec('List and total the recurring costs of a digital business', DCOST, [
        Q('Which is a recurring cost for a digital business?', 'Monthly hosting', ('A one-time logo design', 'once'),
          ('A first laptop purchase', 'once'), ('A single trademark search', 'once'), 'Repeats monthly.'),
        Q('What is marginal cost?', 'The cost of one more sale', ('The total cost of starting the business', 'startup cost'),
          ('The cost of the owner\'s time last year', 'no'), ('A tax on profits', 'no'), 'Incremental cost.'),
        Q('Hosting 25, email 15, software 40, domain 2 a month. What is the monthly total?', '82 dollars', ('80 dollars', 'missed domain'),
          ('40 dollars', 'largest'), ('25 dollars', 'one'), '25 + 15 + 40 + 2 = 82.', calc=lambda: 25 + 15 + 40 + 2 == 82),
        Q('Which cost often grows with more users?', 'Storage', ('A one-time logo fee', 'fixed'), ('The business name', 'none'),
          ('The founding date', 'none'), 'Usage-based.'),
        Q('Why can a low-marginal-cost product still lose money?', 'Fixed monthly costs may be higher than revenue', ('Marginal cost is always zero for digital products', 'not the reason'),
          ('Digital products cannot be sold', 'no'), ('Revenue is never counted', 'no'), 'Fixed costs.'),
    ]),
    B=[mathb('Converting costs to a monthly total', 'Some costs are monthly, some yearly. Convert yearly costs to monthly by dividing '
             'by 12, then add everything. Example: hosting 20 a month, domain 18 a year (1.50 a month), software 240 a year (20 a '
             'month): 20 + 1.50 + 20 = 41.50 a month. Compare that total with monthly revenue to see whether costs are covered.', [
        Q('18 dollars a year is how much a month?', '1.50', ('18', 'not converted'), ('216.00', 'multiplied'), ('6', 'divided by 3'),
          '18 / 12 = 1.50.', calc=lambda: 18 / 12 == 1.5),
        Q('240 dollars a year is how much a month?', '20', ('240', 'not converted'), ('2,880', 'multiplied'), ('24', 'divided by 10'),
          '240 / 12 = 20.', calc=lambda: 240 / 12 == 20),
        Q('20 + 1.50 + 20 is what?', '41.50', ('40.00', 'missed 1.50'), ('21.50', 'missed 20'), ('42.50', 'arithmetic slip'),
          '41.50.', calc=lambda: 20 + 1.5 + 20 == 41.5),
        Q('120 dollars a year is how much a month?', '10', ('12', 'divided by 10'), ('1,440', 'multiplied'), ('120', 'not converted'),
          '120 / 12 = 10.', calc=lambda: 120 / 12 == 10),
        Q('Why convert to one period?', 'To add and compare costs fairly', ('To make costs disappear', 'no'), ('Because yearly costs are fake', 'no'),
          ('To confuse the budget', 'no'), 'Same units.'),
    ], why='A learner who misses MAIN may mix monthly and yearly costs; this practices converting to a monthly total.')],
    F1=sec('Apply it: check whether revenue covers costs', DCOST, [
        Q('An app costs 30 hosting, 50 tools, 25 email monthly and 99 a year for an app store account. What is the monthly total, to the nearest cent?',
          '113.25 dollars', ('105.00 dollars', 'missed store fee'), ('204.00 dollars', 'added yearly as monthly'), ('99.00 dollars', 'store fee'),
          '30 + 50 + 25 + 99/12 = 113.25.', calc=lambda: round(30 + 50 + 25 + 99 / 12, 2) == 113.25),
        Q('Revenue is 90 dollars a month. Are costs covered?', 'No, it falls short by 23.25 dollars', ('Yes, with 23.25 dollars left over', 'reversed'),
          ('Exactly covered', 'no'), ('Cannot tell', 'can'), '90 - 113.25 = -23.25.', calc=lambda: round(90 - 113.25, 2) == -23.25),
        Q('Each new subscriber pays 6 dollars a month and adds 0.50 in costs. How many more subscribers cover the 23.25 shortfall, rounded up?', '5',
          ('4', 'rounded down'), ('47', 'divided by 0.50'), ('3', 'divided by 6'), '23.25 / 5.50 = 4.2, up to 5.',
          calc=lambda: math.ceil(23.25 / (6 - 0.5)) == 5),
        Q('A tool costing 40 a month is used once a quarter. What should the owner consider?', 'Cancelling or switching to a cheaper plan',
          ('Keeping it forever, just in case it is needed', 'waste'), ('Buying a second copy', 'waste'), ('Ignoring it', 'waste'), 'Cut unused costs.'),
        Q('Storage costs rise as users upload more. What should pricing reflect?', 'Costs that grow with heavy use', ('Nothing; storage is free', 'not true'),
          ('Only the founder\'s preference', 'not enough'), ('Only competitor logos', 'irrelevant'), 'Usage-based costs.'),
    ]),
    F2=sec('Handle the complications: creeping costs', DCOST, [
        Q('Small tools were added one by one and now total 300 dollars a month. What is a good habit?', 'Review the tool list every few months',
          ('Never look at tool costs', 'creep'), ('Add more tools to compensate', 'worse'), ('Pay with a personal card to hide it', 'commingling'),
          'Regular review.'),
        Q('A platform raises its fee from 5 to 8 percent on 2,000 dollars of monthly sales. How much more per month?', '60 dollars',
          ('160 dollars', 'new fee'), ('100 dollars', 'old fee'), ('3 dollars', 'percent difference'), '0.03 x 2,000 = 60.',
          calc=lambda: round((0.08 - 0.05) * 2000, 2) == 60),
        Q('A free tier becomes paid at 25 dollars a month. The owner relies on it. What should she do?', 'Compare alternatives and budget for it',
          ('Ignore the change', 'will be charged'), ('Delete all of her data immediately', 'drastic'), ('Assume it stays free', 'wrong'),
          'Plan for change.'),
        Q('Monthly costs are 400 and each sale contributes 8. How many sales a month to break even?', '50', ('400', 'costs'), ('8', 'per sale'),
          ('3,200', 'multiplied'), '400 / 8 = 50.', calc=lambda: 400 / 8 == 50),
        Q('Which statement is accurate?', 'Digital businesses have recurring costs to cover.',
          ('Digital businesses have no costs.', 'not true'), ('Low marginal cost always guarantees a profit.', 'not true'),
          ('Yearly costs can be ignored.', 'not true'), 'Track recurring costs.'),
    ]))

# ------------------------------------------------------------------ Set 149: onboarding and checking usefulness
ONB = ('ONBOARDING is a new customer\'s first experience: signing up, the first steps, and reaching a first useful result. If '
       'that path is confusing, many customers quit early. Make the first steps short and clear, show an example, and send a '
       'helpful message after sign-up. Then CHECK USEFULNESS: are people actually using the product after a week or a month? '
       'Track activation (the share who reach a first useful result) and ask a few customers what helped or confused them.')

s149 = SET('ENT.DIG.04',
    M=sec('Design first steps and measure whether customers find the product useful', ONB, [
        Q('What is activation?', 'The share of new users who reach a first result', ('The number of ads shown', 'no'),
          ('The moment a user\'s computer is switched on', 'pun'), ('The price of a subscription', 'no'), 'Early success.'),
        Q('What often happens if onboarding is confusing?', 'Many customers quit early', ('Customers stay longer', 'no'),
          ('Sales automatically double', 'no'), ('Support emails disappear', 'no'), 'Early drop-off.'),
        Q('100 sign up and 35 reach a first useful result. What is activation?', '35 percent', ('65 percent', 'not activated'),
          ('100 percent', 'all'), ('3.5 percent', 'moved decimal'), '35 / 100 = 0.35.', calc=lambda: 35 / 100 == 0.35),
        Q('Which onboarding step helps?', 'A short example showing a first result', ('A 40-page manual before anything works', 'too long'),
          ('No instructions at all', 'confusing'), ('Hiding the main feature', 'confusing'), 'Quick win.'),
        Q('How can an owner learn what confuses customers?', 'Ask a few customers what helped or confused them', ('Guess without asking', 'unreliable'),
          ('Read only competitor reviews online instead', 'indirect'), ('Ignore feedback', 'no learning'), 'Direct feedback.'),
    ]),
    B=[mathb('Activation and retention rates', 'Rates compare a part to a whole. Activation = users who reached a first useful '
             'result / users who signed up. Retention at 30 days = users still active / users who started. Example: 80 sign up, 28 '
             'activate: 28 / 80 = 35 percent. If 14 are active after 30 days: 14 / 80 = 17.5 percent. Use the same starting group '
             'for both.', [
        Q('28 of 80 activate. What is the rate?', '35 percent', ('28 percent', 'count'), ('52 percent', 'not activated'),
          ('3.5 percent', 'moved decimal'), '28 / 80 = 0.35.', calc=lambda: 28 / 80 == 0.35),
        Q('14 of 80 are active after 30 days. What is the rate?', '17.5 percent', ('14 percent', 'count'), ('50 percent', 'of activated'),
          ('82.5 percent', 'inactive'), '14 / 80 = 0.175.', calc=lambda: 14 / 80 == 0.175),
        Q('40 of 200 activate. What is the rate?', '20 percent', ('40 percent', 'count'), ('80 percent', 'not activated'),
          ('5 percent', 'reversed'), '40 / 200 = 0.2.', calc=lambda: 40 / 200 == 0.2),
        Q('Which number is the whole for both rates here?', 'The users who signed up', ('Only the active users', 'part'),
          ('The website visitors who never signed up', 'different group'), ('The price', 'no'), 'Same base.'),
        Q('Activation rises from 20 to 30 percent of 200 sign-ups. How many more users activate?', '20', ('10', 'percent difference'),
          ('60', 'new count'), ('40', 'old count'), '60 - 40 = 20.', calc=lambda: round(0.3 * 200) - round(0.2 * 200) == 20),
    ], why='A learner who misses MAIN may not compute these rates; this practices part over whole with the same base.')],
    F1=sec('Apply it: improve a first experience', ONB, [
        Q('A budgeting app\'s users must enter 12 months of data before seeing anything useful. Many quit. What change fits?', 'Show a useful result after the first week of data',
          ('Require 24 months of data before anything shows', 'worse'), ('Remove the app\'s main feature', 'worse'), ('Send no messages', 'no help'),
          'Faster first value.'),
        Q('After the change, activation rises from 25 to 40 percent of 300 sign-ups. How many more activate?', '45', ('15', 'percent difference'),
          ('120', 'new count'), ('75', 'old count'), '120 - 75 = 45.', calc=lambda: round(0.4 * 300) - round(0.25 * 300) == 45),
        Q('A course has 500 buyers but only 60 finish lesson 1. What should the owner look at first?', 'Why buyers stop before or during lesson 1',
          ('Only how to get more buyers', 'misses problem'), ('Only the logo', 'irrelevant'), ('Nothing, because sales are all that matter', 'usefulness matters'),
          'Find the drop.'),
        Q('Which welcome message helps most?', '"Start here: a 5-minute lesson to make your first budget."', ('"Welcome. Good luck."', 'unhelpful'),
          ('"Read all 40 pages of the manual first, then come back."', 'overwhelming'), ('No message at all', 'missed chance'), 'Clear first step.'),
        Q('Of 40 activated users, 30 are still active after a month. What is the retention among activated users?', '75 percent',
          ('30 percent', 'count'), ('25 percent', 'lost'), ('40 percent', 'count'), '30 / 40 = 0.75.', calc=lambda: 30 / 40 == 0.75),
    ]),
    F2=sec('Handle the complications: vanity sign-ups', ONB, [
        Q('Sign-ups doubled after a promotion, but activation fell by half. What happened?', 'More people signed up who did not find it useful',
          ('The product became twice as useful', 'no'), ('Activation always falls whenever sign-ups rise', 'not always'),
          ('Nothing changed', 'it changed'), 'Quality of sign-ups.'),
        Q('An owner reports only sign-ups to investors. What is missing?', 'Whether users actually get value and stay', ('Nothing, because sign-ups prove success alone', 'not alone'),
          ('A larger logo', 'irrelevant'), ('More colors', 'irrelevant'), 'Usefulness metrics.'),
        Q('A survey of 3 customers says the product is perfect. What is the limitation?', 'Three answers may not represent all users',
          ('Three answers prove everything about all users', 'too few'), ('Surveys are illegal', 'no'), ('Customers never answer honestly', 'overstated'),
          'Small sample.'),
        Q('A tutorial adds 2 minutes but raises activation from 30 to 45 percent. Is it worth it?', 'Likely yes, if those users keep using it',
          ('No, because every extra minute is bad', 'not necessarily'), ('It makes no difference', 'it does'), ('Cannot be judged at all', 'can'),
          'Weigh value.'),
        Q('Which statement is accurate?', 'First experience and real usefulness matter more than sign-ups.',
          ('Sign-ups are the only number that really matters to a product.', 'not true'), ('Confusing onboarding helps retention.', 'not true'),
          ('Customer feedback is useless.', 'not true'), 'Measure value.'),
    ]))

# ------------------------------------------------------------------ Set 150: Microsoft case
MSFT = ('Documented history (Centre for Computing History): Bill Gates and Paul Allen wrote a BASIC interpreter (a program that '
        'lets people write and run simple code) for the MITS Altair 8800 computer in 1975, demonstrated it to MITS, and '
        'licensed it to MITS as Altair BASIC; this was Microsoft\'s first product. Lesson drawn by this course (an '
        'interpretation): build for one specific platform with real users, show that it works, and license software rather '
        'than selling ownership. One success story does not guarantee the same result for another business.')

s150 = SET('ENT.CASE.11',
    M=sec('Apply a documented early decision: build for one platform and license it', MSFT, [
        Q('According to the passage, what was Microsoft\'s first product?', 'Altair BASIC', ('A word processor for offices', 'later products'),
          ('A video game console', 'not stated'), ('An internet search engine', 'not stated'), 'Altair BASIC.'),
        Q('Which computer was it written for?', 'The MITS Altair 8800', ('Every computer at once', 'one platform'), ('A smartphone', 'not in 1975'),
          ('A tablet', 'not in 1975'), 'One platform.'),
        Q('How did the founders arrange use of the software with MITS?', 'They licensed it', ('They gave it away for free forever', 'not stated'),
          ('They sold the company to MITS', 'not stated'), ('They kept it secret', 'not stated'), 'Licensing.'),
        Q('Which lesson does this course draw?', 'Build for one platform, show it works, and license it',
          ('Build for every platform before testing any of them', 'opposite'), ('Sell full ownership of all code', 'opposite'),
          ('Never demonstrate software to a buyer', 'opposite'), 'Focus and license.'),
        Q('Which statement about the Microsoft case is accurate?', 'It shows one start, not a promise that every license deal succeeds.',
          ('It proves every software license will succeed.', 'one case'), ('It shows demos are useless.', 'opposite'),
          ('It shows one platform is always enough for any business forever.', 'overstated'), 'One story.'),
    ]),
    B=[cs('Writing a game for one console first', 'A small team making a game might build it for one console first, show it running, '
          'and let that console\'s store sell it under license. Later, they might bring it to other systems. The documented '
          'Microsoft facts are the Altair, the demonstration and the license. The idea that focusing on one platform first '
          'reduces risk is this course\'s interpretation.', [
        Q('Building for one console first is like what in the case?', 'Writing BASIC for the Altair', ('Writing for every computer', 'no'),
          ('Selling hardware', 'no'), ('Opening a store', 'no'), 'One platform.'),
        Q('Showing the game running is like what?', 'Demonstrating it to MITS', ('Hiding the software', 'no'), ('Advertising it on national TV', 'no'),
          ('Selling the company', 'no'), 'Demonstration.'),
        Q('Letting the store sell it under license is like what?', 'Licensing Altair BASIC to MITS', ('Giving away all of the code', 'no'),
          ('Selling ownership', 'no'), ('Keeping it private', 'no'), 'Licensing.'),
        Q('"They demonstrated it to MITS" is which kind of statement?', 'Documented fact', ('Course interpretation', 'documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'Recorded.'),
        Q('"Focusing first reduces risk" is which kind?', 'The course\'s interpretation', ('A documented quote from Gates', 'no'), ('A law', 'no'),
          ('A contract', 'no'), 'Lesson drawn.'),
    ], why='A learner who misses MAIN may not see why one platform and a license matter; a game for one console explains it.')],
    F1=sec('Apply it: focus and license a digital product', MSFT, [
        Q('A developer builds a plugin. Applying the lesson, which first step fits?', 'Build it for one popular platform and show a working demo',
          ('Build for ten platforms before any user tries it', 'unfocused'), ('Sell full ownership of the code to the first buyer', 'opposite'),
          ('Never show it to anyone', 'opposite'), 'Focus and demo.'),
        Q('She licenses the plugin at 15 dollars per site. 120 sites buy it. What is revenue?', '1,800 dollars', ('135 dollars', 'added'),
          ('120 dollars', 'count'), ('8 dollars', 'divided'), '120 x 15 = 1,800.', calc=lambda: 120 * 15 == 1800),
        Q('A company offers 2,000 dollars to own the plugin outright. Licensing has earned 1,800 in a year and is growing. What should she weigh?',
          'Ongoing license income versus a one-time sale', ('Only the bigger number today', 'ignores future'), ('Only the buyer\'s logo', 'irrelevant'),
          ('Nothing, because selling outright is always better', 'not always'), 'Compare paths.'),
        Q('The platform takes a 20 percent fee on each 15-dollar license. What does she keep per license?', '12 dollars', ('15 dollars', 'ignored fee'),
          ('3 dollars', 'fee'), ('18 dollars', 'added'), '15 x 0.8 = 12.', calc=lambda: 15 * 0.8 == 12),
        Q('Which detail is documented, not interpreted?', 'Altair BASIC was licensed to MITS', ('Licensing always beats selling', 'interpretation'),
          ('Every developer should start in 1975', 'not documented'), ('One platform guarantees success', 'not documented'), 'Recorded.'),
    ]),
    F2=sec('Handle the complications: platform dependence', MSFT, [
        Q('The platform she built for changes its rules and her plugin stops working. What risk does this show?', 'Depending on one platform carries risk',
          ('No risk, because platforms never change rules', 'they do'), ('Licensing is illegal', 'no'), ('Demos are useless', 'no'), 'Platform risk.'),
        Q('Someone says, "Microsoft started with BASIC, so I should write a BASIC interpreter." What is wrong?', 'The lesson is focus and licensing, not BASIC',
          ('Nothing, because BASIC itself is the secret', 'surface detail'), ('BASIC is illegal', 'no'), ('Microsoft never wrote BASIC', 'it did'),
          'Principle, not copy.'),
        Q('Her license terms do not say whether one purchase covers multiple sites. What problem arises?', 'Customers may use it more widely than intended',
          ('No problem, because license terms never matter', 'they do'), ('Revenue doubles automatically', 'no'), ('The code disappears', 'no'), 'Clear terms.'),
        Q('After a year, 25 percent of 120 licensed sites renew a yearly update plan at 10 dollars. What is renewal revenue?', '300 dollars',
          ('1,200 dollars', 'all renew'), ('30 dollars', 'count'), ('120 dollars', 'count'), '30 x 10 = 300.', calc=lambda: round(0.25 * 120) * 10 == 300),
        Q('Which statement is accurate?', 'Focus and license; each product must find its market.',
          ('One platform is always enough forever.', 'not true'), ('Licensing guarantees success.', 'not true'),
          ('Software must always be sold outright to buyers.', 'not true'), 'Test your own.'),
    ]))

# ------------------------------------------------------------------ Set 151: original content and rights
ORIG = ('Content creators build on ORIGINAL work: your own writing, photos, video, music and ideas. Using someone else\'s '
        'clips, songs, images or text usually needs permission or a license, even if you give credit. Some platforms have '
        'tools that detect copyrighted material and may block, mute or remove content. Keep records of licenses and permissions. '
        'If you film people, especially in private settings, get their permission to publish. Original work protects your '
        'channel and builds a distinct voice.')

s151 = SET('ENT.CONT.01',
    M=sec('Create original content and get permission for others\' material', ORIG, [
        Q('Does giving credit replace getting permission?', 'No, permission or a license is still needed',
          ('Yes, credit always makes any use legal', 'not true'), ('Yes, but only for music', 'no'), ('Yes, for short clips only', 'no'),
          'Credit is not permission.'),
        Q('What may platforms do with copyrighted material?', 'Block, mute or remove it', ('Pay the uploader extra', 'no'),
          ('Ignore it always', 'not always'), ('Make it go viral', 'no'), 'Detection tools.'),
        Q('What should a creator keep records of?', 'Licenses and permissions', ('Only follower counts', 'incomplete'),
          ('Only favorite comments', 'irrelevant'), ('Nothing', 'risky'), 'Proof of rights.'),
        Q('A creator films a friend at home and plans to publish. What should come first?', 'The friend\'s permission', ('A bigger camera', 'irrelevant'),
          ('More background music', 'irrelevant'), ('Nothing; friends never mind', 'ask'), 'Consent.'),
        Q('Why does original work help a channel?', 'It avoids rights problems and builds a distinct voice', ('It is always shorter', 'no'),
          ('Platforms pay double for original work automatically', 'no'), ('It needs no effort', 'no'), 'Protection and identity.'),
    ]),
    B=[cs('Cooking your own recipe versus copying a cookbook', 'If you cook your own recipe and share it, it is yours. If you '
          'photocopy pages from a famous cookbook and post them, that is the author\'s work, even if you write "credit to the '
          'author." Content works the same way: original material is yours to share; other people\'s material needs their '
          'permission or a license.', [
        Q('Your own recipe is like what?', 'Original content', ('Someone else\'s work', 'no'), ('A license', 'no'), ('A tax', 'no'),
          'Yours.'),
        Q('Photocopying cookbook pages is like what?', 'Using others\' work without permission', ('Original content', 'no'),
          ('A fair trade with the cookbook author', 'no'), ('A gift', 'no'), 'Not yours.'),
        Q('Does writing "credit to the author" make the copy fine?', 'No', ('Yes, always', 'no'), ('Only online', 'no'),
          ('Only on weekends', 'no'), 'Credit is not permission.'),
        Q('What do you need to share someone else\'s recipe pages?', 'Their permission or a license', ('Nothing', 'no'),
          ('A bigger kitchen to cook in', 'no'), ('More followers', 'no'), 'Permission.'),
        Q('Original material is what?', 'Yours to share', ('Never shareable', 'no'), ('Someone else\'s', 'no'), ('Illegal', 'no'),
          'You own it.'),
    ], why='A learner who misses MAIN may think credit is enough; a recipe versus a copied cookbook shows the difference.')],
    F1=sec('Apply it: check content before publishing', ORIG, [
        Q('A creator wants a 20-second clip of a popular movie in a review video. What should she do?', 'Check whether her use is permitted, or get a license',
          ('Use it, since 20 seconds is always fine', 'not a rule'), ('Use it with credit and assume that makes it fine', 'credit not permission'),
          ('Use the whole movie instead', 'worse'), 'Check rights.'),
        Q('A creator licenses 3 music tracks at 15 dollars each. What is the total?', '45 dollars', ('15 dollars', 'one'),
          ('18 dollars', 'added'), ('5 dollars', 'divided'), '3 x 15 = 45.', calc=lambda: 3 * 15 == 45),
        Q('A video was muted for copyrighted background music. What should the creator do next time?', 'Use licensed or original music',
          ('Use the same song again, louder', 'same problem'), ('Hide the song name', 'same problem'), ('Speed the song up', 'still infringing'),
          'Licensed audio.'),
        Q('A creator films strangers in a private café meeting and plans to post it. What should she consider?', 'Getting their permission before publishing',
          ('Nothing; anything filmed can be posted', 'not always'), ('Only the lighting', 'irrelevant'), ('Only the background music', 'irrelevant'),
          'Consent.'),
        Q('Which shows the strongest original work?', 'A tutorial with her own footage and explanation', ('A compilation of others\' clips', 'not original'),
          ('Reposted memes with no commentary of her own', 'not original'), ('A copied article read aloud', 'not original'), 'Original.'),
    ]),
    F2=sec('Handle the complications: claims and gray areas', ORIG, [
        Q('A rights holder claims her video. She believes she had a license. What should she do?', 'Use the platform\'s dispute process with her license records',
          ('Ignore the claim', 'loses revenue'), ('Upload the same video again and again until it sticks', 'escalates'), ('Insult the rights holder', 'harmful'),
          'Evidence and process.'),
        Q('A free music site says "free for personal use only." She runs ads on her channel. What is the issue?', 'Commercial use may not be allowed',
          ('No issue; free means any use', 'not true'), ('Ads make the music free', 'no'), ('Personal and commercial are the same', 'no'),
          'Read license terms.'),
        Q('An AI tool generates a song very similar to a famous one. What is the risk?', 'It may still raise rights issues', ('No risk; AI music is always free', 'not guaranteed'),
          ('It guarantees views', 'no'), ('It is automatically licensed', 'no'), 'Similarity risk.'),
        Q('A creator\'s original video is reuploaded by another account. What can she do?', 'Use the platform\'s copyright reporting process',
          ('Nothing can be done', 'there are processes'), ('Reupload their videos in revenge right away', 'escalates'), ('Delete her own channel', 'drastic'),
          'Report.'),
        Q('Which statement is accurate?', 'Original work and recorded permissions protect creators.',
          ('Giving credit always replaces getting permission.', 'not true'), ('Anything online is free to use.', 'not true'),
          ('Platforms never check rights.', 'they do'), 'Rights matter.'),
    ]))

# ------------------------------------------------------------------ Set 152: sponsorships and affiliate relationships (creators)
SPON = ('Creators may earn through SPONSORSHIPS (a brand pays for a mention or video) and AFFILIATE LINKS (a commission on '
        'sales). Both are material connections that should be disclosed clearly where viewers will notice, such as saying '
        '"This video is sponsored by..." at the start and labeling links. A platform\'s built-in disclosure tool is not '
        'automatically enough. Choose sponsors that fit your audience, agree in writing on deliverables, payment and '
        'deadlines, and never make claims about a product you cannot support.')

s152 = SET('ENT.CONT.02',
    M=sec('Disclose and manage sponsorships and affiliate links as a creator', SPON, [
        Q('Where should a sponsorship be disclosed in a video?', 'Clearly, where viewers notice, such as at the start',
          ('Only in the last second after the video ends', 'missed'), ('Only in a separate website nobody visits', 'hidden'),
          ('Nowhere, if the creator likes the product', 'still needed'), 'Clear and early.'),
        Q('Is a platform\'s built-in disclosure tool automatically enough?', 'Not automatically', ('Yes, always and in every case', 'not automatically'),
          ('Yes, if the video is short', 'no'), ('No, disclosures are banned', 'no'), 'Check clarity.'),
        Q('What should a sponsorship agreement include?', 'Deliverables, payment and deadlines', ('Only the brand\'s logo color', 'incomplete'),
          ('Only the creator\'s favorite snack', 'irrelevant'), ('Nothing; handshake deals are best', 'risky'), 'Written terms.'),
        Q('Why choose sponsors that fit the audience?', 'Mismatched sponsors can hurt trust', ('Any sponsor is always fine for any audience', 'not always'),
          ('Audiences never notice', 'they do'), ('Fit only matters for TV', 'no'), 'Trust.'),
        Q('A sponsor asks the creator to say its supplement "cures anxiety." What should she do?', 'Refuse claims she cannot support',
          ('Say it because she is paid', 'risky'), ('Say it quickly so nobody notices', 'still a claim'), ('Add it in small text', 'still a claim'),
          'Truthful claims.'),
    ]),
    B=[cs('A friend recommending a restaurant she owns', 'If a friend raves about a restaurant and later you learn she owns part of '
          'it, you might feel misled, even if the food is good. If she says up front, "I own part of this place, but I think '
          'you\'ll love it," you can decide for yourself. Sponsorship disclosure is that up-front sentence, said before the recommendation.', [
        Q('Why might you feel misled?', 'You did not know about her stake', ('The food was bad', 'not stated'), ('She was rude', 'no'),
          ('The restaurant closed early', 'no'), 'Hidden connection.'),
        Q('Her up-front sentence is like what?', 'A sponsorship disclosure', ('A secret', 'no'), ('An ad hidden in text', 'no'),
          ('A coupon', 'no'), 'Disclosure.'),
        Q('Does disclosure mean the food is bad?', 'No', ('Yes, always', 'no'), ('Only on weekends', 'no'), ('Only for pizza', 'no'),
          'It informs, not judges.'),
        Q('What does disclosure let you do?', 'Decide for yourself with full information', ('Get free food', 'no'), ('Avoid all restaurants in town from now on', 'no'),
          ('Ignore the friend', 'no'), 'Informed choice.'),
        Q('Her ownership stake is like what for a creator?', 'A paid sponsorship or commission', ('A random hobby', 'no'), ('A tax bill', 'no'),
          ('A count of channel subscribers', 'no'), 'Material connection.'),
    ], why='A learner who misses MAIN may not see why disclosure matters; a friend with a hidden stake explains it.')],
    F1=sec('Apply it: handle a sponsorship deal', SPON, [
        Q('A brand offers 800 dollars for one video mention. The creator\'s audience is gardeners; the brand sells car parts. What should she weigh?',
          'Whether the sponsor fits her audience', ('Only the payment amount', 'incomplete'), ('Only the brand\'s logo', 'irrelevant'),
          ('Nothing, because money is money', 'trust risk'), 'Fit.'),
        Q('A sponsorship pays 800 dollars, and she spends 6 hours on it. What is the pay per hour?', '133.33 dollars', ('800.00 dollars', 'total'),
          ('6.00 dollars', 'hours'), ('4,800.00 dollars', 'multiplied'), '800 / 6 = 133.33.', calc=lambda: round(800 / 6, 2) == 133.33),
        Q('An affiliate link pays 6 percent on 2,500 dollars of sales. What does she earn?', '150 dollars', ('6 dollars', 'percent'),
          ('15 dollars', 'moved decimal'), ('2,350 dollars', 'remainder'), '0.06 x 2,500 = 150.', calc=lambda: round(0.06 * 2500, 2) == 150),
        Q('Which disclosure is clearest at the start of a video?', '"This video is sponsored by Green Grow Tools."', ('"Thanks, GGT!"', 'unclear'),
          ('"#sp #ad #collab" in the description only', 'may be missed'), ('No disclosure at all', 'missing'), 'Plain and early.'),
        Q('The brand wants the video posted in 3 days, but the agreement says nothing about deadlines. What should she do?', 'Agree on the deadline in writing',
          ('Guess the deadline', 'risky'), ('Ignore the brand', 'unprofessional'), ('Post whenever, without telling them', 'dispute'),
          'Written terms.'),
    ]),
    F2=sec('Handle the complications: pressure and conflicts', SPON, [
        Q('A sponsor asks her not to mention that the video is sponsored. What should she do?', 'Disclose anyway or decline the deal',
          ('Agree to hide it', 'deceptive'), ('Hide it only in short videos', 'still deceptive'), ('Disclose only if viewers ask about it', 'not enough'),
          'Disclosure is required.'),
        Q('Two sponsors make competing products and both want exclusive mentions this month. What should she check?', 'Exclusivity terms in each agreement',
          ('Nothing, so she accepts both quietly', 'conflict'), ('Only which logo looks better', 'irrelevant'), ('Only follower comments', 'incomplete'),
          'Contract terms.'),
        Q('A sponsor is late paying 1,200 dollars, 30 days past the agreed date. What is a sensible first step?', 'Send a polite reminder referencing the agreement',
          ('Delete the video immediately without notice', 'escalates'), ('Post angry messages', 'unprofessional'), ('Do nothing ever', 'lost money'),
          'Follow up.'),
        Q('Affiliate income is 150 dollars on one month and 20 dollars the next. What does this show?', 'Affiliate income can be uneven',
          ('Affiliate income is always steady', 'not true'), ('The link stopped existing', 'not necessarily'), ('Taxes doubled', 'unrelated'),
          'Variable income.'),
        Q('Which statement is accurate?', 'Disclose paid connections clearly and keep claims true.',
          ('Disclosures are optional for small creators with few viewers.', 'not true'), ('Sponsors decide what is truthful.', 'creator responsible'),
          ('Built-in tools are always enough.', 'not automatically'), 'Honesty.'),
    ]))

# ------------------------------------------------------------------ Set 153: being seen versus being eligible to earn
SEEN = ('Posting content and getting views is not the same as being ELIGIBLE TO EARN from a platform. For example, earning ad '
        'revenue on YouTube requires joining the YouTube Partner Program, which has eligibility thresholds and policies '
        'separate from simply posting videos; the thresholds have changed over time, so check the official help page rather '
        'than old articles. Platforms can also change programs. Creators often earn through several routes at once: '
        'platform programs, sponsorships, affiliate links, their own products, and services.')

s153 = SET('ENT.CONT.03',
    M=sec('Distinguish getting views from being eligible to earn on a platform', SEEN, [
        Q('Does getting views automatically mean earning ad revenue?', 'No; platform programs have eligibility rules',
          ('Yes, every view always pays the creator', 'not true'), ('Yes, after the first video', 'not true'),
          ('Yes, if the video has music', 'irrelevant'), 'Eligibility.'),
        Q('Where should a creator check current YouTube eligibility thresholds?', 'The official YouTube help page', ('A video from several years ago', 'outdated'),
          ('A friend\'s memory of the rules', 'unreliable'), ('A random comment', 'unreliable'), 'Official source.'),
        Q('What does the passage say about thresholds?', 'They have changed over time', ('They never change', 'they have'),
          ('They are the same on every platform', 'not stated'), ('They are secret', 'no'), 'Changes.'),
        Q('Which is a way creators earn beyond platform programs?', 'Selling their own products', ('Buying fake followers', 'harmful'),
          ('Hiding sponsorships', 'deceptive'), ('Copying others\' videos', 'rights issue'), 'Multiple routes.'),
        Q('Why should creators not rely on one program?', 'Platforms can change programs', ('Programs never change', 'they can'),
          ('Other income is illegal', 'no'), ('Views always pay the same', 'no'), 'Diversify.'),
    ]),
    B=[cs('Playing music on the street versus being hired', 'A musician playing on a busy street may draw a crowd, but that is not '
          'the same as being booked for a paid concert. Concerts have their own requirements and contracts. Online, getting '
          'views is like drawing a crowd; joining a platform\'s earning program is like being booked, with its own rules to '
          'meet and keep meeting.', [
        Q('Drawing a crowd on the street is like what online?', 'Getting views', ('Being in a paid program', 'no'), ('Filing taxes', 'no'),
          ('Signing a lease', 'no'), 'Attention.'),
        Q('Being booked for a paid concert is like what?', 'Being accepted into an earning program', ('Getting one view', 'no'),
          ('Posting a photo', 'no'), ('Changing a profile picture online', 'no'), 'Eligibility and terms.'),
        Q('Does a crowd automatically mean a paid booking?', 'No', ('Yes, always', 'no'), ('Only in summer', 'no'), ('Only downtown', 'no'),
          'Separate requirements.'),
        Q('What do concerts have that street playing may not?', 'Requirements and contracts', ('An audience of passersby', 'both'), ('Music', 'both'),
          ('Instruments', 'both'), 'Formal terms.'),
        Q('What is the main lesson?', 'Attention and eligibility to earn are different', ('Crowds are useless', 'no'),
          ('Concerts are illegal for street musicians', 'no'), ('Music is free', 'no'), 'Distinguish them.'),
    ], why='A learner who misses MAIN may assume views pay automatically; street music versus a booked concert shows the gap.')],
    F1=sec('Apply it: plan earning routes', SEEN, [
        Q('A creator has growing views but has not checked program requirements. What should she do first?', 'Read the official program requirements and policies',
          ('Assume she is already earning from every view', 'may not be'), ('Buy views to speed things up', 'violates policies'), ('Quit posting', 'premature'),
          'Check official rules.'),
        Q('She earns 120 dollars from ads, 300 from a sponsor and 80 from affiliate links in a month. What is the total?', '500 dollars',
          ('420 dollars', 'missed affiliate'), ('300 dollars', 'sponsor only'), ('200 dollars', 'missed sponsor'), '120 + 300 + 80 = 500.',
          calc=lambda: 120 + 300 + 80 == 500),
        Q('What share of that total comes from ads?', '24 percent', ('120 percent', 'count'), ('60 percent', 'sponsor'), ('16 percent', 'affiliate'),
          '120 / 500 = 0.24.', calc=lambda: 120 / 500 == 0.24),
        Q('A blog post from years ago lists program thresholds. What should she do?', 'Confirm with the current official page', ('Trust the old blog post fully as written', 'outdated'),
          ('Ignore all rules', 'risky'), ('Ask a stranger', 'unreliable'), 'Current source.'),
        Q('Which plan reduces dependence on one program?', 'Building products, sponsorships and an email list too', ('Relying only on ad revenue from one single platform', 'concentrated'),
          ('Posting only on one app', 'concentrated'), ('Buying followers', 'harmful'), 'Diversify.'),
    ]),
    F2=sec('Handle the complications: policy changes and violations', SEEN, [
        Q('A platform changes its program and her ad income drops by half. What helps most?', 'Other income routes she has already built',
          ('Buying views to recover the lost income', 'violates'), ('Quitting immediately', 'premature'), ('Ignoring the change', 'passive'), 'Diversification.'),
        Q('A service offers to sell her views to reach a threshold faster. What is the risk?', 'It can violate policies and get her removed',
          ('No risk, because bought views are always allowed', 'not true'), ('It guarantees acceptance', 'no'), ('It improves trust', 'no'), 'Policy risk.'),
        Q('Ad income falls from 400 to 200 dollars a month. What is the percent decrease?', '50 percent', ('200 percent', 'dollar change'),
          ('100 percent', 'not all'), ('25 percent', 'miscalculated'), '200 / 400 = 0.5.', calc=lambda: (400 - 200) / 400 == 0.5),
        Q('Her video is demonetized for a policy issue she does not understand. What should she do?', 'Read the policy and use the official review or appeal process',
          ('Repost it many times', 'escalates'), ('Complain only in the comments of other creators\' videos', 'not a process'), ('Delete her channel', 'drastic'),
          'Use official channels.'),
        Q('Which statement is accurate?', 'Views and eligibility differ, and rules can change.',
          ('Every view always pays the creator the same amount.', 'not true'), ('Program thresholds never change.', 'they have'),
          ('One income route is always enough.', 'risky'), 'Know the rules.'),
    ]))

# ------------------------------------------------------------------ Set 154: audience trust and diversification
TRUSTC = ('A creator\'s main asset is AUDIENCE TRUST: viewers believe the creator is honest and useful. Trust is built by '
          'consistent, accurate content, disclosed sponsorships, admitting mistakes, and respecting the audience\'s time. It is '
          'easily lost through hidden ads, misleading claims or low-quality promotions. DIVERSIFICATION means not depending on '
          'one platform or income source: an email list, a website, and more than one channel or product reduce the risk of '
          'losing everything to one change.')

s154 = SET('ENT.CONT.04',
    M=sec('Protect audience trust and diversify platforms and income', TRUSTC, [
        Q('What is a creator\'s main asset according to the passage?', 'Audience trust', ('The camera model', 'tool'),
          ('The logo design', 'minor'), ('The editing software', 'tool'), 'Trust.'),
        Q('Which action builds trust?', 'Admitting a mistake and correcting it', ('Hiding a sponsorship', 'loses trust'),
          ('Making misleading claims', 'loses trust'), ('Promoting low-quality products for money', 'loses trust'), 'Honesty.'),
        Q('What is diversification for a creator?', 'Not depending on one platform or income source', ('Posting the same video ten times', 'no'),
          ('Using only one platform forever', 'opposite'), ('Buying followers on many different apps', 'harmful'), 'Spread risk.'),
        Q('Which is an owned channel?', 'An email list people joined', ('A single social media account', 'platform-controlled'),
          ('A viral video', 'temporary'), ('A comment section', 'platform-controlled'), 'Owned audience.'),
        Q('What can quickly lose trust?', 'Hidden ads', ('Consistent, accurate content', 'builds'), ('Disclosed sponsorships', 'builds'),
          ('Respecting viewers\' time', 'builds'), 'Deception.'),
    ]),
    B=[cs('A trusted local newspaper', 'People trust a local newspaper because it reports accurately, labels ads as ads, and prints '
          'corrections. If it hid paid articles as news, readers would stop trusting it. And a newspaper that also has a website '
          'and a newsletter is not ruined if one delivery route fails. Creators work the same way: honesty builds trust, and more '
          'than one channel spreads risk.', [
        Q('Labeling ads as ads is like what for a creator?', 'Disclosing sponsorships', ('Hiding paid sponsorships', 'no'),
          ('Deleting comments', 'no'), ('Buying views', 'no'), 'Transparency.'),
        Q('Printing corrections is like what?', 'Admitting and fixing mistakes', ('Ignoring errors in old stories', 'no'), ('Blaming readers', 'no'),
          ('Deleting old posts', 'no'), 'Accountability.'),
        Q('Hiding paid articles as news would do what?', 'Lose readers\' trust', ('Gain readers\' trust', 'no'), ('Change nothing', 'no'),
          ('Lower costs', 'not the point'), 'Deception.'),
        Q('A newspaper with a website and a newsletter is like what?', 'A diversified creator', ('A one-platform creator', 'no'),
          ('A creator with no audience', 'no'), ('A competitor', 'no'), 'Multiple channels.'),
        Q('Why is the newspaper not ruined if one route fails?', 'It has other ways to reach readers', ('Routes never fail', 'they can'),
          ('Readers do not care how it arrives', 'no'), ('It is free', 'no'), 'Spread risk.'),
    ], why='A learner who misses MAIN may not see how trust and diversification connect; a local newspaper shows both.')],
    F1=sec('Apply it: protect trust and reduce risk', TRUSTC, [
        Q('A creator recommended a gadget that later proved faulty. What builds trust?', 'Posting an honest update about the problem',
          ('Deleting the video quietly', 'hides'), ('Blaming viewers for buying the gadget', 'harmful'), ('Promoting it more', 'worse'),
          'Admit and correct.'),
        Q('90 percent of her income comes from one platform\'s program. What is the main risk?', 'A program change could remove most income',
          ('No risk, because programs never change', 'they can'), ('Income will double', 'no'), ('Taxes vanish', 'no'), 'Concentration.'),
        Q('She invites viewers to an email list and 400 of 8,000 regular viewers join. What percent joined?', '5 percent',
          ('400 percent', 'count'), ('20 percent', 'misdivided'), ('0.5 percent', 'moved decimal'), '400 / 8,000 = 0.05.', calc=lambda: 400 / 8000 == 0.05),
        Q('A sponsor offers a large fee for a product she would not use. What protects trust?', 'Declining sponsors she does not believe in',
          ('Accepting every offer', 'erodes trust'), ('Hiding the sponsor', 'deceptive'), ('Exaggerating the product to earn the fee', 'misleading'),
          'Selective sponsorship.'),
        Q('Income sources: ads 40 percent, sponsors 35 percent, own products 25 percent. Which is largest?', 'Ads', ('Sponsors', '35'),
          ('Own products', '25'), ('They are all equal', 'differ'), '40 > 35 > 25.', calc=lambda: 40 > 35 > 25),
    ]),
    F2=sec('Handle the complications: trust under pressure', TRUSTC, [
        Q('Viewers accuse her of hiding a sponsorship she did disclose. What should she do?', 'Calmly point to the disclosure and keep it clear',
          ('Delete all comments', 'hostile'), ('Stop disclosing sponsorships to avoid the attention', 'worse'), ('Argue angrily', 'harmful'), 'Calm clarity.'),
        Q('A platform suspends her account for two weeks by mistake. What helps her keep earning?', 'Her email list, website and other channels',
          ('Nothing could help', 'diversification helps'), ('Creating fake accounts', 'violates rules'), ('Buying new followers on another app', 'harmful'),
          'Owned channels.'),
        Q('She wants to post daily but quality drops and viewers complain. What should she weigh?', 'Quality and trust over volume',
          ('Volume always beats quality', 'not true'), ('Complaints never matter', 'they do'), ('Posting hourly instead', 'worse'),
          'Respect the audience.'),
        Q('Her own product earns 1,200 dollars from 80 buyers. What is the average per buyer?', '15 dollars', ('80 dollars', 'count'),
          ('1,200 dollars', 'total'), ('96,000 dollars', 'multiplied'), '1,200 / 80 = 15.', calc=lambda: 1200 / 80 == 15),
        Q('Which statement is accurate?', 'Honesty protects trust; more channels reduce risk.',
          ('Trust cannot be lost once earned.', 'it can'), ('One platform is always the safest choice for creators.', 'risky'),
          ('Hidden ads build trust.', 'they harm it'), 'Trust and diversity.'),
    ]))

# ------------------------------------------------------------------ Set 155: creator costs and uneven income
CCOST = ('Creating content has COSTS: equipment, software subscriptions, music licenses, editing help, travel and the creator\'s '
         'own time. Creator INCOME is often UNEVEN: sponsorships arrive irregularly, ad revenue can swing by season or with '
         'platform changes, and product launches come in bursts. Plan with a monthly budget based on a cautious estimate, keep '
         'a cash reserve for slow months, set aside money for taxes, and track income by source so you can see trends.')

s155 = SET('ENT.CONT.05',
    M=sec('Budget creator costs and plan for uneven income', CCOST, [
        Q('Which is a creator cost?', 'Music licenses and editing software', ('Followers\' birthdays and names', 'no'), ('Viewers\' comments', 'no'),
          ('The platform\'s logo', 'no'), 'Business costs.'),
        Q('Why is creator income often uneven?', 'Sponsors and ad revenue vary month to month', ('Income is always fixed by law', 'not true'),
          ('Platforms pay creators the same every month', 'not true'), ('Viewers pay a monthly salary', 'no'), 'Variable sources.'),
        Q('What helps in slow months?', 'A cash reserve', ('Spending everything in good months', 'risky'), ('Ignoring the budget', 'risky'),
          ('Buying more equipment', 'worse'), 'Buffer.'),
        Q('Why track income by source?', 'To see trends in each source', ('To hide income', 'improper'), ('To confuse the budget', 'no'),
          ('Because sources never change', 'they do'), 'Visibility.'),
        Q('What should a monthly budget be based on?', 'A cautious estimate of income', ('The best month ever', 'risky'),
          ('A guess of doubling each month', 'risky'), ('A competitor\'s income', 'irrelevant'), 'Conservative planning.'),
    ]),
    B=[mathb('Averaging uneven months', 'To plan with uneven income, average several months: add them and divide by the number of '
             'months. Example: 600, 1,400, 400 and 1,000 total 3,400; 3,400 / 4 = 850 a month. A cautious budget might use a '
             'number below the average, or the lowest recent month, so slow months do not cause a crisis or force rushed decisions.', [
        Q('Months: 500, 900, 700. What is the average?', '700', ('2,100', 'total'), ('900', 'highest'), ('500', 'lowest'),
          '2,100 / 3 = 700.', calc=lambda: (500 + 900 + 700) / 3 == 700),
        Q('600, 1,400, 400 and 1,000 total what?', '3,400', ('850', 'average'), ('1,400', 'highest'), ('2,400', 'missed one'),
          '600 + 1,400 + 400 + 1,000 = 3,400.', calc=lambda: 600 + 1400 + 400 + 1000 == 3400),
        Q('3,400 / 4 is what?', '850', ('3,400', 'total'), ('1,360', 'misdivided'), ('425', 'divided by 8'), '850.', calc=lambda: 3400 / 4 == 850),
        Q('What is a cautious number to budget from in that example?', 'The lowest recent month, 400', ('The highest month, 1,400', 'risky'),
          ('The total, 3,400', 'not monthly'), ('Double the average', 'risky'), 'Plan for slow months.'),
        Q('Months: 300, 1,200, 600, 900. What is the average?', '750', ('3,000', 'total'), ('1,200', 'highest'), ('600', 'one month'),
          '3,000 / 4 = 750.', calc=lambda: (300 + 1200 + 600 + 900) / 4 == 750),
    ], why='A learner who misses MAIN may not average uneven income; this practices averages and a cautious choice.')],
    F1=sec('Apply it: budget a creator business', CCOST, [
        Q('Monthly costs: software 45, music 20, storage 10, editing help 200. What is the total?', '275 dollars', ('75 dollars', 'missed editing'),
          ('200 dollars', 'editing only'), ('255 dollars', 'missed music'), '45 + 20 + 10 + 200 = 275.', calc=lambda: 45 + 20 + 10 + 200 == 275),
        Q('Income over 4 months: 900, 300, 1,500, 500. What is the average?', '800 dollars', ('3,200 dollars', 'total'),
          ('1,500 dollars', 'highest'), ('300 dollars', 'lowest'), '3,200 / 4 = 800.', calc=lambda: (900 + 300 + 1500 + 500) / 4 == 800),
        Q('In the 300-dollar month, costs were 275. How much was left before taxes?', '25 dollars', ('300 dollars', 'income'),
          ('575 dollars', 'added'), ('275 dollars', 'costs'), '300 - 275 = 25.', calc=lambda: 300 - 275 == 25),
        Q('She wants a reserve of 3 months of costs. How much is that?', '825 dollars', ('275 dollars', 'one month'), ('550 dollars', 'two months'),
          ('1,100 dollars', 'four months'), '275 x 3 = 825.', calc=lambda: 275 * 3 == 825),
        Q('A sponsor pays 1,200 dollars once. What is a sensible use?', 'Set aside taxes, build the reserve, then invest',
          ('Spend it all on new camera gear that same week', 'risky'), ('Assume it repeats every month', 'risky'), ('Ignore taxes', 'risky'),
          'Plan the windfall.'),
    ]),
    F2=sec('Handle the complications: gear temptation and slumps', CCOST, [
        Q('After a great month, she wants a 2,500-dollar camera. Her average monthly profit is 500. What should she weigh?', 'Whether the camera will raise income enough',
          ('Buy it now, because one month was great', 'risky'), ('Buy two cameras', 'worse'), ('Borrow without a plan', 'risky'), 'Return on gear.'),
        Q('Ad income drops 40 percent from 600 dollars. What is the new amount?', '360 dollars', ('240 dollars', 'drop amount'),
          ('560 dollars', 'subtracted 40'), ('840 dollars', 'added'), '600 x 0.6 = 360.', calc=lambda: round(600 * 0.6, 2) == 360),
        Q('A slump lasts 3 months. What should she adjust first?', 'Cut nonessential costs and lean on her reserve',
          ('Spend more on new gear to feel better about it', 'worse'), ('Stop paying taxes', 'unlawful'), ('Quit immediately', 'premature'), 'Manage the slump.'),
        Q('She sets aside 25 percent of income for taxes (a practice assumption). Income is 1,600 dollars. How much is set aside?', '400 dollars',
          ('25 dollars', 'percent'), ('1,200 dollars', 'remainder'), ('160 dollars', 'ten percent'), '0.25 x 1,600 = 400.',
          calc=lambda: 0.25 * 1600 == 400),
        Q('Which statement is accurate?', 'Budget cautiously, keep a reserve and track sources.',
          ('Creator income is always steady.', 'not true'), ('Equipment always pays for itself.', 'not always'),
          ('Taxes do not apply to creators\' online income.', 'they do'), 'Plan for unevenness.'),
    ]))

# ------------------------------------------------------------------ Set 156: Craigslist case
CL = ('Documented history (Encyclopedia.com): Craig Newmark began emailing San Francisco event notices to friends in 1995. '
      'People asked to join, and they started posting other things such as jobs and apartments. The list moved to the web and '
      'was incorporated as a company in 1999. Lesson drawn by this course (an interpretation): start by sharing something '
      'useful with people who asked for it, listen to what they start using it for, and grow the format around their needs. '
      'One success story does not guarantee the same result for another business.')

s156 = SET('ENT.CASE.12',
    M=sec('Apply a documented early decision: grow a useful list around what people ask for', CL, [
        Q('According to the passage, how did it start?', 'An email list of local event notices for friends',
          ('A paid newspaper with printed classified ads', 'not stated'), ('A television show about San Francisco local events', 'not stated'),
          ('A mobile app for dating', 'not stated'), 'Email list.'),
        Q('What did people start posting besides events?', 'Jobs and apartments', ('Only cat photos', 'not stated'), ('Only family recipes', 'not stated'),
          ('Nothing else', 'they posted more'), 'Expanded use.'),
        Q('When was it incorporated as a company?', '1999', ('1995', 'start of emails'), ('2007', 'not stated'), ('1975', 'not stated'),
          'Documented year.'),
        Q('Which lesson does this course draw?', 'Share something useful with people who asked, then listen',
          ('Buy a large email list of strangers first to grow fast', 'opposite'), ('Ignore what users post', 'opposite'),
          ('Charge everyone before offering anything useful', 'not the lesson'), 'Useful and responsive.'),
        Q('Which statement about the Craigslist case is accurate?', 'It shows one path, not proof for every email list.',
          ('It proves every email list becomes a big company.', 'one case'), ('It shows users never change a product.', 'opposite'),
          ('It shows permission does not matter.', 'opposite'), 'One story.'),
    ]),
    B=[cs('A neighborhood bulletin board', 'Imagine pinning a sheet of local events on a café bulletin board. Soon neighbors add '
          'notes about lost pets, rooms for rent and jobs. You notice and add sections for each. You did not plan those '
          'sections; you followed what people used the board for. The documented Craigslist facts are the email list, the new '
          'kinds of posts and the dates; the bulletin board comparison is this course\'s explanation.', [
        Q('The first sheet of local events is like what?', 'The original email list of events', ('A paid daily newspaper in print', 'no'),
          ('A tax form', 'no'), ('A store sign', 'no'), 'The start.'),
        Q('Neighbors adding notes about rooms and jobs is like what?', 'Users posting jobs and apartments', ('The owner deleting posts', 'no'),
          ('A competitor\'s ad on the board', 'no'), ('A government notice', 'no'), 'New uses.'),
        Q('Adding sections for each kind of note is like what?', 'Growing the format around users\' needs', ('Ignoring users', 'no'),
          ('Closing the board', 'no'), ('Charging money for every pin on it', 'not stated'), 'Responsive growth.'),
        Q('"It was incorporated in 1999" is which kind of statement?', 'Documented fact', ('Course explanation', 'documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'Recorded.'),
        Q('The bulletin board comparison is which kind?', 'The course\'s explanation', ('A documented fact from records', 'no'), ('A law', 'no'),
          ('A contract', 'no'), 'Interpretation.'),
    ], why='A learner who misses MAIN may not see how use shaped the product; a neighborhood bulletin board makes it concrete.')],
    F1=sec('Apply it: grow a list responsibly', CL, [
        Q('Ana emails a weekly list of local craft fairs to 40 friends who asked for it. Readers start replying with booth swaps. What fits the lesson?',
          'Consider adding a booth-swap section', ('Ignore the replies', 'misses need'),
          ('Sell the readers\' email addresses', 'violates trust'), ('Stop the list', 'premature'), 'Follow use.'),
        Q('The list grows from 40 to 260 subscribers in a year. How many more?', '220', ('260', 'new total'), ('300', 'added'),
          ('40', 'start'), '260 - 40 = 220.', calc=lambda: 260 - 40 == 220),
        Q('What percent growth is that?', '550 percent', ('220 percent', 'count'), ('650 percent', 'ratio'), ('15 percent', 'reversed'),
          '220 / 40 = 5.5.', calc=lambda: 220 / 40 == 5.5),
        Q('Before adding strangers to the list, what should Ana do?', 'Let people join by choice with a clear sign-up', ('Add any email she can find', 'no permission'),
          ('Buy a list of addresses from a website quickly', 'no permission'), ('Copy a competitor\'s list', 'no permission'), 'Permission.'),
        Q('Which detail is documented, not interpreted?', 'People asked to join the event emails', ('Listening always leads to success', 'interpretation'),
          ('Every list should add jobs', 'not documented'), ('Email lists guarantee companies', 'not documented'), 'Recorded.'),
    ]),
    F2=sec('Handle the complications: growth, spam and rules', CL, [
        Q('As Ana\'s list grows, some readers post spam offers. What should she do?', 'Set clear posting rules and moderate',
          ('Allow anything to keep growth fast', 'harms readers'), ('Close the list immediately', 'drastic'), ('Add more spam', 'worse'),
          'Protect usefulness.'),
        Q('Readers ask her to charge for job posts to reduce spam. What should she consider?', 'Whether a small fee fits readers\' needs and her goals',
          ('Nothing; fees are always wrong', 'not necessarily'), ('Charging every reader a monthly fee just to read', 'not asked'), ('Ignoring them', 'misses feedback'),
          'Listen and decide.'),
        Q('Someone says, "Craigslist started as email, so email lists always become companies." What is wrong?', 'One case does not prove a general rule',
          ('Nothing, because it always happens that way', 'not true'), ('Email is illegal', 'no'), ('Craigslist never used email', 'it did'), 'Avoid overgeneralizing.'),
        Q('Her commercial emails must include an opt-out and a valid postal address. Which address could she use for privacy?', 'A registered PO Box or private mailbox',
          ('No address at all', 'required'), ('A made-up address', 'invalid'), ('A friend\'s address without asking', 'improper'),
          'Valid mailbox.'),
        Q('Which statement is accurate?', 'Serve people who asked and listen; results vary.',
          ('Email lists should be built from bought addresses.', 'no permission'), ('Users never change how a product is used.', 'they do'),
          ('One story proves a rule.', 'not true'), 'Learn the principle.'),
    ]))

SETS = [s146, s147, s148, s149, s150, s151, s152, s153, s154, s155, s156]
