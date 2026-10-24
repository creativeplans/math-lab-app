"""S-CP.A.1-4: sample spaces and events, independence by the product rule, conditional probability, two-way tables as
sample spaces (sets 32-38). Probabilities are given as fractions in lowest terms or as decimals, as each question states."""
from fractions import Fraction as Fr
from itertools import product

from qb import S, B, sa, mc, tf
from common import why, tbl


def f(v):
    """A probability as a fraction in lowest terms (whole numbers stay whole)."""
    v = Fr(v)
    return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)


DICE = list(product(range(1, 7), repeat=2))
DIE = range(1, 7)


def pd(ev, given=None):
    """Probability over two fair dice, optionally given another event."""
    space = [o for o in DICE if given is None or given(o)]
    return Fr(sum(1 for o in space if ev(o)), len(space))


assert pd(lambda o: o[0] + o[1] == 7) == Fr(1, 6)
assert pd(lambda o: o[0] == o[1], lambda o: sum(o) == 8) == Fr(1, 5)
FL = ' Give a fraction in lowest terms.'


def two(rows, cols, cells):
    header = [''] + cols + ['Total']
    body = [[r] + [str(c) for c in row] + [str(sum(row))] for r, row in zip(rows, cells)]
    body.append(['Total'] + [str(sum(c)) for c in zip(*cells)] + [str(sum(map(sum, cells)))])
    return tbl(header, body)


DRIVE = [[60, 60], [30, 50]]   # juniors, seniors x drives, does not
SPORT = [[30, 20], [42, 28]]   # 9th, 10th x plays a sport, does not
VOTE = [[24, 16], [36, 24]]    # men, women x yes, no (independent)
DT = two(['Juniors', 'Seniors'], ['Drives', 'Does not drive'], DRIVE)
ST = two(['9th grade', '10th grade'], ['Plays a sport', 'Does not'], SPORT)
VT = two(['Men', 'Women'], ['Yes', 'No'], VOTE)

