from qb import S, B, sa, mc, tf, q1, table, tape, hist, hrow, plot

FRUIT = hist(['Apple', 'Banana', 'Grape', 'Orange'], [6, 4, 8, 2], gap=0.35, ymax=10, ystep=2,
             xlabel='Favorite fruit', ylabel='Students', h=200)
PETS = table([['Pet', 'Dogs', 'Cats', 'Fish'], ['Students', '11', '6', '4']], header='both')
ABC = ['A', 'B', 'Both are the same.']


def bar(n, shade=0, **kw):
    d = dict(n=n, shade=shade)
    d.update(kw)
    return tape(d)


def grid(xmax, ymax, ystep=1, xlabel=None, ylabel=None):
    return q1(xmax, ymax, ystep=ystep, square=False, xlabel=xlabel, ylabel=ylabel)


def tplot(rows, xmax, ymax, ystep=1):
    return hrow(table(rows, fs=0.9), grid(xmax, ymax, ystep, rows[0][0], rows[1][0]), h=245)


SETS = [
    # ------------------------------------------------------------------ 6.RP.A.1 (write)
    S('6.RP.A.1', 'Write a ratio that describes the relationship between two quantities',
      main=[
          sa('A fruit bowl has 5 pears and 8 plums.\nWrite the ratio of pears to plums.', 'Ratio:'),
          sa('A choir has 14 sopranos and 9 altos.\nWrite the ratio of altos to sopranos.', 'Ratio:'),
          sa('The table shows the pets owned by students in a class.\nWrite the ratio of dogs to fish.', 'Ratio:', fig=PETS),
          sa('A parking lot has 13 cars and 7 trucks. There are no other vehicles.\nWrite the ratio of trucks to all of the vehicles.', 'Ratio:'),
          sa('A bag has 20 marbles. 12 are green and the rest are yellow.\nWrite the ratio of yellow marbles to green marbles.', 'Ratio:'),
      ],
      back=[
          B('Reading counts from a table or graph', '3.MD.B.3', [
              sa('The graph shows the favorite fruits of a class.\nHow many students chose grape?', 'Students:', fig=FRUIT),
              sa('The graph shows the favorite fruits of a class.\nHow many students chose banana?', 'Students:', fig=FRUIT),
              sa('The table shows the pets owned by students.\nHow many students own cats?', 'Students:', fig=PETS),
              mc('Which fruit was chosen by 2 students?', ['Orange', 'Apple', 'Banana', 'Grape'], fig=FRUIT),
              tf('6 students chose apple.', fig=FRUIT),
          ]),
          B('Parts and totals', '2.OA.A.1', [
              sa('A team has 9 boys and 6 girls.\nHow many players are on the team?', 'Players:'),
              sa('A box holds 24 crayons. 15 are broken.\nHow many crayons are NOT broken?', 'Crayons:'),
              tf('A shelf has 7 red books and 12 blue books. There are 19 books in all.'),
              mc('A garden has 30 plants. 18 are flowers and the rest are herbs.\nHow many herbs are there?', ['12', '48', '18', '22']),
              sa('A bus has 17 adults and 26 children.\nHow many people are on the bus?', 'People:'),
          ]),
          B('Fraction of a whole', '3.NF.A.1', [
              sa('The bar is divided into equal parts.\nWhat fraction of the bar is shaded?', 'Fraction:', fig=bar(7, 3)),
              sa('A pizza is cut into 6 equal slices. Ava eats 5 slices.\nWhat fraction of the pizza does Ava eat?', 'Fraction:'),
              tf('A bar is cut into 4 equal parts and 1 part is shaded. The shaded part is {1/4} of the bar.'),
              mc('What fraction of the bar is shaded?', ['{2/5}', '{2/3}', '{3/5}', '{5/2}'], fig=bar(5, 2)),
              sa('A field has 8 equal sections. Corn grows in 3 of the sections.\nWhat fraction of the field has corn?', 'Fraction:'),
          ]),
      ],
      f1=B('Ratios and unit rates with fractional quantities', '7.RP.A.1', [
          sa('A dressing uses {1/2} cup of oil for every {3/4} cup of vinegar.\nHow many cups of oil are used per cup of vinegar?', 'Cups of oil:'),
          sa('Mia paints {2/3} of a fence in {1/2} hour.\nHow much of the fence does she paint per hour?', 'Fence per hour:'),
          mc('A garden uses {3/4} bag of soil for every {3/8} bag of mulch.\nHow many bags of soil are used per bag of mulch?', ['2', '{1/2}', '{9/32}', '1{1/8}']),
          sa('A cyclist rides 2{1/2} miles in {1/6} hour.\nWhat is the speed in miles per hour?', 'Speed:'),
          sa('A pump moves {5/8} gallon of water every {1/4} minute.\nHow many gallons does it move per minute?', 'Gallons per minute:'),
      ]),
      f2=B('The unit rate as the slope of a graph', '8.EE.B.5', [
          sa('The graph shows a proportional relationship between minutes and gallons.\nWhat is the slope of the line?', 'Slope:',
             fig=q1(5, 12, ystep=2, square=False, xlabel='Minutes', ylabel='Gallons', pts=[(2, 5), (4, 10)], lines=[((0, 0), (4.8, 12))])),
          sa('The graph of a proportional relationship passes through (0, 0) and (6, 9).\nWhat is the slope?', 'Slope:'),
          sa('The graph shows the distance a car travels.\nWhat is the slope of the line in miles per hour?', 'Slope:',
             fig=q1(5, 300, ystep=50, square=False, xlabel='Hours', ylabel='Miles', pts=[(1, 60), (2, 120), (3, 180), (4, 240)], lines=[((0, 0), (5, 300))])),
          mc('A proportional relationship has a unit rate of 4 dollars per pound.\nWhich point is on its graph?', ['(3, 12)', '(12, 3)', '(4, 1)', '(3, 7)']),
          tf('For y = 2.5x, the unit rate is 2.5, and the slope of its graph is also 2.5.'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.1 (interpret)
    S('6.RP.A.1', 'Interpret ratio language ("for every," "to")',
      main=[
          mc('A recipe uses 5 cups of flour for every 2 cups of sugar.\nWhich statement describes the same ratio?',
             ['The ratio of sugar to flour is 2 : 5.', 'The ratio of flour to sugar is 2 : 5.',
              'For every 2 cups of flour, there are 5 cups of sugar.', 'For every 7 cups of sugar, there are 5 cups of flour.']),
          mc('At an aquarium, the ratio of sharks to rays is 4 : 9.\nWhich statement is true?',
             ['For every 9 rays, there are 4 sharks.', 'For every 9 sharks, there are 4 rays.',
              'For every 4 rays, there are 9 sharks.', 'For every 13 sharks, there are 4 rays.']),
          mc('The ratio of red beads to blue beads is 3 : 7.\nWhich statement is true?',
             ['For every 3 red beads, there are 7 blue beads.', 'For every 3 blue beads, there are 7 red beads.',
              'For every 10 blue beads, there are 3 red beads.', 'For every 7 red beads, there are 3 blue beads.']),
          mc('At a camp, there are 2 counselors for every 9 campers.\nWhat is the ratio of campers to counselors?', ['9 : 2', '2 : 9', '2 : 11', '11 : 9']),
          mc('In a class vote, there were 4 votes for pizza for every 3 votes for tacos.\nWhich statement is true?',
             ['The ratio of taco votes to pizza votes is 3 : 4.', 'The ratio of pizza votes to taco votes is 3 : 4.',
              'The ratio of pizza votes to all votes is 4 : 3.', 'There were 4 taco votes for every 3 pizza votes.']),
      ],
      back=[
          B('Equal groups', '3.OA.A.1', [
              tf('4 × 6 can mean 4 groups with 6 in each group.'),
              mc('There are 3 bags with 5 apples in each bag.\nWhich expression shows the total?', ['3 × 5', '3 + 5', '5 - 3', '5 ÷ 3']),
              sa('There are 7 tables with 4 chairs at each table.\nHow many chairs are there?', 'Chairs:'),
              tf('"2 wheels for every bike" means each bike has 2 wheels.'),
              mc('What does 6 × 2 mean?', ['6 groups of 2', '6 more than 2', '6 minus 2', '62']),
          ]),
          B('Multiplicative comparison statements', '4.OA.A.1', [
              tf('24 is 3 times as many as 8.'),
              mc('Which equation shows "42 is 6 times as many as 7"?', ['42 = 6 × 7', '42 = 6 + 7', '7 = 6 × 42', '42 - 7 = 6']),
              tf('18 is 6 times as many as 3.'),
              sa('Fill in the blank.\n45 is ___ times as many as 9.', 'Blank:'),
              tf('20 is 4 times as many as 16.'),
          ]),
      ],
      f1=B('Constant of proportionality from a description', '7.RP.A.2.b', [
          sa('A candle burns 2 inches every 3 hours at a constant rate.\nWhat is the constant of proportionality in inches per hour?', 'k ='),
          sa('For every 5 laps, Jo swims 250 meters.\nWhat is the constant of proportionality in meters per lap?', 'k ='),
          mc('A machine fills 18 bottles for every 4 minutes.\nWhat is the constant of proportionality in bottles per minute?', ['4.5', '{2/9}', '14', '72']),
          sa('For every 8 cups of water, a recipe uses 3 cups of rice.\nWhat is the constant of proportionality in cups of rice per cup of water?', 'k ='),
          tf('For every 6 pounds of apples, the cost is $9. The constant of proportionality is 1.5 dollars per pound.'),
      ]),
      f2=B('Compare proportional relationships represented in different ways', '8.EE.B.5', [
          mc('Cyclist A\'s distance is shown in the graph. Cyclist B rides according to d = 7.5t, where d is miles and t is hours.\nWhich cyclist is faster?',
             ['Cyclist A', 'Cyclist B', 'They ride at the same speed.'],
             fig=q1(4, 32, ystep=4, square=False, xlabel='Hours', ylabel='Miles', pts=[(2, 16), (4, 32)], lines=[((0, 0), (4, 32))])),
          sa('Tank A fills according to y = 12x, where x is minutes and y is gallons. The graph of Tank B is a line through (0, 0) and (3, 45).\nWhich tank fills faster, and by how many gallons per minute?', 'Answer:'),
          mc('Store A: 2 pounds of apples cost $3.50.\nStore B: the cost is c = 1.6p for p pounds.\nWhich store charges less per pound?', ['Store A', 'Store B', 'They charge the same.']),
          mc('Printer A prints 3 pages for every 2 seconds. Printer B prints according to p = 1.4s.\nWhich printer is faster?', ['Printer A', 'Printer B', 'They are the same.']),
          sa('Car A travels 150 miles in 3 hours at a constant speed. Car B travels according to d = 48t.\nHow much faster is Car A, in miles per hour?', 'Miles per hour:'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.2
    S('6.RP.A.2', 'Find and describe a unit rate',
      main=[
          sa('A car travels 150 miles in 3 hours at a constant speed.\nWhat is the unit rate in miles per hour?', 'Unit rate:'),
          sa('A 4-pound bag of rice costs $12.\nWhat is the price per pound?', 'Price per pound:'),
          sa('A punch recipe uses 5 cups of juice for every 8 cups of water.\nHow many cups of juice are used for each cup of water?', 'Cups of juice:'),
          mc('There are 2 teachers for every 30 students on a field trip.\nHow many students are there per teacher?', ['15', '28', '30', '60']),
          sa('A printer prints 90 pages in 6 minutes.\nHow many pages does it print per minute?', 'Pages per minute:'),
      ],
      back=[
          B('Whole-number division', '4.NBT.B.6', [
              sa('Find the quotient.\n150 ÷ 3', 'Quotient:'),
              mc('Which is equal to 96 ÷ 4?', ['24', '22', '26', '23']),
              tf('84 ÷ 6 = 14'),
              sa('Find the quotient.\n212 ÷ 4', 'Quotient:'),
              sa('Find the quotient.\n135 ÷ 5', 'Quotient:'),
          ]),
          B('Fraction as division', '5.NF.B.3', [
              sa('Write 5 ÷ 8 as a fraction.', 'Fraction:'),
              tf('{2/5} means the same as 2 ÷ 5.'),
              sa('Four friends share 3 sandwiches equally.\nHow much sandwich does each friend get?', 'Each friend gets:'),
              mc('Which division expression is equal to {7/8}?', ['7 ÷ 8', '8 ÷ 7', '7 × 8', '8 - 7']),
              sa('A 5-yard ribbon is cut into 6 equal pieces.\nHow long is each piece?', 'Length:'),
          ]),
          B('Meaning of "per" (the amount for each one)', '3.OA.A.2', [
              sa('12 apples are packed equally into 4 bags.\nHow many apples are in each bag?', 'Apples:'),
              tf('"5 miles per hour" means 5 miles for each 1 hour.'),
              mc('Which phrase means the same as "$2 per pound"?', ['$2 for each pound', '$2 for all of the pounds', '2 pounds for each dollar', '$2 more than a pound']),
              sa('A farmer puts 24 eggs into cartons, 6 eggs per carton.\nHow many cartons does the farmer fill?', 'Cartons:'),
              sa('Jen reads 40 pages in 5 days. She reads the same number of pages each day.\nHow many pages does she read per day?', 'Pages:'),
          ]),
      ],
      f1=B('Unit rates with fractions', '7.RP.A.1', [
          sa('Kim walks {3/4} mile in {1/4} hour.\nWhat is her speed in miles per hour?', 'Speed:'),
          sa('A painter paints {2/3} of a wall in {1/3} hour.\nAt this rate, how many walls can the painter paint per hour?', 'Walls per hour:'),
          sa('A snail crawls {5/6} foot in {1/3} minute.\nHow many feet does it crawl per minute?', 'Feet per minute:'),
          mc('A machine fills {3/4} of a tank in {1/2} hour.\nHow many tanks does it fill per hour?', ['1{1/2}', '{3/8}', '{1/4}', '1{1/4}']),
          sa('Leo mows {7/8} of an acre in {1/2} hour.\nHow many acres does he mow per hour?', 'Acres per hour:'),
      ]),
      f2=B('Rate of change of a linear function', '8.F.B.4', [
          sa('The table shows a linear function.\nWhat is the rate of change?', 'Rate of change:', fig=table([['x', '0', '1', '2', '3'], ['y', '5', '8', '11', '14']])),
          sa('A plumber charges a $40 fee plus $65 per hour.\nWrite a function for the cost C after h hours.', 'C ='),
          sa('A line passes through (2, 7) and (6, 19).\nWhat is the rate of change?', 'Rate of change:'),
          sa('A tank drains at a constant rate.\nWhat is the rate of change in gallons per minute?', 'Rate of change:',
             fig=table([['Minutes', '0', '5', '10'], ['Gallons', '200', '170', '140']])),
          mc('A taxi ride costs $3 plus $2.50 per mile.\nWhich function gives the cost y for a ride of x miles?', ['y = 2.5x + 3', 'y = 3x + 2.5', 'y = 5.5x', 'y = 2.5x - 3']),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.a (tables)
    S('6.RP.A.3.a', 'Find missing values in tables of equivalent ratios',
      main=[
          sa('The table shows equivalent ratios.\nFind the missing value.', 'Missing value:',
             fig=table([['Cups of juice', '2', '4', '6', '10'], ['Cups of water', '3', '6', '9', '?']])),
          sa('Paint is mixed in the same ratio in every column.\nFind the missing value.', 'Missing value:',
             fig=table([['Blue (cups)', '3', '6', '?', '15'], ['Yellow (cups)', '2', '4', '8', '10']])),
          sa('A swimmer keeps the same pace.\nFind the missing value.', 'Missing value:',
             fig=table([['Laps', '3', '6', '?', '15'], ['Minutes', '8', '16', '24', '40']])),
          mc('The table shows equivalent ratios.\nWhat is the missing value?', ['18', '16', '20', '35'],
             fig=table([['Tickets', '4', '8', '12', '?'], ['Cost ($)', '10', '20', '30', '45']])),
          sa('A recipe uses 5 cups of oats for every 2 cups of raisins.\nFind the missing values A and B.', ['A =', 'B ='],
             fig=table([['Oats (cups)', '5', '10', 'A', '25'], ['Raisins (cups)', '2', 'B', '6', '10']])),
      ],
      back=[
          B('Equivalent fractions', '4.NF.A.1', [
              tf('{2/3} is equivalent to {8/12}.'),
              sa('Find the missing number.\n{3/4} = {?/20}', 'Missing number:'),
              mc('Which fraction is equivalent to {5/6}?', ['{10/12}', '{10/11}', '{6/7}', '{5/12}']),
              tf('{4/5} is equivalent to {6/7}.'),
              sa('Find the missing number.\n{2/5} = {6/?}', 'Missing number:'),
          ]),
          B('Two related number patterns', '5.OA.B.3', [
              sa('Pattern A starts at 0 and adds 2.\nPattern B starts at 0 and adds 5.\nWhat is the 5th number in Pattern B?', 'Number:'),
              tf('Each number in Pattern B is 2 times the matching number in Pattern A.',
                 fig=table([['Pattern A (add 4)', '0', '4', '8', '12'], ['Pattern B (add 8)', '0', '8', '16', '24']])),
              sa('Pattern A starts at 0 and adds 7.\nPattern B starts at 0 and adds 14.\nWhat is the 4th number in Pattern A?', 'Number:'),
              mc('Pattern A: 0, 2, 4, 6, 8\nPattern B: 0, 6, 12, 18, 24\nHow does each number in Pattern B compare to the matching number in Pattern A?',
                 ['3 times as large', '4 more', '6 times as large', '2 times as large']),
              sa('Pattern A: 0, 1, 2, 3, ...\nPattern B: 0, 4, 8, 12, ...\nWhat number in Pattern B matches 5 in Pattern A?', 'Number:'),
          ]),
          B('Multiples of a number', '4.OA.B.4', [
              sa('List the first four multiples of 3.', 'Multiples:'),
              tf('40 is a multiple of 8.'),
              mc('Which number is a multiple of 5?', ['35', '32', '52', '48']),
              sa('What is the 6th multiple of 4?', 'Multiple:'),
              tf('27 is a multiple of 6.'),
          ]),
      ],
      f1=B('Constant of proportionality from a table', '7.RP.A.2.b', [
          sa('The table shows a proportional relationship.\nWhat is the constant of proportionality ({y/x})?', 'k =', fig=table([['x', '2', '5', '8'], ['y', '7', '17.5', '28']])),
          sa('The table shows the cost of cheese.\nWhat is the constant of proportionality in dollars per pound?', 'k =',
             fig=table([['Pounds', '3', '6', '9'], ['Cost ($)', '7.50', '15.00', '22.50']])),
          mc('The table shows a proportional relationship.\nWhat is the constant of proportionality?', ['{3/4}', '{4/3}', '3', '12'],
             fig=table([['x', '4', '8', '12'], ['y', '3', '6', '9']])),
          sa('The table shows how far a toy car rolls.\nWhat is the constant of proportionality in meters per second?', 'k =',
             fig=table([['Seconds', '2', '3', '5'], ['Meters', '1.2', '1.8', '3.0']])),
          tf('The constant of proportionality for the table is 6.', fig=table([['x', '1', '2', '4'], ['y', '6', '12', '24']])),
      ]),
      f2=B('Rate of change and initial value from a table', '8.F.B.4', [
          sa('The table shows a linear function.\nWhat are the rate of change and the initial value?', ['Rate of change:', 'Initial value:'],
             fig=table([['x', '0', '1', '2', '3'], ['y', '4', '7', '10', '13']])),
          sa('The table shows the height of a plant.\nWhat is the rate of change in cm per week?', 'Rate of change:',
             fig=table([['Weeks', '0', '2', '4'], ['Height (cm)', '6', '9', '12']])),
          mc('The table shows a linear function.\nWhich equation matches the table?', ['y = 2x + 5', 'y = 5x + 2', 'y = 2x', 'y = x + 5'],
             fig=table([['x', '0', '1', '2', '3'], ['y', '5', '7', '9', '11']])),
          sa('The table shows a linear function.\nWrite an equation for the function.', 'y =', fig=table([['x', '1', '2', '3', '4'], ['y', '9', '13', '17', '21']])),
          tf('The initial value of the function in the table is 20.', fig=table([['x', '0', '1', '2'], ['y', '20', '17', '14']])),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.a (plot)
    S('6.RP.A.3.a', 'Plot pairs of values from a ratio table on the coordinate plane',
      main=[
          plot('Plot the pairs of values from the table on the coordinate plane.', tplot([['Flour (cups)', '1', '2', '3', '4'], ['Sugar (cups)', '2', '4', '6', '8']], 5, 10)),
          plot('Plot the pairs of values from the table on the coordinate plane.', tplot([['Laps', '1', '2', '3'], ['Minutes', '10', '20', '30']], 4, 35, 5)),
          plot('Plot the pairs of values from the table on the coordinate plane.', tplot([['Boxes', '1', '2', '3', '4'], ['Pencils', '3', '6', '9', '12']], 5, 15, 3)),
          plot('Plot the pairs of values from the table on the coordinate plane.', tplot([['Hours', '2', '4', '6'], ['Dollars', '15', '30', '45']], 7, 50, 5)),
          plot('Plot the pairs of values from the table on the coordinate plane.', tplot([['Red tiles', '2', '4', '6'], ['White tiles', '5', '10', '15']], 7, 16, 1)),
      ],
      back=[
          B('Ordered pairs from two related patterns', '5.OA.B.3', [
              sa('Pattern A: 0, 1, 2, 3\nPattern B: 0, 3, 6, 9\nWrite the ordered pair formed by the 3rd numbers of the patterns.', 'Ordered pair:'),
              mc('Which ordered pairs come from the table?', ['(1, 5), (2, 10), (3, 15)', '(5, 1), (10, 2), (15, 3)', '(1, 2), (5, 10), (15, 3)', '(1, 10), (2, 5), (3, 15)'],
                 fig=table([['x', '1', '2', '3'], ['y', '5', '10', '15']])),
              tf('The table gives the ordered pair (4, 12).', fig=table([['x', '2', '4', '6'], ['y', '6', '12', '18']])),
              sa('Write the ordered pair from the last column of the table.', 'Ordered pair:', fig=table([['x', '1', '2', '3', '4'], ['y', '7', '14', '21', '28']])),
              tf('In an ordered pair, the first number comes from the top row of the table.', fig=table([['x', '1', '2'], ['y', '4', '8']])),
          ]),
          B('Axes and ordered pairs', '5.G.A.1', [
              tf('To plot (3, 7), start at (0, 0), move 3 units right, then 7 units up.'),
              mc('In the ordered pair (6, 2), which number tells how far to move up?', ['2', '6', '8', '4']),
              sa('What are the coordinates of the origin?', 'Origin:'),
              tf('(4, 9) and (9, 4) name the same point.'),
              mc('Which axis is vertical?', ['The y-axis', 'The x-axis']),
          ]),
          B('Plotting points in the first quadrant', '5.G.A.2', [
              plot('Plot and label point A at (3, 5).', q1(8, 8)),
              plot('Plot and label point B at (6, 2).', q1(8, 8)),
              plot('Plot and label point C at (0, 4).', q1(8, 8)),
              mc('Which point is at (2, 7)?', ['Point A', 'Point B', 'Point C', 'Point D'], fig=q1(8, 8, pts=[(2, 7, 'A'), (7, 2, 'B'), (2, 2, 'C'), (7, 7, 'D')])),
              plot('Plot and label point D at (5, 5).', q1(8, 8)),
          ]),
          B('Reading an axis marked by 2s, 3s, or 5s', '3.MD.B.3', [
              mc('On the y-axis, the grid lines are numbered 0, 5, 10, 15.\nWhere would 20 go?', ['One grid line above 15', 'Halfway between 10 and 15', 'At the 2nd grid line', 'At the 20th grid line']),
              tf('On an axis numbered 0, 3, 6, 9, the value 12 is one grid line above 9.'),
              sa('On an axis numbered 0, 2, 4, 6, 8, where does the value 5 go?', 'Answer:'),
              mc('An axis is numbered 0, 5, 10, 15, 20.\nHow many units does each grid line stand for?', ['5', '1', '10', '20']),
              tf('On an axis numbered by 10s, the value 35 is halfway between 30 and 40.'),
          ]),
      ],
      f1=B('Use a graph to decide whether a relationship is proportional', '7.RP.A.2.a', [
          tf('The graph shows a proportional relationship.', fig=q1(5, 10, ystep=2, square=False, pts=[(1, 2), (2, 4), (3, 6)], lines=[((0, 0), (5, 10))])),
          mc('Which statement about the graph is true?',
             ['It is not proportional because the line does not pass through (0, 0).', 'It is proportional because it is a straight line.',
              'It is proportional because y increases by 2.', 'It is not proportional because the points are not on a line.'],
             fig=q1(5, 10, ystep=2, square=False, pts=[(0, 2), (1, 4), (2, 6), (3, 8)], lines=[((0, 2), (4, 10))])),
          tf('The graph shows a proportional relationship.', fig=q1(4, 10, ystep=2, square=False, pts=[(0, 0), (1, 1), (2, 4), (3, 9)])),
          sa('The points (2, 5), (4, 10), and (6, 15) are graphed.\nDo they lie on a straight line through the origin? Write yes or no.', 'Answer:'),
          mc('Which set of points lies on a straight line through the origin?',
             ['(2, 3), (4, 6), (6, 9)', '(1, 3), (2, 4), (3, 5)', '(0, 2), (1, 4), (2, 6)', '(1, 1), (2, 4), (3, 9)']),
      ]),
      f2=B('Graph proportional relationships; interpret the slope', '8.EE.B.5', [
          sa('Graph y = 2x on the coordinate plane.\nWhat is the slope of the line?', 'Slope:', fig=q1(6, 12, ystep=2, square=False)),
          sa('Graph y = 1.5x on the coordinate plane.\nWhat is the slope of the line?', 'Slope:', fig=q1(6, 9, square=False)),
          sa('Water flows at 4 gallons per minute. Graph the gallons y after x minutes.\nWhat is the slope of the line?', 'Slope:',
             fig=q1(5, 20, ystep=4, square=False, xlabel='Minutes', ylabel='Gallons')),
          mc('The graph of a proportional relationship passes through (5, 2).\nWhat is the slope?', ['{2/5}', '{5/2}', '2', '5']),
          tf('The graph of y = 3x passes through (0, 0) and (2, 6), and its slope is 3.'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.a (compare)
    S('6.RP.A.3.a', 'Use tables of equivalent ratios to compare ratios',
      main=[
          mc('Lemonade A uses 2 cups of mix for every 5 cups of water. Lemonade B uses 3 cups of mix for every 7 cups of water.\nUse tables of equivalent ratios. Which lemonade has a stronger mix flavor?',
             ['Lemonade A', 'Lemonade B', 'They taste the same.'],
             fig=hrow(table([['A: Mix', '2', '4', '6'], ['A: Water', '5', '10', '15']], fs=0.85), table([['B: Mix', '3', '6', '9'], ['B: Water', '7', '14', '21']], fs=0.85), h=110)),
          mc('Class A has 4 boys for every 6 girls. Class B has 6 boys for every 9 girls.\nUse tables of equivalent ratios. Which statement is true?',
             ['The ratios are equivalent.', 'Class A has a greater ratio of boys to girls.', 'Class B has a greater ratio of boys to girls.']),
          mc('Runner A runs 3 laps in 10 minutes. Runner B runs 4 laps in 12 minutes.\nUse tables of equivalent ratios. Who runs faster?', ['Runner B', 'Runner A', 'They run at the same speed.']),
          mc('Paint A uses 1 part blue for every 3 parts white. Paint B uses 2 parts blue for every 5 parts white.\nUse tables of equivalent ratios. Which paint is a darker blue?', ['Paint B', 'Paint A', 'They are the same color.']),
          mc('Store A sells 5 pens for $3. Store B sells 8 pens for $5.\nUse tables of equivalent ratios. Which store gives more pens for the same amount of money?', ['Store A', 'Store B', 'They are the same.']),
      ],
      back=[
          B('Comparing fractions', '4.NF.A.2', [
              mc('Which fraction is greater?', ['{3/5}', '{3/7}']),
              tf('{5/8} > {4/8}'),
              mc('Which symbol makes the statement true?\n{2/3} ___ {3/4}', ['<', '>', '=']),
              tf('{1/3} = {2/6}'),
              mc('Which fraction is greatest?', ['{5/6}', '{2/3}', '{1/2}', '{7/12}']),
          ]),
          B('Common multiples', '4.OA.B.4', [
              sa('List the multiples of 5 and the multiples of 7 up to 40.\nWhich number is on both lists?', 'Common multiple:'),
              tf('30 is a multiple of both 5 and 6.'),
              mc('Which number is a multiple of both 3 and 4?', ['12', '9', '16', '14']),
              sa('Name a number that is a multiple of both 6 and 9.', 'Number:'),
              tf('20 is a multiple of both 4 and 8.'),
          ]),
          B('Equivalent fractions', '4.NF.A.1', [
              sa('Find the missing number.\n{2/5} = {?/35}', 'Missing number:'),
              tf('{3/7} = {6/14}'),
              mc('Which fraction is equivalent to {4/6}?', ['{6/9}', '{6/8}', '{8/10}', '{4/9}']),
              sa('Find the missing number.\n{1/3} = {5/?}', 'Missing number:'),
              tf('{3/10} = {9/20}'),
          ]),
      ],
      f1=B('Compare unit rates involving fractions', '7.RP.A.1', [
          mc('Ana walks {1/2} mile in {1/5} hour. Ben walks {3/4} mile in {1/3} hour.\nWho walks faster?', ['Ana', 'Ben', 'They walk at the same speed.']),
          mc('Mix A uses {2/3} cup of sugar per {1/2} cup of water. Mix B uses {3/4} cup of sugar per {2/3} cup of water.\nWhich mix is sweeter?', ['Mix A', 'Mix B', 'They are the same.']),
          sa('Pump A moves {3/8} gallon in {1/4} minute. Pump B moves {1/2} gallon in {1/2} minute.\nWhich pump is faster, and what is its rate in gallons per minute?', 'Answer:'),
          mc('Snail A crawls {1/6} foot in {1/2} minute. Snail B crawls {1/4} foot in {2/3} minute.\nWhich snail is faster?', ['Snail B', 'Snail A', 'They are the same.']),
          tf('{1/2} mile in {1/4} hour is a faster speed than {3/4} mile in {1/2} hour.'),
      ]),
      f2=B('Compare proportional relationships represented in different ways', '8.EE.B.5', [
          mc('Runner A\'s distance is shown in the graph. Runner B runs according to d = 0.15t, where d is kilometers and t is minutes.\nWhich runner is faster?', ['Runner A', 'Runner B', 'They are the same.'],
             fig=q1(10, 2, ystep=0.5, xstep=1, square=False, xlabel='Minutes', ylabel='Kilometers', pts=[(5, 1), (10, 2)], lines=[((0, 0), (10, 2))])),
          mc('Machine A: y = 45x bottles after x minutes. Machine B: the table shows 3 minutes → 120 bottles, 6 minutes → 240 bottles.\nWhich machine is faster?', ['Machine A', 'Machine B', 'They are the same.']),
          sa('Recipe A uses flour and sugar in the ratio y = 1.5x. Recipe B\'s graph passes through (0, 0) and (4, 7).\nWhich recipe uses more flour y per cup of sugar x?', 'Recipe:'),
          mc('Two proportional relationships: P is y = 6x. Q is a line through (0, 0) and (2, 13).\nWhich has the greater slope?', ['Q', 'P', 'They are the same.']),
          sa('Plan A: 20 minutes of calls cost $3.00. Plan B: c = 0.12m, where m is minutes.\nWhich plan costs less per minute?', 'Plan:'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.b (unit pricing)
    S('6.RP.A.3.b', 'Solve unit pricing problems',
      main=[
          sa('4 notebooks cost $10.\nAt this rate, how much do 7 notebooks cost?', 'Cost:'),
          sa('3 pounds of apples cost $5.40.\nAt this rate, how much do 5 pounds cost?', 'Cost:'),
          sa('6 cans of soup cost $7.50.\nAt this rate, how much do 10 cans cost?', 'Cost:'),
          mc('5 movie tickets cost $42.50.\nAt this rate, how much do 3 tickets cost?', ['$25.50', '$8.50', '$127.50', '$28.33']),
          sa('8 yards of fabric cost $36.\nAt this rate, how much do 3 yards cost?', 'Cost:'),
      ],
      back=[
          B('Dividing money amounts', '5.NBT.B.7', [
              sa('Find the quotient.\n$10.00 ÷ 4', 'Quotient:'),
              sa('Find the quotient.\n$5.40 ÷ 3', 'Quotient:'),
              mc('$7.50 ÷ 6 = ?', ['$1.25', '$1.20', '$0.80', '$12.50']),
              sa('Find the quotient.\n$36 ÷ 8', 'Quotient:'),
              tf('$42.50 ÷ 5 = $8.50'),
          ]),
          B('Multiplying money amounts', '5.NBT.B.7', [
              sa('Multiply.\n$2.50 × 7', 'Product:'),
              sa('Multiply.\n$1.80 × 5', 'Product:'),
              tf('$1.25 × 10 = $12.50'),
              mc('$4.50 × 3 = ?', ['$13.50', '$12.50', '$7.50', '$1.50']),
              sa('Multiply.\n$8.50 × 3', 'Product:'),
          ]),
          B('Finding the cost of one when each costs the same', '3.OA.A.2', [
              sa('4 toys cost $12 in all. Each toy costs the same.\nHow much does 1 toy cost?', 'Cost:'),
              sa('5 pencils cost 30 cents in all. Each pencil costs the same.\nHow much does 1 pencil cost?', 'Cost:'),
              tf('6 stickers cost 18 cents in all. Each costs the same, so 1 sticker costs 3 cents.'),
              mc('8 cards cost $16. Each card costs the same.\nHow much is 1 card?', ['$2', '$8', '$24', '$128']),
              sa('3 books cost $27 in all. Each book costs the same.\nHow much does 1 book cost?', 'Cost:'),
          ]),
      ],
      f1=B('Equations for proportional relationships', '7.RP.A.2.c', [
          sa('Apples cost $2.50 per pound.\nWrite an equation for the cost c of p pounds of apples.', 'Equation:'),
          sa('The table shows a proportional relationship.\nWrite an equation for the earnings e after h hours.', 'Equation:',
             fig=table([['Hours (h)', '2', '3', '5'], ['Earnings (e)', '36', '54', '90']])),
          mc('Pens cost $0.75 each.\nWhich equation gives the cost c of n pens?', ['c = 0.75n', 'n = 0.75c', 'c = n + 0.75', 'c = {n/0.75}']),
          sa('5 pounds of rice cost $8.\nWrite an equation for the cost c of p pounds of rice.', 'Equation:'),
          tf('Grapes cost $3.20 per pound. The equation c = 3.2p gives the cost c of p pounds.'),
      ]),
      f2=B('Build a linear function for a pricing situation', '8.F.B.4', [
          sa('A store charges $2.50 per pound of cherries plus a $4 box fee.\nWrite a function for the total cost C of p pounds.', 'C ='),
          mc('Tickets cost $12 each plus a $5 service fee per order.\nWhich function gives the cost C of t tickets?', ['C = 12t + 5', 'C = 5t + 12', 'C = 17t', 'C = 12t - 5']),
          sa('A delivery costs $6 plus $1.75 per mile.\nWhat are the rate of change and the initial value?', ['Rate of change:', 'Initial value:']),
          sa('The table shows the cost of a gym membership.\nWrite a function for the cost C after m months.', 'C =', fig=table([['Months (m)', '0', '1', '2', '3'], ['Cost (C)', '25', '55', '85', '115']])),
          tf('A function for "$3 per pound plus a $2 bag fee" is C = 3p + 2.'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.b (constant speed)
    S('6.RP.A.3.b', 'Solve constant speed problems',
      main=[
          sa('A runner runs 12 kilometers in 60 minutes at a constant speed.\nHow far does the runner go in 25 minutes?', 'Distance:'),
          sa('A train travels 180 miles in 3 hours at a constant speed.\nHow far does it travel in 5 hours?', 'Distance:'),
          sa('A cyclist rides 45 miles in 3 hours at a constant speed.\nHow long does it take to ride 75 miles?', 'Time:'),
          mc('A snail moves 18 cm in 6 minutes at a constant speed.\nHow far does it move in 20 minutes?', ['60 cm', '54 cm', '3 cm', '120 cm']),
          sa('A car travels 220 miles in 4 hours at a constant speed.\nHow long does it take to travel 385 miles?', 'Time:'),
      ],
      back=[
          B('Whole-number division', '4.NBT.B.6', [
              sa('Divide.\n180 ÷ 3', 'Quotient:'),
              sa('Divide.\n220 ÷ 4', 'Quotient:'),
              tf('385 ÷ 55 = 7'),
              mc('45 ÷ 3 = ?', ['15', '14', '12', '135']),
              sa('Divide.\n375 ÷ 5', 'Quotient:'),
          ]),
          B('Multiplying by a one-digit number', '4.NBT.B.5', [
              sa('Multiply.\n60 × 5', 'Product:'),
              sa('Multiply.\n15 × 7', 'Product:'),
              tf('55 × 4 = 220'),
              mc('48 × 6 = ?', ['288', '248', '54', '2,448']),
              sa('Multiply.\n125 × 3', 'Product:'),
          ]),
          B('Hours and minutes', '4.MD.A.1', [
              sa('How many minutes are in 3 hours?', 'Minutes:'),
              tf('There are 60 minutes in 1 hour.'),
              sa('Complete.\n5 hours = ___ minutes', 'Minutes:'),
              mc('Which is longer?', ['90 minutes', '1 hour', 'They are the same.']),
              sa('How many minutes are in {1/2} hour?', 'Minutes:'),
          ]),
      ],
      f1=B('Speed as a unit rate with fractions', '7.RP.A.1', [
          sa('A hiker walks {3/4} mile in {3/8} hour.\nWhat is the hiker\'s speed in miles per hour?', 'Speed:'),
          sa('A turtle crawls {1/5} mile in {1/2} hour.\nWhat is its speed in miles per hour?', 'Speed:'),
          mc('A boat travels 2{1/2} miles in {1/4} hour.\nWhat is its speed in miles per hour?', ['10', '{5/8}', '2{3/4}', '5']),
          sa('A skater glides {2/3} kilometer in {1/6} hour.\nWhat is the skater\'s speed in kilometers per hour?', 'Speed:'),
          tf('Going {1/2} mile in {1/10} hour is a speed of 5 miles per hour.'),
      ]),
      f2=B('Compare speeds from graphs and equations', '8.EE.B.5', [
          mc('Car A\'s distance is shown in the graph. Car B travels according to d = 55t.\nWhich car is faster?', ['Car A', 'Car B', 'They are the same.'],
             fig=q1(4, 240, ystep=40, square=False, xlabel='Hours', ylabel='Miles', pts=[(2, 120), (4, 240)], lines=[((0, 0), (4, 240))])),
          sa('Train A travels according to d = 80t. Train B\'s graph is a line through (0, 0) and (3, 210).\nWhich train is faster, and by how many miles per hour?', 'Answer:'),
          mc('Walker A: d = 3.5t. Walker B: the graph passes through (0, 0) and (2, 8).\nWho is faster?', ['Walker B', 'Walker A', 'They are the same.']),
          sa('What is the speed shown by the graph in miles per hour?', 'Speed:',
             fig=q1(5, 50, ystep=10, square=False, xlabel='Hours', ylabel='Miles', pts=[(1, 12), (2, 24), (3, 36), (4, 48)], lines=[((0, 0), (4, 48))])),
          tf('A line through (0, 0) and (5, 300) shows a greater speed than d = 65t.'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.b (compare unit rates)
    S('6.RP.A.3.b', 'Compare unit rates to find the better buy or the faster rate',
      main=[
          mc('Which is the better buy?\nA: 6 bottles of water for $4.50\nB: 10 bottles of water for $7.00', ABC),
          mc('Which is the better buy?\nA: a 12-ounce box of cereal for $3.60\nB: an 18-ounce box of cereal for $4.95', ABC),
          mc('Which store has the lower price per pound?\nA: 4 pounds of grapes for $7.00\nB: 3 pounds of grapes for $5.40', ABC),
          mc('Which is the better buy?\nA: 8 batteries for $10.00\nB: 12 batteries for $14.40', ABC),
          mc('Which printer is faster?\nA: 90 pages in 6 minutes\nB: 140 pages in 10 minutes', ABC),
      ],
      back=[
          B('Dividing money amounts', '5.NBT.B.7', [
              sa('Find the quotient.\n$4.50 ÷ 6', 'Quotient:'),
              sa('Find the quotient.\n$3.60 ÷ 12', 'Quotient:'),
              mc('$7.00 ÷ 10 = ?', ['$0.70', '$7.00', '$0.07', '$70.00']),
              sa('Find the quotient.\n$14.40 ÷ 12', 'Quotient:'),
              tf('$5.40 ÷ 3 = $1.80'),
          ]),
          B('Comparing decimals', '5.NBT.A.3.b', [
              mc('Which amount is less?', ['$0.70', '$0.75']),
              tf('0.8 > 0.75'),
              sa('Write >, <, or = to compare.\n0.275 ___ 0.3', 'Symbol:'),
              mc('Which number is greatest?', ['1.8', '1.75', '1.705', '1.075']),
              tf('1.25 < 1.2'),
          ]),
          B('Finding the amount for one', '3.OA.A.2', [
              sa('3 bags hold 21 oranges in all, the same number in each.\nHow many oranges are in 1 bag?', 'Oranges:'),
              sa('A worker packs 32 boxes in 4 hours, the same number each hour.\nHow many boxes per hour?', 'Boxes:'),
              tf('9 muffins cost $18 in all, the same price each, so 1 muffin costs $2.'),
              mc('40 pages are read in 8 days, the same number each day.\nHow many pages per day?', ['5', '32', '48', '320']),
              sa('6 packs hold 54 cards in all, the same number in each.\nHow many cards are in 1 pack?', 'Cards:'),
          ]),
      ],
      f1=B('Compare deals using percents', '7.RP.A.3', [
          mc('A $60 jacket is on sale. Which deal saves more money?', ['20% off', '$10 off', 'They save the same.']),
          mc('Which costs less after the discount?\nA: a $45 game at 30% off\nB: a $40 game at 20% off', ['A', 'B', 'They cost the same.']),
          sa('Store A sells a $80 bike at 15% off. Store B sells the same bike for $70.\nWhich store has the lower price, and by how much?', 'Answer:'),
          mc('Which is the better deal on a $120 phone?', ['25% off', '$25 off', 'They are the same.']),
          tf('A $50 item at 10% off costs the same as a $55 item at 20% off.'),
      ]),
      f2=B('Compare two functions represented in different ways', '8.F.A.2', [
          mc('Plan A costs y = 12x dollars for x months. Plan B is shown in the table.\nWhich plan has the greater rate of change?', ['Plan B', 'Plan A', 'They are the same.'],
             fig=table([['Months (x)', '2', '4', '6'], ['Cost (y)', '26', '52', '78']])),
          mc('Function A is y = 3x + 4. Function B is shown in the graph.\nWhich function has the greater rate of change?', ['Function B', 'Function A', 'They are the same.'],
             fig=q1(4, 12, ystep=2, square=False, pts=[(0, 1), (2, 9)], lines=[((0, 1), (2.75, 12))])),
          mc('Function A is shown in the table. Function B is y = -3x + 2.\nWhich function has the greater y-intercept?', ['Function A', 'Function B', 'They are the same.'],
             fig=table([['x', '0', '1', '2'], ['y', '5', '3', '1']])),
          sa('Phone plan A costs $30 plus $0.05 per text. Phone plan B is a line through (0, 20) and (100, 35).\nWhich plan has the greater cost per text?', 'Plan:'),
          tf('y = 4x + 1 has a greater rate of change than the function in the table.', fig=table([['x', '0', '1', '2'], ['y', '0', '5', '10']])),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.c (percent of a quantity)
    S('6.RP.A.3.c', 'Find a percent of a quantity as a rate per 100',
      main=[
          sa('What is 35% of 60?', 'Answer:'),
          sa('A jacket costs $60. The sales tax is 8%.\nHow much is the tax?', 'Tax:'),
          sa('A class has 25 students. 40% of the students walk to school.\nHow many students walk to school?', 'Students:'),
          mc('A $80 pair of shoes is 15% off.\nHow many dollars are taken off the price?', ['$12', '$15', '$68', '$1.20']),
          sa('A school has 450 students. 12% of them play in the band.\nHow many students play in the band?', 'Students:'),
      ],
      back=[
          B('Hundredths as decimals', '4.NF.C.6', [
              sa('Write {45/100} as a decimal.', 'Decimal:'),
              tf('0.07 = {7/100}'),
              mc('Which decimal is equal to {30/100}?', ['0.30', '3.0', '0.03', '30.0']),
              sa('Write 0.58 as a fraction with a denominator of 100.', 'Fraction:'),
              tf('{8/100} = 0.8'),
          ]),
          B('Tenths as hundredths', '4.NF.C.5', [
              sa('Find the missing number.\n{3/10} = {?/100}', 'Missing number:'),
              tf('{6/10} + {3/100} = {63/100}'),
              mc('Which fraction is equal to {7/10}?', ['{70/100}', '{7/100}', '{17/100}', '{10/70}']),
              sa('Add.\n{2/10} + {45/100}', 'Sum:'),
              tf('{9/10} = {90/100}'),
          ]),
          B('Fraction of a whole number', '5.NF.B.4.a', [
              sa('Multiply.\n{35/100} × 60', 'Product:'),
              sa('Find {1/4} of 60.', 'Answer:'),
              tf('{2/5} × 25 = 10'),
              mc('{3/4} × 20 = ?', ['15', '12', '16', '5']),
              sa('Find {7/10} of 50.', 'Answer:'),
          ]),
          B('Multiplying a decimal by a whole number', '5.NBT.B.7', [
              sa('Multiply.\n0.35 × 60', 'Product:'),
              sa('Multiply.\n0.08 × 60', 'Product:'),
              tf('0.12 × 450 = 54'),
              mc('0.4 × 25 = ?', ['10', '1', '100', '0.1']),
              sa('Multiply.\n0.15 × 80', 'Product:'),
          ]),
      ],
      f1=B('Multi-step percent problems', '7.RP.A.3', [
          sa('A meal costs $40. You leave a 15% tip.\nWhat is the total cost of the meal with the tip?', 'Total:'),
          sa('A pair of shoes costs $80. They are on sale for 25% off.\nWhat is the sale price?', 'Sale price:'),
          sa('A town\'s population grew from 2,000 to 2,300.\nWhat is the percent increase?', 'Percent increase:'),
          mc('A $50 game is marked up 20%. Then a 5% sales tax is added to the new price.\nWhat is the final cost?', ['$63.00', '$62.50', '$60.00', '$62.00']),
          sa('A salesperson earns a 6% commission. She sells $3,500 in products.\nHow much commission does she earn?', 'Commission:'),
      ]),
      f2=B('Build a linear function that uses a percent rate', '8.F.B.4', [
          sa('A salesperson earns $300 per week plus 5% of her sales s.\nWrite a function for her weekly earnings E.', 'E ='),
          mc('A server earns $40 per shift plus 18% of the food sales f.\nWhich function gives the earnings E?', ['E = 0.18f + 40', 'E = 40f + 0.18', 'E = 18f + 40', 'E = 0.18f - 40']),
          sa('An agent earns $500 per month plus 3% of her sales r.\nWhat are the rate of change and the initial value of this function?', ['Rate of change:', 'Initial value:']),
          sa('A delivery driver earns $60 per day plus 10% of the orders d delivered in dollars.\nWrite a function for the daily pay P.', 'P ='),
          tf('For E = 0.04s + 250, earnings increase by $0.04 for each $1 of sales s.'),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.c (find the whole)
    S('6.RP.A.3.c', 'Find the whole, given a part and the percent',
      main=[
          sa('12 is 25% of what number?', 'Answer:'),
          sa('A student answered 18 questions correctly. This was 90% of the questions on the test.\nHow many questions were on the test?', 'Questions:'),
          sa('Maria has saved $45. This is 30% of the cost of a bike.\nHow much does the bike cost?', 'Cost:'),
          mc('The tape diagram shows that 20% of a number is 14.\nWhat is the number?', ['70', '28', '34', '280'],
             fig=tape(dict(n=5, shade=1, seg=['14', '', '', '', ''], brace='100% = ?'))),
          sa('In a survey, 36 students chose pizza. This was 40% of the students surveyed.\nHow many students were surveyed?', 'Students:'),
      ],
      back=[
          B('Benchmark percents as fractions', '4.NF.A.1', [
              sa('Find the missing number.\n{25/100} = {1/?}', 'Missing number:'),
              sa('Find the missing number.\n{50/100} = {?/2}', 'Missing number:'),
              tf('{20/100} = {1/5}'),
              mc('Which fraction is equivalent to {75/100}?', ['{3/4}', '{7/10}', '{1/75}', '{4/3}']),
              sa('Find the missing number.\n{10/100} = {1/?}', 'Missing number:'),
          ]),
          B('Finding an unknown factor', '3.OA.A.4', [
              sa('What number goes in the box?\n□ × 4 = 36', '□ ='),
              sa('What number goes in the box?\n5 × □ = 45', '□ ='),
              tf('If 6 × □ = 42, then □ = 7.'),
              mc('□ × 8 = 56\nWhat number goes in the box?', ['7', '6', '8', '48']),
              sa('What number goes in the box?\n9 × □ = 63', '□ ='),
          ]),
          B('Dividing a whole number by a unit fraction', '5.NF.B.7.b', [
              sa('Divide.\n12 ÷ {1/4}', 'Quotient:'),
              sa('Divide.\n5 ÷ {1/3}', 'Quotient:'),
              tf('6 ÷ {1/2} = 3'),
              mc('How many fifths are in 3?', ['15', '8', '{3/5}', '5']),
              sa('Divide.\n8 ÷ {1/5}', 'Quotient:'),
          ]),
      ],
      f1=B('Percent problems: find the original amount', '7.RP.A.3', [
          sa('After a 20% discount, a jacket costs $48.\nWhat was the original price?', 'Original price:'),
          sa('A price increased by 10%. The new price is $55.\nWhat was the original price?', 'Original price:'),
          sa('The sales tax on an item was $3.60. The tax rate is 6%.\nWhat was the price before tax?', 'Price:'),
          mc('A town\'s population grew by 25% to 1,500 people.\nWhat was the population before the increase?', ['1,200', '1,125', '1,875', '1,475']),
          sa('A store marks up the price of a bike by 40%. The selling price is $210.\nHow much did the store pay for the bike?', 'Cost:'),
      ]),
      f2=B('Linear equations with decimal coefficients', '8.EE.C.7.b', [
          sa('Solve for x.\nx - 0.2x = 48', 'x ='),
          sa('Solve for x.\n0.4x + 12 = 0.1x + 30', 'x ='),
          sa('Solve for x.\n0.25(x + 40) = 30', 'x ='),
          mc('Which value of n solves the equation?\nn + 0.15n = 92', ['80', '78.2', '105.8', '92.15']),
          sa('Solve for y.\n2.5y - 7 = 1.5y + 3', 'y ='),
      ])),

    # ------------------------------------------------------------------ 6.RP.A.3.d
    S('6.RP.A.3.d', 'Convert measurement units using ratio reasoning',
      main=[
          sa('There are 3 feet in 1 yard.\nHow many feet are in 14 yards?', 'Feet:'),
          sa('There are 12 inches in 1 foot.\nHow many inches are in 4.5 feet?', 'Inches:'),
          sa('There are 16 ounces in 1 pound.\nHow many pounds are in 56 ounces?', 'Pounds:'),
          mc('A recipe needs 3 quarts of milk. There are 4 cups in 1 quart.\nHow many cups of milk are needed?', ['12 cups', '7 cups', '{3/4} cup', '1{1/3} cups']),
          sa('1 inch = 2.54 centimeters.\nA book is 10 inches tall. How many centimeters tall is it?', 'Centimeters:'),
      ],
      back=[
          B('Measurement equivalents', '4.MD.A.1', [
              sa('How many ounces are in 1 pound?', 'Ounces:'),
              tf('There are 12 inches in 1 yard.'),
              mc('How many cups are in 1 quart?', ['4', '2', '8', '16']),
              sa('How many grams are in 1 kilogram?', 'Grams:'),
              tf('1 meter = 100 centimeters'),
          ]),
          B('Multiplying and dividing by powers of 10', '5.NBT.A.2', [
              sa('Multiply.\n3.4 × 1,000', 'Product:'),
              sa('Multiply.\n2.54 × 10', 'Product:'),
              tf('0.6 × 1,000 = 60'),
              mc('450 ÷ 100 = ?', ['4.5', '45', '0.45', '45,000']),
              sa('Multiply.\n7.25 × 100', 'Product:'),
          ]),
          B('Multiplying a decimal by a whole number', '5.NBT.B.7', [
              sa('Multiply.\n4.5 × 12', 'Product:'),
              sa('Multiply.\n3.5 × 16', 'Product:'),
              tf('1.5 × 4 = 6'),
              mc('2.25 × 4 = ?', ['9', '8.1', '90', '0.9']),
              sa('Multiply.\n6 × 0.75', 'Product:'),
          ]),
      ],
      f1=B('Rates with fractions and unit conversions', '7.RP.A.1', [
          sa('A faucet drips {1/4} cup of water every {1/3} minute.\nHow many cups does it drip per hour?', 'Cups per hour:'),
          sa('A snail travels {3/8} foot every {1/2} minute.\nHow many feet does it travel per hour?', 'Feet per hour:'),
          mc('A plant grows {1/2} inch in {2/3} week.\nHow many inches does it grow per week?', ['{3/4}', '{1/3}', '1{1/3}', '{1/6}']),
          sa('A hose fills {3/4} gallon in {1/6} minute.\nHow many gallons does it fill per minute?', 'Gallons per minute:'),
          sa('A worker paints {2/5} of a room in {1/2} hour.\nHow many rooms can the worker paint in an 8-hour day?', 'Rooms:'),
      ]),
      f2=B('Convert units for very large and very small quantities', '8.EE.A.4', [
          sa('1 km = 10⁶ mm.\nWrite 3.2 × 10⁶ millimeters in kilometers.', 'Kilometers:'),
          sa('Earth is about 1.5 × 10⁸ km from the Sun. 1 km = 10³ m.\nHow many meters is this? Write the answer in scientific notation.', 'Meters:'),
          mc('A sheet of paper is about 1 × 10⁻⁴ meter thick.\nWhich unit is the most appropriate for this measurement?', ['Millimeters', 'Kilometers', 'Meters', 'Miles']),
          sa('A virus is 1.2 × 10⁻⁷ meter long. 1 nanometer = 10⁻⁹ meter.\nHow many nanometers long is the virus?', 'Nanometers:'),
          sa('A glacier moves 3 × 10⁻¹ meter per day. 1 m = 10² cm.\nHow many centimeters does it move per day?', 'Centimeters:'),
      ])),
]
