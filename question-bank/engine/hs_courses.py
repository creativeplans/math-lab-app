"""High-school course placement for course collections (Algebra I first; Geometry, Algebra II, Probability &
Statistics, and Precalculus later).

Common Core groups high-school standards by conceptual category, not by course. This bank places them in courses
following the Common Core "traditional pathway" (CCSS Appendix A: Algebra I, Geometry, Algebra II), with two choices
of its own, documented here so they can be changed in one place:
  - Inference, probability, and the normal distribution (S-IC, S-CP, S-MD, S-ID.A.4) are placed in the planned
    Probability & Statistics course. (Appendix A puts S-CP in Geometry and S-IC and S-ID.4 in Algebra II.)
  - Every (+) standard, which Appendix A leaves out of the three required courses, is placed in Precalculus.
A standard code may be shared by two courses in Appendix A (for example A-REI.D.11 in Algebra I and Algebra II). A
code that belongs to Algebra I is always placed in Algebra I, so a forward branch never uses an Algebra I code.
"""

COURSES = ['Algebra I', 'Geometry', 'Algebra II', 'Probability & Statistics', 'Precalculus']
RANK = {c: i for i, c in enumerate(COURSES)}

# Traditional pathway, Algebra I (CCSS Appendix A), as leaf standard codes in this bank's format.
ALGEBRA_I = [
    'HSN-RN.A.1', 'HSN-RN.A.2', 'HSN-RN.B.3',
    'HSN-Q.A.1', 'HSN-Q.A.2', 'HSN-Q.A.3',
    'HSA-SSE.A.1.a', 'HSA-SSE.A.1.b', 'HSA-SSE.A.2', 'HSA-SSE.B.3.a', 'HSA-SSE.B.3.b', 'HSA-SSE.B.3.c',
    'HSA-APR.A.1',
    'HSA-CED.A.1', 'HSA-CED.A.2', 'HSA-CED.A.3', 'HSA-CED.A.4',
    'HSA-REI.A.1', 'HSA-REI.B.3', 'HSA-REI.B.4.a', 'HSA-REI.B.4.b', 'HSA-REI.C.5', 'HSA-REI.C.6', 'HSA-REI.C.7',
    'HSA-REI.D.10', 'HSA-REI.D.11', 'HSA-REI.D.12',
    'HSF-IF.A.1', 'HSF-IF.A.2', 'HSF-IF.A.3', 'HSF-IF.B.4', 'HSF-IF.B.5', 'HSF-IF.B.6',
    'HSF-IF.C.7.a', 'HSF-IF.C.7.b', 'HSF-IF.C.7.e', 'HSF-IF.C.8.a', 'HSF-IF.C.8.b', 'HSF-IF.C.9',
    'HSF-BF.A.1.a', 'HSF-BF.A.1.b', 'HSF-BF.A.2', 'HSF-BF.B.3', 'HSF-BF.B.4.a',
    'HSF-LE.A.1.a', 'HSF-LE.A.1.b', 'HSF-LE.A.1.c', 'HSF-LE.A.2', 'HSF-LE.A.3', 'HSF-LE.B.5',
    'HSS-ID.A.1', 'HSS-ID.A.2', 'HSS-ID.A.3', 'HSS-ID.B.5', 'HSS-ID.B.6.a', 'HSS-ID.B.6.b', 'HSS-ID.B.6.c',
    'HSS-ID.C.7', 'HSS-ID.C.8', 'HSS-ID.C.9',
]
# Geometry (traditional pathway, CCSS Appendix A): every HSG standard that is not marked (+), as leaf codes.
GEOMETRY = [
    'HSG-CO.A.1', 'HSG-CO.A.2', 'HSG-CO.A.3', 'HSG-CO.A.4', 'HSG-CO.A.5',
    'HSG-CO.B.6', 'HSG-CO.B.7', 'HSG-CO.B.8',
    'HSG-CO.C.9', 'HSG-CO.C.10', 'HSG-CO.C.11',
    'HSG-CO.D.12', 'HSG-CO.D.13',
    'HSG-SRT.A.1.a', 'HSG-SRT.A.1.b', 'HSG-SRT.A.2', 'HSG-SRT.A.3',
    'HSG-SRT.B.4', 'HSG-SRT.B.5',
    'HSG-SRT.C.6', 'HSG-SRT.C.7', 'HSG-SRT.C.8',
    'HSG-C.A.1', 'HSG-C.A.2', 'HSG-C.A.3', 'HSG-C.B.5',
    'HSG-GPE.A.1', 'HSG-GPE.A.2', 'HSG-GPE.B.4', 'HSG-GPE.B.5', 'HSG-GPE.B.6', 'HSG-GPE.B.7',
    'HSG-GMD.A.1', 'HSG-GMD.A.3', 'HSG-GMD.B.4',
    'HSG-MG.A.1', 'HSG-MG.A.2', 'HSG-MG.A.3',
]
# The HSG standards marked (+). The Geometry collection teaches them in a separate ADVANCED EXTENSION strand
# (enrichment, not core mastery). In every other collection they stay in Precalculus, as before.
GEOMETRY_PLUS = ['HSG-SRT.D.9', 'HSG-SRT.D.10', 'HSG-SRT.D.11', 'HSG-C.A.4', 'HSG-GPE.A.3', 'HSG-GMD.A.2']
# Algebra II course profile (the Algebra II collection; see algebra2/README.md for sources and decisions).
# CORE: every standard of the Common Core traditional-pathway Algebra II course (CCSS Appendix A), including the (+)
# standards that the pathway itself lists (N-CN.8, N-CN.9, A-APR.5, A-APR.7, S-MD.6, S-MD.7) and the codes that the
# pathway shares with Algebra I (revisited with new function families; F-IF.8 is taken as its exponential part, 8b).
ALGEBRA_II_CORE = [
    'HSN-CN.A.1', 'HSN-CN.A.2', 'HSN-CN.C.7', 'HSN-CN.C.8', 'HSN-CN.C.9',
    'HSA-SSE.A.1.a', 'HSA-SSE.A.1.b', 'HSA-SSE.A.2', 'HSA-SSE.B.4',
    'HSA-APR.A.1', 'HSA-APR.B.2', 'HSA-APR.B.3', 'HSA-APR.C.4', 'HSA-APR.C.5', 'HSA-APR.D.6', 'HSA-APR.D.7',
    'HSA-CED.A.1', 'HSA-CED.A.2', 'HSA-CED.A.3', 'HSA-CED.A.4', 'HSA-REI.A.2', 'HSA-REI.D.11',
    'HSF-IF.B.4', 'HSF-IF.B.5', 'HSF-IF.B.6', 'HSF-IF.C.7.b', 'HSF-IF.C.7.c', 'HSF-IF.C.7.e', 'HSF-IF.C.8.b', 'HSF-IF.C.9',
    'HSF-BF.A.1.b', 'HSF-BF.B.3', 'HSF-BF.B.4.a', 'HSF-LE.A.4',
    'HSF-TF.A.1', 'HSF-TF.A.2', 'HSF-TF.B.5', 'HSF-TF.C.8',
    'HSS-ID.A.4', 'HSS-IC.A.1', 'HSS-IC.A.2', 'HSS-IC.B.3', 'HSS-IC.B.4', 'HSS-IC.B.5', 'HSS-IC.B.6',
    'HSS-MD.B.6', 'HSS-MD.B.7',
]
# ADVANCED EXTENSION: official (+) standards beyond the pathway baseline, chosen by this bank as natural continuations
# of Algebra II work (a local decision, not an official assignment).
ALGEBRA_II_ADVANCED = [
    'HSN-CN.A.3', 'HSF-IF.C.7.d', 'HSF-BF.A.1.c', 'HSF-BF.B.4.b', 'HSF-BF.B.4.c', 'HSF-BF.B.4.d', 'HSF-BF.B.5',
    'HSF-TF.A.3', 'HSF-TF.A.4', 'HSF-TF.B.6', 'HSF-TF.B.7',
]
# Every Common Core standard marked (+) that this bank uses outside Precalculus or Geometry's list.
OFFICIAL_PLUS_EXTRA = {'HSN-CN.A.3', 'HSN-CN.B.4', 'HSN-CN.B.5', 'HSN-CN.B.6', 'HSS-MD.A.1', 'HSS-MD.A.2', 'HSS-MD.A.3',
                       'HSS-MD.A.4', 'HSS-MD.B.5', 'HSS-MD.B.5.a', 'HSS-MD.B.5.b', 'HSS-MD.B.6', 'HSS-MD.B.7', 'HSS-CP.B.8',
                       'HSS-CP.B.9'}
