"""Entrepreneurship sets 104-112: Foundation 13, operations, security and continuity. Names are fictional."""
import math

from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 104: simple procedures and scheduling
PROC = ('A PROCEDURE (or checklist) writes down the steps for a task that repeats, such as opening the shop, packing an '
        'order, or closing out the day. Written steps reduce mistakes, make work faster, and let a helper do the task the '
        'same way. Keep each checklist short, in order, and updated when something changes. A simple SCHEDULE blocks time '
        'for paid work, for admin (invoices, email, bookkeeping) and for rest, so important tasks are not always pushed '
        'to "later."')

s104 = SET('ENT.OPS.01',
    M=sec('Write short procedures and block time for admin', PROC, [
        Q('What is a procedure in a small business?', 'Written steps for a task that repeats',
          ('A one-time speech the owner gives on opening day', 'not repeating steps'),
          ('A medical operation for the business owner', 'pun'), ('A legal filing that registers the business', 'not this'),
          'A repeatable checklist.'),
        Q('Which task most needs a written checklist?', 'Packing an order the same way every time',
          ('Choosing a new logo once every ten years', 'rare'), ('Picking a favorite song for the shop', 'trivial'),
          ('Deciding what to eat for lunch today', 'trivial'), 'Repeated tasks benefit most.'),
        Q('Why block time for admin?', 'So admin is not always pushed to "later"',
          ('Because admin tasks are illegal during work hours', 'not true'),
          ('Because admin never needs any time at all', 'it does'),
          ('So customers can do the admin instead', 'not their job'), 'Scheduled admin gets done.'),
        Q('When should a checklist be updated?', 'When something in the task changes', ('Never, once it is written', 'outdated'),
          ('Only when a customer complains loudly', 'too late'), ('Every hour, whether or not anything changed', 'wasteful'),
          'Keep it current.'),
        Q('How does a checklist help a new helper?', 'They can do the task the same way', ('They no longer need any training at all', 'still need some'),
          ('They can skip steps they dislike', 'opposite'), ('They can change the prices freely', 'unrelated'), 'Consistency.'),
    ]),
    B=[cs('A recipe card', 'A recipe card lists ingredients and steps in order, so anyone in the family can make the dish the '
          'same way. If a step changes, like a new oven temperature, you update the card. A business checklist is a recipe '
          'card for a work task: short, in order, and kept up to date. A weekly schedule is like a meal plan: it decides '
          'when each thing gets done.', [
        Q('A business checklist is like what?', 'A recipe card', ('A grocery receipt', 'a record'), ('A menu price list', 'prices'),
          ('A shopping bag', 'no'), 'Steps in order.'),
        Q('Why can anyone make the dish from the card?', 'The steps are written in order', ('The dish is always simple', 'not the reason'),
          ('Everyone already knows it', 'no'), ('The card is colorful', 'no'), 'Written order.'),
        Q('A new oven temperature means what for the card?', 'Update it', ('Throw it away', 'no'), ('Ignore the change', 'no'),
          ('Hide it', 'no'), 'Keep procedures current.'),
        Q('A weekly schedule is like what?', 'A meal plan', ('A recipe card', 'that is the checklist'), ('A fridge', 'no'),
          ('A dish soap', 'no'), 'It decides when.'),
        Q('What should a good card be?', 'Short and in order', ('Long and random', 'no'), ('Secret', 'no'), ('Blank', 'no'),
          'Clear steps.'),
    ], why='A learner who misses MAIN may not see what a procedure is; a recipe card makes it familiar.')],
    F1=sec('Apply it: write a checklist and a weekly schedule', PROC, [
        Q('An Etsy seller forgets to include care cards in about 1 in 10 orders. What helps most?', 'A packing checklist that includes the care card',
          ('Packing faster so she has no time to forget', 'more errors'), ('Removing care cards entirely', 'loses value'),
          ('Asking customers to remind her', 'not their job'), 'Checklists prevent omissions.'),
        Q('She ships 60 orders a month and misses the card in 1 of 10. How many orders a month miss it?', '6',
          ('10', 'the rate base'), ('1', 'per ten'), ('16', 'miscalculated'), '60 / 10 = 6.', calc=lambda: 60 / 10 == 6),
        Q('Which checklist step order makes sense for packing?', 'Check item, add care card, seal, label, record shipment',
          ('Seal, then check the item inside', 'too late to check'), ('Label first, then decide which item goes in the box', 'backward'),
          ('Record shipment before packing', 'premature'), 'Logical order.'),
        Q('An owner works 40 hours a week and wants 15 percent of it for admin. How many hours is that?', '6 hours',
          ('15 hours', 'percent as hours'), ('4 hours', 'ten percent'), ('34 hours', 'remainder'), '0.15 x 40 = 6.',
          calc=lambda: round(0.15 * 40, 2) == 6),
        Q('Invoices are always sent late because there is "no time." What change fits the passage?', 'Block a fixed weekly time for invoicing',
          ('Wait until there is free time', 'never comes'), ('Stop invoicing small jobs', 'loses money'),
          ('Ask clients to invoice themselves', 'not their job'), 'Schedule admin.'),
    ]),
    F2=sec('Handle the complications: outdated steps and overbooked weeks', PROC, [
        Q('A helper follows an old checklist that uses a shipping service the shop no longer uses. What went wrong?', 'The checklist was not updated after a change',
          ('The helper ignored good, current instructions', 'followed them'), ('Checklists never work', 'they do'),
          ('Shipping services never change', 'they did'), 'Update procedures.'),
        Q('A checklist has 40 detailed steps for a 5-minute task, and helpers skip it. What is a better approach?', 'Shorten it to the key steps',
          ('Add 20 more steps', 'worse'), ('Remove the checklist entirely', 'loses consistency'),
          ('Punish anyone who skips it', 'misses the cause'), 'Short checklists get used.'),
        Q('Paid work fills 48 of 50 scheduled hours, leaving 2 hours for admin that needs 6. How many hours short?', '4 hours',
          ('2 hours', 'available'), ('6 hours', 'needed'), ('8 hours', 'added'), '6 - 2 = 4.', calc=lambda: 6 - 2 == 4),
        Q('Each week, paid work leaves 4 fewer hours than the admin work needs. Which change is most sustainable?',
          'Reduce booked work or get help with admin',
          ('Skip all rest every week', 'burnout'), ('Ignore admin indefinitely', 'problems grow'),
          ('Work 90 hours a week permanently instead', 'unsustainable'),
          'Balance the schedule.'),
        Q('Which statement is accurate?', 'Short, current checklists reduce mistakes.',
          ('Written steps slow every business down a lot.', 'usually faster'), ('Admin can always wait.', 'it piles up'),
          ('Checklists never need changes.', 'they do'), 'Simple systems help.'),
    ]))

# ------------------------------------------------------------------ Set 105: inventory and reorder points
INV = ('INVENTORY is the stock of goods or materials you hold to sell. Too little and you run out; too much ties up cash '
       'and risks damage or items going out of style. A REORDER POINT tells you when to order more: reorder point = '
       'average daily use x lead time (days to arrive) + SAFETY STOCK (a small extra cushion). Example: you sell 4 mugs a '
       'day, delivery takes 10 days, safety stock is 10: reorder point = 4 x 10 + 10 = 50 mugs. Count stock regularly so '
       'records match the shelf.')

