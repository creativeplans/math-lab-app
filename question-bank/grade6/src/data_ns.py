from qb import S, B, sa, mc, tf, nl, coord, q1, table, stack, shape, poly, rect, plot, hrow

LET = ['Point A', 'Point B', 'Point C', 'Point D']
SYM = shape([poly([(0, 0), (6, 0), (6, 4), (0, 4)])], segs=[dict(a=(3, -0.6), b=(3, 4.6), color='#155a9c')])
ERR = ['Mistake:', 'Correct answer:']
STEP = ['Step with the mistake:', 'Correct solution:']


def setup(a, b):
    return [stack(*a, rule=len(a), fs=1.1), stack(*b, rule=len(b), fs=1.1)]


def board(name, lines, rule):
    return sa('%s put this example on the board.\nWhat mistake was made? What should the answer be?' % name, ERR,
              fig=stack(*lines, rule=rule), pos='right', split=0.55)


SETS = [
    # ------------------------------------------------------------------ 6.NS.A.1 compute
    S('6.NS.A.1', 'Compute quotients of fractions and mixed numbers',
      main=[
          sa('Divide.\n{3/5} ÷ {2/3}', 'Quotient:'),
          sa('Divide.\n{5/6} ÷ {1/3}', 'Quotient:'),
          sa('Divide.\n1{1/2} ÷ {3/4}', 'Quotient:'),
          mc('Which is equal to {4/5} ÷ {2/3}?', ['1{1/5}', '{8/15}', '{5/6}', '{2/15}']),
          sa('Divide.\n3{1/3} ÷ {5/6}', 'Quotient:'),
      ],
      back=[
          B('Multiplying fractions', '5.NF.B.4.a', [
              sa('Multiply.\n{3/5} × {2/7}', 'Product:'),
              tf('{3/4} × {2/5} = {6/20}'),
              mc('{1/2} × {5/6} = ?', ['{5/12}', '{6/8}', '{5/8}', '{1/3}']),
              sa('Multiply.\n{4/5} × {3/2}', 'Product:'),
              sa('Multiply.\n{5/6} × 3', 'Product:'),
          ]),
          B('Whole number ÷ unit fraction', '5.NF.B.7.b', [
              sa('Divide.\n3 ÷ {1/4}', 'Quotient:'),
              tf('4 ÷ {1/2} = 8'),
              mc('How many thirds are in 2?', ['6', '{2/3}', '5', '{1/6}']),
              sa('Divide.\n6 ÷ {1/5}', 'Quotient:'),
              sa('Divide.\n2 ÷ {1/8}', 'Quotient:'),
          ]),
          B('Unit fraction ÷ whole number', '5.NF.B.7.a', [
              sa('Divide.\n{1/4} ÷ 3', 'Quotient:'),
              tf('{1/2} ÷ 3 = {1/6}'),
              mc('{1/5} ÷ 2 = ?', ['{1/10}', '{2/5}', '10', '{5/2}']),
              sa('Divide.\n{1/6} ÷ 3', 'Quotient:'),
              tf('{1/6} ÷ 2 = {2/6}'),
          ]),
          B('Equivalent fractions', '4.NF.A.1', [
              tf('{8/12} is equivalent to {2/3}.'),
              sa('Find the missing number.\n{10/15} = {?/3}', 'Missing number:'),
              mc('Which fraction is equivalent to {9/12}?', ['{3/4}', '{2/3}', '{9/4}', '{12/9}']),
              sa('Find the missing number.\n{6/8} = {?/4}', 'Missing number:'),
              tf('{4/6} is equivalent to {6/8}.'),
          ]),
          B('Mixed numbers as fractions', '4.NF.B.3.b', [
              sa('Write 1{1/2} as a fraction.', 'Fraction:'),
              sa('Write 3{1/3} as a fraction.', 'Fraction:'),
              tf('2{1/4} = {9/4}'),
              mc('Which fraction is equal to 1{2/3}?', ['{5/3}', '{3/3}', '{12/3}', '{7/3}']),
              sa('Write {11/4} as a mixed number.', 'Mixed number:'),
          ]),
      ],
      f1=B('Multiply and divide rational numbers', '7.NS.A.2.c', [
          sa('Find the value.\n(-{2/3}) ÷ {4/5}', ''),
          sa('Find the value.\n-{3/4} × (-{8/9})', ''),
          mc('(-1{1/2}) ÷ (-{3/8}) = ?', ['4', '-4', '{9/16}', '-{9/16}']),
          sa('Find the value.\n{5/6} ÷ (-{5/12})', ''),
          tf('(-{1/2}) × {4/5} = -{2/5}'),
      ]),
      f2=B('Equations with fraction coefficients', '8.EE.C.7.b', [
          sa('Solve for x.\n{3/4}(x - 2) = {1/2}x + 5', 'x ='),
          sa('Solve for x.\n{2/3}x + 4 = {1/6}x + 7', 'x ='),
          mc('Solve for x.\n{x/2} + {x/3} = 10', ['12', '60', '5', '6']),
          sa('Solve for x.\n{1/2}(4x + 6) = 3x - 5', 'x ='),
          sa('Solve for y.\n{5/8}y - 1 = {3/8}y + 2', 'y ='),
      ])),

    # ------------------------------------------------------------------ 6.NS.A.1 word problems
    S('6.NS.A.1', 'Solve word problems involving division of fractions',
      main=[
          sa('How many {2/3}-cup scoops are in {5/6} cup of flour?', 'Scoops:'),
          sa('A path is {3/4} mile long. It is divided into sections that are each {1/8} mile long.\nHow many sections are there?', 'Sections:'),
          sa('A rectangular patio has an area of {3/5} square yard. Its length is {9/10} yard.\nWhat is its width?', 'Width:'),
          mc('A pitcher holds {9/10} liter of juice. Each glass holds {3/10} liter.\nHow many glasses can be filled?', ['3', '{27/100}', '{1/3}', '6']),
          sa('Ana has {5/6} pound of trail mix. She fills bags that each hold {5/12} pound.\nHow many bags can she fill?', 'Bags:'),
      ],
      back=[
          B('Division as "how many groups?"', '3.OA.A.2', [
              sa('How many groups of 4 are in 20?', 'Groups:'),
              tf('12 ÷ 3 can mean "How many groups of 3 are in 12?"'),
              mc('Tom has 18 cookies. He puts 6 cookies in each bag.\nWhich equation finds the number of bags?', ['18 ÷ 6 = □', '18 × 6 = □', '18 - 6 = □', '6 ÷ 18 = □']),
              sa('24 students are split into teams of 8.\nHow many teams are there?', 'Teams:'),
              sa('How many 5s are in 35?', 'Answer:'),
          ]),
          B('Unit fractions build a fraction', '3.NF.A.1', [
              sa('How many {1/4}s make {3/4}?', 'Answer:'),
              sa('How many {1/8}s make 1 whole?', 'Answer:'),
              tf('{5/6} is 5 parts of size {1/6}.'),
              mc('{3/8} is made of how many parts of size {1/8}?', ['3', '8', '5', '{1/3}']),
              sa('How many {1/3}s make {2/3}?', 'Answer:'),
          ]),
          B('Area with fractional side lengths', '5.NF.B.4.b', [
              sa('What is the area of the rectangle?', 'Area:', fig=rect(4, 3, '{3/4} m', '{2/3} m')),
              tf('A rectangle that is {1/2} foot by {1/3} foot has an area of {1/6} square foot.'),
              mc('A rectangle is {2/5} unit by {1/2} unit.\nWhat is its area?', ['{1/5} square unit', '{3/7} square unit', '{2/7} square unit', '{9/10} square unit']),
              sa('What is the area of the rectangle?', 'Area:', fig=rect(6, 1.6, '1{1/2} ft', '{1/4} ft')),
              sa('A garden is {5/6} yard long and {3/5} yard wide.\nWhat is its area?', 'Area:'),
          ]),
          B('Word problems: dividing with unit fractions', '5.NF.B.7.c', [
              sa('How many {1/4}-pound burgers can be made from 3 pounds of beef?', 'Burgers:'),
              sa('A 4-pound bag of rice is divided into {1/2}-pound portions.\nHow many portions are there?', 'Portions:'),
              mc('Which expression finds how many {1/5}-mile laps are in 3 miles?', ['3 ÷ {1/5}', '{1/5} ÷ 3', '3 × {1/5}', '3 - {1/5}']),
              sa('4 friends share {1/3} pound of cheese equally.\nHow much cheese does each friend get?', 'Each friend:'),
              tf('There are 10 half-hours in 5 hours.'),
          ]),
      ],
      f1=B('Real-world problems with rational numbers', '7.NS.A.3', [
          sa('A diver descends {3/4} foot each second.\nHow many seconds does it take to descend 5{1/4} feet?', 'Seconds:'),
          sa('The temperature was 4°F. It dropped 2{1/2}°F each hour for 3 hours.\nWhat was the final temperature?', 'Temperature:'),
          mc('A stock\'s value changed by -$1{1/4} each day for 4 days.\nWhat was the total change?', ['-$5', '$5', '-$4{1/4}', '-$1']),
          sa('A recipe needs {2/3} cup of oil per batch. Jo has 3{1/3} cups of oil.\nHow many batches can Jo make?', 'Batches:'),
          sa('A hiker descends 1,250 feet in {5/6} hour at a constant rate.\nWhat is the change in elevation per hour?', 'Change per hour:'),
      ]),
      f2=B('Solve linear equations from contexts', '8.EE.C.7.b', [
          sa('Solve for x.\n{1/2}(x + 6) = {1/3}(x + 12)', 'x ='),
          sa('Lee\'s age plus {1/3} of his age is 24.\nWrite and solve an equation to find Lee\'s age.', 'Age:'),
          sa('Tank A has 40 gallons and drains {3/4} gallon per minute. Tank B has 10 gallons and fills at 1{1/4} gallons per minute.\nAfter how many minutes will the tanks hold the same amount?', 'Minutes:'),
          mc('Solve for x.\n{2/5}x - 3 = {1/5}x + 1', ['20', '10', '4', '-10']),
          sa('Solve for n.\n{3/4}n + {1/2} = {1/4}n + 4', 'n ='),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.2
    S('6.NS.B.2', 'Divide multi-digit numbers using the standard algorithm',
      main=[
          sa('Use the standard algorithm to divide.\n4,508 ÷ 23', 'Quotient:'),
          sa('Use the standard algorithm to divide.\n7,236 ÷ 36', 'Quotient:'),
          sa('Use the standard algorithm to divide.\n9,975 ÷ 75', 'Quotient:'),
          mc('Use the standard algorithm to divide.\n1,680 ÷ 48', ['35', '30', '350', '36']),
          sa('Use the standard algorithm to divide.\n25,494 ÷ 42', 'Quotient:'),
      ],
      back=[
          B('Multiplying multi-digit numbers', '5.NBT.B.5', [
              sa('Multiply.\n46 × 23', 'Product:'),
              sa('Multiply.\n196 × 23', 'Product:'),
              tf('35 × 48 = 1,680'),
              mc('133 × 75 = ?', ['9,975', '9,875', '1,596', '9,775']),
              sa('Multiply.\n607 × 42', 'Product:'),
          ]),
          B('Dividing by a one-digit number', '4.NBT.B.6', [
              sa('Divide.\n852 ÷ 4', 'Quotient:'),
              sa('Divide.\n1,256 ÷ 8', 'Quotient:'),
              tf('936 ÷ 3 = 312'),
              mc('714 ÷ 7 = ?', ['102', '12', '120', '1,002']),
              sa('Divide.\n2,345 ÷ 5', 'Quotient:'),
          ]),
          B('Estimating quotients', '5.NBT.B.6', [
              mc('Which is the best estimate for 4,508 ÷ 23?', ['200', '20', '2,000', '2']),
              mc('Which is the best estimate for 7,236 ÷ 36?', ['200', '20', '2,000', '2']),
              tf('9,975 ÷ 75 is between 100 and 200.'),
              sa('Estimate 6,120 ÷ 29 by rounding 29 to 30.', 'Estimate:'),
              mc('How many digits are in the quotient of 1,680 ÷ 48?', ['2', '1', '3', '4']),
          ]),
          B('Multi-digit subtraction', '4.NBT.B.4', [
              sa('Subtract.\n5,012 - 4,698', 'Difference:'),
              sa('Subtract.\n3,000 - 1,847', 'Difference:'),
              tf('7,236 - 7,200 = 36'),
              mc('9,975 - 9,000 = ?', ['975', '9,075', '1,975', '75']),
              sa('Subtract.\n6,203 - 2,875', 'Difference:'),
          ]),
      ],
      f1=B('Long division: fractions to decimals', '7.NS.A.2.d', [
          sa('Use long division to write {5/11} as a decimal.', 'Decimal:'),
          sa('Use long division to write {3/8} as a decimal.', 'Decimal:'),
          mc('Which fraction has a repeating decimal?', ['{2/3}', '{3/4}', '{7/8}', '{1/5}']),
          tf('The decimal form of {7/20} terminates.'),
          sa('Use long division to write {5/6} as a decimal.', 'Decimal:'),
      ]),
      f2=B('Repeating decimals and rational numbers', '8.NS.A.1', [
          sa('Write 0.272727... as a fraction in simplest form.', 'Fraction:'),
          sa('Write 0.444... as a fraction.', 'Fraction:'),
          mc('Which number is irrational?', ['√7', '0.333...', '{5/8}', '√16']),
          tf('Every repeating decimal is a rational number.'),
          sa('Write 1.1666... as a fraction.', 'Fraction:'),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.3 add
    S('6.NS.B.3', 'Add multi-digit decimals',
      main=[
          sa('Find the sum.\n315.4 + 28.75 + 6.309', 'Sum:'),
          sa('Find the sum.\n47.08 + 9.6', 'Sum:'),
          sa('Find the sum.\n128.5 + 3.47 + 60.009', 'Sum:'),
          mc('Find the sum.\n6.75 + 12.9 + 0.48', ['20.13', '19.23', '7.23', '20.03']),
          sa('Find the sum.\n0.875 + 14.2 + 3.06', 'Sum:'),
      ],
      back=[
          B('Place value of decimal digits', '5.NBT.A.3.a', [
              mc('In 7.358, what place value does the digit 5 have?', ['Hundredths', 'Tenths', 'Thousandths', 'Ones']),
              sa('In 42.906, which digit is in the tenths place?', 'Digit:'),
              tf('In 3.47, the digit 7 is in the hundredths place.'),
              mc('What is the value of the 8 in 0.584?', ['0.08', '0.8', '0.008', '8']),
              sa('Write 5 + 0.3 + 0.07 as a decimal.', 'Decimal:'),
          ]),
          B('Equivalent decimals', '5.NBT.A.3.b', [
              tf('2.4 and 2.40 have the same value.'),
              tf('5.6 and 5.06 have the same value.'),
              mc('Which decimal is equal to 7.5?', ['7.50', '7.05', '7.005', '0.75']),
              sa('Write 9.6 with a zero in the hundredths place.', 'Decimal:'),
              tf('0.300 = 0.3'),
          ]),
          B('Lining up decimal points to add', '5.NBT.B.7', [
              mc('Which setup lines up the decimal points for 36.2 + 4.58?', None, cfigs=setup(['36.2', '+4.58'], ['36.20', '+ 4.58']), cfh=150),
              mc('Which setup lines up the decimal points for 5.07 + 12.3?', None, cfigs=setup(['5.07', '+12.30'], ['5.07', '+12.3']), cfh=150),
              tf('The decimal points are lined up correctly.', fig=stack('8.4', '+2.75', rule=2), pos='right'),
              mc('Which setup lines up the decimal points for 128.5 + 3.47?', None, cfigs=setup(['128.50', '+  3.47'], ['128.5', '+3.47']), cfh=150),
              tf('The decimal points are lined up correctly.', fig=stack('9.30', '+ 0.45', rule=2), pos='right'),
          ]),
          B('Multi-digit addition', '4.NBT.B.4', [
              sa('Add.\n3,154 + 2,875', 'Sum:'),
              sa('Add.\n4,605 + 2,798', 'Sum:'),
              tf('1,975 + 3,489 = 5,464'),
              mc('6,758 + 1,265 = ?', ['8,023', '7,923', '8,013', '7,013']),
              sa('Add.\n12,480 + 9,635', 'Sum:'),
          ]),
      ],
      f1=B('Add rational numbers', '7.NS.A.1.d', [
          sa('Find the value.\n-18.6 + 4.35 =', '', fs=34),
          sa('Find the value.\n-24.5 + 3.27 =', '', fs=34),
          sa('Find the value.\n-3.4 + (-9.15) =', '', fs=34),
          mc('Find the value.\n-6.25 + (-2.8) = ?', ['-9.05', '-3.45', '3.45', '9.05']),
          sa('Find the value.\n-15.75 + 20.3 =', '', fs=34),
      ]),
      f2=B('Linear equations with decimal coefficients', '8.EE.C.7.b', [
          sa('Solve for x.\n-2.4x + 7.8 = 1.2x - 1.2', 'x =', fs=28),
          sa('Solve for x.\n-1.5x + 6.4 = 0.5x - 1.6', 'x =', fs=28),
          sa('Solve for x.\n0.8x + 7.2 = -1.2x + 1.2', 'x =', fs=28),
          sa('Solve for x.\n-4.5x - 3.25 = -2.5x + 0.75', 'x =', fs=28),
          sa('Solve for x.\n2.4(x + 1.5) = 1.4x + 6.6', 'x =', fs=28),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.3 subtract
    S('6.NS.B.3', 'Subtract multi-digit decimals',
      main=[
          sa('Find the difference.\n52.3 - 18.47', 'Difference:'),
          sa('Find the difference.\n100 - 36.58', 'Difference:'),
          sa('Find the difference.\n7.4 - 2.068', 'Difference:'),
          mc('Find the difference.\n15.02 - 6.9', ['8.12', '9.12', '8.93', '14.33']),
          sa('Find the difference.\n243.6 - 87.95', 'Difference:'),
      ],
      back=[
          B('Place value of decimal digits', '5.NBT.A.3.a', [
              mc('In 2.068, what place value does the digit 6 have?', ['Hundredths', 'Tenths', 'Thousandths', 'Ones']),
              sa('In 87.95, which digit is in the hundredths place?', 'Digit:'),
              tf('In 36.58, the digit 5 is in the tenths place.'),
              mc('What is the value of the 4 in 7.04?', ['0.04', '0.4', '4', '0.004']),
              sa('Write 20 + 0.6 + 0.009 as a decimal.', 'Decimal:'),
          ]),
          B('Writing zeros to make equal decimal places', '5.NBT.A.3.b', [
              tf('7.4 = 7.400'),
              sa('Write 100 with two decimal places.', 'Decimal:'),
              mc('Which decimal is equal to 15.1?', ['15.10', '15.01', '1.51', '15.001']),
              sa('Write 52.3 with a digit in the hundredths place, without changing its value.', 'Decimal:'),
              tf('6.9 = 6.09'),
          ]),
          B('Lining up decimal points to subtract', '5.NBT.B.7', [
              mc('Which setup lines up the decimal points for 15.6 - 3.42?', None, cfigs=setup(['15.60', '- 3.42'], ['15.6', '-3.42']), cfh=150),
              mc('Which setup lines up the decimal points for 52.3 - 18.47?', None, cfigs=setup(['52.3', '-18.47'], ['52.30', '-18.47']), cfh=150),
              tf('The decimal points are lined up correctly.', fig=stack('7.4', '-2.068', rule=2), pos='right'),
              tf('The decimal points are lined up correctly.', fig=stack('100.00', '- 36.58', rule=2), pos='right'),
              mc('Which setup lines up the decimal points for 243.6 - 87.95?', None, cfigs=setup(['243.60', '- 87.95'], ['243.6', '-87.95']), cfh=150),
          ]),
          B('Subtracting across zeros', '4.NBT.B.4', [
              sa('Subtract.\n5,000 - 2,847', 'Difference:'),
              sa('Subtract.\n3,006 - 1,478', 'Difference:'),
              tf('6,000 - 2,458 = 3,542'),
              mc('8,014 - 3,276 = ?', ['4,738', '5,262', '4,838', '4,748']),
              sa('Subtract.\n10,000 - 3,658', 'Difference:'),
          ]),
      ],
      f1=B('Subtract rational numbers by adding the additive inverse', '7.NS.A.1.c', [
          sa('Find the value.\n-4.2 - 3.75', 'Value:'),
          sa('Find the value.\n2.5 - (-6.8)', 'Value:'),
          mc('Which expression is equal to 8.1 - 12.4?', ['8.1 + (-12.4)', '8.1 + 12.4', '-8.1 + 12.4', '12.4 - 8.1']),
          sa('Find the value.\n-0.65 - (-1.2)', 'Value:'),
          tf('-7.5 - 2.5 = -7.5 + (-2.5)'),
      ]),
      f2=B('Solve equations by collecting like terms', '8.EE.C.7.b', [
          sa('Solve for x.\n5.2x - 3.75 = 2.2x + 8.25', 'x =', fs=28),
          sa('Solve for x.\n0.9x + 12.5 = 0.4x + 10', 'x =', fs=28),
          mc('Solve for x.\n6.3 - 1.2x = 0.8x - 1.7', ['4', '-4', '2.5', '0.4']),
          sa('Solve for x.\n4.75 - x = 2x - 1.25', 'x =', fs=28),
          sa('Solve for x.\n3.4x - 9.6 = 1.4x - 2.6', 'x =', fs=28),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.3 error analysis
    S('6.NS.B.3', 'Find and correct decimal alignment errors in addition and subtraction',
      main=[
          board('Jon', ['315.2', '24.8', '+7.936', '11.336'], 3),
          board('Ava', ['56.4', '+3.25', '8.89'], 2),
          board('Leo', ['48.6', '-2.15', '2.71'], 2),
          board('Mia', ['7.08', '+12.6', '8.34'], 2),
          board('Ben', ['125.6', '-3.48', '9.08'], 2),
      ],
      back=[
          B('Lining up decimal points', '5.NBT.B.7', [
              mc('Which setup lines up the decimal points for 56.4 + 3.25?', None, cfigs=setup(['56.4', '+3.25'], ['56.40', '+ 3.25']), cfh=150),
              mc('Which setup lines up the decimal points for 48.6 - 2.15?', None, cfigs=setup(['48.60', '- 2.15'], ['48.6', '-2.15']), cfh=150),
              tf('The decimal points are lined up correctly.', fig=stack('7.08', '+12.6', rule=2), pos='right'),
              tf('The decimal points are lined up correctly.', fig=stack('125.60', '-  3.48', rule=2), pos='right'),
              mc('Which setup lines up the decimal points for 24.8 + 7.936?', None, cfigs=setup(['24.8', '+7.936'], ['24.800', '+ 7.936']), cfh=150),
          ]),
          B('Place value of decimal digits', '5.NBT.A.3.a', [
              mc('In 7.936, what place value does the digit 3 have?', ['Hundredths', 'Tenths', 'Thousandths', 'Ones']),
              sa('In 315.2, which digit is in the ones place?', 'Digit:'),
              tf('In 3.25, the digit 2 is in the tenths place.'),
              mc('What is the value of the 6 in 12.56?', ['0.06', '0.6', '6', '60']),
              sa('In 48.6, which digit is in the tenths place?', 'Digit:'),
          ]),
          B('Estimating to check reasonableness', '5.NBT.A.4', [
              sa('Round each number to the nearest whole number. Then add to estimate.\n315.2 + 24.8 + 7.936', 'Estimate:'),
              sa('Round 48.6 to the nearest whole number.', 'Rounded:'),
              tf('7.08 + 12.6 is about 20.'),
              mc('Which is the best estimate for 125.6 - 3.48?', ['122', '90', '9', '130']),
              sa('Round 56.4 and 3.25 to the nearest whole numbers. Then add.', 'Estimate:'),
          ]),
      ],
      f1=B('Find errors when adding and subtracting rational numbers', '7.NS.A.1.d', [
          sa('Ray wrote: -3.5 + 1.25 = -4.75\nWhat mistake was made? What is the correct value?', ERR),
          sa('Tia wrote: -6.2 - 2.4 = -3.8\nWhat mistake was made? What is the correct value?', ERR),
          sa('Sam wrote: 4.5 - (-1.5) = 3\nWhat mistake was made? What is the correct value?', ERR),
          sa('Kai wrote: -7.25 + (-2.5) = -4.75\nWhat mistake was made? What is the correct value?', ERR),
          sa('Lia wrote: -0.8 + 2.3 = -1.5\nWhat mistake was made? What is the correct value?', ERR),
      ]),
      f2=B('Find errors in solving linear equations', '8.EE.C.7.b', [
          sa('Kim solved 2.4x + 1.2 = 0.4x - 3.8.\nStep 1: 2x + 1.2 = -3.8\nStep 2: 2x = -2.6\nStep 3: x = -1.3\nWhich step has the mistake? What is the correct solution?', STEP),
          sa('Jo solved 3.5x - 2 = 1.5x + 6.\nStep 1: 2x - 2 = 6\nStep 2: 2x = 4\nStep 3: x = 2\nWhich step has the mistake? What is the correct solution?', STEP),
          sa('Ali solved -1.2x + 5 = 0.8x - 3.\nStep 1: -2x + 5 = -3\nStep 2: -2x = -8\nStep 3: x = -4\nWhich step has the mistake? What is the correct solution?', STEP),
          sa('Ned solved 0.5(x + 6) = 2x - 3.\nStep 1: 0.5x + 6 = 2x - 3\nStep 2: 9 = 1.5x\nStep 3: x = 6\nWhich step has the mistake? What is the correct solution?', STEP),
          sa('Eve solved 4.2x - 1.5 = 2.2x + 2.5.\nStep 1: 2x - 1.5 = 2.5\nStep 2: 2x = 1\nStep 3: x = 0.5\nWhich step has the mistake? What is the correct solution?', STEP),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.3 multiply
    S('6.NS.B.3', 'Multiply multi-digit decimals',
      main=[
          sa('Multiply.\n3.6 × 0.45', 'Product:'),
          sa('Multiply.\n12.5 × 3.8', 'Product:'),
          sa('Multiply.\n4.25 × 2.4', 'Product:'),
          mc('Multiply.\n0.07 × 0.6', ['0.042', '0.42', '4.2', '0.0042']),
          sa('Multiply.\n18.4 × 0.35', 'Product:'),
      ],
      back=[
          B('Multiplying whole numbers', '5.NBT.B.5', [
              sa('Multiply.\n36 × 45', 'Product:'),
              sa('Multiply.\n125 × 38', 'Product:'),
              tf('425 × 24 = 10,200'),
              mc('184 × 35 = ?', ['6,440', '6,340', '1,472', '5,440']),
              sa('Multiply.\n208 × 15', 'Product:'),
          ]),
          B('Powers of 10 and the decimal point', '5.NBT.A.2', [
              sa('Multiply.\n0.45 × 10', 'Product:'),
              sa('Multiply.\n3.6 × 100', 'Product:'),
              tf('24 ÷ 10 = 2.4'),
              mc('1,620 ÷ 1,000 = ?', ['1.62', '16.2', '0.162', '162']),
              sa('Divide.\n475 ÷ 10', 'Quotient:'),
          ]),
          B('Multiplying tenths and hundredths', '5.NBT.B.7', [
              sa('Multiply.\n0.3 × 0.2', 'Product:'),
              sa('Multiply.\n0.5 × 0.8', 'Product:'),
              tf('0.4 × 0.4 = 1.6'),
              mc('0.2 × 0.03 = ?', ['0.006', '0.06', '0.6', '6']),
              sa('Multiply.\n1.2 × 0.3', 'Product:'),
          ]),
          B('Rounding decimals to estimate', '5.NBT.A.4', [
              sa('Round 3.62 to the nearest whole number.', 'Rounded:'),
              sa('Round 12.48 to the nearest tenth.', 'Rounded:'),
              tf('4.25 rounded to the nearest whole number is 4.'),
              mc('Round 0.456 to the nearest hundredth.', ['0.46', '0.45', '0.5', '0.4']),
              sa('Round 8.75 to the nearest whole number.', 'Rounded:'),
          ]),
      ],
      f1=B('Multiply rational numbers', '7.NS.A.2.c', [
          sa('Find the value.\n(-3.6)(0.45)', ''),
          sa('Find the value.\n(-2.5)(-4.2)', ''),
          mc('-0.8 × 1.5 = ?', ['-1.2', '1.2', '-0.12', '0.12']),
          sa('Find the value.\n(-1.2)(-0.5)(-3)', ''),
          tf('(-0.6)(0.7) = 0.42'),
      ]),
      f2=B('Multiply numbers in scientific notation', '8.EE.A.4', [
          sa('Multiply. Write the answer in scientific notation.\n(3.6 × 10⁴)(4.5 × 10⁻²)', 'Product:'),
          sa('Multiply. Write the answer in scientific notation.\n(2.5 × 10³)(4 × 10⁵)', 'Product:'),
          mc('(1.2 × 10⁶)(3 × 10⁻⁴) = ?', ['3.6 × 10²', '3.6 × 10¹⁰', '4.2 × 10²', '3.6 × 10⁻²']),
          sa('A light-year is about 9.5 × 10¹² km.\nAbout how many kilometers are in 4.2 light-years? Write the answer in scientific notation.', 'Kilometers:'),
          tf('(5 × 10³)(6 × 10²) = 3 × 10⁶'),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.3 divide
    S('6.NS.B.3', 'Divide multi-digit decimals',
      main=[
          sa('Divide.\n15.75 ÷ 0.35', 'Quotient:'),
          sa('Divide.\n8.64 ÷ 2.4', 'Quotient:'),
          sa('Divide.\n12.6 ÷ 0.45', 'Quotient:'),
          mc('Divide.\n0.72 ÷ 0.08', ['9', '0.9', '90', '0.09']),
          sa('Divide.\n283.5 ÷ 13.5', 'Quotient:'),
      ],
      back=[
          B('Dividing by a two-digit number', '5.NBT.B.6', [
              sa('Divide.\n1,575 ÷ 35', 'Quotient:'),
              sa('Divide.\n864 ÷ 24', 'Quotient:'),
              tf('1,260 ÷ 45 = 28'),
              mc('672 ÷ 32 = ?', ['21', '12', '210', '22']),
              sa('Divide.\n2,835 ÷ 15', 'Quotient:'),
          ]),
          B('Using powers of 10 to shift the decimal point', '5.NBT.A.2', [
              mc('Which has the same quotient as 15.75 ÷ 0.35?', ['1,575 ÷ 35', '157.5 ÷ 35', '1,575 ÷ 3.5', '15.75 ÷ 35']),
              tf('8.64 ÷ 2.4 has the same quotient as 86.4 ÷ 24.'),
              sa('Multiply.\n0.45 × 100', 'Product:'),
              sa('Multiply.\n12.6 × 100', 'Product:'),
              mc('0.08 × ___ = 8', ['100', '10', '1,000', '0.1']),
          ]),
          B('Dividing tenths and hundredths', '5.NBT.B.7', [
              sa('Divide.\n2.4 ÷ 0.6', 'Quotient:'),
              sa('Divide.\n3.5 ÷ 0.5', 'Quotient:'),
              tf('1.2 ÷ 0.3 = 0.4'),
              mc('0.9 ÷ 0.3 = ?', ['3', '0.3', '30', '0.03']),
              sa('Divide.\n4.8 ÷ 4', 'Quotient:'),
          ]),
      ],
      f1=B('Divide rational numbers', '7.NS.A.2.b', [
          sa('Find the value.\n(-15.75) ÷ 0.35', ''),
          sa('Find the value.\n-8.64 ÷ (-2.4)', ''),
          tf('-(12 ÷ 4) = (-12) ÷ 4'),
          mc('7.2 ÷ (-0.9) = ?', ['-8', '8', '-0.8', '0.8']),
          sa('Find the value.\n-0.72 ÷ 0.08', ''),
      ]),
      f2=B('Divide numbers in scientific notation', '8.EE.A.4', [
          sa('Divide. Write the answer in scientific notation.\n(6.3 × 10⁸) ÷ (2.1 × 10³)', 'Quotient:'),
          sa('Divide. Write the answer in scientific notation.\n(4.8 × 10⁻²) ÷ (1.6 × 10⁻⁵)', 'Quotient:'),
          mc('(9 × 10⁶) ÷ (3 × 10⁹) = ?', ['3 × 10⁻³', '3 × 10³', '6 × 10⁻³', '3 × 10¹⁵']),
          sa('Divide. Write the answer in scientific notation.\n(7.5 × 10⁴) ÷ (2.5 × 10⁻¹)', 'Quotient:'),
          tf('(8.4 × 10⁵) ÷ (4.2 × 10²) = 2 × 10³'),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.4 GCF
    S('6.NS.B.4', 'Find the greatest common factor of two whole numbers',
      main=[
          sa('Find the greatest common factor of 24 and 36.', 'GCF:'),
          mc('What is the greatest common factor of 18 and 45?', ['9', '3', '90', '15']),
          sa('Find the greatest common factor of 28 and 42.', 'GCF:'),
          sa('Find the greatest common factor of 30 and 75.', 'GCF:'),
          sa('Find the greatest common factor of 16 and 40.', 'GCF:'),
      ],
      back=[
          B('Factors', '4.OA.B.4', [
              sa('List all the factors of 18.', 'Factors:'),
              tf('7 is a factor of 42.'),
              mc('Which number is NOT a factor of 36?', ['8', '9', '12', '4']),
              tf('5 is a factor of 32.'),
              sa('List all the factors of 24.', 'Factors:'),
          ]),
          B('Prime and composite numbers', '4.OA.B.4', [
              tf('13 is a prime number.'),
              mc('Which number is composite?', ['21', '17', '11', '2']),
              tf('1 is a prime number.'),
              sa('Is 29 prime or composite?', 'Answer:'),
              mc('Which number is prime?', ['31', '27', '33', '39']),
          ]),
          B('Division facts', '3.OA.C.7', [
              sa('Divide.\n42 ÷ 7', 'Quotient:'),
              sa('Divide.\n36 ÷ 4', 'Quotient:'),
              tf('45 ÷ 9 = 5'),
              mc('56 ÷ 8 = ?', ['7', '6', '8', '9']),
              sa('Divide.\n63 ÷ 9', 'Quotient:'),
          ]),
      ],
      f1=B('Factor linear expressions using a common factor', '7.EE.A.1', [
          sa('Factor using the greatest common factor.\n18x + 24', 'Factored form:'),
          sa('Factor using the greatest common factor.\n20a - 35', 'Factored form:'),
          mc('Which shows 16m + 40 factored using the greatest common factor?', ['8(2m + 5)', '4(4m + 10)', '2(8m + 20)', '8(2m + 40)']),
          sa('Factor using the greatest common factor.\n27x + 45y', 'Factored form:'),
          tf('14n - 21 = 7(2n - 3)'),
      ]),
      f2=B('Solve equations using the distributive property', '8.EE.C.7.b', [
          sa('Solve for x.\n12x + 18 = 6(x + 5)', 'x ='),
          sa('Solve for x.\n4(3x - 2) = 8(x + 1)', 'x ='),
          mc('Solve for x.\n15x - 10 = 5(2x + 3)', ['5', '1', '-1', '25']),
          sa('Solve for x.\n9(x + 2) = 6(x + 5)', 'x ='),
          sa('Solve for x.\n10x + 25 = 5(x + 10)', 'x ='),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.4 LCM
    S('6.NS.B.4', 'Find the least common multiple of two whole numbers',
      main=[
          sa('Find the least common multiple of 6 and 8.', 'LCM:'),
          sa('Find the least common multiple of 4 and 10.', 'LCM:'),
          mc('What is the least common multiple of 9 and 12?', ['36', '108', '3', '72']),
          sa('Find the least common multiple of 5 and 7.', 'LCM:'),
          sa('Find the least common multiple of 6 and 15.', 'LCM:'),
      ],
      back=[
          B('Multiples', '4.OA.B.4', [
              sa('List the first five multiples of 6.', 'Multiples:'),
              tf('36 is a multiple of 8.'),
              mc('Which number is a multiple of both 4 and 6?', ['12', '18', '8', '20']),
              tf('45 is a multiple of 9.'),
              sa('What is the 4th multiple of 7?', 'Multiple:'),
          ]),
          B('Multiplication facts', '3.OA.C.7', [
              sa('Multiply.\n6 × 8', 'Product:'),
              sa('Multiply.\n9 × 4', 'Product:'),
              tf('7 × 5 = 35'),
              mc('3 × 12 = ?', ['36', '15', '33', '39']),
              sa('Multiply.\n5 × 6', 'Product:'),
          ]),
      ],
      f1=B('Add and subtract rational numbers with unlike denominators', '7.NS.A.1.d', [
          sa('Find the value.\n-{5/6} + {3/8}', ''),
          sa('Find the value.\n{3/4} - (-{1/6})', ''),
          mc('-{2/3} - {1/4} = ?', ['-{11/12}', '-{1/12}', '{5/12}', '-{3/7}']),
          sa('Find the value.\n-1{1/2} + {5/6}', ''),
          tf('{3/10} + (-{2/15}) = {1/6}'),
      ]),
      f2=B('Equations with fractions: clearing denominators', '8.EE.C.7.b', [
          sa('Solve for x.\n{x/6} + {x/8} = 7', 'x ='),
          sa('Solve for x.\n{x/4} - 1 = {x/6} + 2', 'x ='),
          mc('Solve for x.\n{2x/3} + {x/2} = 14', ['12', '7', '42', '{84/5}']),
          sa('Solve for x.\n{x/5} + 3 = {x/2}', 'x ='),
          sa('Solve for x.\n{(x+1)/4} = {(x−2)/3}', 'x ='),
      ])),

    # ------------------------------------------------------------------ 6.NS.B.4 distributive
    S('6.NS.B.4', 'Use the distributive property to write a sum as the GCF times a sum',
      main=[
          sa('Use the greatest common factor to write 45 + 20 as a product of the GCF and a sum of two whole numbers.', 'Expression:'),
          mc('Which expression is equal to 42 + 56 and uses the greatest common factor?', ['14(3 + 4)', '7(6 + 8)', '2(21 + 28)', '14(3 + 8)']),
          sa('Use the greatest common factor to write 27 + 45 as a product.', 'Expression:'),
          tf('24 + 60 = 12(2 + 5)'),
          sa('Complete the equation.\n30 + 75 = 15(___ + ___)', ['First blank:', 'Second blank:']),
      ],
      back=[
          B('Common factors', '4.OA.B.4', [
              tf('5 is a factor of both 45 and 20.'),
              sa('List the factors of 12 and the factors of 18.\nWhich factors do they share?', 'Shared factors:'),
              mc('Which number is a factor of both 27 and 45?', ['9', '5', '6', '15']),
              sa('List all the factors of 42.', 'Factors:'),
              tf('6 is a factor of 56.'),
          ]),
          B('Distributive property with whole numbers', '3.OA.B.5', [
              tf('9 × 6 = 9 × 4 + 9 × 2'),
              tf('4 × (9 + 2) = 4 × 9 + 2'),
              mc('Which is equal to 6 × 12?', ['6 × 10 + 6 × 2', '6 × 10 + 2', '6 + 10 × 2', '6 × 10 × 2']),
              sa('Fill in the blank.\n5 × 13 = 5 × 10 + 5 × ___', 'Blank:'),
              sa('Fill in the blank.\n3 × (4 + 5) = 3 × 4 + 3 × ___', 'Blank:'),
          ]),
          B('Parentheses and order of operations', '5.OA.A.1', [
              sa('Evaluate.\n5 × (9 + 4)', 'Value:'),
              sa('Evaluate.\n14 × (3 + 4)', 'Value:'),
              tf('9 × (3 + 5) = 32'),
              mc('12 × (2 + 5) = ?', ['84', '29', '17', '60']),
              sa('Evaluate.\n(20 - 5) × 3', 'Value:'),
          ]),
      ],
      f1=B('Factor and expand linear expressions', '7.EE.A.1', [
          sa('Factor.\n12x - 18', 'Factored form:'),
          sa('Expand.\n-3(2x - 5)', 'Expanded form:'),
          mc('Which expression is equivalent to 8y + 20?', ['4(2y + 5)', '8(y + 20)', '2(4y + 20)', '4(2y + 20)']),
          sa('Factor.\n15a + 10b - 5', 'Factored form:'),
          tf('{1/2}(6x - 4) = 3x - 2'),
      ]),
      f2=B('One, none, or infinitely many solutions', '8.EE.C.7.a', [
          mc('How many solutions does the equation have?\n4(x + 3) = 4x + 12', ['One solution', 'No solution', 'Infinitely many solutions']),
          mc('How many solutions does the equation have?\n2(3x - 1) = 6x + 5', ['One solution', 'No solution', 'Infinitely many solutions']),
          mc('How many solutions does the equation have?\n3(x + 2) = 2x + 9', ['One solution', 'No solution', 'Infinitely many solutions']),
          sa('What number goes in the box so that the equation has infinitely many solutions?\n5(x - 2) = 5x - □', '□ ='),
          mc('Which equation has no solution?', ['2(x + 4) = 2x + 5', '2(x + 4) = 2x + 8', '2(x + 4) = x + 8', '2(x + 4) = 3x']),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.5 represent
    S('6.NS.C.5', 'Use positive and negative numbers to represent quantities in context',
      main=[
          sa('A diver is 30 feet below sea level.\nWrite an integer to represent the diver\'s position.', 'Integer:'),
          sa('A company lost $2,500 this month.\nWrite an integer to represent this change.', 'Integer:'),
          mc('A bank account shows a withdrawal of $45.\nWhich number represents this change?', ['-45', '45', '0', '-4.5']),
          sa('The temperature rose 12 degrees.\nWrite an integer to represent this change.', 'Integer:'),
          sa('A hawk flies 120 feet above sea level. A submarine is 120 feet below sea level.\nWrite an integer for each position.', ['Hawk:', 'Submarine:']),
      ],
      back=[
          B('Whole numbers as distances from 0', '2.MD.B.6', [
              sa('What number does point A represent?', 'Number:', fig=nl(0, 10, 1, pts=[(7, 'A')])),
              sa('How many units from 0 is the number 6?', 'Units:'),
              tf('On a number line, 9 is farther from 0 than 4 is.'),
              mc('Which point is 3 units from 0?', LET, fig=nl(0, 10, 1, pts=[(3, 'A'), (5, 'B'), (8, 'C'), (1, 'D')])),
              sa('What number does point B represent?', 'Number:', fig=nl(0, 20, 2, pts=[(14, 'B')])),
          ]),
          B('Increase and decrease situations', '2.OA.A.1', [
              sa('Kim had $20. She spent $8.\nHow much money does she have now?', 'Money:'),
              sa('A plant was 12 cm tall. It grew 5 cm.\nHow tall is the plant now?', 'Height:'),
              mc('Which situation describes a decrease?', ['A balloon loses 6 feet of height.', 'A plant grows 4 inches.', 'Tom earns $10.', 'A team gains 5 yards.']),
              tf('"The temperature fell 7 degrees" describes a decrease.'),
              mc('Which word describes an increase in money?', ['Deposit', 'Withdrawal', 'Loss', 'Drop']),
          ]),
      ],
      f1=B('Adding integers as moving on a number line', '7.NS.A.1.b', [
          sa('The temperature is -4°F. It rises 9°F.\nWhat is the new temperature?', 'Temperature:'),
          sa('A submarine is at -120 feet. It rises 45 feet.\nWhat is its new position?', 'Position:'),
          mc('On a number line, where is 6 + (-4) compared to 6?', ['4 units to the left of 6', '4 units to the right of 6', '6 units to the left of 4', 'At 0']),
          sa('The number line shows -2 + 5.\nWhat is the sum?', 'Sum:', fig=nl(-5, 5, 1, jumps=[(-2, 3, '+5')])),
          tf('A $30 debt plus a $30 deposit makes a balance of $0.'),
      ]),
      f2=B('The sign of the rate of change in context', '8.F.B.4', [
          sa('A tank holds 60 gallons. It drains 3 gallons per minute.\nWrite a function for the amount A after t minutes.', 'A ='),
          mc('An airplane at 12,000 feet descends 800 feet per minute.\nWhat is the rate of change of its altitude?', ['-800 feet per minute', '800 feet per minute', '12,000 feet per minute', '-12,000 feet per minute']),
          sa('The table shows a linear function.\nWhat is the rate of change in degrees per hour?', 'Rate of change:', fig=table([['Hours', '0', '2', '4'], ['Temperature (°F)', '5', '1', '-3']])),
          sa('A diver starts at -10 feet and descends 4 feet per second.\nWrite a function for the diver\'s position d after t seconds.', 'd ='),
          tf('A line through (0, 8) and (4, 0) has a rate of change of -2.'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.5 meaning of 0
    S('6.NS.C.5', 'Explain the meaning of 0 in a real-world situation',
      main=[
          mc('On a Celsius thermometer, what does 0°C represent?', ['The temperature at which water freezes', 'No temperature at all', 'The hottest possible temperature', 'The temperature at which water boils']),
          mc('When numbers describe elevation, what does 0 represent?', ['Sea level', 'The top of a mountain', 'The ocean floor', 'No elevation at all']),
          mc('A bank account has a balance of $0.\nWhat does this mean?', ['The account has no money and owes nothing.', 'The account owes money.', 'The account has money in it.', 'The account earns interest.']),
          mc('A football team\'s change in yards on a play is 0.\nWhat does 0 mean?', ['The team neither gained nor lost yards.', 'The team lost all its yards.', 'The team scored.', 'The team gained 10 yards.']),
          sa('A scale shows that your weight changed by 0 pounds since last month.\nWhat does 0 mean in this situation?', 'Meaning:'),
      ],
      back=[
          B('Zero as the starting point on a number line', '2.MD.B.6', [
              tf('On a number line, 0 is the starting point for measuring distance.'),
              sa('What number is at point A?', 'A =', fig=nl(0, 10, 1, pts=[(0, 'A')])),
              mc('How far is 0 from itself on a number line?', ['0 units', '1 unit', '10 units', '2 units']),
              sa('How far is 5 from 0 on a number line?', 'Units:'),
              tf('A ruler starts measuring at 1.'),
          ]),
          B('A change of zero means no change', '1.OA.D.8', [
              sa('What number goes in the box?\n8 + □ = 8', '□ ='),
              sa('What number goes in the box?\n15 - □ = 15', '□ ='),
              tf('A plant was 12 cm tall last week and is 12 cm tall now. It grew 0 cm.'),
              mc('A score went from 45 to 45.\nWhat was the change?', ['0', '45', '90', '1']),
              sa('What number goes in the box?\n□ + 23 = 23', '□ ='),
          ]),
      ],
      f1=B('Opposite quantities combine to make 0', '7.NS.A.1.a', [
          sa('Maya earns $25 and then spends $25.\nWhat is the total change in her money?', 'Total change:'),
          tf('-8 + 8 = 0'),
          mc('Which sum is equal to 0?', ['-3.5 + 3.5', '-3.5 + (-3.5)', '3.5 + 3.5', '-3.5 + 0']),
          sa('A balloon rises 40 feet and then falls 40 feet.\nWhat is its total change in height?', 'Total change:'),
          sa('What number added to 14.2 gives 0?', 'Number:'),
      ]),
      f2=B('Interpret the initial value (the value when x = 0)', '8.F.B.4', [
          sa('The water in a tank is W = 60 - 3t, where t is minutes.\nWhat does 60 represent?', 'Meaning:'),
          mc('A hiker\'s elevation is E = -40 + 15t, where t is hours.\nWhat does -40 represent?',
             ['The hiker starts 40 m below sea level.', 'The hiker climbs 40 m each hour.', 'The hiker ends 40 m below sea level.', 'The hike lasts 40 hours.']),
          sa('A phone\'s battery charge is B = 100 - 8h after h hours.\nWhat is B when h = 0, and what does it mean?', ['Value:', 'Meaning:']),
          mc('A savings account has y = 25x + 150 dollars after x weeks.\nWhat does 150 represent?', ['The starting amount', 'The amount saved each week', 'The amount after 25 weeks', 'The number of weeks']),
          tf('For the function y = 4x, the output is 0 when the input is 0.'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.a
    S('6.NS.C.6.a', 'Find opposites; the opposite of the opposite of a number',
      main=[
          sa('What is the opposite of -7?', 'Opposite:'),
          sa('Simplify.\n-(-12)', 'Value:'),
          mc('Which number is the opposite of the number at point P?', ['5', '-5', '0', '{1/5}'], fig=nl(-6, 6, 1, pts=[(-5, 'P')])),
          tf('The opposite of 0 is 0.'),
          sa('What is the opposite of the opposite of 9?', 'Answer:'),
      ],
      back=[
          B('Distance from 0 on a number line', '2.MD.B.6', [
              sa('How far is point A from 0?', 'Units:', fig=nl(0, 10, 1, pts=[(4, 'A')])),
              sa('How many units from 0 is the number 8?', 'Units:'),
              mc('Which number is 2 units from 0 on this number line?', ['2', '0', '4', '20'], fig=nl(0, 10, 1)),
              sa('What number does point K represent?', 'Number:', fig=nl(0, 12, 1, pts=[(9, 'K')])),
              tf('The distance from 0 to 7 is 7 units.'),
          ]),
          B('Positive and negative numbers in context', '6.NS.C.5', [
              tf('-5 can represent 5 degrees below zero.'),
              sa('Write an integer for a gain of 12 yards.', 'Integer:'),
              mc('Which integer represents 20 feet below sea level?', ['-20', '20', '0', '-2']),
              sa('Write an integer for a loss of $7.', 'Integer:'),
              tf('A deposit of $15 is written as -15.'),
          ]),
      ],
      f1=B('Subtract by adding the opposite', '7.NS.A.1.c', [
          sa('Rewrite 5 - 8 as an addition expression.', 'Expression:'),
          sa('Find the value.\n-3 - (-7)', 'Value:'),
          tf('6 - (-2) = 6 + 2'),
          mc('Which expression is equal to -4 - 9?', ['-4 + (-9)', '-4 + 9', '4 + 9', '4 - (-9)']),
          sa('Find the value.\n2.5 - 6', 'Value:'),
      ]),
      f2=B('Solve equations by adding opposites to both sides', '8.EE.C.7.b', [
          sa('Solve for x.\n5x - 7 = 2x + 8', 'x ='),
          sa('Solve for x.\n-3x + 4 = 3x - 8', 'x ='),
          mc('Solve for x.\n6 - 2x = 4x - 12', ['3', '-3', '1', '9']),
          sa('Solve for x.\n7x + 3 = -2x + 21', 'x ='),
          sa('Solve for x.\n4(x - 1) = 2x + 10', 'x ='),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.b quadrants
    S('6.NS.C.6.b', 'Use signs of coordinates to identify quadrants',
      main=[
          mc('In which quadrant is the point (-4, 7)?', ['Quadrant II', 'Quadrant I', 'Quadrant III', 'Quadrant IV']),
          mc('In which quadrant is the point (3, -8)?', ['Quadrant IV', 'Quadrant I', 'Quadrant II', 'Quadrant III']),
          mc('In which quadrant is the point (-2.5, -6)?', ['Quadrant III', 'Quadrant I', 'Quadrant II', 'Quadrant IV']),
          sa('A point has a negative x-coordinate and a positive y-coordinate.\nIn which quadrant is it?', 'Quadrant:'),
          mc('Which point is in Quadrant III?', ['(-5, -1)', '(5, -1)', '(-5, 1)', '(5, 1)']),
      ],
      back=[
          B('Axes, origin, and ordered pairs', '5.G.A.1', [
              tf('The origin is the point (0, 0).'),
              mc('In the ordered pair (5, 2), which number tells how far to move along the x-axis?', ['5', '2', '7', '3']),
              sa('What is the name of the point where the x-axis and the y-axis meet?', 'Name:'),
              tf('In the ordered pair (3, 8), the y-coordinate is 3.'),
              mc('Which axis is horizontal?', ['The x-axis', 'The y-axis']),
          ]),
          B('Negative numbers are on the opposite side of 0', '6.NS.C.6.a', [
              tf('On a horizontal number line, -4 is to the left of 0.'),
              mc('On a vertical number line, where is -3?', ['Below 0', 'Above 0', 'At 0', 'Above 3']),
              tf('On a vertical number line, 5 is below 0.'),
              sa('On a horizontal number line, is 2.5 to the left or the right of 0?', 'Answer:'),
              mc('Which number is to the left of 0 on a horizontal number line?', ['-6', '6', '0', '{1/2}']),
          ]),
          B('Reading points in the first quadrant', '5.G.A.2', [
              sa('What are the coordinates of point B?', 'B =', fig=q1(8, 8, pts=[(5, 4, 'B')])),
              mc('Which point is located at (2, 6)?', LET, fig=q1(8, 8, pts=[(2, 6, 'A'), (6, 2, 'B'), (2, 2, 'C'), (6, 6, 'D')])),
              sa('What are the coordinates of point T?', 'T =', fig=q1(8, 8, pts=[(7, 0, 'T', 'n')])),
              tf('Point R is located at (2, 4).', fig=q1(8, 8, pts=[(4, 2, 'R')])),
              sa('What are the coordinates of point W?', 'W =', fig=q1(8, 8, pts=[(1, 6, 'W')])),
          ]),
      ],
      f1=B('Signs of products of rational numbers', '7.NS.A.2.a', [
          sa('The point (x, y) is in Quadrant II.\nIs the product xy positive or negative?', 'Answer:'),
          sa('The point (x, y) is in Quadrant III.\nIs the product xy positive or negative?', 'Answer:'),
          mc('For the point (x, y), the product xy is positive and x is negative.\nIn which quadrant is the point?', ['Quadrant III', 'Quadrant I', 'Quadrant II', 'Quadrant IV']),
          tf('If (x, y) is in Quadrant IV, then the product xy is negative.'),
          sa('Find the product of the coordinates of the point (-3, 5).', 'Product:'),
      ]),
      f2=B('Transformations and the quadrant of the image', '8.G.A.3', [
          sa('The point (2, 5) is rotated 180° about the origin.\nWhat are the coordinates of the image, and in which quadrant is it?', ['Image:', 'Quadrant:']),
          mc('A point in Quadrant II is reflected across the y-axis.\nIn which quadrant is the image?', ['Quadrant I', 'Quadrant III', 'Quadrant IV', 'Quadrant II']),
          sa('The point (-3, -4) is rotated 90° counterclockwise about the origin.\nWhat are the coordinates of the image?', 'Image:'),
          tf('Translating (1, 2) 5 units to the left moves it into Quadrant II.'),
          mc('The point (4, -1) is reflected across the x-axis.\nIn which quadrant is the image?', ['Quadrant I', 'Quadrant IV', 'Quadrant II', 'Quadrant III']),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.b reflections
    S('6.NS.C.6.b', 'Reflect points across one or both axes',
      main=[
          sa('The point (3, -5) is reflected across the x-axis.\nWhat are the coordinates of its image?', 'Image:'),
          sa('The point (-2, 6) is reflected across the y-axis.\nWhat are the coordinates of its image?', 'Image:'),
          sa('Point A is reflected across the y-axis.\nWhat are the coordinates of its image?', 'Image:', fig=coord(pts=[(-4, 3, 'A')])),
          mc('Which point is the reflection of (-7, -2) across the x-axis?', ['(-7, 2)', '(7, -2)', '(7, 2)', '(-2, -7)']),
          sa('Point B(5, 1) is reflected across the y-axis and then across the x-axis.\nWhat are the coordinates of the final image?', 'Image:'),
      ],
      back=[
          B('Opposite numbers', '6.NS.C.6.a', [
              sa('What is the opposite of 6?', 'Opposite:'),
              tf('The opposite of -9 is 9.'),
              mc('Which pair of numbers are opposites?', ['-4 and 4', '-4 and -4', '4 and {1/4}', '0 and 4']),
              sa('What is the opposite of -2.5?', 'Opposite:'),
              tf('-(-3) = -3'),
          ]),
          B('Lines of symmetry', '4.G.A.3', [
              tf('A line of symmetry divides a figure into two matching halves.'),
              mc('How many lines of symmetry does a square have?', ['4', '2', '1', '0']),
              tf('The dashed line is a line of symmetry of the rectangle.', fig=SYM),
              mc('Which letter has a vertical line of symmetry?', ['A', 'F', 'J', 'R']),
              sa('How many lines of symmetry does a rectangle that is not a square have?', 'Lines:'),
          ]),
          B('Reading coordinates in the first quadrant', '5.G.A.2', [
              sa('What are the coordinates of point E?', 'E =', fig=q1(8, 8, pts=[(3, 6, 'E')])),
              sa('What are the coordinates of point F?', 'F =', fig=q1(8, 8, pts=[(6, 3, 'F')])),
              mc('Which point is located at (4, 0)?', LET, fig=q1(8, 8, pts=[(4, 0, 'A', 'n'), (0, 4, 'B', 'e'), (4, 4, 'C'), (1, 4, 'D')])),
              tf('Point H is located at (5, 2).', fig=q1(8, 8, pts=[(2, 5, 'H')])),
              sa('What are the coordinates of point G?', 'G =', fig=q1(8, 8, pts=[(0, 3, 'G', 'e')])),
          ]),
      ],
      f1=B('Distance between a point and its reflection', '7.NS.A.1.c', [
          sa('The point (3, -4.5) is reflected across the x-axis.\nHow far apart are the point and its image?', 'Distance:'),
          sa('The point (-6.5, 2) is reflected across the y-axis.\nHow far apart are the point and its image?', 'Distance:'),
          mc('The point (1, -2{1/2}) is reflected across the x-axis.\nHow far apart are the point and its image?', ['5', '2{1/2}', '0', '-5']),
          sa('A point in Quadrant I and its reflection across the y-axis are 11 units apart. The point\'s y-coordinate is 7.\nWhat is the point\'s x-coordinate?', 'x ='),
          tf('The point (-4, 3) and its reflection across the x-axis are 6 units apart.'),
      ]),
      f2=B('Reflections and rotations with coordinates', '8.G.A.3', [
          sa('A triangle has a vertex at (2, -3). The triangle is reflected across the y-axis.\nWhat are the coordinates of the image of that vertex?', 'Image:'),
          mc('Which transformation is described by (x, y) → (x, -y)?', ['A reflection across the x-axis', 'A reflection across the y-axis', 'A rotation of 180°', 'A translation']),
          sa('The point (4, 1) is rotated 180° about the origin.\nWhat are the coordinates of its image?', 'Image:'),
          sa('Triangle ABC is reflected across the x-axis.\nWhat are the coordinates of B′?', 'B′ =',
             fig=coord(pts=[(1, 2, 'A', 'nw'), (4, 5, 'B'), (5, 1, 'C', 'se')], polys=[[(1, 2), (4, 5), (5, 1)]])),
          tf('Reflecting (-3, 5) across the y-axis gives (3, 5).'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.c name on number line
    S('6.NS.C.6.c', 'Name the rational number at a point on a number line',
      main=[
          sa('What number does point P represent?', 'P =', fig=nl(-3, 3, 0.5, labels=[-3, -2, -1, 0, 1, 2, 3], pts=[(-1.5, 'P')])),
          sa('Write the number at point Q as a mixed number.', 'Q =', fig=nl(-2, 2, 0.25, labels=[-2, -1, 0, 1, 2], pts=[(-1.25, 'Q')])),
          tf('Point R is located at -0.4.', fig=nl(-1, 1, 0.1, labels=[-1, 0, 1], pts=[(-0.4, 'R')])),
          sa('The number line shows elevations in meters.\nWhat elevation does point S show?', 'S =', fig=nl(-30, 30, 10, vertical=True, pts=[(-20, 'S')]), pos='right'),
          sa('Write the number at point T as a fraction.', 'T =', fig=nl(-2, 1, 1 / 3, labels={-2: '-2', -1: '-1', 0: '0', 1: '1'}, pts=[(-2 / 3, 'T')])),
      ],
      back=[
          B('Fractions on a number line', '3.NF.A.2', [
              sa('What fraction does point A represent?', 'A =', fig=nl(0, 1, 0.25, labels={0: '0', 1: '1'}, pts=[(0.75, 'A')])),
              sa('What fraction does point B represent?', 'B =', fig=nl(0, 1, 1 / 3, labels={0: '0', 1: '1'}, pts=[(1 / 3, 'B')])),
              tf('Point C is located at {5/6}.', fig=nl(0, 1, 1 / 6, labels={0: '0', 1: '1'}, pts=[(5 / 6, 'C')])),
              mc('The space from 0 to 1 is split into equal parts.\nHow many equal parts are there?', ['8', '7', '9', '10'], fig=nl(0, 1, 0.125, labels={0: '0', 1: '1'})),
              sa('Write the number at point D as a fraction.', 'D =', fig=nl(0, 2, 0.5, labels={0: '0', 1: '1', 2: '2'}, pts=[(1.5, 'D')])),
          ]),
          B('Decimals on a number line', '4.NF.C.6', [
              sa('What decimal does point A represent?', 'A =', fig=nl(0, 1, 0.1, labels=[0, 1], pts=[(0.7, 'A')])),
              sa('What decimal does point B represent?', 'B =', fig=nl(2, 3, 0.1, labels=[2, 3], pts=[(2.4, 'B')])),
              tf('Point C is located at 0.3.', fig=nl(0, 1, 0.1, labels=[0, 1], pts=[(0.3, 'C')])),
              mc('What decimal does point D represent?', ['0.26', '2.6', '0.206', '0.62'], fig=nl(0.2, 0.3, 0.01, labels={0.2: '0.2', 0.3: '0.3'}, pts=[(0.26, 'D')])),
              sa('What decimal does point E represent?', 'E =', fig=nl(5, 6, 0.1, labels=[5, 6], pts=[(5.9, 'E')])),
          ]),
          B('Opposites on a number line', '6.NS.C.6.a', [
              sa('Point B (not shown) is the opposite of point A.\nWhat number is at point B?', 'B =', fig=nl(-5, 5, 1, pts=[(3, 'A')])),
              tf('-2.5 and 2.5 are the same distance from 0.'),
              mc('What is the opposite of 1{3/4}?', ['-1{3/4}', '1{3/4}', '-{4/7}', '{4/7}']),
              sa('What is the opposite of -0.8?', 'Opposite:'),
              tf('Points A and B represent opposite numbers.', fig=nl(-5, 5, 1, pts=[(-4, 'A'), (3, 'B')])),
          ]),
      ],
      f1=B('Addition shown on a number line', '7.NS.A.1.b', [
          sa('Start at -2.5 on a number line and move 4 units to the right.\nWhere do you end?', 'Number:'),
          sa('The number line shows 1 + (-4).\nWhat is the sum?', 'Sum:', fig=nl(-5, 5, 1, jumps=[(1, -3, '-4')])),
          mc('Which expression does the number line show?', ['-3 + 5', '5 + 3', '-3 - 5', '2 + 5'], fig=nl(-5, 5, 1, jumps=[(-3, 2, '+5')])),
          sa('The number line shows -0.5 + (-1.5).\nWhat is the sum?', 'Sum:', fig=nl(-3, 1, 0.5, labels=[-3, -2, -1, 0, 1], jumps=[(-0.5, -2, '-1.5')])),
          tf('On a number line, -3 + 7 is 7 units to the right of -3.'),
      ]),
      f2=B('Approximate irrational numbers on a number line', '8.NS.A.2', [
          sa('Between which two consecutive whole numbers is √20?', 'Between:'),
          mc('Which point best shows √10?', LET, fig=nl(0, 5, 0.5, labels=[0, 1, 2, 3, 4, 5], pts=[(3.16, 'A'), (2.5, 'B'), (3.8, 'C'), (1, 'D')])),
          sa('Estimate √50 to the nearest tenth.', 'Estimate:'),
          mc('Which list is ordered from least to greatest?', ['√5, 2.5, √8', '2.5, √5, √8', '√8, √5, 2.5', '√5, √8, 2.5']),
          tf('π is between 3.1 and 3.2 on the number line.'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.c plot on number line
    S('6.NS.C.6.c', 'Plot rational numbers on a horizontal or vertical number line',
      main=[
          plot('Plot and label point A at -2.5 on the number line.', nl(-4, 4, 0.5, labels=[-4, -3, -2, -1, 0, 1, 2, 3, 4])),
          plot('Plot and label point B at -{3/4} on the number line.', nl(-2, 2, 0.25, labels=[-2, -1, 0, 1, 2])),
          plot('Plot and label -1.2 and its opposite on the number line.', nl(-2, 2, 0.1, labels=[-2, -1, 0, 1, 2])),
          plot('The number line shows elevations in feet.\nPlot and label point C at -35 feet.', nl(-50, 50, 10, vertical=True), pos='right'),
          plot('Plot and label point D at 1{2/3} on the number line.', nl(-2, 2, 1 / 3, labels={-2: '-2', -1: '-1', 0: '0', 1: '1', 2: '2'})),
      ],
      back=[
          B('Placing fractions on a number line', '3.NF.A.2', [
              plot('Plot and label {3/4} on the number line.', nl(0, 1, 0.25, labels={0: '0', 1: '1'})),
              plot('Plot and label {2/3} on the number line.', nl(0, 1, 1 / 3, labels={0: '0', 1: '1'})),
              mc('Which point is at {1/2}?', LET, fig=nl(0, 1, 0.25, labels={0: '0', 1: '1'}, pts=[(0.5, 'A'), (0.25, 'B'), (0.75, 'C'), (1, 'D')])),
              plot('Plot and label {5/6} on the number line.', nl(0, 1, 1 / 6, labels={0: '0', 1: '1'})),
              tf('To plot {3/8}, count 3 of the 8 equal parts from 0.', fig=nl(0, 1, 0.125, labels={0: '0', 1: '1'})),
          ]),
          B('Placing decimals on a number line', '4.NF.C.6', [
              plot('Plot and label 0.7 on the number line.', nl(0, 1, 0.1, labels=[0, 1])),
              plot('Plot and label 2.4 on the number line.', nl(2, 3, 0.1, labels=[2, 3])),
              mc('Which point is at 0.6?', LET, fig=nl(0, 1, 0.1, labels=[0, 1], pts=[(0.6, 'A'), (0.4, 'B'), (0.1, 'C'), (1, 'D')])),
              plot('Plot and label 0.35 on the number line.', nl(0.3, 0.4, 0.01, labels={0.3: '0.3', 0.4: '0.4'})),
              tf('On a number line marked in tenths, 0.9 is one tick mark to the left of 1.'),
          ]),
          B('Opposites on a number line', '6.NS.C.6.a', [
              plot('Point A is at 3. Plot and label its opposite.', nl(-5, 5, 1, pts=[(3, 'A')])),
              plot('Plot and label 2 and -2 on the number line.', nl(-5, 5, 1)),
              tf('A number and its opposite are the same distance from 0.'),
              mc('Point B is at -1.5. Where is its opposite?', ['At 1.5', 'At -1.5', 'At 0', 'At 0.15']),
              plot('Plot and label the opposite of -4.', nl(-5, 5, 1)),
          ]),
      ],
      f1=B('Represent addition on a number line', '7.NS.A.1.b', [
          sa('Draw an arrow on the number line to show -2 + 3.5.\nWhat is the sum?', 'Sum:', fig=nl(-4, 4, 0.5, labels=[-4, -3, -2, -1, 0, 1, 2, 3, 4])),
          sa('Draw arrows on the number line to show 1.5 + (-3).\nWhat is the sum?', 'Sum:', fig=nl(-4, 4, 0.5, labels=[-4, -3, -2, -1, 0, 1, 2, 3, 4])),
          sa('Draw arrows on the vertical number line to show -10 + 25.\nWhat is the sum?', 'Sum:', fig=nl(-30, 30, 5, labels=[-30, -20, -10, 0, 10, 20, 30], vertical=True), pos='right'),
          mc('An arrow on a number line starts at -{1/2} and moves {3/4} unit to the right.\nWhere does it end?', ['{1/4}', '-1{1/4}', '{3/4}', '-{1/4}']),
          sa('Draw arrows on the number line to show -1{1/4} + (-{3/4}).\nWhat is the sum?', 'Sum:', fig=nl(-3, 1, 0.25, labels=[-3, -2, -1, 0, 1])),
      ]),
      f2=B('Locate irrational numbers approximately on a number line', '8.NS.A.2', [
          plot('Plot √10 at its approximate location on the number line.', nl(0, 5, 0.5, labels=[0, 1, 2, 3, 4, 5])),
          plot('Plot √2 at its approximate location on the number line.', nl(0, 2, 0.1, labels=[0, 1, 2])),
          plot('Plot π at its approximate location on the number line.', nl(3, 4, 0.1, labels=[3, 4])),
          plot('Plot -√5 at its approximate location on the number line.', nl(-4, 0, 0.5, labels=[-4, -3, -2, -1, 0])),
          plot('Plot √30 at its approximate location on the number line.', nl(4, 7, 0.5, labels=[4, 5, 6, 7])),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.c name coordinates
    S('6.NS.C.6.c', 'Name the coordinates of points in all four quadrants',
      main=[
          sa('What are the coordinates of point A?', 'A =', fig=coord(pts=[(-4, 3, 'A')])),
          sa('What are the coordinates of point B?', 'B =', fig=coord(pts=[(2, -5, 'B')])),
          sa('What are the coordinates of point C?', 'C =', fig=coord(pts=[(-3, -2, 'C')])),
          mc('Which ordered pair names point M?', ['(0, -4)', '(-4, 0)', '(4, 0)', '(0, 4)'], fig=coord(pts=[(0, -4, 'M', 'e')])),
          sa('What are the coordinates of point K?', 'K =', fig=coord(pts=[(-5, -1, 'K')])),
      ],
      back=[
          B('Ordered pairs and the axes', '5.G.A.1', [
              tf('The x-coordinate tells how far to move from the origin along the x-axis.'),
              mc('In the ordered pair (7, 3), what is the y-coordinate?', ['3', '7', '10', '4']),
              sa('The x-axis and the y-axis cross at a point.\nWhat are its name and coordinates?', ['Name:', 'Coordinates:']),
              tf('(2, 5) and (5, 2) name the same point.'),
              mc('In an ordered pair, which number is written first?', ['The x-coordinate', 'The y-coordinate', 'The larger number', 'The smaller number']),
          ]),
          B('Reading points in the first quadrant', '5.G.A.2', [
              sa('What are the coordinates of point E?', 'E =', fig=q1(8, 8, pts=[(4, 7, 'E')])),
              sa('What are the coordinates of point F?', 'F =', fig=q1(8, 8, pts=[(7, 2, 'F')])),
              mc('Which point is located at (0, 5)?', LET, fig=q1(8, 8, pts=[(0, 5, 'A', 'e'), (5, 0, 'B', 'n'), (5, 5, 'C'), (2, 5, 'D')])),
              tf('Point H is located at (6, 1).', fig=q1(8, 8, pts=[(1, 6, 'H')])),
              sa('What are the coordinates of point G?', 'G =', fig=q1(8, 8, pts=[(6, 0, 'G', 'n')])),
          ]),
          B('Quadrants and signs of coordinates', '6.NS.C.6.b', [
              mc('In which quadrant are both coordinates negative?', ['Quadrant III', 'Quadrant I', 'Quadrant II', 'Quadrant IV']),
              mc('In which quadrant is (5, -2)?', ['Quadrant IV', 'Quadrant I', 'Quadrant II', 'Quadrant III']),
              tf('(-3, 4) is in Quadrant II.'),
              sa('A point is in Quadrant IV.\nWrite "positive" or "negative" for each coordinate.', ['x-coordinate:', 'y-coordinate:']),
              tf('The point (0, -6) is in Quadrant III.'),
          ]),
      ],
      f1=B('Interpret a point on the graph of a proportional relationship', '7.RP.A.2.d', [
          sa('The graph shows the cost of apples.\nWhat does the point (2, 8) represent?', 'Meaning:',
             fig=q1(5, 20, ystep=4, square=False, xlabel='Pounds', ylabel='Cost ($)', pts=[(1, 4), (2, 8), (3, 12)], lines=[((0, 0), (5, 20))])),
          mc('The graph shows the cost of apples.\nWhat does the point (1, 4) represent?', ['1 pound costs $4.', '4 pounds cost $1.', 'The cost starts at $4.', '$1 buys 4 pounds.'],
             fig=q1(5, 20, ystep=4, square=False, xlabel='Pounds', ylabel='Cost ($)', pts=[(1, 4), (2, 8), (3, 12)], lines=[((0, 0), (5, 20))])),
          tf('On the graph of a proportional relationship between pounds and cost, the point (0, 0) means 0 pounds cost $0.'),
          sa('The graph of a proportional relationship passes through (1, r) and (5, 30).\nWhat is r?', 'r ='),
          mc('A graph shows the distance y in miles after x hours. It passes through (3, 150).\nWhat does this point mean?',
             ['In 3 hours, the distance is 150 miles.', 'In 150 hours, the distance is 3 miles.', 'The speed is 3 miles per hour.', 'The speed is 150 miles per hour.']),
      ]),
      f2=B('A function as a set of ordered pairs', '8.F.A.1', [
          tf('The set of ordered pairs (1, 2), (2, 4), (3, 6), (4, 8) represents a function.'),
          mc('Which set of ordered pairs does NOT represent a function?', ['(2, 5), (2, 7), (3, 9)', '(1, 4), (2, 4), (3, 4)', '(0, 0), (1, 1), (2, 2)', '(-1, 3), (0, 5), (1, 7)']),
          sa('Does the set (4, 1), (5, 2), (4, 3) represent a function? Write yes or no.', 'Answer:'),
          tf('The graph represents a function.', fig=coord(pts=[(-3, 2), (-1, -2), (1, 3), (3, -1)])),
          mc('A function assigns to each input ___.', ['exactly one output', 'at least two outputs', 'the same output as the input', 'no output']),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.6.c plot on coordinate plane
    S('6.NS.C.6.c', 'Plot points in all four quadrants',
      main=[
          plot('Plot and label point P(-3, 4) and point Q(2, -5).', coord()),
          plot('Plot and label point R(-5, -2) and point S(4, 1).', coord()),
          plot('Plot and label point T(0, -3) and point U(-4, 0).', coord()),
          plot('Plot and label point V(-2.5, 3) and point W(1.5, -2).', coord()),
          plot('Plot and label point X(-6, -6) and point Y(5, -4).', coord()),
      ],
      back=[
          B('Which direction to move first', '5.G.A.1', [
              tf('To plot (6, 1), first move 6 units along the x-axis.'),
              mc('To plot (2, 7) from the origin, what do you do first?', ['Move 2 units right', 'Move 7 units up', 'Move 2 units up', 'Move 7 units right']),
              tf('To plot (0, 5), you do not move left or right.'),
              sa('To plot (4, 3), how many units up do you move?', 'Units:'),
              mc('Which ordered pair is 3 units right and 6 units up from the origin?', ['(3, 6)', '(6, 3)', '(3, 3)', '(6, 6)']),
          ]),
          B('Plotting points in the first quadrant', '5.G.A.2', [
              plot('Plot and label point A at (2, 6).', q1(8, 8)),
              plot('Plot and label point B at (5, 1).', q1(8, 8)),
              plot('Plot and label point C at (0, 7).', q1(8, 8)),
              plot('Plot and label point D at (7, 7).', q1(8, 8)),
              plot('Plot and label point E at (5, 0).', q1(8, 8)),
          ]),
          B('Direction from the sign of a coordinate', '6.NS.C.6.b', [
              tf('To plot a point with a negative x-coordinate, you move left from the origin.'),
              mc('To plot (-2, -5), which directions do you move?', ['Left 2, down 5', 'Right 2, up 5', 'Left 5, down 2', 'Right 2, down 5']),
              tf('To plot (3, -4), you move up 4 units.'),
              sa('To plot (-6, 1), do you move left or right?', 'Answer:'),
              mc('Which point is left of the y-axis and above the x-axis?', ['(-3, 2)', '(3, 2)', '(-3, -2)', '(3, -2)']),
          ]),
      ],
      f1=B('Graph pairs to decide whether a relationship is proportional', '7.RP.A.2.a', [
          sa('Graph the pairs (1, 3), (2, 6), and (3, 9).\nDo they lie on a straight line through the origin?', 'Answer:', fig=q1(5, 12, ystep=2, square=False)),
          sa('Graph the pairs (1, 3), (2, 5), and (3, 7).\nIs the relationship proportional?', 'Answer:', fig=q1(5, 10, square=False)),
          sa('Graph the pairs from the table.\nIs the relationship proportional?', 'Answer:',
             fig=hrow(table([['x', '1', '2', '4'], ['y', '2.5', '5', '10']], fs=0.9), q1(5, 10, square=False), h=230)),
          tf('The points (2, 1), (4, 2), and (6, 3) lie on a line through the origin, so the relationship is proportional.'),
          mc('Which set of pairs would graph as a proportional relationship?', ['(2, 3), (4, 6), (6, 9)', '(1, 3), (2, 4), (3, 5)', '(0, 2), (1, 4), (2, 6)', '(1, 1), (2, 4), (3, 9)']),
      ]),
      f2=B('Graph proportional relationships', '8.EE.B.5', [
          sa('Graph y = 0.5x on the coordinate plane.\nWhat is the slope of the line?', 'Slope:', fig=q1(8, 4, square=False)),
          sa('Graph y = 4x on the coordinate plane.\nWhat is the slope of the line?', 'Slope:', fig=q1(4, 16, ystep=2, square=False)),
          sa('A car travels 50 miles per hour. Graph the distance y after x hours.\nWhat is the slope?', 'Slope:', fig=q1(5, 250, ystep=50, square=False, xlabel='Hours', ylabel='Miles')),
          mc('Which point is on the graph of y = 3x?', ['(4, 12)', '(12, 4)', '(3, 1)', '(4, 7)']),
          tf('The graph of y = {2/3}x passes through (3, 2).'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.7.a
    S('6.NS.C.7.a', 'Interpret inequalities as relative position on a number line',
      main=[
          mc('-4 > -10\nWhich statement explains this inequality?', ['-4 is to the right of -10 on a number line.', '-4 is to the left of -10 on a number line.', '4 is less than 10.', '-4 is farther from 0 than -10.']),
          tf('The number line shows that -6 > -1.', fig=nl(-8, 2, 1, pts=[(-6, 'A'), (-1, 'B')])),
          sa('Write an inequality that compares -4 and -9.', 'Inequality:'),
          mc('Which statement is true?', ['-5 < -2', '-5 > -2', '-2 < -5', '-5 > 0']),
          sa('Write an inequality using the numbers at points P and Q.', 'Inequality:', fig=nl(-5, 5, 1, pts=[(-2, 'P'), (1, 'Q')])),
      ],
      back=[
          B('Comparison symbols', '2.NBT.A.4', [
              sa('Write >, <, or = to compare.\n452 ___ 425', 'Symbol:'),
              tf('67 < 76'),
              mc('Which statement is true?', ['309 > 290', '309 < 290', '309 = 290']),
              sa('Write >, <, or = to compare.\n138 ___ 183', 'Symbol:'),
              tf('500 > 505'),
          ]),
          B('Position on a number line', '2.MD.B.6', [
              tf('On a number line, 8 is to the right of 3.'),
              mc('Which number is farthest to the left on a number line?', ['2', '7', '5', '9']),
              sa('Which point is farther to the left, A or B?', 'Point:', fig=nl(0, 10, 1, pts=[(6, 'A'), (2, 'B')])),
              tf('Numbers get greater as you move to the left on a number line.'),
              mc('Which number is to the right of 14 on a number line?', ['19', '11', '9', '14']),
          ]),
          B('Negative numbers on a number line', '6.NS.C.6.c', [
              sa('What number is at point A?', 'A =', fig=nl(-8, 2, 1, pts=[(-6, 'A')])),
              mc('Which point is at -3?', LET, fig=nl(-5, 5, 1, pts=[(-3, 'A'), (3, 'B'), (-2, 'C'), (-4, 'D')])),
              tf('-4 is to the left of -1 on a number line.'),
              sa('What number is at point B?', 'B =', fig=nl(-10, 0, 2, pts=[(-8, 'B')])),
              mc('Which point is at -5?', LET, fig=nl(-6, 0, 1, pts=[(-1, 'A'), (-5, 'B'), (-6, 'C'), (-4, 'D')])),
          ]),
      ],
      f1=B('Solve and graph inequalities', '7.EE.B.4.b', [
          mc('Which inequality does the graph show?', ['x > 3', 'x ≥ 3', 'x < 3', 'x ≤ 3'], fig=nl(-5, 5, 1, ray=(3, 'right', True))),
          sa('Solve the inequality.\n2x + 5 > 11', 'Solution:'),
          sa('Solve the inequality.\n-3x + 4 ≤ 16', 'Solution:'),
          tf('The graph shows the solutions of 4x - 1 ≤ -9.', fig=nl(-5, 5, 1, ray=(-2, 'left', False))),
          sa('Solve the inequality.\n5x - 2 < 18', 'Solution:'),
      ]),
      f2=B('Compare and order irrational numbers', '8.NS.A.2', [
          sa('Which is greater, √50 or 7.2?', 'Greater:'),
          mc('Which number is between 3 and 4?', ['√12', '√8', '√17', '√3']),
          tf('√30 < 5.5'),
          sa('Order from least to greatest.\nπ, √8, 3.1', 'Order:'),
          mc('Which point best shows -√5?', LET, fig=nl(-4, 0, 0.5, labels=[-4, -3, -2, -1, 0], pts=[(-2.24, 'A'), (-1.5, 'B'), (-2.8, 'C'), (-3.5, 'D')])),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.7.b
    S('6.NS.C.7.b', 'Write, interpret, and explain order statements in real-world contexts',
      main=[
          sa('A temperature of -2°F is warmer than a temperature of -11°F.\nWrite an inequality to show this.', 'Inequality:'),
          mc('Account A has a balance of -$25. Account B has a balance of -$40.\nWhich statement is true?',
             ['-25 > -40, so Account A has the greater balance.', '-40 > -25, so Account B has the greater balance.', '-25 < -40, so Account A owes more.', 'The balances are equal.']),
          sa('A fish swims at -12 feet. A turtle swims at -5 feet.\nWrite an inequality to compare the positions. Which animal is deeper?', ['Inequality:', 'Deeper animal:']),
          tf('-15 < -10 means that -15°F is colder than -10°F.'),
          mc('The lowest point in a valley is -86 meters. A beach is at 0 meters.\nWhich statement is true?',
             ['-86 < 0, so the valley\'s lowest point is lower.', '-86 > 0, so the valley\'s lowest point is higher.', '0 < -86, so the beach is lower.', '-86 = 0']),
      ],
      back=[
          B('Negative numbers in context', '6.NS.C.5', [
              sa('Write an integer for 12 degrees below zero.', 'Integer:'),
              tf('A debt of $30 can be written as -30.'),
              mc('Which situation could be represented by -6?', ['A loss of 6 yards', 'A gain of 6 yards', '6 feet above sea level', 'A deposit of $6']),
              sa('Write an integer for 50 feet below sea level.', 'Integer:'),
              tf('A temperature of 4 degrees above zero is written as -4.'),
          ]),
          B('Inequality symbols', '1.NBT.B.3', [
              mc('Which symbol makes this true?\n42 ___ 24', ['>', '<', '=']),
              tf('15 > 51'),
              sa('Write >, <, or = to compare.\n73 ___ 37', 'Symbol:'),
              mc('Which symbol means "is less than"?', ['<', '>', '=']),
              tf('89 < 98'),
          ]),
          B('Order as position on a number line', '6.NS.C.7.a', [
              tf('-2 > -6 because -2 is to the right of -6 on a number line.'),
              mc('Which number is greatest?', ['-1', '-4', '-9', '-7']),
              sa('-5 is to the left of 3 on a number line.\nWrite an inequality to show this.', 'Inequality:'),
              tf('-8 is to the right of -3 on a number line.'),
              mc('Which number is to the left of -4 on a number line?', ['-6', '-2', '0', '4']),
          ]),
      ],
      f1=B('Write and solve inequalities for real-world situations', '7.EE.B.4.b', [
          sa('A submarine at -40 m descends 12 m per minute. It must stay above -160 m.\nWrite and solve an inequality for the number of minutes t it can descend.', 'Solution:'),
          sa('You have $25 and spend $4 per day. You want to keep at least $5.\nWrite and solve an inequality for the number of days d.', 'Solution:'),
          mc('A freezer is at 2°C. It cools 3°C per hour.\nFor which numbers of hours h is its temperature below -10°C?', ['h > 4', 'h < 4', 'h > -4', 'h < -4']),
          sa('A diver at -8 ft descends 5 ft per minute.\nWrite and solve an inequality to find when the diver is deeper than -48 ft.', 'Solution:'),
          tf('The solution of -2x + 1 > 9 is x < -4.'),
      ]),
      f2=B('Compare quantities written with powers of 10', '8.EE.A.3', [
          sa('A mountain is about 9 × 10³ m tall. An ocean trench is about -1.1 × 10⁴ m deep.\nWhich is farther from sea level?', 'Answer:'),
          mc('Which number is greater?', ['3 × 10⁻²', '8 × 10⁻³']),
          sa('A city has about 2 × 10⁶ people. A town has about 5 × 10⁴ people.\nHow many times as many people live in the city?', 'Times as many:'),
          sa('Order from least to greatest.\n4 × 10³, 9 × 10², 1 × 10⁴', 'Order:'),
          tf('-5 × 10³ < -2 × 10³'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.7.c distance
    S('6.NS.C.7.c', 'Find absolute value as distance from 0',
      main=[
          sa('Find the value.\n|-18|', 'Value:'),
          mc('Which number has the greatest absolute value?', ['-12', '8', '-5', '10']),
          sa('How far is -7.5 from 0 on a number line?', 'Distance:'),
          tf('|-6| = |6|'),
          sa('Which two numbers have an absolute value of 11?', 'Numbers:'),
      ],
      back=[
          B('Distance on a number line', '2.MD.B.6', [
              sa('How many units apart are points A and B?', 'Units:', fig=nl(0, 12, 1, pts=[(3, 'A'), (9, 'B')])),
              tf('The distance from 0 to 5 is the same as the distance from 5 to 10.'),
              mc('How many units from 0 is the number 11?', ['11', '0', '1', '10']),
              sa('What is the distance from 4 to 10 on a number line?', 'Distance:'),
              sa('How many units is point C from 0?', 'Units:', fig=nl(0, 20, 2, pts=[(16, 'C')])),
          ]),
          B('Opposite numbers', '6.NS.C.6.a', [
              sa('What is the opposite of 15?', 'Opposite:'),
              tf('Opposite numbers are the same distance from 0.'),
              mc('Which number is the opposite of -{2/3}?', ['{2/3}', '-{3/2}', '{3/2}', '-{2/3}']),
              sa('What is the opposite of 0?', 'Opposite:'),
              tf('Points A and B represent opposite numbers.', fig=nl(-5, 5, 1, pts=[(-3, 'A'), (3, 'B')])),
          ]),
      ],
      f1=B('Distance between rational numbers as |p - q|', '7.NS.A.1.c', [
          sa('Find the distance between -4 and 7 on a number line.', 'Distance:'),
          sa('Find the value.\n|-3.5 - 2|', 'Value:'),
          mc('Which expression gives the distance between -9 and -2?', ['|-9 - (-2)|', '-9 - 2', '|-9 + (-2)|', '-9 + 2']),
          tf('The distance between -6 and 6 is 0.'),
          sa('Find the distance between -2{1/2} and 1{1/4} on a number line.', 'Distance:'),
      ]),
      f2=B('Square roots and cube roots as solutions', '8.EE.A.2', [
          sa('Solve.\nx² = 49', 'x ='),
          sa('Solve.\nx³ = 64', 'x ='),
          mc('What are the solutions of x² = 81?', ['x = 9 or x = -9', 'x = 9 only', 'x = 40.5', 'x = -9 only']),
          sa('Solve. Write the answer using a square root symbol.\nx² = 20', 'x ='),
          tf('Both 6 and -6 are solutions of x² = 36.'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.7.c context
    S('6.NS.C.7.c', 'Interpret absolute value as magnitude in a real-world situation',
      main=[
          sa('An account balance is -$45.\nWhat is the absolute value of the balance, and what does it describe?', ['Absolute value:', 'It describes:']),
          sa('A diver is at an elevation of -42 feet.\nHow far is the diver from sea level?', 'Distance:'),
          mc('A stock\'s value changed by -$8.50 today.\nWhat is the size of the change?', ['$8.50', '-$8.50', '$0', '$17.00']),
          sa('The temperature is -13°F.\nHow many degrees below zero is it?', 'Degrees:'),
          sa('A submarine is at -275 m. A plane is at 275 m.\nWhich is farther from sea level? Explain using absolute value.', 'Answer:'),
      ],
      back=[
          B('Negative numbers in context', '6.NS.C.5', [
              tf('-30 can represent owing $30.'),
              sa('Write an integer for 42 feet below sea level.', 'Integer:'),
              mc('Which situation is represented by +25?', ['A deposit of $25', 'A debt of $25', '25 feet below sea level', 'A loss of 25 yards']),
              sa('Write an integer for a debt of $18.', 'Integer:'),
              tf('A temperature of 0°F means there is no temperature.'),
          ]),
          B('Distance from 0', '2.MD.B.6', [
              sa('How many units from 0 is point A?', 'Units:', fig=nl(0, 10, 1, pts=[(8, 'A')])),
              tf('The distance from 0 to 13 is 13 units.'),
              mc('Which number is 5 units from 0 on this number line?', ['5', '0', '10', '50'], fig=nl(0, 10, 1)),
              sa('How far is 20 from 0 on a number line?', 'Distance:'),
              tf('The number that is 0 units from 0 is 1.'),
          ]),
          B('Opposites are the same distance from 0', '6.NS.C.6.a', [
              tf('-42 and 42 are the same distance from 0.'),
              sa('What is the opposite of -275?', 'Opposite:'),
              mc('Which number is the same distance from 0 as -8.5?', ['8.5', '-5.8', '0', '85']),
              tf('The opposite of 13 is -13.'),
              sa('Name the number that is the same distance from 0 as -45, on the other side of 0.', 'Number:'),
          ]),
      ],
      f1=B('Real-world problems with rational numbers', '7.NS.A.3', [
          sa('A company lost $2.5 million in one year and earned a profit of $1.8 million the next year.\nWhat is the total for the two years?', 'Total:'),
          sa('The temperature was -6°F. It dropped 11°F.\nWhat is the new temperature?', 'Temperature:'),
          mc('A diver at -35.5 feet rises 12.25 feet.\nWhat is the diver\'s new position?', ['-23.25 feet', '-47.75 feet', '23.25 feet', '-22.75 feet']),
          sa('A hiker goes from an elevation of 1,200 feet to an elevation of -80 feet.\nWhat is the change in elevation?', 'Change:'),
          tf('If the temperature drops from -4°C to -9°C, it gets 5°C colder.'),
      ]),
      f2=B('Compare magnitudes with powers of 10', '8.EE.A.3', [
          sa('One company\'s debt is 2 × 10⁶ dollars. Another company\'s debt is 4 × 10⁴ dollars.\nHow many times as large is the first debt?', 'Times as large:'),
          mc('The deepest ocean point is about -1 × 10⁴ meters. A lake bottom is about -5 × 10¹ meters.\nAbout how many times as deep is the ocean point?', ['200', '20', '2,000', '5']),
          sa('Estimate 7,980,000 as a single digit times a power of 10.', 'Estimate:'),
          tf('6 × 10⁹ is 300 times as large as 2 × 10⁷.'),
          sa('Estimate 0.0000031 as a single digit times a power of 10.', 'Estimate:'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.7.d
    S('6.NS.C.7.d', 'Distinguish comparisons of absolute value from statements about order',
      main=[
          tf('An account balance less than -$50 means a debt greater than $50.'),
          mc('Which account balance shows the greatest debt?', ['-$55', '-$20', '-$38', '$10']),
          tf('-12 < -5, so |-12| < |-5|.'),
          sa('Two temperatures are -15°F and -9°F.\nWhich temperature is colder? Which has the greater absolute value?', ['Colder:', 'Greater absolute value:']),
          mc('A submarine is at -300 feet. A diver is at -45 feet.\nWhich statement is true?',
             ['The submarine is deeper because |-300| > |-45|.', 'The diver is deeper because -45 > -300.', 'The submarine is deeper because -300 > -45.', 'They are at the same depth.']),
      ],
      back=[
          B('Absolute value', '6.NS.C.7.c', [
              sa('Find the value.\n|-25|', 'Value:'),
              sa('Find the value.\n|14|', 'Value:'),
              tf('|-3| = -3'),
              mc('Which number has an absolute value of 7?', ['-7', '{1/7}', '0', '-{1/7}']),
              sa('Find the value.\n|-2.5|', 'Value:'),
          ]),
          B('Ordering negative numbers', '6.NS.C.7.a', [
              mc('Which number is least?', ['-20', '-5', '0', '-12']),
              tf('-9 > -4'),
              sa('Order from least to greatest.\n-3, -8, 1', 'Order:'),
              tf('-1 > -100'),
              mc('Which number is greater?', ['-6', '-16']),
          ]),
          B('Negative numbers in context', '6.NS.C.5', [
              sa('Write an integer for a debt of $40.', 'Integer:'),
              mc('What could -8 represent?', ['8 feet below sea level', '8 feet above sea level', 'A gain of 8 yards', 'A deposit of $8']),
              tf('An account balance of -$10 means you owe $10.'),
              sa('Write an integer for 15 degrees below zero.', 'Integer:'),
              tf('A 20-foot descent can be written as +20.'),
          ]),
      ],
      f1=B('Real-world problems with rational numbers', '7.NS.A.3', [
          sa('Two accounts have balances of -$42.50 and -$18.75.\nHow much greater is the larger debt?', 'Difference:'),
          sa('A diver at -24.5 m rises 9.75 m and then descends 15 m.\nWhat is the diver\'s final position?', 'Position:'),
          mc('The temperature at 6 a.m. was -8.5°F. At noon it was 3.5°F.\nHow much did the temperature rise?', ['12°F', '5°F', '-12°F', '-5°F']),
          sa('Maria\'s balance is -$36. She pays back {1/4} of what she owes.\nWhat is her new balance?', 'Balance:'),
          tf('A change from -12 m to -30 m is a change of -18 m.'),
      ]),
      f2=B('Compare the size and order of irrational numbers', '8.NS.A.2', [
          mc('Which number has the greater absolute value?', ['-√20', '4.3']),
          tf('-√10 < -3'),
          sa('Order from least to greatest.\n-√5, -2.5, -2', 'Order:'),
          mc('Which number is farther from 0 on a number line?', ['-π', '3.1']),
          sa('Between which two consecutive integers is -√30?', 'Between:'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.8 distances
    S('6.NS.C.8', 'Find distances between points with the same first or second coordinate',
      main=[
          sa('Find the distance between (-3, 4) and (5, 4).', 'Distance:'),
          sa('Find the distance between (2, -6) and (2, 5).', 'Distance:'),
          mc('What is the distance between (-7, -2) and (-1, -2)?', ['6', '8', '-6', '3']),
          sa('What is the distance between points A and B?', 'Distance:', fig=coord(pts=[(-4, -3, 'A', 'e'), (-4, 5, 'B', 'e')])),
          sa('Find the distance between (-2.5, 1) and (3.5, 1).', 'Distance:'),
      ],
      back=[
          B('Absolute value', '6.NS.C.7.c', [
              sa('Find the value.\n|-7|', 'Value:'),
              tf('|-3| + |5| = 8'),
              mc('|-4| + |6| = ?', ['10', '2', '-10', '-2']),
              sa('Find the value.\n|-9| + |2|', 'Value:'),
              tf('The distance from -5 to 0 is |-5|.'),
          ]),
          B('Naming points on the coordinate plane', '6.NS.C.6.c', [
              sa('What are the coordinates of point A?', 'A =', fig=coord(pts=[(-3, 4, 'A')])),
              sa('What are the coordinates of point B?', 'B =', fig=coord(pts=[(5, -2, 'B')])),
              mc('Which point is at (-1, -4)?', LET, fig=coord(pts=[(-1, -4, 'A'), (-4, -1, 'B'), (1, 4, 'C'), (4, -1, 'D')])),
              tf('Point C is located at (3, 0).', fig=coord(pts=[(0, 3, 'C', 'e')])),
              sa('What are the coordinates of point D?', 'D =', fig=coord(pts=[(-5, -5, 'D')])),
          ]),
          B('Distance between whole numbers', '2.MD.B.6', [
              sa('What is the distance from 3 to 11 on a number line?', 'Distance:'),
              sa('How many units apart are points A and B?', 'Units:', fig=nl(0, 10, 1, pts=[(2, 'A'), (7, 'B')])),
              tf('The distance from 12 to 4 is 8 units.'),
              mc('What is the distance from 5 to 14?', ['9', '19', '8', '10']),
              sa('What is the distance from 0 to 13 on a number line?', 'Distance:'),
          ]),
      ],
      f1=B('Distance between rational numbers', '7.NS.A.1.c', [
          sa('Find the distance between -2.5 and 4.5 on a number line.', 'Distance:'),
          sa('Find the value.\n|-8.4 - 3.6|', 'Value:'),
          mc('What is the distance between -3{1/2} and 2{1/4} on a number line?', ['5{3/4}', '1{1/4}', '-5{3/4}', '6{1/4}']),
          tf('The distance between -7 and -2 is |-7 - (-2)|, which is 5.'),
          sa('Find the distance between -4 and 2.5 on a number line.', 'Distance:'),
      ]),
      f2=B('Distance between points using the Pythagorean Theorem', '8.G.B.8', [
          sa('Find the distance between (1, 2) and (4, 6).', 'Distance:'),
          sa('Find the distance between points A and B.', 'Distance:', fig=coord(x=(-3, 5), y=(-2, 8), pts=[(-2, -1, 'A'), (4, 7, 'B')])),
          mc('What is the distance between (0, 0) and (5, 12)?', ['13', '17', '7', '√119']),
          sa('Find the distance between (-3, 5) and (1, 2).', 'Distance:'),
          tf('The distance between (2, 1) and (5, 5) is 5.'),
      ])),

    # ------------------------------------------------------------------ 6.NS.C.8 real-world
    S('6.NS.C.8', 'Solve real-world problems by graphing points in all four quadrants',
      main=[
          sa('On the map, each unit is 1 block.\nHow many blocks is it from the library L to the park P?', 'Blocks:', fig=coord(pts=[(-4, -3, 'L', 'e'), (-4, 5, 'P', 'e')])),
          sa('A park is a rectangle with corners at (-2, 3), (4, 3), (4, -1), and (-2, -1). Each unit is 1 meter.\nGraph the park. What is its perimeter?', 'Perimeter:', fig=coord()),
          sa('The school is at (-3, 2) and the pool is at (-3, -4). Each unit is 1 block.\nGraph both places. How many blocks apart are they?', 'Blocks:', fig=coord()),
          mc('A garden is a rectangle with corners at (-5, 1), (1, 1), (1, -3), and (-5, -3). Each unit is 1 meter.\nWhat is the area of the garden?', ['24 square meters', '20 square meters', '12 square meters', '10 square meters'], fig=coord()),
          sa('A hiker starts at (-5, 0), walks to (3, 0), and then walks to (3, 6). Each unit is 1 km.\nGraph the path. How far does the hiker walk?', 'Distance:', fig=coord()),
      ],
      back=[
          B('Absolute value as distance', '6.NS.C.7.c', [
              sa('Find the value.\n|-4| + |5|', 'Value:'),
              tf('The distance from -3 to 0 is 3.'),
              mc('How far is -6 from 0?', ['6', '-6', '0', '12']),
              sa('Find the value.\n|-2| + |4|', 'Value:'),
              tf('|-5| = -5'),
          ]),
          B('Plotting points in all four quadrants', '6.NS.C.6.c', [
              plot('Plot and label point A(-2, 3).', coord()),
              plot('Plot and label point B(4, -1).', coord()),
              mc('Which point is at (-3, -4)?', LET, fig=coord(pts=[(-3, -4, 'A'), (-4, -3, 'B'), (3, 4, 'C'), (3, -4, 'D')])),
              plot('Plot and label point C(0, -5).', coord()),
              tf('Point D is located at (-5, 2).', fig=coord(pts=[(-5, 2, 'D')])),
          ]),
          B('Perimeter of rectangles', '3.MD.D.8', [
              sa('What is the perimeter of the rectangle?', 'Perimeter:', fig=rect(6, 4, '6 units', '4 units')),
              sa('A rectangle is 9 cm long and 3 cm wide.\nWhat is its perimeter?', 'Perimeter:'),
              tf('A square with 5-meter sides has a perimeter of 25 meters.'),
              mc('A rectangle is 8 inches long and 2 inches wide.\nWhat is its perimeter?', ['20 inches', '16 inches', '10 inches', '18 inches']),
              sa('A rectangle has a perimeter of 18 feet and a length of 5 feet.\nWhat is its width?', 'Width:'),
          ]),
          B('Area of rectangles', '3.MD.C.7.b', [
              sa('A rectangle is 6 m long and 4 m wide.\nWhat is its area?', 'Area:'),
              tf('A rectangle that is 7 units by 3 units has an area of 21 square units.'),
              mc('A rectangle is 5 ft by 8 ft.\nWhat is its area?', ['40 square feet', '26 square feet', '13 square feet', '80 square feet']),
              sa('What is the area of the rectangle?', 'Area:', fig=rect(9, 2, '9 cm', '2 cm')),
              sa('A square has 6-inch sides.\nWhat is its area?', 'Area:'),
          ]),
      ],
      f1=B('Use a map scale on a coordinate grid', '7.G.A.1', [
          sa('On a map grid, each unit is {1/2} mile. The school is at (-3, 2) and the park is at (5, 2).\nWhat is the actual distance between them?', 'Distance:'),
          sa('On a trail map, each unit is 250 meters. The trail goes straight from (0, -4) to (0, 6).\nHow long is the actual trail?', 'Length:'),
          mc('On a map, each unit is 1.5 km. A park has corners at (-2, 1), (4, 1), (4, -3), and (-2, -3).\nWhat is the actual perimeter of the park?', ['30 km', '20 km', '13.3 km', '36 km']),
          sa('On a plan, each unit is 20 feet. A garden has corners at (-1, -1), (3, -1), (3, 2), and (-1, 2).\nWhat are the actual length and width?', 'Length and width:'),
          tf('On a map where each unit is 5 miles, the points (-3, 0) and (3, 0) are 30 miles apart.'),
      ]),
      f2=B('Straight-line distances on a map', '8.G.B.8', [
          sa('On a map, the library is at (-2, 1) and the pool is at (4, 9). Each unit is 1 block.\nWhat is the straight-line distance between them?', 'Distance:'),
          sa('A drone flies from (0, 0) to (9, 12). Each unit is 1 meter.\nHow far does it fly in a straight line?', 'Distance:'),
          mc('Home is at (-3, -1) and school is at (1, 2). Each unit is 1 km.\nWhat is the straight-line distance?', ['5 km', '7 km', '25 km', '√7 km']),
          sa('Find the straight-line distance from (-4, 6) to (2, -2).', 'Distance:'),
          tf('The straight-line distance from (1, 1) to (7, 9) is 10.'),
      ])),
]
