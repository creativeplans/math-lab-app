"""Logic sets 33-36: word ladders; translating clues into conditions; must, could, cannot; complete search."""
import itertools
from collections import deque
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt

BANK = ['SAND', 'BAND', 'BEND', 'SEND', 'SENT', 'BENT', 'BEAD', 'BEAT', 'BOAT', 'BELT', 'BOLT', 'BEST', 'REST', 'RENT',
        'RANT', 'PANT', 'PART', 'PORT', 'POST', 'MOST', 'MAST', 'LAST', 'LAND', 'LEND']
BANK_TEXT = ('Word list (the ONLY words allowed): ' + ', '.join(BANK) + '. A ladder step changes exactly one letter and keeps '
             'the other letters in place; every word in the ladder must be on the list.')


def d1(a, b):
    return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1


def ladder(s, t, bank=BANK):
    seen = {s: [s]}
    q = deque([s])
    while q:
        x = q.popleft()
        if x == t:
            return seen[x]
        for y in bank:
            if y not in seen and d1(x, y):
                seen[y] = seen[x] + [y]
                q.append(y)
    return None


def steps(s, t, bank=BANK):
    p = ladder(s, t, bank)
    return None if p is None else len(p) - 1


def shortest_count(s, t, bank=BANK):
    L = steps(s, t, bank)
    out = 0

    def go(path):
        nonlocal out
        if len(path) - 1 == L:
            out += path[-1] == t
            return
        for y in bank:
            if y not in path and d1(path[-1], y):
                go(path + [y])
    go([s])
    return out


# ------------------------------------------------------------------ Set 33: word ladders
def s33():
    return S(33, 'Find shortest one-letter-change paths through a supplied word list',
             main=[
                 order(BANK_TEXT + ' Put these four words in ladder order, starting with SAND, so that each word differs from '
                                   'the next by one letter.', [('A', 'SAND'), ('B', 'SEND'), ('C', 'SENT'), ('D', 'RENT')],
                       lambda p: p[0] == 'A' and all(d1(dict(A='SAND', B='SEND', C='SENT', D='RENT')[x],
                                                       dict(A='SAND', B='SEND', C='SENT', D='RENT')[y]) for x, y in zip(p, p[1:])),
                       'SAND -> SEND (A to E) -> SENT (D to T) -> RENT (S to R).', expect=['A', 'B', 'C', 'D'], unique=True),
                 sa(BANK_TEXT + ' What is the least number of steps in a ladder from BAND to BOAT?', 'Steps:', '4',
                    'BAND -> BEND -> BENT -> BEAT -> BOAT (or through BEAD). Three steps are impossible: BAND has no neighbor '
                    'on the list that is two steps from BOAT.', compute=lambda: str(steps('BAND', 'BOAT'))),
                 mc(BANK_TEXT + ' Which word fills the gap in the ladder SENT, ?, RANT?', 'RENT',
                    [('BENT', 'BENT to RANT changes two letters'), ('SEND', 'SEND to RANT changes three letters'),
                     ('PANT', 'SENT to PANT changes two letters')], 'SENT -> RENT -> RANT.',
                    check=lambda w: d1('SENT', w) and d1(w, 'RANT')),
                 values(BANK_TEXT + ' Give a word from the list that is one step from both BEND and BEAT.', [('w', 'word =')],
                        "w == 'bent' or w == 'bead'", {'w': 'BENT'},
                        'BENT (BEND -> BENT, BEAT -> BENT) and BEAD (BEND -> BEAD, BEAT -> BEAD) both work.',
                        wrong=[{'w': 'BELT'}, {'w': 'BOAT'}, {'w': 'BEST'}]),
                 tf(BANK_TEXT + ' A ladder from LAND to BELT can be done in 3 steps.', False,
                    'LAND and BELT differ in all 4 positions (L/B, A/E, N/L, D/T), and each step changes only one letter, so '
                    'at least 4 steps are needed: LAND -> BAND -> BEND -> BENT -> BELT.', check=lambda: steps('LAND', 'BELT') <= 3),
             ],
             back=[B('Strategy: change the letters that must change, one at a time', 'guided_strategy',
                     'Students try random words. Comparing start and end letter by letter shows which letters must change '
                     'and gives a lower limit on the number of steps.',
                     lesson=lesson('Change the letters that must change, one at a time',
                                   ['Write the start word above the end word and circle each position where they differ. Each '
                                    'step changes one letter, so you need at least as many steps as circled positions.',
                                    'Try changing one circled letter at a time, and check that each new word is on the list.',
                                    'If no circled letter can change to a listed word, you may need a detour: change a letter '
                                    'that is already correct and change it back later. Detours add steps.'],
                                   'Worked example (a different list)',
                                   ['List: COT, CAT, HAT, HOT, HUT. Ladder from COT to HAT?'],
                                   ['COT and HAT differ in 2 positions (C/H, O/A): at least 2 steps.',
                                    'COT -> CAT (O to A) -> HAT (C to H). Both words are listed, so 2 steps.']),
                     qs=[
                         mc(BANK_TEXT + ' Which word is one step from BEST?', 'REST', [('RENT', 'two letters differ from BEST'),
                                                                                      ('POST', 'two letters differ'),
                                                                                      ('BOAT', 'two letters differ')],
                            'BEST -> REST changes only B to R.', check=lambda w: d1('BEST', w)),
                         sa('In how many positions do the words MOST and PART differ?', 'Positions:', '3',
                            'M/P, O/A, S/R differ; T matches.', compute=lambda: str(sum(x != y for x, y in zip('MOST', 'PART')))),
                         tf('A ladder from MAST to LAST can be done in one step.', True, 'Only M changes to L.',
                            check=lambda: d1('MAST', 'LAST')),
                         sa(BANK_TEXT + ' What is the least number of steps from PORT to MOST?', 'Steps:', '2',
                            'PORT -> POST -> MOST.', compute=lambda: str(steps('PORT', 'MOST'))),
                         tf('If two words differ in 3 positions, every ladder between them has at least 3 steps.', True,
                            'Each step fixes at most one position.'),
                     ])],
             f1=FW('Longer ladders and detours', 'Harder: ladders that need detours through the list.', [
                 sa(BANK_TEXT + ' What is the least number of steps from BEND to PORT?', 'Steps:', '6',
                    'BEND -> BENT -> RENT -> RANT -> PANT -> PART -> PORT. BEND and PORT differ in 4 positions, but the list '
                    'forces a longer route.', compute=lambda: str(steps('BEND', 'PORT'))),
                 sa(BANK_TEXT + ' How many different shortest ladders go from BAND to BOAT?', 'Ladders:', '2',
                    'BAND-BEND-BENT-BEAT-BOAT and BAND-BEND-BEAD-BEAT-BOAT.', compute=lambda: str(shortest_count('BAND', 'BOAT'))),
                 mc(BANK_TEXT + ' Which word needs the MOST steps to reach from SAND (using shortest ladders)?', 'LAST',
                    [('MOST', 'MOST takes 9 steps; LAST is two steps farther, through MAST'),
                     ('BOLT', 'BOLT takes only 5 steps: SAND, BAND, BEND, BENT, BELT, BOLT'),
                     ('PORT', 'PORT takes 7 steps; the chain continues past it to POST, MOST, MAST, LAST')],
                    'LAST is 11 steps from SAND: the chain RENT, RANT, PANT, PART, PORT, POST, MOST, MAST, LAST is the only '
                    'way out to it, and LAST is at its far end.',
                    check=lambda w: steps('SAND', w) == max(steps('SAND', x) for x in BANK)),
                 values(BANK_TEXT + ' Give a word from the list that is exactly one step from LAND and also one step from '
                                    'SEND.', [('w', 'word =')], "w == 'sand' or w == 'lend'", {'w': 'SAND'},
                        'SAND (LAND -> SAND, SEND -> SAND) and LEND (LAND -> LEND, SEND -> LEND) both work.',
                        wrong=[{'w': 'BAND'}, {'w': 'BEND'}]),
                 tf(BANK_TEXT + ' BOAT is one step from BOLT.', True, 'B, O and T stay in place; only the third letter '
                                                                      'changes (A to L).', check=lambda: d1('BOAT', 'BOLT')),
             ]),
             f2=FW('Prove a ladder is shortest or impossible', 'Expert: lower bounds and counting.', [
                 sa(BANK_TEXT + ' What is the least number of steps from SAND to MOST?', 'Steps:', '9',
                    'Breadth-first search over the list gives 9 steps: SAND, SEND, SENT, RENT, RANT, PANT, PART, PORT, POST, MOST.',
                    compute=lambda: str(steps('SAND', 'MOST'))),
                 sa(BANK_TEXT + ' Suppose PANT is removed from the list. What is the least number of steps from RANT to PART '
                                'now? Enter 0 if no ladder is possible.', 'Steps:', '0',
                    'Without PANT, PART\'s only neighbor is PORT. The words PART, PORT, POST, MOST, MAST, LAST then link only to '
                    'each other, and none of them is one step from RANT or any word connected to RANT, so no ladder exists.',
                    compute=lambda: str(steps('RANT', 'PART', [w for w in BANK if w != 'PANT']) or 0)),
                 tf(BANK_TEXT + ' Every ladder from BAND to BOAT passes through BEND.', False,
                    'BAND -> SAND -> SEND -> SENT -> BENT -> BEAT -> BOAT avoids BEND. It is longer (6 steps) than the shortest '
                    'ladders, but the statement is about every ladder.',
                    check=lambda: steps('BAND', 'BOAT', [w for w in BANK if w != 'BEND']) is None),
                 sa(BANK_TEXT + ' How many words on the list are exactly one step from BENT?', 'Words:',
                    str(sum(d1('BENT', w) for w in BANK)), 'BEND, SENT, BEAT, BELT, BEST, RENT.',
                    compute=lambda: str(sum(d1('BENT', w) for w in BANK))),
                 mc('A ladder must go from a 4-letter word to another 4-letter word that differs in all 4 positions. What is the '
                    'least possible number of steps?', '4', [('3', 'each step changes only one position'),
                                                            ('2', 'each step changes only one position'),
                                                            ('8', 'that is not the least possible')],
                    'Each of the 4 positions must change at least once.'),
             ]))


