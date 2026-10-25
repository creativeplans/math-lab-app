"""Entrepreneurship sets 15-18: Foundation 3, testing demand (part 2)."""
from eq import Q, sec, cs, SET

# ------------------------------------------------------------------ Set 15: likes are not demand
LIKES = ('Likes, follows, views and compliments feel good, but they are weak signs of demand. They cost people nothing, '
         'so many people give them freely. A post with 2,000 likes may lead to zero sales. Followers can also be '
         'people who enjoy your content but will never buy, or accounts that are not real people. To judge demand, '
         'look for actions that cost the person something: purchases, deposits, bookings, or replies asking how to buy. '
         'Treat likes as a sign of attention, not of buying.')

s15 = SET('ENT.TEST.06',
    M=sec('Explain why likes and praise are weak demand signals', LIKES, [
        Q('A post about a new candle got 3,000 likes and 2 sales. What does this most likely show?',
          'Many people noticed it, but few wanted to buy.', ('Demand is very strong because of the likes.',
                                                              'likes did not turn into sales'),
          ('The likes prove sales will rise soon.', 'likes do not predict sales reliably'),
          ('Likes and sales always move together.', 'this example shows they do not'),
          'Attention is not the same as buying.'),
        Q('Why are compliments weak evidence of demand?', 'They cost nothing to give.',
          ('They are always insincere and untrue.', 'they can be sincere but still free'),
          ('Customers never give compliments.', 'many do'),
          ('Compliments are illegal to collect.', 'not illegal'), 'Free signals do not show willingness to pay.'),
        Q('Which action is the strongest sign of demand?', 'A message asking how to place an order',
          ('A heart reaction on a product photo', 'free and quick'),
          ('A new follower on a social account', 'free and quick'),
          ('A comment saying "so cute!"', 'free praise'), 'Asking how to buy shows intent to purchase.'),
        Q('A creator has 10,000 followers but sells almost nothing. Which is a likely reason?',
          'Followers enjoy the content but are not buyers.', ('10,000 followers always buy something.', 'not true'),
          ('Followers are the same as paying customers.', 'they are not'),
          ('Sales are impossible on social media.', 'many sell on social media'),
          'Followers can be fans of content without needing to buy.'),
        Q('What should likes be treated as?', 'A sign of attention', ('A sign of guaranteed profit', 'no guarantee'),
          ('A replacement for sales', 'they are not sales'), ('A legal contract', 'no'),
          'Likes show that something got noticed.'),
    ]),
    B=[cs('Attention versus buying', 'Think of a store window. Many people stop to look at a pretty display; that is '
          'attention. Far fewer walk in, and fewer still buy. Online, a like is the same as glancing at the window. A '
          'business needs the people who walk in and pay. When you measure an idea, count the people who acted with '
          'money or real effort, not the people who glanced.', [
        Q('People stopping to look at a store window show what?', 'Attention', ('Purchases', 'they did not buy'),
          ('Profit', 'nothing was sold'), ('Refunds', 'nothing was returned'), 'Looking is attention.'),
        Q('Online, a like is most like what?', 'Glancing at a store window', ('Paying for an item at the counter', 'a like costs nothing'),
          ('Signing a lease', 'unrelated'), ('Returning an item', 'unrelated'), 'A like is a quick glance.'),
        Q('Who matters most when measuring demand?', 'People who pay or make a real commitment',
          ('People who glance', 'attention only'), ('People who scroll past', 'no action'),
          ('People who scroll by and never notice the post', 'no action'), 'Paying or committing shows demand.'),
        Q('Which shows buying behavior?', 'A customer pays for an order', ('A person likes a photo', 'attention'),
          ('A person shares a meme', 'attention'), ('A person follows an account', 'attention'), 'Paying is buying.'),
        Q('Many look, few buy. What does this pattern describe?', 'Normal shopping behavior', ('A broken website', 'not necessarily'),
          ('A legal problem', 'no'), ('A guaranteed failure', 'no'), 'Most attention never becomes a purchase.'),
    ], why='A learner who misses MAIN may equate attention with demand; the store window shows the gap between looking '
           'and buying.')],
    F1=sec('Apply it: read social signals sensibly', LIKES, [
        Q('Two products: A got 900 likes and 5 orders. B got 120 likes and 30 orders. Which shows stronger demand?',
          'Product B', ('Product A, because it got more likes', 'fewer orders'),
          ('Both equally, since both got likes', 'orders differ'), ('Neither, since likes were low', 'B sold well'),
          'Orders show demand; B had six times as many.', calc=lambda: 30 / 5 == 6),
        Q('A baker wants a better demand signal than likes. Which step helps most?',
          'Post a pre-order link for Saturday pickup', ('Ask followers to like the post more', 'still likes'),
          ('Post more photos of the same cake', 'more attention, not orders'),
          ('Buy a follower package to look popular', 'fake followers mislead'),
          'A pre-order link turns attention into a real commitment.'),
        Q('A video got 50,000 views. 25 viewers bought the product. What fraction of viewers bought?', '1 in 2,000',
          ('1 in 200', 'that would be 250 buyers'), ('1 in 20', 'that would be 2,500 buyers'),
          ('1 in 50', 'that would be 1,000 buyers'), '50,000 / 25 = 2,000, so 1 in 2,000 bought.',
          calc=lambda: 50000 / 25 == 2000),
        Q('Which comment is the most useful demand signal?', '"Do you ship to Ohio? I want two."',
          ('"Love this!!!"', 'praise only'), ('"So pretty"', 'praise only'), ('"Following for more posts like this one"', 'attention only'),
          'Asking about shipping two items shows buying intent.'),
        Q('A founder plans to judge a launch by likes. What better measure fits the goal of sales?',
          'Orders and sales in the first two weeks', ('Number of likes in the first hour', 'attention only'),
          ('Number of emoji reactions', 'attention only'), ('Number of shares by friends', 'attention only'),
          'The goal is sales, so measure sales.'),
    ]),
    F2=sec('Handle the complications: when attention misleads', LIKES, [
        Q('A post went viral because of a funny mistake in the video, not the product. Sales did not change. What is '
          'the best conclusion?', 'The attention was about the mistake, not demand for the product.',
          ('Viral posts always prove product demand.', 'not here'),
          ('The product must be terrible because sales stayed flat.', 'too strong a conclusion'),
          ('The founder should repeat the mistake on purpose.', 'not a reliable plan'),
          'Viral attention can be about something other than the product.'),
        Q('A seller bought 5,000 followers. Likes rose, sales did not. What is the main problem?',
          'Bought followers are often not real buyers, so the numbers mislead.', ('Followers are always real customers.',
                                                                                   'bought followers are not'),
          ('Sales never follow followers.', 'real followers can buy'),
          ('Buying followers always increases sales a lot over time.', 'it did not here'),
          'Fake or bought followers inflate numbers without adding customers.'),
        Q('Many friends praise a product idea online. Before investing, what should the founder check?',
          'Whether people outside her circle will pay', ('Whether friends will keep praising it', 'praise is weak'),
          ('Whether the post can get more hearts', 'still attention'),
          ('Whether to buy more followers', 'misleading'),
          'Paying strangers are better evidence than praising friends.'),
        Q('An account has high engagement (many comments) but low sales. Which next test best checks demand?',
          'Offer a limited paid pre-order and count buyers', ('Ask for even more comments', 'still attention'),
          ('Post more often each day without any offer or link', 'no test of buying'), ('Delete the account', 'too extreme'),
          'A paid offer tests whether engaged followers will buy.'),
        Q('A post with 4,000 likes sold 8 items at 15 dollars each. What were total sales?', '120 dollars',
          ('60,000 dollars', 'that multiplies likes by price'), ('4,015 dollars', 'that adds likes and price'),
          ('15 dollars', 'one item'), '8 x 15 = 120 dollars; the likes did not add sales.', calc=lambda: 8 * 15 == 120),
    ]))

