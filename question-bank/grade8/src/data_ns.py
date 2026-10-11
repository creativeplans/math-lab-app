from qb import S, B, sa, mc, tf, plot, work, nl


def line(vmin, vmax, step, pts=None):
    """Number line with every whole number labeled."""
    labels = {v: str(v).replace('-', '−') for v in range(int(vmin), int(vmax) + 1)}
    return nl(vmin, vmax, step, labels=labels, pts=pts or [])


SETS = [
    # ------------------------------------------------------------------ 8.NS.A.1 (classify)
    S('8.NS.A.1', 'Classify numbers as rational or irrational',
      main=[
          mc('Which number is irrational?', ['√15', '√49', '{-7/3}', '0.1212... (the digits 12 repeat)']),
          sa('Is 0.375 rational or irrational? Explain.', 'Answer:', key='Rational. It equals 3/8, a quotient of integers (its decimal ends).'),
          sa('Is √50 rational or irrational? Explain.', 'Answer:',
             key='Irrational. 50 is not a perfect square, so √50 cannot be written as a quotient of integers; its decimal neither ends nor repeats.'),
          tf('Every number whose decimal expansion repeats is rational.', key=True),
          tf('π is rational because it is often written as 3.14.', key=False, note='3.14 is only an approximation; π is irrational.'),
      ],
      back=[
          B('Write a fraction as a terminating or repeating decimal', '7.NS.A.2.d', [
              sa('Write {5/8} as a decimal.', 'Decimal:', key='0.625'),
              sa('Write {2/3} as a decimal.', 'Decimal:', key='0.666... (the 6 repeats)'),
              mc('Which fraction has a repeating decimal?', ['{1/6}', '{1/4}', '{3/5}', '{7/8}']),
              tf('{4/11} = 0.3636... (the digits 36 repeat)', key=True),
              tf('{1/3} = 0.3', key=False, note='1/3 = 0.333..., a repeating decimal.'),
          ]),
          B('Write rational numbers as quotients of integers', '7.NS.A.2.b', [
              sa('Write -2{1/4} as a quotient of two integers.', 'Quotient:', key='-9/4'),
              sa('Write 0.7 as a quotient of two integers.', 'Quotient:', key='7/10'),
              mc('Which number is equal to {-5/6}?', ['{5/-6}', '{-5/-6}', '{6/-5}', '{5/6}']),
              tf('-12 can be written as {-12/1}.', key=True),
              tf('{-3/0} is a rational number.', key=False, note='Division by 0 is undefined.'),
          ]),
      ],
      f1=B('Decide whether sums and products are rational or irrational', 'HSN-RN.B.3', [
          sa('Is 4 + √3 rational or irrational? Explain.', 'Answer:', key='Irrational. A rational number plus an irrational number is irrational.'),
          sa('Is √8 × √2 rational or irrational? Give its value.', 'Answer:', key='Rational; √16 = 4.'),
          mc('Which product is irrational?', ['3√5', '√3 × √12', '0 × √7', '{2/3} × 6']),
          tf('The sum of two rational numbers is always rational.', key=True),
          tf('The product of two irrational numbers is always irrational.', key=False, note='√2 × √2 = 2, which is rational.'),
      ]),
      f2=B('Extend the number system to complex numbers using i', 'HSN-CN.A.1', [
          sa('The number i has i² = -1.\nWrite √-16 in the form bi.', 'Answer:', key='4i'),
          sa('The number i has i² = -1.\nWhat is i⁴?', 'i⁴ =', key='1'),
          mc('The number i has i² = -1.\nWhich number is a solution of x² = -9?', ['3i', '3', '-3', '9i']),
          tf('Every real number a is also a complex number, a + 0i.', key=True),
          tf('√-25 is a real number.', key=False, note='√-25 = 5i, which is not real.'),
      ])),

    # ------------------------------------------------------------------ 8.NS.A.1 (repeating decimal to fraction)
    S('8.NS.A.1', 'Convert a repeating decimal into a fraction',
      main=[
          work('Write 0.444... (the 4 repeats) as a fraction. Show your work.', 'Fraction:',
               method='Any valid method. Example: let x = 0.444...; then 10x = 4.444...; subtracting gives 9x = 4, so x = 4/9.',
               key='4/9'),
          sa('Write 0.2727... (the digits 27 repeat) as a fraction in simplest form.', 'Fraction:', key='3/11', note='27/99 is equal but is not in simplest form.'),
          mc('Which fraction is equal to 0.1666... (the 6 repeats)?', ['{1/6}', '{16/100}', '{1/16}', '{6/10}']),
          tf('2.333... (the 3 repeats) is equal to {7/3}.', key=True),
          tf('0.0909... (the digits 09 repeat) is equal to {9/100}.', key=False, note='It is equal to 9/99 = 1/11.'),
      ],
      back=[
          B('Use long division to write a fraction as a repeating decimal', '7.NS.A.2.d', [
              sa('Write {7/9} as a decimal.', 'Decimal:', key='0.777... (the 7 repeats)'),
              sa('Write {5/12} as a decimal.', 'Decimal:', key='0.41666... (the 6 repeats)'),
              mc('Which decimal is equal to {3/11}?', ['0.2727... (the digits 27 repeat)', '0.311', '0.27 (the decimal ends)', '0.3']),
              tf('{1/9} = 0.111... (the 1 repeats)', key=True),
              tf('{5/6} = 0.56', key=False, note='5/6 = 0.8333...'),
          ]),
          B('Multiply decimals by powers of 10', '5.NBT.A.2', [
              sa('Multiply.\n0.454 × 100', 'Product:', key='45.4'),
              sa('Multiply.\n3.27 × 10', 'Product:', key='32.7'),
              mc('Multiply.\n0.0081 × 1,000', ['8.1', '0.81', '81', '0.081']),
              tf('2.5 × 100 = 250', key=True),
              tf('0.36 × 10 = 36', key=False),
          ]),
      ],
      f1=B('Solve linear equations whose solutions are fractions', 'HSA-REI.B.3', [
          sa('Solve for x. Write the answer as a fraction in simplest form.\n100x - x = 45', 'x =', key='5/11'),
          sa('Solve for x.\n10x = x + 6.3', 'x =', key='0.7', note='7/10 is also correct.'),
          mc('Solve for x.\n1,000x - 10x = 270', ['x = {3/11}', 'x = {27/100}', 'x = 27', 'x = {1/37}']),
          tf('x = {4/9} is the solution of 10x - x = 4.', key=True),
          tf('x = 0.12 is the solution of 100x - x = 12.', key=False, note='The solution is 12/99 = 4/33.'),
      ]),
      f2=B('Write a geometric sequence from a repeating decimal', 'HSF-BF.A.2', [
          sa('0.333... = 0.3 + 0.03 + 0.003 + ... The terms 0.3, 0.03, 0.003, ... form a geometric sequence.\nWhat is the common ratio?', 'Ratio:', key='0.1', note='1/10 is also correct.'),
          sa('Write an explicit formula for the nth term of the sequence 0.3, 0.03, 0.003, ...', 'a(n) =', key='0.3(0.1)^(n - 1)', note='Equivalent forms such as 3(0.1)^n are correct.'),
          mc('Which recursive formula gives the sequence 0.27, 0.0027, 0.000027, ...?',
             ['a(1) = 0.27; a(n) = 0.01 · a(n - 1)', 'a(1) = 0.27; a(n) = a(n - 1) - 0.01', 'a(1) = 0.27; a(n) = 100 · a(n - 1)', 'a(1) = 0.0027; a(n) = 0.01 · a(n - 1)']),
          tf('The sequence 0.5, 0.05, 0.005, ... is geometric with a common ratio of {1/10}.', key=True),
          tf('The sequence 0.4, 0.04, 0.004, ... is arithmetic.', key=False, note='The terms have a common ratio, not a common difference.'),
      ])),

    # ------------------------------------------------------------------ 8.NS.A.2 (estimate)
    S('8.NS.A.2', 'Estimate the value of an irrational number',
      main=[
          sa('Between which two whole numbers is √40?', 'Answer:', key='6 and 7'),
          sa('Estimate √20 to the nearest tenth. Explain how you know.', 'Answer:',
             key='4.5. 4.4² = 19.36 and 4.5² = 20.25, and 20 is closer to 20.25.', note='Grade both: 4.5, and a reason that compares squares of tenths.'),
          mc('Which is the best estimate of √75 to the nearest tenth?', ['8.7', '8.6', '9.1', '37.5']),
          tf('√2 is between 1.4 and 1.5.', key=True),
          tf('√90 is between 8 and 9.', key=False, note='9² = 81 and 10² = 100, so √90 is between 9 and 10.'),
      ],
      back=[
          B('Find squares of whole numbers and decimals', '6.EE.A.1', [
              sa('Find the value.\n7²', 'Value:', key='49'),
              sa('Find the value.\n1.5²', 'Value:', key='2.25'),
              mc('Find the value.\n12²', ['144', '24', '122', '121']),
              tf('8² = 64', key=True),
              tf('3² = 6', key=False),
          ]),
          B('Round decimals to the nearest tenth', '5.NBT.A.4', [
              sa('Round 4.472 to the nearest tenth.', 'Rounded:', key='4.5'),
              sa('Round 8.660 to the nearest tenth.', 'Rounded:', key='8.7'),
              mc('Round 3.162 to the nearest tenth.', ['3.2', '3.1', '3.0', '3.16']),
              tf('6.325 rounded to the nearest tenth is 6.3.', key=True),
              tf('2.449 rounded to the nearest tenth is 2.5.', key=False),
          ]),
      ],
      f1=B('Solve quadratic equations by taking square roots, exactly and approximately', 'HSA-REI.B.4.b', [
          sa('Solve x² = 30. Give the exact solutions, then round each to the nearest tenth.', 'Solutions:',
             key='x = √30 and x = -√30; about 5.5 and -5.5', note='Both solutions are required, exact and rounded.'),
          sa('Solve x² - 7 = 0. Give the exact solutions.', 'Solutions:', key='x = √7 and x = -√7', note='Both solutions are required; x = ±√7 is accepted.'),
          mc('Solve (x - 1)² = 5.', ['x = 1 + √5 or x = 1 - √5', 'x = 1 + √5 only', 'x = 6 or x = -4', 'x = √6 or x = -√6']),
          tf('The solutions of x² = 12 are x = 2√3 and x = -2√3.', key=True),
          tf('x² = -9 has the real solutions 3 and -3.', key=False, note='No real number squared is negative, so there is no real solution.'),
      ]),
      f2=B('Find arc lengths and sector areas exactly in terms of π and approximately', 'HSG-C.B.5', [
          sa('A circle has a radius of 6 cm.\nFind the length of a 90° arc exactly in terms of π, then to the nearest tenth.', 'Arc length:',
             key='3π cm, about 9.4 cm', note='Both the exact and the rounded value are required.'),
          sa('A circle has a radius of 4 inches.\nFind the area of a 45° sector exactly in terms of π, then to the nearest tenth.', 'Sector area:',
             key='2π square inches, about 6.3 square inches', note='Both the exact and the rounded value are required.'),
          mc('A circle has a radius of 3 m.\nTo the nearest tenth, how long is a 60° arc?', ['3.1 m', '6.3 m', '9.4 m', '18.8 m']),
          tf('The arc of a semicircle with a radius of 1 is π units long, about 3.14 units.', key=True),
          tf('A 180° sector of a circle with a radius of 2 has an area of 4π.', key=False, note='Its area is half of 4π, which is 2π.'),
      ])),

    # ------------------------------------------------------------------ 8.NS.A.2 (locate and compare)
    S('8.NS.A.2', 'Locate and compare irrational numbers on a number line',
      main=[
          plot('Plot √5 on the number line. Use an estimate to the nearest tenth.', line(0, 4, 0.5),
               key='A point at about 2.2: between 2 and 2.5, closer to 2'),
          mc('Which list is in order from least to greatest?', ['√3, 1.8, 2, √5', '1.8, √3, 2, √5', '√3, 2, 1.8, √5', '2, √5, √3, 1.8']),
          sa('Write <, >, or =.\nπ ___ √10', 'Symbol:', key='<', note='π is about 3.14 and √10 is about 3.16.'),
          sa('Which number is the best name for point P: √2, √3, or √6?', 'Answer:', fig=line(0, 3, 0.5, pts=[(1.73, 'P')]), key='√3'),
          tf('√30 is to the left of 5.5 on a number line.', key=True, note='√30 is about 5.48.'),
      ],
      back=[
          B('Read inequalities as positions on a number line', '6.NS.C.7.a', [
              sa('2.4 is to the right of 2.25 on a number line.\nWrite an inequality that shows this.', 'Inequality:', key='2.4 > 2.25', note='2.25 < 2.4 is also correct.'),
              mc('Which number is farthest to the left on a number line?', ['-2.5', '-2.05', '-1.9', '0.5']),
              sa('What does 1.7 < 1.75 tell you about the positions of the two numbers on a number line?', 'Answer:', key='1.7 is to the left of 1.75.'),
              tf('-1.4 > -1.41', key=True),
              tf('3.09 > 3.1', key=False),
          ]),
          B('Position decimals on a number line', '6.NS.C.6.c', [
              plot('Plot 1.4 and 2.75 on the number line.', line(0, 3, 0.25), key='Points at 1.4 (a little past the 1.25 mark) and 2.75'),
              sa('What decimal is at point A?', 'Decimal:', fig=line(0, 2, 0.25, pts=[(1.25, 'A')]), key='1.25'),
              mc('Which decimal is between 1.7 and 1.8?', ['1.73', '1.69', '1.81', '1.08']),
              tf('2.5 is halfway between 2 and 3.', key=True),
              tf('0.9 is to the right of 1.1 on a number line.', key=False),
          ]),
      ],
      f1=B('Report irrational values to a level of accuracy that fits the situation', 'HSN-Q.A.3', [
          sa('A square garden has an area of 50 square meters, so its side is √50 m. A tape measure reads to the nearest centimeter.\nReport the side length to that accuracy, in meters.', 'Side:', key='7.07 m'),
          sa('A coin has a diameter of 4 cm. Its circumference is 4π cm.\nReport the circumference to the nearest tenth of a centimeter.', 'Circumference:', key='12.6 cm'),
          mc('Which value of √2 is given to the nearest thousandth?', ['1.414', '1.41', '1.4142', '1.42']),
          tf('Reporting √3 as 1.7 is accurate to the nearest tenth.', key=True),
          tf('Writing more digits of √5 always makes a measured length more accurate.', key=False, note='A reported length cannot be more accurate than the measuring tool.'),
      ]),
      f2=B('Use coordinates to find exact lengths and perimeters with radicals', 'HSG-GPE.B.7', [
          sa('Find the exact perimeter of the triangle with vertices (0, 0), (2, 0), and (0, 2).', 'Perimeter:', key='4 + 2√2 units', note='About 6.8 units.'),
          sa('Find the exact length of the segment from (1, 1) to (4, 3).', 'Length:', key='√13 units'),
          mc('A square has vertices (0, 0), (1, 2), (-1, 3), and (-2, 1).\nWhat is its perimeter?', ['4√5 units', '20 units', '4√3 units', '2√5 units']),
          tf('The distance from (-1, -1) to (2, 3) is 5 units.', key=True),
          tf('A rectangle with vertices (0, 0), (3, 0), (3, 1), and (0, 1) has a diagonal 4 units long.', key=False, note='The diagonal is √10 units.'),
      ])),
]
