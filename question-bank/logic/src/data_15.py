"""Logic sets 41-44: parity and alternation; counterexamples; proofs about lines and angles; invariants."""
import itertools
import math
from collections import deque
from lq import S, B, FW, mc, tf, sa, order, values, lesson
import figs


def isprime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


# ------------------------------------------------------------------ Set 41: parity and alternation
GEAR = ('Gears that touch mesh: when one turns clockwise, a gear touching it turns counterclockwise, and the reverse.')


def ring_fig(n):
    nodes = {str(i + 1): (130 + 95 * math.sin(2 * math.pi * i / n), 120 - 95 * math.cos(2 * math.pi * i / n))
             for i in range(n)}
    edges = [(str(i + 1), str((i + 1) % n + 1)) for i in range(n)]
    return (figs.network(nodes, edges, size=(260, 240), node_r=17).svg(),
            'A closed ring of %d numbered gears, each touching the gears on either side.' % n)


def ring_turns(n):
    """Two-color the ring; True when the gears can turn (no gear forced both ways)."""
    return n % 2 == 0


def grid_adj(n, m):
    return {(r, c): [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                     if 0 <= r + dr < n and 0 <= c + dc < m] for r in range(n) for c in range(m)}


def reach_exact(adj, start, k):
    cur = {start}
    for _ in range(k):
        cur = {y for x in cur for y in adj[x]}
    return cur


def sign_totals(n):
    tot = {0}
    for k in range(1, n + 1):
        tot = {t + k for t in tot} | {t - k for t in tot}
    return tot


def ham_path_from(adj, start):
    """True when some path from start visits every vertex exactly once (depth-first search with pruning)."""
    N = len(adj)

    def go(v, seen):
        if len(seen) == N:
            return True
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                if go(w, seen):
                    return True
                seen.remove(w)
        return False
    return go(start, {start})


CUBE = {v: [v ^ (1 << i) for i in range(3)] for v in range(8)}


