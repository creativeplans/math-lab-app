from qb import S, B, sa, mc, tf, nl, table, dot, prism, shape, poly, rect, hrow, plot
from common import fracs, fdot

BEAKERS = fdot(0, 0.625, {0.125: 2, 0.25: 3, 0.375: 1, 0.5: 2}, 8, 'Water in each beaker (liters)')
RIBBONS = fdot(0, 1, {0.25: 2, 0.5: 1, 0.75: 4, 1: 1}, 4, 'Ribbon length (yards)')
INSECTS = fdot(0, 1, {0.25: 1, 0.5: 3, 0.75: 2}, 4, 'Insect length (inches)')
GOALS = dot(0, 6, {1: 2, 2: 1, 3: 2, 5: 1}, xlabel='Goals scored')
PLANTS3 = dict(k='vstack', h=215, figs=[
    dot(2, 11, {3: 1, 4: 2, 5: 2, 6: 2, 7: 1}, xlabel='Plot A: plant heights (inches)'),
    dot(2, 11, {6: 1, 7: 2, 8: 2, 9: 2, 10: 1}, xlabel='Plot B: plant heights (inches)')])
PLANTS2 = dict(k='vstack', h=215, figs=[
    dot(2, 11, {3: 1, 4: 2, 5: 3, 6: 2, 7: 1}, xlabel='Plot A: plant heights (inches)'),
    dot(2, 11, {6: 1, 7: 2, 8: 3, 9: 2, 10: 1}, xlabel='Plot B: plant heights (inches)')])


def fline(vmin, vmax, d):
    """Empty number line marked in 1/d steps, for making line plots."""
    return nl(vmin, vmax, 1 / d, labels=fracs(vmin, vmax, d))


