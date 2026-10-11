from qb import S, B, sa, mc, tf, plot, draw_write, table, dot, coord
from common import grid, ints


def tbl(xname, xs, yname, ys):
    return table([[xname] + [str(v) for v in xs], [yname] + [str(v) for v in ys]], header='col')


def two_way(rows):
    return table(rows, header='both')


def blank_tw(r1, r2, c1, c2):
    e = ' ' * 10
    return two_way([['', c1, c2, 'Total'], [r1, e, e, e], [r2, e, e, e], ['Total', e, e, e]])


# scatter plots for describing patterns (8.SP.A.1)
PRACTICE = grid(10, 10, xlabel='Hours of practice', ylabel='Free throws made',
                pts=[(1, 1), (2, 2), (2, 3), (3, 3), (4, 4), (5, 5), (6, 5), (7, 7), (8, 8), (9, 2)])
TV = grid(10, 10, xlabel='Hours of TV', ylabel='Hours of reading', pts=[(1, 9), (2, 8), (3, 8), (4, 6), (5, 5), (6, 5), (7, 3), (8, 2)])
CURVE = grid(10, 10, pts=[(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 4), (7, 6), (8, 9)])
CLUSTERS = grid(10, 10, pts=[(1, 1), (1, 2), (2, 1), (2, 2), (7, 7), (7, 8), (8, 7), (8, 8)])
NOASSOC = grid(10, 10, pts=[(1, 5), (2, 2), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 3)])

# scatter plots for fitting a line (8.SP.A.2)
UP = [(1, 2), (2, 2), (3, 4), (4, 4), (5, 5), (6, 7), (7, 7), (8, 9)]
DOWN = [(1, 9), (2, 8), (3, 8), (4, 6), (5, 6), (6, 4), (7, 3), (8, 3)]

# two-way tables (8.SP.A.4)
CURFEW = two_way([['', 'Chores', 'No chores', 'Total'], ['Curfew', '24', '12', '36'], ['No curfew', '8', '16', '24'], ['Total', '32', '28', '60']])
CLUB = two_way([['', 'In club', 'Not in club', 'Total'], ['Grade 7', '12', '28', '40'], ['Grade 8', '18', '42', '60'], ['Total', '30', '70', '100']])
PHONE = two_way([['', 'Phone at night', 'No phone at night', 'Total'], ['Sleeps 8+ hours', '12', '28', '40'],
                 ['Sleeps under 8 hours', '36', '24', '60'], ['Total', '48', '52', '100']])
BREAKFAST = two_way([['', 'Breakfast', 'No breakfast', 'Total'], ['Grade 7', '30', '20', '50'], ['Grade 8', '45', '30', '75'], ['Total', '75', '50', '125']])
PETS = dict(k='hist', bins=['Dogs', 'Cats', 'Fish'], counts=[8, 6, 4], gap=0.35, ystep=2, ymax=10, ylabel='Students', h=230,
            desc='Bar graph of favorite pets: Dogs 8, Cats 6, Fish 4. The scale counts by 2s.')

