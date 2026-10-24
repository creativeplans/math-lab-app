"""S-ID.A.1-3: dot plots, histograms, box plots, comparing center and spread, interpreting differences, outliers (sets 1-7)."""
from collections import Counter

from qb import S, B, sa, mc, tf, dot, box, hist
from common import (why, n, d1, mean, median, five, fences, sd_pop, sd_samp, dlist, pickfig, QRULE, OUTRULE, TECH)
from datasets import D

EP = ' Each bin includes its left endpoint and excludes its right endpoint.'
POP = ' Use the population standard deviation (divide by n).'


def counts(xs):
    return Counter(xs)


def dotf(xs, lo, hi, label, step=1, **kw):
    c = Counter(xs) if not isinstance(xs, dict) else Counter(xs)
    desc = 'Dot plot of %s from %s to %s: ' % (label.lower(), n(lo), n(hi)) + ', '.join(
        '%s dot%s at %s' % (c[v], '' if c[v] == 1 else 's', n(v)) for v in sorted(c) if c[v])
    return dot(lo, hi, dict(c), step=step, xlabel=label, desc=desc + '.', **kw)


def bincount(xs, edges):
    """Counts per bin [edges[i], edges[i+1]) (left endpoint included, right excluded)."""
    return [sum(1 for x in xs if edges[i] <= x < edges[i + 1]) for i in range(len(edges) - 1)]


def bincount_right(xs, edges):
    """The wrong rule (right endpoint included), used for distractors."""
    return [sum(1 for x in xs if edges[i] < x <= edges[i + 1]) for i in range(len(edges) - 1)]


def histf(edges, cnts, label, ystep=1, ymax=None, **kw):
    bins = ['%s–%s' % (n(edges[i]), n(edges[i + 1])) for i in range(len(edges) - 1)]
    desc = 'Histogram of %s with bins ' % label.lower() + ', '.join('%s: %d' % (b, k) for b, k in zip(bins, cnts)) + '.'
    return hist(bins, cnts, xlabel=label, ylabel='Frequency', ystep=ystep, ymax=ymax or max(cnts) + 1, desc=desc, **kw)


def boxf(fv, lo, hi, label, step=1, outl=(), **kw):
    a, q1, md, q3, b = [float(v) for v in fv]
    desc = 'Box plot of %s: minimum %s, Q1 %s, median %s, Q3 %s, maximum %s' % (label.lower(), n(a), n(q1), n(md), n(q3), n(b))
    if outl:
        desc += '; outliers plotted as separate points at %s, with the whiskers ending at the most extreme values that are not outliers' % dlist(outl)
        return box(lo, hi, None, step=step, boxes=[(None, (a, q1, md, q3, b), tuple(outl))], xlabel=label, desc=desc + '.', **kw)
    return box(lo, hi, (a, q1, md, q3, b), step=step, xlabel=label, desc=desc + '.', **kw)


def boxes2(names, fvs, lo, hi, label, step=1, **kw):
    desc = 'Two box plots of %s on one scale. ' % label.lower() + ' '.join(
        '%s: minimum %s, Q1 %s, median %s, Q3 %s, maximum %s.' % ((nm,) + tuple(n(float(v)) for v in fv)) for nm, fv in zip(names, fvs))
    return box(lo, hi, None, step=step, boxes=[(nm, tuple(float(v) for v in fv)) for nm, fv in zip(names, fvs)], xlabel=label,
               desc=desc, **kw)


def fvk(xs):
    return '; '.join(n(float(v)) for v in five(xs))


FIVE = ['Minimum:', 'Q1:', 'Median:', 'Q3:', 'Maximum:']

# ------------------------------------------------------------------ datasets (all synthetic; see datasets.py)
BOOKS = D('S1 books', [2, 4, 3, 2, 5, 3, 2, 6, 3, 4, 2, 3, 1, 3, 4], 'books', 'Books read over the summer by 15 students')
PETS = D('S1 pets', [0, 1, 1, 2, 0, 3, 1, 2, 1, 0, 4, 1, 2, 1, 0, 2, 1, 3], 'pets', 'Pets in each of 18 households')
QUIZ = D('S1 quiz', [7, 9, 8, 10, 7, 8, 8, 6, 9, 8, 7, 10, 8, 9], 'points', 'Quiz scores (out of 10) of 14 students')
GOALS = D('S1 goals', [1, 0, 2, 1, 3, 1, 0, 2, 2, 1, 4, 1, 0, 1, 2, 1], 'goals', 'Goals scored by a team in 16 games')
SIBS = D('S1 siblings', [1, 2, 0, 1, 3, 2, 1, 1, 0, 2, 5, 1, 2, 0, 1, 2, 3, 1, 1, 2], 'siblings', 'Siblings of 20 students')
CUPS = D('S1 cups', [2, 3, 1, 2, 4, 2, 3, 0, 2, 1, 3, 2], 'cups', 'Cups of water drunk before noon by 12 workers')
RAIN = D('S1 rain days', [3, 5, 4, 4, 6, 3, 4, 5, 7, 4], 'days', 'Rainy days in each of 10 two-week periods')

COMMUTE = D('S2 commute', [12, 25, 8, 31, 17, 22, 15, 40, 19, 27, 10, 33, 21, 14, 26, 18, 35, 23, 29, 16], 'minutes',
            'Commute times of 20 employees')
WAIT = D('S2 wait', [4, 11, 7, 15, 9, 5, 12, 20, 10, 6, 14, 8, 17, 10, 3, 13, 5, 9], 'minutes', 'Clinic waiting times of 18 patients')
JUMP = D('S2 jump', [152, 168, 145, 175, 160, 158, 171, 149, 163, 180, 155, 166, 150, 172, 161, 157], 'cm',
         'Standing long-jump distances of 16 students')
