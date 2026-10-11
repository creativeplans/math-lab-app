from qb import S, B, sa, mc, tf, plot, table, dot, box, hist, hrow, nl
from common import grid, spinner


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

    # ------------------------------------------------------------------ 7.SP.B.3
    S('7.SP.B.3', 'Describe how much two distributions overlap using the difference in means as a multiple of the MAD',
      main=[
          sa('Team A\'s heights have a mean of 160 cm. Team B\'s heights have a mean of 172 cm. Both teams have a MAD of 4 cm.\nThe difference in the means is how many MADs?', 'MADs:', key='3'),
          sa('Class 1 has a mean quiz score of 82. Class 2 has a mean of 76. Each class has a MAD of 3.\nWrite the difference in means as a multiple of the MAD.', 'Answer:', key='2 MADs'),
          mc('Two data sets have means of 50 and 54. Each has a MAD of 8.\nHow much do the distributions overlap?',
             ['A lot, because the difference is only half of a MAD', 'Not at all, because the means are different', 'Not at all, because the difference is 4 MADs', 'Very little, because the difference is 8 MADs']),
          tf('When the difference in means is several MADs, the two distributions overlap very little.', key=True),
          tf('Two data sets have means of 30 and 40 and a MAD of 10 each. The difference in means is 10 MADs.', key=False, note='It is 1 MAD.'),
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
          sa('Random samples of quiz scores: Class A has a median of 78 and an IQR of 10. Class B has a median of 70 and an IQR of 10.\nWhich class tends to score higher, and by how much (median)?', 'Answer:', key='Class A, by 8 points'),
          sa('A random sample of 7th graders has a mean of 6.5 hours of screen time and a MAD of 1.2. A random sample of 8th graders has a mean of 7.7 hours and a MAD of 1.2.\nWrite the difference in means as a multiple of the MAD.', 'Answer:', key='1 MAD'),
          mc('The box plots show random samples of daily high temperatures in two towns.\nWhich statement is true?',
             ['The median for Town B is 10 degrees greater than the median for Town A.', 'Town A has the greater median.', 'The IQRs differ by 10 degrees.', 'The two towns have the same range.'], fig=TOWNS),
          tf('Random samples are a good way to compare two populations.', key=True),
          tf('Sample A has a greater mean than Sample B. So every value in Sample A is greater than every value in Sample B.', key=False),
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
          sa('A data set is 4, 5, 5, 6, 7, 40.\nWhat is the mean with the outlier, and what is the mean without it?', 'Answer:', key='About 11.2 with the outlier; 5.4 without it'),
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
      f2=B('Describe events as subsets of a sample space', 'HSS-CP.A.1', [
          sa('A number cube is rolled.\nList the outcomes in the event "an even number."', 'Outcomes:', key='2, 4, 6'),
          sa('A number cube is rolled.\nList the outcomes in the complement of the event "a number greater than 4."', 'Outcomes:', key='1, 2, 3, 4'),
          mc('A coin is flipped twice.\nWhat is the sample space?', ['HH, HT, TH, TT', 'HH, TT', 'H, T', 'HH, HT, TT']),
          tf('The probability of an event plus the probability of its complement is 1.', key=True),
          tf('When a number cube is rolled, the events "even number" and "odd number" together include no outcomes.', key=False,
             note='Together they include all six outcomes.'),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.6
    S('7.SP.C.6', 'Estimate a probability from relative frequency and make predictions',
      main=[
          sa('A spinner landed on green 36 times in 120 spins.\nEstimate the probability of landing on green.', 'Probability:', key='0.3', note='36/120 or 3/10 is also correct.'),
          sa('A basketball player made 42 of her last 60 free throws.\nPredict how many she will make in her next 150 free throws.', 'Free throws:', key='105'),
          mc('A coin was flipped 200 times and landed heads 94 times.\nWhat is the relative frequency of heads?', ['0.47', '0.94', '0.53', '0.5']),
          tf('A number cube is rolled 300 times. About 50 of the rolls should be a 4.', key=True),
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

    # ------------------------------------------------------------------ 7.SP.C.7.a
    S('7.SP.C.7.a', 'Develop a uniform probability model and use it to find probabilities',
      main=[
          sa('A number cube has faces numbered 1 to 6.\nWhat is the probability of rolling a number greater than 4?', 'Probability:', key='1/3', note='2/6 is also correct.'),
          sa('The spinner has 5 equal sections.\nWhat is the probability of landing on a vowel?', 'Probability:', fig=spinner('A', 'B', 'C', 'D', 'E'), key='2/5'),
          mc('A class has 12 girls and 18 boys. One student is chosen at random.\nWhat is the probability that a girl is chosen?', ['{2/5}', '{3/5}', '{2/3}', '{1/12}']),
          tf('In a uniform probability model, every outcome has the same probability.', key=True),
          tf('A letter is chosen at random from the word MATH. The probability of choosing a vowel is {1/2}.', key=False, note='The probability is 1/4.'),
      ],
      back=[
          B('Write equivalent fractions', '4.NF.A.1', [
              sa('Write a fraction equivalent to {3/12} with a denominator of 4.', 'Fraction:', key='1/4'),
              sa('Write a fraction equivalent to {10/15} with a denominator of 3.', 'Fraction:', key='2/3'),
              mc('Which fraction is equivalent to {4/6}?', ['{2/3}', '{3/4}', '{4/12}', '{6/4}']),
              tf('{5/10} = {1/2}', key=True),
              tf('{2/8} = {1/3}', key=False),
          ]),
          B('Write a fraction for part of a whole', '3.NF.A.1', [
              sa('A spinner has 8 equal parts. 3 of the parts are red.\nWhat fraction of the spinner is red?', 'Fraction:', key='3/8'),
              sa('A bag has 6 equal-size tiles. 1 tile is blue.\nWhat fraction of the tiles is blue?', 'Fraction:', key='1/6'),
              mc('A pizza is cut into 4 equal slices. 3 slices are eaten.\nWhat fraction of the pizza is eaten?', ['{3/4}', '{1/4}', '{4/3}', '{3/7}']),
              tf('One of 5 equal parts is {1/5} of the whole.', key=True),
              tf('Two of 6 equal parts is {2/4} of the whole.', key=False),
          ]),
      ],
      f1=B('Understand a function as a rule that gives exactly one output for each input', '8.F.A.1', nearest=True, qs=[
          sa('Is the set of pairs (1, 3), (2, 5), (3, 7) a function? Explain.', 'Answer:', key='Yes. Each input has exactly one output.'),
          sa('Is the set of pairs (2, 4), (2, 6), (3, 8) a function? Explain.', 'Answer:', key='No. The input 2 has two different outputs.'),
          mc('Which table shows a function?', ['x: 1, 2, 3 and y: 4, 4, 4', 'x: 1, 1, 2 and y: 3, 5, 7', 'x: 5, 5, 5 and y: 1, 2, 3', 'x: 0, 0, 1 and y: 0, 1, 1']),
          tf('A probability model gives exactly one probability to each outcome, just as a function gives exactly one output to each input.', key=True),
          tf('In a function, one input can have two different outputs.', key=False),
      ]),
      f2=B('Use the addition rule for probability', 'HSS-CP.B.7', [
          sa('A card is chosen at random from cards numbered 1 to 10.\nFind P(even or greater than 7).', 'Probability:', key='3/5', note='6/10 or 0.6 is also correct.'),
          sa('P(A) = 0.4, P(B) = 0.5, and P(A and B) = 0.2.\nFind P(A or B).', 'Probability:', key='0.7'),
          mc('A number cube is rolled.\nWhat is P(less than 3 or odd)?', ['{2/3}', '{5/6}', '{1/2}', '{1/3}']),
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
      f1=B('Construct a two-way table from collected data', '8.SP.A.4', nearest=True, qs=[
          sa('50 students were surveyed. 30 have a phone. 18 of the students with a phone also have a tablet. 8 of the students without a phone have a tablet.\nHow many students have neither a phone nor a tablet?', 'Students:', key='12'),
          sa('50 students were surveyed. 30 have a phone. 18 of the students with a phone also have a tablet. 8 of the students without a phone have a tablet.\nHow many students have a tablet?', 'Students:', key='26'),
          mc('A two-way table has the rows "Phone" and "No phone" and the columns "Tablet" and "No tablet."\nHow many cells show counts for both variables (not totals)?', ['4', '2', '6', '9']),
          tf('A two-way table shows how often each combination of two categories happens.', key=True),
          tf('In a two-way table, the row totals and the column totals add to different grand totals.', key=False),
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
          sa('A fair number cube is rolled 60 times.\nHow many times would you expect to roll a 5?', 'Times:', key='10'),
          sa('A fair coin is flipped 100 times and lands heads 61 times.\nCompare this with the model. Give a possible reason for the difference.', 'Answer:',
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
      f2=B('Decide whether observed results are consistent with a model', 'HSS-IC.A.2', [
          sa('A spinner is claimed to land on red 25% of the time. In 200 spins it lands on red 52 times.\nIs this consistent with the claim? Explain.', 'Answer:', key='Yes. 52 is close to the expected 50.'),
          sa('A number cube is claimed to be fair. In 300 rolls, 6 comes up 120 times.\nIs this consistent with the claim? Explain.', 'Answer:', key='No. The expected number is about 50, and 120 is far more than that.'),
          mc('A model says P(win) = 0.1. Which number of wins in 50 games would cast the most doubt on the model?', ['20', '5', '4', '6']),
          tf('A simulation can show the range of results that a model usually produces.', key=True),
          tf('Any difference between observed and expected results proves that a model is wrong.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.a
    S('7.SP.C.8.a', 'Find the probability of a compound event as the fraction of outcomes in the sample space',
      main=[
          sa('A coin is flipped and a number cube is rolled.\nWhat is the probability of getting heads and a 6?', 'Probability:', key='1/12'),
          sa('Two coins are flipped.\nWhat is the probability that both land tails?', 'Probability:', key='1/4'),
          mc('The spinner has 3 equal sections. It is spun twice.\nWhat is the probability of landing on A both times?', ['{1/9}', '{1/3}', '{2/3}', '{1/6}'], fig=spinner('A', 'B', 'C')),
          tf('Two number cubes are rolled. The probability that the sum is 7 is {6/36} = {1/6}.', key=True),
          tf('Two coins are flipped. The probability of getting one head and one tail is {1/4}.', key=False, note='The probability is 2/4 = 1/2.'),
      ],
      back=[
          B('Multiply fractions', '5.NF.B.4.a', [
              sa('Multiply.\n{1/2} × {1/6}', 'Product:', key='1/12'),
              sa('Multiply.\n{2/3} × {3/4}', 'Product:', key='1/2', note='6/12 is also correct.'),
              mc('Multiply.\n{1/4} × {1/4}', ['{1/16}', '{1/8}', '{2/4}', '{1/2}']),
              tf('{1/3} × {1/2} = {1/6}', key=True),
              tf('{1/5} × {1/5} = {2/5}', key=False),
          ]),
          B('Use multiplication to count combinations in equal groups', '3.OA.A.3', [
              sa('A café has 3 kinds of sandwiches and 4 kinds of drinks.\nHow many different sandwich-and-drink pairs can be made?', 'Pairs:', key='12'),
              sa('Ty has 4 shirts and 5 pairs of pants.\nHow many different shirt-and-pants outfits can he make?', 'Outfits:', key='20'),
              mc('A shop has 6 ice cream flavors and 2 kinds of cones.\nHow many different flavor-and-cone choices are there?', ['12', '8', '6', '3']),
              tf('3 rows of 7 chairs is 21 chairs.', key=True),
              tf('5 hats and 3 scarves make 8 different hat-and-scarf pairs.', key=False, note='They make 15 pairs.'),
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
          sa('A fair coin is flipped 3 times.\nWhat is the probability that all 3 flips are heads?', 'Probability:', key='1/8'),
          mc('A fair number cube is rolled twice.\nWhat is the probability of rolling two 6s?', ['{1/36}', '{1/6}', '{1/12}', '{2/6}']),
          tf('Events A and B are independent when P(A and B) = P(A) × P(B).', key=True),
          tf('Drawing two cards from a deck without putting the first card back are independent events.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.b
    S('7.SP.C.8.b', 'Represent the sample space of a compound event with a list, a table, or a tree diagram',
      main=[
          sa('A coin is flipped and a spinner with sections 1, 2, and 3 is spun.\nList the sample space.', 'Sample space:', key='H1, H2, H3, T1, T2, T3'),
          sa('A café has 3 sandwiches and 4 drinks.\nHow many outcomes are in the sample space for choosing one sandwich and one drink?', 'Outcomes:', key='12'),
          mc('A tree diagram shows choosing a shirt (red or blue) and then pants (black, tan, or gray).\nHow many branches are at the end of the tree?', ['6', '5', '3', '2']),
          tf('"Roll a 3 and get tails" is one outcome in the sample space for rolling a number cube and flipping a coin.', key=True),
          tf('The sample space for flipping two coins is HH, HT, TT.', key=False, note='TH is missing.'),
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
      f1=B('Organize the outcomes of two categorical variables in a two-way table', '8.SP.A.4', nearest=True, qs=[
          sa('In a class, 14 students have a sibling and 10 do not. 8 of the students with a sibling have a pet. 3 of the students without a sibling have a pet.\nHow many students have a sibling but no pet?', 'Students:', key='6'),
          sa('In a class, 14 students have a sibling and 10 do not. 8 of the students with a sibling have a pet. 3 of the students without a sibling have a pet.\nHow many students have a pet?', 'Students:', key='11'),
          mc('A two-way table has the rows "Sibling" and "No sibling" and the columns "Pet" and "No pet."\nHow many outcome cells (not totals) does it have?', ['4', '2', '6', '9']),
          tf('A two-way table can show the counts for two categorical variables at the same time.', key=True),
          tf('A two-way table with 3 rows and 2 columns of outcomes has 5 outcome cells.', key=False, note='It has 3 × 2 = 6 outcome cells.'),
      ]),
      f2=B('Find a conditional probability as P(A and B) ÷ P(B)', 'HSS-CP.A.3', [
          sa('P(A and B) = 0.12 and P(B) = 0.4.\nFind P(A | B).', 'Probability:', key='0.3'),
          sa('Two coins are flipped. At least one landed heads.\nWhat is the probability that both landed heads?', 'Probability:', key='1/3'),
          mc('A number cube is rolled, and the result is even.\nWhat is the probability that it is a 6?', ['{1/3}', '{1/6}', '{1/2}', '{2/3}']),
          tf('If A and B are independent, then P(A | B) = P(A).', key=True),
          tf('P(A | B) is always equal to P(B | A).', key=False),
      ])),

    # ------------------------------------------------------------------ 7.SP.C.8.c
    S('7.SP.C.8.c', 'Design and use a simulation to estimate the probability of a compound event',
      main=[
          sa('A player makes 60% of her free throws.\nDescribe how to use random digits 0 to 9 to simulate one trial of 2 free throws.', 'Answer:',
             key='Let the digits 0 to 5 stand for a make and 6 to 9 stand for a miss. Choose 2 random digits; each pair of digits is one trial.',
             note='Any plan where 6 of the 10 digits stand for a make, and each trial uses 2 digits, is correct.'),
          sa('In a simulation with 50 trials, 18 trials showed both free throws made.\nEstimate the probability that both are made.', 'Probability:', key='0.36', note='18/50 or 9/25 is also correct.'),
          mc('Each of 3 children is equally likely to be a boy or a girl.\nWhich tool can simulate the 3 children?', ['Flip a coin 3 times', 'Roll one number cube once', 'Spin a spinner with 3 unequal parts once', 'Draw one card from a deck']),
          tf('Running more trials of a simulation usually gives a better estimate of a probability.', key=True),
          tf('A single spin of a spinner with 4 equal sections can simulate an event with a probability of {1/3}.', key=False,
             note='Four equal sections give probabilities in fourths; use 3 equal sections instead.'),
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
              tf('{3/5} > {4/5}', key=False),
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
          sa('Plants in Group A grew a mean of 12 cm and plants in Group B grew a mean of 9 cm. In 100 re-randomizations of the data, a difference of 3 cm or more happened 2 times.\nIs the difference likely due to the treatment? Explain.', 'Answer:',
             key='Yes. A difference that large happened by chance only about 2% of the time.'),
          sa('In 100 re-randomizations of the data, a difference of 3 cm or more happened 40 times.\nWhat does this suggest?', 'Answer:', key='The difference could easily be due to chance.'),
          mc('Why are the data re-randomized many times in the simulation?', ['To see what differences happen by chance alone', 'To make the treatment work better', 'To make the mean larger', 'To remove outliers']),
          tf('Random assignment helps make two treatment groups alike before an experiment begins.', key=True),
          tf('A difference between two groups in one experiment is always caused by the treatment.', key=False),
      ])),
]