s105 = SET('ENT.OPS.02',
    M=sec('Calculate a reorder point and balance stock against cash', INV, [
        Q('What is safety stock?', 'A small extra cushion of inventory',
          ('Inventory locked in a safe for security reasons only', 'pun'),
          ('Stock the owner keeps for personal use at home', 'not business stock'),
          ('Items set aside to be thrown away later', 'not this'), 'A buffer against surprises.'),
        Q('Daily use 5, lead time 8 days, safety stock 12. What is the reorder point?', '52', ('40', 'no safety stock'),
          ('25', 'added wrongly'), ('100', 'multiplied all'), '5 x 8 + 12 = 52.', calc=lambda: 5 * 8 + 12 == 52),
        Q('What is a risk of too much inventory?', 'Cash is tied up and items may spoil or go out of style',
          ('Customers can never find anything at all to buy', 'that is too little'),
          ('The business pays no rent at all', 'unrelated'), ('Prices automatically double', 'unrelated'), 'Overstock costs money.'),
        Q('What is lead time?', 'Days for an order to arrive', ('Days a customer waits to pay', 'not lead time'),
          ('Hours a store is open each day', 'not lead time'), ('Time spent on marketing', 'not lead time'), 'Delivery delay.'),
        Q('Why count stock regularly?', 'So records match what is really on the shelf', ('Because counting raises prices', 'no'),
          ('Because records are always perfect anyway', 'they drift'), ('So suppliers can visit', 'unrelated'), 'Catch differences.'),
    ]),
    B=[mathb('Multiply, then add', 'Reorder point uses the order of operations: multiply first, then add. Daily use x lead time '
             'tells how many items sell while you wait for delivery. Then add safety stock. Example: 6 a day x 7 days = 42, plus '
             '8 safety = 50. A common mistake is adding first: (6 + 7) x 8 = 104, which is wrong. Check by asking whether the '
             'answer is about one delivery-wait of sales plus a little extra.', [
        Q('What is 3 x 9 + 5?', '32', ('42', 'added first'), ('17', 'added all'), ('27', 'skipped adding'), '27 + 5 = 32.',
          calc=lambda: 3 * 9 + 5 == 32),
        Q('Which step comes first in "use x lead time + safety"?', 'Multiply use by lead time', ('Add lead time and safety', 'wrong order'),
          ('Divide by safety stock', 'not a step'), ('Subtract use', 'not a step'), 'Multiply first.'),
        Q('What is 6 x 7 + 8?', '50', ('104', 'added first'), ('21', 'added all'), ('42', 'skipped adding'), '42 + 8 = 50.',
          calc=lambda: 6 * 7 + 8 == 50),
        Q('What is 10 x 4 + 15?', '55', ('100', 'added first'), ('29', 'added all'), ('40', 'skipped adding'), '40 + 15 = 55.',
          calc=lambda: 10 * 4 + 15 == 55),
        Q('What does "use x lead time" represent?', 'Items sold while waiting for delivery', ('Total yearly sales of the whole shop', 'no'),
          ('The safety stock', 'no'), ('The price per item', 'no'), 'Sales during the wait.'),
    ], why='A learner who misses MAIN may compute in the wrong order; this practices multiply-then-add.')],
    F1=sec('Apply it: set reorder points for products', INV, [
        Q('A tea shop sells 3 tins a day. The supplier takes 14 days. Safety stock is 9. What is the reorder point?', '51 tins',
          ('42 tins', 'no safety stock'), ('26 tins', 'added all'), ('378 tins', 'multiplied all'), '3 x 14 + 9 = 51.',
          calc=lambda: 3 * 14 + 9 == 51),
        Q('The shop has 60 tins and sells 3 a day. In how many days will it reach the 51-tin reorder point?', '3 days',
          ('20 days', 'used all stock'), ('17 days', 'used reorder point'), ('9 days', 'used safety stock'), '(60 - 51) / 3 = 3.',
          calc=lambda: (60 - 51) / 3 == 3),
        Q('Records show 80 candles; a count finds 72. What is the difference?', '8 candles', ('152 candles', 'added'),
          ('72 candles', 'counted'), ('80 candles', 'recorded'), '80 - 72 = 8.', calc=lambda: 80 - 72 == 8),
        Q('What should the owner do about that difference?', 'Update the records and look for the cause',
          ('Keep the old number so the records look better', 'false records'), ('Ignore it since it is small', 'causes grow'),
          ('Order 8 extra without checking', 'misses cause'), 'Investigate and correct.'),
        Q('A seasonal holiday item sells only in December. What is the risk of a large order in January?', 'Cash tied up in stock that will not sell for months',
          ('It will sell out immediately in January anyway', 'unlikely'), ('There is no risk at all', 'there is'),
          ('The supplier will refuse to deliver', 'not stated'), 'Timing matters.'),
    ]),
    F2=sec('Handle the complications: delays and changing demand', INV, [
        Q('The supplier\'s lead time grows from 10 to 20 days. Daily use is 4 and safety stock 10. What is the new reorder point?', '90',
          ('50', 'old lead time'), ('34', 'added all'), ('800', 'multiplied all'), '4 x 20 + 10 = 90.', calc=lambda: 4 * 20 + 10 == 90),
        Q('Sales jump after a viral post. What should happen to the reorder point?', 'Recalculate it with the new daily use',
          ('Keep the old one forever, unchanged', 'will run out'), ('Set it to zero', 'will run out'), ('Double the price instead', 'not the question'),
          'Inputs changed.'),
        Q('An owner orders far more than needed to get a bulk discount, then cannot pay rent. What lesson applies?', 'A discount is not worth it if it drains needed cash',
          ('Bulk discounts are always worth any cash they use', 'not always'), ('Rent can always wait', 'not true'), ('Inventory equals cash', 'not spendable'),
          'Weigh cash needs.'),
        Q('Daily use 2.5, lead time 9 days, safety 6. What is the reorder point, rounded up to whole items?', '29',
          ('28', 'rounded down'), ('22.5', 'no safety, not rounded'), ('18', 'miscalculated'), '2.5 x 9 + 6 = 28.5, up to 29.',
          calc=lambda: math.ceil(2.5 * 9 + 6) == 29),
        Q('Which statement is accurate?', 'Reorder points should be updated when sales or lead times change.',
          ('Reorder points never change.', 'they do'), ('More inventory is always safer.', 'cash risk'),
          ('Counting stock by hand is unnecessary once software is used.', 'still needed'), 'Keep inputs current.'),
    ]))

# ------------------------------------------------------------------ Set 106: subscriptions, free trials, cancellation dates
SUBS = ('Small recurring charges add up. A business may pay for software, storage, design tools, a website plan, and '
        'several FREE TRIALS that turn into paid plans. Keep a SUBSCRIPTION LIST with each service, its cost, how often it '
        'bills, the renewal date, the card it uses, and who owns the login. Put trial end dates and renewal dates on a '
        'calendar a few days early, review the list every few months, and cancel what you no longer use.')

