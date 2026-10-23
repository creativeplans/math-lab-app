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


def tri_fig(P, desc, h=270):
    return gd(P, [('poly', list(P))], h=h, desc=desc)


T1 = {'A': (0, 0), 'B': (4.4, 0), 'C': (1.4, 3)}
T2 = {'A': (0, 0), 'B': (4.6, 0), 'C': (3.6, 2.2)}
T3 = {'A': (0, 0), 'B': (3.2, 0), 'C': (0, 2.6)}
T4 = {'A': (0, 0), 'B': (4.6, 0), 'C': (-0.8, 1.9)}
PI = math.pi

SETS += [
    # ------------------------------------------------------------------ 59. C.A.3 incircle
    S('HSG-C.A.3', 'Construct the inscribed circle of a triangle',
      target='Construct the inscribed circle (incircle) of a given triangle with compass and straightedge', strand='core', covers=['C3-incircle'],
      main=[
          plot(TOOLS + '\nConstruct the inscribed circle of triangle ABC.', tri_fig(T1, 'Acute triangle ABC.'),
               key='Bisect two angles (for example ∠A and ∠B); they meet at the incenter I; construct the perpendicular from I to one side, meeting it at D; draw the circle with center I and radius ID.',
               note=EV + 'two angle bisector constructions, the perpendicular from I to a side, and the circle touching all three sides.'),
          plot(TOOLS + '\nConstruct the inscribed circle of obtuse triangle ABC.', tri_fig(T4, 'Obtuse triangle ABC with the obtuse angle at A.'),
               key='Same steps: two angle bisectors meet at I (inside the triangle), perpendicular from I to a side gives the radius, then the circle.', note=EV + 'all constructions and the circle.'),
          plot(TOOLS + '\nConstruct the inscribed circle of right triangle ABC.', tri_fig(T3, 'Right triangle ABC with the right angle at A.'),
               key='Two angle bisectors, the perpendicular from their intersection to a side, and the circle.', note=EV + 'all constructions and the circle.'),
          sa('Write the steps for constructing the inscribed circle of a triangle.', 'Steps:',
             key='1. Construct the bisectors of two angles; label their intersection I. 2. Construct the perpendicular from I to one side; label the foot D. 3. Draw the circle with center I through D.',
             note='Any equivalent steps. The radius must come from a PERPENDICULAR to a side, not from I to a vertex.'),
          mc('Why is the radius of the inscribed circle measured along a perpendicular from the incenter to a side?', ['The circle must be tangent to the side, and a tangent is perpendicular to the radius',
                                                                                                                        'The perpendicular is the longest segment', 'Any segment from I works', 'The radius goes to a vertex'],
             note='Tangent ⊥ radius at the point of tangency.'),
      ],
      back=[
          B('Construct an angle bisector', 'HSG-CO.D.12', [
              sa('How many arcs are needed to bisect an angle with compass and straightedge?', 'Answer:', key='Three (one at the vertex, then two equal arcs from the crossing points)', note='Any equivalent answer.'),
              tf('An angle bisector construction ends with a ray from the vertex.', key=True, note='Through the crossing of the equal arcs.'),
              mc('The incenter is where the', ['angle bisectors meet', 'perpendicular bisectors meet', 'medians meet', 'altitudes meet'], note='Equidistant from sides.'),
              sa('Why construct only two angle bisectors to find the incenter?', 'Answer:', key='The third bisector passes through the same point.', note='Any equivalent answer.'),
              tf('Bisecting the sides locates the incenter.', key=False, note='That locates the circumcenter.'),
          ], align='exact',
            why=why('the student cannot bisect the angles.', 'the incenter is found with two angle bisectors.', 'bisects angles.')),
          B('Construct a perpendicular from a point to a line', 'HSG-CO.D.12', [
              sa('Which construction finds the point where the incircle touches a side?', 'Answer:', key='The perpendicular from the incenter to the side', note='Any equivalent answer.'),
              tf('The perpendicular from a point to a line is the shortest segment to the line.', key=True, note='Distance.'),
              mc('From point I, an arc meets side AB at two points. Next step?', ['Arcs of equal radius from those two points, crossing on the other side', 'Measure AB', 'Bisect ∠I', 'Draw a circle at A'],
                 note='Then draw the line through I and that crossing.'),
              sa('Why not measure from I to a vertex for the radius?', 'Answer:', key='Vertices are farther than the sides; the circle must touch the sides, not pass through vertices.', note='Any equivalent answer.'),
              tf('The incircle passes through the vertices.', key=False, note='It touches the sides.'),
          ], align='exact',
            why=why('the student uses the wrong radius.', 'the radius is the perpendicular distance to a side.', 'constructs perpendiculars.')),
          B('Points on an angle bisector are equidistant from the sides', 'HSG-SRT.B.5', [
              tf('A point on the bisector of ∠A is equidistant from the two sides of ∠A.', key=True, note='Congruent right triangles (AAS).'),
              sa('The incenter is 3 cm from side AB. How far is it from side BC?', 'Distance:', key='3 cm', note='Any equivalent form.'),
              mc('Distance from a point to a side is measured', ['along the perpendicular', 'along any segment', 'to the nearest vertex', 'along the bisector'], note='Shortest.'),
              sa('Why is the incenter the same distance from all three sides?', 'Answer:', key='It is on all three angle bisectors, and each bisector point is equidistant from that angle\'s sides.', note='Any equivalent answer.'),
              tf('The incenter is equidistant from the three vertices.', key=False, note='That is the circumcenter.'),
          ], align='supporting',
            why=why('the student does not see why the incenter works.', 'equal distances to the sides make one circle touch all three.', 'uses the bisector distance property.')),
      ],
      f1=B('Prove that the incenter is equidistant from the sides', 'HSG-C.A.3', [
          proof('The bisectors of ∠A and ∠B of △ABC meet at I. Prove that I is equidistant from all three sides and lies on the bisector of ∠C.',
                method='Use the angle bisector distance property twice, then its converse at C.', key='I is equidistant from AB, BC, CA and lies on the bisector of ∠C.',
                note=PR + 'Essential: on the bisector of ∠A: d(I, AB) = d(I, AC); on the bisector of ∠B: d(I, AB) = d(I, BC); so d(I, AC) = d(I, BC); the converse puts I on the bisector of ∠C.'),
          sa('A triangle has area 30 and perimeter 30. Find the radius of its inscribed circle.', 'Radius:', key='2', note='Any equivalent form. Area = r · (perimeter ÷ 2).'),
          tf('The incenter is always inside the triangle.', key=True, note='Angle bisectors stay inside.'),
          mc('A 3-4-5 right triangle has inradius', ['1', '2', '1.5', '2.5'], note='Area 6 = r · 6.'),
          sa('Explain why area = r · s, where s is half the perimeter.', 'Answer:', key='Joining I to the vertices splits the triangle into three triangles with heights r on bases a, b, c: area = ½r(a + b + c) = r · s.',
             note='Any equivalent explanation.'),
      ], prog='same-course deepening', demand='Prove why the construction works and derive the inradius formula.'),
      f2=B('Locate a point equidistant from three lines in a design', 'HSG-MG.A.3', [
          sa('A circular fountain must touch three straight paths that form a triangle with sides 13, 14, and 15 m (area 84 m²). What is the largest possible radius?', 'Radius:', key='4 m',
             note='Any equivalent form. s = 21, r = 84/21.'),
          sa('Explain why the incircle gives the largest circle that fits inside a triangle.', 'Answer:', key='A larger circle would cross some side; the incircle touches all three sides.', note='Any reasonable explanation.'),
          tf('A sprinkler equidistant from three fences (triangle) should be at the incenter.', key=True, note='Equidistant from the sides.'),
          mc('To be equidistant from three towns (points), use the', ['circumcenter', 'incenter', 'centroid', 'orthocenter'], note='Points, not lines.'),
          sa('An equilateral triangle has side 6. Find its inradius exactly.', 'Radius:', key='√3', note='Form required: exact. Area 9√3, s = 9.'),
      ], prog='cross-standard extension', demand='Use the incircle to solve a design problem with a constraint (largest circle touching three lines).',
        builds='Builds on FORWARD 1: the inradius formula finds the largest feasible circle in a design.')),

    # ------------------------------------------------------------------ 60. C.A.3 circumcircle
    S('HSG-C.A.3', 'Construct the circumscribed circle of a triangle',
      target='Construct the circumscribed circle (circumcircle) of a given triangle with compass and straightedge', strand='core', covers=['C3-circumcircle'],
      main=[
          plot(TOOLS + '\nConstruct the circumscribed circle of triangle ABC.', tri_fig(T1, 'Acute triangle ABC.'),
               key='Construct the perpendicular bisectors of two sides; they meet at O; draw the circle with center O through A (it also passes through B and C).',
               note=EV + 'two perpendicular bisector constructions and the circle through all three vertices.'),
          plot(TOOLS + '\nConstruct the circumscribed circle of obtuse triangle ABC.', tri_fig(T2, 'Obtuse triangle ABC with the obtuse angle at C.'),
               key='Same steps; the circumcenter is outside the triangle.', note=EV + 'all constructions and the circle.'),
          plot(TOOLS + '\nConstruct the circumscribed circle of right triangle ABC.', tri_fig(T3, 'Right triangle ABC with the right angle at A.'),
               key='The perpendicular bisectors meet at the midpoint of hypotenuse BC; circle centered there through A.', note=EV + 'constructions and the circle; the center is on BC.'),
          sa('Write the steps for constructing the circumscribed circle of a triangle.', 'Steps:',
             key='1. Construct the perpendicular bisectors of two sides. 2. Label their intersection O. 3. Draw the circle with center O through one vertex.', note='Any equivalent steps.'),
          tf('The circumcenter of an obtuse triangle lies inside the triangle.', key=False, note='It lies outside.'),
      ],
      back=[
          B('Construct the perpendicular bisector of a segment', 'HSG-CO.D.12', [
              sa('Which construction gives all points equidistant from A and B?', 'Answer:', key='The perpendicular bisector of AB', note='Any equivalent answer.'),
              tf('The perpendicular bisector construction uses equal arcs from both endpoints.', key=True, note='Same radius.'),
              mc('The circumcenter is where the', ['perpendicular bisectors of the sides meet', 'angle bisectors meet', 'medians meet', 'sides meet'], note='Equidistant from vertices.'),
              sa('After constructing two perpendicular bisectors, why is the third unnecessary?', 'Answer:', key='It passes through the same point.', note='Any equivalent answer.'),
              tf('The arcs in a perpendicular bisector construction can have any two different radii.', key=False, note='Equal radii.'),
          ], align='exact',
            why=why('the student cannot construct the bisectors.', 'they locate the center.', 'constructs perpendicular bisectors.')),
          B('Points on the perpendicular bisector are equidistant from the endpoints', 'HSG-CO.C.9', [
              tf('Every point on the perpendicular bisector of AB is equidistant from A and B.', key=True, note='Theorem.'),
              sa('O is on the perpendicular bisectors of AB and BC. Compare OA, OB, OC.', 'Answer:', key='OA = OB = OC', note='Any equivalent form.'),
              mc('The circumcircle\'s radius is', ['the distance from O to any vertex', 'the distance from O to a side', 'half a side', 'the longest side'], note='Through the vertices.'),
              sa('A circle passes through A, B, C. Where must its center lie relative to AB?', 'Answer:', key='On the perpendicular bisector of AB', note='Any equivalent answer.'),
              tf('The circumcenter is equidistant from the sides.', key=False, note='From the vertices.'),
          ], align='exact',
            why=why('the student does not know why the bisectors locate the center.', 'equidistance from vertices is needed.', 'uses the theorem.')),
          B('Triangle types: acute, right, obtuse', '4.G.A.2', [
              sa('A triangle has angles 30°, 45°, 105°. Classify it.', 'Answer:', key='Obtuse', note='Any equivalent answer.'),
              tf('A right triangle has one 90° angle.', key=True, note='Definition.'),
              mc('Where is the circumcenter of a right triangle?', ['On the hypotenuse (its midpoint)', 'Inside', 'Outside', 'At the right angle'], note='Hypotenuse is a diameter.'),
              sa('A triangle has angles 50°, 60°, 70°. Classify it.', 'Answer:', key='Acute', note='Any equivalent answer.'),
              tf('An acute triangle can have an obtuse angle.', key=False, note='All angles are acute.'),
          ], align='supporting',
            why=why('the student is surprised when the center is outside.', 'the type of triangle decides where the center is.', 'classifies triangles.')),
      ],
      f1=B('Find the circumcenter and radius with coordinates', 'HSG-GPE.B.5', [
          sa('Triangle with A(0, 0), B(6, 0), C(2, 4). Find the circumcenter and radius.', 'Answer:', key='(3, 1); radius √10', note='Form required: both. Bisector of AB: x = 3; of AC: y - 2 = -½(x - 1).'),
          sa('Triangle with A(-2, 0), B(2, 0), C(0, 2). Find the circumcenter.', 'Center:', key='(0, 0)', note='Form required: an ordered pair. All three are 2 from the origin.'),
          tf('The circumcenter is the intersection of two perpendicular bisector equations.', key=True, note='Solve the system.'),
          mc('A right triangle has vertices (0, 0), (8, 0), (0, 6). Circumradius?', ['5', '10', '4', '6'], note='Half the hypotenuse.'),
          sa('Explain how to check a computed circumcenter.', 'Answer:', key='Verify it is the same distance from all three vertices.', note='Any equivalent answer.'),
      ], prog='cross-standard extension', demand='Locate the circumcenter algebraically with perpendicular bisector equations.'),
      f2=B('Find the circumradius with trigonometry (extended Law of Sines)', 'HSG-SRT.D.10', [
          sa('In a triangle, a = 10 and A = 30°. Find the circumradius R using a/sin A = 2R.', 'R =', key='10', note='Any equivalent form. 10 / 0.5 = 20 = 2R.'),
          sa('Equilateral triangle with side 6. Find the circumradius exactly.', 'R =', key='2√3', note='Form required: exact. 6/sin 60° = 4√3 = 2R.'),
          tf('In any triangle, a/sin A equals the diameter of the circumcircle.', key=True, note='Extended Law of Sines.'),
          mc('A triangle with a 90° angle opposite side 14 has circumradius', ['7', '14', '28', '3.5'], note='14/sin 90° = 14 = 2R.'),
          sa('Explain why a/sin A = 2R using an inscribed angle on a diameter.', 'Answer:',
             key='Draw the diameter from B; the inscribed angle at its far end equals A (same arc) and is in a right triangle with hypotenuse 2R, so sin A = a/(2R).', note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Connect the circumcircle with trigonometry (the extended Law of Sines, advanced strand).',
        builds='A second extension of MAIN: FORWARD 1 computes the center; FORWARD 2 computes the radius from an angle.')),

    # ------------------------------------------------------------------ 61. C.A.3 inscribed quadrilaterals
    S('HSG-C.A.3', 'Prove that opposite angles of an inscribed quadrilateral are supplementary',
      target='Prove that the opposite angles of a quadrilateral inscribed in a circle are supplementary, and use the property', strand='core', covers=['C3-cyclic'],
      main=[
          proof('Quadrilateral ABCD is inscribed in circle O. Prove that m∠A + m∠C = 180°.', fig=CYC,
                method='Use the inscribed angle theorem: ∠A and ∠C intercept the two arcs BCD and BAD, which together make the whole circle.', key='m∠A + m∠C = 180°',
                note=PR + 'Essential: m∠A = ½ arc BCD and m∠C = ½ arc BAD (inscribed angle theorem); the two arcs add to 360°; so the angles add to 180°.'),
          proof('Quadrilateral PQRS is inscribed in a circle. Prove that ∠Q and ∠S are supplementary.', method='Use the inscribed angle theorem: ∠Q and ∠S intercept arcs PSR and PQR, which together make the whole circle.',
                key='m∠Q + m∠S = 180°', note=PR + 'Essential: each angle is half its intercepted arc, and the two intercepted arcs make up the whole circle (360°).'),
          sa('Quadrilateral ABCD is inscribed in a circle with m∠A = 72° and m∠B = 105°. Find m∠C and m∠D.', 'Answer:', key='m∠C = 108°, m∠D = 75°', note='Form required: both.'),
          mc('Which quadrilateral can always be inscribed in a circle?', ['Any rectangle', 'Any rhombus', 'Any parallelogram', 'Any trapezoid'], note='Opposite angles 90° + 90°.'),
          tf('A parallelogram that is not a rectangle can be inscribed in a circle.', key=False, note='Its opposite angles are equal but not 90°, so they are not supplementary.'),
      ],
      back=[
          B('The inscribed angle theorem', 'HSG-C.A.2', [
              sa('An inscribed angle intercepts a 220° arc. Its measure?', 'Measure:', key='110°', note='Any equivalent form.'),
              tf('An inscribed angle can intercept an arc greater than 180°.', key=True, note='Then the angle is obtuse.'),
              mc('An inscribed angle of 70° intercepts', ['140°', '35°', '70°', '290°'], note='Double.'),
              sa('Two arcs together make a whole circle. Their sum?', 'Sum:', key='360°', note='Any equivalent form.'),
              tf('An inscribed angle equals half the central angle only when it is acute.', key=False, note='Always.'),
          ], align='exact',
            why=why('the student cannot relate the angles to arcs.', 'the proof uses the inscribed angle theorem twice.', 'applies the theorem.')),
          B('Supplementary angles', '7.G.B.5', [
              sa('Supplement of 72°?', 'Answer:', key='108°', note='Any equivalent form.'),
              tf('Two angles whose measures add to 180° are supplementary.', key=True, note='Definition.'),
              mc('Angles 3x and 2x are supplementary. x =', ['36°', '30°', '45°', '60°'], note='5x = 180.'),
              sa('If ∠A = ∠C and they are supplementary, find each.', 'Answer:', key='90°', note='Any equivalent form.'),
              tf('Supplementary angles are equal.', key=False, note='Only if both are 90°.'),
          ], align='exact',
            why=why('the student does not know supplementary.', 'the theorem states supplementary angles.', 'finds supplements.')),
          B('Arcs of a circle add to 360°', '4.MD.C.7', [
              sa('A circle is split into arcs of 100°, 80°, and x°. Find x.', 'x =', key='180', note='Any equivalent form.'),
              tf('The arcs between four points on a circle add to 360°.', key=True, note='Whole circle.'),
              mc('Two arcs make a whole circle; one is 150°. The other is', ['210°', '150°', '30°', '360°'], note='360 - 150.'),
              sa('Half of 360° is', 'Answer:', key='180°', note='Any equivalent form.'),
              tf('The arcs of a circle add to 180°.', key=False, note='360°.'),
          ], align='supporting',
            why=why('the student does not see the two arcs fill the circle.', 'that gives the 180° sum.', 'adds arcs.')),
      ],
      f1=B('Use the converse: decide whether a quadrilateral can be inscribed', 'HSG-C.A.3', [
          sa('Quadrilateral ABCD has angles A = 85°, B = 70°, C = 95°, D = 110°. Can it be inscribed in a circle? Explain.', 'Answer:', key='Yes: A + C = 180° and B + D = 180°.',
             note='Form required: the conclusion with the check. (The converse is true: such a quadrilateral is cyclic.)'),
          sa('An isosceles trapezoid has base angles of 64°. Can it be inscribed in a circle? Explain.', 'Answer:', key='Yes: its other angles are 116°, and 64° + 116° = 180° for each pair of opposite angles.',
             note='Any equivalent answer.'),
          tf('Every kite can be inscribed in a circle.', key=False, note='Only kites with two right angles.'),
          mc('Inscribed quadrilateral with angles (2x)°, (3x + 5)°, (2x + 20)°, and y°. If 2x and 2x + 20 are opposite, x =', ['40', '35', '45', '50'], note='4x + 20 = 180.'),
          sa('Inscribed quadrilateral: ∠A = (5y - 10)°, ∠C = (3y + 30)°, A and C opposite. Find y and ∠A.', 'Answer:', key='y = 20; ∠A = 90°', note='Form required: both. 8y + 20 = 180.'),
      ], prog='same-course deepening', demand='Use the property and its converse to decide whether a quadrilateral is cyclic and to solve for unknowns.'),
      f2=B('Exterior angle of a cyclic quadrilateral', 'HSG-C.A.3', [
          proof('ABCD is inscribed in a circle and side DC is extended past C to E. Prove that m∠BCE = m∠A.', method='Use the linear pair at C and the supplementary opposite angles.',
                key='m∠BCE = m∠A', note=PR + 'Essential: m∠BCE = 180° - m∠BCD (linear pair); m∠A = 180° - m∠BCD (opposite angles); so equal.'),
          sa('In inscribed ABCD, ∠A = 77°. Side DC is extended past C to E. Find ∠BCE.', '∠BCE =', key='77°', note='Any equivalent form.'),
          tf('An exterior angle of a cyclic quadrilateral equals the interior angle opposite to it.', key=True, note='Proved above.'),
          mc('Inscribed ABCD with ∠B = 100°. The exterior angle at D (extending CD past D) is', ['100°', '80°', '50°', '180°'], note='Equals the opposite interior angle.'),
          sa('Why is the exterior angle at C equal to ∠A, not ∠B?', 'Answer:', key='It is supplementary to ∠C, and the angle supplementary to ∠C is its opposite angle, ∠A.', note='Any equivalent answer.'),
      ], prog='same-course deepening', demand='Derive and use a further consequence (exterior angle equals the opposite interior angle).',
        builds='Builds on FORWARD 1: supplementary opposite angles combined with linear pairs.')),

    # ------------------------------------------------------------------ 62. C.B.5 arc length and radians
    S('HSG-C.B.5', 'Derive arc length from similarity and define radian measure',
      target='Use similarity to show that the arc cut off by an angle is proportional to the radius, define radian measure as the constant of proportionality, and use s = rθ',
      strand='core', covers=['C5-arc'],
      main=[
          proof('A central angle θ cuts off arc length s₁ on a circle of radius r₁ and arc length s₂ on a circle of radius r₂ (same center). Explain, using similarity, why s₁/r₁ = s₂/r₂.',
                method='Use the dilation about the center with factor r₂/r₁: it maps the first circle to the second and the first arc to the second arc.', key='s₂ = (r₂/r₁)s₁, so s₁/r₁ = s₂/r₂.',
                note=PR + 'Essential: the dilation about the center with factor k = r₂/r₁ maps the first circle onto the second and the arc of angle θ onto the arc of angle θ; it multiplies all lengths, '
                     'including arc length, by k; so s₂ = k s₁ and s/r is the same for both. This constant is θ in radians.'),
          sa('A central angle cuts off an arc of length 12 cm on a circle of radius 4 cm. What is the angle in radians?', 'Angle:', key='3 radians', note='Any equivalent form. θ = s/r.'),
          sa('Find the length of the arc cut off by a central angle of 2.5 radians in a circle of radius 6 m.', 'Length:', key='15 m', note='Any equivalent form. s = rθ.'),
          sa('Find the exact length of the arc cut off by a 120° central angle in a circle of radius 9.', 'Length:', key='6π', note='Form required: exact value. 120° = 2π/3 radians; s = 9 · 2π/3.'),
          mc('Why is a full circle 2π radians?', ['The circumference is 2πr, so s/r = 2π for the whole circle', 'There are 360 degrees', 'π ≈ 3.14', 'Every circle has radius 1'],
             note='Arc length ÷ radius for the whole circle.'),
      ],
      back=[
          B('Similar figures: lengths scale by the scale factor', 'HSG-SRT.A.2', [
              tf('Under a dilation with factor k, every length (straight or curved) is multiplied by k.', key=True, note='Similarity.'),
              sa('Two similar circles have radii 3 and 12. Scale factor?', 'Factor:', key='4', note='Any equivalent form.'),
              mc('An arc of length 5 on the small circle (radius 3) matches which arc length on the large one (radius 12)?', ['20', '15', '8', '60'], note='× 4.'),
              sa('Are all circles similar?', 'Answer:', key='Yes', note='Any equivalent answer.'),
              tf('Arc lengths do not change under dilation.', key=False, note='They scale.'),
          ], align='exact',
            why=why('the student does not apply similarity to arcs.', 'the derivation is a similarity argument.', 'scales arcs.')),
          B('Circumference of a circle', '7.G.B.4', [
              sa('Find the circumference of a circle with radius 5 (exact).', 'Circumference:', key='10π', note='Form required: exact value.'),
              tf('C = 2πr', key=True, note='Formula.'),
              mc('A circle has diameter 8. Its circumference is', ['8π', '16π', '4π', '64π'], note='πd.'),
              sa('A circle has circumference 18π. Radius?', 'Radius:', key='9', note='Any equivalent form.'),
              tf('C = πr²', key=False, note='That is area.'),
          ], align='exact',
            why=why('the student cannot find the whole circumference.', 'an arc is a fraction of it.', 'uses C = 2πr.')),
          B('Find a fraction of a whole', '7.RP.A.3', [
              sa('What fraction of a circle is a 90° arc?', 'Fraction:', key='¼', note='Any equivalent form.'),
              sa('Find ⅓ of 18π.', 'Answer:', key='6π', note='Any equivalent form.'),
              mc('An arc of 45° is what fraction of the circumference?', ['⅛', '¼', '1/45', '45/100'], note='45/360.'),
              tf('A 120° arc is ⅓ of the circle.', key=True, note='120/360.'),
              tf('A 60° arc is 1/60 of the circle.', key=False, note='1/6.'),
          ], align='supporting',
            why=why('the student cannot find the fraction of the circle.', 'arc length = fraction × circumference.', 'computes fractions of a circle.')),
      ],
      f1=B('Convert between degrees and radians', 'HSG-C.B.5', [
          sa('Convert 150° to radians (exact).', 'Radians:', key='5π/6', note='Form required: exact value. Multiply by π/180.'),
          sa('Convert 3π/4 radians to degrees.', 'Degrees:', key='135°', note='Any equivalent form.'),
          tf('1 radian is about 57.3°.', key=True, note='180/π.'),
          mc('Which equals π/3 radians?', ['60°', '30°', '120°', '180°'], note='180/3.'),
          sa('An arc in a circle of radius 10 has length 5π. Find the central angle in degrees.', 'Angle:', key='90°', note='Any equivalent form. θ = π/2.'),
      ], prog='same-course deepening', demand='Work fluently between degree and radian measure, using the definition s = rθ.'),
      f2=B('Radian measure for angles of rotation and the unit circle', 'HSF-TF.A.1', [
          sa('On the unit circle, an angle of 2 radians cuts off an arc of what length?', 'Length:', key='2', note='Any equivalent form. r = 1.'),
          sa('A wheel of radius 0.3 m turns through 10 radians. How far does a point on its rim travel?', 'Distance:', key='3 m', note='Any equivalent form.'),
          tf('An angle of 7 radians is more than one full turn.', key=True, note='2π ≈ 6.28.'),
          mc('A point on the unit circle travels an arc of length π. The angle is', ['π radians (180°)', '1 radian', '2π radians', 'π°'], note='θ = s/r.'),
          sa('Explain why the radian measure of an angle does not depend on the radius of the circle used.', 'Answer:', key='Arc length is proportional to radius, so s/r is the same for every circle.',
             note='Any equivalent answer.'),
      ], prog='later-course extension', demand='Use radians for angles of rotation, including angles beyond 2π (Algebra II).',
        builds='Builds on FORWARD 1: radian fluency extends to rotation angles on the unit circle.')),

    # ------------------------------------------------------------------ 63. C.B.5 sector area
    S('HSG-C.B.5', 'Derive and use the formula for the area of a sector',
      target='Derive the area of a sector as a fraction of the circle\'s area (in degrees and radians) and use it', strand='core', covers=['C5-sector'],
      main=[
          proof('Derive a formula for the area of a sector with central angle θ (in degrees) in a circle of radius r. Then rewrite it for θ in radians.',
                method='Use the fraction of the whole circle that the sector is, times the circle\'s area.', key='A = (θ/360)πr² for degrees; A = ½r²θ for radians.',
                note=PR + 'Essential: the sector is θ/360 of the circle (central angles split the area in proportion); area = (θ/360)πr²; with θ radians, the fraction is θ/(2π), so A = (θ/(2π))πr² = ½r²θ.'),
          sa('Find the exact area of a sector with a 60° central angle in a circle of radius 6.', 'Area:', key='6π', note='Form required: exact value. (60/360)π(36).'),
          sa('Find the area of a sector with central angle 1.2 radians in a circle of radius 5.', 'Area:', key='15', note='Any equivalent form. ½(25)(1.2).'),
          sa('A pizza with diameter 14 in. is cut into 8 equal slices. Find the area of one slice to the nearest tenth of a square inch.', 'Area:', key='%s in²' % d1(PI * 49 / 8),
             note='Rounding to 0.1 required. Radius 7 (not 14): (1/8)π(49).'),
          mc('A sector has area 12π in a circle of radius 6. What is its central angle?', ['120°', '60°', '12°', '240°'], note='12π/36π = ⅓ of 360.'),
      ],
      back=[
          B('Area of a circle', '7.G.B.4', [
              sa('Find the exact area of a circle with radius 6.', 'Area:', key='36π', note='Form required: exact value.'),
              sa('A circle has diameter 10. Exact area?', 'Area:', key='25π', note='Form required: exact value. Use the radius 5.'),
              tf('A = πr²', key=True, note='Formula.'),
              mc('A circle has area 49π. Radius?', ['7', '49', '24.5', '14'], note='r² = 49.'),
              tf('Doubling the radius doubles the area.', key=False, note='It multiplies the area by 4.'),
          ], align='exact',
            why=why('the student cannot find the whole-circle area (or uses the diameter).', 'a sector is a fraction of it.', 'uses A = πr² with the radius.')),
          B('The radius is half the diameter', '7.G.B.4', [
              sa('A circle has diameter 14 in. Radius?', 'Radius:', key='7 in.', note='Any equivalent form.'),
              tf('Using the diameter in A = πr² gives an area four times too large.', key=True, note='(2r)² = 4r².'),
              mc('A sector of a circle with diameter 20 uses r =', ['10', '20', '40', '5'], note='Half.'),
              sa('A circle\'s radius is 2.5 cm. Diameter?', 'Diameter:', key='5 cm', note='Any equivalent form.'),
              tf('The radius and diameter can be used interchangeably in area formulas.', key=False, note='They differ by a factor of 2.'),
          ], align='supporting',
            why=why('the student plugs in the diameter.', 'sector formulas need the radius.', 'converts diameter to radius.')),
          B('Fractions of a circle in degrees and radians', 'HSG-C.B.5', [
              sa('What fraction of a circle is a sector with central angle 45°?', 'Fraction:', key='⅛', note='Any equivalent form.'),
              sa('What fraction of a circle is a sector with central angle π/2 radians?', 'Fraction:', key='¼', note='Any equivalent form. (π/2)/(2π).'),
              mc('A full circle measures', ['360° or 2π radians', '180° or π radians', '360 radians', '2π°'], note='Both units.'),
              tf('A central angle of 1 radian is 1/(2π) of the circle.', key=True, note='Fraction of 2π.'),
              tf('A 90° sector is ⅓ of the circle.', key=False, note='¼.'),
          ], align='exact',
            why=why('the student cannot find what fraction of the circle a sector is.', 'the derivation multiplies the area by that fraction.', 'finds fractions in both units.')),
      ],
      f1=B('Solve inverse sector problems', 'HSG-C.B.5', [
          sa('A sector with a 40° angle has area 4π. Find the radius.', 'Radius:', key='6', note='Any equivalent form. (40/360)πr² = 4π.'),
          sa('A sector of a circle with radius 10 has area 30. Find the central angle in radians.', 'Angle:', key='0.6 radians', note='Any equivalent form. ½(100)θ = 30.'),
          tf('If the radius is tripled and the angle stays the same, the sector area is multiplied by 9.', key=True, note='r².'),
          mc('A sector has area 50 and arc length 10. Radius?', ['10', '5', '20', '2.5'], note='A = ½rs.'),
          sa('Show that the area of a sector is A = ½rs, where s is the arc length.', 'Answer:', key='A = ½r²θ and s = rθ, so A = ½r(rθ) = ½rs.', note='Any equivalent derivation.'),
      ], prog='same-course deepening', demand='Solve the inverse problem: find the radius or angle from a sector area.'),
      f2=B('Areas of segments and composite circular regions', 'HSG-MG.A.1', [
          sa('Find the exact area of the region between a 90° arc and its chord in a circle of radius 4 (a circular segment).', 'Area:', key='4π - 8',
             note='Form required: exact value. Sector 4π minus right triangle 8.'),
          sa('A sprinkler waters a 120° sector of radius 9 m. Find the watered area to the nearest square meter.', 'Area:', key='%d m²' % round(PI * 81 / 3), note='Rounding to the nearest whole number required.'),
          tf('The area of a circular segment equals the sector area minus the area of the triangle formed by the two radii and the chord.', key=True, note='Decomposition.'),
          mc('An annulus (ring) has inner radius 3 and outer radius 5. Its area is', ['16π', '4π', '25π', '8π'], note='25π - 9π.'),
          sa('A windshield wiper blade covers the part of its arm from 20 cm to 60 cm from the pivot and sweeps through 120°. Find the area it wipes to the nearest square centimeter.', 'Area:',
             key='%d cm²' % round((120 / 360) * PI * (3600 - 400)), note='Rounding to the nearest whole number required. ⅓π(60² - 20²).'),
      ], prog='cross-standard extension', demand='Model regions made of sectors, triangles, and rings, and compute their areas.',
        builds='Builds on FORWARD 1: sector areas combine with other figures in modeling problems.')),
]
