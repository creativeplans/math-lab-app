"""Authoring toolkit for the Entrepreneurship collection.

Every scored item is multiple choice with four choices and exactly one keyed answer, plus a teaching passage ("intro")
shown above the question. The author writes, for each question: the prompt, the correct choice, three wrong choices
each with the reason it is wrong, and feedback (why the correct choice is right). Checks made here, while building:
  - four distinct choices; reasons for every wrong choice; feedback present
  - the teaching passage is 55 to 125 words (the contract asks for about 60 to 120)
  - calc: an optional function that recomputes any arithmetic in the question and must return True
"""
import re

WORDS = re.compile(r"[A-Za-z0-9$%][A-Za-z0-9$%,.'\-]*")


def words(text):
    return len(WORDS.findall(text))


def Q(prompt, correct, w1, w2, w3, fb, calc=None, intro=None):
    """One question. w1..w3: (wrong text, why it is wrong). fb: why the correct answer is right."""
    wrong = [w1, w2, w3]
    texts = [correct] + [w[0] for w in wrong]
    assert len({t.strip().lower() for t in texts}) == 4, 'duplicate choices: %s' % texts
    assert all(len(w) == 2 and w[1].strip() for w in wrong), 'every wrong choice needs a reason: %s' % prompt[:60]
    assert fb and fb.strip(), 'feedback missing: %s' % prompt[:60]
    if calc is not None:
        assert calc() is True, 'arithmetic check failed: %s' % prompt[:80]
    return dict(prompt=prompt, correct=correct, wrong=wrong, feedback=fb, calc=calc is not None, intro=intro)


def sec(skill, intro, qs, mode=None, why=None, standard=None):
    """A section. mode: 'cs' (concept_simplification) or 'math' (math_prerequisite) for backward branches.
    why: author metadata for a backward branch, the diagnostic reason it helps a learner who missed MAIN."""
    n = words(intro)
    assert 55 <= n <= 125, 'teaching passage has %d words (55-125 required): %s' % (n, intro[:60])
    for q in qs:
        if q['intro']:
            m = words(q['intro'])
            assert 55 <= m <= 125, 'question teaching passage has %d words: %s' % (m, q['intro'][:60])
    assert len(qs) == 5, 'a section needs exactly 5 questions (%d): %s' % (len(qs), skill)
    if mode:
        assert mode in ('cs', 'math') and why, 'backward branches need a mode and a diagnostic reason'
    return dict(skill=skill, intro=intro, qs=qs,
                mode={'cs': 'concept_simplification', 'math': 'math_prerequisite'}.get(mode), why=why, standard=standard)


def SET(code, M, B, F1, F2):
    assert isinstance(B, list) and 1 <= len(B) <= 7, 'one to seven backward branches'
    assert all(b['mode'] for b in B), 'backward branches need a mode'
    assert not M['mode'] and not F1['mode'] and not F2['mode']
    return dict(code=code, M=M, B=B, F1=F1, F2=F2)


def cs(skill, intro, qs, why):
    return sec(skill, intro, qs, mode='cs', why=why)


def mathb(skill, intro, qs, why, standard=None):
    return sec(skill, intro, qs, mode='math', why=why, standard=standard)