# ------------------------------------------------------------------ Set 34: translate clues into conditions
LOCK = ('Five friends, Ava, Ben, Cal, Dee and Eli, each use one of five lockers numbered 1 to 5 from left to right, one '
        'friend per locker. "Left of" means a lower number. The letters A, B, C, D and E stand for the friends\' locker '
        'numbers.')
CLUES = [('Ava is somewhere left of Ben.', lambda x: x['A'] < x['B']),
         ('Exactly one locker lies between Cal and Dee.', lambda x: abs(x['C'] - x['D']) == 2),
         ('Eli is not at either end.', lambda x: x['E'] not in (1, 5)),
         ('Ben and Cal are next to each other.', lambda x: abs(x['B'] - x['C']) == 1),
         ('Dee is in an even-numbered locker.', lambda x: x['D'] % 2 == 0)]
CLUE_TEXT = ' Clues: ' + ' '.join('(%d) %s' % (i + 1, t) for i, (t, _) in enumerate(CLUES))
NAMES = dict(A='Ava', B='Ben', C='Cal', D='Dee', E='Eli')


def pos(arr):
    """'ADECB' (lockers 1-5) -> {letter: locker}"""
    return {k: i + 1 for i, k in enumerate(arr)}


def arrangements(clues, people='ABCDE'):
    return [''.join(p) for p in itertools.permutations(people) if all(f(pos(''.join(p))) for _, f in clues)]


def broken(arr, clues=CLUES):
    return [i for i, (_, f) in enumerate(clues) if not f(pos(arr))]


def named(arr):
    return ', '.join(NAMES[k] for k in arr)


SIX = [('Ava is somewhere left of Ben.', lambda x: x['A'] < x['B']),
       ('Exactly two lockers lie between Cal and Dee.', lambda x: abs(x['C'] - x['D']) == 3),
       ('Fay is somewhere right of Cal.', lambda x: x['F'] > x['C']),
       ('Dee is in an odd-numbered locker.', lambda x: x['D'] % 2 == 1),
       ('Cal is somewhere left of Ava.', lambda x: x['C'] < x['A']),
       ('Ben is not in locker 6.', lambda x: x['B'] != 6)]


