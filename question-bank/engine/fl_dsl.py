"""Financial Literacy question-set constructors (course "financial_literacy", prefix FL).

A set is one MAIN skill (5 questions) with:
  - backward branches, in the order a student works them when the MAIN attempt has 3 or fewer correct:
      concept(...)  the course's own five simpler questions about a money idea the MAIN skill rests on
      math(...)     a link (no questions) to a MAIN skill already in the game (Grades 3-8, Algebra I), checked
                    against engine/fl_math_catalog.json, which is copied from the game's content/*/curriculum.json
  - "Go Deeper" sections F1, F2, ... (five questions each): the same topic, taken further, as a chain.

Every question is multiple choice with four choices. q(...) takes the correct choice and three wrong choices, each
with the misconception it represents. Letters are assigned later (fl_build.assign_letters) so that correct answers
are balanced; feedback and misconception text never name a letter, because the game shuffles choices.

A question with intro= is a "Learn and Apply" question (question_type "instruction"): the intro is the short teaching
passage shown above the question on the same screen. A question without intro is a "Knowledge Check".

calc= is an independent recomputation of a numeric answer: the build checks that the correct choice shows this value
(at the precision it is printed) and that no wrong choice does.
"""
import re

SETS = []          # filled in order by the data modules (the pathway order)
UNIT = {}          # current unit while a data module is loading
UNITS = []


def unit(code, title, area):
    """Start a unit. area: the content area(s) of the assignment this unit covers (for the coverage report)."""
    UNIT.clear()
    UNIT.update(code=code, title=title, area=area)
    if code not in [u['code'] for u in UNITS]:  # a unit may continue in a second file
        UNITS.append(dict(UNIT))


def q(stem, right, wrong, intro=None, fb=None, calc=None, sub=None, how=False, tol=None, keep_order=False, eff=None,
      pick=0, shared=False):
    """right: correct choice text. wrong: three (text, misconception) pairs.
    how=True marks a practical how-to question. eff: effective date or tax year for a changing rule.
    pick: which number in a choice is the answer (0 = first, -1 = last). shared=True: wrong choices may show the same
    number with different words (comparisons such as "Job A, by $17.50" vs "Job B, by $17.50")."""
    assert isinstance(right, str) and right.strip(), stem
    assert len(wrong) == 3 and all(len(w) == 2 and w[0].strip() and w[1].strip() for w in wrong), (stem[:60], wrong)
    assert fb and fb.strip(), ('every question needs feedback', stem[:70])
    texts = [right] + [w[0] for w in wrong]
    assert len({t.strip().lower() for t in texts}) == 4, ('choices must be distinct', stem[:60], texts)
    for t in [fb] + [w[1] for w in wrong]:
        assert not re.search(r'\b(choice|option|answer) [A-D]\b|\(\s*[A-D]\s*\)', t), ('never name a letter', t)
    for t in texts:
        assert not re.search(r'\b(all|none|both) of (the|these)\b', t, re.I), ('avoid all/none of the above', t)
    return dict(stem=stem.strip(), right=right.strip(), wrong=[(a.strip(), b.strip()) for a, b in wrong],
                intro=intro.strip() if intro else None, fb=fb.strip(), calc=calc, sub=sub, how=how, tol=tol,
                keep_order=keep_order, eff=eff, pick=pick, shared=shared)


def concept(skill, why, qs):
    assert len(qs) == 5, (skill, len(qs))
    return dict(kind='concept', skill=skill, why=why, qs=qs)


def math(skill, why, course, setnum):
    return dict(kind='math', skill=skill, why=why, ref=dict(course=course, set=setnum))


def deeper(skill, qs):
    assert len(qs) == 5, (skill, len(qs))
    return dict(skill=skill, qs=qs)


def S(num, title, skill, main, back, go, nat, nj, status='stable', sources=(), extra=(), note=None):
    """num: fixed set number (IDs FL:S<num>-...). nat: (national topic, learning target). nj: NJSLS 9.1.12 strands.
    status 'time_sensitive' needs sources. extra: practical skills beyond the standards that the set teaches."""
    assert len(main) == 5, (num, title, len(main))
    assert back, (num, 'every set needs at least one backward branch')
    assert go, (num, 'every set needs at least one Go Deeper section')
    assert status in ('stable', 'time_sensitive'), status
    if status == 'time_sensitive':
        assert sources, (num, 'time-sensitive sets need sources')
    assert num not in [s['num'] for s in SETS], ('duplicate set number', num)
    SETS.append(dict(num=num, title=title, skill=skill, main=main, back=back, go=go, nat=nat, nj=list(nj),
                     status=status, sources=list(sources), extra=list(extra), note=note, unit=dict(UNIT)))


def src(org, url, claim, eff=None):
    return dict(org=org, url=url, claim=claim, **({'effective': eff} if eff else {}))
