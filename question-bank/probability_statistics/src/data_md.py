"""S-MD (+), Using Probability to Make Decisions: random variables and their distributions, expected value, theoretical
and empirical distributions, weighing outcomes of decisions, fair decisions, and analyzing decisions and strategies
(sets 46-54). Every set is in the Advanced Extension strand."""
from fractions import Fraction as Fr
from math import comb

from qb import S, B, sa, mc, tf, hist
from common import why, tbl, pickfig
from data_cp1 import f, FL, two
from data_ic1 import DT as DIGT, DIGITS


def ev(dist):
    return sum(Fr(x) * Fr(p) for x, p in dist)


def dtab(xname, dist, pname='P(X = x)'):
    return tbl([xname] + [str(x) for x, _ in dist], [[pname] + [str(p) for _, p in dist]])


def bars(vals, cnts, label):
    desc = 'Bar graph of %s: ' % label.lower() + ', '.join('%s: %d' % (v, c) for v, c in zip(vals, cnts)) + '.'
    return hist([str(v) for v in vals], cnts, xlabel=label, ylabel='Frequency', ystep=1, ymax=max(cnts) + 1, desc=desc, gap=0.2)


H3 = [(0, '1/8'), (1, '3/8'), (2, '3/8'), (3, '1/8')]
DX = [(0, '0.1'), (1, '0.35'), (2, '0.4'), (3, '0.15')]
TV = {0: 5, 1: 30, 2: 40, 3: 20, 4: 5}
CPL = {0: 20, 1: 15, 2: 10, 3: 5}
G3 = [(k, f(Fr(comb(3, k)) * Fr(1, 4) ** k * Fr(3, 4) ** (3 - k))) for k in range(4)]
assert ev(H3) == Fr(3, 2) and ev(DX) == Fr(8, 5) and [p for _, p in G3] == ['27/64', '27/64', '9/64', '1/64']
assert ev([(x, Fr(c, 100)) for x, c in TV.items()]) == Fr(19, 10) and ev([(x, Fr(c, 50)) for x, c in CPL.items()]) == 1
TVT = tbl(['TVs in household', '0', '1', '2', '3', '4'], [['Households'] + [str(v) for v in TV.values()]])
CPT = tbl(['Complaints in a day', '0', '1', '2', '3'], [['Days'] + [str(v) for v in CPL.values()]])
# medical test: 1,000 people, 2% have the disease, test catches 90% of the sick, 5% false positives among the healthy
SICK, TP, FP = 20, 18, 49
TEST = two(['Has disease', 'Does not'], ['Tests positive', 'Tests negative'], [[TP, SICK - TP], [FP, 980 - FP]])
assert Fr(TP, TP + FP) == Fr(18, 67)

