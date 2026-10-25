"""Logic sets 9-12: rotation or reflection; deduction and induction; the structure of words; conditionals."""
import itertools
from lq import S, B, FW, mc, figmc, tf, sa, order, values, lesson, grid, tt, markgrid
import figs
from figs import normalize, reflect_cells
from pz import shape_panel, same_shape, choice_figure
from data_01 import rot, mirror_v, mirror_h, bbox


def rotations(c):
    return [normalize(rot(c, q)) for q in range(4)]


def reflections(c):
    m = normalize(mirror_v(c))
    return [normalize(rot(m, q)) for q in range(4)]


def is_rotation(a, b):
    return normalize(a) in rotations(b)


def is_reflection(a, b):
    return normalize(a) in reflections(b)


SH9 = {(0, 0), (1, 0), (1, 1), (1, 2), (2, 1)}          # a chiral pentomino (F-like)
assert not set(rotations(SH9)) & set(reflections(SH9))
ROT180_LETTERS = set('HINOSXZ')
ROT_TEXT = 'In the block capitals used here, exactly these letters look the same after a half-turn: H I N O S X Z.'


def q9_rotation():
    cand = {'A': mirror_v(SH9), 'B': mirror_h(SH9), 'C': rot(SH9, 1), 'D': {(k, r) for r, k in SH9}}
    items = [shape_panel(SH9, 3, 3)] + [figs.cells_canvas(set(normalize(cand[L])), 3, 3) for L in 'ABCD']
    return figmc('Which figure shows the shape TURNED (rotated in the page), not flipped over? (Only the shape matters, '
                 'not where it sits in its box.)', 4, 'C',
                 {'A': 'a left-right flip (reflection)', 'B': 'a top-bottom flip (reflection)',
                  'D': 'a flip across a diagonal (reflection)'},
                 'Turning never changes which way the shape "curls". Figure C is the shape after a quarter-turn clockwise; '
                 'A, B and D are mirror images, which no turn can produce for this shape.',
                 fig=(choice_figure(items, ['Shape', 'A', 'B', 'C', 'D']), 'A shape of five cells and four candidates A to D.'),
                 check=lambda L: is_rotation(cand[L], SH9))


SH9B = {(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)}
assert not set(rotations(SH9B)) & set(reflections(SH9B))


def q9_reflection():
    cand = {'A': rot(SH9B, 1), 'B': rot(SH9B, 2), 'C': rot(SH9B, 3), 'D': mirror_v(SH9B)}
    items = [shape_panel(SH9B, 3, 3)] + [figs.cells_canvas(set(normalize(cand[L])), 3, 3) for L in 'ABCD']
    return figmc('Three of the figures are the shape turned (rotated). One is the shape flipped over (a mirror image). '
                 'Which figure is the flipped one?', 4, 'D',
                 {'A': 'a quarter-turn clockwise', 'B': 'a half-turn', 'C': 'a quarter-turn counterclockwise'},
                 'Turn each candidate back to the starting position: A, B and C match the shape; D can only be matched by '
                 'flipping it over.',
                 fig=(choice_figure(items, ['Shape', 'A', 'B', 'C', 'D']), 'A shape of five cells and four candidates A to D.'),
                 check=lambda L: is_reflection(cand[L], SH9B) and not is_rotation(cand[L], SH9B))


def q9_quarter():
    sh = {(0, 0), (0, 1), (1, 0), (2, 0), (3, 0), (2, 1)}
    target = rot(sh, 1)
    cand = {'A': rot(sh, 3), 'B': target, 'C': rot(sh, 2), 'D': mirror_v(sh)}
    assert len({normalize(v) for v in cand.values()}) == 4
    items = [shape_panel(sh, 4, 2)] + [figs.cells_canvas(set(normalize(cand[L])), 4, 4) for L in 'ABCD']
    return figmc('The shape is turned a quarter-turn CLOCKWISE (90 degrees, like a clock hand moving from 12 to 3). Which '
                 'figure shows the result?', 4, 'B',
                 {'A': 'a quarter-turn counterclockwise', 'C': 'a half-turn', 'D': 'a mirror image, not a turn'},
                 'After a clockwise quarter-turn, the left column of the shape becomes its top row, read from left to right '
                 'going upward; figure B is that result.',
                 fig=(choice_figure(items, ['Shape', 'A', 'B', 'C', 'D']), 'A tall shape of six cells and four candidates A to D.'),
                 check=lambda L: same_shape(cand[L], target))


def q9_mark():
    given = {(1, 1), (1, 2), (1, 3), (2, 1)}              # 1-based in a 4 x 4 grid
    turned = sorted((c, 5 - r) for r, c in given)        # quarter-turn clockwise about the grid center
    g = figs.cells_canvas({(r - 1, c - 1) for r, c in given}, 4, 4)
    return markgrid('A 4 by 4 grid has shaded cells at (1,1), (1,2), (1,3) and (2,1), written as row,column with row 1 at the '
                    'top. The whole grid is turned a quarter-turn clockwise about its center. Mark the cells where the shaded '
                    'cells end up.', 4, 4, turned,
                    'A clockwise quarter-turn of a 4 by 4 grid sends row r, column c to row c, column 5 - r. So (1,1) -> (1,4), '
                    '(1,2) -> (2,4), (1,3) -> (3,4), (2,1) -> (1,3).',
                    fig=(g.svg(), 'A 4 by 4 grid with four shaded cells in the top-left corner area.'),
                    method='Automatic: each cell mapped by (r, c) -> (c, 5 - r).')


