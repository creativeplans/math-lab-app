"""Source ledger for the Entrepreneurship collection.

Every time-sensitive or historical claim used in the course is listed here with the URL that supports it, the claim,
the date it was checked, the jurisdiction and how it was checked. Official pages could not be opened directly from the
authoring environment (the network blocks those hosts); each claim was checked against the official page as returned
by a web search (title, URL and quoted text), and where the search also returned secondary sources that disagreed,
the course avoids the disputed detail. Review every entry before its review date.
"""
CHECKED = '2026-10-25'
METHOD = 'web search result for the official page (quoted text); page not opened directly'

SRC = {
    # ---------------------------------------------------------------- federal (US) official guidance
    'irs_ein': dict(
        url='https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number',
        claim='An EIN can be obtained directly from the IRS for free ("you never have to pay a fee for an EIN"); '
              'if forming an LLC, partnership or corporation, form the entity with the state first or the EIN '
              'application may be delayed.',
        jurisdiction='US federal', review_days=365),
    'irs_ein_online': dict(
        url='https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online',
        claim='The online application names a "responsible party" (an individual who controls the business) with an SSN '
              'or ITIN, is for businesses located in the US or its territories, and must be completed in one session.',
        jurisdiction='US federal', review_days=365),
    'irs_llc': dict(
        url='https://www.irs.gov/node/7774',
        claim='For federal income tax, a single-member LLC is by default disregarded (taxed with its owner) and a '
              'multi-member LLC is by default a partnership; an LLC can elect to be taxed as a corporation.',
        jurisdiction='US federal', review_days=365),
    'irs_records': dict(
        url='https://www.irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records',
        claim='Keep records that support income, deductions or credits until the period of limitations for that return '
              'runs out; generally 3 years, with longer periods in some situations.',
        jurisdiction='US federal', review_days=365),
    'irs_se': dict(
        url='https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes',
        claim='Self-employed people generally pay self-employment tax (Social Security and Medicare) on net earnings, and '
              'may need to make estimated tax payments during the year. The course teaches the idea only; rates and '
              'thresholds change and are not taught as current figures.',
        jurisdiction='US federal', review_days=365, effective_year='check the current tax year'),
    'irs_estimated': dict(
        url='https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes',
        claim='Tax is pay-as-you-go: people who do not have enough tax withheld, such as many self-employed people, may '
              'need to pay estimated tax in installments during the year.',
        jurisdiction='US federal', review_days=365),
    'sba_structure': dict(
        url='https://www.sba.gov/business-guide/launch-your-business/choose-business-structure',
        claim='A sole proprietorship is not a separate legal entity, so the owner can be held responsible for business '
              'debts; an LLC or corporation generally separates owners from business liability; the structure affects '
              'taxes and liability, and the SBA suggests talking with an attorney or accountant.',
        jurisdiction='US (state law varies)', review_days=365),
    'sba_launch': dict(
        url='https://www.sba.gov/business-guide/launch-your-business',
        claim='The SBA lists the launch steps (choose a structure, register, get federal and state tax IDs, apply for '
              'licenses and permits, open a business bank account, get insurance) as a general guide.',
        jurisdiction='US', review_days=365),
    'sba_counsel': dict(
        url='https://www.score.org/score-faqs-business-mentoring-resources-support/',
        claim='SCORE is an SBA resource partner offering free volunteer mentoring (some workshops charge fees); Small '
              'Business Development Centers (SBDCs) offer free or low-cost consulting through host institutions.',
        jurisdiction='US', review_days=365),
    'usps_pobox': dict(
        url='https://postalpro.usps.com/mailing/competitivepoboxes',
        claim='At participating Post Offices, the PO Box "Street Addressing" option lets a box holder use the Post '
              'Office street address with the box number, so private carriers that need a street address can deliver; '
              'availability varies by location and the customer signs an agreement.',
        jurisdiction='US (USPS)', review_days=365),
    'usps_1583': dict(
        url='https://www.usps.com/manage/forms-publications.htm',
        claim='A private mailbox at a Commercial Mail Receiving Agency (CMRA) requires USPS Form 1583 and identity '
              'documents so the agency may receive mail for the customer. Requirements (for example notarization) '
              'have changed; check the current form and the provider.',
        jurisdiction='US (USPS)', review_days=365),
    'state_agent': dict(
        url='https://sos.wa.gov/corporations-charities/frequently-asked-questions-faqs/what-addresses-use-when-filing',
        claim='Example of a state rule (Washington): the registered agent address must be a physical street address in '
              'the state where the agent can accept service; PO Boxes and private or virtual mailboxes may not be used '
              'for it, though a PO Box may be listed as a separate mailing address. Other states have their own rules.',
        jurisdiction='Washington State (example only)', review_days=365),
    'ftc_endorse': dict(
        url='https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking',
        claim='If an endorser has been paid or given something of value, that connection should be disclosed clearly; '
              'a platform\'s built-in disclosure tool is not automatically enough.',
        jurisdiction='US federal', review_days=365),
    'ftc_reviews': dict(
        url='https://www.ftc.gov/legal-library/browse/rules/rule-use-consumer-reviews-testimonials',
        claim='Fake or AI-generated reviews and testimonials that misrepresent real experiences are deceptive; the FTC '
              'has rules and guidance against fake reviews. The course teaches the principle (do not invent or buy '
              'reviews), not the rule\'s penalty details.',
        jurisdiction='US federal', review_days=365),
    'ftc_canspam': dict(
        url='https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business',
        claim='Commercial email must tell recipients how to opt out, honor opt-out requests, include a valid physical '
              'postal address (which may be a registered PO Box or private mailbox), and not use misleading headers '
              'or subject lines; the law covers business-to-business email too.',
        jurisdiction='US federal', review_days=365),
    'dol_contractor': dict(
        url='https://www.dol.gov/agencies/whd/flsa/misclassification',
        claim='Whether a worker is an employee or an independent contractor depends on the actual working relationship '
              '(economic reality), not on the label in a contract; the federal rule has changed several times since '
              '2021 and states may use stricter tests, so current federal and state rules must be checked.',
        jurisdiction='US federal and states', review_days=180),
    'uspto_name': dict(
        url='https://www.uspto.gov/trademarks/basics',
        claim='Registering a business name with a state, a DBA, or a domain name is not the same as trademark rights; '
              'trademark protection is a separate process.',
        jurisdiction='US', review_days=365),
    'youtube_ypp': dict(
        url='https://support.google.com/youtube/answer/72851',
        claim='Earning ad revenue on YouTube requires joining the YouTube Partner Program, which has eligibility '
              'thresholds and policies separate from simply posting videos; the thresholds have changed and should '
              'be checked in the official help page. The course does not teach the numbers.',
        jurisdiction='Platform policy (worldwide, varies by country)', review_days=180),
    'chargeback': dict(
        url='https://www.consumerfinance.gov/ask-cfpb/how-do-i-dispute-a-charge-on-my-credit-card-bill-en-61/',
        claim='Card customers can dispute charges with their card issuer; the merchant may lose the payment and pay a '
              'fee, and can respond with evidence by the deadline on the dispute notice (deadlines depend on the card '
              'network and reason).',
        jurisdiction='US', review_days=365),

    # ---------------------------------------------------------------- founder and company histories
    'case_benjerry': dict(
        url='https://www.history.com/this-day-in-history/may-5/ben-jerry-open-their-first-ice-cream-shop',
        claim='Ben Cohen and Jerry Greenfield took a $5 correspondence course in ice cream making from Penn State and '
              'opened their first shop in a renovated gas station in Burlington, Vermont, in 1978; they had first '
              'considered bagels but found the equipment too expensive.',
        corroboration='https://www.cnbc.com/2019/08/01/ben-and-jerrys-founders-started-out-by-taking-a-5-dollar-ice-cream-class.html',
        jurisdiction='history', review_days=1095),
    'case_spanx': dict(
        url='https://www.gsb.stanford.edu/insights/sara-blakely-start-small-think-big-scale-fast',
        claim='Sara Blakely cut the feet off control-top pantyhose to wear under white pants, started Spanx in 2000 with '
              '$5,000 of her savings, was turned down by hosiery manufacturers before one agreed, and got the product '
              'into Neiman Marcus.',
        corroboration='https://en.wikipedia.org/wiki/Sara_Blakely',
        jurisdiction='history', review_days=1095),
    'case_zappos': dict(
        url='https://fortune.com/2012/09/05/nick-swinmurn-zappos-silent-founder/',
        claim='Zappos founder Nick Swinmurn tested online shoe sales by photographing shoes in local stores and, when an '
              'order came in, buying the pair from the store and shipping it, before holding inventory.',
        corroboration='https://www.referenceforbusiness.com/history2/90/Zappos-com-Inc.html',
        jurisdiction='history', review_days=1095),
    'case_dropbox': dict(
        url='https://www.alexanderjarvis.com/dropbox-doing-things-that-dont-scale/',
        claim='Before the product was ready for the public, Drew Houston posted a short demo video of Dropbox with a sign-up '
              'form for a beta waiting list, and the waiting list grew sharply after the video was shared online.',
        corroboration='Houston interview transcript (Y Combinator); exact counts and dates differ between accounts, so the '
                      'course uses no numbers',
        jurisdiction='history', review_days=1095),
    'case_hp': dict(
        url='https://www.hp.com/hpinfo/abouthp/histnfacts/timeline/hist_30s.html',
        claim='Bill Hewlett and Dave Packard began part-time work in a garage in Palo Alto with $538 in working capital; '
              'their first product was the HP 200A audio oscillator for testing sound equipment; Walt Disney Studios '
              'asked for changes and ordered eight of the modified model (200B) for the film Fantasia.',
        corroboration='https://www.agilent.com/about/companyinfo/history/timeline_1930s.html',
        jurisdiction='history', review_days=1095),
    'case_amazon': dict(
        url='https://historylink.org/File/23230',
        claim='Amazon.com launched in July 1995 as an online bookstore, started from a rented house in Bellevue, '
              'Washington; Jeff Bezos chose books from a short list of products because of the huge number of titles '
              'in print and broad demand.',
        corroboration='https://en.wikipedia.org/wiki/History_of_Amazon',
        jurisdiction='history', review_days=1095),
    'case_nike': dict(
        url='https://www.britannica.com/biography/Phil-Knight',  # returned by search
        claim='Phil Knight and his former coach Bill Bowerman formed Blue Ribbon Sports in 1964 to distribute Onitsuka '
              'Tiger running shoes from Japan; Knight sold shoes from his car at regional track meets while working '
              'other jobs; the company became Nike after splitting from Onitsuka in 1971.',
        jurisdiction='history', review_days=1095),
    'case_walker': dict(
        url='https://www.indianahistory.org/wp-content/uploads/Madam-Walker-Essay.pdf',
        claim='Madam C. J. Walker sold her hair-care products door to door, advertised in African American newspapers, '
              'trained and recruited sales agents, ran a mail-order business and beauty school, and incorporated her '
              'company in Indianapolis in 1910.',
        corroboration='https://64parishes.org/entry/madam-c-j-walker',
        jurisdiction='history', review_days=1095),
    'case_wrigley': dict(
        url='https://www.britannica.com/biography/William-Wrigley-Jr',
        claim='William Wrigley Jr. moved to Chicago in 1891 selling soap and offered baking powder as a premium; baking '
              'powder proved more popular, he switched to it and offered chewing gum as a premium; the gum proved more '
              'popular and he turned to selling chewing gum. (Exact years of each switch differ between sources.)',
        corroboration='https://www.encyclopedia.com/books/politics-and-business-magazines/wm-wrigley-jr-company',
        jurisdiction='history', review_days=1095),
    'case_airbnb': dict(
        url='https://knowledge.wharton.upenn.edu/?p=16809',
        claim='In 2007 Brian Chesky and Joe Gebbia rented air mattresses in their San Francisco apartment to people '
              'attending a design conference when hotels were booked; the idea was first called AirBed & Breakfast, '
              'and Nathan Blecharczyk joined as a cofounder to build the website.',
        jurisdiction='history', review_days=1095),
    'case_microsoft': dict(
        url='https://www.computinghistory.org.uk/det/5946/MITS-licenses-Altair-BASIC-from-Bill-Gates-and-Paul-Allen/',
        claim='Bill Gates and Paul Allen wrote a BASIC interpreter for the MITS Altair 8800 computer in 1975, demonstrated '
              'it to MITS, and licensed it to MITS as Altair BASIC; this was Microsoft\'s first product.',
        jurisdiction='history', review_days=1095),
    'case_craigslist': dict(
        url='https://www.encyclopedia.com/books/politics-and-business-magazines/craigslist-inc',
        claim='Craig Newmark began emailing San Francisco event notices to friends in 1995; people asked to join and '
              'started posting other things such as jobs and apartments; the list moved to the web and was incorporated '
              'as a company in 1999.',
        corroboration='https://en.wikipedia.org/wiki/Craig_Newmark',
        jurisdiction='history', review_days=1095),
}


