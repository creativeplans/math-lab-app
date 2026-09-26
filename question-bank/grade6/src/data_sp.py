from math import gcd

from qb import S, B, sa, mc, tf, nl, coord, q1, table, hist, dot, box, hrow, plot

SPORT = hist(['Soccer', 'Basketball', 'Baseball', 'Tennis'], [7, 5, 3, 1], gap=0.35, ymax=8, ystep=1,
             xlabel='Favorite sport', ylabel='Students', h=200)
PETS5 = hist(['Dogs', 'Cats', 'Birds', 'Fish'], [15, 10, 5, 20], gap=0.35, ymax=25, ystep=5,
             xlabel='Pets at a shelter', ylabel='Number', h=200)
BOOKS = hist(['0–9', '10–19', '20–29', '30–39'], [3, 7, 6, 2], ymax=8, ystep=1,
             xlabel='Books read this year', ylabel='Students', h=200)


def fracs(vmin, vmax, d):
    out = {}
    n = round(vmin * d)
    while n <= round(vmax * d):
        w, r = divmod(int(n), d)
        if r == 0:
            t = str(w)
        else:
            g = gcd(r, d)
            t = (str(w) if w else '') + '{%d/%d}' % (r // g, d // g)
        out[n / d] = t
        n += 1
    return out


def blank_hist(bins, ymax, ystep, xlabel, ylabel='Frequency'):
    return hist(bins, [0] * len(bins), ymax=ymax, ystep=ystep, xlabel=xlabel, ylabel=ylabel, h=200)


PLANTS = dot(0, 1, {0.25: 2, 0.5: 3, 0.75: 1, 1: 2}, step=0.25, labels=fracs(0, 1, 4), xlabel='Plant height (inches)')
BEAKERS = dot(0, 0.625, {0.125: 1, 0.25: 3, 0.375: 2, 0.5: 2}, step=0.125, labels=fracs(0, 0.625, 8), xlabel='Liquid in each beaker (liters)')
RIBBONS = dot(0, 2, {0.5: 2, 1: 4, 1.5: 3, 2: 1}, step=0.5, labels=fracs(0, 2, 2), xlabel='Ribbon length (feet)')
PENCILS = dot(3, 5, {3: 1, 3.5: 3, 4: 4, 4.5: 2, 5: 1}, step=0.5, labels=fracs(3, 5, 2), xlabel='Pencil length (inches)')

SYM = dot(0, 6, {1: 1, 2: 3, 3: 5, 4: 3, 5: 1})
SKEWR = dot(0, 8, {0: 6, 1: 5, 2: 3, 3: 2, 4: 1, 6: 1}, xlabel='Pets per student')
SKEWL = dot(0, 10, {3: 1, 5: 1, 6: 2, 7: 3, 8: 5, 9: 6}, xlabel='Quiz score')
RANGE = dot(10, 20, {11: 1, 12: 2, 14: 3, 15: 2, 18: 1}, lstep=2, xlabel='Minutes to finish a puzzle')
CLUST = dot(0, 10, {2: 1, 7: 3, 8: 5, 9: 3}, xlabel='Hours of sleep')
OBS = dot(0, 8, {1: 2, 2: 4, 3: 5, 4: 3, 5: 2, 7: 1}, xlabel='Books borrowed')
JUMP = dot(50, 70, {54: 1, 56: 2, 58: 3, 60: 4, 62: 2, 66: 1}, step=2, xlabel='Jump length (?)')
TEAMA = dot(58, 72, {60: 1, 61: 2, 62: 3, 63: 2, 64: 1}, lstep=2, xlabel='Heights (inches)')
DOTMEAN = dot(0, 10, {2: 2, 4: 3, 6: 1, 8: 2}, xlabel='Goals scored')
BELL = hist(['0–9', '10–19', '20–29', '30–39', '40–49'], [1, 4, 7, 4, 1], ymax=8, ystep=1,
            xlabel='Minutes of reading', ylabel='Students', h=200)

SHELLS = dot(1, 3, {1: 2, 1.25: 1, 1.5: 4, 2: 3, 2.5: 1}, step=0.25, labels=fracs(1, 3, 4), xlabel='Shell length (inches)')
LEAVES = dot(2, 4, {2: 1, 2.5: 3, 3: 2, 3.5: 4, 4: 1}, step=0.5, labels=fracs(2, 4, 2), xlabel='Leaf length (cm)')
CLASSES = dict(k='vstack', h=215, figs=[
    dot(2, 10, {6: 1, 7: 3, 8: 4, 9: 2}, title='Class A quiz scores'),
    dot(2, 10, {3: 1, 4: 2, 5: 4, 6: 3}, title='Class B quiz scores')])
SLEEP = dot(3, 10, {4: 1, 7: 2, 8: 6, 9: 5, 10: 1}, xlabel='Hours of sleep last night')
WALKT = dot(0, 30, {5: 2, 6: 3, 7: 3, 8: 2, 10: 2, 25: 1, 28: 1, 30: 1}, lstep=5, xlabel='Minutes to walk home')
AGES = hist(['0\u20139', '10\u201319', '20\u201329', '30\u201339', '40\u201349'], [6, 9, 0, 3, 1], ymax=10, ystep=2,
            xlabel='Ages of people at a youth soccer game', ylabel='People', h=200)
SCORES = dot(10, 100, {20: 1, 70: 1, 75: 2, 80: 3, 85: 3, 90: 2, 95: 1}, step=5, lstep=10, xlabel='Test scores')
TEMPS = dot(55, 90, {60: 1, 62: 2, 64: 3, 65: 4, 66: 3, 68: 2, 70: 1, 88: 1}, lstep=5, xlabel='Daily high temperature (°F)')
TEAMS = dict(k='vstack', h=215, figs=[
    dot(58, 72, {60: 1, 61: 2, 62: 3, 63: 2, 64: 1}, lstep=2, title='Garden A: plant heights (cm)'),
    dot(58, 72, {66: 1, 67: 2, 68: 3, 69: 2, 70: 1}, lstep=2, title='Garden B: plant heights (cm)')])
SPREAD2 = dict(k='vstack', h=215, figs=[
    dot(0, 12, {5: 2, 6: 4, 7: 3}, title='Data set A'),
    dot(0, 12, {1: 1, 3: 2, 6: 2, 9: 2, 11: 2}, title='Data set B')])
TWOBOX = box(50, 100, None, step=5, lstep=10, boxes=[('Class A', (60, 70, 78, 85, 95)), ('Class B', (55, 62, 70, 76, 90))],
             xlabel='Test scores')
TWOHIST = hrow(hist(['0–4', '5–9', '10–14', '15–19'], [2, 6, 3, 1], ymax=7, ystep=1, xlabel='Sample A', ylabel='Count'),
               hist(['0–4', '5–9', '10–14', '15–19'], [1, 2, 6, 3], ymax=7, ystep=1, xlabel='Sample B', ylabel='Count'), h=210)
BOX51 = box(0, 30, (4, 9, 14, 21, 28), step=2, lstep=10)
BOX51B = box(0, 30, (5, 10, 16, 18, 25), step=2, lstep=10)

PETTABLE = table([['', 'Has a pet', 'No pet', 'Total'], ['Grade 7', '18', '12', '30'], ['Grade 8', '20', '10', '30'],
                  ['Total', '38', '22', '60']], header='both')
MUSIC = table([['', 'Plays sports', 'No sports', 'Total'], ['Plays an instrument', '14', '6', '20'],
               ['No instrument', '16', '4', '20'], ['Total', '30', '10', '40']], header='both')
WALK = table([['', 'Walks to school', 'Rides to school', 'Total'], ['Grade 6', '12', '18', '30'],
              ['Grade 8', '15', '5', '20'], ['Total', '27', '23', '50']], header='both')


def two_way(r1, r2, c1, c2):
    return table([['', c1, c2, 'Total'], [r1, '', '', ''], [r2, '', '', ''], ['Total', '', '', '']], header='both')


def sc(pts, xlabel, ylabel, x=(0, 9), y=(0, 10), xstep=1, ystep=1, lines=()):
    return coord(x=x, y=y, xstep=xstep, ystep=ystep, square=False, axisnames=False, xlabel=xlabel, ylabel=ylabel,
                 pts=[(a, b) for a, b in pts], lines=list(lines))


POS = sc([(1, 55), (2, 60), (3, 62), (4, 70), (5, 74), (6, 80), (7, 83), (8, 90)], 'Hours studied', 'Test score', y=(50, 100), ystep=10)
NEG = sc([(1, 92), (2, 88), (3, 85), (4, 80), (5, 74), (6, 72), (7, 65), (8, 60)], 'Hours of TV per day', 'Test score', y=(50, 100), ystep=10)
NONE = sc([(1, 6), (2, 2), (3, 8), (4, 4), (5, 7), (6, 3), (7, 5), (8, 8), (2, 5), (6, 6)], 'Shoe size', 'Pets owned')
NONLIN = sc([(1, 1), (2, 1.5), (3, 2.5), (4, 4), (5, 6), (6, 8.5)], 'Week', 'Plant height (cm)', x=(0, 7))
OUT = sc([(1, 55), (2, 61), (3, 64), (4, 70), (5, 73), (6, 79), (7, 55), (8, 89)], 'Hours studied', 'Test score', y=(50, 100), ystep=10)
OUT2 = sc([(1, 2), (2, 3), (3, 3.5), (4, 5), (5, 9.5), (6, 6.5), (7, 7.5)], 'Age (years)', 'Height (ft)', x=(0, 8))
CLUS = sc([(1, 2), (1.5, 2.5), (2, 2), (2, 3), (6, 7), (6.5, 8), (7, 7), (7, 8.5), (6.5, 7.5)], 'Age of car (years)', 'Repairs', x=(0, 9))
FITPTS = [(1, 3), (2, 4.5), (3, 5), (4, 6), (5, 7.5), (6, 8), (7, 9.5)]
FIT = sc(FITPTS, 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 2), (8, 10))])
BADFIT = sc(FITPTS, 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 0), (8, 2))])
DOWNPTS = [(1, 9), (2, 8.5), (3, 7), (4, 6.5), (5, 5), (6, 4.5), (7, 3)]
FITD = sc(DOWNPTS, 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 10), (8, 2))])
BADFITD = sc(DOWNPTS, 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 6), (8, 6))])
OUT3 = sc([(1, 20), (2, 28), (3, 35), (4, 41), (5, 50), (6, 20), (7, 64)], 'Weeks', 'Savings ($)', x=(0, 8), y=(0, 70), ystep=10)
OUT4 = sc([(1, 8), (2, 7.5), (3, 6), (4, 5.5), (5, 1), (6, 3.5), (7, 3)], 'Price ($)', 'Number sold', x=(0, 8))
GOODPTS = [(1, 2), (2, 3.5), (3, 3.5), (4, 5), (5, 6.5), (6, 6.5), (7, 8)]
GOOD2 = sc(GOODPTS, 'x', 'y', x=(0, 8), y=(0, 10), lines=[((0, 1.5), (8, 9.1))])
BAD2 = sc(GOODPTS, 'x', 'y', x=(0, 8), y=(0, 10), lines=[((0, 8), (8, 2))])
BAD3 = sc(GOODPTS, 'x', 'y', x=(0, 8), y=(0, 10), lines=[((0, 2), (8, 2))])
FITOUT2 = sc([(1, 9), (2, 8), (3, 4), (4, 6), (5, 5), (6, 4), (7, 3)], 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 10), (8, 2))])
FITOUT = sc([(1, 3), (2, 4), (3, 5), (4, 10), (5, 7), (6, 8), (7, 9)], 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 2), (8, 10))])