SETS = [
    # ------------------------------------------------------------------ 8.SP.A.1 (construct)
    S('8.SP.A.1', 'Construct a scatter plot for bivariate measurement data',
      main=[
          plot('Seven students recorded (hours studied, test score):\n(1, 50), (2, 60), (3, 60), (4, 70), (5, 80), (6, 80), (7, 90)\nMake a scatter plot of the data on the grid.',
               grid(8, 100, ystep=10, xlabel='Hours studied', ylabel='Test score'),
               key='Points at (1, 50), (2, 60), (3, 60), (4, 70), (5, 80), (6, 80), and (7, 90)'),
          plot('A bean plant was measured on different days (days after planting, height in cm):\n(2, 1), (4, 3), (5, 4), (6, 4), (8, 6), (9, 7), (10, 8)\nMake a scatter plot of the data on the grid.',
               grid(10, 10, xlabel='Days after planting', ylabel='Height (cm)'),
               key='Points at (2, 1), (4, 3), (5, 4), (6, 4), (8, 6), (9, 7), and (10, 8)'),
          sa('The scatter plot should show the data (1, 6), (2, 5), (3, 5), (5, 3), and (7, 2), but one point is plotted wrong.\nWhich point is wrong, and where should it be?', 'Answer:',
             fig=grid(8, 8, pts=[(1, 6), (2, 5), (3, 5), (5, 3), (2, 7)]),
             key='The pair (7, 2) is plotted at (2, 7). It should be 7 units right and 2 units up, at (7, 2).'),
          mc('Ten students recorded their shoe sizes and heights to make a scatter plot.\nWhat does each point on the scatter plot show?',
             ['One student\'s shoe size and height', 'The mean shoe size of the class', 'How many students have each shoe size', 'One student\'s shoe size only']),
          tf('A scatter plot of hours slept and test scores puts two points on the grid for each student, one for each variable.', key=False, note='Each student is one point: (hours slept, test score).'),
      ],
      back=[
          B('Graph points that represent a real-world situation', '5.G.A.2', [
              plot('A plant was 2 cm tall on day 1, 4 cm tall on day 2, and 5 cm tall on day 3.\nPlot the points (day, height) on the grid.',
                   grid(5, 6, xlabel='Day', ylabel='Height (cm)'), key='Points at (1, 2), (2, 4), and (3, 5)'),
              sa('A graph shows points (day, height in cm).\nWhat does the point (4, 3) mean?', 'Meaning:', key='On day 4, the height was 3 cm.'),
              mc('Points on a graph are (hours, miles).\nWhich point shows 5 hours and 2 miles?', ['(5, 2)', '(2, 5)', '(5, 5)', '(2, 2)']),
              tf('To plot (3, 6), start at the origin, move 3 units right, then 6 units up.', key=True),
              tf('The point (0, 4) is on the x-axis.', key=False, note='(0, 4) is on the y-axis.'),
          ]),
          B('Display a numerical data set in a dot plot', '6.SP.B.4', [
              plot('The numbers of pets of 10 students are 0, 1, 1, 2, 2, 2, 3, 3, 4, and 1.\nMake a dot plot of the data on the number line.', ints(0, 5),
                   key='Dots: 1 above 0, 3 above 1, 3 above 2, 2 above 3, 1 above 4, and none above 5'),
              sa('How many students are shown in the dot plot?', 'Students:', fig=dot(0, 6, [1, 2, 2, 3, 3, 3, 4, 5], xlabel='Books read'), key='8'),
              mc('Which display shows each value of a data set as a dot above a number line?', ['A dot plot', 'A box plot', 'A histogram', 'A bar graph']),
              tf('In a dot plot, a value that appears 3 times has 3 dots stacked above it.', key=True),
              tf('A dot plot shows two different measurements for each student.', key=False, note='A dot plot shows one variable.'),
          ]),
      ],
      f1=B('Compare linear, quadratic, and exponential models for two-variable data, using technology', 'HSS-ID.B.6', [
          sa('Data: (0, 3), (1, 6), (2, 12), (3, 24).\nDoes a linear or an exponential model fit these data better? Explain using differences and ratios, and give the model.', 'Answer:',
             key='Exponential: the differences (3, 6, 12) are not equal, but each y-value is 2 times the one before, so y = 3 · 2^x.', note='Both the reason and the model are required.'),
          sa('Use a calculator or spreadsheet to find the least-squares line for the data (1, 2), (2, 3), (3, 5), (4, 6). Round the slope and the y-intercept to the nearest tenth.', 'Line:',
             key='y = 1.4x + 0.5'),
          mc('Which model fits the data (1, 1), (2, 4), (3, 9), (4, 16) exactly?', ['y = x²', 'y = 5x - 5', 'y = 2^x', 'y = 4x']),
          tf('A scatter plot that curves upward more and more steeply may be fit better by an exponential or quadratic function than by a line.', key=True),
          tf('A line with residuals 0, 3, -5, and 4 fits the same data better than a curve with residuals 0, 0.1, -0.2, and 0.1.', key=False, note='The curve\'s residuals are much smaller.'),
      ]),
      f2=B('Fit an exponential or quadratic function to data and use it to make predictions', 'HSS-ID.B.6.a', [
          sa('A bacteria count is 100 at hour 0, 200 at hour 1, 400 at hour 2, and 800 at hour 3.\nWrite a function that fits the data.', 'y =', key='100 · 2^x'),
          sa('A bacteria count fits y = 100 · 2^x after x hours.\nPredict the count at hour 6.', 'Count:', key='6,400'),
          mc('Which function fits the data exactly?', ['y = x²', 'y = 2^x', 'y = 4x', 'y = x + 4'], fig=tbl('x', [0, 1, 2, 3, 4], 'y', [0, 1, 4, 9, 16])),
          tf('The data (0, 5), (1, 10), (2, 20), and (3, 40) fit y = 5 · 2^x exactly.', key=True),
          tf('Data whose y-values go up by the same amount at each step are best fit by an exponential function.', key=False, note='Equal differences mean a linear function fits.'),
      ])),

    # ------------------------------------------------------------------ 8.SP.A.1 (describe patterns)
    S('8.SP.A.1', 'Describe clustering, outliers, and positive, negative, linear, or nonlinear association in a scatter plot',
      main=[
          sa('Describe the association in the scatter plot (positive, negative, or none; linear or nonlinear), and name any outlier.', 'Answer:', fig=PRACTICE,
             key='A positive linear association; the point (9, 2) is an outlier.', note='Both the association and the outlier are required.'),
          sa('Describe the association in the scatter plot.', 'Answer:', fig=TV,
             key='A negative linear association: as hours of TV increase, hours of reading decrease.'),
          mc('Which best describes the association in the scatter plot?', ['Positive and nonlinear', 'Positive and linear', 'Negative and nonlinear', 'No association'], fig=CURVE),
          sa('The points in the scatter plot form two groups.\nDescribe the two clusters.', 'Answer:', fig=CLUSTERS,
             key='One cluster has x and y from 1 to 2; the other has x and y from 7 to 8.', note='Any description that locates both clusters is correct.'),
          tf('The scatter plot shows a negative association.', key=False, fig=NOASSOC, note='The points show no association.'),
      ],
      back=[
          B('Describe a data distribution by its center, spread, and shape', '6.SP.A.2', [
              sa('Is the data in the dot plot symmetric or skewed?', 'Answer:', fig=dot(0, 8, [2, 3, 3, 4, 4, 4, 5, 5, 6]), key='Symmetric, centered at 4'),
              sa('What is the range of the data in the dot plot?', 'Range:', fig=dot(0, 10, [1, 2, 2, 3, 3, 3, 4, 9]), key='8'),
              mc('Which value is far from the rest of the data?\n3, 4, 4, 5, 5, 6, 18', ['18', '3', '5', '6']),
              tf('The data set 2, 3, 3, 4, 4, 4, 5, 5, 6 is symmetric about 4.', key=True),
              tf('The range of a data set measures its center.', key=False, note='The range measures spread.'),
          ]),
          B('Describe the overall pattern of data and any striking deviations', '6.SP.B.5.c', [
              sa('Find the median.\n4, 6, 7, 7, 8, 9, 30', 'Median:', key='7'),
              sa('Which value is a striking deviation from the pattern?\n4, 6, 7, 7, 8, 9, 30', 'Value:', key='30'),
              mc('The data are 10, 12, 12, 13, 14, and 40.\nWhich measure of center is changed more by the value 40?', ['The mean', 'The median', 'Both are changed equally', 'Neither is changed']),
              tf('Removing a value that is much larger than the others lowers the mean.', key=True),
              tf('An outlier always changes the median by a large amount.', key=False, note='The median depends on the middle value, so it changes little.'),
          ]),
      ],
      f1=B('Distinguish between correlation and causation', 'HSS-ID.C.9', [
          sa('Data show that cities with more ice-cream sales also have more sunburns.\nDo these data show that buying ice cream causes sunburns? Explain.', 'Answer:',
             key='No. The data show an association, not a cause. Something else, such as hot, sunny weather, could explain both.', note='Any reason that separates association from cause is accepted.'),
          sa('A study finds that students who sleep more tend to have higher grades.\nCan you conclude that more sleep causes higher grades? Explain.', 'Answer:',
             key='No. The data show an association, not a cause; a randomized experiment is needed to show cause.'),
          mc('Which kind of study can show that one variable causes a change in another?', ['A randomized experiment', 'An observational study', 'A scatter plot of survey data', 'A survey of volunteers']),
          tf('Two variables can be strongly associated without one causing the other.', key=True),
          tf('A strong correlation shows that one variable causes the other.', key=False),
      ]),
      f2=B('Interpret the correlation coefficient of a linear fit', 'HSS-ID.C.8', [
          sa('Use a calculator or spreadsheet to find the correlation coefficient r for the data (1, 2), (2, 4), (3, 5), (4, 4), (5, 6). Round to the nearest hundredth, and describe the association.', 'Answer:',
             key='r ≈ 0.85: a fairly strong positive linear association.', note='Both the value and the description are required.'),
          sa('Which shows the stronger linear association, r = 0.45 or r = -0.81? Explain.', 'Answer:', key='r = -0.81, because its absolute value is closer to 1.'),
          mc('Points lie almost exactly on a line that rises from left to right.\nWhich value of r fits?', ['0.98', '-0.98', '0.10', '0']),
          tf('The correlation coefficient r is always between -1 and 1.', key=True),
          tf('r = -0.9 shows a weaker linear association than r = 0.5.', key=False, note='|-0.9| is greater than |0.5|, so r = -0.9 is stronger.'),
      ])),

    # ------------------------------------------------------------------ 8.SP.A.2
    S('8.SP.A.2', 'Informally fit a straight line to a scatter plot and judge how closely it fits',
      main=[
          draw_write('Draw a straight line that fits the data. Then write an equation of your line.', grid(10, 10, pts=UP), 'Equation:',
                     draw='A straight line close to the points, with about as many points above it as below it, for example through (0, 0.5) and (8, 8.5)',
                     key='The equation of the line drawn, about y = x + 0.5', note='Slopes from about 0.8 to 1.2 and y-intercepts from about 0 to 1.5 are accepted when they match the line drawn.'),
          draw_write('Draw a straight line that fits the data. Use your line to estimate y when x = 9.', grid(10, 10, pts=DOWN), 'Estimate:',
                     draw='A straight line close to the points, with about as many points above it as below it, for example through (0, 10) and (8, 2)',
                     key='About 1 to 2, read from the line drawn (y = -x + 10 gives 1)', note='Accept an estimate that matches the student\'s own line.'),
          sa('Two students drew lines for the same scatter plot. Line A has every point above it. Line B has about half the points above it and half below, all close to it.\nWhich line fits better? Explain.', 'Answer:',
             key='Line B, because the points are close to it and balanced on both sides.'),
          mc('Why is the line on the scatter plot a poor fit?', ['It does not follow the upward trend of the points.', 'It passes through too many points.', 'It is not long enough.', 'It starts at the y-axis.'],
             fig=grid(10, 10, pts=UP, lines=[((0, 4), (10, 4))])),
          tf('A line that fits a scatter plot well must pass through every point.', key=False, note='A good line is close to the points; it may pass through none of them.'),
      ],
      back=[
          B('Decide from a table or graph whether a relationship is proportional', '7.RP.A.2.a', [
              sa('Is the relationship shown in the graph proportional? Explain.', 'Answer:', fig=grid(6, 12, lines=[((0, 0), (6, 12))]),
                 key='Yes. The graph is a straight line through the origin.'),
              sa('Is the relationship in the table proportional? Explain.', 'Answer:', fig=tbl('x', [1, 2, 4], 'y', [3, 6, 13]),
                 key='No. 3 ÷ 1 = 3 and 6 ÷ 2 = 3, but 13 ÷ 4 is not 3.'),
              mc('Which graph shows a proportional relationship?', ['A straight line through (0, 0) and (2, 5)', 'A straight line through (0, 2) and (2, 6)',
                                                                   'A curve through (0, 0) and (2, 4)', 'A horizontal line through (0, 3)']),
              tf('A straight line through (0, 0) and (3, 9) shows a proportional relationship.', key=True),
              tf('Every straight-line graph shows a proportional relationship.', key=False, note='The line must also pass through the origin.'),
          ]),
          B('Write an equation for a relationship shown in a table or graph', '6.EE.C.9', [
              sa('Write an equation for y in terms of x.', 'y =', fig=tbl('x', [1, 2, 3], 'y', [4, 8, 12]), key='4x'),
              sa('Write an equation for y in terms of x.', 'y =', fig=tbl('x', [0, 1, 2, 3], 'y', [2, 3, 4, 5]), key='x + 2'),
              mc('A line passes through (0, 0), (1, 5), and (2, 10).\nWhich equation does it show?', ['y = 5x', 'y = x + 5', 'y = 10x', 'x = 5y']),
              tf('The points (1, 3), (2, 6), and (3, 9) fit y = 3x.', key=True),
              tf('The points (0, 1), (1, 2), and (2, 3) fit y = 2x.', key=False, note='They fit y = x + 1.'),
          ]),
      ],
      f1=B('Fit a least-squares line with technology and compare candidate lines', 'HSS-ID.B.6.c', [
          sa('Use a calculator or spreadsheet to find the least-squares line for the data (1, 3), (2, 5), (3, 6), (4, 8), (5, 10), (6, 11). Round the slope and the y-intercept to the nearest tenth.', 'Line:',
             key='y = 1.6x + 1.5'),
          sa('Two lines are proposed for the data (1, 3), (2, 5), (3, 6), (4, 8): y = 2x + 1 and y = 1.6x + 1.5.\nFind the sum of the squared residuals for each line. Which line fits better?', 'Answer:',
             key='y = 2x + 1: 0 + 0 + 1 + 1 = 2. y = 1.6x + 1.5: 0.01 + 0.09 + 0.09 + 0.01 = 0.2. So y = 1.6x + 1.5 fits better.', note='Both sums and the conclusion are required.'),
          mc('A least-squares line for hours studied x and test score y is y = 4.2x + 61. A student who studied 0 hours scored 70.\nWhat is that student\'s residual?', ['9', '-9', '61', '70']),
          tf('The least-squares line makes the sum of the squared residuals as small as possible.', key=True),
          tf('A line of fit should always be drawn through the first and last data points.', key=False, note='It should follow the whole trend, not just two points.'),
      ]),
      f2=B('Judge the fit of a line by finding and plotting residuals', 'HSS-ID.B.6.b', [
          sa('A line of fit is y = 2x + 1. A data point is (3, 8).\nFind the residual (actual y minus predicted y).', 'Residual:', key='1'),
          draw_write('A line of fit is y = 2x + 1 for the data (1, 4), (2, 4), (3, 8), and (4, 9).\nFind each residual (actual y minus predicted y) and plot the residuals against x on the grid.',
                     coord(x=(0, 5), y=(-3, 3), xlabel='x', ylabel='Residual'), 'Residuals:',
                     draw='Points at (1, 1), (2, -1), (3, 1), and (4, 0)', key='1, -1, 1, and 0',
                     note='Grade both: the four residuals and the four plotted points.'),
          mc('A residual plot shows small residuals scattered above and below 0 with no pattern.\nWhat does this suggest?',
             ['A linear model is appropriate for the data.', 'A linear model is a poor choice.', 'A curve must be used.', 'Every prediction is exact.']),
          tf('A residual of 0 means the data point lies on the line of fit.', key=True),
          tf('A residual plot with a clear U shape shows that a linear model fits well.', key=False, note='A U shape suggests a curve fits better.'),
      ])),

    # ------------------------------------------------------------------ 8.SP.A.3
    S('8.SP.A.3', 'Use the equation of a linear model to interpret the slope and intercept and to make predictions',
      main=[
          sa('A line of fit for the height h (inches) of a plant after w weeks is h = 1.5w + 4.\nWhat do the slope and the intercept mean?', 'Answer:',
             key='Slope: the plant grows about 1.5 inches per week. Intercept: it was about 4 inches tall at week 0.', note='Both meanings are required.'),
          sa('A line of fit for the gas g (gallons) left in a car\'s tank after m miles is g = 14 - 0.04m.\nPredict the gas left after 200 miles.', 'Gas left:', key='6 gallons'),
          mc('A model for the water level w (feet) of a pond t days after the rain stops is w = 12 - 0.3t.\nWhat does -0.3 mean?',
             ['The level drops about 0.3 foot each day.', 'The level starts at 0.3 foot.', 'The level rises about 0.3 foot each day.', 'The pond is empty after 0.3 day.']),
          sa('A model for the score s after h hours of practice is s = 6h + 58.\nPredict the score after 5 hours of practice.', 'Score:', key='88'),
          tf('In the model y = 3.2x + 15 for the cost of a taxi ride of x miles, 15 is the cost per mile.', key=False, note='15 is the starting fee; 3.2 is the cost per mile.'),
      ],
      back=[
          B('Explain what a point on the graph of a proportional relationship means', '7.RP.A.2.d', [
              sa('The graph of cost (dollars) against pounds is proportional and passes through (1, 3).\nWhat does (1, 3) mean?', 'Meaning:', key='1 pound costs $3; this is the unit rate.'),
              sa('A proportional graph of miles against hours passes through (0, 0).\nWhat does (0, 0) mean?', 'Meaning:', key='In 0 hours, 0 miles are traveled.'),
              mc('A proportional graph of (gallons, cost) passes through (1, 4).\nWhat is the unit rate?', ['$4 per gallon', '$1 per gallon', '$0.25 per gallon', '$5 per gallon']),
              tf('On a proportional graph of (hours, pages), the point (1, 20) means 20 pages are read per hour.', key=True),
              tf('On a proportional graph of (tickets, cost), the point (2, 18) means that one ticket costs $18.', key=False, note='2 tickets cost $18, so one ticket costs 18 ÷ 2 = $9.'),
          ]),
          B('Evaluate a formula for given values of its variable', '6.EE.A.2.c', [
              sa('Evaluate 1.5w + 4 when w = 6.', 'Value:', key='13'),
              sa('Evaluate 300 - 40t when t = 3.', 'Value:', key='180'),
              mc('Evaluate 6h + 58 when h = 2.', ['70', '66', '128', '62']),
              tf('When x = 4, 3x + 5 = 35.', key=False, note='3 × 4 + 5 = 17.'),
              tf('When t = 2, 10 - 3t = 14.', key=False, note='10 - 6 = 4.'),
          ]),
      ],
      f1=B('Interpret the slope and intercept of a linear model in context', 'HSS-ID.C.7', [
          sa('A model for the number n of ice pops sold on a day with a high temperature of t °F is n = 4t - 200.\nWhat does the slope mean?', 'Meaning:',
             key='About 4 more ice pops are sold for each 1 °F rise in temperature.'),
          sa('A model for ice-pop sales is n = 4t - 200, where t is the temperature in °F.\nDoes the intercept -200 make sense in this situation? Explain.', 'Answer:',
             key='No. It would mean -200 ice pops sold at 0 °F, but sales cannot be negative.'),
          mc('A model for a phone\'s battery level b (percent) after h hours of use is b = 100 - 12.5h.\nWhat does 100 mean?',
             ['The battery starts at 100%.', 'The battery lasts 100 hours.', 'The battery loses 100% each hour.', 'The battery charges 100% each hour.']),
          tf('In the model y = 0.8x + 2, y increases by about 0.8 for each increase of 1 in x.', key=True),
          tf('In a linear model, the intercept always has a sensible meaning in the situation.', key=False),
      ]),
      f2=B('Evaluate reports and predictions based on data', 'HSS-IC.B.6', [
          sa('A model of children\'s heights for ages 2 to 10 is h = 2.5a + 31 inches at age a.\nA report uses it to predict the height of a 40-year-old. Is that reasonable? Explain.', 'Answer:',
             key='No. It predicts 131 inches (about 11 feet). The model fits only ages 2 to 10, so using it far outside the data is not reliable.'),
          sa('A line of fit was made from data collected between 60 °F and 90 °F, and the data points lie close to the line.\nA report uses it to predict sales at 70 °F. Is that reasonable? Explain.', 'Answer:',
             key='Yes. 70 °F is inside the range of the data, and the line fits the data closely.', note='A reason about the data range is required; noting how well the line fits is also expected.'),
          mc('A report says: "People who own more books live longer, so buying books makes you live longer."\nWhat is the main flaw?',
             ['It treats an association as a cause.', 'It counts too few books.', 'It uses a line of fit.', 'It reports a positive association.']),
          tf('Predictions far outside the range of the data are less reliable than predictions inside it.', key=True),
          tf('A survey of volunteers always represents the whole population.', key=False),
      ])),

    # ------------------------------------------------------------------ 8.SP.A.4 (construct)
    S('8.SP.A.4', 'Construct a two-way table summarizing data on two categorical variables',
      main=[
          plot('60 students were asked whether they have a curfew and whether they have chores. 36 have a curfew. 24 of the students with a curfew have chores. 8 of the students without a curfew have chores.\nComplete the two-way table.',
               blank_tw('Curfew', 'No curfew', 'Chores', 'No chores'),
               key='Curfew: 24 chores, 12 no chores, 36 total. No curfew: 8 chores, 16 no chores, 24 total. Totals: 32 chores, 28 no chores, 60 in all.'),
          plot('50 students were asked whether they prefer summer or winter. 22 are in Grade 7 and 28 are in Grade 8. 15 of the Grade 7 students and 18 of the Grade 8 students prefer summer.\nComplete the two-way table.',
               blank_tw('Grade 7', 'Grade 8', 'Summer', 'Winter'),
               key='Grade 7: 15 summer, 7 winter, 22 total. Grade 8: 18 summer, 10 winter, 28 total. Totals: 33 summer, 17 winter, 50 in all.'),
          plot('90 people were asked whether they exercise daily and whether they eat breakfast. 40 exercise daily. 30 of the people who exercise daily eat breakfast. 50 of the 90 people eat breakfast.\nComplete the two-way table.',
               blank_tw('Exercises', 'Does not', 'Breakfast', 'No breakfast'),
               key='Exercises: 30 breakfast, 10 no breakfast, 40 total. Does not: 20 breakfast, 30 no breakfast, 50 total. Totals: 50 breakfast, 40 no breakfast, 90 in all.'),
          plot('Ten students answered two questions: "Do you have a pet?" and "Do you have a sibling?" Their answers (pet, sibling) are:\nyes–yes, yes–no, no–no, yes–yes, no–yes, yes–yes, no–no, no–yes, yes–no, no–no\nComplete the two-way table.',
               blank_tw('Pet', 'No pet', 'Sibling', 'No sibling'),
               key='Pet: 3 sibling, 2 no sibling, 5 total. No pet: 2 sibling, 3 no sibling, 5 total. Totals: 5 sibling, 5 no sibling, 10 in all.'),
          tf('A completed two-way table for 60 students has exactly two rows, Curfew and No curfew, and every student is in one of them. Its row totals can be 36 and 20.', key=False,
             note='Every student is in exactly one of the two rows, so the row totals must add to 60.'),
      ],
      back=[
          B('Report the number of observations in a data set', '6.SP.B.5.a', [
              sa('In a survey, 12 students chose soccer, 9 chose basketball, and 7 chose tennis.\nHow many students were surveyed?', 'Students:', key='28'),
              sa('How many observations are shown in the dot plot?', 'Observations:', fig=dot(0, 5, [0, 1, 1, 2, 2, 2, 3, 4, 4], xlabel='Goals scored'), key='9'),
              mc('Each of 25 students named a favorite fruit. 5 different fruits were named.\nHow many observations are in the data set?', ['25', '5', '30', '125']),
              tf('If 14 students answer yes and 11 answer no, there are 25 observations.', key=True),
              tf('The data set 3, 3, 5, 7 has 3 observations.', key=False, note='It has 4 observations.'),
          ]),
          B('Solve "how many more" and "how many in all" problems with a scaled bar graph', '3.MD.B.3', [
              sa('How many more students chose dogs than fish?', 'Answer:', fig=PETS, key='4'),
              sa('How many students chose a pet in all?', 'Answer:', fig=PETS, key='18'),
              mc('How many fewer students chose fish than cats?', ['2', '4', '10', '6'], fig=PETS),
              tf('Fewer students chose cats than fish.', fig=PETS, key=False, note='6 chose cats and 4 chose fish.'),
              tf('The same number of students chose dogs and cats.', fig=PETS, key=False),
          ]),
      ],
      f1=B('Find joint, marginal, and conditional relative frequencies in a two-way table', 'HSS-ID.B.5', [
          sa('What is the joint relative frequency of students who have a curfew and have chores?', 'Relative frequency:', fig=CURFEW, key='0.4', note='{24/60} or 40% is also correct.'),
          sa('What is the marginal relative frequency of students who have chores? Round to the nearest hundredth.', 'Relative frequency:', fig=CURFEW, key='0.53'),
          mc('What is the conditional relative frequency of having chores among students with no curfew?', ['{1/3}', '{2/3}', '{2/15}', '{1/4}'], fig=CURFEW),
          tf('The marginal relative frequency of students with a curfew is 0.36.', fig=CURFEW, key=False, note='It is {36/60} = 0.6.'),
          tf('The joint relative frequencies in the four inner cells add to 2.', fig=CURFEW, key=False, note='They add to 1.'),
      ]),
      f2=B('Use a two-way table to find conditional probabilities and decide whether events are independent', 'HSS-CP.A.4', [
          sa('A student from the table is chosen at random.\nFind P(in club | Grade 8).', 'Probability:', fig=CLUB, key='0.3', note='{18/60} is also correct.'),
          sa('Are being in the club and being in Grade 7 independent? Explain with conditional probabilities.', 'Answer:', fig=CLUB,
             key='Yes. P(club | Grade 7) = {12/40} = 0.3 and P(club | Grade 8) = {18/60} = 0.3, both equal to P(club) = 0.3.'),
          mc('A student from the table is chosen at random.\nFind P(Grade 7 | in club).', ['0.4', '0.3', '0.12', '0.6'], fig=CLUB),
          tf('For a student chosen at random from the table, P(not in club) = 0.7.', fig=CLUB, key=True),
          tf('For the table, P(in club | Grade 7) equals P(Grade 7 | in club).', fig=CLUB, key=False, note='They are 0.3 and 0.4.'),
      ])),

    # ------------------------------------------------------------------ 8.SP.A.4 (relative frequencies)
    S('8.SP.A.4', 'Use relative frequencies in a two-way table to describe a possible association',
      main=[
          sa('For each row, what percent of the people use a phone at night?', 'Answer:', fig=PHONE,
             key='Sleeps 8+ hours: 30%. Sleeps under 8 hours: 60%.', note='Both percents are required.'),
          sa('Is there evidence of an association between sleep and phone use at night? Explain using the row relative frequencies.', 'Answer:', fig=PHONE,
             key='Yes. 60% of those who sleep under 8 hours use a phone at night, but only 30% of those who sleep 8+ hours do.'),
          mc('Which conclusion do the row relative frequencies support?', ['There is no association: 60% of each grade eat breakfast.', 'Grade 8 students are more likely to eat breakfast.',
                                                                         'Grade 7 students are more likely to eat breakfast.', 'There is a strong association because 45 is greater than 30.'], fig=BREAKFAST),
          sa('What percent of the people who use a phone at night sleep under 8 hours?', 'Percent:', fig=PHONE, key='75%'),
          tf('Grade 8 students are more likely to eat breakfast than Grade 7 students, because 45 is greater than 30.', fig=BREAKFAST, key=False,
             note='Both grades have 60%; compare relative frequencies, not counts.'),
      ],
      back=[
          B('Find a percent of a quantity and the percent one number is of another', '6.RP.A.3.c', [
              sa('What percent of 40 is 12?', 'Percent:', key='30%'),
              sa('Find 60% of 75.', 'Answer:', key='45'),
              mc('36 out of 48 is what percent?', ['75%', '36%', '48%', '12%']),
              tf('15 out of 60 is 15%.', key=False, note='15 out of 60 is 25%.'),
              tf('20% of 50 is 20.', key=False, note='20% of 50 is 10.'),
          ]),
          B('Use ratio language to describe two quantities', '6.RP.A.1', [
              sa('In a group, 12 people use a phone at night and 28 do not.\nWrite the ratio of users to non-users in simplest form.', 'Ratio:', key='3 : 7'),
              sa('A class has 18 students who walk to school and 12 who ride.\nFor every 3 students who walk, how many ride?', 'Answer:', key='2'),
              mc('In a survey, 30 people eat breakfast and 20 do not.\nWhich statement describes the ratio?', ['For every 3 who eat breakfast, 2 do not.', 'For every 2 who eat breakfast, 3 do not.',
                                                                                                        'For every 3 who eat breakfast, 5 do not.', 'For every 1 who eats breakfast, 30 do not.']),
              tf('The ratio 24 : 16 is equivalent to 3 : 2.', key=True),
              tf('The ratio 10 : 15 is equivalent to 3 : 2.', key=False, note='10 : 15 is equivalent to 2 : 3.'),
          ]),
      ],
      f1=B('Recognize conditional probability and independence in everyday situations', 'HSS-CP.A.5', [
          sa('Explain the difference between P(sleeps under 8 hours | uses a phone at night) and P(uses a phone at night | sleeps under 8 hours).', 'Answer:',
             key='The first is the chance that a night phone user sleeps under 8 hours; the second is the chance that a person who sleeps under 8 hours uses a phone at night. The condition (the group you look in) is different.'),
          sa('A fair coin is flipped twice, and the flips are independent.\nIs P(second flip is heads | first flip is heads) equal to P(second flip is heads)? Explain.', 'Answer:',
             key='Yes. Both are {1/2}; the first flip does not change the second.'),
          mc('Which pair of events is most likely independent?', ['Rolling a 6 on a fair number cube and flipping heads on a fair coin', 'Smoking and getting lung disease',
                                                                  'Studying more and getting a higher grade', 'Rain today and carrying an umbrella today']),
          tf('If two events are independent, knowing that one happened does not change the probability of the other.', key=True),
          tf('P(A | B) is always equal to P(B | A).', key=False),
      ]),
      f2=B('Find a conditional probability as the fraction of B\'s outcomes that are also in A', 'HSS-CP.B.6', [
          sa('A fair number cube numbered 1 to 6 is rolled.\nGiven that the roll is even, what is the probability that it is greater than 3?', 'Probability:', key='{2/3}'),
          sa('Two fair coins are flipped, and the flips are independent.\nGiven that at least one coin shows heads, what is the probability that both show heads?', 'Probability:', key='{1/3}'),
          mc('Of 100 people, 48 use a phone at night, and 36 of those sleep under 8 hours.\nA night phone user is chosen at random. What is P(sleeps under 8 hours | uses a phone at night)?',
             ['0.75', '0.36', '0.48', '0.6']),
          tf('A card is drawn at random from cards numbered 1 to 10.\nGiven that the number is odd, the probability that it is 5 or less is {3/5}.', key=True),
          tf('A fair number cube numbered 1 to 6 is rolled.\nGiven that the roll is less than 3, the probability that it is 1 is {1/6}.', key=False, note='Only 1 and 2 are possible, so it is {1/2}.'),
      ])),
]
