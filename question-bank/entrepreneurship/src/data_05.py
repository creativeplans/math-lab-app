"""Entrepreneurship sets 19-23: Foundation 4, names and legal structure (part 1)."""
from eq import Q, sec, cs, SET

# ------------------------------------------------------------------ Set 19: name, entity, brand
NAME = (('Three different things are easy to mix up. The LEGAL IDENTITY is the business as the law sees it, with its '
        'legal name. A sole proprietorship is not separate from its owner; an LLC (limited liability company) is a '
        'separate LEGAL ENTITY, with its official name on state records. The BUSINESS NAME customers see may be '
        'different, such as a trade name. The BRAND is how customers recognize and feel about the business: its logo,'
        ' colors, voice and reputation. Example: "Rivera Services LLC" (entity) might operate as "Sparkle Clean" '
        '(name customers see) with a blue bubble logo (brand).'))

s19 = SET('ENT.LEGAL.01',
    M=sec('Tell a business name, a legal entity and a brand apart', NAME, [
        Q('"Rivera Services LLC" operates as "Sparkle Clean" and uses a blue bubble logo. Which is the legal entity?',
          'Rivera Services LLC', ('Sparkle Clean, the name printed on the van doors', 'that is the name customers see'),
          ('The blue bubble logo used on the website', 'that is part of the brand'),
          ('The owner, Ms. Rivera, as a private person', 'the LLC is the entity'),
          'The LLC on state records is the legal entity.'),
        Q('In the same example, what is "Sparkle Clean"?', 'The name customers see',
          ('The legal entity registered with the state as an LLC', 'that is Rivera Services LLC'),
          ('The bank account where all the payments go', 'not a name'),
          ('The tax number the business uses for filings', 'not a name'), 'It is the trade name used with customers.'),
        Q('Which is part of a BRAND?', 'The business\'s logo and the tone of its messages',
          ('The official filing number the state gave the LLC', 'that is a legal record'),
          ('The type of entity, such as an LLC or a corporation', 'that is legal structure'),
          ('The name of the registered agent on state records', 'that is a legal role'),
          'Logo, colors, voice and reputation make up the brand.'),
        Q('Can a business\'s legal name and the name customers see be different?', 'Yes, often',
          ('No, the law always requires them to be identical everywhere', 'businesses often use trade names'),
          ('Only for very large public companies with many stores', 'small businesses do it too'),
          ('Only if the owner changes the bank account first', 'unrelated'),
          'A business may operate under a different name, often after registering it as a trade name where required.'),
        Q('A customer says, "I love that company; they are always friendly." What is the customer describing?', 'The brand',
          ('The legal entity type listed in the state database', 'customers rarely see that'),
          ('The owner\'s personal tax filing status this year', 'not customer-facing'),
          ('The registered agent\'s office address in the state', 'not customer-facing'),
          'Feelings and reputation are part of the brand.'),
    ]),
    B=[cs('Person, nickname, reputation', ('Think about a person. Their legal name is on official papers: "Robert James Lee." Friends call him "Bobby": '
                                          'a nickname. People who know him say he is reliable and funny: his reputation. A business works the same way.'
                                          ' The legal name is the one on official papers (for an LLC, the name of the separate legal entity). The '
                                          'business name customers see is like a nickname. The brand is like a reputation and style that customers '
                                          'recognize.'), [
        Q('"Robert James Lee" on official papers is like a business\'s what?', 'Legal entity name',
          ('Brand and reputation with customers', 'that is reputation'),
          ('Nickname used by friends and customers', 'that is "Bobby"'), ('Logo', 'not a name'), 'Official papers show the legal name.'),
        Q('"Bobby" is like a business\'s what?', 'Name customers see', ('Legal entity on state records', 'that is the legal name'),
          ('Tax identification number', 'unrelated'), ('Insurance policy', 'unrelated'), 'A nickname is like a trade name.'),
        Q('"Reliable and funny" is like a business\'s what?', 'Brand', ('Legal entity', 'not a reputation'),
          ('Bank account', 'unrelated'), ('Mailing address', 'unrelated'), 'Reputation matches brand.'),
        Q('Which belongs on official legal papers?', 'The legal entity name', ('The logo colors', 'brand'),
          ('A customer review posted online', 'reputation'), ('A slogan', 'brand'), 'Legal papers use the legal name.'),
        Q('Which can change without any legal filing in most cases?', 'The colors on a logo', ('The name of an LLC on state records',
                                                                                              'usually requires a filing'),
          ('The type of legal entity', 'requires legal steps'), ('The registered agent on file', 'requires a filing'),
          'Brand design changes usually do not require filings (though trademark issues can still matter).'),
    ], why='A learner who misses MAIN may blur the three ideas; a person\'s legal name, nickname and reputation map onto '
           'them clearly.')],
    F1=sec('Apply it: use the right name in the right place', NAME, [
        Q('"Kim Design LLC" operates as "Pixel Pine." Which name belongs on a contract the LLC signs?', 'Kim Design LLC',
          ('Pixel Pine only, with no mention of the LLC', 'the legal entity should be identified'),
          ('The owner\'s first name only, Jenny', 'the LLC is the party'),
          ('The logo image instead of any written name', 'a contract needs the legal name'),
          'Contracts should name the legal entity (often with "doing business as" the trade name).'),
        Q('Which name usually appears on store signs and the website?', 'The name customers see',
          ('The registered agent\'s company name', 'not customer-facing'),
          ('The bank\'s name for the business account', 'not the business name'),
          ('The state filing number for the entity', 'not a name'), 'Customers see the trade name or brand name.'),
        Q('A baker changes her logo from pink to green. What has changed?', 'Only part of the brand',
          ('Her legal entity type, from LLC to corporation', 'colors do not change entity type'),
          ('Her state registration and filing number', 'not affected'),
          ('Her tax classification with the IRS', 'not affected'), 'Logo colors are brand elements.'),
        Q('An LLC wants customers to see a different name from its legal name. What should the owner check?',
          'Whether the state or county requires registering that trade name', ('Whether the logo is pretty enough', 'not a legal question'),
          ('Whether longtime customers liked the old name better than the new one', 'not the legal question'),
          ('Whether the bank account is open', 'not the main check'),
          'Using a different name often requires a trade name (DBA) filing; rules vary by state.'),
        Q('Which situation mixes up name and brand?', 'Thinking a new logo protects the business name from use by others',
          ('Using the LLC name on contracts and the trade name on signs', 'correct use'),
          ('Keeping the same colors across the website and van', 'consistent branding'),
          ('Checking whether a trade name must be registered', 'sensible check'),
          'A logo is branding; protecting a name involves separate legal steps.'),
    ]),
    F2=sec('Handle the complications: names, records and assumptions', NAME, [
        Q('A customer\'s payment fails because the invoice shows only "Pixel Pine," but the bank account is in the name '
          '"Kim Design LLC." What would most likely help?', 'Show the legal name with the trade name, such as "Kim Design LLC dba Pixel Pine"',
          ('Change the logo and colors so the invoice looks nicer and more professional', 'not the issue'),
          ('Remove all names from future invoices', 'makes it worse'),
          ('Ask the customer to pay the owner personally', 'mixes personal and business money'),
          'Matching the legal name to the account, with the trade name shown, reduces confusion.'),
        Q('An owner assumes that because her LLC name was approved by the state, no one else can use her brand name '
          'anywhere. What is wrong?', 'State approval of an entity name is not the same as trademark rights.',
          ('State approval of the LLC gives her worldwide ownership of the name.', 'it does not'),
          ('Nothing; approval protects the brand everywhere.', 'it does not'),
          ('Names can never be protected in any way.', 'trademarks are a separate process'),
          'Entity name approval and trademark protection are separate.'),
        Q('Two owners argue about whether to rename the business. Which question should be answered first?',
          'Which name is being changed: the legal entity name, the trade name, or the brand?',
          ('Which owner chose the first logo', 'not the first question'),
          ('Which of the two possible names sounds more modern and catchy to customers today', 'secondary'),
          ('Whether to close the bank account', 'premature'),
          'Each kind of name change involves different steps.'),
        Q('A business operates under three trade names. What extra task does this most likely create?',
          'Keeping each name\'s registrations and records straight', ('Nothing at all; extra names never add work', 'they do'),
          ('Forming three separate legal entities automatically', 'trade names do not create entities'),
          ('Changing the tax classification for each name', 'trade names do not change taxes'),
          'Each trade name may need its own filing and consistent use.'),
        Q('Which statement is accurate?', 'One legal entity can use a different name with customers.',
          ('A brand is the same thing as the legal entity.', 'they are different'),
          ('A trade name creates a new legal entity.', 'it does not'),
          ('Logos must be registered with the state to be used.', 'not generally required'),
          'An entity may operate under a trade name; the entity is unchanged.'),
    ]))

