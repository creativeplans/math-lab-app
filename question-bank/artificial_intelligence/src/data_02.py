"""Foundation 2: How a model learns (AI.LEARN.01-05, AI.LEARN.08)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.LEARN.01
TRAIN = ('An AI model has two very different stages. TRAINING is when the model learns: it is shown large amounts of '
         'example data and its internal settings are adjusted again and again until its outputs match the examples '
         'well. Training happens before you use the model and usually takes a lot of computing power. INFERENCE (or '
         'simply "using the model") is when the finished model takes NEW input, such as your question or photo, and '
         'produces an output. During ordinary use the model\'s learned settings do not change. Typing a question into '
         'an app is inference, not training.')
TRAIN_F2 = ('Products can blur the line between training and use, so it helps to ask exactly what changes. Rating an '
            'answer "thumbs up" or "thumbs down" does not instantly retrain the model; a company MAY later use such '
            'feedback, along with other data, to train a new version, depending on its policies. Some products keep '
            'notes about you between conversations, which feels like learning but is stored information the product '
            'feeds back in, not a change to the model\'s settings. When you want to know whether your data could be '
            'used for training, read the provider\'s data policy and settings.')

S_LEARN01 = SET(
    'AI.LEARN.01',
    M=sec('Tell training from inference (using the model)', TRAIN, [
        Q('A company shows a model millions of labeled photos and adjusts it until it sorts them well. Which stage is this?',
          'Training',
          ('Inference', 'it is still learning from examples'), ('Neither, because sorting photos is not AI', 'sorting photos is a common AI task'),
          ('Inference, because the photos are labeled', 'labels are used for learning'),
          'Adjusting the model to match examples is training.'),
        Q('You type a question into a finished chatbot and get a reply. Which stage is this?',
          'Inference: the finished model handles new input',
          ('Training: the model rewrites itself for your question', 'its learned settings do not change'),
          ('Training: your question becomes part of its settings', 'ordinary use does not change the settings'),
          ('Neither stage, because no model is involved', 'a model produces the reply'),
          'Using a finished model on new input is inference.'),
        Q('Which statement about training is accurate?',
          'It adjusts the model\'s settings using many examples',
          ('It happens each time anyone opens the app on a phone', 'training happens before use'),
          ('It needs only one example to finish completely', 'training uses large amounts of data'),
          ('It is the same as typing a question to the model', 'that is inference'),
          'Training means repeated adjustment using many examples.'),
        Q('During ordinary use (inference), what happens to the model\'s learned settings?',
          'They stay the same',
          ('They reset to random values', 'they keep what was learned'),
          ('They update after every message', 'ordinary use does not update them'),
          ('They copy the user\'s whole device', 'not what happens'),
          'Inference uses the settings; it does not change them.'),
        Q('Why does training usually cost much more computing power than a single use?',
          'It repeats adjustments over huge amounts of data',
          ('It only ever handles one short question at a time', 'that describes a single use'),
          ('It happens on the user\'s phone after each reply', 'training is usually done in advance'),
          ('It must print out every training example on paper', 'not how training works'),
          'Training processes vast data many times.'),
    ]),
    B=[cs('Compare studying for a driving test with driving',
          'Think about learning to drive. While you STUDY and PRACTICE with a teacher, you make mistakes, get '
          'corrected and slowly improve: that is like TRAINING. Once you have your license and drive to a store, you '
          'use what you learned on a new road. You are not taking lessons on that trip: that is like INFERENCE. An AI '
          'model is similar. It learns during training, which happens first and takes a long time. Later it uses what '
          'it learned on new input, quickly, without changing what it learned.', [
              Q('Practicing with a driving teacher is like which stage?', 'Training',
                ('Inference', 'practice is the learning stage'), ('Neither stage', 'it matches training'),
                ('Both stages equally', 'practice is learning, not use'), 'Practice and correction are training.'),
              Q('Driving to the store with your license is like which stage?', 'Inference',
                ('Training', 'you are using what you learned'), ('Neither stage', 'it matches inference'),
                ('A driving exam', 'not the comparison made'), 'Using skills on a new road is inference.'),
              Q('Which stage usually happens first?', 'Training',
                ('Inference', 'you use skills after learning them'), ('They happen at once', 'learning comes first'),
                ('Neither happens', 'both happen'), 'Learning comes before use.'),
              Q('On the trip to the store, are you taking a lesson?', 'No, you are using what you learned',
                ('Yes, every trip is a full lesson', 'the trip is not a lesson'),
                ('Yes, the store teaches you to drive', 'the store is not a teacher'),
                ('No, because you forgot how to drive', 'you remember your skills'),
                'Using a skill is different from learning it.'),
              Q('Which stage takes a long time and many corrections?', 'Training',
                ('Inference', 'using is quick'), ('Driving to the store', 'that is use'),
                ('Getting the license card', 'not the stage described'), 'Learning takes time and correction.'),
          ], why='A learner who blends "training" and "using" can first separate them with a familiar learning-then-'
                 'doing example.')],
    F1=sec('Identify training and inference in real situations', TRAIN, [
        Q("A hospital's team spends weeks adjusting a model with thousands of past X-rays. Later, a doctor uploads a new X-ray for a second opinion. Which part is inference?",
          'The doctor uploading the new X-ray',
          ('The weeks of adjusting the model', 'that is training'), ('Collecting the thousands of past X-rays', 'that prepares training data'),
          ('Hiring the team that adjusted the model', 'not a model stage'),
          'Running the finished model on a new X-ray is inference.'),
        Q('Mia asks a translation app to translate a menu. Does her request train the app\'s model?',
          'No; translating her menu is inference',
          ('Yes; every request is a training example instantly', 'ordinary use does not change settings'),
          ('Yes; the model rewrites its settings for menus', 'not during ordinary use'),
          ('No; translation apps never use any models', 'they do use models'),
          'Using the app is inference.'),
        Q('A company says its new model "finished training in June." What does that tell you?',
          'Learning from its data ended then; later use is inference',
          ('It keeps training on every question users type', 'not implied'), ('It cannot answer any questions after June', 'it can be used after training'),
          ("It was trained by answering users' questions in June", 'not implied'),
          "Finishing training means the model's settings were fixed then."),
        Q('Which activity is training?',
          'Adjusting a model\'s settings with labeled examples',
          ('Asking a finished model for a recipe idea', 'inference'),
          ('Uploading a photo to be tagged by an app', 'inference'),
          ('Reading the reply a model already produced', 'not a model stage'),
          'Changing settings with examples is training.'),
        Q('Why is it useful to know that ordinary use does not change a model\'s settings?',
          'Correcting it in one chat will not fix the model itself',
          ('It means the model gets smarter with each question you ask', 'the opposite of what was taught'),
          ('It means the model forgets everything after each reply', 'it keeps its learned settings'),
          ('It means the model can never be updated by its makers', 'makers can train new versions'),
          'A correction in a chat affects that conversation, not the trained model.'),
    ]),
    F2=sec('Ask what actually changes when a product seems to "learn"', TRAIN_F2, [
        Q('You click "thumbs down" on a wrong answer. What is the most accurate description?',
          'It is feedback the company may use later, depending on its policy',
          ('It instantly retrains the model to fix that answer for everyone', 'feedback does not retrain instantly'),
          ('It deletes the model and replaces it with a better one at once', 'not what feedback does'),
          ('It has no possible use for anyone at all', 'companies may use feedback'),
          'Feedback may inform later training, depending on policy.'),
        Q('A chatbot remembers your name in a new conversation. What is the most likely explanation?',
          'The product stored your name and fed it back in',
          ('The model retrained itself on your name overnight', 'ordinary use does not retrain'),
          ('The model guessed your name from its training data', 'it was not in training data'),
          ('Every model is born knowing every user\'s name', 'not true'),
          'Saved information is a product feature, not a change to the model.'),
        Q('Sam wants to know whether his uploaded files could be used to train future models. What should he check?',
          'The provider\'s data policy and his account settings',
          ('Whether the chatbot sounds friendly when he asks', 'tone is not policy'),
          ('Whether the chatbot remembers his name', 'memory is not a training policy'),
          ('Nothing; uploaded files are never used by anyone', 'depends on the provider'),
          'Data use for training is set by policy and settings.'),
        Q('A user corrects a chatbot\'s wrong date and it apologizes. Later, a different user asks the same question. '
          'What should we expect?',
          'The model may make the same mistake for the other user',
          ('The model will now always give the correct date', 'one chat does not retrain the model'),
          ('The model will refuse to answer that question again', 'no reason to expect this'),
          ('The other user will see the first user\'s correction', 'conversations are separate'),
          'A correction in one conversation does not change the trained model.'),
        Q('Which change would actually alter the model\'s learned settings?',
          'The company training a new version with new data',
          ('A user typing "remember this" in a chat', 'that may store a note, not retrain'),
          ('A user rating one reply with a thumbs-up', 'feedback alone does not retrain'),
          ('A user starting a brand-new conversation', 'that changes the context, not the model'),
          'Only training changes the model\'s settings.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.02
PARAM = ('During training, a model adjusts a huge set of numbers called PARAMETERS (sometimes called weights). You can '
         'picture them as millions or billions of tiny dials. Each time the model\'s output is wrong on a training '
         'example, the dials are nudged a little so that next time the output is closer. After enough nudges, the '
         'dial settings capture PATTERNS in the data, for example which pixel shapes usually mean "cat." The model '
         'keeps the dial settings, not a neat copy of every example, although it can sometimes reproduce pieces of '
         'text or images it saw many times. More parameters can capture more patterns, but size alone does not '
         'guarantee better results.')
PARAM_F2 = ('Because learned patterns are stored as dial settings rather than as a list of facts, you usually cannot '
            'open a model and look up "the" fact it learned or delete one example\'s influence by hand. This is one '
            'reason models can mix patterns in surprising ways: an answer may blend several sources into something no '
            'single source said. It also explains why models sometimes reproduce memorized passages: text repeated '
            'very often in training can leave strong traces. Claims such as "the model just copies" or "the model '
            'never copies" are both too simple.')

S_LEARN02 = SET(
    'AI.LEARN.02',
    M=sec('Describe parameters as learned settings that capture patterns', PARAM, [
        Q('What are parameters in a model?',
          'The adjustable numbers set during training',
          ('The questions users type into the finished app', 'those are inputs'),
          ('The rules a programmer wrote out line by line', 'parameters are learned, not written'),
          ('The list of every training example, kept word for word', 'the model keeps settings, not a full copy'),
          'Parameters are numbers the training process adjusts.'),
        Q('What happens to the parameters when the model gets a training example wrong?',
          'They are nudged so the next output is closer',
          ('They are erased and started over from zero', 'they are adjusted a little'),
          ('They stay exactly the same as before', 'training changes them'),
          ('They are replaced with the example itself', 'examples are not stored that way'),
          'Small adjustments add up over many examples.'),
        Q('After training, what does a model mainly keep?',
          'Dial settings that capture patterns in the data',
          ('A tidy, searchable copy of every example it saw', 'it keeps settings, not a full copy'),
          ('Only the last example it saw during training', 'it keeps patterns from all of training'),
          ('Nothing at all; it relearns each time it is used', 'it keeps its settings'),
          'Learned patterns live in the parameter settings.'),
        Q('A model has twice as many parameters as another. Which statement is accurate?',
          'It can capture more patterns, but bigger is not always better',
          ('It is guaranteed to be twice as accurate on every task', 'size alone guarantees nothing'), ('It must have been trained on exactly half the data', 'no such rule'),
          ('It cannot be used by ordinary people at all', 'unrelated'),
          'More parameters add capacity, not a guarantee.'),
        Q('Can a model ever reproduce a piece of text it saw during training?',
          'Sometimes, especially text it saw many times',
          ('Never, because it keeps no trace of any text', 'strong traces can remain'),
          ('Always, because it stores every page exactly', 'it does not store a full copy'),
          ('Only if the user types the password for it', 'no such rule'),
          'Frequently repeated text can be reproduced.'),
    ]),
    B=[cs('Picture tuning a guitar by ear',
          'Imagine tuning a guitar by ear. You pluck a string, hear that it is a little flat, and turn the peg slightly. '
          'You pluck again and turn again, until it sounds right. You do not write down every sound you heard; what '
          'you keep is the final peg position. A model\'s PARAMETERS are like millions of pegs. Training plucks, '
          'listens and turns: each wrong output nudges the pegs a little. What the model keeps afterward is the peg '
          'settings, which capture what "sounding right" means for its task.', [
              Q('In the comparison, what are the guitar pegs like?', 'The model\'s parameters',
                ('The training examples', 'the plucked notes are more like examples'),
                ('The user\'s questions', 'not in the comparison'), ('The app\'s screen', 'not in the comparison'),
                'Pegs are adjustable settings, like parameters.'),
              Q('What do you do when a string sounds flat?',
          'Turn the peg a little and try again',
          ('Throw the guitar away', 'not how tuning works'), ('Write down the sound and keep it forever', 'you keep the setting, not the sound'),
          ('Stop playing for good', 'you adjust and retry'),
          'Small corrections, repeated, are how tuning works.'),
              Q('After tuning, what do you keep?', 'The final peg positions',
                ('A recording of every note plucked', 'not kept'), ('The broken strings', 'not in the passage'),
                ('Nothing at all', 'the positions stay set'),
                'You keep settings, not every sound.'),
              Q('Which part of training is like plucking a string and hearing it is wrong?',
          'Seeing that an output does not match an example',
          ('Typing a new question into the finished app', 'that is use, not training'), ('Buying a faster computer for the model', 'not the comparison'),
          ('Deleting the model to start over', 'not the comparison'),
          'Checking output against examples drives adjustment.'),
              Q('Why are there "millions of pegs" in a model?', 'It has very many parameters',
                ('It plays very many songs', 'not the point'), ('It has many users', 'not the point'),
                ('It runs on many computers', 'not the point'), 'Models have huge numbers of parameters.'),
          ], why='A learner unsure what "parameters" are can grasp them as adjustable settings through a hands-on '
                 'tuning example.')],
    F1=sec('Apply the idea of parameters to claims about models', PARAM, [
        Q('A news article says a model "contains every book it read." What is more accurate?',
          'It holds learned settings, not a complete copy of every book',
          ('It is accurate; models are libraries of full texts', 'models keep settings, not full copies'),
          ('It is accurate; parameters are the books themselves', 'parameters are numbers'),
          ('Models never learn anything from books at all', 'text is common training data'),
          'Parameters capture patterns, not full copies, though fragments can be reproduced.'),
        Q('Two models: one has 1 billion parameters, the other 10 billion. Which conclusion is justified without testing?',
          'The larger has more capacity; testing shows which works better',
          ('The larger one is exactly ten times more accurate on every task', 'size does not set accuracy'), ('The smaller one must be useless for every task', 'not justified'),
          ('Both must give identical answers', 'not justified'),
          'Capacity is not the same as tested performance.'),
        Q('A model was trained to recognize cats. What did training adjust?',
          'Its parameters, so pixel patterns map to "cat"',
          ('A written rule list describing every cat breed', 'it learned rather than followed rules'),
          ('The photos themselves, so they look more like cats', 'training changes the model, not photos'),
          ('The user\'s camera settings', 'unrelated'),
          'Training set the parameters to capture cat patterns.'),
        Q('Why might a model repeat a famous quotation word for word?',
          'Text seen many times in training can leave strong traces',
          ('It looks the quotation up in a stored copy of the internet', 'a model is not a stored copy'),
          ('Models are designed to repeat everything word for word', 'they usually do not'),
          ('The quotation is one of its parameters', 'parameters are numbers'),
          'Frequent repetition in training can cause memorization.'),
        Q('Which description of training is most accurate?',
          'Many small adjustments to settings, based on errors',
          ('One big change made after all examples are seen', 'it adjusts many times'),
          ('Typing in facts one at a time into a database', 'not how training works'),
          ('Copying the examples into the model\'s memory', 'it learns patterns instead'),
          'Training repeats small, error-driven nudges.'),
    ]),
    F2=sec('Avoid oversimplified claims about what a model stores', PARAM_F2, [
        Q('A user asks a company to "delete the fact about me from the model." Why is this hard?',
          'Learned patterns are spread across settings, not stored as one fact',
          ('Models store each fact in a labeled folder that is locked', 'not how models store patterns'),
          ('It is easy; any user can delete one parameter', 'not practical'),
          ('Models never learn anything about people', 'they can learn from text about people'),
          'Influence is spread across many parameters.'),
        Q("A model's answer blends ideas so that no single source said exactly that. What explains this?",
          'It combines learned patterns from many examples',
          ('It always copies one source exactly', 'it often blends'), ('It searched one website and pasted it', 'not implied'),
          ('It has a written rule never to use any real sources', 'no such rule'),
          'Blending patterns can create statements no source made.'),
        Q('Someone says, "Models never copy anything, so there is no copyright issue." What is wrong?',
          'Models can sometimes reproduce passages they saw many times',
          ('Nothing; models are proven never to copy at all', 'they sometimes reproduce text'),
          ('Models only copy images, never text', 'not accurate'),
          ('Copying is impossible because parameters are numbers', 'numbers can still encode strong traces'),
          '"Never copies" is too simple.'),
        Q('Someone says, "Models just copy and paste their training data." What is wrong?',
          'Mostly they produce new combinations from patterns',
          ('Nothing; every output is an exact copy of a source', 'most outputs are new combinations'), ('Models cannot produce any text at all', 'they can'),
          ('Models only copy text from the user', 'not accurate'),
          '"Just copies" is also too simple.'),
        Q('Why can\'t you open a model and read "the fact" it learned about the moon?',
          'It is spread across many numbers, not stored as sentences',
          ('Models refuse to discuss the moon', 'unrelated'), ('The fact is locked away inside it with a secret password', 'not the reason'),
          ('Models never learn about the moon', 'they can learn patterns about it'),
          'Parameters are numbers, not readable sentences.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.03
SPLIT = ('Builders usually split their data into three parts. The TRAINING SET is what the model learns from. The '
         'VALIDATION SET is used during development to compare versions and settings, like practice quizzes. The TEST '
         'SET is kept aside and used only at the end to measure how well the finished model does on examples it has '
         'never seen. If test examples leak into training, the test score looks better than the model really is, '
         'because the model may have learned those exact answers. A trustworthy result comes from examples that '
         'stayed unseen.')
SPLIT_F2 = ('Keeping test data truly separate is harder than it sounds. Copies of the same item can appear twice, for '
            'example the same photo cropped slightly, or the same news story on two websites, so one copy lands in '
            'training and another in the test. Reusing the test set again and again to choose between versions also '
            'wears it out: the team slowly tunes the model to that particular test. And a test set that does not look '
            'like real use, such as clear studio photos when users will upload blurry phone pictures, gives a score '
            'that does not predict real performance.')

S_LEARN03 = SET(
    'AI.LEARN.03',
    M=sec('Explain training, validation and test data', SPLIT, [
        Q('What is the training set used for?',
          'The examples the model learns from',
          ('The final check', 'that is the test set'), ('Comparing versions during development', 'that is the validation set'),
          ('Advertising the model to customers', 'not a data split'),
          'The model learns from the training set.'),
        Q('What is the test set used for?',
          'Measuring the finished model on unseen examples',
          ('Teaching the model its main patterns', 'that is training'), ("Storing users' questions after the app launches", 'not a data split'),
          ('Tuning settings during development', 'that is validation'),
          'The test set gives a final, honest measurement.'),
        Q('Which set is most like practice quizzes during development?', 'The validation set',
          ('The test set', 'the test is the final exam'), ('The training set', 'that is the study material'),
          ('None of the sets', 'validation matches practice quizzes'),
          'Validation helps choose versions and settings.'),
        Q('Why must test examples stay out of training?',
          'Otherwise the test score can overstate real performance',
          ('Otherwise the model will refuse to work on any input at all', 'not the reason'), ('Otherwise the training will finish too quickly', 'not the reason'),
          ('Otherwise the model gets too many parameters', 'unrelated'),
          'Seen examples inflate scores.'),
        Q('A model scores 99 percent, but later it is found that test examples were also in training. What should you conclude?',
          'The 99 percent may overstate how it handles new examples',
          ('The 99 percent is now even more trustworthy than before', 'leakage makes it less trustworthy'), ('The model must be useless for everything', 'it may still work, but the score misleads'),
          ('Nothing; leaks never affect scores', 'leaks can inflate scores'),
          'Leakage makes a score look better than real performance.'),
    ]),
    B=[cs('Compare studying, practice quizzes and a final exam',
          'A student preparing for a final exam studies from a TEXTBOOK, takes PRACTICE QUIZZES to see what still needs '
          'work, and then takes the FINAL EXAM. The exam is useful only if its questions are new. If the student saw '
          'the exact exam questions in advance, a high score would show memory, not real understanding. Model data '
          'works the same way: the training set is the textbook, the validation set is the practice quizzes, and the '
          'test set is the final exam that must stay secret until the end.', [
              Q('The textbook is like which data set?', 'The training set',
                ('The test set', 'that is the final exam'), ('The validation set', 'those are practice quizzes'),
                ('No data set', 'it matches training'), 'The model learns from the training set.'),
              Q('The final exam is like which data set?', 'The test set',
                ('The training set', 'that is the textbook'), ('The validation set', 'those are quizzes'),
                ('All three sets', 'it matches the test set'), 'The test set is the final check.'),
              Q('Why must the final exam questions stay secret?',
          'So a high score shows understanding',
          ('So the exam is harder to print', 'not the reason'), ('So the teacher can grade all the exams faster', 'not the reason'),
          ('So the textbook is not needed', 'not the reason'),
          'Unseen questions give an honest measure.'),
              Q('What do practice quizzes help the student do?',
          'See what still needs work',
          ('Get the final grade early', 'they are practice'), ('Skip the textbook', 'not their purpose'),
          ('Memorize the final exam questions early', 'the exam stays secret'),
          'Quizzes guide preparation.'),
              Q('A student saw the exact exam in advance and scored 100. What does the score mostly show?',
                'Memory of those questions',
                ('Deep understanding of everything', 'not shown'), ('Nothing at all', 'it shows memory'),
                ('That the exam was too easy', 'not the main issue'), 'Seen questions measure memory.'),
          ], why='A learner who cannot keep the three data sets apart can map them onto a familiar study routine.')],
    F1=sec('Apply data splits to real projects', SPLIT, [
        Q('A team building a dog-breed recognizer has 10,000 labeled photos. Which plan follows good practice?',
          'Train on most, use some for validation, keep a test portion unseen',
          ('Train and test on the same 10,000 photos', 'testing on training data inflates scores'),
          ('Skip testing because 10,000 is already enough', 'testing is still needed'),
          ('Test first, then add the test photos into training and report that score', 'the reported score would be inflated'),
          'Separate splits give an honest final measure.'),
        Q('During development, a team compares three versions and picks the best. Which data should they use to '
          'compare?',
          'The validation set',
          ('The test set, again and again', 'the test set is for the final check'),
          ('The training set only', 'scores there are too optimistic'),
          ('No data; they should guess', 'data is needed'),
          'Validation data is for comparing versions.'),
        Q('A student project reports "100 percent accuracy," measured on the same examples it trained on. What is the '
          'problem?',
          'The score does not show how it handles new examples',
          ('There is no problem; 100 percent is always trustworthy', 'it was measured on seen data'),
          ('Training data cannot be used for anything at all', 'it is used to learn'),
          ('Accuracy cannot be measured for student projects', 'it can'),
          'Only unseen examples show real performance.'),
        Q('When should the test set be used?',
          'At the end, to measure the finished model',
          ('At the start, to teach the model', 'that is training'), ('Every day, to choose settings', 'that wears it out; use validation'),
          ('Never, because final tests are always optional', 'testing is essential'),
          'The test set is a final, one-time-style check.'),
        Q('A company says its spam filter is "98 percent accurate on our test set." What question checks whether the '
          'number is trustworthy?',
          'Were the test emails kept out of training?',
          ('Is the number written in a large font?', 'presentation is not evidence'),
          ('Is 98 a bigger number than last year\'s?', 'does not check leakage'),
          ('Does the filter have a friendly name?', 'irrelevant'),
          'An honest test score needs unseen test data.'),
    ]),
    F2=sec('Spot hidden problems with test data', SPLIT_F2, [
        Q('The same news story appears on two websites. One copy is in training, the other in the test set. What is the risk?',
          'The test includes something the model has already seen',
          ('None, because the websites have different names', 'the content is the same'), ('The model will refuse to read news', 'not the risk'),
          ('The test becomes harder than real use', 'it becomes easier, not harder'),
          'Near-duplicates can leak test content into training.'),
        Q('A team checks its test score after every small change for months. What problem can this cause?',
          'The team slowly tunes the model to that one test',
          ('The test questions physically wear out from use', 'not literally'), ('The model forgets its training data', 'not the problem'),
          ('Nothing; checking often always helps', 'reusing the test set wears it out'),
          'Overusing the test set makes it less honest.'),
        Q('A plant-identification app was tested on clear studio photos, but users upload blurry phone pictures. What '
          'should the team conclude?',
          'The test score may not predict real-world performance',
          ('The app will work even better on blurry photos', 'unsupported'),
          ('Blurry photos cannot be identified by anyone', 'too extreme'),
          ('The test score proves the app works for everyone', 'the test did not match real use'),
          'A test set should resemble real use.'),
        Q('Photos of the same dog, cropped slightly differently, end up in both training and test sets. What should '
          'the team do?',
          'Remove near-duplicates so test items are truly unseen',
          ('Keep them, because cropping makes them different', 'they are near-copies'),
          ('Delete the whole test set and skip testing', 'testing is still needed'),
          ('Add more copies to make the test fairer', 'adds more leakage'),
          'Near-duplicates should be kept on one side only.'),
        Q("Which test plan best predicts real performance for a store's receipt scanner?",
          'Unseen receipts like the ones customers really scan',
          ('Receipts the scanner was trained on', 'seen data'), ('Perfect, printed sample receipts from the factory only', 'not like real use'),
          ('One receipt scanned 100 times', 'too narrow'),
          'Unseen, realistic test data gives a useful score.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.04
OVER = ('A model GENERALIZES when it does well on new examples, not just the ones it trained on. OVERFITTING is the '
        'opposite: the model fits its training examples so closely, including their accidents and noise, that it does '
        'worse on new ones. A sign of overfitting is a big gap: very high accuracy on training data but much lower '
        'accuracy on validation or test data. For example, a model that learned "all photos of wolves have snow" '
        'might label a husky in snow as a wolf. Remedies include more varied data, simpler models and stopping '
        'training before it memorizes.')
OVER_F2 = ('Overfitting is not the only way a model can disappoint. A model can also UNDERFIT: it is too simple or '
           'trained too little, so it does poorly even on its training data. And a model can generalize well to data '
           'like its training data but still fail when the situation changes, for example a new camera, a new slang '
           'word or a new kind of fraud. So compare training and validation results first: a big gap suggests '
           'overfitting; low scores on both suggest underfitting; good scores followed by a drop after launch '
           'suggest the world has changed.')

S_LEARN04 = SET(
    'AI.LEARN.04',
    M=sec('Recognize overfitting and good generalization', OVER, [
        Q('What does it mean for a model to generalize well?',
          'It does well on new examples, not just training ones',
          ('It memorizes every one of its training examples exactly', 'that can be overfitting'), ('It works only on the examples it trained on', 'that is the opposite'),
          ('It has as many parameters as possible', 'size is not generalization'),
          'Generalizing means handling new examples well.'),
        Q('Which result is a warning sign of overfitting?',
          '99 percent on training data but 70 percent on test data',
          ('85 percent on training data and 84 percent on test data', 'a small gap'),
          ('50 percent on training data and 50 percent on test data', 'low on both suggests something else'),
          ('A model that has not been trained yet', 'not overfitting'),
          'A large training-to-test gap suggests overfitting.'),
        Q('A model learned that wolf photos have snow and calls a husky in snow a wolf. What happened?',
          'It overfit to an accidental pattern in its photos',
          ('It generalized perfectly from good data', 'it learned the wrong cue'), ('It was never trained on any photos of animals at all', 'it was trained'),
          ('Huskies and wolves are the same animal', 'they are different'),
          'Learning an accident of the data (snow) is overfitting.'),
        Q('Which change could reduce overfitting?',
          'Training with more varied examples',
          ('Training much longer', 'can make overfitting worse'), ('Testing on the training data instead', 'hides the problem'),
          ('Removing the validation set', 'hides the problem'),
          'Varied data helps a model learn the real pattern.'),
        Q('Why is overfitting a problem in practice?',
          'The model performs worse on new, real cases',
          ('The model becomes too fast to measure', 'not the problem'),
          ('The model refuses to accept any input', 'not the problem'),
          ('The training data is deleted automatically', 'not the problem'),
          'Real use means new examples.'),
    ]),
    B=[cs('Compare memorizing answers with understanding the method',
          'Two students prepare for a math test. One MEMORIZES the answers to the 20 practice problems: "Problem 4 is '
          '17." The other learns the METHOD for solving them. On the practice sheet, both score perfectly. On the real '
          'test, with new numbers, the memorizer is lost while the method-learner does fine. The memorizer has '
          'overfit to the practice sheet. The method-learner generalized. A model can do the same: perfect on the '
          'examples it trained on, poor on new ones.', [
              Q('Which student overfit?',
          'The one who memorized the practice answers',
          ('The one who learned the method for solving them', 'that student generalized'), ('Both students', 'only one did'),
          ('Neither student', 'the memorizer did'),
          'Memorizing specific answers is overfitting.'),
              Q('Why did both students score perfectly on the practice sheet?',
                'Both could answer those exact problems',
                ('The practice sheet had no problems', 'it had 20'), ('The teacher gave everyone full marks', 'not stated'),
                ('Both learned the method', 'only one did'),
                'Familiar examples do not separate memorizing from understanding.'),
              Q('What happened on the real test with new numbers?',
          'The memorizer struggled; the other did fine',
          ('Both did equally well', 'they differed'), ('Both failed', 'the method-learner succeeded'),
          ('The memorizer did better than the method-learner', 'the reverse'),
          'New examples reveal overfitting.'),
              Q('Which student is like a model that generalizes?',
          'The method-learner',
          ('The memorizing student', 'overfit'), ('Neither', 'the method-learner generalizes'),
          ('Both', 'only one generalizes'),
          'Generalizing means handling new problems.'),
              Q('What kind of test reveals overfitting?', 'A test with new examples',
                ('The same practice sheet again', 'familiar examples hide it'),
                ('A test with no questions', 'not meaningful'), ('A test the student writes', 'not the point'),
                'Only unseen examples show the difference.'),
          ], why='A learner who cannot see why perfect training scores can mislead is helped by the memorize-versus-'
                 'method contrast.')],
    F1=sec('Diagnose overfitting from results', OVER, [
        Q('A model scores 98 percent on training data and 96 percent on validation data. What is the best reading?',
          'It appears to generalize well',
          ('It is badly overfit', 'the gap is small'),
          ('It has not learned anything', 'scores are high'),
          ('The validation data must have leaked', 'no evidence'),
          'A small gap with high scores suggests good generalization.'),
        Q('A team\'s model gets 100 percent in training but 60 percent in validation. What should they try?',
          'More varied data or a simpler model',
          ('Report the 100 percent as its accuracy', 'misleading'),
          ('Train longer on the same data', 'may worsen overfitting'),
          ('Stop using any validation data', 'hides the problem'),
          'Address the gap with variety or simplicity.'),
        Q('A spam filter learned that every email containing "meeting" is safe, because all its safe training emails '
          'had that word. What could go wrong?',
          'Spam containing "meeting" will slip through',
          ('Nothing; the word "meeting" proves safety', 'an accidental pattern'),
          ('Safe emails will all be blocked', 'the opposite risk'),
          ('The filter will stop reading emails', 'not implied'),
          'Overfitting to an accidental cue causes errors on new cases.'),
        Q('Which report best shows a model generalizes?',
          'Strong results on new examples it never saw',
          ('Perfect results on its own training examples', 'not enough'),
          ('A very large number of parameters', 'size is not evidence'),
          ('A long training time', 'time is not evidence'),
          'Generalization is measured on unseen examples.'),
        Q('A photo model always calls cows "horses" when they stand on sand, because training horses were on beaches. What is the fix?',
          'Train with animals photographed in varied settings',
          ('Show only beach photos from now on', 'reinforces the bad cue'), ('Remove all cow photos from the test', 'hides the problem'),
          ("Increase the model's confidence scores for cows", 'does not fix learning'),
          'Varied backgrounds break the accidental pattern.'),
    ]),
    F2=sec('Tell overfitting from underfitting and a changed world', OVER_F2, [
        Q('A model scores 55 percent on training data and 54 percent on validation data for a task where 90 percent is '
          'expected. What is the most likely issue?',
          'Underfitting: it has not learned the task well',
          ('Overfitting: training is far higher than validation', 'they are nearly equal'),
          ('The world changed after launch', 'it has not launched'),
          ('It is working perfectly', 'scores are far below expectations'),
          'Low scores on both suggest underfitting.'),
        Q('A fraud model tested well, but months after launch it misses a new kind of scam. What best explains this?',
          'The situation changed in ways its training data did not cover',
          ('It overfit, since training was far above validation', 'it tested well on unseen data'),
          ('It underfit, since it never learned anything', 'it tested well'),
          ('Fraud can never be detected by models', 'too extreme'),
          'A changed world can break a model that generalized well before.'),
        Q('Which result pattern suggests overfitting?',
          'High training score, much lower validation score',
          ('Low training score, low validation score', 'underfitting'),
          ('High scores on both, then a drop after launch', 'a changed world'),
          ('High scores on both with a small gap', 'good generalization'),
          'A big gap is the overfitting signature.'),
        Q("A speech model trained on recordings from one microphone does poorly with a new phone model's microphone. What should the team check first?",
          "Whether the new microphone's audio differs from training data",
          ('Whether the model has too few parameters to handle speech', 'not the first check'), ('Whether users are speaking too politely', 'unlikely'),
          ('Whether the old test score was rounded', 'irrelevant'),
          'New conditions can differ from training conditions.'),
        Q('A team sees a big training-validation gap and wants to add many more parameters. What is the concern?',
          'A bigger model might memorize more and overfit worse',
          ('More parameters always fix overfitting', 'not necessarily'), ('Parameters cannot be added to models', 'they can'),
          ('Validation scores will no longer be measured at all', 'unrelated'),
          'Added capacity can increase memorization.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.05
QUAL = ('A model can only learn what its data shows it, so DATA QUALITY matters as much as the model itself. Common '
        'problems: MISSING data (some cases never appear), WRONG LABELS (a cat photo labeled "dog"), OUTDATED data '
        '(prices from five years ago), and UNREPRESENTATIVE data (photos only from one country, voices only from adults). '
        'A LABEL is the correct answer attached to a training example, often added by people, and people make mistakes '
        'or disagree. Problems in the data become problems in the model, which is often summed up as "garbage in, '
        'garbage out."')
QUAL_F2 = ('Fixing data problems takes judgment. Some labels are hard because people genuinely disagree: is a review '
           'that says "not bad" positive or neutral? Writing clear labeling instructions and checking a sample of '
           'labels helps. Collecting more data does not help if the new data has the same gaps. And removing a column '
           'such as age does not always remove its influence, because other data can stand in for it. Good teams '
           'document where their data came from, what it leaves out and how labels were checked.')

S_LEARN05 = SET(
    'AI.LEARN.05',
    M=sec('Explain how data quality and labels shape a model', QUAL, [
        Q('A model was trained on product prices from five years ago. Which data problem is this?', 'Outdated data',
          ('Wrong labels', 'nothing says labels are wrong'), ('Missing data', 'the data exists but is old'),
          ('Too many parameters', 'not a data problem'), 'Old prices are outdated data.'),
        Q('Many cat photos in a training set are labeled "dog." What will most likely happen?',
          'The model may confuse cats and dogs',
          ('The model will recognize cats perfectly anyway', 'wrong labels teach wrong answers'),
          ('The model will refuse to train at all', 'not likely'),
          ('Nothing; labels have no effect on learning', 'labels are what it learns from'),
          'Wrong labels teach wrong answers.'),
        Q('A voice assistant was trained only on adult voices. What problem may appear?',
          'It may understand children poorly',
          ('It will understand children better', 'unsupported'), ('It will refuse to hear adult voices', 'it was trained on them'),
          ('It will have no problems at all', 'unrepresentative data causes gaps'),
          'Unrepresentative data leads to weak performance on missing groups.'),
        Q('What is a label in training data?',
          'The correct answer attached to an example',
          ('The brand name printed on the computer', 'not a data label'),
          ('The title of the finished app', 'not a data label'),
          ('A sticker on the user\'s phone', 'not a data label'),
          'Labels tell the model the answer it should learn.'),
        Q('What does "garbage in, garbage out" mean for AI?',
          'Problems in the data become problems in the model',
          ('Models clean up any bad data automatically', 'they learn whatever the data shows'),
          ('Bad data always makes a model refuse to work', 'it often still works, badly'),
          ('Only the model\'s size affects its quality', 'data quality matters too'),
          'A model inherits its data\'s flaws.'),
    ]),
    B=[cs('Compare learning from a flawed map',
          'Imagine learning a city from a MAP. If the map is missing a neighborhood, you will never know it exists. If '
          'a street is labeled with the wrong name, you will confidently give wrong directions. If the map is twenty '
          'years old, you may send people to a store that closed long ago. If the map shows only the downtown, you '
          'will be lost in the suburbs. A model learns from its data the way you learn from the map: whatever is '
          'missing, wrong, old or one-sided in the data shows up in the model.', [
              Q('A map missing a neighborhood is like which data problem?', 'Missing data',
                ('Wrong labels', 'that is a misnamed street'), ('Outdated data', 'that is an old map'),
                ('Unrepresentative data', 'that is a downtown-only map'), 'Absent areas are missing data.'),
              Q('A street with the wrong name is like which data problem?', 'Wrong labels',
                ('Missing data', 'the street is there'), ('Outdated data', 'the name is simply wrong'),
                ('Unrepresentative data', 'not about coverage'), 'A wrong name is a wrong label.'),
              Q('A twenty-year-old map is like which data problem?', 'Outdated data',
                ('Wrong labels', 'labels may have been right then'), ('Missing data', 'not the main issue'),
                ('Too many streets', 'not a data problem'), 'Old information is outdated data.'),
              Q('A map showing only downtown is like which data problem?',
          'Unrepresentative data',
          ('Wrong labels', 'the labels may be right'), ('Outdated data from long ago', 'it may be current'),
          ('Perfect data', 'it leaves out the suburbs'),
          'Covering only one part is unrepresentative.'),
              Q('Why would you give wrong directions confidently with a flawed map?',
          'You trust what the map shows you',
          ('Maps always tell you', 'they do not'), ('You never look at the map', 'you learned from it'),
          ('Directions cannot be wrong', 'they can'),
          'Learned flaws feel like facts.'),
          ], why='A learner who cannot name data problems can sort them using a familiar flawed-map example.')],
    F1=sec('Identify data problems in real projects', QUAL, [
        Q('A skin-condition app was trained mostly on photos of light skin. What risk should its makers check?',
          'Weaker accuracy on darker skin',
          ('Too many correct answers on light skin', 'not a risk'),
          ('The app running too fast on phones', 'unrelated'),
          ('Users taking photos in good lighting', 'unrelated'),
          'Unrepresentative data can cause uneven accuracy.'),
        Q('Volunteers labeled 10,000 tweets as "angry" or "calm" in a rush and made many mistakes. What is the effect?',
          'The model learns some wrong associations',
          ('The model ignores labels and learns correctly', 'labels guide learning'),
          ('The model will be perfect because 10,000 is many', 'quantity does not fix wrong labels'),
          ('Nothing; rushed labels are always fine', 'mistakes matter'),
          'Label errors become model errors.'),
        Q('A rent-prediction model uses listings from 2019 to predict rents today. Which problem is most likely?',
          'Outdated data that misses recent price changes',
          ('Wrong labels on every listing', 'not stated'), ('Too much data from today', 'the opposite'),
          ('Perfect predictions because the data is old', 'unsupported'),
          'Old data can miss changes.'),
        Q('A traffic model never saw data from snowy days. What could happen on the first snowy day?',
          'Its predictions may be badly wrong',
          ('Its predictions will be most accurate in snow', 'unsupported'),
          ('It will forecast snow by itself', 'not its job'),
          ('Nothing will change at all', 'missing cases cause errors'),
          'Missing data leaves the model unprepared.'),
        Q('Which step best improves the quality of a training set?',
          'Checking a sample of labels for mistakes',
          ('Making the file names shorter', 'cosmetic'), ('Using only the newest computer', 'not about data quality'),
          ('Hiding where all of the data came from', 'documentation helps quality'),
          'Checking labels catches errors.'),
    ]),
    F2=sec('Handle hard data and labeling decisions', QUAL_F2, [
        Q('Labelers disagree whether "not bad" is positive or neutral. What is the best step?',
          'Write clear labeling instructions and check a sample',
          ('Let each labeler decide freely with no guidance', 'causes inconsistent labels'),
          ('Delete every review that is hard to label', 'loses real cases'),
          ('Label every review "positive" to be safe', 'creates wrong labels'),
          'Clear instructions and checks make labels consistent.'),
        Q('A team adds 50,000 more photos, but all from the same city as before. Why might this not help?',
          'The new data has the same gaps as the old data',
          ('More data always fixes every problem', 'not if gaps repeat'),
          ('Photos from one city cannot be used at all', 'they can, but coverage stays narrow'),
          ('The model will forget the old photos', 'not the issue'),
          'More of the same does not fill gaps.'),
        Q('A loan model has no "age" column, but it uses "years since first credit card." Why might age still affect '
          'it?',
          'Other data can stand in for the removed column',
          ('Removing a column always removes its influence', 'not always'),
          ('Credit cards have nothing to do with age', 'they often relate'),
          ('Models cannot use numbers about time', 'they can'),
          'A related column can act as a stand-in.'),
        Q('Why should a team document where its data came from and what it leaves out?',
          'So others can judge where the model may fail',
          ('So the data file looks longer', 'not the reason'), ('So the model trains faster', 'documentation does not speed training'),
          ('So that no one asks any questions about it', 'the opposite'),
          'Documentation reveals limits.'),
        Q('A new labeling team is much faster but less careful. What should the project do?',
          'Check a sample of their labels before trusting them',
          ('Trust them, because working fast shows real skill', 'speed is not accuracy'), ('Stop labeling data forever', 'too extreme'),
          ('Hide their labels from the model', 'avoids rather than checks'),
          'Spot checks reveal label quality.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.08
FT = ('There are two very different ways to make a model handle your needs. FINE-TUNING is more training: a model that '
      'already exists is trained further on new examples, which changes its parameters. It takes data, time and '
      'skill, and the change lasts for every later use of that tuned version. SUPPLYING INFORMATION IN THE REQUEST '
      'means putting what the model needs, such as a policy document, a list of rules or a few examples, into your '
      'message or an attached file. That does not change the model; it only affects that request (and that '
      'conversation, while the text stays in context).')
FT_F2 = ('Choosing between the two depends on the job. For facts that change often, like this week\'s prices or a '
         'policy updated monthly, supplying current information in the request is usually easier to keep up to date. '
         'Fine-tuning suits teaching a lasting style or format across many uses, or a specialized task with lots of '
         'examples. Fine-tuning is NOT a reliable way to make a model "know" a long list of changing facts, and it can '
         'introduce new mistakes. Either way, results need testing, and private data used for fine-tuning needs the '
         'same care as any other data sharing.')

S_LEARN08 = SET(
    'AI.LEARN.08',
    M=sec('Tell fine-tuning from supplying information in a request', FT, [
        Q('A company trains an existing model further on 20,000 of its own support chats. What is this?',
          'Fine-tuning, which changes the model',
          ('Supplying information in a request', 'it is additional training'),
          ('Inference on 20,000 new questions', 'it is training'),
          ('Deleting the model\'s parameters', 'the parameters are adjusted, not deleted'),
          'Training further on new examples is fine-tuning.'),
        Q('Leo pastes his school\'s rules into his message and asks a question about them. What happens to the model?',
          'Nothing changes; the rules affect only this request',
          ('It is fine-tuned on the school rules forever', 'pasting text does not retrain'),
          ('It permanently forgets other schools\' rules', 'nothing is deleted'),
          ('It shares the rules with every other user', 'not how requests work'),
          'Supplied information affects the request, not the model.'),
        Q('Which approach changes the model\'s parameters?', 'Fine-tuning',
          ('Attaching a file to one message', 'does not change parameters'),
          ('Typing a longer, clearer question', 'does not change parameters'),
          ('Adding three examples to a request', 'does not change parameters'),
          'Only further training changes parameters.'),
        Q('What does fine-tuning usually require?',
          'Example data, time and some skill',
          ('Only one sentence typed into a chat', 'that is a request'), ('Nothing; it happens automatically', 'it is deliberate training'),
          ('Deleting the original model first', 'it starts from the existing model'),
          'Fine-tuning is a training project.'),
        Q("How long does information supplied in a request affect the model's answers?",
          'Only while it is in that request or conversation',
          ('Forever, for every user of the model everywhere', 'it does not change the model'), ('Exactly one week, then it expires', 'no such rule'),
          ('Until the company retrains the model', 'it never entered the model'),
          'Supplied text acts through the context, not training.'),
    ]),
    B=[cs('Compare a training course with a note on the desk',
          'A new employee can learn about a company in two ways. She can attend a TRAINING COURSE for weeks, and what '
          'she learns stays with her afterward. Or her manager can leave a NOTE on her desk: "Today the store closes '
          'at 6." The note helps today, but it does not change her training, and tomorrow there may be a different '
          'note. Fine-tuning is like the training course: it changes the model. Putting information in a request is '
          'like the note: it helps with that task and changes nothing permanent.', [
              Q('Fine-tuning is like which option?',
          'The weeks-long training course',
          ('The note left on the desk', 'that is supplying information'), ('Neither option', 'it matches the course'),
          ('Both options', 'only the course changes her'),
          'Further training changes the learner.'),
              Q('Pasting information into a request is like which option?', 'The note on the desk',
                ('The training course', 'that is fine-tuning'), ('Hiring a new employee', 'not the comparison'),
                ('Closing the store', 'not the comparison'), 'A note helps the current task.'),
              Q('Does the note change what the employee learned in training?',
          'No, it only helps today',
          ('Yes', 'a note is temporary'), ('Yes, it replaces the course', 'it does not'),
          ('No, because she cannot read', 'not the point'),
          'Notes do not change training.'),
              Q('Which lasts after the task is done?',
          'What she learned in the course',
          ("The note's message", 'it was for today'), ('Neither', 'the course lasts'),
          ('Only the store hours in the note', 'those change'),
          'Training lasts; notes are temporary.'),
              Q('Tomorrow the store closes at 8. What is the easiest way to tell her?', 'Leave a new note',
                ('Send her back to a weeks-long course', 'too slow for a changing fact'),
                ('Hire a different employee', 'unnecessary'), ('Tell no one', 'she needs to know'),
                'Changing facts are easiest to supply as notes.'),
          ], why='A learner who thinks attaching a document retrains a model can separate the two with a training-'
                 'course-versus-note example.')],
    F1=sec('Choose between fine-tuning and supplying information', FT, [
        Q('A small shop wants answers about its return policy, which it updates often. Which approach is simplest to '
          'keep current?',
          'Supply the current policy in each request',
          ('Fine-tune a model every time the policy changes', 'slow and costly'),
          ('Hope the model already knows the shop\'s policy', 'it likely does not'),
          ('Fine-tune once and never update it', 'it will go out of date'),
          'Supplying current text is easy to update.'),
        Q('Tia attached a recipe file and asked for a shopping list. Did the model learn her recipe permanently?',
          'No; the file was used only for that request',
          ('Yes; attaching a file fine-tunes the model', 'attaching does not retrain'),
          ('Yes; all users can now see her recipe', 'not how it works'),
          ('No; models cannot read attached files', 'many products can'),
          'An attachment adds context, not training.'),
        Q('A law firm wants a model to always write in its strict house format across thousands of documents. Which '
          'approach might suit it?',
          'Fine-tuning on many examples of that format',
          ('Typing "use our format" once and assuming it lasts forever', 'requests do not persist in the model'),
          ('Never giving any examples', 'examples are needed'),
          ('Asking a different model each time', 'inconsistent'),
          'A lasting style across many uses can suit fine-tuning, with testing.'),
        Q('Which statement about fine-tuning is accurate?',
          'It changes the model for later uses of that version',
          ('It changes only the current message', 'that is supplying information'), ('It happens whenever a user says "learn this"', 'it is deliberate training'),
          ('It needs no data at all', 'it needs examples'),
          'Fine-tuning creates a changed version.'),
        Q('A teacher wants a model to answer questions about this week\'s homework sheet. What is the easiest approach?',
          'Include the homework sheet in the request',
          ('Fine-tune a model on the sheet', 'too much effort for one week'),
          ('Expect the model to know the sheet already', 'it has never seen it'),
          ('Ask the model to guess the sheet', 'unreliable'),
          'Supply the sheet directly.'),
    ]),
    F2=sec('Decide when fine-tuning is the wrong tool', FT_F2, [
        Q('A store wants a model to know its 2,000 prices, which change weekly. Why is fine-tuning a poor fit?',
          'Prices change weekly; fine-tuning suits that poorly',
          ('Fine-tuning cannot use numbers at all', 'it can'), ('Prices are illegal to share with any AI model', 'not generally'),
          ('Fine-tuning works only for images', 'not true'),
          'Changing facts are better supplied from a current source.'),
        Q('After fine-tuning, a model starts making errors it did not make before. What does this show?',
          'Fine-tuning can add new mistakes, so test the result',
          ('Fine-tuning always makes every answer better', 'not guaranteed'), ('The original model was deleted by accident', 'not implied'),
          ('Errors cannot happen after fine-tuning', 'they can'),
          'Any changed version needs testing.'),
        Q('A team wants to fine-tune on customer emails that include home addresses. What should they consider first?',
          'Whether they may use that private data, and how to protect it',
          ('Nothing; private data is fine to use for any kind of training', 'requires care and permission'), ('Only how fast the training will finish', 'privacy comes first'),
          ('Whether the emails are long enough', 'not the main concern'),
          'Fine-tuning data needs the same care as any data sharing.'),
        Q('Which task is the best fit for supplying information in the request rather than fine-tuning?',
          'Answering questions about this month\'s updated policy',
          ('Teaching a lasting writing style used across all documents', 'could suit fine-tuning'),
          ('Training a model on a large specialized task', 'fine-tuning may suit'),
          ('Creating a new version for long-term use', 'fine-tuning'),
          'Current, changing information is easiest to supply.'),
        Q('A manager says, "We fine-tuned it, so we no longer need to check its answers." What is wrong?',
          'Tuned models still make mistakes and need testing',
          ('Nothing; fine-tuned models are always correct', 'not true'),
          ('Fine-tuning deletes the ability to check', 'nonsense'),
          ('Checking is only for models that were never tuned', 'all models need checking'),
          'Testing is needed either way.'),
    ]),
)

SETS = [S_LEARN01, S_LEARN02, S_LEARN03, S_LEARN04, S_LEARN05, S_LEARN08]
