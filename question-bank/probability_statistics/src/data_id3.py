"""S-ID.A.4, S-ID.B.5, S-ID.B.6, S-ID.B.6.a: normal models, two-way tables, scatter plots, fitted functions (sets 8-14)."""
from fractions import Fraction as Fr

from qb import S, B, sa, mc, tf
from common import (why, n, phi, dlist, ztable, scatter, tbl, cand, pick, pickfig, QRULE, TECH)
from datasets import D
from data_id1 import histf, boxf

ER = ' Use the 68-95-99.7 rule.'
TBL = ' Use the table values printed below (areas to the left of z).'


def t4(z):
    return round(phi(z), 4)


def between(z1, z2):
    return '%.4f' % (t4(z2) - t4(z1))


def right(z):
    return '%.4f' % (1 - t4(z))


def two_way(rows, cols, cells, title=None):
    """Two-way frequency table with row and column totals."""
    header = [''] + cols + ['Total']
    body = [[r] + [str(c) for c in row] + [str(sum(row))] for r, row in zip(rows, cells)]
    body.append(['Total'] + [str(sum(col)) for col in zip(*cells)] + [str(sum(map(sum, cells)))])
    return tbl(header, body)


# ------------------------------------------------------------------ datasets
SA = D('S13 study', [(1, 52), (2, 58), (2, 61), (3, 63), (4, 70), (5, 72), (5, 76), (6, 80), (7, 83), (8, 90)], '(hours, points)',
       'Hours studied and test score of 10 students')
SB = D('S13 cars', [(1, 24), (2, 21), (3, 22), (4, 17), (5, 18), (6, 13), (7, 14), (8, 9), (9, 11), (10, 6)],
       '(years, thousand dollars)', 'Age and resale value of 10 cars of one model')
SC = D('S13 fuel', [(20, 22), (30, 28), (40, 32), (50, 34), (60, 33), (70, 30), (80, 25)], '(mph, miles per gallon)',
       'Speed and fuel efficiency of one car in 7 test runs')
SD = D('S13 shoes', [(6, 72), (7, 85), (8, 64), (9, 90), (10, 70), (11, 81), (12, 68), (8, 77), (10, 88), (7, 66)],
       '(shoe size, points)', 'Shoe size and quiz score of 10 adults')
SE = D('S13 ice cream', [(60, 120), (65, 140), (70, 155), (75, 175), (80, 190), (85, 210), (90, 60)], '(degrees F, cones)',
       'High temperature and cones sold on 7 days (the 90-degree day had a power outage)')


def sc(pts, x, y, xl, yl, xs=1, ys=1, desc=''):
    return scatter(pts, x, y, desc or ('Scatter plot of %d points: ' % len(pts) + ', '.join('(%s, %s)' % p for p in pts) + '.'),
                   xlabel=xl, ylabel=yl, xstep=xs, ystep=ys)


FIG_A = sc(SA, (0, 9), (40, 100), 'Hours studied', 'Score', 1, 10)
FIG_B = sc(SB, (0, 11), (0, 26), 'Age (years)', 'Value ($1000s)', 1, 2)
FIG_C = sc(SC, (10, 90), (15, 40), 'Speed (mph)', 'Miles per gallon', 10, 5)
FIG_D = sc(SD, (5, 13), (55, 95), 'Shoe size', 'Score', 1, 5)
FIG_E = sc(SE, (55, 95), (0, 240), 'Temperature (°F)', 'Cones sold', 5, 20)

ONLINE = [[30, 50], [45, 35]]          # rows: 9th, 10th; columns: online, in person
CARS = [[18, 12, 10], [22, 8, 30]]     # rows: lot A, lot B; columns: white, red, gray
PETS = [[36, 24], [15, 45]]            # rows: has a dog, no dog; columns: walks daily, does not

