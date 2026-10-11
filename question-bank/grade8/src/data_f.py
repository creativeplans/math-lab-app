from qb import S, B, sa, mc, tf, plot, draw_write, table, hrow
from common import grid, plane


def tbl(xname, xs, yname, ys):
    return table([[xname] + [str(v) for v in xs], [yname] + [str(v) for v in ys]], header='col')


WALK = grid(10, 10, xlabel='Minutes', ylabel='Blocks from home', lines=[((0, 0), (4, 6)), ((4, 6), (6, 6)), ((6, 6), (10, 0))],
            desc='Ana\'s walk: the distance from home rises from 0 to 6 blocks over the first 4 minutes, stays at 6 blocks from 4 to 6 minutes, '
                 'and falls back to 0 from 6 to 10 minutes.')
CAR = grid(6, 50, ystep=10, xlabel='Minutes', ylabel='Speed (mph)', lines=[((0, 0), (2, 40)), ((2, 40), (5, 40)), ((5, 40), (6, 0))],
           desc='A car\'s speed rises from 0 to 40 mph over 2 minutes, stays at 40 mph until minute 5, and falls to 0 at minute 6.')
TEMP = grid(12, 30, ystep=5, xlabel='Hours after 6 a.m.', ylabel='Temperature (°C)', lines=[((0, 10), (9, 28)), ((9, 28), (12, 22))],
            desc='The temperature rises in a straight line from 10°C at 0 hours to 28°C at 9 hours, then falls to 22°C at 12 hours.')
TANK = grid(6, 60, ystep=10, xlabel='Minutes', ylabel='Gallons', lines=[((0, 60), (6, 0))])


def sketch(xlabel, ylabel):
    return grid(10, 10, xlabel=xlabel, ylabel=ylabel)


