"""Logic sets 27-30: negating quantified statements; routes and networks; witnesses and counterexamples; Venn diagrams."""
import itertools
from collections import deque
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt, venn
import figs

TF = [True, False]


# ------------------------------------------------------------------ Set 27: negating quantified statements
def s27():
    return S(27, 'Negate statements with "all", "some", "no", and nested quantifiers',
             main=[
                 mc('What is the negation of "All the tickets were sold"?', 'At least one ticket was not sold.',
                    [('No ticket was sold.', 'too strong: one unsold ticket is enough to make the original false'),
                     ('All the tickets were unsold.', 'same as "no ticket was sold"'),
                     ('Some tickets were sold.', 'compatible with the original')],
                    'The negation of "all are" is "some (at least one) is not".'),
                 mc('What is the negation of "Some student brought a calculator"?', 'No student brought a calculator.',
                    [('Some student did not bring a calculator.', 'can be true together with the original'),
                     ('Every student brought a calculator.', 'that makes the original true'),
                     ('Exactly one student brought a calculator.', 'that makes the original true')],
                    'The negation of "at least one is" is "none is".'),
                 mc('What is the negation of "No bridge in the town is closed"?', 'Some bridge in the town is closed.',
                    [('Every bridge in the town is closed.', 'too strong'), ('Some bridge in the town is open.', 'compatible '
                                                                                                                'with the '
                                                                                                                'original'),
                     ('No bridge in the town is open.', 'not the negation')],
                    'The negation of "none is" is "at least one is".'),
                 values('The domain is the whole numbers. The statement "Every whole number greater than 1 has an even '
                        'square" is false. Give a number n that makes its negation true: a whole number greater than 1 whose '
                        'square is odd.', [('n', 'n =')], 'n > 1 and isOdd(n*n) and isInteger(n)', {'n': 3},
                        'The negation is "Some whole number greater than 1 has an odd square": any odd n > 1.',
                        wrong=[{'n': 2}, {'n': 1}, {'n': 4}]),
                 tf('The negation of "Every square is a rectangle" is "No square is a rectangle".', False,
                    'The negation is "Some square is not a rectangle".'),
             ],
             back=[
                 B('The meaning of each quantifier', 'prerequisite', 'Negating a quantifier needs a precise meaning of "all", '
                                                                    '"some" and "no".', outcome='LOGIC.QUANT.01', qs=[
                     tf('"Some cards are red" is false if exactly one card is red.', False, '"Some" means at least one, so one red card makes the statement true.'),
                     tf('"All cards are red" is false if one card is blue.', True, 'One exception is enough.'),
                     tf('"No card is red" is true if one card is red.', False, '"No" means zero.'),
                     mc('"Not all cards are red" means ...', 'at least one card is not red',
                        [('no card is red', 'too strong'), ('exactly one card is red', 'unrelated'),
                         ('every card is blue', 'too strong')], 'One non-red card is enough.'),
                     tf('"Some cards are red" and "some cards are not red" can both be true.', True, 'A mix of red and blue.'),
                 ]),
                 B('Negating simple statements', 'prerequisite', 'Inside a quantified statement the property itself is '
                                                                'negated; students need simple negation first.',
                   outcome='LOGIC.CONNECTIVE.01', qs=[
                       mc('What is the negation of "the bus is late"?', 'the bus is not late',
                          [('the bus is early', 'it could be on time'), ('the train is late', 'unrelated'),
                           ('the bus is very late', 'not a negation')], 'Negate the whole claim.'),
                       tf('The negation of "x ≥ 4" is "x ≤ 4".', False, 'x = 4 makes both "x ≥ 4" and "x ≤ 4" true, so they are not negations. The negation is "x < 4".'),
                       mc('What is the negation of "the number is even and positive"?', 'the number is odd or not positive',
                          [('the number is odd and negative', 'too strong'), ('the number is even or positive', 'not a '
                                                                                                                'negation'),
                           ('the number is zero', 'too narrow')], 'Not (A and B) = not A or not B.'),
                       tf('"Not (the door is locked)" means the door is not locked.', True, 'Plain negation.'),
                       mc('What is the negation of "it rained on Monday or Tuesday"?', 'it rained on neither Monday nor Tuesday',
                          [('it did not rain on Monday', 'it could have rained on Tuesday'),
                           ('it rained on both days', 'not a negation'), ('it rained on Wednesday', 'unrelated')],
                          'Not (A or B) = not A and not B.'),
                   ]),
             ],
             f1=FW('Negate quantified statements with conditions', 'Harder: quantifiers over conditions and inequalities.', [
                 mc('What is the negation of "Every student who studied passed"?', 'Some student who studied did not pass.',
                    [('Every student who did not study failed.', 'unrelated to the original claim'),
                     ('No student who studied passed.', 'too strong'), ('Some student who passed did not study.', 'swaps the '
                                                                                                                  'condition')],
                    'Negation of "every A is B": some A is not B.'),
                 mc('The domain is the real numbers. What is the negation of "For every x, x squared ≥ 0"?',
                    'There is an x with x squared < 0.', [('For every x, x squared < 0.', 'too strong'),
                                                          ('There is an x with x squared ≥ 0.', 'compatible with the original'),
                                                          ('For every x, x squared ≤ 0.', 'not the negation')],
                    'Negation: "there is an x" with the opposite inequality.'),
                 tf('The negation of "Some prime number is even" is "Every prime number is odd" (for whole numbers greater than '
                    '1).', True, '"No prime is even" means every prime is not even; for whole numbers greater than 1, not even '
                                 'means odd.'),
                 values('The statement "Every whole number from 1 to 30 that ends in 9 is prime" is false. Give a number that '
                        'shows it (a witness for its negation).', [('n', 'n =')],
                        'n % 10 == 9 and n >= 1 and n <= 30 and not isPrime(n)', {'n': 9},
                        'The numbers ending in 9 are 9, 19 and 29; 19 and 29 are prime, but 9 = 3 x 3 is not. So n = 9.',
                        wrong=[{'n': 19}, {'n': 29}, {'n': 39}], search={'n': range(1, 31)}),
                 tf('The negation of "No dog is a cat" is "Every dog is a cat".', False, 'The negation is "Some dog is a cat".'),
             ]),
             f2=FW('Nested quantifiers and their negations', 'Expert: negate "for every ... there is ...".', [
                 mc('What is the negation of "For every student, there is a club the student likes"?',
                    'There is a student who likes no club.',
                    [('For every student, there is a club the student does not like.', 'only flips the inner part'),
                     ('There is a club that no student likes.', 'swaps the roles'),
                     ('No student likes any club.', 'too strong')],
                    'Negate step by step: "there is a student such that NOT (there is a club the student likes)" = "there is '
                    'a student who likes no club".'),
                 mc('The domain is the whole numbers. What is the negation of "There is a number y such that for every x, y > '
                    'x"?', 'For every y, there is an x with y ≤ x.',
                    [('For every y and every x, y ≤ x.', 'too strong'), ('There is a y with y ≤ x for some x.', 'not the '
                                                                                                             'negation'),
                     ('There is no number y.', 'not the negation')],
                    'Flip each quantifier and negate the inside: for every y, there is an x such that not (y > x).'),
                 tf('The negation of "For every x there is a y with x + y = 0" is "There is an x such that for every y, x + y ≠ '
                    '0".', True, 'Flip both quantifiers and negate the equation.'),
                 values('The domain is the whole numbers 1 to 10. The statement "For every x there is a y with y = 2x" is false '
                        'in this domain. Give an x that shows it.', [('x', 'x =')], 'x >= 6 and x <= 10 and isInteger(x)',
                        {'x': 6}, 'For x from 6 to 10, 2x is at least 12, outside the domain. Any of 6 to 10 works.',
                        wrong=[{'x': 5}, {'x': 1}, {'x': 11}], search={'x': range(1, 11)}),
                 tf('For any statement about a domain, either the statement or its negation is true.', True,
                    'A statement and its negation always have opposite truth values.'),
             ]))


