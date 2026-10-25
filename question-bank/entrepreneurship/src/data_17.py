"""Entrepreneurship sets 97-103: Foundation 12, using AI tools responsibly in a small business."""
from eq import Q, sec, cs, mathb, SET

# ------------------------------------------------------------------ Set 97: useful jobs for AI tools
JOBS = ('AI tools (programs that generate text, images or summaries from a request) can save time on DRAFTING and '
        'ORGANIZING work: a first draft of a product description, a summary of long notes, ideas for a social post, a '
        'list of questions to ask a supplier, or reformatting a price list. They are weaker at work that needs verified '
        'facts, legal or tax certainty, or knowledge of your specific customers. A good rule: let the tool draft, and let '
        'a person who knows the business check and decide.')

s97 = SET('ENT.AI.01',
    M=sec('Match tasks to what AI tools do well and poorly', JOBS, [
        Q('Which task suits an AI tool well?', 'Drafting a first version of a product description',
          ('Deciding the final legal structure for the business alone', 'needs professional judgment'),
          ('Confirming this year\'s exact tax rules with certainty', 'needs verified sources'),
          ('Knowing which local customers will definitely buy', 'tool cannot know'), 'Drafting is a strong use.'),
        Q('Which task is AI weaker at?', 'Giving verified legal or tax certainty', ('Suggesting ideas for a social post', 'good use'),
          ('Summarizing long meeting notes', 'good use'), ('Reformatting a price list neatly', 'good use'), 'Certainty needs checking.'),
        Q('What is the good rule from the passage?', 'Let the tool draft; a person checks and decides',
          ('Let the tool decide everything without review', 'risky'), ('Never use any tools for any task', 'too strict'),
          ('Let customers check the drafts for you', 'not their job'), 'Human judgment stays in charge.'),
        Q('Which is an organizing task?', 'Summarizing long notes into key points', ('Signing a lease on the owner\'s behalf', 'not organizing'),
          ('Choosing who to hire without review', 'decision'), ('Approving a refund automatically', 'decision'), 'Summaries organize information.'),
        Q('Why is an AI tool weak at knowing your customers?', 'It does not have your specific customer knowledge',
          ('It always knows every customer personally', 'not true'), ('Customers are illegal to describe', 'not true'),
          ('It refuses to write about customers ever', 'not the reason'), 'Local knowledge comes from you.'),
    ]),
    B=[cs('A fast but new assistant', 'Imagine hiring a very fast assistant on their first day. They can type a draft letter in '
          'minutes and tidy a messy list, but they do not know your customers, your prices, or the law, and they sometimes '
          'guess confidently. You would let them draft, then read it before anything is sent. An AI tool is like that '
          'assistant: helpful for drafts, not a replacement for your judgment.', [
        Q('What is the new assistant good at?', 'Fast drafts and tidying lists', ('Knowing every customer by name', 'new'),
          ('Knowing all the laws', 'no'), ('Never making mistakes', 'they guess'), 'Speed on drafts.'),
        Q('What does the new assistant not know?', 'Your customers, prices and the law', ('How to type', 'they can'),
          ('How to list items', 'they can'), ('How to write short letters to people', 'they can'), 'Business-specific knowledge.'),
        Q('What would you do before a letter is sent?', 'Read and check it', ('Send it unread', 'risky'), ('Throw it away', 'no'),
          ('Ask a stranger to read it', 'no'), 'Review first.'),
        Q('An AI tool is most like what?', 'A fast new assistant', ('A licensed attorney', 'no'), ('A tax agency', 'no'),
          ('An owner', 'no'), 'Helpful but needs supervision.'),
        Q('Why check the assistant\'s work?', 'They sometimes guess confidently', ('They are always perfect on day one', 'no'),
          ('They never type', 'no'), ('Checking is illegal', 'no'), 'Confidence is not accuracy.'),
    ], why='A learner who misses MAIN may over-trust or under-use AI; a fast new assistant shows the right role.')],
    F1=sec('Apply it: decide where AI helps a real business', JOBS, [
        Q('A bakery owner spends 2 hours a week writing product descriptions. Which use of AI fits best?', 'Draft descriptions, then the owner edits them',
          ('Let AI decide the prices of every product', 'needs owner judgment'), ('Let AI reply to complaints without review', 'risky'),
          ('Let AI choose the business structure', 'needs professional'), 'Drafting with review.'),
        Q('Drafting with AI cuts writing from 120 minutes to 45 minutes a week. How many minutes are saved each week?', '75',
          ('45', 'new time'), ('165', 'added'), ('120', 'old time'), '120 - 45 = 75.', calc=lambda: 120 - 45 == 75),
        Q('Drafting with AI cuts writing from 120 minutes to 45 minutes a week. Over 4 weeks, how many hours does that save?',
          '5 hours',
          ('75 hours', 'used minutes'), ('3 hours', 'miscalculated'),
          ('300 hours', 'did not convert'),
          '75 x 4 = 300 minutes = 5 hours.',
          calc=lambda: 75 * 4 / 60 == 5),
        Q('Which request is a poor fit for AI alone?', '"Tell me exactly what I owe in taxes this year."', ('"List 10 ideas for a spring post."', 'good fit'),
          ('"Summarize these customer emails."', 'good fit'), ('"Reformat this price list as a neat table with two columns."', 'good fit'), 'Tax certainty needs a professional.'),
        Q('An owner asks AI for supplier questions before a meeting. What should she do with the list?', 'Review it and add questions only she would know',
          ('Use it unread', 'may miss key items'), ('Send it to the supplier as a signed contract', 'not a contract'),
          ('Delete it without looking', 'wasted'), 'Combine draft and knowledge.'),
    ]),
    F2=sec('Handle the complications: over-reliance and false savings', JOBS, [
        Q('An owner uses AI for everything and stops reading outputs. What is the main risk?', 'Errors reach customers without anyone noticing',
          ('Nothing, because AI output is always right', 'not true'), ('Sales double automatically', 'not guaranteed'), ('Taxes disappear', 'no'),
          'Review is essential.'),
        Q('Fixing AI drafts takes longer than writing from scratch for one task. What should the owner conclude?', 'AI is not saving time for that task',
          ('AI must always be used anyway, even if slower', 'not if slower'), ('Writing is never needed', 'not true'), ('The task should be abandoned', 'not necessary'),
          'Measure actual benefit.'),
        Q('A tool produces a social post with a claim the owner cannot support. What should she do?', 'Remove or correct the claim before posting',
          ('Post it unchanged, since the tool wrote it', 'owner is responsible'), ('Add more unsupported claims', 'worse'),
          ('Blame the tool publicly', 'not a fix'), 'The business is responsible for what it publishes.'),
        Q('Which statement about responsibility is accurate?', 'The business is responsible for what it sends, even if a tool drafted it.',
          ('The tool maker is responsible for every message a business sends.', 'not how it works'),
          ('Customers are responsible for checking drafts.', 'no'), ('Nobody is responsible for AI text.', 'no'),
          'Owners own their messages.'),
        Q('Which statement is accurate?', 'AI tools help most with drafts and organizing, with a person checking.',
          ('AI tools fully replace all professional advice for small businesses.', 'not true'), ('AI tools never help small businesses.', 'not true'),
          ('AI outputs need no review.', 'not true'), 'Balanced use.'),
    ]))

