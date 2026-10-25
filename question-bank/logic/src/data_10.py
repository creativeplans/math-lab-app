"""Logic sets 24-26: valid versus sound; moves and rearrangements; quantifiers over a stated domain."""
import itertools
from collections import deque
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt
import figs
from data_08 import valid, imp

TF = [True, False]


# ------------------------------------------------------------------ Set 24: valid versus sound
def s24():
    return S(24, 'Tell whether an argument is valid, and whether it is also sound',
             main=[
                 mc('"All mammals breathe air. Whales are mammals. So whales breathe air." How is this argument best '
                    'described?', 'valid and sound', [('valid but not sound', 'both premises are true'),
                                                      ('sound but not valid', 'a sound argument must be valid'),
                                                      ('invalid', 'the conclusion is forced by the premises')],
                    'The form is valid and both premises are true, so the argument is sound.'),
                 mc('"All birds can swim. A sparrow is a bird. So a sparrow can swim." How is this argument best described?',
                    'valid but not sound', [('valid and sound', '"All birds can swim" is false'),
                                            ('invalid', 'IF the premises were true, the conclusion would have to be true'),
                                            ('sound but not valid', 'sound arguments are always valid')],
                    'The form is valid; the first premise is false, so the argument is not sound.'),
                 tf('An argument can be sound even if its conclusion is false.', False,
                    'Sound means valid with true premises, and then the conclusion must be true.'),
                 mc('"If a number is divisible by 10, it is even. 14 is even. So 14 is divisible by 10." How is this '
                    'described?', 'invalid, so it cannot be sound', [('valid and sound', 'the form affirms the consequent'),
                                                                     ('valid but not sound', 'the form is not valid'),
                                                                     ('sound but not valid', 'impossible')],
                    'Affirming the consequent is invalid; an invalid argument is never sound.'),
                 mc('Which argument is SOUND?', '"Every prime greater than 2 is odd. 13 is a prime greater than 2. So 13 is odd."',
                    [('"Every prime is odd. 2 is prime. So 2 is odd."', 'the first premise is false (2 is even)'),
                     ('"If 13 is odd, 13 is prime. 13 is prime. So 13 is odd."', 'invalid form (affirming the consequent)'),
                     ('"Every odd number is prime. 9 is odd. So 9 is prime."', 'the first premise is false')],
                    'Only the first is valid with true premises.'),
             ],
             back=[
                 B('Is the form valid?', 'prerequisite', 'Soundness starts with validity; students must first judge the form.',
                   outcome='LOGIC.INFERENCE.01', qs=[
                       tf('"If P then Q. P. So Q." is a valid form.', True, 'Modus ponens.', check=lambda: valid(
                           [lambda p, q: imp(p, q), lambda p, q: p], lambda p, q: q)),
                       tf('"If P then Q. Q. So P." is a valid form.', False, 'Affirming the consequent.', check=lambda: valid(
                           [lambda p, q: imp(p, q), lambda p, q: q], lambda p, q: p)),
                       mc('A valid argument guarantees what?', 'If the premises are true, the conclusion is true.',
                          [('The premises are true.', 'validity says nothing about whether premises are true'),
                           ('The conclusion is true.', 'only if the premises are true'),
                           ('The argument is convincing.', 'persuasiveness is a different question')], 'Definition.'),
                       tf('"P or Q. P. So not Q." is a valid form.', False, 'With inclusive "or", P and Q can both be true, so the premises can be true while "not Q" is false.'),
                       tf('An argument with a true conclusion is always valid.', False, 'An invalid form can reach a true '
                                                                                        'conclusion by luck.'),
                   ]),
                 B('Are the premises true?', 'prerequisite', 'Soundness also needs true premises; students must check each '
                                                            'premise as a fact.', outcome='LOGIC.ARGUMENT.01', qs=[
                     tf('"Every rectangle has four equal sides" is true.', False, 'A 2 by 5 rectangle does not have four equal sides.'),
                     tf('"Every rectangle is a square" is true.', False, 'A 2 by 5 rectangle is not a square.'),
                     tf('"Every multiple of 2 is a multiple of 4" is true.', False, '6 is a multiple of 2 but not of 4.'),
                     tf('"Every prime number is odd" is true.', False, '2 is prime and even.'),
                     tf('"Water freezes at 10 degrees Celsius at normal air pressure" is true.', False, 'At normal air pressure water freezes at 0 degrees Celsius; at 10 degrees it is liquid.'),
                 ]),
             ],
             f1=FW('Classify harder arguments', 'Harder: mathematical premises and hidden false premises.', [
                 mc('"Every whole number that is divisible by 4 is divisible by 8. 12 is divisible by 4. So 12 is divisible by '
                    '8." How is it described?', 'valid but not sound', [('valid and sound', 'the first premise is false: 4 is '
                                                                                            'not divisible by 8'),
                                                                        ('invalid', 'the form is valid'),
                                                                        ('sound but not valid', 'impossible')],
                    'Valid form; false premise; and here the conclusion is also false.'),
                 tf('A valid argument with a false conclusion can have all of its premises true.', False,
                    'In a valid argument, true premises force a true conclusion. So a false conclusion means some premise is false.'),
                 mc('"No reptile has fur. A snake is a reptile. So a snake has no fur." How is it described?', 'valid and sound',
                    [('valid but not sound', 'both premises are true'), ('invalid', 'the conclusion follows'),
                     ('sound but not valid', 'impossible')], 'Valid form, true premises.'),
                 tf('If an argument is invalid, its conclusion must be false.', False, 'Its conclusion may be true by accident; '
                                                                                      'invalid only means it is not guaranteed.'),
                 mc('Which statement is TRUE?', 'Every sound argument is valid.',
                    [('Every valid argument is sound.', 'valid arguments can have false premises'),
                     ('Every argument with true premises is sound.', 'it must also be valid'),
                     ('Every argument with a true conclusion is sound.', 'it could be invalid')],
                    'Sound = valid + true premises.'),
             ]),
             f2=FW('Validity, soundness and truth together', 'Expert: which combinations of truth values are possible?', [
                 mc('Which combination is IMPOSSIBLE for an argument?', 'valid, all premises true, conclusion false',
                    [('valid, a false premise, conclusion true', 'possible: "All fish fly; robins are fish; so robins fly"'),
                     ('invalid, all premises true, conclusion true', 'possible: affirming the consequent with true parts'),
                     ('invalid, all premises true, conclusion false', 'possible: that is what invalid allows')],
                    'Validity rules out exactly this combination.'),
                 tf('An argument whose premises can never all be true at the same time (they contradict each other) is valid.',
                    True, 'There is no case with all premises true and the conclusion false, so it is valid (but never sound).'),
                 sa('Of the 8 combinations (valid or invalid; premises all true or not; conclusion true or false), how many '
                    'are impossible for an argument?', 'Impossible combinations:', '1',
                    'Only "valid, all premises true, conclusion false" is impossible; every other combination has an example '
                    '(for instance "valid, false premise, false conclusion": "All cats fly; Tom is a cat; so Tom flies").'),
                 mc('"If x = 3, then x squared = 9. x squared = 9. So x = 3." For real x, this argument is:',
                    'invalid: x = -3 makes the premises true and the conclusion false',
                    [('valid: squaring is unique', 'squaring is not one-to-one'),
                     ('sound: both premises can be true', 'soundness needs validity'),
                     ('valid but not sound', 'the form is not valid')], 'Affirming the consequent.'),
                 tf('Adding a false premise to a sound argument keeps it valid.', True,
                    'Adding premises never turns a valid argument invalid; it only stops it from being sound.'),
             ]))