def s34():
    six_items = [('A', 'Ava'), ('B', 'Ben'), ('C', 'Cal'), ('D', 'Dee'), ('E', 'Eli'), ('F', 'Fay')]
    return S(34, 'Translate puzzle clues into exact conditions and test candidate arrangements against them',
             main=[
                 mc(LOCK + ' Which condition says exactly the same thing as the clue "Exactly one locker lies between Cal '
                           'and Dee"?', '|C - D| = 2',
                    [('|C - D| = 1', 'that says Cal and Dee are next to each other, with no locker between'),
                     ('C - D = 2', 'that only allows Cal to the right of Dee; the clue allows either order'),
                     ('|C - D| >= 2', 'that also allows two or more lockers between them')],
                    'One locker between them means their numbers differ by 2, in either order, so |C - D| = 2.'),
                 order(LOCK + CLUE_TEXT + ' Put the friends in locker order, from locker 1 to locker 5.',
                       [(k, NAMES[k]) for k in 'ABCDE'], lambda p: not broken(''.join(p)),
                       'Dee is in 2 or 4 (clue 5), and Cal is two away from Dee (clue 2). Testing each case with clues 1, 3 '
                       'and 4 leaves only Ava 1, Dee 2, Eli 3, Cal 4, Ben 5.', expect=list('ADECB'), unique=True),
                 tf(LOCK + CLUE_TEXT + ' The arrangement %s (lockers 1 to 5) breaks exactly one of the five clues.'
                    % named('ACEDB'), True,
                    'Ava 1, Cal 2, Eli 3, Dee 4, Ben 5: clue 1 holds (1 < 5), clue 2 holds (|2 - 4| = 2), clue 3 holds, '
                    'clue 4 fails (|5 - 2| = 3), clue 5 holds. Exactly one clue is broken.',
                    check=lambda: len(broken('ACEDB')) == 1),
                 mc(LOCK + CLUE_TEXT + ' The arrangement %s (lockers 1 to 5) breaks one clue. Which one?' % named('ADEBC'),
                    'Clue 2', [('Clue 1', 'Ava 1 is left of Ben 4, so clue 1 holds'),
                               ('Clue 4', 'Ben 4 and Cal 5 are next to each other, so clue 4 holds'),
                               ('Clue 5', 'Dee is in locker 2, which is even, so clue 5 holds')],
                    'Cal is in 5 and Dee in 2: |5 - 2| = 3, so two lockers lie between them, not one.',
                    check=lambda t: broken('ADEBC') == [int(t.split()[1]) - 1]),
                 values('A row has nine lockers numbered 1 to 9. Eli\'s locker must meet every condition: it is '
                        'odd-numbered; it is not at either end (not 1 and not 9); and it is at least 2 lockers away from '
                        'locker 5 (|E - 5| >= 2). Give one locker number Eli could have.', [('e', 'E =')],
                        'isInteger(e) and isOdd(e) and e > 1 and e < 9 and abs(e - 5) >= 2', {'e': 3},
                        'Odd and not an end: 3, 5 or 7. At least 2 from 5 removes 5. Eli could be in 3 or 7.',
                        wrong=[{'e': 5}, {'e': 9}, {'e': 4}, {'e': 1}], search={'e': range(1, 10)}),
             ],
             back=[B('Strategy: write each clue as a condition on numbers', 'guided_strategy',
                     'Students who misread a clue test arrangements against the wrong rule. Writing each clue as a condition '
                     'on locker numbers makes every test exact.',
                     lesson=lesson('Write each clue as a condition on numbers',
                                   ['Give each person a letter that stands for their position number.',
                                    'Translate each clue: "somewhere left of" becomes <, "next to" becomes a difference of 1 '
                                    'in either order, "exactly one between" becomes a difference of 2 in either order.',
                                    'To test an arrangement, put its numbers into every condition. One failed condition '
                                    'rules the arrangement out.'],
                                   'Worked example (a different puzzle)',
                                   ['Three books, Map (M), Novel (N) and Poems (P), stand on a shelf in spots 1 to 3. Clues: '
                                    'Map is next to Poems; Novel is not in spot 2.'],
                                   ['Conditions: |M - P| = 1 and N is 1 or 3.',
                                    'If N = 1, then M and P fill 2 and 3, which are next to each other: N, M, P or N, P, M.',
                                    'If N = 3, then M and P fill 1 and 2: M, P, N or P, M, N. Four arrangements fit.']),
                     qs=[
                         mc(LOCK + ' Which condition matches the clue "Ava is somewhere left of Ben"?', 'A < B',
                            [('A = B - 1', 'that says Ava is directly left of Ben; the clue allows a gap'),
                             ('A > B', 'that puts Ava to the right of Ben'),
                             ('A + 1 < B', 'that requires at least one locker between them')],
                            '"Somewhere left of" only says Ava\'s number is smaller.'),
                         mc(LOCK + ' Which condition matches the clue "Ben and Cal are next to each other"?', '|B - C| = 1',
                            [('B - C = 1', 'that only allows Ben directly right of Cal'),
                             ('|B - C| = 2', 'that puts one locker between them'),
                             ('|B - C| <= 2', 'that also allows one locker between them')],
                            'Next to each other means the numbers differ by 1, in either order.'),
                         tf(LOCK + ' With five lockers, the clue "Eli is not at either end" means E is 2, 3 or 4.', True,
                            'The ends are lockers 1 and 5, so Eli is in 2, 3 or 4.'),
                         tf(LOCK + ' The clue "Dee is directly left of Ava" means the same as D < A.', False,
                            '"Directly left" means the next locker: D = A - 1. D < A also allows a gap.'),
                         sa(LOCK + ' Dee is in locker 2, and exactly one locker lies between Cal and Dee. Which locker is '
                                   'Cal in?', 'Locker:', '4',
                            '|C - 2| = 2 gives C = 4 or C = 0, and there is no locker 0.',
                            compute=lambda: str([c for c in range(1, 6) if abs(c - 2) == 2][0])),
                     ])],
             f1=FW('Harder clue words', 'Harder: "at least", "unless", "directly" and six-person puzzles.', [
                 mc(LOCK + ' Which condition matches the clue "At least two lockers lie between Ava and Eli"?',
                    '|A - E| >= 3', [('|A - E| >= 2', 'that allows only one locker between them'),
                                     ('|A - E| = 3', 'that allows exactly two between them, not more'),
                                     ('A - E >= 3', 'that only allows Ava to the right of Eli')],
                    'Two lockers between means the numbers differ by 3; "at least" allows more, in either order.'),
                 mc(LOCK + ' In these puzzles, "X unless Y" means "if Y is false, then X is true." Which condition matches '
                           'the clue "Ben is in locker 3 unless Cal is"?', 'B = 3 or C = 3',
                    [('B = 3 and C is not 3', 'that rules out Cal in locker 3, but the clue allows it'),
                     ('B is not 3 and C is not 3', 'that is the opposite: the clue needs one of them in locker 3'),
                     ('C = 3', 'that rules out Ben in locker 3, but the clue allows it')],
                    'If Cal is not in 3, Ben is. So one of them is in locker 3: B = 3 or C = 3.'),
                 order('Six friends, Ava, Ben, Cal, Dee, Eli and Fay, each use one of six lockers numbered 1 to 6 from left '
                       'to right. "Left of" means a lower number. Clues: ' +
                       ' '.join('(%d) %s' % (i + 1, t) for i, (t, _) in enumerate(SIX)) +
                       ' Put the friends in locker order, from locker 1 to locker 6.', six_items,
                       lambda p: all(f(pos(''.join(p))) for _, f in SIX),
                       'Dee is odd and three away from Cal, so (Cal, Dee) is (2, 5), (4, 1) or (6, 3). Cal is left of Ava '
                       'and Fay, so Cal is not 6. If Cal is 4, Ava and Fay need lockers 5 and 6, and Ben must be right of '
                       'Ava, so Ava 5 and Ben 6, which clue 6 forbids. So Cal 2 and Dee 5. Ava, Ben and Fay take 3, 4 and 6 '
                       'with Ava left of Ben and Ben not in 6: Ava 3, Ben 4, Fay 6, and Eli 1.', expect=list('ECABDF'), unique=True),
                 tf(LOCK + ' The two conditions A < B and B < A + 2 together say that Ben is directly right of Ava.', True,
                    'Locker numbers are whole numbers, so A < B < A + 2 forces B = A + 1.'),
                 values('Seven lockers are numbered 1 to 7 from left to right. Give lockers for Ava and Ben that meet every '
                        'clue: Ava is somewhere left of Ben; at least two lockers lie between them; Ben\'s locker is '
                        'even-numbered.', [('a', 'A ='), ('b', 'B =')],
                        'isInteger(a) and isInteger(b) and a >= 1 and b <= 7 and a < b and b - a >= 3 and isEven(b)',
                        {'a': 1, 'b': 4}, 'For example A = 1, B = 4. Other answers: (1, 6), (2, 6), (3, 6).',
                        wrong=[{'a': 2, 'b': 4}, {'a': 6, 'b': 2}, {'a': 1, 'b': 5}],
                        search={'a': range(1, 8), 'b': range(1, 8)}),
             ]),
             f2=FW('Test what each clue contributes', 'Expert: count the arrangements a set of clues allows.', [
                 sa(LOCK + CLUE_TEXT + ' If clue 3 is removed, how many arrangements fit the other four clues?',
                    'Arrangements:', str(len(arrangements(CLUES[:2] + CLUES[3:]))),
                    'Enumerating with clues 1, 2, 4 and 5 gives 4 arrangements, so clue 3 is needed for a single answer.',
                    compute=lambda: str(len(arrangements(CLUES[:2] + CLUES[3:])))),
                 sa(LOCK + ' How many arrangements fit both clues "Eli is not at either end" and "Ben and Cal are next to '
                           'each other" (and no other clues)?', 'Arrangements:',
                    str(len(arrangements([CLUES[2], CLUES[3]]))),
                    'Treat Ben-and-Cal as a block. Eli is in 2, 3 or 4; for each, count the places for the block in either '
                    'order and the arrangements of Ava and Dee in the last two lockers: 24 in all.',
                    compute=lambda: str(len(arrangements([CLUES[2], CLUES[3]])))),
                 tf(LOCK + CLUE_TEXT + ' If clue 5 is replaced by "Dee is in locker 2", the puzzle still has exactly one '
                                       'answer, and it is the same answer.', True,
                    'The answer to the original puzzle has Dee in locker 2, and enumerating clues 1-4 with D = 2 leaves '
                    'only Ava, Dee, Eli, Cal, Ben.',
                    check=lambda: arrangements(CLUES[:4] + [('', lambda x: x['D'] == 2)]) == arrangements(CLUES)),
                 mc(LOCK + ' Which condition matches the clue "Ava and Ben are not both at the ends"?',
                    'At most one of Ava and Ben is in locker 1 or 5',
                    [('Neither Ava nor Ben is in locker 1 or 5', 'that forbids even one of them at an end'),
                     ('Exactly one of Ava and Ben is in locker 1 or 5', 'that forbids both being away from the ends'),
                     ('Ava and Ben are both in lockers 2, 3 or 4', 'that is the same as "neither is at an end"')],
                    '"Not both" only rules out the case where both are at the ends; zero or one at an end is allowed.'),
                 tf(LOCK + ' In these puzzles, "X unless Y" means "if Y is false, then X is true." Under the clue "Ben is '
                           'in locker 3 unless Cal is", an arrangement with Ava in locker 3 is allowed.', False,
                    'If Ava is in 3, Cal is not in 3, so the clue says Ben must be in 3. Ben cannot share the locker, so the '
                    'arrangement breaks the clue.'),
             ]))