# Probability & Statistics course profile (the Probability & Statistics collection). CORE: every HSS standard that is not
# marked (+). ADVANCED EXTENSION: every HSS standard officially marked (+) (S-CP.B.8-9 and all of S-MD). The S-ID codes are
# shared with Algebra I and several S-IC/S-MD codes with the Algebra II collection; this course assesses them again with
# its own questions and IDs (see probstat/README.md).
PROB_STAT_CORE = [
    'HSS-ID.A.1', 'HSS-ID.A.2', 'HSS-ID.A.3', 'HSS-ID.A.4', 'HSS-ID.B.5', 'HSS-ID.B.6', 'HSS-ID.B.6.a', 'HSS-ID.B.6.b', 'HSS-ID.B.6.c',
    'HSS-ID.C.7', 'HSS-ID.C.8', 'HSS-ID.C.9',
    'HSS-IC.A.1', 'HSS-IC.A.2', 'HSS-IC.B.3', 'HSS-IC.B.4', 'HSS-IC.B.5', 'HSS-IC.B.6',
    'HSS-CP.A.1', 'HSS-CP.A.2', 'HSS-CP.A.3', 'HSS-CP.A.4', 'HSS-CP.A.5', 'HSS-CP.B.6', 'HSS-CP.B.7',
]
PROB_STAT_ADVANCED = [
    'HSS-CP.B.8', 'HSS-CP.B.9',
    'HSS-MD.A.1', 'HSS-MD.A.2', 'HSS-MD.A.3', 'HSS-MD.A.4', 'HSS-MD.B.5.a', 'HSS-MD.B.5.b', 'HSS-MD.B.6', 'HSS-MD.B.7',
]
PS = 'Probability & Statistics'
STANDARDS = {'Algebra I': ALGEBRA_I, 'Geometry': GEOMETRY + GEOMETRY_PLUS, 'Algebra II': ALGEBRA_II_CORE + ALGEBRA_II_ADVANCED,
             PS: PROB_STAT_CORE + PROB_STAT_ADVANCED}
