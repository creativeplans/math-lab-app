"""Algebra II standards inventory: every standard of the course profile (engine/hs_courses.py ALGEBRA_II_CORE and
ALGEBRA_II_ADVANCED), split into the distinct demands (subskills) that MAIN sets must cover.

Wording follows the Common Core State Standards for Mathematics, High School (thecorestandards.org/Math/Content/HSN/,
HSA/, HSF/, HSS/). The authoring environment could not open that site or the Appendix A pathway document (network
policy), so the text below was written from the published standards and must be spot-checked against the official pages
(README, "Assumptions"). A "★" is the official modeling mark; "(+)" is the official advanced mark.

REVISIT names the new demand when a code is shared with Algebra I in the pathway: the Algebra II sets assess that demand,
not the Algebra I one. Each subskill ID must be listed in covers= of exactly the MAIN sets that test it.
"""

STANDARDS = {
    # ---------------------------------------------------------------- N-CN The Complex Number System
    'HSN-CN.A.1': ('Know there is a complex number i such that i² = −1, and every complex number has the form a + bi with a '
                   'and b real.', [
        ('CN1-form', 'Write square roots of negative numbers with i and identify the real and imaginary parts of a + bi'),
    ]),
    'HSN-CN.A.2': ('Use the relation i² = −1 and the commutative, associative, and distributive properties to add, subtract, '
                   'and multiply complex numbers.', [
        ('CN2-addsub', 'Add and subtract complex numbers'),
        ('CN2-mult', 'Multiply complex numbers and simplify powers of i using i² = −1'),
    ]),
    'HSN-CN.C.7': ('Solve quadratic equations with real coefficients that have complex solutions.', [
        ('CN7-solve', 'Solve quadratic equations with real coefficients whose solutions are non-real complex numbers'),
    ]),
    'HSN-CN.C.8': ('(+) Extend polynomial identities to the complex numbers. For example, rewrite x² + 4 as (x + 2i)(x − 2i).', [
        ('CN8-factor', 'Factor sums of squares and other polynomials over the complex numbers using polynomial identities'),
    ]),
    'HSN-CN.C.9': ('(+) Know the Fundamental Theorem of Algebra; show that it is true for quadratic polynomials.', [
        ('CN9-fta', 'Use the Fundamental Theorem of Algebra to count complex zeros with multiplicity, and show it for quadratics'),
    ]),
    'HSN-CN.A.3': ('(+) Find the conjugate of a complex number; use conjugates to find moduli and quotients of complex numbers.', [
        ('CN3-conj', 'Use conjugates to find moduli and quotients of complex numbers'),
    ]),
    # ---------------------------------------------------------------- A-SSE Seeing Structure in Expressions
    'HSA-SSE.A.1.a': ('Interpret expressions that represent a quantity in terms of its context.★ a. Interpret parts of an '
                      'expression, such as terms, factors, and coefficients.', [
        ('SSE1a-parts', 'REVISIT with polynomial, rational, and exponential expressions: interpret terms, factors, coefficients, '
                        'and bases in context'),
    ]),
    'HSA-SSE.A.1.b': ('Interpret expressions that represent a quantity in terms of its context.★ b. Interpret complicated '
                      'expressions by viewing one or more of their parts as a single entity. For example, interpret P(1+r)ⁿ '
                      'as the product of P and a factor not depending on P.', [
        ('SSE1b-entity', 'REVISIT: reason about a complicated expression by treating a part as a single quantity (sign, size, '
                         'limits on its value)'),
    ]),
    'HSA-SSE.A.2': ('Use the structure of an expression to identify ways to rewrite it. For example, see x⁴ − y⁴ as '
                    '(x²)² − (y²)², thus recognizing it as a difference of squares that can be factored as (x² − y²)(x² + y²).', [
        ('SSE2-factor', 'REVISIT beyond quadratics: factor higher-degree expressions by seeing differences of squares and '
                        'sums or differences of cubes'),
        ('SSE2-quadform', 'REVISIT: rewrite expressions in quadratic form (a substitution such as u = x²) and factor'),
    ]),
    'HSA-SSE.B.4': ('Derive the formula for the sum of a finite geometric series (when the common ratio is not 1), and use the '
                    'formula to solve problems. For example, calculate mortgage payments.★', [
        ('SSE4-derive', 'Derive the sum formula of a finite geometric series (r ≠ 1)'),
        ('SSE4-apply', 'Use the finite geometric series formula to solve problems'),
    ]),
    # ---------------------------------------------------------------- A-APR
    'HSA-APR.A.1': ('Understand that polynomials form a system analogous to the integers, namely, they are closed under the '
                    'operations of addition, subtraction, and multiplication; add, subtract, and multiply polynomials.', [
        ('APR1-addsub', 'REVISIT beyond quadratics: add and subtract polynomials of higher degree'),
        ('APR1-mult', 'REVISIT beyond quadratics: multiply polynomials of higher degree'),
    ]),
    'HSA-APR.B.2': ('Know and apply the Remainder Theorem: For a polynomial p(x) and a number a, the remainder on division by '
                    'x − a is p(a), so p(a) = 0 if and only if (x − a) is a factor of p(x).', [
        ('APR2-remainder', 'Find a remainder on division by x − a as p(a)'),
        ('APR2-factor', 'Use p(a) = 0 to decide whether x − a is a factor, and factor'),
    ]),
    'HSA-APR.B.3': ('Identify zeros of polynomials when suitable factorizations are available, and use the zeros to construct a '
                    'rough graph of the function defined by the polynomial.', [
        ('APR3-zeros', 'Identify zeros and their multiplicities from a factorization'),
        ('APR3-sketch', 'Identify the rough graph of a polynomial from its zeros (the standard asks students to construct it; here the graph is chosen)'),
    ]),
    'HSA-APR.C.4': ('Prove polynomial identities and use them to describe numerical relationships. For example, the polynomial '
                    'identity (x² + y²)² = (x² − y²)² + (2xy)² can be used to generate Pythagorean triples.', [
        ('APR4-prove', 'Prove polynomial identities by algebra'),
        ('APR4-use', 'Use polynomial identities to describe numerical relationships'),
    ]),
    'HSA-APR.C.5': ('(+) Know and apply the Binomial Theorem for the expansion of (x + y)ⁿ in powers of x and y for a positive '
                    'integer n, where x and y are any numbers, with coefficients determined for example by Pascal\'s Triangle.', [
        ('APR5-binom', 'Expand (x + y)ⁿ and find specific terms with the Binomial Theorem'),
    ]),
    'HSA-APR.D.6': ('Rewrite simple rational expressions in different forms; write a(x)/b(x) in the form q(x) + r(x)/b(x), where '
                    'a(x), b(x), q(x), and r(x) are polynomials with the degree of r(x) less than the degree of b(x), using '
                    'inspection, long division, or, for the more complicated examples, a computer algebra system.', [
        ('APR6-divide', 'Write a(x)/b(x) as q(x) + r(x)/b(x) by long division'),
        ('APR6-inspect', 'Rewrite simple rational expressions by inspection and interpret the quotient and remainder'),
    ]),
    'HSA-APR.D.7': ('(+) Understand that rational expressions form a system analogous to the rational numbers, closed under '
                    'addition, subtraction, multiplication, and division by a nonzero rational expression; add, subtract, '
                    'multiply, and divide rational expressions.', [
        ('APR7-muldiv', 'Multiply and divide rational expressions, keeping the excluded values'),
        ('APR7-addsub', 'Add and subtract rational expressions, keeping the excluded values'),
    ]),
    # ---------------------------------------------------------------- A-CED, A-REI
    'HSA-CED.A.1': ('Create equations and inequalities in one variable and use them to solve problems. Include equations '
                    'arising from linear and quadratic functions, and simple rational and exponential functions.★', [
        ('CED1-eq', 'REVISIT: create and solve one-variable rational, radical, and exponential equations from contexts'),
        ('CED1-ineq', 'REVISIT: create and solve one-variable polynomial, rational, and exponential inequalities from contexts'),
    ]),
    'HSA-CED.A.2': ('Create equations in two or more variables to represent relationships between quantities; graph equations '
                    'on coordinate axes with labels and scales.★', [
        ('CED2-graph', 'REVISIT: create and graph two-variable nonlinear models with labeled axes and scales'),
    ]),
    'HSA-CED.A.3': ('Represent constraints by equations or inequalities, and by systems of equations and/or inequalities, and '
                    'interpret solutions as viable or nonviable options in a modeling context.★', [
        ('CED3-constraints', 'REVISIT: represent nonlinear constraints and judge viable options'),
    ]),
    'HSA-CED.A.4': ('Rearrange formulas to highlight a quantity of interest, using the same reasoning as in solving equations.★', [
        ('CED4-rearrange', 'REVISIT: rearrange rational, radical, and exponential formulas, stating the conditions used'),
    ]),
    'HSA-REI.A.2': ('Solve simple rational and radical equations in one variable, and give examples showing how extraneous '
                    'solutions may arise.', [
        ('REI2-rational', 'Solve rational equations and identify extraneous solutions'),
        ('REI2-radical', 'Solve radical equations and identify extraneous solutions'),
    ]),
    'HSA-REI.D.11': ('Explain why the x-coordinates of the points where the graphs of the equations y = f(x) and y = g(x) '
                     'intersect are the solutions of the equation f(x) = g(x); find the solutions approximately, e.g., using '
                     'technology to graph the functions, make tables of values, or find successive approximations. Include '
                     'cases where f(x) and/or g(x) are linear, polynomial, rational, absolute value, exponential, and '
                     'logarithmic functions.★', [
        ('REI11-explain', 'REVISIT with nonlinear families: explain why intersection x-coordinates solve f(x) = g(x)'),
        ('REI11-approx', 'REVISIT: approximate solutions of f(x) = g(x) with tables, graphs, or successive approximation'),
    ]),
    # ---------------------------------------------------------------- F-TF
    'HSF-TF.A.1': ('Understand radian measure of an angle as the length of the arc on the unit circle subtended by the angle.', [
        ('TF1-radian', 'Use radian measure as arc length on the unit circle'),
    ]),
    'HSF-TF.A.2': ('Explain how the unit circle in the coordinate plane enables the extension of trigonometric functions to all '
                   'real numbers, interpreted as radian measures of angles traversed counterclockwise around the unit circle.', [
        ('TF2-values', 'Find exact trigonometric values of angles beyond the first quadrant from the unit circle'),
        ('TF2-explain', 'Explain the extension of sine and cosine to all real numbers with the unit circle'),
    ]),
    'HSF-TF.B.5': ('Choose trigonometric functions to model periodic phenomena with specified amplitude, frequency, and midline.★', [
        ('TF5-build', 'Write a sinusoidal model with a given amplitude, frequency or period, and midline'),
        ('TF5-interpret', 'Interpret and use the parameters of a sinusoidal model in context'),
    ]),
    'HSF-TF.C.8': ('Prove the Pythagorean identity sin²(θ) + cos²(θ) = 1 and use it to find sin(θ), cos(θ), or tan(θ) given '
                   'sin(θ), cos(θ), or tan(θ) and the quadrant of the angle.', [
        ('TF8-prove', 'Prove the Pythagorean identity'),
        ('TF8-use', 'Use the Pythagorean identity with the quadrant to find the other trigonometric values'),
    ]),
    'HSF-TF.A.3': ('(+) Use special triangles to determine geometrically the values of sine, cosine, tangent for π/3, π/4 and '
                   'π/6, and use the unit circle to express the values of sine, cosine, and tangent for π − x, π + x, and '
                   '2π − x in terms of their values for x, where x is any real number.', [
        ('TF3-special', 'Derive values at π/6, π/4, π/3 from special triangles and relate π − x, π + x, 2π − x to x'),
    ]),
    'HSF-TF.A.4': ('(+) Use the unit circle to explain symmetry (odd and even) and periodicity of trigonometric functions.', [
        ('TF4-symmetry', 'Explain odd/even symmetry and periodicity of sine, cosine and tangent with the unit circle'),
    ]),
    'HSF-TF.B.6': ('(+) Understand that restricting a trigonometric function to a domain on which it is always increasing or '
                   'always decreasing allows its inverse to be constructed.', [
        ('TF6-restrict', 'Choose and justify domain restrictions that make sine, cosine, or tangent invertible'),
    ]),
    'HSF-TF.B.7': ('(+) Use inverse functions to solve trigonometric equations that arise in modeling contexts; evaluate the '
                   'solutions using technology, and interpret them in terms of the context.★', [
        ('TF7-solve', 'Solve trigonometric equations in models with inverse functions and find all solutions in an interval'),
    ]),
    # ---------------------------------------------------------------- F-IF
    'HSF-IF.B.4': ('For a function that models a relationship between two quantities, interpret key features of graphs and '
                   'tables in terms of the quantities, and sketch graphs showing key features given a verbal description of '
                   'the relationship. Key features include: intercepts; intervals where the function is increasing, '
                   'decreasing, positive, or negative; relative maximums and minimums; symmetries; end behavior; and '
                   'periodicity.★', [
        ('IF4-poly', 'REVISIT: interpret intercepts, intervals, relative extrema and end behavior of polynomial and rational models'),
        ('IF4-periodic', 'REVISIT: interpret periodicity, maximums, and minimums of periodic models from graphs and tables'),
    ]),
    'HSF-IF.B.5': ('Relate the domain of a function to its graph and, where applicable, to the quantitative relationship it '
                   'describes.★', [
        ('IF5-domain', 'REVISIT: state the domain of radical, rational, logarithmic and polynomial models in context'),
    ]),
    'HSF-IF.B.6': ('Calculate and interpret the average rate of change of a function (presented symbolically or as a table) '
                   'over a specified interval. Estimate the rate of change from a graph.★', [
        ('IF6-rate', 'REVISIT: average rate of change of nonlinear models, with units'),
    ]),
    'HSF-IF.C.7.b': ('Graph functions expressed symbolically and show key features of the graph, by hand in simple cases and '
                     'using technology for more complicated cases.★ b. Graph square root, cube root, and piecewise-defined '
                     'functions, including step functions and absolute value functions.', [
        ('IF7b-radical', 'REVISIT with transformations: graph square root and cube root functions'),
        ('IF7b-piecewise', 'REVISIT: graph piecewise-defined and absolute value functions'),
        ('IF7b-step', 'Identify the graphs of step functions (greatest integer and rounding-up rate models) with open and closed endpoints'),
    ]),
    'HSF-IF.C.7.c': ('Graph polynomial functions, identifying zeros when suitable factorizations are available, and showing end '
                     'behavior.★', [
        ('IF7c-poly', 'Graph polynomial functions showing zeros and end behavior'),
    ]),
    'HSF-IF.C.7.e': ('Graph exponential and logarithmic functions, showing intercepts and end behavior, and trigonometric '
                     'functions, showing period, midline, and amplitude.★', [
        ('IF7e-exp', 'REVISIT: graph exponential functions with intercept, asymptote, and end behavior'),
        ('IF7e-log', 'Graph logarithmic functions with intercept, asymptote, and end behavior'),
        ('IF7e-trig', 'Graph trigonometric functions showing period, midline, and amplitude'),
    ]),
    'HSF-IF.C.8.b': ('Write a function defined by an expression in different but equivalent forms to reveal and explain '
                     'different properties of the function. b. Use the properties of exponents to interpret expressions for '
                     'exponential functions.', [
        ('IF8b-rates', 'REVISIT: rewrite exponential functions to reveal rates over other time units and compare growth'),
    ]),
    'HSF-IF.C.9': ('Compare properties of two functions each represented in a different way (algebraically, graphically, '
                   'numerically in tables, or by verbal descriptions).', [
        ('IF9-compare', 'REVISIT with Algebra II families: compare properties of functions given in different representations'),
    ]),
    'HSF-IF.C.7.d': ('(+) Graph rational functions, identifying zeros and asymptotes when suitable factorizations are available, '
                     'and showing end behavior.★', [
        ('IF7d-asym', 'Graph rational functions with zeros, vertical and horizontal asymptotes, and end behavior'),
        ('IF7d-hole', 'Distinguish removable discontinuities (holes) from vertical asymptotes'),
    ]),
    # ---------------------------------------------------------------- F-BF, F-LE
    'HSF-BF.A.1.b': ('Write a function that describes a relationship between two quantities.★ b. Combine standard function types '
                     'using arithmetic operations.', [
        ('BF1b-combine', 'REVISIT: build models by adding, subtracting, multiplying, or dividing Algebra II function types'),
    ]),
    'HSF-BF.B.3': ('Identify the effect on the graph of replacing f(x) by f(x) + k, k f(x), f(kx), and f(x + k) for specific '
                   'values of k (both positive and negative); find the value of k given the graphs. Experiment with cases and '
                   'illustrate an explanation of the effects on the graph using technology. Include recognizing even and odd '
                   'functions from their graphs and algebraic expressions for them.', [
        ('BF3-shift', 'REVISIT: f(x) + k, k·f(x), and f(x + k) on Algebra II families; find k from graphs'),
        ('BF3-horizontal', 'Horizontal stretches, compressions, and reflections f(kx), including negative k'),
        ('BF3-evenodd', 'Recognize even and odd functions from graphs and expressions'),
    ]),
    'HSF-BF.B.4.a': ('Find inverse functions. a. Solve an equation of the form f(x) = c for a simple function f that has an '
                     'inverse and write an expression for the inverse.', [
        ('BF4a-inverse', 'REVISIT: write inverses of radical, rational, cubic, exponential, and logarithmic functions with domains'),
    ]),
    'HSF-LE.A.4': ('For exponential models, express as a logarithm the solution to abᶜᵗ = d where a, c, and d are numbers and '
                   'the base b is 2, 10, or e; evaluate the logarithm using technology.★', [
        ('LE4-exact', 'Write the solution of ab^(ct) = d as an exact logarithm'),
        ('LE4-tech', 'Evaluate logarithmic solutions of exponential models with technology and interpret them'),
    ]),
    'HSF-BF.A.1.c': ('(+) Compose functions. For example, if T(y) is the temperature in the atmosphere as a function of height, '
                     'and h(t) is the height of a weather balloon as a function of time, then T(h(t)) is the temperature at the '
                     'location of the weather balloon as a function of time.', [
        ('BF1c-compose', 'Compose functions and interpret compositions in context, with domains'),
    ]),
    'HSF-BF.B.4.b': ('(+) Verify by composition that one function is the inverse of another.', [
        ('BF4b-verify', 'Verify inverses by composition on the stated domains'),
    ]),
    'HSF-BF.B.4.c': ('(+) Read values of an inverse function from a graph or a table, given that the function has an inverse.', [
        ('BF4c-read', 'Read inverse values from graphs and tables'),
    ]),
    'HSF-BF.B.4.d': ('(+) Produce an invertible function from a non-invertible function by restricting the domain.', [
        ('BF4d-restrict', 'Restrict a domain to make a function invertible and write the inverse'),
    ]),
    'HSF-BF.B.5': ('(+) Understand the inverse relationship between exponents and logarithms and use this relationship to solve '
                   'problems involving logarithms and exponents.', [
        ('BF5-loginv', 'Use the inverse relationship of exponents and logarithms to solve logarithmic and exponential equations'),
    ]),
    # ---------------------------------------------------------------- Statistics and probability
    'HSS-ID.A.4': ('Use the mean and standard deviation of a data set to fit it to a normal distribution and to estimate '
                   'population percentages. Recognize that there are data sets for which such a procedure is not '
                   'appropriate. Use calculators, spreadsheets, and tables to estimate areas under the normal curve.', [
        ('ID4-estimate', 'Estimate population percentages with a fitted normal distribution'),
        ('ID4-judge', 'Recognize data sets for which a normal model is not appropriate'),
    ]),
    'HSS-IC.A.1': ('Understand statistics as a process for making inferences about population parameters based on a random '
                   'sample from that population.', [
        ('IC1-infer', 'Distinguish population, sample, parameter, and statistic, and what a random sample allows'),
    ]),
    'HSS-IC.A.2': ('Decide if a specified model is consistent with results from a given data-generating process, e.g., using '
                   'simulation.', [
        ('IC2-model', 'Decide whether a model is consistent with observed results using a supplied simulation'),
    ]),
    'HSS-IC.B.3': ('Recognize the purposes of and differences among sample surveys, experiments, and observational studies; '
                   'explain how randomization relates to each.', [
        ('IC3-types', 'Identify sample surveys, experiments, and observational studies and their purposes'),
        ('IC3-random', 'Explain random sampling versus random assignment and what each allows one to conclude'),
    ]),
    'HSS-IC.B.4': ('Use data from a sample survey to estimate a population mean or proportion; develop a margin of error '
                   'through the use of simulation models for random sampling.', [
        ('IC4-prop', 'Estimate a population proportion with a margin of error from a simulation'),
        ('IC4-mean', 'Estimate a population mean with a margin of error from a simulation'),
    ]),
    'HSS-IC.B.5': ('Use data from a randomized experiment to compare two treatments; use simulations to decide if differences '
                   'between parameters are significant.', [
        ('IC5-compare', 'Compare two treatments with a re-randomization simulation'),
    ]),
    'HSS-IC.B.6': ('Evaluate reports based on data.', [
        ('IC6-evaluate', 'Evaluate claims in reports based on data'),
    ]),
    'HSS-MD.B.6': ('(+) Use probabilities to make fair decisions (e.g., drawing by lots, using a random number generator).', [
        ('MD6-fair', 'Design and judge fair decision procedures with probabilities'),
    ]),
    'HSS-MD.B.7': ('(+) Analyze decisions and strategies using probability concepts (e.g., product testing, medical testing, '
                   'pulling a hockey goalie at the end of a game).', [
        ('MD7-decide', 'Analyze decisions and strategies with probabilities'),
    ]),
}


def subskills():
    return [(sid, code, desc) for code, (_, subs) in STANDARDS.items() for sid, desc in subs]