# ------------------------------------------------------------------ Set 35: must, could, cannot
TALKS = dict(F='Fossils', G='Gears', H='Honey', J='Jazz', K='Kites')
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
WEEK = ('A club holds five talks, Fossils, Gears, Honey, Jazz and Kites, one on each day from Monday to Friday. '
        'Conditions: (1) Gears is earlier in the week than Jazz. (2) Honey is on Wednesday or Friday. (3) Fossils and '
        'Kites are not on consecutive days. (4) Jazz is not on Friday.')
WEEK_RULES = [lambda x: x['G'] < x['J'], lambda x: x['H'] in (3, 5), lambda x: abs(x['F'] - x['K']) != 1,
              lambda x: x['J'] != 5]


def weeks(rules=WEEK_RULES, extra=()):
    return [x for p in itertools.permutations(range(1, 6)) for x in [dict(zip('FGHJK', p))]
            if all(f(x) for f in list(rules) + list(extra))]


def on(t, d):
    return lambda x: x[t] == d


def status(pred, scheds):
    n = sum(1 for x in scheds if pred(x))
    return 'must' if n == len(scheds) else ('cannot' if n == 0 else 'could')


def s35():
    W = weeks()
    statements = {'Gears is on Monday or Tuesday.': lambda x: x['G'] in (1, 2), 'Honey is on Friday.': on('H', 5),
                  'Fossils is on Monday.': on('F', 1), 'Kites is on Friday.': on('K', 5),
                  'Jazz is on Tuesday.': on('J', 2), 'Fossils is on Friday.': on('F', 5),
                  'Kites is on Wednesday.': on('K', 3), 'Honey is on Wednesday.': on('H', 3)}
    k_mon = weeks(extra=[on('K', 1)])
    unique_if = {'Fossils is on Wednesday.': on('F', 3), 'Fossils is on Friday.': on('F', 5),
                 'Kites is on Thursday.': on('K', 4), 'Honey is on Wednesday.': on('H', 3)}
    f_mon = weeks([WEEK_RULES[0], WEEK_RULES[1], WEEK_RULES[3], on('F', 1)])
    st_fmon = {'Jazz is on Wednesday or Thursday.': lambda x: x['J'] in (3, 4), 'Gears is on Tuesday.': on('G', 2),
               'Kites is on Friday.': on('K', 5), 'Honey is on Friday.': on('H', 5)}
    return S(35, 'Decide what must be true, what could be true and what cannot be true in a constrained arrangement',
             main=[
                 mc(WEEK + ' Which statement MUST be true?', 'Gears is on Monday or Tuesday.',
                    [('Honey is on Friday.', 'Fossils, Gears, Honey, Jazz, Kites (Monday to Friday) works with Honey on '
                                             'Wednesday'),
                     ('Fossils is on Monday.', 'Gears, Kites, Honey, Jazz, Fossils works with Fossils on Friday'),
                     ('Kites is on Friday.', 'Fossils, Gears, Jazz, Kites, Honey works with Kites on Thursday')],
                    'Gears must be before Jazz, and Jazz is not on Friday, so Gears is not on Thursday or Friday. If Gears '
                    'were on Wednesday, Jazz would be Thursday and Honey Friday, leaving Monday and Tuesday (consecutive) '
                    'for Fossils and Kites. So Gears is on Monday or Tuesday.', check=lambda t: status(statements[t], W) == 'must'),
                 mc(WEEK + ' Which statement CANNOT be true?', 'Jazz is on Tuesday.',
                    [('Fossils is on Friday.', 'Gears, Kites, Honey, Jazz, Fossils meets every condition'),
                     ('Kites is on Wednesday.', 'Fossils, Gears, Kites, Jazz, Honey meets every condition'),
                     ('Honey is on Wednesday.', 'Fossils, Gears, Honey, Jazz, Kites meets every condition')],
                    'If Jazz is on Tuesday, Gears is on Monday. Honey takes Wednesday or Friday, and Fossils and Kites take '
                    'the other two of Wednesday, Thursday, Friday. If Honey is on Friday they are on Wednesday and '
                    'Thursday (consecutive); if Honey is on Wednesday, they are on Thursday and Friday (consecutive). '
                    'Either way condition 3 fails.', check=lambda t: status(statements[t], W) == 'cannot'),
                 tf(WEEK + ' Fossils could be on Friday.', True,
                    'Gears, Kites, Honey, Jazz, Fossils (Monday to Friday) meets all four conditions.',
                    check=lambda: status(on('F', 5), W) != 'cannot'),
                 sa(WEEK + ' How many complete schedules meet all four conditions?', 'Schedules:', str(len(W)),
                    'Case by Honey\'s day. Honey Wednesday: 4 schedules. Honey Friday: 6 schedules. Total 10.',
                    compute=lambda: str(len(W))),
                 values(WEEK + ' Suppose Honey is on Wednesday. Using Monday = 1, Tuesday = 2, Wednesday = 3, Thursday = 4 '
                               'and Friday = 5, give a day number Kites could be on.', [('k', 'Kites day =')],
                        'k == 1 or k == 2 or k == 5', {'k': 5},
                        'With Honey on Wednesday the schedules are F G H J K, G F H J K, G K H J F and K G H J F, so Kites '
                        'could be on day 1, 2 or 5.', wrong=[{'k': 3}, {'k': 4}]),
             ],
             back=[B('Strategy: list every case, then read must, could, cannot', 'guided_strategy',
                     'Students guess from one schedule. Listing every schedule that meets the conditions turns each '
                     'question into a check: true in all, true in some, or true in none.',
                     lesson=lesson('List every case, then read must, could and cannot',
                                   ['Find every arrangement that meets all the conditions. Organize the list by one item '
                                    'with few choices, so no case is missed.',
                                    'A statement MUST be true if it is true in every arrangement on the list.',
                                    'It COULD be true if it is true in at least one. It CANNOT be true if it is true in '
                                    'none.'],
                                   'Worked example (a different puzzle)',
                                   ['Three chores, dishes (D), laundry (L) and sweeping (W), are done on days 1, 2, 3, one '
                                    'per day. Conditions: laundry is not on day 3; dishes are after sweeping.'],
                                   ['Laundry on day 1: W, D fill days 2 and 3 with W first: L, W, D.',
                                    'Laundry on day 2: W on day 1, D on day 3: W, L, D.',
                                    'Dishes are on day 3 in both, so "dishes are on day 3" must be true. "Laundry is on '
                                    'day 1" could be true. "Sweeping is on day 3" cannot be true.']),
                     qs=[
                         sa('Three talks, P, Q and R, are on days 1, 2 and 3, one per day. Conditions: P is not on day 1; '
                            'Q is earlier than R. How many schedules meet both conditions?', 'Schedules:', '2',
                            'P on day 2: Q, P, R. P on day 3: Q, R, P.',
                            compute=lambda: str(sum(1 for p in itertools.permutations('PQR')
                                                    if p[0] != 'P' and p.index('Q') < p.index('R')))),
                         tf('Three talks, P, Q and R, are on days 1, 2 and 3, one per day. Conditions: P is not on day 1; '
                            'Q is earlier than R. Then Q must be on day 1.', True,
                            'The two schedules are Q, P, R and Q, R, P. Q is on day 1 in both.'),
                         tf('Three talks, P, Q and R, are on days 1, 2 and 3, one per day. Conditions: P is not on day 1; '
                            'Q is earlier than R. Then R must be on day 3.', False,
                            'In Q, R, P, R is on day 2. R could be on day 3 but need not be.'),
                         mc('In a scheduling puzzle, what does it mean to say a statement CANNOT be true?',
                            'It is false in every schedule that meets the conditions.',
                            [('It is false in at least one schedule that meets the conditions.',
                              'that means the statement need not be true; it could still be true in another schedule'),
                             ('It is true in exactly one schedule that meets the conditions.',
                              'then the statement could be true'),
                             ('It is not mentioned in any of the conditions.',
                              'a statement can be forced false by conditions that never mention it')],
                            'Cannot be true means no valid schedule makes it true.'),
                         mc('Three talks, P, Q and R, are on days 1, 2 and 3, one per day. Conditions: P is not on day 1; '
                            'Q is earlier than R. Which statement COULD be true?', 'P is on day 2.',
                            [('P is on day 1.', 'the first condition forbids it'),
                             ('R is on day 1.', 'Q must be earlier than R, so R is never first'),
                             ('Q is on day 3.', 'Q must be earlier than R, so Q is never last')],
                            'Q, P, R meets both conditions and has P on day 2.'),
                     ])],
             f1=FW('Must, could, cannot under an added condition', 'Harder: reason inside a hypothetical case.', [
                 mc(WEEK + ' If Kites is on Monday, which statement MUST be true?', 'Gears is on Tuesday.',
                    [('Honey is on Friday.', 'Kites, Gears, Honey, Jazz, Fossils puts Honey on Wednesday'),
                     ('Fossils is on Wednesday.', 'Kites, Gears, Jazz, Fossils, Honey puts Fossils on Thursday'),
                     ('Jazz is on Thursday.', 'Kites, Gears, Jazz, Fossils, Honey puts Jazz on Wednesday')],
                    'Fossils cannot be on Tuesday (next to Kites), Jazz cannot be on Tuesday (Gears must come first), and '
                    'Honey is on Wednesday or Friday, so Gears is on Tuesday.',
                    check=lambda t: status({'Gears is on Tuesday.': on('G', 2), 'Honey is on Friday.': on('H', 5),
                                            'Fossils is on Wednesday.': on('F', 3), 'Jazz is on Thursday.': on('J', 4)}[t],
                                           k_mon) == 'must'),
                 sa(WEEK + ' If Kites is on Friday, how many schedules are possible?', 'Schedules:',
                    str(len(weeks(extra=[on('K', 5)]))),
                    'Honey must be on Wednesday, and Fossils is not on Thursday (next to Kites). Fossils, Gears and Jazz '
                    'fill Monday, Tuesday and Thursday with Gears before Jazz, so Jazz is on Thursday: F G H J K and '
                    'G F H J K.', compute=lambda: str(len(weeks(extra=[on('K', 5)])))),
                 tf(WEEK + ' If Jazz is on Wednesday, then Honey must be on Friday.', True,
                    'Honey is on Wednesday or Friday, and Wednesday is taken by Jazz.',
                    check=lambda: status(on('H', 5), weeks(extra=[on('J', 3)])) == 'must'),
                 mc(WEEK + ' Which ONE added condition would leave exactly one possible schedule?',
                    'Fossils is on Wednesday.',
                    [('Fossils is on Friday.', 'two schedules remain: G K H J F and K G H J F'),
                     ('Kites is on Thursday.', 'two schedules remain: F G J K H and G F J K H'),
                     ('Honey is on Wednesday.', 'four schedules remain')],
                    'With Fossils on Wednesday, only Kites, Gears, Fossils, Jazz, Honey works.',
                    check=lambda t: len(weeks(extra=[unique_if[t]])) == 1),
                 values(WEEK + ' Suppose Honey is on Friday. Using Monday = 1 to Friday = 5, give the day numbers of Gears '
                               'and Jazz in one schedule that meets every condition.', [('g', 'Gears day ='),
                                                                                        ('j', 'Jazz day =')],
                        '(g == 2 and (j == 3 or j == 4)) or (g == 1 and j == 3)', {'g': 2, 'j': 3},
                        'Listing the schedules with Honey on Friday gives (Gears, Jazz) = (1, 3), (2, 3) or (2, 4). The '
                        'tempting (1, 4) fails: Fossils and Kites would be on Tuesday and Wednesday, which are consecutive.',
                        wrong=[{'g': 1, 'j': 4}, {'g': 3, 'j': 4}, {'g': 4, 'j': 2}]),
             ]),
             f2=FW('Change the conditions and re-test', 'Expert: what happens when a condition is replaced or added.', [
                 sa(WEEK + ' How many of the five talks could be on Friday?', 'Talks:',
                    str(sum(status(on(t, 5), W) != 'cannot' for t in 'FGHJK')),
                    'Fossils, Honey and Kites each appear on Friday in some schedule. Jazz cannot (condition 4) and Gears '
                    'cannot (it must be before Jazz).',
                    compute=lambda: str(sum(status(on(t, 5), W) != 'cannot' for t in 'FGHJK'))),
                 mc(WEEK + ' Suppose condition 3 is replaced by "Fossils is on Monday." Which statement must be true?',
                    'Jazz is on Wednesday or Thursday.',
                    [('Gears is on Tuesday.', 'Fossils, Kites, Gears, Jazz, Honey has Gears on Wednesday'),
                     ('Kites is on Friday.', 'Fossils, Gears, Jazz, Kites, Honey has Kites on Thursday'),
                     ('Honey is on Friday.', 'Fossils, Gears, Honey, Jazz, Kites has Honey on Wednesday')],
                    'The four schedules are F G H J K, F G J K H, F G K J H and F K G J H. Jazz is on Wednesday or Thursday '
                    'in each.', check=lambda t: status(st_fmon[t], f_mon) == 'must'),
                 tf(WEEK + ' Removing condition 4 adds exactly two new schedules.', False,
                    'Without condition 4 there are 14 schedules, which is 4 more than 10.',
                    check=lambda: len(weeks(WEEK_RULES[:3])) - len(W) == 2),
                 sa(WEEK + ' Add a fifth condition: no two of Gears, Honey and Jazz are on consecutive days. How many '
                           'schedules remain?', 'Schedules:',
                    str(len(weeks(extra=[lambda x: all(abs(x[a] - x[b]) != 1 for a, b in ('GH', 'GJ', 'HJ'))]))),
                    'Gears, Jazz and Honey must be on days 1, 3 and 5, so Gears is Monday, Jazz Wednesday, Honey Friday. '
                    'Fossils and Kites take Tuesday and Thursday in either order: 2 schedules.',
                    compute=lambda: str(len(weeks(extra=[lambda x: all(abs(x[a] - x[b]) != 1
                                                                       for a, b in ('GH', 'GJ', 'HJ'))])))),
                 tf(WEEK + ' If Gears is on Monday, then Fossils and Kites could be on Tuesday and Thursday.', True,
                    'Gears, Fossils, Jazz, Kites, Honey meets every condition.',
                    check=lambda: any(x['G'] == 1 and {x['F'], x['K']} == {2, 4} for x in W)),
             ]))


