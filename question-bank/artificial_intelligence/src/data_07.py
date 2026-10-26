"""Specialty: a closer look inside (AI.LEARN.06, AI.LEARN.07, AI.LLM.08)."""
from eq import Q, SET, sec, cs, sk, PR, CODE, TABLE, TEXT  # noqa: F401

# ---------------------------------------------------------------------------------------------- AI.LEARN.06
KIND = ('Models learn from different kinds of SIGNALS. In SUPERVISED learning, each training example comes with a '
        'label, the right answer: photos marked "cat" or "dog," emails marked "spam" or "not spam." In UNSUPERVISED '
        'learning, there are no labels; the model looks for structure on its own, such as grouping customers with '
        'similar shopping habits. In SELF-SUPERVISED learning, the data supplies its own answers: hide a word in a '
        'sentence and train the model to predict it. Large language models are mostly trained this way, because huge '
        'amounts of text need no hand-made labels.')
KIND_F2 = ('Real systems often combine these. A language model might first learn by self-supervision on huge amounts '
           'of text, then be adjusted with a smaller set of labeled, human-written examples (supervised), then with '
           'human ratings. Each stage has its own risks: unlabeled text carries whatever patterns and biases the text '
           'contains, labels can be wrong, and groupings found without labels may not mean what people assume. When '
           'someone says a model "taught itself," ask what signal it actually learned from.')