s106 = SET('ENT.OPS.03',
    M=sec('Track the business\'s own subscriptions and trial dates', SUBS, [
        Q('What should a subscription list include?', 'Service, cost, cycle, renewal date, card, login owner',
          ('Only the service names, with nothing else at all', 'incomplete'), ('Only the owner\'s favorite apps', 'incomplete'),
          ('Only services that are free forever', 'misses paid ones'), 'Full details.'),
        Q('When should a trial end date go on the calendar?', 'A few days before it ends', ('On the day after it ends', 'too late'),
          ('Never; trials always cancel themselves', 'many convert'), ('Only if the trial is very expensive', 'all matter'),
          'Early reminders.'),
        Q('Five tools cost 9, 12, 15, 20 and 29 dollars a month. What is the monthly total?', '85 dollars', ('29 dollars', 'largest'),
          ('75 dollars', 'missed one'), ('17 dollars', 'average'), '9 + 12 + 15 + 20 + 29 = 85.', calc=lambda: 9 + 12 + 15 + 20 + 29 == 85),
        Q('Five tools cost a total of 85 dollars a month. What is that total per year?',
          '1,020 dollars',
          ('85 dollars', 'monthly'), ('850 dollars', '10 months'),
          ('1,105 dollars', '13 months'),
          '85 x 12 = 1,020.',
          calc=lambda: 85 * 12 == 1020),
        Q('What should happen to unused subscriptions?', 'Cancel them', ('Keep them just in case forever', 'waste'),
          ('Move them to a personal card', 'commingling'), ('Hide them from the budget', 'dishonest'), 'Stop paying for unused tools.'),
    ]),
    B=[cs('Magazine subscriptions you forgot', 'Many people discover they still pay for a magazine they stopped reading years '
          'ago. A small monthly charge is easy to forget. Businesses collect these too: tools, storage plans and trials that '
          'quietly turned paid. A simple list with dates works like checking your mailbox for magazines you no longer '
          'read, then cancelling them. Reviewing the list every few months keeps it short.', [
        Q('Why are small monthly charges easy to forget?', 'They are small and automatic', ('They are always huge', 'no'),
          ('They only ever come by mail', 'no'), ('They are illegal', 'no'), 'Small and automatic.'),
        Q('A forgotten business tool is like what?', 'An unread magazine still being paid for', ('A new customer', 'no'),
          ('A paid invoice from a paper supplier', 'no'), ('A refund', 'no'), 'Ongoing waste.'),
        Q('A trial that "quietly turned paid" means what?', 'It started charging after the free period', ('It stayed free forever after the trial', 'no'),
          ('It deleted itself', 'no'), ('It paid you', 'no'), 'Trials convert.'),
        Q('What helps catch these charges?', 'A list with dates', ('Ignoring statements', 'no'), ('More subscriptions', 'no'),
          ('Hiding the card', 'no'), 'Track them.'),
        Q('What do you do with a magazine you no longer read?', 'Cancel it', ('Buy two copies', 'no'), ('Keep paying', 'no'),
          ('Hide it', 'no'), 'Stop unused charges.'),
    ], why='A learner who misses MAIN may underrate small charges; forgotten magazines are familiar.')],
    F1=sec('Apply it: audit subscriptions', SUBS, [
        Q('An audit finds 3 unused tools at 14, 22 and 9 dollars a month. How much is saved per year by cancelling them?', '540 dollars',
          ('45 dollars', 'monthly'), ('450 dollars', '10 months'), ('585 dollars', '13 months'), '(14 + 22 + 9) x 12 = 540.',
          calc=lambda: (14 + 22 + 9) * 12 == 540),
        Q('A 14-day trial started March 3. When does it end?', 'March 17', ('March 14', 'counted day 14 as date'),
          ('March 31', 'end of month'), ('April 3', 'a month'), '3 + 14 = 17.', calc=lambda: 3 + 14 == 17),
        Q('A 14-day trial started March 3 and ends March 17. When should the reminder for that trial be set?',
          'A few days earlier, around March 14',
          ('March 18, the day after it ends', 'too late'), ('April 1', 'too late'),
          ('No reminder needed', 'risky'),
          'Remind before conversion.'),
        Q('A tool bills yearly at 240 dollars on a date the owner forgot. What would have helped?', 'A renewal date on the subscription list and calendar',
          ('A bigger logo', 'irrelevant'), ('A second email address for the business owner', 'irrelevant'), ('More free trials', 'more risk'),
          'Track renewal dates.'),
        Q('A former helper\'s login owns a paid tool. What should the list show?', 'Who owns each login', ('Nothing about logins', 'misses risk'),
          ('Only the price', 'incomplete'), ('Only the tool\'s logo', 'irrelevant'), 'Ownership matters.'),
    ]),
    F2=sec('Handle the complications: hard-to-cancel services and shared cards', SUBS, [
        Q('A service makes cancelling difficult and keeps charging. What should the owner do?', 'Follow its cancellation steps, keep proof, then contact the card issuer',
          ('Keep paying forever, since cancelling the service is so hard', 'waste'), ('Close the business', 'overreaction'), ('Ignore the charges', 'continues'),
          'Document and escalate.'),
        Q('Business subscriptions are on a personal card. What problem does this cause?', 'Business and personal costs get mixed',
          ('No problem at all', 'commingling'), ('The charges become free for her', 'no'), ('Taxes disappear', 'no'), 'Use the business card.'),
        Q('Two team members accidentally signed up for the same tool at 15 dollars a month each. The license needs only one, and one of the charges can be cancelled. How much does the unused duplicate waste per year?',
          '180 dollars',
          ('15 dollars', 'monthly'), ('30 dollars', 'both monthly'),
          ('360 dollars', 'both yearly'),
          'One duplicate x 15 dollars x 12 months = 180 dollars.',
          calc=lambda: 15 * 12 == 180),
        Q('A business card expires and a key service fails to renew. What prevents surprise outages?', 'Updating the card on the list when it changes',
          ('Ignoring card expiry dates', 'causes outages'), ('Using many different cards randomly for each tool', 'confusing'),
          ('Never renewing anything', 'loses service'), 'Keep billing details current.'),
        Q('Which statement is accurate?', 'A dated subscription list prevents surprise renewals.',
          ('Small charges never add up.', 'they do'), ('Trials always end for free.', 'many convert'),
          ('Only big companies need subscription lists at all.', 'all benefit'), 'Track and review.'),
    ]))

# ------------------------------------------------------------------ Set 107: passwords, two-step login, backups
SEC = ('Business accounts (bank, email, website, payment processor) are valuable targets. Basics: use a long, UNIQUE '
       'password for each account, stored in a PASSWORD MANAGER (a secure app that remembers passwords). Turn on TWO-STEP '
       'LOGIN (also called two-factor authentication), which asks for a second proof, such as a code from an app, so a '
       'stolen password alone is not enough. Keep BACKUPS of important files in a separate place and test that you can '
       'restore them. Be wary of messages asking for codes or passwords.')

