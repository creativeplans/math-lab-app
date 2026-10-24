"""S-ID.C.8, S-ID.C.9: computing and interpreting the correlation coefficient; correlation and causation (sets 19-21)."""
from qb import S, B, sa, mc, tf
from common import why, cand, pick, corr, TECH
from data_id3 import SA, SB, SE, FIG_A, FIG_B, FIG_C, FIG_D, FIG_E, NEG, POS, WNEG, CURV
from data_id4 import D1, D2, xy, SAT, SBT


def r_(pts, k=2):
    return ('%.' + str(k) + 'f') % corr([p[0] for p in pts], [p[1] for p in pts])


assert (r_(SA), r_(SB), r_(D2), r_(D1)) == ('0.99', '-0.97', '-0.99', '0.99')
assert (r_(SE, 3), r_(SE[:6], 3)) == ('-0.008', '0.999')
assert r_(WNEG) == '-0.45' and r_([(1, 2), (2, 5), (3, 4), (4, 7)]) == '0.87'
SET_ = xy(SE, 'Temperature (°F)', 'Cones sold')

SETS = [
    # ------------------------------------------------------------------ 19. ID.C.8 compute r
    S('HSS-ID.C.8', 'Compute the correlation coefficient with technology', num=19,
      target='Compute (using technology) the correlation coefficient r of a linear fit',
      strand='core', covers=['ID8-compute'],
      main=[
          sa('Find the correlation coefficient r for hours studied and score. Round to two decimal places.%s' % TECH, 'r:',
             key=r_(SA), fig=SAT, note='r = 0.9920.'),
          sa('Find the correlation coefficient r for car age and value. Round to two decimal places.%s' % TECH, 'r:',
             key=r_(SB), fig=SBT, note='r = -0.9654.'),
          sa('Find the correlation coefficient r for hours after sunrise (x) and ice thickness in cm (y). Round to two decimal '
             'places.%s' % TECH, 'r:', key=r_(D2), fig=xy(D2, 'Hours', 'Thickness (cm)'), note='r = -0.9949.'),
          sa('Find r for the temperature and cones-sold data for all 7 days, and again without the 90-degree day. Round each to '
             'three decimal places.%s' % TECH, ['All 7 days:', 'Without the 90-degree day:'], key='%s; %s' % (r_(SE, 3), r_(SE[:6], 3)),
             fig=SET_, note='Form required: both. -0.0077 and 0.9992.'),
          sa('Find the correlation coefficient r for the spring data (mass and length). Round to two decimal places.%s' % TECH,
             'r:', key=r_(D1), fig=xy(D1, 'Mass (g)', 'Length (cm)'), note='r = 0.9881.'),
      ],
      back=[
          B('Find means and deviations', '6.SP.B.5.c', [
              sa('Find the mean of 1, 2, 3, 4, 5.', 'Mean:', key='3', note='15/5.'),
              sa('For the values 2, 5, 4, 7 (mean 4.5), find the deviations of 2 and 7 from the mean.', ['2:', '7:'],
                 key='-2.5; 2.5', note='Form required: both.'),
              tf('The deviations of a data set from its mean always add to 0.', key=True, note='Balance property.'),
              mc('What is the mean of 48, 44, 41, 35, 33, 28, rounded to two decimal places?', ['38.17', '38', '41', '35'],
                 note='229/6 = 38.1666... ≈ 38.17.'),
              tf('A value below the mean has a positive deviation.', key=False, note='Negative.'),
          ], align='supporting',
            why=why('the student cannot find means and deviations.', 'r combines the deviations of x and y.',
                    'computes means and signed deviations.')),
          B('Read the direction of an association', 'HSS-ID.B.6', [
              mc('The scatter plot shows car age and value. What is the sign of r?', ['negative', 'positive', 'zero',
                                                                                  'cannot be found'],
                 fig=FIG_B, note='Values fall as age rises.'),
              tf('For the hours-studied scatter plot, r is positive.', key=True, fig=FIG_A, note='Rising pattern.'),
              mc('For the shoe-size scatter plot, r is closest to', ['0', '1', '-1', '0.9'], fig=FIG_D,
                 note='No linear pattern.'),
              tf('For a cloud of points with no pattern, r is close to 1.', key=False, note='Close to 0.'),
              mc('Which scatter plot would have r close to -1?', [
                  'points falling closely along a line', 'points rising closely along a line', 'a shapeless cloud',
                  'points along a U-shaped curve'], note='Strong negative linear.'),
          ], align='exact',
            why=why('the student cannot predict the sign and rough size of r from a plot.', 'that check catches entry errors.',
                    'estimates r from a scatter plot.')),
      ],
      f1=B('Compute r from deviations', 'HSS-ID.C.8', [
          sa('For (1, 2), (2, 5), (3, 4), (4, 7): Σ(x - x̄)(y - ȳ) = 7, Σ(x - x̄)^2 = 5 and Σ(y - ȳ)^2 = 13. Compute '
             'r = 7/√(5·13), rounded to two decimal places.', 'r:', key='0.87', note='7/√65 = 0.868.'),
          tf('If all points lie exactly on a line with positive slope, r = 1.', key=True, note='Perfect positive.'),
          sa('For the points (1, 2), (2, 4), (3, 6), what is r?', 'r:', key='1', note='Exactly on y = 2x.'),
          mc('A calculator reports r = 1.4. What should you conclude?', [
              'A mistake was made: r is always between -1 and 1.', 'The association is very strong and positive.',
              'The slope of the line is 1.4.', 'The data have one outlier.'], note='|r| ≤ 1.'),
          tf('For the points (1, 6), (2, 4), (3, 2), r = 1.', key=False, note='r = -1 (falling line).'),
      ], prog='same-course deepening', demand='Compute r from its formula and check results for sense.'),
      f2=B('See how changes to the data affect r', 'HSS-ID.C.8', [
          tf('Changing x from hours to minutes does not change r.', key=True, note='r has no units.'),
          tf('Swapping the roles of x and y changes the value of r.', key=False, note='r is symmetric.'),
          mc('For the cones data, r = 0.999 for six days and -0.008 with the 90-degree day included. What does this show?', [
              'One outlier can change r dramatically.', 'r is not affected by outliers.',
              'The six days have no association.', 'Temperature causes cone sales to fall.'],
             fig=FIG_E, note='The single point erases the pattern.'),
          sa('Find r for (1, 3), (2, 5), (3, 7), and for the same points with every y increased by 10. Give both.',
             ['Original:', 'After adding 10:'], key='1; 1', note='Form required: both. Adding a constant does not change r.'),
          mc('Which change to a data set could change r?', [
              'adding a new point far from the others', 'adding 5 to every x-value', 'doubling every y-value',
              'converting y from meters to centimeters'], note='Shifts and positive rescalings leave r unchanged.'),
      ], prog='same-course deepening', demand='Predict how transformations and outliers change r.',
        builds='Builds on FORWARD 1: r computed from deviations explains why units, shifts and outliers act as they do.')),

    # ------------------------------------------------------------------ 20. ID.C.8 interpret r
    S('HSS-ID.C.8', 'Interpret the correlation coefficient', num=20,
      target='Interpret the correlation coefficient of a linear fit: its sign (direction), its size (strength), and that it '
             'measures only linear association',
      strand='core', covers=['ID8-interpret'],
      main=[
          mc('For car age and value, r = -0.97. Which interpretation is correct?', [
              'strong negative linear association', 'weak negative linear association', 'strong positive linear association',
              'no association'], note='|r| near 1, negative.'),
          mc('For speed and fuel efficiency, r = 0.25 but the scatter plot shows a clear curve. Which statement is correct?', [
              'r measures only linear association, so it misses the curve.', 'There is no relationship between the variables.',
              'There is a weak linear relationship and nothing more.', 'r must have been computed incorrectly.'],
             fig=FIG_C, note='A strong nonlinear relationship can have r near 0.'),
          mc('Which correlation coefficient shows the strongest linear association?', ['-0.91', '0.85', '0.10', '-0.40'],
             note='Largest |r|.'),
          mc('For the cones data, r = -0.008 for all 7 days but 0.999 without the 90-degree day. Which interpretation is best?', [
              'The six typical days show a strong positive linear association.',
              'Temperature and cone sales have no relationship on any day.',
              'Hotter days have fewer cones sold.',
              'The 90-degree day is the most typical day.'],
             fig=FIG_E, note='The outlier hides the pattern.'),
          mc('Which statement about r is correct?', [
              'r has no units and stays the same if the units change.', 'r changes when x is converted from hours to minutes.',
              'r can be as large as 5 for very strong data.', 'r is negative whenever the data contain an outlier.'],
             note='r is unit-free and between -1 and 1.'),
      ],
      back=[
          B('Describe strength and direction from a plot', 'HSS-ID.B.6', [
              mc('The scatter plot shows hours studied and score. How strong is the linear association?', [
                  'strong', 'weak', 'none', 'cannot be judged'], fig=FIG_A, note='Points hug a line.'),
              tf('In a strong association, the points lie close to a line or curve.', key=True, note='Strength.'),
              mc('The scatter plot shows shoe size and quiz score. How strong is the association?', ['very weak or none',
                                                                                                  'strong positive',
                                                                                                  'strong negative',
                                                                                                  'perfect'],
                 fig=FIG_D, note='No pattern.'),
              tf('A scatter plot that falls from left to right shows a positive association.', key=False, note='Negative.'),
              mc('The scatter plot of speed and fuel efficiency has what form?', ['curved', 'linear', 'no form', 'exponential growth'],
                 fig=FIG_C, note='Rises then falls.'),
          ], align='exact',
            why=why('the student cannot read strength and form from a plot.', 'r summarizes the linear part of that picture.',
                    'describes strength and form.')),
          B('Compare numbers on a scale from -1 to 1', '6.NS.C.7.c', [
              sa('What is |-0.91|?', 'Answer:', key='0.91', note='Distance from 0.'),
              tf('|-0.8| > |0.6|.', key=True, note='0.8 > 0.6.'),
              mc('Which is closest to 0?', ['-0.1', '0.5', '-0.6', '0.9'], note='Smallest absolute value.'),
              tf('-0.9 is greater than 0.2.', key=False, note='-0.9 < 0.2, though |-0.9| is larger.'),
              sa('Which has the greater absolute value, -0.75 or 0.7? Enter the number.', 'Number:', key='-0.75',
                 note='0.75 > 0.7.'),
          ], align='supporting',
            why=why('the student confuses a number\'s size with its sign.', 'strength is |r|, direction is the sign.',
                    'compares absolute values.')),
      ],
      f1=B('Match correlation coefficients to scatter plots', 'HSS-ID.C.8', [
          pick('Which scatter plot has r ≈ -0.45?', 'B', [
              cand([], 'points falling loosely with wide scatter', pts=[(a, b, '') for a, b in WNEG]),
              cand([], 'points falling steadily in a narrow band', pts=[(a, b, '') for a, b in NEG]),
              cand([], 'points rising steadily in a narrow band', pts=[(a, b, '') for a, b in POS]),
              cand([], 'points falling then rising in a U shape', pts=[(a, b, '') for a, b in CURV])],
               'Weak negative. The others have r ≈ -1.00, 1.00 and 0.', x=(0, 10), y=(0, 10)),
          mc('A U-shaped scatter plot that is perfectly symmetric has r equal to', ['0', '1', '-1', '0.5'],
             note='The rising and falling halves cancel.'),
          tf('r = -0.45 indicates a stronger linear association than r = 0.30.', key=True, note='0.45 > 0.30.'),
          mc('Which value of r goes with points falling steadily in a narrow band?', ['-0.99', '-0.45', '0', '0.99'],
             note='Strong negative.'),
          tf('Two data sets with the same r must have scatter plots of the same shape.', key=False,
             note='Very different plots can share an r.'),
      ], prog='same-course deepening', demand='Connect values of r with the look of scatter plots.'),
      f2=B('Correlation is not causation', 'HSS-ID.C.9', [
          mc('Across towns, the number of libraries and the number of crimes have r = 0.9. Which is the best explanation?', [
              'Larger towns tend to have more of both.', 'Libraries cause crime.', 'Crime causes towns to build libraries.',
              'r = 0.9 proves a cause in one direction.'], note='Population is a lurking variable.'),
          tf('A correlation of r = 0.95 shows that changes in x cause changes in y.', key=False,
             note='Strong correlation is not evidence of cause by itself.'),
          mc('Which kind of study can show that x causes y?', [
              'a randomized experiment', 'a survey with many people', 'a study with r close to 1', 'a scatter plot of past data'],
             note='Random assignment.'),
          tf('A lurking variable can produce a strong correlation between two variables that do not affect each other.', key=True,
             note='Both follow it.'),
          mc('Students who sleep more have higher grades (r = 0.6) in an observational study. Which conclusion is justified?', [
              'Sleep and grades are positively associated in this group.', 'More sleep causes higher grades for these students.',
              'Higher grades cause these students to sleep more.', 'Sleep and grades are unrelated for these students.'],
             note='Only association is shown.'),
      ], prog='cross-standard extension', demand='Decide what a strong r does and does not justify.',
        builds='Builds on FORWARD 1: after reading what r measures, the student limits what it can be used to claim.')),

    # ------------------------------------------------------------------ 21. ID.C.9 correlation and causation
    S('HSS-ID.C.9', 'Distinguish between correlation and causation', num=21,
      target='Distinguish between correlation and causation: recognize lurking variables and the kind of study needed to '
             'support a causal claim',
      strand='core', covers=['ID9-cause'],
      main=[
          mc('Over several years, a city\'s sunscreen sales and its number of pool visits are strongly correlated. What best '
             'explains this?', ['Sunny, hot weather raises both.', 'Sunscreen causes people to swim.',
                                'Swimming causes people to buy sunscreen.', 'The data must be wrong.'],
             note='A lurking variable drives both.'),
          mc('Countries with more doctors per person have longer life spans. Which conclusion is justified?', [
              'Doctors per person and life span are positively associated.', 'Adding more doctors in a country will lengthen life spans.',
              'Longer life spans cause countries to train more doctors.',
              'Doctors per person and life span are unrelated.'],
             note='Observational data show association only; wealth may drive both.'),
          mc('Researchers want to know whether a new study app raises test scores. Which design can show cause?', [
              'Randomly assign students to use the app or not.', 'Survey students who already chose to use the app.',
              'Compare the scores of last year\'s users and nonusers.', 'Find the correlation of app use and scores.'],
             note='Random assignment balances other causes.'),
          mc('Children with larger shoe sizes have higher reading scores. What is the most likely lurking variable?', [
              'age', 'shoe brand', 'reading-book color', 'school lunch menu'], note='Older children have bigger feet and read better.'),
          mc('Which statement is correct?', [
              'Causation implies association, but association does not imply causation.',
              'Association implies causation when r is above 0.9.',
              'Causation can only be shown with a scatter plot.',
              'If two variables are not correlated, neither can cause anything.'],
             note='A causal link produces an association; the reverse need not hold.'),
      ],
      back=[
          B('Recognize a strong correlation', 'HSS-ID.C.8', [
              tf('r = -0.92 shows a strong linear association.', key=True, note='|r| near 1.'),
              mc('Which r shows the weakest linear association?', ['0.05', '-0.7', '0.6', '-0.95'], note='Smallest |r|.'),
              tf('A strong correlation means the two variables must be causally related.', key=False, note='Not necessarily.'),
              sa('A data set has r = 0.88. Is the linear association positive or negative? Enter positive or negative.',
                 'Answer:', key='positive', note='Sign of r.'),
              mc('r = 0.88 for study time and grades in a survey. What does it describe?', [
                  'a strong positive linear association', 'proof that study time causes grades', 'a weak association',
                  'a curved association'], note='Association only.'),
          ], align='exact',
            why=why('the student cannot read what an r value says.', 'causal claims usually start from a strong r.',
                    'reads strength and direction of r.')),
          B('Describe the association in a scatter plot', '8.SP.A.1', [
              tf('In the ice-cream scatter plot, the six typical days show a positive association.', key=True, fig=FIG_E,
                 note='Rising pattern.'),
              mc('The scatter plot shows car age and value. Which describes it?', ['negative linear association',
                                                                                  'positive linear association',
                                                                                  'no association', 'curved association'],
                 fig=FIG_B, note='Falling pattern.'),
              tf('A scatter plot can show an association between two variables that do not cause each other.', key=True,
                 note='Correlation without cause.'),
              mc('The scatter plot shows shoe size and quiz score of adults. Which describes it?', [
                  'no clear association', 'strong positive', 'strong negative', 'curved'], fig=FIG_D, note='Cloud.'),
              tf('An association seen in a scatter plot shows which variable is the cause.', key=False,
                 note='A plot cannot show cause.'),
          ], align='supporting',
            why=why('the student cannot describe the association being discussed.', 'causation questions start from one.',
                    'describes associations in plots.')),
      ],
      f1=B('Tell experiments from observational studies', 'HSS-IC.B.3', [
          mc('Researchers record the coffee intake and blood pressure of 500 adults without changing anything. What type of study is '
             'this?', ['observational study', 'randomized experiment', 'sample survey of opinions', 'simulation'],
             note='Nothing is imposed.'),
          tf('In a randomized experiment, the researcher assigns the treatments by chance.', key=True, note='Definition.'),
          mc('Which study is a randomized experiment?', [
              'Volunteers are randomly assigned to a new diet or the usual diet.',
              'Doctors record the diets their patients already follow.',
              'A survey asks people which diet they prefer.',
              'Researchers compare towns that chose different school lunches.'],
             note='Chance assignment of treatments.'),
          tf('An observational study can establish cause as well as a randomized experiment can.', key=False,
             note='It cannot control lurking variables.'),
          mc('Why does random assignment help support causal conclusions?', [
              'It tends to balance other variables between the groups.', 'It makes the sample larger than other designs do.',
              'It guarantees that r will be close to 1.', 'It removes all variability from the measurements.'],
             note='Balancing lurking variables.'),
      ], prog='cross-standard extension', demand='Classify study designs by whether they can support causal claims.'),
      f2=B('Judge causal claims from experiment results', 'HSS-IC.B.5', [
          sa('In a randomized experiment, 40 plants got fertilizer and grew a mean of 18 cm; 40 got none and grew a mean of 12 cm. '
             'What is the difference in means (fertilizer minus none)?', 'Difference (cm):', key='6', note='18 - 12.'),
          mc('Re-randomizing the plants many times gave differences of 6 cm or more only 1% of the time. What can be concluded?', [
              'The fertilizer likely caused more growth.', 'The difference is due to chance alone.',
              'Fertilizer is unrelated to growth.', 'No conclusion is possible without r.'],
             note='A rare difference under chance plus random assignment supports cause.'),
          tf('In a randomized experiment, a difference much larger than chance alone would produce supports a causal conclusion.',
             key=True, note='Random assignment rules out lurking variables.'),
          mc('An observational study found a large difference between coffee drinkers and others. Why can\'t it prove cause?', [
              'Coffee drinkers may differ in other ways that matter.', 'Observational studies do not collect any data.',
              'The difference was too large to be believable.', 'Coffee intake cannot be measured accurately.'], note='Lurking variables.'),
          tf('If an experiment\'s difference could easily happen by chance, the experiment proves the treatment has no effect.',
             key=False, note='It only fails to show an effect.'),
      ], prog='cross-standard extension', demand='Use random assignment and a chance comparison to judge a causal claim.',
        builds='Builds on FORWARD 1: once the design is known to be an experiment, its results are judged against chance.')),
]