# ------------------------------------------------------------------ Set 25: moves and rearrangements
def move_end(s, i):
    return s[:i] + s[i + 1:] + s[i]


def swap(s, i):
    l = list(s)
    l[i], l[i + 1] = l[i + 1], l[i]
    return ''.join(l)


def bfs(start, goal, moves):
    seen = {start: 0}
    q = deque([start])
    while q:
        x = q.popleft()
        if x == goal:
            return seen[x]
        for y in moves(x):
            if y not in seen:
                seen[y] = seen[x] + 1
                q.append(y)
    return None


ADJ = lambda s: [swap(s, i) for i in range(len(s) - 1)]
TOEND = lambda s: [move_end(s, i) for i in range(len(s))]
REV3 = lambda s: [s[:i] + s[i:i + 3][::-1] + s[i + 3:] for i in range(len(s) - 2)]
TILE = 'Tiles in a row each show a different letter.'


def s25():
    return S(25, 'Carry out stated moves on a row of tokens and find moves that reach a target',
             main=[
                 order(TILE + ' The row reads T, E, A, M. Move the leftmost tile to the far right end. Then swap the first two '
                              'tiles. What is the row now, from left to right?',
                       [('T', 'T'), ('E', 'E'), ('A', 'A'), ('M', 'M')], lambda p: ''.join(p) == swap(move_end('TEAM', 0), 0),
                       'Moving T to the end gives E, A, M, T. Swapping the first two gives A, E, M, T.',
                       expect=list('AEMT'), unique=True),
                 sa(TILE + ' One move swaps two tiles that are next to each other. What is the least number of moves that turn '
                           'D, C, B, A into A, B, C, D?', 'Moves:', '6',
                    'Each move fixes at most one pair that is in the wrong order. D, C, B, A has 6 such pairs (every pair), so '
                    'at least 6 moves are needed, and 6 moves suffice (bubble the letters into place).',
                    compute=lambda: str(bfs('DCBA', 'ABCD', ADJ))),
                 mc(TILE + ' Which single move turns R, O, P, E into O, P, E, R?', 'Move R from the left end to the right end.',
                    [('Swap R and O.', 'that gives O, R, P, E'), ('Swap the two middle tiles.', 'that gives R, P, O, E'),
                     ('Move E from the right end to the left end.', 'that gives E, R, O, P')],
                    'Taking R off the left and putting it on the right leaves O, P, E, R.',
                    check=lambda t: {'Move R from the left end to the right end.': move_end('ROPE', 0),
                                     'Swap R and O.': swap('ROPE', 0), 'Swap the two middle tiles.': swap('ROPE', 1),
                                     'Move E from the right end to the left end.': 'E' + 'ROP'}[t] == 'OPER'),
                 sa(TILE + ' One move swaps two tiles that are next to each other. What is the least number of moves that turn '
                           'C, A, B, E, D into A, B, C, D, E?', 'Moves:', '3',
                    'Pairs out of order: (C, A), (C, B), (E, D): 3. Each swap fixes one pair, so 3 moves are needed and '
                    'enough: swap C and A, swap C and B, swap E and D.', compute=lambda: str(bfs('CABED', 'ABCDE', ADJ))),
                 tf(TILE + ' Reversing the whole row twice puts every tile back where it started.', True,
                    'The second reversal undoes the first.', check=lambda: 'WORD'[::-1][::-1] == 'WORD'),
             ],
             back=[B('Strategy: number the positions', 'guided_strategy',
                     'Students lose track when tiles move. Writing position numbers under the row and updating them one move '
                     'at a time keeps every move exact.',
                     lesson=lesson('Number the positions',
                                   ['Write the row, and under it the position numbers 1, 2, 3, ... from the left.',
                                    'Do one move at a time and rewrite the whole row after each move.',
                                    'To find the fewest swaps of neighbors, count the pairs that are in the wrong order: each '
                                    'swap of neighbors fixes exactly one such pair.'],
                                   'Worked example (a different row)',
                                   ['Row: B, A, D, C. Fewest swaps of neighbors to reach A, B, C, D?'],
                                   ['Pairs in the wrong order: (B, A) and (D, C). That is 2.',
                                    'Swap B and A: A, B, D, C. Swap D and C: A, B, C, D. Two moves.']),
                     qs=[
                         order(TILE + ' Row: K, I, T. Swap the first two tiles. What is the row?', [('K', 'K'), ('I', 'I'), ('T', 'T')],
                               lambda p: ''.join(p) == 'IKT', 'K and I trade places.', expect=list('IKT'), unique=True),
                         order(TILE + ' Row: P, A, N. Move the leftmost tile to the far right. What is the row?',
                               [('P', 'P'), ('A', 'A'), ('N', 'N')], lambda p: ''.join(p) == move_end('PAN', 0),
                               'P goes to the end: A, N, P.', expect=list('ANP'), unique=True),
                         sa(TILE + ' How many pairs of tiles are in the wrong alphabetical order in C, B, A?', 'Pairs:', '3',
                            '(C, B), (C, A), (B, A).', compute=lambda: str(sum(1 for i in range(3) for j in range(i + 1, 3)
                                                                                if 'CBA'[i] > 'CBA'[j]))),
                         tf(TILE + ' Swapping two neighboring tiles twice returns the row to how it was.', True, 'The second swap '
                                                                                                                 'undoes the first.'),
                         sa(TILE + ' One move swaps neighboring tiles. Least number of moves from B, A, C to A, B, C?', 'Moves:',
                            '1', 'Swap B and A.', compute=lambda: str(bfs('BAC', 'ABC', ADJ))),
                     ])],
             f1=FW('Fewest moves under different rules', 'Harder: other kinds of moves and longer rows.', [
                 sa(TILE + ' One move takes ANY tile and puts it at the far right end. What is the least number of moves that '
                           'turn B, C, D, A into A, B, C, D?', 'Moves:', '3',
                    'A must end up first, so B, C and D must each be moved behind it: move B, then C, then D. Fewer is '
                    'impossible because each of B, C, D is in front of A and only a move can put it after A.',
                    compute=lambda: str(bfs('BCDA', 'ABCD', TOEND))),
                 sa(TILE + ' One move takes ANY tile and puts it at the far right end. What is the least number of moves that '
                           'turn A, C, D, B into A, B, C, D?', 'Moves:', '2',
                    'Move C, then D: A, D, B, C, then A, B, C, D.', compute=lambda: str(bfs('ACDB', 'ABCD', TOEND))),
                 order(TILE + ' Row: S, T, O, P. Move the tile in position 3 to the far left end, then swap the last two tiles. '
                              'What is the row?', [('S', 'S'), ('T', 'T'), ('O', 'O'), ('P', 'P')],
                       lambda p: ''.join(p) == swap('O' + 'STP', 2),
                       'Moving O to the front gives O, S, T, P; swapping the last two gives O, S, P, T.',
                       expect=list('OSPT'), unique=True),
                 sa(TILE + ' One move swaps neighboring tiles. What is the least number of moves that turn E, D, C, B, A into '
                           'A, B, C, D, E?', 'Moves:', '10', 'Every one of the 10 pairs is out of order.',
                    compute=lambda: str(bfs('EDCBA', 'ABCDE', ADJ))),
                 tf(TILE + ' If one move swaps neighboring tiles, any arrangement of 4 tiles can be reached from any other.',
                    True, 'Neighbor swaps can sort any row (as in bubble sort), and reversing the steps reaches any arrangement.',
                    check=lambda: all(bfs('ABCD', ''.join(p), ADJ) is not None for p in itertools.permutations('ABCD'))),
             ]),
             f2=FW('Moves that can never work', 'Expert: find what a move cannot change, and prove a target impossible.', [
                 mc(TILE + ' One move reverses any three tiles that are next to each other (for example A, B, C becomes C, B, '
                           'A). Starting from A, B, C, D, E, can you reach B, A, C, D, E?',
                    'No: each move keeps every tile in an odd or an even position, and A would need to move from position 1 to '
                    'position 2.',
                    [('Yes: reverse A, B, C, then reverse B, A, ... in a few moves.', 'no sequence works'),
                     ('Yes: any arrangement can be reached with enough moves.', 'only 12 of the 120 arrangements can be reached'),
                     ('No: because each move changes three tiles at once.', 'that alone does not rule it out')],
                    'Reversing three tiles swaps the 1st and 3rd of them and keeps the middle one: every tile moves by 0 or 2 '
                    'places, so it stays on odd or on even positions. A starts in position 1 (odd) and would need position 2.',
                    method='Automatic: all positions reachable by the move were searched.',
                    check=lambda t: t.startswith('No: each') and bfs('ABCDE', 'BACDE', REV3) is None),
                 sa(TILE + ' One move reverses any three neighboring tiles. Starting from A, B, C, D, E, how many different '
                           'arrangements can be reached (counting the start)?', 'Arrangements:', '12',
                    'Tiles in odd positions (A, C, E) can be put in any order among positions 1, 3, 5 (6 ways), and B, D in '
                    'positions 2, 4 (2 ways): 6 x 2 = 12.',
                    compute=lambda: str(sum(1 for p in itertools.permutations('ABCDE') if bfs('ABCDE', ''.join(p), REV3) is not None))),
                 values(TILE + ' One move swaps neighboring tiles. The row C, A, D, B, E must become A, B, C, D, E. Give the '
                               'least number of moves m.', [('m', 'm =')], 'm == 3', {'m': 3},
                        'Pairs out of order: (C, A), (C, B), (D, B): 3, so 3 moves are needed and enough.',
                        wrong=[{'m': 2}, {'m': 4}]),
                 tf(TILE + ' One move swaps ANY two tiles (not only neighbors). D, C, B, A can be turned into A, B, C, D in 2 '
                           'moves.', True, 'Swap D and A, then swap C and B.',
                    check=lambda: bfs('DCBA', 'ABCD', lambda s: [''.join(s[k] if k not in (i, j) else s[j if k == i else i]
                                                                         for k in range(4)) for i in range(4) for j in range(i + 1, 4)]) == 2),
                 sa(TILE + ' One move swaps ANY two tiles. What is the least number of moves that turn B, C, D, E, A into A, B, '
                           'C, D, E?', 'Moves:', '4', 'Each swap can put at most one tile into its final place unless it fixes '
                                                     'two at once, which needs two tiles in each other\'s places; here the five '
                                                     'tiles form one cycle, so 5 - 1 = 4 swaps are needed.',
                    compute=lambda: str(bfs('BCDEA', 'ABCDE', lambda s: [''.join(s[k] if k not in (i, j) else s[j if k == i else i]
                                                                                  for k in range(5)) for i in range(5) for j in range(i + 1, 5)]))),
             ]))


