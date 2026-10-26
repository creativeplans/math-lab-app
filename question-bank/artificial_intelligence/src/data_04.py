"""Foundation 4: Asking for what you need (AI.PROMPT.01-09)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.PROMPT.01
TCAP = ('A useful request (often called a PROMPT) usually covers four things. The TASK: what you want done ("write," '
        '"compare," "list," "explain"). The CONTEXT: background the tool cannot know, such as your situation, the '
        'facts involved or what you already tried. The AUDIENCE: who will read or use the result, such as a '
        'ten-year-old, a manager or yourself. The PURPOSE: why you need it, such as to persuade, to decide or to study. '
        'A vague request like "write about recycling" leaves the tool to guess all four, so the result may be '
        'generic. Adding the missing pieces gives it a fair chance.')
TCAP_F2 = (('Sometimes a request seems complete but the pieces pull against each other, or one key detail is assumed '
           'rather than stated. "Write exactly 200 words, and keep the whole answer under 100 words" asks for two '
           'lengths that cannot both be true. "Fix the schedule" assumes the tool knows which schedule and what is wrong'
           ' with it. Before sending an important request, reread it as a stranger would: could someone with no '
           'background do exactly what you want? If not, add or fix the missing piece first.'))

S_PROMPT01 = SET(
    'AI.PROMPT.01',
    M=sec('Identify the task, context, audience and purpose a request needs', TCAP, [
        Q('In "Explain (the action word) photosynthesis (the process) to a group of eight-year-olds," which part names the audience?',
          'a group of eight-year-olds',
          ('Explain (the action word)', 'that is the task'), ('photosynthesis (the process)', 'that is the topic'),
          ('to', 'only a connecting word'),
          'The audience is who will read or use it.'),
        Q('"Write about recycling." Which pieces are missing?',
          'Context, audience and purpose',
          ('Only the task, which is not stated at all', 'the task "write" is stated'),
          ('Nothing is missing; the request is complete', 'three pieces are missing'),
          ('Only the topic of the writing', 'the topic is recycling'),
          'The task is there; context, audience and purpose are not.'),
        Q('Which detail is CONTEXT the tool could not know on its own?',
          '"Our school recycles paper, not plastic."',
          ('"Make it sound friendly and clear."', 'a style instruction'), ('"Use short sentences in the reply."', 'a format instruction'),
          ('"Please answer in English."', 'a language instruction'),
          'Facts about your situation are context.'),
        Q('Which phrase states a PURPOSE?',
          '"so the class votes for a compost bin"',
          ('"for the class newsletter next week"', 'that is where it appears'), ('"about 200 words long"', 'that is a length limit'),
          ('"write a short article"', 'that is the task'),
          'Purpose says why the result is needed.'),
        Q('Why does a vague request often get a generic answer?',
          'The tool has to guess the missing pieces',
          ('Tools refuse to answer short requests', 'they answer, generically'),
          ('Vague requests are always rejected by filters', 'not true'),
          ('Short requests use too many tokens', 'the opposite'),
          'Missing details lead to guesses.'),
    ]),
    B=[cs('Separate a request from the background it needs',
          'Imagine asking a new babysitter to "make dinner." That is a REQUEST, but the babysitter does not know the '
          'BACKGROUND: one child is allergic to nuts, dinner is at 6, and the kids love pasta. Without that '
          'background, the babysitter might make something unsafe or unwanted. An AI tool is similar. The request '
          'says what to do; the background, or context, says what the tool cannot see for itself. Good results need '
          'both, but a request alone often feels complete to the person asking, because they already know the '
          'background.', [
              Q('In "make dinner," what is missing?',
          'The background, such as allergies',
          ('The request itself', '"make dinner" is the request'), ("The babysitter's full name and age", 'not needed'),
          ('The house address', 'they are already there'),
          'The background is missing.'),
              Q('"One child is allergic to nuts" is which part?',
          'Background (context)',
          ('The request', 'it does not say what to do'), ('A greeting', 'not a greeting'),
          ('The audience for dinner', 'not who reads it'),
          'It is information the babysitter cannot see.'),
              Q('Why might the request feel complete to the parent?',
          'The parent already knows the background',
          ('Babysitters can read minds', 'they cannot'), ('Requests never need details', 'they often do'),
          ('The kids will explain everything to the babysitter', 'not reliable'),
          'Known background is easy to forget to say.'),
              Q('What could happen without the background?', 'An unsafe or unwanted dinner',
                ('A perfect dinner every time', 'unlikely without key facts'), ('No dinner at all, ever', 'too extreme'),
                ('The kids cooking instead', 'not described'), 'Missing context leads to bad guesses.'),
              Q('In an AI request, what does context provide?',
          'Facts the tool cannot see for itself',
          ("The tool's training data", 'not context'), ("The tool's price", 'not context'),
          ("A list of the tool's display settings", 'not context'),
          'Context fills in your situation.'),
          ], why='A learner who misses MAIN often confuses the request with the background it needs; an everyday '
                 'babysitter example separates them.')],
    F1=sec('Choose an improved request for a stated need', TCAP, [
        Q('Pat needs a short email asking her landlord to fix a leaking sink before Friday. Which request is best?',
          '"Draft a polite email asking my landlord to fix the sink by Friday."',
          ('"Write an email to my landlord about things in my apartment."', 'no task details, audience or purpose'), ('"Explain how sinks leak and how plumbers fix them."', 'not her task'),
          ('"Write something about landlords in general."', 'too vague'),
          'It states task, audience and purpose.'),
        Q('A student wants a study guide for a biology test on cells. What is the most useful detail to add to "Make a study guide"?',
          'The topic, the course level and the test format',
          ("The color of the student's notebook", 'irrelevant'), ('A request to make the guide sound impressive', 'does not help it fit'),
          ("The name of the student's best friend", 'irrelevant'),
          'Topic, level and format are key context.'),
        Q('Which request names a clear audience?',
          '"Explain credit scores for a high-school senior."',
          ('"Explain credit scores in some detail for me."', 'audience is vague'),
          ('"Explain credit scores very well, please."', 'no audience'),
          ('"Explain credit scores, and make it good."', 'no audience'),
          'A specific reader shapes the explanation.'),
        Q('Marco asks, "Give me ideas." What should he add first?',
          'What the ideas are for and any limits',
          ('A request for the ideas to be numbered in bold', 'formatting before purpose'),
          ('The word "please" at the start of the sentence', 'politeness is not context'),
          ('Nothing; short requests always work best', 'too vague to help'),
          'Purpose and limits make ideas useful.'),
        Q('Which request includes context the tool could not guess?',
          '"Plan meals for a week; we have no oven, only a stove."',
          ('"Plan meals for a week that taste really good."', 'no situational context'),
          ('"Plan a week of meals, please and thank you."', 'no situational context'),
          ('"Plan a week of meals as fast as you can."', 'no situational context'),
          'Having no oven is key context.'),
    ]),
    F2=sec('Find the missing or conflicting piece before sending', TCAP_F2, [
        Q('"Write exactly 200 words, and keep the whole answer under 100 words." What is the problem?',
          'The two length rules cannot both be met',
          ('It does not say what the topic is', 'a missing topic is not the main problem here'), ('200 words is too long for any reader', 'length alone is not the problem'),
          ('It does not say "please"', 'politeness is not the problem'),
          'No answer can be exactly 200 words and also under 100 words; ask which rule matters.'),
        Q('"Fix the schedule." What does this request assume?',
          'That the tool knows which schedule and what is wrong',
          ('That the tool can see every calendar in the world', 'too extreme a reading'),
          ('That schedules never need fixing at all', 'not implied'),
          ('That the user wants a poem', 'not implied'),
          'Key details are assumed, not stated.'),
        Q('What is a good test before sending an important request?',
          'Reread it as a stranger with no background would',
          ('Count the words and make sure it is very short', 'length is not the test'),
          ('Add the word "urgent" to the start', 'urgency is not clarity'),
          ('Send it and hope for the best', 'skips the check'),
          'Strangers reveal missing pieces.'),
        Q('"Summarize the report for the board so they can decide on the budget." Which piece is still missing?',
          'Which report (it must be supplied)',
          ('The audience, which is not mentioned anywhere', 'the board is the audience'),
          ('The purpose, which is not mentioned anywhere', 'deciding the budget is the purpose'),
          ('The task, which is not mentioned anywhere', 'summarize is the task'),
          'The report itself is missing context.'),
        Q('A request asks for "a fun, serious speech." What should the writer do first?',
          'Decide which tone matters more, or how to balance them',
          ('Send it as written; tools resolve conflicts well', 'conflicts lead to muddled results'),
          ('Remove the word "speech" from the request', 'removes the task'),
          ('Ask for ten speeches at once', 'does not resolve the conflict'),
          'Resolve conflicting requirements first.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.02
FMT = ('Besides saying what you want, say what the result should LOOK LIKE. The OUTPUT FORMAT is its shape: a bulleted '
       'list, a table with named columns, a three-paragraph letter, a numbered set of steps. CONSTRAINTS are limits it '
       'must respect: a length ("under 150 words"), a tone ("friendly but professional"), a reading level ("for '
       'beginners"), or things to avoid ("no jargon," "do not mention prices"). Stating format and constraints up '
       'front saves rounds of revision and makes the result easy to check: you can see at once whether it has five '
       'bullets or is under 150 words.')
FMT_F2 = ('Format and constraints work best when they are specific and checkable. "Keep it short" is vague; "under 100 '
          'words" can be checked. "Make it look nice" is vague; "a table with columns Name, Date and Cost" can be '
          'checked. Tools do not always follow every constraint, especially exact word counts or many rules at once, '
          'so check the result against each one. If a constraint really matters, such as a character limit for a '
          'form, verify it yourself rather than trusting the tool\'s claim that it complied.')

FMT_EX = PR('List three tips for saving money on groceries. Use a numbered list. Keep each tip under 15 words.',
            '1. Plan your meals for the week before you go shopping.\n2. Compare unit prices instead of package prices '
            'on the shelf.\n3. Buy store brands, which are often cheaper than name brands, especially for basic '
            'items like flour, sugar, rice and canned vegetables.')

S_PROMPT02 = SET(
    'AI.PROMPT.02',
    M=sec('State the output format and constraints a result must meet', FMT, [
        Q('Which part of a request describes the OUTPUT FORMAT?',
          '"as a table with Item and Price columns"',
          ('"for my coworkers"', 'that is the audience'), ('"so we can choose a caterer by Friday"', 'that is the purpose'),
          ('"compare three caterers"', 'that is the task'),
          'Format is the shape of the result.'),
        Q('Which is a CONSTRAINT?', '"under 150 words"',
          ('"write a cover letter"', 'that is the task'), ('"for a hiring manager"', 'that is the audience'),
          ('"to apply for a job"', 'that is the purpose'),
          'A length limit is a constraint.'),
        Q('In this fictional example, which instruction did the response NOT follow?',
          'Keeping each tip under 15 words',
          ('Using a numbered list', 'it used one'), ('Giving three tips', 'it gave three'),
          ('Keeping the topic on groceries', 'it did'),
          'Tip 3 is far longer than 15 words.',
          ex=FMT_EX),
        Q('Why does stating format up front help?', 'It saves revisions and makes checking easy',
          ('It guarantees the facts are correct', 'format does not check facts'),
          ('It makes the tool respond more slowly', 'not a benefit'),
          ('It lets you skip reading the result', 'you still need to read it'),
          'A clear shape is quick to verify.'),
        Q('Which instruction is something to AVOID, a kind of constraint?', '"Do not mention prices."',
          ('"Write it for parents."', 'audience'), ('"Make a checklist."', 'format'),
          ('"Explain the field trip."', 'task'),
          'An "avoid" rule is a constraint.'),
    ]),
    B=[sk('Turn a vague wish into a checkable instruction',
          'A CHECKABLE instruction is one you can test by looking at the result. "Short" is vague: short to whom? '
          '"Under 100 words" is checkable: count and see. "Nice looking" is vague; "a table with three columns" is '
          'checkable. "Friendly" is partly vague, but "no technical terms" is easier to test. To turn a wish into a '
          'checkable instruction, ask: "What would I look for to know it was done?" Then write that down as the '
          'instruction.', [
              Q('Which instruction is checkable?', '"Under 100 words"',
                ('"Short"', 'vague'), ('"Not too long"', 'vague'), ('"Brief-ish"', 'vague'),
                'You can count to check it.'),
              Q('Which is the most checkable version of "nice looking"?',
          '"A table with three columns"',
          ('"Pretty and neat"', 'vague'), ('"Very professional-looking"', 'vague'),
          ('"Stylish"', 'vague'),
          'Columns can be counted.'),
              Q('What question helps turn a wish into a checkable instruction?',
          '"How would I know it was done?"',
          ('"How do I sound polite?"', 'not about checking'), ('"Which tool is cheapest this month?"', 'not about checking'),
          ('"How fast can it answer?"', 'not about checking'),
          'Define what success looks like.'),
              Q('Which instruction is easier to test than "friendly"?', '"No technical terms"',
                ('"Warm"', 'vague'), ('"Kind and fun"', 'vague'), ('"Happy-sounding"', 'vague'),
                'You can scan for technical terms.'),
              Q('Which result meets "exactly five bullet points"?', 'A list with five bullets',
                ('A list with four bullets', 'one short'), ('A paragraph with no bullets', 'no bullets'),
                ('A list with seven bullets', 'two too many'), 'Five bullets meets the instruction.'),
          ], why='A learner who misses MAIN often writes vague limits; practicing checkable instructions is the '
                 'underlying skill.')],
    F1=sec('Write format and constraints for real requests', FMT, [
        Q('Lee needs a sign-up sheet for a car wash with columns for name, phone and time slot. Which instruction fits?',
          '"Make a table with columns Name, Phone and Time slot."',
          ('"Make something people can sign up on, please."', 'format not specified'),
          ('"Make it look really nice and clean."', 'vague'),
          ('"Write a story about a car wash."', 'wrong task'),
          'Named columns give a checkable format.'),
        Q('A form allows only 280 characters. Which constraint should Ana state?',
          '"Under 280 characters, including spaces."',
          ('"Keep it reasonably short and sweet."', 'not checkable'),
          ('"Use as many words as you need."', 'ignores the limit'),
          ('"Make it sound exciting."', 'a tone, not the limit'),
          'State the exact limit.'),
        Q('A coach wants practice drills a beginner can follow. Which constraint fits best?',
          '"Numbered steps, no jargon, for beginners."',
          ('"Make it as advanced as possible."', 'wrong level'),
          ('"Any format is fine, whatever you like."', 'misses the need'),
          ('"Mention every famous athlete you know."', 'irrelevant'),
          'Format, vocabulary and level match the need.'),
        Q('Which request would produce a result that is easiest to check?',
          '"List exactly five tips, each under 20 words."',
          ('"Give me some tips, not too many."', 'vague count'), ('"Some tips, please, as good as you can make them."', 'vague'),
          ('"Write a lot of helpful tips."', 'vague'),
          'Exact counts and limits are easy to verify.'),
        Q('A teacher wants a parent letter without mentioning grades. How should she say this?',
          '"Do not mention grades."',
          ('"Be careful about some topics."', 'too vague'),
          ('"Use good judgment on content."', 'too vague'),
          ('"Make it nice for parents."', 'does not state the rule'),
          'A clear "avoid" rule is easy to follow and check.'),
    ]),
    F2=sec('Check whether constraints were actually followed', FMT_F2, [
        Q('A response says, "Here is your summary in under 100 words," but it looks long. What should you do?',
          'Count the words yourself',
          ('Trust the claim, since it said it complied', 'claims are not checks'),
          ('Ask it to repeat the claim', 'still not a check'),
          ('Assume all summaries are under 100 words', 'not true'),
          'Verify constraints that matter.'),
        Q('A request lists twelve formatting rules, and the result breaks two. What is a sensible next step?',
          'Point out the two broken rules and ask for a fix',
          ('Give up on using any formatting rules from now on', 'too extreme'), ('Add twelve more rules', 'more rules can make it worse'),
          ('Accept it without checking the rest', 'other rules may also fail'),
          'Name specific failures and recheck.'),
        Q('Which version of "keep it short" can be checked?',
          '"Three sentences or fewer"',
          ('"Short and snappy, please"', 'vague'), ('"Brief, as usual"', 'vague'),
          ('"Not wordy"', 'vague'),
          'A sentence count can be checked.'),
        Q('A grant form requires exactly 500 characters or fewer. The tool says its text is 480 characters. What is the '
          'safest action?',
          'Check the character count before submitting',
          ('Submit it, since the tool stated the count', 'tools can miscount'),
          ('Make it longer to be safe', 'risks breaking the limit'),
          ('Ask the tool if it is sure', 'not a real check'),
          'Verify exact limits yourself.'),
        Q('Why might a tool miss an exact word count even when asked clearly?',
          'Exact counts are hard for it to track precisely',
          ('Tools are designed to ignore every limit on purpose', 'not true'),
          ('Word counts are illegal to request', 'nonsense'),
          ('Exact counts only work in other languages', 'not true'),
          'Precise counting is a known weak spot; check it.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.03
EXM = ('Sometimes the fastest way to explain what you want is to SHOW it. Adding one or two short EXAMPLES of the '
       'desired output, such as a sample product description or a sample quiz question, helps the tool copy the '
       'style, length and structure. But examples are powerful: the tool may copy them too closely, repeating their '
       'topic, length or wording even when your written instructions say otherwise. Use examples that match what you '
       'want, label them clearly ("Example of the style I want:"), and say what should differ ("use new topics, not '
       'the example\'s topic").')
EXM_F2 = ('When written instructions and examples disagree, the example often wins. If your instructions say "write '
          'four-sentence descriptions" but your only example has two sentences, expect short results. If every '
          'example mentions the same product, the tool may keep mentioning it. Fix conflicts by changing the example '
          'to match the rules, giving two varied examples instead of one, or removing the example and describing the '
          'pattern in words. Then check that results follow the rules, not just the example.')

EXM_EX = PR('Write three quiz questions about planets in the style of this example.\nExample: "Which planet is known '
            'as the Red Planet? (Mars)"',
            '1. Which planet is known as the Red Planet? (Mars)\n2. Which planet is often called the Red Planet? '
            '(Mars)\n3. Which planet has a reddish color from iron oxide? (Mars)')

S_PROMPT03 = SET(
    'AI.PROMPT.03',
    M=sec('Use examples to show what you want, and notice when they pull too hard', EXM, [
        Q('Why include a short example of the desired output?',
          'It shows the style, length and structure to copy',
          ('It proves the facts in the answer are true', 'examples do not verify facts'),
          ('It makes the tool ignore all other instructions', 'not the goal'),
          ('It makes the reply arrive faster than usual', 'not the purpose'),
          'Examples demonstrate the pattern.'),
        Q('In this fictional example, what went wrong?',
          'Every question copied the example\'s topic, Mars',
          ('The questions were about the wrong subject entirely', 'they were about planets'),
          ('The questions did not use the example\'s format', 'they did'),
          ('There were too many questions', 'there were three'),
          'The tool copied the example too closely.', ex=EXM_EX),
        Q('What would most likely fix the problem in that example?',
          'Saying "use different planets than the example"',
          ('Removing the word "quiz" from the request', 'not the problem'),
          ('Asking for thirty questions instead of three', 'more copies likely'),
          ('Adding a second example that is also about Mars', 'reinforces the copying'),
          'Say what should differ from the example.', ex=EXM_EX),
        Q('How should an example be marked in a request?',
          'Clearly labeled, like "Example of my style:"',
          ('Hidden in the middle of the request with no label', 'may be confused with instructions'), ('Written in capital letters only', 'not a clear label'),
          ('Placed after the reply is finished', 'too late'),
          'Labels separate examples from instructions.'),
        Q('What is a risk of including examples?', 'The tool may copy them too closely',
          ('The tool will refuse to answer', 'not a typical risk'),
          ('The tool will always ignore them', 'often the opposite'),
          ('The answer will be in another language', 'not a typical risk'),
          'Examples can over-steer the output.'),
    ]),
    B=[cs('Compare examples with a sample a tailor copies',
          'If you bring a TAILOR your favorite shirt and say "make one like this," the tailor copies its fit, collar '
          'and length. That is helpful. But if you wanted a DIFFERENT color and forgot to say so, you may get the same '
          'color too, because the sample shows everything, not only the parts you meant. A tailor also tends to trust '
          'the shirt in hand over a quick comment. Examples in a request work the same way: they show a lot, and the '
          'tool may copy more than you intended.', [
              Q('What does the tailor copy from the sample shirt?', 'Its fit, collar and length',
                ('Only its price tag', 'not described'), ('Nothing at all', 'the tailor copies it'),
                ('Only the store it came from', 'not described'), 'Samples show many features.'),
              Q('Why might you get the same color?',
          'You did not say the color should differ',
          ('The tailor has only one color of cloth', 'not stated'), ('Colors cannot be changed', 'they can'),
          ('The shirt was the wrong size', 'unrelated'),
          'Unstated differences get copied.'),
              Q('What tends to win: the shirt in hand or a quick comment?', 'The shirt in hand',
                ('The quick comment', 'the sample tends to dominate'), ('Neither', 'the sample wins'),
                ('The tailor\'s mood', 'not described'), 'Concrete samples are powerful.'),
              Q('In a request, what is like the sample shirt?',
          'An example of the output',
          ("The tool's price", 'not the comparison'), ("The user's name", 'not the comparison'),
          ("The tool's privacy settings", 'not the comparison'),
          'Examples are samples.'),
              Q('How do you get a different color from the tailor?', 'Say clearly what should differ',
                ('Bring the same shirt again', 'repeats the problem'), ('Say nothing', 'the color gets copied'),
                ('Ask for the same shirt twice', 'repeats the problem'), 'State the differences.'),
          ], why='A learner who does not expect examples to over-steer can see it through a tailor copying a sample.')],
    F1=sec('Write requests with helpful examples', EXM, [
        Q('Dana wants product descriptions like her best one, but for new products. What should she write?',
          'Her best one, labeled, plus "use the new details"',
          ('Only "write some product descriptions"', 'no example or details'), ('Her best description pasted with no label or note', 'may be copied too closely'),
          ('A list of products with no example at all', 'loses the style she wants'),
          'A labeled example plus what should differ.'),
        Q('A teacher gives one sample math word problem about apples. The results all mention apples. What should she '
          'change?',
          'Add a varied second example or ask for other topics',
          ('Give five more apple problems as examples', 'reinforces apples'),
          ('Remove all instructions and keep the example', 'makes copying worse'),
          ('Nothing; apples are required in math problems', 'not true'),
          'Varied examples or explicit differences help.'),
        Q('Which request best uses an example?',
          '"Style example: \'Bright, simple.\' Write three for new products."',
          ('"Write three product descriptions in a style I would like."', 'no example given'), ('"Write three descriptions for new products, nicely."', 'no example given'),
          ('"Copy this exactly: \'Bright, simple.\'"', 'asks to copy, not to follow a style'),
          'A labeled example and a clear task.'),
        Q('Why label an example clearly?',
          'So it is not mistaken for an instruction',
          ('So the reply becomes longer', 'not the purpose'), ('So the tool can skip reading the example', 'it should read it'),
          ('So the facts become verified', 'labels do not verify'),
          'Labels separate examples from the request.'),
        Q('An example email is formal, but you want a casual email. What is the simplest fix?',
          'Use a casual example, or describe the tone',
          ('Keep the formal example and say nothing else', 'tone will likely be copied'), ('Add three more formal examples', 'reinforces formality'),
          ('Ask for "an email" with no example', 'loses guidance'),
          'Examples should match what you want.'),
    ]),
    F2=sec('Fix conflicts between examples and instructions', EXM_F2, [
        Q('Instructions say "four sentences each," but the only example has two sentences. What result is likely?',
          'Short descriptions that follow the example',
          ('Exactly four sentences every time', 'the example often wins'),
          ('No descriptions at all', 'not likely'),
          ('Descriptions in a different language', 'not likely'),
          'Examples tend to override conflicting rules.'),
        Q('Every example mentions "Brand X." The new descriptions keep mentioning Brand X. What is the best fix?',
          'Use examples without Brand X or vary them',
          ('Add more examples with Brand X', 'makes it worse'),
          ('Remove the instructions but keep the examples', 'makes it worse'),
          ('Ask for longer descriptions', 'does not fix the copying'),
          'Remove the repeated detail from examples.'),
        Q('After fixing a conflicting example, what should you still check?', 'That results follow the written rules',
          ('Only that results match the example\'s topic', 'that was the problem'),
          ('Nothing; fixing the example guarantees success', 'still check'),
          ('Only the number of words in the request', 'not the result'),
          'Check outputs against the rules.'),
        Q('When might it be better to remove an example and describe the pattern in words?',
          'When the example keeps pulling results the wrong way',
          ('When the example matches the rules perfectly', 'then keep it'),
          ('When you want results to copy the example', 'then keep it'),
          ('Never; examples are always required', 'not true'),
          'Describe the pattern if examples mislead.'),
        Q('Two varied examples instead of one usually help because they...', 'show what is the same and what can vary',
          ('make the request use fewer tokens', 'they add tokens'),
          ('guarantee every fact is correct', 'not a guarantee'),
          ('force the tool to ignore instructions', 'not the goal'),
          'Variety shows the general pattern.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.04
STG = ('Big jobs go better in STAGES. Instead of "write my whole business plan," ask first for an outline, check it, '
       'then draft one section at a time, checking each before moving on. Stages help because each step is small '
       'enough to review, mistakes are caught early instead of spreading through everything, and you stay in control '
       'of decisions. A good stage has a clear output you can check, such as a list of questions, an outline, a '
       'draft section, or a table of facts. Later stages can build on the approved earlier ones.')
STG_F2 = ('Stages only help if you actually check between them. If an outline contains a wrong assumption and you '
          'approve it without reading, every later section inherits the mistake. Stages also need carrying forward: '
          'in a new conversation, the tool may not have the earlier approved parts, so paste them in. Not every task '
          'needs stages; a quick email does not. Use stages when a task is long, when early choices shape everything '
          'after, or when facts must be verified before writing.')

S_PROMPT04 = SET(
    'AI.PROMPT.04',
    M=sec('Split a large task into stages you can check', STG, [
        Q('What is the first stage in the passage\'s business-plan example?', 'Ask for an outline and check it',
          ('Ask for the whole plan at once', 'the opposite of staging'),
          ('Ask for the final formatting first', 'formatting comes later'),
          ('Ask for a cover image', 'not the first stage'),
          'An outline is a small, checkable first stage.'),
        Q('Why do stages help catch mistakes?',
          'Each step is small enough to review first',
          ('Stages make the tool incapable of errors', 'they reduce spread, not errors'), ('Stages hide mistakes until the very end', 'the opposite'),
          ('Stages remove the need to read anything', 'you must review'),
          'Small steps are easier to check.'),
        Q('Which is a good stage output?', 'A draft outline you can review',
          ('"Everything, all at once, finished"', 'not a stage'),
          ('A vague feeling that it is going well', 'not checkable'),
          ('The tool\'s promise that it is correct', 'not checkable'),
          'Stages should produce checkable outputs.'),
        Q('What happens to a mistake in an early stage if you do not stage the work?',
          'It can spread through everything after it',
          ('It disappears on its own by the end', 'it spreads'),
          ('It becomes a correct fact', 'no'),
          ('It only affects the first sentence', 'it can affect much more'),
          'Unchecked early errors spread.'),
        Q('Which sequence follows the passage\'s advice?', 'Outline, check, draft a section, check, continue',
          ('Draft everything, then outline, then check', 'out of order'),
          ('Check, then never draft anything', 'no output'),
          ('Draft everything without any checks', 'no checks'),
          'Draft and check stage by stage.'),
    ]),
    B=[cs('Compare stages with building a house',
          'Builders do not put up a whole house in one step. First the FOUNDATION is poured and inspected. Then the '
          'FRAME goes up and is inspected. Then walls, wiring and paint. If the foundation is crooked, it is far '
          'cheaper to fix it before the frame is built on top. Each stage produces something an inspector can check. '
          'Breaking an AI task into stages works the same way: check the outline (the foundation) before building '
          'drafts on top of it.', [
              Q('What is inspected first?', 'The foundation',
                ('The paint', 'that is last'), ('The wiring', 'later'), ('The furniture', 'not a stage here'),
                'The base is checked first.'),
              Q('Why fix a crooked foundation early?',
          'It is cheaper before the frame goes up',
          ('Foundations never matter', 'they do'), ('Paint will hide it', 'it does not fix it'),
          ('Inspectors prefer crooked houses', 'no'),
          'Early fixes cost less.'),
              Q('In an AI task, what is like the foundation?', 'The outline',
                ('The final formatting', 'later'), ('The thank-you note', 'not the comparison'),
                ('The file name', 'not the comparison'), 'The outline supports the rest.'),
              Q('What does each building stage produce?', 'Something an inspector can check',
                ('A secret that cannot be seen', 'not checkable'), ('Nothing until the end', 'each stage produces something'),
                ('A new house each time', 'no'), 'Checkable outputs at each stage.'),
              Q('What happens if the frame is built on a bad foundation?',
          'The problem carries up into the frame',
          ('The frame quietly fixes the foundation', 'no'), ('Nothing changes', 'problems carry forward'),
          ('The house becomes taller', 'unrelated'),
          'Errors carry forward.'),
          ], why='A learner who prefers one giant request can see why stages matter through house-building inspections.')],
    F1=sec('Plan stages for real tasks', STG, [
        Q('Amir must write a 10-page research report. Which first request fits a staged approach?',
          '"Suggest an outline with main sections for my topic."',
          ('"Write the complete 10-page report now."', 'not staged'), ('"Format my finished report."', 'there is no report yet'),
          ('"Write the conclusion first, and only the conclusion."', 'conclusion depends on the rest'),
          'Start with an outline.'),
        Q('A club is planning an event with budget, schedule and publicity. How should it use stages?',
          'Settle the budget and schedule, then write publicity',
          ('Write the publicity first, then decide the budget', 'publicity depends on decisions'),
          ('Ask for everything in one message', 'not staged'),
          ('Skip the budget stage entirely', 'needed early'),
          'Early decisions shape later stages.'),
        Q('After approving an outline, what is the next good stage?',
          'Draft one section and review it',
          ('Draft all sections at once', 'loses the benefit'), ('Ask for a new outline every time', 'no progress'),
          ('Print the outline and stop', 'not finished'),
          'One section at a time.'),
        Q('Which stage output is easiest to check for a cooking video script?', 'A list of the steps in order',
          ('A promise that the video will be fun', 'not checkable'),
          ('A finished script of every word', 'harder to check than a list'),
          ('A note saying "trust me"', 'not checkable'),
          'A short ordered list is easy to verify.'),
        Q('Why might a student ask for "questions I should research first" before drafting?',
          'To gather and check facts before writing',
          ('To avoid doing any research at all', 'the opposite'),
          ('To make the essay longer', 'not the reason'),
          ('To skip the outline stage', 'not the reason'),
          'Verify facts early in a stage.'),
    ]),
    F2=sec('Keep stages honest and connected', STG_F2, [
        Q('A user approved an outline without reading it. It had a wrong date, and every section repeated it. What '
          'went wrong?',
          'The check between stages was skipped',
          ('Staging always causes wrong dates', 'not true'),
          ('The sections should have been written first', 'not the fix'),
          ('Dates cannot be checked', 'they can'),
          'Stages help only when checked.'),
        Q('Tomorrow, Nia continues her project in a new conversation. What should she do first?',
          'Paste in the approved outline and finished sections',
          ('Assume the tool remembers everything', 'a new chat may not have it'), ('Start the whole project over again from nothing', 'wasteful'),
          ('Ask for a different topic', 'not her goal'),
          'Carry approved stages forward.'),
        Q('Which task probably does NOT need stages?', 'A two-line reply confirming a meeting time',
          ('A 30-page grant proposal', 'benefits from stages'),
          ('A semester study plan with many parts', 'benefits from stages'),
          ('A report whose facts must be verified first', 'benefits from stages'),
          'Short, simple tasks can be done at once.'),
        Q('When are stages most valuable?', 'When early choices shape everything after',
          ('When the task is one short sentence', 'little benefit'),
          ('When you do not plan to review anything', 'no benefit'),
          ('When the tool is very fast', 'speed is not the reason'),
          'Stages protect long, dependent tasks.'),
        Q('A draft section contradicts the approved outline. What is the best response?',
          'Point out the conflict; ask for a fix that fits the outline',
          ('Accept it and quietly change the outline to match it', 'loses control'), ('Delete the whole project', 'too extreme'),
          ('Ignore the contradiction', 'it will spread'),
          'Keep later stages consistent with approved ones.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.05
CLAR = ('When a request is missing information, a tool usually fills the gaps with GUESSES, and it may not tell you it '
        'guessed. You can change that. Ask it to ASK CLARIFYING QUESTIONS first ("Before you answer, ask me up to three '
        'questions about anything unclear"), or to STATE ITS ASSUMPTIONS ("List any assumptions you made at the top"). '
        'Both make hidden guesses visible so you can correct them. This is especially useful when details matter, such '
        'as dates, budgets, audiences or rules, and when you are not sure what information the tool needs.')
CLAR_F2 = ('Clarifying questions are only useful if you answer them. And stated assumptions are only useful if you '
           'read them: an assumption like "I assumed the budget is 500 dollars" may be the single most important '
           'line in the answer. Be careful with the opposite problem too: if you answer "whatever you think," the '
           'tool will still guess. Some answers depend on facts only you know, such as your own deadline or a '
           'school\'s rules. When a gap involves such facts, supply them rather than letting the tool invent them.')

CLAR_EX = PR('Plan a birthday party for my son.',
             'Here is a plan for a party with 25 guests, a 600-dollar budget, held at a bowling alley on Saturday '
             'afternoon. Start with bowling at 2 p.m., then pizza and cake at 4 p.m., and party favors at 5 p.m.')

S_PROMPT05 = SET(
    'AI.PROMPT.05',
    M=sec('Ask for clarifying questions or stated assumptions', CLAR, [
        Q('In this fictional example, what did the response do with missing details?',
          'It guessed the guest count, budget and place',
          ('It asked clarifying questions first', 'it did not ask'),
          ('It refused to answer the request', 'it answered'),
          ('It listed its assumptions clearly at the top', 'it presented guesses as the plan'),
          'Gaps were filled with unstated guesses.', ex=CLAR_EX),
        Q('Which added sentence would make hidden guesses visible?',
          '"List any assumptions you made at the top."',
          ('"Make the plan sound exciting and fun."', 'tone, not assumptions'), ('"Use bullet points."', 'format, not assumptions'),
          ('"Keep it under 100 words."', 'length, not assumptions'),
          'Asking for assumptions reveals guesses.'),
        Q('What does "Ask me up to three questions before you answer" do?',
          'Lets the tool collect missing details first',
          ('Makes the answer three times longer', 'not the effect'),
          ('Forces the tool to stop answering forever', 'not the effect'),
          ('Proves the answer will be correct', 'no guarantee'),
          'Questions gather information before the answer.'),
        Q('When is asking for assumptions especially useful?',
          'When details like dates or budgets matter',
          ('When you want a random poem', 'low stakes'),
          ('When you already supplied every detail', 'less needed'),
          ('When you will not read the answer', 'you must read it'),
          'Important details deserve visible assumptions.'),
        Q('Why can unstated guesses be a problem?',
          'You may not notice them and act on them',
          ('Guesses are always correct', 'not true'), ('Guesses make answers shorter than needed', 'not the problem'),
          ('Tools never guess', 'they often do'),
          'Hidden guesses can mislead.'),
    ]),
    B=[sk('Spot what information is missing from a request',
          'A quick way to find gaps is to ask the "W" questions about a request: WHO is it for or about? WHAT exactly '
          'is needed? WHEN is it due or happening? WHERE? HOW MUCH (budget, length, number)? Any important "W" with no '
          'answer is a gap the tool will fill by guessing. Example: "Book a table for dinner" is missing who (how many '
          'people), when (date and time) and where (which area or restaurant).', [
              Q('"Book a table for dinner." Which detail is missing?', 'How many people and when',
                ('That it is for dinner', 'stated'), ('That it is a booking', 'stated'),
                ('That a table is wanted', 'stated'), 'Who and when are missing.'),
              Q('"Plan a trip to the coast." Which "W" is answered?', 'Where (the coast)',
                ('When', 'not stated'), ('How much money', 'not stated'), ('Who is going', 'not stated'),
                'Only where is given.'),
              Q('"Write a 200-word bio for my website." Which detail is answered?', 'How much (200 words)',
                ('Who reads the website', 'not stated'), ('What tone to use', 'not stated'),
                ('When it is needed', 'not stated'), 'Length is given.'),
              Q('Which question finds a budget gap?',
          '"How much can we spend?"',
          ('"Who is it for, exactly?"', 'about people'), ('"Where is it?"', 'about place'),
          ('"When is it?"', 'about time'),
          'Budget is a "how much" question.'),
              Q('A request has no answer for "when." What will the tool likely do?', 'Guess a date or time',
                ('Refuse forever', 'unlikely'), ('Ask the internet for your calendar', 'not likely'),
                ('Leave the answer blank always', 'it usually fills gaps'), 'Gaps get filled by guesses.'),
          ], why='A learner who cannot see what a request leaves out practices finding missing details with "W" '
                 'questions.')],
    F1=sec('Use clarification in practical requests', CLAR, [
        Q('Ray asks for a weekly workout plan but does not know what details matter. What should he add?',
          '"Ask me what you need to know before planning."',
          ('"Make it the best workout plan in the world."', 'no information gathered'), ('"Do not ask me anything."', 'blocks clarification'),
          ('"Make the plan really long."', 'length is not information'),
          'Inviting questions fills gaps he cannot foresee.'),
        Q('A tool\'s answer begins: "Assumptions: you have no car; your budget is 200 dollars." Why is this helpful?',
          'You can quickly correct any wrong assumption',
          ('It proves the plan is correct', 'not a proof'), ('It makes the plan longer', 'not the benefit'),
          ('It means you need not read the rest of the plan', 'still read it'),
          'Visible assumptions are easy to fix.'),
        Q('Which request best avoids silent guesses about a meeting summary?',
          '"Summarize these notes; list unclear points."',
          ('"Summarize these notes perfectly."', 'still may guess'), ('"Summarize these notes fast."', 'still may guess'),
          ('"Summarize these notes in bold text, please."', 'still may guess'),
          'Asking for unclear points exposes gaps.'),
        Q('A tool asks, "Is the event indoors or outdoors?" What should you do?',
          'Answer the question with the real detail',
          ('Ignore it and ask for the plan again', 'loses the benefit'),
          ('Reply "whatever you think"', 'leads to a guess'),
          ('Start a new conversation', 'loses the progress'),
          'Clarifying questions help only if answered.'),
        Q('Which situation most needs stated assumptions?', 'Estimating costs for a school trip budget',
          ('Writing a silly limerick about a cat', 'low stakes'),
          ('Suggesting a name for a houseplant', 'low stakes'),
          ('Choosing a fun font for a party flyer', 'low stakes'),
          'Money decisions depend on assumptions.'),
    ]),
    F2=sec('Close the gaps only you can fill', CLAR_F2, [
        Q('The tool asks three questions and the user replies, "Whatever you think." What will happen?',
          'The tool will still have to guess',
          ('The tool will know the right answers', 'it cannot know'),
          ('The tool will refuse to continue', 'unlikely'),
          ('The answers will be verified automatically', 'not true'),
          'Unanswered questions remain gaps.'),
        Q('An answer lists "Assumed deadline: June 30." Your deadline is June 10. What should you do?',
          'Correct it, since the plan may depend on it',
          ('Ignore it, since assumptions do not matter', 'it may matter most'),
          ('Move your real deadline to June 30', 'not realistic'),
          ('Ask for a longer answer', 'does not fix the date'),
          'Read and correct key assumptions.'),
        Q('Which gap should you fill yourself rather than let the tool guess?', 'Your school\'s rules for a project',
          ('Synonyms for the word "happy"', 'the tool can suggest'),
          ('Ideas for a story title', 'the tool can suggest'),
          ('A list of colors that go well with blue', 'the tool can suggest'),
          'Facts only you know must come from you.'),
        Q('A tool states several assumptions. Which one deserves the closest reading?', 'The one your decision depends on',
          ('The shortest one in the list', 'length is not importance'),
          ('The one written in a friendly tone', 'tone is not importance'),
          ('None; assumptions are just filler', 'they can matter most'),
          'Check decision-critical assumptions first.'),
        Q('Why is "I assumed the budget is 500 dollars" possibly the most important line?',
          'The whole plan may be built on that number',
          ('It is the longest sentence', 'length is not importance'), ('Budgets never change plans', 'they often do'),
          ('It proves that the plan is affordable', 'it is an assumption'),
          'A wrong budget changes everything.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.06
REV = ('A first answer is a DRAFT. To improve it, decide what "good" means before you judge it: write SUCCESS '
       'CRITERIA, a short list of checkable requirements such as "mentions all three options," "under 200 words," '
       '"no jargon," "includes a deadline." Then compare the draft against each criterion and ask for specific '
       'changes ("the deadline is missing; add it to the first paragraph"). Specific feedback works better than "make '
       'it better." Criteria also help you compare two drafts fairly, by scoring each against the same list instead '
       'of picking the one that simply sounds nicer.')
REV_F2 = ('Revising can go wrong in a few ways. Each new draft may fix one problem and quietly break another, so '
          'recheck all criteria, not only the one you asked about. Repeated "try again" requests without feedback '
          'can produce drafts that are different but not better. And a draft can meet every stated criterion while '
          'still being wrong about facts, because criteria about format do not check truth. Include accuracy in your '
          'criteria when it matters, and stop revising when the criteria are met.')

S_PROMPT06 = SET(
    'AI.PROMPT.06',
    M=sec('Write success criteria and use them to revise', REV, [
        Q('What are success criteria?',
          'A short list of checkable requirements',
          ("The tool's own rating of its answer", 'not your criteria'), ('A list of synonyms for "good"', 'not checkable requirements'),
          ('The number of times you asked', 'not criteria'),
          'Criteria define what "good" means.'),
        Q('Which is the most useful feedback on a draft?',
          '"The deadline is missing; add it up top."',
          ('"Make it better than this version."', 'too vague'), ('"Try again with a new draft."', 'no direction'),
          ('"I don\'t like this draft very much."', 'no direction'),
          'Specific feedback guides revision.'),
        Q('Which is a checkable criterion?',
          '"Mentions all three options"',
          ('"Feels right to me"', 'vague'), ('"Is pretty good overall"', 'vague'),
          ('"Sounds smart enough"', 'vague'),
          'You can check whether all three appear.'),
        Q('How do criteria help compare two drafts?', 'Both are scored against the same list',
          ('The longer draft automatically wins', 'length is not a criterion'),
          ('The draft that sounds nicer wins', 'not a fair comparison'),
          ('The first draft always wins', 'no reason'),
          'Shared criteria make comparison fair.'),
        Q('When should you write the criteria?', 'Before judging the draft',
          ('After choosing the draft you like', 'too late to be fair'),
          ('Never; drafts speak for themselves', 'criteria help'),
          ('Only if the draft is very long', 'always useful'),
          'Decide what "good" means first.'),
    ]),
    B=[sk('Score a draft against a checklist',
          'Scoring against a CHECKLIST is simple: read each criterion, look at the draft, and mark it MET or NOT MET. '
          'Example criteria for an invitation: (1) gives the date, (2) gives the place, (3) says how to reply, (4) under '
          '80 words. Draft: "Join us Saturday at Lakeside Park! Bring a snack." Date: met (Saturday). Place: met '
          '(Lakeside Park). How to reply: not met. Under 80 words: met. Score: 3 of 4. The missing item tells you '
          'exactly what to ask for next.', [
              Q('Which criterion did the invitation miss?', 'How to reply',
                ('The date', 'met'), ('The place', 'met'), ('Under 80 words', 'met'),
                'There is no reply instruction.'),
              Q('What score did the invitation get?', '3 of 4',
                ('4 of 4', 'one is missing'), ('2 of 4', 'three are met'), ('1 of 4', 'three are met'),
                'Three criteria are met.'),
              Q('What should the next request ask for?', 'Add how to reply',
                ('Change the park', 'already met'), ('Make it longer', 'not needed'),
                ('Remove the date', 'already met'), 'Fix the unmet criterion.'),
              Q('How do you mark each criterion?', 'Met or not met',
                ('Pretty or ugly', 'not checkable'), ('Long or short only', 'too narrow'),
                ('Fun or boring', 'not checkable'), 'A clear yes/no for each.'),
              Q('Draft B: "Party Saturday at Lakeside Park. Text Jo to reply." It is 9 words. Score?', '4 of 4',
                ('3 of 4', 'all are met'), ('2 of 4', 'all are met'), ('0 of 4', 'all are met'),
                'Date, place, reply and length are all met.'),
          ], why='A learner who revises by feel practices the underlying skill of scoring a draft against a checklist.')],
    F1=sec('Revise real drafts against criteria', REV, [
        Q("Kai's criteria for a club flyer: date, place, cost, under 60 words. The draft has date and place only. What should he ask?",
          '"Add the cost and keep it under 60 words."',
          ('"Make it better somehow."', 'vague'), ('"Start over completely."', 'wasteful'),
          ('"Add more exciting adjectives throughout."', 'not a criterion'),
          'Ask for the unmet criteria.'),
        Q('Two cover-letter drafts: A meets 4 of 5 criteria, B meets 2 of 5 but sounds fancier. Which should Mei pick '
          'to refine?',
          'Draft A',
          ('Draft B, since it sounds fancier', 'sounding fancy is not a criterion'),
          ('Neither; criteria cannot compare drafts', 'they can'),
          ('Whichever is longer', 'length is not a criterion'),
          'Criteria guide a fair choice.'),
        Q('Which list makes good success criteria for a recipe summary?',
          '"All ingredients; numbered steps; under 150 words"',
          ('"Tasty; pretty; impressive"', 'not checkable'), ('"As good as possible"', 'not checkable'),
          ('"Something my friends and family would like"', 'not checkable'),
          'Each item can be checked.'),
        Q("A draft is missing the meeting's location. What feedback is most effective?",
          '"Add the location after the time in the first line."',
          ('"Something is missing here, so figure it out."', 'vague'), ('"Try a few more times."', 'no direction'),
          ('"This is wrong."', 'no direction'),
          'Name the gap and where to fix it.'),
        Q('Why write criteria before reading a draft?',
          'So you judge it fairly, not by its sound',
          ('So the draft becomes much shorter and tighter', 'not the reason'), ('So you can skip reading it', 'you still read it'),
          ('So the tool writes faster', 'not the reason'),
          'Criteria first keeps judgment fair.'),
    ]),
    F2=sec('Avoid revision traps', REV_F2, [
        Q('After you asked for an added deadline, the new draft has the deadline but lost the location. What does this '
          'show?',
          'Recheck all criteria after each revision',
          ('Revisions never change other parts', 'they can'),
          ('Locations are not important', 'they were a criterion'),
          ('The first draft must have been perfect', 'not implied'),
          'Fixes can break other parts.'),
        Q('A user typed "try again" ten times without feedback. The drafts differ but none improve. Why?',
          'Without specific feedback, changes are not aimed',
          ('Ten is not enough tries', 'more tries alone will not help'), ('The tool is out of words', 'not the reason'),
          ('Drafts can never really be improved at all', 'they can with feedback'),
          'Targeted feedback directs revision.'),
        Q('A report meets all format criteria but contains a wrong statistic. What was missing from the criteria?',
          'An accuracy check of the facts',
          ('A rule about the font size', 'format, not truth'),
          ('A longer word limit', 'not the issue'),
          ('A friendlier tone', 'not the issue'),
          'Format criteria do not check truth.'),
        Q('When should you stop revising?', 'When the criteria are met',
          ('After exactly ten drafts', 'arbitrary'),
          ('Never; drafts can always be better', 'diminishing returns'),
          ('As soon as it sounds nice', 'not the criteria'),
          'Criteria tell you when you are done.'),
        Q('Which criterion would best protect a science handout from errors?',
          '"Every fact matches the textbook"',
          ('"Uses colorful section headings"', 'format'), ('"Fits on one page"', 'format'),
          ('"Has a fun title"', 'style'),
          'Include accuracy when it matters.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.07
CONF = ('Some requests contain CONFLICTING REQUIREMENTS: rules that cannot all be met at once. "Explain the history of '
        'the internet in full detail in 50 words" is one; "make it formal and very casual" is another. A tool usually '
        'does not stop to ask. It quietly breaks one rule, blends both badly, or claims success anyway. Watch for '
        'conflicts in length versus detail, tone versus audience, and speed versus completeness. When you notice one, '
        'decide which requirement matters more, or how to split the job, before continuing, for example two '
        'versions or a short summary plus a longer appendix.')
CONF_F2 = ('Conflicts are not always visible in the request itself. A rule from earlier in a conversation ("always '
           'under 100 words") can clash with a new request ("include every detail from this 20-page report"). A '
           'supplied document can conflict with your instructions, such as a template with five sections when you '
           'asked for three. When results look strange, look for an older or hidden rule. Ask the tool to point out '
           'any conflicting requirements before it starts, and resolve them yourself instead of letting it choose.')

S_PROMPT07 = SET(
    'AI.PROMPT.07',
    M=sec('Notice requirements that cannot all be met', CONF, [
        Q('Which request contains a conflict?', '"Explain every step in full detail in 20 words."',
          ('"Explain the steps for beginners, in plain words."', 'no conflict'),
          ('"Explain the steps as a numbered list."', 'no conflict'),
          ('"Explain the steps for a 10-year-old reader."', 'no conflict'),
          'Full detail and 20 words cannot both be met.'),
        Q('What does a tool usually do with conflicting rules?', 'Quietly breaks one or blends them badly',
          ('Always stops and asks which rule matters', 'usually it does not'),
          ('Refuses to answer anything', 'not usual'),
          ('Meets every rule perfectly', 'impossible by definition'),
          'Conflicts produce compromised results.'),
        Q('"Make it formal and very casual." What kind of conflict is this?', 'Tone versus tone',
          ('Length versus detail', 'not about length'), ('Speed versus completeness', 'not about speed'),
          ('Format versus audience', 'not this one'), 'Two tones clash.'),
        Q('What should you do when you notice a conflict?', 'Decide which rule matters more or split the job',
          ('Send it anyway and accept whatever comes', 'risks a bad result'),
          ('Add a third conflicting rule', 'makes it worse'),
          ('Delete the whole request', 'unnecessary'),
          'Resolve conflicts before continuing.'),
        Q('Which is a way to split a conflicting job?', 'A short summary plus a longer appendix',
          ('One sentence that includes everything', 'still conflicts'),
          ('No output at all', 'not a solution'),
          ('Two copies of the same summary', 'does not split the needs'),
          'Separate outputs can meet different needs.'),
    ]),
    B=[cs('Compare conflicting rules with a packing list',
          'Imagine packing for a trip with two rules: "Bring everything you might need" and "Use only one small '
          'backpack." You cannot follow both. If you do not decide, you might stuff the bag until it breaks, or leave '
          'behind something important without noticing. A sensible traveler decides which rule wins ("the small bag '
          'is required, so bring only essentials") or changes the plan ("take a second bag"). Conflicting requirements '
          'in a request work the same way.', [
              Q('What is the conflict in the packing example?',
          'Everything you need versus one small bag',
          ('A small bag versus a bright blue bag', 'not described'), ('Shoes versus socks', 'not described'),
          ('Morning versus evening', 'not described'),
          'The two rules cannot both be met.'),
              Q('What can happen if you do not decide?',
          'You may break the bag or forget things',
          ('Everything fits perfectly inside', 'not possible'), ('The bag grows bigger', 'no'),
          ('The trip is canceled', 'not described'),
          'Unresolved conflicts cause problems.'),
              Q('Which is a sensible decision?',
          '"The small bag is required; pack essentials."',
          ('"Ignore both rules."', 'not sensible'), ('"Pack everything and hope that it closes."', 'not a decision'),
          ('"Pack nothing."', 'not sensible'),
          'Choose which rule wins.'),
              Q('Which changes the plan instead?', '"Take a second bag."',
                ('"Pack more tightly forever."', 'not a plan change'), ('"Forget the trip."', 'avoids the problem'),
                ('"Ask a stranger."', 'not described'), 'Splitting the job resolves the conflict.'),
              Q('In a request, what is like the two packing rules?',
          'Two requirements that cannot both be met',
          ('A single clear requirement and nothing else', 'no conflict'), ('A greeting', 'unrelated'),
          ("The tool's settings", 'unrelated'),
          'Conflicting requirements.'),
          ], why='A learner who misses conflicts in a request can see them in an everyday packing dilemma.')],
    F1=sec('Resolve conflicts in practical requests', CONF, [
        Q('Lucy asks for "a one-page summary that covers all 40 pages in detail." What is the best fix?',
          'A one-page summary of key points; details on request',
          ('Send it as written and trust the result', 'conflict unresolved'), ('Ask for a 40-page summary', 'not a summary'),
          ('Remove the page limit and ask for "everything"', 'loses her need for one page'),
          'Prioritize and split.'),
        Q('A manager wants a report "by noon, fully researched with every source checked." It is 11:30. What should happen first?',
          'Decide whether speed or completeness wins',
          ('Promise both and hope', 'conflict ignored'), ('Skip checking the sources without telling anyone', 'quietly breaks a rule'),
          ('Ask for even more sources', 'worse conflict'),
          'Speed versus completeness must be resolved.'),
        Q('Which request has NO conflict?', '"A friendly note for coworkers, under 100 words."',
          ('"A friendly note that is also strictly formal."', 'tone conflict'),
          ('"Every detail, in one sentence."', 'length conflict'),
          ('"A quick note with a full history."', 'length conflict'),
          'Friendly, coworkers and under 100 words fit together.'),
        Q('A tool claims it met "detailed" and "under 30 words" for a complex topic. What should you suspect?',
          'It sacrificed detail or broke the limit',
          ('It achieved both perfectly', 'unlikely for a complex topic'),
          ('The topic must be simple after all', 'not shown'),
          ('Word limits do not apply to it', 'they do'),
          'Check which requirement was broken.'),
        Q('A teacher wants a worksheet that is "challenging" and "easy for everyone." Which fix splits the job?',
          'Two versions: a core and a challenge sheet',
          ('One sheet that is somehow both at once', 'still conflicting'), ('No worksheet at all', 'no solution'),
          ('A harder sheet for everyone', 'drops the easy need'),
          'Two versions meet both needs.'),
    ]),
    F2=sec('Find hidden conflicts before continuing', CONF_F2, [
        Q('Earlier in a chat you said "always under 100 words." Now you ask for every detail of a long report. What '
          'might happen?',
          'The old rule clashes with the new request',
          ('The old rule disappears automatically', 'it may still apply'),
          ('The report will be summarized perfectly', 'conflict unresolved'),
          ('The tool will refuse all future requests', 'unlikely'),
          'Older rules can conflict with new ones.'),
        Q('Your template has five sections, but you asked for three. Results come out with five. Why?',
          'The template conflicts with your instruction',
          ('The tool cannot count sections', 'not the reason'), ('Five is always the default', 'not true'),
          ('Your instruction was never received by the tool', 'not likely'),
          'Supplied material can conflict with instructions.'),
        Q('Results look strange and you suspect a hidden conflict. What is a good first step?',
          'Look for an older rule or file that clashes',
          ('Rewrite the whole request in capitals', 'not a fix'), ('Assume the tool is broken', 'check first'),
          ('Ask for the same thing again', 'repeats the conflict'),
          'Hunt for the hidden rule.'),
        Q('Which request helps catch conflicts early?',
          '"First, point out any conflicting requirements."',
          ('"Be quick and do not ask me anything at all."', 'blocks the check'), ('"Just do your best."', 'no check'),
          ('"Use as many words as you like."', 'not about conflicts'),
          'Ask the tool to flag conflicts.'),
        Q('The tool points out that your length limit conflicts with your detail request. Who should decide?',
          'You, since it is your priority',
          ('The tool, without telling you', 'you lose control'),
          ('Nobody; send it anyway', 'unresolved'),
          ('A random coin flip', 'not a decision'),
          'Priorities are the user\'s choice.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.08
SRCM = ('Two habits make results more grounded and easier to check. First, SUPPLY THE RELEVANT SOURCE MATERIAL: paste '
        'the actual policy, article, notes or data you want used, and say "use only the text below." That steers the '
        'answer toward your material instead of the tool\'s general patterns. Second, ask for STRUCTURED OUTPUT, such '
        'as a table with named columns or a list with a fixed set of fields, that you can scan quickly. A table of '
        '"Claim | Where in the text" is much easier to verify than a long paragraph. Supply only what is relevant; '
        'unrelated material can distract.')
SRCM_F2 = ('Supplying material does not guarantee faithful use. A tool may still add outside facts, misread a table, '
           'or miss part of a long document. Asking it to quote or point to the exact sentence for each claim makes '
           'gaps visible. Structured output has limits too: a neat table can contain wrong values, and forcing '
           'information into fixed columns can drop important nuance, such as "only on weekdays." Check a few entries '
           'against the source, and include a "notes" column when exceptions matter.')

SRCM_EX = TABLE([['Claim from the summary', 'Where in the policy'], ['Returns accepted within 30 days', 'Section 2'],
                 ['Store credit for opened items', 'Section 3'], ['Free return shipping on all orders', 'Not found']],
                label='Prepared example (a structured summary of a fictional store policy)')

S_PROMPT08 = SET(
    'AI.PROMPT.08',
    M=sec('Supply source material and request structured output', SRCM, [
        Q('Why paste the actual policy text and say "use only the text below"?',
          'It steers the answer toward your material',
          ('It guarantees the answer is perfect', 'not a guarantee'),
          ('It retrains the model on the policy', 'it does not retrain'),
          ('It makes the answer longer', 'not the purpose'),
          'Supplied text grounds the answer.'),
        Q('Which output is easiest to verify?',
          'A table of each claim and where it appears',
          ('A long paragraph with no references at all', 'harder to check'), ('A poem summarizing the text', 'harder to check'),
          ('A one-word answer with no context', 'nothing to check against'),
          'Structure makes checking quick.'),
        Q('In this prepared example, which claim needs attention?', '"Free return shipping on all orders"',
          ('"Returns accepted within 30 days"', 'found in Section 2'),
          ('"Store credit for opened items"', 'found in Section 3'),
          ('None; every claim was found', 'one was not found'),
          'It was not found in the policy.', ex=SRCM_EX),
        Q('Why supply only relevant material?',
          'Unrelated material can distract from the task',
          ('Relevant material is always too long to paste', 'not the reason'), ('Tools cannot read unrelated text', 'they can, which is the problem'),
          ('More text always improves accuracy', 'not when unrelated'),
          'Focus helps the tool use the right material.'),
        Q('Which is an example of structured output?',
          'A table with columns Name, Date and Cost',
          ('A friendly paragraph about the costs', 'unstructured'), ('A story about a shopping trip', 'unstructured'),
          ('A single sentence of advice', 'unstructured'),
          'Named columns are structure.'),
    ]),
    B=[sk('Match a claim to the sentence that supports it',
          'To check whether a summary used its source faithfully, take one CLAIM at a time and find the SENTENCE in '
          'the source that supports it. Source: "The library opens at 9 a.m. on weekdays. On Saturdays it opens at 10. '
          'It is closed Sundays." Claim: "It opens at 10 on Saturdays." Supported by sentence 2. Claim: "It opens at 9 '
          'every day." Not supported: sentence 1 says weekdays only. If no sentence supports a claim, or a sentence '
          'contradicts it, mark the claim.', [
              Q('Which sentence supports "It is closed Sundays"?', 'Sentence 3',
                ('Sentence 1', 'about weekdays'), ('Sentence 2', 'about Saturdays'),
                ('None of them', 'sentence 3 does'), 'Sentence 3 states it.'),
              Q('Is "It opens at 9 every day" supported?',
          'No; sentence 1 says weekdays only',
          ('Yes; sentence 1 says so', 'it limits to weekdays'), ('Yes; sentence 3 says so', 'no'),
          ('Yes; all three sentences agree', 'they do not'),
          'The claim overstates the source.'),
              Q('Which sentence supports "It opens at 10 on Saturdays"?', 'Sentence 2',
                ('Sentence 1', 'weekdays'), ('Sentence 3', 'Sundays'), ('No sentence', 'sentence 2 does'),
                'Sentence 2 states it.'),
              Q('A claim says "It opens at 8 a.m. on Mondays." What should you mark?', 'Not supported (contradicted)',
                ('Supported by sentence 1', 'sentence 1 says 9'), ('Supported by sentence 2', 'about Saturdays'),
                ('Supported by sentence 3', 'about Sundays'), 'The source says 9 on weekdays.'),
              Q('What is the first step in checking a summary?',
          'Take one claim and find its support',
          ('Read the summary twice to judge its tone', 'not a check'), ("Count the summary's words", 'not a check'),
          ('Trust it if it is short', 'not a check'),
          'Claim by claim.'),
          ], why='A learner unsure how to verify grounded output practices matching claims to supporting sentences.')],
    F1=sec('Ground requests in real material', SRCM, [
        Q('Zoe wants answers about her lease, not leases in general. What should she do?',
          'Paste the lease; say "answer only from this"',
          ('Ask "what do leases usually say?"', 'general, not hers'), ('Describe her lease from memory, without pasting it', 'less reliable'),
          ('Ask for a longer answer', 'not grounding'),
          'Supply the actual document.'),
        Q('A manager needs to compare three vendor quotes. Which output is easiest to check?',
          'A table: Vendor, Price, Delivery date, Warranty',
          ('A paragraph describing each vendor', 'harder to scan'), ('A ranking with no details', 'cannot verify'),
          ('A motivational note about choosing vendors well', 'unhelpful'),
          'A comparison table is easy to verify.'),
        Q('Which instruction keeps an answer close to supplied notes?',
          '"Use only the notes below; say if something is missing."',
          ('"Use the notes and anything else you know."', 'invites outside facts'), ('"Ignore the notes whenever you have better ideas."', 'abandons the notes'),
          ('"Make the notes sound more exciting."', 'not grounding'),
          'Restrict to the notes and flag gaps.'),
        Q('Ben pastes a 50-page handbook to ask about one vacation rule. What would help?',
          'Paste only the vacation section',
          ('Paste three handbooks', 'distracting'), ('Paste nothing and ask generally', 'ungrounded'),
          ('Paste the handbook twice', 'distracting'),
          'Relevant material only.'),
        Q('Which column helps you verify each claim in a summary table?', '"Where in the text"',
          ('"How exciting it sounds"', 'not verification'), ('"Font used"', 'irrelevant'),
          ('"Number of letters"', 'irrelevant'), 'A location lets you check the source.'),
    ]),
    F2=sec('Check that supplied material was used faithfully', SRCM_F2, [
        Q('An answer about a supplied policy includes a rule the policy never mentions. What happened?',
          'The tool added outside information',
          ('The policy must secretly contain it', 'it does not'),
          ('Supplied text always prevents outside facts', 'not guaranteed'),
          ('The rule must be correct anyway', 'unsupported'),
          'Supplying material does not guarantee faithful use.'),
        Q('Which request makes gaps in grounding most visible?', '"For each claim, quote the sentence it comes from."',
          ('"Make the answer as confident as possible."', 'confidence hides gaps'),
          ('"Keep it to one paragraph."', 'does not expose gaps'),
          ('"Use a friendly tone."', 'does not expose gaps'),
          'Quotes show where each claim comes from.'),
        Q('A neat table lists a store as "Open 9-5," but the source says "9-5 weekdays only." What was lost?',
          'An important exception (weekdays only)',
          ("The store's name", 'still there'), ('The opening time', 'still there'),
          ('Nothing; the table is complete as it is', 'the exception was lost'),
          'Fixed columns can drop nuance.'),
        Q('How can a table keep exceptions like "weekdays only"?', 'Add a Notes column',
          ('Remove all columns but one', 'loses information'),
          ('Make the table smaller', 'loses information'),
          ('Use bigger fonts', 'irrelevant'),
          'A notes column keeps nuance.'),
        Q('A tool summarized a long supplied report. What is a sensible check?',
          'Compare a few entries against the report itself',
          ('Assume it read every page of the report carefully', 'may have missed parts'), ('Check only the formatting', 'not accuracy'),
          ('Ask whether it is sure', 'not a real check'),
          'Spot-check against the source.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.PROMPT.09
MYTH = ('Some popular prompt advice is myth. ROLE-PLAY ("You are a world-class doctor") can change tone and vocabulary, '
        'but it does not give a tool knowledge or a license it lacks. Asking it to "be accurate," "be 100 percent '
        'sure" or "only say true things" does not create a way to check truth. Demanding CITATIONS can produce '
        'references that look real but are invented or do not support the claim. And there is no MAGIC FORMULA of '
        'words that guarantees good results; what helps is clear context, examples, constraints and checking. Good '
        'prompts improve the odds; they do not remove the need to verify.')
MYTH_F2 = ('Myths spread because they sometimes seem to work: a role-play prompt may produce more polished language, '
           'which feels like expertise. But style is not substance. When an answer matters, judge it by what you can '
           'check, not by how it was prompted. Be wary of anyone selling "secret prompts" that promise perfect or '
           'guaranteed results. Prompt advice that is useful tends to be plain and testable: say what you need, give '
           'context and examples, state constraints, and check the output.')

MYTH_EX = PR('You are a world-class doctor. What dose of a common pain reliever should my 4-year-old take?',
             'As a world-class physician, I recommend 500 mg every four hours for your child.')

S_PROMPT09 = SET(
    'AI.PROMPT.09',
    M=sec('Explain why common prompt myths do not create accuracy', MYTH, [
        Q('What does "You are a world-class doctor" change in a response?', 'Mainly tone and wording, not real expertise',
          ('It gives the tool a medical license', 'no license is created'),
          ('It guarantees medically correct answers', 'no guarantee'),
          ('It connects the tool to a hospital', 'not what role-play does'),
          'Role-play shapes style, not knowledge.'),
        Q('In this fictional example, what should a parent do with the dose shown?',
          'Not use it; check the label or a pharmacist',
          ('Use it, since the tool spoke as a doctor', 'role-play is not expertise'),
          ('Use half of it to be safe', 'still unverified'),
          ('Ask the tool to repeat it more confidently', 'confidence is not accuracy'),
          'A high-stakes answer needs a qualified check.', ex=MYTH_EX),
        Q('What does adding "be 100 percent accurate" do?', 'It does not give the tool a way to check truth',
          ('It switches on a hidden fact-checking mode', 'no such guarantee'),
          ('It makes every answer correct', 'not possible'),
          ('It blocks the tool from writing', 'not the effect'),
          'Requests for accuracy are not checks.'),
        Q('What is a risk of demanding citations?',
          'They may look real but be invented',
          ('Citations are always verified before they are shown', 'not true'), ('Citations make answers shorter', 'not the risk'),
          ('Tools cannot write citations', 'they can'),
          'Generated citations need checking.'),
        Q('What actually improves results?',
          'Clear context, examples, constraints and checking',
          ('A secret phrase that guarantees success every time', 'myth'), ('Typing in all capital letters', 'not reliable'),
          ('Threatening the tool', 'not reliable'),
          'Plain, testable practices help.'),
    ]),
    B=[cs('Compare role-play with wearing a costume',
          'Putting on a PILOT\'S UNIFORM for a costume party does not teach you to fly a plane. You might walk and talk '
          'more like a pilot, and people might trust you more, but your actual skills are unchanged. Telling an AI '
          'tool "you are an expert pilot" is like handing it the costume: it may use pilot-like words and sound more '
          'confident, but it gains no new knowledge, training or license. Trust should come from evidence, not from '
          'the costume.', [
              Q('Does the uniform teach you to fly?', 'No, your skills stay the same',
                ('Yes, uniforms carry flight lessons', 'no'), ('Yes, after one hour', 'no'),
                ('Only on long flights', 'no'), 'A costume changes appearance only.'),
              Q('What might change when you wear the uniform?',
          'How you talk and how others trust you',
          ('Your real ability to land a plane', 'unchanged'), ('Your eyesight', 'unchanged'),
          ('Your knowledge of weather', 'unchanged'),
          'Style and trust can shift.'),
              Q('Telling a tool "you are an expert pilot" is like what?', 'Handing it the costume',
                ('Giving it flight training', 'no training is given'), ('Giving it a license', 'no license'),
                ('Giving it a plane', 'no'), 'Role-play is a costume.'),
              Q('Where should trust come from?', 'Evidence you can check',
                ('The costume', 'not evidence'), ('A confident voice', 'not evidence'),
                ('Fancy vocabulary', 'not evidence'), 'Evidence earns trust.'),
              Q('Why can a costume be risky?',
          'People may trust skills that are absent',
          ('It makes people distrust you more', 'the opposite risk'), ('It is too heavy', 'not the point'),
          ('It changes the weather', 'nonsense'),
          'False trust is the danger.'),
          ], why='A learner who believes role-play creates expertise can see the gap through a costume example.')],
    F1=sec('Recognize prompt myths in practice', MYTH, [
        Q('A video promises a "secret prompt" that makes any AI "never wrong." What is the best response?',
          'Be skeptical; no wording guarantees accuracy',
          ('Buy it, since secret prompts are proven', 'not proven'), ('Use it and stop checking answers', 'unsafe'),
          ('Share it widely as a guarantee', 'spreads a myth'),
          'No magic formula exists.'),
        Q('Jen adds "cite your sources" and gets five neat references. What should she do?',
          'Open each to see whether it exists and supports it',
          ('Trust them because they look formal', 'formatting is not proof'), ('Delete them, since citations are never real', 'some may be real'),
          ('Count them; five means reliable', 'count is not quality'),
          'Check generated citations.'),
        Q('A student writes "You are a genius math teacher" before asking for homework help. What changes?',
          'Maybe the tone; answers still need checks',
          ('Every answer becomes correct', 'not guaranteed'), ('The tool becomes a licensed math teacher', 'not true'),
          ('Nothing at all can change', 'tone may change'),
          'Role-play affects style, not accuracy.'),
        Q('Which change most improves a request for a budget plan?',
          'Adding real income, bills and goals',
          ('Adding "be a financial genius"', 'role-play, not information'),
          ('Adding "be 100 percent sure"', 'not a check'),
          ('Adding "this is very important"', 'urgency, not information'),
          'Real context helps.'),
        Q('A coworker says prompts with "expert" in them are always more accurate. What is the problem?',
          'Expert wording can sound better without being right',
          ('Nothing; the word "expert" always boosts accuracy', 'not true'), ('Expert prompts are illegal', 'nonsense'),
          ('Prompts cannot change anything', 'they can change style'),
          'Style is not substance.'),
    ]),
    F2=sec('Judge answers by evidence, not by the prompt', MYTH_F2, [
        Q('A role-play prompt produced polished legal language. Why might that feel like expertise?',
          'Polished style can look like real knowledge',
          ('Polished language is proof of expertise', 'not proof'),
          ('Legal language is always accurate', 'not true'),
          ('Role-play adds a law degree', 'not true'),
          'Style can be mistaken for substance.'),
        Q('A course sells "guaranteed perfect prompts." What should a buyer expect?',
          'No prompt can guarantee perfect results',
          ('Perfect results every single time', 'not possible'), ('A license to skip checking', 'not real'),
          ('Accurate citations always', 'not guaranteed'),
          'Guarantees are a warning sign.'),
        Q('Two answers to the same health question: one from a plain prompt, one from an "expert doctor" prompt. How '
          'should you judge them?',
          'By what each claim can be checked against',
          ('Trust the "expert doctor" one automatically', 'role-play is not credentials'),
          ('Trust the plain one automatically', 'neither is proven'),
          ('Pick the longer one', 'length is not evidence'),
          'Evidence, not prompting, decides.'),
        Q('Which piece of prompt advice is plain and testable?',
          '"Give context and examples, then check the output."',
          ('"Always tell it you will be upset."', 'not testable'), ('"Use the secret word to unlock full accuracy."', 'myth'),
          ('"Say it is a genius every time."', 'myth'),
          'Useful advice can be tested.'),
        Q('A prompt included "only state verified facts," yet the answer had an error. What does this show?',
          'Instructions about truth do not create verification',
          ('The instruction was typed too quietly', 'nonsense'),
          ('Errors are impossible after that instruction', 'disproved by the example'),
          ('The error must be a typo by the user', 'not implied'),
          'Asking for truth is not checking truth.'),
    ]),
)

SETS = [S_PROMPT01, S_PROMPT02, S_PROMPT03, S_PROMPT04, S_PROMPT05, S_PROMPT06, S_PROMPT07, S_PROMPT08, S_PROMPT09]
