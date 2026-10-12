"""Constructors for question sets."""

GRADE = 6  # set by build.load_grade() before the data modules are imported
COURSE = None  # a course collection (for example Algebra I) sets this dict instead of a grade; see engine/hs_courses.py
MAIN_SEEN = []  # course mode: MAIN standards of the sets defined so far, in order
STRICT_BACKWARD = False  # set from the grade's STRICT_BACKWARD; when False, same-grade branches are only listed
SAME_GRADE_BACKWARD = []

DOMAINS = {
    'RP': 'Ratios & Proportional Relationships',
    'NS': 'The Number System',
    'EE': 'Expressions & Equations',
    'G': 'Geometry',
    'SP': 'Statistics & Probability',
    'F': 'Functions',
    'OA': 'Operations & Algebraic Thinking',
    'NBT': 'Number & Operations in Base Ten',
    'NF': 'Number & Operations–Fractions',
    'MD': 'Measurement & Data',
    'CC': 'Counting & Cardinality',
}


# High-school standards (used as Grade 9 forward branches: Algebra I and Geometry), coded like HSA-REI.B.3.
HS_DOMAINS = {
    'N-RN': 'Number & Quantity: The Real Number System',
    'N-Q': 'Number & Quantity: Quantities',
    'N-CN': 'Number & Quantity: The Complex Number System',
    'A-SSE': 'Algebra: Seeing Structure in Expressions',
    'A-APR': 'Algebra: Arithmetic with Polynomials & Rational Expressions',
    'A-CED': 'Algebra: Creating Equations',
    'A-REI': 'Algebra: Reasoning with Equations & Inequalities',
    'F-IF': 'Functions: Interpreting Functions',
    'F-BF': 'Functions: Building Functions',
    'F-LE': 'Functions: Linear, Quadratic & Exponential Models',
    'G-CO': 'Geometry: Congruence',
    'G-SRT': 'Geometry: Similarity, Right Triangles & Trigonometry',
    'G-C': 'Geometry: Circles',
    'G-GPE': 'Geometry: Expressing Geometric Properties with Equations',
    'G-GMD': 'Geometry: Geometric Measurement & Dimension',
    'G-MG': 'Geometry: Modeling with Geometry',
    'S-ID': 'Statistics & Probability: Interpreting Categorical & Quantitative Data',
    'S-IC': 'Statistics & Probability: Making Inferences & Justifying Conclusions',
    'S-CP': 'Statistics & Probability: Conditional Probability & the Rules of Probability',
    'S-MD': 'Statistics & Probability: Using Probability to Make Decisions',
    'N-VM': 'Number & Quantity: Vector & Matrix Quantities',
    'F-TF': 'Functions: Trigonometric Functions',
}
HS_GRADE = 9  # the earliest grade at which this bank places a high-school standard


def hs_place(key=None):
    """Bank grade of a high-school (HS...) standard: it follows its slot, so FORWARD 1 is GRADE + 1 and FORWARD 2 is
    GRADE + 2 (never below 9). Common Core does not assign high-school standards to a grade; this is the bank's choice."""
    if key == 'FORWARD 1':
        return max(HS_GRADE, GRADE + 1)
    if key == 'FORWARD 2':
        return max(HS_GRADE, GRADE + 2)
    return HS_GRADE


def grade_num(code, key=None):
    """Grade of a standard code as a number: K -> 0, high school (HS...) -> its bank placement (see hs_place)."""
    if code.startswith('HS'):
        return hs_place(key)
    g = code.split('.')[0]
    return 0 if g == 'K' else int(g)


def std_info(code, key=None):
    if COURSE and code.startswith('HS'):
        import hs_courses
        return hs_courses.course_label(code, COURSE['name']), HS_DOMAINS[code[2:].split('.')[0]]
    if code.startswith('HS'):
        dom = code[2:].split('.')[0]
        return 'High School (Grade %d in this bank)' % hs_place(key), HS_DOMAINS[dom]
    grade, dom = code.split('.')[:2]
    return 'Grade ' + grade, DOMAINS[dom]


def sa(stem, ans='', fig=None, **kw):
    return dict(t='sa', stem=stem, ans=ans, fig=fig, **kw)


