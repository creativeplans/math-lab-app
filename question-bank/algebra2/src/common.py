"""Shared helpers for the Algebra II data modules: graphs, blank grids, proofs, and number formatting."""
import math
from fractions import Fraction

from qb import coord, table, hist, work, sa, mc  # noqa: F401  (re-exported for the data modules)

PR = 'Any valid proof or derivation. '
EXP = 'Any valid explanation. '


def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


def proof(stem, ans='Conclusion:', method='', fig=None, space=150, **kw):
    """Proof / derivation / explanation with required reasoning: a work question with a blank work-space box."""
    return work(stem, ans, method=method, fig=fig, space=space, **kw)


# ------------------------------------------------------------------ numbers
def n(v):
    """Integer or short decimal as text, with a true minus sign handled by the renderer."""
    if isinstance(v, Fraction):
        return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)
    v = round(v, 10)
    if v == int(v):
        return str(int(v))
    return ('%.6f' % v).rstrip('0').rstrip('.')


def cx(a, b):
    """a + bi as text (a, b integers or Fractions)."""
    if b == 0:
        return n(a)
    bi = ('i' if b == 1 else '-i' if b == -1 else '%si' % n(b))
    if a == 0:
        return bi
    if b < 0:
        return '%s - %s' % (n(a), ('i' if b == -1 else '%si' % n(-b)))
    return '%s + %s' % (n(a), bi)


def d1(x):
    return '%.1f' % round(x + 1e-12, 1)


def d2(x):
    return '%.2f' % round(x + 1e-12, 2)


def d3(x):
    return '%.3f' % round(x + 1e-12, 3)


# ------------------------------------------------------------------ graphs
def curves(f, x0, x1, ylo, yhi, n=300, breaks=()):
    """Polylines for y = f(x) on [x0, x1], clipped to ylo <= y <= yhi. No segment is drawn across an x-value in breaks
    (asymptotes, holes) or where f is undefined, so asymptotes are never bridged."""
    def val(x):
        try:
            y = f(x)
        except (ValueError, ZeroDivisionError, OverflowError):
            return None
        if y is None or isinstance(y, complex) or math.isnan(y) or math.isinf(y):
            return None
        return y

    def clip(p, q):
        (xa, ya), (xb, yb) = p, q
        for edge in (ylo, yhi):
            if (ya - edge) * (yb - edge) < 0:
                t = (edge - ya) / (yb - ya)
                xm = xa + t * (xb - xa)
                if (ya < ylo or ya > yhi):
                    xa, ya = xm, edge
                else:
                    xb, yb = xm, edge
        if ylo - 1e-9 <= ya <= yhi + 1e-9 and ylo - 1e-9 <= yb <= yhi + 1e-9:
            return (round(xa, 4), round(ya, 4)), (round(xb, 4), round(yb, 4))
        return None

    xs = [x0 + (x1 - x0) * i / n for i in range(n + 1)]
    for b in breaks:
        xs = [x for x in xs if abs(x - b) > 1e-9]
    out, cur = [], []
    for a, b in zip(xs, xs[1:]):
        ya, yb = val(a), val(b)
        seg = None
        if ya is not None and yb is not None and not any(a < br < b for br in breaks):
            seg = clip((a, ya), (b, yb))
        if seg is None:
            if len(cur) > 1:
                out.append(cur)
            cur = []
            continue
        if cur and cur[-1] == seg[0]:
            cur.append(seg[1])
        else:
            if len(cur) > 1:
                out.append(cur)
            cur = [seg[0], seg[1]]
    if len(cur) > 1:
        out.append(cur)
    return out


def graph(fs, x=(-6, 6), y=(-6, 6), desc=None, vas=(), has=(), holes=(), pts=(), xticks=None, xstep=1, ystep=1,
          dom=None, h=None, **kw):
    """Coordinate plane with the graphs of the functions in fs. vas: x-values of dashed vertical asymptotes; has: y-values of
    dashed horizontal lines (asymptotes or midlines); holes: open circles; pts: filled labeled points (x, y, label, pos);
    dom: (x0, x1) restricts every curve; xticks: {value: label} for the x-axis (radian marks)."""
    assert desc, 'every graph needs desc= (a plain-text description)'
    x0, x1 = dom if dom else x
    cs = []
    for f in fs:
        cs += curves(f, x0, x1, y[0], y[1], breaks=tuple(vas) + tuple(h_[0] for h_ in holes))
    d = coord(x=x, y=y, curves=cs, xstep=xstep, ystep=ystep, square=kw.pop('square', False),
              dlines=[((v, y[0]), (v, y[1])) for v in vas] + [((x[0], v), (x[1], v)) for v in has],
              opts=[tuple(p) for p in holes], pts=[tuple(p) for p in pts], desc=desc, **kw)
    if xticks:
        d['xticks'] = xticks
    if h:
        d['h'] = h
    return d


