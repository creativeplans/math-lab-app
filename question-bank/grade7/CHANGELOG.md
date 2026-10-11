# Grade 7 question collection — change log

Version 2.0.0 (previous 1.0.0, commit b0a5f7a). One row per question ID that changed. Unchanged IDs are omitted; the full map, including unchanged IDs, is `revisions.json` in the import package.

| Status | Count |
|---|---:|
| unchanged | 1280 |
| revised | 245 |
| retired | 0 |
| new | 230 |

Rules: IDs of corrected questions are kept (status revised). An ID whose skill or standard changes is retired and never reused; the replacement questions get new IDs (status new). Sets added after publication take the next free set number; branches added to an existing set take the next free branch number. Numbers need not be consecutive.

## Review findings

| Code | Finding |
|---|---|
| C01 | Maximum percent error: the actual length is now stated, so 0.5% is exact (S11-F2-Q3) |
| C02 | Battery drops by percentage points of full capacity, a linear change (S20-F2-Q1) |
| C03 | Slant height asks about a RIGHT square pyramid (S48-F1-Q3) |
| C04 | The parallelogram cut is perpendicular to the base, and the slide is described (S43-B1-Q3) |
| C05 | The coin is "claimed to be fair," so doubt about the model is a valid answer (S58-M-Q2) |
| C06 | Treatment questions state random assignment and a no-effect simulation; the key gives evidence, not proof (S61-F2-Q1/Q2) |
| C07 | Overlap questions show paired dot plots whose means and MADs were verified (S52-M) |
| C08 | Write-and-solve questions require both a valid equation (or inequality) and its solution |
| C09 | Equations with two roots require both roots (S32-F2-Q1/Q2, S43-F1-Q1) |
| C10 | Exact or rounded answers are stated explicitly (S29-M-Q2, S53-F2-Q2) |
| C11 | Fair devices, numbered cubes, independent trials, and P(B) > 0 are stated |
| C12 | Formula rearrangements state nonzero divisors; the square-root item states x ≥ 0 |
| C13 | Different triangles means noncongruent; slicing planes cut through the solid's interior |
| B01 | Earlier-grade fractions (and distractors) use their grade's denominators (S56-B1, S56-B2, S61-B2) |
| B02 | Grade 4 branch checks answers to two-step word problems by rounding (S30-B2) |
| B03 | Unit-fraction division items are word problems (S22-B2-Q4/Q5) |
| B04 | Combination counts are built on arrays with one row per first choice (S59-B2) |
| B05 | New numerical addition-property branch: regroup addends within 100 (S18-B3) |
| F01 | Grade 8 equation branches use variables on both sides and rational coefficients (S9-F1, S20-F1, S23-F1) |
| F02 | Grade 8 branch applies the properties of integer exponents with negative bases (S19-F1) |
| F03 | High-school equation branches: justified chains, invalid steps, and letter coefficients (S12-F2, S14-F2, S33-F2) |
| F04 | Expression-interpretation branch interprets terms and factors in context (S26-F2) |
| F05 | Growth-factor branch is percent growth only; the quadratic items were removed (S28-F2) |
| F06 | Modeling branch defines the quantities a model needs (S30-F2-Q1/Q2) |
| F07 | Construction branch performs actual compass-and-straightedge constructions (S38-F2) |
| F08 | Congruence branch explains the criteria with rigid motions (S39-F2) |
| F09 | Proof branches ask for justified chains of reasoning (S44-F2, S45-F2) |
| F10 | Event branch uses unions, intersections, and complements of overlapping events (S54-F2) |
| F11 | Two-way-table branches have students fill in blank tables (S57-F1, S60-F1) |
| F12 | Model-consistency branch judges results against a simulated distribution (S58-F2) |
| F13 | Forward branches strengthened (S2-F2, S4-F2, S25-F2, S46-F2, S56-F1) |
| F14 | Circle forward branches add a derivation item (S41-F2-Q4, S42-F2-Q4) |
| V01 | Focused sets: markup/markdown (S9), simple interest (S10), tips (S62), tax (S63), commissions (S64), fees (S65), combined (S66) |
| V02 | Scale-reproduction (S37) and triangle-drawing (S38) sets are all actual drawings |
| V03 | Signed-fraction addition (S13, S15) and division in context (S22) |
| V04 | Properties applied to subtraction (S18) and division (S23) |
| V05 | S33 asks for an arithmetic solution, an algebraic solution, and a comparison of the steps |
| V06 | S34 is five inequality word problems; S35 is five graph-and-interpret problems in context |
| V07 | Angle sets write and solve equations from labeled figures (S44, S45) |
| V08 | New composite-prism sets: volume (S67) and exterior surface area (S68) |
| V09 | New sets in which students generate random samples (S69) and collect chance data (S70) |
| V10 | S60 has students produce lists, tables, and tree diagrams of sample spaces |
| V11 | S61 runs simulations with given random digits, alongside a design task |
| V12 | Items that drifted from their set's skill were rewritten (S2-M-Q4, S7-M-Q1/Q4, S46-M-Q3, S58-M-Q1) |
| V13 | Population comparisons use both center and spread (S53-M) |
| V14 | S43 asks for the complete wedge argument, with a diagram of the rearranged wedges |
| D01 | High-school standards are labeled as this bank's Grade 9 placement, not an official grade (standard_level field, README) |
| D02 | Coverage and README describe the performances actually tested; CORRECTIONS.md and revisions.json are included |

