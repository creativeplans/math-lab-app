"""G-C: circles (sets 53-63)."""
import math

from qb import S, B, sa, mc, tf, plot
from common import gd, grid_fig, NTS, proof


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


PR = 'Any valid proof (paragraph, two-column, or flow). '
TOOLS = 'Compass and straightedge only; leave all arcs.'
EV = 'Grade the construction marks, not only the final figure: '


def on(deg, r=2.0, c=(0, 0)):
    a = math.radians(deg)
    return (round(c[0] + r * math.cos(a), 6), round(c[1] + r * math.sin(a), 6))


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def d2(x):
    return '%.2f' % round(x + 1e-12, 2)


def circ(points, items=(), desc='', h=240, lab=None, r=2.0):
    P = {'O': (0, 0)}
    P.update({k: on(v, r) for k, v in points.items()})
    return gd(P, [('circle', 'O', r)] + list(items), h=h, lab=lab or {'O': 'sw'}, desc=desc)


INSC = circ({'A': 200, 'B': 340, 'C': 95}, [('seg', 'C', 'A'), ('seg', 'C', 'B'), ('seg', 'O', 'A', {'dash': True}), ('seg', 'O', 'B', {'dash': True}),
                                             ('ang', 'C', 'A', 'B'), ('ang', 'O', 'A', 'B')],
            desc='Circle with center O. Points A, B, C are on the circle with C at the top. Inscribed angle ACB and central angle AOB (dashed radii) both intercept arc AB at the bottom.')
DIAM = circ({'A': 180, 'B': 0, 'C': 60}, [('seg', 'A', 'B'), ('seg', 'A', 'C'), ('seg', 'C', 'B')],
            desc='Circle with center O and diameter AB (horizontal). Point C is on the circle above AB; segments AC and CB form triangle ACB.')
TAN = gd({'O': (0, 0), 'T': (0, -2), 'P': (3, -2)}, [('circle', 'O', 2), ('seg', 'O', 'T'), ('line', (-2.5, -2), 'P'), ('ra', 'T', 'O', 'P')], h=240, lab={'O': 'n', 'T': 's'},
         desc='Circle with center O and radius OT drawn to point T at the bottom. A line touches the circle only at T and passes through P to the right; a right-angle mark is at T.')
CYC = circ({'A': 150, 'B': 40, 'C': 300, 'D': 215}, [('poly', ['A', 'B', 'C', 'D'])], lab={'O': 'n'},
           desc='Quadrilateral ABCD with all four vertices on a circle with center O.')