UNCONFIRMED = {'irs_se': 'official URL not returned by search; claim confirmed only by secondary sources (rates and thresholds deliberately not taught)', 'irs_estimated': 'official URL not returned by search; concept confirmed by secondary sources', 'ftc_endorse': 'claim confirmed through law-firm summaries of the 2023 Endorsement Guides; official FAQ URL not returned by search', 'ftc_reviews': 'final rule status not confirmed by search (search found the 2023 proposal); course teaches only the principle', 'dol_contractor': 'confirmed through law-firm summaries (DLA Piper, Polsinelli, 2025-2026); official URL not returned by search', 'uspto_name': 'confirmed through filing-service and law-firm sources; official USPTO URL not returned by search', 'chargeback': 'confirmed through payment-industry explainers; CFPB URL not returned by search', 'usps_1583': 'confirmed through mailbox-provider sources only; notarization requirement disputed between sources', 'sba_counsel': 'SCORE FAQ returned by search; SBDC description from SCORE chapter pages'}


def entry(key):
    e = dict(SRC[key])
    e.setdefault('checked', CHECKED)
    e.setdefault('method', METHOD)
    e['id'] = key
    e['confirmed_by_search'] = key not in UNCONFIRMED
    if key in UNCONFIRMED:
        e['note'] = UNCONFIRMED[key]
    return e
