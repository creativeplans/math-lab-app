"""Entrepreneurship sets 30-37: Foundation 5, tax IDs and business banking."""
from eq import Q, sec, cs, SET

# ------------------------------------------------------------------ Set 30: what an EIN is
EIN = ('An EIN (Employer Identification Number) is a nine-digit number the IRS (the federal tax agency) gives a '
       'business to identify it for federal taxes, much like a Social Security number identifies a person. Businesses '
       'that hire employees, most partnerships and corporations, and many LLCs need one. Banks often ask for it when '
       'opening a business account. Even a sole proprietor without employees may choose to get one so she can give '
       'clients the EIN instead of her Social Security number. The IRS says an EIN is free: you never have to pay a '
       'fee for one.')

s30 = SET('ENT.ID.01',
    M=sec('Explain what an EIN is and who usually needs one', EIN, [
        Q('What is an EIN?', 'A federal tax ID number for a business',
          ('A state license that lets a business sell food', 'that is a permit'),
          ('A credit score assigned to new businesses', 'not a credit score'),
          ('A registered trademark for a business name', 'trademarks are separate'),
          'The IRS issues EINs to identify businesses for federal taxes.'),
        Q('Which agency issues EINs?', 'The IRS', ('The state\'s business licensing office', 'states issue other IDs'),
          ('The US Postal Service', 'it handles mail'), ('The patent and trademark office', 'it handles trademarks'),
          'The IRS is the federal tax agency.'),
        Q('How much does the IRS charge for an EIN?', 'Nothing; it is free',
          ('A 50-dollar filing fee paid online', 'the IRS says there is no fee'),
          ('A yearly fee based on sales', 'there is no fee'),
          ('A fee set by each county', 'the EIN is federal and free'),
          'The IRS states you never have to pay a fee for an EIN.'),
        Q('Which business most clearly needs an EIN?', 'A shop that hires its first employee',
          ('A hobby blogger who earns no money at all', 'not a business with tax needs'),
          ('A child selling lemonade one afternoon', 'not a formal business'),
          ('A person who only buys from businesses', 'a customer, not a business'),
          'Hiring employees is a common reason an EIN is required.'),
        Q('Why might a sole proprietor with no employees still get an EIN?', 'To give clients an EIN instead of her SSN',
          ('Because it automatically creates an LLC for her', 'it does not create an entity'),
          ('Because it removes the need to pay income tax', 'taxes still apply'),
          ('Because it protects her house from business debts', 'no liability protection'),
          'An EIN can keep her Social Security number more private.'),
    ]),
    B=[cs('An ID number for the business', 'People have Social Security numbers so the government can match their tax '
          'records. A business can have its own ID number too: the EIN. When the business files taxes, pays employees, '
          'or opens a bank account, the EIN tells everyone which business it is. The number does not make the business '
          'legal or protect the owner; it is simply an ID, like a student ID number at school.', [
        Q('An EIN is most like which of these?', 'A student ID number', ('A house key', 'not an ID'),
          ('A shop\'s front sign', 'not an ID'), ('A bank loan', 'not an ID'), 'It identifies the business.'),
        Q('A person\'s tax ID is usually what?', 'A Social Security number', ('A phone number', 'not a tax ID'),
          ('A home street address', 'not a tax ID'), ('A zip code', 'not a tax ID'), 'People use an SSN for taxes.'),
        Q('What does the EIN tell the IRS?', 'Which business the records belong to', ('The owner\'s favorite color and hobbies', 'no'),
          ('How good the products are', 'no'), ('Where to buy supplies', 'no'), 'It matches records to the business.'),
        Q('Does an EIN protect the owner from debts?', 'No, it is only an ID number', ('Yes, from every debt', 'no'),
          ('Yes, but only for LLC owners', 'no'), ('Yes, in every state', 'no'), 'It does not change liability.'),
        Q('When might a bank ask for an EIN?', 'When opening a business bank account', ('When buying a coffee', 'no'),
          ('When checking the weather', 'no'), ('When paying at a city parking meter', 'no'), 'Banks often ask for it.'),
    ], why='A learner who misses MAIN may not know what the number is for; a familiar ID number explains its purpose.')],
    F1=sec('Apply it: decide whether to get an EIN', EIN, [
        Q('Dee runs a one-person bookkeeping service as a sole proprietor. Clients ask for a tax ID on forms. She does not '
          'want to share her SSN widely. What fits?', 'Get a free EIN and give clients that number',
          ('Make up a nine-digit number for the forms', 'false information'),
          ('Refuse all clients who ask for a tax ID', 'loses business unnecessarily'),
          ('Pay a website 200 dollars, believing it is required', 'the EIN is free from the IRS'),
          'A free EIN can be used instead of her SSN.'),
        Q('Raj is hiring two part-time workers for his food truck. What should he get?', 'An EIN from the IRS',
          ('Only a trademark for the truck\'s name', 'not a tax ID'),
          ('Only a new business email address', 'not a tax ID'),
          ('Only a PO Box for mail', 'not a tax ID'), 'Employers need an EIN.'),
        Q('Which statement about an EIN is accurate?', 'It identifies the business for federal taxes.',
          ('It replaces the business license from the city.', 'licenses are separate'),
          ('It means the business has trademark rights.', 'separate'),
          ('It is issued by the bank that holds the account.', 'the IRS issues it'),
          'Its purpose is federal tax identification.'),
        Q('An EIN has how many digits?', 'Nine', ('Six', 'not the format'), ('Twelve', 'not the format'),
          ('Four', 'not the format'), 'An EIN is a nine-digit number.'),
        Q('Lena formed a two-owner LLC with her brother. What is the most likely situation?', 'The LLC will usually need an EIN',
          ('The LLC can never have an EIN', 'false'), ('Each owner must use the other\'s SSN', 'false'),
          ('The LLC uses the state\'s phone number as its ID', 'false'),
          'Multi-member LLCs are generally partnerships for tax and need an EIN.'),
    ]),
    F2=sec('Handle the complications: fees, privacy and misunderstandings', EIN, [
        Q('A website charges 250 dollars to "obtain your EIN." What should a founder know?', 'The IRS gives EINs for free',
          ('Only paid websites can request EINs', 'the IRS accepts direct applications'),
          ('The 250 dollars is the IRS\'s official fee', 'there is no IRS fee'),
          ('Paying more gives a better EIN', 'no such thing'), 'Third parties may charge, but the IRS does not.'),
        Q('An owner thinks getting an EIN means she now has an LLC. What is the error?', 'An EIN is a tax ID, not a legal entity',
          ('There is no error; EINs create LLCs', 'false'), ('EINs are only for corporations', 'false'),
          ('EINs end the business\'s tax duties', 'false'), 'Entities are formed with the state.'),
        Q('A sole proprietor shares her EIN on an invoice. Compared with sharing her SSN, what is the benefit?',
          'Her Social Security number stays more private', ('She pays no income tax at all', 'false'),
          ('Her invoices become legally binding contracts', 'not how invoices work'),
          ('Her business turns into a corporation', 'false'), 'The EIN limits SSN exposure.'),
        Q('Which source is best to confirm whether a business needs an EIN?', 'The IRS website',
          ('A comment on a social media post', 'unreliable'), ('A competitor\'s guess', 'unreliable'),
          ('An old flyer from a print shop', 'unreliable'), 'The IRS is the official source.'),
        Q('An owner loses track of her EIN. What is a sensible first step?', 'Check earlier IRS letters or bank and tax records',
          ('Apply for many new EINs right away', 'creates confusion'),
          ('Use a random nine-digit number on forms until she finds it', 'false information'),
          ('Stop filing taxes until it turns up', 'creates problems'),
          'The number appears on earlier official records.'),
    ]))