# ------------------------------------------------------------------ Set 28: routes and networks
G1 = {'nodes': {'A': (40, 130), 'B': (130, 50), 'C': (130, 210), 'D': (230, 130), 'E': (320, 50), 'F': (320, 210)},
      'edges': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('D', 'F'), ('E', 'F')]}


def nbrs(g, x):
    return sorted({b for a, b in g['edges'] if a == x} | {a for a, b in g['edges'] if b == x})


def simple_paths(g, s, t):
    out = []

    def go(x, path):
        if x == t:
            out.append(path)
            return
        for y in nbrs(g, x):
            if y not in path:
                go(y, path + [y])
    go(s, [s])
    return out


def dist(g, s, t):
    seen = {s: 0}
    q = deque([s])
    while q:
        x = q.popleft()
        for y in nbrs(g, x):
            if y not in seen:
                seen[y] = seen[x] + 1
                q.append(y)
    return seen.get(t)


def degrees(g):
    return {n: len(nbrs(g, n)) for n in g['nodes']}


def connected(g, removed=()):
    nodes = [n for n in g['nodes'] if n not in removed]
    seen = {nodes[0]}
    q = deque([nodes[0]])
    while q:
        x = q.popleft()
        for y in nbrs(g, x):
            if y not in removed and y not in seen:
                seen.add(y)
                q.append(y)
    return len(seen) == len(nodes)