def s41():
    return S(41, 'Use odd/even and alternation to predict outcomes and rule out possibilities',
             main=[
                 mc(GEAR + ' Seven gears form a closed ring, each touching the gears on either side (figure). Gear 1 is '
                           'turned clockwise. What happens?',
                    'The gears jam: going around the ring, gear 1 would have to turn both ways.',
                    [('Every gear turns, and the directions alternate around the ring.',
                      'alternating around 7 gears ends with gear 7 clockwise, touching gear 1, which is also clockwise'),
                     ('Every gear turns clockwise.', 'touching gears must turn opposite ways'),
                     ('Only gears 1, 3, 5 and 7 turn.', 'gears that touch a turning gear are forced to turn')],
                    'Going around: 1 clockwise, 2 counter, 3 clockwise, ..., 7 clockwise. Gear 7 touches gear 1, so they '
                    'must turn opposite ways, but both are clockwise. An odd ring cannot turn.', fig=ring_fig(7),
                    check=lambda t: t.startswith('The gears jam') != ring_turns(7)),
                 sa(GEAR + ' Twelve gears stand in a row (not a ring), each touching the next. Gear 1 turns clockwise. How '
                           'many of the 12 gears turn counterclockwise?', 'Gears:', '6',
                    'Odd-numbered gears turn clockwise and even-numbered gears counterclockwise: 2, 4, ..., 12 is 6 gears.',
                    compute=lambda: str(sum(1 for g in range(1, 13) if g % 2 == 0))),
                 tf('A frog starts on 0 on a number line and makes exactly 9 jumps, each 1 unit left or right. It can end '
                    'on 4.', False,
                    'Each jump changes the position by 1, so it switches between even and odd. After 9 jumps (odd) the frog '
                    'is on an odd number, and 4 is even.',
                    check=lambda: 4 in {sum(s) for s in itertools.product((1, -1), repeat=9)}),
                 values('A lamp starts OFF. Each press of its switch changes it (OFF to ON, or ON to OFF). Give a number of '
                        'presses from 1 to 20 that leaves the lamp ON.', [('n', 'Presses =')],
                        'isInteger(n) and n >= 1 and n <= 20 and isOdd(n)', {'n': 7},
                        'After an odd number of presses the lamp is ON; after an even number it is OFF.',
                        wrong=[{'n': 8}, {'n': 20}, {'n': 0}], search={'n': range(0, 21)}),
                 sa('A token moves along a row of squares numbered 1 to 15. Each move jumps exactly 2 squares left or '
                    'right (staying on the row). It starts on square 4. How many of the 15 squares can it ever reach, '
                    'counting square 4?', 'Squares:',
                    str(len({4 + 2 * k for k in range(-10, 10) if 1 <= 4 + 2 * k <= 15})),
                    'Jumps of 2 keep the token on even squares: 2, 4, 6, 8, 10, 12, 14. That is 7 squares, and all of them '
                    'can be reached.', compute=lambda: str(len({4 + 2 * k for k in range(-10, 10) if 1 <= 4 + 2 * k <= 15}))),
             ],
             back=[B('Strategy: keep track of odd and even only', 'guided_strategy',
                     'Students follow every step of a long process. Often only odd/even matters, and it switches or stays '
                     'the same at each step.',
                     lesson=lesson('Keep track of odd and even only',
                                   ['Ask what happens to odd/even at each step. Does it switch every time, or stay the '
                                    'same?',
                                    'If it switches every step, after an even number of steps it is back where it began; '
                                    'after an odd number it is the other way.',
                                    'A target with the wrong parity can never be reached, however the steps are chosen.'],
                                   'Worked example (a different puzzle)',
                                   ['A card shows its red side. Each turn it is flipped over. After 25 turns, which side '
                                    'shows?'],
                                   ['Each flip switches the side. After an even number of flips it shows red again.',
                                    '25 is odd, so after 25 flips the other side shows.']),
                     qs=[
                         tf('The sum of 5 odd numbers is odd.', True,
                            'Pairs of odd numbers add to even numbers; 5 odd numbers make 2 pairs and 1 left over, so the '
                            'sum is even + odd = odd.', check=lambda: (1 + 3 + 5 + 7 + 9) % 2 == 1),
                         mc('A coin starts heads up. It is turned over 13 times. Which side is up at the end?', 'Tails',
                            [('Heads', 'heads is up only after an even number of turns'),
                             ('Either side, depending on how it is turned', 'every turn switches the side, so the result is '
                                                                           'fixed'),
                             ('It cannot be known without trying', 'the parity of 13 decides it')],
                            '13 is odd, so the side switches an odd number of times: tails.'),
                         sa(GEAR + ' Nine gears stand in a row, each touching the next. Gear 1 turns clockwise. What is the '
                                   'number of the last gear in the row that turns clockwise?', 'Gear:', '9',
                            'Odd-numbered gears turn clockwise, and 9 is odd.',
                            compute=lambda: str(max(g for g in range(1, 10) if g % 2 == 1))),
                         tf('An even number plus an odd number is even.', False, '2 + 3 = 5. Even + odd is always odd.'),
                         mc('Which total CANNOT be the sum of three odd numbers?', '10',
                            [('9', '3 + 3 + 3 = 9'), ('15', '5 + 5 + 5 = 15'), ('3', '1 + 1 + 1 = 3')],
                            'odd + odd + odd = even + odd = odd, so the total is always odd.',
                            check=lambda t: int(t) % 2 == 0),
                     ])],
             f1=FW('Parity on boards and rings', 'Harder: parity on grids, rings and sign choices.', [
                 sa('A token starts on a corner square of a 5 by 5 board. Each move goes to a square sharing a side '
                    '(going back is allowed). After exactly 7 moves, how many different squares could the token be on?',
                    'Squares:', str(len(reach_exact(grid_adj(5, 5), (0, 0), 7))),
                    'Color the board like a checkerboard. Each move changes color, so after 7 moves the token is on the '
                    'other color from the corner: the 12 such squares. All 12 are within 7 moves.',
                    compute=lambda: str(len(reach_exact(grid_adj(5, 5), (0, 0), 7)))),
                 tf(GEAR + ' Ten gears form a closed ring, each touching the gears on either side. They can all turn.',
                    True, 'Alternating around 10 gears ends with gear 10 counterclockwise, opposite to gear 1, which it '
                          'touches. No conflict.', check=lambda: ring_turns(10)),
                 mc('Seven cups stand upside down. A move turns over exactly 4 cups (any 4). Can all seven cups end '
                    'right side up?', 'No: each move changes the number of upside-down cups by an even amount, so it '
                                      'stays odd.',
                    [('Yes: turn over 4 cups, then 3 cups.', 'a move must turn exactly 4 cups'),
                     ('Yes, after exactly 7 moves.', 'no number of moves works'),
                     ('No: 7 is not a multiple of 4.', 'the true reason is parity; for example 6 cups could all be '
                                                      'turned right side up')],
                    'Turning 4 cups changes the upside-down count by -4, -2, 0, 2 or 4. Starting from 7 (odd), it stays '
                    'odd and can never be 0.',
                    check=lambda t: t.startswith('No: each') and not any(
                        0 in s for s in [reach_count(7, 7, 4)])),
                 values('Put a + or - sign in front of each of the numbers 1, 2, 3, ..., 10 and add. Give a total from 0 to '
                        '10 that can be made this way.', [('t', 'Total =')],
                        'isInteger(t) and t >= 0 and t <= 10 and isOdd(t)', {'t': 1},
                        '1 + 2 + ... + 10 = 55 is odd. Changing a + to a - lowers the total by an even amount, so every total '
                        'is odd. Each odd total from 1 to 9 can be made.', wrong=[{'t': 0}, {'t': 4}, {'t': 10}],
                        method='Checked: the totals from 0 to 10 that can be made are %s.'
                        % sorted(t for t in sign_totals(10) if 0 <= t <= 10)),
                 sa(GEAR + ' Nine gears are arranged in a 3 by 3 square, and each gear touches the gears directly beside, '
                           'above and below it. A corner gear turns clockwise. How many gears turn clockwise, including '
                           'the corner gear?', 'Gears:',
                    str(sum(1 for r, c in grid_adj(3, 3) if (r + c) % 2 == 0)),
                    'Color like a checkerboard: the corners and center share the corner\'s color (5 gears) and turn '
                    'clockwise; the other 4 turn counterclockwise.',
                    compute=lambda: str(sum(1 for r, c in grid_adj(3, 3) if (r + c) % 2 == 0))),
             ]),
             f2=FW('Prove impossibility with parity', 'Expert: parity arguments about paths and totals.', [
                 mc('A token must visit every square of a 5 by 5 board exactly once, each move going to a square that shares '
                    'a side. It starts on the square next to a corner (row 1, column 2). Is this possible?',
                    'No: the path must start and end on the corner color, and this square has the other color.',
                    [('Yes: go along row 1, then snake back and forth.', 'that path misses the corner square or repeats one'),
                     ('Yes, but only if it ends on a corner.', 'no such path exists from this square at all'),
                     ('No: 25 is not a multiple of 5.', '25 = 5 x 5; the count is not the problem')],
                    'With checkerboard colors there are 13 corner-colored and 12 other squares. A path alternates colors, '
                    'so a 25-square path must have 13 of one color at positions 1, 3, ..., 25: it starts on the corner '
                    'color. A full search confirms no path starts at row 1, column 2.',
                    check=lambda t: t.startswith('No: the path') and not ham_path_from(grid_adj(5, 5), (0, 1))),
                 sa('Put a + or - sign in front of each of the numbers 1, 2, 3, ..., 10 and add. How many different totals '
                    'can be made?', 'Totals:', str(len(sign_totals(10))),
                    'Totals are odd, from -55 to 55. Every odd number in that range can be made: 56 totals.',
                    compute=lambda: str(len(sign_totals(10)))),
                 tf('On a square grid, a path that moves one square up, down, left or right at each step, and ends where it '
                    'started, always has an even number of steps.', True,
                    'Each step changes the checkerboard color. To return to the starting color, the number of changes must '
                    'be even.'),
                 values(GEAR + ' Give a number of gears n from 3 to 12 for which a closed ring of n gears, each touching '
                               'its two neighbors, would jam.', [('n', 'n =')],
                        'isInteger(n) and n >= 3 and n <= 12 and isOdd(n)', {'n': 5},
                        'A ring jams exactly when the number of gears is odd: 3, 5, 7, 9 or 11.',
                        wrong=[{'n': 4}, {'n': 12}, {'n': 13}], search={'n': range(1, 15)}),
                 sa('A bug walks along the edges of a cube from corner to corner. It starts at one corner and makes exactly '
                    '5 moves (going back is allowed). How many of the 8 corners could it end on?', 'Corners:',
                    str(len(reach_exact(CUBE, 0, 5))),
                    'Color the corners in two colors so every edge joins different colors (4 and 4). After an odd number '
                    'of moves the bug is on the other color: 4 corners, and each can be reached.',
                    compute=lambda: str(len(reach_exact(CUBE, 0, 5)))),
             ]))