# ------------------------------------------------------------------ Set 31: applying from the official source
APPLY = (('The IRS lets businesses apply for an EIN directly, including online, at no charge. The online application '
         'asks for a "responsible party": an individual who controls the business, with a Social Security number (SSN)'
         ' or ITIN. It is for businesses located in the US or its territories, and it must be completed in one '
         'session. If the business will be an LLC or corporation, the IRS advises forming it with the state first; '
         'applying before the entity exists may delay things. Be careful with look-alike websites that charge fees.'))

s31 = SET('ENT.ID.02',
    M=sec('Apply for an EIN through the official IRS source in the right order', APPLY, [
        Q('Where should an owner apply for an EIN to avoid unnecessary fees?', 'Directly with the IRS',
          ('Through any website that appears first in an ad', 'may charge fees'),
          ('Through the business\'s bank teller', 'the IRS issues EINs'),
          ('Through the city hall front desk', 'not the issuer'), 'Applying directly is free.'),
        Q('What is the "responsible party" on the application?', 'An individual who controls the business',
          ('Any customer who bought something from the business', 'customers do not control it'),
          ('The bank that will hold the business account', 'not a person in control'),
          ('The state office that approved the LLC', 'not the controller'), 'It is a person in control.'),
        Q('What must the responsible party have for the online application?', 'An SSN or ITIN',
          ('A business credit card with a high limit', 'not required'),
          ('A registered trademark for the name', 'not required'),
          ('A college degree in business', 'not required'), 'The online form requires an SSN or ITIN.'),
        Q('An owner is forming an LLC. What order does the IRS advise?', 'Form the LLC with the state, then apply for the EIN',
          ('Apply for the EIN, then decide on a business later', 'may cause delays'),
          ('Open a bank account, then form the LLC years later', 'banks need the entity papers'),
          ('Print invoices, then decide on the business form', 'not the advised order'),
          'Form the entity first to avoid delays.'),
        Q('What does the IRS say about completing the online application?', 'It must be finished in one session',
          ('It can be saved for three weeks and resumed', 'must be completed in one session'),
          ('It must be mailed in on paper afterward', 'not for the online version'),
          ('It must be signed in person at a bank', 'not required'), 'Gather information before starting.'),
    ]),
    B=[cs('The official counter versus a middleman', 'Imagine renewing a library card. You can go to the library desk and do '
          'it for free, or pay a stranger outside to stand in line for you. The stranger may help, but the library '
          'itself does not charge. Applying for an EIN is similar: the IRS is the official counter and does not charge. '
          'Websites that look official may add fees for doing the same thing.', [
        Q('In the story, who is the official counter?', 'The library desk', ('The stranger outside', 'a middleman'),
          ('The parking lot', 'no'), ('A bookstore', 'no'), 'The library issues the card.'),
        Q('For an EIN, who is the official counter?', 'The IRS', ('A paid website', 'a middleman'),
          ('A friend', 'no'), ('A competitor', 'no'), 'The IRS issues EINs.'),
        Q('Does the official counter charge for an EIN?', 'No', ('Yes, 100 dollars', 'no fee'),
          ('Yes, monthly', 'no fee'), ('Only on weekends', 'no fee'), 'The IRS EIN is free.'),
        Q('What might a middleman website add?', 'Its own fee', ('A free gift card', 'not typical'),
          ('A trademark', 'no'), ('A business loan', 'no'), 'Middlemen may charge for convenience.'),
        Q('What is the safest way to avoid extra fees?', 'Use the official IRS site', ('Click the first ad you see', 'may be a middleman'),
          ('Pay whoever asks', 'risky'), ('Guess a number', 'false info'), 'Go to the official source.'),
    ], why='A learner who misses MAIN may not see why the official source matters; the library-counter picture shows it.')],
    F1=sec('Apply it: prepare and apply correctly', APPLY, [
        Q('Pat wants to apply online but has not decided who controls the business with his partner. What should he do '
          'first?', 'Decide who the responsible party is before starting', ('Start and leave the field blank', 'it is required'),
          ('List a loyal customer as the responsible party instead', 'not correct'),
          ('Apply twice, once for each partner', 'creates duplicate EINs'),
          'The application must be completed in one session with that information.'),
        Q('A founder searched "get EIN" and found a site charging 199 dollars that looks official. What should she check?',
          'Whether the web address is the IRS\'s official irs.gov site', ('Whether the site has nice colors', 'not a test'),
          ('Whether the price is lower than another paid EIN website', 'still unnecessary'),
          ('Whether the site has many ads', 'not a test'), 'The official IRS site ends in irs.gov.'),
        Q('Kai plans to form an LLC next month. He wants an EIN today for the future LLC. What does the IRS advise?',
          'Form the LLC first, then apply', ('Apply today; order never matters', 'IRS warns of delays'),
          ('Use his own SSN as the LLC\'s EIN forever', 'not the same thing'),
          ('Skip the EIN entirely for an LLC', 'may still need one'), 'Form the entity first.'),
        Q('Which information should be ready before starting the online application?', 'The business type and responsible party\'s SSN or ITIN',
          ('The logo file, brand colors and a sample of the website', 'not needed'), ('A list of competitors\' prices', 'not needed'),
          ('Next year\'s marketing plan', 'not needed'), 'Gather required details in advance.'),
        Q('Nora saved 199 dollars by applying directly with the IRS instead of a paid site. If she had also avoided a '
          '49-dollar "rush" add-on, how much did she save in total?', '248 dollars', ('199 dollars', 'only the base fee'),
          ('150 dollars', 'the difference'), ('49 dollars', 'only the add-on'),
          '199 + 49 = 248 dollars (example prices).', calc=lambda: 199 + 49 == 248),
    ]),
    F2=sec('Handle the complications: special cases and scams', APPLY, [
        Q('A founder has no SSN or ITIN. What does the IRS page say about the online application?',
          'It requires an SSN or ITIN, so another IRS method may be needed', ('Anyone can apply online without any SSN or ITIN at all', 'not online'),
          ('She can never get an EIN', 'other methods exist'), ('She should use a friend\'s SSN', 'false information'),
          'The online option needs an SSN or ITIN; check the IRS for alternatives.'),
        Q('An email says, "Your EIN expires. Pay 75 dollars to renew." What should the owner do?', 'Treat it as suspicious and check with the IRS directly',
          ('Pay quickly by card so the business does not lose its EIN', 'likely a scam'), ('Reply with her bank details', 'risky'),
          ('Click the link and enter her SSN', 'risky'), 'EINs are free; verify through official channels.'),
        Q('A business is located outside the US. What does the IRS online page say?', 'The online application is for businesses in the US or its territories',
          ('Every business located abroad must use only the online tool', 'not correct'),
          ('Foreign businesses can never get an EIN', 'other methods exist'),
          ('Foreign businesses get EINs from their bank', 'not correct'), 'Check the IRS for other application methods.'),
        Q('An owner started the online form, left for lunch and came back. What might happen?', 'She may need to start again because it is one session',
          ('Her progress is saved for several months automatically', 'not how it works'), ('The IRS mails her the EIN anyway', 'not complete'),
          ('She gets two EINs', 'no'), 'The session must be completed at once.'),
        Q('Which statement is accurate?', 'Rules on the IRS site can change, so check it when applying.',
          ('IRS rules never change.', 'they can change'), ('Paid websites set IRS rules.', 'no'),
          ('Banks decide which businesses are allowed to get an EIN.', 'the IRS does'), 'Official pages give current rules.'),
    ]))