SETS = [
    # ------------------------------------------------------------------ 32. CP.A.1 sample spaces
    S('HSS-CP.A.1', 'Describe sample spaces and events', num=32,
      target='Describe the sample space of a chance process and describe events as subsets of it, using characteristics of '
             'the outcomes',
      strand='core', covers=['CP1-space'],
      main=[
          sa('A fair coin is flipped and a fair six-sided die is rolled. How many outcomes are in the sample space?', 'Outcomes:',
             key='12', note='2 · 6.'),
          sa('Two fair coins are flipped; the sample space is HH, HT, TH, TT. How many outcomes are in the event "at least one '
             'head"?', 'Outcomes:', key='3', note='HH, HT, TH.'),
          mc('A coin is flipped twice and the sequence of results is recorded. Which is the sample space?', [
              '{HH, HT, TH, TT}', '{HH, HT, TT}', '{H, T}', '{HH, TT}'], note='Order matters: HT and TH differ.'),
          sa('Two fair dice are rolled. How many of the 36 equally likely outcomes are in the event "the sum is 7"?', 'Outcomes:',
             key='6', note='(1,6), (2,5), (3,4), (4,3), (5,2), (6,1).'),
          sa('A spinner has 8 equal sections numbered 1 to 8. Event A is "an even number greater than 3". How many outcomes are '
             'in A, and what is P(A)?%s' % FL, ['Outcomes in A:', 'P(A):'], key='3; 3/8', note='Form required: both. {4, 6, 8}.'),
      ],
      back=[
          B('List a sample space with a list, table or tree', '7.SP.C.8.b', [
              sa('A bag has a red and a blue marble; a coin is flipped. How many outcomes (color, coin) are there?', 'Outcomes:',
                 key='4', note='2 · 2.'),
              tf('A tree diagram for flipping a coin 3 times has 8 final branches.', key=True, note='2 · 2 · 2.'),
              mc('A sandwich shop offers 3 breads and 4 fillings. How many bread-filling choices are there?', ['12', '7', '34', '81'],
                 note='3 · 4.'),
              tf('The sample space for rolling two dice has 12 outcomes.', key=False, note='36.'),
              sa('A spinner with 3 equal colors is spun twice. How many outcomes are in the sample space?', 'Outcomes:', key='9',
                 note='3 · 3.'),
          ], align='exact',
            why=why('the student cannot list or count the outcomes of a compound process.', 'events are subsets of that list.',
                    'builds sample spaces with lists, tables and trees.')),
          B('Find probabilities in a uniform model', '7.SP.C.7.a', [
              sa('A fair die is rolled. What is P(a number greater than 4)?%s' % FL, 'P:', key='1/3', note='{5, 6}.'),
              tf('In a uniform model, every outcome has the same probability.', key=True, note='Definition.'),
              mc('A letter is chosen at random from the word MATH. What is P(vowel)?', ['1/4', '1/2', '3/4', '1/3'], note='A only.'),
              sa('A number is chosen at random from 1 to 20. What is P(multiple of 5)?%s' % FL, 'P:', key='1/5',
                 note='5, 10, 15, 20.'),
              tf('A spinner with sections of different sizes is a uniform model.', key=False, note='Outcomes are not equally likely.'),
          ], align='supporting',
            why=why('the student cannot compute a probability by counting equally likely outcomes.', 'event probabilities '
                    'follow from the sample space.', 'finds probabilities in uniform models.')),
      ],
      f1=B('Describe events in multi-stage sample spaces', 'HSS-CP.A.1', [
          sa('Three fair coins are flipped. How many outcomes are in the sample space, and how many have exactly 2 heads?',
             ['Outcomes:', 'Exactly 2 heads:'], key='8; 3', note='Form required: both. HHT, HTH, THH.'),
          sa('Three fair coins are flipped. What is P(exactly 2 heads)?%s' % FL, 'P:', key='3/8', note='3 of 8.'),
          tf('For two dice, the event "doubles" contains 6 outcomes.', key=True, note='(1,1) ... (6,6).'),
          mc('For two dice, which event contains exactly 4 outcomes?', ['the sum is 5', 'the sum is 7', 'doubles', 'the sum is 12'],
             note='(1,4), (2,3), (3,2), (4,1). Sum 7 has 6; doubles 6; sum 12 has 1.'),
          sa('Two dice are rolled. How many outcomes have a sum of 10 or more?', 'Outcomes:', key='6',
             note='Sum 10: 3; sum 11: 2; sum 12: 1.'),
      ], prog='same-course deepening', demand='Describe and count events in sample spaces with more stages.'),
      f2=B('Combine events with "and", "or" and "not"', 'HSS-CP.A.1', [
          sa('A die is rolled. A = "even", B = "greater than 3". How many outcomes are in "A and B"?', 'Outcomes:', key='2',
             note='{4, 6}.'),
          sa('A die is rolled. A = "even", B = "greater than 3". How many outcomes are in "A or B"?', 'Outcomes:', key='4',
             note='{2, 4, 5, 6}.'),
          tf('The event "not A" contains every outcome of the sample space that is not in A.', key=True, note='Complement.'),
          mc('A die is rolled. A = "even". Which set is "not A"?', ['{1, 3, 5}', '{2, 4, 6}', '{1, 2, 3}', '{ }'],
             note='Odd outcomes.'),
          tf('The event "A and B" always contains at least as many outcomes as "A or B".', key=False, note='Never more.'),
      ], prog='same-course deepening', demand='Build new events from old ones with and, or and not.',
        builds='Builds on FORWARD 1: the events just described are combined into unions, intersections and complements.')),

    # ------------------------------------------------------------------ 33. CP.A.1 unions, intersections, complements
    S('HSS-CP.A.1', 'Unions, intersections and complements of events', num=33,
      target='Describe events as unions ("or"), intersections ("and") and complements ("not") of other events, and find '
             'their probabilities by counting',
      strand='core', covers=['CP1-sets'],
      main=[
          sa('A fair die is rolled. A = "even" and B = "greater than 3". How many outcomes are in A and B, and what is '
             'P(A and B)?%s' % FL, ['Outcomes:', 'P(A and B):'], key='2; 1/3', note='Form required: both. {4, 6}.'),
          sa('A fair die is rolled. A = "even" and B = "greater than 3". How many outcomes are in A or B, and what is P(A or B)?%s'
             % FL, ['Outcomes:', 'P(A or B):'], key='4; 2/3', note='Form required: both. {2, 4, 5, 6}.'),
          sa('A fair die is rolled. A = "even". What is P(not A)?%s' % FL, 'P(not A):', key='1/2', note='{1, 3, 5}.'),
          mc('A fair die is rolled. A = "even" and B = "greater than 3". Which describes the event {1, 3}?', [
              'not (A or B)', 'A and B', 'A or B', 'not A'], note='Neither even nor greater than 3. "not A" is {1, 3, 5}.'),
          sa('A card is drawn from a standard 52-card deck. H = "heart", F = "face card (jack, queen or king)". Find P(H and F) '
             'and P(H or F).%s' % FL, ['P(H and F):', 'P(H or F):'], key='3/52; 11/26',
             note='Form required: both. 3 heart face cards; 13 + 12 - 3 = 22, and 22/52 = 11/26.'),
      ],
      back=[
          B('Count the outcomes in an event', 'HSS-CP.A.1', [
              sa('A number from 1 to 10 is chosen. How many outcomes are in "multiple of 3"?', 'Outcomes:', key='3',
                 note='3, 6, 9.'),
              tf('For one roll of a die, the event "less than 3" is {1, 2}.', key=True, note='List.'),
              mc('A letter is chosen from the word PROBABILITY. How many outcomes (letter positions) are in "the letter B"?', [
                  '2', '1', '3', '11'], note='B appears twice.'),
              sa('How many cards in a standard deck are face cards?', 'Cards:', key='12', note='3 per suit · 4.'),
              tf('A standard deck has 4 aces and 13 hearts, so it has 17 cards that are aces or hearts.', key=False,
                 note='The ace of hearts is counted twice: 16.'),
          ], align='exact',
            why=why('the student cannot list the outcomes in a described event.', 'combining events starts with the events.',
                    'lists and counts outcomes in events.')),
          B('Find a probability by counting', '7.SP.C.8.a', [
              sa('Two coins are flipped. What is P(two heads)?%s' % FL, 'P:', key='1/4', note='1 of 4.'),
              sa('A die is rolled. What is P(1 or 2)?%s' % FL, 'P:', key='1/3', note='2 of 6.'),
              tf('The probability of an event plus the probability of its complement is 1.', key=True, note='Complements.'),
              mc('A card is drawn from a standard deck. What is P(king)?', ['1/13', '1/4', '4/13', '1/52'], note='4/52.'),
              tf('If P(A) = 0.3, then P(not A) = 0.3.', key=False, note='0.7.'),
          ], align='supporting',
            why=why('the student cannot turn a count into a probability.', 'every answer here is a probability.',
                    'computes fraction-of-outcomes probabilities.')),
      ],
      f1=B('Use a Venn diagram of counts', 'HSS-CP.A.1', [
          sa('Of 30 students, 18 play soccer, 12 play basketball and 5 play both. How many play soccer only, and how many play '
             'neither?', ['Soccer only:', 'Neither:'], key='13; 5', note='Form required: both. 18 - 5; 30 - (18 + 12 - 5).'),
          sa('Of 30 students, 18 play soccer, 12 play basketball and 5 play both. A student is chosen at random. What is P(soccer or '
             'basketball)?%s' % FL, 'P:', key='5/6', note='25/30.'),
          tf('In a Venn diagram, the overlap of two circles shows "A and B".', key=True, note='Intersection.'),
          mc('Of 30 students, 18 play soccer, 12 play basketball and 5 play both. What is P(not soccer)?', [
              '2/5', '3/5', '1/6', '7/30'], note='12/30.'),
          tf('Adding 18 and 12 gives the number who play soccer or basketball.', key=False, note='The 5 are counted twice.'),
      ], prog='same-course deepening', demand='Count unions, intersections and complements from overlapping groups.'),
      f2=B('Apply the Addition Rule', 'HSS-CP.B.7', [
          sa('P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2. Find P(A or B).', 'P(A or B):', key='0.7', note='0.5 + 0.4 - 0.2.'),
          sa('A card is drawn. Find P(king or heart).%s' % FL, 'P:', key='4/13', note='4/52 + 13/52 - 1/52 = 16/52.'),
          tf('If A and B cannot happen together, P(A or B) = P(A) + P(B).', key=True, note='P(A and B) = 0.'),
          mc('P(A) = 0.6, P(B) = 0.3, P(A or B) = 0.7. What is P(A and B)?', ['0.2', '0.9', '0.1', '0.18'],
             note='0.6 + 0.3 - 0.7.'),
          tf('P(A or B) can be greater than 1 if A and B are both likely.', key=False, note='Never above 1.'),
      ], prog='cross-standard extension', demand='Replace counting with the Addition Rule.',
        builds='Builds on FORWARD 1: the double-counting seen in the Venn diagram becomes the subtracted term of the rule.')),

    # ------------------------------------------------------------------ 34. CP.A.2 independence by the product rule
    S('HSS-CP.A.2', 'Decide independence with the product rule', num=34,
      target='Understand that A and B are independent if P(A and B) = P(A)·P(B), and use this to decide whether events are '
             'independent',
      strand='core', covers=['CP2-product'],
      main=[
          sa('P(A) = 0.4, P(B) = 0.5 and P(A and B) = 0.2. Find P(A)·P(B), and decide whether A and B are independent (enter yes '
             'or no).', ['P(A)·P(B):', 'Independent (yes or no):'], key='0.2; yes', note='Form required: both. 0.2 = 0.2.'),
          sa('P(A) = 0.3, P(B) = 0.6 and P(A and B) = 0.25. Find P(A)·P(B), and decide whether A and B are independent (enter yes '
             'or no).', ['P(A)·P(B):', 'Independent (yes or no):'], key='0.18; no', note='Form required: both. 0.18 ≠ 0.25.'),
          sa('A and B are independent with P(A) = 0.7 and P(B) = 0.2. Find P(A and B).', 'P(A and B):', key='0.14',
             note='0.7 · 0.2.'),
          mc('A die is rolled. A = "even" and B = "1 or 2". Are A and B independent?', [
              'Yes: P(A and B) = 1/6 = (1/2)(1/3).', 'No: P(A and B) = 1/6, not 1/2.',
              'No: A and B share the outcome 2.', 'Yes: A and B have no outcomes in common.'],
             note='A and B = {2}. Sharing an outcome does not decide independence.'),
          sa('In the survey table, a person is chosen at random. M = "man" and Y = "said yes". Find P(M and Y), and decide whether '
             'M and Y are independent (enter yes or no).', ['P(M and Y):', 'Independent (yes or no):'], key='0.24; yes', fig=VT,
             note='Form required: both. 24/100; P(M)·P(Y) = 0.4 · 0.6 = 0.24.'),
      ],
      back=[
          B('Multiply probabilities', '5.NF.B.4', [
              sa('Compute (1/2)(1/3).%s' % FL, 'Product:', key='1/6', note='1/6.'),
              sa('Compute 0.4 · 0.5.', 'Product:', key='0.2', note='Decimal product.'),
              tf('(2/3)(3/4) = 1/2.', key=True, note='6/12.'),
              mc('Compute 0.3 · 0.6.', ['0.18', '1.8', '0.9', '0.36'], note='3 · 6 = 18, two decimal places.'),
              tf('0.7 · 0.2 = 1.4.', key=False, note='0.14.'),
          ], align='supporting',
            why=why('the student cannot multiply fractions or decimals.', 'the test multiplies P(A) by P(B).', 'multiplies '
                    'probabilities.')),
          B('Find P(A and B) by counting', 'HSS-CP.A.1', [
              sa('A die is rolled. What is P(even and greater than 3)?%s' % FL, 'P:', key='1/3', note='{4, 6}.'),
              sa('A coin is flipped and a die is rolled. What is P(heads and 6)?%s' % FL, 'P:', key='1/12', note='1 of 12.'),
              tf('For one die, P(odd and even) = 0.', key=True, note='No outcome is both.'),
              mc('Two coins are flipped. What is P(first is heads and second is tails)?', ['1/4', '1/2', '3/4', '1'],
                 note='HT only.'),
              tf('For one die, P(less than 3 and odd) = 1/3.', key=False, note='{1}: 1/6.'),
          ], align='exact',
            why=why('the student cannot find P(A and B) from the sample space.', 'the test compares it with a product.',
                    'counts intersections.')),
      ],
      f1=B('Use independence for several events', 'HSS-CP.A.2', [
          sa('A fair coin is flipped 3 times. What is P(all three heads)?%s' % FL, 'P:', key='1/8', note='(1/2)^3.'),
          sa('Each of 3 independent lights works with probability 0.9. What is P(all 3 work), and P(at least one fails)?',
             ['All work:', 'At least one fails:'], key='0.729; 0.271', note='Form required: both. 0.9^3; 1 - 0.729.'),
          tf('For independent events, P(A and B and C) = P(A)·P(B)·P(C).', key=True, note='Extends the product rule.'),
          mc('A fair die is rolled twice. What is P(two sixes)?', ['1/36', '1/6', '1/12', '2/6'], note='(1/6)(1/6).'),
          tf('If P(A and B) = P(A)·P(B), then A and B cannot happen together.', key=False,
             note='Independent events can happen together; that describes mutually exclusive events.'),
      ], prog='same-course deepening', demand='Use the product rule for more than two events and with complements.'),
      f2=B('Interpret independence with conditional probability', 'HSS-CP.A.3', [
          sa('P(A and B) = 0.2 and P(B) = 0.5. Find P(A given B).', 'P(A given B):', key='0.4', note='0.2/0.5.'),
          tf('If A and B are independent, P(A given B) = P(A).', key=True, note='Knowing B does not change A.'),
          mc('P(A) = 0.4 and P(A given B) = 0.4. What can be concluded?', [
              'A and B are independent.', 'A and B are mutually exclusive.', 'B always happens.', 'P(B) = 0.4.'],
             note='Equal conditional and unconditional probability.'),
          sa('P(A) = 0.3, P(B) = 0.6 and P(A and B) = 0.18. Find P(A given B).', 'P(A given B):', key='0.3', note='0.18/0.6.'),
          tf('If P(A given B) is greater than P(A), then A and B are independent.', key=False, note='B changes A\'s chance.'),
      ], prog='cross-standard extension', demand='Check independence by comparing P(A given B) with P(A).',
        builds='Builds on FORWARD 1: the product rule is restated as "B does not change the probability of A".')),

    # ------------------------------------------------------------------ 35. CP.A.3 conditional probability definition
    S('HSS-CP.A.3', 'Compute conditional probability as P(A and B)/P(B)', num=35,
      target='Understand and compute the conditional probability of A given B as P(A and B)/P(B), without reversing the '
             'condition',
      strand='core', covers=['CP3-def'],
      main=[
          sa('P(A and B) = 0.12 and P(B) = 0.4. Find P(A given B).', 'P(A given B):', key='0.3', note='0.12/0.4.'),
          sa('A fair die is rolled. What is P(6 given the roll is even)?%s' % FL, 'P:', key='1/3', note='P(6)/P(even) = (1/6)/(1/2).'),
          sa('Two fair dice are rolled. What is P(doubles given the sum is 8)?%s' % FL, 'P:',
             key=f(pd(lambda o: o[0] == o[1], lambda o: sum(o) == 8)),
             note='Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2); one is doubles.'),
          mc('On a given day, P(rain) = 0.3 and P(rain and wind) = 0.12. What is P(wind given rain)?', ['0.4', '0.036', '0.12', '2.5'],
             note='0.12/0.3. 0.036 multiplies; 2.5 inverts the division.'),
          sa('P(B) = 0.25 and P(A given B) = 0.6. Find P(A and B).', 'P(A and B):', key='0.15', note='0.6 · 0.25.'),
      ],
      back=[
          B('Divide decimals and fractions', '6.NS.B.3', [
              sa('Compute 0.12 ÷ 0.4.', 'Answer:', key='0.3', note='1.2 ÷ 4.'),
              sa('Compute 0.18 ÷ 0.6.', 'Answer:', key='0.3', note='1.8 ÷ 6.'),
              tf('0.2 ÷ 0.5 = 0.4.', key=True, note='2 ÷ 5.'),
              mc('Compute 0.05 ÷ 0.2.', ['0.25', '0.01', '4', '2.5'], note='0.5 ÷ 2.'),
              tf('0.3 ÷ 0.6 = 2.', key=False, note='0.5.'),
          ], align='supporting',
            why=why('the student cannot divide decimals.', 'the definition divides two probabilities.', 'divides decimals.')),
          B('Count outcomes in a restricted sample space', 'HSS-CP.A.1', [
              sa('A die is rolled and shows an even number. How many outcomes remain possible?', 'Outcomes:', key='3',
                 note='{2, 4, 6}.'),
              sa('Two dice are rolled and the sum is 8. How many outcomes give a sum of 8?', 'Outcomes:', key='5',
                 note='(2,6) to (6,2).'),
              tf('Knowing that a card is a heart leaves 13 possible cards.', key=True, note='The hearts.'),
              mc('A die shows a number greater than 2. How many of the remaining outcomes are odd?', ['2', '3', '4', '1'],
                 note='{3, 4, 5, 6}: 3 and 5.'),
              tf('Knowing a card is a face card leaves 13 possible cards.', key=False, note='12.'),
          ], align='exact',
            why=why('the student does not shrink the sample space to the condition.', 'P(A given B) lives inside B.',
                    'restricts and counts.')),
      ],
      f1=B('Compute conditional probability in both directions', 'HSS-CP.A.3', [
          sa('A card is drawn. Find P(king given face card) and P(face card given king).%s' % FL,
             ['P(king given face card):', 'P(face card given king):'], key='1/3; 1', note='Form required: both. 4/12 and 4/4.'),
          tf('P(A given B) and P(B given A) are always equal.', key=False, note='The king example shows otherwise.'),
          sa('P(A) = 0.5, P(B) = 0.2 and P(A and B) = 0.1. Find P(A given B) and P(B given A).',
             ['P(A given B):', 'P(B given A):'], key='0.5; 0.2', note='Form required: both. 0.1/0.2 and 0.1/0.5.'),
          mc('Which formula gives P(B given A)?', ['P(A and B)/P(A)', 'P(A and B)/P(B)', 'P(A)·P(B)', 'P(A)/P(B)'],
             note='Divide by the condition\'s probability.'),
          tf('P(A given B) = P(B given A) exactly when P(A) = P(B), provided P(A and B) > 0.', key=True,
             note='Both equal P(A and B) divided by equal numbers.'),
      ], prog='same-course deepening', demand='Compute and compare P(A given B) and P(B given A).'),
      f2=B('Test independence with conditional probability', 'HSS-CP.A.3', [
          sa('P(A) = 0.6, P(B) = 0.5, P(A and B) = 0.3. Find P(A given B), and decide whether A and B are independent (enter yes '
             'or no).', ['P(A given B):', 'Independent (yes or no):'], key='0.6; yes', note='Form required: both. 0.3/0.5 = P(A).'),
          tf('If P(A given B) = P(A), then also P(B given A) = P(B), provided P(A) > 0.', key=True, note='Symmetric.'),
          mc('Two cards are drawn without replacement. Are "first card is an ace" and "second card is an ace" independent?', [
              'No: the first draw changes the chance for the second.', 'Yes: each card in the deck is equally likely to be drawn.',
              'Yes: the deck always contains exactly 4 aces.', 'No: two aces can never be drawn one after another.'],
             note='P(second ace given first ace) = 3/51 ≠ 4/52.'),
          sa('P(A) = 0.4, P(B) = 0.5, P(A and B) = 0.1. Find P(A given B).', 'P(A given B):', key='0.2', note='0.1/0.5 ≠ 0.4.'),
          tf('If P(A given B) = 0.2 and P(A) = 0.4, then A and B are independent.', key=False, note='Not equal.'),
      ], prog='same-course deepening', demand='Use P(A given B) to decide independence.',
        builds='Builds on FORWARD 1: conditional probabilities in both directions are compared with unconditional ones.')),

    # ------------------------------------------------------------------ 36. CP.A.3 independence as P(A|B) = P(A)
    S('HSS-CP.A.3', 'Interpret independence through conditional probability', num=36,
      target='Interpret independence of A and B as P(A given B) = P(A) and P(B given A) = P(B), and use it to decide and explain',
      strand='core', covers=['CP3-indep'],
      main=[
          sa('P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2. Find P(A given B), and decide whether A and B are independent (enter '
             'yes or no).', ['P(A given B):', 'Independent (yes or no):'], key='0.5; yes', note='Form required: both. 0.2/0.4.'),
          sa('P(A) = 0.3, P(B) = 0.5 and P(A and B) = 0.1. Find P(A given B), and decide whether A and B are independent (enter '
             'yes or no).', ['P(A given B):', 'Independent (yes or no):'], key='0.2; no', note='Form required: both. 0.1/0.5.'),
          mc('A and B are independent. Which statement is correct?', [
              'Knowing that B happened does not change the probability of A.', 'A and B can never happen at the same time as each other.',
              'Whenever B happens, then A must also happen.', 'P(A) and P(B) must be equal to each other.'], note='Meaning of independence.'),
          sa('Two cards are drawn from a standard deck. Find P(second is an ace given the first is an ace) when the first card is '
             'replaced, and when it is not replaced.%s' % FL, ['With replacement:', 'Without replacement:'], key='1/13; 1/17',
             note='Form required: both. 4/52 and 3/51.'),
          mc('Which pair of events is independent?', [
              'a die shows 6; a separate coin shows heads', 'first card drawn is an ace; second card (not replaced) is an ace',
              'it rains today; the ground is wet today', 'a student studies; the student passes the test'],
             note='Separate devices do not affect each other.'),
      ],
      back=[
          B('Compute a conditional probability', 'HSS-CP.A.3', [
              sa('P(A and B) = 0.06 and P(B) = 0.3. Find P(A given B).', 'P(A given B):', key='0.2', note='0.06/0.3.'),
              sa('P(A and B) = 0.25 and P(A) = 0.5. Find P(B given A).', 'P(B given A):', key='0.5', note='0.25/0.5.'),
              tf('P(A given B) = P(A and B)/P(B).', key=True, note='Definition.'),
              mc('P(A and B) = 0.1, P(B) = 0.4. Find P(A given B).', ['0.25', '0.04', '0.4', '4'], note='0.1/0.4.'),
              tf('P(A given B) = P(A and B)·P(B).', key=False, note='Divide, not multiply.'),
          ], align='exact',
            why=why('the student cannot compute P(A given B).', 'independence compares it with P(A).', 'computes conditional '
                    'probabilities.')),
          B('Test independence with the product rule', 'HSS-CP.A.2', [
              tf('If P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2, A and B are independent.', key=True, note='0.5 · 0.4 = 0.2.'),
              sa('P(A) = 0.2 and P(B) = 0.5. If A and B are independent, what is P(A and B)?', 'P(A and B):', key='0.1',
                 note='Product.'),
              mc('P(A) = 0.3, P(B) = 0.4, P(A and B) = 0.2. Are A and B independent?', [
                  'no, because 0.3 · 0.4 = 0.12', 'yes, because 0.2 < 1', 'yes, because 0.3 < 0.4', 'no, because 0.2 > 0'],
                 note='0.12 ≠ 0.2.'),
              tf('Mutually exclusive events with positive probabilities are independent.', key=False,
                 note='P(A and B) = 0 ≠ P(A)·P(B).'),
              sa('P(A) = 0.6 and P(B) = 0.5 for independent events. Find P(A and B).', 'P(A and B):', key='0.3', note='0.6 · 0.5.'),
          ], align='exact',
            why=why('the student cannot use the product rule.', 'it is equivalent to the conditional test.',
                    'checks independence by the product rule.')),
      ],
      f1=B('Check both directions of independence', 'HSS-CP.A.3', [
          sa('P(A) = 0.6, P(B) = 0.25 and P(A and B) = 0.15. Find P(A given B) and P(B given A).',
             ['P(A given B):', 'P(B given A):'], key='0.6; 0.25', note='Form required: both. Both equal the unconditional values.'),
          tf('If P(A given B) = P(A), then A and B are independent.', key=True, note='Definition (when P(B) > 0).'),
          mc('P(A) = 0.5, P(A given B) = 0.5, and P(B) = 0.3. What is P(B given A)?', ['0.3', '0.5', '0.15', '0.6'],
             note='Independence works both ways.'),
          sa('A and B are independent, P(A) = 0.7 and P(B) = 0.4. Find P(A given B).', 'P(A given B):', key='0.7',
             note='Independence.'),
          tf('If P(B given A) = 0.25 and P(B) = 0.5, then A and B are independent.', key=False, note='Not equal.'),
      ], prog='same-course deepening', demand='Use and justify the two-way meaning of independence.'),
      f2=B('Approximate conditional probabilities from data', 'HSS-CP.A.4', [
          sa('In the survey table, a person is chosen at random. Find P(yes given man) and P(yes).', ['P(yes given man):', 'P(yes):'],
             key='0.6; 0.6', fig=VT, note='Form required: both. 24/40 and 60/100.'),
          tf('In the survey table, gender and answer are independent.', key=True, fig=VT, note='P(yes given man) = P(yes).'),
          sa('In the driving table, find P(drives given junior) and P(drives).', ['P(drives given junior):', 'P(drives):'],
             key='0.5; 0.45', fig=DT, note='Form required: both. 60/120 and 90/200.'),
          tf('In the driving table, grade and driving are independent.', key=False, fig=DT, note='0.5 ≠ 0.45.'),
          mc('In the driving table, which is P(junior given drives)?', ['2/3', '1/2', '3/10', '9/20'], fig=DT,
             note='60/90. 1/2 reverses the condition.'),
      ], prog='cross-standard extension', demand='Estimate the probabilities in the independence test from a two-way table.',
        builds='Builds on FORWARD 1: the two-direction test is applied to data in two-way tables.')),
]