s107 = SET('ENT.OPS.04',
    M=sec('Protect accounts with unique passwords, two-step login and backups', SEC, [
        Q('What does two-step login add?', 'A second proof, so a stolen password alone is not enough',
          ('A second password that is the same as the first', 'not a second factor'),
          ('A longer username for the account', 'not security'), ('An automatic backup of every file', 'different'),
          'Two factors.'),
        Q('Why use a unique password for each account?', 'One leaked password cannot open the others',
          ('Unique passwords are easier to remember', 'not the reason'), ('Sites require the same password', 'no'),
          ('It makes logins faster', 'not the reason'), 'Limits damage.'),
        Q('What is a password manager?', 'A secure app that remembers passwords', ('A person who guesses passwords for you', 'no'),
          ('A sticky note on the monitor', 'insecure'), ('A list emailed to everyone', 'insecure'), 'Secure storage.'),
        Q('A message asks for the code sent to your phone "to verify your account." What should you do?', 'Not share it and check through the official site',
          ('Reply with the code quickly', 'scam'), ('Post the code online', 'scam'), ('Share it with anyone who asks politely by email', 'scam'),
          'Codes are secrets.'),
        Q('Why test restoring a backup?', 'To be sure it actually works', ('Restoring erases backups', 'no'),
          ('Tests are required daily by law', 'no'), ('Backups never fail', 'they can'), 'Untested backups may fail.'),
    ]),
    B=[cs('A door lock plus a security guard', 'A password is like a door key. If someone copies your key, they can walk in. '
          'Two-step login is like a guard who also checks your face: a copied key alone is not enough. Using the same key '
          'for your house, car and office means one lost key opens everything. A backup is a copy of your important papers '
          'kept somewhere else, in case of fire.', [
        Q('A password is like what?', 'A door key', ('A guard', 'that is two-step'), ('A fire', 'no'), ('A glass window', 'no'),
          'Something that opens access.'),
        Q('Two-step login is like what?', 'A guard who also checks your face', ('A spare key hidden under the mat', 'insecure'),
          ('An open door', 'no'), ('A doorbell', 'no'), 'A second check.'),
        Q('Using one key for everything means what?', 'One lost key opens everything', ('Better security', 'no'),
          ('Fewer locks are needed overall', 'not the point'), ('Nothing changes', 'risk'), 'Reused passwords.'),
        Q('A backup is like what?', 'Copies of papers kept somewhere else', ('Papers burned in a fire', 'no'),
          ('A single original', 'no'), ('A locked drawer at home, nowhere else', 'same place'), 'Separate copies.'),
        Q('Why keep copies somewhere else?', 'In case the first place is damaged', ('To confuse yourself', 'no'),
          ('To share the copies with strangers', 'no'), ('It is required', 'not the reason'), 'Separation protects.'),
    ], why='A learner who misses MAIN may not picture these protections; locks, guards and copies make them concrete.')],
    F1=sec('Apply it: secure the key accounts', SEC, [
        Q('An owner uses "Shop2024" for email, bank and website. What should she change first?', 'Use unique passwords and turn on two-step login',
          ('Add "!" to the end of the same password everywhere', 'still reused'), ('Write it on the shop door', 'insecure'),
          ('Change only the website password', 'incomplete'), 'Unique and two-step.'),
        Q('Which account should get two-step login first?', 'The business email, which can reset other passwords',
          ('A free recipe website', 'low value'), ('A game account', 'unrelated'), ('A newsletter she reads that has no login at all', 'none'),
          'Email unlocks other accounts.'),
        Q('Backups run every 7 days. A laptop is stolen 5 days after the last backup. Up to how many days of work could be lost?', '5 days',
          ('7 days', 'full cycle'), ('12 days', 'added'), ('2 days', 'subtracted'), 'Work since the last backup.',
          calc=lambda: 5 <= 7),
        Q('Which backup plan is strongest?', 'Automatic backups kept elsewhere and tested',
          ('One copy on the same laptop', 'lost together'), ('A backup made once years ago', 'outdated'),
          ('No backup, just being careful with the laptop', 'risky'), 'Separate, regular, tested.'),
        Q('A password manager asks for one strong main password. What should that password be?', 'Long and used nowhere else',
          ('The same as the email password', 'reused'), ('"password"', 'weak'), ('The business name', 'guessable'),
          'Protect the vault.'),
    ]),
    F2=sec('Handle the complications: breaches and shortcuts', SEC, [
        Q('A site the owner uses reports a data breach. What should she do?', 'Change that password and any others that reused it',
          ('Nothing, because breaches never matter to small shops', 'they do'), ('Delete her email account', 'overreaction'),
          ('Post her new password online', 'insecure'), 'Contain the damage.'),
        Q('A helper finds two-step login annoying and wants it off. What is the best response?', 'Keep it on and make it easier with an app',
          ('Turn it off for everyone', 'weakens security'), ('Share one code with all staff', 'insecure'),
          ('Use the owner\'s phone for everyone\'s codes', 'insecure'), 'Keep the protection.'),
        Q('Restoring last month\'s backup fails because the files are corrupted. What lesson applies?', 'Test backups regularly',
          ('Backups are useless', 'not true'), ('Never back up', 'worse'), ('Only back up yearly', 'worse'), 'Testing catches failures.'),
        Q('An email claims to be from the bank and links to a login page. What is safest?', 'Go to the bank site by typing its address yourself',
          ('Click the link in the email and log in right away', 'phishing risk'), ('Reply with the password', 'scam'), ('Forward it to customers', 'harmful'),
          'Use known routes.'),
        Q('Which statement is accurate?', 'Unique passwords, two-step login and backups reduce risk.',
          ('Small businesses are never targeted.', 'they are'), ('One strong password reused everywhere is enough.', 'reuse risk'),
          ('Backups never need testing.', 'they do'), 'Basics matter.'),
    ]))

# ------------------------------------------------------------------ Set 108: access for owners and helpers
ACCESS = ('Give each person their OWN login rather than sharing one password, and give only the ACCESS they need for '
          'their job (called least privilege): a helper who packs orders may need the order list, not the bank account. '
          'Keep a list of who has access to what. The owner should hold the main (administrator) account for key services. '
          'When someone leaves or changes roles, remove or change their access the same day.')

