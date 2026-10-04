"""Answer key data and choice presentation.

Every question has a stable ID: S<set>-<section>-Q<n>, where section is M (main),
B1, B2, ... (backward branches), F1 or F2 (forward branches). Example: S40-F2-Q3.

Answers live on the question itself (key=, see inline_raw) or in
<grade>/src/answers/key_*.txt, one line per section:
    S40-F2: ans1 || ans2 || ans3 || ans4 || ans5
    mc  -> letter of the correct choice in AUTHORED order (a, b, c, ...)
    tf  -> T or F
    sa / plot -> answer text; anything after "##" is a grading note.

Multiple-choice questions are authored with the correct choice listed first, so
present() fixes the order students see: numbers ascending, short lists in a
natural order, everything else in a fixed shuffle seeded by the question ID.
"""
import copy
import glob
import hashlib
import os
import random
import re

KEY_DIR = None  # set by build.load_grade()
LETTERS = 'ABCDEFGH'


def section_code(key):
    return 'M' if key == 'MAIN' else key[0] + key.split()[-1]


def qid(set_num, key, i):
    return 'S%d-%s-Q%d' % (set_num, section_code(key), i)


def qtype(q):
    if q['t'] == 'sa' and q.get('ans', '') is None:
        return 'plot'
    if q['t'] == 'sa' and q.get('draw'):
        return 'plot_text'
    if q['t'] == 'sa' and q.get('method'):
        return 'work'
    return q['t']


