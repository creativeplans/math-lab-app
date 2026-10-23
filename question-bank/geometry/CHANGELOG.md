# Geometry question collection — change log

Version 1.1.0 (previous 1.0.0, commit 3ba23bb). One row per question ID that changed. Unchanged IDs are omitted; the full map, including unchanged IDs, is `revisions.json` in the import package.

| Status | Count |
|---|---:|
| unchanged | 2480 |
| revised | 410 |
| retired | 25 |
| new | 270 |

Rules: IDs of corrected questions are kept (status revised). An ID whose skill or standard changes is retired and never reused; the replacement questions get new IDs (status new). Sets added after publication take the next free set number; branches added to an existing set take the next free branch number. Numbers need not be consecutive.

## Review findings

| Code | Finding |
|---|---|
| R01 | Each distinct subskill has its own focused set; the subskill matrix is rebuilt from the actual question mapping (splits S1/S97/S98, S2/S99, S7/S100, S24/S101, S28/S102, S75/S103, S77/S104, S87/S105) |
| R02 | All five MAIN questions are comparable full performances: proofs in proof sets, constructions with evidence in construction sets, derivations or informal arguments in derive/explain sets; true/false items removed from every MAIN |
| R03 | Forward branches audited for focus and one new demand; duplicated or off-demand forward items replaced (S4-F2, S12-F1-Q4, S29-F1, S34-F1, S73-F1, S100-F2-Q3, and others) |
| R04 | Every question states its own givens (points on sides, right angles, tangency, heights, radii, models) instead of relying on a figure or an earlier question |
| R05 | No circular dependencies: SSS (S16) is justified with SAS and an angle bisector, not the perpendicular-bisector converse; S18 establishes corresponding angles by a translation before the other angle-pair theorems |
| R06 | S37 and S38 MAIN are five comparable experimental verifications with different centers, factors and line positions, each stating that examples are evidence, not proof |
| R07 | S68-M-Q1 uses original data (center (2, -1), points (2, 4) and (5, 3)) instead of the official example (1, √3); its prerequisite item changed to match |
| R08 | Exporter crop fixed for coordinate figures whose point list is empty (segments given by coordinates); all such SVG/PNG assets re-rendered and checked |
| R09 | S11-F1-Q2 states rotation directions (70° counterclockwise then 50° clockwise) |
| R10 | S37 dilation items about lines use scale factors k ≠ 1 |
| R11 | S38-F1-Q3 restricts to points other than the center and a dilation with k ≠ 1 |
| R12 | Rotation items require P ≠ center (S8-M-Q4) and a point P different from the center O (S82-B1-Q1) |
| R13 | S16-B2-Q2 says "in a given plane" |
| R14 | Domain assumptions stated: a > 0 and c ≠ 0 (S22-M-Q4, S67-F1-Q2), a ≠ 0 (S22-B2-Q2), P ≠ M (S14-F1-Q2), nonzero values before reciprocals (S42-B3-Q1) |
| R15 | S20-B3-Q3 names a labeled angle |
| R16 | S44-M-Q4 defines x = AD, y = DB with AC = 6 and BC = 8 |
| R17 | Inscribed-angle items use the intercepted arc and state the reflex/major-arc convention (S54-F1-Q1/Q2, S54-F2-Q2/Q3) |
| R18 | S56-M-Q4: "T lies on circle O and P is outside it"; the key concludes "not tangent" |
| R19 | S66-F1-Q3 uses |p| for the focus-vertex distance |
| R20 | S73-B2-Q4 uses the absolute value of the difference |
| R21 | S82-F2 rotation axes are in the rectangle's plane, parallel to a side, and outside the rectangle |
| R22 | S83-F2-Q1 key is 1,380 kg (2.3 m³ × 600 kg/m³) |
| R23 | S84-F2-Q2 asks for the smallest whole number of m² that meets the limit (3,334) |
| R24 | S87-F2-Q2 gives a baseline (a standard metal that never fails) and asks when the expected cost is strictly lower |
| R25 | S77-M-Q1 requires the general pyramid argument (vertical scaling and Cavalieri's principle), not only the cube dissection |
| R26 | Altitude derivations cover acute and obtuse cases (S88-M-Q1, S88-M-Q5, S89-M-Q3/Q5, S89-B1-Q2, S90-M-Q3) |
| R27 | Rounded answers state the precision in the student text (S50-B2-Q2 nearest hundredth, 17.86; bank-wide audit) |
| R28 | Constraint answers round in the direction that keeps the design compliant (S50-F2-Q5 12.0 ft, S50-F2-Q2 16.4 m, S50-F2-Q1/Q4, S80-F1-Q1/Q2, S80-F2-Q2) |
| R29 | S32-F2-Q1/Q2 put the points on the same side of AB |
| R30 | S33-B3-Q5 says the point is not on the line |
| R31 | S28-B3-Q2 lists three cases |
| R32 | The standalone answer-key JSON/CSV carry each question's figure asset paths, description and data by UID (existing fields unchanged) |
| R33 | VALIDATION.md reports each check with its actual scope and evidence; a solved-question log and recalculated totals are included |
| N01 | S1-M-Q1 wording and positive radius |
| N02 | S5-M-Q3 states the trapezoid convention and the rotation range |
| N03 | S7-B2-Q1/Q4 wording on perpendicular lines |
| N04 | S15-F1-Q3 asks how AAS follows from ASA |
| N05 | S20-M-Q5 restated |
| N06 | S35-B2-Q2: "kite that is not a rhombus", most specific name |
| N07 | S58-B2-Q4: two chords that are not parallel (distinct perpendicular bisectors) |
| N08 | S62-F2-Q2: a wheel rotating about a fixed center |
| N09 | S87-F1-Q1/Q3: closed boxes, material thickness ignored |
| N10 | S95-F2-Q3/Q5: a nonzero signed time difference; the extra measurement needed |
| N11 | Noncollinearity assumptions stated where a triangle or circle needs them |
| N12 | Precision or exact form stated in the student text, not only in the grading note |
| N13 | Figure corrected to match its description (S60-M-Q2 triangle is now obtuse at C) |
| N14 | Branch or set title edited after a split; the questions are unchanged |

## ID map

Questions that moved keep their content under a new ID; the old ID is retired or now holds the corrected question for the narrower skill, as the Status column says.

| Old ID | New ID | Old ID status |
|---|---|---|
| S1-B1-Q1 | S97-B1-Q1 | retired |
| S1-B1-Q2 | S97-B1-Q2 | retired |
| S1-B1-Q3 | S97-B1-Q3 | retired |
| S1-B1-Q4 | S97-B1-Q4 | retired |
| S1-B1-Q5 | S97-B1-Q5 | retired |
| S1-B2-Q1 | S98-B1-Q1 | retired |
| S1-B2-Q2 | S98-B1-Q2 | retired |
| S1-B2-Q3 | S98-B1-Q3 | retired |
| S1-B2-Q4 | S98-B1-Q4 | retired |
| S1-B2-Q5 | S98-B1-Q5 | retired |
| S75-M-Q1 | S103-M-Q1 | revised |
| S75-B2-Q1 | S103-B2-Q1 | retired |
| S75-B2-Q2 | S103-B2-Q2 | retired |
| S75-B2-Q3 | S103-B2-Q3 | retired |
| S75-B2-Q4 | S103-B2-Q4 | retired |
| S75-B2-Q5 | S103-B2-Q5 | retired |
| S75-F1-Q1 | S103-F1-Q1 | revised |
| S75-F1-Q2 | S103-F1-Q2 | revised |
| S75-F1-Q3 | S103-F1-Q3 | revised |
| S75-F1-Q4 | S103-F1-Q4 | revised |
| S75-F1-Q5 | S103-F1-Q5 | revised |
| S75-F2-Q1 | S103-F2-Q1 | revised |
| S75-F2-Q2 | S103-F2-Q2 | revised |
| S75-F2-Q3 | S103-F2-Q3 | revised |
| S75-F2-Q4 | S103-F2-Q4 | revised |
| S75-F2-Q5 | S103-F2-Q5 | revised |
| S77-M-Q2 | S104-M-Q1 | revised |
| S77-B3-Q1 | S104-B2-Q1 | retired |
| S77-B3-Q2 | S104-B2-Q2 | retired |
| S77-B3-Q3 | S104-B2-Q3 | retired |
| S77-B3-Q4 | S104-B2-Q4 | retired |
| S77-B3-Q5 | S104-B2-Q5 | retired |
| S87-M-Q4 | S105-M-Q1 | revised |
| S87-M-Q5 | S105-M-Q2 | revised |
| S87-F1-Q2 | S105-M-Q3 | revised |
| S87-B2-Q1 | S105-B1-Q1 | retired |
| S87-B2-Q2 | S105-B1-Q2 | retired |
| S87-B2-Q3 | S105-B1-Q3 | retired |
| S87-B2-Q4 | S105-B1-Q4 | retired |
| S87-B2-Q5 | S105-B1-Q5 | retired |
| S87-F1-Q4 | S105-F1-Q1 | revised |
| S87-F1-Q5 | S105-F1-Q2 | revised |

Retired backward branches and their replacements:

| Retired branch | Replacement branch |
|---|---|

## Changes by question ID

| ID | Status | Findings | What changed | Reason |
|---|---|---|---|---|
| S1-M-Q1 | revised | R01 | prompt, correct_answer, grading_note, skill | Circle-only MAIN: all five items write or repair a circle definition (positive radius, one plane). |
| S1-M-Q2 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Circle-only MAIN: all five items write or repair a circle definition (positive radius, one plane). |
| S1-M-Q3 | revised | R01 | prompt, correct_answer, grading_note, skill | Circle-only MAIN: all five items write or repair a circle definition (positive radius, one plane). |
| S1-M-Q4 | revised | R01 | correct_answer, skill | Circle-only MAIN: all five items write or repair a circle definition (positive radius, one plane). |
| S1-M-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Circle-only MAIN: all five items write or repair a circle definition (positive radius, one plane). |
| S1-B1-Q1 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B1-Q2 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B1-Q3 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B1-Q4 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B1-Q5 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B2-Q1 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B2-Q2 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B2-Q3 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B2-Q4 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B2-Q5 | retired | R01 |  | Angle and segment prerequisites moved with their subskills to S97 and S98. |
| S1-B4-Q1 | new | R01 |  | New prerequisite branch (distance in the plane) for the circle-only set. |
| S1-B4-Q2 | new | R01 |  | New prerequisite branch (distance in the plane) for the circle-only set. |
| S1-B4-Q3 | new | R01 |  | New prerequisite branch (distance in the plane) for the circle-only set. |
| S1-B4-Q4 | new | R01 |  | New prerequisite branch (distance in the plane) for the circle-only set. |
| S1-B4-Q5 | new | R01 |  | New prerequisite branch (distance in the plane) for the circle-only set. |
| S1-F1-Q1 | revised | R01 | skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F1-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F1-Q3 | revised | R01 | skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F1-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F1-Q5 | revised | R01 | skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F2-Q1 | revised | R01 | prompt, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F2-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F2-Q3 | revised | R01 | skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F2-Q4 | revised | R01 | prompt, choices, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S1-F2-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Forward branches now extend the circle subskill only (counterexamples and definitions of circle parts). |
| S2-M-Q1 | revised | R01 | prompt, correct_answer, grading_note, skill | Perpendicular-lines-only MAIN; parallel lines moved to S99. |
| S2-M-Q2 | revised | R01 | skill | Perpendicular-lines-only MAIN; parallel lines moved to S99. |
| S2-M-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Perpendicular-lines-only MAIN; parallel lines moved to S99. |
| S2-M-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Perpendicular-lines-only MAIN; parallel lines moved to S99. |
| S2-M-Q5 | revised | R01 | skill | Perpendicular-lines-only MAIN; parallel lines moved to S99. |
| S2-B1-Q1 | revised | N14 | skill | Branch title edited for the perpendicular-only set; questions unchanged. |
| S2-B1-Q2 | revised | N14 | skill | Branch title edited for the perpendicular-only set; questions unchanged. |
| S2-B1-Q3 | revised | N14 | skill | Branch title edited for the perpendicular-only set; questions unchanged. |
| S2-B1-Q4 | revised | N14 | prompt, choices, correct_answer, grading_note, skill | Branch title edited for the perpendicular-only set; questions unchanged. |
| S2-B1-Q5 | revised | N14 | skill | Branch title edited for the perpendicular-only set; questions unchanged. |
| S2-F1-Q3 | revised | R03 | prompt, correct_answer, grading_note | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F1-Q4 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F1-Q5 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F2-Q1 | revised | R03 | skill, required_method | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F2-Q2 | revised | R03 | skill | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F2-Q3 | revised | R03 | skill | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F2-Q4 | revised | R03 | skill | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S2-F2-Q5 | revised | R03 | prompt, grading_note, skill | Forward items refocused on perpendicular lines with one new demand (explanations; exactly one perpendicular through a point on a line). |
| S3-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | True/false item replaced by a short-answer item about the fixed point. |
| S4-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | True/false item replaced by a short-answer item about V and angles. |
| S4-F2-Q5 | revised | R03 | prompt, correct_letter, correct_answer, grading_note | Duplicate replaced: "preserves every distance implies preserves angles". |
| S5-M-Q2 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Items now list all symmetries with coordinates (comparable full tasks). |
| S5-M-Q3 | revised | N02 | prompt | Trapezoid convention and rotation range (greater than 0° and at most 360°) stated. |
| S5-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Items now list all symmetries with coordinates (comparable full tasks). |
| S5-M-Q5 | revised | N02 | prompt | Trapezoid convention and rotation range (greater than 0° and at most 360°) stated. |
| S6-M-Q3 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Octagon rotations and nonagon reflections as full short-answer tasks. |
| S6-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Octagon rotations and nonagon reflections as full short-answer tasks. |
| S7-M-Q1 | revised | R01 | skill | Reflection-only MAIN; translations moved to S100. |
| S7-M-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Reflection-only MAIN; translations moved to S100. |
| S7-M-Q3 | revised | R01 | skill | Reflection-only MAIN; translations moved to S100. |
| S7-M-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Reflection-only MAIN; translations moved to S100. |
| S7-M-Q5 | revised | R01 | skill | Reflection-only MAIN; translations moved to S100. |
| S7-B2-Q1 | revised | N03 | prompt, skill | Perpendicular-lines prerequisite reworded. |
| S7-B2-Q2 | revised | N03 | prompt, skill | Perpendicular-lines prerequisite reworded. |
| S7-B2-Q3 | revised | N03 | prompt, choices, correct_answer, grading_note, skill | Perpendicular-lines prerequisite reworded. |
| S7-B2-Q4 | revised | N03 | prompt, skill | Perpendicular-lines prerequisite reworded. |
| S7-B2-Q5 | revised | N03 | choices, correct_answer, skill | Perpendicular-lines prerequisite reworded. |
| S7-B3-Q1 | revised | R01 | skill | Prerequisite now about reflections only. |
| S7-B3-Q2 | revised | R01 | prompt, correct_answer, skill | Prerequisite now about reflections only. |
| S7-B3-Q3 | revised | R01 | skill | Prerequisite now about reflections only. |
| S7-B3-Q4 | revised | R01 | skill | Prerequisite now about reflections only. |
| S7-B3-Q5 | revised | R01 | prompt, grading_note, skill | Prerequisite now about reflections only. |
| S7-F1-Q2 | revised | R01 | prompt, correct_answer, grading_note | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S7-F2-Q1 | revised | R01 | skill | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S7-F2-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill, required_method | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S7-F2-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S7-F2-Q4 | revised | R01 | skill | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S7-F2-Q5 | revised | R01 | skill | Forward items are reflection items and reflection proofs (P on ℓ; x-axis coordinate proof). |
| S8-M-Q4 | revised | R12 | type, prompt, choices, correct_letter, correct_answer, grading_note | Short-answer item with P ≠ O and a 70° rotation. |
| S9-F2-Q4 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Construction items (180° rotation about O; translation by a parallelogram) give the branch its new demand. |
| S9-F2-Q5 | revised | R03 | type, prompt, correct_answer, grading_note, figure | Construction items (180° rotation about O; translation by a parallelogram) give the branch its new demand. |
| S10-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | True/false replaced by a coordinate item with an orientation reason. |
| S11-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Short-answer item on orientation. |
| S11-F1-Q2 | revised | R09 | prompt, correct_answer, grading_note | Rotation directions stated: 70° counterclockwise then 50° clockwise, 20° counterclockwise. |
| S12-M-Q3 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Coordinate rotation-plus-translation item and a quadrilateral item replace selected-response items. |
| S12-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Coordinate rotation-plus-translation item and a quadrilateral item replace selected-response items. |
| S12-F1-Q4 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note | Replaced by a sector congruence item (new demand). |
| S13-M-Q3 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Full tasks: 90° rotation coordinate check, converse with coordinates, AAA counterexample. |
| S13-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Full tasks: 90° rotation coordinate check, converse with coordinates, AAA counterexample. |
| S13-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Full tasks: 90° rotation coordinate check, converse with coordinates, AAA counterexample. |
| S14-M-Q2 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable SAS proofs (mirror image, coordinates, kite reflection, 180° rotation). |
| S14-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable SAS proofs (mirror image, coordinates, kite reflection, 180° rotation). |
| S14-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable SAS proofs (mirror image, coordinates, kite reflection, 180° rotation). |
| S14-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable SAS proofs (mirror image, coordinates, kite reflection, 180° rotation). |
| S14-F1-Q2 | revised | R14 | prompt | P ≠ M stated. |
| S15-M-Q2 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable ASA proofs. |
| S15-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable ASA proofs. |
| S15-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable ASA proofs. |
| S15-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable ASA proofs. |
| S15-F1-Q3 | revised | N04 | type, prompt, choices, correct_letter, correct_answer, grading_note | Asks how AAS follows from ASA. |
| S16-M-Q1 | revised | R05 | grading_note | Rubric requires step 3 by SAS with the angle bisector (or coordinates), not SSS or the perpendicular-bisector converse. |
| S16-M-Q2 | revised | R04 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Full proof with local givens. |
| S16-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Comparable SSS proofs (coordinates, kite, two circles). |
| S16-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Comparable SSS proofs (coordinates, kite, two circles). |
| S16-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Comparable SSS proofs (coordinates, kite, two circles). |
| S16-B2-Q2 | revised | R13 | prompt, grading_note | "In a given plane containing A" added. |
| S17-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Proofs replace computations. |
| S17-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs replace computations. |
| S18-M-Q1 | revised | R05 | prompt, correct_answer, grading_note, required_method | Reordered: corresponding angles by a translation first; alternate interior, alternate exterior, same-side interior follow; 180° rotation proof. |
| S18-M-Q2 | revised | R05 | prompt, correct_answer, grading_note, required_method | Reordered: corresponding angles by a translation first; alternate interior, alternate exterior, same-side interior follow; 180° rotation proof. |
| S18-M-Q3 | revised | R05 | prompt, correct_answer, grading_note, required_method | Reordered: corresponding angles by a translation first; alternate interior, alternate exterior, same-side interior follow; 180° rotation proof. |
| S18-M-Q4 | revised | R05 | type, prompt, correct_answer, grading_note, required_method | Reordered: corresponding angles by a translation first; alternate interior, alternate exterior, same-side interior follow; 180° rotation proof. |
| S18-M-Q5 | revised | R05 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure, required_method | Reordered: corresponding angles by a translation first; alternate interior, alternate exterior, same-side interior follow; 180° rotation proof. |
| S19-M-Q2 | revised | R05 | grading_note | SSS use explained as non-circular; converse proved with SAS and the angle bisector. |
| S19-M-Q3 | revised | R05 | type, prompt, correct_answer, grading_note, required_method | SSS use explained as non-circular; converse proved with SAS and the angle bisector. |
| S19-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Coordinate proof. |
| S19-F2-Q4 | revised | N11 | prompt | Towns not on one straight line. |
| S20-M-Q1 | revised | R05 | grading_note | Rubric states the dependency of the exterior-angle argument. |
| S20-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Translation proof. |
| S20-M-Q5 | revised | N05 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Restated as the PQR / ray QT proof. |
| S20-B3-Q3 | revised | R15 | prompt, choices, correct_answer, grading_note | Uses labeled ∠DCA. |
| S21-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Reflection proof with coordinates. |
| S22-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Midsegment proofs (midpoints F and E; general coordinates). |
| S22-M-Q4 | revised | R14 | type, prompt, correct_answer, grading_note, required_method | a > 0 and c ≠ 0 stated; synthetic proof with point G. |
| S22-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Midsegment proofs (midpoints F and E; general coordinates). |
| S22-B2-Q2 | revised | R14 | prompt, grading_note | a ≠ 0 stated. |
| S23-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Coordinate proofs (A(-2a, 0), B(2a, 0), C(0, 2b); general centroid). |
| S23-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Coordinate proofs (A(-2a, 0), B(2a, 0), C(0, 2b); general centroid). |
| S24-M-Q1 | revised | R01 | skill | Opposite-sides-only MAIN; opposite angles moved to S101. |
| S24-M-Q2 | revised | R01 | prompt, correct_answer, grading_note, figure, skill, required_method | Opposite-sides-only MAIN; opposite angles moved to S101. |
| S24-M-Q3 | revised | R01 | prompt, correct_answer, grading_note, figure, skill, required_method | Opposite-sides-only MAIN; opposite angles moved to S101. |
| S24-M-Q4 | revised | R01 | type, prompt, correct_answer, grading_note, skill, required_method | Opposite-sides-only MAIN; opposite angles moved to S101. |
| S24-M-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Opposite-sides-only MAIN; opposite angles moved to S101. |
| S24-B1-Q1 | revised | N14 | skill | Branch title edited after the split; questions unchanged. |
| S24-B1-Q2 | revised | N14 | prompt, grading_note, skill | Branch title edited after the split; questions unchanged. |
| S24-B1-Q3 | revised | N14 | prompt, choices, correct_answer, grading_note, skill | Branch title edited after the split; questions unchanged. |
| S24-B1-Q4 | revised | N14 | prompt, correct_answer, skill | Branch title edited after the split; questions unchanged. |
| S24-B1-Q5 | revised | N14 | skill | Branch title edited after the split; questions unchanged. |
| S24-B3-Q2 | revised | R01 | choices | Prerequisite items refocused on opposite sides. |
| S24-B3-Q5 | revised | R01 | prompt, correct_answer, grading_note | Prerequisite items refocused on opposite sides. |
| S24-F1-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F1-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F1-Q5 | revised | R01 | prompt, correct_answer, grading_note | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F2-Q1 | revised | R01 | type, prompt, correct_answer, grading_note, skill, required_method | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F2-Q2 | revised | R01 | skill | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F2-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F2-Q4 | revised | R01 | skill | New forward branches: rhombus (F1) and coordinates (F2). |
| S24-F2-Q5 | revised | R01 | skill | New forward branches: rhombus (F1) and coordinates (F2). |
| S25-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Proofs (△AED and △CEB; rotation proof for WXYZ). |
| S25-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs (△AED and △CEB; rotation proof for WXYZ). |
| S25-F1-Q3 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note | True/false replaced by an explanation of the 180° rotation. |
| S26-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Supplementary-angles proof. |
| S27-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Proofs: four right angles; bisecting congruent diagonals. |
| S27-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs: four right angles; bisecting congruent diagonals. |
| S28-M-Q4 | revised | R01 | type, prompt, correct_answer, grading_note, figure | Copy-a-segment constructions (XZ = AB + CD; isosceles triangle); tool methods moved to S102. |
| S28-M-Q5 | revised | R01 | type, prompt, correct_answer, grading_note, figure | Copy-a-segment constructions (XZ = AB + CD; isosceles triangle); tool methods moved to S102. |
| S28-B3-Q2 | revised | R31 | prompt, correct_answer, grading_note | Three cases listed. |
| S29-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions with evidence (copy opening below; triangle with ∠K and segments s, t). |
| S29-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Constructions with evidence (copy opening below; triangle with ∠K and segments s, t). |
| S29-B2-Q1 | revised | R04 | prompt, correct_answer | Restated with its own givens. |
| S29-F1-Q2 | revised | R03 | type, prompt, correct_answer, grading_note, required_method | Justification items (new demand). |
| S29-F1-Q3 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Justification items (new demand). |
| S29-F1-Q4 | revised | R04 | type, prompt, choices, correct_letter, correct_answer, grading_note | Justification item with local givens. |
| S29-F1-Q5 | revised | R03 | type, prompt, correct_answer, grading_note, required_method | Justification items (new demand). |
| S30-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (vertical segment UV; divide a segment into four). |
| S30-M-Q5 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (vertical segment UV; divide a segment into four). |
| S31-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (narrow angle KLM; quarter angle). |
| S31-M-Q5 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (narrow angle KLM; quarter angle). |
| S31-B2-Q3 | revised | R04 | prompt | Construction context restated in the item. |
| S31-B2-Q4 | revised | R04 | prompt | Construction context restated in the item. |
| S32-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (perpendicular at P on slanted m; right triangle). |
| S32-M-Q5 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (perpendicular at P on slanted m; right triangle). |
| S32-F2-Q1 | revised | R29 | prompt, correct_answer, grading_note | Same side of AB. |
| S32-F2-Q2 | revised | R29 | prompt, correct_answer, grading_note | Same side of AB. |
| S33-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (alternate interior angle copy; parallelogram). |
| S33-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Constructions (alternate interior angle copy; parallelogram). |
| S33-B3-Q5 | revised | R30 | prompt | Point not on the line. |
| S34-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (vertex at T; unmarked center). |
| S34-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Constructions (vertex at T; unmarked center). |
| S34-F1-Q2 | revised | R03 | type, prompt, correct_answer, grading_note, required_method | Justification items (new demand). |
| S34-F1-Q3 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Justification items (new demand). |
| S34-F1-Q4 | revised | R03 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Justification items (new demand). |
| S34-F1-Q5 | revised | R03 | prompt, correct_answer, grading_note | Justification items (new demand). |
| S35-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (unmarked center; diagonal on line k). |
| S35-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Constructions (unmarked center; diagonal on line k). |
| S35-B2-Q2 | revised | N06 | prompt, choices, grading_note | Kite that is not a rhombus; most specific name. |
| S36-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Constructions (vertex at T; unmarked center). |
| S36-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Constructions (vertex at T; unmarked center). |
| S36-F2-Q2 | revised | R27 | prompt, grading_note | Perimeter 6.212 and "to the nearest hundredth" stated. |
| S37-M-Q1 | revised | R06 | prompt, correct_answer, grading_note | Five comparable verifications with different centers ((0, 0), (0, 2), (2, 1), (1, 2)), factors (3, 2, ½, 3, 4; k ≠ 1) and line positions, each with evidence-versus-proof language (R10). |
| S37-M-Q2 | revised | R06 | prompt, correct_answer, grading_note | Five comparable verifications with different centers ((0, 0), (0, 2), (2, 1), (1, 2)), factors (3, 2, ½, 3, 4; k ≠ 1) and line positions, each with evidence-versus-proof language (R10). |
| S37-M-Q3 | revised | R06 | prompt, correct_answer, grading_note | Five comparable verifications with different centers ((0, 0), (0, 2), (2, 1), (1, 2)), factors (3, 2, ½, 3, 4; k ≠ 1) and line positions, each with evidence-versus-proof language (R10). |
| S37-M-Q4 | revised | R06 | type, prompt, choices, correct_letter, correct_answer, grading_note | Five comparable verifications with different centers ((0, 0), (0, 2), (2, 1), (1, 2)), factors (3, 2, ½, 3, 4; k ≠ 1) and line positions, each with evidence-versus-proof language (R10). |
| S37-M-Q5 | revised | R06 | type, prompt, choices, correct_letter, correct_answer, grading_note | Five comparable verifications with different centers ((0, 0), (0, 2), (2, 1), (1, 2)), factors (3, 2, ½, 3, 4; k ≠ 1) and line positions, each with evidence-versus-proof language (R10). |
| S38-M-Q4 | revised | R06 | type, prompt, choices, correct_letter, correct_answer, grading_note | Coordinate verifications replace selected-response items; evidence versus proof stated. |
| S38-M-Q5 | revised | R06 | type, prompt, choices, correct_letter, correct_answer, grading_note | Coordinate verifications replace selected-response items; evidence versus proof stated. |
| S38-F1-Q3 | revised | R11 | prompt, grading_note | Nonfixed points and k ≠ 1. |
| S39-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Two more decide-and-describe tasks on the grid (not similar; dilation about S then a translation). |
| S39-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Two more decide-and-describe tasks on the grid (not similar; dilation about S then a translation). |
| S40-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explain-and-use tasks replace selected-response items. |
| S40-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explain-and-use tasks replace selected-response items. |
| S40-F2-Q2 | revised | R04 | prompt | D on AB and E on AC stated. |
| S41-M-Q2 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable AA proofs. |
| S41-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable AA proofs. |
| S41-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure, required_method | Five comparable AA proofs. |
| S41-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable AA proofs. |
| S42-M-Q2 | revised | R02 | type, prompt, correct_answer, grading_note, figure, required_method | Five comparable proofs (ratios with DE/BC; coordinate proof; dilation proof). |
| S42-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable proofs (ratios with DE/BC; coordinate proof; dilation proof). |
| S42-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable proofs (ratios with DE/BC; coordinate proof; dilation proof). |
| S42-B1-Q2 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B1-Q3 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B1-Q4 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B1-Q5 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B2-Q2 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B2-Q3 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B2-Q4 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S42-B3-Q1 | revised | R14 | prompt | Nonzero values stated before reciprocals. |
| S42-F1-Q4 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable proofs of the converse. |
| S43-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable proofs of the converse. |
| S43-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable proofs of the converse. |
| S43-B1-Q1 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B1-Q2 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B1-Q3 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B1-Q4 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B2-Q2 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B3-Q2 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-B3-Q3 | revised | R04 | prompt | D on AB and E on AC stated in each item. |
| S43-F2-Q5 | revised | R04 | prompt | P defined as the midpoint of diagonal AC. |
| S44-M-Q2 | revised | R02 | type, prompt, correct_answer, grading_note, figure, required_method | Five comparable similarity proofs of the Pythagorean Theorem. |
| S44-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, figure, required_method | Five comparable similarity proofs of the Pythagorean Theorem. |
| S44-M-Q4 | revised | R16 | prompt, correct_answer, grading_note, figure, required_method | x = AD, y = DB, AC = 6, BC = 8. |
| S44-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable similarity proofs of the Pythagorean Theorem. |
| S44-B1-Q2 | revised | R04 | prompt | Right angle at C and the altitude to the hypotenuse stated. |
| S44-B1-Q3 | revised | R04 | prompt | Right angle at C and the altitude to the hypotenuse stated. |
| S44-B1-Q4 | revised | R04 | prompt | Right angle at C and the altitude to the hypotenuse stated. |
| S44-F1-Q1 | revised | R04 | prompt | Right angle at C and the altitude to the hypotenuse stated. |
| S44-F1-Q2 | revised | R04 | prompt | Right angle at C and the altitude to the hypotenuse stated. |
| S45-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Solve-with-a-criterion tasks replace selected-response items. |
| S45-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Solve-with-a-criterion tasks replace selected-response items. |
| S45-B3-Q1 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S45-B3-Q2 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S45-B3-Q4 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S45-B3-Q5 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S45-F1-Q4 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S45-F2-Q1 | revised | R04 | prompt | Points on the sides and DE ∥ BC stated. |
| S46-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Fifth congruence proof replaces a selected-response item. |
| S47-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Fifth similarity proof replaces a selected-response item. |
| S47-B3-Q1 | revised | R04 | prompt | D on AB and E on AC stated. |
| S47-F1-Q5 | revised | R04 | prompt | D on AB and E on AC stated. |
| S48-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explain-with-similarity tasks replace selected-response items. |
| S48-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explain-with-similarity tasks replace selected-response items. |
| S48-B2-Q3 | revised | R04 | prompt | Right triangle with the right angle at C stated. |
| S48-B2-Q4 | revised | R04 | prompt | Right triangle with the right angle at C stated. |
| S49-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explain-and-use task (ladder) replaces a selected-response item. |
| S49-B2-Q2 | revised | R04 | prompt | Right triangle with the right angle at C stated. |
| S49-B2-Q3 | revised | R04 | prompt | Right triangle with the right angle at C stated. |
| S49-F1-Q2 | revised | N12 | prompt, correct_answer, grading_note | Nearest hundredth stated. |
| S50-B2-Q2 | revised | R27 | prompt, grading_note | Nearest hundredth stated (17.86). |
| S50-F2-Q1 | revised | R28 | prompt | Constraint answers round in the compliant direction (36 ft; 16.4 m; ladder rounded up; 12.0 ft). |
| S50-F2-Q2 | revised | R28 | prompt, correct_answer, grading_note | Constraint answers round in the compliant direction (36 ft; 16.4 m; ladder rounded up; 12.0 ft). |
| S50-F2-Q4 | revised | R28 | prompt | Constraint answers round in the compliant direction (36 ft; 16.4 m; ladder rounded up; 12.0 ft). |
| S50-F2-Q5 | revised | R28 | prompt, correct_answer, grading_note | Constraint answers round in the compliant direction (36 ft; 16.4 m; ladder rounded up; 12.0 ft). |
| S51-F2-Q5 | revised | N12 | prompt | Nearest tenth of a km stated. |
| S53-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Two more similarity proofs (with a check point; dilation first). |
| S53-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Two more similarity proofs (with a check point; dilation first). |
| S54-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Short-answer item with two inscribed angles replaces a true/false item. |
| S54-F1-Q1 | revised | R17 | prompt, correct_answer, grading_note, required_method | Intercepted arc and the major-arc (reflex) convention stated. |
| S54-F1-Q2 | revised | R17 | prompt, correct_answer, grading_note, required_method | Intercepted arc and the major-arc (reflex) convention stated. |
| S54-F2-Q1 | revised | R04 | prompt | "In a circle" stated. |
| S54-F2-Q2 | revised | R17 | prompt, grading_note, required_method | Intercepted arc and the major-arc (reflex) convention stated. |
| S54-F2-Q3 | revised | R17 | prompt, grading_note | Intercepted arc and the major-arc (reflex) convention stated. |
| S55-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Full tasks (angles with x; slope check of a right angle). |
| S55-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Full tasks (angles with x; slope check of a right angle). |
| S56-M-Q4 | revised | R18 | type, prompt, choices, correct_letter, correct_answer, grading_note | "T lies on circle O and P is outside it"; conclusion "not tangent". |
| S56-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Converse task replaces a true/false item. |
| S57-M-Q2 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S57-M-Q3 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S57-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Full tasks replace selected-response items. |
| S57-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Full tasks replace selected-response items. |
| S57-F1-Q1 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S57-F1-Q2 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S57-F1-Q4 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S57-F1-Q5 | revised | R04 | prompt | Tangents from P touch circle O at A and B stated. |
| S58-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Congruent-chords proof and computation replace selected-response items. |
| S58-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Congruent-chords proof and computation replace selected-response items. |
| S58-B2-Q4 | revised | N07 | prompt | Chords that are not parallel. |
| S59-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Two more incircle constructions with evidence (perpendiculars to all sides; third bisector check). |
| S59-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Two more incircle constructions with evidence (perpendiculars to all sides; third bisector check). |
| S60-M-Q2 | revised | N13 | figure | Triangle redrawn so it is obtuse at C, as described. |
| S60-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Two more circumcircle constructions with evidence (third perpendicular bisector; compass check). |
| S60-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Two more circumcircle constructions with evidence (third perpendicular bisector; compass check). |
| S61-M-Q3 | revised | R02 | type, prompt, grading_note, required_method | Computation now a shown-work justification with the theorem named. |
| S61-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs (inscribed parallelogram is a rectangle; inscribed trapezoid is isosceles). |
| S61-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs (inscribed parallelogram is a rectangle; inscribed trapezoid is isosceles). |
| S62-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Explanation task replaces a selected-response item. |
| S62-F2-Q2 | revised | N08 | prompt | Wheel rotating about a fixed center. |
| S63-M-Q2 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable derivations, each followed by a use. |
| S63-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable derivations, each followed by a use. |
| S63-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable derivations, each followed by a use. |
| S63-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable derivations, each followed by a use. |
| S64-M-Q2 | revised | R02 | type, prompt, grading_note, required_method | Five comparable derivations with the Pythagorean Theorem. |
| S64-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable derivations with the Pythagorean Theorem. |
| S64-M-Q4 | revised | R02 | type, prompt, grading_note, required_method | Five comparable derivations with the Pythagorean Theorem. |
| S64-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable derivations with the Pythagorean Theorem. |
| S65-M-Q1 | revised | R02 | prompt, correct_answer | Standard form required in each item. |
| S65-M-Q2 | revised | R02 | prompt, correct_answer | Standard form required in each item. |
| S65-M-Q4 | revised | R02 | prompt, correct_answer | Standard form required in each item. |
| S65-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Work item replaces a selected-response item. |
| S66-M-Q2 | revised | R02 | type, prompt, grading_note, required_method | Five comparable derivations from focus and directrix. |
| S66-M-Q3 | revised | R02 | type, prompt, grading_note, required_method | Five comparable derivations from focus and directrix. |
| S66-M-Q4 | revised | R02 | type, prompt, grading_note, required_method | Five comparable derivations from focus and directrix. |
| S66-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable derivations from focus and directrix. |
| S66-F1-Q3 | revised | R19 | prompt, grading_note | \|p\| used. |
| S67-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Coordinate proofs replace a short answer and a selected-response item. |
| S67-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Coordinate proofs replace a short answer and a selected-response item. |
| S67-F1-Q2 | revised | R14 | prompt | a > 0 and c ≠ 0 stated. |
| S68-M-Q1 | revised | R07 | prompt, correct_answer, grading_note, required_method | Original data replace the official example. |
| S68-M-Q2 | revised | R02 | type, grading_note, required_method | Prove-or-disprove items are now shown-work coordinate proofs. |
| S68-M-Q3 | revised | R02 | type, grading_note, required_method | Prove-or-disprove items are now shown-work coordinate proofs. |
| S68-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Coordinate proof replaces a selected-response item. |
| S68-B1-Q2 | revised | R07 | prompt, correct_answer | Original data replace the official example. |
| S69-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Proofs (parallel implies equal slopes; product -1 implies perpendicular; converse of the Pythagorean Theorem). |
| S69-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs (parallel implies equal slopes; product -1 implies perpendicular; converse of the Pythagorean Theorem). |
| S69-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs (parallel implies equal slopes; product -1 implies perpendicular; converse of the Pythagorean Theorem). |
| S70-F2-Q1 | revised | N12 | prompt, grading_note | Exact value requested in the student text. |
| S70-F2-Q5 | revised | N12 | prompt, grading_note | Exact value requested in the student text. |
| S71-B4-Q4 | revised | R04 | prompt | "In parallelogram ABCD" stated. |
| S71-F2-Q1 | revised | N12 | prompt | Nearest hundredth stated. |
| S73-B2-Q4 | revised | R20 | prompt, grading_note | Absolute value of the difference. |
| S73-F1-Q3 | revised | R03 | prompt, correct_letter, correct_answer, grading_note | Items now find a missing coordinate from a perimeter. |
| S73-F1-Q4 | revised | R03 | prompt, choices, correct_answer, grading_note | Items now find a missing coordinate from a perimeter. |
| S73-F1-Q5 | revised | R03 | prompt, correct_answer, grading_note | Items now find a missing coordinate from a perimeter. |
| S75-M-Q1 | revised | R01 | prompt, correct_answer, grading_note, figure, skill, required_method | Circumference-only MAIN with five comparable informal arguments (hexagon bounds, similarity, rolling, polygon limit); the area argument moved to S103. |
| S75-M-Q2 | revised | R01 | skill | Circumference-only MAIN with five comparable informal arguments (hexagon bounds, similarity, rolling, polygon limit); the area argument moved to S103. |
| S75-M-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Circumference-only MAIN with five comparable informal arguments (hexagon bounds, similarity, rolling, polygon limit); the area argument moved to S103. |
| S75-M-Q4 | revised | R01 | type, prompt, grading_note, skill, required_method | Circumference-only MAIN with five comparable informal arguments (hexagon bounds, similarity, rolling, polygon limit); the area argument moved to S103. |
| S75-M-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Circumference-only MAIN with five comparable informal arguments (hexagon bounds, similarity, rolling, polygon limit); the area argument moved to S103. |
| S75-B1-Q1 | revised | R01 | skill | Prerequisite limited to the circumference formula. |
| S75-B1-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Prerequisite limited to the circumference formula. |
| S75-B1-Q3 | revised | R01 | skill | Prerequisite limited to the circumference formula. |
| S75-B1-Q4 | revised | R01 | skill | Prerequisite limited to the circumference formula. |
| S75-B1-Q5 | revised | R01 | skill | Prerequisite limited to the circumference formula. |
| S75-B2-Q1 | retired | R01 |  | Parallelogram-area prerequisite moved with the area argument to S103-B2. |
| S75-B2-Q2 | retired | R01 |  | Parallelogram-area prerequisite moved with the area argument to S103-B2. |
| S75-B2-Q3 | retired | R01 |  | Parallelogram-area prerequisite moved with the area argument to S103-B2. |
| S75-B2-Q4 | retired | R01 |  | Parallelogram-area prerequisite moved with the area argument to S103-B2. |
| S75-B2-Q5 | retired | R01 |  | Parallelogram-area prerequisite moved with the area argument to S103-B2. |
| S75-B4-Q1 | new | R01 |  | New prerequisite branch: perimeters of regular polygons, for the circumference argument. |
| S75-B4-Q2 | new | R01 |  | New prerequisite branch: perimeters of regular polygons, for the circumference argument. |
| S75-B4-Q3 | new | R01 |  | New prerequisite branch: perimeters of regular polygons, for the circumference argument. |
| S75-B4-Q4 | new | R01 |  | New prerequisite branch: perimeters of regular polygons, for the circumference argument. |
| S75-B4-Q5 | new | R01 |  | New prerequisite branch: perimeters of regular polygons, for the circumference argument. |
| S75-F1-Q1 | revised | R01 | type, prompt, correct_answer, grading_note, skill, required_method | New FORWARD 1: trap π between polygons (the area-limit branch moved to S103-F1). |
| S75-F1-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | New FORWARD 1: trap π between polygons (the area-limit branch moved to S103-F1). |
| S75-F1-Q3 | revised | R01 | prompt, grading_note, skill | New FORWARD 1: trap π between polygons (the area-limit branch moved to S103-F1). |
| S75-F1-Q4 | revised | R01 | prompt, choices, correct_answer, grading_note, skill | New FORWARD 1: trap π between polygons (the area-limit branch moved to S103-F1). |
| S75-F1-Q5 | revised | R01 | prompt, correct_answer, grading_note, skill | New FORWARD 1: trap π between polygons (the area-limit branch moved to S103-F1). |
| S75-F2-Q1 | revised | R01 | prompt, correct_answer, grading_note, skill | New FORWARD 2: extend the circumference argument to arcs (the disk-stacking branch moved to S103-F2). |
| S75-F2-Q2 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | New FORWARD 2: extend the circumference argument to arcs (the disk-stacking branch moved to S103-F2). |
| S75-F2-Q3 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | New FORWARD 2: extend the circumference argument to arcs (the disk-stacking branch moved to S103-F2). |
| S75-F2-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | New FORWARD 2: extend the circumference argument to arcs (the disk-stacking branch moved to S103-F2). |
| S75-F2-Q5 | revised | R01 | prompt, correct_answer, grading_note, skill | New FORWARD 2: extend the circumference argument to arcs (the disk-stacking branch moved to S103-F2). |
| S76-M-Q3 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable informal arguments (Cavalieri with a prism; V = Bh; polygon prisms). |
| S76-M-Q4 | revised | R02 | type, grading_note, required_method | Five comparable informal arguments (Cavalieri with a prism; V = Bh; polygon prisms). |
| S76-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable informal arguments (Cavalieri with a prism; V = Bh; polygon prisms). |
| S77-M-Q1 | revised | R25 | prompt, correct_answer, grading_note, skill, required_method | General pyramid argument required: cube dissection, vertical scaling, and Cavalieri's principle. |
| S77-M-Q2 | revised | R01 | prompt, correct_answer, grading_note, figure, skill, required_method | Pyramid-only MAIN (Euclid prism dissection, experiment as evidence, cube check, slab limit); the cone argument moved to S104. |
| S77-M-Q3 | revised | R01 | type, prompt, correct_answer, grading_note, skill, required_method | Pyramid-only MAIN (Euclid prism dissection, experiment as evidence, cube check, slab limit); the cone argument moved to S104. |
| S77-M-Q4 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Pyramid-only MAIN (Euclid prism dissection, experiment as evidence, cube check, slab limit); the cone argument moved to S104. |
| S77-M-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill, required_method | Pyramid-only MAIN (Euclid prism dissection, experiment as evidence, cube check, slab limit); the cone argument moved to S104. |
| S77-B2-Q3 | revised | R01 | prompt, choices, correct_answer | Base of a square pyramid (not a cone). |
| S77-B3-Q1 | retired | R01 |  | Cylinder-argument prerequisite moved with the cone argument to S104-B2. |
| S77-B3-Q2 | retired | R01 |  | Cylinder-argument prerequisite moved with the cone argument to S104-B2. |
| S77-B3-Q3 | retired | R01 |  | Cylinder-argument prerequisite moved with the cone argument to S104-B2. |
| S77-B3-Q4 | retired | R01 |  | Cylinder-argument prerequisite moved with the cone argument to S104-B2. |
| S77-B3-Q5 | retired | R01 |  | Cylinder-argument prerequisite moved with the cone argument to S104-B2. |
| S77-B4-Q1 | new | R01 |  | New prerequisite branch: splitting a volume into equal parts, for the dissection argument. |
| S77-B4-Q2 | new | R01 |  | New prerequisite branch: splitting a volume into equal parts, for the dissection argument. |
| S77-B4-Q3 | new | R01 |  | New prerequisite branch: splitting a volume into equal parts, for the dissection argument. |
| S77-B4-Q4 | new | R01 |  | New prerequisite branch: splitting a volume into equal parts, for the dissection argument. |
| S77-B4-Q5 | new | R01 |  | New prerequisite branch: splitting a volume into equal parts, for the dissection argument. |
| S77-F1-Q1 | revised | R01 | prompt, skill | Cavalieri branch limited to pyramids. |
| S77-F1-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Cavalieri branch limited to pyramids. |
| S77-F1-Q3 | revised | R01 | skill | Cavalieri branch limited to pyramids. |
| S77-F1-Q4 | revised | R01 | prompt, choices, correct_answer, skill | Cavalieri branch limited to pyramids. |
| S77-F1-Q5 | revised | R01 | skill | Cavalieri branch limited to pyramids. |
| S77-F2-Q1 | revised | R01 | skill | Formula-use branch limited to pyramids. |
| S77-F2-Q2 | revised | R01 | prompt, correct_answer, grading_note, skill | Formula-use branch limited to pyramids. |
| S77-F2-Q3 | revised | R01 | prompt, skill | Formula-use branch limited to pyramids. |
| S77-F2-Q4 | revised | R01 | skill | Formula-use branch limited to pyramids. |
| S77-F2-Q5 | revised | R01 | prompt, correct_answer, grading_note, skill | Formula-use branch limited to pyramids. |
| S80-F1-Q1 | revised | R28 | prompt, grading_note | "At least" requirement; smallest compliant value in tenths (round up). |
| S80-F1-Q2 | revised | R28 | prompt, correct_answer, grading_note | "At least" requirement; smallest compliant value in tenths (round up). |
| S80-F2-Q2 | revised | R28 | prompt, grading_note | "At least" requirement; smallest compliant value in tenths (round up). |
| S81-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note | Short-answer item replaces a true/false item. |
| S81-F1-Q5 | revised | N12 | prompt | Exact area requested. |
| S81-F2-Q4 | revised | R04 | prompt | Hemisphere resting on its base; y is the height above the base plane, 0 ≤ y ≤ r. |
| S82-B1-Q1 | revised | R12 | prompt, grading_note | P different from the center O. |
| S82-F2-Q4 | revised | R21 | prompt, choices, correct_answer, grading_note | Axis in the rectangle's plane, parallel to a side, outside the rectangle. |
| S82-F2-Q5 | revised | R21 | prompt | Axis in the rectangle's plane, parallel to a side, outside the rectangle. |
| S83-F2-Q1 | revised | R22 | correct_answer, grading_note | Key 1,380 kg. |
| S84-F2-Q2 | revised | R23 | prompt, correct_answer, grading_note | Smallest whole number of m² (3,334). |
| S87-M-Q1 | revised | R01 | skill | Cost-only MAIN (two new cost comparisons); grid items moved to S105. |
| S87-M-Q2 | revised | R01 | skill | Cost-only MAIN (two new cost comparisons); grid items moved to S105. |
| S87-M-Q3 | revised | R01 | skill | Cost-only MAIN (two new cost comparisons); grid items moved to S105. |
| S87-M-Q4 | revised | R01 | prompt, correct_answer, grading_note, figure, skill | Cost-only MAIN (two new cost comparisons); grid items moved to S105. |
| S87-M-Q5 | revised | R01 | type, prompt, choices, correct_letter, correct_answer, grading_note, skill | Cost-only MAIN (two new cost comparisons); grid items moved to S105. |
| S87-B2-Q1 | retired | R01 |  | Ratio prerequisite moved with the grid subskill to S105-B1. |
| S87-B2-Q2 | retired | R01 |  | Ratio prerequisite moved with the grid subskill to S105-B1. |
| S87-B2-Q3 | retired | R01 |  | Ratio prerequisite moved with the grid subskill to S105-B1. |
| S87-B2-Q4 | retired | R01 |  | Ratio prerequisite moved with the grid subskill to S105-B1. |
| S87-B2-Q5 | retired | R01 |  | Ratio prerequisite moved with the grid subskill to S105-B1. |
| S87-B4-Q1 | new | R01 |  | New prerequisite branch: areas of surfaces with openings, for cost problems. |
| S87-B4-Q2 | new | R01 |  | New prerequisite branch: areas of surfaces with openings, for cost problems. |
| S87-B4-Q3 | new | R01 |  | New prerequisite branch: areas of surfaces with openings, for cost problems. |
| S87-B4-Q4 | new | R01 |  | New prerequisite branch: areas of surfaces with openings, for cost problems. |
| S87-B4-Q5 | new | R01 |  | New prerequisite branch: areas of surfaces with openings, for cost problems. |
| S87-F1-Q1 | revised | N09 | prompt | Closed boxes; thickness ignored. |
| S87-F1-Q2 | revised | R01 | prompt, correct_answer, grading_note | Least-material cylinder items replace grid items (moved to S105-F1). |
| S87-F1-Q3 | revised | N09 | prompt | Closed boxes; thickness ignored. |
| S87-F1-Q4 | revised | R01 | prompt, choices, correct_answer, grading_note | Least-material cylinder items replace grid items (moved to S105-F1). |
| S87-F1-Q5 | revised | R01 | prompt, correct_answer, grading_note | Least-material cylinder items replace grid items (moved to S105-F1). |
| S87-F2-Q2 | revised | R24 | prompt, correct_answer, grading_note | Baseline metal and "strictly lower" expected cost. |
| S88-M-Q1 | revised | R26 | prompt, correct_answer, grading_note, required_method | Derivation covers acute and obtuse ∠C. |
| S88-M-Q5 | revised | R26 | type, prompt, choices, correct_letter, correct_answer, grading_note | Obtuse included angle task replaces a selected-response item. |
| S89-M-Q3 | revised | R26 | type, prompt, correct_answer, grading_note, required_method | Proofs covering the other altitude and the circumscribed-circle method, with the obtuse case noted. |
| S89-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Right-triangle case proof replaces a selected-response item. |
| S89-M-Q5 | revised | R26 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs covering the other altitude and the circumscribed-circle method, with the obtuse case noted. |
| S89-B1-Q2 | revised | R26 | prompt, grading_note | Acute triangle stated; obtuse case noted. |
| S90-M-Q3 | revised | R26 | type, prompt, correct_answer, grading_note, required_method | Obtuse-angle proof of the Law of Cosines. |
| S90-M-Q4 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs replace selected-response items. |
| S90-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Proofs replace selected-response items. |
| S93-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, figure | Three more tangent constructions, each with evidence or justification. |
| S93-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, figure, required_method | Three more tangent constructions, each with evidence or justification. |
| S93-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | Three more tangent constructions, each with evidence or justification. |
| S93-F2-Q1 | revised | R04 | prompt | Earth radius 6,371 km and the no-refraction model repeated in each item. |
| S93-F2-Q2 | revised | R04 | prompt | Earth radius 6,371 km and the no-refraction model repeated in each item. |
| S94-M-Q2 | revised | R02 | type, prompt, grading_note, required_method | Five comparable ellipse derivations. |
| S94-M-Q3 | revised | R02 | type, prompt, grading_note, required_method | Five comparable ellipse derivations. |
| S94-M-Q4 | revised | R02 | type, prompt, grading_note, required_method | Five comparable ellipse derivations. |
| S94-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable ellipse derivations. |
| S95-M-Q2 | revised | R02 | type, prompt, grading_note, required_method | Five comparable hyperbola derivations. |
| S95-M-Q3 | revised | R02 | type, prompt, grading_note, required_method | Five comparable hyperbola derivations. |
| S95-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable hyperbola derivations. |
| S95-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable hyperbola derivations. |
| S95-F2-Q3 | revised | N10 | prompt, grading_note | Nonzero signed time difference; the extra measurement needed. |
| S95-F2-Q5 | revised | N10 | prompt, correct_answer, grading_note | Nonzero signed time difference; the extra measurement needed. |
| S96-M-Q2 | revised | R02 | type, prompt, correct_answer, grading_note, figure, required_method | Five comparable Cavalieri arguments. |
| S96-M-Q3 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable Cavalieri arguments. |
| S96-M-Q4 | revised | R02 | type, prompt, correct_answer, grading_note, required_method | Five comparable Cavalieri arguments. |
| S96-M-Q5 | revised | R02 | type, prompt, choices, correct_letter, correct_answer, grading_note, required_method | Five comparable Cavalieri arguments. |
| S96-B2-Q2 | revised | R04 | prompt | y defined as the height above the base plane, 0 ≤ y ≤ r. |
| S96-B2-Q5 | revised | R04 | prompt | y defined as the height above the base plane, 0 ≤ y ≤ r. |
| S96-F2-Q2 | revised | R04 | prompt, grading_note | Radii 10 m and 9.5 m repeated; key 717 t. |
| S97-M-Q1 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-M-Q2 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-M-Q3 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-M-Q4 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-M-Q5 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B1-Q1 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B1-Q2 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B1-Q3 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B1-Q4 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B1-Q5 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B2-Q1 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B2-Q2 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B2-Q3 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B2-Q4 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-B2-Q5 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F1-Q1 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F1-Q2 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F1-Q3 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F1-Q4 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F1-Q5 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F2-Q1 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F2-Q2 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F2-Q3 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F2-Q4 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S97-F2-Q5 | new | R01 |  | New set: precise definition of an angle (split from S1). |
| S98-M-Q1 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-M-Q2 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-M-Q3 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-M-Q4 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-M-Q5 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B1-Q1 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B1-Q2 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B1-Q3 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B1-Q4 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B1-Q5 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B2-Q1 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B2-Q2 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B2-Q3 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B2-Q4 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-B2-Q5 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F1-Q1 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F1-Q2 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F1-Q3 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F1-Q4 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F1-Q5 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F2-Q1 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F2-Q2 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F2-Q3 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F2-Q4 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S98-F2-Q5 | new | R01 |  | New set: precise definition of a line segment (split from S1). |
| S99-M-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-M-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-M-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-M-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-M-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B1-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B1-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B1-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B1-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B1-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B2-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B2-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B2-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B2-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B2-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B3-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B3-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B3-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B3-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-B3-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F1-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F1-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F1-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F1-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F1-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F2-Q1 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F2-Q2 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F2-Q3 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F2-Q4 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S99-F2-Q5 | new | R01 |  | New set: precise definition of parallel lines (split from S2). |
| S100-M-Q1 | new | R01 |  | New set: translations (split from S7). |
| S100-M-Q2 | new | R01 |  | New set: translations (split from S7). |
| S100-M-Q3 | new | R01 |  | New set: translations (split from S7). |
| S100-M-Q4 | new | R01 |  | New set: translations (split from S7). |
| S100-M-Q5 | new | R01 |  | New set: translations (split from S7). |
| S100-B1-Q1 | new | R01 |  | New set: translations (split from S7). |
| S100-B1-Q2 | new | R01 |  | New set: translations (split from S7). |
| S100-B1-Q3 | new | R01 |  | New set: translations (split from S7). |
| S100-B1-Q4 | new | R01 |  | New set: translations (split from S7). |
| S100-B1-Q5 | new | R01 |  | New set: translations (split from S7). |
| S100-B2-Q1 | new | R01 |  | New set: translations (split from S7). |
| S100-B2-Q2 | new | R01 |  | New set: translations (split from S7). |
| S100-B2-Q3 | new | R01 |  | New set: translations (split from S7). |
| S100-B2-Q4 | new | R01 |  | New set: translations (split from S7). |
| S100-B2-Q5 | new | R01 |  | New set: translations (split from S7). |
| S100-F1-Q1 | new | R01 |  | New set: translations (split from S7). |
| S100-F1-Q2 | new | R01 |  | New set: translations (split from S7). |
| S100-F1-Q3 | new | R01 |  | New set: translations (split from S7). |
| S100-F1-Q4 | new | R01 |  | New set: translations (split from S7). |
| S100-F1-Q5 | new | R01 |  | New set: translations (split from S7). |
| S100-F2-Q1 | new | R01 |  | New set: translations (split from S7). |
| S100-F2-Q2 | new | R01 |  | New set: translations (split from S7). |
| S100-F2-Q3 | new | R01 |  | New set: translations (split from S7). |
| S100-F2-Q4 | new | R01 |  | New set: translations (split from S7). |
| S100-F2-Q5 | new | R01 |  | New set: translations (split from S7). |
| S101-M-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-M-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-M-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-M-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-M-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B1-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B1-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B1-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B1-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B1-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B2-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B2-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B2-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B2-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B2-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B3-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B3-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B3-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B3-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-B3-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F1-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F1-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F1-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F1-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F1-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F2-Q1 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F2-Q2 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F2-Q3 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F2-Q4 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S101-F2-Q5 | new | R01 |  | New set: opposite angles of a parallelogram (split from S24). |
| S102-M-Q1 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-M-Q2 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-M-Q3 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-M-Q4 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-M-Q5 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B1-Q1 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B1-Q2 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B1-Q3 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B1-Q4 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B1-Q5 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B2-Q1 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B2-Q2 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B2-Q3 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B2-Q4 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-B2-Q5 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F1-Q1 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F1-Q2 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F1-Q3 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F1-Q4 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F1-Q5 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F2-Q1 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F2-Q2 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F2-Q3 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F2-Q4 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S102-F2-Q5 | new | R01 |  | New set: constructions with a variety of tools and methods (split from S28). |
| S103-M-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-M-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-M-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-M-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-M-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B1-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B1-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B1-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B1-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B1-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B2-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B2-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B2-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B2-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B2-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B3-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B3-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B3-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B3-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-B3-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F1-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F1-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F1-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F1-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F1-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F2-Q1 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F2-Q2 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F2-Q3 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F2-Q4 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S103-F2-Q5 | new | R01 |  | New set: informal arguments for the area of a circle (split from S75); five comparable arguments. |
| S104-M-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-M-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-M-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-M-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-M-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B1-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B1-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B1-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B1-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B1-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B2-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B2-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B2-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B2-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B2-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B3-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B3-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B3-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B3-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-B3-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F1-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F1-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F1-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F1-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F1-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F2-Q1 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F2-Q2 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F2-Q3 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F2-Q4 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S104-F2-Q5 | new | R01 |  | New set: informal arguments for the volume of a cone (split from S77); five comparable arguments. |
| S105-M-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-M-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-M-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-M-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-M-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B1-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B1-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B1-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B1-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B1-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B2-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B2-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B2-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B2-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B2-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B3-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B3-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B3-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B3-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-B3-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F1-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F1-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F1-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F1-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F1-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F2-Q1 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F2-Q2 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F2-Q3 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F2-Q4 | new | R01 |  | New set: typographic grid systems (split from S87). |
| S105-F2-Q5 | new | R01 |  | New set: typographic grid systems (split from S87). |

## 1.0.0 — 2026-10-23 (initial release)

All 2915 questions in 96 sets are new. Every ID has the form S<set>-<section>-Q<n> (section M, B1-B4, F1, F2) and uid GEO:<id>.

| Sets | Domain (of the MAIN standard) | IDs |
|---|---|---|
| S1-S36 | Geometry: Congruence | S1-M-Q1 … S36-F2-Q5 (1070 questions) |
| S37-S52 | Geometry: Similarity, Right Triangles & Trigonometry | S37-M-Q1 … S52-F2-Q5 (480 questions) |
| S53-S63 | Geometry: Circles | S53-M-Q1 … S63-F2-Q5 (330 questions) |
| S64-S74 | Geometry: Expressing Geometric Properties with Equations | S64-M-Q1 … S74-F2-Q5 (345 questions) |
| S75-S82 | Geometry: Geometric Measurement & Dimension | S75-M-Q1 … S82-F2-Q5 (250 questions) |
| S83-S87 | Geometry: Modeling with Geometry | S83-M-Q1 … S87-F2-Q5 (155 questions) |
| S88-S96 | Advanced Extension (+) | S88-M-Q1 … S96-F2-Q5 (285 questions) |

### Quality-assurance edits made before release

These were made during this release's own verification, before anyone else saw it. They are listed so a reviewer can see what the checks changed.

- **True/false balance (85 IDs).** The draft keyed 157 more statements True than False, mostly in FORWARD branches. Each listed statement was rewritten as a false statement that targets a common error (for example "Every rotation is its own inverse"), with the grading note saying why it is false. IDs: S3-F2-Q3, S4-F1-Q4, S4-F2-Q5, S5-F2-Q3, S7-F2-Q4, S8-F2-Q3, S9-F1-Q4, S10-F2-Q3, S11-F1-Q3, S11-F2-Q3, S13-F2-Q4, S14-F2-Q3, S15-F2-Q4, S16-F2-Q5, S17-F2-Q4, S18-F2-Q3, S19-F1-Q3, S20-F1-Q3, S20-F2-Q4, S21-F2-Q4, S22-F2-Q3, S23-F1-Q3, S24-F2-Q3, S27-F2-Q3, S29-F2-Q3, S30-F2-Q3, S31-F2-Q3, S32-F1-Q4, S33-F2-Q3, S34-F2-Q3, S35-F1-Q3, S35-F2-Q3, S36-F1-Q3, S36-F2-Q3, S37-F2-Q3, S38-F2-Q3, S39-F2-Q3, S40-F2-Q3, S43-F2-Q3, S44-F2-Q3, S47-F2-Q3, S48-F2-Q3, S49-F2-Q3, S50-F2-Q3, S52-F2-Q3, S53-F2-Q3, S54-F2-Q3, S55-F2-Q3, S56-F2-Q3, S57-F2-Q3, S58-F2-Q3, S59-F1-Q3, S59-F2-Q3, S60-F2-Q3, S61-F2-Q3, S62-F1-Q3, S62-F2-Q3, S63-F1-Q3, S63-F2-Q3, S64-F2-Q3, S65-F2-Q3, S66-F2-Q3, S67-F2-Q3, S68-F2-Q3, S70-F2-Q3, S71-F2-Q3, S72-F2-Q3, S73-F1-Q3, S73-F2-Q3, S74-F2-Q3, S76-F2-Q3, S77-F2-Q3, S78-F2-Q3, S79-F1-Q3, S80-F2-Q3, S81-F2-Q3, S82-F2-Q3, S84-F2-Q3, S85-F2-Q3, S86-F2-Q3, S87-F2-Q3, S90-F2-Q3, S92-F2-Q3, S93-F2-Q3, S94-F2-Q3.
- **Stand-alone wording (64 IDs).** Questions that leaned on another question ("in the same triangle", "the trunk above") or on a figure that is not on their page were rewritten with all the givens; answers unchanged. Short statements that assumed an unstated setup (for example "Dividing both sides by π is allowed") now include it. IDs: S14-F1-Q3, S22-B4-Q3, S25-F1-Q5, S28-F1-Q4, S29-F2-Q4, S30-B1-Q3, S30-F1-Q1, S30-F1-Q2, S31-F1-Q2, S32-F2-Q2, S33-F1-Q1, S33-F2-Q2, S34-M-Q5, S35-F2-Q5, S36-F1-Q2, S42-M-Q5, S44-F1-Q4, S44-M-Q3, S44-M-Q5, S45-B3-Q3, S45-F2-Q4, S46-F1-Q2, S50-F1-Q2, S52-F1-Q4, S52-F1-Q5, S53-F1-Q2, S54-F1-Q4, S54-F1-Q5, S55-F2-Q2, S55-F2-Q4, S58-B1-Q3, S58-B2-Q3, S58-B3-Q3, S61-F2-Q5, S69-F2-Q2, S71-F2-Q2, S75-M-Q3, S77-M-Q4, S80-B1-Q4, S82-F1-Q2, S82-F1-Q3, S83-F2-Q1, S83-F2-Q2, S84-F2-Q5, S86-B1-Q5, S86-B2-Q4, S86-F1-Q1, S86-F2-Q1, S86-F2-Q2, S86-F2-Q4, S86-F2-Q5, S89-B2-Q1, S89-F1-Q2, S89-M-Q4, S90-B1-Q3, S90-F2-Q5, S91-F1-Q2, S91-F2-Q4, S92-F1-Q2, S93-B1-Q4, S93-B2-Q4, S93-F2-Q5, S95-F2-Q4, S96-F2-Q5.
- **Proof criteria (1 ID).** S33-F1-Q2: grading note now lists the essential steps, an accepted alternative, and an invalid argument.

