"""G-GPE: expressing geometric properties with equations (sets 64-74)."""
import math

from qb import S, B, sa, mc, tf, work
from common import gd, grid_fig, NTS, proof


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


PR = 'Any valid proof (paragraph, two-column, or flow). '
CPR = 'Any valid coordinate proof. '


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def d2(x):
    return '%.2f' % round(x + 1e-12, 2)


DERIVE = grid_fig({'C': (2, 1), 'P': (5, 5), 'Q': (5, 1)},
                  [('seg', 'C', 'P', {'label': 'r'}), ('seg', 'C', 'Q', {'dash': True}), ('seg', 'Q', 'P', {'dash': True}), ('ra', 'Q', 'C', 'P')],
                  lo=-1, hi=7, lab={'C': 'nw', 'P': 'ne', 'Q': 'se'},
                  desc='Coordinate grid from -1 to 7. Center C(2, 1) and point P(5, 5) on a circle of radius r are joined by segment CP labeled r. '
                       'Dashed horizontal segment CQ and dashed vertical segment QP meet at Q(5, 1) with a right angle at Q.')
RHOMBUS = grid_fig({'A': (0, 0), 'B': (4, 1), 'C': (5, 5), 'D': (1, 4)}, [('poly', ['A', 'B', 'C', 'D'])], lo=-1, hi=6,
                   lab={'A': 'sw', 'B': 'se', 'C': 'ne', 'D': 'nw'},
                   desc='Coordinate grid from -1 to 6 with quadrilateral ABCD: A(0, 0), B(4, 1), C(5, 5), D(1, 4).')

