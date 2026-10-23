"""ADVANCED EXTENSION (+): SRT.D.9-11, C.A.4, GPE.A.3, GMD.A.2 (sets 88-96)."""
import math

from qb import S, B, sa, mc, tf, plot, work
from common import gd, grid_fig, NTS, proof

R = math.radians


def sind(x):
    return math.sin(R(x))


def cosd(x):
    return math.cos(R(x))


def asind(x):
    return math.degrees(math.asin(x))


def acosd(x):
    return math.degrees(math.acos(x))


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def d2(x):
    return '%.2f' % round(x + 1e-12, 2)


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


PR = 'Any valid proof (paragraph, two-column, or flow). '
EXP = 'Any valid explanation. '
TOOLS = 'Compass and straightedge only; leave all arcs.'
EV = 'Grade the construction marks, not only the final figure: '

ALT = gd({'A': (1.3, 2.4), 'B': (4.2, 0), 'C': (0, 0), 'D': (1.3, 0)},
         [('poly', ['A', 'B', 'C']), ('seg', 'A', 'D', {'dash': True, 'label': 'h', 'side': 1}), ('ra', 'D', 'B', 'A'),
          ('seg', 'C', 'B', {'label': 'a', 'side': -1, 'faint': True}), ('seg', 'C', 'A', {'label': 'b', 'side': 1, 'faint': True}), ('ang', 'C', 'B', 'A')],
         h=230, lab={'A': 'n', 'B': 'se', 'C': 'sw', 'D': 's'}, nodot=['D'],
         desc='Triangle ABC with C at the lower left, B at the lower right, and A at the top. Side CB is labeled a and side CA is labeled b. A dashed altitude from A meets CB at D '
              'with a right angle; the altitude is labeled h. Angle C is marked.', note=NTS)
LOS = gd({'A': (0, 0), 'B': (4.4, 0), 'C': (1.5, 2.5), 'D': (1.5, 0)},
         [('poly', ['A', 'B', 'C']), ('seg', 'C', 'D', {'dash': True, 'label': 'h', 'side': 1}), ('ra', 'D', 'B', 'C'),
          ('seg', 'B', 'C', {'label': 'a', 'side': -1, 'faint': True}), ('seg', 'A', 'C', {'label': 'b', 'side': 1, 'faint': True}),
          ('ang', 'A', 'B', 'C'), ('ang', 'B', 'C', 'A')],
         h=230, lab={'A': 'sw', 'B': 'se', 'C': 'n', 'D': 's'}, nodot=['D'],
         desc='Triangle ABC with A at the lower left, B at the lower right, and C at the top. Side BC is labeled a and side AC is labeled b. A dashed altitude from C meets AB at D with a '
              'right angle; it is labeled h. Angles A and B are marked.', note=NTS)
LOC = grid_fig({'C': (0, 0), 'B': (6, 0), 'A': (2, 3.5)}, [('poly', ['A', 'B', 'C']), ('seg', 'A', (2, 0), {'dash': True})], lo=-1, hi=7, ylo=-1, yhi=5,
               lab={'C': 'sw', 'B': 'se', 'A': 'n'},
               desc='Coordinate grid. Triangle ABC with C at the origin, B on the positive x-axis at (a, 0), and A at (b cos C, b sin C) in the first quadrant; '
                    'a dashed vertical segment from A to the x-axis. (Drawn with a = 6, A at (2, 3.5).)')


def circ_pt(rx=1.4, P=(4.2, 0.6), lab_p='P'):
    return gd({'O': (0, 0), lab_p: P}, [('circle', 'O', rx)], h=220, lab={'O': 'sw', lab_p: 'e'},
              desc='Circle with center O and a point %s outside the circle, to its right.' % lab_p)


TAN_FIG = gd({'O': (0, 0), 'P': (4, 0), 'T': (0.49, 1.4 * math.sqrt(1 - 0.35 ** 2))},
             [('circle', 'O', 1.4), ('seg', 'O', 'T'), ('seg', 'P', 'T'), ('seg', 'O', 'P', {'dash': True}), ('ra', 'T', 'O', 'P')],
             h=220, lab={'O': 'sw', 'P': 'e', 'T': 'n'},
             desc='Circle with center O. Point P is outside the circle. Segment PT touches the circle at T, radius OT is drawn, and a right angle is marked at T. Dashed segment OP joins the center to P.')

