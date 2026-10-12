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
STANDARDS = {'Algebra I': ALGEBRA_I}

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
    if code in PRECALCULUS or code.startswith('HSN-VM.'):
        return 'Precalculus'
    if code.startswith('HSS-IC.') or code.startswith('HSS-CP.') or code.startswith('HSS-MD.') or code == 'HSS-ID.A.4':
        return 'Probability & Statistics'
    if code.startswith('HSG-'):
        return 'Geometry'
    if code in ALGEBRA_II:
        return 'Algebra II'
    raise ValueError('No course placement for %s: add it to engine/hs_courses.py' % code)


def course_label(code, home):
    """PDF/record label for a high-school standard in the collection of course `home`."""
    c = course_of(code)
    if c == home:
        return 'High School — %s' % c
    return 'High School — %s (course placement in this bank)' % c