# ------------------------------------------------------------------ Set 32: EIN vs state IDs vs registration
IDS = ('Different numbers and filings do different jobs. The EIN is the FEDERAL tax ID from the IRS. A STATE tax ID or '
       'account may be needed for state taxes, such as collecting sales tax or paying state payroll taxes; it comes '
       'from the state\'s tax agency. BUSINESS REGISTRATION (forming an LLC, or filing a DBA) records the business or its '
       'name with the state or local government. A LICENSE gives permission to operate. Having one does not replace '
       'the others. The SBA lists getting federal and state tax IDs as separate launch steps.')

s32 = SET('ENT.ID.03',
    M=sec('Tell the EIN apart from state tax IDs, registration and licenses', IDS, [
        Q('Which ID is the federal tax ID?', 'The EIN', ('The state sales tax permit', 'state level'),
          ('The DBA certificate number', 'a name filing'), ('The city business license number', 'local permission'),
          'The EIN comes from the IRS.'),
        Q('A shop will collect sales tax. Which ID is it most likely to need from the state?', 'A state tax account or sales tax permit',
          ('Only an EIN from the IRS', 'the EIN is federal'),
          ('Only a trademark registration', 'not a tax ID'),
          ('Only a domain name registration for the site', 'not a tax ID'), 'Sales tax is usually a state matter.'),
        Q('What does business registration (like forming an LLC) do?', 'Records the business with the state',
          ('Gives a federal tax ID number', 'that is the EIN'), ('Collects sales tax for the state', 'the business collects'),
          ('Replaces all business licenses', 'separate'), 'Registration records the business or name.'),
        Q('Does an EIN replace a city business license?', 'No, they do different jobs',
          ('Yes, an EIN covers every permission', 'it does not'),
          ('Yes, but only for food businesses', 'it does not'),
          ('Yes, if the business has an LLC', 'it does not'), 'An EIN is a tax ID, not permission to operate.'),
        Q('According to the SBA launch steps, how are federal and state tax IDs treated?', 'As separate steps',
          ('As one single combined number', 'they are separate'), ('As optional for all businesses', 'not optional for many'),
          ('As the same as a trademark', 'unrelated'), 'They are listed separately.'),
    ]),
    B=[cs('Different cards in a wallet', 'Picture a wallet with a library card, a driver\'s license and a gym card. Each '
          'card is for a different place; the library will not accept your gym card. A business also carries several '
          'IDs and papers: a federal tax ID (EIN) for the IRS, a state tax account for state taxes, a registration '
          'showing it exists, and licenses giving permission to operate. Each is for a different office.', [
        Q('Why can\'t a gym card be used at the library?', 'Each card is for a different place', ('Gym cards are illegal', 'no'),
          ('Libraries are closed', 'not the point'), ('Gym cards are too big to fit in slots', 'not the point'), 'Each card has its own purpose.'),
        Q('The EIN is the card for which office?', 'The IRS', ('The city', 'licenses'), ('The state tax agency', 'state ID'),
          ('The post office', 'mail'), 'The EIN is federal.'),
        Q('A state tax account is the card for which office?', 'The state tax agency', ('The IRS', 'that is the EIN'),
          ('The bank', 'no'), ('The trademark office', 'no'), 'It is for state taxes.'),
        Q('A license is like which wallet card?', 'A pass letting you do something', ('A store receipt from shopping', 'no'),
          ('A coupon', 'no'), ('A photo', 'no'), 'A license grants permission.'),
        Q('Can one business ID replace all the others?', 'No', ('Yes, the EIN', 'no'), ('Yes, the DBA', 'no'),
          ('Yes, any card', 'no'), 'Each serves its own office.'),
    ], why='A learner who misses MAIN may lump IDs together; a wallet of different cards separates them.')],
    F1=sec('Apply it: build an ID and registration checklist', IDS, [
        Q('Mara is opening a retail gift shop LLC with one employee. Which list is most complete?',
          'LLC registration, EIN, state tax account, local license', ('EIN only', 'missing state and local items'),
          ('A local license only, with no tax IDs or LLC filing', 'missing tax IDs and registration'), ('DBA and logo only', 'missing most items'),
          'A retail employer needs several IDs and permissions.'),
        Q('Theo got an EIN and thinks he is ready to collect sales tax. What is missing?', 'A state sales tax permit or account',
          ('Nothing, the EIN covers sales tax', 'state ID needed'), ('A trademark search', 'not for sales tax'),
          ('A new domain name', 'not for sales tax'), 'Sales tax is usually registered with the state.'),
        Q('Which item gives permission to operate in the city?', 'A city business license', ('The EIN', 'tax ID'),
          ('The state tax account', 'tax ID'), ('The DBA filing', 'name filing'), 'Licenses give permission.'),
        Q('A business owner counts 4 required items and has finished 3. What fraction is done?', '3/4',
          ('1/4', 'the part not done'), ('4/3', 'upside down'), ('3/7', 'adds incorrectly'),
          '3 done out of 4 required = 3/4.', calc=lambda: 3 / 4 == 0.75),
        Q('Which source lists federal and state tax IDs as launch steps?', 'The SBA\'s launch guide',
          ('A competitor\'s social media page', 'not official'), ('An old print advertisement', 'not official'),
          ('A random online forum', 'not official'), 'The SBA provides an official overview.'),
    ]),
    F2=sec('Handle the complications: mixing up IDs', IDS, [
        Q('An owner gives a state tax form her EIN in the box for her state account number. What is the problem?',
          'The EIN and state account number are different IDs', ('No problem; the federal and state numbers are always identical', 'not identical'),
          ('The state form needs a trademark', 'no'), ('The state only needs her logo', 'no'),
          'Each form asks for a specific number.'),
        Q('A seller thinks a DBA filing gives her a state tax account. What is the error?', 'A DBA registers a name, not a tax account',
          ('No error; a DBA filing also opens a state tax account', 'false'), ('DBAs are federal IDs', 'false'),
          ('DBAs replace the EIN', 'false'), 'Tax accounts are separate.'),
        Q('A business moves to a new state. Which items should it check?', 'State registration, state tax accounts and local licenses there',
          ('Only its logo colors', 'unrelated'), ('Nothing; every state registration and license transfers automatically', 'not always'),
          ('Only the EIN, which must be replaced', 'the EIN is federal and usually stays'),
          'State and local items depend on the location.'),
        Q('Which statement is accurate?', 'Requirements depend on the state, the activity and whether there are employees.',
          ('Every business in every state needs exactly the same IDs and filings.', 'not true'), ('Only big companies need IDs.', 'not true'),
          ('No business needs a state ID.', 'not true'), 'Check the specific situation.'),
        Q('Where should a founder check state tax ID needs?', 'The state tax agency\'s official website',
          ('The comment section under a business video', 'unreliable'), ('The IRS only', 'the IRS is federal'),
          ('A neighbor\'s guess', 'unreliable'), 'State agencies handle state taxes.'),
    ]))