SETS = [
    # ------------------------------------------------------------------ 8. ID.A.4 68-95-99.7 rule
    S('HSS-ID.A.4', 'Estimate percentages with the 68-95-99.7 rule', num=8,
      target='Estimate the percent of a normally distributed population in an interval bounded by whole numbers of standard '
             'deviations from the mean, with the 68-95-99.7 rule',
      strand='core', covers=['ID4-rule'],
      main=[
          sa('Heights of adult women in a population are approximately normal with mean 64 inches and standard deviation 2.5 '
             'inches.%s What percent are between 61.5 and 66.5 inches, and what percent are between 59 and 69 inches?' % ER,
             ['61.5 to 66.5:', '59 to 69:'], key='68%; 95%', note='Form required: both, as percents. ±1 SD and ±2 SD.'),
          sa('Battery lives are approximately normal with mean 40 hours and standard deviation 4 hours.%s What percent of batteries '
             'last more than 48 hours?' % ER, 'Answer:', key='2.5%', note='48 is 2 SD above; (100 - 95)/2 = 2.5.'),
          sa('Commute times are approximately normal with mean 30 minutes and standard deviation 5 minutes.%s What percent are '
             'between 25 and 40 minutes?' % ER, 'Answer:', key='81.5%', note='25 to 30 is 34%; 30 to 40 is 47.5%.'),
          sa('Egg masses are approximately normal with mean 58 g and standard deviation 3 g.%s What percent are less than 52 g, and '
             'what percent are more than 61 g?' % ER, ['Less than 52 g:', 'More than 61 g:'], key='2.5%; 16%',
             note='Form required: both. 52 is 2 SD below: 2.5%. 61 is 1 SD above: (100 - 68)/2 = 16%.'),
          sa('Scores on a test are approximately normal with mean 500 and standard deviation 100.%s What percent are between 300 '
             'and 600, and what percent are below 400?' % ER, ['300 to 600:', 'Below 400:'], key='81.5%; 16%',
             note='Form required: both. 47.5% + 34% = 81.5%; 400 is 1 SD below: 16%.'),
      ],
      back=[
          B('Count standard deviations from the mean', 'HSS-ID.A.2', [
              sa('The mean is 50 and the standard deviation is 5. How many standard deviations above the mean is 60?', 'Answer:',
                 key='2', note='(60 - 50)/5.'),
              sa('The mean is 12 and the standard deviation is 3. How many standard deviations below the mean is 9?', 'Answer:',
                 key='1', note='(12 - 9)/3.'),
              tf('With mean 100 and standard deviation 15, the value 70 is 2 standard deviations below the mean.', key=True,
                 note='100 - 2·15 = 70.'),
              mc('With mean 64 and standard deviation 2.5, which value is 1 standard deviation above the mean?', [
                  '66.5', '65', '62.5', '67'], note='64 + 2.5.'),
              sa('The mean is 30 and the standard deviation is 5. What value is 2 standard deviations below the mean?', 'Answer:',
                 key='20', note='30 - 10.'),
          ], align='supporting',
            why=why('the student cannot convert a value to a number of standard deviations from the mean.', 'the rule is stated in '
                    'whole numbers of standard deviations.', 'converts between values and distances in standard deviations.')),
          B('Find a percent of a population', '6.RP.A.3.c', [
              sa('What is 68% of 500?', 'Answer:', key='340', note='0.68 · 500.'),
              sa('Half of 5% is what percent?', 'Answer:', key='2.5%', note='5/2.'),
              tf('34% + 13.5% = 47.5%.', key=True, note='Addition.'),
              mc('If 95% of values are inside an interval, what percent are outside it?', ['5%', '95%', '2.5%', '0%'],
                 note='100 - 95; 2.5% is one side only.'),
              sa('What is 100% minus 68%, divided by 2?', 'Answer:', key='16%', note='32/2.'),
          ], align='supporting',
            why=why('the student mishandles the percent arithmetic of tails.', 'tail and between percents are built from 68, 95 '
                    'and 99.7.', 'adds, subtracts and halves percents.')),
          B('Use the symmetry of the normal curve', '6.SP.A.2', [
              tf('In a normal distribution, half of the values are above the mean.', key=True, note='Symmetric about the mean.'),
              tf('In a normal distribution, more values are between the mean and 1 SD above it than between the mean and 1 SD below it.',
                 key=False, note='Symmetry makes them equal (34% each).'),
              mc('What percent of a normal distribution lies between the mean and 2 standard deviations above it?', [
                  '47.5%', '95%', '34%', '50%'], note='Half of 95%.'),
              sa('What percent of a normal distribution lies between 1 SD below the mean and the mean?', 'Answer:', key='34%',
                 note='Half of 68%.'),
              mc('What percent of a normal distribution is more than 1 standard deviation below the mean?', [
                  '16%', '32%', '34%', '2.5%'], note='(100 - 68)/2.'),
          ], align='supporting',
            why=why('the student does not use the symmetry of the normal curve to split percents.', 'one-sided and between-'
                    'percents come from halving.', 'splits the rule\'s percents with symmetry.')),
      ],
      f1=B('Find a cutoff from a percent', 'HSS-ID.A.4', [
          sa('Heights are approximately normal with mean 64 in and standard deviation 2.5 in.%s Above what height are the tallest '
             '2.5%%?' % ER, 'Height (in):', key='69', note='Mean + 2 SD.'),
          sa('Times are approximately normal with mean 30 min and standard deviation 5 min.%s Below what time are the fastest 16%%?' % ER,
             'Time (min):', key='25', note='Mean - 1 SD.'),
          tf('In a normal distribution with mean 200 and standard deviation 20, the middle 95% is from 160 to 240.', key=True,
             note='±2 SD.'),
          mc('Test scores are approximately normal with mean 70 and SD 8. Which score separates the top 16%?', ['78', '86', '62', '74'],
             note='Mean + 1 SD. 86 marks the top 2.5%; 62 the bottom 16%.'),
          sa('Lengths are approximately normal with mean 12 cm and standard deviation 0.5 cm.%s Give the interval that holds the '
             'middle 68%%.' % ER, ['From:', 'To:'], key='11.5; 12.5', note='Form required: both.'),
      ], prog='same-course deepening', demand='Reverse the rule: find the cutoff for a given percent.'),
      f2=B('Compare positions in two populations with standardized values', 'HSS-ID.A.4', [
          sa('Ana scored 85 on a test with mean 75 and SD 5; Ben scored 90 on a test with mean 80 and SD 10. How many standard '
             'deviations above the mean is each score?', ['Ana:', 'Ben:'], key='2; 1', note='Form required: both. 10/5 and 10/10.'),
          mc('Using the scores above (Ana 2 SDs above, Ben 1 SD above, both tests normal), which is correct?', [
              'Ana\'s score is relatively higher: about 2.5% scored above her, but about 16% scored above Ben.',
              'Ben\'s score is relatively higher, because 90 is a larger number than 85.',
              'The scores are equally good, because both are 10 points above their means.',
              'They cannot be compared, because the two tests had different means.'],
             note='Standardized position decides. The others compare raw scores or raw gaps.'),
          tf('A value 1 SD below the mean in one normal population and a value 1 SD below the mean in another are at the same '
             'percentile.', key=True, note='Both have about 16% below them.'),
          sa('A 100-m time of 12.0 s comes from a population with mean 13.0 s and SD 0.5 s. How many standard deviations below the '
             'mean is it?', 'Answer:', key='2', note='(13.0 - 12.0)/0.5.'),
          mc('Two normal populations: in A, mean 50, SD 5; in B, mean 50, SD 10. Which value is more unusual?', [
              '60 in population A', '60 in population B', 'they are equally unusual', '55 in population B'],
             note='60 is 2 SD above in A, 1 SD in B; 55 is 0.5 SD in B.'),
      ], prog='same-course deepening', demand='Compare values from different normal populations by standardizing.',
        builds='Builds on FORWARD 1: cutoffs found in units of standard deviation become a common scale for comparing populations.')),

    # ------------------------------------------------------------------ 9. ID.A.4 areas with a table
    S('HSS-ID.A.4', 'Estimate normal areas with a table or calculator', num=9,
      target='Estimate the proportion of a normal population in an interval by standardizing and using a normal table (or a '
             'calculator), including left tails, right tails and areas between two values',
      strand='core', covers=['ID4-area'],
      main=[
          sa('IQ scores are approximately normal with mean 100 and standard deviation 15. What proportion of people score below '
             '118?%s Give four decimal places.' % TBL, 'Proportion:', key='%.4f' % t4(1.2), fig=ztable([1.0, 1.2, 1.5, 2.0]),
             note='z = (118 - 100)/15 = 1.2; area to the left 0.8849.'),
          sa('Lengths of calls are approximately normal with mean 50 seconds and standard deviation 8 seconds. What proportion of '
             'calls last more than 60 seconds?%s Give four decimal places.' % TBL, 'Proportion:', key=right(1.25),
             fig=ztable([1.0, 1.25, 1.5, 2.0]), note='z = 10/8 = 1.25; 1 - 0.8944 = 0.1056.'),
          sa('Daily water use is approximately normal with mean 20 gallons and standard deviation 2.5 gallons. What proportion of '
             'days use between 18 and 23 gallons?%s Give four decimal places.' % TBL, 'Proportion:', key=between(-0.8, 1.2),
             fig=ztable([-1.0, -0.8, 0.8, 1.2]), note='z = -0.8 and 1.2; 0.8849 - 0.2119 = 0.6730.'),
          sa('Grade-point averages at a school are approximately normal with mean 3.0 and standard deviation 0.4. What proportion '
             'are below 2.5?%s Give four decimal places.' % TBL, 'Proportion:', key='%.4f' % t4(-1.25),
             fig=ztable([-1.5, -1.25, -1.0, -0.5]), note='z = -0.5/0.4 = -1.25; area 0.1056.'),
          sa('Heights of adult men are approximately normal with mean 175 cm and standard deviation 7 cm. What proportion are '
             'between 168 and 189 cm?%s Give four decimal places.' % TBL, 'Proportion:', key=between(-1, 2),
             fig=ztable([-2.0, -1.0, 1.0, 2.0]), note='z = -1 and 2; 0.9772 - 0.1587 = 0.8185.'),
      ],
      back=[
          B('Compute a standardized value', '7.NS.A.3', [
              sa('Compute (130 - 100)/15.', 'Answer:', key='2', note='30/15.'),
              sa('Compute (42 - 50)/4.', 'Answer:', key='-2', note='-8/4.'),
              tf('(9.5 - 10)/0.5 = -1.', key=True, note='-0.5/0.5.'),
              mc('Compute (61 - 58)/2.', ['1.5', '-1.5', '3', '0.67'], note='3/2.'),
              sa('Compute (2.2 - 3.0)/0.4.', 'Answer:', key='-2', note='-0.8/0.4.'),
          ], align='supporting',
            why=why('the student cannot compute (x - mean)/SD, especially with negative or decimal results.', 'every table lookup '
                    'starts from this value.', 'computes standardized values with signs and decimals.')),
          B('Read areas as proportions', '7.SP.C.5', [
              tf('An area of 0.8413 to the left of z = 1 means about 84% of the population is below 1 SD above the mean.', key=True,
                 note='Area is proportion.'),
              mc('The table gives area 0.0228 to the left of z = -2. What does this mean?', [
                  'About 2.28% of values are below 2 SDs below the mean.', 'About 2.28% of values are above the mean.',
                  'Exactly 2 values are below the mean.', 'About 22.8% of values are below the mean.'], note='Read as a proportion.'),
              sa('Write 0.1587 as a percent.', 'Answer:', key='15.87%', note='× 100.'),
              tf('A proportion of a population can be greater than 1.', key=False, note='Proportions are between 0 and 1.'),
              mc('Which is the largest proportion?', ['0.9772', '0.8413', '0.5', '0.0228'], note='Compare decimals.'),
          ], align='supporting',
            why=why('the student does not read a table area as a proportion of the population.', 'the answer is that proportion.',
                    'interprets table areas as proportions and percents.')),
          B('Find right tails and areas between from left areas', 'HSS-ID.A.4', [
              sa('The area to the left of z = 1.5 is 0.9332. What is the area to the right of z = 1.5?', 'Answer:', key='0.0668',
                 note='1 - 0.9332.'),
              sa('Areas to the left: z = -1 gives 0.1587; z = 1 gives 0.8413. Find the area between z = -1 and z = 1.', 'Answer:',
                 key='0.6826', note='0.8413 - 0.1587.'),
              tf('The area to the right of z = 0 is 0.5.', key=True, note='Symmetry.'),
              mc('The area to the left of z = 0.5 is 0.6915. The area between z = 0 and z = 0.5 is', [
                  '0.1915', '0.6915', '0.3085', '0.5'], note='0.6915 - 0.5.'),
              sa('The area to the left of z = 2 is 0.9772. What is the area to the left of z = -2?', 'Answer:', key='0.0228',
                 note='By symmetry it equals the area to the right of z = 2.'),
          ], align='exact',
            why=why('the student cannot turn a table\'s left areas into a right tail or an area between.', 'many questions ask '
                    'for these areas.', 'finds complements, differences and symmetric areas.')),
      ],
      f1=B('Find the cutoff for a percentile', 'HSS-ID.A.4', [
          sa('IQ scores are normal with mean 100 and SD 15. The table gives area 0.9332 to the left of z = 1.5. What score is at the '
             '93.32nd percentile?', 'Score:', key='122.5', note='100 + 1.5·15.'),
          sa('Call lengths are normal with mean 50 s and SD 8 s. The table gives area 0.1056 to the left of z = -1.25. What length '
             'is at the 10.56th percentile?', 'Seconds:', key='40', note='50 - 1.25·8.'),
          tf('A value with z = 0 is at the 50th percentile of a normal distribution.', key=True, note='The median.'),
          mc('A factory wants only the longest 2.28% of rods to be rejected. Rod lengths are normal with mean 10 cm and SD 0.2 cm; '
             'the table gives area 0.9772 to the left of z = 2. What cutoff should it use?', ['10.4 cm', '10.2 cm', '9.6 cm', '12 cm'],
             note='10 + 2·0.2. 9.6 is the lower cutoff; 12 uses z as centimeters.'),
          sa('Heights are normal with mean 175 cm and SD 7 cm; area 0.8413 is to the left of z = 1. What height separates the '
             'tallest 15.87%?', 'Height (cm):', key='182', note='175 + 7.'),
      ], prog='same-course deepening', demand='Work backward from an area to a cutoff value.'),
      f2=B('Make decisions with normal areas', 'HSS-ID.A.4', [
          sa('A bolt fits if its diameter is between 9.8 and 10.2 mm. Diameters are normal with mean 10.0 mm and SD 0.1 mm. Table: '
             'area 0.9772 left of z = 2 and 0.0228 left of z = -2. What proportion of bolts fit?', 'Answer:', key='0.9544',
             note='0.9772 - 0.0228.'),
          mc('Machine A fills bottles with mean 500 mL, SD 4 mL; machine B with mean 502 mL, SD 1 mL. A bottle is underfilled below '
             '498 mL. Table: area 0.3085 to the left of z = -0.5; the area to the left of z = -4 is less than 0.0001. '
             'Which machine underfills fewer bottles?', [
              'B: under 0.01% versus about 31% for A', 'A, because its mean is closer to 498 mL', 'They underfill the same proportion',
              'A, because its standard deviation is larger'],
             note='A: z = (498 - 500)/4 = -0.5, area 0.3085. B: z = (498 - 502)/1 = -4, area very close to 0.'),
          tf('Reducing a process\'s standard deviation, with the mean unchanged, reduces the proportion of items far from the mean.',
             key=True, note='The same limits are more standard deviations away.'),
          sa('Scores are normal with mean 70 and SD 10. A prize goes to scores of 85 or more. Table: area 0.9332 left of z = 1.5. What '
             'proportion of students win?', 'Answer:', key='0.0668', note='1 - 0.9332.'),
          mc('Two normal processes have the same mean. Process 1 has SD 2; process 2 has SD 5. Which has more items within 4 units of '
             'the mean?', ['process 1', 'process 2', 'the same', 'cannot tell'], note='4 units is 2 SDs for process 1 (95%) and 0.8 SD '
                                                                                      'for process 2 (about 58%).'),
      ], prog='same-course deepening', demand='Use normal areas to compare processes and decide.',
        builds='Builds on FORWARD 1: with cutoffs and areas both available, the student evaluates specification limits and '
               'compares processes.')),
]

