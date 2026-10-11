from qb import S, B, sa, mc, tf, plot, work, table, dot, box, hist, hrow, nl
from common import grid, spinner, BLANK


def tbl(xname, xs, yname, ys):
    return table([[xname] + [str(v) for v in xs], [yname] + [str(v) for v in ys]], header='col')


def two_way(rows):
    return table(rows, header='both')


SC = grid(10, 10, pts=[(1, 2), (2, 3), (3, 3), (4, 5), (5, 5), (6, 7), (7, 7), (8, 9)])
SC2 = grid(10, 10, xlabel='Hours of practice', ylabel='Goals scored', pts=[(1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 5), (8, 1)])
SPORT = two_way([['', 'Plays a sport', 'No sport', 'Total'], ['Has a job', '12', '18', '30'], ['No job', '28', '22', '50'], ['Total', '40', '40', '80']])
TRAVEL = two_way([['', 'Walks', 'Rides', 'Total'], ['Sixth grade', '24', '36', '60'], ['Seventh grade', '15', '45', '60'], ['Total', '39', '81', '120']])
RAIN = two_way([['', 'Likes rain', 'Dislikes rain', 'Total'], ['Adults', '18', '42', '60'], ['Teens', '9', '31', '40'], ['Total', '27', '73', '100']])
PETS = two_way([['', 'Cat', 'Dog', 'Total'], ['Grade 9', '15', '25', '40'], ['Grade 10', '20', '20', '40'], ['Total', '35', '45', '80']])
COINDIE = two_way([['', 'Heads', 'Tails', 'Total'], ['Even', '24', '26', '50'], ['Odd', '27', '23', '50'], ['Total', '51', '49', '100']])
MUSIC = two_way([['', 'Plays music', 'No music', 'Total'], ['Grade 9', '18', '42', '60'], ['Grade 10', '12', '28', '40'], ['Total', '30', '70', '100']])
TOWNS = box(20, 65, None, step=5, lstep=10, xlabel='Daily high temperature (°F)',
            boxes=[('Town A', (20, 30, 35, 40, 50)), ('Town B', (30, 40, 45, 52, 64))])
BP = box(0, 20, (3, 6, 10, 14, 18), step=1, lstep=2)
BASE = [-4, -2, -2, -2, 0, 0, 2, 2, 2, 4]   # mean 0, MAD 2


def pair(c1, c2, n1, n2, lo, hi, xlabel):
    """Two dot plots on the same scale; each data set is BASE shifted to center c (mean c, MAD 2)."""
    return dict(k='vstack', figs=[dot(lo, hi, [c1 + b for b in BASE], lstep=2, title='%s (%s)' % (n1, xlabel), h=150),
                                  dot(lo, hi, [c2 + b for b in BASE], lstep=2, title='%s (%s)' % (n2, xlabel), h=150)])


def blank_tw(r1, r2, c1, c2):
    e = ' ' * 10
    return two_way([['', c1, c2, 'Total'], [r1, e, e, e], [r2, e, e, e], ['Total', e, e, e]])


ART = two_way([['', 'Chose art', 'Did not', 'Total'], ['Grade 7 sample', '12', '18', '30'], ['Grade 8 sample', '9', '21', '30'], ['Total', '21', '39', '60']])
COIN40 = two_way([['', 'Even', 'Odd', 'Total'], ['Heads', '11', '9', '20'], ['Tails', '8', '12', '20'], ['Total', '19', '21', '40']])
SIM_REDS = dot(0, 12, {1: 1, 2: 3, 3: 6, 4: 9, 5: 11, 6: 9, 7: 6, 8: 3, 9: 1, 10: 1}, xlabel='Number of reds in 20 spins (50 simulations)')
SPINS = hist(['Red', 'Blue', 'Green'], [9, 6, 5], gap=0.35, ymax=10, ystep=2, xlabel='Color', ylabel='Spins', h=200)

