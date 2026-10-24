"""S-ID.4, S-IC, S-MD.6-7: the normal distribution, inference, and decisions (sets 61-72).
Simulation results shown in histograms were generated with the seeded script simulations.py (same folder)."""
from qb import S, B, sa, mc, tf, hist
from common import why, proof, PR, EXP, tbl

TECH = ' A calculator may be used.'

ZT = tbl(['z', '-1.5', '-1', '-0.5', '0', '0.5', '1', '1.5', '2'],
         [['Area to the left', '0.0668', '0.1587', '0.3085', '0.5000', '0.6915', '0.8413', '0.9332', '0.9772']])
ER = ' Use the 68-95-99.7 rule.'
SD2 = ' Use the convention that the margin of error is 2 standard deviations of the simulated statistic (a 95% range).'
CUT = ' Use 5% as the cutoff for unusual.'

SKEW = hist(['0–20', '20–40', '40–60', '60–80', '80–100', '100–120', '120–140'], [48, 27, 12, 6, 4, 2, 1], ymax=50, ystep=10,
            xlabel='Household income (thousands of dollars)', ylabel='Number of households')
MOUND = hist(['150–155', '155–160', '160–165', '165–170', '170–175', '175–180', '180–185'], [3, 11, 24, 31, 22, 7, 2], ymax=35, ystep=5,
             xlabel='Height (cm)', ylabel='Number of people')
BIMODAL = hist(['100–110', '110–120', '120–130', '130–140', '140–150', '150–160', '160–170', '170–180'], [6, 14, 9, 3, 2, 8, 15, 7], ymax=16, ystep=2,
               xlabel='Height (cm)', ylabel='Number of people')
FLAT = hist(['1', '2', '3', '4', '5', '6'], [99, 102, 97, 101, 100, 101], ymax=120, ystep=20, xlabel='Die roll', ylabel='Frequency')

COIN = hist(['≤19', '20–22', '23–25', '26–28', '29–31', '32–33', '≥34'], [12, 35, 66, 51, 27, 6, 3], ymax=70, ystep=10,
            xlabel='Heads in 50 fair flips (200 simulated runs)', ylabel='Number of runs')
SPIN = hist(['≤4', '5–6', '7–8', '9–10', '11–12', '13–14', '≥15'], [5, 20, 32, 62, 47, 20, 14], ymax=70, ystep=10,
            xlabel='Reds in 40 spins with P(red) = 0.25 (200 runs)', ylabel='Number of runs')
DIE = hist(['≤5', '6–7', '8–9', '10–11', '12–13', '14–15', '≥16'], [8, 44, 49, 51, 33, 12, 3], ymax=60, ystep=10,
           xlabel='Sixes in 60 fair rolls (200 runs)', ylabel='Number of runs')
FT = hist(['≤9', '10–11', '12–13', '14–15', '16–17', '18–20'], [6, 18, 48, 85, 36, 7], ymax=90, ystep=10,
          xlabel='Shots made out of 20 with P(make) = 0.7 (200 runs)', ylabel='Number of runs')
BIRTH = hist(['≤41', '42–45', '46–49', '50–53', '54–57', '≥58'], [9, 30, 58, 52, 32, 19], ymax=60, ystep=10,
             xlabel='Boys in 100 births with P(boy) = 0.5 (200 runs)', ylabel='Number of runs')
PROP = hist(['<0.46', '0.46–0.49', '0.50–0.53', '0.54–0.57', '0.58–0.61', '0.62–0.65', '0.66–0.69', '≥0.70'], [2, 3, 31, 60, 58, 34, 9, 3], ymax=60, ystep=10,
            xlabel='Sample proportion (200 simulated samples of 100)', ylabel='Number of samples')
BOOT = hist(['<6.40', '6.40–6.54', '6.55–6.69', '6.70–6.84', '6.85–6.99', '7.00–7.14', '≥7.15'], [3, 14, 38, 45, 59, 31, 10], ymax=60, ystep=10,
            xlabel='Mean sleep (h) in 200 resamples of size 40', ylabel='Number of resamples')
RERAND = hist(['< -2', '-2 to -1', '-1 to 0', '0 to 1', '1 to 2', '2 to 3', '≥ 3'], [0, 29, 74, 66, 27, 4, 0], ymax=80, ystep=10,
              xlabel='Difference in means (cm) in 200 re-randomizations', ylabel='Count')