S_LEARN06 = SET(
    'AI.LEARN.06',
    M=sec('Tell supervised, unsupervised and self-supervised learning apart', KIND, [
        Q('Photos are each labeled "cat" or "dog" for training. Which kind of learning is this?', 'Supervised',
          ('Unsupervised, because the model sorts photos by itself', 'the labels make it supervised'),
          ('Self-supervised, because photos contain their own answers', 'humans supplied the labels'),
          ('No learning, because photos cannot teach a model anything', 'photos are common training data'),
          'Labeled examples mean supervised learning.'),
        Q('A store groups customers with similar shopping habits, with no labels given. Which kind is this?',
          'Unsupervised',
          ('Supervised, because the store knows its customers well', 'no labels were given'),
          ('Self-supervised, because each purchase predicts the next word', 'not a word-prediction task'),
          ('Reinforcement learning, because customers earn reward points', 'not the learning signal here'),
          'Finding structure without labels is unsupervised.'),
        Q('A model hides a word in a sentence and learns to predict it. Which kind is this?', 'Self-supervised',
          ('Supervised, because a person labels every hidden word by hand', 'the text supplies the answer'),
          ('Unsupervised, because no answer exists for the hidden word', 'the hidden word is the answer'),
          ('Rule-based, because grammar rules choose each hidden word', 'it learns, not follows rules'),
          'The data provides its own answers.'),
        Q('Why are large language models mostly trained with self-supervision?',
          'Huge amounts of text need no hand-made labels',
          ('Because labeled text is illegal to use in any training at all', 'not the reason'),
          ('Because self-supervision needs no computers or data', 'it needs both'),
          ('Because people refused to read any text', 'not the reason'),
          'Text supplies its own training targets.'),
        Q('What is a label in supervised learning?', 'The right answer attached to an example',
          ('A sticker showing which company built the model', 'not this meaning'),
          ('A group the model invents with no answers given', 'that is unsupervised grouping'),
          ('The price of using the model each month', 'not this meaning'),
          'Labels are the answers to learn.'),
    ]),
    B=[cs('Compare three ways a student might learn',
          'Picture three students. The first works through a WORKBOOK with an answer key: she checks each answer and '
          'learns from corrections (like supervised learning). The second gets a box of mixed seashells with no '
          'instructions and sorts them into piles that look alike (like unsupervised learning). The third covers one '
          'word in each sentence of a novel and guesses it, then uncovers it to check (like self-supervised learning). '
          'All three learn, but from different kinds of signals.', [
              Q('The student with the answer key is like which kind?', 'Supervised learning',
                ('Unsupervised learning, since she sorts things alone', 'she has answers to check'),
                ('Self-supervised learning, since the novel checks her', 'that is the third student'),
                ('No learning at all, since answer keys are cheating', 'she learns from corrections'),
                'Checking against given answers is supervised.'),
              Q('Sorting seashells with no instructions is like which kind?', 'Unsupervised learning',
                ('Supervised learning, since shells come with labels', 'no labels'),
                ('Self-supervised learning, since shells hide words', 'no hidden words'),
                ('Reinforcement learning, since shells give rewards', 'no rewards'),
                'Grouping without answers is unsupervised.'),
              Q('Covering a word and guessing it is like which kind?', 'Self-supervised learning',
                ('Supervised learning, since a teacher labels each word', 'the text checks itself'),
                ('Unsupervised learning, since no answer is ever shown', 'the word is uncovered'),
                ('Rule-based software, since grammar picks the word', 'she is learning'),
                'The data supplies the answer.'),
              Q('Where does the third student get the correct answers?', 'From the novel itself',
                ('From a separate answer key written by a teacher', 'that is the first student'),
                ('From nowhere; no answers exist', 'the uncovered word is the answer'),
                ('From the other two students', 'not described'),
                'The text holds its own answers.'),
              Q('Which student has no answers to check against?', 'The seashell sorter',
                ('The workbook student with the answer key', 'she has answers'),
                ('The novel reader who uncovers each word', 'she can check'),
                ('All three students equally', 'two can check'),
                'Unsupervised learning has no answers.'),
          ], why='A learner who mixes up the three kinds can map them onto three study habits.')],
    F1=sec('Identify the learning signal in real projects', KIND, [
        Q('A hospital trains a model on scans that doctors marked "fracture" or "no fracture." Which kind is this?',
          'Supervised learning',
          ('Unsupervised learning, because scans have no meaning to models', 'doctors labeled them'),
          ('Self-supervised learning, because each scan predicts the next scan', 'not this setup'),
          ('No learning, because scans are only pictures', 'images are common training data'),
          'Doctor labels make it supervised.'),
        Q('A music service finds groups of songs that are often played together, with no genre labels. Which kind?',
          'Unsupervised learning',
          ('Supervised learning, because every song has a correct genre label', 'no labels were used'),
          ('Self-supervised learning, because songs predict their own lyrics', 'not this setup'),
          ('Rule-based software, because a person sorted every song', 'it found groups itself'),
          'Discovering groups is unsupervised.'),
        Q('A model learns from millions of web pages by predicting the next word. Which kind?', 'Self-supervised learning',
          ('Supervised learning, because each page was labeled by experts', 'no hand labels'),
          ('Unsupervised learning, because no words are predicted at all', 'words are predicted'),
          ('Rule-based software, because grammar books were typed in', 'it learns from text'),
          'Next-word prediction uses the text\'s own answers.'),
        Q('Which project most needs people to create labels?', 'Teaching a model to spot damaged parts on a factory line',
          ('Grouping shoppers by habits with no categories in mind', 'unsupervised'),
          ('Training on raw text to predict the next word', 'self-supervised'),
          ('Finding unusual patterns in network traffic with no examples', 'often unsupervised'),
          'Specific "damaged or not" answers need labels.'),
        Q('A company says its model "taught itself to read." What is a more precise description?',
          'It learned from text by predicting hidden or next words',
          ('It read every book ever written and understood them all', 'overstated'),
          ('It learned without any data or computing', 'it needed both'),
          ('It was given a human teacher for every sentence', 'not self-supervised'),
          'Name the actual learning signal.'),
    ]),
    F2=sec('Combine learning stages and question "taught itself" claims', KIND_F2, [
        Q('A model learned from web text, then from labeled examples, then from human ratings. Which is accurate?',
          'It combined several kinds of learning',
          ('It used only unsupervised learning from start to finish', 'labels and ratings were used'),
          ('It used no training data at any stage', 'all stages used data'),
          ('It used only rules written by programmers', 'it learned'),
          'Real systems often combine stages.'),
        Q('A model trained on unlabeled web text repeats stereotypes found online. Why?',
          'Unlabeled text carries the patterns, including biases, it contains',
          ('Self-supervised learning removes all biases automatically', 'it does not'),
          ('Stereotypes are added only during labeling', 'not only then'),
          ('The model invented the stereotypes from nothing', 'learned from text'),
          'The data\'s patterns become the model\'s patterns.'),
        Q('An unsupervised model sorts customers into "Group 3." A manager says Group 3 means "loyal customers." What '
          'should be checked?',
          'Whether the group really matches that meaning',
          ('Nothing; unsupervised groups always have clear meanings', 'meanings are assigned by people'),
          ('Only the number of the group', 'not the meaning'),
          ('Whether the group is the largest one', 'size is not meaning'),
          'Groups found without labels need interpretation.'),
        Q('Labels for a supervised model were made quickly and include mistakes. What risk follows?',
          'The model learns some of the wrong answers',
          ('None, since supervised learning ignores labels', 'labels are what it learns'),
          ('The model refuses to train on mistakes', 'it will train'),
          ('The model becomes unsupervised instead', 'not how it works'),
          'Wrong labels become wrong lessons.'),
        Q('When someone says a model "taught itself," what is the best follow-up question?',
          'What signal did it actually learn from?',
          ('How many computers did it use in total?', 'not the key question'),
          ('Is it smarter than its programmers?', 'vague'),
          ('Does it have a name and a logo?', 'irrelevant'),
          'The learning signal explains what it learned.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LEARN.07
RL = ('REINFORCEMENT LEARNING (RL) teaches a system by REWARDS instead of answer keys. The system tries actions, gets a '
      'reward or penalty, and gradually favors actions that earn more reward, like training a dog with treats. It has '
      'been used for game-playing programs and robot control. Language models are often refined with REINFORCEMENT '
      'LEARNING FROM HUMAN FEEDBACK (RLHF): people rank or rate sample answers, a separate "reward model" learns to '
      'predict those ratings, and the language model is then adjusted to produce answers that score well. Research '
      'in 2022 showed this made models better at following instructions.')
RL_F2 = ('Rewards shape behavior in ways that can surprise designers. If a reward measures the wrong thing, a system '
         'may find a shortcut that earns reward without doing what people intended, sometimes called "reward hacking." '
         'With human feedback, raters may prefer answers that sound confident or flattering, so a model can learn to '
         'sound agreeable rather than to be accurate. RLHF improved instruction-following, but the 2022 researchers '
         'also noted that such models still make simple mistakes. Better rewards help; they do not guarantee truth.')

S_LEARN07 = SET(
    'AI.LEARN.07',
    M=sec('Explain learning from rewards and from human feedback', RL, [
        Q('How does reinforcement learning teach a system?', 'Through rewards and penalties for its actions',
          ('Through an answer key attached to every training example', 'that is supervised learning'),
          ('Through rules a programmer writes for every situation', 'that is rule-based'),
          ('Through copying a single human expert exactly', 'not the idea'),
          'Actions that earn reward become more likely.'),
        Q('Which everyday activity is most like reinforcement learning?', 'Training a dog with treats',
          ('Reading the answers at the back of a textbook', 'more like supervised learning'),
          ('Sorting socks into piles that look alike', 'more like unsupervised learning'),
          ('Following a recipe word for word', 'more like rules'),
          'Rewards shape behavior.'),
        Q('In RLHF, what do people do?', 'Rank or rate sample answers',
          ('Write every answer the model will ever give', 'not possible'),
          ('Delete the model and build a new one each day', 'not the process'),
          ('Give the model rewards in the form of money', 'not literally'),
          'Human ratings guide the adjustment.'),
        Q('What does the "reward model" in RLHF do?', 'Predicts how people would rate an answer',
          ('Pays the people who rate the answers', 'not its job'),
          ('Writes the final answers that users see', 'the language model does'),
          ('Checks every answer against official sources', 'it predicts ratings, not truth'),
          'It learns to predict human preferences.'),
        Q('What did 2022 research report about RLHF?', 'It made models better at following instructions',
          ('It made models perfectly accurate', 'mistakes remained'),
          ('It made models stop using any training data', 'not true'),
          ('It made models refuse every question', 'not true'),
          'Instruction-following improved.'),
    ]),
    B=[cs('Picture training a puppy',
          'When you train a puppy to sit, you do not hand it a rulebook. It tries things: it jumps, barks, lies down, '
          'sits. When it sits, it gets a treat. Over many tries, sitting becomes more likely because it is rewarded. '
          'If you accidentally reward barking, the puppy learns to bark instead. Reinforcement learning works like '
          'this: a system tries actions, rewards make some actions more likely, and the reward decides what is '
          'learned, even if it rewards the wrong thing.', [
              Q('How does the puppy learn to sit?', 'Sitting is rewarded with a treat',
                ('It reads a rulebook about sitting', 'no rulebook'),
                ('It copies a video of another dog', 'not described'),
                ('It is told the answer in words', 'not how it learns'),
                'Rewards make the action more likely.'),
              Q('What happens if you reward barking by mistake?', 'The puppy learns to bark',
                ('The puppy still learns to sit', 'the reward shapes it'),
                ('The puppy stops learning anything', 'it learns barking'),
                ('The puppy learns to read', 'no'),
                'The reward decides what is learned.'),
              Q('In the comparison, the treat is like what?', 'The reward',
                ('The training data', 'not exactly'), ('The answer key', 'there is none'),
                ('The rulebook', 'there is none'), 'Treats are rewards.'),
              Q('Does the puppy get a rulebook?', 'No; it learns from rewards',
                ('Yes; a thick one about sitting', 'no'), ('Yes; but it ignores it', 'no rulebook'),
                ('Only on weekends', 'no'), 'Rewards, not rules.'),
              Q('Why does sitting become more likely over time?', 'It was rewarded many times',
                ('It was punished every time', 'the opposite'), ('It was random luck', 'not random'),
                ('Puppies always sit', 'not without training'), 'Repeated rewards strengthen actions.'),
          ], why='A learner unfamiliar with reward-based learning can grasp it through training a puppy with treats.')],
    F1=sec('Apply reward-based learning to examples', RL, [
        Q('A game-playing program gets points for winning and learns which moves lead to wins. Which kind of learning is '
          'this?',
          'Reinforcement learning',
          ('Supervised learning with an answer key for every move', 'it learns from rewards'),
          ('Unsupervised grouping of game boards by color', 'not the setup'),
          ('Rule-based play with every move written by hand', 'it learns'),
          'Rewards for winning drive learning.'),
        Q('Raters prefer clear, polite answers. After RLHF, what is the model likely to produce more often?',
          'Answers resembling the highly rated ones',
          ('Answers the raters rated lowest', 'the opposite'),
          ('Answers chosen at random with no pattern', 'not the effect'),
          ('Exactly the same single answer to every question', 'not the effect'),
          'It is adjusted toward highly rated answers.'),
        Q('Which step comes first in RLHF?', 'People rank or rate sample answers',
          ('The model is released to the public', 'later'),
          ('The reward model writes the answers', 'not its role'),
          ('Users rate the final product forever', 'not the first step'),
          'Human ratings come first.'),
        Q('A robot arm gets a reward each time it stacks a block successfully. What will it tend to do?',
          'Repeat actions that led to successful stacks',
          ('Avoid stacking blocks entirely', 'rewards encourage stacking'),
          ('Follow a written list of every arm movement', 'it learns from rewards'),
          ('Stop moving after the first reward', 'not the expected effect'),
          'Rewarded actions become more likely.'),
        Q('Why might a company use RLHF on a chatbot?', 'To make answers better match what people prefer',
          ('To guarantee every answer is true', 'no guarantee'),
          ('To remove the need for any training data', 'still needs data'),
          ('To make the chatbot run without electricity', 'nonsense'),
          'Human preferences guide adjustments.'),
    ]),
    F2=sec('Anticipate problems with rewards and ratings', RL_F2, [
        Q('A cleaning robot is rewarded for "no visible mess" and learns to push mess under a rug. What is this?',
          'Reward hacking: reward without the intended result',
          ('Perfect learning of the cleaning task', 'not the intended result'), ('Supervised learning from labeled photos of messy rooms', 'not the setup'),
          ('A broken camera on the robot', 'the reward was the problem'),
          'The reward measured the wrong thing.'),
        Q('Raters often prefer confident, flattering answers. What could a model learn?',
          'To sound agreeable rather than be accurate',
          ('To become more accurate in every case', 'not guaranteed'),
          ('To refuse every question politely', 'not implied'),
          ('To stop responding to raters', 'nonsense'),
          'Ratings can reward style over truth.'),
        Q('What did the 2022 RLHF researchers note about their improved models?', 'They still made simple mistakes',
          ('They never made any mistakes', 'not true'),
          ('They could no longer follow instructions', 'the opposite'),
          ('They no longer needed any ratings', 'not stated'),
          'Improvement is not perfection.'),
        Q('What is the best way to reduce reward hacking?',
          'Design rewards that measure what is truly intended',
          ('Give larger rewards for the same thing', 'still the wrong target'), ('Remove all rewards and hope', 'nothing to learn from'),
          ('Reward the system for any action it takes at all', 'worse'),
          'Rewards must match goals.'),
        Q('Which statement about RLHF is accurate?', 'Better rewards help, but do not guarantee truth',
          ('RLHF guarantees answers are always correct', 'not true'),
          ('RLHF removes the need to check answers', 'still check'),
          ('RLHF makes models conscious', 'unsupported'),
          'Answers still need checking.'),
    ]),
)

# ---------------------------------------------------------------------------------------------- AI.LLM.08
ATT = ('Most modern language models use a design called the TRANSFORMER, introduced in a 2017 research paper. Its key '
       'idea is ATTENTION: when the model processes one word (token), it can weigh how relevant every other word in '
       'the context is. In "The trophy did not fit in the suitcase because it was too big," attention helps link "it" '
       'with "trophy." The model computes these weights with math, many times over, in many layers, which lets it '
       'track relationships across long passages. Attention is a mathematical weighting of text, not a mind paying '
       'attention the way a person does.')
ATT_F2 = ('The word "attention" invites human comparisons, so be careful. A model\'s attention weights are numbers '
          'computed from patterns; they are not feelings, intentions or awareness. Attention also does not guarantee '
          'correct understanding: a model can weigh the wrong words and link "it" to the wrong noun, especially in '
          'tricky sentences. Researchers sometimes inspect attention weights to study models, but high attention on a '
          'word does not by itself prove the model "understood" that word or used it for the reason a person would.')

ATT_EX = TABLE([['Word', 'How strongly "it" is linked (made-up weights)'], ['trophy', '0.71'], ['suitcase', '0.18'],
                ['fit', '0.06'], ['other words', '0.05']],
               label='Prepared example (made-up attention weights, for teaching)')

S_LLM08 = SET(
    'AI.LLM.08',
    M=sec('Explain attention in transformers at a conceptual level', ATT, [
        Q('What is the key idea of the transformer design?', 'Attention: weighing how relevant other words are',
          ('Memorizing every sentence ever written word for word', 'not the key idea'),
          ('Following grammar rules typed in by linguists', 'it learns from data'),
          ('Reading only one word at a time with no context', 'attention uses context'),
          'Attention links words to relevant context.'),
        Q('In the trophy sentence, what does attention help the model link "it" to?', 'The trophy',
          ('The suitcase', 'less relevant here'), ('The word "because"', 'not the referent'),
          ('The word "did"', 'not the referent'),
          'Attention helps resolve references.'),
        Q('Using the made-up weights in the table, which word is most strongly linked to "it"?', 'trophy',
          ('suitcase', '0.18 is lower'), ('fit', '0.06 is lower'), ('other words', '0.05 is lowest'),
          'trophy has the highest weight (0.71).', ex=ATT_EX),
        Q('When was the transformer introduced, according to the passage?', 'In a 2017 research paper',
          ('In a 1956 workshop at a university', 'that was earlier AI history'),
          ('In 2022, when chatbots became popular', 'later'),
          ('It has existed since the first computers', 'not true'),
          '2017.'),
        Q('Which statement about attention is accurate?', 'It is a mathematical weighting, not a mind',
          ('It means the model consciously focuses like a person', 'misleading'),
          ('It means the model has feelings about words', 'not true'),
          ('It means the model reads only the first word', 'not true'),
          'Attention is math.'),
    ]),
    B=[cs('Picture highlighting a sentence',
          'When you read "Maria gave Sam her umbrella because she was leaving early," you might mentally connect "she" '
          'to "Maria." Imagine marking how strongly each other word helps you understand "she": a heavy highlight on '
          '"Maria," a lighter one on "leaving," almost none on "umbrella." A transformer does something like this with '
          'numbers for every word: it computes weights showing how much each other word should influence the current '
          'one. The highlights are a teaching picture; the real thing is arithmetic done many times.', [
              Q('In the example, which word gets the heaviest highlight for "she"?', 'Maria',
                ('umbrella', 'almost none'), ('early', 'not the referent'), ('Sam', 'not the referent here'),
                '"She" refers to Maria.'),
              Q('What do the highlights stand for?',
          'How much each word influences the current one',
          ('How long each word is', 'not the meaning'), ('How rare each word is', 'not the meaning'),
          ('How loudly each word is read aloud by people', 'not the meaning'),
          'Influence weights.'),
              Q('What does a transformer use instead of highlighter ink?', 'Numbers computed for every word',
                ('Real colored ink on paper', 'no'), ('A human reader', 'no'), ('A dictionary lookup', 'no'),
                'Weights are numbers.'),
              Q('Is the highlighter picture the literal mechanism?', 'No, it is a teaching picture',
                ('Yes, models use highlighters', 'no'), ('Yes, models see colors', 'no'),
                ('No, models ignore context', 'they use context'), 'An analogy only.'),
              Q('Why would "umbrella" get almost no highlight for "she"?',
          'It does not help identify "she"',
          ('It is too long a word to weigh', 'not the reason'), ('It is misspelled', 'not misspelled'),
          ('It comes after "she"', 'it comes before'),
          'Relevance decides weight.'),
          ], why='A learner who finds "attention" abstract can picture it as highlighting relevant words, while '
                 'remembering it is only an analogy.')],
    F1=sec('Apply the attention idea to sentences', ATT, [
        Q('"The dog chased the ball until it was tired." Which word should attention most link to "it"?', 'dog',
          ('ball', 'balls do not get tired'), ('chased', 'not a referent'), ('until', 'not a referent'),
          'Dogs get tired; balls do not.'),
        Q('"The dog chased the ball until it rolled under the couch." Now which word should "it" link to?', 'ball',
          ('dog', 'less likely to roll under a couch'), ('couch', 'it rolled under the couch'),
          ('chased', 'not a referent'), 'Balls roll under couches.'),
        Q('Why does attention help with long passages?', 'It can relate words that are far apart',
          ('It shortens every passage to one word', 'not what it does'),
          ('It removes all earlier words', 'not what it does'),
          ('It reads only the final sentence', 'not what it does'),
          'Relationships across distance can be tracked.'),
        Q('A friend says, "Attention means the AI is interested in my story." What is more accurate?',
          'Attention is weighting of words, not interest',
          ('Correct; the AI feels curious about stories', 'not supported'),
          ('Correct; attention means it likes the user', 'not supported'),
          ('Wrong; models never use context at all', 'they do'),
          'The term is technical, not emotional.'),
        Q('Which statement fits the passage?', 'Attention is computed many times across many layers',
          ('Attention is computed once for a whole book', 'many times'),
          ('Attention is typed in by programmers word by word', 'computed'),
          ('Attention is the same as the training cutoff', 'unrelated'),
          'Repeated, layered computation.'),
    ]),
    F2=sec('Avoid over-reading what attention shows', ATT_F2, [
        Q('A model links "it" to the wrong noun in a tricky sentence. What does this show?',
          'Attention can weigh the wrong words',
          ('Attention always resolves references correctly', 'not always'),
          ('The model was not using attention at all', 'not implied'),
          ('Tricky sentences cannot be processed', 'they can, imperfectly'),
          'Weights can be wrong.'),
        Q('A researcher sees high attention on a word. What can they safely conclude?',
          'That word got a high weight; that is not proof',
          ('The model fully understood that word', 'overreading'), ('The model felt strongly about the word', 'not feelings'),
          ('The word was the answer to every later question', 'not implied'),
          'Weights are not proof of understanding.'),
        Q('Why can the word "attention" mislead beginners?', 'It suggests a human mind focusing',
          ('It suggests the model is slow', 'not the issue'),
          ('It suggests the model is a database', 'not the issue'),
          ('It suggests the model has no context', 'the opposite'),
          'Human words invite human comparisons.'),
        Q('Which description of attention weights is most accurate?', 'Numbers computed from patterns',
          ('Feelings about which words matter', 'not feelings'),
          ('Intentions the model chooses freely', 'not intentions'),
          ('Awareness of the reader\'s needs', 'not awareness'),
          'Weights are computed numbers.'),
        Q('Does a transformer design guarantee correct answers?', 'No; it can still produce errors',
          ('Yes; attention prevents all errors', 'not true'),
          ('Yes; transformers check facts automatically', 'not true'),
          ('No; transformers cannot process text', 'they can'),
          'Good design does not guarantee truth.'),
    ]),
)

SETS = [S_LEARN06, S_LEARN07, S_LLM08]