SETS = [
    # ------------------------------------------------------------------ 64. GPE.A.1 derive the circle equation
    S('HSG-GPE.A.1', 'Derive the equation of a circle',
      target='Derive the equation of a circle with given center and radius using the Pythagorean Theorem, and write the equation of a circle from given information',
      strand='core', covers=['GPE1-derive'],
      main=[
          proof('A circle has center (h, k) and radius r. Use the Pythagorean Theorem to derive the equation satisfied by every point (x, y) on the circle. '
                'The diagram shows one example, with center C(2, 1).', fig=DERIVE,
                method='Draw the right triangle with legs |x - h| and |y - k| and hypotenuse r.', key='(x - h)² + (y - k)² = r²',
                note=PR + 'Essential: a right triangle with horizontal leg |x - h|, vertical leg |y - k|, hypotenuse r (the distance CP); the Pythagorean Theorem gives '
                          '(x - h)² + (y - k)² = r²; squaring removes the absolute values; the reasoning holds for every point on the circle (degenerate legs of length 0 included). '
                          'Invalid: only checking the one example point.'),
          proof('Use the Pythagorean Theorem (not a memorized formula) to derive the equation of the circle with center (3, -2) and radius 5. Show the right triangle for a general point (x, y) on the circle.',
                method='Use legs |x - 3| and |y + 2| and hypotenuse 5.', key='(x - 3)² + (y + 2)² = 25',
                note=PR + 'Essential: horizontal leg |x - 3|, vertical leg |y - (-2)| = |y + 2|, hypotenuse 5; (x - 3)² + (y + 2)² = 25 for every point on the circle. Invalid: writing the formula with no triangle.'),
          proof('A circle is centered at the origin and passes through (6, -8). Use the Pythagorean Theorem (not a memorized formula) to derive its equation, first finding the radius.',
                method='Find the radius as a hypotenuse, then use legs |x| and |y| for a general point.', key='r = 10; x² + y² = 100',
                note=PR + 'Essential: r² = 6² + 8² = 100; for a general point the legs are |x| and |y|, so x² + y² = 100.'),
          proof('A circle has center (-1, 4) and passes through (2, 8). Use the Pythagorean Theorem (not a memorized formula) to derive its equation.',
                method='Find r from the right triangle with legs 3 and 4, then write the relationship for a general point (x, y).', key='(x + 1)² + (y - 4)² = 25',
                note=PR + 'Essential: legs 3 and 4 give r = 5; general legs |x + 1| and |y - 4|; (x + 1)² + (y - 4)² = 25.'),
          proof('Use the Pythagorean Theorem (not a memorized formula) to derive the equation of the circle with center (-2, 5) and radius 3. Then use your equation to decide whether (-2, 8) is on the circle.',
                method='Use legs |x + 2| and |y - 5| and hypotenuse 3; substitute the point.', key='(x + 2)² + (y - 5)² = 9; (-2, 8) is on it (0 + 9 = 9).',
                note=PR + 'Essential: the right-triangle relationship with signs handled (x - (-2) = x + 2); r² = 9, not 3; the check.'),
      ],
      back=[
          B('Distance between two points with the Pythagorean Theorem', '8.G.B.8', [
              sa('Find the distance between (1, 2) and (4, 6).', 'Distance:', key='5', note='Any equivalent form. Legs 3 and 4.'),
              sa('Find the distance between (0, 0) and (5, 12).', 'Distance:', key='13', note='Any equivalent form.'),
              mc('The legs of the right triangle joining (2, 1) and (7, 13) are', ['5 and 12', '7 and 13', '9 and 14', '2 and 1'], note='Differences of coordinates.'),
              tf('The distance from (-3, 0) to (3, 0) is 6.', key=True, note='Horizontal distance.'),
              tf('The distance from (0, 0) to (3, 4) is 7.', key=False, note='It is 5; the legs are not added.'),
          ], align='exact',
            why=why('the student cannot find distances on the plane.', 'the radius is the distance from the center to a point.', 'finds distances with the Pythagorean Theorem.')),
          B('Use the Pythagorean Theorem with expressions', '8.G.B.7', [
              sa('A right triangle has legs 6 and 8. Find the hypotenuse.', 'Hypotenuse:', key='10', note='Any equivalent form.'),
              sa('A right triangle has legs a and b and hypotenuse c. Write the Pythagorean relationship.', 'Equation:', key='a² + b² = c²', note='Any equivalent form.'),
              mc('A right triangle has legs (x - 2) and (y - 1) and hypotenuse 4. Which equation is true?', ['(x - 2)² + (y - 1)² = 16', '(x - 2) + (y - 1) = 4', '(x - 2)² + (y - 1)² = 4', 'x² + y² = 16'],
                 note='Square the legs and the hypotenuse.'),
              tf('In a right triangle, the hypotenuse is opposite the right angle.', key=True, note='Definition.'),
              tf('a² + b² = c² holds for every triangle.', key=False, note='Only right triangles.'),
          ], align='exact',
            why=why('the student cannot write the Pythagorean relationship with variable legs.', 'the derivation uses legs x - h and y - k.', 'writes the theorem with expressions.')),
          B('Shifting a graph: reading h and k', 'HSF-BF.B.3', [
              sa('The graph of y = (x - 3)² is the graph of y = x² shifted in which direction and by how much?', 'Answer:', key='Right 3', note='Any equivalent answer.'),
              sa('Write x - (-4) without the double sign.', 'Answer:', key='x + 4', note='Any equivalent form.'),
              mc('In (x + 2)², the shift is', ['2 left', '2 right', '2 up', '2 down'], note='x - (-2).'),
              tf('Replacing x with x - 5 shifts a graph 5 units right.', key=True, note='Horizontal translation.'),
              tf('Replacing y with y + 1 shifts a graph 1 unit up.', key=False, note='It shifts it 1 unit down.'),
          ], align='supporting',
            why=why('the student reverses the signs of the center.', 'the center (h, k) appears as x - h and y - k.', 'reads shifts correctly.')),
      ],
      f1=B('Write circle equations from other given information', 'HSG-GPE.A.1', [
          sa('A diameter of a circle has endpoints (-2, 3) and (6, -3). Write the equation of the circle.', 'Equation:', key='(x - 2)² + y² = 25',
             note='Form required: an equation. Center (2, 0) is the midpoint; radius 5 (half of 10).'),
          sa('A circle has center (4, -3) and is tangent to the x-axis. Write its equation.', 'Equation:', key='(x - 4)² + (y + 3)² = 9', note='Form required: an equation. Radius = distance to the x-axis = 3.'),
          tf('The circle (x - 1)² + (y - 1)² = 2 passes through the origin.', key=True, note='1 + 1 = 2.'),
          mc('A circle with center (0, 5) passes through (0, -1). Its radius is', ['6', '4', '36', '5'], note='Vertical distance.'),
          sa('A circle is centered at (3, 3) and is tangent to both axes. Write its equation.', 'Equation:', key='(x - 3)² + (y - 3)² = 9', note='Form required: an equation.'),
      ], prog='same-course deepening', demand='Use the derived equation when the radius or center must first be found (diameter endpoints, tangency).'),
      f2=B('Prove or disprove that points lie on a circle', 'HSG-GPE.B.4', [
          sa('Does (-4, 6) lie on the circle with center (2, -2) passing through (8, 6)? Show the check.', 'Answer:', key='Yes: both points are 10 from the center (36 + 64 = 100).',
             note='Form required: the conclusion with the distance check.'),
          sa('Is (7, 1) inside, on, or outside the circle (x - 3)² + (y + 2)² = 25?', 'Answer:', key='On (16 + 9 = 25)', note='Form required: the conclusion with the check.'),
          tf('A point is inside a circle when its distance from the center is greater than the radius.', key=False, note='Greater than the radius means outside.'),
          mc('The point (1, 1) is ___ the circle x² + y² = 4.', ['inside', 'on', 'outside', 'the center of'], note='1 + 1 = 2 < 4.'),
          sa('A circle has the diameter with endpoints (-2, 3) and (6, -3). Does (5, 4) lie on it?', 'Answer:', key='Yes: (5 - 2)² + 4² = 25.', note='Form required: the conclusion with the check.'),
      ], prog='cross-standard extension', demand='Use the circle equation as a test in a coordinate proof.',
        builds='Builds on FORWARD 1: circles found from diameters and tangency are tested against given points.')),

    # ------------------------------------------------------------------ 65. GPE.A.1 complete the square
    S('HSG-GPE.A.1', 'Complete the square to find the center and radius of a circle',
      target='Complete the square to find the center and radius of a circle given by an equation in general form', strand='core', covers=['GPE1-complete'],
      main=[
          sa('Complete the square to find the center and radius of the circle x² + y² - 6x + 4y - 12 = 0. Show the standard form.', 'Answer:', key='(x - 3)² + (y + 2)² = 25; center (3, -2); radius 5', note='Form required: both. (x - 3)² + (y + 2)² = 25.'),
          sa('Complete the square to find the center and radius of the circle x² + y² + 8x - 10y + 5 = 0. Show the standard form.', 'Answer:', key='(x + 4)² + (y - 5)² = 36; center (-4, 5); radius 6', note='Form required: both. (x + 4)² + (y - 5)² = -5 + 16 + 25 = 36.'),
          work('Complete the square to write x² + y² - 2x - 14y + 25 = 0 in standard form. Then give the center and radius.', 'Answer:',
               method='Group x and y terms, add (b/2)² for each to both sides, and factor.', key='(x - 1)² + (y - 7)² = 25; center (1, 7); radius 5',
               note='Form required: the standard form, center, and radius. Added 1 and 49 to both sides: -25 + 1 + 49 = 25.'),
          sa('Complete the square to find the center and radius of the circle x² + y² + 10y = 0. Show the standard form.', 'Answer:', key='x² + (y + 5)² = 25; center (0, -5); radius 5', note='Form required: both. x² + (y + 5)² = 25.'),
          work('Complete the square to write x² + y² - 4x + 6y = 3 in standard form. Then give the center and radius.', 'Answer:',
               method='Group x and y terms, add (b/2)² for each to both sides, and factor.', key='(x - 2)² + (y + 3)² = 16; center (2, -3); radius 4',
               note='Form required: the standard form, center, and radius. Added 4 and 9 to both sides: 3 + 4 + 9 = 16.'),
      ],
      back=[
          B('Complete the square in one variable', 'HSA-REI.B.4.a', [
              sa('What number completes the square: x² - 6x + ___?', 'Answer:', key='9', note='Any equivalent form. (6/2)².'),
              sa('Write x² + 10x + 25 as a square.', 'Answer:', key='(x + 5)²', note='Any equivalent form.'),
              mc('x² - 8x + 16 equals', ['(x - 4)²', '(x - 8)²', '(x + 4)²', '(x - 16)²'], note='Half of 8 is 4.'),
              tf('To complete x² + bx, add (b/2)².', key=True, note='Rule.'),
              tf('x² + 6x + 6 is a perfect square.', key=False, note='It needs + 9.'),
          ], align='exact',
            why=why('the student cannot complete the square.', 'it is the main step.', 'completes squares in one variable.')),
          B('Square a binomial', 'HSA-APR.A.1', [
              sa('Expand (x - 3)².', 'Answer:', key='x² - 6x + 9', note='Any equivalent form.'),
              sa('Expand (y + 2)².', 'Answer:', key='y² + 4y + 4', note='Any equivalent form.'),
              mc('(x + 5)² =', ['x² + 10x + 25', 'x² + 25', 'x² + 5x + 25', 'x² + 10x + 10'], note='Middle term 2 · 5x.'),
              tf('(a - b)² = a² - 2ab + b²', key=True, note='Identity.'),
              tf('(x - 3)² = x² - 9', key=False, note='Missing the middle term.'),
          ], align='exact',
            why=why('the student does not see why the added number makes a square.', 'checking the completed square needs expansion.', 'expands binomial squares.')),
          B('Keep an equation balanced', 'HSA-REI.A.1', [
              sa('If 9 is added to the left side of an equation, what must be done to the right side?', 'Answer:', key='Add 9', note='Any equivalent answer.'),
              sa('x² - 6x = 7. Add 9 to both sides and factor.', 'Answer:', key='(x - 3)² = 16', note='Any equivalent form.'),
              mc('x² + y² - 4x = 5 becomes (x - 2)² + y² =', ['9', '5', '1', '4'], note='5 + 4.'),
              tf('Adding the same number to both sides keeps the solutions the same.', key=True, note='Equality property.'),
              tf('A number added to one side need not be added to the other.', key=False, note='That changes the equation.'),
          ], align='supporting',
            why=why('the student adds to one side only and gets the wrong radius.', 'r² comes from the balanced right side.', 'keeps equations balanced.')),
      ],
      f1=B('Leading coefficients and equations that are not circles', 'HSG-GPE.A.1', [
          sa('Find the center and radius of 2x² + 2y² - 8x + 12y - 6 = 0.', 'Answer:', key='Center (2, -3); radius 4', note='Form required: both. Divide by 2 first.'),
          sa('Does x² + y² + 2x + 4y + 10 = 0 represent a circle? Explain.', 'Answer:', key='No: it becomes (x + 1)² + (y + 2)² = -5, and a sum of squares cannot be negative.',
             note='Form required: the conclusion with the reason.'),
          tf('x² + y² - 6x + 9 = 0 represents a single point.', key=True, note='(x - 3)² + y² = 0: only (3, 0).'),
          mc('3x² + 3y² - 12y = 0 has radius', ['2', '4', '12', '√12'], note='x² + (y - 2)² = 4.'),
          sa('For what values of c is x² + y² - 4x + c = 0 a circle?', 'Answer:', key='c < 4', note='Form required: an inequality. r² = 4 - c > 0.'),
      ], prog='same-course deepening', demand='Handle leading coefficients and decide when an equation is not a circle.'),
      f2=B('Complete the square for an ellipse', 'HSG-GPE.A.3', [
          sa('Write 4x² + 9y² - 16x + 18y - 11 = 0 in standard form and give the center.', 'Answer:', key='(x - 2)²/9 + (y + 1)²/4 = 1; center (2, -1)',
             note='Form required: both. 4(x - 2)² + 9(y + 1)² = 11 + 16 + 9 = 36.'),
          sa('Find the center of x² + 4y² + 6x - 8y + 9 = 0.', 'Center:', key='(-3, 1)', note='Form required: an ordered pair. (x + 3)² + 4(y - 1)² = 4.'),
          tf('After factoring 4 out of 4x² - 16x, add 16 inside the parentheses to complete the square.', key=False, note='Add 4 inside: 4(x² - 4x + 4), which adds 16 to the expression.'),
          mc('Which is NOT a circle?', ['x² + 4y² = 4', 'x² + y² = 4', '2x² + 2y² = 8', '(x - 1)² + y² = 4'], note='Unequal coefficients give an ellipse.'),
          sa('Explain why x² + 4y² = 4 is not a circle.', 'Answer:', key='The x² and y² coefficients differ, so the "radius" differs by direction (2 across, 1 up).', note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Use completing the square on a conic whose squared terms have different coefficients (advanced strand).',
        builds='Builds on FORWARD 1: factoring out leading coefficients is the key step for ellipses.')),

    # ------------------------------------------------------------------ 66. GPE.A.2 parabola
    S('HSG-GPE.A.2', 'Derive the equation of a parabola from a focus and directrix',
      target='Derive the equation of a parabola given its focus and directrix', strand='core', covers=['GPE2-parabola'],
      main=[
          proof('Derive the equation of the parabola with focus (0, 2) and directrix y = -2.', method='Set the distance from (x, y) to the focus equal to its distance to the directrix, square, and simplify.',
                key='x² = 8y (y = x²/8)', note=PR + 'Essential: √(x² + (y - 2)²) = |y + 2|; square: x² + y² - 4y + 4 = y² + 4y + 4; simplify to x² = 8y.'),
          proof('Derive, from the definition (equal distances to the focus and the directrix), the equation of the parabola with focus (0, -3) and directrix y = 3.', method='Set √(x² + (y + 3)²) = |y - 3|, square, and simplify.', key='x² = -12y',
                note=PR + 'Essential: x² + y² + 6y + 9 = y² - 6y + 9; x² = -12y. Invalid: quoting x² = 4py without the distance equation.'),
          proof('Derive, from the definition (equal distances to the focus and the directrix), the equation of the parabola with focus (2, 5) and directrix y = 1.', method='Set √((x - 2)² + (y - 5)²) = |y - 1|, square, and simplify.', key='(x - 2)² = 8(y - 3)',
                note=PR + 'Essential: (x - 2)² + y² - 10y + 25 = y² - 2y + 1; (x - 2)² = 8y - 24 = 8(y - 3).'),
          proof('Derive, from the definition (equal distances to the focus and the directrix), the equation of the parabola with focus (3, 0) and directrix x = -3.', method='Set √((x - 3)² + y²) = |x + 3|, square, and simplify.', key='y² = 12x',
                note=PR + 'Essential: x² - 6x + 9 + y² = x² + 6x + 9; y² = 12x.'),
          proof('Derive, from the definition (equal distances to the focus and the directrix), the equation of the parabola with focus (1, 4) and directrix y = 0 (the x-axis). Then give its vertex.', method='Set √((x - 1)² + (y - 4)²) = |y|, square, simplify, and read the vertex.',
                key='(x - 1)² = 8(y - 2); vertex (1, 2)',
                note=PR + 'Essential: (x - 1)² + y² - 8y + 16 = y²; (x - 1)² = 8y - 16 = 8(y - 2); the vertex (1, 2) is midway between the focus and the directrix.'),
      ],
      back=[
          B('Distance between two points', '8.G.B.8', [
              sa('Find the distance from (3, 6) to (0, 2).', 'Distance:', key='5', note='Any equivalent form.'),
              sa('Write the distance from (x, y) to (0, 2) as an expression.', 'Expression:', key='√(x² + (y - 2)²)', note='Any equivalent form.'),
              mc('The distance from (4, 1) to (1, 5) is', ['5', '7', '25', '√7'], note='Legs 3 and 4.'),
              tf('The distance formula comes from the Pythagorean Theorem.', key=True, note='Legs are coordinate differences.'),
              tf('√(9 + 16) = 3 + 4', key=False, note='√25 = 5.'),
          ], align='exact',
            why=why('the student cannot write the distance to the focus.', 'one side of the defining equation is that distance.', 'writes the distance expression.')),
          B('Distance from a point to a horizontal line', '6.NS.C.8', [
              sa('How far is (5, 7) from the line y = 2?', 'Distance:', key='5', note='Any equivalent form.'),
              sa('How far is (1, -3) from the line y = 4?', 'Distance:', key='7', note='Any equivalent form.'),
              mc('The distance from (x, y) to y = -2 is', ['|y + 2|', '|y - 2|', '|x + 2|', 'y'], note='Vertical difference.'),
              tf('The distance from a point to a horizontal line is measured straight up or down.', key=True, note='Perpendicular.'),
              tf('The distance from (6, 1) to y = 4 is 6.', key=False, note='It is 3.'),
          ], align='exact',
            why=why('the student cannot write the distance to the directrix.', 'the other side of the defining equation is that distance.', 'finds vertical distances.')),
          B('Points equidistant from two objects', 'HSG-CO.C.9', [
              tf('The set of points equidistant from two points is the perpendicular bisector of the segment joining them.', key=True, note='Theorem.'),
              sa('A parabola is the set of points equidistant from what two objects?', 'Answer:', key='A point (the focus) and a line (the directrix)', note='Any equivalent answer.'),
              mc('The vertex of a parabola is', ['halfway between the focus and the directrix', 'at the focus', 'on the directrix', 'twice as far from the focus'], note='Equidistant.'),
              sa('Focus (0, 6), directrix y = 0. Find the vertex.', 'Vertex:', key='(0, 3)', note='Form required: an ordered pair.'),
              tf('Every point of a parabola is closer to the focus than to the directrix.', key=False, note='Equal distances.'),
          ], align='supporting',
            why=why('the student does not know the definition.', 'the equation encodes equal distances.', 'states and uses the definition.')),
          B('Expand and simplify squares', 'HSA-APR.A.1', [
              sa('Expand (y - 2)².', 'Answer:', key='y² - 4y + 4', note='Any equivalent form.'),
              sa('Simplify (y + 2)² - (y - 2)².', 'Answer:', key='8y', note='Any equivalent form.'),
              mc('y² + 6y + 9 - (y² - 6y + 9) =', ['12y', '0', '18', '2y²'], note='The squares cancel.'),
              tf('(y + 3)² = y² + 6y + 9', key=True, note='Identity.'),
              tf('(y - 2)² - y² = 4', key=False, note='-4y + 4.'),
          ], align='supporting',
            why=why('the student cannot simplify after squaring.', 'the y² terms must cancel.', 'expands and simplifies.')),
      ],
      f1=B('Find the focus and directrix from an equation', 'HSG-GPE.A.2', [
          sa('Find the focus and directrix of y = x²/12.', 'Answer:', key='Focus (0, 3); directrix y = -3', note='Form required: both. x² = 12y = 4py, p = 3.'),
          sa('Find the vertex, focus, and directrix of (x - 1)² = -8(y + 2).', 'Answer:', key='Vertex (1, -2); focus (1, -4); directrix y = 0', note='Form required: all three. p = -2.'),
          tf('In x² = 4py (p ≠ 0), the focus is |p| units from the vertex.', key=True, note='The focus is (0, p); its distance from the vertex (0, 0) is |p|, since p may be negative.'),
          mc('The parabola y² = -20x opens', ['left', 'right', 'up', 'down'], note='Negative coefficient with y².'),
          sa('Find the focus of y = 2x².', 'Focus:', key='(0, ⅛)', note='Form required: an ordered pair. x² = ½y, 4p = ½.'),
      ], prog='same-course deepening', demand='Reverse the derivation: read the focus and directrix from an equation.'),
      f2=B('Design with the reflective property of parabolas', 'HSG-MG.A.3', [
          sa('A satellite dish is 4 ft across and 1 ft deep. How far from the vertex should the receiver (at the focus) be placed?', 'Distance:', key='1 ft',
             note='Any equivalent form. x² = 4py through (2, 1): 4 = 4p.'),
          sa('A headlight reflector has equation x² = 12y (inches). Where should the bulb go?', 'Answer:', key='3 in. above the vertex, at (0, 3)', note='Any equivalent answer.'),
          tf('Rays parallel to the axis of a parabolic mirror reflect through the vertex.', key=False, note='They reflect through the focus.'),
          mc('A dish has focus 2 m above its vertex. Its equation (vertex at the origin) is', ['x² = 8y', 'x² = 2y', 'y = 8x²', 'x² = 4y'], note='4p = 8.'),
          sa('A dish has equation x² = 16y (meters) and is 8 m across. How deep is it?', 'Depth:', key='1 m', note='Any equivalent form. 16 = 16y at x = 4.'),
      ], prog='cross-standard extension', demand='Apply the focus to a design problem (placing a receiver or bulb).',
        builds='Builds on FORWARD 1: reading the focus from an equation locates the receiver.')),
]

RECT = grid_fig({'P': (-2, -1), 'Q': (2, 1), 'R': (1, 3), 'S': (-3, 1)}, [('poly', ['P', 'Q', 'R', 'S'])], lo=-4, hi=4,
                lab={'P': 's', 'Q': 'e', 'R': 'n', 'S': 'w'},
                desc='Coordinate grid from -4 to 4 with quadrilateral PQRS: P(-2, -1), Q(2, 1), R(1, 3), S(-3, 1).')
SLOPE_ROT = grid_fig({'O': (0, 0), 'A': (3, 2), 'A\'': (-2, 3)}, [('seg', 'O', 'A'), ('seg', 'O', 'A\''), ('seg', 'O', (3, 0), {'dash': True}), ('seg', (3, 0), 'A', {'dash': True}),
                                                               ('seg', 'O', (0, 3), {'dash': True}), ('seg', (0, 3), 'A\'', {'dash': True}), ('ra', 'O', 'A', 'A\'')],
                     lo=-4, hi=4, lab={'O': 'sw', 'A': 'ne', "A'": 'nw'},
                     desc="Coordinate grid from -4 to 4. Segment OA from the origin to A(3, 2) with dashed slope triangle (run 3, rise 2). Segment OA' to A'(-2, 3), the image of A under a 90° counterclockwise rotation about O, "
                          "with dashed slope triangle (run -2, rise 3). A right angle is marked at O between OA and OA'.")

SETS += [
    # ------------------------------------------------------------------ 67. GPE.B.4 quadrilateral proofs
    S('HSG-GPE.B.4', 'Prove or disprove the type of a quadrilateral with coordinates',
      target='Use slopes and distances to prove or disprove that a quadrilateral or triangle defined by coordinates has a given type', strand='core', covers=['GPE4-quad'],
      main=[
          proof('Prove that ABCD with A(0, 0), B(4, 1), C(5, 5), D(1, 4) is a rhombus.', fig=RHOMBUS, method='Compute all four side lengths with the distance formula.',
                key='AB = BC = CD = DA = √17, so ABCD is a rhombus.', note=CPR + 'Essential: all four distances computed correctly (√17 each) and the definition of a rhombus cited. '
                                                                          'Alternative: show it is a parallelogram (slopes) with perpendicular diagonals (slopes 1 and -1). Invalid: "it looks like a rhombus".'),
          proof('Prove that PQRS with P(-2, -1), Q(2, 1), R(1, 3), S(-3, 1) is a rectangle. Is it a square?', fig=RECT, method='Compute the slopes of all four sides; compare adjacent slopes.',
                key='Slopes PQ = RS = ½ and QR = SP = -2; adjacent products are -1, so all angles are right: a rectangle. Not a square: PQ = √20 but QR = √5.',
                note=CPR + 'Essential: four slopes; opposite sides parallel; adjacent slopes multiply to -1 (right angles); side lengths √20 ≠ √5 for "not a square".'),
          proof('Prove or disprove: KLMN with K(0, 0), L(5, 0), M(6, 3), N(0, 3) is a parallelogram.', method='Compare the slopes of both pairs of opposite sides.',
                key='Disproved: KL ∥ MN (slope 0), but LM has slope 3 while NK is vertical, so LM ∦ NK. KLMN is a trapezoid, not a parallelogram.',
                note=CPR + 'Essential: one pair of opposite sides shown NOT parallel (a single counterexample disproves). Alternative: KL = 5 but MN = 6.'),
          proof('Prove that the triangle with vertices A(1, 1), B(4, 5), C(8, 2) is an isosceles right triangle.', method='Use distances for the equal sides and slopes (or the converse of the Pythagorean Theorem) for the right angle.',
                key='AB = BC = 5 and AC = √50; 5² + 5² = 50, so ∠B is right. Isosceles right triangle.',
                note=CPR + 'Essential: three distances; two equal (isosceles); right angle at B by the converse of the Pythagorean Theorem or slopes 4/3 and -3/4.'),
          proof('Prove or disprove: EFGH with E(-1, 0), F(2, -1), G(3, 2), H(0, 3) is a square.', method='Show four equal sides and one right angle (or a rhombus with a right angle).',
                key='Proved: all sides are √10; slopes EF = -⅓ and FG = 3 multiply to -1, so ∠F is right. A rhombus with a right angle is a square.',
                note=CPR + 'Essential: four lengths √10; opposite slopes equal (-⅓ and 3); a right angle; conclusion.'),
      ],
      back=[
          B('Find the slope between two points', '8.F.B.4', [
              sa('Find the slope of the line through (1, 2) and (5, 4).', 'Slope:', key='½', note='Any equivalent form.'),
              sa('Find the slope of the line through (0, 3) and (2, -1).', 'Slope:', key='-2', note='Any equivalent form.'),
              mc('The slope through (2, 5) and (6, 5) is', ['0', 'undefined', '5', '4'], note='Horizontal.'),
              tf('A vertical segment has an undefined slope.', key=True, note='Run 0.'),
              tf('Slope is run divided by rise.', key=False, note='Rise ÷ run.'),
          ], align='exact',
            why=why('the student cannot find slopes.', 'parallel and perpendicular sides are decided by slopes.', 'computes slopes.')),
          B('Find the distance between two points', '8.G.B.8', [
              sa('Find the distance between (0, 0) and (4, 1).', 'Distance:', key='√17', note='Form required: exact value.'),
              sa('Find the distance between (1, 1) and (4, 5).', 'Distance:', key='5', note='Any equivalent form.'),
              mc('Which pair of points is 10 apart?', ['(0, 0) and (6, 8)', '(0, 0) and (10, 10)', '(1, 1) and (5, 7)', '(2, 3) and (8, 3)'], note='36 + 64 = 100.'),
              tf('Two segments with the same length are congruent.', key=True, note='Definition.'),
              tf('√10 + √10 = √20', key=False, note='√10 + √10 = 2√10 = √40.'),
          ], align='exact',
            why=why('the student cannot compare side lengths.', 'rhombus and square proofs compare lengths.', 'computes distances.')),
          B('Properties that define special quadrilaterals', 'HSG-CO.C.11', [
              sa('Which quadrilateral has four congruent sides?', 'Answer:', key='A rhombus (a square is a special rhombus)', note='Any equivalent answer.'),
              sa('A parallelogram with one right angle is a ___.', 'Answer:', key='Rectangle', note='Any equivalent answer.'),
              mc('Which shows a quadrilateral is a parallelogram?', ['Both pairs of opposite sides are parallel', 'One pair of sides is parallel', 'Two adjacent sides are equal', 'One right angle'],
                 note='Definition.'),
              tf('Every square is a rhombus.', key=True, note='Four congruent sides.'),
              tf('Every rhombus is a square.', key=False, note='Its angles need not be right.'),
          ], align='exact',
            why=why('the student does not know what must be shown.', 'the proof checks the defining property.', 'states the needed properties.')),
      ],
      f1=B('Coordinate proofs with variables', 'HSG-GPE.B.4', [
          proof('A rectangle has vertices O(0, 0), A(a, 0), B(a, b), C(0, b). Prove that its diagonals are congruent.', method='Compute OB and AC with the distance formula.',
                key='OB = AC = √(a² + b²)', note=CPR + 'Essential: OB = √(a² + b²), AC = √((0 - a)² + (b - 0)²) = √(a² + b²); equal for all a, b. Invalid: using numbers for a and b.'),
          proof('Triangle with vertices O(0, 0), A(2a, 0), B(2b, 2c), where a > 0 and c ≠ 0 (so the points are not collinear). M and N are the midpoints of OB and AB. Prove that MN ∥ OA and MN = ½OA.', method='Find M and N, then compare slope and length.',
                key='M(b, c), N(a + b, c); MN is horizontal like OA, and MN = a = ½(2a).', note=CPR + 'Essential: correct midpoints; slope 0 for both; length a vs 2a.'),
          tf('Placing a figure with a vertex at the origin and a side on the x-axis is allowed in a coordinate proof.', key=True, note='Any figure can be moved there by a rigid motion.'),
          mc('Why do coordinates like (2a, 0) and (2b, 2c) make the midpoint proof easier?', ['The midpoints have no fractions', 'They make the triangle isosceles', 'They make a right angle', 'They make the slopes 0'],
             note='Halves of even coordinates.'),
          sa('Why is a proof using A(6, 0) and B(2, 4) not enough to prove the midsegment theorem?', 'Answer:', key='It shows only one triangle; the theorem is about all triangles.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Prove general theorems with variable coordinates instead of checking one example.'),
      f2=B('Use the classification to find area', 'HSG-GPE.B.7', [
          sa('ABCD with A(0, 0), B(4, 1), C(5, 5), D(1, 4) is a rhombus. Find its area using its diagonals.', 'Area:', key='15', note='Any equivalent form. AC = 5√2, BD = 3√2; ½ · 5√2 · 3√2.'),
          sa('Rectangle PQRS has P(-2, -1), Q(2, 1), R(1, 3), S(-3, 1). Find its area.', 'Area:', key='10', note='Any equivalent form. √20 · √5.'),
          tf('Once a quadrilateral is proved a rhombus, its area is the product of two adjacent side lengths.', key=False, note='Only for a square; use ½d₁d₂ or base × height.'),
          mc('A square has vertices (0, 0), (3, 1), (2, 4), (-1, 3). Its area is', ['10', '√10', '9', '16'], note='Side √10.'),
          sa('Explain why proving the shape first matters before using a special area formula.', 'Answer:', key='The formula (such as ½d₁d₂ or length × width) is valid only for that type of figure.',
             note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Use the proved type to choose and apply an area formula.',
        builds='Builds on FORWARD 1: after proving the type (with numbers or variables), its properties give the area.')),

    # ------------------------------------------------------------------ 68. GPE.B.4 circles and other coordinate proofs
    S('HSG-GPE.B.4', 'Prove or disprove that a point lies on a circle, and other coordinate proofs',
      target='Use coordinates to prove or disprove statements about points on circles and equal distances', strand='core', covers=['GPE4-circle'],
      main=[
          proof('A circle is centered at (2, -1) and contains the point (2, 4). Prove or disprove that the point (5, 3) lies on the circle.',
                method='Find the radius, then compare the distance from the center to (5, 3).', key='Proved: the radius is 5 and the distance from (2, -1) to (5, 3) is √(9 + 16) = 5.',
                note=CPR + 'Essential: radius |4 - (-1)| = 5; distance √(3² + 4²) = 5; conclusion.'),
          proof('Prove or disprove that (5, 2) lies on the circle with center (1, -1) and radius 5.', method='Compare the distance from the center to the point with the radius.',
                key='Proved: (5 - 1)² + (2 + 1)² = 16 + 9 = 25 = 5².', note=CPR + 'Essential: the squared distance 25 computed from the coordinates; compared with r² = 25; conclusion.'),
          proof('Prove or disprove that (-3, 6) lies on the circle (x - 1)² + (y - 2)² = 30.', method='Substitute the point into the equation, or compare its distance from the center with √30.',
                key='Disproved: 16 + 16 = 32 ≠ 30 (the point is outside).', note=CPR + 'Essential: substitution giving 32; 32 ≠ 30; conclusion (outside, since 32 > 30).'),
          proof('Right triangle ABC has A(0, 0), B(8, 0), C(0, 6). Prove that the midpoint M of hypotenuse BC is equidistant from A, B, and C.', method='Find M, then compute MA, MB, MC.',
                key='M(4, 3); MA = MB = MC = 5', note=CPR + 'Essential: midpoint (4, 3); three distances of 5. Consequence: A, B, C lie on a circle centered at M.'),
          proof('Prove that the point (4, -3) lies outside the circle x² + y² = 20.', method='Compare the distance from the center to the point with the radius.',
                key='Distance 5 > √20 ≈ 4.47, so the point is outside.', note=CPR + 'Essential: center (0, 0), radius √20; distance √(16 + 9) = 5; 5 > √20 (25 > 20); conclusion.'),
      ],
      back=[
          B('Distance between two points', '8.G.B.8', [
              sa('Distance from (1, -1) to (5, 2)?', 'Distance:', key='5', note='Any equivalent form.'),
              sa('Distance from (2, -1) to (5, 3)?', 'Distance:', key='5', note='Any equivalent form.'),
              mc('Distance from (0, 0) to (-3, 4) is', ['5', '7', '1', '25'], note='9 + 16.'),
              tf('(-3)² = 9', key=True, note='Square of a negative.'),
              tf('The distance from (2, 2) to (2, 7) is 9.', key=False, note='It is 5.'),
          ], align='exact',
            why=why('the student cannot compute the distance to the center.', 'it decides whether the point is on the circle.', 'computes distances.')),
          B('The equation of a circle', 'HSG-GPE.A.1', [
              sa('Write the equation of the circle with center (1, -1) and radius 5.', 'Equation:', key='(x - 1)² + (y + 1)² = 25', note='Form required: an equation.'),
              sa('What is the radius of (x - 1)² + (y - 2)² = 30?', 'Radius:', key='√30', note='Form required: exact value.'),
              mc('Center of (x + 4)² + y² = 9?', ['(-4, 0)', '(4, 0)', '(0, -4)', '(-4, 9)'], note='Opposite sign.'),
              tf('A point satisfies a circle\'s equation exactly when it is on the circle.', key=True, note='Meaning of the equation.'),
              tf('The radius of x² + y² = 20 is 20.', key=False, note='√20.'),
          ], align='exact',
            why=why('the student cannot read the center and radius.', 'the proof compares with r.', 'reads circle equations.')),
          B('Substitute values into an expression', '6.EE.A.2', [
              sa('Evaluate (x - 1)² + (y - 2)² when x = -3 and y = 6.', 'Value:', key='32', note='Any equivalent form.'),
              sa('Evaluate x² + y² when x = 4, y = -3.', 'Value:', key='25', note='Any equivalent form.'),
              mc('(x + 1)² when x = -4 is', ['9', '-9', '25', '-3'], note='(-3)².'),
              tf('(-5 - 1)² = 36', key=True, note='(-6)².'),
              tf('(2 + 1)² = 2² + 1²', key=False, note='9 ≠ 5.'),
          ], align='supporting',
            why=why('the student makes sign errors substituting.', 'checks are substitutions.', 'evaluates correctly.')),
      ],
      f1=B('Coordinate proofs about circles with variables', 'HSG-GPE.B.4', [
          proof('A(-r, 0) and B(r, 0) are endpoints of a diameter of the circle x² + y² = r², and P(x, y) is any other point on the circle. Prove that ∠APB is a right angle.',
                method='Compute the slopes of PA and PB and use x² + y² = r².', key='slope PA · slope PB = y²/(x² - r²) = y²/(-y²) = -1, so PA ⊥ PB.',
                note=CPR + 'Essential: slopes y/(x + r) and y/(x - r); product y²/(x² - r²); substitute x² - r² = -y²; product -1. (P is not A or B, so y ≠ 0.)'),
          sa('Show that if (a, b) is on x² + y² = r², then (b, a) and (-a, b) are too.', 'Answer:', key='b² + a² = r² and (-a)² + b² = r², the same sum.', note='Any equivalent argument.'),
          tf('A coordinate proof with variables covers every case at once.', key=True, note='General.'),
          mc('To prove four points lie on one circle, show they are', ['all the same distance from one point', 'all on one line', 'vertices of a rectangle only', 'the same distance from the origin only'],
             note='Common center.'),
          sa('Prove or disprove: A(1, 0), B(0, 1), C(-1, 0), D(0, -2) lie on one circle centered at the origin.', 'Answer:', key='Disproved: D is 2 from the origin, the others 1.',
             note='Form required: the conclusion with distances.'),
      ], prog='same-course deepening', demand='Prove circle statements for every point using variables (Thales\' theorem by slopes).'),
      f2=B('Find the tangent line to a circle at a point', 'HSG-GPE.B.5', [
          sa('Find the equation of the line tangent to x² + y² = 25 at (3, 4).', 'Equation:', key='y = -¾x + 25/4', note='Form required: an equation; equivalent forms (3x + 4y = 25) accepted. Radius slope 4/3.'),
          sa('Find the tangent to (x - 1)² + (y - 1)² = 25 at (4, 5).', 'Equation:', key='y - 5 = -¾(x - 4)', note='Form required: an equation; equivalent forms accepted.'),
          tf('The tangent at P is parallel to the radius drawn to P.', key=False, note='It is perpendicular to that radius.'),
          mc('The radius to (0, 5) on x² + y² = 25 is vertical, so the tangent there is', ['y = 5', 'x = 0', 'y = x + 5', 'x = 5'], note='Horizontal.'),
          sa('Explain how the slope of the tangent at (a, b) on x² + y² = r² is found.', 'Answer:', key='The radius has slope b/a, so the tangent has slope -a/b (negative reciprocal), for a, b ≠ 0.',
             note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Combine the circle equation with the perpendicular slope criterion to write tangent lines.',
        builds='Builds on FORWARD 1: the slope products used there now give tangent lines.')),

    # ------------------------------------------------------------------ 69. GPE.B.5 prove slope criteria
    S('HSG-GPE.B.5', 'Prove the slope criteria for parallel and perpendicular lines',
      target='Prove that nonvertical lines are parallel exactly when their slopes are equal, and perpendicular exactly when the product of their slopes is -1', strand='core', covers=['GPE5-prove'],
      main=[
          proof('Prove that two distinct nonvertical lines with the same slope m are parallel.', method='Write the lines as y = mx + b₁ and y = mx + b₂ with b₁ ≠ b₂ and show there is no intersection.',
                key='mx + b₁ = mx + b₂ gives b₁ = b₂, a contradiction; so the lines never meet and are parallel.',
                note=PR + 'Essential: equations with equal slopes and different intercepts; solving for an intersection leads to b₁ = b₂ (false); conclusion. '
                          'Alternative: a translation maps one line to the other; or congruent slope triangles with corresponding angles equal.'),
          proof('Line OA passes through O(0, 0) and A(a, b) with a, b ≠ 0. Rotating A 90° counterclockwise about O gives A\'(-b, a). Use this to prove that perpendicular lines have slopes whose product is -1. '
                'The diagram shows the case A(3, 2).', fig=SLOPE_ROT,
                method='Find the slopes of OA and OA\', then their product.', key='slope OA = b/a, slope OA\' = a/(-b) = -a/b, product -1.',
                note=PR + 'Essential: a 90° rotation maps OA onto a perpendicular line; the image of (a, b) is (-b, a); slopes b/a and -a/b; product -1. '
                          'Any pair of perpendicular nonvertical lines can be translated to pass through O, keeping slopes. Invalid: checking only the one example.'),
          proof('Prove that two distinct nonvertical lines that are parallel have equal slopes.', method='Indirect: assume the slopes m₁ and m₂ are different and find an intersection point.',
                key='If m₁ ≠ m₂, then m₁x + b₁ = m₂x + b₂ has the solution x = (b₂ - b₁)/(m₁ - m₂), so the lines meet, contradicting parallel. So m₁ = m₂.',
                note=PR + 'Essential: assumption of unequal slopes; solving for the intersection; contradiction with "parallel"; conclusion.'),
          proof('Prove that if two nonvertical lines have slopes m and -1/m (m ≠ 0), they are perpendicular. (Translate both lines so they pass through the origin first.)',
                method='Rotate the point (1, m) on y = mx by 90° about the origin and find the slope of its image line.',
                key='(1, m) rotates to (-m, 1), on the line with slope 1/(-m) = -1/m; so the line with slope -1/m through O is the 90° image of y = mx, hence perpendicular.',
                note=PR + 'Essential: translations keep slopes; the rotation image of (1, m); its slope -1/m; a 90° rotation image is perpendicular; only one line through O has slope -1/m.'),
          proof('Lines y = mx and y = -x/m (m ≠ 0) pass through the origin O. Use the points P(1, m) and Q(-m, 1) and the converse of the Pythagorean Theorem to prove that the lines are perpendicular.',
                method='Compute OP², OQ², and PQ², and compare.', key='OP² + OQ² = (1 + m²) + (m² + 1) = 2 + 2m² = PQ², so ∠POQ = 90°.',
                note=PR + 'Essential: OP² = 1 + m²; OQ² = m² + 1; PQ² = (1 + m)² + (m - 1)² = 2 + 2m²; converse of the Pythagorean Theorem; conclusion.'),
      ],
      back=[
          B('Similar slope triangles give the same slope', '8.EE.B.6', [
              tf('Any two slope triangles on the same line are similar.', key=True, note='AA.'),
              sa('A line passes through (0, 0) and (2, 3). Find the rise for a run of 4.', 'Rise:', key='6', note='Any equivalent form.'),
              mc('Slope triangles with run 2, rise 3 and run 6, rise 9 give slopes', ['both 3/2', '3/2 and 9/6 that differ', '2/3 and 6/9', '6 and 18'], note='9/6 = 3/2.'),
              sa('Explain why the slope of a line is the same between any two of its points.', 'Answer:', key='The slope triangles are similar, so rise/run is the same ratio.', note='Any equivalent explanation.'),
              tf('The slope between two points on a line depends on which points are chosen.', key=False, note='Constant.'),
          ], align='exact',
            why=why('the student does not see why one line has one slope.', 'the proof uses slope triangles.', 'explains constant slope.')),
          B('Rotate a point 90° about the origin', 'HSG-CO.A.5', [
              sa('Rotate (3, 2) 90° counterclockwise about the origin.', 'Image:', key='(-2, 3)', note='Form required: an ordered pair.'),
              sa('Rotate (1, 4) 90° counterclockwise about the origin.', 'Image:', key='(-4, 1)', note='Form required: an ordered pair.'),
              mc('The rule for a 90° counterclockwise rotation about the origin is', ['(x, y) → (-y, x)', '(x, y) → (y, -x)', '(x, y) → (-x, -y)', '(x, y) → (y, x)'], note='Rule.'),
              tf('A 90° rotation maps a line to a perpendicular line.', key=True, note='Angle of rotation.'),
              tf('A 90° rotation maps (2, 0) to (0, -2).', key=False, note='Counterclockwise gives (0, 2).'),
          ], align='exact',
            why=why('the student cannot rotate points.', 'the perpendicular proof rotates (a, b).', 'rotates points 90°.')),
          B('Negative reciprocals', '7.NS.A.2', [
              sa('Negative reciprocal of 2/3?', 'Answer:', key='-3/2', note='Any equivalent form.'),
              sa('Multiply (b/a)(-a/b).', 'Product:', key='-1', note='Any equivalent form.'),
              mc('Negative reciprocal of -4?', ['¼', '-¼', '4', '-4'], note='-1 ÷ (-4).'),
              tf('A number times its negative reciprocal is -1.', key=True, note='Definition.'),
              tf('The negative reciprocal of 1 is 1.', key=False, note='-1.'),
          ], align='supporting',
            why=why('the student cannot simplify the product.', 'the proof ends with (b/a)(-a/b) = -1.', 'computes negative reciprocals.')),
      ],
      f1=B('Use the criteria to classify pairs of lines', 'HSG-GPE.B.5', [
          sa('Are y = 3x - 2 and 6x - 2y = 7 parallel, perpendicular, or neither?', 'Answer:', key='Parallel (both slopes 3)', note='Form required: the classification with the slopes.'),
          sa('Are 2x + 5y = 1 and 5x - 2y = 4 parallel, perpendicular, or neither?', 'Answer:', key='Perpendicular (slopes -2/5 and 5/2)', note='Form required: the classification with the slopes.'),
          tf('A horizontal line and a vertical line are perpendicular even though the slope product rule cannot be used.', key=True, note='Vertical slope is undefined.'),
          mc('y = ½x + 1 and y = 2x - 1 are', ['neither', 'parallel', 'perpendicular', 'the same line'], note='Product 1.'),
          sa('Find k so that y = kx + 1 is perpendicular to y = -⅓x.', 'k =', key='3', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Apply the proved criteria to lines in different forms, including the vertical/horizontal exception.'),
      f2=B('Use the criteria inside a general coordinate proof', 'HSG-GPE.B.4', [
          proof('Rhombus OABC has O(0, 0), A(a, 0), B(a + b, c), C(b, c), with b² + c² = a². Prove that its diagonals are perpendicular.', method='Find the slopes of OB and AC and multiply.',
                key='slope OB · slope AC = c/(a + b) · c/(b - a) = c²/(b² - a²) = c²/(-c²) = -1', note=CPR + 'Essential: both slopes; product simplified with b² + c² = a²; conclusion. (Assume b ≠ ±a, so neither diagonal is vertical.)'),
          sa('A coordinate proof places rhombus OABC at O(0, 0), A(a, 0), B(a + b, c), C(b, c). Why must the proof assume b² + c² = a²?', 'Answer:', key='It says OC = a = OA, the equal sides that make OABC a rhombus.', note='Any equivalent answer.'),
          tf('The slope criterion turns "perpendicular" into an algebra statement.', key=True, note='Product -1.'),
          mc('In a coordinate proof that lines are parallel, you show', ['equal slopes', 'slope product -1', 'equal lengths', 'equal intercepts'], note='Criterion.'),
          sa('Prove or disprove with slopes: A(0, 0), B(4, 2), C(3, 4) form a right angle at B.', 'Answer:', key='Proved: slope AB = ½ and slope BC = -2; the product is -1, so AB ⊥ BC.',
             note='Form required: the conclusion with slopes. Slope BC = (4 - 2)/(3 - 4) = -2; product -1.'),
      ], prog='cross-standard extension', demand='Use the slope criteria as a tool in general coordinate proofs.',
        builds='Builds on FORWARD 1: classifying lines by slope becomes a step in proving theorems.')),
]

PART = grid_fig({'A': (-5, -4), 'B': (5, 1)}, [('seg', 'A', 'B')], lo=-6, hi=6, lab={'A': 'nw', 'B': 'se'},
                desc='Coordinate grid from -6 to 6 with segment AB from A(-5, -4) to B(5, 1).')
PENT = grid_fig({'A': (-4, -2), 'B': (2, -2), 'C': (2, 3), 'D': (-1, 7), 'E': (-4, 3)}, [('poly', ['A', 'B', 'C', 'D', 'E'])], lo=-5, hi=8,
                lab={'A': 'sw', 'B': 'se', 'C': 'e', 'D': 'n', 'E': 'w'},
                desc='Coordinate grid from -5 to 8 with pentagon ABCDE: A(-4, -2), B(2, -2), C(2, 3), D(-1, 7), E(-4, 3).')
TRI_BOX = grid_fig({'A': (-2, -1), 'B': (4, 1), 'C': (1, 5)}, [('poly', ['A', 'B', 'C'])], lo=-3, hi=6, lab={'A': 'sw', 'B': 'e', 'C': 'n'},
                   desc='Coordinate grid from -3 to 6 with triangle ABC: A(-2, -1), B(4, 1), C(1, 5).')

SETS += [
    # ------------------------------------------------------------------ 70. GPE.B.5 equations of parallel/perpendicular lines
    S('HSG-GPE.B.5', 'Write equations of parallel and perpendicular lines',
      target='Use the slope criteria to write the equation of a line parallel or perpendicular to a given line through a given point', strand='core', covers=['GPE5-equation'],
      main=[
          sa('Write the equation of the line parallel to y = 3x - 5 that passes through (2, 4).', 'Equation:', key='y = 3x - 2', note='Form required: an equation; equivalent forms accepted.'),
          sa('Write the equation of the line perpendicular to y = ⅔x + 1 that passes through (4, -1).', 'Equation:', key='y = -3/2 x + 5', note='Form required: an equation; equivalent forms accepted.'),
          sa('Write the equation of the line parallel to 2x + 5y = 10 that passes through (5, 3).', 'Equation:', key='y = -2/5 x + 5', note='Form required: an equation; equivalent forms (2x + 5y = 25) accepted.'),
          sa('Write the equation of the line perpendicular to x = 4 that passes through (1, -3).', 'Equation:', key='y = -3', note='Form required: an equation. x = 4 is vertical, so the line is horizontal.'),
          mc('Which line is perpendicular to y = -4x + 1 and passes through the origin?', ['y = ¼x', 'y = 4x', 'y = -¼x', 'y = -4x'], note='Negative reciprocal of -4.'),
      ],
      back=[
          B('Read the slope of a line', '8.F.B.4', [
              sa('Slope of y = -2x + 7?', 'Slope:', key='-2', note='Any equivalent form.'),
              sa('Slope of y = 5?', 'Slope:', key='0', note='Any equivalent form.'),
              mc('Slope of y = ⅔x - 4?', ['⅔', '-4', '3/2', '4'], note='Coefficient of x.'),
              tf('In y = mx + b, m is the slope.', key=True, note='Slope-intercept form.'),
              tf('The slope of x = 3 is 3.', key=False, note='Undefined.'),
          ], align='exact',
            why=why('the student cannot read the given line\'s slope.', 'the new slope comes from it.', 'reads slopes from equations.')),
          B('Rewrite an equation in slope-intercept form', 'HSA-CED.A.4', [
              sa('Solve 2x + 5y = 10 for y.', 'Answer:', key='y = -2/5 x + 2', note='Any equivalent form.'),
              sa('Solve 3x - y = 4 for y.', 'Answer:', key='y = 3x - 4', note='Any equivalent form.'),
              mc('6x + 3y = 9 in slope-intercept form is', ['y = -2x + 3', 'y = 2x + 3', 'y = -6x + 9', 'y = -2x + 9'], note='Divide by 3.'),
              tf('x - 2y = 6 has slope ½.', key=True, note='y = ½x - 3.'),
              tf('4x + 2y = 8 has slope 4.', key=False, note='-2.'),
          ], align='exact',
            why=why('the student reads the slope from standard form incorrectly.', 'many given lines are in standard form.', 'solves for y.')),
          B('Write a line from a point and a slope', 'HSF-LE.A.2', [
              sa('Write the line with slope 3 through (2, 4).', 'Equation:', key='y = 3x - 2', note='Form required: an equation; equivalent forms accepted.'),
              sa('Write the line with slope -1 through (0, 6).', 'Equation:', key='y = -x + 6', note='Form required: an equation.'),
              mc('Slope 2 through (1, 5): b =', ['3', '5', '7', '-3'], note='5 = 2 + b.'),
              tf('y - 4 = 3(x - 2) is the line with slope 3 through (2, 4).', key=True, note='Point-slope form.'),
              tf('A line through (0, 6) has y-intercept 0.', key=False, note='6.'),
          ], align='exact',
            why=why('the student cannot write a line from a point and slope.', 'that is the last step.', 'writes linear equations.')),
          B('Opposite reciprocals', '7.NS.A.2', [
              sa('Negative reciprocal of ⅔?', 'Answer:', key='-3/2', note='Any equivalent form.'),
              sa('Negative reciprocal of -5?', 'Answer:', key='⅕', note='Any equivalent form.'),
              mc('Negative reciprocal of -2/5?', ['5/2', '-5/2', '2/5', '-2/5'], note='Flip and change sign.'),
              tf('The negative reciprocal of ¼ is -4.', key=True, note='Flip and change sign.'),
              tf('The negative reciprocal of 3 is -3.', key=False, note='-⅓.'),
          ], align='supporting',
            why=why('the student uses the opposite or the reciprocal only.', 'perpendicular slopes need both.', 'finds negative reciprocals.')),
      ],
      f1=B('Write perpendicular bisectors and altitudes', 'HSG-GPE.B.5', [
          sa('Write the equation of the perpendicular bisector of the segment from (2, 1) to (6, 5).', 'Equation:', key='y = -x + 7', note='Form required: an equation. Midpoint (4, 3), slope -1.'),
          sa('Triangle ABC has A(0, 0), B(6, 0), C(2, 4). Write the equation of the altitude from A to BC.', 'Equation:', key='y = x', note='Form required: an equation. BC slope -1, so the altitude has slope 1.'),
          tf('A perpendicular bisector passes through the midpoint of the segment.', key=True, note='Definition.'),
          mc('The perpendicular bisector of the segment from (0, 0) to (0, 8) is', ['y = 4', 'x = 4', 'y = 8', 'x = 0'], note='Horizontal through (0, 4).'),
          sa('Write the perpendicular bisector of the segment from (-3, 2) to (5, 2).', 'Equation:', key='x = 1', note='Form required: an equation.'),
      ], prog='same-course deepening', demand='Combine the midpoint or a vertex with a perpendicular slope to write special lines of triangles.'),
      f2=B('Find the distance from a point to a line', 'HSG-GPE.B.4', [
          work('Find the distance from P(5, 5) to the line y = -x + 2. Give the exact value.', 'Distance:', method='Write the perpendicular through P, find where it meets the line, then use the distance formula.',
               key='4√2 (about 5.66); the foot is (1, 1)', note='Form required: exact value (a decimal to 0.01 is also accepted). Perpendicular y = x meets y = -x + 2 at (1, 1).'),
          sa('Find the distance from (0, 0) to the line y = 4.', 'Distance:', key='4', note='Any equivalent form.'),
          tf('The distance from a point to a line can be measured along any segment from the point to the line.', key=False, note='It is measured along the perpendicular, the shortest segment.'),
          mc('The foot of the perpendicular from (3, 0) to y = x is', ['(1.5, 1.5)', '(3, 3)', '(0, 0)', '(0, 3)'], note='y = -x + 3 meets y = x.'),
          sa('Find the distance from (6, 1) to the line y = 2x - 1. Give the exact value.', 'Distance:', key='2√5 (about 4.47)', note='Form required: exact value (a decimal to 0.01 is also accepted). Foot (2, 3).'),
      ], prog='cross-standard extension', demand='Use a perpendicular line to compute a point-to-line distance.',
        builds='Builds on FORWARD 1: writing perpendicular lines through a point is the first step.')),

    # ------------------------------------------------------------------ 71. GPE.B.5 geometric problems
    S('HSG-GPE.B.5', 'Solve geometric problems with the slope criteria',
      target='Use the slope criteria for parallel and perpendicular lines to solve geometric problems (missing coordinates, altitudes, right angles)', strand='core', covers=['GPE5-problems'],
      main=[
          sa('The line through (1, 2) and (4, k) is parallel to y = 2x + 7. Find k.', 'k =', key='8', note='Any equivalent form. (k - 2)/3 = 2.'),
          sa('ABCD is a parallelogram with A(0, 0), B(5, 1), C(7, 4). Find D.', 'D =', key='(2, 3)', note='Form required: an ordered pair. AD ∥ BC and DC ∥ AB.'),
          sa('The segment from (2, 1) to (5, k) is perpendicular to the line y = 3x. Find k.', 'k =', key='0', note='Any equivalent form. (k - 1)/3 = -⅓.'),
          work('Triangle ABC has A(0, 0), B(8, 4), C(4, 6). Find the foot of the altitude from C to AB.', 'Foot:', method='Write line AB and the perpendicular through C, then solve the system.',
               key='(5.6, 2.8)', note='Form required: an ordered pair. AB: y = ½x; altitude: y = -2x + 14.'),
          mc('Triangle ABC has A(1, 1), B(4, 2), C(3, 5). At which vertex is the right angle?', ['B', 'A', 'C', 'There is no right angle'], note='Slope AB = ⅓, slope BC = -3.'),
      ],
      back=[
          B('Slope from two points', '8.F.B.4', [
              sa('Slope through (1, 2) and (4, 8)?', 'Slope:', key='2', note='Any equivalent form.'),
              sa('Slope through (4, 2) and (3, 5)?', 'Slope:', key='-3', note='Any equivalent form.'),
              mc('Slope through (0, 0) and (8, 4)?', ['½', '2', '4', '8'], note='4/8.'),
              tf('The slope from A to B equals the slope from B to A.', key=True, note='Same ratio.'),
              tf('The slope through (1, 1) and (1, 5) is 0.', key=False, note='Undefined.'),
          ], align='exact',
            why=why('the student cannot find slopes.', 'every problem compares slopes.', 'computes slopes.')),
          B('Solve a linear equation for an unknown', 'HSA-REI.B.3', [
              sa('Solve (k - 2)/3 = 2.', 'k =', key='8', note='Any equivalent form.'),
              sa('Solve ½x = -2x + 14.', 'x =', key='5.6', note='Any equivalent form.'),
              mc('Solve (k - 1)/3 = -⅓.', ['0', '2', '-2', '1'], note='k - 1 = -1.'),
              tf('Multiplying both sides by 3 is a valid first step in (k - 2)/3 = 2.', key=True, note='Inverse operation.'),
              tf('The solution of 2x + 1 = 7 is 4.', key=False, note='3.'),
          ], align='exact',
            why=why('the student sets up the slope condition but cannot solve it.', 'unknown coordinates come from equations.', 'solves linear equations.')),
          B('Equations of parallel and perpendicular lines', 'HSG-GPE.B.5', [
              sa('Line perpendicular to y = ½x through (4, 6)?', 'Equation:', key='y = -2x + 14', note='Form required: an equation.'),
              sa('Line parallel to y = -x through (0, 3)?', 'Equation:', key='y = -x + 3', note='Form required: an equation.'),
              mc('Perpendicular slope to ⅓?', ['-3', '3', '-⅓', '⅓'], note='Negative reciprocal.'),
              tf('An altitude is perpendicular to the side it meets.', key=True, note='Definition.'),
              tf('An altitude passes through the midpoint of the opposite side.', key=False, note='That is a median.'),
          ], align='exact',
            why=why('the student cannot write the needed perpendicular line.', 'the altitude foot needs it.', 'writes parallel and perpendicular lines.')),
          B('Opposite sides of a parallelogram are parallel', 'HSG-CO.C.11', [
              tf('In a parallelogram, both pairs of opposite sides are parallel and congruent.', key=True, note='Theorem.'),
              sa('A parallelogram has A(0, 0), B(3, 0), C(4, 2). Find D (in order ABCD).', 'D =', key='(1, 2)', note='Form required: an ordered pair.'),
              mc('In parallelogram ABCD, side AB is parallel to', ['DC', 'BC', 'AD', 'AC'], note='Opposite side.'),
              sa('In parallelogram ABCD, going from B to C is "right 2, up 3". Going from A to D is', 'Answer:', key='Right 2, up 3', note='Any equivalent answer.'),
              tf('A parallelogram\'s adjacent sides are always perpendicular.', key=False, note='Only rectangles.'),
          ], align='supporting',
            why=why('the student cannot find a missing vertex.', 'parallel opposite sides locate it.', 'uses parallelogram properties.')),
      ],
      f1=B('Find the orthocenter of a triangle', 'HSG-GPE.B.5', [
          work('Triangle ABC has A(0, 0), B(6, 0), C(2, 4). Find the orthocenter (the intersection of the altitudes).', 'Orthocenter:',
               method='Write two altitude equations and solve the system.', key='(2, 2)', note='Form required: an ordered pair. Altitude from C: x = 2; from A: y = x.'),
          sa('Triangle with A(0, 0), B(4, 0), C(0, 3). Where is the orthocenter?', 'Orthocenter:', key='(0, 0)', note='Form required: an ordered pair. Right angle at A.'),
          tf('The orthocenter of a right triangle is at the right-angle vertex.', key=True, note='Two legs are altitudes.'),
          mc('To find the orthocenter, you need at least', ['two altitudes', 'three medians', 'one altitude', 'the circumcenter'], note='Two lines meet in a point.'),
          sa('Check that the third altitude of the triangle A(0, 0), B(6, 0), C(2, 4) also passes through (2, 2).', 'Answer:',
             key='AC has slope 2, so the altitude from B has slope -½: y = -½(x - 6); at x = 2, y = 2. Yes.', note='Any equivalent check.'),
      ], prog='same-course deepening', demand='Solve a multi-step problem that combines two perpendicular lines into a system.'),
      f2=B('Shortest path to a straight line in a design', 'HSG-MG.A.3', [
          work('A well is at W(2, 9). A straight canal runs along y = 2x - 1 (units: 100 m). Where should a pipe from the well meet the canal so the pipe is as short as possible, and how long is it (to the nearest hundredth of a unit)?', 'Answer:',
               method='Use the perpendicular from W to the canal.', key='At (4.4, 7.8); about 2.68 units (268 m)', note='Form required: the point and the length (rounding to 0.01 unit or 1 m). Perpendicular y = -½x + 10.'),
          sa('A pipe will connect a well to a straight canal. Why is the shortest possible pipe perpendicular to the canal?', 'Answer:', key='The perpendicular segment is the shortest distance from a point to a line.', note='Any equivalent answer.'),
          tf('A pipe meeting the canal at a 60° angle is shorter than one meeting it at 90°.', key=False, note='The perpendicular is shortest; the slanted pipe is a hypotenuse.'),
          mc('A path from (0, 5) to the road y = 0 is shortest at', ['(0, 0)', '(5, 0)', '(-5, 0)', '(0, 5)'], note='Straight down.'),
          sa('A sensor at (3, 4) must connect to the line y = x. Where should the wire meet the line?', 'Point:', key='(3.5, 3.5)', note='Form required: an ordered pair. y = -x + 7.'),
      ], prog='cross-standard extension', demand='Use the perpendicular-foot computation to minimize a length in a design problem.',
        builds='Builds on FORWARD 1: intersecting a line with a perpendicular through a point.')),

    # ------------------------------------------------------------------ 72. GPE.B.6 partition
    S('HSG-GPE.B.6', 'Partition a directed segment in a given ratio',
      target='Find the point on a directed line segment between two given points that partitions the segment in a given ratio', strand='core', covers=['GPE6-partition'],
      main=[
          sa('Find the point P on the directed segment from A(1, 2) to B(13, 8) that partitions it in the ratio 1 : 2.', 'P =', key='(5, 4)', note='Form required: an ordered pair. ⅓ of the way from A.'),
          sa('Find the point P on the directed segment from A(-4, 6) to B(6, 1) that partitions it in the ratio 3 : 2.', 'P =', key='(2, 3)', note='Form required: an ordered pair. 3/5 of the way from A.'),
          sa('Find the point P on the directed segment from A(2, -3) to B(-6, 9) that partitions it in the ratio 1 : 3.', 'P =', key='(0, 0)', note='Form required: an ordered pair. ¼ of the way from A.'),
          sa('Find the point P on the directed segment from A to B that partitions it in the ratio 2 : 3.', 'P =', fig=PART, key='(-1, -2)',
             note='Form required: an ordered pair. A(-5, -4), B(5, 1); 2/5 of (10, 5) is (4, 2).'),
          mc('Point P partitions the directed segment from B(10, 5) to A(0, 0) in the ratio 1 : 4. P is', ['(8, 4)', '(2, 1)', '(5, 2.5)', '(4, 8)'], note='Start at B: ⅕ of the way toward A.'),
      ],
      back=[
          B('A ratio as a fraction of the whole', '6.RP.A.1', [
              sa('A ratio of 2 : 3 splits a whole into how many equal parts?', 'Parts:', key='5', note='Any equivalent form.'),
              sa('In a 1 : 2 partition, the first part is what fraction of the whole?', 'Fraction:', key='⅓', note='Any equivalent form.'),
              mc('In a 3 : 2 partition, the first part is', ['3/5 of the whole', '3/2 of the whole', '2/3 of the whole', '2/5 of the whole'], note='3 of 5 parts.'),
              tf('A ratio of 1 : 3 means the point is ¼ of the way along.', key=True, note='1 of 4 parts.'),
              tf('A ratio of 1 : 2 means the point is halfway.', key=False, note='⅓.'),
          ], align='exact',
            why=why('the student uses 1/2 for 1 : 2.', 'the fraction is part over total parts.', 'converts ratios to fractions of the whole.')),
          B('Horizontal and vertical change', '6.NS.C.8', [
              sa('From (1, 2) to (13, 8), what is the change in x?', 'Change:', key='12', note='Any equivalent form.'),
              sa('From (-4, 6) to (6, 1), what is the change in y?', 'Change:', key='-5', note='Any equivalent form (a decrease of 5).'),
              mc('From (2, -3) to (-6, 9), the change in x is', ['-8', '8', '-4', '4'], note='-6 - 2.'),
              tf('Change in x is the ending x minus the starting x.', key=True, note='Direction matters.'),
              tf('The change in y from (0, 5) to (0, 1) is 4.', key=False, note='-4.'),
          ], align='exact',
            why=why('the student cannot find the run and rise of the segment.', 'the partition takes a fraction of each.', 'finds signed changes.')),
          B('Find a fraction of a number', '6.NS.A.1', [
              sa('Find ⅓ of 12.', 'Answer:', key='4', note='Any equivalent form.'),
              sa('Find 3/5 of -5.', 'Answer:', key='-3', note='Any equivalent form.'),
              mc('2/5 of 10 is', ['4', '2', '5', '25'], note='10 ÷ 5 × 2.'),
              tf('¼ of -8 is -2.', key=True, note='Negative.'),
              tf('⅔ of 9 is 3.', key=False, note='6.'),
          ], align='supporting',
            why=why('the student cannot take the fraction of the change.', 'P = start + fraction × change.', 'computes fractions of signed numbers.')),
      ],
      f1=B('Work backward: find an endpoint or the ratio', 'HSG-GPE.B.6', [
          sa('P(3, 4) partitions the directed segment from A(1, 2) to B in the ratio 1 : 2. Find B.', 'B =', key='(7, 8)', note='Form required: an ordered pair. AP is ⅓ of AB.'),
          sa('P(4, 3) is on the segment from A(0, 1) to B(10, 6). In what ratio does P partition AB?', 'Ratio:', key='2 : 3', note='Form required: a ratio. 4/10 = 2/5 of the way.'),
          tf('The midpoint partitions a segment in the ratio 1 : 1.', key=True, note='Halfway.'),
          mc('P partitions AB in 3 : 1. Then P is closer to', ['B', 'A', 'neither', 'the origin'], note='¾ of the way from A.'),
          sa('M(2, 5) is the midpoint of AB with A(-1, 1). Find B.', 'B =', key='(5, 9)', note='Form required: an ordered pair.'),
      ], prog='same-course deepening', demand='Reverse the partition: find an endpoint or the ratio from known points.'),
      f2=B('The centroid as a partition point', 'HSG-GPE.B.4', [
          sa('Triangle with A(0, 0), B(6, 0), C(3, 9). Find the point ⅔ of the way from A to the midpoint of BC.', 'Point:', key='(3, 3)', note='Form required: an ordered pair. Midpoint (4.5, 4.5).'),
          proof('Show that the centroid (the point 2 : 1 along a median from the vertex) of the triangle with vertices (x₁, y₁), (x₂, y₂), (x₃, y₃) is the average of the vertices.',
                method='Partition the median from (x₁, y₁) to the midpoint of the opposite side in the ratio 2 : 1.', key='((x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3)',
                note=CPR + 'Essential: midpoint ((x₂ + x₃)/2, (y₂ + y₃)/2); x₁ + ⅔((x₂ + x₃)/2 - x₁) = (x₁ + x₂ + x₃)/3; the same for y.'),
          tf('The centroid of the triangle (0, 0), (6, 0), (3, 9) is (3, 4.5).', key=False, note='It is (3, 3), the average of the vertices.'),
          mc('The centroid of (1, 2), (4, 8), (7, -1) is', ['(4, 3)', '(4, 9)', '(12, 9)', '(3, 3)'], note='(12/3, 9/3).'),
          sa('Find the centroid of the triangle with vertices (-2, 5), (4, 1), (7, 0).', 'Centroid:', key='(3, 2)', note='Form required: an ordered pair.'),
      ], prog='cross-standard extension', demand='Use partitioning in a general coordinate proof (the centroid formula).',
        builds='Builds on FORWARD 1: reasoning about partition ratios with unknown points becomes a general proof.')),

    # ------------------------------------------------------------------ 73. GPE.B.7 perimeter
    S('HSG-GPE.B.7', 'Compute perimeters of polygons with coordinates',
      target='Use coordinates and the distance formula to compute perimeters of polygons', strand='core', covers=['GPE7-perimeter'],
      main=[
          sa('Find the perimeter of the triangle with vertices (0, 0), (3, 4), and (3, 0).', 'Perimeter:', key='12 units', note='Any equivalent form. 5 + 4 + 3.'),
          sa('Find the perimeter of the quadrilateral with vertices A(1, 1), B(4, 5), C(10, -3), D(7, -7).', 'Perimeter:', key='30 units', note='Any equivalent form. 5 + 10 + 5 + 10.'),
          sa('Find the perimeter of the triangle with vertices (0, 0), (4, 0), (2, 4). Give the exact value and a decimal to the nearest tenth.', 'Perimeter:', key='4 + 4√5 ≈ 12.9 units',
             note='Form required: both. Two sides √20 = 2√5.'),
          sa('Find the perimeter of pentagon ABCDE.', 'Perimeter:', fig=PENT, key='26 units', note='Any equivalent form. 6 + 5 + 5 + 5 + 5.'),
          mc('A square has vertices (0, 0), (3, 1), (2, 4), (-1, 3). Its perimeter is', ['4√10', '10', '16', '40'], note='Side √10.'),
      ],
      back=[
          B('Distance between two points', '8.G.B.8', [
              sa('Distance from (2, 3) to (-1, 7)?', 'Distance:', key='5', note='Any equivalent form.'),
              sa('Distance from (4, 5) to (10, -3)?', 'Distance:', key='10', note='Any equivalent form.'),
              mc('Distance from (0, 0) to (2, 4)?', ['2√5', '6', '20', '√6'], note='√20.'),
              tf('The distance from (0, 0) to (3, 1) is √10.', key=True, note='9 + 1.'),
              tf('Distances can be negative.', key=False, note='Never.'),
          ], align='exact',
            why=why('the student cannot find slanted side lengths.', 'most sides are slanted.', 'uses the distance formula.')),
          B('Lengths of horizontal and vertical sides', '6.G.A.3', [
              sa('Length of the side from (-4, -2) to (2, -2)?', 'Length:', key='6', note='Any equivalent form.'),
              sa('Length of the side from (2, -2) to (2, 3)?', 'Length:', key='5', note='Any equivalent form.'),
              mc('Length from (-3, 4) to (-3, -1)?', ['5', '3', '-5', '7'], note='|4 - (-1)|.'),
              tf('A horizontal side\'s length is the absolute value of the difference of the x-coordinates of its endpoints.', key=True, note='|x₂ - x₁|; a length is never negative.'),
              tf('The side from (1, 1) to (1, 9) has length 10.', key=False, note='8.'),
          ], align='exact',
            why=why('the student overcomplicates horizontal and vertical sides.', 'they are counted directly.', 'finds horizontal and vertical lengths.')),
          B('Simplify square roots', 'HSN-RN.A.2', [
              sa('Simplify √20.', 'Answer:', key='2√5', note='Form required: simplest radical form.'),
              sa('Simplify √50.', 'Answer:', key='5√2', note='Form required: simplest radical form.'),
              mc('2√5 + 2√5 =', ['4√5', '4√10', '2√10', '8√5'], note='Like terms.'),
              tf('√10 ≈ 3.16', key=True, note='Calculator.'),
              tf('√9 + √16 = √25', key=False, note='3 + 4 = 7.'),
          ], align='supporting',
            why=why('the student cannot combine radical side lengths.', 'exact perimeters need it.', 'simplifies and adds radicals.')),
      ],
      f1=B('Find a missing coordinate from a perimeter', 'HSG-GPE.B.7', [
          sa('A rectangle has vertices (0, 0), (k, 0), (k, 3), (0, 3) with k > 0 and perimeter 22. Find k.', 'k =', key='8', note='Any equivalent form. 2k + 6 = 22.'),
          sa('Triangle with vertices (0, 0), (6, 0), (3, h), h > 0, has perimeter 16. Find h.', 'h =', key='4', note='Any equivalent form. Each slanted side is 5.'),
          tf('The triangle with vertices (0, 0), (6, 0), (3, h) has the same perimeter for h = 4 and for h = -4.', key=True,
             note='Both give slanted sides of 5 (perimeter 16); a condition such as h > 0 is needed to pick one.'),
          mc('A square has vertices (0, 0), (a, 0), (a, a), (0, a) with a > 0 and perimeter 18. Find a.', ['4.5', '9', '4', '3'], note='4a = 18.'),
          sa('A right triangle has vertices (0, 0), (8, 0), (8, k) with k > 0 and perimeter 24. Find k.', 'k =', key='6',
             note='Any equivalent form. 8 + k + √(64 + k²) = 24, so √(64 + k²) = 16 - k; 64 + k² = 256 - 32k + k²; k = 6 (check: 8 + 6 + 10 = 24).'),
      ], prog='same-course deepening', demand='Use the perimeter relationship as an equation to find unknown coordinates.'),
      f2=B('Fencing and cost from a coordinate plan', 'HSG-MG.A.3', [
          sa('A garden plan has corners (0, 0), (8, 0), (8, 6), (0, 6), in meters. Fencing costs $12 per meter. Find the cost to fence it.', 'Cost:', key='$336', note='Any equivalent form. 28 m.'),
          sa('A triangular lot has corners (0, 0), (30, 0), (30, 40) in feet. Edging costs $2.50 per foot. Find the total cost.', 'Cost:', key='$300', note='Any equivalent form. 120 ft.'),
          tf('On a map with 1 unit = 5 m, an area of 12 square units is 60 m².', key=False, note='Areas scale by 5²: 12 × 25 = 300 m².'),
          mc('A path has corners (0, 0), (3, 4), (9, 12) (units: 10 m). Its length is', ['150 m', '15 m', '210 m', '21 m'], note='5 + 10 = 15 units.'),
          sa('A run around a lot with corners (0, 0), (5, 12), (5, 0) in units of 100 m: how many meters?', 'Distance:', key='3000 m', note='Any equivalent form. 13 + 12 + 5 = 30 units.'),
      ], prog='cross-standard extension', demand='Use perimeters from coordinates with scales and unit costs in a design problem.',
        builds='Builds on FORWARD 1: perimeters computed from coordinates now carry units and cost.')),

    # ------------------------------------------------------------------ 74. GPE.B.7 area
    S('HSG-GPE.B.7', 'Compute areas of triangles and rectangles with coordinates',
      target='Use coordinates to compute areas of triangles and rectangles (by base and height, side lengths, or a bounding rectangle)', strand='core', covers=['GPE7-area'],
      main=[
          sa('Find the area of the triangle with vertices (0, 0), (8, 0), and (3, 5).', 'Area:', key='20 square units', note='Any equivalent form. Base 8, height 5.'),
          sa('Rectangle ABCD has A(1, 1), B(5, 3), C(4, 5), D(0, 3). Find its area.', 'Area:', key='10 square units', note='Any equivalent form. AB = √20, BC = √5.'),
          sa('Find the area of triangle ABC.', 'Area:', fig=TRI_BOX, key='15 square units', note='Any equivalent form. Bounding rectangle 36 minus 6, 6, and 9.'),
          work('Find the area of the triangle with vertices A(0, 0), B(6, 2), C(2, 6).', 'Area:', method='Enclose the triangle in a rectangle and subtract the three right triangles.',
               key='16 square units', note='Any equivalent form. 36 - 6 - 8 - 6. Alternative methods (shoelace) accepted with work.'),
          mc('A triangle has vertices (0, 0), (10, 0), and (x, 4). What is its area?', ['20, for any x', '40', '20 only if x = 5', 'It depends on x'], note='Base 10, height 4.'),
      ],
      back=[
          B('Area of a triangle from base and height', '6.G.A.1', [
              sa('Area of a triangle with base 8 and height 5?', 'Area:', key='20', note='Any equivalent form.'),
              sa('Area of a right triangle with legs 6 and 2?', 'Area:', key='6', note='Any equivalent form.'),
              mc('A = ', ['½bh', 'bh', '2bh', 'b + h'], note='Formula.'),
              tf('The height of a triangle is perpendicular to the base.', key=True, note='Definition.'),
              tf('The height must be one of the sides.', key=False, note='Only in right triangles.'),
          ], align='exact',
            why=why('the student does not know the triangle area formula.', 'every method uses it.', 'computes triangle areas.')),
          B('Lengths on the coordinate plane', '6.G.A.3', [
              sa('Length from (-2, -1) to (4, -1)?', 'Length:', key='6', note='Any equivalent form.'),
              sa('Height of the point (3, 5) above the x-axis?', 'Height:', key='5', note='Any equivalent form.'),
              mc('Width of the rectangle enclosing x from -2 to 4?', ['6', '2', '4', '8'], note='4 - (-2).'),
              tf('A point with y-coordinate -3 is 3 units from the x-axis.', key=True, note='Absolute value.'),
              tf('The length from (0, 2) to (0, 9) is 11.', key=False, note='7.'),
          ], align='exact',
            why=why('the student cannot read bases and heights from coordinates.', 'they come from coordinates.', 'finds lengths on the grid.')),
          B('Distance between two points', '8.G.B.8', [
              sa('Distance from (1, 1) to (5, 3)?', 'Distance:', key='√20', note='Form required: exact value.'),
              sa('Distance from (5, 3) to (4, 5)?', 'Distance:', key='√5', note='Form required: exact value.'),
              mc('√20 · √5 =', ['10', '√25', '100', '25'], note='√100.'),
              tf('Slanted rectangle sides need the distance formula.', key=True, note='Not grid-aligned.'),
              tf('√20 · √5 = 5', key=False, note='10.'),
          ], align='supporting',
            why=why('the student cannot find slanted side lengths.', 'tilted rectangles need them.', 'computes distances.')),
      ],
      f1=B('Find a missing vertex from an area', 'HSG-GPE.B.7', [
          sa('Triangle with vertices (0, 0), (6, 0), (2, k) has area 18. Find all possible k.', 'k =', key='6 or -6', note='Form required: both values. ½ · 6 · |k| = 18.'),
          sa('A rectangle has vertices (0, 0), (a, 0), (a, 5), (0, 5), a > 0, and area 35. Find a.', 'a =', key='7', note='Any equivalent form.'),
          tf('Moving the top vertex of a triangle parallel to its base does not change its area.', key=True, note='Same height.'),
          mc('Triangle (0, 0), (4, 0), (x, 6). For which x is the area 12?', ['Any x', 'x = 2 only', 'x = 4 only', 'No x'], note='½ · 4 · 6.'),
          sa('Triangle (1, 1), (7, 1), (4, k) has area 21 and k > 1. Find k.', 'k =', key='8', note='Any equivalent form. Base 6, height 7.'),
      ], prog='same-course deepening', demand='Use the area relationship as an equation to find unknown coordinates.'),
      f2=B('Use area from coordinates with density', 'HSG-MG.A.2', [
          sa('A park on a map has corners (0, 0), (4, 0), (4, 3), (0, 3), with 1 unit = 1 km. 1,800 people live there. Find the population density.', 'Density:', key='150 people per km²',
             note='Any equivalent form. Area 12 km².'),
          sa('A triangular field has vertices (0, 0), (200, 0), (0, 150) in meters. Seeds are planted at 4 per m². How many seeds?', 'Seeds:', key='60,000', note='Any equivalent form. Area 15,000 m².'),
          tf('Density based on area is an area divided by a quantity.', key=False, note='It is a quantity divided by an area.'),
          mc('A lot with corners (0, 0), (6, 0), (6, 5), (0, 5) (meters) holds 60 plants. Density?', ['2 plants per m²', '30 plants per m²', '0.5 plants per m²', '11 plants per m²'], note='60/30.'),
          sa('A rectangle with corners (0, 0), (3, 0), (3, 2), (0, 2) (miles) has 4,200 residents. Find the density.', 'Density:', key='700 people per square mile', note='Any equivalent form.'),
      ], prog='cross-standard extension', demand='Use areas computed from coordinates in density models.',
        builds='Builds on FORWARD 1: area from coordinates is now a step in a modeling computation.')),
]
