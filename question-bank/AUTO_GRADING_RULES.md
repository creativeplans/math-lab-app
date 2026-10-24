# Authoring rule: every question is graded automatically

This rule applies to every collection written for Untangle The Nexus from Algebra II 1.2.0 on, including future
Geometry work. It covers the MAIN question and every backward and forward branch.

**No question may need a person to grade it.** Nobody inspects a drawing, a proof, an explanation, or shown work. Every
question is multiple choice, true/false, or a short answer that the game's own answer checker
(`packages/curriculum/src/answers.ts` in the game repository) accepts.

## Choosing the response type

| The skill | Response type |
|---|---|
| Graphing, constructing, sketching | Multiple choice with diagram or graph choices: four candidate figures labeled A to D on one window, the others showing specific errors |
| Proving, deriving, explaining, interpreting, evaluating a claim | Multiple choice: one complete, correct argument against specifically flawed ones (an example check, an invalid step, circular reasoning, a false fact, the wrong direction) |
| A number, a value, a short expression the checker compares reliably | Short answer, with the contract below |
| A formula with radicals, logarithms, trigonometric functions or inverse-function notation, an interval statement, a domain in words | Multiple choice, or ask for numeric parameters (for example "f⁻¹(x) = ∛(x - a) + b; give a and b") |
| A word answer | Only from a closed set the question lists ("Answer Yes or No", "Answer Positive or Negative", "enter none if there are none") |

## Short-answer contract

- **One answer line per part.** Each line has its own label; the key has one part per line, separated by semicolons.
- **The question states the form and precision**: exact, a + bi, factored, "to the nearest hundredth", "as a fraction",
  "in dollars". A rounded answer must be given to exactly the stated precision.
- **The key is only the answer.** No "about", "≈", "for example", "(that is ...)", worked steps or units commentary in
  the key; those belong in the grading note.
- **Lists** (solutions, excluded values) use a set key such as `{-3, 2}`, so any order is accepted.
- **Expressions** are written in standard order (`7x - 4`, not `-4 + 7x`), with `^` for exponents in variables and `·`
  between adjacent letters (`2a·b`).
- **Words the checker infers from the prompt** ("simplify", "expand", "factor", "as a product") apply to every line of
  the question; do not mix a numeric line with a factored line in one question.
- **"Rewrite" items** where the original expression would also be accepted (for example "combine into one fraction") ask
  for a specific part instead (the numerator over a stated denominator) or become multiple choice.

## Every question

- **Stands alone.** It states every given it needs (model, distribution, independence, fair devices, null model, tail,
  cutoff, margin-of-error convention, domain assumptions); it never refers to another question.
- **Has exactly one defensible answer.** Each multiple-choice item has one correct option, and its grading note says what
  is wrong with each other option. Each true/false statement has one truth value under the conditions it states.
- **Has no answer cue.** The correct choice is not much longer than the others, and letters stay balanced.
- **Is recorded honestly in coverage.** When the standard asks students to produce something (construct, prove, sketch)
  and the question asks them to choose, the coverage matrix says so (assessed response: recognition).

## Checks that enforce it (Algebra II)

`algebra2/src/validate.py` checks 19, 21, 22 and 23: response types; every short answer run through the game's checker
(`algebra2/src/tools/checker_contract.ts`, including the answer rewritten without spaces and with terms reversed); clean
keys and listed word options; and the multiple-choice length cue. The checks show that the content files meet the rule.
They are not a test in the live game or with the AI grader.
