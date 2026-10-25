"""Logic course plan: the ordered list of focused sets, their local outcomes, kind (puzzle-driven or formal), genre,
supporting Mathematical Practices, any directly applicable content standard, and the reference-deck genres that
inspired them (author-only source map: inspiration of a reasoning genre, never a copied question).

Deck page numbers refer to the PDF exports "Game Show N REFERENCE for Logic.pdf" (62 pages each). Question k of a deck
is on page 3 + 4(k - 1) and its answer on page 5 + 4(k - 1).
"""

# Mathematical Practices (Common Core State Standards for Mathematics, Standards for Mathematical Practice)
PRACTICES = {
    'MP1': 'Make sense of problems and persevere in solving them',
    'MP2': 'Reason abstractly and quantitatively',
    'MP3': 'Construct viable arguments and critique the reasoning of others',
    'MP6': 'Attend to precision',
    'MP7': 'Look for and make use of structure',
    'MP8': 'Look for and express regularity in repeated reasoning',
}

# Content standards cited as direct alignments (wording as stored in this repository's Algebra I and Geometry sources).
STANDARDS = {
    'HSA-REI.A.1': 'Explain each step in solving a simple equation as following from the equality of numbers asserted at '
                   'the previous step, starting from the assumption that the original equation has a solution. Construct '
                   'a viable argument to justify a solution method.',
    'HSG-CO.C.9': 'Prove theorems about lines and angles. Theorems include: vertical angles are congruent; when a '
                  'transversal crosses parallel lines, alternate interior angles are congruent and corresponding angles '
                  'are congruent; points on a perpendicular bisector of a line segment are exactly those equidistant from '
                  'the segment\'s endpoints.',
}

# Not used as inspiration, on purpose: deck 1 Q8 (meaning depends on spoken stress, an accent-dependent cue) and
# deck 1 Q11 (depends on knowing song lyrics). Both rely on knowledge outside the stated problem.
NOT_USED = {(1, 8): 'depends on spoken stress (pronunciation)', (1, 11): 'depends on knowing song lyrics'}

# Reference decks: (deck, question number) -> short description of the reasoning genre shown
DECK = {
    (1, 1): 'reflection must match the object', (1, 2): 'word lengths grow by one letter', (1, 3): 'a word read as a name',
    (1, 4): 'one feature inverted in an upside-down photo', (1, 5): 'odd/even petal count (parity)',
    (1, 6): 'swapping parts of names', (1, 7): 'grid with no letter next to itself (local impossibility)',
    (1, 8): 'stress changes meaning', (1, 9): 'picture alphabet position', (1, 10): 'letters of number words in alphabetical order',
    (1, 11): 'words that occur once in a song', (1, 12): 'letter count equals position', (1, 13): 'map regions labeled with neighbor counts',
    (1, 14): 'digits that read the same upside down', (1, 15): 'palindrome from smudged keys',
    (2, 1): 'distinct letters of a phrase', (2, 2): 'stack seen from above (occlusion)', (2, 3): 'sign read in reverse',
    (2, 4): 'adding letters to a word', (2, 5): 'joining two word parts', (2, 6): 'order of stacked postcards',
    (2, 7): 'anagram of a whole phrase', (2, 8): 'rotating symbols', (2, 9): 'interleaving letters', (2, 10): 'units (pairs vs items)',
    (2, 11): 'double negation', (2, 12): 'word ladder', (2, 13): 'count of closed loops in digits (symbol code)',
    (2, 14): 'first letters of words', (2, 15): 'longest word from repeated letters',
    (3, 1): 'matching a precise description', (3, 2): 'tracing tangled routes', (3, 3): 'moving and swapping tokens',
    (3, 4): 'rebus with picture code', (3, 5): 'names hidden backward', (3, 6): 'family relations (one sister shared)',
    (3, 7): 'cube net', (3, 8): 'letter values (repeated letters count twice)', (3, 9): 'one feature inconsistent with the rules',
    (3, 10): 'pieces that complete a rectangle (tiling)', (3, 11): 'partly hidden letters', (3, 12): 'counting under a precise definition',
    (3, 13): 'word square', (3, 14): 'largest digit sum on a clock (optimization)', (3, 15): 'month from neighbor-month clues (elimination)',
}