s108 = SET('ENT.OPS.05',
    M=sec('Give each person their own login and only the access they need', ACCESS, [
        Q('What does least privilege mean?', 'Giving only the access a person needs for their job',
          ('Giving everyone full access to everything in the business', 'opposite'), ('Giving the owner the least access', 'opposite'),
          ('Never giving anyone any access', 'unworkable'), 'Minimum needed.'),
        Q('Why give each person their own login?', 'Access can be tracked and removed individually',
          ('It makes passwords easier to share', 'opposite'), ('It is required for free accounts only, not paid', 'no'),
          ('It hides who did what', 'opposite'), 'Accountability.'),
        Q('Who should hold the main administrator account?', 'The owner', ('A temporary helper', 'risk'), ('A customer', 'no'),
          ('Whoever set up the site', 'may leave'), 'The owner controls key accounts.'),
        Q('When should a departing helper\'s access be removed?', 'The same day they leave', ('A few months later, when convenient', 'risk'),
          ('Only if they ask', 'risk'), ('Never', 'risk'), 'Immediately.'),
        Q('A packing helper needs which access?', 'The order list', ('The bank account', 'not needed'), ('The tax account', 'not needed'),
          ('The domain registrar', 'not needed'), 'Job-related access only.'),
    ]),
    B=[cs('Keys to different rooms', 'In an office building, a cleaner may have keys to the hallways and the kitchen but not '
          'the safe. The manager has the master key. Each person signs for their own keys, and when someone leaves, their '
          'keys are returned the same day. Business accounts work the same way: separate keys, only the rooms each person '
          'needs, and a master key the owner keeps.', [
        Q('The cleaner\'s keys are like what?', 'Access only to what the job needs', ('Full access', 'no'), ('No access', 'no'),
          ('A master key to every single room', 'no'), 'Least privilege.'),
        Q('The master key is like what?', 'The administrator account the owner keeps', ('A helper\'s login', 'no'),
          ('A customer\'s password for the online shop', 'no'), ('A guest pass', 'no'), 'Full control.'),
        Q('Why does each person sign for their own keys?', 'So it is clear who has which key', ('To slow everyone down on purpose', 'no'),
          ('To share keys freely', 'opposite'), ('To lose keys', 'no'), 'Tracking.'),
        Q('When are keys returned?', 'The same day someone leaves', ('Next year', 'no'), ('Never', 'no'), ('Whenever it is convenient', 'no'),
          'Promptly.'),
        Q('Does the cleaner need the safe key?', 'No', ('Yes, always', 'no'), ('Only on Fridays', 'no'), ('Only if asked', 'no'),
          'Not needed for the job.'),
    ], why='A learner who misses MAIN may share logins freely; keys to different rooms show why access is split.')],
    F1=sec('Apply it: set up access for a team', ACCESS, [
        Q('A shop has 3 helpers sharing the owner\'s login to the store platform. What is the best fix?', 'Give each helper a separate, limited login',
          ('Keep sharing, but change the password monthly', 'still shared'), ('Give helpers the bank password too', 'worse'),
          ('Remove all helpers\' access to orders', 'unworkable'), 'Individual, limited access.'),
        Q('An access list has 5 people with full admin rights, but only the owner needs them. How many should be reduced?', '4',
          ('5', 'includes owner'), ('1', 'owner only'), ('0', 'some should change'), '5 - 1 = 4.', calc=lambda: 5 - 1 == 4),
        Q('A bookkeeper needs to see bank transactions but not move money. What access fits?', 'View-only access',
          ('Full access to transfer funds', 'more than needed'), ('The owner\'s personal login', 'shared'),
          ('No access at all', 'cannot work'), 'Match access to need.'),
        Q('A helper leaves on Friday. Which checklist item matters most that day?', 'Remove their logins and change any shared codes',
          ('Send a thank-you card to them next month', 'not urgent'), ('Update the logo', 'unrelated'), ('Order new supplies', 'unrelated'),
          'Close access promptly.'),
        Q('What should the access list record?', 'Each person, each service and their access level', ('Only first names', 'incomplete'),
          ('Only everyone\'s passwords written in plain text', 'insecure'), ('Only the owner', 'incomplete'), 'Who has what.'),
    ]),
    F2=sec('Handle the complications: lockouts and role changes', ACCESS, [
        Q('A designer set up the store under her own admin account and stopped replying. What could the owner have done?', 'Kept the admin account in her own name from the start',
          ('Nothing could prevent it', 'it could'), ('Given the designer even more access to everything', 'worse'), ('Avoided having a store', 'overreaction'),
          'Own the master account.'),
        Q('A helper moves from packing to marketing. What should happen to access?', 'Add marketing access and remove unneeded packing access',
          ('Keep all the old access and add the new access', 'access creep'), ('Remove all access', 'cannot work'), ('Share the owner\'s login', 'insecure'),
          'Update with role changes.'),
        Q('A review finds an ex-helper still has access 6 months after leaving. What should the owner do?', 'Remove it now and check activity on that account',
          ('Leave it alone, since nothing bad has happened', 'risk'), ('Give them more access', 'worse'), ('Ask them to stop logging in', 'not enough'),
          'Close and check.'),
        Q('Reviewing access takes 15 minutes each quarter. How many minutes per year?', '60 minutes', ('15 minutes', 'one quarter'),
          ('45 minutes', 'three quarters'), ('180 minutes', 'monthly'), '15 x 4 = 60.', calc=lambda: 15 * 4 == 60),
        Q('Which statement is accurate?', 'Separate, limited logins make access easier to control.',
          ('Sharing one login is safer.', 'not true'), ('Everyone on the team should be an administrator.', 'risky'),
          ('Access never needs review.', 'it does'), 'Control access.'),
    ]))

# ------------------------------------------------------------------ Set 109: organizing records and file names
FILES = ('Records you cannot find are almost as bad as no records. Use a simple FOLDER STRUCTURE, for example by year, then '
         'by type: 2026 / Receipts, 2026 / Invoices, 2026 / Contracts, 2026 / Tax. Use consistent FILE NAMES that sort well, '
         'with the date first in year-month-day order: "2026-03-14 Invoice 104 Lopez.pdf." Keep originals and important '
         'signed documents, and store backups separately. A few minutes of naming now saves hours of searching later.')

s109 = SET('ENT.OPS.06',
    M=sec('Organize folders and name files so they sort and search well', FILES, [
        Q('Which file name sorts best by date?', '"2026-03-14 Invoice 104 Lopez.pdf"', ('"invoice final final Lopez.pdf"', 'no date'),
          ('"March 14 invoice.pdf"', 'sorts alphabetically by month name'), ('"scan0047.pdf"', 'no meaning'),
          'Year-month-day first.'),
        Q('Which folder structure does the passage suggest?', 'By year, then by type', ('All files in one big folder', 'hard to find'),
          ('By the color of each document', 'irrelevant'), ('Random folders for each day', 'too many'), 'Year then type.'),
        Q('Why put the date first as year-month-day?', 'Files then sort in date order', ('It looks more official', 'not the reason'),
          ('Computers require it by law', 'no'), ('It hides the file', 'no'), 'Sorting.'),
        Q('Which documents should especially be kept?', 'Originals and important signed documents', ('Only blank forms', 'not important'),
          ('Only advertisements received in the mail', 'not important'), ('Only duplicate copies', 'not originals'), 'Key records.'),
        Q('What does good naming save later?', 'Time spent searching', ('Taxes owed', 'no'), ('Shipping costs each month', 'no'),
          ('Rent', 'no'), 'Findability.'),
    ]),
    B=[cs('Labeled kitchen jars', 'Imagine a kitchen where every jar is unlabeled. Finding the sugar means opening each jar. '
          'Labeled jars, arranged by type on shelves, make it quick. Digital files work the same way: folders are the '
          'shelves and file names are the labels. A clear label that starts with the date is like writing "packed March '
          '2026" on a jar.', [
        Q('Unlabeled jars are like what?', 'Files with meaningless names', ('Well-named files with dates', 'no'), ('A tidy folder', 'no'),
          ('A backup', 'no'), 'Hard to find.'),
        Q('Shelves in the kitchen are like what?', 'Folders', ('File names', 'labels'), ('Passwords', 'no'), ('Printers', 'no'),
          'Grouping.'),
        Q('Labels on jars are like what?', 'File names', ('Folders', 'shelves'), ('Backups', 'no'), ('Invoices sent', 'no'),
          'Identification.'),
        Q('"Packed March 2026" on a jar is like what?', 'A date in the file name', ('A price', 'no'), ('A recipe', 'no'),
          ('A secret password on a jar', 'no'), 'Dating items.'),
        Q('What do labels save?', 'Time spent searching', ('Sugar', 'no'), ('Money spent on jars', 'no'), ('Space', 'not the point'),
          'Quick finding.'),
    ], why='A learner who misses MAIN may not see why naming matters; labeled kitchen jars make it concrete.')],
    F1=sec('Apply it: rename and file documents', FILES, [
        Q('Rename "IMG_8831.jpg," a receipt for printer ink bought April 2, 2026. Which name is best?', '"2026-04-02 Receipt printer ink.jpg"',
          ('"ink.jpg"', 'no date'), ('"IMG_8831 copy.jpg"', 'no meaning'), ('"April receipt maybe ink thing.jpg"', 'vague'),
          'Date first and description.'),
        Q('Where should a signed 2026 client contract go?', '2026 / Contracts', ('2026 / Receipts', 'wrong type'),
          ('Desktop with other random files', 'disorganized'), ('A personal photos folder', 'wrong place'), 'Year then type.'),
        Q('An owner spends 20 minutes a week searching for files. Good naming cuts it to 5. How many minutes are saved over 52 weeks?', '780',
          ('15', 'per week'), ('1,040', 'old total'), ('260', 'new total'), '15 x 52 = 780.', calc=lambda: (20 - 5) * 52 == 780),
        Q('Which name sorts correctly before "2026-11-05 Invoice.pdf"?', '"2026-02-14 Invoice.pdf"', ('"2026-12-01 Invoice.pdf"', 'later'),
          ('"2027-01-01 Invoice.pdf"', 'later'), ('"2026-11-30 Invoice.pdf"', 'later'), 'Earlier date sorts first.'),
        Q('Receipts are scanned into folders. What else should happen?', 'Back up the folders to a separate place', ('Delete the folders', 'no'),
          ('Rename every file in them to just "scan"', 'worse'), ('Email them to customers', 'privacy'), 'Backups protect records.'),
    ]),
    F2=sec('Handle the complications: messy history and shared folders', FILES, [
        Q('Three years of files are messy. What is a practical approach?', 'Use the new system now and sort old files over time',
          ('Delete all old files', 'loses records'), ('Rename every old file in one long night this week', 'unrealistic'), ('Ignore it forever', 'stays messy'),
          'Start now, fix gradually.'),
        Q('Two helpers name files differently. What helps?', 'A short written naming rule everyone follows', ('Each person invents their own naming style', 'inconsistent'),
          ('No file names at all', 'unusable'), ('Only the owner saves files', 'bottleneck'), 'Shared standard.'),
        Q('A shared folder contains customers\' personal data. What should be checked?', 'Who has access to it', ('Only the folder color', 'irrelevant'),
          ('Nothing; folders are always private', 'not guaranteed'), ('Only the file count', 'not the issue'), 'Protect data.'),
        Q('A file named "Contract FINAL v3 really final.pdf" sits beside "Contract FINAL v4.pdf." What naming habit would prevent confusion?',
          'Date the versions and keep one marked as the signed copy', ('Add more "final" words to the newest one, to be clear', 'worse'), ('Delete both', 'loses records'),
          ('Name them randomly', 'worse'), 'Clear versions.'),
        Q('Which statement is accurate?', 'Folders and dated names make records easy to find.',
          ('File names never matter.', 'they do'), ('One giant folder is best.', 'hard to search'), ('Backups replace the need for organization.', 'both needed'),
          'Organize.'),
    ]))

