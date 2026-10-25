"""Entrepreneurship sets 77-84: Foundation 10, a simple website; Amazon case. Names are fictional."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 77: clear offer and next action
OFFER = ('A visitor decides in seconds whether a website is useful. The top of the main page should answer three '
         'questions: WHAT do you offer, WHO is it for, and WHAT should the visitor do next? The next action is called a '
         'CALL TO ACTION, such as "Book a free 15-minute call" or "Order now." Use one main call to action per page, in '
         'plain words, easy to see. Example: "Dog walking for busy owners in Eastfield. Book your first walk." Vague '
         'slogans like "Excellence in everything" do not tell visitors what to do.')

s77 = SET('ENT.WEB.01',
    M=sec('Write a clear offer and a single call to action', OFFER, [
        Q('Which three questions should the top of a main page answer?', 'What, who it is for, and what to do next',
          ('When the owner was born, where she grew up, and her hobbies', 'not the visitor\'s questions'),
          ('How big the company hopes to grow over the next ten years', 'not the visitor\'s question'),
          ('Which web host and font the site uses for its pages', 'technical details'), 'Offer, audience, next step.'),
        Q('What is a call to action?', 'A clear next step for the visitor',
          ('A phone call from the owner to every visitor who arrives', 'not the meaning'),
          ('A legal notice about the site\'s privacy rules', 'not the meaning'),
          ('A list of every product the business has ever sold', 'not the meaning'), 'It tells visitors what to do.'),
        Q('Which headline is clearest?', '"Dog walking for busy owners in Eastfield"',
          ('"Excellence in everything we do, every day, for you"', 'vague slogan'),
          ('"Welcome to our website, we hope you enjoy your visit"', 'says nothing'),
          ('"Passion, quality and dedication since we started"', 'vague'), 'It says what and for whom.'),
        Q('How many main calls to action should a page usually have?', 'One', ('Ten, so visitors have plenty of choices', 'confusing'),
          ('None, so visitors decide entirely on their own', 'no direction'), ('Five, all with the same size and color', 'competing'),
          'One main action keeps focus.'),
        Q('Which call to action is clearest?', '"Book your first walk"', ('"Click here for more stuff and things"', 'vague'),
          ('"Learn about our journey and our values"', 'not an action toward buying'), ('"Submit"', 'unclear purpose'),
          'Plain, specific action.'),
    ]),
    B=[cs('A shop sign and an open door', 'Walking past a shop, you look for a sign saying what it sells and an open door. '
          '"Fresh bread, open now" tells you everything; a sign reading "Dreams" does not. A website\'s top section is the '
          'sign, and the call to action is the open door. If either is missing, people walk past, even if the shop is '
          'good.', [
        Q('A website\'s top section is like what?', 'The shop sign', ('The back storage room', 'hidden'),
          ('The parking lot behind the shop', 'not visible'), ('The cash register drawer', 'not the sign'), 'It says what is sold.'),
        Q('The call to action is like what?', 'The open door', ('A locked gate around the shop', 'blocks visitors'),
          ('A window with the curtains closed', 'hides the shop'), ('The roof of the building', 'not the entry'), 'It invites people in.'),
        Q('Which sign is clearer?', '"Fresh bread, open now"', ('"Dreams"', 'vague'), ('"Welcome to this place"', 'vague'),
          ('"We are here"', 'vague'), 'It names the product.'),
        Q('What happens if the sign and door are missing?', 'People walk past', ('More people come inside', 'no'),
          ('The bread bakes faster', 'no'), ('Rent goes down', 'no'), 'Visitors leave.'),
        Q('Can a good shop lose visitors because of a bad sign?', 'Yes', ('No, quality always shows from the street', 'not always'),
          ('Only on weekends', 'no'), ('Only if it rains', 'no'), 'Clarity matters.'),
    ], why='A learner who misses MAIN may not see why the top of a page matters; a shop sign and open door make it concrete.')],
    F1=sec('Apply it: rewrite a weak page top', OFFER, [
        Q('A tutor\'s page says "Unlock your potential." Which rewrite is best?', '"Math tutoring for grades 6-8 in Eastfield. Book a free first session."',
          ('"Unlock your potential and reach for the stars every day."', 'still vague'),
          ('"Welcome! Please read our long story about why we started this business years ago."', 'no offer'),
          ('"Tutoring. Things. Stuff. Call maybe if you want to."', 'unclear'), 'What, who, next step.'),
        Q('A bakery page has buttons for "Order," "Newsletter," "Careers," "Blog" and "Gallery," all the same size. What should '
          'change?', 'Make "Order" the clear main button', ('Add five more buttons of the same size', 'more clutter'),
          ('Remove the "Order" button entirely', 'removes the goal'), ('Make every button flash', 'distracting'),
          'One main action stands out.'),
        Q('A page gets 500 visitors and 10 click "Book now." What percent clicked?', '2 percent', ('10 percent', 'count'),
          ('5 percent', 'misdivided'), ('50 percent', 'reversed'), '10 / 500 = 0.02.', calc=lambda: 10 / 500 == 0.02),
        Q('After rewriting the headline, 25 of 500 visitors click. How many more clicks than before?', '15', ('25', 'new total'),
          ('10', 'old total'), ('35', 'added'), '25 - 10 = 15.', calc=lambda: 25 - 10 == 15),
        Q('Which detail best shows WHO the offer is for?', '"for busy owners in Eastfield"', ('"since last spring"', 'time'),
          ('"with lots of passion and care"', 'feeling'), ('"and so much more"', 'vague'), 'Names the audience.'),
    ]),
    F2=sec('Handle the complications: many products and unclear goals', OFFER, [
        Q('A shop sells candles, soap and gift boxes. What is a good approach for the main page?', 'Lead with the main offer and link clearly to the others',
          ('List every product in tiny text with no headline', 'overwhelming'), ('Show nothing until visitors scroll far down', 'hidden'),
          ('Pick a random product each day', 'confusing'), 'Clear priority with simple navigation.'),
        Q('An owner wants visitors to call, email, book online and follow on social media, all equally. What is the risk?',
          'Visitors may do nothing because no step stands out', ('Visitors always do every step', 'unlikely'),
          ('More options always mean more sales for the business', 'not always'), ('Search engines ban the page', 'no'), 'Too many choices.'),
        Q('A call to action says "Get a quote," but the form asks for 15 fields. What might happen?', 'Many visitors give up',
          ('Every visitor finishes happily', 'unlikely'), ('Sales double automatically', 'no'), ('Nothing changes', 'friction matters'),
          'Long forms lose people.'),
        Q('A headline is clear but the page loads very slowly on phones. What should the owner check next?', 'Page speed on a phone',
          ('The logo\'s font', 'minor'), ('The owner\'s biography', 'minor'), ('The footer color', 'minor'), 'Slow pages lose visitors.'),
        Q('Which statement is accurate?', 'A clear offer and one main next step help visitors act.',
          ('Slogans always work better than plain descriptions.', 'not usually'), ('More buttons always help.', 'not always'),
          ('Visitors read every word before deciding.', 'they skim'), 'Clarity drives action.'),
    ]))

# ------------------------------------------------------------------ Set 78: trust signals, pricing, FAQ, policies
TRUST = ('Visitors need reasons to trust a new business. TRUST SIGNALS include real contact details, a short "about" '
         'section with a real person, genuine reviews used with permission, photos of actual work, and clear policies. '
         'Showing PRICES (or a starting price) saves everyone time. An FAQ (frequently asked questions) answers common '
         'worries such as delivery time or what happens if something goes wrong. Posting refund, privacy and shipping '
         'policies before purchase sets expectations. Never invent reviews or badges.')

s78 = SET('ENT.WEB.02',
    M=sec('Add honest trust signals, prices, an FAQ and policies', TRUST, [
        Q('Which is an honest trust signal?', 'Genuine reviews used with permission',
          ('Made-up five-star reviews written by the owner herself', 'fake'),
          ('A "Best in the World" badge the owner designed for herself', 'fake'),
          ('Stock photos labeled as the owner\'s own completed work', 'misleading'), 'Real and permitted.'),
        Q('What is an FAQ?', 'Answers to common questions', ('A list of the owner\'s favorite quotes', 'not FAQ'),
          ('A legal filing with the state each year', 'not FAQ'), ('A fee charged for answering questions', 'not FAQ'),
          'Frequently asked questions.'),
        Q('Why show a price or starting price?', 'It saves visitors and the owner time',
          ('It is required on every website by federal law', 'not a universal rule'),
          ('It guarantees that every visitor will buy', 'no guarantee'),
          ('It hides the real cost from customers', 'opposite'), 'Prices help visitors decide.'),
        Q('When should refund and shipping policies be visible?', 'Before purchase', ('Only after a complaint arrives', 'too late'),
          ('Only in a printed letter mailed later', 'hard to find'), ('Never; policies scare visitors', 'they build trust'),
          'Expectations come first.'),
        Q('Which detail shows a real business behind the site?', 'Real contact details', ('A long list of buzzwords', 'not proof'),
          ('A countdown timer on every page', 'pressure, not trust'), ('A hidden email address', 'opposite'), 'Contact info builds trust.'),
    ]),
    B=[cs('Meeting a new babysitter', 'Before hiring a new babysitter, parents want a real name, a way to reach them, '
          'references from families they helped, a clear hourly rate, and answers to "What if my child gets sick?" A website '
          'is the same first meeting. Real contact details, honest reviews, prices and answers to common worries help a '
          'stranger decide to trust you.', [
        Q('References from families are like what on a website?', 'Genuine reviews', ('A fancy logo', 'not trust'),
          ('A long slogan', 'not trust'), ('Bright colors', 'not trust'), 'Real feedback.'),
        Q('A clear hourly rate is like what?', 'Showing prices', ('Hiding prices', 'opposite'), ('A coupon', 'no'), ('A tax form', 'no'),
          'Prices help decisions.'),
        Q('"What if my child gets sick?" is like what?', 'An FAQ answer', ('A sales pitch', 'no'), ('A review', 'no'),
          ('A logo', 'no'), 'Answers to worries.'),
        Q('A way to reach the babysitter is like what?', 'Real contact details', ('A hidden email', 'no'), ('No phone number listed', 'no'),
          ('A fake address', 'no'), 'Reachability builds trust.'),
        Q('Why do parents want these things?', 'To decide whether to trust a stranger', ('To pay more', 'no'),
          ('To waste time', 'no'), ('To avoid hiring anyone at all, ever', 'no'), 'Trust needs evidence.'),
    ], why='A learner who misses MAIN may not see why trust signals matter; hiring a babysitter is familiar.')],
    F1=sec('Apply it: strengthen a page\'s trust', TRUST, [
        Q('A new cleaning service has no reviews yet. What is an honest option?', 'Ask early customers for permission to share their feedback',
          ('Write a few glowing reviews under made-up customer names', 'fake'), ('Copy reviews from a competitor', 'deceptive'),
          ('Buy reviews from a website', 'fake'), 'Collect genuine reviews.'),
        Q('Customers often email asking about delivery time. What would reduce these emails?', 'An FAQ answer about delivery times',
          ('Removing the email address from the website', 'loses customers'), ('Ignoring the emails', 'harms trust'),
          ('A popup advertisement on every page', 'irrelevant'), 'Answer common questions on the site.'),
        Q('Which "about" section builds the most trust?', '"I\'m Dana, I\'ve cleaned homes in Eastfield for 6 years."',
          ('"We are a world-leading enterprise of solutions."', 'vague'), ('"About us: coming soon, check back."', 'empty'),
          ('"We prefer to stay anonymous."', 'less trust'), 'A real person with relevant detail.'),
        Q('A site shows "from 80 dollars" and gets 40 inquiries, 30 of which fit the budget. Before, without prices, 40 inquiries '
          'had only 12 that fit. How many more fitting inquiries?', '18', ('30', 'new total'), ('12', 'old total'), ('28', 'miscalculated'),
          '30 - 12 = 18.', calc=lambda: 30 - 12 == 18),
        Q('Which policy should a shop selling online post before checkout?', 'Its refund and shipping policy', ('Its owner\'s diet', 'irrelevant'),
          ('Its office plant schedule', 'irrelevant'), ('Its staff birthdays', 'irrelevant'), 'Policies set expectations.'),
    ]),
    F2=sec('Handle the complications: tempting shortcuts', TRUST, [
        Q('A web designer offers to add a "Trusted by 10,000 customers" banner, but the shop has 40. What should the owner do?',
          'Refuse, because the claim is false', ('Accept, since everyone exaggerates', 'deceptive'), ('Change it to 9,000', 'still false'),
          ('Hide it on another page', 'still false'), 'Claims must be true.'),
        Q('A competitor displays award badges from a contest that does not exist. What is the lesson?', 'Invented badges are deceptive and risky',
          ('Copy them to look equal', 'deceptive'), ('Make an even bigger badge for her own site', 'deceptive'), ('Badges never matter', 'not the point'),
          'Do not invent credentials.'),
        Q('A business prefers not to show exact prices because each job differs. What is a helpful middle ground?', 'Show a starting price or typical range',
          ('Show no information at all about cost', 'frustrating'), ('Show a fake low price', 'misleading'),
          ('Show a price meant for another service', 'misleading'), 'Ranges help visitors.'),
        Q('A review mentions a customer\'s full name and address. What should the owner do before posting it?', 'Get permission and remove private details',
          ('Post it exactly as written', 'privacy risk'), ('Add even more details', 'privacy risk'), ('Change the customer\'s words to sound better', 'misleading'),
          'Respect privacy and accuracy.'),
        Q('Which statement is accurate?', 'Honest signals build trust; invented ones risk trust and legal trouble.',
          ('Fake reviews are harmless as long as they are positive and kind.', 'deceptive'), ('Policies scare customers away.', 'they build trust'),
          ('Prices should always be hidden.', 'not helpful'), 'Honesty matters.'),
    ]))

# ------------------------------------------------------------------ Set 79: readable on phones, accessible forms
MOBILE = ('Many visitors use phones, so check every page on a small screen. Text should be large enough to read without '
          'zooming, buttons big enough to tap, and nothing should require sideways scrolling. ACCESSIBILITY means people '
          'with disabilities can use the site too: give images short text descriptions (alt text), keep strong contrast '
          'between text and background, label every form field, and make forms short. A form with 3 fields is usually '
          'finished more often than one with 12.')

s79 = SET('ENT.WEB.03',
    M=sec('Make pages readable on phones and forms accessible', MOBILE, [
        Q('What is alt text?', 'A short text description of an image',
          ('A second, alternative website for older visitors', 'not alt text'),
          ('A secret password typed to edit the website', 'not alt text'),
          ('The large heading at the top of each page', 'not alt text'), 'It describes images for screen readers.'),
        Q('Which is a phone-friendly practice?', 'Buttons big enough to tap', ('Tiny links packed tightly together', 'hard to tap'),
          ('Pages that need sideways scrolling to read', 'awkward'), ('Text so small that zooming is required', 'hard to read'),
          'Tappable buttons help.'),
        Q('Why label every form field?', 'So everyone knows what to type', ('So the form looks longer and more official', 'not the goal'),
          ('Because labels make pages load faster', 'not the reason'), ('So visitors must guess', 'opposite'), 'Labels guide users.'),
        Q('Which is better for contrast?', 'Dark text on a light background', ('Light gray text on a white background', 'low contrast'),
          ('Yellow text on a white background', 'low contrast'), ('Dark blue text on a black background', 'low contrast'),
          'Strong contrast is readable.'),
        Q('Which form is usually finished more often?', 'One with 3 fields', ('One with 12 fields', 'longer'), ('One with 20 fields', 'longer'),
          ('One with no labels', 'confusing'), 'Short forms work better.'),
    ]),
    B=[cs('Reading a menu in a dark restaurant', 'Imagine a menu with tiny gray letters in a dark restaurant: hard to read. Now '
          'imagine a menu with large dark letters on white paper and pictures described in words: easy for everyone, '
          'including someone with poor eyesight. A website on a phone is like that menu. Big clear text, labeled choices '
          'and descriptions of pictures help everyone order.', [
        Q('Tiny gray letters in the dark are like what?', 'Low-contrast small text on a phone', ('A clear, readable website on a phone', 'opposite'),
          ('A big button', 'opposite'), ('A short form', 'unrelated'), 'Hard to read.'),
        Q('Pictures described in words are like what?', 'Alt text', ('Hidden text', 'no'), ('Ads', 'no'), ('Passwords', 'no'),
          'Descriptions help people who cannot see the image.'),
        Q('Who benefits from large dark letters?', 'Everyone, including people with poor eyesight', ('Only the chef working in the kitchen tonight', 'no'),
          ('Nobody', 'no'), ('Only children', 'no'), 'Accessibility helps all.'),
        Q('Labeled choices on a menu are like what?', 'Labeled form fields', ('Blank boxes', 'no'), ('Hidden prices on the menu', 'no'),
          ('A long story', 'no'), 'Labels guide choices.'),
        Q('The website on a phone is like what?', 'The menu', ('The kitchen', 'no'), ('The parking lot', 'no'), ('The roof', 'no'),
          'People read it to decide.'),
    ], why='A learner who misses MAIN may not picture the user\'s view; a hard-to-read menu makes it familiar.')],
    F1=sec('Apply it: fix a page for phones and access', MOBILE, [
        Q('An owner tests her booking page on a phone and must zoom to read the prices. What should change?', 'Increase the text size',
          ('Add more text to the same area', 'worse'), ('Remove the prices', 'loses information'), ('Use lighter gray text', 'worse'),
          'Readable without zooming.'),
        Q('A contact form asks for name, email, phone, address, birthday, company size, budget, favorite color and how they '
          'heard about you. What is the best fix?', 'Keep only the fields truly needed', ('Add more optional fields at the end', 'longer'),
          ('Remove the labels', 'confusing'), ('Make it a 3-page form', 'longer'), 'Short forms finish more.'),
        Q('A form had 12 fields and 20 of 200 visitors finished it. After cutting to 4 fields, 50 of 200 finished. By how many '
          'percentage points did completion rise?', '15', ('30', 'counted finishers'), ('25', 'new rate'), ('10', 'old rate'),
          '25 percent - 10 percent = 15 points.', calc=lambda: round(50 / 200 * 100 - 20 / 200 * 100) == 15),
        Q('Which alt text is most useful for a photo of a blue ceramic mug?', '"Blue ceramic coffee mug, 12 ounces"',
          ('"image123.jpg"', 'not descriptive'), ('"Picture"', 'not descriptive'), ('"Buy now buy now buy now today"', 'not a description'),
          'Describes the image.'),
        Q('A button reads only "Go." What would make it clearer?', '"Send my booking request"', ('"Click"', 'vague'),
          ('"OK"', 'vague'), ('"Next thing, please, now"', 'vague'), 'Say what happens.'),
    ]),
    F2=sec('Handle the complications: design versus usability', MOBILE, [
        Q('A designer wants pale gray text because it "looks elegant." What should the owner weigh?', 'Readability for all visitors',
          ('Only what looks trendy this year', 'ignores readers'), ('Only the designer\'s preference', 'ignores readers'),
          ('Nothing; color never matters', 'it does'), 'Contrast affects readability.'),
        Q('An image contains important text, like the price list, with no other text version. What problem does this create?',
          'Screen readers and some phones may not show the information clearly', ('Nothing, because images with text always work everywhere for everyone', 'not always'),
          ('It makes the site load faster', 'usually slower'), ('Search engines prefer it', 'not usually'), 'Put key info in real text.'),
        Q('A form fails without saying why. What should it do?', 'Show a clear message about what to fix', ('Erase all the visitor\'s entries silently', 'frustrating'),
          ('Show only a red flash', 'unclear'), ('Close the page', 'frustrating'), 'Helpful error messages.'),
        Q('The site works on the owner\'s large computer screen. What else should she test?', 'A phone and a slow connection',
          ('Only her own computer again', 'not enough'), ('Only the logo file', 'not enough'), ('Nothing else', 'not enough'),
          'Test where visitors are.'),
        Q('Which statement is accurate?', 'Clear, accessible pages help more people use the site.',
          ('Accessibility only helps a tiny group of visitors, so it can wait.', 'helps many'), ('Phones are rarely used to browse.', 'often used'),
          ('Longer forms always get more sign-ups.', 'usually fewer'), 'Usability helps everyone.'),
    ]))

# ------------------------------------------------------------------ Set 80: domain, hosting, builders, ownership
OWN = ('A website has parts. The DOMAIN is the address (yourshop.example), rented yearly from a registrar. HOSTING is the '
       'service that stores the site and shows it to visitors. A WEBSITE BUILDER combines hosting and design tools. Check '
       'WHO OWNS each part: the domain should be registered in the business owner\'s name and account, not only a '
       'designer\'s. Keep the login details safe, turn on auto-renewal or a reminder, and know how to export your content '
       'if you switch builders.')

s80 = SET('ENT.WEB.04',
    M=sec('Know the parts of a website and who controls each', OWN, [
        Q('What is a domain?', 'The website\'s address', ('The company that designs the logo', 'not a domain'),
          ('The computer that stores the website\'s files', 'that is hosting'), ('A legal entity like an LLC', 'not a domain'),
          'It is the address.'),
        Q('What is hosting?', 'The service that stores and shows the site', ('The address visitors type into a browser', 'domain'),
          ('The owner of the business', 'not hosting'), ('The text on the homepage', 'content'), 'It stores the site.'),
        Q('In whose account should the domain be registered?', 'The business owner\'s', ('Only the web designer\'s personal account', 'risk'),
          ('A random friend\'s account', 'risk'), ('Nobody\'s account at all', 'not possible'), 'The business should control it.'),
        Q('Why turn on domain auto-renewal or a reminder?', 'So the address does not expire', ('So the website loads faster', 'unrelated'),
          ('So the logo changes color', 'unrelated'), ('So the business pays no taxes', 'unrelated'), 'Expired domains can be lost.'),
        Q('Why know how to export content from a builder?', 'So you can move if you switch builders', ('So the site looks fancier', 'unrelated'),
          ('Because exports double the site\'s traffic', 'no'), ('Because builders never close', 'they can change'), 'Portability protects you.'),
    ]),
    B=[cs('Address, building and furniture', 'Think of a shop. The street address is the domain: how people find it. The '
          'building is the hosting: where the shop actually sits. The furniture and decorations are the design. If the '
          'address is registered in someone else\'s name, they could redirect your customers. That is why the business '
          'owner should hold the address in her own name.', [
        Q('The street address is like what?', 'The domain', ('The hosting', 'building'), ('The design', 'furniture'),
          ('The logo', 'no'), 'The domain is the address.'),
        Q('The building is like what?', 'The hosting', ('The domain', 'address'), ('The design', 'furniture'), ('The price', 'no'),
          'Hosting holds the site.'),
        Q('The furniture is like what?', 'The design', ('The domain', 'address'), ('The hosting', 'building'), ('The bank', 'no'),
          'Design is the look.'),
        Q('What could happen if someone else holds your address?', 'They could redirect your customers', ('Nothing at all would change for you', 'risk'),
          ('Rent goes down', 'no'), ('Sales double', 'no'), 'Control matters.'),
        Q('Who should hold the address?', 'The business owner', ('A stranger', 'no'), ('A competitor down the street', 'no'), ('Nobody', 'no'),
          'Own your domain.'),
    ], why='A learner who misses MAIN may blur the parts of a website; address, building and furniture separate them.')],
    F1=sec('Apply it: check ownership and costs', OWN, [
        Q('A designer built Rosa\'s site and registered the domain in the designer\'s own account. What should Rosa do?',
          'Ask to transfer the domain into her own account', ('Nothing, because designers always keep it safe', 'risk'),
          ('Buy a different domain and forget the old one', 'loses address'), ('Share her bank password with the designer', 'unsafe'),
          'Control the domain.'),
        Q('Domain 15 dollars a year, builder 18 dollars a month. What is the yearly total?', '231 dollars', ('33 dollars', 'one month'),
          ('216 dollars', 'missed domain'), ('195 dollars', 'arithmetic slip'), '15 + 18 x 12 = 231.', calc=lambda: 15 + 18 * 12 == 231),
        Q('A domain expired because the card on file was out of date. What would have prevented this?', 'An updated card and a renewal reminder',
          ('A new logo design', 'unrelated'), ('A longer homepage with more text', 'unrelated'), ('Fewer products', 'unrelated'),
          'Keep billing current.'),
        Q('Which item should the business owner keep in a safe place?', 'The login details for the registrar and host',
          ('A copy of a competitor\'s site and prices', 'irrelevant'), ('An old newspaper ad', 'irrelevant'), ('A blank form', 'irrelevant'),
          'Access is essential.'),
        Q('A builder plan costs 25 dollars a month, or 240 dollars if paid yearly. How much does yearly payment save?', '60 dollars',
          ('25 dollars', 'one month'), ('240 dollars', 'yearly price'), ('300 dollars', 'monthly total'), '25 x 12 - 240 = 60.',
          calc=lambda: 25 * 12 - 240 == 60),
    ]),
    F2=sec('Handle the complications: lock-in and lost access', OWN, [
        Q('An owner wants to leave her builder but cannot export her product pages. What should she plan?', 'Time to rebuild pages elsewhere',
          ('Nothing; everything moves automatically', 'not always'), ('Deleting the domain', 'loses address'),
          ('Paying the builder forever regardless', 'not the only option'), 'Check portability before choosing.'),
        Q('A former helper still has the only login to the host. What is the risk?', 'The owner may lose control of the site',
          ('No risk, because helpers never leave or forget', 'they can'), ('Faster loading', 'unrelated'), ('Lower costs', 'unrelated'),
          'Owners need their own access.'),
        Q('A "free" builder places its ads on the site and uses its own address in the URL. What tradeoff exists?', 'Lower cost but less control and a less professional look',
          ('No tradeoff at all', 'there is one'), ('It always ranks first in search results for the shop\'s name', 'not guaranteed'),
          ('It owns the business', 'not the business'), 'Free plans have limits.'),
        Q('Which statement about domain ownership is accurate?', 'Whoever controls the registrar account controls the domain.',
          ('The business always owns the domain automatically.', 'not always'), ('Domains last forever once bought.', 'renewal needed'),
          ('The host always owns the domain.', 'not necessarily'), 'Account control matters.'),
        Q('Before signing with a web designer, what should the owner ask?', 'Who will own the domain, hosting account and content',
          ('Only the designer\'s favorite color', 'irrelevant'), ('Only how many sites they have built for other clients', 'not enough'),
          ('Nothing; ownership never matters', 'it does'), 'Clarify ownership in writing.'),
    ]))

# ------------------------------------------------------------------ Set 81: HTTPS, testing, backups
SAFE = ('HTTPS (shown by a lock icon and "https://" in the address bar) encrypts the connection between the visitor and '
        'the site; most builders and hosts provide it, often free. TEST before launch and after changes: click every link, '
        'submit every form, place a test order, and check on a phone. BACKUPS are copies of the site and its data; keep '
        'them regularly and know how to restore one. A backup you have never tested may not work when you need it.')

s81 = SET('ENT.WEB.05',
    M=sec('Use HTTPS, test key paths and keep tested backups', SAFE, [
        Q('What does HTTPS do?', 'Encrypts the connection with visitors', ('Makes the site rank first in every search', 'not guaranteed'),
          ('Designs a new logo for the business', 'unrelated'), ('Removes the need for any passwords', 'unrelated'),
          'It protects data in transit.'),
        Q('Which test should happen before launch?', 'Placing a test order', ('Changing the logo color one more time', 'not a test'),
          ('Writing a longer company history', 'not a test'), ('Turning off the contact form', 'harmful'), 'Test the key paths.'),
        Q('What is a backup?', 'A copy of the site and its data', ('A second domain name for the shop', 'not a backup'),
          ('An extra employee', 'not a backup'), ('A spare logo file', 'too narrow'), 'Copies allow recovery.'),
        Q('Why test restoring a backup?', 'An untested backup may not work', ('Restoring always deletes the site', 'not true'),
          ('Testing makes backups expire', 'not true'), ('It is required daily by law', 'not a rule'), 'Confirm it works.'),
        Q('How can a visitor tell HTTPS is on?', 'A lock icon and "https://" in the address bar', ('A big red banner across the top of the page', 'no'),
          ('The site has many pictures', 'no'), ('The page has a long footer', 'no'), 'Browser signs show it.'),
    ]),
    B=[cs('A sealed envelope and a spare key', 'Sending a postcard lets anyone read it; a sealed envelope keeps it private. HTTPS '
          'is the sealed envelope for information sent to your site. A backup is like a spare house key kept with a trusted '
          'friend: if you lose yours, you can get back in. But you should try the spare once to make sure it actually '
          'fits the lock.', [
        Q('HTTPS is like what?', 'A sealed envelope', ('A postcard', 'readable'), ('A roadside billboard', 'public'), ('A shout', 'public'),
          'It keeps information private.'),
        Q('A backup is like what?', 'A spare house key', ('A broken door lock', 'no'), ('A new house', 'no'), ('A doorbell', 'no'),
          'It lets you recover.'),
        Q('Why try the spare key once?', 'To make sure it fits', ('To wear it out', 'no'), ('To lose it', 'no'), ('To copy it publicly', 'no'),
          'Test the backup.'),
        Q('A postcard is like a site without what?', 'HTTPS', ('A logo', 'no'), ('A price list', 'no'), ('A domain', 'no'),
          'Without encryption, data is exposed.'),
        Q('Where is the spare key kept?', 'With a trusted friend', ('Under the front doormat', 'unsafe'), ('In the lock', 'unsafe'),
          ('Nowhere', 'no backup'), 'Backups belong somewhere safe.'),
    ], why='A learner who misses MAIN may not picture encryption and backups; an envelope and spare key make them concrete.')],
    F1=sec('Apply it: run a launch checklist', SAFE, [
        Q('An owner\'s checkout page shows "Not secure" in the browser. What should she do first?', 'Turn on HTTPS through her host or builder',
          ('Add a bigger "Buy now" button to the checkout', 'not the fix'), ('Ignore the warning', 'scares buyers'), ('Change the font', 'not the fix'),
          'Fix the security setting.'),
        Q('A checklist has 20 items and 16 pass. What percent pass?', '80 percent', ('16 percent', 'count'), ('4 percent', 'failures'),
          ('20 percent', 'total'), '16 / 20 = 0.80.', calc=lambda: 16 / 20 == 0.8),
        Q('After editing the shop page, which test is most important?', 'Placing a test order again', ('Rereading the about page', 'minor'),
          ('Checking the footer year', 'minor'), ('Counting images', 'minor'), 'Retest key paths after changes.'),
        Q('Backups run weekly. The site breaks on Friday; the last backup was Monday. How many days of changes could be lost?', '4 days',
          ('7 days', 'full week'), ('1 day', 'too few'), ('0 days', 'some lost'), 'Monday to Friday = 4 days.', calc=lambda: 5 - 1 == 4),
        Q('Which backup habit is best?', 'Regular backups stored separately and tested', ('One backup made years ago', 'outdated'),
          ('Backups stored only on the same server', 'lost together'), ('No backups to save time', 'risky'), 'Regular, separate, tested.'),
    ]),
    F2=sec('Handle the complications: breaks and recoveries', SAFE, [
        Q('A plugin update breaks the checkout. What helps recover fastest?', 'Restoring a recent tested backup',
          ('Rebuilding the whole site from memory', 'slow'), ('Waiting for customers to report problems', 'slow'),
          ('Deleting the domain', 'harmful'), 'Backups enable quick recovery.'),
        Q('Daily orders average 12. Checkout was broken for 3 days unnoticed. About how many orders may have been lost?', '36',
          ('12', 'one day'), ('15', 'added'), ('4', 'divided'), '12 x 3 = 36.', calc=lambda: 12 * 3 == 36),
        Q('What would have caught the broken checkout sooner?', 'Testing checkout after every update', ('Never updating anything', 'other risks'),
          ('Hiding the checkout page from visitors', 'harmful'), ('Adding more pages', 'unrelated'), 'Test after changes.'),
        Q('An owner\'s only backup is on the same server as the site, which fails. What is the lesson?', 'Store backups separately',
          ('Backups are useless', 'not true'), ('Servers never fail', 'they can'), ('Make backups only yearly', 'worse'),
          'Separate storage protects backups.'),
        Q('Which statement is accurate?', 'HTTPS, testing and tested backups reduce the damage from problems.',
          ('HTTPS makes a site impossible to break, so testing is not needed.', 'overstated'), ('Backups never need testing.', 'they do'),
          ('Testing is only needed once at launch.', 'after changes too'), 'Layered habits.'),
    ]))

# ------------------------------------------------------------------ Set 82: search visibility basics
SEO = ('SEARCH VISIBILITY means people can find your site when they search. Basics: use the words customers actually '
       'type (for example "dog walker Eastfield" rather than "canine companionship solutions"); give each page a clear '
       'title and heading; write useful, original text; and for local businesses, keep the business name, address and '
       'phone the same everywhere and set up free local business listings. Results take time. Be wary of anyone '
       'promising "number one on search in a week."')

s82 = SET('ENT.WEB.06',
    M=sec('Apply search basics with customer words and consistent listings', SEO, [
        Q('Which words should a page use?', 'Words customers actually type', ('Fancy terms customers never use', 'not searched'),
          ('Random popular words unrelated to the business', 'misleading'), ('Only the owner\'s inside jokes', 'not searched'),
          'Match how people search.'),
        Q('Which phrase is a better page title for a local dog walker?', '"Dog Walker in Eastfield"', ('"Canine Companionship Solutions"', 'not searched'),
          ('"Welcome Page Number One"', 'vague'), ('"Home"', 'vague'), 'Plain words customers type.'),
        Q('What should stay the same across local listings?', 'Business name, address and phone', ('Only the logo color', 'not enough'),
          ('Only the owner\'s nickname', 'not enough'), ('Nothing; vary them for variety', 'confuses'), 'Consistency helps.'),
        Q('How quickly do search results usually improve?', 'Over time', ('Instantly, within an hour', 'unrealistic'),
          ('Never, under any circumstances', 'they can improve'), ('Only if you pay to guarantee first place', 'not guaranteed'),
          'Patience is needed.'),
        Q('Someone promises "number one on search in a week." How should an owner react?', 'Be wary of the promise',
          ('Pay immediately before the offer ends', 'risky'), ('Trust it because it sounds confident', 'risky'),
          ('Give them all passwords', 'unsafe'), 'Guarantees are a warning sign.'),
    ]),
    B=[cs('Labeling boxes in a storage room', 'If you label storage boxes "Stuff," nobody can find the winter coats. If you label '
          'one "Winter coats - adults," people find it quickly. Search engines are like a giant storage room. Clear page '
          'titles and the words people really use are good labels. Fancy labels that nobody searches for leave your box '
          'unfound, even if what is inside is exactly what people want.', [
        Q('Which box label is easier to find?', '"Winter coats - adults"', ('"Stuff"', 'vague'), ('"Box 7, shelf B, back row"', 'vague'),
          ('"Misc"', 'vague'), 'Specific words.'),
        Q('Search engines are like what?', 'A giant storage room', ('A single small drawer', 'too small'), ('A locked safe', 'no'),
          ('A trash can', 'no'), 'They organize many pages.'),
        Q('Clear page titles are like what?', 'Good box labels', ('Blank boxes', 'no'), ('Hidden boxes', 'no'), ('Broken, torn boxes', 'no'),
          'Labels help finding.'),
        Q('Fancy labels nobody searches for lead to what?', 'Your box going unfound', ('More visitors finding it', 'no'), ('Instant sales', 'no'),
          ('Lower rent', 'no'), 'Use real words.'),
        Q('What makes a good label?', 'The words people really use', ('Secret codes', 'no'), ('Random numbers and letters', 'no'),
          ('Long jokes', 'no'), 'Match the searcher.'),
    ], why='A learner who misses MAIN may not see why words matter; labeling storage boxes makes it concrete.')],
    F1=sec('Apply it: improve a local page', SEO, [
        Q('A bakery\'s homepage title is "Home." What is a better title?', '"Fresh Bread and Cakes - Riverside Bakery, Eastfield"',
          ('"Home Page Welcome Hello - Our Site - Page 1"', 'vague'), ('"Click Here Now Please"', 'vague'), ('"Untitled Document 1"', 'vague'),
          'Product, name, place.'),
        Q('The bakery\'s phone number differs on its site and two listings. What should it do?', 'Make the number the same everywhere',
          ('Keep all three numbers for variety', 'confusing'), ('Remove the phone number entirely', 'loses calls'),
          ('Add a fourth number', 'worse'), 'Consistency helps customers and search.'),
        Q('A page gets 200 visits a month from search. After clearer titles, it gets 260. What is the percent increase?', '30 percent',
          ('60 percent', 'used count'), ('23 percent', 'used new base'), ('260 percent', 'not the change'), '60 / 200 = 0.30.',
          calc=lambda: (260 - 200) / 200 == 0.30),
        Q('Which content is most useful for search and customers?', 'An original page answering "How to order a custom cake"',
          ('A page copied from a competitor', 'not original'), ('A page stuffed with "cake cake cake" repeated hundreds of times', 'spammy'),
          ('An empty page with only a title', 'no content'), 'Useful and original.'),
        Q('A plumber serves Eastfield and Westvale. What might help local searchers?', 'Clear mention of the areas served',
          ('Hiding the service area', 'confusing'), ('Listing 50 cities he never visits', 'misleading'), ('Only a logo', 'not enough'),
          'Honest service areas.'),
    ]),
    F2=sec('Handle the complications: shortcuts and slow results', SEO, [
        Q('An agency offers to add hundreds of hidden keywords to the page. What should the owner consider?', 'Hidden tricks can hurt trust and visibility',
          ('It always guarantees first place', 'not guaranteed'), ('Hidden words are invisible, so harmless', 'risky'),
          ('Search engines reward hidden text', 'not usually'), 'Avoid manipulative tricks.'),
        Q('After a month of improvements, search visits have not changed. What is a reasonable view?', 'Results often take more time; keep improving and measuring',
          ('Search never works for small businesses, so stop trying', 'not true'), ('Undo all improvements immediately', 'premature'),
          ('Pay for a guaranteed ranking', 'not guaranteed'), 'Patience and measurement.'),
        Q('A competitor posts fake listings with other addresses. What should the owner do?', 'Keep her own listings accurate and report misuse through official channels',
          ('Create fake listings with other addresses too, so the competitor is crowded out', 'deceptive'), ('Copy their text', 'not original'), ('Give up on listings', 'loses visibility'),
          'Stay honest.'),
        Q('Which is NOT a search basic from the passage?', 'Buying a guarantee of first place', ('Clear page titles', 'basic'),
          ('Customer words', 'basic'), ('Consistent business listings', 'basic'), 'Guarantees are not a basic.'),
        Q('Which statement is accurate?', 'Clear, useful pages and consistent listings help people find a business over time.',
          ('Search results are instant and permanent.', 'not true'), ('Copying content ranks best.', 'not true'),
          ('Free business listings never matter for local businesses like shops and plumbers.', 'they do'), 'Steady basics.'),
    ]))

# ------------------------------------------------------------------ Set 83: measuring useful actions
MEASURE = ('Count what matters. VISITS show how many people came, but USEFUL ACTIONS show whether the site works: bookings, '
           'orders, sign-ups, calls. CONVERSION RATE = useful actions / visits. Example: 20 orders from 800 visits is '
           '20 / 800 = 2.5 percent. Track where visitors came from, and change one thing at a time so you know what made the '
           'difference. A big number of visits with no actions means the page is not doing its job.')

s83 = SET('ENT.WEB.07',
    M=sec('Measure useful actions and conversion rate', MEASURE, [
        Q('What is a useful action?', 'A booking, order, sign-up or call', ('A visit that lasts one second', 'not an action'),
          ('A like on a stock photo', 'not useful'), ('A page loading', 'not an action'), 'Actions that move business forward.'),
        Q('What is conversion rate?', 'Useful actions divided by visits', ('Visits divided by useful actions', 'reversed'),
          ('Visits minus useful actions', 'not a rate'), ('Useful actions times visits', 'not a rate'), 'Actions per visit.'),
        Q('30 orders from 1,200 visits. What is the conversion rate?', '2.5 percent', ('30 percent', 'count'), ('40 percent', 'reversed'),
          ('0.25 percent', 'moved decimal'), '30 / 1,200 = 0.025.', calc=lambda: 30 / 1200 == 0.025),
        Q('Why change one thing at a time?', 'To know which change made the difference', ('Because many changes are illegal', 'not true'),
          ('Because one change always doubles sales', 'not true'), ('To avoid tracking anything', 'opposite'), 'Isolate the effect.'),
        Q('Many visits but no actions suggests what?', 'The page is not doing its job', ('The page is perfect', 'no'),
          ('Visits are always bad', 'no'), ('Tracking actions is unnecessary', 'no'), 'Look at actions, not just visits.'),
    ]),
    B=[mathb('Rates as percents', 'A rate compares a part to a whole. Conversion rate = actions / visits, then times 100 for a '
             'percent. Example: 15 bookings from 500 visits: 15 / 500 = 0.03 = 3 percent. To predict actions, multiply visits '
             'by the rate: 1,000 visits at 3 percent = 0.03 x 1,000 = 30. Check that the percent is reasonable: actions '
             'cannot exceed visits.', [
        Q('12 actions from 400 visits is what percent?', '3 percent', ('12 percent', 'count'), ('33 percent', 'reversed'),
          ('0.3 percent', 'moved decimal'), '12 / 400 = 0.03.', calc=lambda: 12 / 400 == 0.03),
        Q('2,000 visits at 2 percent gives how many actions?', '40', ('20', 'moved decimal'), ('400', 'moved decimal'),
          ('2,002', 'added'), '0.02 x 2,000 = 40.', calc=lambda: 0.02 * 2000 == 40),
        Q('50 actions from 1,000 visits is what percent?', '5 percent', ('50 percent', 'count'), ('20 percent', 'reversed'),
          ('0.5 percent', 'moved decimal'), '50 / 1,000 = 0.05.', calc=lambda: 50 / 1000 == 0.05),
        Q('A rate of 120 percent means what?', 'A mistake, since actions cannot exceed visits here', ('A great result', 'impossible'),
          ('A normal result for most small business websites', 'impossible'), ('A tax', 'no'), 'Check reasonableness.'),
        Q('Which is the formula for conversion rate?', 'Actions / visits', ('Visits / actions', 'reversed'), ('Actions - visits', 'no'),
          ('Actions + visits', 'no'), 'Part over whole.'),
    ], why='A learner who misses MAIN may not compute a rate; this practices part over whole as a percent.')],
    F1=sec('Apply it: compare pages and sources', MEASURE, [
        Q('Page A: 900 visits, 18 orders. Page B: 400 visits, 16 orders. Which converts better?', 'B, at 4 percent', ('A, at 2 percent', 'A is lower'),
          ('A, because it has more visits', 'visits are not conversion'), ('They are equal', 'they differ'),
          'A: 2 percent; B: 4 percent.', calc=lambda: 18 / 900 == 0.02 and 16 / 400 == 0.04),
        Q('Visitors from local listings convert at 6 percent; from social media at 1 percent. With 300 visits from each, how '
          'many more actions come from listings?', '15', ('18', 'listing total'), ('3', 'social total'), ('5', 'percent difference'),
          '18 - 3 = 15.', calc=lambda: round(0.06 * 300) - round(0.01 * 300) == 15),
        Q('An owner changed the headline, photos and price on the same day, and orders rose. What can she conclude?', 'Orders rose, but she cannot tell which change caused it',
          ('The new headline alone caused the whole increase', 'cannot tell'), ('The photos alone caused it', 'cannot tell'),
          ('Nothing changed at all', 'orders rose'), 'Multiple changes blur the cause.'),
        Q('A store wants 50 orders a month and converts at 2.5 percent. How many visits does it need?', '2,000',
          ('1,250', 'used 4 percent'), ('125', 'misplaced decimal'), ('20,000', 'misplaced decimal'), '50 / 0.025 = 2,000.',
          calc=lambda: round(50 / 0.025) == 2000),
        Q('Which number best shows whether the site is helping the business?', 'Bookings made through the site', ('Total page views', 'not actions'),
          ('Number of images', 'not actions'), ('Length of the homepage in words', 'not actions'), 'Useful actions matter most.'),
    ]),
    F2=sec('Handle the complications: misleading numbers', MEASURE, [
        Q('Visits doubled after a viral post, but orders stayed the same. What happened to conversion rate?', 'It was cut in half',
          ('It doubled along with visits', 'orders unchanged'), ('It stayed the same', 'visits doubled'), ('It tripled', 'no'),
          'Same actions over twice the visits.', calc=lambda: (10 / 200) == (10 / 100) / 2),
        Q('A test ran for one day with 30 visits. One version got 2 orders, the other 1. What is the problem?', 'The sample is too small to trust',
          ('Version A is proven better forever', 'too small'), ('Version B should be deleted now', 'premature'),
          ('Tests always need only one day', 'not true'), 'Small samples mislead.'),
        Q('A tracking code was installed twice, so every visit counts double. Reported conversion is 1.5 percent. What is the true '
          'rate?', '3 percent', ('1.5 percent', 'uncorrected'), ('0.75 percent', 'wrong direction'), ('6 percent', 'doubled twice'),
          'Halving visits doubles the rate.', calc=lambda: 1.5 * 2 == 3),
        Q('Sign-ups rose but almost none of them buy. What should the owner measure too?', 'How many sign-ups become paying customers',
          ('Only the sign-up count each week and month', 'incomplete'), ('Only page views', 'incomplete'), ('Nothing else', 'incomplete'),
          'Follow actions to sales.'),
        Q('Which statement is accurate?', 'Useful actions and their rate tell more than visits alone.',
          ('Visits are the only number that matters.', 'not true'), ('Conversion rates can exceed 100 percent.', 'not here'),
          ('Changing many things at once shows the cause clearly.', 'blurs cause'), 'Measure what matters.'),
    ]))

# ------------------------------------------------------------------ Set 84: Amazon case
AMZ = ('Documented history (HistoryLink, a Washington State history encyclopedia): Amazon.com launched in July 1995 as an '
       'online bookstore, started from a rented house in Bellevue, Washington. Jeff Bezos chose books from a short list '
       'of possible products because of the huge number of titles in print and broad demand. Lesson drawn by this course '
       '(an interpretation): start online with one focused category that suits the web\'s strengths, such as offering '
       'more choice than a physical store. One success story does not guarantee the same result for another business.')

s84 = SET('ENT.CASE.06',
    M=sec('Apply a documented early decision: start online with one focused category', AMZ, [
        Q('According to the passage, what did Amazon.com sell when it launched?', 'Books',
          ('Groceries, clothing and electronics all at once', 'not at launch'),
          ('Streaming movies and music subscriptions', 'not at launch'),
          ('Cloud computing services for businesses', 'not at launch'), 'It launched as an online bookstore.'),
        Q('Why does the passage say books were chosen?', 'Many titles in print and broad demand',
          ('Books were the only product that could be shipped', 'not stated'),
          ('Bezos had never read any other kind of product', 'not stated'),
          ('Books had no competition anywhere', 'not stated'), 'The number of titles and demand.'),
        Q('Where was the company started?', 'A rented house in Bellevue, Washington', ('A large office tower in New York', 'not stated'),
          ('A university laboratory in California', 'not stated'), ('A shopping mall in Seattle', 'not stated'),
          'The passage names a rented house in Bellevue.'),
        Q('Which lesson does this course draw?', 'Start with one focused category that suits the web',
          ('Always sell every product on the first day', 'opposite'), ('Avoid the internet for new businesses', 'opposite'),
          ('Choose products with the fewest options', 'opposite'), 'Focus plus a web advantage.'),
        Q('Which statement about this case is accurate?', 'It is one example and does not guarantee the same result.',
          ('It proves any online bookstore will become huge.', 'one case proves nothing'),
          ('It shows every business must start in a house.', 'surface detail'),
          ('It shows focus never matters.', 'opposite'), 'Learn the principle, not a promise.'),
    ]),
    B=[cs('Why the web suited a huge catalog', 'A physical bookstore can hold only so many books on its shelves. A website is not '
          'limited by shelf space: it can list far more titles than any single store. That is one way to see why books fit '
          'the web well. The documented facts are the launch, the category and the reason given; the explanation of shelf '
          'space is this course\'s way of making the reason concrete.', [
        Q('What limits a physical bookstore\'s selection?', 'Shelf space', ('The weather outside', 'no'), ('The owner\'s age', 'no'),
          ('The color of the walls', 'no'), 'Shelves are limited.'),
        Q('Why can a website list more titles?', 'It is not limited by shelf space', ('It sells only one book', 'no'),
          ('It has no customers', 'no'), ('It never ships anything to anyone', 'no'), 'Online catalogs can be large.'),
        Q('"Amazon launched as an online bookstore" is which kind of statement?', 'Documented fact', ('Course interpretation', 'it is documented'),
          ('A rumor', 'sourced'), ('A promise', 'no'), 'It is recorded.'),
        Q('The shelf-space explanation is which kind of statement?', 'The course\'s explanation', ('A documented quote from Bezos', 'not a quote'),
          ('A legal rule', 'no'), ('A tax fact', 'no'), 'It is an interpretation to make the reason concrete.'),
        Q('What matched books to the web, according to the passage?', 'Many titles and broad demand', ('Low weight of books only', 'not stated'),
          ('Free shipping', 'not stated'), ('No taxes', 'not stated'), 'The documented reason.'),
    ], why='A learner who misses MAIN may not see why a category fits the web; shelf space makes the reason concrete.')],
    F1=sec('Apply it: pick a focused first category', AMZ, [
        Q('Kai wants to sell online and can afford one category. Which choice best applies the lesson?', 'Rare houseplant seeds with many varieties hard to find locally',
          ('Every product a big department store sells', 'not focused'), ('Fresh milk that must arrive cold within an hour of ordering', 'poor fit for shipping'),
          ('A single common item sold in every corner shop', 'no web advantage'), 'Focus where the web offers more choice.'),
        Q('A local shop stocks 200 knitting patterns; an online catalog could list 5,000. How many more patterns online?', '4,800',
          ('5,200', 'added'), ('25', 'divided'), ('200', 'local count'), '5,000 - 200 = 4,800.', calc=lambda: 5000 - 200 == 4800),
        Q('Which question tests whether a category suits online selling?', 'Does the web let us offer something stores cannot, like more choice?',
          ('Is the logo the right shade of orange for an online store?', 'irrelevant'), ('Is the owner\'s house large?', 'surface detail'),
          ('Can we sell everything on day one?', 'not focused'), 'Look for a web advantage.'),
        Q('A seller plans to start with 12 unrelated product types. What does the lesson suggest?', 'Start with one focused category first',
          ('Add even more product types for safety', 'less focus'), ('Avoid selling online', 'opposite'), ('Sell only in person forever', 'opposite'),
          'Focus first.'),
        Q('Which detail is documented, not interpreted?', 'Amazon.com launched in July 1995', ('Focus guarantees success', 'interpretation, overstated'),
          ('Every founder should start in a house', 'not documented'), ('Books are the best product for anyone', 'not documented'),
          'Dates and facts are documented.'),
    ]),
    F2=sec('Handle the complications: copying surface details', AMZ, [
        Q('Someone says, "Amazon started with books, so I should sell books online." What is the flaw?', 'The lesson is the reasoning, not the exact product',
          ('There is no flaw, because books always work online', 'not guaranteed'), ('Books are illegal to sell online', 'not true'),
          ('Amazon never sold books', 'it did'), 'Apply the principle to your situation.'),
        Q('A category has many options online but very high shipping costs compared with the price. What should a founder check?',
          'Whether costs still allow a profit', ('Nothing; more options always win', 'costs matter'), ('Only the logo', 'irrelevant'),
          ('Only the founder\'s location', 'not enough'), 'Economics still matter.'),
        Q('Big competitors already sell your planned category online. What might still help a new seller?', 'A narrower niche they serve poorly',
          ('Copying them exactly', 'no advantage'), ('Selling at a loss forever to win buyers', 'unsustainable'), ('Giving up immediately', 'premature'),
          'Find a focused gap.'),
        Q('Which claim goes beyond what the passage documents?', '"Starting in a house caused Amazon\'s success."', ('"It launched in 1995."', 'documented'),
          ('"It began as a bookstore."', 'documented'), ('"Books had a huge number of titles in print."', 'documented'), 'Location is a detail, not a proven cause.'),
        Q('Which statement is accurate?', 'The case suggests focus and fit; other businesses must test their own markets.',
          ('Every online store that starts focused eventually becomes a giant.', 'not true'), ('Focus guarantees success.', 'not guaranteed'),
          ('Starting small never works.', 'not true'), 'Test your own situation.'),
    ]))

SETS = [s77, s78, s79, s80, s81, s82, s83, s84]
