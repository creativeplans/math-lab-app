"""Logic sets 49-51: common fallacies; weighing evidence; constrained optimization."""
import itertools
from fractions import Fraction
from lq import S, B, FW, mc, tf, sa, values, lesson

GLOSS = {
    'Attacking the person': 'rejecting a claim because of who made it, instead of because of the reasons given',
    'False choice': 'presenting only two options when others are possible',
    'Hasty generalization': 'drawing a broad conclusion from too few cases',
    'Circular reasoning': 'using the conclusion, in other words, as a reason for itself',
    'After, so because': 'concluding that A caused B only because B happened after A',
    'Slippery slope': 'claiming, without support, that one step will lead to a chain of extreme results',
    'Appeal to popularity': 'claiming something is true because many people believe it',
    'Straw man': 'attacking a distorted version of someone\'s argument instead of the real one',
}


def fall_prompt(names, text):
    return ('Definitions: ' + ' '.join('%s: %s.' % (n, GLOSS[n]) for n in names) + ' ' + text)


def fall_mc(text, key, others, why):
    names = [key] + [o for o, _ in others]
    return mc(fall_prompt(names, text + ' Which fallacy is this?'), key, others, why)


# ------------------------------------------------------------------ Set 49: common fallacies
def s49():
    return S(49, 'Recognize common informal fallacies in self-contained arguments',
             main=[
                 fall_mc('Dana argues that the library should stay open later. Raj replies: "Dana is always late to class, so '
                         'her opinion about library hours does not count."', 'Attacking the person',
                         [('Hasty generalization', 'Raj does not generalize from a few cases'),
                          ('Circular reasoning', 'Raj does not use his conclusion as a reason'),
                          ('Appeal to popularity', 'Raj does not mention what many people believe')],
                         'Raj rejects Dana\'s claim because of something about Dana, not because of her reasons.'),
                 fall_mc('"Either we cancel the field trip, or every student will get lost in the city."', 'False choice',
                         [('Slippery slope', 'no chain of steps is described'),
                          ('Straw man', 'no one\'s argument is being distorted'),
                          ('After, so because', 'no claim about one event following another is made')],
                         'Other options exist, such as more chaperones or a planned route.'),
                 fall_mc('"I met two rude people from that town, so everyone from that town is rude."', 'Hasty generalization',
                         [('Attacking the person', 'no one\'s argument is being rejected'),
                          ('False choice', 'no two options are presented'),
                          ('Circular reasoning', 'the conclusion is not used as a reason')],
                         'Two cases are far too few to support a claim about everyone in a town.'),
                 tf(fall_prompt(['Circular reasoning'], '"This app is the best because it is better than all the others" is '
                                                        'an example of circular reasoning.'), True,
                    '"Better than all the others" says the same thing as "the best", so the reason is just the conclusion '
                    'restated.'),
                 fall_mc('"After I started wearing my lucky socks, our team won three games in a row. The socks made us win."',
                         'After, so because',
                         [('Hasty generalization', 'it does not generalize to a group'),
                          ('Appeal to popularity', 'it does not mention what many people believe'),
                          ('Slippery slope', 'it does not predict a chain of extreme results')],
                         'The wins came after the socks, but nothing shows the socks caused them.'),
             ],
             back=[B('Strategy: name what the argument does instead of giving reasons', 'guided_strategy',
                     'Students sense that an argument is weak but cannot say why. Asking what the argument does in place of '
                     'giving real reasons leads to the fallacy\'s name.',
                     lesson=lesson('Name what the argument does instead of giving reasons',
                                   ['Find the conclusion. Then find what is offered as the reason.',
                                    'Ask: is the reason about the claim, or about something else (the person, how popular '
                                    'it is, what came first)?',
                                    'Match what the argument does to a definition: attacking the person, false choice, '
                                    'hasty generalization, circular reasoning, after-so-because, slippery slope, appeal to '
                                    'popularity, straw man.'],
                                   'Worked example (a different argument)',
                                   ['"Everyone in my class uses this calculator, so it must give correct answers."'],
                                   ['Conclusion: the calculator gives correct answers. Reason: everyone uses it.',
                                    'The reason is about popularity, not about accuracy: appeal to popularity.']),
                     qs=[
                         mc(fall_prompt(['Appeal to popularity', 'Straw man', 'False choice', 'Slippery slope'],
                                        'Which definition describes "Millions of people watch this show, so it must be '
                                        'educational"?'), 'Appeal to popularity',
                            [('Straw man', 'no one\'s argument is distorted'), ('False choice', 'no two options are '
                                                                                               'presented'),
                             ('Slippery slope', 'no chain of results is predicted')],
                            'The only reason given is how many people watch it.'),
                         tf(fall_prompt(['Hasty generalization'], 'Concluding that all dogs are friendly after meeting three '
                                                                  'friendly dogs is a hasty generalization.'), True,
                            'Three dogs are too few cases for a claim about all dogs.'),
                         tf(fall_prompt(['Attacking the person'], 'Saying "The bridge design is unsafe because the beams are '
                                                                  'too thin for the load" is attacking the person.'), False,
                            'The reason is about the design itself, not about a person.'),
                         mc('An argument\'s reason is about who made a claim rather than about the claim. Which question best '
                            'helps you notice this?', 'Is the reason about the claim, or about something else?',
                            [('Is the conclusion surprising?', 'surprising conclusions can be well supported'),
                             ('Is the argument long?', 'length does not reveal what the reasons are about'),
                             ('Do I agree with the conclusion?', 'agreeing does not show whether the reasons are good')],
                            'Checking what the reason is about exposes attacks on the person.'),
                         tf(fall_prompt(['Slippery slope'], '"If we allow phones at lunch, then students will use them in '
                                                            'class, then stop learning, then fail school" is a slippery '
                                                            'slope.'), True,
                            'A chain of extreme results is claimed without support for each step.'),
                     ])],
             f1=FW('Straw men, slopes and popularity', 'Harder: tell similar fallacies apart.', [
                 fall_mc('Ava says the school should add one vegetarian meal option. Ben replies: "Ava wants to ban meat '
                         'from the cafeteria completely, and that is unfair to everyone."', 'Straw man',
                         [('Attacking the person', 'Ben attacks a claim, not Ava\'s character'),
                          ('False choice', 'Ben does not offer only two options'),
                          ('Hasty generalization', 'Ben does not generalize from a few cases')],
                         'Ben attacks a much stronger claim (a full ban) than the one Ava made.'),
                 fall_mc('"If we let one student retake the quiz, soon everyone will retake every quiz, and grades will mean '
                         'nothing."', 'Slippery slope',
                         [('False choice', 'it does not present exactly two options'),
                          ('After, so because', 'it does not claim a past event caused another'),
                          ('Circular reasoning', 'the conclusion is not used as a reason')],
                         'It predicts an extreme chain of results from one step, without support.'),
                 tf(fall_prompt(['Appeal to popularity'], '"Most dentists in a large survey recommend brushing twice a day, so '
                                                          'brushing twice a day is likely a good idea" is an appeal to '
                                                          'popularity.'), False,
                    'The people cited are experts on teeth, and their recommendation is evidence about the topic. An appeal '
                    'to popularity relies only on how many people believe something.'),
                 fall_mc('"The rule must be fair because it is the rule, and rules are fair."', 'Circular reasoning',
                         [('Appeal to popularity', 'it does not mention what many people believe'),
                          ('Straw man', 'it does not distort anyone\'s argument'),
                          ('Hasty generalization', 'it does not reason from a few examples')],
                         'Being a rule is offered as proof of fairness only because rules are assumed to be fair: the '
                         'conclusion supports itself.'),
                 fall_mc('"The new principal started in September, and in October the cafeteria food got worse. The principal '
                         'ruined the food."', 'After, so because',
                         [('Attacking the person', 'no argument by the principal is being rejected'),
                          ('Slippery slope', 'no chain of future results is predicted'),
                          ('False choice', 'no two options are presented')],
                         'The timing alone is used as proof that one caused the other.'),
             ]),
             f2=FW('Is it really a fallacy?', 'Expert: tell fallacies from reasonable arguments.', [
                 mc(fall_prompt(['Attacking the person'], 'Which reply is NOT attacking the person?'),
                    '"Your numbers are from 2010, and the prices have changed since then."',
                    [('"You are too young to understand prices."', 'it dismisses the claim because of the speaker\'s age'),
                     ('"You only say that because you work for the store."', 'it dismisses the claim because of the '
                                                                             'speaker\'s job, not the reasons'),
                     ('"Nobody listens to you anyway."', 'it is about the speaker, not the claim')],
                    'The correct reply challenges the evidence itself.'),
                 tf(fall_prompt(['False choice'], '"A whole number is either even or odd" is a false choice.'), False,
                    'Every whole number really is even or odd, so the two options are complete.'),
                 mc(fall_prompt(['Hasty generalization', 'After, so because', 'Straw man', 'Appeal to popularity'],
                                'Which argument avoids all four fallacies defined above?'),
                    'A random sample of 500 voters favored the plan, so most voters probably favor it.',
                    [('Our team won after the coach changed shoes, so the shoes helped.', 'after, so because'),
                     ('Everyone online says the plan is good, so it is good.', 'appeal to popularity'),
                     ('My two cousins liked the plan, so most voters like it.', 'hasty generalization from two people')],
                    'A large random sample is good evidence about the whole group.'),
                 fall_mc('Mo says homework should be shorter on weekends. Lee replies: "So you think students should never '
                         'study at all? That would be terrible."', 'Straw man',
                         [('Slippery slope', 'Lee does not predict a chain of steps from Mo\'s idea'),
                          ('Appeal to popularity', 'Lee does not mention what many people think'),
                          ('Circular reasoning', 'Lee does not use the conclusion as a reason')],
                         'Lee replaces Mo\'s modest claim with an extreme one and attacks that.'),
                 tf(fall_prompt(['Slippery slope'], 'An argument that predicts a chain of results is always a slippery slope, '
                                                    'even when each step is supported by evidence.'), False,
                    'A slippery slope is a fallacy only when the steps are claimed without support. A well-supported chain '
                    'of causes can be good reasoning.'),
             ]))