SETS = [
    # ------------------------------------------------------------------ 88. SRT.D.9
    S('HSG-SRT.D.9', 'Derive and use the formula A = ½ab sin C',
      target='Derive A = ½ab sin C by drawing an altitude, and use it to find areas of triangles', strand='advanced', covers=['SRT9-derive'],
      main=[
          proof('In triangle ABC, the altitude from A to side CB has length h. Derive the formula Area = ½ab sin C.', fig=ALT, method='Express h using sin C in right triangle ADC, then use Area = ½ · base · height.',
                key='h = b sin C, so Area = ½ah = ½ab sin C.', note=PR + 'Essential: in right triangle ADC, sin C = h/b, so h = b sin C; Area = ½ · a · h; substitute. '
                                                                        'Alternative: an altitude from B gives the same result with h = a sin C.'),
          sa('A triangle has sides a = 8 and b = 11 with included angle C = 40°. Find its area to the nearest tenth.', 'Area:', key=d1(44 * sind(40)), note='Rounding to 0.1 required. ½ · 8 · 11 · sin 40°.'),
          sa('Two sides of a triangle are 6 and 10, and the angle between them is 150°. Find the exact area.', 'Area:', key='15', note='Any equivalent form. sin 150° = ½.'),
          sa('A parallelogram has sides 7 cm and 12 cm with an angle of 55° between them. Find its area to the nearest tenth.', 'Area:', key='%s cm²' % d1(84 * sind(55)),
             note='Rounding to 0.1 required. Two congruent triangles: 7 · 12 · sin 55°.'),
          mc('A triangle has sides 5 and 9 with an included angle of 30°. Its area is', ['11.25', '22.5', '19.5', '45'], note='½ · 45 · ½.'),
      ],
      back=[
          B('The sine ratio in a right triangle', 'HSG-SRT.C.6', [
              sa('In a right triangle, sin of an acute angle = ?', 'Answer:', key='opposite ÷ hypotenuse', note='Any equivalent answer.'),
              sa('Hypotenuse 10, angle 30°. Find the side opposite the angle.', 'Side:', key='5', note='Any equivalent form.'),
              mc('If sin C = h/b, then h =', ['b sin C', 'b/sin C', 'sin C/b', 'b + sin C'], note='Multiply by b.'),
              tf('sin 90° = 1', key=True, note='Value.'),
              tf('sin C = adjacent ÷ hypotenuse', key=False, note='That is cos C.'),
          ], align='exact',
            why=why('the student cannot express the altitude with sine.', 'the derivation needs h = b sin C.', 'uses the sine ratio.')),
          B('Area of a triangle from base and height', '6.G.A.1', [
              sa('Base 8, height 5: area?', 'Area:', key='20', note='Any equivalent form.'),
              tf('Area = ½ · base · height', key=True, note='Formula.'),
              mc('The height must be ___ to the base.', ['perpendicular', 'parallel', 'equal', 'adjacent'], note='Altitude.'),
              sa('Base a and height b sin C: area?', 'Area:', key='½ab sin C', note='Any equivalent form.'),
              tf('A slanted side can be used as the height.', key=False, note='Perpendicular height.'),
          ], align='exact',
            why=why('the student does not know the starting formula.', 'the new formula comes from it.', 'uses ½bh.')),
          B('The included angle of two sides', 'HSG-CO.B.8', [
              sa('In triangle ABC, which angle is included between sides AB and AC?', 'Angle:', key='∠A', note='Any equivalent answer.'),
              tf('SAS uses the angle between the two given sides.', key=True, note='Included angle.'),
              mc('For sides a (BC) and b (CA), the included angle is', ['C', 'A', 'B', 'none'], note='Shared vertex.'),
              sa('Why must the angle be included for ½ab sin C?', 'Answer:', key='The altitude is built from side b and the angle between b and the base a.', note='Any reasonable answer.'),
              tf('Any angle of the triangle works in ½ab sin C.', key=False, note='Only the included one.'),
          ], align='supporting',
            why=why('the student uses a non-included angle.', 'the formula needs the included angle.', 'identifies included angles.')),
      ],
      f1=B('Solve for a side or an angle from an area', 'HSG-SRT.D.9', [
          sa('A triangle has sides 10 and 12 and area 30. Find all possible measures of the included angle.', 'Angle:', key='30° or 150°', note='Form required: both. sin C = ½.'),
          sa('A triangle has area 50, one side 20, and an included angle of 45°. Find the other side to the nearest tenth.', 'Side:', key=d1(100 / (20 * sind(45))), note='Rounding to 0.1 required. 50 = ½ · 20 · b · sin 45°.'),
          tf('Two different triangles can have the same two sides and the same area.', key=True, note='C and 180° - C.'),
          mc('The largest area of a triangle with sides 6 and 8 occurs when the included angle is', ['90°', '60°', '45°', '180°'], note='sin C = 1.'),
          sa('Find the area of an equilateral triangle with side 6 using ½ab sin C (exact).', 'Area:', key='9√3', note='Form required: exact value.'),
      ], prog='same-course deepening', demand='Use the formula backward to find an angle or a side, including the two-angle case.'),
      f2=B('From equal areas to the Law of Sines', 'HSG-SRT.D.10', [
          proof('The area of triangle ABC can be written as ½bc sin A, ½ac sin B, or ½ab sin C. Use this to show that sin A/a = sin B/b = sin C/c.', method='Set the three expressions equal and divide by ½abc.',
                key='½bc sin A = ½ac sin B = ½ab sin C; dividing by ½abc gives sin A/a = sin B/b = sin C/c.', note=PR + 'Essential: three area expressions equal; division by ½abc; result.'),
          sa('Use sin A/a = sin B/b: A = 30°, a = 5, b = 8. Find sin B.', 'sin B =', key='0.8', note='Any equivalent form.'),
          tf('The Law of Sines can be derived from the area formula.', key=True, note='As above.'),
          mc('Dividing ½bc sin A = ½ac sin B by ½abc gives', ['sin A/a = sin B/b', 'a sin A = b sin B', 'sin A = sin B', 'a/b = sin A sin B'], note='Cancel.'),
          sa('Why is it allowed to divide by ½abc?', 'Answer:', key='Side lengths are positive, so ½abc ≠ 0.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use the area formula to prove a new theorem (the Law of Sines).',
        builds='Builds on FORWARD 1: the area formula, now used with any pair of sides, yields the Law of Sines.')),

    # ------------------------------------------------------------------ 89. SRT.D.10 Law of Sines proof
    S('HSG-SRT.D.10', 'Prove the Law of Sines',
      target='Prove the Law of Sines (a/sin A = b/sin B = c/sin C) using an altitude, including the obtuse case', strand='advanced', covers=['SRT10-sines'],
      main=[
          proof('In triangle ABC, CD is the altitude to AB. Prove that a/sin A = b/sin B.', fig=LOS, method='Write h two ways, using right triangles ADC and BDC.',
                key='h = b sin A and h = a sin B, so b sin A = a sin B and a/sin A = b/sin B.',
                note=PR + 'Essential: sin A = h/b and sin B = h/a from the two right triangles; equate h; divide by sin A sin B. Repeating with another altitude gives c/sin C.'),
          proof('Triangle ABC has an obtuse angle at A, so the altitude from C meets line AB extended past A at D. Prove that a/sin A = b/sin B in this case.',
                method='Use the right triangle with angle 180° - A at A, and sin(180° - A) = sin A.', key='h = b sin(180° - A) = b sin A and h = a sin B, so a/sin A = b/sin B.',
                note=PR + 'Essential: the exterior angle at A is 180° - A; h = b sin(180° - A); the identity sin(180° - A) = sin A; equate with h = a sin B.'),
          sa('Explain how the area formula ½bc sin A = ½ac sin B gives the Law of Sines.', 'Answer:', key='Dividing both sides by ½abc gives sin A/a = sin B/b.', note='Any equivalent explanation.'),
          mc('In the proof of the Law of Sines, the altitude from C to AB has length h and forms right triangle ADC. Which fact gives h = b sin A?', ['sin A = opposite/hypotenuse in right triangle ADC', 'The Pythagorean Theorem', 'The triangle angle sum', 'cos A = h/b'],
             note='Right triangle ADC.'),
          tf('The Law of Sines works only in right triangles.', key=False, note='It works in every triangle.'),
      ],
      back=[
          B('Use trigonometry in right triangles', 'HSG-SRT.C.8', [
              sa('Right triangle: hypotenuse 12, angle 40°. Opposite side to the nearest tenth?', 'Side:', key=d1(12 * sind(40)), note='Rounding to 0.1 required.'),
              tf('An altitude splits a triangle into two right triangles.', key=True, note='Perpendicular.'),
              mc('If sin B = h/a, then h =', ['a sin B', 'a/sin B', 'sin B/a', 'h sin B'], note='Multiply.'),
              sa('Right triangle: opposite 5, hypotenuse 10. Angle?', 'Angle:', key='30°', note='Any equivalent form.'),
              tf('sin is defined only for angles in right triangles, so it cannot be used after drawing an altitude.', key=False, note='The altitude creates right triangles.'),
          ], align='exact',
            why=why('the student cannot express h with sine.', 'the proof writes h twice.', 'uses right-triangle trigonometry.')),
          B('The area formula ½ab sin C', 'HSG-SRT.D.9', [
              sa('Triangle ABC has b = 4, c = 5, and A = 90°. What is its area?', 'Area:', key='10', note='Any equivalent form.'),
              tf('½bc sin A, ½ac sin B, and ½ab sin C all give the same area.', key=True, note='Same triangle.'),
              mc('Area of a triangle with sides 6, 6 and included 30°?', ['9', '18', '36', '3'], note='½ · 36 · ½.'),
              sa('Write the area of triangle ABC using sides a and c.', 'Area:', key='½ac sin B', note='Any equivalent form.'),
              tf('½ab sin C uses angle A.', key=False, note='Angle C.'),
          ], align='exact',
            why=why('the student cannot use the area route.', 'it gives a second proof.', 'writes the area three ways.')),
          B('Proportions and cross-multiplying', '7.RP.A.2', [
              sa('Solve x/6 = 10/4.', 'x =', key='15', note='Any equivalent form.'),
              tf('If b sin A = a sin B, then a/sin A = b/sin B (when the sines are not 0).', key=True, note='Divide by sin A sin B.'),
              mc('From 3x = 4y, x/y =', ['4/3', '3/4', '12', '7'], note='Divide.'),
              sa('Rewrite p · q = r · s as a proportion with p and r on top.', 'Answer:', key='p/r = s/q (or p/s = r/q)', note='Any correct proportion.'),
              tf('a/b = c/d means a + d = b + c.', key=False, note='ad = bc.'),
          ], align='supporting',
            why=why('the student cannot rearrange the final equation.', 'the law is a proportion.', 'rearranges products into proportions.')),
      ],
      f1=B('Use the Law of Sines (AAS and ASA)', 'HSG-SRT.D.10', [
          sa('In triangle ABC, A = 40°, B = 60°, and a = 10. Find b to the nearest tenth.', 'b =', key=d1(10 * sind(60) / sind(40)), note='Rounding to 0.1 required.'),
          sa('In triangle ABC, A = 40°, B = 60°, and a = 10. Find C, and find c to the nearest tenth.', 'Answer:', key='C = 80°; c ≈ %s' % d1(10 * sind(80) / sind(40)), note='Form required: both.'),
          tf('Knowing two angles and any side determines the triangle.', key=True, note='AAS/ASA.'),
          mc('A = 30°, B = 45°, a = 6. b =', ['6√2 ≈ 8.5', '3√2 ≈ 4.2', '12', '6'], note='6 sin 45°/sin 30°.'),
          sa('Why must the third angle be found before using the Law of Sines for c in an ASA problem?', 'Answer:', key='The law pairs each side with its opposite angle, so C is needed for c.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Use the proved law to solve triangles from two angles and a side.'),
      f2=B('Surveying with the Law of Sines', 'HSG-SRT.D.11', [
          sa('Two observers 500 m apart sight a tree across a river. The angles at the observers (between the baseline and the tree) are 70° and 60°. How far is the tree from the observer at the 70° angle (nearest meter)?',
             'Distance:', key='%d m' % round(500 * sind(60) / sind(50)), note='Rounding to the nearest meter required. Third angle 50°; side opposite 60°.'),
          sa('A surveyor measures a baseline of 200 m and angles of 52° and 71° to a peak. Find the distance from the 52° end to the peak (nearest meter).', 'Distance:',
             key='%d m' % round(200 * sind(71) / sind(57)), note='Rounding to the nearest meter required. Third angle 57°.'),
          tf('Surveyors use a measured baseline and two angles to find distances they cannot walk.', key=True, note='Triangulation.'),
          mc('In a surveying triangle, the side opposite the largest angle is', ['the longest', 'the shortest', 'the baseline always', 'equal to the others'], note='Law of Sines.'),
          sa('Explain why measuring angles is easier than measuring the distance across the river directly.', 'Answer:', key='The far side cannot be reached; angles can be measured from one bank.', note='Any reasonable answer.'),
      ], prog='cross-standard extension', demand='Apply the law to real surveying problems.',
        builds='Builds on FORWARD 1: solving AAS/ASA triangles is the computation inside triangulation.')),
]

SETS += [
    # ------------------------------------------------------------------ 90. SRT.D.10 Law of Cosines proof
    S('HSG-SRT.D.10', 'Prove the Law of Cosines',
      target='Prove the Law of Cosines (c² = a² + b² - 2ab cos C) with coordinates or an altitude, and relate it to the Pythagorean Theorem', strand='advanced', covers=['SRT10-cosines'],
      main=[
          proof('Place triangle ABC with C at the origin and B at (a, 0), so A = (b cos C, b sin C). Prove that c² = a² + b² - 2ab cos C.', fig=LOC,
                method='Use the distance formula for AB and the identity sin²C + cos²C = 1.', key='c² = (b cos C - a)² + (b sin C)² = a² + b² - 2ab cos C',
                note=PR + 'Essential: A = (b cos C, b sin C) because CA = b; c² = (b cos C - a)² + b² sin²C; expand: b²cos²C - 2ab cos C + a² + b² sin²C; sin²C + cos²C = 1 gives a² + b² - 2ab cos C.'),
          proof('In acute triangle ABC, the altitude from A meets BC at D. Let CD = x. Use the two right triangles to prove c² = a² + b² - 2ab cos C.',
                method='Write h² twice with the Pythagorean Theorem, then use x = b cos C.', key='h² = b² - x² = c² - (a - x)², so c² = a² + b² - 2ax = a² + b² - 2ab cos C.',
                note=PR + 'Essential: BD = a - x; h² = b² - x² and h² = c² - (a - x)²; solve for c²; substitute x = b cos C.'),
          sa('Show that the Law of Cosines becomes the Pythagorean Theorem when C = 90°.', 'Answer:', key='cos 90° = 0, so c² = a² + b².', note='Any equivalent answer.'),
          mc('If angle C is obtuse, then', ['c² > a² + b²', 'c² = a² + b²', 'c² < a² + b²', 'c = a + b'], note='cos C < 0, so -2ab cos C > 0.'),
          tf('The Law of Cosines applies only to acute triangles.', key=False, note='It holds for every triangle.'),
      ],
      back=[
          B('The Pythagorean Theorem', '8.G.B.7', [
              sa('Legs 5 and 12: hypotenuse?', 'Hypotenuse:', key='13', note='Any equivalent form.'),
              sa('Hypotenuse b, leg x: the other leg squared?', 'Answer:', key='b² - x²', note='Any equivalent form.'),
              mc('In triangle ABC, the altitude from A to BC has length h and foot D, with CD = x and BC = a. In right triangle ABD, h² + (a - x)² =', ['c²', 'b²', 'a²', 'x²'], note='Right triangle ABD.'),
              tf('The Pythagorean Theorem applies to the right triangles made by an altitude.', key=True, note='Right angles at D.'),
              tf('a² + b² = c² in every triangle.', key=False, note='Right triangles only.'),
          ], align='exact',
            why=why('the student cannot write the right-triangle relationships.', 'the altitude proof uses them twice.', 'applies the theorem.')),
          B('The distance formula', '8.G.B.8', [
              sa('Distance from (0, 0) to (3, 4)?', 'Distance:', key='5', note='Any equivalent form.'),
              sa('Write the squared distance from (p, q) to (a, 0).', 'Answer:', key='(p - a)² + q²', note='Any equivalent form.'),
              mc('Squared distance from (1, 2) to (4, 6)?', ['25', '5', '49', '7'], note='9 + 16.'),
              tf('The distance formula comes from the Pythagorean Theorem.', key=True, note='Legs are coordinate differences.'),
              tf('Distance from (2, 0) to (5, 0) is 7.', key=False, note='3.'),
          ], align='exact',
            why=why('the student cannot find AB in coordinates.', 'the coordinate proof starts there.', 'uses the distance formula.')),
          B('Sine and cosine in a right triangle', 'HSG-SRT.C.6', [
              sa('Hypotenuse b and angle C: adjacent side?', 'Answer:', key='b cos C', note='Any equivalent form.'),
              sa('Hypotenuse b and angle C: opposite side?', 'Answer:', key='b sin C', note='Any equivalent form.'),
              mc('For a 3-4-5 triangle, (sin)² + (cos)² of an acute angle =', ['1', '7/5', '25', '12/25'], note='9/25 + 16/25.'),
              tf('sin²C + cos²C = 1 for acute angles C.', key=True, note='Pythagorean Theorem divided by the hypotenuse squared.'),
              tf('cos C = opposite ÷ hypotenuse', key=False, note='Adjacent ÷ hypotenuse.'),
          ], align='exact',
            why=why('the student cannot write the coordinates of A or simplify.', 'both proofs use b cos C and b sin C.', 'uses sine and cosine.')),
          B('Square a binomial', 'HSA-APR.A.1', [
              sa('Expand (b cos C - a)².', 'Answer:', key='b²cos²C - 2ab cos C + a²', note='Any equivalent form.'),
              sa('Expand (a - x)².', 'Answer:', key='a² - 2ax + x²', note='Any equivalent form.'),
              mc('(p - q)² =', ['p² - 2pq + q²', 'p² - q²', 'p² + q²', 'p² - pq + q²'], note='Identity.'),
              tf('(a - x)² - x² = a² - 2ax', key=True, note='x² cancels.'),
              tf('(a - x)² = a² - x²', key=False, note='Missing -2ax.'),
          ], align='exact',
            why=why('the student cannot expand.', 'the middle term becomes -2ab cos C.', 'expands squares.')),
      ],
      f1=B('Use the Law of Cosines (SAS and SSS)', 'HSG-SRT.D.10', [
          sa('In triangle ABC, a = 7, b = 9, and C = 50°. Find c to the nearest tenth.', 'c =', key=d1(math.sqrt(130 - 126 * cosd(50))), note='Rounding to 0.1 required.'),
          sa('A triangle has sides 5, 7, and 8. Find the angle opposite the side of length 7.', 'Angle:', key='60°', note='Any equivalent form. cos = (25 + 64 - 49)/80 = ½.'),
          tf('The Law of Cosines can find an angle when all three sides are known.', key=True, note='SSS.'),
          mc('Sides 3, 4, 6. The angle opposite 6 is', ['obtuse', 'right', 'acute', 'impossible to tell'], note='36 > 9 + 16.'),
          sa('Find the largest angle of the triangle with sides 4, 5, and 6, to the nearest tenth of a degree.', 'Angle:', key='%s°' % d1(acosd((16 + 25 - 36) / 40)), note='Rounding to 0.1 required.'),
      ], prog='same-course deepening', demand='Use the proved law to find a side (SAS) or an angle (SSS).'),
      f2=B('Distances between moving objects', 'HSG-SRT.D.11', [
          sa('Two ships leave port at the same time on courses 70° apart. One travels 20 km and the other 30 km. How far apart are they, to the nearest tenth?', 'Distance:',
             key='%s km' % d1(math.sqrt(1300 - 1200 * cosd(70))), note='Rounding to 0.1 required.'),
          sa('A golfer\'s ball is 150 yd from the tee; the hole is 180 yd from the tee; the angle between the two directions is 12°. How far is the ball from the hole (nearest yard)?', 'Distance:',
             key='%d yd' % round(math.sqrt(150 ** 2 + 180 ** 2 - 2 * 150 * 180 * cosd(12))), note='Rounding to the nearest yard required.'),
          tf('The Law of Cosines can be used only when the angle between the two known sides is a right angle.', key=False, note='It works for any included angle; with 90° it becomes the Pythagorean Theorem.'),
          mc('Two hikers walk 3 km and 5 km from camp in directions 60° apart. Distance between them?', ['√19 ≈ 4.4 km', '8 km', '2 km', '√34 ≈ 5.8 km'], note='9 + 25 - 15.'),
          sa('Two ships leave port on courses 70° apart. Why can\'t the Pythagorean Theorem alone give the distance between them?', 'Answer:', key='The angle between their courses is not 90°.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Apply the law to real distance problems.',
        builds='Builds on FORWARD 1: the SAS computation now models real distances.')),

    # ------------------------------------------------------------------ 91. SRT.D.11 apply the Law of Sines
    S('HSG-SRT.D.11', 'Apply the Law of Sines, including the ambiguous case',
      target='Apply the Law of Sines to find unknown measurements, and decide how many triangles fit SSA information (the ambiguous case)', strand='advanced', covers=['SRT11-sines'],
      main=[
          sa('Points A and B are 120 m apart on one bank of a river. A tree C is on the other bank. ∠A = 72° and ∠B = 63°. Find AC to the nearest tenth of a meter.', 'AC =',
             key='%s m' % d1(120 * sind(63) / sind(45)), note='Rounding to 0.1 required. ∠C = 45°; AC is opposite ∠B.'),
          sa('In triangle ABC, A = 30°, a = 6, and b = 10. How many triangles are possible? Find all possible measures of B to the nearest tenth.', 'Answer:',
             key='Two: B ≈ %s° or B ≈ %s°' % (d1(asind(5 / 6)), d1(180 - asind(5 / 6))), note='Form required: the number and both angles. sin B = 10 sin 30°/6 ≈ 0.833.'),
          sa('In triangle ABC, A = 40°, a = 12, and b = 10. How many triangles are possible? Find B to the nearest tenth.', 'Answer:', key='One: B ≈ %s°' % d1(asind(10 * sind(40) / 12)),
             note='Form required: the number and the angle. The supplement %s° is too large (with A = 40° the sum exceeds 180°).' % d1(180 - asind(10 * sind(40) / 12))),
          sa('In triangle ABC, A = 50°, a = 5, and b = 10. How many triangles are possible? Explain.', 'Answer:', key='None: sin B = 10 sin 50°/5 ≈ 1.53 > 1.', note='Form required: the number with the reason.'),
          mc('A is acute and b sin A < a < b. How many triangles have these measurements?', ['Two', 'One', 'None', 'Infinitely many'], note='Side a can swing to two positions.'),
      ],
      back=[
          B('The Law of Sines', 'HSG-SRT.D.10', [
              sa('Write the Law of Sines.', 'Answer:', key='a/sin A = b/sin B = c/sin C', note='Any equivalent form.'),
              sa('A = 30°, B = 90°, a = 5. b =', 'b =', key='10', note='Any equivalent form.'),
              mc('Solving a/sin A = b/sin B for sin B gives', ['b sin A/a', 'a sin A/b', 'a/(b sin A)', 'sin A'], note='Cross-multiply.'),
              tf('Each side in the Law of Sines is paired with its opposite angle.', key=True, note='Pairs.'),
              tf('a/sin B = b/sin A', key=False, note='Pairs are opposite.'),
          ], align='exact',
            why=why('the student cannot set up the law.', 'every problem starts with it.', 'writes and solves the law.')),
          B('Inverse sine', 'HSG-SRT.C.8', [
              sa('sin B = 0.5, B acute. B =', 'B =', key='30°', note='Any equivalent form.'),
              sa('sin B = 0.8. Find the acute B to the nearest tenth.', 'B =', key='%s°' % d1(asind(0.8)), note='Rounding to 0.1 required.'),
              mc('sin⁻¹(1) =', ['90°', '0°', '45°', '180°'], note='Value.'),
              tf('The calculator\'s sin⁻¹ always gives an angle between -90° and 90°.', key=True, note='Range.'),
              tf('sin⁻¹(1.2) is an angle.', key=False, note='Sine cannot exceed 1.'),
          ], align='exact',
            why=why('the student cannot recover the angle.', 'SSA problems end with sin⁻¹.', 'uses inverse sine.')),
          B('Triangle angle sum', 'HSG-CO.C.10', [
              sa('Two angles are 72° and 63°. Third angle?', 'Answer:', key='45°', note='Any equivalent form.'),
              tf('A triangle cannot have two obtuse angles.', key=True, note='Sum would exceed 180°.'),
              mc('A = 40° and B = 147.6°. Is this a triangle?', ['No: the sum exceeds 180°', 'Yes', 'Only if C is 0°', 'Only if right'], note='187.6°.'),
              sa('A = 30°, B = 123.6°. Find C.', 'C =', key='26.4°', note='Any equivalent form.'),
              tf('The angles of a triangle add to 360°.', key=False, note='180°.'),
          ], align='exact',
            why=why('the student keeps an impossible second triangle.', 'the angle sum rules it out.', 'checks the angle sum.')),
          B('Sine of supplementary angles', 'HSG-SRT.D.9', [
              tf('sin 150° = sin 30°', key=True, note='sin(180° - x) = sin x.'),
              sa('Name an obtuse angle with the same sine as 56.4°.', 'Answer:', key='123.6°', note='Any equivalent form.'),
              mc('sin 120° equals', ['sin 60°', 'sin 30°', 'cos 120°', '-sin 60°'], note='Supplement.'),
              sa('Why might sin B = 0.83 give two possible triangles?', 'Answer:', key='Both B and 180° - B have that sine.', note='Any equivalent answer.'),
              tf('An obtuse angle has a negative sine.', key=False, note='Positive.'),
          ], align='supporting',
            why=why('the student misses the second triangle.', 'the obtuse supplement has the same sine.', 'uses the supplement.')),
      ],
      f1=B('Solve both triangles in the ambiguous case', 'HSG-SRT.D.11', [
          sa('A = 30°, a = 6, b = 10. For the triangle with acute B, find C and c to the nearest tenth.', 'Answer:',
             key='C ≈ %s°; c ≈ %s' % (d1(150 - asind(5 / 6)), d1(6 * sind(150 - asind(5 / 6)) / 0.5)), note='Form required: both.'),
          sa('In triangle ABC, A = 30°, a = 6, and b = 10, so B ≈ 56.4° or B ≈ 123.6°. For the triangle with obtuse B, find C and c to the nearest tenth.', 'Answer:',
             key='C ≈ %s°; c ≈ %s' % (d1(asind(5 / 6) - 30), d1(6 * sind(asind(5 / 6) - 30) / 0.5)), note='Form required: both. B ≈ 123.6°.'),
          tf('In the ambiguous case the two triangles have different third sides.', key=True, note='Different shapes.'),
          mc('A = 30°, b = 10, and a = 5. How many triangles?', ['One (a right triangle)', 'Two', 'None', 'Three'], note='a = b sin A.'),
          sa('A = 120°, a = 8, b = 10. How many triangles? Explain.', 'Answer:', key='None: with A obtuse, a must be the longest side, but a < b.', note='Form required: the number with the reason.'),
      ], prog='same-course deepening', demand='Solve each possible triangle completely and handle obtuse and boundary cases.'),
      f2=B('Bearings and navigation with the Law of Sines', 'HSG-MG.A.1', [
          sa('A lighthouse is spotted from a ship at an angle of 35° to its course. After the ship sails 8 km farther, the angle is 70°. How far is the ship from the lighthouse at the second sighting (nearest tenth)?',
             'Distance:', key='%s km' % d1(8 * sind(35) / sind(35)), note='Rounding to 0.1 required. The triangle has angles 35°, 110°, 35°, so it is isosceles: 8.0 km.'),
          sa('A forest ranger at A sees a fire at an angle of 48° from the line to a second tower B, 10 km away. From B, the angle is 61°. How far is the fire from A (nearest tenth)?', 'Distance:',
             key='%s km' % d1(10 * sind(61) / sind(71)), note='Rounding to 0.1 required. Third angle 71°.'),
          tf('Bearings and sightings are modeled as triangles with a known side and two angles.', key=True, note='ASA.'),
          mc('A ship sights a lighthouse at 35° to its course; after sailing 8 km farther along the course, the angle is 70°. In the triangle formed by the two ship positions and the lighthouse, the angle at the lighthouse is', ['35°', '70°', '110°', '75°'], note='70° - 35° (exterior angle).'),
          sa('Name one reason a navigation model using a flat triangle might be inaccurate over very long distances.', 'Answer:', key='Earth\'s surface is curved.', note='Any reasonable answer.'),
      ], prog='cross-standard extension', demand='Model navigation sightings as triangles and solve them.',
        builds='Builds on FORWARD 1: complete triangle solutions are applied to sightings.')),

    # ------------------------------------------------------------------ 92. SRT.D.11 apply the Law of Cosines
    S('HSG-SRT.D.11', 'Apply the Law of Cosines, including resultant forces',
      target='Apply the Law of Cosines to find unknown distances, angles, and the magnitudes of resultant forces', strand='advanced', covers=['SRT11-cosines'],
      main=[
          sa('To find the length AB across a lake, a surveyor at C measures CA = 350 m, CB = 420 m, and ∠C = 68°. Find AB to the nearest tenth of a meter.', 'AB =',
             key='%s m' % d1(math.sqrt(350 ** 2 + 420 ** 2 - 2 * 350 * 420 * cosd(68))), note='Rounding to 0.1 required.'),
          sa('Two forces of 40 N and 60 N act on an object with an angle of 50° between them. Find the magnitude of the resultant force to the nearest tenth.', 'Resultant:',
             key='%s N' % d1(math.sqrt(5200 + 4800 * cosd(50))), note='Rounding to 0.1 required. In the force parallelogram the angle opposite the resultant is 130°.'),
          sa('A triangle has sides 8, 10, and 13. Find its largest angle to the nearest tenth of a degree.', 'Angle:', key='%s°' % d1(acosd(-5 / 160)), note='Rounding to 0.1 required. Opposite 13.'),
          sa('A plane flies 200 km, turns 25° to the right, and flies 150 km. How far is it from its start, to the nearest tenth?', 'Distance:',
             key='%s km' % d1(math.sqrt(62500 - 60000 * cosd(155))), note='Rounding to 0.1 required. The angle between the legs inside the triangle is 155°.'),
          mc('Which law should be used first to solve a triangle given all three sides?', ['The Law of Cosines', 'The Law of Sines', 'The Pythagorean Theorem', 'The angle sum'], note='SSS.'),
      ],
      back=[
          B('The Law of Cosines', 'HSG-SRT.D.10', [
              sa('Write the Law of Cosines for side c.', 'Answer:', key='c² = a² + b² - 2ab cos C', note='Any equivalent form.'),
              sa('a = 3, b = 4, C = 90°: c?', 'c =', key='5', note='Any equivalent form.'),
              mc('Solved for cos C:', ['(a² + b² - c²)/(2ab)', '(c² - a² - b²)/(2ab)', '(a² + b² + c²)/(2ab)', '2ab/(a² + b² - c²)'], note='Rearrange.'),
              tf('The angle in the formula is the one opposite the side being found.', key=True, note='C opposite c.'),
              tf('c² = a² + b² + 2ab cos C', key=False, note='Minus.'),
          ], align='exact',
            why=why('the student cannot set up the law.', 'every problem uses it.', 'writes and rearranges the law.')),
          B('Inverse cosine', 'HSG-SRT.C.8', [
              sa('cos C = 0.5. C =', 'C =', key='60°', note='Any equivalent form.'),
              sa('cos C = -0.03125. C to the nearest tenth?', 'C =', key='%s°' % d1(acosd(-0.03125)), note='Rounding to 0.1 required.'),
              mc('A negative cosine means the angle is', ['obtuse', 'acute', 'right', 'zero'], note='Between 90° and 180°.'),
              tf('cos⁻¹ gives angles from 0° to 180°.', key=True, note='Range.'),
              tf('cos⁻¹(0) = 0°', key=False, note='90°.'),
          ], align='exact',
            why=why('the student cannot find the angle.', 'SSS problems end with cos⁻¹.', 'uses inverse cosine.')),
          B('Angles in a parallelogram', 'HSG-CO.C.11', [
              tf('Consecutive angles of a parallelogram are supplementary.', key=True, note='Theorem.'),
              sa('One angle of a parallelogram is 50°. The angle next to it?', 'Answer:', key='130°', note='Any equivalent form.'),
              mc('Forces at 50° form a parallelogram; the angle opposite the resultant in the triangle is', ['130°', '50°', '90°', '25°'], note='Supplement.'),
              sa('A plane turns 25°. The angle inside the triangle at the turn?', 'Answer:', key='155°', note='Any equivalent form.'),
              tf('The angle between two forces is the angle used in the Law of Cosines for the resultant.', key=False, note='Use its supplement.'),
          ], align='supporting',
            why=why('the student uses the wrong angle.', 'force and turning problems need the supplement.', 'finds the triangle angle.')),
      ],
      f1=B('Solve a triangle with both laws', 'HSG-SRT.D.11', [
          sa('In triangle ABC, b = 12, c = 15, A = 40°. Find a to the nearest tenth.', 'a =', key=d1(math.sqrt(144 + 225 - 360 * cosd(40))), note='Rounding to 0.1 required.'),
          sa('In triangle ABC, b = 12, c = 15, and A = 40°. Find B to the nearest tenth of a degree (use the Law of Sines or Cosines).', 'B =',
             key='%s°' % d1(acosd((math.sqrt(144 + 225 - 360 * cosd(40)) ** 2 + 225 - 144) / (2 * 15 * math.sqrt(144 + 225 - 360 * cosd(40))))), note='Rounding to 0.1 required.'),
          tf('After the Law of Cosines, it is safest to find the smaller remaining angle with the Law of Sines.', key=True, note='Avoids the ambiguous obtuse case.'),
          mc('Given two sides and the included angle, use first', ['the Law of Cosines', 'the Law of Sines', 'sin⁻¹', 'the angle sum'], note='SAS.'),
          sa('Use Heron\'s formula or ½ab sin C to find the area of the triangle with sides 8, 10, 13 (nearest tenth).', 'Area:',
             key=d1(0.5 * 8 * 10 * math.sin(math.acos(-5 / 160))), note='Rounding to 0.1 required.'),
      ], prog='same-course deepening', demand='Choose and combine the two laws to solve a triangle completely.'),
      f2=B('Velocity vectors: airspeed and wind', 'HSN-VM.A.3', [
          sa('A plane flies due east at 300 km/h; a wind blows due north at 50 km/h. Find its ground speed (nearest tenth) and direction (degrees north of east, nearest tenth).', 'Answer:',
             key='%s km/h at %s° north of east' % (d1(math.hypot(300, 50)), d1(math.degrees(math.atan(50 / 300)))), note='Form required: both.'),
          sa('A boat heads across a river at 8 km/h; the current is 3 km/h at 90° to its heading. Find its actual speed (nearest tenth).', 'Speed:', key='%s km/h' % d1(math.hypot(8, 3)), note='Rounding to 0.1 required.'),
          tf('The resultant of two velocities is always found by adding their speeds.', key=False, note='Only when they point the same way; otherwise use the parallelogram rule.'),
          mc('Velocities of 10 and 10 with 120° between them have a resultant of', ['10', '20', '17.3', '0'], note='Law of Cosines with 60°.'),
          sa('A plane\'s velocity is 400 km/h; a 60 km/h wind blows at 45° to its heading. Find the ground speed (nearest tenth).', 'Speed:',
             key='%s km/h' % d1(math.sqrt(400 ** 2 + 60 ** 2 + 2 * 400 * 60 * cosd(45))), note='Rounding to 0.1 required. Angle in the triangle 135°.'),
      ], prog='later-course extension', demand='Treat forces and velocities as vectors (Precalculus).',
        builds='Builds on FORWARD 1: solving triangles with both laws becomes vector addition.')),
]

DOME = 2 / 3 * math.pi * (1000 - 9.5 ** 3)
CAV = gd({}, [('arc', (0, 0), 1.5, 0, 180), ('seg', (-1.5, 0), (1.5, 0)), ('seg', (-1.2, 0.9), (1.2, 0.9), {'dash': True}),
              ('poly', [(2.4, 0), (5.4, 0), (5.4, 1.5), (2.4, 1.5)]), ('seg', (3.9, 0), (2.4, 1.5), {'faint': True}), ('seg', (3.9, 0), (5.4, 1.5), {'faint': True}),
              ('seg', (2.4, 0.9), (5.4, 0.9), {'dash': True}), ('text', (0, -0.35), 'hemisphere, radius r'), ('text', (3.9, -0.35), 'cylinder minus cone'), ('text', (5.75, 0.9), 'y')],
         h=200, desc='Left: a hemisphere of radius r resting on its flat base, with a dashed horizontal slice at height y. Right: a cylinder of radius r and height r with an upside-down cone '
                     '(vertex at the center of the bottom, base at the top) removed, shown in side view, with a dashed slice at the same height y.', note=NTS)

SETS += [
    # ------------------------------------------------------------------ 93. C.A.4 tangent construction
    S('HSG-C.A.4', 'Construct a tangent line from a point outside a circle',
      target='Construct the tangent lines from a point outside a given circle to the circle, and justify the construction', strand='advanced', covers=['C4-tangent'],
      main=[
          plot(TOOLS + '\nConstruct a line through P tangent to the circle with center O.', circ_pt(), key='Draw OP; construct its midpoint M (perpendicular bisector); draw the circle with center M through O; '
                                                                                                         'it meets circle O at T₁ and T₂; draw PT₁ (and PT₂).',
               note=EV + 'segment OP, the perpendicular bisector arcs locating M, the circle on diameter OP, and the tangent through a crossing point T.'),
          plot(TOOLS + '\nConstruct BOTH tangent lines from Q to the circle with center O.', circ_pt(rx=1.2, P=(3.6, -0.9), lab_p='Q'),
               key='Same construction; both intersection points T₁ and T₂ give the two tangents QT₁ and QT₂.', note=EV + 'all construction marks and both tangents.'),
          sa('Write the steps for constructing a tangent from an external point P to circle O.', 'Steps:',
             key='1. Draw OP. 2. Bisect OP to find its midpoint M. 3. Draw the circle with center M and radius MO. 4. Label a point T where it meets circle O. 5. Draw line PT.',
             note='Any equivalent steps.'),
          proof('Explain why line PT in the construction is tangent to circle O.', fig=TAN_FIG, ans='Explanation:', method='Use the circle on diameter OP and the tangent-radius theorem.',
                key='T is on the circle with diameter OP, so ∠OTP is inscribed in a semicircle and equals 90°; a line perpendicular to a radius at its endpoint on the circle is tangent.',
                note=EXP + 'Essential: ∠OTP = 90° (inscribed angle on a diameter); PT ⊥ OT at T on circle O; converse of the tangent-radius theorem.'),
          mc('The two tangent segments from P to circle O are', ['congruent', 'perpendicular', 'parallel', 'always equal to the radius'], note='HL congruence of triangles OTP.'),
      ],
      back=[
          B('Construct the midpoint of a segment', 'HSG-CO.D.12', [
              sa('Which construction finds the midpoint of OP?', 'Answer:', key='The perpendicular bisector of OP', note='Any equivalent answer.'),
              tf('The perpendicular bisector crosses the segment at its midpoint.', key=True, note='Definition.'),
              mc('The perpendicular bisector construction uses arcs', ['of equal radius from both endpoints', 'from one endpoint only', 'of any radius', 'centered at the midpoint'], note='Equal radii.'),
              sa('To construct a tangent from a point P outside circle O, why is the midpoint of OP needed?', 'Answer:', key='It is the center of the circle with diameter OP.', note='Any equivalent answer.'),
              tf('The midpoint can be found by eye in a construction.', key=False, note='It must be constructed.'),
          ], align='exact',
            why=why('the student cannot locate M.', 'M is the center of the helper circle.', 'constructs midpoints.')),
          B('Inscribed angles on a diameter', 'HSG-C.A.2', [
              tf('An angle inscribed in a semicircle is a right angle.', key=True, note='Theorem.'),
              sa('A point T is on the circle with diameter OP. m∠OTP = ?', 'Answer:', key='90°', note='Any equivalent form.'),
              mc('The intercepted arc of an angle inscribed in a semicircle is', ['180°', '90°', '360°', '45°'], note='Half of 180 is 90.'),
              sa('To construct a tangent from a point P outside circle O, why is a circle with diameter OP drawn?', 'Answer:', key='Points on it make a right angle with O and P.', note='Any equivalent answer.'),
              tf('An inscribed angle on a diameter can be 60°.', key=False, note='Always 90°.'),
          ], align='exact',
            why=why('the student does not know why the angle is right.', 'the justification uses it.', 'applies the theorem.')),
          B('Tangent is perpendicular to the radius', 'HSG-C.A.2', [
              tf('A line perpendicular to a radius at its endpoint on the circle is tangent to the circle.', key=True, note='Converse.'),
              sa('A tangent meets the radius at what angle?', 'Answer:', key='90°', note='Any equivalent form.'),
              mc('If PT ⊥ OT and T is on circle O, then PT is', ['tangent to the circle', 'a chord', 'a secant', 'a diameter'], note='Converse.'),
              sa('OT = 5 and OP = 13 with PT tangent at T. PT = ?', 'PT =', key='12', note='Any equivalent form.'),
              tf('A tangent passes through the center.', key=False, note='It touches at one point.'),
          ], align='exact',
            why=why('the student cannot justify tangency.', 'the construction makes PT ⊥ OT.', 'uses the tangent-radius relationship.')),
      ],
      f1=B('Prove that the two tangent segments are congruent and compute lengths', 'HSG-C.A.4', [
          proof('PA and PB are tangent to circle O at A and B. Prove that PA = PB.', method='Use the right triangles OAP and OBP.', key='△OAP ≅ △OBP by HL, so PA = PB.',
                note=PR + 'Essential: right angles at A and B (tangent ⊥ radius); OA = OB (radii); OP common hypotenuse; HL; CPCTC.'),
          sa('A circle has radius 5 and P is 13 from its center. Find the length of each tangent segment from P.', 'Length:', key='12', note='Any equivalent form.'),
          tf('OP bisects the angle between the two tangents.', key=True, note='Congruent triangles.'),
          mc('Tangents from P make a 60° angle. The angle AOB is', ['120°', '60°', '30°', '90°'], note='Quadrilateral with two right angles.'),
          sa('Radius 6, tangent segment 8. Distance from P to the center?', 'Distance:', key='10', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Prove a consequence of the construction and compute tangent lengths.'),
      f2=B('Lines of sight to the horizon', 'HSG-MG.A.1', [
          sa('Model Earth as a sphere of radius 6,371 km. A person\'s eyes are 2 m (0.002 km) above the sea. How far is the horizon (tangent distance), to the nearest tenth of a km?', 'Distance:',
             key='%s km' % d1(math.sqrt(2 * 6371 * 0.002 + 0.002 ** 2)), note='Rounding to 0.1 required. d² = (6371.002)² - 6371².'),
          sa('From the top of a 100 m tower (0.1 km), how far is the horizon, to the nearest km?', 'Distance:', key='%d km' % round(math.sqrt(2 * 6371 * 0.1 + 0.01)), note='Rounding to the nearest km required.'),
          tf('The line of sight to the horizon passes through Earth\'s center.', key=False, note='It is tangent, perpendicular to the radius at the horizon point.'),
          mc('Raising the eye height by a factor of 4 multiplies the horizon distance by about', ['2', '4', '16', '8'], note='d ≈ √(2Rh).'),
          sa('In the model of the distance to the horizon from a point above Earth, why is the right angle of the triangle at the horizon point?', 'Answer:', key='The tangent line of sight is perpendicular to the radius at the point of tangency.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use the tangent-radius right triangle to model lines of sight.',
        builds='Builds on FORWARD 1: tangent-length computations model the distance to the horizon.')),

    # ------------------------------------------------------------------ 94. GPE.A.3 ellipse
    S('HSG-GPE.A.3', 'Derive the equation of an ellipse from its foci',
      target='Derive the equation of an ellipse from its foci and the constant sum of distances, and write equations from given information', strand='advanced', covers=['GPE3-ellipse'],
      main=[
          proof('An ellipse is the set of points whose distances to the foci (-3, 0) and (3, 0) add to 10. Derive its equation.', method='Write the distance sum, isolate one radical, square twice, and simplify.',
                key='x²/25 + y²/16 = 1', note=PR + 'Essential: √((x + 3)² + y²) + √((x - 3)² + y²) = 10; isolate and square; simplify to 3x - 25 = -5√((x - 3)² + y²) (or equivalent); '
                                                    'square again; 16x² + 25y² = 400.'),
          sa('Write the equation of the ellipse with foci (0, -4) and (0, 4) whose distances to the foci add to 10.', 'Equation:', key='x²/9 + y²/25 = 1',
             note='Form required: an equation. a = 5 (vertical), c = 4, b² = 9.'),
          sa('Write the equation of the ellipse with foci (±5, 0) and vertices (±13, 0).', 'Equation:', key='x²/169 + y²/144 = 1', note='Form required: an equation. b² = 169 - 25.'),
          sa('Write the equation of the ellipse with foci (1, 2) and (7, 2) whose distances to the foci add to 10.', 'Equation:', key='(x - 4)²/25 + (y - 2)²/16 = 1',
             note='Form required: an equation. Center (4, 2), c = 3, a = 5, b = 4.'),
          mc('For any point on x²/36 + y²/20 = 1, the sum of its distances to the foci is', ['12', '6', '36', '2√20'], note='2a.'),
      ],
      back=[
          B('The distance formula', '8.G.B.8', [
              sa('Distance from (x, y) to (3, 0)?', 'Answer:', key='√((x - 3)² + y²)', note='Any equivalent form.'),
              sa('Distance from (0, 4) to (3, 0)?', 'Distance:', key='5', note='Any equivalent form.'),
              mc('Distance from (5, 0) to (-3, 0)?', ['8', '2', '64', '√34'], note='Horizontal.'),
              tf('The distance formula has a square root.', key=True, note='√.'),
              tf('√(a² + b²) = a + b', key=False, note='Not in general.'),
          ], align='exact',
            why=why('the student cannot write the distances to the foci.', 'the definition adds them.', 'writes distance expressions.')),
          B('Derive a circle equation', 'HSG-GPE.A.1', [
              sa('Equation of the circle with center (0, 0) and radius 5?', 'Equation:', key='x² + y² = 25', note='Form required: an equation.'),
              tf('A circle is an ellipse whose two foci coincide.', key=True, note='Special case.'),
              mc('x²/25 + y²/25 = 1 is', ['a circle of radius 5', 'an ellipse with different axes', 'a parabola', 'a hyperbola'], note='Equal denominators.'),
              sa('A circle is the set of points at a fixed distance from', 'Answer:', key='one point (the center)', note='Any equivalent answer.'),
              tf('An ellipse has one focus.', key=False, note='Two.'),
          ], align='exact',
            why=why('the student cannot connect to the circle derivation.', 'the ellipse derivation follows the same pattern.', 'derives the circle equation.')),
          B('Expand squares', 'HSA-APR.A.1', [
              sa('Expand (x + 3)² - (x - 3)².', 'Answer:', key='12x', note='Any equivalent form.'),
              sa('Expand (x - 3)².', 'Answer:', key='x² - 6x + 9', note='Any equivalent form.'),
              mc('(3x - 25)² =', ['9x² - 150x + 625', '9x² + 625', '9x² - 75x + 625', '3x² - 150x + 625'], note='Middle term 2 · 3x · 25.'),
              tf('(a - b)² = a² - 2ab + b²', key=True, note='Identity.'),
              tf('(x + 3)² = x² + 9', key=False, note='Missing 6x.'),
          ], align='exact',
            why=why('the student cannot simplify after squaring.', 'the derivation expands several squares.', 'expands squares.')),
      ],
      f1=B('Read foci and axes from an ellipse equation', 'HSG-GPE.A.3', [
          sa('Find the foci of x²/25 + y²/9 = 1.', 'Foci:', key='(±4, 0)', note='Form required: both points. c² = 25 - 9.'),
          sa('Find the vertices and foci of x²/16 + y²/25 = 1.', 'Answer:', key='Vertices (0, ±5); foci (0, ±3)', note='Form required: both.'),
          tf('For an ellipse, c² = a² - b².', key=True, note='Relation.'),
          mc('Which ellipse is closest to a circle?', ['x²/25 + y²/24 = 1', 'x²/25 + y²/4 = 1', 'x²/25 + y²/1 = 1', 'x²/100 + y²/9 = 1'], note='Nearly equal denominators.'),
          sa('Find the length of the major axis of x²/49 + y²/36 = 1.', 'Length:', key='14', note='Any equivalent form. 2a.'),
      ], prog='same-course deepening', demand='Reverse the derivation: read foci and axes from an equation.'),
      f2=B('Design with the reflective property of ellipses', 'HSG-MG.A.3', [
          sa('A whispering gallery is an ellipse 40 m long and 16 m wide. How far from the center should two people stand (at the foci), to the nearest tenth?', 'Distance:',
             key='%s m' % d1(math.sqrt(400 - 64)), note='Rounding to 0.1 required. a = 20, b = 8.'),
          sa('A medical device places a kidney stone at one focus of an ellipse x²/100 + y²/64 = 1 (cm). Where is the emitter placed?', 'Answer:', key='At the other focus, 6 cm from the center: (-6, 0) if the stone is at (6, 0).',
             note='Any equivalent answer. c = 6.'),
          tf('Sound from one focus of an elliptical room reflects back to the same focus.', key=False, note='It reflects to the other focus.'),
          mc('A garden ellipse is drawn with a 10 m rope tied to stakes 6 m apart. Its width (minor axis) is', ['8 m', '10 m', '6 m', '4 m'], note='a = 5, c = 3, b = 4.'),
          sa('Explain how the string-and-stakes method uses the definition of an ellipse.', 'Answer:', key='The string length is the constant sum of the distances to the two stakes (foci).', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use foci locations in physical designs.',
        builds='Builds on FORWARD 1: reading foci from dimensions locates design points.')),
]

SETS += [
    # ------------------------------------------------------------------ 95. GPE.A.3 hyperbola
    S('HSG-GPE.A.3', 'Derive the equation of a hyperbola from its foci',
      target='Derive the equation of a hyperbola from its foci and the constant difference of distances, and write equations from given information', strand='advanced', covers=['GPE3-hyperbola'],
      main=[
          proof('A hyperbola is the set of points whose distances to the foci (-5, 0) and (5, 0) differ by 6 (in absolute value). Derive its equation.',
                method='Write the distance difference, isolate one radical, square twice, and simplify.', key='x²/9 - y²/16 = 1',
                note=PR + 'Essential: |√((x + 5)² + y²) - √((x - 5)² + y²)| = 6; isolate and square; simplify to 5x - 9 = ±3√((x - 5)² + y²) (or equivalent); square again; 16x² - 9y² = 144.'),
          sa('Write the equation of the hyperbola with foci (0, ±13) whose distances to the foci differ by 10.', 'Equation:', key='y²/25 - x²/144 = 1',
             note='Form required: an equation. a = 5, c = 13, b² = 144.'),
          sa('Write the equation of the hyperbola with foci (±10, 0) and vertices (±6, 0).', 'Equation:', key='x²/36 - y²/64 = 1', note='Form required: an equation. b² = 100 - 36.'),
          sa('Find the asymptotes of x²/9 - y²/16 = 1.', 'Asymptotes:', key='y = ±(4/3)x', note='Form required: both lines.'),
          mc('For any point on x²/16 - y²/9 = 1, the difference of its distances to the foci is', ['8', '4', '10', '7'], note='2a.'),
      ],
      back=[
          B('The distance formula', '8.G.B.8', [
              sa('Distance from (x, y) to (-5, 0)?', 'Answer:', key='√((x + 5)² + y²)', note='Any equivalent form.'),
              sa('Distance from (3, 0) to (5, 0) minus distance from (3, 0) to (-5, 0)?', 'Answer:', key='-6 (difference 6 in absolute value)', note='Any equivalent form.'),
              mc('Distance from (6, 0) to (-10, 0)?', ['16', '4', '-16', '60'], note='Horizontal.'),
              tf('Distances are never negative.', key=True, note='Definition.'),
              tf('Distance from (0, 13) to (0, -13) is 13.', key=False, note='26.'),
          ], align='exact',
            why=why('the student cannot write the distances to the foci.', 'the definition subtracts them.', 'writes distance expressions.')),
          B('Derive an ellipse equation', 'HSG-GPE.A.3', [
              tf('An ellipse uses a constant SUM of distances to the foci.', key=True, note='Definition.'),
              sa('Ellipse with foci (±3, 0) and sum 10: equation?', 'Equation:', key='x²/25 + y²/16 = 1', note='Form required: an equation.'),
              mc('For an ellipse, b² =', ['a² - c²', 'c² - a²', 'a² + c²', 'ac'], note='Relation.'),
              sa('What changes in the definition to get a hyperbola?', 'Answer:', key='The difference (not the sum) of the distances is constant.', note='Any equivalent answer.'),
              tf('An ellipse equation has a minus sign between the squared terms.', key=False, note='Plus.'),
          ], align='exact',
            why=why('the student has not seen the parallel derivation.', 'the hyperbola derivation mirrors it.', 'derives the ellipse.')),
          B('Absolute value as distance', '6.NS.C.7', [
              sa('|4 - 10| = ', 'Answer:', key='6', note='Any equivalent form.'),
              sa('|10 - 4| = ', 'Answer:', key='6', note='Any equivalent form.'),
              mc('|a - b| means', ['the size of the difference', 'a + b', 'always a - b', 'a negative number'], note='Distance.'),
              tf('|x| = 6 has two solutions.', key=True, note='±6.'),
              tf('|−3| = −3', key=False, note='3.'),
          ], align='supporting',
            why=why('the student only considers one branch.', 'the difference can be positive or negative.', 'uses absolute value.')),
      ],
      f1=B('Read foci and asymptotes from a hyperbola equation', 'HSG-GPE.A.3', [
          sa('Find the foci of x²/16 - y²/9 = 1.', 'Foci:', key='(±5, 0)', note='Form required: both points. c² = 16 + 9.'),
          sa('Find the vertices and asymptotes of y²/4 - x²/9 = 1.', 'Answer:', key='Vertices (0, ±2); asymptotes y = ±(2/3)x', note='Form required: both.'),
          tf('For a hyperbola, c² = a² + b².', key=True, note='Relation.'),
          mc('Which equation is a hyperbola?', ['x²/4 - y²/9 = 1', 'x²/4 + y²/9 = 1', 'x² + y² = 4', 'y = x²/4'], note='Minus sign.'),
          sa('Explain how to tell an ellipse from a hyperbola by its equation.', 'Answer:', key='An ellipse has a plus sign between the squared terms; a hyperbola has a minus sign.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Reverse the derivation: read foci, vertices, and asymptotes from an equation.'),
      f2=B('Locate a position from a time difference', 'HSG-MG.A.3', [
          sa('Two radio stations are 100 km apart at (±50, 0). A ship receives signals showing it is 60 km closer to one station than the other. Write the equation of the hyperbola it lies on.', 'Equation:',
             key='x²/900 - y²/1600 = 1', note='Form required: an equation. 2a = 60, c = 50, b² = 2500 - 900.'),
          sa('Sound travels 0.34 km/s. Two microphones 2 km apart hear a sound 3 s apart. What is the difference in distances to the source?', 'Difference:', key='1.02 km', note='Any equivalent form.'),
          tf('A single time difference places the source on one branch of a hyperbola, not at a single point.', key=True, note='A second pair of stations is needed.'),
          mc('Radio stations are at (-50, 0) and (50, 0) (km). A ship on the x-axis, to the right of the origin, is 60 km closer to the right station than to the left one. Its position is', ['(30, 0)', '(50, 0)', '(60, 0)', '(40, 0)'], note='Vertex.'),
          sa('Why do navigation systems use at least two pairs of stations?', 'Answer:', key='Each pair gives a hyperbola; the intersection pins down the position.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use the hyperbola definition to locate positions from distance differences.',
        builds='Builds on FORWARD 1: reading a, b, c is used to model navigation.')),

    # ------------------------------------------------------------------ 96. GMD.A.2 Cavalieri and the sphere
    S('HSG-GMD.A.2', 'Use Cavalieri\'s principle to justify the volume of a sphere',
      target='Give an informal argument using Cavalieri\'s principle for the volume of a sphere (and other solid figures)', strand='advanced', covers=['GMD2-sphere'],
      main=[
          proof('A hemisphere of radius r and a cylinder of radius r and height r with a cone removed (as shown) sit on the same plane. Use Cavalieri\'s principle to show that the hemisphere\'s volume is ⅔πr³, '
                'and conclude that a sphere has volume 4/3 πr³.', fig=CAV, ans='Explanation:', method='Compare the cross-section areas at height y.',
                key='Both cross-sections have area π(r² - y²), so the volumes are equal: πr³ - ⅓πr³ = ⅔πr³; the sphere is two hemispheres: 4/3 πr³.',
                note=EXP + 'Essential: hemisphere slice radius √(r² - y²) (Pythagorean), area π(r² - y²); the other slice is a ring with outer radius r and inner radius y (the cone radius at height y), '
                           'area πr² - πy²; equal areas at every height and equal heights; Cavalieri; volume cylinder minus cone = ⅔πr³; double.'),
          sa('Let r = 5 and y = 3. Find the cross-section areas of the hemisphere and of the cylinder-minus-cone at height y.', 'Answer:', key='Both 16π', note='Form required: both. 25π - 9π.'),
          sa('Let r = 6. Find the volume of the cylinder-minus-cone and compare it with ⅔πr³.', 'Answer:', key='216π - 72π = 144π = ⅔π(216)', note='Form required: the computation and the comparison.'),
          sa('Explain why a stack of coins pushed into a slanted stack keeps its volume, using Cavalieri\'s principle.', 'Answer:', key='Each coin (cross-section) has the same area at every height, so the volumes are equal.',
             note='Any equivalent explanation.'),
          mc('Cavalieri\'s principle requires', ['equal heights and equal cross-section areas at every level', 'equal surface areas', 'congruent bases only', 'the same shape at every level'],
             note='Statement.'),
      ],
      back=[
          B('Cavalieri\'s principle for prisms and cylinders', 'HSG-GMD.A.1', [
              tf('Solids with equal heights and equal cross-section areas at every level have equal volumes.', key=True, note='Principle.'),
              sa('An oblique cylinder has radius 2 and height 5. Exact volume?', 'Volume:', key='20π', note='Form required: exact value.'),
              mc('A prism and a cylinder both have base area 30 and height 4. Volumes?', ['Both 120', '120 and 40', '30 and 4', 'Cannot tell'], note='Cavalieri.'),
              sa('State what must be equal for Cavalieri\'s principle.', 'Answer:', key='The heights and the cross-section areas at every level.', note='Any equivalent answer.'),
              tf('Cavalieri\'s principle needs the cross-sections to be the same shape.', key=False, note='Only equal areas.'),
          ], align='exact',
            why=why('the student does not know the principle.', 'the sphere argument rests on it.', 'states and applies it.')),
          B('Cross-section radius with the Pythagorean Theorem', '8.G.B.7', [
              sa('A sphere of radius 5 is sliced 3 units from its center. Radius of the slice?', 'Radius:', key='4', note='Any equivalent form.'),
              sa('Radius r, height y: slice radius?', 'Radius:', key='√(r² - y²)', note='Any equivalent form.'),
              mc('Radius 10, height 6: slice radius', ['8', '4', '16', '√136'], note='100 - 36.'),
              tf('The slice radius, the height, and the sphere radius form a right triangle.', key=True, note='Right angle at the slice center.'),
              tf('Slices of a hemisphere get bigger as y increases.', key=False, note='Smaller.'),
          ], align='exact',
            why=why('the student cannot find the slice radius.', 'the hemisphere slice area needs it.', 'uses the Pythagorean Theorem in 3-D.')),
          B('Volumes of cylinders and cones', 'HSG-GMD.A.3', [
              sa('Cylinder r = 6, h = 6: exact volume?', 'Volume:', key='216π', note='Form required: exact value.'),
              sa('Cone r = 6, h = 6: exact volume?', 'Volume:', key='72π', note='Form required: exact value.'),
              mc('Cylinder minus cone (same r and h = r) =', ['⅔πr³', '⅓πr³', 'πr³', '4/3 πr³'], note='πr³ - ⅓πr³.'),
              tf('A cone is ⅓ of the cylinder with the same base and height.', key=True, note='Formula.'),
              tf('πr³ - ⅓πr³ = ⅓πr³', key=False, note='⅔πr³.'),
          ], align='exact',
            why=why('the student cannot compute the comparison solid.', 'its volume becomes the hemisphere\'s.', 'computes those volumes.')),
          B('Area of a ring', '7.G.B.4', [
              sa('Ring with outer radius 5 and inner radius 3: exact area?', 'Area:', key='16π', note='Form required: exact value.'),
              tf('Ring area = π(R² - r²)', key=True, note='Subtract.'),
              mc('Ring with outer 4 and inner 1:', ['15π', '9π', '3π', '16π'], note='16 - 1.'),
              sa('Ring with outer r and inner y: area?', 'Area:', key='π(r² - y²)', note='Any equivalent form.'),
              tf('Ring area = π(R - r)²', key=False, note='π(R² - r²).'),
          ], align='supporting',
            why=why('the student cannot find the ring area.', 'the comparison slice is a ring.', 'computes ring areas.')),
      ],
      f1=B('Use Cavalieri\'s principle for other solids', 'HSG-GMD.A.2', [
          sa('A twisted tower and a straight prism both have height 50 m and every horizontal slice is a 10 m by 10 m square. Compare their volumes.', 'Answer:', key='Equal: 5,000 m³ each',
             note='Form required: the comparison with the value.'),
          sa('A pyramid with base area 36 and height 10 and a cone with base area 36 and height 10: compare volumes.', 'Answer:', key='Equal: 120 each', note='Form required: the comparison with the value.'),
          tf('Cavalieri\'s principle shows that every pyramid with base area B and height h has volume ⅓Bh, once one such pyramid is known.', key=True, note='Equal slices.'),
          mc('Two solids of height 8 have slice areas 5 and 5 at every level. Volumes?', ['Both 40', '40 and 13.3', '5 each', 'Cannot tell'], note='5 × 8.'),
          sa('Two solids have equal heights, but at one level their slice areas differ. Can Cavalieri\'s principle be used? Explain.', 'Answer:', key='No: the areas must be equal at every level.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Apply the principle to solids beyond the sphere (twisted solids, pyramids and cones).'),
      f2=B('Model a dome as a hemispherical shell', 'HSG-MG.A.2', [
          sa('A concrete dome is a hemispherical shell with outer radius 10 m and inner radius 9.5 m. Find the volume of concrete to the nearest tenth of a cubic meter.', 'Volume:',
             key='%s m³' % d1(DOME), note='Rounding to 0.1 required. ⅔π(10³ - 9.5³).'),
          sa('Concrete has density 2.4 t/m³. Estimate the dome\'s mass to the nearest ton.', 'Mass:', key='%d t' % round(DOME * 2.4), note='Rounding to the nearest ton required.'),
          tf('A shell\'s volume is the outer volume minus the inner volume.', key=True, note='Subtract.'),
          mc('A hemisphere of radius 3 has volume', ['18π', '36π', '9π', '27π'], note='⅔π · 27.'),
          sa('A hemispherical shell has outer radius 10 m and inner radius 9.5 m. Why is its volume NOT ⅔π(10 - 9.5)³?', 'Answer:', key='Volumes subtract, not radii: the shell is the difference of two hemispheres.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use the justified sphere volume in a model with density.',
        builds='Builds on FORWARD 1: volumes justified by Cavalieri are used in a structural model.')),
]
