"""Entrepreneurship sets 38-42: Foundation 6, addresses, mail and business contact details."""
from eq import Q, sec, cs, SET

# ------------------------------------------------------------------ Set 38: three kinds of address
ADDR = ('A business can have different addresses for different jobs. The REGISTERED AGENT ADDRESS is where official '
        'legal papers are delivered; states usually require a physical street address in the state. The MAILING '
        'ADDRESS is where ordinary letters and bills go; it may be a PO Box in many cases. The PHYSICAL (or principal) '
        'ADDRESS is where the business actually operates. Some addresses appear in public state records, so a '
        'home-based owner may prefer not to use her home for every one. Each state sets its own rules; Washington, for '
        'example, does not allow a PO Box as the registered agent address.')

s38 = SET('ENT.MAIL.01',
    M=sec('Tell apart the registered agent, mailing and physical addresses', ADDR, [
        Q('Which address receives official legal papers?', 'The registered agent address',
          ('The mailing address used for catalogs and bills', 'ordinary mail'),
          ('The address printed on the shipping boxes', 'not a legal role'),
          ('The address of the owner\'s favorite supplier', 'not the business\'s address'),
          'The registered agent receives legal papers.'),
        Q('Where does the business actually operate?', 'Its physical address',
          ('Its registered agent\'s office in every case', 'may differ'),
          ('Its website\'s domain name registrar', 'not a place of operation'),
          ('Its bank\'s main headquarters building', 'not where it operates'),
          'The physical address is where work happens.'),
        Q('Which address can often be a PO Box?', 'The mailing address',
          ('The registered agent address in Washington', 'not allowed there'),
          ('The physical place where customers visit', 'a box is not a workplace'),
          ('The kitchen where food is prepared', 'a physical place'),
          'Many mailing addresses can be PO Boxes.'),
        Q('Why might a home-based owner avoid listing her home on every form?', 'Some addresses appear in public records',
          ('Home addresses are banned for every business', 'not banned'),
          ('Mail cannot be delivered to houses at all', 'it can'),
          ('Using a home address doubles the tax owed', 'no such rule'),
          'Public records can expose a home address.'),
        Q('Who sets the rules for registered agent addresses?', 'Each state',
          ('Each customer who buys from the business', 'not customers'),
          ('The business\'s favorite delivery company', 'not a rule maker'),
          ('The owner\'s neighbors on the same street', 'not a rule maker'),
          'State rules apply; Washington is one example.'),
    ]),
    B=[cs('Doors of a house', 'Think of a house with different doors: the front door where guests ring the bell, a mail slot '
          'where letters drop, and the rooms inside where the family actually lives. A business also has different '
          '"doors": an official door for legal papers (the registered agent address), a slot for everyday mail (the '
          'mailing address), and the rooms where the work happens (the physical address). Sometimes all three are the '
          'same place; sometimes they are not.', [
        Q('The slot where letters drop matches which address?', 'The mailing address',
          ('The physical address of the workshop', 'that is the rooms'),
          ('The registered agent address for papers', 'the official door'),
          ('The website address for online visitors', 'not in the picture'), 'Everyday mail goes to the mailing address.'),
        Q('The rooms where the family lives match which address?', 'The physical address',
          ('The mailing address on envelopes', 'that is the slot'),
          ('The registered agent address only', 'the official door'),
          ('The bank\'s branch address downtown', 'not in the picture'), 'Work happens at the physical address.'),
        Q('The official door for legal papers matches which address?', 'The registered agent address',
          ('The mailing address for catalogs', 'everyday mail'),
          ('The physical address of a warehouse', 'where work happens'),
          ('The email address for customers', 'not in the picture'), 'Legal papers go to the agent.'),
        Q('Can all three addresses be the same place?', 'Yes, sometimes',
          ('No, never under any state law', 'they can match'),
          ('Only for companies with 500 workers', 'size is not the rule'),
          ('Only if the business has no customers', 'not the rule'), 'They can match or differ.'),
        Q('How many kinds of address does the picture show?', 'Three',
          ('One, because a business has only one address', 'there are three roles'),
          ('Ten, one for each room in the house', 'not the roles'),
          ('Two, mail and email', 'not the roles shown'), 'Agent, mailing and physical.'),
    ], why='A learner who misses MAIN may think a business has one address; a house\'s doors and rooms show the roles.')],
    F1=sec('Apply it: choose an address for each job', ADDR, [
        Q('Ruth runs an online shop from her apartment in Washington and wants privacy. Which plan fits her state\'s rule?',
          'A registered agent service for legal papers, and a PO Box for mail', ('Her PO Box as the registered agent address, and her home for mail', 'Washington does not allow that'),
          ('A made-up street address on every form', 'false information'), ('No address on any form at all', 'addresses are required'),
          'An agent service and a mailing box keep her home off some records.'),
        Q('A bakery has a storefront where customers buy bread. What is its physical address?', 'The storefront\'s street address',
          ('The owner\'s PO Box at the post office', 'that is mailing'),
          ('The registered agent service\'s office', 'that is for papers'),
          ('The flour supplier\'s warehouse address', 'not the bakery'), 'The storefront is where it operates.'),
        Q('Which address should a supplier use to send a monthly bill?', 'The mailing address',
          ('The registered agent address for lawsuits', 'for legal papers'),
          ('A customer\'s home address', 'not the business'),
          ('The state filing office address', 'not the business'), 'Ordinary bills go to the mailing address.'),
        Q('A registered agent service costs 125 dollars a year and a PO Box costs 90 dollars a year. What is the yearly '
          'total for both?', '215 dollars', ('125 dollars, the agent service alone', 'only one item'),
          ('35 dollars, the difference', 'subtracted'), ('90 dollars, the PO Box alone', 'only one item'),
          '125 + 90 = 215 dollars (example prices).', calc=lambda: 125 + 90 == 215),
        Q('Kai lists his home as all three addresses. What is one tradeoff?', 'His home address may appear in public records',
          ('He can never receive any packages', 'packages can arrive'),
          ('His LLC automatically becomes invalid in the state', 'no such rule'),
          ('His taxes are automatically doubled', 'no such rule'), 'Convenience versus privacy.'),
    ]),
    F2=sec('Handle the complications: moves, privacy and state differences', ADDR, [
        Q('An owner moves her business to a new building. Which records may need updating?', 'State filings, bank, licenses and mailing lists',
          ('Only the logo on her social media page', 'not enough'), ('Nothing, because addresses update themselves', 'not automatic'),
          ('Only her personal library card', 'not business records'), 'Address changes must be reported to each place.'),
        Q('A friend in another state says PO Boxes are fine for registered agents everywhere. What should the owner do?',
          'Check her own state\'s official rules', ('Follow the friend because all states match', 'they differ'),
          ('Use a PO Box and hope the state accepts it', 'may be rejected'), ('Skip naming a registered agent', 'usually required'),
          'State rules differ.'),
        Q('A registered agent service forwards legal papers by email. What should the owner do when one arrives?',
          'Read it promptly, because legal papers can have deadlines', ('Ignore it until year end', 'deadlines may pass'),
          ('Delete it if the subject line looks boring or routine', 'may be important'), ('Forward it to customers', 'not appropriate'),
          'Legal papers often require timely action.'),
        Q('Which statement about public records is accurate?', 'Some business addresses are visible to the public.',
          ('Every business address is always kept secret.', 'not true'), ('Only email addresses are public.', 'not true'),
          ('Public records never include addresses.', 'not true'), 'Plan with privacy in mind.'),
        Q('Which source should confirm address rules for a filing?', 'The state\'s official filing office or website',
          ('A post on a neighborhood message board', 'unreliable'), ('A guess based on another state\'s rule', 'differs'),
          ('A shipping company\'s ad', 'not the rule maker'), 'Official sources give the current rule.'),
    ]))