# ------------------------------------------------------------------ Set 26: quantifiers over a stated domain
CLUB = [('Ava', 15, 'chess', True), ('Ben', 16, 'robotics', False), ('Cy', 15, 'robotics', True),
        ('Dee', 17, 'chess', True), ('Eli', 16, 'art', False)]
CLUB_TEXT = ('The domain is exactly these five club members: Ava (age 15, chess, has a bus pass), Ben (16, robotics, no bus '
             'pass), Cy (15, robotics, bus pass), Dee (17, chess, bus pass), Eli (16, art, no bus pass).')


def club_fig():
    return figs.table(['Name', 'Age', 'Club', 'Bus pass'], [[n, str(a), c, 'yes' if b else 'no'] for n, a, c, b in CLUB])


def q(pred):
    return [m for m in CLUB if pred(m)]


def s26():
    fig = (club_fig().svg(), 'A table of five club members with their age, club and whether they have a bus pass.')
    return S(26, 'Decide the truth of "all", "some" and "no" statements over a stated domain',
             main=[
                 tf(CLUB_TEXT + ' "All chess members have a bus pass."', True, 'The chess members are Ava and Dee, and both '
                                                                             'have a bus pass.',
                    check=lambda: all(m[3] for m in CLUB if m[2] == 'chess'), fig=fig),
                 tf(CLUB_TEXT + ' "Some member aged 16 has a bus pass."', False, 'The members aged 16 are Ben and Eli; neither has '
                                                                              'a bus pass.',
                    check=lambda: any(m[3] for m in CLUB if m[1] == 16), fig=fig),
                 mc(CLUB_TEXT + ' Which statement is TRUE?', 'No art member has a bus pass.',
                    [('All robotics members have a bus pass.', 'Ben does not'), ('Some chess member is 16.', 'the chess '
                                                                                                           'members are 15 and 17'),
                     ('Every member is at least 16.', 'Ava and Cy are 15')],
                    'The only art member, Eli, has no bus pass.',
                    check=lambda t: {'No art member has a bus pass.': not any(m[3] for m in CLUB if m[2] == 'art'),
                                     'All robotics members have a bus pass.': all(m[3] for m in CLUB if m[2] == 'robotics'),
                                     'Some chess member is 16.': any(m[1] == 16 for m in CLUB if m[2] == 'chess'),
                                     'Every member is at least 16.': all(m[1] >= 16 for m in CLUB)}[t], fig=fig),
                 sa(CLUB_TEXT + ' How many members make "the member is 15 or has no bus pass" true?', 'Count:', '4',
                    'Aged 15: Ava, Cy. No bus pass: Ben, Eli. Together: 4 members (Dee is the only exception).',
                    compute=lambda: str(len(q(lambda m: m[1] == 15 or not m[3]))), fig=fig),
                 mc('The domain is the whole numbers 1 to 10. Which statement is FALSE?', 'Every number in the domain is less than '
                                                                                         '10.',
                    [('Some number in the domain is prime.', '2, 3, 5 and 7 are prime'),
                     ('No number in the domain is negative.', 'this is true: 1 to 10 are all positive'),
                     ('Some number in the domain is a multiple of 7.', 'this is true: 7 is in the domain')],
                    '10 is in the domain and is not less than 10.',
                    check=lambda t: not {'Every number in the domain is less than 10.': all(n < 10 for n in range(1, 11)),
                                         'Some number in the domain is prime.': any(n in (2, 3, 5, 7) for n in range(1, 11)),
                                         'No number in the domain is negative.': not any(n < 0 for n in range(1, 11)),
                                         'Some number in the domain is a multiple of 7.': any(n % 7 == 0 for n in range(1, 11))}[t]),
             ],
             back=[
                 B('Read "all", "some" and "no"', 'prerequisite', 'Each quantifier makes a different claim; students who read '
                                                                 '"some" as "all" (or "no" as "not all") misjudge truth.', qs=[
                     mc('"Some students walk to school" is true when ...', 'at least one student walks to school',
                        [('every student walks to school', 'that is "all"'), ('exactly one student walks', '"some" allows more'),
                         ('most students walk', '"some" does not mean most')], '"Some" means at least one.'),
                     mc('"No student walks to school" is true when ...', 'not even one student walks',
                        [('some students do not walk', 'that is "not all"'), ('most students ride', 'still allows walkers'),
                         ('exactly one student walks', 'one walker makes it false')], '"No" means zero.'),
                     tf('"All the lights are on" is true if exactly one light is off.', False, 'One light that is off is an exception, and one exception makes an "all" statement false.'),
                     tf('"Some numbers in {2, 4, 6} are odd" is true.', False, 'None of them is odd.',
                        check=lambda: any(n % 2 for n in (2, 4, 6))),
                     tf('"Every number in {3, 5, 7} is odd" is true.', True, 'All three are odd.',
                        check=lambda: all(n % 2 for n in (3, 5, 7))),
                 ]),
                 B('Stay inside the stated domain', 'prerequisite', 'A quantified statement is about the stated domain only. '
                                                                   'Students who think of numbers or people outside it get the '
                                                                   'wrong truth value.', qs=[
                     tf('The domain is {1, 2, 3}. "Every number in the domain is less than 4" is true.', True,
                        'Only 1, 2, 3 count.', check=lambda: all(n < 4 for n in (1, 2, 3))),
                     tf('The domain is {10, 20, 30}. "Some number in the domain is odd" is true.', False, 'All three are even.'),
                     mc('The domain is the days Monday to Friday. Which is true?', 'No day in the domain is a weekend day.',
                        [('Some day in the domain is Sunday.', 'Sunday is not in the domain'),
                         ('Every day in the domain starts with M.', 'only Monday'),
                         ('Some day in the domain is Saturday.', 'not in the domain')],
                        'Saturday and Sunday are outside the domain.'),
                     tf('"All prime numbers are odd" is true when the domain is {3, 5, 7, 11}.', True, 'Within this domain, every '
                                                                                                       'prime is odd.'),
                     tf('"All prime numbers are odd" is true when the domain is all whole numbers.', False, '2 is prime and even.'),
                 ]),
             ],
             f1=FW('Quantifiers with two conditions', 'Harder: statements that combine conditions and count.', [
                 tf(CLUB_TEXT + ' "Every member without a bus pass is 16."', True, 'Ben and Eli have no bus pass; both are 16.',
                    check=lambda: all(m[1] == 16 for m in CLUB if not m[3]), fig=fig),
                 tf(CLUB_TEXT + ' "Some member with a bus pass is older than every robotics member."', True,
                    'Dee (17) has a bus pass and is older than Ben (16) and Cy (15).',
                    check=lambda: any(all(m[1] > r[1] for r in CLUB if r[2] == 'robotics') for m in CLUB if m[3]), fig=fig),
                 sa('The domain is the whole numbers 1 to 20. How many numbers make "the number is even and not a multiple of '
                    '3" true?', 'Count:', '7', 'Even: 10 numbers. Even multiples of 3 (6, 12, 18): 3. So 7.',
                    compute=lambda: str(sum(1 for n in range(1, 21) if n % 2 == 0 and n % 3 != 0))),
                 mc(CLUB_TEXT + ' Which statement is FALSE?', 'No member aged 15 is in robotics.',
                    [('Every chess member is 15 or 17.', 'true: Ava 15, Dee 17'), ('Some member has no bus pass.', 'Ben, Eli'),
                     ('All members aged 17 play chess.', 'Dee is the only 17-year-old')],
                    'Cy is 15 and in robotics.', fig=fig,
                    check=lambda t: not {'No member aged 15 is in robotics.': not any(m[2] == 'robotics' for m in CLUB if m[1] == 15),
                                         'Every chess member is 15 or 17.': all(m[1] in (15, 17) for m in CLUB if m[2] == 'chess'),
                                         'Some member has no bus pass.': any(not m[3] for m in CLUB),
                                         'All members aged 17 play chess.': all(m[2] == 'chess' for m in CLUB if m[1] == 17)}[t]),
                 tf('The domain is empty (it has no members). "Every member of the domain is green" is true.', True,
                    'There is no member to break the claim, so an "every" statement about an empty domain is true '
                    '("vacuously" true).'),
             ]),
             f2=FW('Nested quantifiers', 'Expert: "for every ... there is ..." and the order of quantifiers.', [
                 tf('The domain is the whole numbers 1 to 5. "For every number x, there is a number y with y > x" is true.',
                    False, 'For x = 5 there is no larger number in the domain.',
                    check=lambda: all(any(y > x for y in range(1, 6)) for x in range(1, 6))),
                 tf('The domain is the whole numbers 1 to 5. "There is a number y such that for every number x, y ≥ x" is true.',
                    True, 'y = 5 works for every x.', check=lambda: any(all(y >= x for x in range(1, 6)) for y in range(1, 6))),
                 mc('The domain is all whole numbers. Which statement is TRUE?', 'For every x, there is a y with y > x.',
                    [('There is a y such that for every x, y > x.', 'no whole number is larger than every whole number '
                                                                      '(including itself)'),
                     ('For every x and every y, y > x.', 'false for x = 3, y = 2'),
                     ('There is an x such that for every y, y > x.', 'x would have to be less than itself')],
                    'Given any x, y = x + 1 works. The order of "for every" and "there is" matters.'),
                 sa(CLUB_TEXT + ' For how many members x is the statement "some other member is the same age as x" true?',
                    'Count:', '4', 'Ava and Cy share 15; Ben and Eli share 16; Dee (17) has no partner.',
                    compute=lambda: str(sum(1 for m in CLUB if any(o[1] == m[1] for o in CLUB if o is not m))), fig=fig),
                 values('The domain is the whole numbers 1 to 9. Give a number x that makes "for every y in the domain, x + y > '
                        '5" true.', [('x', 'x =')], 'x >= 5 and x <= 9 and isInteger(x)', {'x': 6},
                        'The smallest y is 1, so x + 1 > 5, x > 4: any x from 5 to 9.',
                        wrong=[{'x': 4}, {'x': 10}, {'x': 2}], search={'x': range(1, 10)}),
             ]))


SETS = [s24(), s25(), s26()]
