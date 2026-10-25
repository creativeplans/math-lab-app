"""Shared puzzle helpers for the Logic data modules (figures with their checkable data)."""
import figs
from figs import Canvas, normalize, reflect_cells, rotate_cells

# Block capitals used in this course (stated in each question that relies on them)
V_SYM = set('AHIMOTUVWXY')          # look the same in a left-right (vertical-line) mirror
H_SYM = set('BCDEHIKOX')            # look the same in a top-bottom (horizontal-line) mirror
VSYM_TEXT = 'In the block capitals used here, exactly these letters look the same in a left-right mirror: A H I M O T U V W X Y.'
HSYM_TEXT = 'In the block capitals used here, exactly these letters look the same in a top-bottom mirror: B C D E H I K O X.'


def shape_panel(cells, n, m, mirror=None, cell=22, dot=None):
    c = figs.cells_canvas(set(cells), n, m, cell=cell, dot=dot)
    pad = 4
    if mirror == 'right':
        c.line(pad + m * cell + 3, 0, pad + m * cell + 3, c.h, dash='5 4', sw=2)
        c.w += 8
    if mirror == 'below':
        c.line(0, pad + n * cell + 3, c.w, pad + n * cell + 3, dash='5 4', sw=2)
        c.h += 8
    return c


def same_shape(a, b):
    return normalize(a) == normalize(b)


def choice_figure(items, labels, cols=None):
    return figs.panels(items, labels=labels, cols=cols).svg()


# ------------------------------------------------------------------ stacks of sheets (occlusion)
def top_map(rects, order, step=2):
    """Which sheet is visible at each sample point when sheets are stacked in `order` (bottom to top).
    rects: {name: (x, y, w, h)}. Returns a dict point -> name (only points covered by some sheet)."""
    xs = [r[0] for r in rects.values()] + [r[0] + r[2] for r in rects.values()]
    ys = [r[1] for r in rects.values()] + [r[1] + r[3] for r in rects.values()]
    out = {}
    for x in range(int(min(xs)) + 1, int(max(xs)), step):
        for y in range(int(min(ys)) + 1, int(max(ys)), step):
            for name in reversed(order):
                rx, ry, rw, rh = rects[name]
                if rx < x < rx + rw and ry < y < ry + rh:
                    out[(x, y)] = name
                    break
    return out


def stack_orders_matching(rects, order):
    """Every stacking order that produces exactly the same visible picture as `order`."""
    import itertools
    target = top_map(rects, order)
    return [list(p) for p in itertools.permutations(rects) if top_map(rects, list(p)) == target]


def stack_figure(rects, order, size=(240, 180)):
    return figs.stack_top([(n,) + tuple(rects[n]) for n in order], size=size)


def labels_visible(rects, order):
    """Each sheet's letter (drawn near its top-left corner) is not covered by a sheet above it."""
    for i, n in enumerate(order):
        x, y, w, h = rects[n]
        lx, ly = x + 11, y + 13
        for m in order[i + 1:]:
            mx, my, mw, mh = rects[m]
            if mx - 2 < lx < mx + mw + 2 and my - 2 < ly < my + mh + 2:
                return False
    return True


# ------------------------------------------------------------------ cube nets
def fold(cells):
    """Fold six grid cells into a cube. Returns {cell: outward normal} or None if two cells land on the same face
    (then the shape is not a net of a cube). Uses the same rolling rule as figs.net_opposites."""
    cells = list(cells)
    if len(cells) != 6:
        return None
    start = cells[0]
    pos = {start: ((0, 0, 1), (0, -1, 0), (1, 0, 0))}
    stack = [start]
    neg = lambda v: tuple(-x for x in v)
    while stack:
        cur = stack.pop()
        nrm, up, right = pos[cur]
        r, k = cur
        for dr, dk in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nb = (r + dr, k + dk)
            if nb in cells and nb not in pos:
                if dr == -1:
                    pos[nb] = (up, neg(nrm), right)
                elif dr == 1:
                    pos[nb] = (neg(up), nrm, right)
                elif dk == -1:
                    pos[nb] = (neg(right), up, nrm)
                else:
                    pos[nb] = (right, up, neg(nrm))
                stack.append(nb)
    if len(pos) != 6 or len({p[0] for p in pos.values()}) != 6:
        return None
    return {c: p[0] for c, p in pos.items()}


def opposite_pairs(net):
    """net: {cell: label}. Returns set of frozensets of opposite labels, or None if not a cube net."""
    f = fold(net)
    if f is None:
        return None
    by = {v: c for c, v in f.items()}
    return {frozenset((net[c], net[by[tuple(-x for x in f[c])]])) for c in net}


def opposite_of(net, label):
    for pair in opposite_pairs(net):
        if label in pair:
            return [x for x in pair if x != label][0]
