"""Probability & Statistics standards inventory: every High School Statistics & Probability (HSS) standard, split into the
distinct demands (subskills) that MAIN sets must cover.

Wording follows the Common Core State Standards for Mathematics, High School Statistics & Probability
(thecorestandards.org/Math/Content/HSS/ and its ID, IC, CP and MD pages). The authoring environment could not open that
site (network policy), so the text below was written from the published standards and must be spot-checked against the
official pages (README, "Assumptions"). "(+)" is the official advanced mark.

Each subskill ID must be listed in covers= of exactly the MAIN sets that test it. A subskill whose verb asks students to
construct, design, perform or explain is assessed by what the game can check (see COVERAGE.md, "Assessed response").
"""

STANDARDS = {
    # ---------------------------------------------------------------- S-ID Interpreting Categorical and Quantitative Data
    'HSS-ID.A.1': ('Represent data with plots on the real number line (dot plots, histograms, and box plots).', [
        ('ID1-dot', 'Represent a data set with a dot plot (the count at each value) and choose the dot plot of a data set'),
        ('ID1-hist', 'Represent a data set with a histogram using stated bins and an endpoint rule'),
        ('ID1-box', 'Represent a data set with a box plot: the five-number summary under a stated quartile rule'),
    ]),
    'HSS-ID.A.2': ('Use statistics appropriate to the shape of the data distribution to compare center (median, mean) and '
                   'spread (interquartile range, standard deviation) of two or more different data sets.', [
        ('ID2-center', 'Compare the centers of two or more data sets with the measure suited to their shapes'),
        ('ID2-spread', 'Compare the spreads of two or more data sets with the IQR or the standard deviation'),
    ]),
    'HSS-ID.A.3': ('Interpret differences in shape, center, and spread in the context of the data sets, accounting for possible '
                   'effects of extreme data points (outliers).', [
        ('ID3-context', 'Interpret differences in shape, center, and spread between data sets in context'),
        ('ID3-outlier', 'Identify outliers with the 1.5·IQR rule and account for their effect on center and spread'),
    ]),
    'HSS-ID.A.4': ('Use the mean and standard deviation of a data set to fit it to a normal distribution and to estimate '
                   'population percentages. Recognize that there are data sets for which such a procedure is not '
                   'appropriate. Use calculators, spreadsheets, and tables to estimate areas under the normal curve.', [
        ('ID4-rule', 'Estimate population percentages from a normal model with the 68-95-99.7 rule'),
        ('ID4-area', 'Estimate areas under a normal curve with standardized values and a table or calculator'),
        ('ID4-suit', 'Decide whether a normal model is appropriate for a data set'),
    ]),
    'HSS-ID.B.5': ('Summarize categorical data for two categories in two-way frequency tables. Interpret relative frequencies '
                   'in the context of the data (including joint, marginal, and conditional relative frequencies). Recognize '
                   'possible associations and trends in the data.', [
        ('ID5-joint', 'Summarize two categorical variables in a two-way table and find joint and marginal relative frequencies'),
        ('ID5-cond', 'Find conditional relative frequencies and use them to recognize an association'),
    ]),
    'HSS-ID.B.6': ('Represent data on two quantitative variables on a scatter plot, and describe how the variables are related.', [
        ('ID6-scatter', 'Represent bivariate data on a scatter plot and describe direction, form, strength and unusual points'),
    ]),
    'HSS-ID.B.6.a': ('Fit a function to the data; use functions fitted to data to solve problems in the context of the data. '
                     'Use given functions or choose a function suggested by the context. Emphasize linear, quadratic, and '
                     'exponential models.', [
        ('ID6a-use', 'Use a given linear, quadratic or exponential function fitted to data to solve problems in context'),
        ('ID6a-choose', 'Choose and fit the function family (linear, quadratic or exponential) suggested by the data and context'),
    ]),
    'HSS-ID.B.6.b': ('Informally assess the fit of a function by plotting and analyzing residuals.', [
        ('ID6b-resid', 'Compute residuals, build the residual plot, and judge the fit from its pattern'),
    ]),
    'HSS-ID.B.6.c': ('Fit a linear function for a scatter plot that suggests a linear association.', [
        ('ID6c-line', 'Fit a linear function to a scatter plot that suggests a linear association (least squares with technology)'),
    ]),
    'HSS-ID.C.7': ('Interpret the slope (rate of change) and the intercept (constant term) of a linear model in the context of '
                   'the data.', [
        ('ID7-interpret', 'Interpret the slope and intercept of a linear model in context, with units'),
    ]),
    'HSS-ID.C.8': ('Compute (using technology) and interpret the correlation coefficient of a linear fit.', [
        ('ID8-compute', 'Compute the correlation coefficient of a data set with technology'),
        ('ID8-interpret', 'Interpret the correlation coefficient: direction, strength and the limits of a linear measure'),
    ]),
    'HSS-ID.C.9': ('Distinguish between correlation and causation.', [
        ('ID9-cause', 'Distinguish correlation from causation'),
    ]),
    # ---------------------------------------------------------------- S-IC Making Inferences and Justifying Conclusions
    'HSS-IC.A.1': ('Understand statistics as a process for making inferences about population parameters based on a random '
                   'sample from that population.', [
        ('IC1-infer', 'Identify population, sample, parameter and statistic, and infer from a random sample to its population'),
    ]),
    'HSS-IC.A.2': ('Decide if a specified model is consistent with results from a given data-generating process, e.g., using '
                   'simulation.', [
        ('IC2-run', 'Carry out a simulation of a specified model with random digits'),
        ('IC2-decide', 'Decide whether a specified model is consistent with observed results using simulation evidence'),
    ]),
    'HSS-IC.B.3': ('Recognize the purposes of and differences among sample surveys, experiments, and observational studies; '
                   'explain how randomization relates to each.', [
        ('IC3-types', 'Recognize the purposes of and differences among sample surveys, experiments and observational studies'),
        ('IC3-random', 'Explain how random sampling and random assignment relate to each kind of study'),
    ]),
    'HSS-IC.B.4': ('Use data from a sample survey to estimate a population mean or proportion; develop a margin of error through '
                   'the use of simulation models for random sampling.', [
        ('IC4-prop', 'Estimate a population proportion with a margin of error from simulated sample proportions'),
        ('IC4-mean', 'Estimate a population mean with a margin of error from simulated sample means'),
    ]),
    'HSS-IC.B.5': ('Use data from a randomized experiment to compare two treatments; use simulations to decide if differences '
                   'between parameters are significant.', [
        ('IC5-compare', 'Compare two treatments with a re-randomization simulation and decide whether the difference is significant'),
    ]),
    'HSS-IC.B.6': ('Evaluate reports based on data.', [
        ('IC6-claims', 'Evaluate the conclusions of a report against its study design (causation, generalization, bias)'),
        ('IC6-displays', 'Evaluate the statistics and displays in a report (scales, margins of error, base rates)'),
    ]),
    # ---------------------------------------------------------------- S-CP Conditional Probability and the Rules of Probability
    'HSS-CP.A.1': ('Describe events as subsets of a sample space (the set of outcomes) using characteristics (or categories) of '
                   'the outcomes, or as unions, intersections, or complements of other events ("or," "and," "not").', [
        ('CP1-space', 'Describe a sample space and events as subsets of it'),
        ('CP1-sets', 'Describe events as unions, intersections and complements of other events'),
    ]),
    'HSS-CP.A.2': ('Understand that two events A and B are independent if the probability of A and B occurring together is the '
                   'product of their probabilities, and use this characterization to determine if they are independent.', [
        ('CP2-product', 'Decide whether two events are independent with the product rule P(A and B) = P(A)·P(B)'),
    ]),
    'HSS-CP.A.3': ('Understand the conditional probability of A given B as P(A and B)/P(B), and interpret independence of A and '
                   'B as saying that the conditional probability of A given B is the same as the probability of A, and the '
                   'conditional probability of B given A is the same as the probability of B.', [
        ('CP3-def', 'Compute P(A given B) as P(A and B)/P(B)'),
        ('CP3-indep', 'Interpret independence as P(A given B) = P(A) and P(B given A) = P(B)'),
    ]),
    'HSS-CP.A.4': ('Construct and interpret two-way frequency tables of data when two categories are associated with each object '
                   'being classified. Use the two-way table as a sample space to decide if events are independent and to '
                   'approximate conditional probabilities.', [
        ('CP4-build', 'Construct a two-way frequency table from a description of the data'),
        ('CP4-use', 'Use a two-way table as a sample space to approximate conditional probabilities and judge independence'),
    ]),
    'HSS-CP.A.5': ('Recognize and explain the concepts of conditional probability and independence in everyday language and '
                   'everyday situations.', [
        ('CP5-words', 'Recognize and explain conditional probability and independence in everyday language and situations'),
    ]),
    'HSS-CP.B.6': ('Find the conditional probability of A given B as the fraction of B\'s outcomes that also belong to A, and '
                   'interpret the answer in terms of the model.', [
        ('CP6-fraction', 'Find P(A given B) as the fraction of B\'s outcomes that are in A, and interpret it in the model'),
    ]),
    'HSS-CP.B.7': ('Apply the Addition Rule, P(A or B) = P(A) + P(B) - P(A and B), and interpret the answer in terms of the '
                   'model.', [
        ('CP7-add', 'Apply the Addition Rule with overlap and interpret the result'),
    ]),
    'HSS-CP.B.8': ('(+) Apply the general Multiplication Rule in a uniform probability model, P(A and B) = P(A)P(B|A) = '
                   'P(B)P(A|B), and interpret the answer in terms of the model.', [
        ('CP8-mult', 'Apply the general Multiplication Rule in a uniform model (draws without replacement) and interpret it'),
    ]),
    'HSS-CP.B.9': ('(+) Use permutations and combinations to compute probabilities of compound events and solve problems.', [
        ('CP9-perm', 'Count ordered arrangements with permutations'),
        ('CP9-comb', 'Count unordered selections with combinations'),
        ('CP9-prob', 'Compute probabilities of compound events with permutations and combinations'),
    ]),
    # ---------------------------------------------------------------- S-MD Using Probability to Make Decisions (all (+))
    'HSS-MD.A.1': ('(+) Define a random variable for a quantity of interest by assigning a numerical value to each event in a '
                   'sample space; graph the corresponding probability distribution using the same graphical displays as '
                   'for data distributions.', [
        ('MD1-define', 'Define a random variable on a sample space, find its probability distribution and graph it'),
    ]),
    'HSS-MD.A.2': ('(+) Calculate the expected value of a random variable; interpret it as the mean of the probability '
                   'distribution.', [
        ('MD2-ev', 'Calculate the expected value of a random variable and interpret it as a long-run mean'),
    ]),
    'HSS-MD.A.3': ('(+) Develop a probability distribution for a random variable defined for a sample space in which '
                   'theoretical probabilities can be calculated; find the expected value.', [
        ('MD3-theory', 'Develop a theoretical probability distribution and find its expected value'),
    ]),
    'HSS-MD.A.4': ('(+) Develop a probability distribution for a random variable defined for a sample space in which '
                   'probabilities are assigned empirically; find the expected value.', [
        ('MD4-empirical', 'Develop an empirical probability distribution from data and find its expected value'),
    ]),
    'HSS-MD.B.5.a': ('(+) Weigh the possible outcomes of a decision by assigning probabilities to payoff values and finding '
                     'expected values. a. Find the expected payoff for a game of chance.', [
        ('MD5a-game', 'Find the expected payoff (net of the cost to play) for a game of chance'),
    ]),
    'HSS-MD.B.5.b': ('(+) Weigh the possible outcomes of a decision by assigning probabilities to payoff values and finding '
                     'expected values. b. Evaluate and compare strategies on the basis of expected values.', [
        ('MD5b-compare', 'Evaluate and compare strategies on the basis of expected values'),
    ]),
    'HSS-MD.B.6': ('(+) Use probabilities to make fair decisions (e.g., drawing by lots, using a random number generator).', [
        ('MD6-fair', 'Use probabilities to judge and design fair decision procedures'),
    ]),
    'HSS-MD.B.7': ('(+) Analyze decisions and strategies using probability concepts (e.g., product testing, medical testing, '
                   'pulling a hockey goalie at the end of a game).', [
        ('MD7-testing', 'Analyze decisions based on test results (screening and product testing) with probabilities'),
        ('MD7-strategy', 'Analyze a strategy choice by comparing the probabilities of success it gives'),
    ]),
}


def subskills():
    return [(sid, code, desc) for code, (_, subs) in STANDARDS.items() for sid, desc in subs]
