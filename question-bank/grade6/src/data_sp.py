from qb import S, B, sa, mc, tf, nl, coord, table, hist, dot, box

SPORT = hist(['Soccer', 'Basketball', 'Baseball', 'Tennis'], [7, 5, 3, 1], gap=0.35, ymax=8, ystep=1,
             xlabel='Favorite sport', ylabel='Students', h=200)
PETS5 = hist(['Dogs', 'Cats', 'Birds', 'Fish'], [15, 10, 5, 20], gap=0.35, ymax=25, ystep=5,
             xlabel='Pets at a shelter', ylabel='Number', h=200)
BOOKS = hist(['0–9', '10–19', '20–29', '30–39'], [3, 7, 6, 2], ymax=8, ystep=1,
             xlabel='Books read this year', ylabel='Students', h=200)


def fracs(vmin, vmax, d, whole_mixed=True):
    out = {}
    n = round(vmin * d)
    while n <= round(vmax * d) + 1e-9:
        w, r = divmod(int(n), d)
        from math import gcd
        if r == 0:
            t = str(w)
        else:
            g = gcd(r, d)
            fr = '{%d/%d}' % (r // g, d // g)
            t = (str(w) if w else '') + fr
        out[n / d] = t
        n += 1
    return out


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

TEAMS = dict(k='vstack', h=215, figs=[
    dot(58, 72, {60: 1, 61: 2, 62: 3, 63: 2, 64: 1}, lstep=2, title='Team A heights (inches)'),
    dot(58, 72, {66: 1, 67: 2, 68: 3, 69: 2, 70: 1}, lstep=2, title='Team B heights (inches)')])
TWOBOX = box(50, 100, None, step=5, lstep=10, boxes=[('Class A', (60, 70, 78, 85, 95)), ('Class B', (55, 62, 70, 76, 90))],
             xlabel='Test scores')
BOX1 = box(10, 40, (12, 18, 24, 30, 40), step=2, lstep=10)
BOX51 = box(0, 30, (4, 9, 14, 21, 28), step=2, lstep=10)

PETTABLE = table([['', 'Has a pet', 'No pet', 'Total'], ['Grade 7', '18', '12', '30'], ['Grade 8', '20', '10', '30'],
                  ['Total', '38', '22', '60']], header='both')
RIDETABLE = table([['', 'Walk', 'Bus', 'Total'], ['Boys', '12', '?', '30'], ['Girls', '15', '10', '25'],
                   ['Total', '27', '28', '55']], header='both')
MUSIC = table([['', 'Plays sports', 'No sports', 'Total'], ['Plays an instrument', '14', '6', '20'],
               ['No instrument', '16', '4', '20'], ['Total', '30', '10', '40']], header='both')


def sc(pts, xlabel, ylabel, x=(0, 9), y=(0, 10), xstep=1, ystep=1, lines=()):
    return coord(x=x, y=y, xstep=xstep, ystep=ystep, square=False, axisnames=False, xlabel=xlabel, ylabel=ylabel,
                 pts=[(a, b) for a, b in pts], lines=list(lines))


POS = sc([(1, 55), (2, 60), (3, 62), (4, 70), (5, 74), (6, 80), (7, 83), (8, 90)], 'Hours studied', 'Test score', y=(50, 100), ystep=10)
NEG = sc([(1, 92), (2, 88), (3, 85), (4, 80), (5, 74), (6, 72), (7, 65), (8, 60)], 'Hours of TV per day', 'Test score', y=(50, 100), ystep=10)
NONE = sc([(1, 6), (2, 2), (3, 8), (4, 4), (5, 7), (6, 3), (7, 5), (8, 8), (2, 5), (6, 6)], 'Shoe size', 'Pets owned')
NONLIN = sc([(1, 1), (2, 1.5), (3, 2.5), (4, 4), (5, 6), (6, 8.5)], 'Week', 'Plant height (cm)', x=(0, 7))
OUT = sc([(1, 55), (2, 61), (3, 64), (4, 70), (5, 73), (6, 79), (7, 55), (8, 89)], 'Hours studied', 'Test score', y=(50, 100), ystep=10)
CLUS = sc([(1, 2), (1.5, 2.5), (2, 2), (2, 3), (6, 7), (6.5, 8), (7, 7), (7, 8.5), (6.5, 7.5)], 'Age of car (years)', 'Repairs', x=(0, 9))
FIT = sc([(1, 3), (2, 4.5), (3, 5), (4, 6), (5, 7.5), (6, 8), (7, 9.5)], 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 2), (8, 10))])
BADFIT = sc([(1, 3), (2, 4.5), (3, 5), (4, 6), (5, 7.5), (6, 8), (7, 9.5)], 'x', 'y', x=(0, 8), y=(0, 12), lines=[((0, 0), (8, 2))])

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
          sa('Rewrite this question so that it is a statistical question.\n"How many books did Mia read this year?"', 'Question:'),
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
      f2=B('Scatter plots of bivariate data', '8.SP.A.1', [
          mc('What type of association does the scatter plot show?', ['Positive linear', 'Negative linear', 'No association', 'Nonlinear'], fig=POS),
          mc('What type of association does the scatter plot show?', ['Negative linear', 'Positive linear', 'No association', 'Nonlinear'], fig=NEG),
          tf('A scatter plot shows data about two variables for each person or object.'),
          mc('Which question would be best answered with a scatter plot?',
             ['Is there a relationship between height and arm span?', 'What is the most common eye color?',
              'How many students ride the bus?', 'What is the median age in the class?']),
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.2
    S('6.SP.A.2', 'Describe a distribution by its center, spread, and shape',
      main=[
          mc('Which word best describes the shape of the data?', ['Symmetric', 'Skewed right', 'Skewed left', 'Uniform'], fig=SYM),
          mc('Which word best describes the shape of the data?', ['Skewed right', 'Symmetric', 'Skewed left', 'Uniform'], fig=SKEWR),
          sa('What is the range of the data?', 'Range:', fig=RANGE),
          mc('Where do most of the data values cluster?', ['Between 7 and 9', 'Between 0 and 2', 'Between 3 and 5', 'At 10'], fig=CLUST),
          tf('The distribution of a data set can be described by its center, its spread, and its overall shape.'),
      ],
      back=[
          B('Line plots with fractional measurements', '5.MD.B.2', [
              sa('The line plot shows the liquid in some beakers.\nHow many beakers hold {1/4} liter?', 'Beakers:', fig=BEAKERS),
              sa('The line plot shows the liquid in some beakers.\nHow much liquid is in all of the {1/2}-liter beakers together?', 'Liters:', fig=BEAKERS),
              tf('There are 8 beakers in all.', fig=BEAKERS),
              mc('The liquid in the {3/8}-liter beakers is poured together.\nHow much liquid is there?', ['{3/4} liter', '{3/8} liter', '{3/16} liter', '1 liter'], fig=BEAKERS),
              sa('How much more liquid is in a {1/2}-liter beaker than in the {1/8}-liter beaker?', 'Liters:', fig=BEAKERS),
          ]),
          B('Finding a difference', '2.NBT.B.5', [
              sa('The greatest value is 47. The least value is 18.\nWhat is the difference?', 'Difference:'),
              sa('Subtract.\n83 - 29', 'Difference:'),
              tf('62 - 35 = 27'),
              mc('91 - 46 = ?', ['45', '55', '47', '137']),
              sa('What is the difference between 100 and 64?', 'Difference:'),
          ]),
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n42, 24, 36, 18', 'Order:'),
              mc('Which number is greatest?', ['350', '305', '299', '53']),
              tf('These numbers are in order from least to greatest: 12, 21, 19, 30'),
              sa('Order from least to greatest.\n105, 150, 115', 'Order:'),
              mc('Which number is least?', ['89', '98', '91', '100']),
          ]),
      ],
      f1=B('Compare two distributions visually', '7.SP.B.3', [
          sa('About how many inches greater is the center of Team B\'s heights than the center of Team A\'s heights?', 'Inches:', fig=TEAMS),
          tf('The two distributions have about the same spread.', fig=TEAMS),
          mc('Which statement is true?', ['Team B\'s heights are typically greater.', 'Team A\'s heights are typically greater.',
                                          'The teams have the same center.', 'The distributions overlap a lot.'], fig=TEAMS),
          sa('Class A\'s mean score is 60 and Class B\'s mean score is 66. Each class has a mean absolute deviation of 3.\nThe difference in means is how many times the MAD?', 'Times:'),
          mc('Two classes have mean scores of 78 and 84. Each has a MAD of 6.\nThe difference in means is how many times the MAD?', ['1', '2', '6', '0.5']),
      ]),
      f2=B('Patterns in scatter plots', '8.SP.A.1', [
          mc('Which describes the pattern in the scatter plot?', ['Two clusters', 'A strong negative association', 'No pattern', 'A single outlier'], fig=CLUS),
          tf('The scatter plot shows a negative association.', fig=NEG),
          mc('Which describes the association in the scatter plot?', ['Nonlinear', 'Negative linear', 'No association', 'Constant'], fig=NONLIN),
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT),
          mc('In the scatter plot, as x increases, y tends to ___.', ['increase', 'decrease', 'stay the same', 'equal x'], fig=POS),
      ])),

    # ------------------------------------------------------------------ 6.SP.A.3
    S('6.SP.A.3', 'A measure of center vs. a measure of variation',
      main=[
          mc('Which measure describes the center of a data set?', ['Median', 'Range', 'Interquartile range', 'Mean absolute deviation']),
          mc('Which measure describes how much the values in a data set vary?', ['Interquartile range', 'Mean', 'Median', 'The middle value']),
          tf('A measure of center summarizes all of the values in a data set with a single number.'),
          tf('A measure of variation describes how the values in a data set vary with a single number.'),
          mc('A teacher wants one number that describes a typical test score.\nWhich measure should she use?', ['The mean', 'The range', 'The interquartile range', 'The mean absolute deviation']),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('The line plot shows ribbon lengths.\nHow many ribbons are 1 foot long?', 'Ribbons:', fig=RIBBONS),
              sa('The line plot shows ribbon lengths.\nHow many ribbons are there in all?', 'Ribbons:', fig=RIBBONS),
              tf('Two ribbons are {1/2} foot long.', fig=RIBBONS),
              mc('Which ribbon length is most common?', ['1 foot', '{1/2} foot', '1{1/2} feet', '2 feet'], fig=RIBBONS),
              sa('What is the total length of the 1{1/2}-foot ribbons?', 'Total length:', fig=RIBBONS),
          ]),
          B('Sharing a total equally', '5.MD.B.2', [
              sa('Three friends have 4, 6, and 8 stickers. They share all of the stickers equally.\nHow many stickers does each friend get?', 'Stickers:'),
              sa('Four jars hold 2, 3, 5, and 6 liters of water. The water is shared equally among the jars.\nHow much water is in each jar?', 'Liters:'),
              tf('Cups holding 1, 2, and 3 liters are shared equally. Each cup then holds 2 liters.'),
              mc('Five friends collected 3, 5, 6, 7, and 9 cans. They share the cans equally.\nHow many cans does each friend get?', ['6', '5', '30', '7']),
              sa('Two bottles hold {1/4} liter and {3/4} liter. The juice is shared equally between the bottles.\nHow much juice is in each bottle?', 'Liters:'),
          ]),
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n56, 65, 38, 83', 'Order:'),
              mc('Which number is greatest?', ['720', '702', '270', '207']),
              tf('These numbers are in order from least to greatest: 14, 41, 44, 114'),
              sa('Order from least to greatest.\n209, 290, 92', 'Order:'),
              mc('Which number is least?', ['147', '174', '417', '471']),
          ]),
      ],
      f1=B('Compare populations using center and variability', '7.SP.B.4', [
          mc('Class A has a median score of 82 and an IQR of 10. Class B has a median score of 75 and an IQR of 10.\nWhich statement is true?',
             ['Class A typically scored higher.', 'Class B typically scored higher.', 'The classes scored the same.', 'Class A\'s scores vary more.']),
          sa('Random samples: Town A has a mean age of 34 years. Town B has a mean age of 42 years.\nWhat is the difference in mean ages?', 'Difference:'),
          tf('Two samples have the same median. The sample with the greater IQR has more variability.'),
          mc('Which measure is best for comparing the variability of two samples?', ['IQR', 'Median', 'Mean', 'Sample size']),
          sa('In random samples, 7th graders sleep a median of 8 hours, and 6th graders sleep a median of 9 hours.\nWhich group typically sleeps more?', 'Group:'),
      ]),
      f2=B('Lines of best fit', '8.SP.A.2', [
          tf('A line of best fit usually has about the same number of points above it as below it.'),
          sa('Use the line of best fit to predict y when x = 6.', 'y =', fig=FIT),
          mc('Which statement about a line of best fit is true?',
             ['It shows the overall trend of the data.', 'It must pass through every point.', 'It must pass through the origin.', 'It is always horizontal.']),
          tf('The line is a good fit for the data.', fig=BADFIT),
          sa('Use the line of best fit to predict y when x = 2.', 'y =', fig=FIT),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.4 dot plots and histograms
    S('6.SP.B.4', 'Display data in dot plots and histograms',
      main=[
          sa('The histogram shows how many books students read.\nHow many students read 10–19 books?', 'Students:', fig=BOOKS),
          mc('Which data set matches the dot plot?', ['1, 2, 2, 3, 5', '1, 2, 3, 5', '1, 1, 2, 3, 5', '1, 2, 2, 3, 3'], fig=dot(0, 6, {1: 1, 2: 2, 3: 1, 5: 1})),
          sa('Data: 2, 4, 4, 5, 7, 7, 7, 9\nMake a dot plot of the data on the number line. How many dots will be above 7?', 'Dots:', fig=nl(0, 10, 1)),
          mc('Which interval has the most students?', ['10–19', '0–9', '20–29', '30–39'], fig=BOOKS),
          tf('6 students read 20–29 books.', fig=BOOKS),
      ],
      back=[
          B('Making a line plot', '4.MD.B.4', [
              sa('Lengths (inches): {1/2}, 1, 1, 1{1/2}, 1, {1/2}\nIn a line plot of these lengths, how many X\'s go above 1?', 'X\'s:'),
              tf('In a line plot of 2, 2{1/2}, 2{1/2}, 3, there are two X\'s above 2{1/2}.'),
              mc('Which number line would you use to make a line plot of these lengths?\n{1/4}, {1/2}, {3/4}, {1/2}',
                 ['A number line from 0 to 1 marked in fourths', 'A number line from 0 to 10 marked in ones', 'A number line from 0 to 100 marked in tens', 'A number line from 1 to 2 marked in halves']),
              sa('Lengths (feet): 3, 3{1/2}, 4, 3{1/2}, 3{1/2}\nWhich length gets the most X\'s?', 'Length:'),
              tf('A line plot shows each data value as a mark above a number line.'),
          ]),
          B('Scaled bar graphs', '3.MD.B.3', [
              sa('The graph shows the pets at a shelter.\nHow many cats are there?', 'Cats:', fig=PETS5),
              sa('The graph shows the pets at a shelter.\nHow many more fish than birds are there?', 'Number:', fig=PETS5),
              tf('Each grid line on the graph stands for 5 pets.', fig=PETS5),
              mc('Which type of pet has 15 at the shelter?', ['Dogs', 'Cats', 'Birds', 'Fish'], fig=PETS5),
              sa('The graph shows the pets at a shelter.\nHow many dogs and cats are there together?', 'Number:', fig=PETS5),
          ]),
          B('Placing numbers in intervals', '2.NBT.A.4', [
              mc('Which interval contains 17?', ['10–19', '0–9', '20–29', '30–39']),
              tf('25 is in the interval 20–29.'),
              sa('Data: 3, 12, 15, 18, 22\nHow many of the numbers are in the interval 10–19?', 'Numbers:'),
              mc('Which number is in the interval 30–39?', ['34', '29', '40', '3']),
              tf('19 is in the interval 20–29.'),
          ]),
      ],
      f1=B('Compare two dot plots', '7.SP.B.3', [
          sa('About how many inches greater is the center of Team B\'s heights?', 'Inches:', fig=TEAMS),
          tf('The dot plots show that the two teams have about the same variability.', fig=TEAMS),
          mc('Which statement is true?', ['The distributions do not overlap.', 'Team A is typically taller.', 'Team B has more variability.', 'The medians are equal.'], fig=TEAMS),
          sa('Team A\'s mean height is 62 in. Team B\'s mean height is 68 in. Each team\'s MAD is about 1 in.\nThe difference in means is about how many times the MAD?', 'Times:'),
          tf('Two data sets with means of 50 and 56 and MADs of 3 have means that differ by 2 MADs.'),
      ]),
      f2=B('Construct a scatter plot', '8.SP.A.1', [
          sa('The table shows hours studied and test scores.\nWhich ordered pair would be plotted for Student C?', 'Ordered pair:',
             fig=table([['Student', 'A', 'B', 'C', 'D'], ['Hours', '1', '3', '4', '6'], ['Score', '62', '70', '78', '88']], header='both')),
          tf('To make a scatter plot of height and arm span, each person is shown as one point.'),
          mc('A scatter plot shows age on the x-axis and height on the y-axis.\nA 10-year-old is 54 inches tall. Which point shows this person?', ['(10, 54)', '(54, 10)', '(10, 10)', '(54, 54)']),
          sa('The table shows hours studied and test scores.\nWhich ordered pair would be plotted for Student D?', 'Ordered pair:',
             fig=table([['Student', 'A', 'B', 'C', 'D'], ['Hours', '1', '3', '4', '6'], ['Score', '62', '70', '78', '88']], header='both')),
          mc('The ordered pairs (1, 62), (3, 70), (4, 78), and (6, 88) are plotted.\nWhat association will the scatter plot show?', ['Positive', 'Negative', 'No association']),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.4 box plots
    S('6.SP.B.4', 'Display data in box plots',
      main=[
          sa('What is the median of the data shown in the box plot?', 'Median:', fig=BOX1),
          sa('What is the interquartile range of the data shown in the box plot?', 'IQR:', fig=BOX1),
          mc('What is the range of the data shown in the box plot?', ['28', '12', '24', '40'], fig=BOX1),
          sa('Data: 3, 5, 7, 8, 10, 12, 15\nFind the five-number summary for a box plot.', ['Minimum:', 'Q1:', 'Median:', 'Q3:', 'Maximum:']),
          tf('In the box plot, the maximum value is 40.', fig=BOX1),
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
      ],
      f1=B('Compare populations with box plots', '7.SP.B.4', [
          mc('Which class has the greater median score?', ['Class A', 'Class B', 'They are the same.'], fig=TWOBOX),
          mc('By how many points do the medians differ?', ['8', '5', '15', '3'], fig=TWOBOX),
          sa('What is the interquartile range of Class A\'s scores?', 'IQR:', fig=TWOBOX),
          tf('At least half of Class A scored 78 or higher.', fig=TWOBOX),
          sa('Which class had the highest single score?', 'Class:', fig=TWOBOX),
      ]),
      f2=B('Two-way tables', '8.SP.A.4', [
          sa('The table shows survey results.\nHow many 8th graders have a pet?', 'Students:', fig=PETTABLE),
          sa('What fraction of the 7th graders have a pet?', 'Fraction:', fig=PETTABLE),
          mc('What is the relative frequency of 8th graders who have no pet?', ['{1/3}', '{1/2}', '{10/22}', '{1/6}'], fig=PETTABLE),
          tf('60 students were surveyed in all.', fig=PETTABLE),
          sa('What number belongs in place of the question mark?', '? =', fig=RIDETABLE),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.a
    S('6.SP.B.5.a', 'Report the number of observations',
      main=[
          sa('The dot plot shows how many books students borrowed.\nHow many observations are in the data set?', 'Observations:', fig=OBS),
          sa('How many students are represented in the histogram?', 'Students:', fig=BOOKS),
          sa('The table shows how many siblings students have.\nHow many observations are in the data set?', 'Observations:',
             fig=table([['Siblings', '0', '1', '2', '3'], ['Students', '4', '9', '6', '2']])),
          tf('A box plot shows how many observations are in a data set.'),
          sa('Data: 12, 15, 9, 15, 20, 11, 13, 18, 15, 10\nHow many observations are in the data set?', 'Observations:'),
      ],
      back=[
          B('Reading a line plot', '4.MD.B.4', [
              sa('The line plot shows pencil lengths.\nHow many pencils are 4 inches long?', 'Pencils:', fig=PENCILS),
              sa('The line plot shows pencil lengths.\nHow many pencils were measured?', 'Pencils:', fig=PENCILS),
              tf('Three pencils are 3{1/2} inches long.', fig=PENCILS),
              mc('How many pencils are longer than 4 inches?', ['3', '4', '2', '7'], fig=PENCILS),
              sa('What is the difference between the longest and the shortest pencil?', 'Difference:', fig=PENCILS),
          ]),
          B('Totals from a bar graph', '3.MD.B.3', [
              sa('How many students answered the survey?', 'Students:', fig=SPORT),
              sa('How many students chose soccer or tennis?', 'Students:', fig=SPORT),
              tf('12 students chose soccer or basketball.', fig=SPORT),
              mc('How many students did NOT choose soccer?', ['9', '7', '16', '5'], fig=SPORT),
              sa('How many pets are at the shelter in all?', 'Pets:', fig=PETS5),
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
          sa('Two random samples of 20 students each found 12 and 14 students who like pizza best.\nWhat is the mean number from the two samples?', 'Mean:'),
      ]),
      f2=B('Totals in two-way tables', '8.SP.A.4', [
          sa('How many students were surveyed in all?', 'Students:', fig=MUSIC),
          sa('How many students play sports?', 'Students:', fig=MUSIC),
          tf('14 students play an instrument and play sports.', fig=MUSIC),
          mc('How many students play an instrument but do NOT play sports?', ['6', '14', '20', '4'], fig=MUSIC),
          sa('What number belongs in place of the question mark?', '? =', fig=RIDETABLE),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.b
    S('6.SP.B.5.b', 'Describe the attribute measured and its units',
      main=[
          sa('A data set lists the heights of 25 plants in centimeters.\nWhat attribute is being measured, and in what unit?', ['Attribute:', 'Unit:']),
          mc('Which unit would be used to record the time students spend on homework?', ['Minutes', 'Inches', 'Pounds', 'Degrees']),
          tf('In a data set of "number of pets for each student," each observation is a count, not a length.'),
          mc('The dot plot shows how far students jumped.\nWhich unit is most likely?', ['Inches', 'Miles', 'Pounds', 'Seconds'], fig=JUMP),
          sa('A survey records how each student gets to school: bus, car, or walk.\nIs this data numerical or categorical?', 'Answer:'),
      ],
      back=[
          B('Choosing measurement units', '4.MD.A.1', [
              mc('Which unit is best for measuring the length of a pencil?', ['Centimeters', 'Kilometers', 'Meters', 'Kilograms']),
              tf('A kilogram is heavier than a gram.'),
              mc('Which unit measures liquid volume?', ['Liters', 'Grams', 'Meters', 'Seconds']),
              sa('Name one unit used to measure time.', 'Unit:'),
              tf('An inch is longer than a foot.'),
          ]),
          B('Categories in a bar graph', '3.MD.B.3', [
              sa('How many categories does the graph show?', 'Categories:', fig=SPORT),
              mc('What does the height of each bar show?', ['The number of students', 'The number of sports', 'The score of a game', 'The length of a game'], fig=SPORT),
              tf('"Tennis" is one of the categories in the graph.', fig=SPORT),
              mc('Which is a category in the graph?', ['Birds', 'Horses', 'Soccer', '25'], fig=PETS5),
              sa('What is being counted in the graph?', 'Answer:', fig=PETS5),
          ]),
      ],
      f1=B('How data are collected: sampling methods', '7.SP.A.1', [
          mc('Which method gives a random sample of the students in a school?',
             ['Draw names from a hat that holds every student\'s name', 'Ask your friends', 'Ask the students in the library', 'Ask the first 20 students to arrive']),
          tf('Surveying people who walk out of a gym is a good way to learn how often all people in a town exercise.'),
          sa('A town wants to know how residents feel about a new library.\nDescribe a way to choose a random sample.', 'Method:'),
          mc('Which sample is most likely to be biased?', ['Asking only people at a dog park whether they like dogs', 'Choosing 50 residents at random from a town list',
                                                           'Picking every 10th name from a school list', 'Drawing 30 names from a hat of all members']),
          tf('Every member of a population has an equal chance of being chosen in a random sample.'),
      ]),
      f2=B('Categorical data in two-way tables', '8.SP.A.4', [
          mc('Which pair of variables would be shown in a two-way table?', ['Grade level and whether a student has a pet', 'Height and weight', 'Age and arm span', 'Hours slept and test score']),
          sa('What fraction of students who play an instrument also play sports?', 'Fraction:', fig=MUSIC),
          tf('The data in a two-way table are categorical.'),
          mc('What is the relative frequency of students who play sports?', ['{3/4}', '{1/4}', '{1/2}', '{3/10}'], fig=MUSIC),
          sa('How many 7th graders do NOT have a pet?', 'Students:', fig=PETTABLE),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c mean and median
    S('6.SP.B.5.c', 'Find the mean and median of a data set',
      main=[
          sa('Find the mean of the data.\n4, 7, 9, 10, 15', 'Mean:'),
          sa('Find the median of the data.\n12, 5, 9, 20, 7, 14', 'Median:'),
          sa('Five test scores are 82, 90, 75, 88, and 95.\nWhat is the mean score?', 'Mean:'),
          tf('The median of 3, 8, 8, 10, 21 is 8.'),
          mc('Heights (in inches): 58, 60, 61, 63, 63\nWhat is the median height?', ['61', '63', '60', '61.5']),
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
              sa('Divide.\n45 ÷ 5', 'Quotient:'),
              tf('108 ÷ 4 = 27'),
              mc('252 ÷ 6 = ?', ['42', '41', '48', '36']),
              sa('Divide.\n315 ÷ 7', 'Quotient:'),
          ]),
          B('Ordering numbers', '2.NBT.A.4', [
              sa('Order from least to greatest.\n12, 5, 9, 20, 7, 14', 'Order:'),
              mc('Which list is in order from least to greatest?', ['58, 60, 61, 63', '60, 58, 61, 63', '58, 61, 60, 63', '63, 61, 60, 58']),
              tf('These numbers are in order from least to greatest: 75, 82, 88, 90, 95'),
              sa('Order from least to greatest.\n47, 74, 44, 77', 'Order:'),
              mc('Which number is in the middle when 3, 9, 6 are put in order?', ['6', '3', '9', '18']),
          ]),
          B('The number halfway between two numbers', '5.NBT.B.7', [
              sa('Find the value.\n(9 + 12) ÷ 2', 'Value:'),
              sa('Find the value.\n(14 + 17) ÷ 2', 'Value:'),
              tf('(6 + 9) ÷ 2 = 7.5'),
              mc('(20 + 25) ÷ 2 = ?', ['22.5', '22', '45', '23.5']),
              sa('Find the value.\n(3.5 + 4.5) ÷ 2', 'Value:'),
          ]),
      ],
      f1=B('Compare populations using means and medians', '7.SP.B.4', [
          sa('A random sample of 6th graders has a mean height of 58 in. A random sample of 8th graders has a mean height of 64 in.\nHow much greater is the 8th graders\' mean?', 'Difference:'),
          mc('Sample A has a median of 12 and Sample B has a median of 15. The samples have similar variability.\nWhich conclusion is best?',
             ['Values in population B tend to be greater.', 'Values in population A tend to be greater.', 'The populations are the same.', 'No conclusion is possible.']),
          tf('To compare two populations, you can compare the means of random samples from each population.'),
          sa('Store A sample: daily sales mean $520. Store B sample: daily sales mean $610.\nWhich store typically has greater daily sales?', 'Store:'),
          mc('Two random samples of plant heights have means of 24 cm and 30 cm. Each has a MAD of 3 cm.\nHow many MADs apart are the means?', ['2', '6', '3', '1']),
      ]),
      f2=B('Use a linear model to make predictions', '8.SP.A.3', [
          sa('The equation y = 2.5x + 40 models test score y after x hours of study.\nPredict the score for 8 hours of study.', 'Score:'),
          sa('The equation y = 2.5x + 40 models test score y after x hours of study.\nWhat does the slope 2.5 mean?', 'Meaning:'),
          mc('The model y = 3x + 12 gives a plant\'s height y (cm) after x weeks.\nWhat does 12 represent?', ['The height at week 0', 'The growth per week', 'The number of weeks', 'The height after 12 weeks']),
          tf('In the model y = -0.5x + 30, y decreases by 0.5 for each 1-unit increase in x.'),
          sa('The model y = 15x + 100 gives the cost y of x tickets.\nPredict the cost of 20 tickets.', 'Cost:'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.c IQR and MAD
    S('6.SP.B.5.c', 'Find the interquartile range and mean absolute deviation',
      main=[
          sa('Find the interquartile range of the data.\n2, 4, 5, 7, 9, 11, 12, 15', 'IQR:'),
          sa('Find the mean absolute deviation of the data.\n2, 4, 6, 8, 10', 'MAD:'),
          mc('What is the mean absolute deviation of the data?\n3, 3, 5, 7, 7', ['1.6', '2', '4', '0']),
          sa('What is the interquartile range of the data shown in the box plot?', 'IQR:', fig=BOX51),
          tf('A greater mean absolute deviation means the data values are more spread out from the mean.'),
      ],
      back=[
          B('The number halfway between two numbers', '5.NBT.B.7', [
              sa('Find the value.\n(4 + 5) ÷ 2', 'Value:'),
              sa('Find the value.\n(11 + 12) ÷ 2', 'Value:'),
              tf('(7 + 10) ÷ 2 = 8.5'),
              mc('(15 + 18) ÷ 2 = ?', ['16.5', '16', '33', '17.5']),
              sa('Find the value.\n(2.5 + 3.5) ÷ 2', 'Value:'),
          ]),
          B('Sharing a total equally', '5.MD.B.2', [
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
      ],
      f1=B('Difference in centers as a multiple of variability', '7.SP.B.3', [
          sa('Class A\'s mean is 72 and Class B\'s mean is 80. Each class has a MAD of 4.\nThe difference in means is how many times the MAD?', 'Times:'),
          mc('Two data sets have means of 15 and 21. Each has a MAD of 2.\nHow many MADs apart are the means?', ['3', '6', '2', '12']),
          tf('Two data sets have means that differ by 1 MAD. The data sets probably overlap a lot.'),
          sa('Two data sets have medians of 40 and 55. Each has an IQR of 5.\nThe difference in medians is how many times the IQR?', 'Times:'),
          mc('Which pair of data sets has the LEAST overlap?', ['Means 10 and 30, each MAD 2', 'Means 10 and 12, each MAD 2', 'Means 10 and 14, each MAD 4', 'Means 10 and 11, each MAD 3']),
      ]),
      f2=B('Clusters and outliers in scatter plots', '8.SP.A.1', [
          sa('Which point is an outlier?\nWrite its coordinates.', 'Outlier:', fig=OUT),
          mc('Which describes the scatter plot?', ['Two clusters', 'A strong positive association', 'No pattern', 'A single outlier'], fig=CLUS),
          tf('The scatter plot shows no association.', fig=NONE),
          mc('Which describes the association in the scatter plot?', ['Negative linear', 'Positive linear', 'Nonlinear', 'No association'], fig=NEG),
          tf('An outlier in a scatter plot is a point that is far from the overall pattern.'),
      ])),

    # ------------------------------------------------------------------ 6.SP.B.5.d
    S('6.SP.B.5.d', 'Choose measures of center and variability based on the shape of the data',
      main=[
          mc('Data: 20, 22, 23, 25, 90\nWhich measure of center best describes a typical value?', ['Median', 'Mean']),
          tf('For a symmetric distribution with no outliers, the mean and the median are about the same.'),
          mc('A data set is skewed right and has an outlier.\nWhich pair of measures best describes its center and spread?', ['Median and IQR', 'Mean and MAD', 'Mean and range', 'Median and MAD']),
          sa('Salaries: $30,000; $32,000; $35,000; $38,000; $250,000\nFind the mean and the median. Which better describes a typical salary?', ['Mean:', 'Median:', 'Better measure:']),
          mc('Data: 2, 3, 3, 4, 40\nWhy is the median a better measure of center than the mean?',
             ['The outlier 40 pulls the mean up.', 'The median is always larger.', 'The mean ignores 40.', 'There is no median.']),
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
          sa('Sample A: median 42, IQR 8. Sample B: median 50, IQR 8.\nThe difference in medians is how many times the IQR?', 'Times:'),
          mc('Class A test scores have mean 78 and MAD 5. Class B test scores have mean 78 and MAD 12.\nWhich statement is true?',
             ['Class B\'s scores vary more.', 'Class A\'s scores vary more.', 'Class B scored higher.', 'Class A scored higher.']),
          sa('Sample of commute times, Town X: median 25 min. Town Y: median 18 min. Both have similar IQRs.\nIn which town are commutes typically longer?', 'Town:'),
      ]),
      f2=B('Judge how well a line fits the data', '8.SP.A.2', [
          tf('The line is a good fit for the data.', fig=FIT),
          tf('The line is a good fit for the data.', fig=BADFIT),
          mc('Which is a sign of a good line of best fit?', ['Points are close to the line on both sides.', 'All points are above the line.', 'All points are below the line.', 'The line goes through only one point.']),
          sa('Use the line of best fit to predict y when x = 4.', 'y =', fig=FIT),
          mc('Why should a scatter plot with no association NOT be modeled with a straight line?', ['There is no linear trend to model.', 'Lines must pass through the origin.', 'There are too many points.', 'The axes are labeled.'], fig=NONE),
      ])),
]