# ------------------------------------------------------------------ Set 98: asking clearly
PROMPT = ('An AI tool works better with a clear request (often called a PROMPT). Include: the TASK ("write a 50-word '
          'product description"), the CONTEXT (what the product is, price, who makes it), the AUDIENCE ("busy parents"), '
          'and any LIMITS (tone, length, words to avoid, facts that must be included). Vague requests like "write '
          'something good" give vague results. If the first answer is off, refine the request with specific feedback.')

s98 = SET('ENT.AI.02',
    M=sec('Write a clear request with task, context, audience and limits', PROMPT, [
        Q('Which request is clearest?', '"Write a 50-word description of our 12-dollar lavender soap for busy parents."',
          ('"Write something good about our soap for people, please, thanks."', 'vague'), ('"Make it nice."', 'vague'), ('"Do marketing."', 'vague'),
          'Task, context, audience and length.'),
        Q('What is "context" in a request?', 'Details like the product and its price',
          ('The color of the computer screen being used', 'irrelevant'), ('The time of day the owner types', 'irrelevant'),
          ('The tool\'s company history', 'irrelevant'), 'Background information.'),
        Q('Which is a limit?', '"Keep it under 60 words and avoid medical claims"', ('"Our soap is lavender scented and handmade"', 'context'),
          ('"For busy parents"', 'audience'), ('"Write a description"', 'task'), 'Limits set boundaries.'),
        Q('The first answer is too formal. What should the owner do?', 'Ask again with specific feedback',
          ('Give up on the tool forever', 'premature'), ('Post the formal version anyway', 'not what she wanted'),
          ('Type the same request again unchanged and hope', 'same result likely'), 'Refine with feedback.'),
        Q('Why do vague requests give vague results?', 'The tool has little to work with', ('Tools punish vague users', 'no'),
          ('Vague requests are illegal', 'no'), ('Tools only answer long questions', 'no'), 'Specific input, specific output.'),
    ]),
    B=[cs('Ordering at a sandwich counter', 'If you say "a sandwich," you might get anything. If you say "turkey on wheat, no '
          'mayo, toasted, cut in half," you get what you wanted. The order includes what (task), how (limits), and for whom '
          '(maybe "for my child, small size"). A clear AI request works the same way. If the sandwich comes out wrong, you '
          'tell the person exactly what to fix.', [
        Q('"A sandwich" is like what kind of request?', 'A vague one', ('A clear one', 'no'), ('A rude one', 'no'), ('A paid one', 'no'),
          'Too little detail.'),
        Q('"No mayo" is like what part of a request?', 'A limit', ('The audience', 'no'), ('The task', 'no'), ('The context', 'no'),
          'A boundary.'),
        Q('"For my child, small size" is like what part?', 'The audience', ('A limit only', 'partly'), ('The task', 'no'), ('A price', 'no'),
          'Who it is for.'),
        Q('If the sandwich is wrong, what do you do?', 'Say exactly what to fix', ('Leave without a word', 'no'), ('Order the same vague thing', 'no'),
          ('Eat it unhappily forever', 'no'), 'Specific feedback.'),
        Q('A clear order gets what?', 'What you wanted', ('Something random', 'no'), ('Nothing', 'no'), ('A bigger bill', 'no'),
          'Clarity improves results.'),
    ], why='A learner who misses MAIN may not see what makes a request clear; ordering a sandwich is familiar.')],
    F1=sec('Apply it: improve requests', PROMPT, [
        Q('Rewrite "help with email." Which version is best?', '"Draft a polite 80-word reply to a customer whose order is 3 days late."',
          ('"Help with my email again, but make it much better this time, please."', 'still vague'), ('"Email."', 'vague'),
          ('"Do my emails for me forever."', 'vague and risky'), 'Specific task, context and limit.'),
        Q('A request lacks the audience. What should be added?', 'Who the message is for',
          ('The owner\'s favorite color for emails', 'irrelevant'), ('The tool\'s price', 'irrelevant'), ('A random number', 'irrelevant'),
          'Audience shapes tone.'),
        Q('An owner wants a description that must mention "handmade in Ohio." Where does that belong in the request?', 'In the limits or required facts',
          ('Nowhere; the tool will guess it', 'it may not'), ('Only after posting', 'too late'), ('In a separate email to customers', 'wrong place'),
          'State required facts.'),
        Q('Three tries with vague requests took 15 minutes; one clear request took 5 minutes. How much time did clarity save?', '10 minutes',
          ('20 minutes', 'added'), ('5 minutes', 'clear time'), ('15 minutes', 'vague time'), '15 - 5 = 10.', calc=lambda: 15 - 5 == 10),
        Q('The tool wrote 200 words when 50 were needed. What feedback is best?', '"Shorten to 50 words, keep the price and key benefit."',
          ('"Wrong. Again."', 'not specific'), ('"Make it different somehow, but similar to before."', 'vague'), ('"Try harder."', 'vague'),
          'Specific feedback fixes it.'),
    ]),
    F2=sec('Handle the complications: requests that cause problems', PROMPT, [
        Q('An owner asks AI to "write 10 glowing customer reviews." What is the problem?', 'Invented reviews would be deceptive',
          ('Nothing; reviews are just text', 'deceptive'), ('The number should be 20', 'still fake'), ('Reviews must be long', 'irrelevant'),
          'Do not request fake reviews.'),
        Q('A request includes a customer\'s full name, address and card number. What should the owner do instead?', 'Remove private details before using the tool',
          ('Include even more personal details', 'risky'), ('Post the details publicly', 'harmful'), ('Ignore privacy because tools are safe', 'unsafe'),
          'Protect customer data.'),
        Q('The tool gives a confident answer about a local permit rule. What should the owner do?', 'Check it with the official local source',
          ('Trust it fully because it sounds sure', 'may be wrong'), ('Share it as legal advice', 'risky'), ('Ignore permits', 'risky'),
          'Verify facts.'),
        Q('Which request leaves out the most important part for a price-list task?', '"Make a table" with no prices given', ('"Table of 5 items with prices"', 'complete'),
          ('"Table with columns item and price"', 'complete'), ('"Use these 5 items and prices"', 'complete'), 'Context is missing.'),
        Q('Which statement is accurate?', 'Clear requests help, but the owner still checks facts.',
          ('A clear request always guarantees a perfect answer.', 'not guaranteed'), ('Vague requests work best.', 'not true'),
          ('Requests never need context.', 'they do'), 'Clarity helps; review remains.'),
    ]))

