"""S-CP.A.5, S-CP.B.6-9: everyday conditional language, conditional probability as a fraction of outcomes, the Addition
Rule, and the (+) general Multiplication Rule, permutations and combinations (sets 39-45)."""
from fractions import Fraction as Fr
from math import comb, perm

from qb import S, B, sa, mc, tf
from common import why
from data_cp1 import f, pd, FL, TRIALT, DT

assert f(pd(lambda o: sum(o) >= 10, lambda o: o[0] == 5)) == '1/3'
assert f(pd(lambda o: sum(o) == 7, lambda o: 6 in o)) == '2/11'
assert f(pd(lambda o: o[0] == o[1] or sum(o) == 8)) == '5/18'
assert f(Fr(5, 8) * Fr(4, 7)) == '5/14' and f(Fr(4, 52) * Fr(3, 51)) == '1/221'
assert f(Fr(comb(4, 3), comb(9, 3))) == '1/21' and f(Fr(comb(13, 2), comb(52, 2))) == '1/17'
assert f(Fr(comb(4, 1) * comb(5, 2), comb(9, 3))) == '10/21'

SETS = [
    # ------------------------------------------------------------------ 39. CP.A.5 everyday language
    S('HSS-CP.A.5', 'Conditional probability and independence in everyday language', num=39,
      target='Recognize and explain conditional probability and independence in everyday language and everyday situations',
      strand='core', covers=['CP5-words'],
      main=[
          mc('Which statement describes a conditional probability?', [
              'Among smokers, the chance of lung disease is higher.', 'The chance of rain tomorrow is 30 percent.',
              'A fair coin lands heads half of the time.', 'One in four cards in a deck is a heart.'],
             note='"Among smokers" names the condition.'),
          mc('"Most people with lung disease were smokers." Which probability does this sentence say is high?', [
              'P(smoker given lung disease)', 'P(lung disease given smoker)', 'P(smoker and lung disease)', 'P(lung disease)'],
             note='The condition is "people with lung disease".'),
          mc('Which pair of events is most likely to be independent?', [
              'a student\'s shirt color; the school bus being late', 'studying hard for a test; passing that test',
              'heavy rain today; a baseball game being canceled', 'a person\'s height; the person\'s shoe size'],
             note='No plausible influence.'),
          mc('A fair coin has landed heads 5 times in a row. What is the probability of heads on the next flip?', [
              '1/2', 'less than 1/2', 'more than 1/2', '1/32'], note='Flips are independent; 1/32 is P(5 heads in a row) before '
                                                                   'flipping.'),
          sa('In a town, 40% of adults own a dog, and among dog owners 70% walk daily. What percent of all adults are dog owners '
             'who walk daily?', 'Percent:', key='28%', note='0.4 · 0.7.'),
      ],
      back=[
          B('Compute and read conditional probabilities', 'HSS-CP.A.3', [
              sa('P(A and B) = 0.28 and P(A) = 0.4. Find P(B given A).', 'P(B given A):', key='0.7', note='0.28/0.4.'),
              tf('"The probability of B given A" means the chance of B when A is known to happen.', key=True, note='Meaning.'),
              mc('P(passing given studying) is the probability that', [
                  'a student passes, among students who study', 'a student studies, among students who pass',
                  'a student both studies and passes', 'a student passes'], note='Condition: studying.'),
              sa('P(B) = 0.5 and P(A given B) = 0.3. Find P(A and B).', 'P(A and B):', key='0.15', note='0.5 · 0.3.'),
              tf('P(rain given clouds) is the same as P(clouds given rain).', key=False, note='Different conditions.'),
          ], align='exact',
            why=why('the student cannot connect the notation to its meaning.', 'everyday statements translate into it.',
                    'reads conditional notation.')),
          B('Read conditional rates in a table', 'HSS-CP.A.4', [
              sa('In the driving table, what fraction of juniors drive? Give lowest terms.', 'Fraction:', key='1/2', fig=DT,
                 note='60/120.'),
              tf('In the driving table, "among drivers, 2 in 3 are juniors" is correct.', key=True, fig=DT, note='60/90.'),
              mc('In the driving table, which sentence is correct?', [
                  'Among seniors, 3 in 8 drive.', 'Among drivers, 3 in 8 are seniors.', 'Among seniors, 1 in 2 drive.',
                  'Among juniors, 3 in 8 drive.'], fig=DT, note='30/80. Drivers who are seniors: 30/90 = 1/3.'),
              sa('In the driving table, what fraction of drivers are seniors? Give lowest terms.', 'Fraction:', key='1/3', fig=DT,
                 note='30/90.'),
              tf('In the driving table, "among seniors, most drive" is correct.', key=False, fig=DT, note='3/8 < 1/2.'),
          ], align='exact',
            why=why('the student cannot match sentences with table rates.', 'everyday claims are usually such rates.',
                    'reads conditional rates in words.')),
      ],
      f1=B('Translate statements and compute', 'HSS-CP.A.5', [
          mc('"If it is a school day, there is an 80% chance that Sam takes the bus." Which notation matches?', [
              'P(bus given school day) = 0.8', 'P(school day given bus) = 0.8', 'P(bus and school day) = 0.8', 'P(bus) = 0.8'],
             note='The condition follows "if".'),
          sa('5 of 7 days are school days, and on a school day Sam takes the bus with probability 0.8. What is P(school day and '
             'bus)?%s' % FL, 'P:', key='4/7', note='(5/7)(4/5).'),
          tf('"Knowing it is a school day changes the chance that Sam takes the bus" means the events are not independent.',
             key=True, note='Dependence.'),
          mc('A test is positive for 95% of people with a disease. Which sentence states this correctly?', [
              'Among people with the disease, 95% test positive.', 'Among people who test positive, 95% have the disease.',
              '95% of all people test positive.', '95% of all people have the disease.'], note='Condition: has the disease.'),
          tf('"Among people who test positive, 95% have the disease" follows from "95% of people with the disease test '
             'positive".', key=False, note='Reversing the condition is not allowed.'),
      ], prog='same-course deepening', demand='Move between everyday sentences, notation and computation.'),
      f2=B('Find a conditional probability as a fraction of outcomes', 'HSS-CP.B.6', [
          sa('A fair six-sided die is rolled. Given the roll is odd, what is P(the roll is 5)?%s' % FL, 'P:', key='1/3', note='{1, 3, 5}.'),
          sa('A card drawn at random from a standard 52-card deck is red. What is P(it is a king)?%s' % FL, 'P:', key='1/13', note='2 of 26.'),
          tf('P(A given B) can be found as (outcomes in both A and B)/(outcomes in B) in a uniform model.', key=True,
             note='Fraction of B.'),
          mc('A number from 1 to 10 is even. What is P(it is greater than 6)?', ['2/5', '1/5', '2/3', '1/2'],
             note='{2, 4, 6, 8, 10}: 8 and 10.'),
          tf('Given the roll of a fair six-sided die is even, P(roll is 3) = 1/6.', key=False, note='0.'),
      ], prog='cross-standard extension', demand='Compute conditional probabilities by counting within the condition.',
        builds='Builds on FORWARD 1: conditional sentences become counts within the conditioning event.')),

    # ------------------------------------------------------------------ 40. CP.B.6 fraction of B's outcomes
    S('HSS-CP.B.6', 'Find conditional probability as a fraction of outcomes', num=40,
      target='Find P(A given B) as the fraction of B\'s outcomes that also belong to A, and interpret the answer in terms of '
             'the model',
      strand='core', covers=['CP6-fraction'],
      main=[
          sa('Two fair dice are rolled independently. The first die shows 5. What is P(the sum is 10 or more)?%s' % FL, 'P:', key='1/3',
             note='Second die 5 or 6: 2 of 6.'),
          sa('A card drawn at random from a standard 52-card deck is red. What is P(it is an ace)?%s' % FL, 'P:', key='1/13', note='2 of 26.'),
          sa('A patient from the drug table is chosen at random and got the placebo. What is P(improved)?%s' % FL, 'P:',
             key='2/5', fig=TRIALT, note='12 of 30.'),
          sa('A number from 1 to 10 is chosen at random and is odd. What is P(it is prime)?%s' % FL, 'P:', key='3/5',
             note='{1, 3, 5, 7, 9}: 3, 5, 7.'),
          mc('From the drug table, P(improved given placebo) = 2/5. What does this mean in the model?', [
              'Of the patients given the placebo, 2 in 5 improved.', 'Of the patients who improved, 2 in 5 got the placebo.',
              '2 in 5 of all patients got the placebo and improved.', '2 in 5 of all patients got the placebo.'],
             fig=TRIALT, note='The placebo group is the sample space.'),
      ],
      back=[
          B('Count outcomes in events', 'HSS-CP.A.1', [
              sa('How many red cards are in a standard 52-card deck?', 'Cards:', key='26', note='Hearts and diamonds.'),
              sa('Two fair dice rolled independently: how many outcomes have the first die equal to 5?', 'Outcomes:', key='6', note='(5,1) to (5,6).'),
              tf('A standard 52-card deck has 2 red aces.', key=True, note='Hearts and diamonds.'),
              mc('How many numbers from 1 to 10 are odd and prime?', ['3', '4', '5', '2'], note='3, 5, 7.'),
              tf('A standard 52-card deck has 4 red kings.', key=False, note='2.'),
          ], align='exact',
            why=why('the student cannot count the outcomes of an event.', 'the fraction needs both counts.', 'counts outcomes.')),
          B('Use the definition of conditional probability', 'HSS-CP.A.3', [
              sa('P(A and B) = 1/12 and P(B) = 1/4. Find P(A given B).%s' % FL, 'P:', key='1/3', note='(1/12)/(1/4).'),
              tf('In a uniform model, P(A and B)/P(B) equals (count of A and B)/(count of B).', key=True,
                 note='The total cancels.'),
              mc('P(A and B) = 0.1 and P(B) = 0.5. Find P(A given B).', ['0.2', '0.05', '0.5', '5'], note='0.1/0.5.'),
              sa('P(A and B) = 2/36 and P(B) = 6/36. Find P(A given B).%s' % FL, 'P:', key='1/3', note='2/6.'),
              tf('P(A given B) = P(A and B)/P(A).', key=False, note='Divide by P(B).'),
          ], align='exact',
            why=why('the student does not connect the formula with counting.', 'both give the same fraction.',
                    'uses the definition.')),
      ],
      f1=B('Condition on "at least one"', 'HSS-CP.B.6', [
          sa('Two fair dice are rolled independently and at least one shows 6. What is P(the sum is 7)?%s' % FL, 'P:', key='2/11',
             note='11 outcomes contain a 6; (1,6) and (6,1) sum to 7.'),
          sa('A family has two children; each is equally likely to be a girl or a boy. Given at least one is a girl, what is '
             'P(both are girls)?%s' % FL, 'P:', key='1/3', note='GG, GB, BG.'),
          tf('Two fair coins are flipped independently. Given at least one shows heads, P(both heads) = 1/2.', key=False, note='1/3.'),
          mc('Two fair dice are rolled independently and the sum is at least 11. What is P(doubles)?', ['1/3', '1/2', '1/6', '1/36'],
             note='(5,6), (6,5), (6,6).'),
          tf('Conditioning on an event removes the outcomes outside it from the sample space.', key=True, note='Restriction.'),
      ], prog='same-course deepening', demand='Condition on compound events such as "at least one".'),
      f2=B('Multiply along a chain of conditions', 'HSS-CP.B.8', [
          sa('A bag has 4 red and 2 blue marbles. Two are drawn at random without replacement. What is P(both red)?%s' % FL, 'P:',
             key='2/5', note='(4/6)(3/5) = 12/30.'),
          tf('P(A and B) = P(A)·P(B given A).', key=True, note='General Multiplication Rule.'),
          sa('P(A) = 0.8 and P(B given A) = 0.25. Find P(A and B).', 'P(A and B):', key='0.2', note='0.8 · 0.25.'),
          mc('Two cards are drawn at random, without replacement, from a standard 52-card deck. What is P(second is a heart given the first is a heart)?', [
              '12/51', '13/52', '1/4', '13/51'], note='12 hearts left of 51 cards.'),
          tf('For draws without replacement, P(second red given first red) equals P(first red).', key=False,
             note='One red is gone.'),
      ], prog='cross-standard extension', demand='Use conditional probabilities as factors in a product.',
        builds='Builds on FORWARD 1: conditioning on what has happened is used step by step in a sequence of draws.')),

    # ------------------------------------------------------------------ 41. CP.B.7 Addition Rule
    S('HSS-CP.B.7', 'Apply the Addition Rule', num=41,
      target='Apply the Addition Rule, P(A or B) = P(A) + P(B) - P(A and B), and interpret the answer in terms of the model',
      strand='core', covers=['CP7-add'],
      main=[
          sa('P(A) = 0.45, P(B) = 0.35 and P(A and B) = 0.15. Find P(A or B).', 'P(A or B):', key='0.65',
             note='0.45 + 0.35 - 0.15.'),
          sa('A card is drawn at random from a standard 52-card deck. Find P(red or king).%s' % FL, 'P:', key='7/13', note='26 + 4 - 2 = 28; 28/52.'),
          sa('Two fair dice are rolled independently. Find P(doubles or sum of 8).%s' % FL, 'P:', key='5/18',
             note='6 + 5 - 1 = 10 outcomes; 10/36.'),
          mc('Of 200 students, 120 take Spanish, 70 take art, and 40 take both. A student is chosen at random. What is '
             'P(Spanish or art)?', ['3/4', '19/20', '1/5', '7/10'], note='150/200. 19/20 forgets to subtract the 40.'),
          mc('For a randomly chosen shopper, P(buys bread or milk) = 0.65. What does this mean?', [
              'About 65% of shoppers buy bread, milk, or both.', 'About 65% of shoppers buy both bread and milk.',
              'About 65% of shoppers buy neither one.', 'About 65% of shoppers buy exactly one.'],
             note='"Or" includes both.'),
      ],
      back=[
          B('Count a union without double counting', 'HSS-CP.A.1', [
              sa('A fair six-sided die is rolled. How many outcomes are "even or less than 3"?', 'Outcomes:', key='4', note='{1, 2, 4, 6}.'),
              tf('In a standard 52-card deck, the number of cards that are hearts or face cards is 13 + 12 - 3 = 22.', key=True, note='Remove the 3 heart face cards counted twice.'),
              mc('In a standard 52-card deck, how many cards are aces or spades?', ['16', '17', '13', '4'], note='4 + 13 - 1.'),
              sa('How many numbers from 1 to 20 are multiples of 2 or multiples of 5?', 'Numbers:', key='12',
                 note='10 + 4 - 2.'),
              tf('The number of outcomes in "A or B" is always the count of A plus the count of B.', key=False,
                 note='Subtract the overlap.'),
          ], align='exact',
            why=why('the student double counts the overlap.', 'the rule subtracts it.', 'counts unions correctly.')),
          B('Add and subtract fractions', '5.NF.A.1', [
              sa('Compute 1/2 + 1/13 - 1/26.%s' % FL, 'Answer:', key='7/13', note='13/26 + 2/26 - 1/26.'),
              sa('Compute 1/6 + 5/36 - 1/36.%s' % FL, 'Answer:', key='5/18', note='6/36 + 5/36 - 1/36.'),
              tf('1/4 + 1/3 = 7/12.', key=True, note='3/12 + 4/12.'),
              mc('Compute 3/5 + 7/20 - 1/5.', ['3/4', '9/20', '17/20', '1'], note='12/20 + 7/20 - 4/20.'),
              tf('1/2 + 1/3 = 2/5.', key=False, note='5/6.'),
          ], align='supporting',
            why=why('the student cannot combine fractions with unlike denominators.', 'card and dice answers are such sums.',
                    'adds and subtracts fractions.')),
      ],
      f1=B('Use the rule in reverse and with exclusive events', 'HSS-CP.B.7', [
          sa('P(A) = 0.5, P(B) = 0.4 and P(A or B) = 0.7. Find P(A and B).', 'P(A and B):', key='0.2', note='0.5 + 0.4 - 0.7.'),
          tf('If A and B are mutually exclusive, P(A or B) = P(A) + P(B).', key=True, note='P(A and B) = 0.'),
          sa('A fair six-sided die is rolled. Find P(1 or 6).%s' % FL, 'P:', key='1/3', note='Exclusive: 1/6 + 1/6.'),
          mc('P(A) = 0.3, P(B) = 0.5, and A and B are independent. What is P(A or B)?', ['0.65', '0.8', '0.15', '0.5'],
             note='0.3 + 0.5 - 0.15.'),
          tf('If P(A) = 0.6 and P(B) = 0.7, then A and B could be mutually exclusive.', key=False,
             note='P(A) + P(B) > 1.'),
      ], prog='same-course deepening', demand='Solve the rule for an unknown term and recognize special cases.'),
      f2=B('Combine the Addition Rule with complements', 'HSS-CP.B.7', [
          sa('P(A or B) = 0.65. What is P(neither A nor B)?', 'P:', key='0.35', note='1 - 0.65.'),
          sa('Of 200 students, 120 take Spanish, 70 take art and 40 take both. What is P(neither)?%s' % FL, 'P:', key='1/4',
             note='1 - 3/4.'),
          tf('P(not (A or B)) = 1 - P(A or B).', key=True, note='Complement.'),
          mc('A card is drawn at random from a standard 52-card deck. What is P(neither red nor a king)?', ['6/13', '7/13', '1/2', '11/26'], note='1 - 7/13.'),
          tf('P(neither A nor B) = 1 - P(A) - P(B) in every case.', key=False, note='Only if A and B cannot overlap.'),
      ], prog='same-course deepening', demand='Find "neither" probabilities with the rule and the complement.',
        builds='Builds on FORWARD 1: the rule\'s pieces are combined with the complement to answer "neither" questions.')),

    # ------------------------------------------------------------------ 42. CP.B.8 (+) general Multiplication Rule
    S('HSS-CP.B.8', 'Apply the general Multiplication Rule (+)', num=42,
      target='Apply the general Multiplication Rule in a uniform probability model, P(A and B) = P(A)·P(B given A) = '
             'P(B)·P(A given B), and interpret the answer',
      strand='advanced', covers=['CP8-mult'],
      main=[
          sa('A bag has 5 red and 3 blue marbles. Two are drawn at random without replacement. What is P(both red)?%s' % FL, 'P:',
             key='5/14', note='(5/8)(4/7) = 20/56.'),
          sa('A bag has 5 red and 3 blue marbles. Two are drawn at random without replacement. What is P(first red and second blue)?%s' % FL,
             'P:', key='15/56', note='(5/8)(3/7).'),
          sa('Two cards are drawn at random, without replacement, from a standard 52-card deck. What is P(both aces)?%s' % FL, 'P:', key='1/221', note='(4/52)(3/51).'),
          sa('P(A) = 0.6 and P(B given A) = 0.5. Find P(A and B).', 'P(A and B):', key='0.3', note='0.6 · 0.5.'),
          mc('A committee has 3 boys and 2 girls. Two members are chosen at random, one after the other. What is P(both girls)?', [
              '1/10', '4/25', '1/5', '2/5'], note='(2/5)(1/4). 4/25 assumes replacement.'),
      ],
      back=[
          B('Rearrange the conditional probability formula', 'HSS-CP.A.3', [
              tf('From P(B given A) = P(A and B)/P(A), it follows that P(A and B) = P(A)·P(B given A).', key=True,
                 note='Multiply both sides.'),
              sa('P(A) = 0.4 and P(B given A) = 0.25. Find P(A and B).', 'P(A and B):', key='0.1', note='Product.'),
              mc('P(B) = 0.5 and P(A given B) = 0.6. What is P(A and B)?', ['0.3', '1.1', '0.83', '0.1'], note='0.5 · 0.6.'),
              sa('P(A and B) = 0.12 and P(A) = 0.3. Find P(B given A).', 'P(B given A):', key='0.4', note='0.12/0.3.'),
              tf('P(A and B) = P(A) + P(B given A).', key=False, note='Multiply.'),
          ], align='exact',
            why=why('the student cannot solve the definition for P(A and B).', 'that is the Multiplication Rule.',
                    'rearranges the definition.')),
          B('Multiply fractions', '5.NF.B.4', [
              sa('Compute (5/8)(4/7).%s' % FL, 'Product:', key='5/14', note='20/56.'),
              sa('Compute (4/52)(3/51).%s' % FL, 'Product:', key='1/221', note='12/2652.'),
              tf('(2/5)(1/4) = 1/10.', key=True, note='2/20.'),
              mc('Compute (3/8)(2/7).', ['3/28', '5/15', '6/15', '3/56'], note='6/56.'),
              tf('(1/2)(1/3) = 2/5.', key=False, note='1/6.'),
          ], align='supporting',
            why=why('the student cannot multiply and simplify fractions.', 'the rule multiplies fractions.', 'multiplies '
                    'fractions.')),
          B('Multiply for independent events', 'HSS-CP.A.2', [
              sa('A fair die is rolled twice, independently. What is P(both 6)?%s' % FL, 'P:', key='1/36', note='(1/6)(1/6).'),
              tf('With replacement, P(red then red) from 5 red and 3 blue is (5/8)(5/8).', key=True, note='Independent draws.'),
              mc('A fair coin is flipped and a fair die is rolled, independently. P(tails and even)?', ['1/4', '1/2', '1/12', '2/3'], note='(1/2)(1/2).'),
              sa('Independent events have P(A) = 0.5 and P(B) = 0.3. Find P(A and B).', 'P(A and B):', key='0.15',
                 note='0.5 · 0.3.'),
              tf('Without replacement, draws are independent.', key=False, note='Without replacement changes the second draw.'),
          ], align='exact',
            why=why('the student cannot use the special case for independent events.', 'the general rule extends it.',
                    'multiplies probabilities of independent events.')),
      ],
      f1=B('Combine orders and longer chains', 'HSS-CP.B.8', [
          sa('A bag has 5 red and 3 blue marbles. Two are drawn at random without replacement. What is P(one of each color)?%s' % FL, 'P:',
             key='15/28', note='(5/8)(3/7) + (3/8)(5/7) = 30/56.'),
          sa('Three cards are drawn at random, without replacement, from a standard 52-card deck. What is P(all three are hearts)?%s' % FL, 'P:', key='11/850',
             note='(13/52)(12/51)(11/50) = 1716/132600.'),
          tf('P(A and B) = P(B)·P(A given B) gives the same answer as P(A)·P(B given A).', key=True, note='Both equal P(A and B).'),
          mc('A bag has 4 green and 6 yellow marbles. Two are drawn at random without replacement. What is P(both yellow)?', [
              '1/3', '9/25', '3/5', '2/5'], note='(6/10)(5/9) = 30/90.'),
          tf('P(first red and second blue) equals P(first blue and second red) for 5 red and 3 blue drawn without replacement.',
             key=True, note='Both 15/56.'),
      ], prog='same-course deepening', demand='Add over orders and extend the rule to three draws.'),
      f2=B('Count arrangements to find probabilities', 'HSS-CP.B.9', [
          sa('How many ways can 2 marbles be chosen from 8 (order does not matter)?', 'Ways:', key='28', note='8·7/2.'),
          sa('How many ways can 2 red marbles be chosen from 5 red?', 'Ways:', key='10', note='5·4/2.'),
          tf('P(both red) = 10/28 agrees with (5/8)(4/7).', key=True, note='Both 5/14.'),
          mc('How many ordered ways can 2 of 8 marbles be drawn one after the other?', ['56', '28', '64', '16'], note='8 · 7.'),
          tf('Counting with combinations always gives a different probability than the Multiplication Rule.', key=False,
             note='Both methods agree.'),
      ], prog='cross-standard extension', demand='Get the same probabilities by counting selections.',
        builds='Builds on FORWARD 1: the step-by-step products are recognized as ratios of counts.')),
]

