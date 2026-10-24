"""Probability & Statistics revision 1.1.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export, which compares each question with src/history/v1.0.0_records.json (the 1.0.0
snapshot) and stops the build if a question changed without an entry here. Each entry is (IDs, finding code, status,
reason); an ID may appear under several codes, and its change-log reason joins them. R01-R09 are the findings of the
external review of 1.0.0. Question IDs are kept; no question was added or retired, and no unchanged multiple-choice item
changed its letter.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'ca62eb8'

FINDINGS = {
    'R01': 'Answer uniqueness: every item has exactly one correct answer (duplicate correct histogram panels, a tie between strategies, a random-digit count that had more than one defensible answer)',
    'R02': 'Statistical statements and models: claims that summary statistics alone cannot support, causal and sampling wording, and the population a conclusion applies to',
    'R03': 'Simulation decisions: each decision rule states its model, the tail counted and the cutoff',
    'R04': 'Missing local givens and answer-form mismatches: each question restates what it uses, and the asked form matches the key',
    'R05': "Probability models stated bank-wide: fairness, independence, random selection, replacement, guessing and payoffs (applied to every item found by the new check 28, not only the review's examples)",
    'R06': 'Precision and numeric wording: keys written to the stated precision; trailing-zero handling by the game checker documented (check 30)',
    'R07': 'Wording that overstated a claim (absolute statements, interval overlap read as proof)',
    'R08': 'Assessment quality: a MAIN item that only repeated its givens',
    'R09': 'Supplied simulation results labeled as hypothetical',
}

CHANGES = [
    (["S2-M-Q2", "S2-M-Q4", "S52-F1-Q4", "S54-F1-Q3"],
     'R01', 'revised', 'Exactly one correct answer: a second correct histogram panel was replaced with a specific error (S2-M-Q2, S2-M-Q4), the strategy item became a computed comparison with one correct choice (S54-F1-Q3), and the random-digit item states that as many numbers as possible are used and a skipped number means reading the next one (S52-F1-Q4).'),
    (["S6-B3-Q2", "S6-B3-Q4", "S6-F1-Q4", "S6-F2-Q1", "S6-F2-Q2", "S6-F2-Q3", "S9-F2-Q2", "S9-F2-Q3", "S17-B1-Q1", "S21-M-Q5", "S22-B1-Q2", "S26-M-Q3", "S29-B2-Q1", "S31-F2-Q1", "S49-M-Q3", "S49-M-Q4", "S51-M-Q1"],
     'R02', 'revised', 'Statistical statement corrected: overlap judged from standardized gaps or a stated normal model; random assignment "tends to" balance groups; least squares balances residuals, not counts; association versus causation worded exactly; the sample is distinguished from the population; the flaw named is exposure.'),
    (["S21-F2-Q2", "S23-F2-Q2", "S24-M-Q2", "S24-M-Q4", "S24-M-Q5", "S24-F1-Q2", "S24-F2-Q2", "S29-M-Q3", "S29-M-Q5"],
     'R03', 'revised', 'Decision rule now states the model, the tail counted (one-sided or two-sided) and the 5% cutoff in the question itself.'),
    (["S24-B1-Q3", "S24-B1-Q4", "S24-B1-Q5", "S24-F1-Q4", "S33-F1-Q5", "S44-B2-Q1", "S45-B2-Q5", "S45-F2-Q1", "S45-F2-Q2", "S45-F2-Q3", "S45-F2-Q4", "S48-M-Q3", "S52-B1-Q5", "S53-F1-Q1", "S53-F2-Q3", "S53-F2-Q4", "S54-M-Q4", "S54-F1-Q4", "S54-F2-Q1", "S54-F2-Q5"],
     'R04', 'revised', 'Question now restates every given it uses (or drops an instruction the answer format cannot grade), and fraction answers are asked and keyed as fractions (5/4).'),
    (["S23-B1-Q4", "S24-B2-Q2", "S24-B2-Q4", "S32-M-Q1", "S32-M-Q2", "S32-M-Q3", "S32-M-Q4", "S32-B1-Q1", "S32-B1-Q2", "S32-B1-Q4", "S32-F1-Q1", "S32-F1-Q2", "S32-F1-Q3", "S32-F1-Q4", "S32-F1-Q5", "S32-F2-Q1", "S32-F2-Q2", "S32-F2-Q4", "S33-M-Q5", "S33-B1-Q2", "S33-B1-Q4", "S33-B2-Q1", "S33-B2-Q2", "S33-B2-Q4", "S33-F2-Q2", "S34-M-Q4", "S34-B2-Q1", "S34-B2-Q2", "S34-B2-Q3", "S34-B2-Q4", "S34-B2-Q5", "S34-F1-Q1", "S34-F1-Q4", "S35-M-Q3", "S35-B2-Q1", "S35-B2-Q2", "S35-B2-Q3", "S35-B2-Q4", "S35-B2-Q5", "S35-F1-Q1", "S35-F2-Q3", "S36-M-Q4", "S39-F2-Q1", "S39-F2-Q2", "S39-F2-Q5", "S40-M-Q1", "S40-M-Q2", "S40-B1-Q1", "S40-B1-Q2", "S40-B1-Q3", "S40-B1-Q5", "S40-F1-Q1", "S40-F1-Q3", "S40-F1-Q4", "S40-F2-Q1", "S40-F2-Q4", "S41-M-Q2", "S41-M-Q3", "S41-B1-Q1", "S41-B1-Q2", "S41-B1-Q3", "S41-F1-Q3", "S41-F2-Q4", "S42-M-Q1", "S42-M-Q2", "S42-M-Q3", "S42-B3-Q1", "S42-B3-Q3", "S42-F1-Q1", "S42-F1-Q2", "S42-F1-Q4", "S44-F1-Q2", "S44-F1-Q4", "S44-F2-Q2", "S44-F2-Q4", "S45-M-Q4", "S45-B2-Q1", "S45-F1-Q4", "S46-M-Q1", "S46-M-Q2", "S46-M-Q3", "S46-B1-Q1", "S46-B1-Q2", "S46-B1-Q3", "S46-B1-Q4", "S46-B1-Q5", "S46-F1-Q2", "S46-F2-Q1", "S47-M-Q1", "S47-B2-Q3", "S47-F2-Q1", "S47-F2-Q2", "S47-F2-Q4", "S47-F2-Q5", "S48-M-Q1", "S48-M-Q2", "S48-M-Q4", "S48-M-Q5", "S48-B2-Q3", "S48-F1-Q1", "S48-F1-Q2", "S48-F1-Q4", "S48-F1-Q5", "S48-F2-Q1", "S49-F1-Q3", "S49-F2-Q1", "S50-F1-Q1", "S50-F1-Q4", "S50-F2-Q4", "S51-M-Q5", "S51-B2-Q3", "S51-F2-Q1", "S51-F2-Q3", "S51-F2-Q4", "S52-M-Q3", "S52-M-Q4", "S52-M-Q5", "S52-B2-Q1", "S52-B2-Q4", "S52-F1-Q1", "S52-F1-Q2", "S52-F1-Q3", "S53-F2-Q1", "S54-M-Q3", "S54-B1-Q3", "S54-F2-Q3", "S54-F2-Q4"],
     'R05', 'revised', 'Probability model stated in the question: fair devices, independent trials, cards drawn at random from a standard 52-card deck with the replacement rule, the guessing model, the payoff when the event does not happen, equally likely tickets, rolling again until a valid face, or selection without replacement.'),
    (["S5-B2-Q1", "S5-F1-Q3", "S14-F2-Q1", "S20-M-Q2", "S31-M-Q1", "S49-F1-Q1"],
     'R06', 'revised', 'Precision and form: the key is written to the precision the question asks for (2.00, 0.10, 44.10, 2.50), r is given as 0.245, and a two-part distance question asks for both distances.'),
    (["S7-F2-Q3", "S18-F2-Q5", "S27-F2-Q1", "S28-F1-Q5", "S30-B1-Q1", "S31-M-Q3", "S31-B1-Q2"],
     'R07', 'revised', 'Wording narrowed: "usually" less sensitive, the randomized experiment as the design built for cause and effect, the margin of error does not correct bias, both variables vary, the headline claims a reliable population lead, and interval overlap is a cautious reading only.'),
    (["S54-M-Q1"],
     'R08', 'revised', 'MAIN item replaced: it repeated its givens; it now asks for a computation (difference in percentage points and ratio).'),
    (["S21-F2-Q2", "S22-F2-Q4", "S23-B2-Q1", "S24-M-Q3", "S24-M-Q4", "S24-M-Q5", "S24-F2-Q1", "S24-F2-Q2", "S27-M-Q2", "S27-B2-Q2", "S27-F1-Q4", "S28-M-Q2", "S28-M-Q5", "S28-F1-Q2", "S28-F2-Q4", "S29-M-Q2", "S29-M-Q3", "S29-M-Q5", "S29-B1-Q2", "S29-F1-Q1", "S29-F2-Q3"],
     'R09', 'revised', 'Simulation results given in the question are labeled as hypothetical.'),
]
