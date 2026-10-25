"""Entrepreneurship sets 24-29: Foundation 4, names and legal structure (part 2)."""
from eq import Q, sec, cs, SET

# ------------------------------------------------------------------ Set 24: forming an LLC; registered agent
FORM = ('Forming an LLC, at a basic level: (1) choose a name that the state will accept; (2) name a registered agent, '
        'a person or company with a physical address in the state who accepts official legal papers for the business '
        'during business hours; (3) file formation papers (often called articles of organization) with the state and '
        'pay the fee; (4) write an operating agreement; (5) then handle tax IDs, licenses and a bank account. Many '
        'states do not accept a PO Box for the registered agent. Steps and fees vary by state; check the state\'s '
        'official business filing site.')

s24 = SET('ENT.LEGAL.06',
    M=sec('Order the steps of forming an LLC and explain the registered agent', FORM, [
        Q('What does a registered agent do?', 'Accepts official legal papers for the business',
          ('Designs the logo and picks brand colors for the LLC', 'that is branding work'),
          ('Files the owner\'s personal tax return every spring', 'that is a tax preparer\'s job'),
          ('Opens and manages the business\'s bank account', 'banking is separate'),
          'The registered agent receives official notices and legal papers.'),
        Q('Which step creates the LLC itself?', 'Filing formation papers with the state',
          ('Opening a business bank account at a local bank', 'banks need the LLC first'),
          ('Buying a matching domain name for the website', 'domains do not create entities'),
          ('Printing business cards that say "LLC" on them', 'printing has no legal effect'),
          'The state filing creates the LLC.'),
        Q('Which order makes the most sense?', 'Choose a name and agent, file with the state, then open a bank account',
          ('Open a bank account, then decide whether to form the LLC later', 'the bank usually needs the LLC\'s papers'),
          ('Print signs first, then pick a registered agent years later', 'agent is required at filing'),
          ('Apply for licenses before deciding what business it is', 'licenses depend on the business'),
          'Formation comes before steps that require the LLC\'s documents.'),
        Q('Many states do not accept which address for a registered agent?', 'A PO Box',
          ('A physical office address inside the state', 'that is what is usually required'),
          ('A street address where someone is present', 'that is usually required'),
          ('The agent\'s own office address in the state', 'acceptable'),
          'The agent needs a physical in-state address where papers can be delivered.'),
        Q('Where should a founder confirm the exact steps and fees?', 'The state\'s official business filing website',
          ('A random social media post about LLCs', 'may be wrong or outdated'),
          ('A competitor\'s opinion about filing fees', 'not authoritative'),
          ('An old textbook from another country', 'not the right jurisdiction'),
          'Official state sources give current steps and fees.'),
    ]),
    B=[cs('The registered agent as a mail desk', 'Picture the front desk of an office building. When an important letter '
          'arrives, someone at the desk signs for it and makes sure it gets to the right person. A registered agent is '
          'the business\'s official front desk for legal papers. That is why the agent needs a real street address in the '
          'state and must be available during business hours: someone has to be there to receive the papers.', [
        Q('A registered agent is most like what?', 'An office front desk for legal papers', ('A logo designer', 'unrelated'),
          ('A delivery truck that carries packages', 'it delivers, not receives'), ('A bank teller', 'unrelated'), 'It receives official papers.'),
        Q('Why does the agent need a street address?', 'Someone must be able to deliver papers there',
          ('So the logo looks local', 'unrelated'), ('So customers can walk in and shop there in person', 'not the purpose'),
          ('So taxes are lower', 'unrelated'), 'Papers are delivered to a physical place.'),
        Q('When must the agent usually be available?', 'During business hours', ('Only late at midnight', 'no'),
          ('Never', 'they must receive papers'), ('Only on holidays', 'no'), 'Someone must be there to receive papers.'),
        Q('What does the agent receive?', 'Official legal papers and notices', ('Customer orders', 'not its job'),
          ('Product shipments from suppliers', 'not its job'), ('Job applications', 'not its job'), 'Its role is legal papers.'),
        Q('Which is a good choice for a registered agent?', 'Someone with a reliable in-state street address',
          ('A PO Box in another state', 'not usually allowed'), ('A friend who moves often and has no address', 'unreliable'),
          ('An email address only', 'not usually enough'), 'Reliability and a physical in-state address matter.'),
    ], why='A learner who misses MAIN may not know what the agent is for; the front-desk picture explains the role.')],
    F1=sec('Apply it: plan an LLC formation', FORM, [
        Q('Lia wants an LLC but works away from home all day and moves often. What registered agent choice fits best?',
          'A registered agent service with a stable in-state office', ('Her own home address, even though she is rarely there', 'she is often away'),
          ('A PO Box near her apartment', 'often not accepted'), ('Her email address', 'not usually enough'),
          'A service with a stable address can reliably receive papers.'),
        Q('Ana filed her LLC papers. The state approved them. What is a sensible next step?',
          'Write an operating agreement and handle tax IDs and banking', ('Pick a registered agent for the very first time now', 'needed at filing'),
          ('File the formation papers again', 'already filed'), ('Choose a name the state will accept', 'already done'),
          'After formation, internal agreements, tax IDs and banking follow.'),
        Q('A state charges a 125-dollar filing fee and a registered agent service costs 100 dollars a year. What is the '
          'first-year cost of these two items?', '225 dollars', ('125 dollars', 'only the filing fee'),
          ('100 dollars', 'only the agent fee'), ('25 dollars', 'the difference'),
          '125 + 100 = 225 dollars in the first year (fees here are example assumptions).', calc=lambda: 125 + 100 == 225),
        Q('Raj picked a name, but the state rejects it as too similar to an existing LLC. What should he do?',
          'Choose a different name and check availability first', ('File anyway and hope it passes', 'it will be rejected'),
          ('Use the rejected name anyway, but only on his website', 'still confusing and risky'),
          ('Skip forming the LLC entirely', 'not necessary'), 'Pick an available name before filing.'),
        Q('Which item is NOT part of forming the LLC with the state?', 'Designing the company logo',
          ('Naming a registered agent', 'part of filing'), ('Filing formation papers', 'part of filing'),
          ('Paying the state filing fee', 'part of filing'), 'Logos are branding, not formation.'),
    ]),
    F2=sec('Handle the complications: addresses, deadlines and checks', FORM, [
        Q('Mo wants privacy and plans to list his PO Box as the registered agent address. What should he check first?',
          'Whether his state allows a PO Box for the registered agent', ('Whether his logo fits neatly in the space on the state form', 'unrelated'),
          ('Whether the PO Box is cheap', 'cost does not decide whether it is allowed'),
          ('Whether friends use PO Boxes', 'not authoritative'),
          'Many states require a physical in-state address; a PO Box may be rejected.'),
        Q('An LLC\'s registered agent quits and the owner forgets to replace them. What is the main risk?',
          'Official legal papers might not reach the business', ('No risk; agents are optional', 'they are usually required'),
          ('The LLC automatically turns into a corporation', 'no'), ('Taxes drop to zero', 'no'),
          'Without an agent, important papers and deadlines may be missed.'),
        Q('A website offers "LLC formation in 5 minutes" for 300 dollars plus the state fee. What should a founder '
          'understand?', 'The state filing can often be done directly; services add their own fee', ('Only paid services can file', 'many states allow direct filing'),
          ('The whole 300-dollar service fee is paid to the state as a tax', 'it is the service\'s fee'),
          ('Services guarantee lower taxes', 'no'), 'Compare the direct state filing option with the paid convenience.'),
        Q('A founder plans to operate in a second state. What should she check?', 'Whether that state requires registering the LLC there too',
          ('Nothing; one state filing automatically covers every other state', 'not always'),
          ('Whether her logo is popular in that state', 'unrelated'),
          ('Whether to dissolve the first LLC', 'not required'), 'Doing business in another state can require registration there.'),
        Q('Which statement is accurate?', 'Formation steps and fees vary by state.',
          ('Every state has identical forms and fees.', 'they differ'),
          ('Only federal law controls LLC formation.', 'state law controls'),
          ('LLCs never need a registered agent.', 'they usually do'), 'Always check the specific state.'),
    ]))