# ------------------------------------------------------------------ Set 110: deadline calendar
DEAD = ('Businesses have recurring deadlines: state annual reports, license and permit renewals, sales tax filings, '
        'estimated tax payments, insurance renewals, domain renewals, and registered agent fees. Missing one can bring late '
        'fees, penalties, or even a business being marked inactive by the state. Keep one DEADLINE CALENDAR with each item, '
        'its due date, how often it repeats, where to file, and a reminder set early enough to gather what you need, such '
        'as two weeks before.')

s110 = SET('ENT.OPS.07',
    M=sec('Build one calendar for filings, renewals and payments', DEAD, [
        Q('Which is a recurring business deadline?', 'A state annual report', ('A one-time logo design', 'once'),
          ('A customer\'s birthday', 'not a filing'), ('A holiday sale idea', 'not a deadline'), 'Filings repeat.'),
        Q('What can happen if a state annual report is missed?', 'Fees or the business being marked inactive', ('A tax refund', 'no'),
          ('Nothing ever happens', 'consequences'), ('Automatic renewal for free the next year', 'no'), 'Penalties apply.'),
        Q('What should each calendar entry include?', 'Item, due date, frequency, where to file, reminder',
          ('Only the item name', 'incomplete'), ('Only a color code for each type of deadline', 'incomplete'), ('Only the fee amount', 'incomplete'),
          'Full details.'),
        Q('Why set reminders about two weeks early?', 'To gather what is needed in time', ('To file twice', 'no'),
          ('Because filings always open late', 'not the reason'), ('To pay extra fees', 'no'), 'Preparation time.'),
        Q('Why keep one calendar instead of several notes?', 'All deadlines are in one place', ('Several notes are required', 'no'),
          ('Calendars cause penalties', 'no'), ('It hides deadlines', 'opposite'), 'Single source.'),
    ]),
    B=[cs('A family calendar on the fridge', 'Families often keep one calendar on the fridge: doctor visits, school events, '
          'bills. If every person kept their own scraps of paper, things would be missed. A business deadline calendar works '
          'the same way: one place, every important date, with a note written a couple of weeks before so nothing sneaks '
          'up. Everyone in the business can look in the same place.', [
        Q('A fridge calendar is like what?', 'A business deadline calendar', ('A grocery store receipt slip', 'no'), ('A logo', 'no'), ('A menu', 'no'),
          'One place for dates.'),
        Q('What happens with scattered scraps of paper?', 'Things get missed', ('Everything is remembered', 'no'), ('Taxes drop', 'no'),
          ('Nothing', 'risk'), 'Scattered info fails.'),
        Q('A note written two weeks before is like what?', 'An early reminder', ('A late fee', 'no'), ('A refund', 'no'),
          ('A signed contract', 'no'), 'Advance notice.'),
        Q('Why put every important date in one place?', 'So nothing is missed', ('To make the fridge heavier', 'no'),
          ('To confuse people', 'no'), ('It is required', 'not the reason'), 'Completeness.'),
        Q('A bill due date on the calendar is like what?', 'A renewal or filing deadline', ('A birthday party invitation', 'not business'),
          ('A movie', 'no'), ('A grocery list', 'no'), 'A deadline.'),
    ], why='A learner who misses MAIN may keep deadlines scattered; a family fridge calendar shows the idea.')],
    F1=sec('Apply it: fill in a deadline calendar', DEAD, [
        Q('A license renews on June 30. A two-week reminder should be set for which date?', 'June 16', ('June 30', 'due date'),
          ('July 14', 'after'), ('June 2', 'four weeks'), '30 - 14 = 16.', calc=lambda: 30 - 14 == 16),
        Q('Sales tax is filed quarterly. How many filings a year?', '4', ('12', 'monthly'), ('1', 'yearly'), ('3', 'miscounted'),
          'Quarterly = 4.', calc=lambda: 12 / 3 == 4),
        Q('A late fee is 50 dollars per missed filing. Missing 2 quarterly filings costs how much in late fees?', '100 dollars',
          ('50 dollars', 'one'), ('200 dollars', 'four'), ('25 dollars', 'halved'), '2 x 50 = 100.', calc=lambda: 2 * 50 == 100),
        Q('Which items belong on the calendar?', 'Annual report, license, estimated tax and domain dates',
          ('Only the owner\'s vacation dates and public holidays', 'not business'), ('Only social media posts', 'incomplete'), ('Only supplier birthdays', 'not filings'),
          'All recurring obligations.'),
        Q('Where should the owner confirm actual due dates?', 'The official agency or provider for each item', ('A friend\'s business calendar from last year', 'unreliable'),
          ('A guess', 'unreliable'), ('A competitor', 'unreliable'), 'Official sources.'),
    ]),
    F2=sec('Handle the complications: changes and missed deadlines', DEAD, [
        Q('The owner moves the business to a new state. What should she do with the calendar?', 'Add the new state\'s filings; drop old ones as they end',
          ('Keep only the old state\'s dates on the calendar', 'outdated'), ('Delete the calendar', 'loses tracking'), ('Guess new dates', 'unreliable'),
          'Update for changes.'),
        Q('A filing was missed last month. What is the best first step?', 'File as soon as possible and check what fees apply',
          ('Wait to see whether anyone at the state notices', 'worse'), ('Never file again', 'worse'), ('Pay a random amount', 'not a fix'),
          'Act promptly.'),
        Q('A reminder fires, but the owner is traveling. What helps?', 'Early reminders and a named backup person',
          ('Ignoring the reminder', 'missed'), ('Removing all reminders while traveling', 'worse'), ('Filing a year late', 'penalties'),
          'Plan for absence.'),
        Q('A state changes its annual report due date. What should the owner do?', 'Update the calendar entry and source note',
          ('Keep the old date', 'wrong'), ('Assume nothing changed at all this year', 'risky'), ('Stop filing', 'harmful'), 'Keep current.'),
        Q('Which statement is accurate?', 'One calendar with early reminders prevents many fees.',
          ('Deadlines never change.', 'they can'), ('States never mark businesses inactive for missed reports.', 'they can'),
          ('Reminders on the due day are enough.', 'too late'), 'Plan early.'),
    ]))

