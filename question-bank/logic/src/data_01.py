"""Logic sets 1-2: mirror reflections; reading exactly what is stated."""
from lq import S, B, FW, mc, figmc, tf, sa, markgrid, values, lesson, order, grid
import figs
from figs import normalize, reflect_cells, rotate_cells
from pz import V_SYM, H_SYM, VSYM_TEXT, HSYM_TEXT, shape_panel, same_shape, choice_figure


def bbox(cells):
    return max(r for r, _ in cells) + 1, max(k for _, k in cells) + 1


def mirror_v(cells):
    n, m = bbox(cells)
    return reflect_cells(cells, n, m, 'v')


def mirror_h(cells):
    n, m = bbox(cells)
    return reflect_cells(cells, n, m, 'h')


def rot(cells, q):
    n, m = bbox(cells)
    return rotate_cells(cells, n, m, q)[0]


def sym_count(cells):
    c = normalize(cells)
    n, m = bbox(c)
    ts = [reflect_cells(c, n, m, 'v'), reflect_cells(c, n, m, 'h')]
    if n == m:
        ts += [{(k, r) for r, k in c}, {(m - 1 - k, n - 1 - r) for r, k in c}]
    return sum(1 for t in ts if normalize(t) == c)


# ------------------------------------------------------------------ Set 1: mirror reflections
S1A = {(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 1)}            # an asymmetric shape in a 4 x 3 box


def q_s1_vertical():
    cand = {'A': rot(S1A, 2), 'B': mirror_h(S1A), 'C': mirror_v(S1A), 'D': rot(S1A, 1)}
    target = mirror_v(S1A)
    assert len({normalize(v) for v in cand.values()}) == 4
    items = [shape_panel(S1A, 4, 3, mirror='right')] + [figs.cells_canvas(set(normalize(cand[L])), 4, 4) for L in 'ABCD']
    svg = choice_figure(items, ['Shape', 'A', 'B', 'C', 'D'])
    return figmc('The shaded shape is reflected in the dashed mirror line on its right. Which figure shows its mirror image? '
                 '(Only the shape matters, not where it sits in its box.)', 4, 'C',
                 {'A': 'a half-turn of the shape, not a reflection', 'B': 'the reflection in a horizontal line (top and bottom swapped)',
                  'D': 'a quarter-turn of the shape'},
                 'A reflection in a vertical line keeps every cell in its row and swaps left and right. Figure C is the only '
                 'panel whose rows match the shape row by row with left and right swapped.',
                 fig=(svg, 'Left: a shape of six shaded cells with a dashed vertical mirror line on its right. Four candidate '
                           'shapes labeled A to D.'),
                 check=lambda L: same_shape(cand[L], target))


S1_PAIRS = [{(0, 0), (1, 0), (1, 1), (1, 2)}, {(0, 1), (1, 0), (1, 1), (0, 2)}, {(0, 0), (0, 1), (0, 2), (1, 2)},
            {(0, 0), (1, 1), (1, 0), (0, 2)}]


def lake_panel(top, bottom, m=3):
    cells = set(top) | {(r + 2, k) for r, k in bottom}
    c = figs.cells_canvas(cells, 4, m)
    c.line(0, 4 + 2 * 22, c.w, 4 + 2 * 22, dash='5 4', sw=2.4)
    return c


def q_s1_lake():
    bottoms = {'A': mirror_h_box(S1_PAIRS[0]), 'B': mirror_h_box(S1_PAIRS[1]), 'C': mirror_h_box(S1_PAIRS[2]),
               'D': {(r, k) for r, k in S1_PAIRS[3]}}   # D just repeats the top shape below the line
    tops = dict(zip('ABCD', S1_PAIRS))
    items = [lake_panel(tops[L], bottoms[L]) for L in 'ABCD']
    svg = choice_figure(items, list('ABCD'))
    ok = lambda L: bottoms[L] == mirror_h_box(tops[L])
    return figmc('Each figure shows a shape above a dashed water line and, below the line, what is supposed to be its reflection '
                 'in the water. In which figure can the lower shape NOT be the reflection of the upper one?', 4, 'D',
                 {L: 'the lower shape is the upper shape flipped top to bottom across the line, so it is a real reflection'
                  for L in 'ABC'},
                 'A reflection in a horizontal line keeps every cell in its column and reverses the order of the rows, measured '
                 'from the line. In D the lower shape is the upper shape moved down without flipping, so the row nearest the '
                 'line is wrong.',
                 fig=(svg, 'Four figures A to D. Each has a shape of four cells in the two rows above a dashed horizontal water '
                           'line and four cells in the two rows below it.'),
                 check=lambda L: not ok(L))


