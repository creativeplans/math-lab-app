"""Logic sets 15-18: converse, inverse and contrapositive; biconditionals; truth-tellers and liars; truth tables."""
import itertools
from lq import S, B, FW, mc, tf, sa, order, values, lesson, grid, tt

TF = [True, False]


def imp(p, q):
    return (not p) or q


def equiv(f, g, n=2):
    return all(f(*v) == g(*v) for v in itertools.product(TF, repeat=n))


FORMS = {'original': lambda p, q: imp(p, q), 'converse': lambda p, q: imp(q, p), 'inverse': lambda p, q: imp(not p, not q),
         'contrapositive': lambda p, q: imp(not q, not p)}


# ------------------------------------------------------------------ Set 15: converse, inverse, contrapositive
def s15():
    return S(15, 'Form the converse, inverse and contrapositive and judge equivalence',
             main=[
                 mc('What is the CONTRAPOSITIVE of "If a shape is a triangle, then it has three sides"?',
                    'If a shape does not have three sides, then it is not a triangle.',
                    [('If a shape has three sides, then it is a triangle.', 'that is the converse'),
                     ('If a shape is not a triangle, then it does not have three sides.', 'that is the inverse'),
                     ('A shape is a triangle and does not have three sides.', 'that is the negation of the conditional')],
                    'The contrapositive of "if P then Q" is "if not Q, then not P".'),
                 mc('Which statement is logically EQUIVALENT to "If n is a multiple of 4, then n is even"?',
                    'If n is not even, then n is not a multiple of 4.',
                    [('If n is even, then n is a multiple of 4.', 'the converse is not equivalent (6 is even)'),
                     ('If n is not a multiple of 4, then n is not even.', 'the inverse is not equivalent (6 is even)'),
                     ('n is a multiple of 4 and n is even.', 'not a conditional')],
                    'A conditional and its contrapositive always have the same truth value.',
                    check=lambda t: t.startswith('If n is not even')),
                 tf('The converse of "If a whole number is a multiple of 6, then it is even" is true.', False,
                    'The converse, "If a whole number is even, then it is a multiple of 6", is false: 4 is even but not a '
                    'multiple of 6.', check=lambda: all(imp(n % 2 == 0, n % 6 == 0) for n in range(1, 100))),
                 values('The statement "If x > 2, then x squared > 4" is true. Find a real number x that shows its CONVERSE is '
                        'false.', [('x', 'x =')], 'x^2 > 4 and not (x > 2)', {'x': -3},
                        'The converse is "If x squared > 4, then x > 2". It fails for any x < -2, for example -3.',
                        wrong=[{'x': 3}, {'x': 1}, {'x': -2}]),
                 mc('"If P, then Q" is true. Which statement MUST also be true?', 'If not Q, then not P.',
                    [('If Q, then P.', 'the converse can be false'), ('If not P, then not Q.', 'the inverse can be false'),
                     ('P and Q.', 'P may be false')],
                    'Only the contrapositive is equivalent to the original.',
                    method='Automatic: checked in every row where "if P then Q" is true.',
                    check=lambda t: all({'If not Q, then not P.': imp(not q, not p), 'If Q, then P.': imp(q, p),
                                         'If not P, then not Q.': imp(not p, not q), 'P and Q.': p and q}[t]
                                        for p, q in itertools.product(TF, repeat=2) if imp(p, q))),
             ],
             back=[
                 B('Negate each part', 'prerequisite', 'The inverse and contrapositive need the negation of each part. '
                                                     'Students who negate wrongly build wrong forms.',
                   outcome='LOGIC.CONNECTIVE.01', qs=[
                       mc('What is the negation of "the shape has three sides"?', 'the shape does not have three sides',
                          [('the shape has four sides', 'too specific'), ('the shape has no sides', 'too specific'),
                           ('the shape has at least three sides', 'not a negation')], 'Put "not" on the whole claim.'),
                       mc('What is the negation of "n is even" for a whole number n?', 'n is odd',
                          [('n is zero', 'too specific'), ('n is prime', 'unrelated'), ('n is negative', 'unrelated')],
                          'Whole numbers that are not even are odd.'),
                       tf('The negation of "x > 3" is "x < 3".', False, 'It is "x ≤ 3".'),
                       mc('What is the negation of "it is raining"?', 'it is not raining',
                          [('it is sunny', 'it could be cloudy and dry'), ('it rained yesterday', 'unrelated'),
                           ('it will rain', 'unrelated')], 'Negate the whole claim.'),
                       tf('"Not (not P)" says the same as "not P".', False, 'Two negations cancel, so "not (not P)" says the same as P.'),
                   ]),
                 B('Hypothesis and conclusion', 'prerequisite', 'Converse and contrapositive swap the two parts; a student '
                                                              'must first identify which part is which.',
                   outcome='LOGIC.CONDITIONAL.01', qs=[
                       mc('In "If it snows, school is closed," what is the conclusion?', 'school is closed',
                          [('it snows', 'the hypothesis'), ('it is cold', 'not stated'), ('school is open', 'not stated')],
                          'The "then" part.'),
                       mc('Swap the parts of "If P, then Q". What do you get?', 'If Q, then P.',
                          [('If not P, then not Q.', 'that negates instead of swapping'),
                           ('If not Q, then not P.', 'that swaps AND negates'), ('P and Q.', 'not a conditional')],
                          'Swapping gives the converse.'),
                       tf('In "If x = 5, then x + 1 = 6," the conclusion is "x = 5".', False, 'The conclusion is the part after "then": "x + 1 = 6". "x = 5" is the hypothesis.'),
                       mc('Which statement has hypothesis "a figure is a square"?', 'If a figure is a square, then it is a '
                                                                                    'rectangle.',
                          [('If a figure is a rectangle, then it is a square.', 'hypothesis is "rectangle"'),
                           ('A figure is a rectangle only if it has four sides.', 'hypothesis is "a figure is a rectangle"'),
                           ('Every rectangle is a square.', 'hypothesis is "rectangle"')],
                          'The hypothesis is the "if" part: "a figure is a square".'),
                       tf('Swapping and negating both parts of "If P, then Q" gives "If not Q, then not P".', True,
                          'That is the contrapositive.'),
                   ]),
             ],
             f1=FW('Which forms are equivalent?', 'Harder: prove the equivalences with truth tables and test them.', [
                 tt('Complete the truth table for "if P then Q" and its contrapositive "if not Q then not P".', ['P', 'Q'],
                    [('if P then Q', imp), ('if not Q then not P', lambda p, q: imp(not q, not p))],
                    'The two columns are identical: a conditional and its contrapositive are equivalent.'),
                 mc('Which two statements are ALWAYS equivalent to each other?', 'the converse and the inverse',
                    [('the original and the converse', 'they differ when P is false and Q true'),
                     ('the original and the inverse', 'they differ when P is false and Q true'),
                     ('the converse and the contrapositive', 'they differ when P is false and Q true')],
                    'The inverse "if not P then not Q" is the contrapositive of the converse "if Q then P".',
                    check=lambda t: equiv(FORMS[t.split(' and ')[0].replace('the ', '')], FORMS[t.split(' and ')[1].replace('the ', '')])),
                 sa('For how many whole numbers n from 1 to 20 is the INVERSE of "If n is a multiple of 4, then n is even" '
                    'false?', 'Count:', '5', 'The inverse is "If n is not a multiple of 4, then n is not even". It is false '
                                             'when n is even but not a multiple of 4: 2, 6, 10, 14, 18.',
                    compute=lambda: str(sum(1 for n in range(1, 21) if not imp(n % 4 != 0, n % 2 != 0)))),
                 tf('If a conditional is false, its contrapositive is true.', False,
                    'A conditional and its contrapositive are equivalent, so they are always true or false together.'),
                 mc('"If a quadrilateral is a square, then its diagonals are equal." Which related statement is FALSE?',
                    'the converse: if the diagonals are equal, the quadrilateral is a square',
                    [('the contrapositive: if the diagonals are not equal, it is not a square', 'equivalent to the true '
                                                                                                'original'),
                     ('the original statement', 'true for every square'),
                     ('"a square has equal diagonals"', 'the original, restated')],
                    'A rectangle that is not a square has equal diagonals, so the converse is false.'),
             ]),
             f2=FW('Converses that hold and fail', 'Expert: decide when both a statement and its converse are true.', [
                 tf('For whole numbers, both "If n is odd, then n squared is odd" and its converse are true.', True,
                    'An odd number squared is odd; and if n were even, n squared would be even, so n squared odd forces n odd.',
                    check=lambda: all(imp(n % 2 == 1, n * n % 2 == 1) and imp(n * n % 2 == 1, n % 2 == 1) for n in range(0, 200))),
                 values('The statement "If n is prime and greater than 2, then n is odd" is true. Its converse is "If n is odd, '
                        'then n is prime and greater than 2". Give a whole number n that shows the converse is false.',
                        [('n', 'n =')], 'isOdd(n) and not (isPrime(n) and n > 2)', {'n': 9},
                        'Any odd number that is not a prime greater than 2: 1, 9, 15, 21, ...',
                        wrong=[{'n': 7}, {'n': 4}, {'n': 3}]),
                 mc('A statement and its converse are both true. Which statement must be true?', 'P if and only if Q',
                    [('P and Q', 'both could be false'), ('not P', 'P could be true'), ('P or Q', 'both could be false')],
                    'If P -> Q and Q -> P, then P and Q always match: that is "P if and only if Q".',
                    check=lambda t: all({'P if and only if Q': p == q, 'P and Q': p and q, 'not P': not p, 'P or Q': p or q}[t]
                                        for p, q in itertools.product(TF, repeat=2) if imp(p, q) and imp(q, p))),
                 sa('In how many of the 4 rows of a truth table do "if P then Q" and its converse "if Q then P" have DIFFERENT '
                    'truth values?', 'Rows:', '2', 'They differ when exactly one of P, Q is true: rows TF and FT.',
                    compute=lambda: str(sum(1 for p, q in itertools.product(TF, repeat=2) if imp(p, q) != imp(q, p)))),
                 mc('C is the conditional "if P then Q". Which statement is correct?',
                    'If C is true, its inverse may be true or false.',
                    [('If C is true, its converse is true.', 'when P is false and Q true, C is true but the converse is false'),
                     ('If C is false, its converse is false.', 'C is false only when P is true and Q false; then the converse '
                                                               '"if Q then P" is true'),
                     ('If C is true, its contrapositive may be false.', 'never: they are equivalent')],
                    'In the rows where C is true, the inverse is true for (T, T) and (F, F) and false for (F, T), so it may be '
                    'either.', method='Automatic: each claim tested in all four rows.',
                    check=lambda t: {
                        'If C is true, its inverse may be true or false.':
                            len({imp(not p, not q) for p, q in itertools.product(TF, repeat=2) if imp(p, q)}) == 2,
                        'If C is true, its converse is true.': all(imp(q, p) for p, q in itertools.product(TF, repeat=2) if imp(p, q)),
                        'If C is false, its converse is false.': all(not imp(q, p) for p, q in itertools.product(TF, repeat=2) if not imp(p, q)),
                        'If C is true, its contrapositive may be false.':
                            any(not imp(not q, not p) for p, q in itertools.product(TF, repeat=2) if imp(p, q))}[t]),
             ]))


