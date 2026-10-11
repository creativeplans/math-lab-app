from qb import S, B, sa, mc, tf, plot, draw_write, work, nl, coord
from common import ints, grid


def ray(v, d, op):
    """Integer number line from -6 to 6 with a solution ray: d = 'right' or 'left'; op = open circle."""
    return ints(-6, 6, ray=(v, d, op))


COMPARE = ('Grade all three parts: (a) a correct arithmetic solution, (b) a correct equation with an algebraic solution, and (c) a comparison '
           'that matches each arithmetic operation to the algebra step that does the same thing in the same order. ')


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
      f2=B('Interpret the terms, factors, and coefficients of an expression in context', 'HSA-SSE.A.1.a', [
          sa('A phone plan costs 0.1m + 25 dollars for m minutes in a month.\nWhat do the terms 0.1m and 25 represent?', 'Meaning:',
             key='0.1m is the cost of the minutes at $0.10 per minute; 25 is a fixed monthly charge of $25.', note='Grade both terms.'),
          sa('The perimeter of a rectangle is 2(l + 4) centimeters, where l is its length.\nWhat does the factor (l + 4) represent?', 'Meaning:',
             key='The length plus the width (the width is 4 cm), which is half of the perimeter.'),
          mc('A ride costs 2.5 + 1.75d dollars for d miles.\nWhat does 1.75 represent?', ['The cost per mile', 'The starting fee', 'The total cost of a 1-mile ride', 'The number of miles']),
          tf('A repair costs 40 + 15h dollars for h hours of work. The term 15h is the labor cost for h hours.', key=True),
          tf('A savings account holds 500 - 20w dollars after w weeks. The coefficient -20 means $20 is added each week.', key=False, note='-20 means $20 is taken out each week.'),
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
      f2=B('Rewrite percent-growth expressions to reveal the growth factor', 'HSA-SSE.B.3', [
          sa('A town\'s population after t years is P(1.02)^t.\nRewrite the expression to show the growth factor for each 10 years, rounded to the nearest hundredth.', 'Expression:',
             key='P(1.22)^(t/10); about 22% growth every 10 years', note='P((1.02)^10)^(t/10) with (1.02)^10 ≈ 1.22 is also correct.'),
          sa('A price p is raised 10%, and then the new price is raised 10% again: p(1.1)(1.1).\nWrite this as a single factor times p, and give the total percent increase.', 'Answer:',
             key='1.21p; a 21% increase'),
          mc('A value after t years is 50(1.03)^t.\nWhat is the yearly percent increase?', ['3%', '103%', '50%', '0.3%']),
          tf('The expression 1,000(0.97)^t shows a value that decreases by 3% each year.', key=True),
          tf('A 10% increase followed by a 10% decrease leaves a price unchanged.', key=False, note='The final price is 0.99 times the original price.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.3 (multistep)
    S('7.EE.B.3', 'Solve multistep problems with positive and negative rational numbers in any form',
      main=[
          sa('Jon earns $16.50 per hour. He gets a raise of {1/5} of his wage. Then he works 30 hours.\nHow much does he earn for the 30 hours?', 'Earnings:', key='$594'),
          sa('A board is 8{1/4} feet long. Ana cuts off 2.5 feet. She cuts the rest into 3 equal pieces.\nHow long is each piece?', 'Length:',
             key='1 11/12 feet', note='23/12 feet is also correct. The question asks for an exact length, so a rounded decimal is not full credit.'),
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
          B('Use rounding to check the answer to a two-step word problem', '4.OA.A.3', [
              sa('A store sells 4 packs of cards for $52 each and charges $11 for shipping.\nRound 52 to the nearest ten, and keep 4 and 11 unchanged, to estimate the total cost.', 'Estimate:',
                 key='$211', note='4 × 50 + 11 = 211.'),
              sa('A store sells 4 packs of cards for $52 each and charges $11 for shipping. Ty says the total is $2,019.\nRound 52 to the nearest ten to decide whether his answer is reasonable.', 'Answer:',
                 key='Not reasonable. 4 × 50 + 11 = 211, so the total should be about $211.'),
              mc('A school buys 6 boxes of 48 pencils and gives away 95 pencils.\nRound 48 and 95 to the nearest ten, and keep 6 unchanged. What is the best estimate of the pencils left?', ['200', '300', '100', '400']),
              tf('A farm picks 312 apples on Monday and 289 apples on Tuesday, then sells 198 apples. Rounding each number to the nearest hundred gives an estimate of 400 apples left.', key=True),
              tf('A bus carries 38 riders on each of 7 trips and 21 riders on one more trip. Rounding 38 and 21 to the nearest ten, and keeping 7 unchanged, gives an estimate of 220 riders.', key=False,
                 note='The estimate is 7 × 40 + 20 = 300 riders.'),
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
          sa('You want to estimate how many times a heart beats in one day.\nWhich two quantities do you need, and what are their units?', 'Quantities:',
             key='The heart rate (beats per minute) and the number of minutes in a day (minutes per day).'),
          sa('You want to model the cost of gas for a car trip to another city.\nName three quantities you would define, with their units.', 'Quantities:',
             key='The distance (miles), the car\'s fuel efficiency (miles per gallon), and the gas price (dollars per gallon).',
             note='Any three relevant quantities with sensible units are correct; for example, kilometers and liters may be used instead.'),
          mc('Which quantity is most useful for estimating the cost to paint the walls of a room?',
             ['The area of the walls', 'The volume of the room', 'The height of the door', 'The number of windows']),
          tf('Gallons of water used per day is a reasonable quantity for modeling a family\'s water use.', key=True),
          tf('The color of a car is a useful quantity for modeling how much fuel it uses on a trip.', key=False),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (px + q = r)
    S('7.EE.B.4.a', 'Solve word problems that lead to equations of the form px + q = r',
      main=[
          sa('A gym charges a $25 sign-up fee plus $18 per month. Ty has paid $151 in all.\nWrite and solve an equation to find the number of months m.', 'Answer:',
             key='The equation 18m + 25 = 151 and the answer m = 7 months',
             note='Both parts are required: a valid equation (for example 18m + 25 = 151) and the correct answer, 7 months. Any valid equation is accepted, but the solution must also be correct.'),
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
          sa('Solve y = mx + b for x. Assume m ≠ 0.', 'x =', key='(y - b)/m'),
          mc('Solve A = {1/2}bh for h, where the base b > 0.', ['h = {2A/b}', 'h = {A/2b}', 'h = 2Ab', 'h = {b/2A}']),
          tf('For a speed r > 0, solving d = rt for t gives t = {d/r}.', key=True),
          tf('Solving C = 5n + 20 for n gives n = 5C - 20.', key=False, note='n = (C - 20)/5.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (p(x + q) = r)
    S('7.EE.B.4.a', 'Solve word problems that lead to equations of the form p(x + q) = r',
      main=[
          sa('A rectangle is 7 cm wide and (x + 3) cm long. Its area is 63 cm².\nWrite and solve an equation to find x.', 'Answer:',
             key='The equation 7(x + 3) = 63 and the answer x = 6',
             note='Both parts are required: a valid equation (for example 7(x + 3) = 63) and the correct answer, x = 6. Any valid equation is accepted, but the solution must also be correct.'),
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
          sa('Solve for x. Give all solutions.\n(x + 3)² = 49', 'x =', key='x = 4 and x = -10',
             note='Both solutions are required. Either order and set notation, such as {4, -10}, are accepted.'),
          sa('Solve for x. Give all solutions.\nx² = 81', 'x =', key='x = 9 and x = -9',
             note='Both solutions are required; x = ±9 and set notation are accepted.'),
          mc('Solve for x.\n(x - 2)(x + 5) = 0', ['x = 2 or x = -5', 'x = -2 or x = 5', 'x = 2 only', 'x = -5 only']),
          tf('The solutions of 2(x - 1)² = 18 are x = 4 and x = -2.', key=True),
          tf('x² = 16 has only one solution, x = 4.', key=False, note='x = 4 or x = -4.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.a (compare solutions)
    S('7.EE.B.4.a', 'Compare an algebraic solution with an arithmetic solution',
      main=[
          work('A gym charges $15 to join plus $8 for each class. Max paid $79 in all.\n(a) Solve with arithmetic. (b) Write and solve an equation. (c) Compare the steps of the two solutions.', 'Classes:',
               method=COMPARE + 'Example: (a) 79 - 15 = 64, 64 ÷ 8 = 8; (b) 8c + 15 = 79, subtract 15 from both sides, then divide both sides by 8; '
                      '(c) both subtract 15 first and then divide by 8. Any valid equation is accepted.',
               key='8 classes'),
          work('Four friends each buy a ticket and a $3 popcorn. They pay $46 in all.\n(a) Solve with arithmetic. (b) Write and solve an equation. (c) Compare the steps of the two solutions.', 'Ticket price:',
               method=COMPARE + 'Example: (a) 46 ÷ 4 = 11.50, 11.50 - 3 = 8.50; (b) 4(t + 3) = 46, divide both sides by 4, then subtract 3; '
                      '(c) both divide by 4 first and then subtract 3. An equation such as 4t + 12 = 46 is also accepted, with the matching comparison.',
               key='$8.50'),
          mc('An algebraic solution of 5x - 8 = 27 adds 8 to both sides and then divides both sides by 5.\nWhich arithmetic steps match it?',
             ['Add 8 to 27, then divide by 5.', 'Subtract 8 from 27, then divide by 5.', 'Divide 27 by 5, then add 8.', 'Multiply 27 by 5, then add 8.']),
          sa('An arithmetic solution of 3(x + 4) = 33 is 33 ÷ 3 - 4.\nFor each arithmetic operation, name the algebra step that matches it. Then give x.', 'Answer:',
             key='Dividing 33 by 3 matches dividing both sides by 3; subtracting 4 matches subtracting 4 from both sides; x = 7.',
             note='Grade both matches and the value x = 7.'),
          tf('An equation multiplies x by 2 and then adds 6: 2x + 6 = 20. The arithmetic (20 - 6) ÷ 2 undoes those operations in reverse order, just as the algebra steps do.', key=True),
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
      f2=B('Justify a complete solution and find an invalid step', 'HSA-REI.A.1', [
          work('Solve 2(x + 3) = {1/2}(4x - 6) + x. Write each step and the reason for it.', 'x =',
               method='Every step with a valid reason. Example: distributive property on both sides (2x + 6 = 2x - 3 + x); combine like terms (2x + 6 = 3x - 3); '
                      'subtract 2x from both sides (6 = x - 3); add 3 to both sides (x = 9). Other valid orders are accepted. A correct answer without reasons is not full credit.',
               key='9'),
          sa('Mo solved {x/2} + 3 = x - 1 like this:\nStep 1: x + 3 = 2x - 1\nStep 2: x = 4\nWhich step is invalid? Correct it and give the solution.', 'Answer:',
             key='Step 1: multiplying both sides by 2 gives x + 6 = 2x - 2, so x = 8.', note='Grade both: Step 1 with the correction, and x = 8.'),
          mc('Which reason justifies rewriting 4x - 7 = 2x + 5 as 2x - 7 = 5?',
             ['Subtraction property of equality (subtract 2x from both sides)', 'Distributive property', 'Division property of equality', 'Commutative property of multiplication']),
          tf('Dividing both sides of 3(x - 2) = 3x - 6 by 3 gives x - 2 = x - 2, so every number is a solution of the original equation.', key=True),
          tf('Dividing both sides of x² = 5x by x keeps every solution of the equation.', key=False, note='It loses the solution x = 0.'),
      ])),

    # ------------------------------------------------------------------ 7.EE.B.4.b (solve)
    S('7.EE.B.4.b', 'Solve word problems that lead to inequalities of the form px + q > r or px + q < r',
      main=[
          sa('Sam has $40. He buys a $12 shirt and some pairs of socks that cost $3.50 each.\nWrite and solve an inequality for the number of pairs of socks p he can buy.', 'Inequality and answer:',
             key='The inequality 3.5p + 12 ≤ 40 and the solution p ≤ 8: he can buy 0 to 8 pairs (whole numbers).',
             note='Both parts are required: a valid inequality and its solution, stated as whole numbers of pairs from 0 to 8. Any valid inequality is accepted.'),
          sa('A plumber charges $55 plus $40 per hour. Ana can spend no more than $255.\nWrite and solve an inequality for the number of hours h.', 'Inequality and answer:',
             key='The inequality 40h + 55 ≤ 255 and the solution h ≤ 5: at most 5 hours.',
             note='Both parts are required. Time can be any amount from 0 to 5 hours. Any valid inequality is accepted.'),
          mc('A club has $120 and earns $15 for each car it washes. It needs more than $300.\nWhich inequality and solution fit the problem?',
             ['15c + 120 > 300; c > 12', '15c + 120 < 300; c < 12', '120c + 15 > 300; c > 2.375', '15c > 300 + 120; c > 28']),
          tf('A tank holds 500 liters and drains 25 liters per minute. The water stays above 200 liters while 500 - 25t > 200, which is while t < 12 minutes.', key=True),
          tf('Kim has $20 and saves $6 each week. To have at least $80, she solves 6w + 20 ≥ 80, so she needs at most 10 weeks.', key=False,
             note='w ≥ 10: she needs at least 10 weeks.'),
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
          draw_write('A taxi charges $3 plus $2 per mile. Ty can spend at most $15.\nSolve 2m + 3 ≤ 15 for the miles m. Then graph the possible distances on the number line. (Distances cannot be negative.)',
                     ints(0, 10), 'Solution:',
                     draw='A closed circle at 6 and the line shaded from 0 to 6 (a closed circle or the end of the shading at 0)', key='m ≤ 6, so 0 ≤ m ≤ 6 miles',
                     note='Grade both: the solution 0 ≤ m ≤ 6 (m ≤ 6 with distances not negative), and the graph from 0 to 6 with a closed circle at 6.'),
          draw_write('A freezer is at 2°C and cools 1.5°C each hour.\nSolve 2 - 1.5t < -4 to find when it is colder than -4°C. Then graph the solution on the number line.',
                     ints(0, 10), 'Solution:',
                     draw='An open circle at 4 with an arrow or shading to the right', key='t > 4: after more than 4 hours',
                     note='Grade both: t > 4 and the graph with an open circle at 4 shaded to the right.'),
          mc('Tickets cost $6 each. Jo has $40 and must keep at least $10, so 6t ≤ 30. The graph shows the solution as whole numbers.\nWhich description fits the graph?',
             ['Jo can buy 0, 1, 2, 3, 4, or 5 tickets.', 'Jo can buy any number of tickets greater than 5.', 'Jo can buy exactly 5 tickets.', 'Jo can buy 2.5 tickets.'],
             fig=ints(0, 8, pts=[(v, None) for v in range(6)])),
          draw_write('A club has $30 and earns $5 for each ticket it sells. It needs more than $230.\nSolve 5t + 30 > 230. Then graph the possible numbers of tickets (whole numbers) on the number line.',
                     ints(30, 50, every=5), 'Solution:',
                     draw='Dots at the whole numbers 41, 42, 43, ... to the end of the line, with an arrow or "..." to show the pattern continues; no dot at 40',
                     key='t > 40: the club must sell at least 41 tickets.',
                     note='Grade both: the solution with the context (at least 41 tickets), and the graph of whole numbers greater than 40.'),
          tf('A plant is 5 cm tall and grows 2 cm per week. The graph shows the weeks w when the plant is taller than 11 cm, the solution of 2w + 5 > 11.',
             fig=ints(0, 10, ray=(3, 'right', True)), key=True),
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
