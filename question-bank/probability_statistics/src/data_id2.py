"""S-ID.A.2-3: comparing center and spread, interpreting differences in context, outliers (sets 4-7)."""
from qb import S, B, sa, mc, tf
from common import why, n, d1, mean, median, five, fences, sd_pop, sd_samp, dlist, QRULE, OUTRULE, TECH
from datasets import D
from data_id1 import (boxf, boxes2, TOWNA, TOWNB, CLP, CLQ, STX, STY, PLA, PLB, M1, M2, TEAMA, TEAMB, SD1, SD2, SD3, SD4,
                      RENTA, RENTB, FISHA, FISHB, GAMES, HOURS, PRICES, POP)


def iqr(xs):
    f = five(xs)
    return f[3] - f[1]


def nm(v):
    return n(float(v))


CALLS = D('S7 calls', [3, 5, 4, 6, 5, 4, 22, 5, 3, 4], 'calls', 'Support calls received in each of 10 hours')
MILES = D('S6 miles', [3, 4, 4, 5, 5, 5, 6, 6, 7], 'miles', 'Distances 9 runners ran on one day')

SETS = [
    # ------------------------------------------------------------------ 4. ID.A.2 compare centers
    S('HSS-ID.A.2', 'Compare centers with the measure suited to the shape', num=4,
      target='Compare the centers of two data sets, choosing the median when a set is skewed or has outliers and the mean when '
             'both are roughly symmetric, and computing that measure for each set',
      strand='core', covers=['ID2-center'],
      main=[
          sa('Sale prices (thousands of dollars) of 8 homes in each of two towns: Town A: %s; Town B: %s. Compare the typical '
             'prices with one measure of center suited to the shapes of both data sets. Give that measure for each town.' % (
                 dlist(TOWNA), dlist(TOWNB)), ['Town A:', 'Town B:'], key='%s; %s' % (nm(median(TOWNA)), nm(median(TOWNB))),
             note='Form required: both medians. Town A has an extreme value (900), so the median is suited; the same measure is '
                  'used for both towns. Town A: (240 + 245)/2 = 242.5; Town B: (255 + 270)/2 = 262.5. (Town A\'s mean, 320, is '
                  'pulled up by 900.)'),
          mc('Scores of 7 students in each of two classes: class P: %s; class Q: %s. Which comparison of centers is appropriate '
             'and correct?' % (dlist(CLP), dlist(CLQ)), [
              'Both are roughly symmetric with no outliers, so compare means: P\'s mean 78 is 4 points above Q\'s mean 74.',
              'Both are roughly symmetric, so compare means: P\'s mean 76 is 2 points above Q\'s mean 74.',
              'Compare the highest scores: P\'s 86 is 4 points above Q\'s 82, so P is 4 points higher.',
              'Compare medians: P\'s median 76 is 2 points above Q\'s median 74, so P is 2 points higher.'],
             note='Means: 546/7 = 78 and 518/7 = 74 (the medians are also 78 and 74). The others miscompute the mean or median of P, '
                  'or compare maximums, which do not describe the center.'),
          sa('Delivery times (days) of 9 orders from each of two stores: store X: %s; store Y: %s. Compare the typical delivery '
             'times with one measure of center suited to the shapes of both data sets. Give that measure for each store.' % (
                 dlist(STX), dlist(STY)), ['Store X:', 'Store Y:'], key='%s; %s' % (nm(median(STX)), nm(median(STY))),
             note='Form required: both medians. Store X has an extreme value (14), so medians are used: 3 and 4 (5th values).'),
          mc('Heights (cm) of 7 seedlings of each of two plants: plant A: %s; plant B: %s. Which comparison of typical heights is '
             'appropriate?' % (dlist(PLA), dlist(PLB)), [
              'A is skewed by the value 30, so compare medians: B\'s median 9 cm is greater than A\'s median 7 cm.',
              'Compare means: A\'s mean (about 9.9 cm) is greater, so A\'s seedlings are typically taller.',
              'Compare means: both are about 9 cm, so the seedlings are typically the same height.',
              'Compare maximums: A\'s tallest seedling (30 cm) is taller, so A\'s seedlings are typically taller.'],
             note='A\'s mean 69/7 ≈ 9.86 is pulled up by 30; medians 7 and 9 describe typical seedlings. The others use the mean '
                  'despite the outlier or use the maximum.'),
          sa('Masses (grams) of 6 bags filled by each of two machines: machine 1: %s; machine 2: %s. Compare the typical masses '
             'with one measure of center suited to the shapes of both data sets. Give that measure for each machine.' % (
                 dlist(M1), dlist(M2)), ['Machine 1:', 'Machine 2:'], key='%s; %s' % (nm(mean(M1)), nm(mean(M2))),
             note='Form required: both. Both sets are symmetric with no outliers, so means suit: 3000/6 = 500 and 3030/6 = 505. '
                  '(The medians are also 500 and 505, so either measure gives the same values.)'),
      ],
      back=[
          B('Compute a mean', '6.SP.B.5.c', [
              sa('Find the mean of 4, 7, 10.', 'Mean:', key='7', note='21/3.'),
              sa('Find the mean of 2, 3, 5, 6. Give a decimal.', 'Mean:', key='4', note='16/4.'),
              tf('The mean of 1, 2, 3, 10 is 4.', key=True, note='16/4 = 4.'),
              mc('What is the mean of 5, 5, 6, 8?', ['6', '5', '5.5', '24'], note='24/4. 5 is the mode, 5.5 the median, 24 the sum.'),
              sa('Find the mean of 1.5, 2.5, 3.5. Give a decimal.', 'Mean:', key='2.5', note='7.5/3.'),
          ], align='exact',
            why=why('the student cannot compute a mean.', 'symmetric data are compared by their means.', 'computes means of '
                    'whole-number and decimal data.')),
          B('Compute a median', '6.SP.B.5.c', [
              sa('Find the median of 8, 2, 6.', 'Median:', key='6', note='Ordered 2, 6, 8.'),
              sa('Find the median of 3, 9, 5, 7.', 'Median:', key='6', note='Ordered 3, 5, 7, 9; (5 + 7)/2.'),
              tf('The median of 1, 2, 3, 100 is 2.5.', key=True, note='(2 + 3)/2.'),
              mc('What is the median of 10, 12, 12, 15, 30?', ['12', '15.8', '15', '30'],
                 note='Third value. 15.8 is the mean; 15 and 30 are other values.'),
              sa('Find the median of 4.5, 6, 5, 7.', 'Median:', key='5.5', note='Ordered 4.5, 5, 6, 7.'),
          ], align='exact',
            why=why('the student cannot find a median, especially for an even count.', 'skewed data are compared by medians.',
                    'finds medians of odd and even counts.')),
          B('Recognize skew and extreme values', '6.SP.A.2', [
              mc('Which data set is skewed to the right?', ['1, 2, 2, 3, 3, 3, 4, 15', '1, 2, 3, 4, 5, 6, 7', '5, 5, 5, 5, 5',
                                                            '1, 12, 13, 13, 14, 14, 14, 15'],
                 note='A long tail of high values (15). The second is symmetric, the third constant, the fourth skewed left.'),
              tf('A data set with a single value far below all the others is skewed to the left.', key=True,
                 note='The tail points toward the low value.'),
              mc('Which value is extreme in 20, 22, 21, 23, 22, 60?', ['60', '20', '23', 'none'], note='60 is far from the rest.'),
              tf('In 4, 5, 5, 6, 6, 6, 7, 7, 8 the values are spread evenly on both sides of 6, so the data are roughly symmetric.',
                 key=True, note='Mirror image around 6.'),
              mc('Incomes in a town include a few very large incomes. The distribution is most likely', [
                  'skewed to the right', 'skewed to the left', 'symmetric', 'uniform'],
                 note='A few large values make a long right tail.'),
          ], align='exact',
            why=why('the student does not notice skew or an extreme value.', 'shape decides which center to use.',
                    'identifies skew direction and extreme values in lists and descriptions.')),
      ],
      f1=B('Find a missing value from a target mean or median', 'HSS-ID.A.2', [
          sa('Four quiz scores are 80, 85, 90, 75. What fifth score makes the mean of all five scores 84?', 'Answer:', key='90',
             note='5 · 84 = 420; 420 - 330 = 90.'),
          sa('The values 3, 5, 8 and x have mean 7. Find x.', 'x =', key='12', note='4 · 7 = 28; 28 - 16 = 12.'),
          tf('In a data set of 7 values, replacing the largest value with a larger number can change the median.', key=False,
             note='The median is the 4th value, which does not change.'),
          mc('The values 4, 6, 9, 10, 12 and one more value x have a median of 8. What is x?', ['7', '8', '16', '6'],
             note='With x = 7: 4, 6, 7, 9, 10, 12 has median (7 + 9)/2 = 8. x = 8 gives 8.5, x = 16 gives 9.5, x = 6 gives 7.5.'),
          sa('A team\'s mean score over 9 games is 70. What score in a 10th game makes the mean of all 10 games 72?', 'Answer:',
             key='90', note='720 - 630.'),
      ], prog='same-course deepening', demand='Work backward from a target center to a missing value.'),
      f2=B('Predict how changes in data move the mean and median', 'HSS-ID.A.3', [
          mc('The values are 10, 12, 13, 15, 40. If 40 is replaced by 20, what happens?', [
              'The mean decreases by 4 and the median stays 13.', 'The mean and the median both decrease by 4.',
              'The mean stays the same and the median decreases.', 'The mean decreases by 20 and the median stays 13.'],
             note='The sum drops by 20, so the mean drops by 20/5 = 4; the middle value 13 is unchanged.'),
          tf('Adding 5 to every value in a data set increases both the mean and the median by 5.', key=True,
             note='Every value, and so every summary of center, moves up by 5.'),
          sa('Find the mean and the median of 2, 4, 6, 8, 100.', ['Mean:', 'Median:'], key='24; 6', note='Form required: both. 120/5 = 24.'),
          mc('Salaries at a company include a few very high salaries. Which statement is most likely true?', [
              'The mean salary is greater than the median salary.', 'The median salary is greater than the mean salary.',
              'The mean and the median are equal.', 'The median is pulled up more than the mean.'],
             note='High values pull the mean up; the median resists them.'),
          tf('Doubling every value in a data set doubles the median but leaves the mean unchanged.', key=False,
             note='Both double.'),
      ], prog='cross-standard extension', demand='Predict the effect of changes and extreme values on the two centers.',
        builds='Builds on FORWARD 1: the reverse reasoning about how one value controls the mean is used to predict the effect of '
               'changing values.')),

    # ------------------------------------------------------------------ 5. ID.A.2 compare spreads
    S('HSS-ID.A.2', 'Compare spreads with the IQR or the standard deviation', num=5,
      target='Compare the spreads of two data sets with the measure suited to their shapes (IQR with skew or outliers, standard '
             'deviation when roughly symmetric), computing that measure for each set',
      strand='core', covers=['ID2-spread'],
      main=[
          sa('Ages of 9 players on each of two teams: team A: %s; team B: %s. Give the interquartile range of each team.%s' % (
              dlist(TEAMA), dlist(TEAMB), QRULE), ['IQR of team A:', 'IQR of team B:'], key='%s; %s' % (nm(iqr(TEAMA)), nm(iqr(TEAMB))),
             note='Form required: both. A: Q1 = 15, Q3 = 18, IQR 3. B: Q1 = 15, Q3 = 21, IQR 6.'),
          sa('Bus delays (minutes) on 5 days: route 1: %s; route 2: %s. Both are symmetric. Give the standard deviation of each '
             'route, to the nearest tenth.%s%s' % (dlist(SD1), dlist(SD2), POP, TECH), ['Route 1:', 'Route 2:'],
             key='%s; %s' % (d1(sd_pop(SD1)), d1(sd_pop(SD2))),
             note='Form required: both, to the nearest tenth. Route 1: deviations -4, -2, 0, 2, 4; variance 40/5 = 8; √8 ≈ 2.83. '
                  'Route 2: deviations -1, 0, 0, 0, 1; variance 2/5 = 0.4; √0.4 ≈ 0.63.'),
          mc('Monthly rents (dollars) of 7 apartments in each of two buildings: A: %s; B: %s. Which comparison of spread is '
             'appropriate and correct?' % (dlist(RENTA), dlist(RENTB)), [
              'A has an outlier, so compare IQRs: B\'s IQR ($400) is twice A\'s ($200), so B\'s typical rents vary more.',
              'Compare ranges: A\'s range ($1,600) is greater than B\'s ($600), so A\'s typical rents vary more.',
              'Compare standard deviations: A\'s is greater, so A\'s typical rents vary more than B\'s.',
              'Compare IQRs: A\'s IQR ($400) is twice B\'s ($200), so A\'s typical rents vary more.'],
             note=QRULE[1:] + ' A: Q1 850, Q3 1050, IQR 200; B: Q1 800, Q3 1200, IQR 400. The range and standard deviation of A are '
                  'inflated by the outlier 2400; the last choice swaps the IQRs.'),
          sa('Lengths (cm) of 8 fish from each of two lakes: lake A: %s; lake B: %s. Lake B has outliers. Give the interquartile '
             'range of each lake.%s' % (dlist(FISHA), dlist(FISHB), QRULE), ['IQR of lake A:', 'IQR of lake B:'],
             key='%s; %s' % (nm(iqr(FISHA)), nm(iqr(FISHB))),
             note='Form required: both. A: Q1 = 22.5, Q3 = 29, IQR 6.5. B: Q1 = 24, Q3 = 26, IQR 2.'),
          sa('Weekly savings (dollars) of 5 students in each of two groups: group 1: %s; group 2: %s. Both are symmetric. Give the '
             'standard deviation of each group, to the nearest tenth.%s%s' % (dlist(SD3), dlist(SD4), POP, TECH),
             ['Group 1:', 'Group 2:'], key='%s; %s' % (d1(sd_pop(SD3)), d1(sd_pop(SD4))),
             note='Form required: both, to the nearest tenth. Group 1: variance (400 + 100 + 0 + 100 + 400)/5 = 200; √200 ≈ 14.14. '
                  'Group 2: deviations -5, -2, 0, 2, 5; variance 58/5 = 11.6; √11.6 ≈ 3.41.'),
      ],
      back=[
          B('Find the range and the interquartile range', '6.SP.B.5.c', [
              sa('Find the range of 7, 3, 12, 5, 9.', 'Range:', key='9', note='12 - 3.'),
              sa('Q1 = 18 and Q3 = 27. Find the IQR.', 'IQR:', key='9', note='27 - 18.'),
              tf('The IQR is the spread of the middle half of the data.', key=True, note='From Q1 to Q3.'),
              mc('For 2, 4, 6, 8, 10, 12, the IQR (with Q1 and Q3 the medians of the halves) is', ['6', '10', '4', '8'],
                 note='Q1 = 4, Q3 = 10. 10 is the range.'),
              sa('A box plot has minimum 5, Q1 9, median 12, Q3 16, maximum 25. Give the IQR and the range.', ['IQR:', 'Range:'],
                 key='7; 20', note='Form required: both.'),
          ], align='exact',
            why=why('the student confuses the range and the IQR.', 'spread is compared with the IQR when there are outliers.',
                    'finds ranges and IQRs from lists and five-number summaries.')),
          B('Measure distances from the mean', '6.SP.B.5.c', [
              sa('The mean of 2, 6, 10 is 6. What are the distances of the values from the mean?', ['Distance of 2:', 'Distance of 10:'],
                 key='4; 4', note='Form required: both.'),
              sa('Find the mean absolute deviation of 1, 3, 5, 7.', 'MAD:', key='2', note='Mean 4; distances 3, 1, 1, 3; mean 2.'),
              tf('A data set whose values are all far from the mean has a large spread.', key=True, note='Spread measures distance from center.'),
              mc('Which set has the larger spread around its mean?', ['0, 10, 20', '9, 10, 11', 'they are the same', 'cannot tell'],
                 note='Distances 10, 0, 10 versus 1, 0, 1.'),
              sa('The values 5, 5, 5, 5 have mean 5. What is their mean absolute deviation?', 'MAD:', key='0', note='Every distance is 0.'),
          ], align='exact',
            why=why('the student does not see spread as distance from the center.', 'the standard deviation averages squared '
                    'distances from the mean.', 'computes distances from the mean and the MAD.')),
          B('Square, average, and take square roots', '8.EE.A.2', [
              sa('Find √16 + √9.', 'Answer:', key='7', note='4 + 3.'),
              sa('The squared distances from a mean are 4, 0, 4. Find their average.', 'Average:', key='8/3', note='8/3 (about 2.67).'),
              tf('√(9 + 16) = √9 + √16.', key=False, note='√25 = 5, but 3 + 4 = 7.'),
              mc('Which is √0.25?', ['0.5', '0.05', '0.125', '0.0625'], note='0.5² = 0.25.'),
              sa('Find √8 to the nearest tenth. A calculator may be used.', 'Answer:', key='2.8', note='2.828....'),
          ], align='supporting',
            why=why('the student mishandles squares and square roots.', 'the standard deviation is the square root of an average of '
                    'squares.', 'squares, averages and takes square roots, including decimals.')),
      ],
      f1=B('Compare population and sample standard deviations', 'HSS-ID.A.2', [
          sa('For the data 4, 6, 8, 10, 12, give the sample standard deviation (divide by n - 1), to the nearest hundredth.' + TECH,
             's =', key='3.16', note='Sum of squared deviations 40; 40/4 = 10; √10 ≈ 3.162.'),
          tf('For the same data, the sample standard deviation (divide by n - 1) is never smaller than the population standard '
             'deviation (divide by n).', key=True, note='Dividing by the smaller number n - 1 gives a larger or equal value.'),
          sa('For 2, 4, 6, give the population and the sample standard deviations, to the nearest hundredth.' + TECH, ['Population:', 'Sample:'],
             key='1.63; 2', note='Form required: both. Squared deviations 4, 0, 4: √(8/3) ≈ 1.633 and √(8/2) = 2.'),
          mc('A spreadsheet gives 5.2 for STDEV.S and 4.9 for STDEV.P of the same data. Which statement is correct?', [
              'STDEV.S divides by n - 1 and treats the data as a sample; STDEV.P divides by n and treats them as the population.',
              'STDEV.S divides by n and treats the data as the whole population; STDEV.P divides by n - 1 for a sample.',
              'The two functions measure different spreads: STDEV.S the range of the data and STDEV.P their IQR.',
              'One of the two values must be an error, because a data set has only one standard deviation.'],
             note='The sample formula divides by n - 1, so it is the larger value. The others swap the formulas or deny the difference.'),
          sa('Ten values have sum of squared deviations from their mean equal to 90. Give the population and sample variances.',
             ['Population variance:', 'Sample variance:'], key='9; 10', note='Form required: both. 90/10 and 90/9.'),
      ], prog='same-course deepening', demand='Distinguish the population and sample formulas and their purposes.'),
      f2=B('Predict how adding or multiplying changes center and spread', 'HSS-ID.A.2', [
          mc('Every value in a data set is increased by 10. What happens to the standard deviation and the IQR?', [
              'Both stay the same.', 'Both increase by 10.', 'Both are multiplied by 10.', 'The SD stays the same and the IQR increases by 10.'],
             note='Shifting every value keeps every distance the same.'),
          sa('A data set has mean 20 and standard deviation 4. Every value is multiplied by 3. Give the new mean and standard deviation.',
             ['Mean:', 'Standard deviation:'], key='60; 12', note='Form required: both. Both are multiplied by 3.'),
          tf('Converting temperatures from degrees to tenths of a degree (multiplying by 10) multiplies the IQR by 10.', key=True,
             note='Q1 and Q3 are both multiplied by 10.'),
          sa('A data set has median 50 and IQR 8. Each value is changed to 2·value + 5. Give the new median and IQR.',
             ['Median:', 'IQR:'], key='105; 16', note='Form required: both. 2·50 + 5; the + 5 does not change the IQR.'),
          mc('Test scores have SD 6. The teacher adds 3 bonus points to every score. The new SD is', ['6', '9', '18', '3'],
             note='Adding a constant does not change spread.'),
      ], prog='same-course deepening', demand='Predict summaries after a linear change of units without recomputing.',
        builds='Builds on FORWARD 1: with both standard deviation formulas understood, the student predicts how each responds to '
               'shifting and scaling the data.')),

    # ------------------------------------------------------------------ 6. ID.A.3 interpret in context
    S('HSS-ID.A.3', 'Interpret differences in shape, center and spread in context', num=6,
      target='Interpret the differences in shape, center and spread between two data sets in the terms of their context',
      strand='core', covers=['ID3-context'],
      main=[
          mc('The box plots show the battery lives (hours) of two brands. Which interpretation is correct?', [
              'Typical lives are the same (both medians 11 hours), but brand B\'s lives vary more (IQR 4 versus 2 hours).',
              'Brand B lasts longer, because its longest-lasting battery runs longer than brand A\'s does.',
              'Brand A\'s lives vary more, because its box is narrower than brand B\'s box is.',
              'Brand B is better in every way, because its whiskers and its box are both longer.'],
             fig=boxes2(['Brand A', 'Brand B'], [(8, 10, 11, 12, 14), (6, 9, 11, 13, 16)], 4, 18, 'Hours'),
             note='Same median; IQRs 2 and 4. The others use the maximum as the center, read a narrow box as more spread, or call '
                  'more spread better.'),
          mc('Waiting times at two stores: store 1 is roughly symmetric with mean 6 minutes and standard deviation 1.5 minutes; '
             'store 2 is skewed right with median 5 minutes, IQR 6 minutes, and a few waits over 20 minutes. Which interpretation '
             'is correct?', [
              'Store 2 often has a shorter wait, but its waits are much less predictable, with occasional very long waits.',
              'Store 2 always has shorter waits than store 1, because its median is 1 minute lower than the mean of store 1.',
              'Store 1\'s waits vary more, because its waits are described with a mean and a standard deviation.',
              'The stores cannot be compared at all, because they are summarized with different measures.'],
             note='Median 5 < mean 6 for a typical wait; IQR 6 and long waits show more variability. The others overstate, invert '
                  'the spread, or refuse a reasonable comparison.'),
          mc('The box plots show commute times (minutes) by bus and by bike for the same group of workers. Which interpretation is '
             'correct?', [
              'Bike trips are more consistent; bus trips take a little longer in the middle and vary much more, including long trips.',
              'Bus trips are shorter in general, because the bus box plot starts at a lower time than the bike box plot.',
              'Both ways take the same time, because both box plots contain the times from 25 to 28 minutes.',
              'Bike trips vary more, because the bike box plot is shorter than the bus box plot on the scale.'],
             fig=boxes2(['Bus', 'Bike'], [(15, 25, 30, 35, 60), (20, 24, 26, 28, 32)], 10, 65, 'Minutes', step=5),
             note='Medians 30 and 26; IQRs 10 and 4; the bus range is 45. The others use the minimum, overlap, or read a short box as '
                  'more spread.'),
          mc('Two classes both have mean score 70 on a test. Class X\'s scores form two clusters, around 55 and around 85; class Y\'s '
             'form one mound around 70. Which interpretation is correct?', [
              'The equal means hide a difference: class X seems to contain two groups doing very differently; class Y is more alike.',
              'The classes performed the same way, because their means are equal and the mean summarizes the whole class.',
              'Class X did better, because some of its students scored around 85, which is above every score in class Y.',
              'Class Y has more spread, because its scores are all close to the middle of the range of scores.'],
             note='A bimodal shape suggests two subgroups; the mean alone hides it. The others ignore shape or invert spread.'),
          mc('Apples from two farms both have mean weight 150 g; farm A\'s weights have standard deviation 5 g and farm B\'s have '
             'standard deviation 20 g. Both distributions are roughly symmetric. Which interpretation is correct?', [
              'Farm A\'s apples are more uniform in size; on average, apples from both farms weigh about the same.',
              'Farm B\'s apples are heavier, because a standard deviation of 20 g is larger than one of 5 g.',
              'Farm A\'s apples are lighter, because a smaller standard deviation means a smaller mean weight.',
              'The farms\' apples are the same in every way, because their mean weights are both 150 g.'],
             note='Same center, different spread. The others read spread as center or ignore spread.'),
      ],
      back=[
          B('Describe the shape of a distribution', '6.SP.A.2', [
              mc('A histogram has one peak in the middle and falls off evenly on both sides. Its shape is', [
                  'symmetric', 'skewed right', 'skewed left', 'bimodal'], note='Mirror image about the center.'),
              tf('A histogram with two separate peaks is called bimodal.', key=True, note='Two modes.'),
              mc('A histogram has a long tail toward small values. Its shape is', ['skewed left', 'skewed right', 'symmetric', 'uniform'],
                 note='The tail names the direction.'),
              tf('A distribution whose bars are all about the same height is skewed right.', key=False, note='That is uniform.'),
              mc('Waiting times at a busy clinic are mostly short with a few very long waits. The shape is most likely', [
                  'skewed right', 'skewed left', 'symmetric', 'bimodal'], note='Long tail of large values.'),
          ], align='exact',
            why=why('the student cannot name the shape of a distribution.', 'shape differences must be described in context.',
                    'names symmetric, skewed and bimodal shapes from descriptions.')),
          B('What center and spread tell about data', '6.SP.A.3', [
              tf('A measure of center summarizes all the values of a data set with a single number.', key=True, note='Definition.'),
              tf('A measure of spread tells how much the values vary.', key=True, note='Definition.'),
              mc('Two data sets have the same median but different IQRs. Which is true?', [
                  'Their typical values are similar, but one varies more.', 'They are identical data sets with the same values.',
                  'One of them has a larger typical value than the other.', 'They have the same range and the same maximum.'], note='Center versus spread.'),
              mc('Which describes spread?', ['the IQR', 'the median', 'the mean', 'the mode'], note='The others are centers.'),
              tf('A data set with a larger mean must have a larger standard deviation.', key=False,
                 note='5, 5, 5 has mean 5 and SD 0; 1, 2, 3 has mean 2 and SD about 0.82.'),
          ], align='exact',
            why=why('the student confuses what center and spread describe.', 'interpretations must keep center and spread apart.',
                    'separates statements about center from statements about spread.')),
          B('Compare two distributions informally', '7.SP.B.4', [
              mc('Group 1 has median 12 and IQR 3; group 2 has median 15 and IQR 3. Which is true?', [
                  'Group 2\'s typical value is 3 higher, with similar spread.', 'Group 1\'s values are higher, since its IQR is the same.',
                  'Group 2 varies more, since its median is higher.', 'The groups are the same, since the IQRs are equal.'], note='Same IQR, higher median.'),
              tf('If two groups have very different medians and small IQRs, their distributions overlap very little.', key=True,
                 note='Small spread around far-apart centers.'),
              sa('Group A has mean 40 and group B has mean 46. By how much are the means different?', 'Answer:', key='6', note='46 - 40.'),
              mc('Which pair of groups overlaps the most?', [
                  'medians 20 and 21, both IQRs 10', 'medians 20 and 40, both IQRs 2', 'medians 20 and 30, both IQRs 1',
                  'medians 10 and 50, both IQRs 5'], note='Centers 1 apart relative to spreads of 10.'),
              tf('Two groups with the same center must have the same spread.', key=False, note='Spread is separate from center.'),
          ], align='exact',
            why=why('the student cannot compare two distributions at all.', 'interpretation in context starts from a comparison.',
                    'compares two groups by their centers and spreads.')),
      ],
      f1=B('Measure separation in units of spread', 'HSS-ID.A.3', [
          sa('Two roughly symmetric groups have means 70 and 76; both have standard deviation 4. How many standard deviations apart '
             'are the means?', 'Answer:', key='1.5', note='6/4.'),
          sa('Group medians are 30 and 45; both IQRs are 10. How many IQRs apart are the medians?', 'Answer:', key='1.5', note='15/10.'),
          mc('Pair 1: means 50 and 55, both SDs 10. Pair 2: means 50 and 53, both SDs 1. Which pair is more clearly separated?', [
              'pair 2, 3 SDs apart', 'pair 1, 5 points apart', 'pair 1, 0.5 SDs apart', 'they are equally separated'],
             note='Pair 1 is 0.5 SDs apart, pair 2 is 3 SDs apart. A larger raw gap is not the larger separation.'),
          tf('Two groups whose means are 0.2 standard deviations apart overlap a great deal.', key=True, note='Small separation relative to spread.'),
          mc('Why measure a difference in units of spread?', [
              'A gap matters only relative to how much values vary within each group.',
              'Units of spread make every difference look larger than it really is.',
              'Units of spread remove the need to compare the centers of the groups.',
              'Units of spread show which group has more values in it.'],
             note='The others are false claims about standardizing.'),
      ], prog='same-course deepening', demand='Quantify how far apart two groups are relative to their spread.'),
      f2=B('Judge whether a difference supports a claim', 'HSS-IC.B.6', [
          mc('A report says that brand X bulbs "last much longer" than brand Y: means 1,010 and 1,000 hours, both with standard '
             'deviation 80 hours. Evaluate.', [
              'Weak: the means differ by about 0.13 standard deviations, so the lives overlap almost completely.',
              'Strong: 1,010 is greater than 1,000, so every brand X bulb lasts longer than any brand Y bulb.',
              'Strong: both brands have the same standard deviation, so the difference in means must be large.',
              'Weak: the claim would be supported only if the standard deviations were different.'],
             note='10/80 = 0.125. The others overstate or misuse the spread.'),
          tf('A difference of 5 points between group means is more convincing when each group\'s standard deviation is 2 than when '
             'it is 20.', key=True, note='2.5 SDs versus 0.25 SDs.'),
          mc('A coach claims the new training "improved race times a lot": median time dropped from 52 to 50 seconds; IQRs 8 seconds. Which '
             'evaluation is best?', [
              'The drop is small relative to the spread (a quarter of an IQR), so "a lot" overstates it.',
              'The drop is large, because two seconds is a long time in a race of 52 seconds.',
              'The claim is wrong, because a drop in the median time means the athletes slowed down.',
              'The claim cannot be judged, because the IQRs of the two groups are equal.'],
             note='2/8 = 0.25 IQR. Lower times are faster, so the third choice is wrong too.'),
          sa('Two groups have means 120 and 135 and the same standard deviation 10. How many standard deviations apart are they?',
             'Answer:', key='1.5', note='15/10.'),
          tf('If two groups\' means differ by less than one standard deviation, the groups cannot differ in any important way.',
             key=False, note='A small standardized difference can still matter in context.'),
      ], prog='cross-standard extension', demand='Use a standardized difference to evaluate a claim in a report.',
        builds='Builds on FORWARD 1: the separation measured in units of spread becomes evidence for or against a reported claim.')),

    # ------------------------------------------------------------------ 7. ID.A.3 outliers
    S('HSS-ID.A.3', 'Identify outliers and account for their effects', num=7,
      target='Identify outliers with the 1.5·IQR rule and determine their effect on the mean, median and spread',
      strand='core', covers=['ID3-outlier'],
      main=[
          sa('Points a player scored in 11 games: %s.%s%s Give the lower fence, the upper fence, and the number of outliers.' % (
              dlist(GAMES), QRULE, OUTRULE), ['Lower fence:', 'Upper fence:', 'Number of outliers:'],
             key='%s; %s; 1' % (nm(fences(GAMES)[0]), nm(fences(GAMES)[1])),
             note='Form required: all three. Ordered 12, 13, 14, 14, 15, 15, 16, 16, 17, 18, 41; Q1 = 14, Q3 = 17, IQR 3; fences '
                  '14 - 4.5 = 9.5 and 17 + 4.5 = 21.5; only 41 is an outlier.'),
          sa('Points a player scored in 11 games: %s. The value 41 is an outlier. Find the mean with and without it, each to the '
             'nearest tenth.' % dlist(GAMES), ['Mean with 41:', 'Mean without 41:'],
             key='%s; %s' % (d1(float(mean(GAMES))), d1(float(mean([g for g in GAMES if g != 41])))),
             note='Form required: both. 191/11 ≈ 17.36; 150/10 = 15.0. (The median is 15 both ways.)'),
          sa('Hours of screen time 11 students reported for one weekend: %s.%s%s Give the lower fence, the upper fence, and the '
             'number of outliers.' % (dlist(HOURS), QRULE, OUTRULE), ['Lower fence:', 'Upper fence:', 'Number of outliers:'],
             key='%s; %s; 2' % (nm(fences(HOURS)[0]), nm(fences(HOURS)[1])),
             note='Form required: all three. Ordered 1, 6, 6, 7, 7, 7, 8, 8, 8, 9, 30; Q1 = 6, Q3 = 8, IQR 2; fences 3 and 11; '
                  '1 and 30 are outliers.'),
          mc('Prices (dollars) of 10 used bikes: %s. The $600 bike is an outlier. Which describes the effect of removing it?' % dlist(PRICES), [
              'The mean drops by $40, while the median drops by only $2.50.', 'The median drops by $40, while the mean drops by only $2.50.',
              'The mean and the median both drop by $40.', 'Neither the mean nor the median changes.'],
             note='Mean 2400/10 = 240 becomes 1800/9 = 200; median (200 + 205)/2 = 202.5 becomes 200.'),
          sa('Support calls received in each of 10 hours: %s.%s%s Give the upper fence and the number of outliers.' % (
              dlist(CALLS), QRULE, OUTRULE), ['Upper fence:', 'Number of outliers:'], key='%s; 1' % nm(fences(CALLS)[1]),
             note='Form required: both. Ordered 3, 3, 4, 4, 4, 5, 5, 5, 6, 22; Q1 = 4, Q3 = 5, IQR 1; fences 2.5 and 6.5; only 22.'),
      ],
      back=[
          B('Find the interquartile range', '6.SP.B.5.c', [
              sa('Q1 = 12 and Q3 = 20. Find the IQR.', 'IQR:', key='8', note='20 - 12.'),
              sa('For 1, 3, 4, 6, 8, 9, find the IQR (Q1 and Q3 are the medians of the halves).', 'IQR:', key='5', note='Q1 = 3, Q3 = 8.'),
              tf('The IQR is the difference between the maximum and the minimum.', key=False, note='That is the range.'),
              mc('A box plot has Q1 = 30 and Q3 = 42. The IQR is', ['12', '36', '72', '42'], note='42 - 30.'),
              sa('For 2, 4, 5, 7, 9, 10, 12 (odd count; leave out the median), find the IQR.', 'IQR:', key='6', note='Q1 = 4, Q3 = 10.'),
          ], align='exact',
            why=why('the student cannot find the IQR the fences use.', 'the outlier rule is built on the IQR.', 'finds IQRs from '
                    'quartiles and from data.')),
          B('Compute the fences', '6.NS.B.3', [
              sa('Find 1.5 × 6.', 'Answer:', key='9', note='6 + 3.'),
              sa('Find 1.5 × 2.5.', 'Answer:', key='3.75', note='2.5 + 1.25.'),
              tf('If Q1 = 10 and the IQR is 4, the lower fence is 10 - 6 = 4.', key=True, note='1.5 · 4 = 6.'),
              mc('If Q3 = 25 and the IQR is 10, the upper fence is', ['40', '35', '15', '37.5'], note='25 + 15.'),
              sa('Q1 = 7.5 and the IQR is 3. Find the lower fence.', 'Answer:', key='3', note='7.5 - 4.5.'),
          ], align='supporting',
            why=why('the student miscalculates 1.5·IQR or adds it on the wrong side.', 'fences decide which values are outliers.',
                    'computes 1.5·IQR and both fences with decimals.')),
          B('How an extreme value affects the mean and the median', '6.SP.B.5.d', [
              mc('In 3, 4, 5, 6, 50, which is pulled more by the value 50?', ['the mean', 'the median', 'neither', 'both equally'],
                 note='Mean 13.6; median 5.'),
              tf('The median of 2, 3, 4, 5, 100 is 4.', key=True, note='Middle value.'),
              sa('Find the mean of 2, 3, 4, 5, 100.', 'Mean:', key='22.8', note='114/5.'),
              tf('Removing an extreme value always changes the median more than the mean.', key=False, note='Usually the reverse.'),
              mc('For skewed data with outliers, the better summary of a typical value is usually', [
                  'the median', 'the mean', 'the maximum', 'the range'], note='Resistant to extremes.'),
          ], align='exact',
            why=why('the student does not see how one extreme value moves the mean.', 'accounting for outliers means knowing which '
                    'summaries they affect.', 'compares the effect of an extreme value on the mean and the median.')),
      ],
      f1=B('Decide whether an outlier is an error or a real value', 'HSS-ID.A.3', [
          mc('Heights of 9 adults in a study are listed in centimeters; one value is 17.5. Which is the most reasonable judgment?', [
              'It is probably a recording error (likely 175 cm), so check the record before using it.',
              'It is an outlier, so it should be deleted without any further checking.',
              'It is a real height, so it must be kept exactly as it is in the data.',
              'Outliers are always errors, so every outlier in the data should be removed.'],
             note='An adult height of 17.5 cm is impossible; an outlier is checked, not removed automatically.'),
          tf('A value that the 1.5·IQR rule flags as an outlier must be removed from the data.', key=False,
             note='The rule flags values to examine; a legitimate unusual value stays.'),
          mc('Among 30 home prices, one mansion sells for 10 times the median. Which is correct?', [
              'It is a legitimate unusual value; report resistant summaries such as the median and the IQR.',
              'It is a recording error, because no real home could cost ten times the median price.',
              'It must be removed, because the outlier rule requires it to be deleted.',
              'It should replace the median, because it is the most informative value in the data.'],
             note='Real but extreme values are kept; resistant summaries describe the typical home.'),
          tf('An outlier can be a correct measurement of an unusual case.', key=True, note='Outliers are not automatically errors.'),
          mc('A thermometer log shows 18, 19, 21, 20, 210, 19 °C in a classroom. What is the best next step?', [
              'Check the 210 reading, since a decimal point was likely lost (21.0), before computing summaries.',
              'Report the mean including 210, because every reading is data and must be used as recorded.',
              'Delete the 19s, because they are the most common values and do not add information.',
              'Report the 210 reading as the median, because it is the most unusual value in the list.'],
             note='210 °C in a classroom is impossible; check it.'),
      ], prog='same-course deepening', demand='Judge from context whether a flagged value is a likely error or a legitimate unusual value.'),
      f2=B('Report resistant summaries after checking outliers', 'HSS-ID.A.3', [
          mc('After checking, the $600 bike price is real. Which summaries best describe a typical used bike and the spread?', [
              'the median and the IQR', 'the mean and the standard deviation', 'the mean and the range', 'the maximum and the minimum'],
             note='Resistant to the outlier.'),
          sa('After a recording error is corrected, the data are 12, 15, 14, 18, 16, 13, 17, 15, 14, 14, 16 (the 41 was really 14). '
             'Find the new mean to the nearest tenth and the new median.', ['Mean:', 'Median:'],
             key='%s; %s' % (d1(float(mean([12, 15, 14, 18, 16, 13, 17, 15, 14, 14, 16]))), nm(median([12, 15, 14, 18, 16, 13, 17, 15, 14, 14, 16]))),
             note='Form required: both. Sum 164/11 ≈ 14.9; ordered middle value 15.'),
          tf('The IQR barely changes when a single extreme value is removed from a large data set.', key=True,
             note='Quartiles depend on the middle of the data.'),
          mc('Which summary is most changed by one extreme value?', ['the standard deviation', 'the IQR', 'the median', 'Q1'],
             note='Squared distances make the SD very sensitive.'),
          sa('Data 5, 6, 6, 7, 8, 30: find the median and the IQR (Q1 and Q3 are the medians of the halves).', ['Median:', 'IQR:'],
             key='6.5; 2', note='Form required: both. Q1 = 6, Q3 = 8.'),
      ], prog='same-course deepening', demand='Choose and compute summaries that resist outliers once their status is known.',
        builds='Builds on FORWARD 1: once a flagged value is judged real or an error, the student reports the summaries that fit.')),
]
