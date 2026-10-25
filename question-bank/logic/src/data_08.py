"""Logic sets 21-24: valid inference forms; tempting invalid forms; cube nets; valid versus sound."""
import itertools
from lq import S, B, FW, mc, figmc, tf, sa, order, values, lesson, grid, tt
import figs
import pz

TF = [True, False]


def imp(p, q):
    return (not p) or q


def valid(premises, conclusion, n=2):
    """An argument form is valid when no row makes every premise true and the conclusion false."""
    return all(conclusion(*v) for v in itertools.product(TF, repeat=n) if all(f(*v) for f in premises))


MP = ([lambda p, q: imp(p, q), lambda p, q: p], lambda p, q: q)
MT = ([lambda p, q: imp(p, q), lambda p, q: not q], lambda p, q: not p)
AC = ([lambda p, q: imp(p, q), lambda p, q: q], lambda p, q: p)
DA = ([lambda p, q: imp(p, q), lambda p, q: not p], lambda p, q: not q)
DS = ([lambda p, q: p or q, lambda p, q: not p], lambda p, q: q)
for _f, _v in ((MP, True), (MT, True), (AC, False), (DA, False), (DS, True)):
    assert valid(*_f) == _v


# ------------------------------------------------------------------ Set 21: valid inference forms
def s21():
    return S(21, 'Draw valid conclusions with modus ponens, modus tollens, chains and disjunctive syllogism',
             main=[
                 mc('Premises: "If the reservoir is full, the dam gates open." "The reservoir is full." What conclusion '
                    'follows?', 'The dam gates open.', [('The reservoir is not full.', 'contradicts a premise'),
                                                        ('The dam gates do not open.', 'contradicts the conditional'),
                                                        ('Nothing follows.', 'modus ponens gives a conclusion')],
                    'Modus ponens: if P then Q; P; therefore Q.', method='Automatic: the form was checked by truth table.'),
                 mc('Premises: "If a number is divisible by 9, it is divisible by 3." "The number 52 is not divisible by 3." '
                    'What follows?', '52 is not divisible by 9.', [('52 is divisible by 9.', 'contradicts the premises'),
                                                                 ('52 is divisible by 3.', 'contradicts a premise'),
                                                                 ('Nothing follows.', 'modus tollens gives a conclusion')],
                    'Modus tollens: if P then Q; not Q; therefore not P.'),
                 order('Arrange the steps of the argument so that each line follows from earlier ones and the conclusion comes '
                       'last.', [('A', 'If the trail is icy, the park closes.'), ('B', 'If the park closes, the race is '
                                                                                      'cancelled.'),
                                 ('C', 'The trail is icy.'), ('D', 'So the park closes.'), ('E', 'So the race is cancelled.')],
                       lambda p: p[-1] == 'E' and p.index('D') > max(p.index('A'), p.index('C'))
                       and p.index('E') > max(p.index('B'), p.index('D')) and p.index('D') < p.index('E')
                       and list(p) in (['A', 'C', 'D', 'B', 'E'], ['C', 'A', 'D', 'B', 'E'], ['A', 'B', 'C', 'D', 'E']),
                       'Use the first rule with the fact to get "the park closes", then the second rule to get the conclusion. '
                       'The two rules may also be stated first.', expect=['A', 'C', 'D', 'B', 'E']),
                 mc('Premises: "The key is in the drawer or in the coat." "The key is not in the drawer." What follows?',
                    'The key is in the coat.', [('The key is in the drawer.', 'contradicts a premise'),
                                                ('The key is in neither place.', 'contradicts the first premise'),
                                                ('Nothing follows.', 'disjunctive syllogism gives a conclusion')],
                    'Disjunctive syllogism: P or Q; not P; therefore Q.'),
                 tf('This argument is valid: "If P then Q. If Q then R. So if P then R."', True,
                    'If P is true, the first premise gives Q and the second gives R (a chain, or hypothetical syllogism).',
                    check=lambda: valid([lambda p, q, r: imp(p, q), lambda p, q, r: imp(q, r)], lambda p, q, r: imp(p, r), 3)),
             ],
             back=[
                 B('When is a conditional true?', 'prerequisite', 'Valid forms work because of when "if...then" is true and '
                                                                 'false; students who misread conditionals misapply them.',
                   outcome='LOGIC.CONDITIONAL.01', qs=[
                       tf('"If P then Q" is false when P is false and Q is true.', False, 'With P false the conditional makes no promise, so it is true. It is false only when P is true and Q is false.'),
                       tf('"If P then Q" is false when P is false.', False, 'It is true whenever P is false.'),
                       mc('"If P then Q" is true and P is true. What is Q?', 'true', [('false', 'then the conditional would be '
                                                                                              'false'),
                                                                                     ('either', 'Q is forced'),
                                                                                     ('neither', 'Q has a value')],
                          'The only row with P true and the conditional true has Q true.'),
                       mc('"If P then Q" is true and Q is false. What is P?', 'false', [('true', 'then the conditional would be '
                                                                                                'false'),
                                                                                       ('either', 'P is forced'),
                                                                                       ('neither', 'P has a value')],
                          'The only row with Q false and the conditional true has P false.'),
                       tf('"If P then Q" is true and Q is true. P must be true.', False, 'P can be false.'),
                   ]),
                 B('Using "or" and "not"', 'prerequisite', 'Disjunctive syllogism needs inclusive "or" and negation.',
                   outcome='LOGIC.CONNECTIVE.02', qs=[
                       tf('"P or Q" is true and P is true. Then Q must be false.', False, 'Inclusive "or" allows both parts to be true, so Q could be true or false.'),
                       tf('"P or Q" is true and P is true. Then Q is false.', False, 'Inclusive or allows both.'),
                       mc('"The meeting is on Monday or Tuesday." It is not on Monday. When is it?', 'Tuesday',
                          [('Monday', 'ruled out'), ('neither day', 'the premise says one of them'),
                           ('it cannot be told', 'only Tuesday is left')], 'Eliminate Monday.'),
                       mc('Which is the negation of "the light is on"?', 'the light is not on',
                          [('the light is dim', 'not a negation'), ('the lamp is broken', 'unrelated'),
                           ('the light is bright', 'not a negation')], 'Put "not" on the claim.'),
                       tf('"P or Q" is true and both P and Q could be true.', True, 'Inclusive or.'),
                   ]),
             ],
             f1=FW('Longer chains of valid steps', 'Harder: combine several forms in one argument.', [
                 mc('Premises: "If it is a holiday, the bank is closed." "If the bank is closed, Mara cannot deposit." "Mara '
                    'deposited." What follows?', 'It is not a holiday.', [('It is a holiday.', 'contradicts the premises'),
                                                                          ('The bank is closed.', 'contradicts the premises'),
                                                                          ('Nothing follows.', 'two steps of modus tollens '
                                                                                               'give a conclusion')],
                    'Mara deposited, so the bank was not closed (modus tollens); so it is not a holiday (modus tollens again).',
                    check=lambda t: valid([lambda h, c, d: imp(h, c), lambda h, c, d: imp(c, not d), lambda h, c, d: d],
                                          {'It is not a holiday.': lambda h, c, d: not h, 'It is a holiday.': lambda h, c, d: h,
                                           'The bank is closed.': lambda h, c, d: c,
                                           'Nothing follows.': lambda h, c, d: False}[t], 3)),
                 tf('Valid: "P or Q. If P then R. If Q then R. So R."', True, 'Either way R follows (proof by cases).',
                    check=lambda: valid([lambda p, q, r: p or q, lambda p, q, r: imp(p, r), lambda p, q, r: imp(q, r)],
                                        lambda p, q, r: r, 3)),
                 mc('Premises: "Ana or Ben will host." "If Ben hosts, the party is on Friday." "The party is not on Friday." '
                    'Who hosts?', 'Ana', [('Ben', 'then the party would be on Friday'), ('both', 'Ben does not host'),
                                          ('it cannot be told', 'the premises decide it')],
                    'Not Friday, so Ben does not host (modus tollens); Ana or Ben hosts, so Ana does (disjunctive syllogism).',
                    check=lambda t: valid([lambda a, b, f: a or b, lambda a, b, f: imp(b, f), lambda a, b, f: not f],
                                          {'Ana': lambda a, b, f: a and not b, 'Ben': lambda a, b, f: b,
                                           'both': lambda a, b, f: a and b, 'it cannot be told': lambda a, b, f: False}[t], 3)),
                 order('Arrange into a valid argument ending with the conclusion "The fountain is off."',
                       [('A', 'If the fountain is on, the pump runs.'), ('B', 'The pump does not run.'),
                        ('C', 'So the fountain is off.')],
                       lambda p: p[-1] == 'C', 'Modus tollens: the rule and the fact (in either order), then the conclusion.',
                       expect=['A', 'B', 'C']),
                 tf('Valid: "If P then Q. Not Q. So not P."', True, 'Modus tollens.', check=lambda: valid(*MT)),
             ]),
             f2=FW('Valid forms with several variables', 'Expert: decide validity of new forms with truth tables.', [
                 tf('Valid: "If P then (Q and R). Not R. So not P."', True,
                    'If P were true, R would be true; R is false, so P is false.',
                    check=lambda: valid([lambda p, q, r: imp(p, q and r), lambda p, q, r: not r], lambda p, q, r: not p, 3)),
                 tf('Valid: "If P then (Q or R). Not Q. So R."', False,
                    'P may be false: P false, Q false, R false makes both premises true and the conclusion false.',
                    check=lambda: valid([lambda p, q, r: imp(p, q or r), lambda p, q, r: not q], lambda p, q, r: r, 3)),
                 mc('Premises: "If A then B." "If C then D." "A or C." Which conclusion follows?', 'B or D',
                    [('B and D', 'only one of A and C need be true'), ('A and C', 'only one is given'),
                     ('not B', 'contradicts a possible case')],
                    'If A, then B; if C, then D; one of A, C holds, so one of B, D holds (constructive dilemma).',
                    check=lambda t: valid([lambda a, b, c, d: imp(a, b), lambda a, b, c, d: imp(c, d), lambda a, b, c, d: a or c],
                                          {'B or D': lambda a, b, c, d: b or d, 'B and D': lambda a, b, c, d: b and d,
                                           'A and C': lambda a, b, c, d: a and c, 'not B': lambda a, b, c, d: not b}[t], 4)),
                 sa('An argument has premises "P or Q" and "if P then R" and conclusion "Q or R". In how many of the 8 rows of '
                    'its truth table are both premises true?', 'Rows:', '4', 'Count the rows where P or Q is true and P -> R '
                                                                              'is true: TTT, FTT, FTF, TFT.',
                    compute=lambda: str(sum(1 for p, q, r in itertools.product(TF, repeat=3) if (p or q) and imp(p, r)))),
                 tf('The argument "P or Q. If P then R. So Q or R." is valid.', True,
                    'In each row where both premises are true, Q or R is true.',
                    check=lambda: valid([lambda p, q, r: p or q, lambda p, q, r: imp(p, r)], lambda p, q, r: q or r, 3)),
             ]))


