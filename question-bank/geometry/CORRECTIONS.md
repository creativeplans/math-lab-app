# Geometry 1.1.0 — corrections

Response to the "Geometry v1.0.0 — correction report for Claude Code". Each finding below says what was changed, which IDs changed, and how the change was verified. IDs of corrected questions are kept; content that moved to a new set gets a new ID (map at the end). Nexus functionality is unchanged: the import package uses the same question types and adds fields only.

| Status | Questions |
|---|---:|
| new | 270 |
| retired | 25 |
| revised | 410 |
| unchanged | 2480 |

Version 1.1.0 has 105 sets and 3,160 questions (1.0.0: 96 sets, 2,915 questions).

## R01-R33 resolution list

### R01 — resolved

Each distinct subskill has its own focused set; the subskill matrix is rebuilt from the actual question mapping (splits S1/S97/S98, S2/S99, S7/S100, S24/S101, S28/S102, S75/S103, S77/S104, S87/S105).

IDs (391): S1-M (all), S1-B1 (all), S1-B2 (all), S1-B4 (all), S1-F1 (all), S1-F2 (all), S2-M (all), S7-M (all), S7-B3 (all), S7-F1-Q2, S7-F2 (all), S24-M (all), S24-B3-Q2/5, S24-F1-Q3/4/5, S24-F2 (all), S28-M-Q4/5, S75-M (all), S75-B1 (all), S75-B2 (all), S75-B4 (all), S75-F1 (all), S75-F2 (all), S77-M-Q2/3/4/5, S77-B2-Q3, S77-B3 (all), S77-B4 (all), S77-F1 (all), S77-F2 (all), S87-M (all), S87-B2 (all), S87-B4 (all), S87-F1-Q2/4/5, S97-M (all), S97-B1 (all), S97-B2 (all), S97-F1 (all), S97-F2 (all), S98-M (all), S98-B1 (all), S98-B2 (all), S98-F1 (all), S98-F2 (all), S99-M (all), S99-B1 (all), S99-B2 (all), S99-B3 (all), S99-F1 (all), S99-F2 (all), S100-M (all), S100-B1 (all), S100-B2 (all), S100-F1 (all), S100-F2 (all), S101-M (all), S101-B1 (all), S101-B2 (all), S101-B3 (all), S101-F1 (all), S101-F2 (all), S102-M (all), S102-B1 (all), S102-B2 (all), S102-F1 (all), S102-F2 (all), S103-M (all), S103-B1 (all), S103-B2 (all), S103-B3 (all), S103-F1 (all), S103-F2 (all), S104-M (all), S104-B1 (all), S104-B2 (all), S104-B3 (all), S104-F1 (all), S104-F2 (all), S105-M (all), S105-B1 (all), S105-B2 (all), S105-B3 (all), S105-F1 (all), S105-F2 (all)

Verified by: Check 4 (every subskill is the declared focus of exactly the sets listed in COVERAGE.md section 3); the COVERAGE matrix is generated from each set's covers= list, so it reflects the actual question mapping.

### R02 — resolved

All five MAIN questions are comparable full performances: proofs in proof sets, constructions with evidence in construction sets, derivations or informal arguments in derive/explain sets; true/false items removed from every MAIN.

IDs (142): S3-M-Q5, S4-M-Q4, S5-M-Q2/4, S6-M-Q3/4, S10-M-Q5, S11-M-Q4, S12-M-Q3/4, S13-M-Q3/4/5, S14-M-Q2/3/4/5, S15-M-Q2/3/4/5, S16-M-Q3/4/5, S17-M-Q3/5, S19-M-Q5, S20-M-Q4, S21-M-Q5, S22-M-Q3/5, S23-M-Q3/5, S25-M-Q4/5, S26-M-Q5, S27-M-Q4/5, S29-M-Q3/5, S30-M-Q4/5, S31-M-Q4/5, S32-M-Q4/5, S33-M-Q4/5, S34-M-Q4/5, S35-M-Q4/5, S36-M-Q4/5, S39-M-Q4/5, S40-M-Q4/5, S41-M-Q2/3/4/5, S42-M-Q2/4/5, S43-M-Q3/4/5, S44-M-Q2/3/5, S45-M-Q4/5, S46-M-Q5, S47-M-Q5, S48-M-Q4/5, S49-M-Q5, S53-M-Q3/5, S54-M-Q5, S55-M-Q4/5, S56-M-Q5, S57-M-Q4/5, S58-M-Q4/5, S59-M-Q4/5, S60-M-Q4/5, S61-M-Q3/4/5, S62-M-Q5, S63-M-Q2/3/4/5, S64-M-Q2/3/4/5, S65-M-Q1/2/4/5, S66-M-Q2/3/4/5, S67-M-Q4/5, S68-M-Q2/3/5, S69-M-Q3/4/5, S76-M-Q3/4/5, S81-M-Q5, S89-M-Q4, S90-M-Q4/5, S93-M-Q3/4/5, S94-M-Q2/3/4/5, S95-M-Q2/3/4/5, S96-M-Q2/3/4/5