# ------------------------------------------------------------------ Set 33: separate business bank account
SEP = ('A separate business bank account keeps business money apart from personal money. All business income goes in '
       'and all business expenses come out of it. This makes bookkeeping and taxes easier, shows clearly what the '
       'business earns, and helps support the separation between an LLC or corporation and its owner. Mixing personal '
       'and business money in one account is called COMMINGLING. It makes records confusing and can weaken liability '
       'protection. The SBA lists opening a business bank account as a launch step.')

s33 = SET('ENT.BANK.01',
    M=sec('Explain why business money needs its own account', SEP, [
        Q('What is commingling?', 'Mixing personal and business money',
          ('Opening several savings accounts at once', 'not the meaning'),
          ('Paying taxes on time each quarter', 'not the meaning'),
          ('Keeping receipts in a folder by month', 'that is good record keeping'),
          'Commingling means mixing funds.'),
        Q('What is one benefit of a separate business account?', 'Bookkeeping and taxes are easier',
          ('The business pays no taxes at all', 'taxes still apply'),
          ('The owner never needs to keep receipts', 'records are still needed'),
          ('Customers must pay in cash only', 'unrelated'), 'Clear records simplify bookkeeping.'),
        Q('Which money should go into the business account?', 'All business income',
          ('Only the owner\'s birthday gifts', 'personal money'),
          ('Only cash from personal savings', 'personal money'),
          ('Nothing; it should stay empty', 'the account is for business money'),
          'All business income goes into the business account.'),
        Q('How can commingling affect an LLC owner?', 'It can weaken liability protection',
          ('It always lowers the owner\'s taxes', 'not a benefit'),
          ('It makes the LLC a trademark', 'unrelated'),
          ('It removes the need for licenses', 'unrelated'), 'Mixing funds blurs the line between owner and LLC.'),
        Q('Which purchase belongs on the business account?', 'Packaging supplies for orders', ('The owner\'s groceries', 'personal'),
          ('A family vacation', 'personal'), ('The owner\'s gym membership', 'personal'), 'Business expenses go through the business account.'),
    ]),
    B=[cs('Two jars', 'Imagine two jars on a shelf: one labeled HOME and one labeled BUSINESS. Money from customers goes '
          'in the BUSINESS jar, and business supplies are paid from it. Money for groceries and rent comes from the '
          'HOME jar. If you pour both into one jar, you cannot tell how much the business earned. A separate business '
          'bank account is the BUSINESS jar.', [
        Q('Customer payments go in which jar?', 'The BUSINESS jar', ('The HOME jar', 'personal'),
          ('Neither jar', 'they must go somewhere'), ('A third secret jar', 'no'), 'Business income goes to business.'),
        Q('Groceries are paid from which jar?', 'The HOME jar', ('The BUSINESS jar', 'personal expense'),
          ('Both jars equally', 'no'), ('No jar', 'no'), 'Personal costs come from personal money.'),
        Q('What happens if both jars are poured into one?', 'You cannot tell what the business earned',
          ('The business automatically earns more money', 'no'), ('Taxes disappear', 'no'), ('Nothing changes', 'records get mixed'),
          'Mixing hides the business results.'),
        Q('A business bank account is like which jar?', 'The BUSINESS jar', ('The HOME jar for family money', 'no'),
          ('A cookie jar', 'no'), ('A broken jar', 'no'), 'It holds only business money.'),
        Q('Business supplies are paid from which jar?', 'The BUSINESS jar', ('The HOME jar', 'no'),
          ('A neighbor\'s jar', 'no'), ('No jar', 'no'), 'Business costs come from business money.'),
    ], why='A learner who misses MAIN may not see why separation matters; two labeled jars make the idea concrete.')],
    F1=sec('Apply it: sort transactions into the right account', SEP, [
        Q('Gia\'s client pays 600 dollars for a design project. Where should it be deposited?', 'The business account',
          ('Her personal savings for safekeeping', 'commingling'), ('Her child\'s school account', 'commingling'),
          ('Split randomly between accounts', 'confusing'), 'Business income goes to the business account.'),
        Q('Ben pays for his personal phone and his business software from one personal card. What is the issue?',
          'Business and personal costs are mixed', ('Nothing, one card is always best', 'mixing makes records unclear'),
          ('Software is never a business cost', 'it can be'), ('Phones are illegal for businesses', 'no'),
          'Business costs should come from business funds.'),
        Q('In a month, the business account shows deposits of 3,200 dollars and expenses of 2,450 dollars. What is the '
          'net change?', '750 dollars more', ('5,650 dollars more', 'adds instead of subtracting'),
          ('750 dollars less', 'wrong direction'), ('2,450 dollars more', 'only expenses'),
          '3,200 - 2,450 = 750 dollars.', calc=lambda: 3200 - 2450 == 750),
        Q('Which is commingling?', 'Paying the owner\'s rent from the LLC account', ('Paying supplier invoices from the LLC account', 'business'),
          ('Depositing client payments in the LLC account', 'business'), ('Paying the LLC\'s web hosting from the LLC account', 'business'),
          'Personal rent paid by the LLC mixes funds.'),
        Q('A new freelancer has no LLC. Is a separate account still useful?', 'Yes, it keeps records clearer',
          ('No, only corporations may have one', 'false'), ('No, freelancers cannot open them', 'false'),
          ('No, it raises taxes automatically', 'false'), 'Separation helps any business.'),
    ]),
    F2=sec('Handle the complications: fixing mistakes and edge cases', SEP, [
        Q('Ava accidentally paid a 40-dollar personal dinner with the business card. What is a sensible fix?',
          'Record it and repay the business from personal money', ('Ignore it, since small mistakes on business cards never matter', 'records become wrong'),
          ('Call it a business expense anyway', 'not honest'), ('Close the business account', 'too extreme'),
          'Correcting and documenting keeps records clean.'),
        Q('A customer pays by a payment app linked to the owner\'s personal account. What should the owner change?',
          'Link the payment app to the business account', ('Nothing, apps never matter', 'still commingling'),
          ('Ask customers to stop paying through the app', 'loses income'), ('Delete all records', 'harmful'),
          'Payment tools should deposit into the business account.'),
        Q('An owner pays herself from the business by moving money to her personal account and noting it. Is that '
          'commingling?', 'No, a recorded transfer to the owner is a normal step', ('Yes, owners can never be paid', 'false'),
          ('Yes, every transfer from business to owner is illegal', 'false'), ('Only if done on Mondays', 'irrelevant'),
          'Clear, recorded owner payments are fine.'),
        Q('Which habit best prevents commingling?', 'Use business cards and accounts only for business',
          ('Keep one shared card for both kinds of spending', 'mixes funds'), ('Pay all costs in untracked cash', 'unclear records'),
          ('Use whichever card is closest', 'mixes funds'), 'Consistent separation prevents mixing.'),
        Q('Which statement is accurate?', 'A separate account helps, but it does not by itself guarantee liability protection.',
          ('A separate account by itself makes the owner immune to every lawsuit and every business debt.', 'overstated'),
          ('A separate account removes the need for bookkeeping.', 'false'),
          ('A separate account eliminates taxes.', 'false'), 'It is one important habit among several.'),
    ]))

