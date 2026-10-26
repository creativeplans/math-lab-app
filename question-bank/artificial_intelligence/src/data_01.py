"""Foundation 1: What AI is and where it appears (AI.BASICS.01-07)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.BASICS.01
UMB = ('ARTIFICIAL INTELLIGENCE (AI) is a broad name for computer systems that do tasks we usually connect with human '
       'thinking, such as recognizing speech, sorting photos, predicting what comes next, recommending a song, or '
       'writing a paragraph. It is an umbrella term, not one machine: a spam filter, a map app\'s travel-time estimate '
       'and a chatbot can all be called AI, yet they work differently and do different jobs. Calling something "AI" '
       'does not tell you how well it works or what it can do. To understand a tool, ask what task it performs, what '
       'it takes in, and what it gives back.')
UMB_F2 = ('Because "AI" is a broad label, it is used loosely. Marketers may call a simple fixed rule "AI" to sound '
          'modern, and some tools that do use learned patterns never mention AI at all. Two products both described as '
          '"AI-powered" can differ greatly in quality, cost and risk. When a claim matters, for example when a school, '
          'employer or bank says AI helps make a decision, look past the label: ask what the system does, what '
          'information it uses, how it was tested, and who checks its results. A label is a starting point for '
          'questions, not an answer.')

S_BASICS01 = SET(
    'AI.BASICS.01',
    M=sec('Describe AI as a broad term for systems that do thinking-like tasks', UMB, [
        Q('Which description fits this course\'s meaning of AI?',
          'A broad name for computer systems that do tasks linked with human thinking',
          ('One specific robot that thinks in exactly the same way as a person', 'AI is a broad group, not one robot'),
          ('Any computer program at all, including a basic pocket calculator', 'AI refers to tasks like recognizing, '
           'predicting, recommending and generating'),
          ('A single website that answers questions in a chat window', 'chatbots are only one kind of AI'),
          'AI is an umbrella term for many kinds of systems that do thinking-like tasks.'),
        Q('A phone groups photos by the faces in them, a music app suggests songs, and a chatbot writes a poem. Which '
          'statement is accurate?',
          'All three can be called AI, but they do different jobs',
          ('Only the chatbot counts as AI, because it writes words', 'recognizing and recommending are AI tasks too'),
          ('All three must run on the very same AI system inside', 'different tools work differently'),
          ('None of them counts as AI, since each does only one task', 'doing one task does not stop a system being AI'),
          'Recognizing faces, recommending songs and writing text are all AI tasks, done by different systems.'),
        Q('A product box says "Now with AI!" What does that label tell you by itself?',
          'Only that some feature uses AI, not how well it works',
          ('That the product now thinks the way a person thinks', 'the label says nothing about human-like thinking'),
          ('That it is more accurate than every older version', 'a label is not evidence of accuracy'),
          ('That every feature in the product learned from data', 'the label may describe just one feature'),
          'A label names a category; it does not describe quality or abilities.'),
        Q('Which three questions does the passage suggest asking about any AI tool?',
          'What task it does, what it takes in, and what it gives back',
          ('Who invented it, what year it came out, and what it costs', 'these do not explain what the tool does'),
          ('How popular it is, how new it is, and who recommends it', 'popularity does not explain the task'),
          ('Whether it has a robot body, a voice and a face', 'most AI has none of these'),
          'Task, input and output describe what a tool actually does.'),
        Q('A spam filter moves suspicious emails into a junk folder. Which AI task is it doing?',
          'Sorting each email into a category',
          ('Writing new emails for the user', 'it does not write anything'),
          ('Recommending new contacts to add', 'it does not suggest contacts'),
          ('Translating emails into other languages', 'it does not translate'),
          'Deciding "junk" or "not junk" is sorting into categories, a recognition task.'),
    ]),
    B=[cs('See "AI" as a broad label, like the word "vehicle"',
          'Think of the word VEHICLE. A bicycle, a bus and a cargo ship are all vehicles, but you would not expect a '
          'bicycle to cross an ocean. "Vehicle" names a broad group, not one machine, and knowing that something is a '
          'vehicle tells you little about its speed or range. "AI" works the same way. It names a broad group of '
          'computer systems that do tasks such as recognizing, predicting, recommending or generating. Knowing that '
          'something is "AI" tells you little about what it can do. You learn more by asking what job it does.', [
              Q('Why is "vehicle" a good comparison for "AI" in the passage?',
                'Both words name a broad group of different things',
                ('Both words describe machines that have engines', 'many AI systems are not machines with engines'),
                ('Both words describe ways of moving people around', 'AI does not move people'),
                ('Both words describe one machine with many parts', 'both name groups, not one machine'),
                'Each word covers many different things that work differently.'),
              Q('Knowing that a tool is "AI" is like knowing that something is "a vehicle." What does that alone tell '
                'you?',
                'Very little about what it can actually do',
                ('Exactly how accurate and how fast it is', 'the label gives no measurements'),
                ('That it can do any job that a person can', 'the label promises no such thing'),
                ('That it is safe to use for any purpose', 'the label says nothing about safety'),
                'A broad label leaves out the details that matter.'),
              Q('Which question tells you more about an AI tool?',
                'What job does it do?',
                ('Is it labeled "AI"?', 'the label is broad'),
                ('Is its logo modern?', 'appearance is not ability'),
                ('Is it a new release?', 'newness is not ability'),
                'Asking about its job tells you what it is for.'),
              Q('A bus and a bicycle are both vehicles. A chatbot and a photo-tagging tool are both what?',
                'AI systems that do different jobs',
                ('the same AI system with two names', 'they are different systems'),
                ('chatbots that only write text', 'a photo tagger is not a chatbot'),
                ('tools that cannot be called AI', 'both can be called AI'),
                'Like vehicles, AI systems share a label but differ.'),
              Q('Which task fits the passage\'s list of AI tasks (recognizing, predicting, recommending, generating)?',
                'Suggesting a movie you might enjoy',
                ('Saving a file when you click Save', 'an ordinary command, not one of the listed tasks'),
                ('Turning the screen brightness up', 'an ordinary command, not one of the listed tasks'),
                ('Printing the page you selected', 'an ordinary command, not one of the listed tasks'),
                'Suggesting a movie is recommending.'),
          ], why='A learner who misses MAIN often treats "AI" as one specific machine; an everyday word for a broad '
                 'group shows why the label alone says little.')],
    F1=sec('Apply the broad meaning of AI to real claims', UMB, [
        Q('Lena\'s school announces an "AI tutor." What is the most useful first question to ask?',
          'What exactly will it help students do?',
          ('Is it smarter than all the teachers?', 'a vague comparison, not a description of the task'),
          ('Is it the same AI as every chatbot?', 'AI tools differ'),
          ('Which company made its logo and colors?', 'branding does not describe the task'),
          'Start with the task: what it does for students.'),
        Q('A store\'s website says its prices are "set by AI." Which statement is accurate?',
          'Some system helps set prices; the label alone does not say how',
          ('A robot employee chooses each price by hand', 'AI here means software, not a robot worker'), ('The prices must be the lowest prices available anywhere', 'the label says nothing about low prices'),
          ('A chatbot writes out every price for the store', 'pricing AI is usually not a chatbot'),
          'The label tells you a system is involved, not how it works or how well.'),
        Q('Marcus says, "My map app isn\'t AI because it doesn\'t talk to me." What is wrong with his reasoning?',
          'AI also includes systems that predict, like travel times',
          ('Map apps are never allowed to use any kind of AI', 'many map apps do use predictions'), ('Nothing; only talking systems can be called AI at all', 'AI is broader than talking systems'),
          ('AI means a robot, so an app can never qualify', 'AI usually means software'),
          'Predicting travel time is an AI task even without conversation.'),
        Q('A job ad asks for "experience with AI." What should an applicant clarify?',
          'Which AI tools or tasks the job actually involves',
          ('Whether the employer owns a humanlike robot', 'AI work rarely involves robots'),
          ('Whether AI is one program that everyone uses', 'AI is not one program'),
          ('Whether the job needs building a human mind', 'unrealistic and not what such ads mean'),
          'Because "AI" is broad, the specific tools and tasks matter.'),
        Q('Two friends argue about whether a smart thermostat that learns your schedule is AI. Which response fits the '
          'passage best?',
          'It can be called AI; what matters is the task it performs',
          ('It cannot be AI because it has no screen', 'a screen is not required'),
          ('It counts as AI only if it can hold a conversation', 'conversation is not required'),
          ('It counts as AI only if it is as smart as a person', 'AI systems are usually narrow'),
          'Learning a schedule to predict settings is an AI task; the useful question is what it does.'),
    ]),
    F2=sec('Look past an "AI" label when a decision matters', UMB_F2, [
        Q('A budgeting app calls itself "AI-powered," but it only applies one fixed rule: save 10 percent of each deposit. What is the best conclusion?',
          'The label may be marketing; a fixed rule is doing the work',
          ("It must be learning from millions of other users' data", 'nothing suggests learning'), ('It is more reliable because it says "AI-powered"', 'a label is not evidence'),
          ('It cannot work, since it is not "real" AI', 'a fixed rule can work fine'),
          'Labels are used loosely; look at what the system actually does.'),
        Q('Two résumé-screening tools are both described as "AI-powered." What should a hiring manager compare?',
          'What each checks, how it was tested, and who reviews results',
          ('Which one uses the word "AI" more often', 'word count says nothing about quality'),
          ('Which one has the newer logo and website', 'design says nothing about quality'),
          ('Nothing, since the same label means the same quality', 'same label, possibly very different quality'),
          'Quality and risk come from what the tool does and how it was checked.'),
        Q('A bank says AI helps decide loan applications. Which question looks past the label?',
          'What information is used, and can a person review it?',
          ('Is it the same AI that powers popular chatbots?', 'does not reveal how decisions are made'),
          ('Does the AI have a friendly name and avatar?', 'irrelevant to how decisions are made'),
          ('Is this year\'s AI newer than last year\'s AI?', 'newness is not a check'),
          'Ask about inputs, testing and human review.'),
        Q('A photo app\'s background-blur feature never mentions AI, but it learned from many example photos. Which '
          'statement is accurate?',
          'It may use AI even though it does not say so',
          ('It cannot use AI, because AI is never mentioned', 'labels are used loosely in both directions'),
          ('It must secretly be a chatbot underneath', 'learning from photos does not make it a chatbot'),
          ('Only features that are advertised can learn from data', 'unadvertised features can learn too'),
          'Some tools use learned patterns without the label.'),
        Q('A news story says a city "used AI" to plan bus routes. What would you need to know before judging the plan?',
          'What the system did, what data it used, and how it was checked',
          ('Whether the city also uses AI for its parking meters', 'unrelated systems'),
          ('Whether AI is a popular topic in the news this year', 'popularity is not evidence'),
          ('Whether the headline used the word "AI" in large type', 'headline wording is not evidence'),
          'A label starts the questions; the task, data and checks answer them.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.02
RULES = ('Some software follows RULES that a person wrote: "If the total is over 50 dollars, apply free shipping." Every '
         'step was decided in advance, so you can read the rule to see why the program acted. Other systems LEARN '
         'PATTERNS from examples. A spam filter shown thousands of emails marked "spam" or "not spam" adjusts itself '
         'until it sorts new emails well. No one wrote a rule for every case; its behavior comes from the examples it '
         'learned from. Rule-based software is predictable but cannot handle cases its rules miss. Learned systems '
         'handle messy, varied input but can make surprising mistakes.')
RULES_F2 = ('Many real products mix both approaches. A learned model might flag a bank transaction as unusual, and then '
            'a written rule decides what happens next, such as "hold any flagged payment over 1,000 dollars." When '
            'something goes wrong, the fix depends on which part failed. A wrong written rule can be found and '
            'rewritten. A learned pattern usually changes only by retraining with better or more examples, and its '
            'mistakes can be harder to explain. Rules give predictability where it matters most; learning helps with '
            'variety that rules cannot list in advance.')

S_BASICS02 = SET(
    'AI.BASICS.02',
    M=sec('Tell written rules from learned patterns', RULES, [
        Q('A checkout page gives free shipping whenever an order is over 50 dollars. How was this behavior most '
          'likely produced?',
          'A person wrote a rule for it',
          ('It learned from many past orders', 'a fixed threshold is a written rule'),
          ('It guessed the amount at random', 'the result is consistent, not random'),
          ('It copied what a chatbot suggested', 'nothing suggests a chatbot is involved'),
          'A fixed "if over 50, then free" step is a written rule.'),
        Q('A spam filter was shown thousands of emails labeled "spam" or "not spam" and now sorts new emails. Where '
          'does its behavior mainly come from?',
          'Patterns learned from the labeled examples',
          ('A rule written for every possible email', 'no one could write a rule for every email'),
          ('The user approving each email by hand first', 'the filter sorts automatically'),
          ('A list of every spam email ever sent', 'it generalizes from examples instead'),
          'Its behavior was learned from labeled examples.'),
        Q('Which is an advantage of rule-based software?',
          'You can read the rule to see why it acted',
          ('It handles any situation, even ones nobody planned', 'rules miss unplanned cases'),
          ('It improves on its own as it sees more data', 'rules change only when someone edits them'),
          ('It never needs anyone to update it over time', 'rules may need updating when needs change'),
          'Written rules are predictable and readable.'),
        Q('Which is a common weakness of a system that learned from examples?',
          'It can make surprising mistakes on unusual inputs',
          ('It can follow only one fixed rule at a time', 'that describes simple rule software'),
          ('It can never handle messy or varied input', 'learned systems often handle variety well'),
          ('It must be rewritten by hand for each new case', 'it generalizes from examples instead'),
          'Learned behavior can fail in unexpected ways.'),
        Q('A thermostat turns the heat on at exactly 6:00 a.m. every weekday. Which describes it?',
          'A written rule that runs on a schedule',
          ('A learned pattern from the family\'s habits', 'a fixed time set in advance is a rule'),
          ('A chatbot predicting the weather each day', 'nothing here is a chatbot or a forecast'),
          ('A model trained on thousands of houses', 'no training is needed for a fixed time'),
          'A fixed schedule is a written rule.'),
    ]),
    B=[cs('Compare a recipe with learning by tasting',
          'Imagine two cooks. The first follows a RECIPE exactly: "Add 2 teaspoons of salt." If the recipe is right, '
          'the soup is right, and if anyone asks why, the cook points to the recipe. The second cook LEARNED BY '
          'TASTING hundreds of soups and adjusting until they tasted good. She can handle new ingredients the recipe '
          'never mentions, but she cannot always explain exactly why she added what she did, and sometimes she gets a '
          'new dish wrong. Rule-based software is like the recipe cook. Systems that learn patterns from examples are '
          'like the tasting cook.', [
              Q('Which cook is like rule-based software?',
                'The one who follows the recipe exactly',
                ('The one who learned by tasting many soups', 'that cook learned patterns'),
                ('The one who changes the recipe at random', 'neither cook works at random'),
                ('The one who refuses to cook new dishes', 'not described in the passage'),
                'A recipe is a set of written rules.'),
              Q('Why can the recipe cook explain her soup easily?',
                'She can point to the written steps',
                ('She tasted hundreds of soups first', 'that is the other cook'),
                ('She guesses differently each time', 'she follows fixed steps'),
                ('She asks the diners to decide', 'not in the passage'),
                'Written rules can be read back as the explanation.'),
              Q('What can the tasting cook do that the recipe cook cannot?',
          'Handle ingredients the recipe never mentions',
          ('Always explain each choice exactly', 'she often cannot explain exactly'), ('Get every new dish right every time', 'she sometimes gets new dishes wrong'),
          ('Follow a written recipe exactly, step by step', "that is the recipe cook's method"),
          'Learning from many examples helps with new situations.'),
              Q('What is a weakness of the tasting cook?',
                'She sometimes gets a new dish wrong',
                ('She cannot handle any new ingredient', 'she handles new ingredients well'),
                ('She needs the recipe for every step', 'she does not use a recipe'),
                ('She never adjusts what she does', 'she adjusts constantly'),
                'Learned skill can fail in surprising ways.'),
              Q('A system learned to recognize birds from thousands of labeled photos. Which cook is it like?',
                'The tasting cook',
                ('The recipe cook', 'no one wrote bird rules'),
                ('Neither cook', 'it matches the tasting cook'),
                ('Both cooks equally', 'it learned rather than followed rules'),
                'Learning from examples matches the tasting cook.'),
          ], why='A learner who confuses the two kinds of software benefits from a familiar contrast between following a '
                 'recipe and learning by experience.')],
    F1=sec('Decide whether a task suits rules or learned patterns', RULES, [
        Q('A library wants to charge 25 cents per day for each overdue book. Which approach fits best?',
          'A written rule, because the policy is exact and simple',
          ('A learned model trained on years of borrowing data', 'unnecessary for an exact policy'),
          ('A chatbot that guesses a fair fee for each reader', 'fees should be exact, not guessed'),
          ('A model that learns each librarian\'s fee habits', 'the policy is already fixed'),
          'An exact, simple policy is best written as a rule.'),
        Q('An app must recognize handwritten numbers written by thousands of different people. Which approach fits best?',
          'Learning patterns from many labeled examples',
          ('One written rule for each person\'s handwriting', 'impossible to list every style'),
          ('A fixed rule checking that every 7 has a line', 'handwriting varies too much'),
          ('Asking users to type each number instead', 'avoids the task rather than doing it'),
          'Messy, varied input is where learned patterns help.'),
        Q('A school rule says any student absent 3 days in a row gets a call home. Which approach should run it?',
          'A written rule that checks for 3 days in a row',
          ('A model trained to guess which families want calls', 'the policy is already exact'),
          ('A model that learns from past principals\' choices', 'the school wants its exact rule followed'),
          ('A chatbot that decides case by case each morning', 'case-by-case guessing breaks the rule'),
          'An exact policy should run as a readable rule.'),
        Q('A photo service wants to suggest "beach" or "forest" tags for vacation pictures. Which approach fits best?',
          'A model that learned from many labeled photos',
          ('A rule that checks whether a file name says "beach"', 'file names are often unrelated'),
          ('A rule that marks every photo taken in July "beach"', 'dates do not show scenes'),
          ('Asking a person to tag every photo by hand forever', 'possible but not the AI approach asked about'),
          'Recognizing scenes from pixels needs learned patterns.'),
        Q('Which situation most needs the predictability of written rules?',
          'Calculating sales tax that the law sets as an exact rate',
          ('Recognizing which animal appears in a photo', 'varied images suit learned patterns'),
          ('Suggesting songs a listener might enjoy next', 'preferences suit learned patterns'),
          ('Sorting thousands of customer comments by topic', 'varied text suits learned patterns'),
          'An exact legal rate should be computed by a rule.'),
    ]),
    F2=sec('Find which part failed in a system that mixes rules and learning', RULES_F2, [
        Q('A bank\'s model flags a normal grocery purchase as unusual, and a written rule then holds the payment. '
          'Which part made the first mistake?',
          'The learned model that flagged the purchase',
          ('The written rule that held the payment', 'it did what it was written to do'),
          ('The customer who bought the groceries', 'the purchase was normal'),
          ('The grocery store\'s card reader', 'nothing suggests the reader failed'),
          'The error began with the learned flag; the rule only followed it.'),
        Q('A written rule says "hold flagged payments over 100 dollars," but the bank meant 1,000. How can this be '
          'fixed?',
          'Rewrite the rule with the correct amount',
          ('Retrain the model on more transactions', 'the model is not the problem'),
          ('Wait for the rule to learn the right amount', 'written rules do not learn'),
          ('Remove the learned model from the system', 'the model was not at fault'),
          'A wrong written rule is found and rewritten.'),
        Q('A learned model keeps misreading a new style of receipt. What is the usual way to improve it?',
          'Retrain it with examples of the new receipts',
          ('Edit one line of its rules by hand', 'learned patterns are not written lines'), ('Tell it the correct answer once in a chat', 'a chat does not retrain the model'),
          ('Make the receipts look like old ones', 'unrealistic and avoids the problem'),
          'Learned patterns usually change through retraining with better examples.'),
        Q('Why might a designer use a written rule for the final payment decision even when a model flags cases?',
          'Rules give predictable results where it matters most',
          ('Rules can recognize unusual payments by themselves', 'recognition is the model\'s job'),
          ('Rules never need to be checked or updated', 'rules still need review'),
          ('Rules handle every possible case automatically', 'rules only cover listed cases'),
          'Combining them uses learning for variety and rules for predictability.'),
        Q('A customer asks why their payment was held. Which part is easier to explain?',
          'The written rule about which flagged payments are held',
          ('The exact reason the model flagged the payment', 'learned patterns can be hard to explain'),
          ('Neither part can ever be explained at all', 'the rule can be read'),
          ('Both parts are always equally easy to explain', 'learned patterns are usually harder'),
          'The rule can be read; the learned flag may be harder to explain.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.03
MLDL = ('MACHINE LEARNING is a way of building AI in which a system improves at a task by learning patterns from data '
        'instead of following only hand-written rules. DEEP LEARNING is one kind of machine learning. It uses NEURAL '
        'NETWORKS: many connected layers of simple math units. Each layer passes numbers to the next, and early layers '
        'pick up simple features while later layers combine them into more complex ones. "Deep" means many layers, not '
        'deep understanding. So the ideas nest like boxes: deep learning sits inside machine learning, which sits '
        'inside AI. Not all AI uses machine learning, and not all machine learning is deep learning.')
MLDL_F2 = ('People often use these terms loosely, so read claims carefully. "Neural network" borrows a word from '
           'biology, but these networks are math, not brains: the comparison helped early researchers and can mislead '
           'beginners. "Deep" counts layers; it does not mean wise or thoughtful. Deep learning often needs much more '
           'data and computing power than simpler machine learning, and simpler methods can work as well on small, '
           'tidy problems such as predicting sales from a few numbers. Choosing an approach depends on the task, the '
           'data available and the need to explain results.')

S_BASICS03 = SET(
    'AI.BASICS.03',
    M=sec('Explain how AI, machine learning and deep learning nest', MLDL, [
        Q('How are AI, machine learning and deep learning related?',
          'Deep learning is part of machine learning, which is part of AI',
          ('AI is part of deep learning, which is part of machine learning', 'the nesting is reversed'),
          ('They are three different words for exactly the same thing', 'each is a narrower group'),
          ('Machine learning and deep learning are unrelated to AI', 'both are kinds of AI'),
          'The groups nest: deep learning inside machine learning inside AI.'),
        Q('What does "deep" mean in "deep learning"?',
          'The network has many layers',
          ('The system understands ideas deeply', '"deep" is about layers, not understanding'),
          ('The training data is kept hidden', 'not what "deep" refers to'),
          ('The model is very old and stable', 'not what "deep" refers to'),
          '"Deep" counts layers in the network.'),
        Q('What is the key idea of machine learning?',
          'A system improves at a task by learning patterns from data',
          ('A person writes a separate rule for every possible case', 'that describes rule-based software'),
          ('A computer copies human brain cells into a chip', 'not what machine learning means'),
          ('A program stores every answer and repeats it', 'learning patterns is not memorizing every answer'),
          'Machine learning learns from data instead of only following written rules.'),
        Q('In a neural network, what do the layers do?',
          'Pass numbers along, turning simple features into complex ones',
          ('Store a separate copy of every training example', 'layers transform numbers, not stored copies'), ('Hold the written rules that a programmer typed', 'learned weights, not typed rules'),
          ('Connect the computer to the internet to look up answers', 'layers are math steps, not connections'),
          'Layers transform numbers step by step.'),
        Q('Which statement is accurate?',
          'Some AI uses no machine learning at all',
          ('All AI is deep learning by definition', 'deep learning is only part of AI'),
          ('All machine learning uses deep neural networks', 'many methods are not deep learning'),
          ('Deep learning is a separate field from AI', 'it is inside AI'),
          'Rule-based systems can count as AI without machine learning.'),
    ]),
    B=[cs('Picture nested boxes',
          'Picture three boxes that fit inside each other. The biggest box is labeled ARTIFICIAL INTELLIGENCE: any '
          'computer system doing thinking-like tasks. Inside it sits a smaller box, MACHINE LEARNING: AI that learns '
          'patterns from data. Inside that sits the smallest box, DEEP LEARNING: machine learning that uses neural '
          'networks with many layers. Everything in a small box is also in the boxes around it, but the big box holds '
          'other things too. A chess program built only from hand-written rules sits in the AI box but outside the '
          'machine learning box.', [
              Q('Which is the biggest box?',
          'Artificial intelligence',
          ('Deep learning', 'the smallest box'), ('Machine learning box', 'the middle box'),
          ('Neural network', 'a tool used in deep learning'),
          'AI is the outer box.'),
              Q('Where does deep learning sit?', 'Inside machine learning',
                ('Outside the AI box', 'it is inside AI'), ('Around machine learning', 'it is inside, not around'),
                ('Beside AI, not in it', 'it is inside AI'),
                'Deep learning is the smallest, innermost box.'),
              Q('A deep learning system is in which boxes?', 'All three boxes',
                ('Only the deep learning box', 'inner boxes are also inside the outer ones'),
                ('Only the AI box', 'it is also in the inner boxes'),
                ('None of the boxes', 'it is in all of them'),
                'Something in the smallest box is in every box around it.'),
              Q('A chess program built only from hand-written rules is in which box?', 'The AI box only',
                ('The deep learning box', 'it does not learn'), ('The machine learning box', 'it does not learn'),
                ('No box at all', 'it does a thinking-like task, so it is AI'),
                'Rules alone can be AI without machine learning.'),
              Q('What puts something in the machine learning box?', 'It learns patterns from data',
                ('It has many hand-written rules', 'that does not involve learning'),
                ('It has a robot body', 'a body is not required'),
                ('It runs on a fast computer', 'speed is not learning'),
                'Learning from data defines machine learning.'),
          ], why='A learner who mixes up the three terms can sort them with a simple picture of nested boxes before '
                 'applying them.')],
    F1=sec('Classify systems as AI, machine learning or deep learning', MLDL, [
        Q('A tool sorts emails using only rules a person wrote, such as "if the subject contains FREE, mark as junk." '
          'Which label fits best?',
          'AI built from rules, not machine learning',
          ('Deep learning with many network layers', 'no learning is involved'),
          ('Machine learning trained on labeled emails', 'it only follows written rules'),
          ('Not AI, because it cannot write emails', 'writing is not required to be AI'),
          'Hand-written rules can be AI without machine learning.'),
        Q('An app recognizes plant species from photos using a neural network with dozens of layers. Which label is '
          'most specific?',
          'Deep learning',
          ('Machine learning only, not deep learning', 'dozens of layers make it deep learning'),
          ('Rule-based AI without learning', 'it learned from data'),
          ('Not AI, since it only looks at pictures', 'recognition is an AI task'),
          'A many-layered neural network is deep learning, the most specific label.'),
        Q("A shop predicts next week's sales from past weekly sales using a simple formula fitted to the data, with no neural network. Which label fits?",
          'Machine learning that is not deep learning',
          ('Deep learning, since it learns from data', 'no many-layered network is used'), ('Not AI, since it predicts numbers', 'prediction can be machine learning'),
          ('Rule-based AI written by hand', 'the formula was fitted to data'),
          'Fitting a simple model to data is machine learning without deep learning.'),
        Q('Someone says, "It uses deep learning, so it truly understands." What is the best response?',
          '"Deep" means many layers, not understanding',
          ('That is right; deep systems understand meaning', '"deep" refers to layers'),
          ('That is right; neural networks are real brains', 'they are math, not brains'),
          ('Deep learning cannot be used for language tasks', 'it often is'),
          'The word "deep" describes structure, not understanding.'),
        Q('Which example sits in the machine learning box but not the deep learning box?',
          'A model fitted to past data with no neural network',
          ('A list of rules typed in by a programmer by hand', 'that is not machine learning'), ('A neural network with forty layers', 'that is deep learning'),
          ('A calculator adding two numbers', 'that is not machine learning'),
          'Machine learning includes methods without deep neural networks.'),
    ]),
    F2=sec('Read claims about neural networks and deep learning carefully', MLDL_F2, [
        Q('An ad says its "neural network works just like a human brain." What is the problem with this claim?',
          'Neural networks are math inspired by a biology word, not brains',
          ('Neural networks are physically built from brain cells', 'they are software and math'),
          ('Nothing; that comparison is scientifically exact', 'the comparison is loose'),
          ('Neural networks cannot be used in any products', 'they are used widely'),
          'The brain comparison is a loose analogy.'),
        Q('A small business has 200 rows of tidy sales numbers and wants a simple forecast it can explain. What does '
          'the passage suggest?',
          'A simpler method may work as well and be easier to explain',
          ('Deep learning is always required for any forecast', 'not for small, tidy problems'),
          ('Forecasting is impossible without a neural network', 'simple methods can forecast'),
          ('More layers always produce more accurate forecasts', 'not on small, tidy data'),
          'Choose the approach that fits the task, data and need to explain.'),
        Q('Which is a common cost of deep learning compared with simpler methods?',
          'It often needs more data and computing power',
          ('It can only handle a few numbers at a time', 'it handles large inputs'),
          ('It cannot learn from examples at all', 'it learns from examples'),
          ('It must be written by hand line by line', 'it is trained, not hand-written'),
          'Deep learning often needs more data and computing.'),
        Q('A headline says, "Deep AI now thinks deeply about your questions." What should a careful reader conclude?',
          'The headline mixes up "deep" (layers) with deep thought',
          ('The system has been proven to reflect like a person', 'nothing proves that'),
          ('"Deep" means the system was trained for a long time', '"deep" means many layers'),
          ('All AI is now deep learning, so it thinks', 'not all AI is deep learning'),
          'The headline uses "deep" loosely.'),
        Q('A team must explain each decision to customers and has little data. Which consideration matters most when choosing an approach?',
          'Whether the method can be explained with this data',
          ('Whether the method has the most layers possible', 'more layers can make explaining harder'), ('Whether the method is described as "deep"', 'the label does not matter'),
          ('Whether competitors call their tools neural', "competitors' labels are irrelevant"),
          'Task, data and the need to explain should guide the choice.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.04
JOBS = ('Most everyday AI does one of four kinds of jobs. RECOMMENDING suggests items you might want, such as videos, '
        'products or friends. RECOGNIZING (also called classifying) puts input into categories: a face in a photo, a '
        'spoken word, a fraudulent payment. FORECASTING predicts a number or event, such as tomorrow\'s temperature, '
        'travel time or next month\'s sales. GENERATING creates new content: text, images, audio or code. One app can '
        'do several jobs, for example recognizing your voice and then generating a reply. Naming the job helps you '
        'decide what could go wrong and how to check the result.')
JOBS_F2 = ('Each job fails in its own way, so naming the job tells you what to check. A RECOMMENDER can keep showing '
           'more of the same and miss what you actually need. A RECOGNIZER can put things in the wrong category, '
           'especially with unusual examples. A FORECAST can miss sudden changes that never appeared in past data. A '
           'GENERATOR can produce fluent content that is false or copied. When one app chains jobs together, an early '
           'mistake can spread: if your speech is misrecognized, the generated reply answers the wrong question.')

S_BASICS04 = SET(
    'AI.BASICS.04',
    M=sec('Classify an AI use as recommending, recognizing, forecasting or generating', JOBS, [
        Q('A video site shows "Up next" suggestions based on what you watched. Which job is this?', 'Recommending',
          ('Recognizing', 'it is not putting input into categories'), ('Forecasting', 'it is not predicting a number'),
          ('Generating', 'it is not creating new content'),
          'Suggesting items you might want is recommending.'),
        Q('A phone unlocks when it identifies its owner\'s face. Which job is this?', 'Recognizing',
          ('Recommending', 'it does not suggest anything'), ('Forecasting', 'it does not predict a future value'),
          ('Generating', 'it does not create content'),
          'Identifying the face puts the input into a category.'),
        Q('A weather app predicts a 70 percent chance of rain tomorrow. Which job is this?', 'Forecasting',
          ('Recognizing', 'it is predicting, not sorting what is there'), ('Recommending', 'it suggests no items'),
          ('Generating', 'a probability is a forecast, not new content'),
          'Predicting a future event is forecasting.'),
        Q('A tool writes a birthday poem from a short description. Which job is this?', 'Generating',
          ('Recognizing', 'it creates rather than categorizes'), ('Forecasting', 'it predicts no future value'),
          ('Recommending', 'it suggests no existing items'),
          'Creating new text is generating.'),
        Q('A voice assistant hears "What\'s the weather?" and then writes a spoken reply. Which jobs does it do?',
          'Recognizing speech, then generating a reply',
          ('Only recommending a weather app to install', 'it recognizes and replies'),
          ('Only forecasting what the user will ask next', 'it recognizes the actual question'),
          ('Only generating; no recognition is needed', 'it must first recognize the spoken words'),
          'One app can chain jobs: recognize, then generate.'),
    ]),
    B=[cs('Match each job to a familiar helper',
          'Think of four helpers in a shop. The SALES CLERK says, "People who bought this also liked that": '
          'recommending. The CASHIER scans an item and knows it is a banana, not a lemon: recognizing. The MANAGER '
          'looks at past weeks and says, "We will sell about 300 loaves on Saturday": forecasting. The SIGN PAINTER '
          'creates a brand-new poster for a sale: generating. AI systems do these same four kinds of jobs, just with '
          'software instead of people.', [
              Q('The cashier knows a scanned item is a banana. Which job is that?', 'Recognizing',
                ('Recommending', 'that is the clerk'), ('Forecasting', 'that is the manager'),
                ('Generating', 'that is the sign painter'), 'Identifying an item is recognizing.'),
              Q('The manager predicts Saturday bread sales. Which job is that?', 'Forecasting',
                ('Recognizing', 'nothing is being identified'), ('Generating', 'no new content is made'),
                ('Recommending', 'nothing is suggested to a buyer'), 'Predicting future sales is forecasting.'),
              Q('Which helper is generating?', 'The sign painter',
                ('The cashier', 'recognizes'), ('The manager', 'forecasts'), ('The sales clerk', 'recommends'),
                'Creating a new poster is generating.'),
              Q('"People who bought this also liked that" matches which job?', 'Recommending',
                ('Forecasting', 'no future number is predicted'), ('Recognizing', 'nothing is identified'),
                ('Generating', 'nothing new is created'), 'Suggesting items is recommending.'),
              Q('An app predicts how many minutes your bus will take. Which shop helper does the same kind of job?',
                'The manager',
                ('The cashier', 'recognizes items'), ('The sign painter', 'creates new posters'),
                ('The sales clerk', 'suggests products'),
                'Predicting a number is forecasting, like the manager.'),
          ], why='A learner who cannot name the four jobs is helped by matching each to a familiar person before '
                 'classifying software.')],
    F1=sec('Name the AI job in real apps', JOBS, [
        Q('A bank text says, "We blocked a payment that looked like fraud." Which job did the AI most likely do?',
          'Recognizing the payment as likely fraud',
          ('Generating a new payment for the customer', 'no new payment was made'),
          ('Recommending a product to the customer', 'nothing was suggested'),
          ('Forecasting next year\'s interest rates', 'unrelated to the block'),
          'Classifying a payment as fraud is recognizing.'),
        Q('A delivery app says your order will arrive in 25 minutes. Which job is this?', 'Forecasting',
          ('Recognizing', 'it predicts rather than identifies'), ('Generating', 'a time estimate is a forecast'),
          ('Recommending', 'it suggests no items'), 'Predicting arrival time is forecasting.'),
        Q('A design app makes three new logo drafts from a description. Which job is this?', 'Generating',
          ('Recognizing', 'it creates new images'), ('Forecasting', 'it predicts no number'),
          ('Recommending', 'the logos are new, not existing items'), 'Creating new images is generating.'),
        Q('A shopping site shows "Customers also bought" items. What could go wrong that fits this job?',
          'It keeps suggesting more of the same, missing your real need',
          ('It miscounts the exact delivery time of your order', 'a forecasting problem'), ('It writes a false product description', 'a generating problem'),
          ('It mislabels your photo as a cat', 'a recognizing problem'),
          'Recommenders can narrow suggestions to more of the same.'),
        Q('A camera app labels a photo of a husky as "wolf." Which job made the mistake?', 'Recognizing',
          ('Generating', 'it did not create content'), ('Forecasting', 'it predicted no future value'),
          ('Recommending', 'it suggested nothing'), 'Putting the photo in the wrong category is a recognition error.'),
    ]),
    F2=sec('Use the job type to decide what to check', JOBS_F2, [
        Q('A voice app answers "Book a table for four" by booking a table for two. Speech was turned into text, then a '
          'booking was made. What should be checked first?',
          'Whether the speech was recognized correctly',
          ('Whether the restaurant forecast was wrong', 'no forecast was involved'),
          ('Whether the recommendations were too narrow', 'no recommendation was involved'),
          ('Whether the booking page used AI at all', 'the question is which step failed'),
          'In a chain, an early recognition error spreads to later steps.'),
        Q('A sales forecast built from three normal years badly misses a month when a new factory opened nearby. Why?',
          'Forecasts can miss sudden changes not in past data',
          ('Forecasts always ignore all past data', 'they rely on past data'),
          ('The forecast must have generated false text', 'forecasts predict numbers'),
          ('Recommenders made the forecast too narrow', 'no recommender was involved'),
          'A change never seen in the data can surprise a forecast.'),
        Q('A tool generated a confident product description listing a feature the product does not have. What kind of '
          'failure is this?',
          'A generator producing fluent but false content',
          ('A recognizer putting the product in a category', 'nothing was categorized'),
          ('A forecaster missing a sudden change', 'nothing was forecast'),
          ('A recommender narrowing suggestions', 'nothing was recommended'),
          'Generators can write fluent content that is false.'),
        Q('A music app plays only songs very similar to ones you already liked. What is the best fix to try?',
          'Look for settings or searches that widen the suggestions',
          ('Retrain its speech recognition to understand your voice', 'the issue is recommendations'), ('Check its weather forecast against a website', 'unrelated'),
          ('Ask it to generate brand-new songs instead', 'avoids the recommendation problem'),
          'Recommenders can narrow choices; widen them on purpose.'),
        Q('A photo tool identifies plants well in a garden but poorly for rare desert plants. What does this suggest?',
          'Recognizers struggle with unusual examples',
          ('Forecasts miss sudden changes in sales', 'nothing is forecast'),
          ('Generators invent fluent but false text', 'nothing is generated'),
          ('Recommenders repeat the same suggestions', 'nothing is recommended'),
          'Recognition errors increase on unusual input.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.05
GEN = ('Two broad uses of AI are easy to confuse. PREDICTIVE (or classifying) uses produce a LABEL or a NUMBER about '
       'the input: "spam or not spam," "92 percent likely to be a cat," "about 30 minutes." GENERATIVE uses produce NEW '
       'CONTENT: a paragraph, a picture, a song, a block of code. They fail differently. A prediction can be the wrong '
       'label or a number that is off. Generated content can look polished while containing false facts, invented '
       'details or material too close to someone else\'s work. Before using AI, ask: do I need a label or a number, or '
       'do I need new content?')
GEN_F2 = ('Many real tasks mix the two uses. A help desk might first PREDICT which category a question belongs to, then '
          'GENERATE a draft reply. A mistake in the first step can make the second step confidently wrong. Some tasks '
          'are better kept predictive even when a generator could do them: if you need a yes or no answer, a '
          'confidence score and an audit trail, a classifier is easier to test than free text. And when facts matter, '
          'generated content needs checking against a source, because polished wording is not evidence.')

S_BASICS05 = SET(
    'AI.BASICS.05',
    M=sec('Decide whether a task needs prediction or generation', GEN, [
        Q('A school wants each incoming email marked "absence," "question" or "other." Which kind of AI use is this?',
          'Predictive: it produces a label',
          ('Generative: it writes new emails', 'it labels emails; it does not write them'),
          ('Generative: it creates new categories each day', 'the categories are fixed labels'),
          ('Neither; labeling emails cannot use AI', 'labeling is a classic AI task'),
          'Assigning a category is a predictive (classifying) use.'),
        Q('A student asks a tool for a short story about a lost robot. Which kind of use is this?',
          'Generative: it produces new content',
          ('Predictive: it produces a label', 'a story is new content'),
          ('Predictive: it produces one number', 'a story is not a number'),
          ('Neither; stories cannot be produced by AI', 'generating stories is a common use'),
          'Writing a new story is generative.'),
        Q('Which output is typical of a predictive use?', '"87 percent likely to be fraud"',
          ('A new poem about the ocean', 'generative'), ('A drawing of a mountain at sunset', 'generative'),
          ('A paragraph of product description', 'generative'),
          'A probability or label is a prediction.'),
        Q('What is a typical failure of generated content?',
          'It looks polished but contains false or invented details',
          ('It gives a single wrong yes or no label', 'that is a predictive failure'), ('It returns a predicted number that is a bit too high', 'that is a predictive failure'),
          ('It refuses to produce any output at all', 'possible, but not the typical failure described'),
          'Generators can sound polished while being wrong.'),
        Q('A clinic wants to estimate how many patients will arrive tomorrow. Which kind of use fits?',
          'Predictive: a number',
          ('Generative: a written story', 'they need a number'),
          ('Generative: a new image', 'they need a number'),
          ('Generative: a song about patients', 'they need a number'),
          'An estimated count is a predictive output.'),
    ]),
    B=[sk('Tell a label or number from new content',
          'A useful skill is looking at an OUTPUT and asking what kind it is. A LABEL names a category: "spam," "cat," '
          '"approved." A NUMBER measures or predicts something: "42 minutes," "12 percent chance." NEW CONTENT is '
          'something made that did not exist before: an essay, a photo, a melody, a joke. Some outputs combine kinds: '
          '"Spam (95 percent sure)" is a label plus a number, but it is still not new content. If the output could be '
          'checked by asking "which category?" or "how much?", it is a label or a number.', [
              Q('Which output is a label?', '"Approved"',
                ('A three-paragraph essay', 'new content'), ('A photo of a sunset', 'new content'),
                ('A new song melody', 'new content'), '"Approved" names a category.'),
              Q('Which output is a number?',
          '"12 percent chance of rain"',
          ('"A poem about rain"', 'new content'), ('"Spam"', 'a label'),
          ('"A new drawing of clouds"', 'new content'),
          'A percentage measures a chance.'),
              Q('Which output is new content?',
          'A newly written joke',
          ('"Cat (label)"', 'a label'), ('"About 42 minutes"', 'a number'),
          ('"Not spam"', 'a label'),
          'A newly written joke did not exist before.'),
              Q('"Spam (95 percent sure)" is which kind of output?',
          'A label plus a number',
          ('New content only, like an essay', 'nothing new was written'), ('A number only', 'it also has a label'),
          ('An essay', 'it is a short label and score'),
          'It combines a category and a confidence number.'),
              Q('Which question checks a label?', '"Which category is it?"',
                ('"How long is the story?"', 'about content length'), ('"Is the drawing pretty?"', 'about content'),
                ('"Does the song rhyme?"', 'about content'),
                'A label answers "which category?"'),
          ], why='A learner who misses MAIN may not recognize what kind of output a task needs; practicing on outputs '
                 'alone builds that skill first.')],
    F1=sec('Choose the right kind of AI use for a task', GEN, [
        Q('A store wants to know which product reviews are positive or negative. Which use fits best?',
          'Predictive: label each review as positive or negative',
          ('Generative: write new reviews for each product', 'they want to sort existing reviews'),
          ('Generative: create images of happy customers', 'unrelated to sorting reviews'),
          ('Generative: write a poem about the reviews', 'they need labels'),
          'Sorting reviews by sentiment is a labeling task.'),
        Q('A teacher wants five new practice questions about fractions. Which use fits best?',
          'Generative: create new questions',
          ('Predictive: label existing questions by topic', 'they need new questions'),
          ('Predictive: forecast next week\'s test scores', 'not what was asked'),
          ('Predictive: score one answer as right or wrong', 'not what was asked'),
          'Creating new questions is generative.'),
        Q('A tool generated five practice questions. What should the teacher check before using them?',
          'That each question and answer is actually correct',
          ('That a label was predicted for each question', 'the risk is false content'),
          ('That the questions are as long as possible', 'length is not correctness'),
          ('Nothing, because generated text is checked already', 'generated content can be wrong'),
          'Generated content can look polished but contain errors.'),
        Q('A city wants an estimate of how many buses are needed at 8 a.m. Which use fits best?',
          'Predictive: estimate a number',
          ('Generative: draw a picture of a bus', 'they need a number'),
          ('Generative: write a story about commuters', 'they need a number'),
          ('Generative: compose a bus jingle', 'they need a number'),
          'An estimated count is predictive.'),
        Q('A volunteer group wants a friendly thank-you letter for donors. Which use fits best?',
          'Generative: draft a new letter',
          ('Predictive: label each donor by city', 'they need a letter'),
          ('Predictive: estimate next year\'s donations', 'they need a letter'),
          ('Predictive: mark the letter "approved"', 'nothing exists to approve yet'),
          'Drafting a letter is generative; a person should still review it.'),
    ]),
    F2=sec('Handle tasks that mix prediction and generation', GEN_F2, [
        Q('A help desk tool labels a billing question as "shipping," then drafts a confident reply about delivery '
          'times. What went wrong?',
          'The wrong label led to a confidently wrong draft',
          ('The draft was right; billing and shipping are the same', 'they are different topics'),
          ('Generators can never write help desk replies', 'they can, with checking'),
          ('The label was right, but the draft was too short', 'the label was wrong'),
          'An early prediction error spread into the generated reply.'),
        Q('A company needs a yes or no decision on each expense claim, with a score and a record it can audit. Which '
          'approach is easier to test?',
          'A classifier that outputs a label and a score',
          ('A generator that writes a paragraph about each claim', 'free text is harder to test'),
          ('A generator that writes a poem about expenses', 'unrelated'),
          ('A generator asked to "decide fairly" in prose', 'harder to test and audit'),
          'A predictive output fits a yes or no decision with an audit trail.'),
        Q('A generated travel guide says a museum is free on Mondays. What should you do?',
          "Check the museum's official site before you rely on it",
          ('Trust it because the writing is polished and clear', 'polish is not evidence'), ('Ask the same tool to repeat the claim', 'repetition is not a check'),
          ('Assume all museums are free on Mondays', 'unsupported'),
          'Facts in generated content need a source check.'),
        Q('A school wants AI to sort essays by topic and then write feedback. Which step should be checked first if the feedback seems off-topic?',
          "The sorting step that labeled each essay's topic",
          ('The paper the essays were printed on', 'irrelevant'), ('The length of each feedback paragraph', 'length is not the likely cause'),
          ('Whether essays should ever get written feedback', 'avoids the problem'),
          'A wrong label early in the chain can make later output off-topic.'),
        Q('A manager asks a generator, "Is this invoice fraudulent?" and gets a long, confident paragraph. What is the main concern?',
          'Confident prose is not evidence the judgment is right',
          ('The long paragraph proves that the invoice is fraud', 'wording proves nothing'), ('Generators always refuse fraud questions', 'not true'),
          ('Long answers are always more accurate', 'length is not accuracy'),
          'A decision needs evidence and testing, not just polished wording.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.06
MOD = ('A MODEL is the trained part of an AI system: the learned patterns that turn input into output. A PRODUCT (an '
       'app, website or feature) wraps a model with other parts: a screen to type in, instructions the company adds, '
       'safety filters, tools such as web search, saved settings, and usage limits. The same model can sit inside '
       'several products that behave differently, and one product can switch models over time. So "this chatbot did '
       'X" does not mean every chatbot does X, and a product\'s feature, like saving files or browsing the web, may '
       'come from the product, not from the model itself.')
MOD_F2 = ('Because products change, details you learned about one can go out of date: a company may update its model, '
          'add or remove tools, or change limits without the name changing much. Different products may also use '
          'different kinds of models: a chatbot, a photo tagger and a translation feature are not interchangeable. '
          'When a result matters, check what the specific product says about itself today, such as its help pages, '
          'settings and release notes, rather than assuming from a friend\'s experience with a different product or '
          'from an old article.')

S_BASICS06 = SET(
    'AI.BASICS.06',
    M=sec('Tell a model from the product built around it', MOD, [
        Q('What is a model in an AI system?',
          'The trained part that turns input into output',
          ('The app\'s screen and buttons you tap', 'that is part of the product'),
          ('The company that sells the subscription', 'a company is not a model'),
          ('The list of usage limits on an account', 'limits are set by the product'),
          'The model is the learned core; the product wraps it.'),
        Q('Two apps use the same model but behave differently. What is the most likely reason?',
          'Each product adds its own instructions, tools and limits',
          ('The model must be broken in one of the apps', 'differences usually come from the products'),
          ('Models change randomly each time you open an app', 'not the usual reason'),
          ('Products cannot share a model, so this cannot happen', 'they can share models'),
          'Products wrap the same model in different ways.'),
        Q('A chatbot app can search the web. Where does that ability most likely come from?',
          'A search tool the product connects to the model',
          ('The model memorizing the entire internet', 'a model is not a live copy of the web'),
          ('Every model\'s built-in ability to browse', 'browsing is a product tool'),
          ('The user\'s own computer searching by itself', 'the product provides the tool'),
          'Tools like web search are added by the product.'),
        Q('Your friend says, "Chatbots always remember everything you tell them." What is the best response?',
          'It depends on the product; features differ',
          ('That is true of every chatbot ever made', 'products differ'),
          ('No chatbot can store anything at all', 'some products save information'),
          ('Only paid chatbots have models inside', 'all chatbots use some model'),
          'Memory is a product feature that varies.'),
        Q('Which is part of the product rather than the model?',
          'A daily limit on how many messages you can send',
          ('The learned patterns that produce replies', 'that is the model'),
          ('The numbers set during training', 'those belong to the model'),
          ('The patterns learned from example text', 'that is the model'),
          'Usage limits are set by the product.'),
    ]),
    B=[cs('Compare an engine with the car around it',
          'Think of a car ENGINE and the CAR built around it. The engine makes the power, but the car adds the steering '
          'wheel, seats, brakes, radio and speed limiter. The same engine can go into a sports car and a delivery van, '
          'and they will drive very differently. An AI MODEL is like the engine: it produces the output. The PRODUCT is '
          'like the car: it adds the screen, rules, tools and limits. If a van is slow, the reason might be its '
          'limiter, not its engine.', [
              Q('In the comparison, what is the AI model like?', 'The engine',
                ('The steering wheel', 'part of the product'), ('The radio', 'part of the product'),
                ('The seats', 'part of the product'), 'The model produces the output, like an engine.'),
              Q('What is the product like?',
          'The car around the engine',
          ('Only the engine by itself', 'that is the model'), ('Only the fuel', 'not in the comparison'),
          ('Only the road', 'not in the comparison'),
          'The product adds everything around the model.'),
              Q('Why can two cars with the same engine drive differently?',
          'Their other parts and settings differ',
          ('Engines change their shape every single day', 'not the reason'), ('One engine must be broken', 'not the usual reason'),
          ('Cars cannot share engines', 'they can'),
          'Same engine, different car.'),
              Q('A van is slow because of a speed limiter. In AI terms, the slowness comes from what?', 'The product',
                ('The model', 'the engine is not the cause here'), ('The training data', 'not the cause here'),
                ('The user', 'not the cause here'), 'A limit set by the product, not the model.'),
              Q('Which is like a product feature added around the model?', 'A safety filter',
                ('The learned patterns', 'model'), ('The trained numbers', 'model'),
                ('The model\'s output', 'produced by the model'), 'Filters are added by the product.'),
          ], why='A learner who blends "model" and "product" can separate them using a familiar engine-and-car '
                 'picture.')],
    F1=sec('Apply the model and product distinction', MOD, [
        Q('A school\'s writing app refuses to write full essays, while another app using the same model will. What '
          'explains this?',
          'The school\'s product added its own rules',
          ('The model in the school app is too weak', 'the model is the same'),
          ('The other app has a different kind of model', 'the model is the same'),
          ('Essay writing is impossible for any model', 'the other app does it'),
          'Products can add rules on top of the same model.'),
        Q('A coworker says, "The model can read our team calendar." What is more accurate?',
          'The product may connect a calendar tool to the model',
          ('Every model can read every calendar automatically', 'access comes from product tools'),
          ('Models learn calendars during training', 'your calendar was not in training'),
          ('Calendars are part of every model\'s patterns', 'they are not'),
          'Access to tools like calendars comes from the product.'),
        Q('Ana read an article about one chatbot\'s limits. What should she remember about a different chatbot?',
          'Its limits may differ, so check that product',
          ('Its limits must match the article exactly', 'products differ'),
          ('It has no limits since it is a different brand', 'unsupported'),
          ('It uses no model if it is different', 'every chatbot uses a model'),
          'Product details do not transfer automatically.'),
        Q('A product updates to a new model but keeps its name. What could change for users?',
          'Its answers and abilities could change',
          ('Nothing, because the name stayed the same', 'the model changed'),
          ('Only the colors of the app', 'the model affects output'),
          ('Only the price, never the answers', 'answers can change too'),
          'Swapping the model can change behavior under the same name.'),
        Q('Which statement about chatbots is accurate?',
          'Different chatbots can answer one question differently',
          ('All chatbots give the same answer to any question', 'products and models differ'), ('A chatbot is a model with no product around it', 'chatbots are products'),
          ('Every chatbot can browse the web and save files', 'tools vary by product'),
          'Products and models vary, so behavior varies.'),
    ]),
    F2=sec('Check current product details instead of assuming', MOD_F2, [
        Q('A blog post from two years ago says a product cannot read PDF files. You need to know today. What should '
          'you check?',
          'The product\'s current help pages or release notes',
          ('The same two-year-old blog post again', 'it may be outdated'),
          ('A friend\'s experience with another product', 'a different product'),
          ('Nothing; products never change their features', 'they do change'),
          'Check current, product-specific information.'),
        Q('A photo tagger and a chatbot are both called "AI." Can you use the photo tagger to draft a letter?',
          'No; they are different products for different tasks',
          ('Yes; all AI products can do every task', 'tools are not interchangeable'), ('Yes; if both use AI, they must share one model', 'they may use different models'),
          ('No; letters can never be drafted with AI', 'chatbots can draft letters'),
          'Different products serve different tasks.'),
        Q('Your settings page says "Chat history saving: off," but a friend says the product always saves chats. What is the best next step?',
          'Read what the product says the setting does and rely on that',
          ('Assume your friend is right and ignore the setting entirely', 'hearsay is weaker evidence'), ('Assume no product ever saves anything', 'some do'),
          ('Delete your account without checking anything', 'check first'),
          'Product documentation for your own settings is the best evidence.'),
        Q('A product changed its limits last month. Your guide from last year says "unlimited messages." What should '
          'you conclude?',
          'The guide may be out of date; check the current terms',
          ('The guide must be right because it was published', 'products change'),
          ('All guides are always wrong about limits', 'too broad'),
          ('Limits are set by the model, so they never change', 'limits are set by the product'),
          'Current product information beats old guides.'),
        Q('A company says its product "uses the latest model." Why might that be hard to rely on later?',
          'The product may switch models over time',
          ('Models never change once released', 'they are updated'),
          ('Products cannot contain models', 'they do'),
          ('"Latest" is a guarantee of accuracy', 'it is not'),
          'A model can be swapped behind the same product name.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.BASICS.07
HUM = ('People often compare AI with humans: "it reads," "it thinks," "it is like a student." Comparisons can help '
       'explain a new idea, but they can also mislead. A system may beat experts at one narrow task, such as spotting a '
       'pattern in thousands of images, yet fail at something a child finds easy, like counting objects in an unusual '
       'picture. Its abilities can be UNEVEN in ways a human\'s are not, so success on one task does not predict '
       'success on a nearby task. Treat a human comparison as a starting point, then check how the system actually '
       'performs on the task you care about.')
HUM_F2 = ('Human comparisons shape trust. If a system "sounds like a person," people may assume it has human '
          'judgment, feelings or common sense. Some language models are trained to sound helpful and friendly, which '
          'can make errors easier to miss. On the other hand, dismissing a system as "just a machine" can hide real '
          'abilities and real risks. A better habit is to describe what was observed: "It summarized these ten '
          'reports accurately but invented one date," rather than "It is smart" or "It is dumb." Specific '
          'observations can be checked.')

S_BASICS07 = SET(
    'AI.BASICS.07',
    M=sec('Use human comparisons carefully', HUM, [
        Q('A system scores better than doctors at spotting one type of spot on X-rays. Which conclusion is justified?',
          'It did well on that narrow task; other tasks need checks',
          ('It can now replace doctors for all medical decisions', 'one task does not predict others'), ('It must understand medicine as well as a doctor', 'performance is not understanding'),
          ('It will also be excellent at reading patient notes', 'nearby tasks can differ'),
          'Narrow success does not transfer automatically.'),
        Q('Why can AI abilities be called "uneven"?',
          'It may do a hard task well but fail an easy one',
          ('It always performs the same on every task', 'that is even, not uneven'),
          ('It improves evenly like a growing child', 'abilities do not grow evenly'),
          ('It only fails at tasks that are very hard', 'it can fail easy tasks'),
          'Abilities can be strong and weak in surprising combinations.'),
        Q('A teacher says, "The AI is like a student learning to write." What is the best way to use this comparison?',
          'As a starting point, then check how it actually performs',
          ('As proof that the AI learns exactly like a student', 'comparisons are not proof'), ('As a reason to give it grades like a student', 'misreads the comparison'),
          ('As a reason never to check its writing', 'checking is still needed'),
          'Comparisons help explain but must be checked.'),
        Q('A system writes fluent essays but miscounts the apples in a simple picture. What does this show?',
          'Skill at one task does not predict skill at another',
          ('The essays must also be full of counting errors', 'not necessarily'),
          ('It is pretending to be bad at counting on purpose', 'no evidence of pretending'),
          ('Counting is always harder than writing for computers', 'unsupported generalization'),
          'Uneven abilities are common.'),
        Q('Which statement is a careful description rather than a misleading comparison?',
          '"It recognized 95 of 100 test images correctly."',
          ('"It sees the world in just the way we do."', 'a misleading comparison'), ('"It thinks like a genius."', 'vague and unsupported'),
          ('"It is as smart as a ten-year-old."', 'a misleading overall comparison'),
          'A measured result on a task can be checked.'),
    ]),
    B=[cs('Compare uneven skill to a calculator and a toddler',
          'A pocket calculator multiplies huge numbers instantly, faster than any person, yet it cannot tell a cat from '
          'a dog. A toddler easily tells a cat from a dog but cannot multiply 27 by 43. Neither is "smarter" overall; '
          'they have different abilities. AI systems are similar: a system can be impressive at one thing and weak at '
          'another, in a pattern unlike any human\'s. So ask "How good is it at THIS task?" rather than "How smart is '
          'it?"', [
              Q('What can the calculator do better than a person?',
          'Multiply huge numbers quickly',
          ('Tell a cat from a dog at a glance', 'it cannot'), ('Learn a language', 'not described'),
          ('Explain a joke', 'not described'),
          'Calculators excel at arithmetic.'),
              Q('What can the toddler do that the calculator cannot?',
          'Tell a cat from a dog',
          ('Multiply 27 by 43 in its head', 'the toddler cannot'), ('Add huge numbers', 'the calculator does that'),
          ('Run on batteries', 'not the point'),
          'The toddler recognizes animals.'),
              Q('Which question does the passage recommend?', '"How good is it at this task?"',
                ('"How smart is it overall?"', 'too vague'), ('"Is it smarter than a toddler?"', 'misleading'),
                ('"Does it think like us?"', 'not checkable'), 'Ask about a specific task.'),
              Q('Who is "smarter" overall: the calculator or the toddler?', 'Neither; they have different abilities',
                ('The calculator, since it is faster', 'speed at one task is not overall smartness'),
                ('The toddler, since it is human', 'not the point'), ('Both are equally smart at everything', 'not true'),
                'Abilities differ; one score misleads.'),
              Q('What does the example suggest about AI?',
          'It can be strong at one thing and weak at another',
          ('It is equally good at all tasks', 'abilities are uneven'), ('It is always weaker than a toddler', 'not true'),
          ('It is always stronger than a calculator at math', 'not true'),
          'Uneven abilities apply to AI too.'),
          ], why='A learner who ranks AI on one "smartness" scale benefits from a familiar case of uneven abilities.')],
    F1=sec('Judge AI ability task by task', HUM, [
        Q('A tool translated a menu well. You now want it to translate a medical form. What should you do?',
          'Check its performance on the medical form separately',
          ('Trust it fully since the menu was perfect', 'one task does not predict another'), ('Refuse because translation is impossible', 'it can translate'),
          ('Assume medical words are easier to translate than menus', 'unsupported'),
          'Check each task that matters.'),
        Q('Jordan says, "This chatbot is basically a person in a box." What is the most accurate reply?',
          "It can sound human, but its abilities differ from a person's",
          ('Yes, it has the same judgment and common sense as a person', 'unsupported'), ('No, it can never do anything useful', 'dismissive and inaccurate'),
          ('Yes, because it uses words like a person', 'sounding human is not being human'),
          'Avoid both over- and under-estimating.'),
        Q('A study tool explains algebra steps clearly but gets one multiplication wrong. What is the best habit?',
          'Use the explanation but check each calculation',
          ('Stop using it for anything at all', 'too extreme'),
          ('Trust every step because the explanation is clear', 'clarity is not correctness'),
          ('Assume all its explanations are wrong', 'too broad'),
          'Uneven ability means checking specific parts.'),
        Q('Which report about an AI tool is most useful to a manager?',
          '"It sorted 180 of 200 invoices; handwritten ones failed."',
          ('"It is really smart, just like a new hire we trained."', 'vague comparison'), ('"It is dumb and will never work."', 'vague and dismissive'),
          ('"It thinks just like our accountant."', 'misleading comparison'),
          'A specific measured observation helps decisions.'),
        Q('An image tool wins an art contest. A friend says it can surely design a safe bridge. What is wrong?',
          'Success in one task does not show skill in a different one',
          ('Art and bridge design are the same task', 'they differ greatly'), ('Nothing; winning a contest proves its general skill', 'it does not'),
          ('Image tools cannot win art contests', 'irrelevant to the reasoning'),
          'Abilities do not transfer automatically.'),
    ]),
    F2=sec('Describe what was observed instead of "smart" or "dumb"', HUM_F2, [
        Q('A chatbot answers warmly, "I totally understand how you feel." What should you keep in mind?',
          'Friendly wording does not show feelings or judgment',
          ('It must truly share your feelings', 'unsupported by the wording'), ('Friendly replies are always more accurate than others', 'tone is not accuracy'),
          ('It is lying, so nothing it says is useful', 'too extreme'),
          'Sounding human can raise trust without evidence.'),
        Q('Which statement is a checkable observation?',
          '"It summarized ten reports but invented one date."',
          ('"It is basically genius-level smart."', 'not checkable'), ('"It is just a dumb machine."', 'not checkable'),
          ('"It understands us better than other people do."', 'not checkable'),
          'Specific observations can be verified.'),
        Q('A coworker dismisses a tool as "just a machine" and ignores that it can write convincing fake emails. What is the risk?',
          'Underestimating real abilities can hide real risks',
          ('None, since machines cannot write convincing emails', 'it can'), ('The tool will stop working if ignored', 'not how tools work'),
          ('Calling it a machine makes it safer', 'labels do not change risk'),
          'Dismissing a system can be as misleading as overpraising it.'),
        Q('Why might a friendly, human-sounding style make errors easier to miss?',
          'People tend to trust things that sound like a helper',
          ('Friendly text contains no errors by design', 'not true'), ('Errors are always marked in red', 'not true'),
          ('Human-sounding systems cannot make real mistakes', 'they can'),
          'Tone affects trust without changing accuracy.'),
        Q('A review says, "The AI is honest and caring." What would make the review more useful?',
          'Describe specific tasks it did well or badly',
          ('Use stronger words like "loving" and "wise"', 'still not checkable'),
          ('Compare it to a famous person', 'still a vague comparison'),
          ('Say it is "better than a human"', 'unsupported overall claim'),
          'Specific observations can be checked; personality labels cannot.'),
    ]),
)

SETS = [S_BASICS01, S_BASICS02, S_BASICS03, S_BASICS04, S_BASICS05, S_BASICS06, S_BASICS07]