def s9():
    return S(9, 'Distinguish rotations from reflections',
             main=[q9_rotation(), q9_reflection(), q9_quarter(),
                   mc('Capital letters are turned upside down by a half-turn (180 degrees in the page). ' + ROT_TEXT +
                      ' Which letter looks the same after the half-turn?', 'N',
                      [('M', 'a half-turn of M looks like W'), ('E', 'a half-turn of E faces the other way and is upside down'),
                       ('A', 'a half-turn of A is upside down')], 'N is on the stated list; M, E and A are not.',
                      check=lambda L: L in ROT180_LETTERS),
                   q9_mark()],
             back=[B('Strategy: follow one marked corner', 'guided_strategy',
                     'Students mix up turns and flips because the whole shape changes position. Following one distinctive '
                     'cell (and which way the shape bends from it) separates turns from flips.',
                     lesson=lesson('Follow one marked corner',
                                   ['Pick one distinctive cell of the shape, for example the end of its longest arm, and note '
                                    'which way the shape bends from there (clockwise or counterclockwise).',
                                    'A turn moves that cell around but keeps the bending direction the same.',
                                    'A flip reverses the bending direction. If the direction is reversed, the figure is a '
                                    'mirror image and no turn can produce it (unless the shape is symmetric).',
                                    'For a quarter-turn clockwise, the top of the shape goes to the right side; for a half-turn, '
                                    'the top goes to the bottom and left goes to right.'],
                                   'Worked example (a different shape)',
                                   ['An L made of 3 cells going down and 1 cell to the right at the bottom. Where does the '
                                    'single cell go after a half-turn?'],
                                   ['After a half-turn, the bottom goes to the top and the right goes to the left.',
                                    'So the single cell ends up at the TOP, on the LEFT: the shape looks like a "7" made of cells.',
                                    'Bending direction: going down the long arm, the foot turns left (counterclockwise) in the '
                                    'original and still turns the same way after the half-turn, so it is a turn, not a flip.']),
                     qs=[
                         tf('A quarter-turn clockwise followed by another quarter-turn clockwise is the same as a half-turn.',
                            True, '90 + 90 = 180 degrees.'),
                         mc('An arrow points up. It is turned a quarter-turn clockwise. Which way does it point now?', 'right',
                            [('left', 'that is a quarter-turn counterclockwise'), ('down', 'that is a half-turn'),
                             ('up', 'it has turned')], 'Up turns to the right, like a clock hand from 12 to 3.'),
                         mc('An arrow points right. It is reflected in a vertical mirror line. Which way does it point now?',
                            'left', [('right', 'a vertical mirror swaps left and right'), ('up', 'reflections do not turn it '
                                                                                                  'sideways'),
                                     ('down', 'reflections in a vertical line do not change up and down')],
                            'Left and right swap in a vertical mirror.'),
                         tf('Flipping a shape over twice in the same mirror line brings it back to where it started.', True,
                            'The second flip undoes the first.'),
                         sa('How many quarter-turns clockwise bring a shape back to its starting position for the first time, '
                            'if the shape has no symmetry at all?', 'Quarter-turns:', '4', 'Four quarter-turns make a full turn.',
                            compute=lambda: str(next(q for q in range(1, 5) if normalize(rot(SH9, q)) == normalize(SH9)))),
                     ])],
             f1=FW('Combine turns and flips', 'Harder: sequences of moves and their single-move equivalents.', [
                 tf('Reflecting a shape in a vertical line and then in a horizontal line gives the same result as a half-turn.',
                    True, '(x, y) -> (-x, y) -> (-x, -y), which is a half-turn.',
                    check=lambda: normalize(mirror_h(mirror_v(SH9))) == normalize(rot(SH9, 2))),
                 mc('A shape is turned a quarter-turn clockwise three times. Which single move gives the same result?',
                    'a quarter-turn counterclockwise', [('a half-turn', 'three quarter-turns are 270 degrees, not 180'),
                                                         ('a quarter-turn clockwise', 'that is only one of the three turns'),
                                                         ('a reflection', 'turns never produce a mirror image of this shape')],
                    '270 degrees clockwise is the same as 90 degrees counterclockwise.',
                    check=lambda t: {'a quarter-turn counterclockwise': normalize(rot(SH9, 3)),
                                     'a half-turn': normalize(rot(SH9, 2)), 'a quarter-turn clockwise': normalize(rot(SH9, 1)),
                                     'a reflection': normalize(mirror_v(SH9))}[t] == normalize(rot(rot(rot(SH9, 1), 1), 1))),
                 mc('A word written in capital letters is turned a half-turn (180 degrees). ' + ROT_TEXT +
                    ' A half-turn also reverses the order of the letters. Which word looks exactly the same after the turn?',
                    'SOS', [('NOW', 'W is not on the list'), ('ZOO', 'turned, it reads OOZ'), ('MOM', 'M turns into W')],
                    'The word must read the same backward and use only listed letters: S, O, S.',
                    check=lambda w: all(c in ROT180_LETTERS for c in w) and w == w[::-1]),
                 q9_f1_mark(),
                 sa('A shape has no symmetry. How many different-looking positions can it be put in using turns AND flips '
                    '(on a grid, counting each distinct picture once)?', 'Positions:', '8',
                    '4 turns of the shape and 4 turns of its mirror image, all different when the shape has no symmetry.',
                    compute=lambda: str(len(set(rotations(SH9)) | set(reflections(SH9))))),
             ]),
             f2=FW('Symmetry under turns and flips', 'Expert: count the moves that leave a figure unchanged and classify '
                                                    'shapes.', [
                 sa('Of the 8 moves of a square grid figure (4 turns: 0, 90, 180, 270 degrees; and 4 flips: vertical, '
                    'horizontal and both diagonals), how many leave a plus-shaped figure of 5 cells (a center cell with one '
                    'cell on each side) unchanged?', 'Moves:', '8', 'The plus shape has every symmetry of the square.',
                    compute=lambda: str(sum(1 for t in rotations(PLUS) + reflections(PLUS) if t == normalize(PLUS)))),
                 q9_f2_chiral(),
                 mc('An S-shaped figure of 4 cells (two cells in a row, and two more cells one row down, shifted one place left) '
                    'is turned and flipped. Which statement is true?', 'A half-turn leaves it unchanged, but no flip does.',
                    [('A quarter-turn leaves it unchanged.', 'a quarter-turn stands it upright'),
                     ('A flip in a vertical line leaves it unchanged.', 'that turns the S into a Z'),
                     ('No move other than doing nothing leaves it unchanged.', 'the half-turn also does')],
                    'The S shape has half-turn symmetry only.',
                    check=lambda t: {'A half-turn leaves it unchanged, but no flip does.': normalize(rot(S4, 2)) == normalize(S4)
                                     and normalize(S4) not in reflections(S4),
                                     'A quarter-turn leaves it unchanged.': normalize(rot(S4, 1)) == normalize(S4),
                                     'A flip in a vertical line leaves it unchanged.': normalize(mirror_v(S4)) == normalize(S4),
                                     'No move other than doing nothing leaves it unchanged.': normalize(rot(S4, 2)) != normalize(S4)}[t]),
                 tf('If a figure looks the same after a quarter-turn, then it also looks the same after a half-turn.', True,
                    'A half-turn is two quarter-turns; each leaves the figure unchanged.'),
                 sa('How many of the 7 shapes made of 4 grid cells joined edge to edge (counting a shape and its turns as the '
                    'same, but its mirror image as different) look the same after a half-turn?', 'Shapes:', '4',
                    'The 7 shapes: straight line, square, T, L, J, S, Z. Those unchanged by a half-turn: straight line, '
                    'square, S and Z.', compute=lambda: str(sum(1 for t in TETRO if normalize(rot(t, 2)) == normalize(t)))),
             ]))