# ------------------------------------------------------------------ Set 34: opening the account
OPEN = ('Banks set their own rules, but opening a business account usually requires: the business\'s formation papers '
        '(for an LLC or corporation), the EIN (or an SSN for some sole proprietors), a DBA certificate if using a '
        'trade name, and personal ID for each signer. A SIGNER is a person allowed to use the account. Compare '
        'accounts: monthly fees, minimum balance needed to avoid fees, transaction limits, cash deposit fees and online '
        'tools. Read the fee schedule before choosing; a "free" account may have conditions.')

s34 = SET('ENT.BANK.02',
    M=sec('Prepare documents and compare business account fees and signers', OPEN, [
        Q('What is a signer on a bank account?', 'A person allowed to use the account',
          ('A customer who pays the business by check', 'not a signer'),
          ('The state office that approved the LLC', 'not a signer'),
          ('The bank employee who opened the account', 'not a signer'), 'Signers can make transactions.'),
        Q('Which document does a bank commonly ask for when opening an LLC account?', 'The LLC\'s formation papers',
          ('The owner\'s high school report card', 'not relevant'), ('A competitor\'s price list', 'not relevant'),
          ('The company\'s logo file', 'not relevant'), 'Banks need proof the LLC exists.'),
        Q('A sole proprietor uses the trade name "Pine Cleaners." What may the bank ask for?', 'A DBA certificate',
          ('A trademark from another country', 'not needed'), ('An operating agreement only', 'for LLCs'),
          ('A food permit', 'not relevant'), 'Banks may need proof of the trade name.'),
        Q('An account is "free" if the balance stays above 1,500 dollars. What should an owner check?', 'Whether she can keep that minimum balance',
          ('Whether the bank\'s logo is attractive', 'not relevant'), ('Whether the lobby has coffee', 'not relevant'),
          ('Whether her friends bank there', 'not relevant'), 'Conditions decide whether fees apply.'),
        Q('Which is part of comparing business accounts?', 'Monthly fees and transaction limits',
          ('The color of the debit card only', 'cosmetic'), ('The bank\'s TV ads', 'not a cost'),
          ('How tall the bank building is', 'irrelevant'), 'Costs and limits matter most.'),
    ]),
    B=[cs('Packing for the bank visit', 'Opening a business account is like checking in for a flight: you bring the right '
          'papers or you get sent back. Bring proof the business exists (formation papers or a DBA certificate), the '
          'tax ID (EIN), and a photo ID for each person who will use the account. Then, like comparing airline baggage '
          'fees, compare the account\'s fees before you choose.', [
        Q('What happens if you arrive without the right papers?', 'You may be sent back', ('You get a free account', 'no'),
          ('The bank guesses for you', 'no'), ('Nothing at all', 'papers are needed'), 'Banks need documents.'),
        Q('Which shows the business exists?', 'Formation papers or a DBA certificate', ('A photo of the shop', 'not proof'),
          ('A business card', 'not proof'), ('A social media page for the business', 'not proof'), 'Official papers prove it.'),
        Q('Which ID does each account user bring?', 'A personal photo ID', ('A library card only', 'not enough'),
          ('A gym card', 'not ID'), ('A coupon', 'not ID'), 'Each signer is identified.'),
        Q('Comparing account fees is like comparing what?', 'Airline baggage fees', ('Movie plots', 'no'),
          ('Song lyrics', 'no'), ('Paint colors at a hardware store', 'no'), 'Compare costs before choosing.'),
        Q('Which tax ID do you bring?', 'The EIN', ('A zip code', 'no'), ('A phone number', 'no'),
          ('A license plate', 'no'), 'The EIN identifies the business.'),
    ], why='A learner who misses MAIN may not know what to bring or compare; a flight check-in is a familiar checklist.')],
    F1=sec('Apply it: compare two accounts', OPEN, [
        Q('Account A costs 15 dollars a month. Account B costs 5 dollars a month plus 0.50 dollars per deposit after 20 '
          'deposits. A business makes 30 deposits a month. Which costs less?', 'Account B (10 dollars)', ('Account A (15 dollars)', 'A is higher'),
          ('They cost the same', 'B is lower'), ('Account B (20 dollars)', 'miscounted the extra deposits'),
          'B: 5 + (30 - 20) x 0.50 = 10 dollars, less than 15.', calc=lambda: 5 + (30 - 20) * 0.5 == 10 and 10 < 15),
        Q('Tia\'s LLC has two owners who will both write checks. What must the bank set up?', 'Both owners as signers with ID',
          ('Only Tia, while her partner uses Tia\'s card', 'sharing cards is unsafe'),
          ('No signers; the LLC signs itself', 'people sign'), ('A customer as a signer', 'not appropriate'),
          'Each person who uses the account is a signer.'),
        Q('An account waives its 12-dollar monthly fee if the balance stays above 1,000 dollars. Ken\'s balance usually '
          'drops to 400 dollars. What yearly fee should he expect?', '144 dollars', ('0 dollars', 'he misses the minimum'),
          ('12 dollars', 'only one month'), ('400 dollars', 'that is the balance'), '12 x 12 = 144 dollars.',
          calc=lambda: 12 * 12 == 144),
        Q('Which document is the bank LEAST likely to require?', 'The business\'s marketing plan', ('The EIN', 'commonly required'),
          ('Formation papers', 'commonly required'), ('A photo ID for each signer', 'commonly required'),
          'Marketing plans are not usually required.'),
        Q('A cash-heavy food truck compares accounts. Which fee matters most to it?', 'Cash deposit fees',
          ('International wire fees', 'rare for it'), ('Check-printing designs', 'minor'),
          ('Branch decor', 'irrelevant'), 'Frequent cash deposits make that fee important.'),
    ]),
    F2=sec('Handle the complications: signers, changes and fine print', OPEN, [
        Q('A partner leaves the business but is still a signer. What should the remaining owner do?', 'Ask the bank to remove that signer',
          ('Nothing; old signers lose access automatically', 'not automatic'),
          ('Share the password with the former partner', 'unsafe'),
          ('Close every account immediately', 'not required'), 'Update signers when roles change.'),
        Q('A bank ad says "Free business checking." What should the owner do before opening?', 'Read the fee schedule and conditions',
          ('Open it right away; free means no fees ever', 'conditions may apply'),
          ('Assume all banks are the same', 'they differ'), ('Ask a stranger online', 'unreliable'),
          'Fine print shows when fees apply.'),
        Q('An owner gives her bookkeeper her own online banking password. What is a better option?',
          'Ask the bank about separate access for the bookkeeper', ('Post the password where every staff member can see it', 'unsafe'),
          ('Use the same password for everything', 'unsafe'), ('Share her ID card too', 'unsafe'),
          'Separate user access keeps control and records clear.'),
        Q('The bank asks for documents the owner did not expect. What is the reason most likely?', 'Banks set their own rules for opening accounts',
          ('The bank is breaking the law', 'not necessarily'), ('The business is not allowed to exist in that state', 'unlikely'),
          ('The IRS controls bank forms', 'not exactly'), 'Requirements vary by bank.'),
        Q('Which statement is accurate?', 'Account requirements and fees vary by bank, so compare before choosing.',
          ('Every bank charges exactly the same monthly and deposit fees.', 'false'), ('No bank ever charges business fees.', 'false'),
          ('Banks never ask for ID.', 'false'), 'Comparison helps choose wisely.'),
    ]))

