"""S-ID.B.6.a-c, S-ID.C.7: choosing and fitting models, residuals, least-squares lines, slope and intercept (sets 15-18)."""
from qb import S, B, sa, mc, tf
from common import why, n, tbl, cand, pick, resid_plot, lsrl, TECH
from datasets import D
from data_id3 import SA, SB, FIG_A, FIG_B, FIG_C


def r2(v):
    return '%.2f' % float(v)


def xy(pts, xn='x', yn='y'):
    """Data table: one row of x-values and one row of y-values."""
    return tbl([xn] + [n(p[0]) for p in pts], [[yn] + [n(p[1]) for p in pts]])


def coef(pts):
    a, b = lsrl([p[0] for p in pts], [p[1] for p in pts])
    return r2(b), r2(a)


D1 = D('S15 spring', [(2, 15), (4, 19), (5, 24), (7, 26), (8, 31), (10, 35)], '(grams, cm)',
       'Mass hung on a spring and the spring\'s length, 6 trials')
D2 = D('S17 ice', [(1, 48), (2, 44), (3, 41), (4, 35), (5, 33), (6, 28)], '(hours, cm)',
       'Hours after sunrise and thickness of a melting ice block')
RES = D('S16 fit', [(1, 3.5), (2, 4.6), (3, 7.2), (4, 8.8), (5, 11.1)], '(x, y)', 'Five measurements checked against the model y = 2x + 1')
SMALL = D('S16 small', [(1, 2), (2, 5), (3, 4), (4, 7)], '(x, y)', 'Four points for computing least-squares residuals by hand')
assert coef(D1) == ('2.52', '9.86') and coef(SA) == ('5.17', '48.28') and coef(SB) == ('-1.88', '25.87')
assert coef(D2) == ('-3.97', '52.07') and coef(SMALL) == ('1.40', '1.00')
RV = [(x, round(y - (2 * x + 1), 1)) for x, y in RES]  # residuals 0.5, -0.4, 0.2, -0.2, 0.1
assert [v for _, v in RV] == [0.5, -0.4, 0.2, -0.2, 0.1]
CURVED = [(1, -2), (2, 0.5), (3, 2), (4, 2.4), (5, 1.8), (6, 0.2), (7, -2.2)]
RANDOM = [(1, 0.6), (2, -0.8), (3, 0.3), (4, 0.9), (5, -0.5), (6, -0.2), (7, 0.7), (8, -0.9)]
FIG_CURVED = resid_plot(CURVED, (0, 8), (-3, 3), 'Residual plot: residuals -2, 0.5, 2, 2.4, 1.8, 0.2, -2.2 at x = 1 to 7, '
                        'forming an upside-down U.', xlabel='x')
FIG_RANDOM = resid_plot(RANDOM, (0, 9), (-1.5, 1.5), 'Residual plot: residuals 0.6, -0.8, 0.3, 0.9, -0.5, -0.2, 0.7, -0.9 at '
                        'x = 1 to 8, scattered above and below 0 with no pattern.', xlabel='x', ystep=0.5)
SAT = xy(SA, 'Hours', 'Score')
SBT = xy(SB, 'Age (years)', 'Value ($1000s)')


def rp(pts, desc):
    return cand([], desc, pts=[(a, b, '') for a, b in pts], has=[0])


