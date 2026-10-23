"""Geometry standards inventory: every HSG standard, split into the distinct demands (subskills) that MAIN must cover.

Wording follows the Common Core State Standards for Mathematics, High School Geometry (thecorestandards.org/Math/
Content/HSG/). The authoring environment could not open that site (network policy), so the text below was written
from the published standards and should be spot-checked against the official page (see README "Assumptions").

Each subskill ID (for example CO1-angle) must be listed in covers= of at least one MAIN set; the build and
validation script check this. Verbs matter: "prove", "construct", "derive", "explain" subskills need sets whose MAIN
questions require that product, not only recognition.
"""

STANDARDS = {
    # ---------------------------------------------------------------- G-CO Congruence
    'HSG-CO.A.1': ('Know precise definitions of angle, circle, perpendicular line, parallel line, and line segment, based on '
                   'the undefined notions of point, line, distance along a line, and distance around a circular arc.', [
        ('CO1-angle', 'Precise definition of an angle'),
        ('CO1-circle', 'Precise definition of a circle'),
        ('CO1-segment', 'Precise definition of a line segment'),
        ('CO1-perp', 'Precise definition of perpendicular lines'),
        ('CO1-par', 'Precise definition of parallel lines'),
    ]),
    'HSG-CO.A.2': ('Represent transformations in the plane using, e.g., transparencies and geometry software; describe '
                   'transformations as functions that take points in the plane as inputs and give other points as outputs. '
                   'Compare transformations that preserve distance and angle to those that do not (e.g., translation versus '
                   'horizontal stretch).', [
        ('CO2-function', 'Describe and use transformations as functions from points to points (rules, inputs, outputs, preimages)'),
        ('CO2-compare', 'Compare transformations that preserve distance and angle with those that do not'),
    ]),
    'HSG-CO.A.3': ('Given a rectangle, parallelogram, trapezoid, or regular polygon, describe the rotations and reflections '
                   'that carry it onto itself.', [
        ('CO3-quad', 'Rotations and reflections carrying a rectangle, parallelogram, or trapezoid onto itself'),
        ('CO3-regular', 'Rotations and reflections carrying a regular polygon onto itself'),
    ]),
    'HSG-CO.A.4': ('Develop definitions of rotations, reflections, and translations in terms of angles, circles, '
                   'perpendicular lines, parallel lines, and line segments.', [
        ('CO4-reflect', 'Definition of a reflection (perpendicular bisector)'),
        ('CO4-translate', 'Definition of a translation (parallel, congruent, same-direction segments)'),
        ('CO4-rotate', 'Definition of a rotation (center, angle, circles)'),
    ]),
    'HSG-CO.A.5': ('Given a geometric figure and a rotation, reflection, or translation, draw the transformed figure using, '
                   'e.g., graph paper, tracing paper, or geometry software. Specify a sequence of transformations that will '
                   'carry a given figure onto another.', [
        ('CO5-draw', 'Draw the image of a figure under a rotation, reflection, or translation'),
        ('CO5-sequence', 'Specify a sequence of transformations carrying one figure onto another'),
    ]),
    'HSG-CO.B.6': ('Use geometric descriptions of rigid motions to transform figures and to predict the effect of a given '
                   'rigid motion on a given figure; given two figures, use the definition of congruence in terms of rigid '
                   'motions to decide if they are congruent.', [
        ('CO6-predict', 'Predict the effect of a given rigid motion on a figure'),
        ('CO6-decide', 'Decide whether two figures are congruent using the rigid-motion definition'),
    ]),
    'HSG-CO.B.7': ('Use the definition of congruence in terms of rigid motions to show that two triangles are congruent if '
                   'and only if corresponding pairs of sides and corresponding pairs of angles are congruent.', [
        ('CO7-iff', 'Show both directions: a rigid motion gives congruent corresponding parts, and congruent corresponding parts give a rigid motion'),
    ]),
    'HSG-CO.B.8': ('Explain how the criteria for triangle congruence (ASA, SAS, and SSS) follow from the definition of '
                   'congruence in terms of rigid motions.', [
        ('CO8-sas', 'Explain SAS from rigid motions'),
        ('CO8-asa', 'Explain ASA from rigid motions'),
        ('CO8-sss', 'Explain SSS from rigid motions'),
    ]),
    'HSG-CO.C.9': ('Prove theorems about lines and angles. Theorems include: vertical angles are congruent; when a '
                   'transversal crosses parallel lines, alternate interior angles are congruent and corresponding angles '
                   'are congruent; points on a perpendicular bisector of a line segment are exactly those equidistant from '
                   'the segment\'s endpoints.', [
        ('CO9-vertical', 'Prove vertical angles are congruent'),
        ('CO9-parallel', 'Prove alternate interior and corresponding angles are congruent for parallel lines'),
        ('CO9-perpbis', 'Prove the perpendicular bisector theorem in both directions ("exactly those")'),
    ]),
    'HSG-CO.C.10': ('Prove theorems about triangles. Theorems include: measures of interior angles of a triangle sum to '
                    '180°; base angles of isosceles triangles are congruent; the segment joining midpoints of two sides of a '
                    'triangle is parallel to the third side and half the length; the medians of a triangle meet at a point.', [
        ('CO10-sum', 'Prove the triangle angle sum theorem'),
        ('CO10-isosceles', 'Prove base angles of an isosceles triangle are congruent'),
        ('CO10-midseg', 'Prove the midsegment theorem (parallel and half as long)'),
        ('CO10-medians', 'Prove the medians of a triangle meet at a point'),
    ]),
    'HSG-CO.C.11': ('Prove theorems about parallelograms. Theorems include: opposite sides are congruent, opposite angles '
                    'are congruent, the diagonals of a parallelogram bisect each other, and conversely, rectangles are '
                    'parallelograms with congruent diagonals.', [
        ('CO11-opposite', 'Prove opposite sides of a parallelogram are congruent'),
        ('CO11-angles', 'Prove opposite angles of a parallelogram are congruent'),
        ('CO11-diagonals', 'Prove the diagonals of a parallelogram bisect each other'),
        ('CO11-converse', 'Prove the converses (a quadrilateral with these properties is a parallelogram)'),
        ('CO11-rectangle', 'Prove rectangles are parallelograms with congruent diagonals'),
    ]),
    'HSG-CO.D.12': ('Make formal geometric constructions with a variety of tools and methods (compass and straightedge, '
                    'string, reflective devices, paper folding, dynamic geometric software, etc.). Copying a segment; copying '
                    'an angle; bisecting a segment; bisecting an angle; constructing perpendicular lines, including the '
                    'perpendicular bisector of a line segment; and constructing a line parallel to a given line through a '
                    'point not on the line.', [
        ('CO12-copyseg', 'Construct a copy of a segment'),
        ('CO12-copyang', 'Construct a copy of an angle'),
        ('CO12-bisseg', 'Bisect a segment (construct its perpendicular bisector)'),
        ('CO12-bisang', 'Bisect an angle'),
        ('CO12-perp', 'Construct a perpendicular to a line through a point on or off the line'),
        ('CO12-parallel', 'Construct a parallel to a line through a point not on it'),
        ('CO12-tools', 'Use more than one tool or method (paper folding, string, software)'),
    ]),
    'HSG-CO.D.13': ('Construct an equilateral triangle, a square, and a regular hexagon inscribed in a circle.', [
        ('CO13-triangle', 'Construct an equilateral triangle inscribed in a circle'),
        ('CO13-square', 'Construct a square inscribed in a circle'),
        ('CO13-hexagon', 'Construct a regular hexagon inscribed in a circle'),
    ]),
    # ---------------------------------------------------------------- G-SRT
    'HSG-SRT.A.1.a': ('Verify experimentally the properties of dilations given by a center and a scale factor: a dilation '
                      'takes a line not passing through the center of the dilation to a parallel line, and leaves a line '
                      'passing through the center unchanged.', [
        ('SRT1a-lines', 'Verify that a dilation maps a line to a parallel line, or to itself when it passes through the center'),
    ]),
    'HSG-SRT.A.1.b': ('Verify experimentally the properties of dilations given by a center and a scale factor: the dilation '
                      'of a line segment is longer or shorter in the ratio given by the scale factor.', [
        ('SRT1b-length', 'Verify that a dilated segment is k times as long'),
    ]),
    'HSG-SRT.A.2': ('Given two figures, use the definition of similarity in terms of similarity transformations to decide '
                    'if they are similar; explain using similarity transformations the meaning of similarity for triangles '
                    'as the equality of all corresponding pairs of angles and the proportionality of all corresponding pairs '
                    'of sides.', [
        ('SRT2-decide', 'Decide whether two figures are similar using similarity transformations'),
        ('SRT2-meaning', 'Explain similarity for triangles as equal angles and proportional sides'),
    ]),
    'HSG-SRT.A.3': ('Use the properties of similarity transformations to establish the AA criterion for two triangles to be '
                    'similar.', [
        ('SRT3-aa', 'Establish the AA criterion from similarity transformations'),
    ]),
    'HSG-SRT.B.4': ('Prove theorems about triangles. Theorems include: a line parallel to one side of a triangle divides the '
                    'other two proportionally, and conversely; the Pythagorean Theorem proved using triangle similarity.', [
        ('SRT4-prop', 'Prove the triangle proportionality theorem'),
        ('SRT4-converse', 'Prove the converse of the triangle proportionality theorem'),
        ('SRT4-pythag', 'Prove the Pythagorean Theorem using similar triangles'),
    ]),
    'HSG-SRT.B.5': ('Use congruence and similarity criteria for triangles to solve problems and to prove relationships in '
                    'geometric figures.', [
        ('SRT5-solve', 'Solve problems with similarity criteria'),
        ('SRT5-congprove', 'Prove relationships in figures with congruence criteria'),
        ('SRT5-simprove', 'Prove relationships in figures with similarity criteria'),
    ]),
    'HSG-SRT.C.6': ('Understand that by similarity, side ratios in right triangles are properties of the angles in the '
                    'triangle, leading to definitions of trigonometric ratios for acute angles.', [
        ('SRT6-ratios', 'Explain why right-triangle side ratios depend only on the angle; define sine, cosine, and tangent'),
    ]),
    'HSG-SRT.C.7': ('Explain and use the relationship between the sine and cosine of complementary angles.', [
        ('SRT7-comp', 'Explain and use sin θ = cos(90° - θ)'),
    ]),
    'HSG-SRT.C.8': ('Use trigonometric ratios and the Pythagorean Theorem to solve right triangles in applied problems.', [
        ('SRT8-sides', 'Find unknown sides with trigonometric ratios in applied problems'),
        ('SRT8-angles', 'Find unknown angles with inverse trigonometric ratios in applied problems'),
        ('SRT8-solve', 'Solve right triangles completely with trigonometry and the Pythagorean Theorem'),
    ]),
    'HSG-SRT.D.9': ('(+) Derive the formula A = 1/2 ab sin(C) for the area of a triangle by drawing an auxiliary line from a '
                    'vertex perpendicular to the opposite side.', [
        ('SRT9-derive', 'Derive A = ½ab sin C and use it'),
    ]),
    'HSG-SRT.D.10': ('(+) Prove the Laws of Sines and Cosines and use them to solve problems.', [
        ('SRT10-sines', 'Prove the Law of Sines'),
        ('SRT10-cosines', 'Prove the Law of Cosines'),
    ]),
    'HSG-SRT.D.11': ('(+) Understand and apply the Law of Sines and the Law of Cosines to find unknown measurements in right '
                     'and non-right triangles (e.g., surveying problems, resultant forces).', [
        ('SRT11-sines', 'Apply the Law of Sines, including the ambiguous case'),
        ('SRT11-cosines', 'Apply the Law of Cosines, including resultant forces'),
    ]),
    # ---------------------------------------------------------------- G-C
    'HSG-C.A.1': ('Prove that all circles are similar.', [
        ('C1-similar', 'Prove that any two circles are similar'),
    ]),
    'HSG-C.A.2': ('Identify and describe relationships among inscribed angles, radii, and chords. Include the relationship '
                  'between central, inscribed, and circumscribed angles; inscribed angles on a diameter are right angles; the '
                  'radius of a circle is perpendicular to the tangent where the radius intersects the circle.', [
        ('C2-inscribed', 'Relationship between central and inscribed angles'),
        ('C2-diameter', 'Inscribed angles on a diameter are right angles'),
        ('C2-tangent', 'A radius is perpendicular to the tangent at the point of tangency'),
        ('C2-circumscribed', 'Relationship between circumscribed and central angles'),
        ('C2-chords', 'Relationships among radii and chords'),
    ]),
    'HSG-C.A.3': ('Construct the inscribed and circumscribed circles of a triangle, and prove properties of angles for a '
                  'quadrilateral inscribed in a circle.', [
        ('C3-incircle', 'Construct the inscribed circle of a triangle'),
        ('C3-circumcircle', 'Construct the circumscribed circle of a triangle'),
        ('C3-cyclic', 'Prove that opposite angles of an inscribed quadrilateral are supplementary'),
    ]),
    'HSG-C.A.4': ('(+) Construct a tangent line from a point outside a given circle to the circle.', [
        ('C4-tangent', 'Construct a tangent from an external point'),
    ]),
    'HSG-C.B.5': ('Derive using similarity the fact that the length of the arc intercepted by an angle is proportional to the '
                  'radius, and define the radian measure of the angle as the constant of proportionality; derive the formula '
                  'for the area of a sector.', [
        ('C5-arc', 'Derive arc length proportional to radius; define radian measure'),
        ('C5-sector', 'Derive and use the area of a sector'),
    ]),
    # ---------------------------------------------------------------- G-GPE
    'HSG-GPE.A.1': ('Derive the equation of a circle of given center and radius using the Pythagorean Theorem; complete the '
                    'square to find the center and radius of a circle given by an equation.', [
        ('GPE1-derive', 'Derive the equation of a circle from its center and radius'),
        ('GPE1-complete', 'Complete the square to find the center and radius'),
    ]),
    'HSG-GPE.A.2': ('Derive the equation of a parabola given a focus and directrix.', [
        ('GPE2-parabola', 'Derive the equation of a parabola from its focus and directrix'),
    ]),
    'HSG-GPE.A.3': ('(+) Derive the equations of ellipses and hyperbolas given the foci, using the fact that the sum or '
                    'difference of distances from the foci is constant.', [
        ('GPE3-ellipse', 'Derive the equation of an ellipse from its foci'),
        ('GPE3-hyperbola', 'Derive the equation of a hyperbola from its foci'),
    ]),
    'HSG-GPE.B.4': ('Use coordinates to prove simple geometric theorems algebraically. For example, prove or disprove that a '
                    'figure defined by four given points in the coordinate plane is a rectangle; prove or disprove that the '
                    'point (1, √3) lies on the circle centered at the origin and containing the point (0, 2).', [
        ('GPE4-quad', 'Prove or disprove the type of a quadrilateral from its vertices'),
        ('GPE4-circle', 'Prove or disprove that a point lies on a circle, and other coordinate proofs'),
    ]),
    'HSG-GPE.B.5': ('Prove the slope criteria for parallel and perpendicular lines and use them to solve geometric problems '
                    '(e.g., find the equation of a line parallel or perpendicular to a given line that passes through a given '
                    'point).', [
        ('GPE5-prove', 'Prove the slope criteria for parallel and perpendicular lines'),
        ('GPE5-equation', 'Write equations of parallel and perpendicular lines through a point'),
        ('GPE5-problems', 'Use the slope criteria to solve geometric problems'),
    ]),
    'HSG-GPE.B.6': ('Find the point on a directed line segment between two given points that partitions the segment in a '
                    'given ratio.', [
        ('GPE6-partition', 'Partition a directed segment in a given ratio'),
    ]),
    'HSG-GPE.B.7': ('Use coordinates to compute perimeters of polygons and areas of triangles and rectangles, e.g., using '
                    'the distance formula.', [
        ('GPE7-perimeter', 'Compute perimeters of polygons from coordinates'),
        ('GPE7-area', 'Compute areas of triangles and rectangles from coordinates'),
    ]),
    # ---------------------------------------------------------------- G-GMD
    'HSG-GMD.A.1': ('Give an informal argument for the formulas for the circumference of a circle, area of a circle, volume '
                    'of a cylinder, pyramid, and cone. Use dissection arguments, Cavalieri\'s principle, and informal limit '
                    'arguments.', [
        ('GMD1-circle', 'Informal argument for the circumference of a circle'),
        ('GMD1-area', 'Informal argument for the area of a circle'),
        ('GMD1-cylinder', 'Informal argument for the volume of a cylinder'),
        ('GMD1-pyramid', 'Informal argument for the volume of a pyramid'),
        ('GMD1-cone', 'Informal argument for the volume of a cone'),
    ]),
    'HSG-GMD.A.2': ('(+) Give an informal argument using Cavalieri\'s principle for the formulas for the volume of a sphere '
                    'and other solid figures.', [
        ('GMD2-sphere', 'Cavalieri argument for the volume of a sphere and other solids'),
    ]),
    'HSG-GMD.A.3': ('Use volume formulas for cylinders, pyramids, cones, and spheres to solve problems.', [
        ('GMD3-cpc', 'Use volume formulas for cylinders, pyramids, and cones'),
        ('GMD3-sphere', 'Use the sphere volume formula, including composite solids'),
        ('GMD3-solve', 'Solve for an unknown dimension from a volume'),
    ]),
    'HSG-GMD.B.4': ('Identify the shapes of two-dimensional cross-sections of three-dimensional objects, and identify '
                    'three-dimensional objects generated by rotations of two-dimensional objects.', [
        ('GMD4-cross', 'Identify cross-sections of solids'),
        ('GMD4-rotate', 'Identify solids generated by rotating plane figures'),
    ]),
    # ---------------------------------------------------------------- G-MG
    'HSG-MG.A.1': ('Use geometric shapes, their measures, and their properties to describe objects (e.g., modeling a tree '
                   'trunk or a human torso as a cylinder).', [
        ('MG1-model', 'Model objects with geometric shapes and use their measures'),
    ]),
    'HSG-MG.A.2': ('Apply concepts of density based on area and volume in modeling situations (e.g., persons per square mile, '
                   'BTUs per cubic foot).', [
        ('MG2-area', 'Density based on area'),
        ('MG2-volume', 'Density based on volume'),
    ]),
    'HSG-MG.A.3': ('Apply geometric methods to solve design problems (e.g., designing an object or structure to satisfy '
                   'physical constraints or minimize cost; working with typographic grid systems based on ratios).', [
        ('MG3-constraints', 'Design to satisfy physical constraints'),
        ('MG3-cost', 'Design to minimize cost'),
        ('MG3-grid', 'Typographic grid systems based on ratios'),
    ]),
}

PLUS = {'HSG-SRT.D.9', 'HSG-SRT.D.10', 'HSG-SRT.D.11', 'HSG-C.A.4', 'HSG-GPE.A.3', 'HSG-GMD.A.2'}


def subskills():
    """[(code, subskill_id, description)] in inventory order."""
    return [(code, sid, d) for code, (_, subs) in STANDARDS.items() for sid, d in subs]
