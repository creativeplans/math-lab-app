"""Logic sets 29-32: witnesses and counterexamples; sets and Venn diagrams; maps and neighbors; categorical arguments."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt, venn
import figs

TF = [True, False]


# ------------------------------------------------------------------ Set 29: witnesses and counterexamples
def s29():
    return S(29, 'Give a witness for a "some" statement and a counterexample to an "all" statement',
             main=[
                 values('Give a witness for the true statement "Some whole number between 20 and 30 is prime."', [('n', 'n =')],
                        'isPrime(n) and n > 20 and n < 30', {'n': 23}, 'The primes between 20 and 30 are 23 and 29.',
                        wrong=[{'n': 21}, {'n': 25}, {'n': 31}], search={'n': range(1, 40)}),
                 values('Give a counterexample to "Every whole number that is divisible by 3 is odd."', [('n', 'n =')],
                        'n % 3 == 0 and isEven(n) and isInteger(n)', {'n': 6},
                        'A counterexample is a multiple of 3 that is even: 6, 12, 18, ...', wrong=[{'n': 9}, {'n': 4}, {'n': 15}]),
                 mc('Which number is a counterexample to "Every number that ends in 1 is prime"?', '21',
                    [('11', '11 is prime, so it agrees with the claim'), ('31', '31 is prime'), ('12', 'does not end in 1')],
                    '21 ends in 1 and 21 = 3 x 7.',
                    check=lambda t: int(t) % 10 == 1 and any(int(t) % d == 0 for d in range(2, int(t)))),
                 values('Give integers a and b (integers are real numbers) that are a counterexample to "For all real numbers a and b, (a + b) squared '
                        '= a squared + b squared."', [('a', 'a ='), ('b', 'b =')], 'a != 0 and b != 0', {'a': 1, 'b': 1},
                        '(a + b) squared - (a squared + b squared) = 2ab, so the claim fails exactly when a and b are both nonzero. '
                        'For example a = 1, b = 1: 4 is not 2.',
                        wrong=[{'a': 0, 'b': 5}, {'a': 3, 'b': 0}]),
                 tf('One example where a statement is true proves "Every number has this property."', False,
                    'An example (a witness) proves only a "some" statement. An "every" statement needs an argument for all cases; '
                    'one counterexample is enough to disprove it.'),
             ],
             back=[
                 B('Read "every" and "some" statements', 'prerequisite', 'A student must know what kind of claim it is before '
                                                                        'choosing a witness or a counterexample.',
                   outcome='LOGIC.QUANT.01', qs=[
                       mc('What kind of example disproves "Every bird can fly"?', 'a bird that cannot fly',
                          [('a bird that can fly', 'agrees with the claim'), ('an animal that is not a bird', 'irrelevant'),
                           ('a flying insect', 'irrelevant')], 'A counterexample has the "every" property but not the claimed one.'),
                       mc('What kind of example proves "Some square numbers are even"?', 'an even square number, such as 4',
                          [('an odd square number', 'does not help'), ('an even number that is not a square', 'not a square'),
                           ('every square number', 'one example is enough')], 'One witness proves "some".'),
                       tf('"All cats are black" is shown true by one black cat.', False, 'One black cat shows that some cats are black. Showing that all cats are black needs every cat to be black.'),
                       tf('"All cats are black" is shown false by one white cat.', True, 'One counterexample.'),
                       tf('"No number is negative" is shown false by the number 1.', False, '1 is not negative, so it does not '
                          'contradict the statement. A negative number such as -1 would.'),
                   ]),
                 B('Test a number against a property', 'prerequisite', 'Checking whether a candidate works requires testing '
                                                                      'each condition exactly.', qs=[
                     tf('15 is prime.', False, '15 = 3 x 5.', check=lambda: all(15 % d for d in range(2, 15))),
                     tf('27 is divisible by 3 and odd.', True, '27 = 3 x 9, odd.', check=lambda: 27 % 3 == 0 and 27 % 2 == 1),
                     sa('What is 7 squared minus 7?', 'Value:', '42', '49 - 7.', compute=lambda: str(7 * 7 - 7)),
                     tf('2 is both prime and even.', True, '2 has exactly two factors and is even.'),
                     mc('Which number is a multiple of 4 but not of 8?', '12', [('16', 'a multiple of 8'), ('8', 'a multiple of '
                                                                                                                 '8'),
                                                                                ('10', 'not a multiple of 4')],
                        '12 = 4 x 3.', check=lambda t: int(t) % 4 == 0 and int(t) % 8 != 0),
                 ]),
             ],
             f1=FW('Counterexamples in algebra', 'Harder: counterexamples to tempting algebra rules.', [
                 values('Give a real number x that is a counterexample to "For every real number x, x squared ≥ x."',
                        [('x', 'x =')], 'x^2 < x', {'x': 0.5}, 'Any x strictly between 0 and 1, such as 0.5 (0.25 < 0.5).',
                        wrong=[{'x': 2}, {'x': -1}, {'x': 1}]),
                 values('Give positive whole numbers a and b that are a counterexample to "If a divides b x c, then a divides b '
                        'or a divides c", using c = 2.', [('a', 'a ='), ('b', 'b =')],
                        'divides(a, b * 2) and not divides(a, b) and not divides(a, 2) and a > 0 and b > 0 and isInteger(a) and isInteger(b)',
                        {'a': 4, 'b': 2}, 'a = 4, b = 2: 4 divides 2 x 2 = 4, but 4 divides neither 2 nor 2. (a = 6, b = 3 also '
                                          'works.)', wrong=[{'a': 3, 'b': 3}, {'a': 2, 'b': 5}]),
                 mc('Which value of n is a counterexample to "n squared + n + 1 is prime for every whole number n ≥ 1"?', '4',
                    [('1', '3 is prime'), ('2', '7 is prime'), ('3', '13 is prime')], '4: 16 + 4 + 1 = 21 = 3 x 7.',
                    check=lambda t: (lambda v: any(v % d == 0 for d in range(2, v)))(int(t) ** 2 + int(t) + 1)),
                 tf('The statement "For every real x, if x > 1 then x squared > x" has no counterexample.', True,
                    'If x > 1, multiplying x > 1 by the positive x gives x squared > x.'),
                 values('Give whole numbers a and b, each from 1 to 9, that show "a - b = b - a" can be false.',
                        [('a', 'a ='), ('b', 'b =')], 'a - b != b - a and a >= 1 and a <= 9 and b >= 1 and b <= 9',
                        {'a': 5, 'b': 2}, 'Any a different from b.', wrong=[{'a': 4, 'b': 4}]),
             ]),
             f2=FW('Witnesses that are hard to find', 'Expert: search a stated range carefully, or show none exists.', [
                 values('Give a witness for "Some whole number from 1 to 100 leaves remainder 2 when divided by 3, remainder 3 '
                        'when divided by 4, and remainder 4 when divided by 5."', [('n', 'n =')],
                        'n % 3 == 2 and n % 4 == 3 and n % 5 == 4 and n >= 1 and n <= 100', {'n': 59},
                        'Each remainder is one less than the divisor, so n + 1 is divisible by 3, 4 and 5, that is by 60. n + 1 = '
                        '60 gives n = 59, the only such number up to 100.',
                        wrong=[{'n': 29}, {'n': 119}, {'n': 14}], search={'n': range(1, 101)}),
                 mc('Is there a whole number n from 1 to 100 with n squared ending in the digit 2?',
                    'No: squares end only in 0, 1, 4, 5, 6 or 9.',
                    [('Yes: n = 12.', '144 ends in 4'), ('Yes: n = 22.', '484 ends in 4'),
                     ('No: but only because 2 is even.', 'that is not the reason; 4 and 6 are even and do appear')],
                    'The last digit of n squared depends only on the last digit of n; checking 0-9 gives 0, 1, 4, 9, 6, 5, 6, 9, '
                    '4, 1.', check=lambda t: t.startswith('No: squares') and not any(n * n % 10 == 2 for n in range(1, 101))),
                 values('Give whole numbers a, b and c (each from 1 to 20) with a squared + b squared = c squared and a < b.',
                        [('a', 'a ='), ('b', 'b ='), ('c', 'c =')],
                        'a^2 + b^2 == c^2 and a < b and a >= 1 and a <= 20 and b >= 1 and b <= 20 and c >= 1 and c <= 20 and isInteger(a) and '
                        'isInteger(b) and isInteger(c)',
                        {'a': 3, 'b': 4, 'c': 5}, 'For example 3, 4, 5; 5, 12, 13; 6, 8, 10; 8, 15, 17; 9, 12, 15; 12, 16, 20.',
                        wrong=[{'a': 2, 'b': 3, 'c': 4}, {'a': 4, 'b': 3, 'c': 5}]),
                 sa('How many counterexamples to "Every odd number from 1 to 30 is prime" are there in that range?',
                    'Counterexamples:', '6', 'Odd numbers 1 to 29 that are not prime: 1, 9, 15, 21, 25, 27.',
                    compute=lambda: str(sum(1 for n in range(1, 31, 2) if n == 1 or any(n % d == 0 for d in range(2, n))))),
                 tf('To disprove "There is a whole number n with n + 5 = n", one example is enough.', False,
                    'A "there is" statement is disproved by showing NO number works: here n + 5 = n would give 5 = 0, which is '
                    'impossible for every n. A single example cannot do that.'),
             ]))


# ------------------------------------------------------------------ Set 30: sets and Venn diagrams
def s30():
    return S(30, 'Mark subset, intersection and complement relations on Venn diagrams',
             main=[
                 venn('Circle A is the set of students in soccer and circle B the set of students in band. Mark the region for '
                      'students in soccer but NOT in band.', ['soccer (A)', 'band (B)'], lambda a, b: a and not b,
                      'Inside A, outside B: the part of A that does not overlap B.'),
                 venn('Circle A is the set of even numbers and circle B the set of multiples of 3 (whole numbers 1 to 30 make up '
                      'the outside box). Mark the region that contains 12.', ['even (A)', 'multiples of 3 (B)'],
                      lambda a, b: a and b, '12 is even and a multiple of 3: the overlap.'),
                 venn('Three circles: A (likes math), B (likes art), C (likes music). Mark every region for people who like '
                      'EXACTLY two of the three subjects.', ['math (A)', 'art (B)', 'music (C)'],
                      lambda a, b, c: a + b + c == 2, 'The three regions where exactly two circles overlap, not the center.'),
                 sa('In a class of 30 students, 18 play soccer, 12 play in the band, and 5 do both. How many students do '
                    'neither?', 'Students:', '5', 'Soccer or band: 18 + 12 - 5 = 25. Neither: 30 - 25 = 5.',
                    compute=lambda: str(30 - (18 + 12 - 5))),
                 venn('Every member of set A is also in set B (A is a subset of B). On a two-circle diagram, mark the region '
                      'that must be EMPTY.', ['A', 'B'], lambda a, b: a and not b,
                      'If every A is a B, nothing can be in A outside B.'),
             ],
             back=[
                 B('Regions of a two-circle diagram', 'prerequisite', 'Students who cannot name the four regions cannot mark '
                                                                     'any relation.', qs=[
                     venn('Mark the region for things in BOTH A and B.', ['A', 'B'], lambda a, b: a and b, 'The overlap.'),
                     venn('Mark the region for things in NEITHER A nor B.', ['A', 'B'], lambda a, b: not a and not b,
                          'Outside both circles.'),
                     venn('Mark every region for things in A (whether or not they are in B).', ['A', 'B'], lambda a, b: a,
                          'A only and the overlap.'),
                     sa('How many regions does a two-circle Venn diagram have, counting the outside?', 'Regions:', '4',
                        'A only, B only, both, neither.', compute=lambda: str(4)),
                     venn('Mark every region for things in B but not in A.', ['A', 'B'], lambda a, b: b and not a, 'B only.'),
                 ]),
                 B('Set words: and, or, not', 'prerequisite', 'Intersection, union and complement are "and", "or" and "not" '
                                                             'for sets.', outcome='LOGIC.CONNECTIVE.02', qs=[
                     mc('The intersection of A and B contains things that are ...', 'in A and in B',
                        [('in A or in B', 'that is the union'), ('in neither', 'outside both'), ('in A but not B', 'part of A')],
                        'Intersection = "and".'),
                     mc('The union of A and B contains things that are ...', 'in A or in B (or both)',
                        [('in A and in B', 'that is the intersection'), ('in exactly one', 'that excludes the overlap'),
                         ('in neither', 'outside both')], 'Union = inclusive "or".'),
                     tf('The complement of A contains everything in the box that is not in A.', True, 'Complement = "not".'),
                     sa('A = {1, 2, 3, 4}, B = {3, 4, 5}. How many numbers are in the union of A and B?', 'Count:', '5',
                        '{1, 2, 3, 4, 5}.', compute=lambda: str(len({1, 2, 3, 4} | {3, 4, 5}))),
                     sa('A = {1, 2, 3, 4}, B = {3, 4, 5}. How many numbers are in the intersection?', 'Count:', '2', '{3, 4}.',
                        compute=lambda: str(len({1, 2, 3, 4} & {3, 4, 5}))),
                 ]),
             ],
             f1=FW('Three-circle diagrams and counts', 'Harder: three sets, complements and counting.', [
                 venn('Three circles A, B, C. Mark every region for things in A or B but NOT in C.', ['A', 'B', 'C'],
                      lambda a, b, c: (a or b) and not c, 'A only, B only and the A-B overlap outside C.'),
                 venn('Three circles A, B, C. Mark every region for things in at least two of the sets.', ['A', 'B', 'C'],
                      lambda a, b, c: a + b + c >= 2, 'The three two-set overlaps and the center.'),
                 sa('Of 40 students, 22 take French, 17 take Spanish and 9 take both. How many take exactly one of the two?',
                    'Students:', '21', 'French only 22 - 9 = 13; Spanish only 17 - 9 = 8; 13 + 8 = 21.',
                    compute=lambda: str((22 - 9) + (17 - 9))),
                 venn('Every member of A is in B, and no member of B is in C. On a three-circle diagram (A, B, C), mark every '
                      'region that must be EMPTY.', ['A', 'B', 'C'], lambda a, b, c: (a and not b) or (b and c),
                      '"Every A is B" empties A outside B (A only and A-C only). "No B is C" empties every region in both B and '
                      'C (B-C only and the center).'),
                 tf('If A is a subset of B, then the intersection of A and B is A.', True, 'Everything in A is also in B.'),
             ]),
             f2=FW('Inclusion and exclusion', 'Expert: count with three sets and decide which counts are possible.', [
                 sa('In a group of 50 people, 25 like tea, 30 like coffee and 15 like both. How many like neither?',
                    'People:', '10', 'Tea or coffee: 25 + 30 - 15 = 40. Neither: 10.', compute=lambda: str(50 - (25 + 30 - 15))),
                 sa('Sets A, B, C have 10, 12 and 8 members. A and B share 4, A and C share 3, B and C share 2, and all three '
                    'share 1. How many members are in the union?', 'Members:', '22',
                    '10 + 12 + 8 - 4 - 3 - 2 + 1 = 22.', compute=lambda: str(10 + 12 + 8 - 4 - 3 - 2 + 1)),
                 values('In a club of 20, s members swim and r members run; every member does at least one. Give possible '
                        'numbers s and r if exactly 5 do both.', [('s', 'swim s ='), ('r', 'run r =')],
                        's + r - 5 == 20 and s >= 5 and r >= 5 and s <= 20 and r <= 20 and isInteger(s) and isInteger(r)',
                        {'s': 12, 'r': 13}, 'Everyone does at least one, so s + r - 5 = 20, s + r = 25, with each at least 5.',
                        wrong=[{'s': 10, 'r': 10}, {'s': 20, 'r': 10}], search={'s': range(0, 21), 'r': range(0, 21)}),
                 tf('Two sets can have 8 and 6 members and a union of 15 members.', False,
                    'The union has at most 8 + 6 = 14 members.'),
                 sa('Sets A and B are inside a box of 30 things. A has 12 things, B has 9, and A and B share 4. How many things '
                    'are in the box but in neither A nor B?', 'Things:', '13', '30 - (12 + 9 - 4) = 13.',
                    compute=lambda: str(30 - (12 + 9 - 4))),
             ]))


# ------------------------------------------------------------------ Set 31: maps and neighbors
M1 = ["AABBCC", "ADDBEC", "ADFFEC", "GGFHHC", "GIIIHC"]
M2 = ["PPQQ", "PRRQ", "SRTT", "SSTU"]
ADJ1 = figs.map_adjacency(M1)
ADJ2 = figs.map_adjacency(M2)
MAP_RULE = ('Regions are neighbors when they share a border of some length; touching only at a corner point does not count.')


def mapfig(m, labels=None, show=None):
    c = figs.region_map(m, labels=labels, show=show)
    return (c.svg(), 'A map of regions made of grid squares with thick borders between regions, each region labeled.')


def min_colors(adj):
    regs = sorted(adj)
    for k in range(1, 6):
        for col in itertools.product(range(k), repeat=len(regs)):
            c = dict(zip(regs, col))
            if all(c[a] != c[b] for a in regs for b in adj[a]):
                return k


def colorings(adj, colors, fixed):
    regs = sorted(adj)
    out = []
    for col in itertools.product(colors, repeat=len(regs)):
        c = dict(zip(regs, col))
        if all(c[a] != c[b] for a in regs for b in adj[a]) and all(c[k] == v for k, v in fixed.items()):
            out.append(c)
    return out


def two_colorable_without(adj, removed):
    regs = [r for r in adj if r != removed]
    for col in itertools.product((0, 1), repeat=len(regs)):
        c = dict(zip(regs, col))
        if all(c[a] != c[b] for a in regs for b in adj[a] if b != removed):
            return True
    return False


def s31():
    counts1 = {r: len(v) for r, v in ADJ1.items()}
    most = max(counts1, key=counts1.get)
    return S(31, 'Turn a map into a neighbor graph and reason about neighbors and colorings',
             main=[
                 sa(MAP_RULE + ' How many neighbors does region F have?', 'Neighbors:', str(counts1['F']),
                    'F shares borders with B, D, E, G, H and I: 6 neighbors.', fig=mapfig(M1),
                    compute=lambda: str(len(ADJ1['F']))),
                 mc(MAP_RULE + ' Which region has the most neighbors?', most,
                    [('B', 'B has 5 neighbors'), ('D', 'D has 4 neighbors'), ('C', 'C has 3 neighbors')],
                    'Counting each region\'s neighbors: F has 6, more than any other.', fig=mapfig(M1),
                    check=lambda t: t == most),
                 tf(MAP_RULE + ' Regions A and I are neighbors.', False, 'A borders only B, D and G.', fig=mapfig(M1),
                    check=lambda: 'I' in ADJ1['A']),
                 sa(MAP_RULE + ' Each region gets one color and neighbors must get different colors. What is the least number '
                               'of colors needed for this map?', 'Colors:', str(min_colors(ADJ2)),
                    'R, S and T all border each other, so at least 3 colors are needed. Three are enough: P red, Q blue, R '
                    'green, S blue, T red, U blue.', fig=mapfig(M2),
                    compute=lambda: str(min_colors(ADJ2))),
                 grid(MAP_RULE + ' Color each region red, blue or green so that neighbors differ. P is red and Q is blue. Give '
                                 'every region\'s color.', ['P', 'Q', 'R', 'S', 'T', 'U'], ['red', 'blue', 'green'],
                      lambda a: all(a[x] != a[y] for x in ADJ2 for y in ADJ2[x]) and a['P'] == 'red' and a['Q'] == 'blue',
                      'R borders P and Q, so R is green. S borders P and R, so S is blue. T borders Q, R and S, so T is red. U '
                      'borders only T, so U is blue or green; both are accepted.', distinct=False, unique=False,
                      fig=mapfig(M2)),
             ],
             back=[B('Strategy: draw the neighbor graph', 'guided_strategy',
                     'Students miscount neighbors on a busy map. Turning each region into a dot and each shared border into a '
                     'line gives a small graph that is easy to count and color.',
                     lesson=lesson('Draw the neighbor graph',
                                   ['Put one dot for each region.',
                                    'Walk around each region\'s border and draw a line to every region it shares a border '
                                    'with. A corner touch is not a border.',
                                    'The number of lines at a dot is the number of neighbors.',
                                    'To color the map, color the dots so that every line joins two different colors. Start with '
                                    'the region that has the most neighbors.'],
                                   'Worked example (a different map)',
                                   ['Four regions W, X, Y, Z: W borders X and Y; X borders Y and Z; Y borders Z.'],
                                   ['Lines: W-X, W-Y, X-Y, X-Z, Y-Z.',
                                    'W, X, Y all border each other, so they need 3 different colors: W red, X blue, Y green.',
                                    'Z borders X and Y, so Z must be red. Three colors are enough.']),
                     qs=[
                         sa(MAP_RULE + ' How many neighbors does region C have?', 'Neighbors:', str(len(ADJ1['C'])),
                            'C borders B, E and H.', fig=mapfig(M1), compute=lambda: str(len(ADJ1['C']))),
                         tf(MAP_RULE + ' Regions B and D are neighbors.', True, 'They share a border.', fig=mapfig(M1),
                            check=lambda: 'D' in ADJ1['B']),
                         mc('Two regions touch only at a single corner point. Are they neighbors under this rule?', 'No',
                            [('Yes', 'a corner point is not a shared border'), ('Only if they are the same color', 'irrelevant'),
                             ('It depends on their size', 'irrelevant')], 'A border must have length.'),
                         sa(MAP_RULE + ' How many neighbors does region U have?', 'Neighbors:', str(len(ADJ2['U'])),
                            'U borders only T.', fig=mapfig(M2), compute=lambda: str(len(ADJ2['U']))),
                         tf('If three regions all border each other, a coloring with different colors for neighbors needs at '
                            'least 3 colors.', True, 'Each of the three must differ from the other two.'),
                     ])],
             f1=FW('Neighbor counts as clues', 'Harder: reason from neighbor counts and fixed colors.', [
                 sa(MAP_RULE + ' What is the total of the neighbor counts of all nine regions?', 'Total:',
                    str(sum(len(v) for v in ADJ1.values())), 'Each shared border is counted twice (once from each side), so the '
                                                             'total is twice the number of shared borders.', fig=mapfig(M1),
                    compute=lambda: str(sum(len(v) for v in ADJ1.values()))),
                 sa(MAP_RULE + ' How many pairs of regions share a border?', 'Pairs:', str(sum(len(v) for v in ADJ1.values()) // 2),
                    'Half of the total of the neighbor counts.', fig=mapfig(M1),
                    compute=lambda: str(sum(len(v) for v in ADJ1.values()) // 2)),
                 sa(MAP_RULE + ' What is the least number of colors needed so that neighbors differ?', 'Colors:',
                    str(min_colors(ADJ1)), 'B, D and F border each other, so at least 3 colors; a 3-coloring exists (checked '
                                           'over all colorings).', fig=mapfig(M1), compute=lambda: str(min_colors(ADJ1))),
                 tf(MAP_RULE + ' In any coloring of this map with 3 colors where neighbors differ, regions A and F have the same '
                               'color.', all(c['A'] == c['F'] for c in colorings(ADJ1, 'rgb', {})),
                    'A borders B, D and G, and so does F. D borders both B and G. If B and G had different colors, B, D and G '
                    'would use all three colors and A could not be colored. So B and G match, B, D, G use two colors, and A and '
                    'F must both take the third color.',
                    fig=mapfig(M1), check=lambda: all(c['A'] == c['F'] for c in colorings(ADJ1, 'rgb', {}))),
                 mc(MAP_RULE + ' Which ONE region could be removed so that only 2 colors are needed for the rest?', 'R',
                    [('T', 'P, Q and R still border each other'), ('U', 'R, S and T still border each other'),
                     ('S', 'P, Q and R still border each other')],
                    'Every group of three regions that all border each other contains R (P-Q-R, P-R-S, Q-R-T, R-S-T). Without '
                    'R, the rest can alternate: P and T one color, Q, S and U the other.', fig=mapfig(M2),
                    check=lambda t: two_colorable_without(ADJ2, t)),
             ]),
             f2=FW('Colorings: count and prove', 'Expert: count colorings and prove lower bounds.', [
                 sa(MAP_RULE + ' How many ways can the map be colored with red, blue and green so that neighbors differ?',
                    'Colorings:', str(len(colorings(ADJ2, 'rgb', {}))), 'Fix colors for P and Q (6 ways), then the rest follow '
                                                                       'as in the MAIN puzzle with 2 choices for U: 6 x 2 = 12.',
                    fig=mapfig(M2), compute=lambda: str(len(colorings(ADJ2, 'rgb', {})))),
                 tf('Some map drawn on a page needs at least 4 colors so that neighbors differ.', True,
                    'For example, one region surrounded by three regions that all border each other: the four all border each '
                    'other, so they need 4 different colors.'),
                 values('A map has regions in a ring: region 1 borders 2, 2 borders 3, and so on, and the last region borders '
                        'region 1 (and there are no other borders). Give a number of regions n, from 3 to 10, for which 2 '
                        'colors are NOT enough.', [('n', 'n =')], 'isOdd(n) and n >= 3 and n <= 10', {'n': 5},
                        'Going around the ring the colors must alternate, which closes up only when n is even. Any odd n: 3, '
                        '5, 7 or 9.', wrong=[{'n': 4}, {'n': 6}, {'n': 2}], search={'n': range(1, 11)}),
                 sa(MAP_RULE + ' How many ways can this map be colored with red, blue and green so that neighbors differ, if A '
                               'is red?', 'Colorings:', str(len(colorings(ADJ1, 'rgb', {'A': 'r'}))),
                    'Counted by checking all colorings with A red.', fig=mapfig(M1),
                    compute=lambda: str(len(colorings(ADJ1, 'rgb', {'A': 'r'})))),
                 tf('If a map can be colored with 4 colors so that neighbors differ, it can also be colored with 3 colors.', False,
                    'Four regions that all border each other need 4 different colors, so 3 colors are not always enough.'),
             ]))


# ------------------------------------------------------------------ Set 32: categorical arguments
def s32():
    return S(32, 'Test categorical arguments with Venn diagrams, including the existence assumption',
             main=[
                 venn('Premise: "No reptile is warm-blooded." Circle A is reptiles and circle B is warm-blooded animals. Mark '
                      'the region this premise says is EMPTY.', ['reptiles (A)', 'warm-blooded (B)'], lambda a, b: a and b,
                      '"No A is B" means the overlap is empty.'),
                 mc('"All violinists are musicians. All musicians practice. So all violinists practice." Is this valid?',
                    'Yes: every violinist is inside the musicians, who are all inside those who practice.',
                    [('No: some violinists may not practice.', 'the premises rule that out'),
                     ('Yes, but only if every musician is a violinist.', 'not needed'),
                     ('No: the conclusion reverses a premise.', 'it does not')],
                    'Nested circles: violinists inside musicians inside practicers.'),
                 mc('"All squares are rectangles. Some rectangles are not rhombuses. So some squares are not rhombuses." Is this '
                    'valid?', 'No: the rectangles that are not rhombuses may all lie outside the squares.',
                    [('Yes: squares are rectangles, so they share every property.', 'subsets do not share every property'),
                     ('Yes: the conclusion is true.', 'validity is about form; and in fact every square IS a rhombus'),
                     ('No: no rectangle is a square.', 'that is false: every square is a rectangle')],
                    'In fact every square is a rhombus, so the premises are true and the conclusion false: invalid.'),
                 tf('"All A are B. Some C are A. So some C are B." This form is valid.', True,
                    'The C that is an A is inside B, so some C is B.',
                    check=lambda: cat_valid([('all', 'A', 'B'), ('some', 'C', 'A')], ('some', 'C', 'B'))),
                 mc('"All dragons breathe fire. So some dragons breathe fire." When does this follow?',
                    'Only if at least one dragon exists (the existence assumption).',
                    [('Always: "all" includes "some".', 'if there are no dragons, "all dragons breathe fire" is true but '
                                                         '"some dragon breathes fire" is false'),
                     ('Never: the premise is about all dragons.', 'it follows once a dragon exists'),
                     ('Only if dragons are real animals.', 'it is about existence, not about being an animal')],
                    'From "all" to "some" needs at least one member.'),
             ],
             back=[
                 B('Mark statements on a Venn diagram', 'prerequisite', 'Testing an argument means drawing each premise; '
                                                                       'students need to draw "all", "no" and "some".',
                   outcome='LOGIC.SETS.01', qs=[
                       venn('"All A are B." Mark the region that must be EMPTY.', ['A', 'B'], lambda a, b: a and not b,
                            'Nothing in A outside B.'),
                       venn('"No A is B." Mark the region that must be EMPTY.', ['A', 'B'], lambda a, b: a and b, 'The overlap.'),
                       venn('"Some A is B." Mark the region where something must be.', ['A', 'B'], lambda a, b: a and b,
                            'At least one thing in the overlap.'),
                       venn('"Some A is not B." Mark the region where something must be.', ['A', 'B'], lambda a, b: a and not b,
                            'At least one thing in A outside B.'),
                       tf('"All A are B" and "No A is B" can both be true if A has no members.', True,
                          'With A empty, both statements are true (vacuously).'),
                   ]),
                 B('Valid means no counterexample', 'prerequisite', 'A categorical argument is valid when no situation makes '
                                                                   'the premises true and the conclusion false.',
                   outcome='LOGIC.INFERENCE.03', qs=[
                       tf('An argument is valid if a situation exists with true premises and a false conclusion.', False,
                          'Such a situation shows it is invalid.'),
                       mc('"All cats are mammals. All dogs are mammals. So all cats are dogs." Which situation shows it is '
                          'invalid?', 'the real world: cats and dogs are both mammals but cats are not dogs',
                          [('a world with no cats', 'then the conclusion is true'), ('a world where all mammals are dogs', 'then '
                                                                                                                          'cats '
                                                                                                                          'would '
                                                                                                                          'be dogs'),
                           ('a world with no mammals', 'then there are no cats')],
                          'True premises, false conclusion.'),
                       tf('"All A are B. All B are C. So all A are C." is valid.', True, 'Nested sets.',
                          check=lambda: cat_valid([('all', 'A', 'B'), ('all', 'B', 'C')], ('all', 'A', 'C'))),
                       tf('"Some A are B. Some B are C. So some A are C." is valid.', False, 'The A-and-B things and the B-and-C '
                                                                                           'things may be different.',
                          check=lambda: cat_valid([('some', 'A', 'B'), ('some', 'B', 'C')], ('some', 'A', 'C'))),
                       mc('Which premise pair makes "So no A is C" follow?', '"All A are B." and "No B is C."',
                          [('"Some A are B." and "No B is C."', 'only some A are known to be outside C'),
                           ('"All A are B." and "Some B are not C."', 'A may still overlap C'),
                           ('"No A is B." and "No B is C."', 'A and C may overlap outside B')],
                          'A inside B, and B outside C, so A is outside C.'),
                   ]),
             ],
             f1=FW('Harder categorical forms', 'Harder: "some ... not", three terms and hidden reversals.', [
                 tf('"No A is B. All C are B. So no C is A." This form is valid.', True, 'C lies inside B and B is outside A.',
                    check=lambda: cat_valid([('no', 'A', 'B'), ('all', 'C', 'B')], ('no', 'C', 'A'))),
                 tf('"All A are B. No C is A. So no C is B." This form is valid.', False, 'C can overlap the part of B outside A.',
                    check=lambda: cat_valid([('all', 'A', 'B'), ('no', 'C', 'A')], ('no', 'C', 'B'))),
                 mc('"Some athletes are vegetarians. All vegetarians eat beans. So ..." Which conclusion follows?',
                    'some athletes eat beans', [('all athletes eat beans', 'only some are known to be vegetarians'),
                                                ('all bean eaters are athletes', 'reverses the relations'),
                                                ('no athlete eats meat', 'not supported')],
                    'The athletes who are vegetarians eat beans.'),
                 venn('Premises: "All A are B" and "No B is C". On a three-circle diagram (A, B, C), mark every region that the '
                      'premises make EMPTY.', ['A', 'B', 'C'], lambda a, b, c: (a and not b) or (b and c),
                      '"All A are B" empties A outside B; "No B is C" empties B inside C.'),
                 tf('"All A are B. Some A are C. So some B are C." This form is valid.', True,
                    'The A that is C is also B.', check=lambda: cat_valid([('all', 'A', 'B'), ('some', 'A', 'C')], ('some', 'B', 'C'))),
             ]),
             f2=FW('Existence and hidden assumptions', 'Expert: arguments that need the existence assumption.', [
                 tf('"All A are B. All A are C. So some B are C." This form is valid without any existence assumption.', False,
                    'If A is empty, both premises are true and B and C may not overlap.',
                    check=lambda: cat_valid([('all', 'A', 'B'), ('all', 'A', 'C')], ('some', 'B', 'C'))),
                 mc('Which added premise makes "All A are B. All A are C. So some B are C." valid?', 'At least one A exists.',
                    [('At least one B exists.', 'B may exist outside C'), ('At least one C exists.', 'C may exist outside B'),
                     ('All B are A.', 'still fails if A is empty')],
                    'An A would be both B and C.'),
                 sa('How many of these forms are valid (with no existence assumption)? (1) All A are B; all B are C; so all A are '
                    'C. (2) No A is B; all C are A; so no C is B. (3) All A are B; some C are not B; so some C are not A. (4) '
                    'Some A are B; all B are C; so some A are C.', 'Valid forms:', '4',
                    'All four are valid: (1) nesting; (2) C inside A, A outside B; (3) a C outside B cannot be in A; (4) the A '
                    'that is B is also C.',
                    compute=lambda: str(sum(cat_valid(p, c) for p, c in [
                        ([('all', 'A', 'B'), ('all', 'B', 'C')], ('all', 'A', 'C')),
                        ([('no', 'A', 'B'), ('all', 'C', 'A')], ('no', 'C', 'B')),
                        ([('all', 'A', 'B'), ('somenot', 'C', 'B')], ('somenot', 'C', 'A')),
                        ([('some', 'A', 'B'), ('all', 'B', 'C')], ('some', 'A', 'C'))]))),
                 tf('"All unicorns have one horn" is true if no unicorns exist.', True, 'An "all" statement about an empty set is '
                                                                                        'vacuously true.'),
                 mc('"No square is a circle. Some circles are shaded. So some shaded things are not squares." Is it valid?',
                    'Yes: a shaded circle is not a square.', [('No: shaded things may all be squares.', 'the shaded circles '
                                                                                                        'are not squares'),
                                                              ('No: it needs squares to exist.', 'it does not'),
                                                              ('Yes, but only if all circles are shaded.', 'not needed')],
                    'The shaded circle is a witness.'),
             ]))


REG8 = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
TERM = {'A': 0, 'B': 1, 'C': 2}


def holds(st, model):
    """st = (form, X, Y) with form all / no / some / somenot; model = which of the 8 regions are non-empty."""
    form, x, y = st
    X, Y = TERM[x], TERM[y]
    full = [r for r, on in zip(REG8, model) if on]
    if form == 'all':
        return not any(r[X] and not r[Y] for r in full)
    if form == 'no':
        return not any(r[X] and r[Y] for r in full)
    if form == 'some':
        return any(r[X] and r[Y] for r in full)
    return any(r[X] and not r[Y] for r in full)


def cat_valid(premises, conclusion):
    """Valid when every pattern of empty and non-empty regions that makes the premises true makes the conclusion true."""
    return all(holds(conclusion, m) for m in itertools.product((0, 1), repeat=8) if all(holds(p, m) for p in premises))


SETS = [s29(), s30(), s31(), s32()]