# ------------------------------------------------------------------ Set 99: made-up answers and checking facts
FACT = ('AI tools can produce answers that sound confident but are wrong or invented, sometimes called HALLUCINATIONS: a '
        'fake statistic, a law that does not exist, a made-up source, or a wrong price. Check any fact that matters: '
        'numbers, dates, laws, prices, names and quotations. Use the original or official source, not another AI answer. '
        'If a source is given, open it and confirm it says what was claimed. When you cannot verify a fact, leave it out.')

s99 = SET('ENT.AI.03',
    M=sec('Recognize made-up answers and verify facts that matter', FACT, [
        Q('What is a hallucination in AI output?', 'A confident answer that is wrong or invented',
          ('A picture the tool draws of someone\'s dream', 'not the meaning'), ('A slow internet connection', 'not the meaning'),
          ('A password reset email', 'not the meaning'), 'Invented or wrong content.'),
        Q('Which facts should be checked?', 'Numbers, dates, laws, prices, names and quotes', ('Only the font of the answer', 'irrelevant'),
          ('Nothing; tools never err', 'they can'), ('Only facts the owner already knows by heart', 'too narrow'), 'Anything that matters.'),
        Q('What is the best way to verify a law mentioned by AI?', 'Read the official government source',
          ('Ask the same tool if it is sure', 'not independent'), ('Ask another AI tool', 'not a source'),
          ('Assume it is right if it sounds formal', 'risky'), 'Use the official source.'),
        Q('An AI answer cites a source. What should the owner do?', 'Open the source and confirm it says that',
          ('Trust it because a source is listed', 'sources can be invented'), ('Delete the source', 'not helpful'),
          ('Share it without reading', 'risky'), 'Confirm the citation.'),
        Q('A fact cannot be verified. What does the passage advise?', 'Leave it out', ('Use it anyway, boldly', 'risky'),
          ('Make it sound more certain', 'worse'), ('Double the number to be safe', 'worse'), 'Unverified facts stay out.'),
    ]),
    B=[cs('A confident friend who sometimes guesses', 'Some people answer every question confidently, even when they are '
          'guessing: "Oh yes, the store closes at 9." Sometimes they are right, sometimes not. You would check the store\'s '
          'own hours before driving there. AI tools can be like that friend. A confident tone is not proof; checking the '
          'original source is. That one extra step can save a wasted trip.', [
        Q('Is a confident tone proof that an answer is right?', 'No', ('Yes, always', 'not proof'), ('Only on weekdays', 'no'),
          ('Only for numbers', 'no'), 'Confidence is not evidence.'),
        Q('How would you check the store\'s closing time?', 'Look at the store\'s own hours', ('Ask the same friend again', 'not independent'),
          ('Guess', 'no'), ('Drive and hope', 'risky'), 'Use the original source.'),
        Q('The confident friend is like what?', 'An AI tool that sometimes guesses', ('A government website page of laws', 'no'),
          ('A store\'s sign', 'no'), ('A receipt', 'no'), 'Sounds sure, may be wrong.'),
        Q('What is the "original source" in the story?', 'The store\'s own hours', ('The confident friend', 'no'), ('A rumor', 'no'),
          ('A map', 'not the hours'), 'The authority on the fact.'),
        Q('What should you do with an important AI fact?', 'Check the original source', ('Trust its tone', 'no'), ('Ignore it', 'not needed'),
          ('Repeat it louder to others', 'no'), 'Verify.'),
    ], why='A learner who misses MAIN may trust confident output; a guessing friend shows why checking matters.')],
    F1=sec('Apply it: check AI output before using it', FACT, [
        Q('An AI draft says "73 percent of shoppers prefer handmade soap," with no source. What should the owner do?', 'Remove the claim unless a real source confirms it',
          ('Keep it, because it sounds convincing to readers', 'unsupported'), ('Change it to 90 percent', 'worse'), ('Add "studies show" to it', 'still unsupported'),
          'No source, no claim.'),
        Q('An AI tool says the state filing fee is 50 dollars. The official site says 125 dollars. Which should the owner use?', '125 dollars, from the official site',
          ('50 dollars, from the tool', 'contradicted'), ('An average of the two, 87.50 dollars', 'not a fact'), ('Neither; skip filing', 'risky'),
          'Official sources win.'),
        Q('A draft quotes a famous founder. The owner cannot find the quote anywhere reliable. What should she do?', 'Leave the quote out',
          ('Keep it and add a date', 'still unverified'), ('Attribute it to someone else', 'worse'), ('Make it longer', 'irrelevant'),
          'Unverifiable quotes stay out.'),
        Q('An AI summary of a supplier contract says delivery is 10 days; the contract says 21. How many days off is the summary?',
          '11 days', ('10 days', 'summary value'), ('21 days', 'contract value'), ('31 days', 'added'), '21 - 10 = 11.',
          calc=lambda: 21 - 10 == 11),
        Q('Which items in a draft press release most need checking?', 'Prices, dates and names', ('The paragraph spacing', 'minor'),
          ('The font choice', 'minor'), ('The number of commas', 'minor'), 'Facts that matter.'),
    ]),
    F2=sec('Handle the complications: subtle errors', FACT, [
        Q('An AI draft gets the price right but the store hours wrong. What does this show?', 'One correct fact does not mean all facts are correct',
          ('The whole draft must be reliable then, including hours', 'not necessarily'), ('Store hours never matter', 'they do'), ('Prices are always wrong', 'no'),
          'Check each fact.'),
        Q('Two AI tools give the same wrong answer. Is that verification?', 'No, verification needs an original source',
          ('Yes, two tools always confirm truth', 'not independent proof'), ('Yes, if both sound confident', 'no'),
          ('Only if a third agrees', 'still not a source'), 'Agreement is not a source.'),
        Q('A tool invents a regulation and the owner posts it. A customer points it out. What should the owner do?', 'Correct the post and thank the customer',
          ('Delete the customer\'s comment quietly', 'hides error'), ('Argue that the tool said so', 'not a defense'),
          ('Ignore it', 'spreads error'), 'Correct mistakes openly.'),
        Q('An AI sales forecast says revenue will grow 300 percent next year. What should the owner treat it as?', 'An unsupported guess until checked against real data',
          ('A guaranteed result for next year\'s sales planning', 'not guaranteed'), ('A legal promise', 'no'), ('A bank statement', 'no'), 'Forecasts need evidence.'),
        Q('Which statement is accurate?', 'Confident AI answers can still be wrong, so check facts that matter.',
          ('AI never invents sources.', 'it can'), ('Checking facts wastes time.', 'not for important facts'),
          ('If an answer sounds formal and certain, then it must be true.', 'not true'), 'Verify.'),
    ]))

