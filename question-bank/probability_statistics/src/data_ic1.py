"""S-IC.A.1, S-IC.A.2, S-IC.B.3: populations and samples, simulation with random digits, deciding whether a model is
consistent with data, kinds of studies and the role of randomization (sets 22-26).

Every simulation question prints its own random digits (DIGITS below), so its key is fixed: the student carries out the
stated rule on the printed digits. Decisions use a threshold stated in the question."""
from qb import S, B, sa, mc, tf
from common import why, tbl, digits_table
from datasets import D

DIGITS = D('S23 random digits', ['15881399869879730911', '41707536455681518844', '72940557616987168976',
                                 '84697880932081967273', '17784864887663440029', '78753477876804571784',
                                 '72671475136270107981', '93319084520599728379'], 'digits',
           'Eight lines of 20 random digits (generated once and printed, so every simulation key is fixed)')
DT = digits_table(DIGITS)


def makes(line, k=10, hi=6):
    """Successes in the first k digits of a line when digits 0..hi are successes."""
    return sum(1 for ch in DIGITS[line][:k] if int(ch) <= hi)


def pairs(line, below):
    """Two-digit numbers in a line that are below `below` (00..below-1 are successes)."""
    s = DIGITS[line]
    return sum(1 for i in range(0, 20, 2) if int(s[i:i + 2]) < below)


def picks(line, top, k):
    """The first k distinct two-digit labels from 01..top read from a line (and the next lines), skipping others."""
    s = ''.join(DIGITS[line:])
    out = []
    for i in range(0, len(s) - 1, 2):
        v = int(s[i:i + 2])
        if 1 <= v <= top and v not in out:
            out.append(v)
        if len(out) == k:
            return out


M1 = makes(0)
M8 = sum(1 for i in range(8) if makes(i) >= 8)
R2 = pairs(4, 25)
P3 = picks(0, 40, 3)
P3b = picks(2, 60, 3)
E3 = [makes(i, 10, 4) for i in range(8)]  # fair-coin model: 0-4 heads
HEADS = {0: 0, 1: 1, 2: 4, 3: 12, 4: 20, 5: 25, 6: 20, 7: 12, 8: 4, 9: 2, 10: 0}  # 100 simulated sets of 10 fair flips
assert sum(HEADS.values()) == 100
HT = tbl(['Heads in 10 flips'] + [str(k) for k in HEADS], [['Number of simulated trials'] + [str(v) for v in HEADS.values()]])
GIRLS = {0: 3, 1: 12, 2: 19, 3: 13, 4: 3}  # 50 simulated families of 4 children
GT = tbl(['Girls in 4 births', '0', '1', '2', '3', '4'], [['Number of simulated trials'] + [str(v) for v in GIRLS.values()]])
RULE5 = (' Decision rule: if results at least as extreme as the observed result happen in fewer than 5% of the simulated '
         'trials, the model is not consistent with the data; otherwise it is consistent.')


def rule(model, counted):
    """A decision rule that names the model, exactly which simulated results are counted (one tail or both) and the 5%
    cutoff, so the test is fixed before any choice is read."""
    return (' Decision rule: the model is %s. Count the simulated results that are %s. If they make up fewer than 5%% of the '
            'simulated results, the model is not consistent with the data; otherwise it is consistent.' % (model, counted))


def frac_at_least(tab, k):
    return sum(v for x, v in tab.items() if x >= k) / sum(tab.values())


