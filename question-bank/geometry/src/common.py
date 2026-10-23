"""Figure helpers shared by the Geometry data modules."""
import math

from qb import coord


def gd(P, items=(), desc=None, h=230, **kw):
    """Geometry diagram (engine/gdiagram.py). P: point names -> (x, y); desc: plain-text description (required)."""
    assert desc, 'gd figures need desc='
    d = dict(k='gd', P=dict(P), items=list(items), desc=desc, h=h)
    d.update(kw)
    return d


def grid_fig(P=None, items=(), lo=-6, hi=6, ylo=None, yhi=None, desc=None, h=260, **kw):
    """Coordinate grid with optional named points and items (a gd figure with grid=)."""
    ylo = lo if ylo is None else ylo
    yhi = hi if yhi is None else yhi
    return gd(P or {}, items, desc=desc, h=h, grid=(lo, hi, ylo, yhi), maxk=60, **kw)


def plane(lo=-6, hi=6, **kw):
    """Blank four-quadrant grid for drawing (the student draws on it)."""
    return coord(x=(lo, hi), y=(lo, hi), **kw)


NTS = 'Not drawn to scale.'


def rot(p, deg, c=(0, 0)):
    """Rotate point p by deg degrees counterclockwise about c (exact for multiples of 90)."""
    a = math.radians(deg)
    x, y = p[0] - c[0], p[1] - c[1]
    ca, sa = round(math.cos(a), 12), round(math.sin(a), 12)
    return (round(c[0] + x * ca - y * sa, 9), round(c[1] + x * sa + y * ca, 9))


def pstr(p):
    """'(x, y)' with integers shown without .0 and minus signs."""
    def f(v):
        v = round(v, 6)
        return str(int(v)) if v == int(v) else ('%g' % v)
    return '(%s, %s)' % (f(p[0]), f(p[1]))


def dist(p, q):
    return math.hypot(q[0] - p[0], q[1] - p[1])


def proof(stem, ans='Conclusion:', method='', fig=None, space=150, **kw):
    """Proof / derivation / explanation with required reasoning: a work question with a blank work-space box."""
    from qb import work
    return work(stem, ans, method=method, fig=fig, space=space, **kw)
