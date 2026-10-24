"""Algebra II revision 1.1.0: every change since the published 1.0.0 collection, keyed by question ID.

Read by engine/revisions.py during export. Each CHANGES entry is (ID patterns, finding code, status, reason). M01 is the
request that no question need a person or a drawing surface to grade; M02 is an error found while rewriting.
"""
VERSION_FROM = '1.0.0'
COMMIT_FROM = 'e3bf665'

FINDINGS = {
    'M01': 'No question may need a person or a drawing surface to grade: every shown-work item (proofs, derivations, '
           'explanations, divisions; 53) and every drawing item (50 graphs on a blank grid and 5 graphs with a written equation) '
           'is redesigned as multiple choice',
    'M02': 'S42-F1-Q2 asked for a cubic with a positive y-intercept that touches the x-axis at 3 and falls to the right; no '
           'cubic has all of these features (touching at 3 and falling to the right make it negative between -1 and 3). The '
           'condition is now a negative y-intercept.',
}

CHANGES = [
    (['S18-M-Q1', 'S18-M-Q2', 'S18-M-Q3', 'S18-M-Q4', 'S18-M-Q5', 'S18-F1-Q1', 'S18-F1-Q2', 'S42-F1-Q1', 'S42-F1-Q2',
      'S46-M-Q1', 'S46-M-Q2', 'S46-M-Q3', 'S46-M-Q4', 'S46-M-Q5', 'S46-F1-Q1', 'S47-M-Q1', 'S47-M-Q2', 'S47-M-Q3',
      'S47-M-Q4', 'S47-M-Q5', 'S48-M-Q1', 'S48-M-Q2', 'S48-M-Q3', 'S48-M-Q4', 'S48-M-Q5', 'S49-M-Q1', 'S49-M-Q2',
      'S49-M-Q3', 'S49-M-Q4', 'S49-M-Q5', 'S50-M-Q1', 'S50-M-Q2', 'S50-M-Q3', 'S50-M-Q4', 'S50-M-Q5', 'S50-F1-Q1',
      'S51-M-Q1', 'S51-M-Q2', 'S51-M-Q3', 'S51-M-Q4', 'S51-M-Q5', 'S51-F1-Q1', 'S74-M-Q1', 'S74-M-Q2', 'S74-M-Q3',
      'S74-M-Q4', 'S74-M-Q5', 'S74-F1-Q1', 'S75-F1-Q2', 'S78-F1-Q2'],
     'M01', 'revised', 'Drawing item rewritten as "Which graph shows ...?" with four candidate graphs labeled A to D on one '
                       'window; the other graphs show common errors (shift direction, reflection, multiplicity, asymptote, '
                       'period, endpoint circles), named in the grading note.'),
    (['S28-M-Q1', 'S28-M-Q2', 'S28-M-Q3', 'S28-M-Q4', 'S28-M-Q5'],
     'M01', 'revised', 'Write-and-graph item rewritten as multiple choice: four graphs, each titled with an equation; the keyed '
                       'graph has the correct model and its correct graph, the others have a wrong model or a graph that does '
                       'not match its equation.'),
    (['S22-M-Q1', 'S22-M-Q2', 'S22-M-Q3', 'S22-M-Q4', 'S22-M-Q5'],
     'M01', 'revised', 'Shown-work division rewritten as multiple choice; the other choices are the results of common division '
                       'errors (missing zero placeholder, wrong synthetic divisor, sign of the remainder), named in the note.'),
    (['S6-M-Q3', 'S6-M-Q5', 'S6-F2-Q1', 'S11-M-Q1', 'S11-M-Q2', 'S11-M-Q3', 'S11-M-Q4', 'S11-M-Q5', 'S11-F1-Q1',
      'S15-F2-Q1', 'S19-M-Q1', 'S19-M-Q2', 'S19-M-Q3', 'S19-M-Q4', 'S19-M-Q5', 'S19-F1-Q1', 'S19-F1-Q2', 'S19-F2-Q1',
      'S37-M-Q1', 'S37-M-Q2', 'S37-M-Q3', 'S37-M-Q4', 'S37-M-Q5', 'S37-F1-Q1', 'S37-F2-Q1', 'S40-M-Q1', 'S40-M-Q2',
      'S40-M-Q3', 'S40-M-Q4', 'S40-M-Q5', 'S40-F1-Q1', 'S40-F1-Q2', 'S40-F1-Q5', 'S57-F1-Q1', 'S57-F1-Q2',
      'S73-F1-Q1', 'S77-M-Q1', 'S77-M-Q2', 'S77-M-Q3', 'S77-M-Q4', 'S77-M-Q5', 'S81-M-Q1', 'S81-M-Q2', 'S81-F1-Q1',
      'S81-F1-Q2', 'S82-M-Q1', 'S82-M-Q2', 'S82-M-Q3'],
     'M01', 'revised', 'Shown-work proof, derivation, verification, or explanation rewritten as multiple choice: a complete valid '
                       'argument against flawed ones (an example check, an invalid step, assuming the result, a false fact); '
                       'the grading note says what is wrong with each.'),
    (['S42-F1-Q2'], 'M02', 'revised', 'Impossible condition corrected (negative y-intercept).'),
]