SETS = [
    # ------------------------------------------------------------------ 22. IC.A.1 populations, samples and inference
    S('HSS-IC.A.1', 'Statistics as a process of inference from samples', num=22,
      target='Identify the population, sample, parameter and statistic in a study, and use a statistic from a random sample to '
             'make an inference about the population parameter',
      strand='core', covers=['IC1-infer'],
      main=[
          sa('A random sample of 200 of a school\'s 1,500 students found that 62 bike to school. What is the sample proportion '
             'who bike? Give a decimal.', 'Sample proportion:', key='0.31', note='62/200. This is the statistic.'),
          mc('A random sample of 200 of a school\'s 1,500 students found that 62 bike to school. What is the parameter of interest?', [
              'the proportion of all 1,500 students who bike', 'the 62 sampled students who said they bike',
              'the sample proportion 0.31 from the survey', 'the 200 students who were in the sample'],
             note='A parameter describes the population. 0.31 is the statistic; 62 and 200 are counts or people.'),
          sa('In a random sample of 200 of a school\'s 1,500 students, the proportion who bike is 0.31. Use it to estimate how '
             'many of the 1,500 students bike.', 'Estimate:', key='465', note='0.31 · 1500.'),
          mc('Which sample of a school\'s students allows an inference about all of the students?', [
              'a random sample of 200 students chosen from the school roster', 'the 200 students who chose to answer an online poll',
              'the first 200 students to arrive at school one morning', 'all 200 students who belong to the school bike club'],
             note='Only random selection makes the sample representative. The others are voluntary or convenience samples.'),
          mc('Two random samples of 200 students from the same school give sample proportions 0.31 and 0.27. Why do they differ?', [
              'Sample statistics vary from one random sample to another by chance.',
              'One of the two samples must have been chosen incorrectly.',
              'The population proportion changed between the two samples.',
              'Sample proportions can never be used to estimate a parameter.'],
             note='Sampling variability.'),
      ],
      back=[
          B('Recognize random and representative samples', '7.SP.A.1', [
              tf('A random sample tends to be representative of its population.', key=True, note='Each member has the same chance.'),
              mc('A town wants residents\' opinion on a new park and has a complete list of all residents. Which method gives a random '
                 'sample of residents?', [
                  'pick 100 names by lottery from the complete resident list', 'ask the first 100 people at the park',
                  'post an online survey and use the first replies', 'ask the members of the parks committee'],
                 note='Chance selection from the whole population.'),
              tf('A sample of volunteers who choose to respond is a random sample.', key=False, note='Self-selected.'),
              mc('A survey of shoppers at a sporting-goods store is used to estimate how much all town residents exercise. What is '
                 'the main problem?', ['the sample is not representative', 'the sample is too random', 'the sample is a census',
                                       'the sample has no data'], note='Shoppers there likely exercise more.'),
              tf('The whole group a study wants to learn about is called the population.', key=True, note='Definition.'),
          ], align='exact',
            why=why('the student cannot tell representative samples from biased ones.', 'inference is valid only from random '
                    'samples.', 'identifies random and biased sampling methods.')),
          B('Use a sample to estimate a population count', '7.SP.A.2', [
              sa('In a random sample of 50 students, 12 play an instrument. Estimate how many of 600 students play.', 'Estimate:',
                 key='144', note='12/50 · 600.'),
              sa('In a random sample of 40 light bulbs, 2 are defective. Estimate the number defective in 2,000 bulbs.', 'Estimate:',
                 key='100', note='0.05 · 2000.'),
              tf('If 30% of a random sample prefer pizza, about 30% of the population is estimated to prefer pizza.', key=True,
                 note='The sample proportion estimates the population proportion.'),
              mc('In a random sample of 80 voters, 44 support a measure. What is the estimated percent of all voters who support it?',
                 ['55%', '44%', '80%', '36%'], note='44/80.'),
              tf('Estimates from a random sample are always exactly equal to the population value.', key=False,
                 note='They vary by chance.'),
          ], align='supporting',
            why=why('the student cannot scale a sample result up to the population.', 'that is the inference step.',
                    'estimates population counts from samples.')),
      ],
      f1=B('See how sample size affects sampling variability', 'HSS-IC.A.1', [
          mc('Many random samples of size 25 and many of size 400 are taken from the same population. Which is true?', [
              'Proportions from samples of 400 vary less.', 'Proportions from samples of 25 vary less.',
              'Both sizes vary the same amount.', 'Larger samples are always biased.'], note='Larger n, less variability.'),
          tf('Increasing the size of a random sample reduces bias caused by a poor sampling method.', key=False,
             note='Size reduces variability, not bias.'),
          sa('A random sample of 400 voters has 228 who favor a law. What is the sample proportion? Give a decimal.',
             'Proportion:', key='0.57', note='228/400.'),
          mc('Which estimate of a population proportion is likely to be closest to the true value?', [
              'one from a random sample of 1,000', 'one from a random sample of 50',
              'one from 1,000 volunteers who called in', 'one from 50 friends of the researcher'],
             note='Large and random.'),
          tf('Sample proportions from repeated random samples center around the population proportion.', key=True,
             note='Random sampling is unbiased.'),
      ], prog='same-course deepening', demand='Relate the size and method of a sample to how much its statistic varies.'),
      f2=B('Attach a margin of error to an estimate', 'HSS-IC.B.4', [
          sa('A random sample gives a sample proportion of 0.57 with a margin of error of 0.05. Give the interval of plausible '
             'values for the population proportion.', ['From:', 'To:'], key='0.52; 0.62', note='Form required: both. 0.57 ± 0.05.'),
          mc('A poll reports 48% with a margin of error of 3 percentage points. Which value is plausible for the population '
             'percent?', ['50%', '52%', '44%', '55%'], note='45% to 51%.'),
          tf('A larger random sample usually gives a smaller margin of error.', key=True, note='Less variability.'),
          sa('(Hypothetical simulation results.) Simulated sample proportions have standard deviation 0.025. Using margin of error = 2 × standard deviation, what is '
             'the margin of error?', 'Margin of error:', key='0.05', note='2 · 0.025.'),
          tf('A margin of error accounts for bias from a sample of volunteers.', key=False,
             note='It covers only chance variation in random samples.'),
      ], prog='cross-standard extension', demand='Report an estimate as an interval using a margin of error.',
        builds='Builds on FORWARD 1: the variability of sample statistics is turned into a margin of error.')),

    # ------------------------------------------------------------------ 23. IC.A.2 carry out a simulation
    S('HSS-IC.A.2', 'Simulate a probability model with random digits', num=23,
      target='Carry out a simulation of a specified model by assigning random digits to outcomes and counting results',
      strand='core', covers=['IC2-run'],
      main=[
          sa('A player makes 70% of free throws. To simulate, digits 0-6 mean "make" and 7-9 mean "miss". Use the first 10 digits '
             'of line 1 of the table as 10 shots. How many shots are made?', 'Shots made:', key=str(M1), fig=DT,
             note='Line 1 begins %s; the digits 0-6 among them: %s → %d.' % (DIGITS[0][:10], ', '.join(c for c in DIGITS[0][:10] if int(c) <= 6), M1)),
          sa('A player makes 70% of free throws (digits 0-6 = make, 7-9 = miss). Each line\'s first 10 digits are one trial of '
             '10 shots, giving 8 trials. In how many trials does the player make 8 or more shots?', 'Trials:', key=str(M8),
             fig=DT, note='Makes per line: %s.' % ', '.join(str(makes(i)) for i in range(8))),
          mc('An event has probability 0.4. Which assignment of single random digits simulates it?', [
              '0-3 = success; 4-9 = failure', '0-4 = success; 5-9 = failure', '0-3 and 9 = success; 4-8 = failure',
              '4 = success; all other digits = failure'],
             note='4 of 10 equally likely digits. The others give 0.5, 0.5 and 0.1.'),
          sa('A spinner lands on red with probability 0.25. Read line 5 of the table as ten two-digit numbers; 00-24 means red. '
             'How many of the ten spins are red?', 'Red spins:', key=str(R2), fig=DT,
             note='Line 5 pairs: %s.' % ', '.join(DIGITS[4][i:i + 2] for i in range(0, 20, 2))),
          sa('A simulation of 50 families of 4 children (each birth a girl with probability 0.5) gave the results in the table. '
             'What proportion of the simulated families had 3 or more girls? Give a decimal.', 'Proportion:',
             key='%g' % frac_at_least(GIRLS, 3), fig=GT, note='(13 + 3)/50.'),
      ],
      back=[
          B('Design a simulation for a compound event', '7.SP.C.8.c', [
              mc('To simulate a fair coin with random digits, which assignment works?', [
                  'even digits = heads; odd digits = tails', '0-6 = heads; 7-9 = tails', '0 = heads; 1-9 = tails',
                  '0-4 = heads; 4-9 = tails'], note='Even and odd digits split 5 and 5. 0-4 and 4-9 overlap at 4; 0 alone gives 0.1; 0-6 gives 0.7.'),
              sa('In the digits 4 1 7 0 7 5 3 6 4 5, digits 0-4 mean heads. How many heads?', 'Heads:', key='5',
                 note='4, 1, 0, 3, 4.'),
              tf('A trial of a simulation for "number of heads in 10 flips" uses 10 random digits.', key=True,
                 note='One digit per flip.'),
              mc('To simulate rolling a fair six-sided die with digits, what should be done with 0, 7, 8 and 9?', [
                  'skip them and read the next digit', 'count them as a 6', 'count them as a 1', 'stop the simulation'],
                 note='Only 1-6 are used, so each face stays equally likely.'),
              tf('Running more trials of a simulation makes the estimated probability less reliable.', key=False,
                 note='More trials, more reliable.'),
          ], align='exact',
            why=why('the student cannot set up a simulation for a chance process.', 'the standard asks for one.',
                    'assigns digits and defines a trial.')),
          B('Find a probability as a relative frequency', '7.SP.C.6', [
              sa('(Hypothetical simulation results.) In 50 simulated trials, an event happened 16 times. What is its relative frequency? Give a decimal.', 'Answer:',
                 key='0.32', note='16/50.'),
              sa('An event happened in 9 of 200 trials. What is its relative frequency as a percent?', 'Percent:', key='4.5%',
                 note='9/200.'),
              tf('A relative frequency of 0.32 means the event happened in 32% of the trials.', key=True, note='Decimal to percent.'),
              mc('An event happened in 12 of 60 trials. What is its relative frequency?', ['0.2', '0.12', '0.6', '5'],
                 note='12/60.'),
              tf('The relative frequency from 10 trials is always exactly equal to the true probability.', key=False,
                 note='It varies, especially in few trials.'),
          ], align='supporting',
            why=why('the student cannot turn a count of trials into a probability estimate.', 'simulation results are read '
                    'that way.', 'computes relative frequencies.')),
      ],
      f1=B('Use two-digit groups for probabilities in hundredths', 'HSS-IC.A.2', [
          mc('An event has probability 0.35. Which assignment of two-digit numbers simulates it?', [
              '00-34 = success; 35-99 = failure', '00-35 = success; 36-99 = failure', '01-34 = success; others = failure',
              '35 = success; others = failure'],
             note='00-34 is 35 of the 100 numbers. 00-35 has 36; 01-34 has 34; 35 alone has probability 0.01.'),
          sa('Read line 3 as ten two-digit numbers; 00-34 means success. How many successes?', 'Successes:',
             key=str(pairs(2, 35)), fig=DT, note='Line 3 pairs: %s.' % ', '.join(DIGITS[2][i:i + 2] for i in range(0, 20, 2))),
          tf('Two-digit groups 00-99 give 100 equally likely outcomes.', key=True, note='Each has probability 0.01.'),
          sa('A fair coin model uses 0-4 = heads. Using the first 10 digits of each of the 8 lines as 8 trials of 10 flips, in how '
             'many trials are there 3 or fewer heads?', 'Trials:', key=str(sum(1 for v in E3 if v <= 3)), fig=DT,
             note='Heads per line: %s.' % ', '.join(map(str, E3))),
          tf('To simulate a probability of 1/3 with single digits, use 1-3 = success, 4-9 = failure and skip 0.', key=True,
             note='3 of 9 used digits.'),
      ], prog='same-course deepening', demand='Simulate models whose probabilities need two-digit groups or skipped digits.'),
      f2=B('Use simulation results to judge a model', 'HSS-IC.A.2', [
          sa('In 100 simulated sets of 10 fair-coin flips (table), in what proportion of the sets were there 9 or more heads? Give '
             'a decimal.', 'Proportion:', key='0.02', fig=HT, note='2/100.'),
          mc('A coin claimed to be fair gave 9 heads in 10 flips. Use the table of 100 simulated sets.%s Which decision is '
             'correct?' % rule('a fair coin', '9 or more heads (a one-sided check: only an excess of heads counts against the '
                                  'model)'), [
              'Not consistent: 9 or more heads happened in only 2% of the trials.',
              'Consistent: 9 or more heads happened in 2% of the trials.',
              'Consistent: a fair coin can land heads 9 times.',
              'Not consistent: a fair coin must give exactly 5 heads.'],
             fig=HT, note='2% < 5%.'),
          tf('A result that happens in 25% of the simulated trials is consistent with the model under the 5% rule.', key=True,
             note='25% ≥ 5%.'),
          sa('In the table of 100 simulated sets, in what proportion were there 7 or more heads? Give a decimal.', 'Proportion:',
             key='0.18', fig=HT, note='(12 + 4 + 2)/100.'),
          tf('If a model is consistent with the data, the simulation proves that the model is true.', key=False,
             note='It only fails to rule the model out.'),
      ], prog='same-course deepening', demand='Read a distribution of simulated results to decide about a model.',
        builds='Builds on FORWARD 1: the simulations the student can now run are summarized and compared with data.')),
]

