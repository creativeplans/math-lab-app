from qb import S, B, sa, mc, tf, nl, table, rect, tri, plot, coord, draw_write
from common import fdot, fline, fracs

LEAVES = fdot(0, 1, {0.25: 2, 0.5: 1, 0.75: 3, 1: 1}, 4, 'Leaf length (inches)')
CRAYONS = fdot(3, 4, {3.25: 1, 3.5: 3, 3.75: 2, 4: 1}, 4, 'Crayon length (inches)')
RAISINS = fdot(0, 0.625, {0.125: 1, 0.25: 3, 0.375: 2, 0.5: 2}, 8, 'Raisins in each bag (pounds)')

SETS = [
    # ------------------------------------------------------------------ 4.MD.A.1 (relative sizes)
    S('4.MD.A.1', 'Know the relative sizes of measurement units within one system',
      main=[
          mc('Which unit is best for measuring the length of a river?', ['Kilometers', 'Centimeters', 'Grams', 'Liters']),
          tf('1 kilogram is 1,000 times as heavy as 1 gram.', key=True),
          sa('How many ounces are in 1 pound?', 'Ounces:', key='16'),
          mc('Which is heaviest?', ['1 kilogram', '1 gram', '100 grams', '500 grams']),
          tf('1 liter is less than 1 milliliter.', key=False),
      ],
      back=[
          B('Grams, kilograms, and liters', '3.MD.A.2', [
              mc('Which object has a mass of about 1 kilogram?', ['A large book', 'A paper clip', 'A car', 'A grape']),
              tf('A spoonful of water is about 1 liter.', key=False),
              sa('Would you measure the mass of a pencil in grams or in kilograms?', 'Unit:', key='Grams'),
              tf('A bucket can hold about 10 liters of water.', key=True),
              sa('A bag of flour has a mass of 2 kg. A bag of sugar has a mass of 3 kg.\nWhat is their total mass?', 'Mass:', key='5 kg'),
          ]),
          B('Measure with two different units', '2.MD.A.2', [
              tf('A desk measured in inches gives a larger number than the same desk measured in feet.', key=True),
              mc('A table is 2 meters long.\nAbout how many centimeters long is it?', ['200', '2', '20', '2,000']),
              sa('A rope is 3 feet long.\nIs it longer or shorter than 3 inches?', 'Answer:', key='Longer'),
              tf('A book measured in centimeters gives a smaller number than the same book measured in meters.', key=False),
              sa('Which is longer: 1 foot or 1 inch?', 'Answer:', key='1 foot'),
          ]),
      ],
      f1=B('Convert measurement units within one system', '5.MD.A.1', [
          sa('Convert.\n3.5 kilometers = ___ meters', 'Meters:', key='3,500'),
          tf('2,500 grams = 2.5 kilograms', key=True),
          mc('How many ounces are in 2{1/2} pounds?', ['40', '32', '20', '36']),
          sa('Convert.\n90 minutes = ___ hours', 'Hours:', key='1 1/2', note='1.5 is also correct.'),
          tf('400 centimeters = 40 meters', key=False),
      ]),
      f2=B('Use ratio reasoning to convert measurement units', '6.RP.A.3.d', [
          sa('There are 12 inches in 1 foot.\nHow many feet are in 54 inches?', 'Feet:', key='4 1/2', note='4.5 is also correct.'),
          tf('If 1 mile is about 1.6 km, then 5 miles is about 8 km.', key=True),
          mc('There are 4 quarts in 1 gallon.\nHow many gallons are in 26 quarts?', ['6{1/2}', '104', '22', '30']),
          sa('A recipe uses 3 cups of milk for every 2 batches.\nHow many cups of milk are needed for 7 batches?', 'Cups:', key='10 1/2', note='10.5 is also correct.'),
          tf('If 1 inch = 2.54 cm, then 10 inches = 2.54 cm.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.1 (larger unit to smaller, table)
    S('4.MD.A.1', 'Express a larger unit in terms of a smaller unit and record the pairs in a table',
      main=[
          sa('Complete the table.', 'Missing values:', key='300; 400', fig=table([['Meters', '1', '2', '3', '4'], ['Centimeters', '100', '200', '?', '?']])),
          sa('How many ounces are in 5 pounds?', 'Ounces:', key='80'),
          mc('A movie is 2 hours long.\nHow many minutes is that?', ['120', '200', '60', '24']),
          tf('7 kilograms = 700 grams', key=False),
          sa('Complete the table.', 'Missing values:', key='120; 240', fig=table([['Hours', '1', '2', '3', '4'], ['Minutes', '60', '?', '180', '?']])),
      ],
      back=[
          B('Multiply one-digit numbers by multiples of 10', '3.NBT.A.3', [
              sa('Multiply.\n4 × 60', 'Product:', key='240'),
              tf('2 × 50 = 100', key=True),
              mc('8 × 60 = ?', ['480', '48', '4,800', '68']),
              sa('Multiply.\n3 × 70', 'Product:', key='210'),
              tf('6 × 60 = 3,600', key=False),
          ]),
          B('Patterns in a table', '3.OA.D.9', [
              sa('What comes next?\n16, 32, 48, ___', 'Next:', key='64'),
              tf('In 15, 30, 45, 60, each number is 15 more than the one before.', key=True),
              mc('What is the rule for 10, 20, 30, 40?', ['Add 10', 'Add 20', 'Multiply by 2', 'Add 1']),
              sa('What comes next?\n12, 24, 36, ___', 'Next:', key='48'),
              tf('The pattern 5, 10, 20, 40 adds 5 each time.', key=False),
          ]),
      ],
      f1=B('Convert from a smaller unit to a larger unit', '5.MD.A.1', [
          sa('Convert.\n48 ounces = ___ pounds', 'Pounds:', key='3'),
          tf('2,000 milliliters = 2 liters', key=True),
          mc('Convert.\n250 centimeters = ___ meters', ['2.5', '25', '0.25', '2,500']),
          sa('Convert.\n150 seconds = ___ minutes', 'Minutes:', key='2 1/2', note='2.5 is also correct.'),
          tf('36 inches = 4 feet', key=False),
      ]),
      f2=B('Use tables of equivalent ratios to convert units', '6.RP.A.3.d', [
          sa('Complete the table.', 'Missing value:', key='15', fig=table([['Yards', '1', '2', '5'], ['Feet', '3', '6', '?']])),
          tf('A table with the pairs (1, 1,000), (2, 2,000), and (3, 3,000) converts kilograms to grams.', key=True),
          mc('There are 16 ounces in 1 pound.\nHow many pounds are 40 ounces?', ['2{1/2}', '24', '640', '3']),
          sa('1 liter = 1,000 milliliters.\nHow many liters are 3,500 milliliters?', 'Liters:', key='3.5', note='3 1/2 is also correct.'),
          tf('Because 1 meter = 100 cm, 0.75 meter = 7.5 cm.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.2 (distance and time)
    S('4.MD.A.2', 'Solve word problems about distances and intervals of time',
      main=[
          sa('A movie started at 3:45 p.m. and ended at 5:20 p.m.\nHow long was the movie?', 'Length:', key='1 hour 35 minutes',
             note='95 minutes is also correct.'),
          sa('Ty biked 2 km 350 m on Monday and 1 km 900 m on Tuesday.\nHow far did he bike in all? Give the answer in meters.', 'Meters:', key='4,250'),
          mc('A race is 3 km long. Ana has run 1,850 m.\nHow many more meters must she run?', ['1,150 m', '1,250 m', '4,850 m', '2,150 m']),
          tf('Soccer practice starts at 4:30 p.m. and lasts 1 hour 15 minutes. It ends at 5:45 p.m.', key=True),
          sa('A bus trip takes 45 minutes each way.\nHow long does a round trip take? Write the answer in hours and minutes.', 'Time:', key='1 hour 30 minutes',
             note='90 minutes is also correct.'),
      ],
      back=[
          B('Time intervals in minutes', '3.MD.A.1', [
              sa('A class starts at 9:10 and ends at 9:55.\nHow many minutes long is it?', 'Minutes:', key='45'),
              tf('From 2:30 to 3:15 is 45 minutes.', key=True),
              mc('Jo started reading at 7:20 and read for 25 minutes.\nWhat time did she stop?', ['7:45', '7:35', '8:45', '7:25']),
              sa('A show begins at 4:05 and lasts 50 minutes.\nWhat time does it end?', 'Time:', key='4:55'),
              tf('From 10:40 to 11:00 is 40 minutes.', key=False),
          ]),
          B('Length word problems within 100', '2.MD.B.5', [
              sa('A ribbon is 64 cm long. Mia cuts off 28 cm.\nHow long is the ribbon now?', 'Length:', key='36 cm'),
              tf('A 45-inch board and a 37-inch board laid end to end are 82 inches long.', key=True),
              mc('A path is 90 m long. Sam has walked 55 m.\nHow far is left?', ['35 m', '45 m', '145 m', '25 m']),
              sa('A tree was 38 feet tall. It grew 6 feet.\nHow tall is it now?', 'Height:', key='44 feet'),
              tf('Cutting 17 cm from a 50-cm rope leaves 37 cm.', key=False),
          ]),
      ],
      f1=B('Solve multistep problems that involve converting units', '5.MD.A.1', [
          sa('A runner ran 1.5 km and then 800 m.\nHow many meters did she run in all?', 'Meters:', key='2,300'),
          tf('A trip of 2 hours 30 minutes takes 150 minutes.', key=True),
          mc('A 4-yard rope has 5 feet cut off.\nHow many feet are left?', ['7 feet', '1 foot', '17 feet', '9 feet']),
          sa('A train ride lasts 2{1/4} hours.\nHow many minutes is that?', 'Minutes:', key='135'),
          tf('3 km - 1,200 m = 2,800 m', key=False),
      ]),
      f2=B('Solve constant-speed problems', '6.RP.A.3.b', [
          sa('A car travels 150 miles in 3 hours at a constant speed.\nWhat is its speed in miles per hour?', 'Speed:', key='50'),
          tf('Walking 6 km in 2 hours is a speed of 3 km per hour.', key=True),
          mc('A cyclist rides 12 miles per hour.\nHow far does she ride in 2.5 hours?', ['30 miles', '24 miles', '14.5 miles', '36 miles']),
          sa('A train goes 240 km in 4 hours.\nAt this rate, how long does it take to go 420 km?', 'Time:', key='7 hours'),
          tf('At 60 miles per hour, a car goes 90 miles in 2 hours.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.2 (volume, mass, money)
    S('4.MD.A.2', 'Solve word problems about liquid volume, mass, and money',
      main=[
          sa('A jug holds 2 liters of juice. Ella pours 6 cups of 250 milliliters each.\nHow many milliliters are left in the jug?', 'Milliliters:', key='500'),
          sa('A box of apples has a mass of 3 kg 400 g. Another box has a mass of 2 kg 750 g.\nWhat is their total mass in grams?', 'Grams:', key='6,150'),
          mc('Jo buys 3 notebooks that cost $2.45 each.\nHow much does she spend?', ['$7.35', '$6.35', '$7.45', '$5.35']),
          tf('Lee pays for items that cost $3.60 and $4.15 with a $10 bill. His change is $3.25.', key=False),
          sa('A cat has a mass of 4 kg. A dog has 6 times as much mass.\nWhat is the dog\'s mass in grams?', 'Grams:', key='24,000'),
      ],
      back=[
          B('Mass and liquid volume word problems', '3.MD.A.2', [
              sa('A pot holds 8 liters. 3 liters are poured out.\nHow many liters are left?', 'Liters:', key='5'),
              tf('Four 5-kg bags have a total mass of 20 kg.', key=True),
              mc('45 liters of water are shared equally among 9 buckets.\nHow many liters go in each bucket?', ['5', '36', '54', '9']),
              sa('A melon has a mass of 900 g. A pear has a mass of 200 g.\nHow much more mass does the melon have?', 'Grams:', key='700'),
              tf('Two 35-liter tubs hold 60 liters in all.', key=False),
          ]),
          B('Dollars and cents', '2.MD.C.8', [
              sa('How much money is 2 quarters, 1 dime, and 3 pennies?', 'Cents:', key='63 cents'),
              tf('3 quarters are worth 75 cents.', key=True),
              mc('Ben has 2 dollar bills and 4 dimes.\nHow much money does he have?', ['$2.40', '$2.04', '$6.00', '$2.10']),
              sa('A toy costs 85 cents. Ann pays with 1 dollar.\nHow much change does she get?', 'Change:', key='15 cents'),
              tf('5 nickels and 2 dimes are worth 50 cents.', key=False),
          ]),
      ],
      f1=B('Solve money and measurement problems with decimal operations', '5.NBT.B.7', [
          sa('Pens cost $1.25 each.\nHow much do 8 pens cost?', 'Cost:', key='$10.00'),
          tf('A $20 bill pays for 3 shirts that cost $5.99 each. The change is $2.03.', key=True),
          mc('A 2.4-liter bottle is shared equally among 6 cups.\nHow many liters go in each cup?', ['0.4', '4', '0.04', '1.4']),
          sa('Grapes cost $2.80 per pound.\nHow much do 3.5 pounds cost?', 'Cost:', key='$9.80'),
          tf('A 1.5-kg bag and a 0.75-kg bag have a total mass of 1.125 kg.', key=False),
      ]),
      f2=B('Find and compare unit prices', '6.RP.A.3.b', [
          sa('A 12-pack of water costs $4.80.\nWhat is the price of 1 bottle?', 'Price:', key='$0.40'),
          tf('4 kg of rice for $6 costs $1.50 per kilogram.', key=True),
          mc('Which is the best buy?', ['3 liters for $4.50', '2 liters for $3.20', '1 liter for $1.70', '4 liters for $6.40']),
          sa('5 pounds of apples cost $8.75.\nHow much does 1 pound cost?', 'Cost:', key='$1.75'),
          tf('A pack of 6 juice boxes for $3.60 costs $0.70 per box.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.2 (fractions, decimals, number lines)
    S('4.MD.A.2', 'Solve measurement problems with simple fractions or decimals, using number line diagrams',
      main=[
          sa('A board is 6 feet long. Jo cuts off {3/4} foot.\nHow long is the board now?', 'Length:', key='5 1/4 feet'),
          sa('Ana ran 0.5 km before lunch and 0.25 km after lunch.\nHow far did she run in all?', 'Distance:', key='0.75 km',
             note='75/100 km is also correct.'),
          mc('The number line shows a 2-mile hike. Lu has hiked to point A.\nHow much farther must she hike to reach the end?',
             ['{3/4} mile', '1{1/4} miles', '{1/4} mile', '2 miles'], fig=nl(0, 2, 0.25, labels=fracs(0, 2, 4), pts=[(1.25, 'A')])),
          tf('A jug has 2 liters of water. Lee pours out {1/4} liter. 1{3/4} liters are left.', key=True),
          draw_write('A rope is 3 meters long. Use the number line to show {1/2} meter being cut off.\nHow much rope is left?',
                     nl(0, 3, 0.5, labels=fracs(0, 3, 2)), 'Rope left:',
                     draw='A jump from 3 back to 2 1/2 (or a bar from 0 to 2 1/2) shown on the number line', key='2 1/2 meters',
                     note='Grade both: the number line shows the 1/2-meter cut from 3, and the answer 2 1/2 meters.'),
      ],
      back=[
          B('Solve time problems with a number line', '3.MD.A.1', [
              sa('Ty starts at 3:00 and works for 40 minutes. Use the number line.\nWhat time does he finish?', 'Time:', key='3:40',
                 fig=nl(0, 60, 10, labels={0: '3:00', 30: '3:30', 60: '4:00'})),
              tf('On a number line from 1:00 to 2:00, 1:30 is halfway.', key=True),
              mc('A game started at 6:15 and lasted 35 minutes.\nWhat time did it end?', ['6:50', '6:40', '7:50', '6:35']),
              sa('How many minutes are there from 8:20 to 9:00?', 'Minutes:', key='40'),
              tf('From 4:45 to 5:05 is 30 minutes.', key=False),
          ]),
          B('Fractions on a number line', '3.NF.A.2', [
              sa('What fraction is at point A?', 'A =', key='5/8', fig=nl(0, 1, 0.125, labels={0: '0', 1: '1'}, pts=[(0.625, 'A')])),
              tf('{3/3} and 1 are at the same point on a number line.', key=True),
              mc('Which fraction is closest to 0?', ['{1/8}', '{1/2}', '{3/4}', '{7/8}']),
              sa('What fraction is at point B?', 'B =', key='2/4', note='1/2 is also correct.', fig=nl(0, 1, 0.25, labels={0: '0', 1: '1'}, pts=[(0.5, 'B')])),
              tf('{1/4} is to the right of {3/4} on a number line.', key=False),
          ]),
      ],
      f1=B('Solve measurement problems by adding and subtracting fractions with unlike denominators', '5.NF.A.2', [
          sa('A board is 5 feet long. {2/3} foot is cut off.\nHow long is the board now?', 'Length:', key='4 1/3 feet'),
          tf('A jug had 1{1/2} liters. {3/4} liter was used. {3/4} liter is left.', key=True),
          mc('Ann walked {1/2} km and then {3/5} km.\nHow far did she walk in all?', ['1{1/10} km', '{4/7} km', '{4/10} km', '1{1/5} km']),
          sa('A rope is 4{1/2} m long. A piece 1{2/3} m long is cut off.\nHow much rope is left?', 'Length:', key='2 5/6 m'),
          tf('{3/8} kg + {1/4} kg = {4/12} kg', key=False),
      ]),
      f2=B('Find distances between points with the same first or second coordinate', '6.NS.C.8', [
          sa('Find the distance between (2, 5) and (2, -3).', 'Distance:', key='8 units'),
          tf('The distance between (-4, 1) and (3, 1) is 7 units.', key=True),
          mc('On a map grid, a school is at (-2, 4) and a park is at (5, 4).\nHow many units apart are they?', ['7', '3', '6', '9']),
          sa('Find the distance between (-6, -2) and (-6, 3).', 'Distance:', key='5 units'),
          tf('The distance between (0, -5) and (0, 5) is 0 units.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.3 (formulas)
    S('4.MD.A.3', 'Apply the area and perimeter formulas for rectangles',
      main=[
          sa('Find the area of the rectangle.', 'Area:', key='36 square meters', fig=rect(9, 4, '9 m', '4 m')),
          sa('Find the perimeter of the rectangle.', 'Perimeter:', key='34 inches', fig=rect(12, 5, '12 in.', '5 in.')),
          mc('A rectangular rug is 8 feet by 6 feet.\nWhat is its area?', ['48 square feet', '28 square feet', '14 square feet', '96 square feet']),
          tf('A square with sides of 7 cm has a perimeter of 49 cm.', key=False),
          sa('A garden is 15 m long and 8 m wide.\nWhat are its area and its perimeter?', ['Area:', 'Perimeter:'], key='120 square meters; 46 meters'),
      ],
      back=[
          B('Area as length times width', '3.MD.C.7.b', [
              sa('A rectangle is 6 units by 7 units.\nWhat is its area?', 'Area:', key='42 square units'),
              tf('A 5-by-9 rectangle has an area of 45 square units.', key=True),
              mc('Which equation gives the area of a 4-by-8 rectangle?', ['4 × 8 = 32', '4 + 8 = 12', '2 × (4 + 8) = 24', '8 - 4 = 4']),
              sa('Find the area of the rectangle.', 'Area:', key='30 square cm', fig=rect(10, 3, '10 cm', '3 cm')),
              tf('A 3-by-9 rectangle has an area of 12 square units.', key=False),
          ]),
          B('Perimeter of polygons', '3.MD.D.8', [
              sa('A triangle has sides of 5 cm, 7 cm, and 9 cm.\nWhat is its perimeter?', 'Perimeter:', key='21 cm'),
              tf('A square with sides of 4 m has a perimeter of 16 m.', key=True),
              mc('What is the perimeter of a rectangle that is 6 ft by 2 ft?', ['16 feet', '12 feet', '8 feet', '14 feet']),
              sa('A pentagon has five sides that are each 3 inches long.\nWhat is its perimeter?', 'Perimeter:', key='15 inches'),
              tf('A rectangle that is 5 units by 3 units has a perimeter of 15 units.', key=False),
          ]),
      ],
      f1=B('Find the area of rectangles with fractional side lengths', '5.NF.B.4.b', [
          sa('Find the area of a rectangle that is {3/4} m by {2/3} m.', 'Area:', key='1/2 square meter', note='6/12 square meter is also correct.'),
          tf('A rectangle that is 2{1/2} ft by 4 ft has an area of 10 square feet.', key=True),
          mc('A square has sides that are {1/2} inch long.\nWhat is its area?', ['{1/4} square inch', '1 square inch', '2 square inches', '{1/2} square inch']),
          sa('Find the area of a rectangle that is 1{1/2} yd by {2/3} yd.', 'Area:', key='1 square yard'),
          tf('A {1/3}-by-{1/3} square has an area of {2/3} square unit.', key=False),
      ]),
      f2=B('Find the area of triangles and parallelograms', '6.G.A.1', [
          sa('A triangle has a base of 10 cm and a height of 6 cm.\nWhat is its area?', 'Area:', key='30 square cm'),
          tf('A parallelogram with a base of 8 m and a height of 5 m has an area of 40 square meters.', key=True),
          mc('A right triangle has legs that are 4 ft and 9 ft long.\nWhat is its area?', ['18 square feet', '36 square feet', '13 square feet', '26 square feet']),
          sa('Find the area of the triangle.', 'Area:', key='20 square inches', fig=tri(8, 5, 3, '8 in.', '5 in.')),
          tf('A triangle with a base of 6 units and a height of 4 units has an area of 24 square units.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.A.3 (unknown side)
    S('4.MD.A.3', 'Find an unknown side length from the area or the perimeter of a rectangle',
      main=[
          sa('A rectangle has an area of 72 square feet and a length of 9 feet.\nWhat is its width?', 'Width:', key='8 feet'),
          sa('A rectangle has a perimeter of 30 cm and a length of 10 cm.\nWhat is its width?', 'Width:', key='5 cm'),
          mc('A rectangular patio has an area of 96 square meters. One side is 12 m long.\nHow long is the other side?', ['8 m', '84 m', '108 m', '36 m']),
          tf('A square has a perimeter of 36 inches, so each side is 9 inches long.', key=True),
          sa('A rectangle has an area of 54 square units and a width of 6 units.\nWrite an equation with a letter for the length. Then solve it.',
             ['Equation:', 'Length:'], key='6 × l = 54; l = 9 units', note='Any equivalent equation (for example 54 ÷ 6 = l) is correct. Both parts are required.'),
      ],
      back=[
          B('Find an unknown side from the perimeter', '3.MD.D.8', [
              sa('A triangle has a perimeter of 20 cm. Two sides are 6 cm and 8 cm long.\nHow long is the third side?', 'Length:', key='6 cm'),
              tf('A square with a perimeter of 12 m has sides that are 3 m long.', key=True),
              mc('A rectangle has a perimeter of 14 ft and a length of 5 ft.\nWhat is its width?', ['2 ft', '9 ft', '4 ft', '7 ft']),
              sa('A rectangle has a perimeter of 18 in. and a width of 4 in.\nWhat is its length?', 'Length:', key='5 inches'),
              tf('A square with a perimeter of 20 units has sides that are 10 units long.', key=False),
          ]),
          B('Find the unknown factor', '3.OA.A.4', [
              sa('Find the unknown number.\n8 × ? = 64', 'Unknown:', key='8'),
              tf('If 9 × w = 45, then w = 5.', key=True),
              mc('? × 7 = 56', ['8', '7', '49', '63']),
              sa('Find the unknown number.\n6 × ? = 42', 'Unknown:', key='7'),
              tf('If 4 × n = 28, then n = 6.', key=False),
          ]),
      ],
      f1=B('Find a missing dimension when the volume is known', '5.MD.C.5.b', [
          sa('A box has a volume of 60 cubic inches. It is 5 in. long and 3 in. wide.\nHow tall is it?', 'Height:', key='4 inches'),
          tf('A prism with a volume of 48 cubic cm and a base area of 12 square cm is 4 cm tall.', key=True),
          mc('A tank holds 120 cubic feet. Its base is 6 ft by 5 ft.\nHow deep is the tank?', ['4 feet', '20 feet', '109 feet', '10 feet']),
          sa('A prism has a volume of 90 cubic meters and a height of 5 m.\nWhat is the area of its base?', 'Base area:', key='18 square meters'),
          tf('A box that is 4 units by 3 units at the base and has a volume of 36 cubic units is 4 units tall.', key=False),
      ]),
      f2=B('Solve equations of the form px = q for a missing measurement', '6.EE.B.7', [
          sa('A rectangle has an area of 7.5 square meters and a length of 3 m.\nWrite and solve an equation for its width w.', ['Equation:', 'w ='],
             key='3w = 7.5; w = 2.5 m', note='Any equivalent equation is correct. Both parts are required.'),
          tf('A triangle has an area of 24 square units and a base of 8 units. Solving 4h = 24 gives a height of 6 units.', key=True),
          mc('Solve for b.\n12b = 84', ['7', '72', '96', '1,008']),
          sa('Solve for x.\n{1/2}x = 9', 'x =', key='18'),
          tf('The solution of 4w = 30 is w = 26.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.B.4 (make a line plot)
    S('4.MD.B.4', 'Make a line plot of measurements in fractions of a unit (1/2, 1/4, 1/8)',
      main=[
          plot('Pencil lengths (inches): 5{1/4}, 5{1/2}, 5{1/4}, 6, 5{3/4}, 5{1/2}, 5{1/4}\nMake a line plot of the data.', fline(5, 6, 4),
               key='Line plot: 3 X\'s at 5 1/4, 2 X\'s at 5 1/2, 1 X at 5 3/4, 1 X at 6'),
          plot('Seedling heights (inches): {1/8}, {3/8}, {3/8}, {1/2}, {5/8}, {3/8}, {1/8}\nMake a line plot of the data.', fline(0, 1, 8),
               key='Line plot: 2 X\'s at 1/8, 3 X\'s at 3/8, 1 X at 1/2, 1 X at 5/8'),
          sa('Shell lengths (inches): {1/2}, {3/4}, {1/2}, 1, {3/4}, {1/2}\nIn a line plot of the data, how many X\'s go above {1/2}?', 'X\'s:', key='3'),
          mc('Which number line is best for a line plot of {1/8}, {3/8}, {5/8}, and {7/8} inch?',
             ['A number line from 0 to 1 marked in eighths', 'A number line from 0 to 1 marked in halves',
              'A number line from 0 to 8 marked in ones', 'A number line from 1 to 2 marked in fourths']),
          plot('Ribbon pieces (yards): 1{1/2}, 2, 1{1/4}, 1{1/2}, 1{3/4}, 1{1/2}\nMake a line plot of the data.', fline(1, 2, 4),
               key='Line plot: 1 X at 1 1/4, 3 X\'s at 1 1/2, 1 X at 1 3/4, 1 X at 2'),
      ],
      back=[
          B('Read a line plot with halves and fourths', '3.MD.B.4', [
              sa('The line plot shows leaf lengths.\nHow many leaves are {3/4} inch long?', 'Leaves:', key='3', fig=LEAVES),
              tf('Two leaves are {1/4} inch long.', key=True, fig=LEAVES),
              mc('Which leaf length is most common?', ['{3/4} inch', '{1/4} inch', '{1/2} inch', '1 inch'], fig=LEAVES),
              sa('How many leaves were measured?', 'Leaves:', key='7', fig=LEAVES),
              tf('No leaf is 1 inch long.', key=False, fig=LEAVES),
          ]),
          B('Line plots of whole-number lengths', '2.MD.D.9', [
              sa('Lengths (cm): 4, 6, 6, 7, 6\nIn a line plot of the data, how many X\'s go above 6?', 'X\'s:', key='3'),
              tf('A line plot shows each measurement as a mark above a number line.', key=True),
              mc('Which number line fits a line plot of 2, 3, 3, and 8?',
                 ['A number line from 0 to 10', 'A number line from 10 to 20', 'A number line from 0 to 3', 'A number line from 4 to 6']),
              plot('Lengths (inches): 3, 5, 5, 6\nMake a line plot of the data.', nl(0, 8, 1), key='Line plot: 1 X at 3, 2 X\'s at 5, 1 X at 6'),
              tf('A line plot of 1, 2, 2, 2 has 2 X\'s above 2.', key=False),
          ]),
      ],
      f1=B('Make line plots and use operations on the data', '5.MD.B.2', [
          sa('Water in 4 cups (liters): {1/4}, {1/2}, {1/2}, {3/4}\nIf the water were shared equally among the cups, how much would each cup hold?',
             'Liters:', key='1/2 liter'),
          tf('The total of {1/8}, {3/8}, and {1/2} inch is 1 inch.', key=True),
          mc('A line plot shows 3 X\'s at {1/4} pound and 2 X\'s at {1/2} pound.\nWhat is the total weight?',
             ['1{3/4} pounds', '{3/4} pound', '5 pounds', '1{1/4} pounds']),
          plot('Rain (inches): {1/8}, {1/4}, {1/4}, {3/8}, {1/2}\nMake a line plot of the data.', fline(0, 1, 8),
               key='Line plot: 1 X at 1/8, 2 X\'s at 1/4, 1 X at 3/8, 1 X at 1/2'),
          tf('The difference between the largest and smallest of {1/8}, {3/8}, and {7/8} is {5/8}.', key=False),
      ]),
      f2=B('Display numerical data in dot plots', '6.SP.B.4', [
          plot('Number of pets: 0, 1, 1, 2, 2, 2, 3, 5\nMake a dot plot of the data.', nl(0, 6, 1),
               key='Dot plot: 1 dot at 0, 2 dots at 1, 3 dots at 2, 1 dot at 3, 1 dot at 5'),
          tf('A histogram groups data values into intervals.', key=True),
          mc('Which display shows every individual data value?', ['A dot plot', 'A histogram', 'A box plot', 'A table of intervals']),
          sa('Data: 12, 15, 15, 18, 20\nIn a dot plot of the data, how many dots go above 15?', 'Dots:', key='2'),
          tf('A dot plot cannot show data with repeated values.', key=False),
      ])),

    # ------------------------------------------------------------------ 4.MD.B.4 (solve problems)
    S('4.MD.B.4', 'Solve addition and subtraction problems using fraction data in a line plot',
      main=[
          sa('The line plot shows the raisins in some bags.\nWhat is the difference between the heaviest and the lightest bag?', 'Difference:',
             key='3/8 pound', fig=RAISINS),
          sa('What is the total weight of the bags that weigh {1/4} pound each?', 'Total:', key='3/4 pound', fig=RAISINS),
          mc('How many bags weigh more than {1/4} pound?', ['4', '2', '3', '5'], fig=RAISINS),
          tf('The two {1/2}-pound bags weigh 1 pound in all.', key=True, fig=RAISINS),
          sa('What is the total weight of all the bags?', 'Total:', key='2 5/8 pounds', note='21/8 pounds is also correct.', fig=RAISINS),
      ],
      back=[
          B('Read a line plot of lengths in fourths of an inch', '3.MD.B.4', [
              sa('How many crayons are 3{1/2} inches long?', 'Crayons:', key='3', fig=CRAYONS),
              tf('One crayon is 4 inches long.', key=True, fig=CRAYONS),
              mc('Which length do exactly 2 crayons have?', ['3{3/4} inches', '3{1/4} inches', '3{1/2} inches', '4 inches'], fig=CRAYONS),
              sa('How many crayons were measured?', 'Crayons:', key='7', fig=CRAYONS),
              tf('The shortest crayon is 3 inches long.', key=False, fig=CRAYONS),
          ]),
          B('Equivalent halves, fourths, and eighths', '3.NF.A.3.b', [
              sa('Write {1/2} as eighths.', 'Fraction:', key='4/8'),
              tf('{1/4} = {2/8}', key=True),
              mc('Which fraction is equal to {3/4}?', ['{6/8}', '{3/8}', '{4/8}', '{5/8}']),
              sa('Find the missing number.\n{1/2} = {?/4}', 'Missing number:', key='2'),
              tf('{2/8} = {1/2}', key=False),
          ]),
      ],
      f1=B('Use operations on fractions to solve line plot problems', '5.MD.B.2', [
          sa('Juice in 3 glasses (cups): {1/2}, {3/4}, 1{1/4}\nIf the juice were shared equally, how much would each glass hold?', 'Cups:', key='5/6 cup'),
          tf('Water in beakers (liters): {1/8}, {1/4}, {3/8}. The total is {3/4} liter.', key=True),
          mc('Ribbons (yards): {1/2}, {1/2}, {3/4}, {1/4}\nWhat is the total length?', ['2 yards', '1{1/2} yards', '2{1/4} yards', '1{3/4} yards']),
          sa('Rock masses (kg): {1/4}, {1/2}, {1/2}, {3/4}\nIf the total mass were shared equally by the 4 rocks, what would each rock\'s mass be?',
             'Mass:', key='1/2 kg'),
          tf('The total of {1/2}, {1/4}, and {1/8} is {3/14}.', key=False),
      ]),
      f2=B('Find the mean of a data set', '6.SP.B.5.c', [
          sa('Find the mean.\n4, 6, 8, 10', 'Mean:', key='7'),
          tf('The mean of 2, 4, and 9 is 5.', key=True),
          mc('Find the mean.\n{1/2}, {1/2}, 1, 2', ['1', '{1/2}', '2', '4']),
          sa('Five plants grew 3, 5, 5, 6, and 6 cm.\nWhat is the mean growth?', 'Mean:', key='5 cm'),
          tf('The mean of 10, 10, and 40 is 10.', key=False),
      ])),
]
