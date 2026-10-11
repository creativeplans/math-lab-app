from qb import S, B, sa, mc, tf, plot, draw_write, work, shape, poly, rect, prism
from common import grid, circle, angles, geo, DRAW, BLANK

HOUSE = shape([poly([(0, 0), (10, 0), (10, 6), (0, 6)], ['10 m', None, None, '6 m']), poly([(10, 0), (14, 3), (10, 6)])],
              segs=[dict(a=(10, 3), b=(14, 3), label='4 m', off=(-8, -12))], ra=[((10, 3), (14, 3), (10, 6))], desc='A 10 m by 6 m rectangle with a triangle attached to its 6 m side. The triangle has a height of 4 m.')
WEDGES = dict(k='wedges', n=12, h=330)
SEG_AB = geo(('segment', (0, 0), (6, 0)), ('point', (0, 0), 'A'), ('point', (6, 0), 'B'), h=230,
             desc='Segment AB, drawn across the middle of the space with room above and below it.')
ANGLE_P = geo(('ray', (0, 0), (6, 0)), ('ray', (0, 0), (4, 3.5)), ('point', (0, 0), 'P'), h=230,
              desc='An angle with vertex P: one ray points right and the other points up and to the right.')
COPY_AB = geo(('segment', (0, 2.5), (4, 2.5)), ('point', (0, 2.5), 'A'), ('point', (4, 2.5), 'B'),
              ('ray', (0, 0), (7, 0)), ('point', (0, 0), 'C'), h=230,
              desc='Segment AB at the top. Below it, a ray starts at point C and points right.')
# two parallel lines m and n cut by transversal t; angles 1-4 at line n, 5-8 at line m
# (1 above-left, 2 above-right, 3 below-left, 4 below-right, and the same order for 5-8)
PARALLEL = geo(('line', (0, 0), (8, 0)), ('line', (0, 3), (8, 3)), ('line', (2, -1), (6, 4)),
               ('text', (9.2, 0), 'n'), ('text', (9.2, 3), 'm'), ('text', (6.5, 4.3), 't'),
               ('text', (2.56, 0.5), '1'), ('text', (3.3, 0.24), '2'), ('text', (2.3, -0.24), '3'), ('text', (3.04, -0.5), '4'),
               ('text', (4.96, 3.5), '5'), ('text', (5.7, 3.24), '6'), ('text', (4.7, 2.76), '7'), ('text', (5.44, 2.5), '8'), h=260,
               desc='Parallel lines m (top) and n (bottom) are cut by transversal t, which slants up to the right. At line n the angles are numbered '
                    '1 (above, left of t), 2 (above, right of t), 3 (below, left of t), and 4 (below, right of t). At line m the angles are '
                    'numbered 5, 6, 7, and 8 in the same positions.')

EQ = ('Both parts are required: a valid equation and the correct solution. Any valid equation is accepted, but the solution must also be correct.')


def cross(theta, top=None, right=None, bottom=None, left=None, desc=None):
    """Two intersecting lines: the angle opening upward measures theta degrees."""
    rays = [90 - theta / 2, 90 + theta / 2, 270 - theta / 2, 270 + theta / 2]
    labels = [(d, t) for d, t in ((90, top), (0, right), (270, bottom), (180, left)) if t]
    return angles(rays, labels, desc=desc)


XLINES = angles([54, 126, 234, 306], [(90, '72°'), (270, '?')], desc='Two lines intersect. One angle measures 72°. The angle opposite it is marked with a question mark.')

def solid(pts, d, labels, dlabel, seams=(), desc=None, h=250):
    f = dict(k='extrude', pts=pts, d=d, labels=labels, dlabel=dlabel, seams=list(seams), h=h)
    if desc:
        f['desc'] = desc
    return f


L_SOLID = solid([(0, 0), (8, 0), (8, 3), (3, 3), (3, 6), (0, 6)], 4, ['8 cm', '3 cm', '5 cm', None, None, '6 cm'], '4 cm',
                seams=[((3, 0), (3, 3))],
                desc='An L-shaped solid made of two right rectangular prisms, 4 cm deep. Its front face is 8 cm along the bottom and 6 cm tall on the left; '
                     'the lower right part is 3 cm tall and its top edge is 5 cm long. A dashed line shows where the two prisms meet.')
STEP_SOLID = solid([(0, 0), (6, 0), (6, 2), (3, 2), (3, 4), (0, 4)], 5, ['6 in', '2 in', '3 in', None, None, '4 in'], '5 in',
                   seams=[((3, 0), (3, 2))],
                   desc='A step-shaped solid made of two right rectangular prisms, 5 in deep. Its front face is 6 in along the bottom and 4 in tall on the left; '
                        'the lower step on the right is 2 in tall and its top edge is 3 in long.')
U_SOLID = solid([(0, 0), (9, 0), (9, 4), (6, 4), (6, 2), (3, 2), (3, 4), (0, 4)], 2,
                ['9 ft', None, '3 ft', '2 ft', None, None, '3 ft', '4 ft'], '2 ft', seams=[((3, 0), (3, 2)), ((6, 0), (6, 2))],
                desc='A U-shaped solid made of three right rectangular prisms, 2 ft deep. Its front face is 9 ft wide and 4 ft tall, '
                     'with a notch 3 ft wide and 2 ft deep cut from the middle of the top.')
TWO_CUBES = solid([(0, 0), (4, 0), (4, 2), (0, 2)], 2, ['4 cm', '2 cm', None, None], '2 cm', seams=[((2, 0), (2, 2))],
                  desc='Two cubes with 2 cm edges joined face to face, making a solid 4 cm long, 2 cm tall, and 2 cm deep. A dashed line shows where they meet.')


