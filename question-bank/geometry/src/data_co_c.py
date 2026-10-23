"""G-CO.C: proving theorems about lines and angles, triangles, and parallelograms (sets 17-27)."""
from qb import S, B, sa, mc, tf
from common import gd, grid_fig, NTS, proof


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


X_AB_CD = gd({'A': (-2.4, -1.1), 'B': (2.4, 1.1), 'C': (-1.6, 1.7), 'D': (1.6, -1.7), 'E': (0, 0)},
             [('line', 'A', 'B', {'ext': 6}), ('line', 'C', 'D', {'ext': 6})], lab={'E': 's'}, h=200,
             desc='Lines AB and CD cross at point E. A and B are on one line, C and D on the other, with E between A and B and between C and D.')
NUM4 = gd({'O': (0, 0)}, [('line', (-2.2, -0.9), (2.2, 0.9)), ('line', (-1.2, 1.9), (1.2, -1.9)),
                          ('text', (0.9, 0.85), '1'), ('text', (-0.75, 0.75), '2'), ('text', (-0.9, -0.85), '3'), ('text', (0.75, -0.75), '4'),
                          ('text', (2.3, 1.35), 'ℓ'), ('text', (1.35, -1.45), 'm')], lab={'O': 's'}, h=200,
          desc='Lines ℓ and m cross at point O, forming four angles numbered 1, 2, 3, 4 in counterclockwise order. Angles 1 and 3 are '
               'vertical angles, and so are angles 2 and 4.')


def transversal(desc_extra='', h=230, marks=True):
    """Lines ℓ ∥ m (horizontal) cut by transversal t; angles 1-4 at the top intersection P, 5-8 at the bottom Q."""
    P, Q = (0.6, 1.5), (-0.6, -1.5)
    items = [('line', (-3, 1.5), (3, 1.5), {'arrows': 1 if marks else 0}), ('line', (-3, -1.5), (3, -1.5), {'arrows': 1 if marks else 0}),
             ('line', (1.2, 3.0), (-1.2, -3.0)),
             ('text', (1.25, 1.85), '1'), ('text', (0.05, 1.85), '2'), ('text', (-0.05, 1.15), '3'), ('text', (1.15, 1.15), '4'),
             ('text', (0.05, -1.15), '5'), ('text', (-1.15, -1.15), '6'), ('text', (-1.25, -1.85), '7'), ('text', (-0.05, -1.85), '8'),
             ('text', (2.7, 1.85), 'ℓ'), ('text', (2.7, -1.15), 'm'), ('text', (1.6, 2.6), 't')]
    return gd({'P': P, 'Q': Q}, items, h=h, nolabel=('P', 'Q'), nodot=('P', 'Q'),
              desc='Two horizontal lines ℓ (top) and m (bottom) cut by a transversal t that slants down to the left. '
                   + ('Arrow marks show ℓ ∥ m. ' if marks else '') +
                   'At the top crossing the angles are numbered 1 (upper right), 2 (upper left), 3 (lower left), 4 (lower right); at the '
                   'bottom crossing 5 (upper right), 6 (upper left), 7 (lower left), 8 (lower right).' + desc_extra)


PROOF_RULE = ('Any valid proof (paragraph, two-column, or flow). ')