SETS += [
    # ------------------------------------------------------------------ 43. CP.B.9 (+) permutations
    S('HSS-CP.B.9', 'Count ordered arrangements with permutations (+)', num=43,
      target='Use permutations to count ordered arrangements of objects, as a step toward computing probabilities of compound '
             'events',
      strand='advanced', covers=['CP9-perm'],
      main=[
          sa('Five runners race. In how many ways can first, second and third place be awarded?', 'Ways:', key=str(perm(5, 3)),
             note='5 · 4 · 3.'),
          sa('In how many ways can 6 different books be arranged on a shelf?', 'Ways:', key=str(perm(6)), note='6!.'),
          sa('A 4-digit code uses the digits 0-9 with no digit repeated. How many codes are possible?', 'Codes:',
             key=str(perm(10, 4)), note='10 · 9 · 8 · 7.'),
          mc('What is the value of 8P2 (the number of ordered arrangements of 2 objects from 8)?', ['56', '28', '16', '64'],
             note='8 · 7. 28 is 8C2.'),
          sa('A club of 10 members chooses a president, a vice president and a treasurer. How many ways are possible?', 'Ways:',
             key=str(perm(10, 3)), note='10 · 9 · 8.'),
      ],
      back=[
          B('Count outcomes with a tree or the counting principle', '7.SP.C.8.b', [
              sa('An outfit is a shirt (4 choices) and pants (3 choices). How many outfits?', 'Outfits:', key='12', note='4 · 3.'),
              tf('A tree for 3 stages with 2 choices each has 8 paths.', key=True, note='2^3.'),
              mc('A meal is a main (5 choices), a side (3) and a drink (2). How many meals?', ['30', '10', '15', '60'],
                 note='5 · 3 · 2.'),
              sa('A license code is a letter (26 choices) followed by a digit (10 choices). How many codes?', 'Codes:', key='260',
                 note='26 · 10.'),
              tf('With 3 shirts and 2 pants there are 5 outfits.', key=False, note='6.'),
          ], align='exact',
            why=why('the student does not multiply choices at each stage.', 'permutations are products of shrinking choices.',
                    'uses the counting principle.')),
          B('Multiply several whole numbers', '5.NBT.B.5', [
              sa('Compute 10 · 9 · 8.', 'Product:', key='720', note='90 · 8.'),
              sa('Compute 6 · 5 · 4 · 3 · 2 · 1.', 'Product:', key='720', note='6!.'),
              tf('5 · 4 · 3 = 60.', key=True, note='20 · 3.'),
              mc('Compute 7 · 6 · 5.', ['210', '180', '42', '343'], note='42 · 5.'),
              tf('4 · 3 · 2 · 1 = 10.', key=False, note='24.'),
          ], align='supporting',
            why=why('the student makes errors multiplying chains of numbers.', 'permutation counts are such chains.',
                    'multiplies multi-factor products.')),
      ],
      f1=B('Count arrangements with conditions', 'HSS-CP.B.9', [
          sa('In how many ways can the letters of MATH be arranged if M must be first?', 'Ways:', key='6', note='3! for the rest.'),
          sa('In how many ways can 5 people stand in a line if Ana and Ben must be at the two ends?', 'Ways:', key='12',
             note='2 ways for the ends · 3! = 12.'),
          tf('nPr = n!/(n - r)!.', key=True, note='Formula.'),
          mc('How many 3-letter arrangements (no repeats) can be made from the letters A, B, C, D, E if the first letter is a '
             'vowel?', ['24', '60', '12', '48'], note='2 vowels · 4 · 3.'),
          tf('The number of ways to arrange 4 people in a line is 4 + 3 + 2 + 1.', key=False, note='4 · 3 · 2 · 1 = 24.'),
      ], prog='same-course deepening', demand='Count arrangements that must satisfy a condition.'),
      f2=B('Count selections where order does not matter', 'HSS-CP.B.9', [
          sa('How many ways can 3 of 5 students be chosen for a team (order does not matter)?', 'Ways:', key='10',
             note='60 ordered / 3! = 10.'),
          tf('Each unordered group of 3 people can be ordered in 6 ways.', key=True, note='3!.'),
          mc('Which situation is counted with combinations rather than permutations?', [
              'choosing 3 pizza toppings', 'awarding gold, silver and bronze', 'arranging books on a shelf',
              'making a 4-digit code'], note='Order of toppings does not matter.'),
          sa('A permutation count is 120 for choosing 3 of 6 in order. How many unordered groups is that?', 'Groups:', key='20',
             note='120/6.'),
          tf('There are more combinations than permutations of 3 objects from 6.', key=False, note='Fewer.'),
      ], prog='same-course deepening', demand='Divide out orderings to count unordered selections.',
        builds='Builds on FORWARD 1: ordered counts are adjusted when order no longer matters.')),

    # ------------------------------------------------------------------ 44. CP.B.9 (+) combinations
    S('HSS-CP.B.9', 'Count unordered selections with combinations (+)', num=44,
      target='Use combinations to count selections in which order does not matter',
      strand='advanced', covers=['CP9-comb'],
      main=[
          sa('How many ways can 3 students be chosen from 5 (order does not matter)?', 'Ways:', key=str(comb(5, 3)),
             note='5C3 = 10.'),
          sa('A pizza shop has 8 toppings. How many 3-topping pizzas are possible (no repeated toppings)?', 'Pizzas:',
             key=str(comb(8, 3)), note='8C3 = 56.'),
          sa('How many 4-person committees can be chosen from 10 people?', 'Committees:', key=str(comb(10, 4)),
             note='10C4 = 210.'),
          mc('What is the value of 6C2?', ['15', '30', '12', '36'], note='6·5/2. 30 is 6P2.'),
          sa('Seven people each shake hands once with every other person. How many handshakes are there?', 'Handshakes:',
             key=str(comb(7, 2)), note='7C2 = 21.'),
      ],
      back=[
          B('Count ordered arrangements', 'HSS-CP.B.9', [
              sa('How many ordered ways can 3 of 5 students be lined up?', 'Ways:', key='60', note='5 · 4 · 3.'),
              tf('5P3 = 60.', key=True, note='5 · 4 · 3.'),
              mc('How many ordered pairs of different people can be formed from 7 people?', ['42', '21', '49', '14'],
                 note='7 · 6.'),
              sa('How many ways can 3 people be arranged in order?', 'Ways:', key='6', note='3!.'),
              tf('10P4 = 210.', key=False, note='5040; 210 is 10C4.'),
          ], align='exact',
            why=why('the student cannot count ordered arrangements.', 'combinations are found from them.', 'counts '
                    'permutations.')),
          B('Represent and count outcomes of compound events', '7.SP.C.8.b', [
              sa('How many 2-letter groups (order does not matter) can be chosen from the letters A, B, C?', 'Groups:', key='3',
                 note='AB, AC, BC.'),
              tf('From A, B, C, D, the groups AB and BA are the same group.', key=True, note='Unordered.'),
              mc('How many 2-letter groups (order does not matter) can be chosen from A, B, C, D?', ['6', '12', '4', '8'],
                 note='AB, AC, AD, BC, BD, CD.'),
              sa('How many ordered pairs of different letters can be made from A, B, C, D?', 'Pairs:', key='12', note='4 · 3.'),
              tf('An organized list of groups should include both AB and BA when order does not matter.', key=False,
                 note='List each group once.'),
          ], align='supporting',
            why=why('the student cannot list selections without repeating.', 'combinations count such lists.',
                    'lists unordered groups.')),
      ],
      f1=B('Count selections from separate groups', 'HSS-CP.B.9', [
          sa('A committee needs 3 of 5 boys and 2 of 4 girls. How many committees are possible?', 'Committees:',
             key=str(comb(5, 3) * comb(4, 2)), note='10 · 6.'),
          sa('How many ways can 2 hearts be chosen from the 13 hearts in a standard 52-card deck?', 'Ways:', key=str(comb(13, 2)), note='13C2.'),
          tf('nCr = n!/(r!(n - r)!).', key=True, note='Formula.'),
          mc('How many 5-card hands can be chosen from a standard 52-card deck (order does not matter)?', ['2,598,960', '311,875,200', '380,204,032', '260'],
             note='52C5. 311,875,200 is 52P5.'),
          tf('Choosing 2 from 4 girls and 3 from 5 boys gives 6 + 10 = 16 committees.', key=False, note='Multiply: 60.'),
      ], prog='same-course deepening', demand='Combine combination counts from separate groups.'),
      f2=B('Turn counts into probabilities', 'HSS-CP.B.9', [
          sa('3 people are chosen at random from 5 boys and 4 girls. How many groups are possible in all?', 'Groups:',
             key=str(comb(9, 3)), note='9C3 = 84.'),
          sa('3 people are chosen at random, without replacement (every group of 3 equally likely), from 5 boys and 4 girls. What is P(all three are girls)?%s' % FL, 'P:', key='1/21',
             note='4C3/9C3 = 4/84.'),
          tf('In a uniform model, P(event) = (number of outcomes in the event)/(number of outcomes in all).', key=True,
             note='Counting probability.'),
          mc('2 cards are drawn at random, without replacement, from a standard 52-card deck. What is P(both hearts)?', ['1/17', '1/16', '13/52', '1/4'], note='78/1326.'),
          tf('P(all three are boys) from 5 boys and 4 girls is 3/9.', key=False, note='10/84 = 5/42.'),
      ], prog='same-course deepening', demand='Use combination counts to compute probabilities.',
        builds='Builds on FORWARD 1: counts from separate groups become the numerator of a probability.')),

    # ------------------------------------------------------------------ 45. CP.B.9 (+) probability with counting
    S('HSS-CP.B.9', 'Compute probabilities with permutations and combinations (+)', num=45,
      target='Use permutations and combinations to compute probabilities of compound events and solve problems',
      strand='advanced', covers=['CP9-prob'],
      main=[
          sa('A lottery draws 3 different numbers from 1 to 10 (order does not matter). What is the probability that one ticket '
             'with 3 numbers wins?%s' % FL, 'P:', key=f(Fr(1, comb(10, 3))), note='1/10C3 = 1/120.'),
          sa('A 3-person group is chosen at random from 5 boys and 4 girls. What is P(all girls)?%s' % FL, 'P:', key='1/21',
             note='4/84.'),
          sa('Five people line up in random order. What is P(Ann is first and Bo is second)?%s' % FL, 'P:',
             key=f(Fr(perm(3), perm(5))), note='3!/5! = 6/120.'),
          sa('Two cards are dealt at random, without replacement, from a standard 52-card deck. What is P(both are hearts)?%s' % FL, 'P:', key='1/17',
             note='13C2/52C2 = 78/1326.'),
          mc('A 3-person group is chosen at random from 5 boys and 4 girls. What is P(exactly one girl)?', [
              '10/21', '5/21', '4/9', '1/3'], note='4C1 · 5C2 / 84 = 40/84.'),
      ],
      back=[
          B('Count with permutations and combinations', 'HSS-CP.B.9', [
              sa('Compute 10C3.', 'Answer:', key='120', note='720/6.'),
              sa('Compute 5!.', 'Answer:', key='120', note='5 · 4 · 3 · 2 · 1.'),
              tf('9C3 = 84.', key=True, note='504/6.'),
              mc('Compute 52C2.', ['1,326', '2,652', '104', '676'], note='52 · 51/2.'),
              tf('5C2 = 20.', key=False, note='10.'),
          ], align='exact',
            why=why('the student cannot compute the counts.', 'probabilities are ratios of them.', 'evaluates nPr and nCr.')),
          B('Multiply conditional probabilities along draws', 'HSS-CP.B.8', [
              sa('Using the Multiplication Rule, find P(both hearts) for two cards dealt at random, without replacement, from a standard 52-card deck.%s' % FL, 'P:',
                 key='1/17', note='(13/52)(12/51).'),
              tf('(4/9)(3/8)(2/7) = 1/21.', key=True, note='24/504.'),
              mc('From 5 boys and 4 girls, two are chosen in order without replacement. P(both boys)?', [
                  '5/18', '25/81', '5/9', '1/4'], note='(5/9)(4/8).'),
              sa('Five people line up at random. P(Ann first)?%s' % FL, 'P:', key='1/5', note='1 of 5.'),
              tf('A group has 5 boys and 4 girls. Two people are chosen one after the other, at random and without replacement. Given that '
                 'the first is a girl, P(second is a girl) = 4/9.', key=False, note='3/8.'),
          ], align='exact',
            why=why('the student cannot use the step-by-step method.', 'it checks the counting answer.', 'applies the '
                    'Multiplication Rule.')),
      ],
      f1=B('Use complements with counting', 'HSS-CP.B.9', [
          sa('A 3-person group is chosen at random from 5 boys and 4 girls. What is P(no girls)?%s' % FL, 'P:', key='5/42',
             note='10/84.'),
          sa('A 3-person group is chosen at random from 5 boys and 4 girls. What is P(at least one girl)?%s' % FL, 'P:',
             key='37/42', note='1 - 5/42.'),
          tf('P(at least one) = 1 - P(none).', key=True, note='Complement.'),
          mc('Four cards are dealt at random, without replacement, from a standard 52-card deck. What is P(no aces)? (48C4 = 194,580 and 52C4 = 270,725.)', [
              '38,916/54,145', '4/52', '1/13', '194,580/52'], note='194,580/270,725 in lowest terms.'),
          tf('P(at least one girl) = 3 · (4/9).', key=False, note='Not a valid method.'),
      ], prog='same-course deepening', demand='Use the complement to count "at least one" events.'),
      f2=B('Define a random variable from a counting model', 'HSS-MD.A.1', [
          sa('X = the number of girls in a group of 3 chosen at random (without replacement, every group equally likely) from 5 boys and 4 girls. What values can X take? Give the smallest and '
             'the largest.', ['Smallest:', 'Largest:'], key='0; 3', note='Form required: both.'),
          sa('X = the number of girls in a group of 3 chosen at random (without replacement, every group equally likely) from 5 boys and 4 girls. Find P(X = 0) and P(X = 3).%s' % FL, ['P(X = 0):', 'P(X = 3):'],
             key='5/42; 1/21', note='Form required: both. 10/84 and 4/84.'),
          tf('X = the number of girls in a group of 3 chosen at random (without replacement, every group equally likely) from 5 boys and 4 girls. The probabilities P(X = 0), P(X = 1), P(X = 2), P(X = 3) add to 1.', key=True, note='10 + 40 + 30 + 4 = 84.'),
          mc('X = the number of girls in a group of 3 chosen at random (without replacement, every group equally likely) from 5 boys and 4 girls. What is P(X = 2)?', ['5/14', '10/21', '1/21', '2/9'],
             note='4C2 · 5C1/84 = 30/84.'),
          tf('A random variable assigns a probability, not a number, to each outcome.', key=False,
             note='It assigns a number; the distribution gives probabilities.'),
      ], prog='cross-standard extension', demand='Collect counting probabilities into the distribution of a random variable.',
        builds='Builds on FORWARD 1: the probabilities of 0, 1, 2 or 3 girls are organized as a random variable.')),
]