SETS = [
    # ------------------------------------------------------------------ 46. MD.A.1 random variables and distributions
    S('HSS-MD.A.1', 'Define a random variable and graph its distribution (+)', num=46,
      target='Define a random variable for a quantity of interest by assigning a numerical value to each event in a sample '
             'space, and graph the corresponding probability distribution',
      strand='advanced', covers=['MD1-define'],
      main=[
          sa('Three fair coins are flipped. X = number of heads. Find P(X = 0), P(X = 1), P(X = 2) and P(X = 3).%s' % FL,
             ['P(X = 0):', 'P(X = 1):', 'P(X = 2):', 'P(X = 3):'], key='1/8; 3/8; 3/8; 1/8',
             note='Form required: all four. Outcomes with 0, 1, 2, 3 heads: 1, 3, 3, 1 of 8.'),
          sa('Two fair dice are rolled and X = the sum. How many different values can X take, and what is P(X = 7)?%s' % FL,
             ['Number of values:', 'P(X = 7):'], key='11; 1/6', note='Form required: both. 2 to 12; 6 of 36.'),
          pickfig('Four fair coins are flipped and X = number of heads. Each bar graph shows, for X = 0 to 4, how many of the 16 '
                  'equally likely outcomes give that value. Which graph shows the distribution of X?', 'C', [
                      bars(range(5), [1, 4, 6, 4, 1], 'Number of heads'), bars(range(5), [3, 3, 4, 3, 3], 'Number of heads'),
                      bars(range(5), [6, 4, 3, 2, 1], 'Number of heads'), bars(range(5), [2, 4, 4, 4, 2], 'Number of heads')],
                  'Counts 1, 4, 6, 4, 1 (4C0 to 4C4). The others are flat, skewed, or have the wrong middle.'),
          mc('Which list could be a probability distribution for X = 1, 2, 3?', [
              '0.2, 0.5, 0.3', '0.3, 0.4, 0.4', '0.5, -0.1, 0.6', '0.2, 0.2, 0.2'],
             note='Each between 0 and 1 and summing to 1. The others sum to 1.1, include a negative, or sum to 0.6.'),
          sa('X takes the values 0, 1, 2, 3 with P(X = 0) = 0.1, P(X = 1) = 0.35 and P(X = 3) = 0.15. Find P(X = 2).',
             'P(X = 2):', key='0.4', note='1 - 0.6.'),
      ],
      back=[
          B('Describe outcomes in a sample space', 'HSS-CP.A.1', [
              sa('Three coins are flipped. How many outcomes have exactly 1 head?', 'Outcomes:', key='3', note='HTT, THT, TTH.'),
              tf('Three coin flips have 8 equally likely outcomes.', key=True, note='2^3.'),
              mc('Two dice are rolled. How many outcomes have a sum of 4?', ['3', '4', '2', '6'], note='(1,3), (2,2), (3,1).'),
              sa('Four coins are flipped. How many outcomes are there?', 'Outcomes:', key='16', note='2^4.'),
              tf('For two dice, the sums 2 and 12 each come from 2 outcomes.', key=False, note='One each.'),
          ], align='exact',
            why=why('the student cannot list the outcomes behind each value.', 'a random variable groups outcomes.',
                    'counts outcomes in events.')),
          B('Read and draw a distribution display', 'HSS-ID.A.1', [
              tf('In a bar graph of a distribution, taller bars show more likely values.', key=True, note='Height is frequency.'),
              mc('A bar graph shows counts 1, 4, 6, 4, 1 for X = 0 to 4. What is its shape?', [
                  'symmetric', 'skewed right', 'skewed left', 'uniform'], note='Mirror image.'),
              sa('Counts 1, 4, 6, 4, 1 are shown for X = 0 to 4. What is the total count?', 'Total:', key='16', note='Sum.'),
              tf('A bar graph with counts 6, 4, 3, 2, 1 is symmetric.', key=False, note='Skewed right.'),
              mc('Counts are 1, 4, 6, 4, 1 for X = 0 to 4. Which value of X is most likely?', ['2', '0', '4', '1'],
                 note='Tallest bar.'),
          ], align='exact',
            why=why('the student cannot read a graph of a distribution.', 'distributions are displayed like data.',
                    'reads bar graphs and shapes.')),
      ],
      f1=B('Find probabilities of ranges of values', 'HSS-MD.A.1', [
          sa('For X = number of heads in 3 flips, find P(X ≥ 2).%s' % FL, 'P:', key='1/2', note='3/8 + 1/8.'),
          sa('For X = sum of two dice, find P(X ≤ 4).%s' % FL, 'P:', key='1/6', note='1 + 2 + 3 = 6 outcomes.'),
          tf('The probabilities of all values of a random variable add to 1.', key=True, note='Distribution.'),
          mc('X takes the values 0 to 3 with probabilities 0.1, 0.35, 0.4, 0.15. What is P(X > 1)?', ['0.55', '0.45', '0.4', '0.9'],
             note='0.4 + 0.15.'),
          tf('P(X ≥ 1) = 1 - P(X = 1).', key=False, note='1 - P(X = 0).'),
      ], prog='same-course deepening', demand='Use a distribution to find probabilities of ranges of values.'),
      f2=B('Compute the expected value of a random variable', 'HSS-MD.A.2', [
          sa('X = number of heads in 3 flips. Find the expected value of X.', 'E(X):', key='1.5', note='(0 + 3 + 6 + 3)/8.'),
          tf('The expected value is the probability-weighted average of the values.', key=True, note='Definition.'),
          sa('X takes 0, 1, 2, 3 with probabilities 0.1, 0.35, 0.4, 0.15. Find E(X).', 'E(X):', key='1.6',
             note='0.35 + 0.8 + 0.45.'),
          mc('X = result of rolling one fair die. What is E(X)?', ['3.5', '3', '6', '21'], note='21/6.'),
          tf('The expected value must be one of the values X can take.', key=False, note='E(X) = 3.5 for a die.'),
      ], prog='cross-standard extension', demand='Summarize a distribution by its mean.',
        builds='Builds on FORWARD 1: the distribution just used for probabilities is summarized by its expected value.')),

    # ------------------------------------------------------------------ 47. MD.A.2 expected value
    S('HSS-MD.A.2', 'Calculate and interpret expected value (+)', num=47,
      target='Calculate the expected value of a random variable and interpret it as the mean of its probability distribution',
      strand='advanced', covers=['MD2-ev'],
      main=[
          sa('X = number of heads when 3 fair coins are flipped (table). Find E(X).', 'E(X):', key='1.5', fig=dtab('x', H3),
             note='0(1/8) + 1(3/8) + 2(3/8) + 3(1/8) = 12/8.'),
          sa('Find E(X) for the distribution in the table.', 'E(X):', key='1.6', fig=dtab('x', DX), note='0.35 + 0.8 + 0.45.'),
          sa('X = the number rolled on a fair six-sided die. Find E(X).', 'E(X):', key='3.5', note='(1 + 2 + ... + 6)/6.'),
          mc('For the distribution in the table, E(X) = 1.6. What does this mean?', [
              'Over many trials, the average value of X is about 1.6.', 'X will equal exactly 1.6 on most of the trials.',
              'X is 1.6 or less with a probability of 1.6.', 'The single most likely value of X is 1.6.'],
             fig=dtab('x', DX), note='Long-run mean.'),
          sa('A game pays $10 with probability 0.2, $2 with probability 0.3, and $0 otherwise. Find the expected payout.',
             'Dollars:', key='2.6', note='2 + 0.6.'),
      ],
      back=[
          B('Compute a mean', '6.SP.B.5.c', [
              sa('Find the mean of 1, 2, 3, 4, 5, 6.', 'Mean:', key='3.5', note='21/6.'),
              sa('Find the mean of 0, 1, 1, 1, 2, 2, 2, 3.', 'Mean:', key='1.5', note='12/8.'),
              tf('A value listed 3 times counts 3 times in the mean.', key=True, note='Weights.'),
              mc('Find the mean of 2, 2, 2, 8.', ['3.5', '5', '2', '14'], note='14/4.'),
              tf('The mean of 0, 0, 0, 4 is 2.', key=False, note='4/4 = 1.'),
          ], align='supporting',
            why=why('the student cannot compute a mean.', 'an expected value is a weighted mean.', 'computes means.')),
          B('Read a probability distribution', 'HSS-MD.A.1', [
              sa('In the distribution table with values 0 to 3, what is P(X = 2)?', 'P:', key='0.4', fig=dtab('x', DX),
                 note='Read the table.'),
              tf('A probability distribution lists every value of X with its probability.', key=True, note='Definition.'),
              mc('In the coin table, which values of X are equally likely?', ['1 and 2', '0 and 1', '2 and 3', 'all four'],
                 fig=dtab('x', H3), note='P(X = 1) = P(X = 2) = 3/8.'),
              sa('A distribution has P(X = 5) = 0.3 and P(X = 10) = 0.7. What is P(X = 5) + P(X = 10)?', 'Sum:', key='1',
                 note='Total probability.'),
              tf('A distribution may have probabilities adding to 1.2.', key=False, note='Must add to 1.'),
          ], align='exact',
            why=why('the student cannot read values and probabilities.', 'the expected value multiplies them.',
                    'reads distribution tables.')),
          B('Multiply and add decimals', '6.NS.B.3', [
              sa('Compute 2(0.4) + 3(0.15).', 'Answer:', key='1.25', note='0.8 + 0.45.'),
              sa('Compute 10(0.2) + 2(0.3).', 'Answer:', key='2.6', note='2 + 0.6.'),
              tf('1(0.35) + 2(0.4) = 1.15.', key=True, note='0.35 + 0.8.'),
              mc('Compute 5(0.3) + 10(0.7).', ['8.5', '15', '1.5', '7'], note='1.5 + 7.'),
              tf('4(0.25) + 2(0.5) = 1.5.', key=False, note='1 + 1 = 2.'),
          ], align='supporting',
            why=why('the student makes arithmetic errors in the weighted sum.', 'expected value is that sum.',
                    'computes sums of products.')),
      ],
      f1=B('Expected value with gains and losses', 'HSS-MD.A.2', [
          sa('A game: win $5 with probability 0.2, lose $2 with probability 0.8. Find the expected gain.', 'Dollars:', key='-0.6',
             note='1 - 1.6.'),
          tf('A negative expected gain means a player loses money on average over many plays.', key=True, note='Long run.'),
          sa('X has values -3, 0, 6 with probabilities 0.5, 0.2, 0.3. Find E(X).', 'E(X):', key='0.3', note='-1.5 + 1.8.'),
          mc('A game has expected gain -$0.60. About how much does a player expect to lose in 100 plays?', [
              '$60', '$0.60', '$6', '$600'], note='100 · 0.6.'),
          tf('If E(X) = 0, the player breaks even on every single play.', key=False, note='Only on average.'),
      ], prog='same-course deepening', demand='Compute expected values with negative values and over many trials.'),
      f2=B('Find expected values of theoretical distributions', 'HSS-MD.A.3', [
          sa('A student guesses on 4 true-false questions. X = number correct. Find P(X = 2).%s' % FL, 'P:', key='3/8',
             note='4C2/16 = 6/16.'),
          sa('A student guesses on 4 true-false questions. Find the expected number correct.', 'E(X):', key='2', note='4 · 0.5.'),
          tf('For n independent trials with success probability p, the expected number of successes is np.', key=True,
             note='Binomial mean.'),
          mc('A student guesses on 10 four-choice questions. What is the expected number correct?', ['2.5', '4', '10', '0.25'],
             note='10 · 1/4.'),
          tf('Guessing on 4 true-false questions, getting all 4 right has probability 1/4.', key=False, note='1/16.'),
      ], prog='cross-standard extension', demand='Build theoretical distributions and find their means.',
        builds='Builds on FORWARD 1: expected value is applied to distributions computed from a probability model.')),

    # ------------------------------------------------------------------ 48. MD.A.3 theoretical distributions
    S('HSS-MD.A.3', 'Develop a theoretical probability distribution (+)', num=48,
      target='Develop a probability distribution for a random variable whose probabilities can be calculated theoretically, '
             'and find its expected value',
      strand='advanced', covers=['MD3-theory'],
      main=[
          sa('A student guesses on 4 true-false questions. X = number correct. Find P(X = 2).%s' % FL, 'P:', key='3/8',
             note='4C2 · (1/2)^4 = 6/16.'),
          sa('A student guesses on 4 true-false questions. X = number correct. Find E(X).', 'E(X):', key='2', note='4 · 1/2.'),
          sa('A student guesses on 5 questions, each with 4 choices. Find P(all 5 correct) and the expected number correct.%s' % FL,
             ['P(all correct):', 'Expected number correct:'], key='1/1024; 1.25', note='Form required: both. (1/4)^5; 5 · 1/4.'),
          mc('A student guesses on 3 four-choice questions. What is P(exactly 1 correct)?', ['27/64', '9/64', '1/4', '3/4'],
             note='3 · (1/4)(3/4)^2.'),
          sa('A student guesses on 3 four-choice questions. What is P(at least 1 correct)?%s' % FL, 'P:', key='37/64',
             note='1 - (3/4)^3.'),
      ],
      back=[
          B('Count arrangements of successes', 'HSS-CP.B.9', [
              sa('In how many ways can exactly 2 of 4 answers be correct?', 'Ways:', key='6', note='4C2.'),
              sa('In how many ways can exactly 1 of 3 answers be correct?', 'Ways:', key='3', note='3C1.'),
              tf('5C5 = 1.', key=True, note='One way to get all correct.'),
              mc('In how many ways can exactly 3 of 5 answers be correct?', ['10', '15', '60', '5'], note='5C3.'),
              tf('4C2 = 8.', key=False, note='6.'),
          ], align='exact',
            why=why('the student cannot count which trials succeed.', 'each count multiplies a probability.', 'uses nCk.')),
          B('Multiply probabilities of independent trials', 'HSS-CP.A.2', [
              sa('Compute (1/2)^4.%s' % FL, 'Answer:', key='1/16', note='1/16.'),
              sa('Compute (1/4)(3/4)(3/4).%s' % FL, 'Answer:', key='9/64', note='9/64.'),
              tf('Guesses on different questions are independent.', key=True, note='Each guess is separate.'),
              mc('P(correct) = 1/4 on each of 2 independent guesses. P(both correct)?', ['1/16', '1/8', '1/2', '1/4'],
                 note='(1/4)^2.'),
              tf('(3/4)^3 = 9/12.', key=False, note='27/64.'),
          ], align='exact',
            why=why('the student cannot find the probability of one sequence.', 'theoretical probabilities multiply them.',
                    'multiplies independent probabilities.')),
      ],
      f1=B('Build the whole theoretical distribution', 'HSS-MD.A.3', [
          sa('A student guesses on 3 four-choice questions; X = number correct. Find P(X = 0), P(X = 1), P(X = 2), P(X = 3).%s' % FL,
             ['P(X = 0):', 'P(X = 1):', 'P(X = 2):', 'P(X = 3):'], key='; '.join(p for _, p in G3),
             note='Form required: all four. 3Ck (1/4)^k (3/4)^(3-k).'),
          sa('For X = number correct out of 3 four-choice guesses, find E(X).', 'E(X):', key='0.75', note='3 · 1/4.'),
          tf('The four probabilities 27/64, 27/64, 9/64, 1/64 add to 1.', key=True, note='64/64.'),
          mc('For 3 four-choice guesses, which value of X is least likely?', ['3', '0', '1', '2'], note='1/64.'),
          tf('For 3 four-choice guesses, X = 1 is more likely than X = 0.', key=False, note='Equal: 27/64 each.'),
      ], prog='same-course deepening', demand='List the full distribution and check it.'),
      f2=B('Compare a theoretical distribution with data', 'HSS-MD.A.4', [
          sa('A die is rolled 60 times. How many sixes does the theoretical distribution predict?', 'Sixes:', key='10',
             note='60/6.'),
          sa('In 60 rolls, a die showed 6 sixes. What is the empirical probability of a six? Give a decimal.', 'P:', key='0.1',
             note='6/60.'),
          tf('An empirical probability is found from observed data.', key=True, note='Definition.'),
          mc('In 100 households, the numbers of TVs gave an average of 1.9. This average is', [
              'the expected value of the empirical distribution', 'a theoretical probability from a model',
              'a margin of error for the survey', 'always equal to 2 for any survey'], note='Mean from data.'),
          tf('Empirical and theoretical probabilities for the same event are always equal.', key=False, note='Data vary.'),
      ], prog='cross-standard extension', demand='Set theoretical predictions beside observed frequencies.',
        builds='Builds on FORWARD 1: theoretical distributions are now compared with distributions found from data.')),

    # ------------------------------------------------------------------ 49. MD.A.4 empirical distributions
    S('HSS-MD.A.4', 'Develop an empirical probability distribution (+)', num=49,
      target='Develop a probability distribution for a random variable whose probabilities are assigned empirically from data, '
             'and find its expected value',
      strand='advanced', covers=['MD4-empirical'],
      main=[
          sa('100 households were surveyed (table). X = number of TVs in a randomly chosen household. Find P(X = 2) and '
             'P(X ≥ 3). Give decimals.', ['P(X = 2):', 'P(X ≥ 3):'], key='0.4; 0.25', fig=TVT,
             note='Form required: both. 40/100; (20 + 5)/100.'),
          sa('Using the TV survey, find the expected number of TVs in a household.', 'E(X):', key='1.9', fig=TVT,
             note='(30 + 80 + 60 + 20)/100.'),
          sa('Using the expected value 1.9 TVs per household, about how many TVs are expected in 500 households?', 'TVs:',
             key='950', note='500 · 1.9.'),
          mc('The TV survey gives E(X) = 1.9. Which interpretation is correct?', [
              'Households in this population average about 1.9 TVs.', 'Most of the households have exactly 1.9 TVs.',
              'Every household surveyed has 1 or 2 TVs.', 'There is a 1.9% chance of owning a TV.'], fig=TVT, note='Mean.'),
          sa('A store recorded complaints for 50 days (table). Find the expected number of complaints in a day.', 'E(X):',
             key='1', fig=CPT, note='(15 + 20 + 15)/50.'),
      ],
      back=[
          B('Find relative frequencies', '7.SP.C.6', [
              sa('In 100 households, 40 have 2 TVs. What is the relative frequency? Give a decimal.', 'Answer:', key='0.4',
                 note='40/100.'),
              sa('On 20 of 50 days there were no complaints. What is the relative frequency? Give a decimal.', 'Answer:',
                 key='0.4', note='20/50.'),
              tf('Relative frequencies of all categories add to 1.', key=True, note='All observations.'),
              mc('On 5 of 50 days there were 3 complaints. Relative frequency?', ['0.1', '0.05', '0.5', '5'], note='5/50.'),
              tf('A relative frequency of 0.25 means 25 observations.', key=False, note='25% of them.'),
          ], align='supporting',
            why=why('the student cannot turn counts into relative frequencies.', 'they become the probabilities.',
                    'computes relative frequencies.')),
          B('Compute an expected value', 'HSS-MD.A.2', [
              sa('X takes 0, 1, 2 with probabilities 0.5, 0.3, 0.2. Find E(X).', 'E(X):', key='0.7', note='0.3 + 0.4.'),
              tf('E(X) = Σ x·P(X = x).', key=True, note='Definition.'),
              mc('X takes 1 and 3 with probabilities 0.5 each. E(X)?', ['2', '4', '1.5', '3'], note='0.5 + 1.5.'),
              sa('X takes 0, 2, 4 with probabilities 0.25, 0.5, 0.25. Find E(X).', 'E(X):', key='2', note='Symmetric.'),
              tf('E(X) is found by adding the probabilities.', key=False, note='Multiply each value by its probability.'),
          ], align='exact',
            why=why('the student cannot compute E(X).', 'the empirical mean is the same computation.', 'computes expected '
                    'values.')),
      ],
      f1=B('Compare empirical and theoretical results', 'HSS-MD.A.4', [
          sa('A die was rolled 60 times: the faces 1-6 appeared 7, 13, 9, 11, 14, 6 times. Find the empirical P(6) and the '
             'theoretical P(6). Give decimals rounded to two places.', ['Empirical:', 'Theoretical:'], key='0.1; 0.17',
             note='Form required: both. 6/60; 1/6 = 0.1666...'),
          sa('Using the 60 rolls (faces 1-6 appeared 7, 13, 9, 11, 14, 6 times), find the empirical expected value of a roll.',
             'E(X):', key='3.5', note='(7 + 26 + 27 + 44 + 70 + 36)/60 = 210/60.'),
          tf('With many more rolls, empirical probabilities tend to get closer to the theoretical ones.', key=True,
             note='Law of large numbers.'),
          mc('Which result would most suggest the die is unfair?', [
              'In 6,000 rolls, a 6 appeared 1,800 times.', 'In 60 rolls, a 6 appeared 6 times.',
              'In 600 rolls, a 6 appeared 104 times.', 'In 6 rolls, no 6 appeared.'],
             note='30% in many rolls is far from 1/6.'),
          tf('An empirical distribution from 10 observations is as reliable as one from 10,000.', key=False,
             note='More data, more reliable.'),
      ], prog='same-course deepening', demand='Judge empirical distributions against theory and sample size.'),
      f2=B('Find the expected payoff of a game of chance', 'HSS-MD.B.5.a', [
          sa('A $2 ticket wins $500 with probability 1/1000. Find the expected net gain per ticket.', 'Dollars:', key='-1.5',
             note='0.5 - 2.'),
          tf('A game with negative expected net gain loses money for the player in the long run.', key=True, note='Long run.'),
          sa('A spinner: win $8 with probability 1/4, lose $2 otherwise. Find the expected gain.', 'Dollars:', key='0.5',
             note='2 - 1.5.'),
          mc('A game\'s expected net gain is -$1.50. Which interpretation is correct?', [
              'Over many plays, a player loses about $1.50 per play.', 'Every player loses exactly $1.50 on each play.',
              'The player wins $1.50 on about half the plays.', 'The game is fair, since some plays win.'], note='Average.'),
          tf('A game with expected net gain $0 is called fair.', key=True, note='Definition.'),
      ], prog='cross-standard extension', demand='Use expected value to judge a game of chance.',
        builds='Builds on FORWARD 1: expected values from distributions are used to weigh real choices.')),
]