P, F = 'puzzle', 'formal'
# set number: (title, outcome id, outcome title, kind, genre, family, practices, standard or None, deck refs)
SETS = {
    1: ('Mirror reflections: what a reflection must show', 'LOGIC.SPATIAL.01', 'Decide whether an image is consistent with a reflection in a horizontal or vertical mirror line', P, 'reflection and symmetry', 'visual', ['MP7', 'MP6'], None, [(1, 1), (1, 4), (1, 14)]),
    2: ('Read exactly what is stated', 'LOGIC.READING.01', 'Read negations, double negations, units and relationships exactly as stated', P, 'precise reading', 'verbal', ['MP6', 'MP1'], None, [(2, 11), (2, 10), (3, 6), (1, 3), (3, 12), (3, 1), (3, 9)]),
    3: ('Statements, premises and conclusions', 'LOGIC.ARGUMENT.01', 'Identify statements, premises, conclusions and unstated assumptions in an argument', F, 'formal logic', 'formal', ['MP3'], None, []),
    4: ('Eliminate candidates clue by clue', 'LOGIC.CONSTRAINT.01', 'Find the only candidate left after applying every clue to a finite list', P, 'elimination', 'constraint', ['MP1', 'MP6'], None, [(3, 15), (1, 12)]),
    5: ('Negation and truth values', 'LOGIC.CONNECTIVE.01', 'Form the negation of a statement and find truth values of simple statements', F, 'formal logic', 'formal', ['MP6', 'MP3'], None, [(2, 11)]),
    6: ('Crack a code with a stated key', 'LOGIC.CODE.01', 'Decode and encode with a stated symbol or value key, and infer a key from examples within a stated family', P, 'symbol codes', 'symbolic', ['MP7', 'MP2'], None, [(2, 13), (3, 8), (1, 9), (3, 4), (2, 9)]),
    7: ('Order from relational clues', 'LOGIC.ORDER.01', 'Build an ordering that satisfies relational clues (before, after, between, next to)', P, 'ordering', 'constraint', ['MP1', 'MP2'], None, [(2, 6), (3, 6)]),
    8: ('And, inclusive or, exclusive or', 'LOGIC.CONNECTIVE.02', 'Find truth values of conjunctions and of inclusive and exclusive disjunctions', F, 'formal logic', 'formal', ['MP6'], None, []),
    9: ('Rotation or reflection?', 'LOGIC.SPATIAL.02', 'Distinguish rotations from reflections of a figure on a grid', P, 'rotation and reflection', 'visual', ['MP7'], None, [(2, 8), (1, 4), (2, 3)]),
    10: ('Deduction and induction', 'LOGIC.ARGUMENT.02', 'Tell deductive conclusions (forced by the premises) from inductive ones (supported by examples)', F, 'formal logic', 'formal', ['MP3', 'MP8'], None, []),
    11: ('The structure of words', 'LOGIC.WORD.01', 'Use letter counts, positions and alphabetical order to test word patterns within a stated rule', P, 'word structure', 'verbal', ['MP7', 'MP6'], None, [(1, 2), (1, 10), (1, 12), (2, 14), (2, 1)]),
    12: ('When is "if ... then" false?', 'LOGIC.CONDITIONAL.01', 'Find the truth value of a conditional and identify the one case that makes it false', F, 'formal logic', 'formal', ['MP3', 'MP6'], None, []),
    13: ('Necessary and sufficient conditions', 'LOGIC.CONDITIONAL.02', 'Translate "only if", "unless", "necessary" and "sufficient" into conditionals', F, 'formal logic', 'formal', ['MP6', 'MP3'], None, []),
    14: ('Logic grid puzzles', 'LOGIC.GRID.01', 'Solve a matching puzzle with a grid by combining clues until one assignment remains', P, 'logic grids', 'constraint', ['MP1', 'MP6'], None, [(3, 15)]),
    15: ('Converse, inverse and contrapositive', 'LOGIC.CONDITIONAL.03', 'Form the converse, inverse and contrapositive and decide which are equivalent to the original', F, 'formal logic', 'formal', ['MP3', 'MP7'], None, []),
    16: ('Biconditionals: "if and only if"', 'LOGIC.CONDITIONAL.04', 'Find truth values of biconditionals and use them as definitions', F, 'formal logic', 'formal', ['MP6', 'MP3'], None, []),
    17: ('Truth-tellers and liars', 'LOGIC.KNIGHTS.01', 'Find who tells the truth when each speaker either always tells the truth or always lies', P, 'truth-teller puzzles', 'constraint', ['MP1', 'MP3'], None, [(2, 11)]),
    18: ('Truth tables', 'LOGIC.TRUTH.01', 'Complete truth tables for compound statements', F, 'formal logic', 'formal', ['MP6', 'MP8'], None, []),
    19: ('Tautology, contradiction and equivalence', 'LOGIC.TRUTH.02', 'Classify compound statements as tautologies, contradictions or contingencies and test equivalence with a table', F, 'formal logic', 'formal', ['MP7', 'MP3'], None, []),
    20: ('What is on top? Stacking and occlusion', 'LOGIC.SPATIAL.03', 'Infer stacking order from what is visible and predict views of a stack', P, 'occlusion and stacking', 'visual', ['MP7', 'MP1'], None, [(2, 2), (2, 6), (3, 11)]),
    21: ('Valid inference forms', 'LOGIC.INFERENCE.01', 'Draw valid conclusions with modus ponens, modus tollens, chains and disjunctive syllogism', F, 'formal logic', 'formal', ['MP3'], None, []),
    22: ('Tempting invalid inferences', 'LOGIC.INFERENCE.02', 'Recognize affirming the consequent and denying the antecedent, and show why they fail', F, 'formal logic', 'formal', ['MP3', 'MP6'], None, []),
    23: ('Cube nets', 'LOGIC.SPATIAL.04', 'Match a cube to its net: which faces are opposite and which are adjacent', P, 'cube nets', 'visual', ['MP7', 'MP1'], None, [(3, 7)]),
    24: ('Valid versus sound', 'LOGIC.INFERENCE.03', 'Tell whether an argument is valid, and whether it is also sound', F, 'formal logic', 'formal', ['MP3'], None, []),
    25: ('Moves and rearrangements', 'LOGIC.SEQUENCE.01', 'Carry out stated moves on a row of tokens and find moves that reach a target', P, 'token moves', 'symbolic', ['MP1', 'MP6'], None, [(3, 3), (2, 7), (1, 6)]),
    26: ('Quantifiers over a stated domain', 'LOGIC.QUANT.01', 'Decide the truth of "all", "some" and "no" statements over a stated finite domain', F, 'formal logic', 'formal', ['MP6', 'MP3'], None, []),
    27: ('Negating quantified statements', 'LOGIC.QUANT.02', 'Negate statements with "all", "some", "no", and nested quantifiers', F, 'formal logic', 'formal', ['MP6', 'MP3'], None, []),
    28: ('Routes and paths', 'LOGIC.GRAPH.01', 'Trace routes in a drawn network and decide which routes exist under stated rules', P, 'routes and graphs', 'visual', ['MP1', 'MP7'], None, [(3, 2)]),
    29: ('Witnesses and counterexamples', 'LOGIC.QUANT.03', 'Give a witness for a "some" statement and a counterexample to an "all" statement', F, 'formal logic', 'formal', ['MP3'], None, []),
    30: ('Sets and Venn diagrams', 'LOGIC.SETS.01', 'Mark subset, intersection and complement relations on Venn diagrams', F, 'formal logic', 'formal', ['MP7', 'MP6'], None, []),
    31: ('Maps and neighbors', 'LOGIC.GRAPH.02', 'Turn a map into a neighbor (adjacency) graph and reason about neighbor counts and colorings', P, 'region adjacency', 'visual', ['MP7', 'MP1'], None, [(1, 13)]),
    32: ('Categorical arguments', 'LOGIC.SETS.02', 'Test categorical arguments with Venn diagrams, including the existence assumption', F, 'formal logic', 'formal', ['MP3', 'MP7'], None, []),
    33: ('Word ladders', 'LOGIC.WORD.02', 'Find shortest one-letter-change paths through a supplied word list', P, 'word ladders', 'verbal', ['MP1', 'MP7'], None, [(2, 12), (2, 4)]),
    34: ('Translate clues into conditions', 'LOGIC.CONSTRAINT.02', 'Translate puzzle clues into exact conditions and test candidate arrangements against them', P, 'clue translation', 'constraint', ['MP2', 'MP6'], None, [(3, 15)]),
    35: ('Must, could, cannot', 'LOGIC.CONSTRAINT.03', 'Decide what must be true, what could be true and what cannot be true in a constrained arrangement', P, 'scheduling puzzles', 'constraint', ['MP1', 'MP3'], None, []),
    36: ('Search every case', 'LOGIC.SEARCH.01', 'Organize a complete case analysis and count or find every solution', P, 'complete search', 'constraint', ['MP1', 'MP8'], None, [(3, 14)]),
    37: ('Direct proof with numbers', 'LOGIC.PROOF.01', 'Build a direct argument about even, odd and multiples from definitions', F, 'formal logic', 'formal', ['MP3', 'MP7'], None, []),
    38: ('Tiling and covering', 'LOGIC.SPATIAL.05', 'Decide which pieces cover a region exactly, and prove when no covering exists', P, 'tiling', 'visual', ['MP1', 'MP7'], None, [(3, 10)]),
    39: ('Justify each step of solving an equation', 'LOGIC.PROOF.02', 'Explain each step in solving an equation and justify the solution method', F, 'formal logic', 'formal', ['MP3', 'MP6'], 'HSA-REI.A.1', []),
    40: ('Proof by contradiction', 'LOGIC.PROOF.03', 'Set up and complete an argument by contradiction', F, 'formal logic', 'formal', ['MP3'], None, []),
    41: ('Parity and alternation', 'LOGIC.INVARIANT.01', 'Use odd/even and alternation to predict outcomes and rule out possibilities', P, 'parity', 'constraint', ['MP7', 'MP8'], None, [(1, 5)]),
    42: ('Disprove a claim with a counterexample', 'LOGIC.PROOF.04', 'Find a counterexample that disproves a general mathematical claim', F, 'formal logic', 'formal', ['MP3'], None, []),
    43: ('Proofs about lines and angles', 'LOGIC.PROOF.05', 'Order and justify the steps of proofs about angles formed by intersecting and parallel lines', F, 'formal logic', 'formal', ['MP3'], 'HSG-CO.C.9', []),
    44: ('Invariants and impossibility', 'LOGIC.INVARIANT.02', 'Find a quantity that never changes under the allowed moves and use it to prove a target is impossible', P, 'invariants', 'constraint', ['MP7', 'MP3'], None, [(1, 7)]),
    45: ('Letter grids and word squares', 'LOGIC.GRID.02', 'Fill and analyze letter grids under stated rules and a supplied word list', P, 'letter grids', 'verbal', ['MP1', 'MP7'], None, [(1, 7), (3, 13)]),
    46: ('Explanations and missing assumptions', 'LOGIC.EVIDENCE.01', 'Identify the unstated assumption an argument needs and evaluate competing explanations', F, 'formal logic', 'formal', ['MP3'], None, []),
    47: ('Is there enough information?', 'LOGIC.EVIDENCE.02', 'Decide whether the given information determines the answer, and what extra fact would', F, 'formal logic', 'formal', ['MP1', 'MP3'], None, []),
    48: ('Digital displays', 'LOGIC.SPATIAL.06', 'Reason about seven-segment digits: segments used, rotations and segment moves', P, 'seven-segment displays', 'visual', ['MP7', 'MP6'], None, [(3, 14), (1, 14), (2, 13)]),
    49: ('Common fallacies', 'LOGIC.FALLACY.01', 'Recognize common informal fallacies in self-contained arguments', F, 'informal logic', 'formal', ['MP3'], None, []),
    50: ('Weighing evidence', 'LOGIC.EVIDENCE.03', 'Judge whether evidence supports a claim: samples, comparisons and correlation', F, 'informal logic', 'formal', ['MP3', 'MP2'], None, []),
    51: ('Best possible: constrained optimization', 'LOGIC.OPTIMIZE.01', 'Find the best value under stated constraints and show nothing better is possible', P, 'optimization', 'constraint', ['MP1', 'MP7'], None, [(3, 14), (2, 15)]),
    52: ('Patterns from a stated rule family', 'LOGIC.PATTERN.01', 'Identify the rule in a stated family that fits a sequence, and continue it', P, 'sequences', 'symbolic', ['MP8', 'MP7'], None, [(1, 9), (1, 10), (2, 14)]),
    53: ('Rearranging letters', 'LOGIC.WORD.03', 'Find anagrams and letter-bank words within a supplied word list and letter rules', P, 'anagrams', 'verbal', ['MP7', 'MP1'], None, [(2, 7), (1, 6), (2, 15), (2, 1), (1, 15), (2, 5), (3, 5)]),
    54: ('Weighings and the least information needed', 'LOGIC.SEARCH.02', 'Plan weighings or questions and find the least number that always identifies the answer', P, 'balance puzzles', 'constraint', ['MP1', 'MP3'], None, []),
}