TRIAL = [[35, 15], [12, 18]]   # drug, placebo x improved, did not
TRIALT = two(['Drug', 'Placebo'], ['Improved', 'Did not'], TRIAL)
MUSIC = [[16, 24, 10], [24, 36, 15]]  # middle school, high school x pop, rock, other (independent)
MT = two(['Middle school', 'High school'], ['Pop', 'Rock', 'Other'], MUSIC)

SETS += [
    # ------------------------------------------------------------------ 37. CP.A.4 build a two-way table
    S('HSS-CP.A.4', 'Construct two-way frequency tables', num=37,
      target='Construct a two-way frequency table from a description of data in which each object is classified by two '
             'categories, and interpret its cells and totals',
      strand='core', covers=['CP4-build'],
      main=[
          sa('Of 200 students, 120 are juniors and 80 are seniors. 90 students drive to school, including 60 juniors. Complete the '
             'two-way table: juniors who do not drive, seniors who drive, seniors who do not drive.',
             ['Juniors, do not drive:', 'Seniors, drive:', 'Seniors, do not drive:'], key='60; 30; 50',
             note='Form required: all three. 120 - 60; 90 - 60; 80 - 30.'),
          sa('Of 150 adults, 90 own a car, 40 own a bike, and 25 own both. In a two-way table (car yes/no by bike yes/no), how many '
             'own a car but no bike, and how many own neither?', ['Car, no bike:', 'Neither:'], key='65; 45',
             note='Form required: both. 90 - 25; 150 - (90 + 40 - 25).'),
          sa('Of 200 students, 120 are juniors, and 60 of the juniors drive. What percent of juniors drive?', 'Percent:',
             key='50%', note='60/120.'),
          mc('80 patients took part in a study. Which description matches the table?', [
              '50 got the drug (35 improved); 12 of the placebo patients improved.',
              '50 patients improved, and 35 of those improved patients got the drug.',
              '35 patients got the drug and 12 patients got a placebo instead.',
              '50 patients got the placebo and the other 30 got the drug.'],
             fig=TRIALT, note='Drug row 35 + 15 = 50; placebo row 12 + 18 = 30. 47 improved, not 50.'),
          sa('80 patients: 50 got a drug and 30 a placebo; 35 drug patients and 12 placebo patients improved. How many drug '
             'patients and how many placebo patients did not improve?', ['Drug, did not:', 'Placebo, did not:'], key='15; 18',
             note='Form required: both.'),
      ],
      back=[
          B('Fill in a two-way frequency table', '8.SP.A.4', [
              sa('A table has row totals 40 and 60. One cell in the first row is 25. What is the other cell in that row?', 'Cell:',
                 key='15', note='40 - 25.'),
              tf('In a two-way table, the column totals add to the grand total.', key=True, note='Every object counted once.'),
              mc('Of 50 people, 30 are adults. 12 of the adults wear glasses. How many adults do not?', ['18', '12', '20', '38'],
                 note='30 - 12.'),
              sa('A two-way table with two columns classifies 100 objects. One column total is 45. What is the other column total?', 'Total:', key='55',
                 note='100 - 45.'),
              tf('A cell can be found from its row total and the other cells in that row.', key=True, note='Subtraction.'),
          ], align='exact',
            why=why('the student cannot complete cells from totals.', 'building a table depends on it.', 'fills in two-way '
                    'tables.')),
          B('Read joint and marginal frequencies', 'HSS-ID.B.5', [
              sa('In the drug table, how many patients improved in total?', 'Improved:', key='47', fig=TRIALT, note='35 + 12.'),
              sa('In the drug table, what fraction of all patients got the drug and improved? Give lowest terms.', 'Fraction:',
                 key='7/16', fig=TRIALT, note='35/80.'),
              tf('In the drug table, 30 patients got the placebo.', key=True, fig=TRIALT, note='12 + 18.'),
              mc('In the drug table, which number is a marginal total?', ['50', '35', '15', '12'], fig=TRIALT,
                 note='The drug row total.'),
              tf('In the drug table, 35/47 is the fraction of drug patients who improved.', key=False, fig=TRIALT,
                 note='35/50; 35/47 is the fraction of improvers who got the drug.'),
          ], align='exact',
            why=why('the student misreads cells and totals.', 'later probabilities come from them.', 'reads joint and marginal '
                    'frequencies.')),
      ],
      f1=B('Check statements against a built table', 'HSS-CP.A.4', [
          tf('In the drug table, a greater percent of drug patients than placebo patients improved.', key=True, fig=TRIALT,
             note='70% versus 40%.'),
          sa('In the drug table, what percent of drug patients improved, and what percent of placebo patients improved?',
             ['Drug:', 'Placebo:'], key='70%; 40%', fig=TRIALT, note='Form required: both. 35/50 and 12/30.'),
          mc('A report says "most patients who improved got the drug." Using the drug table, is this correct?', [
              'Yes: 35 of the 47 who improved got the drug.', 'No: only 35 patients got the drug.',
              'No: 50 patients got the drug.', 'Yes: 70% of all patients improved.'],
             fig=TRIALT, note='35/47 ≈ 74%. Only 47 of 80 improved (58.75%).'),
          sa('Of 120 voters, 70 are under 40. 45 of all voters support a plan, including 30 of those under 40. How many voters 40 '
             'or older do not support it?', 'Number:', key='35', note='50 older; 15 support; 35 do not.'),
          tf('A two-way table can be built when each object is classified by only one category.', key=False,
             note='It needs two categorical variables.'),
      ], prog='same-course deepening', demand='Build tables from words and check claims against them.'),
      f2=B('Use the table as a sample space', 'HSS-CP.A.4', [
          sa('A patient is chosen at random from the drug table. What is P(improved)?%s' % FL, 'P:', key='47/80', fig=TRIALT,
             note='47/80.'),
          sa('A patient is chosen at random from the drug table. What is P(improved given drug)?%s' % FL, 'P:', key='7/10',
             fig=TRIALT, note='35/50.'),
          tf('In the drug table, improving and treatment are independent.', key=False, fig=TRIALT, note='7/10 ≠ 47/80.'),
          mc('A patient is chosen at random from the drug table. What is P(drug given improved)?', ['35/47', '35/50', '7/16', '47/80'],
             fig=TRIALT, note='Condition on the improved column.'),
          sa('A patient is chosen at random. What is P(placebo and did not improve)?%s' % FL, 'P:', key='9/40', fig=TRIALT,
             note='18/80.'),
      ], prog='same-course deepening', demand='Treat the completed table as a sample space for probabilities.',
        builds='Builds on FORWARD 1: the checked table becomes a sample space.')),

    # ------------------------------------------------------------------ 38. CP.A.4 use a two-way table as a sample space
    S('HSS-CP.A.4', 'Use two-way tables to find conditional probabilities and judge independence', num=38,
      target='Use a two-way table as a sample space to approximate conditional probabilities and decide whether two events '
             'are independent',
      strand='core', covers=['CP4-use'],
      main=[
          sa('A student is chosen at random from the driving table. Find P(drives given junior) and P(drives given senior). Give '
             'decimals.', ['Given junior:', 'Given senior:'], key='0.5; 0.375', fig=DT, note='Form required: both. 60/120 and 30/80.'),
          mc('In the driving table, are "drives" and "junior" independent?', [
              'No: P(drives given junior) ≠ P(drives given senior).', 'Yes: 60 juniors drive and 60 do not.',
              'Yes: every student is a junior or a senior.', 'No: more juniors than seniors were surveyed.'],
             fig=DT, note='0.5 versus 0.375. Group sizes alone do not decide.'),
          sa('A student is chosen at random from the sports table. Find P(plays a sport) and P(plays a sport given 9th grade). '
             'Give decimals.', ['P(sport):', 'P(sport given 9th):'], key='0.6; 0.6', fig=ST, note='Form required: both. 72/120 and '
                                                                                                  '30/50.'),
          mc('In the sports table, are "plays a sport" and "9th grade" independent?', [
              'Yes: P(sport given 9th) = P(sport) = 0.6.', 'No: 30 is not equal to 42.', 'No: the grades have different sizes.',
              'Yes: more students play than do not.'], fig=ST, note='Compare rates, not counts.'),
          sa('A student who drives is chosen at random from the driving table. What is P(junior given drives)?%s' % FL, 'P:',
             key='2/3', fig=DT, note='60/90.'),
      ],
      back=[
          B('Compute conditional relative frequencies', 'HSS-ID.B.5', [
              sa('In the driving table, what fraction of seniors drive? Give lowest terms.', 'Fraction:', key='3/8', fig=DT,
                 note='30/80.'),
              tf('In the sports table, 42/70 of 10th graders play a sport.', key=True, fig=ST, note='Row 10th.'),
              mc('In the sports table, what fraction of students who play a sport are in 10th grade?', ['7/12', '3/5', '7/20', '5/12'],
                 fig=ST, note='42/72.'),
              sa('In the driving table, what percent of all students drive?', 'Percent:', key='45%', fig=DT, note='90/200.'),
              tf('A row conditional frequency divides by the grand total.', key=False, note='By the row total.'),
          ], align='exact',
            why=why('the student cannot compute conditional relative frequencies.', 'they approximate the probabilities.',
                    'computes row and column rates.')),
          B('Compare P(A given B) with P(A)', 'HSS-CP.A.3', [
              tf('If P(A given B) = P(A), A and B are independent.', key=True, note='Definition.'),
              mc('P(A) = 0.45 and P(A given B) = 0.5. Are A and B independent?', ['no', 'yes', 'cannot tell', 'only if P(B) = 0.5'],
                 note='Not equal.'),
              sa('P(A and B) = 0.3 and P(B) = 0.5. Find P(A given B).', 'P(A given B):', key='0.6', note='0.3/0.5.'),
              tf('P(A given B) is always less than P(A).', key=False, note='It can be greater, equal or less.'),
              mc('P(A and B) = 0.18 and P(B) = 0.3. If P(A) = 0.6, are A and B independent?', [
                  'yes', 'no', 'cannot tell', 'only if P(A) = 0.3'], note='0.18/0.3 = 0.6.'),
          ], align='exact',
            why=why('the student does not know which probabilities to compare.', 'that comparison decides independence.',
                    'compares conditional and unconditional probabilities.')),
      ],
      f1=B('Use larger two-way tables', 'HSS-CP.A.4', [
          sa('A student is chosen at random from the music table. Find P(rock) and P(rock given high school). Give decimals.',
             ['P(rock):', 'P(rock given high school):'], key='0.48; 0.48', fig=MT, note='Form required: both. 60/125 and 36/75.'),
          tf('In the music table, school level and favorite type of music are independent.', key=True, fig=MT,
             note='Each row has the same proportions 0.32, 0.48, 0.2.'),
          sa('In the music table, what is P(middle school given pop)?%s' % FL, 'P:', key='2/5', fig=MT, note='16/40.'),
          mc('In the music table, what is P(other given middle school)?', ['1/5', '2/25', '2/5', '1/3'], fig=MT, note='10/50.'),
          tf('In the music table, P(pop given middle school) is greater than P(pop given high school).', key=False, fig=MT,
             note='Both 0.32.'),
      ], prog='same-course deepening', demand='Apply the method to tables with more categories.'),
      f2=B('Explain table results in everyday language', 'HSS-CP.A.5', [
          mc('In the driving table, P(drives given junior) = 0.5 and P(drives given senior) = 0.375. Which sentence says this in '
             'everyday language?', [
              'Half of the juniors drive, but fewer than 4 in 10 seniors drive.', 'Half of all the students who drive are juniors.',
              'Juniors and seniors are equally likely to drive.', 'Most of the students who drive to school are seniors.'],
             fig=DT, note='Condition on grade.'),
          tf('"Among students who drive, two-thirds are juniors" describes P(junior given drives).', key=True,
             note='The condition is "drives".'),
          mc('Which statement describes independence in the sports table?', [
              'A student\'s grade does not change the chance of playing a sport.',
              'Every student in the table plays exactly one sport.', 'The two grades have the same number of students.',
              'Students in 10th grade play more sports than 9th graders.'], fig=ST, note='Same rate in each grade.'),
          tf('"Most juniors drive" and "most drivers are juniors" mean the same thing.', key=False,
             note='Different conditions.'),
          mc('"Among seniors, 3 in 8 drive." Which probability is this?', [
              'P(drives given senior)', 'P(senior given drives)', 'P(senior and drives)', 'P(senior)'], note='Condition: senior.'),
      ], prog='cross-standard extension', demand='Translate conditional probabilities and independence into plain language.',
        builds='Builds on FORWARD 1: probabilities from tables are stated and checked in everyday words.')),
]