PLUS = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}
S4 = {(0, 1), (0, 2), (1, 0), (1, 1)}
TETRO = [{(0, 0), (0, 1), (0, 2), (0, 3)}, {(0, 0), (0, 1), (1, 0), (1, 1)}, {(0, 0), (0, 1), (0, 2), (1, 1)},
         {(0, 0), (1, 0), (2, 0), (2, 1)}, {(0, 1), (1, 1), (2, 1), (2, 0)}, S4, {(0, 0), (0, 1), (1, 1), (1, 2)}]


def q9_f1_mark():
    given = {(1, 2), (2, 2), (3, 2), (3, 3)}
    img = sorted((5 - r, 5 - c) for r, c in given)       # half-turn about the center of a 4 x 4 grid
    g = figs.cells_canvas({(r - 1, c - 1) for r, c in given}, 4, 4)
    return markgrid('A 4 by 4 grid has shaded cells at (1,2), (2,2), (3,2) and (3,3), written as row,column with '
                    'row 1 at the top. The grid is given a half-turn about its center. Mark where the shaded cells end up.',
                    4, 4, img, 'A half-turn sends (r, c) to (5 - r, 5 - c): (4,3), (3,3), (2,3), (2,2).',
                    fig=(g.svg(), 'A 4 by 4 grid with an L shape of four shaded cells.'),
                    method='Automatic: each cell mapped by (r, c) -> (5 - r, 5 - c).')


def q9_f2_chiral():
    shapes = {'A': {(0, 0), (0, 1), (0, 2), (1, 0)},             # L: mirror image is not a turn
              'B': {(0, 0), (0, 1), (0, 2), (1, 1)},             # T: mirror image is a turn
              'C': {(0, 0), (0, 1), (1, 1), (1, 2)},             # Z: mirror image (S) is not a turn
              'D': {(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)}}     # W-like: mirror is a turn
    ok = {L: normalize(mirror_v(s)) in rotations(s) for L, s in shapes.items()}
    target = [L for L in 'ABCD' if ok[L]]
    items = [figs.cells_canvas(s, 3, 3) for s in shapes.values()]
    return mc('For which figure can the mirror image be produced by turning the figure (without flipping it over)? Exactly '
              'two of the four figures have this property; choose the answer that names both.',
              ' and '.join(target),
              [('A and C', 'their mirror images cannot be produced by any turn'), ('A and B', 'A\'s mirror image cannot be '
                                                                                         'produced by a turn'),
               ('C and D', 'C\'s mirror image cannot be produced by a turn')],
              'A figure\'s mirror image is a turn of it exactly when the figure has a mirror line itself. B (a T) and D (a '
              'staircase) each have a mirror line; A (an L) and C (a Z) do not.',
              fig=(choice_figure(items, list('ABCD')), 'Four small shapes made of cells, labeled A to D.'),
              check=lambda t: t == ' and '.join(target))