E7 = [0, 10, 20, 30, 40, 50, 60, 70]
SYM, RSK, BIM, UNI = [1, 4, 9, 12, 9, 4, 1], [14, 10, 6, 4, 3, 2, 1], [3, 10, 6, 2, 6, 10, 3], [6, 6, 6, 5, 6, 6, 5]
HOSP = dict(A=[(95, 100), (120, 400)], B=[(360, 400), (25, 100)])  # (survived, patients): mild, severe
TINY = D('S13 plants', [(1, 3), (2, 5), (3, 4), (4, 7), (5, 8)], '(weeks, cm)', 'Age and height of a seedling, measured weekly')


def pts_desc(p):
    return 'points ' + ', '.join('(%s, %s)' % (n(a), n(b)) for a, b in p)


SETS += [
    # ------------------------------------------------------------------ 10. ID.A.4 when a normal model is not appropriate
    S('HSS-ID.A.4', 'Recognize when a normal model is not appropriate', num=10,
      target='Recognize data sets for which fitting a normal model and estimating percentages is not appropriate (skewed, '
             'bimodal or bounded data), using the shape of a display and the percentages the model would give',
      strand='core', covers=['ID4-suit'],
      main=[
          pickfig('Each histogram shows 40 measurements on the same scale. For which data set is a normal model most '
                  'reasonable?', 'D', [histf(E7, SYM, 'Value', 2, 15), histf(E7, RSK, 'Value', 2, 15),
                                       histf(E7, BIM, 'Value', 2, 15), histf(E7, UNI, 'Value', 2, 15)],
                  'The single symmetric mound fits a normal model. The others are skewed right, have two peaks, or are flat.'),
          sa('Waiting times at a clinic can never be negative. Their mean is 3 minutes and their standard deviation is 4 minutes. '
             'If a normal model with this mean and standard deviation were used, what proportion of waiting times would it place '
             'below 0 minutes?%s Give four decimal places.' % TBL, 'Proportion:', key='%.4f' % t4(-0.75),
             fig=ztable([-1.0, -0.75, -0.5, 0.5]), note='z = (0 - 3)/4 = -0.75; area 0.2266.'),
          mc('Waiting times can never be negative, yet a normal model with their mean (3 minutes) and standard deviation (4 '
             'minutes) places about 23% of times below 0. What does this show?', [
              'A normal model is not appropriate for these waiting times.',
              'The times are normal, but 23% of them were recorded wrong.',
              'A normal model fits, because the mean is a positive number.',
              'The standard deviation must have been computed incorrectly.'],
             note='A model that predicts impossible values for a large share of the data does not fit. A large SD relative to '
                  'the mean is typical of right-skewed, bounded data; nothing says it was computed wrongly.'),
          mc('Which data set is least likely to be approximately normal?', [
              'the yearly incomes of all households in a large city', 'the heights of adult women in one country',
              'the masses of eggs from one large farm', 'repeated careful measurements of one object\'s length'],
             note='Incomes are strongly skewed right (a few very large values). The others are classic near-normal examples.'),
          mc('A box plot of 60 values shows minimum 2, Q1 4, median 5, Q3 9 and maximum 30. Which conclusion is correct?', [
              'The data are skewed right, so a normal model is not a good fit.',
              'The data are roughly symmetric, so a normal model fits well.',
              'The data are skewed left, so a normal model is not a good fit.',
              'A median of 5 shows that the data must be normal.'],
             fig=boxf((2, 4, 5, 9, 30), 0, 32, 'Value', 2),
             note='The upper whisker (21) and upper box half (4) are far longer than the lower ones (2 and 1): skewed right.'),
      ],
      back=[
          B('Describe the shape of a distribution', '6.SP.A.2', [
              tf('A histogram with a long tail to the right is called skewed right.', key=True, note='The tail names the skew.'),
              mc('What is the shape of the data 1, 1, 2, 2, 2, 3, 3, 4, 6, 9?', ['skewed right', 'skewed left', 'symmetric', 'uniform'],
                 note='Most values are low, with a tail toward 9.'),
              tf('A distribution with two separate peaks is called unimodal.', key=False, note='Two peaks: bimodal.'),
              mc('Which list of values is roughly symmetric?', ['2, 4, 5, 5, 6, 8', '1, 1, 1, 2, 9, 20', '1, 10, 18, 19, 19, 20',
                                                                '3, 3, 3, 3, 3, 30'],
                 note='Centered at 5 with equal spread on each side. The others have a long tail.'),
              sa('For the data 4, 5, 5, 6, 6, 6, 7, 7, 8, find the mean and the median.', ['Mean:', 'Median:'], key='6; 6',
                 note='Form required: both. Symmetric data: mean = median = 6.'),
          ], align='supporting',
            why=why('the student cannot recognize skewed, symmetric or bimodal shapes.', 'a normal model needs one symmetric '
                    'mound.', 'names the shape of a display or list.')),
          B('Relate the mean and median to the shape', '6.SP.B.5.d', [
              tf('In a distribution skewed right, the mean is usually greater than the median.', key=True,
                 note='The tail pulls the mean.'),
              mc('A data set has mean 52 and median 40. Which shape is most likely?', ['skewed right', 'skewed left', 'symmetric',
                                                                                    'uniform'],
                 note='Mean well above the median.'),
              sa('For the data 1, 2, 2, 3, 22, find the mean and the median.', ['Mean:', 'Median:'], key='6; 2',
                 note='Form required: both. 30/5 = 6.'),
              tf('For strongly skewed data, the mean and standard deviation are the best summaries of center and spread.',
                 key=False, note='The median and IQR resist the tail.'),
              mc('For data skewed right, which measure best describes a typical value?', ['median', 'mean', 'maximum', 'midrange'],
                 note='The median is resistant to the tail.'),
          ], align='supporting',
            why=why('the student does not see how skew separates the mean from the median.', 'that separation is a sign the '
                    'normal model fails.', 'relates the order of mean and median to the shape.')),
          B('Test a normal model against the data', 'HSS-ID.A.4', [
              sa('Counts of errors per page (never negative) have mean 8 and standard deviation 4. How many standard deviations '
                 'below the mean is 0, and what percent would a normal model place below 0 by the 68-95-99.7 rule?',
                 ['Standard deviations:', 'Percent:'], key='2; 2.5%', note='Form required: both. (8 - 0)/4 = 2.'),
              tf('A data set with any mean and any standard deviation is approximately normal.', key=False,
                 note='Every data set has a mean and SD; the shape decides.'),
              mc('Of 20 values with mean 50 and standard deviation 10, 19 lie between 40 and 60. Is this consistent with a normal '
                 'model?', [
                  'No: a normal model predicts about 68% within 1 SD, but 95% are.',
                  'Yes: a normal model predicts about 95% within 1 SD.',
                  'Yes: every value is within 3 SDs of the mean.',
                  'No: a normal model predicts all values within 1 SD.'],
                 note='19/20 = 95% within 1 SD, far above 68%.'),
              sa('A normal model is used for 200 values. About how many values does it predict within 2 standard deviations of the '
                 'mean?', 'Number:', key='190', note='0.95 · 200.'),
              tf('A normal model with mean 3 and SD 4 places about 16% of its values below -1.', key=True,
                 note='-1 is 1 SD below the mean.'),
          ], align='exact',
            why=why('the student does not check a normal model against the facts about the data.', 'the rule\'s percents give '
                    'the check.', 'compares predicted and actual percents.')),
      ],
      f1=B('Compare actual percents with the 68-95-99.7 rule', 'HSS-ID.A.4', [
          sa('Of 40 values, 27 lie within 1 standard deviation of the mean and 38 lie within 2. What percent is each?',
             ['Within 1 SD:', 'Within 2 SD:'], key='67.5%; 95%', note='Form required: both. 27/40 and 38/40.'),
          mc('Of 40 values, 67.5% are within 1 SD of the mean and 95% within 2 SDs, and a histogram is one symmetric mound. Which '
             'conclusion is reasonable?', [
              'A normal model is reasonable for these data.', 'A normal model is not reasonable, because 67.5% is not 68%.',
              'The data must be skewed right.', 'No conclusion is possible without the raw values.'],
             note='Percents match the rule closely and the shape fits.'),
          tf('If 92% of a data set lies within 1 SD of its mean, the data fit a normal model well.', key=False,
             note='A normal model gives about 68%.'),
          sa('Of 50 values, 46 lie within 1 standard deviation of the mean. What percent is that?', 'Percent:', key='92%',
             note='46/50.'),
          mc('Which result most strongly suggests a data set is not normal?', [
              '92% of the values lie within 1 SD of the mean.', '70% of the values lie within 1 SD of the mean.',
              '96% of the values lie within 2 SDs of the mean.', 'About half of the values lie above the mean.'],
             note='92% is far from 68%; the others are close to the rule.'),
      ], prog='same-course deepening', demand='Judge a normal model by comparing the data\'s percents with the rule.'),
      f2=B('Choose summaries for data that are not normal', 'HSS-ID.A.2', [
          mc('Home prices in a town are strongly skewed right. Which pair of summaries is most appropriate?', [
              'median and IQR', 'mean and standard deviation', 'mean and range', 'mode and maximum'],
             note='Resistant summaries for skewed data.'),
          sa('Home prices (thousands of dollars) are 150, 160, 170, 180, 190, 200, 900. Find the median and the IQR.%s' % QRULE,
             ['Median:', 'IQR:'], key='180; 40', note='Form required: both. Q1 = 160, Q3 = 200.'),
          tf('Using a normal model for strongly skewed data can give misleading percentages.', key=True,
             note='The model\'s tails do not match.'),
          mc('For the prices 150, 160, 170, 180, 190, 200, 900 (thousands), which statement is correct?', [
              'The value 900 pulls the mean above the median.', 'The value 900 pulls the median above the mean.',
              'The mean and the median are equal.', 'The value 900 changes the IQR more than the mean.'],
             note='Mean = 1950/7 ≈ 278.6 > 180.'),
          tf('The standard deviation is resistant to one extreme value.', key=False, note='It uses every deviation, squared.'),
      ], prog='cross-standard extension', demand='Replace normal-based summaries with resistant ones when the shape requires it.',
        builds='Builds on FORWARD 1: once the data fail the normal check, the student picks summaries that do not assume it.')),

    # ------------------------------------------------------------------ 11. ID.B.5 joint and marginal frequencies
    S('HSS-ID.B.5', 'Joint and marginal frequencies in two-way tables', num=11,
      target='Summarize categorical data for two categories in a two-way frequency table and interpret joint and marginal '
             'relative frequencies',
      strand='core', covers=['ID5-joint'],
      main=[
          sa('160 students were asked how they prefer to take a class. What fraction of all students are 10th graders who chose '
             'online? Give a fraction in lowest terms.', 'Fraction:', key='9/32',
             fig=two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE), note='45/160 = 9/32 (joint).'),
          sa('160 students were asked how they prefer to take a class. What is the marginal relative frequency of choosing online? '
             'Give a fraction in lowest terms.', 'Fraction:', key='15/32',
             fig=two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE), note='75/160 = 15/32.'),
          sa('A survey of 120 students: 50 are 7th graders and 70 are 8th graders. 18 of the 7th graders play an instrument, and 20 '
             'of the 8th graders do not. How many 7th graders do not play, and how many 8th graders do play?',
             ['7th graders who do not play:', '8th graders who play:'], key='32; 50',
             note='Form required: both. 50 - 18 and 70 - 20.'),
          mc('160 students were surveyed (table). Which statement gives a marginal relative frequency?', [
              '53.125% of all students chose in person.', '28.125% of all students are 10th graders who chose online.',
              '37.5% of the 9th graders chose online.', '56.25% of the 10th graders chose online.'],
             fig=two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE),
             note='85/160 uses a total over the grand total. The others are a joint frequency and two conditional ones.'),
          sa('A dealer has 100 cars in two lots (table). What percent of all the cars are gray, and what percent of all the cars '
             'are red cars in lot B?', ['Gray:', 'Red in lot B:'], key='40%; 8%',
             fig=two_way(['Lot A', 'Lot B'], ['White', 'Red', 'Gray'], CARS), note='Form required: both. 40/100 and 8/100.'),
      ],
      back=[
          B('Complete and read a two-way frequency table', '8.SP.A.4', [
              sa('120 adults were asked whether they own a dog and whether they walk daily (table). How many walk daily?',
                 'Number:', key='51', fig=two_way(['Has a dog', 'No dog'], ['Walks daily', 'Does not'], PETS), note='36 + 15.'),
              sa('From the dog-and-walking table, how many adults have no dog and do not walk daily?', 'Number:', key='45',
                 fig=two_way(['Has a dog', 'No dog'], ['Walks daily', 'Does not'], PETS), note='Read the cell.'),
              mc('Of 50 students, 20 are in band and 12 of the band members are 9th graders. 30 of the 50 students are 9th graders. '
                 'How many 9th graders are not in band?', ['18', '12', '30', '8'], note='30 - 12. 8 is band members not in 9th grade.'),
              tf('In a two-way table, the row totals add up to the grand total.', key=True, note='Every count is in one row.'),
              tf('In a two-way table, a cell count can be greater than its row total.', key=False, note='Cells add to the row total.'),
          ], align='exact',
            why=why('the student cannot fill in or read cells and totals of a two-way table.', 'relative frequencies are built '
                    'from those counts.', 'completes and reads two-way tables.')),
          B('Write a part of a whole as a fraction, decimal and percent', '7.NS.A.2.d', [
              sa('Write 45/160 as a decimal.', 'Decimal:', key='0.28125', note='45 ÷ 160.'),
              sa('Write 24/120 as a percent.', 'Percent:', key='20%', note='0.2.'),
              tf('3/8 = 0.375.', key=True, note='3 ÷ 8.'),
              mc('Write 15/32 as a percent.', ['46.875%', '15.32%', '47%', '2.13%'], note='15 ÷ 32 = 0.46875.'),
              sa('Write 30/160 in lowest terms.', 'Fraction:', key='3/16', note='Divide by 10.'),
          ], align='supporting',
            why=why('the student cannot turn a count over a total into a fraction, decimal or percent.', 'relative frequencies '
                    'are those quotients.', 'converts fractions to decimals and percents.')),
      ],
      f1=B('Build a joint relative-frequency table', 'HSS-ID.B.5', [
          sa('Convert the online-class table to relative frequencies of the grand total (160). What are the joint relative '
             'frequencies for 9th grade online and 9th grade in person? Give decimals.', ['9th online:', '9th in person:'],
             key='0.1875; 0.3125', fig=two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE),
             note='Form required: both. 30/160 and 50/160.'),
          tf('In a table of joint relative frequencies of the grand total, all the cells add to 1.', key=True,
             note='Every individual is in one cell.'),
          mc('In a joint relative-frequency table, the 9th-grade cells are 0.1875 and 0.3125. What is the 9th-grade marginal '
             'relative frequency?', ['0.5', '0.125', '0.1875', '0.6'], note='Add the row.'),
          sa('In the car table (100 cars), what are the joint relative frequencies for white cars in lot A and gray cars in lot B? '
             'Give decimals.', ['White, lot A:', 'Gray, lot B:'], key='0.18; 0.3',
             fig=two_way(['Lot A', 'Lot B'], ['White', 'Red', 'Gray'], CARS), note='Form required: both.'),
          tf('A marginal relative frequency is always smaller than every joint relative frequency in its row.', key=False,
             note='It is the sum of them.'),
      ], prog='same-course deepening', demand='Convert a whole frequency table into joint relative frequencies.'),
      f2=B('Look for an association by comparing rows', 'HSS-ID.B.5', [
          sa('In the online-class table, what percent of 9th graders and what percent of 10th graders chose online?',
             ['9th:', '10th:'], key='37.5%; 56.25%', fig=two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE),
             note='Form required: both. 30/80 and 45/80.'),
          mc('If grade and choice of class were not associated, what would be true?', [
              'The percent choosing online would be about the same in each grade.',
              'The number choosing online would be 0 in one grade.',
              'Every cell of the table would contain the same count.',
              'The grade totals would have to be unequal.'],
             note='No association: equal conditional rates.'),
          tf('Because more 10th graders (45) than 9th graders (30) chose online, the counts alone prove an association, even if '
             'the grades had very different sizes.', key=False, note='Compare rates, not counts, when totals differ.'),
          sa('In the car table, what percent of lot A cars and what percent of lot B cars are gray?', ['Lot A:', 'Lot B:'],
             key='25%; 50%', fig=two_way(['Lot A', 'Lot B'], ['White', 'Red', 'Gray'], CARS),
             note='Form required: both. 10/40 and 30/60.'),
          mc('Gray makes up 25% of lot A and 50% of lot B. Which is correct?', [
              'Lot and color are associated: gray is more common in lot B.', 'Lot and color are not associated.',
              'Lot B has exactly twice as many cars as lot A.', 'Gray is the most common color in lot A.'],
             note='Rates differ. Lot B has 60 cars, A has 40; white (18) is most common in A.'),
      ], prog='same-course deepening', demand='Use row relative frequencies to judge whether two categorical variables are '
                                             'associated.',
        builds='Builds on FORWARD 1: relative frequencies, now taken within each row, are compared to detect association.')),
]