def reach_count(total, start_down, flip):
    """Possible numbers of upside-down cups (out of total) reachable when each move turns over exactly `flip` cups."""
    seen = {start_down}
    q = deque([start_down])
    while q:
        d = q.popleft()
        for k in range(0, flip + 1):  # k of the flipped cups were upside down
            if k <= d and flip - k <= total - d:
                e = d - k + (flip - k)
                if e not in seen:
                    seen.add(e)
                    q.append(e)
    return seen


# ------------------------------------------------------------------ Set 42: disprove a claim with a counterexample
CE = 'A counterexample to a claim about every case is one case where the claim is false.'


def s42():
    return S(42, 'Find a counterexample that disproves a general mathematical claim',
             main=[
                 mc(CE + ' Claim: for every whole number n, n squared + n + 11 is prime. Which n is a counterexample?', '10',
                    [('1', '1 + 1 + 11 = 13, which is prime'), ('2', '4 + 2 + 11 = 17, which is prime'),
                     ('3', '9 + 3 + 11 = 23, which is prime')],
                    '100 + 10 + 11 = 121 = 11 x 11, which is not prime.', check=lambda t: not isprime(int(t) ** 2 + int(t) + 11)),
                 values(CE + ' Claim: for all numbers a and b, if a > b, then a squared > b squared. Give a counterexample.',
                        [('a', 'a ='), ('b', 'b =')], 'a > b and a^2 <= b^2', {'a': 1, 'b': -2},
                        'For example a = 1, b = -2: 1 > -2, but 1 is not greater than 4. A negative b works.',
                        wrong=[{'a': 3, 'b': 2}, {'a': 2, 'b': 3}, {'a': 5, 'b': 0}]),
                 tf(CE + ' The claim "every odd number greater than 1 is prime" is disproved by the number 9.', True,
                    '9 is odd and greater than 1, but 9 = 3 x 3.', check=lambda: not isprime(9)),
                 sa(CE + ' Claim: 2 to the power n, plus 1, is prime for every whole number n from 1 to 6. What is the '
                         'smallest n that disproves it?', 'n =', '3',
                    'n = 1: 3, prime. n = 2: 5, prime. n = 3: 9 = 3 x 3, not prime.',
                    compute=lambda: str(min(n for n in range(1, 7) if not isprime(2 ** n + 1)))),
                 mc(CE + ' Claim: every multiple of 4 is a multiple of 8. Which number is NOT a counterexample?', '16',
                    [('4', '4 is a multiple of 4 but not of 8, so it is a counterexample'),
                     ('12', '12 is a multiple of 4 but not of 8, so it is a counterexample'),
                     ('20', '20 is a multiple of 4 but not of 8, so it is a counterexample')],
                    '16 is a multiple of 8, so the claim holds for 16.', check=lambda t: int(t) % 8 == 0),
             ],
             back=[B('What a counterexample is', 'prerequisite',
                     'Students cannot hunt for a counterexample until they know that one failing case disproves a '
                     '"for every" claim, and that examples that work prove nothing.',
                     qs=[
                         mc('What is a counterexample to the claim "every number with property P has property Q"?',
                            'A number with property P that does not have property Q',
                            [('A number with property Q that does not have property P', 'that does not test the claim'),
                             ('A number with neither property', 'the claim says nothing about numbers without P'),
                             ('A number with both properties', 'that agrees with the claim')],
                            'The claim fails exactly when P holds and Q does not.'),
                         tf('One counterexample is enough to show that a claim about every case is false.', True,
                            'The claim said every case works; one failing case shows it does not.'),
                         tf('If a claim works for five examples, it is proved true for every case.', False,
                            'A later case could still fail.'),
                         mc(CE + ' Which number is a counterexample to "all prime numbers are odd"?', '2',
                            [('9', '9 is odd and not prime, so it does not test the claim'),
                             ('3', '3 is prime and odd, so it agrees with the claim'),
                             ('4', '4 is not prime')], '2 is prime and even.', check=lambda t: isprime(int(t)) and int(t) % 2 == 0),
                         values(CE + ' Claim: every whole number divisible by 3 is divisible by 6. Give a counterexample '
                                     'from 1 to 30.', [('n', 'n =')],
                                'isInteger(n) and n >= 1 and n <= 30 and mod(n, 3) == 0 and mod(n, 6) != 0', {'n': 9},
                                'Any odd multiple of 3 works: 3, 9, 15, 21, 27.', wrong=[{'n': 6}, {'n': 10}, {'n': 12}],
                                search={'n': range(1, 31)}),
                     ])],
             f1=FW('Counterexamples to algebra rules', 'Harder: counterexamples to tempting rules.', [
                 values(CE + ' Claim: (a + b) squared = a squared + b squared for all numbers a and b. Give whole numbers a '
                             'and b that disprove it.', [('a', 'a ='), ('b', 'b =')], 'a != 0 and b != 0', {'a': 1, 'b': 1},
                        '(a + b) squared - (a squared + b squared) = 2ab, so the claim fails exactly when a and b are both '
                        'nonzero. For example a = 1, b = 1: 4 is not 2.',
                        wrong=[{'a': 0, 'b': 5}, {'a': 3, 'b': 0}]),
                 mc(CE + ' Claim: the square root of (a + b) equals the square root of a plus the square root of b, for all '
                         'numbers a and b that are 0 or more. Which pair is a counterexample?', 'a = 9, b = 16',
                    [('a = 0, b = 4', 'square root of 4 = 0 + 2, so the claim holds here'),
                     ('a = 0, b = 0', '0 = 0 + 0, so the claim holds here'),
                     ('a = 1, b = 0', '1 = 1 + 0, so the claim holds here')],
                    'Square root of 25 is 5, but 3 + 4 = 7.',
                    check=lambda t: (lambda a, b: math.sqrt(a + b) != math.sqrt(a) + math.sqrt(b))(
                        *[int(x.split('=')[1]) for x in t.split(',')])),
                 sa(CE + ' Claim: n factorial plus 1 is prime for every positive whole number n. (n factorial is '
                         '1 x 2 x ... x n.) What is the smallest n that disproves it?', 'n =',
                    str(min(n for n in range(1, 10) if not isprime(math.factorial(n) + 1))),
                    '1! + 1 = 2, 2! + 1 = 3, 3! + 1 = 7 are prime; 4! + 1 = 25 = 5 x 5 is not.',
                    compute=lambda: str(min(n for n in range(1, 10) if not isprime(math.factorial(n) + 1)))),
                 tf(CE + ' The claim "if n squared is a multiple of 4, then n is a multiple of 4" is disproved by n = 2.',
                    True, '2 squared = 4 is a multiple of 4, but 2 is not.', check=lambda: (2 * 2) % 4 == 0 and 2 % 4 != 0),
                 mc(CE + ' Claim: every rectangle with perimeter 20 has area 25. Which rectangle is a counterexample?',
                    '4 by 6', [('5 by 5', 'perimeter 20 and area 25, so it agrees with the claim'),
                               ('2 by 10', 'its perimeter is 24, so the claim says nothing about it'),
                               ('3 by 8', 'its perimeter is 22, so the claim says nothing about it')],
                    'A 4 by 6 rectangle has perimeter 20 but area 24.',
                    check=lambda t: (lambda w, h: 2 * (w + h) == 20 and w * h != 25)(*[int(x) for x in t.split(' by ')])),
             ]),
             f2=FW('Counterexamples that take a search', 'Expert: claims that hold for many cases before failing.', [
                 values(CE + ' Claim: for whole numbers a, b and c, if a divides b x c, then a divides b or a divides c. Give a '
                             'counterexample with a, b and c each from 2 to 12.', [('a', 'a ='), ('b', 'b ='), ('c', 'c =')],
                        'isInteger(a) and isInteger(b) and isInteger(c) and a >= 2 and a <= 12 and b >= 2 and b <= 12 and '
                        'c >= 2 and c <= 12 and mod(b * c, a) == 0 and mod(b, a) != 0 and mod(c, a) != 0',
                        {'a': 4, 'b': 2, 'c': 6},
                        'For example a = 4, b = 2, c = 6: 4 divides 12, but 4 divides neither 2 nor 6. (The claim is true when '
                        'a is prime.)', wrong=[{'a': 3, 'b': 3, 'c': 5}, {'a': 5, 'b': 2, 'c': 3}],
                        search={'a': range(2, 13), 'b': range(2, 13), 'c': range(2, 13)}),
                 tf(CE + ' Claim: 2 to the power n, minus 1, is prime whenever n is prime. The smallest counterexample is '
                         'n = 11.', True,
                    'n = 2, 3, 5, 7 give 3, 7, 31, 127, all prime. n = 11 gives 2047 = 23 x 89.',
                    check=lambda: min(n for n in range(2, 30) if isprime(n) and not isprime(2 ** n - 1)) == 11),
                 mc('Which claim is FALSE?', 'If n is prime, then n + 2 is prime.',
                    [('If n is odd, then n squared is odd.', 'true: (2k + 1) squared = 2(2k squared + 2k) + 1'),
                     ('The sum of two even numbers is even.', 'true: 2a + 2b = 2(a + b)'),
                     ('If n squared is odd, then n is odd.', 'true: if n were even, n squared would be even')],
                    'Counterexample: 7 is prime, but 9 is not.'),
                 sa(CE + ' Claim: every whole number from 1 to 30 is a sum of two square numbers (0, 1, 4, 9, 16, 25, ...; a '
                         'square may be used twice). What is the smallest counterexample?', 'Number:',
                    str(min(n for n in range(1, 31) if not any(a * a + b * b == n for a in range(6) for b in range(6)))),
                    '1 = 1 + 0, 2 = 1 + 1, but 3 cannot be made: the squares up to 3 are 0 and 1.',
                    compute=lambda: str(min(n for n in range(1, 31)
                                            if not any(a * a + b * b == n for a in range(6) for b in range(6))))),
                 mc(CE + ' Claim: for every positive whole number n, 2 to the power n is greater than n. Why is n = -1 NOT a '
                         'valid counterexample?', 'The claim is only about positive whole numbers, and -1 is not one.',
                    [('Because 2 to the power -1 is undefined.', '2 to the power -1 is defined: it equals 1/2'),
                     ('Because a counterexample must be a large number.', 'any case covered by the claim may serve'),
                     ('Because counterexamples cannot be negative.', 'they can be, when the claim covers negative numbers')],
                    'A counterexample must be a case the claim is about. (Also, 2 to the power -1 = 1/2 is greater than -1, so -1 '
                    'would not break the inequality anyway; the assessed reason is the domain.)'),
             ]))