SETS = [
    # ------------------------------------------------------------------ 7.G.A.1 (compute)
    S('7.G.A.1', 'Find actual lengths and areas from a scale drawing',
      main=[
          sa('A scale drawing of a garden uses the scale 1 cm : 2 m. The garden is 6 cm long on the drawing.\nWhat is the actual length of the garden?', 'Length:',
             fig=rect(6, 3, '6 cm', '3 cm'), key='12 m'),
          sa('A floor plan uses the scale 1 inch : 4 feet. A room is 3 inches by 2.5 inches on the plan.\nWhat is the actual area of the room?', 'Area:', key='120 square feet'),
          mc('A map uses the scale 1 cm : 25 km. Two towns are 4.4 cm apart on the map.\nWhat is the actual distance between the towns?', ['110 km', '29.4 km', '100 km', '5.68 km']),
          tf('A drawing uses the scale 1 cm : 3 m. A 5 cm by 2 cm rectangle on the drawing has an actual area of 90 m².', key=True),
          tf('A drawing uses the scale 1 cm : 10 cm. The actual area is 10 times the area on the drawing.', key=False, note='The actual area is 100 times the area on the drawing.'),
      ],
      back=[
          B('Convert measurement units', '6.RP.A.3.d', [
              sa('How many inches are in 4.5 feet?', 'Inches:', key='54'),
              sa('How many meters are in 350 centimeters?', 'Meters:', key='3.5'),
              mc('How many yards are in 27 feet?', ['9', '81', '3', '24']),
              tf('2.5 kilometers = 2,500 meters', key=True),
              tf('6 feet = 60 inches', key=False, note='6 feet = 72 inches.'),
          ]),
          B('Find the area of a rectangle', '4.MD.A.3', [
              sa('A rectangle is 12 m long and 9 m wide.\nWhat is its area?', 'Area:', key='108 square meters'),
              sa('A rectangle has an area of 84 square feet. It is 12 feet long.\nHow wide is it?', 'Width:', key='7 feet'),
              mc('A rectangle is 15 cm long and 6 cm wide.\nWhat is its area?', ['90 square centimeters', '42 square centimeters', '21 square centimeters', '96 square centimeters']),
              tf('A square with 7-inch sides has an area of 49 square inches.', key=True),
              tf('A rectangle 10 m long and 4 m wide has an area of 28 square meters.', key=False, note='Its area is 40 square meters; 28 m is its perimeter.'),
          ]),
      ],
      f1=B('Describe similar figures with dilations', '8.G.A.4', [
          sa('A triangle has sides 3, 4, and 5 units. It is dilated by a scale factor of 2.5.\nWhat are the new side lengths?', 'Side lengths:', key='7.5, 10, and 12.5 units'),
          sa('A 4-by-6 rectangle is similar to a rectangle that is 10 by w. The 4 side matches the 10 side.\nFind w.', 'w =', key='15'),
          mc('A figure is dilated by a scale factor of {1/3}. One side is 18 cm long.\nHow long is the matching side of the image?', ['6 cm', '54 cm', '18{1/3} cm', '3 cm']),
          tf('Dilations keep angle measures the same.', key=True),
          tf('A 2-by-3 rectangle and a 4-by-5 rectangle are similar.', key=False),
      ]),
      f2=B('Decide whether two triangles are similar', 'HSG-SRT.A.2', [
          sa('Triangle ABC has angles of 40°, 60°, and 80°. Triangle DEF has angles of 40°, 60°, and 80°.\nAre the triangles similar? Explain.', 'Answer:',
             key='Yes. Their corresponding angles are equal.'),
          sa('One triangle has sides 6, 8, and 10. Another has sides 9, 12, and 15.\nWhat is the scale factor from the first triangle to the second?', 'Scale factor:', key='1.5', note='3/2 is also correct.'),
          mc('Which two triangles must be similar?',
             ['Two triangles that each have a 50° angle and a 70° angle', 'Two right triangles', 'Two triangles that each have a 5 cm side', 'Two isosceles triangles']),
          tf('Two triangles are similar with a scale factor of 3. Each pair of corresponding sides has a ratio of 3 : 1.', key=True),
          tf('All rectangles are similar.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.G.A.1 (redraw)
    S('7.G.A.1', 'Reproduce a scale drawing at a different scale',
      main=[
          plot('A scale drawing of a garden is a rectangle 6 units long and 4 units wide. Its scale is 1 unit : 2 m.\nRedraw the garden on the grid at a scale of 1 unit : 1 m.', DRAW,
               key='A rectangle 12 units by 8 units, in any position or orientation'),
          plot('A rectangle on a drawing is 4 units by 2 units.\nDraw the rectangle at a scale twice as large on the grid.', DRAW,
               key='A rectangle 8 units by 4 units, in any position or orientation'),
          plot('A floor plan shows a room as a rectangle 9 units by 6 units. Its scale is 1 unit : 2 feet.\nRedraw the room on the grid at a scale of 1 unit : 3 feet.', DRAW,
               key='A rectangle 6 units by 4 units, in any position or orientation'),
          plot('A scale drawing of a ramp is a right triangle whose two sides that form the right angle are 3 units and 4 units. Its scale is 1 unit : 5 m.\nRedraw it on the grid at a scale of 1 unit : 2.5 m.', DRAW,
               key='A right triangle whose two sides that form the right angle are 6 units and 8 units, in any position or orientation'),
          plot('A scale drawing of a patio is a rectangle 5 units by 3 units. Its scale is 1 unit : 6 m.\nRedraw the patio on the grid at a scale of 1 unit : 3 m.', DRAW,
               key='A rectangle 10 units by 6 units, in any position or orientation'),
      ],
      back=[
          B('Draw a polygon on the coordinate plane', '6.G.A.3', [
              draw_write('Draw the polygon with vertices (1, 1), (5, 1), (5, 4), and (1, 4).\nHow long is the side from (1, 1) to (5, 1)?', grid(6, 6), 'Length:',
                         draw='A rectangle with vertices (1, 1), (5, 1), (5, 4), and (1, 4)', key='4 units',
                         note='Grade both: the rectangle drawn with the four given vertices, and the length 4 units.'),
              sa('A rectangle has vertices (2, 1), (2, 6), (7, 6), and (7, 1).\nHow long is the side from (2, 1) to (7, 1)?', 'Length:', key='5 units'),
              mc('Which point makes a square with (1, 1), (4, 1), and (4, 4)?', ['(1, 4)', '(4, 7)', '(1, 3)', '(3, 1)']),
              tf('The points (0, 2) and (0, 7) are 5 units apart.', key=True),
              tf('The side from (3, 2) to (3, 8) is 5 units long.', key=False, note='It is 6 units long.'),
          ]),
          B('Compare the size of a product to the size of one factor', '5.NF.B.5.a', [
              sa('Without multiplying, is 3 × 12 greater than or less than 12?', 'Answer:', key='Greater than 12'),
              sa('Without multiplying, is {1/2} × 18 greater than or less than 18?', 'Answer:', key='Less than 18'),
              mc('Which product is greater than 15?', ['2 × 15', '{1/3} × 15', '{3/4} × 15', '{1/2} × 15']),
              tf('{2/3} × 9 is less than 9.', key=True),
              tf('4 × 8 is less than 8.', key=False),
          ]),
      ],
      f1=B('Describe the effect of a dilation on coordinates', '8.G.A.3', [
          sa('The point (4, -2) is dilated by a scale factor of 3 with the origin as the center.\nWhat are the coordinates of the image?', 'Coordinates:', key='(12, -6)'),
          sa('A triangle has vertices (2, 2), (6, 2), and (2, 4). It is dilated by a scale factor of {1/2} with the origin as the center.\nWhat are the vertices of the image?', 'Vertices:',
             key='(1, 1), (3, 1), and (1, 2)'),
          mc('A dilation centered at the origin maps (5, 10) to (2, 4).\nWhat is the scale factor?', ['{2/5}', '{5/2}', '3', '-3']),
          tf('A dilation by a scale factor of 2 with the origin as the center maps (-3, 1) to (-6, 2).', key=True),
          tf('A dilation by a scale factor of 4 with the origin as the center maps (2, 3) to (6, 7).', key=False, note='It maps (2, 3) to (8, 12).'),
      ]),
      f2=B('Verify the properties of dilations', 'HSG-SRT.A.1', [
          sa('A segment 5 cm long is dilated by a scale factor of 1.8.\nHow long is the image?', 'Length:', key='9 cm'),
          sa('A line passes through the center of a dilation.\nWhat is the image of the line?', 'Answer:', key='The same line (it maps to itself).'),
          mc('A line that does not pass through the center of a dilation is dilated.\nWhat is its image?', ['A parallel line', 'A perpendicular line', 'The same line', 'A curve']),
          tf('A dilation with a scale factor between 0 and 1 makes segments shorter.', key=True),
          tf('A dilation always changes the slope of a line that does not pass through its center.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.G.A.2 (draw)
    S('7.G.A.2', 'Draw triangles from given conditions',
      main=[
          plot('On the grid, draw a triangle with a right angle. The two sides that form the right angle should be 4 units and 6 units long.', DRAW,
               key='Any right triangle whose two sides that form the right angle are 4 units and 6 units long, in any position or orientation'),
          draw_write('Use a ruler and a protractor. Draw a triangle with a 5 cm side that has a 50° angle at one end and a 60° angle at the other end.\nMeasure the third angle.', BLANK, 'Third angle:',
                     draw='A triangle with a 5 cm side whose two end angles measure 50° and 60°, in any position or orientation', key='70°',
                     note='Grade both: the triangle drawn with the given side and angles (within ±2 mm and ±2°), and the third angle 70°.'),
          plot('On the grid, draw an obtuse triangle that has one side 5 units long along a grid line.', DRAW,
               key='Any triangle with one angle greater than 90° and one side 5 units long along a grid line, in any position or orientation'),
          plot('On the grid, draw an isosceles triangle that is not equilateral.', DRAW,
               key='Any triangle with exactly two sides of equal length (the third side has a different length)'),
          plot('On the grid, draw a triangle with two sides that are each 5 units long and meet at a right angle.', DRAW,
               key='A right triangle whose two sides that form the right angle are both 5 units long (an isosceles right triangle), in any position or orientation'),
      ],
      back=[
          B('Measure and draw angles with a protractor', '4.MD.C.6', [
              plot('Use a protractor to draw a 65° angle.', BLANK, key='An angle that measures 65° (within ±2°), in any orientation'),
              sa('One ray of an angle lines up with 0 on a protractor. The other ray passes through 120.\nWhat is the measure of the angle?', 'Measure:', key='120°'),
              mc('Which angle is greater than a right angle?', ['110°', '45°', '90°', '80°']),
              tf('A protractor measures angles in degrees.', key=True),
              tf('A 30° angle is an obtuse angle.', key=False),
          ]),
          B('Classify triangles by their angles', '4.G.A.2', [
              sa('A triangle has a 90° angle.\nClassify the triangle by its angles.', 'Answer:', key='Right triangle'),
              sa('A triangle has angles of 100°, 50°, and 30°.\nClassify the triangle by its angles.', 'Answer:', key='Obtuse triangle'),
              mc('What kind of triangle has three angles that are each less than 90°?', ['Acute triangle', 'Right triangle', 'Obtuse triangle', 'Straight triangle']),
              tf('An obtuse triangle has exactly one obtuse angle.', key=True),
              tf('A right triangle can have two right angles.', key=False),
          ]),
      ],
      f1=B('Use the Pythagorean theorem to find an unknown side length', '8.G.B.7', [
          sa('A right triangle has legs of 6 cm and 8 cm.\nHow long is the hypotenuse?', 'Hypotenuse:', key='10 cm'),
          sa('A right triangle has a hypotenuse of 13 m and one leg of 5 m.\nHow long is the other leg?', 'Leg:', key='12 m'),
          mc('A 10-foot ladder leans against a wall. The top of the ladder is 8 feet above the ground.\nHow far is the bottom of the ladder from the wall?', ['6 feet', '2 feet', '18 feet', '12.8 feet']),
          tf('A right triangle with legs of 9 and 12 has a hypotenuse of 15.', key=True),
          tf('A right triangle with legs of 1 and 1 has a hypotenuse of 2.', key=False, note='The hypotenuse is √2.'),
      ]),
      f2=B('Make formal constructions with a compass and straightedge', 'HSG-CO.D.12', [
          plot('Use a compass and a straightedge to construct the perpendicular bisector of segment AB. Leave your construction arcs showing.', SEG_AB,
               key='Two pairs of arcs with the same radius (more than half of AB), centered at A and at B, meeting above and below AB, and the line through the two meeting points. '
                   'It crosses AB at its midpoint at a right angle.'),
          plot('Use a compass and a straightedge to construct an equilateral triangle with side AB. Leave your construction arcs showing.', SEG_AB,
               key='Arcs with radius AB centered at A and at B that meet at a point C (above or below AB), with segments AC and BC drawn.'),
          plot('Use a compass and a straightedge to bisect the angle at P. Leave your construction arcs showing.', ANGLE_P,
               key='An arc centered at P crossing both rays, two arcs with the same radius centered at those crossing points that meet inside the angle, and the ray from P through that meeting point.'),
          plot('Use a compass and a straightedge to copy segment AB onto the ray, starting at point C. Leave your construction arc showing.', COPY_AB,
               key='An arc centered at C with radius AB (the compass set to the length AB) that crosses the ray at a point D, so CD = AB. D may be labeled.'),
          tf('In a compass-and-straightedge construction, a protractor is used to measure angles.', key=False,
             note='Only a compass and a straightedge (with no measuring marks) are used.'),
      ])),

    # ------------------------------------------------------------------ 7.G.A.2 (unique/many/none)
    S('7.G.A.2', 'Decide whether given conditions make one triangle, more than one triangle, or no triangle',
      main=[
          mc('Different triangles means triangles that are not congruent; position and orientation do not matter.\nHow many different triangles have sides of 3 cm, 4 cm, and 9 cm?', ['No triangle', 'Exactly one triangle', 'More than one triangle']),
          sa('Different triangles means triangles that are not congruent; position and orientation do not matter.\nA triangle has angles of 30°, 60°, and 90°. No side lengths are given.\nHow many different triangles fit these conditions? Explain.', 'Answer:',
             key='More than one. Triangles of different sizes can have the same three angles.'),
          sa('Different triangles means triangles that are not congruent; position and orientation do not matter.\nHow many different triangles have sides of 5 cm, 6 cm, and 7 cm?', 'Answer:', key='Exactly one triangle'),
          tf('Angles of 80° and 110° cannot both be angles of the same triangle.', key=True),
          tf('Three side lengths that form a triangle can make two triangles that are not congruent.', key=False),
      ],
      back=[
          B('Find an unknown angle when angles are joined', '4.MD.C.7', [
              sa('Angle ABC is split into two angles that measure 35° and 50°.\nWhat is the measure of angle ABC?', 'Measure:', key='85°'),
              sa('A 90° angle is split into two angles. One measures 28°.\nWhat does the other angle measure?', 'Measure:', key='62°'),
              mc('A 120° angle is split into two angles. One measures 45°.\nWhat does the other angle measure?', ['75°', '165°', '85°', '45°']),
              tf('A 45° angle and a 45° angle joined together make a 90° angle.', key=True),
              tf('A 120° angle and a 70° angle joined together make a 180° angle.', key=False, note='They make a 190° angle.'),
          ]),
          B('Find the perimeter of a polygon from its side lengths', '3.MD.D.8', [
              sa('A triangle has sides of 7 cm, 9 cm, and 12 cm.\nWhat is its perimeter?', 'Perimeter:', key='28 cm'),
              sa('A triangle has a perimeter of 30 inches. Two of its sides are 8 inches and 10 inches.\nHow long is the third side?', 'Length:', key='12 inches'),
              mc('A triangle has sides of 5 m, 5 m, and 6 m.\nWhat is its perimeter?', ['16 m', '150 m', '11 m', '21 m']),
              tf('A triangle with sides of 4 feet, 6 feet, and 7 feet has a perimeter of 17 feet.', key=True),
              tf('A triangle with three 9 cm sides has a perimeter of 18 cm.', key=False),
          ]),
      ],
      f1=B('Use the converse of the Pythagorean theorem to test for a right triangle', '8.G.B.6', [
          sa('Is a triangle with sides of 7, 24, and 25 a right triangle? Explain.', 'Answer:', key='Yes. 7² + 24² = 49 + 576 = 625 = 25².'),
          sa('Is a triangle with sides of 6, 7, and 9 a right triangle? Explain.', 'Answer:', key='No. 6² + 7² = 85, but 9² = 81.'),
          mc('Which side lengths form a right triangle?', ['8, 15, 17', '4, 5, 6', '2, 3, 4', '5, 6, 8']),
          tf('A triangle with sides of 9, 40, and 41 is a right triangle.', key=True),
          tf('A triangle with sides of 3, 3, and 4 is a right triangle.', key=False),
      ]),
      f2=B('Explain triangle congruence criteria with rigid motions', 'HSG-CO.B.8', [
          sa('Triangles ABC and DEF have AB = DE, BC = EF, and angle B = angle E. A rigid motion moves B onto E and ray BA onto ray ED.\nExplain why A lands on D and C lands on F.', 'Explanation:',
             key='A lands on D because AB = DE along the same ray. Because angle B = angle E, ray BC lands on ray EF (after a reflection if needed), and because BC = EF, C lands on F. So the triangles are congruent (SAS).'),
          sa('Triangles PQR and STU have PQ = ST, QR = TU, and PR = SU. A rigid motion moves P onto S and Q onto T, with R and U on the same side of ST.\nExplain why R must land on U.', 'Explanation:',
             key='R lands where a circle of radius PR around S meets a circle of radius QR around T on that side of ST. U is that same point (SU = PR and TU = QR), and there is only one such point, so R lands on U (SSS).'),
          mc('Triangles ABC and DEF have angle A = angle D, AB = DE, and angle B = angle E. A rigid motion puts A on D and B on E, with C and F on the same side.\nWhy must C land on F?',
             ['The rays from D and E at the equal angles cross at only one point, so C and F are the same point.', 'All triangles with a side of length AB are congruent.',
              'The third angles add to 180°.', 'A rigid motion stretches the sides until they match.']),
          tf('Rigid motions (translations, rotations, and reflections) keep side lengths and angle measures the same.', key=True),
          tf('Two triangles with all three pairs of angles equal can always be mapped onto each other by a rigid motion.', key=False,
             note='Equal angles make the triangles similar; they can be different sizes.'),
      ])),

    # ------------------------------------------------------------------ 7.G.A.3
    S('7.G.A.3', 'Describe the cross sections made by slicing right prisms and pyramids',
      main=[
          sa('A right rectangular prism is sliced by a plane parallel to its base.\nWhat is the shape of the cross section?', 'Shape:', fig=prism(5, 3, 4),
             key='A rectangle the same size as the base'),
          sa('A right square pyramid is sliced by a plane parallel to its base, strictly between the base and the top vertex.\nWhat is the shape of the cross section?', 'Shape:', key='A square smaller than the base'),
          mc('A cube is sliced by a plane that is parallel to one of its faces.\nWhat is the shape of the cross section?', ['A square', 'A triangle', 'A circle', 'A pentagon']),
          tf('A right square pyramid is sliced by a plane that passes through its top vertex and the center of its base, perpendicular to the base. The cross section is a triangle.', key=True),
          tf('A right rectangular prism sliced by a plane parallel to its base can have a triangle as its cross section.', key=False),
      ],
      back=[
          B('Identify the faces of solids from their nets', '6.G.A.4', [
              sa('How many faces does a rectangular prism have?', 'Faces:', key='6'),
              sa('A net has 1 square and 4 triangles.\nWhat solid does it fold into?', 'Solid:', key='A square pyramid'),
              mc('Which solid has a net of 2 triangles and 3 rectangles?', ['Triangular prism', 'Square pyramid', 'Cube', 'Rectangular prism']),
              tf('The net of a cube has 6 squares.', key=True),
              tf('A triangular pyramid has 5 faces.', key=False, note='It has 4 faces.'),
          ]),
          B('Name shapes by their number of sides and faces', '2.G.A.1', [
              sa('How many sides does a pentagon have?', 'Sides:', key='5'),
              sa('A shape has 6 sides and 6 angles.\nWhat is the name of the shape?', 'Name:', key='Hexagon'),
              mc('Which shape has 4 sides?', ['Quadrilateral', 'Triangle', 'Pentagon', 'Hexagon']),
              tf('A cube has 6 faces.', key=True),
              tf('A triangle has 4 angles.', key=False),
          ]),
      ],
      f1=B('Find the volumes of cylinders, cones, and spheres', '8.G.C.9', [
          sa('A cylinder has a radius of 2 cm and a height of 9 cm.\nFind its volume. Use 3.14 for π.', 'Volume:', key='113.04 cubic centimeters'),
          sa('A cone has a radius of 6 inches and a height of 5 inches.\nFind its volume in terms of π.', 'Volume:', key='60π cubic inches'),
          mc('A sphere has a radius of 3 m.\nWhat is its volume in terms of π?', ['36π cubic meters', '12π cubic meters', '27π cubic meters', '108π cubic meters']),
          tf('A cone and a cylinder have the same base and height. The cone\'s volume is {1/3} of the cylinder\'s volume.', key=True),
          tf('A cylinder with a radius of 2 and a height of 5 has a volume of 10π.', key=False, note='Its volume is 20π.'),
      ]),
      f2=B('Identify cross sections of three-dimensional objects', 'HSG-GMD.B.4', [
          sa('A right circular cylinder is sliced by a plane parallel to its base that cuts through its interior.\nWhat is the shape of the cross section?', 'Shape:', key='A circle'),
          sa('A right circular cone is sliced by a plane that contains its axis (the line through the apex and the center of the base).\nWhat is the shape of the cross section?', 'Shape:', key='A triangle (an isosceles triangle)'),
          mc('A sphere is sliced by a plane that passes through its interior.\nWhat is the shape of the cross section?', ['A circle', 'An oval that is not a circle', 'A square', 'A triangle']),
          tf('Spinning a rectangle around one of its sides makes a cylinder.', key=True),
          tf('A cube can never have a cross section shaped like a hexagon.', key=False, note='A slice through the midpoints of six edges makes a hexagon.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.4 (circumference)
    S('7.G.B.4', 'Find the circumference of a circle',
      main=[
          sa('Find the circumference of the circle. Use 3.14 for π.', 'Circumference:', fig=circle('d', '10 cm'), key='31.4 cm'),
          sa('Find the circumference of the circle. Use {22/7} for π.', 'Circumference:', fig=circle('r', '7 in'), key='44 in'),
          mc('A circular track has a circumference of 62.8 m.\nWhat is its diameter? Use 3.14 for π.', ['20 m', '10 m', '197.2 m', '31.4 m']),
          tf('A wheel has a radius of 15 inches. In one full turn it rolls about 94.2 inches. (Use 3.14 for π.)', key=True),
          tf('A circle with a radius of 4 m has a circumference of 4π m.', key=False, note='The circumference is 8π m.'),
      ],
      back=[
          B('Find the perimeter of a rectangle', '4.MD.A.3', [
              sa('A rectangle is 9 m long and 4 m wide.\nWhat is its perimeter?', 'Perimeter:', key='26 m'),
              sa('A square has 8 cm sides.\nWhat is its perimeter?', 'Perimeter:', key='32 cm'),
              mc('A rectangle is 12 feet long and 5 feet wide.\nWhat is its perimeter?', ['34 feet', '60 feet', '17 feet', '29 feet']),
              tf('A rectangle 6 inches long and 3 inches wide has a perimeter of 18 inches.', key=True),
              tf('A square with 10 m sides has a perimeter of 100 m.', key=False, note='The perimeter is 40 m.'),
          ]),
          B('Multiply decimals', '5.NBT.B.7', [
              sa('Multiply.\n3.14 × 6', 'Product:', key='18.84'),
              sa('Multiply.\n3.14 × 2.5', 'Product:', key='7.85'),
              mc('Multiply.\n3.14 × 12', ['37.68', '36.48', '376.8', '15.14']),
              tf('3.14 × 10 = 31.4', key=True),
              tf('3.14 × 4 = 12.16', key=False),
          ]),
      ],
      f1=B('Find the volume of a cylinder', '8.G.C.9', [
          sa('A cylinder has a radius of 5 feet and a height of 4 feet.\nFind its volume in terms of π.', 'Volume:', key='100π cubic feet'),
          sa('A cylinder has a diameter of 6 cm and a height of 10 cm.\nFind its volume. Use 3.14 for π.', 'Volume:', key='282.6 cubic centimeters'),
          mc('A cylinder has a volume of 90π cubic meters and a radius of 3 m.\nWhat is its height?', ['10 m', '30 m', '3 m', '15 m']),
          tf('Doubling the height of a cylinder doubles its volume.', key=True),
          tf('A cylinder with a radius of 1 and a height of 1 has a volume of 2π.', key=False, note='Its volume is π.'),
      ]),
      f2=B('Find the length of an arc of a circle', 'HSG-C.B.5', [
          sa('A circle has a radius of 6 cm.\nFind the length of an arc with a central angle of 90°, in terms of π.', 'Arc length:', key='3π cm'),
          sa('A circle has a circumference of 40 inches.\nHow long is an arc with a central angle of 45°?', 'Arc length:', key='5 inches'),
          mc('A circle has a radius of 10 m.\nWhat is the length of an arc with a central angle of 60°?', ['{10/3}π m', '{20/3}π m', '60π m', '{5/3}π m']),
          sa('Explain why an arc with a central angle of n° in a circle of radius r has a length of {n/360} × 2πr.', 'Explanation:',
             key='The arc is n/360 of the whole circle, so its length is n/360 of the circumference, which is 2πr.'),
          tf('In a circle with a radius of 3, an arc with a central angle of 120° has a length of 3π.', key=False, note='The arc length is 2π.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.4 (area)
    S('7.G.B.4', 'Find the area of a circle',
      main=[
          sa('Find the area of the circle. Use 3.14 for π.', 'Area:', fig=circle('r', '5 m'), key='78.5 square meters'),
          sa('Find the area of the circle in terms of π.', 'Area:', fig=circle('d', '12 in'), key='36π square inches'),
          mc('A circular rug has a radius of 3 feet.\nWhat is its area? Use 3.14 for π.', ['28.26 square feet', '18.84 square feet', '9.42 square feet', '113.04 square feet']),
          tf('A circle with a radius of 10 cm has an area of 100π square centimeters.', key=True),
          tf('A circle with a diameter of 8 m has an area of 64π square meters.', key=False, note='The radius is 4 m, so the area is 16π square meters.'),
      ],
      back=[
          B('Evaluate powers with whole-number exponents', '6.EE.A.1', [
              sa('Find the value.\n7²', 'Value:', key='49'),
              sa('Find the value.\n1.5²', 'Value:', key='2.25'),
              mc('Find the value.\n4³', ['64', '12', '16', '7']),
              tf('9² = 81', key=True),
              tf('6² = 12', key=False),
          ]),
          B('Evaluate a formula', '6.EE.A.2.c', [
              sa('Use A = s².\nFind A when s = 11.', 'A =', key='121'),
              sa('Use A = 3.14r².\nFind A when r = 2.', 'A =', key='12.56'),
              mc('Use A = {1/2}bh.\nFind A when b = 8 and h = 5.', ['20', '40', '13', '80']),
              tf('Use V = s³. When s = 2, V = 8.', key=True),
              tf('Use A = lw. When l = 3.5 and w = 2, A = 5.5.', key=False, note='A = 7.'),
          ]),
      ],
      f1=B('Find the volume of a cone', '8.G.C.9', [
          sa('A cone has a radius of 3 cm and a height of 8 cm.\nFind its volume in terms of π.', 'Volume:', key='24π cubic centimeters'),
          sa('A cone has a radius of 6 feet and a height of 7 feet.\nFind its volume. Use 3.14 for π.', 'Volume:', key='263.76 cubic feet'),
          mc('A cone has a base area of 30 square inches and a height of 9 inches.\nWhat is its volume?', ['90 cubic inches', '270 cubic inches', '30 cubic inches', '39 cubic inches']),
          tf('A cone with a radius of 3 and a height of 3 has a volume of 9π.', key=True),
          tf('The volume of a cone is πr²h.', key=False, note='The volume of a cone is (1/3)πr²h.'),
      ]),
      f2=B('Find the area of a sector of a circle', 'HSG-C.B.5', [
          sa('A circle has a radius of 4 m.\nFind the area of a sector with a central angle of 90°, in terms of π.', 'Area:', key='4π square meters'),
          sa('A pizza with a radius of 8 inches is cut into 8 equal slices.\nWhat is the area of one slice, in terms of π?', 'Area:', key='8π square inches'),
          mc('A circle has a radius of 6 cm.\nWhat is the area of a sector with a central angle of 120°?', ['12π square centimeters', '36π square centimeters', '4π square centimeters', '24π square centimeters']),
          sa('Explain why a sector with a central angle of n° in a circle of radius r has an area of {n/360} × πr².', 'Explanation:',
             key='The sector is n/360 of the whole circle, so its area is n/360 of the circle\'s area, which is πr².'),
          tf('In a circle with a radius of 6, a sector with a central angle of 60° has an area of 12π.', key=False, note='The area is 6π.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.4 (relationship)
    S('7.G.B.4', 'Explain the relationship between the circumference and the area of a circle',
      main=[
          sa('The circle with radius r is cut into equal wedges and rearranged into a shape close to a parallelogram. Its base is half the circumference.\nWrite the base in terms of r.', 'Base:',
             fig=WEDGES, key='πr', note='Half of 2πr.'),
          work('The circle with radius r is cut into equal wedges and rearranged as shown.\nExplain how this shows that the area of a circle is πr².', 'Area:', fig=WEDGES,
               method='A complete argument: the rearranged shape is close to a parallelogram (a rectangle with more wedges); its base is half the circumference, '
                      '{1/2} × 2πr = πr; its height is the radius r; so its area is πr × r = πr², and the circle has the same area because it is made of the same wedges. '
                      'Any equivalent wording is accepted.',
               key='πr²'),
          mc('A circle rearranged into a near-parallelogram has a base of πr and a height of r.\nWhat is the area?', ['πr²', '2πr', 'πr', '2πr²']),
          tf('A circle has circumference C and radius r. Its area equals {1/2} × C × r.', key=True),
          tf('A circle with a circumference of 10π has an area of 10π.', key=False, note='Its radius is 5, so its area is 25π.'),
      ],
      back=[
          B('Find the area of a parallelogram', '6.G.A.1', [
              sa('A parallelogram has a base of 9 cm and a height of 4 cm.\nWhat is its area?', 'Area:', key='36 square centimeters'),
              sa('A parallelogram has a base of 12 m and a height of 6.5 m.\nWhat is its area?', 'Area:', key='78 square meters'),
              mc('A parallelogram is cut along a segment from one top corner straight down to the base, at a right angle to the base. The triangle that is cut off is slid to the other end, so its slanted side lines up with the other slanted side.\nWhat shape is made?',
                 ['A rectangle', 'A circle', 'A trapezoid that is not a rectangle', 'A pentagon']),
              tf('A parallelogram and a rectangle with the same base and the same height have the same area.', key=True),
              tf('A parallelogram has a base of 10 and slanted sides of 6. Its area is 60.', key=False, note='The area uses the height, not the slanted side, so it is less than 60.'),
          ]),
          B('Identify equivalent expressions', '6.EE.A.4', [
              sa('Is {1/2} × 2 × r equivalent to r? Explain.', 'Answer:', key='Yes. 1/2 × 2 = 1, and 1 × r = r.'),
              mc('Which expression is equivalent to 3 × r × r?', ['3r²', '(3r)²', '6r', '3 + r²']),
              sa('Write an expression equivalent to x · x · x using an exponent.', 'Expression:', key='x³'),
              tf('2(4y) and 8y are equivalent.', key=True),
              tf('a² and 2a are equivalent.', key=False),
          ]),
      ],
      f1=B('Use square roots to solve equations of the form x² = p', '8.EE.A.2', [
          sa('Solve for x. Give all solutions.\nx² = 64', 'x =', key='x = 8 and x = -8', note='Both solutions are required; x = ±8 and set notation are accepted.'),
          sa('A circle has an area of 49π square centimeters.\nWhat is its radius?', 'Radius:', key='7 cm'),
          mc('Solve for x.\nx³ = 27', ['x = 3', 'x = 9', 'x = 6', 'x = 81']),
          tf('√144 = 12', key=True),
          tf('√50 is a whole number.', key=False),
      ]),
      f2=B('Give an informal argument for circle and volume formulas', 'HSG-GMD.A.1', [
          sa('Use the wedge argument to explain why the area of a circle is πr².', 'Explanation:',
             key='The wedges form a shape close to a parallelogram with base πr (half the circumference) and height r, so the area is πr × r = πr².'),
          sa('Two stacks of 20 identical coins have the same height. One stack is straight and one is slanted.\nDo they have the same volume? Explain.', 'Answer:',
             key='Yes. At every height the cross sections have the same area (Cavalieri\'s principle).'),
          mc('The circumference of a circle is C = πd.\nWhat is the ratio of C to d?', ['π', '2π', 'r', '2']),
          tf('As a circle is cut into more and more wedges, the rearranged shape gets closer to a parallelogram.', key=True),
          tf('Cavalieri\'s principle says that any two solids with the same height have the same volume.', key=False,
             note='The cross sections must also have equal areas at every height.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.5 (supplementary/complementary)
    S('7.G.B.5', 'Write and solve equations for supplementary and complementary angles',
      main=[
          sa('In the figure, angle ABC is a right angle. A ray splits it into angles of x° and (2x + 15)°.\nWrite and solve an equation for x.', 'Equation and answer:',
             fig=angles([0, 65, 90], [(24, '(2x + 15)°'), (78, 'x°')], desc='A right angle split by a ray into two angles labeled (2x + 15)° (the lower angle) and x° (the upper angle).'),
             key='The equation x + (2x + 15) = 90 and the answer x = 25', note=EQ),
          sa('In the figure, angles of (2x + 10)° and 70° form a straight line.\nWrite and solve an equation for x.', 'Equation and answer:',
             fig=angles([0, 70, 180], [(35, '70°'), (125, '(2x + 10)°')], desc='A straight line with a ray from a point on it. The angles on either side of the ray are labeled 70° and (2x + 10)°.'),
             key='The equation (2x + 10) + 70 = 180 and the answer x = 50', note=EQ),
          mc('Two complementary angles measure x° and (x + 20)°.\nWhat is the value of x?', ['35', '45', '80', '70']),
          tf('In the figure, three angles form a straight line. Then x = 30.',
             fig=angles([0, 30, 90, 180], [(15, '30°'), (60, '2x°'), (135, '3x°')], desc='Three angles side by side along a straight line, labeled 30°, 2x°, and 3x°.'),
             key=True, note='3x + 2x + 30 = 180, so x = 30.'),
          tf('In the figure, the two angles form a right angle. Then x = 18.',
             fig=angles([0, 57, 90], [(28, '(3x - 6)°'), (74, '(x + 12)°')], desc='A right angle split by a ray into angles labeled (3x - 6)° and (x + 12)°.'),
             key=False, note='(3x - 6) + (x + 12) = 90 gives x = 21.'),
      ],
      back=[
          B('Find an unknown part of a right angle or a straight angle', '4.MD.C.7', [
              sa('A straight angle (180°) is split into two angles. One measures 115°.\nWhat does the other angle measure?', 'Measure:', key='65°'),
              sa('A right angle is split into two angles. One measures 34°.\nWhat does the other angle measure?', 'Measure:', key='56°'),
              mc('A right angle is split into three angles. Two of them measure 20° and 30°.\nWhat does the third angle measure?', ['40°', '50°', '60°', '10°']),
              tf('Angles of 72° and 18° together make a right angle.', key=True),
              tf('Angles of 95° and 95° together make a straight angle.', key=False),
          ]),
          B('Solve one-step equations', '6.EE.B.7', [
              sa('Solve for x.\nx + 48 = 90', 'x =', key='42'),
              sa('Solve for x.\n3x = 180', 'x =', key='60'),
              mc('Solve for y.\n125 + y = 180', ['y = 55', 'y = 305', 'y = 65', 'y = 45']),
              tf('a = 27 is the solution of a + 63 = 90.', key=True),
              tf('b = 80 is the solution of 2b = 180.', key=False),
          ]),
      ],
      f1=B('Use the angle sum and exterior angles of triangles', '8.G.A.5', [
          sa('Two angles of a triangle measure 48° and 75°.\nWhat does the third angle measure?', 'Measure:', key='57°'),
          sa('An exterior angle of a triangle measures 130°. One of the two remote interior angles measures 60°.\nWhat does the other remote interior angle measure?', 'Measure:', key='70°'),
          mc('The angles of a triangle measure x°, 2x°, and 3x°.\nWhat is the value of x?', ['30', '60', '45', '36']),
          tf('The interior angles of a triangle add to 180°.', key=True),
          tf('An exterior angle of a triangle equals the sum of all three interior angles.', key=False),
      ]),
      f2=B('Prove angle relationships formed by parallel lines and a transversal', 'HSG-CO.C.9', [
          work('In the figure, lines m and n are parallel. Prove that angle 2 = angle 7. Give a reason for each step.', 'Conclusion:', fig=PARALLEL,
               method='A valid chain of reasons. Example: angle 2 = angle 6 (corresponding angles, because m and n are parallel); angle 6 = angle 7 (vertical angles); '
                      'so angle 2 = angle 7 (substitution). Other valid chains are accepted. The conclusion without reasons is not full credit.',
               key='Angle 2 = angle 7'),
          work('In the figure, lines m and n are parallel. Prove that angle 2 + angle 8 = 180°. Give a reason for each step.', 'Conclusion:', fig=PARALLEL,
               method='A valid chain of reasons. Example: angle 6 + angle 8 = 180° (they form a linear pair); angle 2 = angle 6 (corresponding angles); '
                      'so angle 2 + angle 8 = 180° (substitution). Other valid chains are accepted. The conclusion without reasons is not full credit.',
               key='Angle 2 + angle 8 = 180°'),
          mc('In the figure, lines m and n are parallel. A proof says:\nStep 1: angle 1 = angle 5 (corresponding angles)\nStep 2: angle 5 = angle 8 (?)\nStep 3: angle 1 = angle 8\nWhat is the reason for Step 2?',
             ['Vertical angles are congruent.', 'Corresponding angles are congruent.', 'Linear pairs are supplementary.', 'Alternate exterior angles are congruent.'], fig=PARALLEL),
          sa('In the figure, lines m and n are parallel and angle 2 = 52°.\nFind angle 8 and give a reason for each step.', 'Answer:', fig=PARALLEL,
             key='128°: angle 6 = angle 2 = 52° (corresponding angles), and angle 8 = 180° - 52° = 128° (angles 6 and 8 form a linear pair).',
             note='Both parts are required: 128° and a valid chain of reasons. A number without reasons is not full credit.'),
          tf('In the figure, lines m and n are parallel. "Angle 2 = angle 7 because they look the same size" is a valid proof.', fig=PARALLEL, key=False,
             note='A proof needs reasons, such as corresponding angles and vertical angles, not appearance.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.5 (vertical/adjacent)
    S('7.G.B.5', 'Use vertical and adjacent angles to find unknown angles',
      main=[
          sa('Two lines intersect. One angle measures 72°.\nWhat does the angle marked with a question mark measure?', 'Measure:', fig=XLINES, key='72°'),
          sa('Two lines intersect. The angles shown are vertical angles.\nWrite and solve an equation for x.', 'Equation and answer:',
             fig=cross(75, top='(3x + 15)°', bottom='75°', desc='Two lines intersect. The top angle is labeled (3x + 15)° and the bottom angle, vertical to it, is labeled 75°.'),
             key='The equation 3x + 15 = 75 and the answer x = 20', note=EQ),
          mc('Two lines intersect. The adjacent angles shown form a straight line.\nWhat is the value of x?', ['30', '25', '15', '45'],
             fig=cross(126, top='(4x + 6)°', right='(2x - 6)°', desc='Two lines intersect. The top angle is labeled (4x + 6)° and the angle to its right is labeled (2x - 6)°.')),
          tf('Two lines intersect. The angles shown are vertical angles. Each of them measures 75°.',
             fig=cross(75, top='3x°', bottom='(x + 50)°', desc='Two lines intersect. The top angle is labeled 3x° and the bottom angle is labeled (x + 50)°.'),
             key=True, note='3x = x + 50, so x = 25 and each angle is 75°.'),
          tf('Two lines intersect. The adjacent angles shown form a straight line. Then x = 25.',
             fig=cross(80, top='(5x - 20)°', right='(3x + 40)°', desc='Two lines intersect. The top angle is labeled (5x - 20)° and the angle to its right is labeled (3x + 40)°.'),
             key=False, note='(5x - 20) + (3x + 40) = 180 gives x = 20.'),
      ],
      back=[
          B('Identify lines, rays, segments, and angles', '4.G.A.1', [
              sa('How many endpoints does a ray have?', 'Endpoints:', key='1'),
              sa('What figure is formed by two rays that share an endpoint?', 'Figure:', key='An angle'),
              mc('Which figure goes on forever in both directions?', ['Line', 'Ray', 'Segment', 'Angle']),
              tf('Two lines that cross meet at exactly one point.', key=True),
              tf('A line segment has no endpoints.', key=False),
          ]),
          B('Understand angle measure as a fraction of a full turn', '4.MD.C.5.a', [
              sa('How many degrees are in one full turn?', 'Degrees:', key='360°'),
              sa('An angle turns through {1/4} of a circle.\nWhat is its measure?', 'Measure:', key='90°'),
              mc('An angle turns through {1/2} of a circle.\nWhat is its measure?', ['180°', '90°', '360°', '45°']),
              tf('An angle that turns through {1/360} of a circle measures 1°.', key=True),
              tf('An angle that turns through {1/3} of a circle measures 100°.', key=False, note='It measures 120°.'),
          ]),
      ],
      f1=B('Find angles formed by parallel lines cut by a transversal', '8.G.A.5', [
          sa('Two parallel lines are cut by a transversal. One angle measures 110°.\nWhat does the corresponding angle measure?', 'Measure:', key='110°'),
          sa('Two parallel lines are cut by a transversal. Alternate interior angles measure (4x - 10)° and 70°.\nFind x.', 'x =', key='20'),
          mc('Two parallel lines are cut by a transversal. One same-side interior angle measures 75°.\nWhat does the other measure?', ['105°', '75°', '15°', '285°']),
          tf('When parallel lines are cut by a transversal, alternate exterior angles are equal.', key=True),
          tf('When parallel lines are cut by a transversal, corresponding angles add to 180°.', key=False),
      ]),
      f2=B('Prove that vertical angles are congruent', 'HSG-CO.C.9', [
          sa('Angles 1 and 2 form a linear pair. Angles 2 and 3 form a linear pair.\nExplain why angle 1 and angle 3 have the same measure.', 'Explanation:',
             key='Each one equals 180° minus the measure of angle 2.'),
          work('Two lines intersect, forming angles 1, 2, 3, and 4 in order around the point. Prove that angle 2 = angle 4. Give a reason for each step.', 'Conclusion:',
               fig=cross(110, top='1', right='2', bottom='3', left='4', desc='Two lines intersect, forming angles numbered 1 (top), 2 (right), 3 (bottom), and 4 (left).'),
               method='A valid chain of reasons. Example: angle 1 + angle 2 = 180° and angle 1 + angle 4 = 180° (linear pairs); so angle 2 = 180° - angle 1 = angle 4 '
                      '(subtraction property of equality). Other valid chains are accepted. The conclusion without reasons is not full credit.',
               key='Angle 2 = angle 4'),
          mc('A proof that vertical angles are congruent says:\nStep 1: angle 1 + angle 2 = 180°\nStep 2: angle 2 + angle 3 = 180°\nStep 3: angle 1 + angle 2 = angle 2 + angle 3\nStep 4: angle 1 = angle 3\nWhat is the reason for Step 4?',
             ['Subtraction property of equality', 'Vertical angles are congruent', 'Corresponding angles are congruent', 'Definition of a right angle']),
          sa('Two lines intersect, and one of the four angles is 90°.\nProve that all four angles are 90°.', 'Proof:',
             key='Each angle next to the 90° angle forms a linear pair with it, so it measures 180° - 90° = 90°. The angle opposite the 90° angle is vertical to it, so it also measures 90°.',
             note='Full credit needs a reason for each angle (linear pairs and vertical angles).'),
          tf('"Angles 1 and 3 are vertical angles, and they look equal, so angle 1 = angle 3" is a valid proof.', key=False,
             note='A proof needs reasons such as linear pairs, not how the angles look.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.6 (area)
    S('7.G.B.6', 'Find the area of composite figures made of triangles and quadrilaterals',
      main=[
          sa('The figure is a 10 m by 6 m rectangle and a triangle with a base of 6 m (the rectangle\'s side) and a height of 4 m. The parts do not overlap.\nWhat is the total area?', 'Area:',
             fig=HOUSE, key='72 square meters'),
          sa('An L-shaped floor is made of two rectangles that do not overlap. One is 8 feet by 5 feet and the other is 4 feet by 3 feet.\nWhat is the area of the floor?', 'Area:', key='52 square feet'),
          mc('A figure is a 10 cm by 4 cm rectangle with a right triangle attached to one 4 cm side. The legs of the triangle are 4 cm and 3 cm, and the parts do not overlap.\nWhat is the total area?',
             ['46 square centimeters', '52 square centimeters', '40 square centimeters', '34 square centimeters']),
          tf('A 4 cm by 4 cm square is cut from one corner of a 12 cm by 8 cm rectangle. The area that is left is 80 square centimeters.', key=True),
          tf('A 9 m by 4 m rectangle and a right triangle with legs of 4 m and 3 m are joined without overlapping. Their total area is 48 square meters.', key=False,
             note='The total area is 36 + 6 = 42 square meters.'),
      ],
      back=[
          B('Find the area of a triangle', '6.G.A.1', [
              sa('A triangle has a base of 14 cm and a height of 5 cm.\nWhat is its area?', 'Area:', key='35 square centimeters'),
              sa('A right triangle has legs of 9 m and 6 m.\nWhat is its area?', 'Area:', key='27 square meters'),
              mc('A triangle has a base of 7 feet and a height of 10 feet.\nWhat is its area?', ['35 square feet', '70 square feet', '17 square feet', '140 square feet']),
              tf('A triangle with a base of 8 and a height of 3 has an area of 12.', key=True),
              tf('A triangle with a base of 6 and a height of 6 has an area of 36.', key=False, note='Its area is 18.'),
          ]),
          B('Find areas of rectilinear figures by breaking them into rectangles', '3.MD.C.7.d', [
              sa('A shape is made of a 5-by-3 rectangle and a 2-by-2 square that do not overlap.\nWhat is its area?', 'Area:', key='19 square units'),
              sa('A shape is made of a 6-by-2 rectangle and a 3-by-4 rectangle that do not overlap.\nWhat is its area?', 'Area:', key='24 square units'),
              mc('A shape is made of a 4-by-4 square and a 4-by-1 rectangle that do not overlap.\nWhat is its area?', ['20 square units', '16 square units', '13 square units', '25 square units']),
              tf('A 3-by-5 rectangle and a 2-by-5 rectangle that do not overlap have a total area of 25 square units.', key=True),
              tf('A 7-by-2 rectangle and a 1-by-3 rectangle that do not overlap have a total area of 13 square units.', key=False, note='The total area is 17 square units.'),
          ]),
      ],
      f1=B('Find the volume of a solid made of cylinders, cones, and spheres', '8.G.C.9', [
          sa('A cone sits on top of a cylinder. Both have a radius of 3. The cylinder is 10 tall and the cone is 4 tall.\nFind the total volume in terms of π.', 'Volume:', key='102π', note='90π + 12π.'),
          sa('A hemisphere (half of a sphere) has a radius of 6 cm.\nFind its volume in terms of π.', 'Volume:', key='144π cubic centimeters'),
          mc('A capsule is a cylinder with radius 2 and height 5 with half of a sphere of radius 2 on each end.\nWhat is its volume?', ['{92/3}π', '20π', '{32/3}π', '{52/3}π']),
          tf('A sphere with a radius of 3 has a volume of 36π.', key=True),
          tf('A cone with a radius of 3 and a height of 4 has a volume of 36π.', key=False, note='Its volume is 12π.'),
      ]),
      f2=B('Use geometric shapes to model real objects', 'HSG-MG.A.1', [
          sa('A tree trunk is modeled as a cylinder with a diameter of 2 feet and a height of 30 feet.\nEstimate its volume in terms of π. Then give one reason the model might overestimate or underestimate the real volume.', 'Answer:',
             key='30π cubic feet; for example, a real trunk gets narrower toward the top, so the model may overestimate.',
             note='Grade both: 30π cubic feet, and any reasonable way the real trunk differs from a cylinder.'),
          sa('A round tabletop is modeled as a circle with a circumference of 9.42 feet.\nWhat is its radius? Use 3.14 for π.', 'Radius:', key='1.5 feet'),
          mc('A pile of sand is shaped roughly like a cone that is 6 m across at the bottom and 2 m tall.\nWhich is the best estimate of its volume?', ['About 6π cubic meters', 'About 18π cubic meters', 'About 24π cubic meters', 'About 72π cubic meters']),
          tf('A rolled sleeping bag 50 cm long and 20 cm across is modeled as a cylinder. Its volume is about 5,000π cubic centimeters.', key=True),
          tf('To estimate how much cheese covers a pizza, the pizza is best modeled as a sphere.', key=False, note='A thin cylinder (or a circle, for the area) is the better model.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.6 (volume)
    S('7.G.B.6', 'Find the volume of right prisms',
      main=[
          sa('Find the volume of the right rectangular prism.', 'Volume:', fig=prism(8, 5, 3.5, ('8 cm', '5 cm', '3.5 cm')), key='140 cubic centimeters'),
          sa('A right triangular prism has triangular bases with a base of 6 m and a height of 4 m. The prism is 10 m long.\nWhat is its volume?', 'Volume:', key='120 cubic meters'),
          mc('The base of a right prism has an area of 24 square inches. The prism is 7.5 inches tall.\nWhat is its volume?', ['180 cubic inches', '31.5 cubic inches', '90 cubic inches', '360 cubic inches']),
          tf('A cube with {1/2}-foot edges has a volume of {1/8} cubic foot.', key=True),
          tf('Doubling the height of a right prism doubles the area of its base.', key=False, note='It doubles the volume; the base does not change.'),
      ],
      back=[
          B('Find the volume of a rectangular prism with fractional edges', '6.G.A.2', [
              sa('A right rectangular prism is 2{1/2} feet by 2 feet by 4 feet.\nWhat is its volume?', 'Volume:', key='20 cubic feet'),
              sa('A cube has {3/4}-inch edges.\nWhat is its volume?', 'Volume:', key='27/64 cubic inch'),
              mc('A right rectangular prism is {1/2} m by 3 m by 6 m.\nWhat is its volume?', ['9 cubic meters', '9.5 cubic meters', '18 cubic meters', '4.5 cubic meters']),
              tf('A right rectangular prism 1{1/2} cm by 2 cm by 2 cm has a volume of 6 cubic centimeters.', key=True),
              tf('A right rectangular prism {1/2} foot by {1/2} foot by 4 feet has a volume of 2 cubic feet.', key=False, note='Its volume is 1 cubic foot.'),
          ]),
          B('Find volume with V = l × w × h', '5.MD.C.5.b', [
              sa('A rectangular prism is 7 units long, 4 units wide, and 3 units tall.\nWhat is its volume?', 'Volume:', key='84 cubic units'),
              sa('A box is 10 cm long, 6 cm wide, and 5 cm tall.\nWhat is its volume?', 'Volume:', key='300 cubic centimeters'),
              mc('A rectangular prism is 9 feet by 2 feet by 3 feet.\nWhat is its volume?', ['54 cubic feet', '14 cubic feet', '27 cubic feet', '108 cubic feet']),
              tf('A cube with 4-inch edges has a volume of 64 cubic inches.', key=True),
              tf('A box 5 m by 5 m by 2 m has a volume of 12 cubic meters.', key=False, note='Its volume is 50 cubic meters.'),
          ]),
      ],
      f1=B('Compare the volumes of cylinders and prisms', '8.G.C.9', [
          sa('A cylinder has a radius of 4 inches and a height of 5 inches.\nFind its volume. Use 3.14 for π.', 'Volume:', key='251.2 cubic inches'),
          sa('A cylinder\'s base has an area of 12.56 square centimeters. The cylinder is 10 cm tall.\nWhat is its volume?', 'Volume:', key='125.6 cubic centimeters'),
          mc('A cylinder has a radius of 1 m and a height of 3 m.\nWhat is its volume in terms of π?', ['3π cubic meters', '6π cubic meters', '9π cubic meters', 'π cubic meters']),
          tf('The volume of a cylinder is its base area times its height, just like a prism.', key=True),
          tf('A cylinder with a radius of 2 and a height of 2 has a volume of 4π.', key=False, note='Its volume is 8π.'),
      ]),
      f2=B('Use volume formulas to solve problems', 'HSG-GMD.A.3', [
          sa('A pyramid has a square base with 6 m sides. It is 10 m tall.\nWhat is its volume?', 'Volume:', key='120 cubic meters'),
          sa('A cone-shaped cup has a radius of 3 cm and holds 30π cubic centimeters.\nHow tall is the cup?', 'Height:', key='10 cm'),
          mc('A sphere has a volume of 288π cubic centimeters.\nWhat is its radius?', ['6 cm', '8 cm', '12 cm', '4 cm']),
          tf('A pyramid has {1/3} the volume of a prism with the same base and height.', key=True),
          tf('A sphere with a radius of 3 has a volume of 27π.', key=False, note='Its volume is 36π.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.6 (surface area)
    S('7.G.B.6', 'Find the surface area of right prisms',
      main=[
          sa('Find the surface area of a right rectangular prism that is 6 cm by 4 cm by 3 cm.', 'Surface area:', key='108 square centimeters'),
          sa('Find the surface area of a cube with 5-inch edges.', 'Surface area:', key='150 square inches'),
          mc('A right triangular prism has triangular bases with sides of 3 cm, 4 cm, and 5 cm and a right angle between the 3 cm and 4 cm sides. The prism is 10 cm long.\nWhat is its surface area?',
             ['132 square centimeters', '120 square centimeters', '60 square centimeters', '126 square centimeters']),
          tf('A box 10 in by 2 in by 2 in needs exactly 88 square inches of paper to cover it with no overlap.', key=True),
          tf('A right rectangular prism 2 m by 3 m by 4 m has a surface area of 24 square meters.', key=False, note='Its surface area is 52 square meters; 24 cubic meters is its volume.'),
      ],
      back=[
          B('Use a net to find surface area', '6.G.A.4', [
              sa('The net of a cube has 6 squares. Each square is 4 cm by 4 cm.\nWhat is the surface area of the cube?', 'Surface area:', key='96 square centimeters'),
              sa('The net of a rectangular prism has two 5-by-3 rectangles, two 5-by-2 rectangles, and two 3-by-2 rectangles.\nWhat is the surface area?', 'Surface area:', key='62 square units'),
              mc('The net of a square pyramid has a 6-by-6 square and 4 triangles. Each triangle has a base of 6 and a height of 5.\nWhat is the surface area?', ['96 square units', '66 square units', '156 square units', '186 square units']),
              tf('A net shows all the faces of a solid laid flat.', key=True),
              tf('The net of a rectangular prism has 4 rectangles.', key=False, note='It has 6 rectangles.'),
          ]),
          B('Find the area of a rectangle', '4.MD.A.3', [
              sa('A rectangle is 8 cm by 5 cm.\nWhat is its area?', 'Area:', key='40 square centimeters'),
              sa('A rectangle is 14 inches by 3 inches.\nWhat is its area?', 'Area:', key='42 square inches'),
              mc('A rectangle is 11 m by 6 m.\nWhat is its area?', ['66 square meters', '34 square meters', '17 square meters', '60 square meters']),
              tf('A rectangle 9 feet by 2 feet has an area of 18 square feet.', key=True),
              tf('A rectangle 5 cm by 5 cm has an area of 20 square centimeters.', key=False, note='Its area is 25 square centimeters.'),
          ]),
      ],
      f1=B('Use the Pythagorean theorem in three-dimensional figures', '8.G.B.7', nearest=True, qs=[
          sa('A box is 4 units long, 3 units wide, and 12 units tall.\nHow long is a diagonal of its 4-by-3 base?', 'Length:', key='5 units'),
          sa('A box is 4 units long, 3 units wide, and 12 units tall.\nHow long is the diagonal from a bottom corner to the opposite top corner?', 'Length:', key='13 units'),
          mc('A right square pyramid (its top vertex is directly above the center of its base) has base edges of 6 m and is 4 m tall.\nWhat is the slant height (from the top vertex to the midpoint of a base edge)?', ['5 m', '7 m', '10 m', '2 m']),
          tf('A rectangle that is 6 by 8 has a diagonal of 10.', key=True),
          tf('A cube with edges of 1 has a diagonal from one corner to the opposite corner of length 2.', key=False, note='Its length is √3.'),
      ]),
      f2=B('Apply geometric methods to solve design problems', 'HSG-MG.A.3', [
          sa('A company wants a box shaped like a cube with a volume of 64 cubic inches.\nWhat is the edge length, and how much cardboard covers the box?', 'Answer:', key='4 inches; 96 square inches'),
          sa('One gallon of paint covers 350 square feet. The walls of a room total 1,225 square feet.\nHow many whole gallons should be bought?', 'Gallons:', key='4', note='3.5 gallons are needed, so 4 whole gallons.'),
          mc('Each box has a volume of 24 cubic centimeters.\nWhich box uses the least cardboard?', ['2 cm × 3 cm × 4 cm', '1 cm × 1 cm × 24 cm', '1 cm × 2 cm × 12 cm', '1 cm × 4 cm × 6 cm']),
          tf('Among rectangular boxes with the same volume, a cube has the least surface area.', key=True),
          tf('Two boxes with the same volume always have the same surface area.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.G.B.6 (composite volume) -- added in 2.0.0
    S('7.G.B.6', 'Find the volume of a solid made of right prisms', num=67,
      main=[
          sa('The solid is made of two right rectangular prisms joined face to face with no gaps or overlaps.\nFind its volume.', 'Volume:', fig=L_SOLID, key='132 cubic centimeters'),
          sa('The step-shaped solid is made of two right rectangular prisms joined face to face with no gaps or overlaps.\nFind its volume.', 'Volume:', fig=STEP_SOLID, key='90 cubic inches'),
          mc('A cube with 4 cm edges sits on top of a right rectangular prism that is 8 cm by 6 cm by 2 cm. The bottom face of the cube lies flat on the top face of the prism.\nWhat is the total volume?',
             ['160 cubic centimeters', '96 cubic centimeters', '64 cubic centimeters', '224 cubic centimeters']),
          tf('A solid is made of a 10 m by 4 m by 3 m prism and a 2 m by 4 m by 3 m prism joined end to end with no overlap. Its volume is 144 cubic meters.', key=True),
          tf('The solid is made of three right rectangular prisms with no gaps or overlaps. Its volume is 72 cubic feet.', fig=U_SOLID, key=False,
             note='The front face has an area of 9 × 2 + 3 × 2 + 3 × 2 = 30 square feet, so the volume is 30 × 2 = 60 cubic feet.'),
      ],
      back=[
          B('Add the volumes of two rectangular prisms', '5.MD.C.5.c', [
              sa('A 3 by 2 by 2 prism and a 4 by 2 by 1 prism are joined with no overlap.\nWhat is the total volume?', 'Volume:', key='20 cubic units'),
              sa('A 5 by 3 by 2 prism and a 2 by 3 by 2 prism are joined with no overlap.\nWhat is the total volume?', 'Volume:', key='42 cubic units'),
              mc('Two cubes with 3-unit edges are joined face to face.\nWhat is the total volume?', ['54 cubic units', '27 cubic units', '18 cubic units', '36 cubic units']),
              tf('A prism with a volume of 10 cubic units and a prism with a volume of 6 cubic units are joined with no overlap. The total volume is 16 cubic units.', key=True),
              tf('A 2 by 2 by 2 cube and a 2 by 2 by 4 prism are joined with no overlap. The total volume is 12 cubic units.', key=False, note='8 + 16 = 24 cubic units.'),
          ]),
          B('Find the area of a figure made of rectangles', '3.MD.C.7.d', [
              sa('A 4 by 2 rectangle and a 2 by 3 rectangle are joined with no overlap.\nWhat is the total area?', 'Area:', key='14 square units'),
              sa('A 6 by 3 rectangle and a 3 by 3 rectangle are joined with no overlap.\nWhat is the total area?', 'Area:', key='27 square units'),
              mc('A U-shape is made of three rectangles with no overlap: 2 by 4, 4 by 2, and 2 by 4.\nWhat is the total area?', ['24 square units', '16 square units', '32 square units', '20 square units']),
              tf('A 5 by 2 rectangle and a 2 by 2 rectangle joined with no overlap have a total area of 14 square units.', key=True),
              tf('A 3 by 3 rectangle and a 3 by 1 rectangle joined with no overlap have a total area of 10 square units.', key=False, note='9 + 3 = 12 square units.'),
          ]),
      ],
      f1=B('Find the volume of a solid made of a prism and a cylinder', '8.G.C.9', [
          sa('A cylinder with a radius of 2 cm and a height of 6 cm stands on top of a 10 cm by 10 cm by 4 cm block.\nFind the total volume in terms of π.', 'Volume:', key='400 + 24π cubic centimeters'),
          sa('A cylinder with a radius of 3 inches and a height of 8 inches stands on top of a cube with 8-inch edges.\nFind the total volume in terms of π.', 'Volume:', key='512 + 72π cubic inches'),
          mc('A cube with 6 cm edges has a cylinder-shaped hole with a radius of 1 cm drilled straight through it (6 cm long).\nWhat volume is left?',
             ['216 - 6π cubic centimeters', '216 + 6π cubic centimeters', '216 - 36π cubic centimeters', '6π cubic centimeters']),
          tf('A 2 by 2 by 10 prism with half of a cylinder (radius 1, length 10) on top has a volume of 40 + 5π.', key=True),
          tf('A cylinder with a radius of 1 and a height of 5 is stacked on a cylinder with a radius of 1 and a height of 3. The total volume is 15π.', key=False, note='π(1²)(5 + 3) = 8π.'),
      ]),
      f2=B('Use volume formulas to solve problems with composite solids', 'HSG-GMD.A.3', [
          sa('A silo is a cylinder with a radius of 3 m and a height of 10 m, topped with half of a sphere with a radius of 3 m.\nFind its volume in terms of π.', 'Volume:', key='108π cubic meters'),
          sa('A pencil is a cylinder with a radius of 0.4 cm and a length of 15 cm, with a cone-shaped tip with a radius of 0.4 cm and a height of 1.5 cm.\nFind its volume in terms of π.', 'Volume:', key='2.48π cubic centimeters'),
          mc('A cone with a radius of 3 and a height of 4 is carved out of a cylinder with a radius of 3 and a height of 4.\nWhat volume is left?', ['24π', '12π', '36π', '48π']),
          tf('A square pyramid with 6 m base edges and a height of 4 m sits on top of a cube with 6 m edges. The total volume is 264 cubic meters.', key=True),
          tf('Two halves of a sphere with a radius of 2 are joined to make a whole sphere. Its volume is {16/3}π.', key=False, note='The volume is (4/3)π(2³) = 32/3 π.'),
      ])),

    # ------------------------------------------------------------------ 7.G.B.6 (composite surface area) -- added in 2.0.0
    S('7.G.B.6', 'Find the exterior surface area of a solid made of right prisms', num=68,
      main=[
          sa('Two cubes with 2 cm edges are joined face to face.\nFind the exterior surface area of the solid. (The faces where the cubes touch are hidden and are not counted.)', 'Surface area:',
             fig=TWO_CUBES, key='40 square centimeters'),
          sa('A cube with 2 m edges sits on top of a 6 m by 6 m by 2 m prism. Its bottom face lies completely on the top face of the prism.\nFind the exterior surface area. (Do not count the faces where the solids touch.)', 'Surface area:',
             key='136 square meters', note='The prism has 120 square meters, minus the 4 square meters covered by the cube, plus 5 faces of the cube (20 square meters).'),
          mc('The solid is made of two right rectangular prisms joined face to face.\nWhat is its exterior surface area?',
             ['178 square centimeters', '132 square centimeters', '210 square centimeters', '112 square centimeters'], fig=L_SOLID),
          tf('Two 1 by 1 by 1 cubes joined face to face have an exterior surface area of 10 square units.', key=True),
          tf('When two prisms are joined face to face, the exterior surface area is the sum of their two surface areas.', key=False,
             note='Both copies of the shared face are hidden, so twice the shared area is subtracted.'),
      ],
      back=[
          B('Find the surface area of a rectangular prism', '6.G.A.4', [
              sa('Use a net to find the surface area of a 3 by 2 by 1 rectangular prism.', 'Surface area:', key='22 square units'),
              sa('Use a net to find the surface area of a cube with 3-inch edges.', 'Surface area:', key='54 square inches'),
              mc('What is the surface area of a 4 by 1 by 1 rectangular prism?', ['18 square units', '16 square units', '4 square units', '24 square units']),
              tf('A 2 by 2 by 1 rectangular prism has a surface area of 16 square units.', key=True),
              tf('A 5 by 1 by 1 rectangular prism has a surface area of 20 square units.', key=False, note='Its surface area is 22 square units.'),
          ]),
          B('Find the area of a rectangle by multiplying', '3.MD.C.7.b', [
              sa('A face of a box is 6 cm by 4 cm.\nWhat is its area?', 'Area:', key='24 square centimeters'),
              sa('A face of a box is 7 m by 3 m.\nWhat is its area?', 'Area:', key='21 square meters'),
              mc('A face of a box is 5 inches by 5 inches.\nWhat is its area?', ['25 square inches', '20 square inches', '10 square inches', '30 square inches']),
              tf('A 9 by 2 face has an area of 18 square units.', key=True),
              tf('A 4 by 8 face has an area of 24 square units.', key=False, note='Its area is 32 square units.'),
          ]),
      ],
      f1=B('Use the Pythagorean theorem to find a slanted edge needed for surface area', '8.G.B.7', nearest=True, qs=[
          sa('A ramp is a right triangular prism. Its triangular ends have legs of 3 m and 4 m.\nHow wide is the sloped face (the hypotenuse of the end)?', 'Width:', key='5 m'),
          sa('A tent is a triangular prism. Each end is an isosceles triangle with a base of 6 feet and a height of 4 feet.\nHow long is each slanted side?', 'Length:', key='5 feet'),
          mc('The end of a prism is a right triangle with legs of 5 and 12.\nHow long is its hypotenuse?', ['13', '17', '7', '√119']),
          tf('A ramp with triangular ends whose legs are 6 and 8 has a sloped face that is 10 units wide.', key=True),
          tf('A tent end is an isosceles triangle with a base of 10 and a height of 12. Each slanted side is 12 units long.', key=False, note='Each slanted side is √(5² + 12²) = 13.'),
      ]),
      f2=B('Apply surface area to design problems', 'HSG-MG.A.3', [
          sa('A gift is made of two cubes with 3-inch edges joined face to face.\nHow much wrapping paper covers its outside exactly?', 'Paper:', key='90 square inches'),
          sa('A shed is a 10 ft by 8 ft by 8 ft rectangular prism (8 ft tall). Its four walls and its flat roof are painted, but not the floor. One quart of paint covers 40 square feet.\nHow many whole quarts are needed?', 'Quarts:',
             key='10 quarts', note='The walls and roof are 368 square feet, which needs 9.2 quarts, so 10 whole quarts.'),
          mc('Two 1 by 2 by 3 prisms are joined face to face with matching faces.\nWhich way of joining them gives the least exterior surface area?',
             ['Joining their 2 by 3 faces', 'Joining their 1 by 2 faces', 'Joining their 1 by 3 faces', 'All three ways give the same surface area']),
          tf('Joining two solids face to face lowers the total exterior surface area by twice the area of the shared face.', key=True),
          tf('A box with a smaller surface area always has a smaller volume.', key=False),
      ])),
]
