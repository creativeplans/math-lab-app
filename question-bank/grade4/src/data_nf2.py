from qb import S, B, sa, mc, tf, nl, plot, draw_write
from common import bar, fline, hgrid

SETS = [
    # ------------------------------------------------------------------ 4.NF.B.4.a
    S('4.NF.B.4.a', 'Understand a fraction a/b as a multiple of 1/b',
      main=[
          sa('Write {7/8} as a whole number times {1/8}.', 'Expression:', key='7 × 1/8'),
          mc('Which equation shows {3/5} as a multiple of {1/5}?', ['{3/5} = 3 × {1/5}', '{3/5} = 5 × {1/3}', '{3/5} = 3 + {1/5}', '{3/5} = {1/5} ÷ 3']),
          tf('{9/4} = 9 × {1/4}', key=True),
          draw_write('Shade the tape diagram to show 4 × {1/6}.\nThen write the product as a fraction.', bar(6), 'Fraction:',
                     draw='4 of the 6 equal parts shaded', key='4/6', note='Grade both: 4 of the 6 parts shaded, and the fraction 4/6 (or 2/3).'),
          tf('{6/10} = 10 × {1/6}', key=False),
      ],
      back=[
          B('A fraction is a number of unit-fraction parts', '3.NF.A.1', [
              sa('How many {1/4}s make {3/4}?', 'Answer:', key='3'),
              tf('{5/8} is 5 parts of size {1/8}.', key=True),
              mc('What fraction is 4 parts of size {1/6}?', ['{4/6}', '{6/4}', '{1/6}', '{4/8}']),
              sa('What fraction of the bar is shaded?', 'Fraction:', key='5/8', fig=bar(8, 5)),
              tf('{2/3} is 3 parts of size {1/2}.', key=False),
          ]),
          B('Products as equal groups', '3.OA.A.1', [
              sa('What is the total in 5 groups of 3?', 'Total:', key='15'),
              tf('4 × 6 can mean 4 groups of 6.', key=True),
              mc('Which expression shows 7 groups of 2?', ['7 × 2', '7 + 2', '7 - 2', '2 ÷ 7']),
              sa('Write a multiplication expression for 3 groups of 9.', 'Expression:', key='3 × 9'),
              tf('6 × 3 means 6 + 3.', key=False),
          ]),
      ],
      f1=B('Find a fraction of a fractional amount', '5.NF.B.4.a', [
          sa('Multiply.\n{2/3} × {3/4}', 'Product:', key='6/12', note='1/2 is also correct.'),
          tf('{1/4} of {4/5} is {1/5}.', key=True),
          mc('What is {2/5} of {5/6}?', ['{1/3}', '{7/11}', '{12/25}', '{25/12}']),
          sa('What is {1/3} of {3/4} yard? Think of {3/4} as 3 parts of size {1/4}.', 'Answer:', key='1/4 yard',
             note='3/12 yard is also correct. Splitting 3/4 into 3 equal parts gives parts of 1/4.'),
          tf('{1/2} × {2/3} = {3/5}', key=False),
      ]),
      f2=B('Divide a fraction by a unit fraction', '6.NS.A.1', [
          sa('How many {1/5}s are in {4/5}?', 'Answer:', key='4'),
          tf('{7/8} ÷ {1/8} = 7', key=True),
          mc('Divide.\n{3/4} ÷ {1/8}', ['6', '{3/32}', '3', '{1/6}']),
          sa('Divide.\n2 ÷ {1/3}', 'Quotient:', key='6'),
          tf('{2/3} ÷ {1/3} = {2/9}', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.B.4.b
    S('4.NF.B.4.b', 'Multiply a fraction by a whole number: n × (a/b) = (n × a)/b',
      main=[
          sa('Multiply.\n4 × {2/3}', 'Product:', key='8/3', note='2 2/3 is also correct.'),
          sa('Multiply.\n5 × {3/8}', 'Product:', key='15/8', note='1 7/8 is also correct.'),
          mc('Which is equal to 3 × {4/5}?', ['12 × {1/5}', '7 × {1/5}', '{12/15}', '3 × {1/5}']),
          tf('6 × {2/12} = {12/72}', key=False),
          sa('Explain why 2 × {3/10} = 6 × {1/10}.', ['Explanation:', ''],
             key='3/10 is 3 × 1/10, so 2 groups of 3/10 are 2 × 3 = 6 copies of 1/10.',
             note='Must use 3/10 = 3 × 1/10 (or a model with tenths) to show that 2 groups of 3 tenths is 6 tenths.'),
      ],
      back=[
          B('Multiply three numbers in any grouping', '3.OA.B.5', [
              tf('(2 × 3) × 5 = 2 × (3 × 5)', key=True),
              sa('Fill in the blank.\n4 × (2 × 3) = (4 × 2) × ___', 'Blank:', key='3'),
              mc('Which is equal to 3 × 2 × 4?', ['6 × 4', '5 × 4', '3 + 8', '9 × 4']),
              sa('Multiply.\n2 × 4 × 5', 'Product:', key='40'),
              tf('(3 × 2) × 4 = 3 + 2 + 4', key=False),
          ]),
          B('A fraction is a number of unit-fraction parts', '3.NF.A.1', [
              sa('How many {1/3}s make {2/3}?', 'Answer:', key='2'),
              tf('{6/8} is 6 parts of size {1/8}.', key=True),
              mc('What fraction is 3 parts of size {1/4}?', ['{3/4}', '{4/3}', '{1/4}', '{3/8}']),
              sa('What fraction is 5 parts of size {1/6}?', 'Fraction:', key='5/6'),
              tf('{3/6} is 6 parts of size {1/3}.', key=False),
          ]),
      ],
      f1=B('Multiply a fraction by a fraction', '5.NF.B.4.a', [
          sa('Multiply.\n{2/3} × {3/5}', 'Product:', key='2/5', note='6/15 is also correct.'),
          tf('{1/2} × {3/4} = {3/8}', key=True),
          mc('Multiply.\n{3/4} × {2/5}', ['{3/10}', '{5/9}', '{6/9}', '{5/20}']),
          sa('What is {1/3} of {6/7}?', 'Answer:', key='2/7', note='6/21 is also correct.'),
          tf('{2/5} × {1/2} = {3/7}', key=False),
      ]),
      f2=B('Divide a fraction by a fraction', '6.NS.A.1', [
          sa('Divide.\n{2/3} ÷ {1/6}', 'Quotient:', key='4'),
          tf('{3/4} ÷ {3/8} = 2', key=True),
          mc('Divide.\n{4/5} ÷ {2/5}', ['2', '{8/25}', '{1/2}', '4']),
          sa('Divide.\n{5/6} ÷ {1/3}', 'Quotient:', key='2 1/2', note='5/2 is also correct.'),
          tf('{1/2} ÷ {1/8} = {1/16}', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.B.4.c
    S('4.NF.B.4.c', 'Solve word problems by multiplying a fraction by a whole number',
      main=[
          sa('Each glass holds {3/4} cup of milk.\nHow much milk is in 6 glasses?', 'Milk:', key='18/4 cups',
             note='4 2/4, 4 1/2, and 9/2 cups are also correct.'),
          sa('A snail crawls {2/5} meter each hour.\nHow far does it crawl in 4 hours?', 'Distance:', key='8/5 meters', note='1 3/5 meters is also correct.'),
          mc('Each of 3 friends eats {5/8} of a sandwich.\nHow many sandwiches do they eat in all?', ['1{7/8}', '{15/24}', '3{5/8}', '{8/8}']),
          tf('A runner runs {7/10} mile each day for 5 days. She runs 3{5/10} miles in all.', key=True),
          sa('A recipe uses {2/3} cup of flour for each batch.\nHow much flour do 5 batches use, and between which two whole numbers is that amount?',
             ['Flour:', 'Between:'], key='10/3 cups (3 1/3 cups); between 3 and 4', note='Both parts are required.'),
      ],
      back=[
          B('Equal-groups word problems within 100', '3.OA.A.3', [
              sa('Each bag holds 6 oranges.\nHow many oranges are in 7 bags?', 'Oranges:', key='42'),
              tf('9 boxes with 4 pens in each box hold 36 pens.', key=True),
              mc('A spider has 8 legs.\nHow many legs do 5 spiders have?', ['40', '13', '45', '35']),
              sa('Each row has 9 seats.\nHow many seats are in 3 rows?', 'Seats:', key='27'),
              tf('6 packs of 5 cards is 11 cards.', key=False),
          ]),
          B('Jump by a unit fraction on a number line', '3.NF.A.2', [
              sa('Start at 0 and make 3 jumps of {1/4} on the number line.\nWhere do you land?', 'Answer:', key='3/4', fig=fline(0, 1, 4)),
              tf('5 jumps of {1/8} from 0 land on {5/8}.', key=True),
              mc('How many jumps of {1/3} from 0 reach 1?', ['3', '1', '2', '6']),
              sa('Where do 4 jumps of {1/6} from 0 land?', 'Answer:', key='4/6', note='2/3 is also correct.'),
              tf('2 jumps of {1/2} from 0 land on {2/4}.', key=False),
          ]),
      ],
      f1=B('Solve real-world problems by multiplying fractions and mixed numbers', '5.NF.B.6', [
          sa('A recipe uses {3/4} cup of oats per batch.\nHow many cups of oats are in 2{1/2} batches?', 'Cups:', key='1 7/8 cups'),
          sa('A garden is 7{1/2} m long. {3/5} of its length is planted.\nHow many meters are planted?', 'Meters:', key='4 1/2 m',
             note='9/2 m and 4.5 m are also correct.'),
          mc('A bottle holds 1{1/2} liters. It is {2/3} full.\nHow many liters are in the bottle?', ['1 liter', '{3/4} liter', '2{1/6} liters', '{1/2} liter']),
          tf('A board is 4{1/2} feet long. Half of the board is 2{1/4} feet long.', key=True),
          tf('{2/3} of a 4{1/2}-mile trail is 2 miles.', key=False),
      ]),
      f2=B('Find a percent of a quantity', '6.RP.A.3.c', [
          sa('What is 25% of 36?', 'Answer:', key='9'),
          tf('50% of 18 is 9.', key=True),
          mc('What is 75% of 40?', ['30', '10', '35', '25']),
          sa('A class has 20 students. 40% of them walk to school.\nHow many students walk?', 'Students:', key='8'),
          tf('10% of 70 is 10.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.C.5
    S('4.NF.C.5', 'Write a fraction with denominator 10 as an equivalent fraction with denominator 100',
      main=[
          sa('Write {6/10} as an equivalent fraction with a denominator of 100.', 'Fraction:', key='60/100'),
          sa('Find the missing number.\n{4/10} = {?/100}', 'Missing number:', key='40'),
          mc('Which fraction is equivalent to {9/10}?', ['{90/100}', '{9/100}', '{19/100}', '{99/100}']),
          tf('{50/100} = {5/100}', key=False),
          sa('Write {70/100} as an equivalent fraction with a denominator of 10.', 'Fraction:', key='7/10'),
      ],
      back=[
          B('Simple equivalent fractions', '3.NF.A.3.b', [
              sa('Find the missing number.\n{1/2} = {?/8}', 'Missing number:', key='4'),
              tf('{2/4} = {4/8}', key=True),
              mc('Which fraction is equal to {2/3}?', ['{4/6}', '{2/6}', '{3/2}', '{3/6}']),
              sa('Find the missing number.\n{3/4} = {6/?}', 'Missing number:', key='8'),
              tf('{1/3} = {3/6}', key=False),
          ]),
          B('A hundred is ten tens', '2.NBT.A.1.a', [
              sa('How many tens are in 100?', 'Tens:', key='10'),
              tf('10 tens make 1 hundred.', key=True),
              mc('A hundred flat is cut into rods of ten. How many rods are there?', ['10', '100', '1', '20']),
              sa('Mia has 9 bundles of ten straws.\nHow many more bundles of ten does she need to make 1 hundred?', 'Bundles:', key='1'),
              tf('10 tens make 1,000.', key=False),
          ]),
      ],
      f1=B('Add decimals to hundredths', '5.NBT.B.7', [
          sa('Add.\n0.6 + 0.25', 'Sum:', key='0.85'),
          tf('0.3 + 0.07 = 0.37', key=True),
          mc('Add.\n0.4 + 0.58', ['0.98', '0.62', '0.098', '9.8']),
          sa('Add.\n1.7 + 0.15', 'Sum:', key='1.85'),
          tf('0.5 + 0.05 = 0.10', key=False),
      ]),
      f2=B('Write tenths and hundredths as percents', '6.RP.A.3.c', [
          sa('Write {6/10} as a percent.', 'Percent:', key='60%'),
          tf('{45/100} = 45%', key=True),
          mc('Which percent is equal to {3/10}?', ['30%', '3%', '0.3%', '13%']),
          sa('Write 8% as a fraction with a denominator of 100.', 'Fraction:', key='8/100'),
          tf('{9/10} = 9%', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.C.5 (add) — added in 2.0.0
    S('4.NF.C.5', 'Add two fractions with denominators 10 and 100', num=67,
      main=[
          sa('Add.\n{2/10} + {45/100}', 'Sum:', key='65/100'),
          mc('{7/10} + {9/100} = ?', ['{79/100}', '{16/100}', '{16/110}', '{79/10}']),
          sa('Add.\n{8/10} + {15/100}', 'Sum:', key='95/100'),
          tf('{3/10} + {4/100} = {34/100}', key=True),
          sa('A jar is {4/10} full of sand. Ali pours in another {35/100} of a jar.\nWhat fraction of the jar is full now?', 'Fraction:', key='75/100',
             note='3/4 is also correct.'),
      ],
      back=[
          B('Add tens and ones within 100', '2.NBT.B.5', [
              sa('Add.\n20 + 45', 'Sum:', key='65'),
              tf('70 + 9 = 79', key=True),
              mc('80 + 15 = ?', ['95', '23', '815', '85']),
              sa('Add.\n30 + 34', 'Sum:', key='64'),
              tf('40 + 35 = 85', key=False),
          ]),
          B('Simple equivalent fractions', '3.NF.A.3.b', [
              sa('Find the missing number.\n{1/2} = {?/4}', 'Missing number:', key='2'),
              tf('{3/6} = {1/2}', key=True),
              mc('Which fraction is equal to {1/4}?', ['{2/8}', '{1/8}', '{4/1}', '{2/4}']),
              sa('Find the missing number.\n{2/3} = {?/6}', 'Missing number:', key='4'),
              tf('{2/8} = {1/2}', key=False),
          ]),
      ],
      f1=B('Add decimals with tenths and hundredths in context', '5.NBT.B.7', [
          sa('A beetle crawls 0.4 meter and then 0.35 meter.\nHow far does it crawl in all?', 'Distance:', key='0.75 meter'),
          tf('0.8 + 0.12 = 0.92', key=True),
          mc('A cup holds 0.25 liter of water. Ty pours in 0.5 liter more.\nHow much water is in the cup now?',
             ['0.75 liter', '0.30 liter', '0.075 liter', '7.5 liters']),
          sa('Add.\n2.6 + 0.08', 'Sum:', key='2.68'),
          tf('0.9 + 0.09 = 0.18', key=False),
      ]),
      f2=B('Add multi-digit decimals with the standard algorithm', '6.NS.B.3', [
          sa('Add.\n12.6 + 3.45', 'Sum:', key='16.05'),
          tf('7.08 + 2.9 = 9.98', key=True),
          mc('Add.\n0.75 + 18.3', ['19.05', '18.105', '19.8', '0.933']),
          sa('Add.\n45.2 + 6.875', 'Sum:', key='52.075'),
          tf('3.4 + 1.25 = 4.59', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.C.6 (notation)
    S('4.NF.C.6', 'Write fractions with denominators 10 or 100 as decimals',
      main=[
          sa('Write {47/100} as a decimal.', 'Decimal:', key='0.47'),
          sa('Write 0.8 as a fraction with a denominator of 10.', 'Fraction:', key='8/10'),
          mc('What decimal does the shaded part of the grid show?', ['0.36', '3.6', '0.036', '36'], fig=hgrid(36)),
          tf('{5/100} = 0.5', key=False),
          sa('A ribbon is {93/100} meter long.\nWrite its length as a decimal.', 'Length:', key='0.93 meter'),
      ],
      back=[
          B('Dimes, pennies, and dollars', '2.MD.C.8', [
              sa('How many cents are 3 dimes and 4 pennies?', 'Cents:', key='34 cents'),
              tf('10 dimes are worth 1 dollar.', key=True),
              mc('Which coins make 25 cents?', ['2 dimes and 5 pennies', '2 dimes and 2 pennies', '1 dime and 5 pennies', '25 dimes']),
              sa('How many pennies make 1 dollar?', 'Pennies:', key='100'),
              tf('7 dimes are worth 7 cents.', key=False),
          ]),
          B('Hundreds, tens, and ones', '2.NBT.A.1', [
              sa('How many hundreds, tens, and ones are in 245?', 'Answer:', key='2 hundreds, 4 tens, 5 ones'),
              tf('In 307, the 0 means 0 tens.', key=True),
              mc('What is the value of the 5 in 452?', ['50', '5', '500', '45']),
              sa('Write the number that is 6 tens and 2 ones.', 'Number:', key='62'),
              tf('In 180, the 8 means 8 ones.', key=False),
          ]),
      ],
      f1=B('Write thousandths as decimals', '5.NBT.A.3.a', [
          sa('Write {125/1000} as a decimal.', 'Decimal:', key='0.125'),
          tf('0.009 = {9/1000}', key=True),
          mc('Which decimal is equal to {4/1000}?', ['0.004', '0.04', '0.4', '4.000']),
          sa('Write 0.375 as a fraction with a denominator of 1,000.', 'Fraction:', key='375/1000'),
          tf('{72/1000} = 0.72', key=False),
      ]),
      f2=B('Write decimals as percents', '6.RP.A.3.c', [
          sa('Write 0.35 as a percent.', 'Percent:', key='35%'),
          tf('0.07 = 7%', key=True),
          mc('Which decimal is equal to 60%?', ['0.6', '6.0', '0.06', '60']),
          sa('Write 120% as a decimal.', 'Decimal:', key='1.2'),
          tf('0.5 = 5%', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.C.6 (number line)
    S('4.NF.C.6', 'Locate decimals to hundredths on a number line',
      main=[
          sa('What decimal is at point A?', 'A =', key='0.7', fig=nl(0, 1, 0.1, labels={0: '0', 1: '1'}, pts=[(0.7, 'A')])),
          mc('Which point is at 0.35?', ['Point A', 'Point B', 'Point C', 'Point D'],
             fig=nl(0.3, 0.4, 0.01, labels={0.3: '0.3', 0.4: '0.4'}, pts=[(0.35, 'A'), (0.31, 'B'), (0.38, 'C'), (0.33, 'D')])),
          plot('Mark and label 0.4 and 0.85 on the number line.', nl(0, 1, 0.05, labels={0: '0', 0.5: '0.5', 1: '1'}),
               key='0.4 marked at the 8th small tick after 0 and 0.85 marked at the 17th (halfway between 0.8 and 0.9), each labeled'),
          tf('0.5 is halfway between 0 and 1 on a number line.', key=True),
          sa('What decimal is at point B?', 'B =', key='2.6', fig=nl(2, 3, 0.1, labels={2: '2', 3: '3'}, pts=[(2.6, 'B')])),
      ],
      back=[
          B('Fractions on a number line', '3.NF.A.2', [
              sa('What fraction is at point A?', 'A =', key='4/6', note='2/3 is also correct.',
                 fig=nl(0, 1, 1 / 6, labels={0: '0', 1: '1'}, pts=[(4 / 6, 'A')])),
              tf('{1/2} is halfway between 0 and 1 on a number line.', key=True),
              mc('Into how many equal parts is the space from 0 to 1 divided?', ['4', '3', '5', '2'], fig=nl(0, 1, 0.25, labels={0: '0', 1: '1'})),
              sa('What fraction is at point B?', 'B =', key='3/8', fig=nl(0, 1, 0.125, labels={0: '0', 1: '1'}, pts=[(0.375, 'B')])),
              tf('{3/4} is to the left of {1/4} on a number line.', key=False),
          ]),
          B('Whole numbers on a number line', '2.MD.B.6', [
              sa('What number is at point P?', 'P =', key='7', fig=nl(0, 10, 1, labels={0: '0', 5: '5', 10: '10'}, pts=[(7, 'P')])),
              tf('On a number line, 12 is to the right of 9.', key=True),
              mc('Which number is halfway between 20 and 30 on a number line?', ['25', '24', '50', '15']),
              sa('What number is at point Q?', 'Q =', key='43', fig=nl(40, 50, 1, labels={40: '40', 45: '45', 50: '50'}, pts=[(43, 'Q')])),
              tf('The distance from 3 to 8 on a number line is 11.', key=False),
          ]),
      ],
      f1=B('Round decimals using place value', '5.NBT.A.4', [
          sa('Round 2.68 to the nearest tenth.', 'Rounded:', key='2.7'),
          tf('On a number line, 4.17 is closer to 4.2 than to 4.1.', key=True),
          mc('Which number is closest to 5?', ['4.96', '5.1', '4.8', '5.09']),
          sa('Round 0.734 to the nearest hundredth.', 'Rounded:', key='0.73'),
          tf('6.25 rounded to the nearest whole number is 7.', key=False),
      ]),
      f2=B('Locate positive and negative decimals on a number line', '6.NS.C.6.c', [
          sa('What number is at point A?', 'A =', key='-1.5',
             fig=nl(-2, 2, 0.5, labels={-2: '-2', -1: '-1', 0: '0', 1: '1', 2: '2'}, pts=[(-1.5, 'A')])),
          tf('-0.5 is halfway between -1 and 0 on a number line.', key=True),
          mc('Which point is at -0.75?', ['Point A', 'Point B', 'Point C', 'Point D'],
             fig=nl(-1, 1, 0.25, labels={-1: '-1', 0: '0', 1: '1'}, pts=[(-0.75, 'A'), (0.75, 'B'), (-0.25, 'C'), (0.25, 'D')])),
          plot('Mark and label -1.2 and 0.8 on the number line.', nl(-2, 2, 0.2, labels={-2: '-2', -1: '-1', 0: '0', 1: '1', 2: '2'}),
               key='-1.2 marked one small tick to the left of -1 and 0.8 marked one small tick to the left of 1, each labeled'),
          tf('-1.25 is to the right of -1 on a number line.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.NF.C.7
    S('4.NF.C.7', 'Compare two decimals to hundredths and justify the comparison',
      main=[
          sa('Write >, =, or <.\n0.6 ___ 0.58', 'Symbol:', key='>'),
          mc('Which comparison is true?', ['0.09 < 0.1', '0.09 > 0.1', '0.09 = 0.1', '0.1 < 0.09']),
          tf('0.40 = 0.4', key=True),
          sa('Compare 0.3 and 0.25. Write >, =, or <, and explain using place value or a model.', ['Comparison:', 'Explanation:'], key='0.3 > 0.25',
             note='0.3 = 0.30 = 30 hundredths, which is more than 25 hundredths (or a hundredths grid shows 30 squares against 25). Both parts are required.'),
          tf('Jo has 0.5 of a large pizza and Sam has 0.5 of a small pizza. They have the same amount of pizza.', key=False),
      ],
      back=[
          B('Compare fractions with the same numerator or the same denominator', '3.NF.A.3.d', [
              sa('Write >, =, or <.\n{5/8} ___ {3/8}', 'Symbol:', key='>'),
              tf('{1/6} < {1/2}', key=True),
              mc('Which fraction is least?', ['{2/8}', '{2/3}', '{2/4}', '{2/6}']),
              sa('Write >, =, or <.\n{2/4} ___ {2/4}', 'Symbol:', key='='),
              tf('{1/8} > {1/4}', key=False),
          ]),
          B('Compare three-digit numbers', '2.NBT.A.4', [
              sa('Write >, =, or <.\n630 ___ 603', 'Symbol:', key='>'),
              tf('458 < 485', key=True),
              mc('Which number is least?', ['199', '910', '901', '291']),
              sa('Write >, =, or <.\n777 ___ 787', 'Symbol:', key='<'),
              tf('350 > 530', key=False),
          ]),
      ],
      f1=B('Compare decimals to thousandths', '5.NBT.A.3.b', [
          sa('Write >, =, or <.\n0.307 ___ 0.37', 'Symbol:', key='<'),
          tf('4.5 > 4.485', key=True),
          mc('Which decimal is least?', ['0.099', '0.1', '0.19', '0.109']),
          sa('Write >, =, or <.\n2.500 ___ 2.5', 'Symbol:', key='='),
          tf('0.62 < 0.602', key=False),
      ]),
      f2=B('Write and interpret statements of order for decimals in context', '6.NS.C.7.b', [
          sa('Write an inequality that compares -1.5°C and -0.5°C.', 'Inequality:', key='-1.5 < -0.5', note='-0.5 > -1.5 is also correct.'),
          tf('A depth of -3.2 m is deeper than a depth of -2.3 m.', key=True),
          mc('Which statement is true?', ['-0.8 < -0.3', '-0.8 > -0.3', '-0.3 < -0.8', '0.3 < -0.8']),
          sa('Order from least to greatest.\n-0.4, 0.2, -1.1', 'Order:', key='-1.1, -0.4, 0.2'),
          tf('-2.75 > -2.5', key=False),
      ])),
]