# ------------------------------------------------------------------ Set 111: official notices versus paid solicitations
NOTICE = ('New businesses receive official-looking letters. Some are real: tax agency notices, state filing reminders. '
          'Others are PAID SOLICITATIONS designed to look official, offering to file your annual report or provide a '
          '"certificate" for a large fee, or charging for things that are free, like an EIN from the IRS. Check the sender\'s '
          'name, look for small print saying "this is not a government agency," and verify by going to the official website '
          'or calling a number you find yourself. Never pay just because a letter looks urgent.')

s111 = SET('ENT.OPS.08',
    M=sec('Tell real government notices from look-alike paid offers', NOTICE, [
        Q('What is a paid solicitation in this context?', 'An offer designed to look official that charges a fee',
          ('A real tax bill from the IRS', 'official'), ('A customer\'s payment', 'no'), ('A supplier invoice for goods the business received', 'real bill'),
          'Look-alike offer.'),
        Q('What small print may reveal a solicitation?', '"This is not a government agency"', ('"Thank you for your order"', 'unrelated'),
          ('"Printed on recycled paper stock"', 'unrelated'), ('"Page 1 of 2"', 'unrelated'), 'Disclaimer.'),
        Q('A letter charges 150 dollars to get an EIN. What should the owner know?', 'The IRS issues EINs for free',
          ('EINs always cost 150 dollars', 'false'), ('Only letters can issue EINs', 'false'), ('The fee is required by law', 'false'),
          'Free from IRS.'),
        Q('How should a notice be verified?', 'Through the official website or a number you find yourself', ('By calling only the phone number printed on the letter', 'may be fake'),
          ('By replying with a check', 'risky'), ('By guessing', 'unreliable'), 'Independent verification.'),
        Q('Why not pay just because a letter looks urgent?', 'Urgency is a common pressure tactic', ('Urgent letters are always real', 'not true'),
          ('Paying fast lowers fees', 'not true'), ('Agencies require same-day payment', 'not generally'), 'Pressure tactic.'),
    ]),
    B=[cs('A costume uniform', 'Anyone can buy a costume that looks like a police uniform. The uniform alone does not prove who '
          'someone is; you would check a badge number with the station. Official-looking letters are similar: a seal, a '
          'serious font and "FINAL NOTICE" in red do not prove a letter is from the government. Check the source yourself.', [
        Q('Does a uniform prove who someone is?', 'No', ('Yes, always', 'can be faked'), ('Only at night', 'no'), ('Only if it is blue', 'no'),
          'Appearance is not proof.'),
        Q('A seal and serious font on a letter are like what?', 'A costume uniform', ('A verified badge', 'not verified'),
          ('A signed receipt', 'no'), ('A bank statement', 'no'), 'Look official only.'),
        Q('How would you check the person in uniform?', 'Call the station with a number you know', ('Ask them only', 'not independent'),
          ('Trust the uniform you can clearly see', 'risky'), ('Ignore it', 'not checking'), 'Independent check.'),
        Q('"FINAL NOTICE" in red proves what?', 'Nothing by itself', ('That it is official', 'no'), ('That you owe money', 'no'),
          ('That it is free', 'no'), 'Wording is not proof.'),
        Q('What is the lesson?', 'Check the source yourself', ('Pay quickly', 'no'), ('Ignore all mail forever', 'too far'),
          ('Trust fonts', 'no'), 'Verify.'),
    ], why='A learner who misses MAIN may trust official-looking mail; a costume uniform shows why appearance is not proof.')],
    F1=sec('Apply it: sort the mail', NOTICE, [
        Q('A letter titled "Annual Minutes Requirement" asks for 125 dollars, from "Business Compliance Services," with small print '
          '"not affiliated with any government agency." What is it?', 'A paid solicitation', ('An official state bill', 'disclaimer says not'),
          ('A tax refund', 'no'), ('A customer order', 'no'), 'Private offer.'),
        Q('A letter says it is from the state and the annual report is due. What should the owner do?', 'Check the due date on the state\'s official website',
          ('Pay the letter\'s company directly without checking', 'risky'), ('Throw it away unread', 'may be real'),
          ('Call the number in the letter only', 'not independent'), 'Verify officially.'),
        Q('The state fee is 20 dollars; a look-alike service charges 175 dollars to file the same report. How much more is the service?',
          '155 dollars', ('175 dollars', 'service price'), ('195 dollars', 'added'), ('20 dollars', 'state fee'), '175 - 20 = 155.',
          calc=lambda: 175 - 20 == 155),
        Q('Which sign most suggests a real IRS notice?', 'It can be confirmed through official IRS channels',
          ('It demands gift cards', 'scam'), ('It uses lots of red ink', 'not proof'), ('It threatens arrest within an hour unless she pays', 'scam sign'),
          'Verifiable through official channels.'),
        Q('A "trademark registry" letter offers to list the business name for 900 dollars. What should the owner check?', 'Whether it is an official office or a private listing service',
          ('Nothing; pay to protect the name', 'may be useless'), ('Only the letter\'s paper quality', 'irrelevant'),
          ('Only whether the 900-dollar fee must be paid by today', 'pressure'), 'Verify the source.'),
    ]),
    F2=sec('Handle the complications: already paid and mixed mail', NOTICE, [
        Q('An owner already paid a look-alike service. What should she do?', 'Check that the real filing was done; dispute the charge if needed',
          ('Assume everything is properly filed because she already paid', 'may not be'), ('Pay again to be safe', 'waste'), ('Ignore it', 'risk'), 'Confirm and act.'),
        Q('A helper opens mail and pays "bills." What rule helps?', 'New payees need the owner\'s approval after checking',
          ('Pay anything that looks official and urgent', 'risky'), ('Pay nothing ever', 'misses real bills'), ('Let suppliers decide', 'no'),
          'Approval step.'),
        Q('A real tax notice arrives with a deadline. What should the owner not do?', 'Ignore it', ('Read it carefully', 'good'),
          ('Verify it officially', 'good'), ('Ask a tax professional if unsure', 'good'), 'Real notices need action.'),
        Q('Five letters arrive: 2 are confirmed official, 3 are solicitations. What fraction are solicitations?', '3/5',
          ('2/5', 'official'), ('3/2', 'ratio'), ('5/3', 'reversed'), '3 of 5.', calc=lambda: 3 / 5 == 0.6),
        Q('Which statement is accurate?', 'Looking official is not proof, so verify independently.',
          ('All official-looking letters are real government mail.', 'not true'), ('All business mail is a scam.', 'not true'),
          ('Paying quickly is always safest.', 'not true'), 'Verify.'),
    ]))