def mc(stem, ch, fig=None, **kw):
    return dict(t='mc', stem=stem, ch=ch, fig=fig, **kw)


def tf(stem, fig=None, **kw):
    return dict(t='tf', stem=stem, fig=fig, **kw)


def nearest_note(std=None, key=None):
    """Note for a nearest-related forward branch, naming the branch's own grade (from its standard and slot)."""
    if COURSE:
        import hs_courses
        return ('No standard in a later course directly continues this skill at this step. This branch uses the '
                'nearest related %s standard.' % hs_courses.course_of(std))
    g = grade_num(std, key) if std else GRADE + 2
    if std and std.startswith('HS'):
        return ('No high-school standard directly continues this skill at this step. This branch uses the nearest related '
                'high-school standard (placed at Grade %d in this bank).' % g)
    return ('No Grade %d standard directly continues this skill. '
            'This branch uses the nearest related Grade %d standard.' % (g, g))


def B(title, std, qs, nearest=False, num=None):
    """nearest=True flags a forward branch with no direct next-grade continuation. In course mode nearest may instead be
    a sentence stating how the branch connects to the set's MAIN skill (shown on the branch page and exported).
    num fixes a backward branch's number (its ID code B<num>); by default branches count 1, 2, 3."""
    assert len(qs) == 5, (title, len(qs))
    std_info(std)
    d = dict(title=title, std=std, qs=qs, nearest=nearest)
    if num:
        d['fixed_num'] = num
    return d


def S(std, title, main, back, f1, f2, num=None):
    """num fixes the set number (IDs S<num>-...). Sets added after a collection is published take
    the next free number so earlier IDs never move; unnumbered sets count up in collection order."""
    assert len(main) == 5, (std, title)
    if COURSE:
        _check_course_set(std, title, main, back, f1, f2)
        d = dict(std=std, title=title, main=main, back=back, f1=f1, f2=f2)
        if num:
            d['fixed_num'] = num
        return d
    assert std.startswith('%d.' % GRADE), std
    for b in back:
        if not grade_num(b['std']) < GRADE:  # a backward branch must use an earlier grade
            SAME_GRADE_BACKWARD.append((title, b['title'], b['std']))
            assert not STRICT_BACKWARD, (title, b['std'])
    assert grade_num(f1['std'], 'FORWARD 1') == GRADE + 1, f1['std']
    assert grade_num(f2['std'], 'FORWARD 2') == GRADE + 2, f2['std']  # Grade 9 and later forward branches use HS... standards
    d = dict(std=std, title=title, main=main, back=back, f1=f1, f2=f2)
    if num:
        d['fixed_num'] = num
    return d


def _check_course_set(std, title, main, back, f1, f2):
    """Course mode rules. MAIN uses a standard of the course. A backward branch uses a Grade K-8 standard, or a
    course standard that is the MAIN standard of an earlier set (never the set's own standard). Each forward branch
    uses a standard of a later course, never a code the course itself holds, and FORWARD 2 is in a course at least as
    advanced as FORWARD 1. Every question carries an explanation (note=)."""
    import hs_courses
    assert std in COURSE['standards'], (title, std)
    for b in back:
        c = b['std']
        if c.startswith('HS'):
            assert c in COURSE['standards'] and c != std and c in MAIN_SEEN, (
                'backward branch must use an earlier set\'s course standard or Grade K-8', title, c)
        else:
            assert grade_num(c) <= 8, (title, c)
    r1, r2 = (hs_courses.RANK[hs_courses.course_of(f['std'])] for f in (f1, f2))
    home = hs_courses.RANK[COURSE['name']]
    assert r1 > home and r2 > home, ('forward branches use later courses', title, f1['std'], f2['std'])
    assert r2 >= r1, ('FORWARD 2 is at least as advanced as FORWARD 1', title, f1['std'], f2['std'])
    for q in main + [q for b in back + [f1, f2] for q in b['qs']]:
        assert q.get('note'), ('every course question needs an explanation (note=)', title, q['stem'][:60])
        for v in [q.get(k) for k in ('stem', 'key', 'note', 'draw', 'method', 'ans')] + list(q.get('ch') or []):
            if isinstance(v, str):
                for i in [m for m in range(len(v)) if v.startswith('^(', m)]:
                    depth, j = 0, i + 1
                    while j < len(v):
                        depth += v[j] == '('
                        depth -= v[j] == ')'
                        j += 1
                        if depth == 0:
                            break
                    assert ' ' not in v[i:j], ('write exponents without spaces so they typeset as superscripts', v[i:j], v[:60])
    MAIN_SEEN.append(std)