Verified by: Check 18 (MAIN comparability), plus the author's reading of every changed MAIN (VALIDATION.md, "Proofs checked step by step").

### R03 — resolved

Forward branches audited for focus and one new demand; duplicated or off-demand forward items replaced (S4-F2, S12-F1-Q4, S29-F1, S34-F1, S73-F1, S100-F2-Q3, and others).

IDs (23): S2-F1-Q3/4/5, S2-F2 (all), S4-F2-Q5, S9-F2-Q4/5, S12-F1-Q4, S25-F1-Q3, S29-F1-Q2/3/5, S34-F1-Q2/3/4/5, S73-F1-Q3/4/5

Verified by: Bank-wide stem comparison (no repeat within a set; 15 review stems recur only as prerequisites across sets); each forward branch re-read for one new demand.

### R04 — resolved

Every question states its own givens (points on sides, right angles, tangency, heights, radii, models) instead of relying on a figure or an earlier question.

IDs (53): S16-M-Q2, S29-B2-Q1, S29-F1-Q4, S31-B2-Q3/4, S40-F2-Q2, S42-B1-Q2/3/4/5, S42-B2-Q2/3/4, S42-F1-Q4, S43-B1-Q1/2/3/4, S43-B2-Q2, S43-B3-Q2/3, S43-F2-Q5, S44-B1-Q2/3/4, S44-F1-Q1/2, S45-B3-Q1/2/4/5, S45-F1-Q4, S45-F2-Q1, S47-B3-Q1, S47-F1-Q5, S48-B2-Q3/4, S49-B2-Q2/3, S54-F2-Q1, S57-M-Q2/3, S57-F1-Q1/2/4/5, S71-B4-Q4, S81-F2-Q4, S93-F2-Q1/2, S96-B2-Q2/5, S96-F2-Q2

Verified by: Check 16 (phrase search) plus a bank-wide read of stems that start with a figure name (△, DE ∥, AD =, ∠) without their givens.

### R05 — resolved

No circular dependencies: SSS (S16) is justified with SAS and an angle bisector, not the perpendicular-bisector converse; S18 establishes corresponding angles by a translation before the other angle-pair theorems.

IDs (9): S16-M-Q1, S18-M (all), S19-M-Q2/3, S20-M-Q1

Verified by: VALIDATION.md "Proof-dependency review" table (manual).

### R06 — resolved

S37 and S38 MAIN are five comparable experimental verifications with different centers, factors and line positions, each stating that examples are evidence, not proof.

IDs (7): S37-M (all), S38-M-Q4/5

Verified by: Check 18; keys recomputed (resolve.py cases S37-M-Q4/Q5, S38-M-Q4/Q5).

### R07 — resolved

S68-M-Q1 uses original data (center (2, -1), points (2, 4) and (5, 3)) instead of the official example (1, √3); its prerequisite item changed to match.

IDs (2): S68-M-Q1, S68-B1-Q2

### R08 — resolved

Exporter crop fixed for coordinate figures whose point list is empty (segments given by coordinates); all such SVG/PNG assets re-rendered and checked.

Engine: `engine/export.py` write_figure widens each drawing box by its stroke before the union (a horizontal or vertical segment has a zero-height box, which a Rect union ignored). Example S28-F1-Q1: segment c was missing and a, b were cut off; all three now show. Unchanged questions whose PNG/SVG changed only by this crop keep their status (unchanged) because the question content is identical.

Verified by: All 25 point-free coordinate figures re-rendered and inspected (VALIDATION.md, "Figures inspected").

### R09 — resolved

S11-F1-Q2 states rotation directions (70° counterclockwise then 50° clockwise).

IDs (1): S11-F1-Q2

### R10 — resolved

S37 dilation items about lines use scale factors k ≠ 1.

### R11 — resolved

S38-F1-Q3 restricts to points other than the center and a dilation with k ≠ 1.

IDs (1): S38-F1-Q3

### R12 — resolved

Rotation items require P ≠ center (S8-M-Q4) and a point P different from the center O (S82-B1-Q1).

IDs (2): S8-M-Q4, S82-B1-Q1

### R13 — resolved

S16-B2-Q2 says "in a given plane".

IDs (1): S16-B2-Q2

### R14 — resolved

