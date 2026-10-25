"""Logic sets 2-5: reading exactly what is stated; statements and arguments; elimination; negation."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def models(var_ranges, cond):
    names = list(var_ranges)
    return [dict(zip(names, v)) for v in itertools.product(*[var_ranges[k] for k in names]) if cond(dict(zip(names, v)))]


def must(ms, f):
    return all(f(m) for m in ms)


# ------------------------------------------------------------------ Set 2: precise reading
PENS = models({'r': range(0, 7), 'b': range(0, 7)}, lambda m: m['r'] >= 3 and m['b'] <= 2 and m['r'] + m['b'] == 6)
PENS_CH = {'There are at least 4 red pens.': lambda m: m['r'] >= 4, 'There are exactly 3 red pens.': lambda m: m['r'] == 3,
           'There are exactly 2 blue pens.': lambda m: m['b'] == 2, 'There are no blue pens.': lambda m: m['b'] == 0}

BAG = models({'r': range(0, 11), 'b': range(0, 11)}, lambda m: m['r'] >= 2 * m['b'] and m['r'] + m['b'] <= 10 and m['b'] >= 3)


def s2():
    return S(2, 'Read negations, units and relationships exactly as stated',
             main=[
                 mc('Three students each make one statement about themself, and every statement is true. Dee: "It is not '
                    'true that I finished the race." Eli: "I did not fail to finish the race." Fay: "I never said that I '
                    'finished the race." Who definitely finished the race?', 'Eli only',
                    [('Dee only', '"It is not true that I finished" means Dee did not finish'),
                     ('Eli and Fay', 'Fay only says what she never SAID; that tells us nothing about whether she finished'),
                     ('Dee and Fay', 'Dee did not finish, and nothing is known about Fay')],
                    'Eli: "did not fail to finish" is a double negative, so Eli finished. Dee denies finishing. Fay\'s statement '
                    'is about what she said, not about the race, so she may or may not have finished. Only Eli definitely did.'),
                 sa('Shoelaces are sold only in packs of 2 laces for $3 a pack. Each sneaker needs exactly one lace. A club '
                    'needs laces for 12 sneakers and also buys 4 whistles at $5 each. What is the least the club can spend, '
                    'in dollars?', 'Dollars:', '38',
                    '12 sneakers need 12 laces = 6 packs, costing 6 x $3 = $18. Whistles cost 4 x $5 = $20. Total $38. A '
                    'common slip is to pay $3 per lace (12 x 3 = $36, total $56).', compute=lambda: str(12 // 2 * 3 + 4 * 5)),
                 sa('The Ortiz family has at least one son and at least one daughter. Each son has exactly one brother, and each daughter has exactly two brothers and '
                    'three sisters. How many children are in the family?', 'Children:', '6',
                    'A son\'s brothers are the other sons, so one brother means 2 sons. A daughter\'s sisters are the other '
                    'daughters, so three sisters means 4 daughters, and each daughter\'s two brothers are the 2 sons. 2 + 4 = 6.',
                    compute=lambda: str(next(s + d for s in range(1, 9) for d in range(1, 9) if s - 1 == 1 and s == 2 and d - 1 == 3))),
                 mc('A box holds only red pens and blue pens: at least 3 red pens, at most 2 blue pens, and exactly 6 pens in '
                    'all. Which statement MUST be true?', 'There are at least 4 red pens.',
                    [('There are exactly 3 red pens.', 'then there would be 3 blue pens, but there are at most 2'),
                     ('There are exactly 2 blue pens.', '1 or 0 blue pens also fit every condition'),
                     ('There are no blue pens.', '1 or 2 blue pens also fit')],
                    'Blue is 0, 1 or 2, so red is 6, 5 or 4: always at least 4. Each other statement fails in at least one of '
                    'these three possible boxes.',
                    method='Automatic: all (red, blue) pairs enumerated: (4, 2), (5, 1), (6, 0).',
                    check=lambda t: must(PENS, PENS_CH[t])),
                 order('On this team, April, June and May are the names of three players (not months). A coach writes: "June '
                       'scored after April and before May." Put the players in the order in which they scored, first to last.',
                       [('A', 'April'), ('J', 'June'), ('M', 'May')],
                       lambda p: p.index('A') < p.index('J') < p.index('M'),
                       'The words are names here, so read the sentence literally: April, then June, then May.',
                       expect=['A', 'J', 'M']),
             ],
             back=[B('Strategy: rewrite each statement in plain form', 'guided_strategy',
                     'Students who miss MAIN usually react to the first impression of a sentence. Rewriting each statement in '
                     'plain form (cancel double negatives, convert units, turn "at least" into a number list) removes the trap.',
                     lesson=lesson('Rewrite each statement in plain form',
                                   ['Before solving, rewrite every statement so that it says one plain thing.',
                                    'Double negatives cancel: "not untrue" means "true", and "did not fail to" means "did".',
                                    'Units: decide whether a number counts items or groups (pairs, packs, dozens) and convert.',
                                    '"At least 3" means 3, 4, 5, ...; "at most 3" means 0, 1, 2 or 3. List the values that are '
                                    'still possible.',
                                    'A sentence about what someone SAID or THINKS is not a fact about the world.'],
                                   'Worked example (a different situation)',
                                   ['"It is not untrue that the library is not open." Is the library open?',
                                    'Eggs come in cartons of a dozen. Pia needs 30 eggs. How many cartons must she buy?'],
                                   ['"Not untrue" means "true", so the sentence says: the library is not open.',
                                    'Cartons hold 12 eggs. 2 cartons give 24 eggs, which is too few; 3 cartons give 36, which '
                                    'is enough. She must buy 3 cartons.']),
                     qs=[
                         mc('Treat "unhappy" as meaning exactly "not happy". What does "Rui is not unhappy" say?', 'Rui is happy.',
                            [('Rui is unhappy.', 'the "not" cancels the "un-"'), ('Rui is sad and tired.', 'nothing is said '
                              'about being tired'), ('Nothing at all about Rui.', 'it is a definite statement about Rui')],
                            '"Not unhappy" = not (not happy) = happy, under the stated meaning.'),
                         sa('A drawer holds 18 single socks that make complete matching pairs. How many pairs is that?',
                            'Pairs:', '9', 'A pair is 2 socks: 18 / 2 = 9.', compute=lambda: str(18 // 2)),
                         tf('"At most 3 people may enter" allows exactly 3 people to enter.', True,
                            '"At most 3" means 3 or fewer, so 3 is allowed.'),
                         mc('"Not all of the doors are locked." Which statement means the same?', 'At least one door is unlocked.',
                            [('No door is locked.', 'that says more: some doors may still be locked'),
                             ('Every door is unlocked.', 'that says more than the sentence'),
                             ('Exactly one door is unlocked.', 'the sentence does not say how many')],
                            '"Not all are locked" is true exactly when at least one door is not locked.'),
                         sa('Lin has 3 brothers. Each of her brothers has exactly one sister. How many children are in the '
                            'family?', 'Children:', '4', 'The brothers\' one sister is Lin herself: 3 brothers + Lin = 4.',
                            compute=lambda: str(3 + 1)),
                     ])],
             f1=FW('Read layered negations, units and family clues', 'Same skill, harder: more layers and more conditions.', [
                 mc('Every statement below is true. Which person is going to the game? Gus: "It is not true that I am not going." '
                    'Hal: "I am not not staying home." Ivy: "It is false that I won\'t go."',
                    'Gus and Ivy',
                    [('Gus only', 'Ivy\'s statement also cancels to "I will go"'), ('Hal and Ivy', 'Hal\'s "not not staying" '
                      'means Hal is staying home'), ('all three', 'Hal is staying home')],
                    'Gus: not (not going) = going. Hal: not (not staying) = staying home. Ivy: false that (won\'t go) = will go.'),
                 sa('Eggs are sold in half-dozen boxes (6 eggs) for $2 a box. A recipe uses 4 eggs per cake, and a baker makes '
                    '9 cakes. What is the least she can spend on eggs, in dollars?', 'Dollars:', '12',
                    '9 cakes x 4 eggs = 36 eggs = 6 boxes. 6 x $2 = $12.', compute=lambda: str(-(-9 * 4 // 6) * 2)),
                 sa('The Novak family has at least one son and at least one daughter. Each son has exactly 3 sisters and 2 brothers. Each daughter has exactly 2 sisters. '
                    'How many children are in the family?', 'Children:', '6',
                    'A son has 2 brothers, so there are 3 sons. A son has 3 sisters, so there are 3 daughters; then each '
                    'daughter has 2 sisters, as stated. 3 + 3 = 6.',
                    compute=lambda: str(next(s + d for s in range(1, 9) for d in range(1, 9) if s - 1 == 2 and d == 3 and d - 1 == 2))),
                 mc('A bag holds only red and blue marbles: at least twice as many red as blue, at least 3 blue, and at most 10 '
                    'marbles in all. Which statement MUST be true?', 'There are exactly 3 blue marbles.',
                    [('There are exactly 6 red marbles.', '7 red and 3 blue also fit'),
                     ('There are exactly 10 marbles.', '6 red and 3 blue (9 marbles) also fit'),
                     ('There are more blue marbles than red ones.', 'red is at least twice blue')],
                    'If blue were 4, red would be at least 8, giving at least 12 marbles: too many. So blue is exactly 3, and '
                    'red is 6 or 7.', method='Automatic: every (red, blue) pair up to 10 enumerated: (6, 3), (7, 3).',
                    check=lambda t: must(BAG, {'There are exactly 3 blue marbles.': lambda m: m['b'] == 3,
                                               'There are exactly 6 red marbles.': lambda m: m['r'] == 6,
                                               'There are exactly 10 marbles.': lambda m: m['r'] + m['b'] == 10,
                                               'There are more blue marbles than red ones.': lambda m: m['b'] > m['r']}[t])),
                 tf('"Only members may vote" means that everyone who votes is a member.', True,
                    '"Only members may vote": if someone votes, that person is a member. It does not say every member votes.'),
             ]),
             f2=FW('Precise reading in multi-step puzzles', 'Expert: combine several precise readings in one problem.', [
                 sa('Four statements: (1) "It is not the case that 7 is not odd." (2) "It is false that 10 is not even." '
                    '(3) "It is not true that 9 is not a multiple of 4." (4) "5 is not unequal to 5." How many of the four '
                    'statements are true?', 'Number true:', '3',
                    '(1) 7 is odd: true. (2) 10 is even: true. (3) says 9 IS a multiple of 4: false. (4) "not unequal" means '
                    'equal: 5 = 5, true. Three are true.',
                    compute=lambda: str(sum([7 % 2 == 1, 10 % 2 == 0, 9 % 4 == 0, 5 == 5]))),
                 order('On a quiz show, Monday, Tuesday, Wednesday and Friday are the first names of four contestants. The host '
                       'says: "Wednesday answered before Monday. Friday answered right after Tuesday. Monday did not answer '
                       'last." Put the contestants in answering order, first to last.',
                       [('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Fr', 'Friday')],
                       lambda p: p.index('We') < p.index('Mo') and p.index('Fr') == p.index('Tu') + 1 and p[-1] != 'Mo',
                       'The words are names. Tuesday and Friday form a block (Tuesday, then Friday). With Wednesday before '
                       'Monday, the possible orders are: block, Wednesday, Monday; Wednesday, block, Monday; Wednesday, Monday, '
                       'block. Monday is not last, so only Wednesday, Monday, Tuesday, Friday remains.',
                       expect=['We', 'Mo', 'Tu', 'Fr']),
                 values('A bag holds only red and blue marbles: the number of red marbles is at least twice the number of blue, '
                        'there are at least 3 blue marbles, and there are at most 10 marbles in all. Give a possible number of '
                        'red marbles r and blue marbles b.', [('r', 'red r ='), ('b', 'blue b =')],
                        'r >= 2*b and b >= 3 and r + b <= 10 and isInteger(r) and isInteger(b)', {'r': 6, 'b': 3},
                        'Blue must be 3 (with 4 blue, red is at least 8, too many in all). Red can be 6 or 7. Either (6, 3) or '
                        '(7, 3) is correct.', wrong=[{'r': 5, 'b': 3}, {'r': 8, 'b': 4}, {'r': 8, 'b': 2}],
                        search={'r': range(0, 11), 'b': range(0, 11)}),
                 sa('In a group of brothers and sisters, every girl has exactly as many brothers as sisters, and there are 3 '
                    'boys. How many girls are there?', 'Girls:', '4',
                    'A girl\'s brothers are the 3 boys; her sisters are the other girls. So girls - 1 = 3, and there are 4 girls.',
                    compute=lambda: str(next(g for g in range(1, 10) if g - 1 == 3))),
                 mc('"No student who did not study passed the test." Which statement follows?', 'Every student who passed '
                    'studied.', [('Every student who studied passed.', 'that reverses the condition'),
                                 ('Some students who studied failed.', 'nothing is said about students who studied'),
                                 ('No student passed.', 'students who studied may have passed')],
                    'The sentence says: if a student did not study, the student did not pass. Equivalently, if a student '
                    'passed, the student studied (the contrapositive).'),
             ]))


# ------------------------------------------------------------------ Set 3: statements and arguments
def s3():
    return S(3, 'Identify statements, premises, conclusions and assumptions',
             main=[
                 mc('"The trail is closed whenever it rains. It is raining now. So the trail is closed." Which sentence is the '
                    'conclusion?', 'The trail is closed.',
                    [('It is raining now.', 'this is given as a reason (a premise)'),
                     ('The trail is closed whenever it rains.', 'this is a general premise'),
                     ('Rain is likely tomorrow.', 'this sentence is not in the argument')],
                    '"So" introduces the conclusion: the trail is closed. The other two sentences are the reasons (premises).'),
                 mc('Which of these is a statement (a sentence that is either true or false)?', 'Every square has four sides.',
                    [('Please close the window.', 'a request is neither true nor false'),
                     ('Is 15 a prime number?', 'a question is neither true nor false'),
                     ('What a great game!', 'an exclamation of feeling is not a claim that is true or false')],
                    'A statement makes a claim that is true or false. "Every square has four sides" is a (true) statement.'),
                 mc('"Since every ticket holder may enter, and Zoe holds a ticket, Zoe may enter." Which sentence is a premise?',
                    'Zoe holds a ticket.',
                    [('Zoe may enter.', 'this is the conclusion the argument reaches'),
                     ('Zoe bought the ticket online.', 'the argument does not say this'),
                     ('Only Zoe may enter.', 'the argument does not say this')],
                    '"Since" introduces the reasons: every ticket holder may enter, and Zoe holds a ticket. The conclusion is '
                    'that Zoe may enter.'),
                 mc('"Ravi will be on time, because the bus left on schedule." Which unstated assumption does this argument '
                    'need?', 'Ravi is on that bus.',
                    [('The bus is red.', 'the color is irrelevant to the conclusion'),
                     ('Ravi was late yesterday.', 'that would not help the conclusion'),
                     ('Some buses are late.', 'that does not connect the bus to Ravi')],
                    'The reason (the bus left on schedule) supports the conclusion only if Ravi is riding it. That missing link '
                    'is the assumption.'),
                 mc('"All of our club\'s robots passed inspection. Unit 7 is one of our club\'s robots. The room is cold. '
                    'Therefore Unit 7 passed inspection." Which sentence plays no part in the reasoning?', 'The room is cold.',
                    [('Unit 7 is one of our club\'s robots.', 'this premise connects Unit 7 to the group'),
                     ('All of our club\'s robots passed inspection.', 'this premise gives the general rule'),
                     ('Therefore Unit 7 passed inspection.', 'this is the conclusion')],
                    'The conclusion follows from the first two sentences. The temperature of the room is irrelevant.'),
             ],
             back=[
                 B('Which sentences are statements?', 'prerequisite',
                   'An argument is built from statements. A student who treats questions, commands or exclamations as claims '
                   'cannot sort premises from conclusions.', qs=[
                       tf('"Close the door." is a statement.', False, 'It is a command; it is neither true nor false.'),
                       tf('"7 is greater than 9." is a statement.', True, 'It is false, but it is still a statement: it makes '
                                                                         'a claim that is true or false.'),
                       mc('Which is NOT a statement?', 'Who won the game?',
                          [('The game ended in a tie.', 'a claim that is true or false'),
                           ('Nobody scored.', 'a claim that is true or false'),
                           ('Our team won.', 'a claim that is true or false')],
                          'A question asks; it does not claim.'),
                       tf('"x + 2 = 5" with no value of x given is a statement.', False,
                          'Its truth depends on x, which is not given; it becomes a statement once x is fixed (an open sentence).'),
                       mc('Which sentence is a statement?', 'Paris is in Spain.',
                          [('Let\'s go to Paris!', 'a suggestion'), ('Is Paris far?', 'a question'),
                           ('Visit Paris.', 'a command')], 'It is a false claim, but a claim: a statement.'),
                   ]),
                 B('Find the conclusion by its signal words', 'prerequisite',
                   'Students who reverse premise and conclusion usually ignore the signal words. "So, therefore, thus" point '
                   'to the conclusion; "because, since, given that" point to the reasons.', qs=[
                       mc('Which word usually introduces a conclusion?', 'therefore',
                          [('because', 'introduces a reason'), ('since', 'introduces a reason'),
                           ('given that', 'introduces a reason')], '"Therefore" signals the conclusion.'),
                       mc('Which word usually introduces a reason (a premise)?', 'because',
                          [('so', 'introduces a conclusion'), ('thus', 'introduces a conclusion'),
                           ('consequently', 'introduces a conclusion')], '"Because" signals a reason.'),
                       mc('"The lake is frozen, so we can skate." What is the conclusion?', 'We can skate.',
                          [('The lake is frozen.', 'the reason'), ('It is winter.', 'not stated'),
                           ('Skating is fun.', 'not stated')], '"So" introduces the conclusion.'),
                       mc('"We should leave now, since the show starts at 7." What is the conclusion?', 'We should leave now.',
                          [('The show starts at 7.', 'the reason, after "since"'), ('The show is long.', 'not stated'),
                           ('We are late.', 'not stated')], 'The claim supported by the "since" reason is the conclusion.'),
                       tf('In "Because the battery is dead, the car will not start," the conclusion is "the battery is dead."',
                          False, '"Because" marks the reason; the conclusion is that the car will not start.'),
                   ]),
             ],
             f1=FW('Arguments with several premises and hidden structure', 'Same skill, harder: longer arguments, '
                                                                           'conclusions in the middle, ordering steps.', [
                 mc('"The museum must be open today. After all, it is open every weekday except Monday, and today is '
                    'Thursday." Which sentence is the conclusion?', 'The museum must be open today.',
                    [('Today is Thursday.', 'a premise'), ('It is open every weekday except Monday.', 'a premise'),
                     ('The museum is closed on Monday.', 'part of a premise, not the claim being supported')],
                    'The first sentence is supported by the other two ("after all" introduces reasons).'),
                 order('Put these sentences in the order of a clear argument: the general rule first, then the fact, then the '
                       'conclusion.', [('A', 'Therefore, 91 is not prime.'), ('B', 'Any whole number greater than 1 with a '
                                                                                 'factor other than 1 and itself is not prime.'),
                                       ('C', '91 = 7 x 13, so 91 has the factor 7.')],
                       lambda p: list(p) == ['B', 'C', 'A'],
                       'Rule (B), fact about 91 (C), then the conclusion (A).', expect=['B', 'C', 'A']),
                 mc('"Coach Lee will pick Maya, because Coach Lee always picks the fastest runner." Which assumption is needed?',
                    'Maya is the fastest runner.', [('Maya wants to be picked.', 'not needed for the conclusion'),
                                                    ('Coach Lee likes Maya.', 'not what the argument relies on'),
                                                    ('Maya ran yesterday.', 'irrelevant to being the fastest')],
                    'The rule talks about the fastest runner; the conclusion needs Maya to be that runner.'),
                 tf('An argument can have a true conclusion even when one of its premises is false.', True,
                    'For example: "All fish can fly; a pigeon is a fish; so a pigeon can fly." The premises are false, the '
                    'conclusion is true.'),
                 mc('"If the alarm is set, it rings at 6. It did not ring at 6. Hence it was not set." How many premises does '
                    'this argument have?', '2', [('1', 'there are two reasons before "hence"'),
                                                ('3', 'the third sentence is the conclusion'),
                                                ('0', 'the first two sentences are reasons')],
                    'Two premises (the conditional and the fact that it did not ring), and one conclusion after "hence".'),
             ]),
             f2=FW('Evaluate structure and missing links', 'Expert: find the exact missing premise among close options.', [
                 mc('"All sprinters on the team train daily. So Kim trains daily." Which added premise makes the conclusion '
                    'follow for certain?', 'Kim is a sprinter on the team.',
                    [('Kim trains often.', 'does not make Kim a sprinter on the team'),
                     ('Some sprinters train daily.', 'the conclusion is about Kim, who is still not linked to the group'),
                     ('Kim is on the team.', 'Kim might be on the team but not a sprinter')],
                    'The general premise is about sprinters on the team; Kim must be one of them.'),
                 mc('"Every number divisible by 6 is even. So 84 is even." Which added premise makes this valid?',
                    '84 is divisible by 6.', [('84 is divisible by 7.', 'true, but divisibility by 7 says nothing about being even'),
                                             ('84 is greater than 6.', 'size does not matter'),
                                             ('Some even numbers are divisible by 6.', 'still says nothing about 84')],
                    'The rule applies to numbers divisible by 6, so we need 84 to be one: 84 = 6 x 14.'),
                 tf('In a valid argument, adding an extra true premise can make the conclusion no longer follow.', False,
                    'If the conclusion follows from some premises, it still follows when more premises are added.'),
                 order('Arrange these sentences into an argument. Put the dam-to-river rule before the river-to-ferry rule, and put '
                       'the conclusion last.',
                       [('A', 'If the dam opens, the river rises.'), ('B', 'If the river rises, the ferry stops.'),
                        ('C', 'The dam opens.'), ('D', 'So the ferry stops.')],
                       lambda p: p[-1] == 'D' and p.index('A') < p.index('B'),
                       'The rules must appear in the stated order and the conclusion last; the fact "The dam opens" may '
                       'come anywhere before the conclusion, so three orders are accepted.', expect=['C', 'A', 'B', 'D']),
                 mc('"Our new ads worked: sales rose this month." Which assumption is the argument making?',
                    'Nothing other than the ads caused most of the rise in sales.',
                    [('Sales rose this month.', 'that is the stated premise, not an assumption'),
                     ('The ads were expensive.', 'cost is irrelevant to whether they worked'),
                     ('Sales will rise next month.', 'the argument is about this month')],
                    'Claiming the ads "worked" assumes the rise was due to the ads and not to something else.'),
             ]))


# ------------------------------------------------------------------ Set 4: elimination
def survivors(cands, clues):
    return [c for c in cands if all(f(c) for f in clues)]


M4_CLUES = [lambda m: len(m) < 8, lambda m: 'r' in m.lower(), lambda m: MONTHS.index(m) % 2 == 0,
            lambda m: not m.startswith('J')]
M4 = survivors(MONTHS, M4_CLUES)
assert M4 == ['March'], M4
D4 = survivors(DAYS, [lambda d: 'e' not in d, lambda d: DAYS.index(d) > 2, lambda d: len(d) == 6, lambda d: 'u' in d])
assert D4 == ['Sunday'], D4
N4 = survivors(range(1, 51), [lambda n: n % 7 == 3, lambda n: n > 20, lambda n: n % 2 == 0, lambda n: n % 5 != 4])
assert N4 == [38], N4

# the month puzzle for F1: neighbor-month clues
def nb(m, d):
    return MONTHS[(MONTHS.index(m) + d) % 12]


F1M = survivors(MONTHS, [lambda m: len(nb(m, -1)) > 5, lambda m: not nb(m, 1).endswith('ber'),
                         lambda m: 'u' in nb(m, 1).lower(), lambda m: 'a' in m.lower()])
assert F1M == ['January'], F1M

F2CLUES = {'A': lambda n: n % 2 == 1, 'B': lambda n: n % 3 == 0, 'C': lambda n: n > 10, 'D': lambda n: n % 5 == 0}
F2_ALL = survivors(range(1, 31), F2CLUES.values())
assert F2_ALL == [15], F2_ALL
F2_REMOVABLE = [k for k in F2CLUES if len(survivors(range(1, 31), [f for j, f in F2CLUES.items() if j != k])) == 1]


def s4():
    return S(4, 'Find the only candidate left after every clue',
             main=[
                 mc('Which month is it? Its name has fewer than 8 letters. Its name contains the letter R. It is the 1st, 3rd, '
                    '5th, 7th, 9th or 11th month. Its name does not start with J.', 'March',
                    [('January', 'starts with J'), ('May', 'has no R'), ('September', 'has 9 letters')],
                    'Fewer than 8 letters and an R: January, March, April, October. Odd-numbered month (1st, 3rd, ...): '
                    'January, March. Not starting with J: March.',
                    method='Automatic: the four clues applied to all 12 months leave only March.', check=lambda m: m in M4),
                 mc('Which day of the week is it? Its name has no letter E. It comes after Wednesday in the week that starts on '
                    'Monday. Its name has exactly 6 letters. Its name contains the letter U.', 'Sunday',
                    [('Friday', 'fits the first three clues but has no letter U'),
                     ('Saturday', 'has 8 letters'), ('Thursday', 'has 8 letters')],
                    'After Wednesday: Thursday, Friday, Saturday, Sunday (none has an E). Exactly 6 letters: Friday, Sunday. '
                    'Contains a U: Sunday.', method='Automatic: the four clues applied to all 7 days leave only Sunday.',
                    check=lambda d: d in D4),
                 sa('A whole number from 1 to 50 leaves remainder 3 when divided by 7. It is greater than 20. It is even. It '
                    'does not leave remainder 4 when divided by 5. What is the number?', 'Number:', '38',
                    'Remainder 3 mod 7: 3, 10, 17, 24, 31, 38, 45. Greater than 20: 24, 31, 38, 45. Even: 24, 38. 24 leaves '
                    'remainder 4 when divided by 5, so the number is 38.', compute=lambda: str(N4[0])),
                 grid('Three friends, Ana, Ben and Cai, each have exactly one pet: a cat, a dog or a fish, all different. Ana '
                      'does not have the dog. Ben has neither the cat nor the dog. Which pet does each friend have?',
                      ['Ana', 'Ben', 'Cai'], ['cat', 'dog', 'fish'],
                      lambda a: a['Ana'] != 'dog' and a['Ben'] not in ('cat', 'dog'),
                      'Ben has neither cat nor dog, so Ben has the fish. Ana does not have the dog, so Ana has the cat, and Cai '
                      'has the dog.'),
                 mc('A locker number is one of 12, 15, 18, 21, 24, 27. It is even. It is not a multiple of 4. Which locker is it?', '18',
                    [('27', '27 is odd, so it is not even'), ('12', 'a multiple of 4'), ('24', 'a multiple of 4')],
                    'Even: 12, 18, 24. Not a multiple of 4: 18.',
                    check=lambda t: int(t) % 2 == 0 and int(t) % 4 != 0),
             ],
             back=[B('Strategy: cross out, one clue at a time', 'guided_strategy',
                     'Students who guess usually try to hold all clues in mind. Writing the full candidate list and crossing '
                     'out what each clue rules out makes the elimination complete and checkable.',
                     lesson=lesson('Cross out, one clue at a time',
                                   ['Write down every candidate first: all 12 months, all 7 days, every number in range.',
                                    'Apply ONE clue at a time and cross out every candidate it rules out. Do not skip a '
                                    'candidate because it "seems" unlikely.',
                                    'When the clues are done, exactly one candidate should be left. If more than one is left, '
                                    'the clues are not enough; if none is left, recheck the work.'],
                                   'Worked example (a different list)',
                                   ['A number from 1 to 20: it is a multiple of 3; it is odd; it is greater than 10.'],
                                   ['Multiples of 3: 3, 6, 9, 12, 15, 18.', 'Odd: 3, 9, 15.', 'Greater than 10: 15.',
                                    'Exactly one is left, so the number is 15.']),
                     qs=[
                         sa('A number from 1 to 10 is even, greater than 7 and less than 10. What is it?', 'Number:', '8',
                            'Even: 2, 4, 6, 8, 10. Greater than 7: 8, 10. Less than 10: 8.',
                            compute=lambda: str([n for n in range(1, 11) if n % 2 == 0 and 7 < n < 10][0])),
                         mc('A day of the week (Monday to Sunday) starts with T and has more than 7 letters. Which day?',
                            'Thursday', [('Tuesday', 'has exactly 7 letters'), ('Saturday', 'does not start with T'),
                                         ('Wednesday', 'does not start with T')], 'T-days: Tuesday (7), Thursday (8).'),
                         sa('How many months have a name with exactly 4 letters?', 'Months:', '2', 'June and July.',
                            compute=lambda: str(sum(len(m) == 4 for m in MONTHS))),
                         tf('If two candidates are left after every clue, the clues determine the answer.', False,
                            'Two candidates fit every clue, so the answer is not determined.'),
                         mc('Candidates: 2, 3, 4, 5, 6. Clue 1: the number is prime. Clue 2: the number is odd. How many '
                            'candidates are left?', '2', [('1', '3 and 5 are both odd primes'), ('3', '2 is prime but even'),
                                                          ('0', '3 and 5 fit')], 'Primes: 2, 3, 5. Odd: 3, 5.'),
                     ])],
             f1=FW('Eliminate with clues about neighbors and positions', 'Harder: clues about the month before or after, and '
                                                                        'two-way clues.', [
                 mc('Which month is it? The month before it has a name longer than 5 letters. The month after it does not end '
                    'in "ber". The month after it contains the letter U. Its own name contains the letter A.', 'January',
                    [('December', 'fits the three neighbor clues but has no letter A'),
                     ('February', 'the month after it, March, has no letter U'),
                     ('May', 'the month before it, April, has only 5 letters')],
                    'Months whose previous month has more than 5 letters: January, February, March, September, October, '
                    'November, December. Next month not ending in "ber": January, February, March, December. Next month '
                    'containing U: January (February) and December (January). Own name with an A: January.',
                    method='Automatic: all 12 months tested against the four neighbor clues.', check=lambda m: m in F1M),
                 tf('In the week Monday to Sunday, exactly one day has a name whose day before and day after both contain the '
                    'letter T.', False, 'Two days qualify: Wednesday (Tuesday and Thursday) and Friday (Thursday and '
                                        'Saturday).',
                    check=lambda: sum(1 for i, d in enumerate(DAYS) if 't' in DAYS[i - 1].lower() and 't' in DAYS[(i + 1) % 7].lower()) == 1),
                 sa('A whole number from 1 to 100 is a perfect square, is odd, has two digits, and its digits add to 13. What '
                    'is it?', 'Number:', '49', 'Odd two-digit squares: 25, 49, 81. Digit sums 7, 13, 9. So 49.',
                    compute=lambda: str([n for n in range(10, 100) if int(n ** .5) ** 2 == n and n % 2 and sum(map(int, str(n))) == 13][0])),
                 grid('Four runners, Dev, Eva, Finn and Gia, finished 1st to 4th, no ties. Eva finished right after Dev. Gia '
                      'finished before Finn. Finn finished before Dev. Assign each runner a place.', ['Dev', 'Eva', 'Finn', 'Gia'],
                      ['1st', '2nd', '3rd', '4th'],
                      lambda a: (int(a['Eva'][0]) == int(a['Dev'][0]) + 1 and int(a['Gia'][0]) < int(a['Finn'][0])
                                 and int(a['Finn'][0]) < int(a['Dev'][0])),
                      'Gia is before Finn and Finn before Dev, so Dev is at least 3rd; Eva is right after Dev, so Dev is 3rd '
                      'and Eva 4th. Then Gia is 1st and Finn 2nd.'),
                 mc('Candidates are the whole numbers 1 to 30. Clues: A: the number is odd. B: it is a multiple of 3. C: it is '
                    'greater than 10. D: it is a multiple of 5. Which number fits all four clues?', '15',
                    [('30', 'even, so it fails clue A'), ('5', 'not a multiple of 3 and not greater than 10'),
                     ('25', 'not a multiple of 3')], 'Odd multiples of 15 up to 30: 15 only.', check=lambda t: int(t) in F2_ALL),
             ]),
             f2=FW('Which clues are really needed?', 'Expert: find unnecessary clues and the least information that still '
                                                    'determines the answer.', [
                 mc('Candidates are the whole numbers 1 to 30, with four clues: A: odd; B: a multiple of 3; C: greater than 10; '
                    'D: a multiple of 5. Only 15 fits all four. Which ONE clue can be removed so that exactly one number is still left?',
                    'C (greater than 10)', [('B (multiple of 3)', 'without B, 15 and 25 both fit'),
                                           ('A (odd)', 'without A, 15 and 30 both fit'),
                                           ('D (multiple of 5)', 'without D, 15, 21 and 27 fit')],
                    'Remove each clue in turn and recount. Without C the clues say: odd, multiple of 3 and multiple of 5, '
                    'that is an odd multiple of 15, and the only one up to 30 is 15. Removing any other clue leaves two or more '
                    'numbers.', method='Automatic: each clue removed in turn and the survivors recounted.',
                    check=lambda t: t[0] in F2_REMOVABLE),
                 sa('A number from 1 to 30 is a multiple of 4. What is the least number of extra yes/no questions of the form '
                    '"Is it greater than k?" that always identify it?', 'Questions:', '3',
                    'Multiples of 4 up to 30: 4, 8, 12, 16, 20, 24, 28 (7 candidates). Each question at best halves the list, '
                    'so 2 questions separate at most 4; 3 questions separate up to 8, and halving 7 -> 4 -> 2 -> 1 works.',
                    compute=lambda: str(next(q for q in range(10) if 2 ** q >= len(range(4, 31, 4))))),
                 tf('Adding a new clue to a puzzle can never increase the number of candidates left.', True,
                    'Each clue only removes candidates; the survivors of more clues are a subset of the survivors of fewer.'),
                 values('Candidates are the whole numbers 1 to 20. Write a number n that survives BOTH clues: n is prime, and n '
                        'leaves remainder 1 when divided by 4.', [('n', 'n =')],
                        'isPrime(n) and n % 4 == 1 and n >= 1 and n <= 20', {'n': 5},
                        'Primes up to 20 leaving remainder 1 mod 4: 5, 13, 17. Any one is correct.',
                        wrong=[{'n': 9}, {'n': 7}, {'n': 21}], search={'n': range(1, 21)}),
                 mc('Six boxes are numbered 1 to 6. One holds a prize. Which single clue, added alone, would leave exactly one '
                    'box?', '"The box number is prime and even."', [('"The box number is odd."', 'leaves 1, 3, 5'),
                                                                    ('"The box number is less than 4."', 'leaves 1, 2, 3'),
                                                                    ('"The box number is a multiple of 3."', 'leaves 3 and 6')],
                    'The only even prime is 2.',
                    check=lambda t: len([b for b in range(1, 7) if {
                        '"The box number is prime and even."': b == 2,
                        '"The box number is odd."': b % 2 == 1,
                        '"The box number is less than 4."': b < 4,
                        '"The box number is a multiple of 3."': b % 3 == 0}[t]]) == 1),
             ]))


SETS = [s2(), s3(), s4()]
