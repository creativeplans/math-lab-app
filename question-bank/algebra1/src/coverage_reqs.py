"""Algebra I requirements, the set whose MAIN section focuses on each, and the performance tested (for COVERAGE.md).
The requirement text is the set title; the performance says what students actually do in the five MAIN questions."""
_P = {
    1: 'Explain rational exponents from the power-of-a-power property; evaluate and rewrite x^(m/n)',
    2: 'Convert between radicals and rational exponents; simplify products of radicals; recognize √(x²) = |x|',
    3: 'Prove that a rational number plus an irrational number is irrational: specific cases and the general proof by contradiction',
    4: 'Convert units in multistep problems (dimensional analysis) and choose graph scales',
    5: 'Name the quantities and units a model needs and define a rate for a comparison',
    6: 'Report measured results to a precision the measuring tool supports',
    7: 'Interpret terms, factors, and coefficients of expressions in context, including growth and decay factors',
    8: 'Treat (1 + r)^n and (x - h)² as single quantities to reason about growth and greatest or least values',
    9: 'Add and subtract polynomials in standard form; explain closure',
    10: 'Multiply polynomials, including squares of binomials and binomial times trinomial',
    11: 'Factor with a GCF and the difference of squares, factoring completely (x⁴ - 16)',
    12: 'Factor trinomials with leading coefficient 1 and greater than 1',
    13: 'Factor perfect-square trinomials and expressions in quadratic form',
    14: 'Factor to find zeros of quadratic functions, including a height model; build a quadratic from zeros',
    15: 'Complete the square to write vertex form and find greatest or least values, including in context',
    16: 'Rewrite exponential expressions to show yearly, monthly, and doubling rates',
    17: 'Solve with a reason for every step; find the error in a solution; recognize identities and the c ≠ 0 condition',
    18: 'Solve linear equations with fractions, decimals, and letter coefficients; recognize no-solution equations',
    19: 'Solve linear and compound inequalities (sign reversal) and match a solution graph',
    20: 'Write and solve linear equations and inequalities from situations, rounding to whole-number answers',
    21: 'Solve formulas for a named variable (V = πr²h, C = 5/9(F - 32), A = P(1 + rt), Ohm\'s law)',
    22: 'Complete the square to solve quadratics (with work) and to derive the quadratic formula',
    23: 'Solve quadratics by factoring and square roots, including the lost root when dividing by x',
    24: 'Use the quadratic formula (exact and rounded) and the discriminant, including no real solution',
    25: 'Write and solve quadratic and exponential equations from projectile, area, and growth situations',
    26: 'Show that elimination keeps the solutions of a system and identify equivalent systems',
    27: 'Solve systems by substitution and elimination, including fraction coefficients and parallel lines',
    28: 'Write and solve systems in context (tickets, mixtures) and decide infinitely many or no solutions',
    29: 'Solve line-parabola and line-circle systems algebraically and count the intersections',
    30: 'Decide whether points are solutions from equations and graphs',
    31: 'Solve f(x) = g(x) from graphs and tables, approximate a solution to a tenth, and explain why it works',
    32: 'Graph linear inequalities and systems as half-planes, solid or dashed, and test points',
    33: 'Write equations in two or more variables from situations and graph one on labeled axes',
    34: 'Write constraint systems and judge which combinations are possible and viable',
    35: 'Decide whether relations are functions and give domains and ranges',
    36: 'Evaluate functions, solve f(x) = c, and interpret function notation in context',
    37: 'Evaluate recursive sequences and write explicit formulas; know the integer domain',
    38: 'Read maximum, intercepts, and intervals of increase and decrease from a graph in context',
    39: 'Give reasonable domains in context, including discrete and continuous domains',
    40: 'Compute and interpret average rates of change with units, from formulas and tables',
    41: 'Graph linear functions with intercepts and write slope-intercept form from two points',
    42: 'Graph quadratics with vertex and intercepts; find axis, maximum, or minimum',
    43: 'Graph absolute value functions with their vertex and intercepts; describe shifts, reflections, and stretches',
    44: 'Graph exponential functions and give intercepts, asymptotes, and growth or decay',
    45: 'Use factored and vertex forms to find zeros, extreme values, and symmetry, including profit and height models',
    46: 'Rewrite exponential functions to find yearly, monthly, and multi-year rates of growth or decay',
    47: 'Compare functions given by formulas, tables, graphs, and descriptions',
    48: 'Write explicit and recursive rules from situations',
    49: 'Combine functions by adding, subtracting, and multiplying, and interpret the parts',
    50: 'Write arithmetic and geometric sequences both ways; find terms and ratios',
    51: 'Describe and write translations, stretches, and compressions; identify even and odd functions',
    52: 'Solve f(x) = c and write inverses of linear, cubic, and rational functions',
    53: 'Prove equal differences and equal factors with algebra; classify tables',
    54: 'Recognize constant-rate situations and use the rate to predict',
    55: 'Recognize constant-percent situations and compute multi-period growth factors',
    56: 'Write linear and exponential functions from two points, a graph, and a table',
    57: 'Find where exponential growth overtakes linear and quadratic growth',
    58: 'Interpret the parameters of linear and exponential models, including half-life',
    59: 'Make dot plots; find five-number summaries and 1.5 × IQR outliers; read a histogram',
    60: 'Compare centers and spreads; compute a standard deviation; choose a measure of spread',
    61: 'Explain the effect of an outlier on mean and median; describe skew',
    62: 'Compute joint, marginal, and conditional relative frequencies and judge association',
    63: 'Choose and use linear, quadratic, and exponential models for data',
    64: 'Compute residuals, make a residual plot, and judge fit from residual patterns',
    65: 'Draw a line of fit, use the least-squares line to predict, and write a line through data points',
    66: 'Interpret slope and intercept in context and judge whether the intercept is meaningful',
    67: 'Compute r with technology and interpret it; know its range and limits',
    68: 'Separate correlation from causation, name lurking variables, and design an experiment',
    69: 'Prove that 3√7 and ax (a nonzero rational, x irrational) are irrational; explain why a ≠ 0 is needed',
    70: 'Prove that the rational numbers are closed under addition and multiplication, with nonzero denominators',
    71: 'Derive the quadratic formula by completing the square, showing every step',
    72: 'Prove both directions of the elimination equivalence and explain why one equation is kept',
    73: 'Graph line-parabola and line-circle systems, read the intersections, and check them algebraically',
    74: 'Graph square root and cube root functions; give starting points, domains, and ranges',
    75: 'Graph piecewise-defined and step functions with open and closed endpoints, and evaluate them',
    76: 'Make histograms from raw data with given intervals, and read them',
    77: 'Find five-number summaries and draw box plots from raw data',
    78: 'Sketch graphs in context from verbal descriptions of intercepts, maxima, intervals, and end behavior',
    79: 'Estimate average rates of change from graphs, with units and stated tolerances',
    80: 'Write quadratic models for area, revenue, and projectile situations',
    81: 'Write recursive and explicit rules for situations and translate between the two forms',
    82: 'Graph transformations, compare them with tables or technology, and identify even and odd functions',
    83: 'Construct scatter plots from paired data and describe the association and the model type',
    84: 'Solve linear systems by graphing, including approximate solutions checked against exact ones',
}