# ------------------------------------------------------------------ Set 10: deduction and induction
def s10():
    return S(10, 'Tell deductive conclusions from inductive ones',
             main=[
                 mc('Which argument is a valid DEDUCTIVE argument (its conclusion must be true whenever its premises are true)?',
                    'Every prime number greater than 2 is odd. 31 is a prime number greater than 2. So 31 is odd.',
                    [('The last 20 buses were on time. So the next bus will be on time.', 'past cases make the conclusion '
                                                                                         'likely, not certain'),
                     ('Every swan I have seen is white. So all swans are white.', 'a pattern in examples (induction)'),
                     ('Most students like recess. So Ana likes recess.', '"most" gives probability, not certainty')],
                    'Only the first conclusion is forced by its premises; the others generalize from examples or from "most".'),
                 mc('"1 + 3 = 4, 1 + 3 + 5 = 9, 1 + 3 + 5 + 7 = 16. So the sum of the first n odd numbers is always n x n." '
                    'What kind of reasoning is this?', 'inductive: it generalizes from a few examples',
                    [('deductive: the examples prove it for every n', 'checking a few cases does not prove every case'),
                     ('neither: it is not an argument', 'it gives reasons for a conclusion'),
                     ('deductive: the conclusion is true', 'a true conclusion does not make the reasoning deductive')],
                    'The pattern is in fact true, but the argument only checks three cases: that is inductive reasoning.'),
                 tf('In an inductive argument, the premises can all be true while the conclusion is false.', True,
                    'Induction makes the conclusion likely, not certain; a new case can break the pattern.'),
                 mc('n x n + n + 11 is prime for n = 1, 2, 3, ..., 9. A student concludes it is prime for every whole number n. '
                    'Which value of n shows the conclusion is false?', '10',
                    [('8', '64 + 8 + 11 = 83 is prime'), ('4', '16 + 4 + 11 = 31 is prime'),
                     ('9', '81 + 9 + 11 = 101 is prime')],
                    '10 x 10 + 10 + 11 = 121 = 11 x 11, which is not prime, so the conclusion is false.',
                    check=lambda t: not all((int(t) ** 2 + int(t) + 11) % d for d in range(2, int(t) ** 2 + int(t) + 11))),
                 mc('Which conclusion follows DEDUCTIVELY from "All members of the chess club are in grade 10 or grade 11, and '
                    'Jun is a member of the chess club"?', 'Jun is in grade 10 or grade 11.',
                    [('Jun is in grade 11.', 'he could be in grade 10'), ('Jun is good at chess.', 'not stated'),
                     ('Most grade 10 students are in the chess club.', 'not stated')],
                    'Only this conclusion is forced by the premises.'),
             ],
             back=[
                 B('Premises and conclusions', 'prerequisite', 'Classifying reasoning needs the premises and the conclusion '
                                                              'to be identified first.', outcome='LOGIC.ARGUMENT.01', qs=[
                     mc('"All the cookies are gone, so someone ate them." Which part is the conclusion?', 'someone ate them',
                        [('all the cookies are gone', 'the reason given'), ('cookies are tasty', 'not stated'),
                         ('nobody ate them', 'the opposite of the conclusion')], '"So" introduces the conclusion.'),
                     tf('A premise is the statement that an argument is trying to prove.', False, 'The statement an argument tries to prove is its conclusion; premises are the reasons offered for it.'),
                     mc('"It rained every day this week. So it will rain tomorrow." What is the premise?',
                        'It rained every day this week.', [('It will rain tomorrow.', 'the conclusion'),
                                                           ('Rain is good for plants.', 'not stated'),
                                                           ('It never rains.', 'not stated')], 'The reason given first.'),
                     tf('Every argument has at least one premise and one conclusion.', True, 'That is what makes it an argument.'),
                     mc('"Since 12 is even, 12 is divisible by 2." What is the conclusion?', '12 is divisible by 2',
                        [('12 is even', 'the reason after "since"'), ('12 is odd', 'false and not stated'),
                         ('2 is even', 'not stated')], 'The claim supported by the reason.'),
                 ]),
                 B('Certain or only likely?', 'prerequisite', 'Deduction aims to make the conclusion '
                                                             'certain; induction only makes it likely. Students need to judge certainty first.',
                   qs=[
                       tf('"The sun has risen every morning on record, so it will rise tomorrow" has a conclusion that is certain, '
                          'not just likely.', False, 'A past pattern makes the conclusion very likely, but the premises do not '
                          'guarantee it. That is an inductive argument.'),
                       tf('"Most tickets in the box are red, and I drew a ticket" makes "my ticket is red" certain.', False,
                          'It is likely, not certain.'),
                       mc('Which word signals that a conclusion is only likely?', 'probably',
                          [('must', 'signals certainty'), ('therefore', 'signals a conclusion, not its strength'),
                           ('every', 'a premise word')], '"Probably" marks a likely conclusion.'),
                       tf('If a pattern holds for 100 examples, it must hold for the 101st.', False,
                          'Examples alone never guarantee the next case.'),
                       mc('A die has been rolled 5 times and showed an even number each time. Which conclusion is certain?',
                          'Each of those 5 rolls was even.', [('The next roll will be even.', 'not certain'),
                                                              ('The die only has even numbers.', 'not certain'),
                                                              ('The die is unfair.', 'not certain')],
                          'Only the statement about what already happened is certain.'),
                   ]),
             ],
             f1=FW('Patterns that break', 'Harder: test generalizations that hold for many cases and then fail.', [
                 values('The claim "n x n - n + 17 is prime for every whole number n" holds for n = 1 to 16. Find a whole number '
                        'n that makes n x n - n + 17 NOT prime.', [('n', 'n =')],
                        'not isPrime(n*n - n + 17) and n >= 1 and isInteger(n)', {'n': 17},
                        'For n = 17: 17 x 17 - 17 + 17 = 289 = 17 x 17. Other values also work (for example 18: 323 = 17 x 19).',
                        wrong=[{'n': 1}, {'n': 5}, {'n': 16}], search={'n': range(1, 40)}),
                 mc('Points are placed on a circle and every pair is joined by a straight line. With 1, 2, 3, 4, 5 points (in '
                    'general position), the circle is cut into 1, 2, 4, 8, 16 regions. A student predicts 32 regions for 6 '
                    'points. What is the actual number?', '31', [('32', 'the doubling pattern breaks at 6 points'),
                                                                 ('30', 'one too few'), ('36', 'not the count')],
                    'The region count is 1 + C(n, 2) + C(n, 4): for n = 6, 1 + 15 + 15 = 31. The early pattern of doubling '
                    'was only inductive evidence.', check=lambda t: int(t) == 1 + 15 + 15),
                 tf('A valid deductive argument with true premises can have a false conclusion.', False,
                    'In a valid deductive argument, true premises guarantee a true conclusion.'),
                 mc('Which statement is the strongest inductive argument?',
                    'All 500 randomly chosen bolts from the batch passed, so nearly all bolts in the batch pass.',
                    [('My two friends like the song, so everyone does.', 'two hand-picked examples'),
                     ('The first bolt passed, so all bolts pass.', 'one example'),
                     ('All bolts in the batch passed, so this bolt passed.', 'that is deductive, not inductive')],
                    'A large random sample gives the strongest support for a general claim about the batch.'),
                 mc('Which reasoning is deductive?', 'All squares are rectangles; this figure is a square; so it is a rectangle.',
                    [('This figure looks like a rectangle, so it probably is one.', 'based on appearance'),
                     ('Every rectangle I measured had equal diagonals, so all rectangles do.', 'from measured examples'),
                     ('Most rectangles in the book are squares, so this one is.', 'from "most"')],
                    'Only the first is forced by its premises.'),
             ]),
             f2=FW('From pattern to proof', 'Expert: tell when a pattern has been proved and find the exact failure point.', [
                 sa('The expression n x n + n + 41 is prime for n = 0, 1, 2, ..., 39. What is the smallest whole number n for '
                    'which it is NOT prime?', 'n =', '40', 'n = 40 gives 1681 = 41 x 41.',
                    compute=lambda: str(next(n for n in range(0, 100) if any((n * n + n + 41) % d == 0
                                                                               for d in range(2, int((n * n + n + 41) ** .5) + 1))))),
                 mc('"For every whole number n, n x n - n is even, because 2 x 2 - 2 = 2, 3 x 3 - 3 = 6 and 4 x 4 - 4 = 12 are '
                    'even." Which statement about this argument is correct?',
                    'The claim is true, but three examples do not prove it.',
                    [('The argument proves the claim, because three cases are checked.', 'cases do not prove every n'),
                     ('The claim is false, because 1 x 1 - 1 = 0.', '0 is even'),
                     ('The claim is false for large n.', 'n(n - 1) is always even')],
                    'n x n - n = n(n - 1) is a product of two consecutive whole numbers, one of them even, so the claim is '
                    'true; but the argument only checks examples, which does not prove it for every n.'),
                 tf('If every case of a finite list has been checked, the conclusion about that list is deductive.', True,
                    'Checking ALL cases of a finite list is a complete proof (proof by cases).'),
                 values('Give a whole number n from 1 to 20 for which "2 to the power n, minus 1, is prime" is FALSE, even though '
                        'n is prime. (2 to the power n is 2 multiplied by itself n times.)', [('n', 'n =')],
                        'isPrime(n) and not isPrime(2^n - 1) and n <= 20', {'n': 11},
                        '2 to the 11th minus 1 = 2047 = 23 x 89. The pattern "n prime gives 2^n - 1 prime" holds for 2, 3, 5, 7 '
                        'but fails at 11, the only such n up to 20.', wrong=[{'n': 7}, {'n': 5}, {'n': 4}], search={'n': range(1, 21)}),
                 mc('A student checks that every whole number from 4 to 100 that is even can be written as a sum of two primes. '
                    'Which conclusion is justified?', 'Every even number from 4 to 100 is a sum of two primes.',
                    [('Every even number greater than 2 is a sum of two primes.', 'checking up to 100 does not cover all even '
                                                                                 'numbers'),
                     ('No odd number is a sum of two primes.', '2 + 3 = 5'),
                     ('Every even number is a sum of two primes.', '2 is even and is not a sum of two primes')],
                    'Only the statement about the checked range is established.'),
             ]))