def gfig(g, size=(360, 260)):
    return (figs.network(g['nodes'], g['edges'], size=size).svg(),
            'A network of towns ' + ', '.join(sorted(g['nodes'])) + ' joined by roads: ' +
            ', '.join('%s-%s' % e for e in g['edges']) + '.')


ROAD_RULE = 'Roads are the straight lines; towns are the circles. Roads meet only at towns.'

G2 = {'nodes': {'P': (50, 60), 'Q': (180, 40), 'R': (310, 60), 'S': (50, 200), 'T': (180, 220), 'U': (310, 200)},
      'edges': [('P', 'Q'), ('Q', 'R'), ('P', 'S'), ('Q', 'T'), ('R', 'U'), ('S', 'T'), ('T', 'U'), ('Q', 'U')]}


def euler_trail_exists(g):
    odd = sum(1 for d in degrees(g).values() if d % 2)
    return connected(g) and odd in (0, 2)


def tangled():
    """Three walkers start on the left (1, 2, 3) and follow lines to gates on the right (X, Y, Z). Lines cross without
    joining (no dot at a crossing). Returns (svg, mapping)."""
    c = figs.Canvas(380, 230)
    starts = {'1': 40, '2': 115, '3': 190}
    ends = {'X': 40, 'Y': 115, 'Z': 190}
    paths = {'1': [(40, 40), (120, 40), (200, 180), (280, 115), (340, 115)],
             '2': [(40, 115), (110, 115), (190, 40), (270, 190), (340, 190)],
             '3': [(40, 190), (150, 190), (250, 40), (340, 40)]}
    dashes = {'1': None, '2': '7 4', '3': '2 4'}
    for k, pts in paths.items():
        c.poly(pts, close=False, sw=2.6)
    for k, y in starts.items():
        c.circle(22, y, 13, fill='white', sw=2)
        c.text(22, y + 5, k, size=13, weight='bold')
    for k, y in ends.items():
        c.rect(345, y - 13, 26, 26, fill='white', sw=2)
        c.text(358, y + 5, k, size=13, weight='bold')
    mapping = {k: [e for e, y in ends.items() if y == pts[-1][1]][0] for k, pts in paths.items()}
    return c.svg(), mapping