# ------------------------------------------------------------ figure helpers

def nl(vmin, vmax, step=1, **kw):
    d = dict(k='nl', min=vmin, max=vmax, step=step)
    d.update(kw)
    return d


def coord(x=(-6, 6), y=(-6, 6), **kw):
    d = dict(k='coord', x=x, y=y)
    d.update(kw)
    return d


def q1(xmax, ymax, **kw):
    d = dict(k='coord', x=(0, xmax), y=(0, ymax), axisnames=False)
    d.update(kw)
    return d


def dot(vmin, vmax, data, step=1, **kw):
    d = dict(k='dot', min=vmin, max=vmax, step=step, data=data)
    d.update(kw)
    return d


def box(vmin, vmax, five, step=1, **kw):
    d = dict(k='box', min=vmin, max=vmax, step=step, five=five)
    d.update(kw)
    return d


def table(rows, **kw):
    d = dict(k='table', rows=rows)
    d.update(kw)
    return d


def stack(*lines, **kw):
    d = dict(k='stack', lines=list(lines))
    d.update(kw)
    return d


def tape(*bars, **kw):
    d = dict(k='tape', bars=list(bars))
    d.update(kw)
    return d


def hist(bins, counts, **kw):
    d = dict(k='hist', bins=bins, counts=counts)
    d.update(kw)
    return d


def prism(l, w, h, labels=(None, None, None), **kw):
    d = dict(k='prism', l=l, w=w, h=h, labels=labels)
    d.update(kw)
    return d


def shape(polys, **kw):
    d = dict(k='shape', polys=polys)
    d.update(kw)
    return d


def poly(pts, el=None, **kw):
    d = dict(pts=pts, el=el)
    d.update(kw)
    return d


def rect(L, W, ll=None, wl=None, **kw):
    return shape([poly([(0, 0), (L, 0), (L, W), (0, W)], [ll, wl, None, None])], **kw)


def tri(b, h, off, bl=None, hl=None, sides=(None, None), **kw):
    """Triangle with base on the x-axis from (0,0) to (b,0) and apex at (off, h)."""
    A, Bp, C = (0, 0), (b, 0), (off, h)
    segs, ra = [], []
    if hl:
        if off == 0:
            pass
        else:
            segs.append(dict(a=C, b=(off, 0), label=hl, off=(10, 0)))
            if off < 0 or off > b:
                segs.append(dict(a=(min(0, off), 0), b=(max(b, off), 0), label=None))
            ra.append(((off, 0), (off, h), (b if off < b else 0, 0)))
    el = [bl, sides[1], sides[0]]
    if off == 0:
        ra.append(((0, 0), (b, 0), (0, h)))
        if hl:
            el[2] = hl
    return shape([poly([A, Bp, C], el)], segs=segs, ra=ra, **kw)


def para(b, h, off, bl=None, hl=None, side=None, **kw):
    pts = [(0, 0), (b, 0), (b + off, h), (off, h)]
    segs = [dict(a=(off, h), b=(off, 0), label=hl, off=(10, 0))] if hl else []
    ra = [((off, 0), (off, h), (b, 0))] if hl else []
    return shape([poly(pts, [bl, side, None, None])], segs=segs, ra=ra, **kw)


def trap(b1, b2, h, off, l1=None, l2=None, hl=None, **kw):
    """Bottom base b1, top base b2 starting at x=off."""
    pts = [(0, 0), (b1, 0), (off + b2, h), (off, h)]
    segs = [dict(a=(off, h), b=(off, 0), label=hl, off=(10, 0))] if hl else []
    ra = [((off, 0), (off, h), (b1, 0))] if hl else []
    return shape([poly(pts, [l1, None, l2, None])], segs=segs, ra=ra, **kw)