# ------------------------------------------------------------------ Set 50: weighing evidence
def pct(a, b):
    return Fraction(100 * a, b)


def s50():
    return S(50, 'Judge whether evidence supports a claim: samples, comparisons and correlation',
             main=[
                 mc('To learn how often people in a town exercise, a student surveys 100 people leaving a gym. What is the '
                    'main problem with this evidence?', 'People leaving a gym probably exercise more than the town as a '
                                                        'whole.',
                    [('100 people is always too few for a survey.', 'size is not the main issue; who was asked is'),
                     ('The survey should have asked about diet too.', 'that changes the question, not the evidence'),
                     ('Surveys can never give useful evidence.', 'well-chosen samples can be very useful')],
                    'The sample is not representative of the town.'),
                 sa('School A: 45 of its 60 students passed a test. School B: 52 of its 80 students passed. What percent of '
                    'School A\'s students passed?', 'Percent:', str(pct(45, 60)),
                    '45 / 60 = 0.75 = 75%. (School B: 52 / 80 = 65%.) Comparing percents, not counts, is fair when the '
                    'schools differ in size.', compute=lambda: str(pct(45, 60))),
                 tf('In many towns, more ice-cream sales come with more swimming accidents. This shows that eating ice cream '
                    'causes swimming accidents.', False,
                    'Both rise in hot weather. A correlation alone does not show that one causes the other.'),
                 mc('Which study design gives the best evidence that a tutoring program raises test scores?',
                    'Randomly assign students to get tutoring or not, then compare the two groups\' scores.',
                    [('Ask tutored students whether they feel they improved.', 'feelings are not test scores, and there is '
                                                                              'no comparison group'),
                     ('Compare tutored students with students who chose not to sign up.', 'students who sign up may differ '
                                                                                         'in other ways'),
                     ('Measure the scores of tutored students only.', 'with no comparison group, the effect is unknown')],
                    'Random assignment makes the groups alike except for the tutoring.'),
                 values('A claim says that more than half of a school\'s students prefer a later start time. In a random '
                        'sample of 40 students, n said they prefer it. Give a value of n that would support the claim.',
                        [('n', 'n =')], 'isInteger(n) and n > 20 and n <= 40', {'n': 28},
                        'More than half of 40 is more than 20, so n from 21 to 40 supports the claim.',
                        wrong=[{'n': 20}, {'n': 12}, {'n': 41}], search={'n': range(0, 45)}),
             ],
             back=[B('Compare rates, not counts', 'prerequisite',
                     'Most evidence questions compare groups of different sizes. Students who compare raw counts instead '
                     'of rates draw the wrong conclusion.',
                     qs=[
                         sa('18 of 24 students in a class walk to school. What percent is that?', 'Percent:',
                            str(pct(18, 24)), '18 / 24 = 0.75 = 75%.', compute=lambda: str(pct(18, 24))),
                         tf('Club X has 30 members and 12 play chess. Club Y has 10 members and 6 play chess. A larger '
                            'share of Club Y plays chess.', True, 'X: 12 / 30 = 40%. Y: 6 / 10 = 60%.',
                            check=lambda: pct(6, 10) > pct(12, 30)),
                         mc('Town P had 50 car accidents and Town Q had 30. What else do you need before saying Town P\'s '
                            'roads are more dangerous?', 'How many people or cars each town has',
                            [('The names of the drivers', 'names do not affect the rate'),
                             ('Nothing; 50 is more than 30', 'a larger town can have more accidents and still be safer'),
                             ('The colors of the cars', 'color is not relevant to the comparison')],
                            'Accidents per car or per person is the fair comparison.'),
                         sa('A survey of 200 people finds that 30 own a bike. What percent own a bike?', 'Percent:',
                            str(pct(30, 200)), '30 / 200 = 15%.', compute=lambda: str(pct(30, 200))),
                         tf('If Group A has more members with a trait than Group B, then a larger percent of Group A has the '
                            'trait.', False, 'Group A might be much larger: 30 of 100 is less than 20 of 40.'),
                     ])],
             f1=FW('Samples and comparisons', 'Harder: bias, rates and controls.', [
                 mc('A website asks visitors to vote on whether the town needs a new park. Of 300 votes, 80% say yes. Why is '
                    'this weak evidence about the whole town?',
                    'People who choose to vote online may care more about parks than others.',
                    [('300 votes is more than enough.', 'that does not address who chose to vote'),
                     ('80% is too high to be believed.', 'a high percent can be accurate'),
                     ('Websites cannot count votes.', 'counting is not the problem')],
                    'A self-selected sample can differ from the population.'),
                 sa('Class A: 21 of 28 students finished the project on time. Class B: 24 of 30. What is the higher of the '
                    'two on-time percents?', 'Percent:', str(max(pct(21, 28), pct(24, 30))),
                    'A: 75%. B: 80%. The higher is 80%, even though the counts are close.',
                    compute=lambda: str(max(pct(21, 28), pct(24, 30)))),
                 tf('A study finds that students who own more books tend to have higher reading scores. This alone proves '
                    'that buying books raises reading scores.', False,
                    'Families who buy many books may also read together more. The correlation alone does not prove cause.'),
                 mc('To test whether a new fertilizer helps tomato plants grow, which design is best?',
                    'Give fertilizer to a randomly chosen half of the plants and compare them with the other half.',
                    [('Give fertilizer to all plants and measure them.', 'there is no comparison group'),
                     ('Use the fertilizer only on the healthiest plants.', 'healthier plants would grow more anyway'),
                     ('Ask a gardener whether the plants look bigger.', 'opinion is not a measurement')],
                    'Random assignment and a comparison group isolate the effect of the fertilizer.'),
                 values('A coin is flipped 50 times to test whether it is fair. Give a number of heads h from 0 to 50 that would '
                        'be strong evidence the coin favors heads. Use this test: h is at least 35.', [('h', 'h =')],
                        'isInteger(h) and h >= 35 and h <= 50', {'h': 40},
                        'The stated test counts 35 or more heads as strong evidence. (A fair coin rarely gives that many.)',
                        wrong=[{'h': 26}, {'h': 30}, {'h': 51}], search={'h': range(0, 55)}),
             ]),
             f2=FW('Comparisons that reverse', 'Expert: combined groups and base rates.', [
                 sa('Two clinics treat a condition. Clinic A treats 100 mild cases (90 recover) and 20 severe cases (8 '
                    'recover). Clinic B treats 20 mild cases (19 recover) and 100 severe cases (50 recover). What percent of '
                    'all Clinic A patients recover?', 'Percent:', str(pct(98, 120)),
                    '(90 + 8) / 120 = 98 / 120, about 81.7%. In fraction form, 245/3 percent.',
                    compute=lambda: str(pct(98, 120))),
                 mc('In the clinics above, Clinic A has the higher overall recovery rate (about 82% to 58%). Which statement '
                    'is true?', 'Clinic B has the higher recovery rate for mild cases AND for severe cases.',
                    [('Clinic A is better for both mild and severe cases.', 'B: 95% mild, 50% severe; A: 90% mild, 40% '
                                                                            'severe'),
                     ('The two clinics are equally good for mild cases.', '90% and 95% are not equal'),
                     ('Clinic A must be the better clinic.', 'A looks better only because it treats more mild cases')],
                    'A treats mostly mild cases, which recover more often, so its combined rate is higher even though B '
                    'does better within each group.',
                    check=lambda t: t.startswith('Clinic B') and pct(19, 20) > pct(90, 100) and pct(50, 100) > pct(8, 20)),
                 tf('In the clinics above, comparing only the overall recovery rates gives a fair comparison of the clinics.',
                    False, 'The clinics treat very different mixes of cases. Comparing within each group is fairer.'),
                 sa('A test for a rare condition is positive for 95 of every 100 people who have it and for 5 of every 100 '
                    'people who do not. In a town of 10,000 people, 100 have the condition. About how many people in the '
                    'town test positive in all?', 'People:', str(95 + 5 * 99),
                    'Have it: 95 of 100 test positive. Do not have it: 5% of 9,900 = 495. Total 590.',
                    compute=lambda: str(95 + 9900 * 5 // 100)),
                 mc('In the town above, 590 people test positive and 95 of them have the condition. What fraction of the '
                    'positive tests are correct?', 'About 16%', [('About 95%', '95% is the rate among people who have the '
                                                                             'condition, not among positive tests'),
                                                                ('About 5%', '5% is the false-positive rate among people '
                                                                             'without it'),
                                                                ('About 50%', '95 is far less than half of 590')],
                    '95 / 590 is about 0.161, or 16%. Most positives come from the much larger group without the '
                    'condition.', check=lambda t: abs(95 / 590 * 100 - int(t.split()[1].rstrip('%'))) < 1),
             ]))


# ------------------------------------------------------------------ Set 51: best possible
def fewest_coins(total, coins):
    best = [0] + [None] * total
    for t in range(1, total + 1):
        opts = [best[t - c] for c in coins if c <= t and best[t - c] is not None]
        best[t] = min(opts) + 1 if opts else None
    return best[total]


def max_partition_product(n):
    best = {0: 1}
    for t in range(1, n + 1):
        best[t] = max([t] + [k * best[t - k] for k in range(1, t)])
    return best[n]


def clock_times():
    return ['%d:%02d' % (h, m) for h in range(1, 13) for m in range(60)]


def digit_product(t):
    p = 1
    for ch in t.replace(':', ''):
        p *= int(ch)
    return p


LP = [(x, y) for x in range(0, 11) for y in range(0, 11) if x + 2 * y <= 10 and x <= 6]


def s51():
    best_lp = max(x + 3 * y for x, y in LP)
    return S(51, 'Find the best value under stated constraints and show nothing better is possible',
             main=[
                 sa('Two whole numbers add up to 20. What is the largest possible product?', 'Product:',
                    str(max(a * (20 - a) for a in range(21))),
                    '10 x 10 = 100. Moving one number up by k and the other down by k gives (10 + k)(10 - k) = 100 - k '
                    'squared, which is smaller.', compute=lambda: str(max(a * (20 - a) for a in range(21)))),
                 sa('A rectangular pen uses exactly 24 meters of fence, and its sides are whole numbers of meters. What is '
                    'the largest possible area, in square meters?', 'Area:',
                    str(max(w * (12 - w) for w in range(1, 12))),
                    'The sides add to 12. Listing 1 x 11, 2 x 10, ..., 6 x 6 gives areas 11, 20, 27, 32, 35, 36. The 6 by 6 '
                    'square is largest.', compute=lambda: str(max(w * (12 - w) for w in range(1, 12)))),
                 mc('A 12-hour digital clock shows times from 1:00 to 12:59. Which time has the largest product of its '
                    'digits?', '9:59', [('12:59', '1 x 2 x 5 x 9 = 90'), ('8:59', '8 x 5 x 9 = 360'),
                                       ('11:59', '1 x 1 x 5 x 9 = 45')],
                    '9 x 5 x 9 = 405. The hour digit is at most 9 and the minute digits at most 5 and 9, so nothing can '
                    'beat 405, and only 9:59 reaches it.',
                    check=lambda t: digit_product(t) == max(digit_product(x) for x in clock_times())),
                 tf('Using coins worth 1, 5, 10 and 25 cents, the fewest coins that make exactly 30 cents is 2.', True,
                    '25 + 5 uses 2 coins, and no single coin is worth 30 cents.',
                    check=lambda: fewest_coins(30, [1, 5, 10, 25]) == 2),
                 values('Whole numbers x and y are each 0 or more, with x + 2y at most 10 and x at most 6. Make x + 3y as large '
                        'as possible. Give x and y.', [('x', 'x ='), ('y', 'y =')], 'x == 0 and y == 5', {'x': 0, 'y': 5},
                        'x + 3y = (x + 2y) + y is at most 10 + y, and y is at most 5, so x + 3y is at most 15. Only x = 0, '
                        'y = 5 reaches 15.', wrong=[{'x': 6, 'y': 2}, {'x': 2, 'y': 4}, {'x': 1, 'y': 5}],
                        search={'x': range(0, 11), 'y': range(0, 11)},
                        method='Checked all %d allowed pairs: the best value is %d, reached only at (0, 5).'
                        % (len(LP), best_lp) if [p for p in LP if p[0] + 3 * p[1] == best_lp] == [(0, 5)] else 'MISMATCH'),
             ],
             back=[B('Strategy: find a good answer, then prove nothing beats it', 'guided_strategy',
                     'Students stop at the first good answer. A best-answer problem needs two parts: an example that '
                     'reaches a value, and a reason no answer can do better.',
                     lesson=lesson('Find a good answer, then prove nothing beats it',
                                   ['Try several cases in an organized way and keep the best so far.',
                                    'Look for a limit (a bound): a reason every answer is at most some value.',
                                    'If your best example reaches the bound, it is the best possible.'],
                                   'Worked example (a different problem)',
                                   ['Two whole numbers add to 9. What is the largest product?'],
                                   ['Try 1 x 8 = 8, 2 x 7 = 14, 3 x 6 = 18, 4 x 5 = 20.',
                                    'Moving away from the middle makes the product smaller, so 20 is the largest.']),
                     qs=[
                         sa('Two whole numbers add to 14. What is the largest possible product?', 'Product:', '49',
                            '7 x 7 = 49.', compute=lambda: str(max(a * (14 - a) for a in range(15)))),
                         tf('To show that a value is the largest possible, it is enough to find one example that reaches it.',
                            False, 'You also need a reason no other answer can be larger.'),
                         mc('Which numbers from the list 4, 9, 2, 7, 5 give the largest sum if you may choose any two?',
                            '9 and 7', [('9 and 5', '9 + 5 = 14, less than 16'), ('4 and 9', '4 + 9 = 13'),
                                        ('7 and 5', '7 + 5 = 12')],
                            'The two largest numbers give the largest sum: 16.'),
                         sa('Using coins worth 1, 5 and 10 cents, what is the fewest coins that make 27 cents?', 'Coins:',
                            str(fewest_coins(27, [1, 5, 10])), '10 + 10 + 5 + 1 + 1: 5 coins.',
                            compute=lambda: str(fewest_coins(27, [1, 5, 10]))),
                         tf('A rectangle with whole-number sides and perimeter 20 can have area 25.', True, 'A 5 by 5 square.',
                            check=lambda: any(w * (10 - w) == 25 for w in range(1, 10))),
                     ])],
             f1=FW('When the obvious choice is not best', 'Harder: greedy choices that fail, and products.', [
                 sa('Coins are worth 1, 4 and 6 cents. What is the fewest coins that make exactly 8 cents?', 'Coins:',
                    str(fewest_coins(8, [1, 4, 6])),
                    'Taking the biggest coin first gives 6 + 1 + 1 (3 coins), but 4 + 4 uses only 2.',
                    compute=lambda: str(fewest_coins(8, [1, 4, 6]))),
                 sa('Whole numbers add up to 10 (you choose how many numbers). What is the largest possible product?',
                    'Product:', str(max_partition_product(10)),
                    'Use 3s and 2s: 3 + 3 + 2 + 2 gives 36, and 3 + 3 + 4 also gives 36. Splitting any part 5 or more '
                    'into smaller parts raises the product, and 1s never help.',
                    compute=lambda: str(max_partition_product(10))),
                 tf('Coins are worth 1, 4 and 6 cents. Always taking the largest coin that fits gives the fewest coins for '
                    'every amount.', False, 'For 8 cents it gives 6 + 1 + 1, but 4 + 4 is better.',
                    check=lambda: all(greedy(t, [6, 4, 1]) == fewest_coins(t, [1, 4, 6]) for t in range(1, 40))),
                 mc('A backpack can hold at most 10 kilograms. Items: tent 6 kg, value 8; stove 4 kg, value 5; food 5 kg, '
                    'value 6; lamp 1 kg, value 3. Which choice has the greatest total value?', 'Food, stove, lamp',
                    [('Tent, stove', '10 kg with value 13, less than 14'), ('Tent, lamp', '7 kg with value 11'),
                     ('Food, lamp', '6 kg with value 9')],
                    'Food, stove and lamp weigh exactly 10 kg and are worth 14. Taking the most valuable item (the tent) '
                    'first leaves room for at most 4 more kg, and the best that adds is the stove: 13.',
                    check=lambda t: knap_value(t) == max(knap_value(', '.join(c)) for r in range(1, 5)
                                                         for c in itertools.combinations(KNAP, r) if knap_ok(c))),
                 values('Two whole numbers are each at least 1 and their product is 36. Make their sum as small as possible. '
                        'Give the two numbers.', [('a', 'a ='), ('b', 'b =')], 'a == 6 and b == 6', {'a': 6, 'b': 6},
                        'The pairs are 1 x 36, 2 x 18, 3 x 12, 4 x 9, 6 x 6 with sums 37, 20, 15, 13, 12. 6 and 6 is best.',
                        wrong=[{'a': 4, 'b': 9}, {'a': 1, 'b': 36}, {'a': 3, 'b': 12}]),
             ]),
             f2=FW('Prove the best value', 'Expert: bounds that match the best example.', [
                 sa('Whole numbers add up to 20 (you choose how many numbers). What is the largest possible product?',
                    'Product:', str(max_partition_product(20)),
                    'Any part 5 or more can be split into 2 and the rest to raise the product, and 4 = 2 + 2 gives the same '
                    'product, so use only 2s and 3s. Three 2s (product 8) are worse than two 3s (product 9), so use at most '
                    'two 2s: 20 = 3 x 6 + 2, product 729 x 2 = 1458.', compute=lambda: str(max_partition_product(20))),
                 sa('Coins are worth 1, 7 and 10 cents. What is the fewest coins that make exactly 14 cents?', 'Coins:',
                    str(fewest_coins(14, [1, 7, 10])),
                    'Taking the largest coin first gives 10 + 1 + 1 + 1 + 1 (5 coins), but 7 + 7 uses 2, and no single coin '
                    'is worth 14.', compute=lambda: str(fewest_coins(14, [1, 7, 10]))),
                 tf('Among rectangles with whole-number sides and area 36, the 6 by 6 square has the smallest perimeter.',
                    True, 'Perimeters: 1 x 36: 74, 2 x 18: 40, 3 x 12: 30, 4 x 9: 26, 6 x 6: 24.',
                    check=lambda: min((2 * (w + 36 // w), w) for w in range(1, 37) if 36 % w == 0)[1] == 6),
                 values('Whole numbers a, b and c are each at least 1 and add up to 12. Make the product a x b x c as large as '
                        'possible. Give a, b and c.', [('a', 'a ='), ('b', 'b ='), ('c', 'c =')],
                        'a == 4 and b == 4 and c == 4', {'a': 4, 'b': 4, 'c': 4},
                        'If two of the numbers differ by 2 or more, moving 1 from the larger to the smaller raises the '
                        'product. So all three are equal: 4, 4, 4, product 64.',
                        wrong=[{'a': 3, 'b': 4, 'c': 5}, {'a': 2, 'b': 5, 'c': 5}, {'a': 6, 'b': 6, 'c': 0}],
                        method='Checked all triples: the largest product is %d, reached only at (4, 4, 4).'
                        % max(a * b * (12 - a - b) for a in range(1, 11) for b in range(1, 12 - a))),
                 mc('Use each of the digits 1, 2, 3 and 4 once to make two 2-digit numbers. Which pair has the largest '
                    'product?', '41 x 32', [('42 x 31', '42 x 31 = 1302, less than 1312'),
                                           ('43 x 21', '43 x 21 = 903'), ('31 x 24', '31 x 24 = 744')],
                    'The tens digits should be 4 and 3. Then 41 x 32 = 1312 beats 42 x 31 = 1302: the extra unit goes '
                    'with the smaller tens digit.',
                    check=lambda t: (lambda a, b: a * b)(*[int(x) for x in t.split(' x ')]) == best_pair()),
             ]))


KNAP = {'Tent': (6, 8), 'Stove': (4, 5), 'Food': (5, 6), 'Lamp': (1, 3)}


def knap_ok(names):
    return sum(KNAP[n][0] for n in names) <= 10


def knap_value(text):
    names = [w.strip().capitalize() for w in text.split(',')]
    return sum(KNAP[n][1] for n in names) if knap_ok(names) else -1


def best_pair():
    return max(int(p[0] + p[1]) * int(p[2] + p[3]) for p in itertools.permutations('1234'))


def greedy(t, coins):
    n = 0
    for c in coins:
        n += t // c
        t %= c
    return n


SETS = [s49(), s50(), s51()]