# ------------------------------------------------------------------ Set 16: continue, change or stop
DECIDE = ('After a test, decide: continue, change, or stop. CONTINUE when the results meet the target you set in '
          'advance. CHANGE (sometimes called a pivot) when part of the idea works but something important does not: a '
          'different customer, price, or offer might fit better. STOP when the results are far below the target and '
          'nothing points to a better version, or when the cost of continuing is too high. Stopping is not failing; it '
          'protects time and money for a better idea.')

s16 = SET('ENT.TEST.07',
    M=sec('Decide from results whether to continue, change or stop', DECIDE, [
        Q('Target: 20 paid bookings in a month. Result: 26 bookings. What is the sensible decision?', 'Continue',
          ('Stop', 'the target was exceeded'), ('Change the target to 40 and call it a failure', 'moving targets afterward is unfair'),
          ('Ignore the result', 'results should guide the decision'), 'Results above the target support continuing.',
          calc=lambda: 26 >= 20),
        Q('Target: 20 bookings. Result: 3 bookings, and customers said the price was fine but the hours did not suit '
          'them. What fits best?', 'Change the hours and test again', ('Continue exactly as before', 'results were far below target'),
          ('Stop, since all ideas with 3 bookings fail', 'the feedback points to a fixable issue'),
          ('Raise the price immediately', 'price was not the problem'),
          'Part works (price) and part does not (hours); a change is worth testing.'),
        Q('Target: 30 sales. Result: 1 sale. No feedback suggests a better version, and costs keep rising. What fits '
          'best?', 'Stop and move to a better idea', ('Continue with more money', 'nothing suggests improvement'),
          ('Call it a success because one person bought', 'far below target'),
          ('Change only the logo', 'a logo will not fix demand this weak'),
          'Far below target with no promising signal supports stopping.'),
        Q('What does "pivot" mean here?', 'Changing an important part of the idea based on what you learned',
          ('Closing the business for good', 'that is stopping'), ('Repeating the same test again with nothing changed at all', 'that is continuing'),
          ('Hiring a large team at once', 'unrelated'), 'A pivot keeps what works and changes what does not.'),
        Q('Why is stopping sometimes the right decision?', 'It saves time and money for a better idea.',
          ('It proves the founder made no mistakes.', 'not the point'), ('It always earns money back.', 'it may not'),
          ('It is required after any first test.', 'not required'), 'Stopping protects resources.'),
    ]),
    B=[cs('Three choices after a test', 'Think of baking a new cookie for a school sale. If most cookies sell, keep '
          'making them (continue). If people love the taste but say the cookies are too big for the price, make them '
          'smaller (change). If almost no one buys and no one says why, try a different treat (stop). The decision '
          'follows the results and what people told you, not how much you hoped it would work.', [
        Q('Most cookies sold. What is the choice?', 'Continue', ('Change', 'nothing needs changing'),
          ('Stop', 'they sold well'), ('Ignore', 'results matter'), 'Good results mean continue.'),
        Q('People loved the taste but said cookies were too big for the price. What is the choice?', 'Change the size',
          ('Stop selling cookies', 'the taste works'), ('Continue unchanged', 'feedback points to a change'),
          ('Double the price', 'the problem was value for size'), 'Part works; adjust the part that does not.'),
        Q('Almost no one bought, and no one said why. What is the choice?', 'Try a different treat',
          ('Make twice as many cookies', 'demand is weak'), ('Keep going exactly the same', 'no reason to expect change'),
          ('Raise the price', 'unlikely to help'), 'Weak results with no clue suggest stopping.'),
        Q('What should guide the choice?', 'The results and what people said', ('How much you hoped it would work', 'hope is not evidence'),
          ('What your friends prefer', 'friends are not the market'), ('The color of the packaging', 'not the main factor'),
          'Evidence guides the decision.'),
        Q('"Change" means what?', 'Keep what works and adjust what does not', ('Start everything from zero with a brand-new idea', 'that is stopping'),
          ('Do nothing new', 'that is continuing'), ('Close forever', 'that is stopping'), 'Change is a targeted adjustment.'),
    ], why='A learner who misses MAIN may not see how results map to a decision; a simple bake-sale example connects '
           'each outcome to a choice.')],
    F1=sec('Apply it: decide with stated targets and feedback', DECIDE, [
        Q('A tutoring test set a target of 8 students. It got 9 students, but each needs 2 hours of travel. The tutor\'s '
          'goal is to earn at least 25 dollars per hour of total time. Each session pays 40 dollars for 1 hour of '
          'teaching. What should the tutor conclude?', 'Demand is there, but travel time makes the pay too low; change the setup',
          ('Continue unchanged, because the target of 8 students was met and passed', 'the earnings goal is missed'),
          ('Stop, because tutoring never works', 'demand exists'),
          ('Raise the target to 20 students', 'more students would not fix the hourly pay'),
          '40 dollars / 3 hours is about 13 dollars an hour, below 25; a change such as online sessions is needed.',
          calc=lambda: 40 / 3 < 25),
        Q('A juice stand sold 70 cups against a target of 50, but lost money because cups cost too much. Best next step?',
          'Continue selling but change the cost or price', ('Stop immediately, since it lost money', 'demand was strong'),
          ('Ignore the loss because sales were high', 'losses add up'),
          ('Lower the price to sell even more', 'that increases the loss'),
          'Strong demand plus a cost problem calls for a change, not stopping.'),
        Q('An app test: target 100 sign-ups, result 95, and users who signed up used it every day. What fits best?',
          'Continue; it is close to target and usage is strong', ('Stop, because 95 is below 100', 'a near miss with strong usage'),
          ('Change everything about the app, from the name to the features', 'it is mostly working'),
          ('Delete the app and start over', 'too extreme'),
          'A near-target result with strong usage supports continuing.'),
        Q('A dog-walking test got many requests, but almost all were for cat sitting. What change is most sensible?',
          'Test a cat-sitting offer', ('Keep offering only dog walking', 'ignores the clear signal'),
          ('Stop all pet services', 'there is clear demand'), ('Raise dog-walking prices', 'not the signal'),
          'Customer requests point toward a better offer.'),
        Q('A test cost 300 dollars and earned 120 dollars, far below the 400-dollar target, with no useful feedback. What '
          'is the most reasonable choice?', 'Stop or test a clearly different idea', ('Spend 3,000 dollars more on the same plan',
                                                                                      'no sign it would improve'),
          ('Call it a success', 'far below target'), ('Change only the font on the flyer', 'too small a change'),
          'Far below target with no signal supports stopping.', calc=lambda: 120 < 400),
    ]),
    F2=sec('Handle the complications: mixed and unclear results', DECIDE, [
        Q('Results are mixed: half the customers loved it, half asked for refunds. What should the founder check before '
          'deciding?', 'What the happy and unhappy customers have in common', ('Which group is louder online', 'not the key fact'),
          ('Whether to raise prices for every customer right away', 'premature'), ('Whether the logo is popular', 'not relevant'),
          'Finding what separates the two groups points to the right customer or change.'),
        Q('A founder keeps lowering the success target after each weak test so she can "continue." What is the problem?',
          'Moving targets hides weak results and wastes time.', ('Targets should never be set at all.', 'they are useful'),
          ('Lower targets always lead to success in the end.', 'not true'), ('There is no problem with this.', 'it hides evidence'),
          'Targets set in advance keep decisions honest.'),
        Q('A test met its target, but the founder has no time left because of a new job. What is a sensible option?',
          'Pause, or find help, before committing to growth', ('Grow quickly anyway', 'ignores capacity'),
          ('Pretend the test failed so there is no pressure to grow', 'dishonest'), ('Double the target', 'does not solve the time problem'),
          'Good results still require the capacity to deliver.'),
        Q('A test missed its target, but the founder discovers the payment link was broken for most of the test. What '
          'should she do?', 'Fix the link and run the test again', ('Stop the idea based on this result', 'the test was flawed'),
          ('Count the result as a success', 'it was not'), ('Ignore the broken link', 'it affected results'),
          'A flawed test does not give a fair answer; fix and retest.'),
        Q('Target: at least 25 percent of visitors book. Result: 18 of 60 visitors booked. Should the founder continue '
          'by that target?', 'Yes, 30 percent booked, above the target', ('No, 18 is below 25', 'that compares a count with a percent'),
          ('No, only 18 percent booked', '18 is the count; the percent is 30'),
          ('It cannot be judged from these numbers', 'it can'), '18 / 60 = 0.30, which is 30 percent.',
          calc=lambda: 18 / 60 == 0.30),
    ]))

