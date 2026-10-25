"""Entrepreneurship sets 91-96: Foundation 11 (continued), measuring marketing; Blue Ribbon Sports and
Madam C. J. Walker cases. Ad costs and rates are practice assumptions."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 91: organic versus paid; a small ad test
ADS = ('ORGANIC marketing reaches people without paying the platform for each view: posts, word of mouth, search. It '
       'costs time and builds slowly. PAID marketing (ads) buys reach quickly, but stops when the money stops. Before '
       'spending much, run a SMALL AD TEST: set a fixed budget you can afford to lose (for example 50 dollars), one clear '
       'goal (such as sign-ups), one audience, and a set time. Then compare cost per result: total spend / results. '
       'Example: 50 dollars and 10 sign-ups = 5 dollars per sign-up.')

s91 = SET('ENT.MKT.07',
    M=sec('Compare organic and paid reach and run a small, measured ad test', ADS, [
        Q('What is organic marketing?', 'Reaching people without paying per view', ('Marketing that uses only farm products', 'pun'),
          ('Ads that cost the most money per click', 'that is paid'), ('A legal filing for a brand name', 'unrelated'),
          'Unpaid reach such as posts and word of mouth.'),
        Q('What happens to paid reach when spending stops?', 'It stops too', ('It doubles for free', 'not true'),
          ('It becomes organic forever', 'not true'), ('It grows by itself every month', 'not true'), 'Paid reach depends on spend.'),
        Q('A 60-dollar test brings 12 sign-ups. What is the cost per sign-up?', '5 dollars', ('12 dollars', 'count'),
          ('72 dollars', 'added'), ('0.20 dollars', 'reversed'), '60 / 12 = 5.', calc=lambda: 60 / 12 == 5),
        Q('What budget should a first ad test use?', 'An amount the owner can afford to lose', ('All of the business\'s savings at once', 'too risky'),
          ('A loan taken out just for ads', 'too risky'), ('No budget limit at all', 'uncontrolled'), 'Limit the risk.'),
        Q('Why test with one goal and one audience?', 'So the result is clear', ('Because more goals are illegal', 'not true'),
          ('Because one audience always buys', 'not true'), ('So no results are measured', 'opposite'), 'Clear tests teach.'),
    ]),
    B=[mathb('Cost per result', 'Cost per result = total spent / number of results. Example: 80 dollars for 16 clicks is 80 / 16 '
             '= 5 dollars per click. Compare two tests by their cost per result: lower is cheaper for the same kind of result. '
             'Check: cost per result x results should equal total spent (5 x 16 = 80). If results are 0, cost per result '
             'cannot be calculated: the test found nothing.', [
        Q('100 dollars for 20 results. What is the cost per result?', '5 dollars', ('20 dollars', 'count'), ('2,000 dollars', 'multiplied'),
          ('0.20 dollars', 'reversed'), '100 / 20 = 5.', calc=lambda: 100 / 20 == 5),
        Q('45 dollars for 9 results. What is the cost per result?', '5 dollars', ('9 dollars', 'count'), ('4 dollars', 'arithmetic slip'),
          ('405 dollars', 'multiplied'), '45 / 9 = 5.', calc=lambda: 45 / 9 == 5),
        Q('Test A: 4 dollars per result. Test B: 6 dollars per result. Which is cheaper?', 'Test A', ('Test B', 'higher'),
          ('They are the same', 'differ'), ('Cannot tell', 'can tell'), 'Lower cost per result.'),
        Q('How do you check 5 dollars per result for 16 results?', '5 x 16 = 80, the total spent', ('5 + 16 = 21', 'not a check'),
          ('16 / 5 = 3.2, the cost each', 'not a check'), ('5 - 16', 'not a check'), 'Multiply back.'),
        Q('120 dollars for 8 results. What is the cost per result?', '15 dollars', ('8 dollars', 'count'), ('12 dollars', 'guessed'),
          ('960 dollars', 'multiplied'), '120 / 8 = 15.', calc=lambda: 120 / 8 == 15),
    ], why='A learner who misses MAIN may not compute cost per result; this practices the division and a check.')],
    F1=sec('Apply it: design and judge an ad test', ADS, [
        Q('A candle maker has 40 dollars to test ads. Which plan is best?', 'One audience, one goal (orders), 7 days, 40 dollars',
          ('Five audiences, three goals and no end date, for 40 dollars', 'unclear results'), ('Spend 400 dollars on credit', 'too risky'),
          ('No goal; just see what happens', 'unmeasurable'), 'Focused and limited.'),
        Q('Ad A: 50 dollars, 5 orders. Ad B: 50 dollars, 2 orders. What is Ad A\'s cost per order?', '10 dollars', ('25 dollars', 'Ad B'),
          ('5 dollars', 'count'), ('250 dollars', 'multiplied'), '50 / 5 = 10.', calc=lambda: 50 / 5 == 10),
        Q('Each order brings 14 dollars of contribution. Ad A costs 10 dollars per order. Does Ad A pay for itself on the first '
          'order?', 'Yes, by 4 dollars per order', ('No, it loses 4 dollars per order', 'reversed'), ('It breaks exactly even', 'no'),
          ('Cannot tell from the numbers', 'can tell'), '14 - 10 = 4.', calc=lambda: 14 - 10 == 4),
        Q('Ad B costs 25 dollars per order with the same 14-dollar contribution. What happens on each order?', 'It loses 11 dollars',
          ('It earns 11 dollars', 'reversed'), ('It earns 39 dollars', 'added'), ('It breaks even', 'no'), '14 - 25 = -11.',
          calc=lambda: 14 - 25 == -11),
        Q('Organic posts brought 6 orders this month at no ad cost but took 8 hours. What should the owner also consider?',
          'The value of her time', ('Nothing; organic is always free', 'time has value'), ('Only the logo', 'irrelevant'),
          ('Only competitors\' ad budgets', 'irrelevant'), 'Organic costs time.'),
    ]),
    F2=sec('Handle the complications: misleading test results', ADS, [
        Q('An ad got 2,000 likes but 0 orders. The goal was orders. How should the owner judge it?', 'It did not meet the goal',
          ('It succeeded because likes are high', 'wrong goal'), ('It doubled sales', 'no sales'), ('It cannot be judged', 'it can'),
          'Measure against the goal.'),
        Q('A test ran for 1 day with 3 dollars spent and 1 order. What is the problem with scaling up now?', 'The test is too small to trust',
          ('Nothing; one order proves everything', 'too small'), ('Ads always work after one day', 'not true'),
          ('Small tests are illegal', 'no'), 'Small samples mislead.'),
        Q('A platform\'s ad dashboard shows 40 "conversions," but the shop recorded only 22 orders from that ad. What should the '
          'owner rely on?', 'Her own order records, after checking the definitions', ('Only the platform\'s number', 'may count differently'),
          ('Neither, guess instead', 'unreliable'), ('The bigger of the two numbers, to feel good about it', 'biased'), 'Verify with your own data.'),
        Q('Ads stopped and orders fell from 30 to 8 a month. What does this suggest?', 'Most orders depended on paid reach',
          ('Organic marketing was doing most of the work', 'opposite'), ('Ads had no effect', 'opposite'), ('Prices doubled', 'not stated'),
          'Paid reach stops with spending.'),
        Q('Which statement is accurate?', 'Testing small first is safer than a big untested spend.',
          ('Big untested spends are always safer than small tests.', 'riskier'), ('Likes always equal sales.', 'not true'),
          ('Organic marketing costs nothing at all.', 'costs time'), 'Test small first.'),
    ]))

# ------------------------------------------------------------------ Set 92: reach, leads, sales, conversion
FUNNEL = ('Marketing results can be followed in steps. REACH is how many people saw your message. LEADS are people who '
          'showed interest, such as signing up or asking a question. SALES are people who paid. Each step has a '
          'CONVERSION RATE: leads / reach, and sales / leads. Example: 2,000 reached, 100 leads (5 percent), 20 sales '
          '(20 percent of leads). Finding the step where most people drop off shows what to improve: the message, the '
          'offer or the follow-up.')

s92 = SET('ENT.MKT.08',
    M=sec('Follow reach, leads and sales and find the weakest step', FUNNEL, [
        Q('What is a lead?', 'A person who showed interest', ('A person who has already paid twice', 'that is a sale'),
          ('A person who never saw the message', 'not reached'), ('A heavy metal used in old pipes', 'pun'), 'Interest, not yet a sale.'),
        Q('2,000 reached and 100 leads. What is the lead rate?', '5 percent', ('20 percent', 'sales rate'), ('100 percent', 'count'),
          ('2 percent', 'misdivided'), '100 / 2,000 = 0.05.', calc=lambda: 100 / 2000 == 0.05),
        Q('100 leads and 20 sales. What is the sales rate from leads?', '20 percent', ('5 percent', 'lead rate'), ('1 percent', 'of reach'),
          ('80 percent', 'non-buyers'), '20 / 100 = 0.20.', calc=lambda: 20 / 100 == 0.2),
        Q('Why find the step where most people drop off?', 'It shows what to improve', ('It proves marketing never works', 'no'),
          ('It removes the need to measure', 'opposite'), ('It doubles reach automatically', 'no'), 'Focus improvements.'),
        Q('What is reach?', 'How many people saw the message', ('How many people paid', 'sales'), ('How many asked questions', 'leads'),
          ('How far the shop is from customers', 'pun'), 'The first step.'),
    ]),
    B=[mathb('Chaining percentages', 'When results pass through steps, multiply the rates. If 5 percent of 2,000 people become '
             'leads, that is 0.05 x 2,000 = 100 leads. If 20 percent of leads buy, that is 0.20 x 100 = 20 sales. You can also '
             'multiply the rates first: 0.05 x 0.20 = 0.01, so 1 percent of the people reached buy: 0.01 x 2,000 = 20. Both '
             'ways give the same answer.', [
        Q('10 percent of 500 reached become leads. How many leads?', '50', ('10', 'percent'), ('5', 'moved decimal'),
          ('510', 'added'), '0.10 x 500 = 50.', calc=lambda: round(0.10 * 500) == 50),
        Q('20 percent of 50 leads buy. How many sales?', '10', ('20', 'percent'), ('2.5', 'divided'), ('70', 'added'),
          '0.20 x 50 = 10.', calc=lambda: round(0.20 * 50) == 10),
        Q('What is 0.10 x 0.20?', '0.02', ('0.30', 'added'), ('2', 'moved decimal'), ('0.2', 'one factor'),
          '0.10 x 0.20 = 0.02.', calc=lambda: round(0.10 * 0.20, 4) == 0.02),
        Q('2 percent of 500 reached buy. How many sales?', '10', ('2', 'percent'), ('100', 'moved decimal'), ('250', 'divided'),
          '0.02 x 500 = 10.', calc=lambda: round(0.02 * 500) == 10),
        Q('Do the step-by-step and combined-rate methods agree?', 'Yes, both give the same sales', ('No, never', 'they agree'),
          ('Only for large numbers', 'always'), ('Only for small numbers of people', 'always'), 'Multiplication works either way.'),
    ], why='A learner who misses MAIN may not chain percentages; this practices multiplying rates through steps.')],
    F1=sec('Apply it: diagnose a funnel', FUNNEL, [
        Q('Campaign A: 5,000 reached, 50 leads, 25 sales. Campaign B: 1,000 reached, 100 leads, 10 sales. Which has the better lead '
          'rate?', 'B, at 10 percent', ('A, at 1 percent', 'A is lower'), ('A, at 50 percent', 'sales rate'), ('They are equal', 'differ'),
          'A: 50/5,000 = 1 percent; B: 100/1,000 = 10 percent.', calc=lambda: 50 / 5000 == 0.01 and 100 / 1000 == 0.1),
        Q('Same campaigns. Which has the better sales rate from leads?', 'A, at 50 percent', ('B, at 10 percent', 'B is lower'),
          ('B, at 100 percent', 'miscalculated'), ('They are equal', 'differ'), 'A: 25/50; B: 10/100.',
          calc=lambda: 25 / 50 == 0.5 and 10 / 100 == 0.1),
        Q('Campaign B gets many leads but few buy. Which step should it improve?', 'The follow-up or offer after someone shows interest',
          ('Reach, by showing the same ads to many more people', 'leads are not the problem'), ('Nothing; it is perfect', 'low sales rate'),
          ('The logo colors', 'unrelated'), 'The drop is between leads and sales.'),
        Q('A shop reaches 3,000 people, gets 4 percent as leads and 25 percent of leads buy. How many sales?', '30',
          ('120', 'leads'), ('750', 'used reach'), ('12', 'miscalculated'), '0.04 x 3,000 = 120; 0.25 x 120 = 30.',
          calc=lambda: round(0.25 * round(0.04 * 3000)) == 30),
        Q('An owner wants 40 sales. Her lead rate is 5 percent and sales rate is 20 percent of leads. What reach does she need?',
          '4,000', ('800', 'leads needed'), ('200', 'miscalculated'), ('40,000', 'extra zero'), '40 / (0.05 x 0.20) = 40 / 0.01 = 4,000.',
          calc=lambda: round(40 / (0.05 * 0.20)) == 4000),
    ]),
    F2=sec('Handle the complications: vanity numbers and slow follow-up', FUNNEL, [
        Q('Reach doubled but sales stayed flat. What might be happening?', 'The new viewers are not good leads', ('Sales must have doubled too, unseen', 'they did not'),
          ('Reach always equals sales', 'not true'), ('The math is impossible', 'possible'), 'More reach is not always better reach.'),
        Q('Leads wait 5 days for a reply and many buy elsewhere. Which step needs work?', 'Follow-up speed', ('Reach', 'not the drop'),
          ('The logo design', 'unrelated'), ('Nothing', 'there is a drop'), 'Slow follow-up loses leads.'),
        Q('A post reached 10,000 people but only 0.1 percent became leads. How many leads?', '10', ('100', 'used 1 percent'),
          ('1,000', 'used 10 percent'), ('1', 'used 0.01 percent'), '0.001 x 10,000 = 10.', calc=lambda: round(0.001 * 10000) == 10),
        Q('An owner reports only reach to investors. What is missing?', 'Leads and sales that show real results', ('Nothing, because reach alone is enough', 'incomplete'),
          ('A larger font', 'irrelevant'), ('A longer report', 'not the point'), 'Show the whole path.'),
        Q('Which statement is accurate?', 'Watching each step shows where people drop off.',
          ('Reach is the only number that really matters.', 'not true'), ('Sales rates never change.', 'they change'),
          ('Leads and sales are the same thing.', 'different'), 'Steps reveal problems.'),
    ]))

# ------------------------------------------------------------------ Set 93: fake followers, ownership, algorithms
OWNAUD = ('Big numbers can mislead. FAKE FOLLOWERS (bought or bot accounts) inflate counts but never buy, and can hurt how '
          'a platform shows your posts. AUDIENCE OWNERSHIP: on social platforms, the platform controls who sees your posts '
          'and can change its rules or ALGORITHM (the system that decides what people see) at any time, or suspend '
          'accounts. An email list or customer list that people joined with permission is closer to an audience you '
          'control. Build some of both, and never rely on a single platform.')

s93 = SET('ENT.MKT.09',
    M=sec('Avoid fake followers and reduce dependence on one platform', OWNAUD, [
        Q('Why are fake followers harmful?', 'They inflate counts but never buy', ('They buy more than real followers', 'not true'),
          ('They are required for success', 'not true'), ('They lower ad costs automatically', 'not true'), 'Empty numbers.'),
        Q('What is an algorithm on a social platform?', 'The system that decides what people see', ('A type of business license', 'no'),
          ('A list of the owner\'s account passwords', 'no'), ('A tax on posts', 'no'), 'It ranks and filters content.'),
        Q('Which audience is closer to one the business controls?', 'An email list people joined with permission',
          ('Followers on a single social app, however many', 'platform controls'), ('Bought followers from a website', 'fake'),
          ('Viewers of one viral video', 'temporary'), 'Permission lists are portable.'),
        Q('What can a platform do at any time?', 'Change its rules or suspend accounts', ('Guarantee your reach for as long as you post', 'no'),
          ('Hand you its customer data', 'no'), ('Pay all your bills', 'no'), 'Platform control is a risk.'),
        Q('What is the safest approach?', 'Build some of both and do not rely on one platform', ('Put everything on one app', 'risky'),
          ('Buy followers on one app to look popular fast', 'harmful'), ('Avoid all platforms', 'loses reach'), 'Diversify.'),
    ]),
    B=[cs('Renting a stall versus owning a address book', 'Selling on a social platform is like renting a stall in someone '
          'else\'s market. The market owner decides where your stall goes, how many people walk past, and whether you can '
          'stay. Your email list is like your own address book of customers who asked to hear from you. If the market '
          'closes or moves you to a corner, you can still write to your address book.', [
        Q('A social platform is like what?', 'A rented stall in someone else\'s market', ('Your own building on your own land', 'not yours'),
          ('A bank vault', 'no'), ('A tax office', 'no'), 'Someone else controls it.'),
        Q('Who decides how many people walk past the stall?', 'The market owner', ('You alone', 'no'), ('Customers only', 'not fully'),
          ('Nobody', 'someone does'), 'The platform controls visibility.'),
        Q('An email list is like what?', 'Your own address book of customers', ('A rented stall in the town market', 'no'), ('A billboard', 'no'),
          ('A coupon', 'no'), 'A list you hold.'),
        Q('If the market closes, what can you still do?', 'Write to your address book', ('Nothing at all', 'you can'),
          ('Force the market to open again', 'no'), ('Use the same stall', 'closed'), 'Owned contact survives.'),
        Q('What is the lesson of the picture?', 'Do not depend only on a rented stall', ('Never sell at markets', 'too extreme'),
          ('Address books are useless for selling', 'no'), ('Markets never close', 'they can'), 'Diversify.'),
    ], why='A learner who misses MAIN may not see platform risk; a rented market stall makes it concrete.')],
    F1=sec('Apply it: judge audience quality and risk', OWNAUD, [
        Q('Account A has 20,000 followers and 3 sales a month. Account B has 900 followers and 40 sales. Which audience is more '
          'valuable for sales?', 'B', ('A, because the count is bigger', 'count is not sales'), ('They are equal', 'differ'),
          ('Neither', 'B sells'), 'Sales show real value.', calc=lambda: 40 > 3),
        Q('A service offers 10,000 followers for 30 dollars. What is the best response?', 'Decline; fake followers do not buy and can hurt reach',
          ('Buy them, since looking popular attracts real buyers', 'harmful'), ('Buy 5,000 as a test', 'still harmful'), ('Ask for 20,000 instead', 'worse'),
          'Avoid fake audiences.'),
        Q('An owner gets 90 percent of sales from one platform. What risk does she face?', 'A rule change or suspension could cut most sales',
          ('No risk, because platforms never change their rules', 'they do'), ('Sales will double', 'no'), ('Taxes vanish', 'no'), 'Concentration risk.'),
        Q('Which step reduces that risk?', 'Inviting buyers to join an email list', ('Posting more on the same platform only', 'same risk'),
          ('Buying followers', 'harmful'), ('Deleting the account', 'loses sales'), 'Build an owned channel.'),
        Q('A post reaches 8,000 of 40,000 followers. What percent of followers saw it?', '20 percent', ('80 percent', 'reversed'),
          ('5 percent', 'misdivided'), ('8 percent', 'count'), '8,000 / 40,000 = 0.20.', calc=lambda: 8000 / 40000 == 0.2),
    ]),
    F2=sec('Handle the complications: algorithm shifts and suspensions', OWNAUD, [
        Q('Reach dropped by half after a platform changed its algorithm. What is a sensible response?', 'Test new formats and strengthen other channels',
          ('Buy fake followers to recover the lost reach quickly', 'harmful'), ('Assume the business is over', 'premature'), ('Do nothing forever', 'passive'),
          'Adapt and diversify.'),
        Q('An account is suspended by mistake. What would help the business keep selling meanwhile?', 'An email list and a website it controls',
          ('Only the suspended account, once it returns', 'unavailable'), ('Fake accounts', 'violates rules'), ('Nothing could help', 'owned channels help'),
          'Owned channels are a backup.'),
        Q('An influencer with 100,000 followers offers a paid post, but her comments look like bots. What should the owner check?',
          'Whether her audience is real and matches the target customers', ('Only her follower count', 'can be faked'),
          ('Only her profile photo', 'irrelevant'), ('Nothing, because big follower counts are always real people', 'not true'), 'Check audience quality.'),
        Q('An email list of 1,200 gives about 30 sales per campaign. A platform of 12,000 followers gives about 15. What does this '
          'suggest?', 'The smaller owned list produces more sales here', ('The platform is always better because it has more followers', 'not here'),
          ('Lists never work', 'it worked'), ('Followers equal sales', 'not true'), 'Engaged audiences matter.',
          calc=lambda: 30 > 15),
        Q('Which statement is accurate?', 'Engaged audiences beat big counts, and no platform is guaranteed.',
          ('Fake followers help sales.', 'they do not'), ('Platforms promise permanent reach to every account that posts often.', 'they do not'),
          ('Email lists are illegal to build.', 'legal with permission'), 'Quality and independence.'),
    ]))

# ------------------------------------------------------------------ Set 94: scheduling content and platform rules
SCHED = ('Consistency beats bursts. A CONTENT CALENDAR plans what to post and when, for example two useful posts a week on '
         'set days. Batch work: write several posts in one session, then schedule them. Each platform has its own RULES '
         '(community guidelines and terms): limits on contests, restricted products, copyrighted music and images, and '
         'what ads may claim. Read the rules for each platform you use; breaking them can get posts removed or accounts '
         'suspended. Use only images and music you have the right to use.')

s94 = SET('ENT.MKT.10',
    M=sec('Plan a realistic content calendar and follow platform rules', SCHED, [
        Q('What is a content calendar?', 'A plan of what to post and when', ('A wall calendar of the owner\'s holidays', 'not this'),
          ('A list of customer birthdays only', 'not this'), ('A tax deadline schedule', 'not this'), 'Planned posting.'),
        Q('Why batch content?', 'Writing several posts in one session saves time', ('Batching posts is required by platform law', 'not true'),
          ('Batches always go viral', 'not true'), ('It avoids having any plan', 'opposite'), 'Efficiency.'),
        Q('What can happen if platform rules are broken?', 'Posts removed or accounts suspended', ('Automatic promotion to more viewers', 'no'),
          ('A free advertising credit', 'no'), ('Nothing, ever', 'there are consequences'), 'Rules are enforced.'),
        Q('Which images may a business use?', 'Images it has the right to use', ('Any image found online', 'may be copyrighted'),
          ('A famous brand\'s photos without permission', 'no rights'), ('Screenshots of other people\'s art', 'no rights'),
          'Respect copyright.'),
        Q('Which plan is more sustainable for a busy owner?', 'Two useful posts a week on set days', ('Twenty posts on Monday, then nothing for a month', 'bursty'),
          ('Posting only when inspired', 'inconsistent'), ('Hourly posting with no plan', 'unsustainable'), 'Consistent and realistic.'),
    ]),
    B=[cs('Meal prep for posting', 'Some people cook meals for the week on Sunday, then just heat them up. Batching content '
          'works the same way: write several posts in one sitting, then schedule them for the week. A content calendar is the '
          'meal plan. And just as a kitchen has safety rules, each platform has rules about what you can post.', [
        Q('Batching content is like what?', 'Cooking meals for the week on Sunday', ('Eating out at a restaurant every meal', 'no'),
          ('Skipping meals', 'no'), ('Buying a new oven', 'no'), 'Prepare ahead.'),
        Q('A content calendar is like what?', 'A meal plan', ('A grocery receipt', 'no'), ('A recipe book', 'close but not plan'),
          ('A dishwasher', 'no'), 'It plans what and when.'),
        Q('Kitchen safety rules are like what?', 'Platform rules', ('Recipe tips', 'no'), ('Grocery prices', 'no'), ('Table manners', 'no'),
          'Rules to follow.'),
        Q('Why prep on Sunday?', 'To save time during a busy week', ('To waste food', 'no'), ('To avoid ever cooking again', 'no'),
          ('To use more pans', 'no'), 'Efficiency.'),
        Q('Heating up a prepared meal is like what?', 'A scheduled post going live', ('Writing a new post from scratch', 'no'),
          ('Deleting a post', 'no'), ('Breaking a rule', 'no'), 'Work done in advance.'),
    ], why='A learner who misses MAIN may not see how batching helps; meal prep is a familiar routine.')],
    F1=sec('Apply it: plan a month of content', SCHED, [
        Q('An owner plans 2 posts a week for 4 weeks and writes them in batches of 4. How many batch sessions does she need?', '2',
          ('8', 'posts'), ('4', 'weeks'), ('1', 'too few'), '8 posts / 4 per batch = 2.', calc=lambda: (2 * 4) / 4 == 2),
        Q('Each post takes 25 minutes to write. How long for a month of 8 posts?', '200 minutes', ('25 minutes', 'one post'),
          ('33 minutes', 'added'), ('100 minutes', 'four posts'), '8 x 25 = 200.', calc=lambda: 8 * 25 == 200),
        Q('An owner wants to run a giveaway on a platform. What should she check first?', 'That platform\'s contest rules',
          ('Only what a competitor did', 'may break rules'), ('Only the prize color', 'irrelevant'), ('Nothing; giveaways are always allowed', 'rules vary'),
          'Platforms set contest rules.'),
        Q('A video uses a popular song without a license. What is the risk?', 'The video may be removed or muted', ('More views guaranteed by the song', 'not guaranteed'),
          ('A free music license', 'no'), ('No risk at all', 'there is risk'), 'Use licensed music.'),
        Q('Which calendar entry is most useful?', '"Tue: tip on caring for wool sweaters; Fri: customer photo with permission"',
          ('"Post some stuff sometime this week, maybe about sweaters or other things"', 'vague'), ('"Be creative"', 'vague'), ('"Maybe Tuesday"', 'vague'), 'Specific topic and day.'),
    ]),
    F2=sec('Handle the complications: restricted claims and missed weeks', SCHED, [
        Q('A supplement seller wants to post "cures colds." What should she consider?', 'Health claims are restricted and must be truthful and supported',
          ('Any claim is fine on social media', 'not true'), ('Bigger health claims bring more sales safely and quickly', 'risky'),
          ('Platforms never review claims', 'they can'), 'Claims have rules.'),
        Q('The owner missed two weeks of posts while sick. What is a sensible approach?', 'Resume the calendar and keep a few backup posts ready',
          ('Post 20 times in one day to catch up on missed weeks', 'bursty'), ('Quit posting forever', 'overreaction'),
          ('Apologize in ten posts', 'unnecessary'), 'Backups and steady resumption.'),
        Q('A post was removed for using another company\'s logo. What should the owner do next time?', 'Use only her own images or licensed ones',
          ('Use the logo again but smaller', 'still infringing'), ('Use a different company\'s logo instead', 'still infringing'),
          ('Ignore the removal', 'repeats problem'), 'Respect trademarks and copyright.'),
        Q('Platform A allows contests; Platform B restricts them. The owner posts the same contest on both. What is the problem?',
          'It may break Platform B\'s rules', ('No problem; rules are identical', 'they differ'), ('It doubles prizes', 'no'),
          ('Contests are illegal everywhere', 'not true'), 'Rules differ by platform.'),
        Q('Which statement is accurate?', 'Each platform has its own rules, so read them for each one you use.',
          ('All platforms share one rulebook.', 'not true'), ('Copyright does not apply online.', 'it does'),
          ('Posting more often always fixes any problems with rules.', 'not true'), 'Know the rules.'),
    ]))

# ------------------------------------------------------------------ Set 95: Blue Ribbon Sports case
BRS = ('Documented history (Britannica): Phil Knight and his former coach Bill Bowerman formed Blue Ribbon Sports in 1964 '
       'to distribute Onitsuka Tiger running shoes from Japan. Knight sold shoes from his car at regional track meets while '
       'working other jobs. The company became Nike after splitting from Onitsuka in 1971. Lesson drawn by this course (an '
       'interpretation): go in person to the places where your most interested customers already gather, and start part '
       'time if you need income. One success story does not guarantee the same result for another business.')

s95 = SET('ENT.CASE.07',
    M=sec('Apply a documented early decision: sell in person where customers gather', BRS, [
        Q('According to the passage, what did Blue Ribbon Sports first do?', 'Distribute Onitsuka Tiger running shoes from Japan',
          ('Manufacture its own shoes in a large factory', 'not at first'), ('Sell clothing in department stores', 'not stated'),
          ('Run a chain of gyms', 'not stated'), 'It distributed imported shoes.'),
        Q('Where did Knight sell shoes?', 'From his car at regional track meets', ('Only in a big-city storefront', 'not stated'),
          ('Only through a website', 'not in 1964'), ('Only by mail to other countries', 'not stated'), 'At track meets.'),
        Q('What else was Knight doing at the time?', 'Working other jobs', ('Running for political office', 'not stated'),
          ('Studying full time abroad', 'not stated'), ('Managing a large company', 'not stated'), 'He worked other jobs.'),
        Q('Which lesson does this course draw?', 'Go in person where interested customers gather',
          ('Wait for customers to find you online', 'opposite'), ('Quit every other job on day one', 'not the lesson'),
          ('Only sell to people who are not runners', 'opposite'), 'Meet customers where they are.'),
        Q('Which statement about the Blue Ribbon Sports case is accurate?', 'It shows one start, not a promise for other in-person sellers.',
          ('It proves selling from a car at events always succeeds.', 'one case'), ('It shows imported goods never work.', 'opposite'),
          ('It shows part-time starts are impossible.', 'opposite'), 'One story teaches; it does not promise.'),
    ]),
    B=[cs('Why a track meet was a good place', 'A track meet gathers many runners in one place on one day. Runners care about '
          'shoes and can compare and talk about them. Going there is like a farmer selling apples at a farmers market rather '
          'than on an empty road. The documented fact is where Knight sold; the reason it fit is this course\'s explanation.', [
        Q('Who gathers at a track meet?', 'Many runners', ('Mostly chefs', 'no'), ('Mostly bankers', 'no'), ('Nobody', 'no'),
          'Interested customers in one place.'),
        Q('Why do runners care about the product?', 'They need good running shoes', ('They mostly collect hats', 'no'),
          ('They avoid shoes', 'no'), ('They sell shoes', 'no'), 'Strong need.'),
        Q('Selling apples at a farmers market rather than an empty road shows what?', 'Go where buyers already are', ('Apples are better', 'no'),
          ('Roads are illegal for selling', 'no'), ('Markets are free', 'not the point'), 'Location matters.'),
        Q('"Knight sold at track meets" is which kind of statement?', 'Documented fact', ('Course explanation', 'it is documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'It is recorded.'),
        Q('"Track meets fit because runners gather there" is which kind of statement?', 'The course\'s explanation', ('A documented quote from Knight', 'no'),
          ('A legal rule', 'no'), ('A tax fact', 'no'), 'An interpretation.'),
    ], why='A learner who misses MAIN may not see why the location fit; a farmers market comparison explains it.')],
    F1=sec('Apply it: find your "track meet"', BRS, [
        Q('Ana makes grips for rock climbers and has a full-time job. Which first step best applies the lesson?', 'Sell at climbing gym events on weekends',
          ('Quit her job and open a mall store', 'not part time'), ('Run ads to everyone in the country', 'unfocused'),
          ('Wait for climbers to email her', 'passive'), 'Go where climbers gather, part time.'),
        Q('At one event Ana sells 18 grips at 15 dollars each. What is her revenue?', '270 dollars', ('33 dollars', 'added'),
          ('180 dollars', 'used 10'), ('150 dollars', 'used 10 grips'), '18 x 15 = 270.', calc=lambda: 18 * 15 == 270),
        Q('The event booth costs 40 dollars and each grip costs 6 dollars to make. What is her profit from the event?', '122 dollars',
          ('270 dollars', 'revenue'), ('162 dollars', 'ignored booth'), ('230 dollars', 'ignored product cost'),
          '270 - 18 x 6 - 40 = 122.', calc=lambda: 270 - 18 * 6 - 40 == 122),
        Q('Which detail from the case is a surface detail, not the lesson?', 'Selling from a car', ('Going where customers gather', 'lesson'),
          ('Starting part time', 'lesson'), ('Meeting interested buyers in person', 'lesson'), 'The car is incidental.'),
        Q('A baker\'s customers are mostly busy commuters. Applying the lesson, where might she sell?', 'Near a busy train station in the morning',
          ('At a quiet park at midnight', 'no customers'), ('At a track meet', 'wrong audience'), ('Only online, with no promotion at all', 'passive'),
          'Find where your customers gather.'),
    ]),
    F2=sec('Handle the complications: limits of the lesson', BRS, [
        Q('Someone says, "Knight sold from his car, so I should sell everything from my car." What is wrong?', 'The car was a detail; the lesson is meeting customers where they gather',
          ('Nothing, because selling from a car is what guarantees success', 'not true'), ('Cars are illegal for business', 'not the point'),
          ('Knight never had a car', 'he did'), 'Do not copy surface details.'),
        Q('Ana\'s climbing events happen only once a month. What should she consider adding?', 'Another channel to reach climbers between events',
          ('Nothing, because one event a month is plenty of reach', 'may limit sales'), ('Fake reviews', 'dishonest'), ('Quitting immediately', 'premature'),
          'Combine channels.'),
        Q('Selling at events needs permits in some places. What should Ana check?', 'The event\'s and city\'s vendor rules',
          ('Nothing; events never need permits', 'may need'), ('Only her logo', 'irrelevant'), ('Only competitors\' prices', 'not rules'),
          'Rules apply.'),
        Q('Ana works 10 hours at an event to earn 122 dollars of profit. What is her hourly profit?', '12.20 dollars', ('122.00 dollars', 'total'),
          ('10.00 dollars', 'hours'), ('1.22 dollars', 'moved decimal'), '122 / 10 = 12.20.', calc=lambda: round(122 / 10, 2) == 12.2),
        Q('Which statement is accurate?', 'The case suggests a way to start; results depend on the product and market.',
          ('Every in-person seller at events eventually becomes a global brand.', 'not true'), ('Part-time starts always fail.', 'not true'),
          ('Events are the only channel that works.', 'not true'), 'Test your own market.'),
    ]))

# ------------------------------------------------------------------ Set 96: Madam C. J. Walker case
WALKER = ('Documented history (Indiana Historical Society): Madam C. J. Walker sold her hair-care products door to door, '
          'advertised in African American newspapers, trained and recruited sales agents, ran a mail-order business and a '
          'beauty school, and incorporated her company in Indianapolis in 1910. Lesson drawn by this course (an '
          'interpretation): build several channels that reach your customers directly, and train other people to sell and '
          'teach, so the business is not limited to one person\'s time. One success story does not guarantee the same '
          'result for another business.')

s96 = SET('ENT.CASE.08',
    M=sec('Apply a documented early decision: build distribution through trained agents', WALKER, [
        Q('According to the passage, how did Walker first sell products?', 'Door to door', ('Only in large department stores', 'not stated'),
          ('Only through television ads', 'not available'), ('Only to other companies', 'not stated'), 'She sold door to door.'),
        Q('Where did she advertise?', 'In African American newspapers', ('On billboards across Europe', 'not stated'),
          ('On radio in every state', 'not stated'), ('Nowhere at all', 'she advertised'), 'Newspapers reaching her customers.'),
        Q('What did she do with sales agents?', 'Trained and recruited them', ('Replaced them all with machines', 'not stated'),
          ('Refused to work with any', 'opposite'), ('Paid them to stay home', 'not stated'), 'Training agents expanded reach.'),
        Q('Which lesson does this course draw?', 'Build several direct channels and train others to sell',
          ('Rely on one person doing every sale forever', 'opposite'), ('Avoid advertising entirely', 'she advertised'),
          ('Sell only to strangers who never use the product', 'opposite'), 'Multiply reach through people.'),
        Q('Which statement about the Madam C. J. Walker case is accurate?', 'It shows one approach, not a guarantee for other sellers.',
          ('It proves door-to-door sales always succeed for products.', 'one case'), ('It shows training agents never helps.', 'opposite'),
          ('It shows advertising is useless.', 'opposite'), 'One story teaches; it does not promise.'),
    ]),
    B=[cs('One teacher versus a school', 'One teacher can teach only so many students in a day. A school with many trained '
          'teachers can teach thousands. Walker\'s recruiting and training of agents and her beauty school are documented. '
          'This course\'s explanation is that training others let the business reach more customers than one person could '
          'reach alone. Facts are recorded; explanations are interpretations.', [
        Q('Why can a school teach more students than one teacher?', 'It has many trained teachers', ('It has bigger desks and rooms', 'no'),
          ('It has longer days', 'no'), ('It charges less', 'no'), 'More trained people.'),
        Q('Trained sales agents are like what?', 'Many teachers in a school', ('One tired teacher', 'no'), ('An empty classroom at night', 'no'),
          ('A locked door', 'no'), 'They multiply reach.'),
        Q('"Walker recruited and trained agents" is which kind of statement?', 'Documented fact', ('Course explanation', 'documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'It is recorded.'),
        Q('"Training let the business reach more customers" is which kind?', 'The course\'s explanation', ('A documented quote from Walker', 'no'),
          ('A tax rule', 'no'), ('A contract', 'no'), 'An interpretation.'),
        Q('What limits a business that depends on one person?', 'That person\'s time', ('The color of the logo', 'no'),
          ('The weather', 'no'), ('The number of chairs', 'no'), 'Time is limited.'),
    ], why='A learner who misses MAIN may not see why training others matters; a school versus one teacher explains it.')],
    F1=sec('Apply it: extend reach beyond one person', WALKER, [
        Q('Lena sells handmade soap at markets alone and is booked every weekend. Which step best applies the lesson?',
          'Train a helper to run a second market stall', ('Work every night alone with no help at all', 'unsustainable'),
          ('Stop advertising', 'opposite'), ('Sell only to her family', 'opposite'), 'Train others to sell.'),
        Q('Lena pays a trained helper 20 percent commission on 500 dollars of weekend sales. What is the commission?', '100 dollars',
          ('20 dollars', 'percent as dollars'), ('400 dollars', 'remainder'), ('50 dollars', 'ten percent'), '0.20 x 500 = 100.',
          calc=lambda: 0.2 * 500 == 100),
        Q('After commission, how much of the 500 dollars remains for Lena\'s costs and profit?', '400 dollars', ('500 dollars', 'ignored commission'),
          ('100 dollars', 'commission'), ('480 dollars', 'subtracted 20'), '500 - 100 = 400.', calc=lambda: 500 - 100 == 400),
        Q('Which channel mix reflects the case?', 'Markets, a community newsletter ad and mail orders', ('One market stall only', 'single channel'),
          ('Billboards in a different country', 'wrong audience'), ('No channels at all; just wait for word of mouth', 'passive'),
          'Several direct channels.'),
        Q('Before a helper sells for her, what should Lena provide?', 'Training on the products and how to talk about them honestly',
          ('Nothing, because anyone can sell any product without help', 'no training'), ('A script with exaggerated claims', 'dishonest'),
          ('Her bank password', 'unsafe'), 'Training keeps quality and honesty.'),
    ]),
    F2=sec('Handle the complications: quality and fair arrangements', WALKER, [
        Q('A new agent makes promises about the soap that are not true. What should Lena do?', 'Correct the claims and retrain the agent',
          ('Ignore it, since sales are sales either way', 'harms trust'), ('Encourage bigger claims', 'dishonest'), ('Hide it from customers', 'dishonest'),
          'Agents represent the business.'),
        Q('An agent arrangement requires agents to pay a large fee before selling anything. What should Lena consider?',
          'Whether the arrangement is fair and focused on real sales to customers', ('Nothing, because bigger upfront fees are always better for everyone', 'not fair'),
          ('Requiring even larger fees', 'worse'), ('Hiding the fee', 'dishonest'), 'Fair, sales-based arrangements.'),
        Q('Someone says, "Walker sold door to door, so door-to-door is the secret." What is wrong?', 'The lesson is many direct channels, not one method',
          ('Nothing; door-to-door always works', 'not true'), ('Door-to-door selling is illegal everywhere today', 'not true'),
          ('Walker never sold door to door', 'she did'), 'Look at the whole pattern.'),
        Q('Is a helper an employee or contractor? What should Lena check?', 'Current federal and state rules on worker classification',
          ('Only what the helper prefers', 'not the test'), ('Nothing, because the label in the agreement decides everything', 'relationship decides'),
          ('Only her competitor\'s choice', 'irrelevant'), 'Classification depends on the real relationship.'),
        Q('Which statement is accurate?', 'The case shows one path; other businesses must test what works for them.',
          ('Training sales agents guarantees that a business will succeed.', 'not guaranteed'), ('One channel is always enough.', 'not always'),
          ('Advertising never matters.', 'not true'), 'Learn the principle.'),
    ]))

SETS = [s91, s92, s93, s94, s95, s96]