# ------------------------------------------------------------------ Set 20: availability vs trademark
TM = ('Checking a name is not the same as owning it. A domain name you can buy, a social media handle that is free, or '
      'a state\'s approval of an LLC name only shows that THAT specific spot was available. It does not give trademark '
      'rights, and it does not mean the name is safe to use. Another business may already use the same or a similar '
      'name for similar goods or services, and could object. Before investing in a name, also search for businesses '
      'using it and consider a trademark search (US: the USPTO database). Rules: US, check current guidance.')

s20 = SET('ENT.LEGAL.02',
    M=sec('Separate name availability from trademark rights', TM, [
        Q('Nia bought the domain "glowpaws.com." What does this show?', 'That domain was available to buy.',
          ('She owns the trademark "Glow Paws" everywhere in the country.', 'a domain does not give trademark rights'),
          ('No other business anywhere may use the name "Glow Paws."', 'not shown'),
          ('The state has approved "Glow Paws" as her legal entity.', 'a domain is not a state filing'),
          'Buying a domain only shows that the domain was available.'),
        Q('The state approved "Blue Fern LLC." What does this approval mean?', 'The LLC can use that entity name in that state\'s records.',
          ('She has a federal trademark on "Blue Fern" in all fifty states.', 'state entity approval is not a trademark'),
          ('Nobody can ever sell products called Blue Fern.', 'not guaranteed'),
          ('The name is guaranteed safe from any legal objection.', 'not guaranteed'),
          'Entity name approval is a state record, not trademark protection.'),
        Q('Which search best helps check whether a brand name might conflict with others?', 'A trademark database search plus a web search',
          ('Only checking whether the domain name is for sale', 'not enough'),
          ('Only asking friends if they have heard of the name', 'not enough'),
          ('Only checking whether the social media handle is free', 'not enough'),
          'Searching trademark records and the web finds existing users of a name.'),
        Q('Why could a business object to a new company\'s name even if the domain was available?',
          'It may already use a similar name for similar goods.', ('Domains are always illegal to buy.', 'they are legal'),
          ('Only the government can object to names.', 'other businesses can object'),
          ('Names cannot be used by two businesses for any reason.', 'too absolute'),
          'Existing users of a name can have rights even without the domain.'),
        Q('Which statement is accurate?', 'A free social media handle does not give trademark rights.',
          ('A free handle gives the owner exclusive rights to the name.', 'not true'),
          ('A free handle proves no one else uses the name.', 'not true'),
          ('A free handle replaces the need for any search.', 'not true'), 'Handles show only availability on one platform.'),
    ]),
    B=[cs('An empty parking spot is not a deed', 'Finding an empty parking spot means you can park there right now. It does '
          'not mean you own the land. Name checks work the same way. An available domain or handle is an empty spot on '
          'one website. A state approving your LLC name is an empty spot in that state\'s list. None of them is a deed '
          'that proves you own the name against everyone else. Ownership-like rights to a brand name come from '
          'trademark law, which is a separate system.', [
        Q('An available domain is most like what?', 'An empty parking spot', ('A deed to land', 'it is not ownership'),
          ('A signed lease for ten years', 'not a lease'), ('A building permit', 'unrelated'), 'It is only availability.'),
        Q('Which gives ownership-like rights to a brand name?', 'Trademark law', ('Buying a domain', 'availability only'),
          ('Getting a free social handle', 'availability only'), ('Printing business cards', 'no rights'),
          'Trademark rights come from trademark law.'),
        Q('A state approving an LLC name is most like what?', 'An open spot on that state\'s list', ('A worldwide brand deed', 'too broad'),
          ('A federal trademark registration', 'separate'), ('A patent', 'unrelated'), 'It shows availability in state records.'),
        Q('Does an empty parking spot mean you own the land?', 'No', ('Yes, always', 'ownership is separate'),
          ('Only on weekends', 'no'), ('Only if you park first', 'no'), 'Using a spot is not owning it.'),
        Q('Which is a separate system from domain and state name checks?', 'Trademark law', ('Website hosting', 'not about name rights'),
          ('Phone numbers', 'unrelated'), ('Email newsletters', 'unrelated'), 'Trademarks are their own legal system.'),
    ], why='A learner who misses MAIN may treat availability as ownership; the parking-spot comparison separates them.')],
    F1=sec('Apply it: what to check before committing to a name', TM, [
        Q('Ravi plans to print 5,000 bags with his new brand name. Domain and handle are free. What should he do before '
          'printing?', 'Search trademark records and the web for similar names', ('Print right away, since the domain and handle were both free to register', 'not enough checking'),
          ('Ask only his family if they like the name', 'not a legal check'),
          ('Register a second domain to be safe', 'still only availability'),
          'A conflict found after printing would be expensive.'),
        Q('A search finds a company using "Bright Leaf" for tea in another state. Lina wants "Bright Leaf" for tea too. '
          'What is the most sensible next step?', 'Treat it as a possible conflict and consider another name or advice',
          ('Ignore it, because that company sells tea only in another state far away', 'distance does not always remove conflicts'),
          ('Copy their logo as well', 'makes the problem worse'),
          ('Assume her LLC filing protects her', 'it does not'),
          'Similar names for similar goods can conflict; get advice or choose another name.'),
        Q('Which name choice carries the lowest conflict risk, based only on these search results?',
          'A name with no similar uses found in trademark or web searches',
          ('A name used by a large company in the same industry', 'high risk'),
          ('A name very similar to a famous brand', 'high risk'),
          ('A name whose domain is available but used by a competitor offline', 'risk remains'),
          'Fewer existing similar uses means lower risk, though searches are not guarantees.'),
        Q('Which statement about a clear search is accurate?', 'It lowers risk but does not guarantee no conflict.',
          ('It guarantees no one can ever object.', 'searches can miss uses'),
          ('It gives the owner a trademark automatically.', 'registration is separate'),
          ('It is never worth doing.', 'it is worth doing'), 'Searches reduce but do not remove risk.'),
        Q('Who is the most appropriate person to ask about a possible trademark conflict?', 'A trademark attorney',
          ('A website hosting company', 'not legal advice'), ('A graphic designer', 'not legal advice'),
          ('A social media follower', 'not legal advice'), 'Trademark questions are legal questions.'),
    ]),
    F2=sec('Handle the complications: hidden assumptions about names', TM, [
        Q('An owner says, "My LLC name was approved, I bought the domain, and I got the handle, so I own the name." What '
          'is the unsupported assumption?', 'That availability checks create trademark ownership',
          ('That domain names can be bought at all by small businesses', 'they can be bought'),
          ('That LLCs need names', 'they do need names'),
          ('That handles can be registered', 'they can'), 'None of those steps is a trademark right.'),
        Q('A seller gets a letter saying her product name is too similar to another company\'s trademark. What is a '
          'sensible first step?', 'Read it carefully and get advice before responding', ('Ignore it, since her domain is valid', 'risky'),
          ('Post the letter online and mock the company', 'can make things worse'),
          ('Immediately pay any amount demanded', 'get advice first'),
          'Legal letters deserve careful reading and qualified advice.'),
        Q('Two businesses have similar names but sell very different things (bakery versus car repair) in different '
          'towns. What should a founder understand?', 'Conflict risk depends on similarity, goods and markets; check carefully',
          ('Similar names can never conflict at all', 'too absolute'),
          ('Any similar name is always illegal', 'too absolute'),
          ('Only the older business may ever use any similar name for anything at all', 'too absolute'),
          'Trademark questions depend on the specific facts.'),
        Q('Which check is MISSING from this plan? "Name chosen, domain bought, logo designed, bags ordered."',
          'A trademark and web search for similar names', ('A second, more colorful logo design for the bags', 'not missing'),
          ('A larger bag order', 'not missing'), ('A new email address', 'not the key gap'),
          'No step checks whether the name conflicts with existing marks.'),
        Q('A name search costs 0 dollars online. Reprinting 5,000 bags costs 0.60 dollars each. How much could skipping '
          'the search cost if the name must change?', '3,000 dollars', ('600 dollars', 'that uses 1,000 bags'),
          ('5,000 dollars total', 'that uses 1 dollar per bag'), ('60 dollars', 'that uses 100 bags'),
          '5,000 x 0.60 = 3,000 dollars of reprinting, not counting other costs.', calc=lambda: round(5000 * 0.60) == 3000),
    ]))

