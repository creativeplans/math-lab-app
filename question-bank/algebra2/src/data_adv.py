"""ADVANCED EXTENSION (+): N-CN.3, F-IF.7d, F-BF.1c, F-BF.4b-d, F-BF.5, F-TF.3, 4, 6, 7 (sets 73-84).
These sets are optional for the core course; they carry strand='advanced'."""
import math

from qb import S, B, sa, mc, tf, plot
from common import why, proof, PR, EXP, blank, graph, tbl, pick, cand

TECH = ' A calculator may be used.'


def grid(x=(-6, 6), y=(-6, 6), xstep=1, ystep=1):
    return blank(x=x, y=y, xstep=xstep, ystep=ystep, desc='Blank coordinate grid, x from %s to %s and y from %s to %s.' % (x[0], x[1], y[0], y[1]))


RG = 'Graph the rational function on the grid. Show every zero, the y-intercept, each vertical asymptote and the horizontal asymptote (dashed lines), and the behavior near each asymptote.\n'

SETS = [
    # ------------------------------------------------------------------ 73. CN.A.3 conjugates, moduli, quotients
    S('HSN-CN.A.3', 'Use conjugates to find moduli and quotients of complex numbers',
      target='Find the conjugate of a complex number and use it to find the modulus and to write quotients in the form a + bi', strand='advanced', covers=['CN3-conj'],
      main=[
          sa('Give the conjugate of 3 - 4i and find |3 - 4i|.', ['Conjugate:', '|3 - 4i| ='], key='3 + 4i; 5', note='Form required: both. √(9 + 16) = 5.'),
          sa('Write (2 + 3i)/(1 - i) in the form a + bi.', 'Answer:', key='-1/2 + (5/2)i', note='Form required: a + bi. Multiply by (1 + i)/(1 + i).'),
          sa('Write (5 + i)/(2 + 3i) in the form a + bi.', 'Answer:', key='1 - i', note='Form required: a + bi. (5 + i)(2 - 3i)/13 = (13 - 13i)/13.'),
          sa('Find |-5 + 12i| and compute (-5 + 12i)(-5 - 12i).', ['|-5 + 12i| =', 'Product:'], key='13; 169', note='Form required: both. √(25 + 144) = 13; the product is 25 + 144 = 13².'),
          sa('Write 1/(4 + 3i) in the form a + bi.', 'Answer:', key='4/25 - (3/25)i', note='Form required: a + bi.'),
      ],
      back=[
          B('Multiply complex numbers', 'HSN-CN.A.2', [
              sa('Multiply (2 + 3i)(1 + i).', 'Answer:', key='-1 + 5i', note='Form required: a + bi.'),
              sa('Multiply (3 - 4i)(3 + 4i).', 'Answer:', key='25', note='Any equivalent form.'),
              tf('(a + bi)(a - bi) = a² + b².', key=True, note='-b²i² = b².'),
              mc('(5 + i)(2 - 3i) equals', ['13 - 13i', '10 - 3i', '7 - 13i', '13 + 13i'], note='10 - 15i + 2i + 3.'),
              sa('Multiply (1 - i)(1 + i).', 'Answer:', key='2', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot multiply by the conjugate.', 'division multiplies by the conjugate.', 'multiplies complex numbers.')),
          B('Distance from the origin', '8.G.B.8', [
              sa('Find the distance from (0, 0) to (3, -4).', 'Answer:', key='5', note='Any equivalent form.'),
              sa('Find the distance from (0, 0) to (-5, 12).', 'Answer:', key='13', note='Any equivalent form.'),
              tf('The distance from (0, 0) to (a, b) is √(a² + b²).', key=True, note='Pythagorean Theorem.'),
              mc('The distance from (0, 0) to (1, 1) is', ['√2', '2', '1', '0'], note='√(1 + 1).'),
              sa('Find the distance from (0, 0) to (4, 3).', 'Answer:', key='5', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student does not see the modulus as distance.', '|a + bi| is the distance to (a, b).', 'finds distances.')),
          B('Powers of i', 'HSN-CN.A.1', [
              sa('Simplify i².', 'Answer:', key='-1', note='Any equivalent form.'),
              sa('Simplify -12i · i.', 'Answer:', key='12', note='Any equivalent form.'),
              tf('-3i² = -3.', key=False, note='i² = -1, so -3i² = 3.'),
              mc('Which is real?', ['(4 + 3i)(4 - 3i)', '(4 + 3i)²', '4 + 3i', '3i'], note='Conjugate product.'),
              sa('Write 13/13 - 13i/13 in the form a + bi.', 'Answer:', key='1 - i', note='Form required: a + bi.'),
          ], align='supporting',
            why=why('the student keeps i² terms.', 'conjugate products become real using i² = -1.', 'simplifies powers of i.')),
      ],
      f1=B('Prove properties of conjugates and moduli', 'HSN-CN.A.3', [
          mc('Which argument proves z · z̄ = |z|² for z = a + bi (a and b real)?', [
              '(a + bi)(a - bi) = a² - b²i² = a² + b², and |z|² = a² + b².',
              '(a + bi)(a - bi) = a² - b², and |z|² = a² - b².',
              'For z = 3 + 4i: (3 + 4i)(3 - 4i) = 25 = 5², so the statement holds.',
              '(a + bi)(a - bi) = a² + b²i², which is |z|² because |z| = √(a² + b²i²).'],
             note='Multiply, use i² = -1, and compare with |z| = √(a² + b²). The others forget i² = -1 (and misstate |z|), check one example, or expand with a sign error.'),
          sa('Let z = 3 + 4i and w = 1 + i. Find zw, |zw|, and |z||w|, giving the moduli exactly in simplest radical form.', ['zw =', '|zw| =', '|z||w| ='], key='-1 + 7i; 5√2; 5√2',
             note='Form required: all three. zw = 3 + 3i + 4i + 4i² = -1 + 7i; |zw| = √50 = 5√2; |z||w| = 5 · √2.'),
          tf('The conjugate of a real number is itself.', key=True, note='b = 0.'),
          mc('If z = 2 - 5i, then z + z̄ is', ['4', '-10i', '4 - 10i', '0'], note='2a.'),
          sa('Use z̄/|z|² to write 1/z for z = 1 + 2i in the form a + bi.', 'Answer:', key='1/5 - (2/5)i', note='Form required: a + bi. z̄/|z|² = (1 - 2i)/5.'),
      ], prog='same-course deepening', demand='Prove and use general identities for conjugates and moduli.'),
      f2=B('Write complex numbers in polar form', 'HSN-CN.B.4', [
          sa('Write 1 + i in polar form r(cos θ + i sin θ) with 0 ≤ θ < 2π. Give r and θ exactly.', ['r =', 'θ ='], key='√2; π/4', note='Form required: both. r = √(1 + 1); θ = π/4 (first quadrant, equal parts).'),
          sa('Write 2(cos(π/2) + i sin(π/2)) in rectangular form.', 'Answer:', key='2i', note='Any equivalent form.'),
          tf('The modulus of a complex number is the r in its polar form.', key=True, note='Distance.'),
          mc('The polar form of -3 is', ['3(cos π + i sin π)', '3(cos 0 + i sin 0)', '-3(cos π + i sin π)', '3(cos(π/2) + i sin(π/2))'], note='Angle π.'),
          mc('In the complex plane, what do the modulus and the angle of a complex number represent?', [
              'The modulus is the distance from 0; the angle is the direction measured from the positive real axis.',
              'The modulus is the real part; the angle is the imaginary part of the number written as a + bi.',
              'The modulus is the distance from 1; the angle is measured from the positive imaginary axis.',
              'The modulus is the sum of the parts a + b; the angle is the ratio of the parts b/a.'],
             note='Polar form describes a point by its distance and direction from the origin.'),
      ], prog='later-course extension', demand='Represent complex numbers by modulus and angle (Precalculus).',
        builds='Builds on FORWARD 1: the modulus |z| becomes the radius r of the polar form.')),

    # ------------------------------------------------------------------ 74. IF.C.7.d rational graphs with asymptotes
    S('HSF-IF.C.7.d', 'Graph rational functions with zeros and asymptotes',
      target='Identify the graph of a rational function from its zeros, intercepts, vertical and horizontal asymptotes, and end behavior', strand='advanced', covers=['IF7d-asym'],
      main=[
          pick('Which graph shows y = (x + 1)/(x - 2), with its asymptotes dashed?', 'C', [
              cand([lambda x: (x + 1) / (x - 2)], 'two branches with a dashed vertical asymptote x = 2 and a dashed horizontal asymptote y = 1; zero at -1 and y-intercept -1/2; the right branch rises toward +∞ near x = 2.', vas=[2], has=[1]),
              cand([lambda x: (x - 1) / (x + 2)], 'two branches with a dashed vertical asymptote x = -2 and a dashed horizontal asymptote y = 1; zero at 1 and y-intercept -1/2.', vas=[-2], has=[1]),
              cand([lambda x: (x - 2) / (x + 1)], 'two branches with a dashed vertical asymptote x = -1 and a dashed horizontal asymptote y = 1; zero at 2 and y-intercept -2.', vas=[-1], has=[1]),
              cand([lambda x: -(x + 1) / (x - 2)], 'two branches with a dashed vertical asymptote x = 2 and a dashed horizontal asymptote y = -1; zero at -1 and y-intercept 1/2.', vas=[2], has=[-1]),
          ], 'Zero -1, y-intercept -1/2, vertical asymptote x = 2, horizontal asymptote y = 1 (ratio of leading coefficients); y → +∞ as x → 2⁺ and y → -∞ as x → 2⁻. The others show (x - 1)/(x + 2) (same y-intercept), (x - 2)/(x + 1), and the reflection.',
              x=(-6, 8), y=(-6, 6)),
          pick('Which graph shows y = 2x/(x² - 4), with its asymptotes dashed?', 'B', [
              cand([lambda x: 2 * x / (x * x - 4)], 'three branches separated by dashed vertical asymptotes x = -2 and x = 2; horizontal asymptote y = 0; the middle branch falls through the origin; the left branch is below the x-axis and the right branch above it.', vas=[-2, 2], has=[0]),
              cand([lambda x: 2 * x / (x * x + 4)], 'one smooth curve with no vertical asymptotes, through the origin, with a high point at (2, 0.5) and a low point at (-2, -0.5).', has=[0]),
              cand([lambda x: 2 * x * x / (x * x - 4)], 'three branches separated by dashed vertical asymptotes x = -2 and x = 2, with a dashed horizontal asymptote y = 2; the middle branch touches the origin from below.', vas=[-2, 2], has=[2]),
              cand([lambda x: -2 * x / (x * x - 4)], 'three branches separated by dashed vertical asymptotes x = -2 and x = 2; horizontal asymptote y = 0; the middle branch rises through the origin; the left branch is above the x-axis.', vas=[-2, 2], has=[0]),
          ], 'Zero and y-intercept 0; vertical asymptotes x = ±2 (zeros of x² - 4); horizontal asymptote y = 0 (degree of numerator < degree of denominator); e.g. y(3) = 6/5 > 0 and y(1) = -2/3 < 0. The others show 2x/(x² + 4), 2x²/(x² - 4), and the reflection.',
              x=(-6, 6), y=(-5, 5)),
          pick('Which graph shows y = (x² - 1)/(x² - 9), with its asymptotes dashed?', 'D', [
              cand([lambda x: (x * x - 1) / (x * x - 9)], 'three branches with dashed vertical asymptotes x = -3 and x = 3 and a dashed horizontal asymptote y = 1; the middle branch crosses the x-axis at -1 and 1 with y-intercept 1/9; the outer branches stay above y = 1.', vas=[-3, 3], has=[1]),
              cand([lambda x: (x * x - 9) / (x * x - 1)], 'three branches with dashed vertical asymptotes x = -1 and x = 1 and a dashed horizontal asymptote y = 1; zeros at -3 and 3; the middle branch is above the grid near x = 0.', vas=[-1, 1], has=[1]),
              cand([lambda x: (x * x + 1) / (x * x - 9)], 'three branches with dashed vertical asymptotes x = -3 and x = 3 and a dashed horizontal asymptote y = 1; no zeros; the middle branch is below the x-axis with y-intercept -1/9.', vas=[-3, 3], has=[1]),
              cand([lambda x: (x - 1) / (x - 3)], 'two branches with a dashed vertical asymptote x = 3 and a dashed horizontal asymptote y = 1; zero at 1 and y-intercept 1/3.', vas=[3], has=[1]),
          ], 'Zeros ±1, y-intercept 1/9, vertical asymptotes x = ±3, horizontal asymptote y = 1; the outer branches are above y = 1. The others show the reciprocal (x² - 9)/(x² - 1), (x² + 1)/(x² - 9), and (x - 1)/(x - 3).',
              x=(-8, 8), y=(-6, 6), xlab=2),
          pick('Which graph shows y = 3/(x + 1)², with its asymptotes dashed?', 'A', [
              cand([lambda x: 3 / (x + 1) ** 2], 'two branches above the x-axis on both sides of a dashed vertical asymptote x = -1, both rising toward +∞ near it; horizontal asymptote y = 0; y-intercept 3.', vas=[-1], has=[0]),
              cand([lambda x: 3 / (x + 1)], 'two branches on opposite sides of a dashed vertical asymptote x = -1: the left branch below the x-axis, the right branch above it; y-intercept 3.', vas=[-1], has=[0]),
              cand([lambda x: 3 / (x - 1) ** 2], 'two branches above the x-axis on both sides of a dashed vertical asymptote x = 1; y-intercept 3.', vas=[1], has=[0]),
              cand([lambda x: -3 / (x + 1) ** 2], 'two branches below the x-axis on both sides of a dashed vertical asymptote x = -1, both falling toward -∞ near it; y-intercept -3.', vas=[-1], has=[0]),
          ], 'No zeros; y-intercept 3; vertical asymptote x = -1 with y → +∞ on both sides (the square is positive); horizontal asymptote y = 0. The others show 3/(x + 1), 3/(x - 1)² (same y-intercept), and -3/(x + 1)².',
              x=(-6, 4), y=(-5, 8)),
          pick('Which graph shows y = (2x - 4)/(x + 3), with its asymptotes dashed?', 'B', [
              cand([lambda x: (2 * x - 4) / (x + 3)], 'two branches with a dashed vertical asymptote x = -3 and a dashed horizontal asymptote y = 2; zero at 2 and y-intercept -4/3.', vas=[-3], has=[2]),
              cand([lambda x: (2 * x + 4) / (x - 3)], 'two branches with a dashed vertical asymptote x = 3 and a dashed horizontal asymptote y = 2; zero at -2 and y-intercept -4/3.', vas=[3], has=[2]),
              cand([lambda x: (x - 4) / (x + 3)], 'two branches with a dashed vertical asymptote x = -3 and a dashed horizontal asymptote y = 1; zero at 4 and y-intercept -4/3.', vas=[-3], has=[1]),
              cand([lambda x: (x + 3) / (2 * x - 4)], 'two branches with a dashed vertical asymptote x = 2 and a dashed horizontal asymptote y = 1/2; zero at -3 and y-intercept -3/4.', vas=[2], has=[0.5]),
          ], 'Zero 2, y-intercept -4/3, vertical asymptote x = -3, horizontal asymptote y = 2/1 = 2. The others show (2x + 4)/(x - 3) and (x - 4)/(x + 3) (both with the same y-intercept) and the reciprocal.',
              x=(-10, 6), y=(-8, 10), xlab=2, ylab=2),
      ],
      back=[
          B('Rewrite a rational expression by inspection', 'HSA-APR.D.6', [
              sa('Rewrite (x + 1)/(x - 2) as 1 + r/(x - 2).', 'Answer:', key='1 + 3/(x - 2)', note='Form required.'),
              sa('Rewrite (2x - 4)/(x + 3) as 2 + r/(x + 3).', 'Answer:', key='2 - 10/(x + 3)', note='Form required.'),
              tf('The constant q in q + r/(x - a) is the horizontal asymptote.', key=True, note='r/(x - a) → 0.'),
              mc('(x² - 1)/(x² - 9) equals', ['1 + 8/(x² - 9)', '1 - 8/(x² - 9)', '1/9', '1 + 1/(x² - 9)'], note='x² - 1 = (x² - 9) + 8.'),
              sa('Factor the denominator of 2x/(x² - 4).', 'Answer:', key='(x - 2)(x + 2)', note='Form required: factored. The vertical asymptotes are at the zeros of these factors.'),
          ], align='exact',
            why=why('the student cannot find the horizontal asymptote.', 'the inspected form shows it.', 'rewrites rational expressions.')),
          B('Domain and excluded values', 'HSF-IF.B.5', [
              sa('Give the domain of (x + 1)/(x - 2).', 'Answer:', key='x ≠ 2', note='Any equivalent form.'),
              sa('Give the domain of 3/(x + 1)².', 'Answer:', key='x ≠ -1', note='Any equivalent form.'),
              tf('A rational function is undefined where its denominator is 0.', key=True, note='Division by 0.'),
              mc('2x/(x² - 4) is undefined at', ['x = ±2', 'x = 0', 'x = 4', 'x = 2 only'], note='x² = 4.'),
              sa('List the excluded values of (x² - 1)/(x² - 9), separated by commas.', 'Excluded values:', key='{-3, 3}', note='Form required: both. x² - 9 = 0.'),
          ], align='exact',
            why=why('the student misses asymptote locations.', 'vertical asymptotes are at excluded values.', 'finds domains.')),
          B('Sign of a quotient on intervals', '7.NS.A.2', [
              sa('Is (x + 1)/(x - 2) positive or negative at x = 0? Answer Positive or Negative.', 'Answer:', key='Negative', note='1/(-2) < 0.'),
              sa('Is 2x/(x² - 4) positive or negative at x = 3? Answer Positive or Negative.', 'Answer:', key='Positive', note='6/5 > 0.'),
              tf('A quotient of two negative numbers is negative.', key=False, note='For example (-6)/(-2) = 3.'),
              mc('At x = 2.1, (x + 1)/(x - 2) is', ['large and positive', 'large and negative', 'zero', 'undefined'], note='3.1/0.1 = 31.'),
              tf('3/(x + 1)² is negative for some value of x.', key=False, note='A positive number over a positive square is positive (and x = -1 is excluded).'),
          ], align='supporting',
            why=why('the student draws the branches on the wrong side.', 'signs decide the behavior near asymptotes.', 'tests signs.')),
      ],
      f1=B('Graph rational functions with slant asymptotes', 'HSF-IF.C.7.d', [
          pick('Which graph shows y = (x² + 1)/x, with its asymptotes dashed?', 'C', [
              cand([lambda x: (x * x + 1) / x], 'two branches with a dashed vertical asymptote x = 0 and a dashed slant asymptote y = x; no zeros; the right branch has a low point at (1, 2) and the left branch a high point at (-1, -2).', vas=[0], slant=[(1, 0)]),
              cand([lambda x: (x * x - 1) / x], 'two increasing branches with a dashed vertical asymptote x = 0 and a dashed slant asymptote y = x; zeros at -1 and 1.', vas=[0], slant=[(1, 0)]),
              cand([lambda x: (x * x + 1) / (x - 1)], 'two branches with a dashed vertical asymptote x = 1 and a dashed slant asymptote y = x + 1; y-intercept -1.', vas=[1], slant=[(1, 1)]),
              cand([lambda x: -(x * x + 1) / x], 'two branches with a dashed vertical asymptote x = 0 and a dashed slant asymptote y = -x; the right branch has a high point at (1, -2).', vas=[0], slant=[(-1, 0)]),
          ], '(x² + 1)/x = x + 1/x: vertical asymptote x = 0, slant asymptote y = x, no zeros, no y-intercept, through (1, 2) and (-1, -2). The others show (x² - 1)/x, (x² + 1)/(x - 1), and -(x² + 1)/x.',
              x=(-6, 6), y=(-8, 8), ystep=2),
          sa('Find the slant asymptote of y = (x² - x - 1)/(x - 2).', 'Answer:', key='y = x + 1', note='Form required: equation. Quotient x + 1, remainder 1.'),
          tf('A rational function can cross its horizontal asymptote.', key=True, note='For example y = x/(x² + 1) crosses y = 0 at x = 0.'),
          mc('y = (3x² + 1)/(x² + 4) has horizontal asymptote', ['y = 3', 'y = 1/4', 'y = 0', 'none'], note='Ratio of leading coefficients.'),
          mc('Which rational function has vertical asymptote x = 1, horizontal asymptote y = 2, and a zero at x = 3?', ['f(x) = 2(x - 3)/(x - 1)', 'f(x) = (x - 3)/(2(x - 1))', 'f(x) = 2(x - 1)/(x - 3)', 'f(x) = 2(x + 3)/(x + 1)'],
             note='Zero from the numerator factor x - 3; asymptote from x - 1; ratio of leading coefficients 2/1. The others give y = 1/2, swap the roles, or change the signs.'),
      ], prog='same-course deepening', demand='Extend to slant asymptotes and construct functions from features.'),
      f2=B('Interpret a rational model\'s features in context', 'HSF-IF.B.4', [
          mc('The average cost per item is A(x) = (500 + 4x)/x dollars for x items. What do the vertical asymptote x = 0 and the horizontal asymptote y = 4 mean in context?', [
              'x = 0: the average cost grows without bound as the number of items nears 0; y = 4: the average cost approaches $4 per item as x grows.',
              'x = 0: the first item is free to make; y = 4: the total cost of all of the items approaches $4 as the number of items grows.',
              'x = 0: the fixed cost of production is $0; y = 4: no more than 4 items can be made at this average cost per item.',
              'x = 0: the average cost is exactly $500 for very few items; y = 4: the average cost is never more than $4 per item.'],
             note='500/x grows without bound near 0 and shrinks toward 0 as x grows.'),
          mc('A drug concentration is C(t) = 20t/(t² + 4) for t ≥ 0 hours. What does its horizontal asymptote mean?', [
              'y = 0: the concentration approaches 0 as time goes on.', 'y = 0: the drug never enters the blood.', 'y = 20: the concentration approaches 20 as time goes on.', 'y = 0: the concentration is 0 at every time after t = 2.'],
             note='The degree of the denominator is greater, so C → 0; C is positive for t > 0.'),
          tf('For a context, only the part of a rational graph in the context domain is meaningful.', key=True, note='Domain.'),
          mc('In A(x) = (500 + 4x)/x, as x grows the average cost', ['decreases toward 4', 'increases', 'approaches 0', 'is constant'], note='500/x → 0.'),
          sa('The average cost per item is A(x) = (500 + 4x)/x dollars for x items. Find the number of items for which the average cost is $5.', 'x =', key='500', note='500 + 4x = 5x.'),
      ], prog='cross-standard extension', demand='Interpret asymptotes and intercepts as quantities in a model.',
        builds='Builds on FORWARD 1: constructing functions from asymptotes is reversed into interpreting them.')),

    # ------------------------------------------------------------------ 75. IF.C.7.d holes versus asymptotes
    S('HSF-IF.C.7.d', 'Distinguish holes from vertical asymptotes',
      target='Factor a rational function to identify every hole (with its coordinates) and every vertical asymptote', strand='advanced', covers=['IF7d-hole'],
      main=[
          sa('f(x) = (x² - 4)/(x - 2) has exactly one hole. Give the hole as a point (x, y), and give every vertical asymptote as an x-value (enter none if there is none).', ['Hole:', 'Vertical asymptote: x ='], key='(2, 4); none',
             note='Form required: both. f(x) = x + 2 for x ≠ 2.'),
          sa('f(x) = (x - 3)/(x² - 9) has exactly one hole. Give the hole as a point (x, y), and give every vertical asymptote as an x-value (enter none if there is none).', ['Hole:', 'Vertical asymptote: x ='], key='(3, 1/6); -3',
             note='Form required: both. f(x) = 1/(x + 3) for x ≠ 3.'),
          sa('f(x) = (x² + x - 6)/(x² - x - 2) has exactly one hole. Give the hole as a point (x, y), and give every vertical asymptote as an x-value (enter none if there is none).', ['Hole:', 'Vertical asymptote: x ='], key='(2, 5/3); -1',
             note='Form required: both. (x + 3)(x - 2)/((x - 2)(x + 1)) = (x + 3)/(x + 1) for x ≠ 2.'),
          sa('f(x) = (x + 1)/(x² - 1) has exactly one hole. Give the hole as a point (x, y), and give every vertical asymptote as an x-value (enter none if there is none).', ['Hole:', 'Vertical asymptote: x ='], key='(-1, -1/2); 1',
             note='Form required: both. f(x) = 1/(x - 1) for x ≠ -1.'),
          sa('f(x) = x(x - 1)/(x(x + 2)) has exactly one hole. Give the hole as a point (x, y), and give every vertical asymptote as an x-value (enter none if there is none).', ['Hole:', 'Vertical asymptote: x ='], key='(0, -1/2); -2',
             note='Form required: both. f(x) = (x - 1)/(x + 2) for x ≠ 0.'),
      ],
      back=[
          B('Factor numerators and denominators', 'HSA-SSE.A.2', [
              sa('Factor x² + x - 6 and x² - x - 2.', ['x² + x - 6 =', 'x² - x - 2 ='], key='(x + 3)(x - 2); (x - 2)(x + 1)', note='Form required: both factored.'),
              sa('Factor x² - 9.', 'Answer:', key='(x - 3)(x + 3)', note='Form required.'),
              tf('x² - 1 = (x - 1)².', key=False, note='(x - 1)² = x² - 2x + 1; x² - 1 = (x - 1)(x + 1).'),
              mc('x² - 4 equals', ['(x - 2)(x + 2)', '(x - 4)(x + 1)', '(x - 2)²', 'x(x - 4)'], note='Difference of squares.'),
              sa('Factor x² + 2x.', 'Answer:', key='x(x + 2)', note='Form required.'),
          ], align='exact',
            why=why('the student cannot see common factors.', 'holes come from canceled common factors.', 'factors.')),
          B('Simplify rational expressions and keep exclusions', 'HSA-APR.D.7', [
              sa('Simplify (x - 3)/((x - 3)(x + 3)) and list the excluded values of the original expression, separated by commas.', ['Simplified:', 'Excluded values:'], key='1/(x + 3); {-3, 3}',
                 note='Form required: both. The canceled factor still excludes x = 3.'),
              sa('Simplify (x + 1)/((x - 1)(x + 1)) and list the excluded values of the original expression, separated by commas.', ['Simplified:', 'Excluded values:'], key='1/(x - 1); {-1, 1}',
                 note='Form required: both.'),
              tf('After simplifying, the original excluded values are still excluded.', key=True, note='Domain kept.'),
              mc('x(x - 1)/(x(x + 2)) simplifies to', ['(x - 1)/(x + 2), x ≠ 0, -2', '(x - 1)/(x + 2) for all x', 'x - 1', '-1/2'], note='Cancel x but keep x ≠ 0.'),
              sa('Simplify (x² - 4)/(x - 2) and give the excluded value of the original expression.', ['Simplified:', 'Excluded value: x ='], key='x + 2; 2', note='Form required: both.'),
          ], align='exact',
            why=why('the student loses the canceled value.', 'the canceled value becomes a hole.', 'simplifies and keeps exclusions.')),
          B('Evaluate the simplified expression', 'HSF-IF.A.2', [
              sa('Evaluate 1/(x + 3) at x = 3.', 'Answer:', key='1/6', note='Any equivalent form.'),
              sa('Evaluate (x + 3)/(x + 1) at x = 2.', 'Answer:', key='5/3', note='Any equivalent form.'),
              tf('The y-coordinate of a hole is the value of the simplified expression there.', key=True, note='Limit value.'),
              mc('(x - 1)/(x + 2) at x = 0 is', ['-1/2', '1/2', '0', 'undefined'], note='-1/2.'),
              sa('Evaluate 1/(x - 1) at x = -1.', 'Answer:', key='-1/2', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot locate the hole\'s height.', 'the hole is at (a, simplified value).', 'evaluates.')),
      ],
      f1=B('Construct and graph rational functions with holes', 'HSF-IF.C.7.d', [
          mc('Which rational function has a hole at x = 1, a vertical asymptote x = -3, and horizontal asymptote y = 0?', [
              'f(x) = (x - 1)/((x - 1)(x + 3))', 'f(x) = (x - 1)/(x + 3)', 'f(x) = (x + 3)/((x - 1)(x + 3))', 'f(x) = (x - 1)(x + 3)/(x - 1)'],
             note='The shared factor x - 1 gives the hole; x + 3 remains below; the denominator has the higher degree. The others have no hole, swap the hole and asymptote, or have no asymptote.'),
          pick('Which graph shows y = (x² - x - 2)/(x - 2)?', 'A', [
              cand([lambda x: x + 1], 'the line y = x + 1 with an open circle at (2, 3).', holes=[(2, 3)]),
              cand([lambda x: x + 1], 'the line y = x + 1 broken at a dashed vertical asymptote x = 2.', vas=[2]),
              cand([lambda x: x + 1], 'the line y = x + 1 with an open circle at (-1, 0).', holes=[(-1, 0)]),
              cand([lambda x: x + 1], 'the complete line y = x + 1 with no open circle.'),
          ], 'x² - x - 2 = (x - 2)(x + 1), so y = x + 1 for x ≠ 2: the line with a hole at (2, 3). The factor cancels, so there is no asymptote at x = 2, and x = -1 is a zero, not an excluded value.',
              x=(-5, 5), y=(-4, 6)),
          tf('A rational function can have both a hole and a vertical asymptote.', key=True, note='Different factors.'),
          mc('f(x) = (x - 4)²/(x - 4) has', ['a hole at (4, 0)', 'a vertical asymptote x = 4', 'no special features', 'a hole at (4, 4)'], note='Simplifies to x - 4.'),
          mc('For f(x) = (x - 3)/(x² - 9), why is x = -3 a vertical asymptote but x = 3 a hole?', [
              'After canceling x - 3, the factor x + 3 remains in the denominator, but x - 3 does not; near 3 the values approach 1/6.',
              'Both x - 3 and x + 3 cancel, so x = -3 and x = 3 are both holes, and the asymptote comes from x² alone.',
              'The numerator is 0 at x = -3, so the graph has a vertical asymptote at -3, and a hole is at the other zero.',
              'Negative excluded values always give asymptotes, and positive excluded values always give holes in a graph.'],
             note='(x - 3)/((x - 3)(x + 3)) = 1/(x + 3) for x ≠ 3.'),
      ], prog='same-course deepening', demand='Construct functions with prescribed holes and asymptotes and graph them.'),
      f2=B('Relate holes to extraneous solutions', 'HSA-REI.A.2', [
          mc('Solve (x² - 4)/(x - 2) = 4.', [
                        'No solution: x + 2 = 4 gives x = 2, which is excluded (the hole at (2, 4)).', 'x = 2, because it satisfies the simplified equation x + 2 = 4.', 'x = 4, because the hole of the graph is at the height y = 4.', 'Every x ≠ 2, because the function equals 4 at every point of its domain.'],
                       note='The simplified equation has the only candidate x = 2, which is not in the domain.'),
          mc('Solve (x - 3)/(x² - 9) = 1/6.', ['No solution: 1/(x + 3) = 1/6 gives x = 3, which is excluded.', 'x = 3: it satisfies 1/(x + 3) = 1/6, the simplified equation.', 'x = -3: then 1/(x + 3) = 1/6 after simplifying the left side.', 'x = 3 or x = -3: both make x² - 9 = 0, so both solve it.'],
                       note='The only candidate is the hole.'),
          tf('An extraneous solution of f(x) = c can occur exactly at a hole whose height is c.', key=True, note='Graph has no point there.'),
          mc('(x + 1)/(x² - 1) = -1/2 has', ['no solution', 'x = -1', 'x = 1', 'x = 0'], note='The only candidate is the hole.'),
          sa('Solve (x² + x - 6)/(x² - x - 2) = 2.', 'x =', key='1', note='Any equivalent form. (x + 3)/(x + 1) = 2 gives x + 3 = 2x + 2, so x = 1, which is not excluded.'),
      ], prog='cross-standard extension', demand='Explain extraneous solutions of rational equations as holes in graphs.',
        builds='Builds on FORWARD 1: the graph with a hole explains why a solution is missing.')),
]

SETS += [
    # ------------------------------------------------------------------ 76. BF.A.1.c composition
    S('HSF-BF.A.1.c', 'Compose functions and interpret compositions with domains',
      target='Write a composition of two functions, state its domain, and interpret it in context', strand='advanced', covers=['BF1c-compose'],
      main=[
          mc('f(x) = √x and g(x) = x - 4. Which gives f(g(x)) and g(f(x)) with the domain of each?', [
              'f(g(x)) = √(x - 4), x ≥ 4; g(f(x)) = √x - 4, x ≥ 0',
              'f(g(x)) = √x - 4, x ≥ 0; g(f(x)) = √(x - 4), x ≥ 4',
              'f(g(x)) = √(x - 4), x ≥ 0; g(f(x)) = √x - 4, x ≥ 4',
              'f(g(x)) = √(x - 4), all real x; g(f(x)) = √x - 4, all real x'],
             note='The input of a square root must be nonnegative: x - 4 ≥ 0 for f(g(x)), x ≥ 0 for g(f(x)).'),
          sa("The temperature is T(h) = 20 - 6.5h °C at height h km, and a balloon's height is h(t) = 0.3t km after t minutes. Write T(h(t)) = a + bt, and find the temperature at t = 10.", ['a =', 'b =', 'Temperature at t = 10 (°C):'], key='20; -1.95; 0.5',
             note='Form required: all three. T(h(t)) = 20 - 6.5(0.3t) = 20 - 1.95t; T = 20 - 19.5 = 0.5.'),
          sa('f(x) = 1/(x - 1) and g(x) = x². Write f(g(x)) and list the real numbers excluded from its domain, separated by commas. Use ^ for exponents.', ['f(g(x)) =', 'Excluded values:'], key='1/(x^2 - 1); {-1, 1}',
             note='Form required: both. x² - 1 = 0 when x = ±1.'),
          sa("A dollar amount d converts to euros by e(d) = 0.9d, and a store's price with tax in euros is p(e) = 1.2e. Then p(e(d)) = kd. Find k and the price in euros for d = 50.", ['k =', 'p(e(50)) (euros):'], key='1.08; 54',
             note='Form required: both. 1.2(0.9d) = 1.08d; 1.08 · 50 = 54.'),
          mc('f(x) = log₂ x and g(x) = x² - 9. Which gives f(g(x)) and its domain?', [
              'f(g(x)) = log₂(x² - 9); domain x < -3 or x > 3', 'f(g(x)) = log₂(x²) - 9; domain x ≠ 0', 'f(g(x)) = log₂(x² - 9); domain x > 3', 'f(g(x)) = (log₂ x)² - 9; domain x > 0'],
             note='x² - 9 > 0 on both sides. The others compose in the wrong place, miss x < -3, or compose in the other order.'),
      ],
      back=[
          B('Build combined models', 'HSF-BF.A.1.b', [
              sa('f(x) = x² and g(x) = x + 1. Find f(x) + g(x).', 'Answer:', key='x² + x + 1', note='Any equivalent form.'),
              sa('f(x) = x² and g(x) = x + 1. Find f(x) · g(x).', 'Answer:', key='x³ + x²', note='Any equivalent form.'),
              tf('f(g(x)) is a different combination from f(x) · g(x).', key=True, note='Composition vs product.'),
              mc('For f(x) = 2x and g(x) = x + 3, f(x) - g(x) is', ['x - 3', 'x + 3', '3x + 3', '2x² + 6x'], note='Subtract.'),
              mc('Which operation combines T and h in T(h(t))?', ['composition', 'multiplication', 'addition', 'division'], note='The output of h is the input of T.'),
          ], align='supporting',
            why=why('the student confuses composition with arithmetic.', 'composition is a new way to combine.', 'combines functions.')),
          B('Evaluate a function at an expression', 'HSF-IF.A.2', [
              mc('f(x) = √x. Find f(x - 4).', ['√(x - 4)', '√x - 4', '√x - √4', '√(x) · (-4)'], note='Replace x by x - 4 inside the root.'),
              sa('T(h) = 20 - 6.5h. Find T(0.3t) in the form a + bt. Give a and b.', ['a =', 'b ='], key='20; -1.95', note='Form required: both. 6.5 · 0.3 = 1.95.'),
              tf('If f(x) = 1/(x - 1), then f(x²) = 1/(x² - 1).', key=True, note='Substitute.'),
              mc('If g(x) = x² - 9, then g(3) is', ['0', '-3', '9', '-6'], note='9 - 9.'),
              sa('p(e) = 1.2e. Find p(45).', 'Answer:', key='54', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot substitute an expression.', 'composition substitutes one function into another.', 'evaluates at expressions.')),
          B('Domains of radical, rational, and log functions', 'HSF-IF.B.5', [
              sa('Give the domain of √(x - 4).', 'Answer:', key='x ≥ 4', note='Any equivalent form.'),
              sa('Give the domain of log₂ u in terms of u.', 'Answer:', key='u > 0', note='Any equivalent form.'),
              tf('1/(x² - 1) is undefined only at x = 1.', key=False, note='x² - 1 = 0 at both x = 1 and x = -1.'),
              mc('x² - 9 > 0 when', ['x < -3 or x > 3', '-3 < x < 3', 'x > 9', 'all x'], note='Outside the roots.'),
              sa('Give the domain of √x - 4.', 'Answer:', key='x ≥ 0', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student omits the composite\'s domain.', 'the inner output must be a valid input.', 'finds domains.')),
      ],
      f1=B('Decompose functions into compositions', 'HSF-BF.A.1.c', [
          mc('Which pair writes h(x) = (3x + 1)⁵ as f(g(x))?', ['g(x) = 3x + 1, f(x) = x⁵', 'g(x) = x⁵, f(x) = 3x + 1', 'g(x) = 3x, f(x) = x⁵ + 1', 'g(x) = 3x + 1, f(x) = 5x'],
             note='The inner function is 3x + 1 and the outer raises to the 5th power. The others reverse the order, split the inner function, or multiply by 5.'),
          mc('Which pair writes h(x) = 2^(x²) as f(g(x))?', ['g(x) = x², f(x) = 2^x', 'g(x) = 2^x, f(x) = x²', 'g(x) = 2x, f(x) = x²', 'g(x) = x², f(x) = 2x'],
             note='f(g(x)) = 2^(x²). The others give (2^x)², (2x)², or 2x².'),
          tf('h(x) = (x + 1)² can be written as f(g(x)) in more than one way, for example with g(x) = x + 1 and f(x) = x², or with g(x) = x² + 2x and f(x) = x + 1.', key=True,
             note='Both give x² + 2x + 1.'),
          mc('If f(x) = x + 1, g(x) = 2x, k(x) = x², then f(g(k(3))) is', ['19', '37', '64', '13'], note='k(3) = 9, g = 18, f = 19.'),
          mc('Which context describes a composition V(r(t))?', [
              'The volume V of a balloon depends on its radius r, and the radius depends on time t.',
              'The volume V and the radius r of a balloon are added together at each time t.',
              'The volume V of a balloon is multiplied by its radius r at each time t.',
              'The time t depends on the volume V, and the volume depends on the radius r.'],
             note='t → r → V: the output of r is the input of V.'),
      ], prog='same-course deepening', demand='Reverse composition: decompose a function and compose three functions.'),
      f2=B('Verify inverses by composition', 'HSF-BF.B.4.b', [
          mc('Which work shows that f(x) = 2x + 3 and g(x) = (x - 3)/2 are inverses?', [
              'f(g(x)) = 2((x - 3)/2) + 3 = x and g(f(x)) = ((2x + 3) - 3)/2 = x',
              'f(g(x)) = 2((x - 3)/2) + 3 = x + 6 and g(f(x)) = x',
              'f(x) · g(x) = (2x + 3)(x - 3)/2 = x',
              'f(0) = 3 and g(0) = -3/2, which are opposite in sign'],
             note='Both compositions must equal x. The others make an arithmetic error, multiply instead of composing, or compare single values.'),
          sa('Compute f(g(x)) for f(x) = x³ and g(x) = ∛x.', 'Answer:', key='x', note='Any equivalent form.'),
          tf('If f(g(x)) = x for all x in g\'s domain and g(f(x)) = x for all x in f\'s domain, then f and g are inverses.', key=True, note='Definition.'),
          mc('For f(x) = x + 5 and g(x) = x - 5, f(g(2)) is', ['2', '7', '-3', '12'], note='Inverses.'),
          mc('Why is composition the natural test for inverse functions?', [
                        'An inverse undoes the function, so applying one after the other must return the original input.',
                        'Two functions are inverses exactly when their product f(x) · g(x) is equal to 1 for every x.',
                        'Composition adds the two functions, and inverses must add to 0 for every input x.',
                        'Composition reverses the graph across the x-axis, which is where an inverse must lie.'],
                       note='f(g(x)) = x and g(f(x)) = x. The others describe adding, reflecting over the x-axis, or multiplying, none of which is the inverse relationship.'),
      ], prog='cross-standard extension', demand='Use composition to test the inverse relationship.',
        builds='Builds on FORWARD 1: composing and decomposing functions leads to compositions that give the identity.')),

    # ------------------------------------------------------------------ 77. BF.B.4.b verify inverses
    S('HSF-BF.B.4.b', 'Verify inverses by composition on the stated domains',
      target='Verify that two functions are inverses by computing both compositions and checking the domains: identify the complete, correct verification', strand='advanced', covers=['BF4b-verify'],
      main=[
          mc('Which work verifies by composition that f(x) = 2x + 3 and g(x) = (x - 3)/2 are inverses?', [
              'f(g(x)) = 2 · (x - 3)/2 + 3 = x and g(f(x)) = ((2x + 3) - 3)/2 = x, for all real x.',
              'f(g(x)) = 2 · (x - 3)/2 + 3 = x for all real x, and one composition is enough by itself.',
              'f(1) = 5 and g(5) = 1, so f and g are inverses.',
              'f(x) · g(x) = (2x + 3)(x - 3)/2 = 1, so f and g are inverses.'],
             note='Both compositions must simplify to x. The others check one composition only, one input only, or multiply the functions instead of composing them.'),
          mc('Which work verifies by composition that f(x) = x³ - 1 and g(x) = ∛(x + 1) are inverses?', [
              'f(g(x)) = (∛(x + 1))³ - 1 = x and g(f(x)) = ∛((x³ - 1) + 1) = ∛(x³) = x, for all real x.',
              'f(g(x)) = (∛(x + 1))³ - 1 = x, but only for x ≥ 0, so f and g are inverses only when x ≥ 0.',
              'f(2) = 7 and g(7) = 2, so f and g are inverses.',
              'g(f(x)) = ∛(x³ - 1) + 1 = x, so f and g are inverses.'],
             note='Both compositions simplify to x for every real x (cube roots are defined for negatives). The others add a false domain limit, check one input, or compose incorrectly.'),
          mc('Which work verifies by composition that f(x) = 2^x and g(x) = log₂ x are inverses, with the correct domains?', [
              'f(g(x)) = 2^(log₂x) = x for x > 0, and g(f(x)) = log₂(2^x) = x for all real x.',
              'f(g(x)) = 2^(log₂x) = x and g(f(x)) = log₂(2^x) = x, both for every real number x.',
              'f(g(x)) = 2 · log₂ x = x for x > 0.',
              'f(3) = 8 and g(8) = 3, so f and g are inverses for all x.'],
             note='log₂ x is defined only for x > 0, so f(g(x)) = x holds for x > 0; g(f(x)) = x for every real x. The others ignore the domain of log₂, multiply instead of composing, or check one input.'),
          mc('Which work verifies by composition that f(x) = 1/(x - 2) (x ≠ 2) and g(x) = 1/x + 2 (x ≠ 0) are inverses?', [
              'f(g(x)) = 1/((1/x + 2) - 2) = 1/(1/x) = x for x ≠ 0, and g(f(x)) = 1/(1/(x - 2)) + 2 = (x - 2) + 2 = x for x ≠ 2.',
              'f(g(x)) = 1/((1/x + 2) - 2) = 1/(1/x) = x, so f and g are inverses for all real x with no excluded values needed.',
              'g(f(x)) = 1/(x - 2) + 2 = (2x - 3)/(x - 2), so they are not inverses.',
              'f(3) = 1 and g(1) = 3, so f and g are inverses.'],
             note='Both compositions simplify to x on the stated domains. The others drop the second composition and the domains, compute f(x) + 2 instead of g(f(x)), or check one input.'),
          mc('f(x) = x² with domain x ≥ 0 and g(x) = √x. Which work verifies that they are inverses and explains why the domain restriction is needed?', [
              'f(g(x)) = (√x)² = x for x ≥ 0, and g(f(x)) = √(x²) = |x| = x because x ≥ 0. Without the restriction, √(x²) = |x| ≠ x for x < 0.',
              'f(g(x)) = (√x)² = x and g(f(x)) = √(x²) = x for every real number x, so the two functions are inverses and no domain restriction is needed.',
              'The restriction is needed because √x is undefined for x > 0.',
              'g(f(x)) = √(x²) = ±x, and the restriction chooses the + sign.'],
             note='√(x²) = |x|, which equals x only when x ≥ 0 (for example √((-3)²) = 3). The others ignore |x|, state a false fact about √x, or treat √ as giving two values.'),
      ],
      back=[
          B('Find inverses algebraically', 'HSF-BF.B.4.a', [
              sa('Find the inverse of f(x) = 2x + 3.', 'f⁻¹(x) =', key='(x - 3)/2', note='Any equivalent form.'),
              mc('Find the inverse of f(x) = x³ - 1.', ['f⁻¹(x) = ∛(x + 1)', 'f⁻¹(x) = ∛x + 1', 'f⁻¹(x) = ∛(x - 1)', 'f⁻¹(x) = 1/(x³ - 1)'], note='y + 1 = x³.'),
              tf('The inverse of 2^x is log₂ x.', key=True, note='Definition.'),
              mc('The inverse of f(x) = 1/(x - 2) is', ['1/x + 2', '1/(x + 2)', 'x - 2', '2 - 1/x'], note='Solve y = 1/(x - 2).'),
              mc('Find the inverse of f(x) = x² for x ≥ 0.', ['f⁻¹(x) = √x', 'f⁻¹(x) = ±√x', 'f⁻¹(x) = x/2', 'f⁻¹(x) = 1/x²'], note='The nonnegative root undoes squaring on x ≥ 0.'),
          ], align='exact',
            why=why('the student has no candidate to verify.', 'verification checks a proposed inverse.', 'finds inverses.')),
          B('Compose functions', 'HSF-BF.A.1.c', [
              sa('f(x) = 2x + 3 and g(x) = (x - 3)/2. Compute f(g(5)).', 'Answer:', key='5', note='Any equivalent form.'),
              sa('f(x) = 2x + 3 and g(x) = (x - 3)/2. Compute g(f(5)).', 'Answer:', key='5', note='Any equivalent form.'),
              tf('f(g(x)) means apply g first, then f.', key=True, note='Inside out.'),
              mc('For f(x) = x³ and g(x) = x + 1, f(g(x)) is', ['(x + 1)³', 'x³ + 1', '3x + 1', 'x + 1'], note='Substitute.'),
              sa('Compute log₂(2⁵).', 'Answer:', key='5', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot compose.', 'verification is composition.', 'composes functions.')),
          B('Square roots of squares', 'HSN-RN.A.2', [
              sa('Evaluate √((-3)²).', 'Answer:', key='3', note='Any equivalent form.'),
              sa('Evaluate (√7)².', 'Answer:', key='7', note='Any equivalent form.'),
              tf('√(x²) = x for every real x.', key=False, note='√(x²) = |x|.'),
              mc('√(x²) equals', ['|x|', 'x', '-x', 'x²'], note='Principal root.'),
              sa('For which x is √(x²) = x?', 'Answer:', key='x ≥ 0', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student simplifies √(x²) to x.', 'the restriction x ≥ 0 depends on it.', 'simplifies √(x²).')),
      ],
      f1=B('Show that proposed inverses fail', 'HSF-BF.B.4.b', [
          mc('Which work shows by composition that f(x) = 3x - 1 and g(x) = (x - 1)/3 are not inverses?', [
              'f(g(x)) = 3((x - 1)/3) - 1 = x - 2, which is not x',
              'f(g(x)) = 3((x - 1)/3) - 1 = x, so they are inverses',
              'g(f(x)) = ((3x - 1) - 1)/3 = x, so they are inverses',
              'f(0) = -1 and g(0) = -1/3 are different, so they are not inverses'],
             note='One composition that is not x is enough. The others make arithmetic errors or compare f and g at the same input.'),
          mc('f(x) = x² (all real x) and g(x) = √x. Which composition fails to equal x, and for which x?', [
              'g(f(x)) = √(x²) = |x|, which is not x for x < 0', 'f(g(x)) = (√x)² fails for every x > 0', 'g(f(x)) = x for every real x', 'f(g(x)) = |x|, which is not x for x < 0'],
             note='√(x²) = |x|. f(g(x)) is defined only for x ≥ 0, where it equals x.'),
          tf('Checking f(g(x)) = x alone is always enough.', key=False, note='Both compositions must be checked (with domains).'),
          mc('For f(x) = e^x and g(x) = ln x, g(f(x)) =', ['x for all real x', 'x only for x > 0', '|x|', 'e^(lnx)'], note='ln(e^x) = x.'),
          sa('Fix the domain of f(x) = (x - 1)² so that g(x) = 1 + √x is its inverse.', 'Answer:', key='x ≥ 1', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Use composition to disprove proposed inverses and repair domains.'),
      f2=B('Read inverse values from tables and graphs', 'HSF-BF.B.4.c', [
          sa('A table gives f(0) = 1, f(1) = 3, f(2) = 7, f(3) = 15. Find f⁻¹(7).', 'Answer:', key='2', note='Any equivalent form.'),
          sa('A table gives f(0) = 1, f(1) = 3, f(2) = 7, f(3) = 15. Find f⁻¹(f⁻¹(15)).', 'Answer:', key='f⁻¹(3) = 1', note='Any equivalent form.'),
          tf('If (a, b) is on the graph of f, then (b, a) is on the graph of f⁻¹.', key=True, note='Swap.'),
          mc('If f(4) = 9, then f⁻¹(9) is', ['4', '9', '1/4', '13'], note='Swap.'),
          mc('A table gives f(1) = 3 and f(2) = 7. How do these values give f(f⁻¹(7)) = 7?', [
                        'f⁻¹(7) = 2 because f(2) = 7, and then f(2) = 7, so f(f⁻¹(7)) = 7.',
                        'f⁻¹(7) = 1/7 because an inverse is a reciprocal, and f(1/7) = 7, so f(f⁻¹(7)) = 7.',
                        'f⁻¹(7) = 3 because f(1) = 3, and then f(3) = 7.',
                        'f⁻¹(7) = 7 - 3 = 4 by subtracting the outputs, and f(4) = 7 by the pattern.'],
                       note='Read the table backward, then forward.'),
      ], prog='cross-standard extension', demand='Apply the inverse relationship to values in tables and graphs.',
        builds='Builds on FORWARD 1: compositions verified algebraically are now checked with tabled values.')),

    # ------------------------------------------------------------------ 78. BF.B.4.c read inverse values
    S('HSF-BF.B.4.c', 'Read values of an inverse function from graphs and tables',
      target='Read values of f⁻¹ from a table or graph of an invertible function f and interpret them', strand='advanced', covers=['BF4c-read'],
      main=[
          sa('The table shows f. Find f⁻¹(15).', 'f⁻¹(15) =', key='3', fig=tbl(['x', '0', '1', '2', '3', '4'], [['f(x)', '1', '3', '7', '15', '31']]),
             note='f(3) = 15.'),
          sa('The graph of f(x) = 2^x - 1 is shown. Use it to find f⁻¹(3).', 'Answer:', key='2', note='Any equivalent form. The point (2, 3) is on the graph.',
             fig=graph([lambda x: 2 ** x - 1], x=(-3, 4), y=(-2, 8), pts=[(2, 3, '(2, 3)', 'e')], desc='Graph of an increasing exponential curve with asymptote y = -1, passing through (0, 0), (1, 1), (2, 3), and (3, 7).')),
          sa('The table shows a decreasing function g. Find g⁻¹(10) and g⁻¹(g(2)).', ['g⁻¹(10) =', 'g⁻¹(g(2)) ='], key='4; 2', fig=tbl(['x', '1', '2', '3', '4', '5'], [['g(x)', '40', '25', '16', '10', '4']]),
             note='Form required: both. g(4) = 10; g⁻¹ undoes g.'),
          sa('The graph of f(x) = ∛x + 1 is shown. Use it to find f⁻¹(0) and f⁻¹(3).', ['f⁻¹(0) =', 'f⁻¹(3) ='], key='-1; 8', note='Form required: both. The points (-1, 0) and (8, 3) are on the graph.',
             fig=graph([lambda x: math.copysign(abs(x) ** (1 / 3), x) + 1], x=(-9, 9), y=(-2, 4), xlab=3, pts=[(-1, 0, '(-1, 0)', 'nw'), (8, 3, '(8, 3)', 'n')],
                       desc='Graph of an increasing cube-root curve centered at (0, 1), passing through (-8, -1), (-1, 0), (1, 2), and (8, 3).')),
          mc("The table gives a plane's altitude A (m) t minutes after takeoff. Find A⁻¹(1200) and interpret it.", [
              'A⁻¹(1200) = 4: the plane reaches 1200 m four minutes after takeoff.', 'A⁻¹(1200) = 4: the plane climbs 1200 m every minute.', 'A⁻¹(1200) = 1500: the altitude one minute after reaching 1200 m.', 'A⁻¹(1200) = 1/1200: the reciprocal of the altitude.'],
             fig=tbl(['t (min)', '0', '1', '2', '3', '4', '5'], [['A (m)', '0', '250', '550', '880', '1200', '1500']]), note='A(4) = 1200; the inverse gives the time for an altitude.'),
      ],
      back=[
          B('Inverse functions swap inputs and outputs', 'HSF-BF.B.4.a', [
              sa('If f(3) = 15, what is f⁻¹(15)?', 'Answer:', key='3', note='Any equivalent form.'),
              mc('Write the inverse of f(x) = 2^x - 1.', ['f⁻¹(x) = log₂(x + 1)', 'f⁻¹(x) = log₂ x + 1', 'f⁻¹(x) = log₂(x - 1)', 'f⁻¹(x) = 2^(-x) + 1'], note='x + 1 = 2^y.'),
              tf('f⁻¹(y) is the input of f that gives the output y.', key=True, note='Definition.'),
              mc('If (5, 4) is on the graph of g, which point is on g⁻¹?', ['(4, 5)', '(5, 4)', '(-5, -4)', '(1/5, 1/4)'], note='Swap.'),
              sa('Use the formula to find f⁻¹(3) for f(x) = 2^x - 1.', 'Answer:', key='2', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student reads f instead of f⁻¹.', 'reading an inverse means reading backward.', 'swaps inputs and outputs.')),
          B('Read points from graphs and tables', '8.F.A.1', [
              sa('A table gives f(0) = 1, f(1) = 3, f(2) = 7, f(3) = 15. What is f(2)?', 'Answer:', key='7', note='Any equivalent form.'),
              sa('A plane\'s altitude A (m) at t = 0, 1, 2, 3, 4 minutes is 0, 250, 550, 880, 1200. What is A(3)?', 'Answer:', key='880 m', note='Any equivalent form.'),
              tf('A function gives exactly one output for each input.', key=True, note='Definition.'),
              mc('g(1) = 40, g(2) = 25, g(3) = 16, g(4) = 10. Which input of g gives 16?', ['3', '2', '4', '16'], note='Read backward.'),
              sa('A graph passes through (8, 3). What is the output at input 8?', 'Answer:', key='3', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student misreads tables.', 'inverse values are read from the same tables.', 'reads functions.')),
          B('One-to-one functions', 'HSF-BF.B.4.b', [
              mc('Why does a strictly increasing function have an inverse function?', [
                                              'Different inputs give different outputs, so each output comes from exactly one input.', 'Its outputs are always positive, so each output can be undone.', 'Its graph passes through the origin, so it can be reflected over y = x.', 'Its domain is all real numbers, so every input has an output.'],
                                             note='Strictly increasing implies one-to-one. The others name properties (passing through the origin, positive outputs, domain) that do not make a function one-to-one.'),
              sa('Does a function with f(1) = 4 and f(3) = 4 have an inverse function? Answer Yes or No.', 'Answer:', key='No', note='The output 4 has two inputs.'),
              tf('A decreasing function can have an inverse.', key=True, note='Still one-to-one.'),
              mc('Which table has an inverse function?', ['x: 1, 2, 3; y: 5, 7, 9', 'x: 1, 2, 3; y: 5, 7, 5', 'x: 1, 2, 3; y: 2, 2, 2', 'x: 1, 2, 3; y: 0, 1, 0'], note='Distinct outputs.'),
              sa('A table gives f(2) = 7 and f(3) = 15. Use the table to find f⁻¹(15), then f(f⁻¹(15)).', ['f⁻¹(15) =', 'f(f⁻¹(15)) ='], key='3; 15', note='Form required: both.'),
          ], align='supporting',
            why=why('the student reads values from non-invertible data.', 'reading requires one-to-one data.', 'recognizes one-to-one functions.')),
      ],
      f1=B('Estimate inverse values between data points and sketch inverse graphs', 'HSF-BF.B.4.c', [
          sa("A plane's altitude is 880 m at t = 3 min and 1200 m at t = 4 min. Assume it climbs at a constant rate between these times. Estimate the time when it reaches 1000 m, to the nearest tenth of a minute.", 't ≈', key='3.4',
             note='3 + 120/320 = 3.375, which rounds to 3.4.'),
          pick('Which graph shows the inverse of f(x) = 2^x - 1?', 'D', [
              cand([lambda x: math.log(x + 1, 2)], 'an increasing curve to the right of the dashed vertical asymptote x = -1, through (0, 0), (1, 1), (3, 2), and (7, 3).', vas=[-1]),
              cand([lambda x: 2 ** x - 1], 'an increasing curve approaching the dashed line y = -1 to the left, through (0, 0), (1, 1), and (2, 3).', has=[-1]),
              cand([lambda x: 1 / (2 ** x - 1)], 'two branches separated by a dashed vertical asymptote x = 0: decreasing toward 0 on the right and staying below -1 on the left.', vas=[0]),
              cand([lambda x: math.log(x, 2) - 1], 'an increasing curve to the right of the dashed vertical asymptote x = 0, through (1, -1), (2, 0), and (4, 1).', vas=[0]),
          ], 'Swap the coordinates of points of f: (0, 0), (1, 1), (2, 3) on f give (0, 0), (1, 1), (3, 2) on f⁻¹; the asymptote y = -1 becomes x = -1; f⁻¹(x) = log₂(x + 1). The others show f itself, the reciprocal 1/f(x), and log₂ x - 1 (operations undone in the wrong order).',
              x=(-2, 8), y=(-3, 4)),
          tf('The graph of f⁻¹ is the reflection of the graph of f across y = x.', key=True, note='Swap coordinates.'),
          mc('A decreasing function has g(1) = 40, g(2) = 25, g(3) = 16, g(4) = 10. Estimate g⁻¹(20).', ['between 2 and 3', 'between 3 and 4', 'between 1 and 2', 'between 4 and 5'], note='g(2) = 25, g(3) = 16.'),
          sa('A table gives f(0) = 1, f(1) = 3, f(2) = 7, f(3) = 15. Find (f⁻¹)⁻¹(2).', 'Answer:', key='f(2) = 7', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Estimate inverse values between data points and draw inverse graphs.'),
      f2=B('Restrict the domain to make a function invertible', 'HSF-BF.B.4.d', [
          mc('f(x) = (x - 3)² is not invertible on all real numbers. Which restriction and inverse are correct?', [
              'x ≥ 3; f⁻¹(x) = 3 + √x', 'x ≥ 3; f⁻¹(x) = 3 - √x', 'x ≥ 0; f⁻¹(x) = √x + 3', 'x ≤ 3; f⁻¹(x) = 3 + √x'],
             note='On x ≥ 3, y = (x - 3)² gives x = 3 + √y. On x ≤ 3 the inverse is 3 - √x; x ≥ 0 is not one-to-one (f(2) = f(4)).'),
          mc('h(x) = x² has h(-2) = 4, h(0) = 0, and h(2) = 4. Why is h⁻¹(4) not defined, and how can the domain be restricted to fix it?', [
              '4 is the output of two inputs (-2 and 2); restrict h to x ≥ 0 (or to x ≤ 0).',
              '4 is the output of two inputs (-2 and 2); restrict h to -2 ≤ x ≤ 2.',
              'h⁻¹(4) = 1/4, so it is defined, and no restriction is needed.',
              '0 has no inverse, so remove x = 0 from the domain of h.'],
             note='Each half of the parabola is one-to-one; -2 ≤ x ≤ 2 still contains both inputs.'),
          tf('Restricting the domain can turn a non-invertible function into an invertible one.', key=True, note='One-to-one on the piece.'),
          mc('f(x) = x² restricted to x ≤ 0 has inverse', ['-√x', '√x', 'x²', '1/x²'], note='Negative outputs.'),
          mc('f(x) = (x - 3)² has range y ≥ 0. When its domain is restricted to make it invertible, why should the restricted function still take every output value y ≥ 0?', [
              'So the inverse is defined for every output of the original function; for example, x ≥ 3 still gives every y ≥ 0.',
              'So the restricted function has more outputs than the original function, which makes the inverse larger.',
              'Because a restricted function must always have exactly the same domain as the original function.',
              'Because the inverse function must be identical to the original function on the restricted domain.'],
             note='Keeping the original range keeps the inverse defined on all of it.'),
      ], prog='cross-standard extension', demand='Create invertible functions from non-invertible ones by restricting domains.',
        builds='Builds on FORWARD 1: reading inverses needs one-to-one data, which restriction provides.')),

    # ------------------------------------------------------------------ 79. BF.B.4.d restrict domains
    S('HSF-BF.B.4.d', 'Restrict a domain to make a function invertible and write the inverse',
      target='Choose a domain on which a non-invertible function is one-to-one, write the inverse, and state its domain', strand='advanced', covers=['BF4d-restrict'],
      main=[
          mc('Restrict f(x) = (x - 3)² to x ≥ 3. Which is f⁻¹ with its domain?', ['f⁻¹(x) = √x + 3, x ≥ 0', 'f⁻¹(x) = √x - 3, x ≥ 0', 'f⁻¹(x) = √(x + 3), x ≥ -3', 'f⁻¹(x) = √x + 3, x ≥ 3'],
             note='y = (x - 3)² with x ≥ 3 gives x = √y + 3; the domain of f⁻¹ is the range of f, y ≥ 0.'),
          mc('Restrict f(x) = x² + 1 to x ≤ 0. Which is f⁻¹ with its domain?', ['f⁻¹(x) = -√(x - 1), x ≥ 1', 'f⁻¹(x) = √(x - 1), x ≥ 1', 'f⁻¹(x) = -√(x + 1), x ≥ -1', 'f⁻¹(x) = -√(x - 1), x ≤ 0'],
             note='The outputs of f⁻¹ must be ≤ 0, so take the negative root; the domain is the range of f, x ≥ 1.'),
          mc('Restrict f(x) = |x + 2| to x ≥ -2. Which is f⁻¹ with its domain?', ['f⁻¹(x) = x - 2, x ≥ 0', 'f⁻¹(x) = x + 2, x ≥ -2', 'f⁻¹(x) = -x - 2, x ≥ 0', 'f⁻¹(x) = x - 2, x ≥ -2'],
             note='On x ≥ -2, f(x) = x + 2 with range y ≥ 0.'),
          mc('Restrict f(x) = (x + 1)² - 4 to x ≥ -1. Which is f⁻¹ with its domain?', ['f⁻¹(x) = -1 + √(x + 4), x ≥ -4', 'f⁻¹(x) = -1 - √(x + 4), x ≥ -4', 'f⁻¹(x) = 1 + √(x - 4), x ≥ 4', 'f⁻¹(x) = -1 + √(x + 4), x ≥ -1'],
             note='x + 1 = √(y + 4) for x ≥ -1; the range of f is y ≥ -4.'),
          mc('Restrict f(x) = x⁴ to x ≥ 0. Which is f⁻¹ with its domain?', ['f⁻¹(x) = ⁴√x, x ≥ 0', 'f⁻¹(x) = x/4, x ≥ 0', 'f⁻¹(x) = ±⁴√x, x ≥ 0', 'f⁻¹(x) = 1/x⁴, x > 0'],
             note='The nonnegative fourth root; ± is not a function; 1/x⁴ is a reciprocal, not an inverse.'),
      ],
      back=[
          B('Find the vertex of a quadratic', 'HSF-IF.C.8.a', [
              sa('Give the vertex of y = (x + 1)² - 4.', 'Answer:', key='(-1, -4)', note='Any equivalent answer.'),
              sa('Give the vertex of y = x² + 1.', 'Answer:', key='(0, 1)', note='Any equivalent answer.'),
              tf('A parabola is increasing on one side of its vertex and decreasing on the other.', key=True, note='Turning point.'),
              mc('The vertex of y = (x - 3)² is', ['(3, 0)', '(-3, 0)', '(0, 9)', '(0, 3)'], note='h = 3.'),
              sa('On which side of the vertex is y = (x - 3)² increasing?', 'Answer:', key='x ≥ 3', note='Any equivalent answer.'),
          ], align='exact',
            why=why('the student cannot choose where to split the graph.', 'the restriction starts at the vertex.', 'finds vertices.')),
          B('Write inverses of one-to-one functions', 'HSF-BF.B.4.a', [
              mc('Solve y = (x - 3)² for x when x ≥ 3.', ['x = 3 + √y', 'x = 3 - √y', 'x = √y - 3', 'x = √(y + 3)'], note='x - 3 = √y because x - 3 ≥ 0.'),
              mc('Solve y = x² + 1 for x when x ≤ 0.', ['x = -√(y - 1)', 'x = √(y - 1)', 'x = -√y - 1', 'x = -√(y + 1)'], note='x² = y - 1 and x ≤ 0.'),
              tf('When x ≤ 0, the solution of x² = 4 is x = -2.', key=True, note='Choose the negative root.'),
              mc('Solving y = x + 2 (x ≥ -2) for x gives', ['y - 2', 'y + 2', '2 - y', '-y - 2'], note='Linear piece.'),
              sa('Solve y = x⁴ for x when x ≥ 0. Give x as a power of y, using ^ for exponents.', 'x =', key='y^(1/4)', note='The nonnegative fourth root.'),
          ], align='exact',
            why=why('the student picks the wrong root.', 'the restriction decides the sign of the root.', 'solves for x with a restriction.')),
          B('Domains and ranges', 'HSF-IF.B.5', [
              sa('Give the range of f(x) = (x - 3)² for x ≥ 3.', 'Answer:', key='y ≥ 0', note='Any equivalent form.'),
              sa('Give the range of f(x) = (x + 1)² - 4 for x ≥ -1.', 'Answer:', key='y ≥ -4', note='Any equivalent form.'),
              tf('The domain of the inverse is the range of the restricted function.', key=True, note='Swap.'),
              mc('The range of x² + 1 for x ≤ 0 is', ['y ≥ 1', 'y ≤ 1', 'y ≥ 0', 'all reals'], note='Minimum 1.'),
              sa('Give the range of |x + 2| for x ≥ -2.', 'Answer:', key='y ≥ 0', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student omits the inverse\'s domain.', 'the inverse domain is the range.', 'finds ranges.')),
      ],
      f1=B('Compare different restrictions', 'HSF-BF.B.4.d', [
          mc('Restrict f(x) = (x - 3)² to x ≤ 3. Which is the inverse with its domain?', ['f⁻¹(x) = 3 - √x, x ≥ 0', 'f⁻¹(x) = 3 + √x, x ≥ 0', 'f⁻¹(x) = √x - 3, x ≥ 0', 'f⁻¹(x) = 3 - √x, x ≤ 3'],
             note='For x ≤ 3, x - 3 = -√y. The inverse\'s domain is the restricted function\'s range, y ≥ 0.'),
          mc("A ball's height is h(t) = -5(t - 2)² + 20 for 0 ≤ t ≤ 4. Which restriction and inverse give the time as a function of height on the way down?", [
              '2 ≤ t ≤ 4; t = 2 + √((20 - h)/5)', '0 ≤ t ≤ 2; t = 2 - √((20 - h)/5)', '2 ≤ t ≤ 4; t = 2 - √((20 - h)/5)', '0 ≤ t ≤ 4; t = 2 + √((20 - h)/5)'],
             note='The ball falls after the vertex at t = 2, where t - 2 ≥ 0.'),
          tf('A function can have more than one valid restriction that makes it invertible.', key=True, note='Either side of the vertex.'),
          mc('Which restriction does not make f(x) = x² invertible?', ['-1 ≤ x ≤ 1', 'x ≥ 0', 'x ≤ 0', '1 ≤ x ≤ 5'], note='Contains both ±1/2, for example.'),
          mc('Why is the restriction x ≥ 0 natural for f(x) = x² in the area formula A = s²?', ['Side lengths are nonnegative.', 'Areas can be negative.', 'Squares have four sides.', 'x² is always increasing.'], note='Context restricts the domain. The others are false or irrelevant: x² is not always increasing, the number of sides does not restrict s, and areas are not negative.'),
      ], prog='same-course deepening', demand='Choose between restrictions and match the restriction to a context.'),
      f2=B('Restrict trigonometric functions to define inverses', 'HSF-TF.B.6', [
          mc('Why is sin x not invertible on all real numbers?', [
                                  'It repeats values (for example sin 0 = sin π = 0), so it is not one-to-one.', 'It is not defined for negative x, so an inverse would be incomplete.', 'Its outputs are larger than 1 for large x, outside the range of an inverse.', 'It is an odd function, and odd functions never have an inverse.'],
                                 note='A function must be one-to-one to have an inverse. The others are false: sin x stays between -1 and 1, is defined for negative x, and being odd does not prevent an inverse.'),
          mc('What is the standard restricted domain of sin x, and why does it work?', [
              '-π/2 ≤ x ≤ π/2: sin is increasing there and takes every value from -1 to 1 once.',
              '0 ≤ x ≤ π: sin is increasing there and takes every value from -1 to 1 once.',
              '0 ≤ x ≤ 2π: sin takes every value from -1 to 1 there, which is all that is needed.',
              '-π/2 ≤ x ≤ π/2: sin is decreasing there and takes every value from 0 to 1 once.'],
             note='On [-π/2, π/2] sin rises from -1 to 1.'),
          tf('cos x is restricted to 0 ≤ x ≤ π to define arccos.', key=True, note='Decreasing there.'),
          mc('arcsin(1) equals', ['π/2', 'π', '0', '3π/2'], note='In the restricted range.'),
          mc('Why would 0 ≤ x ≤ π not work as a restricted domain for an inverse of sine?', [
                                  'sin increases then decreases there, so values repeat (sin(π/6) = sin(5π/6)).', 'sin is not defined at x = π, so the interval is not closed.', 'sin is negative everywhere on that interval, so it misses positive values.', 'sin is increasing on that whole interval, so it is one-to-one there.'],
                                 note='The function must be one-to-one on the restricted domain. The others are false: sin is defined at π, is nonnegative on [0, π], and is not increasing on the whole interval.'),
      ], prog='cross-standard extension', demand='Apply domain restriction to periodic functions.',
        builds='Builds on FORWARD 1: choosing a monotone piece of a parabola is applied to periodic graphs.')),

    # ------------------------------------------------------------------ 80. BF.B.5 log and exponent inverse relationship
    S('HSF-BF.B.5', 'Use the inverse relationship of exponents and logarithms to solve equations',
      target='Solve logarithmic equations by rewriting them in exponential form (and use log properties), checking for extraneous solutions', strand='advanced', covers=['BF5-loginv'],
      main=[
          sa('Solve log₃ x = 4.', 'x =', key='81', note='Any equivalent form. x = 3⁴.'),
          sa('Solve 2 log₅(x - 1) = 4.', 'x =', key='26', note='Any equivalent form. log₅(x - 1) = 2.'),
          sa('Solve ln(x + 2) = 1 exactly.', 'x =', key='e - 2', note='Form required: exact.'),
          sa('Solve log₂ x + log₂(x - 2) = 3. The equation x(x - 2) = 8 gives two candidates. Give the actual solution and the extraneous value.', ['Solution: x =', 'Extraneous value: x ='], key='4; -2',
             note='Form required: both. x² - 2x - 8 = 0 gives 4 or -2; log₂(-2) is undefined.'),
          sa('Solve log x - log(x - 9) = 1 (base 10) and check.', 'x =', key='10', note='Form required: the solution with a check. x/(x - 9) = 10.'),
      ],
      back=[
          B('Write exact logarithmic solutions of exponential equations', 'HSF-LE.A.4', [
              sa('Solve 3^x = 81.', 'x =', key='4', note='Any equivalent form.'),
              mc('Solve e^x = 5 exactly.', ['x = ln 5', 'x = 5/e', 'x = e⁵', 'x = log 5'], note='ln is the inverse of e^x; log 5 is base 10.'),
              tf('log_b y = x means b^x = y.', key=True, note='Definition.'),
              mc('5² = 25 written as a logarithm is', ['log₅ 25 = 2', 'log₂ 25 = 5', 'log₂₅ 5 = 2', 'log₅ 2 = 25'], note='Definition.'),
              sa('Solve 10^x = 1000.', 'x =', key='3', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot convert forms.', 'log equations are solved by converting to exponential form.', 'converts between forms.')),
          B('Check for extraneous solutions', 'HSA-REI.A.2', [
              mc('Check x = -2 in log₂ x + log₂(x - 2) = 3.', [
                  'log₂(-2) is undefined, so x = -2 is not a solution.', 'log₂(-2) = -1, so x = -2 is a solution.', '(-2)(-4) = 8 = 2³, so x = -2 is a solution.', 'log₂(-2) = 1, so the left side is 3 and x = -2 is a solution.'],
                 note='Logarithms of negative numbers are undefined; the product check skips the domain.'),
              sa('Check x = 4 in log₂ x + log₂(x - 2) = 3: find the value of the left side, then say whether x = 4 is a solution.', ['Left side:', 'Solution? (Yes or No)'], key='3; Yes',
                 note='Form required: both. log₂ 4 + log₂ 2 = 2 + 1 = 3.'),
              tf('Combining logs can introduce solutions outside the original domain.', key=True, note='log a + log b = log(ab) needs a, b > 0.'),
              mc('Which value is excluded from log(x - 9)?', ['x = 5', 'x = 10', 'x = 20', 'x = 100'], note='x - 9 > 0.'),
              sa('Solve x(x - 2) = 8.', 'x =', key='4 or -2', note='Form required: both.'),
          ], align='exact',
            why=why('the student keeps invalid solutions.', 'log domains reject some candidates.', 'checks candidates.')),
          B('Domains of logarithmic expressions', 'HSF-IF.B.5', [
              sa('Give the domain of log₅(x - 1).', 'Answer:', key='x > 1', note='Any equivalent form.'),
              sa('Give the domain of ln(x + 2).', 'Answer:', key='x > -2', note='Any equivalent form.'),
              tf('log 0 = 0.', key=False, note='No power of 10 equals 0, so log 0 is undefined (log 1 = 0).'),
              mc('The domain of log₂ x + log₂(x - 2) is', ['x > 2', 'x > 0', 'x ≠ 2', 'all reals'], note='Both inputs positive.'),
              sa('Give the domain of log x - log(x - 9).', 'Answer:', key='x > 9', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student ignores the domain.', 'the domain decides extraneous solutions.', 'finds log domains.')),
      ],
      f1=B('Use log properties and change of base in equations', 'HSF-BF.B.5', [
          sa('Solve log₂(x + 6) - log₂ x = 2.', 'x =', key='2', note='Any equivalent form. (x + 6)/x = 4.'),
          sa('Solve log₄ x = log₂ 3. (Hint: change of base.)', 'x =', key='9', note='Any equivalent form. log₄ x = (log₂ x)/2.'),
          tf('log₂(x + 6) - log₂ x = log₂((x + 6)/x) for x > 0.', key=True, note='Quotient property.'),
          mc('log(x + 1) + log(x - 1) = log 8 has solution', ['x = 3', 'x = -3 and 3', 'x = 8', 'no solution'], note='x² - 1 = 8; -3 rejected.'),
          mc('Why does log₂(x - 5) = log₂(1 - x) have no solution?', [
                        'Both sides are defined only if x > 5 and x < 1 at the same time, which is impossible.',
                        'Setting x - 5 = 1 - x gives x = 3, which is a solution, so the equation does have one.',
                        'Logarithms with base 2 can never be equal to each other.',
                        'The equation has a solution only when x is negative.'],
                       note='The candidate x = 3 makes both arguments negative. The others accept x = 3 without checking the domain, invent a condition about negative x, or claim logarithms cannot be equal.'),
      ], prog='same-course deepening', demand='Combine log properties, change of base, and domain reasoning.'),
      f2=B('Check logarithmic solutions graphically', 'HSA-REI.D.11', [
          mc('How do the graphs of y = log₂ x + log₂(x - 2) and y = 3 show that the only solution is x = 4?', [
              'They intersect only at x = 4; the left graph exists only for x > 2, so there is no point at x = -2.',
              'They intersect at x = 4 and at x = -2, so both values are solutions of the equation.',
              'They never intersect, so x = 4 must come from the algebra only.',
              'They intersect at y = 4, which is the solution of the equation.'],
             note='Graphs show only points in the domain.'),
          sa('Use a graph or table to approximate the solution of ln x = 2 - x to the nearest hundredth.' + TECH, 'x ≈', key='1.56', note='Accept 1.55 to 1.56 (root 1.5571).'),
          tf('An extraneous solution of a log equation corresponds to no intersection point.', key=True, note='Outside the domain.'),
          mc('The graphs of y = log x and y = 1 meet at', ['x = 10', 'x = 1', 'x = 0', 'x = e'], note='log 10 = 1.'),
          mc('Why can ln x = 2 - x not be solved exactly with logarithm rules?', [
                        'x appears both inside a logarithm and outside it, so no algebraic step isolates x.',
                        'ln x is undefined for every x, so the equation has no solution at all.',
                        'The equation has infinitely many solutions, so no single exact value exists.',
                        'Logarithm rules apply only to equations with base-10 logarithms.'],
                       note='Such equations are solved with graphs or tables. The others are false: ln x is defined for x > 0, the equation has one solution, and the rules apply to every base.'),
      ], prog='cross-standard extension', demand='Use graphs to confirm algebraic solutions and approximate non-algebraic ones.',
        builds='Builds on FORWARD 1: domain reasoning about log equations is seen as where the graphs exist and meet.')),

    # ------------------------------------------------------------------ 81. TF.A.3 special triangles and related angles
    S('HSF-TF.A.3', 'Derive values from special triangles and relate π - x, π + x, 2π - x to x',
      target='Use special right triangles to find exact values at π/6, π/4, π/3, and use the unit circle to express values at π - x, π + x, and 2π - x in terms of x', strand='advanced', covers=['TF3-special'],
      main=[
          mc('A 30°-60°-90° triangle with hypotenuse 1 is half of an equilateral triangle with side 1. Which derivation of sin(π/3) and cos(π/3) is correct?', [
              'The short leg is 1/2 and the long leg is √(1 - 1/4) = √3/2. The angle π/3 is opposite the long leg, so sin(π/3) = √3/2 and cos(π/3) = 1/2.',
              'The short leg is 1/2 and the long leg is √(1 - 1/4) = √3/2. The angle π/3 is opposite the short leg, so sin(π/3) = 1/2 and cos(π/3) = √3/2.',
              'The legs are 1/2 and 1 - 1/2 = 1/2, so sin(π/3) = cos(π/3) = 1/2.',
              'The long leg is √(1 + 1/4) = √5/2, so sin(π/3) = √5/2.'],
             note='Halving the base gives 1/2; the Pythagorean Theorem gives √3/2; the larger angle is opposite the longer leg. The others put π/3 opposite the short leg, subtract lengths instead of using the Pythagorean Theorem, or add instead of subtracting squares.'),
          mc('Which derivation of tan(π/4) from a 45°-45°-90° triangle is correct?', [
              'The two legs are equal, so tan(π/4) = opposite/adjacent = 1.',
              'The legs are 1 and √2, so tan(π/4) = opposite/adjacent = 1/√2 = √2/2.',
              'tan(π/4) = sin(π/4) + cos(π/4) = √2.',
              'The hypotenuse is twice a leg, so tan(π/4) = 1/2.'],
             note='Equal legs make the ratio 1. The others use the hypotenuse as a leg, add instead of dividing, or use a 30°-60°-90° fact.'),
          mc('Which uses sin(π - x) = sin x to find sin(5π/6) exactly, with a correct unit-circle explanation?', [
                        'sin(5π/6) = sin(π/6) = 1/2: the points for x and π - x are reflections over the y-axis, so they have the same y-coordinate.',
                        'sin(5π/6) = -sin(π/6) = -1/2: the points for x and π - x are reflections over the x-axis, so their y-coordinates are opposite.',
                        'sin(5π/6) = sin(π/6) = 1/2: the points for x and π - x are reflections over the x-axis, so they have the same y-coordinate.',
                        'sin(5π/6) = cos(π/6) = √3/2: the point for π - x is a quarter turn from the point for x, so y becomes x.'],
                       note='(cos x, sin x) and (-cos x, sin x) mirror over the y-axis. The others name the x-axis reflection (which changes the sign of y), or treat π - x as a quarter turn.'),
          sa('Use cos(π + x) = -cos x to find cos(7π/6) exactly.', 'cos(7π/6) =', key='-√3/2', note='cos(7π/6) = -cos(π/6) = -√3/2.'),
          sa('Use tan(2π - x) = -tan x to find tan(5π/3) exactly.', 'tan(5π/3) =', key='-√3', note='tan(5π/3) = -tan(π/3) = -√3.'),
      ],
      back=[
          B('Special right triangle side ratios', 'HSG-SRT.C.6', [
              sa('A 30°-60°-90° triangle has hypotenuse 2. Give the lengths of its legs exactly.', ['Short leg:', 'Long leg:'], key='1; √3', note='Form required: both. Half of an equilateral triangle with side 2.'),
              sa('Give the hypotenuse of a 45°-45°-90° triangle with legs 1.', 'Answer:', key='√2', note='Any equivalent form.'),
              tf('In a 30°-60°-90° triangle, the shortest side is half the hypotenuse.', key=True, note='Half of an equilateral triangle.'),
              mc('cos 30° equals', ['√3/2', '1/2', '√2/2', '√3'], note='Adjacent/hypotenuse.'),
              sa('Give tan 60°.', 'Answer:', key='√3', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student does not know the ratios.', 'derivations use the triangles.', 'uses special triangles.')),
          B('Unit-circle values in all quadrants', 'HSF-TF.A.2', [
              sa('Give cos(5π/6) exactly.', 'Answer:', key='-√3/2', note='Any equivalent form.'),
              sa('Give sin(7π/6) exactly.', 'Answer:', key='-1/2', note='Any equivalent form.'),
              tf('sin is positive in quadrant II.', key=True, note='y > 0.'),
              mc('Which quadrant contains 5π/3?', ['IV', 'III', 'II', 'I'], note='Between 3π/2 and 2π.'),
              sa('Give tan(π/3).', 'Answer:', key='√3', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot place angles.', 'the relations map angles to the first quadrant.', 'finds unit-circle values.')),
          B('The Pythagorean Theorem', '8.G.B.7', [
              sa('A right triangle has hypotenuse 1 and leg 1/2. Find the other leg.', 'Answer:', key='√3/2', note='Any equivalent form.'),
              sa('A right isosceles triangle has hypotenuse 1. Find each leg.', 'Answer:', key='√2/2', note='Any equivalent form.'),
              tf('(1/2)² + (√3/2)² = 2.', key=False, note='1/4 + 3/4 = 1.'),
              mc('Legs 1 and 1 give hypotenuse', ['√2', '2', '1', '√3'], note='√2.'),
              sa('Find x if x² + x² = 1 (x > 0).', 'x =', key='√2/2', note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot compute the missing side.', 'the derivation needs it.', 'uses the Pythagorean Theorem.')),
      ],
      f1=B('Derive more special values and the reflection identities', 'HSF-TF.A.3', [
          mc('Which derivation of tan(π/6) from a special triangle is correct?', [
              'In the 30°-60°-90° triangle with hypotenuse 1, π/6 is opposite the leg 1/2 and adjacent to the leg √3/2, so tan(π/6) = (1/2)/(√3/2) = 1/√3 = √3/3.',
              'In the 30°-60°-90° triangle with hypotenuse 1, π/6 is opposite the leg √3/2 and adjacent to the leg 1/2, so tan(π/6) = (√3/2)/(1/2) = √3 exactly.',
              'The opposite side is half the hypotenuse, so tan(π/6) = 1/2.',
              'tan(π/6) = (1/2)/(√3/2) = √3/2.'],
             note='Opposite over adjacent, then simplify (1/2)/(√3/2) = 1/√3 = √3/3. The others use the angle π/3, give sin(π/6) instead, or simplify the quotient incorrectly.'),
          mc('Which unit-circle argument explains why cos(π - x) = -cos x?', [
              'The points for x and π - x are reflections of each other over the y-axis, so their x-coordinates (the cosines) are opposites.',
              'The points for x and π - x are reflections of each other over the x-axis, so their x-coordinates (the cosines) are opposites.',
              'cos(π - x) = cos π - cos x = -1 - cos x.',
              'cos(π - π/3) = -1/2 = -cos(π/3), so the rule always holds.'],
             note='Reflection over the y-axis changes the sign of x and keeps y. The others name the wrong reflection (it keeps x), distribute cosine over a difference, or check one value.'),
          tf('sin(π + x) = -sin x.', key=True, note='Rotation by π.'),
          mc('cos(2π - x) equals', ['cos x', '-cos x', 'sin x', '-sin x'], note='Reflection over the x-axis.'),
          sa('Use sin(2π - x) = -sin x to find sin(11π/6) exactly.', 'sin(11π/6) =', key='-1/2', note='sin(11π/6) = -sin(π/6) = -1/2.'),
      ], prog='same-course deepening', demand='Derive all the special values and prove the reflection relations.'),
      f2=B('Explain symmetry and periodicity', 'HSF-TF.A.4', [
          mc('Which unit-circle reasoning explains why sin(-x) = -sin x?', [
                        'The points for x and -x are reflections over the x-axis, so their y-coordinates are opposites.',
                        'The points for x and -x are reflections over the y-axis, so their y-coordinates are opposites.',
                        'The points for x and -x are the same point, so their y-coordinates are equal.',
                        'The points for x and -x are opposite points, so their x-coordinates are equal.'],
                       note='Equal arcs in opposite directions from (1, 0) mirror over the x-axis. The others call the points opposite or the same, or name the y-axis reflection, which keeps the y-coordinate.'),
          mc('Is cos an even or odd function, and why?', [
              'Even: the points for x and -x have the same x-coordinate, so cos(-x) = cos x.', 'Odd: the points for x and -x have opposite x-coordinates, so cos(-x) = -cos x.',
              'Even: the points for x and -x have the same y-coordinate, so cos(-x) = cos x.', 'Neither: cos(-x) is not related to cos x.'],
             note='Reflection over the x-axis keeps the x-coordinate.'),
          tf('sin(x + 2π) = sin x.', key=True, note='Period.'),
          mc('tan(-π/4) equals', ['-1', '1', '0', 'undefined'], note='Odd.'),
          mc('Using 2π - x = -x + 2π, which reasoning explains why tan(2π - x) = -tan x?', [
              'tan(-x + 2π) = tan(-x) by periodicity, and tan is odd, so tan(-x) = -tan x.',
              'tan(-x + 2π) = tan(-x) + tan(2π) = -tan x + 1.',
              'tan(-x + 2π) = tan x by periodicity, and tan is even.',
              'tan(2π - x) = 2π - tan x, because tan distributes over subtraction.'],
             note='Period π (so also 2π) and oddness.'),
      ], prog='cross-standard extension', demand='Generalize the reflection relations into odd/even symmetry and periodicity.',
        builds='Builds on FORWARD 1: the reflection identities combine into symmetry and period statements.')),

    # ------------------------------------------------------------------ 82. TF.A.4 symmetry and periodicity
    S('HSF-TF.A.4', 'Explain the symmetry and periodicity of trigonometric functions with the unit circle',
      target='Use the unit circle to explain odd/even symmetry and periodicity of sine, cosine, and tangent, and use them to evaluate', strand='advanced', covers=['TF4-symmetry'],
      main=[
          mc('Which unit-circle explanation shows why sin(-x) = -sin x?', [
              'The points for x and -x are (a, b) and (a, -b), reflections over the x-axis, so the sines b and -b are opposites.',
              'The points for x and -x are (a, b) and (-a, b), reflections of each other over the y-axis, so their sines are opposites.',
              'A negative sign can always be moved outside a function, so sin(-x) = -sin x.',
              'sin(-π/6) = -1/2 = -sin(π/6), so the rule always holds.'],
             note='Equal arcs in opposite directions from (1, 0) give points that mirror over the x-axis. The others name the wrong reflection, use a false general rule (cos(-x) = cos x, not -cos x), or check one value.'),
          mc('Which unit-circle explanation shows why cos(x + 2π) = cos x?', [
              'Adding 2π travels one full turn around the unit circle and ends at the same point, so the x-coordinate (the cosine) is the same.',
              'cos(x + 2π) = cos x + cos 2π = cos x + 1.',
              'Adding 2π moves the point to the opposite side of the unit circle, and opposite points on the circle have the same x-coordinate, so the cosine is the same.',
              'cos(0 + 2π) = 1 = cos 0, so the rule always holds.'],
             note='The circumference is 2π, so x and x + 2π give the same point. The others distribute cosine over a sum, describe the wrong motion, or check one value.'),
          mc('Which unit-circle explanation shows why tan(x + π) = tan x?', [
              'Adding π gives the opposite point (-a, -b) of (a, b), and tan = (-b)/(-a) = b/a, the same ratio.',
              'Adding π gives the point (a, -b), a reflection over the x-axis, so tan(x + π) = -b/a = -tan x, which is not tan x.',
              'Adding π travels a full turn, so the point is the same.',
              'tan(π/4 + π) = 1 = tan(π/4), so the rule always holds.'],
             note='Half a turn takes (a, b) to (-a, -b); both coordinates change sign, so the ratio is unchanged. The others use the wrong point, mistake π for a full turn, or check one value.'),
          mc('Use symmetry to evaluate cos(-2π/3).', [
                        '-1/2, because cos is even: cos(-2π/3) = cos(2π/3) = -1/2', '1/2, because cos is odd: cos(-2π/3) = -cos(2π/3) = 1/2', '-√3/2, because cos(-2π/3) = -sin(2π/3)', '1/2, because cos is even: cos(-2π/3) = cos(π/3) = 1/2'],
                       note='cos(-x) = cos x. The others call cos odd, use sine instead of cosine, or use the reference angle π/3 with the wrong sign.'),
          mc('Is f(x) = sin x cos x even, odd, or neither?', [
                        'Odd: f(-x) = sin(-x)cos(-x) = (-sin x)(cos x) = -f(x)', 'Even: f(-x) = sin(-x)cos(-x) = sin x cos x = f(x)', 'Neither: sin is odd but cos is even', 'Even: a product of two functions is always even'],
                       note='Odd × even = odd. The others use sin(-x) = sin x, judge the product by its factors without computing f(-x), or use a false rule about products.'),
      ],
      back=[
          B('Explain the unit-circle definition', 'HSF-TF.A.2', [
              mc('Which point on the unit circle represents angle x?', ['(cos x, sin x)', '(sin x, cos x)', '(x, sin x)', '(cos x, x)'], note='Definition.'),
              sa('In which direction from (1, 0) does a negative angle go on the unit circle? Answer Clockwise or Counterclockwise.', 'Answer:', key='Clockwise', note='Positive angles go counterclockwise.'),
              tf('tan x = sin x/cos x.', key=True, note='Definition.'),
              mc('The point for angle π is', ['(-1, 0)', '(0, 1)', '(1, 0)', '(0, -1)'], note='Half turn.'),
              sa('Give cos(2π/3).', 'Answer:', key='-1/2', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot use the definition.', 'explanations rest on it.', 'uses the unit circle.')),
          B('Even and odd functions', 'HSF-BF.B.3', [
              mc('Which is the definition of an even function?', ['f(-x) = f(x) for every x in the domain', 'f(-x) = -f(x) for every x in the domain', 'f(x) > 0 for every x in the domain', 'f(x + 2π) = f(x) for every x in the domain'], note='Symmetric about the y-axis.'),
              mc('Which is the definition of an odd function?', ['f(-x) = -f(x) for every x in the domain', 'f(-x) = f(x) for every x in the domain', 'f(x) < 0 for every x in the domain', 'f(x + π) = -f(x) for every x in the domain'], note='Symmetric about the origin.'),
              tf('An odd function\'s graph is symmetric about the origin.', key=True, note='Rotation by 180°.'),
              mc('x³ is', ['odd', 'even', 'neither', 'both'], note='(-x)³ = -x³.'),
              sa('Is the product of an odd function and an even function odd or even? Answer Odd or Even.', 'Answer:', key='Odd', note='f(-x)g(-x) = (-f(x))g(x).'),
          ], align='exact',
            why=why('the student lacks the definitions.', 'symmetry statements use them.', 'defines even and odd.')),
          B('Reflect points over the axes', '8.G.A.3', [
              mc('Reflect (a, b) over the x-axis.', ['(a, -b)', '(-a, b)', '(-a, -b)', '(b, a)'], note='The y-coordinate changes sign.'),
              mc('Rotate (a, b) by 180° about the origin.', ['(-a, -b)', '(a, -b)', '(-a, b)', '(-b, a)'], note='Both coordinates change sign; (-b, a) is a 90° rotation.'),
              tf('Reflecting over the x-axis keeps the y-coordinate.', key=False, note='(a, b) → (a, -b): the x-coordinate stays and y changes sign.'),
              mc('Reflecting (0.6, 0.8) over the x-axis gives', ['(0.6, -0.8)', '(-0.6, 0.8)', '(-0.6, -0.8)', '(0.8, 0.6)'], note='Negate y.'),
              mc('Rotate the point (√3/2, 1/2) by 180° about the origin.', ['(-√3/2, -1/2)', '(√3/2, -1/2)', '(-√3/2, 1/2)', '(-1/2, √3/2)'], note='Both coordinates change sign; the last is a 90° rotation.'),
          ], align='supporting',
            why=why('the student cannot describe the motions.', 'symmetry and periodicity are motions of the circle.', 'reflects and rotates points.')),
      ],
      f1=B('Use periodicity and symmetry to evaluate and simplify', 'HSF-TF.A.4', [
          sa('Find sin(17π/6) exactly.', 'Answer:', key='1/2', note='Any equivalent form. 17π/6 - 2π = 5π/6.'),
          sa('Find tan(-11π/4) exactly.', 'Answer:', key='1', note='Any equivalent form. tan(-11π/4) = tan(-11π/4 + 3π) = tan(π/4).'),
          tf('cos(x + π) = -cos x.', key=True, note='Opposite point.'),
          mc('sin(x + π) + sin x equals', ['0', '2 sin x', '1', 'sin 2x'], note='sin(x + π) = -sin x.'),
          sa('Simplify cos(-x) + cos(x + 2π).', 'Answer:', key='2cos x', note='Any equivalent form.'),
      ], prog='same-course deepening', demand='Combine periodicity and symmetry to evaluate and simplify.'),
      f2=B('Restrict trigonometric functions so they have inverses', 'HSF-TF.B.6', [
          mc('How does periodicity prevent sin x from having an inverse on all real numbers?', [
                                  'Each value repeats every 2π, so an output does not determine its input.', 'Periodic functions are undefined at multiples of 2π, which breaks the domain.', 'Periodicity makes sin increasing everywhere, so it has no turning points.', 'Each value appears only once in every period, so periodicity changes nothing.'],
                                 note='Not one-to-one. The others are false: values repeat, sin is not increasing everywhere, and it is defined at multiples of 2π.'),
          mc('What is the restricted domain used for tan x, and why?', [
              '-π/2 < x < π/2: tan increases there and takes every real value once.', '0 < x < π: tan is defined and increasing everywhere there.', '-π/2 ≤ x ≤ π/2: tan is defined at both endpoints.', '0 ≤ x < 2π: tan takes every real value there.'],
             note='tan is undefined at ±π/2 and at π/2 inside (0, π).'),
          tf('arccos gives values between 0 and π.', key=True, note='Restricted range.'),
          mc('arctan(-1) equals', ['-π/4', '3π/4', '7π/4', 'π/4'], note='In (-π/2, π/2).'),
          mc('Why is arcsin(-1/2) = -arcsin(1/2)?', [
                        'sin is odd on [-π/2, π/2], so sin(-π/6) = -1/2, giving arcsin(-1/2) = -π/6 = -arcsin(1/2).',
                        'sin is even on [-π/2, π/2], so sin(-π/6) = 1/2, giving arcsin(-1/2) = π/6.',
                        'arcsin(-1/2) = 7π/6 because sin(7π/6) = -1/2, which is -arcsin(1/2).',
                        'A minus sign can always be moved outside any function, so arcsin(-a) = -arcsin(a).'],
                       note='Oddness on the restricted domain carries over to the inverse. The others use an output outside [-π/2, π/2], call sin even, or use a false rule about moving a minus sign.'),
      ], prog='cross-standard extension', demand='Use periodicity and symmetry to justify domain restrictions for inverses.',
        builds='Builds on FORWARD 1: periodicity, which repeats values, is exactly what the restriction removes.')),

    # ------------------------------------------------------------------ 83. TF.B.6 restrict for inverses
    S('HSF-TF.B.6', 'Choose and justify domain restrictions that make trigonometric functions invertible',
      target='State and justify the restricted domains for sine, cosine, and tangent, and evaluate inverse trigonometric functions on them', strand='advanced', covers=['TF6-restrict'],
      main=[
          mc('Why does sin x have no inverse on all real numbers, and on which restricted domain does it have one?', [
                        'sin repeats values, so it is not one-to-one; on -π/2 ≤ x ≤ π/2 it is increasing and takes each value in [-1, 1] once.',
                        'sin is not defined for all real numbers; on 0 ≤ x ≤ π it is defined and takes each value in [-1, 1] once.',
                        'sin repeats values, so it is not one-to-one; on 0 ≤ x ≤ π it is increasing and takes each value in [-1, 1] once.',
                        'sin has outputs greater than 1 for large x; on -π ≤ x ≤ π it takes each value in [-1, 1] exactly once.'],
                       note='On [0, π] sin rises then falls; on [-π, π] values repeat. The others use [0, π] or [-π, π], where values repeat, or claim false facts about the domain and outputs of sin.'),
          mc('What is the standard restricted domain of cos x, and why does it work?', [
                        '0 ≤ x ≤ π: cos decreases from 1 to -1 there, taking each value once.',
                        '-π/2 ≤ x ≤ π/2: cos increases from -1 to 1 there, taking each value once.',
                        '0 ≤ x ≤ 2π: cos takes every value from -1 to 1 there, so it is enough.',
                        '-π ≤ x ≤ 0: cos decreases from 1 to -1 there, taking each value once.'],
                       note='On [-π/2, π/2] cos rises and falls; on [-π, 0] it increases. The others use [-π/2, π/2], where cos rises then falls, [0, 2π], where values repeat, or [-π, 0], where cos increases.'),
          mc('What is the standard restricted domain of tan x, and why does it work?', [
                        '-π/2 < x < π/2: tan increases from -∞ to ∞ there, taking each real value once.',
                        '0 < x < π: tan is defined and increasing at every point of that interval.',
                        '-π/2 ≤ x ≤ π/2: tan increases there, including its values at both endpoints.',
                        '0 ≤ x < π/2: tan increases there and takes each real value exactly once.'],
                       note='tan is undefined at ±π/2 and takes only nonnegative values on [0, π/2). The others include π/2 (where tan is undefined), include the endpoints ±π/2, or use [0, π/2), which gives only nonnegative values.'),
          mc('What is arcsin(1/2), and why is it not 5π/6?', [
                        'π/6: arcsin outputs only angles in [-π/2, π/2], and 5π/6 is outside that interval.',
                        '5π/6: arcsin gives the largest angle in [0, 2π) whose sine is 1/2.',
                        'π/6 and 5π/6: arcsin gives every angle in [0, 2π) whose sine is 1/2.',
                        'π/3: arcsin(1/2) is the angle whose cosine is 1/2, not 5π/6.'],
                       note='An inverse function has one output. The others give an angle outside the range of arcsin, give two outputs for one input, or use the cosine value.'),
          sa('Evaluate arccos(-1/2) exactly.', 'Answer:', key='2π/3', note='Form required: exact value in [0, π].'),
      ],
      back=[
          B('Restrict a domain to make a function invertible', 'HSF-BF.B.4.d', [
              mc('On which domain is f(x) = x² invertible?', ['x ≥ 0', 'all real numbers', '-1 ≤ x ≤ 1', 'x ≥ -2'], note='f is one-to-one on one side of the vertex only.'),
              mc('Why must a function be strictly increasing or strictly decreasing on an interval to be invertible there?', [
                                              'Then no output repeats on the interval, so each output comes from exactly one input.', 'Then the function is defined at every real number, inside and outside the interval.', 'Then the function has no zeros on the interval, so it never crosses the x-axis.', 'Then the outputs are all positive on the interval, so each can be undone.'],
                                             note='Strict monotonicity on an interval implies one-to-one there. The others name properties (domain, zeros, positive outputs) that do not make a function one-to-one.'),
              tf('A function that is always increasing on an interval is one-to-one there.', key=True, note='Monotonic.'),
              mc('f(x) = (x - 1)² is one-to-one on', ['x ≥ 1', 'all reals', '-1 ≤ x ≤ 3', 'x ≥ 0'], note='One side of the vertex.'),
              mc('Which is the inverse of f(x) = x² on x ≥ 0?', ['√x', '-√x', 'x/2', '1/x²'], note='The outputs of the inverse must be ≥ 0.'),
          ], align='exact',
            why=why('the student does not know why restrictions are made.', 'the trig case uses the same idea.', 'restricts domains.')),
          B('Exact values on the unit circle', 'HSF-TF.A.2', [
              sa('Give sin(π/6) and sin(5π/6) exactly.', ['sin(π/6) =', 'sin(5π/6) ='], key='1/2; 1/2', note='Form required: both.'),
              sa('Give cos(2π/3) and cos(4π/3) exactly.', ['cos(2π/3) =', 'cos(4π/3) ='], key='-1/2; -1/2', note='Form required: both.'),
              tf('tan(π/4) = tan(3π/4).', key=False, note='tan(π/4) = 1 and tan(3π/4) = -1.'),
              mc('Which angle in [0, π] has cos = -1/2?', ['2π/3', '4π/3', 'π/3', '5π/6'], note='Quadrant II.'),
              sa('Give sin(-π/6).', 'Answer:', key='-1/2', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot evaluate inverses exactly.', 'inverse values are exact angles.', 'knows exact values.')),
          B('Periodicity of trigonometric functions', 'HSF-TF.A.4', [
              sa('What is the period of sin x?', 'Answer:', key='2π', note='Any equivalent form.'),
              sa('What is the period of tan x?', 'Answer:', key='π', note='Any equivalent form.'),
              tf('A periodic function cannot be one-to-one on its whole domain.', key=True, note='Values repeat.'),
              mc('sin x = 0 for', ['x = kπ', 'x = 2kπ only', 'x = π/2 + kπ', 'no x'], note='Every multiple of π.'),
              mc('Which two angles both have cosine 1?', ['0 and 2π', '0 and π', 'π/2 and 3π/2', 'π and 2π'], note='cos x = 1 at multiples of 2π.'),
          ], align='supporting',
            why=why('the student does not see repetition.', 'repetition is why restriction is needed.', 'uses periodicity.')),
      ],
      f1=B('Compose trigonometric functions with their inverses', 'HSF-TF.B.6', [
          sa('Evaluate arcsin(sin(5π/6)).', 'Answer:', key='π/6', note='Any equivalent form.'),
          sa('Evaluate sin(arcsin(0.3)).', 'Answer:', key='0.3', note='Any equivalent form.'),
          tf('arccos(cos x) = x for every real x.', key=False, note='Only for 0 ≤ x ≤ π.'),
          mc('arctan(tan(3π/4)) equals', ['-π/4', '3π/4', 'π/4', '-3π/4'], note='Into (-π/2, π/2).'),
          mc('What are the domain and range of arccos?', ['domain [-1, 1]; range [0, π]', 'domain [0, π]; range [-1, 1]', 'domain [-1, 1]; range [-π/2, π/2]', 'all real numbers; range [0, π]'],
             note='arccos inverts cos on [0, π].'),
      ], prog='same-course deepening', demand='Track how the restricted domain affects compositions with inverses.'),
      f2=B('Solve trigonometric equations with inverses', 'HSF-TF.B.7', [
          sa('Solve sin x = 0.4 on 0 ≤ x < 2π. Give both solutions to the nearest hundredth, separated by a comma.' + TECH, 'x ≈', key='{0.41, 2.73}', note='Form required: both. arcsin(0.4) and π - arcsin(0.4).'),
          sa('Solve cos x = 0.4 on 0 ≤ x < 2π. Give both solutions to the nearest hundredth, separated by a comma.' + TECH, 'x ≈', key='{1.16, 5.12}', note='Form required: both. arccos(0.4) and 2π - arccos(0.4).'),
          tf('For 0 < c < 1, arcsin c gives only one of the two solutions of sin x = c on [0, 2π).', key=True, note='The other is π - arcsin c.'),
          mc('The second solution of sin x = c in [0, 2π) (with 0 < c < 1) is', ['π - arcsin c', 'π + arcsin c', '2π - arcsin c', '-arcsin c'], note='Quadrant II.'),
          mc('For -1 < c < 1, how is the restricted range of arccos used to find both solutions of cos x = c on [0, 2π)?', [
              'arccos c gives the solution in (0, π); the other is 2π - arccos c, by symmetry over the x-axis.',
              'arccos c gives the solution in (0, π); the other is π - arccos c, by symmetry over the y-axis.',
              'arccos c gives both solutions at once, because its range is the whole interval [0, 2π).',
              'arccos c gives the solution in (-π/2, π/2); the other is arccos c + π, by periodicity.'],
             note='cos is even: cos(2π - a) = cos(-a) = cos a.'),
      ], prog='cross-standard extension', demand='Use inverse values plus symmetry to find all solutions in an interval.',
        builds='Builds on FORWARD 1: knowing that inverses return one restricted angle leads to recovering the others.')),

    # ------------------------------------------------------------------ 84. TF.B.7 solve trigonometric equations
    S('HSF-TF.B.7', 'Solve trigonometric equations in models with inverse functions',
      target='Solve trigonometric equations, including model equations, with inverse functions, and find all solutions in a given interval', strand='advanced', covers=['TF7-solve'],
      main=[
          sa('Solve 2sin x - 1 = 0 for 0 ≤ x < 2π. Give exact values.', 'x =', key='π/6 and 5π/6', note='Form required: both.'),
          sa('Solve 3cos x = -2 for 0 ≤ x < 2π. Give both solutions to the nearest hundredth, separated by a comma.' + TECH, 'x ≈', key='{2.30, 3.98}', note='Form required: both. arccos(-2/3) and 2π - arccos(-2/3).'),
          sa("A Ferris wheel rider's height is h(t) = 12 + 10sin(πt/15) m after t seconds. Find every time in 0 ≤ t < 30 when h = 17 m, in seconds, separated by commas.", 't =', key='{2.5, 12.5}', note='Form required: both. sin(πt/15) = 1/2 gives πt/15 = π/6 or 5π/6.'),
          sa('Harbor depth is d(t) = 5 + 4cos(πt/6) ft after t hours. Find every time in 0 ≤ t < 12 when d = 7 ft, in hours, separated by commas.', 't =', key='{2, 10}', note='Form required: both. cos(πt/6) = 1/2 gives πt/6 = π/3 or 5π/3.'),
          sa('Solve tan x = 3 for 0 ≤ x < 2π. Give both solutions to the nearest hundredth, separated by a comma.' + TECH, 'x ≈', key='{1.25, 4.39}', note='Form required: both. arctan 3 and arctan 3 + π.'),
      ],
      back=[
          B('Evaluate inverse trigonometric functions on restricted domains', 'HSF-TF.B.6', [
              sa('Evaluate arcsin(1/2).', 'Answer:', key='π/6', note='Any equivalent form.'),
              sa('Evaluate arccos(1/2).', 'Answer:', key='π/3', note='Any equivalent form.'),
              tf('arctan 3 is between 0 and π/2.', key=True, note='Positive input.'),
              mc('arccos(-2/3) is in quadrant', ['II', 'I', 'III', 'IV'], note='Range [0, π], negative cosine.'),
              sa('Evaluate arctan 3 to the nearest hundredth.' + TECH, 'Answer:', key='1.25', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot get the first solution.', 'inverses give one solution.', 'evaluates inverses.')),
          B('Parameters of sinusoidal models', 'HSF-TF.B.5', [
              sa('In h(t) = 12 + 10sin(πt/15), what is the period?', 'Answer:', key='30 s', note='Any equivalent form.'),
              sa("A rider's height is h(t) = 12 + 10sin(πt/15) m. Setting h(t) = 17 gives an equation sin(πt/15) = c. Find c.", 'c =', key='1/2', note='10sin(πt/15) = 5.'),
              tf('d(t) = 5 + 4cos(πt/6) has a maximum of 5.', key=False, note='The maximum is 5 + 4 = 9; 5 is the midline.'),
              mc('Isolating the cosine in 5 + 4cos(πt/6) = 7 gives', ['cos(πt/6) = 1/2', 'cos(πt/6) = 7/4', 'cos(πt/6) = 2', 'cos(πt/6) = 3'], note='Subtract 5, divide by 4.'),
              sa('What is the midline of d(t)?', 'Answer:', key='d = 5', note='Any equivalent form.'),
          ], align='exact',
            why=why('the student cannot isolate the trig part.', 'model equations need it first.', 'reads and rearranges models.')),
          B('Symmetry of unit-circle solutions', 'HSF-TF.A.2', [
              sa('Give both angles in [0, 2π) with sin = 1/2.', 'Answer:', key='π/6 and 5π/6', note='Form required: both.'),
              sa('Give both angles in [0, 2π) with cos = 1/2.', 'Answer:', key='π/3 and 5π/3', note='Form required: both.'),
              tf('tan x = c has two solutions in [0, 2π) that differ by π.', key=True, note='Period π.'),
              mc('For -1 < c < 1, cos x = c has a solution a in (0, π). The other solution in [0, 2π) is', ['2π - a', 'π - a', 'π + a', '-a'], note='Reflection over the x-axis; -a is not in [0, 2π).'),
              sa('Give both angles in [0, 2π) with tan = 1.', 'Answer:', key='π/4 and 5π/4', note='Form required: both.'),
          ], align='exact',
            why=why('the student finds only one solution.', 'all solutions in the interval are required.', 'uses symmetry.')),
      ],
      f1=B('Find all real solutions and solve equations that factor', 'HSF-TF.B.7', [
          mc('Which gives all real solutions of 2sin x - 1 = 0?', ['x = π/6 + 2kπ or x = 5π/6 + 2kπ, k an integer', 'x = π/6 + kπ, k an integer', 'x = π/6 + 2kπ, k an integer', 'x = π/3 + 2kπ or x = 2π/3 + 2kπ, k an integer'],
             note='sin x = 1/2 at π/6 and 5π/6 in each period. π/6 + π gives sin = -1/2.'),
          sa('Solve 2sin²x - sin x = 0 for 0 ≤ x < 2π. List all solutions exactly, separated by commas.', 'x =', key='{0, π/6, 5π/6, π}', note='Form required: all four. sin x(2sin x - 1) = 0.'),
          tf('cos x = 2 has no real solution.', key=True, note='Range.'),
          mc('How many solutions does sin(2x) = 1/2 have in 0 ≤ x < 2π?', ['4', '2', '1', '8'], note='2x runs over two periods.'),
          sa('Solve cos²x = 1/4 for 0 ≤ x < 2π.', 'x =', key='π/3, 2π/3, 4π/3, 5π/3', note='Form required: all four.'),
      ], prog='same-course deepening', demand='Find general solutions and solve equations that factor or involve squares and multiple angles.'),
      f2=B('Solve equations with sum and double-angle identities', 'HSF-TF.C.9', [
          sa('Use sin 2x = 2sin x cos x to solve sin 2x = cos x for 0 ≤ x < 2π.', 'x =', key='π/6, π/2, 5π/6, 3π/2', note='Form required: all four. cos x(2sin x - 1) = 0.'),
          sa('Use cos 2x = 1 - 2sin²x to solve cos 2x = sin x for 0 ≤ x < 2π.', 'x =', key='π/6, 5π/6, 3π/2', note='Form required: all three. 2sin²x + sin x - 1 = 0.'),
          tf('sin(x + π/2) = cos x.', key=True, note='Sum formula.'),
          mc('cos 2x equals', ['cos²x - sin²x', '2cos x', 'cos²x + sin²x', '1 + 2sin²x'], note='Double angle.'),
          mc('Why are identities useful for solving equations that contain different trigonometric functions?', [
                        'They rewrite the equation in one function (or let it factor), so inverse functions can be applied.',
                        'They turn every equation into a linear equation that has exactly one solution.',
                        'They remove the need to check the solutions in the original equation.',
                        'They change the period of each function to 2π, so the graphs match.'],
                       note='For example sin 2x = sin x becomes sin x(2cos x - 1) = 0. The others are false: identities do not make equations linear, do not remove the need to check, and do not change periods.'),
      ], prog='later-course extension', demand='Use addition and double-angle identities (Precalculus) to solve equations.',
        builds='Builds on FORWARD 1: factoring trig equations is extended with identities that create factorable forms.')),
]
