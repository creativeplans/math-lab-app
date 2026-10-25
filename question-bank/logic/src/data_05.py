"""Logic sets 13-18: necessary and sufficient; logic grids; converse, inverse, contrapositive; biconditionals;
truth-tellers and liars; truth tables."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt

TF = [True, False]


def imp(p, q):
    return (not p) or q


def iff(p, q):
    return p == q


def nums(n=200):
    return range(1, n + 1)


def necessary(cond, target, dom=nums()):
    """cond is necessary for target: every n with target(n) has cond(n)."""
    return all(cond(n) for n in dom if target(n))


def sufficient(cond, target, dom=nums()):
    return all(target(n) for n in dom if cond(n))


# ------------------------------------------------------------------ Set 13: necessary and sufficient
DIV6 = lambda n: n % 6 == 0
NEC6 = {'n is even': lambda n: n % 2 == 0, 'n is divisible by 12': lambda n: n % 12 == 0,
        'n is divisible by 9': lambda n: n % 9 == 0, 'n ends in the digit 6': lambda n: n % 10 == 6}
SUF4 = {'n is divisible by 8': lambda n: n % 8 == 0, 'n is even': lambda n: n % 2 == 0,
        'n is divisible by 2 and by 3': lambda n: n % 6 == 0, 'n is greater than 4': lambda n: n > 4}


def s13():
    return S(13, 'Translate "only if", "unless", "necessary" and "sufficient"',
             main=[
                 mc('"Being at least 16 years old is NECESSARY for getting a driving permit in this town." Which conditional '
                    'says the same thing?', 'If a person has a driving permit, then the person is at least 16.',
                    [('If a person is at least 16, then the person has a driving permit.', 'this makes age sufficient, which '
                                                                                            'was not claimed'),
                     ('If a person is under 16, then the person may still get a permit.', 'this contradicts the statement'),
                     ('A person is at least 16 and has a permit.', 'not a conditional')],
                    'A necessary condition is required: whoever has the permit must meet it. "B is necessary for A" means "if A, '
                    'then B".'),
                 mc('"You may enter the museum only if you have a ticket." Which statement means the same?',
                    'If you enter the museum, then you have a ticket.',
                    [('If you have a ticket, then you may enter the museum.', '"only if" does not say a ticket is enough'),
                     ('If you have no ticket, then you may still enter.', 'that contradicts the rule'),
                     ('You have a ticket and you enter.', 'not a conditional')],
                    '"A only if B" means "if A, then B".'),
                 mc('In logic, "P unless Q" means "if not Q, then P". Which statement means the same as "The picnic is held '
                    'unless it rains"?', 'If it does not rain, the picnic is held.',
                    [('If it rains, the picnic is held.', 'swaps the condition'),
                     ('If the picnic is held, it does not rain.', 'that is the converse of the stated meaning'),
                     ('If it does not rain, the picnic is not held.', 'adds a negation')],
                    'With the stated meaning: if it does not rain, then the picnic is held.'),
                 tf('Being a square is a NECESSARY condition for being a rectangle.', False,
                    'A 2 by 5 rectangle is not a square, so a shape can be a rectangle without being a square. Being a square is sufficient, not necessary.'),
                 mc('n is a whole number. Which condition is NECESSARY for "n is divisible by 6"?', 'n is even',
                    [('n is divisible by 12', 'sufficient but not necessary: 6 is divisible by 6 but not by 12'),
                     ('n is divisible by 9', '12 is divisible by 6 but not by 9'),
                     ('n ends in the digit 6', '12 is divisible by 6 but ends in 2')],
                    'Every multiple of 6 is even, so being even is required (necessary). It is not sufficient: 4 is even.',
                    method='Automatic: each condition tested against every n from 1 to 200.',
                    check=lambda t: necessary(NEC6[t], DIV6)),
             ],
             back=[
                 B('Write a statement as "if ..., then ..."', 'prerequisite',
                   'Necessary and sufficient conditions are both stated as conditionals. A student must first rewrite '
                   'everyday sentences in if-then form.', outcome='LOGIC.CONDITIONAL.01', qs=[
                       mc('Rewrite "All birds have feathers" as a conditional.', 'If an animal is a bird, then it has feathers.',
                          [('If an animal has feathers, then it is a bird.', 'parts swapped'),
                           ('If an animal is not a bird, then it has no feathers.', 'changes the meaning'),
                           ('Birds and feathers.', 'not a statement')], '"All A are B" means "if A, then B".'),
                       mc('Rewrite "When the bell rings, class ends" as a conditional.', 'If the bell rings, then class ends.',
                          [('If class ends, then the bell rings.', 'parts swapped'), ('The bell rings and class ends.', 'not a '
                                                                                                                 'conditional'),
                           ('If the bell does not ring, class does not end.', 'changes the meaning')],
                          '"When" introduces the condition.'),
                       tf('"If x = 2, then x + x = 4" has hypothesis "x + x = 4".', False, 'The hypothesis is the part after "if", which is "x = 2". "x + x = 4" is the conclusion.'),
                       mc('What is the conclusion of "If a number ends in 5, it is divisible by 5"?', 'it is divisible by 5',
                          [('a number ends in 5', 'the hypothesis'), ('it is odd', 'not stated'), ('it is 5', 'not stated')],
                          'The "then" part.'),
                       tf('"Every even number is divisible by 2" can be written "If a number is even, then it is divisible by 2".',
                          True, '"Every A is B" = "if A, then B".'),
                   ]),
                 B('Necessary means required; sufficient means enough', 'prerequisite',
                   'Students who mix up "required" and "enough" reverse every translation. Everyday examples fix the meaning.',
                   qs=[
                       tf('Having fuel is the only thing a gas car needs in order to run.', False, 'A car with fuel can still fail to run, for example with a dead battery. Fuel is necessary, not sufficient.'),
                       tf('Having fuel is sufficient for a gas car to run.', False, 'A car with fuel may still not run (for '
                                                                                   'example, a dead battery).'),
                       mc('Which is SUFFICIENT for a whole number to be even?', 'It is a multiple of 10.',
                          [('It is greater than 2.', '3 is greater than 2 and odd'), ('It is a multiple of 3.', '3 is odd'),
                           ('It ends in 1.', 'such numbers are odd')], 'Every multiple of 10 is even.',
                          check=lambda t: sufficient({'It is a multiple of 10.': lambda n: n % 10 == 0,
                                                      'It is greater than 2.': lambda n: n > 2,
                                                      'It is a multiple of 3.': lambda n: n % 3 == 0,
                                                      'It ends in 1.': lambda n: n % 10 == 1}[t], lambda n: n % 2 == 0)),
                       tf('If A is sufficient for B, then whenever B happens, A happens.', False, 'Sufficient means A guarantees '
                          'B. B can still happen without A.'),
                       mc('Being a mammal is ___ for being a dog.', 'necessary', [('sufficient', 'a cat is a mammal but not a '
                                                                                                 'dog'),
                                                                                  ('neither necessary nor sufficient', 'every '
                                                                                                                      'dog '
                                                                                                                      'is a '
                                                                                                                      'mammal'),
                                                                                  ('both necessary and sufficient', 'not '
                                                                                                                    'sufficient')],
                          'Every dog is a mammal (required), but not every mammal is a dog.'),
                   ]),
             ],
             f1=FW('Combine conditions', 'Harder: conditions that are necessary but not sufficient, and the reverse.', [
                 values('"n is even" is necessary for "n is divisible by 6". Give a whole number n that shows it is NOT '
                        'sufficient: n is even but not divisible by 6.', [('n', 'n =')],
                        'isEven(n) and n % 6 != 0 and isInteger(n)', {'n': 4},
                        'Any even number that is not a multiple of 6: 2, 4, 8, 10, ...', wrong=[{'n': 6}, {'n': 12}, {'n': 3}]),
                 mc('n is a whole number. Which condition is SUFFICIENT for "n is divisible by 4"?', 'n is divisible by 8',
                    [('n is even', '2 is even but not divisible by 4'), ('n is divisible by 2 and by 3', '6 is not '
                                                                                                         'divisible by 4'),
                     ('n is greater than 4', '5 is not divisible by 4')],
                    'Every multiple of 8 is a multiple of 4.', method='Automatic: tested for every n from 1 to 200.',
                    check=lambda t: sufficient(SUF4[t], lambda n: n % 4 == 0)),
                 mc('"A triangle is equilateral only if it is isosceles (has at least two equal sides)." Which statement is '
                    'correct?', 'Being isosceles is necessary for being equilateral.',
                    [('Being isosceles is sufficient for being equilateral.', 'a 5-5-8 triangle is isosceles, not equilateral'),
                     ('Being equilateral is necessary for being isosceles.', 'reverses the relation'),
                     ('The two conditions mean the same thing.', 'they do not')],
                    '"A only if B": B is necessary for A.'),
                 mc('"You get the discount unless you pay late." Using "P unless Q" = "if not Q, then P", which person is '
                    'guaranteed the discount?', 'someone who did not pay late',
                    [('someone who paid late', 'the statement promises nothing to late payers'),
                     ('everyone', 'late payers are not covered'), ('no one', 'on-time payers are covered')],
                    'If you did not pay late, you get the discount.'),
                 tf('A condition can be both necessary and sufficient for another.', True,
                    'For example, for a whole number, "ends in 0 or 5" is necessary and sufficient for "divisible by 5".'),
             ]),
             f2=FW('Chains of conditions', 'Expert: combine several necessary and sufficient conditions.', [
                 mc('Facts: A is sufficient for B. B is sufficient for C. Which statement must be true?',
                    'C is necessary for A.', [('A is necessary for C.', 'C can hold without A'),
                                              ('B is sufficient for A.', 'reverses the first fact'),
                                              ('C is sufficient for A.', 'reverses the chain')],
                    'A -> B -> C, so A -> C: C is necessary for A (and A is sufficient for C).',
                    method='Automatic: all 8 truth assignments of A, B, C checked.',
                    check=lambda t: all({'C is necessary for A.': imp(a, c), 'A is necessary for C.': imp(c, a),
                                         'B is sufficient for A.': imp(b, a), 'C is sufficient for A.': imp(c, a)}[t]
                                        for a, b, c in itertools.product(TF, repeat=3) if imp(a, b) and imp(b, c))),
                 sa('For whole numbers n from 1 to 60, condition X: "n is divisible by 4"; condition Y: "n is divisible by 6". '
                    'How many n satisfy Y but not X (showing X is not necessary for Y)?', 'Count:', '5',
                    'Multiples of 6 up to 60: 10 numbers. Those also divisible by 4 are multiples of 12: 5. So 10 - 5 = 5.',
                    compute=lambda: str(sum(1 for n in range(1, 61) if n % 6 == 0 and n % 4 != 0))),
                 mc('Which condition on a whole number n is BOTH necessary and sufficient for "n is divisible by 10"?',
                    'n is divisible by 2 and by 5', [('n is divisible by 5', 'not sufficient: 15'),
                                                     ('n is even', 'not sufficient: 4'),
                                                     ('n is divisible by 20', 'not necessary: 10')],
                    'A number is divisible by 10 exactly when it is divisible by both 2 and 5.',
                    check=lambda t: (lambda f: necessary(f, lambda n: n % 10 == 0) and sufficient(f, lambda n: n % 10 == 0))(
                        {'n is divisible by 2 and by 5': lambda n: n % 2 == 0 and n % 5 == 0,
                         'n is divisible by 5': lambda n: n % 5 == 0, 'n is even': lambda n: n % 2 == 0,
                         'n is divisible by 20': lambda n: n % 20 == 0}[t])),
                 tf('If A is necessary for B and B is necessary for A, then A and B are always both true or both false.', True,
                    'B -> A and A -> B together mean A and B have the same truth value.'),
                 values('Give a whole number n for which "n is a multiple of 3" holds but "n is a multiple of 9" fails, '
                        'showing that being a multiple of 3 is not sufficient for being a multiple of 9.',
                        [('n', 'n =')], 'n % 3 == 0 and n % 9 != 0 and isInteger(n)', {'n': 6},
                        'Any multiple of 3 that is not a multiple of 9: 3, 6, 12, 15, ...',
                        wrong=[{'n': 9}, {'n': 18}, {'n': 4}]),
             ]))


# ------------------------------------------------------------------ Set 14: logic grids
def r(a, x):
    return int(a[x])


def s14():
    return S(14, 'Solve a matching puzzle by combining clues',
             main=[
                 grid('Three students, Ama, Bex and Cho, each play one instrument: drums, flute or violin (all different). '
                      'Ama does not play the flute. Bex plays neither the drums nor the flute. Which instrument does each '
                      'student play?', ['Ama', 'Bex', 'Cho'], ['drums', 'flute', 'violin'],
                      lambda a: a['Ama'] != 'flute' and a['Bex'] not in ('drums', 'flute'),
                      'Bex plays the violin (not drums, not flute). Ama does not play the flute, so Ama plays the drums, and '
                      'Cho plays the flute.'),
                 grid('Four friends, Dara, Eli, Faye and Gus, each ordered a different drink: cocoa, juice, milk or tea. Dara '
                      'did not order a hot drink (cocoa and tea are hot). Eli ordered tea. Faye ordered neither cocoa nor juice. '
                      'Who ordered what?', ['Dara', 'Eli', 'Faye', 'Gus'], ['cocoa', 'juice', 'milk', 'tea'],
                      lambda a: a['Dara'] not in ('cocoa', 'tea') and a['Eli'] == 'tea' and a['Faye'] not in ('cocoa', 'juice'),
                      'Eli: tea. Faye: not cocoa, not juice, not tea, so milk. Dara: not hot, so juice. Gus: cocoa.'),
                 grid('Four runners wore bibs 1, 2, 3 and 4 (all different): Hal, Ivy, Jun and Kit. Ivy\'s number is twice '
                      'Hal\'s. Hal\'s number is even. Jun\'s number is odd. Kit\'s number is greater than Jun\'s. What number did '
                      'each runner wear?',
                      ['Hal', 'Ivy', 'Jun', 'Kit'], ['1', '2', '3', '4'],
                      lambda a: (r(a, 'Ivy') == 2 * r(a, 'Hal') and r(a, 'Hal') % 2 == 0 and r(a, 'Jun') % 2 == 1
                                 and r(a, 'Kit') > r(a, 'Jun')),
                      'Ivy = 2 x Hal with Hal even means Hal 2 and Ivy 4. Jun and Kit share 1 and 3; Jun is odd either way, and '
                      'Kit is greater, so Jun 1 and Kit 3.'),
                 grid('Three pets, a cat, a dog and a rabbit, belong to Lea, Max and Noa (one each). The cat\'s owner sits next '
                      'to Max. Lea owns neither the dog nor the cat. Noa does not own the dog. Who owns which pet?',
                      ['Lea', 'Max', 'Noa'], ['cat', 'dog', 'rabbit'],
                      lambda a: a['Lea'] not in ('dog', 'cat') and a['Noa'] != 'dog' and a['Max'] != 'cat',
                      'Lea owns the rabbit. Noa does not own the dog, so Noa owns the cat and Max owns the dog. (The cat\'s '
                      'owner sits next to Max, so the cat is not Max\'s.)'),
                 grid('Four lockers, numbered 1 to 4 in a row, belong to Oz, Pia, Quin and Rae (one each). Pia\'s locker is '
                      'directly to the right of Oz\'s (one number higher). Rae\'s locker is at an end of the row. Quin\'s '
                      'locker number is even. Rae\'s number is lower than Quin\'s. Oz\'s locker is not number 2. Who has '
                      'which locker?',
                      ['Oz', 'Pia', 'Quin', 'Rae'], ['1', '2', '3', '4'],
                      lambda a: (r(a, 'Pia') == r(a, 'Oz') + 1 and r(a, 'Rae') in (1, 4) and r(a, 'Quin') % 2 == 0
                                 and r(a, 'Rae') < r(a, 'Quin') and r(a, 'Oz') != 2),
                      'Rae is at an end and lower than Quin, so Rae is 1. Oz is not 2, and Pia is directly after Oz, so Oz 3 and '
                      'Pia 4. Quin gets 2, which is even.'),
             ],
             back=[B('Strategy: mark X for "no" and O for "yes" in a grid', 'guided_strategy',
                     'Students lose track of eliminated options. A grid with X for "not possible" and O for "this one", plus '
                     'the rule "one O per row and per column", makes every deduction visible.',
                     lesson=lesson('Mark X for "no" and O for "yes"',
                                   ['Draw a grid: people down the side, options across the top.',
                                    'For each "not" clue, put an X in that cell.',
                                    'When a row has only one empty cell left, put an O there; then put X in the rest of that '
                                    'column (each option is used once).',
                                    'Repeat until every row has an O. Then check every clue again.'],
                                   'Worked example (a different puzzle)',
                                   ['Three hikers, Uri, Val and Wen, carry a map, a rope or a stove (one each). Val does not '
                                    'carry the rope or the stove. Wen does not carry the rope.'],
                                   ['Val: X rope, X stove, so O map. Put X under "map" for Uri and Wen.',
                                    'Wen: X rope, X map, so O stove.',
                                    'Uri gets the rope. Check: every clue holds.']),
                     qs=[
                         grid('Two friends, Ann and Bo, each pick a different color: red or blue. Ann does not pick red. Who '
                              'picks which color?', ['Ann', 'Bo'], ['red', 'blue'], lambda a: a['Ann'] != 'red',
                              'Ann: blue, so Bo: red.'),
                         mc('In a 3 by 3 grid (3 people, 3 jobs, one each), a person\'s row has X in two cells. What follows?',
                            'The person has the job in the third cell.',
                            [('The person has no job.', 'everyone has exactly one job'),
                             ('Nothing follows yet.', 'only one option remains'),
                             ('Another person has that job.', 'it must be this person\'s job')],
                            'Only one option is left in that row.'),
                         tf('In a matching puzzle where each option is used once, if Kim has the bike, no one else has the '
                            'bike.', True, 'Each option is used exactly once.'),
                         grid('Three cousins, Cy, Di and Ed, are ages 8, 9 and 10 (all different). Cy is the youngest. Ed is '
                              'not 10. How old is each?', ['Cy', 'Di', 'Ed'], ['8', '9', '10'],
                              lambda a: a['Cy'] == '8' and a['Ed'] != '10', 'Cy 8; Ed not 10, so 9; Di 10.'),
                         mc('Three people and three snacks, one each. Gil does not have the apple or the pear. Which snack does '
                            'Gil have, if the snacks are apple, pear and plum?', 'plum', [('apple', 'ruled out'),
                                                                                            ('pear', 'ruled out'),
                                                                                            ('it cannot be known', 'only plum '
                                                                                                                  'is left')],
                            'Two snacks are ruled out, so Gil has the plum.'),
                     ])],
             f1=FW('Grids with relative clues', 'Harder: clues that compare positions or numbers.', [
                 grid('Four friends, Ari, Bea, Cal and Dev, finished a quiz with scores 6, 7, 8 and 9 (all different). Bea '
                      'scored 1 more than Dev. Ari scored the most. Cal did not score 6. What did each score?',
                      ['Ari', 'Bea', 'Cal', 'Dev'], ['6', '7', '8', '9'],
                      lambda a: r(a, 'Bea') == r(a, 'Dev') + 1 and a['Ari'] == '9' and a['Cal'] != '6',
                      'Ari 9. Bea and Dev are consecutive with Bea higher, among 6, 7, 8. Cal is not 6, so Dev is 6 and Bea 7, '
                      'leaving Cal 8.'),
                 grid('Five boxes in a row, positions 1 to 5, hold a hat, a kite, a lamp, a mug and a net (one each). The kite '
                      'is in an even position. The lamp is directly left of the mug. The hat is at position 5. The net is not '
                      'next to the kite. Which item is in each position?', ['1', '2', '3', '4', '5'],
                      ['hat', 'kite', 'lamp', 'mug', 'net'],
                      lambda a: (int([p for p, x in a.items() if x == 'kite'][0]) % 2 == 0
                                 and int([p for p, x in a.items() if x == 'mug'][0]) == int([p for p, x in a.items() if x == 'lamp'][0]) + 1
                                 and a['5'] == 'hat'
                                 and abs(int([p for p, x in a.items() if x == 'net'][0]) - int([p for p, x in a.items() if x == 'kite'][0])) != 1),
                      'The hat is 5th. The kite is 2nd or 4th. Lamp-mug is a pair. If the kite were 2nd, the pair would be 3-4 '
                      'and the net 1st, next to the kite: not allowed. So the kite is 4th, the pair is 1-2 or 2-3; the net is '
                      'not next to the kite (not 3rd), so the pair is 2-3 and the net is 1st.'),
                 mc('Rae, Sol and Tom own a cat, a dog and a fish, one each. Clue 1: Rae does not own the cat. Clue 2: Sol '
                    'does not own the dog. These two clues allow three matchings. Which additional clue leaves exactly one?',
                    'Tom owns the cat.',
                    [('Sol does not own the fish.', 'two matchings remain: Rae dog, Sol cat, Tom fish; and Rae fish, Sol cat, '
                                                    'Tom dog'),
                     ('Tom does not own the dog.', 'two remain: Rae dog with Sol cat or Sol fish'),
                     ('Rae does not own the fish.', 'Rae owns the dog, and Sol and Tom can still split cat and fish two ways')],
                    'The three matchings allowed by clues 1 and 2 are (Rae, Sol, Tom) = (dog, cat, fish), (dog, fish, cat), '
                    '(fish, cat, dog). Only "Tom owns the cat" keeps exactly one: (dog, fish, cat).',
                    method='Automatic: each added clue tested against all 6 matchings.',
                    check=lambda t: sum(1 for m in itertools.permutations(['cat', 'dog', 'fish']) if m[0] != 'cat' and m[1] != 'dog'
                                        and {'Tom owns the cat.': m[2] == 'cat', 'Sol does not own the fish.': m[1] != 'fish',
                                             'Tom does not own the dog.': m[2] != 'dog',
                                             'Rae does not own the fish.': m[0] != 'fish'}[t]) == 1),
                 grid('Three students, Uma, Vik and Wyn, each chose a different sport (golf, judo or swimming) and a different '
                      'day (Monday, Tuesday, Wednesday). The judo student trains on Monday. Uma trains on Wednesday. Uma does not '
                      'play golf. Wyn trains on Tuesday. Which sport did each choose?', ['Uma', 'Vik', 'Wyn'],
                      ['golf', 'judo', 'swimming'],
                      lambda a: any(
                          {'Uma': d[0], 'Vik': d[1], 'Wyn': d[2]}[[p for p in a if a[p] == 'judo'][0]] == 'Mon'
                          and d[0] == 'Wed' and d[2] == 'Tue' and a['Uma'] != 'golf'
                          for d in itertools.permutations(['Mon', 'Tue', 'Wed'])),
                      'Uma trains Wednesday and Wyn Tuesday, so Vik trains Monday; the judo student trains Monday, so Vik does '
                      'judo. Uma does not play golf, so Uma swims and Wyn plays golf.'),
                 tf('In a matching puzzle with 4 people and 4 options (one each), if three people\'s options are known, the '
                    'fourth person\'s option is also known.', True, 'Only one option is left.'),
             ]),
             f2=FW('Two-attribute grids and decisive clues', 'Expert: puzzles with two attributes and the least information '
                                                           'that decides them.', [
                 grid('Four students, Al, Bo, Cy and Di, each have a different favorite number from 1 to 4 and a different '
                      'color (red, blue, green, gold). The red student\'s number is 1 more than the blue student\'s number. Al '
                      'is gold. Bo\'s number is 4. Cy\'s number is twice Di\'s number. What is each student\'s number?', ['Al', 'Bo', 'Cy', 'Di'], ['1', '2', '3', '4'],
                      lambda a: any(
                          (lambda col: r(a, [p for p in col if col[p] == 'red'][0]) == r(a, [p for p in col if col[p] == 'blue'][0]) + 1
                           and col['Al'] == 'gold')(dict(zip(['Al', 'Bo', 'Cy', 'Di'], c)))
                          for c in itertools.permutations(['red', 'blue', 'green', 'gold']))
                      and a['Bo'] == '4' and r(a, 'Cy') == 2 * r(a, 'Di'),
                      'Bo is 4. Cy = 2 x Di with 1, 2, 3 left gives Di 1 and Cy 2, so Al 3. (The colors are not asked, but '
                      'they must also work: Al is gold; red is one more than blue, which among Bo 4, Cy 2, Di 1 means Cy red '
                      'and Di blue, since 4 = 3 + 1 would need Al blue. So Bo is green.)'),
                 mc('Three people wear a red, a blue and a green hat, one each, so there are 6 possible matchings. Clues have '
                    'the form "person X does not wear color Y". What is the smallest number of such clues that can leave '
                    'exactly one matching?', '3',
                    [('1', 'one clue removes 2 matchings and leaves 4'), ('2', 'two clues always leave at least 2 matchings'),
                     ('4', 'three well-chosen clues already suffice')],
                    'Example with 3 clues: A not red, A not blue (so A green), B not red (so B blue): C red. With 2 clues, at '
                    'least 2 matchings always remain (checked for every pair of clues).',
                    method='Automatic: every set of 1, 2 and 3 clues tested against the 6 matchings.',
                    check=lambda t: int(t) == next(k for k in range(1, 7) for cs in itertools.combinations(
                        [(p, c) for p in range(3) for c in range(3)], k)
                        if sum(1 for m in itertools.permutations(range(3)) if all(m[p] != c for p, c in cs)) == 1)),
                 sa('Four people each get a different one of 4 prizes. How many matchings are possible if one person, Ash, '
                    'cannot get prize 1 or prize 2?', 'Matchings:', '12',
                    'Ash has 2 choices (prize 3 or 4); the other three people take the remaining 3 prizes in 3 x 2 x 1 = 6 '
                    'ways: 2 x 6 = 12.', compute=lambda: str(sum(1 for p in itertools.permutations('1234') if p[0] not in '12'))),
                 tf('In a 3-person, 3-option matching puzzle, the clues "A not x" and "B not x" together force C to have x.',
                    True, 'Option x must go to someone, and A and B are ruled out.'),
                 values('Five players wear the numbers 1 to 5 (all different). Al\'s number plus Bo\'s number is 9. Give one '
                        'possible pair: Al\'s number a and Bo\'s number b.', [('a', 'Al a ='), ('b', 'Bo b =')],
                        'a + b == 9 and a != b and a >= 1 and a <= 5 and b >= 1 and b <= 5 and isInteger(a) and isInteger(b)',
                        {'a': 4, 'b': 5}, 'Only 4 + 5 = 9 works with different numbers up to 5, in either order.',
                        wrong=[{'a': 3, 'b': 6}, {'a': 5, 'b': 5}], search={'a': range(1, 6), 'b': range(1, 6)}),
             ]))


SETS = [s13(), s14()]
