from qb import S, B, sa, mc, tf, plot, draw_write, nl, coord
from common import ints, grid


def ray(v, d, op):
    """Integer number line from -6 to 6 with a solution ray: d = 'right' or 'left'; op = open circle."""
    return ints(-6, 6, ray=(v, d, op))


SETS = [
    # ------------------------------------------------------------------ 7.EE.A.1 (add/subtract)
    S('7.EE.A.1', 'Add and subtract linear expressions with rational coefficients',
      main=[
          sa('Simplify.\n(3x + 5) + (2x - 8)', 'Expression:', key='5x - 3'),
          sa('Simplify.\n(4.5y - 2) - (1.5y + 6)', 'Expression:', key='3y - 8'),
          mc('Simplify.\n{1/2}a + 3 - {3/4}a + 1', ['-{1/4}a + 4', '{5/4}a + 4', '-{1/4}a + 2', '{1/4}a + 4']),
          tf('(6m - 1) - (2m - 4) = 4m + 3', key=True),
          tf('-3k + 7 + 5k - 2 = 8k + 5', key=False, note='The expression simplifies to 2k + 5.'),
      ],
      back=[
          B('Combine like terms', '6.EE.A.3', [
              sa('Combine like terms.\n5n + 3n + 4', 'Expression:', key='8n + 4'),
              sa('Combine like terms.\n2y + 7 + y', 'Expression:', key='3y + 7'),
              mc('Which expression is equivalent to x + x + x + 6?', ['3x + 6', 'x³ + 6', '9x', '3x + 2']),
              tf('4b + 2b = 6b', key=True),
              tf('3a + 2 = 5a', key=False),
          ]),
          B('Identify equivalent expressions', '6.EE.A.4', [
              sa('Are 2(x + 3) and 2x + 6 equivalent? Explain.', 'Answer:', key='Yes. Using the distributive property, 2(x + 3) = 2x + 6 for every value of x.'),
              mc('Which expression is equivalent to y + y + y?', ['3y', 'y³', '3 + y', 'y + 3']),
              sa('Write an expression with no parentheses that is equivalent to 4(n + 1).', 'Expression:', key='4n + 4'),
              tf('5m - 2m and 3m are equivalent.', key=True),
              tf('a + 4 and 4a are equivalent.', key=False),
          ]),
      ],
      f1=B('Solve equations by expanding and collecting like terms', '8.EE.C.7.b', [
          sa('Solve for x.\n2(3x - 1) - (x + 4) = 9', 'x =', key='3'),
          sa('Solve for x.\n{1/2}(4x + 6) = 3x - 5', 'x =', key='8'),
          mc('Solve for x.\n0.5(x + 8) - 2x = 1', ['x = 2', 'x = -2', 'x = 6', 'x = 3']),
          tf('x = 5 is the solution of 3(x - 2) = 2x - 1.', key=True),
          tf('x = 1 is the solution of 4x - (x + 2) = 4.', key=False, note='The solution is x = 2.'),
      ]),
      f2=B('Interpret the terms, factors, and coefficients of an expression', 'HSA-SSE.A.1.a', [
          sa('What is the coefficient of x in 5x² - 3x + 8?', 'Coefficient:', key='-3'),
          sa('How many terms are in 4a³ - 2a + 7?', 'Terms:', key='3'),
          mc('Which is a factor of 7(x + 2)²?', ['(x + 2)²', 'x²', '14', '7x']),
          tf('In -6y + 9, the constant term is 9.', key=True),
          tf('In 3x² + x, the coefficient of x is 0.', key=False, note='The coefficient of x is 1.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.A.1 (factor/expand)
    S('7.EE.A.1', 'Factor and expand linear expressions with rational coefficients',
      main=[
          sa('Expand.\n-4(2x - 3)', 'Expression:', key='-8x + 12'),
          sa('Factor out the greatest common factor.\n6y + 15', 'Expression:', key='3(2y + 5)'),
          mc('Which expression is equivalent to {1/2}(8a - 6)?', ['4a - 3', '4a - 6', '8a - 3', '16a - 12']),
          tf('12m - 18 = 6(2m - 3)', key=True),
          tf('-5(n + 2) = -5n + 10', key=False, note='-5(n + 2) = -5n - 10.'),
      ],
      back=[
          B('Use the greatest common factor and the distributive property', '6.NS.B.4', [
              sa('Find the greatest common factor of 24 and 36.', 'GCF:', key='12'),
              sa('Use the greatest common factor to write 30 + 42 as a product.', 'Product:', key='6(5 + 7)'),
              mc('Which expression is equal to 18 + 27?', ['9(2 + 3)', '9(2 + 27)', '3(6 + 27)', '9(18 + 3)']),
              tf('The greatest common factor of 16 and 40 is 8.', key=True),
              tf('20 + 35 = 5(4 + 6)', key=False, note='20 + 35 = 5(4 + 7).'),
          ]),
          B('Identify the parts of an expression', '6.EE.A.2.b', [
              sa('How many terms are in 3x + 7y - 2?', 'Terms:', key='3'),
              sa('What is the coefficient of w in 9 + 5w?', 'Coefficient:', key='5'),
              mc('Which part of 4(n + 6) is a sum?', ['n + 6', '4', '4n', '6']),
              tf('In 2(a + b), the factor 2 multiplies the sum a + b.', key=True),
              tf('In 8k - 3, the term 8k is a constant.', key=False),
          ]),
      ],
      f1=B('Expand to decide how many solutions an equation has', '8.EE.C.7.a', [
          sa('How many solutions does this equation have?\n4(x - 2) = 4x - 8', 'Answer:', key='Infinitely many solutions'),
          sa('How many solutions does this equation have?\n-3(x + 1) = -3x + 3', 'Answer:', key='No solution'),
          mc('Which equation has no solution?', ['2(x + 5) = 2x + 7', '2(x + 5) = 2x + 10', '2(x + 5) = x + 10', '2(x + 5) = 3x']),
          tf('6(x - 1) = 2(3x - 3) has infinitely many solutions.', key=True),
          tf('5(x + 1) = 5x + 1 has exactly one solution.', key=False, note='It has no solution.'),
      ]),
      f2=B('Factor quadratic expressions', 'HSA-SSE.A.2', [
          sa('Factor.\nx² + 7x + 12', 'Factored form:', key='(x + 3)(x + 4)'),
          sa('Factor completely.\n3x² - 12', 'Factored form:', key='3(x + 2)(x - 2)'),
          mc('Factor.\nx² - 2x - 15', ['(x - 5)(x + 3)', '(x + 5)(x - 3)', '(x - 5)(x - 3)', '(x - 15)(x + 1)']),
          tf('2x² + 10x = 2x(x + 5)', key=True),
          tf('x² + 5x + 6 = (x + 1)(x + 6)', key=False, note='x² + 5x + 6 = (x + 2)(x + 3).'),
      ])),

    # ------------------------------------------------------------------ 7.EE.A.2
    S('7.EE.A.2', 'Rewrite an expression to show how the quantities in a problem are related',
      main=[
          sa('A shirt costs p dollars. The price is raised by 30%.\nWrite the new price as a single term.', 'New price:', key='1.3p'),
          sa('A rectangle\'s length is 4 cm more than its width w.\nWrite its perimeter in two equivalent ways.', 'Perimeter:',
             key='2w + 2(w + 4) and 4w + 8', note='Any two correct equivalent expressions earn credit.'),
          mc('A price p is lowered by 15%.\nWhich expression shows the new price?', ['0.85p', '0.15p', 'p - 15', '1.15p']),
          tf('n + 0.08n = 1.08n shows that increasing n by 8% is the same as multiplying n by 1.08.', key=True),
          tf('The price after a 20% discount on a price of d dollars is d - 20.', key=False, note='The price is 0.8d.'),
      ],
      back=[
          B('Write expressions from words', '6.EE.A.2.a', [
              sa('Write an expression for "5 less than y."', 'Expression:', key='y - 5'),
              sa('Write an expression for "the product of 8 and n."', 'Expression:', key='8n'),
              mc('Which expression means "the sum of x and 3, times 4"?', ['4(x + 3)', '4x + 3', 'x + 3 × 4', '4 + x + 3']),
              tf('"Twice a number m" can be written as 2m.', key=True),
              tf('"7 fewer than k" can be written as 7 - k.', key=False, note='It is k - 7.'),
          ]),
          B('Write and interpret numerical expressions', '5.OA.A.2', [
              sa('Write an expression for "add 6 and 9, then multiply by 2."', 'Expression:', key='2 × (6 + 9)', note='(6 + 9) × 2 is also correct.'),
              mc('How does 5 × (24 + 13) compare with 24 + 13?', ['It is 5 times as large.', 'It is 5 more.', 'It is 5 less.', 'They are equal.']),
              sa('Write an expression for "subtract 4 from 20, then divide by 2."', 'Expression:', key='(20 - 4) ÷ 2'),
              tf('(7 + 8) × 3 is three times as large as 7 + 8.', key=True),
              tf('10 × (5 - 2) is 10 more than 5 - 2.', key=False),
          ]),
      ],
      f1=B('Write equivalent expressions with the properties of integer exponents', '8.EE.A.1', [
          sa('Write as a single power.\n4⁵ × 4⁻²', 'Power:', key='4³'),
          sa('Write as a single power.\n(2³)⁴', 'Power:', key='2¹²'),
          mc('Which number is equal to 5⁶ ÷ 5⁸?', ['{1/25}', '25', '5¹⁴', '-25']),
          tf('7⁰ = 1', key=True),
          tf('3² × 3³ = 9⁵', key=False, note='3² × 3³ = 3⁵.'),
      ]),
      f2=B('Choose an equivalent form of an expression to reveal a property', 'HSA-SSE.B.3', [
          sa('Factor f(x) = x² - 6x + 8 to find the values of x where f(x) = 0.', 'x =', key='2 and 4'),
          sa('A price p is raised 10%, and then the new price is raised 10% again: p(1.1)(1.1).\nWrite this as a single factor times p, and give the total percent increase.', 'Answer:',
             key='1.21p; a 21% increase'),
          mc('A value after t years is 50(1.03)^t.\nWhat is the yearly percent increase?', ['3%', '103%', '50%', '0.3%']),
          tf('Writing x² - 9 as (x - 3)(x + 3) shows that the expression equals 0 when x = 3 or x = -3.', key=True),
          tf('A 10% increase followed by a 10% decrease leaves a price unchanged.', key=False, note='The final price is 0.99 times the original price.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.3 (multistep)
    S('7.EE.B.3', 'Solve multistep problems with positive and negative rational numbers in any form',
      main=[
          sa('Jon earns $16.50 per hour. He gets a raise of {1/5} of his wage. Then he works 30 hours.\nHow much does he earn for the 30 hours?', 'Earnings:', key='$594'),
          sa('A board is 8{1/4} feet long. Ana cuts off 2.5 feet. She cuts the rest into 3 equal pieces.\nHow long is each piece?', 'Length:',
             key='1 11/12 feet', note='23/12 feet, or about 1.92 feet, is also correct.'),
          mc('A 60-gallon tank is {3/4} full. Then 12.5 gallons are used.\nHow many gallons are left?', ['32.5', '47.5', '45', '57.5']),
          tf('A $40 sweater is 25% off. Mia pays with a $50 bill. Her change is $20.', key=True),
          tf('Leo runs 2{1/2} miles on Monday and 3.4 miles on Tuesday. He runs 6.4 miles in all.', key=False, note='He runs 5.9 miles.'),
      ],
      back=[
          B('Interpret a fraction as division', '5.NF.B.3', [
              sa('Write {3/4} as a division expression. Then find its decimal value.', 'Answer:', key='3 ÷ 4 = 0.75'),
              sa('5 friends share 2 pizzas equally.\nHow much pizza does each friend get?', 'Amount:', key='2/5 of a pizza'),
              mc('Which number is equal to 7 ÷ 8?', ['{7/8}', '{8/7}', '7.8', '0.78']),
              tf('{9/2} = 9 ÷ 2', key=True),
              tf('3 ÷ 5 = {5/3}', key=False),
          ]),
          B('Find a percent of a quantity', '6.RP.A.3.c', [
              sa('What is 35% of 60?', 'Answer:', key='21'),
              sa('What is 12.5% of 64?', 'Answer:', key='8'),
              mc('What is 150% of 20?', ['30', '3', '15', '130']),
              tf('60% of 25 is 15.', key=True),
              tf('5% of 300 is 1.5.', key=False, note='5% of 300 is 15.'),
          ]),
      ],
      f1=B('Solve real-world problems with two linear equations', '8.EE.C.8.c', [
          sa('Adult tickets cost $9 and child tickets cost $5. Someone buys 20 tickets for $140.\nHow many adult tickets were bought?', 'Adult tickets:', key='10'),
          sa('Plan A costs $20 plus $0.10 per minute. Plan B costs $0.35 per minute.\nFor how many minutes do the plans cost the same?', 'Minutes:', key='80'),
          mc('Two numbers have a sum of 30 and a difference of 8.\nWhat is the larger number?', ['19', '11', '22', '15']),
          tf('x = 3 and y = 5 is a solution of both x + y = 8 and 2x - y = 1.', key=True),
          tf('x = 4 and y = 2 is a solution of both x + y = 6 and x - y = 1.', key=False),
      ]),
      f2=B('Represent constraints with equations or inequalities', 'HSA-CED.A.3', [
          sa('A baker has 24 cups of flour. Each muffin uses {3/4} cup and each loaf uses 2.5 cups.\nWrite an inequality for m muffins and l loaves.', 'Inequality:', key='0.75m + 2.5l ≤ 24'),
          sa('A baker has 24 cups of flour. Each muffin uses {3/4} cup and each loaf uses 2.5 cups.\nCan she make 12 muffins and 7 loaves? Explain.', 'Answer:',
             key='No. 12 muffins and 7 loaves need 9 + 17.5 = 26.5 cups, which is more than 24 cups.'),
          mc('A trip budget is at most $150. Gas costs $3.50 per gallon (g) and meals cost $12 each (f).\nWhich inequality shows the budget?', ['3.5g + 12f ≤ 150', '3.5g + 12f ≥ 150', '3.5 + 12 ≤ 150gf', '12g + 3.5f ≤ 150']),
          tf('m = 8 and l = 4 makes 0.75m + 2.5l ≤ 24 true.', key=True),
          tf('m = 10 and l = 9 makes 0.75m + 2.5l ≤ 24 true.', key=False, note='0.75(10) + 2.5(9) = 30, which is more than 24.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.3 (estimation)
    S('7.EE.B.3', 'Use estimation to judge whether an answer is reasonable',
      main=[
          sa('Estimate 19.8 × 4.1 by rounding each number to the nearest whole number.', 'Estimate:', key='80', note='20 × 4 = 80.'),
          sa('Kim says 48.7 + 31.2 = 799.\nUse estimation to explain whether her answer is reasonable.', 'Answer:',
             key='Not reasonable. 49 + 31 is about 80, so the sum should be about 80.'),
          mc('A meal costs $38.75. Ana adds a 20% tip.\nWhich is the best estimate of the total?', ['About $47', 'About $40', 'About $58', 'About $78']),
          tf('6{7/8} × 3{1/10} is about 7 × 3, so a product of about 21 is reasonable.', key=True),
          tf('A $59.99 jacket is 30% off. A sale price of about $18 is reasonable.', key=False, note='The sale price should be about $42.'),
      ],
      back=[
          B('Round decimals', '5.NBT.A.4', [
              sa('Round 7.86 to the nearest whole number.', 'Rounded:', key='8'),
              sa('Round 12.348 to the nearest tenth.', 'Rounded:', key='12.3'),
              mc('Round 4.165 to the nearest hundredth.', ['4.17', '4.16', '4.2', '4.1']),
              tf('3.97 rounded to the nearest tenth is 4.0.', key=True),
              tf('15.52 rounded to the nearest whole number is 15.', key=False),
          ]),
          B('Use rounding to check whether an answer is reasonable', '4.OA.A.3', [
              sa('Estimate 398 + 211 by rounding each number to the nearest hundred.', 'Estimate:', key='600'),
              sa('Lia says 52 × 4 = 2,008.\nRound 52 to the nearest ten to decide whether her answer is reasonable.', 'Answer:',
                 key='Not reasonable. 50 × 4 = 200, so the answer should be about 200.'),
              mc('Round each number to the nearest hundred.\nWhat is the best estimate of 689 - 312?', ['400', '300', '1,000', '500']),
              tf('Rounding 49 to the nearest ten gives an estimate of 300 for 49 × 6.', key=True),
              tf('Rounding each number to the nearest hundred gives an estimate of 1,200 for 812 - 397.', key=False, note='The estimate is 800 - 400 = 400.'),
          ]),
      ],
      f1=B('Estimate very large or very small quantities with powers of 10', '8.EE.A.3', [
          sa('Estimate 38,900,000 as a single digit times a power of 10.', 'Estimate:', key='4 × 10⁷'),
          sa('Estimate 0.00062 as a single digit times a power of 10.', 'Estimate:', key='6 × 10⁻⁴'),
          mc('About how many times as large as 3 × 10⁵ is 9 × 10⁸?', ['3,000', '300', '30', '3']),
          tf('3 × 10⁸ is a reasonable estimate for 296,000,000.', key=True),
          tf('6 × 10⁻³ is about 6,000.', key=False, note='6 × 10⁻³ = 0.006.'),
      ]),
      f2=B('Define appropriate quantities and units for a model', 'HSN-Q.A.2', [
          sa('A heart beats about 70 times per minute.\nAbout how many times does it beat in 1 day? Round to the nearest ten thousand.', 'Estimate:', key='100,000', note='70 × 1,440 = 100,800.'),
          sa('Which unit best describes the distance between two cities: millimeters, meters, or kilometers?', 'Unit:', key='Kilometers'),
          mc('Which quantity is most useful for estimating the cost to paint the walls of a room?',
             ['The area of the walls', 'The volume of the room', 'The height of the door', 'The number of windows']),
          tf('Gallons of water used per day is a reasonable quantity for modeling a family\'s water use.', key=True),
          tf('The color of a car is a useful quantity for modeling how much fuel it uses on a trip.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (px + q = r)
    S('7.EE.B.4.a', 'Solve word problems that lead to equations of the form px + q = r',
      main=[
          sa('A gym charges a $25 sign-up fee plus $18 per month. Ty has paid $151 in all.\nWrite and solve an equation to find the number of months m.', 'Answer:',
             key='18m + 25 = 151; m = 7', note='Any correct equation earns credit.'),
          sa('Solve for x.\n4x + 9 = -11', 'x =', key='-5'),
          mc('Ava has $60. She buys movie tickets for $7.50 each and has $15 left.\nWhich equation finds the number of tickets t?', ['60 - 7.5t = 15', '7.5t + 60 = 15', '60t - 7.5 = 15', '7.5 - 60t = 15']),
          tf('x = 6 is the solution of {1/2}x + 3 = 6.', key=True),
          tf('A plumber charges $45 plus $30 per hour. A bill of $165 means the plumber worked 5 hours.', key=False, note='The plumber worked 4 hours.'),
      ],
      back=[
          B('Solve one-step equations', '6.EE.B.7', [
              sa('Solve for x.\nx + 13 = 41', 'x =', key='28'),
              sa('Solve for y.\n9y = 72', 'y =', key='8'),
              mc('Solve for n.\nn - 6.4 = 3.6', ['n = 10', 'n = 2.8', 'n = -2.8', 'n = 23.04']),
              tf('k = 7 is the solution of 5k = 35.', key=True),
              tf('p = 9 is the solution of p + 4 = 15.', key=False),
          ]),
          B('Write an expression with a variable for a situation', '6.EE.B.6', [
              sa('A ticket costs $12.\nWrite an expression for the cost of t tickets.', 'Expression:', key='12t'),
              sa('Ana has 5 more stickers than Ben. Ben has b stickers.\nWrite an expression for the number of stickers Ana has.', 'Expression:', key='b + 5'),
              mc('A pizza has s slices. 4 friends share it equally.\nWhich expression gives the number of slices each friend gets?', ['{s/4}', '4s', 's - 4', 's + 4']),
              tf('A pen costs p dollars. 3 pens cost 3p dollars.', key=True),
              tf('Mo is m years old. His age in 6 years is 6m.', key=False, note='His age in 6 years is m + 6.'),
          ]),
      ],
      f1=B('Solve equations with the variable on both sides', '8.EE.C.7.b', [
          sa('Store A charges $40 plus $5 per day. Store B charges $25 plus $8 per day.\nAfter how many days do the stores charge the same amount?', 'Days:', key='5'),
          sa('Solve for x.\n7x - 4 = 3x + 20', 'x =', key='6'),
          mc('Solve for x.\n-2x + 9 = 4x - 15', ['x = 4', 'x = -4', 'x = 1', 'x = 12']),
          tf('x = -1 is the solution of 5x + 3 = 2x.', key=True),
          tf('x = 2 is the solution of 6x - 1 = 4x + 5.', key=False, note='The solution is x = 3.'),
      ]),
      f2=B('Rearrange a formula to solve for a chosen quantity', 'HSA-CED.A.4', [
          sa('Solve P = 2l + 2w for l.', 'l =', key='(P - 2w)/2', note='l = P/2 - w is also correct.'),
          sa('Solve y = mx + b for x.', 'x =', key='(y - b)/m'),
          mc('Solve A = {1/2}bh for h.', ['h = {2A/b}', 'h = {A/2b}', 'h = 2Ab', 'h = {b/2A}']),
          tf('Solving d = rt for t gives t = {d/r}.', key=True),
          tf('Solving C = 5n + 20 for n gives n = 5C - 20.', key=False, note='n = (C - 20)/5.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (p(x + q) = r)
    S('7.EE.B.4.a', 'Solve word problems that lead to equations of the form p(x + q) = r',
      main=[
          sa('A rectangle is 7 cm wide and (x + 3) cm long. Its area is 63 cm².\nWrite and solve an equation to find x.', 'Answer:',
             key='7(x + 3) = 63; x = 6', note='Any correct equation earns credit.'),
          sa('Solve for x.\n-3(x - 4) = 27', 'x =', key='-5'),
          mc('5 friends each buy a $4 snack and a drink that costs d dollars. They spend $32.50 in all.\nWhich equation finds d?', ['5(d + 4) = 32.5', '5d + 4 = 32.5', 'd + 5(4) = 32.5', '4(d + 5) = 32.5']),
          tf('x = 2.5 is the solution of 2(x + 1.5) = 8.', key=True),
          tf('The solution of {1/3}(x - 6) = 4 is x = 6.', key=False, note='The solution is x = 18.'),
      ],
      back=[
          B('Evaluate expressions with parentheses', '5.OA.A.1', [
              sa('Evaluate.\n3 × (8 + 4)', 'Value:', key='36'),
              sa('Evaluate.\n(15 - 6) × 2', 'Value:', key='18'),
              mc('Evaluate.\n4 × (9 - 2) + 1', ['29', '36', '33', '25']),
              tf('2 × (5 + 5) = 20', key=True),
              tf('(12 + 3) × 2 = 18', key=False),
          ]),
          B('Use the distributive property to expand an expression', '6.EE.A.3', [
              sa('Rewrite using the distributive property.\n9(m + 2)', 'Expression:', key='9m + 18'),
              sa('Rewrite using the distributive property.\n4(3k + 5)', 'Expression:', key='12k + 20'),
              mc('Which expression is equivalent to 6(x + 1.5)?', ['6x + 9', '6x + 1.5', '7x + 1.5', '6x + 7.5']),
              tf('5(2 + y) = 10 + 5y', key=True),
              tf('8(p + 3) = 8p + 3', key=False),
          ]),
      ],
      f1=B('Solve equations with the distributive property on both sides', '8.EE.C.7.b', [
          sa('Solve for x.\n3(x + 2) = 2(x + 7)', 'x =', key='8'),
          sa('Solve for x.\n-2(x - 5) = 4(x + 1)', 'x =', key='1'),
          mc('Solve for x.\n{1/2}(6x - 4) = 2(x + 3)', ['x = 8', 'x = 2', 'x = -8', 'x = 10']),
          tf('x = 4 is the solution of 5(x - 1) = 3(x + 1).', key=True),
          tf('x = 3 is the solution of 2(x + 6) = 4(x - 1).', key=False, note='The solution is x = 8.'),
      ]),
      f2=B('Solve quadratic equations by square roots or factoring', 'HSA-REI.B.4.b', [
          sa('Solve for x.\n(x + 3)² = 49', 'x =', key='4 or -10'),
          sa('Solve for x.\nx² = 81', 'x =', key='9 or -9'),
          mc('Solve for x.\n(x - 2)(x + 5) = 0', ['x = 2 or x = -5', 'x = -2 or x = 5', 'x = 2 only', 'x = -5 only']),
          tf('The solutions of 2(x - 1)² = 18 are x = 4 and x = -2.', key=True),
          tf('x² = 16 has only one solution, x = 4.', key=False, note='x = 4 or x = -4.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (compare solutions)
    S('7.EE.B.4.a', 'Compare an algebraic solution with an arithmetic solution',
      main=[
          sa('Ron has $50. He buys 3 books that cost the same amount and has $14 left.\nArithmetic: (50 - 14) ÷ 3. Algebra: 3b + 14 = 50.\nWhat is the price of one book?', 'Price:', key='$12'),
          sa('An arithmetic solution to 4(x + 2) = 36 is 36 ÷ 4 - 2.\nDescribe the operations in order, and give x.', 'Answer:', key='Divide 36 by 4, then subtract 2; x = 7.'),
          mc('Which arithmetic steps solve 5x - 8 = 27?',
             ['Add 8 to 27, then divide by 5.', 'Subtract 8 from 27, then divide by 5.', 'Divide 27 by 5, then add 8.', 'Multiply 27 by 5, then add 8.']),
          tf('Solving 2x + 6 = 20 with algebra and computing (20 - 6) ÷ 2 both give 7.', key=True),
          tf('The arithmetic steps "subtract 4 from 15, then divide by 3" solve 3(x - 4) = 15.', key=False,
             note='The correct steps are to divide 15 by 3, then add 4, so x = 9.'),
      ],
      back=[
          B('Solve two-step word problems', '3.OA.D.8', [
              sa('Jo has 45 stickers. She gives away 9. Then she shares the rest equally among 4 friends.\nHow many stickers does each friend get?', 'Stickers:', key='9'),
              sa('There are 6 boxes with 8 pens in each box. 5 pens are lost.\nHow many pens are left?', 'Pens:', key='43'),
              mc('A book has 90 pages. Kim reads 20 pages on Monday and 35 pages on Tuesday.\nHow many pages are left?', ['35', '55', '145', '15']),
              tf('3 packs of 7 cards and 4 more cards make 25 cards.', key=True),
              tf('40 apples are shared equally in 5 bags. Then 2 apples are taken out of each bag. Each bag now has 8 apples.', key=False, note='Each bag has 6 apples.'),
          ]),
          B('Decide whether a value makes an equation true', '6.EE.B.5', [
              sa('Is x = 4 a solution of 3x + 2 = 14? Explain.', 'Answer:', key='Yes. 3(4) + 2 = 14.'),
              mc('Which value of n makes n + 9 = 15 true?', ['6', '24', '9', '5']),
              sa('Which of the values 2, 5, and 8 makes 7y = 35 true?', 'Value:', key='5'),
              tf('m = 3 makes 12 ÷ m = 4 true.', key=True),
              tf('a = 5 makes 2a - 1 = 11 true.', key=False),
          ]),
      ],
      f1=B('Solve systems of two linear equations algebraically and by inspection', '8.EE.C.8.b', [
          sa('Solve the system.\ny = 2x\nx + y = 18', 'Solution:', key='x = 6, y = 12'),
          sa('Solve the system.\ny = x + 3\ny = -2x + 9', 'Solution:', key='x = 2, y = 5'),
          mc('Look at the system. How many solutions does it have?\n3x + 2y = 5\n3x + 2y = 6', ['No solution', 'One solution', 'Two solutions', 'Infinitely many solutions']),
          tf('The system y = 4x and y = 4x + 1 has no solution.', key=True),
          tf('x = 4 and y = 6 is the solution of the system x + y = 10 and x - y = 2.', key=False, note='The solution is x = 6, y = 4.'),
      ]),
      f2=B('Explain each step in solving an equation', 'HSA-REI.A.1', [
          sa('In solving an equation, 5(x - 2) = 30 is rewritten as 5x - 10 = 30.\nWhich property is used?', 'Property:', key='The distributive property'),
          sa('In solving an equation, 5x - 10 = 30 is rewritten as 5x = 40.\nExplain this step.', 'Explanation:', key='10 is added to both sides (addition property of equality).'),
          mc('Which step changes 5x = 40 into x = 8?', ['Divide both sides by 5.', 'Subtract 5 from both sides.', 'Multiply both sides by 5.', 'Add 5 to both sides.']),
          tf('Each step in solving a linear equation should give an equation with the same solution.', key=True),
          tf('Subtracting 3 from only one side of an equation keeps the equation true.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.b (solve)
    S('7.EE.B.4.b', 'Solve word problems that lead to inequalities of the form px + q > r or px + q < r',
      main=[
          sa('Sam has $40. He buys a $12 shirt and some pairs of socks that cost $3.50 each.\nWrite and solve an inequality for the number of pairs of socks p he can buy.', 'Answer:',
             key='3.5p + 12 ≤ 40; p ≤ 8', note='He can buy at most 8 pairs. Any correct inequality earns credit.'),
          sa('Solve.\n-2x + 5 > 13', 'Solution:', key='x < -4'),
          mc('Solve.\n3x - 7 ≥ 11', ['x ≥ 6', 'x ≤ 6', 'x ≥ {4/3}', 'x ≤ {4/3}']),
          tf('Dividing both sides of -4x < 20 by -4 gives x > -5.', key=True),
          tf('The solution of 5x + 2 < 17 is x > 3.', key=False, note='The solution is x < 3.'),
      ],
      back=[
          B('Write an inequality for a situation', '6.EE.B.8', [
              sa('Riders must be at least 48 inches tall.\nWrite an inequality for a rider\'s height h.', 'Inequality:', key='h ≥ 48'),
              sa('Write an inequality for "a temperature t below -2°F."', 'Inequality:', key='t < -2'),
              mc('Which inequality means "x is more than 7"?', ['x > 7', 'x < 7', 'x ≤ 7', 'x = 7']),
              tf('x < 3 has infinitely many solutions.', key=True),
              tf('5 is a solution of x < 5.', key=False),
          ]),
          B('Decide whether a value makes an inequality true', '6.EE.B.5', [
              sa('Is 9 a solution of 2x > 16? Explain.', 'Answer:', key='Yes. 2(9) = 18, and 18 > 16.'),
              mc('Which value makes y + 4 < 10 true?', ['5', '6', '8', '10']),
              sa('Which of the values 3, 6, and 9 make n - 2 ≥ 4 true?', 'Values:', key='6 and 9'),
              tf('x = 0 makes 3x < 1 true.', key=True),
              tf('k = 2 makes 5k > 10 true.', key=False),
          ]),
      ],
      f1=B('Solve multistep equations with the variable on both sides', '8.EE.C.7.b', nearest=True, qs=[
          sa('Solve for x.\n0.5x + 7 = 2x - 2', 'x =', key='6'),
          sa('Solve for x.\n{2/3}(x + 3) = x - 1', 'x =', key='9'),
          mc('Solve for x.\n6 - 3x = x + 22', ['x = -4', 'x = 4', 'x = -7', 'x = 7']),
          tf('x = -2 is the solution of 4(x + 5) = x + 14.', key=True),
          tf('x = 1 is the solution of 9x - 3 = 2x + 2.', key=False, note='The solution is x = 5/7.'),
      ]),
      f2=B('Solve linear inequalities with the variable on both sides', 'HSA-REI.B.3', [
          sa('Solve.\n5x - 3 > 2x + 9', 'Solution:', key='x > 4'),
          sa('Solve.\n-4(x + 1) ≤ 2x + 8', 'Solution:', key='x ≥ -2'),
          mc('Solve.\n7 - 2x < x - 8', ['x > 5', 'x < 5', 'x > -5', 'x < -5']),
          tf('x = 0 is a solution of 3(x - 2) < x + 1.', key=True),
          tf('The solution of 6x + 1 ≥ 4x + 11 is x ≤ 5.', key=False, note='The solution is x ≥ 5.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.b (graph)
    S('7.EE.B.4.b', 'Graph the solution set of an inequality and interpret it in context',
      main=[
          plot('Graph the solution set of x > -3 on the number line.', ints(-6, 6), key='An open circle at -3 with an arrow or shading to the right'),
          draw_write('Solve 2x + 1 ≤ 9. Then graph the solution set on the number line.', ints(-6, 6), 'Solution:',
                     draw='A closed circle at 4 with an arrow or shading to the left', key='x ≤ 4',
                     note='Grade both: the solution x ≤ 4, and the graph with a closed circle at 4 shaded to the left.'),
          mc('Which inequality does the graph show?', ['x ≥ 2', 'x > 2', 'x ≤ 2', 'x < 2'], fig=ray(2, 'right', False)),
          sa('A club has $30. It earns $5 for each ticket it sells. It needs more than $230.\nSolve 5t + 30 > 230 and describe the solution in context.', 'Answer:',
             key='t > 40. The club must sell more than 40 tickets (at least 41).'),
          tf('The graph shows the solution set of -x < 2.', fig=ray(-2, 'right', True), key=True),
      ],
      back=[
          B('Graph an inequality on a number line', '6.EE.B.8', [
              plot('Graph x < 4 on the number line.', ints(-6, 6), key='An open circle at 4 with an arrow or shading to the left'),
              plot('Graph x ≥ -1 on the number line.', ints(-6, 6), key='A closed circle at -1 with an arrow or shading to the right'),
              mc('Which inequality does the graph show?', ['x < 0', 'x > 0', 'x ≤ 0', 'x ≥ 0'], fig=ray(0, 'left', True)),
              tf('A closed circle on the graph of an inequality shows that the endpoint is a solution.', key=True),
              tf('The graph of x > 5 has a closed circle at 5.', key=False),
          ]),
          B('Read an inequality as positions on a number line', '6.NS.C.7.a', [
              sa('-4 is to the left of 1 on a number line.\nWrite an inequality that shows this.', 'Inequality:', key='-4 < 1'),
              mc('Which statement says that -2 is to the right of -6 on a number line?', ['-2 > -6', '-2 < -6', '-6 > -2', '-2 = -6']),
              sa('What does -8 < -3 tell you about the positions of -8 and -3 on a number line?', 'Answer:', key='-8 is to the left of -3.'),
              tf('-1 > -9 because -1 is to the right of -9 on a number line.', key=True),
              tf('-5 > 0', key=False),
          ]),
      ],
      f1=B('Find the solution of a system of equations from its graph', '8.EE.C.8.a', [
          sa('The graph shows y = x + 1 and y = -x + 5.\nAt what point do the lines intersect?', 'Point:',
             fig=grid(6, 6, lines=[((0, 1), (5, 6)), ((0, 5), (5, 0))]), key='(2, 3)'),
          sa('Two lines are graphed on the same grid.\nWhat does their point of intersection represent?', 'Answer:', key='The pair (x, y) that makes both equations true; the solution of the system.'),
          mc('The graphs of two linear equations are parallel lines.\nHow many solutions does the system have?', ['No solution', 'One solution', 'Two solutions', 'Infinitely many solutions']),
          tf('(1, 4) is the solution of the system y = 2x + 2 and y = 3x + 1.', key=True),
          tf('If two equations have the same graph, the system has no solution.', key=False, note='It has infinitely many solutions.'),
      ]),
      f2=B('Graph the solutions of a linear inequality in two variables', 'HSA-REI.D.12', [
          plot('Graph y > x + 1 on the coordinate plane.', coord(), key='A dashed line through (0, 1) with slope 1, with the region above the line shaded'),
          sa('Is (2, 5) a solution of y ≥ 2x? Explain.', 'Answer:', key='Yes. 5 ≥ 2(2), because 5 ≥ 4.'),
          mc('Which point is in the solution set of y < -x + 3?', ['(0, 0)', '(2, 4)', '(3, 1)', '(0, 5)']),
          tf('The boundary line of the graph of y ≤ 3x - 2 is drawn solid.', key=True),
          tf('The solution set of y > 2 is the region below the line y = 2.', key=False),
      ])),
]
