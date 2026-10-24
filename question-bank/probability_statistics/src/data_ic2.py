"""S-IC.B.4, S-IC.B.5, S-IC.B.6: margins of error from simulation, comparing treatments by re-randomization, evaluating
reports based on data (sets 27-31).

Convention stated in every margin-of-error question: margin of error = 2 × (standard deviation of the simulated sample
statistics), so an interval is estimate ± margin of error."""
from fractions import Fraction as Fr

from qb import S, B, sa, mc, tf
from common import why, n, mean, dlist, tbl
from datasets import D
from data_id1 import histf
from data_ic1 import RULE5, rule

def plant(counted):
    return rule('the "no difference" model (plant food does not change growth)', counted + ' (A minus B; a one-sided check)').replace(
        'with the data;', 'with the data and the difference is significant;').replace(
        'otherwise it is consistent', 'otherwise it is consistent and the difference is not significant')

MOE = ' Use margin of error = 2 × (standard deviation of the simulated values).'
SLEEP = D('S28 sleep', [7, 6.5, 8, 7.5, 6, 9, 7, 8], 'hours', 'Hours of sleep reported by a random sample of 8 students')
GA = D('S29 group A', [14, 11, 13, 12, 15], 'cm', 'Growth of 5 plants randomly assigned to plant food A')
GB = D('S29 group B', [10, 12, 9, 11, 8], 'cm', 'Growth of 5 plants randomly assigned to plant food B')
assert mean(SLEEP) == Fr(59, 8) and mean(GA) == 13 and mean(GB) == 10
PE = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
PC = [3, 26, 71, 72, 25, 3]
assert sum(PC) == 200
PHIST = histf(PE, PC, 'Sample proportion', 10, 80)
GT = tbl(['Plant food', 'Growth of the 5 plants (cm)'], [['A', dlist(GA)], ['B', dlist(GB)]])