# ------------------------------------------------------------------ Set 17: Zappos case
ZAP = ('Documented history: Zappos founder Nick Swinmurn tested whether people would buy shoes online before holding '
       'any inventory. He photographed shoes at local stores and posted them online; when someone ordered a pair, he '
       'bought it from the store at full price and shipped it. Lesson drawn by this course (an interpretation): you can '
       'test demand before investing in stock, even if each early sale earns little or loses money, because the goal '
       'of the test is to learn. One success story does not guarantee the same result for another business.')

s17 = SET('ENT.CASE.03',
    M=sec('Apply a documented test: sell before holding inventory', ZAP, [
        Q('According to the passage, how did Swinmurn fill early orders?', 'He bought the shoes from local stores and shipped them.',
          ('He shipped shoes from a large warehouse he owned.', 'he held no inventory'),
          ('He asked customers to pick up shoes at his home.', 'not in the passage'),
          ('He had a factory make each pair to order.', 'not in the passage'),
          'He bought each ordered pair at full price from the store.'),
        Q('What question was this test designed to answer?', 'Would people buy shoes online?',
          ('Which shoe color is the most popular?', 'not the main question'),
          ('How cheaply can shoes be made?', 'not tested'), ('Which store has the best staff?', 'not tested'),
          'The test checked whether online shoe buying had demand.'),
        Q('Why might early sales have earned little money?', 'He paid full store price for each pair.',
          ('He gave every pair away free.', 'customers paid'), ('Customers paid twice the price.', 'not stated'),
          ('He had no shipping costs at all on any order.', 'he shipped the shoes'),
          'Buying at full retail left little or no margin.'),
        Q('Mara wants to sell imported tea online but cannot afford stock. Applying the lesson, what is a good first test?',
          'List a few teas, buy them only after orders arrive, and ship', ('Buy a full container of tea first', 'heavy stock first'),
          ('Wait until she can afford to rent a warehouse full of tea', 'no learning meanwhile'),
          ('Assume demand without any test', 'no evidence'), 'Selling before stocking tests demand cheaply.'),
        Q('Which statement fits the course\'s interpretation?', 'Early tests aim to learn, not to maximize profit.',
          ('Every early sale must be profitable.', 'not required in a test'),
          ('Holding large stock is the only real test.', 'the case shows otherwise'),
          ('This method guarantees success for any product.', 'no guarantee'), 'The test\'s goal was learning.'),
    ]),
    B=[cs('Testing demand before stock', 'Imagine opening a small bakery stand. One way: bake 200 loaves and hope they sell. '
          'Another way: take orders first, then bake only what was ordered. The second way risks less, because you buy '
          'ingredients only when customers have committed. It may be slower and less efficient, but it tells you what '
          'people actually want before you spend a lot.', [
        Q('Which approach takes orders first?', 'Bake only what customers ordered', ('Bake 200 loaves and hope', 'no orders first'),
          ('Buy a bakery building first', 'no orders first'), ('Hire staff before any orders', 'no orders first'),
          'Ordering first ties spending to demand.'),
        Q('Why does taking orders first risk less?', 'You spend only after customers commit.',
          ('Ingredients become free.', 'they are not free'), ('Customers pay double.', 'not stated'),
          ('It avoids dealing with any customers at all.', 'it needs customers'), 'Spending follows commitments.'),
        Q('What is a downside of baking only to order?', 'It can be slower and less efficient.',
          ('It guarantees huge waste.', 'it reduces waste'), ('It needs a large warehouse for the bread.', 'it does not'),
          ('It is illegal.', 'not illegal'), 'Small batches can be slower.'),
        Q('Baking 200 loaves before any orders is what?', 'Spending before knowing demand',
          ('Testing demand first with real orders', 'no test happened'), ('A pre-order', 'no orders were taken'),
          ('A refund', 'unrelated'), 'It risks money before evidence.'),
        Q('What does ordering first tell you?', 'What people actually want', ('Your future profit for sure', 'no guarantee'),
          ('The best bakery name', 'unrelated'), ('Nothing useful', 'it shows real demand'), 'Orders reveal real demand.'),
    ], why='A learner who misses MAIN may not see why selling before stocking reduces risk; a bakery makes it concrete.')],
    F1=sec('Apply it: test before stocking in a new business', ZAP, [
        Q('Leo wants to sell custom phone stands. Which plan best applies the lesson?', 'Show photos of a sample, take orders, then make each stand',
          ('Make 1,000 stands in a workshop before showing anyone a sample', 'stock before demand'),
          ('Rent a store before making a sample', 'big cost first'), ('Skip samples and only post a logo', 'no real offer'),
          'Taking orders before production tests demand cheaply.'),
        Q('A seller buys each item at 20 dollars and sells at 22 dollars, plus pays 5 dollars shipping. What happens on '
          'each sale during this test?', 'She loses 3 dollars per sale.', ('She earns 2 dollars per sale.', 'that ignores shipping'),
          ('She earns 7 dollars per sale.', 'that adds shipping instead of subtracting'), ('She breaks even.', 'not quite'),
          '22 - 20 - 5 = -3 dollars per sale.', calc=lambda: 22 - 20 - 5 == -3),
        Q('Given the loss above, why might the test still be worthwhile?', 'It shows whether people buy before investing in stock.',
          ('Losses are always good for a business.', 'not true'), ('It proves the business will make a large profit later.', 'no guarantee'),
          ('Shipping costs do not matter in tests.', 'they matter'), 'A small, temporary loss can buy useful evidence.'),
        Q('A test showed strong orders. What should come next before buying large stock?',
          'Find a supplier price that leaves a profit', ('Keep losing money on every sale forever', 'not sustainable'),
          ('Stop testing and ignore costs', 'costs matter'), ('Raise prices without checking demand', 'risky'),
          'After proving demand, the business must fix its costs.'),
        Q('Which product is LEAST suited to "buy only after an order"?', 'Fresh food that must be ready instantly',
          ('Shoes from a nearby store', 'can be bought after an order'),
          ('Printed posters made on demand after each order', 'made after orders'), ('Books from a supplier', 'can be ordered after sales'),
          'Some products cannot wait for an order to be bought or made.'),
    ]),
    F2=sec('Handle the complications: when the tactic does not fit', ZAP, [
        Q('A store owner learns her photos are being used to sell her shoes without permission. What should a founder '
          'using this tactic have done?', 'Get the store\'s permission to use photos and sell its items',
          ('Assume any photo of a store\'s shoes is free to use online', 'not safe'), ('Hide where the shoes came from', 'unfair'),
          ('Copy the store\'s brand name', 'could be a trademark problem'),
          'Using others\' photos and products needs permission.'),
        Q('Customers expect delivery in 2 days, but buying each item after an order takes 5 days. What is the main risk?',
          'Slow delivery may cause cancellations and bad reviews.', ('There is no risk if the item arrives eventually.', 'expectations matter'),
          ('Customers prefer slow delivery.', 'not usually'), ('Delivery time never matters online.', 'it matters'),
          'The test must still meet customer expectations or tell them clearly.'),
        Q('Which detail should a founder check before copying the "buy after order" approach for a rare product?',
          'Whether the supplier will reliably have the item in stock', ('Whether the founder of Zappos personally liked this kind of product', 'irrelevant'),
          ('What year Zappos started', 'trivia'), ('Whether competitors use the same font', 'irrelevant'),
          'If supply is unreliable, orders may not be filled.'),
        Q('A founder ran the test, lost money on every sale, and kept going for two years without changing costs. What '
          'went wrong?', 'The test turned into a long-term loss without a plan to fix costs.',
          ('Nothing went wrong, because losses are part of every business forever.', 'not sustainable'),
          ('The test should have lasted five years.', 'longer does not fix costs'),
          ('Tests should never lose any money.', 'small losses can be acceptable'),
          'A test should be short and lead to a plan for profitable operation.'),
        Q('Which is the most accurate statement about using a famous founder\'s tactic?',
          'The tactic may help, but your product, costs and customers must be checked.',
          ('The tactic guarantees the same success for any founder who copies it.', 'no guarantee'), ('The tactic never works for anyone else.', 'too strong'),
          ('Only shoe sellers may use it.', 'others can adapt it'), 'Tactics must be adapted to different conditions.'),
    ]))

