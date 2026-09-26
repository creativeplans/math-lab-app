from qb import (S, B, sa, mc, tf, coord, q1, shape, poly, rect, tri, para, trap, prism,
                net_prism, net_pyramid, net_triprism, net_tetra, plot)


def L(pts, labels, **kw):
    return shape([poly(pts, labels)], **kw)


HOUSE = shape([poly([(0, 0), (10, 0), (10, 6), (5, 10), (0, 6)], ['10 ft', '6 ft', None, None, None])],
              segs=[dict(a=(5, 10), b=(5, 6), label='4 ft', off=(10, 0)), dict(a=(0, 6), b=(10, 6))])
HOUSE7 = shape([poly([(0, 0), (8, 0), (8, 5), (4, 8), (0, 5)], ['8 m', '5 m', None, None, None])],
               segs=[dict(a=(4, 8), b=(4, 5), label='3 m', off=(10, 0)), dict(a=(0, 5), b=(8, 5))])

SETS = [
    # ------------------------------------------------------------------ 6.G.A.1 triangles
    S('6.G.A.1', 'Area of right triangles and other triangles',
      main=[
          sa('Find the area of the triangle.', 'Area:', fig=tri(10, 6, 3, '10 cm', '6 cm')),
          sa('Find the area of the right triangle.', 'Area:', fig=tri(8, 5, 0, '8 in.', '5 in.')),
          sa('Find the area of the triangle.', 'Area:', fig=tri(6, 5, 9, '6 m', '5 m')),
          mc('A triangle has a base of 12 feet and a height of 7 feet.\nWhat is its area?',
             ['42 square feet', '84 square feet', '19 square feet', '38 square feet']),
          sa('A triangular sign has a base of 3.5 feet and a height of 2 feet.\nWhat is its area?', 'Area:'),
      ],
      back=[
          B('Area of rectangles', '3.MD.C.7.b', [
              sa('Find the area of the rectangle.', 'Area:', fig=rect(7, 4, '7 cm', '4 cm')),
              sa('A rectangle is 9 feet long and 6 feet wide.\nWhat is its area?', 'Area:'),
              tf('A rectangle that is 5 cm long and 3 cm wide has an area of 15 square centimeters.'),
              mc('A rectangle is 12 m long and 4 m wide.\nWhat is its area?', ['48 square meters', '32 square meters', '16 square meters', '24 square meters']),
              sa('Find the area of the rectangle.', 'Area:', fig=rect(10, 6, '10 in.', '6 in.')),
          ]),
          B('Half of a product', '5.NF.B.4.a', [
              sa('Multiply.\n{1/2} × 10 × 6', 'Product:'),
              sa('Multiply.\n{1/2} × 14', 'Product:'),
              tf('{1/2} × 8 × 5 = 20'),
              mc('{1/2} × 12 × 7 = ?', ['42', '84', '19', '21']),
              sa('Multiply.\n{1/2} × 9 × 4', 'Product:'),
          ]),
          B('Right angles and perpendicular segments', '4.G.A.1', [
              tf('Perpendicular lines meet to form right angles.'),
              mc('Which angle measure is a right angle?', ['90°', '45°', '180°', '100°']),
              tf('The dashed segment is perpendicular to the base of the triangle.', fig=tri(10, 6, 3, None, 'h')),
              sa('How many degrees are in a right angle?', 'Degrees:'),
              tf('A square has 4 right angles.'),
          ]),
      ],
      f1=B('Area and volume of figures made of triangles', '7.G.B.6', [
          sa('Find the area of the figure.', 'Area:', fig=HOUSE7),
          sa('A kite is made of two triangles. Each triangle has a base of 10 inches and a height of 4 inches.\nWhat is the area of the kite?', 'Area:'),
          mc('A triangle with a base of 4 cm and a height of 3 cm is cut out of a rectangle that is 12 cm by 6 cm.\nWhat is the area of the part that is left?',
             ['66 square cm', '72 square cm', '78 square cm', '60 square cm']),
          sa('A triangular prism has triangle bases with a base of 6 cm and a height of 4 cm. The prism is 10 cm long.\nWhat is its volume?', 'Volume:'),
          tf('A figure made of a 6-by-4 rectangle and a triangle with a base of 3 and a height of 4 has an area of 30 square units.'),
      ]),
      f2=B('Use the Pythagorean Theorem in right triangles', '8.G.B.7',
           [
               sa('A right triangle has legs of 6 cm and 8 cm.\nWhat is the length of the hypotenuse?', 'Hypotenuse:'),
               sa('Find the length b.', 'b =', fig=tri(12, 5, 0, 'b', '5 cm', sides=(None, '13 cm'))),
               mc('A 10-foot ladder leans against a wall. The top reaches 8 feet up the wall.\nHow far is the bottom of the ladder from the wall?',
                  ['6 feet', '2 feet', '18 feet', '12.8 feet']),
               sa('An isosceles triangle has a base of 16 inches and two sides of 10 inches.\nWhat is its area?', 'Area:'),
               sa('A right triangle has legs of 9 m and 12 m.\nWhat is the length of the hypotenuse?', 'Hypotenuse:'),
           ])),

    # ------------------------------------------------------------------ 6.G.A.1 quadrilaterals
    S('6.G.A.1', 'Area of parallelograms and trapezoids',
      main=[
          sa('Find the area of the parallelogram.', 'Area:', fig=para(8, 4, 3, '8 cm', '4 cm', side='5 cm')),
          sa('Find the area of the trapezoid.', 'Area:', fig=trap(12, 6, 5, 3, '12 m', '6 m', '5 m')),
          mc('A parallelogram has a base of 9 feet and a height of 5 feet.\nWhat is its area?',
             ['45 square feet', '22.5 square feet', '14 square feet', '28 square feet']),
          sa('A trapezoid has bases of 7 inches and 11 inches. Its height is 4 inches.\nWhat is its area?', 'Area:'),
          sa('A parallelogram has a base of 12.5 meters and a height of 4 meters.\nWhat is its area?', 'Area:'),
      ],
      back=[
          B('Area of rectangles', '3.MD.C.7.b', [
              sa('Find the area of the rectangle.', 'Area:', fig=rect(8, 3, '8 ft', '3 ft')),
              sa('A rectangle is 11 cm long and 5 cm wide.\nWhat is its area?', 'Area:'),
              tf('A square with 6-meter sides has an area of 24 square meters.'),
              mc('A rectangle is 15 inches long and 2 inches wide.\nWhat is its area?', ['30 square inches', '17 square inches', '34 square inches', '60 square inches']),
              sa('Find the area of the rectangle.', 'Area:', fig=rect(9, 7, '9 m', '7 m')),
          ]),
          B('Area by splitting into rectangles', '3.MD.C.7.d', [
              sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (8, 0), (8, 3), (3, 3), (3, 6), (0, 6)], ['8', '3', '5', '3', '3', '6'])),
              sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (6, 0), (6, 2), (2, 2), (2, 5), (0, 5)], ['6', '2', '4', '3', '2', '5'])),
              tf('The area of an L-shaped figure can be found by adding the areas of two rectangles.'),
              mc('A figure is made of a 4-by-5 rectangle and a 2-by-3 rectangle that do not overlap.\nWhat is its area?', ['26 square units', '14 square units', '20 square units', '120 square units']),
              sa('A figure is made of a 10-by-2 rectangle and a 3-by-3 square that do not overlap.\nWhat is its area?', 'Area:'),
          ]),
          B('Classifying quadrilaterals', '5.G.B.4', [
              tf('Every rectangle is a parallelogram.'),
              tf('Every parallelogram is a rectangle.'),
              mc('Which quadrilateral always has four right angles?', ['Rectangle', 'Rhombus', 'Trapezoid', 'Parallelogram']),
              mc('How many pairs of parallel sides does a parallelogram have?', ['2', '1', '0', '4']),
              tf('A square is a rhombus.'),
          ]),
          B('Height is perpendicular to the base', '4.G.A.1', [
              tf('The height of a parallelogram is perpendicular to its base.'),
              tf('The dashed segment shows the height of the parallelogram.', fig=para(8, 4, 3, None, 'h')),
              mc('Which statement describes perpendicular lines?', ['They meet at right angles.', 'They never meet.', 'They meet at a 45° angle.', 'They are always the same length.']),
              tf('The slanted side of a parallelogram is always its height.'),
              sa('What is the measure of the angle between a base and its height?', 'Angle:'),
          ]),
      ],
      f1=B('Area of figures made of quadrilaterals in real-world problems', '7.G.B.6', [
          sa('A patio is made of a rectangle that is 10 ft by 6 ft and a trapezoid with bases of 6 ft and 4 ft and a height of 3 ft.\nWhat is the area of the patio?', 'Area:'),
          sa('A wall is 12 ft by 8 ft. It has a window shaped like a parallelogram with a base of 3 ft and a height of 2 ft.\nWhat is the area of the wall that is not window?', 'Area:'),
          mc('A sign is a trapezoid with bases of 1.5 m and 2.5 m and a height of 1.2 m.\nWhat is its area?', ['2.4 square meters', '4.8 square meters', '5.2 square meters', '3.6 square meters']),
          sa('A garden is made of two parallelograms that do not overlap. Each has a base of 7 m and a height of 4 m.\nWhat is the total area?', 'Area:'),
          tf('A trapezoid with bases of 6 and 10 and a height of 5 has the same area as a rectangle that is 8 by 5.'),
      ]),
      f2=B('Use the Pythagorean Theorem to find a missing height', '8.G.B.7', [
          sa('A parallelogram has a slanted side of 5 cm. The slanted side, the height, and a 3 cm piece of the base form a right triangle.\nWhat is the height?', 'Height:'),
          sa('Find the height h of the trapezoid.', 'h =', fig=shape([poly([(0, 0), (14, 0), (11, 4), (3, 4)], ['14 in.', '5 in.', '8 in.', '5 in.'])],
                                                                  segs=[dict(a=(3, 4), b=(3, 0), label='h', off=(10, 0))], ra=[((3, 0), (3, 4), (14, 0))])),
          mc('A ramp forms a right triangle. The ramp is 13 ft long and its base is 12 ft long.\nHow tall is the ramp?', ['5 ft', '25 ft', '17.7 ft', '1 ft']),
          sa('A parallelogram has a slanted side of 10 m. The slanted side, the height, and a 6 m piece of the base form a right triangle.\nWhat is the height?', 'Height:'),
          tf('A trapezoid has a slanted side of 10 in. The slanted side, the height, and a 6 in. piece of the base form a right triangle. The height is 8 in.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.1 composite polygons
    S('6.G.A.1', 'Area of polygons by composing and decomposing',
      main=[
          sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (12, 0), (12, 4), (5, 4), (5, 9), (0, 9)], ['12 m', '4 m', '7 m', '5 m', '5 m', '9 m'])),
          sa('Find the area of the figure.', 'Area:', fig=HOUSE),
          sa('A rectangular yard is 20 m by 15 m. A triangular garden in the yard has a base of 6 m and a height of 5 m.\nWhat is the area of the yard that is NOT garden?', 'Area:'),
          mc('A polygon is split into a rectangle that is 8 by 3 and two triangles. Each triangle has a base of 2 and a height of 3.\nWhat is the area of the polygon?', ['30 square units', '27 square units', '36 square units', '24 square units']),
          sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (10, 0), (10, 4), (4, 8), (0, 8)], ['10 cm', '4 cm', None, '4 cm', '8 cm'])),
      ],
      back=[
          B('Area of rectilinear figures', '3.MD.C.7.d', [
              sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (7, 0), (7, 2), (4, 2), (4, 6), (0, 6)], ['7', '2', '3', '4', '4', '6'])),
              sa('Find the area of the figure.', 'Area:', fig=L([(0, 0), (9, 0), (9, 5), (6, 5), (6, 2), (0, 2)], ['9', '5', '3', '3', '6', '2'])),
              tf('A figure made of a 5-by-2 rectangle and a 3-by-4 rectangle has an area of 22 square units.'),
              mc('Which expression gives the area of the figure?', ['4 × 3 + 2 × 2', '4 × 5', '4 + 3 + 2 + 2', '4 × 3 × 2'],
                 fig=L([(0, 0), (4, 0), (4, 3), (2, 3), (2, 5), (0, 5)], ['4', '3', '2', '2', '2', '5'])),
              sa('A figure is made of two rectangles: 6 by 3 and 2 by 4.\nWhat is its area?', 'Area:'),
          ]),
          B('Missing side lengths of rectangles', '4.MD.A.3', [
              sa('A rectangle has an area of 48 square feet and a width of 6 feet.\nWhat is its length?', 'Length:'),
              sa('A rectangle has a perimeter of 30 cm and a length of 9 cm.\nWhat is its width?', 'Width:'),
              tf('A rectangle with an area of 36 square cm and a length of 9 cm has a width of 4 cm.'),
              mc('A rectangle has an area of 56 square inches and a width of 7 inches.\nWhat is its length?', ['8 inches', '49 inches', '63 inches', '9 inches']),
              sa('The rectangle has an area of 60 square meters.\nWhat is the missing side length?', 'Length:', fig=rect(12, 5, '12 m', '?')),
          ]),
          B('Area of triangles', '6.G.A.1', [
              sa('Find the area of the triangle.', 'Area:', fig=tri(8, 6, 5, '8 cm', '6 cm')),
              sa('A triangle has a base of 10 m and a height of 3 m.\nWhat is its area?', 'Area:'),
              tf('A right triangle with legs of 4 in. and 6 in. has an area of 24 square inches.'),
              mc('A triangle has a base of 5 ft and a height of 8 ft.\nWhat is its area?', ['20 square feet', '40 square feet', '13 square feet', '26 square feet']),
              sa('Find the area of the triangle.', 'Area:', fig=tri(6, 4, 0, '6 ft', '4 ft')),
          ]),
      ],
      f1=B('Area of composite figures in real-world problems', '7.G.B.6', [
          sa('A deck is made of a rectangle that is 12 ft by 10 ft and a triangle with a base of 10 ft and a height of 6 ft.\nWhat is the area of the deck?', 'Area:'),
          sa('A trapezoid-shaped garden has bases of 8 m and 14 m and a height of 5 m. It has a square pond with 2 m sides.\nWhat is the area of the garden without the pond?', 'Area:'),
          mc('A regular hexagon is split into 6 equal triangles. Each triangle has a base of 4 cm and a height of 3.5 cm.\nWhat is the area of the hexagon?',
             ['42 square cm', '84 square cm', '21 square cm', '24 square cm']),
          sa('An L-shaped prism has a base area of 30 square feet and a height of 4 feet.\nWhat is its volume?', 'Volume:'),
          tf('A figure made of a 5-by-5 square and a triangle with a base of 5 and a height of 2 has an area of 30 square units.'),
      ]),
      f2=B('Volume of composite solids', '8.G.C.9', [
          sa('A silo is a cylinder with a radius of 3 m and a height of 10 m, topped by a hemisphere with a radius of 3 m.\nWhat is its volume in terms of π?', 'Volume:'),
          sa('A cone has a radius of 3 in. and a height of 4 in. A hemisphere with a radius of 3 in. sits on top.\nWhat is the total volume in terms of π?', 'Volume:'),
          mc('A cone with a radius of 2 and a height of 3 is cut out of a cylinder with a radius of 2 and a height of 6.\nWhat volume is left?', ['20π', '28π', '24π', '4π']),
          sa('A cylinder and a cone each have a radius of 1 and a height of 2.\nHow much more volume does the cylinder have, in terms of π?', 'Difference:'),
          tf('A sphere with a radius of 3 has the same volume as a cylinder with a radius of 3 and a height of 4.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.2 packing
    S('6.G.A.2', 'Find volume by packing a prism with unit-fraction cubes',
      main=[
          sa('How many cubes with {1/2}-inch edges fill a box that is 2 in. by 1{1/2} in. by 1 in.?', 'Cubes:'),
          sa('A box is 3 in. by 2 in. by 1{1/2} in.\nHow many cubes with {1/2}-inch edges fill the box?', 'Cubes:'),
          tf('A prism is packed with 48 cubes that each have {1/2}-unit edges. Its volume is 6 cubic units.'),
          mc('A prism is packed with 64 cubes that each have {1/4}-inch edges.\nWhat is the volume of the prism?', ['1 cubic inch', '16 cubic inches', '4 cubic inches', '{1/4} cubic inch']),
          sa('The prism is packed with cubes that have {1/2}-cm edges. It is 5 cubes long, 4 cubes wide, and 3 cubes tall.\nWhat is its volume?', 'Volume:', fig=prism(5, 4, 3, grid=True)),
      ],
      back=[
          B('Volume by counting unit cubes', '5.MD.C.4', [
              sa('Each cube is 1 cubic unit.\nWhat is the volume of the prism?', 'Volume:', fig=prism(3, 2, 2, grid=True)),
              sa('Each cube is 1 cubic unit.\nWhat is the volume of the prism?', 'Volume:', fig=prism(4, 2, 3, grid=True)),
              tf('A prism made of 2 layers with 6 unit cubes in each layer has a volume of 12 cubic units.'),
              mc('A box holds 3 layers with 5 unit cubes in each layer.\nWhat is its volume?', ['15 cubic units', '8 cubic units', '35 cubic units', '53 cubic units']),
              sa('Each cube is 1 cubic unit.\nWhat is the volume of the prism?', 'Volume:', fig=prism(2, 2, 2, grid=True)),
          ]),
          B('The volume of one small cube', '5.NF.B.4.a', [
              sa('Multiply.\n{1/2} × {1/2} × {1/2}', 'Product:'),
              sa('Multiply.\n{1/4} × {1/4} × {1/4}', 'Product:'),
              tf('{1/3} × {1/3} × {1/3} = {1/9}'),
              mc('Multiply.\n24 × {1/8}', ['3', '{1/3}', '192', '32']),
              sa('Multiply.\n64 × {1/64}', 'Product:'),
          ]),
          B('Volume as the number of unit cubes', '5.MD.C.3.b', [
              tf('A solid that can be packed with 20 unit cubes with no gaps has a volume of 20 cubic units.'),
              mc('A box is filled with 36 unit cubes with no gaps or overlaps.\nWhat is its volume?', ['36 cubic units', '36 square units', '6 cubic units', '12 cubic units']),
              sa('A box is filled with 45 unit cubes with no gaps.\nWhat is its volume?', 'Volume:'),
              tf('Volume is measured in square units.'),
              mc('Which unit could be used to measure volume?', ['Cubic centimeters', 'Square centimeters', 'Centimeters', 'Kilograms']),
          ]),
      ],
      f1=B('Volume of prisms in real-world problems', '7.G.B.6', [
          sa('A triangular prism has triangle bases with a base of 5 in. and a height of 4 in. The prism is 8 in. long.\nWhat is its volume?', 'Volume:'),
          sa('A prism has a base area of 12{1/2} square cm and a height of 4 cm.\nWhat is its volume?', 'Volume:'),
          mc('A cube has edges of 2.5 cm.\nWhat is its volume?', ['15.625 cubic cm', '7.5 cubic cm', '6.25 cubic cm', '15 cubic cm']),
          sa('An aquarium is 30 in. long, 12 in. wide, and 16 in. tall. It is filled with water to a height of 12 in.\nWhat is the volume of the water?', 'Volume:'),
          tf('A triangular prism with a base area of 15 square units and a length of 6 units has a volume of 90 cubic units.'),
      ]),
      f2=B('Volume of cylinders, cones, and spheres', '8.G.C.9', [
          sa('A cylinder has a radius of 5 and a height of 4.\nWhat is its volume in terms of π?', 'Volume:'),
          sa('Find the volume of the cylinder.\nUse 3.14 for π.', 'Volume:', fig=dict(k='cyl', r=2, h=7, rlab='2 cm', hlab='7 cm')),
          mc('A cone has a radius of 6 and a height of 5.\nWhat is its volume?', ['60π', '180π', '30π', '150π'], fig=dict(k='cone', r=6, h=5, rlab='6', hlab='5')),
          sa('A sphere has a radius of 6.\nWhat is its volume in terms of π?', 'Volume:'),
          tf('A cylinder has a greater volume than a cone with the same radius and height.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.2 formula
    S('6.G.A.2', 'Apply V = l w h and V = b h with fractional edge lengths',
      main=[
          sa('Find the volume of the rectangular prism.', 'Volume:', fig=prism(2.5, 3, 4.5, ('2{1/2} ft', '3 ft', '4{1/2} ft'))),
          mc('A box is 1{1/2} ft long, 2 ft wide, and {3/4} ft tall.\nWhat is its volume?', ['2{1/4} cubic feet', '4{1/4} cubic feet', '3 cubic feet', '2{3/4} cubic feet']),
          sa('Use V = l × w × h to find the volume of a prism with l = 5 cm, w = 2{1/2} cm, and h = 1{1/5} cm.', 'V ='),
          sa('A cube has edges of 1{1/2} feet.\nWhat is its volume?', 'Volume:'),
          sa('A prism has a base area of 4{1/2} square inches and a height of 2{2/3} inches.\nUse V = b × h to find its volume.', 'V ='),
      ],
      back=[
          B('Volume formula with whole numbers', '5.MD.C.5.b', [
              sa('Find the volume of the prism.', 'Volume:', fig=prism(6, 4, 3, ('6 cm', '4 cm', '3 cm'))),
              sa('A prism has a length of 10 m, a width of 2 m, and a height of 5 m.\nWhat is its volume?', 'Volume:'),
              tf('A cube with 3-inch edges has a volume of 27 cubic inches.'),
              mc('A box is 8 in. by 5 in. by 2 in.\nWhat is its volume?', ['80 cubic inches', '15 cubic inches', '40 cubic inches', '160 cubic inches']),
              sa('A prism has a base area of 20 square cm and a height of 6 cm.\nWhat is its volume?', 'Volume:'),
          ]),
          B('Multiplying mixed numbers', '5.NF.B.6', [
              sa('Multiply.\n2{1/2} × 3', 'Product:'),
              sa('Multiply.\n1{1/2} × {3/4}', 'Product:'),
              tf('2{1/2} × 2 = 5'),
              mc('3 × 4{1/2} = ?', ['13{1/2}', '12{1/2}', '7{1/2}', '12{1/6}']),
              sa('Multiply.\n1{1/3} × 1{1/2}', 'Product:'),
          ]),
          B('Multiplying fractions', '5.NF.B.4.a', [
              sa('Multiply.\n{3/4} × {2/3}', 'Product:'),
              sa('Multiply.\n{5/2} × {9/2}', 'Product:'),
              tf('{3/2} × {3/2} = {9/4}'),
              mc('{1/2} × {4/5} = ?', ['{2/5}', '{5/7}', '{4/7}', '{8/5}']),
              sa('Multiply.\n{6/5} × 5', 'Product:'),
          ]),
      ],
      f1=B('Volume of triangular and rectangular prisms', '7.G.B.6', [
          sa('A triangular prism has triangle bases with a base of 6 cm and a height of 4 cm. The prism is 9 cm long.\nWhat is its volume?', 'Volume:'),
          sa('A tent is a triangular prism. Its triangle has a base of 2.4 m and a height of 1.5 m. The tent is 3 m long.\nWhat is its volume?', 'Volume:'),
          mc('A prism has a base area of 7.5 square feet and a height of 2.4 feet.\nWhat is its volume?', ['18 cubic feet', '9.9 cubic feet', '15 cubic feet', '180 cubic feet']),
          sa('A box is 4.5 cm by 2 cm by 3.2 cm.\nWhat is its volume?', 'Volume:'),
          tf('A triangular prism with a triangle area of 10 square inches and a length of 7 inches has a volume of 70 cubic inches.'),
      ]),
      f2=B('Volume of cylinders using V = Bh', '8.G.C.9', [
          sa('A cylinder has a base area of 12π square cm and a height of 5 cm.\nWhat is its volume in terms of π?', 'Volume:'),
          sa('A can has a radius of 3 in. and a height of 8 in.\nWhat is its volume in terms of π?', 'Volume:'),
          mc('A cylinder has a radius of 1.5 m and a height of 4 m.\nWhat is its volume?', ['9π cubic meters', '6π cubic meters', '12π cubic meters', '3π cubic meters']),
          sa('Find the volume of the cylinder in terms of π.', 'Volume:', fig=dict(k='cyl', r=5, h=2, rlab='5 ft', hlab='2 ft')),
          tf('Doubling the height of a cylinder doubles its volume.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.3 draw
    S('6.G.A.3', 'Draw polygons in the coordinate plane from the coordinates of their vertices',
      main=[
          sa('Plot A(-3, 2), B(4, 2), C(4, -3), and D(-3, -3). Connect them in order.\nWhat polygon did you draw?', 'Polygon:', fig=coord()),
          sa('Plot P(0, 4), Q(3, -2), and R(-3, -2). Connect them in order.\nWhat polygon did you draw?', 'Polygon:', fig=coord()),
          sa('Plot E(-2, 1), F(2, 1), G(4, -3), and H(-4, -3). Connect them in order.\nWhat polygon did you draw?', 'Polygon:', fig=coord()),
          sa('Plot J(-1, 3), K(3, 3), L(3, -1), and M(-1, -1). Connect them in order.\nWhat polygon did you draw?', 'Polygon:', fig=coord()),
          sa('Plot W(-5, -2), X(-2, 3), Y(4, 3), and Z(1, -2). Connect them in order.\nWhat polygon did you draw?', 'Polygon:', fig=coord()),
      ],
      back=[
          B('Plotting points in all four quadrants', '6.NS.C.6.c', [
              plot('Plot and label point A(-3, 2).', coord()),
              plot('Plot and label point B(4, -3).', coord()),
              mc('Which point is at (-2, -4)?', ['Point A', 'Point B', 'Point C', 'Point D'], fig=coord(pts=[(-2, -4, 'A'), (-4, -2, 'B'), (2, 4, 'C'), (2, -4, 'D')])),
              plot('Plot and label point C(0, 4).', coord()),
              tf('Point D is at (-3, -3).', fig=coord(pts=[(-3, -3, 'D')])),
          ]),
          B('Attributes of quadrilaterals', '3.G.A.1', [
              tf('A rectangle has 4 right angles.'),
              tf('Opposite sides of a rectangle have the same length.'),
              mc('Which shape always has 4 sides of equal length and 4 right angles?', ['Square', 'Rectangle', 'Trapezoid', 'Rhombus']),
              tf('Every quadrilateral has 4 right angles.'),
              sa('How many sides does a quadrilateral have?', 'Sides:'),
          ]),
          B('Naming shapes by sides and angles', '2.G.A.1', [
              sa('A shape has 3 sides and 3 angles.\nWhat is it called?', 'Shape:'),
              mc('How many sides does a pentagon have?', ['5', '4', '6', '8']),
              tf('A hexagon has 6 sides.'),
              sa('A shape has 4 sides and 4 angles.\nWhat is it called?', 'Shape:'),
              mc('Which shape has the most sides?', ['Hexagon', 'Pentagon', 'Triangle', 'Quadrilateral']),
          ]),
      ],
      f1=B('Draw shapes with given conditions', '7.G.A.2', [
          plot('Draw a rectangle with an area of 12 square units. One vertex is at the origin.', coord()),
          plot('Draw a right triangle with legs of 4 units and 3 units. One vertex is at (-2, -2).', coord()),
          sa('Can a triangle have side lengths of 2 cm, 3 cm, and 6 cm? Write yes or no.', 'Answer:'),
          mc('A triangle has angles of 90° and 45°.\nWhat is the third angle?', ['45°', '90°', '135°', '55°']),
          plot('Draw a square with a side length of 5 units. One vertex is at (-3, 1).', coord()),
      ]),
      f2=B('Draw images of polygons under transformations', '8.G.A.3', [
          plot('Triangle ABC has vertices A(1, 1), B(4, 1), and C(1, 3).\nDraw its image after a translation 5 units left and 2 units down.', coord()),
          plot('Rectangle PQRS has vertices P(1, 2), Q(4, 2), R(4, 4), and S(1, 4).\nDraw its image after a reflection across the x-axis.', coord()),
          sa('Triangle ABC has vertices A(2, 1), B(4, 3), and C(2, 3). It is rotated 180° about the origin.\nWhat are the coordinates of B′?', 'B′ ='),
          plot('Square EFGH has vertices E(1, 1), F(2, 1), G(2, 2), and H(1, 2).\nDraw its image after a dilation by a scale factor of 3 centered at the origin.', coord()),
          tf('A rectangle with vertices (1, 1), (3, 1), (3, 2), (1, 2) is reflected across the y-axis. One image vertex is (-3, 2).'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.3 side lengths
    S('6.G.A.3', 'Use coordinates to find side lengths and perimeters of polygons',
      main=[
          sa('A rectangle has vertices at (-3, 2), (4, 2), (4, -5), and (-3, -5).\nWhat is its perimeter?', 'Perimeter:'),
          sa('One side of a polygon goes from (-2, -3) to (-2, 5).\nHow long is this side?', 'Length:'),
          sa('What is the length of side AB?', 'AB =', fig=coord(pts=[(-5, 3, 'A', 'nw'), (2, 3, 'B', 'ne'), (2, -4, 'C', 'se'), (-5, -4, 'D', 'sw')],
                                                           polys=[[(-5, 3), (2, 3), (2, -4), (-5, -4)]])),
          mc('A triangle has vertices at (-4, 1), (2, 1), and (2, -7).\nHow long is the horizontal side?', ['6 units', '8 units', '2 units', '10 units']),
          sa('A rectangle has vertices at (-5, -2), (1, -2), (1, 3), and (-5, 3).\nWhat is its perimeter?', 'Perimeter:'),
      ],
      back=[
          B('Distance between points with the same x or y', '6.NS.C.8', [
              sa('Find the distance between (-3, 2) and (4, 2).', 'Distance:'),
              sa('Find the distance between (1, -4) and (1, 6).', 'Distance:'),
              tf('The distance between (-5, 0) and (5, 0) is 10.'),
              mc('What is the distance between (2, -3) and (2, -8)?', ['5', '11', '-5', '-11']),
              sa('Find the distance between (-6, -1) and (-2, -1).', 'Distance:'),
          ]),
          B('Absolute value', '6.NS.C.7.c', [
              sa('Find the value.\n|-5| + |2|', 'Value:'),
              tf('|-7| = 7'),
              mc('|-3| + |4| = ?', ['7', '1', '-7', '-1']),
              sa('Find the value.\n|-6|', 'Value:'),
              tf('|-2| + |-2| = 0'),
          ]),
          B('Perimeter of polygons', '3.MD.D.8', [
              sa('Find the perimeter of the rectangle.', 'Perimeter:', fig=rect(7, 3, '7 cm', '3 cm')),
              sa('A square has sides of 9 inches.\nWhat is its perimeter?', 'Perimeter:'),
              tf('A rectangle that is 10 m by 4 m has a perimeter of 28 m.'),
              mc('A triangle has sides of 5 cm, 6 cm, and 7 cm.\nWhat is its perimeter?', ['18 cm', '30 cm', '11 cm', '210 cm']),
              sa('A rectangle is 12 ft long and 5 ft wide.\nWhat is its perimeter?', 'Perimeter:'),
          ]),
      ],
      f1=B('Lengths between points with rational coordinates', '7.NS.A.1.c', [
          sa('A side of a polygon goes from (-2.5, 3) to (4, 3).\nHow long is the side?', 'Length:'),
          sa('A rectangle has vertices at (-1.5, 2), (3.5, 2), (3.5, -1), and (-1.5, -1).\nWhat is its perimeter?', 'Perimeter:'),
          mc('How long is the segment from (0, -3{1/2}) to (0, 1{1/4})?', ['4{3/4}', '2{1/4}', '-4{3/4}', '5{1/4}']),
          sa('A square has vertices at (-2.5, -2.5), (2.5, -2.5), (2.5, 2.5), and (-2.5, 2.5).\nWhat is the length of one side?', 'Length:'),
          tf('The segment from (-4.2, 1) to (1.8, 1) is 6 units long.'),
      ]),
      f2=B('Find slanted side lengths with the Pythagorean Theorem', '8.G.B.8', [
          sa('A triangle has vertices at (0, 0), (6, 0), and (6, 8).\nHow long is the slanted side?', 'Length:'),
          sa('Find the length of side AC.', 'AC =', fig=coord(pts=[(-3, -2, 'A', 'sw'), (1, -2, 'B', 'se'), (1, 1, 'C', 'ne')], polys=[[(-3, -2), (1, -2), (1, 1)]])),
          mc('A parallelogram has a side from (1, 1) to (4, 5).\nHow long is that side?', ['5', '7', '25', '3']),
          sa('Find the perimeter of the triangle with vertices (0, 0), (5, 0), and (0, 12).', 'Perimeter:'),
          tf('The side from (-2, 3) to (4, -5) is 10 units long.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.4 nets
    S('6.G.A.4', 'Represent three-dimensional figures using nets',
      main=[
          mc('What three-dimensional figure does the net form?', ['Rectangular prism', 'Cube', 'Triangular prism', 'Square pyramid'], fig=net_prism(4, 3, 2)),
          mc('What three-dimensional figure does the net form?', ['Square pyramid', 'Triangular pyramid', 'Cube', 'Triangular prism'], fig=net_pyramid(6, 5)),
          mc('What three-dimensional figure does the net form?', ['Cube', 'Rectangular prism', 'Square pyramid', 'Triangular prism'], fig=net_prism(3, 3, 3)),
          mc('What three-dimensional figure does the net form?', ['Triangular prism', 'Rectangular prism', 'Triangular pyramid', 'Square pyramid'], fig=net_triprism(3, 4, 5, 6)),
          mc('What three-dimensional figure does the net form?', ['Triangular pyramid', 'Square pyramid', 'Triangular prism', 'Cube'], fig=net_tetra()),
      ],
      back=[
          B('Faces of three-dimensional shapes', '2.G.A.1', [
              sa('How many faces does a cube have?', 'Faces:'),
              mc('How many faces does a rectangular prism have?', ['6', '4', '8', '12']),
              tf('A square pyramid has 5 faces.'),
              sa('How many faces does a triangular prism have?', 'Faces:'),
              mc('How many triangular faces does a square pyramid have?', ['4', '1', '5', '3']),
          ]),
          B('Shapes of faces', '3.G.A.1', [
              mc('What shape are the faces of a cube?', ['Squares', 'Triangles', 'Circles', 'Pentagons']),
              tf('Every square is also a rectangle.'),
              mc('What shape is the base of a square pyramid?', ['Square', 'Triangle', 'Circle', 'Rectangle that is not a square']),
              tf('The two ends of a triangular prism are triangles.'),
              sa('What shape are the side faces of a triangular prism?', 'Shape:'),
          ]),
      ],
      f1=B('Cross sections of three-dimensional figures', '7.G.A.3', [
          mc('A rectangular prism is sliced parallel to its base.\nWhat shape is the cross section?', ['Rectangle', 'Triangle', 'Circle', 'Pentagon']),
          mc('A square pyramid is sliced parallel to its base.\nWhat shape is the cross section?', ['Square', 'Triangle', 'Rectangle that is not a square', 'Circle']),
          sa('A cube is sliced through the middle, parallel to one face.\nWhat shape is the cross section?', 'Shape:'),
          mc('A square pyramid is sliced vertically through its top vertex.\nWhat shape is the cross section?', ['Triangle', 'Square', 'Rectangle', 'Pentagon']),
          tf('A triangular prism sliced parallel to its triangular bases makes a triangle cross section.'),
      ]),
      f2=B('Volume of a cylinder described by its net', '8.G.C.9', [
          sa('A net of a cylinder has two circles with a radius of 3 cm and a rectangle that is 8 cm tall.\nWhat is the volume of the cylinder in terms of π?', 'Volume:'),
          sa('A net of a cylinder has two circles with a radius of 5 in. and a rectangle that is 4 in. tall.\nWhat is the volume in terms of π?', 'Volume:'),
          mc('A net of a cylinder has circles with a diameter of 6 m. The rectangle is 10 m tall.\nWhat is the volume?', ['90π cubic meters', '360π cubic meters', '60π cubic meters', '30π cubic meters']),
          sa('A net of a cylinder has two circles with a radius of 2 ft and a rectangle that is 7 ft tall.\nWhat is the volume? Use 3.14 for π.', 'Volume:'),
          tf('In the net of a cylinder, the height of the rectangle is the height of the cylinder.'),
      ])),

    # ------------------------------------------------------------------ 6.G.A.4 surface area
    S('6.G.A.4', 'Use nets to find surface area',
      main=[
          sa('The net folds into a rectangular prism.\nWhat is the surface area of the prism?', 'Surface area:', fig=net_prism(4, 3, 2, '4 cm', '3 cm', '2 cm')),
          sa('The net folds into a square pyramid.\nWhat is the surface area of the pyramid?', 'Surface area:', fig=net_pyramid(6, 5, '6 m', '5 m')),
          sa('The net folds into a cube.\nWhat is the surface area of the cube?', 'Surface area:', fig=net_prism(5, 5, 5, '5 in.', '5 in.', '5 in.')),
          sa('The net folds into a triangular prism.\nWhat is the surface area of the prism?', 'Surface area:', fig=net_triprism(3, 4, 5, 10, ('3 cm', '4 cm', '5 cm', '10 cm'))),
          sa('The net folds into a rectangular prism.\nWhat is the surface area of the prism?', 'Surface area:', fig=net_prism(6, 2, 3, '6 ft', '2 ft', '3 ft')),
      ],
      back=[
          B('Area of rectangles', '3.MD.C.7.b', [
              sa('Find the area of the rectangle.', 'Area:', fig=rect(4, 2, '4 cm', '2 cm')),
              sa('A rectangle is 5 m by 7 m.\nWhat is its area?', 'Area:'),
              tf('A rectangle that is 3 units by 6 units has an area of 18 square units.'),
              mc('A rectangle is 6 m by 2 m.\nWhat is its area?', ['12 square meters', '8 square meters', '16 square meters', '24 square meters']),
              sa('A square face has 5-inch edges.\nWhat is its area?', 'Area:'),
          ]),
          B('Area of triangles', '6.G.A.1', [
              sa('Find the area of the triangle.', 'Area:', fig=tri(6, 5, 2, '6 m', '5 m')),
              sa('A triangle has a base of 8 cm and a height of 3 cm.\nWhat is its area?', 'Area:'),
              tf('A triangle with a base of 10 and a height of 4 has an area of 40 square units.'),
              mc('A right triangle has legs of 3 cm and 4 cm.\nWhat is its area?', ['6 square cm', '12 square cm', '7 square cm', '10 square cm']),
              sa('Four triangles each have a base of 6 m and a height of 5 m.\nWhat is their total area?', 'Total area:'),
          ]),
          B('Adding the areas of parts', '3.MD.C.7.d', [
              sa('A figure is made of a 4-by-3 rectangle and a 4-by-2 rectangle that do not overlap.\nWhat is its total area?', 'Area:'),
              tf('A figure made of two 5-by-5 squares has an area of 50 square units.'),
              mc('A figure is made of rectangles with areas of 12, 8, and 6 square units.\nWhat is its total area?', ['26 square units', '576 square units', '20 square units', '14 square units']),
              sa('Six squares each have an area of 9 square inches.\nWhat is their total area?', 'Area:'),
              sa('A figure is made of rectangles that are 2 by 6, 2 by 6, and 3 by 6.\nWhat is its total area?', 'Area:'),
          ]),
      ],
      f1=B('Surface area of prisms in real-world problems', '7.G.B.6', [
          sa('A cube has edges of 2.5 cm.\nWhat is its surface area?', 'Surface area:'),
          mc('A rectangular prism is 5 in. by 4 in. by 2.5 in.\nWhat is its surface area?', ['85 square inches', '50 square inches', '42.5 square inches', '65 square inches']),
          sa('A gift box is 8 in. by 6 in. by 4 in.\nHow much wrapping paper covers the box exactly?', 'Paper:'),
          sa('A box with no lid is 10 in. long, 4 in. wide, and 3 in. tall.\nHow much cardboard is needed to make its 5 faces?', 'Cardboard:'),
          tf('The surface area of a prism is the sum of the areas of all of its faces.'),
      ]),
      f2=B('Pythagorean Theorem in three dimensions', '8.G.B.7', [
          sa('The square pyramid has a base edge of 10 cm and a height of 12 cm.\nWhat is its slant height s?', 's =', fig=dict(k='pyramid', b=10, h=12, blab='10 cm', hlab='12 cm', slant='s')),
          sa('A box is 3 in. by 4 in. by 12 in.\nHow long is the longest diagonal from one corner to the opposite corner?', 'Length:'),
          mc('A square pyramid has a base edge of 16 cm and a slant height of 10 cm.\nWhat is its height?', ['6 cm', '8 cm', '12.8 cm', '18.9 cm']),
          sa('A cone has a radius of 5 in. and a slant height of 13 in.\nWhat is its height?', 'Height:'),
          tf('The bottom of a box is 6 in. by 8 in. The diagonal across the bottom is 10 in.'),
      ])),
]
