"""Figure helpers shared by the Grade 5 data modules."""
from math import gcd

from qb import tape, q1, table, hrow, dot


def fracs(vmin, vmax, d):
    """Number-line labels in fraction form: {value: '{1/4}', ...}."""
    out = {}
    n = round(vmin * d)
    while n <= round(vmax * d):
        w, r = divmod(int(n), d)
        if r == 0:
            t = str(w)
        else:
            g = gcd(r, d)
            t = (str(w) if w else '') + '{%d/%d}' % (r // g, d // g)
        out[n / d] = t
        n += 1
    return out


def bar(n, shade=0, **kw):
    d = dict(n=n, shade=shade)
    d.update(kw)
    return tape(d)


def grid(xmax, ymax, ystep=1, xlabel=None, ylabel=None, **kw):
    return q1(xmax, ymax, ystep=ystep, square=False, xlabel=xlabel, ylabel=ylabel, **kw)


def tplot(rows, xmax, ymax, ystep=1):
    """A table beside an empty first-quadrant grid, for plotting questions."""
    return hrow(table(rows, fs=0.9), grid(xmax, ymax, ystep, rows[0][0], rows[1][0]), h=245)


def hgrid(shade, rows=10, cols=10):
    """A hundredths grid with the first `shade` squares shaded."""
    return dict(k='grid', rows=rows, cols=cols, shade=shade, h=240,
                desc='Hundredths grid (%d by %d squares) with %d squares shaded.' % (rows, cols, shade))


def fdot(vmin, vmax, data, d, xlabel):
    """Dot plot with fraction labels every 1/d."""
    return dot(vmin, vmax, data, step=1 / d, labels=fracs(vmin, vmax, d), xlabel=xlabel)
