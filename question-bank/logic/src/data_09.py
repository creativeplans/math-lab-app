"""Logic sets 23-26: cube nets; valid versus sound; moves and rearrangements; quantifiers over a stated domain."""
import itertools
from collections import deque
from lq import S, B, FW, mc, figmc, tf, sa, order, values, lesson, grid, tt
import figs
import pz
from pz import opposite_pairs, opposite_of, fold, choice_figure
from data_08 import valid, imp

TF = [True, False]

# ------------------------------------------------------------------ Set 23: cube nets
NET_RULE = ('The squares are folded along their shared edges to make a cube, with the letters on the outside. Faces that '
            'are opposite each other on the cube never touch.')
N1 = {(0, 1): 'A', (1, 0): 'B', (1, 1): 'C', (1, 2): 'D', (2, 1): 'E', (3, 1): 'F'}           # cross
N2 = {(0, 0): 'P', (1, 0): 'Q', (1, 1): 'R', (1, 2): 'S', (1, 3): 'T', (2, 3): 'U'}           # 1-4-1 stagger
N3 = {(0, 0): 'G', (0, 1): 'H', (1, 1): 'I', (1, 2): 'J', (2, 2): 'K', (2, 3): 'L'}           # staircase
N4 = {(0, 0): 'M', (0, 1): 'N', (0, 2): 'O', (1, 2): 'V', (1, 3): 'W', (1, 4): 'X'}           # 3-3 shifted
for _n in (N1, N2, N3, N4):
    assert opposite_pairs(_n) is not None


def adjacent(net, a, b):
    return a != b and frozenset((a, b)) not in opposite_pairs(net)


def net_fig(net):
    return figs.cube_net(net)


BAD = [{(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0)},          # five in a row
       {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)},          # 2 x 3 block
       {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)} ^ {(1, 2), (2, 1)},
       {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2)}]
GOOD = [{(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)}, {(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)}]
for _b in BAD:
    assert fold({c: i for i, c in enumerate(_b)}) is None, _b
for _g in GOOD:
    assert fold({c: i for i, c in enumerate(_g)}) is not None


def shape_fig(cells_list, labels):
    items = []
    for cs in cells_list:
        n = max(r for r, _ in cs) + 1
        m = max(k for _, k in cs) + 1
        items.append(figs.cells_canvas(set(cs), n, m, cell=18))
    return choice_figure(items, labels)


def q23_which_folds():
    cand = {'A': BAD[0], 'B': BAD[1], 'C': GOOD[0], 'D': BAD[3]}
    return figmc('Each figure is made of six squares. Which figure can be folded along the lines between squares into a closed '
                 'cube (with no overlapping squares)?', 4, 'C',
                 {'A': 'five squares in a row: the 1st and 5th squares would land on the same face',
                  'B': 'a 2 by 3 block: the squares fold into a ring of four with two squares overlapping',
                  'D': 'four squares meet around one point, so two faces of the cube would overlap when folded'},
                 'Fold C: its row of four squares wraps around to make four sides, and the two single squares (one above and '
                 'one below the row) close the top and the bottom. The others fold with two squares on the same face.',
                 fig=(shape_fig([cand[L] for L in 'ABCD'], list('ABCD')), 'Four shapes made of six squares, labeled A to D.'),
                 check=lambda L: fold({c: i for i, c in enumerate(cand[L])}) is not None)