# ------------------------------------------------------------------ Set 21: sole prop and partnership
SOLE = ('A SOLE PROPRIETORSHIP is one person doing business without forming a separate entity. It is the default: if '
        'you sell on your own and do not register another form, you are usually a sole proprietor. It is simple, but the '
        'business is not separate from you, so you are personally responsible for its debts. A GENERAL PARTNERSHIP is '
        'two or more people doing business together for profit without forming another entity. Partners usually share '
        'profits and can each be personally responsible for business debts. Source: SBA guidance; state law varies.')

s21 = SET('ENT.LEGAL.03',
    M=sec('Describe sole proprietorships and general partnerships', SOLE, [
        Q('Jo starts selling crafts alone and registers no entity. What is her business most likely?', 'A sole proprietorship',
          ('An LLC, created automatically when she makes a sale', 'LLCs require a state filing'),
          ('A corporation, because she sells products to the public', 'corporations require filings'),
          ('A partnership, because she has customers', 'customers are not partners'),
          'Doing business alone without forming an entity is usually a sole proprietorship.'),
        Q('What is the main risk of a sole proprietorship?', 'The owner is personally responsible for business debts.',
          ('It can never earn a profit under the law.', 'it can earn profits'),
          ('It must have at least ten employees on payroll.', 'no such rule'),
          ('It is always taxed as a large corporation.', 'not true'),
          'The owner and business are not separate, so debts can reach personal assets.'),
        Q('Two friends start a painting business together, share profits, and form no entity. What is it most likely?',
          'A general partnership', ('A sole proprietorship, since only one can own it', 'there are two owners'),
          ('An LLC, because two people are involved', 'an LLC requires a filing'),
          ('A nonprofit, because they are friends', 'unrelated'), 'Two or more people in business together without an entity is usually a partnership.'),
        Q('In a general partnership, who can be personally responsible for business debts?', 'Usually each partner',
          ('Only the partner who signed the most recent contract', 'responsibility is usually shared'),
          ('No one, because the partnership is a separate shield', 'general partners usually are responsible'),
          ('Only the customers who owe the business money', 'customers are not responsible for the business\'s debts'),
          'General partners can each be personally responsible.'),
        Q('What is a main advantage of a sole proprietorship?', 'It is simple to start.',
          ('It always protects personal savings from lawsuits.', 'it does not'),
          ('It must be approved by the federal government.', 'no such requirement'),
          ('It guarantees lower taxes than other forms.', 'not guaranteed'),
          'Few formal steps are needed, though local licenses and permits may still apply.'),
    ]),
    B=[cs('You and the business are the same', 'In a sole proprietorship, there is no wall between you and the business. '
          'Picture one wallet: business money and debts are legally yours. If the business owes a supplier, you owe the '
          'supplier. A general partnership is like several people sharing that same wallet: each can be on the hook for '
          'what the business owes. Forming an LLC or corporation is how some owners try to build a wall, but that is a '
          'separate step with its own limits.', [
        Q('In a sole proprietorship, whose debt is the business\'s debt?', 'The owner\'s', ('Only the customers\'', 'no'),
          ('The bank\'s', 'no'), ('No one\'s', 'debts belong to someone'), 'Owner and business are the same legally.'),
        Q('Is there a legal wall between a sole proprietor and the business?', 'No', ('Yes, always', 'not in this form'),
          ('Only for small debts', 'no such rule'), ('Only on weekends', 'no'), 'There is no separation.'),
        Q('A general partnership is like what?', 'Several people sharing one wallet', ('One person with two wallets', 'not quite'),
          ('A wall between owners and debts', 'that is what some other forms try'), ('A bank loan', 'unrelated'),
          'Partners share the business and its debts.'),
        Q('What do some owners form to try to build a wall?', 'An LLC or corporation', ('A logo', 'branding'),
          ('A website', 'not a legal entity'), ('A business card with a printed logo', 'no legal effect'), 'Entities can separate liability, with limits.'),
        Q('If a sole proprietor\'s business owes a supplier, who owes the supplier?', 'The owner', ('Nobody', 'someone owes it'),
          ('The supplier\'s customers', 'unrelated'), ('The local library', 'unrelated'), 'The owner is personally responsible.'),
    ], why='A learner who misses MAIN may not grasp personal responsibility; the one-wallet picture shows why it matters.')],
    F1=sec('Apply it: recognize the structure and its risk', SOLE, [
        Q('Mo tutors on his own, files nothing with the state, and a client sues him over a missed contract. Whose assets '
          'could be at risk?', 'Mo\'s personal assets, since he is a sole proprietor',
          ('Only the tutoring business\'s separate assets, protected from Mo', 'there is no separation'),
          ('No one\'s, because tutoring is too small to sue', 'size does not prevent lawsuits'),
          ('Only the client\'s assets', 'the client is suing Mo'),
          'Without a separate entity, Mo is personally responsible.'),
        Q('Two partners have no written agreement. One partner orders 3,000 dollars of supplies for the business without '
          'telling the other. What risk does this show?', 'Each partner can create debts that affect both',
          ('Only the ordering partner can ever be responsible', 'partners usually share responsibility'),
          ('The order is automatically canceled by law', 'not automatically'),
          ('Partnerships cannot buy supplies', 'they can'),
          'In a general partnership, one partner\'s business actions can bind the others.'),
        Q('Which business is most likely a sole proprietorship?', 'A single dog walker who never registered an entity',
          ('A company with an LLC certificate from the state', 'that is an LLC'),
          ('Three cofounders who filed incorporation papers', 'that is a corporation'),
          ('Two partners who formed an LLC together', 'that is an LLC'), 'One owner, no entity filed.'),
        Q('A sole proprietor has 2,000 dollars of business debt and 5,000 dollars of personal savings. If the business '
          'cannot pay, what could happen?', 'Creditors could seek payment from her personal savings.',
          ('The debt disappears because the business closed.', 'debts do not vanish that way'),
          ('Only 50 percent of the debt can ever be collected.', 'no such rule'),
          ('Savings are always protected from business debts.', 'not for a sole proprietor'),
          'Personal assets can be used to pay business debts.'),
        Q('Which step changes a sole proprietorship into a different structure?', 'Forming an entity, such as an LLC, with the state',
          ('Opening a business bank account in his own name at a local bank', 'helpful but does not create an entity'),
          ('Getting a logo designed', 'branding only'), ('Hiring a first customer', 'no legal change'),
          'A state filing creates a different entity.'),
    ]),
    F2=sec('Handle the complications: structure is not chosen by labels alone', SOLE, [
        Q('Two friends call their joint business "just a hobby" but share profits from regular sales. What should they '
          'understand?', 'The law may treat them as a partnership based on what they do',
          ('Calling it a hobby removes all legal responsibility', 'labels do not decide this'),
          ('Hobbies cannot have profits by law', 'not the rule'),
          ('They become an LLC by sharing profits', 'an LLC needs a filing'),
          'Structure can depend on the actual arrangement, not the name they use.'),
        Q('A sole proprietor wants less personal risk but is unsure what to do. What is the best first step?',
          'Learn about other structures and ask an attorney or accountant', ('Change the business logo', 'no legal effect'),
          ('Stop keeping records', 'harmful'), ('Assume insurance is never needed for a small one-person business', 'risky assumption'),
          'Structure and insurance choices depend on facts; professional advice helps.'),
        Q('Which is MISSING from a two-person business plan with no entity? "We split profits 50/50 and both buy supplies."',
          'A written agreement about roles, decisions and debts', ('A third logo', 'not missing'),
          ('A larger supply budget', 'not the key gap'), ('A second social media account for posting photos of their work', 'not the key gap'),
          'Partners need a written agreement even without forming an entity.'),
        Q('A sole proprietor assumes local business licenses are not needed "because I am just one person." What should '
          'she check?', 'Her city, county and state license and permit requirements', ('Nothing, one-person businesses never need licenses', 'often false'),
          ('Only federal rules, since local rules never apply', 'local rules often apply'),
          ('Only whether her friends have licenses', 'not reliable'),
          'Licensing depends on the activity and location, not the number of owners.'),
        Q('Which statement is accurate?', 'Being simple to start does not make a sole proprietorship risk-free.',
          ('Simple structures like this have no legal responsibilities at all.', 'they do'),
          ('Sole proprietors cannot be sued.', 'they can'),
          ('Partnerships protect partners from all debts.', 'general partnerships usually do not'),
          'Simplicity and personal responsibility go together.'),
    ]))