SETS = [
    # ------------------------------------------------------------------ 61. ID.A.4 estimate with a normal model
    S('HSS-ID.A.4', 'Estimate population percentages with a normal distribution',
      target='Use the mean and standard deviation of a normal model, with the 68-95-99.7 rule or a table, to estimate a population percentage', strand='core', covers=['ID4-estimate'],
      main=[
          sa('Adult women\'s heights are approximately normal with mean 64 in and standard deviation 2.5 in. Estimate the percent between 59 and 69 inches.' + ER, 'Answer:', key='95%',
             note='Any equivalent form. 59 and 69 are 2 standard deviations from the mean.'),
          sa('Adult women\'s heights are approximately normal with mean 64 in and standard deviation 2.5 in. Estimate the percent of women taller than 66.5 inches.' + ER, 'Answer:', key='16%', note='Any equivalent form. (100 - 68)/2.'),
          sa('Test scores are approximately normal with mean 500 and standard deviation 100. Estimate the percent of scores between 400 and 700.' + ER, 'Answer:', key='81.5%',
             note='Any equivalent form. 34 + 34 + 13.5.'),
          sa('Battery life is approximately normal with mean 40 h and standard deviation 4 h. Use the table to estimate the percent of batteries lasting less than 46 hours.', 'Answer:',
             key='93.32%', fig=ZT, note='Any equivalent form. z = 1.5.'),
          sa('Cereal box weights are approximately normal with mean 16.0 oz and standard deviation 0.2 oz. Use the table to estimate the percent between 15.8 and 16.3 oz.', 'Answer:',
             key='77.45%', fig=ZT, note='Any equivalent form. z from -1 to 1.5: 0.9332 - 0.1587.'),
      ],
      back=[
          B('Interpret mean and standard deviation', 'HSS-ID.A.2', [
              sa('A data set has mean 64 and standard deviation 2.5. What value is one standard deviation above the mean?', 'Answer:', key='66.5', note='Any equivalent form.'),
              sa('Which value is two standard deviations below a mean of 500 with standard deviation 100?', 'Answer:', key='300', note='Any equivalent form.'),
              tf('A larger standard deviation means the data are more spread out.', key=True, note='Spread.'),
              mc('46 is how many standard deviations above a mean of 40 when the standard deviation is 4?', ['1.5', '6', '4', '0.67'], note='(46 - 40)/4.'),
              sa('Compute (15.8 - 16.0)/0.2.', 'Answer:', key='-1', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot locate values in standard deviations.', 'normal estimates depend on z-scores.', 'measures distance in standard deviations.')),
          B('Describe the shape of a distribution', 'HSS-ID.A.1', [
              mc('Which describes a histogram that is highest in the middle and falls off evenly on both sides?', ['symmetric and mound-shaped', 'skewed right', 'uniform', 'bimodal'], note='Bell-shaped.'),
              mc('In a symmetric distribution, how do the mean and the median compare?', ['They are about equal, both at the center.', 'The mean is much larger than the median.', 'The median is much larger than the mean.', 'They are at opposite ends of the data.'],
                 note='Symmetry puts both measures at the center.'),
              tf('A normal curve is symmetric about its mean.', key=True, note='Bell shape.'),
              mc('A bell-shaped histogram is called', ['mound-shaped and symmetric', 'skewed right', 'uniform', 'bimodal'], note='Shape vocabulary.'),
              sa('A continuous distribution is symmetric about its median. What percent of the distribution lies below the median? Give a percent.', 'Answer:', key='50%', note='The median splits the area in half.'),
          ], align='supporting',
            why=why('the student does not know the normal shape.', 'the rule only fits mound-shaped data.', 'describes shapes.')),
          B('Percents of a whole', '6.RP.A.3.c', [
              sa('Find 95% of 2,000.', 'Answer:', key='1900', note='Any equivalent form.'),
              sa('What is 34% + 13.5%?', 'Answer:', key='47.5%', note='Any equivalent form.'),
              tf('Half of 68% is 36%.', key=False, note='68/2 = 34.'),
              mc('100% - 95% split equally into two tails gives each tail', ['2.5%', '5%', '47.5%', '0.5%'], note='5/2.'),
              sa('Write 0.7745 as a percent.', 'Answer:', key='77.45%', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot combine percents.', 'estimates add and split percents.', 'computes percents.')),
      ],
      f1=B('Find values from percentiles of a normal model', 'HSS-ID.A.4', [
          sa("Women's heights are approximately normal with mean 64 inches and standard deviation 2.5 inches. Above what height are the tallest 2.5% of women? Give the height in inches." + ER, 'Answer:', key='69',
             note='2.5% lies above mean + 2 SD = 64 + 5 = 69.'),
          sa('Battery life is approximately normal with mean 40 hours and standard deviation 4 hours. Use the table to find the battery life at the 84th percentile, in hours.', 'Answer:', key='44', fig=ZT,
             note='The table gives area 0.8413 at z = 1, so 40 + 4 = 44.'),
          tf('In a normal model, the median equals the mean.', key=True, note='Symmetry.'),
          mc('The 16th percentile of scores with mean 500 and SD 100 is', ['400', '340', '600', '484'], note='One SD below.'),
          sa('A cereal box below 15.7 oz is rejected. Use the table to estimate the percent rejected (mean 16.0, SD 0.2).', 'Answer:', key='6.68%', fig=ZT, note='Any equivalent form. z = -1.5.'),
      ], prog='same-course deepening', demand='Reverse the estimate: find the value that corresponds to a given percent.'),
      f2=B('Use a normal model for a margin of error', 'HSS-IC.B.4', [
          sa('Simulated sample proportions are approximately normal with mean 0.58 and standard deviation 0.049. Using the 68-95-99.7 rule, within what interval do about 95% of them fall?', ['Lower end:', 'Upper end:'], key='0.482; 0.678',
             note='Form required: both. 0.58 ± 2(0.049).'),
          sa('Simulated sample proportions from random samples of 100 have standard deviation 0.049. What margin of error does this give for the population proportion? Give a decimal.' + SD2, 'Answer:', key='0.098',
             note='2 × 0.049 = 0.098.'),
          tf('When a simulated statistic is approximately normal and the margin of error is defined as the half-width of a 95% range, the margin of error is about two standard deviations of the simulated statistic.', key=True,
             note='About 95% of a normal distribution is within 2 SD of the mean.'),
          mc('Simulated sample means are approximately normal with standard deviation 0.2 hours. Using a margin of error of 2 standard deviations (the 95% convention), the margin of error is', ['0.4 hours', '0.2 hours', '0.1 hours', '2 hours'],
             note='2 × 0.2 = 0.4. The others use 1 SD, half an SD, or 10 SD.'),
          mc('Why can the 68-95-99.7 rule be used to find a 95% range for simulated sample proportions from large random samples?', [
                        'For large enough samples their distribution is approximately normal, so about 95% fall within 2 SD of the mean.',
                        'Sample proportions are exactly normal for every sample size, so the rule needs no conditions at all.',
                        'The population values must be normal, even though the sample proportions themselves are not normal.',
                        'The 68-95-99.7 rule applies to every histogram, whatever its shape, so no check is needed.'],
                       note='The normal model is an approximation that works when the simulated distribution is mound-shaped and symmetric. The others require the population to be normal, claim exact normality for every sample size, or apply the rule to any shape.'),
      ], prog='cross-standard extension', demand='Apply the 95% normal range to the sampling distribution of a statistic.',
        builds='Builds on FORWARD 1: finding cutoffs for 95% of a population becomes finding a 95% range for a statistic.')),

    # ------------------------------------------------------------------ 62. ID.A.4 judge when a normal model fits
    S('HSS-ID.A.4', 'Recognize data sets for which a normal model is not appropriate',
      target='Decide from a graph or summary whether a normal model is appropriate for a data set, and justify the decision', strand='core', covers=['ID4-judge'],
      main=[
          mc('The histogram shows household incomes in a town. Is a normal model appropriate?', [
              'No: the distribution is strongly skewed right, not symmetric and mound-shaped.',
              'Yes: it has a single peak, and any single-peaked distribution is normal.',
              'Yes: incomes are measured in dollars, and measurements are always normal.',
              'No: it has two separate peaks, so it is bimodal rather than normal.'], fig=SKEW,
             note='The long right tail rules out a normal model.'),
          mc('The histogram shows heights of adults in a club. Is a normal model appropriate?', [
              'Yes: it is roughly symmetric and mound-shaped with a single peak.',
              'No: the bars are not exactly equal on both sides of the peak.',
              'No: it is strongly skewed right with a long tail to the right.',
              'No: it has two separate peaks, one for each group in the club.'], fig=MOUND,
             note='Approximate symmetry and one peak support a normal model.'),
          mc('The histogram shows heights of all people at a school event (children and adults). Is a normal model appropriate?', [
              'No: it has two peaks, from two different groups combined.',
              'Yes: it is roughly symmetric about its middle, so it is normal.',
              'Yes: heights of people are always approximately normal.',
              'No: it is uniform, with all of the bars the same height.'], fig=BIMODAL,
             note='A bimodal shape is not normal.'),
          mc('Waiting times at a clinic have mean 4 minutes, standard deviation 5 minutes, and minimum 0. Is a normal model appropriate?', [
              'No: a normal model would put about 16% of times below 4 - 5 = -1 minute, which is impossible.',
              'Yes: the mean and the standard deviation are both positive, so a normal model fits the times.',
              'Yes: a normal model can describe any data set once its mean and standard deviation are known.',
              'No: a normal model requires the standard deviation to be smaller than 1 for any data set.'],
             note='About 16% of a normal model lies below mean - 1 SD. The data must be skewed right.'),
          mc('The histogram shows the results of 600 rolls of a fair die. Is a normal model appropriate?', [
              'No: it is roughly uniform (flat), not mound-shaped.',
              'Yes: it is symmetric about 3.5, so it is normal.',
              'Yes: results of dice are always approximately normal.',
              'No: it is strongly skewed left with a long tail.'], fig=FLAT,
             note='Symmetric is not enough; the shape is flat.'),
      ],
      back=[
          B('Describe skewed, symmetric, bimodal, and uniform shapes', 'HSS-ID.A.3', [
              mc('A histogram has a long tail to the right. Which describes its shape?', ['skewed right', 'skewed left', 'symmetric', 'uniform'], note='The tail names the skew.'),
              mc('A histogram has two separate peaks. Which describes its shape?', ['bimodal', 'uniform', 'skewed left', 'symmetric with one peak'], note='Two modes.'),
              tf('In a right-skewed distribution, the mean is usually less than the median.', key=False, note='The long right tail pulls the mean above the median.'),
              mc('A histogram with bars all about the same height is', ['uniform', 'skewed left', 'bimodal', 'normal'], note='Flat.'),
              mc('Which measure of center is more resistant to a long tail?', ['the median', 'the mean', 'both equally', 'the maximum'], note='The median depends only on the middle values.'),
          ], align='exact',
            why=why('the student cannot name a shape.', 'the decision depends on the shape.', 'names distribution shapes.')),
          B('Measures of center and spread for a data set', '6.SP.A.2', [
              mc('What does the standard deviation of a data set describe?', ['how spread out the values are around the mean', 'the most common value in the data set', 'the middle value when the data are in order', 'the number of values in the data set'], note='Spread.'),
              tf('A data set has all values at least 0 and mean 4. Some value in the data set can be more than 4 below the mean.', key=False, note='A value more than 4 below 4 would be negative.'),
              tf('A distribution can be described by its center, spread, and shape.', key=True, note='Three features.'),
              mc('Which is a measure of center?', ['median', 'range', 'IQR', 'standard deviation'], note='Center.'),
              sa('Give one value two standard deviations below a mean of 4 with SD 5.', 'Answer:', key='-6', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot use summaries.', 'one item is judged from numbers alone.', 'uses center and spread.')),
          B('Groups combined in one data set', 'HSS-ID.A.1', [
              mc('Two groups with very different centers are combined into one data set. What will the histogram of the combined data most likely show?', ['two peaks', 'one peak exactly in the middle', 'a flat shape', 'a long right tail only'],
                 note='Each group forms its own peak.'),
              mc('Which data set is most likely to have a histogram with two peaks?', ['heights of 5-year-olds and their parents together', 'heights of the parents only', 'heights of the 5-year-olds only', 'ages of students in one 10th-grade class'],
                 note='Two groups with different centers are combined.'),
              tf('A histogram of one group can look different from a histogram of two groups combined.', key=True, note='Mixtures.'),
              mc('A bimodal histogram suggests', ['two groups in the data', 'an error in counting', 'a normal model', 'a small standard deviation'], note='Two populations.'),
              mc('Heights of all people at a school event (young children and adults) form a two-peaked histogram. Which change is most likely to give mound-shaped distributions?', [
                                'Make separate histograms for the children and for the adults.', 'Round every height in the combined data to the nearest centimeter.', 'Remove the tallest person from the combined data.', 'Add more children to the combined data set.'],
                               note='Separating the groups removes the second peak.'),
          ], align='supporting',
            why=why('the student does not see why two peaks occur.', 'a normal model fits one population.', 'recognizes mixtures.')),
      ],
      f1=B('Check a normal model with the 68-95-99.7 rule', 'HSS-ID.A.4', [
          mc('In 1,000 measurements, 70% are within 1 SD of the mean and 96% are within 2 SDs. Is a normal model reasonable?', [
              'Yes: 70% and 96% are close to the normal 68% and 95%.', 'No: the percents must be exactly 68% and 95%.', 'No: 96% is more than 95%, so the data cannot be normal.', 'Yes: any data set with 1,000 values is normal.'],
             note='Approximate agreement with 68-95 supports the model.'),
          mc('A data set has 85% of its values within 1 SD of the mean and 91% within 2 SDs. Is a normal model reasonable?', [
              'No: 85% is far above 68% and 91% is below 95%.', 'Yes: both percents are above 50%.', 'Yes: 91% is close to 95%, so 85% does not matter.', 'No: a normal model needs 100% within 2 SDs.'],
             note='Both percents disagree with the normal model.'),
          tf('If a data set has an extreme outlier, the normal model may still fit the rest but the mean and SD are distorted.', key=True, note='Outliers affect mean and SD.'),
          mc('About what percent of normal data lies more than 3 SDs from the mean?', ['0.3%', '3%', '5%', '32%'], note='100 - 99.7.'),
          sa('A data set of 200 values has 25 values more than 2 SDs from the mean. What percent of the values is that, and about what percent does the 68-95-99.7 rule predict for a normal model?', ['Observed percent:', 'Normal model percent:'], key='12.5%; 5%',
             note='Form required: both. 25/200 = 12.5%, far more than 5%, so a normal model does not fit.'),
      ], prog='same-course deepening', demand='Use percents within 1 and 2 SDs as numerical evidence for or against normality.'),
      f2=B('Decide whether a probability model fits observed data', 'HSS-IC.A.2', [
          mc('A spinner is claimed to land on each of 4 colors equally often. In 400 spins the counts are 98, 105, 97, 100. Are the results consistent with the claim?', [
              'Yes: each count is close to the expected 100.', 'No: the counts are not all exactly 100.', 'No: 105 proves the spinner favors one color.', 'Yes: any 4 counts adding to 400 are consistent.'],
             note='Small chance variation around 100 is expected.'),
          mc('A model says a coin is fair. In 50 flips there were 34 heads. In 200 simulated runs of 50 fair flips, 3 runs had 34 or more heads.' + CUT + ' What do you conclude?', [
                        '1.5% < 5%: unusual for a fair coin, so evidence against the model.', '1.5% < 5%: this proves the coin is unfair.', '1.5% is not unusual, so the data show that the fair-coin model fits.', 'No simulated run had exactly 34 heads, so a fair coin has probability 0 of giving 34.'],
                       note='3/200 = 1.5%. Evidence is not proof, and a rare result is not impossible.'),
          tf('A model is rejected only if the observed result would be unusual under the model.', key=True, note='Logic of the test.'),
          mc('Under a model, a simulated result at least as extreme as the observed one occurs in 34 of 200 runs.' + CUT + ' The model is', ['consistent with the data', 'proved true', 'rejected', 'impossible'],
             note='17% is not unusual; consistency is not proof.'),
          mc('How does judging a normal model for a data set differ from judging a probability model with a simulation?', [
                        'The first compares the shape of the data with a normal curve; the second asks whether an observed result is unusual among simulated results.',
                        'The first uses many simulated runs of the model; the second only compares the shape of the histogram with a bell curve.',
                        'Both check whether the data form a bell curve; the simulation just repeats the same comparison many more times.',
                        'Both compare the sample mean with the population mean and ignore the shape of the data and the simulation.'],
                       note='Shape check versus how-unusual check. The others swap the two methods, describe both as the same shape check, or describe a comparison of means that neither method makes.'),
      ], prog='cross-standard extension', demand='Move from judging a distribution\'s shape to judging a model\'s consistency with observed results.',
        builds='Builds on FORWARD 1: comparing observed percents with model percents is extended to simulated outcomes.')),

    # ------------------------------------------------------------------ 63. IC.A.1 statistics as inference
    S('HSS-IC.A.1', 'Distinguish population, sample, parameter, and statistic',
      target='Identify the population, sample, parameter, and statistic in a study and explain what a random sample allows one to conclude', strand='core', covers=['IC1-infer'],
      main=[
          mc('A city surveys 400 randomly chosen residents, and 62% of them support a new park. Which identifies the population, sample, parameter, and statistic correctly?', [
              'Population: all residents; sample: the 400 surveyed; parameter: percent of all residents in support; statistic: 62%.',
              'Population: the 400 surveyed; sample: all residents; parameter: 62%; statistic: percent of all residents in support.',
              'Population: all residents; sample: the 400 surveyed; parameter: 62%; statistic: percent of all residents in support.',
              'Population: all residents; sample: the 62% who support it; parameter: 400; statistic: 62%.'],
             note='A parameter describes the population; a statistic describes the sample.'),
          mc("A factory measures 50 randomly selected bolts from a day's production; their mean length is 5.02 cm. Which identifies the parameter and the statistic?", [
              'Parameter: the mean length of all bolts made that day; statistic: 5.02 cm, the mean of the 50 bolts.',
              'Parameter: 5.02 cm, the mean of the 50 bolts; statistic: the mean length of all bolts made that day.',
              'Parameter: the 50 bolts that were measured; statistic: all of the bolts that were made that day.',
              'Parameter: the number of bolts measured, 50; statistic: the mean length of those bolts, 5.02 cm.'],
             note='Parameter = population value; statistic = sample value.'),
          mc('A news website posts a poll; 80% of the 2,000 visitors who answered want a later school start. Can this result be generalized to all students?', [
              'No: it is a voluntary-response sample, so people with strong opinions are over-represented.',
              'Yes: 2,000 responses form a large sample, so the result must be accurate for all students.',
              'Yes: 80% is so far above 50% that any bias could not change the overall conclusion.',
              'No: a poll can never be used to estimate a population percent, even with random sampling.'],
             note='Voluntary response is biased regardless of size.'),
          mc('Why does a random sample allow conclusions about the whole population?', [
                        'Chance decides who is chosen, so the sample tends to represent the population without systematic bias.',
                        'A random sample always has exactly the same statistic as the population parameter it estimates.',
                        'A random sample always includes every member of the population, so nothing is left out of it.',
                        'A random sample is always larger than a voluntary sample, so its result is always more exact.'],
                       note='Random selection removes selection bias; chance variation remains. The others are false: a sample does not include everyone, is not always larger, and does not match the parameter exactly.'),
          mc("A school uses the first 30 students arriving in the morning to estimate the students' average hours of sleep. Which statement is correct?", [
              'It is not a random sample: early arrivers may sleep differently, so the estimate may be biased.',
              'It is a random sample, because no one chose the students by name or by any other rule.',
              'It is not random, but 30 students is enough to remove any bias from the estimate.',
              'It is a random sample, because the times the students arrive vary by chance.'],
             note='Convenience sample; early arrivers may sleep less.'),
      ],
      back=[
          B('Samples and populations', '7.SP.A.1', [
              mc('In statistics, what is a population?', ['the entire group a study wants to describe', 'the part of the group that is measured', 'a number computed from a sample', 'the number of people in a city'], note='Definition.'),
              mc('In statistics, what is a sample?', ['the part of the population that is studied', 'the entire group of interest', 'a number describing the whole population', 'a list of every possible outcome'], note='Definition.'),
              tf('A random sample gives every member of the population a chance to be chosen.', key=True, note='Definition.'),
              mc('Surveying every student in a school is', ['a census', 'a sample', 'an experiment', 'a statistic'], note='Whole population.'),
              mc('Why do studies often use a sample instead of the whole population?', ['Studying everyone may be too costly, slow, or impossible.', 'Samples always give the exact population value.', 'Samples have no chance variation at all.', 'A population cannot be described by a number.'],
                               note='Practical limits. The others are false: samples do vary by chance, do not give the exact population value, and populations are described by numbers.'),
          ], align='exact',
            why=why('the student confuses sample and population.', 'inference goes from sample to population.', 'defines sample and population.')),
          B('Draw inferences from random samples', '7.SP.A.2', [
              sa('In a random sample of 50 students, 20 walk to school. Estimate how many of 600 students walk.', 'Answer:', key='240', note='Any equivalent form.'),
              mc('Two random samples of 500 voters from the same city give 40% and 44% support for a plan. What is the best explanation for the difference?', [
                  'Random samples vary by chance, so a 4-point difference is not surprising.',
                  'One of the two samples must have been chosen incorrectly.',
                  'The population percent changed between the two samples.',
                  'Random samples from one population always give the same percent.'],
                 note='For n = 500 the sample percent varies by about 2 points (1 SD), so 4 points apart is common.'),
              tf('Different random samples from the same population usually give slightly different results.', key=True, note='Sampling variability.'),
              mc('From a random sample, 30% of 200 voters prefer a candidate. The best estimate for all voters is', ['30%', '200', '60%', 'cannot estimate'], note='Statistic estimates parameter.'),
              mc('Why is a larger random sample usually better for estimating a population value?', [
                                              'Its statistic varies less from sample to sample, so the estimate is more precise.', 'It removes all bias, even when the sample is not chosen at random.', 'It always gives exactly the population value, with no chance variation.', 'It makes the population value larger, so the estimate is closer to it.'],
                                             note='Less sampling variability. The others are false: no sample gives the exact value, size does not change the population, and size does not remove bias.'),
          ], align='exact',
            why=why('the student does not use samples to estimate.', 'the statistic estimates the parameter.', 'makes inferences from samples.')),
          B('Compute sample proportions and means', '6.SP.B.5.c', [
              sa('248 of 400 people say yes. What proportion is that?', 'Answer:', key='0.62', note='Any equivalent form.'),
              sa('Find the mean of 5.0, 5.1, 4.9, 5.08.', 'Answer:', key='5.02', note='Any equivalent form.'),
              tf('A proportion can be greater than 1.', key=False, note='A part of a whole is between 0 and 1.'),
              mc('1,600 of 2,000 is', ['80%', '20%', '16%', '1.25%'], note='1600/2000.'),
              sa('Write 62% as a decimal.', 'Answer:', key='0.62', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot compute the statistic.', 'statistics are computed from the sample.', 'computes proportions and means.')),
      ],
      f1=B('Describe sampling variability', 'HSS-IC.A.1', [
          mc('Two random samples of 400 residents of the same city give 62% and 59% support for a park. Which statement is correct?', [
              'The samples differ by chance; both estimate the same population percent.', 'One sample must be biased, since random samples agree exactly.', 'The population percent is exactly their average, 60.5%.', 'Each sample estimates a different population percent.'],
             note='Sampling variability.'),
          mc('Would random samples of 40 or random samples of 400 from the same population vary more from sample to sample?', [
              'Samples of 40: smaller samples are affected more by chance.', 'Samples of 400: more people means more variation.', 'They vary the same amount, since both are random.', 'Samples of 40: small samples are always biased.'],
             note='Variability decreases as n increases.'),
          tf('A parameter changes from sample to sample.', key=False, note='The parameter is fixed; the statistic varies.'),
          mc('Which is a statistic?', ['the mean height of 30 sampled students', 'the mean height of all students', 'the population size', 'the population proportion'], note='From a sample.'),
          mc('Why can a large voluntary-response sample be worse than a small random sample?', [
                                  'A large size does not remove bias; volunteers are systematically unrepresentative.', 'Large samples always have a larger margin of error than small random samples.', 'Small samples have no chance variation.', 'Voluntary samples are random, but a large one has too many answers to analyze well.'],
                                 note='Bias is not reduced by size. The others are false: voluntary samples are not random, larger samples have smaller margins, and small samples do vary.'),
      ], prog='same-course deepening', demand='Separate the effects of chance variation and of bias on statistics.'),
      f2=B('Quantify variability with a margin of error', 'HSS-IC.B.4', [
          sa('A city surveys a random sample of 400 residents, and 62% support a new park. Simulated sample proportions (samples of 400 with p = 0.62) have standard deviation 0.024. What is the margin of error? Give a decimal.' + SD2, 'Answer:', key='0.048',
             note='2 × 0.024 = 0.048, or 4.8 percentage points.'),
          sa('In a random sample of 400 residents, 62% support a new park, and the margin of error is 4.8 percentage points. Give the interval estimate for the percent of all residents who support the park.', ['Lower end (%):', 'Upper end (%):'], key='57.2; 66.8',
             note='Form required: both. 62 ± 4.8.'),
          tf('A margin of error describes chance variation, not bias.', key=True, note='Bias is not measured.'),
          mc('If the sample size is multiplied by 4, the margin of error is about', ['halved', 'doubled', 'divided by 4', 'unchanged'], note='Square-root law.'),
          mc('A random sample of 400 residents gives 62% support for a park, with the 95% interval 57.2% to 66.8%. What does the interval say?', [
              'The percent of all residents who support the park is plausibly between 57.2% and 66.8%.',
              'Exactly 62% of all of the residents of the city support the park.',
              '95% of all of the residents of the city support the park.',
              'Between 57.2% and 66.8% of the 400 surveyed residents support the park.'],
             note='The interval estimates the population percent; the sample percent is exactly 62%.'),
      ], prog='cross-standard extension', demand='Attach a numerical margin of error to the statistic.',
        builds='Builds on FORWARD 1: the variability of statistics described in words is now measured.')),

    # ------------------------------------------------------------------ 64. IC.A.2 model consistency with simulation
    S('HSS-IC.A.2', 'Decide whether a model is consistent with observed results using a simulation',
      target='Use supplied simulation results to decide whether a probability model is consistent with an observed result', strand='core', covers=['IC2-model'],
      main=[
          mc('A coin is claimed to be fair. It landed heads 34 times in 50 flips. The histogram shows 200 simulated runs of 50 flips of a fair coin. Count runs with 34 or more heads.' + CUT + ' Which conclusion is justified?', [
              '3 of 200 runs (1.5%) had 34 or more heads; 1.5% < 5%, so the data are evidence against a fair coin.',
              '3 of 200 runs (1.5%) had 34 or more heads, so the coin is proved to be unfair.',
              '36 of 200 runs (18%) had 29 or more heads, so 34 heads is not unusual for a fair coin.',
              'A fair coin can never land heads 34 times in 50 flips, so the claim is false.'], fig=COIN,
             note='Only the ≥34 bar counts: 3/200. Evidence is not proof, and the event is rare, not impossible.'),
          mc('A spinner is claimed to land on red 25% of the time. It landed on red 13 times in 40 spins. The histogram shows 200 simulated runs of 40 spins under the claim. Count runs with 13 or more reds.' + CUT + ' Which conclusion is justified?', [
              '34 of 200 runs (17%) had 13 or more reds; 17% > 5%, so the result is consistent with the claim.',
              '34 of 200 runs (17%) had 13 or more reds, so the claim is proved true.',
              'Only runs with exactly 13 reds count, which is rare, so the claim is rejected.',
              'The expected count is 10, and 13 is not 10, so the claim is false.'], fig=SPIN,
             note='20 + 14 = 34 runs. Consistent with the model does not prove it.'),
          mc('A die is claimed to be fair. It showed 16 sixes in 60 rolls. The histogram shows 200 simulated runs of 60 rolls of a fair die. Count runs with 16 or more sixes.' + CUT + ' Which conclusion is justified?', [
              '3 of 200 runs (1.5%) had 16 or more sixes; 1.5% < 5%, so the data are evidence against a fair die.',
              '3 of 200 runs (1.5%) had 16 or more sixes, so the die is proved to be unfair.',
              '15 of 200 runs (7.5%) had 14 or more sixes, so 16 sixes is not unusual.',
              'A fair die can never show 16 sixes in 60 rolls, so the claim is false.'], fig=DIE,
             note='Only the ≥16 bar counts: 3/200.'),
          mc('A player claims to make 70% of her free throws. She made 11 of 20. The histogram shows 200 simulated runs of 20 shots under the claim. Count runs with 11 or fewer makes.' + CUT + ' Which conclusion is justified?', [
              '24 of 200 runs (12%) had 11 or fewer makes; 12% > 5%, so the result is consistent with the claim.',
              '24 of 200 runs (12%) had 11 or fewer makes, so the 70% claim is proved true.',
              '6 of 200 runs (3%) had 9 or fewer makes; 3% < 5%, so 11 makes is unusual.',
              'She made 11, not the expected 14, so the claim is false.'], fig=FT,
             note='6 + 18 = 24 runs. Not unusual is not proof.'),
          mc('A model says boys and girls are equally likely. A hospital had 58 boys in 100 births. The histogram shows 200 simulated runs of 100 births under the model. Count runs with 58 or more boys.' + CUT + ' Which conclusion is justified?', [
              '19 of 200 runs (9.5%) had 58 or more boys; 9.5% > 5%, so the result is consistent with the model.',
              '19 of 200 runs (9.5%) had 58 or more boys, so the model is proved true.',
              '19 runs had 58 or more boys, and 19 is more than 5, so the result is unusual.',
              'There were 58 boys, not the expected 50, so the model is false.'], fig=BIRTH,
             note='19/200 = 9.5%.'),
      ],
      back=[
          B('Probability as long-run relative frequency', '7.SP.C.6', [
              sa('A fair coin is flipped 50 times. About how many heads do you expect?', 'Answer:', key='25', note='Any equivalent form.'),
              sa('A spinner has P(red) = 0.25. About how many reds in 40 spins?', 'Answer:', key='10', note='Any equivalent form.'),
              tf('Getting exactly the expected number every time is likely.', key=False, note='Results vary.'),
              mc('A fair die is rolled 60 times. Expected sixes:', ['10', '6', '16', '60'], note='60/6.'),
              mc('A fair coin is flipped 50 times and lands heads 26 times. Why is this not surprising?', [
                  '26 is close to the expected 25, and results vary by chance.', 'A fair coin always gives exactly 26 heads in 50 flips.', '26 is more than half, which proves the coin is fair.', 'Every number of heads from 0 to 50 is equally likely.'],
                 note='Chance variation around 25.'),
          ], align='exact',
            why=why('the student expects exact results.', 'judging requires knowing what is typical.', 'uses expected counts.')),
          B('Use simulations of compound events', '7.SP.C.8.c', [
              mc('Which design simulates 50 flips of a fair coin with random digits 0-9?', [
                  'Use 50 random digits; even = heads, odd = tails.', 'Use 50 random digits; 0 = heads, 1-9 = tails.', 'Use 1 random digit and multiply it by 50.', 'Use 50 random digits; only the digit 5 = heads.'],
                 note='Half of the digits must represent heads.'),
              mc('Which design simulates one spin of a spinner with P(red) = 0.25 using two-digit random numbers 00-99?', ['00-24 = red; 25-99 = not red', '00-25 = red; 26-99 = not red', '00-49 = red; 50-99 = not red', '25 = red; all other numbers = not red'],
                 note='25 of the 100 numbers must mean red; 00-25 has 26.'),
              tf('Each run of a simulation should copy the real process under the model.', key=True, note='Model.'),
              mc('A simulation has 200 runs. Each run represents', ['one repetition of the whole experiment', 'one flip', 'one histogram bar', 'the final answer'], note='Run = experiment.'),
              mc('Why does a simulation use many runs instead of just one?', [
                                'To see the pattern of results the model produces by chance.', 'Because a single run always gives the wrong answer.', 'To make the model match the observed data exactly.', "Because more runs change the model's probabilities."],
                               note='Many runs show the distribution under the model. The others are false: one run is not wrong, more runs do not change the model, and runs are not fitted to the data.'),
          ], align='exact',
            why=why('the student does not know what the histogram represents.', 'decisions rest on simulated runs.', 'designs and reads simulations.')),
          B('Relative frequency of a group of outcomes', '6.RP.A.3.c', [
              sa('3 of 200 runs is what percent?', 'Answer:', key='1.5%', note='Any equivalent form.'),
              sa('6 + 18 runs out of 200 is what percent?', 'Answer:', key='12%', note='Any equivalent form.'),
              tf('19 out of 200 is 19%.', key=False, note='19/200 = 0.095 = 9.5%.'),
              mc('34 of 200 is', ['17%', '34%', '6.8%', '1.7%'], note='34/200.'),
              sa('Is 2% less than 5%? Answer Yes or No.', 'Answer:', key='Yes', note='Compare the percents.'),
          ], align='supporting',
            why=why('the student cannot find the simulated proportion.', 'the decision compares a proportion to a cutoff.', 'computes percents.')),
      ],
      f1=B('Design a simulation to test a model', 'HSS-IC.A.2', [
          mc('A player claims to make 70% of her free throws, and she made 11 of 20. Which simulation tests the claim?', [
              'Digits 0-6 = make; 20 digits per run; repeat many runs; find how often 11 or fewer makes occur.',
              'Digits 0-6 = make; 11 digits per run; repeat many runs; find how often 20 makes occur.',
              'Digits 0-4 = make; 20 digits per run; repeat many runs; find how often exactly 11 makes occur.',
              'Digits 0-6 = make; 20 digits in a single run; the claim is true if that run has 14 makes.'],
             note='7 of 10 digits model 70%; each run copies 20 shots; count results at least as extreme.'),
          mc('A player who claims to make 70% of free throws made 11 of 20. Why should a simulation count runs with 11 or fewer makes, not only runs with exactly 11?', [
              'Any one exact count can be rare; the question is how often results at least this far below the claim occur.',
              'Runs with exactly 11 makes are impossible under the model, so they would never be counted at all.',
              'Counting 11 or fewer always makes the result significant, which is the goal of the simulation.',
              'The claim is about making 11 or fewer shots, not about making 70% of her free throws.'],
             note='Use results as extreme or more extreme.'),
          tf('A result that happens in 30% of simulated runs is strong evidence against the model.', key=False, note='30% is common.'),
          mc('A common cutoff for "unusual" is', ['about 5% of runs', 'about 50% of runs', '100% of runs', 'about 25% of runs'], note='Convention.'),
          mc('A simulation of a model is run 400 times instead of 200 times. What does this change?', [
                        'It gives a more precise estimate of how often a result occurs under the model.', "It changes the probabilities that the model assigns to each outcome.", 'It changes the observed data that the model is compared with.', 'It turns an unusual result into a usual one, because more runs are counted.'],
                       note='More runs estimate the model\'s proportion more precisely; the model and data are unchanged.'),
      ], prog='same-course deepening', demand='Design the simulation and justify the "as extreme" criterion.'),
      f2=B('Compare two treatments with a re-randomization simulation', 'HSS-IC.B.5', [
          mc('In an experiment, 20 plants were randomly assigned to fertilizer or no fertilizer, and the fertilized plants grew 2.9 cm more on average. The histogram shows 200 re-randomized differences under the model that fertilizer has no effect; none was 2.9 cm or more.' + CUT + ' What do you conclude?', [
              '0/200 < 5%: a difference this large is very unlikely by chance, so fertilizer appears to increase growth.',
              '0/200: a difference this large has probability exactly 0, so the fertilizer is proved to work.',
              'The difference is not significant, because no re-randomized difference matched it exactly.',
              'No conclusion is possible, because the result must first be compared with a fair coin.'], fig=RERAND,
             note='A rare result is evidence of an effect, not proof; probability is not shown to be zero.'),
          mc('What model does a re-randomization simulation assume?', [
              'The treatment has no effect, so the group labels can be shuffled.', 'The treatment has the same large effect on every subject.', 'The two groups were chosen by voluntary response.', 'The observed difference is exactly the true effect.'],
             note='The null model.'),
          tf('Re-randomization is a simulation of a model, like the coin-flip simulation.', key=True, note='Both test a model.'),
          mc('Under the model of no treatment effect, 60 of 200 re-randomized differences were at least as large as the observed one.' + CUT + ' The result is', ['not statistically significant', 'significant', 'proof of no effect', 'impossible'],
             note='30% is common; not significant does not prove the model.'),
          mc('How does a re-randomization test for an experiment extend the reasoning of testing a fair-coin claim with a simulation?', [
                        'Both ask how often a model produces a result at least as extreme as the observed one; here the model is "no treatment effect."',
                        'Both flip a real coin many times and then count how many heads appear in each of the groups of subjects in the study.',
                        'The coin test uses a probability model, but the re-randomization test does not use any model of the results at all.',
                        'Both prove the model is true whenever the observed result turns out to be common among the simulated results.'],
                       note='Same logic, different null model. The others describe flipping a real coin, deny that re-randomization uses a model, or treat a common result as proof.'),
      ], prog='cross-standard extension', demand='Apply the same model-testing logic to a randomized experiment.',
        builds='Builds on FORWARD 1: the designed simulation for one proportion becomes a shuffle of treatment labels.')),

    # ------------------------------------------------------------------ 65. IC.B.3 study types
    S('HSS-IC.B.3', 'Identify sample surveys, experiments, and observational studies',
      target='Identify the type of study (sample survey, experiment, observational study) and state its purpose and what it can show', strand='core', covers=['IC3-types'],
      main=[
          mc('Researchers randomly assign 100 volunteers to take a vitamin or a placebo and compare the number of colds. What type of study is this, and what is its purpose?', [
              'Experiment: to test whether the vitamin causes fewer colds.', 'Sample survey: to estimate the percent of people who take vitamins.', 'Observational study: to describe colds without any treatment.', 'Experiment: to estimate the percent of all people who catch colds.'],
             note='Random assignment of a treatment makes it an experiment.'),
          mc('A pollster asks a random sample of 1,000 voters which candidate they prefer. What type of study is this, and what is its purpose?', [
              'Sample survey: to estimate the preference of all voters.', 'Experiment: to test whether a candidate causes votes.', 'Observational study: to show which candidate causes turnout.', "Sample survey: to show the poll caused voters' choices."],
             note='A random sample survey estimates a population value.'),
          mc('Researchers compare the hospital records of smokers and nonsmokers for lung disease. What type of study is this, and can it by itself show causation?', [
              'Observational study; no, the groups were not randomly assigned.', 'Experiment; yes, smoking was the treatment in the study.', 'Observational study; yes, hospital records are accurate.', 'Sample survey; yes, the sample of records is large.'],
             note='No treatments were assigned.'),
          mc('Which study best answers "Does playing music while studying improve test scores?"', [
              'an experiment: randomly assign students to study with or without music and compare scores',
              'a survey that asks students whether they think music helps them study',
              'an observational study of students who already choose to play music',
              'a census of how many students in the school own headphones'],
             note='A cause-and-effect question needs an experiment.'),
          mc('Which study best answers "What percent of students at the school use the library weekly?"', [
              "a sample survey of a random sample of the school's students", 'a randomized experiment that assigns students to use the library', 'an observational study of students in the library today', 'a voluntary online poll posted on the library website'],
             note='Estimating a percent calls for a random sample survey.'),
      ],
      back=[
          B('Statistical questions and data collection', '6.SP.A.1', [
              mc('Is "How many hours do students at our school sleep?" a statistical question?', [
                  'Yes: the answers vary from student to student.', 'No: it has a single correct answer.', 'Yes: it asks about one particular student.', 'No: hours of sleep cannot be measured.'],
                 note='A statistical question anticipates variability.'),
              mc("Which method of collecting data best answers \"What percent of the city's voters favor the new library?\"", [
                  "a survey of a random sample of the city's voters", 'an experiment that assigns voters to read books', 'a survey of people leaving the old library', 'asking the members of the city council'],
                 note='Estimating a population percent calls for a random sample survey.'),
              tf('An experiment imposes a treatment on the subjects.', key=True, note='Definition.'),
              mc('Watching and recording without imposing treatments is', ['an observational study', 'an experiment', 'a placebo', 'a census'], note='Definition.'),
              mc('In an experiment, what is a placebo?', ['a fake treatment with no active ingredient', 'the group that gets the real treatment', 'a measurement taken before the study', 'a random sample of the population'], note='Definition.'),
          ], align='supporting',
            why=why('the student has no vocabulary for studies.', 'types are defined by how data are collected.', 'describes data collection.')),
          B('Association is not causation', 'HSS-ID.C.9', [
              mc('Ice cream sales and sunburns are positively correlated. Which explanation is best supported?', [
                  'Hot, sunny weather increases both; the correlation does not show that ice cream causes sunburn.',
                  'Ice cream causes sunburn, because the two variables are positively correlated.',
                  'Sunburns cause ice cream sales, because a correlation shows the direction of cause.',
                  'The correlation must be a calculation error, because the variables are unrelated.'],
                 note='A lurking variable explains the association.'),
              mc('"Students with more books at home get higher test scores." Which is a plausible lurking variable?', ['family income', 'the color of the book covers', "the test's page count", "the student's ID number"],
                 note='Income can affect both books at home and scores.'),
              tf('A strong correlation proves that one variable causes the other.', key=False, note='Correlation is not causation.'),
              mc('A variable that affects both variables in a study is', ['a confounding (lurking) variable', 'the response', 'the sample', 'the placebo'], note='Definition.'),
              mc('Which kind of study can show cause and effect?', ['a randomized experiment', 'an observational study', 'a voluntary-response survey', 'a sample survey'], note='Random assignment.'),
          ], align='exact',
            why=why('the student draws causal conclusions from associations.', 'study type determines whether causation can be shown.', 'separates correlation and causation.')),
          B('Random samples', '7.SP.A.1', [
              mc('Which method gives a simple random sample of 50 students from a school list?', [
                                'Number the students and use a random number generator to pick 50 different numbers.', 'Choose the first 50 names on the list, which is in alphabetical order.', 'Ask for 50 volunteers by posting a sign-up sheet in the school office.', 'Choose 50 students who are standing in the cafeteria line at lunch.'],
                               note='Every group of 50 has the same chance.'),
              mc('Is surveying the students in the cafeteria line a random sample of the school?', [
                  'No: students who are not in the line have no chance to be chosen.', 'Yes: the students in the line arrived in a random order.', 'Yes: any student could be in the cafeteria line.', 'No: a random sample must include every student.'],
                 note='Convenience sample.'),
              tf('A random sample tends to represent the population.', key=True, note='No systematic bias.'),
              mc('Which sample is random?', ['names drawn from a hat with every student\'s name', 'students who volunteer when asked in class', 'the first 50 students to arrive at school', 'the teacher\'s friends among the students'], note='Chance selection.'),
              mc('Why does a survey need a random sample?', ['so its results can be generalized to the population', 'so every person gives the same answer', 'so it needs to ask only 2 people', 'so it can show cause and effect by itself'], note='Generalization. The others are false: random samples are not limited to 2 people, do not make answers equal, and do not show cause and effect.'),
          ], align='supporting',
            why=why('the student does not see the role of randomness.', 'surveys rely on random samples.', 'describes random sampling.')),
      ],
      f1=B('Identify confounding and design flaws', 'HSS-IC.B.3', [
          mc('Students who choose to take an SAT prep course score higher than students who do not. Which is a confounding variable, with a correct reason?', [
              'Motivation: students who choose the course may be more motivated, which also raises scores.',
              'The course itself: it raises scores, so it is the confounding variable in the study.',
              'The test date: all students take the same test, so the date explains the difference.',
              'Hair color: it differs between students, so it must confound the result of the study.'],
             note='A confounder is related to both the choice and the outcome.'),
          mc('Students who choose to take an SAT prep course score higher than students who do not. Which design could show whether the course causes higher scores?', [
                        'Randomly assign volunteers to take the course or not, then compare their scores.', 'Survey many more students who chose to take the course about their scores.', 'Compare the scores of students at two different schools that offer the course.', 'Let students choose whether to take the course again, but use a larger sample.'],
                       note='Random assignment breaks the link with confounders.'),
          tf('An experiment without a control group can still show the treatment caused the result.', key=False, note='Comparison is needed.'),
          mc('In an experiment, why use a placebo?', ['to control for believing one is treated', 'to make the real treatment work better', 'to increase the sample size of the study', 'to make the study observational instead'], note='Placebo effect.'),
          mc('Why is an observational study, rather than an experiment, used to study whether smoking causes lung disease in people?', [
                        'It would be unethical to assign people to smoke.', 'Observational studies always show causation.', 'Experiments cannot use random assignment.', 'Smokers cannot be counted in an experiment.'],
                       note='Ethics. The others are false: experiments do use random assignment, smokers can be counted, and observational studies do not show causation.'),
      ], prog='same-course deepening', demand='Diagnose confounding and redesign studies to support causal claims.'),
      f2=B('Analyze the results of an experiment', 'HSS-IC.B.5', [
          mc('100 volunteers were randomly assigned to a vitamin or a placebo; the vitamin group had 1.2 fewer colds on average. Under the model that the vitamin has no effect, 40 of 200 re-randomizations gave the vitamin group at least 1.2 fewer colds.' + CUT + ' What do you conclude?', [
                        '40/200 = 20% > 5%: the difference could easily be chance, so it is not significant.', '40/200 = 20% > 5%: this proves the vitamin has no effect.', '40/200 = 20%: the vitamin prevents 20% of colds in these volunteers.', '40/200 = 20% > 5%: the difference is significant.'],
                       note='Not significant is not proof of no effect.'),
          mc('In a randomized vitamin-versus-placebo experiment, the vitamin group had 1.2 fewer colds on average. Under the model that the vitamin has no effect, 2 of 200 re-randomized differences were that large in the vitamin\'s favor.' + CUT + ' What do you conclude?', [
              '2/200 = 1% < 5%: significant, so the vitamin appears to reduce colds.', '2/200 = 1%: the vitamin works for only 1% of people.', '2/200 = 1% < 5%: the difference is not significant.', '2/200 = 1%: this proves the vitamin works for everyone.'],
             note='A significant result is evidence, not proof.'),
          tf('Random assignment makes it possible to attribute a significant difference to the treatment.', key=True, note='Groups differ only by chance otherwise.'),
          mc('The re-randomization model assumes', ['the treatment has no effect', 'the treatment works', 'the groups are different sizes', 'the data are normal'], note='Null model.'),
          mc('Why can a significant difference in an observational study not be interpreted as a treatment effect the way it can in a randomized experiment?', [
                        'Without random assignment, the difference could come from confounding variables rather than the treatment.',
                        'Observational studies cannot measure any differences between groups, so no difference can be found.',
                        'Observational studies always use smaller samples, so their differences are always due to chance.',
                        'A significant difference in an observational study is always the result of a calculation error.'],
                       note='Confounding. The others make false claims about sample size, measurement, and calculation errors; the real issue is confounding.'),
      ], prog='cross-standard extension', demand='Analyze experimental data with simulation to decide if the treatment effect is significant.',
        builds='Builds on FORWARD 1: after designing an experiment that can show causation, its results are tested.')),

    # ------------------------------------------------------------------ 66. IC.B.3 random sampling vs random assignment
    S('HSS-IC.B.3', 'Explain random sampling versus random assignment',
      target='Explain the difference between random sampling and random assignment and state what each allows a study to conclude', strand='core', covers=['IC3-random'],
      main=[
          mc('A random sample of 500 adults is surveyed about exercise and sleep; adults who exercise more tend to sleep better. Which conclusion is justified?', [
                        'The association can be generalized to all adults, but it does not show that exercise causes better sleep.',
                        'Exercise causes better sleep for all adults, because the sample was chosen at random.',
                        'Exercise causes better sleep, but only for the 500 adults who were surveyed.',
                        'Nothing can be concluded about any adults beyond the 500 who were surveyed.'],
                       note='Random sample: generalize. No random assignment: no causation. The others claim causation from a survey, limit the association to the 500 surveyed, or deny any conclusion.'),
          mc("60 volunteers are randomly assigned to two diets, and diet A's group loses significantly more weight. Which conclusion is justified?", [
                        'There is evidence that diet A caused more weight loss for these volunteers, but the result cannot be generalized to all people.',
                        'Diet A causes more weight loss for all people, because the volunteers were randomly assigned to the two diets.',
                        'Diet A is associated with weight loss for all people, but the study cannot show that the diet caused it.',
                        'Nothing can be concluded, because the volunteers chose to participate instead of being randomly sampled.'],
                       note='Random assignment: evidence of cause for these subjects. No random sample: no generalization. The others generalize to all people, deny causation despite random assignment, or deny any conclusion.'),
          mc("A random sample of 200 students from a school is randomly assigned to two study methods, and method 1 leads to significantly higher scores. Which conclusion is justified?", [
                        "There is evidence that method 1 causes higher scores, and the result can be generalized to the school's students.",
                        'There is evidence that method 1 causes higher scores, but only for the 200 students in the study.',
                        'Method 1 is associated with higher scores, but the study cannot show that it causes them.',
                        'Method 1 causes higher scores for students at every school, because the result was significant.'],
                       note='Random sample and random assignment: both conclusions, limited to this school. The others limit the result to the 200 students, deny causation despite random assignment, or generalize beyond the school.'),
          mc('A teacher compares test scores of students in her class who chose to use a review app with those who did not. Which conclusion is justified?', [
                        'Only an association in this class: there was no random assignment and no random sample.',
                        'The app causes higher scores for all students, because the groups were compared.',
                        'The app causes higher scores, but only for the students in this class.',
                        'The result can be generalized to all students, but it does not show causation.'],
                       note='Neither random assignment nor random sampling. The others claim causation or generalization, which need random assignment and random sampling.'),
          mc('How can 40 subjects be randomly assigned to two groups of 20?', [
                        'Number the subjects 1-40; choose 20 different random numbers for group 1; the rest form group 2.',
                        'Put the first 20 subjects who arrive in group 1 and the other 20 subjects in group 2.',
                        'Let each subject choose a group, and stop when one of the groups has 20 subjects.',
                        'Put the 20 tallest subjects in group 1 and the 20 shortest subjects in group 2.'],
                       note='Chance alone decides the groups. The others let arrival order, choice, or height decide the groups, so the groups may differ systematically.'),
      ],
      back=[
          B('Study types and their purposes', 'HSS-IC.B.3', [
              mc('Which type of study uses random assignment of treatments?', ['an experiment', 'a sample survey', 'an observational study', 'a census'], note='Definition.'),
              mc('Which type of study is designed to estimate a population value?', ['a sample survey', 'an experiment', 'a placebo', 'a case study of one person'], note='Definition.'),
              tf('An observational study assigns treatments.', key=False, note='It observes.'),
              mc('Random assignment is used to', ['make the groups comparable', 'choose who is in the population', 'avoid measuring', 'make the sample larger'], note='Comparability.'),
              mc('What does random sampling allow you to do?', ['generalize from the sample to the population', 'conclude cause and effect from the data', 'remove all chance variation from results', 'skip measuring the people in the sample'], note='Random sampling supports generalization.'),
          ], align='exact',
            why=why('the student confuses the two random processes.', 'each random step allows a different conclusion.', 'names study types.')),
          B('Choose a random sample', '7.SP.A.1', [
              mc('Which method chooses 20 names at random from a numbered list of 500?', [
                                'Pick 20 different random numbers from 1 to 500 and take those names.', 'Take the first 20 names on the numbered list, numbers 1 to 20.', 'Pick 20 names that look like a good mix of the whole list.', 'Email all 500 and take the first 20 people who reply to the email.'],
                               note='Random numbers give every name the same chance.'),
              sa('Is a sample of volunteers a random sample? Answer Yes or No.', 'Answer:', key='No', note='Any equivalent answer.'),
              tf('A sample of volunteers may differ from the population.', key=True, note='Self-selection.'),
              mc('Which method gives a random sample?', ['drawing numbered slips from a well-mixed hat', 'asking friends to take part', 'choosing the first 20 people on the list', 'asking for volunteers to sign up'], note='Chance.'),
              mc('Names are written on slips and drawn from a hat. Why must the slips be well mixed?', ['so every slip has the same chance of being drawn', 'so the hat can hold more slips', 'so the first slip drawn is always the same', 'so the drawing takes longer'],
                 note='Equal chance.'),
          ], align='exact',
            why=why('the student cannot describe random selection.', 'one of the two random steps.', 'chooses random samples.')),
          B('Correlation and causation', 'HSS-ID.C.9', [
              sa('Can an association between two variables in observational data prove causation? Answer Yes or No.', 'Answer:', key='No', note='Any equivalent answer.'),
              mc('Students who exercise more tend to sleep better. Which is a plausible lurking variable?', ['stress level', 'the brand of their shoes', 'the day of the month they were born', 'their locker number'],
                 note='Stress can affect both exercise and sleep.'),
              tf('Random assignment controls lurking variables on average.', key=True, note='Balances groups.'),
              mc('Causation can be concluded from', ['a randomized experiment', 'a survey', 'an observational study', 'a correlation alone'], note='Random assignment.'),
              mc('Why does a correlation alone not show which variable causes the other?', [
                                              'Either variable could affect the other, or a third variable could affect both.', 'Correlation is always 0 when one variable causes the other.', 'Correlated variables can never be related to each other.', 'Correlation can be found only for categories, not for numbers.'],
                                             note='Direction and lurking variables. The others are false: correlation is for numerical variables, is not 0 under causation, and correlated variables can be related.'),
          ], align='supporting',
            why=why('the student overstates conclusions.', 'causal claims need random assignment.', 'separates association and causation.')),
      ],
      f1=B('Improve an experimental design', 'HSS-IC.B.3', [
          mc('60 volunteers try a new diet and lose weight. Why is a control group (for example a second, randomly assigned diet) needed to judge the diet?', [
                        'Without a comparison group, the weight loss could be due to other factors, not the diet.', 'A control group makes every volunteer in the study lose more weight on the diet.', 'A control group is needed only in studies with more than 100 volunteers.', 'A control group proves that the new diet works for everyone who tries it.'],
                       note='Comparison.'),
          mc('A drug study blocks subjects by age, then randomly assigns treatments within each age group. Why?', ['so age differences cannot hide or create a treatment effect', 'so every subject in each age group receives both treatments', 'so the study can avoid random assignment within the groups', 'so the older subjects all get the drug and the younger the placebo'],
                       note='Blocking compares treatments within similar ages.'),
          tf('In a double-blind experiment, neither subjects nor evaluators know who gets the treatment.', key=True, note='Definition.'),
          mc('60 volunteers were randomly assigned to two diets, and diet A led to more weight loss. Which change would let the result be generalized to all adults?', ['randomly selecting subjects from all adults', 'adding more volunteers to each diet', 'measuring the volunteers more often during the study', 'using a placebo for one group'], note='Random sampling.'),
          mc('Why are many subjects better than few in an experiment?', [
                                  'Chance differences between groups are smaller, so real effects are easier to detect.', 'More subjects remove the need for random assignment to the groups.', 'More subjects always make the treatment itself work better.', 'More subjects make any observed result statistically significant.'],
                                 note='Less chance variation. The others are false: random assignment is still needed, size does not change the treatment, and not every result becomes significant.'),
      ], prog='same-course deepening', demand='Improve designs with control, blocking, blinding, and sampling.'),
      f2=B('Use re-randomization to judge a treatment difference', 'HSS-IC.B.5', [
          mc("60 volunteers were randomly assigned to two diets; diet A's group lost 2.4 kg more on average. Under the model that the diets have the same effect, 5 of 200 re-randomizations gave a difference of at least 2.4 kg in favor of A." + CUT + ' Is the difference significant?', [
              'Yes: 5/200 = 2.5% < 5%.', 'No: 5/200 = 2.5% < 5%.', 'Yes: 5 is more than 2.4.', 'No: 5/200 = 25% > 5%.'],
             note='2.5% is below the cutoff.'),
          mc("60 volunteers (not a random sample of adults) were randomly assigned to two diets, and diet A's group lost significantly more weight. Which conclusion is justified?", [
              'There is evidence that diet A caused more weight loss for these volunteers; it may not apply to all adults.',
              'Diet A causes more weight loss for all adults, because the result was significant.',
              'Diet A is associated with weight loss, but the study cannot show that it caused it.',
              'Nothing can be concluded, because the volunteers were not a random sample of adults.'],
             note='Random assignment supports cause; no random sample limits the scope.'),
          tf('Re-randomization shuffles the group labels as if the treatment had no effect.', key=True, note='Null model.'),
          mc('If 70 of 200 re-randomized differences were at least 2.4 kg, conclude', ['the difference could be due to chance', 'diet A works', 'diet B works', 'the study was observational'], note='35% is common.'),
          mc('Why is a re-randomization test valid only when the original groups were formed by random assignment?', [
                        'The shuffle copies the random assignment; if the groups were not randomly formed, the shuffle does not model how they arose.',
                        'Re-randomization needs exactly the same number of subjects as a fair coin needs flips, so it requires random groups.',
                        'Random assignment makes every difference significant, so the test can only be used after random assignment.',
                        'Without random assignment the group means cannot be computed, so there is nothing to shuffle in the test.'],
                       note='The simulation models the assignment process. The others are false: group means can always be computed, random assignment does not make results significant, and no coin is involved.'),
      ], prog='cross-standard extension', demand='Use simulation to test the effect allowed by random assignment.',
        builds='Builds on FORWARD 1: a well-designed experiment is analyzed with re-randomization.')),
]

SETS += [
    # ------------------------------------------------------------------ 67. IC.B.4 proportion with margin of error
    S('HSS-IC.B.4', 'Estimate a population proportion with a margin of error from a simulation',
      target='Use a sample proportion and the variability of simulated sample proportions to give an estimate with a margin of error, and interpret it', strand='core', covers=['IC4-prop'],
      main=[
          sa('In a random sample of 100 students, 58 want a later start time. The histogram shows 200 simulated samples of 100 from a population with p = 0.58; their standard deviation is 0.049.' + SD2 + ' Give the margin of error and the interval estimate, as decimals.',
             ['Margin of error:', 'Lower end:', 'Upper end:'], key='0.098; 0.482; 0.678', fig=PROP, note='Form required: all three. 2(0.049) = 0.098; 0.58 ± 0.098.'),
          sa('In a random sample of 300 voters, 120 support a measure. Simulated sample proportions (n = 300, p = 0.40) have standard deviation 0.0275.' + SD2 + ' Give the estimate, the margin of error, and the interval, as decimals.',
             ['Estimate:', 'Margin of error:', 'Lower end:', 'Upper end:'], key='0.4; 0.055; 0.345; 0.455', note='Form required: all four. 120/300 = 0.40; 2(0.0275) = 0.055.'),
          sa('In a random sample of 50 shoppers, 35 use a store app. Simulated sample proportions (n = 50, p = 0.70) have standard deviation 0.064.' + SD2 + ' Give the margin of error and the interval, as decimals.',
             ['Margin of error:', 'Lower end:', 'Upper end:'], key='0.128; 0.572; 0.828', note='Form required: all three. 2(0.064) = 0.128; 0.70 ± 0.128.'),
          mc('Three random-sample surveys have simulated-proportion standard deviations 0.064 (n = 50), 0.049 (n = 100), and 0.0275 (n = 300). Using margin of error = 2 SD, which survey has the smallest margin of error, and why?', [
              'n = 300 (margin 0.055): larger samples give less variable sample proportions.',
              'n = 50 (margin 0.128): smaller samples are easier to measure exactly.',
              'n = 100 (margin 0.098): the middle size balances the two kinds of error.',
              'All are equal: the margin depends only on the population size.'],
             note='2(0.0275) = 0.055 is smallest.'),
          mc('A report from a random sample says "52% of voters support the plan, with a margin of error of 3 percentage points (95% confidence)." Which interpretation is correct?', [
              'The percent of all voters who support the plan is plausibly between 49% and 55%.',
              'Exactly 52% of all voters support the plan, give or take nothing at all.',
              'Between 49% and 55% of the sampled voters support the plan.',
              'The plan will win, because 52% is more than 50% of the voters.'],
             note='The interval estimates the population percent; it includes values below 50%.'),
      ],
      back=[
          B('Statistics, parameters, and sampling variability', 'HSS-IC.A.1', [
              sa('In a random sample of 100 students, 58 want a later start time. What is the statistic?', 'Answer:', key='0.58 (58%)', note='Any equivalent answer.'),
              mc('In a random sample of 100 students, 58% want a later start time. What parameter does 58% estimate?', [
                  'the percent of all students who want a later start', 'the percent of the 100 sampled students who want it', 'the number of students in the sample', 'the margin of error of the survey'],
                 note='The parameter describes the population.'),
              tf('Different random samples of 100 would give different sample proportions.', key=True, note='Sampling variability.'),
              mc('A histogram of 200 simulated sample proportions (samples of 100) shows', ['how sample proportions vary', 'the whole population of values', 'one sample of 100 values', 'the population parameter exactly'], note='Sampling distribution.'),
              mc('Why must a sample be random for its margin of error to be meaningful?', [
                                              'The margin describes chance variation in random samples; a biased sample can be off by more.', 'A random sample always has a margin of error of 0, so any error is bias.', 'A biased sample has a smaller margin of error than a random one.', 'The margin depends only on the size of the population, not the sample.'],
                                             note='The margin does not measure bias. The others are false: random samples have a positive margin, bias is not measured by the margin, and the margin depends on the sample size.'),
          ], align='exact',
            why=why('the student confuses statistic and parameter.', 'the margin is about estimating the parameter.', 'identifies statistic and parameter.')),
          B('Proportions and percents', '6.RP.A.3.c', [
              sa('Write 120 out of 300 as a proportion.', 'Answer:', key='0.40', note='Any equivalent form.'),
              sa('Write 0.58 ± 0.10 as an interval.', ['Lower end:', 'Upper end:'], key='0.48; 0.68', note='Form required: both.'),
              tf('35 out of 50 is 35%.', key=False, note='35/50 = 0.70 = 70%.'),
              mc('52% ± 3% gives', ['49% to 55%', '52% to 55%', '49% to 52%', '50% to 54%'], note='Subtract and add.'),
              sa('Write 0.055 as a percent.', 'Answer:', key='5.5%', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot form the interval.', 'answers are proportions and intervals.', 'works with proportions.')),
          B('Standard deviation as typical distance from the mean', 'HSS-ID.A.2', [
              sa('By the 68-95-99.7 rule, what percent of a normal distribution lies within 2 standard deviations of the mean?', 'Answer:', key='95%', note='The middle number of the rule.'),
              sa('If the SD is 0.049, what is 2 SDs?', 'Answer:', key='0.098', note='Any equivalent form.'),
              tf('A smaller standard deviation means more variability.', key=False, note='A smaller SD means the values are closer to the mean.'),
              mc('Which set of simulated proportions varies least?', ['SD 0.0275', 'SD 0.049', 'SD 0.064', 'SD 0.1'], note='Smallest SD.'),
              sa('Compute 2 × 0.064.', 'Answer:', key='0.128', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot convert the SD to a margin.', 'the margin is about 2 SDs.', 'uses standard deviation.')),
      ],
      f1=B('Plan a sample size for a desired margin of error', 'HSS-IC.B.4', [
          sa('A survey of a random sample of 100 students has a margin of error of 0.10. Quadrupling the sample size halves the margin of error. What is the margin of error with n = 400? Give a decimal.', 'Answer:', key='0.05', note='0.10/2.'),
          sa('About what sample size gives a margin of error of 0.05 when p ≈ 0.5? (Use margin ≈ 2√(p(1 - p)/n).)', 'n ≈', key='400', note='Any equivalent form.'),
          tf('Doubling the sample size halves the margin of error.', key=False, note='It divides it by √2.'),
          mc('A random sample of n = 100 people gives a margin of error for a proportion. Which change to the sample size reduces the margin of error the most?', ['use n = 900', 'use n = 200', 'use n = 110', 'take a second sample of 100 and report it alone'],
             note='The margin is about proportional to 1/√n: n = 900 divides it by 3.'),
          sa('Two random-sample polls of the same population have margins of error 0.05 and 0.025 for a proportion. The margin of error is about proportional to 1/√n. How many times as large is the second sample as the first?', 'Answer:', key='4',
             note='Halving the margin requires 4 times the sample size.'),
      ], prog='same-course deepening', demand='Reason backward from a desired margin of error to a sample size.'),
      f2=B('Evaluate reports that use margins of error', 'HSS-IC.B.6', [
          mc('A poll shows candidate A at 51% and B at 49%, each with a margin of error of ±4 percentage points. A headline says "A leads." Evaluate.', [
                        'Not justified: the intervals 47%-55% and 45%-53% overlap, so either could lead.', 'Justified: 51% is greater than 49%, and the poll used a large sample.', 'Justified: the margin of error is the same for both, so it cancels and A leads by 2.', 'Not justified: A must have less than 50% support, since 51% - 4% is below 50%.'],
                       note='The difference is within the margin of error.'),
          mc('A report gives 58% ± 10% from a random sample of 100 students and claims "a majority of students want a later start." Evaluate.', [
              'Not clearly justified: the interval 48% to 68% includes values below 50%.', 'Justified: 58% is more than 50%.', 'Justified: the whole interval is above 50%.', 'Not justified: a sample of 100 can never support a claim.'],
             note='Plausible values include less than a majority.'),
          tf('A margin of error accounts for bias from a voluntary-response sample.', key=False, note='Only chance variation.'),
          mc('Which claim is best supported by its data?', [
              'A random sample gives 70% ± 3% support, so a majority support the plan.',
              'A random sample gives 51% ± 5% support, so a majority support the plan.',
              'An online poll gives 60% support, so a majority support the plan.',
              'A random sample gives 52% ± 4% support, so exactly 52% support it.'],
             note='Only 67%-73% stays above 50% and comes from a random sample.'),
          mc('Besides the percent, what should a careful poll report include?', [
                        'the sample size, how the sample was chosen, and the margin of error', 'only the percent, rounded to the nearest whole number', 'the names and answers of the people who were surveyed', "only last year's result, so readers can compare"],
                       note='Information needed to judge the estimate.'),
      ], prog='cross-standard extension', demand='Use the margin of error to evaluate claims made in reports.',
        builds='Builds on FORWARD 1: planned margins of error are used to judge whether reported differences are meaningful.')),

    # ------------------------------------------------------------------ 68. IC.B.4 mean with margin of error
    S('HSS-IC.B.4', 'Estimate a population mean with a margin of error from a simulation',
      target='Use a sample mean and the variability of simulated (resampled) means to estimate a population mean with a margin of error, and interpret it', strand='core', covers=['IC4-mean'],
      main=[
          sa('A random sample of 40 students slept a mean of 6.8 hours. The histogram shows the means of 200 resamples of the data; their standard deviation is 0.20 hours.' + SD2 + ' Give the margin of error and the interval, in hours.',
             ['Margin of error:', 'Lower end:', 'Upper end:'], key='0.4; 6.4; 7.2', fig=BOOT, note='Form required: all three. 2(0.20) = 0.4; 6.8 ± 0.4.'),
          sa('A random sample of 25 apples has mean weight 152 g. Simulated sample means have standard deviation 3.6 g.' + SD2 + ' Give the margin of error and the interval, in grams.',
             ['Margin of error:', 'Lower end:', 'Upper end:'], key='7.2; 144.8; 159.2', note='Form required: all three. 2(3.6) = 7.2; 152 ± 7.2.'),
          sa('A random sample of 60 commuters has mean commute 24.5 minutes. Simulated sample means have standard deviation 1.4 minutes.' + SD2 + ' Give the margin of error and the interval, in minutes.',
             ['Margin of error:', 'Lower end:', 'Upper end:'], key='2.8; 21.7; 27.3', note='Form required: all three. 2(1.4) = 2.8; 24.5 ± 2.8.'),
          mc('A random sample of 40 students gives the 95% interval 6.4 to 7.2 hours for the mean hours of sleep. Which interpretation is correct?', [
              'The mean sleep of all students is plausibly between 6.4 and 7.2 hours.',
              '95% of all students sleep between 6.4 and 7.2 hours each night.',
              'Every student at the school sleeps at least 6.4 hours each night.',
              'The 40 sampled students each slept between 6.4 and 7.2 hours.'],
             note='The interval is about the population mean, not individual students.'),
          sa('A random sample of 25 apples gives a margin of error of 7.2 g for the mean weight. Assume apple weights vary the same way and the same 2-SD (95%) convention is used, so the margin of error is proportional to 1/√n. What margin of error do you expect from a random sample of 100 apples? Give grams.', 'Answer:', key='3.6',
             note='4 times the sample size halves the margin.'),
      ],
      back=[
          B('Mean of a data set', '6.SP.B.5.c', [
              sa('Find the mean of 6, 7, 7.5, 6.5.', 'Answer:', key='6.75', note='Any equivalent form.'),
              mc('What does the mean of a random sample estimate?', ['the population mean', 'the sample size', 'the largest value in the population', 'the margin of error'], note='Statistic estimates parameter.'),
              tf('The mean is not affected by extreme values.', key=False, note='One extreme value can move the mean a lot; the median is resistant.'),
              mc('The mean of 150, 152, 154 is', ['152', '150', '154', '456'], note='Sum/3.'),
              sa('Each of 40 values in a data set increases by 0.5. By how much does the mean increase? Give a number.', 'Answer:', key='0.5', note='Adding a constant to every value adds it to the mean.'),
          ], align='exact',
            why=why('the student cannot find the statistic.', 'the estimate starts from the sample mean.', 'computes means.')),
          B('What resampling simulates', 'HSS-IC.A.1', [
              mc('Why can resampling a random sample (drawing with replacement) show how sample means vary?', [
                                              'The resamples act like new samples from a population that looks like the sample.', 'Resampling collects new data from the whole population each time it is done.', 'Resampling always gives the true population mean as the center.', 'Resampling removes all chance variation from the sample means.'],
                                             note='The sample stands in for the population. The others are false: resampling uses only the original sample, does not give the true mean, and does not remove chance variation.'),
              mc("In a histogram of 200 resample means, what does one bar's height show?", [
                  'how many of the 200 resample means fell in that interval', 'the mean of the original sample', 'the number of values in each resample', 'the chance the population mean is in that interval'],
                 note='Bar height = count.'),
              tf('Sample means vary less than individual values.', key=True, note='Averaging reduces variability.'),
              mc('A random sample of 40 students slept a mean of 6.8 hours. The parameter being estimated is', ['the mean sleep of all students', 'the 40 students\' mean', 'the resample SD', '6.8'], note='Population mean.'),
              mc('A random sample of 40 students had a mean of 6.8 hours of sleep. Is 6.8 hours a parameter or a statistic?', [
                  'a statistic: it describes the sample of 40', 'a parameter: it describes the sample of 40', 'a parameter: it describes all students', 'a statistic: it describes all students'],
                 note='It is computed from the sample.'),
          ], align='exact',
            why=why('the student does not understand the simulation.', 'the margin comes from it.', 'interprets the simulation.')),
          B('Two standard deviations and the 95% range', 'HSS-ID.A.2', [
              sa('Compute 6.8 - 2(0.20) and 6.8 + 2(0.20).', ['6.8 - 2(0.20) =', '6.8 + 2(0.20) ='], key='6.4; 7.2', note='Form required: both.'),
              sa('Compute 2 × 1.4.', 'Answer:', key='2.8', note='Any equivalent form.'),
              tf('About 95% of a mound-shaped distribution is within 2 SDs of its mean.', key=True, note='Rule.'),
              mc('152 ± 7.2 gives', ['144.8 to 159.2', '145 to 159', '144.8 to 152', '152 to 159.2'], note='Subtract and add.'),
              sa('Is 7.5 inside the interval from 6.4 to 7.2? Answer Yes or No.', 'Answer:', key='No', note='7.5 > 7.2.'),
          ], align='supporting',
            why=why('the student cannot form the interval.', 'margin = 2 SD.', 'computes the 95% range.')),
      ],
      f1=B('Use intervals to judge claims about a mean', 'HSS-IC.B.4', [
          mc("A random sample gives the 95% interval 6.4 to 7.2 hours for students' mean sleep. A health guide says students average 8 hours. Does the interval support this?", [
                        'No: 8 is outside the interval of plausible values for the mean.', 'Yes: 8 is close to the upper end of the interval, 7.2 hours.', 'Yes: some of the students in the sample sleep 8 hours or more.', 'No: the interval proves the mean is exactly its center, 6.8 hours.'],
                       note='8 is not a plausible mean.'),
          mc('A random sample gives the 95% interval 144.8 g to 159.2 g for the mean apple weight. A grower claims the apples average 155 g. Is the claim consistent with the interval?', [
              'Yes: 155 g is inside the interval, so it is a plausible mean.', 'Yes: the claim is proved true because 155 is inside it.', 'No: 155 g is not the center of the interval.', 'No: the mean must be exactly 152 g.'],
             note='Consistent, not proved.'),
          tf('A value inside a 95% interval estimate for a mean is proved to be the true mean.', key=False, note='It is only plausible.'),
          mc('A random sample of 60 commuters gives an interval for the mean commute time. Which change would most likely narrow the interval?', ['sampling 240 commuters instead of 60', 'sampling 30 commuters', 'rounding the data', 'using the median'], note='Larger n.'),
          mc('A random sample of students at one school gives the interval 6.4 to 7.2 hours for their mean sleep. Why should the interval not be applied to students at a different school?', [
                        "The sample came only from this school, so it estimates only this school's mean.", 'An interval for a mean can only describe a single student\'s sleep.', 'The students at the other school must have a higher mean sleep time.', 'The interval is too narrow to be applied to any group of students.'],
                       note='The population sampled limits the inference.'),
      ], prog='same-course deepening', demand='Use interval estimates to evaluate claimed values and their scope.'),
      f2=B('Compare two group means with re-randomization', 'HSS-IC.B.5', [
          mc('In an experiment, 40 students were randomly assigned to use a study app or not (20 each). The app group scored 6 points more on average. Under the model that the app has no effect, 9 of 200 re-randomizations gave the app group at least 6 more points. Using a one-sided count and a 5% cutoff, is the difference significant?', [
              'Yes: 9/200 = 4.5% < 5%.', 'No: 9/200 = 4.5% > 5%.', 'No: 9 is more than 6.', 'Yes: 9/200 = 45%.'],
             note='4.5% is below the cutoff.'),
          mc('Students were randomly assigned to a treatment group (study app) or a control group (no app), and the difference in mean scores was re-randomized 200 times. What null model do the re-randomizations represent?', [
              'The app has no effect on scores, so the group labels are interchangeable.', 'The app raises every score by exactly 6 points.', 'The control group scores lower in every re-randomization.', 'The students were chosen by voluntary response.'],
             note='Null model: no treatment effect.'),
          tf('An interval for one mean and a re-randomization test for two means both use simulated variability.', key=True, note='Same idea.'),
          mc('In an app experiment, the app group scored 6 points more on average. Under the model of no app effect, 30 of 200 re-randomizations gave the app group at least 6 more points.' + CUT + ' The conclusion is', [
              'the difference could be chance (15% > 5%)', 'the app works (15% < 50%)', 'the app lowers scores', 'the app is proved to have no effect'],
             note='30/200 = 15%. Not significant is not proof of no effect.'),
          mc('How is the margin of error for one mean related to judging a difference between two means?', [
              'Both ask how much a statistic varies by chance; a difference is meaningful only if it is large compared with that variability.',
              'A difference between two means never varies by chance, so it does not need any measure of chance variation.',
              'The margin of error for one mean is always equal to the difference between the two group means.',
              'They are unrelated: one uses the data, and the other uses only the number of subjects in each group.'],
             note='Both compare a statistic with its chance variability.'),
      ], prog='cross-standard extension', demand='Move from estimating one mean to comparing two treatment means.',
        builds='Builds on FORWARD 1: judging a claimed mean against chance variation becomes judging a treatment difference.')),

    # ------------------------------------------------------------------ 69. IC.B.5 compare treatments
    S('HSS-IC.B.5', 'Compare two treatments with a re-randomization simulation',
      target='Use data from a randomized experiment and a supplied re-randomization simulation to decide whether a difference between treatments is significant', strand='core', covers=['IC5-compare'],
      main=[
          mc('10 plants got fertilizer and 10 did not (randomly assigned). Fertilized plants grew 2.9 cm more on average. The histogram shows 200 re-randomized differences under the model that fertilizer has no effect. Use a one-sided count (2.9 cm or more) and a 5% cutoff. Which conclusion is justified?', [
              '0 of 200 were 2.9 cm or more; 0% < 5%, so the difference is significant: fertilizer appears to increase growth.',
              '0 of 200 were 2.9 cm or more, so this difference has probability exactly 0 and fertilizer is proved to work.',
              '4 of 200 (2%) were 2 cm or more, so the observed difference of 2.9 cm is not significant.',
              'Most re-randomized differences were near 0, so the observed difference is not significant.'], fig=RERAND,
             note='The ≥ 3 bar and the part of the 2-to-3 bar at 2.9 or more: none of 200. Rare is not impossible.'),
          mc("In a randomized caffeine experiment, the caffeine group's mean reaction time was 0.04 s faster. Under the model that caffeine has no effect, 62 of 200 re-randomizations gave the caffeine group a mean at least 0.04 s faster. Using a one-sided count and a 5% cutoff, is the difference significant?", [
                        'No: 62/200 = 31% > 5%, so the difference could easily be chance.', 'Yes: 62/200 = 31% is more than 5%, so the difference is significant.', 'No: 31% > 5%, and this proves that caffeine has no effect.', 'Yes: 0.04 s is less than 5% of a second, so it is significant.'],
                       note='31% is common. Not significant is not proof of no effect.'),
          mc('Students were randomly assigned to use a study app or not, and the app group scored 6 points higher on average. Under the model that the app has no effect, 9 of 200 re-randomizations gave the app group at least 6 more points. Using a one-sided count and a 5% cutoff, is the difference significant?', [
              'Yes: 9/200 = 4.5%, which is below 5%.', 'No: 9/200 = 4.5%, which is above 5%.', 'Yes: 9/200 = 45%, which is above 5%.', 'No: 9 is more than 6, so the app has no effect.'],
             note='One-sided: 9/200 = 4.5% < 5%.'),
          mc('What does a re-randomization simulation assume, and how is it carried out?', [
              'It assumes no treatment effect; all responses are pooled and randomly re-split into groups of the original sizes, and the difference in means is recorded many times.',
              'It assumes the treatment works; new subjects are recruited for each run, and the difference in their group means is recorded many times to estimate the true effect.',
              "It assumes no treatment effect; each group's values are re-sorted from smallest to largest, and the two sorted lists are compared once to find the difference.",
              'It assumes the treatment works; the observed difference is doubled and halved many times, and the results are graphed to show how large the effect could be.'],
             note='Null model plus shuffling of labels.'),
          mc('Using the histogram of 200 re-randomized differences, how many differences were 2 cm or more, and would an observed difference of 2 cm be significant using a one-sided count and a 5% cutoff?', [
              '4 of 200 (2%); 2% < 5%, so yes, it would be significant.',
              '4 of 200 (2%); 2% < 5%, so no, it would not be significant.',
              '31 of 200 (15.5%); 15.5% > 5%, so no, it would not be significant.',
              '0 of 200; a difference of 2 cm has probability 0 under the model.'], fig=RERAND,
             note='The 2-to-3 bar has 4 and the ≥ 3 bar has 0. 31 counts from 1 cm.'),
      ],
      back=[
          B('Compare the means of two groups', '7.SP.B.4', [
              sa('Group A has mean 25.4 cm and group B has mean 22.5 cm. Find the difference A - B.', 'Answer:', key='2.9 cm', note='Any equivalent form.'),
              sa('Group A: 4, 6, 8. Group B: 3, 5, 4. Find the difference in means.', 'Answer:', key='2', note='Any equivalent form.'),
              tf('A difference in sample means could happen even if the treatments have the same effect.', key=True, note='Chance.'),
              mc('Mean A = 0.52 s and mean B = 0.48 s. A - B is', ['0.04 s', '-0.04 s', '1.00 s', '0.4 s'], note='Subtract.'),
              mc('Why is a difference between two group means compared with the variability in the groups?', [
                                              'A difference is meaningful only if it is large relative to the natural variation.', 'Any difference between the group means proves a treatment effect.', 'The variability in the groups gives the exact size of the effect.', 'Variability matters only when the two group means are equal.'],
                                             note='Signal versus noise. The others are false: a difference alone is not proof, variability is not the effect size, and variability always matters.'),
          ], align='exact',
            why=why('the student cannot compute the observed difference.', 'the test compares this difference with the simulation.', 'compares group means.')),
          B('Random assignment in experiments', 'HSS-IC.B.3', [
              mc('In a fertilizer experiment, 20 plants were randomly assigned to fertilizer or no fertilizer. Why were they randomly assigned?', [
                                              'to make the groups comparable, so a difference can be due to the fertilizer', 'to make sure every plant grows exactly the same amount', 'so the result can be generalized to all plants of every kind, everywhere', 'so that no measurements of growth are needed afterward'],
                                             note='Random assignment balances other factors.'),
              mc('How can 20 plants be randomly assigned to two groups of 10?', [
                  'Number the plants 1-20 and use random numbers to choose 10 for fertilizer.', 'Put the 10 tallest plants in the fertilizer group.', 'Put the 10 plants nearest the window in the fertilizer group.', 'Let the gardener pick 10 healthy-looking plants for fertilizer.'],
                 note='Chance alone decides.'),
              tf('Without random assignment, a re-randomization test does not justify a cause-and-effect conclusion.', key=True, note='Design matters.'),
              mc('Random assignment is a feature of', ['experiments', 'surveys', 'observational studies', 'censuses'], note='Definition.'),
              mc('A randomized experiment gives a significant difference. Which conclusion does it allow?', [
                                'there is evidence the treatment caused the difference for these subjects', 'the treatment causes the same difference in everyone everywhere', 'the difference is due to chance alone, not the treatment', 'the subjects were a random sample of everyone in the population'],
                               note='Cause for the subjects studied.'),
          ], align='exact',
            why=why('the student does not see why shuffling is valid.', 're-randomization copies the random assignment.', 'explains random assignment.')),
          B('Probability as relative frequency in simulations', '7.SP.C.6', [
              sa('62 of 200 is what percent?', 'Answer:', key='31%', note='Any equivalent form.'),
              sa('9 of 200 is what percent?', 'Answer:', key='4.5%', note='Any equivalent form.'),
              tf('An event that happens in 40% of simulated runs is unusual.', key=False, note='40% is common; unusual usually means about 5% or less.'),
              mc('0 of 200 runs suggests the observed result is', ['very unlikely under the model', 'impossible', 'certain', 'typical'], note='Rare, not impossible.'),
              sa('Is 4/200 less than 5%? Answer Yes or No.', 'Answer:', key='Yes', note='4/200 = 2%.'),
          ], align='supporting',
            why=why('the student cannot convert counts to proportions.', 'significance compares a proportion to a cutoff.', 'uses relative frequencies.')),
      ],
      f1=B('Two-sided comparisons and design choices', 'HSS-IC.B.5', [
          mc('In a caffeine experiment, the observed difference in mean reaction time was 0.04 s. The question is whether caffeine changes reaction time in either direction. Which re-randomized differences should be counted?', [
              'those with |difference| ≥ 0.04 s, in either direction', 'only those with difference ≥ 0.04 s', 'only those with difference exactly 0.04 s', 'only those with |difference| ≤ 0.04 s'],
             note='A two-sided question counts both tails.'),
          sa('The histogram shows 200 re-randomized differences in mean growth (cm). How many differences were 2 cm or more, or less than -2 cm?', 'Answer:', key='4', fig=RERAND,
             note='The 2-to-3 bar has 4; the ≥ 3 and < -2 bars have 0.'),
          tf('Using more plants in each group usually makes the re-randomized differences less spread out.', key=True, note='Less chance variation.'),
          mc('A small observed difference can be significant when', ['the groups have very little natural variation', 'the sample in each group is small', 'the groups were not randomly assigned', 'the data are rounded to whole numbers'], note='Small spread.'),
          mc('Why should the cutoff for significance (such as 5%) be chosen before seeing the data?', [
                                  'Choosing it afterward could bias the conclusion toward the result one wants.', 'The cutoff must equal the observed proportion of the data.', 'Cutoffs chosen in advance are always 50%, the fairest choice.', 'The cutoff changes the data that are collected in the study.'],
                                 note='Avoids bias. The others are false: the cutoff does not change the data, is not set equal to the result, and is usually 5%, not 50%.'),
      ], prog='same-course deepening', demand='Choose one- or two-sided criteria and reason about how design affects significance.'),
      f2=B('Evaluate reports of experiments', 'HSS-IC.B.6', [
          mc('A company says its supplement "improved memory scores by 3 points" in a study of 8 people with no control group. Which evaluation is correct?', [
              'Weak evidence: with no control group and only 8 people, the change could be due to other factors or chance.',
              'Strong evidence: an increase of 3 points is a real improvement in memory for these people.',
              'Strong evidence: every one of the 8 people in the study took the supplement as directed.',
              'Weak evidence, but only because an increase of 3 points is too small a number to matter.'],
             note='No comparison and a tiny sample.'),
          mc('A report says a new teaching method "significantly" raised scores in a randomized experiment. Under the no-effect model, 2 of 200 re-randomized differences were at least as large as the observed difference.' + CUT + ' Evaluate the report.', [
              'Supported: the assignment was random, and 2/200 = 1% < 5%.', 'Not supported: 2/200 = 1% is too small to matter.', 'Supported: the method is proved to work for all students.', 'Not supported: re-randomization cannot be used for experiments.'],
             note='Significant evidence from a randomized design.'),
          tf('"Statistically significant" means the effect is large and important.', key=False, note='It means unlikely by chance; it may be small.'),
          mc('Which report is most convincing?', ['a randomized experiment with a control group and a rare result', 'testimonials from many satisfied customers', 'an online poll of 10,000 users of the product', 'a study of 500 users with no comparison group or random assignment'], note='Design and evidence.'),
          mc('Which information should a report of an experiment include?', [
                                  'the assignment method, group sizes, observed difference, and how unusual it is', 'only the observed difference between the two groups', 'only the names of the treatments, the date of the study, and who paid for it', 'only the conclusion that the treatment works for everyone'],
                                 note='All the evidence needed to judge it.'),
      ], prog='cross-standard extension', demand='Use the logic of randomized comparisons to evaluate published claims.',
        builds='Builds on FORWARD 1: knowing what makes a comparison convincing is applied to outside reports.')),

    # ------------------------------------------------------------------ 70. IC.B.6 evaluate reports
    S('HSS-IC.B.6', 'Evaluate claims in reports based on data',
      target='Evaluate a report based on data by examining the design, the sample, the graph, and whether the conclusion follows', strand='core', covers=['IC6-evaluate'],
      main=[
          mc('An ad says "4 out of 5 dentists recommend our toothpaste." Only 5 dentists, chosen by the company, were asked. Evaluate the claim.', [
              'Weak: the sample is tiny and not random, so it cannot represent all dentists.',
              'Strong: 80% is a large majority of the dentists who were asked.',
              'Strong: dentists are experts, so any group of them is representative.',
              'Weak: the claim would only be fine if all 5 of the dentists agreed.'],
             note='Small, company-chosen sample.'),
          mc('A report says "Students who eat breakfast earn higher grades, so breakfast causes higher grades." The data came from a survey. Evaluate.', [
              'Not justified: a survey shows association, not causation; lurking variables could explain it.',
              'Justified: the survey found that students who eat breakfast have higher grades.',
              'Justified: the survey was large enough to show cause and effect.',
              'Not justified: breakfast and grades cannot be associated in a survey.'],
             note='Observational data.'),
          mc('A bar graph shows sales of 50 and 52 thousand dollars, with the vertical axis starting at 48 thousand, so one bar looks twice as tall. Evaluate the impression the graph gives.', [
              'Misleading: the truncated axis makes a 4% difference look like a 100% difference.',
              'Fair: the tops of the bars show the correct values of 50 and 52 thousand.',
              'Fair: starting the axis at 48 thousand makes the graph easier to read.',
              'Misleading: the taller bar should be drawn more than twice as tall.'],
             note='52 is 4% more than 50, but the bars above 48 are 2 and 4 units tall.'),
          mc('A TV show asks viewers to text their vote; 90% of 10,000 texts favor a policy. The show claims most citizens support it. Evaluate.', [
                                  'Not justified: texters are a voluntary response, not a random sample.',
                                  'Justified: 10,000 texts form a very large sample of the citizens.',
                                  'Justified: 90% is so far above 50% that the method of collecting the votes does not matter.',
                                  'Not justified: 10,000 texts is too few to represent a whole country.'],
                                 note='Voluntary response bias is not fixed by size.'),
          mc('A poll shows candidate A at 51% and B at 49%, each with a margin of error of ±4 percentage points. A headline says "A is winning." Evaluate.', [
              'Not justified: the intervals 47%-55% and 45%-53% overlap, so the lead is within the margin of error.',
              'Justified: A has more support than B in the poll, so A is winning the race.',
              'Justified: the margin of error is the same for both candidates, so it cancels out.',
              'Not justified: B is actually winning, because the margin favors the trailing candidate.'],
             note='Either could lead.'),
      ],
      back=[
          B('Random samples and bias', 'HSS-IC.A.1', [
              mc('Why is a voluntary-response sample usually biased?', ['People with strong opinions are more likely to respond.', 'Every member of the population responds to it.', 'The sample is chosen with random numbers instead.', 'Voluntary samples are always too small to use.'], note='Self-selection. The others are false: not everyone responds, size is not the problem, and volunteers are not chosen with random numbers.'),
              mc('What does a random sample allow?', ['generalizing from the sample to the population', 'concluding cause and effect from the data', 'eliminating all chance variation from results', 'skipping the margin of error in the report'], note='Generalization.'),
              tf('A very large sample cannot be biased.', key=False, note='Size does not fix bias.'),
              mc('Which sample is most likely biased?', ['customers who chose to write reviews', 'randomly chosen customers', 'every customer', 'a random sample of 1,000'], note='Self-selected.'),
              sa('Is "5 dentists chosen by the company" a random sample? Answer Yes or No.', 'Answer:', key='No', note='Any equivalent answer.'),
          ], align='exact',
            why=why('the student trusts any sample.', 'evaluation starts with the sample.', 'recognizes bias.')),
          B('Study design and causation', 'HSS-IC.B.3', [
              mc("A survey records students' breakfast habits and grades. What type of study is it?", ['an observational study', 'a randomized experiment', 'a placebo-controlled experiment', 'a simulation'], note='No treatment is assigned.'),
              mc('Which design could test whether eating breakfast causes higher grades?', [
                                'a randomized experiment that assigns students to eat breakfast or not', "a larger survey of students' breakfast habits and grades", 'a voluntary online poll about eating breakfast and grades', 'comparing grades of students who already eat breakfast or not'],
                               note='Random assignment is needed for causation.'),
              tf('Only randomized experiments can establish cause and effect.', key=True, note='Random assignment.'),
              mc('A confounding variable is', ['a variable related to both the explanatory and response variables', 'the response variable that is measured in the study', 'the number of subjects in the sample of the study', 'the margin of error of the estimate'], note='Definition.'),
              mc('Students who eat breakfast tend to earn higher grades. Which is a plausible confounding variable?', ['the amount of sleep students get', 'the color of the cereal box', "the students' locker numbers", 'the day the survey was printed'],
                 note='Sleep can affect both.'),
          ], align='exact',
            why=why('the student accepts causal claims.', 'many reports confuse association and causation.', 'connects design and conclusions.')),
          B('Read scales on graphs', '3.MD.B.3', [
              sa("A bar graph's vertical axis starts at 48. One bar reaches 50 and another reaches 52. What values do the two bars show?", ['First bar:', 'Second bar:'], key='50; 52', note='Form required: both. Read the scale, not the bar length.'),
              sa('What percent larger is 52 than 50?', 'Answer:', key='4%', note='Any equivalent form.'),
              tf('An axis that does not start at 0 can make differences look larger.', key=True, note='Truncation.'),
              mc('On a graph whose axis starts at 48, a bar of 52 looks how many times as tall as a bar of 50?', ['2 times', '1.04 times', '4 times', 'the same'], note='Heights 4 and 2 above the axis start.'),
              mc('A bar graph of sales of 50 and 52 thousand dollars has a vertical axis starting at 48 thousand. How should it be redrawn to be fair?', [
                  'Start the vertical axis at 0, or clearly mark the axis break.', 'Start the axis at 51 to show the difference better.', 'Make the bars wider.', 'Remove the axis labels.'],
                 note='A truncated axis exaggerates differences.'),
          ], align='supporting',
            why=why('the student is misled by graphs.', 'reports often use graphs.', 'reads scales.')),
      ],
      f1=B('Rewrite claims so that they follow from the data', 'HSS-IC.B.6', [
          mc('A survey found that students who eat breakfast earn higher grades. Which claim is supported by the survey?', [
              'Students who eat breakfast tend to have higher grades.', 'Eating breakfast causes higher grades.', 'Skipping breakfast causes lower grades.', 'Higher grades cause students to eat breakfast.'],
             note='An observational survey supports only an association.'),
          mc('A poll shows 51% for A and 49% for B, each with a margin of error of ±4 percentage points. Which headline is accurate?', ['"The race is too close to call"', '"A is winning"', '"B is winning"', '"A has a certain 2-point lead"'],
             note='The difference is within the margin of error.'),
          tf('Saying "is associated with" instead of "causes" is appropriate for an observational study.', key=True, note='Careful wording.'),
          mc('Which conclusion is justified by a random sample of 1,000 voters showing 62% ± 3% support?', ['most voters support the measure', 'exactly 62% support it', 'the measure will pass by 24 points', 'the sample was biased'], note='59% to 65%.'),
          mc('An ad says "4 out of 5 dentists recommend our toothpaste," based on 5 dentists chosen by the company. What would make the claim more convincing?', [
                        'a large random sample of dentists, with the question wording reported', 'asking the same 5 dentists again a year later', 'choosing 5 different dentists who already like the brand', 'printing the claim in larger letters on the box'],
                       note='Size and random selection.'),
      ], prog='same-course deepening', demand='Produce accurate claims, not only criticize inaccurate ones.'),
      f2=B('Analyze decisions based on test results', 'HSS-MD.B.7', [
          sa('A screening test detects 95% of people who have a disease (sensitivity 95%) and gives a false positive for 5% of healthy people. In a group of 10,000 people, 1% have the disease. How many true positives are there, and how many positive results in all?', ['True positives:', 'All positives:'], key='95; 590',
             note='Form required: both. 0.95(100) = 95; 0.05(9,900) = 495; 95 + 495 = 590.'),
          mc('A screening test has sensitivity 95% and a 5% false-positive rate. In a group of 10,000 people where 1% have the disease, there are 95 true positives and 495 false positives. A report says "a positive test means you almost surely have the disease." Evaluate.', [
              'Misleading: only 95/590 ≈ 16% of positives have the disease.', 'Correct: the test detects 95% of cases.', 'Correct: only 5% of positive results are false.', 'Misleading: 495/590 ≈ 84% of positives have the disease.'],
             note='P(disease | positive) = 95/590 ≈ 0.161.'),
          tf('The probability of having the disease given a positive result can be low even with an accurate test.', key=True, note='Rare disease.'),
          mc('A screening test has sensitivity 95% and a 5% false-positive rate. If 1% of a population has the disease, P(disease | positive) is about', ['0.16', '0.95', '0.05', '0.99'],
             note='Per 10,000: 95 true and 495 false positives; 95/590 ≈ 0.161.'),
          mc('For a screening test, P(disease | positive) ≈ 0.16. Which follow-up decision makes the most sense after a positive result?', [
              'Confirm with a second, more accurate test before treatment.', 'Begin treatment at once, since the test detects 95% of cases.', 'Ignore the result, since it is probably a false positive.', 'Repeat the same test and treat only if it is negative.'],
             note='Most positives are false, but some are real.'),
      ], prog='cross-standard extension', demand='Evaluate claims and decisions that depend on probabilities from tests.',
        builds='Builds on FORWARD 1: accurate rewording of claims is applied to medical test claims using probabilities.')),

    # ------------------------------------------------------------------ 71. MD.B.6 fair decisions (+)
    S('HSS-MD.B.6', 'Design and judge fair decision procedures with probabilities',
      target='Decide whether a random procedure is fair (each option equally likely) and design fair procedures with coins, dice, or random numbers', strand='core', covers=['MD6-fair'],
      main=[
          mc('Three friends choose a driver by flipping a fair coin twice: HH = Ana, HT = Ben, TH = Cy, and TT = flip twice again. Is this fair?', [
              'Yes: HH, HT, and TH are equally likely and TT is redone, so each friend has probability 1/3.',
              'No: Ana has probability 1/2, because HH has two heads and the others have only one.',
              'No: TT is ignored, so the three probabilities add to 3/4 instead of 1.',
              'Yes: each friend has probability 1/4, the same as each of the four outcomes.'],
             note='Redoing TT scales 1/4 each to 1/3 each.'),
          mc('Four people use a fair die: 1 = A, 2 = B, 3 = C, 4 = D, and 5 or 6 means roll again. Is this fair?', [
              'Yes: each person has probability 1/4 after rerolls.', 'No: each person has 1/6, and 1/3 of the time is wasted.', 'No: D is less likely, because 4 is next to 5 and 6.', 'Yes: each person has probability 1/6.'],
             note='Four equally likely faces remain.'),
          mc("A well-mixed hat holds 3 slips with Ana's name and 2 with Ben's. One slip is drawn at random to choose who goes first. Is this fair?", [
              'No: P(Ana) = 3/5 and P(Ben) = 2/5.', 'Yes: each name is drawn or not, so each has 1/2.', 'Yes: the slips are well mixed.', 'No: P(Ana) = 2/5 and P(Ben) = 3/5.'],
             note='Each slip is equally likely.'),
          mc('A random number generator gives a whole number 1-100, each equally likely. Numbers 1-33 choose A, 34-66 choose B, 67-99 choose C, and 100 means generate again. Is this fair?', [
              'Yes: each person has 33 equally likely numbers, and 100 is redone, so each has 1/3.',
              'No: A has 33 numbers but C has 34 numbers, so C is a little more likely.',
              'No: 100 is wasted, so the probabilities are 0.33 each and do not add to 1.',
              'Yes: each has probability 33/100, and the leftover 1/100 does not matter.'],
             note='Each range has 33 numbers; redoing 100 scales each to 1/3.'),
          mc('Two fair dice are rolled; if the sum is even, player 1 wins, otherwise player 2 wins. Is this fair?', [
              'Yes: 18 of the 36 equally likely outcomes have an even sum, so each player has 1/2.',
              'No: there are 6 even sums (2, 4, ..., 12) and only 5 odd sums, so player 1 wins more.',
              'No: a sum of 7 is the most likely sum, so player 2 wins more often than player 1.',
              'Yes: there are 11 possible sums, and about half of the 11 sums are even.'],
             note='Count equally likely outcomes, not sums.'),
      ],
      back=[
          B('Probabilities of equally likely outcomes', '7.SP.C.7.a', [
              sa('A fair die is rolled. What is P(3)?', 'Answer:', key='1/6', note='Any equivalent form.'),
              sa('A bag has 3 red and 2 blue slips. What is P(red)?', 'Answer:', key='3/5', note='Any equivalent form.'),
              tf('Each face of a fair die has the same probability.', key=True, note='Uniform model.'),
              mc('Two fair coins are flipped, one after the other. P(first is heads and second is tails) is', ['1/4', '1/2', '1/3', '1/8'], note='4 equally likely outcomes.'),
              sa('A spinner has 4 equal sections. What is P(one section)?', 'Answer:', key='1/4', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot assign probabilities.', 'fairness compares probabilities.', 'uses equally likely outcomes.')),
          B('Sample spaces for compound events', '7.SP.C.8.b', [
              mc('A fair coin is flipped twice. Which list is the sample space of equally likely outcomes?', ['HH, HT, TH, TT', 'HH, HT, TT', 'two heads, one head, no heads', 'H, T'],
                 note='Order matters for equally likely outcomes.'),
              sa('How many outcomes does rolling two dice have?', 'Answer:', key='36', note='Any equivalent form.'),
              tf('When a fair coin is flipped twice, the 3 outcomes "two heads," "one head," and "no heads" are equally likely.', key=False, note='P(one head) = 1/2, while the other two are 1/4 each.'),
              mc('How many outcomes for two dice give an even sum?', ['18', '12', '6', '21'], note='Half.'),
              sa('List the outcomes of rolling two dice with a sum of 4.', 'Answer:', key='(1, 3), (2, 2), (3, 1)', note='Form required: all three.'),
          ], align='exact',
            why=why('the student miscounts outcomes.', 'fairness needs the correct sample space.', 'lists sample spaces.')),
          B('Probability between 0 and 1 and redoing outcomes', '7.SP.C.5', [
              mc('A fair die is rolled; a roll of 5 or 6 is ignored and the die is rolled again until it shows 1-4. What are the probabilities of the final results 1, 2, 3, and 4?', [
                                'They stay equally likely, and each becomes 1/4.', 'Each stays 1/6, because the die is still fair.', '1 becomes more likely than 4, since it is first.', 'Each becomes 1/5, because one reroll is added.'],
                               note='The four equally likely results are scaled to add to 1.'),
              sa('A fair die is rolled, and any 5 or 6 is rerolled until the result is 1-4. What is P(final result is 1)?', 'Answer:', key='1/4', note='Any equivalent form.'),
              tf('Probabilities of all outcomes in a sample space add to 1.', key=True, note='Total probability.'),
              mc('An event that can never happen has probability', ['0', '1', '1/2', '-1'], note='Impossible.'),
              sa('Three equally likely outcomes: what is each probability?', 'Answer:', key='1/3', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student is confused by "flip again" rules.', 'fair procedures often redo outcomes.', 'reasons about probabilities.')),
      ],
      f1=B('Design fair procedures and count expected trials', 'HSS-MD.B.6', [
          mc('Which procedure chooses one of 5 people fairly using a fair coin?', [
              'Flip 3 times (8 equally likely outcomes); assign 5 outcomes to the people and flip again on the other 3.',
              'Flip 5 times; the person whose number equals the count of heads is chosen, and 0 heads means flip again.',
              'Flip 3 times (8 equally likely outcomes); assign 5 outcomes to people and give the other 3 to person 1.',
              'Flip twice (4 equally likely outcomes); one outcome each for persons 1-4, and person 5 also gets HH.'],
             note='Equal numbers of equally likely outcomes, with the rest redone.'),
          sa('Three friends choose a driver by flipping a coin twice: HH, HT, and TH each pick a friend, and TT means flip again. What is the probability that a choice is made on the first try?', 'Answer:', key='3/4', note='Any equivalent form.'),
          tf('A fair procedure must give each person an equal chance, even if it may take several tries.', key=True, note='Fairness is about probabilities.'),
          mc('To choose among 6 people fairly with one die, you', ['assign one face to each person', 'roll twice and add', 'reroll on 6', 'assign 1-3 to person A'], note='Six equally likely faces.'),
          mc('A teacher picks a student from a class of 28 using a random number generator that gives whole numbers 1-30, each equally likely. Which rule is fair?', [
              'Assign numbers 1-28 to the students, and generate again on 29 or 30.', 'Assign numbers 1-28; 29 and 30 both choose student 1.', 'Assign numbers 1-28; 29 and 30 choose students 1 and 2.', 'Generate one number and divide it by 30.'],
             note='Each student gets one number; extra numbers are redone.'),
      ], prog='same-course deepening', demand='Design fair procedures for awkward numbers of choices and analyze their efficiency.'),
      f2=B('Analyze strategies and decisions with probability', 'HSS-MD.B.7', [
          sa('A game costs $1. You roll a fair die and win $4 if you roll a 6, and nothing otherwise. Find the expected net gain per game, in dollars, as a fraction.', 'Answer:', key='-1/3',
             note='(1/6)(4) - 1 = -1/3.'),
          sa('A game costs $1. You roll a fair die and win a prize if you roll a 6, and nothing otherwise. With a $4 prize, what is the expected net gain in dollars? What prize makes the expected net gain 0?', ['Expected net gain ($):', 'Fair prize ($):'], key='-1/3; 6',
             note='Form required: both. (1/6)(4) - 1 = -1/3; (1/6)P - 1 = 0 gives P = 6.'),
          tf('A game can be fair in who is chosen but still have a negative expected value for the player.', key=True, note='Two meanings of fair.'),
          mc('With P(win) = 1/4 and prize $8 for a $2 ticket, the expected net gain is', ['$0', '$2', '-$2', '$6'], note='8/4 - 2.'),
          mc('What is the difference between a fair choice procedure and a fair game?', [
              'A fair choice procedure gives everyone equal probability; a fair game has expected net gain 0.',
              'They mean the same thing: both require each player to have probability 1/2 of winning.',
              'A fair choice procedure has expected net gain 0; a fair game gives everyone equal probability.',
              'A fair game always has a prize; a fair choice procedure never uses probability at all.'],
             note='Two meanings of fair.'),
      ], prog='cross-standard extension', demand='Extend fairness from equal probabilities to expected value in strategies.',
        builds='Builds on FORWARD 1: designing equal-chance procedures leads to evaluating games and choices by expected gain.')),

    # ------------------------------------------------------------------ 72. MD.B.7 analyze decisions (+)
    S('HSS-MD.B.7', 'Analyze decisions and strategies with probabilities',
      target='Use probabilities (including conditional reasoning with counts) to analyze decisions such as medical testing, product testing, warranties, and test-taking strategies', strand='core', covers=['MD7-decide'],
      main=[
          sa('A disease affects 1% of 10,000 people. A test detects 95% of people who have it and gives a false positive for 5% of healthy people. Find the number of true positives, the number of false positives, and P(disease | positive) as a decimal rounded to the nearest thousandth.',
             ['True positives:', 'False positives:', 'P(disease | positive):'], key='95; 495; 0.161', note='Form required: all three. 0.95(100) = 95; 0.05(9,900) = 495; 95/590 ≈ 0.161.'),
          sa('A shipment is accepted if 2 randomly tested items are both non-defective. Each item is defective with probability 0.1, independently. What is the probability the shipment is accepted? Give a decimal.', 'Answer:', key='0.81', note='0.9 × 0.9.'),
          mc('A $30 warranty covers a repair that costs $200 and is needed with probability 0.1 (otherwise there is no cost). Using expected cost as the decision rule, which is correct?', [
              'Expected repair cost 0.1 × 200 = $20 < $30, so the warranty is not worth buying.',
              'Expected repair cost 0.1 × 200 = $20 < $30, so the warranty is worth buying.',
              'Expected repair cost 0.9 × 200 = $180 > $30, so the warranty is worth buying.',
              'Expected repair cost 200 - 30 = $170 > $30, so the warranty is worth buying.'],
             note='On average the warranty costs $10 more than it saves.'),
          mc('Option A pays $10 with probability 0.5 and $0 otherwise; option B pays $50 with probability 0.1 and $0 otherwise. Compare the expected values and the risks.', [
              'Both have expected value $5; B is riskier, because it usually pays $0.',
              'A has expected value $5 and B has $50, so B is better.',
              'Both have expected value $5; A is riskier, because it pays less.',
              'A has expected value $10 and B has $5, so A is better.'],
             note='0.5(10) = 0.1(50) = 5; B pays $0 90% of the time.'),
          mc('A test gives +1 point for a correct answer, -1/4 point for a wrong answer, and 0 for a blank, on 4-choice questions. Using expected score as the decision rule, should a student with no idea of the answer guess randomly or leave it blank?', [
              'Guess: the expected score is (1/4)(1) + (3/4)(-1/4) = 1/16, more than 0 for a blank.',
              'Leave it blank: the expected score of guessing is (1/4)(1) + (3/4)(-1) = -1/2.',
              'Leave it blank: a wrong answer loses points, so guessing always lowers the score.',
              'Guess: the expected score is (1/4)(1) = 1/4, because wrong answers do not count.'],
             note='1/16 > 0.'),
      ],
      back=[
          B('Probability of compound independent events', '7.SP.C.8.a', [
              sa('Each item is non-defective with probability 0.9, independently of the others. Find the probability that two items are both non-defective. Give a decimal.', 'Answer:', key='0.81', note='0.9 × 0.9.'),
              sa('Two fair coins: P(both heads)?', 'Answer:', key='1/4', note='Any equivalent form.'),
              tf('For independent events, P(A and B) = P(A) · P(B).', key=True, note='Multiplication rule.'),
              mc('Each item is non-defective with probability 0.9, independently of the others. The probability that three items are all non-defective is', ['0.729', '0.27', '0.9', '2.7'], note='0.9³.'),
              sa('Each item is defective with probability 0.1, independently of the others. Find the probability that at least one of two items is defective. Give a decimal.', 'Answer:', key='0.19', note='1 - 0.9² = 0.19.'),
          ], align='exact',
            why=why('the student adds instead of multiplying.', 'product testing uses independent events.', 'multiplies probabilities.')),
          B('Two-way tables of counts', '8.SP.A.4', [
              sa('Of 10,000 people, 1% have a disease. How many have it?', 'Answer:', key='100', note='Any equivalent form.'),
              sa('Of 9,900 healthy people, 5% test positive. How many?', 'Answer:', key='495', note='Any equivalent form.'),
              tf('A two-way table can show test results for people with and without a disease.', key=True, note='Rows and columns.'),
              mc('If 95 sick and 495 healthy people test positive, the total positives are', ['590', '495', '95', '10,000'], note='Add.'),
              sa('What fraction of positives are sick (95 of 590)? Give a decimal to the nearest thousandth.', 'Answer:', key='0.161', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot organize the counts.', 'conditional reasoning uses a table.', 'builds two-way tables.')),
          B('Weighted averages of outcomes', '6.RP.A.3.c', [
              sa('Find 10% of $200.', 'Answer:', key='$20', note='Any equivalent form.'),
              sa('Compute 0.5 × 10 and 0.1 × 50.', ['0.5 × 10 =', '0.1 × 50 ='], key='5; 5', note='Form required: both.'),
              tf('1/4 × 1 + 3/4 × (-1/4) = 1/4.', key=False, note='1/4 - 3/16 = 1/16.'),
              mc('0.2 × 30 + 0.8 × 0 equals', ['6', '30', '24', '0.2'], note='Weighted sum.'),
              sa('Compute 0.9 × 0 + 0.1 × 200.', 'Answer:', key='20', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot compute expected values.', 'decisions compare averages.', 'computes weighted sums.')),
      ],
      f1=B('Investigate how changing conditions changes the decision', 'HSS-MD.B.7', [
          sa('A test detects 95% of people who have a disease and gives a false positive for 5% of healthy people. In a group of 10,000 where 10% have the disease, find P(disease | positive). Give a decimal rounded to the nearest thousandth.', 'Answer:', key='0.679',
             note='950 true and 0.05(9,000) = 450 false positives; 950/1,400 ≈ 0.679.'),
          mc('A $30 warranty covers a repair that costs $200; the repair is needed with probability 0.2 and otherwise there is no cost. Using expected cost as the decision rule, is the warranty worth buying?', [
              'Yes: the expected repair cost is 0.2 × 200 = $40, more than $30.', 'No: the expected repair cost is $40, which is more than $30.', 'No: the repair probably will not happen, since 0.2 < 0.5.', 'Yes: the repair cost of $200 is more than $30.'],
             note='Compare $40 with $30.'),
          tf('A positive result is more convincing when the disease is more common.', key=True, note='Compare 0.161 and 0.679.'),
          mc('A test gives +1 point for a correct answer and -1/4 point for a wrong answer on 4-choice questions. A student eliminates one wrong choice and guesses randomly among the 3 remaining choices. What is the expected score for the guess?', [
              '(1/3)(1) + (2/3)(-1/4) = 1/6', '(1/4)(1) + (3/4)(-1/4) = 1/16', '(1/3)(1) + (2/3)(-1) = -1/3', '(1/3)(1) = 1/3'],
             note='With 3 choices, P(correct) = 1/3.'),
          sa('A shipment is accepted only if all n tested items are non-defective. Each item is defective with probability 0.1, independently. What is the smallest whole number n for which the probability of acceptance is below 0.5?', 'Answer:', key='7',
             note='0.9⁶ ≈ 0.531 and 0.9⁷ ≈ 0.478.'),
      ], prog='same-course deepening', demand='Re-analyze decisions when probabilities or rules change.'),
      f2=B('Find expected values of random variables', 'HSS-MD.A.2', [
          sa('A random variable X takes values 0, 1, 2 with probabilities 0.25, 0.5, 0.25. Find E(X).', 'E(X) =', key='1', note='Any equivalent form.'),
          sa('A raffle sells 500 tickets at $2 each; one ticket wins a $400 prize. Find the expected net gain of one ticket, in dollars, as a decimal.', 'Answer:', key='-1.2', note='400/500 - 2 = -1.20.'),
          tf('The expected value is the long-run average of many repetitions.', key=True, note='Interpretation.'),
          mc('For a fair die, E(roll) is', ['3.5', '3', '6', '21'], note='21/6.'),
          mc('A $30 warranty covers a $200 repair that is needed with probability 0.1 (otherwise no cost). Why is deciding whether to buy it an expected-value calculation?', [
              'The repair cost is a random variable (0 or 200) with expected value $20, compared with the certain $30 price.',
              'The warranty price is a random variable whose expected value is $200, compared with the $30 price.',
              'The repair will cost exactly $20 for certain, so the warranty price is compared with $20.',
              'The expected repair cost is 0.1 + 200 = $200.10, which is compared with the $30 price.'],
             note='E(cost) = 0.1(200) + 0.9(0) = 20.'),
      ], prog='later-course extension', demand='Formalize decisions with random variables and expected values (Probability and Statistics).',
        builds='Builds on FORWARD 1: the repeated what-if decisions are expressed as expected values of random variables.')),
]
