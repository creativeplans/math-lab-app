"""Logic sets 45-48: letter grids and word squares; missing assumptions; enough information; digital displays."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson
import figs
from figs import SEG


# ------------------------------------------------------------------ Set 45: letter grids and word squares
def latin(n, given, letters):
    """Every completion of an n x n grid where each row and column holds each letter once. given: {(r, c): letter}."""
    out = []
    rows = list(itertools.permutations(letters))

    def go(r, acc):
        if r == n:
            out.append([''.join(x) for x in acc])
            return
        for p in rows:
            if all(p[c] == given[(r, c)] for c in range(n) if (r, c) in given) and \
                    all(p[c] != acc[k][c] for k in range(r) for c in range(n)):
                acc.append(p)
                go(r + 1, acc)
                acc.pop()
    go(0, [])
    return out


def grid_fig(n, given, shade=(), desc=''):
    rows = [''.join(given.get((r, c), '.') for c in range(n)) for r in range(n)]
    return (figs.letter_grid(rows, cell=40, shade=set(shade), bold=True).svg(),
            desc or 'A %d by %d letter grid; some cells hold letters, the rest are empty%s.'
            % (n, n, ', and one empty cell is shaded' if shade else ''))


LATIN = ('Rule: each row and each column must contain each of the letters %s exactly once.')
G4 = {(0, 0): 'A', (0, 3): 'C', (1, 0): 'C', (1, 2): 'D', (1, 3): 'B', (2, 3): 'D'}
G3 = {(0, 0): 'A', (1, 1): 'A'}
WORDS3 = ['CAT', 'ARE', 'TEN', 'ART', 'EAR', 'NET', 'TAN', 'ATE', 'RAT', 'ERA', 'TEA', 'ACE', 'ONE', 'NAP', 'APE', 'PEN',
          'OAR', 'ORE', 'ROE', 'TOE', 'TON', 'NOT', 'ANT']
WS = ('Word list (the ONLY words allowed): ' + ', '.join(WORDS3) + '. In a word square, the three rows, read left to right, '
      'are the same words as the three columns, read top to bottom, in the same order.')


def word_squares(first, words=WORDS3):
    return [[first, a, b] for a in words for b in words
            if [''.join(w[i] for w in (first, a, b)) for i in range(3)] == [first, a, b]]


def two_color(n, m, fixed):
    """Fillings of an n x m grid with A/B where side neighbors differ, matching fixed {(r, c): letter}."""
    out = []
    for bits in itertools.product('AB', repeat=n * m):
        g = {(r, c): bits[r * m + c] for r in range(n) for c in range(m)}
        if all(g[k] == v for k, v in fixed.items()) and all(
                g[(r, c)] != g[(r + dr, c + dc)] for r in range(n) for c in range(m) for dr, dc in ((0, 1), (1, 0))
                if r + dr < n and c + dc < m):
            out.append(g)
    return out


def s45():
    sol4 = latin(4, G4, 'ABCD')
    return S(45, 'Fill and analyze letter grids under stated rules and a supplied word list',
             main=[
                 sa(LATIN % 'A, B, C and D' + ' The grid in the figure has six letters filled in. Which letter belongs in '
                                            'the shaded cell (bottom row, first column)?', 'Letter:', sol4[0][3][0],
                    'Column 1 already has A (row 1) and C (row 2), so rows 3 and 4 start with B and D in some order. Row 3 '
                    'already has D (in column 4), so row 3 starts with B and row 4 starts with D. (The whole grid is ADBC, '
                    'CADB, BCAD, DBCA.)', compute=lambda: sol4[0][3][0] if len(sol4) == 1 else 'MISMATCH',
                    fig=grid_fig(4, G4, shade=[(3, 0)])),
                 values(WS + ' The first row of a word square is TEN. Give the second and third rows.',
                        [('w2', 'Row 2 ='), ('w3', 'Row 3 =')], "w2 == 'era' and w3 == 'nap'", {'w2': 'ERA', 'w3': 'NAP'},
                        'Column 1 must be TEN, so row 2 starts with E and row 3 with N. Row 2 = column 2, which starts with '
                        'E: ERA fits (E, R, A). Then column 3 is N, A, ?, and row 3 = NA?: NAP. Check: columns TEN, ERA, '
                        'NAP.', wrong=[{'w2': 'EAR', 'w3': 'NAP'}, {'w2': 'ERA', 'w3': 'NET'}],
                        method='Search of every pair of listed words: %d word square(s) start with TEN.'
                        % len(word_squares('TEN'))),
                 tf('Rule: a 3 by 3 grid is filled with the letters A and B so that no two cells that share a side hold the '
                    'same letter. The center cell holds A. Then all four corner cells hold the same letter.', True,
                    'The center\'s four side neighbors must be B, and each corner touches two of those B cells, so each '
                    'corner is A.', check=lambda: all(len({g[(0, 0)], g[(0, 2)], g[(2, 0)], g[(2, 2)]}) == 1
                                                      for g in two_color(3, 3, {(1, 1): 'A'}))),
                 mc(LATIN % 'A, B and C' + ' The top-left cell holds A and the center cell holds A. Which letter must go '
                                           'in the bottom-right cell?', 'A',
                    [('B', 'the grid can be completed only with A there'), ('C', 'the grid can be completed only with A '
                                                                                 'there'),
                     ('It could be B or C', 'A is already in rows 1 and 2 and in columns 1 and 2, so A must go in row 3, '
                                            'column 3')],
                    'Row 3 needs an A, but columns 1 and 2 already have one. So A goes in column 3 of row 3.',
                    check=lambda t: {g[2][2] for g in latin(3, G3, 'ABC')} == {t}, fig=grid_fig(3, G3)),
                 sa(LATIN % 'A, B and C' + ' The first row is A B C. How many ways are there to complete the grid?',
                    'Ways:', str(len(latin(3, {(0, 0): 'A', (0, 1): 'B', (0, 2): 'C'}, 'ABC'))),
                    'The second row must avoid the letter above each cell: B C A or C A B. Each choice forces the third row. '
                    'So 2 ways.', compute=lambda: str(len(latin(3, {(0, 0): 'A', (0, 1): 'B', (0, 2): 'C'}, 'ABC')))),
             ],
             back=[B('Strategy: fill the most constrained cell first', 'guided_strategy',
                     'Students guess letters and get stuck. Looking for a row, column or cell with only one possibility '
                     'turns the grid into a chain of forced steps.',
                     lesson=lesson('Fill the most constrained cell first',
                                   ['For each empty cell, list the letters its row and column have not used yet.',
                                    'A cell with only one possible letter is forced: fill it in.',
                                    'Also look along a row: if a letter can go in only one cell of that row, it goes there.',
                                    'Repeat. Each new letter removes options from other cells.'],
                                   'Worked example (a different grid)',
                                   ['Rule: each row and column of a 3 by 3 grid holds X, Y and Z once. Row 1 is X Y Z. Row 2 '
                                    'starts with Z.'],
                                   ['Row 2, column 2 cannot be Y (column) or Z (row), so it is X. Row 2 is Z X Y.',
                                    'Row 3 gets the letter missing from each column: Y Z X.']),
                     qs=[
                         sa(LATIN % 'A, B and C' + ' A row reads A _ C. Which letter fills the gap?', 'Letter:', 'B',
                            'Each row holds A, B and C once, and only B is missing.', compute=lambda: 'B'),
                         tf(LATIN % 'A, B and C' + ' If column 1 holds A and B, its third cell must hold C.', True,
                            'C is the only letter not yet used in that column.'),
                         mc(LATIN % 'A, B, C and D' + ' A cell\'s row already holds A and D, and its column holds B. Which '
                                                     'letter must go in the cell?', 'C',
                            [('A', 'A is already in the row'), ('B', 'B is already in the column'),
                             ('D', 'D is already in the row')], 'Only C is used by neither the row nor the column.',
                            check=lambda t: t not in 'ADB'),
                         tf(LATIN % 'A, B and C' + ' A grid can have the row A B C directly above the row A C B.', False,
                            'Both rows put A in column 1, so column 1 would have A twice.'),
                         sa(LATIN % 'A, B and C' + ' Rows 1 and 2 are A B C and C A B. What is row 3? Type the three '
                                                  'letters with no spaces.', 'Row 3:', 'BCA',
                            'Each column needs its missing letter: column 1 has A, C so B; column 2 has B, A so C; column 3 '
                            'has C, B so A.', compute=lambda: latin(3, {(0, 0): 'A', (0, 1): 'B', (0, 2): 'C', (1, 0): 'C',
                                                                      (1, 1): 'A', (1, 2): 'B'}, 'ABC')[0][2]),
                     ])],
             f1=FW('Word squares from a list', 'Harder: word squares and larger grids.', [
                 values(WS + ' The first row of a word square is ATE. Give the second and third rows.',
                        [('w2', 'Row 2 ='), ('w3', 'Row 3 =')], "w2 == 'tea' and w3 == 'ear'", {'w2': 'TEA', 'w3': 'EAR'},
                        'Row 2 = column 2 starts with T, and row 3 = column 3 starts with E. TEA and EAR fit: columns ATE, '
                        'TEA, EAR.', wrong=[{'w2': 'TEN', 'w3': 'EAR'}, {'w2': 'TAN', 'w3': 'ERA'}],
                        method='Search: %d word square(s) start with ATE.' % len(word_squares('ATE'))),
                 sa(WS + ' How many words on the list can be the first row of at least one word square?', 'Words:',
                    str(sum(1 for w in WORDS3 if word_squares(w))),
                    'A search of every pair of words for each possible first row finds the squares; count the first rows '
                    'that work.', compute=lambda: str(sum(1 for w in WORDS3 if word_squares(w)))),
                 tf(WS + ' A word square can start with the row ONE.', False,
                    'Row 2 must start with N (NET, NAP or NOT) and row 3 with E. The middle letter of row 3 must equal the '
                    'last letter of row 2 (T or P), but no listed word starts with ET or EP.',
                    check=lambda: bool(word_squares('ONE'))),
                 sa(LATIN % 'A, B, C and D' + ' The grid in the figure has six letters filled in. Type the complete top row '
                                             '(four letters, no spaces).', 'Row 1:', sol4[0][0],
                    'Row 2 is C _ D B, so its gap is A. Column 4 needs A in row 4. Continuing cell by cell gives the only '
                    'completion: ADBC, CADB, BCAD, DBCA.', compute=lambda: sol4[0][0], fig=grid_fig(4, G4)),
                 mc('Rule: a 2 by 3 grid is filled with A and B so that no two cells sharing a side hold the same letter. How '
                    'many such grids are there?', str(len(two_color(2, 3, {}))),
                    [('1', 'the top-left cell can be either letter'), ('4', 'once the top-left cell is chosen, every other '
                                                                          'cell is forced'),
                     ('6', 'that counts cells, not grids')],
                    'The top-left letter decides the whole checkerboard pattern: 2 grids.',
                    check=lambda t: int(t) == len(two_color(2, 3, {}))),
             ]),
             f2=FW('Prove a grid is impossible or count it', 'Expert: counting completions and impossibility.', [
                 sa(LATIN % 'A, B, C and D' + ' How many ways are there to fill the whole grid if the first row is A B C D?',
                    'Ways:', str(len(latin(4, {(0, i): 'ABCD'[i] for i in range(4)}, 'ABCD'))),
                    'Count the second rows that avoid the letter above each cell (9 ways), then the completions of each '
                    '(search): 24 in all.', compute=lambda: str(len(latin(4, {(0, i): 'ABCD'[i] for i in range(4)}, 'ABCD')))),
                 tf('Rule: a 3 by 3 grid is filled with A and B so that no two cells sharing a side hold the same letter. The '
                    'top-left cell holds A and the top-right cell holds B.', False,
                    'The top row must alternate A, B, A, so its two ends match. A grid with A and B at the two top corners '
                    'breaks the rule.', check=lambda: bool(two_color(3, 3, {(0, 0): 'A', (0, 2): 'B'}))),
                 mc(LATIN % 'A, B and C' + ' Which partly filled grid can NOT be completed?',
                    'Row 1 starts A B, and row 2 ends in C',
                    [('Row 1 is A B C', 'it can be completed in 2 ways'),
                     ('Row 1 starts A, and row 2 starts B', 'for example A B C, B C A, C A B'),
                     ('The diagonal from top left to bottom right is A, A, A', 'for example A B C, C A B, B C A')],
                    'Row 1 is A B _, so its last cell must be C. But column 3 already has C in row 2, so no letter fits.',
                    check=lambda t: not latin(3, PARTIAL[t], 'ABC')),
                 values(WS + ' Give the second and third rows of the word square whose first row is ROE.',
                        [('w2', 'Row 2 ='), ('w3', 'Row 3 =')], "w2 == 'oar' and w3 == 'era'", {'w2': 'OAR', 'w3': 'ERA'},
                        'Row 2 starts with O and row 3 with E. OAR and ERA give columns ROE, OAR, ERA.',
                        wrong=[{'w2': 'ORE', 'w3': 'ERA'}, {'w2': 'OAR', 'w3': 'EAR'}],
                        method='Search: %d word square(s) start with ROE.' % len(word_squares('ROE'))),
                 sa(LATIN % 'A, B and C' + ' How many ways are there to fill an empty 3 by 3 grid?', 'Ways:',
                    str(len(latin(3, {}, 'ABC'))),
                    'The first row can be any of the 6 orders of A, B, C, and each has 2 completions: 12.',
                    compute=lambda: str(len(latin(3, {}, 'ABC')))),
             ]))


PARTIAL = {'Row 1 starts A B, and row 2 ends in C': {(0, 0): 'A', (0, 1): 'B', (1, 2): 'C'},
           'Row 1 is A B C': {(0, 0): 'A', (0, 1): 'B', (0, 2): 'C'},
           'Row 1 starts A, and row 2 starts B': {(0, 0): 'A', (1, 0): 'B'},
           'The diagonal from top left to bottom right is A, A, A': {(0, 0): 'A', (1, 1): 'A', (2, 2): 'A'}}


# ------------------------------------------------------------------ Set 46: explanations and missing assumptions
ASM = 'An assumption is an unstated statement that an argument needs in order for its conclusion to follow.'


def s46():
    return S(46, 'Identify the unstated assumption an argument needs and evaluate competing explanations',
             main=[
                 mc(ASM + ' "The school\'s robot passed every test in the lab, so it will work at the competition." Which '
                          'assumption does this argument need?', 'Conditions at the competition are like those in the lab.',
                    [('The robot was built by students.', 'who built it does not connect the lab results to the competition'),
                     ('The robot failed some tests last year.', 'that is about the past and weakens nothing here'),
                     ('Other teams also tested their robots.', 'other teams\' testing is irrelevant to this robot')],
                    'Lab success supports competition success only if the two settings are alike.'),
                 mc(ASM + ' "Mia\'s plant grew faster after she moved it to the window, so sunlight made it grow faster." '
                          'Which assumption does this argument need?', 'Nothing else that affects growth changed when the '
                                                                       'plant was moved.',
                    [('Plants need water to grow.', 'true, but it does not link the move to the faster growth'),
                     ('The window faces south.', 'the direction is not needed for the conclusion'),
                     ('Mia has other plants indoors.', 'other plants are not part of the argument')],
                    'If the temperature or watering also changed, those could explain the faster growth instead.'),
                 tf(ASM + ' "Every member of the chess club is in grade 10. Jo is in grade 10. So Jo is in the chess club." '
                          'This argument would become valid if we add the assumption "Everyone in grade 10 is in the chess '
                          'club."', True,
                    'With that added premise, Jo being in grade 10 forces Jo into the club. The original premise points '
                    'the other way.'),
                 mc('The cafeteria sold fewer sandwiches this week than last week. Which explanation is best supported if '
                    'we also learn that the cafeteria was closed on two days this week?',
                    'The cafeteria was open on fewer days to sell sandwiches.',
                    [('Students stopped liking sandwiches.', 'nothing given says tastes changed'),
                     ('The sandwich price went up.', 'nothing given mentions prices'),
                     ('Fewer students attend the school this year.', 'the comparison is week to week, and enrollment was '
                                                                     'not mentioned')],
                    'The given fact directly explains fewer sales without any other change.'),
                 tf(ASM + ' "This bridge is safe because it has stood for 80 years." The argument needs the assumption '
                          'that the bridge will be used the same way as it has been.', True,
                    'If much heavier loads start crossing, 80 years of standing would say little about safety under the '
                    'new loads.'),
             ],
             back=[B('Find the gap between premise and conclusion', 'guided_strategy',
                     'Students choose statements that are true or related instead of ones the argument needs. Looking for '
                     'the gap between what is given and what is concluded points straight to the assumption.',
                     lesson=lesson('Find the gap between premise and conclusion',
                                   ['Write the premise and the conclusion side by side.',
                                    'Find a word or idea in the conclusion that the premise never mentions, or a jump from '
                                    '"some" to "all" or from "then" to "now".',
                                    'The assumption is the statement that bridges that gap. Test it: if the assumption were '
                                    'false, the conclusion should no longer follow.'],
                                   'Worked example (a different argument)',
                                   ['"Leo practiced piano every day this month, so he will win the recital prize."'],
                                   ['Gap: daily practice to winning the prize.',
                                    'Needed assumption: practicing every day is enough to play better than the other '
                                    'players. If it were false, the conclusion would not follow.']),
                     qs=[
                         mc(ASM + ' "Sam is taller than Ana, so Sam is taller than Raj." Which assumption fills the gap?',
                            'Ana is at least as tall as Raj.',
                            [('Raj is taller than Ana.', 'that would make the conclusion less certain, not more'),
                             ('Sam is the tallest in his class.', 'Raj may not be in Sam\'s class'),
                             ('Ana and Raj are friends.', 'friendship says nothing about height')],
                            'Sam > Ana and Ana >= Raj give Sam > Raj.'),
                         tf(ASM + ' Every true statement about the topic of an argument is an assumption that the argument needs.', False,
                            'A true fact that does not bridge the gap between premise and conclusion is not needed by the argument.'),
                         mc(ASM + ' "The park was crowded on Saturday, so it will be crowded this Saturday." What is the '
                                  'gap?', 'From one past Saturday to a future Saturday',
                            [('From the park to the city', 'the argument never mentions a city'),
                             ('From crowded to empty', 'the conclusion also says crowded'),
                             ('From Saturday to Sunday', 'both days in the argument are Saturdays')],
                            'The argument needs this Saturday to be like the last one.'),
                         tf(ASM + ' If an assumption an argument needs turns out to be false, the conclusion no longer '
                                  'follows from the premises.', True, 'That is what it means for the argument to need it.'),
                         tf(ASM + ' "All squares are rectangles, so all rectangles are squares" needs no assumption to be '
                                  'valid.', False,
                            'It reverses the premise. It would need the extra premise "all rectangles are squares", which is '
                            'false.'),
                     ])],
             f1=FW('Weaken and strengthen explanations', 'Harder: facts that support or undercut an explanation.', [
                 mc('Claim: "Students who eat breakfast score higher on tests, so eating breakfast raises test scores." Which '
                    'fact would most WEAKEN the claim?',
                    'Students who eat breakfast also sleep more, and sleep is linked to higher scores.',
                    [('Many students eat breakfast.', 'how common breakfast is does not affect the link'),
                     ('Test scores rose last year.', 'a general rise does not touch the breakfast link'),
                     ('Breakfast foods are cheap.', 'price does not touch the link between breakfast and scores')],
                    'Another factor (sleep) could explain both, so breakfast might not be the cause.'),
                 mc('Claim: "The new crosswalk signal reduced accidents at Elm Street." Which fact would most STRENGTHEN the '
                    'claim?', 'Accidents did not drop at similar streets that did not get the signal.',
                    [('The signal cost a lot of money.', 'cost says nothing about the effect'),
                     ('Elm Street is near a school.', 'location alone does not show the signal worked'),
                     ('Drivers like the new signal.', 'liking it does not show accidents fell because of it')],
                    'If accidents fell only where the signal was added, the signal is the likely cause.'),
                 tf(ASM + ' "No reptiles have fur. This animal has fur. So this animal is not a reptile." This argument needs '
                          'an unstated assumption to be valid.', False,
                    'It is already valid: if it were a reptile, it would have no fur, but it has fur.'),
                 mc(ASM + ' "Our team lost every game we played in the rain. It will rain on Friday. So we will lose '
                          'Friday\'s game." Which assumption does the argument need?',
                    'The rain caused the losses, rather than something else about those games.',
                    [('Our team has played in the rain before.', 'that is already stated in the premise'),
                     ('Friday\'s game is at home.', 'location is not part of the argument'),
                     ('It rains more in the spring.', 'that does not connect rain to losing')],
                    'The past pattern predicts Friday only if rain is the reason for the losses.'),
                 tf('Two explanations both fit the facts. Then no new fact can help decide between them.', False,
                    'A new fact that one explanation predicts and the other does not supports the first over the second.'),
             ]),
             f2=FW('Judge explanations with care', 'Expert: alternative explanations and hidden assumptions.', [
                 mc('A town\'s ice-cream sales and its number of sunburns rise and fall together during the year. Which '
                    'explanation is best?', 'Hot, sunny weather increases both.',
                    [('Eating ice cream causes sunburn.', 'nothing suggests ice cream affects skin'),
                     ('Sunburns make people buy ice cream.', 'the timing fits weather better than this'),
                     ('The two numbers match by chance every year.', 'a yearly pattern is unlikely to be chance alone')],
                    'A common cause (weather) explains why the two move together.'),
                 mc(ASM + ' "Ming read the book, so Ming knows how it ends." Which assumption is needed?',
                    'Ming read the book all the way to the end.',
                    [('The book has a surprise ending.', 'the type of ending does not matter'),
                     ('Ming liked the book.', 'liking it is not needed to know the ending'),
                     ('The book is long.', 'length is not needed for the conclusion')],
                    'Reading part of the book would not reveal the ending.'),
                 tf(ASM + ' "Every prize winner practiced daily. Kai practiced daily. So Kai won a prize." Adding "Only prize '
                          'winners practiced daily" makes the argument valid.', True,
                    'Then anyone who practiced daily is a prize winner, and Kai practiced daily.'),
                 mc('A survey of the chess club finds that 90% of members prefer quiet study rooms. A student concludes that '
                    '90% of the whole school prefers quiet study rooms. What assumption does this need?',
                    'Chess club members have the same preferences as the whole school.',
                    [('The chess club has more than 10 members.', 'size alone does not make the club like the school'),
                     ('Quiet rooms are better for studying.', 'that does not link the club to the school'),
                     ('The survey asked about study rooms.', 'that is already part of the information')],
                    'The conclusion jumps from one group to the school; it needs the group to represent the school.'),
                 tf('If a needed assumption is shown to be false, the conclusion of the argument must be false.', False,
                    'The argument fails, but the conclusion could still be true for other reasons.'),
             ]))


# ------------------------------------------------------------------ Set 47: is there enough information?
SUFF = ['Clue (1) alone is enough, but clue (2) alone is not.', 'Clue (2) alone is enough, but clue (1) alone is not.',
        'Neither clue alone is enough, but both together are.', 'Each clue alone is enough.']
SUFF_NOTE = ('Decide whether each clue, alone or together with the other, is enough to answer the question with exactly one '
             'answer. (In each of these questions, the two clues together are enough.)')


def enough(domain, ask, pred):
    return len({ask(x) for x in domain if pred(x)}) == 1


def suff_choice(domain, ask, c1, c2):
    e1, e2 = enough(domain, ask, c1), enough(domain, ask, c2)
    assert enough(domain, ask, lambda x: c1(x) and c2(x))
    return SUFF[3] if e1 and e2 else SUFF[0] if e1 else SUFF[1] if e2 else SUFF[2]


def suff_mc(prompt, domain, ask, c1, c2, why):
    key = suff_choice(domain, ask, c1, c2)
    reasons = {SUFF[0]: 'check whether clue (1) alone leaves exactly one answer',
               SUFF[1]: 'check whether clue (2) alone leaves exactly one answer',
               SUFF[2]: 'check each clue alone before combining them',
               SUFF[3]: 'one of the clues alone leaves more than one answer'}
    return mc(SUFF_NOTE + ' ' + prompt, key, [(t, reasons[t]) for t in SUFF if t != key], why,
              check=lambda t: t == suff_choice(domain, ask, c1, c2))


RACE = list(itertools.permutations('ABC'))  # finishing order, first to last


def s47():
    nums = range(1, 21)
    return S(47, 'Decide whether the given information determines the answer, and what extra fact would',
             main=[
                 suff_mc('Ana, Ben and Cal ran a race with no ties. Who finished first? Clue (1): Ana finished ahead of Ben. '
                         'Clue (2): Cal finished last.', RACE, lambda o: o[0],
                         lambda o: o.index('A') < o.index('B'), lambda o: o[2] == 'C',
                         'Clue (1) allows A B C, A C B and C A B (first could be Ana or Cal). Clue (2) allows A B C and '
                         'B A C. Together only A B C: Ana.'),
                 suff_mc('x is a whole number from 1 to 20. What is x? Clue (1): x is a multiple of 7 and greater than 10. '
                         'Clue (2): x is even.', nums, lambda x: x, lambda x: x % 7 == 0 and x > 10, lambda x: x % 2 == 0,
                         'Clue (1) leaves only 14. Clue (2) leaves 10 numbers.'),
                 tf('Two whole numbers, each from 1 to 9, add up to 17. Knowing only this is enough to know which two '
                    'numbers they are.', True, 'Only 8 + 9 = 17 (in either order).',
                    check=lambda: len({frozenset((a, b)) for a in range(1, 10) for b in range(1, 10) if a + b == 17}) == 1),
                 suff_mc('A rectangle has whole-number side lengths. What is its area? Clue (1): its perimeter is 12. '
                         'Clue (2): one side is twice as long as the other.',
                         [(w, h) for w in range(1, 13) for h in range(1, 13)], lambda s: s[0] * s[1],
                         lambda s: 2 * (s[0] + s[1]) == 12, lambda s: s[0] == 2 * s[1] or s[1] == 2 * s[0],
                         'Clue (1) allows 1 by 5, 2 by 4, 3 by 3 (areas 5, 8, 9). Clue (2) allows 1 by 2, 2 by 4, and more. '
                         'Together: 2 by 4, area 8.'),
                 sa('x is a whole number from 1 to 50. You know that x is a multiple of 6 and also a multiple of 4. How many '
                    'values of x are still possible?', 'Values:',
                    str(sum(1 for x in range(1, 51) if x % 6 == 0 and x % 4 == 0)),
                    'Multiples of both 6 and 4 are multiples of 12: 12, 24, 36, 48. Four values remain, so the clues are '
                    'not enough to find x.',
                    compute=lambda: str(sum(1 for x in range(1, 51) if x % 6 == 0 and x % 4 == 0))),
             ],
             back=[B('Strategy: list what each clue leaves', 'guided_strategy',
                     'Students decide "enough" by feel. Listing every possibility each clue leaves makes the decision '
                     'exact: one possibility left means enough.',
                     lesson=lesson('List what each clue leaves',
                                   ['List every possibility allowed before any clue.',
                                    'Cross out the ones a clue rules out. If exactly one answer remains, the clue is '
                                    'enough.',
                                    'Do this for each clue alone, then for the clues together.'],
                                   'Worked example (a different question)',
                                   ['n is a whole number from 1 to 10. What is n? Clue (1): n is odd. Clue (2): n is a '
                                    'multiple of 3.'],
                                   ['Clue (1) leaves 1, 3, 5, 7, 9: not enough. Clue (2) leaves 3, 6, 9: not enough.',
                                    'Together: 3 and 9. Still not enough: a third clue is needed.']),
                     qs=[
                         sa('n is a whole number from 1 to 10, and n is a multiple of 4. How many values of n are '
                            'possible?', 'Values:', '2', '4 and 8.',
                            compute=lambda: str(sum(1 for n in range(1, 11) if n % 4 == 0))),
                         tf('n is a whole number from 1 to 10. Knowing that n is prime and even is enough to find n.', True,
                            '2 is the only even prime.', check=lambda: enough(range(1, 11), lambda n: n,
                                                                            lambda n: n == 2)),
                         tf('Two whole numbers add to 10. Knowing only this is enough to find the larger number.', False,
                            '1 + 9, 2 + 8, 3 + 7, 4 + 6 and 5 + 5 all work.'),
                         mc('A clue is "enough" to answer a question when...', 'exactly one answer is left after using it.',
                            [('at least one answer is left after using it.', 'two or more answers left means not enough'),
                             ('it rules out at least one answer.', 'it may still leave several answers'),
                             ('it is true.', 'a true clue can still leave several answers')],
                            'Enough means the answer is determined.'),
                         sa('n is a whole number from 1 to 20. Clue: n is a square number and n is odd. How many values of n '
                            'are left?', 'Values:', '2', '1 and 9.',
                            compute=lambda: str(sum(1 for n in range(1, 21) if int(n ** 0.5) ** 2 == n and n % 2 == 1))),
                     ])],
             f1=FW('Which clue is enough?', 'Harder: clues about orders, ages and numbers.', [
                 suff_mc('Four friends sit in a row of four seats numbered 1 to 4: Dee, Eli, Fay and Gus. Who sits in seat 1? '
                         'Clue (1): Dee sits in seat 4. Clue (2): Eli sits directly left of Fay, and Gus sits directly left '
                         'of Eli.', list(itertools.permutations('DEFG')), lambda o: o[0], lambda o: o[3] == 'D',
                         lambda o: o.index('E') + 1 == o.index('F') and o.index('G') + 1 == o.index('E'),
                         'Clue (2) forces G E F together in that order, so the order is G E F D or D G E F: not enough. Clue '
                         '(1) alone leaves 6 orders. Together: G E F D, so Gus.'),
                 suff_mc('Pat is older than Quinn. How old is Quinn, in whole years? Clue (1): their ages add to 30. Clue '
                         '(2): Pat is 4 years older than Quinn.', [(p, q) for p in range(1, 60) for q in range(1, 60) if p > q],
                         lambda a: a[1], lambda a: a[0] + a[1] == 30, lambda a: a[0] - a[1] == 4,
                         'Clue (1) allows many pairs (16, 14), (20, 10), ... Clue (2) allows many pairs. Together: P + Q = 30 '
                         'and P - Q = 4, so Q = 13.'),
                 suff_mc('n is a whole number from 1 to 30. What is n? Clue (1): n leaves remainder 1 when divided by 7. Clue '
                         '(2): n is a perfect square.', range(1, 31), lambda n: n,
                         lambda n: n % 7 == 1, lambda n: int(n ** 0.5) ** 2 == n,
                         'Clue (1) allows 1, 8, 15, 22, 29. Clue (2) allows 1, 4, 9, 16, 25. Only 1 is in both lists.'),
                 tf('A bag holds only red and blue marbles, 12 in all. Knowing that there are 4 more red marbles than blue '
                    'ones is enough to find the number of red marbles.', True, 'r + b = 12 and r - b = 4 give r = 8.',
                    check=lambda: enough([(r, 12 - r) for r in range(13)], lambda x: x[0], lambda x: x[0] - x[1] == 4)),
                 values('x is a whole number from 1 to 20 and x is a multiple of 3. Give one extra clue as a single number: '
                        'a value m from 2 to 10 such that knowing "x is also a multiple of m" leaves exactly one possible x.',
                        [('m', 'm =')], 'm == 4 or m == 5', {'m': 4},
                        'The multiples of 3 up to 20 are 3, 6, 9, 12, 15, 18. "Also a multiple of 4" leaves only 12, and "also '
                        'a multiple of 5" leaves only 15. Other values of m leave none or several.',
                        wrong=[{'m': 2}, {'m': 6}, {'m': 9}, {'m': 7}],
                        method='Checked every m from 2 to 10: exactly one x remains for m = %s.'
                        % [m for m in range(2, 11) if sum(1 for x in range(1, 21) if x % 3 == 0 and x % m == 0) == 1]),
             ]),
             f2=FW('Design the missing clue', 'Expert: find what extra fact would settle the question.', [
                 suff_mc('n is a whole number from 1 to 20. What is n? Clue (1): n + 5 = 12. Clue (2): 2n = 14.', range(1, 21),
                         lambda n: n, lambda n: n + 5 == 12, lambda n: 2 * n == 14, 'Each clue alone gives n = 7.'),
                 suff_mc('n is a whole number from 1 to 20. What is n? Clue (1): n is odd. Clue (2): n is a multiple of 13.',
                         range(1, 21), lambda n: n, lambda n: n % 2 == 1, lambda n: n % 13 == 0,
                         'Clue (2) alone leaves only 13 (26 is too big). Clue (1) leaves 10 odd numbers.'),
                 values('Two whole numbers from 1 to 9 multiply to 12. Give a sum s such that also knowing "the two numbers add '
                        'to s" tells you exactly which two numbers they are.', [('s', 's =')], 's == 7 or s == 8', {'s': 7},
                        'The pairs with product 12 are 2 and 6 (sum 8) and 3 and 4 (sum 7). Either sum picks out one pair.',
                        wrong=[{'s': 13}, {'s': 6}, {'s': 12}],
                        method='Checked every sum from 2 to 18: the pair is determined for s = %s.'
                        % [t for t in range(2, 19) if len({frozenset((a, b)) for a in range(1, 10) for b in range(1, 10)
                                                          if a * b == 12 and a + b == t}) == 1]),
                 tf('Two whole numbers, each from 1 to 9, multiply to 36. Knowing only this is enough to know which two '
                    'numbers they are.', False, 'Both 4 x 9 and 6 x 6 equal 36.',
                    check=lambda: len({frozenset((a, b)) for a in range(1, 10) for b in range(1, 10) if a * b == 36}) == 1),
                 sa('Three different whole numbers from 1 to 9 add up to 23. How many different sets of three numbers are '
                    'possible?', 'Sets:', str(sum(1 for c in itertools.combinations(range(1, 10), 3) if sum(c) == 23)),
                    'The largest possible total is 9 + 8 + 7 = 24. To get 23, lower one number by 1 without repeating: only '
                    '9 + 8 + 6. So the total alone is enough to find the set.',
                    compute=lambda: str(sum(1 for c in itertools.combinations(range(1, 10), 3) if sum(c) == 23))),
             ]))


# ------------------------------------------------------------------ Set 48: digital displays
ROT = dict(a='d', b='e', c='f', d='a', e='b', f='c', g='g')
INV = {frozenset(v): k for k, v in SEG.items()}
DISPLAY = ('Digits are shown on a seven-segment display exactly as in the reference figure (0 to 9). Turning the display '
           'upside down means a half turn; a turned digit counts as a digit only if its lit segments are exactly those of '
           'a digit in the reference figure.')


def segs(s):
    return sum(len(SEG[d]) for d in s)


def turned(d):
    return INV.get(frozenset(ROT[x] for x in SEG[d]))


def turned_number(s):
    out = [turned(d) for d in reversed(s)]
    return None if None in out else ''.join(out)


def move_one(d):
    v = set(SEG[d])
    return sorted({INV[frozenset(v - {r} | {a})] for r in v for a in 'abcdefg' if a not in v
                   and frozenset(v - {r} | {a}) in INV})


REF = (figs.seven('0123456789', w=26, h=46, gap=12).svg(), 'Reference: the digits 0 to 9 on a seven-segment display.')


def s48():
    return S(48, 'Reason about seven-segment digits: segments used, rotations and segment moves',
             main=[
                 sa(DISPLAY + ' How many segments are lit when the display shows 2026?', 'Segments:', str(segs('2026')),
                    '2 uses 5, 0 uses 6, 2 uses 5, 6 uses 6: 22.', compute=lambda: str(segs('2026')), fig=REF),
                 mc(DISPLAY + ' Which digit uses exactly 3 lit segments?', '7',
                    [('1', '1 uses 2 segments'), ('4', '4 uses 4 segments'), ('2', '2 uses 5 segments')],
                    '7 lights the top bar and the two right-hand segments.', check=lambda t: len(SEG[t]) == 3, fig=REF),
                 tf(DISPLAY + ' When the display showing 69 is turned upside down, it shows 69 again.', True,
                    'A half turn turns 6 into 9 and 9 into 6, and also reverses their order: 69 becomes 69.',
                    check=lambda: turned_number('69') == '69', fig=REF),
                 values(DISPLAY + ' Give a digit that looks exactly the same after the display is turned upside down.',
                        [('d', 'Digit =')], 'd == 0 or d == 2 or d == 5 or d == 8', {'d': 8},
                        '0, 2, 5 and 8 are unchanged by a half turn. 6 and 9 swap, and 1, 3, 4, 7 do not become digits.',
                        wrong=[{'d': 6}, {'d': 1}, {'d': 9}, {'d': 3}], fig=REF,
                        method='Checked by turning every digit: unchanged digits %s.'
                        % [d for d in '0123456789' if turned(d) == d]),
                 mc(DISPLAY + ' Exactly one lit segment of the digit 2 is moved to an unlit position. Which digit can '
                              'result?', move_one('2')[0],
                    [('5', 'turning 2 into 5 needs two segments moved'), ('8', '8 has more segments than 2'),
                     ('7', '7 has fewer segments than 2')],
                    'Move the lower-left segment to the lower-right position: 2 becomes 3.',
                    check=lambda t: t in move_one('2'), fig=REF),
             ],
             back=[B('Read the segments of each digit', 'prerequisite',
                     'Every display puzzle depends on knowing which segments each digit lights.',
                     qs=[
                         sa(DISPLAY + ' How many segments does the digit 4 light?', 'Segments:', str(len(SEG['4'])),
                            'Upper left, middle, and both right-hand segments: 4.', compute=lambda: str(len(SEG['4'])),
                            fig=REF),
                         tf(DISPLAY + ' The digit 8 lights all seven segments.', True, '8 uses every segment.',
                            check=lambda: len(SEG['8']) == 7, fig=REF),
                         mc(DISPLAY + ' Which digit lights the fewest segments?', '1',
                            [('7', '7 lights 3'), ('4', '4 lights 4'), ('0', '0 lights 6')], '1 lights only 2 segments.',
                            check=lambda t: len(SEG[t]) == min(len(v) for v in SEG.values()), fig=REF),
                         tf(DISPLAY + ' The digits 0 and 6 light the same number of segments.', True,
                            'Each lights 6 segments (in different positions).', check=lambda: len(SEG['0']) == len(SEG['6']),
                            fig=REF),
                         tf(DISPLAY + ' The digit 3 lights the middle segment and both left-hand segments.', False,
                            '3 lights the top, middle, bottom and both right-hand segments; no left-hand ones.', fig=REF,
                            check=lambda: {'e', 'f', 'g'} <= set(SEG['3'])),
                     ])],
             f1=FW('Turned displays and segment counts', 'Harder: whole numbers turned upside down.', [
                 sa(DISPLAY + ' The display shows 1958. How many segments are lit?', 'Segments:', str(segs('1958')),
                    '2 + 6 + 5 + 7 = 20.', compute=lambda: str(segs('1958')), fig=REF),
                 mc(DISPLAY + ' The display shows 625. What does it show after being turned upside down?', '529',
                    [('526', 'the 6 also turns into a 9'), ('925', 'the order of the digits is also reversed'),
                     ('It does not show a number', '6, 2 and 5 all turn into digits')],
                    'Reverse the order and turn each digit: 5 stays 5, 2 stays 2, 6 becomes 9: 529.',
                    check=lambda t: turned_number('625') == t, fig=REF),
                 tf(DISPLAY + ' The display showing 1001 still shows a number after it is turned upside down.', False,
                    'The 1 lights the two right-hand segments; turned, they become the two left-hand segments, which is '
                    'not a digit in the reference.', check=lambda: turned_number('1001') is not None, fig=REF),
                 sa(DISPLAY + ' How many two-digit numbers (10 to 99) still show a number after the display is turned upside '
                              'down?', 'Numbers:',
                    str(sum(1 for n in range(10, 100) if turned_number(str(n)))),
                    'Both digits must be from 0, 2, 5, 6, 8, 9; the first cannot be 0: 5 x 6 = 30.',
                    compute=lambda: str(sum(1 for n in range(10, 100) if turned_number(str(n)))), fig=REF),
                 values(DISPLAY + ' Give a digit d such that adding exactly one lit segment to d (moving nothing) makes '
                                  'the digit 8.', [('d', 'd =')], 'd == 0 or d == 6 or d == 9', {'d': 0},
                        '0, 6 and 9 each light 6 segments, and each is 8 with one segment missing.',
                        wrong=[{'d': 5}, {'d': 3}, {'d': 8}], fig=REF,
                        method='Checked: digits one segment short of 8: %s.'
                        % [d for d in SEG if len(SEG[d]) == 6 and set(SEG[d]) < set(SEG['8'])]),
             ]),
             f2=FW('Segment moves and best displays', 'Expert: moves, budgets and maximum values.', [
                 values(DISPLAY + ' Exactly one lit segment of the digit 3 is moved to an unlit position. Give a digit that '
                                  'can result.', [('d', 'Digit =')], 'd == 2 or d == 5', {'d': 5},
                        'Move the upper-right segment to the upper left to make 5, or the lower-right segment to the lower '
                        'left to make 2.', wrong=[{'d': 9}, {'d': 8}, {'d': 3}], fig=REF,
                        method='Checked every one-segment move: 3 can become %s.' % move_one('3')),
                 sa(DISPLAY + ' You may light at most 12 segments in total. What is the largest whole number you can show? '
                              '(Any number of digits; the first digit is not 0.)', 'Number:', str(best_number(12)),
                    'More digits beat bigger digits, and 1 is the cheapest digit (2 segments). Six 1s use 12 segments: '
                    '111111. Swapping a 1 for 7 costs one more segment, which is not available.',
                    compute=lambda: str(best_number(12)), fig=REF),
                 tf(DISPLAY + ' Every digit can be turned into some other digit by moving exactly one lit segment.', False,
                    '1, 4, 7 and 8 cannot: no single move turns them into another digit.',
                    check=lambda: all(move_one(d) for d in SEG), fig=REF),
                 mc(DISPLAY + ' A clock shows hours 1 to 12 and minutes 00 to 59 (for example 9:58 uses the digits 9, 5, 8). '
                              'Which time lights the most segments?', '10:08',
                    [('12:59', '12:59 lights 2 + 5 + 5 + 6 = 18'), ('9:58', '9:58 lights 6 + 5 + 7 = 18'),
                     ('11:11', '11:11 lights only 8')],
                    '10:08 lights 2 + 6 + 6 + 7 = 21. A search of every time confirms 21 is the most, and 10:08 is one '
                    'of the times that reach it.',
                    check=lambda t: clock_segs(t) == max(clock_segs('%d:%02d' % (h, m)) for h in range(1, 13)
                                                         for m in range(60)), fig=REF),
                 sa(DISPLAY + ' How many digits light more than 5 segments?', 'Digits:',
                    str(sum(1 for v in SEG.values() if len(v) > 5)), '0, 6, 9 light 6 and 8 lights 7: four digits.',
                    compute=lambda: str(sum(1 for v in SEG.values() if len(v) > 5)), fig=REF),
             ]))


def best_number(budget):
    best = 0
    for n in range(1, budget // 2 + 1):
        for ds in itertools.product('0123456789', repeat=n) if n <= 6 else ():
            if ds[0] != '0' and segs(ds) <= budget:
                best = max(best, int(''.join(ds)))
    return best


def clock_segs(t):
    return segs(t.replace(':', ''))


SETS = [s45(), s46(), s47(), s48()]