Domain assumptions stated: a > 0 and c ≠ 0 (S22-M-Q4, S67-F1-Q2), a ≠ 0 (S22-B2-Q2), P ≠ M (S14-F1-Q2), nonzero values before reciprocals (S42-B3-Q1).

IDs (5): S14-F1-Q2, S22-M-Q4, S22-B2-Q2, S42-B3-Q1, S67-F1-Q2

### R15 — resolved

S20-B3-Q3 names a labeled angle.

IDs (1): S20-B3-Q3

### R16 — resolved

S44-M-Q4 defines x = AD, y = DB with AC = 6 and BC = 8.

IDs (1): S44-M-Q4

### R17 — resolved

Inscribed-angle items use the intercepted arc and state the reflex/major-arc convention (S54-F1-Q1/Q2, S54-F2-Q2/Q3).

IDs (4): S54-F1-Q1/2, S54-F2-Q2/3

### R18 — resolved

S56-M-Q4: "T lies on circle O and P is outside it"; the key concludes "not tangent".

IDs (1): S56-M-Q4

### R19 — resolved

S66-F1-Q3 uses |p| for the focus-vertex distance.

IDs (1): S66-F1-Q3

### R20 — resolved

S73-B2-Q4 uses the absolute value of the difference.

IDs (1): S73-B2-Q4

### R21 — resolved

S82-F2 rotation axes are in the rectangle's plane, parallel to a side, and outside the rectangle.

IDs (2): S82-F2-Q4/5

### R22 — resolved

S83-F2-Q1 key is 1,380 kg (2.3 m³ × 600 kg/m³).

IDs (1): S83-F2-Q1

### R23 — resolved

S84-F2-Q2 asks for the smallest whole number of m² that meets the limit (3,334).

IDs (1): S84-F2-Q2

### R24 — resolved

S87-F2-Q2 gives a baseline (a standard metal that never fails) and asks when the expected cost is strictly lower.

IDs (1): S87-F2-Q2

### R25 — resolved

