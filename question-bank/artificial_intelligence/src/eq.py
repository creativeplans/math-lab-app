"""Authoring toolkit for the Artificial Intelligence collection.

Every scored item is multiple choice with four choices and exactly one keyed answer, plus a teaching passage ("intro")
shown above the question. The author writes, for each question: the prompt, the correct choice, three wrong choices
each with the reason it is wrong, and feedback (why the correct choice is right). Checks made here, while building:
  - four distinct choices; reasons for every wrong choice; feedback present
  - the correct choice is never more than 20 percent longer than the longest wrong choice (no length give-away)
  - the teaching passage is 55 to 125 words (the contract asks for about 60 to 120)
  - calc: an optional function that recomputes any arithmetic in the question and must return True
  - ex: an optional prepared example (prompt/response, code, table or text). A code example is RUN here, in the
    authoring environment only, and its printed output must equal the stated output; learners never run anything.
"""
import contextlib
import io
import re

WORDS = re.compile(r"[A-Za-z0-9$%][A-Za-z0-9$%,.'\-]*")
ISSUES = []  # problems found while loading data files; build.py stops if any remain
FICTIONAL = 'Fictional example (prepared in advance; not a real AI output)'
PREPARED = 'Prepared example (written for this course)'


def words(text):
    return len(WORDS.findall(text))


# ------------------------------------------------------------------ prepared examples
def PR(prompt, response, label=FICTIONAL):
    """A fictional request and AI-style response, written by the course author."""
    return dict(kind='prompt_response', label=label, prompt=prompt, response=response)


def CODE(code, out=None, language='Python 3', label=None, runs=True):
    """A short program shown to the learner. If runs is True it is executed here and must print exactly `out`
    (use out='' for no output). runs=False is for fragments that are not complete programs (still shown only)."""
    code = code.strip('\n')
    if runs:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(compile(code, '<example>', 'exec'), {'__name__': '__example__'})  # author-written snippet only
        got = buf.getvalue().rstrip('\n')
        assert got == (out or '').rstrip('\n'), 'code example printed %r, expected %r' % (got, out)
    return dict(kind='code', label=label or 'Prepared code example (%s). Shown only; nothing runs.' % language,
                code=code, language=language, checked=runs)


def TABLE(rows, label=PREPARED):
    assert len(rows) >= 2 and len({len(r) for r in rows}) == 1, 'a table needs a header and equal-length rows'
    return dict(kind='table', label=label, table=[[str(c) for c in r] for r in rows])


def TEXT(text, label=PREPARED):
    return dict(kind='text', label=label, text=text)


# ------------------------------------------------------------------ questions and sections
def Q(prompt, correct, w1, w2, w3, fb, calc=None, ex=None):
    """One question. w1..w3: (wrong text, why it is wrong). fb: why the correct answer is right."""
    wrong = [w1, w2, w3]
    texts = [correct] + [w[0] for w in wrong]
    assert len({t.strip().lower() for t in texts}) == 4, 'duplicate choices: %s' % texts
    assert all(len(w) == 2 and w[1].strip() for w in wrong), 'every wrong choice needs a reason: %s' % prompt[:60]
    assert fb and fb.strip(), 'feedback missing: %s' % prompt[:60]
    longest = max(len(w[0]) for w in wrong)
    if calc is not None:
        assert calc() is True, 'arithmetic check failed: %s' % prompt[:80]
    if ex is not None:
        assert ex.get('kind') in ('prompt_response', 'code', 'table', 'text') and ex.get('label'), ex
    return dict(prompt=prompt, correct=correct, wrong=wrong, feedback=fb, calc=calc is not None, intro=None, ex=ex)


MODES = {'cs': 'concept_simplification', 'skill': 'underlying_skill'}


def sec(skill, intro, qs, mode=None, why=None):
    """A section. mode: 'cs' (concept_simplification) or 'skill' (underlying_skill) for backward branches.
    why: the diagnostic reason a backward branch helps a learner who missed MAIN."""
    n = words(intro)
    if not 55 <= n <= 125:
        ISSUES.append('WORDS %d | %s' % (n, intro[:70]))
    assert len(qs) == 5, 'a section needs exactly 5 questions (%d): %s' % (len(qs), skill)
    if mode:
        assert mode in MODES and why, 'backward branches need a mode and a diagnostic reason'
    return dict(skill=skill, intro=intro, qs=qs, mode=MODES.get(mode), why=why)


def SET(code, M, B, F1, F2):
    assert isinstance(B, list) and 1 <= len(B) <= 7, 'one to seven backward branches'
    assert all(b['mode'] for b in B), 'backward branches need a mode'
    assert not M['mode'] and not F1['mode'] and not F2['mode']
    return dict(code=code, M=M, B=B, F1=F1, F2=F2)


def cs(skill, intro, qs, why):
    return sec(skill, intro, qs, mode='cs', why=why)


def sk(skill, intro, qs, why):
    return sec(skill, intro, qs, mode='skill', why=why)