def mirror_h_box(cells):
    """Reflect cells of a 2-row band across the line under it (row 0 <-> row 1)."""
    return {(1 - r, k) for r, k in cells}


def mirror_word_v(w):
    return all(ch in V_SYM for ch in w) and w == w[::-1]


def mirror_word_h(w):
    return all(ch in H_SYM for ch in w)


S1_MARK = {(1, 2), (2, 2), (2, 3), (3, 4), (2, 4)}   # 1-based (row, col) in columns 1-4 of a 4 x 8 grid


def q_s1_mark():
    img = sorted((r, 9 - c) for r, c in S1_MARK)
    c = figs.cells_canvas({(r - 1, k - 1) for r, k in S1_MARK}, 4, 8)
    c.line(4 + 4 * 22, 0, 4 + 4 * 22, c.h, dash='5 4', sw=2.6)
    return markgrid('The grid has 4 rows and 8 columns. The dashed mirror line runs between columns 4 and 5. The shaded cells '
                    'are in row 1 column 2, row 2 columns 2, 3 and 4, and row 3 column 4. Mark the cells of their mirror image. '
                    '(Cells are named row,column; row 1 is the top row and column 1 the left column.)', 4, 8, img,
                    'Each cell keeps its row, and a cell in column c lands in column 9 - c (the same distance on the other side '
                    'of the line between columns 4 and 5): (1,7), (2,7), (2,6), (2,5), (3,5).',
                    fig=(c.svg(), 'A 4 by 8 grid with five shaded cells left of a dashed vertical line between columns 4 and 5.'),
                    method='Automatic: the key is computed as column 9 - c for every shaded cell.')