# ------------------------------------------------------------------ Set 16: biconditionals
def s16():
    return S(16, 'Find truth values of "if and only if" statements and use them as definitions',
             main=[
                 tt('Complete the truth table for "P if and only if Q".', ['P', 'Q'], [('P if and only if Q', lambda p, q: p == q)],
                    'It is true exactly when P and Q have the same truth value.'),
                 tf('For real numbers x, "x squared = 9 if and only if x = 3" is true.', False,
                    'x = -3 makes the left part true and the right part false.'),
                 values('Find a real number x that makes "x > 5 if and only if x > 3" FALSE.', [('x', 'x =')],
                        '(x > 5) != (x > 3)', {'x': 4},
                        'The two parts must differ: x > 3 but not x > 5, so any x with 3 < x ≤ 5.',
                        wrong=[{'x': 6}, {'x': 2}, {'x': 3}]),
                 mc('Which statement is a correct DEFINITION of an even whole number?',
                    'A whole number is even if and only if it is divisible by 2.',
                    [('A whole number is even if it is divisible by 4.', 'true, but it leaves out 2, 6, 10, ...'),
                     ('A whole number is even only if it is greater than 1.', '0 is even'),
                     ('A whole number is even if and only if it ends in 0.', '4 is even and does not end in 0')],
                    'A definition must work both ways: every even number is divisible by 2, and every number divisible by 2 is '
                    'even.'),
                 mc('"P if and only if Q" is true and P is false. What follows?', 'Q is false.',
                    [('Q is true.', 'then P and Q would differ'), ('Nothing about Q.', 'Q must match P'),
                     ('P and Q are both true.', 'P is false')], 'In a true biconditional the two parts have the same value.'),
             ],
             back=[
                 B('Conditionals first', 'prerequisite', '"If and only if" joins two conditionals; students must know when '
                                                       'one conditional is true.', outcome='LOGIC.CONDITIONAL.01', qs=[
                     tf('"If 2 > 3, then 4 > 5" is true.', True, 'The "if" part is false.'),
                     tf('"If 3 > 2, then 4 > 5" is true.', False, 'True "if", false "then".'),
                     mc('When is "if P then Q" false?', 'when P is true and Q is false',
                        [('when P is false', 'it is true then'), ('when Q is true', 'it is true then'),
                         ('when both are false', 'it is true then')], 'Only one row is false.'),
                     tf('"If 4 > 1, then 2 > 6" is true.', False, 'The "if" part is true and the "then" part is false, which is the one case that makes a conditional false.'),
                     sa('In how many of the 4 rows is "if P then Q" true?', 'Rows:', '3', 'All rows except P true, Q false.',
                        compute=lambda: str(sum(1 for p, q in itertools.product(TF, repeat=2) if imp(p, q)))),
                 ]),
                 B('The converse', 'prerequisite', '"P if and only if Q" means the conditional AND its converse. Students '
                                                  'must be able to form the converse.', outcome='LOGIC.CONDITIONAL.03', qs=[
                     mc('What is the converse of "If it is a dog, then it barks"?', 'If it barks, then it is a dog.',
                        [('If it is not a dog, then it does not bark.', 'the inverse'),
                         ('If it does not bark, then it is not a dog.', 'the contrapositive'), ('It is a barking dog.', 'not '
                                                                                                                     'a conditional')],
                        'Swap the parts.'),
                     tf('The converse of "If n = 2, then n is even" is "If n is not 2, then n is not even".', False, 'That statement negates both parts; it is the inverse. The converse swaps the parts: "If n is even, then n = 2".'),
                     tf('The converse of a true statement is always true.', False, 'Example: "If n = 2, then n is even" is '
                                                                                   'true, its converse is false.'),
                     mc('"P if and only if Q" means "if P then Q" AND what?', 'if Q then P',
                        [('if not P then Q', 'not the converse'), ('P or Q', 'not part of it'), ('not P and not Q', 'not part '
                                                                                                                  'of it')],
                        'The other direction is the converse.'),
                     tf('If a conditional is true but its converse is false, the biconditional is true.', False,
                        'A biconditional needs both directions true; a false converse makes it false.'),
                 ]),
             ],
             f1=FW('Biconditionals as definitions and tests', 'Harder: count where a biconditional holds and test '
                                                             'definitions.', [
                 sa('For how many whole numbers n from 1 to 20 is "n is even if and only if n is a multiple of 4" TRUE?',
                    'Count:', '15', 'It fails exactly when n is even but not a multiple of 4: 2, 6, 10, 14, 18 (5 numbers). '
                                    'The other 15 make it true (odd numbers make both parts false).',
                    compute=lambda: str(sum(1 for n in range(1, 21) if (n % 2 == 0) == (n % 4 == 0)))),
                 tt('Complete the table to compare "P if and only if Q" with "(if P then Q) and (if Q then P)".', ['P', 'Q'],
                    [('P if and only if Q', lambda p, q: p == q), ('(if P then Q) and (if Q then P)', lambda p, q: imp(p, q) and imp(q, p))],
                    'The columns match in every row.'),
                 mc('Which definition of a SQUARE is correct (works in both directions)?',
                    'A quadrilateral is a square if and only if it has four equal sides and four right angles.',
                    [('A quadrilateral is a square if and only if it has four equal sides.', 'a rhombus with no right angles '
                                                                                           'has four equal sides'),
                     ('A quadrilateral is a square if and only if it has four right angles.', 'a non-square rectangle has '
                                                                                             'four right angles'),
                     ('A quadrilateral is a square if and only if its diagonals are equal.', 'a non-square rectangle has '
                                                                                            'equal diagonals')],
                    'Only the first condition is true of every square and of nothing else.'),
                 tf('"A whole number is divisible by 10 if and only if it ends in 0" is true.', True,
                    'Both directions hold for whole numbers.',
                    check=lambda: all((n % 10 == 0) == (str(n)[-1] == '0') for n in range(1, 1000))),
                 values('Find a whole number n that makes "n is divisible by 3 if and only if n is odd" FALSE.', [('n', 'n =')],
                        '(n % 3 == 0) != isOdd(n) and isInteger(n)', {'n': 6},
                        'The parts must differ: divisible by 3 but even (6, 12, ...) or odd but not divisible by 3 (1, 5, ...).',
                        wrong=[{'n': 9}, {'n': 4}, {'n': 15}]),
             ]),
             f2=FW('Chains and opposites of biconditionals', 'Expert: combine biconditionals and relate them to exclusive or.', [
                 tf('"P exclusive-or Q" has the opposite truth value of "P if and only if Q" in every row.', True,
                    'Exclusive-or is true exactly when the parts differ; the biconditional exactly when they match.',
                    check=lambda: all((p != q) == (not (p == q)) for p, q in itertools.product(TF, repeat=2))),
                 mc('"P iff Q" and "Q iff R" are both true. Which must be true?', 'P iff R',
                    [('P and R', 'all three could be false'), ('P exclusive-or R', 'P and R match'), ('not Q', 'Q could be true')],
                    'P matches Q and Q matches R, so P matches R.',
                    check=lambda t: all({'P iff R': p == r, 'P and R': p and r, 'P exclusive-or R': p != r, 'not Q': not q}[t]
                                        for p, q, r in itertools.product(TF, repeat=3) if p == q and q == r)),
                 sa('In how many of the 8 rows of a truth table for P, Q, R is "(P iff Q) iff R" true?', 'Rows:', '4',
                    'Exactly half of the rows: the statement is true when an even number of P, Q, R are false.',
                    compute=lambda: str(sum(1 for p, q, r in itertools.product(TF, repeat=3) if (p == q) == r))),
                 values('Find whole numbers a and b, each from 1 to 9, that make "a + b is even if and only if a is even" '
                        'TRUE and a different from b.', [('a', 'a ='), ('b', 'b =')],
                        '(isEven(a + b) == isEven(a)) and a != b and a >= 1 and a <= 9 and b >= 1 and b <= 9',
                        {'a': 2, 'b': 4},
                        'The biconditional is true exactly when b is even (then a + b and a have the same parity). Any a, b with '
                        'b even and a different from b works, such as 2 and 4 or 3 and 8.',
                        wrong=[{'a': 2, 'b': 3}, {'a': 4, 'b': 4}], search={'a': range(1, 10), 'b': range(1, 10)}),
                 mc('Which statement about whole numbers is TRUE?', 'n is odd if and only if n + 1 is even.',
                    [('n is odd if and only if n is prime.', '9 is odd, not prime; 2 is prime, not odd'),
                     ('n is even if and only if n is a multiple of 4.', '6 is even but not a multiple of 4'),
                     ('n is a multiple of 3 if and only if n is a multiple of 9.', '3 is a multiple of 3 but not of 9')],
                    'Adding 1 always changes parity, so n odd and n + 1 even always match.'),
             ]))


