"""G-SRT: similarity, right triangles, and trigonometry (sets 37-52)."""
import math

from qb import S, B, sa, mc, tf, plot
from common import gd, grid_fig, NTS, proof


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


PR = 'Any valid proof (paragraph, two-column, or flow). '


def r1(x):
    """Round to one decimal place, as text."""
    return ('%.1f' % (x + 1e-12)).rstrip('0').rstrip('.') if abs(x - round(x, 1)) > 1e-9 or True else ''


def d1(x):
    return '%.1f' % (round(x + 1e-12, 1))


def d2(x):
    return '%.2f' % (round(x + 1e-12, 2))


def sind(a):
    return math.sin(math.radians(a))


def cosd(a):
    return math.cos(math.radians(a))


def tand(a):
    return math.tan(math.radians(a))


def asind(x):
    return math.degrees(math.asin(x))


def acosd(x):
    return math.degrees(math.acos(x))


def atand(x):
    return math.degrees(math.atan(x))


SIM_TRI = gd({'A': (0, 0), 'B': (3, 0), 'C': (1, 2), 'D': (4.5, 0), 'E': (10.5, 0), 'F': (6.5, 4)},
             [('poly', ['A', 'B', 'C']), ('poly', ['D', 'E', 'F'])], h=200,
             desc='A small triangle ABC and a larger triangle DEF of the same shape, DEF twice as large.')
PROP = gd({'A': (1.6, 3.4), 'B': (0, 0), 'C': (5, 0), 'D': (0.8, 1.7), 'E': (3.3, 1.7)},
          [('poly', ['A', 'B', 'C']), ('seg', 'D', 'E', {'arrows': 1}), ('seg', 'B', 'C', {'arrows': 1})], h=210,
          desc='Triangle ABC with D on AB and E on AC; segment DE is parallel to BC (arrow marks).')
ALT = gd({'A': (0, 0), 'B': (5, 0), 'C': (1.8, 2.4), 'D': (1.8, 0)},
         [('poly', ['A', 'B', 'C']), ('seg', 'C', 'D', {'dash': True}), ('ra', 'C', 'A', 'B'), ('ra', 'D', 'B', 'C')], h=210, lab={'D': 's'},
         desc='Right triangle ABC with the right angle at C. The altitude CD is drawn from C to the hypotenuse AB, with a right-angle mark at D.')


def rt(a_lab=None, b_lab=None, c_lab=None, ang=None, ang_at='A', h=210, desc=None, w=4.0, ht=2.6):
    """Right triangle with the right angle at C(w, 0), A at (0, 0), B at (w, ht). Labels on legs AC (bottom), BC (vertical), hypotenuse AB."""
    P = {'A': (0, 0), 'C': (w, 0), 'B': (w, ht)}
    it = [('poly', ['A', 'C', 'B']), ('ra', 'C', 'A', 'B')]
    if a_lab:
        it.append(('seg', 'A', 'C', {'label': a_lab, 'side': -1}))
    if b_lab:
        it.append(('seg', 'C', 'B', {'label': b_lab, 'side': 1}))
    if c_lab:
        it.append(('seg', 'A', 'B', {'label': c_lab, 'side': 1}))
    if ang:
        it.append(('ang', 'A', 'C', 'B', {'label': ang}) if ang_at == 'A' else ('ang', 'B', 'A', 'C', {'label': ang}))
    return gd(P, it, h=h, desc=desc or 'Right triangle ABC with the right angle at C.')