# ------------------------------------------------------------------ Set 22: LLC and corporation
LLC = ('A LIMITED LIABILITY COMPANY (LLC) is a business entity formed by filing with a state. Its main feature is limited '
       'liability: generally, business debts and lawsuits are the company\'s, not the owners\' personal ones. A '
       'CORPORATION is also formed with the state; it is owned by shareholders and run with more formal rules. Both can '
       'help separate personal and business risk, but neither is total immunity: owners can still be personally '
       'responsible for their own wrongful acts, for personal guarantees they sign, or if they mix personal and business '
       'money. Source: SBA; state law varies.')

s22 = SET('ENT.LEGAL.04',
    M=sec('Describe LLCs and corporations and the limits of limited liability', LLC, [
        Q('How is an LLC created?', 'By filing with a state', ('Automatically when a business makes its first sale', 'that is a sole proprietorship'),
          ('By opening a business bank account', 'a bank account does not form an entity'),
          ('By buying a domain name with "LLC" in it', 'a domain does not form an entity'),
          'An LLC exists after a state filing.'),
        Q('What does "limited liability" generally mean?', 'Business debts are generally the company\'s, not the owners\'.',
          ('The owners can never be sued for anything at all.', 'not total immunity'),
          ('The business never has to pay any taxes.', 'unrelated to taxes'),
          ('The company can only earn a limited amount of money.', 'not what it means'),
          'Limited liability separates business debts from owners in general.'),
        Q('Which can still make an LLC owner personally responsible?', 'Signing a personal guarantee for a business loan',
          ('Choosing a business name with an LLC ending', 'naming does not create liability'),
          ('Paying the state filing fee on time', 'not a source of liability'),
          ('Using a logo on business cards', 'not a source of liability'),
          'A personal guarantee makes the owner personally responsible for that debt.'),
        Q('Who owns a corporation?', 'Its shareholders', ('Its customers', 'customers buy, not own'),
          ('The state that approved it', 'the state does not own it'),
          ('Its suppliers', 'suppliers sell to it'), 'Shareholders own corporations.'),
        Q('Which statement about LLCs is accurate?', 'An LLC is not total immunity from personal responsibility.',
          ('An LLC protects owners from every possible claim.', 'not true'),
          ('An LLC automatically lowers taxes for every owner.', 'not automatic'),
          ('An LLC means owners may mix personal and business money freely.', 'mixing can weaken protection'),
          'Protection has limits, such as guarantees and personal wrongful acts.'),
    ]),
    B=[cs('A wall with doors', 'Think of an LLC as a wall between the business and the owner\'s personal life. Most '
          'business debts stay on the business side. But the wall has doors that the owner can open: signing a personal '
          'guarantee, causing harm personally, or treating business money as personal money. Each of these can let '
          'business problems reach the owner. Forming an LLC builds the wall; careful habits keep the doors closed.', [
        Q('In this picture, what does forming an LLC do?', 'Builds a wall between business and personal life',
          ('Removes all business debts from existence at once', 'debts remain'), ('Guarantees profit', 'no'), ('Pays taxes automatically', 'no'),
          'The LLC creates separation.'),
        Q('Which is a "door" through the wall?', 'Signing a personal guarantee', ('Filing the LLC paperwork', 'that builds the wall'),
          ('Keeping separate bank accounts', 'keeps the door closed'), ('Using the LLC name on contracts', 'good practice'),
          'Personal guarantees bypass the wall.'),
        Q('Mixing business and personal money does what?', 'Can weaken the wall', ('Makes the wall stronger', 'no'),
          ('Has no effect at all', 'it can matter'), ('Creates a corporation', 'no'), 'Mixing money can undermine protection.'),
        Q('Do most ordinary business debts stay on the business side?', 'Generally, yes', ('Never', 'that is the point of the wall'),
          ('Only for corporations', 'LLCs too'), ('Only after five years', 'no'), 'That is the main feature.'),
        Q('What keeps the doors closed?', 'Careful habits, like separate accounts and not guaranteeing debts personally',
          ('Changing the logo often', 'no effect'), ('Posting about the business often on several social media accounts', 'no effect'),
          ('Ignoring contracts', 'risky'), 'Good habits protect the separation.'),
    ], why='A learner who misses MAIN may think limited liability is total protection; the wall-with-doors picture shows '
           'its limits.')],
    F1=sec('Apply it: what limited liability does in real situations', LLC, [
        Q('Lee\'s LLC owes a supplier 4,000 dollars and cannot pay. Lee signed nothing personally and kept money '
          'separate. Generally, whose debt is it?', 'The LLC\'s debt', ('Lee\'s personal debt automatically', 'not without more'),
          ('The supplier\'s own debt', 'the supplier is owed'), ('The state\'s debt', 'no'),
          'With separation maintained and no guarantee, the debt is generally the company\'s.'),
        Q('Same LLC, but Lee personally guaranteed a 10,000-dollar loan. If the LLC cannot repay, who may have to pay?',
          'Lee personally', ('Only the LLC, never Lee', 'the guarantee makes Lee responsible'),
          ('The bank absorbs the loss automatically', 'not automatically'), ('No one', 'someone owes it'),
          'A personal guarantee makes the owner personally responsible for that loan.'),
        Q('An LLC owner pays personal rent from the business account every month and records nothing. What risk does '
          'this create?', 'It can weaken the separation between owner and LLC', ('No risk; LLC money is the owner\'s to use any way', 'mixing is risky'),
          ('It turns the LLC into a corporation', 'no'), ('It lowers the owner\'s taxes automatically', 'no'),
          'Treating business money as personal can undermine limited liability.'),
        Q('Which business is a corporation?', 'One formed with the state that issues shares to owners',
          ('A single owner selling crafts at markets with no state filing at all', 'sole proprietorship'),
          ('Two friends sharing profits with no filing', 'partnership'),
          ('A brand name printed on a website', 'not an entity'), 'Corporations are formed with the state and have shareholders.'),
        Q('An LLC owner personally causes a car accident while driving for the business. What should the owner understand?',
          'Personal wrongful acts can create personal responsibility, and insurance matters.',
          ('The LLC always shields the owner from any claim about any accident at all.', 'not always'),
          ('Accidents are never a business concern.', 'they can be'),
          ('Only the other driver is ever responsible.', 'depends on facts'),
          'Limited liability does not erase responsibility for one\'s own wrongful acts.'),
    ]),
    F2=sec('Handle the complications: common LLC myths', LLC, [
        Q('A friend says, "Form an LLC and you can never be sued." What is wrong with this?',
          'People can still sue, and owners can still be responsible in some situations',
          ('Nothing is wrong, because LLC owners can never be sued for anything', 'false'),
          ('LLCs make lawsuits illegal', 'false'), ('Only corporations can be sued', 'false'),
          'An LLC limits some liability; it does not stop lawsuits.'),
        Q('A friend says, "An LLC automatically saves taxes." What should the owner check?',
          'How the LLC will be taxed and whether it actually changes her taxes', ('Nothing, because forming an LLC always saves taxes for its owners', 'not automatic'),
          ('Only the LLC\'s logo design', 'unrelated'), ('Whether the bank likes LLCs', 'unrelated'),
          'Tax effects depend on classification and facts; an accountant can help.'),
        Q('An owner forms an LLC but keeps signing contracts in her own name only. What risk might this create?',
          'She may be personally bound by those contracts', ('None; the LLC covers anything she signs', 'not necessarily'),
          ('The contracts become invalid automatically', 'not automatically'),
          ('The state will cancel the LLC immediately', 'not automatically'),
          'Signing as the LLC (with the LLC\'s name) helps keep obligations with the company.'),
        Q('Which detail should an owner verify before relying on LLC protection for a risky activity, such as running '
          'trampoline parties?', 'Insurance coverage and how liability works for that activity', ('Logo colors', 'unrelated'),
          ('The number of social media followers the business has gained', 'unrelated'), ('The domain renewal date', 'unrelated'),
          'Risky activities call for insurance and advice; the LLC is not enough alone.'),
        Q('Which statement is accurate?', 'An LLC can help, but it works best with separate money and careful signing.',
          ('An LLC replaces the need for insurance.', 'it does not'),
          ('An LLC means its owners can safely ignore the contracts they sign.', 'no'),
          ('An LLC is required for every business.', 'not required'),
          'Protection depends on maintaining separation and good practices.'),
    ]))