SETS = [
    # ------------------------------------------------------------------ 15. ID.B.6.a choose and fit a function family
    S('HSS-ID.B.6.a', 'Choose and fit a linear, quadratic or exponential function', num=15,
      target='Fit a function to data: choose the family (linear, quadratic or exponential) suggested by the data and the '
             'context, and find its parameters',
      strand='core', covers=['ID6a-choose'],
      main=[
          sa('The data fit an exponential function y = a·b^x exactly. Find a and b.', ['a:', 'b:'], key='3; 2',
             fig=xy([(0, 3), (1, 6), (2, 12), (3, 24), (4, 48)]), note='Form required: both. y(0) = 3; each value doubles.'),
          sa('The data fit a linear function y = mx + b exactly. Find m and b.', ['m:', 'b:'], key='3; 5',
             fig=xy([(0, 5), (1, 8), (2, 11), (3, 14), (4, 17)]), note='Form required: both. Constant difference 3; y(0) = 5.'),
          mc('The scatter plot shows a car\'s speed and fuel efficiency. Which family of functions best fits the data?', [
              'quadratic', 'linear', 'exponential', 'constant'], fig=FIG_C,
             note='The values rise to a peak and fall: a parabola opening downward.'),
          mc('A town has 12,000 people and its population grows by about 8% each year. Which model fits, with t in years?', [
              'P = 12000(1.08)^t', 'P = 12000 + 0.08t', 'P = 12000(0.08)^t', 'P = 12000 + 1.08t'],
             note='Constant percent growth: factor 1.08.'),
          sa('An exponential function y = a·b^x passes through (0, 500) and (1, 400). Find a and b.', ['a:', 'b:'], key='500; 0.8',
             note='Form required: both. a = 500; b = 400/500.'),
      ],
      back=[
          B('Tell equal differences from equal factors', 'HSF-LE.A.1.a', [
              tf('In y = 3x + 5, y changes by equal differences over equal intervals of x.', key=True, note='Linear.'),
              mc('For x = 0, 1, 2, 3 the values of y are 2, 6, 18, 54. What is the pattern?', [
                  'multiplied by 3 each step', 'add 4 each step', 'add 3 each step', 'squared each step'], note='6/2 = 18/6 = 3.'),
              tf('The values 4, 7, 12, 19 (for x = 0 to 3) have constant first differences.', key=False,
                 note='Differences 3, 5, 7.'),
              sa('For x = 0 to 4, y = 4, 7, 12, 19, 28. What is the constant second difference?', 'Second difference:',
                 key='2', note='First differences 3, 5, 7, 9.'),
              mc('Which list of y-values (for x = 0, 1, 2, 3) is linear?', [
                  '10, 7, 4, 1', '1, 2, 4, 8', '0, 1, 4, 9', '5, 5.5, 6.5, 8'], note='Constant difference -3.'),
          ], align='supporting',
            why=why('the student cannot tell linear, quadratic and exponential patterns apart in a table.', 'choosing the '
                    'family starts there.', 'uses differences and ratios to identify the family.')),
          B('Write a linear function from two points', '8.F.B.4', [
              sa('A line passes through (0, 5) and (2, 11). Find its slope and y-intercept.', ['Slope:', 'y-intercept:'],
                 key='3; 5', note='Form required: both. 6/2.'),
              sa('Find the slope of the line through (1, 4) and (5, 12).', 'Slope:', key='2', note='8/4.'),
              tf('The table x = 0, 1, 2 and y = 7, 4, 1 fits y = -3x + 7.', key=True, note='Check each point.'),
              mc('Which function fits x = 0, 1, 2 and y = 2, 4.5, 7?', ['y = 2.5x + 2', 'y = 2x + 2.5', 'y = 2.5x', 'y = 4.5x'],
                 note='Difference 2.5, start 2.'),
              tf('The line through (0, 4) and (1, 10) has slope 4.', key=False, note='Slope 6.'),
          ], align='supporting',
            why=why('the student cannot find a line\'s parameters from points.', 'fitting a linear model needs them.',
                    'writes a linear function from points.')),
          B('Write an exponential function from two points', 'HSF-LE.A.2', [
              sa('An exponential function y = a·b^x passes through (0, 200) and (1, 300). Find a and b.', ['a:', 'b:'],
                 key='200; 1.5', note='Form required: both. 300/200.'),
              sa('An exponential function y = a·b^x with b > 0 passes through (0, 80) and (2, 20). Find a and b.', ['a:', 'b:'],
                 key='80; 0.5', note='Form required: both. b^2 = 1/4.'),
              tf('y = 50(1.2)^x passes through (1, 60).', key=True, note='50 · 1.2.'),
              mc('Which exponential function passes through (0, 4) and (1, 12)?', [
                  'y = 4(3)^x', 'y = 3(4)^x', 'y = 4 + 8x', 'y = 12(4)^x'], note='a = 4, b = 3. 4 + 8x is linear.'),
              tf('y = 10(0.5)^x passes through (2, 5).', key=False, note='10 · 0.25 = 2.5.'),
          ], align='supporting',
            why=why('the student cannot find the starting value and factor of an exponential function.', 'fitting an '
                    'exponential model needs them.', 'writes an exponential function from points.')),
      ],
      f1=B('Fit a model with regression technology', 'HSS-ID.B.6.a', [
          sa('Find the least-squares line y = mx + b for the spring data. Round m and b to two decimal places.%s' % TECH,
             ['m:', 'b:'], key='2.52; 9.86', fig=xy(D1, 'Mass (g)', 'Length (cm)'), note='Form required: both. Linear regression.'),
          sa('The points (0, 2), (1, 5), (2, 10), (3, 17) lie exactly on a quadratic y = ax^2 + bx + c. Find a, b and c.%s' % TECH,
             ['a:', 'b:', 'c:'], key='1; 2; 2', note='Form required: all three. Second difference 2, so a = 1; c = 2; b = 2.'),
          mc('Data on y rise faster and faster as x increases, y is always positive, and each step multiplies y by about 1.3. '
             'Which regression should be used?', ['exponential', 'linear', 'quadratic', 'none of these'],
             note='Nearly constant factor.'),
          sa('Using the fitted line y = 2.52x + 9.86, predict y when x = 6.', 'y:', key='24.98', note='15.12 + 9.86.'),
          tf('Height-versus-time data for a thrown ball are better fitted by a quadratic than by a line.', key=True,
             note='Projectile heights follow a parabola.'),
      ], prog='same-course deepening', demand='Fit the chosen family with regression technology and use it.'),
      f2=B('Check a fitted model with residuals', 'HSS-ID.B.6.b', [
          sa('For the model y = 2.52x + 9.86, find the residual (observed minus predicted) for the data point (5, 24).',
             'Residual:', key='1.54', note='24 - 22.46.'),
          sa('For the model y = 2.52x + 9.86, find the residual (observed minus predicted) for the data point (4, 19).', 'Residual:', key='-0.94',
             note='19 - 19.94.'),
          tf('A positive residual means the data point lies above the fitted line.', key=True, note='Observed > predicted.'),
          mc('A line is fitted to data that actually grow exponentially. What pattern do the residuals usually show?', [
              'a curved (U-shaped) pattern', 'random scatter around 0', 'all residuals equal to 0', 'every residual positive'],
             note='The line misses the curvature systematically.'),
          tf('If the residuals of a linear model are small but form a clear curve, a linear model is still the best family.',
             key=False, note='A pattern means the family is wrong.'),
      ], prog='cross-standard extension', demand='Judge the fitted model by computing and reading residuals.',
        builds='Builds on FORWARD 1: the regression model just fitted is checked point by point.')),

    # ------------------------------------------------------------------ 16. ID.B.6.b residuals
    S('HSS-ID.B.6.b', 'Assess the fit of a function with residuals', num=16,
      target='Informally assess the fit of a function by computing residuals (observed minus predicted), plotting them and '
             'analyzing the pattern',
      strand='core', covers=['ID6b-resid'],
      main=[
          sa('The model y = 2x + 1 is used for the data in the table. Find the residuals (observed minus predicted) at x = 1 and '
             'at x = 2.', ['Residual at x = 1:', 'Residual at x = 2:'], key='0.5; -0.4', fig=xy(RES),
             note='Form required: both. 3.5 - 3 and 4.6 - 5.'),
          sa('A model predicts y = 3x + 10. Find the residuals (observed minus predicted) for the observed points (4, 20) and (6, 30).',
             ['Residual for (4, 20):', 'Residual for (6, 30):'], key='-2; 2', note='Form required: both. 20 - 22 and 30 - 28.'),
          pick('The model y = 2x + 1 is used for the data in the table (x = 1 to 5; y = 3.5, 4.6, 7.2, 8.8, 11.1). Which plot is '
               'the residual plot (observed minus predicted)?', 'A', [
                   rp(RV, 'points at heights 0.5, -0.4, 0.2, -0.2, 0.1'),
                   rp([(x, -v) for x, v in RV], 'points at heights -0.5, 0.4, -0.2, 0.2, -0.1'),
                   rp([(x, v) for x, (_, v) in zip(range(1, 6), reversed(RV))], 'points at heights 0.1, -0.2, 0.2, -0.4, 0.5'),
                   rp([(1, 0.5), (2, -0.4), (3, -0.2), (4, -0.2), (5, 0.1)], 'points at heights 0.5, -0.4, -0.2, -0.2, 0.1')],
               'Residuals 0.5, -0.4, 0.2, -0.2, 0.1. The others use predicted minus observed, reverse the order, or flip the '
               'sign at x = 3.', x=(0, 6), y=(-1, 1), ystep=0.5),
          mc('A line was fitted to a data set. The residual plot is shown. Which conclusion is correct?', [
              'A linear model is not appropriate; the curve suggests a curved model.',
              'The linear model is appropriate, because some residuals are near 0.',
              'The linear model is appropriate, because residuals are both signs.',
              'The data must contain an error, because residuals are not all 0.'],
             fig=FIG_CURVED, note='A systematic curve in the residuals shows the line misses the form.'),
          mc('A line was fitted to a different data set, and its residual plot is shown. What does the plot show about the linear '
             'model?', [
              'The linear model is appropriate: the residuals show no pattern.',
              'The linear model is not appropriate, because residuals are not 0.',
              'A quadratic model is needed, because residuals change sign.',
              'The model is perfect, because the residuals add to about 0.'],
             fig=FIG_RANDOM, note='Random scatter around 0 supports the linear form; residuals are never all 0.'),
      ],
      back=[
          B('Subtract with signed decimals', '7.NS.A.1.c', [
              sa('Compute 3.5 - 3.', 'Answer:', key='0.5', note='Difference.'),
              sa('Compute 4.6 - 5.', 'Answer:', key='-0.4', note='Below zero.'),
              tf('20 - 22 = -2.', key=True, note='Signed result.'),
              mc('Compute 7.2 - 7.5.', ['-0.3', '0.3', '14.7', '-14.7'], note='Smaller minus larger is negative.'),
              tf('11 - 11.4 = 0.4.', key=False, note='-0.4.'),
          ], align='supporting',
            why=why('the student drops the sign when subtracting.', 'the sign of a residual tells above or below.',
                    'subtracts decimals with correct signs.')),
          B('Find a predicted value from a model', 'HSF-IF.A.2', [
              sa('For y = 2x + 1, find the predicted y at x = 3.', 'y:', key='7', note='6 + 1.'),
              sa('For y = 3x + 10, find the predicted y at x = 4.', 'y:', key='22', note='12 + 10.'),
              tf('For y = -1.5x + 20, the predicted y at x = 4 is 14.', key=True, note='-6 + 20.'),
              mc('For y = 0.5x + 3, what is the predicted y at x = 8?', ['7', '4', '11', '8.5'], note='4 + 3.'),
              tf('For y = 4x - 2, the predicted y at x = 0 is 2.', key=False, note='-2.'),
          ], align='supporting',
            why=why('the student cannot compute the predicted value.', 'a residual needs it.', 'evaluates the model at a data '
                    'point\'s x.')),
          B('Compare an observed value with a prediction', 'HSS-ID.B.6.a', [
              sa('A model predicts y = 2.5x + 12 free throws for x hours of practice. A student practiced 8 hours and made 35. What '
                 'is the predicted number, and how many more did the student make than predicted?', ['Predicted:', 'More by:'],
                 key='32; 3', note='Form required: both.'),
              tf('If an observed value is less than the predicted value, the point lies below the fitted line.', key=True,
                 note='Observed < predicted.'),
              mc('The observed value is 50 and the predicted value is 46. What is observed minus predicted?', ['4', '-4', '96', '46'],
                 note='50 - 46.'),
              tf('In this collection, a residual is defined as predicted minus observed.', key=False,
                 note='Residual = observed - predicted.'),
              sa('The observed value is 18 and the predicted value is 20.5. What is observed minus predicted?', 'Answer:',
                 key='-2.5', note='18 - 20.5.'),
          ], align='exact',
            why=why('the student mixes up observed and predicted values.', 'the residual compares them in a fixed order.',
                    'compares observed and predicted values.')),
      ],
      f1=B('Compute least-squares residuals', 'HSS-ID.B.6.b', [
          sa('The least-squares line for (1, 2), (2, 5), (3, 4), (4, 7) is y = 1.4x + 1. Find the residuals (observed minus predicted) at '
             'x = 1 and x = 2.',
             ['At x = 1:', 'At x = 2:'], key='-0.4; 1.2', note='Form required: both. 2 - 2.4 and 5 - 3.8.'),
          sa('For y = 1.4x + 1 and the points (1, 2), (2, 5), (3, 4), (4, 7), what is the sum of all four residuals?', 'Sum:',
             key='0', note='-0.4 + 1.2 - 1.2 + 0.4.'),
          tf('For a least-squares line, the residuals always add to 0.', key=True, note='A property of least squares.'),
          mc('For y = 1.4x + 1 and the points (1, 2), (2, 5), (3, 4), (4, 7), which points have the largest residuals in absolute '
             'value?', ['(2, 5) and (3, 4)', '(1, 2) and (4, 7)', '(1, 2) only', '(4, 7) only'], note='|1.2| > |0.4|.'),
          tf('A residual of -1.2 means the point lies 1.2 units above the line.', key=False, note='Below the line.'),
      ], prog='same-course deepening', demand='Compute every residual of a least-squares line and use their properties.'),
      f2=B('Compare two models with residuals', 'HSS-ID.B.6.b', [
          mc('Two models were fitted to the same data. Linear residuals: 3, -1, -3, -2, 1, 4. Exponential residuals: 0.2, -0.3, '
             '0.1, 0.3, -0.2, -0.1. Which model fits better?', ['the exponential model', 'the linear model', 'they fit equally',
                                                               'neither model can be judged'],
             note='The exponential residuals are small and patternless; the linear ones form a U.'),
          sa('Find the sum of squared residuals for each model: linear 3, -1, -3, -2, 1, 4 and exponential 0.2, -0.3, 0.1, 0.3, '
             '-0.2, -0.1.', ['Linear:', 'Exponential:'], key='40; 0.28', note='Form required: both. 9+1+9+4+1+16; 0.04+0.09+0.01+'
                                                                                '0.09+0.04+0.01.'),
          tf('Of two models fitted to the same data, the one with the smaller sum of squared residuals fits those data more '
             'closely.', key=True, note='Smaller total squared error.'),
          mc('A residual plot fans out: the residuals get larger as x increases. What does this show?', [
              'prediction errors grow as x increases', 'the model is exact', 'the data have no outliers', 'the slope is negative'],
             note='Spread of errors depends on x.'),
          tf('A residual plot with a clear U shape shows that the model is a good fit.', key=False, note='A pattern shows a '
                                                                                                 'poor fit.'),
      ], prog='same-course deepening', demand='Use residual patterns and sums of squares to compare models.',
        builds='Builds on FORWARD 1: residuals of one model become a tool for choosing between models.')),

    # ------------------------------------------------------------------ 17. ID.B.6.c fit a least-squares line
    S('HSS-ID.B.6.c', 'Fit a linear function to a linear scatter plot', num=17,
      target='Fit a linear function to a scatter plot that suggests a linear association, using least-squares regression '
             'with technology, and use it',
      strand='core', covers=['ID6c-line'],
      main=[
          sa('Find the least-squares line y = mx + b for hours studied (x) and score (y). Round m and b to two decimal places.%s'
             % TECH, ['m:', 'b:'], key='5.17; 48.28', fig=SAT, note='Form required: both. m = 2485/481 ≈ 5.166; b = 23225/481 ≈ 48.285.'),
          sa('Find the least-squares line y = mx + b for car age (x) and value in $1000s (y). Round m and b to two decimal '
             'places.%s' % TECH, ['m:', 'b:'], key='-1.88; 25.87', fig=SBT, note='Form required: both. m = -311/165 ≈ -1.885; b = 388/15 ≈ 25.867.'),
          pick('Which graph shows the line that best fits the study data (hours, score)?', 'D', [
              cand([lambda x: 48.28 + 5.17 * x], 'a line through the middle of the points', pts=[(a, b, '') for a, b in SA]),
              cand([lambda x: 40 + 5.17 * x], 'a line below almost every point', pts=[(a, b, '') for a, b in SA]),
              cand([lambda x: 40 + 8 * x], 'a line steeper than the points', pts=[(a, b, '') for a, b in SA]),
              cand([lambda x: 90 - 5 * x], 'a falling line', pts=[(a, b, '') for a, b in SA])],
               'The least-squares line y = 5.17x + 48.28 runs through the middle. The others are too low, too steep, or falling.',
               x=(0, 9), y=(40, 100), ystep=10),
          sa('Using the least-squares line y = 5.17x + 48.28 for hours studied and score, predict the score for 3 hours.',
             'Score:', key='63.79', note='15.51 + 48.28.'),
          mc('A student wants to fit a least-squares line to the data in this scatter plot. Which statement is correct?', [
              'A line is not appropriate: the pattern is curved.', 'A line is appropriate, because r can always be computed.',
              'A line is appropriate, because the data have no outliers.', 'A line fits well, because the points rise at first.'],
             fig=FIG_C, note='The standard applies to scatter plots that suggest a linear association.'),
      ],
      back=[
          B('Fit a line by eye', '8.SP.A.2', [
              tf('A least-squares line must have exactly as many data points above it as below it.', key=False,
                 note='Least squares (with an intercept) makes the residuals add to 0; the numbers of points above and below can differ.'),
              mc('Which line passes through (0, 2), (2, 6) and (4, 10)?', ['y = 2x + 2', 'y = x + 2', 'y = 2x', 'y = 4x + 2'],
                 note='Check each point.'),
              sa('A line drawn by eye passes through (0, 50) and (5, 75). Find its slope and y-intercept.', ['Slope:',
                                                                                                      'y-intercept:'],
                 key='5; 50', note='Form required: both. 25/5.'),
              tf('A fitted line must pass through every data point.', key=False, note='It summarizes the trend.'),
              sa('Use the line y = 5x + 50 to predict y at x = 4.', 'y:', key='70', note='20 + 50.'),
          ], align='exact',
            why=why('the student does not know what a fitted line should do.', 'least squares makes that idea precise.',
                    'fits and uses a line drawn by eye.')),
          B('Find slope and intercept from points', '8.F.B.4', [
              sa('Find the slope of the line through (2, 58) and (6, 80).', 'Slope:', key='5.5', note='22/4.'),
              sa('A line has slope 5 and passes through (2, 60). Find its y-intercept.', 'y-intercept:', key='50', note='60 - 10.'),
              tf('The line through (0, 26) with slope -2 has y = 16 at x = 5.', key=True, note='26 - 10.'),
              mc('Which equation is the line through (0, 10) and (4, 2)?', ['y = -2x + 10', 'y = 2x + 10', 'y = -0.5x + 10',
                                                                            'y = -2x + 2'], note='Slope -8/4.'),
              tf('The slope of the line through (1, 24) and (10, 6) is 2.', key=False, note='-18/9 = -2.'),
          ], align='supporting',
            why=why('the student cannot read slope and intercept.', 'they are the line\'s parameters.', 'finds slope and '
                    'intercept from points.')),
      ],
      f1=B('Use the properties of the least-squares line', 'HSS-ID.B.6.c', [
          sa('Find the mean hours x̄ and the mean score ȳ for the study data.', ['x̄:', 'ȳ:'], key='4.3; 70.5', fig=SAT,
             note='Form required: both. 43/10 and 705/10.'),
          tf('The least-squares line passes through the point (x̄, ȳ).', key=True, note='A property of least squares.'),
          mc('The least-squares line is the line that makes which quantity as small as possible?', [
              'the sum of the squared residuals', 'the sum of the residuals', 'the number of points off the line',
              'the largest single residual'], note='Definition. The plain sum is 0 for many lines.'),
          sa('A least-squares line has slope 2 and passes through (x̄, ȳ) = (5, 20). Find its y-intercept.', 'y-intercept:',
             key='10', note='20 - 10.'),
          tf('Adding one point far from the others can never change the least-squares line.', key=False,
             note='An influential point can move it a lot.'),
      ], prog='same-course deepening', demand='Use what least squares guarantees to check and reason about the line.'),
      f2=B('Interpret the fitted line\'s slope and intercept', 'HSS-ID.C.7', [
          mc('For hours studied (x) and score (y), the least-squares line is y = 5.17x + 48.28. What does 5.17 mean?', [
              'Each extra hour goes with about 5.17 more points, on average.', 'Each student scored 5.17 points per test.',
              'A student who studied 0 hours scored exactly 5.17.', 'The score rises 48.28 points for each hour.'],
             note='Slope: predicted change in y per unit of x.'),
          sa('Using y = 5.17x + 48.28, how much higher is the predicted score for a student who studies 2 more hours?',
             'Points:', key='10.34', note='2 · 5.17.'),
          mc('For car age (x, years) and value (y, $1000s), y = -1.88x + 25.87. What does 25.87 mean?', [
              'A new car (age 0) has a predicted value of about $25,870.', 'Cars lose about $25,870 each year.',
              'The oldest car is worth about $25,870.', 'A car is predicted to be worth $0 after 25.87 years.'],
             note='Intercept: predicted y at x = 0 (age 0 is near the data).'),
          tf('In y = -1.88x + 25.87, the slope means every car loses exactly $1,880 each year.', key=False,
             note='It is an average rate for the model, not exact for each car.'),
          sa('Using y = -1.88x + 25.87, how much greater (in $1000s) is the predicted value of a 3-year-old car than a '
             '7-year-old car?', 'Difference:', key='7.52', note='4 · 1.88.'),
      ], prog='cross-standard extension', demand='Interpret the parameters of the line just fitted.',
        builds='Builds on FORWARD 1: the line\'s slope and intercept, now trusted, are read in context.')),

    # ------------------------------------------------------------------ 18. ID.C.7 interpret slope and intercept
    S('HSS-ID.C.7', 'Interpret the slope and intercept of a linear model', num=18,
      target='Interpret the slope (rate of change) and the intercept (constant term) of a linear model in the context of the '
             'data, with units, and recognize when the intercept is not meaningful',
      strand='core', covers=['ID7-interpret'],
      main=[
          mc('A model for a family\'s savings is y = 85x + 1200, where x is months and y is dollars. What does 85 mean?', [
              'The savings are predicted to grow by $85 each month.', 'The family started with $85 in savings.',
              'The savings will reach $85 after 1200 months.', 'The family saves $1200 each month.'],
             note='Slope: dollars per month.'),
          mc('A model for weekly hours of exercise is y = 6 - 0.2x, where x is weekly hours of TV. What does 6 mean?', [
              'A person who watches 0 hours of TV is predicted to exercise 6 hours.',
              'Each hour of TV is predicted to add 6 hours of exercise.',
              'Each hour of TV is predicted to cut exercise by 6 hours.',
              'A person exercises at most 0.2 hours per week.'],
             note='Intercept: predicted y at x = 0.'),
          sa('A tree\'s height is modeled by y = 0.4x + 1.5, with y in meters and x in years since planting. What is the predicted '
             'growth per year, and what is the predicted height at planting?', ['Growth per year (m):', 'Height at planting (m):'],
             key='0.4; 1.5', note='Form required: both.'),
          mc('For adults with heights from 150 to 190 cm, arm span is modeled by y = 1.1x - 15 (both in cm). Which statement '
             'about the intercept -15 is correct?', [
              'It is not meaningful: a height of 0 cm is far outside the data.',
              'It means a person 0 cm tall has an arm span of -15 cm.',
              'It means arm spans are 15 cm less than heights.',
              'It means the slope of the model is negative.'],
             note='Extrapolating to x = 0 makes no sense here.'),
          sa('Weekly gasoline use is modeled by y = 0.35x + 4.2 gallons, where x is miles driven per day. By how many gallons '
             'do the predictions differ for two drivers whose daily miles differ by 20?', 'Gallons:', key='7', note='20 · 0.35.'),
      ],
      back=[
          B('Interpret the rate and the initial value of a linear function', '8.F.B.4', [
              mc('A plumber charges y = 50x + 80 dollars for x hours. What does 80 mean?', [
                  'a fixed fee charged before any hours', 'the charge per hour', 'the total for 1 hour', 'the number of hours'],
                 note='Initial value.'),
              sa('A phone plan costs y = 0.1x + 25 dollars for x minutes. What is the cost per minute, and what is the fixed cost?',
                 ['Per minute ($):', 'Fixed ($):'], key='0.1; 25', note='Form required: both.'),
              tf('In y = 3x + 12, when x increases by 1, y increases by 12.', key=False, note='By 3.'),
              mc('A candle\'s height is h = 20 - 1.5t centimeters after t hours. What does 1.5 mean?', [
                  'the candle burns 1.5 cm per hour', 'the candle starts 1.5 cm tall', 'the candle burns 20 cm per hour',
                  'the candle lasts 1.5 hours'], note='Rate of change.'),
              tf('In y = 3x + 12, the value of y when x = 0 is 12.', key=True, note='Initial value.'),
          ], align='exact',
            why=why('the student cannot say what a rate and an initial value mean in a situation.', 'slope and intercept of a '
                    'model are those.', 'interprets both parameters with units.')),
          B('Use a linear model\'s equation to answer questions', '8.SP.A.3', [
              sa('Plant height is modeled by y = 1.5x + 5 (cm after x weeks). Predict the height at 6 weeks.', 'Height (cm):',
                 key='14', note='9 + 5.'),
              mc('In the plant model y = 1.5x + 5, one more week of growth goes with', [
                  '1.5 cm more height', '5 cm more height', '6.5 cm more height', '1.5 more weeks'], note='Slope.'),
              tf('In the plant model y = 1.5x + 5, the slope means the plants were 1.5 cm tall at the start.', key=False,
                 note='That is the intercept, 5 cm.'),
              sa('In the plant model y = 1.5x + 5, how much greater is the predicted height at week 10 than at week 2?',
                 'Difference (cm):', key='12', note='8 · 1.5.'),
              tf('A negative slope means the predicted y decreases as x increases.', key=True, note='Direction.'),
          ], align='exact',
            why=why('the student cannot use a model\'s equation for predictions and differences.', 'interpretation is checked '
                    'that way.', 'answers questions with a linear model.')),
      ],
      f1=B('Interpret parameters with units and judge meaning', 'HSS-ID.C.7', [
          sa('Using y = 5.17x + 48.28 (score versus hours studied), what is the predicted score increase for 3 more hours?',
             'Points:', key='15.51', note='3 · 5.17.'),
          mc('A shipping cost is modeled by y = 0.02x + 3.5 dollars for x grams. What does 0.02 mean?', [
              'Each additional gram adds about $0.02 to the predicted cost.', 'Each package costs $0.02 no matter what it weighs.',
              'The predicted cost rises by $3.50 for each gram.',
              'A package weighing 0 grams is predicted to cost $0.02.'], note='Dollars per gram.'),
          tf('The intercept of a linear model always has a meaningful interpretation in context.', key=False,
             note='Not when x = 0 is outside the data.'),
          mc('For ages 20 to 60, maximum heart rate is modeled by y = 208 - 0.7x beats per minute, x in years. Which statement '
             'about 208 is correct?', [
              'It is the prediction at age 0, outside the data: not meaningful.',
              'It is the predicted heart rate for a 20-year-old person.',
              'It is the decrease in maximum heart rate for each year of age.',
              'It is the largest heart rate that any person can have.'],
             note='Age 0 is outside 20 to 60.'),
          sa('Using y = 208 - 0.7x, predict the maximum heart rate at age 40.', 'Beats per minute:', key='180', note='208 - 28.'),
      ], prog='same-course deepening', demand='Interpret parameters for non-unit changes and decide when the intercept is '
                                             'meaningful.'),
      f2=B('Relate the slope to the correlation coefficient', 'HSS-ID.C.8', [
          tf('The sign of the correlation coefficient matches the sign of the slope of the least-squares line.', key=True,
             note='Both measure direction.'),
          mc('The least-squares line is y = -1.88x + 25.87. Which could be the correlation coefficient?', [
              '-0.97', '0.97', '1.88', '-1.88'], note='Negative, and |r| ≤ 1.'),
          tf('A larger slope always means a stronger correlation.', key=False, note='Slope depends on units; r does not.'),
          sa('The least-squares slope equals r·(s_y/s_x). If r = 0.8, s_y = 10 and s_x = 4, what is the slope?', 'Slope:',
             key='2', note='0.8 · 2.5.'),
          mc('The x-values vary and the y-values vary (neither is constant). If the least-squares line has slope 0, what is r?', ['0', '1', '-1', 'it cannot be found'], note='b = r·s_y/s_x.'),
      ], prog='cross-standard extension', demand='Connect the slope of the fitted line with the correlation coefficient.',
        builds='Builds on FORWARD 1: the slope, read as a rate with units, is compared with the unit-free r.')),
]