# ------------------------------------------------------------------ Set 17: truth-tellers and liars
RULES = ('On this island every person is either a truth-teller, who always tells the truth, or a liar, who always lies.')


def knights(names, st):
    out = []
    for v in itertools.product(TF, repeat=len(names)):
        a = dict(zip(names, v))
        if all(st[n](a) == a[n] for n in st):
            out.append(a)
    return out


def kgrid(prompt, names, st, why):
    lab = lambda b: 'truth-teller' if b else 'liar'
    sols = knights(names, st)
    assert len(sols) == 1, (prompt[:60], sols)
    return grid(RULES + ' ' + prompt + ' Mark each person as a truth-teller or a liar.', names, ['truth-teller', 'liar'],
                lambda a: all(st[n]({k: v == 'truth-teller' for k, v in a.items()}) == (a[n] == 'truth-teller') for n in st),
                why, distinct=False)


def s17():
    return S(17, 'Decide who tells the truth when each speaker always tells the truth or always lies',
             main=[
                 kgrid('Ana says: "Ben is a liar." Ben says: "Ana and I are both truth-tellers."', ['Ana', 'Ben'],
                       {'Ana': lambda a: not a['Ben'], 'Ben': lambda a: a['Ana'] and a['Ben']},
                       'If Ben were truthful, both would be truthful, but then Ana\'s "Ben is a liar" would be false. So Ben '
                       'lies, Ana\'s statement is true, and Ana is a truth-teller.'),
                 kgrid('Cal says: "Dee and I are different kinds." Dee says: "Cal is a liar."', ['Cal', 'Dee'],
                       {'Cal': lambda a: a['Cal'] != a['Dee'], 'Dee': lambda a: not a['Cal']},
                       'Suppose Cal tells the truth: they are different, so Dee is a liar, and Dee\'s claim "Cal is a liar" is '
                       'indeed false. Consistent. Suppose Cal lies: they are the same kind, so Dee lies too, but then "Cal is a '
                       'liar" would be true, a contradiction. So Cal is truthful and Dee lies.'),
                 kgrid('Eve says: "Fin and Gia are both liars." Fin says: "Eve is a truth-teller." Gia says: "Fin is a liar."',
                       ['Eve', 'Fin', 'Gia'],
                       {'Eve': lambda a: (not a['Fin']) and (not a['Gia']), 'Fin': lambda a: a['Eve'], 'Gia': lambda a: not a['Fin']},
                       'Fin and Eve stand or fall together (Fin says Eve is truthful). If both were truthful, Eve\'s claim would '
                       'make Fin a liar: contradiction. So Eve and Fin are liars. Then Gia\'s "Fin is a liar" is true, so Gia '
                       'is truthful (and Eve\'s claim is indeed false).'),
                 kgrid('Jo says: "Kai is a liar." Kai says: "Lu is a liar." Lu says: "Jo and Kai are both liars."',
                       ['Jo', 'Kai', 'Lu'],
                       {'Jo': lambda a: not a['Kai'], 'Kai': lambda a: not a['Lu'], 'Lu': lambda a: (not a['Jo']) and (not a['Kai'])},
                       'If Lu were truthful, Jo and Kai would both lie, but Jo lying means Kai is truthful: contradiction. So Lu '
                       'lies; then Kai\'s "Lu is a liar" is true, Kai is truthful, and Jo (who calls Kai a liar) lies.'),
                 mc(RULES + ' Mo says: "Exactly one of Ned and Ola is a liar." Ned says: "Mo is a liar." Ola says: "Ned and I '
                            'are the same kind." Who is a liar?', 'Mo only',
                    [('Ned only', 'then Mo and Ola are truthful, but Ola would be claiming Ned and Ola are the same kind'),
                     ('Ola only', 'then Ned is truthful and calls Mo a liar, but Mo would be truthful'),
                     ('Mo and Ned', 'then Ola is truthful, but Ola says Ned and Ola are the same kind')],
                    'Check the 8 possibilities: only Mo lying, with Ned and Ola truthful, is consistent. Ned truthfully says '
                    'Mo lies; Ola truthfully says Ned and Ola match; Mo\'s claim "exactly one of Ned and Ola lies" is false.',
                    method='Automatic: all 8 assignments checked.',
                    check=lambda t: knights(['Mo', 'Ned', 'Ola'], {'Mo': lambda a: a['Ned'] != a['Ola'], 'Ned': lambda a: not a['Mo'],
                                                                 'Ola': lambda a: a['Ned'] == a['Ola']})
                    == [{'Mo': False, 'Ned': True, 'Ola': True}] and t == 'Mo only'),
             ],
             back=[B('Strategy: suppose, then test', 'guided_strategy',
                     'Students guess and then stop. Supposing one speaker is truthful, following the consequences, and '
                     'switching when a contradiction appears is a complete method.',
                     lesson=lesson('Suppose, then test',
                                   ['Pick one speaker and SUPPOSE that person tells the truth.',
                                    'Then everything that person says is true. Use it to decide others, one step at a time. A '
                                    'liar\'s statement must be false.',
                                    'If you reach a contradiction, the supposition was wrong: that speaker is a liar. Start '
                                    'again with that fact.',
                                    'When every statement agrees with the speaker\'s type, you have a solution. Check that no '
                                    'other choice works if the question expects one answer.'],
                                   'Worked example (different people)',
                                   ['Pip says: "Rue and I are both liars." Rue says nothing. Who is what?'],
                                   ['Suppose Pip is truthful. Then Pip is a liar: contradiction.',
                                    'So Pip is a liar, and "Rue and I are both liars" is false.',
                                    'Pip IS a liar, so for the statement to be false, Rue must be a truth-teller.',
                                    'Answer: Pip liar, Rue truth-teller.']),
                     qs=[
                         tf(RULES + ' A truth-teller can say "I am a liar."', False, 'That would be a false statement.'),
                         tf(RULES + ' A liar can say "I am a truth-teller."', True, 'That is a false statement, which a liar '
                                                                                   'can make.'),
                         mc(RULES + ' Vic says: "2 + 2 = 5." What is Vic?', 'a liar', [('a truth-teller', 'the statement is '
                                                                                                         'false'),
                                                                                      ('either', 'only liars make false '
                                                                                                 'statements'),
                                                                                      ('neither', 'everyone is one or the other')],
                            'A false statement comes from a liar.'),
                         mc(RULES + ' Wes is a truth-teller and says: "Xia is a liar." What is Xia?', 'a liar',
                            [('a truth-teller', 'Wes speaks truly'), ('either', 'Wes\'s true statement decides it'),
                             ('neither', 'everyone is one or the other')], 'Wes tells the truth.'),
                         mc(RULES + ' Yan is a liar and says: "Zed is a liar." What is Zed?', 'a truth-teller',
                            [('a liar', 'Yan\'s statement is false'), ('either', 'it is decided'),
                             ('neither', 'everyone is one or the other')], 'The statement is false, so Zed is not a liar.'),
                     ])],
             f1=FW('Statements about counts', 'Harder: speakers who talk about how many liars there are.', [
                 kgrid('Ash says: "Exactly one of us three is a truth-teller." Bly says: "Exactly two of us three are '
                       'truth-tellers." Cru says: "None of us three is a truth-teller."', ['Ash', 'Bly', 'Cru'],
                       {'Ash': lambda a: sum(a.values()) == 1, 'Bly': lambda a: sum(a.values()) == 2,
                        'Cru': lambda a: sum(a.values()) == 0},
                       'The three claims contradict each other, so at most one is true. Cru cannot be truthful (that would make '
                       'none truthful). If none were truthful, Cru\'s claim would be true: contradiction. So exactly one is '
                       'truthful, which makes Ash\'s claim true: Ash is the truth-teller.'),
                 kgrid('Dov says: "At least one of Ela and Fyn is a liar." Ela says: "Dov and Fyn are both truth-tellers." Fyn '
                       'says: "Dov is a liar."', ['Dov', 'Ela', 'Fyn'],
                       {'Dov': lambda a: not a['Ela'] or not a['Fyn'], 'Ela': lambda a: a['Dov'] and a['Fyn'],
                        'Fyn': lambda a: not a['Dov']},
                       'Suppose Dov truthful: then Fyn ("Dov is a liar") lies, so '
                       'Ela\'s claim is false and Ela lies; Dov\'s claim (one of Ela, Fyn lies) is true. Consistent. Suppose '
                       'Dov lies: then Ela and Fyn are both truthful, but Ela says Dov is truthful: contradiction. So Dov is '
                       'truthful, Ela and Fyn lie.'),
                 kgrid('Pat says: "Exactly two of us three are truth-tellers." Quy says: "Pat is a liar." Ren says: "Quy and '
                       'Pat are the same kind."', ['Pat', 'Quy', 'Ren'],
                       {'Pat': lambda a: sum(a.values()) == 2, 'Quy': lambda a: not a['Pat'], 'Ren': lambda a: a['Quy'] == a['Pat']},
                       'Quy and Pat are always different kinds (Quy calls Pat a liar), so Ren\'s claim is false: Ren lies. Then '
                       'exactly one of Pat, Quy is truthful, so the number of truth-tellers is 1, Pat\'s claim is false, Pat '
                       'lies and Quy is truthful.'),
                 tf(RULES + ' If two people each say "The other one is a liar," then exactly one of them is a liar.', True,
                    'If A is truthful, B lies; if A lies, B is truthful. Either way they are different.',
                    check=lambda: all(len(set(s.values())) == 2 for s in knights(['A', 'B'], {'A': lambda a: not a['B'],
                                                                                              'B': lambda a: not a['A']}))),
                 sa(RULES + ' Four people each say exactly the same sentence: "Exactly one of us four is a truth-teller." '
                            'How many of them are truth-tellers?', 'Truth-tellers:', '0',
                    'They say the same sentence, so they are all the same kind. If all were truthful, there would be four '
                    'truth-tellers, not one: impossible. So all four lie, and indeed the sentence is false (there are none).',
                    compute=lambda: str(sum(knights(list('ABCD'), {n: (lambda a: sum(a.values()) == 1) for n in 'ABCD'})[0].values()))),
             ]),
             f2=FW('Larger systems and impossible statements', 'Expert: four speakers, and statements no one can make.', [
                 kgrid('Uri says: "Exactly three of us four are liars." Vee says: "Uri is a truth-teller." Wil says: "Vee is a '
                       'liar." Xan says: "Wil is a truth-teller and Uri is a liar."', ['Uri', 'Vee', 'Wil', 'Xan'],
                       {'Uri': lambda a: sum(not x for x in a.values()) == 3, 'Vee': lambda a: a['Uri'],
                        'Wil': lambda a: not a['Vee'], 'Xan': lambda a: a['Wil'] and not a['Uri']},
                       'Vee and Uri are the same kind; Wil is the opposite of Vee. If Uri were truthful, Vee would be too, and '
                       'at most two could lie: contradiction with "exactly three". So Uri and Vee lie and Wil is truthful. '
                       'Xan\'s claim (Wil truthful, Uri lying) is true, so Xan is truthful. Two liars: Uri\'s claim is false, '
                       'as it must be.'),
                 mc(RULES + ' Which statement can NO person on the island say?', '"I am a liar."',
                    [('"I am a truth-teller."', 'anyone can say it: true for a truth-teller, false for a liar'),
                     ('"2 + 2 = 4."', 'a truth-teller can say it'), ('"2 + 2 = 5."', 'a liar can say it')],
                    'A truth-teller saying it would be lying; a liar saying it would be telling the truth.'),
                 sa(RULES + ' Five people stand in a circle. Each says: "The person on my left is a liar." In how many ways '
                            'can the five be truth-tellers and liars so that every statement fits?', 'Ways:', '0',
                    'Each statement makes neighbors different kinds, so the types must alternate around the circle. An odd '
                    'circle cannot alternate (going once around returns to the start after 5 changes), so no assignment works.',
                    compute=lambda: str(len(knights(['P1', 'P2', 'P3', 'P4', 'P5'],
                                                    {'P%d' % (i + 1): (lambda a, i=i: not a['P%d' % ((i + 1) % 5 + 1)]) for i in range(5)})))),
                 tf(RULES + ' A person says: "I am a liar or 2 + 2 = 4." This person must be a truth-teller.', True,
                    'The statement is true (2 + 2 = 4), so the speaker tells the truth. A liar could not say a true statement.',
                    check=lambda: knights(['X'], {'X': lambda a: (not a['X']) or True}) == [{'X': True}]),
                 mc(RULES + ' You meet Gil and Hal. Gil says: "At least one of us two is a truth-teller." Hal says nothing. '
                            'Which statement MUST be true?', 'If Hal is a truth-teller, then Gil is a truth-teller.',
                    [('Gil is a truth-teller.', 'Gil and Hal could both be liars: then Gil\'s claim is false, as a liar\'s '
                                                'must be'),
                     ('Hal is a liar.', 'Gil and Hal could both be truth-tellers'),
                     ('Both are liars.', 'Gil could be a truth-teller')],
                    'Three cases fit: both truthful; Gil truthful and Hal lying; both lying. In every case where Hal is '
                    'truthful, Gil\'s claim is true, so Gil is truthful.',
                    method='Automatic: all 4 assignments checked; 3 fit.',
                    check=lambda t: all({'If Hal is a truth-teller, then Gil is a truth-teller.': imp(a['H'], a['G']),
                                         'Gil is a truth-teller.': a['G'], 'Hal is a liar.': not a['H'],
                                         'Both are liars.': not a['G'] and not a['H']}[t]
                                        for a in knights(['G', 'H'], {'G': lambda a: a['G'] or a['H']}))),
             ]))


