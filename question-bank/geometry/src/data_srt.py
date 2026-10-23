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

KITE = gd({'A': (0, 2.4), 'B': (-1.6, 0.6), 'C': (0, -1.8), 'D': (1.6, 0.6), 'E': (0, 0.6)},
          [('poly', ['A', 'B', 'C', 'D']), ('seg', 'A', 'C', {'dash': True}), ('seg', 'B', 'D', {'dash': True}),
           ('seg', 'A', 'B', {'ticks': 1}), ('seg', 'A', 'D', {'ticks': 1}), ('seg', 'C', 'B', {'ticks': 2}), ('seg', 'C', 'D', {'ticks': 2})], h=220, lab={'E': 'ne'},
          desc='Kite ABCD with AB = AD (one tick each) and CB = CD (two ticks each). Diagonals AC and BD are dashed and cross at E.')

# trigonometry values (computed, not typed)
T50 = [(12, 35), (20, 52), (9, 28), (15, 61), (30, 23)]

SETS += [
    # ------------------------------------------------------------------ 46. SRT.B.5 prove with congruence
    S('HSG-SRT.B.5', 'Use congruence criteria to prove relationships in figures',
      target='Prove a relationship in a geometric figure by first proving two triangles congruent with a criterion', strand='core', covers=['SRT5-congprove'],
      main=[
          proof('Kite ABCD has AB = AD and CB = CD. Its diagonals meet at E. Prove that AC ⊥ BD.', fig=KITE,
                method='Prove △ABC ≅ △ADC (SSS) to get ∠BAE ≅ ∠DAE; then △ABE ≅ △ADE (SAS); then the angles at E form a congruent linear pair.', key='AC ⊥ BD',
                note=PR + 'Essential: SSS (AB = AD, CB = CD, AC shared); ∠BAC ≅ ∠DAC; SAS on △ABE and △ADE (AE shared); ∠AEB ≅ ∠AED, a linear pair, so 90°. '
                     'Alternative: A and C are each equidistant from B and D, so AC is the perpendicular bisector of BD.'),
          proof('Segments AB and CD bisect each other at M. Prove that AC ∥ DB.',
                method='Prove △AMC ≅ △BMD (SAS with vertical angles), then use congruent alternate interior angles.', key='AC ∥ DB',
                note=PR + 'Essential: AM = BM, CM = DM (bisect), ∠AMC ≅ ∠BMD (vertical); SAS; ∠CAM ≅ ∠DBM; these are alternate interior angles for AC and DB with transversal AB; converse.'),
          proof('Point P is on the bisector of ∠ABC. PD ⊥ BA at D and PE ⊥ BC at E. Prove that PD = PE.',
                method='Prove △PBD ≅ △PBE by AAS.', key='PD = PE',
                note=PR + 'Essential: ∠PBD ≅ ∠PBE (bisector), ∠PDB ≅ ∠PEB (right angles), PB shared; AAS; PD = PE.'),
          proof('In △ABC, AB = AC. M is the midpoint of BC. Prove that AM bisects ∠BAC and AM ⊥ BC.',
                method='Prove △ABM ≅ △ACM (SSS), then use corresponding angles.', key='∠BAM ≅ ∠CAM and AM ⊥ BC',
                note=PR + 'Essential: SSS; ∠BAM ≅ ∠CAM (bisects); ∠AMB ≅ ∠AMC form a linear pair, so each is 90°.'),
          mc('To prove that two segments in a figure are congruent, the most common first step is to', ['prove two triangles containing them are congruent', 'measure them carefully',
                                                                                                         'assume they are congruent', 'show the figure is symmetric by looking'],
             note='Then use corresponding parts.'),
      ],
      back=[
          B('Choose and apply SSS, SAS, ASA, AAS', 'HSG-CO.B.8', [
              sa('Two triangles share a side and have two more pairs of congruent sides. Criterion?', 'Criterion:', key='SSS', note='Any equivalent form.'),
              sa('Two angles and a non-included side match. Criterion?', 'Criterion:', key='AAS', note='Any equivalent form.'),
              mc('Which pair of facts plus a shared side gives SAS?', ['A pair of congruent sides and the congruent included angles', 'Two pairs of congruent angles',
                                                                     'Two pairs of congruent sides not including the angle', 'Nothing more is needed'], note='Included angle.'),
              tf('A shared side is a valid pair for any criterion.', key=True, note='Reflexive.'),
              tf('AAA proves congruence.', key=False, note='Only similarity.'),
          ], align='exact',
            why=why('the student cannot pick a criterion.', 'every proof starts with a congruence.', 'chooses criteria.')),
          B('Find hidden parts: shared sides, vertical angles, right angles', 'HSG-CO.C.9', [
              sa('Segments AB and CD cross at M. Which angles are vertical to ∠AMC?', 'Angle:', key='∠BMD', note='Any equivalent form.'),
              tf('Perpendicular lines give congruent right angles.', key=True, note='All 90°.'),
              mc('Which is a hidden fact in figures where two triangles share a side?', ['The shared side is congruent to itself', 'All angles are equal', 'The triangles are right', 'Nothing'],
                 note='Reflexive property.'),
              sa('A bisector divides ∠ABC into which two congruent angles?', 'Answer:', key='∠ABP and ∠PBC (for bisector ray BP)', note='Any equivalent answer.'),
              tf('Vertical angles are supplementary.', key=False, note='They are congruent.'),
          ], align='exact',
            why=why('the student misses parts not stated in the problem.', 'proofs depend on them.', 'finds hidden congruent parts.')),
          B('Use corresponding parts to finish a proof', 'HSG-CO.B.7', [
              sa('△ABC ≅ △ADC. Which angle corresponds to ∠BAC?', 'Angle:', key='∠DAC', note='Any equivalent form.'),
              tf('Once triangles are congruent, all corresponding parts are congruent.', key=True, note='Definition.'),
              mc('△PBD ≅ △PBE. Which conclusion follows?', ['PD = PE', 'PB = PD', 'BD = PE', '∠D ≅ ∠B'], note='Corresponding sides.'),
              sa('Two congruent angles form a linear pair. Each measures', 'Measure:', key='90°', note='Any equivalent form.'),
              tf('Corresponding parts can be used before the triangles are proved congruent.', key=False, note='Only after.'),
          ], align='exact',
            why=why('the student stops after the congruence.', 'the goal is a relationship about specific parts.', 'states the final conclusion.')),
      ],
      f1=B('Prove relationships that need two congruences in a row', 'HSG-SRT.B.5', [
          proof('In quadrilateral ABCD, AB = CD and AD = CB. Diagonals AC and BD meet at E. Prove that E is the midpoint of AC.',
                method='Prove △ABC ≅ △CDA (SSS) to get parallel sides, then △ABE ≅ △CDE (ASA).', key='AE = CE',
                note=PR + 'Essential: SSS gives alternate interior angles congruent (AB ∥ DC); then ASA (or AAS) for △ABE and △CDE gives AE = CE.'),
          proof('In the figure, AB = AC and BD = CE, with D on AB and E on AC. Prove that BE = CD.',
                method='Show AD = AE, then prove △ABE ≅ △ACD by SAS (shared ∠A).', key='BE = CD',
                note=PR + 'Essential: AD = AB - BD = AC - CE = AE; ∠A shared; AB = AC; SAS; corresponding sides.'),
          tf('Some proofs need one congruence to find a part used in a second congruence.', key=True, note='Chained congruences.'),
          mc('In a two-step proof, the first congruence gives ∠1 ≅ ∠2. This is used to', ['supply a pair of parts for the second congruence', 'end the proof', 'restart', 'measure'],
             note='Chaining.'),
          sa('Explain why you cannot use corresponding parts of the second pair of triangles before proving them congruent.', 'Answer:',
             key='That would assume what must be proved (circular reasoning).', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Prove relationships that need a chain of two congruences.'),
      f2=B('Decide which given data are sufficient for a proof, and supply a missing condition', 'HSG-SRT.B.5', [
          sa('In △PQR and △PSR (sharing PR), PQ = PS. What one more fact would prove ∠QPR ≅ ∠SPR? Explain.', 'Answer:',
             key='QR = SR (then SSS gives the congruence and the angles correspond).', note='Any sufficient condition with explanation (∠PRQ ≅ ∠PRS would give SSA, which is not enough).'),
          sa('A student claims a kite\'s diagonals bisect each other. Prove or disprove.', 'Answer:',
             key='False in general: only the diagonal BD is bisected (by AC); AC is bisected only if the kite is a rhombus. Example: A(0, 3), B(-1, 0), C(0, -1), D(1, 0).',
             note='Any valid counterexample or explanation.'),
          tf('Given AB = DE, BC = EF, and ∠C ≅ ∠F, the triangles must be congruent.', key=False, note='SSA.'),
          mc('Given ∠A ≅ ∠D and AB = DE in △ABC and △DEF, which extra fact gives ASA?', ['∠B ≅ ∠E', '∠C ≅ ∠F', 'BC = EF', 'AC = DF'], note='The angle at the other end of AB.'),
          sa('Given AB = DE and AC = DF, name an angle condition that guarantees congruence.', 'Answer:', key='∠A ≅ ∠D (the included angle)', note='Form required: the included angle.'),
      ], prog='same-course deepening', demand='Judge sufficiency of data and identify a missing condition, with justification.',
        builds='Builds on FORWARD 1: before chaining congruences, decide whether each step has enough data.')),

    # ------------------------------------------------------------------ 47. SRT.B.5 prove with similarity
    S('HSG-SRT.B.5', 'Use similarity criteria to prove relationships in figures',
      target='Prove a relationship (such as a product or proportion of lengths) by first proving two triangles similar', strand='core', covers=['SRT5-simprove'],
      main=[
          proof('In △ABC, DE ∥ BC with D on AB and E on AC. Prove that AD · AC = AE · AB.', fig=PROP,
                method='Prove △ADE ~ △ABC (AA), write the proportion, and cross-multiply.', key='AD · AC = AE · AB',
                note=PR + 'Essential: AA (shared ∠A; corresponding angles); AD/AB = AE/AC; cross-multiply.'),
          proof('Chords AB and CD of a circle meet at P, and ∠BAD ≅ ∠BCD (given). Prove that PA · PB = PC · PD.',
                method='Prove △PAD ~ △PCB (AA: the given angles and vertical angles), then cross-multiply.', key='PA · PB = PC · PD',
                note=PR + 'Essential: ∠PAD ≅ ∠PCB (given), ∠APD ≅ ∠CPB (vertical); AA; PA/PC = PD/PB; cross-multiply.'),
          proof('In right triangle ABC (right angle at C), CD is the altitude to AB. Prove that AC · BC = AB · CD.', fig=ALT,
                method='Prove △ACB ~ △ADC (or △CDB) and use the ratio of corresponding sides.', key='AC · BC = AB · CD',
                note=PR + 'Essential: △ADC ~ △ACB (AA); DC/CB = AC/AB; cross-multiply. Alternative: both products equal twice the area.'),
          proof('In trapezoid ABCD with AB ∥ DC, the diagonals AC and BD meet at E. Prove that AE/EC = AB/DC.',
                method='Prove △ABE ~ △CDE by AA (alternate interior angles or vertical angles).', key='AE/EC = AB/DC',
                note=PR + 'Essential: ∠EAB ≅ ∠ECD and ∠EBA ≅ ∠EDC (alternate interior, AB ∥ DC); AA; corresponding sides.'),
          mc('To prove a product relationship such as PA · PB = PC · PD, which is the usual strategy?', ['Find two similar triangles whose sides appear in the products', 'Measure the four lengths',
                                                                                                      'Assume the product is true', 'Use the Pythagorean Theorem only'],
             note='A proportion from similar triangles becomes a product by cross-multiplying.'),
      ],
      back=[
          B('Prove triangles similar with AA', 'HSG-SRT.A.3', [
              tf('Vertical angles can be one pair of congruent angles in an AA proof.', key=True, note='They are congruent.'),
              sa('Two triangles share ∠A and have another pair of congruent angles. Criterion?', 'Criterion:', key='AA', note='Any equivalent form.'),
              mc('Parallel lines in a figure usually supply', ['congruent corresponding or alternate interior angles', 'equal side lengths', 'right angles', 'a scale factor'], note='Angle pairs.'),
              sa('△PAD ~ △PCB. Which side of △PCB corresponds to PA?', 'Side:', key='PC', note='Any equivalent form.'),
              tf('Similarity requires all three pairs of sides to be equal.', key=False, note='Proportional, not equal.'),
          ], align='exact',
            why=why('the student cannot establish the similarity.', 'each proof starts with AA.', 'applies AA.')),
          B('Turn a proportion into a product', '7.RP.A.2', [
              sa('From a/b = c/d, write the product relationship.', 'Answer:', key='ad = bc', note='Any equivalent form.'),
              sa('From PA/PC = PD/PB, write the product relationship.', 'Answer:', key='PA · PB = PC · PD', note='Any equivalent form.'),
              mc('If x/3 = 4/6, then', ['6x = 12', '3x = 24', 'x = 8', '4x = 18'], note='Cross-multiply.'),
              tf('a/b = c/d implies ab = cd.', key=False, note='It implies ad = bc.'),
              tf('2/5 = 6/15 implies 2 · 15 = 5 · 6.', key=True, note='30 = 30.'),
          ], align='exact',
            why=why('the student cannot rewrite the proportion.', 'the result is a product.', 'cross-multiplies.')),
          B('Match corresponding sides of similar triangles', 'HSG-SRT.A.2', [
              sa('△ADE ~ △ABC. Write the proportion with AD, AB, AE, AC.', 'Answer:', key='AD/AB = AE/AC', note='Any equivalent proportion.'),
              tf('In △ABE ~ △CDE, AB corresponds to CD.', key=True, note='A ↔ C, B ↔ D.'),
              mc('△ACB ~ △ADC. Which side corresponds to CB?', ['DC', 'AD', 'AC', 'AB'], note='A ↔ A, C ↔ D, B ↔ C, so CB ↔ DC.'),
              sa('△XYZ ~ △UVW. Write all three equal ratios.', 'Answer:', key='XY/UV = YZ/VW = XZ/UW', note='Any equivalent form.'),
              tf('Any two sides of similar triangles are proportional.', key=False, note='Only corresponding sides.'),
          ], align='exact',
            why=why('the student pairs the wrong sides.', 'the product must use corresponding sides.', 'writes correct proportions.')),
      ],
      f1=B('Use proved product relationships to compute', 'HSG-SRT.B.5', [
          sa('Chords AB and CD meet at P with PA = 4, PB = 9, PC = 6. Find PD.', 'PD =', key='6', note='Any equivalent form. 4 · 9 = 6 · PD.'),
          sa('In right triangle ABC (right angle at C), AC = 6, BC = 8, AB = 10. Find the altitude CD to AB.', 'CD =', key='4.8', note='Any equivalent form. 6 · 8 = 10 · CD.'),
          tf('If two chords meet inside a circle, the products of their segments are equal.', key=True, note='Proved by similarity.'),
          mc('Trapezoid diagonals: AB = 18, DC = 12, AE = 9. Find EC.', ['6', '13.5', '4', '8'], note='AE/EC = 18/12.'),
          sa('DE ∥ BC in △ABC with AD = 3, AB = 9, AC = 12. Find AE.', 'AE =', key='4', note='Any equivalent form. AD · AC = AE · AB.'),
      ], prog='same-course deepening', demand='Apply the proved relationships as tools to compute unknown lengths.'),
      f2=B('Prove relationships in circles with similar triangles', 'HSG-C.A.2', [
          proof('From point P outside a circle, a tangent touches the circle at T and a secant meets it at A and B (A between P and B). Given ∠PTA ≅ ∠PBT, prove that PT² = PA · PB.',
                method='Prove △PTA ~ △PBT (AA), then cross-multiply.', key='PT² = PA · PB',
                note=PR + 'Essential: shared ∠P and the given angles; AA; PT/PB = PA/PT; cross-multiply.'),
          sa('A tangent segment from P is 8 and the secant from P has outer part 4. Find the whole secant length.', 'Length:', key='16', note='Any equivalent form. 64 = 4 · PB.'),
          tf('Two secants from an outside point satisfy PA · PB = PC · PD.', key=True, note='Similar triangles.'),
          mc('From P, secants meet a circle at A, B and at C, D with PA = 3, PB = 12, PC = 4. Find PD.', ['9', '16', '1', '7'], note='36 = 4 · PD.'),
          sa('Explain why the angle facts used in these circle proofs depend on inscribed angles.', 'Answer:', key='Angles that intercept the same arc are congruent (inscribed angle theorem), which supplies the AA pairs.',
             note='Any reasonable answer.'),
      ], prog='cross-standard extension', demand='Use similarity proofs in circle configurations (tangents and secants).',
        builds='Builds on FORWARD 1: the chord product extends to tangents and secants.')),
]


def trig_side(i, L, A):
    """Q: hypotenuse L, angle A at the base: opposite leg."""
    return d1(L * sind(A))


SETS += [
    # ------------------------------------------------------------------ 48. SRT.C.6 trig ratios from similarity
    S('HSG-SRT.C.6', 'Understand trigonometric ratios as properties of an angle, by similarity',
      target='Explain why right-triangle side ratios depend only on the acute angle (by similarity) and define sine, cosine, and tangent from them',
      strand='core', covers=['SRT6-ratios'],
      main=[
          proof('Right triangles ABC and DEF have right angles at C and F and ∠A ≅ ∠D. Explain why BC/AB = EF/DE.',
                method='Use AA similarity, then the proportion of corresponding sides, rearranged.', key='BC/AB = EF/DE',
                note=PR + 'Essential: right angles and ∠A ≅ ∠D give AA similarity; BC/EF = AB/DE; rearranging gives BC/AB = EF/DE. So the ratio depends only on the angle.'),
          sa('Two right triangles each have a 30° angle. In one, the side opposite 30° is 4 and the hypotenuse is 8. In the other, the hypotenuse is 15. Find the side opposite 30°, and explain.', 'Answer:',
             key='7.5; the triangles are similar (AA), so opposite/hypotenuse = 4/8 = ½ in both.', note='Form required: the length and the similarity reason.'),
          sa('In right triangle PQR, the right angle is at R, PR = 5, QR = 12, PQ = 13. Write sin P, cos P, and tan P.', 'Answer:', key='sin P = 12/13, cos P = 5/13, tan P = 12/5',
             note='Form required: all three ratios (any equivalent fractions).'),
          mc('Why is sin 40° the same in every right triangle with a 40° angle?', ['All such triangles are similar, so the opposite-to-hypotenuse ratio is the same', 'Every hypotenuse is 1',
                                                                                  'The sides are always 3, 4, 5', 'Sine depends on the triangle\'s size'],
             note='Similarity fixes the ratio.'),
          tf('Doubling every side of a right triangle doubles the tangent of its acute angles.', key=False, note='The ratio stays the same.'),
      ],
      back=[
          B('Similar triangles have equal side ratios within each triangle', 'HSG-SRT.A.2', [
              sa('Triangles with sides 3, 4, 5 and 6, 8, 10 are similar. Compare 3/5 and 6/10.', 'Answer:', key='Both equal 0.6.', note='Any equivalent answer.'),
              tf('If △ABC ~ △DEF, then AB/AC = DE/DF.', key=True, note='Ratios within each triangle match.'),
              mc('△ABC ~ △DEF with BC/AB = 0.8. Find EF/DE.', ['0.8', '1.25', '0.2', 'Cannot tell'], note='Same ratio.'),
              sa('A triangle has legs 2 and 3. A similar one has shorter leg 8. Find the longer leg.', 'Leg:', key='12', note='Any equivalent form.'),
              tf('Similar triangles have equal side lengths.', key=False, note='Proportional, not equal.'),
          ], align='exact',
            why=why('the student does not see ratios inside a triangle as fixed by shape.', 'trig ratios are such ratios.', 'compares internal ratios.')),
          B('Name the opposite side, adjacent side, and hypotenuse for an angle', 'HSG-SRT.A.3', [
              sa('In right triangle ABC with right angle at C, which side is opposite ∠A?', 'Side:', key='BC', note='Any equivalent form.'),
              sa('In right triangle ABC with right angle at C, which side is adjacent to ∠A (not the hypotenuse)?', 'Side:', key='AC', note='Any equivalent form.'),
              mc('The hypotenuse is always', ['opposite the right angle', 'next to the right angle', 'the shortest side', 'opposite the smallest angle'], note='Longest side.'),
              tf('The side opposite ∠A is adjacent to ∠B.', key=True, note='BC is next to ∠B.'),
              tf('The opposite side of an angle depends on the triangle\'s size.', key=False, note='It depends on position.'),
          ], align='supporting',
            why=why('the student labels sides relative to the wrong angle.', 'every ratio is defined relative to the chosen angle.', 'labels sides.')),
          B('Write and simplify ratios', '6.RP.A.1', [
              sa('Write 12 : 13 as a fraction.', 'Fraction:', key='12/13', note='Any equivalent form.'),
              sa('Simplify 8/10.', 'Answer:', key='4/5', note='Any equivalent form.'),
              mc('Which equals 0.75?', ['3/4', '4/3', '7/5', '3/7'], note='3 ÷ 4.'),
              tf('5/13 ≈ 0.385', key=True, note='Division.'),
              tf('A ratio changes when both quantities are tripled.', key=False, note='It stays the same.'),
          ], align='supporting',
            why=why('the student cannot work with ratios.', 'trig values are ratios.', 'writes and simplifies ratios.')),
      ],
      f1=B('Find trig ratios from one ratio, using a similar right triangle', 'HSG-SRT.C.6', [
          sa('For an acute angle θ, sin θ = 3/5. Find cos θ and tan θ.', 'Answer:', key='cos θ = 4/5, tan θ = 3/4', note='Form required: both. A 3-4-5 triangle.'),
          sa('tan θ = 5/12 for an acute angle θ. Find sin θ.', 'sin θ =', key='5/13', note='Any equivalent form.'),
          tf('For any acute angle, (sin θ)² + (cos θ)² = 1.', key=True, note='Pythagorean Theorem divided by the hypotenuse squared.'),
          mc('cos θ = 0.6. Which is sin θ (θ acute)?', ['0.8', '0.4', '0.6', '1.6'], note='√(1 - 0.36).'),
          sa('Explain why sin θ < 1 for every acute angle θ.', 'Answer:', key='The opposite leg is shorter than the hypotenuse.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Work backward from one ratio to the others by building a similar right triangle.'),
      f2=B('The unit circle extends the ratios beyond acute angles', 'HSF-TF.A.2', [
          sa('On a unit circle, the point for angle θ is (cos θ, sin θ). Find the point for 90°.', 'Point:', key='(0, 1)', note='Form required: an ordered pair.'),
          sa('Find the coordinates of the point on the unit circle at 30°.', 'Point:', key='(√3/2, ½)', note='Form required: exact values.'),
          tf('For acute angles, the unit-circle definition agrees with the right-triangle definition.', key=True, note='The hypotenuse is 1.'),
          mc('sin 150° on the unit circle equals', ['½', '-½', '√3/2', '-√3/2'], note='Point (-√3/2, ½).'),
          sa('Explain why the unit circle lets us define sine for 120°, when no right triangle has a 120° acute angle.', 'Answer:',
             key='The point on the unit circle at 120° has a y-coordinate, which defines sin 120°.', note='Any equivalent answer.'),
      ], prog='later-course extension', demand='Extend the ratio definitions to all angles using the unit circle (Algebra II).',
        builds='Builds on FORWARD 1: the triangle with hypotenuse 1 is the step to the unit circle.')),
]


def two_obs(d, a1, a2):
    """Height of an object seen at elevation a1 from one point and a2 from a point d closer (a2 > a1)."""
    return d / (1 / tand(a1) - 1 / tand(a2))


H2 = two_obs(40, 25, 40)
DIST1 = H2 / tand(40)

SETS += [
    # ------------------------------------------------------------------ 49. SRT.C.7 complementary
    S('HSG-SRT.C.7', 'Explain and use the relationship between the sine and cosine of complementary angles',
      target='Explain why sin θ = cos(90° - θ) and use the relationship to rewrite and solve', strand='core', covers=['SRT7-comp'],
      main=[
          proof('Right triangle ABC has its right angle at C. Explain why sin A = cos B.', fig=rt(desc='Right triangle ABC with the right angle at C; A at the lower left, B at the top right.'),
                method='Name the side opposite ∠A and the side adjacent to ∠B, and use the angle sum.', key='sin A = BC/AB = cos B, and A and B are complementary.',
                note=PR + 'Essential: sin A = BC/AB (opposite over hypotenuse); cos B = BC/AB (BC is adjacent to ∠B); so they are equal; ∠A + ∠B = 90°, so sin A = cos(90° - A).'),
          sa('sin 25° = cos x°, where 0 < x < 90. Find x.', 'x =', key='65', note='Any equivalent form. Complementary angles.'),
          sa('θ is acute and cos θ = 0.6. Find sin(90° - θ).', 'Answer:', key='0.6', note='Any equivalent form.'),
          sa('Both angles are acute and sin(2x + 10)° = cos(3x)°. Find x.', 'x =', key='16', note='Any equivalent form. 2x + 10 + 3x = 90.'),
          mc('Which expression equals cos 72°?', ['sin 18°', 'sin 72°', 'cos 18°', 'tan 18°'], note='72 + 18 = 90.'),
      ],
      back=[
          B('Complementary angles add to 90°', '7.G.B.5', [
              sa('Find the complement of 37°.', 'Complement:', key='53°', note='Any equivalent form.'),
              tf('The two acute angles of a right triangle are complementary.', key=True, note='They add to 90°.'),
              mc('Angles x and 2x are complementary. x =', ['30°', '60°', '45°', '90°'], note='3x = 90.'),
              sa('The complement of θ is 90° - θ. If θ = 64°, find it.', 'Answer:', key='26°', note='Any equivalent form.'),
              tf('Complementary angles must be adjacent.', key=False, note='They need only add to 90°.'),
          ], align='exact',
            why=why('the student does not know "complementary".', 'the relationship is about complementary angles.', 'finds complements.')),
          B('Opposite and adjacent sides depend on the chosen angle', 'HSG-SRT.C.6', [
              sa('In right triangle ABC (right angle at C), name the side adjacent to ∠B.', 'Side:', key='BC', note='Any equivalent form.'),
              tf('The side opposite ∠A is the side adjacent to ∠B.', key=True, note='Both are BC.'),
              mc('cos B equals', ['BC/AB', 'AC/AB', 'AC/BC', 'BC/AC'], note='Adjacent over hypotenuse.'),
              sa('Write sin A using the sides of right triangle ABC (right angle at C).', 'sin A =', key='BC/AB', note='Any equivalent form.'),
              tf('sin A and cos A are always equal.', key=False, note='Only when A = 45°.'),
          ], align='exact',
            why=why('the student labels sides only for one angle.', 'the relationship swaps the roles of the two acute angles.', 'labels sides for each angle.')),
          B('Angle sum in a right triangle', '8.G.A.5', [
              sa('A right triangle has an acute angle of 28°. Find the other acute angle.', 'Angle:', key='62°', note='Any equivalent form.'),
              tf('A right triangle can have two right angles.', key=False, note='The sum would exceed 180°.'),
              mc('In a right triangle, the acute angles are x and x + 20. x =', ['35°', '45°', '55°', '70°'], note='2x + 20 = 90.'),
              sa('Why do the acute angles of a right triangle add to 90°?', 'Answer:', key='The angles add to 180° and the right angle uses 90°.', note='Any equivalent answer.'),
              tf('The two acute angles of an isosceles right triangle are 45° each.', key=True, note='Equal and complementary.'),
          ], align='exact',
            why=why('the student does not see the two acute angles as complementary.', 'that is why the relationship holds.', 'uses the right-triangle angle sum.')),
      ],
      f1=B('Relationships between tangents of complementary angles', 'HSG-SRT.C.7', [
          sa('Explain why tan θ · tan(90° - θ) = 1 for an acute angle θ.', 'Answer:', key='tan θ = opposite/adjacent and tan(90° - θ) = adjacent/opposite, which are reciprocals.',
             note='Any equivalent explanation.'),
          sa('tan 20° ≈ 0.364. Estimate tan 70°.', 'Answer:', key='About 2.75 (1 ÷ 0.364)', note='Any value 2.74-2.75.'),
          tf('sin θ = cos θ exactly when θ = 45° (for acute θ).', key=True, note='Then 90° - θ = θ.'),
          mc('Which equals 1 for every acute θ?', ['tan θ · tan(90° - θ)', 'sin θ · cos θ', 'tan θ + tan(90° - θ)', 'sin θ + cos θ'], note='Reciprocals.'),
          sa('Show that sin θ / cos(90° - θ) = 1 for acute θ.', 'Answer:', key='cos(90° - θ) = sin θ, so the quotient is sin θ / sin θ = 1.', note='Any equivalent argument.'),
      ], prog='same-course deepening', demand='Extend the complementary relationship to tangent (reciprocals) and to new identities.'),
      f2=B('The Pythagorean identity', 'HSF-TF.C.8', [
          proof('Prove that (sin θ)² + (cos θ)² = 1 for every acute angle θ.', method='Use a right triangle with legs a, b and hypotenuse c and the Pythagorean Theorem.',
                key='(sin θ)² + (cos θ)² = 1', note=PR + 'Essential: sin θ = a/c, cos θ = b/c; a² + b² = c²; divide by c².'),
          sa('sin θ = 0.28 for acute θ. Find cos θ.', 'cos θ =', key='0.96', note='Any equivalent form. √(1 - 0.0784).'),
          tf('(sin 35°)² + (cos 35°)² = 1', key=True, note='Pythagorean identity.'),
          mc('cos θ = 12/13 (θ acute). sin θ =', ['5/13', '12/5', '1/13', '13/12'], note='√(1 - 144/169).'),
          sa('Use complementary angles to show (sin 20°)² + (sin 70°)² = 1.', 'Answer:', key='sin 70° = cos 20°, so the sum is (sin 20°)² + (cos 20°)² = 1.', note='Any equivalent argument.'),
      ], prog='later-course extension', demand='Prove and use the Pythagorean identity, which Algebra II extends to all angles.',
        builds='Builds on FORWARD 1: combining complementary relationships with the Pythagorean Theorem gives the identity.')),

    # ------------------------------------------------------------------ 50. SRT.C.8 sides
    S('HSG-SRT.C.8', 'Find unknown sides of right triangles with trigonometric ratios in applied problems',
      target='Use sine, cosine, or tangent to find an unknown side of a right triangle in an applied problem', strand='core', covers=['SRT8-sides'],
      main=[
          sa('A 12 ft ladder leans against a wall, making a 70° angle with the level ground. How high up the wall does it reach, to the nearest tenth of a foot?', 'Height:',
             key='%s ft' % d1(12 * sind(70)), note='Rounding to 0.1 required. 12 sin 70° = %.4f.' % (12 * sind(70)),
             fig=rt(c_lab='12 ft', ang='70°', desc='Right triangle: the ladder (hypotenuse, 12 ft) makes a 70° angle with the ground at A; the wall is the vertical leg BC.')),
          sa('A wheelchair ramp rises 2.5 ft and makes an 8° angle with the ground. How long is the ramp surface, to the nearest tenth of a foot?', 'Length:',
             key='%s ft' % d1(2.5 / sind(8)), note='Rounding to 0.1 required. 2.5 ÷ sin 8° = %.4f.' % (2.5 / sind(8))),
          sa('From a point 25 m from the base of a tree, on level ground, the angle of elevation to the top is 38°. How tall is the tree, to the nearest tenth of a meter?', 'Height:',
             key='%s m' % d1(25 * tand(38)), note='Rounding to 0.1 required. 25 tan 38° = %.4f.' % (25 * tand(38))),
          mc('A kite string 60 m long makes a 50° angle with the level ground. About how high is the kite above the point where the string is held (nearest meter)?',
             ['%d m' % round(60 * sind(50)), '%d m' % round(60 * cosd(50)), '%d m' % round(60 * tand(50)), '%d m' % round(60 / sind(50))],
             note='Opposite = hypotenuse × sin 50° = %.2f.' % (60 * sind(50))),
          sa('A right triangle has hypotenuse 20 and a 32° angle. Find the leg adjacent to the 32° angle, to the nearest tenth.', 'Leg:', key=d1(20 * cosd(32)),
             note='Rounding to 0.1 required. 20 cos 32° = %.4f.' % (20 * cosd(32))),
      ],
      back=[
          B('Choose the trigonometric ratio that links the known and unknown sides', 'HSG-SRT.C.6', [
              mc('You know the hypotenuse and an angle and want the opposite side. Which ratio?', ['sine', 'cosine', 'tangent', 'none'], note='Opposite/hypotenuse.'),
              mc('You know the adjacent side and an angle and want the opposite side. Which ratio?', ['tangent', 'sine', 'cosine', 'none'], note='Opposite/adjacent.'),
              sa('Which ratio uses the adjacent side and the hypotenuse?', 'Ratio:', key='Cosine', note='Any equivalent answer.'),
              tf('To find the hypotenuse from the opposite side and the angle, use sine.', key=True, note='sin A = opposite/hypotenuse.'),
              tf('Tangent uses the hypotenuse.', key=False, note='Tangent uses the two legs.'),
          ], align='exact',
            why=why('the student picks the wrong ratio.', 'the ratio must contain the known and the unknown side.', 'chooses sine, cosine, or tangent.')),
          B('Solve one-variable equations with a multiplication or division', 'HSA-REI.B.3', [
              sa('Solve x/12 = 0.94.', 'x =', key='11.28', note='Any equivalent form.'),
              sa('Solve 0.14 = 2.5/x.', 'x ≈', key='17.86', note='Any value 17.8-17.9.'),
              mc('If sin 30° = h/10, then h =', ['10 sin 30°', '10 ÷ sin 30°', 'sin 30° ÷ 10', '30 ÷ 10'], note='Multiply both sides by 10.'),
              tf('From 0.5 = 4/x we get x = 8.', key=True, note='x = 4 ÷ 0.5.'),
              tf('From tan 40° = 20/x we get x = 20 tan 40°.', key=False, note='x = 20 ÷ tan 40°.'),
          ], align='exact',
            why=why('the student cannot solve the trig equation for the side.', 'the unknown may be in the numerator or the denominator.', 'solves both forms.')),
          B('Round to a stated precision and keep track of units', 'HSN-Q.A.3', [
              sa('Round 11.2763 to the nearest tenth.', 'Answer:', key='11.3', note='Any equivalent form.'),
              sa('A calculation gives 19.532 m. Report it to the nearest tenth of a meter.', 'Answer:', key='19.5 m', note='Any equivalent form.'),
              tf('Rounding in the middle of a calculation can change the final answer.', key=True, note='Round at the end.'),
              mc('A height is measured in feet and the angle in degrees. The answer\'s unit is', ['feet', 'degrees', 'feet per degree', 'no unit'], note='Lengths keep their units.'),
              tf('17.96 rounded to the nearest tenth is 17.9.', key=False, note='It is 18.0.'),
          ], align='exact',
            why=why('the student rounds early or drops units.', 'applied answers need the stated precision and units.', 'rounds correctly and labels units.')),
      ],
      f1=B('Find a height from two angle-of-elevation observations', 'HSG-SRT.C.8', [
          sa('From point A on level ground the angle of elevation to the top of a tower is 25°. From point B, 40 m closer, it is 40°. Find the tower\'s height to the nearest tenth of a meter.', 'Height:',
             key='%s m' % d1(H2), note='Rounding to 0.1 required. h = 40 ÷ (1/tan 25° - 1/tan 40°) = %.3f. Two equations: h = x tan 40° and h = (x + 40) tan 25°.' % H2),
          sa('In the same situation, how far is point B from the base of the tower, to the nearest tenth of a meter?', 'Distance:', key='%s m' % d1(DIST1),
             note='Rounding to 0.1 required. x = h ÷ tan 40° = %.3f.' % DIST1),
          tf('With only one angle of elevation and no distance, the height cannot be found.', key=True, note='One equation has two unknowns.'),
          mc('Which equations describe two observations 40 m apart (angles 25° and 40°, distance x from the closer point)?', ['h = x tan 40° and h = (x + 40) tan 25°',
                                                                                                                             'h = x tan 25° and h = (x + 40) tan 40°',
                                                                                                                             'h = 40 tan 25°', 'h = x sin 40°'],
             note='The closer point has the larger angle.'),
          sa('Explain why the closer observation point has the larger angle of elevation.', 'Answer:', key='The same height over a shorter horizontal distance gives a larger tangent, so a larger angle.',
             note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Solve an inverse problem with two observations: two trigonometric equations in two unknowns.'),
      f2=B('Find a feasible location under a clearance constraint', 'HSG-MG.A.3', [
          sa('A ramp must rise 3 ft, and its angle with the ground may be at most 4.8°. What is the shortest allowed horizontal run, to the nearest foot?', 'Run:',
             key='%d ft' % math.ceil(3 / tand(4.8)), note='Form required: a whole number of feet that meets the constraint (round up). 3 ÷ tan 4.8° = %.2f.' % (3 / tand(4.8))),
          sa('A camera on a 6 m pole must see a point on the ground at an angle of depression of at least 20°. How far from the pole can that point be, at most, to the nearest tenth of a meter?', 'Distance:',
             key='%s m' % d1(6 / tand(20)), note='Rounding to 0.1 required. 6 ÷ tan 20° = %.3f; farther points need smaller angles.' % (6 / tand(20))),
          tf('Rounding down the run of a ramp with a maximum angle can make the ramp too steep.', key=True, note='A shorter run gives a larger angle.'),
          mc('A ladder must reach 10 ft up and make an angle of at most 75° with the ground. The shortest ladder that works is about', ['%.1f ft' % (10 / sind(75)), '10.0 ft', '%.1f ft' % (10 * sind(75)), '%.1f ft' % (10 / tand(75))],
             note='At exactly 75°, length = 10 ÷ sin 75° = %.2f; a smaller angle needs a longer ladder.' % (10 / sind(75))),
          sa('A building code allows stairs with an angle of at most 37°. A staircase must rise 9 ft. What is the shortest horizontal run, to the nearest tenth of a foot?', 'Run:',
             key='%s ft' % d1(9 / tand(37)), note='Rounding to 0.1 required. 9 ÷ tan 37° = %.3f.' % (9 / tand(37))),
      ], prog='cross-standard extension', demand='Design under a constraint: find the extreme feasible dimension and decide which way to round.',
        builds='Builds on FORWARD 1: the same trigonometric models, now used to satisfy a stated constraint.')),

    # ------------------------------------------------------------------ 51. SRT.C.8 angles
    S('HSG-SRT.C.8', 'Find unknown angles with inverse trigonometric ratios in applied problems',
      target='Use inverse sine, cosine, or tangent to find an acute angle of a right triangle in an applied problem', strand='core', covers=['SRT8-angles'],
      main=[
          sa('A ramp rises 1 m over a horizontal distance of 12 m. What angle does it make with the ground, to the nearest tenth of a degree?', 'Angle:', key='%s°' % d1(atand(1 / 12)),
             note='Rounding to 0.1° required. tan⁻¹(1/12) = %.3f°.' % atand(1 / 12)),
          sa('A 6 m ladder reaches 5.5 m up a vertical wall. What angle does it make with the level ground, to the nearest tenth of a degree?', 'Angle:', key='%s°' % d1(asind(5.5 / 6)),
             note='Rounding to 0.1° required. sin⁻¹(5.5/6) = %.3f°.' % asind(5.5 / 6)),
          sa('A 10 m flagpole casts a 14 m shadow on level ground. Find the angle of elevation of the sun, to the nearest tenth of a degree.', 'Angle:', key='%s°' % d1(atand(10 / 14)),
             note='Rounding to 0.1° required. tan⁻¹(10/14) = %.3f°.' % atand(10 / 14)),
          mc('A right triangle has legs 7 and 24. What is its smaller acute angle, to the nearest tenth of a degree?', ['%s°' % d1(atand(7 / 24)), '%s°' % d1(atand(24 / 7)), '%s°' % d1(asind(7 / 25) * 2), '%s°' % d1(7 / 24 * 90)],
             note='tan⁻¹(7/24) = %.3f°.' % atand(7 / 24)),
          sa('A road rises 6 m for every 100 m of horizontal distance (a 6% grade). What angle does it make with the horizontal, to the nearest tenth of a degree?', 'Angle:', key='%s°' % d1(atand(0.06)),
             note='Rounding to 0.1° required. tan⁻¹(0.06) = %.3f°.' % atand(0.06)),
      ],
      back=[
          B('Inverse trig undoes a trig ratio', 'HSG-SRT.C.6', [
              sa('sin θ = 0.5 for an acute angle θ. Find θ.', 'θ =', key='30°', note='Any equivalent form.'),
              sa('tan θ = 1 for an acute angle θ. Find θ.', 'θ =', key='45°', note='Any equivalent form.'),
              mc('Which gives an angle from a ratio?', ['sin⁻¹', 'sin', 'cos', 'tan'], note='Inverse functions.'),
              tf('cos⁻¹(0.5) = 60°', key=True, note='cos 60° = 0.5.'),
              tf('sin⁻¹(x) means 1 ÷ sin(x).', key=False, note='It is the angle whose sine is x.'),
          ], align='supporting',
            why=why('the student does not know how to get an angle from a ratio.', 'every angle problem ends with an inverse ratio.', 'uses inverse trig.')),
          B('Choose the ratio from the two known sides', 'HSG-SRT.C.6', [
              mc('You know the opposite side and the hypotenuse. Which inverse function finds the angle?', ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'none'], note='Opposite/hypotenuse.'),
              mc('You know both legs. Which inverse function finds an acute angle?', ['tan⁻¹', 'sin⁻¹', 'cos⁻¹', 'none'], note='Opposite/adjacent.'),
              sa('Rise 5 and run 12. Write the ratio for the angle with the ground.', 'Ratio:', key='tan θ = 5/12', note='Any equivalent form.'),
              tf('Adjacent side and hypotenuse give the angle by cos⁻¹.', key=True, note='Cosine.'),
              tf('Opposite side and hypotenuse give the angle by tan⁻¹.', key=False, note='sin⁻¹.'),
          ], align='exact',
            why=why('the student uses the wrong ratio.', 'the inverse must match the known sides.', 'chooses the ratio.')),
          B('Use degree mode and round angles', 'HSN-Q.A.3', [
              sa('Round 4.7636° to the nearest tenth of a degree.', 'Answer:', key='4.8°', note='Any equivalent form.'),
              tf('A calculator in radian mode gives sin⁻¹(0.5) ≈ 0.524, not 30.', key=True, note='Radians.'),
              mc('An acute angle of a right triangle must be', ['between 0° and 90°', 'exactly 45°', 'more than 90°', 'any angle'], note='Acute.'),
              sa('A computed angle is 112°. Can it be an acute angle of a right triangle?', 'Answer:', key='No', note='Any equivalent answer; check the calculation.'),
              tf('35.537° to the nearest tenth is 35.6°.', key=False, note='35.5°.'),
          ], align='exact',
            why=why('the student gets impossible angles from mode or rounding errors.', 'answers must be reasonable acute angles.', 'checks mode and rounding.')),
      ],
      f1=B('Solve a right triangle completely from two sides', 'HSG-SRT.C.8', [
          sa('A right triangle has legs 9 and 14. Find the hypotenuse and both acute angles (nearest tenth).', 'Answer:',
             key='Hypotenuse %s; angles %s° and %s°' % (d1(math.hypot(9, 14)), d1(atand(9 / 14)), d1(90 - atand(9 / 14))),
             note='Rounding to 0.1 required for all three; the angles add to 90°.'),
          sa('A right triangle has hypotenuse 17 and one leg 8. Find the other leg and both acute angles (nearest tenth of a degree).', 'Answer:',
             key='Other leg 15; angles %s° and %s°' % (d1(asind(8 / 17)), d1(90 - asind(8 / 17))), note='Form required: all three.'),
          tf('Once one acute angle is known, the other is 90° minus it.', key=True, note='Complementary.'),
          mc('Legs 5 and 5. Angles?', ['45° and 45°', '30° and 60°', '5° and 85°', '50° and 40°'], note='Isosceles right triangle.'),
          sa('Explain how to check a solved right triangle.', 'Answer:', key='The acute angles add to 90°, a² + b² = c², and each ratio matches its angle.', note='Any reasonable checks.'),
      ], prog='same-course deepening', demand='Find ALL missing parts of a right triangle and check them for consistency.'),
      f2=B('Find directions (bearings) with inverse trigonometry', 'HSG-SRT.C.8', [
          sa('A boat travels 8 km east and then 5 km north. Find the angle north of east of its straight-line direction from the start, to the nearest tenth of a degree.', 'Angle:',
             key='%s°' % d1(atand(5 / 8)), note='Rounding to 0.1° required.'),
          sa('A hiker walks 3 km north and 4 km west. What is the bearing angle west of north from the start, to the nearest tenth of a degree?', 'Angle:', key='%s°' % d1(atand(4 / 3)),
             note='Rounding to 0.1° required.'),
          tf('Bearing problems become right-triangle problems when the motions are perpendicular.', key=True, note='East-west and north-south legs.'),
          mc('A drone flies 120 m horizontally and rises 50 m. Its angle of climb is about', ['%s°' % d1(atand(50 / 120)), '%s°' % d1(atand(120 / 50)), '%s°' % d1(asind(50 / 120)), '50°'],
             note='tan⁻¹(50/120).'),
          sa('A ship is 10 km east and 10 km south of port. Find the straight-line distance and the angle south of east.', 'Answer:', key='%s km; 45°' % d1(10 * math.sqrt(2)),
             note='Form required: both. 10√2 ≈ 14.1.'),
      ], prog='same-course deepening', demand='Model navigation situations as right triangles and report directions as angles.',
        builds='Builds on FORWARD 1: solving the whole triangle gives both distance and direction.')),

    # ------------------------------------------------------------------ 52. SRT.C.8 solve right triangles
    S('HSG-SRT.C.8', 'Solve right triangles in applied problems with trigonometry and the Pythagorean Theorem',
      target='Find all requested parts of a right triangle in an applied problem, choosing trigonometric ratios and the Pythagorean Theorem', strand='core', covers=['SRT8-solve'],
      main=[
          sa('From the top of an 80 m cliff, the angle of depression to a boat is 25°. How far is the boat from the base of the cliff, to the nearest tenth of a meter? How far is it from the observer?', 'Answer:',
             key='%s m from the base; %s m from the observer' % (d1(80 / tand(25)), d1(80 / sind(25))), note='Rounding to 0.1 required for both. Horizontal = 80 ÷ tan 25°; line of sight = 80 ÷ sin 25°.'),
          sa('A plane flying at an altitude of 2,000 m is seen at an angle of elevation of 14°. Find the horizontal ground distance and the line-of-sight distance to the plane, to the nearest meter.', 'Answer:',
             key='%d m horizontal; %d m line of sight' % (round(2000 / tand(14)), round(2000 / sind(14))), note='Rounding to the nearest meter required for both.'),
          sa('A ramp is 15 ft long and rises 2 ft. Find its horizontal run (nearest tenth of a foot) and its angle with the ground (nearest tenth of a degree).', 'Answer:',
             key='Run %s ft; angle %s°' % (d1(math.sqrt(225 - 4)), d1(asind(2 / 15))), note='Rounding required as stated. Run = √(15² - 2²); angle = sin⁻¹(2/15).'),
          mc('A 25 ft guy wire from the top of a pole meets the level ground 9 ft from the pole. How tall is the pole and what angle does the wire make with the ground (nearest tenth)?',
             ['%s ft; %s°' % (d1(math.sqrt(625 - 81)), d1(acosd(9 / 25))), '%s ft; %s°' % (d1(math.sqrt(625 + 81)), d1(acosd(9 / 25))),
              '%s ft; %s°' % (d1(math.sqrt(625 - 81)), d1(asind(9 / 25))), '16.0 ft; 21.1°'],
             note='Height √(25² - 9²); angle cos⁻¹(9/25).'),
          sa('A right triangle has hypotenuse 25 and a 40° angle. Find both legs and the other acute angle (legs to the nearest tenth).', 'Answer:',
             key='Legs %s and %s; other angle 50°' % (d1(25 * sind(40)), d1(25 * cosd(40))), note='Form required: both legs and the angle.'),
      ],
      back=[
          B('Use the Pythagorean Theorem to find a side', '8.G.B.7', [
              sa('A right triangle has hypotenuse 25 and a leg 9. Find the other leg, to the nearest tenth.', 'Leg:', key=d1(math.sqrt(544)), note='Any equivalent form. √(625 - 81).'),
              sa('Legs 8 and 15. Find the hypotenuse.', 'Hypotenuse:', key='17', note='Any equivalent form.'),
              tf('In a right triangle, the hypotenuse is the longest side.', key=True, note='It is opposite the largest angle.'),
              mc('Hypotenuse 13, leg 5. Other leg?', ['12', '8', '18', '√194'], note='√(169 - 25).'),
              tf('a² + b² = c² works for every triangle.', key=False, note='Only right triangles.'),
          ], align='exact',
            why=why('the student cannot find a side without trig.', 'often the quickest step uses the Pythagorean Theorem.', 'applies it in both directions.')),
          B('Interpret angles of elevation and depression', 'HSG-SRT.C.6', [
              tf('An angle of depression is measured down from the horizontal.', key=True, note='Definition.'),
              sa('The angle of depression from a cliff top to a boat is 25°. What is the angle of elevation from the boat to the cliff top?', 'Angle:', key='25°', note='Alternate interior angles.'),
              mc('Which side is horizontal in an angle-of-elevation triangle?', ['The leg along the ground', 'The hypotenuse', 'The vertical leg', 'None'], note='Level ground.'),
              sa('An observer looks up at 30° to a bird. Is that an angle of elevation or depression?', 'Answer:', key='Elevation', note='Any equivalent answer.'),
              tf('The angle of depression is measured from the vertical line.', key=False, note='From the horizontal.'),
          ], align='supporting',
            why=why('the student puts the angle in the wrong place.', 'the triangle must be set up correctly before solving.', 'locates elevation and depression angles.')),
          B('Choose sine, cosine, or tangent', 'HSG-SRT.C.6', [
              mc('Known: opposite side and angle. Wanted: hypotenuse. Ratio?', ['sine', 'cosine', 'tangent', 'none'], note='sin = opp/hyp.'),
              mc('Known: adjacent side and angle. Wanted: opposite side. Ratio?', ['tangent', 'sine', 'cosine', 'none'], note='tan = opp/adj.'),
              sa('Known: hypotenuse and angle. Wanted: adjacent side. Ratio?', 'Ratio:', key='Cosine', note='Any equivalent answer.'),
              tf('Two different ratios can lead to the same correct side if used correctly.', key=True, note='For example, finding the third side by trig or Pythagoras.'),
              tf('Tangent relates the hypotenuse and a leg.', key=False, note='Tangent relates the two legs.'),
          ], align='exact',
            why=why('the student cannot plan which ratio to use.', 'each requested part needs its own ratio.', 'chooses ratios.')),
      ],
      f1=B('Solve problems that need two right triangles', 'HSG-SRT.C.8', [
          sa('From a window 20 m up, the angle of elevation to the top of a building across the street is 30° and the angle of depression to its base is 40°. How tall is the building, to the nearest tenth of a meter?', 'Height:',
             key='%s m' % d1(20 + (20 / tand(40)) * tand(30)), note='Rounding to 0.1 required. Street width = 20 ÷ tan 40° = %.3f; height = 20 + width · tan 30°.' % (20 / tand(40))),
          sa('Two observers 100 m apart on opposite sides of a tower see its top at 35° and 50°. Find the tower\'s height, to the nearest tenth of a meter.', 'Height:',
             key='%s m' % d1(100 / (1 / tand(35) + 1 / tand(50))), note='Rounding to 0.1 required. h/tan 35° + h/tan 50° = 100.'),
          tf('A shared side links two right triangles in such problems.', key=True, note='For example, a common height or distance.'),
          mc('In the two-observer problem, which equation is correct?', ['h/tan 35° + h/tan 50° = 100', 'h tan 35° + h tan 50° = 100', 'h/sin 35° + h/sin 50° = 100', 'h = 100 tan 85°'],
             note='Horizontal distances add to 100.'),
          sa('Explain why the two-observer problem cannot be solved with one triangle.', 'Answer:', key='Each triangle alone has two unknowns (h and its distance); the shared height and total distance give the needed second equation.',
             note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Combine two right triangles that share a side to answer a question neither triangle answers alone.'),
      f2=B('Solve non-right triangles with the Law of Sines', 'HSG-SRT.D.11', [
          sa('In △ABC, A = 40°, B = 65°, and a = 12. Find b to the nearest tenth.', 'b =', key=d1(12 * sind(65) / sind(40)), note='Rounding to 0.1 required. b = a sin B ÷ sin A.'),
          sa('In △ABC, A = 52°, C = 70°, and c = 20. Find a to the nearest tenth.', 'a =', key=d1(20 * sind(52) / sind(70)), note='Rounding to 0.1 required.'),
          tf('The Law of Sines can solve a triangle with no right angle.', key=True, note='a/sin A = b/sin B = c/sin C.'),
          mc('Which data allow the Law of Sines directly?', ['Two angles and any side', 'Three sides', 'Two sides and the included angle', 'Three angles only'], note='AAS or ASA.'),
          sa('Explain how dropping an altitude turns a non-right triangle into two right triangles.', 'Answer:', key='The altitude creates two right triangles that share it, so h = b sin A = a sin B.',
             note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Extend from right triangles to oblique triangles with the Law of Sines (advanced strand).',
        builds='Builds on FORWARD 1: two right triangles sharing an altitude are exactly how the Law of Sines is derived.')),
]