TEMP = D('S2 temps', [61, 58, 70, 66, 72, 59, 64, 75, 68, 63, 71, 60, 67, 65, 74, 69, 62, 70], 'degrees F',
         'Daily high temperatures in a town over 18 days')
PAGES = D('S2 pages', [120, 255, 188, 310, 96, 205, 150, 275, 230, 182, 140, 200, 260, 175], 'pages', 'Page counts of 14 novels')

LAPS = D('S3 laps', [12, 15, 9, 18, 14, 11, 16, 20, 13, 10, 17], 'laps', 'Laps swum by 11 swimmers')
SCORES = D('S3 scores', [72, 85, 90, 64, 78, 88, 95, 70, 81, 76, 84, 92], 'points', 'Test scores of 12 students')
SLEEP = D('S3 sleep', [7.5, 6, 8, 6.5, 9, 7, 5.5, 8.5, 7, 6.5, 7.5, 8, 6, 7], 'hours', 'Hours of sleep of 14 teenagers')
PRICE = D('S3 price', [3, 8, 5, 12, 6, 4, 9, 7, 10, 5, 6, 15, 4], 'dollars', 'Prices of 13 items on a menu')
DIST = D('S3 dist', [2.1, 3.4, 1.8, 5.0, 2.7, 4.2, 3.0, 2.4, 3.9, 1.5], 'km', 'Distances 10 students live from school')
SNOW = D('S3 snow', [4, 7, 2, 9, 5, 12, 6, 3, 8], 'inches', 'Snowfall in 9 storms')

TOWNA = D('S4 town A', [210, 225, 230, 240, 245, 250, 260, 900], 'thousand dollars', 'Sale prices of 8 homes in Town A')
TOWNB = D('S4 town B', [190, 220, 235, 255, 270, 280, 300, 310], 'thousand dollars', 'Sale prices of 8 homes in Town B')
CLP = D('S4 class P', [70, 74, 76, 78, 80, 82, 86], 'points', 'Scores of 7 students in class P')
CLQ = D('S4 class Q', [66, 70, 72, 74, 76, 78, 82], 'points', 'Scores of 7 students in class Q')
STX = D('S4 store X', [2, 2, 3, 3, 3, 4, 4, 5, 14], 'days', 'Delivery times of 9 orders from store X')
STY = D('S4 store Y', [2, 3, 3, 4, 4, 5, 5, 6, 6], 'days', 'Delivery times of 9 orders from store Y')
PLA = D('S4 plant A', [5, 6, 6, 7, 7, 8, 30], 'cm', 'Heights of 7 seedlings of plant A')
PLB = D('S4 plant B', [8, 8, 9, 9, 9, 10, 10], 'cm', 'Heights of 7 seedlings of plant B')
M1 = D('S4 machine 1', [498, 499, 500, 500, 501, 502], 'grams', 'Masses of 6 bags filled by machine 1')
M2 = D('S4 machine 2', [503, 504, 505, 505, 506, 507], 'grams', 'Masses of 6 bags filled by machine 2')

TEAMA = D('S5 team A', [14, 15, 15, 16, 16, 17, 18, 18, 19], 'years', 'Ages of 9 players on team A')
TEAMB = D('S5 team B', [13, 14, 16, 16, 17, 18, 20, 22, 25], 'years', 'Ages of 9 players on team B')
SD1 = D('S5 set 1', [4, 6, 8, 10, 12], 'minutes', 'Bus delays on 5 days, route 1')
SD2 = D('S5 set 2', [7, 8, 8, 8, 9], 'minutes', 'Bus delays on 5 days, route 2')
SD3 = D('S5 set 3', [10, 20, 30, 40, 50], 'dollars', 'Weekly savings of 5 students, group 1')
SD4 = D('S5 set 4', [25, 28, 30, 32, 35], 'dollars', 'Weekly savings of 5 students, group 2')
RENTA = D('S5 rent A', [800, 850, 900, 950, 1000, 1050, 2400], 'dollars', 'Monthly rents of 7 apartments in building A')
RENTB = D('S5 rent B', [700, 800, 900, 1000, 1100, 1200, 1300], 'dollars', 'Monthly rents of 7 apartments in building B')
FISHA = D('S5 fish A', [20, 22, 23, 25, 26, 28, 30, 31], 'cm', 'Lengths of 8 fish from lake A')
FISHB = D('S5 fish B', [18, 24, 24, 25, 25, 26, 26, 40], 'cm', 'Lengths of 8 fish from lake B')

GAMES = D('S7 points', [12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16], 'points', 'Points a player scored in 11 games')
TIMES = D('S7 race', [52, 55, 54, 31, 56, 53, 57, 55, 54], 'seconds', 'Times of 9 swimmers in a 50-meter race')
HOURS = D('S7 hours', [6, 8, 7, 9, 7, 8, 30, 6, 7, 8, 1], 'hours', 'Hours of screen time 11 students reported for one weekend')
PRICES = D('S7 bikes', [180, 210, 195, 205, 190, 600, 200, 185, 215, 220], 'dollars', 'Prices of 10 used bikes')


def dot_choices(xs, lo, hi, label, wrongs):
    """Correct dot plot first, then the dot plots of three wrong count tables (dicts)."""
    return [dotf(xs, lo, hi, label)] + [dotf(w, lo, hi, label) for w in wrongs]


def iqr(xs):
    f = five(xs)
    return f[3] - f[1]


