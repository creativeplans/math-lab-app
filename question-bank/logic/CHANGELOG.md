# Logic collection: change log

## Version 1.1.0 (2026-10-25)

Corrections from the review of version 1.0.0. Question IDs are unchanged; no question was added or retired. Every
section still has 5 questions. Page numbers were regenerated (see `pdf/PART_INDEX.md` and the `question_page` field).

### Answer choices with more than one defensible answer

| ID | Change | How it was rechecked |
|---|---|---|
| S8-F1-Q5 | Replaced the choice "P is false or Q is false" (which also follows) with "P is true or Q is true". | Every choice evaluated at P = false, Q = false: only the key holds as a conclusion. |
| S54-F1-Q2 | Prompt now asks which next weighing is sure to identify the heavy coin. Replaced "a left-side coin against a right-side coin" (which also works) with "a right-side coin against a coin left off the scale" (both genuine). | Each choice traced against both possible heavy coins. |
| S42-F2-Q5 | Replaced "2 to the power -1 is greater than -1" (also a valid reason) with "2 to the power -1 is undefined" (false: it is 1/2). Solution notes both reasons. | Reviewed by the author. |
| S3-F2-Q2 | Replaced "84 is divisible by 4" (which also shows 84 is even) with "84 is divisible by 7". | Reviewed by the author. |

### Rule-graded answers (values): stated domain now enforced

The values constructor now reads the number domain from each question's wording (whole number: integer 0 or more;
positive whole number or "from 1": integer 1 or more; integer: integer; otherwise real) and joins it to the packaged
rule. All 95 values questions were rebuilt this way. Among them, the reviewer's examples now fail:
S8-M-Q4, S12-F2-Q5, S13-F1-Q1, S13-F2-Q5, S15-F2-Q2, S16-F1-Q5, S16-F2-Q4, S22-M-Q4, S29-M-Q2, S29-F1-Q5, S29-F2-Q3,
S42-F1-Q1.

| ID | Additional change |
|---|---|
| S29-F2-Q3 | Rule now bounds each of a, b, c to 1 to 20. |
| S29-M-Q4, S42-F1-Q1 | Rule is now the exact condition "a is not 0 and b is not 0" (since (a + b) squared - (a squared + b squared) = 2ab), so no cancellation can reject a true counterexample. The solutions explain this. S29-M-Q4 now asks for integers: the game treats numbers within 0.000000001 of each other as equal, so a tiny nonzero real such as 10 to the power -20 would be read as 0. Integers avoid that, and they are still real numbers, so the counterexample is valid. |
| S40-M-Q5 | Explicitly real (the answer is 7.5), so no integer condition is added. |

### Ordering questions: every valid order accepted

| ID | Change |
|---|---|
| S21-M-Q3 | The grader now accepts all 8 orders allowed by the dependencies (D after A and C; E last, after B and D). It accepted 3 before. |
| S43-M-Q5 | The vertical-angles step does not need the given, so 3 orders are valid (it accepted 2). The prompt now says each step may use only lines placed before it. |
| S3-F2-Q4 | The prompt now states the intended presentation order (dam rule before river rule, conclusion last); the 3 orders allowed by that wording are accepted. |

All 39 ordering questions were reread against their dependency rules; the others already accepted every valid order.

### Under-determined questions and missing domains

| ID | Change |
|---|---|
| S1-F1-Q4 | Added "Add as few shaded cells as possible", so the 16-cell completion is the only answer. |
| S2-M-Q3, S2-F1-Q3 | Each family now has at least one son and at least one daughter. |
| S27-B2-Q3 | Now about an integer n, so "not even" is "odd". |
| S20-M-Q5 | "Square cards" changed to "Rectangular cards" (card D is 3 by 4). |
| S48-F1-Q4 | Now says the turned display must be a two-digit number not starting with 0. The key changed from 30 to 25 (computed). |

### Deduction, validity and assumptions

| ID | Change |
|---|---|
| S10-F1-Q3 | Now "A VALID deductive argument with true premises can have a false conclusion" (still False). |
| S10-M-Q1 | Now asks for a valid deductive argument; the S10 prerequisite description no longer equates deduction with certainty. |
| S46 (definition) | Assumptions are now defined as bridging (makes the conclusion follow) or supporting (makes it more likely). |
| S46-M-Q1, S46-M-Q2, S46-F1-Q4, S46-F2-Q2 | Now ask which assumption most supports or strengthens the prediction or explanation; the keys and explanations no longer claim strict necessity. S46-M-Q2's key is now "watered and kept as warm as before". S46-F1-Q4's key is now "Friday's game will be like those rainy games in the ways that mattered". |
| S46-M-Q5 | Now "A major change in how the bridge is used could weaken this argument" (True). |
| S46 B1 lesson | Distinguishes bridging, supporting and necessary assumptions; the piano example is now a supporting assumption. |

### Self-contained questions

| ID | Change |
|---|---|
| S50-F2-Q2, S50-F2-Q3 | Both now repeat the full clinic data (mild and severe cases and recoveries for each clinic). |
| S50-F2-Q5 | Now begins "Of 590 people who test positive for a condition, 95 actually have it". |

### Smaller teaching fixes

| ID | Change |
|---|---|
| S25 B1 lesson, S25-M-Q4 solution | A neighboring swap changes the out-of-order count by exactly one (not "fixes one pair"). |
| S52 rule family (all S52 questions) | The terms shown may fit more than one rule type; rule (3) needs a nonzero growth. |
| S1-M-Q1 | Now says "reflected left to right in a vertical mirror line" instead of relying on a drawn dashed line. |
| S10-B2-Q1 | Replaced the near-duplicate of S10-B2-Q2 with a different item (the sun-rising argument is inductive; False). |
| S13-B2-Q1 | Replaced the near-duplicate of S13-B2-Q2 with a necessary-condition item (concert ticket; True). |
| S21-B2-Q1 | Replaced the near-duplicate of S21-B2-Q2 with "P or Q is true and Q is false, so P is true" (True). |
| S21-F1-Q1 | All three premises are now about the same day. |

### New permanent checks

- The values constructor tests negative and fractional probes against the packaged rule, and validate.py repeats this on
  the built package for every values question.
- validate.py's self-containment check now catches any "the ... above" reference.
- The ordering limit was raised so that every order a dependency rule allows is accepted (up to 12).
