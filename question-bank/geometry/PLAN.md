# Geometry collection — authoring plan (saved inventory)

This file is the saved plan for building the collection in batches. If work is interrupted, resume from the first set
not yet written, in this order, without renumbering existing sets. The standards inventory (every subskill that MAIN
must cover) is `src/standards.py`; each set lists the subskills it covers with `covers=`.

Set numbers below are the planned numbers (sets are numbered in module order). Backward branches are chosen per set by
diagnostic need; forward branches record a progression type (same-course deepening, cross-standard extension,
later-course extension) and, when needed, NEAREST RELATED.

## Batch 1 — G-CO.A definitions and transformations (`data_co_a.py`)
1. CO.A.1 Precise definitions of angle, circle, line segment
2. CO.A.1 Precise definitions of perpendicular and parallel lines
3. CO.A.2 Transformations as functions (inputs, outputs, preimages)
4. CO.A.2 Compare transformations that preserve distance and angle with those that do not
5. CO.A.3 Symmetries of rectangles, parallelograms, trapezoids
6. CO.A.3 Symmetries of regular polygons
7. CO.A.4 Definitions of reflection and translation
8. CO.A.4 Definition of rotation
9. CO.A.5 Draw the image under a rotation, reflection, or translation
10. CO.A.5 Specify a sequence of transformations carrying one figure onto another

## Batch 2 — G-CO.B rigid motions and congruence (`data_co_b.py`)
11. CO.B.6 Predict the effect of a rigid motion
12. CO.B.6 Decide congruence with rigid motions
13. CO.B.7 Congruent triangles iff corresponding parts congruent
14. CO.B.8 SAS from rigid motions
15. CO.B.8 ASA from rigid motions
16. CO.B.8 SSS from rigid motions

## Batch 3 — G-CO.C proofs (`data_co_c.py`)
17. CO.C.9 Vertical angles   18. CO.C.9 Parallel lines and transversals   19. CO.C.9 Perpendicular bisector theorem (both directions)
20. CO.C.10 Angle sum   21. CO.C.10 Isosceles base angles   22. CO.C.10 Midsegment   23. CO.C.10 Medians concurrent
24. CO.C.11 Opposite sides and angles   25. CO.C.11 Diagonals bisect   26. CO.C.11 Converses   27. CO.C.11 Rectangle diagonals

## Batch 4 — G-CO.D constructions (`data_co_d.py`)
28. Copy a segment   29. Copy an angle   30. Bisect a segment (perpendicular bisector)   31. Bisect an angle
32. Perpendicular through a point   33. Parallel through a point   34. Inscribed equilateral triangle
35. Inscribed square   36. Inscribed regular hexagon

## Batch 5 — G-SRT (`data_srt.py`)
37. SRT.A.1.a Dilations and lines   38. SRT.A.1.b Dilations and lengths   39. SRT.A.2 Decide similarity with transformations
40. SRT.A.2 Meaning of similarity for triangles   41. SRT.A.3 Establish AA   42. SRT.B.4 Triangle proportionality theorem
43. SRT.B.4 Converse   44. SRT.B.4 Pythagorean Theorem by similarity   45. SRT.B.5 Solve with similarity
46. SRT.B.5 Prove with congruence   47. SRT.B.5 Prove with similarity   48. SRT.C.6 Trig ratios from similarity
49. SRT.C.7 Complementary angles   50. SRT.C.8 Unknown sides   51. SRT.C.8 Unknown angles   52. SRT.C.8 Solve right triangles in applications

## Batch 6 — G-C (`data_c.py`)
53. C.A.1 All circles similar   54. C.A.2 Inscribed and central angles   55. C.A.2 Angles on a diameter
56. C.A.2 Radius perpendicular to tangent   57. C.A.2 Circumscribed angles   58. C.A.2 Radii and chords
59. C.A.3 Construct the incircle   60. C.A.3 Construct the circumcircle   61. C.A.3 Inscribed quadrilaterals
62. C.B.5 Arc length and radians   63. C.B.5 Sector area

## Batch 7 — G-GPE (`data_gpe.py`)
64. GPE.A.1 Derive circle equation   65. GPE.A.1 Complete the square   66. GPE.A.2 Parabola from focus and directrix
67. GPE.B.4 Prove quadrilateral type   68. GPE.B.4 Points on circles and other coordinate proofs
69. GPE.B.5 Prove slope criteria   70. GPE.B.5 Parallel and perpendicular line equations   71. GPE.B.5 Geometric problems
72. GPE.B.6 Partition a segment   73. GPE.B.7 Perimeter   74. GPE.B.7 Area

## Batch 8 — G-GMD (`data_gmd.py`)
75. GMD.A.1 Circle circumference and area arguments   76. GMD.A.1 Cylinder volume argument   77. GMD.A.1 Pyramid and cone arguments
78. GMD.A.3 Cylinders, pyramids, cones   79. GMD.A.3 Spheres and composites   80. GMD.A.3 Solve for a dimension
81. GMD.B.4 Cross-sections   82. GMD.B.4 Solids of rotation

## Batch 9 — G-MG (`data_mg.py`)
83. MG.A.1 Model objects   84. MG.A.2 Area density   85. MG.A.2 Volume density   86. MG.A.3 Physical constraints
87. MG.A.3 Minimize cost and typographic grids

## Batch 10 — ADVANCED EXTENSION (+) (`data_adv.py`)
88. SRT.D.9 Area = ½ab sin C   89. SRT.D.10 Prove the Law of Sines   90. SRT.D.10 Prove the Law of Cosines
91. SRT.D.11 Apply the Law of Sines (ambiguous case)   92. SRT.D.11 Apply the Law of Cosines   93. C.A.4 Tangent from an external point
94. GPE.A.3 Ellipse   95. GPE.A.3 Hyperbola   96. GMD.A.2 Cavalieri and the sphere

The plan may grow if a set turns out to mix two distinct demands; new sets take the next free number.
