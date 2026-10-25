"""Coverage plan for the Entrepreneurship collection (course "entrepreneurship", Adults & HS Students, prefix ENT).

One row per focused set, in the order a learner meets them. Set numbers are assigned in this order and never reused.
Row: (outcome code, set title, outcome title, module id, path references, required outcome codes, sources)
  path references: the paths a SHARED skill serves (the set is authored once and listed for each path); [] = all
  required: only prerequisites the set truly needs (suggested reading is listed separately in SUGGESTED)
  sources: keys in sources.SRC; a set with sources is "time_sensitive", otherwise "stable"
"""

PATHS = [
    dict(id='services', title='Services, freelancing & local businesses',
         description='Selling your time and skill: tutoring, cleaning, lawn care, repair, design, bookkeeping help.'),
    dict(id='products', title='Physical products & e-commerce',
         description='Making or buying things and selling them in person or online, including shipping and returns.'),
    dict(id='digital', title='Digital products, software & AI-assisted businesses',
         description='Templates, courses, apps and online tools: access, support, updates and recurring costs.'),
    dict(id='content', title='Content creation & social-media businesses',
         description='Videos, posts, podcasts and newsletters earning from sponsors, affiliates, platforms or products.'),
]

MODULES = [
    # id, title, kind, paths, description
    ('start', 'Foundation 1: Start here', 'foundation', [], 'What a business is, and four common ways to sell.'),
    ('customers', 'Foundation 2: Customers and offers', 'foundation', [], 'Who has the problem, who pays, what you offer.'),
    ('testing', 'Foundation 3: Testing demand', 'foundation', [], 'Finding evidence before spending a lot.'),
    ('legal', 'Foundation 4: Names and legal structure', 'foundation', [], 'Names, business types, filings, permits.'),
    ('ids', 'Foundation 5: EIN and business banking', 'foundation', [], 'Tax ID numbers and separate business money.'),
    ('mail', 'Foundation 6: Addresses and contact details', 'foundation', [], 'Mail, addresses, email and phone.'),
    ('money', 'Foundation 7: Costs, pricing and cash', 'foundation', [], 'Costs, prices, profit and cash timing.'),
    ('books', 'Foundation 8: Bookkeeping and taxes', 'foundation', [], 'Records, reports and tax ideas for beginners.'),
    ('paid', 'Foundation 9: Selling and getting paid', 'foundation', [], 'Quotes, invoices, refunds, disputes and scams.'),
    ('web', 'Foundation 10: Website essentials', 'foundation', [], 'A clear, working, measurable website.'),
    ('marketing', 'Foundation 11: Marketing, sales and social media', 'foundation', [],
     'Channels, permission, reviews, ads and measuring results.'),
    ('ai', 'Foundation 12: AI as a practical helper', 'foundation', [], 'Using AI tools carefully and checking the work.'),
    ('ops', 'Foundation 13: Operations and overlooked admin', 'foundation', [],
     'Procedures, accounts, security, records and deadlines.'),
    ('risk', 'Foundation 14: Insurance, contracts and risk', 'foundation', [], 'Spotting risks and what to check.'),
    ('help', 'Foundation 15: Help, delegation and partners', 'foundation', [], 'Hiring help, partners and advisors.'),
    ('growth', 'Funding, growth and limits', 'specialty', [], 'Paying for the business and growing it carefully.'),
    ('services', 'Path: services, freelancing & local businesses', 'path', ['services'], 'Estimating, scheduling, scope.'),
    ('products', 'Path: physical products & e-commerce', 'path', ['products'], 'Suppliers, packaging, returns.'),
    ('digital', 'Path: digital products & software', 'path', ['digital'], 'Access, support, licensing, costs.'),
    ('content', 'Path: content creation & social media', 'path', ['content'], 'Rights, sponsors, platforms, trust.'),
]

A = []  # all paths
SV, PR, DG, CT = ['services'], ['products'], ['digital'], ['content']