WIN = dict(x=(0, 10), y=(0, 10))
NEG = [(1, 9), (2, 8.4), (3, 7.8), (4, 7.1), (5, 6.2), (6, 5.6), (7, 4.9), (8, 4.1), (9, 3.4)]
POS = [(1, 2), (2, 2.8), (3, 3.3), (4, 4.1), (5, 4.9), (6, 5.4), (7, 6.3), (8, 7), (9, 7.6)]
WNEG = [(1, 7), (2, 4), (3, 8), (4, 3), (5, 6), (6, 2), (7, 6), (8, 3), (9, 4)]
CURV = [(1, 8), (2, 5), (3, 3), (4, 2), (5, 1.6), (6, 2), (7, 3), (8, 5), (9, 8)]
OT = lambda: two_way(['9th grade', '10th grade'], ['Online', 'In person'], ONLINE)
PT = lambda: two_way(['Has a dog', 'No dog'], ['Walks daily', 'Does not'], PETS)
CT = lambda: two_way(['Lot A', 'Lot B'], ['White', 'Red', 'Gray'], CARS)
HT = tbl(['Hospital', 'Mild: survived / patients', 'Severe: survived / patients'],
         [['A', '95 / 100', '120 / 400'], ['B', '360 / 400', '25 / 100']])