# ------------------------------------------------------------------ Set 100: confidential data and tool terms
DATA = ('Before putting information into an AI tool, think about who could see it. Some tools may store what you type or use '
        'it to improve their systems, depending on the tool\'s TERMS and settings. Do not paste CONFIDENTIAL information '
        'unless you know how it is handled: customer names with contact details, card numbers, passwords, private health '
        'details, or a client\'s secret plans. Read the tool\'s privacy terms, check business settings, and remove or '
        'replace personal details (for example "Customer A") when you can.')

s100 = SET('ENT.AI.04',
    M=sec('Protect confidential data when using AI tools', DATA, [
        Q('What may some AI tools do with what you type?', 'Store it or use it to improve their systems, depending on terms',
          ('Delete it before you finish typing, always', 'not how it works'),
          ('Send it back to you as a printed letter', 'not how it works'),
          ('Turn it into a legal contract automatically for you to sign', 'no'), 'Terms and settings decide.'),
        Q('Which should NOT be pasted into a tool without knowing how it is handled?', 'A customer\'s card number',
          ('A generic list of product colors', 'not sensitive'), ('A public holiday schedule', 'not sensitive'),
          ('A draft headline for a post', 'not sensitive'), 'Payment data is confidential.'),
        Q('What is a safer way to ask about a customer complaint?', 'Replace names and details with "Customer A"',
          ('Include the full name, address and phone', 'exposes data'), ('Paste the customer\'s login password', 'never'),
          ('Attach the customer\'s card photo', 'never'), 'Remove personal details.'),
        Q('Where can an owner learn how a tool handles data?', 'The tool\'s privacy terms and settings', ('A random forum guess', 'unreliable'),
          ('The tool\'s logo', 'irrelevant'), ('A competitor\'s opinion of the tool', 'unreliable'), 'Read the terms.'),
        Q('Which information is confidential?', 'A client\'s secret product launch plans', ('A public store address', 'public'),
          ('A posted price list', 'public'), ('The business\'s public website text', 'public'), 'Secret plans are confidential.'),
    ]),
    B=[cs('Talking in a crowded café', 'You would not read a customer\'s credit card number out loud in a crowded café, because '
          'strangers might hear. Typing into an online tool can be similar: depending on its terms, what you type may be '
          'stored or seen. Talk about general ideas freely, but keep private details private, or replace them with '
          'placeholders like "Customer A."', [
        Q('Why not read a card number aloud in a café?', 'Strangers might hear', ('Cafés ban numbers', 'no'),
          ('Coffee gets cold', 'no'), ('It is too long', 'not the reason'), 'Privacy risk.'),
        Q('Typing into an online tool can be like what?', 'Talking in a crowded café', ('Whispering alone at home', 'no'),
          ('Writing in a locked diary', 'not necessarily'), ('Thinking silently', 'no'), 'Others may access it.'),
        Q('What can be discussed freely?', 'General ideas', ('Card numbers', 'no'), ('Passwords', 'no'), ('Health details', 'no'),
          'Non-private topics.'),
        Q('What is a placeholder?', 'A stand-in like "Customer A"', ('A real phone number in full', 'no'), ('A password', 'no'),
          ('A signature', 'no'), 'It hides identity.'),
        Q('What should stay private?', 'Private customer details', ('Product colors and sizes', 'public'), ('Store hours', 'public'),
          ('A blog title', 'public'), 'Protect personal data.'),
    ], why='A learner who misses MAIN may not see why typed data can be exposed; a crowded café makes it concrete.')],
    F1=sec('Apply it: decide what is safe to share', DATA, [
        Q('A bookkeeper wants AI to summarize a client\'s bank statements. What should she check first?', 'The tool\'s data terms and her client agreement',
          ('Nothing, because summaries are always private', 'not necessarily'), ('Only the summary length', 'not the issue'),
          ('Only the tool\'s colors', 'irrelevant'), 'Confidential financial data.'),
        Q('Which prompt is safest?', '"Draft a polite reply to a customer upset about a late order."', ('"Reply to Jane Lee, 14 Elm St, card 4111..."', 'exposes data'),
          ('"Here is my admin password; fix my site."', 'never share'), ('"Here are all customer emails and phone numbers; write to them."', 'exposes data'),
          'No personal details needed.'),
        Q('A business tool plan says data is not used for training; the free plan says it may be. Which fits confidential work better?',
          'The business plan, after confirming its terms', ('The free plan, since it costs less each month', 'may use data'),
          ('Either; terms never matter', 'they matter'), ('Neither; tools are illegal', 'not true'), 'Terms decide fit.'),
        Q('An owner pastes 120 customer emails into a tool by mistake. What is a sensible first step?', 'Check the tool\'s deletion options and terms, and stop sharing more',
          ('Paste the rest too', 'worse'), ('Paste the rest of the customer emails too, since the first batch is already in', 'harmful'), ('Ignore it entirely', 'risky'),
          'Limit and address the exposure.'),
        Q('Which detail can usually be replaced with a placeholder?', 'The customer\'s name', ('The question being asked', 'needed'),
          ('The product type', 'often needed'), ('The tone wanted', 'needed'), 'Names are rarely needed.'),
    ]),
    F2=sec('Handle the complications: client rules and staff use', DATA, [
        Q('A client contract says their information must not be shared with outside services. What should the owner do?', 'Not paste their information into outside tools',
          ('Paste it anyway, since tools are helpful', 'breaks contract'), ('Ask the tool for permission', 'not the client'),
          ('Hide it from the client', 'dishonest'), 'Follow the contract.'),
        Q('A helper uses a personal AI account for business documents. What should the owner set?', 'Clear rules on which tools and data are allowed',
          ('No rules at all', 'risky'), ('Rules only for the owner, not for helpers', 'incomplete'), ('A ban on all computers', 'impractical'),
          'Set a simple policy.'),
        Q('A tool\'s terms change. What should a business that relies on it do?', 'Review the new terms and settings',
          ('Assume nothing changed', 'risky'), ('Stop reading terms forever after this', 'risky'), ('Share more data', 'worse'),
          'Terms can change.'),
        Q('Which item is never appropriate to paste?', 'A password', ('A public product name', 'fine'), ('A generic question', 'fine'),
          ('A draft headline', 'fine'), 'Passwords stay private.'),
        Q('Which statement is accurate?', 'How a tool handles data depends on its terms and settings, so check before sharing.',
          ('Every AI tool keeps everything private.', 'not guaranteed'), ('Customer data is fine to share with any tool, as long as it is useful.', 'not true'),
          ('Terms never change.', 'they can'), 'Check first.'),
    ]))