# ------------------------------------------------------------------ Set 22: tempting invalid inferences
def s22():
    return S(22, 'Recognize affirming the consequent and denying the antecedent',
             main=[
                 mc('"If a phone is waterproof, it survives a fall into a pool. Leo\'s phone survived a fall into a pool. So '
                    'Leo\'s phone is waterproof." What is wrong with this argument?',
                    'It affirms the consequent: the phone may have survived for another reason.',
                    [('Nothing: it is modus ponens.', 'modus ponens starts from the "if" part, not the "then" part'),
                     ('It denies the antecedent.', 'no premise says "not waterproof"'),
                     ('A premise is false.', 'the problem is the form, whatever the premises')],
                    'From "if P then Q" and Q, P does not follow.', check=lambda t: t.startswith('It affirms') and not valid(*AC)),
                 mc('"If n is a multiple of 4, then n is even. 6 is not a multiple of 4. So 6 is not even." What is wrong?',
                    'It denies the antecedent: not P does not give not Q.',
                    [('Nothing: it is modus tollens.', 'modus tollens starts from not Q'),
                     ('It affirms the consequent.', 'no premise says "6 is even"'), ('The conditional is false.', 'it is true')],
                    'The conclusion is false (6 is even) even though both premises are true, so the form is invalid.',
                    check=lambda t: t.startswith('It denies') and not valid(*DA)),
                 tf('This form is valid: "If P then Q. Q. So P."', False, 'P false, Q true makes both premises true and the '
                                                                         'conclusion false.', check=lambda: valid(*AC)),
                 values('Use whole numbers to show that "If n is a multiple of 6, then n is even. n is even. So n is a multiple '
                        'of 6." is invalid: give a value of n that makes both premises true and the conclusion false.',
                        [('n', 'n =')], 'isEven(n) and n % 6 != 0', {'n': 4},
                        'Any even number that is not a multiple of 6 (2, 4, 8, 10, ...): the conditional is always true, n is '
                        'even, and n is not a multiple of 6.', wrong=[{'n': 6}, {'n': 3}, {'n': 12}]),
                 mc('Which argument is VALID?', '"If it rains, the game is off. The game is not off. So it is not raining."',
                    [('"If it rains, the game is off. The game is off. So it is raining."', 'affirms the consequent'),
                     ('"If it rains, the game is off. It is not raining. So the game is not off."', 'denies the antecedent'),
                     ('"If it rains, the game is off. So if the game is off, it rains."', 'concludes the converse')],
                    'Only the modus tollens argument is valid.'),
             ],
             back=[
                 B('Valid forms first', 'prerequisite', 'Invalid forms are recognized by comparing them with the valid forms '
                                                       'they imitate.', outcome='LOGIC.INFERENCE.01', qs=[
                     mc('"If P then Q. P. So Q." What is this form called?', 'modus ponens',
                        [('modus tollens', 'that uses not Q'), ('affirming the consequent', 'that uses Q as a premise'),
                         ('denying the antecedent', 'that uses not P')], 'Affirm the "if" part.'),
                     mc('"If P then Q. Not Q. So not P." What is this form called?', 'modus tollens',
                        [('modus ponens', 'that uses P'), ('denying the antecedent', 'that uses not P'),
                         ('affirming the consequent', 'that uses Q')], 'Deny the "then" part.'),
                     tf('Modus ponens is valid.', True, 'Truth table check.', check=lambda: valid(*MP)),
                     tf('Modus tollens is valid.', True, 'Truth table check.', check=lambda: valid(*MT)),
                     mc('In modus ponens, which part of the conditional is given as a fact?', 'the "if" part',
                        [('the "then" part', 'that would affirm the consequent'), ('neither part', 'one part is given'),
                         ('the negation of the "if" part', 'that would deny the antecedent')], 'P is given.'),
                 ]),
                 B('A counterexample shows invalidity', 'prerequisite', 'Students see that an invalid form "feels" right; a '
                                                                       'case with true premises and a false conclusion '
                                                                       'proves it is invalid.', outcome='LOGIC.QUANT.03', qs=[
                     tf('An argument form is invalid if there is one case with all premises true and the conclusion false.', True,
                        'One such case is enough.'),
                     mc('"If x > 5, then x > 2. x > 2. So x > 5." Which value of x shows it is invalid?', '3',
                        [('6', 'the conclusion is true'), ('1', 'the premise x > 2 is false'), ('10', 'the conclusion is true')],
                        'x = 3: both premises true, conclusion false.',
                        check=lambda t: (lambda x: imp(x > 5, x > 2) and x > 2 and not x > 5)(int(t))),
                     tf('A valid argument can have true premises and a false conclusion.', False, 'That is what validity '
                                                                                                   'rules out.'),
                     mc('"If an animal is a robin, it has wings. A bat has wings. So a bat is a robin." Which fact shows the '
                        'form is invalid?', 'A bat has wings but is not a robin.',
                        [('Robins have wings.', 'that is a premise'), ('Bats fly at night.', 'irrelevant'),
                         ('Some birds cannot fly.', 'irrelevant')], 'True premises, false conclusion.'),
                     tf('If one case with true premises has a true conclusion, the argument is valid.', False, 'Validity needs EVERY case with true premises to have a true conclusion; one good case is not enough.'),
                 ]),
             ],
             f1=FW('Spot invalid forms in disguise', 'Harder: invalid forms in everyday wording and with "only if".', [
                 mc('"The alarm sounds only if there is smoke. There is smoke. So the alarm sounds." Is this valid?',
                    'No: "A only if S" means "if A then S"; from S, A does not follow.',
                    [('Yes: it is modus ponens.', '"only if" puts the alarm in the "if" part'),
                     ('Yes: smoke always sets off alarms.', 'the premises do not say that'),
                     ('No: the conclusion is false.', 'validity is about form, not the truth of the conclusion')],
                    'This affirms the consequent of "if the alarm sounds, there is smoke".'),
                 tf('"Every square is a rectangle. This shape is not a square. So it is not a rectangle." This argument is '
                    'valid.', False, 'Denying the antecedent: a non-square rectangle is a counterexample.'),
                 values('Show that "If x > 10, then x > 3. x is not greater than 10. So x is not greater than 3." is invalid: '
                        'give a number x that makes the premises true and the conclusion false.', [('x', 'x =')],
                        'not (x > 10) and x > 3', {'x': 5}, 'Any x with 3 < x ≤ 10.', wrong=[{'x': 2}, {'x': 11}, {'x': 3}]),
                 mc('Which argument has the SAME form as "If it is a cat, it is a mammal. It is a mammal. So it is a cat."?',
                    '"If n is 2, n is even. n is even. So n is 2."',
                    [('"If n is 2, n is even. n is 2. So n is even."', 'modus ponens'),
                     ('"If n is 2, n is even. n is odd. So n is not 2."', 'modus tollens'),
                     ('"n is 2 or n is 3. n is not 3. So n is 2."', 'disjunctive syllogism')],
                    'Both affirm the consequent.'),
                 tf('Denying the antecedent and affirming the consequent are both invalid.', True, 'Both have counterexample '
                                                                                                   'rows.',
                    check=lambda: not valid(*AC) and not valid(*DA)),
             ]),
             f2=FW('Invalid or just unconvincing?', 'Expert: separate an invalid form from an argument with true premises '
                                                   'and conclusion.', [
                 tf('"If a number is divisible by 4, it is even. 12 is even. So 12 is divisible by 4." The conclusion is true, '
                    'so the argument is valid.', False, 'The conclusion happens to be true, but the form (affirming the '
                                                         'consequent) is invalid; 6 shows the form can fail.'),
                 sa('For whole numbers n from 1 to 30, the argument "If n is a multiple of 6, then n is even. n is even. So n '
                    'is a multiple of 6." has true premises for every even n. For how many of these n is the conclusion '
                    'false?', 'Count:', '10', 'Even numbers up to 30: 15. Multiples of 6: 5. So 10 even numbers are not '
                                              'multiples of 6.',
                    compute=lambda: str(sum(1 for n in range(1, 31) if n % 2 == 0 and n % 6 != 0))),
                 mc('Which argument is INVALID, even though every premise and the conclusion are true?',
                    '"If 9 is odd, then 9 is a whole number. 9 is a whole number. So 9 is odd."',
                    [('"If 9 is odd, then 9 is a whole number. 9 is odd. So 9 is a whole number."', 'valid (modus ponens)'),
                     ('"9 is odd or 9 is even. 9 is not even. So 9 is odd."', 'valid (disjunctive syllogism)'),
                     ('"If 9 is even, then 9 is a whole number. 9 is even. So 9 is a whole number."', 'valid (modus ponens); '
                                                                                                         'its second premise is '
                                                                                                         'false')],
                    'The keyed argument affirms the consequent, so it is invalid even though every sentence in it is true.'),
                 tf('Valid: "If P then Q. If not P then Q. So Q."', True, 'Q follows whether P is true or false.',
                    check=lambda: valid([lambda p, q: imp(p, q), lambda p, q: imp(not p, q)], lambda p, q: q)),
                 tf('Valid: "If P then Q. If Q then P. Not P. So not Q."', True,
                    'The premises make P and Q equivalent; not P then gives not Q.',
                    check=lambda: valid([lambda p, q: imp(p, q), lambda p, q: imp(q, p), lambda p, q: not p], lambda p, q: not q)),
             ]))


SETS = [s21(), s22()]