# ------------------------------------------------------------------ Set 25: operating agreement
OA = ('An operating agreement is a written document among an LLC\'s owners (members) that sets the rules for running '
      'the business. It usually covers: who owns what percentage; who makes which decisions; how profits and losses are '
      'shared; what happens if an owner wants to leave, becomes unable to work, or dies; how new owners can join; and '
      'how disagreements are settled. Even a one-owner LLC can benefit from one. Some states require it. Writing it '
      'while everyone gets along prevents painful arguments later.')

s25 = SET('ENT.LEGAL.07',
    M=sec('Identify what an operating agreement should cover', OA, [
        Q('Which topic belongs in an operating agreement?', 'What happens if an owner wants to leave',
          ('The color scheme for the company website', 'branding detail'),
          ('The menu for the office holiday party', 'not a governance topic'),
          ('Which social media app to post on first', 'marketing detail'),
          'Exit rules are a core part of an operating agreement.'),
        Q('Who are the parties to an LLC\'s operating agreement?', 'The LLC\'s owners (members)',
          ('The LLC\'s customers who buy its products', 'customers are not parties'),
          ('The state that approved the LLC filing', 'the state is not a party'),
          ('The bank that holds the business account', 'not a party'), 'Members agree among themselves.'),
        Q('When is the best time to write an operating agreement?', 'At the start, while owners agree',
          ('Only after a serious argument begins', 'too late for calm decisions'),
          ('Only if the business becomes very large', 'small businesses benefit too'),
          ('Never, because it is always unnecessary', 'it is often valuable'),
          'Calm early agreement prevents later disputes.'),
        Q('Two owners each own 50 percent. Which topic is especially important to settle?', 'How tie votes are broken',
          ('Which owner has the nicer handwriting', 'irrelevant'),
          ('Whose car is newer for deliveries', 'not governance'),
          ('Which font the invoices use', 'not governance'), 'Equal ownership can lead to deadlocks.'),
        Q('Does a one-owner LLC ever benefit from an operating agreement?', 'Yes, it can',
          ('No, never, under any circumstances at all', 'it can help'),
          ('Only if it has more than 100 employees', 'size is not the test'),
          ('Only if the owner changes the logo', 'unrelated'),
          'It documents how the LLC is run and can support the separation from the owner.'),
    ]),
    B=[cs('House rules for owners', 'Think of roommates writing house rules: who pays which bills, who cleans, what '
          'happens if someone moves out, and how to settle arguments. Writing them on move-in day is easy; writing them '
          'during a fight is hard. An operating agreement is the house rules for the owners of an LLC: ownership, '
          'decisions, money, leaving, and disagreements.', [
        Q('An operating agreement is most like what?', 'Roommates\' house rules', ('A grocery list', 'unrelated'),
          ('A movie ticket', 'unrelated'), ('A daily weather report', 'unrelated'), 'It sets rules for those who share something.'),
        Q('When are house rules easiest to write?', 'On move-in day', ('During an argument', 'hardest'),
          ('After someone moves out', 'too late'), ('Never', 'they help'), 'Early agreement is easier.'),
        Q('"What happens if someone moves out" matches which agreement topic?', 'An owner leaving the business',
          ('Website design', 'unrelated'), ('A list of product prices for the shop', 'unrelated'), ('Logo colors', 'unrelated'),
          'Exit rules cover an owner leaving.'),
        Q('"Who pays which bills" matches what?', 'How money and responsibilities are shared', ('Who designs the logo and the website', 'branding'),
          ('Who is the customer', 'unrelated'), ('Where to advertise', 'marketing'), 'Money and duties are covered.'),
        Q('"How to settle arguments" matches what?', 'Resolving disagreements between owners', ('Raising prices', 'unrelated'),
          ('Choosing a domain', 'unrelated'), ('Hiring a designer for the brand and website', 'unrelated'), 'Dispute rules are part of it.'),
    ], why='A learner who misses MAIN may not see why owners need written rules; roommates\' house rules are familiar.')],
    F1=sec('Apply it: spot gaps in an agreement', OA, [
        Q('A two-owner LLC agreement covers ownership and profit split only. What important gap remains?',
          'What happens if an owner leaves or cannot work', ('Which printer brand to buy for the office', 'minor'),
          ('The office plant schedule', 'minor'), ('Holiday decorations', 'minor'),
          'Exit and incapacity rules are a major gap.'),
        Q('Owners own 60 and 40 percent. Profits are 10,000 dollars, split by ownership. How much goes to the 40-percent '
          'owner?', '4,000 dollars', ('6,000 dollars', 'that is the 60-percent share'),
          ('5,000 dollars', 'that is an equal split'), ('400 dollars', 'decimal error'),
          '40 percent of 10,000 = 4,000 dollars.', calc=lambda: 10000 * 40 // 100 == 4000),
        Q('One owner does most of the daily work but owns 30 percent. What should the agreement make clear?',
          'How work is paid separately from ownership', ('That ownership must always equal hours worked', 'not required'),
          ('That the hard worker gets nothing extra ever', 'may not be fair'),
          ('That work and pay never need to be discussed', 'causes disputes'),
          'Ownership share and pay for work can be set separately.'),
        Q('An agreement says big purchases need both owners\' approval. Which purchase most clearly needs it?',
          'A 20,000-dollar delivery van', ('A 5-dollar pack of pens', 'small'), ('A 3-dollar coffee', 'small'),
          ('A 10-dollar shipping label', 'small'), 'A large purchase falls under the approval rule.'),
        Q('A new person wants to buy into the LLC. Where should the rules for adding owners be?', 'In the operating agreement',
          ('On the company website', 'not binding'), ('In a social media post', 'not binding'),
          ('In a customer invoice', 'unrelated'), 'Admitting new members is a governance rule.'),
    ]),
    F2=sec('Handle the complications: disagreements and changes', OA, [
        Q('Two equal owners disagree on hiring and their agreement has no tie-break rule. What is a sensible step?',
          'Use a mediator or add a tie-break process both accept', ('Let the louder owner decide every disagreement from now on', 'unfair'),
          ('Stop all business forever', 'too extreme'), ('Ask customers to vote', 'not their role'),
          'A neutral process helps resolve deadlocks.'),
        Q('An owner wants to sell her share to an outsider. The agreement gives other owners first chance to buy. What '
          'should she do first?', 'Offer her share to the other owners as the agreement requires',
          ('Sell to the outsider quietly without telling the other owners', 'breaks the agreement'),
          ('Ignore the agreement because it is old', 'it still applies'),
          ('Dissolve the LLC immediately', 'not required'), 'Follow the agreed process.'),
        Q('A template agreement from the internet does not fit the owners\' real arrangement. What is the risk?',
          'It may not match what they actually agreed or state law', ('None; any template works', 'not always'),
          ('Templates are illegal', 'not illegal'), ('It automatically guarantees the owners lower taxes', 'no'),
          'Agreements should fit the actual business and state rules.'),
        Q('Which detail should be checked before signing an operating agreement?', 'Whether it covers decisions, money, exits and disputes',
          ('Whether the font is attractive', 'minor'), ('Whether it is longer than ten pages, since longer is better', 'length is not the test'),
          ('Whether a competitor approves', 'not relevant'), 'Coverage of key topics matters most.'),
        Q('Who can help write or review an operating agreement for a complex situation?', 'A business attorney',
          ('A web developer', 'not legal'), ('A sign maker', 'not legal'), ('A social media influencer', 'not legal'),
          'Legal documents benefit from legal review.'),
    ]))

# ------------------------------------------------------------------ Set 26: DBA
DBA = ('A DBA ("doing business as"), also called a trade name, assumed name or fictitious name, lets a business operate '
       'under a name different from its legal name. A sole proprietor named Maria Lopez who sells as "Sunny Bakes" may '
       'need to register that name; so may an LLC operating under a different name. Where it is filed (state, county or '
       'city) depends on the location. A DBA does NOT create a new entity, does NOT give liability protection, and does '
       'NOT give trademark rights. Check local rules.')

s26 = SET('ENT.LEGAL.08',
    M=sec('Explain what a DBA does and does not do', DBA, [
        Q('Maria Lopez sells cakes as "Sunny Bakes." What does a DBA filing let her do?', 'Operate under the name "Sunny Bakes"',
          ('Turn her business into an LLC without other filings', 'a DBA does not create an entity'),
          ('Protect her house from business debts', 'no liability protection'),
          ('Stop all others from using "Sunny Bakes" nationwide', 'no trademark rights'),
          'A DBA registers a name the business uses.'),
        Q('Does a DBA create a new legal entity?', 'No', ('Yes, it creates an LLC', 'it does not'),
          ('Yes, it creates a corporation', 'it does not'), ('Only for partnerships', 'it never does'),
          'A DBA is a name registration, not an entity.'),
        Q('Which is another common term for a DBA?', 'Trade name', ('Articles of organization', 'LLC formation papers'),
          ('Operating agreement', 'owners\' agreement'), ('Registered agent', 'a role'),
          'Trade name, assumed name and fictitious name are similar terms.'),
        Q('Where is a DBA filed?', 'It depends on the location: state, county or city', ('Always with the IRS only, in every location', 'not typical'),
          ('Always with a bank', 'banks may ask for it but do not file it'),
          ('Never anywhere', 'many places require it'), 'Filing location varies.'),
        Q('Which is TRUE about a DBA?', 'It does not give liability protection.', ('It shields personal savings.', 'it does not'),
          ('It gives trademark rights everywhere.', 'it does not'), ('It replaces a business license.', 'separate requirement'),
          'A DBA is only a name registration.'),
    ]),
    B=[cs('A name tag, not a new person', 'A DBA is like a name tag. If Robert wears a tag saying "Coach Bob," he is still '
          'Robert. The tag tells people what to call him at work; it does not make him a different person or give him '
          'special protection. A business with a DBA is still the same business, with the same owner, the same '
          'responsibilities and the same legal form. It simply uses another name with customers.', [
        Q('A DBA is most like what?', 'A name tag', ('A new person', 'it is the same business'),
          ('A shield', 'no protection'), ('A trademark certificate', 'not trademark rights'), 'It is just a name used publicly.'),
        Q('Robert wearing a "Coach Bob" tag is still who?', 'Robert', ('A new person named Bob', 'same person'),
          ('A company', 'no'), ('No one', 'he is Robert'), 'The name changes; the person does not.'),
        Q('Does a business with a DBA change its legal form?', 'No', ('Yes, always', 'it does not'),
          ('Only for LLCs', 'never'), ('Only on weekends', 'no'), 'The legal form stays the same.'),
        Q('Does a DBA give special protection?', 'No', ('Yes, from debts', 'no'), ('Yes, from lawsuits', 'no'),
          ('Yes, from taxes', 'no'), 'It is only a name.'),
        Q('What does a DBA tell customers?', 'What name the business uses', ('Who the owner\'s doctor is', 'unrelated'),
          ('The owner\'s salary', 'unrelated'), ('The bank balance', 'unrelated'), 'It is the public-facing name.'),
    ], why='A learner who misses MAIN may think a DBA creates protection or a new entity; the name-tag picture corrects it.')],
    F1=sec('Apply it: when a DBA is needed and what it changes', DBA, [
        Q('Lee, a sole proprietor, opens a bank account for "Lee\'s Lawns." The bank asks for a DBA certificate. Why?',
          'The business name differs from Lee\'s legal name', ('Because a DBA replaces the owner\'s driver\'s license', 'no'),
          ('Because banks issue DBAs', 'banks do not issue them'), ('Because it creates an LLC', 'it does not'),
          'Banks often require proof the business may use that name.'),
        Q('Which business most likely needs a DBA?', '"Green Path LLC" selling under the name "Fresh Bowls"',
          ('"Green Path LLC" selling only as "Green Path LLC"', 'same as legal name'),
          ('Jane Smith selling as "Jane Smith"', 'same as legal name'),
          ('A business with no name at all', 'unusual case'), 'Using a different name usually needs a DBA where required.'),
        Q('A sole proprietor files a DBA to look more official. What does she still lack?', 'Liability protection',
          ('A business name to use', 'she has one'), ('Permission to sell', 'licenses are separate, but she has the name'),
          ('Customers', 'unrelated'), 'A DBA adds a name, not protection.'),
        Q('A DBA filing costs 25 dollars and must be renewed every 5 years. Over a 15-year window (the first filing now plus renewals at years 5 and 10), how much is spent, assuming the same fee?',
          '75 dollars',
          ('25 dollars', 'only the first filing'), ('375 dollars', 'multiplies wrongly'),
          ('15 dollars', 'not the fee'),
          '3 filings x 25 dollars = 75 dollars (fees are example assumptions).',
          calc=lambda: 15 // 5 * 25 == 75),
        Q('Which step would actually give some liability protection?', 'Forming an LLC or corporation', ('Filing a DBA', 'no protection'),
          ('Ordering business cards with "LLC"', 'no protection'), ('Buying a domain', 'no protection'),
          'Entity formation, not a DBA, aims at liability separation.'),
    ]),
    F2=sec('Handle the complications: DBA myths and checks', DBA, [
        Q('An owner believes his DBA means no one else can use "River Tees." What should he check?',
          'Trademark records and whether anyone else already uses the name', ('Nothing; the DBA protects the name everywhere in the nation', 'false'),
          ('Only his county website', 'not enough'), ('Only his domain registrar', 'not enough'),
          'A DBA does not give trademark rights.'),
        Q('A business uses a DBA in two counties. What should the owner check?', 'Whether each county requires its own filing',
          ('Whether one filing covers every country in the world', 'no'), ('Whether DBAs are illegal', 'they are legal'),
          ('Whether the logo needs a DBA', 'no'), 'Filing rules vary by place.'),
        Q('A customer contract is signed only as "Fresh Bowls" with no legal name. What is the risk?',
          'Confusion about which legal entity is responsible', ('None at all', 'confusion is possible'),
          ('Signing as Fresh Bowls creates a new LLC called Fresh Bowls', 'no'), ('It cancels the DBA', 'no'),
          'Showing the legal name with the DBA reduces confusion.'),
        Q('A founder plans: "File DBA, then sell food from home." What else must be checked?',
          'Licenses, permits and local rules for selling food', ('Nothing; the DBA is enough', 'no'),
          ('Only the font and layout of the printed DBA certificate', 'no'), ('Only competitor prices', 'not the key gap'),
          'Selling food usually involves separate rules; a DBA is only a name.'),
        Q('Which statement is accurate?', 'A DBA can be useful, but it is only a registered name.',
          ('A DBA replaces the need to form an LLC for protection.', 'no'), ('A DBA lowers taxes.', 'no'), ('A DBA is a trademark.', 'no'),
          'A DBA has a narrow purpose.'),
    ]))

# ------------------------------------------------------------------ Set 27: guarantees
GUAR = ('Limited liability has gaps. A PERSONAL GUARANTEE is a promise you sign to pay a business debt yourself if the '
        'business cannot. Lenders, landlords and some suppliers often ask new business owners for one, because the '
        'business has little history. If you sign it, your personal savings and other assets can be used to pay that '
        'debt, even if you have an LLC. Personal guarantees can be hidden in long forms. Read before signing, ask what '
        'you are guaranteeing, and consider whether the amount is one you could pay personally.')

s27 = SET('ENT.LEGAL.09',
    M=sec('Recognize personal guarantees and how they bypass limited liability', GUAR, [
        Q('What is a personal guarantee?', 'A promise to pay a business debt yourself if the business cannot',
          ('A guarantee that the business will make a profit this year', 'not what it is'),
          ('A warranty you give customers on a product', 'different meaning'),
          ('A promise by the bank to lend you more money later', 'not what it is'),
          'It makes you personally responsible for that debt.'),
        Q('An LLC owner signed a personal guarantee on the shop lease. The business closes. Who may owe the rest of the '
          'lease?', 'The owner personally', ('No one, because the LLC closed', 'the guarantee remains'),
          ('Only the landlord', 'the landlord is owed'), ('The state', 'no'),
          'The guarantee makes the owner responsible.'),
        Q('Why do lenders often ask new owners for guarantees?', 'New businesses have little history.',
          ('Because guarantees are required by every state.', 'not a universal law'),
          ('Because guarantees lower the owner\'s taxes.', 'unrelated'),
          ('Because LLCs cannot sign contracts.', 'they can'), 'Lenders want someone with a track record responsible.'),
        Q('Where can a personal guarantee sometimes hide?', 'Inside a long application or contract',
          ('Only on billboards outside the bank', 'no'), ('Only in social media ads', 'no'),
          ('Only in the company logo', 'no'), 'Read long forms carefully.'),
        Q('Before signing a guarantee, what should an owner ask?', 'Could I pay this amount personally if needed?',
          ('Is the paper a nice color?', 'irrelevant'), ('How fast can I sign?', 'speed is not the point'),
          ('Will signing this make my company logo look better?', 'irrelevant'), 'Consider the personal risk.'),
    ]),
    B=[cs('Co-signing for a friend', 'Imagine co-signing a friend\'s phone contract. If your friend stops paying, the phone '
          'company can ask you to pay. A personal guarantee for your business works the same way: you are co-signing for '
          'your own company. Your LLC may be the main borrower, but your signature means you will pay if it cannot. '
          'That is why it matters so much.', [
        Q('Co-signing means what?', 'You may have to pay if the main borrower does not', ('You get a free phone', 'no'),
          ('You can never be asked to pay anything at all', 'you can'), ('You own the company', 'no'), 'The co-signer backs the debt.'),
        Q('A personal guarantee is like co-signing for whom?', 'Your own business', ('A stranger', 'no'),
          ('The bank', 'no'), ('A competitor down the street', 'no'), 'You back your company\'s debt.'),
        Q('If the LLC cannot pay a guaranteed debt, who may pay?', 'The person who signed the guarantee',
          ('Nobody', 'someone owes it'), ('The business\'s regular customers', 'no'), ('The state', 'no'), 'The guarantor pays.'),
        Q('Who is the main borrower on a business loan with a guarantee?', 'The business', ('The guarantor only', 'the business borrows'),
          ('The bank', 'the bank lends'), ('The landlord', 'no'), 'The business borrows; the guarantor backs it.'),
        Q('Does an LLC stop a guarantor from having to pay?', 'No', ('Yes, always', 'no'), ('Only if small', 'no'),
          ('Only in summer', 'no'), 'The guarantee is personal.'),
    ], why='A learner who misses MAIN may not see how a guarantee works; co-signing is a familiar comparison.')],
    F1=sec('Apply it: read offers that include guarantees', GUAR, [
        Q('A supplier offers 30-day payment terms if the owner signs a personal guarantee up to 5,000 dollars. The owner '
          'has 1,000 dollars in savings. What is the main concern?', 'She could owe more than she could personally pay',
          ('Payment terms are always free of risk', 'not with a guarantee'),
          ('Guarantees only apply to big companies', 'no'), ('The supplier will never actually ask anyone for payment', 'they may'),
          'A 5,000-dollar guarantee exceeds her 1,000 dollars of savings.', calc=lambda: 5000 > 1000),
        Q('Two lease offers: A requires a personal guarantee; B costs 100 dollars more a month with no guarantee. The '
          'owner\'s priority is protecting her house. Which fits her priority?', 'Offer B, without the guarantee',
          ('Offer A, because it is cheaper', 'it adds personal risk'),
          ('Neither, because all leases require guarantees', 'not true here'),
          ('Offer A, because guarantees never get used', 'they can be used'), 'Avoiding the guarantee protects personal assets.'),
        Q('A loan application has a page titled "Unconditional Guaranty." What should the owner do?', 'Read it and ask what it covers before signing',
          ('Sign quickly so the loan closes faster', 'risky'), ('Ignore it because it is a standard form', 'it matters'),
          ('Cross it out without telling the lender', 'not an agreement'), 'Understanding the guarantee is essential.'),
        Q('A guarantee covers a 12,000-dollar loan. The business repays 9,000 dollars and then closes. How much might the '
          'guarantor owe, ignoring interest and fees?', '3,000 dollars', ('12,000 dollars', 'ignores repayments'),
          ('9,000 dollars', 'that was repaid'), ('0 dollars', 'a balance remains'),
          '12,000 - 9,000 = 3,000 dollars remaining.', calc=lambda: 12000 - 9000 == 3000),
        Q('Which action can reduce guarantee risk?', 'Negotiating a limit or a time period on the guarantee',
          ('Signing several guarantees at once', 'increases risk'), ('Hiding the guarantee from a business partner so they do not worry', 'unfair'),
          ('Ignoring the amount', 'risky'), 'Limits and time periods can reduce exposure.'),
    ]),
    F2=sec('Handle the complications: guarantees and partners', GUAR, [
        Q('Two partners own an LLC equally. Only one signs a personal guarantee. What should the partners discuss?',
          'How they will share that risk fairly', ('Nothing; guarantees are always shared automatically', 'not automatically'),
          ('Whether to change the logo', 'unrelated'), ('Whether to stop keeping records', 'harmful'),
          'Uneven personal risk should be addressed in their agreement.'),
        Q('An owner says, "I have an LLC, so the guarantee does not matter." What is wrong?',
          'The guarantee makes her personally responsible despite the LLC', ('Nothing; the LLC overrides it', 'no'),
          ('Personal guarantees are illegal for anyone who owns an LLC', 'no'), ('Guarantees expire when signed', 'no'),
          'A personal guarantee bypasses limited liability for that debt.'),
        Q('Which missing information should be checked before signing a guarantee?', 'The maximum amount and how long it lasts',
          ('The lender\'s office paint color', 'irrelevant'), ('How many employees the lender has', 'irrelevant'),
          ('Whether the lender likes your logo', 'irrelevant'), 'Amount and duration define the risk.'),
        Q('A business owner\'s spouse is asked to sign a guarantee too. What should the spouse understand?',
          'Their personal assets could also be used for the debt', ('Spouses can never be responsible', 'they can if they sign'),
          ('Signing only helps the credit score', 'it creates liability'),
          ('It is just a formality that has no legal effect on the spouse', 'it has effect'), 'Anyone who signs can be personally responsible.'),
        Q('Who is the best person to review a large guarantee before signing?', 'A business attorney',
          ('A social media follower', 'not qualified'), ('The lender only', 'they represent the lender'),
          ('A graphic designer', 'not qualified'), 'Independent legal advice helps.'),
    ]))

# ------------------------------------------------------------------ Set 28: licenses, permits, zoning
LIC = ('Many activities need permission from a government before you start. A BUSINESS LICENSE is general permission '
       'to operate in a city or county. A PERMIT covers a specific activity, such as selling food, putting up a sign, '
       'or doing construction. ZONING rules say what activities are allowed at a location, including homes; some '
       'neighborhoods limit customer visits, signs, parking or noise. Some jobs, such as hair care or electrical work, '
       'need a professional license. Rules depend on the activity and the place: city, county, state and sometimes '
       'federal. Rental leases and homeowner associations can add limits.')

s28 = SET('ENT.LEGAL.10',
    M=sec('Identify which permissions to check for an activity and place', LIC, [
        Q('Lucy wants to sell homemade baked goods from her kitchen. What should she check?',
          'Local and state rules for selling food made at home', ('Only whether her friends and neighbors like her cookies', 'not a legal check'),
          ('Only the price of flour at the store', 'not a legal check'), ('Only how to post on social media', 'not a legal check'),
          'Food sales often have specific rules.'),
        Q('What do zoning rules decide?', 'What activities are allowed at a location',
          ('Which colors a business logo may use', 'not zoning'), ('How much tax the owner pays each year', 'not zoning'),
          ('Which bank the business must use', 'not zoning'), 'Zoning is about land use and location.'),
        Q('Which job most likely needs a professional license?', 'Electrical wiring in customers\' homes',
          ('Selling greeting cards online', 'usually no special license'),
          ('Writing a personal blog for fun', 'not a business license issue'),
          ('Dog photography at a park', 'usually no professional license'),
          'Electrical work commonly needs a license.'),
        Q('Who sets licensing and permit rules?', 'It depends: city, county, state and sometimes federal agencies',
          ('Only the business owner\'s friends', 'no'), ('Only the federal government, for every business in the country', 'too narrow'),
          ('Only the bank that holds the account', 'no'), 'Several levels can apply.'),
        Q('A tenant wants to run a business from an apartment. What else besides city rules should she check?',
          'Her lease terms', ('Her favorite restaurant\'s hours', 'irrelevant'), ('A competitor\'s logo', 'irrelevant'),
          ('The weather forecast', 'irrelevant'), 'Leases can limit business use.'),
    ]),
    B=[cs('Permission slips', 'Think of permission slips at school: one lets you go on a field trip, another lets you play '
          'a sport. A business may need several kinds: a general business license (permission to operate), a permit for '
          'a specific activity (like serving food), and approval that the location allows the activity (zoning). Some '
          'people also need a personal professional license, like a driver\'s license for a job. Each comes from the '
          'group in charge of that rule.', [
        Q('A general business license is like which permission slip?', 'Permission to operate at all', ('Permission to drive a car', 'that is personal'),
          ('Permission to skip class', 'unrelated'), ('Permission to change a logo', 'not needed'), 'It is broad permission.'),
        Q('A food permit covers what?', 'A specific activity: selling food', ('All business activity everywhere', 'too broad'),
          ('The owner\'s taxes', 'unrelated'), ('The company name', 'unrelated'), 'Permits cover specific activities.'),
        Q('Zoning approval is about what?', 'Whether the location allows the activity', ('The owner\'s education level and degrees', 'no'),
          ('The product\'s price', 'no'), ('The website design', 'no'), 'Zoning concerns the place.'),
        Q('A hair stylist\'s license is which kind?', 'A personal professional license', ('A zoning rule for the salon', 'no'),
          ('A trademark', 'no'), ('A DBA', 'no'), 'It applies to the person doing the work.'),
        Q('Who issues each permission?', 'The group in charge of that rule', ('The business owner alone, by choice', 'no'),
          ('Customers', 'no'), ('Competitors', 'no'), 'Each authority issues its own permission.'),
    ], why='A learner who misses MAIN may lump all permissions together; permission slips separate the kinds.')],
    F1=sec('Apply it: make a permissions checklist', LIC, [
        Q('Sam wants to run a home-based tutoring business with students visiting 4 evenings a week. Which checks fit best?',
          'City business license, zoning limits on home visits, and his lease or HOA rules', ('Only a food permit', 'he is not selling food'),
          ('Only a trademark search', 'not the main permission'), ('Only a social media account to advertise the tutoring sessions to local families', 'not a permission'),
          'Visits to a home business can trigger zoning and lease rules.'),
        Q('A food truck plans to sell in two cities. What should the owner check?', 'Each city\'s permits and rules',
          ('One city\'s rules, since all cities match', 'they differ'), ('Only the truck\'s paint color', 'irrelevant'),
          ('Nothing, trucks are always exempt', 'no'), 'Each city may have its own permits.'),
        Q('A city charges 50 dollars for a business license and 120 dollars for a sign permit. What is the total for '
          'both?', '170 dollars', ('120 dollars', 'only the sign permit'), ('50 dollars', 'only the license'),
          ('70 dollars', 'the difference'), '50 + 120 = 170 dollars (example fees).', calc=lambda: 50 + 120 == 170),
        Q('An online-only digital product seller works from home with no visitors. Which check is still sensible?',
          'Whether the city or state requires a general business license or registration', ('A food handler permit and a restaurant health inspection for the home kitchen', 'not relevant'),
          ('A liquor license', 'not relevant'), ('A construction permit', 'not relevant'),
          'Even online businesses may need general registration where they are based.'),
        Q('Where is the best place to find local requirements?', 'The city or county government\'s business office or website',
          ('A random forum post', 'unreliable'), ('A competitor', 'unreliable'), ('The comment section under a video about business licenses', 'unreliable'),
          'Official local sources give current requirements.'),
    ]),
    F2=sec('Handle the complications: assumptions about home businesses', LIC, [
        Q('A friend says, "Home businesses never need permits." What is wrong with this?', 'Rules depend on the activity and location',
          ('Nothing; it is always true', 'false'), ('Home businesses are illegal everywhere', 'false'),
          ('Only big businesses exist', 'false'), 'Many home businesses need registration or permits.'),
        Q('A dog groomer\'s city allows home businesses, but her homeowner association bans customer visits. What '
          'should she do?', 'Follow both sets of rules or find another location', ('Ignore the association because the city allows it', 'both can apply'),
          ('Ask customers to keep visits secret', 'not honest'), ('Assume rules never get enforced', 'risky'),
          'Private association rules can add limits beyond city rules.'),
        Q('Which missing check is the biggest risk in this plan? "Rent a shop, print signs, open next week."',
          'Whether zoning and permits allow this use at the shop', ('Whether the printed signs are colorful enough to attract walkers', 'minor'),
          ('Whether the website loads fast', 'minor'), ('Whether competitors are nearby', 'not a permission'),
          'Opening without allowed use and permits can force closure.'),
        Q('A license must be renewed each year. What is a sensible habit?', 'Put renewal dates on a deadline calendar',
          ('Wait for a reminder that may never come', 'risky'), ('Renew only if inspected', 'not compliant'),
          ('Assume one license lasts forever', 'often false'), 'Tracking renewals avoids lapses.'),
        Q('Which statement is accurate for this course?', 'Rules vary by place, so check the official sources where you operate.',
          ('New Jersey\'s rules apply the same way everywhere in the US.', 'no single state\'s rules apply everywhere'),
          ('Federal rules replace all local rules.', 'not true'),
          ('No business needs any permission.', 'false'), 'Jurisdiction matters.'),
    ]))

# ------------------------------------------------------------------ Set 29: when to ask a professional
PRO = ('Some questions are worth paying an expert to answer. An ATTORNEY helps with legal questions: contracts, entity '
       'choice, disputes, leases and trademarks. An ACCOUNTANT or tax professional helps with taxes, bookkeeping set-up, '
       'tax elections and estimated payments. An INSURANCE AGENT helps match coverage to risks. Get help when the stakes '
       'are high, the rules are complex, or a mistake would be hard to undo. Prepare: write your questions, bring '
       'documents, and ask about fees before you start.')

s29 = SET('ENT.LEGAL.11',
    M=sec('Decide when a question needs a professional and prepare', PRO, [
        Q('Which professional best fits a question about a confusing lease clause?', 'An attorney',
          ('A graphic designer who made the logo', 'not legal'), ('A social media manager', 'not legal'),
          ('A delivery driver', 'not legal'), 'Lease clauses are legal questions.'),
        Q('Which professional best fits a question about whether to make a tax election?', 'An accountant or tax professional',
          ('A web developer who builds websites', 'not tax'), ('A sign maker', 'not tax'), ('A florist', 'not tax'),
          'Tax elections are tax questions.'),
        Q('When is professional help most worth paying for?', 'When stakes are high and mistakes are hard to undo',
          ('When choosing a font for the business\'s social media posts', 'low stakes'), ('When ordering pens', 'low stakes'),
          ('When picking a lunch spot', 'irrelevant'), 'High stakes justify expert help.'),
        Q('What is a good way to prepare for a meeting with an expert?', 'Write questions and bring documents',
          ('Arrive with no questions to save time', 'wastes time'), ('Avoid asking about fees', 'fees matter'),
          ('Bring only a logo sketch', 'not enough'), 'Preparation saves time and money.'),
        Q('Which professional helps match coverage to business risks?', 'An insurance agent or broker', ('A trademark examiner at the agency', 'no'),
          ('A banker', 'not insurance'), ('A copywriter', 'no'), 'Insurance professionals match coverage to risks.'),
    ]),
    B=[cs('Matching the question to the expert', 'Think of health: you see a dentist for teeth and an eye doctor for eyes. '
          'Business questions work the same way. Legal questions (contracts, leases, disputes) go to an attorney. Money '
          'and tax questions go to an accountant or tax professional. Coverage questions go to an insurance agent. '
          'Asking the right expert saves time and gets a better answer.', [
        Q('A contract question goes to whom?', 'An attorney', ('An accountant', 'tax'), ('An insurance agent', 'coverage'),
          ('A designer', 'not legal'), 'Contracts are legal.'),
        Q('A tax question goes to whom?', 'An accountant or tax professional', ('An attorney only, never anyone else', 'tax pro fits better'),
          ('A dentist', 'no'), ('A designer', 'no'), 'Taxes go to a tax professional.'),
        Q('An insurance coverage question goes to whom?', 'An insurance agent', ('A chef', 'no'), ('A tutor', 'no'),
          ('A store cashier', 'no'), 'Coverage goes to an insurance professional.'),
        Q('Why match the question to the expert?', 'To get a better answer faster', ('To pay more', 'not the goal'),
          ('To avoid all advice', 'no'), ('To confuse the expert on purpose', 'no'), 'The right expert answers best.'),
        Q('A dentist for teeth is like what for a lease dispute?', 'An attorney', ('A baker', 'no'), ('A house painter', 'no'),
          ('A coach', 'no'), 'Legal disputes go to an attorney.'),
    ], why='A learner who misses MAIN may not know which expert fits; the doctor comparison makes matching easy.')],
    F1=sec('Apply it: decide whether to get help now', PRO, [
        Q('Mia is about to sign a 5-year commercial lease with a personal guarantee. What is the best step?',
          'Have an attorney review it before signing', ('Sign quickly before the landlord changes his mind', 'risky'),
          ('Ask a friend who once rented an apartment', 'not equivalent'), ('Skip reading the guarantee page', 'risky'),
          'A long lease with a guarantee is high stakes.'),
        Q('Jon needs to choose a font for his flyers. Does he need an attorney?', 'No, this is a low-stakes design choice',
          ('Yes, every decision needs an attorney', 'too costly'), ('Yes, fonts are legal contracts', 'no'),
          ('Yes, attorneys design flyers', 'no'), 'Low-stakes choices rarely need legal help (though licensed font use matters).'),
        Q('An attorney charges 200 dollars an hour. A lease review takes 1.5 hours. What is the cost?', '300 dollars',
          ('200 dollars', 'one hour'), ('400 dollars', 'two hours'), ('201.5 dollars', 'adds instead of multiplying'),
          '200 x 1.5 = 300 dollars (example rate).', calc=lambda: 200 * 1.5 == 300),
        Q('Which question is best brought to a tax professional?', 'How to plan estimated tax payments for a new business',
          ('Which color to paint the shop\'s front door this spring', 'not tax'), ('How to write an Instagram caption', 'not tax'),
          ('Which supplier has nicer boxes', 'not tax'), 'Estimated tax planning is a tax question.'),
        Q('A founder can afford only one paid consultation this month. Which use is most valuable?',
          'Reviewing the partnership agreement before both partners sign', ('Choosing a logo color', 'low stakes'),
          ('Picking a nice email signature for every message she sends', 'low stakes'), ('Naming a product flavor', 'low stakes'),
          'A binding agreement between owners is high stakes.'),
    ]),
    F2=sec('Handle the complications: free help, limits and preparation', PRO, [
        Q('A free online article explains LLC rules but is from another state and five years old. What is the limit?',
          'It may not match current rules where you operate', ('It is always perfectly accurate', 'not necessarily'),
          ('Articles can never be useful', 'they can help'), ('It fully replaces all professional advice for every owner', 'no'),
          'Location and date matter for legal information.'),
        Q('A founder asks a lawyer friend casually at a party about a lawsuit threat. What is the concern?',
          'Casual answers may be incomplete; a proper consultation is safer', ('No concern; advice given at a party is binding and complete', 'not reliable'),
          ('Lawyers never answer questions', 'they do'), ('The lawsuit will disappear', 'no'),
          'Serious issues need proper advice with full facts.'),
        Q('Before hiring an accountant, which question should the owner ask?', 'What the fee is and what is included',
          ('What the accountant\'s favorite movie is', 'irrelevant'), ('Whether the accountant uses social media', 'irrelevant'),
          ('Whether the accountant likes the logo', 'irrelevant'), 'Fees and scope prevent surprises.'),
        Q('A founder uses an AI tool to draft a contract. What is the sensible next step for an important deal?',
          'Have a qualified professional review it', ('Sign it as written', 'AI can make errors'),
          ('Assume AI drafts are legally verified', 'they are not'), ('Delete all contracts', 'no'),
          'AI drafts need human professional review for important matters.'),
        Q('Which statement fits this course?', 'Education explains what to check; individual decisions may need professional advice.',
          ('This course gives each learner individual legal advice for their own business.', 'it does not'), ('Professionals are never needed.', 'sometimes they are'),
          ('Every question needs a lawyer.', 'too costly and unnecessary'), 'The course teaches what to check and why.'),
    ]))

SETS = [s24, s25, s26, s27, s28, s29]