S77-M-Q1 requires the general pyramid argument (vertical scaling and Cavalieri's principle), not only the cube dissection.

IDs (1): S77-M-Q1

### R26 — resolved

Altitude derivations cover acute and obtuse cases (S88-M-Q1, S88-M-Q5, S89-M-Q3/Q5, S89-B1-Q2, S90-M-Q3).

IDs (6): S88-M-Q1/5, S89-M-Q3/5, S89-B1-Q2, S90-M-Q3

### R27 — resolved

Rounded answers state the precision in the student text (S50-B2-Q2 nearest hundredth, 17.86; bank-wide audit).

IDs (2): S36-F2-Q2, S50-B2-Q2

Verified by: Bank-wide search for decimal keys whose stems state no precision; each hit either already exact or now states the precision.

### R28 — resolved

Constraint answers round in the direction that keeps the design compliant (S50-F2-Q5 12.0 ft, S50-F2-Q2 16.4 m, S50-F2-Q1/Q4, S80-F1-Q1/Q2, S80-F2-Q2).

IDs (7): S50-F2-Q1/2/4/5, S80-F1-Q1/2, S80-F2-Q2

Verified by: Bank-wide search for at most / at least / smallest / largest items with rounding; resolve.py now recomputes S50-F2 and S80 with floor/ceil.

### R29 — resolved

S32-F2-Q1/Q2 put the points on the same side of AB.

IDs (2): S32-F2-Q1/2

### R30 — resolved

S33-B3-Q5 says the point is not on the line.

IDs (1): S33-B3-Q5

### R31 — resolved

S28-B3-Q2 lists three cases.

IDs (1): S28-B3-Q2

### R32 — resolved

The standalone answer-key JSON/CSV carry each question's figure asset paths, description and data by UID (existing fields unchanged).

Engine: `engine/build.py` figure_fields adds figure_svg, figure_png, figure_description, figure_data (and choice_figures) to every Geometry key record; the CSV appends the four figure columns at the end. Example: GEO:S74-M-Q3 now has figure_svg = assets/S74-M-Q3.svg, its description, and its data.

Verified by: Check 19 (figure fields on every record with a figure) and check 14 (JSON and CSV agree).

### R33 — resolved

VALIDATION.md reports each check with its actual scope and evidence; a solved-question log and recalculated totals are included.

`src/validate.py`: every check has a scope statement; new checks 18-21; `src/review_log.py` records the manual proof-dependency review, the hand-solved and step-checked questions, and the inspected figures, and says that no second person reviewed them.

Verified by: VALIDATION.md: scope column on all 21 checks, manual-review sections, check 21 (totals).

## Refinements and issues found in this release's own verification

### N01 — resolved

S1-M-Q1 wording and positive radius.

### N02 — resolved

S5-M-Q3 states the trapezoid convention and the rotation range.

IDs (2): S5-M-Q3/5

### N03 — resolved

S7-B2-Q1/Q4 wording on perpendicular lines.

IDs (5): S7-B2 (all)

### N04 — resolved

S15-F1-Q3 asks how AAS follows from ASA.

IDs (1): S15-F1-Q3

### N05 — resolved

S20-M-Q5 restated.

IDs (1): S20-M-Q5

### N06 — resolved

S35-B2-Q2: "kite that is not a rhombus", most specific name.

IDs (1): S35-B2-Q2

### N07 — resolved

S58-B2-Q4: two chords that are not parallel (distinct perpendicular bisectors).

IDs (1): S58-B2-Q4

### N08 — resolved

S62-F2-Q2: a wheel rotating about a fixed center.

IDs (1): S62-F2-Q2

### N09 — resolved

S87-F1-Q1/Q3: closed boxes, material thickness ignored.

IDs (2): S87-F1-Q1/3

### N10 — resolved

S95-F2-Q3/Q5: a nonzero signed time difference; the extra measurement needed.

IDs (2): S95-F2-Q3/5

### N11 — resolved

Noncollinearity assumptions stated where a triangle or circle needs them.

S19-F2-Q4 (towns not on one line), S67-F1-Q2 (c ≠ 0 so O, A, B are not collinear), S63/S93 constructions use triangles and external points in general position.

IDs (1): S19-F2-Q4

### N12 — resolved

Precision or exact form stated in the student text, not only in the grading note.

IDs (6): S49-F1-Q2, S51-F2-Q5, S70-F2-Q1/5, S71-F2-Q1, S81-F1-Q5

### N13 — resolved

Figure corrected to match its description (S60-M-Q2 triangle is now obtuse at C).

Found by this release's own verification.

IDs (1): S60-M-Q2

### N14 — resolved

Branch or set title edited after a split; the questions are unchanged.

IDs (10): S2-B1 (all), S24-B1 (all)

## Old-to-new ID map

Content that moved keeps its wording under the new ID. Retired IDs are never reused.

| Old ID (1.0.0) | New ID (1.1.0) | Old ID status |
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
| S75-B2-Q1 | S103-B2-Q1 | retired |
| S75-B2-Q2 | S103-B2-Q2 | retired |
| S75-B2-Q3 | S103-B2-Q3 | retired |
| S75-B2-Q4 | S103-B2-Q4 | retired |
| S75-B2-Q5 | S103-B2-Q5 | retired |
| S77-B3-Q1 | S104-B2-Q1 | retired |
| S77-B3-Q2 | S104-B2-Q2 | retired |
| S77-B3-Q3 | S104-B2-Q3 | retired |
| S77-B3-Q4 | S104-B2-Q4 | retired |
| S77-B3-Q5 | S104-B2-Q5 | retired |
| S87-B2-Q1 | S105-B1-Q1 | retired |
| S87-B2-Q2 | S105-B1-Q2 | retired |
| S87-B2-Q3 | S105-B1-Q3 | retired |
| S87-B2-Q4 | S105-B1-Q4 | retired |
| S87-B2-Q5 | S105-B1-Q5 | retired |
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
| S75-M-Q1 | S103-M-Q1 | revised |
| S77-M-Q2 | S104-M-Q1 | revised |
| S87-M-Q4 | S105-M-Q1 | revised |
| S87-M-Q5 | S105-M-Q2 | revised |
| S87-F1-Q2 | S105-M-Q3 | revised |
| S87-F1-Q4 | S105-F1-Q1 | revised |
| S87-F1-Q5 | S105-F1-Q2 | revised |

Retired IDs (25): S1-B1-Q1, S1-B1-Q2, S1-B1-Q3, S1-B1-Q4, S1-B1-Q5, S1-B2-Q1, S1-B2-Q2, S1-B2-Q3, S1-B2-Q4, S1-B2-Q5, S75-B2-Q1, S75-B2-Q2, S75-B2-Q3, S75-B2-Q4, S75-B2-Q5, S77-B3-Q1, S77-B3-Q2, S77-B3-Q3, S77-B3-Q4, S77-B3-Q5, S87-B2-Q1, S87-B2-Q2, S87-B2-Q3, S87-B2-Q4, S87-B2-Q5.

New sets: S97 (angle definition), S98 (segment definition), S99 (parallel-lines definition), S100 (translations), S101 (opposite angles of a parallelogram), S102 (constructions with several tools), S103 (circle area argument), S104 (cone volume argument), S105 (typographic grids). New branches in existing sets: S1-B4, S75-B4, S77-B4, S87-B4.

Every ID with its status, finding codes, and reason is in `revisions.json` in the import package.
