from qb import S, B, sa, mc, tf, plot, draw_write, work, nl, LONG_DIVISION
from common import ints


def halves(vmin, vmax, **kw):
    """Number line in steps of 0.25 with every whole number labeled."""
    labels = {v: str(v).replace('-', '−') for v in range(vmin, vmax + 1)}
    return nl(vmin, vmax, 0.25, labels=labels, **kw)


SETS = [
    # ------------------------------------------------------------------ 7.NS.A.1.a
    S('7.NS.A.1.a', 'Describe situations in which opposite quantities combine to make 0',
      main=[
          sa('Ari has $15 in his wallet. He spends all $15.\nWrite an addition expression for this situation and find its value.', 'Expression and value:',
             key='15 + (-15) = 0'),
          mc('Which situation combines to make 0?',
             ['Climbing up 8 floors, then down 8 floors', 'Gaining 5 points, then gaining 5 more points',
              'Walking 3 miles east, then 2 miles west', 'A temperature drop of 6°, then another drop of 6°']),
          sa('A diver is 12 feet below the surface of the water (-12 feet).\nHow many feet must she rise to be at the surface (0 feet)?', 'Feet:', key='12'),
          tf('A gain of 9 yards followed by a loss of 9 yards is a total change of 0 yards.', key=True),
          tf('A deposit of $40 followed by a withdrawal of $30 leaves an account balance unchanged.', key=False),
      ],
      back=[
          B('Use positive and negative numbers to represent quantities', '6.NS.C.5', [
              sa('Write an integer for 20 feet below sea level.', 'Integer:', key='-20'),
              sa('Write an integer for a gain of 7 yards.', 'Integer:', key='7', note='+7 is also correct.'),
              mc('Which integer represents a withdrawal of $35?', ['-35', '35', '0', '-3.5']),
              tf('A temperature of 4 degrees below zero can be written as -4°.', key=True),
              tf('The integer -10 represents a deposit of $10.', key=False),
          ]),
          B('Recognize opposite numbers', '6.NS.C.6.a', [
              sa('What is the opposite of 8?', 'Opposite:', key='-8'),
              sa('What is the opposite of -13?', 'Opposite:', key='13'),
              mc('Point P is at -5.\nWhich number is the same distance from 0 on the other side of 0?', ['5', '-10', '0', '10'], fig=ints(-6, 6, pts=[(-5, 'P')])),
              tf('The opposite of the opposite of 6 is 6.', key=True),
              tf('0 and 1 are opposites.', key=False),
          ]),
      ],
      f1=B('Use opposite exponents with the properties of integer exponents', '8.EE.A.1', nearest=True, qs=[
          sa('Find the value.\n5³ × 5⁻³', 'Value:', key='1'),
          sa('Write as a single power. Then find its value.\n2⁴ × 2⁻⁶', 'Answer:', key='2⁻² = 1/4'),
          mc('Which expression is equal to 1?', ['7⁻² × 7²', '7⁻² × 7⁻²', '7² × 7²', '7⁻² + 7²']),
          tf('10⁻² = {1/100}', key=True),
          tf('3⁻² = -9', key=False, note='3⁻² = 1/9.'),
      ]),
      f2=B('Explain the steps used to solve an equation', 'HSA-REI.A.1', [
          sa('To solve x - 9 = 4, Lia adds 9 to both sides.\nWhat property of equality justifies this step?', 'Property:',
             key='The addition property of equality', note='Any answer saying that adding the same number to both sides keeps the equation true.'),
          sa('Solve x + 15 = 6.\nWhat number do you add to both sides, and what is x?', 'Answer:', key='Add -15 to both sides; x = -9'),
          mc('Which step removes the 5 when solving 3x + 5 = 20?',
             ['Add -5 to both sides.', 'Add 5 to both sides.', 'Multiply both sides by -5.', 'Divide both sides by 5.']),
          tf('Adding -4 to both sides of x + 4 = 10 gives x = 6.', key=True),
          tf('Adding 8 to both sides of x - 8 = 3 gives x = -5.', key=False, note='It gives x = 11.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.b (number line)
    S('7.NS.A.1.b', 'Add rational numbers on a number line',
      main=[
          sa('Use the number line to add.\n-3 + 7', 'Sum:', fig=ints(-8, 8), key='4'),
          sa('Add.\n-6 + (-4)', 'Sum:', key='-10'),
          mc('Start at 2 on a number line and move 5 units to the left.\nWhich sum does this show?', ['2 + (-5)', '2 + 5', '-2 + 5', '-5 + (-2)']),
          draw_write('Show -2 + 6 on the number line. Start at -2 and draw an arrow 6 units long.\nWhat is the sum?', ints(-8, 8), 'Sum:',
                     draw='An arrow that starts at -2 and ends at 4 (6 units to the right)', key='4',
                     note='Grade both: the arrow from -2 to 4, and the sum 4.'),
          tf('-4.5 + 2 = -2.5', key=True),
      ],
      back=[
          B('Find and position integers on a number line', '6.NS.C.6.c', [
              sa('What number is at point A?', 'Number:', fig=ints(-6, 6, pts=[(-4, 'A')]), key='-4'),
              plot('Plot -3 and 5 on the number line.', ints(-6, 6), key='Points at -3 and 5'),
              mc('Which number is farthest to the left on a number line?', ['-7', '-2', '0', '3']),
              tf('-1 is to the right of -5 on a number line.', key=True),
              tf('-6 is between -3 and 0 on a number line.', key=False),
          ]),
          B('Add decimals', '5.NBT.B.7', [
              sa('Add.\n3.75 + 2.5', 'Sum:', key='6.25'),
              sa('Add.\n0.8 + 4.65', 'Sum:', key='5.45'),
              mc('Add.\n12.4 + 3.06', ['15.46', '15.10', '12.71', '46.4']),
              tf('2.7 + 1.3 = 4', key=True),
              tf('5.6 + 0.04 = 6', key=False),
          ]),
      ],
      f1=B('Locate irrational numbers on a number line', '8.NS.A.2', [
          sa('Between which two whole numbers is √20?', 'Answer:', key='4 and 5'),
          plot('Plot an approximate location of √2 on the number line.', ints(0, 4), key='A point between 1 and 2, a little less than halfway (about 1.4)'),
          mc('Which is the best approximation of √50 to the nearest tenth?', ['7.1', '7.0', '25', '7.5']),
          tf('√10 is between 3 and 4.', key=True),
          tf('π is less than 3.', key=False),
      ]),
      f2=B('Decide whether a sum is rational or irrational', 'HSN-RN.B.3', [
          sa('Is 3 + √2 rational or irrational?', 'Answer:', key='Irrational'),
          sa('Is {1/2} + {3/4} rational or irrational? Give its value.', 'Answer:', key='Rational; 5/4', note='1 1/4 or 1.25 is also correct for the value.'),
          mc('Which sum is irrational?', ['√3 + 4', '√9 + 4', '0.5 + {1/2}', '-2 + 2']),
          tf('The sum of two rational numbers is always rational.', key=True),
          tf('The sum of a rational number and an irrational number can be rational.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.b (additive inverses)
    S('7.NS.A.1.b', 'Use additive inverses: a number plus its opposite is 0',
      main=[
          sa('What number added to -9.5 gives 0?', 'Number:', key='9.5'),
          sa('Fill in the blank.\n{3/4} + ___ = 0', 'Blank:', key='-3/4'),
          mc('Which sum is equal to 0?', ['-2.6 + 2.6', '-2.6 + (-2.6)', '2.6 + 0', '-2.6 + 6.2']),
          tf('For any rational number p, -p + p = 0.', key=True),
          tf('The additive inverse of -7 is -7.', key=False, note='The additive inverse of -7 is 7.'),
      ],
      back=[
          B('Opposites are the same distance from 0', '6.NS.C.6.a', [
              sa('What is the opposite of 2.5?', 'Opposite:', key='-2.5'),
              mc('Which pair of numbers are opposites?', ['-11 and 11', '-11 and -11', '1 and -11', '11 and {1/11}']),
              sa('How far is -9 from 0 on a number line?', 'Distance:', key='9 units'),
              tf('-{2/3} and {2/3} are the same distance from 0.', key=True),
              tf('The opposite of 0 is 1.', key=False),
          ]),
          B('Interpret absolute value as distance from 0', '6.NS.C.7.c', [
              sa('Find the value.\n|-18|', 'Value:', key='18'),
              sa('A diver is at -30 feet.\nHow far is she from the surface (0 feet)?', 'Distance:', key='30 feet'),
              mc('Which number has an absolute value of 6?', ['-6', '{1/6}', '0', '-{1/6}']),
              tf('|-3.5| = |3.5|', key=True),
              tf('|-20| = -20', key=False),
          ]),
      ],
      f1=B('Tell whether a linear equation has one, no, or infinitely many solutions', '8.EE.C.7.a', [
          sa('How many solutions does this equation have?\n3x + 5 = 3x - 2', 'Answer:', key='No solution'),
          sa('How many solutions does this equation have?\n2(x + 4) = 2x + 8', 'Answer:', key='Infinitely many solutions'),
          mc('Which equation has exactly one solution?', ['4x + 1 = 2x + 7', '4x + 1 = 4x + 7', '4x + 1 = 4x + 1', '2(2x) = 4x']),
          tf('x + 6 = x - 6 has no solution.', key=True),
          tf('5x - 5x = 0 has no solution.', key=False, note='It is true for every x, so it has infinitely many solutions.'),
      ]),
      f2=B('Solve linear equations in one variable', 'HSA-REI.B.3', [
          sa('Solve for x.\n4x - 7 = -2x + 11', 'x =', key='3'),
          sa('Solve for x.\n-3(x - 2) = 15', 'x =', key='-3'),
          mc('Solve for x.\n{x/5} + 3 = -1', ['x = -20', 'x = 10', 'x = -4', 'x = 20']),
          tf('x = -2 is the solution of 6 + 2x = 2.', key=True),
          tf('x = 4 is the solution of 7 - x = 11.', key=False, note='The solution is x = -4.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.b (context)
    S('7.NS.A.1.b', 'Interpret sums of rational numbers in real-world situations',
      main=[
          sa('The temperature was -5°F at dawn. It rose 12°F by noon.\nWhat was the temperature at noon?', 'Temperature:', key='7°F'),
          sa('A submarine is at -240 feet. It rises 85 feet.\nWhat is its new position?', 'Position:', key='-155 feet', note='"155 feet below sea level" is also correct.'),
          mc('Jo\'s account balance is -$18. She deposits $25.\nWhich sum gives her new balance?', ['-18 + 25 = 7', '18 + 25 = 43', '-18 + (-25) = -43', '18 + (-25) = -7']),
          tf('A football team loses 6 yards, then gains 4 yards. The total change is -2 yards.', key=True),
          tf('A hiker 350 feet below sea level climbs 400 feet. She ends 50 feet below sea level.', key=False, note='She ends 50 feet above sea level.'),
      ],
      back=[
          B('Use signed numbers in a real-world situation', '6.NS.C.5', [
              sa('A stock\'s price changed by -$3.25.\nWas this a gain or a loss, and of how much?', 'Answer:', key='A loss of $3.25'),
              mc('Which number describes 15 meters above sea level?', ['15', '-15', '0', '{1/15}']),
              sa('Write a number for a temperature of 8 degrees below zero.', 'Number:', key='-8°'),
              tf('In a bank account, a balance of -$50 can mean $50 is owed.', key=True),
              tf('A temperature of -2° is warmer than 0°.', key=False),
          ]),
          B('Compare signed numbers in a real-world situation', '6.NS.C.7.b', [
              sa('Which temperature is colder, -8°C or -3°C?', 'Answer:', key='-8°C'),
              mc('Which statement is true?', ['-12 < -7', '-12 > -7', '-7 < -12', '-7 = -12']),
              sa('Write an inequality to compare elevations of -15 feet and -9 feet.', 'Inequality:', key='-15 < -9', note='-9 > -15 is also correct.'),
              tf('A balance of -$20 is less than a balance of -$5.', key=True),
              tf('-4°F is colder than -10°F.', key=False),
          ]),
      ],
      f1=B('Model a changing quantity with a linear function', '8.F.B.4', [
          sa('A diver starts at -10 feet and descends 4 feet per minute.\nWrite a function for her position d after t minutes.', 'd =', key='-4t - 10'),
          sa('The temperature is -6°F and rises 3°F per hour.\nWrite a function for the temperature T after h hours.', 'T =', key='3h - 6'),
          mc('An account balance starts at -$40 and goes up $15 per week.\nWhat is the balance after 4 weeks?', ['$20', '-$100', '$60', '-$20']),
          tf('For T = 3h - 6, the temperature reaches 0°F after 2 hours.', key=True),
          tf('For d = -4t - 10, the starting position is -4 feet.', key=False, note='The starting position is -10 feet.'),
      ]),
      f2=B('Evaluate a function and interpret the value in context', 'HSF-IF.A.2', [
          sa('h(t) = -16t² + 64t gives the height, in feet, of a ball after t seconds.\nFind h(1).', 'h(1) =', key='48 feet'),
          sa('T(h) = -2 + 1.5h gives the temperature in °C after h hours.\nFind T(6). What does it mean?', 'Answer:', key='7; the temperature is 7°C after 6 hours.'),
          mc('f(x) = 3x - 8\nWhat is f(-2)?', ['-14', '-2', '14', '2']),
          tf('If g(x) = -x + 5, then g(-3) = 8.', key=True),
          tf('If f(x) = x² - 4, then f(-3) = -13.', key=False, note='f(-3) = 5.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.c (subtract)
    S('7.NS.A.1.c', 'Subtract rational numbers by adding the additive inverse',
      main=[
          sa('Rewrite as an addition expression. Then find the value.\n4 - 9', 'Answer:', key='4 + (-9) = -5'),
          sa('Subtract.\n-7 - (-12)', 'Difference:', key='5'),
          mc('Which expression is equal to -3 - 8?', ['-3 + (-8)', '-3 + 8', '3 + (-8)', '3 + 8']),
          tf('-2.5 - 4 = -6.5', key=True),
          tf('{1/2} - (-{1/4}) = {1/4}', key=False, note='The difference is 3/4.'),
      ],
      back=[
          B('Subtract decimals', '5.NBT.B.7', [
              sa('Subtract.\n8.2 - 3.75', 'Difference:', key='4.45'),
              sa('Subtract.\n10 - 6.38', 'Difference:', key='3.62'),
              mc('Subtract.\n5.4 - 2.9', ['2.5', '3.5', '2.15', '8.3']),
              tf('7.06 - 2.5 = 4.56', key=True),
              tf('9.3 - 0.7 = 9.6', key=False),
          ]),
          B('Subtract fractions with unlike denominators', '5.NF.A.1', [
              sa('Subtract.\n{5/6} - {1/4}', 'Difference:', key='7/12'),
              sa('Subtract.\n3{1/2} - 1{2/3}', 'Difference:', key='1 5/6', note='11/6 is also correct.'),
              mc('Subtract.\n{3/4} - {2/5}', ['{7/20}', '{1/20}', '{5/9}', '{1/2}']),
              tf('{2/3} - {1/6} = {1/2}', key=True),
              tf('{4/5} - {1/3} = {3/2}', key=False),
          ]),
      ],
      f1=B('Find a rate of change from two points with negative coordinates', '8.F.B.4', [
          sa('Find the rate of change of the line through (-2, 5) and (3, -5).', 'Rate of change:', key='-2'),
          sa('Find the slope of the line through (-4, -1) and (2, 8).', 'Slope:', key='3/2', note='1.5 or 1 1/2 is also correct.'),
          mc('What is the slope of the line through (1, -3) and (-1, 5)?', ['-4', '4', '-1', '1']),
          tf('The slope of the line through (-3, -2) and (0, 4) is 2.', key=True),
          tf('The slope of the line through (2, -1) and (5, -7) is 2.', key=False, note='The slope is -2.'),
      ]),
      f2=B('Subtract polynomials', 'HSA-APR.A.1', [
          sa('Subtract.\n(5x² - 3x + 2) - (2x² - 7x - 4)', 'Difference:', key='3x² + 4x + 6'),
          sa('Subtract.\n(4x - 9) - (-x + 3)', 'Difference:', key='5x - 12'),
          mc('Subtract.\n(x² + 2x) - (3x² - 5x)', ['-2x² + 7x', '-2x² - 3x', '4x² + 7x', '-2x² + 3x']),
          tf('(6x + 1) - (2x - 5) = 4x + 6', key=True),
          tf('(3x² - x) - (x² + x) = 2x²', key=False, note='The difference is 2x² - 2x.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.c (distance)
    S('7.NS.A.1.c', 'Find the distance between two rational numbers as the absolute value of their difference',
      main=[
          sa('Find the distance between -6 and 9 on the number line.', 'Distance:', fig=ints(-10, 10, every=2), key='15'),
          sa('Find the distance between -4.5 and -1.2 on a number line.', 'Distance:', key='3.3'),
          mc('Which expression gives the distance between -3 and 8 on a number line?', ['|-3 - 8|', '-3 - 8', '|-3 + 8|', '-3 + 8']),
          tf('|2 - (-5)| = 7, so 2 and -5 are 7 units apart.', key=True),
          tf('The distance between -10 and -2 on a number line is 12.', key=False, note='The distance is 8.'),
      ],
      back=[
          B('Find the distance between points with the same x- or y-coordinate', '6.NS.C.8', [
              sa('Find the distance between (-3, 4) and (5, 4).', 'Distance:', key='8 units'),
              sa('Find the distance between (2, -6) and (2, 1).', 'Distance:', key='7 units'),
              mc('Which two points are 5 units apart?', ['(1, -2) and (1, 3)', '(1, -2) and (1, 2)', '(1, -2) and (6, 3)', '(-2, 1) and (2, 1)']),
              tf('(-4, -1) and (-4, 6) are 7 units apart.', key=True),
              tf('(-5, 2) and (3, 2) are 2 units apart.', key=False, note='They are 8 units apart.'),
          ]),
          B('Position fractions and decimals on a number line', '6.NS.C.6.c', [
              plot('Plot -1.5 and {3/4} on the number line.', halves(-2, 2), key='Points at -1.5 and 3/4 (0.75)'),
              sa('Name a number between -2 and -1.', 'Number:', key='-1.5', note='Any number greater than -2 and less than -1 is correct.'),
              mc('Which number is between -0.5 and 0?', ['-0.25', '-0.75', '0.25', '-1']),
              tf('-{1/2} is to the left of 0 on a number line.', key=True),
              tf('-2.3 is to the right of -2 on a number line.', key=False),
          ]),
      ],
      f1=B('Use the Pythagorean theorem to find the distance between two points', '8.G.B.8', [
          sa('Find the distance between (1, 2) and (4, 6).', 'Distance:', key='5 units'),
          sa('Find the distance between (-2, -3) and (4, 5).', 'Distance:', key='10 units'),
          mc('What is the distance between (0, 0) and (5, 12)?', ['13 units', '17 units', '7 units', '60 units']),
          tf('The distance between (-1, 1) and (2, 5) is 5 units.', key=True),
          tf('The distance between (0, 0) and (3, 3) is 6 units.', key=False, note='The distance is √18, about 4.24 units.'),
      ]),
      f2=B('Use coordinates to find the perimeter of a polygon', 'HSG-GPE.B.7', [
          sa('A triangle has vertices (0, 0), (6, 0), and (6, 8).\nFind its perimeter.', 'Perimeter:', key='24 units'),
          sa('A rectangle has vertices (-3, -2), (5, -2), (5, 4), and (-3, 4).\nFind its perimeter.', 'Perimeter:', key='28 units'),
          mc('A triangle has vertices (-2, 1), (2, 1), and (2, 4).\nWhat is its perimeter?', ['12 units', '7 units', '10 units', '6 units']),
          tf('A square with vertices (1, 1), (4, 1), (4, 4), and (1, 4) has a perimeter of 12 units.', key=True),
          tf('A triangle with vertices (0, 0), (8, 0), and (0, 6) has a perimeter of 14 units.', key=False, note='The perimeter is 24 units.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.1.d
    S('7.NS.A.1.d', 'Use properties of operations to add and subtract rational numbers',
      main=[
          work('Find the sum by grouping numbers to make the work easier. Show your work.\n-8 + 13.5 + 8', 'Sum:',
               method='Any grouping that uses the commutative and associative properties correctly. Example: (-8 + 8) + 13.5 = 0 + 13.5. Other valid groupings are also correct.',
               key='13.5'),
          sa('Find the sum.\n{3/4} + (-2) + {1/4}', 'Sum:', key='-1'),
          mc('Which property is shown?\n-5 + 2.7 = 2.7 + (-5)', ['Commutative property of addition', 'Associative property of addition', 'Additive identity property', 'Additive inverse property']),
          tf('-6 + (4 + 6) = (-6 + 6) + 4', key=True),
          tf('7 - 3 = 3 - 7', key=False, note='Subtraction is not commutative: 4 ≠ -4.'),
      ],
      back=[
          B('Apply properties to write equivalent expressions', '6.EE.A.3', [
              sa('Use the distributive property to rewrite 3(x + 5).', 'Expression:', key='3x + 15'),
              sa('Combine like terms.\n4y + 2 + 6y', 'Expression:', key='10y + 2'),
              mc('Which expression is equivalent to 2(4 + n)?', ['8 + 2n', '8 + n', '6 + n', '4 + 2n']),
              tf('5 + (a + 7) = (5 + 7) + a', key=True),
              tf('6(x + 2) = 6x + 2', key=False),
          ]),
          B('Add multi-digit decimals', '6.NS.B.3', [
              sa('Add.\n14.62 + 7.9', 'Sum:', key='22.52'),
              sa('Add.\n0.75 + 3.6 + 1.25', 'Sum:', key='5.6'),
              mc('Add.\n9.08 + 2.5', ['11.58', '9.33', '11.13', '34.08']),
              tf('2.25 + 3.75 = 6', key=True),
              tf('4.5 + 0.55 = 5.5', key=False),
          ]),
      ],
      f1=B('Solve equations by collecting like terms', '8.EE.C.7.b', [
          sa('Solve for x.\n-2.5x + 4 + 1.5x = -3', 'x =', key='7'),
          sa('Solve for x.\n{1/3}x - 5 + {2/3}x = 9', 'x =', key='14'),
          mc('Solve for x.\n3x - 7 + x = 2x + 5', ['x = 6', 'x = -1', 'x = 2', 'x = 12']),
          tf('x = -4 is the solution of 5x + 3 - 2x = -9.', key=True),
          tf('x = 2 is the solution of -x + 6 + 3x = 8.', key=False, note='The solution is x = 1.'),
      ]),
      f2=B('Use the structure of an expression to rewrite it', 'HSA-SSE.A.2', [
          sa('Rewrite x² - 9 as a product of two factors.', 'Product:', key='(x + 3)(x - 3)'),
          sa('Factor out the greatest common factor.\n4x² + 12x', 'Product:', key='4x(x + 3)'),
          mc('Which expression is equivalent to x² - 25?', ['(x - 5)(x + 5)', '(x - 5)²', '(x + 5)²', '(x - 25)(x + 1)']),
          tf('x² + 6x + 9 = (x + 3)²', key=True),
          tf('x² - 16 = (x - 4)²', key=False, note='x² - 16 = (x - 4)(x + 4).'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.a (multiply)
    S('7.NS.A.2.a', 'Multiply rational numbers using the rules for signs',
      main=[
          sa('Multiply.\n-6 × 7', 'Product:', key='-42'),
          sa('Multiply.\n-2.5 × (-4)', 'Product:', key='10'),
          mc('Multiply.\n-{2/3} × {9/10}', ['-{3/5}', '{3/5}', '-{11/13}', '-{27/20}']),
          tf('(-1)(-1) = 1', key=True),
          tf('The product of three negative numbers is positive.', key=False),
      ],
      back=[
          B('Multiply fractions', '5.NF.B.4.a', [
              sa('Multiply.\n{3/5} × {10/9}', 'Product:', key='2/3'),
              sa('Multiply.\n{4/7} × 14', 'Product:', key='8'),
              mc('Multiply.\n{5/6} × {3/4}', ['{5/8}', '{8/10}', '{15/10}', '{3/8}']),
              tf('{1/2} × {2/3} = {1/3}', key=True),
              tf('{3/4} × 8 = 24', key=False),
          ]),
          B('Multiply decimals', '5.NBT.B.7', [
              sa('Multiply.\n2.4 × 3.5', 'Product:', key='8.4'),
              sa('Multiply.\n0.6 × 0.7', 'Product:', key='0.42'),
              mc('Multiply.\n1.25 × 8', ['10', '100', '1', '9.25']),
              tf('0.3 × 0.3 = 0.09', key=True),
              tf('4.2 × 10 = 4.20', key=False),
          ]),
      ],
      f1=B('Find powers of negative numbers', '8.EE.A.1', [
          sa('Find the value.\n(-2)⁵', 'Value:', key='-32'),
          sa('Find the value.\n(-3)² × (-3)', 'Value:', key='-27'),
          mc('Which expression has a positive value?', ['(-4)⁴', '(-4)³', '-4⁴', '(-4)⁵']),
          tf('(-5)² = 25', key=True),
          tf('-2⁴ = 16', key=False, note='-2⁴ = -(2⁴) = -16.'),
      ]),
      f2=B('Multiply polynomials', 'HSA-APR.A.1', [
          sa('Multiply.\n-3x(2x - 5)', 'Product:', key='-6x² + 15x'),
          sa('Multiply.\n(x - 4)(x + 6)', 'Product:', key='x² + 2x - 24'),
          mc('Multiply.\n(-2x)(-7x)', ['14x²', '-14x²', '-9x', '14x']),
          tf('(x - 3)(x - 3) = x² - 6x + 9', key=True),
          tf('-4(x - 2) = -4x - 8', key=False, note='-4(x - 2) = -4x + 8.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.a (context)
    S('7.NS.A.2.a', 'Interpret products of rational numbers in real-world situations',
      main=[
          sa('A stock\'s price drops $1.75 each day for 6 days.\nWhat is the total change in price?', 'Change:', key='-$10.50'),
          sa('A diver descends 2.5 feet each second.\nWhat is the change in her position after 8 seconds?', 'Change:', key='-20 feet'),
          mc('A tank loses 3 gallons each minute.\nWhich product gives the change in the amount of water after 12 minutes?',
             ['12 × (-3) = -36', '12 × 3 = 36', '-12 × (-3) = 36', '12 + (-3) = 9']),
          tf('The temperature falls 4°F each hour for 5 hours. The total change is -20°F.', key=True),
          tf('An account balance changes by -$15 each week. The change over 3 weeks is $45.', key=False, note='The change is -$45.'),
      ],
      back=[
          B('Multiply fractions and mixed numbers in word problems', '5.NF.B.6', [
              sa('A recipe uses {3/4} cup of oats for each batch.\nHow many cups of oats are needed for 6 batches?', 'Cups:', key='4 1/2', note='9/2 is also correct.'),
              sa('A path is 2{1/2} miles long. Sam walks {2/5} of it.\nHow far does he walk?', 'Distance:', key='1 mile'),
              mc('A board is {7/8} yard long. Ty cuts a piece that is {1/2} as long as the board.\nHow long is the piece?', ['{7/16} yard', '{7/4} yards', '1{3/8} yards', '{8/14} yard']),
              tf('{2/3} of a 12-foot rope is 8 feet.', key=True),
              tf('4 bags each hold {2/3} pound of nuts. Together they hold 3 pounds.', key=False, note='They hold 8/3 = 2 2/3 pounds.'),
          ]),
          B('Explain the meaning of signed numbers and 0', '6.NS.C.5', [
              sa('In a game, a score of 0 means no points won or lost.\nWhat does a score of -12 mean?', 'Meaning:', key='12 points were lost (12 points below 0).'),
              mc('Sea level is 0 meters.\nWhich elevation is 30 meters below sea level?', ['-30 m', '30 m', '0 m', '-3 m']),
              sa('What does a change of -$8 in a bank account mean?', 'Meaning:', key='$8 was taken out of the account.'),
              tf('A temperature change of -5° means it got colder.', key=True),
              tf('On a horizontal number line, positive numbers are to the left of 0.', key=False),
          ]),
      ],
      f1=B('Solve real-world equations with negative rates', '8.EE.C.7.b', [
          sa('A balloon at 300 m descends 12.5 m each minute. Solve 300 - 12.5t = 175 to find when it is at 175 m.', 't =', key='10 minutes'),
          sa('A diver at -8 feet descends 1.5 feet each second. Solve -8 - 1.5t = -26 to find when she is at -26 feet.', 't =', key='12 seconds'),
          mc('Solve for x.\n-4x + 10 = -14', ['x = 6', 'x = -6', 'x = 1.5', 'x = -1']),
          tf('t = 5 is the solution of 20 - 3t = 5.', key=True),
          tf('x = -3 is the solution of -2x - 7 = 13.', key=False, note='The solution is x = -10.'),
      ]),
      f2=B('Create a one-variable equation for a situation with a negative rate', 'HSA-CED.A.1', [
          sa('A phone battery is at 90% and drops 6% each hour.\nWrite and solve an equation to find when it reaches 30%.', 'Answer:',
             key='90 - 6h = 30; h = 10 hours', note='Any correct equation earns credit.'),
          sa('A submarine at -50 m dives 20 m each minute.\nWrite and solve an equation to find when it reaches -170 m.', 'Answer:',
             key='-50 - 20t = -170; t = 6 minutes', note='Any correct equation earns credit.'),
          mc('A store\'s profit was -$400 and goes up $125 each month.\nWhich equation finds the month m when the profit is $600?',
             ['-400 + 125m = 600', '400 + 125m = 600', '-400 - 125m = 600', '125 - 400m = 600']),
          tf('A 72°F room cools 4°F each hour. The equation 72 - 4t = 40 finds when the room is 40°F.', key=True),
          tf('The solution of 72 - 4t = 40 is t = 28.', key=False, note='t = 8.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.b (divide)
    S('7.NS.A.2.b', 'Divide integers and explain the sign of a quotient',
      main=[
          sa('Divide.\n-48 ÷ 6', 'Quotient:', key='-8'),
          sa('Divide.\n-63 ÷ (-9)', 'Quotient:', key='7'),
          mc('Which fraction is equal to -{3/4}?', ['{-3/4}', '{-3/-4}', '{3/4}', '{4/-3}']),
          tf('{-10/2} = {10/-2} = -5', key=True),
          tf('-7 ÷ 0 = 0', key=False, note='Division by 0 is undefined.'),
      ],
      back=[
          B('Divide multi-digit whole numbers', '6.NS.B.2', [
              sa('Divide.\n1,872 ÷ 24', 'Quotient:', key='78'),
              sa('Divide.\n3,915 ÷ 45', 'Quotient:', key='87'),
              mc('Divide.\n2,436 ÷ 12', ['203', '23', '230', '2,030']),
              tf('5,040 ÷ 35 = 144', key=True),
              tf('1,950 ÷ 15 = 13', key=False),
          ]),
          B('Divide fractions', '6.NS.A.1', [
              sa('Divide.\n{4/5} ÷ {2/15}', 'Quotient:', key='6'),
              sa('Divide.\n3 ÷ {3/8}', 'Quotient:', key='8'),
              mc('Divide.\n{7/10} ÷ {1/5}', ['3{1/2}', '{7/50}', '{2/7}', '1{2/5}']),
              tf('{3/8} ÷ {3/4} = {1/2}', key=True),
              tf('{5/6} ÷ {5/12} = {1/2}', key=False),
          ]),
      ],
      f1=B('Classify numbers as rational or irrational', '8.NS.A.1', [
          sa('Is {-5/8} rational? Explain.', 'Answer:', key='Yes. It is a quotient of the integers -5 and 8.'),
          mc('Which number is irrational?', ['√7', '{-22/7}', '0.25', '-√16']),
          sa('Write -2.4 as a quotient of two integers.', 'Quotient:', key='-12/5', note='Any equivalent quotient, such as -24/10, is correct.'),
          tf('Every integer is a rational number.', key=True),
          tf('√25 is irrational.', key=False),
      ]),
      f2=B('Decide whether a product is rational or irrational', 'HSN-RN.B.3', [
          sa('Is -3 × √5 rational or irrational?', 'Answer:', key='Irrational'),
          sa('Is {-2/3} × {9/4} rational or irrational? Give its value.', 'Answer:', key='Rational; -3/2', note='-1 1/2 or -1.5 is also correct for the value.'),
          mc('Which product is rational?', ['√2 × √8', '2 × √3', '-1 × π', '5 × √2']),
          tf('The product of a nonzero rational number and an irrational number is irrational.', key=True),
          tf('The quotient of two rational numbers (with a nonzero divisor) can be irrational.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.b (context)
    S('7.NS.A.2.b', 'Interpret quotients of rational numbers in real-world situations',
      main=[
          sa('A stock lost $18 in value over 6 days at a steady rate.\nWhat was the change in value per day?', 'Change per day:', key='-$3'),
          sa('A diver\'s position changed by -45 feet in 9 seconds at a steady rate.\nWhat was the change in position per second?', 'Change per second:', key='-5 feet'),
          mc('The temperature changed by -14°F over 4 hours at a steady rate.\nWhat was the change per hour?', ['-3.5°F', '3.5°F', '-56°F', '-10°F']),
          tf('A balance changes by -$120 over 8 weeks at a steady rate. The change is -$15 per week.', key=True),
          tf('A hiker descends 600 feet in 4 hours at a steady rate. Her change in elevation is 150 feet per hour.', key=False, note='The change is -150 feet per hour.'),
      ],
      back=[
          B('Divide fractions in word problems', '6.NS.A.1', [
              sa('How many {3/4}-cup servings are in 6 cups of rice?', 'Servings:', key='8'),
              sa('A {2/3}-mile trail is split into 4 equal parts.\nHow long is each part?', 'Length:', key='1/6 mile'),
              mc('A strip {5/6} meter long is cut into pieces {1/12} meter long.\nHow many pieces are there?', ['10', '{5/72}', '12', '6']),
              tf('There are 6 half-pound portions in 3 pounds.', key=True),
              tf('3 people share {3/4} pound of nuts equally. Each gets {1/2} pound.', key=False, note='Each gets 1/4 pound.'),
          ]),
          B('Divide unit fractions and whole numbers in word problems', '5.NF.B.7.c', [
              sa('How many {1/4}-pound burgers can be made from 5 pounds of meat?', 'Burgers:', key='20'),
              sa('3 friends share {1/2} pound of grapes equally.\nHow much does each friend get?', 'Amount:', key='1/6 pound'),
              mc('2 people share {1/3} of a pizza equally.\nHow much of the whole pizza does each person get?',
                 ['{1/6} of the pizza', '{2/3} of the pizza', '6 pizzas', '{3/2} of the pizza']),
              tf('4 ÷ {1/5} = 20', key=True),
              tf('{1/8} ÷ 2 = {1/4}', key=False),
          ]),
      ],
      f1=B('Find a rate of change from a description', '8.F.B.4', [
          sa('A tank held 240 gallons at 2:00 and 180 gallons at 2:15. It drained at a constant rate.\nWhat is the rate of change in gallons per minute?', 'Rate of change:', key='-4 gallons per minute'),
          sa('A plane descends from 30,000 feet to 21,000 feet in 15 minutes at a constant rate.\nWhat is the rate of change in feet per minute?', 'Rate of change:', key='-600 feet per minute'),
          mc('A line passes through (0, 50) and (10, 20).\nWhat is its rate of change?', ['-3', '3', '-30', '-{1/3}']),
          tf('A balance that goes from $80 to $20 in 12 weeks at a constant rate changes by -$5 per week.', key=True),
          tf('A temperature that goes from 10° to -6° in 4 hours at a constant rate changes by -1° per hour.', key=False, note='It changes by -4° per hour.'),
      ]),
      f2=B('Calculate and interpret a negative average rate of change', 'HSF-IF.B.6', [
          sa('The table shows temperatures.\nWhat is the average rate of change from 0 hours to 6 hours?', 'Average rate:',
             fig=dict(k='table', rows=[['Time (h)', '0', '3', '6'], ['Temperature (°F)', '12', '3', '-6']], header='col'), key='-3°F per hour'),
          sa('f(x) = -x² + 10\nWhat is the average rate of change from x = 1 to x = 3?', 'Average rate:', key='-4'),
          mc('A company\'s profit was $5,000 in year 2 and $2,000 in year 5.\nWhat is the average rate of change?',
             ['-$1,000 per year', '$1,000 per year', '-$3,000 per year', '-$600 per year']),
          tf('A negative average rate of change means the quantity decreased over the interval.', key=True),
          tf('For f(x) = 5 - 2x, the average rate of change from x = 0 to x = 4 is 2.', key=False, note='It is -2.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.c
    S('7.NS.A.2.c', 'Use properties of operations to multiply and divide rational numbers',
      main=[
          work('Use properties to multiply. Show how you grouped or ordered the factors.\n-4 × 7.3 × 25', 'Product:',
               method='Any correct use of the commutative and associative properties. Example: (-4 × 25) × 7.3 = -100 × 7.3. Other valid groupings are also correct.',
               key='-730'),
          sa('Multiply.\n{3/5} × (-12) × {5/3}', 'Product:', key='-12'),
          mc('Which property is shown?\n-2 × (5 × 3.1) = (-2 × 5) × 3.1',
             ['Associative property of multiplication', 'Commutative property of multiplication', 'Distributive property', 'Multiplicative identity property']),
          tf('-6 × (10 + {1/2}) = -60 + (-3)', key=True),
          tf('-8 × {1/8} = 1', key=False, note='The product is -1.'),
      ],
      back=[
          B('Apply the distributive property', '6.EE.A.3', [
              sa('Rewrite using the distributive property.\n7(2y + 3)', 'Expression:', key='14y + 21'),
              sa('Use the distributive property to find 8 × 47 as 8 × (40 + 7).', 'Product:', key='376'),
              mc('Which expression is equivalent to 5(x + 9)?', ['5x + 45', '5x + 9', 'x + 45', '5x + 14']),
              tf('4(3 + 2.5) = 12 + 10', key=True),
              tf('3(a + 4) = 3a + 7', key=False),
          ]),
          B('Use the commutative and associative properties of multiplication', '3.OA.B.5', [
              sa('Fill in the blank.\n6 × 4 = 4 × ___', 'Blank:', key='6'),
              sa('Find 2 × 7 × 5 by first multiplying 2 × 5.', 'Product:', key='70'),
              mc('Which expression is equal to (3 × 2) × 4?', ['3 × (2 × 4)', '3 + (2 × 4)', '(3 + 2) × 4', '3 × 2 + 4']),
              tf('8 × 3 = 3 × 8', key=True),
              tf('(2 × 3) × 5 = 2 × 3 + 5', key=False),
          ]),
      ],
      f1=B('Solve equations by multiplying by a reciprocal', '8.EE.C.7.b', [
          sa('Solve for x.\n-{3/4}x = 18', 'x =', key='-24'),
          sa('Solve for x.\n-0.6x = -4.2', 'x =', key='7'),
          mc('Solve for x.\n{2/5}(x - 10) = -6', ['x = -5', 'x = -25', 'x = 25', 'x = 5']),
          tf('x = -10 is the solution of -{1/2}x = 5.', key=True),
          tf('x = 3 is the solution of -1.5x = 4.5.', key=False, note='The solution is x = -3.'),
      ]),
      f2=B('Rewrite expressions with rational exponents', 'HSN-RN.A.2', [
          sa('Find the value.\n27^(1/3)', 'Value:', key='3'),
          sa('Write √x using a rational exponent.', 'Answer:', key='x^(1/2)'),
          mc('Which number is equal to 16^(1/2)?', ['4', '8', '2', '32']),
          tf('(x³)^(1/3) = x', key=True),
          tf('25^(1/2) = 12.5', key=False, note='25^(1/2) = 5.'),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.2.d
    S('7.NS.A.2.d', 'Use long division to write a rational number as a terminating or repeating decimal',
      main=[
          work('Use long division to write {3/8} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION, key='0.375'),
          work('Use long division to write {5/11} as a decimal. Show your work.', 'Decimal:', method=LONG_DIVISION,
               key='0.4545... (the digits 45 repeat)', note='A bar over 45 is also correct.'),
          mc('Which decimal is equal to -{7/12}?', ['-0.58333... (the 3 repeats)', '-0.712', '-0.5833 (the decimal ends)', '-1.714...']),
          tf('{2/9} = 0.222..., a repeating decimal.', key=True),
          tf('{7/20} is a repeating decimal.', key=False, note='7/20 = 0.35, a terminating decimal.'),
      ],
      back=[
          B('Write fractions with denominators of 10 or 100 as decimals', '4.NF.C.6', [
              sa('Write {7/10} as a decimal.', 'Decimal:', key='0.7'),
              sa('Write {43/100} as a decimal.', 'Decimal:', key='0.43'),
              mc('Which decimal is equal to {6/100}?', ['0.06', '0.6', '6.0', '0.006']),
              tf('{9/10} = 0.9', key=True),
              tf('{25/100} = 2.5', key=False),
          ]),
          B('Divide multi-digit whole numbers', '6.NS.B.2', [
              sa('Divide.\n7,425 ÷ 25', 'Quotient:', key='297'),
              sa('Divide.\n4,368 ÷ 52', 'Quotient:', key='84'),
              mc('Divide.\n9,072 ÷ 36', ['252', '25.2', '2,520', '242']),
              tf('6,912 ÷ 48 = 144', key=True),
              tf('2,925 ÷ 75 = 49', key=False),
          ]),
      ],
      f1=B('Write a repeating decimal as a fraction', '8.NS.A.1', [
          sa('Write 0.777... (the 7 repeats) as a fraction.', 'Fraction:', key='7/9'),
          sa('Write 0.1818... (the digits 18 repeat) as a fraction.', 'Fraction:', key='2/11', note='18/99 is also correct.'),
          mc('Which fraction is equal to 0.333... (the 3 repeats)?', ['{1/3}', '{3/10}', '{33/100}', '{3/100}']),
          tf('0.999... (the 9 repeats) is equal to 1.', key=True),
          tf('0.4545... (the digits 45 repeat) is equal to {45/100}.', key=False, note='It is equal to 45/99 = 5/11.'),
      ]),
      f2=B('Report a decimal result to a sensible level of accuracy', 'HSN-Q.A.3', [
          sa('A 10-foot board is cut into 3 equal pieces. The tape measure reads to the nearest hundredth of a foot.\nReport the length of each piece to that accuracy.', 'Length:', key='3.33 feet'),
          sa('{2/7} = 0.285714... Round it to the nearest thousandth.', 'Rounded:', key='0.286'),
          mc('A scale reads to the nearest 0.1 kg. 5 kg of flour is split into 3 equal bags.\nWhich report of each bag\'s mass fits the scale?', ['1.7 kg', '1.666666 kg', '2 kg', '1.67 kg']),
          tf('Reporting {1/3} hour as 0.33 hour is accurate to the nearest hundredth of an hour.', key=True),
          tf('A length reported as 4.0 cm is less precise than a length reported as 4 cm.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.NS.A.3
    S('7.NS.A.3', 'Solve real-world problems with the four operations on rational numbers',
      main=[
          sa('A freezer is at 4°C. It cools 1.5°C every hour.\nWhat is the temperature after 6 hours?', 'Temperature:', key='-5°C'),
          sa('Maya owes $42.60. She pays it off in 6 equal payments.\nHow much is each payment?', 'Payment:', key='$7.10'),
          mc('A diver is at -18 m. She rises {1/3} of the distance to the surface.\nWhat is her new position?', ['-12 m', '-6 m', '-24 m', '12 m']),
          tf('A hiker is at -86 m. She climbs 120 m. She ends 34 m above sea level.', key=True),
          tf('Three stock prices change by -$2.50, +$4, and -$3.25. The total change is +$1.75.', key=False, note='The total change is -$1.75.'),
      ],
      back=[
          B('Multiply and divide decimals in word problems', '6.NS.B.3', [
              sa('Gas costs $3.85 per gallon.\nHow much do 12 gallons cost?', 'Cost:', key='$46.20'),
              sa('A 7.5-meter rope is cut into 3 equal pieces.\nHow long is each piece?', 'Length:', key='2.5 m'),
              mc('A 4.8-liter jug fills cups that hold 0.3 liter each.\nHow many cups can it fill?', ['16', '1.6', '160', '14.4']),
              tf('A 2.5-pound bag of nuts costs $3.20 per pound. The bag costs $8.', key=True),
              tf('$9.60 shared equally by 4 people is $2.60 each.', key=False, note='Each gets $2.40.'),
          ]),
          B('Solve one-step equations', '6.EE.B.7', [
              sa('Solve for x.\nx + 4.5 = 12', 'x =', key='7.5'),
              sa('Solve for y.\n6y = 39', 'y =', key='6.5'),
              mc('Solve for n.\n{2/3}n = 10', ['n = 15', 'n = {20/3}', 'n = 30', 'n = 9{1/3}']),
              tf('m = 8 is the solution of m - 2.75 = 5.25.', key=True),
              tf('k = 3 is the solution of 4k = 1.2.', key=False, note='The solution is k = 0.3.'),
          ]),
      ],
      f1=B('Solve real-world problems with scientific notation', '8.EE.A.4', [
          sa('A hard drive holds 2 × 10¹² bytes. A file is 4 × 10⁸ bytes.\nHow many files of this size fit on the drive?', 'Files:', key='5,000', note='5 × 10³ is also correct.'),
          sa('Earth is about 1.5 × 10⁸ km from the Sun. Mars is about 2.3 × 10⁸ km from the Sun.\nAbout how much farther from the Sun is Mars? Write the answer in scientific notation.', 'Distance:', key='8 × 10⁷ km'),
          mc('A cell is 2 × 10⁻⁵ m wide.\nHow wide are 3,000 of these cells placed side by side?', ['6 × 10⁻² m', '6 × 10⁻⁸ m', '6 × 10² m', '5 × 10⁻² m']),
          tf('(6 × 10⁴) × 5 = 3 × 10⁵', key=True),
          tf('(9 × 10⁶) ÷ (3 × 10²) = 3 × 10³', key=False, note='The quotient is 3 × 10⁴.'),
      ]),
      f2=B('Use units to solve multistep problems', 'HSN-Q.A.1', [
          sa('A car uses 0.04 gallon of gas per mile. Gas costs $3.50 per gallon.\nHow much does the gas cost for a 250-mile trip?', 'Cost:', key='$35'),
          sa('A faucet leaks 0.2 liter per hour.\nHow many liters leak in 1 week?', 'Liters:', key='33.6'),
          mc('A worker earns $18.50 per hour. She works 7.5 hours per day for 4 days.\nHow much does she earn?', ['$555', '$138.75', '$74', '$540']),
          tf('A speed of 12 meters per second is 43.2 kilometers per hour.', key=True),
          tf('Walking 3 miles per hour for 45 minutes covers 2.5 miles.', key=False, note='It covers 2.25 miles.'),
      ])),
]