SETS = [
    # ------------------------------------------------------------------ 5.MD.A.1 (larger to smaller)
    S('5.MD.A.1', 'Convert from a larger unit to a smaller unit',
      main=[
          sa('How many inches are in 4{1/2} feet?', 'Inches:', key='54'),
          sa('How many ounces are in 3 pounds?', 'Ounces:', key='48'),
          mc('A track is 2.5 kilometers long.\nHow many meters is that?', ['2,500 m', '250 m', '25 m', '25,000 m']),
          sa('Convert.\n6 yards = ___ feet', 'Feet:', key='18'),
          sa('A jug holds 3 gallons.\nHow many quarts is that?', 'Quarts:', key='12'),
      ],
      back=[
          B('Relative sizes of measurement units', '4.MD.A.1', [
              sa('How many inches are in 1 foot?', 'Inches:', key='12'),
              tf('1 pound = 16 ounces', key=True),
              mc('How many quarts are in 1 gallon?', ['4', '2', '8', '16']),
              sa('How many meters are in 1 kilometer?', 'Meters:', key='1,000'),
              tf('1 yard = 12 inches', key=False),
          ]),
          B('Multiplying whole numbers', '4.NBT.B.5', [
              sa('Multiply.\n16 × 3', 'Product:', key='48'),
              sa('Multiply.\n1,000 × 7', 'Product:', key='7,000'),
              tf('3 × 36 = 98', key=False),
              mc('12 × 9 = ?', ['108', '96', '118', '21']),
              sa('Multiply.\n60 × 5', 'Product:', key='300'),
          ]),
          B('Multiply whole numbers by 10, 100, and 1,000', '4.NBT.A.1', [
              sa('Multiply.\n25 × 100', 'Product:', key='2,500'),
              tf('7 × 1,000 = 700', key=False),
              mc('42 × 10 = ?', ['420', '4,200', '42', '4.2']),
              sa('Multiply.\n16 × 1,000', 'Product:', key='16,000'),
              tf('3 × 100 is 10 times as much as 3 × 10.', key=True),
          ], num=4),
      ],
      f1=B('Use ratio reasoning to convert measurement units', '6.RP.A.3.d', [
          sa('There are 2.54 centimeters in 1 inch.\nHow many centimeters are in 5 inches?', 'Centimeters:', key='12.7'),
          sa('A car travels 3 miles every 4 minutes.\nAt this rate, how many miles does it travel in 1 hour?', 'Miles:', key='45'),
          mc('There are 3 feet in 1 yard.\nHow many yards are in 27 feet?', ['9', '81', '24', '30']),
          sa('1 kilogram is about 2.2 pounds.\nAbout how many pounds are in 15 kilograms?', 'Pounds:', key='33'),
          tf('If 1 cup = 8 fluid ounces, then 5 cups = 13 fluid ounces.', key=False),
      ]),
      f2=B('Unit rates with fractional quantities and different units', '7.RP.A.1', [
          sa('A snail moves 6 feet in {1/2} hour.\nWhat is its speed in feet per minute?', 'Speed:', key='1/5 foot per minute',
             note='0.2 foot per minute is also correct.'),
          sa('A cyclist rides {3/4} mile in 3 minutes.\nWhat is the speed in miles per hour?', 'Speed:', key='15 miles per hour'),
          mc('A faucet drips {1/2} cup every 5 minutes.\nHow many cups does it drip per hour?', ['6', '10', '{1/10}', '2{1/2}']),
          sa('A plant grows {1/4} inch per week.\nHow many inches does it grow in 52 weeks?', 'Inches:', key='13'),
          tf('Running 1{1/2} miles in 15 minutes is a speed of 6 miles per hour.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.A.1 (smaller to larger)
    S('5.MD.A.1', 'Convert from a smaller unit to a larger unit',
      main=[
          sa('Convert.\n30 inches = ___ feet', 'Feet:', key='2 1/2', note='2.5 is also correct.'),
          sa('Convert.\n750 milliliters = ___ liters', 'Liters:', key='0.75', note='3/4 is also correct.'),
          mc('A rope is 45 feet long.\nHow many yards is that?', ['15', '135', '42', '5']),
          sa('Convert.\n40 ounces = ___ pounds', 'Pounds:', key='2 1/2', note='2.5 is also correct.'),
          sa('Convert.\n1,350 grams = ___ kilograms', 'Kilograms:', key='1.35'),
      ],
      back=[
          B('Relative sizes of measurement units', '4.MD.A.1', [
              sa('How many milliliters are in 1 liter?', 'Milliliters:', key='1,000'),
              tf('1 kilogram = 1,000 grams', key=True),
              mc('How many feet are in 1 yard?', ['3', '12', '36', '10']),
              sa('How many cups are in 1 pint?', 'Cups:', key='2'),
              tf('1 foot = 10 inches', key=False),
          ]),
          B('Dividing by a one-digit number', '4.NBT.B.6', [
              sa('Divide.\n36 ÷ 3', 'Quotient:', key='12'),
              sa('Divide.\n64 ÷ 4', 'Quotient:', key='16'),
              tf('84 ÷ 7 = 14', key=False),
              mc('90 ÷ 3 = ?', ['30', '27', '33', '300']),
              sa('Divide.\n5,000 ÷ 5', 'Quotient:', key='1,000'),
          ]),
          B('Write tenths and hundredths as decimals', '4.NF.C.6', [
              sa('Write {75/100} as a decimal.', 'Decimal:', key='0.75'),
              tf('{5/10} = 0.5', key=True),
              mc('Which decimal is equal to {45/100}?', ['0.45', '4.5', '0.045', '45']),
              sa('Write 2{6/10} as a decimal.', 'Decimal:', key='2.6'),
              tf('{8/10} = 0.08', key=False),
          ], num=4),
      ],
      f1=B('Use ratio reasoning to convert measurement units', '6.RP.A.3.d', [
          sa('There are 12 inches in 1 foot.\nHow many feet are in 102 inches?', 'Feet:', key='8.5', note='8 1/2 is also correct.'),
          sa('There are 1,000 meters in 1 kilometer.\nHow many kilometers are in 4,200 meters?', 'Kilometers:', key='4.2'),
          mc('A recipe needs 10 cups of milk. There are 4 cups in 1 quart.\nHow many quarts of milk are needed?', ['2{1/2}', '40', '6', '14']),
          sa('A trail is 5 kilometers long. 1 kilometer is about 0.62 mile.\nAbout how many miles long is the trail?', 'Miles:', key='3.1'),
          tf('There are 60 minutes in 1 hour, so 150 minutes = 1{1/2} hours.', key=False),
      ]),
      f2=B('Equations for unit conversions', '7.RP.A.2.c', [
          sa('There are 2.54 centimeters in 1 inch.\nWrite an equation for the number of centimeters c in i inches.', 'Equation:', key='c = 2.54i'),
          sa('Write an equation for the number of feet f in y yards.', 'Equation:', key='f = 3y'),
          mc('Which equation converts k kilograms to g grams?', ['g = 1,000k', 'k = 1,000g', 'g = k + 1,000', 'g = k ÷ 1,000']),
          sa('Write an equation for the number of pounds p in z ounces.', 'Equation:', key='p = z/16',
             note='p = z ÷ 16 or p = (1/16)z is also correct.'),
          tf('The equation m = 60h gives the number of minutes m in h hours.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.A.1 (multistep)
    S('5.MD.A.1', 'Solve multistep problems that involve converting units',
      main=[
          sa('Ana has a 3-yard ribbon. She cuts off 4 feet.\nHow many feet of ribbon are left?', 'Feet:', key='5'),
          sa('A recipe needs 2 pounds of flour. Jo has 20 ounces.\nHow many more ounces does she need?', 'Ounces:', key='12'),
          mc('A runner ran 1.2 km and then 850 m.\nHow many meters did she run in all?', ['2,050 m', '862 m', '9,700 m', '1,050 m']),
          sa('A jug holds 2 liters of water. Six glasses of 250 milliliters each are poured from it.\nHow many milliliters are left in the jug?',
             'Milliliters:', key='500'),
          sa('A board is 8 feet long. It is cut into pieces that are 16 inches long.\nHow many pieces are there?', 'Pieces:', key='6'),
      ],
      back=[
          B('Word problems with measurement', '4.MD.A.2', [
              sa('A movie starts at 2:15 and lasts 1 hour 40 minutes.\nWhat time does it end?', 'Time:', key='3:55'),
              tf('3 quarters and 2 dimes make 85 cents.', key=False),
              mc('Jake has 2 meters of string. He uses 75 cm.\nHow many centimeters are left?', ['125 cm', '75 cm', '275 cm', '1.25 cm']),
              sa('A bag holds 3 kilograms of apples.\nHow many grams is that?', 'Grams:', key='3,000'),
              sa('Liz runs 400 meters four times.\nHow many meters does she run in all?', 'Meters:', key='1,600'),
          ]),
          B('Relative sizes of measurement units', '4.MD.A.1', [
              sa('How many ounces are in 2 pounds?', 'Ounces:', key='32'),
              tf('1 gallon = 4 quarts', key=True),
              mc('How many centimeters are in 1 meter?', ['100', '10', '1,000', '12']),
              sa('How many feet are in 3 yards?', 'Feet:', key='9'),
              tf('1 liter = 100 milliliters', key=False),
          ]),
      ],
      f1=B('Convert units to compare rates', '6.RP.A.3.d', [
          sa('A car uses 2 gallons of gas to drive 64 miles. There are 4 quarts in 1 gallon.\nHow many miles does the car drive per quart?', 'Miles:',
             key='8 miles per quart'),
          sa('Mo walks 3 kilometers in 40 minutes.\nAt this rate, how many meters does he walk per minute?', 'Meters per minute:', key='75'),
          mc('Fabric costs $6 per yard.\nHow much do 12 feet of fabric cost?', ['$24', '$72', '$18', '$2']),
          sa('A 24-ounce bag of rice costs $3. There are 16 ounces in 1 pound.\nWhat is the cost per pound?', 'Cost per pound:', key='$2'),
          tf('60 miles per hour is the same speed as 1 mile per minute.', key=True),
      ]),
      f2=B('Multistep ratio problems', '7.RP.A.3', [
          sa('A 2-liter bottle of soda costs $1.80. A 500-milliliter can costs $0.60.\nWhich is the better buy per liter?', 'Better buy:',
             key='The 2-liter bottle', note='Bottle: $0.90 per liter; can: $1.20 per liter.'),
          sa('A map scale is 1 cm : 2 km. Two towns are 7.5 cm apart on the map. A car drives 60 km per hour.\nHow many minutes does the drive take?',
             'Minutes:', key='15 minutes', note='7.5 cm = 15 km; 15 km at 60 km per hour takes 1/4 hour.'),
          mc('One gallon of paint covers 350 square feet.\nHow many gallons are needed to cover 1,400 square feet?', ['4', '5', '3', '1,050']),
          sa('A recipe for 4 people uses 600 grams of pasta.\nHow many kilograms are needed for 10 people?', 'Kilograms:', key='1.5 kg'),
          tf('At 5 miles per hour, a 2.5-mile walk takes 50 minutes.', key=False),
      ])),

    # ------------------------------------------------------------------ 5.MD.B.2 (make line plots)
    S('5.MD.B.2', 'Make a line plot of measurements in fractions of a unit',
      main=[
          plot('Pencil lengths (inches): 4{1/2}, 5, 4{1/2}, 5{1/4}, 4{3/4}, 5, 4{1/2}\nMake a line plot of the data.', fline(4, 5.5, 4),
               key='Line plot: 3 X\'s at 4 1/2, 1 X at 4 3/4, 2 X\'s at 5, 1 X at 5 1/4'),
          plot('Rainfall (inches): {1/4}, {1/2}, {1/8}, {1/4}, {3/8}, {1/4}, {1/2}\nMake a line plot of the data.', fline(0, 1, 8),
               key='Line plot: 1 X at 1/8, 3 X\'s at 1/4, 1 X at 3/8, 2 X\'s at 1/2'),
          plot('Apple weights (pounds): {3/4}, {1/2}, {3/4}, 1, {1/2}, {3/4}, {1/4}\nMake a line plot of the data.', fline(0, 1, 4),
               key='Line plot: 1 X at 1/4, 2 X\'s at 1/2, 3 X\'s at 3/4, 1 X at 1'),
          sa('Lengths (inches): {1/8}, {3/8}, {3/8}, {5/8}, {3/8}\nIn a line plot, how many X\'s are drawn at {3/8}?', 'X\'s:', key='3'),
          plot('Water in each bottle (liters): 1{1/2}, 2, 1{1/4}, 1{1/2}, 1{3/4}, 2, 1{1/2}\nMake a line plot of the data.', fline(1, 2, 4),
               key='Line plot: 1 X at 1 1/4, 3 X\'s at 1 1/2, 1 X at 1 3/4, 2 X\'s at 2'),
      ],
      back=[
          B('Reading a line plot with fractions', '4.MD.B.4', [
              sa('The line plot shows ribbon lengths.\nHow many ribbons are {3/4} yard long?', 'Ribbons:', key='4', fig=RIBBONS),
              tf('Two ribbons are {1/4} yard long.', key=True, fig=RIBBONS),
              mc('Which ribbon length is the most common?', ['{3/4} yard', '{1/4} yard', '{1/2} yard', '1 yard'], fig=RIBBONS),
              sa('How many ribbons were measured?', 'Ribbons:', key='8', fig=RIBBONS),
              sa('What is the difference between the longest and the shortest ribbon?', 'Difference:', key='3/4 yard', fig=RIBBONS),
          ]),
          B('Fractions on a number line', '3.NF.A.2', [
              sa('What fraction is at point P?', 'P =', key='3/8', fig=nl(0, 1, 0.125, pts=[(0.375, 'P')], labels={0: '0', 1: '1'})),
              tf('{2/4} and {1/2} are at the same point on a number line.', key=True),
              mc('Into how many equal parts is the space from 0 to 1 divided?', ['6', '5', '7', '1'],
                 fig=nl(0, 1, 1 / 6, labels={0: '0', 1: '1'})),
              sa('What number is at point Q?', 'Q =', key='1 1/4', note='5/4 is also correct.',
                 fig=nl(0, 2, 0.25, pts=[(1.25, 'Q')], labels={0: '0', 1: '1', 2: '2'})),
              tf('On a number line from 0 to 1 marked in eighths, {6/8} is one mark to the left of 1.', key=False),
          ]),
          B('Line plots of whole-number measurements', '2.MD.D.9', [
              sa('Lengths (inches): 5, 6, 6, 8, 6\nIn a line plot, how many X\'s are drawn at 6?', 'X\'s:', key='3'),
              tf('A line plot shows each measurement as a mark above a number line.', key=True),
              mc('Which number line would you use for a line plot of 3, 4, 4, 7?',
                 ['A number line from 0 to 8', 'A number line from 10 to 20', 'A number line from 0 to 3', 'A number line from 5 to 6']),
              plot('Lengths (cm): 2, 4, 4, 5\nMake a line plot of the data.', nl(0, 6, 1),
                   key='Line plot: 1 X at 2, 2 X\'s at 4, 1 X at 5'),
              sa('Lengths (feet): 9, 10, 10, 10, 12\nWhich length gets the most X\'s?', 'Length:', key='10 feet'),
          ]),
      ],
      f1=B('Display numerical data in a dot plot', '6.SP.B.4', [
          plot('Hours of sleep: 8, 9, 9, 10, 8, 9, 7\nMake a dot plot of the data.', nl(6, 11, 1),
               key='Dot plot: 1 dot at 7, 2 dots at 8, 3 dots at 9, 1 dot at 10'),
          plot('Number of siblings: 0, 1, 1, 2, 3, 1, 0, 2\nMake a dot plot of the data.', nl(0, 4, 1),
               key='Dot plot: 2 dots at 0, 3 dots at 1, 2 dots at 2, 1 dot at 3'),
          mc('Which number line fits a dot plot of 12, 15, 15, 18, 20?',
             ['A number line from 10 to 20', 'A number line from 0 to 5', 'A number line from 20 to 40', 'A number line from 15 to 18']),
          sa('Data: 4, 6, 6, 6, 7, 9\nIn a dot plot, how many dots go at 6?', 'Dots:', key='3'),
          tf('A dot plot shows every value in a data set.', key=True),
      ]),
      f2=B('Compare the difference in centers with the variability', '7.SP.B.3', [
          sa('Plot A has a mean of 5 inches and Plot B has a mean of 8 inches. Each plot has a mean absolute deviation (MAD) of 1 inch.\nThe difference in the means is how many times the MAD?',
             'Times the MAD:', key='3', fig=PLANTS3),
          tf('The difference in the means (3 inches) is 3 times the MAD, so the two distributions overlap only a little.', key=True, fig=PLANTS3),
          mc('Which statement compares the two plots correctly?',
             ['The centers differ by 3 times the MAD, so Plot B plants are noticeably taller.',
              'The centers differ by less than 1 MAD, so the plots are about the same.',
              'The plots cannot be compared because they show different plants.',
              'Plot A has much more variation than Plot B.'], fig=PLANTS3),
          sa('Two teams have mean heights of 150 cm and 156 cm. Each team has a MAD of 3 cm.\nThe difference in the means is how many times the MAD?',
             'Times the MAD:', key='2'),
          tf('Two data sets have means of 20 and 21, and each has a MAD of 4. The difference in the means is large compared with the variability.', key=False),
      ])),

    # ------------------------------------------------------------------ 5.MD.B.2 (operations on line plot data)
    S('5.MD.B.2', 'Use operations on fractions to solve problems with line plot data',
      main=[
          sa('The line plot shows the water in some beakers.\nWhat is the total amount of water?', 'Total:', key='2 3/8 liters', fig=BEAKERS),
          sa('If all of the water were shared equally among the beakers, how much would each beaker hold?', 'Liters:', key='19/64 liter',
             note='Total 2 3/8 liters ÷ 8 beakers.', fig=BEAKERS),
          mc('How much more water is in the fullest beaker than in the least full beaker?',
             ['{3/8} liter', '{1/2} liter', '{1/8} liter', '{5/8} liter'], fig=BEAKERS),
          sa('What is the total amount of water in the beakers that hold {1/4} liter each?', 'Total:', key='3/4 liter', fig=BEAKERS),
          tf('The beakers that hold {1/2} liter each contain 1 liter in all.', key=True, fig=BEAKERS),
      ],
      back=[
          B('Solving problems from a line plot with like denominators', '4.MD.B.4', [
              sa('How many insects are {1/2} inch long?', 'Insects:', key='3', fig=INSECTS),
              sa('What is the difference between the longest and the shortest insect?', 'Difference:', key='1/2 inch', fig=INSECTS),
              tf('The total length of the {3/4}-inch insects is 1{1/2} inches.', key=True, fig=INSECTS),
              mc('How many insects were measured?', ['6', '3', '5', '4'], fig=INSECTS),
              sa('What is the total length of the {1/2}-inch insects?', 'Total:', key='1 1/2 inches', fig=INSECTS),
          ]),
          B('Rename halves and fourths as eighths', '4.NF.A.1', [
              sa('Write {1/4} as eighths.', 'Fraction:', key='2/8'),
              tf('{1/2} = {4/8}', key=True),
              mc('Which fraction is equal to {3/4}?', ['{6/8}', '{3/8}', '{4/8}', '{7/8}']),
              sa('Find the missing number.\n{1/2} = {?/8}', 'Missing number:', key='4'),
              tf('{3/8} = {3/4}', key=False),
          ], num=4),
          B('Add fractions with like denominators', '4.NF.B.3.a', [
              sa('Add.\n{1/8} + {2/8}', 'Sum:', key='3/8'),
              tf('{3/8} + {3/8} = {6/16}', key=False),
              mc('{2/8} + {4/8} + {1/8} = ?', ['{7/8}', '{7/24}', '{6/8}', '1']),
              sa('Add.\n{5/8} + {3/8}', 'Sum:', key='1', note='8/8 is also correct.'),
              tf('{1/8} + {1/8} + {1/8} = {3/8}', key=True),
          ], num=5),
      ],
      f1=B('Find the mean of a data set', '6.SP.B.5.c', [
          sa('Find the mean.\n3, 5, 6, 8, 8', 'Mean:', key='6'),
          sa('Find the mean.\n12, 15, 21', 'Mean:', key='16'),
          mc('Four friends have 2, 4, 5, and 9 marbles. They share the marbles equally.\nHow many marbles does each friend get?', ['5', '4', '20', '4.5']),
          sa('The dot plot shows the goals scored in 6 games.\nWhat is the mean number of goals?', 'Mean:', key='2.5', note='2 1/2 is also correct.',
             fig=GOALS),
          tf('The mean of 4, 4, and 10 is 4.', key=False),
      ]),
      f2=B('Compare two populations using means', '7.SP.B.4', [
          sa('Random samples: Sample A has a mean of 15 minutes. Sample B has a mean of 22 minutes.\nHow much greater is the mean of Sample B?',
             'Difference:', key='7 minutes'),
          mc('Two random samples of plant heights have means of 18 cm and 24 cm. Both samples have similar variability.\nWhich conclusion is best?',
             ['Plants in the second population tend to be taller.', 'Plants in the first population tend to be taller.',
              'The populations are the same.', 'No conclusion is possible.']),
          tf('Comparing the means of random samples is one way to compare two populations.', key=True),
          sa('In random samples, Class X sleeps a mean of 7.5 hours and Class Y sleeps a mean of 8.25 hours.\nWhich class probably sleeps more?',
             'Class:', key='Class Y'),
          sa('A random sample of 30 students from School A spends a mean of 40 minutes on homework. A random sample of 30 students from School B spends a mean of 50 minutes. The samples have similar variability.\nWhat can you infer about all the students at the two schools?',
             'Inference:', key='Students at School B probably tend to spend more time on homework than students at School A.',
             note='Must draw a conclusion about the populations (all students at each school), for example that School B students typically spend '
                  'about 10 minutes more. Comparing only the two sample means, without a conclusion about the schools, is not enough.'),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.3.a
    S('5.MD.C.3.a', 'Understand a unit cube and a cubic unit of volume',
      main=[
          tf('A cube with edges that are 1 unit long is called a unit cube.', key=True),
          mc('What is the volume of a unit cube?', ['1 cubic unit', '1 square unit', '6 square units', '3 cubic units']),
          sa('What is the volume of a cube with edges that are 1 cm long?', 'Volume:', key='1 cubic centimeter'),
          mc('Which object has a volume closest to 1 cubic inch?', ['A sugar cube', 'A shoebox', 'A bathtub', 'A school bus']),
          tf('Volume measures the amount of space inside a solid figure.', key=True),
      ],
      back=[
          B('Unit squares and square units', '3.MD.C.5.a', [
              tf('A square with sides that are 1 unit long is called a unit square.', key=True),
              mc('What is the area of a unit square?', ['1 square unit', '4 square units', '1 cubic unit', '2 square units']),
              sa('How many unit squares cover a 3-by-3 square?', 'Unit squares:', key='9'),
              tf('Area is measured in cubic units.', key=False),
              sa('A square has sides that are 1 inch long.\nWhat is its area?', 'Area:', key='1 square inch'),
          ]),
          B('Faces, edges, and vertices of a cube', '2.G.A.1', [
              sa('How many faces does a cube have?', 'Faces:', key='6'),
              tf('All the faces of a cube are squares.', key=True),
              mc('How many edges does a cube have?', ['12', '6', '8', '4']),
              sa('How many vertices (corners) does a cube have?', 'Vertices:', key='8'),
              tf('All the edges of a cube are the same length.', key=True),
          ]),
      ],
      f1=B('Volume of cubes with fractional edge lengths', '6.G.A.2', [
          sa('What is the volume of a cube with edges that are {1/2} inch long?', 'Volume:', key='1/8 cubic inch'),
          sa('How many cubes with {1/2}-inch edges fit in a cube with 1-inch edges?', 'Cubes:', key='8'),
          mc('A cube has edges that are {1/3} foot long.\nWhat is its volume?', ['{1/27} cubic foot', '{1/9} cubic foot', '{1/3} cubic foot', '1 cubic foot']),
          sa('A box is packed with 16 cubes that each have {1/2}-cm edges.\nWhat is the volume of the box?', 'Volume:', key='2 cubic cm'),
          tf('Four cubes with {1/2}-unit edges have a total volume of 1 cubic unit.', key=False),
      ]),
      f2=B('Volume of right prisms', '7.G.B.6', [
          sa('A prism has a base area of 24 square cm and a height of 5 cm.\nWhat is its volume?', 'Volume:', key='120 cubic cm'),
          sa('A cube has edges that are 3 m long.\nWhat is its volume?', 'Volume:', key='27 cubic meters'),
          mc('A triangular prism has a triangle base with an area of 6 square inches. The prism is 10 inches long.\nWhat is its volume?',
             ['60 cubic inches', '16 cubic inches', '30 cubic inches', '600 cubic inches']),
          sa('A box is 2.5 cm by 4 cm by 6 cm.\nWhat is its volume?', 'Volume:', key='60 cubic cm'),
          tf('Volume is measured in cubic units.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.3.b
    S('5.MD.C.3.b', 'A solid packed with n unit cubes has a volume of n cubic units',
      main=[
          sa('A box is filled with 30 unit cubes with no gaps or overlaps.\nWhat is its volume?', 'Volume:', key='30 cubic units'),
          tf('If unit cubes fill a box but leave gaps, the number of cubes is less than the volume of the box.', key=True),
          mc('A solid is built from 18 unit cubes with no gaps or overlaps.\nWhat is its volume?',
             ['18 cubic units', '18 square units', '6 cubic units', '54 cubic units']),
          sa('Each cube is 1 cubic unit.\nWhat is the volume of the solid?', 'Volume:', key='12 cubic units', fig=prism(3, 2, 2, grid=True)),
          sa('A tower is made of 9 cubes stacked with no gaps. Each cube is 1 cubic inch.\nWhat is the volume of the tower?', 'Volume:',
             key='9 cubic inches'),
      ],
      back=[
          B('Measuring area by counting unit squares', '3.MD.C.6', [
              sa('A shape is covered by 12 unit squares with no gaps or overlaps.\nWhat is its area?', 'Area:', key='12 square units'),
              tf('Overlapping squares give a wrong count for area.', key=True),
              mc('A rectangle is covered by 20 unit squares.\nWhat is its area?', ['20 square units', '20 cubic units', '10 square units', '40 square units']),
              sa('Each square is 1 square cm. A rectangle is covered by 15 of these squares.\nWhat is its area?', 'Area:', key='15 square cm'),
              tf('Area can be found by counting the unit squares that cover a shape.', key=True),
          ]),
          B('Arrays and repeated addition', '2.OA.C.4', [
              sa('An array has 4 rows with 5 in each row.\nHow many are there in all?', 'Total:', key='20'),
              tf('3 rows of 5 make 8.', key=False),
              mc('Which equation matches an array with 2 rows of 5?', ['5 + 5 = 10', '2 + 5 = 7', '5 - 2 = 3', '2 + 2 = 4']),
              sa('An array has 5 rows with 3 in each row.\nHow many are there in all?', 'Total:', key='15'),
              sa('Write an addition equation for 3 rows of 4.', 'Equation:', key='4 + 4 + 4 = 12'),
          ]),
      ],
      f1=B('Pack prisms with fractional unit cubes', '6.G.A.2', [
          sa('A box is packed with cubes that have {1/2}-inch edges. It is 4 cubes long, 2 cubes wide, and 2 cubes tall.\nWhat is the volume of the box?',
             'Volume:', key='2 cubic inches'),
          sa('How many cubes with {1/4}-inch edges fill a cube with 1-inch edges?', 'Cubes:', key='64'),
          mc('A prism is packed with 27 cubes that each have {1/3}-foot edges.\nWhat is its volume?',
             ['1 cubic foot', '9 cubic feet', '3 cubic feet', '27 cubic feet']),
          sa('A box is 1{1/2} in. by 1 in. by {1/2} in.\nHow many cubes with {1/2}-inch edges fill it?', 'Cubes:', key='6'),
          tf('40 cubes with {1/2}-unit edges have a total volume of 20 cubic units.', key=False),
      ]),
      f2=B('Solve real-world volume problems', '7.G.B.6', [
          sa('A fish tank is 30 cm by 20 cm by 25 cm.\nWhat is its volume?', 'Volume:', key='15,000 cubic cm'),
          sa('A prism has a volume of 96 cubic inches and a base area of 12 square inches.\nWhat is its height?', 'Height:', key='8 inches'),
          mc('A triangular prism has a triangle base with a base of 4 m and a height of 3 m. The prism is 7 m long.\nWhat is its volume?',
             ['42 cubic meters', '84 cubic meters', '14 cubic meters', '21 cubic meters']),
          sa('A storage box is 1.5 m by 1 m by 0.8 m.\nWhat is its volume?', 'Volume:', key='1.2 cubic meters'),
          tf('Two prisms with the same base area and the same height have the same volume.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.4
    S('5.MD.C.4', 'Measure volume by counting unit cubes',
      main=[
          sa('Each cube is 1 cubic cm.\nWhat is the volume of the prism?', 'Volume:', key='24 cubic cm', fig=prism(4, 3, 2, grid=True)),
          sa('Each cube is 1 cubic inch.\nWhat is the volume of the prism?', 'Volume:', key='30 cubic inches', fig=prism(5, 2, 3, grid=True)),
          mc('Each cube is 1 cubic foot.\nWhat is the volume of the prism?', ['27 cubic feet', '9 cubic feet', '18 cubic feet', '54 cubic feet'],
             fig=prism(3, 3, 3, grid=True)),
          sa('A box is filled with number cubes. The bottom layer has 6 rows of 4 cubes, and there are 3 layers.\nWhat is the volume of the box, measured in number cubes?',
             'Volume:', key='72 number cubes'),
          tf('Each cube is 1 cubic cm. The volume of the prism is 16 cubic cm.', key=True, fig=prism(4, 2, 2, grid=True)),
      ],
      back=[
          B('Counting the squares in one layer', '3.MD.C.7.a', [
              sa('The bottom layer of a box has 5 rows of 4 cubes.\nHow many cubes are in the layer?', 'Cubes:', key='20'),
              tf('A layer with 3 rows of 6 cubes has 18 cubes.', key=True),
              mc('How many unit squares cover a 4-by-6 rectangle?', ['24', '10', '20', '46']),
              sa('A rectangle is tiled with 7 rows of 3 unit squares.\nHow many squares are there?', 'Squares:', key='21'),
              tf('The number of unit squares that tile a rectangle is its length times its width.', key=True),
          ]),
          B('Equal groups', '3.OA.A.1', [
              sa('There are 3 layers with 12 cubes in each layer.\nHow many cubes are there in all?', 'Cubes:', key='36'),
              tf('4 layers of 10 cubes is 14 cubes.', key=False),
              mc('Which expression shows 5 layers of 8 cubes?', ['5 × 8', '5 + 8', '8 - 5', '58']),
              sa('Multiply.\n6 × 9', 'Product:', key='54'),
              sa('There are 2 layers with 15 cubes in each layer.\nHow many cubes are there in all?', 'Cubes:', key='30'),
          ]),
      ],
      f1=B('Volume with fractional edge lengths', '6.G.A.2', [
          sa('A prism is 3 cubes long, 2 cubes wide, and 2 cubes tall. Each cube has {1/2}-inch edges.\nWhat is the volume of the prism?',
             'Volume:', key='1 1/2 cubic inches'),
          sa('A box is 2{1/2} cm by 2 cm by 1 cm.\nWhat is its volume?', 'Volume:', key='5 cubic cm'),
          mc('How many cubes with {1/2}-foot edges fill a box that is 2 ft by 1 ft by 1 ft?', ['16', '2', '8', '4']),
          sa('Find the volume of the prism.', 'Volume:', key='9 cubic inches', fig=prism(3, 1.5, 2, labels=('3 in.', '1{1/2} in.', '2 in.'))),
          tf('A cube with edges of 1{1/2} feet has a volume of 2{1/4} cubic feet.', key=False),
      ]),
      f2=B('Volume of right prisms', '7.G.B.6', [
          sa('A prism has a rectangular base that is 5 units by 4 units. It is 6 units tall.\nWhat is its volume?', 'Volume:', key='120 cubic units'),
          sa('A box has a volume of 120 cubic cm. Its base is 6 cm by 5 cm.\nWhat is its height?', 'Height:', key='4 cm'),
          mc('A prism has a base area of 15 square feet and a height of 4 feet.\nWhat is its volume?',
             ['60 cubic feet', '19 cubic feet', '30 cubic feet', '120 cubic feet']),
          sa('A triangular prism has a base area of 9 square cm and a length of 12 cm.\nWhat is its volume?', 'Volume:', key='108 cubic cm'),
          tf('A box that is 10 in. by 2 in. by 3 in. has a volume of 15 cubic inches.', key=False),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.5.a
    S('5.MD.C.5.a', 'Relate packing with unit cubes to the formulas V = l × w × h and V = b × h',
      main=[
          sa('A prism is packed with unit cubes. It is 5 cubes long, 3 cubes wide, and 4 layers tall.\nWhat is its volume?', 'Volume:',
             key='60 cubic units'),
          mc('The bottom layer of a prism has 12 unit cubes. There are 5 layers.\nWhich expression gives the volume?',
             ['12 × 5', '12 + 5', '12 × 12 × 5', '5 × 5']),
          tf('For a prism that is 4 by 3 by 2, (4 × 3) × 2 and 4 × (3 × 2) give the same volume.', key=True),
          sa('Each cube is 1 cubic unit.\nFind the volume by multiplying the area of the base by the height.', 'Volume:', key='36 cubic units',
             note='Base area 4 × 3 = 12; 12 × 3 = 36.', fig=prism(4, 3, 3, grid=True)),
          sa('A prism has a base area of 18 square units and a height of 4 units.\nWhat is its volume?', 'Volume:', key='72 cubic units'),
      ],
      back=[
          B('Area by tiling', '3.MD.C.7.a', [
              sa('A rectangle is tiled with unit squares in 3 rows of 4.\nWhat is its area?', 'Area:', key='12 square units'),
              tf('The area of a 5-by-2 rectangle is 10 square units.', key=True),
              mc('Which expression gives the area of a 6-by-3 rectangle?', ['6 × 3', '6 + 3', '2 × (6 + 3)', '6 - 3']),
              sa('How many unit squares tile a 9-by-2 rectangle?', 'Squares:', key='18'),
              tf('Tiling a rectangle and multiplying its side lengths give the same area.', key=True),
          ]),
          B('Multiplying three numbers in any grouping', '3.OA.B.5', [
              tf('(2 × 3) × 4 = 2 × 3 + 4', key=False),
              sa('Fill in the blank.\n(5 × 2) × 3 = 5 × (2 × ___)', 'Blank:', key='3'),
              mc('Which expression is equal to 4 × 5 × 2?', ['4 × 10', '9 × 2', '20 + 2', '4 + 5 + 2']),
              sa('Multiply.\n3 × 2 × 5', 'Product:', key='30'),
              tf('6 × (2 × 3) = 6 + 6', key=False),
          ]),
      ],
      f1=B('Apply the volume formulas with fractional edge lengths', '6.G.A.2', [
          sa('Use V = l × w × h to find V when l = 3{1/2} in., w = 2 in., and h = 1{1/2} in.', 'Volume:', key='10 1/2 cubic inches'),
          sa('Use V = b × h to find the volume of a prism with b = 6{1/4} square cm and h = 4 cm.', 'Volume:', key='25 cubic cm'),
          mc('A prism is packed with cubes that have edges {1/2} unit long: 6 cubes long, 4 cubes wide, and 2 cubes tall.\nWhich shows its volume?',
             ['3 × 2 × 1 = 6 cubic units', '6 × 4 × 2 = 48 cubic units', '6 + 4 + 2 = 12 cubic units', '{1/2} × 48 = 24 cubic units']),
          sa('A cube has edges that are {3/4} foot long.\nWhat is its volume?', 'Volume:', key='27/64 cubic foot'),
          tf('For a rectangular prism, V = l × w × h and V = b × h give the same volume.', key=True),
      ]),
      f2=B('Volume of right prisms using V = b × h', '7.G.B.6', [
          sa('A triangular prism has a triangle base with a base of 6 cm and a height of 4 cm. The prism is 10 cm long.\nWhat is its volume?',
             'Volume:', key='120 cubic cm'),
          sa('A prism has a trapezoid base with an area of 14 square inches. The prism is 5 inches tall.\nWhat is its volume?', 'Volume:',
             key='70 cubic inches'),
          mc('A prism has a volume of 84 cubic meters and a base area of 12 square meters.\nWhat is its height?', ['7 m', '72 m', '96 m', '1,008 m']),
          sa('A rectangular prism is 8 by 5 by 2.5.\nWhat is its volume?', 'Volume:', key='100 cubic units'),
          tf('V = b × h works for triangular prisms as well as rectangular prisms.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.5.b (apply)
    S('5.MD.C.5.b', 'Apply V = l × w × h and V = b × h to solve real-world problems',
      main=[
          sa('A fish tank is 24 inches long, 12 inches wide, and 15 inches tall.\nWhat is its volume?', 'Volume:', key='4,320 cubic inches'),
          sa('A sandbox has a base area of 30 square feet. It is filled with sand to a depth of 2 feet.\nHow much sand does it hold?', 'Volume:',
             key='60 cubic feet'),
          mc('A box is 9 cm long, 4 cm wide, and 5 cm tall.\nWhat is its volume?', ['180 cubic cm', '18 cubic cm', '36 cubic cm', '90 cubic cm']),
          sa('Find the volume of the prism.', 'Volume:', key='120 cubic meters', fig=prism(8, 3, 5, labels=('8 m', '3 m', '5 m'))),
          sa('A cube-shaped box has edges that are 7 inches long.\nWhat is its volume?', 'Volume:', key='343 cubic inches'),
      ],
      back=[
          B('Multiplying multi-digit numbers', '4.NBT.B.5', [
              sa('Multiply.\n24 × 12', 'Product:', key='288'),
              sa('Multiply.\n288 × 5', 'Product:', key='1,440'),
              tf('36 × 5 = 150', key=False),
              mc('49 × 7 = ?', ['343', '283', '353', '56']),
              sa('Multiply.\n15 × 24', 'Product:', key='360'),
          ]),
          B('The area of the base', '4.MD.A.3', [
              sa('A rectangle is 24 in. by 12 in.\nWhat is its area?', 'Area:', key='288 square inches'),
              tf('A 9-by-4 rectangle has an area of 36 square units.', key=True),
              mc('The base of a box is 8 m by 3 m.\nWhat is the area of the base?', ['24 square meters', '11 square meters', '22 square meters', '48 square meters']),
              sa('A square has sides that are 7 inches long.\nWhat is its area?', 'Area:', key='49 square inches'),
              sa('A rectangle has an area of 30 square feet and a length of 6 feet.\nWhat is its width?', 'Width:', key='5 feet'),
          ]),
      ],
      f1=B('Real-world volume with fractional edge lengths', '6.G.A.2', [
          sa('A box is 1{1/2} ft by 1 ft by {3/4} ft.\nWhat is its volume?', 'Volume:', key='1 1/8 cubic feet', note='9/8 is also correct.'),
          sa('A prism has a base area of 12{1/2} square inches and a height of 3 inches.\nWhat is its volume?', 'Volume:', key='37 1/2 cubic inches'),
          mc('A cube has edges that are 2{1/2} cm long.\nWhat is its volume?', ['15{5/8} cubic cm', '6{1/4} cubic cm', '7{1/2} cubic cm', '15 cubic cm']),
          sa('A drawer is 2 ft by 1{1/2} ft by {1/2} ft.\nWhat is its volume?', 'Volume:', key='1 1/2 cubic feet'),
          tf('A box that is 3 by {1/2} by 4 has a volume of 12 cubic units.', key=False),
      ]),
      f2=B('Real-world volume problems with right prisms', '7.G.B.6', [
          sa('A tent is a triangular prism. Its triangle has a base of 2 m and a height of 1.5 m. The tent is 3 m long.\nWhat is its volume?',
             'Volume:', key='4.5 cubic meters'),
          sa('A pool is 10 m long, 5 m wide, and 2 m deep. It is filled to {3/4} of its depth.\nHow much water is in the pool?', 'Volume:',
             key='75 cubic meters'),
          mc('A box has a volume of 360 cubic inches. Its base is 12 in. by 6 in.\nWhat is its height?', ['5 inches', '30 inches', '60 inches', '3 inches']),
          sa('A rectangular prism is 4.5 cm by 2 cm by 3 cm.\nWhat is its volume?', 'Volume:', key='27 cubic cm'),
          tf('A triangular prism with a base area of 8 square feet and a length of 5 feet holds 40 cubic feet.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.5.b (missing dimension)
    S('5.MD.C.5.b', 'Find a missing dimension when the volume is known',
      main=[
          sa('A box has a volume of 96 cubic inches. It is 6 inches long and 4 inches wide.\nHow tall is it?', 'Height:', key='4 inches'),
          sa('A prism has a volume of 150 cubic cm and a height of 6 cm.\nWhat is the area of its base?', 'Base area:', key='25 square cm'),
          mc('A tank holds 240 cubic feet. Its base is 8 feet by 5 feet.\nHow deep is the tank?', ['6 feet', '40 feet', '227 feet', '30 feet']),
          sa('A rectangular prism has a volume of 84 cubic meters. It is 7 m long and 4 m tall.\nHow wide is it?', 'Width:', key='3 m'),
          tf('A box with a volume of 60 cubic units and a base area of 12 square units is 5 units tall.', key=True),
      ],
      back=[
          B('Dividing by a one-digit number', '4.NBT.B.6', [
              sa('Divide.\n96 ÷ 4', 'Quotient:', key='24'),
              sa('Divide.\n150 ÷ 6', 'Quotient:', key='25'),
              tf('240 ÷ 8 = 3', key=False),
              mc('84 ÷ 7 = ?', ['12', '11', '13', '77']),
              sa('Divide.\n60 ÷ 5', 'Quotient:', key='12'),
          ]),
          B('Finding an unknown factor', '3.OA.A.4', [
              sa('What number goes in the box?\n6 × □ = 48', 'Number:', key='8'),
              tf('If □ × 5 = 35, then □ = 7.', key=True),
              mc('What number goes in the box?\n4 × □ = 36', ['9', '8', '32', '40']),
              sa('What number goes in the box?\n□ × 7 = 63', 'Number:', key='9'),
              tf('If 8 × □ = 56, then □ = 6.', key=False),
          ]),
      ],
      f1=B('Solve one-step equations of the form px = q', '6.EE.B.7', [
          sa('Solve for h.\n24h = 96', 'h =', key='4'),
          sa('Solve for b.\n6b = 150', 'b =', key='25'),
          mc('Solve for w.\n28w = 84', ['3', '56', '112', '2,352']),
          sa('A prism has a volume of 52.5 cubic cm and a base area of 15 square cm.\nWrite and solve an equation to find its height h.',
             'Equation and solution:', key='15h = 52.5; h = 3.5 cm'),
          tf('The solution of {3/4}x = 12 is x = 9.', key=False),
      ]),
      f2=B('Solve two-step equations', '7.EE.B.4.a', [
          sa('A box is 4 in. wide, 5 in. tall, and (x + 2) in. long. Its volume is 120 cubic inches.\nFind x.', 'x =', key='4',
             note='20(x + 2) = 120'),
          sa('Solve for x.\n6(x + 3) = 54', 'x =', key='6'),
          mc('Solve for h.\n12h + 8 = 68', ['5', '6.3', '4', '60']),
          sa('Two boxes have a total volume of 100 cubic feet. One box holds 40 cubic feet. The other has a base area of 12 square feet.\nWrite and solve an equation to find the height h of the other box.',
             'Equation and solution:', key='12h + 40 = 100; h = 5 feet'),
          tf('The solution of 3(x - 2) = 21 is x = 9.', key=True),
      ])),

    # ------------------------------------------------------------------ 5.MD.C.5.c
    S('5.MD.C.5.c', 'Find the volume of a figure made of two rectangular prisms',
      main=[
          sa('A figure is made of two rectangular prisms that do not overlap. One is 6 ft by 4 ft by 3 ft. The other is 2 ft by 4 ft by 5 ft.\nWhat is the total volume?',
             'Volume:', key='112 cubic feet'),
          sa('A figure is made of the two prisms shown, which do not overlap.\nWhat is the total volume?', 'Volume:', key='66 cubic cm',
             fig=hrow(prism(5, 3, 2, labels=('5 cm', '3 cm', '2 cm')), prism(3, 3, 4, labels=('3 cm', '3 cm', '4 cm')), h=200)),
          mc('An L-shaped step is made of a 4-by-2-by-1 prism with a 2-by-2-by-1 prism on top.\nWhat is its volume?',
             ['12 cubic units', '8 cubic units', '10 cubic units', '16 cubic units']),
          sa('A building is a 10 m by 8 m by 6 m prism with a 4 m by 8 m by 3 m prism attached to one side.\nWhat is the total volume?', 'Volume:',
             key='576 cubic meters'),
          tf('The volume of a figure made of two prisms that do not overlap is the sum of their volumes.', key=True),
      ],
      back=[
          B('Area of figures made of rectangles', '3.MD.C.7.d', [
              sa('A figure is split into two rectangles that do not overlap. Their areas are 15 square units and 8 square units.\nWhat is the area of the figure?', 'Area:',
                 key='23 square units'),
              tf('The area of a figure made of two non-overlapping parts is the sum of the areas of the parts.', key=True),
              mc('The figure is split into a 6-by-2 rectangle along the bottom and a rectangle above it.\nWhat is the area of the 6-by-2 rectangle?',
                 ['12 square units', '8 square units', '16 square units', '6 square units'],
                 fig=shape([poly([(0, 0), (6, 0), (6, 2), (2, 2), (2, 5), (0, 5)], ['6', '2', '4', '3', '2', '5'])])),
              mc('A figure is made of two squares that do not overlap. Their areas are 9 square units and 25 square units.\nTo find the area of the figure, what do you do with the two areas?',
                 ['Add them', 'Subtract them', 'Multiply them', 'Divide them']),
              sa('A square with an area of 4 square units is cut out of a rectangle with an area of 48 square units.\nWhat is the area of the part that is left?', 'Area:', key='44 square units'),
          ]),
          B('The area formula for rectangles', '4.MD.A.3', [
              sa('A rectangle is 6 units by 4 units.\nWhat is its area?', 'Area:', key='24 square units'),
              tf('A rectangle with an area of 32 square units and a length of 8 units has a width of 4 units.', key=True),
              mc('A rectangle is 10 m by 8 m.\nWhat is its area?', ['80 square meters', '18 square meters', '36 square meters', '800 square meters']),
              sa('A rectangle has an area of 45 square feet and a width of 5 feet.\nWhat is its length?', 'Length:', key='9 feet'),
              tf('A 4-by-8 rectangle has an area of 24 square units.', key=False),
          ], num=3),
      ],
      f1=B('Volume of composite figures with fractional edge lengths', '6.G.A.2', [
          sa('A figure is made of two prisms that do not overlap: 2{1/2} ft by 2 ft by 1 ft, and 1 ft by 2 ft by {1/2} ft.\nWhat is the total volume?',
             'Volume:', key='6 cubic feet'),
          sa('Two prisms are joined. One has a volume of 4{1/2} cubic inches. The other is 3 in. by 1 in. by {1/2} in.\nWhat is the total volume?',
             'Volume:', key='6 cubic inches'),
          mc('A step is made of a 3-by-1-by-{1/2} prism and a 1-by-1-by-{1/2} prism that do not overlap.\nWhat is its volume?',
             ['2 cubic units', '1{1/2} cubic units', '4 cubic units', '{1/2} cubic unit']),
          sa('A block that is 1 in. by 1 in. by 2{1/2} in. is cut out of a box that is 4 in. by 3 in. by 2{1/2} in.\nWhat volume is left?',
             'Volume:', key='27 1/2 cubic inches'),
          tf('A figure made of two cubes with {1/2}-foot edges has a volume of 1 cubic foot.', key=False),
      ]),
      f2=B('Volume of composite solids', '7.G.B.6', [
          sa('A figure is a 6-by-4-by-3 rectangular prism with a triangular prism on top. The triangle has a base of 4 and a height of 2, and the triangular prism is 6 long.\nWhat is the total volume?',
             'Volume:', key='96 cubic units'),
          sa('A concrete step is made of two prisms: 1.5 m by 0.5 m by 0.2 m and 1.5 m by 0.25 m by 0.4 m.\nWhat is the total volume?', 'Volume:',
             key='0.3 cubic meter'),
          mc('A 10-by-10-by-10 cube has a 2-by-2-by-10 hole cut all the way through it.\nWhat volume remains?', ['960 cubic units', '1,000 cubic units', '40 cubic units', '800 cubic units']),
          sa('A shed is a 3 m by 4 m by 2.5 m prism with a roof shaped like a triangular prism. The triangle has a base of 3 m and a height of 1 m, and the roof is 4 m long.\nWhat is the total volume?',
             'Volume:', key='36 cubic meters'),
          tf('The volume of a composite solid can be found by adding the volumes of its parts.', key=True),
      ])),
]