SETS = [
    # ------------------------------------------------------------------ 27. IC.B.4 estimate a proportion
    S('HSS-IC.B.4', 'Estimate a population proportion with a margin of error', num=27,
      target='Use data from a sample survey to estimate a population proportion, and develop a margin of error from a '
             'simulation of random sampling',
      strand='core', covers=['IC4-prop'],
      main=[
          sa('In a random sample of 400 adults, 248 favor a new park. What is the sample proportion? Give a decimal.',
             'Proportion:', key='0.62', note='248/400.'),
          sa('(Hypothetical simulation results.) 500 random samples of size 400 were simulated from a population with proportion 0.62. The simulated sample '
             'proportions had standard deviation 0.024.%s What is the margin of error?' % MOE, 'Margin of error:', key='0.048',
             note='2 · 0.024.'),
          sa('A sample proportion is 0.62 and the margin of error is 0.048. Give the interval of plausible values for the '
             'population proportion.', ['From:', 'To:'], key='0.572; 0.668', note='Form required: both. 0.62 ± 0.048.'),
          sa('The histogram shows 200 simulated sample proportions. How many of them are between 0.35 and 0.45 (bins 0.35-0.40 and '
             '0.40-0.45)?', 'Number:', key='143', fig=PHIST, note='71 + 72.'),
          mc('A poll of a random sample reports that 54% of voters support a measure, with a margin of error of 3 percentage '
             'points. Which conclusion is best supported?', [
              'A majority plausibly supports it: 51% to 57% are all above 50%.',
              'Exactly 54% of all voters support the measure.',
              'Support could plausibly be anywhere from 0% to 100%.',
              'The poll shows that support is below 50%.'],
             note='54 ± 3 gives 51% to 57%.'),
      ],
      back=[
          B('Compute a sample proportion and name it', 'HSS-IC.A.1', [
              sa('In a random sample of 250 students, 90 walk to school. What is the sample proportion? Give a decimal.',
                 'Proportion:', key='0.36', note='90/250.'),
              tf('A sample proportion is a statistic.', key=True, note='It describes the sample.'),
              mc('The proportion of all voters in a state who favor a law is a', ['parameter', 'statistic', 'sample', 'margin of error'],
                 note='Describes the population.'),
              sa('In a random sample of 80 phones, 6 were defective. What is the sample proportion? Give a decimal.', 'Proportion:',
                 key='0.075', note='6/80.'),
              tf('Different random samples always give the same sample proportion.', key=False, note='They vary.'),
          ], align='exact',
            why=why('the student cannot compute or name the sample statistic.', 'the estimate starts from it.',
                    'computes sample proportions.')),
          B('Read a standard deviation as typical variation', 'HSS-ID.A.2', [
              tf('A standard deviation measures how far values typically are from their mean.', key=True, note='Meaning.'),
              mc('(Hypothetical simulation results.) Simulated proportions from samples of size 100 have SD 0.05; from samples of size 400, SD 0.025. Which vary '
                 'less?', ['the proportions from samples of size 400', 'the proportions from samples of size 100',
                           'they vary the same', 'cannot tell'], note='Smaller SD.'),
              sa('Compute 2 × 0.031.', 'Answer:', key='0.062', note='Doubling.'),
              tf('A larger standard deviation means the values are more tightly clustered.', key=False, note='More spread.'),
              mc('About what percent of values in a roughly normal distribution lie within 2 SDs of the mean?', [
                  '95%', '68%', '50%', '99.7%'], note='The rule behind the convention.'),
          ], align='exact',
            why=why('the student does not connect the SD of simulated values with their spread.', 'the margin of error is two '
                    'of them.', 'reads and doubles a standard deviation.')),
      ],
      f1=B('See how sample size changes the margin of error', 'HSS-IC.B.4', [
          sa('For a sample proportion near 0.5, the margin of error is about 2·√(0.5·0.5/n). Find it for n = 400 and n = 100.',
             ['n = 400:', 'n = 100:'], key='0.05; 0.1', note='Form required: both. 2·0.025 and 2·0.05.'),
          tf('Making the sample 4 times as large cuts the margin of error about in half.', key=True, note='√4 = 2.'),
          mc('A pollster wants a smaller margin of error. What should change?', [
              'take a larger random sample', 'take a smaller random sample', 'ask only volunteers', 'round the results'],
             note='Larger n.'),
          sa('(Hypothetical simulation results.) Simulated proportions from samples of size 900 have SD 0.016.%s What is the margin of error?' % MOE,
             'Margin of error:', key='0.032', note='2 · 0.016.'),
          tf('A larger sample removes the bias of a poorly worded question.', key=False, note='Size does not fix bias.'),
      ], prog='same-course deepening', demand='Predict and compute how the margin of error depends on sample size.'),
      f2=B('Read margins of error in poll reports', 'HSS-IC.B.6', [
          mc('Candidate A has 48% and candidate B has 45%, each with a margin of error of 4 percentage points. What is the best '
             'conclusion?', [
              'No clear leader: the two intervals overlap a lot.', 'A is certainly ahead of B by exactly 3 points.',
              'B is certainly behind A by at least 3 points.', 'Both candidates have under 50%, so both lose.'],
             note='44%-52% and 41%-49% overlap a lot, so a cautious reading is that the poll shows no clear leader. The others claim certainty the poll cannot give, or confuse sample percents with winning.'),
          sa('A report gives 62% with a margin of error of 5 percentage points. Give the interval in percents.', ['From:', 'To:'],
             key='57%; 67%', note='Form required: both.'),
          tf('A margin of error describes only random sampling variation, not bias from how the sample was chosen.', key=True,
             note='It assumes a random sample.'),
          mc('A website poll of 10,000 visitors reports 70% ± 1%. Why is the margin of error misleading?', [
              'The visitors chose themselves, so the sample is not random.', 'The sample is too small for a margin of error.',
              'A margin of error must be at least 5%.', 'Percents cannot have a margin of error.'],
             note='Self-selected sample.'),
          tf('If two candidates\' intervals overlap, the poll proves that they are tied.', key=False,
             note='It shows the difference is not clear, not that they are tied.'),
      ], prog='cross-standard extension', demand='Use margins of error to judge claims in poll reports.',
        builds='Builds on FORWARD 1: knowing what controls the margin of error, the student judges reports that use one.')),

    # ------------------------------------------------------------------ 28. IC.B.4 estimate a mean
    S('HSS-IC.B.4', 'Estimate a population mean with a margin of error', num=28,
      target='Use data from a sample survey to estimate a population mean, and develop a margin of error from a simulation of '
             'random sampling',
      strand='core', covers=['IC4-mean'],
      main=[
          sa('A random sample of 8 students reported these hours of sleep: %s. What is the sample mean?' % dlist(SLEEP), 'Mean:',
             key='7.375', note='59/8.'),
          sa('(Hypothetical simulation results.) Simulated random samples of 8 students gave sample means with standard deviation 0.15 hour.%s What is the margin of '
             'error?' % MOE, 'Margin of error (hours):', key='0.3', note='2 · 0.15.'),
          sa('A sample mean is 7.4 hours with a margin of error of 0.3 hour. Give the interval of plausible values for the '
             'population mean.', ['From:', 'To:'], key='7.1; 7.7', note='Form required: both.'),
          mc('A study reports a mean of 7.4 hours of sleep with a margin of error of 0.3 hour, from a random sample. Which '
             'interpretation is correct?', [
              'Population means from 7.1 to 7.7 hours are plausible.', 'Every student sleeps between 7.1 and 7.7 hours.',
              'The population mean is exactly 7.4 hours.', 'Half of all students sleep 7.4 hours.'],
             note='The interval is for the mean, not for individuals.'),
          sa('(Hypothetical simulation results.) In 1,000 simulated samples, the middle 95% of sample means ran from 41.2 to 44.8. Give the center of this interval '
             'and the margin of error (half its width).', ['Center:', 'Margin of error:'], key='43; 1.8',
             note='Form required: both. (41.2 + 44.8)/2 and (44.8 - 41.2)/2.'),
      ],
      back=[
          B('Use a margin of error', 'HSS-IC.B.4', [
              sa('An estimate is 0.40 with a margin of error of 0.06. Give the interval.', ['From:', 'To:'], key='0.34; 0.46',
                 note='Form required: both.'),
              tf('Margin of error = 2 × 0.05 = 0.1 when the simulated values have SD 0.05.', key=True, note='Convention.'),
              mc('Which estimate has the widest interval?', ['20 ± 4', '20 ± 2', '20 ± 1', '20 ± 0.5'], note='Largest margin.'),
              sa('An interval runs from 12 to 18. What is the margin of error?', 'Margin of error:', key='3', note='Half of 6.'),
              tf('An interval from 0.30 to 0.40 has center 0.30.', key=False, note='Center 0.35.'),
          ], align='exact',
            why=why('the student cannot build or read an interval.', 'means use the same form as proportions.', 'builds intervals '
                    'from an estimate and a margin.')),
          B('Compute a mean', '6.SP.B.5.c', [
              sa('Find the mean of 4, 6, 8, 10.', 'Mean:', key='7', note='28/4.'),
              sa('Find the mean of 6.5, 7, 8.5, rounded to three decimal places.', 'Mean:', key='7.333', note='22/3 = 7.333..., to three decimal places.'),
              tf('The mean of 2, 4, 9 is 5.', key=True, note='15/3.'),
              mc('What is the mean of 10, 12, 14, 20?', ['14', '13', '12', '56'], note='56/4.'),
              tf('The mean of a data set must be one of its values.', key=False, note='Not necessarily.'),
          ], align='supporting',
            why=why('the student cannot compute the sample mean.', 'it is the estimate.', 'computes means.')),
      ],
      f1=B('Compare variability of sample means', 'HSS-IC.B.4', [
          mc('Sample means from samples of size 9 have SD 2; from samples of size 36, SD 1. Which statement is correct?', [
              'Means of larger samples vary less, so the margin of error is smaller.',
              'Means of larger samples vary more, so the margin is larger.',
              'Both sample sizes give the same margin of error.',
              'Sample size has no effect at all on sample means.'], note='Quadrupling n halves the SD.'),
          sa('(Hypothetical simulation results.) Simulated sample means from samples of size 36 have SD 1.%s What is the margin of error?' % MOE,
             'Margin of error:', key='2', note='2 · 1.'),
          tf('Individual values vary more than means of samples of those values.', key=True, note='Averaging reduces spread.'),
          sa('An estimate of 52 has a margin of error of 2. Is 55 a plausible population mean? Enter yes or no.', 'Answer:',
             key='no', note='50 to 54.'),
          tf('A margin of error corrects the bias of a convenience sample.', key=False,
             note='A margin of error describes only random sampling variation; it does not fix bias from how the sample was chosen.'),
      ], prog='same-course deepening', demand='Relate sample size to the spread of sample means and judge values.'),
      f2=B('Compare two treatments\' means', 'HSS-IC.B.5', [
          sa('Plant food A: mean growth 13 cm; plant food B: mean growth 10 cm. What is the difference (A minus B)?',
             'Difference:', key='3', note='13 - 10.'),
          mc('An experiment\'s difference in means could be due to the treatments or to chance. What tool checks chance?', [
              'a re-randomization simulation', 'a larger margin of error', 'a census', 'a scatter plot'],
             note='Re-randomization models "no effect".'),
          tf('A difference in means from a randomized experiment is always caused by the treatment.', key=False,
             note='It may be chance.'),
          sa('(Hypothetical simulation results.) In 200 re-randomizations, a difference of 3 or more occurred 4 times. What proportion? Give a decimal.',
             'Proportion:', key='0.02', note='4/200.'),
          tf('A difference that chance alone produces in only 2% of re-randomizations is significant under a 5% rule.', key=True,
             note='2% < 5%.'),
      ], prog='cross-standard extension', demand='Move from estimating one mean to comparing two treatment means.',
        builds='Builds on FORWARD 1: variability of means, now understood, is used to judge a difference between two means.')),

    # ------------------------------------------------------------------ 29. IC.B.5 compare treatments
    S('HSS-IC.B.5', 'Compare two treatments with a randomization simulation', num=29,
      target='Use data from a randomized experiment to compare two treatments, and use a re-randomization simulation to decide '
             'whether the difference is significant',
      strand='core', covers=['IC5-compare'],
      main=[
          sa('Ten plants were randomly assigned to plant food A or B. Find the mean growth for each group and the difference '
             '(A minus B).', ['Mean A:', 'Mean B:', 'Difference:'], key='13; 10; 3', fig=GT,
             note='Form required: all three. 65/5, 50/5.'),
          sa('(Hypothetical simulation results.) In an experiment, 10 plants were randomly assigned to two plant foods (5 each), and the difference in mean growth was '
             '3 cm. The 10 results were re-randomized into two groups of 5 a total of 200 times. A difference of 3 or more occurred 4 '
             'times. What proportion of the re-randomizations is that? Give a decimal.', 'Proportion:', key='0.02',
             note='4/200.'),
          mc('(Hypothetical simulation results.) Ten plants were randomly assigned to plant food A or B (5 each); mean growth A minus B was 3 cm. In 200 '
             're-randomizations, a difference (A minus B) of 3 or more occurred 4 times.%s Which decision is correct?' % (
                 plant('differences of 3 or more')), [
              'The difference is significant: chance gave it only 2% of the time.',
              'The difference is not significant: it happened 4 times by chance.',
              'The difference is not significant: the groups had only 5 plants.',
              'The difference is significant: any difference is significant.'],
             note='2% < 5%.'),
          mc('In an experiment, 10 plants were randomly assigned to plant food A or B (5 each). What does one re-randomization of '
             'the 10 growth results do?', [
              'Reshuffles the 10 results into groups of 5, ignoring food.',
              'Grows 10 new plants, again using the two plant foods.', 'Repeats the whole experiment with many more plants.',
              'Swaps the means of the two original groups of plants.'],
             note='It models the "no difference" assumption.'),
          mc('(Hypothetical simulation results.) In another plant-food experiment with random assignment, mean growth A minus B was 1.2 cm. In 200 re-randomizations, '
             'differences (A minus B) of 1.2 or more occurred 62 times.%s Which decision is correct?' % (
                 plant('differences of 1.2 or more')), [
              'Not significant: chance gave such a difference 31% of the time.',
              'Significant: 62 is a large number of re-randomizations.',
              'Significant: the difference 1.2 is greater than 0.',
              'Not significant: re-randomizations can never be significant.'],
             note='62/200 = 31% ≥ 5%.'),
      ],
      back=[
          B('Decide whether a model is consistent with data', 'HSS-IC.A.2', [
              tf('A result that would happen rarely under a model is evidence against the model.', key=True, note='Logic of the test.'),
              sa('(Hypothetical simulation results.) A result at least as extreme happened in 3 of 150 simulated trials. What proportion? Give a decimal.',
                 'Proportion:', key='0.02', note='3/150.'),
              mc('Under the 5% rule, a result as extreme as the data occurred in 12% of trials. The decision is', [
                  'consistent with the model', 'not consistent with the model', 'the model is proven', 'no decision'],
                 note='12% ≥ 5%.'),
              tf('Under the 5% rule, 4% of trials means the model is consistent.', key=False, note='4% < 5%.'),
              mc('Which proportion of simulated results gives the strongest evidence against a model?', [
                  '0.001', '0.04', '0.2', '0.5'], note='Smallest.'),
          ], align='exact',
            why=why('the student cannot apply the decision rule.', 'deciding significance uses the same rule.',
                    'decides from a proportion and a threshold.')),
          B('Explain random assignment', 'HSS-IC.B.3', [
              tf('Random assignment tends to make the treatment groups similar before treatment, although chance differences remain.', key=True, note='It tends to balance other variables between the groups; it does not make them identical.'),
              mc('In an experiment, plants were assigned to two plant foods at random. Why?', [
                  'so growth differences can be credited to food', 'so that more of the plants grow well',
                  'so the two group means come out equal', 'so that no plant needs to be measured'], note='Purpose.'),
              tf('In an experiment, subjects choose which treatment they receive.', key=False, note='The researcher assigns.'),
              mc('Ten plants are numbered 1-10. Which assignment is random?', [
                  'draw 5 numbers from a hat for food A', 'put the 5 tallest plants on food A', 'let the gardener choose',
                  'put plants 1-5 on food A'], note='Chance.'),
              tf('Random assignment is what allows an experiment to support a conclusion about cause.', key=True, note='Key idea.'),
          ], align='exact',
            why=why('the student does not see why an experiment\'s groups are formed randomly.', 're-randomization imitates '
                    'that process.', 'explains random assignment.')),
          B('Compute means of small groups', '6.SP.B.5.c', [
              sa('Find the mean of 14, 11, 13, 12, 15.', 'Mean:', key='13', note='65/5.'),
              sa('Find the mean of 10, 12, 9, 11, 8.', 'Mean:', key='10', note='50/5.'),
              tf('The difference of the means 13 and 10 is 3.', key=True, note='13 - 10.'),
              mc('Find the mean of 2.5, 3, 3.5, 5.', ['3.5', '3.25', '14', '3'], note='14/4.'),
              tf('The mean of 8, 9, 10, 11, 12 is 11.', key=False, note='10.'),
          ], align='supporting',
            why=why('the student cannot compute the group means.', 'the comparison uses their difference.', 'computes means.')),
      ],
      f1=B('Use differences in either direction', 'HSS-IC.B.5', [
          sa('(Hypothetical simulation results.) In 200 re-randomizations, differences of 3 or more occurred 4 times and differences of -3 or less occurred 5 times. '
             'What proportion is at least 3 away from 0 in either direction? Give a decimal.', 'Proportion:', key='0.045',
             note='9/200.'),
          tf('Under a 5% rule, a proportion of 0.045 means the difference is significant.', key=True, note='0.045 < 0.05.'),
          mc('With more plants per group, re-randomized differences tend to be', [
              'closer to 0', 'farther from 0', 'exactly 0', 'always positive'], note='Less variability.'),
          sa('Treatment mean 31, control mean 28. What is the difference (treatment minus control)?', 'Difference:', key='3',
             note='31 - 28.'),
          tf('A significant difference proves that the treatment helps every individual.', key=False,
             note='It is about the groups on average.'),
      ], prog='same-course deepening', demand='Count extreme differences in both directions and reason about group size.'),
      f2=B('Evaluate a report of an experiment', 'HSS-IC.B.6', [
          mc('A company reports: "Our drink improved scores in a study." The study gave the drink to 10 volunteers and compared '
             'them with 10 who chose not to drink it. What is the main flaw?', [
              'Subjects chose their own group: no random assignment.', 'Twenty subjects is too many for a study.',
              'Scores of two groups cannot be compared.', 'Drinks cannot be studied in an experiment.'], note='Self-selection.'),
          tf('A report should say whether a difference could plausibly be due to chance.', key=True, note='Significance.'),
          mc('(Hypothetical simulation results.) A report says a new method raised mean scores from 70 to 71, "a significant improvement." Re-randomization shows '
             'such differences 40% of the time. What is the best response?', [
              'Not supported: chance often gives such differences.', 'Supported: 71 is higher than 70.',
              'Proven true: the study was an experiment.', 'The new method actually lowered scores.'], note='40% ≥ 5%.'),
          tf('A randomized experiment on adults automatically applies to children.', key=False, note='Scope is the subjects.'),
          mc('Which detail most strengthens a report\'s causal claim?', [
              'subjects were randomly assigned to treatments', 'the report used colorful, eye-catching graphs',
              'the study had a long and technical name', 'the researchers felt confident in the result'], note='Design.'),
      ], prog='cross-standard extension', demand='Apply experiment-comparison ideas to claims in reports.',
        builds='Builds on FORWARD 1: the significance reasoning is used to check how others report experiments.')),
]
