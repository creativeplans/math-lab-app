"""Figure helpers shared by the Grade 7 data modules."""
from qb import q1, table, nl, shape, poly, dot, box, coord


def grid(xmax, ymax, ystep=1, xlabel='x', ylabel='y', **kw):
    """First-quadrant grid. A generic grid names its axes x and y; a situation graph passes its own names."""
    return q1(xmax, ymax, ystep=ystep, square=False, xlabel=xlabel, ylabel=ylabel, **kw)


def ints(vmin, vmax, step=1, pts=None, every=1, **kw):
    """Integer number line with labels every `every` steps."""
    labels = {v: str(v).replace('-', '−') for v in range(vmin, vmax + 1) if (v - vmin) % (every * step) == 0}
    return nl(vmin, vmax, step, labels=labels, pts=pts or [], **kw)


def circle(seg=None, label='', h=200):
    return dict(k='circle', seg=seg, label=label, h=h)


def spinner(*labels, h=210):
    return dict(k='spinner', labels=list(labels), h=h)


def angles(rays, labels, ra=(), desc=None, h=230):
    d = dict(k='rays', rays=list(rays), labels=list(labels), ra=list(ra), h=h, fs=1.05, lr=0.62)
    if desc:
        d['desc'] = desc
    return d


def geo(*items, **kw):
    d = dict(k='geo', items=list(items), h=kw.pop('h', 200))
    d.update(kw)
    return d


DRAW = dict(k='grid', rows=9, cols=12, shade=0, h=230, maxcell=24,
            desc='Blank grid for drawing. Each small square is 1 unit by 1 unit.')
BLANK = dict(k='text', text=' ', h=200, desc='Blank space for drawing.')


def solid(kind, r, ht=None, rlab='', hlab='', h=220):
    """Cylinder, cone, or sphere. ht is the solid's height in units (h is the figure height on the page)."""
    d = dict(k=kind, r=r, rlab=rlab, h=h)
    if kind != 'sphere':
        d.update(ht=ht, hlab=hlab)
    return d


def plane(lo=-6, hi=6, **kw):
    """Four-quadrant coordinate grid named x and y."""
    return coord(x=(lo, hi), y=(lo, hi), **kw)