SETS = [
    # ------------------------------------------------------------------ 17. CO.C.9 vertical angles
    S('HSG-CO.C.9', 'Prove that vertical angles are congruent',
      target='Prove that vertical angles are congruent', strand='core', covers=['CO9-vertical'],
      main=[
          proof('Lines AB and CD intersect at E. Prove that ∠AEC ≅ ∠BED.', fig=X_AB_CD,
                method='Use the two linear pairs that share ∠CEB, and the subtraction property of equality.',
                key='∠AEC ≅ ∠BED',
                note=PROOF_RULE + 'Essential: (1) m∠AEC + m∠CEB = 180° (linear pair: A, E, B are collinear); (2) m∠CEB + m∠BED = 180° (linear pair: '
                     'C, E, D are collinear); (3) so m∠AEC + m∠CEB = m∠CEB + m∠BED (substitution/transitive); (4) subtract m∠CEB. Alternative: the 180° '
                     'rotation about E maps ray EA to ray EB and ray EC to ray ED. Invalid: "they look equal", measuring, or citing the theorem itself.'),
          proof('Lines ℓ and m meet at O, forming ∠1, ∠2, ∠3, and ∠4 in order around O. Prove that ∠2 ≅ ∠4.', fig=NUM4,
                method='Use the linear pairs ∠1 and ∠2, and ∠1 and ∠4, then the subtraction property of equality.',
                key='∠2 ≅ ∠4',
                note=PROOF_RULE + 'Essential: m∠1 + m∠2 = 180° and m∠1 + m∠4 = 180° (linear pairs, each with a reason); so m∠2 = 180° - m∠1 = m∠4. '
                     'Using ∠3 as the shared angle is also valid. Invalid: using ∠2 ≅ ∠4 as a step.'),
          sa('A proof that ∠1 ≅ ∠3 for vertical angles 1 and 3 (with ∠2 next to both):\n1. m∠1 + m∠2 = 180°  (linear pair)\n2. m∠2 + m∠3 = 180°  (linear pair)\n'
             '3. m∠1 + m∠2 = m∠2 + m∠3  (?)\n4. m∠1 = m∠3  (?)\nGive the reasons for steps 3 and 4.', 'Reasons:',
             key='Step 3: substitution (or the transitive property of equality); step 4: subtraction property of equality.',
             note='Any equivalent names for both reasons. Both are required.'),
          proof('Lines AB and CD intersect at E. Explain, using a rigid motion, why ∠AEC ≅ ∠BED.', fig=X_AB_CD,
                method='Use the 180° rotation about E and explain where it sends rays EA and EC.',
                key='The 180° rotation about E maps ∠AEC onto ∠BED, so the angles are congruent.',
                note='Any valid explanation. Essential: a 180° rotation about E maps each line through E onto itself, sending ray EA to the opposite ray EB '
                     'and ray EC to ray ED; so it maps ∠AEC onto ∠BED; rotations keep angle measures.'),
          mc('A student measures two vertical angles in one drawing, finds that both are 47°, and writes "vertical angles are congruent." Why is this not a proof?',
             ['It checks one example; a proof must show the result for every pair of vertical angles', 'Protractors are never accurate',
              'Vertical angles are not always congruent', 'The student should have measured all four angles'],
             note='Measuring can suggest a theorem but cannot prove it for all cases.'),
      ],
      back=[
          B('Angles in a linear pair add to 180°', '7.G.B.5', [
              sa('Two angles form a linear pair. One measures 128°. Find the other.', 'Measure:', key='52°', note='Any equivalent form.'),
              sa('∠PQR and ∠RQS form a linear pair, and m∠PQR = 3 · m∠RQS. Find m∠RQS.', 'Measure:', key='45°', note='Any equivalent form. 4x = 180.'),
              tf('The two angles of a linear pair are always supplementary.', key=True, note='Together they form a straight angle, 180°.'),
              mc('Points A, B, C are on a line with B between A and C, and ray BD is drawn. Which angles form a linear pair?', ['∠ABD and ∠DBC', '∠ABD and ∠ABC',
                                                                                                                             '∠DBC and ∠ABC', '∠BAD and ∠BCD'],
                 note='They share ray BD and their other sides are opposite rays BA and BC.'),
              tf('Two angles that add to 180° must form a linear pair.', key=False, note='Supplementary angles need not be adjacent.'),
          ], align='exact',
            why=why('the student does not know that a linear pair adds to 180°.', 'every step of the vertical angle proof uses a linear pair.',
                    'finds and uses linear pairs.')),
          B('Use properties of equality as reasons', 'HSA-REI.A.1', [
              sa('From m∠1 + 40° = m∠2 + 40°, which property gives m∠1 = m∠2?', 'Property:', key='Subtraction property of equality', note='Any equivalent wording.'),
              sa('If x + y = 180 and y + z = 180, which property lets you write x + y = y + z?', 'Property:', key='Substitution (or the transitive property of equality)',
                 note='Any equivalent wording.'),
              mc('Which property justifies: if a = b, then b = a?', ['Symmetric property', 'Reflexive property', 'Transitive property', 'Distributive property'],
                 note='Swapping the sides is the symmetric property.'),
              tf('The reflexive property says that any quantity equals itself, such as m∠A = m∠A.', key=True, note='a = a.'),
              tf('From 2x = 2y you may conclude x = y by the subtraction property of equality.', key=False, note='That step divides by 2 (division property).'),
          ], align='exact',
            why=why('the student cannot name the algebra behind a proof step.', 'the vertical angle proof is two linear pairs plus equality properties.',
                    'names the property that justifies each algebraic step.')),
          B('Identify vertical angles and linear pairs in a figure', '7.G.B.5', [
              mc('Lines ℓ and m meet at O, forming ∠1, ∠2, ∠3, ∠4 in order. Which angle is vertical to ∠1?', ['∠3', '∠2', '∠4', '∠1'], fig=NUM4,
                 note='Vertical angles are opposite each other.'),
              sa('Lines ℓ and m meet at O, forming ∠1, ∠2, ∠3, ∠4 in order. Name the two angles that form linear pairs with ∠2.', 'Angles:', fig=NUM4,
                 key='∠1 and ∠3', note='Any order.'),
              tf('Vertical angles share a side.', key=False, note='They share only the vertex; their sides are opposite rays.'),
              tf('When two lines cross, they form two pairs of vertical angles.', key=True, note='∠1 with ∠3, and ∠2 with ∠4.'),
              sa('Two lines cross. One angle is 63°. Find its vertical angle and the angles next to it.', 'Answer:', key='Vertical: 63°; adjacent: 117° and 117°',
                 note='Any equivalent form.'),
          ], align='supporting',
            why=why('the student cannot find the vertical and linear-pair angles in a figure.', 'the proof starts by naming them.',
                    'identifies the angle pairs formed by two crossing lines.')),
      ],
      f1=B('Use the vertical angle theorem in multistep proofs', 'HSG-CO.C.9', [
          proof('Lines AB and CD intersect at E, and ray EF bisects ∠AEC. Ray EG is the ray opposite ray EF. Prove that ray EG bisects ∠BED.',
                method='Combine the bisector definition with vertical angles (∠AEF and ∠BEG; ∠FEC and ∠GED).',
                key='m∠BEG = m∠GED, so EG bisects ∠BED.',
                note=PROOF_RULE + 'Essential: m∠AEF = m∠FEC (bisector); ∠AEF ≅ ∠BEG and ∠FEC ≅ ∠DEG (vertical angles, since EG is opposite EF, '
                     'EB opposite EA, ED opposite EC); so m∠BEG = m∠GED.'),
          proof('Three lines meet at point O, forming six angles. Two of the angles that are next to each other are 50° and 70°. Prove that the six angles are 50°, 70°, 60°, 50°, 70°, 60° in order.',
                method='Use the straight angle (180°) to find the third angle on one side, then vertical angles for the other three.',
                key='The angles in order are 50°, 70°, 60°, 50°, 70°, 60°.',
                note=PROOF_RULE + 'Essential: three adjacent angles on one side of a line add to 180°, so the third is 60°; each of the other three is vertical to one of these.'),
          sa('Two lines meet. One angle is (4x + 10)° and its vertical angle is (6x - 30)°. Find x and all four angles.', 'Answer:',
             key='x = 20; angles 90°, 90°, 90°, 90°', note='Form required: x and the four angles. 4x + 10 = 6x - 30 gives x = 20, so the angle is 90°.'),
          tf('If one angle formed by two crossing lines is a right angle, all four angles are right angles.', key=True,
             note='Its vertical angle is 90° and its neighbors are 180° - 90°.'),
          mc('Lines AB and CD meet at E with m∠AEC = 2x and m∠CEB = 3x. What is m∠BED?', ['72°', '108°', '36°', '144°'],
             note='2x + 3x = 180, so x = 36 and m∠AEC = 72°; ∠BED is vertical to ∠AEC.'),
      ], prog='same-course deepening', demand='Use the vertical angle theorem as one step inside a longer proof with bisectors and several lines.'),
      f2=B('Prove statements about the bisectors of angles formed by two lines', 'HSG-CO.C.9', [
          proof('∠ABD and ∠DBC form a linear pair. Ray BE bisects ∠ABD and ray BF bisects ∠DBC. Prove that ∠EBF is a right angle.',
                method='Express m∠EBF as half of m∠ABD plus half of m∠DBC.',
                key='m∠EBF = 90°',
                note=PROOF_RULE + 'Essential: m∠EBD = ½m∠ABD, m∠DBF = ½m∠DBC (bisectors); m∠EBF = ½(m∠ABD + m∠DBC) = ½(180°) = 90°.'),
          sa('Is the converse of the vertical angle theorem true: "If two angles are congruent, they are vertical angles"? Explain.', 'Answer:',
             key='No. Two 30° angles in different places in a figure are congruent but not vertical angles.', note='Any valid counterexample.'),
          proof('Two lines meet at O. Prove that the bisectors of a pair of vertical angles lie on one line.',
                method='Show that the angle between the two bisector rays is 180°.',
                key='The bisector rays are opposite rays, so they lie on one line.',
                note=PROOF_RULE + 'Essential: if the vertical angles each measure 2a and the other two each 180° - 2a, the angle from one bisector to the other '
                     'is a + (180° - 2a) + a = 180°.'),
          tf('The bisectors of two angles that form a linear pair are perpendicular.', key=True, note='Half of 180° is 90°.'),
          mc('Two lines meet, and the bisectors of two adjacent angles are drawn. What angle do the bisectors form?', ['90°', '180°', '45°', 'It depends on the lines'],
             note='Adjacent angles formed by two lines are a linear pair, so their bisectors meet at 90°.'),
      ], prog='same-course deepening', demand='Prove new statements about angle bisectors, and test a converse with a counterexample.',
        builds='Builds on FORWARD 1: combines bisectors with linear pairs and vertical angles in new, general statements.')),

    # ------------------------------------------------------------------ 18. CO.C.9 parallel lines
    S('HSG-CO.C.9', 'Prove the angle theorems for parallel lines cut by a transversal',
      target='Prove that when a transversal crosses parallel lines, alternate interior angles are congruent and corresponding angles are congruent',
      strand='core', covers=['CO9-parallel'],
      main=[
          proof('Lines ℓ and m are parallel and are cut by transversal t. Assume the corresponding angles postulate (corresponding angles formed by a transversal '
                'of parallel lines are congruent). Prove that alternate interior angles ∠3 and ∠5 are congruent.', fig=transversal(),
                method='Use the corresponding angle of ∠5 at the top crossing and vertical angles.',
                key='∠3 ≅ ∠5',
                note=PROOF_RULE + 'Essential: ∠1 ≅ ∠5 (corresponding angles postulate, ℓ ∥ m); ∠1 ≅ ∠3 (vertical angles); so ∠3 ≅ ∠5 (transitive). '
                     'Invalid: "they look equal"; assuming alternate interior angles are congruent.'),
          proof('Lines ℓ and m are parallel and are cut by transversal t. Assume that alternate interior angles are congruent. Prove that corresponding angles ∠2 and ∠6 are congruent.',
                fig=transversal(), method='Use an alternate interior angle and vertical angles.',
                key='∠2 ≅ ∠6',
                note=PROOF_RULE + 'Essential: ∠4 ≅ ∠6 (alternate interior angles); ∠2 ≅ ∠4 (vertical angles); so ∠2 ≅ ∠6 (transitive).'),
          proof('Lines ℓ and m are parallel and are cut by transversal t, crossing ℓ at P and m at Q. Explain, using a translation, why corresponding angles ∠1 and ∠5 are congruent.',
                fig=transversal(),
                method='Translate along the transversal from Q to P. Explain why the image of m is ℓ and why the image of ∠5 is ∠1.',
                key='The translation that moves Q to P maps m onto ℓ and maps t onto itself, so it maps ∠5 onto ∠1; translations keep angle measure.',
                note='Any valid explanation. Essential: (1) the translation maps t onto itself (it moves along t); (2) it maps m to a line through P parallel to m; '
                     '(3) by the parallel postulate that line is ℓ; (4) so the angle formed by t and m at Q maps to the corresponding angle at P; (5) angle measure is kept.'),
          sa('Lines ℓ ∥ m are cut by transversal t, and m∠1 = 115°. Find m∠5, m∠3, and m∠6. Give a reason for each.', 'Answer:', fig=transversal(),
             key='m∠5 = 115° (corresponding to ∠1); m∠3 = 115° (vertical to ∠1); m∠6 = 65° (linear pair with ∠5).',
             note='Form required: each measure with a valid reason. Other valid reason chains are accepted.'),
          mc('A student "proves" that alternate interior angles are congruent by saying: "The lines are parallel because the alternate interior angles are congruent." What is wrong?',
             ['The argument is circular: it assumes the conclusion', 'Nothing; the argument is correct', 'Alternate interior angles are supplementary',
              'The lines must be perpendicular'],
             note='The statement uses the result it is trying to prove (and states a converse instead).'),
      ],
      back=[
          B('Name and use angles formed by parallel lines and a transversal', '8.G.A.5', [
              sa('Lines ℓ ∥ m are cut by transversal t. ∠4 measures 70°. Find the measure of ∠6.', 'Measure:', fig=transversal(), key='70°',
                 note='Any equivalent form. ∠4 and ∠6 are alternate interior angles.'),
              mc('Lines ℓ ∥ m are cut by transversal t. Which angle corresponds to ∠2?', ['∠6', '∠5', '∠7', '∠8'], fig=transversal(),
                 note='Both are in the upper-left position at their crossings.'),
              tf('Lines ℓ ∥ m are cut by transversal t. ∠4 and ∠5 are same-side interior angles, so they add to 180°.', key=True, fig=transversal(),
                 note='They are on the same side of t, between the lines.'),
              tf('When two lines are cut by a transversal, corresponding angles are congruent even if the lines are not parallel.', key=False,
                 note='They are congruent only when the lines are parallel.'),
              sa('Lines ℓ ∥ m are cut by transversal t. ∠8 measures 112°. Find the measure of ∠2.', 'Measure:', fig=transversal(), key='112°',
                 note='Any equivalent form. ∠8 and ∠2 are alternate exterior angles.'),
          ], align='exact',
            why=why('the student cannot name the angle pairs or their relationships.', 'the theorems are about these specific pairs.',
                    'names corresponding, alternate interior, and same-side angles and finds their measures.')),
          B('Vertical angles and linear pairs as reasons', 'HSG-CO.C.9', [
              sa('Two lines cross. Name the reason two opposite angles are congruent.', 'Reason:', key='Vertical angles are congruent', note='Any equivalent wording.'),
              sa('Name the reason two adjacent angles on a line add to 180°.', 'Reason:', key='They form a linear pair (supplementary)', note='Any equivalent wording.'),
              mc('At the top crossing, ∠1 = 110°. What is ∠2 and why?', ['70°, linear pair', '110°, vertical angles', '70°, vertical angles', '110°, linear pair'],
                 fig=transversal(), note='∠1 and ∠2 are next to each other on line ℓ.'),
              tf('Angles 1 and 3 are vertical angles in the figure.', key=True, fig=transversal(), note='They are opposite each other at the top crossing.'),
              tf('Angles 1 and 4 are vertical angles in the figure.', key=False, fig=transversal(), note='They are adjacent: a linear pair along t.'),
          ], align='exact',
            why=why('the student cannot connect angles at one crossing.', 'each proof links the two crossings with vertical angles or linear pairs.',
                    'gives vertical-angle and linear-pair reasons.')),
          B('The parallel postulate and the definition of parallel lines', 'HSG-CO.A.1', [
              tf('Through a point not on a line, there is exactly one line parallel to it (in a plane).', key=True, note='The parallel postulate.'),
              sa('Line ℓ is parallel to line m. Line n passes through a point of ℓ and is also parallel to m. What can you conclude about n?', 'Answer:',
                 key='n is the same line as ℓ.', note='Any equivalent answer: by the parallel postulate.'),
              mc('Which pair of lines in a plane are parallel?', ['y = 2x + 1 and y = 2x - 5', 'y = 2x + 1 and y = -2x + 1', 'y = x and y = -x', 'x = 2 and y = 2'],
                 note='Same slope, different intercepts: they never meet.'),
              tf('Two lines in a plane that never meet are parallel.', key=True, note='Definition of parallel lines.'),
              sa('Line ℓ ∥ line m. A translation maps m to a line through a point of ℓ. Must that image line be parallel to m or the same as m?', 'Answer:',
                 key='Parallel to m (a translation maps a line to a parallel line or itself); so it is ℓ.', note='Any equivalent answer.'),
          ], align='exact',
            why=why('the student does not know the uniqueness of the parallel through a point.', 'the rigid-motion proof depends on it.',
                    'uses the definition of parallel lines and the parallel postulate.')),
      ],
      f1=B('Prove the converse: congruent alternate interior angles make lines parallel', 'HSG-CO.C.9', [
          proof('Lines ℓ and m are cut by transversal t, and alternate interior angles ∠3 and ∠5 are congruent. Prove that ℓ ∥ m.', fig=transversal(marks=False),
                method='Indirect proof: suppose ℓ and m meet; they would form a triangle with t whose angles contradict a known result. Or use the 180° '
                       'rotation about the midpoint of PQ.',
                key='ℓ ∥ m',
                note=PROOF_RULE + 'Essential (indirect): if ℓ and m met at a point R, triangle PQR would have an exterior angle equal to a remote interior '
                     'angle, which is impossible (an exterior angle is greater than each remote interior angle); so they do not meet. Alternative: the 180° '
                     'rotation about the midpoint of PQ swaps P and Q and maps ℓ onto m, so if they met on one side they would also meet on the other, '
                     'giving two common points. Invalid: assuming ℓ ∥ m.'),
          sa('Lines ℓ and m are cut by transversal t with m∠4 = (5x - 20)° and m∠6 = (3x + 30)°. For what value of x is ℓ ∥ m? Explain.', 'Answer:',
             fig=transversal(marks=False), key='x = 25, because then the alternate interior angles are congruent (105°).',
             note='Form required: x with the converse as the reason. 5x - 20 = 3x + 30.'),
          tf('If same-side interior angles are supplementary, the lines are parallel.', key=True, note='Then the alternate interior angles are congruent.'),
          mc('Which fact proves that lines ℓ and m are parallel?', ['A pair of corresponding angles is congruent', 'A pair of vertical angles is congruent',
                                                                     'A linear pair adds to 180°', 'Two angles at the same crossing are equal'],
             note='Vertical angles and linear pairs hold for any crossing lines.'),
          sa('Lines ℓ and m are cut by a transversal. m∠1 = 72° and m∠7 = 108°. Are ℓ and m parallel? Explain.', 'Answer:', fig=transversal(marks=False),
             key='No. ∠1 and ∠7 are alternate exterior angles; if ℓ ∥ m they would be congruent, but 72° ≠ 108°.',
             note='Form required: the conclusion with a reason. Equivalently, ∠5 is vertical to ∠7, so m∠5 = 108°, but its corresponding angle ∠1 is 72°.'),
      ], prog='same-course deepening', demand='Prove the CONVERSE (from congruent angles to parallel lines), which needs an indirect argument.'),
      f2=B('Use parallel-line theorems to prove the triangle angle sum', 'HSG-CO.C.10', [
          proof('Prove that the angles of triangle ABC add to 180°. Begin by drawing the line through B parallel to AC.',
                method='Name the two new angles at B, use alternate interior angles, and the straight angle at B.',
                key='m∠A + m∠B + m∠C = 180°',
                note=PROOF_RULE + 'Essential: the line through B parallel to AC exists (parallel postulate); the angles it makes with BA and BC are congruent '
                     'to ∠A and ∠C (alternate interior angles); those two angles and ∠ABC form a straight angle, 180°.'),
          sa('In triangle ABC, a line through B parallel to AC makes a 50° angle with BA (on A\'s side) and a 65° angle with BC (on C\'s side). Find all three angles of the triangle.',
             'Answer:', key='∠A = 50°, ∠C = 65°, ∠B = 65°', note='Form required: all three. Alternate interior angles give ∠A and ∠C; 180 - 50 - 65 = 65.'),
          tf('The proof of the triangle angle sum depends on the parallel postulate.', key=True, note='It needs the unique parallel through B.'),
          mc('Which theorem is used to show the new angles at B equal ∠A and ∠C?', ['Alternate interior angles theorem', 'Vertical angles theorem',
                                                                                    'Isosceles triangle theorem', 'Triangle inequality'],
             note='Sides BA and BC are transversals of the parallel lines (AC and the line through B).'),
          sa('Explain why the exterior angle at C of triangle ABC equals m∠A + m∠B.', 'Explanation:',
             key='The exterior angle forms a linear pair with ∠C, so it is 180° - m∠C, which equals m∠A + m∠B by the angle sum.', note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Apply the parallel-line theorems as tools to prove a triangle theorem.',
        builds='FORWARD 1 proves when lines are parallel; FORWARD 2 uses parallel lines to prove the triangle angle sum.')),
]

PB = gd({'A': (-2.5, 0), 'B': (2.5, 0), 'M': (0, 0), 'P': (0, 2.6)},
        [('seg', 'A', 'B'), ('line', (0, -1.4), (0, 3.2)), ('seg', 'P', 'A', {'dash': True}), ('seg', 'P', 'B', {'dash': True}),
         ('seg', 'A', 'M', {'ticks': 1}), ('seg', 'M', 'B', {'ticks': 1}), ('ra', 'M', 'B', 'P'), ('text', (0.35, -1.3), 'ℓ')],
        lab={'M': 'sw', 'P': 'e'}, h=210,
        desc='Segment AB with midpoint M (AM and MB marked congruent). Line ℓ is perpendicular to AB at M (right-angle mark). Point P is on ℓ above AB; dashed segments join P to A and to B.')
TRI = gd({'A': (0, 0), 'B': (5, 0), 'C': (1.6, 3)}, [('poly', ['A', 'B', 'C'])], h=190,
         desc='Triangle ABC with base AB and vertex C above it.')
ISO = gd({'A': (0, 3.2), 'B': (-1.8, 0), 'C': (1.8, 0)},
         [('poly', ['A', 'B', 'C']), ('seg', 'A', 'B', {'ticks': 1}), ('seg', 'A', 'C', {'ticks': 1})], h=200,
         desc='Triangle ABC with AB and AC marked congruent (one tick mark each); BC is the base.')

SETS += [
    # ------------------------------------------------------------------ 19. CO.C.9 perpendicular bisector
    S('HSG-CO.C.9', 'Prove the perpendicular bisector theorem and its converse',
      target='Prove that the points on the perpendicular bisector of a segment are exactly the points equidistant from its endpoints (both directions)',
      strand='core', covers=['CO9-perpbis'],
      main=[
          proof('Line ℓ is the perpendicular bisector of segment AB, meeting AB at M. Point P is on ℓ. Prove that PA = PB.', fig=PB,
                method='Use SAS on triangles PMA and PMB.',
                key='PA = PB',
                note=PROOF_RULE + 'Essential: AM = BM (M is the midpoint); ∠PMA ≅ ∠PMB (both right angles, ℓ ⊥ AB); PM = PM (reflexive); △PMA ≅ △PMB (SAS); '
                     'PA = PB (corresponding parts). If P = M, PA = MA = MB = PB directly. Alternative: the reflection across ℓ fixes P and swaps A and B.'),
          proof('Point P is not on line AB, and PA = PB. Let M be the midpoint of AB. Prove that line PM is perpendicular to AB, so P is on the perpendicular bisector of AB.',
                method='Use SSS on triangles PMA and PMB, then the linear pair of congruent angles at M.',
                key='PM ⊥ AB, so P is on the perpendicular bisector of AB.',
                note=PROOF_RULE + 'Essential: PA = PB (given), AM = BM (midpoint), PM = PM; △PMA ≅ △PMB (SSS); ∠PMA ≅ ∠PMB; they form a linear pair, so each '
                     'is 90°; so PM is perpendicular to AB through its midpoint. Invalid: drawing the perpendicular bisector through P and assuming it '
                     'passes through P (that is the claim).'),
          sa('The theorem says the points on the perpendicular bisector of AB are EXACTLY the points equidistant from A and B. Which two statements must be proved?',
             'Answer:', key='(1) Every point on the perpendicular bisector is equidistant from A and B. (2) Every point equidistant from A and B is on the perpendicular bisector.',
             note='Any equivalent wording of both directions.'),
          proof('In a coordinate plane, A(-a, 0) and B(a, 0) with a > 0. Prove that every point P(0, y) on the y-axis is equidistant from A and B, and that every point '
                'P(x, y) with PA = PB has x = 0.',
                method='Use the distance formula in both directions.',
                key='PA = PB = √(a² + y²) for P(0, y); and PA = PB gives (x + a)² = (x - a)², so x = 0.',
                note=PROOF_RULE + 'Essential: both directions. (1) √(a² + y²) both ways. (2) (x + a)² + y² = (x - a)² + y² simplifies to 4ax = 0, and a ≠ 0, so x = 0.'),
          mc('A student proves only that every point on the perpendicular bisector of AB is equidistant from A and B. What is missing?',
             ['The converse: every point equidistant from A and B is on the perpendicular bisector', 'A proof that the bisector is a line',
              'A measurement of PA and PB', 'Nothing; one direction proves "exactly"'],
             note='"Exactly those points" needs both directions.'),
      ],
      back=[
          B('Use the definitions of midpoint and perpendicular bisector', 'HSG-CO.A.1', [
              sa('M is the midpoint of AB and AB = 14. Find AM.', 'AM =', key='7', note='Any equivalent form.'),
              tf('The perpendicular bisector of AB passes through the midpoint of AB and is perpendicular to AB.', key=True, note='That is its definition.'),
              mc('Line ℓ meets AB at M with AM = MB, but ℓ is not perpendicular to AB. What is ℓ?', ['A bisector of AB that is not the perpendicular bisector',
                                                                                                   'The perpendicular bisector of AB', 'Parallel to AB', 'Not related to AB'],
                 note='It bisects the segment but is not perpendicular.'),
              sa('Line ℓ is perpendicular to AB at M, and AM = 3, MB = 5. Is ℓ the perpendicular bisector of AB? Explain.', 'Answer:',
                 key='No. M is not the midpoint (3 ≠ 5).', note='Any equivalent answer.'),
              tf('A segment has exactly one perpendicular bisector in a plane.', key=True, note='Exactly one line is perpendicular to AB at its midpoint.'),
          ], align='exact',
            why=why('the student does not know what the perpendicular bisector is.', 'the theorem is about that line.',
                    'applies the definitions of midpoint and perpendicular bisector.')),
          B('Use SAS and SSS to prove triangles congruent', 'HSG-CO.B.8', [
              sa('In △PMA and △PMB, PM is shared, AM = BM, and ∠PMA ≅ ∠PMB. Which criterion proves they are congruent?', 'Criterion:', key='SAS', note='Any equivalent form.'),
              sa('In △PMA and △PMB, PA = PB, AM = BM, and PM is shared. Which criterion proves they are congruent?', 'Criterion:', key='SSS', note='Any equivalent form.'),
              mc('Two triangles share a side and have two other pairs of congruent sides. Which criterion applies?', ['SSS', 'SAS', 'ASA', 'AAS'],
                 note='Three pairs of congruent sides.'),
              tf('A side shared by two triangles counts as a pair of congruent sides.', key=True, note='Reflexive property.'),
              tf('SSA is a valid congruence criterion.', key=False, note='Two sides and a non-included angle do not always determine a triangle.'),
          ], align='exact',
            why=why('the student cannot choose a congruence criterion.', 'both directions of the proof use a congruence (SAS, then SSS).',
                    'picks SAS or SSS from given parts.')),
          B('Corresponding parts of congruent triangles and right angles from a linear pair', 'HSG-CO.B.7', [
              sa('△PMA ≅ △PMB. Which angle corresponds to ∠PMA?', 'Angle:', key='∠PMB', note='Any equivalent form.'),
              sa('Two congruent angles form a linear pair. What is each angle\'s measure?', 'Measure:', key='90°', note='Any equivalent form.'),
              tf('If △PMA ≅ △PMB, then PA = PB.', key=True, note='Corresponding sides.'),
              mc('△XYZ ≅ △XWZ. Which pair of segments must be congruent?', ['YZ and WZ', 'XY and XZ', 'XZ and YW', 'YZ and XW'], note='Y ↔ W and Z ↔ Z.'),
              tf('Two angles in a linear pair are always congruent.', key=False, note='They are supplementary; they are congruent only when both are 90°.'),
          ], align='exact',
            why=why('the student cannot draw conclusions from a congruence.', 'each proof ends by naming corresponding parts.',
                    'names corresponding parts and the right-angle consequence.')),
      ],
      f1=B('Use the perpendicular bisector to find points equidistant from two points', 'HSG-GPE.B.5', [
          sa('Find an equation of the perpendicular bisector of the segment from A(2, 1) to B(6, 5).', 'Equation:', key='y = -x + 7',
             note='Any equivalent equation. Midpoint (4, 3); slope of AB is 1, so the bisector has slope -1.'),
          sa('Find the point on the x-axis that is equidistant from A(2, 1) and B(6, 5).', 'Point:', key='(7, 0)',
             note='Form required: an ordered pair. It is where y = -x + 7 meets y = 0.'),
          tf('The point (4, 3) is equidistant from (0, 0) and (8, 6).', key=True, note='It is the midpoint; both distances are 5.'),
          mc('Which point is equidistant from A(0, 0) and B(4, 0)?', ['(2, 7)', '(3, 1)', '(0, 2)', '(4, 4)'], note='Points on x = 2.'),
          sa('Points A(-1, 2) and B(3, 2). Describe all points equidistant from A and B.', 'Answer:', key='The vertical line x = 1.', note='Any equivalent description.'),
      ], prog='cross-standard extension', demand='Use the theorem with coordinates to locate points equidistant from two points (equation of the bisector).'),
      f2=B('Prove that the perpendicular bisectors of a triangle meet at one point', 'HSG-C.A.3', [
          proof('Prove that the perpendicular bisectors of the sides of triangle ABC meet at one point O, and that O is equidistant from A, B, and C.',
                method='Let the bisectors of AB and BC meet at O; use the theorem and its converse.',
                key='The three perpendicular bisectors meet at O, and OA = OB = OC.',
                note=PROOF_RULE + 'Essential: the bisectors of AB and BC are not parallel (AB and BC are not parallel), so they meet at O; OA = OB and OB = OC (theorem); '
                     'so OA = OC; by the converse O is on the bisector of AC.'),
          sa('Triangle ABC has A(0, 0), B(6, 0), C(0, 8). Find the point equidistant from all three vertices.', 'Point:', key='(3, 4)',
             note='Form required: an ordered pair. Bisectors x = 3 and y = 4 meet at (3, 4); it is 5 from each vertex.'),
          tf('The point where the perpendicular bisectors of a triangle meet is always inside the triangle.', key=False,
             note='For an obtuse triangle it is outside; for a right triangle it is on the hypotenuse.'),
          mc('Three towns are to share a well equally distant from all three. Where should it go?', ['Where the perpendicular bisectors of the triangle\'s sides meet',
                                                                                                      'Where the angle bisectors meet', 'At the midpoint of the longest side', 'Where the medians meet'],
             note='Points equidistant from two towns are on the perpendicular bisector.'),
          sa('Explain why showing that the perpendicular bisectors of AB and BC meet at O is enough to show that all three meet at O.', 'Explanation:',
             key='OA = OB and OB = OC give OA = OC, and by the converse O is on the perpendicular bisector of AC.', note='Any equivalent explanation.'),
      ], prog='cross-standard extension', demand='Use both directions of the theorem in a new proof: the three perpendicular bisectors are concurrent.',
        builds='FORWARD 1 finds points equidistant from two points; FORWARD 2 extends to three points (the circumcenter) with a proof.')),

    # ------------------------------------------------------------------ 20. CO.C.10 angle sum
    S('HSG-CO.C.10', 'Prove that the angles of a triangle add to 180°',
      target='Prove that the measures of the interior angles of any triangle add to 180°', strand='core', covers=['CO10-sum'],
      main=[
          proof('Prove that m∠A + m∠B + m∠C = 180° in triangle ABC. Draw the line through C parallel to AB.', fig=TRI,
                method='Name the two new angles at C, use alternate interior angles with AB, and the straight angle at C.',
                key='m∠A + m∠B + m∠C = 180°',
                note=PROOF_RULE + 'Essential: (1) through C there is exactly one line parallel to AB (parallel postulate); (2) the angles it makes with CA and CB are '
                     'congruent to ∠A and ∠B (alternate interior angles, transversals CA and CB); (3) those two angles and ∠ACB form a straight angle, 180°; '
                     '(4) substitute. Invalid: measuring angles; citing the exterior angle theorem (it depends on this result).'),
          proof('In triangle PQR, draw the line through P parallel to QR. Prove that the angles of triangle PQR add to 180°.',
                method='Same strategy with vertex P: alternate interior angles and a straight angle at P.',
                key='m∠P + m∠Q + m∠R = 180°',
                note=PROOF_RULE + 'Essential: unique parallel through P; the two angles at P next to ∠QPR are congruent to ∠Q and ∠R (alternate interior); the three '
                     'angles at P make 180°.'),
          proof('In triangle ABC, extend side BC past C to point D, and draw ray CE parallel to BA (E on the same side of line BD as A). Prove that the angles of triangle ABC add to 180°.',
                method='Use alternate interior angles (∠A and ∠ACE) and corresponding angles (∠B and ∠ECD), then the straight angle BCD.',
                key='m∠A + m∠B + m∠ACB = 180°',
                note=PROOF_RULE + 'Essential: ∠ACE ≅ ∠A (alternate interior, transversal AC); ∠ECD ≅ ∠B (corresponding, transversal BD); ∠ACB + ∠ACE + ∠ECD = 180° '
                     '(straight angle at C).'),
          sa('A proof of the triangle angle sum (line ℓ through C parallel to AB, making ∠1 next to CA and ∠2 next to CB):\n1. m∠1 + m∠ACB + m∠2 = 180°  (?)\n'
             '2. ∠1 ≅ ∠A and ∠2 ≅ ∠B  (?)\n3. m∠A + m∠ACB + m∠B = 180°  (?)\nGive the three reasons.', 'Reasons:',
             key='1: the angles form a straight angle (angle addition); 2: alternate interior angles are congruent (ℓ ∥ AB); 3: substitution.',
             note='Any equivalent names for all three reasons.'),
          mc('A student proves the angle sum theorem using "an exterior angle equals the sum of the two remote interior angles." What is wrong?',
             ['That theorem is usually proved FROM the angle sum, so the argument is circular', 'Exterior angles do not exist in triangles',
              'The exterior angle theorem is false', 'Nothing is wrong'],
             note='Using a result that depends on the theorem being proved is circular reasoning.'),
      ],
      back=[
          B('Use the angle sum and parallel-line angles informally', '8.G.A.5', [
              sa('Two angles of a triangle are 47° and 68°. Find the third.', 'Angle:', key='65°', note='Any equivalent form.'),
              tf('Tearing off the three corners of a paper triangle and lining them up makes a straight angle.', key=True, note='They add to 180°.'),
              sa('A triangle has angles x, 2x, and 3x. Find x.', 'x =', key='30', note='Any equivalent form. 6x = 180.'),
              mc('Lines ℓ ∥ m are cut by a transversal. An angle at ℓ is 72°. Which angle at m must also be 72°?', ['Its alternate interior angle',
                                                                                                                  'The angle next to it on the same line', 'Its same-side interior angle', 'Every angle at m'],
                 note='Alternate interior angles are congruent.'),
              tf('A triangle can have two obtuse angles.', key=False, note='Two angles over 90° would already add to more than 180°.'),
          ], align='exact',
            why=why('the student does not know the angle sum or the parallel-line angle facts informally.', 'the proof turns this informal fact into a deduction.',
                    'uses the angle sum and parallel-line angle pairs in calculations.')),
          B('Angles that form a straight angle add to 180°', '4.MD.C.7', [
              sa('Three angles together form a straight angle. Two are 40° and 75°. Find the third.', 'Angle:', key='65°', note='Any equivalent form.'),
              tf('The angles around a point on one side of a straight line add to 180°.', key=True, note='They make a straight angle.'),
              mc('∠1, ∠2, and ∠3 form a straight angle, with ∠1 = ∠3 = 50°. Find ∠2.', ['80°', '100°', '50°', '130°'], note='180 - 100 = 80.'),
              sa('Angle ABC is a straight angle. Ray BD makes ∠ABD = 3x and ∠DBC = 2x. Find x.', 'x =', key='36', note='Any equivalent form. 5x = 180.'),
              tf('Two angles that make up a straight angle must be equal.', key=False, note='They add to 180° but can be any pair, such as 30° and 150°.'),
          ], align='exact',
            why=why('the student does not see that the angles at the parallel line form a straight angle.', 'that is the final step of the proof.',
                    'adds angles that make up a straight angle.')),
          B('Alternate interior angles of parallel lines are congruent', 'HSG-CO.C.9', [
              sa('Lines ℓ ∥ m are cut by transversal t. An alternate interior angle of a 58° angle measures', 'Measure:', key='58°', note='Any equivalent form.'),
              tf('Alternate interior angles formed by a transversal of parallel lines are congruent.', key=True, note='This is the theorem proved in an earlier set.'),
              mc('Line ℓ through C is parallel to AB. Which angle at C is congruent to ∠A?', ['The angle between ℓ and CA', 'The angle between ℓ and CB',
                                                                                         '∠ACB', 'The angle between CA and CB'],
                 note='CA is a transversal of ℓ and AB.'),
              sa('Why is it allowed to draw the line through C parallel to AB?', 'Reason:', key='The parallel postulate: through a point not on a line there is exactly one parallel line.',
                 note='Any equivalent wording.'),
              tf('Alternate interior angles are congruent for any two lines cut by a transversal.', key=False, note='Only when the lines are parallel.'),
          ], align='exact',
            why=why('the student cannot justify the key step of the proof.', 'the new angles at C equal ∠A and ∠B because of this theorem.',
                    'uses alternate interior angles and the parallel postulate.')),
      ],
      f1=B('Prove the exterior angle theorem', 'HSG-CO.C.10', [
          proof('In triangle ABC, side BC is extended past C to D. Prove that m∠ACD = m∠A + m∠B.',
                method='Use the linear pair at C and the triangle angle sum.',
                key='m∠ACD = m∠A + m∠B',
                note=PROOF_RULE + 'Essential: m∠ACD + m∠ACB = 180° (linear pair); m∠A + m∠B + m∠ACB = 180° (angle sum); substitute and subtract m∠ACB.'),
          sa('An exterior angle of a triangle measures 125°. One remote interior angle is 48°. Find the other remote interior angle and the adjacent interior angle.', 'Answer:',
             key='Remote interior: 77°; adjacent interior: 55°.', note='Form required: both angles.'),
          tf('An exterior angle of a triangle is always greater than each remote interior angle.', key=True, note='It equals their sum, and each is positive.'),
          mc('The exterior angle at C is (5x + 10)° and the remote interior angles are (2x + 15)° and (2x + 20)°. Find x.', ['25', '15', '35', '5'],
             note='5x + 10 = 4x + 35.'),
          sa('Prove that the three exterior angles of a triangle (one at each vertex) add to 360°.', 'Answer:',
             key='Each exterior angle is 180° minus its interior angle, so the sum is 540° - 180° = 360°.', note='Any valid argument.'),
      ], prog='same-course deepening', demand='Prove a new theorem (the exterior angle theorem) that depends on the angle sum.'),
      f2=B('Generalize the angle sum to polygons', 'HSG-CO.C.10', [
          proof('Prove that the interior angles of any convex polygon with n sides add to (n - 2) · 180°.',
                method='Draw the diagonals from one vertex to divide the polygon into triangles and use the triangle angle sum.',
                key='(n - 2) · 180°',
                note=PROOF_RULE + 'Essential: from one vertex there are n - 3 diagonals, making n - 2 triangles; their angles together make up exactly the polygon\'s angles; '
                     'each triangle contributes 180°.'),
          sa('Find the measure of each interior angle of a regular octagon.', 'Measure:', key='135°', note='Any equivalent form. (8 - 2) · 180 ÷ 8 = 135.'),
          sa('Each interior angle of a regular polygon is 156°. How many sides does it have?', 'Sides:', key='15', note='Any equivalent form. Each exterior angle is 24°; 360 ÷ 24 = 15.'),
          tf('The interior angles of a hexagon add to 720°.', key=True, note='(6 - 2) · 180 = 720.'),
          mc('A pentagon has angles 100°, 110°, 120°, 95°, and x°. Find x.', ['115', '105', '125', '135'], note='540 - 425 = 115.'),
      ], prog='same-course deepening', demand='Generalize the result with a parameter: the angle sum of an n-sided polygon, by dissection into triangles.',
        builds='FORWARD 1 derives one consequence (exterior angles); FORWARD 2 generalizes the theorem to every polygon.')),

    # ------------------------------------------------------------------ 21. CO.C.10 isosceles
    S('HSG-CO.C.10', 'Prove that the base angles of an isosceles triangle are congruent',
      target='Prove that the base angles of an isosceles triangle are congruent', strand='core', covers=['CO10-isosceles'],
      main=[
          proof('In triangle ABC, AB = AC. Prove that ∠B ≅ ∠C. (Draw the bisector of ∠A, meeting BC at D.)', fig=ISO,
                method='Prove △ABD ≅ △ACD by SAS, then use corresponding angles.',
                key='∠B ≅ ∠C',
                note=PROOF_RULE + 'Essential: AB = AC (given); ∠BAD ≅ ∠CAD (definition of angle bisector); AD = AD; △ABD ≅ △ACD (SAS); ∠B ≅ ∠C (corresponding angles). '
                     'Invalid: "∠B and ∠C look equal"; using the fact that AD ⊥ BC (not yet known).'),
          proof('In triangle ABC, AB = AC. Prove that ∠B ≅ ∠C using the midpoint M of BC.', fig=ISO,
                method='Prove △ABM ≅ △ACM by SSS.',
                key='∠B ≅ ∠C',
                note=PROOF_RULE + 'Essential: AB = AC; BM = CM (midpoint); AM = AM; SSS; corresponding angles.'),
          proof('In triangle ABC, AB = AC. Prove that ∠B ≅ ∠C using a rigid motion: the reflection across the bisector of ∠A.', fig=ISO,
                method='Explain where the reflection sends ray AB, point B, and point C.',
                key='The reflection maps ∠ABC onto ∠ACB, so ∠B ≅ ∠C.',
                note='Any valid explanation. Essential: the reflection across the bisector of ∠A swaps rays AB and AC (the bisector makes equal angles with them); '
                     'B goes to the point of ray AC at distance AB = AC, which is C; so B ↔ C and the triangle maps onto itself with ∠B ↔ ∠C.'),
          proof('Prove that every equilateral triangle is equiangular (all three angles are congruent).',
                method='Apply the isosceles base angle theorem twice, with two different pairs of equal sides.',
                key='All three angles are congruent (each is 60°).',
                note=PROOF_RULE + 'Essential: AB = AC gives ∠B ≅ ∠C; AB = BC gives ∠A ≅ ∠C; so all three are congruent (and each is 60° by the angle sum).'),
          mc('In the proof that base angles of isosceles triangle ABC (AB = AC) are congruent, the bisector of ∠A meets BC at D. Which criterion proves △ABD ≅ △ACD?',
             ['SAS', 'SSS', 'ASA', 'AAS'], note='AB = AC, ∠BAD ≅ ∠CAD, and AD is shared: two sides and the included angle.'),
      ],
      back=[
          B('Prove triangles congruent with SAS or SSS', 'HSG-CO.B.8', [
              sa('Two triangles share side AD, and AB = AC, ∠BAD ≅ ∠CAD. Which criterion shows △ABD ≅ △ACD?', 'Criterion:', key='SAS', note='Any equivalent form.'),
              sa('Two triangles share side AM, and AB = AC, BM = CM. Which criterion shows △ABM ≅ △ACM?', 'Criterion:', key='SSS', note='Any equivalent form.'),
              tf('A shared side counts as a pair of congruent sides in a congruence proof.', key=True, note='Reflexive property.'),
              mc('Which information is NOT enough for congruence?', ['Two sides and a non-included angle', 'Three sides', 'Two sides and the included angle',
                                                                     'Two angles and the included side'],
                 note='SSA is not a criterion.'),
              tf('If △ABD ≅ △ACD, then ∠ABD ≅ ∠ACD.', key=True, note='Corresponding angles.'),
          ], align='exact',
            why=why('the student cannot choose or apply a congruence criterion.', 'each proof of the theorem uses SAS or SSS.',
                    'chooses SAS or SSS and states the corresponding parts.')),
          B('Use the definitions of angle bisector and midpoint', 'HSG-CO.A.1', [
              sa('Ray AD bisects ∠BAC, and m∠BAC = 64°. Find m∠BAD.', 'Measure:', key='32°', note='Any equivalent form.'),
              sa('M is the midpoint of BC, and BC = 18. Find BM.', 'BM =', key='9', note='Any equivalent form.'),
              tf('An angle bisector divides an angle into two congruent angles.', key=True, note='Definition.'),
              mc('Ray AD bisects ∠BAC. Which equation is true?', ['m∠BAD = m∠DAC', 'BD = DC', 'AD = AB', 'm∠BAD = m∠BAC'], note='Equal angle measures.'),
              tf('The bisector of ∠A of triangle ABC always passes through the midpoint of BC.', key=False, note='Only when AB = AC.'),
          ], align='supporting',
            why=why('the student does not use the auxiliary line\'s definition as a reason.', 'the proofs depend on the bisector or midpoint giving congruent parts.',
                    'states what a bisector and a midpoint give.')),
          B('Classify triangles and name legs, base, and base angles', '4.G.A.2', [
              sa('Triangle PQR has PQ = PR. Name the base and the base angles.', 'Answer:', key='Base QR; base angles ∠Q and ∠R', note='Any equivalent form.'),
              tf('An isosceles triangle has at least two congruent sides.', key=True, note='Definition used in this course.'),
              mc('Which triangle is scalene?', ['Sides 4, 5, 6', 'Sides 4, 4, 6', 'Sides 5, 5, 5', 'Sides 3, 3, 3'], note='No two sides are equal.'),
              sa('In isosceles triangle XYZ with XY = XZ, which angle is the vertex angle?', 'Angle:', key='∠X', note='Any equivalent form.'),
              tf('Every equilateral triangle is isosceles.', key=True, note='It has at least two congruent sides.'),
          ], align='supporting',
            why=why('the student does not know which angles are the base angles.', 'the theorem is about the angles opposite the congruent sides.',
                    'names legs, base, and base angles.')),
      ],
      f1=B('Prove the converse: congruent base angles give congruent sides', 'HSG-CO.C.10', [
          proof('In triangle ABC, ∠B ≅ ∠C. Prove that AB = AC.',
                method='Draw the bisector of ∠A meeting BC at D and prove △ABD ≅ △ACD by AAS.',
                key='AB = AC',
                note=PROOF_RULE + 'Essential: ∠B ≅ ∠C (given); ∠BAD ≅ ∠CAD (bisector); AD = AD; AAS; AB = AC. Invalid: using AB = AC to choose the auxiliary line.'),
          sa('In triangle PQR, m∠Q = 70° and m∠R = 70°, and PQ = 3x + 2, PR = 5x - 6. Find x and PQ.', 'Answer:', key='x = 4; PQ = 14', note='Form required: x and PQ.'),
          tf('A triangle with two congruent angles must have two congruent sides.', key=True, note='This is the converse of the isosceles triangle theorem.'),
          mc('Triangle ABC has m∠A = 50° and m∠B = 65°. Which two sides are congruent?', ['AB and AC', 'AB and BC', 'AC and BC', 'No two sides'],
             note='m∠C = 65° = m∠B, so the sides opposite them, AC and AB, are congruent.'),
          proof('Prove that every equiangular triangle is equilateral.', method='Apply the converse twice.',
                key='All three sides are congruent.',
                note=PROOF_RULE + 'Essential: ∠A ≅ ∠B gives BC = AC; ∠B ≅ ∠C gives AC = AB; so all three sides are congruent.'),
      ], prog='same-course deepening', demand='Prove the converse theorem (from angles to sides), which needs a different congruence criterion (AAS).'),
      f2=B('Use isosceles triangle theorems in multistep problems and proofs', 'HSG-CO.C.10', [
          sa('In triangle ABC, AB = AC and the vertex angle ∠A measures 38°. Find m∠B.', 'Measure:', key='71°', note='Any equivalent form. (180 - 38) ÷ 2.'),
          sa('Point D is on side BC of triangle ABC with AD = BD = CD. Find m∠BAC.', 'Measure:', key='90°',
             note='Any equivalent form. Triangles ABD and ACD are isosceles, so ∠BAD = ∠B and ∠CAD = ∠C; then 2(∠B + ∠C) = 180.'),
          proof('In triangle ABC, AB = AC, and D and E are points on BC with BD = CE. Prove that AD = AE.',
                method='Use the base angles and SAS on triangles ABD and ACE.',
                key='AD = AE',
                note=PROOF_RULE + 'Essential: ∠B ≅ ∠C (base angles); AB = AC; BD = CE; △ABD ≅ △ACE (SAS); AD = AE.'),
          tf('If the vertex angle of an isosceles triangle is 100°, each base angle is 40°.', key=True, note='(180 - 100) ÷ 2 = 40.'),
          mc('In isosceles triangle PQR with PQ = PR, the exterior angle at Q (on the extension of RQ past Q) is 112°. Find m∠P.', ['44°', '68°', '56°', '112°'],
             note='∠PQR = 68° = ∠R, so ∠P = 180 - 136 = 44.'),
      ], prog='same-course deepening', demand='Use the theorem and its converse as steps inside longer calculations and proofs.',
        builds='Builds on FORWARD 1: both directions of the theorem are used together in multistep reasoning.')),
]

MIDSEG = gd({'A': (0, 0), 'B': (5, 0), 'C': (1.8, 3.2), 'D': (0.9, 1.6), 'E': (3.4, 1.6)},
            [('poly', ['A', 'B', 'C']), ('seg', 'D', 'E'), ('seg', 'A', 'D', {'ticks': 1}), ('seg', 'D', 'C', {'ticks': 1}),
             ('seg', 'C', 'E', {'ticks': 2}), ('seg', 'E', 'B', {'ticks': 2})], h=200,
            desc='Triangle ABC. D is the midpoint of AC and E is the midpoint of BC (tick marks show AD = DC and CE = EB). Segment DE joins the midpoints.')
PGRAM = gd({'A': (0, 0), 'B': (4.5, 0), 'C': (6, 2.6), 'D': (1.5, 2.6)},
           [('poly', ['A', 'B', 'C', 'D']), ('seg', 'A', 'B', {'arrows': 1}), ('seg', 'D', 'C', {'arrows': 1}),
            ('seg', 'A', 'D', {'arrows': 2}), ('seg', 'B', 'C', {'arrows': 2})], h=190,
           desc='Parallelogram ABCD: AB ∥ DC (one arrow mark each) and AD ∥ BC (two arrow marks each).')
PGRAM_D = gd({'A': (0, 0), 'B': (4.5, 0), 'C': (6, 2.6), 'D': (1.5, 2.6), 'E': (3, 1.3)},
             [('poly', ['A', 'B', 'C', 'D']), ('seg', 'A', 'C'), ('seg', 'B', 'D'), ('seg', 'A', 'B', {'arrows': 1}), ('seg', 'D', 'C', {'arrows': 1}),
              ('seg', 'A', 'D', {'arrows': 2}), ('seg', 'B', 'C', {'arrows': 2})], lab={'E': 's'}, h=190,
             desc='Parallelogram ABCD (AB ∥ DC and AD ∥ BC, shown by arrows) with diagonals AC and BD crossing at E.')
QUAD_D = gd({'A': (0, 0), 'B': (4.5, 0), 'C': (6, 2.6), 'D': (1.5, 2.6), 'E': (3, 1.3)},
            [('poly', ['A', 'B', 'C', 'D']), ('seg', 'A', 'C'), ('seg', 'B', 'D')], lab={'E': 's'}, h=190,
            desc='Quadrilateral ABCD with diagonals AC and BD crossing at E. No sides are marked parallel.')
RECT = gd({'A': (0, 0), 'B': (5, 0), 'C': (5, 2.6), 'D': (0, 2.6)},
          [('poly', ['A', 'B', 'C', 'D']), ('seg', 'A', 'C'), ('seg', 'B', 'D'), ('ra', 'A', 'B', 'D'), ('ra', 'B', 'C', 'A'), ('ra', 'C', 'D', 'B'), ('ra', 'D', 'A', 'C')],
          h=180, desc='Rectangle ABCD with right-angle marks at all four vertices and diagonals AC and BD drawn.')

SETS += [
    # ------------------------------------------------------------------ 22. CO.C.10 midsegment
    S('HSG-CO.C.10', 'Prove the midsegment theorem',
      target='Prove that the segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long',
      strand='core', covers=['CO10-midseg'],
      main=[
          proof('Triangle ABC has A(0, 0), B(2a, 0), and C(2b, 2c), with a > 0 and c ≠ 0. D is the midpoint of AC and E is the midpoint of BC. Prove that DE ∥ AB and DE = ½AB.',
                method='Find D and E with the midpoint formula, then compare slopes and lengths.',
                key='D(b, c), E(a + b, c); DE is horizontal like AB, and DE = a = ½(2a) = ½AB.',
                note=PROOF_RULE + 'Essential: both midpoints; DE has slope 0 (same y) and AB has slope 0, so DE ∥ AB (and DE ≠ AB since c ≠ 0); DE = |a + b - b| = a '
                     'and AB = 2a. Invalid: checking one numerical triangle only.'),
          proof('In triangle ABC, D is the midpoint of AC and E is the midpoint of BC. Extend DE past E to F so that EF = DE. Prove that DE ∥ AB and DE = ½AB.', fig=MIDSEG,
                method='Prove △DEC ≅ △FEB (SAS), deduce BF = DC = AD and BF ∥ AD, so ABFD is a parallelogram; then use its opposite sides.',
                key='DE ∥ AB and DE = ½AB',
                note=PROOF_RULE + 'Essential: CE = BE, DE = FE, vertical angles at E, so △DEC ≅ △FEB (SAS); BF = DC = AD; ∠DCE ≅ ∠FBE gives BF ∥ AC (alternate '
                     'interior converse); one pair of opposite sides of ABFD is parallel and congruent, so ABFD is a parallelogram; so DF ∥ AB and DF = AB; '
                     'DE = ½DF = ½AB.'),
          sa('In the coordinate proof of the midsegment theorem, the vertices are A(0, 0), B(2a, 0), C(2b, 2c). Why are the coordinates written with 2a, 2b, and 2c?',
             'Answer:', key='So the midpoints have whole-letter coordinates (a, b, c) without fractions, which keeps the algebra simple; any triangle can still be placed this way.',
             note='Any equivalent explanation that mentions avoiding fractions in the midpoint formula and that the placement is general.'),
          sa('A proof of the midsegment theorem with A(0, 0), B(2a, 0), C(2b, 2c):\n1. D = (b, c), E = (a + b, c)  (?)\n2. slope DE = 0 = slope AB  (?)\n3. DE ∥ AB  (?)\n'
             '4. DE = a and AB = 2a, so DE = ½AB  (?)\nGive the four reasons.', 'Reasons:',
             key='1: midpoint formula; 2: slope formula (equal y-coordinates); 3: lines with equal slopes are parallel; 4: distance formula (horizontal distances).',
             note='Any equivalent names for all four reasons.'),
          mc('A student checks the triangle A(0, 0), B(6, 0), C(2, 4), finds the midsegment is parallel to AB and 3 units long, and concludes the theorem is proved. What is the flaw?',
             ['One example cannot prove a statement about every triangle', 'The midsegment should be 6 units long', 'The midsegment is not parallel to AB',
              'Midpoints cannot be found with coordinates'],
             note='A general proof must work for every triangle, for example with variable coordinates.'),
      ],
      back=[
          B('Find midpoints of segments in the coordinate plane', '6.G.A.3', [
              sa('Find the midpoint of the segment from (2, 6) to (8, 2).', 'Midpoint:', key='(5, 4)', note='Form required: an ordered pair. Average the coordinates.'),
              sa('Find the midpoint of the segment from (-3, 1) to (5, -7).', 'Midpoint:', key='(1, -3)', note='Form required: an ordered pair.'),
              sa('Find the midpoint of the segment from (0, 0) to (2a, 2c).', 'Midpoint:', key='(a, c)', note='Any equivalent form.'),
              tf('The midpoint of the segment from (1, 1) to (7, 1) is (4, 1).', key=True, note='((1 + 7) ÷ 2, 1).'),
              tf('The midpoint of the segment from (0, 4) to (6, 0) is (6, 4).', key=False, note='It is (3, 2).'),
          ], align='supporting',
            why=why('the student cannot find midpoints, especially with letters.', 'the coordinate proof starts from the two midpoints.',
                    'averages coordinates, including variable coordinates.')),
          B('Find and compare slopes to decide whether lines are parallel', '8.EE.B.6', [
              sa('Find the slope of the line through (1, 2) and (4, 8).', 'Slope:', key='2', note='Any equivalent form. (8 - 2) ÷ (4 - 1).'),
              sa('Find the slope of the line through (b, c) and (a + b, c).', 'Slope:', key='0', note='Any equivalent form. The y-coordinates are equal.'),
              tf('Two different nonvertical lines with the same slope are parallel.', key=True, note='Same steepness, different positions.'),
              mc('Which segment is parallel to the segment from (0, 0) to (4, 2)?', ['From (1, 3) to (5, 5)', 'From (1, 3) to (3, 7)', 'From (0, 0) to (2, -1)', 'From (2, 2) to (2, 6)'],
                 note='Both have slope 1/2.'),
              tf('A horizontal segment and a vertical segment have the same slope.', key=False, note='Horizontal has slope 0; vertical is undefined.'),
          ], align='exact',
            why=why('the student cannot test parallelism with slopes.', 'the coordinate proof shows DE ∥ AB by equal slopes.', 'computes and compares slopes.')),
          B('Find lengths with the distance formula', '8.G.B.8', [
              sa('Find the distance between (b, c) and (a + b, c), with a > 0.', 'Distance:', key='a (that is, |a|, with a > 0)', note='Any equivalent form.'),
              sa('Find the distance between (0, 0) and (6, 8).', 'Distance:', key='10', note='Any equivalent form.'),
              mc('Find the length of the segment from (-2, 5) to (4, 5).', ['6', '2', '10', '3'], note='Horizontal: |4 - (-2)| = 6.'),
              tf('The distance from (1, 2) to (4, 6) is 5.', key=True, note='√(9 + 16) = 5.'),
              tf('The distance from (0, 0) to (2a, 0) is a, when a > 0.', key=False, note='It is 2a.'),
          ], align='exact',
            why=why('the student cannot compare the lengths of DE and AB.', 'the "half as long" part needs both lengths.', 'finds lengths, including with variables.')),
          B('Prove lines parallel from congruent alternate interior angles', 'HSG-CO.C.9', [
              sa('Lines ℓ and m are cut by a transversal, and alternate interior angles are congruent. What can you conclude?', 'Answer:', key='ℓ ∥ m', note='Any equivalent form.'),
              tf('If two lines are cut by a transversal and alternate interior angles are congruent, the lines are parallel.', key=True, note='Converse of the alternate interior angles theorem.'),
              mc('In the synthetic midsegment proof, which fact shows BF ∥ AC?', ['∠DCE ≅ ∠FBE are alternate interior angles', 'BF = DC',
                                                                                  'E is the midpoint of BC', 'DE = EF'],
                 note='Congruent alternate interior angles (transversal BC) give parallel lines.'),
              sa('Two lines are cut by a transversal and corresponding angles measure 70° and 70°. Are the lines parallel?', 'Answer:', key='Yes', note='Any equivalent answer.'),
              tf('Congruent vertical angles prove that two lines are parallel.', key=False, note='Vertical angles are congruent for any crossing lines.'),
          ], align='exact',
            why=why('the student cannot justify a parallel conclusion in the synthetic proof.', 'the proof shows BF ∥ AC this way.',
                    'uses the converse to conclude lines are parallel.')),
      ],
      f1=B('Prove that the midpoints of a quadrilateral\'s sides form a parallelogram', 'HSG-CO.C.11', [
          proof('ABCD is any quadrilateral, and P, Q, R, S are the midpoints of AB, BC, CD, DA. Prove that PQRS is a parallelogram.',
                method='Draw diagonal AC and apply the midsegment theorem in triangles ABC and ADC.',
                key='PQ ∥ AC ∥ SR and PQ = ½AC = SR, so PQRS is a parallelogram.',
                note=PROOF_RULE + 'Essential: in △ABC, PQ ∥ AC and PQ = ½AC; in △ADC, SR ∥ AC and SR = ½AC; so PQ ∥ SR and PQ = SR; a quadrilateral with one pair '
                     'of opposite sides parallel and congruent is a parallelogram.'),
          sa('Quadrilateral ABCD has diagonals AC = 10 and BD = 14. Find the perimeter of the quadrilateral formed by the midpoints of its sides.', 'Perimeter:', key='24',
             note='Any equivalent form. Its sides are ½AC, ½BD, ½AC, ½BD: 5 + 7 + 5 + 7.'),
          tf('The midpoint quadrilateral of any quadrilateral is a parallelogram.', key=True, note='This is Varignon\'s theorem.'),
          mc('If the diagonals of ABCD are perpendicular, the midpoint quadrilateral is a', ['rectangle', 'rhombus', 'trapezoid that is not a parallelogram', 'kite that is not a parallelogram'],
             note='Its sides are parallel to the diagonals, so adjacent sides are perpendicular.'),
          sa('In triangle ABC, D, E, F are the midpoints of AB, BC, CA. AB = 12, BC = 16, CA = 10. Find the perimeter of triangle DEF.', 'Perimeter:', key='19',
             note='Any equivalent form. Each midsegment is half the parallel side: 6 + 8 + 5.'),
      ], prog='cross-standard extension', demand='Use the midsegment theorem twice inside a new proof about quadrilaterals.'),
      f2=B('Midsegment triangles: similarity, scale factor, and area', 'HSG-SRT.A.2', [
          sa('D, E, F are the midpoints of the sides of triangle ABC. Explain why triangle DEF is similar to triangle ABC, and give the scale factor.', 'Answer:',
             key='Each side of DEF is half of a side of ABC (midsegment theorem), so the triangles are similar by SSS similarity with scale factor ½.',
             note='Any equivalent explanation with the factor ½ (or 2 from DEF to ABC).'),
          sa('Triangle ABC has area 48. Find the area of the triangle formed by the midpoints of its sides.', 'Area:', key='12',
             note='Any equivalent form. Scale factor ½ gives area factor ¼; also the 4 small triangles are congruent.'),
          tf('The four triangles formed by drawing all three midsegments of a triangle are congruent.', key=True, note='Each has sides ½AB, ½BC, ½CA (SSS).'),
          mc('The midsegment parallel to AB in triangle ABC is 9. A line segment connects the midpoints of that midsegment\'s triangle the same way. How long is the new segment parallel to AB?',
             ['4.5', '9', '18', '3'], note='Each repetition halves the length.'),
          sa('Triangle ABC has vertices A(0, 0), B(8, 0), C(2, 6). Find the vertices of its midsegment triangle and verify the ratio of areas.', 'Answer:',
             key='(4, 0), (5, 3), (1, 3); area of ABC = 24 and area of the midsegment triangle = 6, a ratio of 1 : 4.',
             note='Form required: the three midpoints and both areas.'),
      ], prog='cross-standard extension', demand='Connect the midsegment theorem to similarity: scale factor ½ and the area ratio ¼.',
        builds='FORWARD 1 uses midsegments to prove a parallelogram; FORWARD 2 measures how the midsegment figure compares in size (similarity and area).')),

    # ------------------------------------------------------------------ 23. CO.C.10 medians
    S('HSG-CO.C.10', 'Prove that the medians of a triangle meet at one point',
      target='Prove that the three medians of any triangle meet at one point', strand='core', covers=['CO10-medians'],
      main=[
          proof('Triangle ABC has A(0, 0), B(2b, 0), and C(2c, 2d), with b ≠ 0 and d ≠ 0. Prove that the point G((2b + 2c)/3, 2d/3) lies on all three medians.',
                method='Find the midpoint of each side, then show G is two-thirds of the way from each vertex to the opposite midpoint (or on each median line).',
                key='G is on the median from A (to (b + c, d)), from B (to (c, d)), and from C (to (b, 0)), so the medians meet at G.',
                note=PROOF_RULE + 'Essential: the three midpoints (b + c, d), (c, d), (b, 0); for each median, G = vertex + ⅔(midpoint - vertex): '
                     'A + ⅔((b + c, d) - A) = G; B + ⅔((c, d) - (2b, 0)) = G; C + ⅔((b, 0) - (2c, 2d)) = G. Alternative: show G satisfies each median\'s '
                     'equation. Invalid: checking one triangle with numbers.'),
          proof('In triangle ABC, medians BE and CF meet at G. Let H and K be the midpoints of BG and CG. Prove that BG = 2GE. Then explain why the third median also passes through G.',
                method='Use the midsegment theorem in triangles ABC and GBC to show FEKH is a parallelogram, then its diagonals.',
                key='BG = 2GE; the same argument for medians AD and BE gives the point that is two-thirds along BE, which is G, so AD passes through G.',
                note=PROOF_RULE + 'Essential: FE ∥ BC and FE = ½BC (midsegment in △ABC); HK ∥ BC and HK = ½BC (midsegment in △GBC); so FEKH is a parallelogram; its '
                     'diagonals bisect each other, so HG = GE; with BH = HG, BG = 2GE; any two medians meet at the point two-thirds along each, so all three share it.'),
          sa('Explain why proving that the point two-thirds of the way along EACH median is the same point proves that the three medians meet at one point.', 'Explanation:',
             key='Each median contains its own two-thirds point. If those three points are one point, that point lies on all three medians, so they meet there.',
             note='Any equivalent explanation.'),
          proof('Triangle PQR has P(0, 0), Q(6, 0), and R(0, 6). Find the three medians\' equations and prove that they meet at one point.',
                method='Find each median as a line through a vertex and a midpoint, find where two meet, and check that the third passes through that point.',
                key='The medians meet at (2, 2).',
                note=PROOF_RULE + 'Essential: midpoints (3, 3), (0, 3), (3, 0); medians y = x, y = -½x + 3 (from Q), y = -2x + 6 (from R); y = x and y = -2x + 6 meet at (2, 2); '
                     '(2, 2) satisfies y = -½x + 3. (This proves the claim for this triangle; the general proof needs variables.)'),
          tf('Drawing medians carefully in three different triangles and seeing that they meet proves that the medians of every triangle meet at one point.', key=False,
             note='Examples suggest a theorem but cannot prove it for every triangle.'),
      ],
      back=[
          B('Find midpoints, including with variables', '6.G.A.3', [
              sa('Find the midpoint of the segment from (2b, 0) to (2c, 2d).', 'Midpoint:', key='(b + c, d)', note='Any equivalent form.'),
              sa('Find the midpoint of the segment from (0, 6) to (6, 0).', 'Midpoint:', key='(3, 3)', note='Form required: an ordered pair.'),
              mc('A median of a triangle joins a vertex to', ['the midpoint of the opposite side', 'the midpoint of an adjacent side',
                                                             'the foot of the perpendicular from that vertex', 'another vertex'],
                 note='Definition of a median.'),
              tf('A triangle has exactly three medians.', key=True, note='One from each vertex.'),
              tf('A median always bisects the angle at its vertex.', key=False, note='Only in special cases (for example, the vertex angle of an isosceles triangle).'),
          ], align='supporting',
            why=why('the student cannot locate the endpoints of the medians.', 'every median ends at a midpoint.', 'finds midpoints and identifies medians.')),
          B('Use the midsegment theorem', 'HSG-CO.C.10', [
              sa('In triangle ABC, F and E are the midpoints of AB and AC. BC = 14. Find FE.', 'FE =', key='7', note='Any equivalent form.'),
              tf('The segment joining the midpoints of two sides of a triangle is parallel to the third side.', key=True, note='Midsegment theorem.'),
              mc('In triangle GBC, H and K are midpoints of GB and GC. Which statement is true?', ['HK ∥ BC and HK = ½BC', 'HK ∥ GB', 'HK = BC', 'HK ⊥ BC'],
                 note='Midsegment theorem in triangle GBC.'),
              sa('A midsegment of a triangle is 11 cm. How long is the side parallel to it?', 'Length:', key='22 cm', note='Any equivalent form.'),
              tf('A midsegment of a triangle is always half as long as each of the other two sides.', key=False, note='Only half as long as the side it is parallel to.'),
          ], align='exact',
            why=why('the student does not apply the midsegment theorem.', 'the synthetic proof uses it twice.', 'uses the theorem for lengths and parallelism.')),
          B('Find the point a given fraction of the way along a segment', '7.RP.A.2', [
              sa('On a number line, what point is ⅔ of the way from 0 to 9?', 'Point:', key='6', note='Any equivalent form.'),
              sa('On a number line, what point is ⅔ of the way from 3 to 12?', 'Point:', key='9', note='Any equivalent form. 3 + ⅔(9).'),
              mc('A point is ⅔ of the way from A to D. What is the ratio of its distances from A and from D?', ['2 : 1', '1 : 2', '2 : 3', '3 : 2'], note='⅔ and ⅓ of the length.'),
              tf('The point ⅔ of the way from (0, 0) to (6, 3) is (4, 2).', key=True, note='⅔ of each coordinate.'),
              tf('The point ⅔ of the way from (0, 0) to (3, 6) is (2, 2).', key=False, note='It is (2, 4).'),
          ], align='supporting',
            why=why('the student cannot find a point two-thirds of the way along a segment.', 'the medians meet at the two-thirds point of each.',
                    'computes points at a fractional distance along segments.')),
          B('Write the equation of a line through two points', '8.F.B.4', [
              sa('Write an equation of the line through (0, 0) and (3, 3).', 'Equation:', key='y = x', note='Any equivalent equation.'),
              sa('Write an equation of the line through (6, 0) and (0, 3).', 'Equation:', key='y = -½x + 3', note='Any equivalent equation.'),
              mc('Which point is on the line y = -2x + 6?', ['(2, 2)', '(1, 2)', '(3, 3)', '(0, 2)'], note='-2(2) + 6 = 2.'),
              tf('The line through (0, 6) and (3, 0) has slope -2.', key=True, note='(0 - 6) ÷ (3 - 0).'),
              tf('The line y = x passes through (2, 3).', key=False, note='2 ≠ 3.'),
          ], align='exact',
            why=why('the student cannot write a median as a line.', 'the coordinate method shows a point is on each median line.', 'writes and checks line equations.')),
      ],
      f1=B('Locate the centroid and use the 2 : 1 ratio', 'HSG-GPE.B.6', [
          sa('Find the point where the medians of the triangle with vertices (1, 2), (7, 4), and (4, 9) meet.', 'Point:', key='(4, 5)', note='Form required: an ordered pair. Average the vertices.'),
          sa('Median AD of a triangle is 18 cm long. How far is the centroid from A and from D?', 'Answer:', key='12 cm from A and 6 cm from D', note='Form required: both distances.'),
          tf('The centroid divides each median so that the part from the vertex is twice the part from the midpoint.', key=True, note='The 2 : 1 ratio.'),
          mc('G is the centroid of triangle ABC, and GE = 5 on median BE. Find BE.', ['15', '10', '7.5', '20'], note='BG = 10, so BE = 15.'),
          sa('Explain why the centroid of a triangle is the average of its three vertices.', 'Explanation:',
             key='The centroid is ⅔ of the way from A to the midpoint of BC: A + ⅔((B + C)/2 - A) = (A + B + C)/3.', note='Any equivalent derivation.'),
      ], prog='cross-standard extension', demand='Use the concurrency point quantitatively: find the centroid and apply the 2 : 1 division of each median.'),
      f2=B('Prove that the angle bisectors of a triangle meet at one point', 'HSG-C.A.3', [
          proof('Prove that the bisectors of the three angles of triangle ABC meet at one point that is equidistant from the three sides.',
                method='Use the fact that a point on an angle bisector is equidistant from the angle\'s sides, and its converse.',
                key='The three angle bisectors meet at one point I, equidistant from all three sides.',
                note=PROOF_RULE + 'Essential: the bisectors of ∠A and ∠B meet at I; I is equidistant from AB and AC, and from AB and BC; so it is equidistant from AC and BC; '
                     'by the converse it lies on the bisector of ∠C.'),
          sa('Why must the bisectors of ∠A and ∠B of a triangle meet inside the triangle?', 'Answer:',
             key='Each bisector goes from its vertex into the triangle\'s interior and reaches the opposite side, so the two bisectors cross inside the triangle.',
             note='Any reasonable explanation.'),
          tf('A point on the bisector of an angle is equidistant from the two sides of the angle.', key=True, note='Proved with congruent right triangles (AAS).'),
          mc('The point where the angle bisectors of a triangle meet is the center of the', ['inscribed circle', 'circumscribed circle', 'nine-point circle', 'largest square inside the triangle'],
             note='It is equidistant from the sides.'),
          tf('The angle bisectors and the medians of every triangle meet at the same point.', key=False, note='Only in an equilateral triangle in general.'),
      ], prog='cross-standard extension', demand='Prove a different concurrency theorem (angle bisectors) with the same strategy of two lines meeting and a converse.',
        builds='A second, separate extension of MAIN: FORWARD 1 measures with the centroid; FORWARD 2 proves concurrency of a different set of lines.')),
]