# ------------------------------------------------------------------ Set 11: the structure of words
def alpha(w):
    return list(w) == sorted(w)


NUMWORDS = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN']


def s11():
    return S(11, 'Use letter counts, positions and order to test word patterns',
             main=[
                 mc('Which word has its letters in alphabetical order (each letter the same as or later in the alphabet than '
                    'the one before)?', 'ALMOST', [('BEGAN', 'A comes after G'), ('FLOWER', 'E comes after W in the word but '
                                                                                               'before W in the alphabet'),
                                                   ('CHART', 'A comes after H')],
                    'A, L, M, O, S, T are in alphabetical order.', check=alpha),
                 sa('How many times does the letter S appear in the word ASSESSMENTS?', 'Count:', '5',
                    'A S S E S S M E N T S: positions 2, 3, 5, 6 and 11.', compute=lambda: str('ASSESSMENTS'.count('S'))),
                 mc('Number words are written in capital letters (ONE, TWO, ..., TEN). Which number word has exactly as many '
                    'letters as the number it names?', 'FOUR', [('FIVE', '4 letters, value 5'), ('THREE', '5 letters, value 3'),
                                                                ('TWO', '3 letters, value 2')],
                    'F-O-U-R has 4 letters.', check=lambda w: len(w) == NUMWORDS.index(w) + 1),
                 mc('Take the first letter of each word: "Every Apple Tastes Sweet." What word do the first letters spell?',
                    'EATS', [('EAST', 'the order is E, A, T, S'), ('SEAT', 'the letters must stay in order'),
                             ('TEAS', 'the letters must stay in order')], 'E, A, T, S in order: EATS.',
                    check=lambda w: w == ''.join(x[0] for x in 'Every Apple Tastes Sweet'.split())),
                 mc('Write the letters of STEAM in alphabetical order. Which letter is in the middle position?', 'M',
                    [('E', 'E is 2nd'), ('A', 'A is 1st'), ('S', 'S is 4th')], 'A, E, M, S, T: the 3rd letter is M.',
                    check=lambda L: sorted('STEAM')[2] == L),
             ],
             back=[B('Strategy: list the letters with their positions', 'guided_strategy',
                     'Students misjudge word patterns by eye. Writing each letter with its position number turns the pattern '
                     'into something that can be checked one step at a time.',
                     lesson=lesson('List the letters with their positions',
                                   ['Write the word in capitals with a position number under each letter: 1, 2, 3, ...',
                                    'For "alphabetical order", compare each letter only with the one before it.',
                                    'For counting, mark each match as you find it, then count the marks.',
                                    'For first letters or acrostics, write the first letter of each word in order before reading '
                                    'the result.'],
                                   'Worked example (a different word)',
                                   ['Is GHOST in alphabetical order? How many times does O appear in COOKBOOK?'],
                                   ['G(1) H(2) O(3) S(4) T(5): G <= H, H <= O, O <= S, S <= T. Yes, in order.',
                                    'C O O K B O O K: O at positions 2, 3, 6, 7. O appears 4 times.']),
                     qs=[
                         tf('The letters of BELLOW are in alphabetical order.', True, 'B, E, L, L, O, W: each the same as or later '
                                                                                     'than the one before.',
                            check=lambda: alpha('BELLOW')),
                         sa('How many times does the letter E appear in REFERENCE?', 'Count:', '4', 'R E F E R E N C E.',
                            compute=lambda: str('REFERENCE'.count('E'))),
                         mc('What is the 4th letter of the word PLANET?', 'N', [('A', 'the 3rd letter'), ('E', 'the 5th letter'),
                                                                                ('L', 'the 2nd letter')], 'P L A N.',
                            check=lambda L: 'PLANET'[3] == L),
                         mc('Take the first letter of each word: "Owls Watch Lakes." What do the first letters spell?', 'OWL',
                            [('LOW', 'the order changed'), ('OLW', 'the letters are out of order'),
                             ('WOL', 'the order changed')], 'O, W, L.'),
                         sa('How many letters does the word EIGHT have?', 'Letters:', '5', 'E I G H T.', compute=lambda: str(len('EIGHT'))),
                     ])],
             f1=FW('Patterns across several words', 'Harder: patterns that link words in a list.', [
                 mc('In the list GO, CAT, LAMP, PLANT, each word has one more letter than the word before. Which word could come '
                    'next?', 'GARDEN', [('HOUSE', '5 letters'), ('BALLOON', '7 letters'), ('TREE', '4 letters')],
                    'GO has 2 letters, CAT 3, LAMP 4, PLANT 5, so the next word needs 6 letters.',
                    check=lambda w: len(w) == 6),
                 sa('How many of the number words ONE, TWO, THREE, ..., TEN have their letters in alphabetical order?',
                    'Count:', '0', 'Check each: none of them is in alphabetical order (for example ONE: N comes before O).',
                    compute=lambda: str(sum(alpha(w) for w in NUMWORDS))),
                 mc('Which word has its letters in strictly reverse alphabetical order (each letter earlier in the alphabet '
                    'than the one before it)?', 'SPOKE', [('STONE', 'T comes after S'), ('TRACK', 'C comes after A'),
                                                          ('SPELL', 'L comes after E')],
                    'S, P, O, K, E: each letter comes earlier in the alphabet than the one before it.',
                    check=lambda w: all(a > b for a, b in zip(w, w[1:]))),
                 sa('Write the letters of each number word ONE to TEN in alphabetical order; for example, ONE becomes ENO. '
                    'Which number word becomes EENSV? Give its value as a number.', 'Value:', '7',
                    'SEVEN sorted: E, E, N, S, V. No other number word has these letters.',
                    compute=lambda: str([NUMWORDS.index(w) + 1 for w in NUMWORDS if ''.join(sorted(w)) == 'EENSV'][0])),
                 tf('Every word whose letters are in alphabetical order reads differently backward unless all its letters are '
                    'the same.', True, 'Backward it is in reverse order; the two orders agree only if no two letters differ.'),
             ]),
             f2=FW('Count and construct letter strings under rules', 'Expert: count every string that follows a rule.', [
                 sa('How many 3-letter strings can be made from the letters A, B, C, D (letters may repeat) whose letters are in '
                    'alphabetical order (each letter the same as or later than the one before)?', 'Strings:', '20',
                    'Choosing a multiset of 3 letters from 4 kinds: C(6, 3) = 20.',
                    compute=lambda: str(sum(1 for w in itertools.product('ABCD', repeat=3) if list(w) == sorted(w)))),
                 sa('How many 4-letter strings using only the letters X and Y have no two equal letters next to each other?',
                    'Strings:', '2', 'They must alternate: XYXY or YXYX.',
                    compute=lambda: str(sum(1 for w in itertools.product('XY', repeat=4) if all(a != b for a, b in zip(w, w[1:]))))),
                 sa('How many 4-letter strings using the letters A, B, C (letters may repeat) have no letter next to itself?',
                    'Strings:', '24', '3 choices for the first letter, then 2 for each of the next three: 3 x 2 x 2 x 2 = 24.',
                    compute=lambda: str(sum(1 for w in itertools.product('ABC', repeat=4) if all(a != b for a, b in zip(w, w[1:]))))),
                 mc('A 6-letter string uses each of the letters A, B, C exactly twice, and no letter is next to itself. Which '
                    'string follows the rule?', 'ABCABC', [('AABBCC', 'equal letters are next to each other'),
                                                           ('ABBCAC', 'B is next to B'), ('ACBBCA', 'B is next to B')],
                    'Check neighbors: A-B, B-C, C-A, A-B, B-C are all different.',
                    check=lambda w: sorted(w) == sorted('AABBCC') and all(a != b for a, b in zip(w, w[1:]))),
                 sa('The five letters of LEVEL (L, E, V, E, L) are rearranged into 5-letter strings. How many different '
                    'strings have no two equal letters next to each other?', 'Strings:', '12',
                    'Place V first. V at either end: the other four positions are in a row and must alternate (LELE or ELEL), '
                    '2 ways each, so 4. V in the middle: positions 1-2 and 4-5 each need one L and one E, 2 x 2 = 4 ways. V 2nd '
                    'or 4th: the single end letter is L or E and the three positions on the other side must alternate starting '
                    'with the other letter, 2 ways each, so 4. Total 4 + 4 + 4 = 12.',
                    compute=lambda: str(len({p for p in itertools.permutations('LEVEL') if all(a != b for a, b in zip(p, p[1:]))}))),
             ]))