# ------------------------------------------------------------------ Set 112: lost phone, lost account, continuity
CONT = ('A business should keep running if something goes wrong: a lost phone, a hacked email, a sick owner. Prepare '
        'RECOVERY OPTIONS: backup codes for two-step login stored safely, an up-to-date recovery email and phone, and '
        'knowledge of how to reach each service\'s support. Write a short CONTINUITY PLAN: where key information is, who '
        'can step in for urgent tasks, and how customers will be told about delays. Test the plan once, for example by '
        'logging in with backup codes.')

s112 = SET('ENT.OPS.09',
    M=sec('Prepare recovery options and a short continuity plan', CONT, [
        Q('What are backup codes for two-step login?', 'One-time codes to sign in if the phone is lost',
          ('Codes that turn off two-step security forever', 'not their purpose'), ('Discount codes for customers', 'unrelated'),
          ('Codes for the office alarm', 'unrelated'), 'Recovery access.'),
        Q('What does a continuity plan cover?', 'Where key information is, who steps in, what customers hear',
          ('Only the business\'s logo design', 'irrelevant'), ('Only next year\'s marketing', 'irrelevant'),
          ('Only the owner\'s vacation photos and her travel plans', 'irrelevant'), 'Keeping things running.'),
        Q('Where should backup codes be kept?', 'Somewhere safe and separate from the phone', ('On the same phone, and nowhere else', 'lost together'),
          ('Posted on social media', 'insecure'), ('Emailed to customers', 'insecure'), 'Separate safe place.'),
        Q('Why test the plan once?', 'To find problems before a real emergency', ('Testing breaks accounts', 'no'),
          ('Plans never need any testing at all', 'they do'), ('It is required daily', 'no'), 'Practice reveals gaps.'),
        Q('What should be up to date for account recovery?', 'The recovery email and phone', ('The logo file', 'irrelevant'),
          ('The office plants', 'irrelevant'), ('The shop\'s holiday schedule', 'irrelevant'), 'Recovery contacts.'),
    ]),
    B=[cs('A spare house key and a neighbor', 'Many people leave a spare key with a trusted neighbor and tell them which plants '
          'need water if they are away. If they lose their own key, they can still get in; if they are sick, the neighbor '
          'can help. Backup codes are the spare key. A continuity plan is the note telling the neighbor what to do.', [
        Q('Backup codes are like what?', 'A spare house key', ('A broken door lock', 'no'), ('A new house', 'no'), ('A doorbell', 'no'),
          'Way back in.'),
        Q('The note for the neighbor is like what?', 'A continuity plan', ('A weekly grocery list', 'no'), ('A bill', 'no'), ('A receipt', 'no'),
          'Instructions to keep things going.'),
        Q('Who keeps the spare key?', 'A trusted neighbor', ('A stranger', 'no'), ('Nobody', 'no'), ('The mail carrier', 'no'),
          'Trusted person.'),
        Q('What can happen if you lose your own key?', 'You can still get in with the spare', ('You can never get in', 'not with spare'),
          ('The house simply disappears overnight', 'no'), ('Rent doubles', 'no'), 'Recovery.'),
        Q('Why tell the neighbor which plants need water?', 'So they can help while you are away', ('To confuse them', 'no'),
          ('To sell the plants while you are away', 'no'), ('It is required', 'no'), 'Clear instructions.'),
    ], why='A learner who misses MAIN may not picture recovery planning; a spare key with a neighbor makes it familiar.')],
    F1=sec('Apply it: prepare for a lost phone', CONT, [
        Q('An owner\'s phone holds her two-step codes and is lost. Which preparation would have helped most?', 'Backup codes stored safely elsewhere',
          ('A new phone case', 'irrelevant'), ('A longer password on the lost phone only', 'not recovery'), ('More apps', 'irrelevant'),
          'Recovery codes.'),
        Q('A plan names a backup person for urgent orders. What should that person have?', 'Limited access and written steps for urgent tasks',
          ('The owner\'s full bank login', 'too much'), ('Nothing at all', 'cannot help'), ('Every password written on one sticky note', 'insecure'),
          'Enough to help safely.'),
        Q('The owner is sick for 5 days with 8 orders a day due. How many orders must be handled or delayed?', '40',
          ('8', 'one day'), ('13', 'added'), ('5', 'days'), '5 x 8 = 40.', calc=lambda: 5 * 8 == 40),
        Q('Which customer message fits a short delay?', '"Orders this week will ship by Monday. Thank you for your patience."',
          ('No message at all', 'silence'), ('"We may or may not ship your order ever, sorry about that, bye."', 'alarming'), ('"Your order is your problem."', 'rude'),
          'Clear and honest.'),
        Q('A test login with backup codes fails. What should the owner do?', 'Generate new codes and store them correctly',
          ('Ignore it until a real emergency happens', 'too late'), ('Turn off all security', 'unsafe'), ('Delete the account', 'overreaction'),
          'Fix before needed.'),
    ]),
    F2=sec('Handle the complications: hacked accounts and single points of failure', CONT, [
        Q('The business email is hacked and sending scams to customers. What is the first step?', 'Recover the account officially, then warn customers',
          ('Wait for it to stop by itself', 'harm continues'), ('Create a new email address and never mention it', 'customers unaware'),
          ('Pay the hacker', 'risky'), 'Contain and inform.'),
        Q('Only the owner knows where key information is. What is the risk?', 'If she is unavailable, no one can keep things running',
          ('No risk at all', 'single point of failure'), ('More privacy for the owner, always a good thing', 'not the issue'), ('Lower taxes', 'no'),
          'Document essentials.'),
        Q('A recovery email is an old address the owner no longer checks. What should she do?', 'Update it to a current address',
          ('Leave it; it rarely matters', 'it matters in recovery'), ('Delete recovery options', 'worse'), ('Use a customer\'s email', 'no'),
          'Keep recovery current.'),
        Q('A continuity plan takes 1 hour to write and 30 minutes to test. How many minutes total?', '90 minutes',
          ('60 minutes', 'writing only'), ('30 minutes', 'testing only'), ('130 minutes', 'misadded'), '60 + 30 = 90.',
          calc=lambda: 60 + 30 == 90),
        Q('Which statement is accurate?', 'Recovery options and a tested plan keep a business running.',
          ('Small businesses never need plans.', 'they do'), ('Backup codes can be stored on the same phone safely.', 'lost together'),
          ('Customers prefer silence during delays and problems.', 'not usually'), 'Prepare.'),
    ]))

SETS = [s104, s105, s106, s107, s108, s109, s110, s111, s112]