# ------------------------------------------------------------------ Set 43: proofs about lines and angles
LINES = ('In the figure, lines p and q are cut by the transversal t. Angles 1 to 4 are at line p and angles 5 to 8 at line '
         'q, in the same positions: 1 upper left, 2 upper right, 3 lower left, 4 lower right (and 5, 6, 7, 8 likewise).')
SAME = {1: 'X', 4: 'X', 5: 'X', 8: 'X', 2: 'Y', 3: 'Y', 6: 'Y', 7: 'Y'}  # equal groups when p and q are parallel


def angle_fig(parallel=True):
    c = figs.Canvas(340, 240)
    for y, name in ((70, 'p'), (170, 'q')):
        c.line(20, y, 300, y, sw=2)
        c.text(318, y + 5, name, size=15, weight='bold')
    x1, y1, x2, y2 = 110, 10, 250, 230
    c.line(x1, y1, x2, y2, sw=2)
    c.text(258, 228, 't', size=15, weight='bold')

    def xat(y):
        return x1 + (x2 - x1) * (y - y1) / (y2 - y1)
    for y, base in ((70, 1), (170, 5)):
        x = xat(y)
        for k, (dx, dy) in enumerate(((-22, -10), (26, -10), (-26, 22), (22, 22))):
            c.text(x + dx, y + dy, str(base + k), size=14, weight='bold')
    if parallel:
        c.text(60, 230, 'p is parallel to q', size=13)
    return (c.svg(), 'Two horizontal lines p (top) and q (bottom) cut by a slanted transversal t. At each crossing the four '
                     'angles are numbered: at p, 1 upper left, 2 upper right, 3 lower left, 4 lower right; at q, 5, 6, 7, '
                     '8 in the same positions.' + (' A note says p is parallel to q.' if parallel else ''))