assert Fr(comb(8, 2), comb(10, 2)) == Fr(28, 45) and Fr(comb(9, 2), comb(12, 2)) == Fr(6, 11)
assert Fr(comb(8, 5), comb(10, 5)) == Fr(2, 9)
WHO = {'0': 'A', '1': 'A', '2': 'B', '3': 'B', '4': 'C', '5': 'C', '6': 'D', '7': 'D'}
FIRST2 = next(WHO[c] for c in DIGITS[1] if c in WHO)
assert FIRST2 == 'C'

SETS += [
    # ------------------------------------------------------------------ 50. MD.B.5.a games of chance
    S('HSS-MD.B.5.a', 'Weigh the payoffs of a game of chance (+)', num=50,
      target='Find the expected payoff for a game of chance (lotteries, raffles, spinners, dice games) and interpret it',
      strand='advanced', covers=['MD5a-game'],
      main=[
          sa('A lottery ticket costs $2 and wins $500 with probability 1/1000; otherwise it wins nothing. Find the expected net '
             'gain per ticket.', 'Dollars:', key='-1.5', note='500/1000 - 2.'),
          sa('A game: roll a fair die. If it shows 6, you win $5; otherwise you lose $1. Find the expected gain per play.',
             'Dollars:', key='0', note='5(1/6) - 1(5/6) = 0.'),
          sa('A raffle sells 500 tickets at $5 each for one $1,000 prize. Find the expected net gain per ticket.', 'Dollars:',
             key='-3', note='1000/500 - 5.'),
          mc('A lottery ticket has expected net gain -$1.50. Which interpretation is correct?', [
              'Over many tickets, a buyer loses about $1.50 per ticket on average.',
              'Every ticket loses exactly $1.50 for the person who buys it.',
              'Buyers win $1.50 on about half of the tickets they buy.',
              'The lottery is fair, because some tickets win a prize.'],
             note='Long-run average.'),
          sa('A spinner wins $8 with probability 1/4 and loses $2 otherwise. Find the expected gain per spin.', 'Dollars:',
             key='0.5', note='2 - 1.5.'),
      ],
      back=[
          B('Compute an expected value', 'HSS-MD.A.2', [
              sa('X = 10 with probability 0.1 and X = 0 otherwise. Find E(X).', 'E(X):', key='1', note='10 · 0.1.'),
              tf('E(X) = Σ x·P(X = x).', key=True, note='Definition.'),
              mc('X = 4 with probability 0.25 and X = -1 otherwise. E(X)?', ['0.25', '1', '-0.75', '3'], note='1 - 0.75.'),
              sa('X = 100 with probability 0.01 and 0 otherwise. Find E(X).', 'E(X):', key='1', note='100 · 0.01.'),
              tf('E(X) = 5 when X = 10 with probability 0.2 and X = 0 otherwise.', key=False, note='2.'),
          ], align='exact',
            why=why('the student cannot compute E(X).', 'the payoff of a game is an expected value.', 'computes E(X).')),
          B('Add and subtract signed numbers', '7.NS.A.3', [
              sa('Compute 0.5 - 2.', 'Answer:', key='-1.5', note='Negative result.'),
              sa('Compute 5(1/6) - 1(5/6).', 'Answer:', key='0', note='5/6 - 5/6.'),
              tf('2 - 1.5 = 0.5.', key=True, note='Difference.'),
              mc('Compute 2 - 5.', ['-3', '3', '-7', '7'], note='Negative.'),
              tf('-1.5 + 2 = -3.5.', key=False, note='0.5.'),
          ], align='supporting',
            why=why('the student mishandles losses as negatives.', 'net gain combines wins and losses.',
                    'computes with signed numbers.')),
      ],
      f1=B('Set a price that makes a game fair', 'HSS-MD.B.5.a', [
          sa('A game pays $12 if a die shows 6 and nothing otherwise. What price makes the game fair?', 'Dollars:', key='2',
             note='Expected payout 12/6.'),
          sa('A raffle has one $1,000 prize and 400 tickets. What ticket price makes the raffle fair?', 'Dollars:', key='2.5',
             note='1000/400.'),
          tf('A game is fair when the price equals the expected payout.', key=True, note='Expected net 0.'),
          mc('A game costs $3 and pays $10 with probability 0.25. What is the expected net gain over 100 plays?', [
              '-$50', '$50', '-$0.50', '$250'], note='100(2.5 - 3).'),
          tf('A raffle with 400 tickets and a $1,000 prize is fair at $5 per ticket.', key=False, note='Fair at $2.50.'),
      ], prog='same-course deepening', demand='Work backward from fairness to a price and scale to many plays.'),
      f2=B('Compare decisions by expected value', 'HSS-MD.B.5.b', [
          sa('Option X gains $1,000 with probability 0.6 and loses $500 with probability 0.4. Option Y gains $300 for sure. Find '
             'the expected gain of each.', ['X:', 'Y:'], key='400; 300', note='Form required: both. 600 - 200.'),
          mc('Option X: expected gain $400 but a 40% chance of losing $500. Option Y: $300 for sure. Which statement is correct?', [
              'X has the higher expected value, but Y has no risk of loss.', 'Y has the higher expected value of the two.',
              'X is certain to gain $400 for whoever chooses it.', 'X and Y have exactly the same expected value.'], note='Expected value and risk.'),
          tf('Expected value describes the long-run average, not what happens in one decision.', key=True, note='Meaning.'),
          sa('Insurance costs $150. Without it, a $800 repair is needed with probability 0.1. What is the expected repair cost '
             'without insurance?', 'Dollars:', key='80', note='800 · 0.1.'),
          tf('Buying insurance always has a greater expected value than not buying it.', key=False,
             note='Insurers set prices above expected costs.'),
      ], prog='cross-standard extension', demand='Use expected values to compare two choices.',
        builds='Builds on FORWARD 1: expected payoffs of games become a tool for comparing decisions.')),

    # ------------------------------------------------------------------ 51. MD.B.5.b compare strategies by expected value
    S('HSS-MD.B.5.b', 'Evaluate and compare strategies by expected value (+)', num=51,
      target='Evaluate and compare strategies on the basis of expected values (insurance plans, warranties, investments)',
      strand='advanced', covers=['MD5b-compare'],
      main=[
          sa('Plan A: premium $1,200, deductible $500. Plan B: premium $900, deductible $1,000. A claim larger than $1,000 occurs '
             'with probability 0.2 (at most one claim). Find the expected yearly cost of each plan (premium plus expected '
             'deductible).', ['Plan A:', 'Plan B:'], key='1300; 1100', note='Form required: both. 1200 + 100; 900 + 200.'),
          mc('Plan A has expected cost $1,300 and plan B $1,100 per year. Which plan is better on the basis of expected cost?', [
              'Plan B', 'Plan A', 'They are equal', 'It cannot be decided'], note='Lower expected cost.'),
          sa('Option X gains $2,000 with probability 0.3 and loses $400 with probability 0.7. Option Y gains $250 for sure. Find '
             'the expected gain of each.', ['X:', 'Y:'], key='320; 250', note='Form required: both. 600 - 280.'),
          mc('X has expected gain $320 with a 70% chance of losing $400; Y gains $250 for sure. Which statement is correct?', [
              'X is better on average, but someone who cannot risk a loss may prefer Y.',
              'Y is better on expected value, so everyone should prefer Y.',
              'X is certain to gain $320 for the person who chooses it.',
              'X and Y have the same expected value, so they are equal.'],
             note='Expected value plus risk.'),
          sa('A phone warranty costs $150. Without it, a repair costing $800 is needed with probability 0.1. What is the expected '
             'repair cost without the warranty, and how much more is the warranty than that?', ['Expected cost:', 'Difference:'],
             key='80; 70', note='Form required: both. 800 · 0.1; 150 - 80.'),
      ],
      back=[
          B('Find the expected payoff of one choice', 'HSS-MD.B.5.a', [
              sa('A choice gains $200 with probability 0.5 and $0 otherwise. Find the expected gain.', 'Dollars:', key='100',
                 note='200 · 0.5.'),
              sa('A choice loses $1,000 with probability 0.2 and $0 otherwise. Find the expected loss.', 'Dollars:', key='200',
                 note='1000 · 0.2.'),
              tf('A sure gain of $300 has expected value $300.', key=True, note='Probability 1.'),
              mc('A bet wins $50 with probability 0.3 and loses $20 otherwise. Expected gain?', ['$1', '$15', '-$14', '$30'],
                 note='15 - 14.'),
              tf('A choice with expected gain $0 can never make money.', key=False, note='It averages 0.'),
          ], align='exact',
            why=why('the student cannot find one option\'s expected value.', 'comparisons need two of them.',
                    'computes expected payoffs.')),
          B('Read a distribution and its mean', 'HSS-MD.A.2', [
              tf('The option with the larger expected value is better on average.', key=True, note='Long run.'),
              sa('X = 1000 with probability 0.6 and -500 with probability 0.4. Find E(X).', 'E(X):', key='400', note='600 - 200.'),
              mc('Which has the larger expected value: $50 for sure, or $120 with probability 0.5?', [
                  '$120 with probability 0.5', '$50 for sure', 'they are equal', 'cannot tell'], note='60 > 50.'),
              sa('Cost = 500 with probability 0.2 and 0 otherwise. Find the expected cost.', 'Dollars:', key='100',
                 note='500 · 0.2.'),
              tf('Expected cost = cost × (1 - probability).', key=False, note='Cost × probability.'),
          ], align='exact',
            why=why('the student misreads expected values.', 'the decision rests on them.', 'computes and compares means.')),
      ],
      f1=B('Find break-even probabilities', 'HSS-MD.B.5.b', [
          sa('A $150 warranty covers an $800 repair. For what repair probability is the expected repair cost equal to $150? Give '
             'a decimal.', 'Probability:', key='0.1875', note='150/800.'),
          tf('If the repair probability is below the break-even value, skipping the warranty has the lower expected cost.',
             key=True, note='Expected repair cost < 150.'),
          sa('Plan A costs $1,200 plus a $500 deductible; plan B costs $900 plus a $1,000 deductible. For what claim probability '
             'p are the expected costs equal?', 'p:', key='0.6', note='1200 + 500p = 900 + 1000p.'),
          mc('With claim probability 0.8, which plan has the lower expected cost (A: 1200 + 500p; B: 900 + 1000p)?', [
              'Plan A', 'Plan B', 'They are equal', 'Neither'], note='A 1600, B 1700.'),
          tf('The better plan never depends on the claim probability.', key=False, note='It switches at p = 0.6.'),
      ], prog='same-course deepening', demand='Find where two strategies have equal expected value.'),
      f2=B('Make fair decisions with probability', 'HSS-MD.B.6', [
          mc('Three friends want to decide fairly who gets one ticket. Which method is fair?', [
              'Roll a die: 1-2 Ana, 3-4 Ben, 5-6 Cy.', 'Flip a coin: heads Ana, tails Ben.',
              'Choose the person who asks first.', 'Roll a die: 1 Ana, 2 Ben, 3-6 Cy.'], note='Each has 1/3.'),
          tf('A method is fair if every person has the same probability of being chosen.', key=True, note='Definition.'),
          sa('Ana has 3 tickets, Ben 5 and Cy 2 in a drawing of 10 tickets. What is P(Ben wins)?%s' % FL, 'P:', key='1/2',
             note='5/10.'),
          mc('In a two-dice game, A wins if the sum is 6, 7 or 8; otherwise B wins. Is it fair?', [
              'No: A wins with probability 4/9.', 'Yes: A has 3 sums and B has 8.', 'No: A wins with probability 3/11.',
              'Yes: each player has 1/2.'], note='5 + 6 + 5 = 16 of 36 outcomes.'),
          tf('Letting the oldest person choose is a fair random method.', key=False, note='Not random.'),
      ], prog='cross-standard extension', demand='Use probability to design and check fair decisions.',
        builds='Builds on FORWARD 1: from comparing strategies, the student turns to designing decisions that are fair.')),

    # ------------------------------------------------------------------ 52. MD.B.6 fair decisions
    S('HSS-MD.B.6', 'Use probabilities to make fair decisions (+)', num=52,
      target='Use probabilities to make fair decisions, for example drawing by lots or using a random number generator',
      strand='advanced', covers=['MD6-fair'],
      main=[
          mc('Three friends want to decide fairly who gets the last ticket. Which method is fair?', [
              'Roll a die: 1-2 Ana, 3-4 Ben, 5-6 Cy.', 'Flip a coin: heads Ana, tails Ben; Cy only on an edge.',
              'Roll a die: 1 Ana, 2 Ben, 3-6 Cy.', 'Ana chooses, since she asked first.'],
             note='Each person gets 2 of 6 outcomes.'),
          sa('Four people A, B, C, D are chosen from with random digits: 0-1 = A, 2-3 = B, 4-5 = C, 6-7 = D, and 8-9 are skipped. '
             'Reading line 2 of the table from the left, who is chosen? Enter A, B, C or D.', 'Person:', key=FIRST2, fig=DIGT,
             note='The first digit of line 2 is 4 → C.'),
          sa('Two players each flip a coin. Ana wins if the coins match; Ben wins if they differ. What is P(Ana wins)?%s' % FL, 'P:',
             key='1/2', note='HH or TT: 2 of 4.'),
          mc('Two dice are rolled. Player A wins if the sum is 6, 7 or 8; otherwise B wins. Is the game fair?', [
              'No: A wins with probability 4/9.', 'Yes: the sums are split fairly.', 'No: A wins with probability 3/11.',
              'Yes: each player wins with probability 1/2.'], note='16 of 36 outcomes.'),
          sa('In a drawing, Ana has 3 tickets, Ben 5 and Cy 2, out of 10. What is P(Ben wins)?%s' % FL, 'P:', key='1/2',
             note='5/10.'),
      ],
      back=[
          B('Simulate with random digits', 'HSS-IC.A.2', [
              tf('Each digit 0-9 in a random-digit table is equally likely.', key=True, note='Uniform.'),
              mc('To choose among 4 people with single digits, which assignment is fair?', [
                  '0-1, 2-3, 4-5, 6-7 and skip 8-9', '0-2, 3-5, 6-8 and 9', '0-1, 2-3, 4-5, 6-9', '0, 1, 2, 3 and stop'],
                 note='Two digits each, extras skipped.'),
              sa('Using 0-1 = A, 2-3 = B, 4-5 = C, 6-7 = D, skip 8-9, what does the digit 9 mean?', 'Answer (enter skip or a '
                                                                                                      'letter):',
                 key='skip', note='Skipped.'),
              tf('Skipping digits 8 and 9 makes the assignment unfair.', key=False, note='The others stay equally likely.'),
              mc('Using the same assignment, the digits read 8, 9, 3. Who is chosen?', ['B', 'D', 'A', 'no one'],
                 note='8 and 9 skipped; 3 → B.'),
          ], align='exact',
            why=why('the student cannot use digits to choose at random.', 'fair decisions often use them.',
                    'assigns and reads random digits.')),
          B('Find probabilities in a uniform model', '7.SP.C.7.a', [
              sa('A die is rolled. What is P(1 or 2)?%s' % FL, 'P:', key='1/3', note='2/6.'),
              tf('With a fair coin, heads and tails each have probability 1/2.', key=True, note='Uniform.'),
              mc('Names of 5 people are in a hat. P(a particular person is drawn)?', ['1/5', '1/4', '1/2', '5'], note='Uniform.'),
              sa('Two coins are flipped. What is P(they match)?%s' % FL, 'P:', key='1/2', note='HH, TT.'),
              tf('A spinner with one half red and two quarters blue and green is fair among the three colors.', key=False,
                 note='1/2, 1/4, 1/4.'),
          ], align='supporting',
            why=why('the student cannot compute the chances a method gives each person.', 'fairness compares them.',
                    'finds probabilities in uniform models.')),
      ],
      f1=B('Design fair methods for awkward numbers', 'HSS-MD.B.6', [
          mc('Five people must be chosen from fairly with one die. Which method works?', [
              'Assign 1-5 to the people and reroll a 6.', 'Assign 1-5 to the people and give 6 to the first person.',
              'Roll and divide the result by 5.', 'Assign 1-6 and let the sixth face mean "everyone".'],
             note='Rerolling keeps 1/5 each.'),
          sa('With the "reroll a 6" method for 5 people, what is each person\'s probability of being chosen?%s' % FL, 'P:',
             key='1/5', note='Uniform over 5 faces.'),
          tf('A method that gives one person 2 of 6 die faces and the others 1 each is unfair.', key=True, note='2/6 vs 1/6.'),
          sa('Using two-digit numbers 00-99, how many numbers should each of 3 people get for a fair choice, if the rest are '
             'skipped?', 'Numbers each:', key='33', note='99 numbers (00-98) split 33 each; skip 99.'),
          tf('Drawing names one at a time from a hat without replacement is unfair to the last name.', key=False,
             note='Each order position is equally likely.'),
      ], prog='same-course deepening', demand='Build fair methods when the number of people does not divide the outcomes.'),
      f2=B('Analyze a decision with a medical test', 'HSS-MD.B.7', [
          sa('Of 1,000 people, 2% have a disease. How many have it?', 'People:', key='20', note='0.02 · 1000.'),
          sa('A test is positive for 90% of the 20 people with the disease. How many test positive?', 'People:', key='18',
             note='0.9 · 20.'),
          tf('A test can give positive results for people who do not have the disease.', key=True, note='False positives.'),
          mc('Of the 980 healthy people, 5% test positive. How many false positives?', ['49', '18', '5', '931'],
             note='0.05 · 980.'),
          tf('If a test is positive for 90% of sick people, then 90% of positives are sick.', key=False,
             note='The condition is reversed.'),
      ], prog='cross-standard extension', demand='Use counts in a large population to analyze a test decision.',
        builds='Builds on FORWARD 1: probability reasoning about fairness extends to reasoning about medical decisions.')),

    # ------------------------------------------------------------------ 53. MD.B.7 medical testing
    S('HSS-MD.B.7', 'Analyze decisions about medical testing (+)', num=53,
      target='Use probability concepts to analyze decisions, such as medical testing: find and interpret the probability of '
             'disease given a positive result',
      strand='advanced', covers=['MD7-testing'],
      main=[
          sa('1,000 people are tested. 2% have a disease; the test is positive for 90% of people with the disease. How many have '
             'the disease, and how many of them test positive?', ['Have the disease:', 'Test positive:'], key='20; 18',
             note='Form required: both.'),
          sa('Of the 980 people without the disease, 5% test positive. How many false positives are there?', 'People:', key='49',
             note='0.05 · 980.'),
          sa('Use the table for 1,000 people. A person tests positive. What is P(has disease given positive)?%s' % FL, 'P:',
             key='18/67', fig=TEST, note='18/(18 + 49).'),
          mc('In the table, P(disease given positive) = 18/67, about 27%. What does this show?', [
              'Most people who test positive do not have the disease.', 'The test is wrong 73% of the time for everyone.',
              'Most people who have the disease test negative.', 'A positive test means a 90% chance of disease.'],
             fig=TEST, note='Low prevalence makes false positives outnumber true ones.'),
          sa('Use the table. A person tests negative. What is P(does not have the disease given negative)?%s' % FL, 'P:',
             key='931/933', fig=TEST, note='931/(931 + 2).'),
      ],
      back=[
          B('Read a two-way table as a sample space', 'HSS-CP.A.4', [
              sa('In the test table, how many people test positive in all?', 'People:', key='67', fig=TEST, note='18 + 49.'),
              sa('In the test table, how many people test negative in all?', 'People:', key='933', fig=TEST, note='2 + 931.'),
              tf('In the test table, 20 people have the disease.', key=True, fig=TEST, note='Row total.'),
              mc('In the test table, which cell counts false positives?', [
                  'does not have the disease, tests positive', 'has the disease, tests positive',
                  'has the disease, tests negative', 'does not have the disease, tests negative'], fig=TEST, note='49.'),
              tf('In the test table, false negatives number 18.', key=False, fig=TEST, note='2.'),
          ], align='exact',
            why=why('the student cannot read the cells of a test table.', 'each probability uses them.', 'reads two-way '
                    'tables.')),
          B('Find a conditional probability as a fraction of outcomes', 'HSS-CP.B.6', [
              sa('Of 67 people who test positive, 18 have the disease. What fraction is that?', 'Fraction:', key='18/67',
                 note='18/67.'),
              tf('P(disease given positive) uses the positive column as the sample space.', key=True, note='Condition.'),
              mc('Of 20 people with the disease, 18 test positive. P(positive given disease)?', ['9/10', '18/67', '1/50', '2/20'],
                 note='18/20.'),
              sa('Of 980 healthy people, 49 test positive. What is P(positive given healthy)? Give a decimal.', 'P:', key='0.05',
                 note='49/980.'),
              tf('P(positive given disease) = P(disease given positive).', key=False, note='9/10 vs 18/67.'),
          ], align='exact',
            why=why('the student conditions on the wrong group.', 'the key question conditions on a positive test.',
                    'computes conditional fractions.')),
      ],
      f1=B('See how prevalence changes the answer', 'HSS-MD.B.7', [
          sa('Now 10% of 1,000 people have the disease; the test is positive for 90% of them and for 5% of the healthy. How many '
             'true positives and how many false positives?', ['True positives:', 'False positives:'], key='90; 45',
             note='Form required: both. 0.9 · 100; 0.05 · 900.'),
          sa('With 90 true positives and 45 false positives, what is P(disease given positive)?%s' % FL, 'P:', key='2/3',
             note='90/135.'),
          tf('The same test gives a higher P(disease given positive) when the disease is more common.', key=True,
             note='18/67 versus 2/3.'),
          mc('Why do doctors often order a second test after a positive result for a rare disease?', [
              'Many first positives are false positives.', 'The first test is always wrong.',
              'A second test lowers the prevalence.', 'Negative results are never correct.'], note='Low prevalence.'),
          tf('For a rare disease, a positive result makes having the disease certain.', key=False, note='About 27% here.'),
      ], prog='same-course deepening', demand='Compare the same test in populations with different prevalence.'),
      f2=B('Analyze strategies in games and quality control', 'HSS-MD.B.7', [
          sa('A box of 10 parts has 2 defective. An inspector checks 2 parts at random. What is P(no defective part is found)?%s' % FL,
             'P:', key='28/45', note='8C2/10C2.'),
          tf('Checking more parts raises the chance of finding a defective part.', key=True, note='Fewer escape.'),
          sa('A test question has 4 choices; a correct answer earns 1 point and a wrong answer loses 1/3 point. What is the '
             'expected score of a random guess, and of a guess after one wrong choice is eliminated?%s' % FL,
             ['Random guess:', 'After eliminating one:'], key='0; 1/9', note='Form required: both. 1/4 - (3/4)(1/3); 1/3 - '
                                                                           '(2/3)(1/3).'),
          mc('Using those expected scores, when is guessing worthwhile?', [
              'after eliminating at least one wrong choice', 'never, under any circumstances', 'always, even with no information',
              'only on the last question of the test'], note='Expected 1/9 > 0.'),
          tf('A strategy with a higher expected value always wins in a single try.', key=False, note='Only on average.'),
      ], prog='same-course deepening', demand='Apply the same probability analysis to other decisions.',
        builds='Builds on FORWARD 1: the decision analysis used for tests is carried to inspection and test-taking strategy.')),

    # ------------------------------------------------------------------ 54. MD.B.7 strategies
    S('HSS-MD.B.7', 'Analyze strategies and decisions with probability (+)', num=54,
      target='Use probability concepts to analyze decisions and strategies, such as product testing, test-taking and when to '
             'take a risk in a game',
      strand='advanced', covers=['MD7-strategy'],
      main=[
          sa('A hockey team trails by 1 goal with 2 minutes left. Keeping the goalie gives a 0.08 chance of tying; pulling the '
             'goalie for an extra skater gives a 0.20 chance of tying (but more chance of allowing another goal, which also loses). '
             'Give both chances of tying.', ['Keep goalie:', 'Pull goalie:'], key='0.08; 0.2', note='Form required: both.'),
          mc('The team loses unless it ties. Keeping the goalie gives a 0.08 chance of tying; pulling gives 0.20. Which strategy '
             'is better?', [
              'Pull the goalie: it gives the better chance of avoiding a loss.',
              'Keep the goalie: allowing another goal would be worse.',
              'Keep the goalie: 0.08 is the safer probability.',
              'Either one: both chances are less than one-half.'],
             note='A second goal against changes nothing: a loss is a loss.'),
          sa('A box of 12 parts has 3 defective. An inspector checks 2 parts at random. What is P(no defective part is found)?%s'
             % FL, 'P:', key='6/11', note='9C2/12C2 = 36/66.'),
          sa('A test question has 5 choices; a correct answer earns 1 point and a wrong answer loses 1/4 point. Find the expected '
             'score of a random guess, and of a guess after eliminating one wrong choice.%s' % FL,
             ['Random guess:', 'After eliminating one:'], key='0; 1/16', note='Form required: both. 1/5 - (4/5)(1/4); 1/4 - '
                                                                            '(3/4)(1/4).'),
          mc('A company can test 2 or 5 parts from each box of 10 (2 defective). With 2 tested, P(missing both defectives) = 28/45; '
             'with 5 tested, it is 2/9. Which is correct?', [
              'Testing 5 parts lowers the chance of missing the defects.', 'Testing 2 parts finds the defects more often.',
              'The number tested does not change anything.', 'Testing 5 parts always finds both defects.'],
             note='With 5 tested, P(no defective found) = 8C5/10C5 = 56/252 = 2/9, less than 28/45.'),
      ],
      back=[
          B('Compare expected values of choices', 'HSS-MD.A.2', [
              sa('Strategy A scores 3 with probability 0.5 and 0 otherwise. Find its expected score.', 'Score:', key='1.5',
                 note='3 · 0.5.'),
              tf('Between two strategies, the one with the larger expected value is better on average.', key=True,
                 note='Long run.'),
              mc('Strategy B scores 2 for sure; strategy A scores 3 with probability 0.5. Which is better on average?', [
                  'B', 'A', 'equal', 'cannot tell'], note='2 > 1.5.'),
              sa('A guess earns 1 with probability 1/3 and loses 1/3 otherwise. Expected score?%s' % FL, 'Score:', key='1/9',
                 note='1/3 - 2/9.'),
              tf('An expected score of 0 means the strategy always scores 0.', key=False, note='Average.'),
          ], align='exact',
            why=why('the student cannot compare strategies by expected value.', 'strategy analysis depends on it.',
                    'computes and compares expected values.')),
          B('Count selections to find probabilities', 'HSS-CP.B.9', [
              sa('Compute 10C2.', 'Answer:', key='45', note='10 · 9/2.'),
              sa('Compute 8C2.', 'Answer:', key='28', note='8 · 7/2.'),
              tf('8C5 = 56.', key=True, note='8C3.'),
              mc('Compute 10C5.', ['252', '120', '30240', '50'], note='Combinations.'),
              tf('P(no defectives in 2 of 10 with 2 defective) = 8/10.', key=False, note='28/45.'),
          ], align='exact',
            why=why('the student cannot count selections.', 'inspection probabilities are ratios of counts.', 'computes nCr.')),
      ],
      f1=B('Weigh probabilities against consequences', 'HSS-MD.B.7', [
          sa('A product test costs $50 per box and finds the defects with probability 0.8. An undetected defective box costs '
             '$400. For a defective box, what is the expected cost of shipping without testing, and with testing (test cost plus '
             'expected cost of a missed defect)?', ['Without testing:', 'With testing:'], key='400; 130',
             note='Form required: both. 50 + 0.2 · 400.'),
          tf('A strategy can have a better expected value even if it sometimes produces the worst outcome.', key=True,
             note='Expected value averages outcomes.'),
          mc('A student must decide whether to guess on 10 four-choice questions with a 1/3-point penalty. Which strategy has '
             'the highest expected score?', [
              'Guess only where at least one choice can be eliminated.', 'Never guess at all.',
              'Guess on every question, even with no information.', 'Leave every question blank.'],
             note='Expected 0 with no information; 1/9 or more after eliminating.'),
          sa('With two choices eliminated (2 left), what is the expected score of a guess (1 point right, -1/3 wrong)?%s' % FL,
             'Score:', key='1/3', note='1/2 - (1/2)(1/3).'),
          tf('Probability analysis can tell exactly what will happen in one game.', key=False, note='It describes chances.'),
      ], prog='same-course deepening', demand='Combine probabilities with costs to choose a strategy.'),
      f2=B('Combine several probability tools in one decision', 'HSS-MD.B.7', [
          sa('A quiz has 5 four-choice questions. A student guesses on all. What is the expected number correct, and P(all '
             'wrong)?%s' % FL, ['Expected correct:', 'P(all wrong):'], key='1.25; 243/1024',
             note='Form required: both. 5/4; (3/4)^5.'),
          tf('P(at least one correct) = 1 - P(all wrong).', key=True, note='Complement.'),
          sa('A quiz has 5 four-choice questions and a student guesses on all. What is P(at least one correct)?%s' % FL, 'P:',
             key='781/1024', note='1 - 243/1024.'),
          mc('A team must choose between a play that gains 2 points with probability 0.5 and one that gains 3 points with '
             'probability 0.3. Which has the higher expected gain?', ['the 2-point play', 'the 3-point play', 'equal',
                                                                       'cannot tell'],
             note='1.0 versus 0.9.'),
          tf('If the team needs 3 points to win, the 2-point play is still the better choice.', key=False,
             note='Only the 3-point play can win; its chance is 0.3 versus 0.'),
      ], prog='same-course deepening', demand='Use expected value, complements and goals together.',
        builds='Builds on FORWARD 1: costs and probabilities are combined with a goal that changes which strategy is best.')),
]