SETS = [
    # ------------------------------------------------------------------ 7.SP.A.1
    S('7.SP.A.1', 'Understand random sampling and representative samples',
      main=[
          mc('A principal wants to know students\' favorite lunch.\nWhich sample is most likely to represent all the students in the school?',
             ['20 students chosen at random from the school list', 'The first 20 students in the lunch line', '20 students on the basketball team', '20 students in one 7th grade class']),
          sa('A town surveys people at a gym about how often they exercise.\nIs the sample likely to represent the whole town? Explain.', 'Answer:',
             key='No. People at a gym probably exercise more than people in the whole town, so the sample is biased.'),
          sa('Describe one way to choose a random sample of 30 students from a school of 600 students.', 'Answer:',
             key='Number the students 1 to 600 and use a random number generator to choose 30 different numbers.',
             note='Any method that gives every student the same chance of being chosen is correct.'),
          tf('In a random sample, every member of the population has the same chance of being chosen.', key=True),
          tf('A large sample always represents the population, even if it is not chosen at random.', key=False),
      ],
      back=[
          B('Recognize a statistical question', '6.SP.A.1', [
              sa('Is "How tall are the students in my class?" a statistical question? Explain.', 'Answer:', key='Yes. The answers will vary from student to student.'),
              mc('Which is a statistical question?', ['How many hours do 7th graders sleep on school nights?', 'How tall is the school flagpole?', 'What is 5 × 8?', 'What day is it today?']),
              sa('Rewrite "How old am I?" as a statistical question.', 'Question:', key='How old are the students in my school?',
                 note='Any question whose answers vary, such as one about a group\'s ages, is correct.'),
              tf('"What are the shoe sizes of the players on the team?" is a statistical question.', key=True),
              tf('"How many days are in March?" is a statistical question.', key=False),
          ]),
          B('Report the number of observations', '6.SP.B.5.a', [
              sa('How many observations does the dot plot show?', 'Observations:', fig=dot(1, 6, [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]), key='10'),
              sa('A survey asks 25 students how many pets they have. Each student gives one answer.\nHow many observations are there?', 'Observations:', key='25'),
              mc('A table lists the heights of 18 plants, one height for each plant.\nHow many observations are there?', ['18', '1', '36', '9']),
              tf('Each dot on a dot plot shows one observation.', key=True),
              tf('A data set of 12 test scores has 24 observations.', key=False),
          ]),
      ],
      f1=B('Summarize survey data in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows the results of a survey.\nWhat fraction of the surveyed students play a sport?', 'Fraction:', fig=SPORT, key='1/2', note='40/80 is also correct.'),
          sa('The table shows the results of a survey.\nWhat fraction of all surveyed students have a job and play a sport?', 'Fraction:', fig=SPORT, key='3/20', note='12/80, or 0.15, is also correct.'),
          mc('The table shows the results of a survey.\nAmong students who have a job, what fraction play a sport?', ['{2/5}', '{3/10}', '{3/20}', '{3/5}'], fig=SPORT),
          tf('In the table, 56% of the students with no job play a sport.', fig=SPORT, key=True),
          tf('In the table, more than half of all the students have a job.', fig=SPORT, key=False),
      ]),
      f2=B('Recognize surveys, experiments, and observational studies', 'HSS-IC.B.3', [
          sa('Researchers randomly assign 50 plants to get a new plant food and 50 plants to get none.\nIs this a survey, an experiment, or an observational study?', 'Answer:', key='An experiment'),
          sa('A study records the screen time of 200 teens without changing anything they do.\nIs this a survey, an experiment, or an observational study?', 'Answer:', key='An observational study'),
          mc('Why is random assignment used in an experiment?',
             ['To make the groups alike, so differences can be linked to the treatment', 'To make the sample larger', 'To let people choose their own group', 'To avoid collecting data']),
          tf('A survey asks a sample of people questions in order to estimate facts about a population.', key=True),
          tf('An observational study can prove that one variable causes another.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.A.2 (inference)
    S('7.SP.A.2', 'Use data from a random sample to draw inferences about a population',
      main=[
          sa('In a random sample of 50 students, 18 prefer the art club.\nPredict how many of the 800 students in the school prefer the art club.', 'Students:', key='288'),
          sa('In a random sample of 40 light bulbs, 2 do not work.\nEstimate how many bulbs in a shipment of 2,000 do not work.', 'Bulbs:', key='100'),
          mc('In a random sample of 60 voters, 33 support a plan.\nWhat is the best estimate of the percent of all voters who support it?', ['55%', '33%', '60%', '45%']),
          tf('In a random sample of 25 fish from a lake, 5 are trout. A good estimate is that 20% of the fish in the lake are trout.', key=True),
          tf('In a random sample of 30 homes, 9 have a dog. A good estimate is that 900 of 1,500 homes have a dog.', key=False, note='A good estimate is 450 homes.'),
      ],
      back=[
          B('Find what percent a part is of a whole', '6.RP.A.3.c', [
              sa('18 out of 50 is what percent?', 'Percent:', key='36%'),
              sa('10 is what percent of 40?', 'Percent:', key='25%'),
              mc('7 out of 20 is what percent?', ['35%', '7%', '20%', '70%']),
              tf('12 out of 48 is 25%.', key=True),
              tf('9 out of 30 is 9%.', key=False, note='9 out of 30 is 30%.'),
          ]),
          B('Find a missing value in equivalent ratios', '6.RP.A.3.a', [
              sa('Find the missing value.\n2 : 5 = ? : 100', 'Missing value:', key='40'),
              sa('Find the missing value.\n4 : 9 = 28 : ?', 'Missing value:', key='63'),
              mc('Which ratio is equivalent to 6 : 15?', ['2 : 5', '3 : 5', '6 : 5', '1 : 3']),
              tf('5 : 8 = 25 : 40', key=True),
              tf('3 : 7 = 9 : 14', key=False),
          ]),
      ],
      f1=B('Use a linear model to make a prediction', '8.SP.A.3', nearest=True, qs=[
          sa('A line of fit is y = 2.5x + 40, where x is hours studied and y is a test score.\nPredict the score for 8 hours of study.', 'Score:', key='60'),
          sa('A line of fit is y = 2.5x + 40, where x is hours studied and y is a test score.\nWhat does 2.5 mean?', 'Meaning:',
             key='Each extra hour of study goes with a score about 2.5 points higher.'),
          mc('A line of fit is y = -3x + 90.\nWhat does it predict for x = 10?', ['60', '120', '87', '93']),
          tf('For the line of fit y = 0.5x + 12, the predicted y-value at x = 0 is 12.', key=True),
          tf('The line of fit y = 4x + 1 predicts y = 41 when x = 9.', key=False, note='It predicts y = 37.'),
      ]),
      f2=B('Use a margin of error to describe a population estimate', 'HSS-IC.B.4', [
          sa('A random sample shows 52% support for a plan, with a margin of error of 4%.\nWhat interval of values is likely for the whole population?', 'Interval:', key='48% to 56%'),
          sa('A random sample has a mean of 6.8 hours with a margin of error of 0.5 hour.\nWhat interval of values is likely for the population mean?', 'Interval:', key='6.3 to 7.3 hours'),
          mc('As a random sample gets larger, what usually happens to the margin of error?', ['It gets smaller.', 'It gets larger.', 'It stays the same.', 'It becomes 0 once the sample is over 10.']),
          tf('A margin of error describes how far a sample estimate is likely to be from the population value.', key=True),
          tf('A poll result of 52% with a 4% margin of error proves that more than half of the population supports the plan.', key=False,
             note='The interval 48% to 56% includes values below 50%.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.A.2 (variation)
    S('7.SP.A.2', 'Use several random samples to judge how much estimates vary',
      main=[
          sa('Four random samples of 20 students give these mean hours of sleep: 7.8, 8.2, 8.0, and 8.4.\nWhat is a good estimate of the mean for all the students? Use the mean of the samples.', 'Estimate:', key='8.1 hours'),
          sa('Four random samples give mean estimates of 7.8, 8.2, 8.0, and 8.4 hours.\nWhat is the range of the estimates?', 'Range:', key='0.6 hour'),
          mc('Three random samples of 50 people show that 22%, 26%, and 24% prefer blue.\nWhich conclusion is best?',
             ['About 24% of the population prefers blue.', 'Exactly 22% of the population prefers blue.', 'Exactly 26% of the population prefers blue.', 'The samples are useless because they differ.']),
          tf('Different random samples from the same population usually give somewhat different results.', key=True),
          tf('Small random samples usually give estimates that vary less than large random samples.', key=False),
      ],
      back=[
          B('Find the mean of a data set', '6.SP.B.5.c', [
              sa('Find the mean.\n4, 7, 9, 10', 'Mean:', key='7.5'),
              sa('Find the mean.\n12, 15, 18', 'Mean:', key='15'),
              mc('What is the mean of 3, 3, 6, and 8?', ['5', '4.5', '6', '3']),
              tf('The mean of 2, 4, 6, and 8 is 5.', key=True),
              tf('The mean of 10, 20, and 60 is 20.', key=False, note='The mean is 30.'),
          ]),
          B('Find the range as a measure of variation', '6.SP.A.3', [
              sa('Find the range.\n12, 18, 9, 15', 'Range:', key='9'),
              sa('Find the range.\n3.5, 7, 4.25, 6', 'Range:', key='3.5'),
              mc('Which data set has the greatest range?', ['2, 10, 5', '4, 6, 5', '7, 9, 8', '1, 3, 2']),
              tf('The range of 20, 25, and 30 is 10.', key=True),
              tf('A data set whose values are all the same has a range of 1.', key=False, note='Its range is 0.'),
          ]),
      ],
      f1=B('Describe the association shown in a scatter plot', '8.SP.A.1', nearest=True, qs=[
          sa('What kind of association does the scatter plot show?', 'Association:', fig=SC, key='A positive linear association'),
          sa('A scatter plot shows hours of practice (x) and free throws made (y). The points rise from left to right in a roughly straight pattern.\nDescribe the association.', 'Association:',
             key='A positive linear association'),
          mc('A scatter plot shows the age of a car (x) and its value (y).\nWhat association is most likely?', ['Negative association', 'Positive association', 'No association', 'Every point on one line']),
          tf('In a scatter plot with no association, the points show no clear trend.', key=True),
          tf('Points that fall from left to right in a scatter plot show a positive association.', key=False),
      ]),
      f2=B('Decide whether a result is consistent with a model by simulation', 'HSS-IC.A.2', [
          sa('A coin is said to be fair. In 100 simulated sets of 20 fair flips, 15 or more heads happened only 2 times. A real coin gives 15 heads in 20 flips.\nIs the fair-coin model believable? Explain.', 'Answer:',
             key='Probably not. A result that extreme happens only about 2% of the time with a fair coin, so the result casts doubt on the model.'),
          mc('Simulations of a spinner model usually give 3 to 7 reds in 20 spins. A real spinner gives 5 reds in 20 spins.\nWhat does this show?',
             ['The result is consistent with the model.', 'The model is proven wrong.', 'The result is impossible.', 'The spinner is proven unfair.']),
          sa('In 100 simulations of a model, a certain result happened 40 times.\nIs that result unusual for the model? Explain.', 'Answer:', key='No. It happened about 40% of the time.'),
          tf('A result that rarely happens in simulations of a model suggests that the model may be wrong.', key=True),
          tf('A result that happens even once in 1,000 simulations is a common result.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.A.2 (generate samples) -- added in 2.0.0
    S('7.SP.A.2', 'Generate several same-size random samples with random digits and see how the estimates vary', num=69,
      main=[
          sa('A school has 100 students numbered 00 to 99. Students 00 to 39 chose art as their favorite class.\nUse these random two-digit numbers to choose a sample of 5 students:\n07  52  31  88  14\nWhat percent of the sample chose art?', 'Percent:',
             key='60%', note='07, 31, and 14 chose art: 3 out of 5.'),
          sa('A school has 100 students numbered 00 to 99. Students 00 to 39 chose art as their favorite class.\nUse these random two-digit numbers to choose a sample of 5 students:\n45  63  02  97  71\nWhat percent of the sample chose art?', 'Percent:',
             key='20%', note='Only 02 chose art: 1 out of 5.'),
          mc('Students 00 to 39 of a school of 100 chose art. Four random samples of 5 students were chosen with random digits:\nSample 1: 07 52 31 88 14\nSample 2: 45 63 02 97 71\nSample 3: 38 19 60 25 84\nSample 4: 50 11 76 93 66\nWhat is the range of the four sample percents?',
             ['40 percentage points', '20 percentage points', '60 percentage points', '0 percentage points']),
          sa('Students 00 to 39 of a school of 100 chose art, so the true percent is 40%. Four random samples of 5 students gave 60%, 20%, 60%, and 20%.\nWhat is the mean of the four sample percents? How does it compare with the true percent, and how much do single samples vary?', 'Answer:',
             key='The mean is 40%, the same as the true percent, but single samples varied from 20% to 60%.', note='Grade both: the mean 40%, and the variation of single samples.'),
          tf('Random samples of 5 students gave estimates from 20% to 60%. Random samples of 50 students from the same school would usually give estimates that are closer together.', key=True),
      ],
      back=[
          B('Write a part of a small sample as a percent', '6.RP.A.3.c', [
              sa('Write 3 out of 5 as a percent.', 'Percent:', key='60%'),
              sa('Write 2 out of 5 as a percent.', 'Percent:', key='40%'),
              mc('What percent is 4 out of 5?', ['80%', '45%', '4%', '20%']),
              tf('1 out of 5 is 20%.', key=True),
              tf('3 out of 5 is 35%.', key=False, note='3 out of 5 is 60%.'),
          ]),
          B('Find the mean of a small data set', '6.SP.B.5.c', [
              sa('Find the mean.\n60, 20, 60, 20', 'Mean:', key='40'),
              sa('Find the mean.\n30, 50, 40', 'Mean:', key='40'),
              mc('What is the mean of 20, 40, 40, and 60?', ['40', '45', '50', '35']),
              tf('The mean of 10, 30, and 50 is 30.', key=True),
              tf('The mean of 20, 20, and 80 is 20.', key=False, note='The mean is 40.'),
          ]),
      ],
      f1=B('Summarize categorical data from two random samples in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows random samples of 30 students from each grade.\nWhat percent of the Grade 7 sample chose art?', 'Percent:', fig=ART, key='40%', note='12/30 or 2/5 is also correct.'),
          sa('The table shows random samples of 30 students from each grade.\nWhat percent of the Grade 8 sample chose art?', 'Percent:', fig=ART, key='30%'),
          mc('The table shows random samples of 30 students from each grade.\nWhich conclusion do the samples best support?',
             ['A greater share of Grade 7 students than Grade 8 students may prefer art.', 'Exactly 40% of all Grade 7 students prefer art.',
              'No Grade 8 student prefers art.', 'Every Grade 7 student prefers art.'], fig=ART),
          tf('In the table, the relative frequency of choosing art in the whole sample of 60 students is 0.35.', fig=ART, key=True),
          tf('In the table, more Grade 8 students than Grade 7 students chose art.', fig=ART, key=False),
      ]),
      f2=B('Use the spread of simulated samples to give an interval for a population percent', 'HSS-IC.B.4', [
          sa('Simulations show that the middle 95% of random samples of 50 students land within 10 percentage points of the true percent. A real random sample of 50 gives 44%.\nWhat interval is likely to contain the population percent?', 'Interval:', key='34% to 54%'),
          sa('Simulations show that the middle 95% of random samples of 200 people land within 7 percentage points of the true percent. A real random sample of 200 gives 58%.\nWhat interval is likely to contain the population percent?', 'Interval:', key='51% to 65%'),
          mc('In simulations, how does the spread of sample percents change as the samples get larger?', ['It gets smaller.', 'It gets larger.', 'It stays the same.', 'It becomes 0.']),
          tf('An interval of 34% to 54% means the population percent is likely between those values, but it is not certain.', key=True),
          tf('Simulated samples of 50 vary by about 10 percentage points. So one real sample of 50 always lands exactly on the population percent.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.B.3
    S('7.SP.B.3', 'Describe how much two distributions overlap using the difference in means as a multiple of the MAD',
      main=[
          sa('The dot plots show quiz scores for two classes. The means are 10 and 16, and each data set has a MAD of 2.\nWrite the difference in the means as a multiple of the MAD.', 'Answer:',
             fig=pair(10, 16, 'Class A', 'Class B', 4, 22, 'Quiz score'), key='3 MADs'),
          sa('The dot plots show the heights of two kinds of plants, in centimeters. The means are 10 and 11, and each data set has a MAD of 2.\nWrite the difference in the means as a multiple of the MAD, and describe how much the dot plots overlap.', 'Answer:',
             fig=pair(10, 11, 'Plant A', 'Plant B', 4, 16, 'Height (cm)'),
             key='0.5 MAD; the dot plots overlap a lot (most values of each set are inside the range of the other).', note='Grade both parts.'),
          mc('The dot plots show the minutes two groups spent reading. The means are 10 and 14, and each data set has a MAD of 2.\nWhich statement describes the dot plots?',
             ['The means differ by 2 MADs, and the plots overlap somewhat.', 'The means differ by 4 MADs, and the plots do not overlap.',
              'The means are the same, so the plots overlap completely.', 'The means differ by 2 MADs, so the plots cannot share any values.'],
             fig=pair(10, 14, 'Group A', 'Group B', 4, 20, 'Minutes')),
          tf('The dot plots show two data sets with means of 10 and 12, and each has a MAD of 2. The means differ by 1 MAD, and the dot plots overlap a lot.',
             fig=pair(10, 12, 'Set A', 'Set B', 4, 18, 'Value'), key=True),
          tf('The dot plots show two data sets with means of 20 and 26, and each has a MAD of 2. The means differ by 3 MADs, and the two dot plots share no values.',
             fig=pair(20, 26, 'Team A', 'Team B', 14, 32, 'Points'), key=False,
             note='The values 22 and 24 appear in both data sets. For distributions of similar shape and spread, a difference of several MADs usually means little overlap, but not necessarily none.'),
      ],
      back=[
          B('Find the mean absolute deviation (MAD)', '6.SP.B.5.c', [
              sa('Find the MAD.\n2, 4, 6, 8', 'MAD:', key='2'),
              sa('Find the MAD.\n5, 5, 9, 13', 'MAD:', key='3'),
              mc('What is the MAD of 10, 10, 10, 10?', ['0', '10', '40', '1']),
              tf('The MAD of 1, 3, 5, 7 is 2.', key=True),
              tf('The MAD of 0 and 10 is 10.', key=False, note='The MAD is 5.'),
          ]),
          B('Describe the shape of a distribution', '6.SP.A.2', [
              mc('A dot plot has most of its dots on the left and a long tail to the right.\nHow is its shape described?', ['Skewed right', 'Skewed left', 'Symmetric', 'Uniform']),
              sa('Is the distribution in the dot plot symmetric?', 'Answer:', fig=dot(3, 7, [3, 4, 4, 5, 5, 5, 6, 6, 7]), key='Yes'),
              sa('A dot plot has a tall stack of dots in the middle and short, equal stacks on each side.\nWhat is the shape of the distribution?', 'Shape:', key='Symmetric (mound-shaped)'),
              tf('A distribution that looks the same on both sides of its center is symmetric.', key=True),
              tf('A dot plot with all of its dots stacked above one value is skewed left.', key=False),
          ]),
      ],
      f1=B('Compare groups using relative frequencies in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows how students get to school.\nWhat percent of sixth graders walk?', 'Percent:', fig=TRAVEL, key='40%'),
          sa('The table shows how students get to school.\nWhat percent of seventh graders walk?', 'Percent:', fig=TRAVEL, key='25%'),
          mc('The table shows how students get to school.\nIs there evidence that grade and walking are related?',
             ['Yes, because 40% of sixth graders walk but only 25% of seventh graders do.', 'No, because each grade has 60 students.',
              'No, because more students ride than walk in both grades.', 'Yes, because 24 is greater than 15.'], fig=TRAVEL),
          tf('Relative frequencies make it possible to compare groups of different sizes.', key=True),
          tf('If 40% of sixth graders and 40% of seventh graders walk, there is a strong relationship between grade and walking.', key=False),
      ]),
      f2=B('Compare the center and spread of two data sets', 'HSS-ID.A.2', [
          sa('Data set A has a mean of 20 and a standard deviation of 2. Data set B has a mean of 20 and a standard deviation of 6.\nWhich data set is more spread out?', 'Answer:', key='Data set B'),
          sa('Data set A has a median of 45 and an IQR of 10. Data set B has a median of 52 and an IQR of 10.\nCompare the centers and the spreads.', 'Answer:',
             key='B\'s median is 7 greater; the spreads (IQRs) are the same.'),
          mc('Which measure of spread is best for a skewed data set with outliers?', ['Interquartile range', 'Standard deviation', 'Mean', 'Range']),
          tf('Standard deviation measures how spread out the data are around the mean.', key=True),
          tf('Two data sets with the same mean must have the same standard deviation.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.B.4
    S('7.SP.B.4', 'Compare two populations using measures of center and variability from random samples',
      main=[
          sa('Random samples of quiz scores: Class A has a median of 78 and an IQR of 10. Class B has a median of 70 and an IQR of 10.\nWhat do the samples suggest about the two classes? Use both the center and the spread.', 'Answer:',
             key='The samples suggest Class A tends to score higher, by about 8 points (median). The spreads are the same (IQR 10), so the scores overlap and some Class B students may score higher than some Class A students.',
             note='Full credit uses both the centers and the spreads and states a tendency, not a certainty about every student.'),
          sa('A random sample of 7th graders has a mean of 6.5 hours of screen time and a MAD of 1.2. A random sample of 8th graders has a mean of 7.7 hours and a MAD of 1.2.\nWrite the difference in means as a multiple of the MAD. What does this suggest about the two populations?', 'Answer:',
             key='1 MAD. The samples suggest 8th graders tend to have more screen time, but the distributions overlap a lot, so the difference is modest.',
             note='Grade both: 1 MAD, and an inference that uses the overlap.'),
          mc('The box plots show random samples of daily high temperatures in two towns.\nWhich statement is true?',
             ['The median for Town B is 10 degrees greater than the median for Town A.', 'Town A has the greater median.', 'The IQRs differ by 10 degrees.', 'The two towns have the same range.'], fig=TOWNS),
          tf('Random samples from two populations have means of 20 and 30, and each has a MAD of 2. The samples suggest that values in the second population tend to be greater.', key=True),
          tf('A random sample from population A has a mean of 52 and one from population B has a mean of 48, each with a MAD of 10. The samples prove that every member of population A has a greater value than every member of population B.', key=False,
             note='The difference is only 0.4 MAD, and samples can only suggest a tendency.'),
      ],
      back=[
          B('Find the interquartile range', '6.SP.B.5.c', [
              sa('A data set has Q1 = 12 and Q3 = 20.\nWhat is the IQR?', 'IQR:', key='8'),
              sa('Find the IQR.\n2, 4, 6, 8, 10, 12, 14, 16', 'IQR:', key='8'),
              mc('A box plot has Q1 = 30 and Q3 = 55.\nWhat is the IQR?', ['25', '85', '30', '55']),
              tf('The IQR is the difference between Q3 and Q1.', key=True),
              tf('A data set with Q1 = 7 and Q3 = 15 has an IQR of 22.', key=False, note='The IQR is 8.'),
          ]),
          B('Read a box plot', '6.SP.B.4', [
              sa('What is the median of the data in the box plot?', 'Median:', fig=BP, key='10'),
              sa('What is the first quartile (Q1) of the data in the box plot?', 'Q1:', fig=BP, key='6'),
              mc('What is the maximum of the data in the box plot?', ['18', '14', '20', '3'], fig=BP),
              tf('The box of a box plot shows the middle half of the data.', key=True),
              tf('The minimum of the data in the box plot is 6.', fig=BP, key=False, note='The minimum is 3.'),
          ]),
      ],
      f1=B('Identify clusters and outliers in a scatter plot', '8.SP.A.1', nearest=True, qs=[
          sa('Which point in the scatter plot is an outlier?', 'Point:', fig=SC2, key='(8, 1)'),
          mc('A scatter plot has a group of points close together.\nWhat is the group called?', ['A cluster', 'An outlier', 'An intercept', 'A slope']),
          sa('Leaving out the outlier, describe the association in the scatter plot.', 'Association:', fig=SC2, key='A positive linear association'),
          tf('An outlier is a point that is far from the overall pattern of the data.', key=True),
          tf('Every scatter plot has exactly one outlier.', key=False),
      ]),
      f2=B('Interpret differences in center and spread, including the effect of outliers', 'HSS-ID.A.3', [
          sa('A data set is 4, 5, 5, 6, 7, 40.\nWhich better describes its center, the mean or the median? Explain.', 'Answer:', key='The median, because the outlier 40 pulls the mean up.'),
          sa('A data set is 4, 5, 5, 6, 7, 40.\nFind the mean with the outlier and the mean without it. Round a mean that does not end to the nearest tenth.', 'Answer:',
             key='11.2 with the outlier; 5.4 without it', note='The exact values 67/6 and 27/5 are also correct.'),
          mc('Which measure is affected most by an outlier?', ['Mean', 'Median', 'IQR', 'Mode']),
          tf('The median is resistant to outliers.', key=True),
          tf('Removing a very large outlier makes the mean larger.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.5
    S('7.SP.C.5', 'Understand probability as a number from 0 to 1 that shows how likely an event is',
      main=[
          mc('Which probability describes an event that is likely to happen?', ['0.8', '0.1', '0', '0.5']),
          sa('A bag has 5 red marbles and no other marbles.\nWhat is the probability of drawing a red marble?', 'Probability:', key='1'),
          sa('The spinner has 4 equal sections.\nIs landing on Blue likely, unlikely, or neither likely nor unlikely?', 'Answer:', fig=spinner('Blue', 'Blue', 'Blue', 'Red'), key='Likely'),
          tf('An event with a probability of {1/2} is just as likely to happen as not to happen.', key=True),
          tf('A probability of 1.3 means that an event is very likely.', key=False, note='Probabilities are from 0 to 1.'),
      ],
      back=[
          B('Compare two fractions', '4.NF.A.2', [
              sa('Which is greater, {3/8} or {2/3}?', 'Answer:', key='2/3'),
              sa('Write >, <, or =.\n{5/10} ___ {1/2}', 'Symbol:', key='='),
              mc('Which fraction is less than {1/2}?', ['{3/8}', '{5/8}', '{4/6}', '{3/4}']),
              tf('{7/12} > {1/2}', key=True),
              tf('{2/5} > {3/4}', key=False),
          ]),
          B('Place fractions on a number line from 0 to 1', '3.NF.A.2', [
              plot('Plot {3/4} on the number line.', nl(0, 1, 0.25, labels={0: '0', 1: '1'}), key='A point at the third tick mark after 0 (3/4)'),
              sa('A number line from 0 to 1 is split into 4 equal parts.\nWhat fraction is at the first tick mark after 0?', 'Fraction:', key='1/4'),
              mc('Which fraction is halfway between 0 and 1 on a number line?', ['{1/2}', '{1/4}', '{2/1}', '{1/3}']),
              tf('{4/4} is at the same point as 1 on a number line.', key=True),
              tf('{1/3} is farther from 0 than {2/3} is.', key=False),
          ]),
      ],
      f1=B('Find relative frequencies in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows the results of a survey.\nAmong Grade 9 students, what is the relative frequency of playing music?', 'Relative frequency:', fig=MUSIC, key='0.3', note='18/60 or 30% is also correct.'),
          sa('The table shows the results of a survey.\nAmong Grade 10 students, what is the relative frequency of playing music?', 'Relative frequency:', fig=MUSIC, key='0.3', note='12/40 or 30% is also correct.'),
          mc('The table shows the results of a survey.\nWhat is the relative frequency of all students who play music?', ['0.3', '0.18', '0.7', '0.12'], fig=MUSIC),
          tf('In the table, students in both grades play music at the same rate.', fig=MUSIC, key=True),
          tf('In the table, Grade 9 students are more likely than Grade 10 students to play music, because 18 > 12.', fig=MUSIC, key=False,
             note='Both rates are 30%.'),
      ]),
      f2=B('Describe unions, intersections, and complements of events as subsets of a sample space', 'HSS-CP.A.1', [
          sa('A card is drawn at random from cards numbered 1 to 10. Event A is "an even number." Event B is "a number greater than 6."\nList the outcomes in "A and B" (the intersection).', 'Outcomes:', key='8, 10'),
          sa('A card is drawn at random from cards numbered 1 to 10. Event A is "an even number." Event B is "a number greater than 6."\nList the outcomes in "A or B" (the union).', 'Outcomes:', key='2, 4, 6, 7, 8, 9, 10'),
          mc('A card is drawn at random from cards numbered 1 to 10. Event A is "an even number."\nWhich set of outcomes is the complement of A ("not A")?',
             ['1, 3, 5, 7, 9', '2, 4, 6, 8, 10', '1, 2, 3, 4, 5', '7, 8, 9, 10']),
          tf('A card is drawn at random from cards numbered 1 to 10. Event A is "an even number" and event B is "a number greater than 6." Then P(A or B) = {7/10}.', key=True),
          tf('A card is drawn at random from cards numbered 1 to 10. Event A is "an even number" and event B is "a number greater than 6." The intersection of A and B has more outcomes than their union.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.6
    S('7.SP.C.6', 'Estimate a probability from relative frequency and make predictions',
      main=[
          sa('A spinner landed on green 36 times in 120 spins.\nEstimate the probability of landing on green.', 'Probability:', key='0.3', note='36/120 or 3/10 is also correct.'),
          sa('A basketball player made 42 of her last 60 free throws.\nPredict how many she will make in her next 150 free throws.', 'Free throws:', key='105'),
          mc('A coin was flipped 200 times and landed heads 94 times.\nWhat is the relative frequency of heads?', ['0.47', '0.94', '0.53', '0.5']),
          tf('A fair number cube (numbered 1 to 6) is rolled 300 times. About 50 of the rolls should be a 4.', key=True),
          tf('A spinner landed on red 9 out of 10 times. The probability of red must be exactly 0.9.', key=False,
             note='Relative frequency only estimates the probability, and 10 spins is a small number of trials.'),
      ],
      back=[
          B('Use a rate to make a prediction', '6.RP.A.3.b', [
              sa('A team scores 3 goals every 2 games.\nAt this rate, how many goals does it score in 10 games?', 'Goals:', key='15'),
              sa('4 out of every 10 apples in a crate are green.\nAt this rate, how many of 250 apples are green?', 'Apples:', key='100'),
              mc('A machine fills 6 bottles every 4 seconds.\nAt this rate, how many bottles does it fill in 30 seconds?', ['45', '24', '20', '180']),
              tf('At a rate of 2 out of every 5, there are 40 out of every 100.', key=True),
              tf('At a rate of 3 out of every 8, there are 30 out of every 64.', key=False, note='There are 24 out of every 64.'),
          ]),
          B('Compare decimals to thousandths', '5.NBT.A.3.b', [
              sa('Which is greater, 0.47 or 0.5?', 'Answer:', key='0.5'),
              sa('Write >, <, or =.\n0.305 ___ 0.35', 'Symbol:', key='<'),
              mc('Which decimal is the greatest?', ['0.62', '0.6', '0.059', '0.506']),
              tf('0.250 = 0.25', key=True),
              tf('0.09 > 0.1', key=False),
          ]),
      ],
      f1=B('Use relative frequencies in a two-way table to make predictions', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows the results of a survey.\nAmong teens, what is the relative frequency of liking rain?', 'Relative frequency:', fig=RAIN, key='0.225', note='9/40 or 22.5% is also correct.'),
          sa('Use the adults row of the table.\nPredict how many of 200 adults like rain.', 'Adults:', fig=RAIN, key='60'),
          mc('The table shows the results of a survey.\nWhich group has the greater relative frequency of liking rain?', ['Adults', 'Teens', 'They are the same.'], fig=RAIN),
          tf('In the table, the relative frequency of liking rain among all 100 people is 0.27.', fig=RAIN, key=True),
          tf('In the table, the relative frequency of disliking rain among adults is 0.42.', fig=RAIN, key=False, note='It is 42/60 = 0.7.'),
      ]),
      f2=B('Find conditional probabilities from a two-way table', 'HSS-CP.A.4', [
          sa('The table shows students\' favorite pets. A student is chosen at random.\nFind P(dog | Grade 9).', 'Probability:', fig=PETS, key='5/8', note='25/40 or 0.625 is also correct.'),
          sa('The table shows students\' favorite pets. A student is chosen at random.\nFind P(Grade 10 | cat).', 'Probability:', fig=PETS, key='4/7', note='20/35 is also correct.'),
          mc('The table shows students\' favorite pets. A student is chosen at random.\nFind P(cat).', ['{7/16}', '{3/8}', '{1/2}', '{9/16}'], fig=PETS),
          tf('In the table, P(dog | Grade 10) = {1/2}.', fig=PETS, key=True),
          tf('In the table, P(Grade 9 | dog) = {25/40}.', fig=PETS, key=False, note='P(Grade 9 | dog) = 25/45 = 5/9.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.6 (collect data) -- added in 2.0.0
    S('7.SP.C.6', 'Collect data from a chance process and use it to estimate a probability', num=70,
      main=[
          sa('Use these random digits as rolls of a fair number cube. Use only the digits 1 to 6, and skip 0, 7, 8, and 9.\n4 8 2 6 6 1 9 3 5 6 0 2 4 6 1 7 3 6 5 2\nRecord the first 15 rolls. What is the relative frequency of rolling a 6?', 'Answer:',
             key='5 sixes in 15 rolls; 5/15 = 1/3', note='The first 15 rolls are 4, 2, 6, 6, 1, 3, 5, 6, 2, 4, 6, 1, 3, 6, 5. Grade both: the count 5 and the relative frequency 1/3.'),
          sa('A student records 20 flips of a coin:\nH T T H H H T H T T H H T H H T H H T H\nWhat is the relative frequency of heads? Use it to predict the number of heads in 200 flips.', 'Answer:',
             key='12/20 = 0.6; about 120 heads in 200 flips', note='Grade both parts.'),
          work('Roll a number cube (or use a number-cube app) 30 times. Record each result in a tally table. Then find the relative frequency of rolling an even number.', 'Relative frequency:',
               method='A tally table of 30 recorded results, a count of even results (2, 4, 6) that matches the tally, and that count divided by 30. '
                      'Grade the recording and the calculation; the relative frequency does not have to equal 1/2.',
               key='The number of even results ÷ 30 (answers vary)'),
          mc('A student records 50 spins of a spinner: 18 red, 22 blue, and 10 green.\nWhat is the relative frequency of blue?', ['0.44', '0.22', '0.36', '0.5']),
          tf('A student rolls a fair number cube 30 times. Her data must show exactly 5 threes, or she made a mistake.', key=False,
             note='Results vary from the expected 5; any count can happen.'),
      ],
      back=[
          B('Organize data with up to four categories', '2.MD.D.10', [
              sa('A spinner gives these results: R, B, R, G, R, B, R, G, B, R.\nHow many times did it land on R?', 'Times:', key='5'),
              sa('A spinner gives these results: R, B, R, G, R, B, R, G, B, R.\nHow many results are there in all?', 'Results:', key='10'),
              mc('A tally chart shows red 4, blue 3, and green 3.\nHow many results are there in all?', ['10', '4', '7', '9']),
              tf('A tally chart can be used to record results as they happen.', key=True),
              tf('Red has 5 tally marks and blue has 3. Blue has 2 more than red.', key=False),
          ]),
          B('Write fractions with denominators of 10 or 100 as decimals', '4.NF.C.6', [
              sa('Write {6/10} as a decimal.', 'Decimal:', key='0.6'),
              sa('Write {44/100} as a decimal.', 'Decimal:', key='0.44'),
              mc('Which decimal is equal to {35/100}?', ['0.35', '3.5', '0.035', '35']),
              tf('{8/10} = 0.8', key=True),
              tf('{5/100} = 0.5', key=False),
          ]),
      ],
      f1=B('Record results of two chance processes in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('A coin was flipped and a number cube rolled 40 times. The table shows the results.\nWhat is the relative frequency of heads?', 'Relative frequency:', fig=COIN40, key='0.5', note='20/40 is also correct.'),
          sa('A coin was flipped and a number cube rolled 40 times. The table shows the results.\nAmong the heads results, what is the relative frequency of an even number?', 'Relative frequency:', fig=COIN40, key='0.55', note='11/20 is also correct.'),
          mc('A coin was flipped and a number cube rolled 40 times. The table shows the results.\nWhich result happened most often?', ['Tails and odd', 'Heads and even', 'Heads and odd', 'Tails and even'], fig=COIN40),
          tf('In the table, the relative frequency of tails and odd is 0.3.', fig=COIN40, key=True),
          tf('In the table, the relative frequencies of the four results add to more than 1.', fig=COIN40, key=False),
      ]),
      f2=B('Use collected data to judge whether two events seem independent', 'HSS-CP.A.2', [
          sa('A coin was flipped and a number cube rolled 40 times. The table shows the results.\nEstimate P(heads), P(even), and P(heads and even).', 'Estimates:', fig=COIN40, key='0.5, 0.475, and 0.275'),
          sa('A coin was flipped and a number cube rolled 40 times. The table shows the results.\nIs P(heads and even) close to P(heads) × P(even)? What does this suggest?', 'Answer:', fig=COIN40,
             key='0.5 × 0.475 = 0.2375, which is fairly close to 0.275; the data are consistent with independence (small differences are expected by chance).'),
          mc('Events A and B are independent.\nWhich statement must be true?', ['P(A and B) = P(A) × P(B)', 'P(A and B) = P(A) + P(B)', 'P(A) = P(B)', 'P(A or B) = 1']),
          tf('A fair coin is flipped and a fair number cube numbered 1 to 6 is rolled. P(heads and 6) = {1/12}.', key=True),
          tf('Events A and B are independent, with P(A) = 0.5 and P(B) = 0.4. Then P(A and B) = 0.9.', key=False, note='P(A and B) = 0.5 × 0.4 = 0.2.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.7.a
    S('7.SP.C.7.a', 'Develop a uniform probability model and use it to find probabilities',
      main=[
          sa('A fair number cube has faces numbered 1 to 6.\nWhat is the probability of rolling a number greater than 4?', 'Probability:', key='1/3', note='2/6 is also correct.'),
          sa('The spinner has 5 equal sections.\nWhat is the probability of landing on a vowel?', 'Probability:', fig=spinner('A', 'B', 'C', 'D', 'E'), key='2/5'),
          mc('A class has 12 girls and 18 boys. One student is chosen at random.\nWhat is the probability that a girl is chosen?', ['{2/5}', '{3/5}', '{2/3}', '{1/12}']),
          tf('In a uniform probability model, every outcome has the same probability.', key=True),
          tf('A letter is chosen at random from the word MATH. The probability of choosing a vowel is {1/2}.', key=False, note='The probability is 1/4.'),
      ],
      back=[
          B('Write equivalent fractions', '4.NF.A.1', [
              sa('Write a fraction equivalent to {3/12} with a denominator of 4.', 'Fraction:', key='1/4'),
              sa('Write a fraction equivalent to {8/12} with a denominator of 3.', 'Fraction:', key='2/3'),
              mc('Which fraction is equivalent to {4/6}?', ['{2/3}', '{3/4}', '{4/12}', '{6/4}']),
              tf('{5/10} = {1/2}', key=True),
              tf('{2/8} = {1/3}', key=False),
          ]),
          B('Write a fraction for part of a whole', '3.NF.A.1', [
              sa('A spinner has 8 equal parts. 3 of the parts are red.\nWhat fraction of the spinner is red?', 'Fraction:', key='3/8'),
              sa('A bag has 6 equal-size tiles. 1 tile is blue.\nWhat fraction of the tiles is blue?', 'Fraction:', key='1/6'),
              mc('A pizza is cut into 4 equal slices. 3 slices are eaten.\nWhat fraction of the pizza is eaten?', ['{3/4}', '{1/4}', '{4/3}', '{3/6}']),
              tf('One of 6 equal parts is {1/6} of the whole.', key=True),
              tf('Two of 6 equal parts is {2/4} of the whole.', key=False),
          ]),
      ],
      f1=B('Use a function that assigns a probability to each outcome', '8.F.A.1', nearest=True, qs=[
          sa('A spinner has 4 equal sections, A, B, C, and D, and a fair pointer. A probability model assigns a probability to each outcome.\nWrite the model as pairs (outcome, probability). Is it a function? Explain.', 'Answer:',
             key='(A, 1/4), (B, 1/4), (C, 1/4), (D, 1/4). Yes: each outcome is assigned exactly one probability.'),
          sa('A rule assigns (red, 0.5), (blue, 0.3), and (red, 0.2).\nIs this rule a function from outcomes to probabilities? Explain.', 'Answer:',
             key='No. The outcome red is assigned two different probabilities.'),
          mc('A fair number cube numbered 1 to 6 is rolled. The function P gives the probability of each outcome.\nWhat is P(4)?', ['{1/6}', '{4/6}', '4', '{1/4}']),
          tf('A probability model gives exactly one probability to each outcome, just as a function gives exactly one output to each input.', key=True),
          tf('In a function, one input can have two different outputs.', key=False),
      ]),
      f2=B('Use the addition rule for probability', 'HSS-CP.B.7', [
          sa('A card is chosen at random from cards numbered 1 to 10.\nFind P(even or greater than 7).', 'Probability:', key='3/5', note='6/10 or 0.6 is also correct.'),
          sa('P(A) = 0.4, P(B) = 0.5, and P(A and B) = 0.2.\nFind P(A or B).', 'Probability:', key='0.7'),
          mc('A fair number cube numbered 1 to 6 is rolled.\nWhat is P(less than 3 or odd)?', ['{2/3}', '{5/6}', '{1/2}', '{1/3}']),
          tf('If A and B cannot both happen, then P(A or B) = P(A) + P(B).', key=True),
          tf('P(A or B) is always equal to P(A) + P(B).', key=False, note='You subtract P(A and B) when A and B can happen together.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.7.b
    S('7.SP.C.7.b', 'Develop a probability model from observed frequencies',
      main=[
          sa('A bottle cap is tossed 80 times. It lands top-up 52 times.\nEstimate the probability that it lands top-up.', 'Probability:', key='0.65', note='52/80 or 13/20 is also correct.'),
          sa('A spinner with three unequal sections is spun 200 times: red 90 times, blue 70 times, and green 40 times.\nWrite an estimated probability for each color.', 'Probabilities:',
             key='Red 0.45, blue 0.35, green 0.2', note='Equivalent fractions or percents are also correct.'),
          mc('A spinner landed on red 90 times, blue 70 times, and green 40 times in 200 spins.\nWhich is the best prediction for 1,000 spins?', ['About 450 reds', 'About 333 reds', 'About 90 reds', 'About 900 reds']),
          tf('A probability estimated from observed frequencies can change when more trials are done.', key=True),
          tf('A model built from 10 tosses is just as reliable as a model built from 1,000 tosses.', key=False),
      ],
      back=[
          B('Read a scaled bar graph', '3.MD.B.3', [
              sa('The bar graph shows the results of some spins.\nHow many spins landed on red?', 'Spins:', fig=SPINS, key='9'),
              sa('The bar graph shows the results of some spins.\nHow many more spins landed on red than on green?', 'Spins:', fig=SPINS, key='4'),
              mc('The bar graph shows the results of some spins.\nHow many spins are shown in all?', ['20', '9', '15', '11'], fig=SPINS),
              tf('The bar graph shows that blue was spun 6 times.', fig=SPINS, key=True),
              tf('The bar graph shows that green was spun more times than blue.', fig=SPINS, key=False),
          ]),
          B('Write a part of a whole as a percent', '6.RP.A.3.c', [
              sa('Write 45 out of 60 as a percent.', 'Percent:', key='75%'),
              sa('Write 13 out of 50 as a percent.', 'Percent:', key='26%'),
              mc('What percent is 72 out of 120?', ['60%', '72%', '40%', '48%']),
              tf('9 out of 36 is 25%.', key=True),
              tf('14 out of 40 is 14%.', key=False, note='14 out of 40 is 35%.'),
          ]),
      ],
      f1=B('Construct a two-way table from survey counts', '8.SP.A.4', nearest=True, qs=[
          plot('50 students were surveyed. 30 have a phone. 18 of the students with a phone also have a tablet. 8 of the students without a phone have a tablet.\nComplete the two-way table.',
               blank_tw('Phone', 'No phone', 'Tablet', 'No tablet'),
               key='Phone: 18 tablet, 12 no tablet, 30 total. No phone: 8 tablet, 12 no tablet, 20 total. Totals: 26 tablet, 24 no tablet, 50 in all.'),
          plot('40 people were surveyed. 15 have a dog. 6 of the dog owners also have a cat. 10 of the people without a dog have a cat.\nComplete the two-way table.',
               blank_tw('Dog', 'No dog', 'Cat', 'No cat'),
               key='Dog: 6 cat, 9 no cat, 15 total. No dog: 10 cat, 15 no cat, 25 total. Totals: 16 cat, 24 no cat, 40 in all.'),
          plot('60 students were surveyed. 35 play a sport. 20 of the sport players also play an instrument. 30 of the students play an instrument.\nComplete the two-way table.',
               blank_tw('Sport', 'No sport', 'Instrument', 'No instrument'),
               key='Sport: 20 instrument, 15 no instrument, 35 total. No sport: 10 instrument, 15 no instrument, 25 total. Totals: 30 instrument, 30 no instrument, 60 in all.'),
          plot('80 adults were surveyed. 48 drink coffee. 12 of the coffee drinkers also drink tea. 20 adults drink neither coffee nor tea.\nComplete the two-way table.',
               blank_tw('Coffee', 'No coffee', 'Tea', 'No tea'),
               key='Coffee: 12 tea, 36 no tea, 48 total. No coffee: 12 tea, 20 no tea, 32 total. Totals: 24 tea, 56 no tea, 80 in all.'),
          plot('100 students were surveyed: 45 in Grade 7 and 55 in Grade 8. 27 of the Grade 7 students and 22 of the Grade 8 students ride the bus.\nComplete the two-way table.',
               blank_tw('Grade 7', 'Grade 8', 'Bus', 'No bus'),
               key='Grade 7: 27 bus, 18 no bus, 45 total. Grade 8: 22 bus, 33 no bus, 55 total. Totals: 49 bus, 51 no bus, 100 in all.'),
      ]),
      f2=B('Summarize categorical data with relative frequencies', 'HSS-ID.B.5', [
          sa('The table shows the results of a survey.\nWhat is the joint relative frequency of Grade 9 students who play music?', 'Relative frequency:', fig=MUSIC, key='0.18', note='18/100 or 18% is also correct.'),
          sa('The table shows the results of a survey.\nWhat is the marginal relative frequency of students who do not play music?', 'Relative frequency:', fig=MUSIC, key='0.7', note='70/100 or 70% is also correct.'),
          mc('The table shows the results of a survey.\nWhat is the conditional relative frequency of playing music among Grade 10 students?', ['0.3', '0.12', '0.4', '0.7'], fig=MUSIC),
          tf('A marginal relative frequency uses a row total or a column total divided by the grand total.', key=True),
          tf('A conditional relative frequency always divides by the grand total.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.7 (compare model and data)
    S('7.SP.C.7', 'Compare probabilities from a model with observed frequencies and explain any differences',
      main=[
          sa('A fair number cube is rolled 60 times, and a 5 comes up 14 times.\nHow many 5s does the model predict? How does the observed count compare?', 'Answer:',
             key='The model predicts 10 fives; the observed 14 is 4 more than expected.', note='Grade both: 10 expected, and the comparison with 14.'),
          sa('A coin is claimed to be fair. It is flipped 100 times and lands heads 61 times.\nCompare this with the model. Give a possible reason for the difference.', 'Answer:',
             key='The model predicts about 50 heads. Random variation can explain some of the difference, but 61 heads might also mean the coin is not fair.',
             note='Any answer that compares with the expected 50 and gives a reasonable cause (chance variation or an unfair coin).'),
          mc('A spinner has 4 equal sections, one of them yellow. In 80 spins, it lands on yellow 35 times.\nWhich conclusion is best?',
             ['Yellow came up much more than the expected 20 times, so the spinner may not be fair.', 'The results match the model exactly.',
              'Yellow should come up 35 times in every 80 spins.', 'The model predicts 40 yellows.']),
          tf('A good probability model does not have to match observed frequencies exactly.', key=True),
          tf('A coin that lands heads 7 times in 10 flips must be unfair.', key=False),
      ],
      back=[
          B('Find a fraction of a whole number', '5.NF.B.4.a', [
              sa('Find the value.\n{1/6} × 60', 'Value:', key='10'),
              sa('What is {1/4} of 80?', 'Answer:', key='20'),
              mc('What is {2/5} of 50?', ['20', '10', '25', '125']),
              tf('{1/3} of 90 is 30.', key=True),
              tf('{3/4} of 40 is 10.', key=False, note='3/4 of 40 is 30.'),
          ]),
          B('Divide whole numbers to find equal shares', '4.NBT.B.6', [
              sa('Divide.\n240 ÷ 4', 'Quotient:', key='60'),
              sa('Divide.\n300 ÷ 6', 'Quotient:', key='50'),
              mc('Divide.\n1,000 ÷ 8', ['125', '12', '150', '105']),
              tf('500 ÷ 5 = 100', key=True),
              tf('720 ÷ 3 = 24', key=False),
          ]),
      ],
      f1=B('Compare a linear model\'s predictions with observed data', '8.SP.A.3', nearest=True, qs=[
          sa('A model is y = 2x + 1. At x = 4, the observed value is y = 11.\nHow far is the observed value from the prediction?', 'Difference:', key='2', note='The model predicts 9.'),
          sa('A model is y = 5x. At x = 3, the observed value is y = 13.\nIs the model\'s prediction too high or too low, and by how much?', 'Answer:', key='Too high, by 2'),
          mc('Which observed point is closest to the model y = x + 3?', ['(2, 5.2)', '(2, 7)', '(2, 3)', '(2, 9)']),
          tf('A linear model can be useful even when the data points do not all lie on the line.', key=True),
          tf('If one data point is far from the line of fit, the model must be thrown out.', key=False),
      ]),
      f2=B('Judge whether a result is consistent with a model by using a simulation', 'HSS-IC.A.2', [
          sa('A spinner is claimed to land on red 25% of the time. The dot plot shows the number of reds in each of 50 simulated sets of 20 spins under that model. A real spinner lands on red 11 times in 20 spins.\nIs the result consistent with the model? Use the simulation.', 'Answer:',
             fig=SIM_REDS, key='No. 11 or more reds never happened in the 50 simulations, so the result casts doubt on the 25% model.'),
          sa('A spinner is claimed to land on red 25% of the time. The dot plot shows the number of reds in each of 50 simulated sets of 20 spins under that model. A real spinner lands on red 6 times in 20 spins.\nIs the result consistent with the model? Use the simulation.', 'Answer:',
             fig=SIM_REDS, key='Yes. 6 or more reds happened in 20 of the 50 simulations (40%), so 6 reds is not unusual.'),
          mc('The dot plot shows the number of reds in each of 50 simulated sets of 20 spins of a spinner that lands on red 25% of the time.\nWhich real result would be the most surprising under this model?',
             ['10 reds', '6 reds', '4 reds', '5 reds'], fig=SIM_REDS),
          tf('In the simulation shown, 9 or more reds happened in 2 of the 50 sets, about 4% of the time.', fig=SIM_REDS, key=True),
          tf('A real spinner gives 8 reds in 20 spins. Because 8 is more than the expected 5, the simulation shown proves the 25% model is wrong.', fig=SIM_REDS, key=False,
             note='8 or more reds happened in 5 of the 50 simulations (10%), so the result is not very unusual.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.a
    S('7.SP.C.8.a', 'Find the probability of a compound event as the fraction of outcomes in the sample space',
      main=[
          sa('A fair coin is flipped and a fair number cube numbered 1 to 6 is rolled.\nWhat is the probability of getting heads and a 6?', 'Probability:', key='1/12'),
          sa('Two fair coins are flipped.\nWhat is the probability that both land tails?', 'Probability:', key='1/4'),
          mc('The spinner has 3 equal sections and a fair pointer. It is spun twice, and the spins do not affect each other.\nWhat is the probability of landing on A both times?', ['{1/9}', '{1/3}', '{2/3}', '{1/6}'], fig=spinner('A', 'B', 'C')),
          tf('Two fair number cubes numbered 1 to 6 are rolled. The probability that the sum is 7 is {6/36} = {1/6}.', key=True),
          tf('Two fair coins are flipped. The probability of getting one head and one tail is {1/4}.', key=False, note='The probability is 2/4 = 1/2.'),
      ],
      back=[
          B('Multiply fractions', '5.NF.B.4.a', [
              sa('Multiply.\n{1/2} × {1/6}', 'Product:', key='1/12'),
              sa('Multiply.\n{2/3} × {3/4}', 'Product:', key='1/2', note='6/12 is also correct.'),
              mc('Multiply.\n{1/4} × {1/4}', ['{1/16}', '{1/8}', '{2/4}', '{1/2}']),
              tf('{1/3} × {1/2} = {1/6}', key=True),
              tf('{1/5} × {1/5} = {2/5}', key=False),
          ]),
          B('Count pairs with an array: one row for each first choice', '3.OA.A.3', [
          sa('A café has 3 kinds of sandwiches and 4 kinds of drinks. The array has one row for each sandwich and one column for each drink; each dot is one sandwich-and-drink pair.\nHow many pairs are there?', 'Pairs:',
             fig=dict(k='array', rows=3, cols=4, h=170), key='12'),
          sa('Ty has 4 shirts and 5 pairs of pants. The array has one row for each shirt and one column for each pair of pants; each dot is one outfit.\nHow many outfits are there?', 'Outfits:',
             fig=dict(k='array', rows=4, cols=5, h=190), key='20'),
          mc('A shop has 6 ice cream flavors and 2 kinds of cones. Each flavor can go with each cone, so there are 6 rows with 2 choices in each row.\nHow many flavor-and-cone choices are there?', ['12', '8', '6', '3']),
          tf('3 rows of 7 chairs is 21 chairs.', key=True),
          tf('An array has one row for each of 5 hats and one column for each of 3 scarves. It shows 8 hat-and-scarf pairs.', key=False, note='5 rows of 3 is 15 pairs.'),
      ]),
      ],
      f1=B('Find joint relative frequencies in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('The table shows 100 trials of flipping a coin and rolling a number cube.\nWhat is the relative frequency of an even number and heads?', 'Relative frequency:', fig=COINDIE, key='0.24'),
          sa('The table shows 100 trials of flipping a coin and rolling a number cube.\nWhat is the relative frequency of tails?', 'Relative frequency:', fig=COINDIE, key='0.49'),
          mc('The table shows 100 trials of flipping a coin and rolling a number cube.\nWhich result happened most often?', ['Odd and heads', 'Even and heads', 'Even and tails', 'Odd and tails'], fig=COINDIE),
          tf('In the table, the relative frequency of an odd number and tails is 0.23.', fig=COINDIE, key=True),
          tf('The relative frequencies of the four results in the table add to 2.', fig=COINDIE, key=False, note='They add to 1.'),
      ]),
      f2=B('Use the multiplication rule for independent events', 'HSS-CP.A.2', [
          sa('Events A and B are independent. P(A) = 0.3 and P(B) = 0.5.\nFind P(A and B).', 'Probability:', key='0.15'),
          sa('A fair coin is flipped 3 times, and the flips are independent.\nWhat is the probability that all 3 flips are heads?', 'Probability:', key='1/8'),
          mc('A fair number cube numbered 1 to 6 is rolled twice, and the rolls are independent.\nWhat is the probability of rolling two 6s?', ['{1/36}', '{1/6}', '{1/12}', '{2/6}']),
          tf('Events A and B are independent when P(A and B) = P(A) × P(B).', key=True),
          tf('Drawing two cards from a deck without putting the first card back are independent events.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.b
    S('7.SP.C.8.b', 'Represent the sample space of a compound event with a list, a table, or a tree diagram',
      main=[
          sa('A coin is flipped and a spinner with sections 1, 2, and 3 is spun.\nList the sample space.', 'Sample space:', key='H1, H2, H3, T1, T2, T3'),
          sa('A café offers 3 sandwiches (ham, egg, tuna) and 2 drinks (milk, juice).\nMake an organized list of every sandwich-and-drink pair.', 'Sample space:',
             key='ham-milk, ham-juice, egg-milk, egg-juice, tuna-milk, tuna-juice', note='All 6 pairs are required, in any order or format.'),
          plot('Draw a tree diagram for choosing a shirt (red or blue) and then pants (black, tan, or gray). Write the outcome at the end of each branch.', BLANK,
               key='A tree with 2 first branches (red, blue), each splitting into 3 branches (black, tan, gray), ending in 6 outcomes: red-black, red-tan, red-gray, blue-black, blue-tan, blue-gray.'),
          plot('Complete the table to show the sample space for flipping a coin and then rolling a number cube numbered 1 to 6.',
               table([['', '1', '2', '3', '4', '5', '6'], ['H', '', '', '', '', '', ''], ['T', '', '', '', '', '', '']], header='both'),
               key='Row H: H1, H2, H3, H4, H5, H6. Row T: T1, T2, T3, T4, T5, T6 (12 outcomes).'),
          sa('A first coin and a second coin are flipped.\nMake an organized list of the sample space. Then list the outcomes in the event "exactly one head."', 'Answer:',
             key='HH, HT, TH, TT; the event "exactly one head" is HT and TH.', note='Grade both: all 4 outcomes (HT and TH listed separately), and the event HT, TH.'),
      ],
      back=[
          B('Use repeated addition to find the total in an array', '2.OA.C.4', [
              sa('An array has 3 rows with 4 objects in each row.\nWrite an addition equation for the total.', 'Equation:', key='4 + 4 + 4 = 12'),
              sa('An array has 2 rows with 5 objects in each row.\nWrite an addition equation for the total.', 'Equation:', key='5 + 5 = 10'),
              mc('Which equation gives the total of an array with 4 rows of 3?', ['3 + 3 + 3 + 3 = 12', '4 + 3 = 7', '3 + 4 + 3 = 10', '3 + 3 + 3 = 9']),
              tf('An array with 3 rows of 5 has 5 + 5 + 5 = 15 objects.', key=True),
              tf('An array with 2 rows of 4 has 4 + 2 = 6 objects.', key=False),
          ]),
          B('Form ordered pairs from two numerical patterns', '5.OA.B.3', [
              sa('Pattern A starts at 0 and adds 2. Pattern B starts at 0 and adds 4.\nWrite the first 3 ordered pairs (A, B).', 'Ordered pairs:', key='(0, 0), (2, 4), (4, 8)'),
              sa('Pattern A starts at 1 and adds 1. Pattern B starts at 3 and adds 3.\nWrite the first 3 ordered pairs (A, B).', 'Ordered pairs:', key='(1, 3), (2, 6), (3, 9)'),
              mc('Pattern A is 0, 3, 6, 9. Pattern B is 0, 6, 12, 18.\nWhich ordered pair (A, B) comes from these patterns?', ['(6, 12)', '(12, 6)', '(6, 9)', '(3, 3)']),
              tf('In the patterns A: 0, 5, 10 and B: 0, 10, 20, each term in B is twice the matching term in A.', key=True),
              tf('The patterns A: 0, 2, 4 and B: 0, 3, 6 make the ordered pair (4, 3).', key=False, note='They make the pair (4, 6).'),
          ]),
      ],
      f1=B('Organize two categorical variables in a two-way table', '8.SP.A.4', nearest=True, qs=[
          plot('In a class, 14 students have a sibling and 10 do not. 8 of the students with a sibling have a pet. 3 of the students without a sibling have a pet.\nComplete the two-way table.',
               blank_tw('Sibling', 'No sibling', 'Pet', 'No pet'),
               key='Sibling: 8 pet, 6 no pet, 14 total. No sibling: 3 pet, 7 no pet, 10 total. Totals: 11 pet, 13 no pet, 24 in all.'),
          plot('A class has 30 students. 18 like soccer. 12 of the soccer fans also like basketball. 4 of the students who do not like soccer like basketball.\nComplete the two-way table.',
               blank_tw('Soccer', 'No soccer', 'Basketball', 'No basketball'),
               key='Soccer: 12 basketball, 6 no basketball, 18 total. No soccer: 4 basketball, 8 no basketball, 12 total. Totals: 16 basketball, 14 no basketball, 30 in all.'),
          plot('50 shoppers were counted. 20 used a coupon. 15 of the coupon users paid by card. 25 of the shoppers paid by card.\nComplete the two-way table.',
               blank_tw('Coupon', 'No coupon', 'Card', 'Cash'),
               key='Coupon: 15 card, 5 cash, 20 total. No coupon: 10 card, 20 cash, 30 total. Totals: 25 card, 25 cash, 50 in all.'),
          plot('A team played 36 games. It played 20 at home and won 14 of them. It won 22 games in all.\nComplete the two-way table.',
               blank_tw('Home', 'Away', 'Won', 'Lost'),
               key='Home: 14 won, 6 lost, 20 total. Away: 8 won, 8 lost, 16 total. Totals: 22 won, 14 lost, 36 in all.'),
          plot('90 students were surveyed. 40 walk to school, and 25 of them eat breakfast at home. 30 of the students who do not walk eat breakfast at home.\nComplete the two-way table.',
               blank_tw('Walk', 'Do not walk', 'Breakfast', 'No breakfast'),
               key='Walk: 25 breakfast, 15 no breakfast, 40 total. Do not walk: 30 breakfast, 20 no breakfast, 50 total. Totals: 55 breakfast, 35 no breakfast, 90 in all.'),
      ]),
      f2=B('Find a conditional probability as P(A and B) ÷ P(B)', 'HSS-CP.A.3', [
          sa('P(A and B) = 0.12 and P(B) = 0.4.\nFind P(A | B).', 'Probability:', key='0.3'),
          sa('Two fair coins are flipped. At least one landed heads.\nWhat is the probability that both landed heads?', 'Probability:', key='1/3'),
          mc('A fair number cube numbered 1 to 6 is rolled, and the result is even.\nWhat is the probability that it is a 6?', ['{1/3}', '{1/6}', '{1/2}', '{2/3}']),
          tf('If A and B are independent and P(B) > 0, then P(A | B) = P(A).', key=True),
          tf('P(A | B) is always equal to P(B | A).', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.c
    S('7.SP.C.8.c', 'Design and use a simulation to estimate the probability of a compound event',
      main=[
          sa('A player makes 60% of her free throws, and each shot is independent of the others.\nDescribe how to use random digits 0 to 9 to simulate one trial of 2 free throws.', 'Answer:',
             key='Let the digits 0 to 5 stand for a make and 6 to 9 stand for a miss. Choose 2 random digits; each pair of digits is one trial.',
             note='Any plan where 6 of the 10 digits stand for a make, and each trial uses 2 digits, is correct.'),
          sa('A player makes 60% of her free throws; each shot is independent. In the simulation, the digits 0 to 5 mean a make and 6 to 9 mean a miss. Each pair of digits is one trial of 2 shots:\n32  70  15  86  41  09  55  63  27  84\nIn how many trials are both shots made? Estimate the probability that both shots are made.', 'Answer:',
             key='4 trials (32, 15, 41, 55); about 4/10 = 0.4', note='Grade both: the count 4 and the estimate 0.4.'),
          mc('Each of 3 children is equally likely to be a boy or a girl, and the children are independent.\nWhich tool can simulate the 3 children?', ['Flip a fair coin 3 times', 'Roll one number cube once', 'Spin a spinner with 3 unequal parts once', 'Draw one card from a deck']),
          sa('Each of 3 children is independently equally likely to be a boy or a girl. In the simulation, an even digit means a girl and an odd digit means a boy. Each group of 3 digits is one family:\n204  317  856  993  120  448  715  362  091  574\nEstimate the probability that a family has at least 2 girls.', 'Answer:',
             key='5 of the 10 families (204, 856, 120, 448, 362); about 5/10 = 0.5', note='Grade both: the count 5 and the estimate 0.5.'),
          tf('A simulation of 3 children uses even digits for girls and odd digits for boys. Its trials are 246, 135, and 802. Exactly 1 of these 3 trials shows at least 2 girls.', key=False,
             note='246 and 802 each show 3 girls, so 2 trials show at least 2 girls.'),
      ],
      back=[
          B('Display data in a dot plot', '6.SP.B.4', [
              plot('Make a dot plot of the numbers of heads in 8 trials:\n1, 2, 2, 3, 1, 2, 0, 2', dot(0, 3, []),
                   key='Dots above 0: 1, above 1: 2, above 2: 4, above 3: 1'),
              sa('The dot plot shows the number of heads in 10 trials.\nIn how many trials were there 2 or more heads?', 'Trials:', fig=dot(0, 3, [0, 1, 1, 1, 2, 2, 2, 2, 3, 3]), key='6'),
              mc('Which display shows each data value as a dot above a number line?', ['Dot plot', 'Box plot', 'Histogram', 'Bar graph']),
              tf('A dot plot shows every value in a data set.', key=True),
              tf('A box plot shows every value in a data set.', key=False),
          ]),
          B('Compare fractions with the same numerator or the same denominator', '3.NF.A.3.d', [
              sa('Which is greater, {3/8} or {5/8}?', 'Answer:', key='5/8'),
              sa('Write >, <, or =.\n{2/3} ___ {2/6}', 'Symbol:', key='>'),
              mc('Which fraction is less than {4/6}?', ['{3/6}', '{5/6}', '{6/6}', '{4/4}']),
              tf('{1/4} < {1/2}', key=True),
              tf('{3/8} > {4/8}', key=False),
          ]),
      ],
      f1=B('Construct and interpret a scatter plot', '8.SP.A.1', nearest=True, qs=[
          plot('Make a scatter plot of the data in the table.', hrow(tbl('x', [1, 2, 3, 4, 5], 'y', [2, 4, 5, 7, 9]), grid(6, 10)),
               key='Points at (1, 2), (2, 4), (3, 5), (4, 7), and (5, 9)'),
          sa('The table shows x-values 1, 2, 3, 4, 5 and y-values 2, 4, 5, 7, 9.\nDescribe the association between x and y.', 'Association:', key='A positive linear association'),
          mc('What does each point in a scatter plot stand for?', ['One pair of values from the data', 'The mean of the data', 'An outlier', 'The line of fit']),
          tf('A scatter plot shows the relationship between two numerical variables.', key=True),
          tf('All the points in a scatter plot must lie on a straight line.', key=False),
      ]),
      f2=B('Use a simulation to decide whether a difference between treatments is significant', 'HSS-IC.B.5', [
          sa('In an experiment, 40 similar plants were randomly assigned: 20 got a new plant food (Group A) and 20 got none (Group B). Group A grew a mean of 12 cm and Group B a mean of 9 cm. The data were re-randomized 100 times to simulate no treatment effect; a difference of 3 cm or more happened 2 times.\nIs there evidence that the plant food made a difference? Explain.', 'Answer:',
             key='Yes. With random assignment, a difference that large happened by chance only about 2% of the time, so the results give evidence of a treatment effect (but do not prove it).'),
          sa('In the same kind of randomized experiment (plants randomly assigned to plant food or none), the data were re-randomized 100 times to simulate no treatment effect. A difference of 3 cm or more happened 40 times.\nWhat does this suggest about the plant food?', 'Answer:',
             key='The difference could easily be due to chance, so the experiment does not give evidence that the plant food made a difference.'),
          mc('Why are the data re-randomized many times in the simulation?', ['To see what differences happen by chance alone', 'To make the treatment work better', 'To make the mean larger', 'To remove outliers']),
          tf('Random assignment helps make two treatment groups alike before an experiment begins.', key=True),
          tf('A difference between two groups in one experiment is always caused by the treatment.', key=False),
      ])),
]
