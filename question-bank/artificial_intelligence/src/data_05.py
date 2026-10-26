"""Foundation 5: Checking results (AI.CHECK.01-10)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.CHECK.01
HAL = ('A HALLUCINATION is AI output that is false or unsupported but presented as if it were true: a made-up quote, '
       'a statistic with no source, a nonexistent book, a wrong date stated confidently. It happens because a language '
       'model generates likely-sounding text rather than looking facts up, so when it lacks the right information it '
       'can still produce something that fits the pattern of an answer. Hallucinations are more likely with obscure '
       'topics, very specific details (exact numbers, names, dates, page numbers) and questions about recent events. '
       'They are not lies in the human sense; they are errors.')
HAL_F2 = ('You cannot spot every hallucination by reading carefully, because invented details often look exactly like '
          'real ones. Some practical defenses: give the tool reliable source material to work from, ask it to say '
          '"I don\'t know" when the material does not contain an answer, and check specific details that matter in an '
          'independent source. Tools that search the web or cite documents reduce some hallucinations but can still '
          'misread or misquote sources. The habit that always helps is the same: verify the claims you will rely on.')

HAL_EX = PR('What did the scientist Dr. Lena Varga say about bees in her 2019 speech?',
            'In her 2019 speech in Vienna, Dr. Lena Varga said, "Every third bite of food we eat depends on a bee," and '
            'called for a ban on certain pesticides.')

S_CHECK01 = SET(
    'AI.CHECK.01',
    M=sec('Recognize a hallucination and why it happens', HAL, [
        Q('What is a hallucination in AI output?', 'False or unsupported output stated as true',
          ('A blurry image shown on a screen', 'not this meaning'),
          ('A deliberate lie the tool chose to tell', 'errors, not lies'),
          ('An answer that is slow to arrive', 'speed is unrelated'),
          'Confident but false or unsupported output.'),
        Q('Why do language models hallucinate?',
          'They generate likely text instead of looking it up',
          ('They are told to deceive users', 'not deliberate'), ('They copy only from websites full of false facts', 'not the cause'),
          ('They never learned any language', 'they did'),
          'Pattern-fitting text can be false.'),
        Q('Which request is most likely to produce a hallucination?', 'The exact page number of an obscure quote',
          ('A list of synonyms for "happy"', 'low risk'),
          ('A rhyming poem about the ocean', 'creative, low factual risk'),
          ('A friendlier rewording of your note', 'low factual risk'),
          'Specific details on obscure topics are risky.'),
        Q('In this fictional example (the scientist and speech are invented for this question), what should a reader do?',
          'Find a real record of the speech before using it',
          ('Quote it, since it includes a city and year', 'details are not proof'),
          ('Assume the quote is real since it is specific', 'specificity is not proof'),
          ('Ask the same tool if the quote is real', 'not an independent check'),
          'Verify quotes in a reliable record.', ex=HAL_EX),
        Q('Are hallucinations lies?', 'No; they are errors, not deliberate deception',
          ('Yes; the tool knows the truth and hides it', 'it is not deliberate'),
          ('Yes; they are always made on purpose', 'not on purpose'),
          ('No; they are always correct', 'they are false or unsupported'),
          'They are errors from how text is generated.'),
    ]),
    B=[cs('Compare hallucination with a confident guesser at trivia night',
          'At a trivia night, one teammate never says "I don\'t know." Asked the year a small town was founded, he says '
          '"1847" with total confidence. He is not lying on purpose; he just produces an answer that sounds right. '
          'Sometimes he is correct, sometimes not, and his tone is the same either way. A language model can act like '
          'this teammate. When it lacks the right information, it may still produce a confident, specific answer. '
          'That confident wrong answer is what people call a hallucination.', [
              Q('What does the teammate never say?', '"I don\'t know"',
                ('"1847"', 'he says that'), ('"Let\'s check"', 'he does not check'), ('"Good question"', 'not mentioned'),
                'He always gives an answer.'),
              Q('Is the teammate lying on purpose?', 'No, he gives answers that sound right',
                ('Yes, he wants to trick the team', 'not deliberate'), ('Yes, he knows the truth', 'he does not'),
                ('No, he is always correct', 'sometimes wrong'), 'Confident guessing, not lying.'),
              Q('How does his tone differ when he is wrong?',
          'It does not; he sounds the same',
          ('He sounds nervous', 'not described'), ('He whispers', 'not described'),
          ('He apologizes before every wrong answer', 'not described'),
          'Tone gives no clue.'),
              Q('A confident, specific, wrong AI answer is called what?', 'A hallucination',
                ('A citation', 'not this'), ('A token', 'not this'), ('A prompt', 'not this'),
                'That is the term.'),
              Q("What would make the teammate's answer trustworthy?",
          'Checking it in a reliable source',
          ('Saying it louder', 'volume is not evidence'), ('Saying it faster', 'speed is not evidence'),
          ('Adding more digits to the year he says', 'precision is not evidence'),
          'Verification makes it trustworthy.'),
          ], why='A learner who thinks confident answers must be correct can see a hallucination through a familiar '
                 'confident guesser.')],
    F1=sec('Spot likely hallucinations in practical answers', HAL, [
        Q('A model lists five books by a little-known local author, but the library has only two of them. What is the '
          'most likely explanation?',
          'Some of the titles may be hallucinated',
          ('The library must be hiding three books', 'unsupported'),
          ('The author secretly wrote three more books', 'unsupported'),
          ('Libraries never have complete lists', 'too broad'),
          'Obscure topics invite invented details.'),
        Q('Which part of an answer about a historical battle deserves the closest check?', 'The exact casualty numbers',
          ('The general idea that a battle happened', 'well-documented'),
          ('The friendly summary sentence', 'not a factual detail'),
          ('The paragraph breaks', 'formatting'),
          'Specific numbers are a common hallucination spot.'),
        Q('A student asks about an event from last week and gets a detailed answer. What should she suspect?',
          'Details may be invented if it lacked current information',
          ('The answer must be verified already', 'not unless sources are shown'), ('Recent events are always answered correctly by tools', 'not true'),
          ('The tool watched the event live', 'not how it works'),
          'Recent events raise hallucination risk.'),
        Q('A model gives a quote "from" a famous speech. What is the best check?', 'Find the speech transcript',
          ('Ask the model to add quotation marks', 'formatting is not proof'),
          ('Search for the quote on a meme page', 'not reliable'),
          ('Trust it because it sounds like the speaker', 'imitation is easy'),
          'Primary records confirm quotes.'),
        Q('Which request is LEAST likely to be harmed by a hallucination?', 'Ideas for a fantasy story plot',
          ('The dosage on a medicine label', 'high stakes'),
          ('A company\'s exact refund policy', 'needs accuracy'),
          ('A court case citation for a report', 'needs accuracy'),
          'Invented content is fine in fiction.'),
    ]),
    F2=sec('Reduce and catch hallucinations', HAL_F2, [
        Q('Why can careful reading alone not catch every hallucination?', 'Invented details can look like real ones',
          ('Hallucinations are always in red text', 'they are not marked'),
          ('Reading carefully makes errors appear', 'not true'),
          ('Hallucinations only appear in images', 'they appear in text'),
          'Checking needs outside evidence.'),
        Q('Which instruction helps reduce hallucinations when using supplied material?',
          '"If the text does not say, answer \'I don\'t know.\'"',
          ('"Always give a complete answer, no matter what."', 'encourages guessing'),
          ('"Sound as certain as possible."', 'encourages confident errors'),
          ('"Add extra details to be helpful."', 'invites invention'),
          'Allowing "I don\'t know" reduces invented answers.'),
        Q('A tool that searches the web cites a page but misstates what it says. What does this show?',
          'Search-based tools can still misread sources',
          ('Search-based tools never make any errors at all', 'they can'), ('The web page must be wrong', 'not shown'),
          ('Citations always prove accuracy', 'not true'),
          'Retrieval reduces but does not remove errors.'),
        Q('What habit always helps against hallucinations?', 'Verify claims you will rely on',
          ('Ask for longer answers', 'length is not accuracy'),
          ('Use a friendlier tone in requests', 'tone is not accuracy'),
          ('Trust answers that include dates', 'dates can be invented'),
          'Verification is the reliable defense.'),
        Q('A report draft from a tool has ten facts. You have time to check only three. Which three?',
          "The ones the report's conclusions depend on",
          ('The first three facts that appear in the report', 'position is not importance'), ('The three shortest sentences', 'length is not importance'),
          ('The three you already believe', 'confirmation bias'),
          'Check the claims that matter most.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.02
CITE = ('Citations can be wrong in two different ways. An INVENTED citation points to a source that does not exist: a '
        'made-up article, a fake court case, a book with the wrong author. A MISMATCHED citation points to a real '
        'source that does NOT support the claim: the article exists, but it says something different, or nothing on '
        'the topic. To check, first confirm the source exists (search a library catalog, an official database or the '
        'publisher\'s site), then open it and find the passage that supports the exact claim. In 2023 a federal court in '
        'New York sanctioned lawyers who filed court cases invented by a chatbot without checking them.')
CITE_F2 = ('Checking a citation means comparing the claim with what the source actually says. Watch for small shifts: '
           'a study about adults cited for children, a 2015 figure presented as current, a "may help" turned into '
           '"cures," or one example presented as a general rule. Also notice WHO the source is: a press release, an '
           'opinion piece or an unknown website is weaker support than an original study or an official record. If '
           'you cannot find the supporting passage, treat the claim as unsupported, even if the source is real and '
           'reputable.')

CITE_EX = PR('Does drinking green tea improve memory? Include a source.',
             'Yes. Drinking two cups of green tea a day strongly improves memory in adults (Kim and Ortiz, Journal of '
             'Everyday Nutrition, 2018, vol. 12, pp. 44-51).')

S_CHECK02 = SET(
    'AI.CHECK.02',
    M=sec('Check whether a citation exists and supports the claim', CITE, [
        Q('What is an invented citation?', 'A reference to a source that does not exist',
          ('A real source that disagrees with the claim', 'that is a mismatched citation'),
          ('A source written by a famous scientist', 'not the definition'),
          ('A source that is more than ten years old', 'age is not invention'),
          'Invented means the source is not real.'),
        Q('What is a mismatched citation?',
          'A real source that does not support the claim',
          ('A source that does not exist anywhere at all', 'that is invented'), ('A source in a different language', 'not the definition'),
          ('A source with a long title', 'not the definition'),
          'Real source, wrong support.'),
        Q('In this fictional example, what are the two checks to make, in order?',
          'Confirm the article exists, then find the supporting passage',
          ('Count the pages listed, then trust the claim if they add up', 'counting pages checks nothing'), ('Check the font, then check the year', 'not meaningful checks'),
          ('Ask the tool again, then accept it', 'not independent'),
          'Existence first, then support.',
          ex=CITE_EX),
        Q('Where is a good place to confirm that a published article exists?',
          "A library catalog or the publisher's site",
          ('The same chatbot that cited it', 'not independent'), ('A social media comment thread', 'not reliable'),
          ('Your memory of similar articles you have read', 'not a check'),
          'Use catalogs and publisher records.'),
        Q('What happened in the 2023 federal court case described in the passage?',
          'Lawyers were sanctioned for filing unchecked invented cases',
          ('A chatbot was put on trial for lying', 'not what happened'), ('The court ruled that chatbot research is always reliable', 'the opposite'),
          ('Lawyers won by citing more cases', 'not what happened'),
          'Unverified invented citations led to sanctions.'),
    ]),
    B=[sk('Separate an assertion from a supporting source',
          'An ASSERTION is a statement that something is true: "Bananas are the most popular fruit." A SUPPORTING '
          'SOURCE is something you can open that shows evidence for it: a survey report with the numbers. Words like '
          '"according to experts" or "research shows" are part of the assertion, not a source, unless they name '
          'something specific you can find. To separate them, ask: "Is there a specific document or record named here '
          'that I could open?" If not, you only have an assertion.', [
              Q('Which is a supporting source?',
          'A named survey report you can open',
          ('"Research shows it clearly"', 'unnamed'), ('"Experts agree on this point"', 'unnamed'),
          ('"It is well known by everyone"', 'unnamed'),
          'A specific document can be opened.'),
              Q('"According to experts, cats sleep 15 hours a day." What do you have?',
          'An assertion with no source',
          ('A verified fact', 'nothing to open'), ('A primary source', 'no document'),
          ('An official record of the fact', 'no record'),
          'Unnamed experts are not a source.'),
              Q('Which question separates an assertion from a source?',
          '"Is a specific document named here?"',
          ('"Does it sound true?"', 'not a test'), ('"Is it long?"', 'not a test'),
          ('"Is it written formally and politely?"', 'not a test'),
          'Look for something openable.'),
              Q('"The city budget report, page 4, lists the parks budget." What is this?', 'A specific source to check',
                ('An assertion with no source', 'a document is named'), ('A rumor', 'not a rumor'),
                ('An opinion', 'a factual pointer'), 'A named report and page.'),
              Q('Is "research shows" a source by itself?',
          'No, unless it names research you can find',
          ('Yes, always', 'it is vague'), ('Yes, if said confidently', 'confidence is not a source'),
          ('No, research is never useful for anything', 'research can be useful'),
          'Vague phrases are not sources.'),
          ], why='A learner who cannot check citations often cannot yet tell a claim from a source; this branch '
                 'practices that underlying skill.')],
    F1=sec('Compare a response with a supplied source excerpt', CITE, [
        Q('An answer says, "The study found the program cut costs by 40 percent." The study\'s summary says "costs fell 14 percent." What is wrong?',
          'The citation is mismatched: the number is wrong',
          ('Nothing; 40 and 14 use the same two digits anyway', 'different numbers'), ('The study must not exist', 'it exists'),
          ('Both numbers are equally correct', 'they conflict'),
          'The source does not support 40 percent.'),
        Q('A response cites a court case. You search the official court database and find nothing. What should you '
          'conclude?',
          'The case may be invented; do not rely on it',
          ('The database must be incomplete for every case', 'unsupported'),
          ('Use it anyway, since it sounds legal', 'unsafe'),
          ('The case is real but secret', 'unsupported'),
          'An unfound citation is likely invented.'),
        Q('Source excerpt: "Students who slept 8 hours scored slightly higher." Response: "Sleep doubles test scores." '
          'What should you do?',
          'Reject the claim; the source says slightly higher',
          ('Accept it, since the source mentions sleep', 'topic match is not support'),
          ('Accept it, since doubling is "higher"', 'overstated'),
          ('Ignore the source excerpt', 'it is the evidence'),
          'The claim exaggerates the source.'),
        Q('A real, reputable website is cited, but you cannot find the claimed fact on the page. What is the right '
          'conclusion?',
          'Treat the claim as unsupported until you find it',
          ('Accept it because the website is reputable', 'reputation is not support'),
          ('Assume the fact is on another page', 'unverified'),
          ('Report the website as fake', 'the site is real'),
          'Support must be found, not assumed.'),
        Q('Which check comes first for an unfamiliar citation?', 'Confirm the source exists',
          ('Decide whether you like its conclusion', 'bias'),
          ('Count how many times it is cited', 'not first'),
          ('Check whether the author sounds smart', 'not a check'),
          'Existence before support.'),
    ]),
    F2=sec('Catch citations that exist but do not support the claim', CITE_F2, [
        Q('A source studied adults, but the answer cites it for a claim about children. What is the problem?',
          'The source does not support claims about children',
          ('None; adults and children respond the same way', 'they differ'), ('The source must be invented', 'it exists'),
          ('Studies about adults are always wrong', 'not true'),
          'The population shifted.'),
        Q('A study says a supplement "may help some people sleep." The answer says it "cures insomnia." What happened?',
          'A careful claim became an overstatement',
          ('The answer quoted the study exactly', 'it did not'), ('"May help" and "cures" mean the same', 'they differ'),
          ('The study must have been updated', 'unsupported'),
          'Watch for strengthened claims.'),
        Q('An answer cites a 2015 statistic as "today\'s rate." What should you do?',
          'Look for a current figure before using it',
          ('Use it, since statistics never change', 'they often change'),
          ('Delete the citation and keep the claim', 'removes evidence'),
          ('Assume 2015 is close enough always', 'not necessarily'),
          'Dates matter when claims are current.'),
        Q('Which source gives the strongest support for a medical claim?', 'The original peer-reviewed study',
          ('A press release about the study', 'weaker support'),
          ('An anonymous blog post', 'weaker support'),
          ('A product advertisement', 'weaker support'),
          'Original research is stronger support.'),
        Q('A real, reputable source is cited, but its passage only mentions one example, while the answer states a '
          'general rule. What is the best conclusion?',
          'One example does not support a general rule',
          ('A reputable source supports any claim', 'not true'),
          ('One example proves the general rule', 'overgeneralization'),
          ('The source must be fake', 'it is real'),
          'Check the scope of the support.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.03
NUM = ('Language models can make arithmetic and counting mistakes, sometimes inside an otherwise good answer. A total '
       'may not match its parts, a percentage may be calculated from the wrong base, units may be mixed (minutes and '
       'hours), or a rounded number may be treated as exact. When a number matters, CHECK IT: redo simple arithmetic '
       'yourself or with a calculator, ESTIMATE whether the size makes sense ("a month of groceries for 1,000 dollars '
       'is plausible; 100,000 is not"), and confirm that units match. Some products can run a calculation tool, but you '
       'should still check results that matter.')
NUM_F2 = ('Number errors often hide in multi-step answers: one wrong step early on makes every later number wrong while '
          'the reasoning still looks tidy. Check the inputs first (did it use your actual figures?), then each step, '
          'then the final number. Watch percentage traps: a 50 percent rise followed by a 50 percent fall does not return '
          'to the start. And be careful with very precise-looking results from uncertain inputs: "12.37 percent" built '
          'on a guessed number is still a guess.')

NUM_EX = PR('I bought 3 notebooks at 4.50 dollars each and 2 pens at 1.25 dollars each. What is the total?',
            'Notebooks: 3 x 4.50 = 13.50 dollars. Pens: 2 x 1.25 = 2.50 dollars. Total: 13.50 + 2.50 = 17.00 dollars.')

S_CHECK03 = SET(
    'AI.CHECK.03',
    M=sec('Recalculate or estimate numbers before relying on them', NUM, [
        Q('In this fictional example, what is the correct total?', '16.00 dollars',
          ('17.00 dollars', 'the response added wrong'), ('15.50 dollars', 'dropped the pens'),
          ('13.50 dollars', 'notebooks only'),
          '13.50 + 2.50 = 16.00.', calc=lambda: 3 * 4.50 + 2 * 1.25 == 16.00, ex=NUM_EX),
        Q('In the same example, which step was wrong?', 'Adding 13.50 and 2.50',
          ('Multiplying 3 by 4.50', 'that was correct'), ('Multiplying 2 by 1.25', 'that was correct'),
          ('Listing the items bought', 'that was correct'),
          'Each product was right; the sum was wrong.', calc=lambda: 13.50 + 2.50 == 16.00, ex=NUM_EX),
        Q('A tool says a family\'s groceries for one month cost 95,000 dollars. What does estimation suggest?',
          'The number is implausibly large; recheck it',
          ('The number is fine since it is precise', 'precision is not plausibility'),
          ('All grocery estimates are accurate', 'not true'),
          ('Large numbers are always correct', 'not true'),
          'A sanity check catches it.'),
        Q('An answer adds 90 minutes and 2 hours and says "92 hours." What is the error?', 'It mixed units',
          ('It used too few decimal places', 'not the issue'), ('It rounded too early', 'not the issue'),
          ('Nothing; 90 + 2 is 92', 'units differ'),
          '90 minutes + 2 hours = 3.5 hours.', calc=lambda: 90 / 60 + 2 == 3.5),
        Q('Which is the best way to check a simple sum in an answer?', 'Redo it yourself or with a calculator',
          ('Ask the tool whether it is sure', 'not independent'),
          ('Trust it because the steps are shown', 'shown steps can be wrong'),
          ('Round it to the nearest hundred', 'hides errors'),
          'Independent recalculation.'),
    ]),
    B=[sk('Recalculate and estimate',
          'Two quick skills check most numbers. RECALCULATE: redo the arithmetic yourself, one step at a time. Example: '
          '4 tickets at 7.50 dollars: 4 x 7.50 = 30.00 dollars. ESTIMATE: round the numbers and see if the answer is in '
          'the right range. Example: 19 x 21 is about 20 x 20 = 400, so an answer of 3,990 is clearly wrong. Also check '
          'UNITS: 30 minutes is 0.5 hours, not 30 hours. A wrong unit can make a number look reasonable when it is not.',
          [
              Q('What is 4 x 7.50?', '30.00', ('28.00', 'arithmetic slip'), ('11.50', 'added instead'),
                ('34.00', 'arithmetic slip'), '4 x 7.50 = 30.00.', calc=lambda: 4 * 7.50 == 30.00),
              Q('About how much is 19 x 21?', 'About 400', ('About 40', 'off by ten'), ('About 4,000', 'off by ten'),
                ('About 40,000', 'far off'), '20 x 20 = 400.', calc=lambda: 20 * 20 == 400),
              Q('How many hours is 45 minutes?', '0.75 hours', ('45 hours', 'unit mix-up'), ('4.5 hours', 'wrong conversion'),
                ('0.45 hours', 'decimal error'), '45 / 60 = 0.75.', calc=lambda: 45 / 60 == 0.75),
              Q('An answer says 52 x 10 = 5,200. What does a quick estimate show?', 'It should be about 500',
                ('It is correct', '52 x 10 = 520'), ('It should be about 50', 'too small'),
                ('It should be about 50,000', 'too large'), '52 x 10 = 520.', calc=lambda: 52 * 10 == 520),
              Q('What is 3 x 2.25 + 1.50?', '8.25', ('6.75', 'forgot to add 1.50'), ('7.75', 'arithmetic slip'),
                ('9.00', 'arithmetic slip'), '6.75 + 1.50 = 8.25.', calc=lambda: 3 * 2.25 + 1.50 == 8.25),
          ], why='A learner who misses MAIN may not yet recalculate or estimate confidently; this branch practices the '
                 'arithmetic directly.')],
    F1=sec('Check numbers in practical answers', NUM, [
        Q('A tool says a 25 percent discount on a 80-dollar jacket brings the price to 55 dollars. What is correct?',
          '60 dollars', ('55 dollars', 'took 25 off, not 25 percent'), ('20 dollars', 'that is the discount'),
          ('64 dollars', 'used 20 percent'),
          '80 - 0.25 x 80 = 60.', calc=lambda: 80 - 0.25 * 80 == 60),
        Q('A trip plan says driving 300 miles at about 60 miles per hour takes "about 3 hours." What is correct?',
          'About 5 hours', ('About 3 hours', 'wrong division'), ('About 18 hours', 'multiplied instead'),
          ('About 6 hours', 'arithmetic slip'),
          '300 / 60 = 5 hours.', calc=lambda: 300 / 60 == 5),
        Q('A budget lists rent 900, food 400, transport 150, and says the total is 1,350. What should you do?',
          'Recalculate: the total is 1,450', ('Accept 1,350, since it is close', 'off by 100'),
          ('Change rent to 800 to match', 'changes your real data'), ('Ignore the transport line', 'drops a cost'),
          '900 + 400 + 150 = 1,450.', calc=lambda: 900 + 400 + 150 == 1450),
        Q('A recipe scaled for 8 people says to use 3 eggs, while the original for 4 people uses 2 eggs. What should it '
          'say?',
          '4 eggs', ('3 eggs', 'not doubled'), ('6 eggs', 'tripled'), ('8 eggs', 'one per person'),
          'Doubling 2 eggs gives 4.', calc=lambda: 2 * 8 / 4 == 4),
        Q('An answer says a phone plan of 35 dollars a month costs "about 42 dollars a year." What does estimation show?',
          'It should be about 420 dollars a year', ('It is correct as written', 'off by ten'),
          ('It should be about 4,200 dollars', 'too large'), ('It should be about 35 dollars', 'one month only'),
          '35 x 12 = 420.', calc=lambda: 35 * 12 == 420),
    ]),
    F2=sec('Find errors in multi-step and percentage answers', NUM_F2, [
        Q('A tool computed a project cost in four tidy steps, but used 12 workers instead of your 21. What should you '
          'check first?',
          'Whether it used your actual input figures',
          ('Whether the steps are neatly formatted', 'format is not accuracy'),
          ('Whether the final number is rounded', 'not the first check'),
          ('Whether the answer is long enough', 'irrelevant'),
          'Wrong inputs make every later step wrong.'),
        Q('A price rises 50 percent, then falls 50 percent. A tool says it is "back to the original price." Starting at '
          '100 dollars, what is the final price?',
          '75 dollars', ('100 dollars', 'percentage trap'), ('50 dollars', 'arithmetic slip'), ('125 dollars', 'wrong direction'),
          '100 x 1.5 = 150; 150 x 0.5 = 75.', calc=lambda: 100 * 1.5 * 0.5 == 75),
        Q('A tool reports "12.37 percent growth" based on a guessed starting number. How should you treat it?',
          'As a guess, despite the precise look',
          ('As exact, since it has two decimals', 'precision is not certainty'),
          ('As verified, since it is a percentage', 'not verified'),
          ('As official, since a tool produced it', 'not official'),
          'Precision on guessed inputs is still a guess.'),
        Q('In a multi-step answer, step 2 has an error. What happens to steps 3 and 4?', 'They are likely wrong too',
          ('They fix the error automatically', 'they build on it'),
          ('They are unaffected', 'they depend on step 2'),
          ('They become more accurate', 'no'),
          'Errors carry forward.'),
        Q('A tool says, "Sales went from 200 to 250, a 25 percent increase." Is this right?', 'Yes, 50 is 25 percent of 200',
          ('No, it is a 20 percent increase', 'used 250 as the base'),
          ('No, it is a 50 percent increase', 'confused amount and percent'),
          ('No, it is a 250 percent increase', 'not a percent change'),
          '50 / 200 = 0.25.', calc=lambda: (250 - 200) / 200 == 0.25),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.04
OLD = ('Information can be OUTDATED even when it was once true. A model\'s built-in knowledge stops at its training '
       'cutoff, and sources it retrieves may also be old. Facts that change often include prices, laws and rules, '
       'schedules and opening hours, who holds an office, software features, and records such as "the tallest '
       'building." Clues that an answer may be stale: no date given, words like "currently" or "latest" without a date, '
       'or a source more than a year or two old for a fast-changing topic. To check, find a CURRENT, DATED source, '
       'ideally the organization that controls the fact.')
OLD_F2 = ('Dates on sources need care too. A web page may show "last updated" for a minor edit while its main content '
          'is old, or a news article may describe a plan that later changed. When you find two sources that disagree, '
          'prefer the more recent one from the organization in charge, and check whether something changed between '
          'their dates. For decisions with deadlines, such as applications, travel or taxes, confirm the facts close to '
          'the date you act, because they can change even after you checked.')

S_CHECK04 = SET(
    'AI.CHECK.04',
    M=sec('Spot information that may be out of date', OLD, [
        Q('Which fact is most likely to change over time?', 'A museum\'s ticket price',
          ('The number of days in a week', 'stable'), ('The boiling point of water at sea level', 'stable'),
          ('The spelling of "elephant"', 'stable'),
          'Prices change often.'),
        Q('An answer says "the current mayor is ..." with no date. What should you do?',
          'Check a current, dated official source',
          ('Trust it, since "current" means up to date', 'the word proves nothing'),
          ('Assume mayors never change', 'they do'),
          ('Ask for a longer biography', 'not a check'),
          'Officeholders change; confirm with a dated source.'),
        Q('Which is a clue that an answer may be stale?', '"Latest version" with no date given',
          ('A step-by-step list of instructions', 'not a staleness clue'),
          ('A polite closing sentence', 'not a staleness clue'),
          ('A short and simple answer', 'not a staleness clue'),
          'Undated "latest" claims are a warning sign.'),
        Q('What is the best source for a bus schedule?', 'The transit agency\'s current schedule',
          ('A forum post from three years ago', 'possibly outdated'),
          ('A model\'s answer with no source', 'possibly outdated'),
          ('A friend\'s memory of last summer', 'possibly outdated'),
          'Go to the organization that controls the fact.'),
        Q('Why can retrieved sources be outdated too?', 'The pages themselves may be old',
          ('Retrieval always finds the newest page', 'not guaranteed'),
          ('Search engines update every fact daily', 'pages may still be old'),
          ('Only training data can be outdated', 'sources can be too'),
          'Check the source\'s date.'),
    ]),
    B=[cs('Compare stale information with an old milk carton',
          'A milk carton has a date because milk that was fresh last month may not be good today. Information works '
          'the same way. A store\'s hours, a ticket price or a rule might have been right when it was written but '
          'wrong now. Some information keeps for a long time, like the number of legs on a spider. Other information '
          '"spoils" quickly, like prices and schedules. Before using information that spoils quickly, check its date, '
          'the way you would check the date on milk.', [
              Q('Why does a milk carton have a date?', 'Fresh milk can go bad over time',
                ('To show where it was made', 'not the reason given'), ('To look nice', 'no'),
                ('To set the price', 'no'), 'Dates show freshness.'),
              Q('Which information "spoils" quickly?', 'A store\'s opening hours',
                ('The number of legs on a spider', 'keeps'), ('The color of grass', 'keeps'),
                ('The letters of the alphabet', 'keeps'), 'Hours change.'),
              Q('Which information "keeps" for a long time?',
          'The number of legs on a spider',
          ('A ticket price', 'spoils'), ('A bus schedule', 'spoils'),
          ('A store sale ending date', 'spoils'),
          'Stable facts keep.'),
              Q('Before using quick-spoiling information, what should you check?', 'Its date',
                ('Its font', 'irrelevant'), ('Its length', 'irrelevant'), ('Its color', 'irrelevant'),
                'Like checking milk.'),
              Q('A price was right last year. Is it right today?',
          'Maybe not; check a current source',
          ('Yes, prices always stay the same', 'prices change'), ('No, never', 'too strong'),
          ('Only on national holidays', 'nonsense'),
          'Old correct is not current correct.'),
          ], why='A learner who treats all facts as permanent can see why some information goes stale with a familiar '
                 'expiration-date example.')],
    F1=sec('Check time-sensitive facts in practical answers', OLD, [
        Q('A model says a national park pass costs 70 dollars. Mia is buying one this week. What should she do?',
          "Check the park service's official current price",
          ('Pay exactly 70 dollars at the gate without checking', 'price may have changed'), ('Assume prices drop every year', 'unsupported'),
          ('Use the price from a 2018 blog', 'outdated'),
          'Confirm prices with the official source.'),
        Q("A student uses an answer about a school's application deadline. What is the best check?",
          "The school's admissions page, dated this year",
          ('A cousin who applied to the school five years ago', 'outdated'), ("The model's answer repeated twice", 'not independent'),
          ('A general article about deadlines', 'not specific'),
          'Deadlines change; check the current page.'),
        Q('Which topic most needs a recent source?', 'The features of a phone app',
          ('The plot of a classic novel', 'stable'), ('The rules of basic addition', 'stable'),
          ('The meaning of "photosynthesis"', 'stable'),
          'App features change frequently.'),
        Q('An answer about a tax rule cites a source from six years ago. What should you do?',
          'Look for the current year\'s official guidance',
          ('Use it, since tax rules never change', 'they change'),
          ('Use it, since older sources are more careful', 'not a rule'),
          ('Ignore taxes entirely', 'not an option'),
          'Rules change; check current guidance.'),
        Q('A tool says, "Currently, the tallest building is ..." Why be careful?', 'Records like this can change',
          ('"Currently" guarantees it is up to date', 'it does not'),
          ('Buildings never change height', 'records change'),
          ('Tall buildings are never in the news', 'irrelevant'),
          'Records are time-sensitive.'),
    ]),
    F2=sec('Handle source dates and conflicts carefully', OLD_F2, [
        Q('A page says "last updated this week," but its prices mention an event from three years ago. What should you think?',
          'The edit may be minor; the prices may be old',
          ('Everything on the page must be current now', 'not guaranteed'), ('The event must be happening now', 'unsupported'),
          ('The page must be fake', 'too strong'),
          'An update date does not prove all content is current.'),
        Q('Two sources disagree on a fee. One is the agency\'s page from this year; one is a blog from last year. Which '
          'should you prefer?',
          'The agency\'s page from this year',
          ('The blog, since it is older and established', 'older is not better'),
          ('Whichever number is lower', 'preference is not evidence'),
          ('Average the two fees', 'not a check'),
          'Prefer the recent source from the authority.'),
        Q('A news article describes a city plan to open a library in June. What should you check before going in June?',
          'Whether the plan changed after the article',
          ('Nothing; plans in news always happen', 'plans change'),
          ('Only the article\'s word count', 'irrelevant'),
          ('Whether the article had photos', 'irrelevant'),
          'Plans can change after reporting.'),
        Q('You checked a visa rule a month ago and travel next week. What is wise?', 'Recheck the rule close to your trip',
          ('Rely on last month\'s check forever', 'rules can change'),
          ('Ask a chatbot instead', 'not authoritative'),
          ('Skip checking since you already did', 'risky'),
          'Confirm close to when you act.'),
        Q('A source says a rule "will change next year" and is two years old. What should you suspect?',
          'The change may have already happened',
          ('The rule never changes', 'unsupported'),
          ('The source is current', 'it is two years old'),
          ('Future tense means it is still future', 'time has passed'),
          'Check what happened since.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.05
EVI = ('A CLAIM says something is true. EVIDENCE is what shows it: data, a document, a recording, an observation. '
       'An AI answer is a claim until you connect it to evidence. Sources differ in strength. A PRIMARY SOURCE is the '
       'original: the law\'s text, the study itself, the official schedule, the company\'s own policy. A SECONDARY '
       'SOURCE describes the original: a news story, a summary, a blog. Secondary sources are useful but can '
       'simplify, misquote or go out of date. When accuracy matters, trace a claim back to the primary source if you '
       'can, and notice who benefits if the claim is believed.')
EVI_F2 = ('Primary sources need reading skills too. An official document may contain the answer in a specific section, '
          'with conditions and exceptions, and a summary can drop those. Sometimes no primary source is available, for '
          'example a private conversation; then look for several independent secondary sources and note the '
          'uncertainty. And remember the difference between "no evidence found" and "evidence it is false": not '
          'finding support means the claim is unconfirmed, not disproven.')

S_CHECK05 = SET(
    'AI.CHECK.05',
    M=sec('Tell a claim from evidence and prefer primary sources', EVI, [
        Q('Which is evidence rather than a claim?', 'The official schedule showing the time',
          ('"The bus comes at 8, I am sure."', 'a claim'), ('"Everyone says 8 o\'clock."', 'hearsay'),
          ('"It is definitely at 8."', 'a claim'),
          'A document showing the fact is evidence.'),
        Q("What is a primary source for a city's parking rule?",
          "The city's published parking ordinance",
          ('A news story about the new parking rule', 'secondary'), ("A neighbor's summary of it", 'secondary'),
          ('An AI answer describing it', 'secondary at best'),
          'The original rule text is primary.'),
        Q('Why can secondary sources be less reliable?',
          'They can simplify, misquote or go out of date',
          ('They are always written by computers, not people', 'not true'), ('They are always false', 'too strong'),
          ('They never mention the original', 'often they do'),
          'Summaries can lose accuracy.'),
        Q('An AI answer about a law is what, until you check it?', 'A claim',
          ('Evidence', 'it needs support'), ('A primary source', 'it is not the law\'s text'),
          ('An official record', 'not official'),
          'Answers are claims until connected to evidence.'),
        Q('A company\'s ad says its product is "proven best." What should you also notice?',
          'Who benefits if you believe the claim',
          ('The color of the ad', 'irrelevant'), ('How many words and pictures are in the ad', 'irrelevant'),
          ('The font size', 'irrelevant'),
          'Interest affects how much weight a claim deserves.'),
    ]),
    B=[cs('Compare a rumor with a receipt',
          'Your friend says, "I paid you back yesterday." That is a CLAIM. If your friend shows you the bank RECEIPT '
          'with the date and amount, that is EVIDENCE. The receipt is also a PRIMARY SOURCE: it is the original '
          'record of the payment. If another friend says, "I heard she paid you," that is a SECONDARY account, and it '
          'could be mistaken. When something matters, you look for the receipt, not just the story about it.', [
              Q('"I paid you back yesterday" is what?', 'A claim',
                ('Evidence', 'no record shown'), ('A primary source', 'no record'), ('A receipt', 'no'),
                'It states something without proof.'),
              Q('The bank receipt is what?', 'Evidence and a primary source',
                ('Only a rumor', 'it is a record'), ('A secondary account', 'it is the original'),
                ('A claim with no support', 'it is support'), 'The original record.'),
              Q('"I heard she paid you" is what kind of account?', 'Secondary',
                ('Primary', 'not the original record'), ('Official', 'no'), ('A receipt', 'no'),
                'It describes someone else\'s claim.'),
              Q('When something matters, what should you look for?',
          'The receipt (the original record)',
          ('The loudest story', 'not evidence'), ('The newest rumor', 'not evidence'),
          ('The friendliest version of the story', 'not evidence'),
          'Primary evidence.'),
              Q('Why might the second friend be wrong?', 'They are passing on what they heard',
                ('They have the receipt', 'they do not'), ('They are the bank', 'no'),
                ('Secondary accounts are always right', 'not true'), 'Secondhand accounts can be mistaken.'),
          ], why='A learner who cannot tell claims from evidence can see it in a familiar payment-and-receipt example.')],
    F1=sec('Trace practical claims to evidence', EVI, [
        Q('An AI answer says your school allows phones during lunch. What is the best evidence?',
          'The school\'s published student handbook',
          ('A classmate\'s opinion', 'secondary'), ('The AI answer repeated', 'not evidence'),
          ('A news story about phones in schools', 'not specific'),
          'The school\'s own rule is primary.'),
        Q('A blog says a medicine was "recalled last month." What should you check?',
          'The official recall notice',
          ('More blogs that repeat the same claim', 'not independent'), ("The blog's comment section", 'not reliable'),
          ('How popular the blog is', 'not evidence'),
          'Recalls are announced officially.'),
        Q("Which source is primary for a company's return policy?",
          "The policy page on the company's site",
          ("A review site's summary of the policy", 'secondary'), ('A forum post', 'secondary'),
          ('An AI answer', 'secondary at best'),
          "The company's own policy is primary."),
        Q('A news story summarizes a new law. What should you read for the exact requirements?', 'The law\'s official text',
          ('The headline only', 'too short'), ('Comments on the story', 'not reliable'),
          ('A social media post about it', 'secondary'),
          'Primary text gives exact requirements.'),
        Q('A seller says its charger is "certified safe." What evidence should you look for?',
          'A certification listing you can check',
          ('The seller saying it again, louder', 'not evidence'), ('Five-star reviews only', 'not certification'),
          ('A shiny package', 'not evidence'),
          'Verify certifications with the certifier.'),
    ]),
    F2=sec('Read primary sources and handle missing evidence', EVI_F2, [
        Q('A summary says a scholarship is "open to all students." The official rules say "full-time students only." '
          'What happened?',
          'The summary dropped a condition',
          ('The official rules are wrong', 'primary source wins'),
          ('Both statements say the same thing', 'they differ'),
          ('Scholarships never have conditions', 'not true'),
          'Summaries can drop conditions.'),
        Q('You search for evidence of a claim and find none. What is the correct conclusion?',
          'It is unconfirmed, not disproven',
          ('It is definitely false now', 'no evidence is not disproof'), ('It is definitely true', 'no support'),
          ('It does not matter', 'it may'),
          'Absence of evidence is not evidence of falsehood.'),
        Q('A claim is about a private meeting with no public record. What is a reasonable approach?',
          'Seek independent accounts and note uncertainty',
          ('Accept the first account that you happen to find', 'too hasty'), ('Assume the meeting never happened', 'unsupported'),
          ('Ask an AI tool to decide', 'not evidence'),
          'Use independent sources and be honest about limits.'),
        Q('An official document answers your question in section 4b, with two exceptions. What should you do?',
          'Read the section and its exceptions',
          ('Read only the title page', 'misses details'),
          ('Use the first sentence only', 'misses exceptions'),
          ('Skip it; documents are too long', 'misses the answer'),
          'Details and exceptions matter.'),
        Q('Three websites repeat the same claim, all quoting one anonymous post. How strong is this evidence?',
          'Weak; they share one unverified origin',
          ('Strong; three sites agree', 'not independent'),
          ('Very strong; repetition proves it', 'repetition is not proof'),
          ('Perfect; websites cannot be wrong', 'not true'),
          'Independence matters, not count.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.06
IND = ('An INDEPENDENT CHECK is one that does not rely on the same source of possible error. Asking the same AI tool '
       '"Are you sure?" is not independent: it may simply repeat or rephrase its answer, or apologize and change a '
       'correct answer to a wrong one. Asking a second AI tool is not fully independent either, because tools trained '
       'on similar data can share the same mistakes. Agreement between them is not proof. Independent checks include '
       'the primary source, an official record, your own calculation, a measurement, or a qualified person who checks '
       'the evidence.')
IND_F2 = ('Choosing the right independent check depends on the claim. For a fact, find the record that controls it. '
          'For a calculation, redo it. For code, run tests. For advice, ask someone accountable and qualified. Also '
          'watch for checks that only look independent: three websites copying one source, or a "review" written by '
          'the seller. If the best check is too costly, decide how much the decision matters and say honestly what '
          'remains unverified.')

S_CHECK06 = SET(
    'AI.CHECK.06',
    M=sec('Choose an independent check and avoid false confirmation', IND, [
        Q('Why is asking the same tool "Are you sure?" not an independent check?',
          'It relies on the same source of possible error',
          ('The tool always tells the truth when asked twice', 'not true'),
          ('Asking twice is against the rules', 'nonsense'),
          ('The tool cannot answer that question', 'it can, but it is not a check'),
          'The same source can repeat the same error.'),
        Q('Two different AI tools give the same answer. What does that show?', 'Agreement, not proof',
          ('Proof the answer is correct', 'they can share mistakes'),
          ('Proof both tools are broken', 'not shown'),
          ('That no further check is ever needed', 'not true'),
          'Similar training can produce shared errors.'),
        Q('Which is an independent check of a historical date?',
          'The official record or a reputable reference',
          ('Asking the same chatbot again', 'not independent'), ('Asking it to "double-check itself" carefully', 'not independent'),
          ('Asking a second chatbot', 'not fully independent'),
          'Records are independent of the tool.'),
        Q('A tool changes a correct answer to a wrong one after "Are you sure?" What does this show?',
          'Its reconsidering is not real verification',
          ('The second answer must be right', 'not necessarily'), ('The first answer must be wrong', 'it was correct'),
          ('Questions improve accuracy every time', 'not true'),
          'Asking again is not a check.'),
        Q('Which is an independent check of a calculation in an answer?', 'Redoing it yourself',
          ('Asking the tool to show more steps', 'still the same source'),
          ('Asking for a longer explanation', 'still the same source'),
          ('Asking the tool to be confident', 'not a check'),
          'Your own recalculation is independent.'),
    ]),
    B=[cs('Compare checking with asking a witness to vouch for himself',
          'Imagine someone says he was at the library at noon. If you ask him, "Are you sure?" and he says "Yes," you '
          'have learned nothing new: it is the same person. If his twin brother says, "He was there," that sounds like '
          'confirmation, but the twin may simply repeat what he was told. An INDEPENDENT check would be the library\'s '
          'sign-in sheet or its camera record: evidence that does not depend on the person who made the claim.', [
              Q('Why does "Are you sure?" add little?', 'It asks the same person again',
                ('He will always change his answer', 'not necessarily'), ('He cannot speak', 'no'),
                ('The library is closed', 'irrelevant'), 'Same source, no new evidence.'),
              Q('Why is the twin not a strong check?',
          'He may repeat what he was told',
          ('Twins always lie', 'not true'), ('He is too young', 'not stated'),
          ('He works at the library every day', 'not stated'),
          'Not independent of the claim.'),
              Q('Which is an independent check?', 'The library\'s sign-in sheet',
                ('Asking him a third time', 'same source'), ('Asking his twin again', 'not independent'),
                ('His promise in writing', 'still his claim'), 'A record not controlled by him.'),
              Q('In AI terms, asking a tool "are you sure?" is like what?', 'Asking him "Are you sure?"',
                ('Checking the sign-in sheet', 'that is independent'), ('Checking the camera', 'independent'),
                ('Visiting the library', 'independent'), 'Same source again.'),
              Q('In AI terms, a second tool trained on similar data is most like whom?', 'The twin brother',
                ('The sign-in sheet', 'that is independent'), ('The camera record', 'independent'),
                ('The librarian\'s log', 'independent'), 'Similar sources can share errors.'),
          ], why='A learner who treats "asking again" as checking can see why independence matters through a witness '
                 'example.')],
    F1=sec('Pick independent checks for practical claims', IND, [
        Q('A tool says your flight leaves at 6:40. Which check is independent?', 'The airline\'s app or confirmation email',
          ('Asking the tool again', 'not independent'), ('Asking a second chatbot', 'not fully independent'),
          ('Your memory of last year\'s flight', 'different flight'),
          'The airline controls the fact.'),
        Q('Two chatbots both say a plant is safe for cats. What is the best next step?',
          'Check a veterinary or poison-control source',
          ('Trust it, since two separate tools agree', 'agreement is not proof'), ('Ask a third chatbot', 'still not independent'),
          ('Ask the first one if it is sure', 'not independent'),
          'Pet safety deserves an authoritative check.'),
        Q('A tool converts 5 kilometers to "about 3.1 miles." How can you check independently?',
          'Use a calculator: 5 x 0.621',
          ('Ask the tool to show its work', 'same source'), ('Ask it to convert again', 'same source'),
          ('Trust it', 'not a check'),
          '5 x 0.621 = 3.105.',
          calc=lambda: abs(5 * 0.621 - 3.105) < 1e-9),
        Q('A tool says a word means "brave" in another language. Which check is most independent?',
          'A reputable dictionary for that language',
          ('Asking the tool to use it in a sentence', 'same source'),
          ('Asking a second AI tool', 'not fully independent'),
          ('Asking it to be more certain', 'not a check'),
          'Dictionaries are independent references.'),
        Q('Which statement is accurate?',
          'Agreement between AI tools does not prove it',
          ('Two tools agreeing proves a claim', 'they may share errors'), ('Asking twice doubles the accuracy', 'not true'),
          ("A tool's apology proves that its answer was wrong", 'not necessarily'),
          'Look for evidence outside the tools.'),
    ]),
    F2=sec('Match the check to the claim and spot fake independence', IND_F2, [
        Q('A tool wrote a function that sorts names. What is the best independent check?',
          'Run tests with known inputs and expected outputs',
          ('Ask the tool whether the code is correct', 'same source'),
          ('Read the comments it wrote', 'comments are claims'),
          ('Ask a second tool to praise it', 'not a check'),
          'Tests check code behavior.'),
        Q('A product has five glowing reviews, all posted by the seller\'s own account. How independent are they?',
          'Not independent at all',
          ('Very independent; there are five', 'same source'),
          ('Independent if the reviews are long', 'length is irrelevant'),
          ('Independent if they mention prices', 'irrelevant'),
          'Seller-written reviews are not independent.'),
        Q('A tool gives advice about a lease dispute. Which check is most appropriate?',
          'A qualified, accountable person, such as a lawyer',
          ("Another chatbot's opinion", 'not accountable'), ('A forum post from a renter in another state', 'different rules'),
          ('Asking the tool to cite itself', 'same source'),
          'Advice needs an accountable, qualified check.'),
        Q('Checking a claim fully would take days, and the decision is minor. What is reasonable?',
          'Weigh the stakes and note what is unverified',
          ('Never use the claim at all', 'too strict for minor decisions'), ('Pretend it is fully verified', 'dishonest'),
          ('Ask the tool to verify its own claim carefully', 'not a check'),
          'Match effort to stakes, and be honest.'),
        Q('Three news sites report a statistic, each citing the same press release. What do you really have?',
          'One source repeated three times',
          ('Three independent confirmations', 'same origin'),
          ('Proof the statistic is correct', 'not proof'),
          ('Evidence the press release is false', 'not shown'),
          'Trace sources to their origin.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.07
SUM = ('A summary can go wrong in three ways. OMISSION: it leaves out something important, such as a deadline, a cost '
       'or an exception. DISTORTION: it changes the meaning, such as turning "may" into "will," reversing a finding, '
       'or giving a minor point the main spotlight. ADDITION: it includes a claim that is not in the source at all. To '
       'check a summary, compare it with the original: list the original\'s key points and confirm each appears '
       'accurately, then check that every claim in the summary can be found in the original. Summaries of long '
       'documents deserve extra care.')
SUM_F2 = ('Some omissions matter more than others. A summary of a lease that leaves out the pet policy may be fine '
          'for one reader and a serious problem for another. Decide what YOU need from the document before judging '
          'its summary, and ask for those items explicitly ("include all deadlines, fees and penalties"). Also watch '
          'for balance: a summary of a debate that gives one side three paragraphs and the other one sentence can '
          'mislead even if every sentence is accurate.')

SUM_EX = TABLE([['Original notice (excerpt)', 'Summary'],
                ['The pool closes for repairs from June 3 to June 10. Swim lessons on those dates will be refunded. '
                 'Members must reschedule by May 31.',
                 'The pool will close for repairs in early June, and lessons on those dates will be refunded.']],
               label='Prepared example (a fictional notice and summary)')

S_CHECK07 = SET(
    'AI.CHECK.07',
    M=sec('Compare a summary with its source to find problems', SUM, [
        Q('What is an omission in a summary?', 'Leaving out something important',
          ('Adding a claim not in the source', 'that is an addition'),
          ('Changing "may" to "will"', 'that is a distortion'),
          ('Using shorter sentences', 'not a problem by itself'),
          'An omission leaves something out.'),
        Q('A study says a diet "may lower" blood pressure; the summary says it "will cure" high blood pressure. What '
          'kind of problem is this?',
          'Distortion', ('Omission', 'nothing was left out'), ('Addition', 'it changed an existing claim'),
          ('No problem', 'the meaning changed'),
          'Changing the strength of a claim is distortion.'),
        Q('In this prepared example, what did the summary omit?',
          'The May 31 deadline to reschedule',
          ('The repair closure', 'included'), ('The refund for missed lessons', 'included'),
          ('The month of June', 'included'),
          'The rescheduling deadline is missing.',
          ex=SUM_EX),
        Q('What is the first step in checking a summary?', 'List the original\'s key points',
          ('Count the summary\'s words', 'not a check of content'),
          ('Check the summary\'s font', 'irrelevant'),
          ('Trust it if it reads smoothly', 'smoothness is not accuracy'),
          'Start from the source.'),
        Q('A summary includes "parking is free," which the original never mentions. What kind of problem is this?',
          'Addition', ('Omission', 'something was added, not left out'), ('Distortion', 'not a changed claim'),
          ('No problem', 'unsupported claim'),
          'A claim not in the source is an addition.'),
    ]),
    B=[sk('List key points and match them',
          'Checking a summary is a matching job. First, LIST the key points of the original, such as dates, amounts, '
          'conditions and the main finding. Second, MATCH each one to the summary: present and correct, present but '
          'changed, or missing. Third, REVERSE the check: for each sentence in the summary, find where the original '
          'supports it. Example original: "Tickets cost 12 dollars; children under 5 free; sales end Friday." Key '
          'points: price, child rule, end date.', [
              Q('In the example, how many key points are there?', '3', ('1', 'there are more'), ('2', 'there are more'),
                ('5', 'only three are listed'), 'Price, child rule, end date.'),
              Q('A summary says "Tickets are 12 dollars; sales end Friday." Which key point is missing?',
          'Children under 5 are free',
          ('The price', 'included'), ('The end date', 'included'),
          ('Nothing is missing from it', 'the child rule is'),
          'The child rule is missing.'),
              Q('A summary says "Tickets cost 15 dollars." What is the problem?', 'A key point was changed',
                ('A key point is missing', 'it is present but wrong'), ('Nothing', '15 is not 12'),
                ('It added a new topic', 'same topic, wrong number'), 'Present but changed.'),
              Q('What does the reverse check do?',
          'Finds support in the original for each sentence',
          ("Counts the summary's commas and periods carefully", 'not a check'), ('Reads the summary backward', 'not the meaning'),
          ('Deletes the original', 'no'),
          'It catches additions.'),
              Q('A summary adds "free parking available." Which step catches this?', 'The reverse check',
                ('Listing key points', 'that finds omissions'), ('Counting words', 'no'),
                ('Checking the title', 'no'), 'Additions have no support in the original.'),
          ], why='A learner who cannot find summary errors practices the underlying skill of listing key points and '
                 'matching them both ways.')],
    F1=sec('Check practical summaries', SUM, [
        Q('A summary of a job posting leaves out "must have a driver\'s license." Why does this matter?',
          'An applicant might miss a key requirement',
          ('It does not; requirements are optional', 'they are required'),
          ('Driver\'s licenses are never required', 'this job requires one'),
          ('Summaries must leave out requirements', 'not true'),
          'Omitted requirements can mislead.'),
        Q('A summary says a medicine "is safe for everyone." The leaflet says "not for children under 12." What kind of error is this?',
          'Distortion, plus a missing age limit',
          ('Addition only', 'it changed meaning'), ('No error', 'the meaning changed'),
          ('A spelling error in the leaflet', 'not spelling'),
          'Safety claims were changed.'),
        Q('Raj asks for a summary of a meeting. Which instruction helps prevent omissions?',
          '"Include every decision, owner and deadline."',
          ('"Keep it as short as you possibly can."', 'may drop details'), ('"Make it sound upbeat."', 'tone, not completeness'),
          ('"Use fancy words."', 'not completeness'),
          'Name the items that must appear.'),
        Q('A summary of a study reports the main finding backward. What should you do?',
          'Correct it from the original and recheck the rest',
          ('Keep it, since summaries are only ever approximate', 'reversal is serious'), ('Ask for a longer summary', 'not a fix'),
          ('Assume the study is wrong', 'the summary is wrong'),
          'Reversed findings must be fixed.'),
        Q('A two-sentence summary of a 40-page contract says "standard terms." What is the risk?',
          'Important conditions may be left out',
          ('None; all contracts are standard', 'not true'),
          ('Short summaries are always complete', 'not true'),
          ('The contract must be invalid', 'not implied'),
          'Long documents need careful checking.'),
    ]),
    F2=sec('Judge a summary by your needs and its balance', SUM_F2, [
        Q('A lease summary leaves out the pet policy. Maya has a dog. What should she conclude?',
          'For her it is serious; she should check the lease',
          ('No summary can ever omit anything important', 'they can'), ('Pet policies never matter', 'they matter to her'),
          ('The lease must allow pets', 'not shown'),
          'Importance depends on the reader.'),
        Q("Which request best fits a tenant's needs?",
          '"Summarize, with all fees, deadlines and penalties."',
          ('"Summarize in one sentence."', 'likely drops needs'), ('"Summarize the landlord\'s history and background."', 'not her need'),
          ('"Summarize it as a poem."', 'not useful'),
          'Ask for what you need.'),
        Q('A debate summary gives one side three paragraphs and the other one line. What is the problem?',
          'It can mislead even if each sentence is accurate',
          ('No problem, as long as each sentence is true', 'balance matters'), ('It must be a translation error', 'not implied'),
          ('Longer sides are always correct', 'not true'),
          'Imbalance distorts the picture.'),
        Q('Before judging a summary of a school policy, what should a parent decide?', 'What she needs from the policy',
          ('How long summaries usually are', 'not the key'),
          ('Which font the school uses', 'irrelevant'),
          ('Whether the summary sounds confident', 'not the key'),
          'Needs define which omissions matter.'),
        Q('A summary is accurate but leaves out a fee that applies only to late payments. Who should care most?',
          'Someone likely to pay late',
          ('Someone who never reads policies', 'not the point'),
          ('No one; late fees never apply', 'they may'),
          ('Only the summary writer', 'not the point'),
          'Relevance depends on the reader\'s situation.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.08
GAP = ('Before trusting a conclusion, look for two warning signs. A CONTRADICTION is when two statements cannot both '
       'be true: an answer says a store opens at 9 in one paragraph and 10 in another, or a total does not match its '
       'parts. MISSING INFORMATION is what the conclusion needs but the answer never establishes: a recommendation to '
       'buy a laptop "for school" without knowing the budget, or a claim that a plan is "cheaper" without the prices '
       'of the alternatives. When you spot either, do not just pick the version you prefer; resolve the contradiction '
       'with a source and supply or find the missing facts.')
GAP_F2 = ('Some missing information hides inside assumptions that sound reasonable: "Since you live near the city..." '
          'or "Assuming you work full time..." If the assumption is wrong for you, the conclusion may be wrong too. '
          'Another hidden gap is comparison: "Plan A saves money" needs Plan B\'s cost and the same time period for '
          'both. A good habit is to ask, "What would have to be true for this conclusion to hold?" and then check those '
          'conditions one by one.')

GAP_EX = PR('Is the Riverside Gym or the Oak Street Gym the better deal for me?',
            'Riverside Gym is the better deal. It costs 30 dollars a month and is open from 6 a.m. Note that Riverside '
            'opens at 7 a.m. on weekdays, so it suits most schedules.')

S_CHECK08 = SET(
    'AI.CHECK.08',
    M=sec('Spot contradictions and missing information', GAP, [
        Q('In this fictional example, what is contradictory?', 'It says Riverside opens at 6 and also at 7 a.m.',
          ('It says the gym costs 30 dollars a month', 'stated once'),
          ('It names two different gyms', 'that was the question'),
          ('It says the gym suits most schedules', 'not a contradiction'),
          'Two opening times cannot both be true.', ex=GAP_EX),
        Q('In the same example, what key information is missing for its conclusion?', 'Oak Street Gym\'s price',
          ('Riverside Gym\'s monthly price', 'given as 30 dollars'),
          ('The name of the second gym', 'given'),
          ('The word "deal" in the answer', 'present'),
          '"Better deal" needs the other gym\'s cost.', ex=GAP_EX),
        Q('What is a contradiction?', 'Two statements that cannot both be true',
          ('A statement with no source', 'that is unsupported'),
          ('A statement that is very long', 'not a contradiction'),
          ('A statement in a different language', 'not a contradiction'),
          'Contradictions are incompatible statements.'),
        Q('When you spot a contradiction, what should you do?', 'Resolve it with a reliable source',
          ('Pick the version you prefer', 'preference is not evidence'),
          ('Average the two numbers', 'not a resolution'),
          ('Ignore both and move on', 'leaves it unresolved'),
          'Use evidence to decide.'),
        Q('"Buy this laptop; it is perfect for school." What information is missing?', 'Your budget and needs',
          ('The laptop\'s color', 'minor'), ('The store\'s logo', 'irrelevant'), ('The answer\'s length', 'irrelevant'),
          'The conclusion depends on facts it never established.'),
    ]),
    B=[sk('Find what a conclusion depends on',
          'Every conclusion rests on CONDITIONS. To find them, ask: "What would have to be true for this to hold?" '
          'Conclusion: "Take the bus; it is faster." Conditions: the bus runs at your time, and its trip time is less '
          'than the alternatives\' times. If any condition is unknown, the conclusion is not yet supported. Listing '
          'conditions turns a vague doubt into specific questions you can check.', [
              Q('"Take the bus; it is faster." Which condition must be true?', 'The bus trip takes less time',
                ('The bus is painted blue', 'irrelevant'), ('The bus has Wi-Fi', 'irrelevant'),
                ('The bus driver is friendly', 'irrelevant'), 'Speed must be compared.'),
              Q('"Buy the large size; it is cheaper per ounce." Which fact is needed?', 'Price and size of each option',
                ('The store\'s opening year', 'irrelevant'), ('The color of the box', 'irrelevant'),
                ('The cashier\'s name', 'irrelevant'), 'Per-ounce cost needs price and size.'),
              Q("What question finds a conclusion's conditions?",
          '"What must be true for this to hold?"',
          ('"Does this sound nice and clear to me?"', 'not useful'), ('"Is it long?"', 'not useful'),
          ('"Who wrote it?"', 'sometimes useful, not this'),
          'It reveals the conditions.'),
              Q('If a condition is unknown, the conclusion is...', 'Not yet supported',
                ('Definitely false', 'too strong'), ('Definitely true', 'too strong'), ('Irrelevant', 'not irrelevant'),
                'Unknown conditions leave it unsupported.'),
              Q('"Wear a coat; it will be cold." Which condition matters?', 'The temperature forecast',
                ('The coat\'s brand', 'irrelevant'), ('Your shoe size', 'irrelevant'), ('The day of the week', 'irrelevant'),
                'Cold depends on the weather.'),
          ], why='A learner who misses MAIN may not see what a conclusion depends on; this branch practices listing '
                 'conditions.')],
    F1=sec('Check practical answers for contradictions and gaps', GAP, [
        Q('An answer says a recipe serves 4 and later says "enough for 6 people." What should you do?',
          'Check the recipe source to resolve it',
          ('Assume it serves 5 as a compromise', 'not a resolution'),
          ('Ignore the serving size', 'it matters'),
          ('Trust the later number', 'no reason'),
          'Resolve contradictions with the source.'),
        Q('"This phone plan is cheaper." What do you need before agreeing?',
          "Both plans' costs for the same period",
          ("The plan's advertising slogan and logo", 'irrelevant'), ('The color of the phone', 'irrelevant'),
          ("Only one plan's monthly price", 'needs both'),
          'Comparisons need both sides.'),
        Q('A budget says total spending is 1,200 dollars, but the listed items add to 1,050. What is this?',
          'A contradiction between total and parts',
          ('A rounding style, nothing wrong', '150 is not rounding'), ('Missing information about the income', 'not the issue'),
          ('A formatting choice', 'not formatting'),
          'Totals must match their parts.',
          calc=lambda: 1200 - 1050 == 150),
        Q('A tool recommends a college "because it fits your goals." You never stated your goals. What is missing?',
          'Your goals, which it depends on',
          ("The college's mascot", 'irrelevant'), ("The tool's confidence", 'not information'),
          ("The college's founding year and history", 'irrelevant'),
          'The conclusion rests on unknown information.'),
        Q('An answer says a museum is "free on Sundays" and later "tickets cost 10 dollars daily." What is the best '
          'step?',
          'Check the museum\'s official site',
          ('Assume Sundays are free', 'unresolved'), ('Assume it is 10 dollars every day', 'unresolved'),
          ('Ask the tool which one it prefers', 'not evidence'),
          'Resolve with the source.'),
    ]),
    F2=sec('Uncover hidden assumptions and comparisons', GAP_F2, [
        Q('"Since you work full time, a part-time course is best." You are a full-time student, not a worker. What '
          'happened?',
          'A wrong assumption led to the conclusion',
          ('Nothing; the conclusion still holds', 'its basis was wrong'),
          ('Courses are always part time', 'not true'),
          ('Students cannot take courses', 'not true'),
          'Check the assumptions behind advice.'),
        Q('"Plan A saves 200 dollars." Plan A\'s cost is for a year; Plan B\'s is for a month. What is wrong?',
          'The comparison uses different time periods',
          ('Nothing; 200 dollars of savings is clear', 'periods differ'), ('Plan B must be cheaper', 'not shown'),
          ('Plans cannot be compared', 'they can, fairly'),
          'Comparisons need the same period.'),
        Q('Which question best tests a conclusion?',
          '"What must be true for this to hold?"',
          ('"Does it sound confident?"', 'tone'), ('"Is it longer than other answers?"', 'length'),
          ('"Did it use bullet points?"', 'format'),
          'Then check those conditions.'),
        Q('"Assuming you live near the city, the train is best." You live 50 miles away. What should you do?',
          'Reconsider; the assumption does not fit you',
          ('Take the train anyway', 'ignores the mismatch'), ('Move closer to the city', 'unreasonable'),
          ('Trust it, because it honestly said "assuming"', 'the assumption is wrong for you'),
          'Wrong assumptions weaken conclusions.'),
        Q('A tool concludes a car is reliable "based on owner reviews" but shows none. What is missing?',
          'The reviews it depends on',
          ("The car's color", 'irrelevant'), ('A friendlier tone in the answer', 'not information'),
          ("The tool's name", 'irrelevant'),
          'Claimed evidence must be shown and checked.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.09
HUMAN = ('Some questions carry HIGH STAKES: health and medicine, legal rights and court matters, large money '
         'decisions, safety (electrical work, chemicals, driving), and decisions about other people\'s well-being. For '
         'these, an AI answer can help you prepare: understand terms, make a list of questions, organize your '
         'documents. But a QUALIFIED PERSON who is accountable, such as a doctor, pharmacist, lawyer, licensed '
         'electrician or financial counselor, should review the actual decision, because they can examine your '
         'specific situation and take responsibility. In an emergency, contact emergency services directly.')
HUMAN_F2 = ('Deciding when to involve a qualified person is itself a skill. Signs that you need one: the answer depends '
            'on facts about your body, your documents or your location; being wrong could cause injury, legal trouble '
            'or a large loss; or different sources disagree. Signs that an AI answer may be enough: low stakes, easy '
            'to reverse, and checkable yourself. Cost and access can be real barriers, so look for free or low-cost '
            'qualified help, such as pharmacists, legal aid clinics, school counselors or nonprofit credit counselors.')

S_CHECK09 = SET(
    'AI.CHECK.09',
    M=sec('Recognize when a qualified person must review the answer', HUMAN, [
        Q('Which question most needs a qualified person to review the answer?',
          'Whether two medicines are safe together',
          ('Synonyms for the word "quick" in a story', 'low stakes'), ('Ideas for a birthday card', 'low stakes'),
          ('How to format a bulleted list', 'low stakes'),
          'Medicine interactions are high stakes.'),
        Q('How can an AI tool help with a legal problem?',
          'By helping you prepare questions and documents',
          ('By replacing the need for any lawyer', 'not appropriate for high stakes'), ('By taking legal responsibility for advice', 'it cannot'),
          ('By filing court papers automatically', 'not a safe assumption'),
          'Preparation, not the final decision.'),
        Q('Why does a qualified person matter for high-stakes decisions?',
          'They can examine your case and take responsibility',
          ('They always agree with whatever AI answers say', 'not the reason'), ('They use longer words', 'not the reason'),
          ('They are faster than any tool', 'not the reason'),
          'Accountability and individual assessment.'),
        Q('Someone has chest pain and asks a chatbot what to do. What is the right action?', 'Call emergency services',
          ('Wait for a detailed answer', 'delay is dangerous'),
          ('Ask the chatbot for a second opinion', 'delay is dangerous'),
          ('Search for home remedies first', 'delay is dangerous'),
          'Emergencies need emergency services.'),
        Q('Which is a high-stakes area?', 'Electrical wiring in a home',
          ('Choosing a playlist for a party', 'low stakes'), ('Naming a pet goldfish', 'low stakes'),
          ('Picking a font for a flyer', 'low stakes'),
          'Safety work needs qualified review.'),
    ]),
    B=[cs('Compare AI help with a recipe versus surgery',
          'If a recipe goes wrong, you get a bad dinner and try again tomorrow: LOW STAKES and easy to reverse. If '
          'surgery goes wrong, the harm can be serious and permanent: HIGH STAKES. You might read about either online, '
          'but you would never let a website perform surgery. AI answers fit the same pattern: fine to rely on for '
          'low-stakes, reversible things you can check, but for high-stakes decisions about health, law, money or '
          'safety, a qualified, accountable person should be involved.', [
              Q('Why is a failed recipe low stakes?',
          'You can try again with little harm',
          ('Recipes are always perfect the first time', 'no'), ('Food never matters', 'no'),
          ('Recipes are illegal', 'no'),
          'Reversible and minor.'),
              Q('Why is surgery high stakes?',
          'Harm can be serious and permanent',
          ('It is always quick', 'irrelevant'), ('It is only expensive, nothing else', 'not the main reason'),
          ('It is done indoors', 'irrelevant'),
          'Serious, lasting harm.'),
              Q('For which can you rely on an AI answer you can check?', 'A low-stakes, reversible task',
                ('A surgery decision', 'high stakes'), ('A court filing deadline', 'high stakes'),
                ('A large loan decision', 'high stakes'), 'Low stakes and checkable.'),
              Q('Which area is NOT listed as high stakes?',
          'Choosing a dinner recipe',
          ('Decisions about health', 'listed'), ('Legal decisions', 'listed'),
          ('Safety decisions', 'listed'),
          'Recipes are low stakes.'),
              Q('Who should be involved in high-stakes decisions?',
          'A qualified, accountable person',
          ('Only a website on the topic', 'not accountable'), ('Only a chatbot', 'not accountable'),
          ('Nobody at all, to save time', 'unsafe'),
          'Qualified people take responsibility.'),
          ], why='A learner unsure which questions need a professional can sort stakes with a recipe-versus-surgery '
                 'contrast.')],
    F1=sec('Decide when to involve a qualified person', HUMAN, [
        Q('Leo wants to rewire a light switch and gets AI instructions. What should he do?',
          'Have a licensed electrician do or check the work',
          ('Follow the steps exactly, alone', 'safety risk'), ('Ask a second chatbot for steps', 'still unqualified'),
          ('Skip turning off the power to save a little time', 'dangerous'),
          'Electrical work is a safety risk.'),
        Q('A student uses AI to understand words in a lease before meeting a legal aid lawyer. Is this a good use?',
          'Yes; it helps her prepare questions',
          ('No; she should never read her lease', 'reading is good'),
          ('Yes; she no longer needs the lawyer', 'review still needed'),
          ('No; legal aid will not see her if she used AI', 'not true'),
          'Preparation is a good use.'),
        Q('Which situation can an AI answer reasonably handle alone?', 'Ideas for organizing a closet',
          ('A child\'s medicine dose', 'needs a pharmacist or doctor'),
          ('Whether to sign a business loan', 'needs a qualified review'),
          ('Whether a gas smell is dangerous', 'needs emergency or utility services'),
          'Low stakes and reversible.'),
        Q('An AI answer says a mole "looks harmless" from a description. What should the person do?',
          'See a doctor or dermatologist to examine it',
          ('Trust the answer completely', 'cannot examine it'), ('Ask the tool to describe the mole again', 'not an exam'),
          ('Ignore it forever', 'risky'),
          'Only an exam can assess it.'),
        Q('A family wants to understand retirement account options. What is a good plan?',
          'Learn terms with AI, then see a qualified advisor',
          ('Let AI pick the investments', 'high stakes'), ('Avoid learning anything', 'understanding helps'),
          ("Copy a friend's investment choices exactly", 'not tailored'),
          'Learn, then get qualified advice.'),
    ]),
    F2=sec('Weigh stakes, sources and access to qualified help', HUMAN_F2, [
        Q('Three sources disagree about whether a supplement is safe with a prescription. What does this signal?',
          'Ask a pharmacist or doctor',
          ('Pick the most popular answer', 'not a safety check'),
          ('Take half the dose', 'unsafe guess'),
          ('Assume it is safe', 'unsupported'),
          'Disagreement on safety means ask a qualified person.'),
        Q("An answer depends on your state's laws and your exact documents. What should you do?",
          'Have a qualified person review your case',
          ('Use the general answer as final', 'depends on specifics'), ('Assume all states have the same law', 'they differ'),
          ('Ask the tool to guess your state', 'not reliable'),
          'Specific facts need specific review.'),
        Q('Paying for a lawyer is not possible for Ana. What is a reasonable next step?',
          'Look for a legal aid clinic or free consultation',
          ('Rely only on chatbot answers', 'high stakes'), ('Give up on the issue', 'help may exist'),
          ('Copy a court form she found from another state', 'may not apply'),
          'Free and low-cost qualified help exists.'),
        Q('Which situation is fine to handle with an AI answer you check yourself?',
          'Rewording an email to a coworker',
          ('Deciding whether to stop a medicine', 'high stakes'),
          ('Answering a court summons', 'high stakes'),
          ('Fixing a gas appliance', 'safety risk'),
          'Low stakes and easy to reverse.'),
        Q('Which sign most clearly means you need a qualified person?',
          'Being wrong could cause injury or legal trouble',
          ('The answer is very long', 'not a sign'), ('The answer uses bullet points and bold text', 'not a sign'),
          ('The topic is interesting', 'not a sign'),
          'Serious consequences call for qualified review.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.CHECK.10
USE = ('USEFUL and CORRECT are different questions. A draft can be useful (it saves time, gives you a structure or '
       'ideas) even if some facts in it are wrong, as long as you fix them. An answer can also be correct but not '
       'useful (accurate but off-topic, too technical, or missing what you needed). Judge both separately. Also expect '
       'that results may not REPEAT exactly: the same request can give different wording or even different facts on '
       'another day, after a product update, or with a different setting. If you need to rely on a result later, save '
       'the version you checked.')
USE_F2 = ('Because results can change, a one-time success is weak evidence that a tool will work for you every time. '
          'If you use a tool repeatedly for the same kind of task, keep a few test examples with known good answers and '
          'rerun them now and then. Record what you asked, what you got and what you checked. This makes your work '
          'reproducible: someone else, or you next month, can see how a result was produced and judge it, instead of '
          'trusting "the AI said so."')

S_CHECK10 = SET(
    'AI.CHECK.10',
    M=sec('Judge usefulness and correctness separately; expect variation', USE, [
        Q('A draft outline saves you an hour but has one wrong date. How would you describe it?',
          'Useful, but not fully correct until fixed',
          ('Correct and useful, so no edits needed', 'it has an error'),
          ('Useless, since it has an error', 'it saved time'),
          ('Correct but useless', 'it is useful'),
          'Usefulness and correctness are separate.'),
        Q('An answer is accurate but written for experts, and you are a beginner. What is the problem?',
          'Correct but not useful for you',
          ('Useful but incorrect', 'it is accurate'), ('Neither useful nor correct', 'it is correct'),
          ('No problem at all', 'you cannot use it'),
          'Accuracy does not guarantee usefulness.'),
        Q('Why might the same request give a different answer next week?', 'Results can vary over time and updates',
          ('Requests are deleted after a week', 'not the reason'),
          ('The first answer was always fake', 'not implied'),
          ('Tools only work once per question', 'not true'),
          'Outputs can vary.'),
        Q('You will cite an AI-assisted summary in a report later. What should you do now?',
          'Save the version you checked',
          ('Plan to regenerate it later', 'it may differ'),
          ('Trust you will get the same text', 'not guaranteed'),
          ('Delete it after reading', 'you will need it'),
          'Keep the checked version.'),
        Q('Which statement is accurate?',
          'Judge usefulness and correctness separately',
          ('Useful answers are always correct as well', 'not true'), ('Correct answers are always useful', 'not true'),
          ('Results always repeat exactly', 'not true'),
          'Two separate questions.'),
    ]),
    B=[cs('Compare a rough map sketch with a perfect map in another language',
          'A friend sketches a ROUGH MAP on a napkin. It is not to scale and one street name is wrong, but it gets you '
          'to the party: USEFUL, though not fully correct. Another friend gives you a PERFECT MAP, but it is printed in '
          'a language you cannot read: CORRECT, but not useful to you. And if you ask the napkin friend to draw it again '
          'tomorrow, the sketch will look a little different. That is why you judge usefulness and correctness '
          'separately, and keep the version you checked.', [
              Q('The napkin sketch is...', 'Useful but not fully correct',
                ('Correct but not useful', 'that is the other map'), ('Neither', 'it got you there'),
                ('Perfectly correct', 'a street is wrong'), 'It works despite an error.'),
              Q('The perfect map in another language is...', 'Correct but not useful to you',
                ('Useful but wrong', 'it is correct'), ('Useful and correct for you', 'you cannot read it'),
                ('Neither', 'it is correct'), 'Accurate but unusable for you.'),
              Q("Will tomorrow's sketch look the same?",
          'Probably a little different',
          ('Exactly the same', 'unlikely'), ('Completely blank', 'no'),
          ('It cannot be drawn twice', 'no'),
          'Results vary.'),
              Q('Why judge usefulness and correctness separately?',
          'Each can be true without the other',
          ('They always go together in every case', 'they do not'), ('Neither ever matters', 'both matter'),
          ('Only usefulness matters', 'correctness matters too'),
          'They are different qualities.'),
              Q('What should you do with the sketch you checked?', 'Keep that version',
                ('Throw it away', 'you may need it'), ('Ask for a new one every time', 'it may change'),
                ('Translate it', 'not needed'), 'Save checked versions.'),
          ], why='A learner who merges "useful" and "correct" can separate them through two contrasting maps.')],
    F1=sec('Apply usefulness, correctness and repeatability', USE, [
        Q('A tool drafts a cover letter with a strong structure but invents a job title you never held. What should you do?',
          'Keep the structure and fix the false detail',
          ('Send it as is, since it reads well overall', 'contains a falsehood'), ('Throw it all away', 'loses the useful structure'),
          ('Ask it to invent more titles', 'worse'),
          'Use what helps; correct what is wrong.'),
        Q('A summary is accurate but leaves out the deadline you needed. How would you rate it?',
          'Correct but not fully useful',
          ('Useful and complete for her', 'missing your need'), ('Incorrect', 'what it says is accurate'),
          ('Perfect', 'missing your need'),
          'Correct, yet missing what matters to you.'),
        Q('Tom got a great answer yesterday and wants the same result today for a report. What is safest?',
          'Use the saved, checked version',
          ('Ask again and assume the new answer matches', 'may differ'), ('Quote from memory', 'may differ'),
          ('Ask a different tool', 'may differ'),
          'Saved versions are stable.'),
        Q('Which result is correct but not useful?',
          "An accurate answer about the wrong city's rules",
          ('A rough draft with one typo', 'useful, mostly correct'), ('A helpful list with a fixed error', 'useful and corrected'),
          ('A clear answer that fits your question exactly', 'useful and correct'),
          'Accurate but irrelevant.'),
        Q('A tool gave a different total on two runs of the same budget question. What should you do?',
          'Recalculate the total yourself',
          ('Use the smaller of the two totals', 'preference is not a check'), ('Use the larger total', 'preference is not a check'),
          ('Average them', 'not a check'),
          'Variation calls for an independent check.'),
    ]),
    F2=sec('Make AI-assisted work reproducible', USE_F2, [
        Q('A tool worked well once for sorting invoices. Should you assume it will always work?',
          'No; test it on several examples over time',
          ('Yes; one success proves reliability', 'weak evidence'),
          ('Yes; tools never change', 'they do'),
          ('No; it will never work again', 'too strong'),
          'One success is weak evidence.'),
        Q('What should you record to make an AI-assisted result reproducible?',
          'What you asked, got and checked',
          ('Only the final answer you used', 'missing context'), ('Only the date', 'not enough'),
          ("Only the tool's name", 'not enough'),
          'A record lets others judge the result.'),
        Q('Why keep test examples with known good answers?', 'To rerun them and catch changes',
          ('To make the tool faster', 'not the purpose'),
          ('To train the model yourself', 'not what they do'),
          ('To avoid reading new results', 'you still read them'),
          'Known answers reveal drift.'),
        Q('A coworker says, "The AI said so," as the only support for a number. What is missing?',
          'A record of how the number was checked',
          ('A friendlier tone', 'not support'), ('A longer explanation of the number', 'not support'),
          ('A second AI agreeing', 'not independent'),
          'Reproducible work shows its process and checks.'),
        Q('After a product update, your saved test examples give different results. What should you do?',
          'Review the differences before relying on it',
          ('Ignore the tests from now on', 'defeats their purpose'), ('Assume the new results are better than before', 'not shown'),
          ('Delete the old examples', 'loses the baseline'),
          'Tests catch changes worth reviewing.'),
    ]),
)

SETS = [S_CHECK01, S_CHECK02, S_CHECK03, S_CHECK04, S_CHECK05, S_CHECK06, S_CHECK07, S_CHECK08, S_CHECK09, S_CHECK10]