ROWS = [
    # ---------------------------------------------------------------- Foundation 1: Start here
    ('ENT.START.01', 'What a business is', 'Describe a business as solving a problem for customers who pay, and tell '
     'revenue-seeking activity from a hobby', 'start', A, [], []),
    ('ENT.START.02', 'Side business or full-time business', 'Compare a side business with a full-time business by time, '
     'income needs and risk', 'start', A, ['ENT.START.01'], []),
    ('ENT.START.03', 'Four ways to sell: services, products, digital, content', 'Classify a business idea as a service, '
     'physical product, digital product or content business, and name what each needs', 'start', A, ['ENT.START.01'], []),
    ('ENT.CASE.01', 'Founder case: Ben & Jerry\'s starts small', 'Apply a documented early decision (learning a skill '
     'cheaply and starting with one small shop) to a new small business', 'start', ['products', 'services'],
     ['ENT.START.01'], ['case_benjerry']),
    # ---------------------------------------------------------------- Foundation 2: Customers and offers
    ('ENT.CUST.01', 'Finding a real customer problem', 'Identify a specific, frequent problem that someone already '
     'spends time or money on', 'customers', A, ['ENT.START.01'], []),
    ('ENT.CUST.02', 'Naming a specific customer', 'Describe a specific customer group instead of "everyone"',
     'customers', A, ['ENT.CUST.01'], []),
    ('ENT.CUST.03', 'Writing a clear offer', 'Write an offer (value proposition) that says who it is for, the problem '
     'and the result', 'customers', A, ['ENT.CUST.02'], []),
    ('ENT.CUST.04', 'Customer or user: who pays?', 'Tell the paying customer from the user and the decision-maker',
     'customers', A, ['ENT.CUST.02'], []),
    ('ENT.CASE.02', 'Founder case: Spanx and a problem the founder had', 'Apply a documented early decision (solving a '
     'problem you have and checking that others share it) to a new business', 'customers', ['products'],
     ['ENT.CUST.01'], ['case_spanx']),
    # ---------------------------------------------------------------- Foundation 3: Testing demand
    ('ENT.TEST.01', 'Customer interviews about past behavior', 'Plan interview questions about what people already do '
     'rather than what they say they would do', 'testing', A, ['ENT.CUST.02'], []),
    ('ENT.TEST.02', 'Avoiding leading questions', 'Recognize and rewrite leading or yes-pushing interview questions',
     'testing', A, ['ENT.TEST.01'], []),
    ('ENT.TEST.03', 'Competitors and alternatives', 'Identify direct competitors and the other ways customers solve the '
     'problem today', 'testing', A, ['ENT.CUST.01'], []),
    ('ENT.TEST.04', 'Testing a small version first', 'Choose a small, cheap test that answers one question about '
     'demand', 'testing', A, ['ENT.CUST.03'], []),
    ('ENT.TEST.05', 'Evidence of willingness to pay', 'Rank evidence of demand, with payments and pre-orders above '
     'opinions', 'testing', A, ['ENT.TEST.04'], []),
    ('ENT.TEST.06', 'Likes and praise are not demand', 'Explain why likes, follows and compliments are weak demand '
     'signals', 'testing', A, ['ENT.TEST.05'], []),
    ('ENT.TEST.07', 'Continue, change or stop', 'Decide from stated test results whether to continue, change or stop '
     'an idea', 'testing', A, ['ENT.TEST.05'], []),
    ('ENT.CASE.03', 'Founder case: Zappos tests before buying stock', 'Apply a documented test (selling before holding '
     'inventory) to a new product idea, and see its limits', 'testing', ['products'], ['ENT.TEST.04'], ['case_zappos', 'copyright_fairuse', 'usc_109']),
    ('ENT.CASE.04', 'Founder case: Dropbox shows a demo first', 'Apply a documented test (a demo with a sign-up list) '
     'and tell sign-ups from paying customers', 'testing', ['digital'], ['ENT.TEST.04'], ['case_dropbox']),
    # ---------------------------------------------------------------- Foundation 4: Names and legal structure
    ('ENT.LEGAL.01', 'Business name, legal entity and brand', 'Tell a business name, a legal entity and a brand apart',
     'legal', A, ['ENT.START.01'], []),
    ('ENT.LEGAL.02', 'Name and domain checks are not trademark rights', 'Explain that a free domain or state name '
     'approval does not grant trademark rights, and what to check', 'legal', A, ['ENT.LEGAL.01'], ['uspto_name']),
    ('ENT.LEGAL.03', 'Sole proprietorships and partnerships', 'Describe sole proprietorships and general partnerships, '
     'including personal responsibility for debts', 'legal', A, ['ENT.LEGAL.01'], ['sba_structure']),
    ('ENT.LEGAL.04', 'LLCs and corporations', 'Describe LLCs and corporations at a basic level, including what limited '
     'liability does and does not do', 'legal', A, ['ENT.LEGAL.03'], ['sba_structure']),
    ('ENT.LEGAL.05', 'Legal structure versus tax treatment', 'Separate an entity\'s legal form from how it is taxed',
     'legal', A, ['ENT.LEGAL.04'], ['irs_llc']),
    ('ENT.LEGAL.06', 'Forming an LLC: state filing and registered agent', 'Order the conceptual steps of forming an '
     'LLC and explain the registered agent\'s role', 'legal', A, ['ENT.LEGAL.04'], ['sba_launch', 'state_agent']),
    ('ENT.LEGAL.07', 'Operating agreements and multiple owners', 'Identify what a written agreement among owners should '
     'cover', 'legal', A, ['ENT.LEGAL.06'], []),
    ('ENT.LEGAL.08', 'DBA (trade name) filings', 'Explain when a trade name (DBA) filing is used and what it does not '
     'do', 'legal', A, ['ENT.LEGAL.01'], ['uspto_name']),
    ('ENT.LEGAL.09', 'Liability limits and personal guarantees', 'Recognize how personal guarantees and personal '
     'actions can bypass limited liability', 'legal', A, ['ENT.LEGAL.04'], ['sba_structure']),
    ('ENT.LEGAL.10', 'Licenses, permits, zoning and home businesses', 'Identify which local, state or industry permissions '
     'to check for an activity and location', 'legal', A, ['ENT.START.03'], ['sba_launch']),
    ('ENT.LEGAL.11', 'When a professional helps', 'Decide when a question needs an attorney, accountant or other '
     'professional, and prepare for the meeting', 'legal', A, ['ENT.LEGAL.04'], ['sba_structure']),
    # ---------------------------------------------------------------- Foundation 5: EIN and banking
    ('ENT.ID.01', 'What an EIN is', 'Explain what an Employer Identification Number (EIN) is for and when to check '
     'whether one is needed', 'ids', A, ['ENT.LEGAL.03'], ['irs_ein']),
    ('ENT.ID.02', 'Applying from the official source', 'Recognize the official free EIN application and unnecessary '
     'third-party charges', 'ids', A, ['ENT.ID.01'], ['irs_ein', 'irs_ein_online']),
    ('ENT.ID.03', 'EIN, state tax ID and registration', 'Tell an EIN, a state tax account and a business registration '
     'apart, and their usual order', 'ids', A, ['ENT.ID.01', 'ENT.LEGAL.06'], ['irs_ein', 'sba_launch']),
    ('ENT.BANK.01', 'A separate business bank account', 'Explain why business money belongs in a separate account',
     'ids', A, ['ENT.START.01'], ['sba_launch']),
    ('ENT.BANK.02', 'Opening the account: documents, fees, signers', 'Identify documents a bank may ask for, account fees '
     'and who may sign', 'ids', A, ['ENT.BANK.01'], ['sba_launch']),
    ('ENT.BANK.03', 'Debit, credit and payment processing', 'Tell debit cards, credit cards and payment processors '
     'apart, including when money arrives', 'ids', A, ['ENT.BANK.01'], []),
    ('ENT.BANK.04', 'Moving money between owner and business', 'Record owner contributions and owner withdrawals '
     'separately from sales and expenses', 'ids', A, ['ENT.BANK.01'], []),
    ('ENT.BANK.05', 'Reconciling transactions', 'Match business records against the bank statement and explain '
     'differences', 'ids', A, ['ENT.BANK.01'], []),
    # ---------------------------------------------------------------- Foundation 6: Addresses and contact
    ('ENT.MAIL.01', 'Three kinds of business address', 'Tell a mailing address, a physical business address and a '
     'registered-agent address apart', 'mail', A, ['ENT.LEGAL.06'], ['state_agent']),
    ('ENT.MAIL.02', 'PO Boxes, private mailboxes and street addressing', 'Compare a PO Box, a private mailbox and the '
     'PO Box street-addressing option', 'mail', A, ['ENT.MAIL.01'], ['usps_pobox', 'usps_1583']),
    ('ENT.MAIL.03', 'Which address each organization accepts', 'Check which address a bank, state, platform or carrier '
     'will accept instead of assuming they are interchangeable', 'mail', A, ['ENT.MAIL.02'],
     ['usps_pobox', 'state_agent']),
    ('ENT.MAIL.04', 'Mailbox practicalities', 'Plan pickup access, forwarding or scanning, renewals and important '
     'notices for a business mailbox', 'mail', A, ['ENT.MAIL.02'], ['usps_pobox']),
    ('ENT.MAIL.05', 'Business email, phone and voicemail', 'Separate business contact channels from personal ones and '
     'keep them reachable', 'mail', A, ['ENT.START.01'], []),
    # ---------------------------------------------------------------- Foundation 7: Costs, pricing and cash
    ('ENT.COST.01', 'One-time and recurring costs', 'Classify costs as one-time or recurring', 'money', A,
     ['ENT.START.01'], []),
    ('ENT.COST.02', 'Fixed and variable costs', 'Classify costs as fixed or variable and use them in a small total',
     'money', A, ['ENT.COST.01'], []),
    ('ENT.COST.03', 'A realistic startup budget', 'Build a small startup budget with a buffer and no missing items',
     'money', A, ['ENT.COST.02'], []),
    ('ENT.PRICE.01', 'Price and cost per item', 'Find cost per item and profit per item from a stated price', 'money', A,
     ['ENT.COST.02'], []),
    ('ENT.CASH.01', 'Revenue, profit and cash', 'Tell revenue, profit and cash available apart in a small example',
     'money', A, ['ENT.PRICE.01'], []),
    ('ENT.PRICE.02', 'Markup and margin', 'Compute markup and margin and explain why they differ', 'money', A,
     ['ENT.PRICE.01'], []),
    ('ENT.PRICE.03', 'Break-even with stated assumptions', 'Find a break-even quantity from fixed costs and profit per '
     'item', 'money', A, ['ENT.PRICE.01', 'ENT.COST.02'], []),
    ('ENT.PRICE.04', 'Payment-processing fees', 'Include a stated processing fee when finding what a sale brings in',
     'money', A, ['ENT.PRICE.01'], []),
    ('ENT.PRICE.05', 'Refunds and discounts', 'Find the effect of refunds and discounts on revenue and profit', 'money',
     A, ['ENT.PRICE.01'], []),
    ('ENT.PRICE.06', 'Owner time and capacity', 'Include the owner\'s time and limited capacity when judging a price',
     'money', A, ['ENT.PRICE.01'], []),
    ('ENT.PRICE.07', 'Reviewing and raising prices', 'Decide when a price needs review from stated costs, demand and '
     'capacity, and communicate a change', 'money', A, ['ENT.PRICE.06'], []),
    ('ENT.CASH.02', 'Cash timing, unpaid invoices and deposits', 'Track when cash actually arrives and leaves, and use '
     'deposits', 'money', A, ['ENT.CASH.01'], []),
    ('ENT.CASH.03', 'A simple cash reserve', 'Size a simple cash reserve from stated monthly costs', 'money', A,
     ['ENT.CASH.02'], []),
    ('ENT.CASE.05', 'Founder case: HP\'s first product and first big customer', 'Apply a documented early decision '
     '(a customer asking for changes and placing an order) to a new business', 'money', ['products'],
     ['ENT.CUST.04'], ['case_hp']),
    # ---------------------------------------------------------------- Foundation 8: Bookkeeping and taxes
    ('ENT.BOOK.01', 'Why bookkeeping and receipts matter', 'Explain what bookkeeping is for and keep usable receipts',
     'books', A, ['ENT.BANK.01'], []),
    ('ENT.BOOK.02', 'Categorizing and a simple ledger', 'Record transactions in a simple ledger with sensible categories',
     'books', A, ['ENT.BOOK.01'], []),
    ('ENT.BOOK.03', 'Invoices, bills, money owed to you and by you', 'Tell invoices from bills and accounts receivable '
     'from accounts payable', 'books', A, ['ENT.BOOK.02'], []),
    ('ENT.BOOK.04', 'Owner contributions and draws in the books', 'Keep owner money moves out of sales and expenses '
     'in the records', 'books', A, ['ENT.BANK.04'], []),
    ('ENT.BOOK.05', 'Cash and accrual basics', 'Tell cash-basis from accrual-basis recording in a simple example',
     'books', A, ['ENT.BOOK.03'], []),
    ('ENT.BOOK.06', 'Profit and loss, balance sheet, cash flow', 'Tell what a profit-and-loss statement, balance sheet '
     'and cash-flow summary each show', 'books', A, ['ENT.BOOK.02'], []),
    ('ENT.TAX.01', 'Deductions versus credits', 'Tell a tax deduction from a tax credit, and explain that a deduction '
     'does not make a purchase free', 'books', A, ['ENT.BOOK.02'], ['irs_credits']),
    ('ENT.TAX.02', 'Business use versus personal use', 'Separate business and personal use of an item or account',
     'books', A, ['ENT.TAX.01'], []),
    ('ENT.TAX.03', 'Sales tax versus income tax', 'Tell sales tax (collected from customers where required) from income '
     'tax (on profit)', 'books', A, ['ENT.CASH.01'], ['sba_launch']),
    ('ENT.TAX.04', 'Self-employment tax and estimated payments', 'Explain the ideas of self-employment tax and paying '
     'estimated tax during the year', 'books', A, ['ENT.TAX.03'], ['irs_se', 'irs_estimated']),
    ('ENT.TAX.05', 'Setting money aside for taxes', 'Set aside a stated share of profit for taxes using an assumed rate',
     'books', A, ['ENT.TAX.04'], ['irs_estimated']),
    ('ENT.TAX.06', 'Records, tax forms and professional help', 'Keep records for the needed period, recognize payment-'
     'reporting forms as a concept, and know when to ask a tax professional', 'books', A, ['ENT.BOOK.01'],
     ['irs_records']),
    # ---------------------------------------------------------------- Foundation 9: Selling and getting paid
    ('ENT.PAY.01', 'Quotes and proposals', 'Write or judge a quote that states the work, price and what is not '
     'included', 'paid', A, ['ENT.PRICE.01'], []),
    ('ENT.PAY.02', 'Invoices, payment terms and deposits', 'Read and set payment terms, due dates and deposits',
     'paid', A, ['ENT.PAY.01'], []),
    ('ENT.PAY.03', 'Cancellations, refunds and expectations', 'Write clear cancellation and refund terms and apply them '
     'consistently', 'paid', A, ['ENT.PAY.02'], []),
    ('ENT.PAY.04', 'Scope changes', 'Handle a request for extra work with a written change and new price', 'paid', A,
     ['ENT.PAY.01'], []),
    ('ENT.PAY.05', 'Subscriptions and recurring billing', 'Explain recurring billing terms customers need to see and how '
     'cancellations work', 'paid', A, ['ENT.PAY.02'], []),
    ('ENT.PAY.06', 'Chargebacks and payment disputes', 'Explain a chargeback and gather evidence to respond',
     'paid', A, ['ENT.BANK.03'], ['chargeback', 'stripe_disputes']),
    ('ENT.PAY.07', 'Invoice and payment scams', 'Spot fraud signals in invoices, overpayments and changed payment '
     'details', 'paid', A, ['ENT.PAY.02'], ['ftc_fakecheck']),
    ('ENT.PAY.08', 'Supplier terms and communicating delays', 'Read supplier terms and tell customers about delays early '
     'and honestly', 'paid', A, ['ENT.PAY.02'], []),
    # ---------------------------------------------------------------- Foundation 10: Website essentials
    ('ENT.WEB.01', 'A clear offer and next action', 'Make a page say what is offered, for whom and what to do next',
     'web', A, ['ENT.CUST.03'], []),
    ('ENT.WEB.02', 'Trust signals, pricing, FAQ and policies', 'Choose truthful trust signals and the policies and '
     'answers a visitor needs', 'web', A, ['ENT.WEB.01'], []),
    ('ENT.WEB.03', 'Readable on phones, accessible forms', 'Make pages readable on phones and forms usable by more people',
     'web', A, ['ENT.WEB.01'], []),
    ('ENT.WEB.04', 'Domain, hosting and builders: who owns what', 'Tell a domain, hosting and a website builder apart, '
     'and keep ownership, renewals and recovery access', 'web', A, ['ENT.WEB.01'], []),
    ('ENT.WEB.05', 'HTTPS, testing and backups', 'Check HTTPS, test links, forms and checkout, and keep backups', 'web',
     A, ['ENT.WEB.04'], ['chromium_lock']),
    ('ENT.WEB.06', 'Search visibility basics', 'Improve how search engines and people understand a page, without '
     'promised rankings', 'web', A, ['ENT.WEB.01'], []),
    ('ENT.WEB.07', 'Measuring useful actions', 'Choose measures that match a site\'s goal, such as inquiries or sales',
     'web', A, ['ENT.WEB.01'], []),
    ('ENT.CASE.06', 'Founder case: Amazon starts with books', 'Apply a documented early decision (starting with one '
     'product category chosen for clear reasons) to a new online business', 'web', ['products', 'digital'],
     ['ENT.CUST.03'], ['case_amazon']),
    # ---------------------------------------------------------------- Foundation 11: Marketing, sales and social media
    ('ENT.MKT.01', 'Choosing a channel', 'Choose a marketing channel by where the stated customers already are',
     'marketing', A, ['ENT.CUST.02'], []),
    ('ENT.MKT.02', 'Useful content and a clear next step', 'Write marketing that is useful, consistent and ends with a '
     'clear next action', 'marketing', A, ['ENT.MKT.01'], []),
    ('ENT.MKT.03', 'Email lists: permission and unsubscribing', 'Build an email list with permission and honor '
     'unsubscribe requests', 'marketing', A, ['ENT.MKT.01'], ['ftc_canspam']),
    ('ENT.MKT.04', 'Local outreach, referrals and networking', 'Plan local outreach and referral relationships that '
     'help both sides', 'marketing', ['services', 'products'], ['ENT.MKT.01'], []),
    ('ENT.MKT.05', 'Testimonials and reviews with permission', 'Use real testimonials with permission and ask for honest '
     'reviews', 'marketing', A, ['ENT.MKT.02'], ['ftc_endorse', 'ftc_reviews']),
    ('ENT.MKT.06', 'Disclosing sponsorships and affiliate links', 'Recognize when a paid or affiliate relationship must '
     'be disclosed clearly', 'marketing', A, ['ENT.MKT.05'], ['ftc_endorse']),
    ('ENT.MKT.07', 'Organic versus paid; a small ad test', 'Plan a small paid test with a stated budget and measure',
     'marketing', A, ['ENT.MKT.01'], []),
    ('ENT.MKT.08', 'Reach, leads, sales and conversion rate', 'Compute and compare reach, leads, sales and conversion '
     'rates', 'marketing', A, ['ENT.MKT.07'], []),
    ('ENT.MKT.09', 'Fake followers, audience ownership and algorithm changes', 'Explain why bought followers mislead and '
     'why owning a direct contact list reduces platform risk', 'marketing', A, ['ENT.MKT.08'], []),
    ('ENT.MKT.10', 'Scheduling content and following platform rules', 'Plan a sustainable posting schedule and follow '
     'each platform\'s rules', 'marketing', ['content', 'products'], ['ENT.MKT.02'], []),
    ('ENT.CASE.07', 'Founder case: Blue Ribbon Sports sells at track meets', 'Apply a documented early decision '
     '(selling where the customers gather) to a new business', 'marketing', ['products'], ['ENT.MKT.01'],
     ['case_nike']),
    ('ENT.CASE.08', 'Founder case: Madam C. J. Walker builds distribution', 'Apply a documented early decision '
     '(training sales agents and reaching customers directly) to a new business', 'marketing', ['products'],
     ['ENT.MKT.04'], ['case_walker']),
    # ---------------------------------------------------------------- Foundation 12: AI as a helper
    ('ENT.AI.01', 'Useful jobs for AI tools', 'Choose tasks where an AI tool helps (drafts, outlines, ideas, summaries)',
     'ai', A, ['ENT.START.01'], []),
    ('ENT.AI.02', 'Asking clearly: task, context, audience', 'Write a clear request with task, context and audience, and '
     'improve it step by step', 'ai', A, ['ENT.AI.01'], []),
    ('ENT.AI.03', 'Made-up answers and checking facts', 'Explain that AI tools can state false things confidently, and '
     'check output against trusted sources', 'ai', A, ['ENT.AI.01'], []),
    ('ENT.AI.04', 'Confidential data and tool terms', 'Keep private customer and business data out of tools whose terms '
     'do not allow it', 'ai', A, ['ENT.AI.01'], []),
    ('ENT.AI.05', 'Human approval before it matters', 'Keep a person responsible for consequential actions, and tell '
     'automation from judgment', 'ai', A, ['ENT.AI.03'], []),
    ('ENT.AI.06', 'Measuring benefit and choosing tools', 'Choose AI tools by task, cost and measured results, and track '
     'subscriptions', 'ai', A, ['ENT.AI.01'], []),
    ('ENT.AI.07', 'No fake testimonials or false claims', 'Refuse AI-made testimonials, fake reviews and claims the '
     'business cannot support', 'ai', A, ['ENT.AI.03', 'ENT.MKT.05'], ['ftc_reviews']),
    # ---------------------------------------------------------------- Foundation 13: Operations and admin
    ('ENT.OPS.01', 'Simple procedures and scheduling', 'Write a short repeatable procedure and schedule work realistically',
     'ops', A, ['ENT.START.01'], []),
    ('ENT.OPS.02', 'Inventory and reorder points', 'Compute a reorder point from stated daily sales and delivery time',
     'ops', ['products'], ['ENT.OPS.01'], []),
    ('ENT.OPS.03', 'Subscriptions, free trials and cancellation dates', 'Track software subscriptions and free-trial end '
     'dates', 'ops', A, ['ENT.COST.01'], []),
    ('ENT.OPS.04', 'Passwords, two-step login and backups', 'Protect accounts with unique passwords, multifactor '
     'authentication and backups', 'ops', A, ['ENT.START.01'], []),
    ('ENT.OPS.05', 'Access for owners and helpers', 'Give helpers only the access they need and keep owner control',
     'ops', A, ['ENT.OPS.04'], []),
    ('ENT.OPS.06', 'Organizing records and file names', 'Name and store business files so they can be found later',
     'ops', A, ['ENT.BOOK.01'], []),
    ('ENT.OPS.07', 'A deadline calendar for filings and renewals', 'Keep one calendar of filings, renewals and other '
     'deadlines', 'ops', A, ['ENT.LEGAL.06'], []),
    ('ENT.OPS.08', 'Official notices versus paid solicitations', 'Tell an official government notice from a look-alike '
     'paid offer and verify it', 'ops', A, ['ENT.OPS.07'], ['irs_ein']),
    ('ENT.OPS.09', 'Lost phone, lost account and continuity', 'Plan recovery for a lost phone or account and who can act '
     'if the owner is unavailable', 'ops', A, ['ENT.OPS.04'], []),
    # ---------------------------------------------------------------- Foundation 14: Insurance, contracts, risk
    ('ENT.RISK.01', 'Insurance categories and exclusions', 'Match common business risks to insurance categories and '
     'check exclusions', 'risk', A, ['ENT.START.03'], []),
    ('ENT.RISK.02', 'Limits of personal and home policies', 'Recognize that personal or home policies may not cover '
     'business activity, and when to ask an agent', 'risk', A, ['ENT.RISK.01'], []),
    ('ENT.RISK.03', 'What a written agreement covers', 'Check an agreement for scope, payment, responsibilities, '
     'cancellation and ownership of work', 'risk', A, ['ENT.PAY.01'], []),
    ('ENT.RISK.04', 'Signed documents and customer information', 'Keep signed documents and protect customer '
     'information', 'risk', A, ['ENT.RISK.03'], []),
    ('ENT.RISK.05', 'Permission to use images, music, code and names', 'Recognize copyright and trademark issues and get '
     'permission or use licensed material', 'risk', A, ['ENT.LEGAL.02'], ['uspto_name', 'copyright_fairuse']),
    ('ENT.RISK.06', 'Truthful advertising and handling complaints', 'Keep claims supportable and handle complaints '
     'promptly and fairly', 'risk', A, ['ENT.MKT.02'], ['ftc_reviews']),
    # ---------------------------------------------------------------- Foundation 15: Help and partners
    ('ENT.HELP.01', 'Doing it yourself or getting help', 'Decide whether to do a task or get help, and define a clear '
     'deliverable', 'help', A, ['ENT.PRICE.06'], []),
    ('ENT.HELP.02', 'Contractor or employee is not just a label', 'Explain that worker classification depends on the '
     'real working relationship and current rules', 'help', A, ['ENT.HELP.01'], ['dol_contractor']),
    ('ENT.HELP.03', 'Payroll responsibilities (the idea)', 'Describe the ideas of payroll withholding and employer '
     'responsibilities', 'help', A, ['ENT.HELP.02'], ['dol_contractor']),
    ('ENT.HELP.04', 'Onboarding and offboarding helpers', 'Plan access, files and handover when a helper starts or '
     'leaves', 'help', A, ['ENT.OPS.05'], []),
    ('ENT.HELP.05', 'Partners: roles, ownership and disagreements', 'Separate ownership percentages from work roles and '
     'plan for disagreements', 'help', A, ['ENT.LEGAL.07'], []),
    ('ENT.HELP.06', 'Mentors, accountants, attorneys and free help', 'Match a question to the right kind of advisor or '
     'free resource', 'help', A, ['ENT.LEGAL.11'], ['sba_counsel']),
    # ---------------------------------------------------------------- Funding, growth and limits
    ('ENT.FUND.01', 'Bootstrapping and using savings', 'Compare paying for a business from savings and early sales with '
     'outside money', 'growth', A, ['ENT.CASH.03'], []),
    ('ENT.FUND.02', 'Loans: interest, repayment and guarantees', 'Compute simple loan costs from stated terms and spot '
     'personal guarantees', 'growth', A, ['ENT.FUND.01'], []),
    ('ENT.FUND.03', 'Grants and their limits', 'Explain that grants are competitive, limited and come with conditions',
     'growth', A, ['ENT.FUND.01'], ['sba_counsel']),
    ('ENT.FUND.04', 'Investors and crowdfunding', 'Compare repaying money with giving up ownership, and see that most '
     'businesses do not fit investor funding', 'growth', A, ['ENT.FUND.02'], []),
    ('ENT.FUND.05', 'Money raised is not profit', 'Separate money from loans or investors from revenue and profit',
     'growth', A, ['ENT.FUND.04', 'ENT.CASH.01'], []),
    ('ENT.GROW.01', 'Unit economics', 'Compute profit per customer or per order from stated numbers', 'growth', A,
     ['ENT.PRICE.03'], []),
    ('ENT.GROW.02', 'Getting customers, keeping customers, repeat sales', 'Compare the cost of getting a customer with '
     'what a returning customer brings', 'growth', A, ['ENT.GROW.01'], []),
    ('ENT.GROW.03', 'Growing after evidence, protecting quality', 'Decide when growth is supported by evidence and '
     'capacity', 'growth', A, ['ENT.GROW.02'], []),
    ('ENT.GROW.04', 'Burnout and a sustainable pace', 'Plan workload and limits that a person can keep up', 'growth', A,
     ['ENT.PRICE.06'], []),
    ('ENT.GROW.05', 'Winding down honestly', 'List the obligations to handle when closing or pausing a business',
     'growth', A, ['ENT.OPS.07'], []),
    ('ENT.CASE.09', 'Founder case: Wrigley follows what customers wanted', 'Apply a documented change of offer (switching '
     'to the item customers preferred) to a new business', 'growth', ['products'], ['ENT.TEST.07'], ['case_wrigley']),
    # ---------------------------------------------------------------- Path: services
    ('ENT.SVC.01', 'Estimating a service job', 'Estimate a job from stated hours, rate, materials and travel', 'services',
     SV, ['ENT.PRICE.06'], []),
    ('ENT.SVC.02', 'Appointment capacity and travel time', 'Compute how many appointments fit with travel and setup',
     'services', SV, ['ENT.SVC.01'], []),
    ('ENT.SVC.03', 'Service scope and deposits', 'Write service scope and deposit terms that prevent disputes', 'services',
     SV, ['ENT.PAY.04'], []),
    ('ENT.SVC.04', 'Repeat clients and scheduling them', 'Plan for repeat clients and recurring appointments', 'services',
     SV, ['ENT.GROW.02'], []),
    ('ENT.CASE.10', 'Founder case: Airbnb starts with its founders\' own apartment', 'Apply a documented early test '
     '(serving a few real guests during a known demand spike) to a new service', 'services', SV, ['ENT.TEST.04'],
     ['case_airbnb']),
    # ---------------------------------------------------------------- Path: products
    ('ENT.PROD.01', 'Suppliers, samples and reliability', 'Compare suppliers by samples, terms and reliability, not '
     'price alone', 'products', PR, ['ENT.PAY.08'], []),
    ('ENT.PROD.02', 'Packaging and damage', 'Choose packaging that protects items, and price in damage', 'products', PR,
     ['ENT.PRICE.01'], []),
    ('ENT.PROD.03', 'Returns and fulfillment', 'Plan returns, restocking and order fulfillment', 'products', PR,
     ['ENT.PAY.03'], []),
    ('ENT.PROD.04', 'Choosing selling channels', 'Compare selling channels by fees, control and customers reached',
     'products', PR, ['ENT.PRICE.04'], []),
    ('ENT.PROD.05', 'Shipping costs and return addresses', 'Include shipping costs and a reliable return address in an '
     'online product plan', 'products', PR, ['ENT.PROD.02', 'ENT.MAIL.03'], []),
    # ---------------------------------------------------------------- Path: digital
    ('ENT.DIG.01', 'Support and updates for digital products', 'Plan support and updates a digital product needs',
     'digital', DG, ['ENT.START.03'], []),
    ('ENT.DIG.02', 'Access, accounts and licensing', 'Decide what buyers may do with a digital product and how they get '
     'access', 'digital', DG, ['ENT.DIG.01'], []),
    ('ENT.DIG.03', 'Recurring costs of digital businesses', 'Include hosting, tools and fees that grow with customers',
     'digital', DG, ['ENT.COST.02'], []),
    ('ENT.DIG.04', 'Onboarding and checking usefulness', 'Help new users succeed and measure whether they keep using it',
     'digital', DG, ['ENT.DIG.01'], []),
    ('ENT.CASE.11', 'Founder case: Microsoft\'s first product for one platform', 'Apply a documented early decision '
     '(building software for a specific new machine and licensing it) to a new digital business', 'digital', DG,
     ['ENT.CUST.04'], ['case_microsoft']),
    # ---------------------------------------------------------------- Path: content
    ('ENT.CONT.01', 'Original content and rights', 'Use original or licensed material and respect others\' rights',
     'content', CT, ['ENT.RISK.05'], ['copyright_fairuse']),
    ('ENT.CONT.02', 'Sponsorships and affiliate relationships', 'Evaluate a sponsor or affiliate deal for fit, terms and '
     'disclosure', 'content', CT, ['ENT.MKT.06'], ['ftc_endorse']),
    ('ENT.CONT.03', 'Being seen versus being eligible to earn', 'Tell platform visibility from monetization eligibility '
     'and check the official rules', 'content', CT, ['ENT.MKT.09'], ['youtube_ypp']),
    ('ENT.CONT.04', 'Audience trust and diversification', 'Protect audience trust and avoid depending on one platform or '
     'sponsor', 'content', CT, ['ENT.CONT.02'], []),
    ('ENT.CONT.05', 'Creator costs and uneven income', 'Plan for creator costs and income that changes month to month',
     'content', CT, ['ENT.CASH.03'], []),
    ('ENT.CASE.12', 'Founder case: Craigslist grows from an email list', 'Apply a documented early pattern (a free list '
     'that grew because users asked for more) to a new content or community business', 'content', CT,
     ['ENT.MKT.03'], ['case_craigslist']),
]

SUGGESTED = {
    # optional reading that helps but is not required (shown as "you may also like")
    'ENT.PAY.06': ['ENT.BANK.05'], 'ENT.WEB.06': ['ENT.MKT.02'], 'ENT.CONT.03': ['ENT.CASE.12'],
    'ENT.FUND.03': ['ENT.HELP.06'], 'ENT.AI.06': ['ENT.OPS.03'],
}

SET_NUM = {row[0]: i + 1 for i, row in enumerate(ROWS)}
SETS = {i + 1: dict(code=row[0], title=row[1], outcome_title=row[2], module=row[3], paths=row[4],
                    requires=[SET_NUM[c] for c in row[5]], sources=row[6],
                    status='time_sensitive' if row[6] else 'stable')
        for i, row in enumerate(ROWS)}

# sanity: prerequisites point backward, modules and paths exist
_mods = {m[0] for m in MODULES}
_paths = {p['id'] for p in PATHS}
for _n, _s in SETS.items():
    assert _s['module'] in _mods, _s
    assert all(r < _n for r in _s['requires']), ('prerequisite must come earlier', _n, _s['requires'])
    assert all(p in _paths for p in _s['paths'])
assert len(SET_NUM) == len(ROWS), 'duplicate outcome code'