def s28():
    paths_AF = simple_paths(G1, 'A', 'F')
    tsvg, tmap = tangled()
    return S(28, 'Trace routes in a network and decide which routes exist',
             main=[
                 sa(ROAD_RULE + ' What is the least number of roads on a route from A to F?', 'Roads:', '3',
                    'A to B (or C), then to D, then to F: 3 roads. No route uses fewer, because A is not joined to D or F, and '
                    'no town next to A is joined to F.', fig=gfig(G1), compute=lambda: str(dist(G1, 'A', 'F'))),
                 sa(ROAD_RULE + ' How many different routes go from A to F without visiting any town twice?', 'Routes:',
                    str(len(paths_AF)), 'Every route goes through D (the only way to E and F). From A to D: A-B-D, A-C-D, '
                                        'A-B-C-D, A-C-B-D (4 ways). From D to F: D-F or D-E-F (2 ways). 4 x 2 = 8.',
                    fig=gfig(G1), compute=lambda: str(len(simple_paths(G1, 'A', 'F')))),
                 mc(ROAD_RULE + ' Which town, if it were closed (with all its roads), would cut the network into two parts '
                                'that cannot reach each other?', 'D', [('B', 'A can still reach D through C'),
                                                                       ('C', 'A can still reach D through B'),
                                                                       ('E', 'F is still joined to D')],
                    'Every route from A, B or C to E or F passes through D.', fig=gfig(G1),
                    check=lambda t: not connected(G1, removed=(t,))),
                 mc('Walkers 1, 2 and 3 each follow their own line from the left to a gate on the right. Where lines cross, '
                    'there is no turning: each walker keeps going straight along their own line. Which gate does walker 2 reach?',
                    tmap['2'], [(g, 'that is where another walker\'s line ends') for g in 'XYZ' if g != tmap['2']] +
                    [('none of the gates', 'every line ends at a gate')],
                    'Follow line 2: it goes right, climbs to the top, crosses down to the bottom right and ends at gate %s.'
                    % tmap['2'], fig=(tsvg, 'Three lines start at circles 1, 2, 3 on the left and end at squares X, Y, Z on the '
                                            'right; the lines cross each other.'),
                    check=lambda t: t == tmap['2']),
                 tf(ROAD_RULE + ' A walk can use every road exactly once (towns may be visited more than once).',
                    euler_trail_exists(G1),
                    'Count the roads at each town: A 2, B 3, C 3, D 4, E 2, F 2. Exactly two towns (B and C) have an odd '
                    'number, so a walk using every road once exists: it must start at B and end at C (or the reverse).',
                    fig=gfig(G1), check=lambda: euler_trail_exists(G1)),
             ],
             back=[B('Strategy: mark the route as you trace it', 'guided_strategy',
                     'Students lose track in a busy network or miscount routes. Tracing with a finger and writing the towns in '
                     'order, and listing routes in a fixed order, makes counts complete.',
                     lesson=lesson('Mark the route as you trace it',
                                   ['Write each route as a list of towns, for example A-B-D.',
                                    'To count routes, list them in a fixed order: all routes starting A-B first, then those '
                                    'starting A-C, and so on. Never revisit a town in the same route if the rule forbids it.',
                                    'For the shortest route, find all towns 1 road away, then all towns 2 roads away, and so on.',
                                    'For a walk that uses every road once, count roads at each town: it is possible only if 0 '
                                    'or 2 towns have an odd number of roads (and the network is all one piece).'],
                                   'Worked example (a different network)',
                                   ['Towns W, X, Y, Z with roads W-X, X-Y, Y-Z, W-Y. How many routes from W to Z without '
                                    'repeating a town?'],
                                   ['Routes must end with Y-Z, because Z only touches Y.',
                                    'From W to Y: W-Y, or W-X-Y.',
                                    'So the routes are W-Y-Z and W-X-Y-Z: 2 routes.']),
                     qs=[
                         sa(ROAD_RULE + ' How many roads meet at town D?', 'Roads:', '4', 'D-B, D-C, D-E, D-F.', fig=gfig(G1),
                            compute=lambda: str(degrees(G1)['D'])),
                         mc(ROAD_RULE + ' Which towns can be reached from A using exactly one road?', 'B and C',
                            [('B, C and D', 'D needs two roads'), ('only B', 'C is also joined to A'),
                             ('D', 'not joined to A')], 'A is joined only to B and C.', fig=gfig(G1),
                            check=lambda t: set(t.split(' and ')) == set(nbrs(G1, 'A'))),
                         tf(ROAD_RULE + ' There is a road directly from A to D.', False, 'A is joined only to B and C.',
                            fig=gfig(G1), check=lambda: ('A', 'D') in G1['edges'] or ('D', 'A') in G1['edges']),
                         sa(ROAD_RULE + ' How many routes go from E to F without visiting a town twice?', 'Routes:', '2',
                            'E-F directly, or E-D-F.', fig=gfig(G1), compute=lambda: str(len(simple_paths(G1, 'E', 'F')))),
                         tf('In a network, a town with 3 roads must be the start or end of a walk that uses every road once.',
                            True, 'At a town in the middle of the walk, roads are used in pairs (in and out); an odd number '
                                  'leaves one unpaired road, so the walk must start or end there.'),
                     ])],
             f1=FW('Routes with conditions', 'Harder: routes that must or must not pass certain towns, and longer networks.', [
                 sa(ROAD_RULE + ' How many routes go from P to U without visiting a town twice?', 'Routes:',
                    str(len(simple_paths(G2, 'P', 'U'))), 'Listing them in order: P-Q-R-U, P-Q-U, P-Q-T-U, P-S-T-U, '
                                                          'P-S-T-Q-R-U, P-S-T-Q-U.', fig=gfig(G2),
                    compute=lambda: str(len(simple_paths(G2, 'P', 'U')))),
                 sa(ROAD_RULE + ' How many routes from P to U (no town twice) pass through T?', 'Routes:', '4',
                    'P-Q-T-U, P-S-T-U, P-S-T-Q-R-U, P-S-T-Q-U.', fig=gfig(G2),
                    compute=lambda: str(sum(1 for p in simple_paths(G2, 'P', 'U') if 'T' in p))),
                 tf(ROAD_RULE + ' A walk can use every road exactly once.', euler_trail_exists(G2),
                    'Roads at each town: P 2, Q 4, R 2, S 2, T 3, U 3. Exactly two odd towns (T and U), so yes: start at T and '
                    'end at U.', fig=gfig(G2), check=lambda: euler_trail_exists(G2)),
                 mc(ROAD_RULE + ' Which single road, if closed, makes T unreachable from P by any route?', 'none of these roads',
                    [('P-S', 'T can still be reached through Q'), ('Q-T', 'T can still be reached through S'),
                     ('S-T', 'T can still be reached through Q')],
                    'T has three roads (to Q, S and U), and P reaches T through more than one of them, so no single road cuts '
                    'T off.', fig=gfig(G2),
                    check=lambda t: t == 'none of these roads' and all(
                        connected({'nodes': G2['nodes'], 'edges': [e for e in G2['edges'] if e != c]}) for c in
                        [('P', 'S'), ('Q', 'T'), ('S', 'T')])),
                 sa(ROAD_RULE + ' What is the least number of roads on a route from S to R?', 'Roads:', '3',
                    'S-T-U-R or S-P-Q-R or S-T-Q-R: 3 roads.', fig=gfig(G2), compute=lambda: str(dist(G2, 'S', 'R'))),
             ]),
             f2=FW('Every road, every town', 'Expert: walks through every road or every town, and proofs that they cannot '
                                             'exist.', [
                 sa('In a network of 6 towns, the numbers of roads at the towns are 1, 2, 2, 3, 3 and 3. Every road has two '
                    'ends, each at a town. How many roads are there?', 'Roads:', '7',
                    'Adding the numbers counts every road twice (once at each end): 1 + 2 + 2 + 3 + 3 + 3 = 14, so there are '
                    '14 / 2 = 7 roads.', compute=lambda: str((1 + 2 + 2 + 3 + 3 + 3) // 2)),
                 tf('Some network has exactly three towns with an odd number of roads.', False,
                    'Every road adds 2 to the total count of road-ends, so the total is even; that needs an even number of '
                    'odd towns.'),
                 mc(ROAD_RULE + ' What is the least number of roads that must be ADDED so that a walk can use every road '
                                'exactly once and return to its starting town?', '1',
                    [('0', 'B and C have an odd number of roads, so a closed walk is impossible now'),
                     ('2', 'one new road between B and C makes every town even'), ('3', 'far fewer are needed')],
                    'A closed walk needs every town to have an even number of roads. Only B and C are odd; adding one road '
                    'B-C fixes both.', fig=gfig(G1),
                    check=lambda t: t == '1'),
                 sa(ROAD_RULE + ' How many routes from A to F visit EVERY town exactly once?', 'Routes:',
                    str(sum(1 for p in simple_paths(G1, 'A', 'F') if len(p) == 6)),
                    'A route through all six towns must go A, then B and C (in some order), then D, then E, then F: A-B-C-D-E-F '
                    'and A-C-B-D-E-F.', fig=gfig(G1),
                    compute=lambda: str(sum(1 for p in simple_paths(G1, 'A', 'F') if len(p) == 6))),
                 values('A network has towns with these numbers of roads: 3, 3, 2, 2 and k. For a walk that uses every road '
                        'exactly once to be possible in a connected network, at most two towns may have an odd number of '
                        'roads. Give a whole number k from 1 to 6 that keeps this possible.', [('k', 'k =')],
                        'isEven(k) and k >= 1 and k <= 6', {'k': 2},
                        'There are already two odd towns (the two 3s), so k must be even: 2, 4 or 6.',
                        wrong=[{'k': 3}, {'k': 1}, {'k': 5}], search={'k': range(1, 7)}),
             ]))


SETS = [s27(), s28()]