assert P3 == [15, 13, 9] and P3b == [5, 57, 16]
assert abs(frac_at_least(HEADS, 8) - 0.06) < 1e-12

SETS += [
    # ------------------------------------------------------------------ 24. IC.A.2 decide whether a model is consistent
    S('HSS-IC.A.2', 'Decide whether a model is consistent with data', num=24,
      target='Decide whether a specified model is consistent with results from a data-generating process, using the '
             'proportion of simulated results at least as extreme as the observed result and a stated threshold',
      strand='core', covers=['IC2-decide'],
      main=[
          sa('The table shows 100 simulated sets of 10 fair-coin flips. In what proportion of the sets were there 8 or more heads? '
             'Give a decimal.', 'Proportion:', key='0.06', fig=HT, note='(4 + 2 + 0)/100.'),
          mc('A coin claimed to be fair gave 8 heads in 10 flips. Use the table of 100 simulated sets.%s Which decision is '
             'correct?' % rule('a fair coin', '8 or more heads (a one-sided check: only an excess of heads counts against the '
                               'model)'), [
              'Consistent: 8 or more heads happened in 6% of the simulated sets.',
              'Not consistent: 8 or more heads happened in only 6% of the sets.',
              'Not consistent: a fair coin should give 5 heads every time.',
              'Consistent: 8 heads happened in exactly 4% of the sets.'],
             fig=HT, note='6% is not fewer than 5%. The others misapply the rule, expect exactly 5 heads, or use "exactly 8" (4%) instead of "8 or more".'),
          sa('(Hypothetical simulation results.) A die is claimed to be fair. In 60 rolls it showed 18 sixes. In 200 simulated sets of 60 fair rolls, 18 or more sixes '
             'happened 4 times. What proportion of the simulated sets is that? Give a decimal.', 'Proportion:', key='0.02',
             note='4/200.'),
          mc('(Hypothetical simulation results.) A die claimed to be fair showed 18 sixes in 60 rolls. In 200 simulated sets of 60 fair rolls, 18 or more sixes '
             'happened 4 times.%s Which decision is correct?' % rule('a fair die', '18 or more sixes (a one-sided check: only an excess of '
                                                                 'sixes counts against the model)'), [
              'Not consistent: so many sixes happened in only 2% of simulated sets.',
              'Consistent: 18 sixes is possible with a fair die.',
              'Consistent: 4 simulated sets had 18 or more sixes.',
              'Not consistent: a fair die must give exactly 10 sixes.'],
             note='2% < 5%. Possible is not the test; the proportion is.'),
          mc('(Hypothetical simulation results.) A spinner is claimed to land on red 25%% of the time. In 40 spins it landed on red 6 times. In 1,000 simulated sets '
             'of 40 spins, 6 or fewer reds happened 120 times.%s Which decision is correct?' % rule(
                 'a spinner that lands on red 25% of the time', '6 or fewer reds (a one-sided check: only too few reds counts '
                 'against the model)'), [
              'Consistent: 6 or fewer reds happened in 12% of the sets.',
              'Not consistent: 6 is fewer than the expected 10 reds.',
              'Not consistent: only 120 of the sets had 6 or fewer.',
              'Consistent: the spinner landed on red exactly 25% of the time.'],
             note='120/1000 = 12% ≥ 5%. 6/40 = 15%, not 25%.'),
      ],
      back=[
          B('Read the results of a simulation', 'HSS-IC.A.2', [
              sa('In the table of 50 simulated families of 4 children, how many families had exactly 2 girls?', 'Families:',
                 key='19', fig=GT, note='Read the table.'),
              sa('In the table of 50 simulated families, what proportion had 1 or fewer girls? Give a decimal.', 'Proportion:',
                 key='0.3', fig=GT, note='(3 + 12)/50.'),
              tf('The table of 100 simulated sets of 10 fair-coin flips shows 25 sets with exactly 5 heads.', key=True, fig=HT, note='Read it.'),
              mc('In the table of 100 simulated sets of 10 fair-coin flips, how many sets had 3 or fewer heads?', ['17', '12', '5', '29'], fig=HT,
                 note='0 + 1 + 4 + 12.'),
              tf('In the table of 100 simulated sets of 10 fair-coin flips, more sets had 6 heads than 4 heads.', key=False, fig=HT,
                 note='20 each.'),
          ], align='exact',
            why=why('the student cannot read counts and proportions from simulation output.', 'the decision uses them.',
                    'reads simulation tables.')),
          B('Compare observed frequencies with a probability model', '7.SP.C.7.b', [
              tf('A coin that lands heads 520 times in 1,000 flips is reasonably consistent with a fair coin.', key=True,
                 note='52% is close to 50%.'),
              mc('A fair die is rolled 600 times, independently. About how many sixes does the fair model predict?', ['100', '160', '60', '600'],
                 note='600/6.'),
              sa('How many heads does a fair-coin model predict on average in 10 flips?', 'Heads:', key='5', note='10 · 0.5.'),
              tf('A fair die rolled 60 times, independently, must show each face exactly 10 times.', key=False, note='Results vary by chance.'),
              mc('A spinner is claimed to land on red 50% of the time. Which result in 100 spins most suggests the claim is wrong?',
                 ['82 red', '53 red', '47 red', '50 red'], note='Farthest from 50.'),
          ], align='supporting',
            why=why('the student expects data to match a model exactly, or ignores large gaps.', 'deciding needs a sense of '
                    'ordinary chance variation.', 'compares observed and expected frequencies.')),
      ],
      f1=B('Decide using results extreme in either direction', 'HSS-IC.A.2', [
          sa('In the table of 100 simulated sets of 10 fair flips, what proportion had 9 or more heads or 1 or fewer heads? Give a '
             'decimal.', 'Proportion:', key='0.03', fig=HT, note='(2 + 0) + (0 + 1) = 3.'),
          mc('A coin claimed to be fair gave 1 head in 10 flips. Use the table of 100 simulated sets of 10 fair-coin '
             'flips; results at least as far from 5 heads as 1 head are in either tail.%s Which decision is correct?' % rule(
                 'a fair coin', '9 or more heads or 1 or fewer heads (a two-sided check: too many or too few heads both count)'), [
              'Not consistent: such results happened in 3% of the sets.', 'Consistent: such results happened in 3% of the sets.',
              'Consistent: 1 head happened in exactly 1 set.', 'Not consistent: a fair coin cannot give 1 head.'],
             fig=HT, note='3% < 5%.', cols=2),
          tf('Under the 5% rule, the smaller the proportion of simulated results as extreme as the data, the stronger the evidence '
             'against the model.', key=True, note='Rarer under the model means stronger evidence.'),
          sa('A coin claimed to be fair gave 7 heads in 10 flips. In the table, what proportion of sets are at least as far from 5 heads in either '
             'direction (7 or more, or 3 or fewer)? Give a decimal.', 'Proportion:', key='0.35', fig=HT,
             note='(12 + 4 + 2) + (12 + 4 + 1) = 35.'),
          tf('If a model is judged not consistent under the 5% rule, there is no chance that the model is true.', key=False,
             note='Rare results can still happen.'),
      ], prog='same-course deepening', demand='Count results extreme in both directions and decide.'),
      f2=B('Judge a treatment difference by re-randomization', 'HSS-IC.B.5', [
          sa('(Hypothetical simulation results.) In 100 re-randomizations of an experiment\'s results, a difference in means of 6 or more appeared 3 times. What '
             'proportion is that? Give a decimal.', 'Proportion:', key='0.03', note='3/100.'),
          mc('(Hypothetical simulation results.) In a randomized experiment, the treatment group\'s mean minus the control group\'s mean was 6. In 100 re-randomizations '
             'of the results, differences (treatment minus control) of 6 or more appeared 3 times.%s Which decision is correct?' % rule(
                 'the "no effect" model (the treatment does not change the results)', 'differences of 6 or more (a one-sided '
                 'check)').replace('the model is not consistent', 'the "no effect" model is not consistent').replace(
                 'otherwise it is consistent', 'otherwise it is consistent, and the difference is not significant').replace(
                 'with the data;', 'with the data and the difference is significant;'), [
              'The difference is significant: chance alone gave it 3% of the time.',
              'The difference is not significant: it appeared 3 times.',
              'The difference is not significant: re-randomizing changes the data.',
              'The difference is significant: every difference is significant.'],
             note='3% < 5%.'),
          tf('A re-randomization simulation assumes that the treatment has no effect.', key=True,
             note='It reshuffles the responses as if labels did not matter.'),
          sa('In an experiment, the treatment group\'s mean was 24 and the control group\'s mean was 19. What is the difference '
             '(treatment minus control)?', 'Difference:', key='5', note='24 - 19.'),
          tf('If the observed difference appeared in 40% of re-randomizations, the treatment effect is significant under the '
             '5% rule.', key=False, note='40% ≥ 5%: not significant.'),
      ], prog='cross-standard extension', demand='Apply the same consistency reasoning to a difference between treatments.',
        builds='Builds on FORWARD 1: the "is it rare under the model?" decision is applied to an experiment.')),

    # ------------------------------------------------------------------ 25. IC.B.3 kinds of studies
    S('HSS-IC.B.3', 'Sample surveys, experiments and observational studies', num=25,
      target='Recognize the purposes of and differences among sample surveys, experiments and observational studies',
      strand='core', covers=['IC3-types'],
      main=[
          mc('A researcher randomly assigns 60 volunteers to a new sleep routine or their usual routine and compares their test '
             'scores. What kind of study is this?', ['experiment', 'sample survey', 'observational study', 'census'],
             note='Treatments are imposed and assigned.'),
          mc('A polling company asks a random sample of 1,000 adults which candidate they prefer. What kind of study is this?', [
              'sample survey', 'experiment', 'observational study comparing groups', 'simulation'],
             note='It estimates a population characteristic by asking a sample.'),
          mc('Researchers compare lung health of people who already smoke with people who do not. What kind of study is this?', [
              'observational study', 'experiment', 'sample survey of opinions', 'census'],
             note='Groups form on their own; nothing is imposed.'),
          mc('Which kind of study is designed mainly to estimate a characteristic of a population?', [
              'a sample survey', 'an experiment', 'an observational study of two groups', 'a simulation of a model'],
             note='Surveys estimate; experiments test treatments.'),
          mc('Why can an experiment support a cause-and-effect conclusion when an observational study cannot?', [
              'The researcher imposes treatments, so other variables can be controlled.',
              'Experiments always use more subjects than observational studies.',
              'Observational studies never collect any numerical data.',
              'Experiments do not need any comparison or control group.'],
             note='Imposed, randomly assigned treatments control lurking variables. The others are false claims about data, sizes '
                  'or control groups.'),
      ],
      back=[
          B('Identify the population, sample, parameter and statistic', 'HSS-IC.A.1', [
              mc('300 randomly chosen city residents are asked how often they ride the bus. What is the population?', [
                  'all city residents', 'the 300 residents', 'bus riders only', 'the city\'s buses'], note='The whole group.'),
              sa('300 randomly chosen city residents are asked how often they ride the bus. What is the sample size?', 'Size:',
                 key='300', note='Count of people asked.'),
              tf('A statistic describes a sample.', key=True, note='Definition.'),
              tf('A census collects data from only part of the population.', key=False, note='A census uses everyone.'),
              mc('Which is a parameter?', [
                  'the mean height of all students in a state', 'the mean height of 50 sampled students', 'the number 50',
                  'the proportion in the sample'], note='Describes the population.'),
          ], align='exact',
            why=why('the student cannot name the parts of a statistical study.', 'study types differ in those parts.',
                    'identifies population, sample, parameter and statistic.')),
          B('Separate association from causation', 'HSS-ID.C.9', [
              tf('An association seen without assigning treatments may be caused by a lurking variable.', key=True,
                 note='Observational data.'),
              mc('Towns with more ice-cream shops have more drownings. What is a likely lurking variable?', [
                  'hot weather', 'the number of shops', 'the town\'s name', 'the price of ice cream'], note='Affects both.'),
              tf('A correlation always implies causation when the study is large.', key=False, note='Size does not change it.'),
              mc('Which conclusion requires an experiment?', [
                  'A vitamin causes faster recovery.', 'Recovery time and vitamin use are associated.',
                  'Half of the patients took the vitamin.', 'The mean recovery time was 6 days.'], note='A causal claim.'),
              tf('Random assignment helps rule out lurking variables.', key=True, note='It balances them.'),
          ], align='exact',
            why=why('the student does not see why study type limits conclusions.', 'that is the purpose of experiments.',
                    'separates association from cause.')),
      ],
      f1=B('Identify the parts of an experiment', 'HSS-IC.B.3', [
          mc('An experiment compares two fertilizers on 40 plots and measures crop yield. What is the response variable?', [
              'crop yield', 'the two fertilizers', 'the 40 plots', 'the farmer'], note='What is measured.'),
          sa('An experiment tests 3 doses of a medicine and a placebo. How many treatments are there?', 'Treatments:', key='4',
             note='3 + 1.'),
          tf('A control group receives the standard treatment or a placebo so the new treatment can be compared.', key=True,
             note='Purpose of control.'),
          mc('Why do experiments on medicines often give some subjects a placebo?', [
              'to account for the effect of believing one is being treated', 'to make the experiment cheaper to run',
              'to increase the number of different treatments', 'to make sure the results come out positive'], note='Placebo effect. The others are false: a placebo does not lower cost, add treatments, or fix the outcome.'),
          tf('In a double-blind experiment, only the subjects do not know which treatment they receive.', key=False,
             note='The people who evaluate them do not know either.'),
      ], prog='same-course deepening', demand='Name treatments, units, response, control and blinding in an experiment.'),
      f2=B('Choose a study design for a question', 'HSS-IC.B.3', [
          mc('Question: does a new math app raise test scores? Which design fits best?', [
              'a randomized experiment', 'a sample survey', 'an observational study of app users', 'a census of all students'],
             note='Cause needs an experiment.'),
          mc('Question: what percent of a town\'s residents own a bicycle? Which design fits best?', [
              'a sample survey', 'a randomized experiment', 'an observational study of cyclists', 'a simulation'],
             note='Estimate a population percent.'),
          mc('Question: do people who live near highways have more asthma? Assigning where people live is not possible. Which '
             'design fits best?', ['an observational study', 'a randomized experiment', 'a sample survey of opinions', 'a simulation'],
             note='Treatment cannot be assigned.'),
          tf('It is ethical to randomly assign people to smoke in an experiment on lung disease.', key=False,
             note='It would cause harm.'),
          tf('An observational study can be the best choice when assigning a treatment would be unethical.', key=True,
             note='Then observation is what is possible.'),
      ], prog='same-course deepening', demand='Match a research question to the study design that can answer it.',
        builds='Builds on FORWARD 1: knowing the parts of an experiment, the student decides when one is needed and possible.')),

    # ------------------------------------------------------------------ 26. IC.B.3 randomization
    S('HSS-IC.B.3', 'How randomization relates to each kind of study', num=26,
      target='Explain how randomization relates to sample surveys (random sampling) and experiments (random assignment), and '
             'what each allows a study to conclude',
      strand='core', covers=['IC3-random'],
      main=[
          sa('A class has 40 students numbered 01 to 40. Read line 1 of the table as two-digit numbers, skipping 00, numbers above '
             '40 and repeats. Which three students are chosen first?', ['First:', 'Second:', 'Third:'],
             key='; '.join(map(str, P3)), fig=DT, note='Form required: all three, in order. Line 1: 15, 88, 13, 99, 86, 98, 79, 73, '
                                                       '09 → 15, 13, 9.'),
          mc('What is the main purpose of selecting a sample at random in a survey?', [
              'so the results can be generalized to the population', 'so a treatment can be shown to cause a change',
              'so that every answer comes out the same', 'so the sample is as small as possible'],
             note='Random sampling supports generalization. The others describe random assignment (cause), or claim it makes answers '
                  'identical or the sample small.'),
          mc('What is the main purpose of assigning subjects to treatments at random in an experiment?', [
              'to help balance other variables between the groups', 'to let the results describe everyone in the country',
              'to guarantee that the treatment will work', 'to avoid needing any control or comparison group'],
             note='Random assignment tends to balance other variables, so a difference larger than chance variation can be credited to '
                  'the treatment; it does not guarantee identical groups. The others describe random sampling (generalization) or '
                  'claim it guarantees success or replaces a control group.'),
          mc('A study randomly assigned 80 volunteers to two diets and found a significant difference in weight loss. The '
             'volunteers were not a random sample. What can be concluded?', [
              'The diet caused the difference for volunteers like these.',
              'The diet causes the same difference for everyone in the country.',
              'Nothing, because the subjects were volunteers.',
              'Only that the two diets are associated with weight.'],
             note='Random assignment gives cause; no random sample, so no broad generalization. The others generalize to the '
                  'country, ignore the random assignment, or claim only association.'),
          sa('Plots in a field are numbered 01 to 60. Read line 3 of the table as two-digit numbers, skipping 00, numbers above 60 '
             'and repeats. Which three plots are assigned fertilizer A first?', ['First:', 'Second:', 'Third:'],
             key='; '.join(map(str, P3b)), fig=DT,
             note='Form required: all three, in order. Line 3: 72, 94, 05, 57, 61, 69, 87, 16 → 5, 57, 16.'),
      ],
      back=[
          B('Classify a study', 'HSS-IC.B.3', [
              mc('A teacher asks a random sample of 50 students how many hours they sleep. What kind of study is this?', [
                  'sample survey', 'experiment', 'observational study comparing treatments', 'census'], note='Asking a sample.'),
              tf('In an experiment, the researcher decides which subjects get which treatment.', key=True, note='Imposed.'),
              mc('Doctors compare the heart health of people who already jog with people who do not. What kind of study is this?', [
                  'observational study', 'experiment', 'sample survey', 'simulation'], note='Nothing imposed.'),
              tf('A sample survey assigns treatments to people.', key=False, note='It asks or measures only.'),
              mc('Which study imposes a treatment?', [
                  'giving half of the volunteers a new drug, chosen by lottery', 'asking a random sample of voters for their opinion',
                  'recording the diets that people already choose to eat', 'counting the cars that pass along a busy road'], note='Assignment by chance.'),
          ], align='exact',
            why=why('the student cannot tell the three kinds of study apart.', 'each uses randomization differently.',
                    'classifies studies.')),
          B('Select a simple random sample', '7.SP.A.1', [
              tf('In a simple random sample, every group of the same size has the same chance of being chosen.', key=True,
                 note='Definition.'),
              mc('Which method gives a simple random sample of 5 students from a class of 30?', [
                  'draw 5 names from a hat holding all 30 names', 'choose the 5 tallest students in the class',
                  'choose the first 5 students to arrive', 'ask for 5 volunteers to raise their hands'], note='Chance selection.'),
              sa('Students are numbered 01 to 30. Reading the two-digit numbers 45 07 29 07 33 18, skipping numbers above 30 and '
                 'repeats, which three students are chosen?', ['First:', 'Second:', 'Third:'], key='7; 29; 18',
                 note='Form required: all three, in order.'),
              tf('Choosing every student whose name starts with A is a random sample.', key=False, note='Not chance-based.'),
              mc('Why are repeated numbers skipped when selecting a sample from a random-digit table?', [
                  'a person cannot be chosen twice', 'repeated digits are always printing errors', 'repeated numbers are too large to use',
                  'skipping them saves time in the selection'],
                 note='Sampling without replacement. The others are false reasons: repeats are valid digits of the right size.'),
          ], align='supporting',
            why=why('the student cannot carry out random selection.', 'random sampling and assignment use it.',
                    'selects a random sample with a table.')),
      ],
      f1=B('Decide the scope of conclusions', 'HSS-IC.B.3', [
          mc('A study used a random sample from a population but no random assignment. What can be concluded?', [
              'Associations generalize to the population, but not cause.',
              'Cause can be concluded for the whole population.',
              'Cause can be concluded, but only for the sample.',
              'Nothing at all can be concluded from such a study.'],
             note='Random sampling → generalize; no random assignment → no cause.'),
          mc('A study used both a random sample from a population and random assignment to treatments. What can be concluded?', [
              'Cause, generalized to the population.', 'Cause, but only for the sample.', 'Association only.', 'Nothing.'],
             note='Both kinds of randomization.'),
          tf('Random assignment allows cause-and-effect conclusions.', key=True, note='Its purpose.'),
          tf('Random sampling allows cause-and-effect conclusions even without random assignment.', key=False,
             note='It allows generalization only.'),
          mc('A study used neither random sampling nor random assignment. What can be concluded?', [
              'Associations in the group studied only.', 'Cause for the population.', 'Cause for the group studied.',
              'Associations for the population.'], note='No randomization of either kind.'),
      ], prog='same-course deepening', demand='Use the kind of randomization to state what a study can conclude.'),
      f2=B('Evaluate a report\'s conclusion from its design', 'HSS-IC.B.6', [
          mc('A news report says, "People who drink green tea live longer, so drink tea to live longer." The data came from an '
             'observational study. What is the main flaw?', [
              'It claims cause from an observational study.', 'The sample was too large to be trusted.',
              'Green tea intake cannot be measured at all.', 'Observational studies cannot find associations.'],
             note='Cause needs random assignment.'),
          tf('A report based on a voluntary online poll can be generalized to all adults.', key=False,
             note='Volunteers are not a random sample.'),
          mc('A randomized experiment on 200 college athletes found a new drink improved sprint times. To whom does the result '
             'apply most directly?', ['college athletes like those studied', 'all adults', 'all children', 'nobody'],
             note='The subjects define the scope.'),
          tf('A report should state how its sample was chosen and whether treatments were randomly assigned.', key=True,
             note='Needed to judge the conclusion.'),
          mc('A survey of 50 gym members found 90% exercise daily, reported as "90% of Americans exercise daily." What is wrong?', [
              'Gym members are not representative of all Americans.', 'The sample of 50 people is far too large.',
              'Surveys can never be used to estimate percents.', 'The percent of 90 was computed incorrectly.'],
             note='Biased sample.'),
      ], prog='cross-standard extension', demand='Apply the scope-of-conclusion rules to reports in the media.',
        builds='Builds on FORWARD 1: the scope rules are now used to check real-style claims.')),
]