SETS = [
    # ------------------------------------------------------------------ 6.SP.A.1
    S('6.SP.A.1', 'Recognize statistical questions',
      main=[
          mc('Which question is a statistical question?',
             ['How many hours of sleep do students in my class get each night?', 'How many hours did I sleep last night?',
              'How many days are in a week?', 'What time does our school start?']),
          tf('"How tall is the flagpole at our school?" is a statistical question.'),
          mc('Which question is NOT a statistical question?',
             ['What is the population of our city right now?', 'How many pets do the students in grade 6 have?',
              'How long do students spend on homework each day?', 'How much do the dogs at the shelter weigh?']),
          tf('"What are the ages of the teachers at our school?" is a statistical question.'),
          mc('Which question is a statistical question?',
             ['How many minutes do the players on our team practice each week?', 'How many minutes are in an hour?',
              'How many minutes did Coach Lee practice today?', 'How many players are on a soccer field at once?']),
      ],
      back=[
          B('Reading a bar graph', '3.MD.B.3', [
              sa('The graph shows the favorite sports of a class.\nHow many students chose basketball?', 'Students:', fig=SPORT),
              sa('The graph shows the favorite sports of a class.\nHow many more students chose soccer than baseball?', 'Students:', fig=SPORT),
              mc('Which sport did 3 students choose?', ['Baseball', 'Soccer', 'Basketball', 'Tennis'], fig=SPORT),
              sa('The graph shows the favorite sports of a class.\nHow many students answered in all?', 'Students:', fig=SPORT),
              tf('More students chose basketball than soccer.', fig=SPORT),
          ]),
          B('Reading a line plot', '4.MD.B.4', [
              sa('The line plot shows the heights of plants.\nHow many plants are {1/2} inch tall?', 'Plants:', fig=PLANTS),
              sa('The line plot shows the heights of plants.\nHow many plants were measured?', 'Plants:', fig=PLANTS),
              tf('The most common plant height is {3/4} inch.', fig=PLANTS),
              mc('Which height appears least often?', ['{3/4} inch', '{1/4} inch', '{1/2} inch', '1 inch'], fig=PLANTS),
              sa('What is the difference between the tallest and the shortest plant heights?', 'Difference:', fig=PLANTS),
          ]),
      ],
      f1=B('Random samples and representative samples', '7.SP.A.1', [
          mc('A principal wants to know the favorite lunch of all 600 students.\nWhich sample is most likely to represent all students?',
             ['50 students chosen at random from the whole school', 'The 30 students in one class', 'The first 50 students in line on pizza day', 'The students on the soccer team']),
          tf('A random sample is more likely to represent a population than a sample of your friends.'),
          sa('A reporter asks only basketball players, "What is your favorite sport?"\nWhy is this sample biased?', 'Reason:'),
          mc('A random sample of 40 students out of 800 shows that 10 walk to school.\nAbout how many of the 800 students walk to school?', ['200', '10', '40', '80']),
          tf('Conclusions about a population from a sample are valid only if the sample represents the population.'),
      ]),
      f2=B('Statistical questions about two variables and scatter plots', '8.SP.A.1', [
          mc('What type of association does the scatter plot show?', ['Positive linear', 'Negative linear', 'No association', 'Nonlinear'], fig=POS),
          mc('What type of association does the scatter plot show?', ['Negative linear', 'Positive linear', 'No association', 'Nonlinear'], fig=NEG),
          tf('A scatter plot shows data about two variables for each person or object.'),
          mc('Which question would be best answered with a scatter plot?',
             ['Is there a relationship between height and arm span?', 'What is the most common eye color?', 'How many students ride the bus?', 'What is the median age in the class?']),
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.2 shape
    S('6.SP.A.2', 'Describe the overall shape of a distribution',
      main=[
          mc('Which word best describes the shape of the data?', ['Symmetric', 'Skewed right', 'Skewed left', 'Uniform'], fig=SYM),
          mc('Which word best describes the shape of the data?', ['Skewed right', 'Symmetric', 'Skewed left', 'Uniform'], fig=SKEWR),
          mc('Which word best describes the shape of the data?', ['Skewed left', 'Skewed right', 'Symmetric', 'Uniform'], fig=SKEWL),
          mc('Which word best describes the shape of the data in the histogram?', ['Symmetric', 'Skewed right', 'Skewed left', 'Uniform'], fig=BELL),
          tf('The data are skewed right.', fig=SKEWL),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('How many ribbons are 1 foot long?', 'Ribbons:', fig=RIBBONS),
              sa('How many ribbons are there in all?', 'Ribbons:', fig=RIBBONS),
              tf('Two ribbons are {1/2} foot long.', fig=RIBBONS),
              mc('Which ribbon length is most common?', ['1 foot', '{1/2} foot', '1{1/2} feet', '2 feet'], fig=RIBBONS),
              sa('How many ribbons are longer than 1 foot?', 'Ribbons:', fig=RIBBONS),
          ]),
          B('Most and least in a bar graph', '3.MD.B.3', [
              mc('Which pet does the shelter have the most of?', ['Fish', 'Dogs', 'Cats', 'Birds'], fig=PETS5),
              mc('Which pet does the shelter have the fewest of?', ['Birds', 'Dogs', 'Cats', 'Fish'], fig=PETS5),
              tf('The shelter has more dogs than cats.', fig=PETS5),
              sa('How many more fish than birds are at the shelter?', 'Number:', fig=PETS5),
              tf('The tallest bar shows the smallest number.', fig=PETS5),
          ]),
      ],
      f1=B('Compare two distributions visually', '7.SP.B.3', [
          sa('About how many centimeters greater is the center of Garden B\'s plant heights?', 'Centimeters:', fig=TEAMS),
          tf('The two distributions have about the same shape and spread.', fig=TEAMS),
          mc('Which statement is true?', ['The distributions do not overlap.', 'Garden A\'s plants are typically taller.', 'Garden B has more variability.', 'The centers are equal.'], fig=TEAMS),
          sa('Garden A\'s mean height is 62 cm and Garden B\'s is 68 cm. Each has a MAD of about 1 cm.\nThe difference in means is about how many times the MAD?', 'Times:'),
          mc('Two classes have mean scores of 78 and 84. Each has a MAD of 6.\nThe difference in means is how many times the MAD?', ['1', '2', '6', '0.5']),
      ]),
      f2=B('Linear and nonlinear patterns in scatter plots', '8.SP.A.1', [
          mc('Which describes the pattern in the scatter plot?', ['Nonlinear', 'Negative linear', 'No association', 'Constant'], fig=NONLIN),
          mc('Is the pattern in the scatter plot linear or nonlinear?', ['Linear', 'Nonlinear'], fig=POS),
          tf('The pattern in the scatter plot is linear.', fig=NONLIN),
          sa('How many clusters does the scatter plot show?', 'Clusters:', fig=CLUS),
          mc('Which describes the scatter plot?', ['No association', 'Positive linear', 'Negative linear', 'Nonlinear'], fig=NONE),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.2 center
    S('6.SP.A.2', 'Describe the center of a distribution',
      main=[
          sa('Around what value do most of the data cluster?', 'Value:', fig=CLUST),
          sa('The data are symmetric.\nWhat value is at the center of the distribution?', 'Value:', fig=SYM),
          mc('In which interval is the center of the data?', ['10–19', '0–9', '20–29', '30–39'], fig=BOOKS),
          sa('What value is at the center of the heights?', 'Value:', fig=TEAMA),
          tf('The center of the distribution is about 12.', fig=RANGE),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('How many pencils are 4 inches long?', 'Pencils:', fig=PENCILS),
              sa('How many pencils were measured?', 'Pencils:', fig=PENCILS),
              tf('Three pencils are 3{1/2} inches long.', fig=PENCILS),
              mc('Which pencil length is most common?', ['4 inches', '3{1/2} inches', '5 inches', '3 inches'], fig=PENCILS),
              sa('How many pencils are shorter than 4 inches?', 'Pencils:', fig=PENCILS),
          ]),
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n42, 24, 36, 18', 'Order:'),
              mc('Which number is greatest?', ['350', '305', '299', '53']),
              tf('These numbers are in order from least to greatest: 12, 21, 19, 30'),
              sa('Order from least to greatest.\n105, 150, 115', 'Order:'),
              mc('Which number is least?', ['89', '98', '91', '100']),
          ]),
          B('Halfway between two numbers', '2.MD.B.6', [
              sa('What number is halfway between 10 and 20?', 'Number:'),
              sa('What number is halfway between points A and B?', 'Number:', fig=nl(0, 10, 1, pts=[(2, 'A'), (8, 'B')])),
              tf('The number halfway between 60 and 64 is 62.'),
              mc('What number is halfway between 4 and 12?', ['8', '6', '16', '10']),
              sa('What number is halfway between 0 and 18?', 'Number:'),
          ]),
      ],
      f1=B('Compare the centers of two populations', '7.SP.B.4', [
          mc('Class A has a median score of 82. Class B has a median score of 75. The variability is similar.\nWhich statement is true?',
             ['Class A typically scored higher.', 'Class B typically scored higher.', 'The classes scored the same.', 'Class A\'s scores vary more.']),
          sa('Random samples: Town A has a mean age of 34 years. Town B has a mean age of 42 years.\nWhat is the difference in mean ages?', 'Difference:'),
          sa('In random samples, 7th graders sleep a median of 8 hours, and 6th graders sleep a median of 9 hours.\nWhich group typically sleeps more?', 'Group:'),
          mc('Sample A has a mean of 12 and Sample B has a mean of 15. The samples have similar variability.\nWhich conclusion is best?', ['Values in population B tend to be greater.', 'Values in population A tend to be greater.', 'The populations are the same.', 'No conclusion is possible.']),
          tf('To compare the centers of two populations, you can compare the medians of random samples.'),
      ]),
      f2=B('Use a line of best fit to make predictions', '8.SP.A.2', nearest=True, qs=[
          sa('Use the line of best fit to predict y when x = 6.', 'y =', fig=FIT),
          sa('Use the line of best fit to predict y when x = 2.', 'y =', fig=FIT),
          sa('Use the line of best fit to predict y when x = 4.', 'y =', fig=FITD),
          mc('Which statement about a line of best fit is true?', ['It shows the overall trend of the data.', 'It must pass through every point.', 'It must pass through the origin.', 'It is always horizontal.']),
          tf('A line of best fit usually has about the same number of points above it as below it.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.2 spread
    S('6.SP.A.2', 'Describe the spread of a distribution',
      main=[
          sa('What is the range of the data?', 'Range:', fig=RANGE),
          sa('What is the range of the data?', 'Range:', fig=SKEWR),
          mc('Which data set has the greater spread?', ['Data set B', 'Data set A', 'They have the same spread.'], fig=SPREAD2),
          sa('What is the range of the jump lengths?', 'Range:', fig=JUMP),
          tf('Data set A has a range of 2.', fig=SPREAD2),
      ],
      back=[
          B('Finding a difference', '2.NBT.B.5', [
              sa('The greatest value is 47. The least value is 18.\nWhat is the difference?', 'Difference:'),
              sa('Subtract.\n83 - 29', 'Difference:'),
              tf('62 - 35 = 27'),
              mc('91 - 46 = ?', ['45', '55', '47', '137']),
              sa('What is the difference between 66 and 54?', 'Difference:'),
          ]),
          B('Reading a line plot', '4.MD.B.4', [
              sa('What is the longest ribbon length shown?', 'Length:', fig=RIBBONS),
              sa('What is the shortest ribbon length shown?', 'Length:', fig=RIBBONS),
              tf('The longest pencil is 5 inches.', fig=PENCILS),
              mc('What is the shortest pencil length?', ['3 inches', '3{1/2} inches', '4 inches', '5 inches'], fig=PENCILS),
              sa('How many plants are 1 inch tall?', 'Plants:', fig=PLANTS),
          ]),
          B('Greatest and least numbers', '2.NBT.A.4', [
              sa('What is the greatest number?\n18, 81, 58, 85', 'Greatest:'),
              sa('What is the least number?\n204, 240, 402, 42', 'Least:'),
              tf('The least number in the list 33, 30, 13, 31 is 13.'),
              mc('Which number is greatest?', ['720', '702', '270', '207']),
              sa('What is the least number?\n66, 56, 65, 60', 'Least:'),
          ]),
      ],
      f1=B('Compare variability of two distributions', '7.SP.B.3', [
          mc('Which data set has more variability?', ['Data set B', 'Data set A', 'They are the same.'], fig=SPREAD2),
          sa('Class A\'s mean is 60 and Class B\'s mean is 66. Each class has a MAD of 3.\nThe difference in means is how many times the MAD?', 'Times:'),
          tf('Two data sets with means of 50 and 56 and MADs of 3 have means that differ by 2 MADs.'),
          mc('Data set A has a mean of 20 and a MAD of 2. Data set B has a mean of 21 and a MAD of 6.\nWhich statement is true?', ['Data set B\'s values are more spread out.', 'Data set A\'s values are more spread out.', 'The means differ by 3 MADs.', 'The data sets do not overlap.']),
          sa('Two data sets have means of 8 and 14. Each has a MAD of 1.5.\nThe difference in means is how many times the MAD?', 'Times:'),
      ]),
      f2=B('Judge how closely data fit a line', '8.SP.A.2', [
          tf('The line is a good fit for the data.', fig=FIT),
          tf('The line is a good fit for the data.', fig=BADFIT),
          mc('Which is a sign of a good line of best fit?', ['Points are close to the line on both sides.', 'All points are above the line.', 'All points are below the line.', 'The line goes through only one point.']),
          tf('The line is a good fit for the data.', fig=BADFITD),
          sa('Which point is farthest from the line?\nWrite its coordinates.', 'Point:', fig=FITOUT),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.3
    S('6.SP.A.3', 'A measure of center vs. a measure of variation',
      main=[
          mc('Which measure describes the center of a data set?', ['Median', 'Range', 'Interquartile range', 'Mean absolute deviation']),
          mc('Which measure describes how much the values in a data set vary?', ['Interquartile range', 'Mean', 'Median', 'The middle value']),
          tf('A measure of center summarizes all of the values in a data set with a single number.'),
          tf('A measure of variation describes how the values in a data set vary with a single number.'),
          mc('Which measure is a measure of variation?', ['Mean absolute deviation', 'Mean', 'Median', 'The middle value']),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('The line plot shows shell lengths.\nHow many shells are 1{1/2} inches long?', 'Shells:', fig=SHELLS),
              sa('The line plot shows shell lengths.\nHow many shells are there in all?', 'Shells:', fig=SHELLS),
              tf('Three shells are 2 inches long.', fig=SHELLS),
              mc('Which shell length is most common?', ['1{1/2} inches', '1 inch', '2 inches', '2{1/2} inches'], fig=SHELLS),
              sa('What is the total length of the 2-inch shells?', 'Total length:', fig=SHELLS),
          ]),
          B('Sharing a total equally', '5.MD.B.2', [
              sa('Three friends have 4, 6, and 8 stickers. They share all of the stickers equally.\nHow many stickers does each friend get?', 'Stickers:'),
              sa('Four jars hold 2, 3, 5, and 6 liters of water. The water is shared equally among the jars.\nHow much water is in each jar?', 'Liters:'),
              tf('Cups holding 1, 2, and 3 liters are shared equally. Each cup then holds 2 liters.'),
              mc('Five friends collected 3, 5, 6, 7, and 9 cans. They share the cans equally.\nHow many cans does each friend get?', ['6', '5', '30', '7']),
              sa('Two bottles hold {1/4} liter and {3/4} liter. The juice is shared equally between the bottles.\nHow much juice is in each bottle?', 'Liters:'),
          ]),
          B('Finding a difference', '2.NBT.B.5', [
              sa('Subtract.\n76 - 38', 'Difference:'),
              sa('The highest score is 95 and the lowest is 58.\nWhat is the difference?', 'Difference:'),
              tf('100 - 47 = 53'),
              mc('84 - 29 = ?', ['55', '65', '45', '113']),
              sa('Subtract.\n62 - 17', 'Difference:'),
          ]),
      ],
      f1=B('Compare populations using center and variability', '7.SP.B.4', [
          mc('Class A has a median score of 82 and an IQR of 10. Class B has a median score of 75 and an IQR of 10.\nWhich statement is true?',
             ['Class A typically scored higher.', 'Class B typically scored higher.', 'The classes scored the same.', 'Class A\'s scores vary more.']),
          tf('Two samples have the same median. The sample with the greater IQR has more variability.'),
          mc('Which measure is best for comparing the variability of two samples?', ['IQR', 'Median', 'Mean', 'Sample size']),
          sa('Sample A: mean 40, MAD 2. Sample B: mean 40, MAD 7.\nWhich sample has values that vary more?', 'Sample:'),
          sa('Store A\'s daily sales have a median of $520. Store B\'s have a median of $610. Their IQRs are similar.\nWhich store typically has greater daily sales?', 'Store:'),
      ]),
      f2=B('Interpret the slope and intercept of a linear model', '8.SP.A.3', nearest=True, qs=[
          sa('The model y = 2.5x + 40 predicts a test score y after x hours of study.\nWhat does the slope 2.5 mean?', 'Meaning:'),
          mc('The model y = 3x + 12 gives a plant\'s height y (cm) after x weeks.\nWhat does 12 represent?', ['The height at week 0', 'The growth per week', 'The number of weeks', 'The height after 12 weeks']),
          tf('In the model y = -0.5x + 30, y decreases by 0.5 for each increase of 1 in x.'),
          sa('The model y = 1.2x + 5 gives the length y (cm) of a fish at x months old.\nWhat does 5 represent?', 'Meaning:'),
          mc('In the model y = 45x + 200, what does 45 represent if y is dollars saved after x weeks?', ['Dollars saved per week', 'Starting savings', 'Number of weeks', 'Total savings']),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.4 dot plots
    S('6.SP.B.4', 'Display numerical data in a dot plot',
      main=[
          plot('Data: 2, 4, 4, 5, 7, 7, 7, 9\nMake a dot plot of the data on the number line.', nl(0, 10, 1, h=130)),
          plot('Number of pets: 0, 1, 1, 2, 2, 2, 3, 5\nMake a dot plot of the data on the number line.', nl(0, 6, 1, h=130)),
          plot('Quiz scores: 6, 7, 7, 8, 8, 8, 9, 10, 10\nMake a dot plot of the data on the number line.', nl(5, 10, 1, h=130)),
          plot('Ribbon lengths (feet): {1/2}, 1, 1, 1{1/2}, 2, 1\nMake a dot plot of the data on the number line.', nl(0, 2, 0.5, labels=fracs(0, 2, 2), h=130)),
          plot('Hours of sleep: 7, 8, 9, 8, 10, 7, 8\nMake a dot plot of the data on the number line.', nl(6, 11, 1, h=130)),
      ],
      back=[
          B('Line plots of whole-number measurements', '2.MD.D.9', [
              sa('Lengths (inches): 3, 4, 4, 5, 4\nIn a line plot, how many marks go above 4?', 'Marks:'),
              plot('Lengths (cm): 2, 3, 3, 5\nMake a line plot of the lengths.', nl(0, 6, 1, h=130)),
              tf('In a line plot of 6, 6, 7, 9, there are two marks above 6.'),
              mc('Which number line is best for a line plot of 12, 14, 15, 15?', ['A number line from 10 to 16', 'A number line from 0 to 5', 'A number line from 20 to 30', 'A number line from 0 to 100 by tens']),
              sa('Lengths (feet): 8, 9, 9, 9, 11\nWhich value gets the most marks?', 'Value:'),
          ]),
          B('Line plots with fractional measurements', '4.MD.B.4', [
              sa('Lengths (inches): {1/2}, 1, 1, 1{1/2}, 1, {1/2}\nIn a line plot, how many X\'s go above 1?', 'X\'s:'),
              tf('In a line plot of 2, 2{1/2}, 2{1/2}, 3, there are two X\'s above 2{1/2}.'),
              mc('Which number line would you use for these lengths?\n{1/4}, {1/2}, {3/4}, {1/2}', ['A number line from 0 to 1 marked in fourths', 'A number line from 0 to 10 marked in ones', 'A number line from 0 to 100 marked in tens', 'A number line from 1 to 2 marked in halves']),
              plot('Lengths (inches): {1/4}, {1/2}, {1/2}, {3/4}\nMake a line plot of the lengths.', nl(0, 1, 0.25, labels=fracs(0, 1, 4), h=130)),
              tf('A line plot shows each data value as a mark above a number line.'),
          ]),
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n7, 2, 9, 4, 4', 'Order:'),
              mc('Which list is in order from least to greatest?', ['6, 7, 8, 10', '7, 6, 8, 10', '6, 8, 7, 10', '10, 8, 7, 6']),
              tf('These numbers are in order from least to greatest: 1, 2, 5, 3'),
              sa('What are the least and greatest values?\n8, 10, 7, 9, 7', ['Least:', 'Greatest:']),
              mc('Which number is least?', ['0', '2', '1', '5']),
          ]),
      ],
      f1=B('Compare two dot plots', '7.SP.B.3', [
          sa('About how many points greater is the center of Class A\'s scores than Class B\'s?', 'Points:', fig=CLASSES),
          tf('The two dot plots overlap.', fig=CLASSES),
          mc('Which statement is true?', ['Class A\'s scores are typically higher.', 'Class B\'s scores are typically higher.', 'The medians are equal.', 'Class B has more variability.'], fig=CLASSES),
          sa('What is the range of each class\'s scores?', ['Class A:', 'Class B:'], fig=CLASSES),
          tf('Data set A and data set B have the same median.', fig=SPREAD2),
      ]),
      f2=B('Construct a scatter plot', '8.SP.A.1', [
          plot('Make a scatter plot of the data.', hrow(table([['Hours', '1', '2', '3', '4', '5'], ['Score', '60', '65', '75', '80', '90']], fs=0.85),
                                                        q1(6, 100, ystep=10, square=False, xlabel='Hours', ylabel='Score'), h=245)),
          plot('Make a scatter plot of the data.', hrow(table([['Age', '2', '4', '6', '8'], ['Height (in.)', '34', '40', '46', '50']], fs=0.85),
                                                        q1(10, 60, ystep=10, square=False, xlabel='Age', ylabel='Height'), h=245)),
          mc('A scatter plot shows age on the x-axis and height on the y-axis.\nA 10-year-old is 54 inches tall. Which point shows this person?', ['(10, 54)', '(54, 10)', '(10, 10)', '(54, 54)']),
          plot('Make a scatter plot of the data.', hrow(table([['Price ($)', '1', '2', '3', '4'], ['Sold', '9', '7', '4', '2']], fs=0.85),
                                                        q1(5, 10, square=False, xlabel='Price ($)', ylabel='Sold'), h=245)),
          tf('To make a scatter plot of height and arm span, each person is shown as one point.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.4 histograms
    S('6.SP.B.4', 'Display numerical data in a histogram',
      main=[
          plot('Books read: 3, 12, 15, 8, 22, 17, 25, 11, 31, 19\nMake a histogram of the data.', blank_hist(['0–9', '10–19', '20–29', '30–39'], 6, 1, 'Books read')),
          plot('Heights (in.): 52, 58, 61, 55, 63, 57, 66, 60, 54, 59\nMake a histogram of the data.', blank_hist(['50–54', '55–59', '60–64', '65–69'], 5, 1, 'Height (inches)')),
          plot('Ages: 11, 12, 12, 13, 14, 14, 14, 15, 16, 17, 19\nMake a histogram of the data.', blank_hist(['10–11', '12–13', '14–15', '16–17', '18–19'], 5, 1, 'Age (years)')),
          plot('Minutes of exercise: 5, 18, 22, 25, 30, 34, 41, 45, 12, 28\nMake a histogram of the data.', blank_hist(['0–15', '16–31', '32–47'], 6, 1, 'Minutes')),
          plot('Test scores: 62, 75, 78, 81, 84, 88, 90, 93, 95, 71, 86, 79\nMake a histogram of the data.', blank_hist(['60–69', '70–79', '80–89', '90–99'], 6, 1, 'Score')),
      ],
      back=[
          B('Drawing a scaled bar graph', '3.MD.B.3', [
              plot('Draw a bar graph: Red 4, Blue 6, Green 2.', blank_hist(['Red', 'Blue', 'Green'], 8, 1, 'Favorite color', 'Students')),
              sa('On a bar graph, the bar for "Cats" ends at 5 on a scale that counts by 1s.\nHow many cats does the bar show?', 'Cats:'),
              tf('On a bar graph with a scale of 2, a bar that stops halfway between 6 and 8 shows 7.'),
              mc('A bar graph has a scale that counts by 5s. A bar shows 20.\nHow many grid lines tall is the bar?', ['4', '20', '5', '15']),
              plot('Draw a bar graph: Apples 3, Pears 1, Plums 5.', blank_hist(['Apples', 'Pears', 'Plums'], 6, 1, 'Fruit', 'Number')),
          ]),
          B('Placing numbers in intervals', '2.NBT.A.4', [
              mc('Which interval contains 17?', ['10–19', '0–9', '20–29', '30–39']),
              tf('25 is in the interval 20–29.'),
              sa('Data: 3, 12, 15, 18, 22\nHow many of the numbers are in the interval 10–19?', 'Numbers:'),
              mc('Which number is in the interval 30–39?', ['34', '29', '40', '3']),
              tf('19 is in the interval 20–29.'),
          ]),
          B('Organizing data into categories', '1.MD.C.4', [
              sa('Data: cat, dog, cat, fish, dog, cat\nHow many answers are "cat"?', 'Cat:'),
              tf('Data: red, blue, red, red. There are 3 answers of "red."'),
              mc('Data: A, B, A, C, A, B\nWhich category has the most?', ['A', 'B', 'C']),
              sa('Data: yes, no, yes, yes, no\nHow many more "yes" answers than "no" answers are there?', 'More:'),
              sa('Data: 3, 7, 12, 14, 18\nHow many numbers are less than 10?', 'Numbers:'),
          ]),
      ],
      f1=B('Compare two populations shown in histograms', '7.SP.B.4', [
          mc('Which sample tends to have greater values?', ['Sample B', 'Sample A', 'They are the same.'], fig=TWOHIST),
          mc('In which interval is the median of Sample A?', ['5–9', '0–4', '10–14', '15–19'], fig=TWOHIST),
          sa('How many values are in each sample?', 'Values:', fig=TWOHIST),
          tf('Sample B has more values from 15 to 19 than Sample A.', fig=TWOHIST),
          mc('In which interval is the median of Sample B?', ['10–14', '5–9', '15–19', '0–4'], fig=TWOHIST),
      ]),
      f2=B('Display numerical data for two variables in a scatter plot', '8.SP.A.1', nearest=True, qs=[
          sa('Make a scatter plot of the data.\nDescribe the association between temperature and drinks sold.', 'Association:',
             fig=hrow(table([['Temp (°F)', '60', '70', '75', '85', '90'], ['Drinks sold', '20', '35', '40', '55', '65']], fs=0.8),
                      q1(100, 70, xstep=10, ystep=10, square=False, xlabel='Temperature (°F)', ylabel='Drinks sold'), h=245)),
          plot('Make a scatter plot of the data.', hrow(table([['Height (in.)', '50', '54', '58', '62'], ['Arm span (in.)', '49', '55', '57', '63']], fs=0.8),
                                                        q1(70, 70, xstep=10, ystep=10, square=False, xlabel='Height (in.)', ylabel='Arm span (in.)'), h=245)),
          mc('A data set gives the height and the shoe size of 20 students.\nWhich display shows how the two variables are related?', ['Scatter plot', 'Histogram', 'Box plot', 'Dot plot']),
          tf('A histogram displays one numerical variable, while a scatter plot displays two numerical variables for each person or object.'),
          sa('Make a scatter plot of the data.\nWhich point does not fit the pattern?', 'Point:',
             fig=hrow(table([['Hours', '1', '2', '3', '4', '5'], ['Score', '62', '68', '40', '80', '86']], fs=0.8),
                      q1(6, 100, ystep=10, square=False, xlabel='Hours', ylabel='Score'), h=245)),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.4 box plots
    S('6.SP.B.4', 'Display numerical data in a box plot',
      main=[
          plot('Data: 3, 5, 7, 8, 10, 12, 15\nMake a box plot of the data on the number line.', nl(0, 16, 1, labels=list(range(0, 17, 2)), h=130)),
          plot('Data: 12, 14, 15, 18, 20, 21, 25, 28\nMake a box plot of the data on the number line.', nl(10, 30, 1, labels=list(range(10, 31, 2)), h=130)),
          plot('Data: 40, 45, 45, 50, 55, 60, 70\nMake a box plot of the data on the number line.', nl(40, 70, 5, h=130)),
          plot('Data: 2, 4, 4, 5, 6, 8, 9, 11, 12\nMake a box plot of the data on the number line.', nl(0, 12, 1, h=130)),
          plot('Data: 21, 23, 24, 26, 28, 30, 31, 35\nMake a box plot of the data on the number line.', nl(20, 36, 1, labels=list(range(20, 37, 2)), h=130)),
      ],
      back=[
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n15, 8, 23, 4, 16', 'Order:'),
              mc('Which list is in order from least to greatest?', ['7, 12, 21, 27', '12, 7, 21, 27', '7, 21, 12, 27', '27, 21, 12, 7']),
              tf('These numbers are in order from least to greatest: 30, 33, 31, 35'),
              sa('Order from least to greatest.\n62, 26, 60, 20, 66', 'Order:'),
              mc('Which number is least?', ['108', '180', '118', '801']),
          ]),
          B('Halfway between two numbers', '2.MD.B.6', [
              sa('What number is halfway between 12 and 18?', 'Number:'),
              sa('What number is halfway between points A and B?', 'Number:', fig=nl(20, 30, 1, pts=[(20, 'A'), (30, 'B')])),
              tf('The number halfway between 40 and 50 is 45.'),
              mc('What number is halfway between 6 and 10?', ['8', '7', '16', '4']),
              sa('What number is halfway between 0 and 30?', 'Number:'),
          ]),
          B('Reading a number line scale', '4.MD.A.2', [
              sa('What number is at point A?', 'A =', fig=nl(0, 100, 10, minor=5, pts=[(65, 'A')])),
              sa('What number is at point B?', 'B =', fig=nl(0, 50, 10, minor=2, pts=[(34, 'B')])),
              tf('Point C is at 12.', fig=nl(0, 20, 5, minor=1, pts=[(12, 'C')])),
              mc('What number is at point D?', ['175', '170', '150', '180'], fig=nl(100, 200, 25, pts=[(175, 'D')])),
              sa('What number is at point E?', 'E =', fig=nl(0, 1000, 100, minor=50, labels=[0, 200, 400, 600, 800, 1000], pts=[(450, 'E')])),
          ]),
          B('Finding the median', '6.SP.B.5.c', [
              sa('Find the median.\n3, 5, 7, 8, 10, 12, 15', 'Median:'),
              sa('Find the median.\n12, 14, 15, 18, 20, 21, 25, 28', 'Median:'),
              tf('The median of 40, 45, 45, 50, 55, 60, 70 is 50.'),
              mc('What is the median of 2, 4, 4, 5, 6, 8, 9, 11, 12?', ['6', '5', '7', '8']),
              sa('Find the median of the lower half.\n3, 5, 7', 'Median:'),
          ]),
      ],
      f1=B('Compare populations with box plots', '7.SP.B.4', [
          mc('Which class has the greater median score?', ['Class A', 'Class B', 'They are the same.'], fig=TWOBOX),
          mc('By how many points do the medians differ?', ['8', '5', '15', '3'], fig=TWOBOX),
          sa('What is the interquartile range of Class A\'s scores?', 'IQR:', fig=TWOBOX),
          tf('At least half of Class A scored 78 or higher.', fig=TWOBOX),
          sa('Which class had the highest single score?', 'Class:', fig=TWOBOX),
      ]),
      f2=B('Spread and outliers in scatter plots', '8.SP.A.1', nearest=True, qs=[
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT3),
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT2),
          mc('Which describes the scatter plot?', ['Two clusters', 'A strong positive association', 'No pattern', 'A single outlier'], fig=CLUS),
          tf('An outlier in a scatter plot is a point that is far from the overall pattern.'),
          tf('The scatter plot shows no association.', fig=NONE),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.a
    S('6.SP.B.5.a', 'Report the number of observations',
      main=[
          sa('The dot plot shows how many books students borrowed.\nHow many observations are in the data set?', 'Observations:', fig=OBS),
          sa('How many students are represented in the histogram?', 'Students:', fig=BOOKS),
          sa('The table shows how many siblings students have.\nHow many observations are in the data set?', 'Observations:', fig=table([['Siblings', '0', '1', '2', '3'], ['Students', '4', '9', '6', '2']])),
          sa('The bar graph shows survey answers.\nHow many observations are in the data set?', 'Observations:', fig=SPORT),
          sa('Data: 12, 15, 9, 15, 20, 11, 13, 18, 15, 10\nHow many observations are in the data set?', 'Observations:'),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('The line plot shows pencil lengths.\nHow many pencils are 4 inches long?', 'Pencils:', fig=PENCILS),
              sa('The line plot shows pencil lengths.\nHow many pencils were measured?', 'Pencils:', fig=PENCILS),
              tf('Two pencils are 4{1/2} inches long.', fig=PENCILS),
              mc('How many pencils are longer than 4 inches?', ['3', '4', '2', '7'], fig=PENCILS),
              sa('How many X\'s are above 4{1/2}?', 'X\'s:', fig=PENCILS),
          ]),
          B('Totals from a bar graph', '3.MD.B.3', [
              sa('How many pets are at the shelter in all?', 'Pets:', fig=PETS5),
              sa('How many students chose soccer or tennis?', 'Students:', fig=SPORT),
              tf('12 students chose soccer or basketball.', fig=SPORT),
              mc('How many students did NOT choose soccer?', ['9', '7', '16', '5'], fig=SPORT),
              sa('How many dogs and cats are at the shelter together?', 'Number:', fig=PETS5),
          ]),
          B('Adding several two-digit numbers', '2.NBT.B.6', [
              sa('Add.\n14 + 23 + 31 + 12', 'Sum:'),
              sa('Add.\n25 + 18 + 30', 'Sum:'),
              tf('16 + 16 + 20 + 8 = 60'),
              mc('41 + 27 + 13 + 9 = ?', ['90', '80', '91', '100']),
              sa('Add.\n35 + 22 + 18 + 15', 'Sum:'),
          ]),
      ],
      f1=B('Use a random sample to make inferences', '7.SP.A.2', [
          mc('A researcher surveys 80 randomly chosen students out of 900.\nWhat is the sample size?', ['80', '900', '820', '980']),
          tf('A larger random sample generally gives a better estimate about a population.'),
          sa('In a random sample of 25 students out of 500, 5 like jazz.\nEstimate how many of the 500 students like jazz.', 'Estimate:'),
          mc('In a random sample of 50 voters, 30 support a new park. There are 2,000 voters.\nAbout how many voters support the park?', ['1,200', '600', '30', '1,500']),
          sa('Two random samples of 20 students each found 12 and 14 students who like pizza best.\nWhat is the mean of the two sample results?', 'Mean:'),
      ]),
      f2=B('Relative frequencies in two-way tables', '8.SP.A.4', [
          sa('What fraction of 7th graders have a pet? What fraction of 8th graders have a pet?', ['Grade 7:', 'Grade 8:'], fig=PETTABLE),
          mc('Compare the relative frequencies. Which grade has a greater fraction of pet owners?', ['Grade 8', 'Grade 7', 'They are the same.'], fig=PETTABLE),
          mc('What is the relative frequency of instrument players who also play sports?', ['0.7', '0.35', '0.47', '14'], fig=MUSIC),
          sa('Among students with no instrument, what fraction play sports?', 'Fraction:', fig=MUSIC),
          tf('Students with no instrument are more likely to play sports than students who play an instrument.', fig=MUSIC),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.b
    S('6.SP.B.5.b', 'Describe the attribute measured and its units',
      main=[
          sa('A data set lists the heights of 25 plants in centimeters.\nWhat attribute is being measured, and in what unit?', ['Attribute:', 'Unit:']),
          mc('A data set records the time each student spends on homework.\nWhich unit is most likely?', ['Minutes', 'Inches', 'Pounds', 'Degrees']),
          mc('The dot plot shows how far students jumped.\nWhich unit is most likely?', ['Inches', 'Miles', 'Pounds', 'Seconds'], fig=JUMP),
          sa('A data set lists the mass of each of 30 apples.\nWhat attribute is being measured, and what is a reasonable unit?', ['Attribute:', 'Unit:']),
          mc('A data set records how long each student\'s trip to school takes.\nWhich describes the attribute and its unit?', ['Time; minutes', 'Distance; minutes', 'Time; miles', 'Speed; pounds']),
      ],
      back=[
          B('Choosing measurement units', '4.MD.A.1', [
              mc('Which unit is best for measuring the length of a pencil?', ['Centimeters', 'Kilometers', 'Meters', 'Kilograms']),
              tf('A kilogram is heavier than a gram.'),
              mc('Which unit measures liquid volume?', ['Liters', 'Grams', 'Meters', 'Seconds']),
              sa('Name one unit used to measure time.', 'Unit:'),
              tf('An inch is longer than a foot.'),
          ]),
          B('What a bar graph shows', '3.MD.B.3', [
              sa('How many categories does the graph show?', 'Categories:', fig=SPORT),
              mc('What does the height of each bar show?', ['The number of students', 'The number of sports', 'The score of a game', 'The length of a game'], fig=SPORT),
              tf('"Tennis" is one of the categories in the graph.', fig=SPORT),
              mc('Which is a category in the graph?', ['Birds', 'Horses', 'Soccer', '25'], fig=PETS5),
              sa('What is being counted in the graph?', 'Answer:', fig=PETS5),
          ]),
          B('Choosing a measuring tool', '2.MD.A.1', [
              mc('Which tool measures the length of a table?', ['Tape measure', 'Scale', 'Clock', 'Thermometer']),
              mc('Which tool measures how heavy an apple is?', ['Scale', 'Ruler', 'Clock', 'Measuring cup']),
              tf('A clock measures time.'),
              mc('Which tool measures temperature?', ['Thermometer', 'Ruler', 'Scale', 'Yardstick']),
              sa('Name a tool that measures the length of a pencil.', 'Tool:'),
          ]),
      ],
      f1=B('How data are collected: sampling methods', '7.SP.A.1', [
          mc('Which method gives a random sample of the students in a school?', ['Draw names from a hat that holds every student\'s name', 'Ask your friends', 'Ask the students in the library', 'Ask the first 20 students to arrive']),
          tf('Surveying people who walk out of a gym is a good way to learn how often all people in a town exercise.'),
          sa('A town wants to know how residents feel about a new library.\nDescribe a way to choose a random sample.', 'Method:'),
          mc('Which sample is most likely to be biased?', ['Asking only people at a dog park whether they like dogs', 'Choosing 50 residents at random from a town list', 'Picking every 10th name from a school list', 'Drawing 30 names from a hat of all members']),
          tf('In a random sample, every member of the population has an equal chance of being chosen.'),
      ]),
      f2=B('Association between two categorical variables', '8.SP.A.4', [
          mc('Which pair of variables is categorical and could be shown in a two-way table?', ['Grade level and way of getting to school', 'Height and weight', 'Age and arm span', 'Hours slept and test score']),
          sa('What fraction of 6th graders walk to school?', 'Fraction:', fig=WALK),
          sa('What fraction of 8th graders walk to school?', 'Fraction:', fig=WALK),
          mc('What is the relative frequency of 8th graders who ride to school?', ['{1/4}', '{5/23}', '{1/10}', '{3/4}'], fig=WALK),
          tf('8th graders are more likely to walk to school than 6th graders.', fig=WALK),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c mean
    S('6.SP.B.5.c', 'Find the mean of a data set',
      main=[
          sa('Find the mean.\n4, 7, 9, 10, 15', 'Mean:'),
          sa('Five test scores are 82, 90, 75, 88, and 95.\nWhat is the mean score?', 'Mean:'),
          mc('Find the mean.\n12, 15, 18, 19', ['16', '64', '16.5', '15']),
          sa('The dot plot shows goals scored in 8 games.\nWhat is the mean number of goals?', 'Mean:', fig=DOTMEAN),
          sa('Find the mean.\n3.5, 4.2, 5.0, 6.1, 6.2', 'Mean:'),
      ],
      back=[
          B('Adding multi-digit numbers', '4.NBT.B.4', [
              sa('Add.\n82 + 90 + 75 + 88 + 95', 'Sum:'),
              sa('Add.\n145 + 238 + 97', 'Sum:'),
              tf('56 + 64 + 70 = 190'),
              mc('125 + 175 + 200 = ?', ['500', '400', '450', '550']),
              sa('Add.\n1,250 + 875', 'Sum:'),
          ]),
          B('Dividing a total into equal groups', '4.NBT.B.6', [
              sa('Divide.\n430 ÷ 5', 'Quotient:'),
              sa('Divide.\n64 ÷ 4', 'Quotient:'),
              tf('108 ÷ 4 = 27'),
              mc('252 ÷ 6 = ?', ['42', '41', '48', '36']),
              sa('Divide.\n315 ÷ 7', 'Quotient:'),
          ]),
          B('Sharing a total equally', '5.MD.B.2', [
              sa('Two friends have 5 and 9 shells. They share the shells equally.\nHow many shells does each friend get?', 'Shells:'),
              sa('Three boxes hold 2, 7, and 9 books. The books are shared equally among the boxes.\nHow many books are in each box?', 'Books:'),
              tf('Jars holding 4, 4, and 10 cups are shared equally. Each jar then holds 6 cups.'),
              mc('Four children have 1, 2, 6, and 7 cards. They share the cards equally.\nHow many cards does each child get?', ['4', '3', '16', '5']),
              sa('Two cups hold {1/3} cup and {2/3} cup of milk. The milk is shared equally.\nHow much is in each cup?', 'Cups:'),
          ]),
      ],
      f1=B('Compare populations using means', '7.SP.B.4', [
          sa('A random sample of 6th graders has a mean height of 58 in. A random sample of 8th graders has a mean height of 64 in.\nHow much greater is the 8th graders\' mean?', 'Difference:'),
          mc('Two random samples of plant heights have means of 24 cm and 30 cm. Each has a MAD of 3 cm.\nHow many MADs apart are the means?', ['2', '6', '3', '1']),
          tf('To compare two populations, you can compare the means of random samples from each population.'),
          sa('Sample A: mean 15.2 minutes. Sample B: mean 18.7 minutes.\nWhich population probably has greater values?', 'Population:'),
          mc('Ten random samples of 20 students gave these mean hours of sleep: 8.1, 8.3, 7.9, 8.0, 8.2, 8.1, 8.4, 7.8, 8.0, 8.2.\nWhat is a good estimate of the population mean?', ['About 8.1 hours', 'About 7 hours', 'About 9 hours', 'About 20 hours']),
      ]),
      f2=B('Use a linear model to make predictions', '8.SP.A.3', nearest=True, qs=[
          sa('The equation y = 2.5x + 40 models test score y after x hours of study.\nPredict the score for 8 hours of study.', 'Score:'),
          sa('The model y = 15x + 100 gives the cost y of x tickets.\nPredict the cost of 20 tickets.', 'Cost:'),
          mc('The model y = 3x + 12 gives a plant\'s height y (cm) after x weeks.\nWhat height does the model predict after 5 weeks?', ['27 cm', '15 cm', '60 cm', '36 cm']),
          sa('The model y = -0.5x + 30 gives the value y of a toy after x years.\nPredict the value after 6 years.', 'Value:'),
          tf('The model y = 4x + 10 predicts y = 50 when x = 10.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c median
    S('6.SP.B.5.c', 'Find the median of a data set',
      main=[
          sa('Find the median.\n12, 5, 9, 20, 7, 14', 'Median:'),
          tf('The median of 3, 8, 8, 10, 21 is 8.'),
          mc('Heights (in inches): 58, 60, 61, 63, 63\nWhat is the median height?', ['61', '63', '60', '61.5']),
          sa('What is the median of the data in the dot plot?', 'Median:', fig=SYM),
          sa('Find the median.\n4.5, 2.1, 3.8, 6.0', 'Median:'),
      ],
      back=[
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n12, 5, 9, 20, 7, 14', 'Order:'),
              mc('Which list is in order from least to greatest?', ['58, 60, 61, 63', '60, 58, 61, 63', '58, 61, 60, 63', '63, 61, 60, 58']),
              tf('These numbers are in order from least to greatest: 75, 82, 88, 90, 95'),
              sa('Order from least to greatest.\n47, 74, 44, 77', 'Order:'),
              mc('When 3, 9, and 6 are put in order, which number is in the middle?', ['6', '3', '9', '18']),
          ]),
          B('The number halfway between two numbers', '5.NBT.B.7', [
              sa('Find the value.\n(9 + 12) ÷ 2', 'Value:'),
              sa('Find the value.\n(3.8 + 4.5) ÷ 2', 'Value:'),
              tf('(6 + 9) ÷ 2 = 7.5'),
              mc('(20 + 25) ÷ 2 = ?', ['22.5', '22', '45', '23.5']),
              sa('Find the value.\n(3.5 + 4.5) ÷ 2', 'Value:'),
          ]),
          B('Reading a line plot', '4.MD.B.4', [
              sa('How many leaves are 3{1/2} cm long?', 'Leaves:', fig=LEAVES),
              sa('How many leaves were measured?', 'Leaves:', fig=LEAVES),
              tf('One leaf is 4 cm long.', fig=LEAVES),
              mc('Which leaf length is most common?', ['3{1/2} cm', '2{1/2} cm', '3 cm', '4 cm'], fig=LEAVES),
              sa('How many leaves are shorter than 3 cm?', 'Leaves:', fig=LEAVES),
          ]),
      ],
      f1=B('Compare populations using medians', '7.SP.B.4', [
          mc('Sample A has a median of 12 and Sample B has a median of 15. The samples have similar variability.\nWhich conclusion is best?', ['Values in population B tend to be greater.', 'Values in population A tend to be greater.', 'The populations are the same.', 'No conclusion is possible.']),
          sa('In random samples, the median commute is 25 minutes in Town X and 18 minutes in Town Y. The IQRs are similar.\nIn which town are commutes typically longer?', 'Town:'),
          sa('Sample A: median 42, IQR 8. Sample B: median 50, IQR 8.\nThe difference in medians is how many times the IQR?', 'Times:'),
          tf('When data are skewed, comparing medians is often better than comparing means.'),
          mc('Sample X has a median of 7.5 hours of sleep. Sample Y has a median of 8.5 hours. Both IQRs are 1 hour.\nWhich statement is best?', ['Population Y probably sleeps more.', 'Population X probably sleeps more.', 'They sleep the same amount.', 'Nothing can be said.']),
      ]),
      f2=B('Draw and use a line of best fit', '8.SP.A.2', nearest=True, qs=[
          plot('Draw a line of best fit for the data.', POS),
          plot('Draw a line of best fit for the data.', NEG),
          mc('A line of best fit should have ___.', ['about the same number of points above and below it', 'all points above it', 'all points below it', 'no points near it']),
          plot('Draw a line of best fit for the data.', sc(DOWNPTS, 'x', 'y', x=(0, 8), y=(0, 12))),
          tf('A line of best fit must pass through the first and last points.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c IQR
    S('6.SP.B.5.c', 'Find the interquartile range of a data set',
      main=[
          sa('Find the interquartile range.\n2, 4, 5, 7, 9, 11, 12, 15', 'IQR:'),
          sa('What is the interquartile range of the data in the box plot?', 'IQR:', fig=BOX51),
          mc('What is the interquartile range?\n10, 12, 15, 18, 20, 25, 30', ['13', '20', '18', '5']),
          sa('Find the interquartile range.\n3, 6, 6, 8, 9, 12, 14, 15, 18', 'IQR:'),
          sa('What is the interquartile range of the data in the box plot?', 'IQR:', fig=BOX51B),
      ],
      back=[
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n15, 9, 2, 12, 5', 'Order:'),
              mc('Which list is in order from least to greatest?', ['10, 12, 15, 18', '12, 10, 15, 18', '10, 15, 12, 18', '18, 15, 12, 10']),
              tf('These numbers are in order from least to greatest: 3, 6, 9, 8'),
              sa('Order from least to greatest.\n25, 20, 30, 10', 'Order:'),
              mc('Which number is least?', ['2', '12', '5', '9']),
          ]),
          B('The number halfway between two numbers', '5.NBT.B.7', [
              sa('Find the value.\n(4 + 5) ÷ 2', 'Value:'),
              sa('Find the value.\n(11 + 12) ÷ 2', 'Value:'),
              tf('(7 + 10) ÷ 2 = 8.5'),
              mc('(15 + 18) ÷ 2 = ?', ['16.5', '16', '33', '17.5']),
              sa('Find the value.\n(2.5 + 3.5) ÷ 2', 'Value:'),
          ]),
          B('Finding a difference', '2.NBT.B.5', [
              sa('Subtract.\n25 - 12', 'Difference:'),
              sa('Subtract.\n21 - 9', 'Difference:'),
              tf('30 - 14 = 16'),
              mc('18 - 10 = ?', ['8', '28', '9', '7']),
              sa('Subtract.\n40 - 23', 'Difference:'),
          ]),
      ],
      f1=B('Difference in centers as a multiple of the IQR', '7.SP.B.3', [
          sa('Two data sets have medians of 40 and 55. Each has an IQR of 5.\nThe difference in medians is how many times the IQR?', 'Times:'),
          mc('Two data sets have medians of 20 and 26. Each has an IQR of 3.\nHow many IQRs apart are the medians?', ['2', '6', '3', '9']),
          tf('Two data sets with medians that differ by less than one IQR probably overlap a lot.'),
          sa('Class A\'s median is 72 and Class B\'s median is 84. Each class has an IQR of 12.\nThe difference in medians is how many times the IQR?', 'Times:'),
          mc('Which pair of data sets has the LEAST overlap?', ['Medians 10 and 30, each IQR 4', 'Medians 10 and 12, each IQR 4', 'Medians 10 and 14, each IQR 8', 'Medians 10 and 11, each IQR 3']),
      ]),
      f2=B('Outliers and clusters in scatter plots', '8.SP.A.1', nearest=True, qs=[
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT4),
          mc('Which point would be an outlier if it were added to the scatter plot?', ['(7, 50)', '(7, 85)', '(3, 63)', '(5, 73)'], fig=POS),
          mc('Which describes the association in the scatter plot?', ['Negative linear', 'Positive linear', 'Nonlinear', 'No association'], fig=NEG),
          tf('The scatter plot has an outlier.', fig=NONLIN),
          tf('Every scatter plot has at least one outlier.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c MAD
    S('6.SP.B.5.c', 'Find the mean absolute deviation of a data set',
      main=[
          sa('Find the mean absolute deviation.\n2, 4, 6, 8, 10', 'MAD:'),
          mc('What is the mean absolute deviation?\n3, 3, 5, 7, 7', ['1.6', '2', '4', '0']),
          sa('Find the mean absolute deviation.\n5, 7, 8, 12', 'MAD:'),
          sa('Find the mean absolute deviation.\n6, 8, 10, 12, 14, 16', 'MAD:'),
          sa('Find the mean absolute deviation.\n20, 22, 25, 29', 'MAD:'),
      ],
      back=[
          B('Sharing a total equally (the mean)', '5.MD.B.2', [
              sa('Five jars hold 2, 4, 6, 8, and 10 cups of rice. The rice is shared equally among the jars.\nHow much is in each jar?', 'Cups:'),
              sa('Four friends have 3, 3, 7, and 7 marbles. They share the marbles equally.\nHow many marbles does each friend get?', 'Marbles:'),
              tf('Bags with 1, 5, and 6 pounds of flour are shared equally. Each bag then has 4 pounds.'),
              mc('Six students have 2, 3, 3, 4, 5, and 7 pencils. They share equally.\nHow many pencils does each student get?', ['4', '3', '24', '5']),
              sa('Three cups hold {1/2}, {1/2}, and 2 cups of water. The water is shared equally.\nHow much is in each cup?', 'Cups:'),
          ]),
          B('Distance as absolute value', '6.NS.C.7.c', [
              sa('Find the value.\n|2 - 6|', 'Value:'),
              sa('How far is 9 from 6 on a number line?', 'Distance:'),
              tf('|4 - 10| = 6'),
              mc('What is the distance between 3 and 8 on a number line?', ['5', '11', '-5', '24']),
              sa('Find the value.\n|10 - 6|', 'Value:'),
          ]),
          B('Dividing to find an average distance', '5.NBT.B.7', [
              sa('Divide.\n12 ÷ 5', 'Quotient:'),
              sa('Divide.\n8 ÷ 5', 'Quotient:'),
              tf('18 ÷ 6 = 3'),
              mc('10 ÷ 4 = ?', ['2.5', '2.4', '0.4', '40']),
              sa('Divide.\n9 ÷ 4', 'Quotient:'),
          ]),
      ],
      f1=B('Difference in means as a multiple of the MAD', '7.SP.B.3', [
          sa('Class A\'s mean is 72 and Class B\'s mean is 80. Each class has a MAD of 4.\nThe difference in means is how many times the MAD?', 'Times:'),
          mc('Two data sets have means of 15 and 21. Each has a MAD of 2.\nHow many MADs apart are the means?', ['3', '6', '2', '12']),
          tf('Two data sets have means that differ by 1 MAD. The data sets probably overlap a lot.'),
          sa('Two teams have mean heights of 150 cm and 162 cm. Each has a MAD of 4 cm.\nThe difference in means is how many times the MAD?', 'Times:'),
          mc('Which pair of data sets has the LEAST overlap?', ['Means 10 and 30, each MAD 2', 'Means 10 and 12, each MAD 2', 'Means 10 and 14, each MAD 4', 'Means 10 and 11, each MAD 3']),
      ]),
      f2=B('Judge model fit by distances from the line', '8.SP.A.2', [
          sa('Which point is farthest from the line?\nWrite its coordinates.', 'Point:', fig=FITOUT2),
          tf('The points are close to the line, so it is a good fit.', fig=FITD),
          tf('The line is a good fit for the data.', fig=BAD2),
          mc('Which line fits data better?', ['A line with points close to it on both sides', 'A line with all points far above it', 'A line with all points below it', 'A line that touches only one point']),
          sa('For the point (4, 10), the line gives y = 6.\nHow far is the point from the line, measured vertically?', 'Distance:', fig=FITOUT),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c pattern and deviations
    S('6.SP.B.5.c', 'Describe the overall pattern and striking deviations in the context of the data',
      main=[
          sa('The dot plot shows how many hours students slept last night.\nDescribe the overall pattern. Which value stands apart, and what might explain it?', ['Overall pattern:', 'Value that stands apart:'], fig=SLEEP),
          mc('The dot plot shows how long students take to walk home.\nWhich description best fits the data in context?',
             ['Most students take 5 to 10 minutes; a few who live farther away take 25 to 30 minutes.', 'All students take about the same amount of time.',
              'Most students take 25 to 30 minutes.', 'The times are spread evenly from 5 to 30 minutes.'], fig=WALKT),
          sa('The histogram shows the ages of people at a youth soccer game.\nDescribe the overall pattern. Which ages stand apart, and who might they be?', ['Overall pattern:', 'Ages that stand apart:'], fig=AGES),
          mc('The dot plot shows the scores on a class test.\nWhich statement describes a striking deviation in context?',
             ['One student scored 20, far below the others, who scored from 70 to 95.', 'The scores are spread evenly from 20 to 95.',
              'Most students scored below 50.', 'There are no unusual scores.'], fig=SCORES),
          tf('The daily high temperatures cluster from 60°F to 70°F, with one unusually hot day at 88°F.', fig=TEMPS),
      ],
      back=[
          B('Where data cluster and where there are gaps', '6.SP.A.2', [
              sa('Between which two values do most of the data cluster?', 'Between:', fig=SLEEP),
              tf('There is a gap in the data between 10 and 25 minutes.', fig=WALKT),
              mc('Where is there a gap in the data?', ['Between 20 and 70', 'Between 70 and 80', 'Between 85 and 95', 'There is no gap.'], fig=SCORES),
              sa('Between which two temperatures do most of the data cluster?', 'Between:', fig=TEMPS),
              tf('The data have no gaps.', fig=SYM),
          ]),
          B('Reading a dot plot in context', '4.MD.B.4', [
              sa('How many students slept 8 hours last night?', 'Students:', fig=SLEEP),
              sa('How many students take 7 minutes to walk home?', 'Students:', fig=WALKT),
              tf('Three students scored 85 on the test.', fig=SCORES),
              mc('How many days had a high temperature of 65°F?', ['4', '3', '5', '65'], fig=TEMPS),
              sa('What does each dot in the dot plot represent?', 'Each dot:', fig=SLEEP),
          ]),
          B('Greatest and least values', '2.NBT.A.4', [
              sa('What is the least value in the data?', 'Least:', fig=SCORES),
              sa('What is the greatest value in the data?', 'Greatest:', fig=TEMPS),
              tf('The greatest walking time is 30 minutes.', fig=WALKT),
              mc('Which number is least?', ['20', '70', '75', '95']),
              sa('What is the least number of hours of sleep shown?', 'Least:', fig=SLEEP),
          ]),
      ],
      f1=B('Compare the patterns of two distributions', '7.SP.B.3', [
          sa('Describe how the two distributions differ in context.', 'Comparison:', fig=CLASSES),
          mc('Which statement describes both gardens?', ['Both cluster tightly, and Garden B\'s plants are about 6 cm taller.', 'Garden A\'s plants are taller.',
                                                        'Garden B is much more spread out.', 'The gardens have the same center.'], fig=TEAMS),
          tf('Data set B is more spread out than data set A.', fig=SPREAD2),
          sa('Class A\'s quiz scores cluster from 7 to 9, with one score of 2. Class B\'s scores cluster from 4 to 6 with no unusual values.\nWhich class has a striking deviation?', 'Class:'),
          mc('Which statement about the middle halves of the two box plots is true?', ['They overlap from 70 to 76.', 'They do not overlap.', 'They overlap from 55 to 95.', 'They are the same.'], fig=TWOBOX),
      ]),
      f2=B('Describe patterns and deviations in scatter plots in context', '8.SP.A.1', [
          sa('The scatter plot shows savings over several weeks.\nDescribe the overall pattern and the point that does not fit.', ['Pattern:', 'Point that does not fit:'], fig=OUT3),
          mc('The scatter plot shows the age of cars and the number of repairs.\nWhich description fits the data in context?',
             ['Newer cars have few repairs and older cars have many repairs, forming two groups.', 'All cars have the same number of repairs.',
              'Older cars have fewer repairs.', 'There is no pattern.'], fig=CLUS),
          mc('Which statement describes the association in context?', ['As hours of TV increase, test scores tend to decrease.', 'As hours of TV increase, test scores tend to increase.',
                                                                         'Hours of TV and test scores are not related.', 'Every student scored the same.'], fig=NEG),
          sa('The scatter plot shows the price of an item and the number sold.\nWhich point does not fit the pattern? What might explain it?', ['Point:', 'Possible reason:'], fig=OUT4),
          tf('The plant grows faster each week, so the pattern in the scatter plot is nonlinear.', fig=NONLIN),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.d
    S('6.SP.B.5.d', 'Choose measures of center and variability based on the shape of the data',
      main=[
          mc('Data: 20, 22, 23, 25, 90\nWhich measure of center better describes a typical value?', ['Median', 'Mean']),
          mc('A data set is skewed right and has an outlier.\nWhich pair of measures best describes its center and spread?', ['Median and IQR', 'Mean and MAD', 'Mean and range', 'Mode and range']),
          mc('The dot plot is skewed right.\nWhich measure of center better describes the typical number of pets?', ['Median', 'Mean'], fig=SKEWR),
          mc('Salaries: $30,000; $32,000; $35,000; $38,000; $250,000\nWhich measure of center better describes a typical salary?', ['Median', 'Mean']),
          tf('Heights of 20 sixth graders are symmetric with no outliers, so the mean is a good measure of center.'),
      ],
      back=[
          B('Shape of a distribution', '6.SP.A.2', [
              mc('Which word describes the shape of the data?', ['Skewed left', 'Skewed right', 'Symmetric', 'Uniform'], fig=SKEWL),
              mc('Which word describes the shape of the data?', ['Symmetric', 'Skewed left', 'Skewed right', 'Uniform'], fig=SYM),
              tf('The data are skewed right.', fig=SKEWR),
              tf('A data set with most values on the left and a long tail to the right is skewed right.'),
              mc('Which value in the data set is an outlier?\n5, 6, 6, 7, 8, 30', ['30', '5', '6', '8']),
          ]),
          B('Computing the mean and median', '6.SP.B.5.c', [
              sa('Find the mean.\n2, 3, 3, 4, 8', 'Mean:'),
              sa('Find the median.\n2, 3, 3, 4, 8', 'Median:'),
              tf('The mean of 10, 20, 30 is 20.'),
              mc('What is the median of 1, 4, 6, 9?', ['5', '6', '4', '20']),
              sa('Find the mean.\n5, 5, 6, 8, 11', 'Mean:'),
          ]),
          B('Reading a dot plot', '4.MD.B.4', [
              sa('How many students scored 9 on the quiz?', 'Students:', fig=SKEWL),
              sa('What is the lowest quiz score shown?', 'Score:', fig=SKEWL),
              tf('Five students scored 8.', fig=SKEWL),
              mc('How many students took the quiz?', ['18', '15', '9', '6'], fig=SKEWL),
              sa('How many students had 0 pets?', 'Students:', fig=SKEWR),
          ]),
      ],
      f1=B('Compare populations using appropriate measures', '7.SP.B.4', [
          mc('Two random samples of house prices are both skewed right with outliers.\nWhich measures are best for comparing them?', ['Medians and IQRs', 'Means and MADs', 'Maximums', 'Minimums']),
          tf('When two samples are symmetric with no outliers, comparing their means is appropriate.'),
          sa('Sample A: median 30, IQR 6. Sample B: median 45, IQR 6.\nThe difference in medians is how many times the IQR?', 'Times:'),
          mc('Class A test scores have mean 78 and MAD 5. Class B test scores have mean 78 and MAD 12.\nWhich statement is true?', ['Class B\'s scores vary more.', 'Class A\'s scores vary more.', 'Class B scored higher.', 'Class A scored higher.']),
          sa('In random samples, the median commute is 25 minutes in Town X and 18 minutes in Town Y. Both have similar IQRs.\nIn which town are commutes typically longer?', 'Town:'),
      ]),
      f2=B('Judge how well a line fits the data', '8.SP.A.2', nearest=True, qs=[
          tf('The line is a good fit for the data.', fig=GOOD2),
          tf('The line is a good fit for the data.', fig=BAD3),
          mc('A line of best fit should show ___.', ['the overall trend of the data', 'only the largest value', 'only the smallest value', 'only the first point']),
          sa('Use the line of best fit to predict y when x = 2.', 'y =', fig=FITD),
          mc('Why should a scatter plot with no association NOT be modeled with a straight line?', ['There is no linear trend to model.', 'Lines must pass through the origin.', 'There are too many points.', 'The axes are labeled.'], fig=NONE),
      ])),
]