def blank(x=(-6, 6), y=(-6, 6), xstep=1, ystep=1, desc=None, xticks=None, **kw):
    """Blank coordinate grid for the student's graph."""
    d = coord(x=x, y=y, xstep=xstep, ystep=ystep, square=kw.pop('square', False),
              desc=desc or 'Blank coordinate grid, x from %s to %s and y from %s to %s.' % (n(x[0]), n(x[1]), n(y[0]), n(y[1])), **kw)
    if xticks:
        d['xticks'] = xticks
    return d


GRAPHS = ['Graph A', 'Graph B', 'Graph C', 'Graph D']


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


def cand(fs, desc, **kw):
    """One candidate graph for pick(): the functions drawn, a plain description of what the panel shows (no equation,
    so the description does not give the answer away), and its own features (vas, has, holes, pts)."""
    return dict(fs=fs, desc=desc, **kw)


def pick(stem, at, cands, note, x=(-6, 6), y=(-6, 6), xstep=1, ystep=1, xticks=None, window=None, h=230, **win):
    """Multiple choice 'Which graph ...?': four graphs on the same window in a 2 x 2 figure labeled A-D. cands[0] is the
    correct graph and is placed at letter `at`; the others fill the remaining letters in order. The choices are the
    fixed list Graph A-D, so the letter is set here (balanced by hand across the collection), not by the engine."""
    order = list(cands[1:])
    order.insert('ABCD'.index(at), cands[0])
    if not xticks and 'xlab' not in win:  # at most about 10 numbers per axis in a quarter-size panel
        win['xlab'] = xstep * max(1, math.ceil((x[1] - x[0]) / xstep / 10))
    if 'ylab' not in win:
        win['ylab'] = ystep * max(1, math.ceil((y[1] - y[0]) / ystep / 6))
    panels = []
    for L, c in zip('ABCD', order):
        c = dict(c)
        fs, desc = c.pop('fs'), c.pop('desc')
        slants = c.pop('slant', ())
        g = graph(fs, x=x, y=y, xstep=xstep, ystep=ystep, xticks=xticks, desc='Graph %s: %s' % (L, desc),
                  tag=L, h=h, **dict(win, **c))
        g['fs'] = 1.35  # larger axis numbers: each panel is a quarter of the figure
        for m, b in slants:  # dashed slant asymptote y = mx + b, clipped to the window
            ya, yb = (y[0] - b) / m, (y[1] - b) / m
            lo, hi = max(x[0], min(ya, yb)), min(x[1], max(ya, yb))
            g['dlines'].append(((lo, m * lo + b), (hi, m * hi + b)))
        panels.append(g)
    window = window or 'x from %s to %s and y from %s to %s' % (n(x[0]), n(x[1]), n(y[0]), n(y[1]))
    fig = dict(k='vstack', figs=[dict(k='hrow', figs=panels[:2]), dict(k='hrow', figs=panels[2:])],
               desc='Four graphs labeled A to D, each on a grid with %s. %s' % (window, ' '.join(p['desc'] for p in panels)))
    return mc(stem, list(GRAPHS), fig=fig, key='abcd'['ABCD'.index(at)], note=note, cols=4)


def rise_fall(y0, T, peak, L):
    """f(t) = L + (ct + d)e^(-kt) with f(0) = y0, a single maximum peak at t = T, and f(t) -> L as t grows."""
    d = y0 - L

    def h_(u):
        return d * math.exp(-u) / (1 - u) - (peak - L)
    lo, hi = (1e-6, 1 - 1e-9) if d > 0 else (1 + 1e-9, 40.0)
    for _ in range(200):
        mid = (lo + hi) / 2
        if (h_(lo) < 0) == (h_(mid) < 0):
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2
    k = u / T
    c = k * d / (1 - u)
    return lambda t: L + (c * t + d) * math.exp(-k * t)


def pticks(lo, hi, step):
    """Radian x-axis labels for multiples of π·step between lo and hi (all given as multiples of π)."""
    out = {}
    k = lo
    while k <= hi + 1e-9:
        v = round(k, 6)
        if abs(v) > 1e-9:
            fr = Fraction(v).limit_denominator(12)
            num, den = fr.numerator, fr.denominator
            sgn = '-' if num < 0 else ''
            num = abs(num)
            t = ('π' if num == 1 else '%dπ' % num) if den == 1 else ('π/%d' % den if num == 1 else '%dπ/%d' % (num, den))
            out[v * math.pi] = sgn + t
        k += step
    return out


def tbl(header, rows, **kw):
    """Table with a header row."""
    return table([list(map(str, header))] + [list(map(str, r)) for r in rows], header='row', **kw)
