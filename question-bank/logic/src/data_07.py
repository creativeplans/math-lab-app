"""Logic sets 19-22: tautologies and equivalence; stacking and occlusion; valid inference forms; invalid forms."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt
import figs
import pz

TF = [True, False]


def imp(p, q):
    return (not p) or q


def kind(f, n):
    vals = [f(*v) for v in itertools.product(TF, repeat=n)]
    return 'tautology' if all(vals) else 'contradiction' if not any(vals) else 'contingency'


def equiv(f, g, n=2):
    return all(f(*v) == g(*v) for v in itertools.product(TF, repeat=n))


# ------------------------------------------------------------------ Set 19: tautology, contradiction, equivalence
F19 = {'P or not P': (lambda p: p or not p, 1), 'P and not P': (lambda p: p and not p, 1),
       'if P then Q': (lambda p, q: imp(p, q), 2), 'P or Q': (lambda p, q: p or q, 2),
       '(P and Q) or not P or not Q': (lambda p, q: (p and q) or not p or not q, 2),
       'P and Q and not Q': (lambda p, q: p and q and not q, 2), '(if P then Q) or (if Q then P)': (lambda p, q: imp(p, q) or imp(q, p), 2),
       'P iff not P': (lambda p: p == (not p), 1)}


def s19():
    return S(19, 'Classify statements as tautologies, contradictions or contingencies, and test equivalence',
             main=[
                 mc('Which statement is a TAUTOLOGY (true in every row of its truth table)?', '(P and Q) or not P or not Q',
                    [('P or Q', 'false when both are false'), ('if P then Q', 'false when P is true and Q false'),
                     ('P and Q and not Q', 'false in every row')],
                    'If P and Q are both true, the first bracket is true; otherwise "not P or not Q" is true. So it is always true.',
                    check=lambda t: kind(*F19[t]) == 'tautology'),
                 mc('Which statement is a CONTRADICTION (false in every row)?', 'P and Q and not Q',
                    [('P or not P', 'a tautology'), ('if P then Q', 'a contingency'), ('P or Q', 'a contingency')],
                    'Q and not Q can never both be true.', check=lambda t: kind(*F19[t]) == 'contradiction'),
                 tt('Complete the truth table for "(if P then Q) or (if Q then P)".', ['P', 'Q'],
                    [('if P then Q', imp), ('if Q then P', lambda p, q: imp(q, p)),
                     ('(if P then Q) or (if Q then P)', lambda p, q: imp(p, q) or imp(q, p))],
                    'In every row at least one of the two conditionals is true, so the last column is all T: a tautology.'),
                 tf('"not (P and Q)" is logically equivalent to "(not P) or (not Q)".', True,
                    'Both are false only when P and Q are both true (De Morgan\'s law).',
                    check=lambda: equiv(lambda p, q: not (p and q), lambda p, q: (not p) or (not q))),
                 mc('How is "if P then Q" classified?', 'a contingency: true in some rows and false in one',
                    [('a tautology', 'it is false when P is true and Q false'), ('a contradiction', 'it is true in three rows'),
                     ('neither true nor false', 'every row has a value')],
                    'It is false only in the row P true, Q false, so it is a contingency.',
                    check=lambda t: t.startswith('a contingency') and kind(imp, 2) == 'contingency'),
             ],
             back=[
                 B('Fill in truth tables', 'prerequisite', 'Classifying a statement means reading its whole column; students '
                                                         'need to build the column first.', outcome='LOGIC.TRUTH.01', qs=[
                     tt('Complete the truth table for "P or not P".', ['P'], [('not P', lambda p: not p), ('P or not P', lambda p: p or not p)],
                        'Always true.'),
                     tt('Complete the truth table for "P and not P".', ['P'], [('not P', lambda p: not p), ('P and not P', lambda p: p and not p)],
                        'Always false.'),
                     tt('Complete the truth table for "not P or Q".', ['P', 'Q'], [('not P or Q', lambda p, q: (not p) or q)],
                        'False only when P true and Q false.'),
                     sa('How many rows does a truth table for P and Q have?', 'Rows:', '4', '2 x 2.', compute=lambda: str(4)),
                     tf('A truth table for three statements P, Q and R has 6 rows.', False, 'Each of the 3 statements '
                        'can be true or false: 2 x 2 x 2 = 8 rows.'),
                 ]),
                 B('Always, never, sometimes', 'prerequisite', 'The three classes are just "always true", "never true" and '
                                                              '"sometimes true". Students need that link.', qs=[
                     mc('A statement is true in every row of its table. What is it called?', 'a tautology',
                        [('a contradiction', 'that is never true'), ('a contingency', 'that is sometimes true'),
                         ('a premise', 'a role in an argument, not a class')], 'Always true = tautology.'),
                     mc('A statement is false in every row. What is it called?', 'a contradiction',
                        [('a tautology', 'always true'), ('a contingency', 'sometimes true'), ('a conclusion', 'not a class')],
                        'Never true = contradiction.'),
                     tf('A contingency is true in every row of its truth table.', False, 'A statement true in every row is a tautology. A contingency is true in some rows and false in others.'),
                     mc('A column reads T, T, F, T. How is the statement classified?', 'a contingency',
                        [('a tautology', 'it has an F'), ('a contradiction', 'it has a T'), ('it cannot be told', 'the column '
                                                                                                                 'decides it')],
                        'Mixed values: contingency.'),
                     tf('"7 is odd and 7 is not odd" is true.', False,
                        'It has the form "P and not P", a contradiction: it is false in every case.'),
                 ]),
             ],
             f1=FW('Equivalences by truth table', 'Harder: prove and refute equivalences.', [
                 tt('Complete the table to compare "not (P or Q)" with "(not P) and (not Q)".', ['P', 'Q'],
                    [('not (P or Q)', lambda p, q: not (p or q)), ('(not P) and (not Q)', lambda p, q: (not p) and (not q))],
                    'The columns match: De Morgan\'s law.'),
                 tf('"if P then Q" is equivalent to "if Q then P".', False, 'They differ when exactly one of P, Q is true.',
                    check=lambda: equiv(imp, lambda p, q: imp(q, p))),
                 mc('Which statement is equivalent to "not (if P then Q)"?', 'P and not Q',
                    [('not P and not Q', 'true when both are false, but the original is false there'),
                     ('if not P then not Q', 'that is the inverse'), ('not P or Q', 'that is the conditional itself')],
                    '"if P then Q" is false exactly when P is true and Q false.',
                    check=lambda t: equiv(lambda p, q: not imp(p, q), {'P and not Q': lambda p, q: p and not q,
                                                                     'not P and not Q': lambda p, q: (not p) and (not q),
                                                                     'if not P then not Q': lambda p, q: imp(not p, not q),
                                                                     'not P or Q': lambda p, q: (not p) or q}[t])),
                 sa('How many of these are tautologies? "P or not P"; "P and not P"; "if P then Q"; "(if P then Q) or (if Q '
                    'then P)"; "P iff not P".', 'Tautologies:', '2', '"P or not P" and "(if P then Q) or (if Q then P)".',
                    compute=lambda: str(sum(kind(*F19[k]) == 'tautology' for k in
                                            ['P or not P', 'P and not P', 'if P then Q', '(if P then Q) or (if Q then P)', 'P iff not P']))),
                 tf('The negation of a tautology is also a tautology.', False, 'If a statement is true in every row, its negation '
                                                                            'is false in every row.'),
             ]),
             f2=FW('Laws of logic', 'Expert: use equivalences to simplify and to find hidden tautologies.', [
                 mc('Which statement is equivalent to "P or (P and Q)"?', 'P', [('Q', 'differs when P true, Q false'),
                                                                               ('P and Q', 'differs when P true, Q false'),
                                                                               ('P or Q', 'differs when P false, Q true')],
                    'If P is true, the statement is true; if P is false, both parts are false. So it equals P (absorption).',
                    check=lambda t: equiv(lambda p, q: p or (p and q), {'P': lambda p, q: p, 'Q': lambda p, q: q,
                                                                        'P and Q': lambda p, q: p and q,
                                                                        'P or Q': lambda p, q: p or q}[t])),
                 tf('"((if P then Q) and P) implies Q", written "if ((if P then Q) and P) then Q", is a tautology.', True,
                    'This is modus ponens written as one statement; it is true in all four rows.',
                    check=lambda: kind(lambda p, q: imp(imp(p, q) and p, q), 2) == 'tautology'),
                 tf('"if ((if P then Q) and Q) then P" is a tautology.', False,
                    'Row P false, Q true: the "if" part is true and P is false, so the statement is false (affirming the '
                    'consequent).', check=lambda: kind(lambda p, q: imp(imp(p, q) and q, p), 2) == 'tautology'),
                 sa('Of the 16 possible truth-table columns for statements in P and Q, how many are contingencies?',
                    'Contingencies:', '14', 'All 16 columns except all-T (tautology) and all-F (contradiction).',
                    compute=lambda: str(sum(1 for col in itertools.product(TF, repeat=4) if any(col) and not all(col)))),
                 mc('Which pair are equivalent?', '"if P then (Q and R)" and "(if P then Q) and (if P then R)"',
                    [('"if (P or Q) then R" and "(if P then R) or (if Q then R)"', 'P true, Q false, R false: the first is '
                                                                                  'false, the second true'),
                     ('"P and (Q or R)" and "(P and Q) or R"', 'P false, R true: the first is false, the second true'),
                     ('"not (P and Q)" and "not P and not Q"', 'P true, Q false: the first is true, the second false')],
                    'Both sides of the first pair are false exactly when P is true and at least one of Q, R is false.',
                    check=lambda t: {
                        '"if P then (Q and R)" and "(if P then Q) and (if P then R)"':
                            equiv(lambda p, q, r: imp(p, q and r), lambda p, q, r: imp(p, q) and imp(p, r), 3),
                        '"if (P or Q) then R" and "(if P then R) or (if Q then R)"':
                            equiv(lambda p, q, r: imp(p or q, r), lambda p, q, r: imp(p, r) or imp(q, r), 3),
                        '"P and (Q or R)" and "(P and Q) or R"':
                            equiv(lambda p, q, r: p and (q or r), lambda p, q, r: (p and q) or r, 3),
                        '"not (P and Q)" and "not P and not Q"':
                            equiv(lambda p, q, r: not (p and q), lambda p, q, r: (not p) and (not q), 3)}[t]),
             ]))


# ------------------------------------------------------------------ Set 20: stacking and occlusion
L1 = ({'A': (92, 58, 89, 79), 'B': (38, 18, 120, 67), 'C': (58, 82, 86, 87), 'D': (62, 7, 97, 56)}, ['B', 'C', 'A', 'D'])
L2 = ({'A': (101, 71, 113, 61), 'B': (67, 31, 78, 72), 'C': (59, 96, 126, 58), 'D': (12, 51, 118, 57)}, ['B', 'D', 'A', 'C'])
L3 = ({'A': (105, 31, 114, 82), 'B': (111, 68, 89, 88), 'C': (120, 26, 91, 77), 'D': (29, 19, 107, 65), 'E': (29, 81, 126, 82)},
      ['E', 'D', 'A', 'C', 'B'])
L4 = ({'A': (43, 54, 126, 77), 'B': (56, 9, 110, 93), 'C': (131, 13, 81, 81), 'D': (115, 70, 118, 87), 'E': (77, 31, 89, 90)},
      ['B', 'E', 'A', 'C', 'D'])
L5 = ({'A': (99, 50, 109, 71), 'B': (8, 64, 120, 88), 'C': (88, 11, 119, 70)}, ['B', 'C', 'A'])
L6 = ({'A': (56, 75, 116, 62), 'B': (131, 86, 78, 84), 'C': (23, 49, 74, 63), 'D': (28, 72, 103, 56)}, ['C', 'D', 'A', 'B'])
for _R, _o in (L1, L2, L3, L4, L5, L6):
    assert pz.stack_orders_matching(_R, _o) == [_o] and pz.labels_visible(_R, _o)

STACK_RULE = ('Rectangular paper sheets are lying flat, one on top of another, seen from directly above. Each sheet is white '
              'with a dark outline and a letter in its corner. A sheet hides the parts of the sheets under it.')


def stack_q(prompt, L, why):
    R, o = L
    fig = pz.stack_figure(R, o)
    items = [(k, 'sheet ' + k) for k in sorted(R)]
    return order(STACK_RULE + ' This stack has %d sheets: %s. ' % (len(R), ', '.join(sorted(R))) + prompt, items, lambda p: pz.top_map(R, list(p)) == pz.top_map(R, o), why, expect=o,
                 fig=(fig.svg(), 'Several overlapping rectangles labeled with letters, seen from above.'),
                 method='Automatic: every stacking order was drawn on a fine grid and compared with the picture.', unique=True)


def discs_visible(stack):
    """stack: list of (name, radius) bottom to top, all centered. A disc is visible if some disc above does not cover it."""
    vis = []
    for i, (n, r) in enumerate(stack):
        above = [rr for _, rr in stack[i + 1:]]
        if not above or max(above) < r:
            vis.append(n)
    return vis


def cards_visible(cards, n=8):
    """cards: list of (name, r1, c1, r2, c2) bottom to top on an n x n grid (inclusive cells)."""
    top = {}
    for name, r1, c1, r2, c2 in cards:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                top[(r, c)] = name
    return sorted(set(top.values()))


CARDS = [('A', 1, 1, 4, 4), ('B', 3, 3, 6, 6), ('C', 2, 2, 5, 5), ('D', 1, 4, 3, 7), ('E', 5, 1, 7, 3)]
CARDS_F = [('A', 2, 2, 3, 3), ('B', 1, 1, 4, 4), ('C', 4, 4, 6, 6), ('D', 1, 5, 2, 6), ('E', 3, 1, 6, 4)]


def s20():
    return S(20, 'Infer stacking order from what is visible',
             main=[
                 stack_q('Put the sheets in order from the BOTTOM sheet to the TOP sheet.', L5,
                         'Overlaps: B is under C, C is under A, B is under A. A\'s outline is complete, so A is on top; then C; '
                         'B is at the bottom: B, C, A.'),
                 stack_q('List the sheets starting with the one at the BOTTOM and ending with the one on TOP.', L1,
                         'At each overlap the cut-off outline is underneath: B is under C, A and D; C is under A; A is under D. '
                         'So the chain is B, C, A, D from bottom to top.'),
                 mc('Four round discs are stacked with their centers lined up, from bottom to top: W (radius 5 cm), X (radius 3 '
                    'cm), Y (radius 4 cm), Z (radius 1 cm). Looking straight down from above, which discs can be seen?',
                    'W, Y and Z', [('W, X, Y and Z', 'X is entirely covered by the larger disc Y above it'),
                                   ('Z only', 'larger discs below Z show around it'),
                                   ('W and Z', 'Y shows as a ring between radius 1 and 4 cm')],
                    'A disc can be seen if every disc above it is smaller. W: all above are smaller. X: Y (4 cm) is above and '
                    'larger, so X is hidden. Y: only Z (1 cm) is above. Z: on top.',
                    check=lambda t: t.replace(' and ', ', ').split(', ') == discs_visible([('W', 5), ('X', 3), ('Y', 4), ('Z', 1)])),
                 stack_q('Put the sheets in order from the BOTTOM sheet to the TOP sheet.', L6,
                         'Overlaps: C is under D and A; D is under A; A is under B. From bottom to top: C, D, A, B.'),
                 sa('Rectangular cards are placed one at a time on an 8 by 8 grid, each covering a block of cells (rows and columns '
                    'numbered 1 to 8; "rows 1-4, columns 1-4" means a 4 by 4 block). In order: A covers rows 1-4, columns 1-4; '
                    'B covers rows 3-6, columns 3-6; C covers rows 2-5, columns 2-5; D covers rows 1-3, columns 4-7; E covers '
                    'rows 5-7, columns 1-3. Seen from above, how many of the five cards can be seen at least partly?',
                    'Cards seen:', '5', 'Check each card for a cell not covered by a later card. A: cell (1,1). B: cell (6,6). '
                                        'C: cell (4,4). D and E are near the top of the pile and show fully or partly. All 5 '
                                        'can be seen.', compute=lambda: str(len(cards_visible(CARDS)))),
             ],
             back=[B('Strategy: the cut-off sheet is underneath', 'guided_strategy',
                     'Students guess the order from size or position. The rule "where two sheets overlap, the one whose '
                     'outline is cut off is underneath" settles each pair, and the pairs together give the order.',
                     lesson=lesson('The cut-off sheet is underneath',
                                   ['Look at one place where two sheets overlap.',
                                    'The sheet whose outline runs straight through the overlap is on top there. The sheet whose '
                                    'outline stops at the other sheet\'s edge is underneath.',
                                    'Record each pair as "X under Y". Then find the sheet that is under no other sheet: that is '
                                    'the top. Remove it and repeat.',
                                    'For stacks of centered discs, a disc shows only if every disc above it is smaller.'],
                                   'Worked example (different sheets)',
                                   ['Three sheets: the outline of K stops at the edge of M; the outline of M stops at the edge '
                                    'of J; the outline of K stops at the edge of J.'],
                                   ['Pairs: K under M, M under J, K under J.', 'J is under nothing: J is on top.',
                                    'Then M, then K at the bottom. Order from bottom to top: K, M, J.']),
                     qs=[
                         mc('Where sheets X and Y overlap, the outline of X runs straight through and the outline of Y stops at '
                            'X\'s edge. What follows?', 'Y is under X.', [('X is under Y.', 'the cut-off outline is the lower '
                                                                                            'one'),
                                                                         ('They are side by side.', 'they overlap'),
                                                                         ('It cannot be told.', 'the outlines decide it')],
                            'The sheet whose outline is cut off is underneath.'),
                         order('Pairs found: P under Q, Q under R, P under R. Order the sheets from bottom to top.',
                               [('P', 'sheet P'), ('Q', 'sheet Q'), ('R', 'sheet R')],
                               lambda p: p.index('P') < p.index('Q') < p.index('R'), 'P, Q, R.', expect=['P', 'Q', 'R'],
                               unique=True),
                         tf('A sheet whose whole outline can be seen must be on top of every sheet it overlaps.', True,
                            'If any sheet above it overlapped it, part of its outline would be hidden.'),
                         mc('Discs are stacked with centers lined up, from bottom to top: radius 2 cm, then 6 cm. Which can be '
                            'seen from above?', 'only the 6 cm disc', [('both discs', 'the larger disc above covers the '
                                                                                     'smaller one'),
                                                                       ('only the 2 cm disc', 'it is underneath'),
                                                                       ('neither disc', 'the top disc is visible')],
                            'The 6 cm disc covers the 2 cm disc completely.',
                            check=lambda t: discs_visible([('a', 2), ('b', 6)]) == ['b'] and t == 'only the 6 cm disc'),
                         sa('Five sheets are stacked. Exactly one of them is on top of all four others. How many sheets are '
                            'under it?', 'Sheets under it:', '4', 'All four others are under the top sheet.',
                            compute=lambda: str(5 - 1)),
                     ])],
             f1=FW('Larger stacks', 'Harder: five sheets and stacks described by numbers.', [
                 stack_q('Put the five sheets in order from the BOTTOM sheet to the TOP sheet.', L3,
                         'Every pair overlaps here. B is cut off by no sheet (top); C is cut off only by B; A by C and B; D by A, '
                         'C and B; E by all four. From bottom to top: E, D, A, C, B.'),
                 stack_q('List the five sheets starting with the BOTTOM sheet and ending with the TOP sheet.', L4,
                         'Every pair overlaps. D is cut off by no sheet (top); C only by D; A by C and D; E by A, C and D; B by '
                         'all four. From bottom to top: B, E, A, C, D.'),
                 sa('Cards are placed one at a time on an 8 by 8 grid: A covers rows 2-3, columns 2-3; B covers rows 1-4, '
                    'columns 1-4; C covers rows 4-6, columns 4-6; D covers rows 1-2, columns 5-6; E covers rows 3-6, columns '
                    '1-4. Seen from above, how many of the five cards can be seen at least partly?', 'Cards seen:', '4',
                    'A lies inside B and B was placed later, so A is hidden. B still shows in rows 1-2, columns 1-4. C shows in '
                    'columns 5-6 (E only covers column 4 of C). D and E show. So B, C, D and E: 4 cards.',
                    compute=lambda: str(len(cards_visible(CARDS_F)))),
                 mc('Four discs with centers lined up are stacked, bottom to top: radius 6, 2, 5, 3 (cm). How many can be seen '
                    'from above?', '3', [('4', 'the 2 cm disc is covered by the 5 cm disc above it'),
                                         ('2', 'the 5 cm disc shows as a ring outside the 3 cm disc'),
                                         ('1', 'larger discs below show around smaller ones')],
                    'Visible: 6 (nothing larger above), 5 (only 3 above), 3 (top). The 2 cm disc is under the 5 cm disc.',
                    check=lambda t: int(t) == len(discs_visible([('a', 6), ('b', 2), ('c', 5), ('d', 3)]))),
                 tf('If two sheets do not overlap at all, the picture from above cannot show which one is higher.', True,
                    'Nothing in the picture depends on their order.'),
             ]),
             f2=FW('How much does a picture tell?', 'Expert: count the orders a picture allows and design stacks.', [
                 sa('Three sheets: A and B do not overlap each other, and sheet C overlaps both and is on top of both. How many '
                    'different bottom-to-top orders are consistent with the picture from above?', 'Orders:', '2',
                    'C must be on top. A and B can be in either order below it: A, B, C or B, A, C.',
                    compute=lambda: str(len(pz.stack_orders_matching({'A': (15, 15, 90, 70), 'B': (130, 15, 90, 70),
                                                                      'C': (60, 60, 120, 90)}, ['A', 'B', 'C'])))),
                 mc('Discs of radius 1, 2, 3 and 4 cm are stacked with centers lined up. In which stacking order (bottom to top) '
                    'can ALL four discs be seen from above?', '4, 3, 2, 1', [('1, 2, 3, 4', 'only the top 4 cm disc shows'),
                                                                            ('4, 2, 3, 1', 'the 2 cm disc is under the 3 cm '
                                                                                           'disc'),
                                                                            ('3, 4, 2, 1', 'the 3 cm disc is under the 4 cm '
                                                                                           'disc')],
                    'Each disc must be larger than every disc above it: largest at the bottom.',
                    check=lambda t: len(discs_visible([(x, int(x)) for x in t.split(', ')])) == 4),
                 sa('Discs of radius 1, 2, 3 and 4 cm are stacked in some order with centers lined up. Over all 24 stacking '
                    'orders, in how many is EXACTLY one disc visible from above?', 'Orders:', '6',
                    'Exactly one disc shows when the 4 cm disc is on top. The other three can be in any order below: 3 x 2 x 1 '
                    '= 6.', compute=lambda: str(sum(1 for p in itertools.permutations([1, 2, 3, 4])
                                                    if len(discs_visible([(str(x), x) for x in p])) == 1))),
                 tf('From a picture of a stack of sheets, the TOP sheet can always be identified if every sheet overlaps at '
                    'least one other sheet.', False,
                    'Two separate piles (A under B, and C under D, with no overlap between the piles) have two sheets with '
                    'complete outlines, B and D, and the picture cannot tell which of them is the highest.'),
                 mc('Cards on a grid: P covers rows 1-3, columns 1-3; Q covers rows 2-4, columns 2-4. P was placed first. Which '
                    'cell shows card P?', 'row 1, column 2', [('row 3, column 3', 'covered by Q'),
                                                             ('row 2, column 2', 'covered by Q'),
                                                             ('row 4, column 4', 'that cell is only Q')],
                    'Q covers rows 2-4 and columns 2-4, so P shows in row 1 and in column 1.',
                    check=lambda t: (lambda r, c: 1 <= r <= 3 and 1 <= c <= 3 and not (2 <= r <= 4 and 2 <= c <= 4))(
                        int(t.split(',')[0].split()[1]), int(t.split(',')[1].split()[1]))),
             ]))


SETS = [s19(), s20()]