ADVANCED = {'Geometry': GEOMETRY_PLUS, 'Algebra II': ALGEBRA_II_ADVANCED, PS: PROB_STAT_ADVANCED}
HOME = None  # the collection being built (set by build.load_grade); only 'Geometry' and 'Algebra II' change any placement

# (+) standards, placed in Precalculus.
PRECALCULUS = {
    'HSN-CN.B.4', 'HSN-CN.B.5', 'HSN-CN.B.6', 'HSN-CN.C.8', 'HSN-CN.C.9',
    'HSA-APR.C.5', 'HSA-APR.D.7', 'HSA-REI.C.8', 'HSA-REI.C.9',
    'HSF-IF.C.7.d', 'HSF-BF.A.1.c', 'HSF-BF.B.4.b', 'HSF-BF.B.4.c', 'HSF-BF.B.4.d', 'HSF-BF.B.5',
    'HSF-TF.A.3', 'HSF-TF.A.4', 'HSF-TF.B.6', 'HSF-TF.B.7', 'HSF-TF.C.9',
    'HSG-SRT.D.9', 'HSG-SRT.D.10', 'HSG-SRT.D.11', 'HSG-C.A.4', 'HSG-GPE.A.3', 'HSG-GMD.A.2',
}

# Standards placed in Algebra II (traditional pathway), other than codes that Algebra I already holds.
ALGEBRA_II = {
    'HSN-CN.A.1', 'HSN-CN.A.2', 'HSN-CN.C.7',
    'HSA-SSE.B.4', 'HSA-APR.B.2', 'HSA-APR.B.3', 'HSA-APR.C.4', 'HSA-APR.D.6', 'HSA-REI.A.2',
    'HSF-IF.C.7.c', 'HSF-LE.A.4', 'HSF-TF.A.1', 'HSF-TF.A.2', 'HSF-TF.B.5', 'HSF-TF.C.8',
}