# ------------------------------------------------------------------ Set 35: debit, credit and payment processing
PAYTOOLS = ('A business DEBIT card takes money straight from the business account. A business CREDIT card borrows money '
            'that must be repaid; unpaid balances usually charge interest. A PAYMENT PROCESSOR is a company that lets the '
            'business accept card or app payments from customers; it charges a fee, often a percentage plus a small '
            'fixed amount per sale, and deposits the rest into the business account, usually a day or more later. Know '
            'which tool moves money in, and which moves money out.')

s35 = SET('ENT.BANK.03',
    M=sec('Tell debit, credit and payment processing apart', PAYTOOLS, [
        Q('Where does a business debit card take money from?', 'The business bank account',
          ('A loan that must be repaid with interest', 'that is credit'),
          ('The customer\'s bank account directly', 'not how debit works for the owner'),
          ('The owner\'s personal savings account', 'not if it is a business card'),
          'Debit draws from the account.'),
        Q('What happens if a credit card balance is not paid in full?', 'Interest is usually charged',
          ('The balance is forgiven after a month', 'not usually'),
          ('The bank pays the balance for the business', 'no'),
          ('The card becomes a debit card', 'no'), 'Unpaid credit balances usually charge interest.'),
        Q('What does a payment processor do?', 'Lets the business accept customer card payments',
          ('Files the business\'s yearly tax return', 'not its job'),
          ('Registers the business name with the state', 'not its job'),
          ('Designs the online store', 'not its main job'), 'Processors move customer payments to the business.'),
        Q('Which tool brings money IN from customers?', 'A payment processor', ('A business debit card', 'money out'),
          ('A business credit card', 'borrowing to pay out'), ('A checkbook', 'usually money out'),
          'Processors collect customer payments.'),
        Q('When does the processor usually deposit the money?', 'A day or more after the sale',
          ('Before the customer buys anything', 'not possible'), ('Never; it keeps the money', 'false'),
          ('Exactly one year later', 'not typical'), 'Deposits often take one or more business days.'),
    ]),
    B=[cs('In-doors and out-doors', 'Think of money moving through doors. A payment processor is an IN door: customers\' '
          'card payments come through it into the business account, minus a fee. A debit card is an OUT door: money '
          'leaves the account immediately. A credit card is a borrowed OUT door: you spend now and must pay the card '
          'company back later, sometimes with interest.', [
        Q('A payment processor is which door?', 'An IN door', ('An OUT door', 'it brings money in'),
          ('A locked door', 'no'), ('No door', 'no'), 'Customer payments come in.'),
        Q('A debit card is which door?', 'An OUT door', ('An IN door', 'it pays out'), ('A borrowed door', 'that is credit'),
          ('A locked door', 'no'), 'Debit takes money out now.'),
        Q('A credit card is which door?', 'A borrowed OUT door', ('An IN door', 'no'), ('A free door', 'not free'),
          ('A locked door with no key', 'no'), 'Credit lets you spend borrowed money.'),
        Q('What does the processor keep?', 'A fee', ('Nothing', 'it charges a fee'), ('The whole sale', 'no'),
          ('The customer\'s card', 'no'), 'Processors charge a fee.'),
        Q('What may you owe on a credit card later?', 'The balance and maybe interest', ('Nothing', 'no'),
          ('Only a thank-you note to the card company', 'no'), ('A free gift', 'no'), 'Borrowed money must be repaid.'),
    ], why='A learner who misses MAIN may mix up the tools; the door picture shows the direction money moves.')],
    F1=sec('Apply it: estimate deposits and choose tools', PAYTOOLS, [
        Q('A processor charges 2.9 percent plus 0.30 dollars per sale. A sale is 50 dollars. What is the fee?', '1.75 dollars',
          ('1.45 dollars', 'forgot the 0.30 dollars'), ('0.30 dollars', 'only the fixed part'), ('3.20 dollars', 'added 2.9 as dollars'),
          '0.029 x 50 + 0.30 = 1.45 + 0.30 = 1.75 dollars (example rate).', calc=lambda: round(0.029 * 50 + 0.30, 2) == 1.75),
        Q('A processor charges 2.9 percent plus 0.30 dollars per sale. How much is deposited for a 50-dollar sale?',
          '48.25 dollars',
          ('50.00 dollars', 'ignores the fee'), ('48.55 dollars', 'forgot the 0.30 dollars'),
          ('46.80 dollars', 'added 2.9 as dollars'),
          '50 - 1.75 = 48.25 dollars.',
          calc=lambda: round(50 - 1.75, 2) == 48.25),
        Q('Lou buys 300 dollars of supplies with a business credit card and pays the whole bill on time. What interest '
          'does he pay, assuming the card charges none when paid in full?', '0 dollars', ('300 dollars', 'that is the purchase'),
          ('30 dollars', 'guessed a rate'), ('3 dollars', 'guessed a rate'), 'Paying in full on time avoids interest on many cards.'),
        Q('A business wants to stop overspending money it does not have. Which card fits that goal?', 'A business debit card',
          ('A credit card with a high limit', 'allows borrowing'), ('Several new credit cards', 'more borrowing'),
          ('A store credit account', 'borrowing'), 'Debit spends only what is in the account.'),
        Q('A customer pays by card on Friday. The owner needs the cash Friday afternoon. What should she know?',
          'Processor deposits often arrive a day or more later', ('Card deposits always arrive before the customer even pays', 'false'),
          ('Card sales never deposit', 'false'), ('Cash arrives in her wallet instantly', 'false'),
          'Plan for deposit timing.'),
    ]),
    F2=sec('Handle the complications: fees, timing and debt', PAYTOOLS, [
        Q('An owner charges 2,000 dollars on a credit card and pays only the minimum each month. What is the main risk?',
          'Interest builds and the debt lasts a long time', ('No risk; minimum payments clear the debt quickly', 'slow and costly'),
          ('The bank cancels the debt', 'no'), ('The purchase becomes free', 'no'), 'Carrying a balance costs interest.'),
        Q('Two processors: one charges 2.6 percent plus 0.15 dollars per sale, one charges 3 percent with no fixed fee. For a '
          '10-dollar sale, which costs less?', '3 percent (0.30 dollars)', ('2.6 percent plus 0.15 dollars (0.41 dollars)', 'that is higher'),
          ('They cost the same', 'they differ'), ('3 percent (3.00 dollars)', 'used 3 as dollars'),
          '0.026 x 10 + 0.15 = 0.41; 0.03 x 10 = 0.30 (example rates).',
          calc=lambda: round(0.026 * 10 + 0.15, 2) == 0.41 and round(0.03 * 10, 2) == 0.30),
        Q('A processor holds a new seller\'s deposits for a few days after a large sale. What is a sensible response?',
          'Read the processor\'s terms and plan cash for delays', ('Assume the money is lost forever', 'not necessarily'),
          ('Sign up for many processors at once to spread out sales', 'not a fix'), ('Stop recording sales', 'harmful'),
          'Processors may hold funds under their terms.'),
        Q('An owner pays personal bills with the business credit card to earn rewards. What is the problem?', 'It mixes personal and business spending',
          ('Nothing; rewards make it fine', 'still commingling'), ('Rewards are illegal', 'not the point'),
          ('Business cards cannot earn rewards', 'some do'), 'Keep business cards for business costs.'),
        Q('Which statement is accurate?', 'Fees and rules differ by provider, so compare current terms.',
          ('All processors charge the same.', 'false'), ('Credit cards never charge interest on any unpaid balance.', 'false'),
          ('Debit cards borrow money.', 'false'), 'Provider terms vary.'),
    ]))