## ID map

Questions that moved keep their content under a new ID; the old ID is retired or now holds the corrected question for the narrower skill, as the Status column says.

| Old ID | New ID | Old ID status |
|---|---|---|
| S9-M-Q1 | S62-M-Q1 | revised |
| S9-M-Q5 | S63-M-Q5 | revised |
| S10-M-Q2 | S64-M-Q1 | revised |
| S10-M-Q3 | S65-M-Q1 | revised |
| S10-M-Q5 | S65-M-Q5 | revised |
| S9-M-Q2 | S66-M-Q1 | revised |

Retired backward branches and their replacements:

| Retired branch | Replacement branch |
|---|---|

## Changes by question ID

| ID | Status | Findings | What changed | Reason |
|---|---|---|---|---|
| S2-M-Q4 | revised | V12 | prompt, correct_answer, grading_note, figure | Decides whether the table is proportional, with ratio evidence, instead of filling in values. |
| S2-F2-Q1 | revised | F13 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Tells equal differences from equal factors with evidence from tables; branch title updated. |
| S2-F2-Q2 | revised | F13 | prompt, correct_answer, grading_note, figure, skill | Tells equal differences from equal factors with evidence from tables; branch title updated. |
| S2-F2-Q3 | revised | F13 | prompt, choices, correct_answer, skill | Tells equal differences from equal factors with evidence from tables; branch title updated. |
| S2-F2-Q4 | revised | F13 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Tells equal differences from equal factors with evidence from tables; branch title updated. |
| S2-F2-Q5 | revised | F13 | prompt, grading_note, skill | Tells equal differences from equal factors with evidence from tables; branch title updated. |
| S4-F2-Q1 | revised | F13 | prompt, correct_answer, skill | Constructs functions from two input-output pairs, a sequence, or a description; branch title updated. |
| S4-F2-Q2 | revised | F13 | prompt, correct_answer, skill | Constructs functions from two input-output pairs, a sequence, or a description; branch title updated. |
| S4-F2-Q3 | revised | F13 | prompt, choices, correct_answer, skill | Constructs functions from two input-output pairs, a sequence, or a description; branch title updated. |
| S4-F2-Q4 | revised | F13 | prompt, skill | Constructs functions from two input-output pairs, a sequence, or a description; branch title updated. |
| S4-F2-Q5 | revised | F13 | prompt, grading_note, skill | Constructs functions from two input-output pairs, a sequence, or a description; branch title updated. |
| S7-M-Q1 | revised | V12 | prompt, correct_answer, grading_note | A genuinely multistep ratio problem (three-part ratio; map distance then travel time). |
| S7-M-Q4 | revised | V12 | prompt, grading_note | A genuinely multistep ratio problem (three-part ratio; map distance then travel time). |
| S7-F2-Q1 | revised | C08 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S7-F2-Q2 | revised | C08 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S9-M-Q1 | revised | V01 | prompt, correct_answer, skill | S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66. |
| S9-M-Q2 | revised | V01 | prompt, correct_answer, skill | S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66. |
| S9-M-Q3 | revised | V01 | skill | S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66. |
| S9-M-Q4 | revised | V01 | skill | S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66. |
| S9-M-Q5 | revised | V01 | prompt, grading_note, skill | S9 is markup and markdown only (set title updated); its tip, tax, and combined items moved to S62, S63, and S66. |
| S9-F1-Q1 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S9-F1-Q2 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S9-F1-Q3 | revised | F01 | prompt, choices, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S9-F1-Q4 | revised | F01 | prompt, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S9-F1-Q5 | revised | F01 | prompt, grading_note, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S10-M-Q1 | revised | V01 | skill | S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65. |
| S10-M-Q2 | revised | V01 | prompt, correct_answer, skill | S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65. |
| S10-M-Q3 | revised | V01 | prompt, choices, correct_answer, skill | S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65. |
| S10-M-Q4 | revised | V01 | skill | S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65. |
| S10-M-Q5 | revised | V01 | prompt, grading_note, skill | S10 is simple interest only (set title updated); its commission and fee items moved to S64 and S65. |
| S10-F1-Q2 | revised | V01 | prompt, correct_answer, grading_note | Models an interest-bearing loan instead of a commission, to match the simple-interest set. |
| S10-F1-Q5 | revised | V01 | prompt, grading_note | Models an interest-bearing loan instead of a commission, to match the simple-interest set. |
| S11-F2-Q3 | revised | C01 | prompt | States that the actual length is 400 m and the measurement is off by at most 2 m, so the greatest percent error is exactly 0.5%. |
| S12-F2-Q1 | revised | F03 | type, prompt, correct_answer, grading_note, skill, required_method | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S12-F2-Q2 | revised | F03 | prompt, correct_answer, grading_note, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S12-F2-Q3 | revised | F03 | prompt, choices, correct_answer, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S12-F2-Q4 | revised | F03 | prompt, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S12-F2-Q5 | revised | F03 | prompt, grading_note, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S13-M-Q2 | revised | V03 | prompt, correct_answer, grading_note, figure | Adds signed fractions and mixed numbers (on a number line or in context). |
| S13-M-Q5 | revised | V03 | prompt | Adds signed fractions and mixed numbers (on a number line or in context). |
| S14-F2-Q1 | revised | F03 | prompt, correct_answer, grading_note, skill | Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated. |
| S14-F2-Q2 | revised | F03 | prompt, correct_answer, grading_note, skill | Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated. |
| S14-F2-Q3 | revised | F03 | prompt, choices, correct_answer, skill | Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated. |
| S14-F2-Q4 | revised | F03 | prompt, skill | Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated. |
| S14-F2-Q5 | revised | F03 | prompt, grading_note, skill | Equations with letter coefficients (with the needed restrictions) and fraction coefficients; branch title updated. |
| S15-M-Q2 | revised | V03 | prompt, correct_answer, grading_note | Adds signed fractions and mixed numbers (on a number line or in context). |
| S15-M-Q4 | revised | V03 | prompt | Adds signed fractions and mixed numbers (on a number line or in context). |
| S18-M-Q2 | revised | V04 | type, prompt, correct_answer, required_method | Rewrites subtraction as adding the opposite, then regroups (required work). |
| S18-B3-Q1 | new | B05 |  | New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch. |
| S18-B3-Q2 | new | B05 |  | New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch. |
| S18-B3-Q3 | new | B05 |  | New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch. |
| S18-B3-Q4 | new | B05 |  | New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch. |
| S18-B3-Q5 | new | B05 |  | New branch: reorder and regroup addends to add within 100 (2.NBT.B.5). B1 is kept as the symbolic-expression branch. |
| S19-F1-Q1 | revised | F02 | prompt, correct_answer, skill | Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated. |
| S19-F1-Q2 | revised | F02 | prompt, correct_answer, skill | Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated. |
| S19-F1-Q3 | revised | F02 | prompt, choices, correct_answer, skill | Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated. |
| S19-F1-Q4 | revised | F02 | prompt, skill | Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated. |
| S19-F1-Q5 | revised | F02 | prompt, grading_note, skill | Product, quotient, power-of-a-power, zero, and negative exponents with negative bases; branch title updated. |
| S20-F1-Q1 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S20-F1-Q2 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S20-F1-Q3 | revised | F01 | prompt, choices, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S20-F1-Q4 | revised | F01 | prompt, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S20-F1-Q5 | revised | F01 | prompt, grading_note, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S20-F2-Q1 | revised | C02, C08 | prompt, correct_answer, grading_note | The battery drops by 6 percentage points of its full capacity each hour; the equation 90 - 6h = 30 is unchanged. The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S20-F2-Q2 | revised | C08 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S22-M-Q1 | revised | V03 | prompt, correct_answer, grading_note | Divides signed fractions and mixed numbers in context. |
| S22-M-Q3 | revised | V03 | prompt, choices, correct_answer | Divides signed fractions and mixed numbers in context. |
| S22-M-Q5 | revised | V03 | prompt, grading_note | Divides signed fractions and mixed numbers in context. |
| S22-B2-Q4 | revised | B03 | prompt | The same divisions are now word problems (1/5-pound bags; sharing 1/8 pound). |
| S22-B2-Q5 | revised | B03 | prompt, grading_note | The same divisions are now word problems (1/5-pound bags; sharing 1/8 pound). |
| S23-M-Q2 | revised | V04 | type, prompt, correct_answer, required_method | Rewrites division as multiplying by a reciprocal; shows that division itself is not associative. |
| S23-M-Q5 | revised | V04 | prompt, grading_note | Rewrites division as multiplying by a reciprocal; shows that division itself is not associative. |
| S23-F1-Q1 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S23-F1-Q2 | revised | F01 | prompt, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S23-F1-Q3 | revised | F01 | prompt, choices, correct_answer, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S23-F1-Q4 | revised | F01 | prompt, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S23-F1-Q5 | revised | F01 | prompt, grading_note, skill | Equations with the variable on both sides, distribution, or fraction coefficients; branch title updated. |
| S23-F2-Q2 | revised | C12 | prompt | States m ≠ 0, b > 0, r > 0, or real x ≥ 0 as needed. |
| S25-F2-Q1 | revised | F13 | prompt, correct_answer, grading_note | Units are carried through each step of a multistep rate problem. |
| S25-F2-Q2 | revised | F13 | prompt, correct_answer, grading_note | Units are carried through each step of a multistep rate problem. |
| S25-F2-Q3 | revised | F13 | prompt, choices, correct_answer | Units are carried through each step of a multistep rate problem. |
| S26-F2-Q1 | revised | F04 | prompt, correct_answer, grading_note, skill | Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated. |
| S26-F2-Q2 | revised | F04 | prompt, correct_answer, skill | Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated. |
| S26-F2-Q3 | revised | F04 | prompt, choices, correct_answer, skill | Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated. |
| S26-F2-Q4 | revised | F04 | prompt, skill | Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated. |
| S26-F2-Q5 | revised | F04 | prompt, grading_note, skill | Interprets terms, factors, and coefficients of cost, perimeter, and savings expressions; branch title updated. |
| S28-F2-Q1 | revised | F05 | prompt, correct_answer, grading_note, skill | All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated. |
| S28-F2-Q2 | revised | F05 | skill | All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated. |
| S28-F2-Q3 | revised | F05 | skill | All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated. |
| S28-F2-Q4 | revised | F05 | prompt, skill | All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated. |
| S28-F2-Q5 | revised | F05 | skill | All five items rewrite or interpret percent-growth expressions; the quadratic items were removed; branch title updated. |
| S29-M-Q2 | revised | C10 | grading_note | Exact answer 1 11/12 feet (or 23/12); a rounded decimal is no longer listed as correct. |
| S30-B2-Q1 | revised | B02 | prompt, correct_answer, grading_note, skill | Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated. |
| S30-B2-Q2 | revised | B02 | prompt, correct_answer, skill | Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated. |
| S30-B2-Q3 | revised | B02 | prompt, choices, correct_answer, skill | Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated. |
| S30-B2-Q4 | revised | B02 | prompt, skill | Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated. |
| S30-B2-Q5 | revised | B02 | prompt, grading_note, skill | Each item checks the answer to a two-step word problem by rounding, with the numbers to round named; branch title updated. |
| S30-F2-Q1 | revised | F06 | prompt, correct_answer, grading_note | Students name the quantities and units a model needs instead of computing or naming a unit. |
| S30-F2-Q2 | revised | F06 | prompt, correct_answer, grading_note | Students name the quantities and units a model needs instead of computing or naming a unit. |
| S31-M-Q1 | revised | C08 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S31-F2-Q2 | revised | C12 | prompt | States m ≠ 0, b > 0, r > 0, or real x ≥ 0 as needed. |
| S31-F2-Q3 | revised | C12 | prompt | States m ≠ 0, b > 0, r > 0, or real x ≥ 0 as needed. |
| S31-F2-Q4 | revised | C12 | prompt | States m ≠ 0, b > 0, r > 0, or real x ≥ 0 as needed. |
| S32-M-Q1 | revised | C08 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. |
| S32-F2-Q1 | revised | C09 | prompt, correct_answer, grading_note | Asks for all solutions; the key lists both roots and says both are required (either order or set notation). |
| S32-F2-Q2 | revised | C09 | prompt, correct_answer, grading_note | Asks for all solutions; the key lists both roots and says both are required (either order or set notation). |
| S33-M-Q1 | revised | V05 | type, prompt, correct_answer, required_method | Arithmetic and algebraic solutions of the same problem, with the steps compared. |
| S33-M-Q2 | revised | V05 | type, prompt, correct_answer, required_method | Arithmetic and algebraic solutions of the same problem, with the steps compared. |
| S33-M-Q3 | revised | V05 | prompt | Arithmetic and algebraic solutions of the same problem, with the steps compared. |
| S33-M-Q4 | revised | V05 | type, prompt, choices, correct_letter, correct_answer, grading_note | Arithmetic and algebraic solutions of the same problem, with the steps compared. |
| S33-M-Q5 | revised | V05 | prompt, correct_letter, correct_answer, grading_note | Arithmetic and algebraic solutions of the same problem, with the steps compared. |
| S33-F2-Q1 | revised | F03 | type, prompt, correct_answer, skill, required_method | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S33-F2-Q2 | revised | F03 | prompt, correct_answer, grading_note, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S33-F2-Q3 | revised | F03 | prompt, choices, correct_answer, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S33-F2-Q4 | revised | F03 | prompt, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S33-F2-Q5 | revised | F03 | prompt, grading_note, skill | A complete solution with a reason for each step, finding an invalid step, and steps that change the solution set; branch title updated. |
| S34-M-Q1 | revised | C08, V06 | correct_answer, grading_note | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. The solution is stated as whole numbers of pairs from 0 to 8. |
| S34-M-Q2 | revised | V06 | prompt, correct_answer, grading_note | An inequality word problem with a solution stated in context. |
| S34-M-Q3 | revised | V06 | prompt, choices, correct_answer | An inequality word problem with a solution stated in context. |
| S34-M-Q4 | revised | V06 | prompt | An inequality word problem with a solution stated in context. |
| S34-M-Q5 | revised | V06 | prompt, grading_note | An inequality word problem with a solution stated in context. |
| S35-M-Q1 | revised | V06 | type, prompt, correct_answer, grading_note, figure, drawing_answer | Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count). |
| S35-M-Q2 | revised | V06 | prompt, correct_answer, grading_note, figure, drawing_answer | Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count). |
| S35-M-Q3 | revised | V06 | prompt, choices, correct_answer, figure | Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count). |
| S35-M-Q4 | revised | V06 | type, prompt, correct_answer, grading_note, figure, drawing_answer | Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count). |
| S35-M-Q5 | revised | V06 | prompt, figure | Each item solves an inequality from a situation and graphs or reads the graph in context (whole numbers where the quantity is a count). |
| S37-M-Q1 | revised | V02 | type, prompt, correct_answer, figure | An actual redrawing at a new scale on the grid, so all five items reproduce a scale drawing. |
| S37-M-Q3 | revised | V02 | type, prompt, choices, correct_letter, correct_answer, figure | An actual redrawing at a new scale on the grid, so all five items reproduce a scale drawing. |
| S37-M-Q4 | revised | V02 | type, prompt, choices, correct_letter, correct_answer, figure | An actual redrawing at a new scale on the grid, so all five items reproduce a scale drawing. |
| S37-M-Q5 | revised | V02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | An actual redrawing at a new scale on the grid, so all five items reproduce a scale drawing. |
| S38-M-Q3 | revised | V02 | type, prompt, choices, correct_letter, correct_answer, figure | An actual triangle drawing on the grid; triangle existence stays in S39. |
| S38-M-Q5 | revised | V02 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure | An actual triangle drawing on the grid; triangle existence stays in S39. |
| S38-F2-Q1 | revised | F07 | type, prompt, correct_answer, figure | Actual constructions on a given segment or angle: perpendicular bisector, equilateral triangle, angle bisector, and copying a segment. |
| S38-F2-Q2 | revised | F07 | type, prompt, correct_answer, figure | Actual constructions on a given segment or angle: perpendicular bisector, equilateral triangle, angle bisector, and copying a segment. |
| S38-F2-Q3 | revised | F07 | type, prompt, choices, correct_letter, correct_answer, figure | Actual constructions on a given segment or angle: perpendicular bisector, equilateral triangle, angle bisector, and copying a segment. |
| S38-F2-Q4 | revised | F07 | type, prompt, choices, correct_letter, correct_answer, figure | Actual constructions on a given segment or angle: perpendicular bisector, equilateral triangle, angle bisector, and copying a segment. |
| S38-F2-Q5 | revised | F07 | prompt, grading_note | Says "in a compass-and-straightedge construction"; still False. |
| S39-M-Q1 | revised | C13 | prompt | Defines different triangles as noncongruent triangles; position and orientation do not matter. |
| S39-M-Q2 | revised | C13 | prompt | Defines different triangles as noncongruent triangles; position and orientation do not matter. |
| S39-M-Q3 | revised | C13 | prompt | Defines different triangles as noncongruent triangles; position and orientation do not matter. |
| S39-M-Q5 | revised | C13 | prompt | Defines different triangles as noncongruent triangles; position and orientation do not matter. |
| S39-F2-Q1 | revised | F08 | prompt, correct_answer, skill | Explains SAS, SSS, and ASA by following rigid motions; branch title updated. |
| S39-F2-Q2 | revised | F08 | prompt, correct_answer, skill | Explains SAS, SSS, and ASA by following rigid motions; branch title updated. |
| S39-F2-Q3 | revised | F08 | prompt, choices, correct_answer, skill | Explains SAS, SSS, and ASA by following rigid motions; branch title updated. |
| S39-F2-Q4 | revised | F08 | prompt, skill | Explains SAS, SSS, and ASA by following rigid motions; branch title updated. |
| S39-F2-Q5 | revised | F08 | prompt, grading_note, skill | Explains SAS, SSS, and ASA by following rigid motions; branch title updated. |
| S40-M-Q2 | revised | C13 | prompt | Each plane cuts through the solid's interior (strictly between base and apex; through the axis of a right circular cone). |
| S40-M-Q4 | revised | C13 | prompt | Each plane cuts through the solid's interior (strictly between base and apex; through the axis of a right circular cone). |
| S40-F2-Q1 | revised | C13 | prompt | Each plane cuts through the solid's interior (strictly between base and apex; through the axis of a right circular cone). |
| S40-F2-Q2 | revised | C13 | prompt | Each plane cuts through the solid's interior (strictly between base and apex; through the axis of a right circular cone). |
| S40-F2-Q3 | revised | C13 | prompt | Each plane cuts through the solid's interior (strictly between base and apex; through the axis of a right circular cone). |
| S41-F2-Q4 | revised | F14 | type, prompt, choices, correct_letter, correct_answer | Explain why an arc length or sector area is n/360 of the whole circle's circumference or area. |
| S42-F2-Q4 | revised | F14 | type, prompt, choices, correct_letter, correct_answer | Explain why an arc length or sector area is n/360 of the whole circle's circumference or area. |
| S43-M-Q1 | revised | V14 | prompt, figure | Shows the circle cut into wedges and rearranged; Q2 asks for the complete argument that the area is πr². |
| S43-M-Q2 | revised | V14 | type, prompt, correct_answer, figure, required_method | Shows the circle cut into wedges and rearranged; Q2 asks for the complete argument that the area is πr². |
| S43-B1-Q3 | revised | C04 | prompt | The cut runs from a top corner straight down to the base at a right angle, and the triangle slides to the other end; the answer is a rectangle. |
| S43-F1-Q1 | revised | C09 | prompt, correct_answer, grading_note | Asks for all solutions; the key lists both roots and says both are required (either order or set notation). |
| S44-M-Q1 | revised | V07 | prompt, correct_answer, grading_note, figure | Writes and solves an equation from a labeled angle figure. |
| S44-M-Q2 | revised | C08, V07 | prompt, correct_answer, grading_note, figure | The key and grading note require both a valid equation (or inequality) and the correct solution; any valid model is accepted. Writes and solves an equation from a labeled angle figure. |
| S44-M-Q4 | revised | V07 | prompt, grading_note, figure | Writes and solves an equation from a labeled angle figure. |
| S44-M-Q5 | revised | V07 | prompt, grading_note, figure | Writes and solves an equation from a labeled angle figure. |
| S44-F2-Q1 | revised | F09 | type, prompt, correct_answer, figure, skill, required_method | Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated. |
| S44-F2-Q2 | revised | F09 | type, prompt, correct_answer, figure, skill, required_method | Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated. |
| S44-F2-Q3 | revised | F09 | prompt, choices, figure, skill | Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated. |
| S44-F2-Q4 | revised | F09 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure, skill | Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated. |
| S44-F2-Q5 | revised | F09 | prompt, grading_note, figure, skill | Proofs with reasons about angles formed by parallel lines, using a labeled figure; branch title updated. |
| S45-M-Q2 | revised | V07 | prompt, correct_answer, grading_note, figure | Writes and solves an equation from a labeled figure of intersecting lines. |
| S45-M-Q3 | revised | V07 | prompt, choices, correct_answer, figure | Writes and solves an equation from a labeled figure of intersecting lines. |
| S45-M-Q4 | revised | V07 | prompt, grading_note, figure | Writes and solves an equation from a labeled figure of intersecting lines. |
| S45-M-Q5 | revised | V07 | prompt, grading_note, figure | Writes and solves an equation from a labeled figure of intersecting lines. |
| S45-F2-Q2 | revised | F09 | type, prompt, correct_answer, figure, required_method | Proofs with reasons that vertical angles are congruent, built from linear pairs. |
| S45-F2-Q3 | revised | F09 | prompt, choices, correct_answer | Proofs with reasons that vertical angles are congruent, built from linear pairs. |
| S45-F2-Q4 | revised | F09 | type, prompt, choices, correct_letter, correct_answer, grading_note | Proofs with reasons that vertical angles are congruent, built from linear pairs. |
| S45-F2-Q5 | revised | F09 | prompt, grading_note | Proofs with reasons that vertical angles are congruent, built from linear pairs. |
| S46-M-Q3 | revised | V12 | prompt, choices, correct_answer | A composite rectangle-and-triangle area replaces a single trapezoid. |
| S46-F2-Q1 | revised | F13 | prompt, correct_answer, grading_note | Modeling items estimate with a model and judge whether the model fits. |
| S46-F2-Q3 | revised | F13 | prompt, choices, correct_answer | Modeling items estimate with a model and judge whether the model fits. |
| S46-F2-Q4 | revised | F13 | prompt | Modeling items estimate with a model and judge whether the model fits. |
| S46-F2-Q5 | revised | F13 | prompt, grading_note | Modeling items estimate with a model and judge whether the model fits. |
| S48-F1-Q3 | revised | C03 | prompt | Says the pyramid is a right square pyramid with its top vertex above the center of the base; still 5 m. |
| S52-M-Q1 | revised | C07 | prompt, correct_answer, figure | Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified. |
| S52-M-Q2 | revised | C07 | prompt, correct_answer, grading_note, figure | Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified. |
| S52-M-Q3 | revised | C07 | prompt, choices, correct_answer, figure | Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified. |
| S52-M-Q4 | revised | C07 | prompt, figure | Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified. |
| S52-M-Q5 | revised | C07 | prompt, grading_note, figure | Each item shows paired dot plots (each set has the stated mean and a MAD of 2, checked from the data); students describe the overlap they see and the difference in MADs. General rules are qualified. |
| S53-M-Q1 | revised | V13 | prompt, correct_answer, grading_note | Draws a population inference from both center and spread, stated as a tendency. |
| S53-M-Q2 | revised | V13 | prompt, correct_answer, grading_note | Draws a population inference from both center and spread, stated as a tendency. |
| S53-M-Q4 | revised | V13 | prompt | Draws a population inference from both center and spread, stated as a tendency. |
| S53-M-Q5 | revised | V13 | prompt, grading_note | Draws a population inference from both center and spread, stated as a tendency. |
| S53-F2-Q2 | revised | C10 | prompt, correct_answer, grading_note | Says to round a mean that does not end to the nearest tenth: 11.2 and 5.4; exact 67/6 and 27/5 accepted. |
| S54-F2-Q1 | revised | F10 | prompt, correct_answer, skill | Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated. |
| S54-F2-Q2 | revised | F10 | prompt, correct_answer, skill | Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated. |
| S54-F2-Q3 | revised | F10 | prompt, choices, correct_answer, skill | Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated. |
| S54-F2-Q4 | revised | F10 | prompt, skill | Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated. |
| S54-F2-Q5 | revised | F10 | prompt, grading_note, skill | Unions, intersections, and complements of overlapping events on cards 1 to 10; branch title updated. |
| S55-M-Q4 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S56-M-Q1 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S56-B1-Q2 | revised | B01 | prompt | Uses 8/12 (Grade 4 denominators) instead of 10/15; still 2/3. |
| S56-B2-Q3 | revised | B01 | choices | The distractor 3/7 is now 3/6 (Grade 3 denominators). |
| S56-B2-Q4 | revised | B01 | prompt | One of 6 equal parts is 1/6 (Grade 3 denominators); still True. |
| S56-F1-Q1 | revised | F13 | prompt, correct_answer, skill | Uses a probability model as a function from outcomes to probabilities; branch title updated. |
| S56-F1-Q2 | revised | F13 | prompt, correct_answer, skill | Uses a probability model as a function from outcomes to probabilities; branch title updated. |
| S56-F1-Q3 | revised | F13 | prompt, choices, correct_answer, skill | Uses a probability model as a function from outcomes to probabilities; branch title updated. |
| S56-F1-Q4 | revised | F13 | skill | Uses a probability model as a function from outcomes to probabilities; branch title updated. |
| S56-F1-Q5 | revised | F13 | skill | Uses a probability model as a function from outcomes to probabilities; branch title updated. |
| S56-F2-Q3 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S57-F1-Q1 | revised | F11 | type, prompt, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S57-F1-Q2 | revised | F11 | type, prompt, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S57-F1-Q3 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S57-F1-Q4 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S57-F1-Q5 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S58-M-Q1 | revised | V12 | prompt, correct_answer, grading_note | Gives an observed count (14 fives) and asks for the comparison with the expected 10. |
| S58-M-Q2 | revised | C05 | prompt | The coin is claimed to be fair, so chance variation or an unfair coin are both valid explanations. |
| S58-F2-Q1 | revised | F12 | prompt, correct_answer, figure, skill | Results are judged against a dot plot of 50 simulated results under the model; branch title updated. |
| S58-F2-Q2 | revised | F12 | prompt, correct_answer, figure, skill | Results are judged against a dot plot of 50 simulated results under the model; branch title updated. |
| S58-F2-Q3 | revised | F12 | prompt, choices, correct_answer, figure, skill | Results are judged against a dot plot of 50 simulated results under the model; branch title updated. |
| S58-F2-Q4 | revised | F12 | prompt, figure, skill | Results are judged against a dot plot of 50 simulated results under the model; branch title updated. |
| S58-F2-Q5 | revised | F12 | prompt, grading_note, figure, skill | Results are judged against a dot plot of 50 simulated results under the model; branch title updated. |
| S59-M-Q1 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-M-Q2 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-M-Q3 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-M-Q4 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-M-Q5 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-B2-Q1 | revised | B04 | prompt, figure, skill | Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated. |
| S59-B2-Q2 | revised | B04 | prompt, figure, skill | Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated. |
| S59-B2-Q3 | revised | B04 | prompt, skill | Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated. |
| S59-B2-Q4 | revised | B04 | skill | Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated. |
| S59-B2-Q5 | revised | B04 | prompt, grading_note, skill | Pairs are counted with an array: one row for each first choice and one column for each second choice; branch title updated. |
| S59-F2-Q2 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S59-F2-Q3 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S60-M-Q2 | revised | V10 | prompt, correct_answer, grading_note | Students make a complete organized list, tree diagram, or table, and identify an event in it. |
| S60-M-Q3 | revised | V10 | type, prompt, choices, correct_letter, correct_answer, figure | Students make a complete organized list, tree diagram, or table, and identify an event in it. |
| S60-M-Q4 | revised | V10 | type, prompt, choices, correct_letter, correct_answer, figure | Students make a complete organized list, tree diagram, or table, and identify an event in it. |
| S60-M-Q5 | revised | V10 | type, prompt, choices, correct_letter, correct_answer, grading_note | Students make a complete organized list, tree diagram, or table, and identify an event in it. |
| S60-F1-Q1 | revised | F11 | type, prompt, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S60-F1-Q2 | revised | F11 | type, prompt, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S60-F1-Q3 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S60-F1-Q4 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S60-F1-Q5 | revised | F11 | type, prompt, choices, correct_letter, correct_answer, grading_note, figure, skill | Students fill in a blank two-way table from survey counts (five constructions); branch title updated. |
| S60-F2-Q2 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S60-F2-Q3 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S60-F2-Q4 | revised | C11 | prompt | States P(B) > 0 for the conditional-probability rule. |
| S61-M-Q1 | revised | C11 | prompt | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S61-M-Q2 | revised | V11 | prompt, correct_answer, grading_note | Runs a simulation with given random digits: group the digits into trials, count successes, and estimate the probability. |
| S61-M-Q3 | revised | C11 | prompt, choices, correct_answer | States fair coins, fair cubes numbered 1 to 6, a fair pointer, and independent trials. |
| S61-M-Q4 | revised | V11 | type, prompt, choices, correct_letter, correct_answer, grading_note | Runs a simulation with given random digits: group the digits into trials, count successes, and estimate the probability. |
| S61-M-Q5 | revised | V11 | prompt, grading_note | Runs a simulation with given random digits: group the digits into trials, count successes, and estimate the probability. |
| S61-B2-Q5 | revised | B01 | prompt | Compares 3/8 and 4/8 (Grade 3 denominators); still False. |
| S61-F2-Q1 | revised | C06 | prompt, correct_answer | States that similar plants were randomly assigned to plant food or none and that the re-randomizations simulate no effect; the key says evidence, not proof. |
| S61-F2-Q2 | revised | C06 | prompt, correct_answer | States that similar plants were randomly assigned to plant food or none and that the re-randomizations simulate no effect; the key says evidence, not proof. |
| S62-M-Q1 | new | V01 |  | Moved unchanged from S9-M-Q1. New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-M-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-M-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-M-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-M-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-B2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S62-F2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a tip and the total cost with the tip. |
| S63-M-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-M-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-M-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-M-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-M-Q5 | new | V01 |  | Moved unchanged from S9-M-Q5. New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-B2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S63-F2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find sales tax and the final cost with tax. |
| S64-M-Q1 | new | V01 |  | Moved unchanged from S10-M-Q2. New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-M-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-M-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-M-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-M-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-B2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S64-F2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a commission and pay that includes a commission. |
| S65-M-Q1 | new | V01 |  | Moved unchanged from S10-M-Q3. New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-M-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-M-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-M-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-M-Q5 | new | V01 |  | Moved unchanged from S10-M-Q5. New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-B2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S65-F2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — find a percent fee and the total with the fee. |
| S66-M-Q1 | new | V01 |  | Moved unchanged from S9-M-Q2. New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-M-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-M-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-M-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-M-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-B2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F1-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F1-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F1-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F1-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F1-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F2-Q1 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F2-Q2 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F2-Q3 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F2-Q4 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S66-F2-Q5 | new | V01 |  | New focused set: 7.RP.A.3 — multistep percent problems that combine a discount with tax or a tip. |
| S67-M-Q1 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-M-Q2 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-M-Q3 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-M-Q4 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-M-Q5 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B1-Q1 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B1-Q2 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B1-Q3 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B1-Q4 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B1-Q5 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B2-Q1 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B2-Q2 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B2-Q3 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B2-Q4 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-B2-Q5 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F1-Q1 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F1-Q2 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F1-Q3 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F1-Q4 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F1-Q5 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F2-Q1 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F2-Q2 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F2-Q3 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F2-Q4 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S67-F2-Q5 | new | V08 |  | New focused set: 7.G.B.6 — volume of solids made of right prisms, with 3-D diagrams. |
| S68-M-Q1 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-M-Q2 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-M-Q3 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-M-Q4 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-M-Q5 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B1-Q1 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B1-Q2 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B1-Q3 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B1-Q4 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B1-Q5 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B2-Q1 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B2-Q2 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B2-Q3 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B2-Q4 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-B2-Q5 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F1-Q1 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F1-Q2 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F1-Q3 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F1-Q4 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F1-Q5 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F2-Q1 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F2-Q2 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F2-Q3 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F2-Q4 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S68-F2-Q5 | new | V08 |  | New focused set: 7.G.B.6 — exterior surface area of solids made of right prisms (shared faces not counted). |
| S69-M-Q1 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-M-Q2 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-M-Q3 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-M-Q4 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-M-Q5 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B1-Q1 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B1-Q2 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B1-Q3 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B1-Q4 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B1-Q5 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B2-Q1 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B2-Q2 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B2-Q3 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B2-Q4 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-B2-Q5 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F1-Q1 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F1-Q2 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F1-Q3 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F1-Q4 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F1-Q5 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F2-Q1 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F2-Q2 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F2-Q3 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F2-Q4 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S69-F2-Q5 | new | V09 |  | New focused set: 7.SP.A.2 — generate several same-size random samples with random digits and see how the estimates vary. |
| S70-M-Q1 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-M-Q2 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-M-Q3 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-M-Q4 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-M-Q5 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B1-Q1 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B1-Q2 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B1-Q3 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B1-Q4 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B1-Q5 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B2-Q1 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B2-Q2 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B2-Q3 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B2-Q4 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-B2-Q5 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F1-Q1 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F1-Q2 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F1-Q3 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F1-Q4 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F1-Q5 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F2-Q1 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F2-Q2 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F2-Q3 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F2-Q4 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
| S70-F2-Q5 | new | V09 |  | New focused set: 7.SP.C.6 — collect data from a chance process (given digits, recorded flips, or the student's own rolls) and estimate a probability. |
