"""Figure helpers shared by the Grade 3 data modules."""
from math import gcd

from qb import tape, q1, table, dot, nl, shape, poly


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


def ends(vmin, vmax):
    """Labels only at the whole numbers from vmin to vmax."""
    return {v: str(v) for v in range(vmin, vmax + 1)}


def fl(vmin, vmax, d, pts=None, **kw):
    """Number line from vmin to vmax with ticks every 1/d, labeled only at whole numbers."""
    return nl(vmin, vmax, 1 / d, labels=ends(vmin, vmax), pts=pts or [], **kw)


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


def fdot(vmin, vmax, data, d, xlabel):
    """Line plot with fraction labels every 1/d."""
    return dot(vmin, vmax, data, step=1 / d, labels=fracs(vmin, vmax, d), xlabel=xlabel)


def fline(vmin, vmax, d):
    """Empty number line marked in 1/d steps with fraction labels, for making line plots."""
    return nl(vmin, vmax, 1 / d, labels=fracs(vmin, vmax, d))


def arr(rows, cols, split=None):
    d = dict(k='array', rows=rows, cols=cols, h=190)
    if split:
        d['split'] = split
    return d


def area_grid(rows, cols, shade=0, h=200, maxcell=30):
    return dict(k='grid', rows=rows, cols=cols, shade=shade, h=h, maxcell=maxcell,
                desc='A rectangle made of %d rows of %d unit squares%s.' % (
                    rows, cols, ', with %d squares shaded' % shade if shade else ''))


DRAW = dict(k='grid', rows=9, cols=12, shade=0, h=230, maxcell=24,
            desc='Blank grid for drawing. Each small square is 1 unit by 1 unit.')


def tiles(cells, desc, labels=()):
    """A figure made of unit squares; cells are (column, row) of each square's lower-left corner."""
    polys = [poly([(c, r), (c + 1, r), (c + 1, r + 1), (c, r + 1)]) for c, r in cells]
    return shape(polys, texts=list(labels), desc=desc)


def clock(hour, minute):
    return dict(k='clock', hour=hour, minute=minute, h=230)


BLANK_CLOCK = dict(k='clock', hands=False, h=230)


def ruler(n, obj=None, name=None, div=4):
    d = dict(k='ruler', max=n, div=div, h=120)
    if obj:
        d['obj'] = obj
    if name:
        d['name'] = name
    return d


def beaker(mx, step, fill, unit='L', label_step=None):
    return dict(k='beaker', max=mx, step=step, fill=fill, unit=unit, label_step=label_step or step, h=240)


def bargraph(cats, vals, step, ylabel, xlabel=None, ymax=None):
    d = dict(k='hist', bins=list(cats), counts=list(vals), gap=0.35, ystep=step, ymax=ymax or max(vals), ylabel=ylabel, h=230)
    if xlabel:
        d['xlabel'] = xlabel
    return d


def picgraph(title, rows, key, each=None):
    """Picture graph: rows of (category, number of symbols); key says what one ● stands for."""
    return dict(k='picgraph', title=title, rows=[list(r) for r in rows], key=key, h=60 + 40 * (len(rows) + 1))


def amodel(side, parts):
    """Area model (not to scale): one side length, then (width, top label, area label) for each part."""
    total = sum(w for w, _, _ in parts)
    hh = 1.4
    polys, texts, x = [], [], 0
    for i, (w, top, area) in enumerate(parts):
        w = 1 + 1.6 * w / total
        polys.append(poly([(x, 0), (x + w, 0), (x + w, hh), (x, hh)], [None, None, top, side if i == 0 else None]))
        texts.append((x + w / 2, hh / 2, area))
        x += w
    desc = 'Area model (not to scale): a rectangle with side length %s, split into %d parts. ' % (side, len(parts))
    desc += '; '.join('part %d: length %s, area %s' % (i, top, area) for i, (_, top, area) in enumerate(parts, 1)) + '.'
    return shape(polys, texts=texts, fs=1.15, desc=desc)


def tm(h, minutes, suffix=''):
    """Clock time minutes after h:00, as text (12-hour clock)."""
    hh = (h + minutes // 60 - 1) % 12 + 1
    return '%d:%02d%s' % (hh, minutes % 60, suffix)


def tline(h0, total, step=5, every=15, pts=(), jumps=(), suffix=''):
    """Time number line from h0:00 for `total` minutes, ticks every `step` minutes, labels every `every` minutes.
    pts and jumps use minutes after h0:00."""
    labels = {v: tm(h0, v, suffix) for v in range(0, total + 1, every)}
    desc = 'Time number line from %s to %s, with a tick mark every %d minutes and labels every %d minutes' % (
        tm(h0, 0, suffix), tm(h0, total, suffix), step, every)
    if pts:
        desc += '. Points: ' + ', '.join('%s at %s' % (lab or 'a point', tm(h0, v, suffix)) for v, lab in pts)
    if jumps:
        desc += '. ' + '; '.join('Arrow from %s to %s%s' % (tm(h0, a, suffix), tm(h0, b, suffix), ' labeled "%s"' % lab if lab else '')
                                 for a, b, lab in jumps)
    if not pts and not jumps:
        desc += '. Nothing is marked; the student draws on it'
    return nl(0, total, step, labels=labels, pts=list(pts), jumps=list(jumps), desc=desc + '.')


def blank_picgraph(title, cats, key):
    """An empty picture graph (category rows with no symbols) for the student to complete."""
    return picgraph(title, [(c, 0) for c in cats], key)