# ------------------------------------------------------------------ Set 36: owner and business money
DRAW = (('Owners move money in and out of a business in a few ways. An OWNER CONTRIBUTION is money the owner puts in. '
        "An OWNER'S DRAW (also called a distribution) is an owner withdrawal for personal use; for sole proprietors "
        "and most LLCs, a draw is not a wage and is not a business expense, so it lowers the business's cash but does"
        ' not reduce its profit. A LOAN from the owner to the business should be written down with how it will be '
        'repaid. In every case, move the money by transfer and record what it is, so the books show the truth.'))

s36 = SET('ENT.BANK.04',
    M=sec('Record contributions, draws and owner loans correctly', DRAW, [
        Q('Money an owner puts into the business is called what?',
          'An owner contribution',
          ("An owner's draw for personal use", 'that is money out'), ('A customer payment for a product', 'that is revenue'),
          ('A refund to a customer', 'that is money out'),
          'A contribution is money in from the owner.'),
        Q('Money an owner withdraws from the business for personal use is called what?',
          "An owner's draw",
          ('A business expense for supplies', 'not a draw'), ('A loan from a bank', 'not a draw'),
          ('A sales tax payment', 'not a draw'),
          'A draw is an owner withdrawal for personal use.'),
        Q('For a sole proprietor, is a draw a business expense?', 'No', ('Yes, always', 'it is not an expense'),
          ('Only in December', 'no'), ('Only if over 1,000 dollars', 'no'), 'Draws are not business expenses.'),
        Q('An owner lends the business 2,000 dollars. What should be done?', 'Write it down with how it will be repaid',
          ('Keep it secret from any partners', 'unclear'), ('Call it sales income', 'not revenue'),
          ('Spend it without recording anything', 'unclear books'), 'Documented loans keep books accurate.'),
        Q('What is the best way to move money between owner and business?', 'A recorded bank transfer',
          ('Untracked cash from a drawer', 'hard to prove'), ('Paying personal bills from the business card', 'commingling'),
          ('Guessing amounts at year end', 'inaccurate'), 'Transfers leave a clear record.'),
    ]),
    B=[cs('A family piggy bank with a notebook', 'Picture a family piggy bank with a notebook next to it. When you put money '
          'in, you write "Added 50." When you take money out, you write "Took 20." If you borrow from it, you write '
          '"Borrowed 30, will repay Friday." The notebook tells the true story. Owner contributions, draws and loans '
          'are the same idea: money moves in and out, and each move is written down.', [
        Q('Putting money in the piggy bank is like what?', 'An owner contribution', ('An owner\'s draw', 'money out'),
          ('A refund paid to a customer', 'no'), ('A tax bill', 'no'), 'Money in from the owner.'),
        Q('Taking money out is like what?', 'An owner\'s draw', ('A contribution', 'money in'), ('A sale', 'no'),
          ('A business license', 'no'), 'Money out to the owner.'),
        Q('Why keep the notebook?', 'It tells the true story of the money', ('For decoration', 'no'),
          ('To hide the money', 'no'), ('To make the piggy bank heavier', 'no'), 'Records show what happened.'),
        Q('"Borrowed 30, will repay Friday" is like what?', 'A loan with repayment terms', ('A gift to a friend or cousin', 'no'),
          ('A sale', 'no'), ('A tax', 'no'), 'A loan is repaid.'),
        Q('What happens if moves are not written down?', 'No one knows the true balance', ('The money multiplies by itself', 'no'),
          ('Taxes vanish', 'no'), ('Nothing at all', 'records get lost'), 'Unrecorded moves create confusion.'),
    ], why='A learner who misses MAIN may confuse the kinds of owner money; a piggy bank with a notebook shows each move.')],
    F1=sec('Apply it: label owner money moves', DRAW, [
        Q('Ivy moves 1,000 dollars from her savings into her new LLC account to buy supplies. How should it be recorded?',
          'As an owner contribution', ('As sales revenue from customers', 'not revenue'),
          ('As an owner\'s draw', 'that is money out'), ('As a supply expense', 'the purchase is later'),
          'Money put in by the owner is a contribution.'),
        Q("A sole proprietor's business has 5,000 dollars of cash available. The owner withdraws 1,500 dollars as a draw for personal use. With no other transactions, how much cash remains in the business?",
          '3,500 dollars',
          ('5,000 dollars', 'ignores the draw'), ('6,500 dollars', 'added the draw'),
          ('1,500 dollars', 'that is the draw'),
          '5,000 - 1,500 = 3,500 dollars of cash. The draw lowers cash, but it is not an expense, so it does not reduce profit.',
          calc=lambda: 5000 - 1500 == 3500),
        Q('Omar lends his business 3,000 dollars to be repaid 250 dollars a month. How many months to repay it?', '12 months',
          ('10 months', 'miscounted'), ('25 months', 'used the wrong numbers'), ('3 months', 'used thousands'),
          '3,000 / 250 = 12 months.', calc=lambda: 3000 / 250 == 12),
        Q('An owner takes 200 dollars cash from the register for personal use without recording it. What is the problem?',
          'The books will not match the real money', ('No problem; owners can take any cash', 'records break'),
          ('It becomes a business expense', 'not an expense'), ('It counts as sales', 'not sales'),
          'Every owner withdrawal should be recorded.'),
        Q('Which is NOT a business expense for a sole proprietor?', 'The owner\'s draw', ('Shipping supplies', 'expense'),
          ('Web hosting', 'expense'), ('Business software', 'expense'), 'Draws are not expenses.'),
    ]),
    F2=sec('Handle the complications: draws, cash shortages and partners', DRAW, [
        Q('An owner takes large draws while the business owes suppliers. What is the risk?', 'The business may not have cash to pay its bills',
          ('No risk; draws create more cash', 'false'), ('Draws reduce taxes to zero', 'false'),
          ('Suppliers stop asking the business for payment', 'false'), 'Draws reduce business cash.'),
        Q('Two equal LLC partners agreed to take draws equally. One takes 2,000 dollars and the other 500 dollars. What '
          'should they do?', 'Record it and fix the imbalance as their agreement says', ('Ignore it forever', 'creates disputes'),
          ('Delete the records', 'harmful'), ('Have their customers vote on which partner was right', 'not their role'),
          'Draws should follow the agreement.'),
        Q('A corporation\'s owner who works in the business may be paid through payroll. Why does this differ from a sole '
          'proprietor\'s draw?', 'Business structure affects how owners are paid', ('All owners are paid identically', 'not true'),
          ('Corporations cannot pay owners', 'false'), ('Sole proprietors must always pay themselves through payroll', 'not usually'),
          'Rules depend on structure; a tax professional can help.'),
        Q('An owner put 2,000 dollars into the business but did not record whether it was a loan or a contribution. Why does the label matter?',
          'A loan is a debt to repay; a contribution adds to owner equity',
          ('The label has no effect on the books or on repayment', 'the label decides how the books show it and whether repayment is owed'), ('Both labels mean the money counts as customer sales', 'neither is sales'),
          ('Both labels mean the money is tax the business owes', 'neither is a tax'),
          'A loan is recorded as a debt repaid on agreed terms. A contribution increases owner equity and has no repayment schedule, though owners may later take money out, for example as draws.'),
        Q('Which statement is accurate?', 'Owner pay rules vary by structure, so check with a tax professional.',
          ('Every business owner must take a weekly salary through payroll.', 'not true'), ('Draws are always business expenses.', 'not true'),
          ('Owners may never take money out.', 'not true'), 'Structure and tax treatment matter.'),
    ]))

