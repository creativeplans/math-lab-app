"""Figure helpers shared by the Grade 4 data modules."""
from math import gcd

from qb import tape, q1, table, hrow, dot, nl, shape, poly


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


def bars(*specs, **kw):
    """Several fraction bars of the same whole, one above the other: bars((4, 3), (8, 6))."""
    return tape(*[dict(n=n, shade=k, size=max(n for n, _ in specs) / n) for n, k in specs], **kw)


def grid(xmax, ymax, ystep=1, xlabel='x', ylabel='y', **kw):
    """First-quadrant grid. A generic grid names its axes x and y; a situation graph passes its own names."""
    return q1(xmax, ymax, ystep=ystep, square=False, xlabel=xlabel, ylabel=ylabel, **kw)


def hgrid(shade, rows=10, cols=10):
    """A hundredths grid with the first `shade` squares shaded."""
    return dict(k='grid', rows=rows, cols=cols, shade=shade, h=240,
                desc='Hundredths grid (%d by %d squares) with %d squares shaded.' % (rows, cols, shade))


def tenths(shade):
    """A strip of 10 equal parts with `shade` parts shaded."""
    return dict(k='grid', rows=1, cols=10, shade=shade, h=90, maxcell=40,
                desc='A strip divided into 10 equal parts with %d parts shaded.' % shade)


def fdot(vmin, vmax, data, d, xlabel):
    """Line plot (dot plot) with fraction labels every 1/d."""
    return dot(vmin, vmax, data, step=1 / d, labels=fracs(vmin, vmax, d), xlabel=xlabel)


def fline(vmin, vmax, d):
    """Empty number line marked in 1/d steps, for making line plots or placing fractions."""
    return nl(vmin, vmax, 1 / d, labels=fracs(vmin, vmax, d))


def arr(rows, cols, split=None):
    d = dict(k='array', rows=rows, cols=cols, h=190)
    if split:
        d['split'] = split
    return d


def prot(rays=(), labels=(), inner=False):
    return dict(k='protractor', rays=list(rays), labels=list(labels), inner=inner, h=300)


def geo(*items, **kw):
    d = dict(k='geo', items=list(items), h=kw.pop('h', 200))
    d.update(kw)
    return d


def angles(rays, labels, ra=(), desc=None, h=230):
    d = dict(k='rays', rays=list(rays), labels=list(labels), ra=list(ra), h=h, fs=1.05, lr=0.62)
    if desc:
        d['desc'] = desc
    return d


def amodel(side, parts):
    """Area model (not to scale): one side length, then (width, top label, area label) for each part."""
    total = sum(w for w, _, _ in parts)
    h = 1.4
    polys, texts, x = [], [], 0
    for i, (w, top, area) in enumerate(parts):
        w = 1 + 1.6 * w / total
        polys.append(poly([(x, 0), (x + w, 0), (x + w, h), (x, h)], [None, None, top, side if i == 0 else None]))
        texts.append((x + w / 2, h / 2, area))
        x += w
    desc = 'Area model (not to scale): a rectangle with side length %s, split into %d parts. ' % (side, len(parts))
    desc += '; '.join('part %d: length %s, area %s' % (i, top, area) for i, (_, top, area) in enumerate(parts, 1)) + '.'
    return shape(polys, texts=texts, fs=1.15, desc=desc)


DRAW = dict(k='grid', rows=9, cols=12, shade=0, h=230, maxcell=24,
            desc='Blank grid for drawing. Each small square is 1 unit by 1 unit.')


def amodel2(top, side, areas):
    """Area model for a two-digit by two-digit product (not to scale).
    top: labels for the two column widths; side: labels for the two row heights; areas: [[a, b], [c, d]]."""
    W, H = (1.8, 1.0), (1.3, 0.9)
    polys, texts = [], []
    y = H[1]
    for r in range(2):
        hh = H[r]
        y0 = H[1] if r == 0 else 0
        x = 0
        for col in range(2):
            ww = W[col]
            el = [None, None, top[col] if r == 0 else None, side[r] if col == 0 else None]
            polys.append(poly([(x, y0), (x + ww, y0), (x + ww, y0 + hh), (x, y0 + hh)], el))
            texts.append((x + ww / 2, y0 + hh / 2, areas[r][col]))
            x += ww
    desc = ('Area model (not to scale): a rectangle split into 2 rows and 2 columns. Column widths %s and %s; row heights %s and %s. '
            'Areas: %s and %s (top row), %s and %s (bottom row).' % (top[0], top[1], side[0], side[1],
                                                                     areas[0][0], areas[0][1], areas[1][0], areas[1][1]))
    return shape(polys, texts=texts, fs=1.1, desc=desc)