SETS += [
    # ------------------------------------------------------------------ 12. ID.B.5 conditional relative frequencies
    S('HSS-ID.B.5', 'Conditional relative frequencies and association', num=12,
      target='Interpret conditional relative frequencies in a two-way table and use them to recognize possible associations '
             'and trends',
      strand='core', covers=['ID5-cond'],
      main=[
          sa('160 students were surveyed (table). What fraction of the 9th graders chose online, and what fraction of the 10th '
             'graders chose online? Give fractions in lowest terms.', ['9th graders:', '10th graders:'], key='3/8; 9/16', fig=OT(),
             note='Form required: both. 30/80 and 45/80.'),
          mc('In the survey, 37.5% of 9th graders and 56.25% of 10th graders chose online. Which statement is correct?', [
              '10th graders chose online at a higher rate, so grade and choice are associated.',
              '9th graders chose online at a higher rate, so grade and choice are associated.',
              'Each grade has 80 students, so grade and choice cannot be associated.',
              'The rates are equal, so grade and choice are not associated.'],
             fig=OT(), note='Compare the conditional rates. Equal group sizes say nothing about association.'),
          sa('160 students were surveyed (table). Of the students who chose online, what percent were 10th graders?',
             'Percent:', key='60%', fig=OT(), note='45/75 (the online column).'),
          sa('120 adults were surveyed (table). What percent of dog owners walk daily, and what percent of adults without a dog '
             'walk daily?', ['Dog owners:', 'No dog:'], key='60%; 25%', fig=PT(), note='Form required: both. 36/60 and 15/60.'),
          mc('In the survey, 60% of dog owners and 25% of adults without a dog walk daily. Which conclusion is supported?', [
              'Owning a dog and walking daily are associated in this sample.',
              'Owning a dog causes people to walk daily.',
              'Dog ownership and walking daily are not associated.',
              'Adults without a dog walk daily more often.'],
             fig=PT(), note='Different rates show association; a survey cannot show cause.'),
      ],
      back=[
          B('Choose the denominator for a conditional relative frequency', '8.SP.A.4', [
              sa('Of the 60 dog owners, 36 walk daily. What fraction of dog owners walk daily? Give lowest terms.', 'Fraction:',
                 key='3/5', note='36/60.'),
              tf('To find the percent of 9th graders who chose online, divide the 9th-grade online count by the grand total of all '
                 'students.', key=False, note='Divide by the 9th-grade total.'),
              mc('In the online-class table, which number is the denominator for the percent of online-choosers who are 9th '
                 'graders?', ['75, the online total', '80, the 9th-grade total', '160, the grand total', '30, the cell count'],
                 fig=OT(), note='"Of online-choosers" names the column.'),
              sa('Write 30 out of 80 as a percent.', 'Percent:', key='37.5%', note='30/80.'),
              tf('A row relative frequency uses that row\'s total as the denominator.', key=True, note='Definition.'),
          ], align='exact',
            why=why('the student divides by the wrong total.', 'a conditional rate is "of" a group.', 'picks the row or column '
                    'total that matches the wording.')),
          B('Find a percent of a group', '6.RP.A.3.c', [
              sa('45 is what percent of 80?', 'Percent:', key='56.25%', note='45/80.'),
              sa('What is 25% of 60?', 'Answer:', key='15', note='0.25 · 60.'),
              mc('18 out of 24 is what percent?', ['75%', '18%', '24%', '133%'], note='18/24.'),
              tf('9/16 = 56.25%.', key=True, note='9 ÷ 16.'),
              tf('45 is 60% of 80.', key=False, note='45/80 = 56.25%.'),
          ], align='supporting',
            why=why('the student cannot compute a part as a percent of a group.', 'every conditional rate is such a percent.',
                    'finds percents of groups.')),
          B('Compare two fractions', '4.NF.A.2', [
              mc('Which is larger, 3/8 or 9/16?', ['9/16', '3/8', 'they are equal', 'they cannot be compared'],
                 note='3/8 = 6/16.'),
              tf('3/5 > 1/4.', key=True, note='0.6 > 0.25.'),
              sa('Write 3/8 as an equivalent fraction with denominator 16. What is the numerator?', 'Numerator:', key='6',
                 note='Multiply by 2/2.'),
              tf('2/5 > 3/4.', key=False, note='0.4 < 0.75.'),
              mc('Order 1/4, 3/5 and 3/8 from least to greatest.', ['1/4, 3/8, 3/5', '1/4, 3/5, 3/8', '3/8, 1/4, 3/5',
                                                                    '3/5, 3/8, 1/4'],
                 note='0.25, 0.375, 0.6.'),
          ], align='supporting',
            why=why('the student cannot compare the rates once found.', 'association is judged by comparing them.',
                    'compares fractions with unlike denominators.')),
      ],
      f1=B('Distinguish the two directions of a conditional rate', 'HSS-ID.B.5', [
          sa('In the car table, what percent of the gray cars are in lot B, and what percent of the lot B cars are gray?',
             ['Gray cars in lot B:', 'Lot B cars that are gray:'], key='75%; 50%', fig=CT(),
             note='Form required: both. 30/40 and 30/60.'),
          tf('The percent of lot B cars that are gray equals the percent of gray cars that are in lot B.', key=False,
             note='50% versus 75%: different denominators.'),
          mc('In the car table, what percent of the white cars are in lot A?', ['45%', '18%', '30%', '40%'], fig=CT(),
             note='18/40. 18% is of all cars; 40% is lot A\'s share; 30% is 12/40.'),
          sa('In the car table, what percent of the lot A cars are red?', 'Percent:', key='30%', fig=CT(), note='12/40.'),
          mc('Which statement uses a column total of the car table as its denominator?', [
              'Of the red cars, 60% are in lot A.', 'Of the lot A cars, 30% are red.', '12% of all cars are red cars in lot A.',
              '40% of all cars are in lot A.'],
             fig=CT(), note='12/20. The others divide by a row total or the grand total.'),
      ], prog='same-course deepening', demand='Compute conditional rates in both directions and tell them apart.'),
      f2=B('Recognize when combining groups reverses a comparison', 'HSS-ID.B.5', [
          sa('Use the hospital table. What is the survival rate for mild cases at hospital A and at hospital B?',
             ['A:', 'B:'], key='95%; 90%', fig=HT, note='Form required: both. 95/100 and 360/400.'),
          sa('Use the hospital table. What is the survival rate for severe cases at hospital A and at hospital B?',
             ['A:', 'B:'], key='30%; 25%', fig=HT, note='Form required: both. 120/400 and 25/100.'),
          sa('Use the hospital table. What is the overall survival rate (all 500 patients) at hospital A and at hospital B?',
             ['A:', 'B:'], key='43%; 77%', fig=HT, note='Form required: both. 215/500 and 385/500.'),
          mc('Hospital A has the higher survival rate for mild cases and for severe cases, but the lower rate overall. Why?', [
              'A treats many more severe cases, and severe cases survive less often.',
              'A treats many more mild cases, and mild cases survive less often.',
              'The two hospitals treated different total numbers of patients.',
              'The overall rates were computed with the wrong denominators.'],
             fig=HT, note='A: 400 of 500 severe; B: 100 of 500. Both treated 500 patients.'),
          tf('If one group has the higher rate within every category, it must have the higher rate overall.', key=False,
             note='The hospital data are a counterexample (Simpson\'s paradox).'),
      ], prog='same-course deepening', demand='Compare conditional rates within groups and overall, and explain a reversal.',
        builds='Builds on FORWARD 1: the student now chooses which conditional rates to compare when a third variable is '
               'present.')),

    # ------------------------------------------------------------------ 13. ID.B.6 scatter plots and association
    S('HSS-ID.B.6', 'Represent two quantitative variables on a scatter plot', num=13,
      target='Represent data on two quantitative variables on a scatter plot and describe how the variables are related '
             '(direction, form, strength, outliers)',
      strand='core', covers=['ID6-scatter'],
      main=[
          pick('A seedling was measured weekly: (week, height in cm) = %s. Which scatter plot shows the data?' %
               ', '.join('(%d, %d)' % p for p in TINY), 'B', [
                   cand([], 'five points rising from left to right with a dip at week 3', pts=[(a, b, '') for a, b in TINY]),
                   cand([], 'five points rising steeply', pts=[(b, a, '') for a, b in TINY]),
                   cand([], 'five points rising steadily', pts=[(1, 3, ''), (2, 5, ''), (3, 6, ''), (4, 7, ''), (5, 8, '')]),
                   cand([], 'five points falling from left to right', pts=[(1, 8, ''), (2, 7, ''), (3, 4, ''), (4, 5, ''),
                                                                          (5, 3, '')])],
               'The others swap the coordinates, move the week-3 point to 6, or reverse the heights.', x=(0, 9), y=(0, 9)),
          mc('The scatter plot shows hours studied and test scores. Which describes the association?', [
              'strong, positive, linear', 'strong, negative, linear', 'curved, not linear', 'no clear association'],
             fig=FIG_A, note='Points rise in a narrow band along a line.'),
          mc('The scatter plot shows a car\'s speed and fuel efficiency. Which describes the relationship?', [
              'curved: rises, then falls', 'strong, positive, linear',
              'strong, negative, linear', 'no association at all'],
             fig=FIG_C, note='Peaks near 50 mph; a line does not describe it.'),
          sa('The scatter plot shows daily high temperature and ice-cream cones sold. One day does not follow the pattern. Give '
             'its temperature and its cones sold.', ['Temperature (°F):', 'Cones sold:'], key='90; 60', fig=FIG_E,
             note='Form required: both. The other six days lie close to a rising line.'),
          mc('Which pair of variables would most likely show a negative association?', [
              'the age of a car and its resale value', 'the height and arm span of adults',
              'hours studied and test score', 'shoe size and quiz score of adults'],
             note='Value falls with age. Height/arm span and study/score are positive; shoe size and quiz score are unrelated.'),
      ],
      back=[
          B('Plot and read points in the first quadrant', '5.G.A.2', [
              sa('In the study scatter plot, what score did the student who studied 7 hours get?', 'Score:', key='83', fig=FIG_A,
                 note='Point (7, 83).'),
              sa('In the study scatter plot, how many students studied 2 hours?', 'Number:', key='2', fig=FIG_A,
                 note='(2, 58) and (2, 61).'),
              mc('In the study data, what does the point (4, 70) mean?', [
                  'a student studied 4 hours and scored 70', 'a student studied 70 hours and scored 4',
                  '4 students scored 70', 'the average score was 70'],
                 note='(x, y) = (hours, score).'),
              tf('In the ordered pair (3, 63), 63 is the x-coordinate.', key=False, note='63 is the y-coordinate.'),
              sa('In the car scatter plot, what is the resale value of the 8-year-old car, in thousands of dollars?', 'Value:',
                 key='9', fig=FIG_B, note='Point (8, 9).'),
          ], align='supporting',
            why=why('the student cannot plot or read ordered pairs.', 'a scatter plot is a set of ordered pairs.', 'locates and '
                    'reads points.')),
          B('Describe patterns of association', '8.SP.A.1', [
              tf('When y tends to increase as x increases, the association is positive.', key=True, note='Definition.'),
              mc('The scatter plot shows shoe size and quiz score. Which describes it?', [
                  'no clear association', 'strong, positive, linear', 'strong, negative, linear', 'curved'],
                 fig=FIG_D, note='The points form a shapeless cloud.'),
              tf('A scatter plot whose points lie close to a U-shaped curve shows a linear association.', key=False,
                 note='That is a nonlinear association.'),
              mc('In the ice-cream scatter plot, the point (90, 60) is best described as', [
                  'an outlier', 'a cluster', 'the trend line', 'the y-intercept'], fig=FIG_E,
                 note='It lies far from the pattern of the other points.'),
              sa('In the fuel-efficiency scatter plot, at what speed is the fuel efficiency greatest?', 'Speed (mph):', key='50',
                 fig=FIG_C, note='Highest point (50, 34).'),
          ], align='exact',
            why=why('the student cannot name direction, form or outliers.', 'the standard asks for that description.',
                    'describes association in a scatter plot.')),
      ],
      f1=B('Compare the direction, form and strength of associations', 'HSS-ID.B.6', [
          pick('Which scatter plot shows a strong, negative, linear association?', 'C', [
              cand([], 'points falling steadily in a narrow band', pts=[(a, b, '') for a, b in NEG]),
              cand([], 'points rising steadily in a narrow band', pts=[(a, b, '') for a, b in POS]),
              cand([], 'points falling loosely with wide scatter', pts=[(a, b, '') for a, b in WNEG]),
              cand([], 'points falling then rising in a U shape', pts=[(a, b, '') for a, b in CURV])],
               'The others are positive, weak, or curved.', x=(0, 10), y=(0, 10)),
          mc('The scatter plot shows the age and resale value of cars. Which describes it?', [
              'strong, negative, linear', 'strong, positive, linear', 'weak, positive, linear', 'curved, then level'],
             fig=FIG_B, note='Values fall steadily with age.'),
          tf('A pattern can show a strong association even when it is not linear.', key=True, note='The fuel data are an example.'),
          mc('In the ice-cream scatter plot, if the outlier (90, 60) is ignored, the other six days show', [
              'a strong, positive, linear association', 'a strong, negative, linear association', 'no association',
              'a U-shaped association'],
             fig=FIG_E, note='The six points rise along a line.'),
          tf('Removing an outlier can never change how strong an association looks.', key=False,
             note='The ice-cream data look weak with it and strong without it.'),
      ], prog='same-course deepening', demand='Compare several scatter plots and judge strength with and without outliers.'),
      f2=B('Distinguish association from causation', 'HSS-ID.C.9', [
          mc('Cities with more fire stations tend to have more fires. Which is the best explanation?', [
              'Larger cities have both more stations and more fires.', 'Fire stations cause fires to start.',
              'Fires cause cities to build fewer stations.', 'The association must be a mistake in the data.'],
             note='City size is a lurking variable.'),
          tf('A strong association between two variables proves that one causes the other.', key=False,
             note='Association alone does not show cause.'),
          mc('To show that a fertilizer causes taller plants, which study is needed?', [
              'a randomized experiment with fertilized and unfertilized plants', 'a survey of gardeners about their plants',
              'a scatter plot of plant heights found in gardens', 'measuring only the plants that received fertilizer'],
             note='Random assignment controls other causes.'),
          mc('Ice-cream sales and swimming accidents both rise during the year. What best explains the association?', [
              'Hot weather increases both.', 'Eating ice cream causes swimming accidents.',
              'Swimming accidents cause ice-cream sales.', 'The two variables are unrelated.'],
             note='A lurking variable (temperature).'),
          tf('In an observational study, a lurking variable can create an association between two variables.', key=True,
             note='Both depend on it.'),
      ], prog='cross-standard extension', demand='Decide whether an observed association supports a causal claim.',
        builds='Builds on FORWARD 1: after judging how strong an association is, the student asks whether it shows cause.')),

    # ------------------------------------------------------------------ 14. ID.B.6.a use a fitted function
    S('HSS-ID.B.6.a', 'Use a function fitted to data to solve problems', num=14,
      target='Use a given function fitted to data (linear, exponential or quadratic) to make predictions and solve problems '
             'in context',
      strand='core', covers=['ID6a-use'],
      main=[
          sa('For a group of students, a line fitted to the data is y = 2.5x + 12, where x is hours of practice and y is the '
             'predicted number of free throws made out of 50. Predict y for 8 hours of practice.', 'Predicted y:', key='32',
             note='2.5·8 + 12.'),
          sa('A bacteria culture is modeled by P = 200(1.15)^t, where t is hours. Predict the population after 6 hours, to the '
             'nearest whole number.%s' % TECH, 'Population:', key='463', note='200 · 1.15^6 = 462.61...'),
          sa('A ball\'s height is modeled by h = -4.9t^2 + 20t + 1.5 (meters, t in seconds). Predict the height at t = 2 seconds.',
             'Height (m):', key='21.9', note='-19.6 + 40 + 1.5.'),
          sa('A line fitted to data is y = 0.8x + 5, where x is the temperature (°C) and y is the predicted number of visitors '
             '(hundreds). For what temperature does the model predict 29 hundred visitors?', 'Temperature (°C):', key='30',
             note='0.8x = 24.'),
          sa('A car\'s value is modeled by V = 18000(0.85)^t, where t is years. Predict the value after 4 years, to the nearest '
             'dollar.%s' % TECH, 'Value ($):', key='9396', note='0.85^4 = 0.52200625; 18000 · 0.52200625 = 9396.11.'),
      ],
      back=[
          B('Evaluate a function at an input', 'HSF-IF.A.2', [
              sa('f(x) = 3x - 4. Find f(6).', 'f(6):', key='14', note='18 - 4.'),
              sa('g(t) = 100(2)^t. Find g(3).', 'g(3):', key='800', note='100 · 8.'),
              tf('If h(t) = -5t^2 + 10t, then h(1) = 5.', key=True, note='-5 + 10.'),
              mc('f(x) = 0.5x + 7. What is f(10)?', ['12', '17', '7.5', '57'], note='5 + 7. 57 treats 0.5x as 50.'),
              tf('If p(t) = 50(1.1)^t, then p(0) = 55.', key=False, note='p(0) = 50.'),
          ], align='supporting',
            why=why('the student cannot substitute into function notation.', 'every prediction is an evaluation.',
                    'evaluates linear, exponential and quadratic functions.')),
          B('Evaluate expressions with exponents', '6.EE.A.2.c', [
              sa('Evaluate 1.5^2.', 'Answer:', key='2.25', note='1.5 · 1.5.'),
              sa('Evaluate 4·3^2 - 6.', 'Answer:', key='30', note='Exponent first: 36 - 6.'),
              tf('2·5^2 = 100.', key=False, note='2·25 = 50; 100 squares 10.'),
              mc('Evaluate 1000(0.9)^2.', ['810', '1800', '900', '81'], note='0.81 · 1000.'),
              tf('(-3)^2 = 9.', key=True, note='(-3)(-3).'),
          ], align='supporting',
            why=why('the student applies operations in the wrong order or mishandles powers.', 'exponential and quadratic models '
                    'need powers first.', 'evaluates powers in the correct order.')),
          B('Solve a linear equation for the input', 'HSA-REI.B.3', [
              sa('Solve 0.8x + 5 = 21.', 'x:', key='20', note='0.8x = 16.'),
              sa('Solve 2.5x + 12 = 47.', 'x:', key='14', note='2.5x = 35.'),
              tf('The solution of 3x - 4 = 11 is x = 5.', key=True, note='3x = 15.'),
              mc('Solve 1.2x + 6 = 30.', ['20', '30', '25', '28.8'], note='1.2x = 24.'),
              tf('The solution of 0.5x + 3 = 8 is x = 5.5.', key=False, note='0.5x = 5, x = 10.'),
          ], align='supporting',
            why=why('the student cannot work backward from a predicted output.', 'some questions give the output.',
                    'solves linear equations with decimal coefficients.')),
      ],
      f1=B('Judge whether a prediction is reasonable', 'HSS-ID.B.6.a', [
          mc('The line y = 2.5x + 12 was fitted to students who practiced 0 to 12 hours (y = free throws made out of 50). It '
             'predicts y = 87 for 30 hours. Which is correct?', [
              'Unreasonable: 30 hours is far outside the data, and 87 exceeds 50.',
              'Reasonable, because the line fits the data from 0 to 12 hours.',
              'Reasonable, because 30 hours is a whole number of hours.',
              'Unreasonable, because a fitted line must have a negative slope.'],
             note='Extrapolation; the value is impossible. A positive slope is not the problem.'),
          sa('A line fitted to data for x from 10 to 40 is y = 3x - 5. Predict y at x = 25, and state whether x = 25 is inside the '
             'data range by entering yes or no.', ['Predicted y:', 'Inside the range (yes or no):'], key='70; yes',
             note='Form required: both. 75 - 5 = 70; 25 is between 10 and 40.'),
          tf('Predicting far outside the range of the data (extrapolation) is usually less reliable than predicting inside it.',
             key=True, note='The pattern may not continue.'),
          sa('The model V = 18000(0.85)^t fits a car\'s value for t = 0 to 8 years. What value does it predict at t = 0?', 'V ($):',
             key='18000', note='0.85^0 = 1.'),
          tf('The model h = -4.9t^2 + 20t + 1.5 gives sensible heights for every value of t, including t = 10.', key=False,
             note='h(10) = -288.5, below the ground: the ball has landed.'),
      ], prog='same-course deepening', demand='Check a prediction against the data range and the context.'),
      f2=B('Compare predictions from two fitted models', 'HSS-ID.B.6.a', [
          sa('Two models fit a town\'s population (thousands), t years after 2020: linear L = 2t + 40 and exponential '
             'E = 40(1.05)^t. Predict each for t = 2. Round E to two decimal places.', ['L:', 'E:'], key='44; 44.1',
             note='Form required: both. 40 · 1.1025 = 44.1.'),
          mc('For the models L = 2t + 40 and E = 40(1.05)^t, which statement about large t is correct?', [
              'E eventually predicts more, because it grows by a constant percent.',
              'L always predicts more, because its slope is 2.',
              'The two models always predict the same population.',
              'E eventually predicts less, because 1.05 is close to 1.'],
             note='Exponential growth eventually exceeds linear growth.'),
          sa('Using L = 2t + 40 (thousands), in what year t after 2020 does L predict 60 thousand?', 't:', key='10',
             note='2t = 20.'),
          tf('If two models fit the data equally well inside the data range, they must give the same prediction far outside it.',
             key=False, note='They can diverge, as L and E do.'),
          mc('A residual check shows the exponential model leaves random scatter and the linear model leaves a curved pattern. '
             'Which model should be used for predictions?', ['the exponential model', 'the linear model', 'either, equally',
                                                              'neither, because residuals exist'],
             note='A curved residual pattern shows the linear form is wrong.'),
      ], prog='same-course deepening', demand='Use and compare two fitted models of different families.',
        builds='Builds on FORWARD 1: judging one model\'s predictions becomes choosing between two models\' predictions.')),
]
