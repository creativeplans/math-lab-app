"""Logic sets 37-40: direct proof; tiling and covering; justifying equation steps; proof by contradiction."""
import itertools
from fractions import Fraction
from lq import S, B, FW, mc, figmc, tf, sa, order, values, lesson
import figs

EVEN = ('Definitions: an integer n is even if n = 2k for some integer k, and odd if n = 2k + 1 for some integer k. '
        'An integer n is a multiple of m if n = mk for some integer k.')


def steps_in_order(keys):
    return lambda p: list(p) == list(keys)


# ------------------------------------------------------------------ Set 37: direct proof with numbers
def s37():
    return S(37, 'Build a direct argument about even, odd and multiples from definitions',
             main=[
                 order(EVEN + ' Put the steps of a direct proof that the sum of two odd integers is even in order.',
                       [('A', 'Let m = 2a + 1 and n = 2b + 1, where a and b are integers.'),
                        ('B', 'Then m + n = 2a + 2b + 2.'), ('C', 'So m + n = 2(a + b + 1).'),
                        ('D', 'Since a + b + 1 is an integer, m + n is even.')], steps_in_order('ABCD'),
                       'Start from the definitions, add, factor out 2, then name the integer that shows the sum is even.',
                       expect=list('ABCD'), unique=True),
                 mc(EVEN + ' Which first line correctly begins a direct proof that the product of any two odd integers is '
                           'odd?', 'Let m = 2a + 1 and n = 2b + 1, where a and b are integers.',
                    [('Let m = 2a + 1 and n = 2a + 1, where a is an integer.',
                      'using the same a makes m and n equal, so it proves the claim only for a number times itself'),
                     ('Let m = 3 and n = 5.', 'one example cannot prove a claim about all odd integers'),
                     ('Assume that m times n is odd.', 'that assumes the conclusion the proof must reach')],
                    'Two general odd integers need two separate integers a and b.'),
                 mc(EVEN + ' A proof that an even integer plus an odd integer is odd reaches the line m + n = 2a + 2b + 1. '
                           'Which line correctly finishes it?',
                    'm + n = 2(a + b) + 1, and a + b is an integer, so m + n is odd.',
                    [('m + n is odd because the expression 2a + 2b + 1 contains a 1.',
                      'containing a 1 is not the definition of odd'),
                     ('Since 4 + 3 = 7 is odd, m + n is odd.', 'an example does not finish a general proof'),
                     ('m + n = 2(a + b + 1), so m + n is even.', '2a + 2b + 1 is not equal to 2(a + b + 1)')],
                    'The definition of odd needs the form 2(integer) + 1.'),
                 tf(EVEN + ' Checking that 3 + 5, 7 + 9 and 11 + 13 are all even proves that the sum of any two odd '
                           'integers is even.', False,
                    'Examples can support a guess but cannot prove a claim about infinitely many integers. A proof must '
                    'use general odd integers 2a + 1 and 2b + 1.'),
                 values(EVEN + ' To show that 6n + 4 is even for every integer n, write 6n + 4 = 2(pn + q). Give the '
                               'numbers p and q.', [('p', 'p ='), ('q', 'q =')], 'p == 3 and q == 2', {'p': 3, 'q': 2},
                        '6n + 4 = 2(3n + 2), and 3n + 2 is an integer, so 6n + 4 is even.',
                        wrong=[{'p': 6, 'q': 4}, {'p': 3, 'q': 4}, {'p': 2, 'q': 3}]),
             ],
             back=[B('Use the definitions of even and odd', 'prerequisite',
                     'A direct proof starts from the definitions. Students who cannot write even and odd numbers in the '
                     'forms 2k and 2k + 1 cannot begin.',
                     qs=[
                         mc(EVEN + ' Which expression is odd for every integer k?', '2k + 7',
                            [('2k + 4', '2k + 4 = 2(k + 2), which is even'), ('4k', '4k = 2(2k), which is even'),
                             ('k + 1', 'k + 1 is odd only when k is even')],
                            '2k + 7 = 2(k + 3) + 1, which has the odd form.'),
                         tf(EVEN + ' 2k + 6 is even for every integer k.', True, '2k + 6 = 2(k + 3).'),
                         sa(EVEN + ' Write 19 in the form 2k + 1. What is k?', 'k =', '9', '19 = 2(9) + 1.',
                            compute=lambda: str((19 - 1) // 2)),
                         tf(EVEN + ' If n = 2k + 1, then n + 1 is odd.', False, 'n + 1 = 2k + 2 = 2(k + 1), which is even.'),
                         mc('Which statement is the definition of an even integer?', 'n = 2k for some integer k',
                            [('n ends in the digit 0', 'that describes multiples of 10; 4 is even but ends in 4'),
                             ('n = 2k + 1 for some integer k', 'that is the definition of odd'),
                             ('n leaves remainder 1 when divided by 2', 'that also describes odd numbers')],
                            'Even means 2 times some integer.'),
                     ])],
             f1=FW('Direct proofs about multiples', 'Harder: direct proofs about multiples of 3 and 9.', [
                 order(EVEN + ' Put the steps of a direct proof that if n is a multiple of 3, then n squared is a multiple '
                              'of 9 in a correct order. (Two orders are correct.)',
                       [('A', 'Let n = 3k, where k is an integer.'), ('B', 'Then n squared = 9k squared.'),
                        ('C', 'k squared is an integer, because k is an integer.'),
                        ('D', 'So n squared is 9 times an integer, a multiple of 9.')],
                       lambda p: p[0] == 'A' and p[-1] == 'D',
                       'Begin with the definition (A) and end with the conclusion (D). B and C can come in either order.',
                       expect=list('ABCD')),
                 mc(EVEN + ' Which is a correct direct proof that the sum of three consecutive integers is a multiple of 3?',
                    'n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1), and n + 1 is an integer.',
                    [('1 + 2 + 3 = 6, and 6 is a multiple of 3.', 'one example does not prove the general claim'),
                     ('n + n + n = 3n, which is a multiple of 3.', 'n, n, n are not consecutive integers'),
                     ('n + (n + 1) + (n + 2) = 3n + 3, which is odd.', '3n + 3 is not always odd, and odd is not the claim')],
                    'Write three general consecutive integers, add, and factor out 3.'),
                 tf(EVEN + ' If n is odd, then n squared minus 1 is a multiple of 8.', True,
                    'n = 2k + 1 gives n squared - 1 = 4k(k + 1). One of k and k + 1 is even, so k(k + 1) = 2j and the '
                    'expression is 8j.', check=lambda: all((n * n - 1) % 8 == 0 for n in range(-99, 100, 2))),
                 values(EVEN + ' (2a + 1)(2b + 1) = 2(2ab + a + b) + 1. For a = 3 and b = 4, what number is 2ab + a + b?',
                        [('x', 'Number =')], 'x == 31', {'x': 31},
                        '2(3)(4) + 3 + 4 = 31. Check: 7 x 9 = 63 = 2(31) + 1.', wrong=[{'x': 63}, {'x': 24}, {'x': 32}]),
                 mc(EVEN + ' A student proves that every multiple of 4 is even by writing n = 4k = 2(2k). What justifies '
                           'the last sentence, "so n is even"?', '2k is an integer, so n is 2 times an integer.',
                    [('4 is an even number.', 'that alone does not put n in the form 2 times an integer'),
                     ('n can be any number at all.', 'the claim is about multiples of 4 only'),
                     ('k must be an even number.', 'k can be any integer; nothing makes it even')],
                    'The definition needs n = 2 times an integer, and 2k is an integer.'),
             ]),
             f2=FW('Judge and complete direct proofs', 'Expert: find the flaw in a proof, and prove remainder facts.', [
                 order(EVEN + ' Put the steps of a direct proof that the square of an odd integer leaves remainder 1 when '
                              'divided by 4 in order.',
                       [('A', 'Let n = 2k + 1, where k is an integer.'), ('B', 'Then n squared = 4k squared + 4k + 1.'),
                        ('C', 'So n squared = 4(k squared + k) + 1.'),
                        ('D', 'Since k squared + k is an integer, n squared leaves remainder 1 when divided by 4.')],
                       steps_in_order('ABCD'), 'Definition, expand, factor out 4, then name the integer.',
                       expect=list('ABCD'), unique=True),
                 mc(EVEN + ' Claim: the sum of two even integers is a multiple of 4. "Proof: Let m = 2k and n = 2k. Then '
                           'm + n = 4k." What is wrong?',
                    'It uses the same k for both, so it only covers the case m = n.',
                    [('It should have started with m = 4k.', 'the given numbers are only known to be even'),
                     ('Nothing is wrong; the proof is correct.', '2 + 4 = 6 is not a multiple of 4, so the claim is false'),
                     ('It should check an example before starting.', 'checking examples is not the flaw')],
                    'With separate integers, m + n = 2(a + b), which is a multiple of 4 only when a + b is even. 2 + 4 = 6 '
                    'shows the claim is false.'),
                 tf(EVEN + ' The statement "n squared + n is even for every integer n" can be proved by two cases: n even '
                           'and n odd.', True,
                    'If n = 2k, n squared + n = 2(2k squared + k). If n = 2k + 1, n squared + n = (2k + 1)(2k + 2) = '
                    '2(2k + 1)(k + 1). Both are even.', check=lambda: all((n * n + n) % 2 == 0 for n in range(-50, 51))),
                 sa(EVEN + ' For odd n = 2k + 1, n squared + 4n + 3 = 2(2k squared + 6k + 4). For k = 5, what number is '
                           '2k squared + 6k + 4?', 'Number:', '84',
                    '2(25) + 30 + 4 = 84. Check: n = 11 gives 121 + 44 + 3 = 168 = 2 x 84.',
                    compute=lambda: str((11 * 11 + 44 + 3) // 2)),
                 values(EVEN + ' Give an integer n from 1 to 20 for which n squared + n + 1 is even. If no such n exists, '
                               'enter 0.', [('n', 'n =')], 'n == 0', {'n': 0},
                        'n squared + n = n(n + 1) is always even, so n squared + n + 1 is always odd. No such n exists.',
                        wrong=[{'n': 1}, {'n': 2}, {'n': 7}]),
             ]))


# ------------------------------------------------------------------ Set 38: tiling and covering
DOM = [((0, 0), (0, 1)), ((0, 0), (1, 0))]
STR3 = [((0, 0), (0, 1), (0, 2)), ((0, 0), (1, 0), (2, 0))]
LTRO = [((0, 0), (1, 0), (1, 1)), ((0, 0), (0, 1), (1, 0)), ((0, 0), (0, 1), (1, 1)), ((0, 1), (1, 0), (1, 1))]


def tilings(region, pieces):
    """Count exact covers of a set of cells by the given piece shapes (every orientation listed)."""
    def go(left):
        if not left:
            return 1
        r, c = min(left)
        total = 0
        for p in pieces:
            for ar, ac in p:
                cells = frozenset((r + dr - ar, c + dc - ac) for dr, dc in p)
                if cells <= left:
                    total += go(left - cells)
        return total
    return go(frozenset(region))


def rect(n, m):
    return {(r, c) for r in range(n) for c in range(m)}


def shape(rows):
    return {(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == '#'}


def board_fig(cells, n, m, desc, removed=()):
    c = figs.cells_canvas(set(cells), n, m, cell=30, fill='white', mark={rc: 'X' for rc in removed})
    return (c.svg(), desc)


REGIONS = {'A': shape(['.#..', '###.', '.#..', '.###']), 'B': shape(['#...', '###.', '.#..', '.###']),
           'C': shape(['###.', '.#..', '.##.', '..##']), 'D': shape(['..#.', '.##.', '####', '..#.'])}
TILE_RULE = ('A domino covers exactly two squares that share a side. A tiling covers every square of the region exactly '
             'once, with no domino hanging off the region.')


def s38():
    region_fig = (figs.panels([figs.cells_canvas(REGIONS[k], 4, 4, cell=26, grid=False) for k in 'ABCD']).svg(),
                  'Four shaded regions labeled A to D, each made of 8 grid squares.')
    r5 = rect(5, 5)
    return S(38, 'Decide which pieces cover a region exactly, and prove when no covering exists',
             main=[
                 sa(TILE_RULE + ' In how many different ways can a rectangle 2 squares tall and 4 squares wide be tiled '
                                'with dominoes?', 'Ways:', str(tilings(rect(2, 4), DOM)),
                    'Look at the left end: one upright domino leaves a 2 by 3 (3 ways), or two flat dominoes leave a 2 by 2 '
                    '(2 ways): 3 + 2 = 5.', compute=lambda: str(tilings(rect(2, 4), DOM)),
                    fig=board_fig(rect(2, 4), 2, 4, 'An empty grid 2 squares tall and 4 squares wide.')),
                 tf(TILE_RULE + ' The 3 by 3 board with its center square removed (shown) can be tiled by 4 dominoes.', True,
                    'The 8 remaining squares form a ring; going around it, pair the squares two at a time.',
                    check=lambda: tilings(rect(3, 3) - {(1, 1)}, DOM) > 0,
                    fig=board_fig(rect(3, 3) - {(1, 1)}, 3, 3, 'A 3 by 3 grid with the center square marked X (removed).',
                                  removed=[(1, 1)])),
                 figmc(TILE_RULE + ' Which region can be tiled by 4 dominoes?', 4, 'B',
                       {'A': 'color it like a checkerboard: 5 squares of one color and 3 of the other, but every domino '
                             'covers one of each',
                        'C': 'color it like a checkerboard: 5 squares of one color and 3 of the other',
                        'D': 'the right end of the long row and the square below the row each touch only one square, the '
                             'same one, so both cannot be covered'},
                       'Region B: the top-left square must pair with the square below it, and the rest then pairs off in '
                       'one way.', region_fig, check=lambda L: tilings(REGIONS[L], DOM) > 0),
                 values(TILE_RULE + ' One square is removed from a 5 by 5 board, and the other 24 squares are to be tiled by '
                                    '12 dominoes. Rows and columns are numbered 1 to 5. Give the row r and column c of a '
                                    'square whose removal makes a tiling possible.', [('r', 'Row r ='), ('c', 'Column c =')],
                        'isInteger(r) and isInteger(c) and r >= 1 and r <= 5 and c >= 1 and c <= 5 and isEven(r + c)',
                        {'r': 1, 'c': 1},
                        'Color the board like a checkerboard with the corners dark: 13 dark, 12 light. A tiling needs 12 of '
                        'each, so the removed square must be dark (r + c even). Every dark square works; a computer search '
                        'of all 25 removals confirms it.', wrong=[{'r': 1, 'c': 2}, {'r': 2, 'c': 3}, {'r': 6, 'c': 2}],
                        search={'r': range(1, 6), 'c': range(1, 6)},
                        method='Tilings counted for every one of the 25 removals: exactly the 13 squares with r + c even '
                               'leave a tileable board.' if all((tilings(r5 - {(r, c)}, DOM) > 0) == ((r + c) % 2 == 0)
                                                               for r, c in r5) else 'MISMATCH'),
                 sa('An L-tromino is three squares in an L shape (a 2 by 2 square with one square missing). It may be '
                    'turned any way. In how many ways can a rectangle 2 squares tall and 3 wide be tiled by two L-trominoes?',
                    'Ways:', str(tilings(rect(2, 3), LTRO)),
                    'One L must cover the top-left square. Of its placements, only two leave an L-shaped gap; each gives one '
                    'tiling.', compute=lambda: str(tilings(rect(2, 3), LTRO))),
             ],
             back=[B('Strategy: color the board like a checkerboard', 'guided_strategy',
                     'Students try placements forever on a region that cannot be tiled. Counting colors can prove '
                     'impossibility at once, and shows when a search is still needed.',
                     lesson=lesson('Color the board like a checkerboard',
                                   ['Color the squares in a checkerboard pattern: squares that share a side get different '
                                    'colors.',
                                    'Every domino covers one dark and one light square. So a region can be tiled only if it '
                                    'has equally many dark and light squares.',
                                    'Equal counts do not guarantee a tiling. Then look for a square with only one neighbor: '
                                    'its domino is forced.'],
                                   'Worked example (a different region)',
                                   ['A T shape: three squares in a row, plus one square below the middle one. Can it be '
                                    'tiled by 2 dominoes?'],
                                   ['Colors: the middle square is dark; the two ends and the square below are light. That '
                                    'is 1 dark and 3 light.',
                                    'Each domino needs one dark square, so at most one domino fits. No tiling exists.']),
                     qs=[
                         sa('A 4 by 4 board is colored like a checkerboard. How many of its squares are dark?', 'Dark:', '8',
                            'Each row has 2 dark and 2 light squares: 4 x 2 = 8.',
                            compute=lambda: str(sum((r + c) % 2 == 0 for r, c in rect(4, 4)))),
                         tf('Every domino placed on a checkerboard covers one dark square and one light square.', True,
                            'The two squares share a side, and squares sharing a side have different colors.'),
                         sa(TILE_RULE + ' A region has 7 dark and 5 light squares on a checkerboard coloring. According to '
                                        'the color count, what is the greatest number of dominoes that could be placed on '
                                        'it without overlapping?', 'Dominoes:', '5',
                            'Each domino uses one light square, and there are only 5.', compute=lambda: str(min(7, 5))),
                         mc(TILE_RULE + ' A region has 6 dark and 6 light squares. What does the color count tell you?',
                            'It does not rule out a tiling; you still have to find one or show none exists.',
                            [('It can certainly be tiled by 6 dominoes.', 'equal colors are needed, but they are not enough'),
                             ('It cannot be tiled by dominoes.', 'equal colors do not rule out a tiling'),
                             ('It can be tiled in exactly 6 ways.', 'the color count says nothing about the number of ways')],
                            'Equal counts pass the test, but a region such as region D in this set can still fail.'),
                         tf(TILE_RULE + ' A region with an even number of squares can always be tiled by dominoes.', False,
                            'The T shape in the worked example has 4 squares and cannot be tiled.'),
                     ])],
             f1=FW('Count tilings and use other pieces', 'Harder: longer strips and three-square pieces.', [
                 sa(TILE_RULE + ' In how many ways can a strip 2 squares tall and 6 squares wide be tiled by dominoes?',
                    'Ways:', str(tilings(rect(2, 6), DOM)),
                    'Let w(n) be the number for width n. The left end is one upright domino (leaving width n - 1) or two flat '
                    'ones (leaving n - 2): w(n) = w(n - 1) + w(n - 2). 1, 2, 3, 5, 8, 13.',
                    compute=lambda: str(tilings(rect(2, 6), DOM))),
                 tf('A straight tromino covers three squares in a row. A 3 by 3 square can be tiled by three straight '
                    'trominoes in exactly 2 ways.', True,
                    'If the top-left tromino lies flat, the top row is filled and so are the other rows: all flat. If it '
                    'stands upright, all must stand. 2 ways.', check=lambda: tilings(rect(3, 3), STR3) == 2),
                 mc('A straight tromino covers three squares in a row, flat or upright. One corner square is removed from a '
                    '4 by 4 board. Can the other 15 squares be tiled by 5 straight trominoes?',
                    'Yes, and there is more than one way.',
                    [('No: 15 squares cannot be split into trominoes.', '15 = 5 x 3, so the count is fine'),
                     ('No: the corner gap blocks every tiling.', 'tilings exist; the search finds 4'),
                     ('Yes, but in exactly one way.', 'a search finds 4 different tilings')],
                    'For example, the row with the gap holds one flat tromino in its other three squares, and the remaining '
                    '3 by 4 block can be filled with upright trominoes. A full search finds 4 tilings.',
                    check=lambda t: t.startswith('Yes, and') == (tilings(rect(4, 4) - {(0, 0)}, STR3) > 1)
                    and t.startswith('Yes, and')),
                 sa('A straight tromino covers three squares in a row, flat or upright. In how many ways can a rectangle 3 '
                    'squares tall and 4 wide be tiled by straight trominoes?', 'Ways:', str(tilings(rect(3, 4), STR3)),
                    'All flat does not fit (rows of 4). Each column can hold an upright tromino; a flat block of three flat '
                    'trominoes fills 3 by 3. Upright x 4; flat block then upright; upright then flat block: 3.',
                    compute=lambda: str(tilings(rect(3, 4), STR3))),
                 values(TILE_RULE + ' A strip 2 squares tall and n squares wide can be tiled by dominoes in exactly 8 ways. '
                                    'What is n?', [('n', 'n =')], 'n == 5', {'n': 5},
                        'The counts for widths 1, 2, 3, 4, 5 are 1, 2, 3, 5, 8.', wrong=[{'n': 4}, {'n': 8}, {'n': 6}],
                        method='Counts by width: %s.' % [tilings(rect(2, w), DOM) for w in range(1, 7)]),
             ]),
             f2=FW('Prove impossibility and count harder tilings', 'Expert: color arguments and larger counts.', [
                 sa(TILE_RULE + ' In how many ways can a rectangle 3 squares tall and 4 wide be tiled by dominoes?', 'Ways:',
                    str(tilings(rect(3, 4), DOM)), 'An organized search by the placement covering the top-left square, '
                                                   'then the next uncovered square, finds 11 tilings.',
                    compute=lambda: str(tilings(rect(3, 4), DOM))),
                 tf(TILE_RULE + ' A board 4 rows by 5 columns has two squares removed: row 1, column 1 and row 3, column 3. '
                                'The other 18 squares can be tiled by 9 dominoes.', False,
                    'Both removed squares have the same checkerboard color (1 + 1 and 3 + 3 are even). That leaves 8 of '
                    'that color and 10 of the other, so no tiling exists.',
                    check=lambda: tilings(rect(4, 5) - {(0, 0), (2, 2)}, DOM) > 0),
                 mc('An L-tromino is three squares in an L shape, turned any way. In how many ways can a strip 2 squares '
                    'tall and 9 wide be tiled by L-trominoes?', str(tilings(rect(2, 9), LTRO)),
                    [('6', 'the strip splits into three 2 by 3 blocks with 2 choices each, so multiply, not add'),
                     ('3', 'that counts the blocks, not the ways'),
                     ('9', 'that is the width, not a count of tilings')],
                    'The leftmost L-tromino and its partner always fill a 2 by 3 block, which has 2 tilings. Three blocks: '
                    '2 x 2 x 2 = 8.', check=lambda t: int(t) == tilings(rect(2, 9), LTRO)),
                 values(TILE_RULE + ' One square is removed from a 3 by 3 board. Rows and columns are numbered 1 to 3. Give a '
                                    'square (row r, column c) whose removal leaves 8 squares that can be tiled by dominoes.',
                        [('r', 'Row r ='), ('c', 'Column c =')],
                        'isInteger(r) and isInteger(c) and r >= 1 and r <= 3 and c >= 1 and c <= 3 and isEven(r + c)',
                        {'r': 2, 'c': 2},
                        'The corners and the center are the majority color (5 of 9). Removing one of them leaves 4 of each, '
                        'and each such board can be tiled.', wrong=[{'r': 1, 'c': 2}, {'r': 2, 'c': 3}],
                        search={'r': range(1, 4), 'c': range(1, 4)},
                        method='Tilings counted for all 9 removals; the 5 with r + c even work.'
                        if [(r + 1, c + 1) for r, c in sorted(rect(3, 3)) if tilings(rect(3, 3) - {(r, c)}, DOM)]
                        == [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)] else 'MISMATCH'),
                 sa(TILE_RULE + ' One square is removed from a board 3 rows by 5 columns. For how many of the 15 squares does '
                                'removing it leave 14 squares that can be tiled by dominoes?', 'Squares:',
                    str(sum(1 for rc in rect(3, 5) if tilings(rect(3, 5) - {rc}, DOM))),
                    'The 8 squares of the majority color (row + column even) are the only candidates, and a search shows '
                    'each of them works.', compute=lambda: str(sum(1 for rc in rect(3, 5) if tilings(rect(3, 5) - {rc}, DOM)))),
             ]))


# ------------------------------------------------------------------ Set 39: justify each step of solving an equation
EQ = ('Assume the equation has a solution x. Each new line must follow from the equality in the line before it.')


def s39():
    return S(39, 'Explain each step in solving an equation and justify the solution method',
             main=[
                 order(EQ + ' Put the steps for solving 4x + 7 = 2x + 19 in order.',
                       [('A', '2x + 7 = 19   (subtract 2x from both sides)'), ('B', '2x = 12   (subtract 7 from both sides)'),
                        ('C', 'x = 6   (divide both sides by 2)'), ('D', 'Check: 4(6) + 7 = 31 and 2(6) + 19 = 31')],
                       steps_in_order('ABCD'),
                       'Each line uses the line before it; the check comes last, once x is known.', expect=list('ABCD'),
                       unique=True),
                 mc(EQ + ' Which reason justifies going from 5x - 4 = 21 to 5x = 25?',
                    'Add 4 to both sides; equal numbers plus 4 are still equal.',
                    [('Use the distributive property on 5x - 4.', 'nothing is distributed in this step'),
                     ('Multiply both sides by 4.', 'multiplying by 4 would give 20x - 16 = 84'),
                     ('Rewrite 5x - 4 as 4 - 5x.', 'subtraction cannot be reordered that way, and the step does not do it')],
                    'Adding the same number to two equal numbers gives equal results: 21 + 4 = 25.'),
                 mc(EQ + ' A student writes: Line 1: 2(x + 3) = 14. Line 2: 2x + 3 = 14. Line 3: 2x = 11. Line 4: x = 5.5. '
                         'Which line is the first one that does NOT follow from the line before it?', 'Line 2',
                    [('Line 3', 'from Line 2, subtracting 3 does give 2x = 11'),
                     ('Line 4', 'from Line 3, dividing by 2 does give x = 5.5'),
                     ('None; every line follows', 'Line 2 is wrong, and x = 5.5 does not check: 2(8.5) = 17')],
                    '2(x + 3) = 2x + 6, not 2x + 3. The correct steps give 2x = 8 and x = 4.'),
                 tf(EQ + ' From 6 - x = 10, the next line "x = 10 - 6" follows correctly.', False,
                    'Subtracting 6 gives -x = 4, so x = -4. The line x = 4 does not follow; 6 - 4 = 2, not 10.'),
                 values(EQ + ' Solve 7 - 2(x - 1) = x - 3. Give x.', [('x', 'x =')], 'x == 4', {'x': 4},
                        '7 - 2x + 2 = x - 3 (distribute), 9 - 2x = x - 3 (combine), 12 = 3x (add 2x and 3), x = 4 (divide '
                        'by 3). Check: 7 - 2(3) = 1 and 4 - 3 = 1.', wrong=[{'x': 2}, {'x': -4}, {'x': 6}]),
             ],
             back=[B('Properties of equality', 'prerequisite',
                     'Each step of solving an equation is justified by a property of equality or of operations. Students '
                     'who cannot name them cannot justify a step.',
                     qs=[
                         mc('If a = b, which statement must also be true?', 'a - 5 = b - 5',
                            [('a - 5 = b + 5', 'different amounts were changed on the two sides'),
                             ('5a = b', 'only one side was multiplied'),
                             ('a / 5 = b / 3', 'the two sides were divided by different numbers')],
                            'Doing the same thing to two equal numbers keeps them equal.'),
                         tf('If 3x = 12, then x = 4 follows by dividing both sides by 3.', True, '12 / 3 = 4.'),
                         mc('Which step uses the distributive property?', '5(x - 2) = 13 becomes 5x - 10 = 13',
                            [('x + 3 = 8 becomes x = 5', 'that subtracts 3 from both sides'),
                             ('4x = 20 becomes x = 5', 'that divides both sides by 4'),
                             ('x + 2 = 9 becomes 2 + x = 9', 'that uses the commutative property')],
                            'The distributive property rewrites 5(x - 2) as 5x - 10.'),
                         tf('Multiplying both sides of an equation by 0 always gives an equation with the same solutions.',
                            False, 'It gives 0 = 0, which every number satisfies, so solutions can be gained.'),
                         sa('To solve x / 4 = 9 in one step, by what number do you multiply both sides?', 'Number:', '4',
                            'Multiplying both sides by 4 gives x = 36.', compute=lambda: str(4)),
                     ])],
             f1=FW('Steps that need care', 'Harder: dividing by a variable, no solution, every number a solution.', [
                 mc(EQ + ' A student solves x squared = 5x by dividing both sides by x and gets x = 5. What is wrong?',
                    'Dividing by x assumes x is not 0, and x = 0 is also a solution.',
                    [('Nothing; x = 5 is the only solution.', 'x = 0 also works: 0 = 0'),
                     ('The answer should be x = 0 only.', 'x = 5 also works: 25 = 25'),
                     ('x squared = 5x has no solutions.', 'both 0 and 5 are solutions')],
                    'x squared - 5x = 0 gives x(x - 5) = 0, so x = 0 or x = 5.'),
                 tf('The equation 3(x + 2) = 3x + 6 is true for every number x.', True,
                    'By the distributive property, 3(x + 2) and 3x + 6 are the same expression.',
                    check=lambda: all(3 * (x + 2) == 3 * x + 6 for x in range(-20, 21))),
                 sa(EQ + ' Solve 2(x - 4) + 3 = 5x + 7. What is x?', 'x =', '-4',
                    '2x - 8 + 3 = 5x + 7, so 2x - 5 = 5x + 7, so -12 = 3x, so x = -4. Check: 2(-8) + 3 = -13 and '
                    '5(-4) + 7 = -13.', compute=lambda: str(Fraction(-8 + 3 - 7, 5 - 2))),
                 mc(EQ + ' Solving 4x + 1 = 4x - 3 leads to the line 1 = -3. What does this show?',
                    'The equation has no solution.',
                    [('The solution is x = 0.', 'x = 0 gives 1 = -3, which is false'),
                     ('Every number is a solution.', 'that would be shown by a true line such as 1 = 1'),
                     ('The solution is x = -3.', 'x = -3 gives -11 = -15, which is false')],
                    'If some x solved it, then 1 = -3 would follow, which is false. So no x solves it.'),
                 order(EQ + ' Put the lines of this solution of (x + 5) / 3 = 4 in order.',
                       [('A', 'Assume x is a number with (x + 5) / 3 = 4.'),
                        ('B', 'x + 5 = 12   (multiply both sides by 3)'), ('C', 'x = 7   (subtract 5 from both sides)'),
                        ('D', 'Check: (7 + 5) / 3 = 4')], steps_in_order('ABCD'),
                       'Start from the assumption that a solution exists, then undo the division, then the addition, then '
                       'check.', expect=list('ABCD'), unique=True),
             ]),
             f2=FW('Justify a solution method', 'Expert: steps that are not reversible, and why checking matters.', [
                 mc(EQ + ' To solve the equation (square root of (x + 2)) = x, a student squares both sides: x + 2 = x '
                         'squared, so x = 2 or x = -1. Which answer is correct?',
                    'Only x = 2; x = -1 gives square root of 1 = 1, not -1.',
                    [('Both x = 2 and x = -1.', 'x = -1 fails the original equation'),
                     ('Only x = -1.', 'x = -1 fails and x = 2 works: square root of 4 = 2'),
                     ('Neither one.', 'x = 2 works: square root of 4 = 2')],
                    'Squaring both sides can add solutions, so each candidate must be checked in the original equation.'),
                 tf(EQ + ' If each line of a solution follows from the line before it, then every number found at the end '
                         'must solve the original equation.', False,
                    'The steps show that any solution is among the numbers found, not that each number found works. '
                    'Squaring, for example, can add a number that fails the original equation.'),
                 values(EQ + ' Solve 3(2x - 1) = 4(x + 2) - 1. Give x.', [('x', 'x =')], 'x == 5', {'x': 5},
                        '6x - 3 = 4x + 7, so 2x = 10, so x = 5. Check: 3(9) = 27 and 4(7) - 1 = 27.',
                        wrong=[{'x': 3}, {'x': 2}, {'x': -5}]),
                 mc('Which step can give an equation with MORE solutions than the one before it?', 'Squaring both sides',
                    [('Adding 7 to both sides', 'subtracting 7 undoes it, so the solutions stay the same'),
                     ('Dividing both sides by 2', 'multiplying by 2 undoes it, so the solutions stay the same'),
                     ('Multiplying both sides by -3', 'dividing by -3 undoes it, so the solutions stay the same')],
                    'Squaring cannot be undone: a = b and a = -b both lead to a squared = b squared.'),
                 order(EQ + ' Put the lines of this solution of 5 - 3(x - 1) = 2x - 2 in order.',
                       [('A', '5 - 3x + 3 = 2x - 2   (distributive property)'), ('B', '8 - 3x = 2x - 2   (combine 5 and 3)'),
                        ('C', '10 = 5x   (add 3x and 2 to both sides)'), ('D', 'x = 2   (divide both sides by 5)')],
                       steps_in_order('ABCD'), 'Distribute, combine like terms, collect x on one side, divide. Check: '
                                               '5 - 3(1) = 2 and 2(2) - 2 = 2.', expect=list('ABCD'), unique=True),
             ]))


# ------------------------------------------------------------------ Set 40: proof by contradiction
CONTRA = ('In a proof by contradiction, you assume the statement is false and show that this leads to something '
          'impossible.')


def s40():
    return S(40, 'Set up and complete an argument by contradiction',
             main=[
                 mc(CONTRA + ' To prove "there is no largest even integer" by contradiction, how should the proof begin?',
                    'Assume there is a largest even integer; call it N.',
                    [('Assume there is no largest even integer.', 'that assumes the statement itself, not its opposite'),
                     ('Show that 100 is an even integer.', 'one example says nothing about a largest even integer'),
                     ('Assume every even integer is less than 100.', 'that is a different, narrower assumption')],
                    'Assume the opposite. Then N + 2 is even and larger than N, which is impossible.'),
                 order(EVEN + ' ' + CONTRA + ' Put the steps of a proof that if n squared is even, then n is even, in order.',
                       [('A', 'Assume n squared is even, but n is odd.'), ('B', 'Then n = 2k + 1 for some integer k.'),
                        ('C', 'So n squared = 2(2k squared + 2k) + 1, which is odd.'),
                        ('D', 'This contradicts n squared being even, so n must be even.')], steps_in_order('ABCD'),
                       'Assume the opposite of the conclusion, use the definition, compute, then point to the contradiction.',
                       expect=list('ABCD'), unique=True),
                 tf(CONTRA + ' Reaching a statement that contradicts a known fact shows that the assumption was false.',
                    True, 'If the assumption were true, a false statement would follow from it. So the assumption is false.'),
                 mc(EVEN + ' ' + CONTRA + ' Claim: no integer is both even and odd. Suppose n = 2a and n = 2b + 1 for '
                                         'integers a and b. Which line gives the contradiction?',
                    '2a = 2b + 1, so 2(a - b) = 1, but 1 is not 2 times an integer.',
                    [('2a = 2b + 1, so a = b.', 'that algebra is wrong, and it is not a contradiction'),
                     ('n = 4 is even and not odd.', 'one example does not treat a general n'),
                     ('2a + 2b + 1 is an odd number.', 'adding the two forms is true but contradicts nothing')],
                    'a - b would be an integer equal to 1/2, which is impossible.'),
                 values(EVEN + ' ' + CONTRA + ' To show that 15 is not the sum of two even integers, assume 15 = 2a + 2b for '
                                             'integers a and b. Then a + b must equal what number?', [('x', 'a + b =')],
                        'x == 7.5', {'x': 7.5},
                        '2(a + b) = 15 gives a + b = 7.5. But a + b is an integer, so the assumption is impossible.',
                        wrong=[{'x': 7}, {'x': 8}, {'x': 15}]),
             ],
             back=[B('Strategy: assume the opposite and look for the impossible', 'guided_strategy',
                     'Students start a contradiction proof by assuming the wrong thing. Writing the exact opposite first, '
                     'and then hunting for a clash, gives every such proof the same shape.',
                     lesson=lesson('Assume the opposite and look for the impossible',
                                   ['Write the exact opposite (negation) of what you want to prove, and assume it.',
                                    'Reason from that assumption with definitions and facts you know.',
                                    'Stop when you reach something impossible, such as 1 = 0 or a number that is both even '
                                    'and odd. Then the assumption is false, so the statement is true.'],
                                   'Worked example (a different claim)',
                                   ['Prove: there is no smallest positive fraction.'],
                                   ['Assume the opposite: there is a smallest positive fraction r.',
                                    'Then r / 2 is also a positive fraction, and r / 2 < r.',
                                    'That contradicts r being smallest, so no smallest positive fraction exists.']),
                     qs=[
                         mc(CONTRA + ' To prove "n is not divisible by 4" by contradiction, what do you assume?',
                            'n is divisible by 4.', [('n is not divisible by 4.', 'that is the statement itself'),
                                                     ('n is divisible by 2.', 'that is a different statement'),
                                                     ('n is an odd number.', 'that is a different statement')],
                            'Assume the exact opposite of the statement.'),
                         mc(CONTRA + ' To prove "there is no integer x with 2x = 7" by contradiction, what do you assume?',
                            'There is an integer x with 2x = 7.',
                            [('Every integer x has 2x = 7.', 'the opposite of "no x" is "some x", not "every x"'),
                             ('There is an integer x with 2x not equal to 7.', 'that is true and is not the opposite'),
                             ('There is no integer x with 2x = 7.', 'that is the statement itself')],
                            'The opposite of "there is no such x" is "there is such an x".'),
                         tf(CONTRA + ' A proof by contradiction begins by assuming that the statement to be proved is true.',
                            False, 'It begins by assuming the statement is false.'),
                         tf(CONTRA + ' If assuming P leads to 1 = 0, then P is false.', True,
                            'A true assumption cannot lead to a false statement by valid steps.'),
                         mc(EVEN + ' ' + CONTRA + ' Assume there is a largest odd integer M. Which number gives the '
                                                 'contradiction?', 'M + 2',
                            [('M + 1', 'M + 1 is even, so it does not contradict M being the largest odd integer'),
                             ('M - 2', 'M - 2 is smaller than M'),
                             ('2M', '2M is even, so it does not contradict anything')],
                            'M + 2 is odd and larger than M.'),
                     ])],
             f1=FW('Contradiction with divisibility', 'Harder: contradiction arguments about multiples and remainders.', [
                 mc(CONTRA + ' To prove that no integers a and b satisfy 6a + 9b = 10, which fact gives the contradiction?',
                    '6a + 9b = 3(2a + 3b) is a multiple of 3, but 10 is not.',
                    [('6 and 9 are both odd numbers.', '6 is even'),
                     ('10 is even, and 6a + 9b is always odd.', 'a = 1, b = 0 gives 6, which is even'),
                     ('a and b would have to be fractions.', 'that is what is to be shown; it is not a contradiction')],
                    'If 6a + 9b = 10, then 10 would be 3 times an integer, which it is not.'),
                 order(CONTRA + ' Put the steps of the proof that the square root of 2 is not a fraction in order.',
                       [('A', 'Assume the square root of 2 = p / q, with p and q integers in lowest terms.'),
                        ('B', 'Then p squared = 2q squared, so p squared is even, so p is even: p = 2m.'),
                        ('C', 'Then 4m squared = 2q squared, so q squared = 2m squared, and q is even.'),
                        ('D', 'Both p and q are even, which contradicts lowest terms.')], steps_in_order('ABCD'),
                       'Each step uses the one before it, and D clashes with the assumption in A.', expect=list('ABCD'),
                       unique=True),
                 tf('Among any 5 integers, two of them leave the same remainder when divided by 4.', True,
                    'Assume all 5 remainders are different. But only 4 remainders (0, 1, 2, 3) exist, a contradiction.'),
                 sa('A perfect square is divided by 4. What is the largest remainder (0, 1, 2 or 3) that can NEVER occur?',
                    'Remainder:', str(max(set(range(4)) - {n * n % 4 for n in range(100)})),
                    'Even squares are (2k) squared = 4k squared (remainder 0); odd squares are 4(k squared + k) + 1 '
                    '(remainder 1). So 2 and 3 never occur; the larger is 3.',
                    compute=lambda: str(max(set(range(4)) - {n * n % 4 for n in range(100)}))),
                 values('Give an integer n from 1 to 50 for which n squared + 1 is a multiple of 3. If no such n exists, '
                        'enter 0.', [('n', 'n =')], 'n == 0', {'n': 0},
                        'Assume some n works. n leaves remainder 0, 1 or 2 when divided by 3, so n squared leaves 0, 1 or 1; '
                        'then n squared + 1 leaves 1 or 2, never 0. Contradiction, so none exists.',
                        wrong=[{'n': 1}, {'n': 2}, {'n': 5}],
                        method='Checked: no n from 1 to 50 works.' if all((n * n + 1) % 3 for n in range(1, 51))
                        else 'MISMATCH'),
             ]),
             f2=FW('Contradiction in larger arguments', 'Expert: primes, inequalities and flawed contradiction proofs.', [
                 mc(CONTRA + ' Assume there are only finitely many primes, p1, p2, ..., pk, and let N = p1 x p2 x ... x pk + 1. '
                             'Why is this a contradiction?',
                    'N leaves remainder 1 when divided by each listed prime, so a prime factor of N is not on the list.',
                    [('N is always a prime number.', 'not always: 2 x 3 x 5 x 7 x 11 x 13 + 1 = 30031 = 59 x 509'),
                     ('N is always an even number.', 'N is one more than an even product, so it is odd'),
                     ('N is larger than every prime, so N is not prime.', 'being large does not make a number composite')],
                    'Every integer greater than 1 has a prime factor, and none of the listed primes divides N.'),
                 tf('2 x 3 x 5 x 7 x 11 x 13 + 1 is a prime number.', False, '30031 = 59 x 509.',
                    check=lambda: all(30031 % d for d in range(2, 174))),
                 order(CONTRA + ' Put the steps of a proof that if a + b is at least 20, then a is at least 10 or b is at '
                                'least 10, in order.',
                       [('A', 'Assume a + b is at least 20, but a < 10 and b < 10.'), ('B', 'Adding the two inequalities '
                                                                                         'gives a + b < 20.'),
                        ('C', 'That contradicts a + b being at least 20.'),
                        ('D', 'So a is at least 10 or b is at least 10.')], steps_in_order('ABCD'),
                       'The opposite of "a at least 10 or b at least 10" is "a < 10 and b < 10".', expect=list('ABCD'),
                       unique=True),
                 mc(CONTRA + ' Claim: every integer is even. "Proof: Assume some integer is odd, say 3. Then 3 = 2k for no '
                             'integer k. Contradiction." What is wrong?',
                    'Nothing impossible was reached; 3 not being 2k agrees with 3 being odd.',
                    [('It should assume that every integer is odd.', 'the opposite of "every integer is even" is "some '
                                                                     'integer is not even"'),
                     ('It should use 5 instead of 3.', 'any odd example has the same problem'),
                     ('Nothing; the proof is correct.', 'the claim is false, since 3 is odd')],
                    'A contradiction must clash with the assumption or a known fact. Here everything found is consistent.'),
                 sa('At least how many integers must you choose to be sure that two of them leave the same remainder when '
                    'divided by 6?', 'Integers:', '7',
                    'Six integers can have the six different remainders 0 to 5. With 7, assuming all remainders differ '
                    'needs 7 remainders, but only 6 exist.', compute=lambda: str(6 + 1)),
             ]))


SETS = [s37(), s38(), s39(), s40()]