# ------------------------------------------------------------------ Set 101: human approval before it matters
HUMAN = ('Some actions should never happen without a person checking first. Require HUMAN APPROVAL before AI-assisted work '
         'reaches customers or creates obligations: sending emails or posts, changing prices, issuing refunds, signing or '
         'sending contracts, making hiring decisions, or giving advice about health, money or law. The higher the stakes, '
         'the more careful the review. A simple rule is: "Draft by tool, decision by person," with the reviewer named for '
         'each type of task.')

s101 = SET('ENT.AI.05',
    M=sec('Decide which AI-assisted actions need a person\'s approval first', HUMAN, [
        Q('Which action needs human approval first?', 'Sending a refund to a customer', ('Brainstorming ten slogan ideas', 'low stakes'),
          ('Sorting notes into a list for yourself', 'internal'), ('Drafting a private to-do list', 'internal'),
          'Refunds create obligations.'),
        Q('What is the simple rule from the passage?', '"Draft by tool, decision by person"', ('"Decide by tool, never review"', 'risky'),
          ('"Never use tools for drafts"', 'too strict'), ('"Let customers decide everything"', 'not their role'), 'Humans decide.'),
        Q('How should review change as stakes rise?', 'It should become more careful', ('It should stop entirely', 'opposite'),
          ('It should become random', 'no'), ('It should be done by the tool', 'no'), 'Higher stakes, more care.'),
        Q('Which is a high-stakes area?', 'Advice about health, money or law', ('Choosing an emoji for a post', 'low'),
          ('Picking a background color', 'low'), ('Naming a playlist', 'low'), 'Mistakes can cause harm.'),
        Q('Why name a reviewer for each task type?', 'So it is clear who must approve', ('So nobody has to be responsible', 'opposite'),
          ('So reviews never happen', 'opposite'), ('So the tool can sign', 'no'), 'Clear accountability.'),
    ]),
    B=[cs('A teacher grading a draft', 'A student can write a draft quickly, but the teacher reads it before it counts. In a '
          'business, AI can write a draft quickly, but a person reads it before it reaches a customer. The bigger the '
          'consequence, like a final exam versus a practice quiz, the more carefully the teacher checks. The student still learns from the feedback.', [
        Q('Who reads the draft before it counts?', 'The teacher', ('Nobody', 'no'), ('A random stranger', 'no'),
          ('The draft itself', 'no'), 'A responsible reviewer.'),
        Q('In business, who is like the teacher?', 'A person who approves before it reaches customers', ('The AI tool', 'it drafts'),
          ('The customer who will receive the message later', 'no'), ('A competitor', 'no'), 'Human approval.'),
        Q('A final exam versus a practice quiz is like what?', 'High stakes versus low stakes', ('Two equal tasks', 'no'),
          ('Two kinds of pens for writing', 'no'), ('Two lunch options', 'no'), 'Stakes differ.'),
        Q('When does the teacher check most carefully?', 'When the consequence is bigger', ('Never', 'no'), ('When bored', 'no'),
          ('Only on Friday afternoons', 'no'), 'More care for higher stakes.'),
        Q('The AI tool is like whom in the picture?', 'The student writing a quick draft', ('The teacher', 'no'), ('The principal of the whole school', 'no'),
          ('The parent', 'no'), 'It drafts.'),
    ], why='A learner who misses MAIN may skip review; a teacher grading a draft shows who decides.')],
    F1=sec('Apply it: set approval rules', HUMAN, [
        Q('A shop uses AI to draft replies to reviews. Which rule fits?', 'The owner approves each reply before posting',
          ('Replies post automatically with no review', 'risky'), ('Replies are never posted', 'too strict'),
          ('Customers approve the replies', 'not their role'), 'Approve public replies.'),
        Q('An AI tool suggests raising all prices 25 percent. What should happen?', 'The owner reviews the reasoning and decides',
          ('Prices change automatically', 'risky'), ('The suggestion is ignored without reading', 'wasteful'),
          ('Customers vote on it', 'not their role'), 'Pricing is a business decision.'),
        Q('A refund rule: tool drafts, owner approves. The owner approves 18 of 20 drafts. How many needed changes?', '2',
          ('18', 'approved'), ('20', 'total'), ('38', 'added'), '20 - 18 = 2.', calc=lambda: 20 - 18 == 2),
        Q('Which task can usually run with lighter review?', 'Sorting the owner\'s own notes', ('Sending a contract to a client', 'high stakes'),
          ('Giving tax advice to a customer', 'high stakes'), ('Issuing refunds', 'obligation'), 'Internal, low stakes.'),
        Q('An AI tool screens job applications and ranks them. What should the owner do?', 'Review the applications herself before deciding',
          ('Hire the top-ranked person without reading', 'risky'), ('Reject everyone the tool ranked low without review', 'risky'),
          ('Let the tool send rejection letters unreviewed', 'risky'), 'Hiring decisions need people.'),
    ]),
    F2=sec('Handle the complications: speed pressure and automation creep', HUMAN, [
        Q('A busy owner wants to skip review "just this week." What is the risk?', 'An error could reach customers when no one is checking',
          ('No risk, because tools never make errors during busy weeks', 'not true'), ('Sales double', 'no'), ('Taxes vanish', 'no'), 'Review matters most under pressure.'),
        Q('An automation sends AI-written emails to all customers when stock arrives. What safeguard fits?', 'Approve the template and test it before it goes live',
          ('Let it send anything it writes without review', 'risky'), ('Turn off all emails forever', 'overreaction'), ('Hide it from staff', 'no oversight'),
          'Approve what is automated.'),
        Q('An AI reply promised a customer a refund the policy does not allow. What should the owner do?', 'Decide fairly, honor or explain, and fix the approval step',
          ('Blame the tool and refuse to discuss it with the customer', 'unfair'), ('Ignore the customer', 'harmful'), ('Promise even more', 'worse'),
          'Own the outcome and fix the process.'),
        Q('Reviewing each reply takes 2 minutes and there are 30 replies a week. How long is review each week?', '60 minutes',
          ('30 minutes', 'one minute each'), ('32 minutes', 'added'), ('15 minutes', 'divided'), '30 x 2 = 60.', calc=lambda: 30 * 2 == 60),
        Q('Which statement is accurate?', 'Customer-facing or binding actions need a person\'s approval.',
          ('Tools may sign contracts alone.', 'not appropriate'), ('Human review is only needed for large businesses with staff.', 'all benefit'),
          ('High stakes need less review.', 'opposite'), 'People decide what matters.'),
    ]))