SETS = [
    # ------------------------------------------------------------------ 8.F.A.1 (is it a function)
    S('8.F.A.1', 'Decide whether a relation is a function',
      main=[
          tf('The table shows y as a function of x.', fig=tbl('x', [1, 2, 3, 4], 'y', [5, 5, 7, 9]), key=True),
          sa('Is the relation in the table a function? Explain.', 'Answer:', fig=tbl('x', [2, 3, 3, 5], 'y', [4, 6, 8, 10]),
             key='No. The input 3 has two different outputs (6 and 8).'),
          mc('Which set of ordered pairs is a function?', ['(1, 4), (2, 4), (3, 4)', '(1, 2), (1, 3), (2, 4)', '(0, 0), (0, 1), (1, 1)', '(5, 1), (6, 2), (5, 3)']),
          sa('Do the points on the graph show y as a function of x? Explain.', 'Answer:', fig=grid(5, 6, pts=[(1, 1), (2, 3), (2, 5), (4, 2)]),
             key='No. The input x = 2 has two outputs (3 and 5).'),
          tf('A rule assigns each month of the year to the students in a class born in that month. This rule is a function.', key=False,
             note='One month can be paired with several students, so an input has more than one output.'),
      ],
      back=[
          B('Find the output of a rule', '6.EE.C.9', [
              sa('The rule is y = 2x + 1.\nWhat is y when x = 4?', 'y =', key='9'),
              sa('The table follows a pattern.\nWhat is y when x = 4?', 'y =', fig=tbl('x', [1, 2, 3], 'y', [4, 7, 10]), key='13'),
              mc('The rule is: output = input × 3.\nWhat is the output for an input of 7?', ['21', '10', '73', '4']),
              tf('For y = x - 5, an input of x = 9 gives y = 4.', key=True),
              tf('For y = 4x, an input of x = 3 gives y = 7.', key=False),
          ]),
          B('Read points in the first quadrant', '5.G.A.2', [
              sa('What are the coordinates of point A?', 'Coordinates:', fig=grid(6, 6, pts=[(3, 4, 'A')]), key='(3, 4)'),
              sa('What are the coordinates of point B?', 'Coordinates:', fig=grid(6, 6, pts=[(5, 1, 'B')]), key='(5, 1)'),
              mc('Which point is 2 units to the right of the origin and 5 units up?', ['(2, 5)', '(5, 2)', '(2, 2)', '(5, 5)']),
              tf('The point (0, 3) is on the y-axis.', key=True),
              tf('The point (4, 0) is 4 units up from the origin.', key=False),
          ]),
      ],
      f1=B('Use function notation and find the domain and range', 'HSF-IF.A.1', [
          sa('A function f is made of the pairs (1, 3), (2, 5), and (4, 9).\nWhat is its domain?', 'Domain:', key='1, 2, and 4'),
          sa('A function f is made of the pairs (1, 3), (2, 5), and (4, 9).\nWhat is its range?', 'Range:', key='3, 5, and 9'),
          mc('The output of f is 7 when the input is 2.\nWhich statement says this in function notation?', ['f(2) = 7', 'f(7) = 2', 'f = 2 × 7', '2f = 7']),
          tf('If f(x) = x², then f(-3) = 9.', key=True),
          tf('A function can assign two different outputs to the same input.', key=False),
      ]),
      f2=B('Find the inverse of a linear function', 'HSF-BF.B.4.a', [
          sa('f(x) = 2x + 3\nWrite the inverse function.', 'f⁻¹(x) =', key='(x - 3)/2', note='{x/2} - {3/2} is also correct.'),
          sa('f(x) = 2x + 3\nSolve f(x) = 11.', 'x =', key='4'),
          mc('g(x) = {x/5}\nWhat is the inverse function?', ['g⁻¹(x) = 5x', 'g⁻¹(x) = {5/x}', 'g⁻¹(x) = x - 5', 'g⁻¹(x) = x + 5']),
          tf('If f(2) = 7 and f has an inverse, then f⁻¹(7) = 2.', key=True),
          tf('Every function has an inverse function.', key=False, note='f(x) = x² gives the same output for 2 and -2, so it has no inverse on all real numbers.'),
      ])),

    # ------------------------------------------------------------------ 8.F.A.1 (graph of a function)
    S('8.F.A.1', 'Graph a function as the set of ordered pairs of inputs and outputs',
      main=[
          plot('The function y = 2x + 1 has the inputs 0, 1, 2, and 3.\nPlot the ordered pairs (input, output) on the grid.', grid(4, 8), key='Points at (0, 1), (1, 3), (2, 5), and (3, 7)'),
          sa('The points show a function.\nWhat is the output when the input is 3?', 'Output:', fig=grid(5, 10, pts=[(1, 2), (2, 4), (3, 7), (4, 9)]), key='7'),
          mc('The graph of a function contains the point (4, 10).\nWhich statement is true?',
             ['When the input is 4, the output is 10.', 'When the input is 10, the output is 4.', 'The function adds 4 to every input.', 'The graph has only one point.']),
          sa('The rule is "output = input squared."\nWrite the ordered pairs (input, output) for the inputs -2, -1, 0, 1, and 2.', 'Ordered pairs:',
             key='(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)'),
          tf('The graph of a function can contain both (2, 5) and (2, 8).', key=False, note='The input 2 cannot have two outputs.'),
      ],
      back=[
          B('Make ordered pairs from an equation', '6.EE.C.9', [
              sa('For y = 3x, what are the values of y when x = 0, 1, and 2?', 'Values:', key='0, 3, and 6'),
              sa('For y = x + 4, what is y when x = 5?', 'y =', key='9'),
              mc('Which pair (x, y) fits y = 5x?', ['(2, 10)', '(10, 2)', '(5, 1)', '(2, 7)']),
              tf('The pair (3, 9) fits y = 3x.', key=True),
              tf('The pair (4, 6) fits y = x + 1.', key=False),
          ]),
          B('Graph points from a pattern', '5.G.A.2', [
              plot('Plot the points (1, 2), (2, 4), and (3, 6) on the grid.', grid(4, 7), key='Points at (1, 2), (2, 4), and (3, 6)'),
              sa('The y-values start at 1 and increase by 2: (1, 1), (2, 3), (3, 5), ...\nWhat is the point for x = 4?', 'Point:', key='(4, 7)'),
              mc('Which point is 3 units to the right of the origin and 1 unit up?', ['(3, 1)', '(1, 3)', '(3, 3)', '(1, 1)']),
              tf('The point (2, 6) is 2 units to the right of the origin and 6 units up.', key=True),
              tf('To plot (5, 2), you move 5 units up and 2 units to the right.', key=False),
          ]),
      ],
      f1=B('Choose a domain that fits a function\'s situation', 'HSF-IF.B.5', [
          sa('A function gives the cost of n concert tickets at $12 each. A buyer may buy at most 8 tickets.\nWhat is a sensible domain?', 'Domain:', key='The whole numbers 0 through 8'),
          sa('h(t) gives the height of a ball t seconds after it is thrown, until it lands at t = 3.\nWhat is a sensible domain?', 'Domain:', key='0 ≤ t ≤ 3'),
          mc('p is the number of people in a car that seats 5.\nWhich domain makes sense for p?', ['0, 1, 2, 3, 4, 5', 'All real numbers', 'p ≥ 0', '-5 ≤ p ≤ 5']),
          tf('For the area of a square as a function of its side length, the domain contains only positive numbers.', key=True),
          tf('A function that gives the number of buses needed for n students should have all real numbers as its domain.', key=False),
      ]),
      f2=B('Graph quadratic functions and show their key features', 'HSF-IF.C.7.a', [
          plot('Graph y = x² - 4 on the coordinate plane. Mark the vertex and the x-intercepts.', plane(),
               key='A U-shaped parabola with its vertex at (0, -4), crossing the x-axis at (-2, 0) and (2, 0)'),
          sa('What is the vertex of the graph of y = (x - 1)² + 2?', 'Vertex:', key='(1, 2)'),
          mc('Where does the graph of y = x² - 9 cross the x-axis?', ['At (3, 0) and (-3, 0)', 'At (9, 0) and (-9, 0)', 'At (0, -9)', 'At (3, 0) only']),
          tf('The graph of y = -x² opens downward.', key=True),
          tf('The graph of y = 2x + 3 has a vertex.', key=False),
      ])),

    # ------------------------------------------------------------------ 8.F.A.2
    S('8.F.A.2', 'Compare two functions represented in different ways',
      main=[
          sa('f(x) = 3x + 2. The table shows g.\nWhich function has the greater rate of change?', 'Answer:', fig=tbl('x', [0, 2, 4], 'g(x)', [1, 9, 17]), key='g (its rate is 4; f\'s is 3)'),
          sa('The graph shows f. g(x) = -2x + 5.\nWhich function has the greater initial value?', 'Answer:', fig=grid(5, 8, lines=[((0, 3), (5, 8))]), key='g (5 is greater than 3)'),
          mc('Function A is y = 0.5x + 10. Function B is a line through (0, 4) and (2, 8).\nWhich statement is true?',
             ['B has the greater rate of change; A has the greater initial value.', 'A has the greater rate of change and the greater initial value.',
              'B has the greater rate of change and the greater initial value.', 'They have the same rate of change.']),
          sa('Car A travels d = 45t miles in t hours. The table shows Car B.\nWhich car is faster, and by how much?', 'Answer:', fig=tbl('Hours', [1, 2, 3], 'Miles', [50, 100, 150]),
             key='Car B, by 5 miles per hour'),
          tf('A function with x-values 0, 1, 2 and y-values 6, 4, 2 decreases faster than y = -x + 6.', key=True),
      ],
      back=[
          B('Find a unit rate from a table, graph, or equation', '7.RP.A.2.b', [
              sa('The table shows a proportional relationship.\nWhat is the unit rate?', 'Unit rate:', fig=tbl('x', [2, 4, 6], 'y', [5, 10, 15]), key='2.5'),
              sa('What is the unit rate in y = 7x?', 'Unit rate:', key='7'),
              mc('A proportional graph passes through (0, 0) and (3, 12).\nWhat is the unit rate?', ['4', '3', '12', '36']),
              tf('A proportional table with the pairs (1, 9) and (2, 18) has a unit rate of 9.', key=True),
              tf('The unit rate in y = 0.5x is 2.', key=False),
          ]),
          B('Find the starting value of a relationship', '6.EE.C.9', [
              sa('For y = 4x + 7, what is y when x = 0?', 'y =', key='7'),
              sa('For the table, what is y when x = 0?', 'y =', fig=tbl('x', [0, 1, 2], 'y', [9, 11, 13]), key='9'),
              mc('Which equation gives y = 5 when x = 0?', ['y = 2x + 5', 'y = 5x', 'y = 5x + 2', 'y = x - 5']),
              tf('For y = 3x + 1, y = 1 when x = 0.', key=True),
              tf('For y = 6x, y = 6 when x = 0.', key=False),
          ]),
      ],
      f1=B('Compare average rates of change of linear and nonlinear functions over intervals', 'HSF-IF.B.6', [
          sa('f(x) = x². The table shows g.\nFind the average rate of change of each function from x = 0 to x = 3.', 'Answer:', fig=tbl('x', [0, 1, 2, 3], 'g(x)', [0, 3, 6, 9]),
             key='Both are 3: f goes from 0 to 9 and g goes from 0 to 9 over 3 units.'),
          sa('f(x) = 2^x and g(x) = 3x + 5.\nFind the average rate of change of each function from x = 0 to x = 4. Which is greater?', 'Answer:',
             key='f: (16 - 1) ÷ 4 = 3.75; g: 3. f has the greater average rate of change.', note='Both rates and the comparison are required.'),
          mc('f(x) = x² and g(x) = 4x.\nWhich statement about the average rates of change from x = 1 to x = 3 is true?',
             ['They are equal (both are 4).', 'f\'s rate is greater.', 'g\'s rate is greater.', 'f\'s rate is 9 and g\'s rate is 12.']),
          tf('The average rate of change of f(x) = -x² + 4 from x = 0 to x = 2 is -2.', key=True),
          tf('The average rate of change of a linear function depends on which interval you use.', key=False, note='A linear function has the same rate over every interval.'),
      ]),
      f2=B('Describe the effect of transformations on the graph of a function', 'HSF-BF.B.3', [
          sa('How does the graph of g(x) = f(x) + 3 compare with the graph of f?', 'Answer:', key='It is the graph of f shifted up 3 units.'),
          sa('How does the graph of g(x) = (x - 2)² compare with the graph of y = x²?', 'Answer:', key='It is shifted 2 units to the right.'),
          mc('Which function shifts the graph of y = |x| down 4 units?', ['y = |x| - 4', 'y = |x - 4|', 'y = |x + 4|', 'y = 4|x|']),
          tf('The graph of y = -f(x) is the reflection of the graph of y = f(x) across the x-axis.', key=True),
          tf('The graph of y = f(x + 5) is the graph of y = f(x) shifted 5 units to the right.', key=False, note='It is shifted 5 units to the left.'),
      ])),

    # ------------------------------------------------------------------ 8.F.A.3
    S('8.F.A.3', 'Decide whether a function is linear or nonlinear',
      main=[
          mc('Which equation is a linear function?', ['y = 4x - 7', 'y = x² + 1', 'y = {3/x}', 'y = 2^x']),
          sa('Is the function in the table linear? Explain.', 'Answer:', fig=tbl('x', [0, 1, 2, 3], 'y', [1, 2, 5, 10]),
             key='No. y increases by 1, then 3, then 5, so the rate of change is not constant.'),
          sa('A = s² gives the area of a square with side length s.\nIs A a linear function of s? Use three points to support your answer.', 'Answer:',
             key='No. (1, 1), (2, 4), and (3, 9) are not on one line: the area increases by 3, then by 5.'),
          sa('Is the function in the table linear? Explain.', 'Answer:', fig=tbl('x', [0, 2, 4, 6], 'y', [7, 4, 1, -2]),
             key='Yes. y decreases by 3 each time x increases by 2, a constant rate of change of -1.5.'),
          tf('y = 3(x + 2) is a linear function.', key=True),
      ],
      back=[
          B('Decide whether a table shows a proportional relationship', '7.RP.A.2.a', [
              tf('The table shows a proportional relationship.', fig=tbl('x', [1, 2, 3], 'y', [4, 8, 12]), key=True),
              sa('Is the relationship in the table proportional? Explain.', 'Answer:', fig=tbl('x', [1, 2, 3], 'y', [3, 5, 7]), key='No. The ratios 3, 2.5, and about 2.33 are not equal.'),
              mc('Which table shows a proportional relationship?', ['x: 2, 4, 6 and y: 3, 6, 9', 'x: 1, 2, 3 and y: 2, 3, 4', 'x: 0, 1, 2 and y: 1, 2, 3', 'x: 1, 2, 3 and y: 1, 4, 9']),
              sa('The pairs (5, 2) and (10, 4) are from a proportional relationship.\nWhat is the constant of proportionality (y per x)?', 'k =', key='0.4'),
              tf('y = x + 1 is a proportional relationship.', key=False),
          ]),
          B('Find how much y changes for each change in x', '6.EE.C.9', [
              sa('How much does y increase each time x increases by 1?', 'Increase:', fig=tbl('x', [0, 1, 2, 3], 'y', [5, 8, 11, 14]), key='3'),
              sa('How much does y increase each time x increases by 2?', 'Increase:', fig=tbl('x', [0, 2, 4], 'y', [1, 5, 9]), key='4'),
              mc('In y = 6x, how much does y increase when x increases by 1?', ['6', '1', '7', '0']),
              tf('In the table with x-values 1, 2, 3 and y-values 10, 20, 30, y increases by 10 each time x increases by 1.', key=True),
              tf('In y = x + 9, y increases by 9 each time x increases by 1.', key=False),
          ]),
      ],
      f1=B('Show that linear functions grow by equal differences and exponential functions by equal factors', 'HSF-LE.A.1.a', [
          sa('Show that f(x) = 4x + 1 grows by the same amount over every interval of length 2.', 'Answer:', key='f(x + 2) - f(x) = 4(x + 2) + 1 - (4x + 1) = 8, for every x.'),
          sa('Show that g(x) = 3^x grows by the same factor over every interval of length 1.', 'Answer:', key='g(x + 1) ÷ g(x) = 3^(x + 1) ÷ 3^x = 3, for every x.'),
          mc('Which function grows by equal factors over equal intervals?', ['y = 5(2)^x', 'y = 5x + 2', 'y = 2x²', 'y = x + 5']),
          tf('The linear function f(x) = mx + b changes by m(x₂ - x₁) from x₁ to x₂.', key=True),
          tf('y = x² grows by equal differences over equal intervals.', key=False),
      ]),
      f2=B('Use factoring to find the zeros and maximum of a quadratic function', 'HSF-IF.C.8.a', [
          sa('A ball\'s height is h(t) = -16t² + 32t = -16t(t - 2) feet after t seconds.\nUse the factored form to find when the ball is at height 0.', 'Answer:',
             key='t = 0 and t = 2 seconds', note='Both times are required.'),
          sa('A ball\'s height is h(t) = -16t(t - 2) feet after t seconds. Its greatest height is halfway between the zeros.\nWhen does it reach its greatest height, and what is that height?', 'Answer:',
             key='At t = 1 second; 16 feet', note='Both the time and the height are required.'),
          mc('f(x) = x² - 6x + 8 = (x - 2)(x - 4)\nWhat are the zeros of f?', ['2 and 4', '-2 and -4', '8 only', '6 and 8']),
          tf('The graph of a quadratic function is symmetric about a vertical line through its vertex.', key=True),
          tf('The zeros of f(x) = (x - 3)(x + 5) are 3 and 5.', key=False, note='The zeros are 3 and -5.'),
      ])),

    # ------------------------------------------------------------------ 8.F.B.4 (rate and initial value)
    S('8.F.B.4', 'Find the rate of change and initial value from two points, a table, or a graph',
      main=[
          sa('A linear function passes through (2, 7) and (5, 16).\nWhat are its rate of change and its initial value?', 'Answer:', key='Rate of change 3; initial value 1', note='Grade both values.'),
          sa('The table shows a linear function.\nWhat are its rate of change and its initial value?', 'Answer:', fig=tbl('x', [1, 3, 5], 'y', [10, 16, 22]),
             key='Rate of change 3; initial value 7', note='Grade both values.'),
          mc('The graph shows a linear function.\nWhat are its rate of change and its initial value?',
             ['Rate 2, initial value -2', 'Rate -2, initial value 2', 'Rate 4, initial value -2', 'Rate 2, initial value 6'], fig=plane(lines=[((0, -2), (4, 6))])),
          sa('A line passes through (-1, 8) and (3, 0).\nWrite its equation in the form y = mx + b.', 'Equation:', key='y = -2x + 6'),
          tf('A linear function with f(0) = 5 and f(2) = 1 has a rate of change of -2.', key=True),
      ],
      back=[
          B('Find a constant rate from a table', '7.RP.A.2.b', [
              sa('The table shows a proportional relationship.\nWhat is the constant rate (y per x)?', 'Rate:', fig=tbl('x', [3, 6, 9], 'y', [12, 24, 36]), key='4'),
              sa('The table shows a proportional relationship.\nWhat is the constant rate (y per x)?', 'Rate:', fig=tbl('Hours', [2, 5, 8], 'Miles', [7, 17.5, 28]), key='3.5 miles per hour'),
              mc('A proportional table contains the pair (4, 10).\nWhat is the constant rate (y per x)?', ['2.5', '0.4', '6', '40']),
              tf('A proportional table with the pairs (2, 1) and (6, 3) has a constant rate of 0.5.', key=True),
              tf('A proportional table with the pairs (5, 15) and (8, 24) has a constant rate of 5.', key=False),
          ]),
          B('Subtract integers', '7.NS.A.1.c', [
              sa('Subtract.\n6 - (-2)', 'Difference:', key='8'),
              sa('Subtract.\n-3 - 5', 'Difference:', key='-8'),
              mc('Subtract.\n-4 - (-9)', ['5', '-13', '13', '-5']),
              tf('2 - 7 = -5', key=True),
              tf('-6 - (-6) = -12', key=False),
          ]),
      ],
      f1=B('Construct linear and exponential functions from two points', 'HSF-LE.A.2', [
          sa('Write the linear function whose graph passes through (1, 4) and (3, 10).', 'f(x) =', key='3x + 1'),
          sa('Write the exponential function f(x) = a · b^x whose graph passes through (0, 5) and (1, 15).', 'f(x) =', key='5 · 3^x'),
          mc('Which exponential function passes through (0, 2) and (2, 18)?', ['f(x) = 2 · 3^x', 'f(x) = 2 · 9^x', 'f(x) = 8x + 2', 'f(x) = 18 · 2^x']),
          tf('The linear function through (0, -1) and (4, 7) is f(x) = 2x - 1.', key=True),
          tf('The exponential function through (0, 4) and (1, 2) is f(x) = 4 · 2^x.', key=False, note='The function is f(x) = 4 · (0.5)^x.'),
      ]),
      f2=B('Write arithmetic and geometric sequences recursively and explicitly', 'HSF-BF.A.2', [
          sa('Write an explicit formula for the arithmetic sequence 7, 11, 15, ..., starting with n = 1.', 'a(n) =', key='4n + 3'),
          sa('Write a recursive formula for the sequence 7, 11, 15, ...', 'Formula:', key='a(1) = 7; a(n) = a(n - 1) + 4'),
          mc('Which explicit formula gives 3, 6, 12, 24, ..., starting with n = 1?', ['a(n) = 3 · 2^(n - 1)', 'a(n) = 3n', 'a(n) = 2 · 3^(n - 1)', 'a(n) = 3 + 2n']),
          tf('An arithmetic sequence is a linear function whose domain is the counting numbers.', key=True),
          tf('The sequence 2, 5, 8, 11, ... has a common ratio of 3.', key=False, note='It has a common difference of 3.'),
      ])),

    # ------------------------------------------------------------------ 8.F.B.4 (model)
    S('8.F.B.4', 'Construct a linear function to model a situation',
      main=[
          sa('A plumber charges $65 for a visit plus $40 per hour.\nWrite a function for the cost C after h hours.', 'C =', key='40h + 65'),
          sa('A candle is 30 cm tall and burns down 2.5 cm each hour.\nWrite a function for its height h after t hours.', 'h =', key='30 - 2.5t', note='-2.5t + 30 is also correct.'),
          mc('A phone plan costs $20 per month after a $50 activation fee.\nWhich function gives the total cost C after m months?', ['C = 20m + 50', 'C = 50m + 20', 'C = 70m', 'C = 20m - 50']),
          sa('The cost of a taxi ride is a linear function of the miles m. A 3-mile ride costs $11 and a 7-mile ride costs $21.\nWrite the function.', 'C =', key='2.5m + 3.5'),
          tf('A tank holds 500 liters and drains 20 liters each minute. The function V = 500 - 20t gives the liters V after t minutes.', key=True),
      ],
      back=[
          B('Write an equation for a situation', '6.EE.C.9', [
              sa('Tickets cost $9 each.\nWrite an equation for the cost c of t tickets.', 'Equation:', key='c = 9t'),
              sa('Mia has $15 and saves $5 each week.\nWrite an equation for her savings s after w weeks.', 'Equation:', key='s = 5w + 15'),
              mc('A pool holds 100 gallons and fills at 10 gallons per minute.\nWhich equation gives the gallons g after m minutes?', ['g = 10m + 100', 'g = 100m + 10', 'g = 110m', 'g = 10m']),
              tf('Apples cost $3 per pound. The equation c = 3p gives the cost c of p pounds.', key=True),
              tf('A game costs a $10 fee plus $2 per game. The equation c = 10g + 2 gives the cost c of g games.', key=False, note='The equation is c = 2g + 10.'),
          ]),
          B('Solve a two-step equation from a model', '7.EE.B.4.a', [
              sa('Solve for h.\n40h + 65 = 185', 'h =', key='3'),
              sa('Solve for t.\n30 - 2.5t = 10', 't =', key='8'),
              mc('Solve for m.\n20m + 50 = 170', ['m = 6', 'm = 11', 'm = 8.5', 'm = 3']),
              tf('t = 4 is the solution of 500 - 20t = 420.', key=True),
              tf('h = 5 is the solution of 12h + 8 = 50.', key=False, note='The solution is h = 3.5.'),
          ]),
      ],
      f1=B('Write a function for a situation and use it to answer a question', 'HSF-BF.A.1.a', [
          sa('A gym charges $25 per month, but the first month is free.\nWrite a function for the total cost C after m months, where m ≥ 1.', 'C(m) =', key='25(m - 1)', note='25m - 25 is also correct.'),
          sa('A savings account starts with $300, and $40 is added each week.\nWrite a function S(w), then find when the balance reaches $700.', 'Function and answer:',
             key='S(w) = 40w + 300; 10 weeks', note='Grade both: the function and 10 weeks.'),
          mc('A pool is 4 feet deep and drains 0.25 foot each hour.\nWhich function gives the depth after t hours, and when is the pool empty?',
             ['d(t) = 4 - 0.25t; after 16 hours', 'd(t) = 0.25t + 4; after 16 hours', 'd(t) = 4t - 0.25; after 1 hour', 'd(t) = 4 - 0.25t; after 4 hours']),
          tf('A rental costs $30 plus $0.20 per mile. The function C(m) = 0.2m + 30 gives the cost for m miles.', key=True),
          tf('A balance of $200 decreases by $15 each month. The function B(m) = 15m + 200 gives the balance after m months.', key=False, note='The function is B(m) = 200 - 15m.'),
      ]),
      f2=B('Rearrange a formula to solve for a chosen quantity', 'HSA-CED.A.4', [
          sa('Solve C = 40h + 65 for h.', 'h =', key='(C - 65)/40'),
          sa('Solve F = {9/5}C + 32 for C.', 'C =', key='(5/9)(F - 32)'),
          mc('Solve y = mx + b for b.', ['b = y - mx', 'b = y + mx', 'b = {y/mx}', 'b = mx - y']),
          tf('For t ≠ 0, solving d = rt for r gives r = {d/t}.', key=True),
          tf('For l ≠ 0, solving A = lw for w gives w = A - l.', key=False, note='w = A/l.'),
      ])),

    # ------------------------------------------------------------------ 8.F.B.4 (interpret)
    S('8.F.B.4', 'Interpret the rate of change and initial value of a linear function in context',
      main=[
          sa('Renting a bike costs C = 4h + 10 dollars for h hours.\nWhat do the 4 and the 10 mean?', 'Meaning:', key='4: the cost goes up $4 for each hour. 10: a $10 fee (the cost at 0 hours).', note='Grade both numbers.'),
          sa('The graph shows the water in a tank.\nWhat do the rate of change and the initial value mean?', 'Meaning:', fig=TANK,
             key='The tank starts with 60 gallons (initial value) and drains 10 gallons per minute (rate of change -10).'),
          mc('A plant\'s height is h = 0.5w + 12 centimeters after w weeks.\nWhat does 0.5 mean?',
             ['The plant grows 0.5 cm each week.', 'The plant was 0.5 cm tall at the start.', 'The plant grows 12 cm each week.', 'The plant grows for 0.5 week.']),
          sa('The table shows the money in a savings account.\nWhat does the rate of change mean?', 'Meaning:', fig=tbl('Weeks', [0, 4, 8], 'Dollars', [150, 210, 270]), key='$15 is added each week.'),
          tf('For C = 4h + 10, the initial value means the bike costs $4 before any hours.', key=False, note='The initial value is $10.'),
      ],
      back=[
          B('Explain points on the graph of a proportional relationship', '7.RP.A.2.d', [
              sa('A proportional graph of gallons (x) and miles (y) passes through (1, 28).\nWhat does this point mean?', 'Meaning:', key='The car travels 28 miles on 1 gallon.'),
              mc('A proportional graph shows hours worked (x) and pay (y).\nWhat does the point (0, 0) mean?', ['0 hours of work earn $0.', 'The pay is $0 per hour.', 'The worker starts with $0 per hour.', 'There is no graph.']),
              sa('A proportional graph of minutes (x) and laps (y) passes through (6, 3).\nWhat does this point mean?', 'Meaning:', key='3 laps are swum in 6 minutes.'),
              tf('On the graph of a proportional relationship, the point (1, r) shows the unit rate r.', key=True),
              tf('On a graph of tickets (x) and cost (y), the point (2, 18) means each ticket costs $18.', key=False, note='It means 2 tickets cost $18 ($9 each).'),
          ]),
          B('Identify the independent and dependent variables', '6.EE.C.9', [
              sa('In C = 4h + 10, which variable is the independent variable?', 'Variable:', key='h'),
              sa('"Pay depends on the hours worked." Which quantity is the dependent variable?', 'Quantity:', key='Pay'),
              mc('In d = 60t, what is d?', ['The dependent variable', 'The independent variable', 'A constant', 'The rate']),
              tf('In a table of hours worked and pay, the hours are usually the independent variable.', key=True),
              tf('In y = 3x + 2, x depends on y.', key=False),
          ]),
      ],
      f1=B('Interpret the slope and intercept of a linear model of data', 'HSS-ID.C.7', [
          sa('A line of fit predicts a test score y = 4.5x + 60 for x hours of study.\nWhat does 4.5 mean?', 'Meaning:', key='Each extra hour of study goes with about 4.5 more points.'),
          sa('A line of fit predicts a test score y = 4.5x + 60 for x hours of study.\nWhat does 60 mean?', 'Meaning:', key='The predicted score for 0 hours of study.'),
          mc('A model gives a used car\'s value as y = 18,000 - 1,500x dollars after x years.\nWhat does -1,500 mean?',
             ['The value drops about $1,500 each year.', 'The car costs $1,500.', 'The value rises $1,500 each year.', 'The car is 1,500 years old.']),
          tf('A model gives a child\'s height as y = 2.1x + 30 cm at age x months. The intercept 30 is the predicted height at 0 months.', key=True),
          tf('A slope of -3 in a linear model means y increases by 3 for each unit of x.', key=False),
      ]),
      f2=B('Interpret the parameters of linear and exponential functions', 'HSF-LE.B.5', [
          sa('P(t) = 2,000(1.05)^t gives an account balance after t years.\nWhat do 2,000 and 1.05 mean?', 'Meaning:', key='2,000 is the starting amount; 1.05 means the balance grows 5% each year.', note='Grade both.'),
          sa('V(t) = 25,000(0.85)^t gives a car\'s value after t years.\nWhat is the yearly percent change?', 'Change:', key='A 15% decrease each year'),
          mc('A phone plan costs C(m) = 0.12m + 9.99 dollars for m minutes.\nWhat does 9.99 represent?', ['A fixed monthly charge', 'The cost per minute', 'The total cost', 'The number of minutes']),
          tf('In f(t) = 100(2)^t, the quantity doubles each time t increases by 1.', key=True),
          tf('In f(t) = 50(0.9)^t, the quantity grows by 90% each period.', key=False, note='It decreases by 10% each period.'),
      ])),

    # ------------------------------------------------------------------ 8.F.B.5 (describe)
    S('8.F.B.5', 'Describe the relationship shown by a graph',
      main=[
          sa('The graph shows Ana\'s walk.\nDescribe what happens from 4 to 6 minutes.', 'Description:', fig=WALK, key='She stays 6 blocks from home; she stops.'),
          mc('The graph shows Ana\'s walk.\nDuring which interval is Ana moving toward home?', ['6 to 10 minutes', '0 to 4 minutes', '4 to 6 minutes', '0 to 6 minutes'], fig=WALK),
          sa('The graph shows Ana\'s walk.\nIs the relationship linear or nonlinear over the whole walk? Explain.', 'Answer:', fig=WALK,
             key='Nonlinear. The graph is not one straight line; the rate of change is different on different parts.'),
          sa('The graph shows a car\'s speed.\nDescribe how the speed changes over the 6 minutes.', 'Description:', fig=CAR,
             key='The car speeds up for 2 minutes, travels at a steady 40 mph until minute 5, then slows to a stop.'),
          tf('In the graph of Ana\'s walk, she walks faster going home than going away from home.', fig=WALK, key=False,
             note='Both trips cover 6 blocks in 4 minutes.'),
      ],
      back=[
          B('Interpret points on a graph of a situation', '5.G.A.2', [
              sa('A graph shows minutes (x) and blocks from home (y). What does the point (3, 5) mean?', 'Meaning:', key='After 3 minutes, the walker is 5 blocks from home.'),
              sa('A graph shows days (x) and plant height in centimeters (y). What does the point (10, 4) mean?', 'Meaning:', key='After 10 days, the plant is 4 cm tall.'),
              mc('A graph shows hours (x) and miles driven (y).\nWhich point shows 120 miles after 2 hours?', ['(2, 120)', '(120, 2)', '(2, 60)', '(60, 2)']),
              tf('On a graph of time (x) and distance (y), the point (0, 0) can mean the start of a trip.', key=True),
              tf('The point (4, 1) on a graph of hours (x) and miles (y) means 4 miles in 1 hour.', key=False),
          ]),
          B('Compare speeds as unit rates', '6.RP.A.3.b', [
              sa('Ana walks 6 blocks in 4 minutes at a steady pace.\nWhat is her speed in blocks per minute?', 'Speed:', key='1.5 blocks per minute'),
              sa('Which is faster: 12 miles in 3 hours, or 10 miles in 2 hours?', 'Answer:', key='10 miles in 2 hours (5 mph, compared with 4 mph)'),
              mc('Which rate is the greatest?', ['60 miles in 1 hour', '100 miles in 2 hours', '150 miles in 3 hours', '20 miles in 0.5 hour']),
              tf('Walking 3 miles in 1 hour is faster than walking 5 miles in 2 hours.', key=True),
              tf('Running 8 km in 40 minutes is the same rate as running 2 km in 20 minutes.', key=False),
          ]),
      ],
      f1=B('Interpret the key features of a graph in context', 'HSF-IF.B.4', [
          sa('The graph shows the temperature during a day.\nWhen is the temperature highest, and what is it?', 'Answer:', fig=TEMP, key='9 hours after 6 a.m. (3 p.m.); 28°C'),
          sa('The graph shows the temperature during a day.\nOn what interval is the temperature increasing?', 'Interval:', fig=TEMP, key='From 0 to 9 hours after 6 a.m.'),
          mc('The graph shows the temperature during a day.\nWhat does the y-intercept mean?', ['It was 10°C at 6 a.m.', 'It was 28°C at 3 p.m.', 'The temperature rose for 9 hours.', 'It was 22°C at 6 p.m.'], fig=TEMP),
          tf('In the graph, the temperature is decreasing from 9 to 12 hours after 6 a.m.', fig=TEMP, key=True),
          tf('The graph shows that the temperature never dropped below 22°C.', fig=TEMP, key=False, note='It started at 10°C.'),
      ]),
      f2=B('Graph and evaluate piecewise-defined functions', 'HSF-IF.C.7.b', [
          plot('Graph the function on the coordinate plane.\nf(x) = x + 2 for x < 0\nf(x) = 2 for x ≥ 0', plane(),
               key='The line y = x + 2 for x < 0 (an open end at (0, 2) is acceptable) and the horizontal line y = 2 for x ≥ 0, with a closed point at (0, 2)'),
          sa('f(x) = 3 for x ≤ 2, and f(x) = x + 1 for x > 2.\nFind f(5).', 'f(5) =', key='6'),
          mc('A taxi charges $3 for the first mile and $2 for each mile after that.\nWhich function gives the cost for m miles?',
             ['C(m) = 3 for 0 < m ≤ 1; C(m) = 3 + 2(m - 1) for m > 1', 'C(m) = 2m + 3 for all m', 'C(m) = 3m for all m', 'C(m) = 3 + 2m for m ≤ 1 only']),
          tf('For f(x) = |x|, f(-4) = 4.', key=True),
          tf('A piecewise-defined function can never have an unbroken graph.', key=False, note='For example, f(x) = |x| is piecewise-defined and unbroken.'),
      ])),

    # ------------------------------------------------------------------ 8.F.B.5 (sketch)
    S('8.F.B.5', 'Sketch a graph from a description of a relationship',
      main=[
          plot('Sketch a graph of the water level in a bathtub over time: it fills at a steady rate, stays the same while someone bathes, and then drains quickly.',
               sketch('Time', 'Water level'),
               key='A rising straight segment from 0, then a horizontal segment, then a steeper falling segment back to 0. Any lengths are accepted if the order and steepness are right.'),
          plot('Sketch a graph of a car\'s speed over time: it speeds up, travels at a steady speed, and then slows down to a stop.', sketch('Time', 'Speed'),
               key='A rising segment from 0, a horizontal segment, then a falling segment back to 0. Any lengths are accepted if the order is right.'),
          plot('Sketch the height of a ball thrown straight up over time: it rises, slows down, reaches a highest point, and falls back to the ground.', sketch('Time', 'Height'),
               key='A curve that rises, levels off at one highest point, and falls back to height 0, like an upside-down U. Starting at ground level or at the throwing height is accepted.'),
          plot('Sketch the number of people in a theater from 6:00 to 10:00. It fills quickly before a 7:00 show, stays full, and empties after the show ends at 9:30.',
               sketch('Time', 'People in the theater'),
               key='A steep rise before 7:00, a horizontal segment from about 7:00 to 9:30, then a steep fall after 9:30 back to about 0. Exact times are not required if the order is right.'),
          draw_write('Sketch a graph of a hike: the hiker climbs a steep trail for 2 hours, then a gentle slope for 1 hour, then rests for 1 hour.\nIs elevation a linear function of time for the whole hike? Explain.',
                     sketch('Hours', 'Elevation'), 'Answer:',
                     draw='A steeper rising segment from 0 to 2 hours, a less steep rising segment from 2 to 3 hours, and a horizontal segment from 3 to 4 hours',
                     key='No. The rate of change is different on each part (steep, gentle, then zero), so the whole graph is not one line.',
                     note='Grade both: the three-part graph in the right order and steepness, and "no" with a reason.'),
      ],
      back=[
          B('Graph a relationship from a table', '6.EE.C.9', [
              plot('Graph the pairs in the table.', hrow(tbl('Hours', [0, 1, 2, 3], 'Miles', [0, 4, 8, 12]), grid(4, 12, ystep=2, xlabel='Hours', ylabel='Miles')),
                   key='Points at (0, 0), (1, 4), (2, 8), and (3, 12)'),
              sa('A hiker walks 4 miles each hour, so miles = 4 × hours.\nHow many miles does she walk in 2.5 hours?', 'Miles:', key='10'),
              mc('Which table shows y increasing by the same amount each time?', ['x: 0, 1, 2 and y: 0, 3, 6', 'x: 0, 1, 2 and y: 0, 3, 4', 'x: 0, 1, 2 and y: 5, 5, 6', 'x: 0, 1, 2 and y: 6, 3, 9']),
              tf('A table where y is 5 for every x shows y not changing.', key=True),
              tf('A table with y-values 2, 4, 3 shows y always increasing.', key=False),
          ]),
          B('Plot points that represent a situation', '5.G.A.2', [
              plot('A plant is 2 cm tall at week 0, 4 cm at week 1, and 6 cm at week 2.\nPlot the points (week, height).', grid(3, 7, xlabel='Week', ylabel='Height (cm)'),
                   key='Points at (0, 2), (1, 4), and (2, 6)'),
              sa('A plant is 2 cm tall at week 0 and grows 2 cm each week.\nWhich point shows its height at week 3?', 'Point:', key='(3, 8)'),
              mc('On a graph of weeks (x) and plant height in cm (y), what does the point (2, 6) mean?',
                 ['At week 2 the plant is 6 cm tall.', 'At week 6 the plant is 2 cm tall.', 'The plant grows 2 cm.', 'The plant grows 6 cm each week.']),
              tf('On a graph of weeks (x) and height (y), the point (0, 2) shows the height at the start.', key=True),
              tf('On a graph of weeks (x) and height in cm (y), the point (1, 4) means the plant is 1 cm tall at week 4.', key=False),
          ]),
      ],
      f1=B('Sketch graphs that show given key features', 'HSF-IF.B.4', [
          plot('Sketch a function that increases for 0 < x < 3, has a maximum value of 5 at x = 3, and decreases for x > 3.', plane(),
               key='Any graph that rises up to the point (3, 5) and falls after it, with 5 as its highest value'),
          plot('Sketch a function whose graph crosses the y-axis at 2 and that increases for all x shown.', plane(),
               key='Any always-increasing graph through (0, 2); a line or a curve is accepted'),
          mc('Which description matches y = -(x - 2)² + 4?', ['A maximum of 4 at x = 2; increasing for x < 2', 'A minimum of 4 at x = 2', 'A maximum of 2 at x = 4', 'Increasing for every x']),
          tf('A graph with a maximum at x = 3 decreases for some x-values greater than 3.', key=True),
          tf('A function that is always decreasing can have its maximum in the middle of its domain.', key=False),
      ]),
      f2=B('Graph exponential functions and describe their end behavior', 'HSF-IF.C.7.e', [
          plot('Graph y = 2^x for x from -2 to 2 on the coordinate plane.', plane(),
               key='The points (-2, 1/4), (-1, 1/2), (0, 1), (1, 2), and (2, 4) joined by a smooth increasing curve that gets close to the x-axis on the left'),
          sa('What is the y-intercept of the graph of y = 5(0.5)^x?', 'y-intercept:', key='(0, 5)'),
          mc('For y = 3^x, what happens to y as x decreases without bound?', ['y gets closer to 0.', 'y decreases without bound.', 'y gets closer to 3.', 'y increases.']),
          tf('The graph of y = 2^x never touches the x-axis.', key=True),
          tf('The function y = (0.5)^x is increasing.', key=False),
      ])),
]