SETS = [
    # ------------------------------------------------------------------ 53. C.A.1 all circles similar
    S('HSG-C.A.1', 'Prove that all circles are similar',
      target='Prove that any two circles are similar by giving a similarity transformation that maps one onto the other', strand='core', covers=['C1-similar'],
      main=[
          proof('Circle C has center A and radius r, and circle D has center B and radius s. Prove that the two circles are similar.',
                method='Translate A to B, then dilate about B with scale factor s/r. Show the image of C is exactly D.', key='A translation followed by a dilation maps C onto D, so they are similar.',
                note=PR + 'Essential: (1) the translation maps C onto the circle with center B and radius r (distances kept); (2) the dilation about B with factor s/r maps each point at distance r '
                     'from B to a point at distance s on the same ray, so onto D; (3) every point of D is reached (the inverse dilation); a similarity transformation exists. '
                     'Invalid: "circles all look alike"; only checking two specific circles.'),
          proof('Circle C₁ has center (1, 2) and radius 3. Circle C₂ has center (-4, 0) and radius 6. Describe a similarity transformation that maps C₁ onto C₂ and explain why it works.',
                method='Give the translation that moves the centers together and the dilation (center and factor).',
                key='Translate 5 units left and 2 units down, then dilate about (-4, 0) with scale factor 2.',
                note=PR + 'Essential: the translation (x, y) → (x - 5, y - 2) moves the center to (-4, 0) keeping the radius 3; the dilation about (-4, 0) by 2 doubles every distance from the center, so radius 6.'),
          sa('In the proof that all circles are similar, why must the scale factor be the ratio of the radii (s/r)?', 'Answer:',
             key='A dilation about the center multiplies every distance from the center by the factor, so the radius r must become s: k · r = s.', note='Any equivalent explanation.'),
          proof('Explain why two circles with the same center but different radii, r and s, are similar using only ONE transformation.', method='Name the transformation and its center and factor.',
                key='The dilation about the common center with factor s/r maps the first circle onto the second.', note=PR + 'Essential: dilation about the shared center; factor s/r; each point at distance r goes to distance s.'),
          tf('A circle can be similar to an ellipse that is not a circle.', key=False, note='A similarity keeps the ratio of all distances from the center, so the image of a circle is a circle.'),
      ],
      back=[
          B('A dilation multiplies distances by the scale factor', 'HSG-SRT.A.1.b', [
              sa('A dilation with factor 2.5 is applied to a segment of length 4. How long is the image?', 'Length:', key='10', note='Any equivalent form.'),
              tf('A dilation about point O keeps O fixed and multiplies each distance from O by the factor.', key=True, note='Definition.'),
              mc('Which factor maps a circle of radius 4 about its center to one of radius 10?', ['2.5', '6', '0.4', '40'], note='10 ÷ 4.'),
              sa('A circle of radius 9 is dilated about its center by ⅓. New radius?', 'Radius:', key='3', note='Any equivalent form.'),
              tf('A dilation can turn a circle into a square.', key=False, note='It keeps shape.'),
          ], align='exact',
            why=why('the student does not know what a dilation does to distances.', 'the proof scales the radius.', 'applies scale factors to radii.')),
          B('Translate a point to another point', '8.G.A.3', [
              sa('Which translation moves (1, 2) onto (-4, 0)?', 'Answer:', key='5 units left and 2 units down', note='Any equivalent form.'),
              tf('A translation keeps the radius of a circle.', key=True, note='It is a rigid motion.'),
              mc('A circle centered at (3, 3) is translated by (x, y) → (x - 3, y + 1). New center?', ['(0, 4)', '(6, 2)', '(3, 4)', '(0, 3)'], note='Apply the rule.'),
              sa('A translation moves (2, -1) to (7, 4). Describe it.', 'Answer:', key='5 units right and 5 units up', note='Any equivalent form.'),
              tf('A translation changes the size of a figure.', key=False, note='Rigid motion.'),
          ], align='exact',
            why=why('the student cannot move one center onto the other.', 'the proof starts with a translation.', 'finds translations.')),
          B('A circle is all points at one distance from its center', 'HSG-CO.A.1', [
              tf('Every point of a circle is the same distance from its center.', key=True, note='Definition.'),
              sa('A circle has center (0, 0) and passes through (3, 4). Its radius?', 'Radius:', key='5', note='Any equivalent form.'),
              mc('A circle is completely determined by', ['its center and radius', 'its center only', 'one point on it', 'its color'], note='Definition.'),
              sa('Two circles have the same center and the same radius. What can you say?', 'Answer:', key='They are the same circle.', note='Any equivalent answer.'),
              tf('A circle\'s radius can be different in different directions.', key=False, note='The definition requires one distance.'),
          ], align='exact',
            why=why('the student does not use the definition.', 'the proof checks distances from the center.', 'uses the definition.')),
      ],
      f1=B('Find a single dilation that maps one circle onto another', 'HSG-C.A.1', [
          sa('Circle P: center (0, 0), radius 2. Circle Q: center (6, 0), radius 4. Find the center of the dilation with a positive factor that maps P onto Q.', 'Center:', key='(-6, 0)',
             note='Form required: an ordered pair. The center (c, 0) satisfies 6 = c + 2(0 - c), so c = -6; check: (0, 0) → -6 + 2(0 + 6) = 6, and the radius 2 → 4.'),
          sa('For the same circles, what is the scale factor?', 'Factor:', key='2', note='Any equivalent form. 4 ÷ 2.'),
          tf('Two circles with different radii can always be mapped onto each other by one dilation.', key=True, note='Choose the center on the line of centers.'),
          mc('Circles with equal radii and different centers are related by', ['a translation (no dilation needed)', 'a dilation with factor 2', 'a reflection only', 'nothing'],
             note='Same size: congruent.'),
          sa('Circle A has radius 3 and circle B has radius 12, both centered at the origin. Which dilation maps A onto B?', 'Answer:', key='Center (0, 0), factor 4', note='Form required: both.'),
      ], prog='same-course deepening', demand='Find the single dilation (center and factor) relating two circles, an inverse problem.'),
      f2=B('Arcs of similar circles scale with the radius', 'HSG-C.B.5', [
          sa('Two circles have radii 3 and 7. A 60° central angle cuts off an arc in each. What is the ratio of the arc lengths?', 'Ratio:', key='3 : 7', note='Any equivalent form.'),
          sa('A 90° arc of a circle with radius 4 has length 2π. How long is a 90° arc of a circle with radius 10?', 'Length:', key='5π', note='Form required: exact value.'),
          tf('For a fixed central angle, arc length divided by radius is the same in every circle.', key=True, note='This constant is the radian measure.'),
          mc('An arc of length 6 in a circle of radius 2 corresponds, by similarity, to what arc length in a circle of radius 5 (same angle)?', ['15', '9', '2.4', '30'], note='Multiply by 5/2.'),
          sa('Explain how the similarity of circles leads to radian measure.', 'Answer:', key='Since arc length is proportional to radius for a fixed angle, arc/radius depends only on the angle; that number is the angle in radians.',
             note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Use the similarity of circles to compare arcs (the start of radian measure).',
        builds='A second extension of MAIN: FORWARD 1 finds the dilation; FORWARD 2 uses the similarity to scale arc lengths.')),

    # ------------------------------------------------------------------ 54. C.A.2 inscribed and central
    S('HSG-C.A.2', 'Relate inscribed angles and central angles',
      target='Identify and describe the relationship between a central angle and an inscribed angle that intercept the same arc', strand='core', covers=['C2-inscribed'],
      main=[
          sa('In circle O, central angle AOB measures 110°. Inscribed angle ACB intercepts the same arc AB. Find m∠ACB.', 'm∠ACB =', key='55°', fig=INSC,
             note='Any equivalent form. An inscribed angle is half the central angle on the same arc.'),
          sa('In circle O, inscribed angle PQR measures 38°. Find the measure of arc PR (the arc it intercepts) and of central angle POR.', 'Answer:', key='Arc PR = 76°; ∠POR = 76°',
             note='Form required: both. The central angle equals its arc.'),
          proof('In circle O, AC is a diameter and B is another point on the circle. Prove that m∠BAC = ½ m∠BOC (the inscribed angle theorem when one side of the angle is a diameter).',
                method='Use isosceles triangle AOB (OA = OB) and the exterior angle theorem at O.', key='m∠BAC = ½ m∠BOC',
                note=PR + 'Essential: OA = OB (radii), so ∠OAB ≅ ∠OBA; ∠BOC is an exterior angle of △AOB, so m∠BOC = m∠OAB + m∠OBA = 2m∠BAC.'),
          mc('Inscribed angle XYZ and central angle XOZ intercept the same arc XZ, and m∠XYZ = 47°. What is m∠XOZ?', ['94°', '47°', '23.5°', '133°'], note='Double the inscribed angle.'),
          tf('An inscribed angle and a central angle that intercept the same arc have equal measures.', key=False, note='The inscribed angle is half the central angle.'),
      ],
      back=[
          B('Base angles of an isosceles triangle are congruent', 'HSG-CO.C.10', [
              sa('In △AOB, OA = OB and m∠OAB = 35°. Find m∠OBA and m∠AOB.', 'Answer:', key='35° and 110°', note='Form required: both.'),
              tf('Two radii of a circle and the chord joining their ends form an isosceles triangle.', key=True, note='The radii are equal.'),
              mc('Isosceles triangle with vertex angle 80°. Each base angle?', ['50°', '80°', '40°', '100°'], note='(180 - 80)/2.'),
              sa('In △OPQ with OP = OQ, m∠P = 2x and m∠Q = 50°. Find x.', 'x =', key='25', note='Any equivalent form.'),
              tf('In an isosceles triangle, the vertex angle always equals a base angle.', key=False, note='Only when equilateral.'),
          ], align='exact',
            why=why('the student misses the isosceles triangle formed by two radii.', 'the proof uses its base angles.', 'uses isosceles base angles.')),
          B('The exterior angle theorem', 'HSG-CO.C.10', [
              sa('A triangle has remote interior angles 30° and 30°. Find the exterior angle.', 'Angle:', key='60°', note='Any equivalent form.'),
              tf('An exterior angle equals the sum of the two remote interior angles.', key=True, note='Theorem.'),
              mc('Exterior angle 100°, one remote interior angle 45°. The other?', ['55°', '45°', '80°', '135°'], note='100 - 45.'),
              sa('If both remote interior angles equal x, the exterior angle is', 'Answer:', key='2x', note='Any equivalent form.'),
              tf('An exterior angle equals the adjacent interior angle.', key=False, note='They are supplementary.'),
          ], align='exact',
            why=why('the student cannot get the doubling.', 'the central angle is an exterior angle of the isosceles triangle.', 'applies the exterior angle theorem.')),
          B('A central angle and its arc have the same measure', '4.MD.C.5.a', [
              sa('A central angle cuts off ¼ of a circle. Its measure?', 'Measure:', key='90°', note='Any equivalent form.'),
              tf('The measure of a minor arc equals its central angle.', key=True, note='Definition of arc measure.'),
              mc('An arc measures 70°. Its central angle measures', ['70°', '35°', '140°', '290°'], note='Equal.'),
              sa('A central angle of 150°. What fraction of the circle is its arc?', 'Fraction:', key='5/12', note='Any equivalent form.'),
              tf('All arcs of 60° have the same length.', key=False, note='Length depends on the radius.'),
          ], align='supporting',
            why=why('the student does not connect central angles with arcs.', 'the relationship is stated with arcs.', 'converts between arcs and central angles.')),
      ],
      f1=B('Prove the inscribed angle theorem when the center is inside or outside the angle', 'HSG-C.A.2', [
          proof('Inscribed angle ABC has the center O inside it. Prove that m∠ABC = ½ m∠AOC. (Draw diameter BD.)',
                method='Split ∠ABC and ∠AOC along BD and apply the diameter case twice, then add.', key='m∠ABC = ½ m∠AOC',
                note=PR + 'Essential: m∠ABD = ½m∠AOD and m∠DBC = ½m∠DOC (diameter case); add: m∠ABC = ½(m∠AOD + m∠DOC) = ½m∠AOC.'),
          proof('Inscribed angle ABC has the center O outside it. Prove that m∠ABC = ½ m∠AOC. (Draw diameter BD.)',
                method='Use the diameter case twice and SUBTRACT.', key='m∠ABC = ½ m∠AOC',
                note=PR + 'Essential: with D such that A and C are on the same side of BD: m∠DBC = ½m∠DOC and m∠DBA = ½m∠DOA; subtract.'),
          tf('The inscribed angle theorem needs three cases for a complete proof.', key=True, note='Center on a side, inside, or outside.'),
          mc('In the "center inside" case, the two diameter-case results are', ['added', 'subtracted', 'multiplied', 'averaged'], note='The angle is the sum of two pieces.'),
          sa('Why can\'t the proof stop after the diameter case?', 'Answer:', key='Most inscribed angles do not have a diameter as a side; the other positions must be covered too.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Complete the proof for every position of the center (all three cases).'),
      f2=B('Inscribed angles on the same arc, and arc applications', 'HSG-C.A.2', [
          sa('Inscribed angles ∠ADB and ∠ACB intercept the same arc AB, and m∠ADB = 41°. Find m∠ACB.', 'm∠ACB =', key='41°', note='Any equivalent form.'),
          proof('Prove that two inscribed angles that intercept the same arc are congruent.', method='Each is half the same central angle.', key='They are congruent.',
                note=PR + 'Essential: each equals ½ of the central angle on that arc (inscribed angle theorem).'),
          tf('An inscribed angle that intercepts a 200° arc measures 100°.', key=True, note='Half the arc.'),
          mc('Points A, B, C, D are on a circle with arc AB = 80° and arc CD = 50° (arcs not containing the other points). Chords AC and BD meet at E inside. m∠AEB?', ['65°', '130°', '30°', '15°'],
             note='Angle formed by two chords = half the sum of the intercepted arcs: (80 + 50)/2.'),
          sa('An inscribed angle measures 3x + 10 and its intercepted arc measures 110°. Find x.', 'x =', key='15', note='Any equivalent form. 3x + 10 = 55.'),
      ], prog='same-course deepening', demand='Derive consequences of the theorem (congruent inscribed angles, angles between chords) and use them.',
        builds='Builds on FORWARD 1: with the theorem proved in all cases, its consequences follow.')),
]

CIRCA = gd({'O': (0, 0), 'P': (4, 0), 'A': on(60), 'B': on(-60)}, [('circle', 'O', 2), ('seg', 'O', 'A'), ('seg', 'O', 'B'), ('seg', 'P', 'A'), ('seg', 'P', 'B'),
                                                                  ('ra', 'A', 'O', 'P'), ('ra', 'B', 'O', 'P')], h=240, lab={'O': 'w', 'P': 'e'},
           desc='Circle with center O. From external point P, two tangent segments PA and PB touch the circle at A and B; radii OA and OB are drawn with right-angle marks at A and B. '
                'Angle APB is the circumscribed angle and angle AOB the central angle.')
CHORD = gd({'O': (0, 0), 'A': on(150, 2.5), 'B': on(30, 2.5), 'M': (0, 1.25)}, [('circle', 'O', 2.5), ('seg', 'A', 'B'), ('seg', 'O', 'M'), ('seg', 'O', 'B', {'dash': True}),
                                                                             ('ra', 'M', 'B', 'O')], h=240, lab={'O': 's', 'M': 'n'},
           desc='Circle with center O and chord AB. Segment OM is drawn from O to the chord with a right-angle mark at M; radius OB is dashed.')

SETS += [
    # ------------------------------------------------------------------ 55. C.A.2 diameter
    S('HSG-C.A.2', 'Inscribed angles on a diameter are right angles',
      target='Explain why an angle inscribed in a semicircle (on a diameter) is a right angle, and use it', strand='core', covers=['C2-diameter'],
      main=[
          proof('AB is a diameter of circle O and C is any other point on the circle. Prove that ∠ACB is a right angle.', fig=DIAM,
                method='Use the inscribed angle theorem (the intercepted arc is 180°), or the two isosceles triangles AOC and BOC.', key='m∠ACB = 90°',
                note=PR + 'Essential (theorem): ∠ACB intercepts a semicircle, 180°, so it measures 90°. Alternative: OA = OC = OB, so △AOC and △BOC are isosceles; with base angles x and y, '
                     'the angle sum of △ABC gives 2x + 2y = 180°, so x + y = 90° = m∠ACB.'),
          sa('AB is a diameter of a circle and C is on the circle. AC = 6 and BC = 8. Find AB and the radius.', 'Answer:', key='AB = 10; radius 5',
             note='Form required: both. ∠C = 90°, so AB = √(36 + 64).'),
          sa('AB is a diameter of circle O and C is on the circle with m∠CAB = 34°. Find m∠CBA.', 'm∠CBA =', key='56°', note='Any equivalent form. ∠C = 90°.'),
          mc('Triangle PQR is inscribed in a circle with PR a diameter. Which statement must be true?', ['∠Q = 90°', '∠P = 90°', 'PQ = QR', 'PR = PQ'], note='The angle opposite the diameter.'),
          tf('Every triangle inscribed in a circle is a right triangle.', key=False, note='Only when one side is a diameter.'),
      ],
      back=[
          B('Use the inscribed angle theorem', 'HSG-C.A.2', [
              sa('An inscribed angle intercepts an arc of 140°. Its measure?', 'Measure:', key='70°', note='Any equivalent form.'),
              tf('An inscribed angle is half its intercepted arc.', key=True, note='Theorem.'),
              mc('A semicircle measures', ['180°', '90°', '360°', '120°'], note='Half the circle.'),
              sa('An inscribed angle measures 25°. Its arc?', 'Arc:', key='50°', note='Any equivalent form.'),
              tf('An inscribed angle equals its intercepted arc.', key=False, note='Half.'),
          ], align='exact',
            why=why('the student does not use the inscribed angle theorem.', 'the result is the case of a 180° arc.', 'applies the theorem.')),
          B('Isosceles triangles from radii', 'HSG-CO.C.10', [
              sa('OA = OC (radii) and m∠OAC = 40°. Find m∠OCA.', 'Measure:', key='40°', note='Any equivalent form.'),
              tf('Any two radii and the chord between them form an isosceles triangle.', key=True, note='Equal radii.'),
              mc('In △OBC with OB = OC, m∠BOC = 100°. m∠OBC =', ['40°', '50°', '80°', '100°'], note='(180 - 100)/2.'),
              sa('Why are ∠OAC and ∠OCA congruent when OA = OC?', 'Answer:', key='Base angles of an isosceles triangle are congruent.', note='Any equivalent answer.'),
              tf('A radius is always longer than a chord.', key=False, note='Chords can be longer (up to the diameter).'),
          ], align='exact',
            why=why('the student misses the isosceles triangles.', 'the alternative proof uses them.', 'uses equal radii.')),
          B('Triangle angle sum', '8.G.A.5', [
              sa('Two angles of a triangle are 90° and 34°. The third?', 'Angle:', key='56°', note='Any equivalent form.'),
              tf('The acute angles of a right triangle add to 90°.', key=True, note='180 - 90.'),
              mc('2x + 2y = 180. Then x + y =', ['90', '180', '45', '360'], note='Divide by 2.'),
              sa('A triangle has angles x, x, and 2x. Find 2x.', 'Answer:', key='90°', note='4x = 180.'),
              tf('A triangle can have angles 90°, 60°, and 40°.', key=False, note='They add to 190°.'),
          ], align='exact',
            why=why('the student cannot finish the angle argument.', 'the proof ends with the angle sum.', 'uses the angle sum.')),
      ],
      f1=B('Use the converse to find a circle through a right triangle', 'HSG-C.A.2', [
          sa('Right triangle ABC has its right angle at C, with A(0, 0) and B(8, 6). Where is the center of the circle through A, B, and C, and what is its radius?', 'Answer:',
             key='Center (4, 3), the midpoint of AB; radius 5.', note='Form required: both. The hypotenuse is a diameter.'),
          proof('In △ABC, m∠C = 90°. Prove that C lies on the circle with diameter AB.', method='Let M be the midpoint of AB and show MC = MA (for example, by completing a rectangle).',
                key='MC = MA = MB, so C is on the circle with center M and diameter AB.',
                note=PR + 'Essential: reflect C through M to D; ACBD is a parallelogram with a right angle, so a rectangle; its diagonals are congruent and bisect each other, so MC = MA.'),
          tf('The hypotenuse of a right triangle is a diameter of its circumscribed circle.', key=True, note='Converse.'),
          mc('A right triangle has legs 5 and 12. Radius of its circumscribed circle?', ['6.5', '13', '8.5', '6'], note='Half the hypotenuse.'),
          sa('A carpenter\'s square (a right angle) is placed with its corner touching a circular board and its edges crossing the edge at P and Q. What is segment PQ?', 'Answer:',
             key='A diameter of the board.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Prove and use the converse: a right angle\'s hypotenuse is a diameter.'),
      f2=B('Use the diameter property to construct tangents from an external point', 'HSG-C.A.4', [
          plot(TOOLS + '\nConstruct the two tangent lines from point P to circle O.',
               gd({'O': (0, 0), 'P': (4.2, 0.6)}, [('circle', 'O', 1.8)], h=260, lab={'O': 'w'}, desc='Circle with center O and a point P outside it, to the right.'),
               key='Construct the midpoint M of OP; draw the circle with center M through O and P; it meets circle O at T₁ and T₂; lines PT₁ and PT₂ are tangents.',
               note=EV + 'the perpendicular bisector of OP, the circle on diameter OP, and both tangent lines.'),
          sa('Why are the lines PT₁ and PT₂ tangent?', 'Answer:', key='T₁ is on the circle with diameter OP, so ∠OT₁P = 90°; a line perpendicular to a radius at its endpoint is tangent.', note='Any equivalent answer.'),
          tf('From a point outside a circle there are exactly two tangent lines.', key=True, note='Two intersection points.'),
          mc('In the construction, the circle with diameter OP is used because', ['every angle inscribed in it on OP is a right angle', 'it has the same radius as circle O',
                                                                                   'it passes through the center only', 'it is tangent to circle O'],
             note='Right angle at the tangent point.'),
          sa('O is the center, OP = 10, and the radius is 6. How long is each tangent segment?', 'Length:', key='8', note='Any equivalent form.'),
      ], prog='cross-standard extension', demand='Use the property to construct tangents from an external point (advanced strand).',
        builds='Builds on FORWARD 1: the circle on a diameter locates the right-angle points needed for tangents.')),

    # ------------------------------------------------------------------ 56. C.A.2 tangent
    S('HSG-C.A.2', 'A radius is perpendicular to the tangent at the point of tangency',
      target='Explain why a tangent line is perpendicular to the radius at the point of tangency, and use it', strand='core', covers=['C2-tangent'],
      main=[
          proof('Line ℓ is tangent to circle O at T. Prove that OT ⊥ ℓ. (Use an indirect argument.)', fig=TAN,
                method='Suppose OT is not perpendicular; drop the perpendicular from O to ℓ at Q ≠ T; show a second point of ℓ is on the circle or inside it.', key='OT ⊥ ℓ',
                note=PR + 'Essential: if OQ ⊥ ℓ with Q ≠ T, then OQ < OT (the perpendicular is the shortest segment, as the hypotenuse OT is longest in right △OQT), so Q is inside the circle, '
                     'and then ℓ would cross the circle twice, contradicting tangency. Invalid: "it looks perpendicular".'),
          sa('Line PT is tangent to circle O at T. OT = 5 and PT = 12. Find OP.', 'OP =', key='13', note='Any equivalent form. ∠OTP = 90°.'),
          sa('A tangent from P touches circle O at T. OP = 17 and the radius is 8. Find PT.', 'PT =', key='15', note='Any equivalent form.'),
          mc('Segment PT touches circle O at T. OT = 7, PT = 24, OP = 26. Is PT tangent to the circle?', ['No, because 7² + 24² ≠ 26²', 'Yes, because it touches at T',
                                                                                                         'Yes, because 26 > 24', 'No, because 7 < 24'],
             note='Tangency requires ∠OTP = 90°, but 49 + 576 = 625 ≠ 676.'),
          tf('A line perpendicular to a radius at its endpoint on the circle is tangent to the circle.', key=True, note='Converse.'),
      ],
      back=[
          B('Use the Pythagorean Theorem and its converse', '8.G.B.7', [
              sa('Legs 5 and 12. Hypotenuse?', 'Hypotenuse:', key='13', note='Any equivalent form.'),
              sa('Hypotenuse 17, leg 8. Other leg?', 'Leg:', key='15', note='Any equivalent form.'),
              tf('A triangle with sides 7, 24, 25 is a right triangle.', key=True, note='49 + 576 = 625.'),
              mc('Sides 6, 8, 11. Right triangle?', ['No', 'Yes', 'Only if 11 is a leg', 'Cannot tell'], note='36 + 64 ≠ 121.'),
              tf('The Pythagorean Theorem applies to any triangle.', key=False, note='Right triangles only.'),
          ], align='exact',
            why=why('the student cannot compute with the right triangle formed by the radius and tangent.', 'tangent problems are right-triangle problems.', 'uses the theorem and converse.')),
          B('The perpendicular is the shortest segment from a point to a line', '7.G.A.2', [
              tf('The shortest segment from a point to a line is perpendicular to the line.', key=True, note='Any other segment is a hypotenuse.'),
              sa('In a right triangle, which side is longest?', 'Answer:', key='The hypotenuse', note='Any equivalent answer.'),
              mc('O is 4 cm from line ℓ (perpendicular distance). Another segment from O to ℓ could be', ['5 cm', '3 cm', '2 cm', '4 cm only'], note='At least 4 cm.'),
              sa('Why is the perpendicular segment shorter than any slanted one?', 'Answer:', key='Each slanted segment is the hypotenuse of a right triangle with the perpendicular as a leg.', note='Any equivalent answer.'),
              tf('The distance from a point to a line is measured along any segment.', key=False, note='Along the perpendicular.'),
          ], align='supporting',
            why=why('the student does not know the shortest-distance fact.', 'the indirect proof relies on it.', 'explains shortest distance.')),
          B('A tangent touches a circle at exactly one point', 'HSG-CO.A.1', [
              tf('A tangent line meets the circle at exactly one point.', key=True, note='Definition.'),
              mc('A line meets a circle at two points. It is a', ['secant', 'tangent', 'radius', 'diameter'], note='Two points.'),
              sa('Point Q on a line is inside the circle. Can the line be tangent?', 'Answer:', key='No; it would cross the circle twice.', note='Any equivalent answer.'),
              sa('What is the point where a tangent touches the circle called?', 'Answer:', key='The point of tangency', note='Any equivalent answer.'),
              tf('A tangent can pass through the center.', key=False, note='Then it would meet the circle twice.'),
          ], align='supporting',
            why=why('the student is unclear what tangent means.', 'the proof uses the one-point property.', 'uses the definition.')),
      ],
      f1=B('Tangent segments from an external point are congruent', 'HSG-C.A.2', [
          proof('From point P outside circle O, tangent segments PA and PB touch the circle at A and B. Prove that PA = PB.', fig=CIRCA,
                method='Use the right angles at A and B, OA = OB, and the shared hypotenuse OP (HL, or the Pythagorean Theorem).', key='PA = PB',
                note=PR + 'Essential: ∠OAP = ∠OBP = 90°; OA = OB; OP shared; HL (or PA = √(OP² - r²) = PB).'),
          sa('Tangent segments from P to a circle are 3x + 4 and 25. Find x.', 'x =', key='7', note='Any equivalent form.'),
          tf('The segment from P to the center bisects the angle between the two tangents.', key=True, note='Congruent triangles.'),
          mc('A circle is inscribed in a triangle with sides tangent to it. From one vertex, the two tangent segments are', ['equal', 'unequal', 'perpendicular', 'parallel'], note='Same external point.'),
          sa('A circle is tangent to all sides of a quadrilateral ABCD. AB = 9, BC = 11, CD = 13. Find DA.', 'DA =', key='11', note='Any equivalent form. AB + CD = BC + DA.'),
      ], prog='same-course deepening', demand='Prove and use a new consequence: tangent segments from one point are congruent.'),
      f2=B('Write the equation of a tangent line in the coordinate plane', 'HSG-GPE.B.5', [
          sa('Find an equation of the line tangent to x² + y² = 25 at (3, 4).', 'Equation:', key='y = -¾x + 25/4', note='Any equivalent form, such as 3x + 4y = 25. The radius has slope 4/3.'),
          sa('Find an equation of the tangent to x² + y² = 13 at (2, -3).', 'Equation:', key='2x - 3y = 13', note='Any equivalent form. Radius slope -3/2; tangent slope 2/3.'),
          tf('A tangent line\'s slope is the negative reciprocal of the radius\'s slope (when neither is vertical or horizontal).', key=True, note='Perpendicular slopes.'),
          mc('The tangent to x² + y² = 16 at (0, 4) is', ['y = 4', 'x = 0', 'y = x + 4', 'x = 4'], note='The radius is vertical, so the tangent is horizontal.'),
          sa('Is y = 7 tangent to the circle with center (2, 3) and radius 4? Explain.', 'Answer:', key='Yes: the distance from (2, 3) to the line y = 7 is 4, the radius.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Use radius ⊥ tangent with slopes to write tangent line equations.',
        builds='A second extension of MAIN: FORWARD 1 stays synthetic; FORWARD 2 moves the same fact to coordinates.')),

    # ------------------------------------------------------------------ 57. C.A.2 circumscribed angles
    S('HSG-C.A.2', 'Relate circumscribed angles and central angles',
      target='Describe and use the relationship between a circumscribed angle and the central angle that intercepts the same arc (they are supplementary)', strand='core', covers=['C2-circumscribed'],
      main=[
          proof('Tangents from P touch circle O at A and B. Prove that m∠APB + m∠AOB = 180°.', fig=CIRCA,
                method='Use the right angles at A and B and the angle sum of quadrilateral OAPB.', key='m∠APB + m∠AOB = 180°',
                note=PR + 'Essential: ∠OAP = ∠OBP = 90° (radius ⊥ tangent); the angles of quadrilateral OAPB add to 360°; so m∠APB + m∠AOB = 360° - 180° = 180°.'),
          sa('The circumscribed angle APB measures 52°. Find the central angle AOB and the minor arc AB.', 'Answer:', key='∠AOB = 128°; arc AB = 128°', note='Form required: both.'),
          sa('Minor arc AB measures 100°. Find the circumscribed angle formed by the tangents at A and B.', 'Angle:', key='80°', note='Any equivalent form.'),
          mc('A circumscribed angle measures 90°. The quadrilateral formed by the center, the two tangent points, and the vertex is a', ['square', 'rhombus that is not a square',
                                                                                                                                         'kite that is not a square', 'trapezoid'],
             note='All four angles are 90°, so OAPB is a rectangle; its opposite sides give OA = PB, and with PA = PB and OA = OB all four sides are equal, so it is a square.'),
          tf('A circumscribed angle and its central angle are congruent.', key=False, note='They are supplementary.'),
      ],
      back=[
          B('A tangent is perpendicular to the radius at the point of tangency', 'HSG-C.A.2', [
              tf('The radius to the point of tangency is perpendicular to the tangent.', key=True, note='Theorem.'),
              sa('What is m∠OAP when PA is tangent at A?', 'Measure:', key='90°', note='Any equivalent form.'),
              mc('In quadrilateral OAPB with tangents PA and PB, how many right angles are certain?', ['2', '4', '1', '0'], note='At A and B.'),
              sa('Tangent PA, radius OA = 9, PA = 12. OP?', 'OP =', key='15', note='Any equivalent form.'),
              tf('The angle between a tangent and a radius can be 60°.', key=False, note='Always 90° at the point of tangency.'),
          ], align='exact',
            why=why('the student does not use the right angles.', 'they are the key to the relationship.', 'uses radius ⊥ tangent.')),
          B('The angles of a quadrilateral add to 360°', '8.G.A.5', [
              sa('A quadrilateral has angles 90°, 90°, and 70°. The fourth?', 'Angle:', key='110°', note='Any equivalent form.'),
              tf('A diagonal splits a quadrilateral into two triangles, so its angles add to 360°.', key=True, note='2 × 180.'),
              mc('Two angles of a quadrilateral are right angles. The other two must', ['add to 180°', 'each be 90°', 'add to 90°', 'add to 360°'], note='360 - 180.'),
              sa('Angles x, 90°, 90°, 2x in a quadrilateral. Find x.', 'x =', key='60', note='Any equivalent form.'),
              tf('The angles of a quadrilateral add to 180°.', key=False, note='360°.'),
          ], align='exact',
            why=why('the student does not know the quadrilateral angle sum.', 'the proof uses it.', 'applies 360°.')),
          B('Supplementary angles add to 180°', '7.G.B.5', [
              sa('Find the supplement of 52°.', 'Supplement:', key='128°', note='Any equivalent form.'),
              tf('Supplementary angles add to 180°.', key=True, note='Definition.'),
              mc('Angles x and 3x are supplementary. x =', ['45°', '60°', '30°', '90°'], note='4x = 180.'),
              sa('If two angles are supplementary and one is obtuse, the other is', 'Answer:', key='acute', note='Any equivalent answer.'),
              tf('Supplementary angles must form a linear pair.', key=False, note='They need not be adjacent.'),
          ], align='exact',
            why=why('the student does not know "supplementary".', 'the relationship is supplementary angles.', 'finds supplements.')),
      ],
      f1=B('Use the circumscribed angle with arcs, including major arcs', 'HSG-C.A.2', [
          sa('The circumscribed angle at P is 40°. Find the minor arc AB and the major arc AB.', 'Answer:', key='Minor arc 140°; major arc 220°', note='Form required: both.'),
          sa('Show that a circumscribed angle equals ½(major arc - minor arc).', 'Answer:',
             key='If the minor arc is m, the major arc is 360 - m and the angle is 180 - m = ½((360 - m) - m).', note='Any equivalent algebra.'),
          tf('A circumscribed angle can measure more than 180°.', key=False, note='It is 180° minus the minor arc, so it is less than 180°.'),
          mc('Tangents from P make a 70° angle. An inscribed angle intercepting the minor arc AB measures', ['55°', '110°', '35°', '70°'], note='Minor arc = 110°, inscribed angle = 55°.'),
          sa('The minor arc between two tangent points is x°, and the circumscribed angle is (x - 20)°. Find x.', 'x =', key='100', note='Any equivalent form. x + x - 20 = 180.'),
      ], prog='same-course deepening', demand='Express the circumscribed angle in terms of both arcs and combine it with inscribed angles.'),
      f2=B('Angles formed by secants and tangents outside a circle', 'HSG-C.A.2', [
          proof('Two secants from P meet a circle at A, B and at C, D (A between P and B, C between P and D). Prove that m∠P = ½(arc BD - arc AC).',
                method='Draw chord BC; use the exterior angle theorem in triangle PBC and the inscribed angle theorem.', key='m∠P = ½(arc BD - arc AC)',
                note=PR + 'Essential: ∠BCD is exterior to △PBC, so m∠BCD = m∠P + m∠PBC; m∠BCD = ½ arc BD and m∠PBC = ½ arc AC; subtract.'),
          sa('Two secants from P intercept arcs of 110° and 30°. Find m∠P.', 'm∠P =', key='40°', note='Any equivalent form.'),
          tf('The angle outside a circle formed by a tangent and a secant is half the difference of the intercepted arcs.', key=True, note='Same pattern.'),
          mc('An angle outside a circle intercepts arcs of 160° and 50°. Its measure?', ['55°', '105°', '110°', '210°'], note='(160 - 50)/2.'),
          sa('Explain why the formula for two tangents is a special case of the secant formula.', 'Answer:', key='The tangent case is the limit where each secant\'s two intersection points merge; the arcs are the major and minor arcs.',
             note='Any reasonable explanation.'),
      ], prog='same-course deepening', demand='Generalize to angles formed outside the circle by secants (proof and use).',
        builds='Builds on FORWARD 1: the "half the difference of the arcs" form found there extends to secants.')),

    # ------------------------------------------------------------------ 58. C.A.2 radii and chords
    S('HSG-C.A.2', 'Relationships among radii and chords',
      target='Identify and use relationships among radii and chords: a radius perpendicular to a chord bisects it, and congruent chords are equidistant from the center', strand='core', covers=['C2-chords'],
      main=[
          proof('In circle O, OM ⊥ chord AB at M. Prove that M is the midpoint of AB.', fig=CHORD, method='Prove △OMA ≅ △OMB (HL, using OA = OB).', key='AM = MB',
                note=PR + 'Essential: OA = OB (radii); OM shared; right angles at M; HL (or the Pythagorean Theorem: AM = √(r² - OM²) = MB).'),
          sa('A circle has radius 13. A chord is 5 units from the center. How long is the chord?', 'Length:', key='24', note='Any equivalent form. Half-chord √(169 - 25) = 12.'),
          sa('A chord of length 16 is in a circle of radius 10. How far is the chord from the center?', 'Distance:', key='6', note='Any equivalent form.'),
          mc('Two chords of a circle are each 7 units from the center. Which is true?', ['The chords are congruent', 'The chords are parallel', 'The chords are perpendicular', 'The chords meet at the center'],
             note='Equidistant chords are congruent.'),
          tf('The perpendicular bisector of any chord passes through the center of the circle.', key=True, note='The center is equidistant from the chord\'s endpoints.'),
      ],
      back=[
          B('Right triangles: Hypotenuse-Leg and the Pythagorean Theorem', 'HSG-SRT.B.5', [
              sa('Right triangles with equal hypotenuses and one pair of equal legs are congruent by', 'Answer:', key='HL', note='Any equivalent form.'),
              sa('Hypotenuse 10, leg 6. Other leg?', 'Leg:', key='8', note='Any equivalent form.'),
              tf('Two radii are congruent hypotenuses in the chord figure.', key=True, note='OA = OB.'),
              mc('OM ⊥ AB in circle O. △OMA and △OMB share', ['OM', 'AB', 'OA', 'nothing'], note='Common leg.'),
              tf('HL works for any triangles.', key=False, note='Right triangles only.'),
          ], align='exact',
            why=why('the student cannot prove the two halves equal.', 'the proof uses the two right triangles.', 'uses HL and the Pythagorean Theorem.')),
          B('The perpendicular bisector theorem', 'HSG-CO.C.9', [
              tf('A point equidistant from A and B lies on the perpendicular bisector of AB.', key=True, note='Converse.'),
              sa('The center O of a circle is equidistant from the endpoints of chord AB. Why?', 'Answer:', key='OA and OB are radii.', note='Any equivalent answer.'),
              mc('So the center lies on', ['the perpendicular bisector of every chord', 'every chord', 'the circle', 'a tangent'], note='Converse.'),
              sa('Two chords\' perpendicular bisectors meet at P. What is P?', 'Answer:', key='The center of the circle', note='Any equivalent answer.'),
              tf('The perpendicular bisector of a chord can miss the center.', key=False, note='It always passes through it.'),
          ], align='exact',
            why=why('the student does not connect chords to perpendicular bisectors.', 'the center is on every chord\'s bisector.', 'applies the theorem.')),
          B('Radii of a circle are equal', 'HSG-CO.A.1', [
              sa('A circle has center O. OA = 7. Find OB if B is on the circle.', 'OB =', key='7', note='Any equivalent form.'),
              tf('All radii of one circle have the same length.', key=True, note='Definition.'),
              mc('Chord AB with OA = 5. OB =', ['5', '10', '2.5', 'unknown'], note='Radius.'),
              sa('What is the longest chord in a circle of radius 6?', 'Answer:', key='A diameter, 12', note='Any equivalent answer.'),
              tf('A chord always passes through the center.', key=False, note='Only a diameter.'),
          ], align='exact',
            why=why('the student does not see the equal radii.', 'they make the isosceles triangle.', 'uses equal radii.')),
      ],
      f1=B('Locate the center of a circle from chords', 'HSG-C.A.2', [
          plot(TOOLS + '\nThe arc below is part of a circle. Construct its center.',
               gd({'A': on(200, 2.4), 'B': on(250, 2.4), 'C': on(320, 2.4)}, [('arc', (0, 0), 2.4, 185, 335)], h=260,
                  desc='An arc of a circle (the lower part), with three points A, B, C marked on it. The center is not shown.'),
               key='Draw chords AB and BC; construct their perpendicular bisectors; they meet at the center.', note=EV + 'two chords and both perpendicular bisector constructions.'),
          sa('A circle passes through (0, 0), (8, 0), and (0, 6). Find its center.', 'Center:', key='(4, 3)', note='Form required: an ordered pair. Perpendicular bisectors x = 4 and y = 3.'),
          tf('Three points not on one line determine exactly one circle.', key=True, note='The perpendicular bisectors meet in one point.'),
          mc('Why can\'t three points on one line lie on a circle?', ['Their perpendicular bisectors are parallel, so no center exists', 'They are too close',
                                                                      'Only two points can lie on a circle', 'Three points on a line always lie on a circle'],
             note='Parallel bisectors never meet.'),
          sa('A circular plate is broken. Describe how to find its original radius from the piece.', 'Answer:', key='Mark three points on the edge, construct the perpendicular bisectors of two chords to find the center, then measure to the edge.',
             note='Any valid method.'),
      ], prog='same-course deepening', demand='Use the chord relationships in reverse to locate a circle\'s center (inverse problem).'),
      f2=B('Find chord lengths and central angles with trigonometry', 'HSG-SRT.C.8', [
          sa('A chord subtends a central angle of 80° in a circle of radius 10. Find its length to the nearest tenth.', 'Length:', key=d1(2 * 10 * math.sin(math.radians(40))),
             note='Rounding to 0.1 required. Half the chord = 10 sin 40°.'),
          sa('A chord of length 12 is in a circle of radius 10. Find the central angle to the nearest tenth of a degree.', 'Angle:', key='%s°' % d1(2 * math.degrees(math.asin(0.6))),
             note='Rounding to 0.1° required. Half-angle sin⁻¹(6/10).'),
          tf('A chord\'s length is 2r sin(θ/2) for central angle θ.', key=True, note='From the right triangle with the half-chord.'),
          mc('Central angle 60°, radius 9. Chord length?', ['9', '4.5', '18', '9√3'], note='2 · 9 · sin 30° = 9.'),
          sa('A chord equals the radius. Find its central angle.', 'Angle:', key='60°', note='Any equivalent form. Equilateral triangle.'),
      ], prog='cross-standard extension', demand='Combine the perpendicular-bisector relationship with trigonometry to relate chords and central angles.',
        builds='A second extension of MAIN: FORWARD 1 finds centers; FORWARD 2 measures chords with trigonometry.')),
]
