from qb import S, B, sa, mc, tf, plot, draw_write, shape, poly
from common import area_grid, DRAW


def box(w, h):
    return shape([poly([(0, 0), (w, 0), (w, h), (0, h)])])


SETS = [
    # ------------------------------------------------------------------ 3.G.A.1 (shared attributes)
    S('3.G.A.1', 'Understand that shapes in different categories can share attributes, and that quadrilaterals form a category',
      main=[
          mc('What do a rhombus, a rectangle, and a square always have in common?',
             ['They all have 4 sides.', 'They all have 4 square corners.', 'They all have 4 sides of equal length.', 'They all have 3 sides.']),
          tf('A trapezoid and a square are both quadrilaterals.', key=True),
          sa('A closed shape has 4 straight sides and 4 angles.\nWhat category does it belong to?', 'Category:', key='Quadrilaterals',
             note='"Quadrilateral" is also correct.'),
          sa('Name an attribute that every rectangle and every square share, and an attribute that a square must have but a rectangle might not.',
             ['Shared:', 'Only the square must have:'], key='4 square corners; 4 sides of equal length',
             note='Any correct shared attribute (4 sides, 4 square corners, opposite sides of equal length) is correct for the first part. '
                  'The second part must be 4 sides of equal length. Both parts are required.'),
          tf('A triangle is a quadrilateral because it has straight sides.', key=False),
      ],
      back=[
          B('Name triangles, quadrilaterals, pentagons, and hexagons', '2.G.A.1', [
              sa('How many sides does a hexagon have?', 'Sides:', key='6'),
              tf('A quadrilateral has 4 sides.', key=True),
              mc('Which shape has 5 angles?', ['Pentagon', 'Hexagon', 'Triangle', 'Quadrilateral']),
              sa('What is a closed shape with 3 straight sides called?', 'Name:', key='Triangle'),
              tf('A pentagon has 6 sides.', key=False),
          ]),
          B('Tell defining attributes from other attributes', '1.G.A.1', [
              tf('A square can be any color and still be a square.', key=True),
              mc('Which is a defining attribute of a triangle?', ['It has 3 sides.', 'It is red.', 'It is big.', 'It points up.']),
              sa('Is size a defining attribute of a rectangle?', 'Answer:', key='No'),
              sa('A closed shape has 4 straight sides.\nName one shape it could be.', 'Shape:', key='A square',
                 note='Any quadrilateral (rectangle, rhombus, trapezoid, and so on) is correct.'),
              tf('A shape must be blue to be a hexagon.', key=False),
          ]),
      ],
      f1=B('Classify quadrilaterals by parallel sides and right angles', '4.G.A.2', [
          sa('A quadrilateral has exactly one pair of parallel sides.\nWhat is it called?', 'Name:', key='Trapezoid'),
          tf('A rectangle has two pairs of parallel sides.', key=True),
          mc('Which shape must have four right angles?', ['Square', 'Rhombus', 'Trapezoid', 'Parallelogram']),
          sa('Name a quadrilateral that has two pairs of parallel sides and no right angles.', 'Shape:', key='A rhombus that is not a square',
             note='Any parallelogram that is not a rectangle is correct. A square or a rectangle is not correct.'),
          tf('Every quadrilateral has at least one pair of parallel sides.', key=False),
      ]),
      f2=B('Attributes of a category belong to all of its subcategories', '5.G.B.3', [
          tf('All rectangles have 4 right angles, and every square is a rectangle, so every square has 4 right angles.', key=True),
          mc('A shape is a square.\nWhich statement must be true?',
             ['It is a rectangle.', 'It has exactly one pair of parallel sides.', 'It is a triangle.', 'It has 5 sides.']),
          sa('Every parallelogram has opposite sides of equal length. A rhombus is a parallelogram.\nWhat must be true about the opposite sides of a rhombus?',
             'Answer:', key='They are equal in length.'),
          sa('Does every rectangle have 4 sides? Explain using categories.', ['Answer:', 'Explanation:'], key='Yes',
             note='A rectangle is a quadrilateral, and every quadrilateral has 4 sides. Both parts are required.'),
          tf('Every rhombus is a square.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.G.A.1 (subcategories and drawing)
    S('3.G.A.1', 'Recognize rhombuses, rectangles, and squares as quadrilaterals, and draw quadrilaterals that are not in these subcategories',
      main=[
          draw_write('Draw a quadrilateral that is not a rhombus, not a rectangle, and not a square.\nWhat makes your shape a quadrilateral?', DRAW, 'Reason:',
                     draw='Any closed shape with 4 straight sides that does not have 4 equal sides and does not have 4 square corners '
                          '(for example a trapezoid with exactly one pair of parallel sides, or a kite)',
                     key='It is a closed shape with 4 straight sides and 4 angles.',
                     note='Grade both: a quadrilateral that is not a rhombus, rectangle, or square, and the reason. A rhombus, rectangle, or square is not correct.'),
          mc('Which shape is a quadrilateral but is NOT a rhombus, a rectangle, or a square?',
             ['A trapezoid with exactly one pair of parallel sides', 'A square', 'A rhombus', 'A rectangle whose length and width are different']),
          tf('A square is a rectangle, and it is also a rhombus.', key=True),
          mc('A shape has 4 sides of equal length and no square corners.\nWhat is it?',
             ['A rhombus that is not a square', 'A square', 'A rectangle whose length and width are different', 'A triangle']),
          tf('Every quadrilateral is a rectangle.', key=False),
      ],
      back=[
          B('Draw shapes with a given number of sides or angles', '2.G.A.1', [
              plot('Draw a shape with 4 sides.', DRAW, key='Any closed shape with 4 straight sides'),
              tf('A closed shape with 4 angles has 4 sides.', key=True),
              mc('Which shape has 4 sides?', ['Quadrilateral', 'Pentagon', 'Triangle', 'Hexagon']),
              plot('Draw a shape with 3 angles.', DRAW, key='Any closed shape with 3 straight sides and 3 angles'),
              tf('A closed shape with 5 sides has 4 angles.', key=False),
          ]),
          B('Square corners and equal sides as defining attributes', '1.G.A.1', [
              tf('A square has 4 sides of equal length.', key=True),
              sa('How many square corners does a rectangle have?', 'Square corners:', key='4'),
              mc('Which shape always has 4 square corners?', ['Rectangle', 'Triangle', 'Circle', 'Hexagon']),
              sa('Is a rectangle that is turned on its corner still a rectangle?', 'Answer:', key='Yes'),
              tf('A rectangle must have 4 sides of equal length.', key=False),
          ]),
      ],
      f1=B('Draw and identify parallel and perpendicular sides in quadrilaterals', '4.G.A.1', [
          draw_write('Draw a quadrilateral with exactly one pair of parallel sides.\nWhat is it called?', DRAW, 'Name:',
                     draw='A quadrilateral with exactly one pair of parallel sides', key='Trapezoid',
                     note='Grade both: the quadrilateral with exactly one pair of parallel sides, and its name.'),
          tf('A rectangle has 4 right angles, so the sides that meet at each corner are perpendicular.', key=True),
          mc('Which quadrilateral always has perpendicular sides?',
             ['A rectangle', 'A rhombus that is not a square', 'A trapezoid with no right angles', 'A parallelogram with no right angles']),
          sa('How many pairs of parallel sides does a square have?', 'Pairs:', key='2'),
          tf('A rhombus that is not a square has perpendicular sides.', key=False),
      ]),
      f2=B('Classify quadrilaterals in a hierarchy', '5.G.B.4', [
          mc('Which list goes from the most general category to the most specific?',
             ['Quadrilateral, parallelogram, rectangle, square', 'Square, rectangle, parallelogram, quadrilateral',
              'Rectangle, quadrilateral, square, parallelogram', 'Parallelogram, square, quadrilateral, rectangle']),
          tf('Every square is a rhombus.', key=True),
          sa('Which of these categories does every square belong to?\nquadrilateral, parallelogram, rectangle, rhombus', 'Categories:',
             key='All four: quadrilateral, parallelogram, rectangle, and rhombus', note='All four are required.'),
          tf('Every rectangle is a square.', key=False),
          mc('A parallelogram has 4 right angles and 4 sides of equal length.\nWhat is its most specific name?', ['Square', 'Rectangle', 'Rhombus', 'Quadrilateral']),
      ])),

    # ------------------------------------------------------------------ 3.G.A.2 (partition)
    S('3.G.A.2', 'Split shapes into parts with equal areas',
      main=[
          plot('Draw lines to split the rectangle into 4 parts with equal areas.', box(8, 4),
               key='Lines that split the rectangle into 4 parts of equal area (for example 3 lines from top to bottom 2 units apart, '
                   'or one line across and one line down through the middle)'),
          plot('Draw lines to split the square into 3 parts with equal areas.', box(6, 6),
               key='Two lines that split the square into 3 parts of equal area (for example 2 lines from top to bottom, 2 units apart)'),
          mc('Which line always splits a rectangle into 2 parts with equal areas?',
             ['A line through the middle from one long side to the opposite long side, parallel to the short sides', 'A line close to one end',
              'A line from a corner to the middle of the opposite side', 'Any line that crosses the rectangle']),
          tf('One diagonal splits a square into 2 triangles with equal areas.', key=True),
          tf('If a rectangle is split into 4 parts, the parts always have equal areas.', key=False),
      ],
      back=[
          B('Split circles and rectangles into 2, 3, or 4 equal shares', '2.G.A.3', [
              plot('Draw a line to split the rectangle into 2 equal shares.', box(6, 3), key='One line that splits the rectangle into 2 equal shares (halves)'),
              tf('A rectangle can be split into 3 equal shares called thirds.', key=True),
              mc('How many equal shares are there when a shape is split into halves?', ['2', '3', '4', '1']),
              plot('Draw lines to split the square into 4 equal shares.', box(4, 4), key='Lines that split the square into 4 equal shares (fourths)'),
              tf('Two shares of different sizes are halves.', key=False),
          ]),
          B('Draw rows and columns of same-size squares in a rectangle', '2.G.A.2', [
              plot('Draw lines to split the square into 3 rows of 3 same-size squares.', box(3, 3),
                   key='Two lines across and two lines from top to bottom, making 3 rows of 3 same-size squares'),
              tf('Splitting a square into 2 rows of 2 same-size squares makes 4 squares.', key=True),
              mc('A rectangle is split into 1 row of 4 same-size squares.\nHow many squares are there?', ['4', '1', '5', '8']),
              sa('A rectangle is split into 2 rows of 3 same-size squares.\nHow many squares are there?', 'Squares:', key='6'),
              tf('A rectangle split into 3 rows of 2 same-size squares has 5 squares.', key=False),
          ]),
      ],
      f1=B('Draw lines of symmetry that split a figure into matching parts', '4.G.A.3', nearest=True, qs=[
          plot('Draw all the lines of symmetry of the rectangle.', box(6, 3), key='Two lines: one vertical line and one horizontal line, each through the middle'),
          tf('A line of symmetry splits a figure into two matching parts.', key=True),
          mc('How many lines of symmetry does a square have?', ['4', '2', '1', '0']),
          sa('How many lines of symmetry does a triangle with three sides of equal length have?', 'Lines:', key='3'),
          tf('Every line that splits a rectangle into two parts with equal areas is a line of symmetry.', key=False),
      ]),
      f2=B('Tile a rectangle with unit-fraction squares or rectangles to find its area', '5.NF.B.4.b', [
          sa('A square with an area of 1 square unit is split into 4 equal small squares.\nWhat is the area of each small square?', 'Area:', key='1/4 square unit'),
          tf('A rectangle {1/2} unit by {1/3} unit has an area of {1/6} square unit.', key=True),
          mc('A unit square is split into 3 equal columns and 2 equal rows.\nWhat is the area of each small rectangle?',
             ['{1/6} square unit', '{1/5} square unit', '{1/3} square unit', '6 square units']),
          sa('A rectangle {3/4} unit by {1/2} unit is tiled with rectangles that are {1/4} unit by {1/2} unit.\nHow many tiles fit? What is the area of the rectangle?',
             ['Tiles:', 'Area:'], key='3; 3/8 square unit', note='Both parts are required.'),
          tf('A unit square split into 8 equal parts has parts with an area of {1/4} square unit each.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.G.A.2 (unit fraction of the area)
    S('3.G.A.2', 'Express the area of each equal part as a unit fraction of the whole',
      main=[
          sa('The rectangle is split into parts with equal areas.\nWhat fraction of the whole area is each part?', 'Fraction:', key='1/4', fig=area_grid(1, 4, h=110, maxcell=60)),
          mc('A circle is split into 8 parts with equal areas.\nWhat fraction of the area is one part?', ['{1/8}', '{8/1}', '{1/7}', '{7/8}']),
          tf('If a hexagon is split into 6 parts with equal areas, each part is {1/6} of the area of the hexagon.', key=True),
          draw_write('Split the square into 2 parts with equal areas.\nWhat fraction of the area of the square is each part?', box(4, 4), 'Fraction:',
                     draw='One line that splits the square into 2 parts with equal areas', key='1/2',
                     note='Grade both: a split into 2 equal-area parts, and 1/2.'),
          tf('A rectangle split into 3 parts with equal areas has parts that are each {1/4} of the area.', key=False),
      ],
      back=[
          B('Name one of 2, 3, or 4 equal shares', '2.G.A.3', [
              sa('A circle is split into 4 equal shares.\nWhat is one share called?', 'Name:', key='A fourth', note='"A quarter" is also correct.'),
              tf('One of 2 equal shares is called a half.', key=True),
              mc('A rectangle is split into 3 equal shares.\nWhat is one share called?', ['A third', 'A half', 'A fourth', 'A whole']),
              sa('A shape is split into 2 equal shares.\nWhat do the 2 shares make together?', 'Answer:', key='The whole', note='"Two halves" is also correct.'),
              tf('One of 4 equal shares is called a third.', key=False),
          ]),
          B('Halves and quarters', '1.G.A.3', [
              sa('A square is cut into 4 equal parts.\nWhat is one part called?', 'Name:', key='A quarter', note='"A fourth" is also correct.'),
              tf('Two halves make a whole.', key=True),
              mc('A pizza is cut into 2 equal parts.\nWhat is each part called?', ['A half', 'A quarter', 'A third', 'A whole']),
              sa('How many halves are in one whole?', 'Halves:', key='2'),
              tf('One of 4 equal parts is called a half.', key=False),
          ]),
      ],
      f1=B('Add fractions as joining parts of the same whole', '4.NF.B.3.a', [
          sa('A rectangle is split into 6 equal parts. 2 parts are red and 3 parts are blue.\nWhat fraction of the rectangle is red or blue?', 'Fraction:', key='5/6'),
          tf('{2/8} + {3/8} means joining 2 eighths and 3 eighths of the same whole.', key=True),
          mc('A square is split into 4 equal parts. 1 part is shaded, and then 2 more parts are shaded.\nWhich equation shows the shaded fraction?',
             ['{1/4} + {2/4} = {3/4}', '{1/4} + {2/4} = {3/8}', '{1/4} + {2/4} = {2/4}', '{1/2} + {2/4} = {3/4}']),
          sa('A pie is cut into 8 equal pieces. 3 pieces are eaten.\nWhat fraction of the pie is left?', 'Fraction:', key='5/8'),
          tf('{1/3} + {1/3} = {2/6}', key=False),
      ]),
      f2=B('Add fractions with unlike denominators in word problems about parts of a whole', '5.NF.A.2', [
          sa('{1/2} of a garden is corn and {1/3} of it is beans.\nWhat fraction of the garden is corn or beans?', 'Fraction:', key='5/6'),
          tf('{1/4} of a field is grass and {1/2} is dirt. Together they are {3/4} of the field.', key=True),
          mc('A flag is {1/3} red and {1/6} white.\nWhat fraction of the flag is red or white?', ['{1/2}', '{2/9}', '{2/6}', '{1/18}']),
          sa('A cake is {3/8} chocolate and {1/4} vanilla.\nWhat fraction of the cake is chocolate or vanilla?', 'Fraction:', key='5/8'),
          tf('{1/2} of a wall is blue and {1/3} is green. The rest of the wall is {1/5} of it.', key=False),
      ])),
]
