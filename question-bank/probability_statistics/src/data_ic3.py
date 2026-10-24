"""S-IC.B.6: evaluating reports based on data — conclusions against design, and statistics and displays (sets 30-31)."""
from qb import S, B, sa, mc, tf
from common import why

SETS = [
    # ------------------------------------------------------------------ 30. IC.B.6 evaluate claims
    S('HSS-IC.B.6', 'Evaluate the conclusions of reports based on data', num=30,
      target='Evaluate the conclusions of a report against how its data were produced: causation claims, generalization '
             'beyond the sample, and bias from sampling or question wording',
      strand='core', covers=['IC6-claims'],
      main=[
          mc('A report says: "Teens who eat breakfast get better grades, so eating breakfast raises grades." The data came from a '
             'survey of 2,000 randomly chosen teens. What is the main problem?', [
              'A survey shows association, not that breakfast causes better grades.',
              'A random sample of 2,000 teens is far too small for any survey.',
              'Grades cannot be compared between different groups of teens.',
              'Random samples cannot be used to describe a population of teens.'],
             note='Cause needs an experiment.'),
          mc('A magazine asked readers to mail in whether they liked their jobs; 80% of the 3,000 replies said no. The magazine '
             'reports that "80% of workers dislike their jobs." What is the main problem?', [
              'Readers chose to reply, so the sample is likely biased.', 'Three thousand replies is too few to report.',
              'The percent 80% was computed incorrectly.', 'Job satisfaction cannot be surveyed.'],
             note='Voluntary response.'),
          mc('A survey asked, "Don\'t you agree that the unfair new tax should be repealed?" What is the problem?', [
              'The wording pushes people toward one answer.', 'The question is too short to be answered.',
              'The sample must have been too large.', 'Tax questions cannot appear in surveys.'],
             note='Leading question: response bias.'),
          mc('A randomized experiment found that a reading program raised scores of 3rd graders in one district. Which conclusion '
             'is best supported?', [
              'The program caused higher scores for students like those in the study.',
              'The program will raise scores for students of every age everywhere.',
              'The program is associated with scores but did not cause any change.',
              'Nothing can be concluded, because only one district was studied.'],
             note='Cause for the subjects; limited generalization.'),
          mc('A report on 12 patients says a new treatment "works for everyone," because 9 of the 12 improved. Which criticism is '
             'most important?', [
              'No comparison group, and 3 of the 12 did not improve.', 'Twelve patients is too many to study at once.',
              'Improvement cannot be measured in patients.', 'The fraction 9/12 should have been written 12/9.'],
             note='No control; and "everyone" contradicts the data.'),
      ],
      back=[
          B('Know what each design can support', 'HSS-IC.B.3', [
              tf('Only a randomized experiment can support a cause-and-effect conclusion.', key=True, note='Among these designs.'),
              mc('Which design lets results be generalized to a population?', [
                  'a random sample from that population', 'a group of volunteers', 'a convenience sample', 'an experiment on friends'],
                 note='Random sampling.'),
              tf('An observational study can prove cause if it is large enough.', key=False, note='Size does not help.'),
              mc('A study used volunteers and random assignment. Its conclusions can include', [
                  'cause, for subjects like the volunteers', 'cause, for the whole population', 'nothing at all',
                  'association only'], note='Assignment yes, sampling no.'),
              tf('Random sampling and random assignment serve different purposes.', key=True, note='Generalize versus cause.'),
          ], align='exact',
            why=why('the student does not know what each design allows.', 'evaluating a claim compares it with the design.',
                    'states the scope of each design.')),
          B('Recognize lurking variables', 'HSS-ID.C.9', [
              mc('Cities with more police officers have more crimes. What is a likely lurking variable?', [
                  'city population', 'police uniforms', 'crime reports', 'the number of officers'], note='Size drives both.'),
              tf('A lurking variable affects both variables in an association.', key=True, note='Definition.'),
              mc('Students who take music lessons score higher in math. Which is a possible lurking variable?', [
                  'family income', 'the music teacher\'s name', 'math test length', 'the number of notes played'],
                 note='May affect both.'),
              tf('If an association is strong, there can be no lurking variable.', key=False, note='Strength does not exclude one.'),
              tf('Random assignment protects an experiment from lurking variables.', key=True, note='It balances them.'),
          ], align='exact',
            why=why('the student does not look for other explanations.', 'reports often skip them.', 'names lurking variables.')),
      ],
      f1=B('Identify the type of bias in a report', 'HSS-IC.B.6', [
          mc('A phone survey calls only landlines during work hours. Which bias is most likely?', [
              'undercoverage of people away or with only cell phones', 'response bias from the wording of questions',
              'voluntary response bias from self-selection', 'no bias, because calls are made at random'], note='Some groups cannot be reached.'),
          mc('Many people chosen for a survey refuse to answer. Which bias is this?', [
              'nonresponse bias', 'voluntary response bias', 'wording bias', 'measurement error'], note='Chosen but missing.'),
          tf('A larger sample removes bias caused by a poor sampling method.', key=False, note='It only reduces variability.'),
          mc('A survey of mall shoppers is used to describe all residents\' shopping habits. Which bias is this?', [
              'a convenience sample that is not representative', 'nonresponse bias from refusals to answer',
              'wording bias from a leading question', 'random sampling error only, with no bias'],
             note='Easy to reach, not representative.'),
          tf('People may give socially acceptable answers instead of true ones when asked sensitive questions.', key=True,
             note='Response bias.'),
      ], prog='same-course deepening', demand='Name the specific source of bias in a reported study.'),
      f2=B('Weigh several flaws and decide what a report shows', 'HSS-IC.B.6', [
          mc('An app maker reports: "Users who used our app for 30 days lost 8 pounds on average." The users were volunteers and '
             'there was no comparison group. Which conclusion is justified?', [
              'Only that these volunteers lost weight; the app\'s role is unclear.', 'The app causes weight loss in everyone who uses it.',
              'The study has shown that the app has no effect on weight.', 'Every single user of the app lost exactly 8 pounds.'],
             note='No control, no random sample.'),
          tf('A report that gives no information about how its sample was chosen should be treated with caution.', key=True,
             note='Cannot judge bias.'),
          mc('Which change would most improve the app study?', [
              'randomly assign volunteers to use the app or not', 'ask the users whether they liked the app',
              'extend the study from 30 days to 31 days', 'report the weight loss as a percent instead'], note='Comparison and random assignment.'),
          tf('A study funded by a company is always wrong about that company\'s product.', key=False,
             note='Funding is a reason to check the design, not proof of error.'),
          mc('Two reports disagree. Report 1 is a randomized experiment with 400 subjects; report 2 is a voluntary online poll of '
             '5,000. Which deserves more weight for a causal claim?', ['report 1', 'report 2', 'equal weight', 'neither'],
             note='Design beats size.'),
      ], prog='same-course deepening', demand='Combine design, bias and scope to decide what a report actually shows.',
        builds='Builds on FORWARD 1: after naming individual biases, the student weighs them together.')),

    # ------------------------------------------------------------------ 31. IC.B.6 evaluate statistics and displays
    S('HSS-IC.B.6', 'Evaluate the statistics and displays in reports', num=31,
      target='Evaluate the statistics and displays in a report: truncated axes, relative versus absolute change, margins of '
             'error, and the choice of summary statistic',
      strand='core', covers=['IC6-displays'],
      main=[
          sa('A bar graph\'s vertical axis starts at 50. One bar shows 52 and another shows 55. How tall is the second bar compared '
             'with the first (ratio of drawn heights), and what is the ratio of the actual values? Round the second answer to two '
             'decimal places.', ['Ratio of drawn heights:', 'Ratio of values:'], key='2.5; 1.06',
             note='Form required: both. (55 - 50)/(52 - 50) = 2.5; 55/52 = 1.0577.'),
          mc('An ad says a risk "increased 80%," from 1 in 10,000 to 1.8 in 10,000. Which statement is correct?', [
              'The absolute risk rose by only 0.8 in 10,000.', 'The risk is now 80 out of every 100 people.',
              'Most people will now be affected by it.', 'The risk went from 1% of people to 80%.'],
             note='Relative change sounds large; absolute change is tiny.'),
          mc('A poll shows candidate A at 51% and B at 49%, with a margin of error of 3 percentage points. A headline says "A '
             'leads!" What is the best evaluation?', [
              'Misleading: the gap is well within the margin of error.', 'Correct: 51% is more than 49%, so A leads.',
              'Correct: A has a majority of all the voters.', 'Misleading: B is certainly ahead of A.'],
             note='48%-54% and 46%-52% overlap.'),
          mc('A report gives the mean income in a town as $95,000, but most households earn under $50,000 and a few earn millions. '
             'What is the best evaluation?', [
              'The median would describe a typical household better.', 'The mean is the best summary for skewed data.',
              'The report must have added incomes incorrectly.', 'The range is the best measure of center.'],
             note='Right-skewed: the mean is pulled up.'),
          sa('A pictograph shows sales doubling by drawing a square icon twice as tall and twice as wide. How many times as large '
             'is the new icon\'s area?', 'Times as large:', key='4', note='2 · 2.'),
      ],
      back=[
          B('Use margins of error to compare results', 'HSS-IC.B.4', [
              sa('An estimate is 51% with a margin of error of 3 points. Give the interval.', ['From:', 'To:'], key='48%; 54%',
                 note='Form required: both.'),
              tf('If two intervals overlap a lot, the data do not clearly show which value is larger.', key=True, note='Too close.'),
              mc('Which pair of estimates (each ± 2 points) clearly differs?', ['40% and 50%', '48% and 50%', '49% and 51%',
                                                                                 '45% and 47%'],
                 note='38-42 and 48-52 do not overlap.'),
              tf('A margin of error of 3 points means the estimate is off by exactly 3 points.', key=False,
                 note='It bounds plausible values.'),
              sa('An interval is 46% to 52%. What is the estimate at its center?', 'Estimate:', key='49%', note='Midpoint.'),
          ], align='exact',
            why=why('the student cannot read intervals.', 'reports often skip the margin of error.', 'compares intervals.')),
          B('Compute percent change', '7.RP.A.3', [
              sa('A value rises from 1 to 1.8. What is the percent increase?', 'Percent:', key='80%', note='0.8/1.'),
              sa('A price rises from $40 to $50. What is the percent increase?', 'Percent:', key='25%', note='10/40.'),
              tf('A rise from 2 to 3 is a 50% increase.', key=True, note='1/2.'),
              mc('A count falls from 200 to 150. What is the percent decrease?', ['25%', '50%', '33%', '75%'], note='50/200.'),
              tf('A rise from 50 to 55 is a 5% increase.', key=False, note='5/50 = 10%.'),
          ], align='supporting',
            why=why('the student cannot compute relative change.', 'reports often state changes as percents.',
                    'computes percent change.')),
      ],
      f1=B('Spot misleading features of displays', 'HSS-IC.B.6', [
          mc('A line graph of monthly sales has a vertical axis from 980 to 1,000. What effect does this have?', [
              'Small changes look very large.', 'Large changes look very small.', 'It has no effect.',
              'It hides the months.'], note='Truncated axis.'),
          tf('A pie chart whose percents add to 130% is misleading or in error.', key=True,
             note='Parts of one whole add to 100%.'),
          sa('A graph\'s vertical axis starts at 90. Bars show 92 and 98. What is the ratio of the drawn heights?', 'Ratio:',
             key='4', note='8/2.'),
          tf('Using a 3-D effect on a pie chart never changes how large slices appear.', key=False, note='Perspective distorts.'),
          mc('Which display choice is most honest for comparing two counts of 52 and 55?', [
              'a bar graph with the axis starting at 0', 'a bar graph with the axis starting at 51', 'icons of different widths',
              'a 3-D pie chart'], note='Zero baseline.'),
      ], prog='same-course deepening', demand='Name and quantify distortions in common displays.'),
      f2=B('Reason about conditional rates in reports', 'HSS-CP.A.5', [
          mc('A report says "most car accidents happen within 5 miles of home, so driving near home is dangerous." What is the '
             'main flaw?', ['Most driving happens near home.', 'Accidents cannot be counted.', 'Five miles is too short.',
                            'Cars are safer far away.'],
             note='Rates need the amount of driving: P(accident given driving near home) is not reported.'),
          tf('Knowing that 90% of people in a hospital are sick does not tell you the chance that a sick person is in the hospital.',
             key=True, note='P(sick given in the hospital) differs from P(in the hospital given sick).'),
          mc('A test catches 95% of people who have a rare disease. A report concludes that 95% of people who test positive have '
             'it. What is the error?', [
              'It confuses P(positive given disease) with P(disease given positive).',
              'A test must catch 100% of cases before it is reported.',
              'Rare diseases cannot be tested for at all.',
              'The 95% should have been written as a fraction.'],
             note='Conditional probabilities are not symmetric.'),
          tf('A higher number of accidents involving red cars proves that red cars are more dangerous.', key=False,
             note='It depends on how many red cars there are.'),
          mc('To compare the safety of two car colors fairly, which statistic is needed?', [
              'accidents per car (or per mile) for each color', 'the total number of accidents for each color',
              'the number of different car colors sold', 'the average price of the cars of each color'], note='A rate.'),
      ], prog='cross-standard extension', demand='Recognize when a report needs a conditional rate rather than a count.',
        builds='Builds on FORWARD 1: after correcting distorted displays, the student corrects distorted rates.')),
]