SETS = [
    # ------------------------------------------------------------------ 37. SRT.A.1.a dilations and lines
    S('HSG-SRT.A.1.a', 'Verify that a dilation maps a line to a parallel line (or to itself through the center)',
      target='Verify with coordinates that a dilation maps a line not through its center to a parallel line and leaves a line through the center unchanged',
      strand='core', covers=['SRT1a-lines'],
      main=[
          sa('Line ℓ is y = 2x + 1. Dilate it about the origin with scale factor 3: find the images of (0, 1) and (1, 3), and write an equation of the image line. Is it parallel to ℓ?',
             'Answer:', key='(0, 3) and (3, 9); y = 2x + 3; yes, parallel (both slopes are 2).', note='Form required: both images, the equation, and the conclusion.'),
          sa('Line m is y = -x, which passes through the origin. Dilate it about the origin with scale factor 2: find the images of (1, -1) and (3, -3). What is the image line?',
             'Answer:', key='(2, -2) and (6, -6); the image is y = -x, the same line.', note='Form required: the images and the conclusion that the line maps onto itself.'),
          sa('The horizontal line y = 4 is dilated about the origin with scale factor ½. Find an equation of the image and compare it with the original.', 'Answer:',
             key='y = 2; it is parallel to y = 4 (both horizontal).', note='Form required: the equation and the comparison. (x, 4) → (½x, 2).'),
          mc('A dilation with center C maps line ℓ, which does not pass through C, to line ℓ′. Which is true?', ['ℓ′ ∥ ℓ', 'ℓ′ is the same line as ℓ', 'ℓ′ ⊥ ℓ', 'ℓ′ passes through C'],
             note='Lines not through the center map to parallel lines.'),
          tf('A dilation about point C maps every line through C onto itself.', key=True, note='Each point of the line moves along the line, toward or away from C.'),
      ],
      back=[
          B('Dilate points with coordinates', '8.G.A.3', [
              sa('Dilate (2, -3) about the origin with scale factor 4.', 'Image:', key='(8, -12)', note='Form required: an ordered pair.'),
              sa('Dilate (6, 10) about the origin with scale factor ½.', 'Image:', key='(3, 5)', note='Form required: an ordered pair.'),
              mc('A dilation about the origin sends (3, 1) to (9, 3). What is the scale factor?', ['3', '6', '⅓', '9'], note='Each coordinate is tripled.'),
              tf('A dilation about the origin with scale factor 1 leaves every point where it is.', key=True, note='(x, y) → (x, y).'),
              tf('A dilation with scale factor 2 moves the center to a new point.', key=False, note='The center is fixed.'),
          ], align='exact',
            why=why('the student cannot dilate a point.', 'checking a line\'s image starts with images of its points.', 'applies (x, y) → (kx, ky).')),
          B('Compare slopes to test whether lines are parallel', '8.EE.B.6', [
              sa('Find the slope of the line through (0, 3) and (3, 9).', 'Slope:', key='2', note='Any equivalent form.'),
              tf('y = 2x + 1 and y = 2x + 3 are parallel.', key=True, note='Same slope, different intercepts.'),
              mc('Which line is parallel to y = -3x + 2?', ['y = -3x - 5', 'y = 3x + 2', 'y = ⅓x', 'y = -3'], note='Slope -3.'),
              sa('Are y = 5 and y = 2 parallel?', 'Answer:', key='Yes (both horizontal)', note='Any equivalent answer.'),
              tf('Lines with slopes 2 and -2 are parallel.', key=False, note='Different slopes.'),
          ], align='exact',
            why=why('the student cannot decide whether two lines are parallel.', 'the property is about parallel images.', 'compares slopes.')),
          B('Write the equation of a line through two points', '8.F.B.4', [
              sa('Write an equation of the line through (0, 3) and (3, 9).', 'Equation:', key='y = 2x + 3', note='Any equivalent equation.'),
              sa('Write an equation of the line through (2, -2) and (6, -6).', 'Equation:', key='y = -x', note='Any equivalent equation.'),
              mc('Which point is on y = 2x + 3?', ['(1, 5)', '(5, 1)', '(0, 2)', '(2, 3)'], note='2(1) + 3 = 5.'),
              tf('The line through (0, 0) and (4, 8) is y = 2x.', key=True, note='Slope 2, intercept 0.'),
              tf('The line through (1, 1) and (2, 4) has slope 2.', key=False, note='(4 - 1) ÷ (2 - 1) = 3.'),
          ], align='exact',
            why=why('the student cannot name the image line.', 'the image line is described by an equation.', 'writes line equations from two points.')),
      ],
      f1=B('Dilate lines about a center other than the origin', 'HSG-SRT.A.1.a', [
          sa('Dilate the line y = x + 2 about the center (2, 0) with scale factor 2. Find the images of (0, 2) and (2, 4) and the image line.', 'Answer:',
             key='(-2, 4) and (2, 8); y = x + 6, parallel to y = x + 2.', note='Form required: images, equation, and conclusion. Image = center + 2(point - center).'),
          sa('Does the line y = x - 2 pass through the center (2, 0)? What happens to it under any dilation about (2, 0)?', 'Answer:',
             key='Yes, 0 = 2 - 2; it maps onto itself.', note='Form required: both parts.'),
          tf('Under a dilation about (1, 1) with scale factor 3, the point (2, 1) goes to (4, 1).', key=True, note='(1, 1) + 3(1, 0) = (4, 1).'),
          mc('A dilation about (0, 2) with scale factor ½ maps (4, 6) to', ['(2, 4)', '(2, 3)', '(4, 4)', '(8, 10)'], note='(0, 2) + ½(4, 4) = (2, 4).'),
          sa('Line ℓ: y = 3x. A dilation about (1, 0) with scale factor 2 maps ℓ to ℓ′. Find ℓ′.', 'Equation:', key='y = 3x + 3',
             note='Any equivalent equation. (0, 0) → (-1, 0) and (1, 3) → (1, 6); slope 3.'),
      ], prog='same-course deepening', demand='Carry out the verification when the center is not the origin.'),
      f2=B('Prove algebraically that a dilation maps a line to a parallel line', 'HSG-SRT.A.1.a', [
          proof('Prove that the dilation about the origin with scale factor k (k > 0, k ≠ 1) maps the line y = mx + b to the line y = mx + kb.',
                method='Take any point (x, mx + b) on the line, find its image, and show the image satisfies y = mx + kb (and every point of that line is an image).',
                key='The image of (x, mx + b) is (kx, kmx + kb), which satisfies y = mx + kb.',
                note=PR + 'Essential: image (X, Y) = (kx, k(mx + b)); Y = m(kx) + kb = mX + kb; conversely (X, mX + kb) is the image of (X/k, mX/k + b). Conclusion: same slope m, '
                     'so parallel when b ≠ 0, the same line when b = 0. Invalid: checking only two points of one example.'),
          sa('From the general result, when does the image of y = mx + b coincide with the original line?', 'Answer:', key='When b = 0 (the line passes through the center).', note='Any equivalent answer.'),
          tf('The dilation (x, y) → (kx, ky) maps vertical lines x = c to vertical lines x = kc.', key=True, note='Parallel vertical lines (or the same when c = 0).'),
          mc('Under the dilation about the origin with scale factor 4, the line y = -2x + 5 maps to', ['y = -2x + 20', 'y = -8x + 20', 'y = -2x + 5', 'y = -8x + 5'],
             note='y = mx + kb.'),
          sa('Explain why measuring a few dilated lines is not a proof of the property.', 'Answer:', key='Examples cannot cover every line; a proof must work for all lines (with variables).',
             note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Generalize the verification with parameters into a proof for every line.',
        builds='FORWARD 1 verifies for any center; FORWARD 2 proves the property for every line algebraically.')),

    # ------------------------------------------------------------------ 38. SRT.A.1.b dilations and lengths
    S('HSG-SRT.A.1.b', 'Verify that a dilation multiplies lengths by the scale factor',
      target='Verify with coordinates and measurements that a dilated segment is k times as long as the original', strand='core', covers=['SRT1b-length'],
      main=[
          sa('Segment AB has A(1, 2) and B(4, 6). Dilate it about the origin with scale factor 3. Find A′B′ and AB, and compare.', 'Answer:',
             key='A′(3, 6), B′(12, 18); AB = 5 and A′B′ = 15 = 3 · AB.', note='Form required: images, both lengths, and the ratio.'),
          sa('Segment PQ has P(-4, 2) and Q(8, -6). Dilate it about the origin with scale factor ½. Find PQ and P′Q′.', 'Answer:',
             key='P′(-2, 1), Q′(4, -3); PQ = √208 = 4√13 ≈ 14.42 and P′Q′ = √52 = 2√13 ≈ 7.21, half as long.', note='Form required: both lengths (exact or to 0.01) and the ratio.'),
          sa('Segment CD has C(2, 1) and D(5, 5). Dilate it about the center (2, 1) with scale factor 2. Find C′D′.', 'Answer:',
             key='C′ = (2, 1), D′ = (8, 9); C′D′ = 10 = 2 · CD (CD = 5).', note='Form required: images and lengths.'),
          mc('A segment 8 cm long is dilated with scale factor 0.75. How long is the image?', ['6 cm', '8.75 cm', '10.67 cm', '7.25 cm'], note='0.75 × 8.'),
          tf('A dilation with scale factor 2.5 makes every segment 2.5 units longer.', key=False, note='It multiplies lengths by 2.5; it does not add 2.5.'),
      ],
      back=[
          B('Find lengths with the distance formula', '8.G.B.8', [
              sa('Find the distance between (3, 6) and (12, 18).', 'Distance:', key='15', note='Any equivalent form.'),
              sa('Find the distance between (-2, 1) and (4, -3).', 'Distance:', key='√52 = 2√13', note='Any equivalent exact form.'),
              mc('Find the distance between (0, 0) and (5, 12).', ['13', '17', '7', '√17'], note='√169.'),
              tf('The distance between (1, 2) and (4, 6) is 5.', key=True, note='√(9 + 16).'),
              tf('The distance between (0, 0) and (3, 3) is 6.', key=False, note='3√2.'),
          ], align='exact',
            why=why('the student cannot compute lengths.', 'the property compares lengths.', 'uses the distance formula.')),
          B('Scale factor in scale drawings', '7.G.A.1', [
              sa('A drawing uses scale factor 4. A 3 cm segment in the original is how long in the drawing?', 'Length:', key='12 cm', note='Any equivalent form.'),
              sa('A 15 m wall is drawn 5 cm long. What scale factor (drawing ÷ actual, in the same units) was used?', 'Scale factor:', key='5/1500 = 1/300', note='Any equivalent form.'),
              tf('A scale factor less than 1 makes a figure smaller.', key=True, note='Lengths shrink.'),
              mc('A rectangle 4 by 6 is enlarged by a scale factor of 1.5. Its new dimensions are', ['6 by 9', '5.5 by 7.5', '4 by 9', '8 by 12'], note='Multiply each side.'),
              tf('Enlarging by a scale factor of 2 doubles the area.', key=False, note='Area is multiplied by 4.'),
          ], align='exact',
            why=why('the student treats a scale factor as something added.', 'dilation multiplies lengths.', 'applies scale factors.')),
          B('Dilate points about the origin', '8.G.A.3', [
              sa('Dilate (4, 6) about the origin with scale factor 3.', 'Image:', key='(12, 18)', note='Form required: an ordered pair.'),
              sa('Dilate (-4, 2) about the origin with scale factor ½.', 'Image:', key='(-2, 1)', note='Form required: an ordered pair.'),
              mc('Dilation about the origin sends (2, 5) to (5, 12.5). Scale factor?', ['2.5', '3', '7', '0.4'], note='5 ÷ 2.'),
              tf('Dilating about the origin multiplies both coordinates by the scale factor.', key=True, note='(kx, ky).'),
              tf('Dilating (3, 0) by 2 about the origin gives (5, 0).', key=False, note='(6, 0).'),
          ], align='exact',
            why=why('the student cannot find the dilated endpoints.', 'lengths are computed from images.', 'dilates points.')),
      ],
      f1=B('Find the center or scale factor from a segment and its image', 'HSG-SRT.A.1.b', [
          sa('A dilation about the origin maps a segment of length 6 to a segment of length 15. What is the scale factor?', 'Scale factor:', key='2.5', note='Any equivalent form.'),
          sa('A dilation maps A(1, 1) to A′(3, 3) and B(2, 1) to B′(5, 3). Find the scale factor and the center.', 'Answer:',
             key='Scale factor 2; center (-1, -1).', note='Form required: both. A′B′ = 2 = 2AB; lines AA′ and BB′ meet at (-1, -1).'),
          tf('Lines through each point and its image under a dilation all pass through the center.', key=True, note='Each image is on the ray from the center.'),
          mc('A dilation maps P(4, 0) to P′(1, 0) and its center is the origin. Scale factor?', ['¼', '4', '-3', '3'], note='1 ÷ 4.'),
          sa('A segment of length 9 is dilated by an unknown factor k, and the image is 3 units shorter than the original. Find k.', 'k =', key='⅔', note='Any equivalent form. 9k = 6.'),
      ], prog='same-course deepening', demand='Solve the inverse problem: find the scale factor and center from a segment and its image.'),
      f2=B('Perimeter and area of dilated figures', 'HSG-SRT.A.2', [
          sa('A triangle with perimeter 18 and area 12 is dilated with scale factor 3. Find the new perimeter and area.', 'Answer:', key='Perimeter 54; area 108', note='Form required: both.'),
          sa('A square of area 50 is dilated so its area becomes 8. Find the scale factor.', 'Scale factor:', key='⅖', note='Any equivalent form. k² = 8/50 = 4/25.'),
          tf('If lengths are multiplied by k, areas are multiplied by k².', key=True, note='Area is length times length.'),
          mc('A figure is dilated with scale factor ½. Its area is multiplied by', ['¼', '½', '2', '4'], note='(½)².'),
          sa('Explain why a dilation with factor k multiplies the perimeter by k.', 'Answer:', key='Every side is multiplied by k, and the perimeter is the sum of the sides.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Extend from one length to whole-figure measures: perimeter scales by k and area by k².',
        builds='A second extension of MAIN: FORWARD 1 reverses the length relationship; FORWARD 2 applies it to perimeter and area.')),
]


def pair_grid(P1, P2, desc, lo=-8, hi=8, names=None):
    P = dict(P1)
    P.update(P2)
    return grid_fig(P, [('poly', list(P1)), ('poly', list(P2))], lo=lo, hi=hi, desc=desc, names=names or {})


SETS += [
    # ------------------------------------------------------------------ 39. SRT.A.2 decide similarity
    S('HSG-SRT.A.2', 'Decide whether two figures are similar using similarity transformations',
      target='Given two figures, decide whether they are similar by finding a similarity transformation (dilation and rigid motions) or explaining why none exists',
      strand='core', covers=['SRT2-decide'],
      main=[
          sa('Is triangle ABC similar to triangle DEF? If so, describe a similarity transformation that maps ABC onto DEF; if not, explain.', 'Answer:',
             fig=pair_grid({'A': (0, 0), 'B': (2, 0), 'C': (0, 1)}, {'D': (0, 0), 'E': (-6, 0), 'F': (0, -3)},
                           'Grid from -8 to 8. Triangle ABC: A(0, 0), B(2, 0), C(0, 1). Triangle DEF: D(0, 0), E(-6, 0), F(0, -3).'),
             key='Yes. Dilate by 3 about the origin, then rotate 180° about the origin.', note='Any valid similarity transformation. Check: (2, 0) → (6, 0) → (-6, 0); (0, 1) → (0, 3) → (0, -3).'),
          sa('Is rectangle R (4 by 6) similar to rectangle S (6 by 8)? Explain using similarity transformations.', 'Answer:',
             key='No. A dilation would need factor 6/4 = 1.5 for one side and 8/6 ≈ 1.33 for the other; no single scale factor works.', note='Any equivalent explanation comparing the ratios.'),
          sa('Is triangle PQR similar to triangle XYZ? If so, describe a similarity transformation; if not, explain.', 'Answer:',
             fig=pair_grid({'P': (1, 1), 'Q': (3, 1), 'R': (1, 4)}, {'X': (-2, 2), 'Y': (-6, 2), 'Z': (-2, 8)},
                           'Grid from -8 to 8. Triangle PQR: P(1, 1), Q(3, 1), R(1, 4). Triangle XYZ: X(-2, 2), Y(-6, 2), Z(-2, 8).'),
             key='Yes. Dilate by 2 about the origin, then reflect across the y-axis.', note='Any valid sequence. (1, 1) → (2, 2) → (-2, 2); (3, 1) → (6, 2) → (-6, 2); (1, 4) → (2, 8) → (-2, 8).'),
          mc('Which pair of figures must be similar?', ['Any two squares', 'Any two rectangles', 'Any two rhombuses', 'Any two isosceles triangles'],
             note='Two squares differ only by a scale factor (and position); the others can have different shapes.'),
          tf('If a sequence of rigid motions and one dilation carries figure F onto figure G, then F and G are similar.', key=True, note='Definition of similarity.'),
      ],
      back=[
          B('Similar figures as a sequence of transformations including a dilation', '8.G.A.4', [
              tf('A figure and its image after a dilation and a translation are similar.', key=True, note='A similarity sequence.'),
              mc('Two figures are similar. What may be different?', ['Their size', 'Their angle measures', 'Their shape', 'The ratios of their sides'], note='Size may change.'),
              sa('A triangle is dilated by 2 and then rotated. Its sides were 3, 4, 5. What are the image\'s sides?', 'Lengths:', key='6, 8, 10', note='Any order.'),
              tf('Two figures with the same angles but different side ratios are similar.', key=False, note='Side ratios must all be equal.'),
              sa('Name the transformation that changes size.', 'Answer:', key='A dilation', note='Any equivalent answer.'),
          ], align='exact',
            why=why('the student does not connect similarity with transformations.', 'the decision is made with a similarity transformation.', 'describes similarity sequences.')),
          B('Specify a sequence of rigid motions', 'HSG-CO.A.5', [
              sa('Which rigid motion maps (x, y) to (-x, y)?', 'Answer:', key='Reflection across the y-axis', note='Any equivalent answer.'),
              sa('Which rigid motion maps (x, y) to (-x, -y)?', 'Answer:', key='Rotation of 180° about the origin', note='Any equivalent answer.'),
              mc('Which rigid motion maps (2, 3) to (-3, 2)?', ['Rotation 90° counterclockwise about the origin', 'Reflection across the x-axis', 'Translation 5 left', 'Rotation 180°'],
                 note='(x, y) → (-y, x).'),
              tf('A translation then a reflection is a valid sequence of rigid motions.', key=True, note='Any composition of rigid motions.'),
              tf('A dilation is a rigid motion.', key=False, note='It changes lengths unless k = 1.'),
          ], align='exact',
            why=why('the student cannot finish the sequence after scaling.', 'a similarity sequence ends with rigid motions.', 'names rigid motions from rules.')),
          B('Dilate figures about the origin', '8.G.A.3', [
              sa('Dilate triangle (0, 0), (2, 0), (0, 1) by 3 about the origin.', 'Image:', key='(0, 0), (6, 0), (0, 3)', note='Form required: the three vertices.'),
              tf('A dilation about the origin with factor 3 triples each coordinate.', key=True, note='(3x, 3y).'),
              mc('(4, -2) dilated by ½ about the origin is', ['(2, -1)', '(8, -4)', '(4.5, -1.5)', '(2, -2)'], note='Halve each coordinate.'),
              sa('A dilation about the origin maps (5, 5) to (2, 2). What is the factor?', 'Factor:', key='0.4', note='Any equivalent form.'),
              tf('A dilation can change the angles of a triangle.', key=False, note='Angles are preserved.'),
          ], align='exact',
            why=why('the student cannot apply the scaling step.', 'similarity sequences include a dilation.', 'dilates figures.')),
      ],
      f1=B('Find the scale factor and correspondence when the image is turned or flipped', 'HSG-SRT.A.2', [
          sa('Triangle ABC has sides AB = 4, BC = 6, CA = 8. Triangle PQR has PQ = 9, QR = 12, RP = 6. Are they similar? If so, give the correspondence and the scale factor.', 'Answer:',
             key='Yes: A ↔ R, B ↔ P, C ↔ Q (AB ↔ RP = 6, BC ↔ PQ = 9, CA ↔ QR = 12); scale factor 1.5.', note='Form required: the correspondence and the factor. Match shortest to shortest.'),
          sa('A 3-4-5 triangle and a triangle with sides 7.5, 10, 12.5: similar? Scale factor?', 'Answer:', key='Yes; 2.5', note='Form required: both.'),
          tf('Matching the shortest side with the shortest side, middle with middle, and longest with longest gives the correspondence for similar triangles.', key=True,
             note='Similarity preserves the order of side lengths.'),
          mc('Triangles with sides 5, 6, 7 and 10, 12, 15: are they similar?', ['No, 15/7 ≠ 2', 'Yes, factor 2', 'Yes, factor 2.5', 'Cannot tell'], note='Ratios 2, 2, 15/7.'),
          sa('Triangle ABC ~ triangle DEF with a factor of 4 from ABC to DEF. DE = 10. Find AB.', 'AB =', key='2.5', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Decide similarity and its correspondence when the figures are in different orientations, using side ratios.'),
      f2=B('Prove that all circles are similar', 'HSG-C.A.1', [
          proof('Circle C₁ has center A and radius r; circle C₂ has center B and radius s. Prove that C₁ and C₂ are similar.',
                method='Translate A to B, then dilate about B with scale factor s/r; show the image of C₁ is C₂.', key='A translation and a dilation map C₁ onto C₂.',
                note=PR + 'Essential: the translation maps C₁ to the circle with center B and radius r; the dilation about B with factor s/r sends each point at distance r from B to '
                     'a point at distance s, so the image is C₂ (and every point of C₂ is reached).'),
          sa('Circle P has radius 4 and circle Q has radius 10. What scale factor maps P onto Q (after a translation)?', 'Scale factor:', key='2.5', note='Any equivalent form.'),
          tf('Any two circles are similar.', key=True, note='Translate and dilate.'),
          mc('Which pair of figures is NOT always similar?', ['Two ellipses', 'Two circles', 'Two squares', 'Two equilateral triangles'], note='Ellipses can have different shapes.'),
          sa('Explain why all equilateral triangles are similar.', 'Answer:', key='All their angles are 60°, so AA applies (or all side ratios are equal).', note='Any valid explanation.'),
      ], prog='cross-standard extension', demand='Extend the transformation definition of similarity to curved figures (circles).',
        builds='A second extension of MAIN: FORWARD 1 handles turned and flipped triangles; FORWARD 2 applies the definition to circles.')),

    # ------------------------------------------------------------------ 40. SRT.A.2 meaning for triangles
    S('HSG-SRT.A.2', 'Explain similarity of triangles as equal angles and proportional sides',
      target='Explain, using similarity transformations, why similar triangles have all corresponding angles congruent and all corresponding sides proportional, and use this meaning',
      strand='core', covers=['SRT2-meaning'],
      main=[
          proof('A similarity transformation (a dilation with scale factor k followed by rigid motions) maps △ABC onto △DEF with A → D, B → E, C → F. Explain why ∠A ≅ ∠D, ∠B ≅ ∠E, ∠C ≅ ∠F and DE/AB = EF/BC = FD/CA = k.',
                method='Use what dilations and rigid motions do to angles and to lengths.', key='Angles are preserved and every length is multiplied by k.',
                note='Any valid explanation. Essential: dilations and rigid motions preserve angle measure, so corresponding angles are congruent; the dilation multiplies every length '
                     'by k and rigid motions keep lengths, so each image side is k times its original side.'),
          sa('△ABC ~ △DEF with A ↔ D, B ↔ E, C ↔ F. AB = 6, BC = 9, DE = 10. Find EF and the scale factor from ABC to DEF.', 'Answer:', key='EF = 15; scale factor 5/3',
             note='Form required: both. 10/6 = 5/3; EF = 9 · 5/3.'),
          sa('△PQR ~ △STU with P ↔ S, Q ↔ T, R ↔ U. m∠P = 42° and m∠Q = 71°. Find m∠U.', 'm∠U =', key='67°', note='Any equivalent form. ∠U ≅ ∠R = 180 - 113.'),
          mc('Which information shows that △ABC is NOT similar to △XYZ (A ↔ X, B ↔ Y, C ↔ Z)?', ['AB/XY = 2 but BC/YZ = 3', '∠A ≅ ∠X', 'AB/XY = BC/YZ = CA/ZX = 2', 'All angles of both are 60°'],
             note='All three side ratios must be equal.'),
          tf('If △ABC ~ △DEF, then AB/DE = BC/EF.', key=True, note='Corresponding sides are proportional.'),
      ],
      back=[
          B('Read correspondence from a similarity or congruence statement', 'HSG-CO.B.7', [
              sa('△ABC ~ △XYZ. Which angle corresponds to ∠C?', 'Angle:', key='∠Z', note='Any equivalent form.'),
              sa('△ABC ~ △XYZ. Which side corresponds to BC?', 'Side:', key='YZ', note='Any equivalent form.'),
              mc('△KLM ~ △RST. Which ratio equals KL/RS?', ['LM/ST', 'LM/RT', 'KM/ST', 'RS/LM'], note='Second pair of letters.'),
              tf('△DEF ~ △GHI means ∠E ≅ ∠H.', key=True, note='Middle letters.'),
              tf('△DEF ~ △GHI means DF corresponds to GH.', key=False, note='DF ↔ GI.'),
          ], align='exact',
            why=why('the student mismatches parts.', 'proportional sides must be corresponding sides.', 'reads correspondences.')),
          B('Solve proportions', '7.RP.A.2', [
              sa('Solve 6/9 = 10/x.', 'x =', key='15', note='Any equivalent form.'),
              sa('Solve x/4 = 15/6.', 'x =', key='10', note='Any equivalent form.'),
              mc('Which ratio is equal to 3 : 5?', ['12 : 20', '5 : 3', '6 : 8', '9 : 12'], note='Multiply both by 4.'),
              tf('2/3 = 8/12', key=True, note='Both reduce to 2/3.'),
              tf('4/6 = 6/9 = 10/14', key=False, note='10/14 = 5/7.'),
          ], align='exact',
            why=why('the student cannot solve proportions.', 'missing sides are found with proportions.', 'solves and checks proportions.')),
          B('Scale factor between figures', '7.G.A.1', [
              sa('A figure is enlarged so that a 4 cm side becomes 10 cm. Scale factor?', 'Factor:', key='2.5', note='Any equivalent form.'),
              tf('All lengths of a scale drawing are multiplied by the same number.', key=True, note='The scale factor.'),
              mc('With scale factor 3, a 7 cm side becomes', ['21 cm', '10 cm', '7 cm', '73 cm'], note='Multiply.'),
              sa('A scale drawing\'s 12 cm side represents 60 cm. Scale factor (drawing to actual)?', 'Factor:', key='⅕', note='Any equivalent form.'),
              tf('A scale drawing changes the angles of a figure.', key=False, note='Angles stay the same.'),
          ], align='exact',
            why=why('the student does not use one factor for all sides.', 'the meaning of similarity is one common ratio.', 'finds and applies scale factors.')),
      ],
      f1=B('Use the AA criterion to recognize similar triangles', 'HSG-SRT.A.3', [
          sa('Two triangles have angles of 35° and 80°. Are they similar? Why?', 'Answer:', key='Yes, by AA: two pairs of congruent angles (the third angles are both 65°).', note='Any equivalent answer.'),
          sa('Triangle ABC has m∠A = 50°, m∠B = 60°. Triangle DEF has m∠D = 60°, m∠F = 70°. Are they similar? Give the correspondence.', 'Answer:',
             key='Yes: ∠C = 70°, ∠E = 50°; A ↔ E, B ↔ D, C ↔ F.', note='Form required: the decision and the correspondence.'),
          tf('Two right triangles with one pair of congruent acute angles are similar.', key=True, note='Two pairs of congruent angles (the right angles and the acute angles).'),
          mc('Which pair is NOT necessarily similar?', ['Two isosceles triangles', 'Two equilateral triangles', 'Two right isosceles triangles', 'Two triangles with angles 30° and 60°'],
             note='Isosceles triangles can have different vertex angles.'),
          sa('In a figure, DE ∥ BC with D on AB and E on AC. Explain why △ADE ~ △ABC.', 'Answer:', key='∠A is shared and ∠ADE ≅ ∠ABC (corresponding angles), so AA.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Move from the full definition (all angles and sides) to a shortcut criterion (AA).'),
      f2=B('Use similarity to find unknown lengths in problems', 'HSG-SRT.B.5', [
          sa('A 1.8 m person casts a 2.4 m shadow when a tree casts a 16 m shadow. How tall is the tree?', 'Height:', key='12 m', note='Any equivalent form. 1.8/2.4 = h/16.'),
          sa('In △ABC, DE ∥ BC with AD = 4, DB = 6, and DE = 5. Find BC.', 'BC =', key='12.5', note='Any equivalent form. AD/AB = DE/BC: 4/10 = 5/BC.'),
          tf('In similar triangles with scale factor 3, a 7 cm side corresponds to a 21 cm side.', key=True, note='7 × 3.'),
          mc('A 6 ft pole casts a 4 ft shadow. At the same time, a building casts a 30 ft shadow. How tall is the building?', ['45 ft', '20 ft', '36 ft', '24 ft'], note='6/4 = h/30.'),
          sa('Two similar triangles have perimeters 24 and 36. A side of the smaller is 10. Find the corresponding side of the larger.', 'Side:', key='15', note='Any equivalent form. Factor 1.5.'),
      ], prog='cross-standard extension', demand='Apply the meaning of similarity to solve real and geometric problems.',
        builds='Builds on FORWARD 1: once AA identifies similar triangles, their proportional sides solve problems.')),

    # ------------------------------------------------------------------ 41. SRT.A.3 AA
    S('HSG-SRT.A.3', 'Establish the AA criterion with similarity transformations',
      target='Use the properties of similarity transformations to prove that two triangles with two pairs of congruent angles are similar',
      strand='core', covers=['SRT3-aa'],
      main=[
          proof('In △ABC and △DEF, ∠A ≅ ∠D and ∠B ≅ ∠E. Prove that △ABC ~ △DEF using similarity transformations.',
                method='Dilate △ABC by k = DE/AB; show the image is congruent to △DEF by ASA; conclude a dilation followed by rigid motions maps ABC onto DEF.',
                key='△ABC ~ △DEF.',
                note=PR + 'Essential: (1) dilate by k = DE/AB to get △A′B′C′ with A′B′ = DE; (2) dilations keep angles, so ∠A′ ≅ ∠D and ∠B′ ≅ ∠E; (3) △A′B′C′ ≅ △DEF by ASA; '
                     '(4) so rigid motions map A′B′C′ onto DEF, and the dilation followed by those motions maps ABC onto DEF. Invalid: assuming the sides are proportional.'),
          sa('In the AA proof, why is the scale factor chosen as DE/AB?', 'Answer:', key='So the image of AB has the same length as DE, making ASA possible.', note='Any equivalent answer.'),
          sa('In the AA proof, after dilating △ABC to △A′B′C′, which criterion shows △A′B′C′ ≅ △DEF, and which parts does it use?', 'Answer:',
             key='ASA: ∠A′ ≅ ∠D, A′B′ = DE, ∠B′ ≅ ∠E.', note='Form required: the criterion and the three parts.'),
          mc('Why is it enough to know TWO pairs of congruent angles?', ['The angle sum makes the third pair congruent too', 'Two angles fix the side lengths',
                                                                         'Any two triangles are similar', 'The third angle can be different'],
             note='Both third angles equal 180° minus the other two.'),
          tf('The AA argument uses the fact that dilations preserve angle measure.', key=True, note='The dilated triangle keeps ∠A and ∠B.'),
      ],
      back=[
          B('Prove triangles congruent with ASA', 'HSG-CO.B.8', [
              sa('Two triangles have ∠A ≅ ∠D, AB = DE, ∠B ≅ ∠E. Which criterion?', 'Criterion:', key='ASA', note='Any equivalent form.'),
              tf('ASA needs the side between the two angles.', key=True, note='Included side.'),
              mc('Which set of parts gives ASA?', ['Two angles and the side between them', 'Two sides and the angle between them', 'Three sides', 'Three angles'], note='Definition.'),
              sa('After proving △PQR ≅ △XYZ, are their corresponding sides equal?', 'Answer:', key='Yes', note='Corresponding parts.'),
              tf('ASA works only for right triangles.', key=False, note='Any triangles.'),
          ], align='exact',
            why=why('the student cannot finish with a congruence.', 'the AA proof ends with ASA.', 'applies ASA.')),
          B('Dilations multiply lengths and keep angles', 'HSG-SRT.A.1.b', [
              sa('A 5 cm segment is dilated by 1.6. How long is the image?', 'Length:', key='8 cm', note='Any equivalent form.'),
              tf('A dilation preserves angle measures.', key=True, note='Similar shapes.'),
              mc('A dilation maps AB = 4 to A′B′ = 10. Factor?', ['2.5', '6', '0.4', '14'], note='10 ÷ 4.'),
              sa('What scale factor makes a 6 cm segment 6 cm long?', 'Factor:', key='1', note='Any equivalent form.'),
              tf('A dilation by 2 doubles the angles of a triangle.', key=False, note='Angles are unchanged.'),
          ], align='exact',
            why=why('the student does not know what the dilation step does.', 'the proof relies on matching one side and keeping angles.', 'states dilation properties.')),
          B('Use the angle sum to find a third angle', '8.G.A.5', [
              sa('A triangle has angles 47° and 88°. Find the third.', 'Angle:', key='45°', note='Any equivalent form.'),
              tf('If two angles of one triangle equal two angles of another, the third angles are equal.', key=True, note='Angle sum.'),
              mc('Triangles with angles 30°, 70°, x and 70°, 80°, y. Which is true?', ['x = 80, y = 30; the triangles are similar', 'x = 80, y = 30; not similar',
                                                                                        'x = 70, y = 30', 'x = 30, y = 80'],
                 note='180 - 100 = 80; 180 - 150 = 30; same angles.'),
              sa('Two angles of a triangle are equal and the third is 40°. Find the equal angles.', 'Angles:', key='70° each', note='Any equivalent form.'),
              tf('Knowing one angle of each triangle is enough for similarity.', key=False, note='Need two pairs.'),
          ], align='exact',
            why=why('the student does not see why two angles suffice.', 'the third angle follows from the sum.', 'computes third angles.')),
      ],
      f1=B('Establish the SAS and SSS similarity criteria', 'HSG-SRT.A.3', [
          proof('In △ABC and △DEF, DE/AB = DF/AC = k and ∠A ≅ ∠D. Prove that △ABC ~ △DEF.',
                method='Dilate △ABC by k, then use SAS congruence with △DEF.', key='△ABC ~ △DEF (SAS similarity).',
                note=PR + 'Essential: dilate by k: A′B′ = DE, A′C′ = DF, ∠A′ ≅ ∠A ≅ ∠D; SAS congruence; dilation then rigid motions map ABC onto DEF.'),
          sa('Triangles with sides 4, 6, 8 and 6, 9, 12. Similar? Which criterion?', 'Answer:', key='Yes, SSS similarity (ratio 1.5).', note='Form required: both.'),
          tf('Two triangles with two pairs of proportional sides and congruent included angles are similar.', key=True, note='SAS similarity.'),
          mc('Which is NOT a similarity criterion?', ['SSA', 'AA', 'SAS', 'SSS'], note='SSA does not determine shape.'),
          sa('△PQR: PQ = 5, PR = 7, ∠P = 40°. △XYZ: XY = 10, XZ = 14, ∠X = 40°. Similar? Factor?', 'Answer:', key='Yes (SAS similarity); factor 2', note='Form required: both.'),
      ], prog='same-course deepening', demand='Extend the transformation proof to the other similarity criteria (SAS and SSS).'),
      f2=B('Use AA to set up and solve problems', 'HSG-SRT.B.5', [
          sa('Two vertical poles are 3 m and 7 m tall. A wire from the top of each to the bottom of the other crosses at a point P. How high above the ground is P? (Use similar triangles.)', 'Height:',
             key='2.1 m', note='Any equivalent form. h = (3 · 7)/(3 + 7) = 2.1, from two pairs of AA-similar triangles.'),
          sa('In △ABC, D is on AB and E is on AC with ∠ADE ≅ ∠ACB. AD = 4, AE = 6, AB = 12. Find AC.', 'AC =', key='8', note='Any equivalent form. △ADE ~ △ACB (AA): AD/AC = AE/AB.'),
          tf('A mirror on the ground can be used to find a building\'s height with similar triangles.', key=True, note='Equal angles of incidence and reflection give AA.'),
          mc('Diagonals of trapezoid ABCD (AB ∥ DC) meet at E. AB = 12, DC = 4, AE = 9. Find EC.', ['3', '27', '6', '4'], note='△ABE ~ △CDE (AA): EC = 9 · 4/12.'),
          sa('A 2 m stick casts a 1.5 m shadow. A flagpole casts a 9 m shadow. How tall is the flagpole?', 'Height:', key='12 m', note='Any equivalent form.'),
      ], prog='cross-standard extension', demand='Use AA to identify similar triangles in problems and solve for lengths.',
        builds='A second extension of MAIN: FORWARD 1 proves more criteria; FORWARD 2 uses AA as a tool in applied problems.')),

    # ------------------------------------------------------------------ 42. SRT.B.4 triangle proportionality
    S('HSG-SRT.B.4', 'Prove the triangle proportionality theorem',
      target='Prove that a line parallel to one side of a triangle divides the other two sides proportionally', strand='core', covers=['SRT4-prop'],
      main=[
          proof('In △ABC, D is on AB and E is on AC with DE ∥ BC. Prove that AD/DB = AE/EC.', fig=PROP,
                method='Prove △ADE ~ △ABC by AA, write AD/AB = AE/AC, then rewrite with AB = AD + DB and AC = AE + EC.', key='AD/DB = AE/EC',
                note=PR + 'Essential: ∠A shared; ∠ADE ≅ ∠ABC (corresponding angles, DE ∥ BC); AA; AD/AB = AE/AC; so AB/AD = AC/AE, (AD + DB)/AD = (AE + EC)/AE, '
                     '1 + DB/AD = 1 + EC/AE, DB/AD = EC/AE, and AD/DB = AE/EC.'),
          sa('In the proof of the triangle proportionality theorem, the similarity gives AD/AB = AE/AC. Show the algebra that turns this into AD/DB = AE/EC.', 'Work:',
             key='Take reciprocals: AB/AD = AC/AE; write AB = AD + DB and AC = AE + EC; subtract 1 from both sides: DB/AD = EC/AE; take reciprocals: AD/DB = AE/EC.',
             note='Any correct algebraic route.'),
          proof('In △PQR, a line parallel to QR meets PQ at S and PR at T. Prove that PS/SQ = PT/TR.',
                method='AA similarity of △PST and △PQR, then the same algebra.', key='PS/SQ = PT/TR',
                note=PR + 'Essential: shared ∠P and corresponding angles give △PST ~ △PQR; then the proportion algebra.'),
          sa('A proof of the triangle proportionality theorem:\n1. ∠ADE ≅ ∠ABC  (?)\n2. ∠A ≅ ∠A  (?)\n3. △ADE ~ △ABC  (?)\n4. AD/AB = AE/AC  (?)\nGive the reasons.', 'Reasons:',
             key='1: corresponding angles (DE ∥ BC); 2: reflexive; 3: AA; 4: corresponding sides of similar triangles are proportional.', note='Any equivalent names for all four.'),
          mc('Which fact does the proof use first?', ['DE ∥ BC makes corresponding angles congruent', 'D and E are midpoints', 'DE = ½BC', 'AB = AC'],
             note='Only DE ∥ BC is given.'),
      ],
      back=[
          B('Use AA to show triangles are similar', 'HSG-SRT.A.3', [
              tf('Two pairs of congruent angles make two triangles similar.', key=True, note='AA.'),
              sa('DE ∥ BC in △ABC. Name two pairs of congruent angles in △ADE and △ABC.', 'Answer:', key='∠A ≅ ∠A and ∠ADE ≅ ∠ABC (or ∠AED ≅ ∠ACB)', note='Any two valid pairs.'),
              mc('△ADE ~ △ABC. Which ratio equals AD/AB?', ['AE/AC', 'DE/AB', 'AE/EC', 'DB/AB'], note='Corresponding sides.'),
              sa('△ADE ~ △ABC with AD = 3, AB = 9, AE = 4. Find AC.', 'AC =', key='12', note='Any equivalent form.'),
              tf('△ADE ~ △ABC means AD/DB = DE/BC.', key=False, note='DB is not a side of either triangle.'),
          ], align='exact',
            why=why('the student cannot get the similarity.', 'the theorem is proved from △ADE ~ △ABC.', 'uses AA and its ratios.')),
          B('Corresponding angles of parallel lines', 'HSG-CO.C.9', [
              tf('When a transversal crosses parallel lines, corresponding angles are congruent.', key=True, note='Theorem.'),
              sa('DE ∥ BC and AB is a transversal. Which angle corresponds to ∠ADE?', 'Angle:', key='∠ABC', note='Any equivalent form.'),
              mc('DE ∥ BC, AC a transversal. ∠AED corresponds to', ['∠ACB', '∠ABC', '∠BAC', '∠DEC'], note='Same position.'),
              sa('∠ABC = 65° and DE ∥ BC. Find ∠ADE.', 'Angle:', key='65°', note='Any equivalent form.'),
              tf('Corresponding angles are always supplementary.', key=False, note='Congruent for parallel lines.'),
          ], align='exact',
            why=why('the student cannot justify the congruent angles.', 'they come from DE ∥ BC.', 'names corresponding angles.')),
          B('Rewrite and solve proportions algebraically', '7.RP.A.2', [
              sa('If a/b = c/d, write the equation you get by taking reciprocals.', 'Answer:', key='b/a = d/c', note='Any equivalent answer.'),
              sa('Solve 4/(4 + x) = 6/15.', 'x =', key='6', note='Any equivalent form. 60 = 24 + 6x.'),
              mc('If (a + b)/a = (c + d)/c, then', ['b/a = d/c', 'a/b = c/d is false', 'a = c', 'b = d'], note='Subtract 1 from both sides.'),
              tf('3/5 = 6/10 implies 5/3 = 10/6.', key=True, note='Reciprocals.'),
              tf('(2 + 3)/2 = 5/2 implies 3/2 = 5/2.', key=False, note='Subtracting 1 gives 3/2 = 3/2.'),
          ], align='supporting',
            why=why('the student cannot convert the similarity proportion.', 'the theorem\'s proportion is a rewritten form.', 'manipulates proportions.')),
      ],
      f1=B('Prove that parallel lines cut transversals proportionally', 'HSG-SRT.B.4', [
          proof('Three parallel lines cut transversal t at A, B, C and transversal u at D, E, F (in order). Prove that AB/BC = DE/EF.',
                method='Draw segment AF; apply the triangle proportionality theorem in △ACF and in △FDA.', key='AB/BC = DE/EF',
                note=PR + 'Essential: AF crosses the middle line at G; in △ACF, BG ∥ CF so AB/BC = AG/GF; in △FAD, GE ∥ AD so FG/GA = FE/ED, so AG/GF = DE/EF; combine.'),
          sa('Three parallel lines cut one transversal into segments 4 and 6 and another into segments 5 and x. Find x.', 'x =', key='7.5', note='Any equivalent form.'),
          tf('Parallel lines that cut equal segments on one transversal cut equal segments on every transversal.', key=True, note='Ratio 1.'),
          mc('In △ABC, DE ∥ BC, AD = 5, DB = 3, AE = 7.5. Find EC.', ['4.5', '12.5', '5', '6'], note='5/3 = 7.5/EC.'),
          sa('Lots between parallel streets have frontages 30 m and 45 m on one avenue. On another avenue the first frontage is 40 m. Find the second.', 'Frontage:', key='60 m',
             note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Generalize the theorem to three parallel lines cutting any two transversals.'),
      f2=B('Prove the angle bisector theorem', 'HSG-SRT.B.5', [
          proof('In △ABC, the bisector of ∠A meets BC at D. Prove that BD/DC = AB/AC. (Draw the line through C parallel to AD, meeting line AB at E.)',
                method='Show △ACE is isosceles (AE = AC), then apply the triangle proportionality theorem in △BCE.', key='BD/DC = AB/AC',
                note=PR + 'Essential: ∠BAD ≅ ∠AEC (corresponding) and ∠DAC ≅ ∠ACE (alternate interior), and ∠BAD ≅ ∠DAC, so ∠AEC ≅ ∠ACE and AE = AC; in △BCE, AD ∥ EC '
                     'gives BD/DC = BA/AE = AB/AC.'),
          sa('In △ABC, the bisector of ∠A meets BC at D. AB = 9, AC = 6, BC = 10. Find BD and DC.', 'Answer:', key='BD = 6, DC = 4', note='Form required: both. BD/DC = 9/6.'),
          tf('The bisector of an angle of a triangle always meets the opposite side at its midpoint.', key=False, note='Only when the two sides are equal.'),
          mc('The bisector of ∠P in △PQR divides QR into 3 and 5. PQ = 6. Find PR.', ['10', '3.6', '8', '15'], note='3/5 = 6/PR.'),
          sa('Explain why the angle bisector theorem is a relationship that similarity or proportionality, not congruence, proves.', 'Answer:',
             key='It states a ratio of lengths, which comes from proportional segments (parallel lines), not from equal lengths.', note='Any reasonable explanation.'),
      ], prog='cross-standard extension', demand='Use the triangle proportionality theorem as a tool to prove a new relationship (the angle bisector theorem).',
        builds='A second extension of MAIN: FORWARD 1 generalizes the theorem; FORWARD 2 uses it to prove another theorem.')),
]

SETS += [
    # ------------------------------------------------------------------ 43. SRT.B.4 converse
    S('HSG-SRT.B.4', 'Prove the converse of the triangle proportionality theorem',
      target='Prove that a line dividing two sides of a triangle proportionally is parallel to the third side', strand='core', covers=['SRT4-converse'],
      main=[
          proof('In △ABC, D is on AB and E is on AC with AD/DB = AE/EC. Prove that DE ∥ BC.',
                method='Turn the given ratio into AD/AB = AE/AC, prove △ADE ~ △ABC by SAS similarity, then use congruent corresponding angles.', key='DE ∥ BC',
                note=PR + 'Essential: AD/DB = AE/EC gives AD/AB = AE/AC (add 1 to the reciprocals); ∠A shared; SAS similarity; ∠ADE ≅ ∠ABC; congruent corresponding angles '
                     'make DE ∥ BC (converse). Invalid: assuming DE ∥ BC to get the similarity.'),
          proof('In △PQR, S is on PQ and T is on PR with PS = 4, SQ = 6, PT = 6, TR = 9. Prove that ST ∥ QR.',
                method='Show PS/PQ = PT/PR, then SAS similarity and corresponding angles.', key='ST ∥ QR',
                note=PR + 'Essential: PS/PQ = 4/10 = 0.4 and PT/PR = 6/15 = 0.4; ∠P shared; SAS similarity; corresponding angles congruent; converse of corresponding angles theorem.'),
          sa('Show the algebra that turns AD/DB = AE/EC into AD/AB = AE/AC.', 'Work:',
             key='Reciprocals: DB/AD = EC/AE; add 1: (AD + DB)/AD = (AE + EC)/AE, so AB/AD = AC/AE; reciprocals: AD/AB = AE/AC.', note='Any correct route.'),
          mc('In △ABC, AD = 3, DB = 5, AE = 4.5, EC = 7.5 (D on AB, E on AC). Is DE ∥ BC?', ['Yes, because 3/5 = 4.5/7.5', 'No, because 3 ≠ 4.5', 'Yes, because D and E are midpoints',
                                                                                              'No, because 5 ≠ 7.5'],
             note='Both ratios equal 0.6, so the converse applies.'),
          tf('In △ABC, D is on AB and E is on AC with AD = 2, DB = 3, AE = 3, EC = 4. Then DE ∥ BC.', key=False, note='2/3 ≠ 3/4, so DE is not parallel to BC.'),
      ],
      back=[
          B('Use the triangle proportionality theorem', 'HSG-SRT.B.4', [
              sa('In △ABC, DE ∥ BC, AD = 6, DB = 4, AE = 9. Find EC.', 'EC =', key='6', note='Any equivalent form.'),
              tf('If DE ∥ BC in △ABC, then AD/DB = AE/EC.', key=True, note='The theorem.'),
              mc('DE ∥ BC, AD = 2, AB = 8, AC = 12. Find AE.', ['3', '6', '4', '9'], note='2/8 = AE/12.'),
              sa('State the converse of "If DE ∥ BC, then AD/DB = AE/EC."', 'Converse:', key='If AD/DB = AE/EC, then DE ∥ BC.', note='Any equivalent wording.'),
              tf('A theorem and its converse are always both true.', key=False, note='Some converses are false; this one must be proved.'),
          ], align='exact',
            why=why('the student does not know the forward theorem.', 'the converse reverses it.', 'applies and states the theorem.')),
          B('SAS similarity', 'HSG-SRT.A.3', [
              tf('Two pairs of proportional sides with congruent included angles make triangles similar.', key=True, note='SAS similarity.'),
              sa('△ADE and △ABC share ∠A, AD/AB = AE/AC = 0.4. Are they similar? Criterion?', 'Answer:', key='Yes, SAS similarity', note='Form required: both.'),
              mc('After △ADE ~ △ABC, which angle is congruent to ∠ADE?', ['∠ABC', '∠ACB', '∠BAC', '∠DEA'], note='D ↔ B.'),
              sa('Ratios 3/6 and 4/8 with a shared included angle: similar? Factor?', 'Answer:', key='Yes; factor 2 (or ½)', note='Form required: both.'),
              tf('SAS similarity needs the angle to be between the two pairs of sides.', key=True, note='Included angle.'),
          ], align='exact',
            why=why('the student cannot get the similarity from ratios.', 'the converse proof uses SAS similarity.', 'applies SAS similarity.')),
          B('Converse of the corresponding angles theorem', 'HSG-CO.C.9', [
              tf('Congruent corresponding angles make two lines parallel.', key=True, note='Converse.'),
              sa('∠ADE ≅ ∠ABC with transversal AB. What can you conclude about DE and BC?', 'Answer:', key='DE ∥ BC', note='Any equivalent form.'),
              mc('Which angles, if congruent, prove DE ∥ BC?', ['∠AED and ∠ACB', '∠ADE and ∠AED', '∠A and ∠B', '∠B and ∠C'], note='Corresponding angles along AC.'),
              sa('Corresponding angles measure 58° and 62°. Are the lines parallel?', 'Answer:', key='No', note='Any equivalent answer.'),
              tf('Vertical angles prove lines parallel.', key=False, note='They are always congruent.'),
          ], align='exact',
            why=why('the student cannot conclude parallel lines.', 'the last step of the proof.', 'applies the converse.')),
      ],
      f1=B('Use the converse to decide parallelism in figures', 'HSG-SRT.B.4', [
          sa('In △ABC, D is on AB with AD = 5, DB = 10, and E is on AC with AE = 4. How long must EC be for DE ∥ BC?', 'EC =', key='8', note='Any equivalent form.'),
          sa('In △PQR, S on PQ, T on PR: PS = x, SQ = 6, PT = 4, TR = 8. For which x is ST ∥ QR?', 'x =', key='3', note='Any equivalent form.'),
          tf('The midsegment theorem\'s parallel part is a special case of the converse (ratio 1 : 1).', key=True, note='AD/DB = AE/EC = 1.'),
          mc('Points divide two sides in ratios 2 : 3 and 4 : 6. The segment joining them is', ['parallel to the third side', 'perpendicular to the third side',
                                                                                            'half the third side', 'not parallel to the third side'],
             note='2 : 3 = 4 : 6.'),
          sa('In △ABC, D is on AB with AD : DB = 1 : 2 and DE ∥ BC with E on AC. Find DE : BC.', 'Ratio:', key='1 : 3', note='Any equivalent form. AD : AB = 1 : 3.'),
      ], prog='same-course deepening', demand='Use the converse to find unknown lengths that force parallelism, and connect it to the midsegment theorem.'),
      f2=B('Prove the trapezoid midsegment theorem', 'HSG-SRT.B.5', [
          proof('Trapezoid ABCD has AB ∥ DC. M and N are the midpoints of legs AD and BC. Prove that MN ∥ AB and MN = ½(AB + DC).',
                method='Draw diagonal AC; let P be the midpoint of AC; use the midsegment theorem (or the converse) in △ACD and △ABC.', key='MN ∥ AB and MN = ½(AB + DC)',
                note=PR + 'Essential: in △ADC, MP ∥ DC and MP = ½DC; in △ABC, PN ∥ AB and PN = ½AB; AB ∥ DC so MP and PN are both parallel to AB through P, so M, P, N are collinear; MN = ½(AB + DC).'),
          sa('A trapezoid has bases 10 and 16. Find the length of the segment joining the midpoints of the legs.', 'Length:', key='13', note='Any equivalent form.'),
          tf('The midsegment of a trapezoid is parallel to both bases.', key=True, note='Proved above.'),
          mc('A trapezoid\'s midsegment is 12 and one base is 9. Find the other base.', ['15', '3', '21', '6'], note='(9 + b)/2 = 12.'),
          sa('Explain why M, P, N are on one line in the trapezoid midsegment proof.', 'Answer:', key='MP and PN are both parallel to the bases through P, and only one line through P is parallel to them.',
             note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Combine the converse with midsegments to prove a new theorem about trapezoids.',
        builds='Builds on FORWARD 1: the parallel conditions found there combine into the trapezoid midsegment proof.')),

    # ------------------------------------------------------------------ 44. SRT.B.4 Pythagorean
    S('HSG-SRT.B.4', 'Prove the Pythagorean Theorem using similar triangles',
      target='Prove the Pythagorean Theorem using triangle similarity (the altitude to the hypotenuse)', strand='core', covers=['SRT4-pythag'],
      main=[
          proof('Right triangle ABC has the right angle at C, legs a = BC, b = AC, and hypotenuse c = AB. The altitude from C meets AB at D. Prove that a² + b² = c².', fig=ALT,
                method='Show △ACD ~ △ABC and △CBD ~ △ABC (AA), write two proportions, and add.', key='a² + b² = c²',
                note=PR + 'Essential: △ADC ~ △ACB (shared ∠A, right angles), so AD/AC = AC/AB and b² = c · AD; △CDB ~ △ACB (shared ∠B), so BD/BC = BC/AB and a² = c · BD; '
                     'adding, a² + b² = c(AD + BD) = c · c = c². Invalid: assuming a² + b² = c² anywhere; using the distance formula (it depends on the theorem).'),
          sa('In the similarity proof of the Pythagorean Theorem, why is △ADC ~ △ACB?', 'Answer:', key='They share ∠A and both have a right angle (at D and at C), so AA applies.', fig=ALT,
             note='Any equivalent answer naming both pairs of angles.'),
          sa('In the proof, b² = c · AD and a² = c · BD. Show how these give a² + b² = c².', 'Work:', key='a² + b² = c · BD + c · AD = c(BD + AD) = c · c = c², since AD + DB = AB = c.',
             note='Any correct algebra, including why AD + BD = c (D is between A and B).'),
          proof('A right triangle has legs 6 and 8, and the altitude to the hypotenuse divides it into parts x and y. Use similar triangles (not the Pythagorean Theorem) to find x and y, and show that the hypotenuse is 10.',
                method='Use 6² = c · x and 8² = c · y with x + y = c.', key='c = 10, x = 3.6, y = 6.4',
                note=PR + 'Essential: from similarity 36 = cx and 64 = cy; adding, 100 = c(x + y) = c², so c = 10, x = 3.6, y = 6.4.'),
          mc('Which pair of triangles is NOT similar in the figure of a right triangle with the altitude to the hypotenuse?', ['None; all three triangles are similar',
                                                                                                                                 '△ACD and △ABC', '△BCD and △ABC', '△ACD and △CBD'],
             note='All three triangles are similar (AA).'),
      ],
      back=[
          B('Show triangles similar with AA', 'HSG-SRT.A.3', [
              tf('Two right triangles that share an acute angle are similar.', key=True, note='AA.'),
              sa('△ADC and △ACB: name two pairs of congruent angles.', 'Answer:', key='∠A ≅ ∠A; ∠ADC ≅ ∠ACB (right angles)', note='Any two valid pairs.'),
              mc('△ADC ~ △ACB. Which ratio equals AD/AC?', ['AC/AB', 'DC/AB', 'AD/AB', 'CB/AC'], note='AD ↔ AC, AC ↔ AB.'),
              sa('If △ADC ~ △ACB with AD = 4 and AB = 9, find AC.', 'AC =', key='6', note='Any equivalent form. AC² = AD · AB = 36.'),
              tf('Similar triangles must be the same size.', key=False, note='Only the shape matches.'),
          ], align='exact',
            why=why('the student cannot see the three similar triangles.', 'the proof is built on them.', 'identifies AA in the altitude figure.')),
          B('Cross-multiply proportions', '7.RP.A.2', [
              sa('From AD/AC = AC/AB, write an equation without fractions.', 'Answer:', key='AC² = AD · AB', note='Any equivalent equation.'),
              sa('Solve 4/x = x/9 for x > 0.', 'x =', key='6', note='Any equivalent form.'),
              mc('If p/q = q/r, then', ['q² = pr', 'p² = qr', 'r² = pq', 'p = r'], note='Cross-multiply.'),
              tf('From a/b = b/c we get b² = ac.', key=True, note='Cross-multiply.'),
              tf('From x/5 = 5/x we get x = 5 only.', key=False, note='x² = 25, so x = ±5 (x = 5 for a length).'),
          ], align='supporting',
            why=why('the student cannot turn proportions into products.', 'the proof uses b² = c · AD.', 'cross-multiplies.')),
          B('Explain a proof of the Pythagorean Theorem informally', '8.G.B.6', [
              tf('The Pythagorean Theorem says a² + b² = c² for every right triangle with legs a, b and hypotenuse c.', key=True, note='Statement.'),
              sa('Name a way to show the theorem by rearranging area pieces.', 'Answer:', key='Arrange four copies of the triangle inside a square of side a + b (the leftover is c², or a² + b²).',
                 note='Any valid area argument.'),
              mc('Which triangle satisfies the theorem?', ['5, 12, 13', '5, 6, 7', '2, 3, 4', '6, 7, 9'], note='25 + 144 = 169.'),
              sa('Legs 9 and 12. Hypotenuse?', 'Hypotenuse:', key='15', note='Any equivalent form.'),
              tf('Checking the theorem with three triangles proves it for all right triangles.', key=False, note='Examples are not proofs.'),
          ], align='exact',
            why=why('the student does not know what is being proved.', 'the proof must establish this statement in general.', 'states and applies the theorem.')),
      ],
      f1=B('Use the geometric mean relationships in a right triangle', 'HSG-SRT.B.5', [
          sa('In right triangle ABC with altitude CD to hypotenuse AB, AD = 4 and DB = 9. Find CD.', 'CD =', key='6', note='Any equivalent form. CD² = AD · DB.'),
          proof('In right triangle ABC with right angle at C and altitude CD, prove that CD² = AD · DB.', method='Show △ACD ~ △CBD and write a proportion.', key='CD² = AD · DB',
                note=PR + 'Essential: △ADC ~ △CDB (AA: right angles at D, and ∠A ≅ ∠BCD since both are complementary to ∠B); AD/CD = CD/DB.'),
          tf('The altitude to the hypotenuse is the geometric mean of the two parts of the hypotenuse.', key=True, note='CD² = AD · DB.'),
          mc('AD = 2 and AB = 8 in the altitude figure. Find AC.', ['4', '16', '2√2', '6'], note='AC² = AD · AB = 16.'),
          sa('A right triangle\'s altitude to the hypotenuse is 12 and one part of the hypotenuse is 9. Find the other part.', 'Part:', key='16', note='Any equivalent form. 144 = 9x.'),
      ], prog='cross-standard extension', demand='Derive and use further relationships (geometric means) from the same similar triangles.'),
      f2=B('The Law of Cosines as a generalization of the Pythagorean Theorem', 'HSG-SRT.D.10', [
          sa('For a triangle with sides a, b, c and angle C opposite c, the Law of Cosines says c² = a² + b² - 2ab cos C. What does it become when C = 90°?', 'Answer:',
             key='c² = a² + b² (the Pythagorean Theorem), since cos 90° = 0.', note='Any equivalent answer.'),
          sa('A triangle has sides 5 and 8 with a 60° angle between them. Find the third side.', 'Side:', key='7', note='Any equivalent form. 25 + 64 - 40 = 49.'),
          tf('If a² + b² > c², the angle opposite c is acute.', key=True, note='Then cos C > 0.'),
          mc('A triangle has sides 4, 5, 7. The largest angle is', ['obtuse', 'right', 'acute', 'impossible to tell'], note='16 + 25 = 41 < 49.'),
          sa('Use the converse idea: is a triangle with sides 7, 24, 25 right, acute, or obtuse?', 'Answer:', key='Right (49 + 576 = 625)', note='Form required: the classification with the check.'),
      ], prog='cross-standard extension', demand='See the theorem as the C = 90° case of a general relationship, and classify triangles by comparing squares.',
        builds='A second extension of MAIN: FORWARD 1 extracts more right-triangle relationships; FORWARD 2 generalizes to all triangles (advanced strand).')),

    # ------------------------------------------------------------------ 45. SRT.B.5 solve with similarity
    S('HSG-SRT.B.5', 'Use similarity criteria to solve problems in geometric figures',
      target='Identify similar triangles with a criterion and use them to find unknown lengths in figures and situations', strand='core', covers=['SRT5-solve'],
      main=[
          sa('In △ABC, D is on AB and E is on AC with DE ∥ BC. AD = 6, DB = 9, DE = 8. Find BC. Name the criterion you used for similar triangles.', 'Answer:',
             key='BC = 20; △ADE ~ △ABC by AA.', note='Form required: the length and the criterion. 6/15 = 8/BC.'),
          sa('A lamppost lights a student who is 1.6 m tall and stands 3 m from the post. The student\'s shadow is 2 m long, measured away from the post. How tall is the lamppost? Name the similarity criterion you used.',
             'Answer:', key='4 m; AA (the shared angle at the tip of the shadow, and two right angles).',
             note='Form required: the height and the criterion. The tip of the shadow is 5 m from the post: 1.6/2 = h/5.'),
          sa('Two triangles: △PQR with PQ = 8, QR = 12, ∠Q = 50°; △STU with ST = 6, TU = 9, ∠T = 50°. Are they similar? If so, find the ratio of their perimeters.', 'Answer:',
             key='Yes, SAS similarity (8/6 = 12/9 = 4/3); perimeter ratio 4 : 3.', note='Form required: the criterion and the ratio.'),
          mc('A surveyor finds a river\'s width w with similar right triangles: legs 12 m and 18 m on the small triangle, 12 m corresponding to 40 m on the large one. What is w (the side matching 18 m)?',
             ['60 m', '26.7 m', '46 m', '54 m'], note='18 · 40/12 = 60.'),
          tf('If two triangles have sides 3, 5, 7 and 6, 10, 15, they are similar.', key=False, note='15/7 ≠ 2.'),
      ],
      back=[
          B('Similarity criteria: AA, SAS, SSS', 'HSG-SRT.A.3', [
              sa('Which criterion uses two pairs of congruent angles?', 'Answer:', key='AA', note='Any equivalent form.'),
              sa('Sides 2, 3, 4 and 4, 6, 8. Criterion?', 'Answer:', key='SSS similarity', note='Any equivalent form.'),
              mc('Which information is enough for similarity?', ['Two pairs of congruent angles', 'One pair of congruent angles', 'One pair of proportional sides', 'Two sides of each triangle'],
                 note='AA.'),
              tf('SAS similarity requires the congruent angle to be between the proportional sides.', key=True, note='Included angle.'),
              tf('Any two right triangles are similar.', key=False, note='They need another congruent angle.'),
          ], align='exact',
            why=why('the student cannot justify the similarity.', 'each problem starts by naming a criterion.', 'names criteria.')),
          B('Solve proportions', '7.RP.A.2', [
              sa('Solve 6/15 = 8/x.', 'x =', key='20', note='Any equivalent form.'),
              sa('Solve 1.6/2 = h/5.', 'h =', key='4', note='Any equivalent form.'),
              mc('Solve 12/40 = 18/x.', ['60', '26.7', '46', '54'], note='x = 18 · 40/12.'),
              tf('3/4 = 9/12', key=True, note='Equal ratios.'),
              tf('5/8 = 10/14', key=False, note='10/16 would be equal.'),
          ], align='exact',
            why=why('the student cannot finish the computation.', 'unknown lengths come from proportions.', 'solves proportions.')),
          B('Identify corresponding sides in overlapping triangles', 'HSG-SRT.A.2', [
              sa('△ADE ~ △ABC. Which side of △ABC corresponds to DE?', 'Side:', key='BC', note='Any equivalent form.'),
              tf('In △ADE ~ △ABC, side AD corresponds to side AB.', key=True, note='Correspondence.'),
              mc('In the DE ∥ BC figure, the side of the big triangle matching AD is', ['AB', 'DB', 'BC', 'AC'], note='Whole side, not the piece DB.'),
              sa('AD = 6, DB = 9. What is AB?', 'AB =', key='15', note='Any equivalent form.'),
              tf('In △ADE ~ △ABC, DB corresponds to DE.', key=False, note='DB is not a side of △ADE.'),
          ], align='supporting',
            why=why('the student pairs a piece of a side with a whole side.', 'proportions must use corresponding whole sides.', 'matches corresponding sides.')),
      ],
      f1=B('Solve multistep problems with two or more pairs of similar triangles', 'HSG-SRT.B.5', [
          sa('Trapezoid ABCD has AB ∥ DC, AB = 15, DC = 10. The diagonals meet at E, and AC = 20. Find AE and EC.', 'Answer:', key='AE = 12, EC = 8', note='Form required: both. AE/EC = 15/10.'),
          sa('A pinhole camera: an object 2 m tall is 8 m from the pinhole; the image is 5 cm from the pinhole on the screen. How tall is the image?', 'Height:', key='1.25 cm', note='Any equivalent form.'),
          tf('In a figure with two pairs of similar triangles, one ratio found in the first pair can be reused in the second.', key=True, note='Shared sides link them.'),
          mc('In △ABC, DE ∥ BC with AD = 2, DB = 6; and FG ∥ BC farther down with AF = 5. If BC = 16, find FG.', ['10', '4', '8', '12'], note='FG/BC = AF/AB = 5/8.'),
          sa('Using a mirror on the ground, Ana (eyes 1.5 m high) stands 2 m from the mirror and sees the top of a tree 12 m beyond the mirror. How tall is the tree?', 'Height:', key='9 m',
             note='Any equivalent form. 1.5/2 = h/12.'),
      ], prog='same-course deepening', demand='Solve problems that need two linked similarities or a hidden pair of similar triangles.'),
      f2=B('Solve similarity problems with algebra (unknowns on both sides)', 'HSG-SRT.B.5', [
          sa('In △ABC, DE ∥ BC with AD = x, DB = 6, AE = 4, EC = x + 2. Find x.', 'x =', key='4', note='Any equivalent form. x(x + 2) = 24, x > 0.'),
          sa('Similar triangles have corresponding sides x + 1 and 2x - 3 with scale factor 1.5 (larger to smaller is 2x - 3 to x + 1). Find x.', 'x =', key='9',
             note='Any equivalent form. 2x - 3 = 1.5(x + 1).'),
          tf('A proportion with the unknown in two places can lead to a quadratic equation.', key=True, note='Cross-multiplying gives products.'),
          mc('In the altitude figure of a right triangle, AD = x, DB = x + 5, CD = 6. Find x.', ['4', '9', '6', '3'], note='x(x + 5) = 36.'),
          sa('Two similar rectangles: the first is 4 by x, the second is x by 9. Find x.', 'x =', key='6', note='Any equivalent form. 4/x = x/9.'),
      ], prog='same-course deepening', demand='Set up and solve similarity problems whose unknowns lead to quadratic equations (rejecting invalid roots).',
        builds='Builds on FORWARD 1: the same linked similarities, now with algebraic unknowns.')),
]