def s1():
    return S(1, 'Decide what a mirror reflection must show',
             main=[
                 q_s1_vertical(),
                 q_s1_lake(),
                 mc('Words are written left to right in block capitals and seen in a left-right mirror (a vertical mirror line). '
                    + VSYM_TEXT + ' Which word looks exactly the same in the mirror?', 'TOOT',
                    [('NOON', 'N is not one of the listed letters, so each N appears reversed in the mirror'),
                     ('ZOOM', 'Z is not listed, and the mirror reverses the letter order, giving MOOZ'),
                     ('BIB', 'B is not listed, so each B appears reversed even though BIB reads the same backward')],
                    'A left-right mirror reverses the order of the letters and mirrors each letter. The word looks the same only '
                    'if it reads the same backward AND every letter is a listed symmetric letter. TOOT is the only choice that '
                    'does both.', check=mirror_word_v),
                 mc('A word is written in block capitals and seen reflected in calm water below it (a horizontal mirror line). '
                    + HSYM_TEXT + ' The letter order stays the same in this reflection. Which word looks exactly the same in '
                    'the water?', 'CODE',
                    [('CORE', 'R is not one of the listed letters, so it appears upside down'),
                     ('BEAD', 'A is not listed, so it appears upside down'),
                     ('BOXES', 'S is not listed, so it appears changed')],
                    'A top-bottom reflection keeps the order of the letters and flips each letter. The word looks the same when '
                    'every letter is a listed letter; only CODE qualifies.', check=mirror_word_h),
                 q_s1_mark(),
             ],
             back=[B('Strategy: reflect one cell at a time', 'guided_strategy',
                     'Students who pick a rotated or unflipped shape usually try to picture the whole shape at once. Reflecting '
                     'one cell at a time (same row, same distance on the other side) makes every reflection checkable.',
                     lesson=lesson('Reflect one cell at a time',
                                   ['A mirror line acts like a fold. Each point keeps its distance from the line but ends up on '
                                    'the other side. Points on the line stay where they are.',
                                    'For a vertical mirror line, a cell keeps its row and only its column changes. For a '
                                    'horizontal mirror line, a cell keeps its column and only its row changes.',
                                    'So reflect one cell at a time: count how far it is from the line, then count the same '
                                    'distance on the other side. Check two or three cells; if any one is wrong, the figure is '
                                    'not the reflection.'],
                                   'Worked example (a different figure)',
                                   ['A grid has 6 rows. A horizontal mirror line lies between rows 3 and 4. A shape has cells at '
                                    'row 1 column 2, row 2 column 2 and row 3 column 5. Where is its reflection?'],
                                   ['Row 3 is 1 row above the line, so its image is 1 row below it: row 4. Row 2 goes to row 5 '
                                    'and row 1 to row 6.',
                                    'Columns do not change in a horizontal mirror.',
                                    'Image: row 6 column 2, row 5 column 2 and row 4 column 5.',
                                    'Quick check: each cell and its image add up to 7 rows (1 + 6, 2 + 5, 3 + 4), the same for '
                                    'every pair, because the line is halfway between them.']),
                     qs=[
                         sa('A grid has 10 columns. A vertical mirror line lies between columns 5 and 6. A shaded cell is in '
                            'column 2. In which column is its mirror image?', 'Column:', '9',
                            'Column 2 is 4 columns left of the line (columns 2, 3, 4, 5), so its image is 4 columns right of '
                            'it: column 9. Check: 2 + 9 = 11 = 5 + 6.', compute=lambda: str(11 - 2)),
                         sa('A grid has 8 rows. A horizontal mirror line lies between rows 4 and 5. A shaded cell is in row 1. '
                            'In which row is its mirror image?', 'Row:', '8',
                            'Row 1 is 4 rows above the line, so the image is 4 rows below it: row 8.', compute=lambda: str(9 - 1)),
                         tf('A reflection in a vertical mirror line keeps every cell in its own row.', True,
                            'Only the column changes; the row stays the same.'),
                         mc('A cell is 3 columns to the left of a vertical mirror line. Where is its mirror image?',
                            '3 columns to the right of the line',
                            [('3 columns to the left of the line', 'that is the original cell'),
                             ('6 columns to the right of the line', 'the distance from the line is kept, not doubled'),
                             ('on the mirror line itself', 'only points on the line stay on it')],
                            'A reflection keeps the distance to the line and changes the side.'),
                         markgrid('A row of 6 cells has a mirror line between cells 3 and 4. Cell 1 is shaded. Mark the cell '
                                  'of its mirror image. (The grid is 1 row by 6 columns; cells are named row,column.)', 1, 6,
                                  [(1, 6)], 'Cell 1 is 3 cells left of the line, so its image is 3 cells right: cell 6.',
                                  method='Automatic: image column = 7 - 1.'),
                     ])],
             f1=FW('Combine reflections and read mirrored clocks and words',
                   'Same skill, harder: two reflections in a row, reflections of clock faces, and words written downward.', [
                       mc('A clock face with no numbers shows 2:20. You see it in a left-right mirror. What time does the '
                          'mirrored clock appear to show?', '9:40',
                          [('10:20', 'only the hour hand was mirrored; the minute hand was left at 20 minutes'),
                           ('2:40', 'only the minute hand was mirrored'), ('3:40', 'the hands were swapped instead of mirrored')],
                          'A left-right mirror sends a time t to 12:00 - t. 12:00 - 2:20 = 9:40. Check: the minute hand at 4 '
                          '(20 minutes) appears at 8 (40 minutes), and the hour hand just past 2 appears just before 10.',
                          check=lambda t: (lambda h, m: (12 * 60 - (2 * 60 + 20)) == h * 60 + m)(*map(int, t.split(':')))),
                       q_s1_double(),
                       mc('A word is written DOWN the page, one block capital under another, and seen in a left-right mirror. '
                          + VSYM_TEXT + ' Which word looks exactly the same?', 'MATH',
                          [('MAZE', 'Z and E are not listed, so they appear reversed'),
                           ('BATH', 'B is not listed'), ('MASK', 'S and K are not listed')],
                          'Written downward, a left-right mirror keeps the order (top to bottom) and mirrors each letter, so the '
                          'word looks the same when every letter is listed. Only MATH qualifies.',
                          check=lambda w: all(ch in V_SYM for ch in w)),
                       q_s1_both_axes(),
                       tf('A figure looks the same after a reflection in a vertical line through its center and after a '
                          'reflection in a horizontal line through its center. Then it also looks the same after a half-turn '
                          'about its center.', True,
                          'Reflecting in the vertical line and then in the horizontal line sends (x, y) to (-x, y) and then to '
                          '(-x, -y), which is a half-turn. Each reflection leaves the figure unchanged, so the half-turn does too.'),
                   ]),
             f2=FW('Construct and count symmetric figures', 'Expert: least changes for symmetry, counting symmetric strings, '
                                                           'composing parallel mirrors, and classifying symmetry.', [
                 q_s1_least(),
                 sa('Strings of 3 letters are made from the letters A, H, M, O and T (letters may repeat). Each is written left '
                    'to right in block capitals. ' + VSYM_TEXT + ' How many of these strings look exactly the same in a '
                    'left-right mirror?', 'Number of strings:', '25',
                    'All five letters are mirror-symmetric, so a string looks the same exactly when it reads the same backward: '
                    'the first and last letters match. Choose the first letter (5 ways) and the middle letter (5 ways): 25.',
                    compute=lambda: str(sum(1 for a in 'AHMOT' for b in 'AHMOT' for c in 'AHMOT' if a + b + c == (a + b + c)[::-1]))),
                 mc('Two vertical mirror lines are 3 cells apart: line 1 on the left, line 2 on the right. A shape is reflected '
                    'in line 1 and the image is then reflected in line 2. Where does the final image end up?',
                    'the original shape moved 6 cells to the right, not flipped',
                    [('the original shape moved 3 cells to the right, not flipped', 'two reflections move the shape twice the '
                      'distance between the lines'),
                     ('a mirror image of the shape, 6 cells to the right', 'two reflections undo each other\'s flip'),
                     ('back exactly where the shape started', 'that only happens when both lines are the same line')],
                    'Put line 1 at x = a and line 2 at x = b = a + 3. The first reflection sends x to 2a - x; the second sends that '
                    'to 2b - (2a - x) = x + 2(b - a) = x + 6. Every point moves 6 to the right and nothing is flipped.'),
                 values('A row of 12 cells is numbered 1 to 12. A mirror line lies between cells 6 and 7. Give two cell numbers a '
                        'and b, with a less than b, that are mirror images of each other.', [('a', 'a ='), ('b', 'b =')],
                        'a + b == 13 and a < b and a >= 1 and b <= 12 and isInteger(a) and isInteger(b)', {'a': 4, 'b': 9},
                        'Cells that mirror each other are the same distance from the line, so their numbers add to 6 + 7 = 13: '
                        '(1, 12), (2, 11), (3, 10), (4, 9), (5, 8) or (6, 7). Any one pair is correct.',
                        wrong=[{'a': 4, 'b': 10}, {'a': 6, 'b': 6}, {'a': 9, 'b': 4}],
                        search={'a': range(1, 13), 'b': range(1, 13)}),
                 q_s1_one_line(),
             ]))