# ------------------------------------------------------------------ Set 18: truth tables
def s18():
    return S(18, 'Complete truth tables for compound statements',
             main=[
                 tt('Complete the truth table for "P and (not Q)".', ['P', 'Q'], [('not Q', lambda p, q: not q),
                                                                                  ('P and (not Q)', lambda p, q: p and not q)],
                    'First fill "not Q", then combine with P: true only when P is true and Q is false.'),
                 tt('Complete the truth table for "(not P) or Q".', ['P', 'Q'], [('not P', lambda p, q: not p),
                                                                                 ('(not P) or Q', lambda p, q: (not p) or q)],
                    'False only when P is true and Q is false (it matches "if P then Q").'),
                 tt('Complete the truth table for "(P or Q) and not (P and Q)".', ['P', 'Q'],
                    [('P or Q', lambda p, q: p or q), ('P and Q', lambda p, q: p and q),
                     ('(P or Q) and not (P and Q)', lambda p, q: (p or q) and not (p and q))],
                    'True exactly when one of P, Q is true: exclusive or.'),
                 sa('A truth table for three statements P, Q and R lists every combination of truth values. How many rows does '
                    'it have?', 'Rows:', '8', 'Each statement has 2 values: 2 x 2 x 2 = 8.', compute=lambda: str(2 ** 3)),
                 tt('Complete the truth table for "(P and Q) or R".', ['P', 'Q', 'R'],
                    [('P and Q', lambda p, q, r: p and q), ('(P and Q) or R', lambda p, q, r: (p and q) or r)],
                    'True when R is true or both P and Q are true.'),
             ],
             back=[
                 B('The basic connectives', 'prerequisite', 'A compound table is built from the tables of "not", "and", '
                                                           '"or". Students must know those by heart.',
                   outcome='LOGIC.CONNECTIVE.02', qs=[
                       tt('Complete the truth table for "P and Q".', ['P', 'Q'], [('P and Q', lambda p, q: p and q)],
                          'True only when both are true.'),
                       tt('Complete the truth table for "P or Q" (inclusive).', ['P', 'Q'], [('P or Q', lambda p, q: p or q)],
                          'False only when both are false.'),
                       tt('Complete the truth table for "not P".', ['P'], [('not P', lambda p: not p)], 'Flip the value.'),
                       tf('"P and Q" is true when P is true and Q is false.', False, 'Both must be true.'),
                       tf('"P or Q" is true when P is false and Q is true.', True, 'At least one is true.'),
                   ]),
                 B('Work from the inside out', 'prerequisite', 'Students who combine parts in the wrong order get wrong '
                                                             'columns. Brackets tell which part to compute first.', qs=[
                     mc('In "not (P and Q)", which part is computed first?', 'P and Q', [('not P', '"not" applies to the '
                                                                                                 'whole bracket'),
                                                                                        ('not Q', 'same reason'),
                                                                                        ('P or Q', 'not in the statement')],
                        'Inside the brackets first.'),
                     tf('"not (P and Q)" and "(not P) and Q" always have the same truth value.', False,
                        'P true, Q true: the first is false and the second false; P false, Q false: the first is true and the '
                        'second false.', check=lambda: all((not (p and q)) == ((not p) and q) for p, q in itertools.product(TF, repeat=2))),
                     sa('P is true and Q is false. Is "not (P and Q)" true or false? Enter 1 for true or 0 for false.',
                        'Value (1 or 0):', '1', 'P and Q is false, so its negation is true.',
                        compute=lambda: str(int(not (True and False)))),
                     mc('P is false, Q is true. What is the value of "(P or Q) and P"?', 'false',
                        [('true', 'the final "and P" is false'), ('it cannot be found', 'all parts are known'),
                         ('both', 'a statement has one value')], 'P or Q is true; true and false is false.'),
                     tt('Complete the truth table for "not (P or Q)".', ['P', 'Q'], [('P or Q', lambda p, q: p or q),
                                                                                     ('not (P or Q)', lambda p, q: not (p or q))],
                        'Compute the bracket, then negate.'),
                 ]),
             ],
             f1=FW('Three-variable tables', 'Harder: more rows and nested brackets.', [
                 tt('Complete the truth table for "P and (Q or R)".', ['P', 'Q', 'R'],
                    [('Q or R', lambda p, q, r: q or r), ('P and (Q or R)', lambda p, q, r: p and (q or r))],
                    'True when P is true and at least one of Q, R is true.'),
                 tt('Complete the truth table for "(P or Q) and (not R)".', ['P', 'Q', 'R'],
                    [('P or Q', lambda p, q, r: p or q), ('(P or Q) and (not R)', lambda p, q, r: (p or q) and not r)],
                    'True when R is false and at least one of P, Q is true.'),
                 sa('In how many of the 8 rows is "P or (Q and R)" true?', 'Rows:', '5',
                    'True whenever P is true (4 rows) plus the row P false, Q true, R true: 5.',
                    compute=lambda: str(sum(1 for p, q, r in itertools.product(TF, repeat=3) if p or (q and r)))),
                 mc('A statement in P and Q is true only in the row P true, Q false. Which statement is it?',
                    'P and (not Q)', [('P or (not Q)', 'also true when both are true and when both are false'),
                                      ('(not P) and Q', 'true only when P is false and Q true'),
                                      ('not (P and Q)', 'true in three rows')],
                    'Check each candidate in the four rows.',
                    check=lambda t: [{'P and (not Q)': p and not q, 'P or (not Q)': p or not q, '(not P) and Q': (not p) and q,
                                      'not (P and Q)': not (p and q)}[t] for p, q in itertools.product(TF, repeat=2)]
                    == [False, True, False, False]),
                 tf('A truth table for 4 statements has 16 rows.', True, '2 x 2 x 2 x 2 = 16.', check=lambda: 2 ** 4 == 16),
             ]),
             f2=FW('Read and build statements from tables', 'Expert: find statements that match a given column.', [
                 mc('A statement in P, Q, R is true in exactly the rows where an odd number of P, Q, R are true. Which statement '
                    'is it?', 'P exclusive-or (Q exclusive-or R)',
                    [('P or Q or R', 'true also when two are true'), ('P and Q and R', 'true only when all three are true'),
                     ('(P and Q) or R', 'true in rows with two true')],
                    'Exclusive-or flips the value each time a true part is added.',
                    check=lambda t: all({'P exclusive-or (Q exclusive-or R)': p != (q != r), 'P or Q or R': p or q or r,
                                         'P and Q and R': p and q and r, '(P and Q) or R': (p and q) or r}[t]
                                        == ((p + q + r) % 2 == 1) for p, q, r in itertools.product(TF, repeat=3))),
                 sa('How many different possible output columns can a truth table with two statement letters P and Q have (4 '
                    'rows, each output T or F)?', 'Columns:', '16', 'Each of the 4 rows can be T or F: 2 to the 4th = 16.',
                    compute=lambda: str(2 ** 4)),
                 tt('Complete the truth table for "(P and not Q) or (not P and Q)".', ['P', 'Q'],
                    [('P and not Q', lambda p, q: p and not q), ('not P and Q', lambda p, q: (not p) and q),
                     ('(P and not Q) or (not P and Q)', lambda p, q: (p and not q) or ((not p) and q))],
                    'Each row where exactly one is true makes one bracket true.'),
                 sa('In how many of the 16 rows of a table for P, Q, R, S is "(P and Q) or (R and S)" true?', 'Rows:', '7',
                    'P and Q true: 4 rows; R and S true: 4 rows; both: 1 row. 4 + 4 - 1 = 7.',
                    compute=lambda: str(sum(1 for p, q, r, s_ in itertools.product(TF, repeat=4) if (p and q) or (r and s_)))),
                 tf('Every truth-table column for P and Q can be produced by some statement using only "not", "and", "or".',
                    True, 'For each true row write a bracket like "P and not Q", then join the brackets with "or" (for the all-F '
                          'column use "P and not P").'),
             ]))


SETS = [s15(), s16(), s17(), s18()]