def net_prism(l, w, h, ll=None, wl=None, hl=None):
    """Cross-shaped net of an l x w x h rectangular prism."""
    polys = [
        poly([(0, h), (h, h), (h, h + w), (0, h + w)], [None, None, None, wl]),          # left side
        poly([(h, h), (h + l, h), (h + l, h + w), (h, h + w)]),                          # bottom
        poly([(h + l, h), (2 * h + l, h), (2 * h + l, h + w), (h + l, h + w)]),          # right side
        poly([(2 * h + l, h), (2 * h + 2 * l, h), (2 * h + 2 * l, h + w), (2 * h + l, h + w)]),  # top
        poly([(h, 0), (h + l, 0), (h + l, h), (h, h)], [ll, None, None, hl]),            # front
        poly([(h, h + w), (h + l, h + w), (h + l, 2 * h + w), (h, 2 * h + w)]),          # back
    ]
    return shape(polys, fs=0.9)


def net_pyramid(b, s, bl=None, sl=None):
    """Net of a square pyramid: square base b with four triangles of height s."""
    polys = [poly([(0, 0), (b, 0), (b, b), (0, b)], [bl, None, None, None]),
             poly([(0, 0), (b / 2, -s), (b, 0)]),
             poly([(b, 0), (b + s, b / 2), (b, b)]),
             poly([(b, b), (b / 2, b + s), (0, b)]),
             poly([(0, b), (-s, b / 2), (0, 0)])]
    segs = [dict(a=(b / 2, b), b=(b / 2, b + s), label=sl, off=(10, 0))] if sl else []
    return shape(polys, segs=segs, fs=0.9)


def net_triprism(a, b, c, L, labels=(None, None, None, None)):
    """Net of a right triangular prism: legs a, b, hypotenuse c, length L."""
    polys = [poly([(0, 0), (a, 0), (a, L), (0, L)], [None, None, None, labels[3]]),
             poly([(a, 0), (a + b, 0), (a + b, L), (a, L)]),
             poly([(a + b, 0), (a + b + c, 0), (a + b + c, L), (a + b, L)]),
             poly([(0, L), (a, L), (0, L + b)]),
             poly([(0, 0), (0, -b), (a, 0)])]
    texts = [(x, L * 0.12, t) for x, t in ((a / 2, labels[0]), (a + b / 2, labels[1]), (a + b + c / 2, labels[2])) if t]
    return shape(polys, texts=texts, fs=0.9)


def net_tetra():
    h = 3 ** 0.5 / 2
    polys = [poly([(0, 0), (1, 0), (0.5, h)]), poly([(1, 0), (2, 0), (1.5, h)]),
             poly([(0.5, h), (1.5, h), (1, 2 * h)]), poly([(1, 0), (1.5, h), (0.5, h)])]
    return shape(polys)


def hrow(*figs, h=240):
    return dict(k='hrow', figs=list(figs), h=h)


def plot(stem, fig, **kw):
    """A question the student answers by drawing on the figure (no answer line)."""
    return dict(t='sa', stem=stem, ans=None, fig=fig, **kw)


def draw_write(stem, fig, ans, draw, **kw):
    """Drawing + written response: the student draws on the figure AND writes an answer.
    draw= describes the correct drawing; key= is the correct written answer. Both are graded."""
    return dict(t='sa', stem=stem, ans=ans, fig=fig, draw=draw, **kw)


LONG_DIVISION = ('Long division of the numerator by the denominator, shown step by step, until the remainder is 0 '
                 'or the digits start to repeat. A correct decimal without the division earns partial credit.')
DIVISION_ALGORITHM = ('The standard division algorithm with every step shown (divide, multiply, subtract, bring down). '
                      'A correct quotient without the algorithm earns partial credit.')


def work(stem, ans='', method='', fig=None, **kw):
    """Answer with required work: method= says what the shown work must use or contain.
    A correct final answer without the required work is not full credit."""
    assert method
    return dict(t='sa', stem=stem, ans=ans, fig=fig, method=method, **kw)