def s43():
    F = angle_fig()
    G = angle_fig(parallel=False)
    return S(43, 'Order and justify the steps of proofs about angles formed by intersecting and parallel lines',
             main=[
                 order('Lines meet at a point, forming angle 1 and angle 2 as vertical angles, and angle 3 next to both '
                       '(angle 3 forms a linear pair with angle 1 and with angle 2). Put the steps of the proof that angle 1 '
                       '= angle 2 in a correct order. (Two orders are correct.)',
                       [('A', 'angle 1 + angle 3 = 180 degrees (linear pair)'),
                        ('B', 'angle 2 + angle 3 = 180 degrees (linear pair)'),
                        ('C', 'angle 1 + angle 3 = angle 2 + angle 3 (both sums equal 180 degrees)'),
                        ('D', 'angle 1 = angle 2 (subtract angle 3 from both sides)')],
                       lambda p: p[-1] == 'D' and p[-2] == 'C',
                       'Both linear pairs come first (in either order), then substitution, then subtraction.',
                       expect=list('ABCD')),
                 mc(LINES + ' Which pair of angles are alternate interior angles?', 'Angles 4 and 5',
                    [('Angles 1 and 5', 'they are corresponding angles: same position at each line'),
                     ('Angles 2 and 3', 'they are vertical angles at line p'),
                     ('Angles 4 and 8', 'they are corresponding angles: same position at each line')],
                    'Angles 4 and 5 lie between p and q, on opposite sides of t.', fig=F),
                 tf(LINES + ' Lines p and q are parallel. If angle 2 = 70 degrees, then angle 7 = 70 degrees.', True,
                    'Angle 2 = angle 3 (vertical), angle 3 = angle 6 (alternate interior, p parallel to q), and angle 6 = '
                    'angle 7 (vertical). So angle 7 = 70 degrees.', fig=F, check=lambda: SAME[2] == SAME[7]),
                 values(LINES + ' Lines p and q are parallel, and angle 1 = 115 degrees. Give the measure of angle 6 in '
                                'degrees.', [('x', 'angle 6 =')], 'x == 65', {'x': 65},
                        'Angle 1 = angle 5 (corresponding), and angle 5 + angle 6 = 180 degrees (linear pair), so angle 6 = '
                        '65 degrees.', wrong=[{'x': 115}, {'x': 75}, {'x': 245}], fig=F),
                 order(LINES + ' Put the steps of the proof that angle 3 = angle 6 when p is parallel to q in a correct '
                               'order. Each step may use only lines placed before it. (More than one order is correct.)',
                       [('A', 'p is parallel to q, cut by transversal t (given)'),
                        ('B', 'angle 2 = angle 6 (corresponding angles, p parallel to q)'),
                        ('C', 'angle 2 = angle 3 (vertical angles)'),
                        ('D', 'angle 3 = angle 6 (both equal angle 2)')],
                       lambda p: p[-1] == 'D' and p.index('A') < p.index('B'),
                       'B uses the given A (parallel lines), so A comes before B. The vertical-angles step C needs no given, '
                       'so it can come anywhere before the conclusion D. Three orders are accepted.', expect=list('ABCD'), fig=F),
             ],
             back=[B('Name the angle pairs', 'prerequisite',
                     'A proof step cites an angle relationship by name. Students who cannot identify linear pairs, vertical '
                     'angles and corresponding angles cannot justify the steps.',
                     qs=[
                         sa('Two angles form a linear pair (together they make a straight line). One measures 48 degrees. '
                            'What does the other measure, in degrees?', 'Degrees:', '132', '180 - 48 = 132.',
                            compute=lambda: str(180 - 48)),
                         tf(LINES + ' Angles 1 and 4 are vertical angles.', True,
                            'They are opposite each other at the same crossing.', fig=G),
                         mc(LINES + ' What kind of angle pair are angles 3 and 7?', 'Corresponding angles',
                            [('Vertical angles', 'vertical angles are at the same crossing'),
                             ('Alternate interior angles', 'angle 7 is below q, outside the two lines'),
                             ('A linear pair', 'a linear pair is at one crossing and shares a side')],
                            'Both are in the lower-left position at their crossings.', fig=G),
                         tf(LINES + ' Angles 3 and 5 are alternate interior angles.', False,
                            'Both are on the left of t; they are same-side interior angles. The alternate interior pairs are '
                            '3 and 6, and 4 and 5.', fig=G),
                         values(LINES + ' Angle 3 = 2x + 10 degrees and angle 2 = 3x - 15 degrees. They are vertical angles. '
                                        'Find x.', [('x', 'x =')], 'x == 25', {'x': 25},
                                'Vertical angles are equal: 2x + 10 = 3x - 15, so x = 25.',
                                wrong=[{'x': 5}, {'x': 37}], fig=G),
                     ])],
             f1=FW('Perpendicular bisectors and converses', 'Harder: the perpendicular bisector theorem and converses.', [
                 order('M is the midpoint of segment AB, and line PM is perpendicular to AB, so P is on the perpendicular '
                       'bisector of AB. Put the steps of the proof that PA = PB in a correct order. (Two orders are '
                       'correct.)',
                       [('A', 'AM = BM, and angles PMA and PMB are right angles (midpoint; perpendicular)'),
                        ('B', 'PM = PM (a segment equals itself)'),
                        ('C', 'Triangle PMA is congruent to triangle PMB (SAS)'),
                        ('D', 'PA = PB (corresponding parts of congruent triangles)')],
                       lambda p: p[-1] == 'D' and p[-2] == 'C',
                       'The two side facts and the angle fact come first, in either order; then SAS, then the conclusion.',
                       expect=list('ABCD')),
                 mc('Theorem: a point is on the perpendicular bisector of AB exactly when it is the same distance from A and '
                    'B. Point P has PA = PB = 7. What follows?', 'P is on the perpendicular bisector of AB.',
                    [('P is the midpoint of AB.', 'P need not be on segment AB at all'),
                     ('AB = 7.', 'the distances to A and B do not fix the length of AB'),
                     ('Nothing follows without more information.', 'the theorem works in both directions')],
                    'The "exactly when" part means equal distances put P on the perpendicular bisector.'),
                 tf(LINES + ' Lines p and q are parallel. Then angle 4 + angle 6 = 180 degrees.', True,
                    'Angle 4 = angle 5 (alternate interior), and angle 5 + angle 6 = 180 degrees (linear pair).', fig=F,
                    check=lambda: SAME[4] != SAME[6]),
                 values(LINES + ' Lines p and q are parallel. Angle 4 = 3x + 5 degrees and angle 5 = 5x - 35 degrees. Find '
                                'x.', [('x', 'x =')], 'x == 20', {'x': 20},
                        'Alternate interior angles are equal: 3x + 5 = 5x - 35, so x = 20 (both angles are 65 degrees).',
                        wrong=[{'x': 15}, {'x': 65}], fig=F),
                 mc(LINES + ' Here p and q are NOT known to be parallel. Which fact would prove that they are parallel?',
                    'angle 3 = angle 6', [('angle 1 = angle 4', 'vertical angles are always equal, parallel or not'),
                                          ('angle 1 + angle 2 = 180 degrees', 'a linear pair always adds to 180 degrees'),
                                          ('angle 5 = angle 8', 'vertical angles are always equal, parallel or not')],
                    'If alternate interior angles are equal, the lines are parallel (the converse theorem).', fig=G),
             ]),
             f2=FW('Complete and check angle proofs', 'Expert: same-side interior angles, flawed proofs, systems.', [
                 order(LINES + ' Put the steps of the proof that angle 4 + angle 6 = 180 degrees when p is parallel to q in a '
                               'correct order. (Two orders are correct.)',
                       [('A', 'angle 4 = angle 5 (alternate interior angles, p parallel to q)'),
                        ('B', 'angle 5 + angle 6 = 180 degrees (linear pair)'),
                        ('C', 'angle 4 + angle 6 = 180 degrees (substitute angle 4 for angle 5)')],
                       lambda p: p[-1] == 'C', 'A and B in either order, then the substitution.', expect=list('ABC'), fig=F),
                 mc('A student writes: "Angle 1 = angle 4 because they look the same size in the diagram." What is wrong '
                    'with this step?', 'A diagram is not a reason; the step needs the vertical angles theorem.',
                    [('Angles 1 and 4 are never equal.', 'vertical angles are always equal'),
                     ('The step should say angle 1 + angle 4 = 180 degrees.', 'that is false for vertical angles in general'),
                     ('Nothing; looking at the diagram is enough.', 'diagrams can be drawn inaccurately')],
                    'Each step of a proof must cite a definition, given or theorem.'),
                 values(LINES + ' Lines p and q are parallel. Angle 1 = 2x + 30 degrees and angle 6 = x + 15 degrees. Find x.',
                        [('x', 'x =')], 'x == 45', {'x': 45},
                        'Angle 1 = angle 5 (corresponding), and angle 5 + angle 6 = 180. So 2x + 30 + x + 15 = 180, 3x = '
                        '135, x = 45.', wrong=[{'x': 15}, {'x': -15}], fig=F),
                 tf(LINES + ' Without knowing that p and q are parallel, one can conclude that angle 3 = angle 6.', False,
                    'Alternate interior angles are equal only when the lines are parallel. If p is tilted, angle 3 and '
                    'angle 6 differ.', fig=G),
                 sa('P is on the perpendicular bisector of segment AB. PA = 3x - 4 and PB = x + 10. What is PA?', 'PA =', '17',
                    'Points on the perpendicular bisector are equidistant from A and B: 3x - 4 = x + 10, so x = 7 and PA = '
                    '17.', compute=lambda: str(3 * 7 - 4)),
             ]))