# ------------------------------------------------------------------ Set 39: PO Box, private mailbox, street addressing
BOX = ('A PO BOX is a locked mailbox rented at a Post Office. Some carriers (like private package companies) need a street '
       'address. At participating Post Offices, the "Street Addressing" option lets a box holder use the Post Office\'s '
       'street address with the box number, so those carriers can deliver; availability varies and the customer signs '
       'an agreement. A PRIVATE MAILBOX is rented from a private store called a Commercial Mail Receiving Agency (CMRA). '
       'To receive mail there, the customer completes USPS Form 1583 with identity documents; requirements have '
       'changed over time, so check the current form.')

s39 = SET('ENT.MAIL.02',
    M=sec('Compare PO Boxes, private mailboxes and PO Box street addressing', BOX, [
        Q('Where is a PO Box rented?', 'At a Post Office',
          ('At a bank branch near the business', 'not a PO Box'),
          ('At the state business filing office', 'not a PO Box'),
          ('At any coffee shop that sells stamps', 'not a PO Box'), 'PO Boxes are rented from the Postal Service.'),
        Q('What does the Street Addressing option allow?', 'Using the Post Office\'s street address with the box number',
          ('Using any home address on the street as if it were the box', 'not allowed'),
          ('Skipping the box rental fee for a year', 'not the purpose'),
          ('Receiving legal papers in every state', 'agent rules differ'),
          'It lets carriers that need a street address deliver.'),
        Q('What is a CMRA?', 'A private business that receives mail for customers',
          ('A government agency that issues tax ID numbers to businesses', 'that is the IRS'),
          ('A type of business bank account', 'not a bank account'),
          ('A state rule for registered agents', 'not a rule'), 'CMRAs offer private mailboxes.'),
        Q('Which form is used so a CMRA can receive mail for a customer?', 'USPS Form 1583',
          ('IRS Form SS-4 for an EIN', 'that is a tax form'), ('A state DBA certificate', 'a name filing'),
          ('A city business license form', 'local permission'), 'Form 1583 authorizes the CMRA.'),
        Q('Is Street Addressing offered at every Post Office?', 'No; availability varies',
          ('Yes, at every single location', 'not everywhere'), ('Only at locations in large cities', 'not stated'),
          ('Only for customers with no business', 'not the rule'), 'Ask the specific Post Office.'),
    ]),
    B=[cs('Lockers at a gym', 'Think of renting a locker at a gym. A PO Box is like a locker at the post office: you get a '
          'key and your mail waits there. A private mailbox is like a locker at a private shop that holds mail for you, '
          'and you sign a form so the shop may accept your mail. Some delivery companies only drop off at a street '
          'address, so some post offices let you write their street address plus your locker number.', [
        Q('A PO Box is like a locker where?', 'At the post office', ('At a private shop', 'that is a private mailbox'),
          ('At your house', 'no'), ('At the bank', 'no'), 'PO Boxes are at post offices.'),
        Q('A private mailbox is like a locker where?', 'At a private shop', ('At the post office', 'that is a PO Box'),
          ('At the state office', 'no'), ('At a school', 'no'), 'Private stores offer them.'),
        Q('Why sign a form at the private shop?', 'So the shop may accept your mail', ('To get a discount', 'not the reason'),
          ('To change your name', 'no'), ('To open a bank account at the shop', 'no'), 'Permission is required.'),
        Q('Why do some post offices offer a street address?', 'Some carriers deliver only to street addresses',
          ('To make the lockers bigger for packages', 'no'), ('To lower taxes', 'no'), ('To replace the key', 'no'),
          'It helps carriers that need a street address.'),
        Q('What do you add to the post office\'s street address?', 'Your box number', ('Your phone number', 'no'),
          ('Your birthday', 'no'), ('Your logo', 'no'), 'The box number routes the mail.'),
    ], why='A learner who misses MAIN may not picture the options; gym lockers make them concrete.')],
    F1=sec('Apply it: pick a mailbox option', BOX, [
        Q('Ana ships products and her suppliers use private package carriers that need a street address. She rents a PO '
          'Box. What should she ask her Post Office?', 'Whether it offers the Street Addressing option', ('Whether it sells padded envelopes in bulk at a discount', 'not the need'),
          ('Whether it can file her taxes', 'no'), ('Whether it is open on holidays', 'not the need'),
          'Street Addressing can let those carriers deliver.'),
        Q('Ben rents a box at a private mail store. What must he complete so the store may receive his mail?',
          'USPS Form 1583 with identity documents', ('An IRS application for a new EIN number', 'not this purpose'),
          ('A trademark application', 'not this purpose'), ('A business license renewal', 'not this purpose'),
          'Form 1583 authorizes the CMRA.'),
        Q('A PO Box costs 40 dollars for 3 months. What is the cost for 12 months at the same rate?', '160 dollars',
          ('120 dollars, three times the fee', 'miscounted periods'), ('40 dollars, the same as 3 months', 'only one period'),
          ('480 dollars, twelve times the fee', 'multiplied by months'), '12 / 3 = 4 periods; 4 x 40 = 160 dollars (example price).',
          calc=lambda: 12 // 3 * 40 == 160),
        Q('A private mailbox costs 25 dollars a month; a PO Box costs 160 dollars a year. How much more does the private '
          'mailbox cost per year?', '140 dollars', ('300 dollars, the private box alone', 'not the difference'),
          ('135 dollars, a small miscalculation', 'arithmetic slip'), ('160 dollars, the PO Box alone', 'not the difference'),
          '25 x 12 = 300; 300 - 160 = 140 dollars (example prices).', calc=lambda: 25 * 12 - 160 == 140),
        Q('Which option is run by a private business?', 'A private mailbox at a CMRA', ('A PO Box at the Post Office', 'postal'),
          ('PO Box Street Addressing', 'postal'), ('Home mail delivery by the Postal Service', 'postal'),
          'CMRAs are private businesses.'),
    ]),
    F2=sec('Handle the complications: rules that change and limits', BOX, [
        Q('An online article from several years ago explains Form 1583 steps. What is the concern?', 'Requirements have changed, so check the current form',
          ('Nothing; postal forms never change', 'they can change'), ('The form no longer exists for anyone', 'not stated'),
          ('Online articles are always newer than the official forms', 'not true'), 'Use the current form and the provider\'s instructions.'),
        Q('An owner wants to use her private mailbox as her registered agent address in Washington. What is the issue?',
          'Washington does not allow private or virtual mailboxes for it', ('No issue; any box works in every state', 'not in Washington'),
          ('Private mailboxes cannot receive any mail or packages at all', 'they can'), ('It must be a PO Box instead', 'also not allowed there'),
          'The agent needs a physical in-state street address.'),
        Q('A box holder using Street Addressing gives a package carrier the address. What must be included?', 'The box number with the Post Office street address',
          ('Only the Post Office street address with no box number', 'mail cannot be routed'),
          ('Her home address instead', 'defeats the purpose'), ('The Post Office\'s phone number', 'not an address'),
          'The box number is part of the address.'),
        Q('A mail store closes suddenly. What should an owner using it do first?', 'Update her mailing address with banks, customers and agencies',
          ('Wait a few months to see if her mail still arrives somewhere', 'risky'), ('Do nothing; mail forwards itself forever', 'not guaranteed'),
          ('Close the business entirely', 'too extreme'), 'A changed mailing address must be updated everywhere.'),
        Q('Which statement is accurate?', 'Availability and rules vary, so confirm with the Post Office or provider.',
          ('Every Post Office offers every service at the same price nationwide.', 'not true'), ('Private mailboxes need no paperwork.', 'Form 1583 applies'),
          ('PO Boxes are free.', 'they are rented'), 'Check the specific location.'),
    ]))

# ------------------------------------------------------------------ Set 40: which address each organization accepts
ACCEPT = ('Different organizations accept different addresses. The STATE often requires a physical in-state street '
          'address for the registered agent; Washington, for example, does not accept PO Boxes or private mailboxes '
          'there, though a PO Box may be listed as a separate mailing address. Some PACKAGE CARRIERS cannot deliver to '
          'a plain PO Box; Street Addressing at participating Post Offices can help. BANKS and some licensing offices '
          'may ask for a physical address. Before filing any form, read what kind of address it asks for.')

s40 = SET('ENT.MAIL.03',
    M=sec('Match each organization to the kind of address it accepts', ACCEPT, [
        Q('In Washington, what can be listed separately as a mailing address?', 'A PO Box',
          ('Nothing other than the agent\'s address', 'a separate mailing address is allowed'),
          ('A made-up address that sounds official', 'false information'),
          ('The address of another state\'s office', 'not appropriate'), 'A PO Box can be the mailing address.'),
        Q('Why might a package carrier fail to deliver to a plain PO Box?', 'Some carriers need a street address',
          ('PO Boxes are only for postcards and nothing else', 'boxes hold more'),
          ('Package carriers deliver only to banks', 'not true'),
          ('Packages are not allowed for businesses', 'not true'), 'Street addresses are needed by some carriers.'),
        Q('What should an owner do before filling in an address on a form?', 'Read what kind of address the form asks for',
          ('Use whichever address is shortest to write', 'may be the wrong kind'),
          ('Leave the address line blank to stay private', 'forms may be rejected'),
          ('Copy an address from a competitor\'s form', 'false information'), 'Each form may require a specific type.'),
        Q('Which organization may require a physical address when opening an account?', 'A bank',
          ('A customer buying one product online', 'not usually'), ('A social media follower', 'not relevant'),
          ('A supplier of packing tape', 'not usually'), 'Banks may ask for a physical address.'),
        Q('Which address does a state usually require for the registered agent?', 'A physical in-state street address',
          ('Any email address the owner checks', 'not a physical address'), ('A PO Box in any state', 'often not allowed'),
          ('A phone number with voicemail', 'not an address'), 'Agents need a physical location.'),
    ]),
    B=[cs('Different doors accept different deliveries', 'Imagine a school. The office accepts official letters, the loading '
          'dock accepts big deliveries, and the classroom accepts homework. Sending a truck to the classroom does not '
          'work. Organizations are similar: the state wants a real street address for legal papers, some carriers need a '
          'street address for packages, and ordinary letters can go to a PO Box.', [
        Q('Where do big deliveries go at the school?', 'The loading dock', ('The classroom', 'homework only'),
          ('The office mail tray', 'letters'), ('The parking lot', 'not a door'), 'Each door has its own job.'),
        Q('Ordinary letters for a business can often go where?', 'A PO Box', ('Only a registered agent', 'not ordinary mail'),
          ('A loading dock only', 'no'), ('Nowhere', 'they must go somewhere'), 'Letters often go to a box.'),
        Q('Legal papers usually need what kind of address?', 'A real street address', ('An email only', 'not usually'),
          ('Any PO Box', 'often not allowed'), ('A phone number with voicemail', 'not an address'), 'Papers need a physical place.'),
        Q('Some packages need what kind of address?', 'A street address', ('A PO Box only', 'some carriers cannot'),
          ('A phone number', 'no'), ('A website', 'no'), 'Some carriers need a street address.'),
        Q('Sending a truck to a classroom is like what mistake?', 'Using the wrong address type', ('Using a pen', 'no'),
          ('Paying a bill', 'no'), ('Writing a short letter to a friend', 'no'), 'Match the address to the job.'),
    ], why='A learner who misses MAIN may not see why one address does not fit all; a school\'s doors show the idea.')],
    F1=sec('Apply it: fill in the right address', ACCEPT, [
        Q('Tom\'s Washington LLC form asks for the registered agent address and a mailing address. He has a PO Box and '
          'an agent service. What fits?', 'Agent service address for the agent; PO Box for mailing', ('PO Box for both lines', 'not allowed for the agent'),
          ('Agent service for mailing and PO Box for the agent', 'reversed'), ('Leave both lines blank', 'rejected'),
          'Match each line to the allowed type.'),
        Q('A supplier ships by a private carrier that cannot deliver to plain PO Boxes. The owner\'s Post Office offers '
          'Street Addressing. What should she give the supplier?', 'The Post Office street address with her box number',
          ('Her plain PO Box number only', 'carrier cannot deliver'), ('The registered agent\'s address', 'not for packages'),
          ('A neighbor\'s street address, without asking first', 'not appropriate'), 'Street Addressing helps here.'),
        Q('Of 5 forms, 2 require a physical street address and the rest accept a PO Box. How many accept a PO Box?', '3',
          ('2, the forms needing a street address', 'reversed'), ('5, every one of the forms', 'not all'),
          ('7, the two numbers added', 'added'), '5 - 2 = 3 forms.', calc=lambda: 5 - 2 == 3),
        Q('A bank form asks for the business\'s physical address. The owner works from home. What should she write?',
          'Her actual home address, if that is where the business operates', ('Her PO Box number, labeled on the form as her physical address', 'not physical'),
          ('A fake address for privacy', 'false information'), ('The bank\'s own address', 'not her business'),
          'Give truthful information of the requested type.'),
        Q('Which address type is most often accepted for ordinary bills and letters?', 'A mailing address such as a PO Box',
          ('Only the registered agent address', 'not required for bills'), ('Only a storefront address', 'not required'),
          ('Only an overseas address', 'not appropriate'), 'Mailing addresses handle ordinary mail.'),
    ]),
    F2=sec('Handle the complications: rejected forms and mixed rules', ACCEPT, [
        Q('A state rejected a filing because the agent address was a private mailbox. What should the owner do?', 'Name an agent with a physical in-state address and refile',
          ('File the same form again unchanged', 'will be rejected again'), ('Give up on forming the LLC', 'not necessary'),
          ('Use a PO Box instead of the private mailbox and refile', 'also often rejected'), 'Fix the address type.'),
        Q('A licensing office asks for a physical address but the owner has only a PO Box. What should she do?',
          'Ask the office what address it accepts for her situation', ('Write the PO Box anyway and call it her physical address', 'misleading'),
          ('Skip the license', 'not compliant'), ('Use a random street address', 'false information'),
          'Ask the issuer when unsure.'),
        Q('Which mistake is most likely to cause missed legal papers?', 'Listing an address where no one receives documents',
          ('Listing a PO Box as the ordinary mailing address', 'often fine'), ('Using a business email for customers', 'fine'),
          ('Printing the address on invoices', 'fine'), 'The agent address must be monitored.'),
        Q('An owner used three different addresses on her forms. Is that wrong?', 'Not necessarily, if each fits the form\'s request',
          ('Yes, businesses may only have one address', 'not true'), ('Yes, it is always illegal', 'not true'),
          ('Yes, the bank will close her account', 'not necessarily'), 'Different forms can need different types.'),
        Q('Which statement is accurate?', 'Address rules depend on the organization and state, so read each form.',
          ('Every organization accepts a PO Box for every kind of address.', 'not true'), ('No organization accepts PO Boxes.', 'not true'),
          ('Only email addresses matter today.', 'not true'), 'Check each requirement.'),
    ]))

# ------------------------------------------------------------------ Set 41: mailbox practicalities
PRACT = ('Practical choices matter once you have a mailbox. PO Boxes come in sizes and are rented for set periods, such '
         'as 3, 6 or 12 months; fees vary by location and size. Plan how often you will check it: important letters, '
         'such as tax notices or bills, can have deadlines. Decide who may pick up mail, keep keys safe, and ask how '
         'large packages are handled. When moving, update your address with banks, customers and agencies; forwarding '
         'may help for a while but does not replace updating records. Renew before the rental period ends.')

s41 = SET('ENT.MAIL.04',
    M=sec('Plan box size, checking, renewals and address updates', PRACT, [
        Q('Why plan how often to check a business mailbox?', 'Important letters can have deadlines',
          ('Mail disappears after exactly one day', 'not the reason'),
          ('Checking often lowers the rental fee', 'not how fees work'),
          ('Boxes must be emptied every hour by law', 'no such rule'), 'Bills and notices may need action.'),
        Q('What may happen if a box rental is not renewed?', 'The box can be closed and mail disrupted',
          ('The box becomes free for life', 'not how rentals work'),
          ('The Post Office files the owner\'s taxes', 'not its job'),
          ('Mail is automatically sent to customers', 'not how it works'), 'Renew before the period ends.'),
        Q('When moving, what should the owner do besides forwarding mail?', 'Update the address with banks, customers and agencies',
          ('Nothing, because forwarding fixes everything forever', 'not a full fix'),
          ('Only change the logo on her website', 'not an address update'),
          ('Cancel the business bank account', 'not required'), 'Records still need updating.'),
        Q('What do PO Box fees depend on?', 'Location and box size', ('The owner\'s age and height', 'irrelevant'),
          ('How many products the business sells', 'not the basis'), ('The business\'s logo colors', 'irrelevant'),
          'Fees vary by location and size.'),
        Q('Which is a good practice for mailbox keys?', 'Keep them safe and decide who may use them',
          ('Tape a spare key to the outside of the box', 'unsafe'), ('Give keys to any customer who asks', 'unsafe'),
          ('Never decide who picks up mail', 'causes confusion'), 'Control access to business mail.'),
    ]),
    B=[cs('Renting a storage unit', 'Renting a mailbox is like renting a small storage unit. You pick a size, pay for a set '
          'period, keep the key safe, and check on it regularly. If you forget to pay, the unit can be closed. If you '
          'move your things, you tell people your new location. A business mailbox works the same way, with letters '
          'and packages instead of boxes of belongings.', [
        Q('Choosing a mailbox size is like what?', 'Choosing a storage unit size', ('Choosing a movie to watch', 'no'),
          ('Choosing a meal', 'no'), ('Choosing a song', 'no'), 'Pick a size that fits.'),
        Q('What happens if you forget to pay for the unit?', 'It can be closed', ('It becomes free', 'no'),
          ('It gets bigger', 'no'), ('Nothing at all', 'it can be closed'), 'Renewal matters.'),
        Q('Why check the unit regularly?', 'To find important items in time', ('To make it heavier', 'no'),
          ('To lower taxes', 'no'), ('To change the color of its door', 'no'), 'Regular checks catch deadlines.'),
        Q('What should you do with the key?', 'Keep it safe', ('Lose it', 'no'), ('Share it with strangers', 'unsafe'),
          ('Leave it in the lock', 'unsafe'), 'Protect access.'),
        Q('If you move, what do you tell people?', 'Your new location', ('Your old location', 'no'), ('Nothing', 'no'),
          ('A fake location', 'no'), 'Update your address.'),
    ], why='A learner who misses MAIN may not think through the practical steps; a storage unit is a familiar rental.')],
    F1=sec('Apply it: budget and schedule a mailbox', PRACT, [
        Q('A small box costs 60 dollars for 6 months and a medium box costs 95 dollars for 6 months. How much more does '
          'the medium box cost per year?', '70 dollars', ('35 dollars, the 6-month difference', 'only half a year'),
          ('190 dollars, the medium box per year', 'not the difference'), ('120 dollars, the small box per year', 'not the difference'),
          '(95 - 60) x 2 = 70 dollars (example prices).', calc=lambda: (95 - 60) * 2 == 70),
        Q('Mia receives tax notices that give 30 days to respond. She checks her box once a month. What is a better plan?',
          'Check at least weekly', ('Check once a year', 'too rare'), ('Never check; notices arrive by email', 'not always'),
          ('Check only when she remembers', 'unreliable'), 'More frequent checks leave time to respond.'),
        Q('A box was rented on March 1 for 6 months. When does it need renewal?', 'By September 1',
          ('By April 1, one month later', 'too early'), ('By March 1 next year', 'a year is too long'),
          ('Never; rentals last forever', 'they expire'), 'March + 6 months = September.', calc=lambda: (3 + 6) == 9),
        Q('An owner\'s employee picks up mail. What should the owner set up?', 'Clear permission and a key for that employee only',
          ('A key hidden under the doormat', 'unsafe'), ('No rules about who collects mail', 'confusing'),
          ('A sign on the wall that lists the box\'s lock combination', 'unsafe'), 'Control who has access.'),
        Q('A business moved and set up mail forwarding. Six months later some mail still goes to the old address. What '
          'is the fix?', 'Update the address directly with those senders', ('Rely on forwarding forever', 'it may end'),
          ('Ignore the misdirected mail', 'risky'), ('Move the business back to the old address', 'unnecessary'),
          'Senders need the new address.'),
    ]),
    F2=sec('Handle the complications: packages, travel and missed mail', PRACT, [
        Q('A package is too large for the box. What should the owner ask the Post Office?', 'How it handles packages that do not fit',
          ('Whether it can deliver to her neighbor without asking', 'not appropriate'),
          ('Whether packages are banned for businesses', 'not true'), ('Whether she must rent ten boxes', 'not necessary'),
          'Many locations hold packages for pickup; ask how.'),
        Q('An owner travels for three weeks. What is a sensible plan for her business mail?', 'Arrange for a trusted person or a hold service',
          ('Let mail pile up and hope nothing is urgent', 'risky'), ('Close the box for the trip', 'disrupts mail'),
          ('Ask customers to stop writing', 'unrealistic'), 'Plan coverage while away.'),
        Q('A late fee notice arrived in the box two weeks ago, but she checked late. What lesson fits?', 'Regular checks prevent missed deadlines',
          ('Late fees are always forgiven if you ask', 'not always'), ('Mailboxes cause late fees', 'missed checking did'),
          ('Bills never matter', 'they do'), 'Build a checking routine.'),
        Q('Box rent rises from 120 to 150 dollars a year. What is the percent increase?', '25 percent',
          ('30 percent, the dollar change', 'used dollars as percent'), ('20 percent, based on the new price', 'wrong base'),
          ('150 percent, the new price', 'not the increase'), '(150 - 120) / 120 = 0.25 = 25 percent.',
          calc=lambda: (150 - 120) / 120 == 0.25),
        Q('Which statement is accurate?', 'Fees and services vary by location, so ask the specific Post Office.',
          ('Every Post Office charges the same price for every box size.', 'not true'), ('Boxes never need renewal.', 'not true'),
          ('Forwarding replaces updating records.', 'not true'), 'Confirm locally.'),
    ]))

# ------------------------------------------------------------------ Set 42: business email, phone and voicemail
CONTACT = ('Customers judge a business by how easy it is to reach. A BUSINESS EMAIL that uses the company\'s own web '
           'domain (like hello@yourshop.example) looks more established than a free personal address. A separate '
           'business phone number (a second line or a calling app) keeps personal and business calls apart and protects '
           'privacy. Record a short voicemail greeting with the business name and when callers can expect a reply. '
           'Then answer within the time you promise; a clear, kept promise builds trust.')

s42 = SET('ENT.MAIL.05',
    M=sec('Set up professional email, phone and voicemail', CONTACT, [
        Q('Which email address looks most established for a business called Lime Tree Pets?', 'hello@limetreepets.example',
          ('limetreefan2003@freemail.example', 'personal style'), ('catsrule99@freemail.example', 'unrelated name'),
          ('xyz123@freemail.example', 'random'), 'An address on the business domain looks established.'),
        Q('Why use a separate business phone number?', 'It separates business calls and protects privacy',
          ('It doubles the number of customers each month', 'not guaranteed'),
          ('It is required for every business by federal law', 'not a universal law'),
          ('It removes the need for any email', 'still useful'), 'Separation and privacy are the main benefits.'),
        Q('What should a business voicemail greeting include?', 'The business name and when to expect a reply',
          ('The owner\'s home address and birthday', 'privacy risk'), ('A long story about the founder', 'too long'),
          ('Nothing; silence is professional', 'confusing'), 'Name and response time help callers.'),
        Q('A greeting promises a reply within one business day. What builds trust?', 'Actually replying within one business day',
          ('Replying whenever convenient, even a week later', 'breaks the promise'),
          ('Deleting messages from unknown numbers', 'loses customers'),
          ('Changing the promise every week', 'confusing'), 'Kept promises build trust.'),
        Q('What is a web domain?', 'The business\'s own website name, like yourshop.example',
          ('A type of business bank account', 'not a domain'), ('A state filing that registers the business\'s legal name', 'that is a DBA or entity'),
          ('A shipping label format', 'not a domain'), 'A domain can also host email.'),
    ]),
    B=[cs('A shop\'s front window and bell', 'A clean shop window and a bell that works tell customers someone is ready to '
          'help. Email, phone and voicemail are a modern shop\'s window and bell. A business email on the shop\'s own '
          'web name looks tidy; a separate phone keeps business calls from mixing with family calls; and a voicemail '
          'greeting says who you are and when you will call back.', [
        Q('A business email on its own web name is like what?', 'A clean shop window', ('A broken shop bell', 'no'),
          ('A locked door', 'no'), ('A dark sign', 'no'), 'It looks tidy and ready.'),
        Q('Why keep a separate business phone?', 'To keep business calls apart from family calls', ('To get more ads', 'no'),
          ('To avoid hearing from any customers at all', 'no'), ('To raise prices', 'no'), 'Separation helps.'),
        Q('A voicemail greeting should say what?', 'Who you are and when you will call back', ('Nothing', 'no'),
          ('Your bank PIN and online password', 'unsafe'), ('A joke only', 'not helpful'), 'Name and timing.'),
        Q('A bell that works tells customers what?', 'Someone is ready to help', ('The shop is closed for good', 'no'),
          ('Prices went up', 'no'), ('The owner left', 'no'), 'Reachability builds trust.'),
        Q('Email, phone and voicemail are like what for a modern shop?', 'Its window and bell', ('Its roof', 'no'),
          ('Its basement', 'no'), ('Its back parking lot', 'no'), 'They are how customers reach you.'),
    ], why='A learner who misses MAIN may not see why contact details matter; a shop window and bell are familiar.')],
    F1=sec('Apply it: improve contact details', CONTACT, [
        Q('Rita\'s flyers list "rita.party.girl@freemail.example." She owns ritasbakes.example. What is the best change?',
          'Use an address like orders@ritasbakes.example', ('Keep the personal address on every flyer', 'less established'),
          ('Remove all contact details from the flyer', 'customers cannot reach her'),
          ('List her home address instead of email', 'privacy risk'), 'A domain address looks professional.'),
        Q('Leo answers business calls on his personal phone at family dinners. What helps most?', 'A separate business number with set hours',
          ('Answering every call at any hour', 'stressful'), ('Never answering business calls', 'loses customers'),
          ('Giving customers his family\'s numbers', 'privacy risk'), 'Separation sets boundaries.'),
        Q('A business gets 40 voicemails a month and promises a same-day reply. It replies same day to 34. What percent '
          'met the promise?', '85 percent', ('34 percent, the count itself', 'not a percent of 40'),
          ('15 percent, the ones missed', 'reversed'), ('6 percent, the number missed', 'not a percent'),
          '34 / 40 = 0.85 = 85 percent.', calc=lambda: 34 / 40 == 0.85),
        Q('Which voicemail greeting is best?', '"You\'ve reached Pine Cleaners. We reply within one business day."',
          ('"Hey, it\'s me. Leave something after the beep, maybe I\'ll call."', 'unclear'), ('"This number is unavailable forever."', 'confusing'),
          ('"Call my cousin instead at home."', 'unprofessional'), 'Clear name and promise.'),
        Q('A customer emails on Saturday; the business replies Monday as its auto-reply promised. Was the promise kept?',
          'Yes, it matched what was promised', ('No, every email needs a reply in minutes', 'not what was promised'),
          ('No, weekends are banned for email', 'not true'), ('Only if the reply was very long', 'length is not the test'),
          'Keeping the stated promise builds trust.'),
    ]),
    F2=sec('Handle the complications: privacy, overload and scams', CONTACT, [
        Q('Customers call at midnight. What is a reasonable boundary?', 'State business hours in the greeting and reply then',
          ('Answer every midnight call to keep them happy', 'unsustainable'), ('Block all customer numbers', 'loses customers'),
          ('Give out a personal number for night calls', 'privacy risk'), 'Set and share clear hours.'),
        Q('An email claims to be from the owner\'s bank and asks for her password. What should she do?', 'Contact the bank through its official number',
          ('Reply with the password quickly', 'scam risk'), ('Click the email link and log in to check', 'scam risk'),
          ('Forward it to customers', 'not helpful'), 'Verify through official channels.'),
        Q('The owner\'s inbox gets 200 messages a week and replies are slipping. Which step helps most?', 'Use folders or templates for common questions',
          ('Delete every message unread', 'loses customers'), ('Stop listing any email address', 'customers cannot reach her'),
          ('Promise faster replies she cannot meet', 'breaks trust'), 'Organized tools save time.'),
        Q('A greeting promises a reply in one hour, but the owner is often away for half a day. What should change?',
          'Promise a time she can actually meet', ('Keep the promise and miss it often', 'breaks trust'),
          ('Remove the voicemail entirely', 'confusing'), ('Never check messages', 'loses customers'),
          'Promises should be realistic.'),
        Q('Which statement is accurate?', 'Clear, realistic response promises build more trust than fast but broken ones.',
          ('Customers never care about replies.', 'they do'), ('Free email addresses are illegal for any business to use for customer messages.', 'not illegal'),
          ('A business must answer every call at any hour.', 'not required'), 'Reliability builds trust.'),
    ]))

SETS = [s38, s39, s40, s41, s42]
