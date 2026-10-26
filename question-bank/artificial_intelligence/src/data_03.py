"""Foundation 3: Large language models (AI.LLM.01-07, AI.LLM.09)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.LLM.01
LLM = ('A LARGE LANGUAGE MODEL (LLM) is a model trained on enormous amounts of text to do one core job: given some '
       'text, predict a likely next piece of text. Repeating that prediction, piece by piece, produces sentences, '
       'answers, stories or code. Because it learned from so much writing, an LLM can imitate many styles and often '
       'produces useful, relevant text. But predicting likely text is not the same as looking up facts or reasoning '
       'like a person. An LLM has no built-in way to check truth, so its output can be plausible and wrong. "Large" '
       'refers to the size of the model and its training data.')
LLM_F2 = ('People sometimes describe LLMs with extreme claims: "it is just autocomplete, so it can do nothing useful," '
          'or "it knows everything, so it is always right." Both mislead. Predicting text well, at large scale, '
          'produces abilities that are genuinely useful, such as drafting, summarizing and explaining. Yet the same '
          'process can produce confident errors, because a likely-sounding sentence and a true sentence are not '
          'always the same. Judge an LLM by testing it on your task and checking facts, not by a slogan about what it '
          '"really" is.')

S_LLM01 = SET(
    'AI.LLM.01',
    M=sec('Describe what a large language model does', LLM, [
        Q('What is the core job a large language model is trained to do?',
          'Predict a likely next piece of text',
          ('Look up each answer in a database of verified facts', 'it predicts text; it does not check facts'),
          ('Follow a fixed rule list written by programmers', 'it learned patterns from text'),
          ('Store a copy of the internet to read from', 'it is a trained model, not a stored copy'),
          'An LLM predicts likely next text, repeatedly.'),
        Q('What does "large" refer to in "large language model"?',
          'The size of the model and its training data',
          ('The length of the answers it is allowed to write', 'not what "large" means'),
          ('The number of languages printed on its box', 'not what "large" means'),
          ('The physical size of the computer screen it uses', 'not what "large" means'),
          '"Large" describes model size and training data.'),
        Q('How does an LLM produce a whole paragraph?',
          'By repeating next-piece predictions one after another',
          ('By copying one paragraph from a single website', 'it generates piece by piece'),
          ('By asking a human writer to type each sentence', 'it generates automatically'),
          ('By choosing a finished paragraph from a stored list', 'it builds text step by step'),
          'Repeated prediction builds longer text.'),
        Q('Why can an LLM\'s answer be plausible but wrong?',
          'Likely-sounding text is not always true',
          ('It is programmed to make mistakes on purpose', 'errors are not deliberate'),
          ('It always checks facts before it writes', 'it has no built-in truth check'),
          ('It writes only random words with no pattern', 'its output follows patterns'),
          'Prediction favors plausible text, which may be false.'),
        Q('Which task is an LLM usually well suited to help with?',
          'Drafting a first version of a short letter',
          ('Guaranteeing the exact current price of a stock', 'needs a live, checked source'),
          ('Certifying that a medicine dose is safe for you', 'needs a qualified professional'),
          ('Proving a fact is true just by stating it', 'stating is not proving'),
          'Drafting text plays to an LLM\'s strengths; facts still need checks.'),
    ]),
    B=[cs('Compare an LLM with a phone\'s word suggestions',
          'When you type a message, your phone may suggest the next word: after "See you," it might offer "soon" or '
          '"tomorrow." It suggests words that often come next, not words it has checked are true for you. A large '
          'language model works on a similar core idea at a far bigger scale. It was trained on huge amounts of text, '
          'so it can continue whole sentences and paragraphs in many styles. The scale makes it much more capable '
          'than a phone keyboard, but the basic job is still predicting likely text.', [
              Q('After "See you," why might a phone suggest "soon"?', '"Soon" often comes next in messages',
                ('It knows when you will meet', 'it does not know your plans'),
                ('It checked your calendar for the date', 'suggestions come from patterns'),
                ('It was told by your friend', 'not how suggestions work'), 'Suggestions reflect common patterns.'),
              Q('What core job do the phone keyboard and an LLM share?', 'Predicting likely next text',
                ('Checking facts against a database', 'neither does this by default'),
                ('Taking photos of the screen', 'unrelated'), ('Sending messages for you', 'unrelated'),
                'Both predict likely continuations.'),
              Q('What makes an LLM much more capable than a phone keyboard?',
          'Its far bigger scale of training',
          ('It has a much larger screen', 'irrelevant'), ('It uses fewer words', 'not the reason'),
          ('It only works offline', 'not the reason'),
          'Scale greatly increases ability.'),
              Q('Does a likely next word have to be true for you?', 'No, likely is not the same as true',
                ('Yes, likely words are always true', 'not necessarily'),
                ('Yes, if the phone is expensive', 'price does not matter'),
                ('No, because phones cannot spell', 'not the point'), 'Likely text can be wrong for your situation.'),
              Q('Which continuation would a keyboard most likely suggest after "Happy"?', '"birthday"',
                ('"spreadsheet"', 'rarely follows "Happy"'), ('"tax refund deadline"', 'unlikely continuation'),
                ('"carburetor"', 'unlikely continuation'), 'Common phrases are likely continuations.'),
          ], why='A learner who pictures an LLM as a fact database can start from the familiar next-word suggestions on '
                 'a phone.')],
    F1=sec('Apply what an LLM is to everyday uses', LLM, [
        Q('Rosa asks an LLM-based chatbot for the population of her town and gets a precise number. What should she do before using it in a report?',
          'Check the number in an official source',
          ('Use it', 'precision is not accuracy'), ('Ask the chatbot to repeat the same number', 'repetition is not a check'),
          ('Round it up so it looks more official', 'does not check it'),
          'A plausible number still needs a source.'),
        Q('A student wants help turning bullet notes into a clear paragraph. Is an LLM a reasonable tool to try?',
          'Yes; rewriting suits it, then check the facts',
          ('No; LLMs cannot produce paragraphs', 'they can'), ('Yes; and the result needs no checking', 'facts and meaning still need review'),
          ('No; only search engines can rewrite notes', 'not true'),
          'Drafting suits LLMs; review keeps it accurate.'),
        Q('Which description of an LLM is most accurate for a beginner?',
          'A model that writes by predicting text, which can be wrong',
          ('A talking encyclopedia that is always correct', 'it can be wrong'), ('A search engine that only shows links', 'it generates text'),
          ('A robot that understands everything just like a person', 'misleading comparison'),
          'Prediction-based writing with possible errors.'),
        Q('An LLM writes a confident paragraph about a law. What is the right attitude?',
          'Treat it as a draft and check the law\'s actual text',
          ('Trust it, because legal wording sounds official', 'tone is not evidence'),
          ('Ignore it completely, since LLMs never help', 'it may help as a starting point'),
          ('Assume it is current because it sounds confident', 'it may be outdated'),
          'Useful draft, unverified facts.'),
        Q('Why might two well-written LLM answers about the same history event disagree?',
          'Each is predicted text; either could contain errors',
          ('One of them must have been copied from a textbook', 'not implied'), ('History has no facts that can be checked', 'it does'),
          ('LLMs always agree on facts', 'they do not'),
          'Plausible text can differ and be wrong; check a source.'),
    ]),
    F2=sec('Avoid both extreme claims about LLMs', LLM_F2, [
        Q('A friend says, "LLMs are just autocomplete, so they are useless." What is the best response?',
          'Prediction at large scale can still be very useful',
          ('Correct; they cannot help with any real task', 'they help with drafting and more'), ('Correct; autocomplete never produces sentences', 'it can'),
          ('Wrong; LLMs never predict text at all', 'prediction is their core job'),
          'The "useless" slogan ignores real abilities.'),
        Q('A coworker says, "It knows everything, so I never check it." What is the risk?',
          'Confident but wrong answers will slip through',
          ('None; LLMs cannot make errors', 'they can'),
          ('The model will stop working if not checked', 'not how it works'),
          ('Checking is illegal for business tools', 'nonsense'),
          'The "knows everything" slogan hides errors.'),
        Q('What is the best way to judge whether an LLM is good for your task?',
          'Test it on examples of your task and check the facts',
          ('Decide based on a slogan about what it "really" is', 'slogans are not tests'),
          ('Count how many people use it worldwide', 'popularity is not fit'),
          ('Ask it whether it is good at your task', 'self-reports are not tests'),
          'Testing beats slogans.'),
        Q('An LLM summarized a report well but added a statistic not in the report. What does this show?',
          'It can be useful and still make confident errors',
          ('It is useless for every kind of task at all', 'it summarized well'), ('It is always right about statistics', 'it added one'),
          ('Summaries never contain errors', 'this one did'),
          'Usefulness and errors can coexist.'),
        Q('Why can a likely-sounding sentence be false?',
          'Prediction favors typical-sounding text, not checked text',
          ('Likely sentences are always checked against sources first', 'no built-in check'), ('False sentences are always unlikely', 'false claims can sound typical'),
          ('LLMs cannot write sentences', 'they can'),
          'Typical-sounding is not the same as verified.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.02
TOK = ('Language models do not read words the way people do. They read and write TOKENS: chunks of text that may be a '
       'whole word, part of a word, a punctuation mark or a space. A common word like "the" is often one token, while '
       'a long or rare word like "unbelievably" may be split into several. For English, one provider\'s rule of thumb '
       'is about 4 characters, or about three quarters of a word, per token, but the exact count depends on the model. '
       'Token counts matter because limits on how much text a model can handle, and many usage prices, are measured '
       'in tokens, not words.')
TOK_F2 = ('Token counts can surprise you. Text in some languages, unusual spellings, long numbers, code and tables '
          'often use more tokens per word than everyday English, so the same message length in words can cost more '
          'tokens. Because a model sees tokens rather than letters, tasks such as counting the letters in a word or '
          'reversing a word can trip it up even when it writes fluent sentences. And because different models split '
          'text differently, a count from one tool is only an estimate for another.')

S_LLM02 = SET(
    'AI.LLM.02',
    M=sec('Explain tokens and why counts differ from words', TOK, [
        Q('What is a token?',
          'A chunk of text, such as a word or part of one',
          ('A coin you pay with to use an AI website', 'not the meaning here'), ('A password that unlocks a model', 'not the meaning here'),
          ('A whole page of text read at once', 'tokens are small chunks'),
          'Tokens are pieces of text.'),
        Q('Which word is (a very common short word) most likely split into several tokens?',
          'unbelievably (a long, rarer word)',
          ('the (a very common short word)', 'a common short word'), ('and (a very common short word)', 'a common short word'),
          ('is (a very common short word)', 'a common short word'),
          'Long or rare words are often split.'),
        Q('Using the rule of thumb of about three quarters of a word per token, about how many tokens is a 300-word '
          'English text?',
          'About 400 tokens',
          ('About 225 tokens', 'that multiplies by 0.75 instead of dividing'),
          ('About 300 tokens', 'tokens are not equal to words'),
          ('About 1,200 tokens', 'that is the character estimate'),
          '300 / 0.75 = 400 tokens (an estimate).', calc=lambda: 300 / 0.75 == 400),
        Q('Why do token counts matter to users?',
          'Many limits and prices are measured in tokens',
          ('Tokens decide the font the answer appears in', 'unrelated'),
          ('Tokens decide whether the answer is true', 'unrelated'),
          ('Tokens are only used for counting images', 'they measure text'),
          'Limits and usage prices often use tokens.'),
        Q('Is the token rule of thumb exact for every model?',
          'No; counts depend on how each model splits text',
          ('Yes; every model splits text identically', 'models differ'),
          ('Yes; one token always equals one word', 'not true'),
          ('No; tokens are always exactly one letter', 'not true'),
          'Rules of thumb are estimates.'),
    ]),
    B=[sk('Estimate tokens from words',
          'A simple estimate turns words into tokens. One provider\'s rule of thumb for English is that a token is '
          'about three quarters of a word. To estimate tokens from words, DIVIDE the number of words by 0.75, which '
          'is the same as multiplying by 4 and then dividing by 3. Example: 60 words / 0.75 = 80 tokens. To estimate '
          'words from tokens, MULTIPLY tokens by 0.75. Example: 200 tokens x 0.75 = 150 words. These are rough '
          'estimates for ordinary English, not exact counts.', [
              Q('About how many tokens is 30 words?', '40', ('22.5', 'multiplied instead of dividing'),
                ('30', 'tokens are not words'), ('120', 'used the character estimate'),
                '30 / 0.75 = 40.', calc=lambda: 30 / 0.75 == 40),
              Q('About how many words is 400 tokens?', '300', ('533', 'divided instead of multiplying'),
                ('400', 'words are not tokens'), ('100', 'used the wrong factor'),
                '400 x 0.75 = 300.', calc=lambda: 400 * 0.75 == 300),
              Q('About how many tokens is 150 words?', '200', ('112.5', 'multiplied instead of dividing'),
                ('150', 'tokens are not words'), ('600', 'used the character estimate'),
                '150 / 0.75 = 200.', calc=lambda: 150 / 0.75 == 200),
              Q('Dividing by 0.75 gives the same result as which steps?', 'Multiply by 4, then divide by 3',
                ('Multiply by 3, then divide by 4', 'that is multiplying by 0.75'),
                ('Add 75 to the number', 'not equivalent'), ('Subtract a quarter', 'not equivalent'),
                'x / 0.75 = x x 4 / 3.', calc=lambda: abs(9 / 0.75 - 9 * 4 / 3) < 1e-9),
              Q('About how many words is 1,000 tokens?', '750', ('1,333', 'divided instead of multiplying'),
                ('1,000', 'words are not tokens'), ('250', 'subtracted instead'),
                '1,000 x 0.75 = 750.', calc=lambda: 1000 * 0.75 == 750),
          ], why='A learner who cannot convert words and tokens practices the one division and one multiplication the '
                 'MAIN questions use.')],
    F1=sec('Use token estimates in practical situations', TOK, [
        Q('A tool allows about 2,000 tokens per message. About how many words of English is that?',
          'About 1,500 words',
          ('About 2,667 words', 'divided instead of multiplying'),
          ('Exactly 2,000 words', 'tokens are not words'),
          ('About 500 words', 'subtracted a quarter of a quarter'),
          '2,000 x 0.75 = 1,500 words (an estimate).', calc=lambda: 2000 * 0.75 == 1500),
        Q('Jun\'s essay is 900 words. About how many tokens will it use?',
          'About 1,200 tokens',
          ('About 675 tokens', 'multiplied instead of dividing'),
          ('Exactly 900 tokens', 'tokens are not words'),
          ('About 3,600 tokens', 'used the character estimate'),
          '900 / 0.75 = 1,200 tokens (an estimate).', calc=lambda: 900 / 0.75 == 1200),
        Q('Why might a message hit a token limit even though it seems short in words?',
          'Some words and symbols use several tokens each',
          ('Every word always uses exactly ten tokens', 'not true'),
          ('Spaces are never counted at all', 'not the reason'),
          ('Token limits only count pictures', 'they count text'),
          'Rare words, numbers and symbols can use more tokens.'),
        Q('A pricing page charges by tokens. What does that mean for a long document?',
          'Longer text usually costs more tokens',
          ('Cost depends only on the number of pages printed', 'tokens, not pages'),
          ('Long documents are always free', 'not implied'),
          ('Cost depends on the font size used', 'unrelated'),
          'More text means more tokens, usually more cost.'),
        Q('Two tools report different token counts for the same paragraph. What is the likely reason?',
          'They split text into tokens differently',
          ('One tool must be broken', 'differences are normal'), ('Tokens are random numbers', 'they follow rules'),
          ('Paragraphs have no fixed text inside them', 'the text is the same'),
          'Different tokenizers give different counts.'),
    ]),
    F2=sec('Handle surprising token counts', TOK_F2, [
        Q('A message with a long table of numbers uses many more tokens than a story of the same word count. Why?',
          'Numbers and table symbols often take more tokens',
          ('Stories are never counted in tokens', 'they are'), ('Tables are always converted into images first', 'not implied'),
          ('Numbers always count as zero tokens', 'the opposite'),
          'Long numbers and symbols raise token counts.'),
        Q('A fluent model miscounts how many times the letter r appears in "strawberry." What helps explain this?',
          'It works with tokens, not individual letters',
          ('It cannot read English at all', 'it writes fluent English'),
          ('Letter counting is always easy for every model', 'not when it sees tokens'),
          ('The word is spelled differently for computers', 'not the reason'),
          'Seeing chunks, not letters, can trip up letter tasks.'),
        Q('You estimate a cost using one tool\'s token counter, but you will use a different model. What should you '
          'remember?',
          'The count is only an estimate for the other model',
          ('The count will match exactly for every model', 'models split differently'),
          ('Token counts never affect cost', 'they often do'),
          ('You must count tokens by hand instead', 'a counter is still a useful estimate'),
          'Different models tokenize differently.'),
        Q('A message in a language other than English uses more tokens than its English translation. What is the best explanation?',
          'Some languages use more tokens per word for some models',
          ('Languages other than English are not allowed to be tokenized', 'not true'), ('The translation must have deleted words', 'not implied'),
          ('Tokens count only English letters', 'not true'),
          'Token efficiency varies by language and model.'),
        Q('A code snippet of 50 lines seems short but uses a lot of tokens. What is the likely reason?',
          'Symbols, spaces and names in code split into many tokens',
          ('Code is never counted in tokens', 'it is'), ('Each line of code always counts as exactly one token', 'not true'),
          ('Code is turned into pictures first', 'not implied'),
          'Code can be token-heavy.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.03
PROB = ('At each step, a language model gives every possible next token a PROBABILITY: how likely it is to come next. '
        'After "The sky is," the token "blue" might get a high probability and "green" a low one. The model then picks '
        'a token, often by SAMPLING, which means choosing at random but weighted by those probabilities. That is why '
        'the same request can produce different answers on different tries. Some products let users or developers '
        'adjust settings, sometimes called temperature, that make choices more predictable or more varied. Variation '
        'is useful for brainstorming but means you should not expect identical answers every time.')
PROB_F2 = ('Variation has practical effects. If you ask the same factual question twice and get two different numbers, '
           'at most one can be right, and maybe neither, so the difference is a signal to check a source, not to pick '
           'the one you like. When you need consistency, such as the same format for 100 product descriptions, give '
           'clear instructions and a template, and check the results, because even predictable settings do not '
           'guarantee identical outputs in every product. When you want ideas, variation is a feature: ask for several '
           'options at once.')

PROB_EX = TABLE([['Possible next token after "The sky is"', 'Probability (made-up numbers)'],
                 ['blue', '0.62'], ['clear', '0.18'], ['gray', '0.12'], ['green', '0.01'], ['all other tokens', '0.07']],
                label='Prepared example (made-up probabilities for teaching)')

S_LLM03 = SET(
    'AI.LLM.03',
    M=sec('Explain probabilities and why answers vary', PROB, [
        Q('What does a language model assign to each possible next token?',
          'A probability of how likely it is to come next',
          ('A grade showing whether it is true or false', 'probability is not truth'),
          ('A fixed rule saying which token is required', 'it weighs options'),
          ('A price for using that particular token', 'not what it assigns'),
          'Each candidate token gets a probability.'),
        Q('Using the table, which token is the most likely next choice?', 'blue',
          ('clear', '0.18 is lower than 0.62'), ('gray', '0.12 is lower'), ('green', '0.01 is very low'),
          'blue has the highest probability (0.62).', ex=PROB_EX),
        Q('Using the table, what is the combined probability of "clear" or "gray"?', '0.30',
          ('0.18', 'only "clear"'), ('0.12', 'only "gray"'), ('0.80', 'added "blue" and "clear" instead'),
          '0.18 + 0.12 = 0.30.', calc=lambda: abs(0.18 + 0.12 - 0.30) < 1e-9, ex=PROB_EX),
        Q('Why can the same request produce different answers on different tries?',
          'The model often samples among likely tokens',
          ('The model forgets its training each time', 'its training stays the same'),
          ('Someone edits the answers by hand each time', 'not how it works'),
          ('The internet changes the model every second', 'not the usual reason'),
          'Weighted random choices lead to variation.'),
        Q('Settings such as "temperature" usually change what?',
          'How predictable or varied the choices are',
          ('Whether the facts are true', 'settings do not check truth'), ('How warm the computer runs', 'not this meaning'),
          ('Which language the user speaks and reads', 'not this setting'),
          'These settings adjust variation.'),
    ]),
    B=[sk('Read and combine simple probabilities',
          'A PROBABILITY is a number from 0 to 1 that says how likely something is: 0 means impossible, 1 means certain, '
          '0.5 means as likely as not. Probabilities for all the options in one choice add up to 1. To find the chance '
          'of "this OR that" when they cannot both happen, ADD their probabilities: if the chance of rain is 0.3 and '
          'of snow is 0.1, the chance of rain or snow is 0.4. A higher number means more likely, but a likely option '
          'is not guaranteed to happen.', [
              Q('Which probability means "certain"?', '1', ('0', 'impossible'), ('0.5', 'as likely as not'),
                ('0.1', 'unlikely'), '1 means certain.'),
              Q('Rain 0.3, snow 0.1. What is the chance of rain or snow?', '0.4', ('0.03', 'multiplied instead'),
                ('0.2', 'subtracted instead'), ('0.3', 'only rain'),
                '0.3 + 0.1 = 0.4.', calc=lambda: abs(0.3 + 0.1 - 0.4) < 1e-9),
              Q('Three options have probabilities 0.5, 0.3 and a missing value. What is the missing value?', '0.2',
                ('0.8', 'added instead of finding what is left'), ('0.5', 'repeated a value'),
                ('1.0', 'that is the total'), '1 - 0.5 - 0.3 = 0.2.', calc=lambda: abs(1 - 0.5 - 0.3 - 0.2) < 1e-9),
              Q('Which option is most likely: A 0.25, B 0.45, C 0.30?', 'B', ('A', '0.25 is lowest'),
                ('C', '0.30 is less than 0.45'), ('All are equal', 'they differ'),
                'B has the highest probability.'),
              Q('An option has probability 0.9. Is it guaranteed to happen?', 'No, it is likely but not certain',
                ('Yes, anything over 0.5 is certain', 'only 1 is certain'), ('Yes, 0.9 equals 1', 'it does not'),
                ('No, it is impossible', '0 is impossible'), 'Likely is not guaranteed.'),
          ], why='A learner who misreads the probability table or the idea of variation practices reading and adding '
                 'simple probabilities.')],
    F1=sec('Apply variation to everyday use', PROB, [
        Q('Ali asks for a party theme twice and gets two different ideas. What does this most likely mean?',
          'The model sampled differently; both are normal',
          ('The model is broken and should be reported', 'variation is normal'), ('His first request was deleted by mistake', 'not implied'),
          ('Only one of the ideas could be a real party theme', 'both can be valid ideas'),
          'For ideas, variation is expected and useful.'),
        Q('A teacher wants many different practice sentences. What does variation offer?',
          'Several different options from similar requests',
          ('The same sentence every single time', 'the opposite'),
          ('A guarantee that every sentence is correct', 'variation does not guarantee correctness'),
          ('Nothing useful for this task', 'variety helps here'),
          'Variation is a feature for brainstorming.'),
        Q('A tool offers a setting for "more creative" or "more focused" answers. Which choice fits writing a list of '
          'unusual story ideas?',
          'More creative (more varied)',
          ('More focused (more predictable)', 'less variety for ideas'),
          ('Turn the tool off', 'avoids the task'),
          ('It makes no difference at all', 'it changes variation'),
          'Varied output helps brainstorming.'),
        Q('Why is a likely next token not guaranteed to be correct?',
          'Likely means common in patterns, not checked as true',
          ('Likely tokens are always true facts', 'not necessarily'), ('Correct tokens always get a probability of exactly 1', 'not how it works'),
          ('Probabilities are only used for pictures', 'they are used for text'),
          'Probability reflects patterns, not truth.'),
        Q('A user wants three different subject lines for an email. What is the best request?',
          'Ask for three distinct options in one request',
          ('Ask once and expect the same line every time', 'one line is not three options'),
          ('Ask for exactly one line and copy it three times', 'not distinct'),
          ('Never use AI for subject lines', 'unnecessary'),
          'Asking for several options uses variation on purpose.'),
    ]),
    F2=sec('Respond sensibly when answers vary', PROB_F2, [
        Q('You ask a model the height of a famous tower twice and get 324 meters and 330 meters. What should you do?',
          'Check a reliable source; at most one is right',
          ('Pick the number you like better', 'preference is not evidence'), ('Average them to 327 and report that', 'averaging guesses is not a check'),
          ('Ask a third time and trust whichever number repeats', 'agreement is not proof'),
          'Different answers to a factual question signal the need to check.'),
        Q('A store needs 100 product descriptions in exactly the same format. What helps most?',
          'Clear instructions, a template, and checking the results',
          ('Higher variation settings for more creativity', 'works against consistency'),
          ('Asking without any format and hoping it matches', 'unlikely to be consistent'),
          ('Assuming outputs are always identical', 'they may differ'),
          'Templates and checks support consistency.'),
        Q('Even with "predictable" settings, a product gives slightly different wording each time. What is the best '
          'conclusion?',
          'Settings reduce variation but may not guarantee identical output',
          ('The settings must be ignored completely by every product', 'too strong'),
          ('The model is learning from each request', 'ordinary use does not retrain'),
          ('The answers are therefore all false', 'wording differences do not mean false'),
          'Do not count on identical outputs.'),
        Q('When is variation in answers most helpful?',
          'When you want many ideas to choose from',
          ('When you need one exact legal date', 'needs a source, not variety'), ('When you must match a strict template', 'variety works against it'),
          ('When you need a precise measurement', 'needs a source'),
          'Variety helps idea generation.'),
        Q('Two runs of the same request give different conclusions about whether a contract clause is risky. What should a careful user do?',
          'Treat it as uncertain and get the clause reviewed',
          ('Choose the more reassuring conclusion', 'preference is not evidence'), ('Run it ten times and take the most common answer', 'agreement is not proof'),
          ('Ignore the clause entirely', 'unsafe'),
          'Conflicting answers signal uncertainty; get a reliable check.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.04
FLU = ('Language models are trained to produce text that reads naturally, so their answers are usually FLUENT: smooth, '
       'confident and well organized. Fluency is not EVIDENCE. A model can describe a book that does not exist, '
       'invent a statistic, or misstate a rule in the same confident tone it uses for correct facts. Signs such as '
       'precise numbers, formal language or phrases like "studies show" do not prove anything by themselves. To judge '
       'a claim, look for something you can check: a source you can open, a calculation you can redo, or a fact you '
       'can confirm elsewhere.')
FLU_F2 = ('Some answers include their own reassurances, such as "I am confident," "this is a verified fact," or a '
          'neat reference list. These are still generated text, so they do not add evidence by themselves. An answer '
          'can also mix correct and incorrect parts, which makes errors harder to notice: three right facts can make a '
          'fourth wrong one seem trustworthy. A practical habit is to identify the specific claims that matter for '
          'your decision and check those, rather than judging the whole answer by how it sounds.')

FLU_EX = PR('Who wrote the novel "The Silver Lantern of Brightwater"?',
            'The novel "The Silver Lantern of Brightwater" was written by Eleanor Marsh and published in 1962. It won '
            'praise for its vivid portrait of a fishing town and is often taught in literature classes.')

S_LLM04 = SET(
    'AI.LLM.04',
    M=sec('Explain why fluent language is not evidence', FLU, [
        Q('Why do language model answers usually sound smooth and confident?',
          'They are trained to produce natural-sounding text',
          ('They have checked every fact before writing', 'fluency does not come from checking'),
          ('They copy only from verified textbooks', 'not how they work'),
          ('They are always written by human experts', 'they are generated'),
          'Fluency comes from training on natural text.'),
        Q('In this fictional example, the book title was invented for the question. What does the response show?',
          'A confident, detailed answer about something unreal',
          ('Proof that the book exists, since details are given', 'details are not proof'), ('That the model checked a library catalog', 'nothing shows a check'),
          ('That any answer with a year must be correct', 'a year is not evidence'),
          'Fluent detail can describe something unreal.',
          ex=FLU_EX),
        Q('An answer says, "Studies show 73 percent of people prefer this." What does that sentence prove by itself?',
          'Nothing yet; you would need the actual studies',
          ('That a real study found exactly 73 percent', 'the phrase is not a source'),
          ('That the number is rounded correctly', 'not established'),
          ('That most people prefer it, for certain', 'not established'),
          '"Studies show" is a claim, not evidence.'),
        Q('Which of these is something you can actually check?',
          'A link to the report that you can open',
          ('A confident, formal tone', 'tone is not checkable evidence'), ('The phrase "experts agree"', 'vague, not a source'),
          ('A very precise-looking number with decimals', 'precision is not proof'),
          'A source you can open can be checked.'),
        Q('A model gives a correct-sounding rule for a game. What is the best way to confirm it?',
          'Check the official rulebook',
          ('Trust it because it is well organized', 'organization is not evidence'),
          ('Ask the model whether it is sure', 'its answer is more generated text'),
          ('Assume it is right since it is fluent', 'fluency is not evidence'),
          'An official source confirms a rule.'),
    ]),
    B=[sk('Separate how a claim sounds from what supports it',
          'Two questions help with any claim. First: HOW DOES IT SOUND? Confident, formal, detailed, friendly. Second: '
          'WHAT SUPPORTS IT? A source you can open, a calculation you can redo, a fact you can confirm elsewhere. Only '
          'the second question tells you whether to trust it. Example: "The museum opens at 9 a.m., according to its '
          'website (link)" has support you can check. "The museum definitely opens at 9 a.m." only sounds sure. A '
          'claim can sound weak and be true, or sound strong and be false.', [
              Q('Which part tells you whether to trust a claim?', 'What supports it',
                ('How confident it sounds', 'sound is not support'), ('How long it is', 'length is not support'),
                ('How formal the words are', 'style is not support'), 'Support decides trust.'),
              Q('Which claim includes support you can check?',
          '"Opens at 9 a.m., per its website (link)"',
          ('"Definitely opens at 9 a.m."', 'only sounds sure'), ('"Everyone knows it opens at 9"', 'vague'),
          ('"It surely opens at 9 a.m., just trust me"', 'only sounds sure'),
          'A link can be checked.'),
              Q('"The bridge is 2.3 km long, I am completely certain." What kind of statement is "I am completely certain"?',
          'How it sounds, not support',
          ('A source that you can open', 'nothing to open'), ('A calculation', 'no calculation'),
          ('An official record', 'not a record'),
          'Certainty words are about sound.'),
              Q('Can a claim sound unsure and still be true?', 'Yes; how it sounds does not decide truth',
                ('No; true claims always sound sure', 'not true'), ('No; unsure claims are always false', 'not true'),
                ('Only if it is very long', 'length is irrelevant'), 'Sound and truth are separate.'),
              Q('Which is a calculation you can redo?',
          '"3 tickets at 12 dollars each is 36 dollars"',
          ('"The tickets are a great deal"', 'opinion'), ('"Everyone online says the tickets are cheap"', 'hearsay'),
          ('"The price is surely fair"', 'opinion'),
          'You can redo 3 x 12.',
          calc=lambda: 3 * 12 == 36),
          ], why='A learner who trusts fluent answers practices the skill of separating how a claim sounds from what '
                 'supports it.')],
    F1=sec('Apply "fluent is not evidence" to real answers', FLU, [
        Q('A chatbot gives a detailed biography of a local artist, including awards. Nothing else online mentions them. What is the most reasonable conclusion?',
          'Some details may be invented; confirm them elsewhere',
          ('The biography must be true because it is detailed', 'detail is not proof'), ('The artist must be famous but very private', 'unsupported guess'),
          ('Search engines must be hiding the awards', 'unsupported guess'),
          'Unconfirmed detail may be invented.'),
        Q('Sara needs a statistic for a speech. The model gives one with no source. What should she do?',
          'Find the original source before using it',
          ('Use it, because it looks precise', 'precision is not proof'),
          ('Use it but round it to sound safer', 'still unchecked'),
          ('Ask the model to sound more confident', 'confidence is not evidence'),
          'A statistic needs a checkable source.'),
        Q('An answer explains a tax rule in formal language. Which step best checks it?',
          'Compare it with the official government page',
          ('Read it again to see if it still sounds right', 'sounding right is not checking'),
          ('Check whether it uses legal vocabulary', 'vocabulary is not evidence'),
          ('Trust it because tax rules are simple', 'they often are not'),
          'An official source is the check.'),
        Q('Which answer feature is the best sign you can verify a claim?',
          'It names a specific source you can look up',
          ('It uses many technical words', 'not evidence'),
          ('It is written in a calm, confident tone', 'not evidence'),
          ('It is longer than other answers', 'not evidence'),
          'A specific, checkable source supports verification.'),
        Q('A model confidently states a store\'s holiday hours. What is the most reliable next step?',
          'Check the store\'s own website or call it',
          ('Trust it because it sounded sure', 'not evidence'),
          ('Ask the model to repeat it', 'repetition is not a check'),
          ('Assume all stores have the same hours', 'unsupported'),
          'Go to the source that controls the fact.'),
    ]),
    F2=sec('Check the claims that matter in a mixed answer', FLU_F2, [
        Q('An answer ends with "This is a verified fact." What does that sentence add?',
          'No evidence; it is also generated text',
          ('Proof that a person verified it first', 'nothing shows that'), ('A legal guarantee of accuracy', 'not a guarantee'),
          ('A link to the verification', 'no link was given'),
          'Self-reassurance is not evidence.'),
        Q('An answer gives four facts; you confirm three are right. What should you assume about the fourth?',
          'Nothing yet; check it too if it matters',
          ('It must be right since the others were', 'errors can hide among correct facts'),
          ('It must be wrong since the others were right', 'unsupported'),
          ('It can be ignored without checking', 'only if it does not matter'),
          'Mixed answers need claim-by-claim checks.'),
        Q("You are deciding whether to buy a used car. A model summary of the car's history is long and fluent. Which claims should you check first?",
          'The claims the decision depends on, like accidents',
          ('The sentence with the friendliest tone', 'tone does not set importance'), ('Only the first sentence, which sets the tone for the rest', 'not about importance'),
          ('None, since a long summary covers everything', 'length is not accuracy'),
          'Focus checks on decision-critical claims.'),
        Q('An answer includes a tidy reference list. What should you do before relying on it?',
          'Open the references to see if they exist and agree',
          ('Trust it, since a reference list proves accuracy', 'lists can be generated'), ('Count the references; more means more accurate', 'count is not quality'),
          ('Delete the list, since references are never real', 'some may be real'),
          'Generated references must be checked.'),
        Q('Why can three correct facts make a fourth wrong fact more dangerous?',
          'The correct facts make the wrong one seem trustworthy',
          ('Wrong facts disappear when mixed with right ones', 'they do not'),
          ('Three correct facts make all facts correct', 'not true'),
          ('Readers always check the fourth fact first', 'unlikely'),
          'Mixed accuracy lowers our guard.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.05
CTX = ('A model can only consider a limited amount of text at once, called its CONTEXT WINDOW, measured in tokens. The '
       'context usually includes instructions the product adds, the conversation so far, any files or pasted text, '
       'and the reply being written. When a long conversation or document exceeds the window, something has to give: '
       'depending on the product, older messages may be dropped or shortened, part of a file may be left out, or the '
       'request may be refused. The model cannot use text that is no longer in its context, so it may "forget" early '
       'details or miss the end of a long document.')
CTX_F2 = ('Even text that fits in the context window is not always used equally well. Models can overlook details '
          'buried in the middle of a very long input, especially when many similar details compete. Practical habits '
          'help: put the most important instructions and facts where they are easy to find, restate key requirements '
          'when a conversation gets long, split very long documents into sections, and check that answers cover the '
          'parts you care about. A bigger context window raises the limit; it does not guarantee careful reading.')

S_LLM05 = SET(
    'AI.LLM.05',
    M=sec('Explain the context window and what happens when it is exceeded', CTX, [
        Q('What is a context window?',
          'The limited amount of text a model can use at once',
          ('The window on screen where the app is shown', 'not this meaning'), ('The time of day when the model is available', 'not this meaning'),
          ('The list of every fact the model learned', 'that is training, not context'),
          'Context is the text the model can use right now.'),
        Q('Which of these is usually part of the context?',
          'The conversation so far and any pasted text',
          ('Every conversation all users have ever had', 'only this request\'s text'),
          ('The model\'s entire training data', 'training data is not the context'),
          ('The user\'s whole computer hard drive', 'only supplied text'),
          'Context holds the current conversation and supplied material.'),
        Q('A very long conversation exceeds the window. What might happen, depending on the product?',
          'Older messages may be dropped or shortened',
          ('The model becomes permanently smarter', 'not related'),
          ('All messages are kept forever with no limit', 'there is a limit'),
          ('The model rewrites its training data', 'not related'),
          'Something must give when the limit is passed.'),
        Q('Why might a model "forget" a detail from the start of a very long chat?',
          'That detail may no longer be in its context',
          ('It chose to ignore the user on purpose', 'not intentional'),
          ('Details from chats are erased from the internet', 'not the reason'),
          ('Models cannot read the first message ever', 'they can if it is in context'),
          'Text outside the context cannot be used.'),
        Q('In what unit is a context window usually measured?', 'Tokens',
          ('Pages', 'not the usual unit'), ('Minutes', 'not a text measure'), ('Megapixels', 'an image measure'),
          'Context limits are counted in tokens.'),
    ]),
    B=[cs('Compare the context window with a whiteboard',
          'Imagine a WHITEBOARD in a meeting room. Everything the group is discussing must be written on it to be '
          'used. The board is big but not endless. When it fills up, someone erases the oldest notes to make room, and '
          'from then on the group cannot look at what was erased. A model\'s context window works like the board: '
          'instructions, the conversation and any pasted text are "written" there. When it fills, older material may '
          'be removed, and the model can no longer use it.', [
              Q('In the comparison, what is the whiteboard like?', 'The context window',
                ('The model\'s training data', 'training is not on the board'), ('The user\'s keyboard', 'not the comparison'),
                ('The company office', 'not the comparison'), 'The board holds what is in use now.'),
              Q('What happens when the board fills up?',
          'The oldest notes are erased',
          ('The board grows forever', 'it is not endless'), ('All notes are kept', 'there is no room'),
          ('The meeting ends at once for everyone', 'not described'),
          'Old material is removed.'),
              Q('Can the group use notes that were erased?', 'No, they are gone from the board',
                ('Yes, the board remembers them', 'erased notes are gone'), ('Yes, if they shout', 'not how it works'),
                ('Only on Fridays', 'nonsense'), 'Erased text cannot be used.'),
              Q('What is written on the board?',
          'Instructions, the chat and pasted text',
          ('Only the newest single word', 'more than that'), ('Everything ever said anywhere in the building', 'only this meeting'),
          ('Nothing at all', 'the board holds the discussion'),
          'The context holds current material.'),
              Q('Why might the group forget a point made at the start?', 'It may have been erased to make room',
                ('It was never said', 'it was said'), ('The board was too small to write on at all', 'it held the point at first'),
                ('Points made first are always wrong', 'not the reason'), 'Early material can be removed.'),
          ], why='A learner who does not see why models "forget" can picture a whiteboard that must be erased when '
                 'full.')],
    F1=sec('Work within a context window', CTX, [
        Q('After two hours of chat, a model ignores a formatting rule Kim gave at the start. What should she try?',
          'Restate the rule in a new message',
          ('Assume the model is broken forever', 'a likely context limit'),
          ('Wait until tomorrow and hope it remembers', 'waiting does not restore context'),
          ('Delete her account', 'unnecessary'),
          'Restating puts the rule back into context.'),
        Q('Omar pastes a 400-page manual, and the answer seems to miss the last chapters. What is a likely reason?',
          'Part of the manual may not fit in the context',
          ('The last chapters were written in code', 'not implied'),
          ('Models refuse to read past page 100 by law', 'not a law'),
          ('The model already knew those chapters', 'not the issue'),
          'Long inputs can exceed the context window.'),
        Q('Which approach helps with a very long document?',
          'Split it into sections and do one at a time',
          ('Paste the whole manual three times to be safe', 'uses even more context'), ('Remove all headings first', 'does not help'),
          ('Send it with no question at all', 'does not help'),
          'Sections keep each request within limits.'),
        Q('A product says its context window is 8,000 tokens. Using about three quarters of a word per token, about how '
          'many words of total conversation can it consider?',
          'About 6,000 words',
          ('About 10,667 words', 'divided instead of multiplying'),
          ('Exactly 8,000 words', 'tokens are not words'),
          ('About 2,000 words', 'subtracted instead'),
          '8,000 x 0.75 = 6,000 words (an estimate).', calc=lambda: 8000 * 0.75 == 6000),
        Q('Why does starting a fresh conversation sometimes fix confused answers?',
          'It clears old text that crowded the context',
          ('It retrains the model from scratch', 'not what a new chat does'),
          ('It switches the user to a paid account', 'not implied'),
          ('It deletes the model\'s parameters', 'not what happens'),
          'A new chat starts with a clean context.'),
    ]),
    F2=sec('Help a model use long input well', CTX_F2, [
        Q('A long report fits in the context, but the answer misses a key figure in the middle. What does this show?',
          'Fitting in the window does not ensure careful use',
          ('The figure must not exist in the report', 'it does'), ('Context windows are always unlimited', 'they are limited'),
          ('Models never read the middle of documents', 'too strong'),
          'Details in the middle can be overlooked.'),
        Q('Where should you put the most important instructions in a long request?',
          'Somewhere easy to find, then restate them',
          ('Hidden in the middle among many other details', 'harder to use'), ('Only in the file name', 'unlikely to be used'),
          ('Nowhere; models guess instructions', 'they need them'),
          'Prominent, repeated instructions help.'),
        Q('A tool advertises a much bigger context window. What can you conclude?',
          'It takes more text; answers still need checking',
          ('It now reads every detail perfectly', 'size is not careful reading'), ('It no longer makes any errors', 'not guaranteed'),
          ('It must use a completely different kind of model', 'not implied'),
          'A bigger limit is not a guarantee.'),
        Q('You need answers about sections 2 and 7 of a long contract. What is a sensible way to check the answer?',
          'Confirm it covers both sections, using the text',
          ('Accept it as long as the answer is long and detailed', 'length is not coverage'), ('Check only section 2', 'misses section 7'),
          ('Assume both were read', 'verify instead'),
          'Check coverage of the parts you care about.'),
        Q('A conversation has many similar product codes. The model mixes two up. What would help?',
          'Restate the key codes clearly in this message',
          ('Add even more similar codes', 'more confusion'), ('Ask the model to sound more confident about them', 'confidence is not accuracy'),
          ('Change the font of the codes', 'irrelevant'),
          'Clear, current restatement reduces mix-ups.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.06
KNOW = ('A model\'s built-in knowledge comes from its training data, which stops at a TRAINING CUTOFF date. It does not '
        'know about events after that date unless the information is SUPPLIED or RETRIEVED during your request: you '
        'paste a document, or the product runs a web search and adds the results to the context. These are '
        'different: built-in knowledge is patterns frozen at training time and may be incomplete or wrong, while '
        'supplied or retrieved text is current material the model reads now, which is only as good as its source. '
        'When an answer depends on recent facts, know which kind you are getting.')
KNOW_F2 = ('Answers often blend both kinds of information, and it is not always obvious which part came from where. A '
           'model might quote a supplied article correctly but fill a gap with older built-in knowledge, or describe '
           'a "latest" product that has since been replaced. Retrieved sources can also be outdated, unreliable or '
           'off-topic. Useful habits: ask the answer to say which statements come from the supplied material, check '
           'the dates of any sources, and confirm time-sensitive facts such as prices, laws, schedules and officials '
           'directly.')

S_LLM06 = SET(
    'AI.LLM.06',
    M=sec('Tell built-in knowledge from supplied or retrieved information', KNOW, [
        Q('What is a training cutoff?',
          'The date after which the training data has no information',
          ('The time limit for typing a question', 'not this meaning'),
          ('The point where a model stops answering for the day', 'not this meaning'),
          ('The maximum number of users at once', 'not this meaning'),
          'Built-in knowledge stops at the cutoff.'),
        Q("A model's training cutoff was before a recent election. How could it still describe the result correctly?",
          'If the result is supplied or retrieved for it',
          ('By guessing based on old patterns', 'a guess is not knowledge'), ('By training itself during the conversation', 'ordinary use does not retrain'),
          ('It cannot ever do so in any situation', 'supplied information makes it possible'),
          'Current information must be supplied or retrieved.'),
        Q('A product runs a web search and adds the results to the request. Which kind of information is that?',
          'Retrieved information read now',
          ('Built-in knowledge from training', 'it was fetched now'), ('A permanent change to the model', 'it does not retrain'),
          ('Information that has no source at all', 'it comes from search results'),
          'Search results are retrieved into the context.'),
        Q('Which statement about retrieved information is accurate?',
          'It is only as good as the source it came from',
          ('It is always correct because it is recent', 'sources can be wrong'),
          ('It permanently updates the model\'s knowledge', 'it does not retrain'),
          ('It is the same as training data', 'it is read during the request'),
          'Retrieved text inherits its source\'s quality.'),
        Q('Which question most needs supplied or retrieved information rather than built-in knowledge?',
          'What are this week\'s opening hours for the city pool?',
          ('What is a noun in English grammar?', 'stable knowledge'),
          ('What is the boiling point of water at sea level?', 'stable knowledge'),
          ('What is a triangle?', 'stable knowledge'),
          'Recent, changing facts need current sources.'),
    ]),
    B=[cs('Compare an encyclopedia on the shelf with today\'s newspaper',
          'A printed ENCYCLOPEDIA on a shelf holds a lot of knowledge, but only up to the year it was printed. It '
          'cannot tell you yesterday\'s news. If you also hand someone TODAY\'S NEWSPAPER, they can read current '
          'events, but the newspaper might contain mistakes, and it does not change the encyclopedia. A model\'s '
          'built-in knowledge is like the encyclopedia: fixed at its training cutoff. Supplied or retrieved text is '
          'like the newspaper: current material read right now.', [
              Q('The encyclopedia is like which kind of information?', 'Built-in knowledge',
                ('Retrieved information', 'that is the newspaper'), ('Neither kind', 'it matches built-in knowledge'),
                ('A web search', 'that would be retrieval'), 'Fixed at printing, like training.'),
              Q("Today's newspaper is like which kind of information?",
          'Supplied or retrieved text',
          ('Built-in knowledge', 'that is the encyclopedia'), ('Training data', 'it is read now'),
          ("The model's trained parameters", 'not stored there'),
          'Current material read now.'),
              Q('Can the encyclopedia tell you yesterday\'s news?', 'No, it stops at its printing date',
                ('Yes, if you read it slowly', 'no'), ('Yes, encyclopedias update themselves', 'printed ones do not'),
                ('Only on weekends', 'nonsense'), 'Built-in knowledge has a cutoff.'),
              Q('Does reading the newspaper change the encyclopedia?', 'No, it stays the same',
                ('Yes, it rewrites the pages', 'no'), ('Yes, it adds a new volume', 'no'),
                ('Only if the news is big', 'no'), 'Supplied text does not retrain the model.'),
              Q('Is the newspaper guaranteed to be correct?', 'No, it can contain mistakes',
                ('Yes, all news is correct', 'not guaranteed'), ('Yes, because it is new', 'new is not correct'),
                ('Only if it is long', 'length is irrelevant'), 'Retrieved sources can be wrong.'),
          ], why='A learner who blends training knowledge with current information can separate them with the '
                 'encyclopedia-and-newspaper picture.')],
    F1=sec('Decide which kind of information an answer needs', KNOW, [
        Q('Ben asks which phone model is newest. The tool does not search the web. What should he expect?',
          'The answer may be out of date, reflecting its training cutoff',
          ('It will always name the newest model released today', 'it has a cutoff'),
          ('It will refuse to mention any phones', 'not implied'),
          ('It will search stores secretly', 'it does not search'),
          'Without retrieval, answers reflect training-time knowledge.'),
        Q('A student pastes this year\'s club rules and asks about meeting times. What is the model using?',
          'The supplied rules in the current request',
          ('Its memory of every club in the world', 'not built-in'),
          ('A web search of the school\'s site', 'nothing was searched'),
          ('A retrained version of itself', 'pasting does not retrain'),
          'Pasted text is supplied information.'),
        Q('Which situation shows retrieval?',
          'The product searches news sites and quotes them',
          ('The model answers from what it learned in training', 'built-in knowledge'), ('The user types a short question with no files', 'no retrieval shown'),
          ('The model writes a poem from imagination', 'no retrieval'),
          'Fetching and quoting sources is retrieval.'),
        Q('A retrieved web page is three years old. What should you do before relying on it?',
          'Check a current source for time-sensitive facts',
          ('Trust it, because it was retrieved by the product', 'old pages can be stale'), ('Assume nothing has changed', 'unsupported'),
          ('Ask the model to make it newer', 'it cannot change the source'),
          'Retrieved information can be outdated.'),
        Q('Which question can a model usually answer from built-in knowledge without current sources?',
          'What does the word "photosynthesis" mean?',
          ("Who won last night's game?", 'needs current information'), ("What is today's exchange rate?", 'needs current information'),
          ('Is the corner store open this holiday weekend?', 'needs current information'),
          'Stable concepts suit built-in knowledge.'),
    ]),
    F2=sec('Untangle blended answers about recent facts', KNOW_F2, [
        Q('An answer quotes a supplied article correctly but adds a detail the article does not contain. Where might '
          'that detail have come from?',
          'Older built-in knowledge or an invented guess',
          ('The supplied article, which must contain it', 'it does not'),
          ('A permanent update to the model', 'not implied'),
          ('A law that requires extra details', 'nonsense'),
          'Blended answers can mix sources.'),
        Q('You want to know which parts of an answer came from your uploaded document. What is a useful request?',
          'Ask it to mark statements taken from the document',
          ('Ask it to sound more confident about everything', 'confidence is not sourcing'), ('Ask for a longer answer', 'length is not sourcing'),
          ('Ask it to stop using the document', 'defeats the purpose'),
          'Labeled sources make checking easier.'),
        Q('A model describes "the latest version" of a product. How should you treat that phrase?',
          'Check, since "latest" may reflect an old cutoff',
          ('Trust it, since models always know the latest', 'cutoffs exist'),
          ('Assume no newer version can exist', 'unsupported'),
          ('Assume it is always wrong', 'too strong'),
          '"Latest" is time-sensitive.'),
        Q('A retrieved source is an unknown blog with no author or date. What is the best step?',
          'Confirm it with a more reliable, dated source',
          ('Trust it, since the product chose to retrieve it', 'retrieval is not endorsement'), ('Use it but remove the link', 'hides the problem'),
          ('Assume blogs are always wrong', 'too strong'),
          'Retrieved sources vary in quality.'),
        Q('Which facts most need direct confirmation even after retrieval?',
          'Prices, laws, schedules and officeholders',
          ('The meaning of common words', 'stable'), ('Basic arithmetic facts', 'stable'),
          ('The plot of a famous novel from long ago', 'stable'),
          'Time-sensitive facts change often.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.07
MEM = ('Two different things can make a chatbot seem to "remember." CONVERSATION CONTEXT is the text of the current '
       'chat that is sent back to the model with each message, so it can refer to what you said earlier in that chat. '
       'SAVED MEMORY (or history features) is something a PRODUCT may offer: it stores notes or past chats and adds '
       'them to future conversations. Saved memory is a product feature, it varies between products, and it can '
       'usually be viewed, turned off or deleted in settings. Neither one retrains the model. Check what a specific '
       'product saves rather than assuming.')
MEM_F2 = ('Memory features raise practical questions. Something you mentioned weeks ago could appear in a new '
          'answer, which may be helpful or unwelcome. Shared devices or shared accounts can expose saved notes to '
          'other people. Turning off memory may not delete chats already stored, and deleting a chat may not remove '
          'information a product saved separately; read what each setting actually does. For sensitive topics, the '
          'safest habit is not to share details you would not want stored, whatever the settings say.')

S_LLM07 = SET(
    'AI.LLM.07',
    M=sec('Tell conversation context from saved memory', MEM, [
        Q("In one chat, you mention your dog's name, and later in the same chat the model uses it. What makes this possible?",
          'The earlier message is still in the chat context',
          ("The model was retrained on your dog's name", 'no retraining happens'), ('The model guessed the name from training data', 'it read it from the chat'),
          ("Every model knows every pet's name", 'not true'),
          'Earlier messages in the chat are part of the context.'),
        Q('A product greets you by name in a brand-new chat. What is the most likely reason?',
          'The product saved a note and added it to the new chat',
          ('The model\'s parameters changed to include your name', 'saved memory is not retraining'),
          ('The model read your mind from your typing', 'not possible'),
          ('All chatbots know every user\'s name', 'not true'),
          'Saved memory is a product feature.'),
        Q('Which statement about saved memory is accurate?',
          'It is a product feature that varies and has settings',
          ("It is part of every language model's design", 'it is a product feature'), ('It permanently retrains the model for every user', 'it does not retrain'),
          ('It can never be viewed or deleted', 'often it can'),
          'Memory varies by product and is usually controllable.'),
        Q('Does conversation context retrain the model?',
          'No; it is just text sent with each message',
          ('Yes; every chat retrains the model', 'not during ordinary use'),
          ('Yes; but only on weekends', 'nonsense'),
          ('No; because context is deleted instantly', 'it is kept for the chat'),
          'Context is supplied text, not training.'),
        Q('A friend says, "All chatbots remember everything forever." What is the best response?',
          'It depends on the product; check its memory settings',
          ('True; every chatbot saves all chats forever', 'products differ'),
          ('False; no chatbot can ever save anything', 'some do'),
          ('True; models store chats in their parameters', 'not how it works'),
          'Memory behavior is product-specific.'),
    ]),
    B=[cs('Compare a conversation with a notebook',
          'Talking to a friend at lunch, you can say "the movie I mentioned" because it came up a few minutes ago: '
          'that is like CONVERSATION CONTEXT. If your friend also keeps a NOTEBOOK and writes "likes horror movies," '
          'then next month they can bring it up again: that is like SAVED MEMORY. The notebook is something extra '
          'that your friend chose to keep, could show you, and could erase. Neither the lunch talk nor the notebook '
          'changes who your friend fundamentally is, just as neither one retrains a model.', [
              Q('Saying "the movie I mentioned" during lunch is like what?',
          'Conversation context',
          ('Saved memory', 'that is the notebook'), ('Training a new model', 'nothing is trained'),
          ('A web search', 'not described'),
          'The current talk holds recent details.'),
              Q('The friend\'s notebook is like what?', 'Saved memory',
                ('Conversation context', 'that is the lunch talk'), ('The model\'s parameters', 'not the comparison'),
                ('A search engine', 'not the comparison'), 'Kept notes carry over to later talks.'),
              Q('Can the friend show you or erase the notebook?',
          'Yes, it is kept separately and can be managed',
          ('No, notebooks like that can never be erased or shown', 'they can'), ('No, it is secret forever', 'not described'),
          ('Only if it is full', 'not required'),
          'Saved memory is often viewable and deletable.'),
              Q('Next month, how could the friend recall "likes horror movies"?', 'By reading the notebook',
                ('By remembering every word of lunch', 'the notebook keeps it'), ('By guessing', 'they wrote it down'),
                ('By asking a stranger', 'not described'), 'Saved notes carry over.'),
              Q('Does keeping a notebook change who the friend is?',
          'No, it is extra information they keep',
          ('Yes, it rewires their brain', 'not the comparison'), ('Yes, they become a new person entirely', 'no'),
          ('Only if the notebook is long', 'no'),
          'Like memory, it does not retrain the model.'),
          ], why='A learner who confuses chat context with saved memory can separate them with a lunch-and-notebook '
                 'picture.')],
    F1=sec('Manage context and memory in practice', MEM, [
        Q('Lia wants a product to stop bringing up her old projects in new chats. What should she check?',
          'The product\'s memory or history settings',
          ('Whether the model needs retraining', 'memory is a product feature'),
          ('Whether her internet is slow', 'unrelated'),
          ('Whether her messages are too short', 'unrelated'),
          'Memory settings control carried-over notes.'),
        Q('In a long chat, a model correctly refers to a recipe from 20 minutes earlier. What does it rely on?',
          'The conversation context from this chat',
          ('A permanent change to its parameters', 'no retraining'),
          ('Every recipe ever written', 'it used this chat'),
          ('A separate saved note from last year', 'not needed here'),
          'Recent chat text is in context.'),
        Q('A product has no memory feature. You start a new chat. Should you expect it to know your earlier chat?',
          'No; you would need to supply the details again',
          ('Yes; every model remembers every past chat', 'not without a memory feature'), ('Yes; the earlier chat retrained it', 'chats do not retrain'),
          ('No; and it will refuse to talk to you', 'it will talk, just without the history'),
          'Without saved memory, new chats start fresh.'),
        Q('Which action is about saved memory rather than conversation context?',
          'Viewing and deleting stored notes in settings',
          ('Scrolling up to reread this chat', 'context'), ('Restating a rule in the current chat window', 'context'),
          ('Pasting a file into this message', 'supplied context'),
          'Stored notes are product memory.'),
        Q('A coworker says, "I told it my preference once, so the model learned it forever." What is more accurate?',
          'A product may have saved a note; the model did not retrain',
          ('Correct; models retrain after each preference', 'they do not'), ('Correct; all preferences are added to its training right away', 'not automatically'),
          ('Wrong; products never save preferences', 'some do'),
          'Saved notes are separate from the model.'),
    ]),
    F2=sec('Handle memory features carefully', MEM_F2, [
        Q('A family shares one account, and a new answer mentions a private detail one member shared. What is the issue?',
          'Saved memory on a shared account can expose details',
          ("The model hacked the family's computer", 'not implied'), ('Memory features never store private details', 'they may'),
          ('This is impossible with any product', 'possible with saved memory'),
          'Shared accounts plus memory can leak details.'),
        Q('Jay turns memory off. Does that automatically delete chats already stored?',
          'Not necessarily; read what the setting does',
          ('Yes, always, in every product', 'products differ'), ('No, chats can never be deleted by anyone', 'often they can'),
          ('Yes, and it retrains the model', 'no retraining'),
          'Check what each setting actually does.'),
        Q('Which is the safest habit for very sensitive details, such as medical history?',
          'Do not share details you would not want stored',
          ('Share them, since settings always protect you', 'settings vary'),
          ('Share them only in long conversations', 'length does not protect'),
          ('Share them with a friendly greeting', 'tone does not protect'),
          'Not sharing is the most reliable protection.'),
        Q('A user deletes a chat but later sees a detail from it in a new answer. What is a possible explanation?',
          'The product saved that detail separately as a note',
          ('Deleting chats retrains the model', 'not how it works'), ("The detail was in the model's original training", 'unlikely for a personal detail'),
          ('The new chat is the same chat', 'it is new'),
          'Saved notes can be separate from chat history.'),
        Q('What is the best source for how a specific product handles memory?',
          'Its own settings and help pages',
          ('A general article about all chatbots', 'too general'),
          ('A friend\'s guess', 'hearsay'),
          ('The model\'s answer about itself, with no documentation', 'may be inaccurate'),
          'Product documentation is the best evidence.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.09
PROD = ('A general description of language models cannot tell you exactly how a particular product will behave. '
        'Products add their own layers: SYSTEM INSTRUCTIONS the company writes (for example, "be brief" or "do not give '
        'medical diagnoses"), SAFETY FILTERS, TOOLS such as web search, code running or file reading, SETTINGS, and '
        'LIMITS on length or usage. Two products built on similar models can therefore refuse different requests, '
        'format answers differently, or have different abilities. To know what a product does, test it on your task '
        'and read its documentation.')
PROD_F2 = ('Products also change. A company may update instructions, add or remove tools, adjust filters, or switch '
           'models, sometimes without obvious notice. A workflow that worked last month can break, and a limit that '
           'blocked you may disappear. Version names, release notes and help pages are the best record. When results '
           'matter, keep a few test cases and rerun them after updates, and avoid building important processes on an '
           'undocumented behavior you happened to notice once.')

S_LLM09 = SET(
    'AI.LLM.09',
    M=sec('Explain why a product\'s behavior is more than its model', PROD, [
        Q('What are system instructions?',
          'Directions the company adds to shape answers',
          ('Questions the user types into the chat box', 'those are user messages'), ('The training data used to build the model', 'not instructions'),
          ('The operating system of your phone', 'not this meaning'),
          'Companies write instructions that guide their product.'),
        Q('Two products use similar models, but one refuses a request the other accepts. What is a likely reason?',
          'Different instructions or filters in each product',
          ('One model must be completely broken', 'usually a product difference'), ('Similar models always behave identically in every product', 'products differ'),
          ('The user typed the request too slowly', 'irrelevant'),
          'Product layers shape refusals.'),
        Q('A product can read your spreadsheet files. Where does that ability come from?',
          'A file-reading tool the product provides',
          ('Every language model reads files by itself', 'tools are product features'),
          ('The model memorized your spreadsheet in training', 'not possible'),
          ('Your spreadsheet program sends answers automatically', 'not how it works'),
          'Tools are added by the product.'),
        Q('What is the best way to learn how a specific product behaves?',
          'Test it on your task and read its documentation',
          ('Read a general description of all language models', 'too general'),
          ('Assume it matches the first chatbot you used', 'products differ'),
          ('Ask a friend who uses a different product', 'different product'),
          'Product-specific testing and docs are best.'),
        Q('Which is an example of a product limit?',
          'A maximum length for each answer',
          ('The patterns learned in training', 'model, not limit'),
          ('The meaning of a word', 'not a limit'),
          ('The user\'s choice of topic', 'not a product limit'),
          'Products set limits on length and usage.'),
    ]),
    B=[cs('Compare a restaurant\'s kitchen with its menu',
          'Two restaurants might buy ingredients from the same supplier, yet their meals differ: each has its own '
          'RECIPES, its own HOUSE RULES ("no substitutions"), its own EQUIPMENT (one has a pizza oven), and its own '
          'PORTION SIZES. Knowing the supplier tells you little about what you will be served. An AI product is '
          'similar: the model is like the supplier\'s ingredients, while the company\'s instructions, filters, tools '
          'and limits are like the recipes, house rules, equipment and portions.', [
              Q('In the comparison, the model is like what?',
          "The supplier's ingredients",
          ('The house rules', 'those are like instructions'), ('The pizza oven', 'that is like a tool'),
          ('The portion sizes it serves', 'those are like limits'),
          'The model is the shared ingredient.'),
              Q('A "no substitutions" rule is like which product layer?',
          'System instructions or filters',
          ("The model's original training", 'not the comparison'), ('The supplier', 'that is the model'),
          ("The user's order", 'not a house rule'),
          'House rules shape what is allowed.'),
              Q('One restaurant has a pizza oven. In AI terms, that is like what?',
          'A tool the product provides',
          ("The model's learned parameters", 'not equipment'), ('A safety filter', 'a filter blocks, a tool enables'),
          ('Training data', 'not equipment'),
          'Equipment enables extra abilities, like tools.'),
              Q('Why can two restaurants using the same supplier serve different meals?',
                'Their recipes, rules, equipment and portions differ',
                ('The supplier changes ingredients for each one', 'same supplier'),
                ('Customers cook the meals themselves', 'not described'),
                ('They cannot; same supplier means same meals', 'they differ'),
                'Layers on top create differences.'),
              Q('Knowing the supplier tells you how much about the meal?', 'Only a little',
                ('Everything about it', 'layers matter'), ('Nothing at all', 'it tells you some'),
                ('Exactly the price', 'not determined'), 'Like knowing the model: helpful but incomplete.'),
          ], why='A learner who assumes a model description predicts every product can see the role of product layers '
                 'through a restaurant example.')],
    F1=sec('Predict and check product behavior', PROD, [
        Q("A school's chatbot refuses to write complete essays, but a public chatbot will. What explains this best?",
          'The school product added limits on essay writing',
          ('The school chatbot cannot write sentences at all', 'it can'), ('Public chatbots ignore all instructions', 'not true'),
          ('Essays cannot be generated by any model', 'the public one did'),
          'Product instructions differ.'),
        Q('An article says "language models cannot browse the web." Your product shows web results. What is true?',
          'Your product adds a browsing tool to its model',
          ('The article proves your product is fake', 'products add tools'),
          ('The model learned the web results in training', 'they were fetched now'),
          ('Browsing is part of every model', 'it is a product tool'),
          'General statements about models may not describe products.'),
        Q('Before relying on a product to summarize contracts, what should a manager do?',
          'Test it on sample contracts and read its documentation',
          ('Trust a general article about language models', 'too general'),
          ('Assume all products summarize equally well', 'they differ'),
          ('Ask the product if it is good at contracts', 'not a test'),
          'Test the specific product on the task.'),
        Q('A product gives very short answers no matter what you ask. What is a likely reason?',
          'Its instructions or settings limit answer length',
          ('The model has run out of words forever', 'not how it works'),
          ('Your device has a broken keyboard', 'unrelated'),
          ('All language models only give short answers', 'not true'),
          'Product settings shape length.'),
        Q('Which statement is most accurate?',
          'Products built on similar models can behave quite differently',
          ('Any two products with similar models act the same', 'layers differ'),
          ('A model description predicts product behavior exactly', 'it does not'),
          ('Products never change how models behave', 'they do'),
          'Product layers matter.'),
    ]),
    F2=sec('Plan for product changes', PROD_F2, [
        Q('A workflow that summarized meeting notes worked last month but now formats answers differently. What is a likely explanation?',
          'The product updated its instructions or model',
          ('The meeting notes became illegal to summarize', 'unlikely'), ('The workflow was never possible', 'it worked before'),
          ("Your computer's clock is wrong", 'unrelated'),
          'Products change over time.'),
        Q('Where is the best record of what changed in a product?',
          'Its release notes and help pages',
          ('A guess from a friend', 'not a record'),
          ('An old screenshot from last year', 'may be outdated'),
          ('The model\'s description of itself with no documentation', 'may be inaccurate'),
          'Official documentation records changes.'),
        Q('A team relies on a product for weekly reports. What habit protects them from surprises?',
          'Keep test cases and rerun them after updates',
          ('Never look at the outputs again once it works', 'risky'), ('Assume updates never affect results', 'they can'),
          ('Switch products every week', 'disruptive'),
          'Retesting catches changes.'),
        Q('You noticed once that a product ignores a filter if you phrase things oddly. Should you build a process on this?',
          'No; undocumented behavior can stop at any time',
          ('Yes; once noticed, it will always work', 'not guaranteed'), ('Yes; odd phrasing is an official feature of the product', 'not documented'),
          ('No; because products never change', 'they do change'),
          'Do not rely on undocumented behavior.'),
        Q('A limit that blocked a request last month is gone. What is the most accurate conclusion?',
          'The product changed its limits; check its documentation',
          ('The model learned on its own to ignore its limits', 'models do not change limits'), ('Limits never existed', 'it existed before'),
          ('The request must now be unsafe', 'unsupported'),
          'Limits are product decisions that change.'),
    ]),
)

SETS = [S_LLM01, S_LLM02, S_LLM03, S_LLM04, S_LLM05, S_LLM06, S_LLM07, S_LLM09]