def q_s1_double():
    sh = {(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)} | {(0, 1)}
    target = rot(sh, 2)
    cand = {'A': mirror_v(sh), 'B': target, 'C': sh, 'D': mirror_h(sh)}
    assert len({normalize(v) for v in cand.values()}) == 4
    items = [shape_panel(sh, 3, 3)] + [figs.cells_canvas(set(normalize(cand[L])), 3, 3) for L in 'ABCD']
    return figmc('The shape is reflected in a vertical mirror line and then the result is reflected in a horizontal mirror '
                 'line. Which figure shows the final result? (Only the shape matters, not where it sits.)', 4, 'B',
                 {'A': 'only the first (vertical) reflection', 'C': 'the starting shape: the two reflections do not cancel',
                  'D': 'only the second (horizontal) reflection'},
                 'A vertical reflection then a horizontal one sends (x, y) to (-x, -y): a half-turn. Figure B is the shape turned '
                 'halfway around.', fig=(choice_figure(items, ['Shape', 'A', 'B', 'C', 'D']),
                                         'A shape of six cells and four candidate shapes A to D.'),
                 check=lambda L: same_shape(cand[L], target))


def q_s1_both_axes():
    given = {(1, 1), (1, 2), (2, 2), (3, 3)}            # 1-based, top-left quadrant of a 6 x 6 grid (rows/cols 1-3)
    full = set()
    for r, c in given:
        full |= {(r, c), (r, 7 - c), (7 - r, c), (7 - r, 7 - c)}
    g = figs.cells_canvas({(r - 1, c - 1) for r, c in given}, 6, 6)
    g.line(4 + 3 * 22, 0, 4 + 3 * 22, g.h, dash='5 4', sw=2.4)
    g.line(0, 4 + 3 * 22, g.w, 4 + 3 * 22, dash='5 4', sw=2.4)
    return markgrid('A 6 by 6 grid has two dashed mirror lines: a vertical one between columns 3 and 4 and a horizontal one '
                    'between rows 3 and 4. The figure must look the same in BOTH mirrors. Four cells are already shaded in the '
                    'top-left quarter: (1,1), (1,2), (2,2) and (3,3). Mark every shaded cell of the completed figure, including '
                    'the four given cells.', 6, 6, sorted(full),
                    'Each given cell (r, c) also needs its images (r, 7 - c), (7 - r, c) and (7 - r, 7 - c). That gives 4 x 4 = 16 '
                    'cells, one copy of the pattern in each quarter.', fig=(g.svg(), 'A 6 by 6 grid with four shaded cells in '
                                                                               'the top-left quarter and two dashed mirror lines.'),
                    method='Automatic: the key is the union of the four images of each given cell.')