# ------------------------------------------------------------------ Set 36: search every case
def digits(n):
    return [int(c) for c in str(n)]


def coin_ways(total, coins):
    if not coins:
        return int(total == 0)
    c = coins[0]
    return sum(coin_ways(total - k * c, coins[1:]) for k in range(total // c + 1))


def clock_times():
    return [(h, m) for h in range(1, 13) for m in range(60)]


def clock_sum(h, m):
    return sum(digits(h)) + sum(digits(m // 10)) + m % 10


def ordered_sums(n):
    """Ordered ways to write n as a sum of 1s and 2s, counted by listing every sequence."""
    def go(left):
        return 1 if left == 0 else go(left - 1) + (go(left - 2) if left >= 2 else 0)
    return go(n)


def makeable(n, a=3, b=5):
    return any((n - a * i) % b == 0 for i in range(n // a + 1))


def s36():
    CLOCK = ('A 12-hour digital clock shows times from 1:00 to 12:59: the hour (1 to 12, no leading zero) and then two '
             'minute digits (00 to 59).')
    rect = sum(1 for r1 in range(3) for r2 in range(r1 + 1, 3) for c1 in range(4) for c2 in range(c1 + 1, 4))
    return S(36, 'Organize a complete case analysis and count or find every solution',
             main=[
                 sa('How many three-digit whole numbers (100 to 999) have digits that add up to 5?', 'Numbers:',
                    str(sum(1 for n in range(100, 1000) if sum(digits(n)) == 5)),
                    'Case by the hundreds digit: 1 leaves 4 for two digits (5 ways), 2 leaves 3 (4 ways), 3 leaves 2 '
                    '(3 ways), 4 leaves 1 (2 ways), 5 leaves 0 (1 way): 15.',
                    compute=lambda: str(sum(1 for n in range(100, 1000) if sum(digits(n)) == 5))),
                 sa(CLOCK + ' At how many times do the shown digits add up to exactly 22?', 'Times:',
                    str(sum(1 for h, m in clock_times() if clock_sum(h, m) == 22)),
                    'The minute digits add to at most 5 + 9 = 14, so the hour digits must add to at least 8: hours 8 and 9. '
                    'Hour 8 needs minutes adding to 14: 59. Hour 9 needs 13: 49 and 58. Three times: 8:59, 9:49, 9:58.',
                    compute=lambda: str(sum(1 for h, m in clock_times() if clock_sum(h, m) == 22))),
                 values('Find the two-digit whole number that equals 3 times the sum of its digits.', [('n', 'Number =')],
                        'isInteger(n) and n >= 10 and n <= 99 and n == 3 * (floor(n / 10) + mod(n, 10))', {'n': 27},
                        '27 = 3 x (2 + 7). Writing n = 10a + b, the condition 10a + b = 3a + 3b gives 7a = 2b, so a = 2, '
                        'b = 7 is the only digit solution.', wrong=[{'n': 18}, {'n': 72}, {'n': 30}],
                        search={'n': range(10, 100)}),
                 sa('In how many ways can you make 30 cents using nickels (5 cents), dimes (10 cents) and quarters (25 '
                    'cents)? You may use any number of each coin, including none; the order of the coins does not matter.',
                    'Ways:', str(coin_ways(30, [25, 10, 5])),
                    'With no quarter: 0, 1, 2 or 3 dimes, the rest nickels (4 ways). With one quarter: one nickel (1 way). '
                    'Total 5.', compute=lambda: str(coin_ways(30, [25, 10, 5]))),
                 tf('Exactly 6 of the 24 orderings of the letters A, B, C and D have A before B and also C before D.', True,
                    'Each of the conditions "A before B" and "C before D" holds in half of the orderings, independently: '
                    '24 / 2 / 2 = 6. Listing them confirms 6.',
                    check=lambda: sum(1 for p in itertools.permutations('ABCD')
                                      if p.index('A') < p.index('B') and p.index('C') < p.index('D')) == 6),
             ],
             back=[B('Strategy: make an organized list', 'guided_strategy',
                     'Students who list cases at random miss some or count some twice. Ordering the list by one choice at a '
                     'time makes it complete.',
                     lesson=lesson('Make an organized list',
                                   ['Pick the choice with the fewest options and go through its values in order.',
                                    'For each value, list what the rest can be, again in order.',
                                    'When every value has been handled, the list is complete; count it.'],
                                   'Worked example (a different count)',
                                   ['How many two-digit numbers have digits that add up to 4?'],
                                   ['Go through the tens digit in order: 1 gives 13, 2 gives 22, 3 gives 31, 4 gives 40.',
                                    'A tens digit of 5 or more is too big, and 0 is not allowed for a two-digit number. So '
                                    'there are 4.']),
                     qs=[
                         sa('How many two-digit numbers have digits that add up to 6?', 'Numbers:',
                            str(sum(1 for n in range(10, 100) if sum(digits(n)) == 6)), '15, 24, 33, 42, 51, 60: six.',
                            compute=lambda: str(sum(1 for n in range(10, 100) if sum(digits(n)) == 6))),
                         sa('In how many ways can you make 20 cents using only nickels and dimes? The order of the coins '
                            'does not matter.', 'Ways:', str(coin_ways(20, [10, 5])),
                            '0 dimes and 4 nickels, 1 dime and 2 nickels, 2 dimes: 3 ways.',
                            compute=lambda: str(coin_ways(20, [10, 5]))),
                         tf('There are exactly 4 two-digit numbers whose digits multiply to 12.', True,
                            'Tens digit 2, 3, 4, 6 gives 26, 34, 43, 62. Other tens digits do not divide 12 into a single '
                            'digit.', check=lambda: sum(1 for n in range(10, 100) if digits(n)[0] * digits(n)[1] == 12) == 4),
                         mc('Ana lists the ways to make 15 cents from nickels and dimes: "3 nickels; 1 dime and 1 nickel." '
                            'Is her list complete? The order of the coins does not matter.',
                            'Yes: she used 0 dimes and 1 dime, and 2 dimes is too much',
                            [('No: 2 dimes and no nickels is missing', '2 dimes make 20 cents, not 15'),
                             ('No: 1 dime alone is missing', '1 dime makes only 10 cents'),
                             ('No: a nickel then a dime is a third way', 'the order of the coins does not matter')],
                            'Organize by the number of dimes: 0 dimes needs 3 nickels, 1 dime needs 1 nickel, 2 dimes is too '
                            'much. Her two ways are all of them.'),
                         tf('There are 5 two-digit numbers whose digits add up to 3.', False,
                            'By tens digit: 12, 21, 30. There are 3.',
                            check=lambda: sum(1 for n in range(10, 100) if sum(digits(n)) == 3) == 5),
                     ])],
             f1=FW('Counting with extra conditions', 'Harder: complete searches with several conditions.', [
                 sa('How many three-digit numbers have three different digits that add up to 6?', 'Numbers:',
                    str(sum(1 for n in range(100, 1000) if sum(digits(n)) == 6 and len(set(digits(n))) == 3)),
                    'The digit sets are {0, 1, 5}, {0, 2, 4} and {1, 2, 3}. Each set with a 0 gives 4 numbers (0 cannot '
                    'lead), and {1, 2, 3} gives 6: 4 + 4 + 6 = 14.',
                    compute=lambda: str(sum(1 for n in range(100, 1000) if sum(digits(n)) == 6 and len(set(digits(n))) == 3))),
                 sa('In how many ways can 10 be written as a sum of 1s and 2s if the order matters? (For example, 3 can be '
                    'written 3 ways: 1 + 1 + 1, 1 + 2 and 2 + 1.)', 'Ways:', '89',
                    'Organize by the first number: ways(n) = ways(n - 1) + ways(n - 2). Starting 1, 2, 3, 5, 8, ... gives '
                    '89 for 10.', compute=lambda: str(ordered_sums(10))),
                 values('Find a three-digit number whose three digits are all odd, all different, and add up to 15.',
                        [('n', 'Number =')],
                        'isInteger(n) and n >= 100 and n <= 999 and isOdd(floor(n / 100)) and isOdd(mod(floor(n / 10), 10)) '
                        'and isOdd(mod(n, 10)) and floor(n / 100) + mod(floor(n / 10), 10) + mod(n, 10) == 15 and '
                        'floor(n / 100) != mod(floor(n / 10), 10) and floor(n / 100) != mod(n, 10) and '
                        'mod(floor(n / 10), 10) != mod(n, 10)', {'n': 159},
                        'The digit sets are {1, 5, 9} and {3, 5, 7}; any order works, for example 159 or 357.',
                        wrong=[{'n': 555}, {'n': 168}, {'n': 339}], search={'n': range(100, 1000)}),
                 tf('There are more ways to make 50 cents from nickels and dimes than from dimes and quarters. The order of '
                    'the coins does not matter.', True,
                    'Nickels and dimes: 0 to 5 dimes, 6 ways. Dimes and quarters: 5 dimes, or 2 quarters, 2 ways (1 quarter '
                    'leaves 25 cents, which dimes cannot make).',
                    check=lambda: coin_ways(50, [10, 5]) > coin_ways(50, [25, 10])),
                 mc('How many rectangles of any size (including squares) can be traced along the lines of a grid that is 2 '
                    'squares tall and 3 squares wide?', str(rect),
                    [('6', 'that counts only the single squares'),
                     ('15', 'that leaves out the three rectangles 2 squares tall and 1 wide'),
                     ('17', 'that leaves out the whole grid')],
                    'By size: 1 by 1: 6; 1 tall by 2 wide: 4; 1 by 3: 2; 2 tall by 1: 3; 2 by 2: 2; 2 by 3: 1. Total 18.',
                    check=lambda t: int(t) == rect),
             ]),
             f2=FW('Searches with many cases', 'Expert: split a large search into organized cases.', [
                 sa(CLOCK + ' At how many times do the shown digits add up to exactly 6?', 'Times:',
                    str(sum(1 for h, m in clock_times() if clock_sum(h, m) == 6)),
                    'Case by the hour: its digit sum s leaves 6 - s for the minutes; count minute pairs (tens 0 to 5) for '
                    'each hour and add.', compute=lambda: str(sum(1 for h, m in clock_times() if clock_sum(h, m) == 6))),
                 sa('In how many ways can you make 1 dollar (100 cents) using nickels, dimes and quarters? The order of the '
                    'coins does not matter.', 'Ways:', str(coin_ways(100, [25, 10, 5])),
                    'Case by quarters. 0 quarters: 0 to 10 dimes (11 ways). 1 quarter leaves 75: 0 to 7 dimes (8). 2 '
                    'quarters leave 50: 6. 3 quarters leave 25: 3. 4 quarters: 1. Total 29.',
                    compute=lambda: str(coin_ways(100, [25, 10, 5]))),
                 sa('How many positive whole numbers less than 1000 have digits that add up to 4?', 'Numbers:',
                    str(sum(1 for n in range(1, 1000) if sum(digits(n)) == 4)),
                    'One digit: 4 (1). Two digits: 13, 22, 31, 40 (4). Three digits: leading digit 1 to 4 leaves 3, 2, 1, 0 '
                    'for two digits: 4 + 3 + 2 + 1 = 10. Total 15.',
                    compute=lambda: str(sum(1 for n in range(1, 1000) if sum(digits(n)) == 4))),
                 tf('Every whole number of cents from 8 to 30 can be paid exactly using only 3-cent and 5-cent stamps.', True,
                    '8 = 3 + 5, 9 = 3 + 3 + 3, 10 = 5 + 5. Once three amounts in a row work, adding a 3-cent stamp reaches '
                    'every larger amount.', check=lambda: all(makeable(n) for n in range(8, 31))),
                 values('Give a whole number of cents from 1 to 10 that CANNOT be paid exactly using only 3-cent and 5-cent '
                        'stamps.', [('n', 'Amount =')], 'n == 1 or n == 2 or n == 4 or n == 7', {'n': 7},
                        'Checking 1 to 10: 3, 5, 6, 8, 9 and 10 can be made; 1, 2, 4 and 7 cannot.',
                        wrong=[{'n': 8}, {'n': 6}, {'n': 10}, {'n': 3}]),
             ]))


SETS = [s33(), s34(), s35(), s36()]