# ------------------------------------------------------------------ Set 12: conditionals
def imp(p, q):
    return (not p) or q


def s12():
    return S(12, 'Find when a conditional is true and the one case that makes it false',
             main=[
                 mc('A rule: "If a package weighs more than 5 kg, then it has a yellow label." Which package BREAKS the rule?',
                    'a 7 kg package with a blue label',
                    [('a 3 kg package with a yellow label', 'the rule says nothing about light packages'),
                     ('a 3 kg package with a blue label', 'light packages may have any label'),
                     ('a 7 kg package with a yellow label', 'this follows the rule')],
                    'A conditional is false only when the "if" part is true and the "then" part is false: heavy and not yellow.'),
                 tt('Complete the truth table for "if P then Q".', ['P', 'Q'], [('if P then Q', imp)],
                    'It is false only in the row P true, Q false.'),
                 values('Find a whole number n that is a counterexample to "If n is odd, then n is prime." (A counterexample '
                        'makes the "if" part true and the "then" part false.)', [('n', 'n =')],
                        'isOdd(n) and not isPrime(n) and n >= 1', {'n': 9},
                        'Any odd number that is not prime works: 1, 9, 15, 21, 25, ...', wrong=[{'n': 7}, {'n': 4}, {'n': 2}]),
                 tf('"If 5 > 8, then 2 + 2 = 5" is true.', True,
                    'The "if" part is false, so the conditional is true (it makes no promise when the "if" part is false).',
                    check=lambda: imp(5 > 8, 2 + 2 == 5)),
                 mc('"If it is a weekend day, the library opens at noon." Today the library opened at 9 a.m. What follows?',
                    'Today is not a weekend day.', [('Today is a weekend day.', 'then it would have opened at noon'),
                                                    ('The rule was broken.', 'the rule allows 9 a.m. on weekdays'),
                                                    ('Nothing follows.', 'the contrapositive gives a conclusion')],
                    'If it were a weekend day, the library would have opened at noon. It did not, so it is not a weekend day.'),
             ],
             back=[
                 B('Find the "if" part and the "then" part', 'prerequisite',
                   'Students who cannot split a conditional into hypothesis and conclusion cannot find the case that breaks '
                   'it.', qs=[
                       mc('In "If the sun sets, the street lights turn on," what is the "if" part (the hypothesis)?',
                          'the sun sets', [('the street lights turn on', 'that is the "then" part'),
                                           ('the lights are bright', 'not stated'), ('it is night', 'not stated')],
                          'The part after "if".'),
                       mc('In "Students may enter the lab only if they wear goggles," which is the "then" part when it is written '
                          'as "If ..., then ..."?', 'they wear goggles', [('students enter the lab', 'that becomes the "if" '
                                                                                                   'part'),
                                                                          ('the lab is open', 'not stated'),
                                                                          ('they leave the lab', 'not stated')],
                          '"A only if B" means "if A, then B": if a student enters, the student wears goggles.'),
                       mc('Rewrite "Every multiple of 10 ends in 0" as a conditional.',
                          'If a number is a multiple of 10, then it ends in 0.',
                          [('If a number ends in 0, then it is a multiple of 10.', 'the parts are swapped'),
                           ('If a number is not a multiple of 10, then it does not end in 0.', 'that changes the meaning'),
                           ('A number ends in 0 and is a multiple of 10.', 'not a conditional')],
                          '"Every A is B" means "if something is A, then it is B".'),
                       tf('In "If x = 3, then x + 1 = 4," the hypothesis is "x + 1 = 4".', False, 'The hypothesis is "x = 3".'),
                       mc('In "The alarm rings whenever the door opens," which part is the hypothesis?', 'the door opens',
                          [('the alarm rings', 'the conclusion'), ('the alarm is loud', 'not stated'),
                           ('the door closes', 'not stated')], '"Whenever the door opens" = "if the door opens".'),
                   ]),
                 B('Truth values of the parts', 'prerequisite', 'Judging a conditional requires judging each part.',
                   outcome='LOGIC.CONNECTIVE.01', qs=[
                       tf('"6 is a factor of 30" is true.', True, '30 = 6 x 5.', check=lambda: 30 % 6 == 0),
                       tf('"4 squared is 8" is true.', False, '4 x 4 = 16.'),
                       tf('"Every square is a triangle" is true.', False, 'A square has 4 sides.'),
                       mc('Which statement is true?', '-5 is less than 2.', [('2 is less than -5.', '2 is to the right of -5 on the number line, so it is greater'),
                                                                            ('-5 is greater than 2.', '-5 is to the left of 2 on the number line, so it is less'),
                                                                            ('-5 equals 5.', '-5 and 5 are on opposite sides of 0')], 'On a number line -5 '
                                                                                                         'is left of 2.'),
                       tf('"1 is a prime number" is true.', False, 'A prime has exactly two different factors; 1 has one.'),
                   ]),
             ],
             f1=FW('Conditionals in mathematics', 'Harder: conditionals with variables, domains and false hypotheses.', [
                 values('Find a real number x that makes "If x squared is greater than 9, then x is greater than 3" FALSE.',
                        [('x', 'x =')], 'x^2 > 9 and not (x > 3)', {'x': -4},
                        'The conditional is false when x squared > 9 but x ≤ 3: any x < -3 works, for example -4.',
                        wrong=[{'x': 4}, {'x': 2}, {'x': -3}]),
                 tf('"If a whole number is divisible by 6, then it is divisible by 3" is true for every whole number.', True,
                    '6 = 2 x 3, so a multiple of 6 is a multiple of 3. No case has the "if" true and the "then" false.',
                    check=lambda: all(imp(n % 6 == 0, n % 3 == 0) for n in range(1, 500))),
                 sa('For how many whole numbers n from 1 to 12 is "If n is even, then n is a multiple of 4" FALSE?',
                    'Count:', '3', 'False when n is even but not a multiple of 4: 2, 6, 10.',
                    compute=lambda: str(sum(1 for n in range(1, 13) if not imp(n % 2 == 0, n % 4 == 0)))),
                 mc('P is false. Which statement MUST be true?', 'If P then Q', [('If Q then P', 'false when Q is true'),
                                                                                ('P and Q', 'false because P is false'),
                                                                                ('Q', 'not determined')],
                    'A conditional with a false "if" part is always true.',
                    check=lambda t: all({'If P then Q': imp(False, q), 'If Q then P': imp(q, False), 'P and Q': False and q,
                                         'Q': q}[t] for q in (True, False))),
                 mc('"If you score above 90, you earn a badge." Lin earned a badge. What follows?', 'Nothing about Lin\'s score '
                                                                                                  'follows.',
                    [('Lin scored above 90.', 'the rule does not say badges come only from scores above 90'),
                     ('Lin scored 90 or below.', 'not supported'), ('The rule was broken.', 'earning a badge breaks nothing')],
                    'The rule only says what happens above 90; badges may be earned in other ways.'),
             ]),
             f2=FW('Nested and chained conditionals', 'Expert: conditionals inside conditionals and their truth tables.', [
                 tt('Complete the truth table for "if P then (if Q then R)".', ['P', 'Q', 'R'],
                    [('if Q then R', lambda p, q, r: imp(q, r)), ('if P then (if Q then R)', lambda p, q, r: imp(p, imp(q, r)))],
                    'It is false only when P and Q are true and R is false.'),
                 sa('In how many of the 8 rows of a truth table for P, Q, R is "(if P then Q) and (if Q then R)" true?',
                    'Rows:', '4', 'Check all 8 rows; it is true in TTT, FTT, FFT, FFF.',
                    compute=lambda: str(sum(1 for p, q, r in itertools.product([True, False], repeat=3) if imp(p, q) and imp(q, r)))),
                 tf('"If P then (if Q then R)" has the same truth value as "if (P and Q) then R" in every row.', True,
                    'Both are false exactly when P and Q are true and R is false.',
                    check=lambda: all(imp(p, imp(q, r)) == imp(p and q, r) for p, q, r in itertools.product([True, False], repeat=3))),
                 tf('"If P then (if Q then R)" has the same truth value as "if (if P then Q) then R" in every row.', False,
                    'Row P false, Q false, R false: the first is true, but "if P then Q" is true and R false, so the second is '
                    'false.', check=lambda: all(imp(p, imp(q, r)) == imp(imp(p, q), r) for p, q, r in itertools.product([True, False], repeat=3))),
                 values('Find whole numbers a and b that make the statement "If a + b is even, then a and b are both even" FALSE.',
                        [('a', 'a ='), ('b', 'b =')], 'isEven(a + b) and not (isEven(a) and isEven(b)) and isInteger(a) and isInteger(b)',
                        {'a': 3, 'b': 5}, 'Two odd numbers have an even sum: for example 3 + 5 = 8.',
                        wrong=[{'a': 2, 'b': 4}, {'a': 2, 'b': 3}], search={'a': range(0, 10), 'b': range(0, 10)}),
             ]))


SETS = [s9(), s10(), s11(), s12()]
