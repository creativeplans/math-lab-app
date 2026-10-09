from qb import S, B, sa, mc, tf, plot, draw_write, work, rect, shape, poly
from common import area_grid, tiles, DRAW, arr, ruler, amodel

MUL_ALG = ('The standard multiplication algorithm with the partial products or regrouping shown. '
           'A correct product without the algorithm earns partial credit.')

T7 = tiles([(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2)],
           'A shape made of 7 unit squares: a row of 3, another row of 3 above it, and 1 square on top at the left.')
T9 = tiles([(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (0, 2), (1, 2), (0, 3)],
           'A shape made of 9 unit squares: a bottom row of 4, two rows of 2 above it at the left, and 1 square on top at the left.')
T8 = tiles([(0, 0), (1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (1, 2), (2, 2)],
           'A shape made of 8 unit squares: a bottom row of 4 with a 2-by-2 block of squares centered on top of it.')
T6 = tiles([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3)],
           'A shape made of 6 unit squares: a bottom row of 3 and a column of 3 squares rising from the middle square.')
T10 = tiles([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2)],
            'A shape made of 10 unit squares: a bottom row of 5, a row of 4 above it at the left, and 1 square on top at the left.')

L1 = shape([poly([(0, 0), (8, 0), (8, 3), (3, 3), (3, 7), (0, 7)], ['8 m', '3 m', '5 m', '4 m', '3 m', '7 m'])])
L2 = shape([poly([(0, 0), (10, 0), (10, 2), (6, 2), (6, 6), (0, 6)], ['10 ft', '2 ft', '4 ft', '4 ft', '6 ft', '6 ft'])])
L3 = shape([poly([(0, 0), (9, 0), (9, 5), (5, 5), (5, 2), (0, 2)], ['9 cm', '5 cm', '4 cm', '3 cm', '5 cm', '2 cm'])])
SPLIT48 = dict(k='grid', rows=4, cols=8, cshade=5, h=200, maxcell=28,
               desc='A rectangle of 4 rows of 8 unit squares. The first 5 columns are shaded and the last 3 columns are not.')