# ------------------------------------------------------------------ Set 23: legal form vs tax treatment
TAX = ('A business\'s LEGAL FORM (sole proprietorship, partnership, LLC, corporation) is set by state law. Its TAX '
       'TREATMENT is how the IRS taxes it, which is a separate question. An LLC is a good example. By default, for '
       'federal income tax, a single-owner LLC is usually taxed with its owner (the IRS calls it "disregarded"), and a '
       'multi-owner LLC is usually taxed as a partnership. An LLC can choose (elect) to be taxed as a corporation. So '
       '"LLC" tells you the legal form, not automatically how it is taxed. Source: IRS; check current rules.')

s23 = SET('ENT.LEGAL.05',
    M=sec('Separate legal form from tax treatment', TAX, [
        Q('Who sets a business\'s legal form?', 'State law, through the entity\'s formation', ('The IRS, by assigning it a tax form', 'the IRS sets tax treatment'),
          ('The bank, when it opens an account', 'banks do not set legal form'),
          ('Customers, by how they pay', 'unrelated'), 'Legal form comes from state law.'),
        Q('By default, a single-owner LLC is usually taxed how for federal income tax?', 'With its owner ("disregarded")',
          ('Always as a large corporation with shareholders', 'not by default'),
          ('Never taxed at all, since it is an LLC', 'income is still taxed'),
          ('As a partnership, even with one owner', 'partnerships need two or more'),
          'By default the single-owner LLC is disregarded and taxed with the owner.'),
        Q('By default, an LLC with three owners is usually taxed as what?', 'A partnership',
          ('A sole proprietorship', 'it has more than one owner'), ('A nonprofit', 'not by default'),
          ('A government agency', 'no'), 'Multi-owner LLCs default to partnership tax treatment.'),
        Q('Can an LLC choose to be taxed as a corporation?', 'Yes, by making an election',
          ('No, never, under any circumstance', 'an election is possible'),
          ('Only if it changes its name', 'naming is unrelated'), ('Only if it closes', 'no'),
          'An LLC can elect corporate tax treatment.'),
        Q('"My business is an LLC." What does this tell you for sure?', 'Its legal form', ('Exactly how it is taxed', 'not by itself'),
          ('How much tax it owes this year', 'not by itself'), ('That it pays no tax', 'not true'),
          '"LLC" names the legal form; tax treatment is separate.'),
    ]),
    B=[cs('Two different labels', 'Think of a student with two labels: the school they attend (set by enrollment) and the '
          'sports team they play on (set by tryouts). Knowing the school does not tell you the team. A business also has '
          'two labels: its legal form (set by state filings) and its tax treatment (set by IRS rules and elections). '
          'Knowing one does not automatically tell you the other.', [
        Q('A business\'s legal form is like a student\'s what?', 'School', ('Sports team', 'that is tax treatment'),
          ('Favorite food', 'unrelated'), ('Shoe size', 'unrelated'), 'Legal form is one label.'),
        Q('Tax treatment is like what?', 'The team, chosen separately', ('The school', 'that is legal form'),
          ('The bus route', 'unrelated'), ('The cafeteria lunch menu', 'unrelated'), 'Tax treatment is a separate label.'),
        Q('Does knowing the legal form always tell you the tax treatment?', 'No', ('Yes, always', 'they are separate'),
          ('Only for big companies', 'no'), ('Only in summer', 'no'), 'They are separate questions.'),
        Q('Who decides tax treatment rules?', 'Federal IRS rules and the business\'s elections',
          ('The state alone, with no federal rules applying at all', 'state sets legal form'), ('The bank', 'no'), ('Customers', 'no'),
          'Federal tax rules and elections decide tax treatment.'),
        Q('Which word means "choosing" a tax treatment?', 'Election', ('Formation', 'creating the entity'),
          ('Registration', 'filing with the state'), ('Reconciliation', 'matching records'), 'An election is a choice.'),
    ], why='A learner who misses MAIN may think "LLC" is a tax type; two separate labels make the distinction clear.')],
    F1=sec('Apply it: name the form and the tax treatment', TAX, [
        Q('Ana forms an LLC alone and makes no tax election. What are her legal form and default federal tax treatment?',
          'LLC; taxed with Ana as a disregarded entity', ('Corporation; taxed as a corporation', 'she formed an LLC'),
          ('Partnership; taxed as a partnership', 'she is the only owner'),
          ('Sole proprietorship; not taxed at all', 'income is taxed'),
          'Legal form LLC; default tax treatment disregarded (with the owner).'),
        Q('Ben and Cal form an LLC together with no election. What is the default federal tax treatment?', 'Partnership',
          ('Disregarded with Ben only', 'there are two owners'), ('Corporation automatically', 'not by default'),
          ('No tax ever', 'income is taxed'), 'Two-owner LLCs default to partnership treatment.'),
        Q('An LLC elected to be taxed as a corporation. What is its legal form now?', 'Still an LLC',
          ('A corporation under state law automatically', 'the election changes tax treatment, not state legal form'),
          ('A sole proprietorship', 'no'), ('A partnership', 'no'), 'The election changes tax treatment, not the state legal form.'),
        Q('A friend says, "LLCs pay a special LLC tax rate." What is the best response?',
          'Tax depends on how the LLC is classified, not on "LLC" alone', ('Yes, every LLC in the country pays one special LLC tax rate', 'not true'),
          ('LLCs never pay any tax', 'not true'), ('Only states tax LLCs', 'not true'),
          'There is no single "LLC tax"; treatment depends on classification.'),
        Q('Who is the best person to help decide whether an LLC should make a tax election?',
          'An accountant or tax professional', ('A web designer', 'not tax advice'),
          ('A sign printer', 'not tax advice'), ('A social media manager for the business', 'not tax advice'),
          'Elections have tax consequences; a tax professional can help.'),
    ]),
    F2=sec('Handle the complications: mixed-up assumptions', TAX, [
        Q('An owner thinks forming an LLC changed her tax forms automatically into corporate forms. What should she '
          'check?', 'Her LLC\'s tax classification and what returns it must file', ('Her logo\'s file format', 'unrelated'),
          ('Her domain renewal date', 'unrelated'), ('Her competitor\'s prices and the services they list online', 'unrelated'),
          'Tax filing depends on classification; she should confirm it.'),
        Q('Two owners disagree: one says their LLC is a partnership, the other says it is an LLC. What is the clearest '
          'way to put it?', 'Legally an LLC; by default taxed as a partnership', ('Only a partnership, not an LLC', 'it is an LLC'),
          ('Only an LLC, which has no tax treatment of any kind', 'it has a tax treatment'),
          ('Neither, since it has two owners', 'it is both, in different senses'),
          'Both are right in different senses: legal form versus tax treatment.'),
        Q('Rules about elections and deadlines can change. What is the sensible approach for a beginner?',
          'Check current IRS guidance or ask a tax professional before choosing', ('Rely on an old blog post', 'may be outdated'),
          ('Assume the rules never change and rely on what a friend did years ago', 'they can'), ('Ask a competitor', 'not reliable'),
          'Time-sensitive tax rules should be checked at the source.'),
        Q('Which statement is accurate?', 'A sole proprietorship and a single-owner LLC can both be taxed with the owner by default.',
          ('A single-owner LLC can never be taxed together with its owner under any rule.', 'that is its default'),
          ('Sole proprietorships are taxed as corporations.', 'not true'),
          ('All LLCs are taxed as corporations by default.', 'not true'),
          'Default treatment for a single-owner LLC is like a sole proprietor for income tax.'),
        Q('Which information is needed to know how an LLC is taxed?', 'Its number of owners and whether it made an election',
          ('Its logo and slogan', 'unrelated'), ('Its website color scheme', 'unrelated'),
          ('Its number of social media followers and likes', 'unrelated'), 'Owners and elections decide default and chosen treatment.'),
    ]))

SETS = [s19, s20, s21, s22, s23]