# ------------------------------------------------------------------ Set 37: reconciling
REC = ('RECONCILING means comparing your own records with the bank statement to make sure they match. Each month, check '
       'every deposit and withdrawal. Differences usually come from: transactions the bank has not processed yet (such '
       'as a check that has not cleared), bank fees you did not record, mistakes in your records, or charges you do not '
       'recognize. Unknown charges may be errors or fraud and should be reported to the bank quickly. Reconciling '
       'catches problems while they are still small.')

s37 = SET('ENT.BANK.05',
    M=sec('Reconcile records with the bank statement and explain differences', REC, [
        Q('What does reconciling mean?', 'Comparing your records with the bank statement',
          ('Opening a second account at another bank', 'not reconciling'),
          ('Asking the bank for a loan', 'not reconciling'),
          ('Paying all bills on the same day', 'not reconciling'), 'It checks that records match.'),
        Q('Which is a common reason records and the bank differ?', 'A bank fee that was not recorded',
          ('The owner changed the logo colors', 'unrelated'), ('A customer posted a review', 'unrelated'),
          ('The website was redesigned', 'unrelated'), 'Unrecorded fees cause differences.'),
        Q('A check was written but has not cleared. What does that mean?', 'The bank has not processed it yet',
          ('The check was never written at all', 'it was written'), ('The money was refunded twice', 'no'),
          ('The bank closed the account', 'no'), 'Uncleared checks cause timing differences.'),
        Q('An unknown 89-dollar charge appears. What should the owner do?', 'Report it to the bank quickly',
          ('Ignore it, since small charges never matter', 'may be fraud'), ('Record it as sales', 'wrong'),
          ('Delete it from the records', 'hides the problem'), 'Unknown charges should be checked quickly.'),
        Q('How often is reconciling commonly done?', 'Monthly', ('Once every ten years', 'too rare'),
          ('Only when closing the business', 'too late'), ('Never', 'problems would be missed'),
          'Monthly reconciling catches problems early.'),
    ]),
    B=[cs('Checking a receipt against the bag', 'After shopping, you might compare the receipt with what is in the bag. '
          'If the receipt shows two milks but you have one, something is wrong. Reconciling is the same check for a '
          'business: your records are one list, the bank statement is the other, and you look for any item that '
          'appears on only one of them. Then you find out why.', [
        Q('In the shopping example, what is compared?', 'The receipt and the bag', ('Two stores', 'no'),
          ('Prices and the weather', 'no'), ('Coupons and ads', 'no'), 'Two lists are compared.'),
        Q('For a business, which two lists are compared?', 'Records and bank statement', ('Logo and website', 'no'),
          ('Ads and reviews', 'no'), ('Products and their colors', 'no'), 'Records versus the bank.'),
        Q('Two milks on the receipt but one in the bag means what?', 'Something does not match', ('Everything is fine as it is', 'no'),
          ('Milk is free', 'no'), ('The store closed', 'no'), 'A mismatch needs checking.'),
        Q('After finding a mismatch, what do you do?', 'Find out why', ('Ignore it', 'no'), ('Throw away the receipt', 'no'),
          ('Buy more milk', 'no'), 'Investigate differences.'),
        Q('An item only on the bank statement could be what?', 'A fee you did not record', ('A logo', 'no'),
          ('A review a customer posted', 'no'), ('A paper coupon', 'no'), 'Fees are common unrecorded items.'),
    ], why='A learner who misses MAIN may not picture reconciling; checking a receipt against the bag is familiar.')],
    F1=sec('Apply it: find the difference', REC, [
        Q('Records show 2,450 dollars. The bank shows 2,435 dollars. The statement lists a 15-dollar monthly fee not in the '
          'records. What explains the difference?', 'The unrecorded 15-dollar fee', ('A 150-dollar deposit error', 'wrong size'),
          ('A missing 2,435-dollar sale', 'wrong size'), ('Nothing; they match', 'they differ by 15'),
          '2,450 - 2,435 = 15 dollars.', calc=lambda: 2450 - 2435 == 15),
        Q('Records show 1,800 dollars. A 200-dollar check to a supplier has not cleared. What will the bank likely show?',
          '2,000 dollars', ('1,600 dollars', 'subtracted twice'), ('1,800 dollars', 'ignores the uncleared check'),
          ('200 dollars', 'only the check'), 'The bank has not subtracted the 200 yet: 1,800 + 200 = 2,000.',
          calc=lambda: 1800 + 200 == 2000),
        Q('A deposit of 350 dollars was recorded as 530 dollars. What is the difference?', '180 dollars', ('350 dollars', 'not the difference'),
          ('530 dollars', 'not the difference'), ('880 dollars', 'added instead'), '530 - 350 = 180 dollars.',
          calc=lambda: 530 - 350 == 180),
        Q('The statement shows two identical 45-dollar charges from one supplier on the same day. The owner made one '
          'purchase. What should she do?', 'Contact the supplier or bank about a possible duplicate', ('Record both as normal', 'one may be wrong'),
          ('Delete both charges from her records and move on', 'one was real'), ('Close the business', 'too extreme'), 'Check duplicates promptly.'),
        Q('Which habit makes reconciling easier?', 'Recording transactions as they happen', ('Recording only at year end', 'harder'),
          ('Keeping no receipts', 'harder'), ('Mixing in personal purchases now and then', 'harder'), 'Timely records simplify matching.'),
    ]),
    F2=sec('Handle the complications: fraud, timing and delays', REC, [
        Q('An owner has not reconciled for 8 months and finds an unknown charge from 7 months ago. What is the problem?',
          'Waiting long can make disputes and recovery harder', ('No problem; any timing is fine', 'delays can matter'),
          ('Old charges always disappear', 'no'), ('The bank fixes any old charge automatically', 'not without notice'),
          'Banks may set time limits for reporting problems.'),
        Q('A small recurring 9.99-dollar charge appears for software the owner cancelled. What should she do?',
          'Cancel properly and dispute charges after cancellation', ('Ignore it; it is small', 'adds up'),
          ('Record it as revenue', 'wrong'), ('Hide it from her accountant to keep the books simple', 'harmful'), 'Small recurring charges add up.'),
        Q('The 9.99-dollar charge has continued for 12 months. How much has it cost?', '119.88 dollars', ('9.99 dollars', 'one month'),
          ('99.90 dollars', '10 months'), ('129.87 dollars', '13 months'), '9.99 x 12 = 119.88 dollars.',
          calc=lambda: round(9.99 * 12, 2) == 119.88),
        Q('Records and bank match exactly, but the owner forgot to record a customer refund paid in cash. What is true?',
          'Matching the bank does not catch cash moves outside the account', ('All money is always perfect', 'not necessarily'),
          ('Cash never needs recording', 'it does'), ('The bank automatically records the cash kept in her drawer', 'no'),
          'Cash outside the bank needs its own records.'),
        Q('Which statement is accurate?', 'Reconciling regularly catches errors and fraud sooner.',
          ('Reconciling is only needed by large companies with many staff.', 'all benefit'), ('Banks never make mistakes.', 'they can'),
          ('Reconciling replaces keeping receipts.', 'receipts still matter'), 'Regular checks help.'),
    ]))

SETS = [s30, s31, s32, s33, s34, s35, s36, s37]