SETS = [
    # ------------------------------------------------------------------ 3.MD.C.5.a
    S('3.MD.C.5.a', 'Understand a unit square and that it is used to measure area',
      main=[
          tf('A square with sides 1 unit long is a unit square, and its area is 1 square unit.', key=True),
          mc('Which shape is a unit square?', ['A square with sides 1 cm long', 'A square with sides 2 cm long', 'A rectangle 1 cm by 2 cm',
                                              'A circle 1 cm across']),
          sa('What is the area of a square with sides 1 inch long?', 'Area:', key='1 square inch'),
          sa('Why can unit squares be used to measure area?', ['Explanation:', ''],
             key='Each unit square has an area of 1 square unit, so counting how many unit squares cover a shape gives its area.',
             note='Must say that a unit square has an area of 1 square unit and that area is found by counting how many cover the shape.'),
          tf('A square with sides 1 meter long has an area of 1 square centimeter.', key=False),
      ],
      back=[
          B('Count the same-size squares in a rectangle', '2.G.A.2', [
              sa('How many same-size squares are in the rectangle?', 'Squares:', key='12', fig=area_grid(3, 4)),
              tf('A rectangle split into 2 rows of 3 same-size squares has 6 squares.', key=True),
              mc('A rectangle has 4 rows of 2 same-size squares.\nHow many squares are there?', ['8', '6', '4', '2']),
              sa('How many same-size squares are in each column of the rectangle?', 'Squares in each column:', key='3', fig=area_grid(3, 5)),
              tf('A rectangle split into 3 rows of 3 same-size squares has 6 squares.', key=False),
          ]),
          B('Defining attributes of a square', '1.G.A.1', [
              tf('Every square has 4 sides of the same length.', key=True),
              mc('Which is a defining attribute of a square?', ['4 equal sides and 4 square corners', 'It is blue.', 'It is big.', 'It is turned on a corner.']),
              sa('How many sides does a square have?', 'Sides:', key='4'),
              sa('Is a very small square still a square?', 'Answer:', key='Yes'),
              tf('A shape with 3 sides can be a square.', key=False),
          ]),
      ],
      f1=B('Find the area of a rectangle with the area formula', '4.MD.A.3', [
          sa('Find the area of a rectangle that is 12 m by 7 m.', 'Area:', key='84 square meters'),
          tf('A 9-by-11 rectangle has an area of 99 square units.', key=True),
          mc('A rug is 15 feet by 6 feet.\nWhat is its area?', ['90 square feet', '42 square feet', '21 square feet', '96 square feet']),
          sa('A square has sides that are 13 cm long.\nWhat is its area?', 'Area:', key='169 square cm'),
          tf('A rectangle that is 20 in. by 5 in. has an area of 50 square inches.', key=False),
      ]),
      f2=B('Understand a unit cube and that it is used to measure volume', '5.MD.C.3.a', nearest=True, qs=[
          tf('A cube with edges 1 unit long is a unit cube, and its volume is 1 cubic unit.', key=True),
          mc('Which can be used to measure volume?', ['A unit cube', 'A unit square', 'A ruler', 'A clock']),
          sa('What is the volume of a cube with edges 1 cm long?', 'Volume:', key='1 cubic centimeter'),
          sa('How is a unit cube like a unit square?', ['Answer:', ''],
             key='A unit square measures area (1 square unit), and a unit cube measures volume (1 cubic unit).',
             note='Must say that each is the unit that measures its quantity: 1 square unit of area and 1 cubic unit of volume.'),
          tf('A unit cube has a volume of 6 cubic units because it has 6 faces.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.5.b
    S('3.MD.C.5.b', 'A figure covered by n unit squares without gaps or overlaps has an area of n square units',
      main=[
          sa('Each small square is 1 square unit.\nWhat is the area of the shape?', 'Area:', key='7 square units', fig=T7),
          tf('A shape covered by 15 unit squares with no gaps or overlaps has an area of 15 square units.', key=True),
          mc('A rectangle is covered by 12 unit squares with no gaps or overlaps.\nWhat is its area?',
             ['12 square units', '12 units', '24 square units', '6 square units']),
          sa('Ben covers a shape with unit squares, but he leaves gaps between them. He counts 10 squares.\nIs the area exactly 10 square units? Explain.',
             ['Answer:', 'Explanation:'], key='No',
             note='The squares must cover the shape with no gaps or overlaps. With gaps, the area is more than 10 square units. Both parts are required.'),
          tf('If unit squares overlap, counting them gives the exact area.', key=False),
      ],
      back=[
          B('Measure length with same-size units and no gaps or overlaps', '1.MD.A.2', [
              sa('A crayon is as long as 6 cubes laid end to end with no gaps.\nHow many cubes long is it?', 'Cubes:', key='6'),
              tf('Length units laid end to end must have no gaps or overlaps.', key=True),
              mc('Which shows the correct way to measure with paper clips?',
                 ['Clips end to end with no gaps', 'Clips with spaces between them', 'Clips that overlap', 'Clips in a pile']),
              sa('A desk is 9 hands long. A table is 4 hands longer.\nHow many hands long is the table?', 'Hands:', key='13'),
              tf('If the cubes overlap when you measure, the count is still correct.', key=False),
          ]),
          B('Count the same-size squares that fill a rectangle', '2.G.A.2', [
              sa('How many same-size squares fill the rectangle?', 'Squares:', key='10', fig=area_grid(2, 5)),
              tf('A rectangle split into 3 rows of 4 same-size squares has 12 squares.', key=True),
              mc('How many same-size squares fill the rectangle?', ['9', '6', '12', '3'], fig=area_grid(3, 3)),
              sa('A rectangle has 5 rows of 2 same-size squares.\nHow many squares fill it?', 'Squares:', key='10'),
              tf('A rectangle with 2 rows of 4 same-size squares has 6 squares.', key=False),
          ]),
      ],
      f1=B('Find an unknown side length of a rectangle from its area', '4.MD.A.3', [
          sa('A rectangle has an area of 48 square feet and a length of 8 feet.\nWhat is its width?', 'Width:', key='6 feet'),
          tf('A rectangle with an area of 72 square cm and a width of 6 cm has a length of 12 cm.', key=True),
          mc('A garden has an area of 90 square meters. One side is 9 meters long.\nHow long is the other side?', ['10 m', '81 m', '99 m', '18 m']),
          sa('A square has an area of 64 square inches.\nHow long is each side?', 'Side:', key='8 inches'),
          tf('A rectangle with an area of 56 square units and a length of 7 units has a width of 9 units.', key=False),
      ]),
      f2=B('A solid packed with n unit cubes has a volume of n cubic units', '5.MD.C.3.b', nearest=True, qs=[
          sa('A box is filled with 30 unit cubes with no gaps or overlaps.\nWhat is its volume?', 'Volume:', key='30 cubic units'),
          tf('A solid built from 18 unit cubes has a volume of 18 cubic units.', key=True),
          mc('A prism has 4 layers with 6 unit cubes in each layer.\nWhat is its volume?', ['24 cubic units', '10 cubic units', '24 square units', '46 cubic units']),
          sa('How many unit cubes fill a box with a volume of 36 cubic units?', 'Unit cubes:', key='36'),
          tf('If the cubes in a box have gaps between them, counting them gives the exact volume.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.6
    S('3.MD.C.6', 'Measure areas by counting unit squares in square centimeters, meters, inches, feet, and other units',
      main=[
          sa('Each square is 1 square centimeter.\nWhat is the area of the shape?', 'Area:', key='9 square centimeters', fig=T9),
          sa('Each square is 1 square foot.\nWhat is the area of the rug?', 'Area:', key='10 square feet', fig=area_grid(2, 5)),
          mc('Each square is 1 square inch.\nWhat is the area of the shape?', ['8 square inches', '8 inches', '12 square inches', '6 square inches'], fig=T8),
          tf('Each square is 1 square meter. The shape has an area of 6 square meters.', key=True, fig=T6),
          tf('Each square is 1 square unit. The shape has an area of 11 square units.', key=False, fig=T10),
      ],
      back=[
          B('Count objects to tell how many', 'K.CC.B.5', [
              sa('How many squares are in the grid?', 'Squares:', key='8', fig=area_grid(2, 4)),
              tf('Counting each square once, a row of 6 squares has 6 squares.', key=True),
              mc('How many squares are shaded?', ['5', '4', '6', '10'], fig=area_grid(2, 5, shade=5)),
              sa('How many squares are in the grid?', 'Squares:', key='15', fig=area_grid(3, 5)),
              tf('When you count objects, you may count one object twice.', key=False),
          ]),
          B('Estimate lengths in inches, feet, centimeters, and meters', '2.MD.A.3', [
              sa('Would you measure the length of a classroom in meters or in centimeters?', 'Unit:', key='Meters'),
              tf('A centimeter is shorter than a meter.', key=True),
              mc('Which unit is best for the length of a bug?', ['Centimeters', 'Meters', 'Feet', 'Yards']),
              sa('Would you measure a book in inches or in feet?', 'Unit:', key='Inches'),
              tf('A foot is shorter than an inch.', key=False),
          ]),
      ],
      f1=B('Find areas of rectangles in real-world problems with the area formula', '4.MD.A.3', [
          sa('A classroom floor is 9 m by 8 m.\nWhat is its area?', 'Area:', key='72 square meters'),
          tf('A 14-ft by 10-ft deck has an area of 140 square feet.', key=True),
          mc('A poster is 24 in. by 18 in.\nWhat is its area?', ['432 square inches', '84 square inches', '42 square inches', '422 square inches']),
          sa('A garden is 25 ft by 4 ft.\nWhat is its area?', 'Area:', key='100 square feet'),
          tf('A 16-cm by 5-cm card has an area of 42 square cm.', key=False),
      ]),
      f2=B('Measure volume by counting unit cubes in cubic cm, cubic in., and cubic ft', '5.MD.C.4', nearest=True, qs=[
          sa('A box holds 2 layers of 6 cubes. Each cube is 1 cubic centimeter.\nWhat is the volume of the box?', 'Volume:', key='12 cubic centimeters'),
          tf('A stack of 3 layers of 4 one-inch cubes has a volume of 12 cubic inches.', key=True),
          mc('A prism is made of 20 cubes that are each 1 cubic foot.\nWhat is its volume?', ['20 cubic feet', '20 square feet', '20 feet', '40 cubic feet']),
          sa('A figure is built from 15 unit cubes.\nWhat is its volume?', 'Volume:', key='15 cubic units'),
          tf('A box that holds 2 layers of 9 one-centimeter cubes has a volume of 11 cubic centimeters.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.7.a
    S('3.MD.C.7.a', 'Find the area of a rectangle by tiling, and show that it equals the product of the side lengths',
      main=[
          sa('The rectangle is tiled with unit squares.\nCount the squares. Then multiply the side lengths. Do you get the same area?',
             ['Count:', 'Multiply:', 'Same?'], key='15; 3 × 5 = 15; yes', fig=area_grid(3, 5), note='All three parts are required.'),
          mc('A rectangle is tiled with 4 rows of 6 unit squares.\nWhich equation gives its area?', ['4 × 6 = 24', '4 + 6 = 10', '4 + 4 + 6 + 6 = 20', '6 - 4 = 2']),
          tf('A rectangle 5 units long and 2 units wide can be tiled with 10 unit squares.', key=True),
          draw_write('Draw a rectangle 4 units long and 3 units wide on the grid, and show its unit squares.\nWrite a multiplication equation for its area.',
                     DRAW, 'Equation:', draw='A 4-by-3 rectangle on the grid with its 12 unit squares', key='4 × 3 = 12',
                     note='Grade both: the 4-by-3 rectangle, and the equation (3 × 4 = 12 is also correct).'),
          tf('Tiling a 6-by-3 rectangle takes 9 unit squares.', key=False),
      ],
      back=[
          B('Find the total of an array by adding equal addends', '2.OA.C.4', [
              sa('How many squares are in 3 rows of 5 squares? Write an addition equation.', 'Equation:', key='5 + 5 + 5 = 15',
                 note='3 + 3 + 3 + 3 + 3 = 15 is also correct.'),
              tf('An array of 4 rows of 4 has 16 objects.', key=True),
              mc('Which addition matches 2 rows of 5 squares?', ['5 + 5', '2 + 5', '2 + 2', '5 + 2 + 5']),
              sa('How many squares are in 5 rows of 3 squares?', 'Squares:', key='15'),
              tf('3 + 3 + 3 + 3 matches 3 rows of 3 squares.', key=False),
          ]),
          B('Split a rectangle into rows and columns of same-size squares', '2.G.A.2', [
              plot('Draw lines to split the rectangle into 2 rows of 4 same-size squares.', shape([poly([(0, 0), (4, 0), (4, 2), (0, 2)])]),
                   key='One line across the middle and three lines from top to bottom, making 2 rows of 4 same-size squares'),
              tf('A rectangle split into 3 rows and 2 columns has 6 same-size squares.', key=True),
              mc('A rectangle is split into 2 rows and 3 columns of same-size squares.\nHow many squares are there?', ['6', '5', '9', '4']),
              sa('A rectangle is split into 4 rows and 4 columns of same-size squares.\nHow many squares are there?', 'Squares:', key='16'),
              tf('A rectangle split into 5 rows and 1 column has 6 squares.', key=False),
          ]),
      ],
      f1=B('Write and apply the area formula A = l × w', '4.MD.A.3', [
          sa('Write a formula for the area A of a rectangle with length l and width w.', 'Formula:', key='A = l × w', note='A = w × l is also correct.'),
          tf('A rectangle with l = 13 and w = 6 has A = 78.', key=True),
          mc('Use A = l × w.\nWhat is the area when l = 25 cm and w = 4 cm?', ['100 square cm', '29 square cm', '58 square cm', '104 square cm']),
          sa('Find the area of a rectangle with l = 18 ft and w = 5 ft.', 'Area:', key='90 square feet'),
          tf('A rectangle with l = 11 and w = 9 has A = 40.', key=False),
      ]),
      f2=B('Find the volume of a prism by packing it with unit cubes and by multiplying', '5.MD.C.5.a', nearest=True, qs=[
          sa('A box is packed with unit cubes: 3 cubes long, 2 cubes wide, and 4 cubes tall.\nCount the cubes and then multiply. Do you get the same volume?',
             ['Count:', 'Multiply:', 'Same?'], key='24; 3 × 2 × 4 = 24; yes', note='All three parts are required.'),
          tf('A prism 5 units by 2 units by 3 units can be packed with 30 unit cubes.', key=True),
          mc('Which equation gives the volume of a prism 4 by 3 by 2?', ['4 × 3 × 2 = 24', '4 + 3 + 2 = 9', '4 × 3 = 12', '2 × 4 + 3 = 11']),
          sa('A prism has a base area of 6 square units and a height of 5 units.\nWhat is its volume?', 'Volume:', key='30 cubic units'),
          tf('A 2-by-2-by-2 cube can be packed with 6 unit cubes.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.7.b
    S('3.MD.C.7.b', 'Multiply side lengths to find the area of a rectangle in real-world problems',
      main=[
          sa('A rug is 6 feet long and 4 feet wide.\nWhat is its area?', 'Area:', key='24 square feet'),
          sa('Find the area of the rectangle.', 'Area:', key='35 square meters', fig=rect(7, 5, '7 m', '5 m')),
          mc('A garden is 8 yards long and 9 yards wide.\nWhat is its area?', ['72 square yards', '17 square yards', '34 square yards', '72 yards']),
          tf('A poster 3 feet by 2 feet has an area of 5 square feet.', key=False),
          tf('A tile 8 inches by 8 inches has an area of 16 square inches.', key=False),
      ],
      back=[
          B('Measure side lengths with a ruler', '2.MD.A.1', [
              sa('How long is the side?', 'Length:', key='3 inches', fig=ruler(5, (0, 3), 'side', div=1)),
              tf('To measure with a ruler, line up one end of the side with 0.', key=True),
              mc('How long is the edge?', ['4 inches', '5 inches', '3 inches', '6 inches'], fig=ruler(6, (0, 4), 'edge', div=1)),
              sa('A side reaches from 0 to 7 on a centimeter ruler.\nHow long is it?', 'Length:', key='7 cm'),
              tf('A side that reaches from 0 to 2 on an inch ruler is 3 inches long.', key=False),
          ]),
          B('Find the total of equal rows by repeated addition', '2.OA.C.4', [
              sa('A tray has 4 rows of 5 cups.\nUse repeated addition to find the number of cups.', 'Cups:', key='20', note='5 + 5 + 5 + 5 = 20.'),
              tf('3 rows of 5 tiles is 5 + 5 + 5 = 15 tiles.', key=True),
              mc('Which addition gives the number of squares in 2 rows of 4?', ['4 + 4', '2 + 4', '2 + 2 + 4', '4 + 2']),
              sa('How many tiles are in 3 rows of 3?', 'Tiles:', key='9'),
              tf('4 rows of 4 tiles is 4 + 4 = 16 tiles.', key=False),
          ]),
      ],
      f1=B('Use the area formula to solve real-world problems with larger numbers', '4.MD.A.3', [
          sa('A patio is 12 feet by 11 feet.\nWhat is its area?', 'Area:', key='132 square feet'),
          tf('A 15-m by 20-m field has an area of 300 square meters.', key=True),
          mc('A wall is 9 ft tall and 14 ft wide.\nWhat is its area?', ['126 square feet', '46 square feet', '23 square feet', '116 square feet']),
          sa('A pool is 25 m long and 10 m wide.\nWhat is its area?', 'Area:', key='250 square meters'),
          tf('A 13-cm by 7-cm card has an area of 81 square cm.', key=False),
      ]),
      f2=B('Find the area of a rectangle with fractional side lengths', '5.NF.B.4.b', [
          sa('Find the area of a rectangle that is {2/3} m by {3/4} m.', 'Area:', key='1/2 square meter', note='6/12 square meter is also correct.'),
          tf('A rectangle 2{1/2} ft by 2 ft has an area of 5 square feet.', key=True),
          mc('A square has sides that are {1/3} yard long.\nWhat is its area?', ['{1/9} square yard', '{2/3} square yard', '{1/6} square yard', '{4/3} square yards']),
          sa('A rug is 4 feet by 1{1/2} feet.\nWhat is its area?', 'Area:', key='6 square feet'),
          tf('A rectangle {1/2} inch by {1/4} inch has an area of {3/4} square inch.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.7.c
    S('3.MD.C.7.c', 'Use tiling to show that the area of a rectangle with sides a and b + c is a × b + a × c',
      main=[
          sa('The 4-by-8 rectangle is split into a 4-by-5 part (shaded) and a 4-by-3 part.\nWrite the area as a sum of two products. Then find the total area.',
             ['Sum of products:', 'Total area:'], key='4 × 5 + 4 × 3; 32 square units', fig=SPLIT48,
             note='4 × 3 + 4 × 5 is also correct. Both parts are required.'),
          mc('A 6-by-9 rectangle is split into a 6-by-4 part and a 6-by-5 part.\nWhich expression gives its area?',
             ['6 × 4 + 6 × 5', '6 × 4 × 5', '6 + 4 + 5', '4 × 5 + 6']),
          tf('The area of a 3-by-7 rectangle equals 3 × 5 + 3 × 2.', key=True),
          draw_write('Draw one line along the grid to split the 5-by-6 rectangle into two smaller rectangles.\nWrite the total area as a sum of the two areas.',
                     area_grid(5, 6), 'Sum:',
                     draw='One straight line along the grid lines that splits the rectangle into two rectangles (for example 5 by 4 and 5 by 2)',
                     key='5 × 4 + 5 × 2 = 30',
                     note='Grade both: any split into two rectangles, and a matching sum equal to 30 (for example 5 × 3 + 5 × 3 = 30 or 2 × 6 + 3 × 6 = 30).'),
          tf('A 2-by-10 rectangle split into a 2-by-6 part and a 2-by-4 part has an area of 2 × 6 × 4.', key=False),
      ],
      back=[
          B('Split an array into two parts and add', '2.OA.C.4', [
              sa('An array has 3 rows of 5 dots. A line splits it into 3 rows of 3 and 3 rows of 2.\nHow many dots are in each part? How many are there in all?',
                 ['Parts:', 'Total:'], key='9 and 6; 15', note='Both parts are required.'),
              tf('Splitting an array of 4 rows of 5 into 4 rows of 2 and 4 rows of 3 keeps 20 dots in all.', key=True),
              mc('An array of 2 rows of 5 is split into 2 rows of 2 and 2 rows of 3.\nHow many dots are in the 2-rows-of-3 part?', ['6', '4', '5', '10']),
              sa('The dashed line splits the array.\nHow many dots are there in all?', 'Dots:', key='12', fig=arr(4, 3, split=1)),
              tf('An array of 5 rows of 4 split into two parts has 10 dots in all.', key=False),
          ]),
          B('Add tens and ones within 100', '2.NBT.B.5', [
              sa('Add.\n20 + 15', 'Sum:', key='35'),
              tf('30 + 24 = 54', key=True),
              mc('40 + 32 = ?', ['72', '62', '82', '8']),
              sa('Add.\n18 + 12', 'Sum:', key='30'),
              tf('35 + 25 = 50', key=False),
          ]),
      ],
      f1=B('Use area models and the distributive property to multiply a two-digit number', '4.NBT.B.5', [
          sa('Use the area model to find 6 × 47.', 'Product:', key='282', fig=amodel('6', [(40, '40', '240'), (7, '7', '42')])),
          tf('8 × 53 = 8 × 50 + 8 × 3', key=True),
          mc('Which two parts of an area model show 4 × 26?', ['4 × 20 and 4 × 6', '4 × 2 and 4 × 6', '20 × 6 and 4', '4 × 20 and 6']),
          work('Use an area model or the distributive property to find 7 × 38. Show your work.', 'Product:', key='266',
               method='Any valid area model or chain of equations, for example 7 × 30 + 7 × 8 = 210 + 56, or 7 × 40 - 7 × 2 = 280 - 14. '
                      'The product without a model or equations earns partial credit.'),
          tf('5 × 64 = 5 × 60 + 4', key=False),
      ]),
      f2=B('Multiply two-digit numbers with partial products and the standard algorithm', '5.NBT.B.5', [
          sa('Use partial products to find 34 × 26.', 'Product:', key='884',
             note='30 × 20 + 30 × 6 + 4 × 20 + 4 × 6 = 600 + 180 + 80 + 24 = 884.'),
          tf('25 × 43 = 25 × 40 + 25 × 3', key=True),
          mc('Which partial products give 12 × 35?', ['10 × 35 + 2 × 35', '10 × 30 + 2 × 5', '12 × 30 + 5', '10 × 35 + 2']),
          work('Use the standard algorithm to multiply. Show your work.\n48 × 27', 'Product:', method=MUL_ALG, key='1,296'),
          tf('16 × 25 = 16 × 20 + 5', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.C.7.d
    S('3.MD.C.7.d', 'Find areas of rectilinear figures by splitting them into rectangles and adding the areas',
      main=[
          sa('Find the area of the figure. Split it into two rectangles and add their areas.', ['Areas of the parts:', 'Total area:'],
             key='24 and 12; 36 square meters', fig=L1,
             note='Any correct split is accepted (for example 3 × 7 = 21 and 5 × 3 = 15, total 36). Both parts are required.'),
          mc('A figure is split into a 6-by-4 rectangle and a 2-by-3 rectangle that do not overlap.\nWhat is the area of the figure?',
             ['30 square units', '24 square units', '15 square units', '144 square units']),
          tf('The area of a figure made of two rectangles that do not overlap is the sum of the areas of the rectangles.', key=True),
          sa('Find the area of the figure.', 'Area:', key='44 square feet', fig=L2,
             note='For example, 10 × 2 = 20 and 6 × 4 = 24, so 20 + 24 = 44.'),
          tf('The figure has an area of 50 square centimeters.', key=False, fig=L3),
      ],
      back=[
          B('Put shapes together to make a new shape', '1.G.A.2', [
              tf('Two rectangles can be put together to make a new shape.', key=True),
              mc('Two same-size squares are put side by side.\nWhat shape do they make?', ['A rectangle', 'A circle', 'A triangle', 'A hexagon']),
              sa('How many same-size squares make a rectangle that is 3 squares long and 1 square wide?', 'Squares:', key='3'),
              sa('A shape is made of one square and one rectangle put together.\nHow many smaller shapes make it?', 'Shapes:', key='2'),
              tf('Putting two rectangles together always makes a square.', key=False),
          ]),
          B('Add two-digit numbers within 100', '2.NBT.B.5', [
              sa('Add.\n24 + 18', 'Sum:', key='42'),
              tf('36 + 30 = 66', key=True),
              mc('45 + 27 = ?', ['72', '62', '18', '82']),
              sa('Add.\n32 + 49', 'Sum:', key='81'),
              tf('28 + 16 = 34', key=False),
          ]),
      ],
      f1=B('Find areas of figures made of rectangles in real-world problems', '4.MD.A.3', [
          sa('A room is made of a 12-ft by 10-ft rectangle and a 5-ft by 4-ft rectangle.\nWhat is its total area?', 'Area:', key='140 square feet'),
          tf('A garden made of a 15-m by 6-m bed and a 6-m by 6-m bed has an area of 126 square meters.', key=True),
          mc('A deck is a 20-ft by 8-ft rectangle with a 6-ft by 5-ft hole cut out for a tree.\nWhat is the area of the deck?',
             ['130 square feet', '160 square feet', '190 square feet', '30 square feet']),
          sa('A parking lot is made of a 30-m by 15-m part and a 10-m by 15-m part.\nWhat is its area?', 'Area:', key='600 square meters'),
          tf('A figure made of a 9-by-7 rectangle and a 3-by-4 rectangle has an area of 23 square units.', key=False),
      ]),
      f2=B('Find the volume of a solid made of two prisms by adding their volumes', '5.MD.C.5.c', nearest=True, qs=[
          sa('Two prisms that do not overlap have volumes of 20 and 18 cubic units.\nWhat is their total volume?', 'Volume:', key='38 cubic units'),
          tf('A 2-by-3-by-4 prism and a 2-by-3-by-1 prism together have a volume of 30 cubic units.', key=True),
          mc('A solid is a 4-by-2-by-3 prism joined to a 2-by-2-by-3 prism.\nWhat is its volume?',
             ['36 cubic units', '24 cubic units', '12 cubic units', '288 cubic units']),
          sa('A building is a 10-by-6-by-3 prism with a 4-by-6-by-3 prism attached.\nWhat is its total volume?', 'Volume:', key='252 cubic units'),
          tf('The volume of two joined prisms is the product of their volumes.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.D.8 (perimeter)
    S('3.MD.D.8', 'Find the perimeter of a polygon from its side lengths',
      main=[
          sa('Find the perimeter of the rectangle.', 'Perimeter:', key='22 cm', fig=rect(7, 4, '7 cm', '4 cm')),
          sa('A triangle has sides of 6 in., 8 in., and 10 in.\nWhat is its perimeter?', 'Perimeter:', key='24 inches'),
          mc('A square has sides that are 9 m long.\nWhat is its perimeter?', ['36 m', '81 m', '18 m', '27 m']),
          tf('A pentagon with five sides that are each 5 ft long has a perimeter of 25 ft.', key=True),
          sa('Find the perimeter of the figure.', 'Perimeter:', key='30 meters', fig=L1, note='8 + 3 + 5 + 4 + 3 + 7 = 30.'),
      ],
      back=[
          B('Add lengths in word problems within 100', '2.MD.B.5', [
              sa('A fence has parts that are 12 ft, 15 ft, and 20 ft long.\nWhat is the total length?', 'Length:', key='47 feet'),
              tf('Ribbons of 18 cm and 25 cm have a total length of 43 cm.', key=True),
              mc('Three sticks are 9 in., 14 in., and 21 in. long.\nWhat is their total length?', ['44 inches', '34 inches', '54 inches', '23 inches']),
              sa('A path has two parts, 35 m and 46 m long.\nHow long is the path?', 'Length:', key='81 meters'),
              tf('Boards of 30 in., 30 in., and 15 in. have a total length of 65 in.', key=False),
          ]),
          B('Add up to four two-digit numbers', '2.NBT.B.6', [
              sa('Add.\n12 + 15 + 12 + 15', 'Sum:', key='54'),
              tf('20 + 8 + 20 + 8 = 56', key=True),
              mc('9 + 16 + 9 + 16 = ?', ['50', '25', '40', '41']),
              sa('Add.\n30 + 25 + 18', 'Sum:', key='73'),
              tf('11 + 11 + 11 + 11 = 40', key=False),
          ]),
      ],
      f1=B('Apply the perimeter formula for rectangles', '4.MD.A.3', [
          sa('Use P = 2 × l + 2 × w to find the perimeter of a 15-m by 9-m rectangle.', 'Perimeter:', key='48 m'),
          tf('A 25-ft by 10-ft rectangle has a perimeter of 70 ft.', key=True),
          mc('A square field has sides that are 45 yd long.\nWhat is its perimeter?', ['180 yd', '90 yd', '2,025 yd', '135 yd']),
          sa('A rectangle is 36 cm long and 14 cm wide.\nWhat is its perimeter?', 'Perimeter:', key='100 cm'),
          tf('A 30-m by 20-m rectangle has a perimeter of 50 m.', key=False),
      ]),
      f2=B('Find perimeters of shapes with fractional side lengths', '5.NF.A.2', [
          sa('A rectangle is {3/4} ft by {1/2} ft.\nWhat is its perimeter?', 'Perimeter:', key='2 1/2 feet', note='5/2 feet is also correct.'),
          tf('A triangle with sides of {1/2} m, {1/3} m, and {1/6} m has a perimeter of 1 m.', key=True),
          mc('A square has sides that are {5/8} inch long.\nWhat is its perimeter?', ['2{1/2} inches', '{20/32} inch', '1{1/4} inches', '{5/32} inch']),
          sa('A rectangle is 2{1/4} yd by 1{1/2} yd.\nWhat is its perimeter?', 'Perimeter:', key='7 1/2 yards'),
          tf('A rectangle {2/3} m by {1/6} m has a perimeter of {5/6} m.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.D.8 (unknown side)
    S('3.MD.D.8', 'Find an unknown side length of a polygon from its perimeter',
      main=[
          sa('A rectangle has a perimeter of 20 cm. Its length is 6 cm.\nWhat is its width?', 'Width:', key='4 cm'),
          sa('A triangle has a perimeter of 30 in. Two of its sides are 9 in. and 12 in.\nHow long is the third side?', 'Length:', key='9 inches'),
          mc('A square has a perimeter of 28 m.\nHow long is each side?', ['7 m', '14 m', '24 m', '112 m']),
          tf('A rectangle with a perimeter of 18 ft and a length of 5 ft has a width of 8 ft.', key=False),
          sa('A quadrilateral has a perimeter of 40 cm. Three of its sides are 10 cm, 12 cm, and 8 cm.\nHow long is the fourth side?', 'Length:', key='10 cm'),
      ],
      back=[
          B('Find an unknown part in a word problem within 100', '2.OA.A.1', [
              sa('A fence will be 50 m long. 32 m are built.\nHow many meters are left to build?', 'Meters:', key='18'),
              tf('Kim needs 45 beads. She has 27 beads. She needs 18 more.', key=True),
              mc('A path is 80 ft long. Lu walked some of it and has 35 ft left.\nHow far did she walk?', ['45 ft', '115 ft', '55 ft', '35 ft']),
              sa('A lot has some cars and 14 trucks. There are 40 vehicles in all.\nHow many cars are there?', 'Cars:', key='26'),
              tf('A tape is 60 cm long. 25 cm are used, so 45 cm are left.', key=False),
          ]),
          B('Find the unknown number in an addition equation within 20', '1.OA.D.8', [
              sa('Find the unknown number.\n12 + ? = 20', 'Unknown:', key='8'),
              tf('In ? + 9 = 15, the unknown number is 6.', key=True),
              mc('18 = 10 + ?', ['8', '28', '10', '9']),
              sa('Find the unknown number.\n? + 7 = 19', 'Unknown:', key='12'),
              tf('In 11 + ? = 17, the unknown number is 5.', key=False),
          ]),
      ],
      f1=B('Find an unknown side length from the perimeter of a rectangle with the formula', '4.MD.A.3', [
          sa('A rectangle has a perimeter of 64 m and a length of 20 m.\nWhat is its width?', 'Width:', key='12 m'),
          tf('A square with a perimeter of 96 in. has sides that are 24 in. long.', key=True),
          mc('A rectangle has a perimeter of 50 ft and a width of 9 ft.\nWhat is its length?', ['16 ft', '32 ft', '41 ft', '25 ft']),
          sa('A rectangular garden has a perimeter of 100 yd. Its length is 30 yd.\nWrite an equation with a letter for the width. Then solve it.',
             ['Equation:', 'Width:'], key='2 × 30 + 2 × w = 100; w = 20 yd',
             note='Any equivalent equation with a letter (such as 100 = 2 × (30 + w)) is correct. Both parts are required.'),
          tf('A rectangle with a perimeter of 44 cm and a length of 15 cm has a width of 14 cm.', key=False),
      ]),
      f2=B('Find an unknown side length from a perimeter with fractions', '5.NF.A.2', [
          sa('A triangle has a perimeter of 3 ft. Two of its sides are {3/4} ft and 1{1/4} ft.\nHow long is the third side?', 'Length:', key='1 foot'),
          tf('A square with a perimeter of 5 m has sides that are 1{1/4} m long.', key=True),
          mc('A rectangle has a perimeter of 6 in. and a length of 1{3/4} in.\nWhat is its width?', ['1{1/4} in.', '4{1/4} in.', '2{1/2} in.', '3{1/4} in.']),
          sa('A rectangle has a perimeter of 4 yd and a width of {2/3} yd.\nWhat is its length?', 'Length:', key='1 1/3 yards', note='4/3 yards is also correct.'),
          tf('A square with a perimeter of 2 m has sides that are {1/4} m long.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.MD.D.8 (same perimeter or area)
    S('3.MD.D.8', 'Show rectangles with the same perimeter and different areas, or the same area and different perimeters',
      main=[
          draw_write('Draw two different rectangles on the grid that each have a perimeter of 12 units.\nWhat is the area of each rectangle?', DRAW, 'Areas:',
                     draw='Two different rectangles with a perimeter of 12 units each (from 1 by 5, 2 by 4, and 3 by 3)',
                     key='For example, 2 by 4: 8 square units; 1 by 5: 5 square units',
                     note='Grade both: two different rectangles with perimeter 12, and their correct areas (1 by 5 = 5, 2 by 4 = 8, 3 by 3 = 9 square units).'),
          mc('Which rectangle has the same area as a 4-by-6 rectangle but a different perimeter?', ['3 by 8', '5 by 5', '4 by 5', '2 by 10']),
          tf('A 2-by-6 rectangle and a 3-by-4 rectangle have the same area but different perimeters.', key=True),
          sa('A 1-by-8 rectangle and a 2-by-4 rectangle both have an area of 8 square units.\nFind the perimeter of each.', ['1 by 8:', '2 by 4:'],
             key='18 units; 12 units', note='Both parts are required.'),
          tf('Two rectangles with the same perimeter always have the same area.', key=False),
      ],
      back=[
          B('Recognize and draw rectangles', '2.G.A.1', [
              plot('Draw a rectangle on the grid.', DRAW, key='A closed 4-sided shape with 4 square corners'),
              tf('A rectangle has 4 sides and 4 corners.', key=True),
              mc('Which shape has 4 sides, with opposite sides the same length, and 4 square corners?', ['Rectangle', 'Triangle', 'Pentagon', 'Hexagon']),
              sa('How many sides does a rectangle have?', 'Sides:', key='4'),
              tf('A rectangle has 3 corners.', key=False),
          ]),
          B('Arrays with the same total', '2.OA.C.4', [
              sa('An array has 2 rows of 6 dots. Another array has 3 rows of 4 dots.\nHow many dots does each array have?', ['2 rows of 6:', '3 rows of 4:'],
                 key='12; 12', note='Both parts are required.'),
              tf('An array of 4 rows of 5 and an array of 5 rows of 4 have the same number of dots.', key=True),
              mc('Which array has 10 dots?', ['2 rows of 5', '3 rows of 3', '2 rows of 4', '4 rows of 3']),
              sa('How many dots are in 3 rows of 5?', 'Dots:', key='15'),
              tf('An array of 2 rows of 3 and an array of 3 rows of 3 have the same number of dots.', key=False),
          ]),
      ],
      f1=B('Compare the areas and perimeters of rectangles with the formulas', '4.MD.A.3', [
          sa('A rectangle is 10 m by 6 m.\nFind its area and its perimeter.', ['Area:', 'Perimeter:'], key='60 square meters; 32 m', note='Both parts are required.'),
          tf('A 9-by-4 rectangle and a 12-by-3 rectangle have the same area.', key=True),
          mc('Which rectangle has a perimeter of 30 ft and an area of 50 square feet?', ['10 ft by 5 ft', '15 ft by 2 ft', '6 ft by 9 ft', '25 ft by 2 ft']),
          sa('A 2-by-10 rectangle and a 6-by-6 square both have a perimeter of 24 cm.\nWhich has the greater area?', 'Answer:',
             key='The 6-by-6 square', note='6 by 6 has an area of 36 square cm and 2 by 10 has 20 square cm.'),
          tf('A 7-by-7 square and an 8-by-6 rectangle have the same perimeter and the same area.', key=False),
      ]),
      f2=B('Find different prisms with the same volume', '5.MD.C.5.b', nearest=True, qs=[
          sa('Give the dimensions of two different prisms that each have a volume of 24 cubic units.', ['Prism 1:', 'Prism 2:'],
             key='2 by 3 by 4; 1 by 4 by 6', note='Any two different sets of whole-number dimensions with a product of 24 are correct.'),
          tf('A 2-by-2-by-6 prism and a 3-by-4-by-2 prism have the same volume.', key=True),
          mc('Which prism has a volume of 36 cubic units?', ['3 by 3 by 4', '3 by 4 by 4', '2 by 2 by 8', '6 by 6 by 2']),
          sa('A box is 5 by 2 by 3. Another box is 3 by 2 by ? and has the same volume.\nWhat is the missing dimension?', 'Missing dimension:', key='5'),
          tf('A 1-by-1-by-10 prism and a 2-by-2-by-2 prism have the same volume.', key=False),
      ])),
]
