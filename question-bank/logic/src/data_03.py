"""Logic sets 5-8: negation and truth values; codes; ordering from clues; and / inclusive or / exclusive or."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt


def pos(p, x):
    return p.index(x)


# ------------------------------------------------------------------ Set 5: negation and truth values
def s5():
    return S(5, 'Form negations and find truth values',
             main=[
                 mc('What is the negation of "Sam is taller than Ana"?', 'Sam is not taller than Ana.',
                    [('Ana is taller than Sam.', 'this leaves out the case where they are the same height'),
                     ('Sam is shorter than Ana.', 'this also leaves out equal heights'),
                     ('Sam and Ana are the same height.', 'this leaves out the case where Ana is taller')],
                    'A negation is true exactly when the original is false. "Sam is taller" is false when Sam is shorter OR '
                    'the same height; only "Sam is not taller than Ana" covers both.'),
                 mc('x stands for a real number. What is the negation of "x > 5"?', 'x ≤ 5',
                    [('x < 5', 'misses x = 5, where "x > 5" is false'), ('x ≥ 5', 'includes values like 6 that make "x > 5" true'),
                     ('x < -5', 'misses every x from -5 to 5')],
                    '"x > 5" is false exactly when x is 5 or less: x ≤ 5.',
                    check=lambda t: all((x > 5) != {'x ≤ 5': x <= 5, 'x < 5': x < 5, 'x ≥ 5': x >= 5, 'x < -5': x < -5}[t]
                                        for x in [i / 2 for i in range(-20, 21)])),
                 tf('P is the statement "48 is a multiple of 9." The negation of P is true.', True,
                    '48 = 9 x 5 + 3, so P is false and its negation, "48 is not a multiple of 9", is true.',
                    check=lambda: not (48 % 9 == 0)),
                 values('Give a number x that makes the NEGATION of the statement "x ≤ 4" true.', [('x', 'x =')], 'x > 4',
                        {'x': 7}, 'The negation of "x ≤ 4" is "x > 4", so any number greater than 4 is correct.',
                        wrong=[{'x': 4}, {'x': 3}, {'x': -5}]),
                 mc('Which pair of statements are negations of each other (in every situation, exactly one of the two is '
                    'true)?', '"The coin landed heads up." / "The coin did not land heads up."',
                    [('"The cup is full." / "The cup is empty."', 'a half-full cup makes both false'),
                     ('"Every student passed." / "Every student failed."', 'if some passed and some failed, both are false'),
                     ('"x > 3" / "x < 3"', 'x = 3 makes both false')],
                    'Negations can never be both false or both true. Each other pair has a situation where both are false: they '
                    'are opposites (contraries), not negations.'),
             ],
             back=[
                 B('Truth values of simple statements', 'prerequisite',
                   'To negate correctly, a student must first decide whether a statement is true or false. A student who '
                   'misjudges the original cannot judge its negation.', outcome='LOGIC.ARGUMENT.01', qs=[
                       tf('"17 is a prime number" is true.', True, '17 has no factors other than 1 and itself.',
                          check=lambda: all(17 % d for d in range(2, 17))),
                       tf('"3 x 7 = 24" is true.', False, '3 x 7 = 21.', check=lambda: 3 * 7 == 24),
                       tf('"Every even number is a multiple of 4" is true.', False, '6 is even but not a multiple of 4, so the statement is false.'),
                       mc('Which statement is false?', '0.5 is greater than 0.75.',
                          [('0.5 equals one half.', 'this is true: 0.5 = 1/2'), ('0.75 is greater than 0.5.', 'this is true: 75 hundredths > 50 hundredths'),
                           ('0.5 + 0.25 = 0.75.', 'this is true: 50 + 25 = 75 hundredths')], '0.5 < 0.75.'),
                       tf('"10 is not an even number" is true.', False, '10 = 2 x 5 is even, so "10 is not even" is false.'),
                   ]),
                 B('Negation is not the same as the opposite', 'prerequisite',
                   'The most common MAIN error is replacing a statement by its opposite (full/empty, taller/shorter). A '
                   'negation must cover every case where the original is false.', qs=[
                       mc('What is the negation of "The door is open"?', 'The door is not open.',
                          [('The door is locked.', 'a door can be closed without being locked'),
                           ('The window is open.', 'that is about the window'),
                           ('The door is wide open.', 'that is not a negation')], 'Put "not" on the whole claim.'),
                       tf('"The water is cold" and "The water is hot" are negations of each other.', False,
                          'Warm water makes both false; they are opposites, not negations.'),
                       mc('What is the negation of "Tom won the race"?', 'Tom did not win the race.',
                          [('Tom lost the race.', 'he may not have raced at all'), ('Tom came last.', 'too specific'),
                           ('Someone else won.', 'there may have been no winner')], 'Negate the whole statement.'),
                       tf('If a statement is true, its negation is also true.', False, 'A statement and its negation always have '
                                                                                 'opposite truth values.'),
                       mc('n is a whole number. What is the negation of "n is even"?', 'n is odd.',
                          [('n is 0.', 'too specific'), ('n is negative.', 'unrelated'), ('n is prime.', 'unrelated')],
                          'For whole numbers, "not even" means exactly "odd".'),
                   ]),
             ],
             f1=FW('Negate ranges, counts and double negatives', 'Harder: negations of ranges, of "at least", and repeated '
                                                              'negations.', [
                 mc('x stands for a real number. What is the negation of "3 < x < 7" (x is between 3 and 7)?',
                    'x ≤ 3 or x ≥ 7', [('x < 3 or x > 7', 'misses x = 3 and x = 7'),
                                      ('3 ≥ x ≥ 7', 'no number satisfies this'), ('x ≤ 3 and x ≥ 7', 'no number satisfies this')],
                    'x is not strictly between 3 and 7 exactly when it is at most 3 or at least 7.',
                    check=lambda t: all((3 < x < 7) != {'x ≤ 3 or x ≥ 7': x <= 3 or x >= 7, 'x < 3 or x > 7': x < 3 or x > 7,
                                                        '3 ≥ x ≥ 7': 3 >= x >= 7, 'x ≤ 3 and x ≥ 7': x <= 3 and x >= 7}[t]
                                        for x in [i / 2 for i in range(-4, 21)])),
                 mc('Exactly 9 lamps are in a room. What is the negation of "At least 5 lamps are on"?', 'At most 4 lamps are on.',
                    [('At most 5 lamps are on.', 'exactly 5 lamps on makes both statements true'),
                     ('No lamps are on.', 'too strong: 1 to 4 lamps on also makes the original false'),
                     ('At least 4 lamps are off.', 'with 5 on and 4 off, the original and this statement are both true')],
                    'With whole numbers 0 to 9, "at least 5 on" is false exactly when 0 to 4 are on: at most 4.',
                    check=lambda t: all((n >= 5) != {'At most 4 lamps are on.': n <= 4, 'At most 5 lamps are on.': n <= 5,
                                                     'No lamps are on.': n == 0, 'At least 4 lamps are off.': 9 - n >= 4}[t]
                                        for n in range(10))),
                 tt('Complete the truth table: the columns are "not P" and "not (not P)".', ['P'],
                    [('not P', lambda p: not p), ('not (not P)', lambda p: p)],
                    '"not P" flips each value; flipping again gives back P.'),
                 sa('How many of these are true? (1) "It is not true that 8 is odd." (2) "It is false that 0 is not a whole '
                    'number." (3) "It is not the case that 2 + 2 is not 4." (4) "It is not true that 5 is not less than 3."',
                    'Number true:', '3', '(1) 8 is not odd: true. (2) says 0 IS a whole number: true. (3) says 2 + 2 is 4: true. '
                                         '(4) says 5 IS less than 3: false. Three are true.',
                    compute=lambda: str(sum([not (8 % 2 == 1), True, 2 + 2 == 4, 5 < 3]))),
                 tf('The negation of "Mia always walks to school" is "Mia never walks to school".', False,
                    'If Mia walks on some days and not others, both are false. The negation is "Mia does not always walk to '
                    'school": on at least one day she does not walk.'),
             ]),
             f2=FW('Negation inside conditions and counts', 'Expert: negations of combined conditions and claims about how '
                                                           'many.', [
                 values('Give a number x that makes the negation of "x < 2 or x > 5" true.', [('x', 'x =')],
                        'x >= 2 and x <= 5', {'x': 3},
                        '"x < 2 or x > 5" is false exactly when x is not less than 2 AND not greater than 5: 2 ≤ x ≤ 5.',
                        wrong=[{'x': 1}, {'x': 6}, {'x': 5.5}]),
                 mc('There are 6 lights. What is the negation of "At most 2 lights are on"?', 'At least 3 lights are on.',
                    [('At least 2 lights are on.', 'exactly 2 on makes both true'),
                     ('Exactly 3 lights are on.', 'too narrow: 4, 5 or 6 on also make the original false'),
                     ('At most 2 lights are off.', '3 lights on and 3 off makes both false')],
                    '"At most 2" is false exactly when 3 or more are on.',
                    check=lambda t: all((n <= 2) != {'At least 3 lights are on.': n >= 3, 'At least 2 lights are on.': n >= 2,
                                                     'Exactly 3 lights are on.': n == 3, 'At most 2 lights are off.': 6 - n <= 2}[t]
                                        for n in range(7))),
                 mc('Ana says: "It is false that it is not true that the test is not on Friday." What is Ana saying?',
                    'The test is not on Friday.', [('The test is on Friday.', 'count the negations: there are three'),
                                                   ('Nothing about the test.', 'it is a definite claim'),
                                                   ('The test might be on Friday.', 'the statement is definite')],
                    'Count: "false that" (1), "not true that" (2), "not on Friday" (3). Two negations cancel, leaving one: the '
                    'test is not on Friday.'),
                 tf('For every statement P, exactly one of P and "not P" is true.', True,
                    'That is what a negation means: it is true exactly when P is false.'),
                 sa('Statements about a whole number n from 1 to 10: A: "n is even." B: "n is not greater than 6." C: "It is '
                    'not true that n is a multiple of 3." For how many values of n are all three statements true?',
                    'Values:', '2', 'Even and at most 6: 2, 4, 6. Not a multiple of 3: 2, 4. Two values.',
                    compute=lambda: str(sum(1 for n in range(1, 11) if n % 2 == 0 and not n > 6 and n % 3 != 0))),
             ]))


# ------------------------------------------------------------------ Set 6: codes
def letval(w):
    return sum(ord(c) - 64 for c in w)


def shift(w, k):
    return ''.join(chr((ord(c) - 65 + k) % 26 + 65) for c in w)


def interleave(a, b):
    return ''.join(x + y for x, y in zip(a, b))


HOLES = {c: 1 for c in 'ADOPQR'}
HOLES['B'] = 2


def holes(w):
    return sum(HOLES.get(c, 0) for c in w)


HOLE_TEXT = ('In this code, a letter\'s value is the number of closed spaces inside it in plain block capitals: A, D, O, P, '
             'Q and R have 1, B has 2, and every other letter has 0. A word\'s value is the sum of its letters\' values.')

SYM = [(a, b, c) for a in range(1, 13) for b in range(1, 13) for c in range(1, 13)
       if a + a == 10 and a + b == 8 and b + c == 9]
assert SYM == [(5, 3, 6)]


def s6():
    return S(6, 'Decode and encode with a stated key, and find a key within a stated family',
             main=[
                 sa('In a code, each letter has the value of its position in the alphabet (A = 1, B = 2, ..., Z = 26), and a '
                    'word\'s value is the sum of its letters\' values. For example, CAB = 3 + 1 + 2 = 6. What is the value of '
                    'BEAD?', 'Value:', '12', 'B = 2, E = 5, A = 1, D = 4: 2 + 5 + 1 + 4 = 12.', compute=lambda: str(letval('BEAD'))),
                 mc('In a code, every letter is replaced by the letter 3 places later in the alphabet (A becomes D, B becomes E, '
                    'and X, Y, Z wrap around to A, B, C). A coded word reads FDW. What was the original word?', 'CAT',
                    [('IGZ', 'that shifts 3 more places forward instead of back'), ('CAW', 'only the first two letters '
                                                                                         'were decoded'),
                     ('DBX', 'each letter was moved back only 2 places')],
                    'Decoding moves each letter 3 places back: F -> C, D -> A, W -> T.',
                    check=lambda w: shift(w, 3) == 'FDW'),
                 sa('A code adds the same whole number k to every digit and keeps only the last digit of each sum (so 8 + 3 '
                    'gives 1). The code turns 2025 into 4247. What does it turn 1990 into?', 'Code:', '3112',
                    'From 2 -> 4, k = 2 (every digit agrees: 0 -> 2, 2 -> 4, 5 -> 7). Then 1 -> 3, 9 -> 1, 9 -> 1, 0 -> 2: 3112.',
                    compute=lambda: ''.join(str((int(d) + 2) % 10) for d in '1990')),
                 sa('Each symbol stands for a whole number. Star + Star = 10. Star + Circle = 8. Circle + Square = 9. What '
                    'number is Square?', 'Square:', '6', 'Star = 5, so Circle = 3, so Square = 6.',
                    compute=lambda: str(SYM[0][2])),
                 mc('Two 3-letter words were interleaved: first letter of word 1, first letter of word 2, second letter of '
                    'word 1, and so on. The result is CDAORT. Which two words were interleaved?', 'CAR and DOT',
                    [('COD and ART', 'interleaving COD and ART gives CAORDT'), ('CAT and DOR', 'interleaving gives CDAOTR'),
                     ('CAD and ORT', 'interleaving gives COARDT')],
                    'Letters 1, 3, 5 (C, A, R) form word 1 and letters 2, 4, 6 (D, O, T) form word 2.',
                    check=lambda t: interleave(*t.split(' and ')) == 'CDAORT'),
             ],
             back=[B('Strategy: write the key as a table', 'guided_strategy',
                     'Students who decode in their head lose track of which way the key works. Writing the key as a table and '
                     'applying it one symbol at a time keeps encoding and decoding straight.',
                     lesson=lesson('Write the key as a table',
                                   ['A code is a rule that turns each symbol into another symbol (or a number).',
                                    'Write the key as a two-row table: plain symbols on top, coded symbols below. To encode, '
                                    'read top to bottom; to decode, find the coded symbol on the bottom row and read up.',
                                    'When the key must be found from an example, use the example to fill in the table, then '
                                    'check the key on EVERY symbol of the example before using it.'],
                                   'Worked example (a different code)',
                                   ['A code replaces each digit d by 9 - d. What is 274 in code, and what number does the code '
                                    '815 come from?'],
                                   ['Table: 0->9, 1->8, 2->7, 3->6, 4->5, 5->4, 6->3, 7->2, 8->1, 9->0.',
                                    'Encode 274: 2->7, 7->2, 4->5, so 725.',
                                    'Decode 815: 8 comes from 1, 1 from 8, 5 from 4, so 184.',
                                    'Check: 184 encodes to 815.']),
                     qs=[
                         sa('A code replaces each letter by its position in the alphabet (A = 1, ..., Z = 26) and adds them. '
                            'What is the value of DOG?', 'Value:', '26', 'D = 4, O = 15, G = 7: 26.',
                            compute=lambda: str(letval('DOG'))),
                         mc('A code moves each letter 1 place later (A -> B, ..., Z -> A). What is BOX in code?', 'CPY',
                            [('ANW', 'moved back instead of forward'), ('CPX', 'the last letter was not coded'),
                             ('DQZ', 'moved 2 places')], 'B -> C, O -> P, X -> Y.', check=lambda w: shift('BOX', 1) == w),
                         sa('A code replaces each digit d by 9 - d. What is the code for 306?', 'Code:', '693',
                            '3 -> 6, 0 -> 9, 6 -> 3.', compute=lambda: ''.join(str(9 - int(d)) for d in '306')),
                         tf('If a code moves every letter 2 places later, then decoding moves every letter 2 places earlier.',
                            True, 'Decoding undoes encoding.'),
                         sa('Triangle + Triangle + Triangle = 12. What number is Triangle?', 'Triangle:', '4', '3 x 4 = 12.',
                            compute=lambda: str(12 // 3)),
                     ])],
             f1=FW('Codes with structure: shapes of letters and combined rules', 'Harder: a key based on letter shapes, and two '
                                                                                'rules applied in order.', [
                 sa(HOLE_TEXT + ' What is the value of BREAD?', 'Value:', '5', 'B 2 + R 1 + E 0 + A 1 + D 1 = 5.',
                    compute=lambda: str(holes('BREAD'))),
                 mc(HOLE_TEXT + ' Which word has value 0?', 'FLIES', [('TOWEL', 'O has 1'), ('MAZE', 'A has 1'),
                                                                      ('SHIRT', 'R has 1')],
                    'F, L, I, E and S all have 0.', check=lambda w: holes(w) == 0),
                 sa('A code first writes a word backward and then moves each letter 1 place later in the alphabet. What is '
                    'the code for MAP?', 'Code:', 'QBN', 'Backward: PAM. Shift by 1: QBN.',
                    compute=lambda: shift('MAP'[::-1], 1)),
                 sa('Each symbol stands for a whole number. Moon + Moon + Sun = 13. Sun + Sun = 6. Moon + Star = 9. What '
                    'number is Star?', 'Star:', '4', 'Sun = 3, so 2 x Moon = 10 and Moon = 5, so Star = 4.',
                    compute=lambda: str([s for m in range(10) for su in range(10) for s in range(10)
                                         if 2 * m + su == 13 and 2 * su == 6 and m + s == 9][0])),
                 tf('A code moves every letter 13 places later in the alphabet (wrapping around). Applying this code twice '
                    'gives back the original word.', True, '13 + 13 = 26 places, a full trip around the alphabet.',
                    check=lambda: shift(shift('LOGIC', 13), 13) == 'LOGIC'),
             ]),
             f2=FW('Find a key and prove when none exists', 'Expert: determine a key from coded examples, and show that a '
                                                           'requested code cannot exist.', [
                 mc('A code adds 3 to each digit of a 4-digit number and keeps only the last digit of each sum (so 8 becomes 1). '
                    'Is there a 4-digit number whose code is the same number written backward?',
                    'No: the middle digits would need b + 6 to end in the same digit as b, which never happens.',
                    [('Yes: 1234 works.', '1234 codes to 4567, not 4321'),
                     ('Yes: any number whose digits are all equal works.', '5555 codes to 8888, not 5555'),
                     ('No: but only because the first digit cannot be 0.', 'the reason is the middle digits, not a leading zero')],
                    'If abcd codes to dcba, then b + 3 ends in c and c + 3 ends in b, so b + 6 ends in b, which is impossible '
                    '(6 is not a multiple of 10).', method='Automatic: all 9000 four-digit numbers tested; none works.',
                    check=lambda t: t.startswith('No: the middle') and not any(
                        ''.join(str((int(d) + 3) % 10) for d in str(n)) == str(n)[::-1] for n in range(1000, 10000))),
                 sa('A code moves every letter the same number of places later in the alphabet (wrapping around). It turns '
                    'GO into MU. What does it turn LOGIC into?', 'Code:', 'RUMOI', 'G -> M is 6 places, and O -> U is also 6. '
                                                                                   'Shift LOGIC by 6: RUMOI.',
                    compute=lambda: shift('LOGIC', 6)),
                 values('Each symbol stands for a whole number from 1 to 9. Square + Square = Circle, and Circle + Square = 12. '
                        'Find Square s and Circle c.', [('s', 'Square s ='), ('c', 'Circle c =')],
                        's + s == c and c + s == 12 and isInteger(s) and isInteger(c)', {'s': 4, 'c': 8},
                        '3 x Square = 12, so Square = 4 and Circle = 8. This is the only solution.',
                        wrong=[{'s': 6, 'c': 6}, {'s': 3, 'c': 9}], search={'s': range(1, 10), 'c': range(1, 10)}),
                 sa(HOLE_TEXT + ' Using only the letters B, O and T (each as often as you like), what is the greatest value of '
                                'a 4-letter string?', 'Value:', '8', 'B has the most closed spaces (2), so BBBB = 8.',
                    compute=lambda: str(max(holes(''.join(w)) for w in itertools.product('BOT', repeat=4)))),
                 mc('A code sends each letter to the letter at the same distance from the other end of the alphabet (A <-> Z, '
                    'B <-> Y, C <-> X, ...). Which word is coded as itself?', 'No word: no letter is coded as itself.',
                    [('MOON', 'M codes to N and O to L'), ('WIZARD', 'W -> D, I -> R, ...: it codes to DRAZIW'),
                     ('NOON', 'N codes to M')],
                    'A letter at position p codes to position 27 - p. A letter would code to itself only if p = 27 - p, which '
                    'needs p = 13.5: impossible. So no word codes to itself.',
                    check=lambda t: t.startswith('No word') and not any(chr(155 - ord(c)) == c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')),
             ]))


# ------------------------------------------------------------------ Set 7: ordering from clues
def s7():
    return S(7, 'Build an ordering that satisfies relational clues',
             main=[
                 order('Four books stand on a shelf. The atlas is left of the cookbook. The diary is right of the cookbook. '
                       'The biography is at the far left. Order the books from left to right.',
                       [('A', 'atlas'), ('B', 'biography'), ('C', 'cookbook'), ('D', 'diary')],
                       lambda p: pos(p, 'A') < pos(p, 'C') < pos(p, 'D') and p[0] == 'B',
                       'The biography is first. The atlas, cookbook and diary must come in that order after it.',
                       expect=['B', 'A', 'C', 'D'], unique=True),
                 order('Five friends arrived at a party one at a time. Gil arrived before Hana but after Ivo. Jo arrived last. '
                       'Kai arrived right after Ivo. Order the arrivals, first to last.',
                       [('G', 'Gil'), ('H', 'Hana'), ('I', 'Ivo'), ('J', 'Jo'), ('K', 'Kai')],
                       lambda p: pos(p, 'I') < pos(p, 'G') < pos(p, 'H') and p[-1] == 'J' and pos(p, 'K') == pos(p, 'I') + 1,
                       'Jo is last. Ivo comes before Gil, who comes before Hana, and Kai is right after Ivo: Ivo, Kai, Gil, '
                       'Hana, Jo.', expect=['I', 'K', 'G', 'H', 'J'], unique=True),
                 mc('Five runners finished a race with no ties. Uma beat Vic. Wes finished right after Uma. Xia beat Uma. Yan '
                    'finished last. Who finished in the middle (3rd)?', 'Wes',
                    [('Uma', 'Uma is 2nd'), ('Vic', 'Vic is 4th'), ('Xia', 'Xia is 1st')],
                    'Yan is 5th. Xia beat Uma and Uma beat Vic, with Wes right after Uma: Xia, Uma, Wes, Vic, Yan.',
                    method='Automatic: all 120 orders checked; only Xia, Uma, Wes, Vic, Yan fits.',
                    check=lambda t: [p for p in itertools.permutations('UVWXY') if pos(p, 'U') < pos(p, 'V')
                                     and pos(p, 'W') == pos(p, 'U') + 1 and pos(p, 'X') < pos(p, 'U') and p[-1] == 'Y'] ==
                    [tuple('XUWVY')] and t == 'Wes'),
                 order('Four flags hang on a pole, from top to bottom. The green flag is somewhere between the red and the blue '
                       'flags. The red flag is not at the top. The yellow flag is directly below the blue flag. Order the '
                       'flags from top to bottom.', [('R', 'red'), ('G', 'green'), ('B', 'blue'), ('Y', 'yellow')],
                       lambda p: (min(pos(p, 'R'), pos(p, 'B')) < pos(p, 'G') < max(pos(p, 'R'), pos(p, 'B'))
                                  and p[0] != 'R' and pos(p, 'Y') == pos(p, 'B') + 1),
                       'Blue must be above yellow with nothing between them, and green lies between red and blue. If blue were '
                       'below green, yellow would follow blue at the bottom and red would have to be on top, which is not '
                       'allowed. So blue is on top, then yellow, then green, then red.',
                       expect=['B', 'Y', 'G', 'R'], unique=True),
                 sa('Seven students stand in a line. Lee is 2nd from the left. Max is 3rd from the right. How many students '
                    'stand between Lee and Max?', 'Students between:', '2',
                    'Max is 3rd from the right of 7, so 5th from the left. Between positions 2 and 5 are positions 3 and 4: '
                    '2 students.', compute=lambda: str((7 - 3 + 1) - 2 - 1)),
             ],
             back=[B('Strategy: place the most constrained item first', 'guided_strategy',
                     'Students who get stuck usually try the clues in the order given. Starting with fixed positions and tight '
                     'links (first, last, "right after") shrinks the search fast.',
                     lesson=lesson('Place the most constrained item first',
                                   ['Draw a row of blanks, one per position.',
                                    'Fill in fixed positions first ("last", "2nd from the left").',
                                    'Then join items that must be next to each other into a block ("right after").',
                                    'Finally use before/after clues to order the remaining pieces, and check every clue at '
                                    'the end.'],
                                   'Worked example (a different line)',
                                   ['Four cars wait at a light: Pia\'s car is last. Quin\'s car is right in front of Rose\'s. '
                                    'Sal\'s car is in front of Quin\'s. Order the cars from front to back.'],
                                   ['Pia is 4th.', 'Quin-Rose is a block of two.',
                                    'Sal is in front of Quin, so the order of the front three is Sal, Quin, Rose.',
                                    'Answer: Sal, Quin, Rose, Pia. Check each clue: all true.']),
                     qs=[
                         order('Three cups stand in a row. The red cup is between the other two. The blue cup is on the right. '
                               'Order them from left to right.', [('R', 'red'), ('B', 'blue'), ('W', 'white')],
                               lambda p: p[1] == 'R' and p[2] == 'B', 'Blue on the right, red in the middle, white on the left.',
                               expect=['W', 'R', 'B'], unique=True),
                         sa('In a line of 9 people, Ola is 4th from the front. What is her position counted from the back?',
                            'Position from the back:', '6', '9 - 4 + 1 = 6.', compute=lambda: str(9 - 4 + 1)),
                         tf('"Bea is right after Cy" means no one is between Cy and Bea.', True, '"Right after" means directly next.'),
                         mc('Ava is taller than Ben, and Ben is taller than Cal. Who is shortest?', 'Cal',
                            [('Ava', 'Ava is tallest'), ('Ben', 'Ben is in the middle'), ('It cannot be known.', 'the clues '
                                                                                                              'give a full order')],
                            'Ava > Ben > Cal.'),
                         order('Four racers: Dot finished first. Eli beat Fay. Gus finished last. Order them, first to last.',
                               [('D', 'Dot'), ('E', 'Eli'), ('F', 'Fay'), ('G', 'Gus')],
                               lambda p: p[0] == 'D' and p[-1] == 'G' and pos(p, 'E') < pos(p, 'F'),
                               'Dot first, Gus last, Eli before Fay.', expect=['D', 'E', 'F', 'G'], unique=True),
                     ])],
             f1=FW('Orderings with "next to" and "not next to"', 'Harder: adjacency clues and more items.', [
                 order('Five houses stand in a row, numbered 1 to 5 from left to right. The bakery is next to the bank. The '
                       'café is at one end. The dentist is directly right of the café. The florist is not next to the dentist. '
                       'The bank is in house 4. Order the businesses from left to right.',
                       [('K', 'bakery'), ('N', 'bank'), ('C', 'café'), ('D', 'dentist'), ('F', 'florist')],
                       lambda p: (abs(pos(p, 'K') - pos(p, 'N')) == 1 and pos(p, 'C') in (0, 4) and pos(p, 'D') == pos(p, 'C') + 1
                                  and abs(pos(p, 'F') - pos(p, 'D')) != 1 and pos(p, 'N') == 3),
                       'The dentist is right of the café, so the café is house 1 and the dentist house 2. The bank is house 4. '
                       'The florist is not next to the dentist, so not house 3: the florist is house 5 and the bakery house 3, '
                       'next to the bank.', expect=['C', 'D', 'K', 'N', 'F'], unique=True),
                 sa('Six people, A to F, sit in seats 1 to 6 in a row. C is in seat 1 and D is in seat 6. B sits right '
                    'after A, and E sits right after B. F does not sit next to C. Which seat is F in?', 'Seat:', '5',
                    'A, B, E form a block of three in seats 2-4 or 3-5. If the block were in 3-5, F would be in seat 2, next to '
                    'C. So the block is in seats 2-4 and F is in seat 5.',
                    compute=lambda: str([p.index('F') + 1 for p in itertools.permutations('ABCDEF') if p[0] == 'C'
                                         and p[5] == 'D' and pos(p, 'B') == pos(p, 'A') + 1 and pos(p, 'E') == pos(p, 'B') + 1
                                         and pos(p, 'F') != 1][0])),
                 mc('Five students line up. Pat is in front of Quinn. Rae is right behind Sol. Tia is first. Quinn is last. '
                    'Which statement must be true?', 'Tia is directly in front of Pat or of Sol.',
                    [('Pat is 2nd.', 'Sol and Rae can be 2nd and 3rd'), ('Rae is 4th.', 'Rae can be 3rd'),
                     ('Sol is right behind Pat.', 'Sol can be in front of Pat')],
                    'Tia is 1st and Quinn 5th. The middle three are Pat and the block Sol-Rae in some order: Pat, Sol, Rae or '
                    'Sol, Rae, Pat. In both, position 2 is Pat or Sol.',
                    method='Automatic: all 120 orders checked.',
                    check=lambda t: all({'Tia is directly in front of Pat or of Sol.': p[1] in 'PS', 'Pat is 2nd.': p[1] == 'P',
                                         'Rae is 4th.': p[3] == 'R', 'Sol is right behind Pat.': pos(p, 'S') == pos(p, 'P') + 1}[t]
                                        for p in itertools.permutations('PQRST') if pos(p, 'P') < pos(p, 'Q')
                                        and pos(p, 'R') == pos(p, 'S') + 1 and p[0] == 'T' and p[-1] == 'Q')),
                 grid('Four friends sit in seats 1 to 4 in a row. Ari is not next to Bo. Cy sits in seat 2. Bo is in a higher '
                      'seat number than Cy. Di is not in seat 4. Give each friend\'s seat.', ['Ari', 'Bo', 'Cy', 'Di'],
                      ['1', '2', '3', '4'],
                      lambda a: (abs(int(a['Ari']) - int(a['Bo'])) != 1 and a['Cy'] == '2' and int(a['Bo']) > 2 and a['Di'] != '4'),
                      'Cy is in seat 2. Bo is in seat 3 or 4. If Bo were in 3, Ari (not next to Bo) would need seat 1, leaving '
                      'seat 4 for Di, which is not allowed. So Bo is in 4; Ari is not in 3, so Ari is in 1 and Di in 3.'),
                 tf('If five people stand in a line and three of them must stand next to each other in a fixed order, there '
                    'are exactly 6 possible lines.', True,
                    'Treat the three as one block: 3 units (the block and two people) can be ordered in 3 x 2 x 1 = 6 ways.',
                    check=lambda: sum(1 for p in itertools.permutations('ABCDE') if pos(p, 'B') == pos(p, 'A') + 1
                                      and pos(p, 'C') == pos(p, 'B') + 1) == 6),
             ]),
             f2=FW('Count and compare orderings', 'Expert: count every valid ordering and find which clue is decisive.', [
                 sa('Five students, P, Q, R, S and T, stand in a line. P is somewhere in front of Q, and R is somewhere in front '
                    'of S. How many different lines are possible?', 'Lines:', '30',
                    'There are 120 lines without clues. Half have P before Q, and of those half have R before S: '
                    '120 / 4 = 30.', compute=lambda: str(sum(1 for p in itertools.permutations('PQRST')
                                                             if pos(p, 'P') < pos(p, 'Q') and pos(p, 'R') < pos(p, 'S')))),
                 order('Six relay swimmers, A to F, swim in order. B swims right after E. D swims before A. C swims last. F '
                       'swims first. A swims right after B. Give the swimming order.',
                       [(k, k) for k in 'ABCDEF'],
                       lambda p: (pos(p, 'B') == pos(p, 'E') + 1 and pos(p, 'D') < pos(p, 'A') and p[-1] == 'C' and p[0] == 'F'
                                  and pos(p, 'A') == pos(p, 'B') + 1),
                       'F is first and C last. E, B, A form a block (B right after E, A right after B) in positions 2-4 or 3-5. '
                       'If the block were in 2-4, D would be 5th, after A, which is not allowed. So the block is in 3-5 and D is '
                       '2nd: F, D, E, B, A, C.', expect=list('FDEBAC'), unique=True),
                 mc('Four people, W, X, Y and Z, stand in a line. Clues: (1) W is not first. (2) X is right after W. (3) Y is '
                    'last. Which clue could be removed and still leave exactly one possible line?', 'No clue can be removed.',
                    [('Clue 1', 'without it, both W, X, Z, Y and Z, W, X, Y fit'),
                     ('Clue 2', 'without it, four lines fit (for example X, W, Z, Y)'),
                     ('Clue 3', 'without it, four lines fit (for example Z, W, X, Y and Y, W, X, Z)')],
                    'With all three clues the only line is Z, W, X, Y. Removing any one clue leaves at least two lines, so '
                    'every clue is needed.', method='Automatic: each clue removed in turn and all 24 lines recounted.',
                    check=lambda t: t == 'No clue can be removed.' and all(
                        sum(1 for p in itertools.permutations('WXYZ') if all(c(p) for j, c in enumerate(W_CLUES) if j != k)) > 1
                        for k in range(3))),
                 values('Seven people stand in a line, numbered 1 to 7 from the front. Ana is in position a and Ben is in '
                        'position b. Ana is in front of Ben, exactly two people stand between them, and Ben is not last. Give '
                        'one possible pair of positions.', [('a', 'Ana a ='), ('b', 'Ben b =')],
                        'b - a == 3 and b <= 6 and a >= 1 and isInteger(a) and isInteger(b)', {'a': 2, 'b': 5},
                        'Two people between means b = a + 3. Ben not last means b ≤ 6, so (1, 4), (2, 5) or (3, 6).',
                        wrong=[{'a': 4, 'b': 7}, {'a': 2, 'b': 4}, {'a': 5, 'b': 2}],
                        search={'a': range(1, 8), 'b': range(1, 8)}),
                 tf('With the clues "J is before K" and "K is before L" for three people in a line, the order is fully '
                    'determined.', True, 'J, K, L is the only order.',
                    check=lambda: sum(1 for p in itertools.permutations('JKL') if pos(p, 'J') < pos(p, 'K') < pos(p, 'L')) == 1),
             ]))


W_CLUES = [lambda p: p[0] != 'W', lambda p: pos(p, 'X') == pos(p, 'W') + 1, lambda p: p[-1] == 'Y']
LAMPS = [p for p in itertools.product([True, False], repeat=3)
         if sum([p[0] or p[1], p[2], p[0] != p[2]]) == 1]


# ------------------------------------------------------------------ Set 8: and, or, exclusive or
def s8():
    return S(8, 'Truth values of and, inclusive or, exclusive or',
             main=[
                 tf('"7 is odd and 7 is greater than 10" is true.', False, 'An "and" statement needs both parts true; 7 > 10 is '
                                                                           'false.', check=lambda: 7 % 2 == 1 and 7 > 10),
                 tf('"7 is odd or 7 is greater than 10" is true (with "or" meaning at least one).', True,
                    'An inclusive "or" needs at least one part true; 7 is odd.', check=lambda: 7 % 2 == 1 or 7 > 10),
                 mc('A sign says: "Each meal comes with soup or salad, but not both." Which order follows the sign?',
                    'a meal with salad and no soup', [('a meal with soup and salad', '"not both" rules this out'),
                                                      ('a meal with neither soup nor salad', 'the meal must come with one '
                                                                                             'of them'),
                                                      ('a meal with two salads and a soup', 'includes both soup and salad')],
                    'This is an exclusive "or": exactly one of soup and salad.'),
                 values('Give a whole number n that makes "n is even or n is greater than 20" true but "n is even and n is '
                        'greater than 20" false.', [('n', 'n =')],
                        '(isEven(n) or n > 20) and not (isEven(n) and n > 20) and isInteger(n)', {'n': 4},
                        'Exactly one part must be true: an even number up to 20 (like 4) or an odd number greater than 20 '
                        '(like 25).', wrong=[{'n': 22}, {'n': 7}, {'n': 30}], search={'n': range(1, 41)}),
                 mc('P is true and Q is false. Which statement is FALSE?', 'P and Q',
                    [('P or Q', 'one part is true, so the "or" is true'),
                     ('P exclusive-or Q', 'exactly one part is true, so it is true'),
                     ('P and not Q', 'P is true and not Q is true')],
                    '"P and Q" needs both true, but Q is false.',
                    check=lambda t: not {'P and Q': True and False, 'P or Q': True or False, 'P exclusive-or Q': True != False,
                                         'P and not Q': True and not False}[t]),
             ],
             back=[
                 B('Truth values of the parts', 'prerequisite',
                   'A compound statement can only be judged once each part is judged. Students who misjudge a part get the '
                   'whole wrong.', outcome='LOGIC.CONNECTIVE.01', qs=[
                       tf('"12 is a multiple of 5" is true.', False, '12 = 5 x 2 + 2.', check=lambda: 12 % 5 == 0),
                       tf('"-3 < 1" is true.', True, '-3 is to the left of 1.', check=lambda: -3 < 1),
                       tf('"A triangle has 4 sides" is true.', False, 'A triangle has 3 sides.'),
                       tf('"0 is even" is true.', True, '0 = 2 x 0.', check=lambda: 0 % 2 == 0),
                       mc('Which part of "9 is odd and 9 is prime" is false?', '9 is prime',
                          [('9 is odd', 'that part is true'), ('both parts', '9 is odd is true'),
                           ('neither part', '9 = 3 x 3, so it is not prime')], '9 = 3 x 3.'),
                   ]),
                 B('Inclusive or exclusive?', 'prerequisite',
                   'Students who apply "or" differently from the question\'s meaning get the opposite truth value when both '
                   'parts are true. Reading the stated meaning of "or" is the obstacle.', qs=[
                       tf('With inclusive "or", "P or Q" is false when both P and Q are true.', False, 'Inclusive "or" needs at least one '
                          'part true; with both true it is true.'),
                       tf('With exclusive "or", "P or Q" is true when both P and Q are true.', False, 'Exclusive means exactly one.'),
                       mc('A rule says "You may bring a pencil or a pen (or both)." Which kind of "or" is this?', 'inclusive',
                          [('exclusive', '"or both" allows both'), ('neither kind', 'it is an "or"'),
                           ('it cannot be told', '"or both" tells us')], '"Or both" signals inclusive "or".'),
                       mc('"The light is either on or off" describes two cases that can never both happen. Which "or" fits '
                          'best?', 'exclusive', [('inclusive', 'both cannot be true at once, so exactly one holds'),
                                                 ('neither', 'it is an "or" statement'), ('"and"', 'it is not a conjunction')],
                          'Exactly one of the two is true.'),
                       tf('When P is false and Q is false, exclusive "P or Q" is true.', False,
                          'Exclusive "or" needs exactly one part true; with neither true it is false.'),
                   ]),
             ],
             f1=FW('Compound statements with three parts', 'Harder: three parts and mixed connectives.', [
                 tf('"(3 > 2 and 5 > 9) or 4 is even" is true.', True, 'The bracket is false (5 > 9 is false), but 4 is even, so '
                                                                       'the "or" is true.',
                    check=lambda: (3 > 2 and 5 > 9) or 4 % 2 == 0),
                 tf('"3 > 2 and (5 > 9 or 4 is odd)" is true.', False, 'The bracket is false (both parts false), so the "and" is '
                                                                      'false.', check=lambda: 3 > 2 and (5 > 9 or 4 % 2 == 1)),
                 sa('For how many whole numbers n from 1 to 20 is "n is a multiple of 3 exclusive-or n is a multiple of 4" '
                    'true?', 'Count:', '9',
                    'Multiples of 3: 6 numbers; of 4: 5 numbers; of both (12): 1 number. Exactly one: 6 + 5 - 2 x 1 = 9.',
                    compute=lambda: str(sum(1 for n in range(1, 21) if (n % 3 == 0) != (n % 4 == 0)))),
                 tt('Complete the truth table for "P exclusive-or Q" and for "P or Q" (inclusive).', ['P', 'Q'],
                    [('P exclusive-or Q', lambda p, q: p != q), ('P or Q', lambda p, q: p or q)],
                    'They differ only in the first row, where both parts are true.'),
                 mc('Statement S: "P or Q" (inclusive). S is false. What can be concluded?', 'P is false and Q is false.',
                    [('P is true or Q is true.', 'that says S itself is true, but S is false'),
                     ('Exactly one of P and Q is false.', 'both are false'),
                     ('P is true and Q is false.', 'then S would be true')],
                    'An inclusive "or" is false only when both parts are false.'),
             ]),
             f2=FW('Design statements with given truth values', 'Expert: build and count assignments that make compound '
                                                             'statements true.', [
                 sa('P, Q and R are statements. In how many of the 8 combinations of truth values is "(P or Q) and not R" true?',
                    'Combinations:', '3', 'R must be false (4 cases), and at least one of P, Q true: 3 of those 4.',
                    compute=lambda: str(sum(1 for p, q, r in itertools.product([True, False], repeat=3) if (p or q) and not r))),
                 values('Give whole numbers a and b with "a > b exclusive-or a + b is even" true and both numbers between 1 and '
                        '9.', [('a', 'a ='), ('b', 'b =')],
                        '((a > b) != isEven(a + b)) and a >= 1 and a <= 9 and b >= 1 and b <= 9 and isInteger(a) and isInteger(b)',
                        {'a': 5, 'b': 2},
                        'Exactly one of "a > b" and "a + b is even" must hold, for example a = 5, b = 2 (a > b, sum 7 odd) or '
                        'a = 2, b = 4 (a < b, sum even).', wrong=[{'a': 5, 'b': 3}, {'a': 2, 'b': 5}],
                        search={'a': range(1, 10), 'b': range(1, 10)}),
                 tf('"P exclusive-or Q" has the same truth value as "(P or Q) and not (P and Q)" in every row of a truth '
                    'table.', True, 'Both are true exactly when one part is true and the other false.',
                    check=lambda: all((p != q) == ((p or q) and not (p and q)) for p, q in itertools.product([True, False], repeat=2))),
                 mc('Three lamps A, B and C are each on or off. Exactly one of these statements is true: (1) "A is on or B is '
                    'on." (2) "C is on." (3) "A is on exclusive-or C is on." Which lamps are on?', 'B only',
                    [('A only', 'then (1) and (3) are both true'), ('A and B', 'then (1) and (3) are both true'),
                     ('none', 'then all three statements are false')],
                    'Check the 8 patterns. If C is on, (2) is true, so (1) and (3) must be false: (3) false needs A on, but then '
                    '(1) is true. So C is off and (2) is false; exactly one of (1), (3) is true. (3) is true exactly when A is '
                    'on, and then (1) is also true. So A is off, (3) is false, and (1) must be true: B is on.',
                    method='Automatic: all 8 on/off patterns checked; only B on fits.',
                    check=lambda t: t == {(False, True, False): 'B only'}.get(LAMPS[0]) and len(LAMPS) == 1),
                 sa('For how many whole numbers n from 1 to 30 is "n is odd and (n is a multiple of 3 or n is a multiple of 5)" '
                    'true?', 'Count:', '7', 'Odd multiples of 3: 3, 9, 15, 21, 27. Odd multiples of 5: 5, 15, 25. Together, '
                                           'counting 15 once: 3, 5, 9, 15, 21, 25, 27, which is 7 numbers.',
                    compute=lambda: str(sum(1 for n in range(1, 31) if n % 2 == 1 and (n % 3 == 0 or n % 5 == 0)))),
             ]))


SETS = [s5(), s6(), s7(), s8()]