def course_of(code):
    """The course this bank places a high-school standard code in (raises for an unknown code)."""
    if code in ALGEBRA_I:
        return 'Algebra I'
    if HOME == 'Geometry' and code in GEOMETRY_PLUS:
        return 'Geometry'
    if HOME == 'Algebra II' and code in STANDARDS['Algebra II']:
        return 'Algebra II'
    if code in PRECALCULUS or code.startswith('HSN-VM.'):
        return 'Precalculus'
    if code.startswith('HSS-IC.') or code.startswith('HSS-CP.') or code.startswith('HSS-MD.') or code == 'HSS-ID.A.4':
        return 'Probability & Statistics'
    if code.startswith('HSG-'):
        return 'Geometry'
    if code in ALGEBRA_II:
        return 'Algebra II'
    if HOME == PS and code in STANDARDS[PS]:
        return PS  # a P&S standard with no Algebra I home (the stem HSS-ID.B.6), revisited in a later set's backward branch
    raise ValueError('No course placement for %s: add it to engine/hs_courses.py' % code)


def is_plus(code):
    return code in GEOMETRY_PLUS or code in PRECALCULUS


def official_plus(code):
    """True for a Common Core standard marked (+)."""
    return code in GEOMETRY_PLUS or code in PRECALCULUS or code in OFFICIAL_PLUS_EXTRA or code.startswith('HSN-VM.')


def placement(code, role='main'):
    """The course of a code as used in a section: 'main', 'backward' or 'forward'. Only the Algebra II collection
    distinguishes roles: a code Appendix A shares with Algebra I is Algebra II work in MAIN and forward sections (it is
    revisited with new function families) and an Algebra I prerequisite in a backward branch."""
    if HOME == 'Algebra II' and role != 'backward' and code in STANDARDS['Algebra II']:
        return 'Algebra II'
    if HOME == PS and role != 'backward' and code in STANDARDS[PS]:
        return PS  # an S-ID code is Probability & Statistics work in MAIN and forward sections, Algebra I in a backward branch
    return course_of(code)


def course_label(code, home, role='main'):
    """PDF/record label for a high-school standard in the collection of course `home`."""
    if home == 'Algebra II':
        c = placement(code, role)
        if c == 'Algebra II':
            if code in ALGEBRA_II_ADVANCED:
                return 'High School — Algebra II, Advanced Extension (+)'
            tags = (['(+) standard listed in the pathway'] if official_plus(code) else []) + \
                   (['revisits an Algebra I standard'] if code in ALGEBRA_I else [])
            return 'High School — Algebra II' + (', ' + '; '.join(tags) if tags else '')
        if c == 'Algebra I':
            return 'High School — Algebra I'
        return 'High School — %s (course placement in this bank)' % c
    if home == PS:
        c = placement(code, role)
        if c == PS:
            if code in PROB_STAT_ADVANCED:
                return 'High School — Probability & Statistics, Advanced Extension (+)'
            return 'High School — Probability & Statistics' + (', revisits an Algebra I standard' if code in ALGEBRA_I else '')
        if c == 'Algebra I':
            return 'High School — Algebra I'
        return 'High School — %s (course placement in this bank)' % c
    c = course_of(code)
    if home == 'Geometry' and code in GEOMETRY_PLUS:
        return 'High School — Geometry, Advanced Extension (+)'
    if c == home:
        return 'High School — %s' % c
    return 'High School — %s (course placement in this bank)' % c