# ------------------------------------------------------------------ Set 102: measuring benefit and choosing tools
BENEFIT = ('A tool is worth using only if it helps. MEASURE the benefit: time saved, errors reduced, or sales gained, '
           'compared with the cost (subscription price plus time spent learning and checking). Example: a 20-dollar-a-month '
           'tool that saves 3 hours a month is worth it if your time is worth more than about 6.67 dollars an hour. Try a '
           'tool on one task first, compare before and after, and drop tools that do not help. Check terms, data handling '
           'and whether you can export your work.')

s102 = SET('ENT.AI.06',
    M=sec('Measure whether a tool is worth its cost', BENEFIT, [
        Q('Which is a cost of a tool besides its price?', 'Time spent learning and checking its work',
          ('The color of its logo', 'irrelevant'), ('The number of its employees worldwide', 'irrelevant'), ('Its company slogan', 'irrelevant'),
          'Time is a cost.'),
        Q('A 30-dollar-a-month tool saves 5 hours a month. What is the cost per hour saved?', '6 dollars', ('150 dollars', 'multiplied'),
          ('25 dollars', 'subtracted'), ('0.17 dollars', 'reversed'), '30 / 5 = 6.', calc=lambda: 30 / 5 == 6),
        Q('How should a new tool be tried first?', 'On one task, comparing before and after', ('On every task at once with no measuring', 'unclear'),
          ('Only after paying for a year', 'risky'), ('By reading ads only', 'not a test'), 'Small, measured trial.'),
        Q('What should happen to a tool that does not help?', 'Drop it', ('Keep paying forever', 'waste'), ('Buy a second copy', 'waste'),
          ('Hide it from the budget', 'dishonest'), 'Remove unhelpful costs.'),
        Q('Besides price, what should be checked before choosing?', 'Terms, data handling and export options', ('Only the logo', 'irrelevant'),
          ('Only the website color', 'irrelevant'), ('Only its number of social media followers', 'irrelevant'), 'Fit and risk.'),
    ]),
    B=[mathb('Cost per hour saved', 'To judge a tool, divide its monthly cost by the hours it saves each month. Example: 24 '
             'dollars / 4 hours saved = 6 dollars per hour saved. If your time is worth more than that per hour, the tool '
             'pays off. Include checking time: if the tool saves 4 hours but checking takes 1 hour, the net saving is 3 hours, '
             'so 24 / 3 = 8 dollars per hour saved.', [
        Q('20 dollars a month saves 4 hours. What is the cost per hour saved?', '5 dollars', ('80 dollars', 'multiplied'),
          ('16 dollars', 'subtracted'), ('0.20 dollars', 'reversed'), '20 / 4 = 5.', calc=lambda: 20 / 4 == 5),
        Q('A tool saves 6 hours but checking takes 2. What is the net saving?', '4 hours', ('8 hours', 'added'), ('6 hours', 'ignored checking'),
          ('2 hours', 'checking only'), '6 - 2 = 4.', calc=lambda: 6 - 2 == 4),
        Q('36 dollars a month with a 4-hour net saving. What is the cost per hour saved?', '9 dollars', ('144 dollars', 'multiplied'),
          ('32 dollars', 'subtracted'), ('4 dollars', 'hours'), '36 / 4 = 9.', calc=lambda: 36 / 4 == 9),
        Q('If time is worth 15 dollars an hour and the cost per hour saved is 9 dollars, does the tool pay off?', 'Yes',
          ('No', '9 < 15'), ('Cannot tell', 'can tell'), ('Only on weekends', 'no'), '9 < 15.', calc=lambda: 9 < 15),
        Q('Why include checking time?', 'It reduces the real time saved', ('It increases the time saved', 'opposite'),
          ('It makes the tool free', 'no'), ('It does not matter', 'it does'), 'Net savings are what count.'),
    ], why='A learner who misses MAIN may not compute whether a tool pays off; this practices cost per hour saved.')],
    F1=sec('Apply it: compare tools with real numbers', BENEFIT, [
        Q('Tool A costs 15 dollars and saves a net 3 hours a month. Tool B costs 40 dollars and saves a net 5 hours. Which costs less '
          'per hour saved?', 'A, at 5 dollars per hour', ('B, at 8 dollars per hour', 'B is higher'), ('They are equal', 'differ'),
          ('B, at 5 dollars per hour', 'miscalculated'), 'A: 15/3 = 5; B: 40/5 = 8.', calc=lambda: 15 / 3 == 5 and 40 / 5 == 8),
        Q('Before a tool, invoices took 4 hours a month with 6 errors. After, 2 hours with 1 error. How many errors were avoided?', '5',
          ('6', 'before'), ('1', 'after'), ('7', 'added'), '6 - 1 = 5.', calc=lambda: 6 - 1 == 5),
        Q('A tool claims to "save 20 hours a week," but the owner measured 1 hour. What should she rely on?', 'Her own measurement',
          ('The tool\'s advertisement', 'unverified'), ('A guess halfway between', 'not measured'), ('Nothing', 'she has data'),
          'Measure for yourself.'),
        Q('Three tools cost 12, 18 and 25 dollars a month. The owner uses only the 18-dollar one. How much could she save each month by '
          'dropping the others?', '37 dollars', ('55 dollars', 'all three'), ('18 dollars', 'the one used'), ('43 dollars', 'miscalculated'),
          '12 + 25 = 37.', calc=lambda: 12 + 25 == 37),
        Q('A tool helps a lot but cannot export the owner\'s work. What risk should she weigh?', 'Being stuck if the tool changes or closes',
          ('No risk, because tools never change or close', 'they can'), ('Faster work forever', 'not guaranteed'), ('Lower taxes', 'irrelevant'),
          'Lock-in risk.'),
    ]),
    F2=sec('Handle the complications: hidden costs and hype', BENEFIT, [
        Q('A "free" tool requires 3 hours of fixing its errors each week. What is its real cost?', 'The owner\'s time spent fixing errors',
          ('Nothing, because free means no cost', 'time costs'), ('Only its logo', 'irrelevant'), ('Only electricity', 'minor'), 'Time is a cost.'),
        Q('A tool\'s price rises from 10 to 25 dollars a month. It saves a net 2 hours. What is the new cost per hour saved?', '12.50 dollars',
          ('5.00 dollars', 'old price'), ('25.00 dollars', 'price'), ('50.00 dollars', 'multiplied'), '25 / 2 = 12.50.',
          calc=lambda: 25 / 2 == 12.5),
        Q('Everyone online says a new tool is "a must." The owner\'s trial showed no benefit. What should she do?', 'Trust her trial results',
          ('Buy it because everyone says so', 'not evidence'), ('Buy three of them', 'waste'), ('Ignore her own data', 'not wise'),
          'Evidence over hype.'),
        Q('A tool saves time but its terms allow using her client data for training. Her contract forbids sharing client data. What fits?',
          'Do not use it for client data', ('Use it anyway', 'breaks contract'), ('Hide it from clients', 'dishonest'),
          ('Ask the tool to promise privacy', 'not enough'), 'Terms and contracts win.'),
        Q('Which statement is accurate?', 'A tool is worth keeping only if measured benefits exceed its full costs.',
          ('Every popular tool pays off.', 'not always'), ('Free tools have no costs.', 'time costs'),
          ('Measuring a tool\'s benefit is impossible for a small business.', 'it is possible'), 'Measure and decide.'),
    ]))

