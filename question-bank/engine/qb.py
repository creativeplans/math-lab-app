"""Constructors for question sets."""

GRADE = 6  # set by build.load_grade() before the data modules are imported

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


def std_info(code):
    grade, dom = code.split('.')[:2]
    return 'Grade ' + grade, DOMAINS[dom]


def sa(stem, ans='', fig=None, **kw):
    return dict(t='sa', stem=stem, ans=ans, fig=fig, **kw)


def mc(stem, ch, fig=None, **kw):
    return dict(t='mc', stem=stem, ch=ch, fig=fig, **kw)


def tf(stem, fig=None, **kw):
    return dict(t='tf', stem=stem, fig=fig, **kw)


NEAREST_NOTE = ('No Grade 8 standard directly continues this skill. '
                'This branch uses the nearest related Grade 8 standard.')


def B(title, std, qs, nearest=False):
    """nearest=True flags a forward branch with no direct next-grade continuation."""
    assert len(qs) == 5, (title, len(qs))
    std_info(std)
    return dict(title=title, std=std, qs=qs, nearest=nearest)


def S(std, title, main, back, f1, f2):
    assert len(main) == 5, (std, title)
    assert std.startswith('%d.' % GRADE), std
    assert f1['std'].startswith('%d.' % (GRADE + 1)), f1['std']
    assert f2['std'].startswith('%d.' % (GRADE + 2)), f2['std']
    return dict(std=std, title=title, main=main, back=back, f1=f1, f2=f2)


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