# ------------------------------------------------------------------ Set 44: invariants and impossibility
def coin_reach(start, move):
    seen = {start}
    q = deque([start])
    while q:
        s = q.popleft()
        for t in move(s):
            if t not in seen:
                seen.add(t)
                q.append(t)
    return seen


def flip_adjacent(s):
    flip = {'H': 'T', 'T': 'H'}
    return [s[:i] + flip[s[i]] + flip[s[i + 1]] + s[i + 2:] for i in range(len(s) - 1)]


def robot_reach(target, moves, limit=12):
    return any(tuple(sum(k * m[i] for k, m in zip(ks, moves)) for i in range(2)) == target
               for ks in itertools.product(range(limit), repeat=len(moves)))


def board_finals(nums, op):
    """Every possible final number when a move erases two numbers and writes op(a, b)."""
    out = set()
    seen = set()

    def go(ms):
        key = tuple(sorted(ms))
        if key in seen:
            return
        seen.add(key)
        if len(ms) == 1:
            out.add(ms[0])
            return
        for i, j in itertools.combinations(range(len(ms)), 2):
            rest = [ms[k] for k in range(len(ms)) if k not in (i, j)]
            go(rest + [op(ms[i], ms[j])])
    go(list(nums))
    return out


def s44():
    COINS = 'HHTHTTT'
    reach = coin_reach(COINS, flip_adjacent)
    return S(44, 'Find a quantity that never changes under the allowed moves and use it to prove a target is impossible',
             main=[
                 mc('The numbers 1, 2, 3, ..., 10 are written on a board. A move erases any two numbers and writes their sum. '
                    'After 9 moves one number is left. What is it?', '55',
                    [('10', 'the moves combine numbers; they do not count them'),
                     ('45', 'that is the sum of 1 to 9; the 10 is still there'),
                     ('It depends on the moves chosen', 'every move keeps the total the same')],
                    'Erasing a and b and writing a + b does not change the total. The total starts at 55, so the last '
                    'number is 55.', check=lambda t: t.isdigit() and board_finals(range(1, 11), lambda a, b: a + b) == {int(t)}),
                 tf('The numbers 1, 2, ..., 10 are written on a board. A move erases two numbers and writes their difference '
                    '(larger minus smaller). After 9 moves one number is left. It can be 0.', False,
                    'Replacing a and b by a - b changes the total by 2b, an even amount, so the total stays odd (it starts '
                    'at 55). The last number is odd, so it cannot be 0.',
                    check=lambda: 0 in board_finals(range(1, 11), lambda a, b: abs(a - b))),
                 sa('Seven coins lie in a row: H H T H T T T (H = heads, T = tails). A move turns over any two coins that are '
                    'next to each other. What is the smallest number of heads that can ever be showing?', 'Heads:',
                    str(min(s.count('H') for s in reach)),
                    'A move changes the number of heads by -2, 0 or +2, so it stays odd (it starts at 3). It can reach 1 '
                    'but never 0.', compute=lambda: str(min(s.count('H') for s in reach))),
                 values('Seven coins lie in a row: H H T H T T T. A move turns over any two coins that are next to each other. '
                        'Give a number of heads (0 to 7) that can be showing after some moves.', [('h', 'Heads =')],
                        'isInteger(h) and h >= 0 and h <= 7 and isOdd(h)', {'h': 5},
                        'The number of heads stays odd: 1, 3, 5 or 7 are possible, and all four can be reached.',
                        wrong=[{'h': 0}, {'h': 4}, {'h': 2}],
                        method='Breadth-first search over all reachable rows: head counts %s.'
                        % sorted({s.count('H') for s in reach})),
                 mc('A robot starts at the point (0, 0). Each move takes it from (x, y) to (x + 1, y + 2) or to (x + 2, y + 1). '
                    'Which point can it reach?', '(4, 5)',
                    [('(5, 5)', 'each move adds 3 to x + y, but 5 + 5 = 10 is not a multiple of 3'),
                     ('(2, 3)', '2 + 3 = 5 is not a multiple of 3'),
                     ('(7, 0)', '7 + 0 = 7 is not a multiple of 3, and y can never stay 0')],
                    'x + y is always a multiple of 3. (4, 5): two moves of (1, 2) and one of (2, 1).',
                    check=lambda t: robot_reach(tuple(int(v) for v in t.strip('()').split(', ')), [(1, 2), (2, 1)])),
             ],
             back=[B('Strategy: look for something that never changes', 'guided_strategy',
                     'Students try move after move without end. A quantity that every move leaves unchanged (an invariant) '
                     'can prove at once that a target is out of reach.',
                     lesson=lesson('Look for something that never changes',
                                   ['Write down how one move changes simple quantities: a total, a count, odd/even, or a '
                                    'remainder.',
                                    'If some quantity is the same after every move, it is an invariant.',
                                    'Compare the invariant at the start and at the target. If they differ, the target can '
                                    'never be reached.'],
                                   'Worked example (a different puzzle)',
                                   ['A counter shows 14. A move adds 6 or subtracts 9. Can it ever show 20?'],
                                   ['Both moves change the count by a multiple of 3, so the remainder after dividing by 3 '
                                    'never changes.',
                                    '14 leaves remainder 2; 20 leaves remainder 2 too, so this test does not rule it out. '
                                    'Indeed 14 + 6 = 20.']),
                     qs=[
                         mc('A counter shows 12. A move adds 4 or subtracts 6. Can it ever show 15?',
                            'No: every move keeps the number even, and 15 is odd.',
                            [('Yes: add 4, then subtract 1.', 'subtracting 1 is not an allowed move'),
                             ('Yes: after enough moves.', 'no number of moves can change even to odd'),
                             ('No: 15 is not a multiple of 4.', '12 + 4 + 4 - 6 = 14 is reachable and is not a multiple of '
                                                               '4 either; the true reason is parity')],
                            'Adding 4 or subtracting 6 keeps an even number even.'),
                         tf('Three numbers on a board are 2, 4 and 9. A move adds 2 to any one of them. The total of the three '
                            'numbers always stays odd.', True,
                            'The total starts at 15 (odd), and each move adds 2, which keeps it odd.'),
                         sa('A move erases two numbers a and b on a board and writes a + b. The board starts with 3, 5, 6 and '
                            '8. What number is left after 3 moves?', 'Number:', '22',
                            'The total never changes: 3 + 5 + 6 + 8 = 22.',
                            compute=lambda: str(board_finals([3, 5, 6, 8], lambda a, b: a + b).pop())),
                         tf('If a quantity is the same after every allowed move, it can never change, however many moves are '
                            'made.', True, 'Each move leaves it unchanged, so a chain of moves does too.'),
                         mc('A robot starts at (0, 0). Each move goes from (x, y) to (x + 2, y) or to (x, y + 2). Which point '
                            'can it NEVER reach?', '(3, 4)',
                            [('(2, 4)', 'reached by (2, 0), then (2, 2), then (2, 4)'),
                             ('(0, 6)', 'three moves of (0, 2)'), ('(4, 0)', 'two moves of (2, 0)')],
                            'Both coordinates always stay even, and 3 is odd.',
                            check=lambda t: not robot_reach(tuple(int(v) for v in t.strip('()').split(', ')),
                                                            [(2, 0), (0, 2)])),
                     ])],
             f1=FW('Invariants with remainders', 'Harder: remainders and totals that change in a fixed way.', [
                 sa('The numbers 1, 2, ..., 10 are on a board. A move erases two numbers a and b and writes a + b + 1. After 9 '
                    'moves one number is left. What is it?', 'Number:',
                    str(board_finals(range(1, 11), lambda a, b: a + b + 1).pop()),
                    'Each move raises the total by exactly 1. The total starts at 55, and 9 moves add 9: 64.',
                    compute=lambda: str(board_finals(range(1, 11), lambda a, b: a + b + 1).pop())
                    if len(board_finals(range(1, 9), lambda a, b: a + b + 1)) == 1 else 'MISMATCH'),
                 tf('A robot starts at (0, 0). Each move goes from (x, y) to (x + 1, y + 2) or to (x + 2, y + 1). It can reach '
                    '(10, 10).', False, 'x + y must be a multiple of 3, and 20 is not.',
                    check=lambda: robot_reach((10, 10), [(1, 2), (2, 1)])),
                 mc('Three numbers are on a board: 1, 2, 3. A move picks two of them, adds 1 to one and subtracts 1 from the '
                    'other. Which quantity never changes?', 'The total of the three numbers',
                    [('The largest number', 'adding 1 to the largest number changes it'),
                     ('The product of the three numbers', '1, 2, 3 can become 0, 3, 3, whose product is 0'),
                     ('The number of odd numbers', '1, 2, 3 can become 2, 2, 2, which has no odd numbers')],
                    'The move adds 1 and subtracts 1, so the total is always 6.'),
                 values('Ten coins all show heads. A move turns over any four coins (they need not be next to each other). '
                        'Give a number of heads from 0 to 10 that can NEVER be showing.', [('h', 'Heads =')],
                        'isInteger(h) and h >= 0 and h <= 10 and isOdd(h)', {'h': 7},
                        'If k of the four turned coins were heads, the heads count changes by (4 - k) - k = 4 - 2k, an even '
                        'number. It starts at 10, so it stays even: 1, 3, 5, 7 and 9 are impossible.',
                        wrong=[{'h': 0}, {'h': 6}, {'h': 10}],
                        method='Search of all reachable head counts: %s.' % sorted(reach_count(10, 10, 4))),
                 sa('A counter shows 100. A move subtracts 7 or adds 3. What is the smallest number of moves that makes it '
                    'show 0?', 'Moves:', str(min_moves(100, 0, (-7, 3))),
                    'If a moves subtract 7 and b moves add 3, then 7a - 3b = 100. So 7a is at least 100 and 7a - 100 is a '
                    'multiple of 3: a = 16 gives 112 - 100 = 12, so b = 4. Total 16 + 4 = 20, and any other solution has '
                    'larger a and b.', compute=lambda: str(min_moves(100, 0, (-7, 3)))),
             ]),
             f2=FW('Prove targets impossible', 'Expert: build the invariant yourself.', [
                 sa('The numbers 1, 2, 3, 4 and 5 are on a board. A move erases two numbers a and b and writes '
                    'a x b + a + b. After 4 moves one number is left. What is it?', 'Number:',
                    str(board_finals(range(1, 6), lambda a, b: a * b + a + b).pop()),
                    'a x b + a + b = (a + 1)(b + 1) - 1. So the product of (each number + 1) never changes: 2 x 3 x 4 x 5 '
                    'x 6 = 720. The last number n has n + 1 = 720, so n = 719.',
                    compute=lambda: str(board_finals(range(1, 6), lambda a, b: a * b + a + b).pop())),
                 tf('A 4 by 4 grid of lights starts all off. A move switches every light in one whole row, or every light '
                    'in one whole column. Some sequence of moves leaves exactly one light on.', False,
                    'Look at any 2 by 2 block of lights. A row or column move switches either none or exactly 2 of its 4 '
                    'lights, so the number of lit lights in the block stays even. With exactly one light on, a block '
                    'containing it would have 1 lit light, which is odd.', check=lambda: 1 in light_counts()),
                 mc('A robot starts at (0, 0). Each move goes from (x, y) to (x + 3, y), to (x, y + 3), or to (x + 1, y + 1). '
                    'Which point can it reach?', '(5, 2)',
                    [('(4, 0)', 'x - y changes only by 3, -3 or 0, so it stays a multiple of 3; here x - y = 4'),
                     ('(2, 3)', 'here x - y = -1, not a multiple of 3'),
                     ('(1, 5)', 'here x - y = -4, not a multiple of 3')],
                    'x - y is always a multiple of 3. (5, 2): two moves of (1, 1) and one of (3, 0).',
                    check=lambda t: robot_reach(tuple(int(v) for v in t.strip('()').split(', ')), [(3, 0), (0, 3), (1, 1)])),
                 values('A 4 by 4 grid of lights starts all off. A move switches every light in one whole row, or every light '
                        'in one whole column. Give a number of lit lights from 1 to 15 that some sequence of moves can '
                        'leave.', [('h', 'Lit lights =')], 'h == 4 or h == 6 or h == 8 or h == 10 or h == 12', {'h': 6},
                        'Only the rows and columns switched an odd number of times matter. With r such rows and c such '
                        'columns, the lit count is 4r + 4c - 2rc. For r and c from 0 to 4 this gives 0, 4, 6, 8, 10, 12 or '
                        '16.', wrong=[{'h': 1}, {'h': 2}, {'h': 5}, {'h': 14}],
                        method='Breadth-first search of all reachable patterns: lit counts %s.' % sorted(light_counts())),
                 tf('The numbers 1, 2, 3, ..., 10 are on a board. A move erases two numbers a and b and writes a + b + 1. The '
                    'last number left does not depend on which moves are made.', True,
                    'Each move raises the total by exactly 1, and there are always exactly 9 moves, so the last number is '
                    '55 + 9 = 64.', check=lambda: len(board_finals(range(1, 9), lambda a, b: a + b + 1)) == 1),
             ]))


def min_moves(start, target, steps, lo=-60, hi=220):
    dist = {start: 0}
    q = deque([start])
    while q:
        v = q.popleft()
        for d in steps:
            w = v + d
            if lo <= w <= hi and w not in dist:
                dist[w] = dist[v] + 1
                q.append(w)
    return dist[target]


def light_counts():
    moves = [[r * 4 + c for c in range(4)] for r in range(4)] + [[r * 4 + c for r in range(4)] for c in range(4)]
    seen = {0}
    q = deque([0])
    while q:
        s = q.popleft()
        for m in moves:
            t = s
            for cell in m:
                t ^= 1 << cell
            if t not in seen:
                seen.add(t)
                q.append(t)
    return {bin(s).count('1') for s in seen}


SETS = [s41(), s42(), s43(), s44()]
