"""Entrepreneurship sets 113-124: Foundation 14 (risk and agreements) and 15 (getting help).
Insurance prices and pay rates are practice assumptions. Names are fictional."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 113: insurance categories and exclusions
INS = ('Insurance moves some financial risk to an insurer in exchange for a PREMIUM (the price of the policy). Common '
       'business categories include GENERAL LIABILITY (injuries or property damage to others, such as a customer '
       'slipping), PROFESSIONAL LIABILITY (mistakes in advice or services), PROPERTY (your equipment and inventory), and '
       'COMMERCIAL AUTO. Every policy has LIMITS (the most it pays), a DEDUCTIBLE (what you pay first), and EXCLUSIONS '
       '(what it does not cover). Read the exclusions and ask a licensed agent which coverage fits your activities.')

s113 = SET('ENT.RISK.01',
    M=sec('Match common insurance categories to risks and read limits and exclusions', INS, [
        Q('A customer slips on a wet floor in the shop. Which category usually applies?', 'General liability',
          ('Professional liability for advice mistakes', 'not an advice error'), ('Commercial auto coverage for vehicles', 'no vehicle'),
          ('Property coverage for the owner\'s equipment', 'not the owner\'s property'), 'Injuries to others.'),
        Q('A bookkeeper\'s error costs a client money. Which category usually applies?', 'Professional liability',
          ('General liability for slips and falls', 'not an injury'), ('Property coverage for inventory', 'not property'),
          ('Commercial auto coverage for deliveries', 'no vehicle'), 'Service mistakes.'),
        Q('What is a deductible?', 'The amount you pay before the insurer pays', ('The most the insurer will ever pay', 'that is a limit'),
          ('The yearly price of the policy itself', 'that is the premium'), ('A list of things the policy excludes', 'exclusions'),
          'You pay first.'),
        Q('What are exclusions?', 'Situations the policy does not cover', ('Discounts for paying the premium early', 'no'),
          ('Extra benefits added for free each year', 'no'), ('The insurer\'s office locations', 'no'), 'Read them carefully.'),
        Q('A claim is 5,000 dollars with a 1,000-dollar deductible. Within limits, about how much does the insurer pay?', '4,000 dollars',
          ('5,000 dollars', 'ignores deductible'), ('1,000 dollars', 'the deductible'), ('6,000 dollars', 'added'),
          '5,000 - 1,000 = 4,000.', calc=lambda: 5000 - 1000 == 4000),
    ]),
    B=[cs('An umbrella with holes in certain places', 'Insurance is like an umbrella you pay for. It keeps you dry from some '
          'kinds of rain, but it is only so big (the limit), you still get a little wet before it opens (the deductible), and '
          'it has a few holes in known places (the exclusions). Before a storm, you want to know where the holes are, not '
          'discover them while you are getting soaked.', [
        Q('The size of the umbrella stands for what?', 'The policy limit', ('The deductible you pay first', 'no'),
          ('The premium price of the policy', 'no'), ('The insurer\'s name and logo', 'no'), 'Maximum coverage.'),
        Q('Getting a little wet before it opens is like what?', 'The deductible', ('The policy limit', 'no'),
          ('An exclusion in the policy', 'no'), ('A refund from the insurer', 'no'), 'You pay first.'),
        Q('Holes in known places are like what?', 'Exclusions', ('Discounts', 'no'), ('Premiums paid monthly', 'no'),
          ('Extra coverage for free', 'no'), 'Not covered.'),
        Q('When should you learn where the holes are?', 'Before the storm', ('During the storm while getting soaked', 'too late'),
          ('Never; holes do not matter', 'they do'), ('Only after filing a claim', 'too late'), 'Read first.'),
        Q('Paying for the umbrella is like what?', 'The premium', ('The deductible', 'no'), ('An exclusion', 'no'),
          ('A claim payment', 'no'), 'The price of coverage.'),
    ], why='A learner who misses MAIN may confuse limits, deductibles and exclusions; an umbrella shows each part.')],
    F1=sec('Apply it: choose coverage for activities', INS, [
        Q('A dog walker takes dogs to parks. Which coverage is most relevant to ask about?', 'Liability that covers dogs in her care',
          ('Only property coverage for her phone', 'misses main risk'), ('Only commercial auto for a truck she does not have', 'no truck'),
          ('No coverage, since dogs are friendly', 'risky'), 'Match risk to activity.'),
        Q('A policy has a 10,000-dollar limit. A covered claim is 14,000 dollars with a 500-dollar deductible. What might the owner pay?',
          '4,000 dollars', ('500 dollars', 'deductible only'), ('4,500 dollars', 'added the deductible on top'), ('14,000 dollars', 'all'),
          'After the 500 deductible the insurer would owe 13,500 but pays at most 10,000; the owner pays 14,000 - 10,000 = 4,000.',
          calc=lambda: 14000 - min(14000 - 500, 10000) == 4000),
        Q('Policy A: 600 dollars a year, 2,000-dollar deductible. Policy B: 900 dollars a year, 500-dollar deductible. If one claim '
          'happens, which has lower total cost to the owner that year?', 'B, at 1,400 dollars', ('A, at 2,600 dollars', 'A is higher'),
          ('They are equal', 'they differ'), ('A, at 600 dollars', 'ignores deductible'), 'A: 2,600; B: 1,400.',
          calc=lambda: 600 + 2000 == 2600 and 900 + 500 == 1400),
        Q('With no claim that year, which policy costs less?', 'A, at 600 dollars', ('B, at 900 dollars', 'B is higher'),
          ('They are equal', 'differ'), ('B, at 500 dollars', 'deductible not paid'), 'Only premiums are paid.', calc=lambda: 600 < 900),
        Q('A baker\'s policy excludes food poisoning claims. What should she do?', 'Ask an agent about coverage for that risk',
          ('Assume it is covered anyway because she has a policy', 'excluded'), ('Stop reading exclusions', 'risky'), ('Hide the exclusion from customers', 'irrelevant'),
          'Fill the gap.'),
    ]),
    F2=sec('Handle the complications: gaps and claims', INS, [
        Q('An owner starts offering a new service not listed on her policy. What should she do?', 'Tell her agent and check whether it is covered',
          ('Assume the old policy covers everything new', 'may not'), ('Cancel all insurance', 'risky'), ('Hide the new service', 'risky'),
          'Coverage depends on activities.'),
        Q('A cheaper policy has many more exclusions. What should the owner compare?', 'What is actually covered, not only the price',
          ('Only the price, since cheaper is always better', 'misses gaps'), ('Only the insurer\'s logo color', 'irrelevant'),
          ('Only how fast the website loads', 'irrelevant'), 'Coverage matters.'),
        Q('A claim is denied because of an exclusion the owner never read. What lesson applies?', 'Read exclusions before you need the policy',
          ('Insurance never pays anything', 'not true'), ('Exclusions are always unfair, so they can be ignored', 'not necessarily'),
          ('Claims should never be filed', 'not true'), 'Know the policy.'),
        Q('Premiums rose from 800 to 920 dollars. What is the percent increase?', '15 percent', ('120 percent', 'dollar change'),
          ('13 percent', 'used new price'), ('8 percent', 'guessed'), '120 / 800 = 0.15.', calc=lambda: (920 - 800) / 800 == 0.15),
        Q('Which statement is accurate?', 'Insurance covers specific risks within limits.',
          ('One policy covers every possible business risk at once.', 'not true'), ('Deductibles are paid by the insurer.', 'reversed'),
          ('Exclusions never matter.', 'they do'), 'Fit matters.'),
    ]))

# ------------------------------------------------------------------ Set 114: personal and home policy limits
HOME = ('Many owners assume their HOMEOWNERS or RENTERS insurance covers a home business. Often it does not, or covers '
        'very little: business equipment and inventory may have low limits, and injuries to customers visiting the home '
        'for business may be excluded. A PERSONAL AUTO policy may not cover driving for business deliveries. Ask your '
        'insurer directly: "Does this policy cover my business activities?" Options can include a home-business add-on '
        '(often called an endorsement) or a separate business policy.')

s114 = SET('ENT.RISK.02',
    M=sec('Recognize where personal and home policies stop covering business use', HOME, [
        Q('Does a homeowners policy always cover a home business?', 'Not necessarily; coverage may be limited or excluded',
          ('Yes, every home policy covers any business fully', 'not true'),
          ('Yes, but only if the business is profitable', 'not the test'),
          ('No home policy can ever be changed', 'endorsements exist'), 'Check the policy.'),
        Q('Which risk is often excluded under a home policy?', 'Injuries to customers visiting for business',
          ('Damage to the home from a covered fire', 'usually covered'), ('Theft of the family\'s personal TV', 'usually covered'),
          ('A broken window from a storm', 'usually covered'), 'Business visitors may be excluded.'),
        Q('What may a personal auto policy not cover?', 'Driving for business deliveries', ('Driving to the grocery store', 'personal'),
          ('Driving to visit family', 'personal'), ('Driving to a doctor visit', 'personal'), 'Business use may differ.'),
        Q('What is an endorsement?', 'An add-on that changes a policy\'s coverage', ('A celebrity promoting the insurer', 'pun'),
          ('A signature on the business license', 'no'), ('A tax deduction for premiums', 'no'), 'Policy add-on.'),
        Q('What question should an owner ask the insurer?', '"Does this policy cover my business activities?"',
          ('"What color is your company logo?"', 'irrelevant'), ('"Can I skip reading the policy?"', 'risky'),
          ('"Are all claims always paid instantly, every time?"', 'not the key question'), 'Ask directly.'),
    ]),
    B=[cs('A family car used as a taxi', 'Imagine using the family car to drive paying passengers. The family car insurance was '
          'priced for school runs and grocery trips, not for business driving all day. The insurer may say the business use '
          'was never part of the deal. Home and personal policies work the same way: they were priced for personal life, so '
          'business activities may fall outside them.', [
        Q('Why might the car insurer refuse a taxi claim?', 'Business driving was not part of the policy', ('The car was red', 'irrelevant'),
          ('Passengers were too polite', 'irrelevant'), ('The trip was too short to count as driving', 'not the reason'), 'Different use.'),
        Q('What was the family policy priced for?', 'Personal trips like school runs', ('All-day paid driving', 'no'),
          ('Racing at a track', 'no'), ('Deliveries for a company all day', 'no'), 'Personal use.'),
        Q('A home policy is like what in this picture?', 'The family car policy', ('A taxi company policy', 'no'),
          ('A racing license', 'no'), ('A bus ticket', 'no'), 'Priced for personal life.'),
        Q('What could help the taxi driver?', 'A policy that covers business driving', ('A new car color', 'no'),
          ('Driving faster', 'no'), ('Hiding the business use from the insurer', 'dishonest'), 'Match coverage to use.'),
        Q('What is the main lesson?', 'Personal policies may not cover business activities', ('Insurance never pays', 'no'),
          ('All policies are the same', 'no'), ('Business use is always covered by personal policies', 'no'), 'Check business use.'),
    ], why='A learner who misses MAIN may assume personal coverage stretches to business; a family car used as a taxi shows why not.')],
    F1=sec('Apply it: check a home-business setup', HOME, [
        Q('A home baker stores 3,000 dollars of equipment. Her home policy covers business property up to 500 dollars. How much is '
          'uncovered?', '2,500 dollars', ('500 dollars', 'covered part'), ('3,000 dollars', 'all'), ('3,500 dollars', 'added'),
          '3,000 - 500 = 2,500.', calc=lambda: 3000 - 500 == 2500),
        Q('A tutor has students visit her home. What should she ask her insurer about?', 'Liability for business visitors',
          ('Only coverage for her personal jewelry', 'misses the risk'), ('Only coverage for her car stereo', 'irrelevant'),
          ('Nothing, since students are young', 'risk remains'), 'Visitors are a business risk.'),
        Q('A florist uses her personal car for weddings deliveries. What should she check?', 'Whether her auto policy covers business deliveries',
          ('Only the car\'s fuel economy', 'irrelevant'), ('Only the flowers\' prices', 'irrelevant'), ('Nothing, because cars are always covered for any use', 'not always'),
          'Business driving may differ.'),
        Q('An endorsement costs 150 dollars a year and covers 5,000 dollars of business equipment. What is the cost per 1,000 dollars '
          'of coverage?', '30 dollars', ('150 dollars', 'total'), ('5 dollars', 'count'), ('750 dollars', 'multiplied'),
          '150 / 5 = 30.', calc=lambda: 150 / 5 == 30),
        Q('Which owner most needs to ask about coverage?', 'One with customers visiting and inventory at home',
          ('One who writes a blog for fun with no customers', 'no business risk'), ('One with no business at all', 'none'),
          ('One who only buys personal groceries', 'none'), 'More exposure, more need.'),
    ]),
    F2=sec('Handle the complications: assumptions and honesty', HOME, [
        Q('An owner does not tell her insurer about her home business, hoping to keep premiums low. What is the risk?', 'A business-related claim could be denied',
          ('No risk, because insurers never ask about business use', 'they can deny'), ('Premiums will drop to zero', 'no'), ('The business becomes an LLC', 'no'),
          'Undisclosed use can void coverage.'),
        Q('A renter thinks her landlord\'s insurance covers her business inventory. What should she know?', 'The landlord\'s policy usually covers only the building',
          ('Landlords always insure their tenants\' business inventory', 'not usually'), ('Inventory never needs insurance', 'risky'),
          ('Renters cannot get insurance', 'they can'), 'Tenants insure their own property.'),
        Q('A home business grows and now has a part-time helper working there. What should the owner review?', 'Whether her coverage still fits, including for workers',
          ('Nothing, because coverage never needs review once bought', 'risky'), ('Only the helper\'s favorite snacks', 'irrelevant'),
          ('Only the logo design', 'irrelevant'), 'Changes require review.'),
        Q('A separate business policy costs 700 dollars; a home endorsement costs 200 but covers less. What should guide the choice?',
          'Which risks each covers for her real activities', ('Only the lowest price, whatever the coverage', 'may miss risks'),
          ('Only which agent is friendlier', 'not enough'), ('Only the policy\'s page count', 'irrelevant'), 'Fit to risk.'),
        Q('Which statement is accurate?', 'Personal policies may not cover business use unless confirmed.',
          ('Home policies cover all home businesses automatically.', 'not true'), ('Personal auto always covers deliveries.', 'not always'),
          ('Insurers never need to know about business use.', 'they do'), 'Confirm coverage.'),
    ]))

# ------------------------------------------------------------------ Set 115: what a written agreement covers
AGREE = ('A written AGREEMENT (contract) records what both sides promised, so there is less room for "I thought you meant..." '
         'A simple service or sales agreement usually covers: who the parties are; what will be delivered (scope); price and '
         'payment terms; timeline; what happens if plans change, including cancellation and refunds; who owns the finished '
         'work; and how disagreements will be handled. Use plain words, keep a signed copy, and have important or unusual '
         'agreements reviewed by an attorney.')

s115 = SET('ENT.RISK.03',
    M=sec('Identify the core parts of a simple written agreement', AGREE, [
        Q('Why put an agreement in writing?', 'It records what both sides promised',
          ('It makes any promise automatically legal everywhere', 'overstated'), ('It replaces the need to do the work', 'no'),
          ('It hides the price from the customer', 'opposite'), 'Shared record.'),
        Q('Which item belongs in a simple service agreement?', 'Who owns the finished work', ('The owner\'s favorite color', 'irrelevant'),
          ('The customer\'s home décor style', 'irrelevant'), ('A list of competitors', 'irrelevant'), 'Ownership matters.'),
        Q('What is "scope" in an agreement?', 'What will be delivered', ('The price per hour only', 'part of price'),
          ('The name of the business bank', 'irrelevant'), ('The length of the document', 'irrelevant'), 'The work included.'),
        Q('Who should review important or unusual agreements?', 'An attorney', ('A social media follower', 'not qualified'),
          ('The customer\'s friend', 'not independent'), ('A graphic designer', 'not legal'), 'Legal review.'),
        Q('What should be kept after signing?', 'A signed copy', ('Nothing, once the work starts', 'needed later'),
          ('Only the first page', 'incomplete'), ('Only a photo of the pen', 'irrelevant'), 'Keep records.'),
    ]),
    B=[cs('A written plan for a group trip', 'Friends planning a trip write down who is coming, where they are going, what it '
          'costs, who pays for what, what happens if someone cancels, and how they will decide if they disagree. Without the '
          'note, everyone remembers it differently. A business agreement is the written plan for a job, so both sides '
          'remember the same thing.', [
        Q('Why write down the trip plan?', 'So everyone remembers the same thing', ('To make the trip longer', 'no'),
          ('To avoid going', 'no'), ('Because notes are required by law', 'not the reason'), 'Shared memory.'),
        Q('"Who pays for what" is like which part of an agreement?', 'Price and payment terms', ('Scope of work', 'no'),
          ('Ownership of the work', 'no'), ('The parties\' names', 'no'), 'Money terms.'),
        Q('"What happens if someone cancels" is like which part?', 'Cancellation and refunds', ('Timeline', 'no'), ('Scope', 'no'),
          ('Ownership of the work', 'no'), 'Changes in plans.'),
        Q('"How to decide if they disagree" is like which part?', 'Handling disagreements', ('Payment terms and dates', 'no'),
          ('Scope', 'no'), ('Parties', 'no'), 'Dispute process.'),
        Q('"Who is coming" is like which part?', 'The parties', ('The price', 'no'), ('The deliverables', 'no'), ('The deadline', 'no'),
          'Who is involved.'),
    ], why='A learner who misses MAIN may not see what an agreement records; a written trip plan is familiar.')],
    F1=sec('Apply it: find gaps in a draft agreement', AGREE, [
        Q('A web design agreement lists price and timeline but not what happens if the client cancels halfway. What should be added?',
          'Cancellation and refund terms', ('A longer company history', 'irrelevant'), ('The designer\'s hobbies', 'irrelevant'),
          ('More pictures of websites', 'irrelevant'), 'Cover changes.'),
        Q('Which clause best describes scope?', '"Design 5 pages: Home, About, Services, Gallery, Contact."', ('"Make a nice website."', 'vague'),
          ('"Do whatever is needed on the website forever, for one price."', 'unlimited'), ('"Web stuff."', 'vague'), 'Specific deliverables.'),
        Q('The agreement says 2,400 dollars, half due at signing. How much is due at signing?', '1,200 dollars', ('2,400 dollars', 'all'),
          ('600 dollars', 'quarter'), ('1,000 dollars', 'guessed'), '2,400 / 2 = 1,200.', calc=lambda: 2400 / 2 == 1200),
        Q('The draft says nothing about who owns the final logo files. What risk does this create?', 'A later dispute about who may use the files',
          ('No risk; ownership is always obvious', 'not always'), ('The logo will look worse', 'irrelevant'),
          ('The price automatically doubles', 'no'), 'Clarify ownership.'),
        Q('Which agreement most needs attorney review?', 'A 3-year exclusive supply deal with large penalties', ('A one-time 40-dollar flyer design for a yard sale', 'low stakes'),
          ('A note confirming a coffee meeting', 'not a contract'), ('A thank-you card', 'not a contract'), 'High stakes.'),
    ]),
    F2=sec('Handle the complications: verbal changes and templates', AGREE, [
        Q('A client verbally adds two pages after signing. What should happen?', 'Put the change in writing with any new price and date',
          ('Do it free and say nothing', 'scope creep'), ('Refuse to discuss changes ever', 'inflexible'),
          ('Change the original contract without telling the client', 'improper'), 'Written changes.'),
        Q('A template from another country uses legal terms the owner does not understand. What should she do?', 'Adapt it to her situation and get it reviewed',
          ('Sign it as is', 'risky'), ('Add more confusing terms', 'worse'), ('Never use written agreements again for any job', 'risky'), 'Fit and review.'),
        Q('Both parties signed different versions. What problem arises?', 'It is unclear which terms apply', ('None; both are valid', 'conflict'),
          ('The price becomes zero', 'no'), ('The work is finished automatically', 'no'), 'Use one final version.'),
        Q('An agreement has no plan for disagreements. A dispute arises. What would have helped?', 'A clause on how disputes are handled',
          ('A bigger font', 'irrelevant'), ('More signatures on the last page', 'not a process'), ('A longer deadline', 'not a process'), 'Dispute process.'),
        Q('Which statement is accurate?', 'Clear written agreements prevent many misunderstandings.',
          ('Written agreements cause most disputes.', 'not true'), ('Verbal promises are always enough.', 'risky'),
          ('Online templates fit every situation without changes.', 'not true'), 'Write it down.'),
    ]))

# ------------------------------------------------------------------ Set 116: signed documents and customer information
CUSTINFO = ('Keep SIGNED DOCUMENTS (contracts, waivers, change orders) where you can find them, with a backup. Collect only '
            'the CUSTOMER INFORMATION you need, such as name, contact details and what they ordered. Protect it: limit who '
            'can see it, do not leave lists in public places, never store full card numbers yourself (let the payment '
            'processor handle them), and delete what you no longer need. If you promise privacy in a policy, keep that '
            'promise. Some kinds of data, such as health details, have special rules.')

s116 = SET('ENT.RISK.04',
    M=sec('Keep signed documents and handle customer information carefully', CUSTINFO, [
        Q('What customer information should be collected?', 'Only what the business needs', ('Everything possible, just in case', 'excess'),
          ('Customers\' passwords to other sites', 'never'), ('Customers\' full card numbers in a notebook', 'never'), 'Data minimization.'),
        Q('Who should store full card numbers?', 'The payment processor', ('The owner in a spreadsheet', 'risky'),
          ('A helper in a notebook', 'risky'), ('A shared email folder', 'risky'), 'Let processors handle cards.'),
        Q('What should happen to data no longer needed?', 'Delete it safely', ('Keep it forever in a public folder', 'risky'),
          ('Post it online for safekeeping', 'harmful'), ('Sell it to anyone', 'improper'), 'Reduce risk.'),
        Q('If a business promises privacy in its policy, what must it do?', 'Keep that promise', ('Change it secretly', 'deceptive'),
          ('Ignore it when convenient', 'deceptive'), ('Remove the policy without notice', 'improper'), 'Promises bind.'),
        Q('Why keep a backup of signed documents?', 'So they are not lost if the original is damaged', ('To share them publicly', 'no'),
          ('Because originals are illegal', 'no'), ('To change their terms later without asking', 'no'), 'Protection.'),
    ]),
    B=[cs('Holding a friend\'s spare key', 'If a friend gives you their spare key, you keep it safe, you do not lend it to others, '
          'and you give it back when you no longer need it. Customer information is like that key: customers trust you with '
          'it. Take only what you need, protect it, do not share it carelessly, and let go of it when it is no longer '
          'needed.', [
        Q('Customer information is like what?', 'A friend\'s spare key you were trusted with', ('Your own property to sell to others', 'no'),
          ('Public information for anyone', 'no'), ('Trash to throw anywhere', 'no'), 'Held in trust.'),
        Q('What do you do with the key?', 'Keep it safe', ('Lend it to strangers', 'no'), ('Copy it for everyone', 'no'),
          ('Leave it in the door', 'no'), 'Protect it.'),
        Q('When do you give the key back?', 'When you no longer need it', ('Never', 'no'), ('Only if the friend asks twice', 'no'),
          ('When you lose it', 'no'), 'Let go of unneeded data.'),
        Q('Taking only the key you need is like what?', 'Collecting only needed data', ('Collecting everything possible', 'no'),
          ('Selling data', 'no'), ('Posting data', 'no'), 'Minimization.'),
        Q('Why do you protect the key?', 'Your friend trusted you with it', ('It is shiny', 'no'), ('Keys are rare', 'no'),
          ('The law says keys are gold', 'no'), 'Trust.'),
    ], why='A learner who misses MAIN may treat customer data casually; a friend\'s spare key shows it is held in trust.')],
    F1=sec('Apply it: review data habits', CUSTINFO, [
        Q('A shop writes customer card numbers on order slips "for refunds." What should change?', 'Stop writing card numbers; refund through the processor',
          ('Write them more neatly', 'still risky'), ('Keep them in a locked drawer forever, just in case', 'still risky'),
          ('Email them to staff', 'worse'), 'Never store card numbers yourself.'),
        Q('An order form asks for birthday, income and favorite color for a candle purchase. What should change?', 'Remove questions the business does not need',
          ('Add more questions', 'worse'), ('Make all of the questions required to order', 'worse'), ('Sell the answers', 'improper'), 'Collect only what is needed.'),
        Q('A signed waiver is needed for a climbing class. Where should it be kept?', 'In an organized file with a backup', ('In the instructor\'s car glove box', 'risky'),
          ('Thrown away after class', 'lost proof'), ('Posted on social media', 'privacy'), 'Organized and backed up.'),
        Q('A list of 200 customers is left on a café table. What is the problem?', 'Customer information could be seen by strangers',
          ('Nothing, because customer lists are public anyway', 'not public'), ('The list will get longer', 'irrelevant'), ('Coffee will spill', 'not the main issue'),
          'Protect data.'),
        Q('An old customer list has 400 people, of whom 150 have not bought in 6 years and are no longer needed. How many records remain if those are deleted?',
          '250', ('400', 'none deleted'), ('150', 'deleted'), ('550', 'added'), '400 - 150 = 250.', calc=lambda: 400 - 150 == 250),
    ]),
    F2=sec('Handle the complications: special data and mistakes', CUSTINFO, [
        Q('A fitness coach collects clients\' health conditions. What should she check?', 'Whether special rules apply to that kind of data',
          ('Nothing, because health data has no special rules', 'may have rules'), ('Only her logo', 'irrelevant'), ('Only her prices', 'irrelevant'),
          'Sensitive data.'),
        Q('A helper emails the customer list to the wrong person. What should the owner do?', 'Ask for deletion, review what was shared, follow notice rules',
          ('Ignore it', 'risky'), ('Blame the customers', 'unfair'), ('Send the list to more people so it seems normal and routine', 'worse'), 'Respond responsibly.'),
        Q('A privacy policy says "we never share your data," but the owner plans to share emails with a partner. What should she do?', 'Not share without updating the policy and getting consent',
          ('Share anyway', 'breaks promise'), ('Share secretly', 'deceptive'), ('Delete the privacy policy quietly first, then share', 'deceptive'),
          'Keep promises.'),
        Q('A signed contract cannot be found during a dispute. What habit would have helped?', 'Filing signed documents with a backup',
          ('Remembering the terms', 'unreliable'), ('Asking the client to remember the terms', 'unreliable'), ('Writing a new contract now', 'not the original'),
          'Records matter.'),
        Q('Which statement is accurate?', 'Collect only needed data, protect it and keep signed copies.',
          ('More customer data is always better.', 'more risk'), ('Card numbers are safe in spreadsheets.', 'not safe'),
          ('Privacy promises can be ignored later if plans change.', 'not true'), 'Care and minimization.'),
    ]))

# ------------------------------------------------------------------ Set 117: permission for images, music, code, names
RIGHTS = ('Things you find online are usually owned by someone. Using another person\'s PHOTO, MUSIC, ARTWORK, written text '
          'or software CODE in your business generally needs PERMISSION, a LICENSE (written terms of use), or a source that '
          'clearly allows your kind of use. "I found it on Google" is not permission. Read license terms: some allow only '
          'personal use, or require credit. Using another business\'s NAME or LOGO in a way that confuses customers can '
          'infringe trademark rights. Registering a business name, DBA or domain is not the same as trademark rights.')

s117 = SET('ENT.RISK.05',
    M=sec('Get permission or a license for images, music, code and names', RIGHTS, [
        Q('Is "I found it on Google" permission to use a photo?', 'No', ('Yes, anything online is free to use', 'not true'),
          ('Yes, if the photo is small', 'not true'), ('Yes, for businesses only', 'not true'), 'Finding is not permission.'),
        Q('What is a license?', 'Written terms that say how something may be used', ('A driver\'s permit for driving the delivery vans', 'different meaning'),
          ('A business tax ID number', 'no'), ('A logo design file', 'no'), 'Terms of use.'),
        Q('A license allows "personal use only." Can a business use it in ads?', 'Not under that license', ('Yes, ads are personal', 'no'),
          ('Yes, if the ad is short', 'no'), ('Yes, with a smaller image', 'no'), 'Follow terms.'),
        Q('Does registering a DBA give trademark rights?', 'No, they are separate', ('Yes, nationwide automatically', 'no'),
          ('Yes, but only for logos', 'no'), ('Yes, for domains too', 'no'), 'Separate processes.'),
        Q('Which use of another business\'s logo is risky?', 'Using it so customers think you are connected', ('Not using it at all', 'safe'),
          ('Referring to it in a short factual review', 'generally different'), ('Designing your own different logo', 'safe'), 'Confusion risk.'),
    ]),
    B=[cs('Borrowing a neighbor\'s ladder', 'If a neighbor\'s ladder is leaning against their house, you would not just take it '
          'because you can see it. You would ask, and maybe agree on when to return it. Photos, music and code online are like '
          'that ladder: being able to see them does not mean you may use them. A license is the neighbor\'s "yes" with the '
          'rules attached.', [
        Q('Seeing the ladder means what?', 'Nothing about permission', ('You may take it', 'no'), ('It is free', 'no'),
          ('The neighbor gave it away', 'no'), 'Visibility is not permission.'),
        Q('A license is like what?', 'The neighbor\'s "yes" with rules', ('Taking the ladder quietly at night', 'no'),
          ('Buying a new house', 'no'), ('A broken ladder', 'no'), 'Permission with terms.'),
        Q('Online photos are like what?', 'The neighbor\'s ladder', ('Your own ladder', 'no'), ('Free public air', 'no'),
          ('Trash on the street', 'no'), 'Owned by someone.'),
        Q('What should you do before using something?', 'Ask or check the license', ('Just take it quietly', 'no'), ('Hide it', 'no'),
          ('Change the color', 'still theirs'), 'Get permission.'),
        Q('Agreeing when to return the ladder is like what?', 'License terms', ('A refund policy', 'no'), ('A tax', 'no'), ('A logo', 'no'),
          'Conditions of use.'),
    ], why='A learner who misses MAIN may think online means free; borrowing a neighbor\'s ladder shows why permission matters.')],
    F1=sec('Apply it: check rights before using material', RIGHTS, [
        Q('An owner wants a popular song in a promotional video. What should she do?', 'Get a license or use music that allows commercial use',
          ('Use it because the clip is short', 'still needs rights'), ('Use it and credit the artist in the caption only', 'credit is not permission'),
          ('Use it on one platform only', 'still needs rights'), 'License first.'),
        Q('A stock photo site license allows commercial use with credit. What must the owner do?', 'Give the required credit',
          ('Nothing at all', 'credit required'), ('Pay the photographer twice', 'not required'), ('Remove the watermark and skip credit', 'violates'),
          'Follow terms.'),
        Q('A developer copies code from a website into the store\'s app. What should be checked?', 'The code\'s license terms',
          ('Nothing; code online is always free', 'not true'), ('Only how long the code is', 'irrelevant'), ('Only the font', 'irrelevant'),
          'Code is licensed too.'),
        Q('Licensing 4 photos at 12 dollars each costs how much?', '48 dollars', ('16 dollars', 'added'), ('12 dollars', 'one'),
          ('3 dollars', 'divided'), '4 x 12 = 48.', calc=lambda: 4 * 12 == 48),
        Q('An owner names her coffee shop very similar to a famous chain. What risk does this create?', 'Customer confusion and a trademark dispute',
          ('No risk if her state approved the name', 'not trademark rights'), ('Automatic free advertising', 'risky'),
          ('Lower rent', 'irrelevant'), 'Avoid confusing names.'),
    ]),
    F2=sec('Handle the complications: unclear rights and takedowns', RIGHTS, [
        Q('A photographer asks a shop to remove her photo it used without a license. What should the shop do?', 'Remove it promptly and resolve it fairly',
          ('Ignore the request', 'escalates'), ('Argue that it was online, so anyone may use it', 'not permission'), ('Post it more widely', 'worse'),
          'Respond respectfully.'),
        Q('A designer gives the owner a logo but the contract does not say who owns it. What should she get?', 'A written transfer or license of the logo rights',
          ('Nothing; paying means owning automatically', 'not always'), ('A bigger file size', 'irrelevant'), ('A new color', 'irrelevant'),
          'Clarify rights.'),
        Q('A free image site says images are free for commercial use but some show recognizable people. What should the owner consider?',
          'Whether the people agreed to commercial use of their image', ('Nothing, because free means anything goes for any use', 'not always'),
          ('Only the image size', 'irrelevant'), ('Only the image color', 'irrelevant'), 'People have rights too.'),
        Q('An AI tool generates an image very similar to a famous character. What is the concern?', 'It may still infringe someone\'s rights',
          ('AI images are always free of rights issues', 'not guaranteed'), ('Characters cannot be owned', 'they can'),
          ('Similar is always fine', 'not always'), 'Check similarity risks.'),
        Q('Which statement is accurate?', 'Use material only with permission or a license.',
          ('Anything visible online is free.', 'not true'), ('Giving credit always replaces asking permission.', 'not true'),
          ('A DBA gives trademark rights.', 'not true'), 'Respect rights.'),
    ]))

# ------------------------------------------------------------------ Set 118: truthful advertising and complaints
TRUTH = ('Advertising must be TRUTHFUL and not misleading, and claims that need proof must be supported before they are made. '
         'This includes prices ("from 20 dollars" must be available), comparisons ("cheaper than X" must be accurate), '
         'environmental claims ("eco-friendly"), and fake urgency ("only 2 left" when there are 200). Fake reviews and '
         'testimonials are deceptive. When customers COMPLAIN, respond quickly and calmly, find out what happened, fix what '
         'you can, and keep a record. Complaints often show where to improve.')

s118 = SET('ENT.RISK.06',
    M=sec('Keep ad claims truthful and handle complaints well', TRUTH, [
        Q('Which claim is misleading?', '"Only 2 left!" when there are 200', ('"From 20 dollars" when 20-dollar items exist', 'true'),
          ('"Ships in 3 days" when that is the usual time', 'true'), ('"Handmade in Ohio" when it is', 'true'), 'Fake urgency.'),
        Q('When must a claim be supported?', 'Before it is made', ('Only after a complaint', 'too late'), ('Never', 'must be'),
          ('Only if the ad is large', 'all ads'), 'Proof first.'),
        Q('What should a business do when a customer complains?', 'Respond quickly and calmly and find out what happened',
          ('Ignore it until it goes away', 'harmful'), ('Argue publicly with the customer to defend the shop', 'harmful'), ('Delete all records', 'harmful'),
          'Calm response.'),
        Q('Why keep a record of complaints?', 'They show where to improve', ('To post them as ads', 'no'), ('To blame customers', 'no'),
          ('Because records lower taxes', 'no'), 'Learning.'),
        Q('A shop advertises "cheaper than Big Mart" without checking prices. What is the problem?', 'The comparison may be false',
          ('Comparisons need no checking', 'they do'), ('Big Mart must prove it', 'no'), ('It is always true', 'unknown'), 'Check comparisons.'),
    ]),
    B=[cs('A promise on a sign', 'If a lemonade stand sign says "Fresh squeezed, 1 dollar," customers expect fresh juice for '
          'a dollar. If it is powdered mix for 2 dollars, they feel tricked, even if it tastes fine. An ad is a promise on a '
          'sign. And when someone complains, listening calmly is like checking whether your lemonade really was what the sign '
          'said.', [
        Q('An ad is like what?', 'A promise on a sign', ('A secret note', 'no'), ('A tax form', 'no'), ('A weekly grocery list', 'no'),
          'Public promise.'),
        Q('Why do customers feel tricked by powdered mix?', 'The sign promised fresh juice', ('Powder is illegal', 'no'),
          ('Lemonade is always bad', 'no'), ('The price was much too low', 'it was higher'), 'Broken promise.'),
        Q('If the sign says 1 dollar but they charge 2, what is wrong?', 'The price claim was false', ('Nothing is wrong', 'no'),
          ('The cups were small', 'not the point'), ('The weather changed that day', 'no'), 'False price.'),
        Q('Listening to a complaint is like what?', 'Checking whether the lemonade matched the sign', ('Making a bigger batch of lemonade for the next day', 'no'),
          ('Painting the stand', 'no'), ('Closing early', 'no'), 'Find what happened.'),
        Q('What should the sign always do?', 'Tell the truth about the product', ('Exaggerate', 'no'), ('Hide prices', 'no'),
          ('Promise everything customers want', 'no'), 'Truthful claims.'),
    ], why='A learner who misses MAIN may not see an ad as a promise; a lemonade sign makes it concrete.')],
    F1=sec('Apply it: fix ads and respond to complaints', TRUTH, [
        Q('An ad says "Eco-friendly packaging," but only the box is recyclable; the filler is plastic. What should change?', 'State exactly what is recyclable',
          ('Keep the broad claim', 'misleading'), ('Add "very" to the eco-friendly claim', 'worse'), ('Remove the box', 'not the issue'),
          'Specific, accurate claims.'),
        Q('A sale ad says "Prices from 10 dollars," but no item is under 25 dollars. What should the owner do?', 'Change the ad to the real starting price',
          ('Keep it to attract clicks', 'misleading'), ('Add one 10-dollar item no one can buy', 'bait'), ('Hide the prices', 'misleading'),
          'True prices.'),
        Q('A complaint says a mug arrived broken. Which reply is best?', '"Sorry it arrived broken. Could you send a photo? We will replace it."',
          ('"Not our problem."', 'dismissive'), ('"You must have broken it yourself after it arrived, not us."', 'accusatory'), ('No reply', 'harmful'), 'Calm and helpful.'),
        Q('In a month, 6 of 300 orders bring complaints about late shipping. What percent is that?', '2 percent', ('6 percent', 'count'),
          ('50 percent', 'misdivided'), ('0.2 percent', 'moved decimal'), '6 / 300 = 0.02.', calc=lambda: 6 / 300 == 0.02),
        Q('Most complaints mention slow replies. What should the owner improve first?', 'Response time to messages', ('The logo', 'unrelated'),
          ('Product colors and sizes', 'unrelated'), ('Ad budget', 'unrelated'), 'Address the pattern.'),
    ]),
    F2=sec('Handle the complications: unfair complaints and claims pressure', TRUTH, [
        Q('A customer posts an angry complaint that is partly wrong. What is the best response?', 'Reply calmly with facts; offer to resolve it privately',
          ('Insult the customer publicly', 'harmful'), ('Post the customer\'s address', 'harmful'), ('Threaten legal action immediately in a public reply', 'escalates'),
          'Professional response.'),
        Q('A supplier says its cream "removes wrinkles in 3 days" and offers no proof. What should the reseller do?', 'Not repeat the claim without support',
          ('Repeat it since the supplier said it', 'still responsible'), ('Make the claim stronger', 'worse'), ('Add a celebrity photo', 'misleading'),
          'Resellers need support too.'),
        Q('A countdown timer resets every time the page loads. What is the problem?', 'It creates fake urgency', ('None; timers are always fine', 'misleading'),
          ('It is too slow', 'not the issue'), ('It is too colorful', 'irrelevant'), 'False urgency.'),
        Q('A business resolves 45 of 50 complaints within 2 days. What percent is that?', '90 percent', ('45 percent', 'count'),
          ('5 percent', 'unresolved count'), ('10 percent', 'unresolved rate'), '45 / 50 = 0.9.', calc=lambda: 45 / 50 == 0.9),
        Q('Which statement is accurate?', 'Ads must be truthful, and complaints help fix problems.',
          ('Exaggeration is always allowed in ads for small shops.', 'misleading'), ('Complaints should be ignored.', 'harmful'),
          ('Fake urgency is a harmless tactic.', 'misleading'), 'Honesty and service.'),
    ]))

# ------------------------------------------------------------------ Set 119: doing it yourself or getting help
DIY = ('Owners often try to do everything themselves to save money. Compare the cost of HIRING HELP with the value of your '
       'own time and the risk of mistakes. Example: if you can earn 50 dollars an hour on paid work and a bookkeeper charges 35 '
       'dollars an hour, paying the bookkeeper may free time for better-paid work. Get help for tasks that are complex, '
       'risky, or that you do slowly; keep tasks that are simple and central to your business. Start small, for example a '
       'few hours a month.')

s119 = SET('ENT.HELP.01',
    M=sec('Compare the cost of help with the value of your own time and risk', DIY, [
        Q('Earning 50 dollars an hour, an owner can pay a 35-dollar bookkeeper. What is the difference per hour?', '15 dollars',
          ('35 dollars', 'bookkeeper rate'), ('85 dollars', 'added'), ('50 dollars', 'owner rate'), '50 - 35 = 15.', calc=lambda: 50 - 35 == 15),
        Q('Which task is a good candidate for help?', 'A complex task the owner does slowly', ('A simple task central to the business', 'keep'),
          ('A task that takes one minute a month', 'low value'), ('The owner\'s core skill that customers pay for', 'keep'),
          'Complex, slow or risky.'),
        Q('What should be compared before hiring help?', 'Cost of help versus value of the owner\'s time and risk', ('Only the helper\'s favorite tools', 'irrelevant'),
          ('Only the color of the helper\'s website', 'irrelevant'), ('Nothing, since owners should always do everything themselves', 'misses value'),
          'Weigh the tradeoff.'),
        Q('How can an owner start getting help?', 'Small, such as a few hours a month', ('By hiring ten full-time staff at once', 'too big'),
          ('By signing a long contract without testing', 'risky'), ('By never trying', 'no help'), 'Start small.'),
        Q('Why might doing everything yourself cost more than it saves?', 'Mistakes and lost time can cost more than help',
          ('Doing things yourself is always free of any cost', 'time has value'), ('Help is always more expensive', 'not always'),
          ('Owners never make mistakes', 'not true'), 'Hidden costs.'),
    ]),
    B=[mathb('Comparing hourly values', 'To compare doing a task yourself with paying someone, look at the value per hour. If you '
             'can earn 40 dollars an hour on paid work and a helper charges 25 dollars an hour, each hour you hand off can free you '
             'to earn 40 instead. The net gain per hour is 40 - 25 = 15 dollars, if you really fill the freed hour with paid work. '
             'If you cannot, the gain is smaller.', [
        Q('You earn 60 dollars an hour; help costs 30. What is the net gain per freed hour?', '30 dollars', ('90 dollars', 'added'),
          ('60 dollars', 'your rate'), ('2 dollars', 'divided'), '60 - 30 = 30.', calc=lambda: 60 - 30 == 30),
        Q('Net gain 20 dollars per hour for 5 hours. What is the total gain?', '100 dollars', ('25 dollars', 'added'),
          ('4 dollars', 'divided'), ('20 dollars', 'one hour'), '20 x 5 = 100.', calc=lambda: 20 * 5 == 100),
        Q('You earn 25 dollars an hour; help costs 35. What is the net per hour?', 'A loss of 10 dollars', ('A gain of 10 dollars', 'sign'),
          ('A gain of 60 dollars', 'added'), ('No difference', 'differs'), '25 - 35 = -10.', calc=lambda: 25 - 35 == -10),
        Q('If the freed hour is not used for paid work, what happens to the gain?', 'It is smaller or zero', ('It doubles', 'no'),
          ('It stays exactly the same', 'no'), ('It becomes a tax', 'no'), 'Gain depends on use.'),
        Q('Help costs 30 an hour for 4 hours. What is the total cost?', '120 dollars', ('34 dollars', 'added'), ('7.50 dollars', 'divided'),
          ('30 dollars', 'one hour'), '30 x 4 = 120.', calc=lambda: 30 * 4 == 120),
    ], why='A learner who misses MAIN may not compare hourly values; this practices net gain per hour.')],
    F1=sec('Apply it: decide what to hand off', DIY, [
        Q('A photographer spends 8 hours a month on bookkeeping and earns 60 dollars an hour shooting. A bookkeeper does it in 3 hours '
          'at 40 dollars. What does the bookkeeper cost?', '120 dollars', ('320 dollars', 'used 8 hours'), ('480 dollars', 'owner value'),
          ('43 dollars', 'added'), '3 x 40 = 120.', calc=lambda: 3 * 40 == 120),
        Q('If she fills the freed 8 hours with shoots at 60 dollars, what does she earn in that time?', '480 dollars', ('120 dollars', 'cost'),
          ('360 dollars', '6 hours'), ('68 dollars', 'added'), '8 x 60 = 480.', calc=lambda: 8 * 60 == 480),
        Q('What is her net gain from handing off bookkeeping?', '360 dollars', ('480 dollars', 'ignores cost'), ('120 dollars', 'cost'),
          ('600 dollars', 'added'), '480 - 120 = 360.', calc=lambda: 480 - 120 == 360),
        Q('Which task should the photographer most likely keep?', 'Taking the photos clients hire her for', ('Bookkeeping she does slowly', 'hand off'),
          ('Filing simple paperwork she dislikes', 'could hand off'), ('Editing tax forms she finds confusing', 'hand off'),
          'Keep core skills.'),
        Q('A baker wants help but cash is tight. What is a sensible start?', 'Hire help for a few hours a month on one task',
          ('Hire a full-time manager immediately to run everything', 'too costly'), ('Never get help', 'misses value'), ('Borrow to hire five people', 'risky'),
          'Start small.'),
    ]),
    F2=sec('Handle the complications: freed time that is not used', DIY, [
        Q('An owner hires help but uses the freed hours for unpaid tasks. What happens to the financial gain?', 'It may be small or negative',
          ('It always doubles', 'no'), ('It is the same as before', 'no'), ('The helper pays her', 'no'), 'Gain depends on use.'),
        Q('A helper makes many mistakes the owner must fix. What should she weigh?', 'Whether training or a different helper is needed',
          ('Nothing; mistakes are free', 'costly'), ('Hiring three more helpers just like that one', 'worse'), ('Never giving feedback', 'no improvement'),
          'Quality matters.'),
        Q('An owner enjoys bookkeeping and finds it restful. Should she hand it off?', 'Not necessarily; value is not only money',
          ('Yes, always, regardless of preference', 'too rigid'), ('Yes, because enjoyment is irrelevant', 'not true'),
          ('No business should ever hire help', 'too rigid'), 'Consider well-being too.'),
        Q('Help costs 300 dollars a month and saves 10 hours. What is the cost per hour saved?', '30 dollars', ('300 dollars', 'total'),
          ('10 dollars', 'hours'), ('3,000 dollars', 'multiplied'), '300 / 10 = 30.', calc=lambda: 300 / 10 == 30),
        Q('Which statement is accurate?', 'Help can pay off when freed time is used well.',
          ('Doing everything yourself always saves the most money.', 'not always'), ('Help always costs more than it gives.', 'not always'),
          ('Owner time has no value.', 'it does'), 'Weigh the tradeoff.'),
    ]))

# ------------------------------------------------------------------ Set 120: contractor or employee is not just a label
LABEL = ('Whether a worker is an EMPLOYEE or an INDEPENDENT CONTRACTOR depends on the actual working relationship, not on the '
         'label in a contract. Factors often include how much control the business has over how and when the work is done, '
         'whether the worker can profit or lose based on their own decisions, whether they work for other clients, who '
         'provides tools, and whether the work is ongoing. Federal rules have changed several times, and states may use '
         'stricter tests. Misclassification can bring back taxes and penalties, so check current rules or ask a professional.')

s120 = SET('ENT.HELP.02',
    M=sec('Recognize that worker classification depends on the real relationship', LABEL, [
        Q('What decides whether a worker is an employee or contractor?', 'The actual working relationship', ('Only the title written in the contract', 'label alone does not decide'),
          ('Only what the worker prefers to be called', 'not decisive'), ('Only the size of the paycheck', 'not decisive'), 'Reality, not labels.'),
        Q('Which factor suggests an employee relationship?', 'The business controls how and when the work is done',
          ('The worker serves many other clients', 'suggests contractor'), ('The worker sets her own prices', 'suggests contractor'),
          ('The worker provides all of her own tools and equipment', 'suggests contractor'), 'Control matters.'),
        Q('Which factor suggests an independent contractor?', 'The worker has other clients and her own tools',
          ('The business sets a fixed daily schedule', 'suggests employee'), ('The business trains her on its methods', 'suggests employee'),
          ('The work is ongoing and full time for one business', 'suggests employee'), 'Independence.'),
        Q('What can misclassification bring?', 'Back taxes and penalties', ('A tax refund for the business', 'no'),
          ('Automatic trademark rights', 'no'), ('Lower insurance costs', 'not the risk'), 'Costly consequences.'),
        Q('Why check current rules?', 'Federal rules have changed and states may be stricter', ('Rules never change', 'they have'),
          ('Only customers decide', 'no'), ('Rules are the same in every country and state', 'no'), 'Rules vary and change.'),
    ]),
    B=[cs('Calling a dog a cat', 'If you put a sign saying "cat" on a dog, it still barks. Writing "independent contractor" on '
          'a contract does not change the work if the business sets the hours, provides the tools, trains the worker and '
          'directs every step. Rules look at what the relationship is really like, the same way you would look at the animal '
          'rather than the sign.', [
        Q('A "cat" sign on a dog does what?', 'Nothing to change the animal', ('Makes it meow', 'no'), ('Makes it a cat in the eyes of the law', 'no'),
          ('Makes it quieter', 'no'), 'Labels do not change reality.'),
        Q('The sign is like what in hiring?', 'The label in a contract', ('The actual work done', 'no'), ('The paycheck', 'no'),
          ('The tools', 'no'), 'A label.'),
        Q('The animal itself is like what?', 'The real working relationship', ('The title written in the contract', 'no'), ('The logo', 'no'),
          ('The business name', 'no'), 'Reality.'),
        Q('What do rules look at?', 'What the relationship is really like', ('Only what the sign on the animal says', 'no'), ('Only the font', 'no'),
          ('Only the date', 'no'), 'Substance.'),
        Q('Setting hours and directing every step suggests what?', 'An employee-like relationship', ('A contractor relationship for sure', 'no'),
          ('A customer', 'no'), ('A supplier', 'no'), 'Control factor.'),
    ], why='A learner who misses MAIN may trust the label; a sign on an animal shows why reality decides.')],
    F1=sec('Apply it: weigh the factors', LABEL, [
        Q('A café calls a barista a contractor but sets her shifts, gives her an apron and trains her on recipes. What does this suggest?',
          'The relationship looks like employment', ('She is clearly a contractor because of the label', 'label alone'),
          ('She is a customer', 'no'), ('She is a supplier', 'no'), 'Control and training.'),
        Q('A web developer works for 6 clients, sets her own price and uses her own computer. What does this suggest?', 'An independent contractor relationship',
          ('An employee relationship for each client', 'independent signs'), ('A business partnership with each client', 'not stated'),
          ('A volunteer role', 'no'), 'Independence factors.'),
        Q('Of 5 listed factors, 4 point toward employment. What fraction points toward employment?', '4/5', ('1/5', 'contractor share'),
          ('5/4', 'reversed'), ('4/1', 'ratio'), '4 of 5.', calc=lambda: 4 / 5 == 0.8),
        Q('An owner is unsure how to classify a helper. What is the best step?', 'Check current federal and state rules, or ask a professional',
          ('Pick whichever label is cheapest for the business this year', 'risky'), ('Let the helper decide', 'not decisive'), ('Ignore classification', 'risky'),
          'Get it right.'),
        Q('Which factor is LEAST useful by itself?', 'The job title written in the contract', ('Who controls the schedule', 'useful'),
          ('Whether the worker has other clients', 'useful'), ('Who provides tools', 'useful'), 'Labels are weak evidence.'),
    ]),
    F2=sec('Handle the complications: changing roles and state rules', LABEL, [
        Q('A contractor starts working 40 hours a week only for one business, following its schedule. What should the owner do?',
          'Review whether the classification still fits', ('Nothing; the original label lasts forever', 'reality changed'),
          ('Change the label word only', 'not enough'), ('Hide the hours', 'improper'), 'Re-evaluate.'),
        Q('The federal test and the state test give different answers. What should the owner do?', 'Comply with the stricter rule that applies',
          ('Choose only the friendlier test for the business', 'risky'), ('Ignore both', 'risky'), ('Ask the worker to pick', 'not decisive'),
          'Follow applicable law.'),
        Q('Misclassification back taxes are 2,400 dollars and penalties add 25 percent. What is the total?', '3,000 dollars',
          ('2,425 dollars', 'added 25'), ('600 dollars', 'penalty only'), ('2,400 dollars', 'no penalty'), '2,400 x 1.25 = 3,000.',
          calc=lambda: 2400 * 1.25 == 3000),
        Q('An article from 2019 explains the federal test. What is the concern?', 'The rule has changed since, so it may be outdated',
          ('Old articles about labor rules are always correct', 'not true'), ('Federal rules never change', 'they have'), ('Articles replace professionals', 'no'),
          'Check current rules.'),
        Q('Which statement is accurate?', 'The real relationship and current rules decide, not the label.',
          ('A contract label always decides how a worker is classified.', 'not true'), ('States always follow federal rules exactly.', 'not always'),
          ('Misclassification has no consequences.', 'it does'), 'Reality and rules.'),
    ]))

# ------------------------------------------------------------------ Set 121: payroll responsibilities (the idea)
PAY = ('Hiring an EMPLOYEE brings PAYROLL duties. In general terms, an employer withholds certain taxes from the employee\'s '
       'pay, pays its own share of some payroll taxes, sends the money and reports to tax agencies on schedule, follows '
       'minimum wage and overtime rules, and gives the employee year-end tax forms. Many states also require registration '
       'and may require workers\' compensation insurance. This course teaches the idea; rates, forms and deadlines vary. '
       'Many small businesses use a payroll service or an accountant.')

s121 = SET('ENT.HELP.03',
    M=sec('Describe an employer\'s payroll duties in general terms', PAY, [
        Q('What does withholding mean for an employer?', 'Taking taxes out of pay and sending them to the agency',
          ('Holding back the employee\'s whole paycheck as a penalty', 'not this'), ('Refusing to pay overtime', 'not this'),
          ('Keeping the employee\'s tools', 'not this'), 'Withhold and remit.'),
        Q('Which is an employer duty?', 'Following minimum wage and overtime rules', ('Choosing the employee\'s lunch', 'no'),
          ('Paying the employee\'s personal rent', 'no'), ('Filing the employee\'s personal return', 'no'), 'Wage rules.'),
        Q('What does the employer give employees at year end?', 'Tax forms showing pay and withholding', ('A new employment contract every single year', 'no'),
          ('A list of customers', 'no'), ('A refund of all taxes', 'no'), 'Year-end forms.'),
        Q('What may many states require of employers?', 'Registration and workers\' compensation insurance', ('Nothing at all', 'not true'),
          ('A trademark filing', 'unrelated'), ('A new LLC formed for each employee hired', 'no'), 'State duties.'),
        Q('What do many small businesses use for payroll?', 'A payroll service or an accountant', ('Guesswork each pay period', 'risky'),
          ('The employee to calculate her own taxes', 'not their job'), ('Nothing; payroll is optional', 'not optional'), 'Help with payroll.'),
    ]),
    B=[cs('A collection box at the counter', 'Imagine a cashier who collects a small amount from each sale for a charity and '
          'must send it in every month. The money passes through the cashier but belongs to the charity. Withheld payroll taxes '
          'are similar: the employer holds them briefly and must send them on time. Spending them on rent is like spending the '
          'charity\'s money.', [
        Q('The charity money belongs to whom?', 'The charity', ('The cashier', 'only holds it'), ('The customer forever', 'no'),
          ('The store owner', 'no'), 'Held for others.'),
        Q('Withheld payroll taxes are like what?', 'The charity money in the box', ('The employer\'s profit', 'no'),
          ('A bonus for the employer', 'no'), ('A gift from the employee', 'no'), 'Held in trust.'),
        Q('When must the charity money be sent?', 'On schedule', ('Whenever convenient', 'no'), ('Never', 'no'), ('After ten years', 'no'),
          'Deadlines apply.'),
        Q('Spending withheld taxes on rent is like what?', 'Spending the charity\'s money', ('Saving money', 'no'), ('Paying a fair bill on time', 'no'),
          ('A tax refund', 'no'), 'Misusing held funds.'),
        Q('What is the cashier\'s role?', 'Collect and pass on the money', ('Keep the money for yourself', 'no'), ('Spend the money', 'no'),
          ('Hide the money', 'no'), 'A pass-through.'),
    ], why='A learner who misses MAIN may think withheld taxes are business money; a charity box shows they are held for others.')],
    F1=sec('Apply it: prepare for a first employee', PAY, [
        Q('An owner hires her first employee. Which step should come first?', 'Learn the federal and state employer requirements',
          ('Pay cash with no records', 'non-compliant'), ('Call the employee a contractor to skip payroll entirely', 'misclassification risk'),
          ('Wait until year end to think about taxes', 'too late'), 'Prepare first.'),
        Q('An employee earns 18 dollars an hour for 20 hours a week. What is weekly gross pay?', '360 dollars', ('38 dollars', 'added'),
          ('180 dollars', '10 hours'), ('900 dollars', 'miscalculated'), '18 x 20 = 360.', calc=lambda: 18 * 20 == 360),
        Q('A payroll service costs 45 dollars a month. What is the yearly cost?', '540 dollars', ('45 dollars', 'one month'),
          ('450 dollars', '10 months'), ('585 dollars', '13 months'), '45 x 12 = 540.', calc=lambda: 45 * 12 == 540),
        Q('An owner withheld taxes but used the money for supplies. What problem does she face?', 'She still owes those taxes to the agency',
          ('None, because withheld money is hers to spend', 'not hers'), ('The taxes are cancelled', 'no'), ('The employee owes them now', 'no'),
          'Held funds must be sent.'),
        Q('Which detail varies by place and should be checked?', 'Minimum wage and state payroll requirements', ('Whether employees need to be paid at all', 'always'),
          ('Whether taxes exist', 'they do'), ('Whether records matter', 'they do'), 'Rules vary.'),
    ]),
    F2=sec('Handle the complications: mistakes and overtime', PAY, [
        Q('A payroll deposit was missed. What is a sensible step?', 'Make it right away and check penalties or ask a professional',
          ('Ignore it until someone from the tax agency notices it', 'worse'), ('Skip the next one too', 'worse'), ('Ask the employee to pay', 'improper'),
          'Act promptly.'),
        Q('An employee works 45 hours in a week where overtime applies after 40. How many overtime hours?', '5', ('45', 'total'),
          ('40', 'regular'), ('85', 'added'), '45 - 40 = 5.', calc=lambda: 45 - 40 == 5),
        Q('If overtime pays 1.5 times a 20-dollar rate, what is the overtime pay for those hours?', '150 dollars', ('100 dollars', 'regular rate'),
          ('30 dollars', 'one hour'), ('900 dollars', 'all hours'), '5 x 30 = 150.', calc=lambda: 5 * 20 * 1.5 == 150),
        Q('An owner thinks payroll is too complex to handle alone. What is reasonable?', 'Use a payroll service or accountant',
          ('Avoid payroll by paying cash secretly', 'non-compliant'), ('Guess each period', 'risky'), ('Stop paying the employee', 'unlawful'),
          'Get help.'),
        Q('Which statement is accurate?', 'Employers must withhold, pay and report on schedule.',
          ('Withheld taxes belong to the employer.', 'not true'), ('Payroll rules are identical in every state and city.', 'they vary'),
          ('Employers have no reporting duties.', 'they do'), 'Payroll duties.'),
    ]))

# ------------------------------------------------------------------ Set 122: onboarding and offboarding helpers
ONB = ('ONBOARDING sets up a new helper to succeed and keeps the business safe: a written role description, any required '
       'paperwork, training with the checklists, their own logins with limited access, and who to ask for help. '
       'OFFBOARDING happens when someone leaves: remove their access the same day, collect keys and equipment, transfer any '
       'files or customer conversations they handled, settle final pay as required, and thank them. Both are easier with a '
       'simple checklist.')

s122 = SET('ENT.HELP.04',
    M=sec('Use simple checklists to start and end work with helpers', ONB, [
        Q('What is onboarding?', 'Setting up a new helper to succeed', ('Removing a helper\'s access', 'offboarding'),
          ('Loading boxes onto a delivery truck', 'pun'), ('Filing an annual report', 'no'), 'Start well.'),
        Q('Which belongs in onboarding?', 'Their own logins with limited access', ('The owner\'s bank password', 'no'),
          ('Full access to every business account', 'excess'), ('No training at all', 'no'), 'Safe access.'),
        Q('When should a departing helper\'s access be removed?', 'The same day', ('Next month', 'risk'), ('Never', 'risk'),
          ('Only if they ask', 'risk'), 'Promptly.'),
        Q('Which belongs in offboarding?', 'Collecting keys and transferring their files', ('Giving them more access', 'opposite'),
          ('Hiring their replacement before anything else', 'not required'), ('Deleting all customer records', 'harmful'), 'Close properly.'),
        Q('What makes both processes easier?', 'A simple checklist', ('Memory alone, with no notes', 'unreliable'), ('Guesswork', 'unreliable'),
          ('Skipping steps', 'risky'), 'Checklists.'),
    ]),
    B=[cs('Moving into and out of an apartment', 'When you move into an apartment, you get keys, learn where things are, and sign '
          'papers. When you move out, you return the keys, take your things, and leave a forwarding address. Starting and '
          'ending work with a helper is the same pair of steps: give access and information at the start, then take back '
          'access and pass on their work at the end.', [
        Q('Getting keys when moving in is like what?', 'Giving a new helper logins', ('Removing all their access', 'no'), ('Final pay', 'no'),
          ('A complaint', 'no'), 'Onboarding access.'),
        Q('Returning keys when moving out is like what?', 'Removing a helper\'s access', ('Hiring', 'no'), ('Training', 'no'),
          ('A promotion to manager', 'no'), 'Offboarding access.'),
        Q('Learning where things are is like what?', 'Training', ('Firing', 'no'), ('Paying taxes', 'no'), ('Advertising', 'no'),
          'Orientation.'),
        Q('Leaving a forwarding address is like what?', 'Passing on their work and contacts', ('Deleting everything', 'no'),
          ('Keeping secrets', 'no'), ('Taking the customers with them', 'no'), 'Handover.'),
        Q('How many main stages are in the picture?', 'Two: moving in and moving out', ('One: moving in, and nothing else', 'no'), ('Ten', 'no'), ('Zero', 'no'),
          'Start and end.'),
    ], why='A learner who misses MAIN may not see both stages; moving into and out of an apartment shows them.')],
    F1=sec('Apply it: run the checklists', ONB, [
        Q('A new helper starts Monday. Which item is most urgent to prepare?', 'A login with only the access her role needs',
          ('A copy of the owner\'s personal tax return', 'no'), ('Full admin rights to every account', 'excess'),
          ('Nothing until she asks', 'unprepared'), 'Safe access.'),
        Q('An onboarding checklist has 10 items and 7 are done. How many remain?', '3', ('7', 'done'), ('10', 'total'), ('17', 'added'),
          '10 - 7 = 3.', calc=lambda: 10 - 7 == 3),
        Q('A helper leaves and was handling 12 customer conversations. What should happen?', 'Transfer them to someone else with notes',
          ('Let them go unanswered', 'harms customers'), ('Delete them', 'harmful'), ('Let the departing helper keep them', 'risk'),
          'Handover.'),
        Q('A helper still has a shop key after leaving. What should the owner do?', 'Collect it, or change the lock if it cannot be returned',
          ('Ignore it', 'risk'), ('Give them another key', 'worse'), ('Post about it online and wait for the key to come back', 'unhelpful'), 'Secure access.'),
        Q('Which onboarding item helps a helper know who to ask?', 'A named contact for questions', ('A blank page', 'no'),
          ('A secret password', 'no'), ('A competitor\'s phone number', 'no'), 'Support.'),
    ]),
    F2=sec('Handle the complications: sudden departures and gaps', ONB, [
        Q('A helper quits suddenly by text. What is the first step?', 'Remove access immediately', ('Wait a week to see if they return', 'risk'),
          ('Give them more access to finish', 'risk'), ('Ignore it', 'risk'), 'Secure first.'),
        Q('After a departure, customers report unanswered emails. What would have prevented this?', 'Transferring conversations as part of offboarding',
          ('Hiring nobody ever', 'too far'), ('Deleting the helper\'s email account entirely', 'worse'), ('Changing the logo', 'irrelevant'),
          'Handover step.'),
        Q('Final pay rules vary by state. What should the owner do?', 'Check the state\'s rules for final pay timing',
          ('Pay the final wages whenever convenient', 'may violate'), ('Skip final pay', 'unlawful'), ('Ask the helper to wait indefinitely', 'improper'),
          'Follow rules.'),
        Q('A new helper was given no training and made errors on 6 of 30 orders. What percent had errors?', '20 percent',
          ('6 percent', 'count'), ('30 percent', 'total'), ('5 percent', 'misdivided'), '6 / 30 = 0.2.', calc=lambda: 6 / 30 == 0.2),
        Q('Which statement is accurate?', 'Simple checklists make starting and ending work safer.',
          ('Offboarding can wait months.', 'risk'), ('Training is never needed.', 'needed'), ('Everyone should get full access on their first day.', 'excess'),
          'Checklists help.'),
    ]))

# ------------------------------------------------------------------ Set 123: partners
PART = ('Starting with a PARTNER can add skills, money and support, but disagreements are a common reason partnerships fail. '
        'Before starting, agree in writing on: each person\'s ROLE and time commitment, ownership percentages and money '
        'contributed, how decisions are made (and how ties are broken), how profits are shared, what happens if someone '
        'wants to leave or stops contributing, and how to resolve disagreements. Talk openly about goals, risk tolerance '
        'and money. Friendship is not a substitute for a written agreement.')

s123 = SET('ENT.HELP.05',
    M=sec('Agree on partner roles, ownership and disagreements before starting', PART, [
        Q('Which topic should partners agree on in writing?', 'How ties are broken', ('Their favorite lunch spots', 'irrelevant'),
          ('Which music plays in the office', 'irrelevant'), ('The color of business cards', 'minor'), 'Decision rules.'),
        Q('Why put a partnership agreement in writing?', 'To reduce later disagreements', ('Because friends never disagree', 'not true'),
          ('Because writing makes profits higher', 'not directly'), ('To avoid ever talking', 'opposite'), 'Clarity.'),
        Q('What should partners discuss openly?', 'Goals, risk tolerance and money', ('Nothing important', 'risky'),
          ('Only the logo', 'minor'), ('Only who sits where in the office', 'minor'), 'Align expectations.'),
        Q('Is friendship a substitute for a written agreement?', 'No', ('Yes, always', 'not true'), ('Only for family', 'no'),
          ('Only for small businesses', 'no'), 'Write it down.'),
        Q('What should the agreement say about someone leaving?', 'What happens to their share and duties', ('Nothing; leaving never happens', 'it can'),
          ('That they must stay forever', 'unrealistic'), ('That the business closes automatically', 'not required'), 'Exit plan.'),
    ]),
    B=[cs('Planning a road trip with a friend', 'Before a long road trip, friends decide who drives when, how gas money is split, '
          'and what happens if one wants to stop early. Without that talk, small annoyances grow into big fights by day three. '
          'A business partnership is a much longer trip with more money at stake, so the same planning matters even more.', [
        Q('Who drives when is like what?', 'Each partner\'s role', ('The profit split', 'no'), ('Exit rule', 'no'), ('Logo', 'no'),
          'Roles.'),
        Q('How gas money is split is like what?', 'How money and profits are shared', ('Who drives', 'no'), ('The music choice in the car', 'no'),
          ('Exit rules', 'no'), 'Money terms.'),
        Q('One friend wanting to stop early is like what?', 'A partner wanting to leave', ('A new customer arriving', 'no'), ('A tax bill', 'no'),
          ('A supplier', 'no'), 'Exit.'),
        Q('What happens without the planning talk?', 'Small annoyances can grow into big fights', ('Everything goes smoothly anyway, always', 'unlikely'),
          ('The trip gets shorter', 'no'), ('Gas becomes free', 'no'), 'Unspoken expectations.'),
        Q('Why does planning matter more for a business?', 'It lasts longer with more money at stake', ('It is shorter', 'no'),
          ('Money never matters', 'no'), ('Friends never disagree about money', 'no'), 'Higher stakes.'),
    ], why='A learner who misses MAIN may assume goodwill is enough; planning a road trip shows why agreements matter.')],
    F1=sec('Apply it: set up a two-partner business', PART, [
        Q('Partner A puts in 6,000 dollars and Partner B puts in 4,000 dollars. If ownership follows money, what is A\'s share?', '60 percent',
          ('40 percent', 'B'), ('50 percent', 'equal'), ('6 percent', 'not converted'), '6,000 / 10,000 = 0.6.', calc=lambda: 6000 / 10000 == 0.6),
        Q('B works full time and A works 5 hours a week, but ownership follows money only. What should they discuss?', 'Whether pay for work should be separate from ownership',
          ('Nothing, because the split is obviously fair already', 'may not be'), ('Only the office décor', 'irrelevant'), ('Only the logo', 'irrelevant'),
          'Work versus capital.'),
        Q('Two equal partners disagree on a key hire. Their agreement names a trusted mentor to break ties. What should they do?', 'Ask the mentor, as agreed',
          ('Stop talking to each other', 'harmful'), ('Let the louder partner decide', 'unfair'), ('Close the business', 'too far'),
          'Follow the agreement.'),
        Q('Profit is 18,000 dollars, split 60/40. How much goes to the 40-percent partner?', '7,200 dollars', ('10,800 dollars', '60 percent'),
          ('9,000 dollars', 'equal'), ('720 dollars', 'moved decimal'), '0.4 x 18,000 = 7,200.', calc=lambda: 0.4 * 18000 == 7200),
        Q('Which question best reveals different risk tolerance?', '"How much of our savings are we willing to lose if this fails?"',
          ('"What is your favorite color?"', 'irrelevant'), ('"Where should we eat today, and who is paying for it?"', 'irrelevant'), ('"Which font do you like?"', 'irrelevant'),
          'Money and risk.'),
    ]),
    F2=sec('Handle the complications: stalled partners and exits', PART, [
        Q('A partner stops contributing work for months. The agreement covers this. What should happen?', 'Follow the agreement\'s process for non-contribution',
          ('Ignore it and resent them', 'harmful'), ('Lock them out of everything without any notice', 'improper'), ('Post about it online', 'harmful'),
          'Use the agreed process.'),
        Q('A partner wants to sell her share to a stranger. What should the others check?', 'What the agreement says about selling shares',
          ('Nothing, because anyone can join any business', 'may be restricted'), ('Only the stranger\'s car', 'irrelevant'), ('Only the logo', 'irrelevant'),
          'Transfer rules.'),
        Q('Partners never wrote an agreement and now disagree about profit shares. What is likely?', 'A difficult dispute with no agreed rule',
          ('An easy, quick resolution', 'unlikely'), ('Automatic equal shares everywhere, always', 'uncertain'),
          ('The business pays no taxes', 'irrelevant'), 'Missing rules cause disputes.'),
        Q('A mediator costs 150 dollars an hour for 4 hours, split equally. What does each partner pay?', '300 dollars', ('600 dollars', 'total'),
          ('150 dollars', 'one hour'), ('75 dollars', 'half hour'), '150 x 4 / 2 = 300.', calc=lambda: 150 * 4 / 2 == 300),
        Q('Which statement is accurate?', 'Written agreements help partnerships survive disagreements.',
          ('Good friends never need written partnership agreements.', 'not true'), ('Partnerships never fail.', 'they can'),
          ('Ownership always equals hours worked.', 'not necessarily'), 'Plan ahead.'),
    ]))

# ------------------------------------------------------------------ Set 124: mentors, accountants, attorneys, free help
FREE = ('Help comes in different forms. MENTORS share experience and can spot blind spots. SCORE, an SBA resource partner, '
        'offers free volunteer mentoring (some workshops charge fees). SMALL BUSINESS DEVELOPMENT CENTERS (SBDCs) offer free or '
        'low-cost consulting through host institutions. Libraries and local chambers of commerce may run workshops. For '
        'specific legal or tax decisions, a licensed ATTORNEY or ACCOUNTANT gives advice for your situation. Free help is '
        'valuable, but check the person\'s experience and whether they are qualified for your question.')

s124 = SET('ENT.HELP.06',
    M=sec('Match questions to mentors, free programs and licensed professionals', FREE, [
        Q('What does SCORE offer?', 'Free volunteer mentoring', ('Free legal representation in court', 'not stated'),
          ('Free business loans for every owner', 'not stated'), ('Free tax filing for all businesses', 'not stated'), 'Mentoring.'),
        Q('What do SBDCs offer?', 'Free or low-cost consulting', ('Trademark registrations for free', 'not stated'),
          ('Guaranteed grants', 'not stated'), ('Payroll processing', 'not stated'), 'Consulting.'),
        Q('Who should answer a specific tax decision?', 'A licensed accountant or tax professional', ('A friendly mentor in another field', 'not qualified'),
          ('A social media follower with tax tips', 'not qualified'), ('A competitor', 'not independent'), 'Licensed advice.'),
        Q('What should an owner check about free help?', 'Their experience and qualifications for the question',
          ('Nothing, because free help is always right for any question', 'not always'), ('Only their website colors', 'irrelevant'),
          ('Only how fast they reply', 'not enough'), 'Fit and qualifications.'),
        Q('What can a mentor help with?', 'Spotting blind spots from experience', ('Signing contracts for you', 'no'),
          ('Filing your taxes by law', 'no'), ('Guaranteeing that the business succeeds', 'no'), 'Perspective.'),
    ]),
    B=[cs('Asking for directions', 'If you are lost, a local resident can point the way, which is free and often good. For a '
          'complicated trip through a mountain pass in winter, you might want a licensed guide. Business help is similar: '
          'mentors and free programs give useful directions, and licensed professionals handle the risky, specific routes '
          'such as contracts and taxes.', [
        Q('A helpful local resident is like what?', 'A mentor or free program', ('A licensed attorney in court', 'no'), ('A tax agency', 'no'),
          ('A bank', 'no'), 'Free guidance.'),
        Q('A licensed mountain guide is like what?', 'A licensed professional for risky decisions', ('A random stranger', 'no'),
          ('A paper map with no roads drawn on it', 'no'), ('A friend\'s guess', 'no'), 'Qualified help.'),
        Q('When do you want the licensed guide?', 'For a risky, complicated route', ('For a short walk to the store', 'not needed'),
          ('Never', 'no'), ('Only on sunny days', 'no'), 'High stakes.'),
        Q('Contracts and taxes are like what in the picture?', 'The risky mountain pass', ('A short walk', 'no'), ('A parking lot near the trail', 'no'),
          ('A coffee break', 'no'), 'Specific, risky decisions.'),
        Q('Is free help useful?', 'Yes, often', ('Never', 'no'), ('Only when paid later', 'no'), ('Only for experts', 'no'),
          'Often valuable.'),
    ], why='A learner who misses MAIN may not match help to the question; asking for directions versus hiring a guide shows it.')],
    F1=sec('Apply it: choose the right help', FREE, [
        Q('A new owner wants feedback on her business plan at no cost. Which option fits best?', 'A free mentoring program such as SCORE',
          ('A paid attorney for a full lawsuit', 'mismatch'), ('A social media poll of strangers', 'unreliable'),
          ('A competitor\'s opinion', 'conflict'), 'Free mentoring.'),
        Q('An owner must decide how to structure a large investor deal. Who fits best?', 'A licensed attorney', ('A friend who once sold cookies', 'not qualified'),
          ('A library workshop alone', 'not specific'), ('A random forum', 'unreliable'), 'Specific legal advice.'),
        Q('A workshop costs 25 dollars and an attorney consultation costs 200. How much more is the consultation?', '175 dollars',
          ('225 dollars', 'added'), ('200 dollars', 'consultation'), ('8 dollars', 'ratio'), '200 - 25 = 175.', calc=lambda: 200 - 25 == 175),
        Q('A mentor gives confident tax advice outside her field. What should the owner do?', 'Confirm it with a tax professional',
          ('Follow it without checking with anyone', 'risky'), ('Ignore all mentors forever', 'overreaction'), ('Post it online as fact', 'risky'),
          'Verify outside expertise.'),
        Q('Where else might an owner find local workshops?', 'Libraries and chambers of commerce', ('Only private, paid online courses', 'not only'),
          ('Only abroad', 'no'), ('Nowhere', 'no'), 'Local options.'),
    ]),
    F2=sec('Handle the complications: conflicting advice and fit', FREE, [
        Q('Two mentors give opposite advice. What should the owner do?', 'Ask each for reasons and test against her own evidence',
          ('Follow whichever mentor happened to speak to her last', 'arbitrary'), ('Ignore both and guess', 'wasteful'), ('Flip a coin', 'arbitrary'),
          'Weigh reasons.'),
        Q('A "free" advisor pushes the owner to buy his own expensive program. What should she consider?', 'Whether the advice is influenced by his sales interest',
          ('Nothing, because free advice is always unbiased', 'not necessarily'), ('Buying immediately', 'risky'), ('Only his website', 'irrelevant'),
          'Check conflicts of interest.'),
        Q('An owner can afford one hour with an accountant. Which question is the best use?', 'How to plan for taxes given her business structure',
          ('Which logo color to choose for the new shop', 'not accounting'), ('Which coffee to stock', 'not accounting'), ('What to name her cat', 'irrelevant'),
          'High-value expertise.'),
        Q('A mentor helped her avoid a 1,500-dollar mistake. The mentoring was free. What was the net value of that advice?', '1,500 dollars',
          ('0 dollars', 'it had value'), ('750 dollars', 'halved'), ('3,000 dollars', 'doubled'), '1,500 saved - 0 cost.',
          calc=lambda: 1500 - 0 == 1500),
        Q('Which statement is accurate?', 'Free help is valuable; licensed pros handle legal and tax decisions.',
          ('Free help is always wrong.', 'not true'), ('Mentors can replace attorneys and accountants for any question.', 'not true'),
          ('Professionals are never needed.', 'not true'), 'Match help to need.'),
    ]))

SETS = [s113, s114, s115, s116, s117, s118, s119, s120, s121, s122, s123, s124]