def load_key():
    key = {}
    if not KEY_DIR:
        return key
    for path in sorted(glob.glob(os.path.join(KEY_DIR, 'key_*.txt'))):
        for n, line in enumerate(open(path, encoding='utf-8'), 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            sec, rest = line.split(':', 1)
            parts = [p.strip() for p in rest.split('||')]
            assert sec not in key, 'duplicate section %s' % sec
            assert len(parts) == 5, '%s:%d %s has %d answers' % (path, n, sec, len(parts))
            key[sec] = parts
    return key


def inline_raw(q):
    """Answer written on the question itself (key= / note= keywords).

    mc: key is the authored letter, default 'a' (the correct choice is written first)
    tf: key is True or False;  sa / plot: key is the answer text.
    """
    t = qtype(q)
    k = q.get('key')
    if t == 'mc':
        raw = k or 'a'
    elif t == 'tf':
        assert k in (True, False), 'tf needs key=True/False: %s' % q['stem']
        raw = 'T' if k else 'F'
    else:
        assert k, 'missing key: %s' % q['stem']
        raw = k
    return raw + (' ## ' + q['note'] if q.get('note') else '')


def split_note(raw):
    if '##' in raw:
        a, n = raw.split('##', 1)
        return a.strip(), n.strip()
    return raw.strip(), ''


# ----------------------------------------------------------- choice ordering

CATCH_ALL = re.compile(r'^(They |Both are|Both$|Neither|None|There is no|There are no|No conclusion|Never|'
                       r'The ratios are equivalent|The balances are equal)')
FIXED = [('One solution', 'No solution', 'Infinitely many solutions')]
NUM = re.compile(r'^(-)?\$?(-)?(\d[\d,]*(?:\.\d+)?)?(?:\{(\d+)/(\d+)\})?\s*(?:°?[A-Za-z%° .]*)$')


def num_value(s):
    m = NUM.match(s.strip())
    if not m or not (m.group(3) or m.group(4)):
        return None
    v = float(m.group(3).replace(',', '')) if m.group(3) else 0.0
    if m.group(4):
        v += int(m.group(4)) / int(m.group(5))
    return -v if (m.group(1) or m.group(2)) else v


def natural_key(s):
    v = num_value(s)
    if s in ('Yes', 'No'):
        return (0, 0 if s == 'Yes' else 1, '')
    if s in ('<', '>', '='):
        return (0, '<>='.index(s), '')
    return (1, v, '') if v is not None else (2, 0, s)


def order_for(q, qid_):
    """Display order: a list of authored indexes."""
    ch = q['ch']
    n = len(ch)
    idx = list(range(n))
    if tuple(ch) in FIXED or all(c.startswith('Point ') for c in ch):
        return idx
    if all(re.fullmatch(r'Quadrant [IV]+', c) for c in ch):
        return sorted(idx, key=lambda i: ['I', 'II', 'III', 'IV'].index(ch[i].split()[1]))
    if all(re.fullmatch(r'\d+–\d+', c) for c in ch):
        return sorted(idx, key=lambda i: int(ch[i].split('–')[0]))
    tail = [i for i in idx if CATCH_ALL.match(ch[i])]
    body = [i for i in idx if i not in tail]
    vals = [num_value(ch[i]) for i in body]
    if n <= 3 or all(v is not None for v in vals):
        body.sort(key=lambda i: natural_key(ch[i]))
        return body + tail
    rng = random.Random(int(hashlib.md5(qid_.encode()).hexdigest(), 16))
    rng.shuffle(body)
    return body + tail


def relabel_points(fig, qid_):
    """For 'Point A..D' choices: rename the plotted points instead of reordering."""
    pts = fig['pts']
    names = [p[1] if fig['k'] == 'nl' else p[2] for p in pts]
    if fig['k'] == 'nl':
        new = [None] * len(pts)
        for rank, i in enumerate(sorted(range(len(pts)), key=lambda i: pts[i][0])):
            new[i] = LETTERS[rank]
    else:
        new = sorted(names)
        random.Random(int(hashlib.md5(qid_.encode()).hexdigest(), 16)).shuffle(new)
    mapping = dict(zip(names, new))
    out = []
    for p in pts:
        p = list(p)
        if fig['k'] == 'nl':
            p[1] = mapping[p[1]]
        else:
            p[2] = mapping[p[2]]
        out.append(tuple(p))
    fig = dict(fig, pts=out)
    return fig, mapping


PLAN = {}  # qid -> display position of the correct choice, when a grade balances its letters


def balanced(q):
    """Four-choice lists that may be freely reordered to balance answer letters."""
    ch = q.get('ch')
    if qtype(q) != 'mc' or q.get('cfigs') or not ch or len(ch) != 4:
        return False
    if tuple(ch) in FIXED or all(c.startswith('Point ') for c in ch):
        return False
    if any(CATCH_ALL.match(c) for c in ch):
        return False
    if all(re.fullmatch(r'Quadrant [IV]+', c) or re.fullmatch(r'\d+–\d+', c) for c in ch):
        return False
    return True


def make_plan(items, seed, frozen=None):
    """items: qids of balanced questions, in collection order. Deal positions A-D evenly, in a seeded order.

    frozen (qid -> position) keeps the letters of an already published collection: those questions keep
    their position, and new questions fill whichever letters are least used, so the totals stay even."""
    PLAN.clear()
    frozen = {k: v for k, v in (frozen or {}).items() if k in set(items)}
    if not frozen:
        pos = [i % 4 for i in range(len(items))]
        random.Random(seed).shuffle(pos)
        PLAN.update(zip(items, pos))
        return
    PLAN.update(frozen)
    count = [0, 0, 0, 0]
    for v in frozen.values():
        count[v] += 1
    rng = random.Random(seed)
    for q in items:
        if q in PLAN:
            continue
        low = min(count)
        p = rng.choice([i for i in range(4) if count[i] == low])
        PLAN[q] = p
        count[p] += 1


def present(q, qid_, answer):
    """Return (display question, correct display letter or None)."""
    t = qtype(q)
    if t == 'tf':
        return q, 'A' if answer == 'T' else 'B'
    if t != 'mc':
        return q, None
    a = 'abcdefgh'.index(answer)
    if q.get('cfigs'):
        return q, LETTERS[a]
    ch = q['ch']
    if all(c.startswith('Point ') for c in ch) and q.get('fig') and q['fig'].get('pts'):
        fig, mapping = relabel_points(q['fig'], qid_)
        old = ch[a].split()[-1]
        q2 = dict(q, fig=fig)
        return q2, mapping[old]
    if qid_ in PLAN:
        others = [i for i in range(len(ch)) if i != a]
        random.Random(int(hashlib.md5(qid_.encode()).hexdigest(), 16)).shuffle(others)
        order = others[:PLAN[qid_]] + [a] + others[PLAN[qid_]:]
    else:
        order = order_for(q, qid_)
    q2 = dict(q, ch=[ch[i] for i in order])
    return q2, LETTERS[order.index(a)]


# ------------------------------------------------------------ plain text

def _grp(t):
    simple = re.fullmatch(r'[\w.√²³⁴⁵⁻]+', t) or re.fullmatch(r'\([^()]*\)', t)
    return t if simple else '(%s)' % t


def plain(s):
    s = re.sub(r'(\d)\{(\d+)/(\d+)\}', r'\1 \2/\3', s)
    s = re.sub(r'(× ?)\{([^{}/]+)/([^{}]+)\}', lambda m: '%s(%s/%s)' % (m.group(1), _grp(m.group(2)), _grp(m.group(3))), s)
    s = re.sub(r'\{([^{}/]+)/([^{}]+)\}(?=[A-Za-z(])', lambda m: '(%s/%s)' % (_grp(m.group(1)), _grp(m.group(2))), s)
    s = re.sub(r'\{([^{}/]+)/([^{}]+)\}', lambda m: '%s/%s' % (_grp(m.group(1)), _grp(m.group(2))), s)
    return s.replace(' ', ' ')


def validate(q, raw):
    """Return an error string if the answer does not fit the question type."""
    t = qtype(q)
    a, _ = split_note(raw)
    if t == 'tf':
        return None if a in ('T', 'F') else 'tf answer must be T or F: %r' % a
    if t == 'mc':
        n = len(q['cfigs']) if q.get('cfigs') else len(q['ch'])
        return None if len(a) == 1 and a in 'abcdefgh'[:n] else 'mc answer must be a-%s: %r' % ('abcdefgh'[n - 1], a)
    if len(a) == 1 and a in 'abcdTF':
        return '%s answer looks like a letter: %r' % (t, a)
    return None if a else 'empty answer'


def answer_record(q, qdisp, raw, letter):
    """Human/AI-readable answer fields."""
    t = qtype(q)
    a, note = split_note(raw)
    rec = dict(type=t, note=note)
    if t == 'tf':
        rec.update(letter=letter, answer='True' if a == 'T' else 'False')
    elif t == 'mc':
        if q.get('cfigs'):
            rec.update(letter=letter, answer='Choice %s (picture)' % letter)
        else:
            rec.update(letter=letter, answer=plain(qdisp['ch'][LETTERS.index(letter)]))
    else:
        rec.update(letter=None, answer=a)
    if t == 'plot_text':
        rec['drawing'] = q['draw']
    if t == 'work':
        rec['method'] = q['method']
    return rec