SETS = [
    # ------------------------------------------------------------------ 1. ID.A.1 dot plots
    S('HSS-ID.A.1', 'Represent data with dot plots', num=1,
      target='Represent a data set with a dot plot: the number of dots above each value, and the dot plot that matches a list',
      strand='core', covers=['ID1-dot'],
      main=[
          sa('The numbers of books 15 students read over the summer are %s. A dot plot shows one dot for each student above '
             'the number of books. How many dots are above 2, above 3, and above 4?' % dlist(BOOKS),
             ['Dots above 2:', 'Dots above 3:', 'Dots above 4:'], key='%d; %d; %d' % (counts(BOOKS)[2], counts(BOOKS)[3], counts(BOOKS)[4]),
             note='Form required: all three. Counts: 1 → 1, 2 → 4, 3 → 5, 4 → 3, 5 → 1, 6 → 1 (15 dots in all).'),
          pickfig('The numbers of pets in 18 households are %s. Which dot plot shows the data?' % dlist(PETS), 'B',
                  dot_choices(PETS, 0, 5, 'Pets', [
                      {0: 4, 1: 6, 2: 5, 3: 2, 4: 1}, {1: 4, 2: 7, 3: 4, 4: 2, 5: 1}, {0: 7, 1: 4, 2: 4, 3: 2, 4: 1}]),
                  'Counts: 0 → 4, 1 → 7, 2 → 4, 3 → 2, 4 → 1. The others move one dot from 1 to 2, shift every value up 1, or swap '
                  'the counts of 0 and 1.'),
          sa('Fourteen quiz scores (out of 10) are %s. In a dot plot of the scores, which score has the tallest stack of dots, '
             'and how many dots are in that stack?' % dlist(QUIZ), ['Score:', 'Dots in that stack:'], key='8; 5',
             note='Form required: both. Counts: 6 → 1, 7 → 3, 8 → 5, 9 → 3, 10 → 2.'),
          pickfig('A team scored these numbers of goals in 16 games: %s. Which dot plot shows the data?' % dlist(GOALS), 'C',
                  dot_choices(GOALS, 0, 5, 'Goals', [
                      {0: 3, 1: 6, 2: 4, 3: 2, 4: 1}, {0: 7, 1: 3, 2: 4, 3: 1, 4: 1}, {0: 3, 1: 7, 2: 4, 3: 1}]),
                  'Counts: 0 → 3, 1 → 7, 2 → 4, 3 → 1, 4 → 1 (16 dots). The others move a dot from 1 to 3, swap the counts of 0 '
                  'and 1, or leave out the 4.'),
          sa('Twenty students reported their numbers of siblings: %s. In a dot plot of the data, how many dots are at values '
             'of 2 or more, and how many dots are there in all?' % dlist(SIBS), ['Dots at 2 or more:', 'Dots in all:'],
             key='%d; %d' % (sum(1 for x in SIBS if x >= 2), len(SIBS)),
             note='Form required: both. Counts: 0 → 3, 1 → 8, 2 → 6, 3 → 2, 5 → 1; 6 + 2 + 1 = 9 at 2 or more.'),
      ],
      back=[
          B('Count how often each value occurs', '6.SP.B.5.a', [
              sa('In the list 3, 5, 3, 4, 3, 5, how many times does 3 appear?', 'Answer:', key='3', note='3 appears in positions 1, 3 and 5.'),
              sa('In the list 1, 2, 2, 4, 2, 1, 2, how many times does 2 appear?', 'Answer:', key='4', note='Four of the seven values are 2.'),
              tf('The list 6, 6, 7, 8, 6 has three values equal to 6.', key=True, note='6 appears three times.'),
              mc('How many values are in the list 2, 4, 4, 5, 2, 4, 4?', ['7', '4', '3', '5'],
                 note='Count every value, repeats included. 4 is how often the value 4 appears; 3 and 5 are other miscounts.'),
              sa('In the list 0, 1, 0, 2, 1, 0, how many values are 0 or 1?', 'Answer:', key='5', note='Three 0s and two 1s.'),
          ], align='supporting',
            why=why('the student loses track of repeated values when tallying a list.', 'each stack in a dot plot is the count '
                    'of one value.', 'counts the occurrences of a value and the total number of values.')),
          B('Locate values on a number-line scale', '6.NS.C.6.c', [
              mc('A number line has marks labeled 0, 1, 2, 3, 4, 5, 6. Where does a dot for the value 4 go?', [
                  'above the mark labeled 4', 'above the fourth mark from the left, labeled 3', 'above the mark labeled 5',
                  'at the right end of the number line'],
                 note='Place the dot at the label, not by counting marks; the fourth mark from the left is 3 because the first is 0.'),
              tf('On a number line with marks at 0, 2, 4, 6, 8, the value 5 is halfway between the marks 4 and 6.', key=True,
                 note='5 is 1 more than 4 and 1 less than 6.'),
              sa('A number line has marks at 10, 15, 20, 25, 30. What value is halfway between the marks 15 and 20?', 'Answer:',
                 key='17.5', note='(15 + 20)/2.'),
              sa('A number line runs from 0 to 10 with a mark at every whole number. How many marks are there?', 'Answer:', key='11',
                 note='0, 1, ..., 10 is eleven marks.'),
              tf('On a horizontal number line, a larger value is placed to the left of a smaller value.', key=False,
                 note='Values increase to the right.'),
          ], align='supporting',
            why=why('the student misplaces values on the axis (counting marks instead of reading labels).', 'a dot plot is a '
                    'number line with stacks above it.', 'places values on number lines with different scales.')),
          B('Read counts from a dot plot', '6.SP.B.4', [
              sa('The dot plot shows the cups of water 12 workers drank before noon. How many workers drank 3 cups?', 'Answer:',
                 key=str(counts(CUPS)[3]), fig=dotf(CUPS, 0, 5, 'Cups of water'), note='The stack above 3 has 3 dots.'),
              sa('The dot plot shows the cups of water some workers drank before noon. How many workers are shown in all?', 'Answer:',
                 key=str(len(CUPS)), fig=dotf(CUPS, 0, 5, 'Cups of water'), note='1 + 2 + 5 + 3 + 1 = 12 dots.'),
              tf('The dot plot shows the cups of water 12 workers drank before noon. No worker drank 5 cups.', key=True,
                 fig=dotf(CUPS, 0, 5, 'Cups of water'), note='There are no dots above 5.'),
              mc('The dot plot shows the cups of water 12 workers drank before noon. Which number of cups occurs most often?',
                 ['2', '3', '5', '12'], fig=dotf(CUPS, 0, 5, 'Cups of water'),
                 note='The tallest stack (5 dots) is above 2. 12 is the number of workers; 5 is the height of the stack.'),
              sa('The dot plot shows the cups of water 12 workers drank before noon. How many workers drank fewer than 2 cups?',
                 'Answer:', key=str(sum(1 for x in CUPS if x < 2)), fig=dotf(CUPS, 0, 5, 'Cups of water'),
                 note='1 at 0 and 2 at 1.'),
          ], align='exact',
            why=why('the student cannot read a count from the height of a stack.', 'building a dot plot means producing these '
                    'stack heights.', 'reads single counts, totals and counts over a range from a dot plot.')),
      ],
      f1=B('Find the median and mean from a dot plot', 'HSS-ID.A.2', [
          sa('The dot plot shows rainy days in 10 two-week periods. Find the median number of rainy days.', 'Median:',
             key=n(float(median(RAIN))), fig=dotf(RAIN, 2, 8, 'Rainy days'),
             note='Ordered: 3, 3, 4, 4, 4, 4, 5, 5, 6, 7; the middle two values are 4 and 4.'),
          sa('The dot plot shows rainy days in 10 two-week periods. Find the mean number of rainy days. Give a decimal.', 'Mean:',
             key=n(float(mean(RAIN))), fig=dotf(RAIN, 2, 8, 'Rainy days'), note='Sum 45 over 10 values = 4.5.'),
          tf('A dot plot shows the values 3, 3, 4, 4, 4, 4, 5, 5, 6, 7. Adding one more dot at 20 changes the median more than it '
             'changes the mean.', key=False, note='The median stays 4; the mean moves from 4.5 to 65/11 ≈ 5.9.'),
          mc('The dot plot shows the cups of water 12 workers drank before noon. Which statement is correct?', [
              'The median is 2 cups and the mean is 2.08 cups (to the nearest hundredth).',
              'The median is 2.5 cups, halfway between the smallest and largest values.',
              'The median is 5 cups, the height of the tallest stack in the plot.',
              'The mean is 12 cups, because 12 workers are shown in the plot.'], fig=dotf(CUPS, 0, 5, 'Cups of water'),
             note='Ordered values: 0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4; median (2 + 2)/2 = 2; mean 25/12 ≈ 2.08. The others use the '
                  'midrange, a stack height, or the number of workers.'),
          sa('The dot plot shows the cups of water 12 workers drank before noon. Find the total number of cups drunk.', 'Answer:',
             key=str(sum(CUPS)), fig=dotf(CUPS, 0, 5, 'Cups of water'), note='0·1 + 1·2 + 2·5 + 3·3 + 4·1 = 25.'),
      ], prog='cross-standard extension', demand='Recover the data from a dot plot and compute its center.'),
      f2=B('Choose the display that keeps the information you need', 'HSS-ID.A.1', [
          mc('Which display always shows every individual value of a small data set?', [
              'a dot plot', 'a box plot', 'a histogram with bins of width 10', 'a box plot with outliers marked'],
             note='A dot plot keeps every value; box plots keep five summary values; a histogram keeps only counts per bin.'),
          mc('From a box plot alone, which of these can always be found?', ['the median', 'the mean', 'the most common value',
                                                                             'the number of values'],
             note='The box plot shows the five-number summary only.'),
          tf('A histogram with bins 0-10, 10-20, 20-30 shows how many values are exactly 15.', key=False,
             note='It shows only how many values are in the bin 10-20.'),
          mc('A school records the number of people in each of 400 students\' households (whole numbers from 1 to 9). Which '
             'display shows how many households have each size and stays readable?', [
              'a histogram with one bin for each whole number', 'a dot plot with one dot per household',
              'a box plot of the household sizes', 'a list of all 400 household sizes'],
             note='A dot plot of 400 values has stacks too tall to read; a box plot loses the counts; a list is not a display.'),
          tf('Two different data sets can have the same box plot but different dot plots.', key=True,
             note='1, 2, 3, 4, 5, 6, 7 and 1, 2, 3.5, 4, 4.5, 6, 7 both have the five-number summary 1, 2, 4, 6, 7.'),
      ], prog='same-course deepening', demand='Decide which display keeps the information a question needs.',
        builds='Builds on FORWARD 1: after recovering summaries from a dot plot, the student judges which other displays keep '
               'enough information to recover them.')),

    # ------------------------------------------------------------------ 2. ID.A.1 histograms
    S('HSS-ID.A.1', 'Represent data with histograms', num=2,
      target='Represent a data set with a histogram: the count in each stated bin, using the stated endpoint rule',
      strand='core', covers=['ID1-hist'],
      main=[
          sa('Commute times (minutes) of 20 employees are %s. A histogram uses the bins 0-10, 10-20, 20-30, 30-40 and 40-50.%s '
             'How many values are in the bins 10-20, 30-40 and 40-50?' % (dlist(COMMUTE), EP), ['10-20:', '30-40:', '40-50:'],
             key='%d; %d; %d' % (bincount(COMMUTE, [10, 20])[0], bincount(COMMUTE, [30, 40])[0], bincount(COMMUTE, [40, 50])[0]),
             note='Form required: all three. Counts 0-10: 1, 10-20: 8 (10 is included), 20-30: 7, 30-40: 3, 40-50: 1 (40 goes '
                  'in 40-50).'),
          pickfig('Waiting times (minutes) of 18 patients are %s. Which histogram shows the data with bins 0-5, 5-10, 10-15, '
                  '15-20, 20-25?%s' % (dlist(WAIT), EP), 'A',
                  [histf([0, 5, 10, 15, 20, 25], bincount(WAIT, [0, 5, 10, 15, 20, 25]), 'Minutes', ymax=8, ystep=2),
                   histf([0, 5, 10, 15, 20, 25], bincount_right(WAIT, [0, 5, 10, 15, 20, 25]), 'Minutes', ymax=8, ystep=2),
                   histf([0, 5, 10, 15, 20, 25], [2, 7, 6, 2, 1], 'Minutes', ymax=8, ystep=2),
                   histf([0, 5, 10, 15, 20, 25], [3, 5, 6, 3, 1], 'Minutes', ymax=8, ystep=2)],
                  'Counts 0-5: %d, 5-10: %d, 10-15: %d, 15-20: %d, 20-25: %d (5, 10, 15 and 20 go in the bin they start). The '
                  'others put endpoints in the lower bin or miscount.' % tuple(bincount(WAIT, [0, 5, 10, 15, 20, 25])), h=200),
          sa('Standing long-jump distances (cm) of 16 students are %s. A histogram uses the bins 140-150, 150-160, 160-170, '
             '170-180 and 180-190.%s How many values are in the bins 150-160 and 170-180?' % (dlist(JUMP), EP),
             ['150-160:', '170-180:'], key='%d; %d' % (bincount(JUMP, [150, 160])[0], bincount(JUMP, [170, 180])[0]),
             note='Form required: both. Counts 140-150: 2, 150-160: 5, 160-170: 5, 170-180: 3, 180-190: 1.'),
          pickfig('Daily high temperatures (°F) over 18 days are %s. Which histogram shows the data with bins 55-60, 60-65, 65-70, '
                  '70-75, 75-80?%s' % (dlist(TEMP), EP), 'D',
                  [histf([55, 60, 65, 70, 75, 80], bincount(TEMP, [55, 60, 65, 70, 75, 80]), '°F', ymax=8, ystep=2),
                   histf([55, 60, 65, 70, 75, 80], bincount_right(TEMP, [55, 60, 65, 70, 75, 80]), '°F', ymax=8, ystep=2),
                   histf([55, 60, 65, 70, 75, 80], [2, 5, 5, 5, 1], '°F', ymax=8, ystep=2),
                   histf([55, 60, 65, 70, 75, 80], [2, 4, 6, 5, 1], '°F', ymax=8, ystep=2)],
                  'Counts 55-60: %d, 60-65: %d, 65-70: %d, 70-75: %d, 75-80: %d. The others put endpoints such as 60, 65, 70 and 75 '
                  'in the lower bin, or miscount.' % tuple(bincount(TEMP, [55, 60, 65, 70, 75, 80])), h=200),
          sa('Page counts of 14 novels are %s. A histogram uses bins of width 50: 50-100, 100-150, ..., 300-350.%s Which bin has '
             'the most values (give its left endpoint), and how many values does it have?' % (dlist(PAGES), EP),
             ['Left endpoint of the tallest bin:', 'Values in that bin:'], key='150; %d' % bincount(PAGES, [150, 200])[0],
             note='Form required: both. Counts 50-100: 1, 100-150: 2, 150-200: 4, 200-250: 3, 250-300: 3, 300-350: 1.'),
      ],
      back=[
          B('Assign values to bins with an endpoint rule', '6.SP.B.4', [
              mc('Bins 10-20 and 20-30 each include their left endpoint and exclude their right endpoint. Which bin holds 20?',
                 ['20-30', '10-20', 'both bins', 'neither bin'], note='20 is the left endpoint of 20-30 and the excluded right end of 10-20.'),
              tf('With bins that include the left endpoint and exclude the right endpoint, the value 30 goes in the bin 20-30.',
                 key=False, note='30 is excluded from 20-30; it goes in 30-40.'),
              sa('Bins 0-5, 5-10 and 10-15 include their left endpoint and exclude their right endpoint. Which bin holds 9.9? Give '
                 'its left endpoint.', 'Answer:', key='5', note='5 ≤ 9.9 < 10.'),
              sa('How many of the values 4, 5, 9, 10, 12 fall in the bin 5-10, which includes 5 and excludes 10?', 'Answer:', key='2',
                 note='5 and 9.'),
              tf('If every bin included both of its endpoints, a value equal to an endpoint shared by two bins would be counted twice.',
                 key=True, note='That is why a rule must give each endpoint to exactly one bin.'),
          ], align='exact',
            why=why('the student puts a value equal to a bin endpoint in the wrong bin.', 'histogram counts depend on the endpoint '
                    'rule.', 'assigns endpoint and non-endpoint values to bins under a stated rule.')),
          B('Count the values in an interval', '6.SP.B.5.a', [
              sa('How many of the values 12, 18, 25, 31, 19, 22 are at least 15 and less than 25?', 'Answer:', key='3', note='18, 19, 22.'),
              sa('How many of the values 3.5, 4, 6.2, 7, 8 are at least 4 and less than 7?', 'Answer:', key='2', note='4 and 6.2.'),
              tf('Exactly two of the values 40, 45, 50, 55 are at least 45 and less than 55.', key=True, note='45 and 50.'),
              mc('How many of the values 2, 9, 11, 14, 20, 21 are at least 10 and less than 20?', ['2', '3', '4', '1'],
                 note='11 and 14; 20 is not less than 20.'),
              sa('How many of the values 100, 150, 199, 200, 250 are at least 100 and less than 200?', 'Answer:', key='3',
                 note='100, 150, 199.'),
          ], align='supporting',
            why=why('the student miscounts values in an interval, especially at its ends.', 'each bar of a histogram is one such '
                    'count.', 'counts values in intervals with included and excluded ends.')),
          B('Read a histogram', '6.SP.B.4', [
              sa('The histogram shows the commute times of some employees. How many employees have commutes in the bin 20-30?',
                 'Answer:', key='7', fig=histf([0, 10, 20, 30, 40, 50], bincount(COMMUTE, [0, 10, 20, 30, 40, 50]), 'Minutes', ymax=9),
                 note='The 20-30 bar reaches 7.'),
              sa('The histogram shows the commute times of some employees. How many employees are shown in all?', 'Answer:',
                 key='20', fig=histf([0, 10, 20, 30, 40, 50], bincount(COMMUTE, [0, 10, 20, 30, 40, 50]), 'Minutes', ymax=9),
                 note='1 + 8 + 7 + 3 + 1 = 20.'),
              tf('The histogram shows the commute times of some employees. It shows that one employee\'s commute was exactly 15 minutes.',
                 key=False, fig=histf([0, 10, 20, 30, 40, 50], bincount(COMMUTE, [0, 10, 20, 30, 40, 50]), 'Minutes', ymax=9),
                 note='A histogram shows counts per bin, not individual values.'),
              mc('The histogram shows the commute times of some employees. Which bin has the most values?',
                 ['10-20', '20-30', '0-10', '30-40'],
                 fig=histf([0, 10, 20, 30, 40, 50], bincount(COMMUTE, [0, 10, 20, 30, 40, 50]), 'Minutes', ymax=9),
                 note='Its bar reaches 8.'),
              sa('The histogram shows the commute times of some employees. How many employees have commutes of at least 30 minutes?',
                 'Answer:', key='4', fig=histf([0, 10, 20, 30, 40, 50], bincount(COMMUTE, [0, 10, 20, 30, 40, 50]), 'Minutes', ymax=9),
                 note='3 in 30-40 and 1 in 40-50.'),
          ], align='exact',
            why=why('the student reads a histogram as individual values or misreads bar heights.', 'the student must produce '
                    'these bar heights.', 'reads bar heights, totals and counts over several bins.')),
      ],
      f1=B('Regroup a histogram with wider bins', 'HSS-ID.A.1', [
          sa('A histogram with bins 0-5, 5-10, 10-15, 15-20 has counts 3, 6, 8, 2. What are the counts for the wider bins 0-10 and '
             '10-20?', ['0-10:', '10-20:'], key='9; 10', note='Form required: both. 3 + 6 and 8 + 2.'),
          sa('A histogram with bins 60-65, 65-70, 70-75, 75-80 has counts 2, 5, 6, 4. What are the counts for 60-70 and 70-80?',
             ['60-70:', '70-80:'], key='7; 10', note='Form required: both. 2 + 5 and 6 + 4.'),
          tf('Combining each pair of neighboring bins into one bin never changes the total number of values shown.', key=True,
             note='Every value is still counted exactly once.'),
          mc('A histogram with bins of width 1 has counts 1, 0, 2, 0, 1, 0, 3, 0, 2, so it looks jagged. Why might bins of width 2 '
             'help?', [
              'Wider bins group nearby values, so the overall shape is easier to see.',
              'Wider bins change the data values, so the shape becomes smoother.',
              'Wider bins add values to the empty bins, so no bin is 0.',
              'Wider bins always make a distribution look symmetric.'],
             note='Regrouping changes only the summary, not the data. The others claim the data change, values are added, or '
                  'symmetry always appears.'),
          mc('A histogram with bins of width 10 has counts 4, 9, 5. Can the counts for bins of width 5 be found from it?', [
              'No: each count could be split between the two narrower bins in many ways.',
              'Yes: halve each count, because each narrower bin is half as wide.',
              'Yes: keep the same counts, because the data have not changed.',
              'No: a histogram with bins of width 10 cannot be redrawn at all.'],
             note='Combining bins loses information that cannot be recovered. Halving assumes an even split; the others are false.'),
      ], prog='same-course deepening', demand='Regroup bins and judge what a change of bin width can and cannot show.'),
      f2=B('Locate the median in a histogram', 'HSS-ID.A.2', [
          sa('A histogram of 21 values has counts 0-10: 4, 10-20: 6, 20-30: 7, 30-40: 4. The median is the 11th value in order. '
             'Which bin holds it? Give its left endpoint.', 'Answer:', key='20', note='4 + 6 = 10 values come before 20, so the 11th is in 20-30.'),
          sa('A histogram of 20 values has counts 50-60: 3, 60-70: 5, 70-80: 8, 80-90: 4. The median is the mean of the 10th and '
             '11th values. Which bin holds both? Give its left endpoint.', 'Answer:', key='70',
             note='3 + 5 = 8 values lie below 70; the 9th through 16th are in 70-80.'),
          tf('The bin with the tallest bar always holds the median.', key=False,
             note='Counts 10, 2, 3, 1, 9 (25 values): the tallest bar is the first, but the median (13th value) is in the third bin.'),
          mc('A histogram of 15 values has counts 0-5: 10, 5-10: 2, 10-15: 2, 15-20: 1. Which bin holds the median (the 8th value)?',
             ['0-5', '5-10', '10-15', '15-20'], note='The first 10 values are in 0-5. The others use the middle bin or later bins.'),
          sa('A histogram of 15 values has counts 0-10: 2, 10-20: 3, 20-30: 3, 30-40: 7. Which bin holds the median (the 8th '
             'value)? Give its left endpoint.', 'Answer:', key='20', note='2 + 3 = 5 below 20, 8 below 30; the 8th is in 20-30.'),
      ], prog='cross-standard extension', demand='Use cumulative bin counts to locate the median.',
        builds='Builds on FORWARD 1: with only grouped counts available (as after regrouping), the student locates the median '
               'from cumulative counts.')),

    # ------------------------------------------------------------------ 3. ID.A.1 box plots
    S('HSS-ID.A.1', 'Represent data with box plots', num=3,
      target='Represent a data set with a box plot: its five-number summary under the stated quartile rule, and the box plot '
             'that matches a list',
      strand='core', covers=['ID1-box'],
      main=[
          sa('Laps swum by 11 swimmers: %s. Give the five-number summary for a box plot.%s' % (dlist(LAPS), QRULE), FIVE,
             key=fvk(LAPS), note='Form required: all five. Ordered: 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20; median 14; lower '
                                 'half 9-13 gives Q1 = 11; upper half 15-20 gives Q3 = 17.'),
          pickfig('Test scores of 12 students: %s. Which box plot shows the data?%s' % (dlist(SCORES), QRULE), 'C',
                  [boxf(five(SCORES), 60, 100, 'Points', step=5),
                   boxf((64, 74, 81, 89, 95), 60, 100, 'Points', step=5),
                   boxf((64, 72, 82.5, 88, 95), 60, 100, 'Points', step=5),
                   boxf((64, 76, 82.5, 90, 95), 60, 100, 'Points', step=5)],
                  'Ordered: 64, 70, 72, 76, 78, 81, 84, 85, 88, 90, 92, 95; median (81 + 84)/2 = 82.5; Q1 = (72 + 76)/2 = 74; '
                  'Q3 = (88 + 90)/2 = 89. The others use 81 as the median, the 3rd and 9th values as quartiles, or the wrong '
                  'middle pair of each half.', h=150),
          sa('Hours of sleep of 14 teenagers: %s. Give the five-number summary for a box plot.%s' % (dlist(SLEEP), QRULE), FIVE,
             key=fvk(SLEEP), note='Form required: all five. Ordered: 5.5, 6, 6, 6.5, 6.5, 7, 7 | 7, 7.5, 7.5, 8, 8, 8.5, 9; '
                                  'median 7; Q1 = 6.5; Q3 = 8.'),
          pickfig('Prices (dollars) of 13 menu items: %s. Which box plot shows the data?%s' % (dlist(PRICE), QRULE), 'A',
                  [boxf(five(PRICE), 0, 16, 'Dollars', step=1, lstep=2),
                   boxf((3, 4.5, 7, 9.5, 15), 0, 16, 'Dollars', step=1, lstep=2),
                   boxf((3, 5, 6, 9, 15), 0, 16, 'Dollars', step=1, lstep=2),
                   boxf((3, 4.5, 6, 9.5, 12), 0, 16, 'Dollars', step=1, lstep=2)],
                  'Ordered: 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 10, 12, 15; median 6 (7th value); Q1 = (4 + 5)/2 = 4.5; Q3 = (9 + 10)/2 = '
                  '9.5. The others use 7 as the median, keep the median in both halves (Q1 = 5, Q3 = 9), or end the whisker at 12.',
                  h=150),
          sa('Distances (km) 10 students live from school: %s. Give the five-number summary for a box plot.%s' % (dlist(DIST), QRULE),
             FIVE, key=fvk(DIST), note='Form required: all five. Ordered: 1.5, 1.8, 2.1, 2.4, 2.7 | 3.0, 3.4, 3.9, 4.2, 5.0; median '
                                       '(2.7 + 3.0)/2 = 2.85; Q1 = 2.1; Q3 = 3.9.'),
      ],
      back=[
          B('Order data and find the median', '6.SP.B.5.c', [
              sa('Find the median of 9, 3, 7, 5, 11.', 'Median:', key='7', note='Ordered: 3, 5, 7, 9, 11.'),
              sa('Find the median of 4, 10, 6, 8.', 'Median:', key='7', note='Ordered: 4, 6, 8, 10; (6 + 8)/2.'),
              tf('The median of 2, 9, 4 is 9, the middle value of the list as written.', key=False,
                 note='Order first: 2, 4, 9; the median is 4.'),
              mc('What is the median of 1, 3, 3, 6, 7, 8?', ['4.5', '3', '6', '4.67'],
                 note='(3 + 6)/2 = 4.5. 3 is the mode, 6 a middle value alone, 4.67 the mean.'),
              sa('Find the median of 12, 15, 11, 14, 13, 16, 10.', 'Median:', key='13', note='Ordered: 10, 11, 12, 13, 14, 15, 16.'),
          ], align='exact',
            why=why('the student takes the middle of the unordered list or mishandles an even count.', 'every box plot needs the '
                    'median.', 'orders data and finds the median for odd and even counts.')),
          B('Find quartiles as medians of the halves', '6.SP.B.5.c', [
              sa('For 2, 4, 6, 8, 10, 12, 14, 16, find Q1 and Q3 (each the median of a half).', ['Q1:', 'Q3:'], key='5; 13',
                 note='Form required: both. Halves 2, 4, 6, 8 and 10, 12, 14, 16.'),
              sa('For 1, 3, 5, 7, 9, 11, 13 (an odd count), leave out the median and find Q1 and Q3.', ['Q1:', 'Q3:'], key='3; 11',
                 note='Form required: both. Halves 1, 3, 5 and 9, 11, 13.'),
              tf('For 1, 2, 3, 4, 5, 6, 7, 8, 9, Q1 is 2.5 when the median 5 is left out of both halves.', key=True,
                 note='Lower half 1, 2, 3, 4; its median is 2.5.'),
              mc('For 10, 20, 30, 40, 50, 60, what is the interquartile range Q3 - Q1?', ['30', '50', '20', '35'],
                 note='Q1 = 20, Q3 = 50. 50 is the range; 20 and 35 come from wrong halves.'),
              sa('For 5, 6, 8, 9, 12, 15, find Q1.', 'Q1:', key='6', note='Lower half 5, 6, 8.'),
          ], align='exact',
            why=why('the student cannot split the data into halves or forgets to leave out the median.', 'the box edges are the '
                    'quartiles.', 'finds Q1 and Q3 for odd and even counts under the stated rule.')),
          B('Read a box plot', '6.SP.B.4', [
              sa('The box plot shows the snowfall in some storms. What is the median snowfall?', 'Median (inches):', key=n(float(median(SNOW))),
                 fig=boxf(five(SNOW), 0, 14, 'Inches'), note='The line inside the box is at 6.'),
              sa('The box plot shows the snowfall in some storms. What is the interquartile range?', 'IQR (inches):',
                 key=n(float(five(SNOW)[3] - five(SNOW)[1])), fig=boxf(five(SNOW), 0, 14, 'Inches'),
                 note='Q3 - Q1 = 8.5 - 3.5 = 5.'),
              tf('The box plot shows the snowfall in some storms. About half of the storms had at least 6 inches.', key=True,
                 fig=boxf(five(SNOW), 0, 14, 'Inches'), note='The median is 6.'),
              mc('The box plot shows the snowfall in some storms. What is the range?', ['10 inches', '5 inches', '12 inches', '6 inches'],
                 fig=boxf(five(SNOW), 0, 14, 'Inches'), note='12 - 2 = 10. 5 is the IQR, 12 the maximum, 6 the median.'),
              sa('The box plot shows the snowfall in some storms. What is Q1?', 'Q1 (inches):', key=n(float(five(SNOW)[1])),
                 fig=boxf(five(SNOW), 0, 14, 'Inches'), note='The left edge of the box is at 3.5.'),
          ], align='exact',
            why=why('the student cannot match the parts of a box plot to the five-number summary.', 'the student must produce '
                    'those five numbers.', 'reads the median, quartiles, IQR and range from a box plot.')),
      ],
      f1=B('Mark outliers on a box plot', 'HSS-ID.A.3', [
          sa('A data set has Q1 = 20 and Q3 = 30.%s What are the lower and upper fences?' % OUTRULE, ['Lower fence:', 'Upper fence:'],
             key='5; 45', note='Form required: both. IQR 10; 20 - 15 and 30 + 15.'),
          sa('Prices of 10 used bikes (dollars): %s.%s%s How many outliers are there, and where does the upper whisker end?' % (
              dlist(PRICES), QRULE, OUTRULE), ['Number of outliers:', 'Upper whisker ends at:'], key='1; 220',
             note='Form required: both. Ordered 180, 185, 190, 195, 200, 205, 210, 215, 220, 600; Q1 = 190, Q3 = 215, IQR 25; '
                  'fences 152.5 and 252.5; only 600 is an outlier; the whisker ends at the largest non-outlier, 220.'),
          tf('In a box plot that marks outliers, a whisker ends at the fence value.', key=False,
             note='It ends at the most extreme data value inside the fence.'),
          mc('Race times (seconds) of 9 swimmers: %s.%s%s Which value is an outlier?' % (dlist(TIMES), QRULE, OUTRULE),
             ['31', '57', 'both 31 and 57', 'none'],
             note='Ordered 31, 52, 53, 54, 54, 55, 55, 56, 57; Q1 = (52 + 53)/2 = 52.5, Q3 = (55 + 56)/2 = 55.5; IQR 3; fences 48 '
                  'and 60; only 31 is outside.'),
          sa('A box plot that marks outliers has Q1 = 14 and Q3 = 17, and the largest data values are 18 and 41.%s Where does the '
             'upper whisker end?' % OUTRULE, 'Answer:', key='18', note='Upper fence 17 + 4.5 = 21.5; 41 is an outlier, 18 is not.'),
      ], prog='cross-standard extension', demand='Apply the 1.5·IQR rule to decide which values are drawn as outliers.'),
      f2=B('Compare two box plots', 'HSS-ID.A.2', [
          mc('The box plots show the reaction times of two groups. Which comparison is correct?', [
              'Group 2 has the greater median and the greater IQR.', 'Group 1 has the greater median and the greater IQR.',
              'The groups have the same median but different IQRs.', 'Group 1 has the greater range and the greater median.'],
             fig=boxes2(['Group 1', 'Group 2'], [(200, 230, 250, 270, 310), (210, 240, 280, 330, 360)], 180, 380, 'Milliseconds',
                        step=20), note='Medians 250 and 280; IQRs 40 and 90. The others reverse or misread.'),
          sa('Box plot 1 has median 40 and IQR 12; box plot 2 has median 46 and IQR 8. By how much do the medians differ, and which '
             'has the smaller IQR (enter 1 or 2)?', ['Difference of medians:', 'Smaller IQR (1 or 2):'], key='6; 2',
             note='Form required: both. 46 - 40 = 6; 8 < 12.'),
          tf('If two box plots have the same median, the two data sets have the same mean.', key=False,
             note='The mean is not shown by a box plot and can differ (for example with different skew).'),
          mc('The box plots show the battery lives of two brands. About what fraction of brand B batteries last longer than the '
             'median life of brand A?', ['about 3/4', 'about 1/4', 'about 1/2', 'none'],
             fig=boxes2(['Brand A', 'Brand B'], [(6, 8, 9, 10, 12), (7, 9, 10, 11, 13)], 4, 14, 'Hours'),
             note='Brand A\'s median is 9, which is Brand B\'s Q1, so about 3/4 of Brand B lies above it.'),
          sa('Two box plots: class A has Q1 = 70 and Q3 = 85; class B has Q1 = 72 and Q3 = 80. Give each IQR.', ['IQR of A:', 'IQR of B:'],
             key='15; 8', note='Form required: both.'),
      ], prog='cross-standard extension', demand='Compare two data sets through their box plots.',
        builds='Builds on FORWARD 1: with outliers marked correctly, box plots can be read side by side to compare center and spread.')),
]
