"""Shared helpers for the Probability & Statistics data modules: statistics with stated conventions, figures (dot plots,
histograms, box plots, scatterplots, residual plots, tables), four-figure choice items, and number formatting.

Every key in this collection is computed here from the data printed on the question page, so a figure, its data and its
answer cannot disagree. resolve.py recomputes them with separate code."""
import math
from fractions import Fraction

from qb import coord, table, hist, dot, box, sa, mc, tf  # noqa: F401  (re-exported for the data modules)



def why(o, m, e):
    return 'Obstacle: %s Why it matters: %s Evidence: %s' % (o, m, e)


# ------------------------------------------------------------------ numbers
def n(v):
    """Integer or short decimal as text, with a true minus sign handled by the renderer."""
    if isinstance(v, Fraction):
        return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)
    v = round(v, 10)
    if v == int(v):
        return str(int(v))
    return ('%.6f' % v).rstrip('0').rstrip('.')


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


def tbl(header, rows, **kw):
    """Table with a header row."""
    return table([list(map(str, header))] + [list(map(str, r)) for r in rows], header='row', **kw)


# ------------------------------------------------------------------ statistics (conventions stated in every question)
QRULE = (' Quartiles: Q1 is the median of the lower half and Q3 the median of the upper half of the ordered data; when the '
         'number of values is odd, the median is left out of both halves.')
OUTRULE = ' An outlier is a value below Q1 - 1.5·IQR or above Q3 + 1.5·IQR.'
TECH = ' A calculator or spreadsheet may be used.'


def mean(xs):
    return Fraction(sum(Fraction(x) for x in xs), len(xs))


def median(xs):
    v = sorted(Fraction(x) for x in xs)
    k = len(v)
    return v[k // 2] if k % 2 else (v[k // 2 - 1] + v[k // 2]) / 2


def quartiles(xs):
    """Q1, median, Q3 with the stated rule (median of each half, the median left out when n is odd)."""
    v = sorted(Fraction(x) for x in xs)
    k = len(v)
    lo, hi = v[:k // 2], v[(k + 1) // 2:]
    return median(lo), median(v), median(hi)


def five(xs):
    q1, md, q3 = quartiles(xs)
    return min(xs), q1, md, q3, max(xs)


def fences(xs):
    q1, _, q3 = quartiles(xs)
    i = q3 - q1
    return q1 - Fraction(3, 2) * i, q3 + Fraction(3, 2) * i


def sd_pop(xs):
    m = mean(xs)
    return math.sqrt(float(sum((Fraction(x) - m) ** 2 for x in xs) / len(xs)))


def sd_samp(xs):
    m = mean(xs)
    return math.sqrt(float(sum((Fraction(x) - m) ** 2 for x in xs) / (len(xs) - 1)))


def lsrl(xs, ys):
    """Least-squares line y = a + b·x as exact Fractions (a, b)."""
    mx, my = mean(xs), mean(ys)
    sxy = sum((Fraction(x) - mx) * (Fraction(y) - my) for x, y in zip(xs, ys))
    sxx = sum((Fraction(x) - mx) ** 2 for x in xs)
    b = sxy / sxx
    return my - b * mx, b


def corr(xs, ys):
    mx, my = mean(xs), mean(ys)
    sxy = sum((Fraction(x) - mx) * (Fraction(y) - my) for x, y in zip(xs, ys))
    sxx = sum((Fraction(x) - mx) ** 2 for x in xs)
    syy = sum((Fraction(y) - my) ** 2 for y in ys)
    return float(sxy) / math.sqrt(float(sxx) * float(syy))


def phi(z):
    """Standard normal area to the left of z."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def pct(p, places=1):
    """A proportion as a percent rounded to the given places, as text (for example 0.15866 -> '15.9%')."""
    return ('%.' + str(places) + 'f%%') % round(p * 100 + 1e-12, places)


def fr(v):
    """A Fraction in lowest terms as text ('3/8', '2')."""
    v = Fraction(v)
    return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)


def dlist(xs):
    return ', '.join(n(x) for x in xs)


# ------------------------------------------------------------------ figures
def ztable(zs):
    """Table of standard normal areas to the left of each z (four decimals)."""
    return tbl(['z'] + ['%.1f' % z if abs(z * 10 - round(z * 10)) < 1e-9 else '%.2f' % z for z in zs],
               [['Area to the left'] + ['%.4f' % phi(z) for z in zs]])


def digits_table(rows):
    """Rows of random digits, printed in groups of five (a reproducible stand-in for a random number generator). More than
    four lines are printed in two side-by-side halves (lines 1-4 left, 5-8 right) so the digits stay large."""
    cells = [[str(i + 1), ' '.join(r[k:k + 5] for k in range(0, len(r), 5))] for i, r in enumerate(rows)]
    if len(cells) <= 4:
        return tbl(['Line', 'Digits'], cells)
    h = (len(cells) + 1) // 2
    right = cells[h:] + [['', '']] * (2 * h - len(cells))
    return tbl(['Line', 'Digits', 'Line', 'Digits'], [a_ + b_ for a_, b_ in zip(cells[:h], right)])


def scatter(pts, x, y, desc, xlabel='x', ylabel='y', xstep=1, ystep=1, fs=(), has=(), **kw):
    """Scatterplot: one filled point per (x, y); fs = functions drawn over the points (fitted lines or curves)."""
    return graph(list(fs), x=x, y=y, xstep=xstep, ystep=ystep, pts=[(a, b, '') for a, b in pts], desc=desc,
                 xlabel=xlabel, ylabel=ylabel, has=has, **kw)


def resid_plot(pts, x, y, desc, xlabel='x', ystep=1, xstep=1, **kw):
    """Residual plot: residual against x with a dashed line at 0."""
    return graph([], x=x, y=y, xstep=xstep, ystep=ystep, pts=[(a, b, '') for a, b in pts], has=[0], desc=desc,
                 xlabel=xlabel, ylabel='residual', **kw)


def pickfig(stem, at, figs, note, h=210, cols=4):
    """Multiple choice 'Which plot ...?' with four non-coordinate figures (dot plots, histograms, box plots) titled
    Graph A-D in a 2 x 2 figure. figs[0] is correct and is placed at letter `at`; the choices are the fixed Graph A-D."""
    order = list(figs[1:])
    order.insert('ABCD'.index(at), figs[0])
    if figs[0]['k'] == 'hist' and figs[0].get('xlabel'):
        stem += ' In each histogram, the horizontal axis shows %s and the vertical axis shows frequency.' % (figs[0]['xlabel'] if not figs[0]['xlabel'][:1].isalpha() or figs[0]['xlabel'][1:2].isupper() else figs[0]['xlabel'][0].lower() + figs[0]['xlabel'][1:])
    panels = []
    for L, f in zip('ABCD', order):
        f = dict(f)
        f['title'] = 'Graph %s' % L
        f['h'] = h
        if f['k'] == 'hist':  # axis titles move into the question text (see hist_axes); panels use compact margins
            f['compact'] = True
            f.pop('xlabel', None)
            f.pop('ylabel', None)
        panels.append(f)
    desc = 'Four plots labeled Graph A to Graph D. ' + ' '.join('Graph %s: %s' % (L, p.get('desc', '')) for L, p in zip('ABCD', panels))
    fig = dict(k='vstack', figs=[dict(k='hrow', figs=panels[:2]), dict(k='hrow', figs=panels[2:])], desc=desc)
    return mc(stem, list(GRAPHS), fig=fig, key='abcd'['ABCD'.index(at)], note=note, cols=cols)
