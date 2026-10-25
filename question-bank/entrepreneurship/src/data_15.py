"""Entrepreneurship sets 85-90: Foundation 11, marketing basics and honest promotion. Names are fictional."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 85: choosing a channel
CHAN = ('A MARKETING CHANNEL is a way of reaching customers: a social media platform, email, local flyers, a market '
        'stall, search, word of mouth, or partnerships with other businesses. Choose a channel by asking: Where do my '
        'target customers already spend time? What can I keep doing every week with my time and budget? Can I measure '
        'results? Starting with one or two channels done well usually beats a little effort on seven. A channel that '
        'works for one business may not work for another.')

s85 = SET('ENT.MKT.01',
    M=sec('Choose a marketing channel by customers, effort and measurability', CHAN, [
        Q('What is a marketing channel?', 'A way of reaching customers',
          ('A television station the business must own itself', 'too narrow'),
          ('The bank account where sales are deposited', 'not marketing'),
          ('A legal filing that registers the brand name', 'not marketing'), 'Channels reach people.'),
        Q('What is the first question when choosing a channel?', 'Where do my target customers already spend time?',
          ('Which channel do celebrities use most often?', 'not your customers'),
          ('Which channel has the most colorful logo?', 'irrelevant'),
          ('Which channel did a friend\'s different business use?', 'may not fit'), 'Go where customers are.'),
        Q('Why start with one or two channels?', 'Doing a few well usually beats spreading thin',
          ('Because using more than two channels is illegal', 'not true'),
          ('Because one channel always reaches every customer', 'not true'),
          ('Because measuring results is never useful', 'opposite'), 'Focus helps consistency.'),
        Q('Which is a reason to prefer a channel?', 'Results can be measured', ('It is popular with people outside your market', 'wrong audience'),
          ('It needs more time than the owner has', 'unsustainable'), ('Nobody in the target market uses it', 'wrong audience'),
          'Measurement shows what works.'),
        Q('A channel worked great for a gym. Will it work for a bookkeeping service?', 'Not necessarily; customers differ',
          ('Yes, every channel works the same for all businesses', 'not true'),
          ('Yes, if the bookkeeper copies the gym\'s logo', 'irrelevant'),
          ('No, bookkeepers can never market at all', 'not true'), 'Fit depends on the audience.'),
    ]),
    B=[cs('Fishing where the fish are', 'An old saying goes, "Fish where the fish are." A fancy rod is useless in an empty '
          'pond. Marketing channels work the same way: the best channel is where your particular customers already '
          'gather, not the newest or most famous one. And just as a person can only watch so many fishing lines, an owner '
          'can only keep up a few channels well.', [
        Q('"Fish where the fish are" means what for marketing?', 'Reach customers where they already are', ('Buy the fanciest tools', 'not the point'),
          ('Market everywhere at once, on every app', 'not the point'), ('Avoid all customers', 'opposite'), 'Go to your audience.'),
        Q('A fancy rod in an empty pond is like what?', 'A great ad on a channel your customers never use', ('A good plan', 'no'),
          ('A shop that is already full of eager customers', 'no'), ('A big sale', 'no'), 'Tools do not help without the audience.'),
        Q('Why watch only a few fishing lines?', 'One person can only keep up a few well', ('More lines always catch nothing at all', 'no'),
          ('Lines are expensive', 'not the point'), ('Fish dislike lines', 'no'), 'Limited time and attention.'),
        Q('The "pond" stands for what?', 'A marketing channel', ('A bank', 'no'), ('A product on sale', 'no'), ('A tax', 'no'),
          'Where you look for customers.'),
        Q('The "fish" stand for what?', 'Your target customers', ('Your nearby competitors', 'no'), ('Your suppliers', 'no'),
          ('Your taxes', 'no'), 'The people you want to reach.'),
    ], why='A learner who misses MAIN may chase popular channels; fishing where the fish are explains fit.')],
    F1=sec('Apply it: pick channels for real businesses', CHAN, [
        Q('A mobile pet groomer serves one town. Owners are mostly local families. Which first channel fits best?',
          'Local community groups and flyers at vet offices', ('A national TV advertisement', 'too broad and costly'),
          ('A podcast for software engineers worldwide', 'wrong audience'), ('Billboards in another state', 'wrong place'),
          'Local reach for a local service.'),
        Q('A freelancer can spend 3 hours a week on marketing. Which plan is most realistic?', 'One channel done consistently each week',
          ('Seven channels, posting daily on each', 'unsustainable'), ('No marketing until she has more time', 'no reach'),
          ('A new channel every week', 'inconsistent'), 'Match effort to available time.'),
        Q('Flyers cost 60 dollars and brought 3 clients. Online posts took 5 hours and brought 6 clients. Which brought more '
          'clients?', 'Online posts, with 6', ('Flyers, with 3', 'fewer'), ('They brought the same', 'they differ'),
          ('Neither brought any', 'both did'), '6 > 3.', calc=lambda: 6 > 3),
        Q('Flyers cost 60 dollars and brought 3 clients. What was the flyer cost per client?',
          '20 dollars',
          ('60 dollars', 'total'), ('3 dollars', 'count'),
          ('180 dollars', 'multiplied'),
          '60 / 3 = 20.',
          calc=lambda: 60 / 3 == 20),
        Q('A seller of business software for dentists is choosing a channel. Which fits best?', 'A dental trade newsletter or association',
          ('A teen gaming forum', 'wrong audience'), ('A local playground bulletin board for parents', 'wrong audience'),
          ('A cooking video channel', 'wrong audience'), 'Reach dentists where they gather.'),
    ]),
    F2=sec('Handle the complications: hype and changing channels', CHAN, [
        Q('A new app is very popular, but the owner\'s customers are mostly over 60 and do not use it. What should she do?',
          'Stay with channels her customers actually use', ('Move all her marketing to the new app right now', 'wrong audience'),
          ('Stop marketing entirely', 'no reach'), ('Copy a teen influencer\'s style', 'mismatch'), 'Audience fit beats hype.'),
        Q('A channel brought customers last year but results have fallen for 6 months. What is a sensible step?', 'Test another channel while measuring both',
          ('Keep doing exactly the same thing without measuring', 'ignores evidence'), ('Quit all marketing', 'no reach'),
          ('Double spending on the falling channel immediately', 'untested'), 'Test and measure.'),
        Q('An owner cannot tell which channel brought new customers. What would help?', 'Asking new customers how they heard about the business',
          ('Guessing based on feelings', 'unreliable'), ('Stopping all channels at once to see what changes', 'loses reach'),
          ('Ignoring the question', 'no learning'), 'Simple tracking helps.'),
        Q('Two channels each cost 100 dollars a month. A brings 10 customers, B brings 4. Ignoring other factors, which is cheaper '
          'per customer?', 'A, at 10 dollars per customer', ('B, at 25 dollars per customer', 'B is higher'),
          ('They are equal', 'they differ'), ('A, at 100 dollars per customer', 'not divided'), 'A: 10; B: 25.',
          calc=lambda: 100 / 10 == 10 and 100 / 4 == 25),
        Q('Which statement is accurate?', 'The best channel depends on the customers and the owner\'s capacity.',
          ('One channel is always best for every kind of business everywhere.', 'not true'), ('More channels always mean more sales.', 'not always'),
          ('Measuring channels is a waste of time.', 'not true'), 'Fit and focus matter.'),
    ]))

# ------------------------------------------------------------------ Set 86: useful content and a next step
CONT = ('Useful marketing content helps the reader before asking for anything: a short tip, an answer to a common '
        'question, a before-and-after photo of real work, or a simple how-to. Each piece should end with one clear NEXT '
        'STEP, such as "Book a call" or "See this week\'s menu." Write for one type of reader, use plain words, and be '
        'specific. "5 ways to keep your houseplants alive in winter" is more useful than "We love plants!"')

s86 = SET('ENT.MKT.02',
    M=sec('Create useful content with a single next step', CONT, [
        Q('What makes content useful?', 'It helps the reader before asking for anything',
          ('It repeats "buy now" as many times as possible', 'pushy'),
          ('It talks only about how great the owner is', 'self-focused'),
          ('It uses as many complicated words as possible', 'unclear'), 'Value first.'),
        Q('Which post is more useful?', '"5 ways to keep houseplants alive in winter"', ('"We love plants so much!"', 'vague'),
          ('"Buy plants. Buy plants. Buy plants."', 'pushy'), ('"Plants are cool, right?"', 'vague'), 'Specific help.'),
        Q('What should each piece of content end with?', 'One clear next step', ('Five unrelated links to choose from', 'confusing'),
          ('No next step at all', 'no direction'), ('A long legal disclaimer only', 'not a next step'), 'Guide the reader.'),
        Q('Who should content be written for?', 'One type of reader', ('Every person on earth at once', 'too broad'),
          ('Only the owner\'s family members', 'too narrow'), ('Competitors only', 'wrong audience'), 'Specific audience.'),
        Q('Which is a clear next step?', '"See this week\'s menu"', ('"Stuff and things"', 'vague'), ('"Maybe check something"', 'vague'),
          ('"Click"', 'unclear'), 'Plain and specific.'),
    ]),
    B=[cs('A helpful neighbor', 'Think of a neighbor who knows a lot about gardening. She shares tips freely, and when you need a '
          'garden designed, you think of her first. Useful content works the same way: you help people with small, '
          'specific tips, and they remember you. At the end, you mention one simple way to work with you, not ten.', [
        Q('Why do people think of the helpful neighbor first?', 'She has helped them before', ('She shouts the loudest', 'no'),
          ('She is the cheapest', 'not stated'), ('She hides her skills', 'no'), 'Help builds trust.'),
        Q('Her free tips are like what?', 'Useful content', ('Ads with no information', 'no'), ('Taxes', 'no'), ('Invoices', 'no'),
          'Value before asking.'),
        Q('Mentioning one simple way to work with her is like what?', 'A clear next step', ('Ten different offers', 'too many'),
          ('No offer at all', 'missed chance'), ('A secret', 'no'), 'One next step.'),
        Q('Are her tips vague or specific?', 'Specific', ('Vague', 'no'), ('Secret', 'no'), ('Random ones', 'no'), 'Specific tips help.'),
        Q('What does the neighbor avoid?', 'Pushing ten offers at once', ('Sharing tips', 'she shares'), ('Helping people', 'she helps'),
          ('Being remembered by anyone', 'she is'), 'Keep the ask simple.'),
    ], why='A learner who misses MAIN may see marketing as only selling; a helpful neighbor shows value first.')],
    F1=sec('Apply it: improve a post', CONT, [
        Q('A bakery posts "Best bakery ever!!!" with no details. Which rewrite is more useful?', '"How to keep sourdough fresh for 3 days. Order Friday\'s loaves here."',
          ('"Best bakery ever, really, truly, the very best in the whole town!!!"', 'still vague'), ('"Bread."', 'empty'),
          ('"Follow us for no reason at all."', 'no value'), 'Useful tip plus one step.'),
        Q('A post ends with links to the shop, blog, newsletter, survey and careers page. What should change?', 'Choose the one most important next step',
          ('Add five more links', 'more clutter'), ('Remove every link', 'no direction'), ('Make all the links blinking and bright', 'distracting'),
          'One clear action.'),
        Q('A tutor\'s readers are parents of 7th graders. Which topic fits best?', '"3 signs your 7th grader needs math help"',
          ('"Advanced calculus proofs for researchers"', 'wrong audience'), ('"Our office furniture choices"', 'irrelevant'),
          ('"Why we love our logo"', 'self-focused'), 'Write for the reader.'),
        Q('A post got 400 views and 12 people clicked "Book a call." What percent clicked?', '3 percent', ('12 percent', 'count'),
          ('33 percent', 'reversed'), ('0.3 percent', 'moved decimal'), '12 / 400 = 0.03.', calc=lambda: 12 / 400 == 0.03),
        Q('Which detail makes content more believable?', 'A real before-and-after photo of the owner\'s work', ('A stock photo of a stranger\'s work labeled as her own', 'misleading'),
          ('A made-up statistic', 'false'), ('An unrelated celebrity photo', 'irrelevant'), 'Real examples build trust.'),
    ]),
    F2=sec('Handle the complications: pressure to post constantly', CONT, [
        Q('An owner posts 5 times a day but each post is filler. What might help more?', 'Fewer, more useful posts',
          ('Posting 10 times a day instead', 'more filler'), ('Stopping all posts forever', 'no reach'),
          ('Copying competitors\' posts word for word', 'not original'), 'Quality over quantity.'),
        Q('A how-to post gives advice that could be unsafe if followed wrongly. What should the owner do?', 'Add clear safety notes or recommend a professional where needed',
          ('Post it without any warnings, since readers are adults', 'risky'), ('Exaggerate the benefits', 'misleading'), ('Delete all content', 'overreaction'),
          'Responsible content.'),
        Q('Posts with tips get 30 clicks each; pure ads get 5. How many more clicks do 4 tip posts bring than 4 ads?', '100',
          ('25', 'one post difference'), ('120', 'tip total'), ('20', 'ad total'), '4 x 30 - 4 x 5 = 100.', calc=lambda: 4 * 30 - 4 * 5 == 100),
        Q('A competitor\'s post is very popular. The owner wants to copy it word for word. What is the problem?', 'Copying can violate rights and is not original',
          ('No problem; posts are always free to copy', 'not true'), ('Copying guarantees more clicks', 'not guaranteed'),
          ('It improves search results', 'not usually'), 'Create original content.'),
        Q('Which statement is accurate?', 'Useful, specific content with one next step tends to work better than vague hype.',
          ('Vague hype always beats specific help.', 'not usually'), ('Content should never include a next step, because readers dislike being asked.', 'it should'),
          ('More posts always mean more sales.', 'not always'), 'Value and clarity.'),
    ]))

# ------------------------------------------------------------------ Set 87: email lists, permission, unsubscribing
EMAIL = ('An EMAIL LIST lets you contact people who asked to hear from you. Build it with PERMISSION: a sign-up form '
         'where people choose to join. Under the US CAN-SPAM Act, commercial emails must not use misleading headers or '
         'subject lines, must tell recipients how to opt out, must honor opt-out requests, and must include a valid '
         'physical postal address (which can be a registered PO Box or private mailbox). The rules cover '
         'business-to-business email too. Buying lists of strangers\' addresses damages trust and deliverability.')

s87 = SET('ENT.MKT.03',
    M=sec('Build an email list with permission and follow opt-out rules', EMAIL, [
        Q('How should an email list be built?', 'With permission, through a sign-up form',
          ('By buying a list of strangers\' addresses online', 'no permission'),
          ('By copying addresses from other companies\' websites', 'no permission'),
          ('By guessing addresses at popular email providers', 'no permission'), 'People choose to join.'),
        Q('What must a commercial email tell recipients?', 'How to opt out', ('The owner\'s home phone number', 'not required'),
          ('The owner\'s favorite products', 'not required'), ('The business\'s bank balance', 'not required'),
          'Opt-out information is required.'),
        Q('Which address may be used as the required postal address?', 'A registered PO Box or private mailbox',
          ('Only a made-up address that sounds official', 'must be valid'), ('An email address instead of a postal one', 'not postal'),
          ('No address is ever needed', 'required'), 'A valid physical postal address is required.'),
        Q('Do the rules cover emails sent to other businesses?', 'Yes', ('No, only emails to consumers', 'covers B2B too'),
          ('Only on weekends', 'no'), ('Only for large companies', 'no'), 'Business-to-business email is covered.'),
        Q('Which subject line is NOT allowed?', 'A misleading one, like "Re: your order" when there was no order',
          ('"Spring sale: 20 percent off all planters and pots this weekend"', 'accurate'), ('"New class dates for May"', 'accurate'),
          ('"Our monthly gardening tips"', 'accurate'), 'Subject lines must not mislead.'),
    ]),
    B=[cs('Invited guests versus gate-crashers', 'Think of a party. People you invited are glad to come. People who show up '
          'uninvited annoy everyone. An email list is your guest list: people who said "yes, invite me." When a guest says '
          '"please stop inviting me," you take them off the list. Sending emails to people who never signed up is like '
          'inviting gate-crashers.', [
        Q('An email list is like what?', 'A guest list of people who said yes', ('A list of strangers\' addresses', 'no permission'),
          ('A phone book', 'no permission'), ('A shopping list', 'unrelated'), 'Permission-based.'),
        Q('A guest saying "please stop inviting me" is like what?', 'An unsubscribe request', ('A new sign-up', 'opposite'),
          ('A purchase', 'no'), ('A complaint about food', 'no'), 'Opt-out.'),
        Q('What should you do when a guest asks to stop?', 'Take them off the list', ('Invite them twice as often', 'no'),
          ('Ignore them', 'no'), ('Sell their name', 'no'), 'Honor opt-outs.'),
        Q('Emailing people who never signed up is like what?', 'Inviting gate-crashers', ('Inviting friends', 'they agreed'),
          ('Sending thank-you notes', 'no'), ('Paying bills', 'no'), 'No permission.'),
        Q('Who is glad to come to the party?', 'People you invited who said yes', ('Strangers', 'no'), ('Nobody', 'no'),
          ('Competitors from across town', 'no'), 'Permission makes a welcome audience.'),
    ], why='A learner who misses MAIN may not see why permission matters; a party guest list makes it concrete.')],
    F1=sec('Apply it: check an email campaign', EMAIL, [
        Q('Mei\'s newsletter has no unsubscribe link. What should she add?', 'A clear way to opt out', ('A bigger logo', 'not required'),
          ('More product photos', 'not required'), ('A countdown timer', 'not required'), 'Opt-out is required.'),
        Q('An owner wants privacy and does not want her home address in emails. What option fits the rule?', 'Use a registered PO Box or private mailbox',
          ('Leave out any postal address in the email', 'required'), ('Use a fake address', 'must be valid'), ('Use only a phone number', 'not postal'),
          'A valid mailbox address works.'),
        Q('A list has 800 subscribers. 16 unsubscribe after one email. What percent unsubscribed?', '2 percent', ('16 percent', 'count'),
          ('50 percent', 'misdivided'), ('0.2 percent', 'moved decimal'), '16 / 800 = 0.02.', calc=lambda: 16 / 800 == 0.02),
        Q('A vendor offers 10,000 email addresses for 50 dollars. What is the main problem?', 'Those people never gave permission',
          ('The price is too low to be worth it', 'not the main problem'), ('10,000 is too few', 'not the issue'), ('Nothing at all', 'permission matters'),
          'Bought lists lack consent.'),
        Q('Which subject line is honest for a sale email?', '"Weekend sale: 15 percent off all candles"', ('"Your account is suspended"', 'misleading'),
          ('"Re: our meeting yesterday about your account"', 'misleading'), ('"Urgent tax notice"', 'misleading'), 'Accurate subject.'),
    ]),
    F2=sec('Handle the complications: old lists and ignored requests', EMAIL, [
        Q('Someone unsubscribed but still gets emails because the owner forgot to update the list. What should she do?',
          'Remove them promptly and fix the process', ('Keep emailing them anyway', 'violates opt-out'),
          ('Ask them to unsubscribe again later', 'burden'), ('Move them to a second list', 'still emailing'), 'Honor opt-outs.'),
        Q('An owner collected business cards at a fair and wants to add everyone to her newsletter. What is the better approach?',
          'Send one message inviting them to join, or ask permission first', ('Add them all silently', 'no consent'),
          ('Sell the list of card addresses to other businesses at the fair', 'harmful'), ('Never contact them', 'missed chance'), 'Ask permission.'),
        Q('An email\'s "From" name says a famous company the owner does not represent. What rule does this break?', 'Headers must not be misleading',
          ('No rule; any name is fine', 'misleading'), ('Only the color rule', 'no such rule'), ('Only the image size rule', 'no such rule'),
          'Honest headers.'),
        Q('A list of 1,000 had 300 sign-ups from a contest with unrelated prizes; few read emails. What might improve results?',
          'Focus on people who joined for the actual topic', ('Run even bigger contests with unrelated prizes', 'same problem'),
          ('Buy more addresses', 'no consent'), ('Email 5 times a day', 'more unsubscribes'), 'Relevant subscribers.'),
        Q('Which statement is accurate?', 'Permission, honest subject lines and working opt-outs are basic email duties.',
          ('Emails sent to other businesses are exempt from all of these rules.', 'covered'), ('An address is never required.', 'required'),
          ('Buying lists is the best way to grow.', 'harms trust'), 'Follow the rules.'),
    ]))

# ------------------------------------------------------------------ Set 88: local outreach, referrals and networking
LOCAL = ('Local businesses often grow through people. LOCAL OUTREACH means showing up where customers are: farmers '
         'markets, community events, partnerships with nearby businesses. REFERRALS are recommendations from happy '
         'customers; you can ask for them directly and make it easy ("Tell a friend; you both get 10 percent off"). '
         'NETWORKING means building real relationships with people who serve the same customers, like a wedding '
         'photographer and a florist. Follow up, keep promises, and give before you ask.')

s88 = SET('ENT.MKT.04',
    M=sec('Grow through local outreach, referrals and networking', LOCAL, [
        Q('What is a referral?', 'A recommendation from a happy customer', ('A paid ad on a billboard', 'not a referral'),
          ('A tax form sent to the state', 'not a referral'), ('A discount the owner gives only to herself', 'not a referral'),
          'Customers recommend you.'),
        Q('Which partnership makes sense?', 'A wedding photographer and a florist', ('A plumber and a video game studio', 'different customers'),
          ('A dentist and a tire shop', 'little overlap'), ('A bakery and a car wash in another state', 'no overlap'),
          'They serve the same customers.'),
        Q('How can an owner make referrals easier?', 'Ask directly and offer a simple reward for both people',
          ('Never mention referrals to anyone', 'no request'), ('Require a long form to refer a friend', 'friction'),
          ('Only accept referrals sent by mailed letter to the shop', 'friction'), 'Simple and direct.'),
        Q('What does "give before you ask" mean in networking?', 'Help others first', ('Ask for favors immediately', 'opposite'),
          ('Never help anyone', 'opposite'), ('Give away all products free forever', 'too extreme'), 'Build goodwill.'),
        Q('Which is local outreach?', 'A stall at the farmers market', ('An email to a bought list', 'not outreach'),
          ('A secret social media account', 'not outreach'), ('Hiding the shop address', 'opposite'), 'Show up where customers are.'),
    ]),
    B=[cs('A good restaurant tip from a friend', 'If a friend says, "Try the pasta at Luca\'s, it\'s great," you are more likely '
          'to go than if you saw an ad. That is a referral. Now imagine Luca\'s gives your friend and you a free dessert '
          'for the recommendation: that is a referral reward. And if Luca\'s chef is friends with the wine shop next door, '
          'they send customers to each other: that is networking.', [
        Q('A friend recommending Luca\'s is like what?', 'A referral', ('A billboard', 'an ad'), ('A tax', 'no'), ('A recipe', 'no'),
          'A personal recommendation.'),
        Q('The free dessert is like what?', 'A referral reward', ('A refund of the meal', 'no'), ('A fine', 'no'), ('A tax', 'no'),
          'A thank-you for referring.'),
        Q('The chef and wine shop sending customers to each other is like what?', 'Networking', ('Competing', 'no'), ('Advertising on TV', 'no'),
          ('Ignoring each other', 'no'), 'Mutual relationships.'),
        Q('Why do people trust a friend\'s tip more than an ad?', 'They trust the friend', ('Ads are illegal', 'no'),
          ('Friends are paid actors', 'no'), ('Ads cost nothing', 'no'), 'Trust transfers.'),
        Q('Who benefits from the wine shop partnership?', 'Both businesses', ('Only the chef', 'both'), ('Neither', 'both'),
          ('Only the customer', 'both businesses too'), 'Partnerships are mutual.'),
    ], why='A learner who misses MAIN may not see how people-based growth works; a restaurant tip from a friend is familiar.')],
    F1=sec('Apply it: plan people-based marketing', LOCAL, [
        Q('A new house cleaner has 10 happy clients. Which first step uses referrals well?', 'Ask each client to tell a friend, with 10 percent off for both',
          ('Wait quietly and hope clients mention her to friends someday', 'passive'), ('Buy a national TV ad', 'costly'),
          ('Ask clients to write fake reviews', 'dishonest'), 'Ask directly with a simple reward.'),
        Q('A referral reward gives 10 percent off a 120-dollar cleaning to both people. What is the total discount given?', '24 dollars',
          ('12 dollars', 'one person'), ('120 dollars', 'full price'), ('10 dollars', 'percent as dollars'), '2 x 12 = 24.',
          calc=lambda: 2 * 0.10 * 120 == 24),
        Q('If that referral brings a client who books 10 cleanings a year at 120 dollars, what is the yearly revenue from that client?',
          '1,200 dollars', ('120 dollars', 'one cleaning'), ('24 dollars', 'discount'), ('12,000 dollars', 'extra zero'),
          '10 x 120 = 1,200.', calc=lambda: 10 * 120 == 1200),
        Q('A photographer meets a florist at a networking event. Which follow-up builds the relationship?', 'Send a short note and share one of the florist\'s posts',
          ('Never contact the florist again', 'no relationship'), ('Ask for 20 referrals immediately', 'too soon'),
          ('Criticize the florist\'s work publicly to look more expert', 'harmful'), 'Give first and follow up.'),
        Q('A booth at a market costs 50 dollars and brings 5 new customers. What is the cost per customer?', '10 dollars',
          ('50 dollars', 'total'), ('5 dollars', 'count'), ('250 dollars', 'multiplied'), '50 / 5 = 10.', calc=lambda: 50 / 5 == 10),
    ]),
    F2=sec('Handle the complications: one-sided partners and broken promises', LOCAL, [
        Q('A partner business receives many referrals from the owner but never sends any back. What is a sensible step?',
          'Talk openly about how the partnership can work for both', ('Keep sending referrals forever without saying anything', 'one-sided'),
          ('Post complaints about them online', 'harmful'), ('Start sending fake referrals', 'dishonest'), 'Honest conversation.'),
        Q('An owner promised a free consultation to anyone she met at an event, then forgot. What is the risk?', 'Broken promises damage trust and referrals',
          ('No risk, because people at events forget too', 'trust suffers'), ('It increases demand', 'no'), ('It lowers taxes', 'no'),
          'Keep promises.'),
        Q('A referral program pays 50 dollars per referral, but most referred people buy a 40-dollar item once. What is the problem?',
          'Each referral costs more than it brings in', ('Nothing, because referral rewards always pay off', 'not here'),
          ('The reward is too small', 'opposite'), ('Customers buy too much', 'opposite'), '50 > 40.', calc=lambda: 50 > 40),
        Q('A networking group requires paid membership, but members serve very different customers. What should the owner weigh?',
          'Whether the members connect to her customers', ('Only the group\'s logo', 'irrelevant'), ('Only the meeting snacks', 'irrelevant'),
          ('Nothing, because all networking groups help equally', 'not true'), 'Relevance matters.'),
        Q('Which statement is accurate?', 'Referrals and partnerships work best when both sides benefit and promises are kept.',
          ('Referrals only come from paid ads.', 'not true'), ('Networking means asking new contacts for favors immediately after meeting.', 'not true'),
          ('Local marketing never works online.', 'irrelevant'), 'Mutual benefit and trust.'),
    ]))

# ------------------------------------------------------------------ Set 89: testimonials and reviews with permission
REV = ('Reviews and testimonials are powerful because they come from customers, so they must be REAL. Ask customers for '
       'permission before quoting them, use their actual words (fixing only small typos), and do not show a review as '
       'typical if it is not. Never write fake reviews, pay for positive reviews, or use AI to invent customer '
       'experiences; the FTC treats fake reviews and testimonials as deceptive. Respond calmly and helpfully to negative '
       'reviews; do not threaten or pay reviewers to remove them.')

s89 = SET('ENT.MKT.05',
    M=sec('Use real reviews with permission and avoid fake ones', REV, [
        Q('What should an owner do before quoting a customer on the website?', 'Ask the customer for permission',
          ('Quote them without asking, since the review is public', 'ask first'),
          ('Change their words to sound more exciting', 'not their words'),
          ('Make up a name to protect privacy and add details', 'invented'), 'Permission first.'),
        Q('Which is deceptive?', 'Writing reviews under made-up customer names', ('Quoting a real customer with permission', 'honest'),
          ('Fixing a small typo in a real review', 'acceptable'), ('Replying politely to a negative review', 'honest'),
          'Fake reviews deceive.'),
        Q('Can AI be used to invent customer reviews?', 'No, invented experiences are deceptive', ('Yes, if they sound realistic', 'still fake'),
          ('Yes, if only positive ones are written', 'still fake'), ('Yes, for small businesses only', 'still fake'),
          'Reviews must reflect real experiences.'),
        Q('How should an owner respond to a negative review?', 'Calmly and helpfully', ('By threatening the reviewer', 'harmful'),
          ('By paying them to remove it', 'improper'), ('By posting their private details', 'harmful'), 'Respond professionally.'),
        Q('A review describes results most customers do not get. What should the owner avoid?', 'Presenting it as typical',
          ('Reading it carefully', 'fine'), ('Thanking the reviewer', 'fine'), ('Keeping it on file', 'fine'), 'Do not mislead about typical results.'),
    ]),
    B=[cs('A reference letter', 'When you apply for a job, a teacher might write a reference letter. It is valuable because it '
          'comes from someone else who knows your work. If you wrote the letter yourself and signed the teacher\'s name, it '
          'would be fake and could get you in serious trouble. Reviews are reference letters for a business: valuable only '
          'when they really come from customers.', [
        Q('Why is a reference letter valuable?', 'It comes from someone who knows your work', ('You wrote it', 'that would be fake'),
          ('It is long', 'not the reason'), ('It is printed on thick, colorful paper', 'no'), 'Independent source.'),
        Q('Writing your own letter and signing the teacher\'s name is like what?', 'A fake review', ('A real review', 'no'),
          ('A thank-you note', 'no'), ('A receipt', 'no'), 'Faked endorsement.'),
        Q('A business review is like what?', 'A reference letter from a customer', ('A tax return filed by the owner', 'no'), ('A logo', 'no'),
          ('An invoice', 'no'), 'Third-party endorsement.'),
        Q('When are reviews valuable?', 'When they really come from customers', ('When the owner writes them herself', 'fake'),
          ('When they are bought', 'fake'), ('When AI invents them', 'fake'), 'Authenticity.'),
        Q('What could happen with a faked letter?', 'Serious trouble', ('A job promotion', 'no'), ('Nothing', 'risky'), ('A gift', 'no'),
          'Deception has consequences.'),
    ], why='A learner who misses MAIN may not see why reviews must be real; a reference letter makes it familiar.')],
    F1=sec('Apply it: handle reviews honestly', REV, [
        Q('A friend offers to post five 5-star reviews for an owner\'s new café that she has never visited. What should the owner do?',
          'Decline, because those reviews would not reflect real experiences', ('Accept, because friends are allowed to help a new business look popular', 'still fake'),
          ('Accept, but only three reviews', 'still fake'), ('Ask her to use different names', 'more deceptive'), 'Reviews must be genuine.'),
        Q('A customer emails praise. Which next step is right before posting it?', 'Ask permission and use her actual words',
          ('Post it with a fake name', 'altered'), ('Rewrite it to add more praise', 'altered'), ('Post her phone number and email with it', 'privacy'),
          'Permission and accuracy.'),
        Q('A shop has 40 reviews averaging 4.5 stars. After asking all recent customers, it gets 10 more 3-star reviews. What is the new '
          'average?', '4.2 stars', ('4.5 stars', 'unchanged'), ('3.75 stars', 'simple average'), ('3.0 stars', 'only new'),
          '(40 x 4.5 + 10 x 3) / 50 = 210 / 50 = 4.2.', calc=lambda: (40 * 4.5 + 10 * 3) / 50 == 4.2),
        Q('A negative review says an order arrived late. Which reply is best?', '"Sorry about the delay. Please email us so we can make it right."',
          ('"You\'re lying and we will sue you."', 'threatening'), ('"Delete this review now or we will post your home address online."', 'harmful'),
          ('No reply, then pay someone to bury it', 'improper'), 'Calm and helpful.'),
        Q('Which practice is honest?', 'Asking every customer for a review, not just happy ones', ('Asking only the customers who seem likely to give 5 stars', 'skewed'),
          ('Hiding all negative reviews', 'misleading'), ('Offering money only for positive reviews', 'improper'), 'Fair request.'),
    ]),
    F2=sec('Handle the complications: incentives and edited quotes', REV, [
        Q('An owner offers a discount for leaving a review "of any kind." What should the review show to stay honest?', 'That the reviewer received an incentive',
          ('Nothing; incentives never need mention', 'disclose'), ('Only positive reviews should be accepted', 'skewed'),
          ('The reviewer\'s home address', 'privacy'), 'Disclose material connections.'),
        Q('A testimonial says "I lost 30 pounds in a week" for a supplement. What is the concern?', 'It may suggest unrealistic results as typical',
          ('No concern, because any real customer quote is fine to use', 'misleading'), ('It is too short', 'not the issue'), ('It lacks emojis', 'irrelevant'),
          'Unusual results should not be presented as typical.'),
        Q('An agency offers to "remove bad reviews" by flooding the page with fake positive ones. What should the owner do?',
          'Refuse, because fake reviews are deceptive', ('Accept the offer, since everyone else does it', 'deceptive'),
          ('Accept for a short time', 'still deceptive'), ('Ask for fewer fake reviews', 'still fake'), 'Stay honest.'),
        Q('A customer approved a quote but later asks to withdraw it. What should the owner do?', 'Remove it',
          ('Keep it, since permission was given once', 'respect withdrawal'), ('Post it twice', 'no'), ('Edit it to be anonymous without asking', 'ask first'),
          'Respect the customer\'s choice.'),
        Q('Which statement is accurate?', 'Reviews and testimonials must reflect real customers\' honest experiences.',
          ('AI-written reviews are fine if realistic.', 'deceptive'), ('Paying for positive reviews is normal.', 'improper'),
          ('Negative reviews should be threatened away or paid off quickly.', 'harmful'), 'Authenticity and honesty.'),
    ]))

# ------------------------------------------------------------------ Set 90: disclosing sponsorships and affiliate links
DISC = ('If someone promoting a product has a MATERIAL CONNECTION to the business (they were paid, given free products, '
        'or earn a commission), that connection should be DISCLOSED clearly. An AFFILIATE LINK pays the promoter a '
        'commission when someone buys. Clear disclosures are short, plain and placed where people will see them before '
        'clicking or buying, such as "Ad," "Sponsored," or "I earn a commission if you buy." A platform\'s built-in '
        'disclosure tool is not automatically enough. Businesses should tell the people promoting them to disclose.')

s90 = SET('ENT.MKT.06',
    M=sec('Disclose sponsorships and affiliate links clearly', DISC, [
        Q('What is a material connection?', 'A payment, free product or commission tied to the promotion',
          ('A friendship with no money or gifts involved at all', 'not this meaning'),
          ('The material a product is made from', 'pun'), ('A broken internet connection', 'not this meaning'),
          'A connection that could affect trust.'),
        Q('What is an affiliate link?', 'A link that pays the promoter a commission on purchases',
          ('A link to the business\'s own privacy policy page', 'not affiliate'),
          ('A broken link that leads nowhere', 'not affiliate'), ('A link to a government website', 'not affiliate'),
          'Commission-paying link.'),
        Q('Where should a disclosure appear?', 'Where people will see it before clicking or buying',
          ('At the very bottom after 40 hashtags', 'hard to see'), ('Only on a separate page that nobody visits', 'hard to see'),
          ('Nowhere, if the post is short', 'still needed'), 'Clear and noticeable.'),
        Q('Is a platform\'s built-in disclosure tool always enough?', 'Not automatically', ('Yes, it always replaces any other disclosure', 'not automatically'),
          ('Yes, if the post has a photo', 'irrelevant'), ('No, disclosures are banned', 'not true'), 'Check that it is clear.'),
        Q('Which disclosure is clearest?', '"I earn a commission if you buy through this link."', ('"#sp #collab #thx"', 'unclear'),
          ('"Thanks to my friends at the shop for everything!"', 'unclear'), ('No disclosure at all', 'missing'), 'Plain words.'),
    ]),
    B=[cs('A friend who earns money from the recommendation', 'If a friend recommends a phone and you later learn the store paid '
          'her for every phone she helped sell, you might feel misled. It does not mean the phone is bad; you just would '
          'have wanted to know. Disclosures tell people about the connection up front, so they can decide how much weight to '
          'give the recommendation.', [
        Q('Why might you feel misled?', 'You did not know she was paid', ('The phone she chose was free', 'no'), ('She was rude', 'not stated'),
          ('The store closed', 'no'), 'Hidden connection.'),
        Q('Does a paid recommendation mean the product is bad?', 'No, not necessarily', ('Yes, always', 'not necessarily'),
          ('Only for phones', 'no'), ('Only on weekends', 'no'), 'Disclosure is about trust, not quality.'),
        Q('What does a disclosure let people do?', 'Decide how much weight to give the recommendation', ('Buy without thinking', 'no'),
          ('Get a refund automatically from the store later', 'no'), ('Ignore all ads', 'no'), 'Informed choice.'),
        Q('When should people learn about the connection?', 'Up front', ('After buying', 'too late'), ('Never', 'no'),
          ('Only if they ask', 'not enough'), 'Before deciding.'),
        Q('The store paying the friend is like what?', 'A material connection', ('A tax', 'no'), ('A refund of the meal', 'no'), ('A paper coupon', 'no'),
          'Payment tied to the promotion.'),
    ], why='A learner who misses MAIN may not see why disclosure matters; a friend paid for a recommendation explains it.')],
    F1=sec('Apply it: write and request disclosures', DISC, [
        Q('A skincare shop sends free products to an influencer who posts a glowing review. What should the post include?',
          'A clear note that the products were free from the shop', ('Nothing, because no cash was paid', 'gifts count'),
          ('Only a hashtag buried at the end', 'may not be clear'), ('A note saying the opinion is completely unbiased', 'not a disclosure'),
          'Free products are a material connection.'),
        Q('A blogger earns 8 percent commission on a 50-dollar item through an affiliate link. What does she earn per sale?', '4 dollars',
          ('8 dollars', 'percent as dollars'), ('0.40 dollars', 'moved decimal'), ('42 dollars', 'subtracted'), '0.08 x 50 = 4.',
          calc=lambda: round(0.08 * 50, 2) == 4),
        Q('Which disclosure placement is best on a short video?', 'Said aloud and shown on screen early', ('Only in the last second', 'easy to miss'),
          ('Only in a profile bio', 'easy to miss'), ('Only in a comment reply days later', 'easy to miss'), 'Early and visible.'),
        Q('A business runs a program paying people to promote it. What should the business do?', 'Tell promoters to disclose and check that they do',
          ('Tell promoters to hide payments so posts look natural', 'deceptive'), ('Ignore what promoters post', 'risky'),
          ('Ask promoters to use fake names', 'deceptive'), 'Businesses share responsibility.'),
        Q('Which phrase is a clear disclosure for a paid post?', '"Paid partnership with Lime Tree Pets"', ('"Thanks, LTP!"', 'unclear'),
          ('"#blessed"', 'unclear'), ('"Check them out maybe, if you like"', 'unclear'), 'Plain and specific.'),
    ]),
    F2=sec('Handle the complications: unclear and hidden connections', DISC, [
        Q('An influencer says, "I only post things I love, so I don\'t need to disclose payments." What is wrong?', 'Payment should be disclosed regardless of opinion',
          ('Nothing; honest opinions need no disclosure', 'connection still matters'), ('Disclosures are only for TV', 'not true'),
          ('Payments are always obvious', 'not always'), 'Disclose the connection.'),
        Q('An owner\'s employee praises the shop online without saying she works there. What should she add?', 'That she works for the shop',
          ('Nothing; employees are customers too', 'connection exists'), ('A discount code only', 'not a disclosure'),
          ('A fake name', 'deceptive'), 'Employment is a material connection.'),
        Q('A disclosure is written in tiny light-gray text. What is the problem?', 'People may not notice it', ('It is too clear', 'opposite'),
          ('It is too long', 'not the problem'), ('Gray text is illegal', 'no'), 'Must be easy to see.'),
        Q('A promoter refuses to disclose after being asked. What should the business do?', 'Stop working with that promoter',
          ('Keep paying and say nothing', 'risky'), ('Pay more to stay quiet', 'deceptive'), ('Disclose nothing either', 'risky'),
          'Enforce the rule.'),
        Q('Which statement is accurate?', 'Material connections should be disclosed clearly where people will see them.',
          ('Only cash payments count as connections.', 'gifts and commissions too'), ('Hashtags at the end are always enough.', 'not always'),
          ('Businesses have no role at all in whether their promoters disclose payments.', 'they do'), 'Clear disclosure.'),
    ]))

SETS = [s85, s86, s87, s88, s89, s90]