def q_s1_least():
    sh = {(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (3, 1)}   # inside a 4-row x 4-column box, line between cols 2 and 3
    n, m = 4, 4
    img = {(r, m - 1 - k) for r, k in sh}
    need = len(img - sh)
    g = figs.cells_canvas(sh, n, m)
    g.line(4 + 2 * 22, 0, 4 + 2 * 22, g.h, dash='5 4', sw=2.4)
    return sa('The figure is on a 4 by 4 grid with a dashed vertical line between columns 2 and 3. Shaded cells can be added but '
              'not removed. What is the least number of cells you must add so that the figure looks the same in a mirror '
              'along the dashed line?', 'Cells to add:', str(need),
              'For symmetry every shaded cell needs its image across the line (column c pairs with column 5 - c). Row 1: columns 1 '
              'and 2 need columns 4 and 3. Row 2: column 1 needs column 4; columns 2 and 3 are already each other\'s images. '
              'Row 3: column 1 needs column 4. Row 4: column 2 needs column 3. New cells: (1,3), (1,4), (2,4), (3,4), (4,3), so '
              '%d. Adding fewer leaves some shaded cell without its image.'
              % need, fig=(g.svg(), 'A 4 by 4 grid with seven shaded cells and a dashed vertical line through the middle.'),
              compute=lambda: str(len({(r, 3 - k) for r, k in sh} - sh)))


def q_s1_one_line():
    shapes = {'A': {(0, 0), (0, 1), (0, 2), (1, 1)},                 # T: one line (vertical)
              'B': {(0, 0), (0, 1), (1, 1), (1, 2)},                 # S/Z: none
              'C': {(0, 0), (0, 1), (1, 0), (1, 1)},                 # square: four
              'D': {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}}         # plus: four
    counts = {L: sym_count(s) for L, s in shapes.items()}
    items = [figs.cells_canvas(s, 3, 3) for s in shapes.values()]
    return figmc('Count only mirror lines that run vertically, horizontally or diagonally through the center of the shape '
                 '(the middle of the smallest rectangle around it). Which figure has exactly ONE mirror line?', 4, 'A',
                 {'B': 'no mirror line: it only looks the same after a half-turn',
                  'C': 'four mirror lines (vertical, horizontal and both diagonals)',
                  'D': 'four mirror lines (vertical, horizontal and both diagonals)'},
                 'Testing each kind of line: A (a T shape) looks the same only in the vertical line. B looks the same after a '
                 'half-turn but in no mirror; C and D each have four mirror lines.',
                 fig=(choice_figure(items, list('ABCD')), 'Four small shapes made of cells, labeled A to D.'),
                 check=lambda L: counts[L] == 1)


SETS = [s1()]