# ------------------------------------------------------------------ Set 103: no fake testimonials or false claims
FALSE = ('AI makes it easy to create text and images, which makes it easy to deceive by accident or on purpose. Never use '
         'AI to invent customer testimonials or reviews, create fake "before and after" photos, imply endorsements that '
         'did not happen, or make claims you cannot support, such as "clinically proven" or "number one in the state." '
         'The FTC treats fake reviews and testimonials as deceptive. Use AI to draft honest descriptions of what your '
         'product actually does, and label AI-generated images where it would affect a buyer\'s decision.')

s103 = SET('ENT.AI.07',
    M=sec('Avoid fake testimonials and unsupported claims made with AI', FALSE, [
        Q('Which use of AI is deceptive?', 'Inventing customer testimonials', ('Drafting an honest product description', 'honest'),
          ('Summarizing real customer feedback accurately', 'honest'), ('Fixing grammar in a real review with permission', 'minor edit'),
          'Invented testimonials deceive.'),
        Q('Which claim needs support before it is used?', '"Clinically proven to reduce wrinkles"', ('"Made with lavender oil"', 'factual if true'),
          ('"Ships in 3 business days by mail"', 'factual if true'), ('"Available in 4 colors"', 'factual if true'), 'Strong claims need evidence.'),
        Q('What does the FTC say about fake reviews and testimonials?', 'They are deceptive', ('They are fine if positive', 'not true'),
          ('They are required for new businesses', 'not true'), ('They are allowed if AI writes them', 'not true'), 'Fake endorsements deceive.'),
        Q('When should an AI-generated image be labeled?', 'When it would affect a buyer\'s decision', ('Never, under any circumstances at all', 'can mislead'),
          ('Only if it is blue', 'irrelevant'), ('Only on weekends', 'irrelevant'), 'Avoid misleading buyers.'),
        Q('What is a good use of AI here?', 'Drafting honest descriptions of what the product does', ('Creating fake before-and-after photos of results', 'deceptive'),
          ('Implying a celebrity endorsement', 'deceptive'), ('Inventing awards', 'deceptive'), 'Honest drafting.'),
    ]),
    B=[cs('A photo filter on a used-car ad', 'Imagine a used-car ad where the seller edits out the dents and rust. Buyers drive '
          'over, see the real car and feel cheated. AI can make that kind of edit in seconds. The rule stays the same as '
          'before AI: show the product as it really is and say only what you can back up.', [
        Q('Editing dents out of a car photo is what?', 'Misleading buyers', ('Honest marketing', 'no'), ('Required by law', 'no'),
          ('A free repair', 'no'), 'It hides the truth.'),
        Q('How do buyers feel when they see the real car?', 'Cheated', ('Delighted', 'no'), ('Grateful', 'no'), ('Indifferent', 'no'),
          'Deception damages trust.'),
        Q('Does AI change the honesty rule?', 'No, the same rule applies', ('Yes, AI edits are always allowed', 'no'),
          ('Yes, rules vanish online', 'no'), ('Only for cars', 'no'), 'Honesty still applies.'),
        Q('What should a product photo show?', 'The product as it really is', ('An imagined better version', 'misleading'),
          ('A competitor\'s product', 'misleading'), ('Nothing', 'no'), 'Truthful images.'),
        Q('What should a claim be?', 'Something you can back up', ('As exciting as possible', 'not the test'), ('Made up if needed', 'no'),
          ('Copied from rivals', 'no'), 'Supportable claims.'),
    ], why='A learner who misses MAIN may think AI changes the rules; an edited used-car photo shows the same old deception.')],
    F1=sec('Apply it: clean up AI-made marketing', FALSE, [
        Q('An AI draft for a candle shop includes "Loved by 50,000 customers," but the shop has 600. What should the owner do?',
          'Replace it with a true statement or remove it', ('Keep it, because big numbers sound good', 'false'), ('Change it to 40,000', 'still false'),
          ('Add "approximately"', 'still false'), 'Claims must be true.'),
        Q('An AI image shows a cake far more elaborate than the bakery makes. What should the owner use instead?', 'Photos of cakes the bakery actually made',
          ('The AI image, without any label on it', 'misleading'), ('A competitor\'s cake photo', 'misleading'), ('No photos ever', 'unnecessary'),
          'Real examples.'),
        Q('A draft says "Number one plumber in the state." The owner has no ranking data. What should she write instead?', '"Licensed, 8 years serving Eastfield"',
          ('Keep "number one" because many plumbers say it', 'unsupported'), ('Write "number one in the country"', 'worse'),
          ('Write "best ever" in capitals', 'unsupported'), 'Specific and true.'),
        Q('A shop has 12 real reviews. An AI tool offers to write 30 more. If it did, what fraction of all reviews would be fake?', '30/42',
          ('12/42', 'real share'), ('30/12', 'not a fraction of total'), ('12/30', 'not the fraction'), '30 fake of 42 total.',
          calc=lambda: 30 / (12 + 30) == 30 / 42),
        Q('Which use of AI with real reviews is honest?', 'Summarizing common themes from real reviews accurately', ('Rewriting them to sound more positive', 'altered'),
          ('Adding fake names to them', 'deceptive'), ('Inventing extra reviews in the same style as the real ones', 'deceptive'), 'Accurate summary.'),
    ]),
    F2=sec('Handle the complications: gray areas and pressure', FALSE, [
        Q('A competitor uses AI-made testimonials and seems to sell more. What should the owner do?', 'Stay honest and build real reviews',
          ('Copy the competitor\'s tactic to keep up', 'deceptive'), ('Write even more fake reviews', 'worse'), ('Buy reviews instead', 'deceptive'),
          'Do not join deception.'),
        Q('A "sample testimonial" written by AI is placed on the site as a design placeholder and forgotten. What is the risk?', 'Visitors may think it is a real customer',
          ('No risk; placeholders are invisible', 'they are visible'), ('It improves trust', 'it misleads'), ('It is required', 'no'),
          'Remove placeholders before launch.'),
        Q('A product claim was true last year but the formula changed. What should the owner do?', 'Update or remove the claim',
          ('Keep it; it was true once', 'now false'), ('Make the claim stronger', 'worse'), ('Hide the formula change', 'dishonest'),
          'Claims must stay accurate.'),
        Q('An AI tool suggests saying a product is "FDA approved," but it is not. What should the owner do?', 'Not make the claim',
          ('Make it in small print', 'still false'), ('Make it only on social media', 'still false'), ('Ask the AI again', 'still false'),
          'False regulatory claims are serious.'),
        Q('Which statement is accurate?', 'With or without AI, claims must be real and supportable.',
          ('AI-written reviews are acceptable as long as they sound realistic.', 'deceptive'), ('Claims need no support online.', 'they do'),
          ('Images never mislead.', 'they can'), 'Honesty rule stands.'),
    ]))

SETS = [s97, s98, s99, s100, s101, s102, s103]
