from qb import S, B, sa, mc, tf, nl, plot, draw_write
from common import bar, bars, fl, ruler


def two_lines(d1, d2, p1=None, p2=None):
    """Two number lines from 0 to 1 of the same length, one above the other."""
    return dict(k='vstack', figs=[fl(0, 1, d1, pts=p1 or []), fl(0, 1, d2, pts=p2 or [])])


SETS = [
    # ------------------------------------------------------------------ 3.NF.A.1 (unit fractions)
    S('3.NF.A.1', 'Understand a unit fraction as one part of a whole split into equal parts',
      main=[
          sa('The bar is split into 6 equal parts. One part is shaded.\nWhat fraction of the bar is shaded?', 'Fraction:', key='1/6', fig=bar(6, 1)),
          mc('A pizza is cut into 8 equal slices.\nWhat fraction of the pizza is one slice?', ['{1/8}', '{8/1}', '{1/7}', '{7/8}']),
          tf('{1/3} is one part when a whole is split into 3 equal parts.', key=True),
          draw_write('Shade {1/4} of the bar. Then explain why the part you shaded is {1/4} of the bar.', bar(4), 'Explanation:',
                     draw='Exactly 1 of the 4 equal parts shaded', key='The bar has 4 equal parts, and I shaded 1 of them.',
                     note='Grade both: 1 of the 4 parts shaded, and an explanation that names 4 equal parts with 1 part shaded.'),
          tf('If a whole is cut into 2 parts of different sizes, each part is {1/2} of the whole.', key=False),
      ],
      back=[
          B('Split shapes into halves, thirds, and fourths', '2.G.A.3', [
              sa('A rectangle is split into 3 equal shares.\nWhat is each share called?', 'Name:', key='A third'),
              tf('Four fourths make one whole.', key=True),
              mc('A circle is split into 2 equal shares.\nHow many halves make the whole circle?', ['2', '1', '4', '3']),
              sa('A square is split into 4 equal shares.\nWhat is each share called?', 'Name:', key='A fourth', note='"A quarter" is also correct.'),
              tf('A rectangle split into 3 equal shares is split into fourths.', key=False),
          ]),
          B('Halves and quarters of circles and rectangles', '1.G.A.3', [
              tf('Cutting a circle into 4 equal parts makes smaller parts than cutting it into 2 equal parts.', key=True),
              sa('A sandwich is cut into 2 equal parts.\nWhat is each part called?', 'Name:', key='A half'),
              mc('A pie is cut into 4 equal parts.\nWhat is each part called?', ['A quarter', 'A half', 'A third', 'A whole']),
              sa('How many quarters make a whole circle?', 'Quarters:', key='4'),
              tf('Halves of a rectangle are smaller than quarters of the same rectangle.', key=False),
          ]),
      ],
      f1=B('Write a fraction as a sum of unit fractions', '4.NF.B.3.b', [
          sa('Write {5/6} as a sum of unit fractions.', 'Sum:', key='1/6 + 1/6 + 1/6 + 1/6 + 1/6'),
          tf('{3/4} = {1/4} + {1/4} + {1/4}', key=True),
          mc('Which sum is equal to {4/5}?', ['{1/5} + {1/5} + {1/5} + {1/5}', '{1/4} + {1/4} + {1/4} + {1/4}', '{4/5} + {1/5}', '{2/5} + {1/5}']),
          sa('Write {7/8} as a sum of two fractions with a denominator of 8.', 'Sum:', key='3/8 + 4/8',
             note='Any two eighths that add to 7/8 are correct, for example 1/8 + 6/8.'),
          tf('{2/3} = {1/3} + {1/2}', key=False),
      ]),
      f2=B('Find a unit fraction of a unit fraction', '5.NF.B.4.a', [
          sa('What is {1/2} of {1/4}?', 'Answer:', key='1/8'),
          tf('{1/3} × {1/2} = {1/6}', key=True),
          mc('Multiply.\n{1/4} × {1/3}', ['{1/12}', '{2/7}', '{1/7}', '{4/3}']),
          sa('A ribbon is {1/2} yard long. Ana uses {1/5} of it.\nWhat fraction of a yard does she use?', 'Answer:', key='1/10 yard'),
          tf('{1/2} of {1/2} is 1.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.1 (a/b)
    S('3.NF.A.1', 'Understand a fraction a/b as a parts of size 1/b',
      main=[
          sa('What fraction of the bar is shaded?', 'Fraction:', key='5/8', fig=bar(8, 5)),
          mc('Which fraction is 3 parts of size {1/4}?', ['{3/4}', '{4/3}', '{1/3}', '{3/8}']),
          tf('{4/6} is 4 parts of size {1/6}.', key=True),
          draw_write('Shade {3/8} of the bar.\nHow many parts of size {1/8} did you shade?', bar(8), 'Parts:',
                     draw='Any 3 of the 8 equal parts shaded', key='3', note='Grade both: 3 of the 8 parts shaded, and the answer 3.'),
          tf('{5/6} is 6 parts of size {1/5}.', key=False),
      ],
      back=[
          B('Count halves, thirds, and fourths of a shape', '2.G.A.3', [
              sa('A rectangle is cut into 3 equal shares, and 2 shares are shaded.\nHow many thirds are shaded?', 'Thirds:', key='2'),
              tf('A whole is 3 thirds.', key=True),
              mc('A circle is cut into 4 equal shares.\nHow many fourths make the whole circle?', ['4', '3', '2', '1']),
              sa('A rectangle is cut into 2 equal shares, and both are shaded.\nHow many halves are shaded?', 'Halves:', key='2'),
              tf('A whole is 3 halves.', key=False),
          ]),
          B('Count halves and quarters of a shape', '1.G.A.3', [
              sa('A pizza is cut into 4 equal parts, and 3 parts are eaten.\nHow many quarters are eaten?', 'Quarters:', key='3'),
              tf('Two halves make one whole.', key=True),
              mc('A rectangle is cut into 4 equal parts.\nHow many parts make the whole?', ['4', '2', '1', '8']),
              sa('A pie is cut into 2 equal parts, and 1 part is eaten.\nWhat is the part that was eaten called?', 'Name:', key='A half'),
              tf('Four quarters make two wholes.', key=False),
          ]),
      ],
      f1=B('Understand a fraction a/b as a multiple of 1/b', '4.NF.B.4.a', [
          sa('Write {5/6} as a whole number times {1/6}.', 'Expression:', key='5 × 1/6'),
          tf('{7/4} = 7 × {1/4}', key=True),
          mc('Which equation shows {3/8} as a multiple of {1/8}?', ['{3/8} = 3 × {1/8}', '{3/8} = 8 × {1/3}', '{3/8} = 3 + {1/8}', '{3/8} = {1/8} ÷ 3']),
          sa('Fill in the blank.\n{9/10} = ___ × {1/10}', 'Blank:', key='9'),
          tf('{4/5} = 5 × {1/4}', key=False),
      ]),
      f2=B('Find a fraction of a quantity by first finding the unit fraction of it', '5.NF.B.4.a', [
          sa('Find {3/5} of 20 by first finding {1/5} of 20.', ['{1/5} of 20:', '{3/5} of 20:'], key='4; 12', note='Both parts are required.'),
          tf('{2/3} of 9 is 2 parts of size 3, which is 6.', key=True),
          mc('What is {5/8} of 16?', ['10', '2', '8', '80']),
          sa('Multiply.\n{4/7} × 14', 'Product:', key='8'),
          tf('{3/4} of 20 is 3 parts of size 4, which is 12.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.2.a
    S('3.NF.A.2.a', 'Represent a unit fraction on a number line',
      main=[
          sa('The space from 0 to 1 is split into 4 equal parts.\nWhat fraction is at point A?', 'A =', key='1/4', fig=fl(0, 1, 4, pts=[(0.25, 'A')])),
          plot('Mark and label {1/3} on the number line.', fl(0, 1, 3),
               key='A point at the first tick mark after 0 (one of the 3 equal parts from 0 to 1), labeled 1/3'),
          mc('Into how many equal parts must the space from 0 to 1 be split to show {1/6}?', ['6', '1', '5', '7']),
          tf('On a number line, {1/2} is halfway between 0 and 1.', key=True),
          tf('On a number line from 0 to 1 split into 8 equal parts, the first tick mark after 0 is {1/7}.', key=False),
      ],
      back=[
          B('Whole numbers as lengths from 0 on a number line', '2.MD.B.6', [
              sa('What number is at point A?', 'A =', key='3', fig=nl(0, 6, 1, labels={0: '0', 6: '6'}, pts=[(3, 'A')])),
              tf('On a number line, 5 is 5 equal lengths of 1 from 0.', key=True),
              mc('A jump from 0 to 4 on a number line is how many lengths of 1?', ['4', '5', '3', '1']),
              sa('What number is at point B?', 'B =', key='8', fig=nl(0, 10, 1, labels={0: '0', 10: '10'}, pts=[(8, 'B')])),
              tf('On a number line, the distance from 0 to 7 is 6 lengths of 1.', key=False),
          ]),
          B('Measure lengths in whole inches with a ruler', '2.MD.A.1', [
              sa('How long is the crayon?', 'Length:', key='4 inches', fig=ruler(6, (0, 4), 'crayon', div=1)),
              tf('To measure with a ruler, line up one end of the object with 0.', key=True),
              mc('How long is the pencil?', ['5 inches', '6 inches', '4 inches', '1 inch'], fig=ruler(6, (0, 5), 'pencil', div=1)),
              sa('A leaf reaches from 0 to 3 on an inch ruler.\nHow long is the leaf?', 'Length:', key='3 inches'),
              tf('A stick that reaches from 0 to 6 on an inch ruler is 7 inches long.', key=False),
          ]),
      ],
      f1=B('Write tenths and hundredths as decimals and locate them on a number line', '4.NF.C.6', [
          sa('The space from 0 to 1 is split into 10 equal parts.\nWrite the decimal at point A.', 'A =', key='0.1',
             fig=nl(0, 1, 0.1, labels={0: '0', 1: '1'}, pts=[(0.1, 'A')])),
          tf('{1/10} = 0.1', key=True),
          mc('Which decimal is equal to {1/100}?', ['0.01', '0.1', '1.01', '10.0']),
          sa('Write {1/100} as a decimal.', 'Decimal:', key='0.01'),
          tf('On a number line, 0.1 is between 0 and {1/100}.', key=False),
      ]),
      f2=B('Divide a unit fraction by a whole number', '5.NF.B.7.a', [
          sa('{1/2} is split into 3 equal parts.\nWhat fraction is each part?', 'Fraction:', key='1/6'),
          tf('{1/4} ÷ 2 = {1/8}', key=True),
          mc('{1/3} ÷ 2 = ?', ['{1/6}', '{2/3}', '{1/5}', '6']),
          sa('Divide.\n{1/2} ÷ 4', 'Quotient:', key='1/8'),
          tf('{1/5} ÷ 3 = {3/5}', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.2.b
    S('3.NF.A.2.b', 'Represent a fraction a/b on a number line by marking off a lengths of 1/b',
      main=[
          sa('What fraction is at point B?', 'B =', key='3/4', fig=fl(0, 1, 4, pts=[(0.75, 'B')])),
          plot('Start at 0 and mark off 5 lengths of {1/6}. Mark and label the point {5/6}.', fl(0, 1, 6),
               key='A point at the 5th tick mark after 0 (5 lengths of 1/6), labeled 5/6'),
          mc('A point is 3 lengths of {1/8} from 0.\nWhat fraction is at the point?', ['{3/8}', '{8/3}', '{1/3}', '{3/1}']),
          tf('The point {2/3} is 2 lengths of {1/3} from 0.', key=True),
          sa('What fraction is at point C? Write it as a fraction with a denominator of 4.', 'C =', key='7/4',
             fig=fl(0, 2, 4, pts=[(1.75, 'C')]), note='C is 7 lengths of 1/4 from 0. The question asks for fourths, so 7/4 is the form required.'),
      ],
      back=[
          B('Mark whole numbers as lengths from 0 on a number line', '2.MD.B.6', [
              plot('Mark and label 6 on the number line.', nl(0, 10, 1, labels={0: '0', 10: '10'}), key='A point at the 6th tick mark after 0, labeled 6'),
              tf('The point 3 is 3 lengths of 1 from 0.', key=True),
              mc('A point is 7 lengths of 1 from 0.\nWhat number is it?', ['7', '8', '6', '1']),
              sa('What number is at point A?', 'A =', key='4', fig=nl(0, 8, 1, labels={0: '0', 8: '8'}, pts=[(4, 'A')])),
              tf('The point 9 is 10 lengths of 1 from 0.', key=False),
          ]),
          B('Show sums as jumps on a number line', '2.MD.B.6', num=2, qs=[
              sa('Start at 20 on a number line and jump 15 more.\nWhere do you land?', 'Number:', key='35'),
              tf('Starting at 0, a jump of 30 and then a jump of 20 lands on 50.', key=True),
              mc('Start at 10 and make three jumps of 10.\nWhere do you land?', ['40', '30', '13', '50']),
              sa('Start at 25 and jump 40 more.\nWhere do you land?', 'Number:', key='65'),
              tf('Starting at 40, a jump of 15 lands on 65.', key=False),
          ]),
      ],
      f1=B('Multiply a fraction by a whole number with jumps on a number line', '4.NF.B.4.b', [
          sa('Start at 0 and make 4 jumps of {2/3} on a number line.\nWhere do you land?', 'Number:', key='8/3', note='2 2/3 is also correct.'),
          tf('3 jumps of {3/4} from 0 land on {9/4}.', key=True),
          mc('5 × {2/6} = ?', ['{10/6}', '{7/6}', '{10/30}', '{2/30}']),
          sa('Multiply.\n6 × {3/8}', 'Product:', key='18/8', note='2 2/8, 2 1/4, and 9/4 are also correct.'),
          tf('2 jumps of {5/6} from 0 land on {10/12}.', key=False),
      ]),
      f2=B('Add fractions with unlike denominators', '5.NF.A.1', [
          sa('Add.\n{1/2} + {1/3}', 'Sum:', key='5/6'),
          tf('{3/4} + {1/8} = {7/8}', key=True),
          mc('Add.\n{2/3} + {1/6}', ['{5/6}', '{3/9}', '{3/6}', '{2/18}']),
          sa('Add.\n{3/8} + {1/4}', 'Sum:', key='5/8'),
          tf('{1/4} + {1/3} = {2/7}', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.a
    S('3.NF.A.3.a', 'Understand equivalent fractions as the same size or the same point on a number line',
      main=[
          tf('The number lines are the same length. {1/2} and {2/4} are at the same point.', key=True,
             fig=two_lines(2, 4, [(0.5, '{1/2}')], [(0.5, '{2/4}')])),
          mc('The number lines are the same length.\nWhich fraction is at the same point as {2/3}?', ['{4/6}', '{2/6}', '{3/6}', '{5/6}'],
             fig=two_lines(3, 6, [(2 / 3, '{2/3}')])),
          sa('The two bars are the same size. The top bar shows {3/4} shaded and the bottom bar shows {6/8} shaded.\nAre the fractions equivalent? Explain.',
             ['Answer:', 'Explanation:'], key='Yes',
             note='The shaded parts are the same size (they cover the same amount of the same whole), so 3/4 = 6/8. Both parts are required.',
             fig=bars((4, 3), (8, 6))),
          tf('{1/3} and {2/6} are at different points on a number line from 0 to 1.', key=False),
          sa('Name a fraction in eighths that is at the same point as {1/4} on a number line.', 'Fraction:', key='2/8'),
      ],
      back=[
          B('Measure one length with two different units', '2.MD.A.2', [
              tf('A table measured in centimeters gives a larger number than the same table measured in meters.', key=True),
              mc('A pencil is 6 paper clips long and 3 crayons long.\nWhich unit is longer?', ['The crayon', 'The paper clip', 'They are the same length', 'You cannot tell']),
              sa('A shelf is 10 large blocks long and 20 small blocks long.\nDid the shelf\'s length change?', 'Answer:', key='No',
                 note='The shelf is the same length; only the unit changed.'),
              sa('A ribbon is 4 feet long. Is its length in inches a number greater than or less than 4?', 'Answer:', key='Greater than 4'),
              tf('When you measure with a bigger unit, you get a bigger number.', key=False),
          ]),
          B('Equal shares of the same whole', '2.G.A.3', [
              tf('Two halves of the same rectangle can have different shapes and still be equal shares.', key=True),
              sa('A square is cut into 2 equal triangles. Another square of the same size is cut into 2 equal rectangles.\nIs a triangle the same size as a rectangle?',
                 'Answer:', key='Yes', note='Each is half of the same-size square.'),
              mc('A circle is cut into 4 equal shares.\nWhat is each share called?', ['A fourth', 'A third', 'A half', 'A whole']),
              sa('How many halves make one whole?', 'Halves:', key='2'),
              tf('A third of a rectangle is larger than a half of the same rectangle.', key=False),
          ]),
      ],
      f1=B('Explain equivalent fractions with visual models', '4.NF.A.1', [
          sa('The bars show {3/5} and {6/10} of the same whole.\nExplain why the fractions are equal.', ['Explanation:', ''],
             key='Each fifth is split into 2 equal parts, so there are twice as many parts and twice as many shaded parts; '
                 'each new part is half the size, and the shaded amount stays the same.',
             note='Must connect both the number and the size of the parts.', fig=bars((5, 3), (10, 6))),
          tf('{2/5} = {4/10} because the numerator and the denominator are both multiplied by 2.', key=True),
          mc('Which fraction is equal to {3/4}?', ['{9/12}', '{3/12}', '{6/4}', '{4/3}']),
          sa('Find the missing number.\n{4/5} = {?/10}', 'Missing number:', key='8'),
          tf('{1/3} = {3/6}', key=False),
      ]),
      f2=B('Use equivalent fractions to add fractions with unlike denominators', '5.NF.A.1', [
          sa('Rewrite {1/2} and {1/5} with a common denominator. Then add.', ['Rewritten:', 'Sum:'], key='5/10 and 2/10; 7/10',
             note='Any common denominator is correct for the first part. Both parts are required.'),
          tf('{2/3} + {1/4} = {8/12} + {3/12}', key=True),
          mc('Add.\n{1/6} + {3/4}', ['{11/12}', '{4/10}', '{4/12}', '{3/24}']),
          sa('Add.\n{2/5} + {1/10}', 'Sum:', key='1/2', note='5/10 is also correct.'),
          tf('{1/3} + {1/2} = {2/5}', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.b
    S('3.NF.A.3.b', 'Recognize and generate simple equivalent fractions, and explain why they are equivalent',
      main=[
          sa('Find the missing number.\n{1/3} = {?/6}', 'Missing number:', key='2'),
          mc('Which fraction is equivalent to {3/4}?', ['{6/8}', '{3/8}', '{4/6}', '{4/3}']),
          draw_write('The bar shows {1/2} shaded. Draw lines to split each half into 4 equal parts.\nThen write the equivalent fraction in eighths.',
                     bar(2, 1), 'Fraction:', draw='Each half split into 4 equal parts (8 parts in all), with 4 parts shaded', key='4/8',
                     note='Grade both: the bar split into 8 equal parts with 4 shaded, and 4/8.'),
          tf('{2/6} = {1/3}', key=True),
          sa('Explain why {2/8} = {1/4}. You may use a model.', ['Explanation:', ''],
             key='Each fourth of a whole is made of 2 eighths, so 2 eighths cover the same amount as 1 fourth.',
             note='Any correct explanation with a visual model or number line that shows the same size or the same point is correct.'),
      ],
      back=[
          B('Halves, thirds, and fourths that make a whole', '2.G.A.3', [
              sa('How many fourths make a whole?', 'Fourths:', key='4'),
              tf('Three thirds make one whole.', key=True),
              mc('Which describes one whole?', ['2 halves', '3 halves', '2 thirds', '3 fourths']),
              sa('A rectangle is cut into 3 equal shares.\nHow many of the shares make the whole rectangle?', 'Shares:', key='3'),
              tf('Four halves make one whole.', key=False),
          ]),
          B('Write even numbers as doubles', '2.OA.C.3', [
              sa('Write 8 as the sum of two equal addends.', 'Sum:', key='4 + 4'),
              tf('6 = 3 + 3', key=True),
              mc('Which number is the double of 4?', ['8', '6', '4', '16']),
              sa('What is the double of 3?', 'Double:', key='6'),
              tf('10 = 6 + 4 shows 10 as the sum of two equal addends.', key=False),
          ]),
      ],
      f1=B('Generate equivalent fractions by multiplying the numerator and the denominator by the same number', '4.NF.A.1', [
          sa('Find the missing number.\n{3/5} = {?/15}', 'Missing number:', key='9'),
          tf('{4/6} = {8/12}', key=True),
          mc('Which fraction is equivalent to {2/5}?', ['{4/10}', '{2/10}', '{5/2}', '{3/6}']),
          sa('Write two fractions that are equivalent to {3/4}.', 'Fractions:', key='6/8 and 9/12', note='Any two fractions equal to 3/4 are correct.'),
          tf('{5/8} = {10/24}', key=False),
      ]),
      f2=B('Explain equivalent fractions as multiplying by a fraction equal to 1', '5.NF.B.5.b', [
          tf('{2/3} × {4/4} = {8/12}, and {8/12} = {2/3} because {4/4} = 1.', key=True),
          sa('To rewrite {3/5} as {9/15}, by which whole number must you multiply BOTH its numerator and its denominator?\n'
             'Which fraction equal to 1 is that the same as multiplying by?', ['Whole number:', 'Fraction equal to 1:'], key='3; 3/3',
             note='Both parts are required.'),
          mc('Which equation shows that {5/6} = {10/12}?', ['{5/6} × {2/2} = {10/12}', '{5/6} + {5/6} = {10/12}', '{5/6} × 2 = {10/12}', '{5/6} × {2/1} = {10/12}']),
          sa('Explain why multiplying {1/4} by {3/3} does not change its value.', ['Explanation:', ''],
             key='3/3 = 1, and multiplying a number by 1 does not change it.'),
          tf('{1/2} × {2/3} = {2/6} shows that {1/2} = {2/6}.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.c
    S('3.NF.A.3.c', 'Express whole numbers as fractions and recognize fractions that are equal to whole numbers',
      main=[
          sa('Write 5 as a fraction with a denominator of 1.', 'Fraction:', key='5/1'),
          mc('Which fraction is equal to 2?', ['{8/4}', '{4/8}', '{2/4}', '{2/8}']),
          tf('{6/6} = 6', key=False),
          sa('The number line from 0 to 3 is marked in thirds.\nWhat fraction in thirds names the point 2?', 'Fraction:', key='6/3',
             fig=fl(0, 3, 3, pts=[(2, '2')])),
          tf('{3/3} = 3', key=False),
      ],
      back=[
          B('Two halves or four quarters make a whole', '1.G.A.3', [
              sa('How many halves make one whole pizza?', 'Halves:', key='2'),
              tf('4 quarters of a sandwich make the whole sandwich.', key=True),
              mc('A pie is cut into 4 equal parts. All 4 parts are eaten.\nHow much of the pie is eaten?',
                 ['The whole pie', 'Half of the pie', 'A quarter of the pie', 'None of the pie']),
              sa('How many quarters make one whole?', 'Quarters:', key='4'),
              tf('2 quarters make a whole circle.', key=False),
          ]),
          B('Count lengths of 1 on a number line', '2.MD.B.6', [
              sa('How many lengths of 1 are there from 0 to 3 on a number line?', 'Lengths:', key='3'),
              tf('From 0 to 5 on a number line there are 5 lengths of 1.', key=True),
              mc('Which number is 2 lengths of 1 from 0?', ['2', '1', '3', '0']),
              sa('What number is at point A?', 'A =', key='5', fig=nl(0, 8, 1, labels={0: '0', 8: '8'}, pts=[(5, 'A')])),
              tf('From 0 to 4 on a number line there are 3 lengths of 1.', key=False),
          ]),
      ],
      f1=B('Write mixed numbers as fractions and fractions as mixed numbers', '4.NF.B.3.b', [
          sa('Write 2{1/3} as a fraction.', 'Fraction:', key='7/3'),
          tf('1{3/4} = {4/4} + {3/4}', key=True),
          mc('Which mixed number is equal to {11/4}?', ['2{3/4}', '3{1/4}', '2{1/4}', '1{3/4}']),
          sa('Write {9/2} as a mixed number.', 'Mixed number:', key='4 1/2'),
          tf('3{2/5} = {32/5}', key=False),
      ]),
      f2=B('Interpret a fraction as the numerator divided by the denominator', '5.NF.B.3', [
          sa('Write {20/4} as a division. Then find its value.', ['Division:', 'Value:'], key='20 ÷ 4; 5', note='Both parts are required.'),
          tf('{15/3} = 15 ÷ 3 = 5', key=True),
          mc('Which division is equal to {7/2}?', ['7 ÷ 2', '2 ÷ 7', '7 × 2', '7 - 2']),
          sa('Find the value of {42/6}.', 'Value:', key='7'),
          tf('{5/10} = 10 ÷ 5', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.d (same denominator)
    S('3.NF.A.3.d', 'Compare two fractions with the same denominator',
      main=[
          sa('Write >, =, or <.\n{3/8} ___ {5/8}', 'Symbol:', key='<'),
          tf('{5/6} > {1/6}', key=True),
          mc('Which fraction is greatest?', ['{3/4}', '{1/4}', '{2/4}', '{0/4}']),
          sa('Compare {2/3} and {1/3}. Write >, =, or <, and explain how you know.', ['Comparison:', 'Explanation:'], key='2/3 > 1/3',
             note='Both are thirds of the same whole, and 2 parts of size 1/3 is more than 1 part. Both parts are required.'),
          tf('{4/8} < {3/8}', key=False),
      ],
      back=[
          B('Compare two- and three-digit numbers', '2.NBT.A.4', [
              sa('Write >, =, or <.\n57 ___ 75', 'Symbol:', key='<'),
              tf('130 > 103', key=True),
              mc('Which number is least?', ['209', '290', '920', '902']),
              sa('Write >, =, or <.\n408 ___ 480', 'Symbol:', key='<'),
              tf('615 < 561', key=False),
          ]),
          B('Order objects by length', '1.MD.A.1', [
              sa('A red pencil is longer than a blue pencil. The blue pencil is longer than a green pencil.\nWhich pencil is longest?', 'Answer:',
                 key='The red pencil'),
              tf('If rope A is longer than rope B, then rope B is shorter than rope A.', key=True),
              mc('Ty\'s string is shorter than Ann\'s string. Ann\'s string is shorter than Bo\'s string.\nWhose string is shortest?',
                 ['Ty\'s', 'Ann\'s', 'Bo\'s', 'They are the same length.']),
              sa('A bat is longer than a stick.\nIs the stick longer or shorter than the bat?', 'Answer:', key='Shorter'),
              tf('If a crayon is shorter than a marker, then the marker is shorter than the crayon.', key=False),
          ]),
      ],
      f1=B('Compare fractions with different numerators and different denominators', '4.NF.A.2', [
          sa('Write >, =, or <.\n{2/3} ___ {5/8}', 'Symbol:', key='>'),
          tf('{3/5} > {1/2}', key=True),
          mc('Which comparison is true?', ['{3/4} > {7/10}', '{3/4} < {7/10}', '{3/4} = {7/10}', '{7/10} > {3/4}']),
          sa('Compare {5/6} and {7/9}. Write >, =, or <.', 'Comparison:', key='5/6 > 7/9'),
          tf('{2/5} > {1/2}', key=False),
      ]),
      f2=B('Use benchmark fractions to estimate sums of fractions', '5.NF.A.2', [
          sa('Is {2/5} + {3/8} more or less than 1? Explain using benchmark fractions.', ['Answer:', 'Reason:'], key='Less than 1',
             note='Both fractions are less than 1/2, so their sum is less than 1/2 + 1/2 = 1. Both parts are required.'),
          tf('{4/7} + {3/5} > 1, because each fraction is greater than {1/2}.', key=True),
          mc('Which is the best estimate of {7/8} + {5/6}?', ['About 2', 'About 1', 'About {1/2}', 'About 3']),
          sa('Use benchmark fractions to estimate {1/12} + {6/11}.', 'Estimate:', key='About 1/2',
             note='1/12 is close to 0 and 6/11 is close to 1/2.'),
          tf('{1/8} + {1/9} is about 1.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.d (same numerator)
    S('3.NF.A.3.d', 'Compare two fractions with the same numerator',
      main=[
          sa('Write >, =, or <.\n{1/3} ___ {1/6}', 'Symbol:', key='>'),
          tf('{2/8} < {2/4}', key=True),
          mc('Which fraction is greatest?', ['{1/2}', '{1/3}', '{1/6}', '{1/8}']),
          sa('Compare {2/3} and {2/6} of the same whole. Write >, =, or <, and explain how you know.', ['Comparison:', 'Explanation:'], key='2/3 > 2/6',
             note='Thirds are larger parts than sixths of the same whole, so 2 thirds is more than 2 sixths. Both parts are required.'),
          tf('{5/8} > {5/6}', key=False),
      ],
      back=[
          B('More equal shares make smaller shares', '1.G.A.3', [
              tf('A pizza cut into 4 equal parts has larger parts than the same pizza cut into 2 equal parts.', key=False),
              sa('Which is bigger: half of a sandwich or a quarter of the same sandwich?', 'Answer:', key='Half'),
              mc('The same cake is cut in two different ways.\nWhich way makes the smaller pieces?',
                 ['4 equal pieces', '2 equal pieces', 'Both make the same size', 'You cannot tell']),
              sa('A ribbon is cut into 2 equal parts. Another ribbon of the same length is cut into 4 equal parts.\nWhich ribbon has the longer parts?',
                 'Answer:', key='The ribbon cut into 2 parts'),
              tf('Halves of a circle are larger than quarters of the same circle.', key=True),
          ]),
          B('Compare halves, thirds, and fourths of the same shape', '2.G.A.3', [
              sa('Which is larger: a third or a fourth of the same rectangle?', 'Answer:', key='A third'),
              tf('A half of a circle is larger than a third of the same circle.', key=True),
              mc('Which share of the same square is smallest?', ['A fourth', 'A third', 'A half', 'The whole']),
              sa('Ann eats a half of a pie. Bo eats a third of a pie of the same size.\nWho eats more?', 'Answer:', key='Ann'),
              tf('A fourth of a rectangle is larger than a half of the same rectangle.', key=False),
          ]),
      ],
      f1=B('Compare fractions by finding a common numerator or a common denominator', '4.NF.A.2', [
          sa('Rewrite {3/5} with a numerator of 6. Then compare it with {6/12} using >, =, or <.', ['Rewritten:', 'Comparison:'],
             key='6/10; 3/5 > 6/12', note='Both parts are required.'),
          tf('{4/7} > {4/9}', key=True),
          mc('Which comparison is true?', ['{2/3} > {4/10}', '{2/3} < {4/10}', '{2/3} = {4/10}', '{4/10} > {2/3}']),
          sa('Write >, =, or <.\n{5/12} ___ {5/9}', 'Symbol:', key='<'),
          tf('{3/10} > {3/5}', key=False),
      ]),
      f2=B('Compare the size of a product with the size of one factor without multiplying', '5.NF.B.5.a', [
          tf('{3/4} × 10 is less than 10.', key=True),
          sa('Without multiplying, is {5/3} × 12 greater than, less than, or equal to 12?', 'Answer:', key='Greater than 12'),
          mc('Which product is less than 8?', ['{2/3} × 8', '{3/2} × 8', '{4/4} × 8', '2 × 8']),
          sa('Without multiplying, which is greater: {1/3} × 9 or {1/6} × 9?', 'Answer:', key='1/3 × 9'),
          tf('{7/8} × 5 is greater than 5.', key=False),
      ])),

    # ------------------------------------------------------------------ 3.NF.A.3.d (same whole)
    S('3.NF.A.3.d', 'Compare fractions only when they refer to the same whole, and justify the comparison with a model',
      main=[
          tf('Ana ate {1/2} of a small pizza. Ben ate {1/2} of a large pizza. They ate the same amount of pizza.', key=False),
          sa('Explain why {1/4} of a large cake can be more cake than {1/2} of a small cake.', ['Explanation:', ''],
             key='The wholes are different sizes, so a fourth of the large cake can be bigger than a half of the small cake.',
             note='Must say that fractions can be compared only when they refer to the same whole (or wholes of the same size).'),
          mc('The two bars are the same size.\nWhich comparison do they show?', ['{2/3} > {2/4}', '{2/3} < {2/4}', '{2/3} = {2/4}', '{2/4} > {2/3}'],
             fig=bars((3, 2), (4, 2))),
          draw_write('The bars are the same size. Shade {3/4} of the top bar and {3/8} of the bottom bar.\nThen write >, =, or < to compare {3/4} and {3/8}.',
                     bars((4, 0), (8, 0)), 'Comparison:',
                     draw='3 of the 4 parts of the top bar shaded, and 3 of the 8 parts of the bottom bar shaded', key='3/4 > 3/8',
                     note='Grade both: the shading of both bars, and 3/4 > 3/8.'),
          tf('To compare {2/6} and {5/6} with models, both models must show the same whole.', key=True),
      ],
      back=[
          B('Find how much longer one object is than another', '2.MD.A.4', [
              sa('A pencil is 7 inches long. A crayon is 4 inches long.\nHow much longer is the pencil?', 'Answer:', key='3 inches'),
              tf('A 10-cm stick is 6 cm longer than a 4-cm stick.', key=True),
              mc('A book is 12 inches long and a card is 5 inches long.\nHow much longer is the book?', ['7 inches', '17 inches', '5 inches', '12 inches']),
              sa('A rope is 9 feet long and a string is 6 feet long.\nHow much longer is the rope?', 'Answer:', key='3 feet'),
              tf('An 8-inch ribbon is 5 inches longer than a 2-inch ribbon.', key=False),
          ]),
          B('Equal shares of same-size wholes', '2.G.A.3', [
              tf('Halves of a big circle and halves of a small circle are the same size.', key=False),
              sa('Two same-size rectangles are each cut in half.\nAre all four halves the same size?', 'Answer:', key='Yes'),
              mc('Which pair shows the same amount?',
                 ['Half of a sheet of paper and half of a same-size sheet', 'Half of a big sheet and half of a small sheet',
                  'A third of a sheet and a half of the same sheet', 'A fourth of a sheet and a third of the same sheet']),
              sa('A small pizza and a large pizza are each cut into fourths.\nWhich pizza has the larger fourths?', 'Answer:', key='The large pizza'),
              tf('Equal shares of the same rectangle are the same size.', key=True),
          ]),
      ],
      f1=B('Compare fractions with the benchmark 1/2 and explain the comparison', '4.NF.A.2', [
          sa('Compare {2/5} and {5/8} by comparing each one with {1/2}. Write >, =, or <.', ['Comparison:', 'Reason:'], key='2/5 < 5/8',
             note='2/5 is less than 1/2 and 5/8 is more than 1/2, so 2/5 < 5/8. Both parts are required.'),
          tf('{7/12} > {1/2}', key=True),
          mc('Which fraction is less than {1/2}?', ['{3/7}', '{5/8}', '{4/6}', '{6/10}']),
          sa('Explain why {3/4} of a 1-meter rope is longer than {3/4} of a 1-foot rope.', ['Explanation:', ''],
             key='The wholes are different lengths: 1 meter is longer than 1 foot.', note='Must refer to the different-size wholes.'),
          tf('{5/12} > {1/2}', key=False),
      ]),
      f2=B('Explain why multiplying by a fraction greater or less than 1 makes a product larger or smaller', '5.NF.B.5.b', [
          tf('Multiplying 6 by {5/4} gives a number greater than 6.', key=True),
          sa('Explain why {2/3} × 15 is less than 15.', ['Explanation:', ''], key='2/3 is less than 1, so 2/3 of 15 is less than all of 15.'),
          mc('Which product is greater than 20?', ['{6/5} × 20', '{4/5} × 20', '{1/2} × 20', '{5/5} × 20']),
          sa('Explain why {4/4} × 7 = 7.', ['Explanation:', ''], key='4/4 = 1, and multiplying a number by 1 does not change it.'),
          tf('Multiplying 9 by {3/8} gives a number greater than 9.', key=False),
      ])),
]