def s23():
    o1 = opposite_of(N1, 'A')
    return S(23, 'Match a cube to its net: opposite and adjacent faces',
             main=[
                 mc(NET_RULE + ' Which letter is on the face OPPOSITE the face A?', o1,
                    [('C', 'C shares an edge with A in the net, so they touch on the cube'),
                     ('B', 'B folds up next to A, so they touch'), ('F', 'F folds over the top and touches A')],
                    'In the cross-shaped net, the column A, C, E, F folds around the cube: A and E are two squares apart in the '
                    'column, so they are opposite. (C is opposite F, and B is opposite D.)',
                    fig=(net_fig(N1).svg(), 'A cross-shaped net of six squares: A on top, then B, C, D in a row, then E, then F '
                                            'below C.'),
                    check=lambda t: t == opposite_of(N1, 'A')),
                 q23_which_folds(),
                 grid(NET_RULE + ' For each face P, Q and R of this net, which letter is on the opposite face?',
                      ['P', 'Q', 'R'], ['S', 'T', 'U'], lambda a: all(opposite_of(N2, x) == a[x] for x in 'PQR'),
                      'In the row Q, R, S, T, squares two apart are opposite: Q-S and R-T. P and U, attached at opposite ends, '
                      'are opposite each other.',
                      fig=(net_fig(N2).svg(), 'A net: P above Q; a row Q, R, S, T; U below T.')),
                 mc(NET_RULE + ' Which two letters can NEVER be seen at the same time when you look at the cube?',
                    'G and J', [('G and H', 'they share an edge in the net'), ('H and I', 'they share an edge'),
                                ('H and J', 'H is opposite K, so H and J share an edge on the cube')],
                    'Two faces can never be seen together only if they are opposite. In this staircase net, G is opposite J, '
                    'H is opposite K, and I is opposite L.',
                    fig=(net_fig(N3).svg(), 'A staircase net: G, H in the top row; H above I; I, J in the middle; J above K; '
                                            'K, L in the bottom row.'),
                    check=lambda t: frozenset(t.split(' and ')) in opposite_pairs(N3)),
                 tf(NET_RULE + ' On the cube made from this net, faces M and W share an edge.', True,
                    'Folding this net makes M opposite O, N opposite W, and V opposite X. M and W are not an opposite pair, '
                    'so they share an edge.', check=lambda: adjacent(N4, 'M', 'W'),
                    fig=(net_fig(N4).svg(), 'A net: M, N, O in the top row; V, W, X in the next row, starting under O.')),
             ],
             back=[B('Strategy: skip one square to find the opposite face', 'guided_strategy',
                     'Students try to picture the whole fold. The rule "in a straight row, squares with exactly one square '
                     'between them are opposite" finds most opposite faces without folding in your head.',
                     lesson=lesson('Skip one square to find the opposite face',
                                   ['A cube has 3 pairs of opposite faces. Opposite faces never share an edge.',
                                    'In any straight row or column of the net, two squares with exactly one square between them '
                                    'end up opposite.',
                                    'Squares that share an edge in the net always share an edge on the cube.',
                                    'For a square sticking out of a row, slide it along its row in your mind: it is opposite the '
                                    'square two steps away along the direction it folds.'],
                                   'Worked example (a different net)',
                                   ['A net has the row 1, 2, 3, 4 with square 5 above square 2 and square 6 below square 3.'],
                                   ['In the row: 1 and 3 are opposite; 2 and 4 are opposite.',
                                    'That leaves 5 and 6, which must be opposite each other.',
                                    'Check: 5 touches 2 in the net, and 2 is not opposite 5. Every face has exactly one opposite.']),
                     qs=[
                         mc('A straight row of four squares, numbered 1 to 4, is part of a cube net. Which square is opposite '
                            'square 1?', '3', [('2', 'shares an edge with 1'), ('4', '4 is opposite 2'), ('1', 'a face is not '
                                                                                                             'opposite itself')],
                            'Exactly one square between them.'),
                         tf('Two squares that share an edge in a net always share an edge on the cube.', True,
                            'Folding keeps shared edges together.'),
                         sa('How many pairs of opposite faces does a cube have?', 'Pairs:', '3', '6 faces in pairs: 3.',
                            compute=lambda: str(6 // 2)),
                         mc('On a cube, how many faces share an edge with any one face?', '4', [('5', 'the opposite face does '
                                                                                                  'not touch it'),
                                                                                         ('3', 'four sides surround it'),
                                                                                         ('6', 'a face does not touch itself')],
                            'All faces except itself and the opposite face.'),
                         tf('Two faces that are opposite on the cube can be seen at the same time.', False,
                            'You can see at most three faces at once, and they all meet at one corner; opposite faces never meet.'),
                     ])],
             f1=FW('Harder nets', 'Harder: nets of other shapes and questions about every face.', [
                 mc(NET_RULE + ' Which letter is opposite H?', opposite_of(N3, 'H'),
                    [('G', 'shares an edge with H'), ('I', 'shares an edge with H'), ('J', 'J is opposite G')],
                    'In the staircase, H is opposite K (H and K are two steps apart along the stair).',
                    fig=(net_fig(N3).svg(), 'A staircase net of six squares labeled G to L.'),
                    check=lambda t: t == opposite_of(N3, 'H')),
                 sa('Each of the four figures is made of six squares. How many of them can be folded into a closed cube?',
                    'Count:', '2', 'Folding each figure: in A and C two squares land on the same face of the cube, so they '
                    'do not make a closed cube. B (a staircase) and D (a row of four with one square above and one below) '
                    'fold into a cube. So 2.',
                    fig=(shape_fig([BAD[2], GOOD[1], BAD[0], GOOD[0]], list('ABCD')), 'Four shapes made of six squares, '
                                                                                     'labeled A to D.'),
                    compute=lambda: str(sum(fold({c: i for i, c in enumerate(x)}) is not None
                                            for x in [BAD[2], GOOD[1], BAD[0], GOOD[0]]))),
                 grid(NET_RULE + ' For each face M, N and V of this net, which letter is on the opposite face?',
                      ['M', 'N', 'V'], ['O', 'W', 'X'], lambda a: all(opposite_of(N4, x) == a[x] for x in 'MNV'),
                      'M, N, O are a row of three, so M and O (one square apart) are opposite. V, W, X are a row of three, so V '
                      'and X are opposite. That leaves N and W as the third pair.',
                      fig=(net_fig(N4).svg(), 'A net: M, N, O in the top row; V, W, X in the next row, starting under O.')),
                 tf('Every net of a cube has exactly 6 squares.', True, 'A cube has 6 faces.'),
                 mc(NET_RULE + ' In the cross-shaped net (A on top; B, C, D across; E and F below C), which two faces each '
                               'share an edge with all of B, C and D?', 'A and E',
                    [('A and F', 'F is opposite C, so F does not touch C'), ('E and F', 'F does not touch C'),
                     ('B and D', 'B and D are opposite each other')],
                    'The opposite pairs are A-E, B-D and C-F. A face touches B, C and D unless it is one of them or opposite '
                    'one of them; that leaves A and E.',
                    check=lambda t: set(t.split(' and ')) == {x for x in 'ABCDEF' if all(adjacent(N1, x, y) for y in 'BCD')},
                    fig=(net_fig(N1).svg(), 'A cross-shaped net of six squares labeled A to F.')),
             ]),
             f2=FW('Counting and designing nets', 'Expert: count all nets and design numbered cubes.', [
                 sa('Count the different nets of a cube: shapes of six squares joined edge to edge that fold into a cube, '
                    'where shapes that are turns or flips of each other count as the same. How many are there?', 'Nets:', '11',
                    'There are 35 shapes of six squares; folding each one shows that exactly 11 make a cube.',
                    compute=lambda: str(count_nets())),
                 sa('The faces of a cube are colored so that faces sharing an edge always have different colors. What is the '
                    'least number of colors needed?', 'Colors:', '3', 'Opposite faces never touch, so each opposite pair can '
                                                                     'share a color: 3 colors. Two colors are not enough: the '
                                                                     'three faces at a corner all touch each other.',
                    compute=lambda: str(min_colors())),
                 tf('On a standard die, opposite faces add to 7. In a cross-shaped net with 1, 2, 3, 4 in the long column and '
                    '5, 6 on the two sides, the numbers can follow this rule.', False,
                    'In the long column, the 1st and 3rd squares are opposite (1 and 3) and so are the 2nd and 4th (2 and 4); '
                    'neither pair adds to 7.',
                    check=lambda: all(sum(v for k, v in {'A': 1, 'C': 2, 'E': 3, 'F': 4, 'B': 5, 'D': 6}.items() if k in pr) == 7
                                      for pr in opposite_pairs(N1))),
                 mc(NET_RULE + ' The numbers 1 to 6 are written on the cross-shaped net with A = 1, B = 2, C = 3, D = 5, E = 6 '
                               'and F = 4. Which statement is true?', 'Every pair of opposite faces adds to 7.',
                    [('Faces 1 and 2 are opposite.', 'they share an edge'), ('Faces 3 and 4 touch.', 'they are opposite'),
                     ('Faces 2 and 6 are opposite.', '2 is opposite 5')],
                    'Opposite pairs of this net are A-E (1, 6), B-D (2, 5) and C-F (3, 4): each adds to 7.',
                    fig=(net_fig(N1).svg(), 'A cross-shaped net of six squares labeled A to F.'),
                    check=lambda t: t.startswith('Every') and all(sum({'A': 1, 'B': 2, 'C': 3, 'D': 5, 'E': 6, 'F': 4}[x]
                                                                      for x in pr) == 7 for pr in opposite_pairs(N1))),
                 tf('A cube net can contain four squares in a 2 by 2 block.', False,
                    'Four squares around one point would fold onto only three faces at that corner, so two would overlap.',
                    check=lambda: count_nets(with_block=True) > 0),
             ]))


def all_hexominoes():
    from figs import normalize

    def canon(c):
        forms = []
        for flip in (False, True):
            s = {(r, -k) for r, k in c} if flip else set(c)
            for _ in range(4):
                s = {(k, -r) for r, k in s}
                forms.append(tuple(sorted(normalize(s))))
        return min(forms)
    shapes = {frozenset([(0, 0)])}
    for _ in range(5):
        nxt = set()
        for s in shapes:
            for r, k in s:
                for dr, dk in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (r + dr, k + dk)
                    if c not in s:
                        nxt.add(frozenset(canon(s | {c})))
        shapes = nxt
    return shapes


def count_nets(with_block=False):
    out = 0
    for s in all_hexominoes():
        if fold({c: i for i, c in enumerate(s)}) is None:
            continue
        if with_block and not any({(r, k), (r + 1, k), (r, k + 1), (r + 1, k + 1)} <= set(s) for r, k in s):
            continue
        out += 1
    return out


def min_colors():
    pairs = list(opposite_pairs(N1))
    faces = 'ABCDEF'
    for k in range(1, 7):
        for col in itertools.product(range(k), repeat=6):
            c = dict(zip(faces, col))
            if all(c[a] != c[b] for a in faces for b in faces if adjacent(N1, a, b)):
                return k


SETS = [s23()]