def requirements():
    """One row per set: (standard, requirement, [set number], performance tested). Call after build.load_grade()."""
    import build
    return [(st['std'], st['title'], [st['num']], _P[st['num']]) for st in build.all_sets()]


NOTES = [
    '- **Standards list.** The 60 standards are the Algebra I course of the Common Core traditional pathway (CCSS Appendix A, '
    'Model Course Pathways), written as leaf codes. Appendix A could not be downloaded during authoring; the list was built '
    'from it as published and checked against district Algebra I maps. A reviewer should confirm it against the adopted '
    'Algebra I course before import.',
    '- **Course placement of forward standards** (`engine/hs_courses.py`) follows Appendix A, with two choices of this bank: '
    'S-IC, S-CP, S-MD, and S-ID.A.4 are placed in Probability & Statistics, and every (+) standard is placed in Precalculus.',
    '- **Complex numbers.** Appendix A leaves quadratics with complex solutions to Algebra II. MAIN questions answer "no real '
    'solution"; complex solutions appear only in forward branches (N-CN.C.7, N-CN.C.9).',
    '- **A-REI.D.11** names linear, polynomial, rational, absolute value, exponential, and logarithmic functions. The MAIN '
    'questions use quadratic, linear, absolute value, and exponential functions; logarithmic and rational cases are left to '
    'the forward branches (Algebra II and Precalculus).',
    '- **F-IF.C.7.b** names several function families. Each has graphing work in a focused set: absolute value (S43), square and cube '
    'roots (S74), and piecewise-defined and step functions (S75).',
    '- **N-Q.A.1-3** are modeling standards that apply throughout the course. They have one focused set each, and many other '
    'questions state units and rounding.',
    '- **No difficulty or hint fields.** As in Grades 3-8, difficulty is carried by the section (Section 3), and each '
    'question\'s explanation is in its `grading_note`, which can be shown as feedback after grading.',
    '- **Answer checking.** The game\'s answer checker has not been seen. Questions marked "Any equivalent form" need a '
    'checker that can recognize equivalent expressions (for example 2.5 and 5/2, or 4(0.5)^x and 4(1/2)^x) or a person. '
    'Questions marked "Form required" accept only the stated form (factored, expanded, vertex form, exact, rounded).',
    '- **Drawing and figures.** Graphing questions (`plot`, `plot_text`) need a drawing surface or teacher grading. The '
    'figure renderer draws solid lines only, so no figure shows a dashed boundary: inequality graphs are drawn by students, '
    'and one question describes a boundary line in words.',
    '- **Forward branches.** FORWARD 2 is never in an earlier course than FORWARD 1 (the build checks the course order). Within a '
    'course, the branch titles in Section 2 state the demand each branch adds. Branches that do not directly continue the MAIN skill '
    'are marked NEAREST RELATED and state their connection (Section 5).',
    '- **Technology.** Questions that ask for a correlation coefficient, logarithm values, or rounded roots expect a '
    'calculator (listed in Section 6).',
]