# ------------------------------------------------------------------ Set 18: Dropbox case
DBX = ('Documented history: before Dropbox was ready for the public, cofounder Drew Houston posted a short demo video '
       'showing how the file-syncing product would work, with a way to join a waiting list for the beta (early test) '
       'version. After the video was shared online, the waiting list grew sharply. Accounts differ on the exact numbers, '
       'so none are used here. Lesson drawn by this course (an interpretation): a clear demonstration can test interest '
       'before a product is finished, but sign-ups are interest, not payment. One success story does not guarantee '
       'the same result.')

s18 = SET('ENT.CASE.04',
    M=sec('Apply a documented test: a demo with a sign-up list', DBX, [
        Q('According to the passage, what did Houston share before the product was public?', 'A short demo video',
          ('A finished product sold in stores', 'it was not finished'), ('A printed catalog of features', 'not mentioned'),
          ('A list of investors', 'not mentioned'), 'He shared a demo video with a waiting-list sign-up.'),
        Q('What did the video let viewers do?', 'Join a waiting list for the early version',
          ('Buy a lifetime plan for the product immediately', 'not stated'), ('Download the finished app', 'not finished'),
          ('Apply for a job at the company', 'not stated'), 'The sign-up was for a beta waiting list.'),
        Q('Why does the passage avoid exact sign-up numbers?', 'Different accounts give different numbers.',
          ('The numbers were secret forever.', 'not stated'), ('There were no sign-ups at all.', 'the list grew'),
          ('Numbers never matter in business stories like this one.', 'they matter, but must be reliable'),
          'When sources disagree, the course avoids the disputed detail.'),
        Q('Which lesson does the course draw?', 'A demo can test interest, but sign-ups are not payment.',
          ('Sign-ups prove customers will pay.', 'sign-ups are weaker than payment'),
          ('Products must be fully finished before any test is run.', 'the case shows otherwise'),
          ('Videos always go viral.', 'no guarantee'), 'Interest is useful evidence but weaker than payment.'),
        Q('Sofia is building a budgeting app. Applying the lesson, what is a good early test?',
          'Show a short demo and offer a waiting list', ('Spend a year building every feature first', 'no early evidence'),
          ('Buy ads for an app that does not exist without explaining it', 'misleading'),
          ('Skip any test and launch in app stores', 'no early evidence'), 'A demo tests interest before full building.'),
    ]),
    B=[cs('Interest versus payment', 'A sign-up list measures interest: people giving their email to hear more. A payment '
          'measures commitment: people giving money. Both are useful, but they are different. Many people sign up for '
          'things they never buy. If a waiting list is large, the next step is to check how many will pay, for example '
          'with a paid early-access offer.', [
        Q('A waiting-list sign-up measures what?', 'Interest', ('Payment', 'no money given'), ('Profit', 'no sale'),
          ('Refunds', 'unrelated'), 'Giving an email shows interest.'),
        Q('Which measures commitment?', 'Paying for early access', ('Joining an email list', 'interest only'),
          ('Watching a demo', 'interest only'), ('Liking a post', 'attention only'), 'Paying shows commitment.'),
        Q('A large waiting list should lead to which next step?', 'Check how many will pay', ('Assume all will pay', 'not safe'),
          ('Stop collecting emails', 'not necessary'), ('Delete the list', 'no reason'), 'Test payment next.'),
        Q('Why can a sign-up list overstate demand?', 'Many people sign up but never buy.', ('Sign-ups cost a lot of money.',
                                                                                             'they are free'),
          ('Sign-ups are always fake.', 'not always'), ('Sign-ups are illegal.', 'no'), 'Free sign-ups are easy to give.'),
        Q('Which is stronger evidence?', '50 paid early-access customers', ('500 email sign-ups for updates', 'interest only'),
          ('5,000 video views', 'attention only'), ('50 likes', 'attention only'), 'Paid customers are strongest.'),
    ], why='A learner who misses MAIN may treat sign-ups as sales; separating interest from payment is the obstacle.')],
    F1=sec('Apply it: a demo test for a new digital product', DBX, [
        Q('A designer has a template idea. Which test follows the lesson AND checks payment?',
          'Show a demo, then offer paid early access at a discount', ('Show a demo only to friends', 'biased audience'),
          ('Build 100 templates before showing anyone a single example', 'no early evidence'), ('Post a logo and wait', 'no real test'),
          'A demo plus a paid offer tests interest and payment.'),
        Q('A demo page got 1,200 visitors and 300 sign-ups. What percent signed up?', '25 percent',
          ('12 percent', 'not the right division'), ('30 percent', 'not the right division'), ('40 percent', 'too high'),
          '300 / 1,200 = 0.25, or 25 percent.', calc=lambda: 300 / 1200 == 0.25),
        Q('Of the 300 sign-ups, 15 paid for early access. What does this show?', 'Some real demand, much smaller than the sign-up list',
          ('All 300 will certainly pay later', 'not shown'), ('No demand at all', '15 paid'),
          ('Payments do not matter much if the number of sign-ups is high', 'payments matter most'),
          'Only 15 of 300 paid, so paid demand is about 5 percent of sign-ups.', calc=lambda: 15 / 300 == 0.05),
        Q('Which demo would be misleading?', 'A video showing features that do not exist and are not planned',
          ('A video showing a real early prototype', 'honest'), ('A video clearly labeled "planned features"', 'honest labeling'),
          ('A short screen recording that shows the current early version', 'honest'), 'Showing features that will not exist misleads people.'),
        Q('After a strong demo test, what should a founder do before promising a launch date?',
          'Check how long building the real product will take', ('Promise the earliest possible date anyway to keep people excited', 'risky'),
          ('Stop talking to people on the list', 'they need updates'), ('Raise money without a plan', 'not required'),
          'Promises must match realistic building time.'),
    ]),
    F2=sec('Handle the complications: why the demo tactic may fail', DBX, [
        Q('A founder\'s product is hard to show in a short video (for example, a new kind of accounting method). What is '
          'a sensible adaptation?', 'Use a different test, such as a simple trial with a few customers',
          ('Make a confusing video anyway', 'unlikely to test interest fairly'), ('Skip testing entirely', 'no evidence'),
          ('Copy Dropbox\'s video style exactly, scene by scene, for the method', 'style does not fix the fit'),
          'When a demo does not fit, choose a test that does.'),
        Q('A demo video went viral, but most viewers were outside the countries the founder can serve. What should she '
          'check?', 'How many sign-ups come from customers she can actually serve', ('The total view count only', 'misleading'),
          ('The number of likes', 'attention only'), ('Which country liked the video the most, judging by comments', 'not the key question'),
          'Only reachable customers count toward real demand.'),
        Q('A founder copies the demo approach but has no clear problem to show. What is the likely result?',
          'Few people will care, because the demo shows no clear benefit.', ('Huge numbers of sign-ups, because demo videos always work well', 'no guarantee'),
          ('Payment from everyone who watches', 'unlikely'), ('A guaranteed investor offer', 'no'),
          'A demo works only if it shows a real problem being solved.'),
        Q('Which statement correctly separates history from interpretation?',
          'The video and waiting list are documented; "demos test interest" is a lesson drawn.',
          ('Both are quotes from the founder.', 'the lesson is the course\'s interpretation'),
          ('Neither is documented.', 'the video is documented'),
          ('The exact number of sign-ups is documented and agreed on by every source.', 'sources disagree'),
          'Documented facts versus the course\'s interpretation.'),
        Q('A waiting list has 2,000 people. Past launches in this field turned about 3 percent of a list into paying '
          'customers. About how many paying customers might the founder expect?', 'About 60',
          ('About 2,000', 'that assumes everyone pays'), ('About 600', 'that uses 30 percent'),
          ('About 6', 'that uses 0.3 percent'), '3 percent of 2,000 is 60.', calc=lambda: 2000 * 3 / 100 == 60),
    ]))

SETS = [s15, s16, s17, s18]
