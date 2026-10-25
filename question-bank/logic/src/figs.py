"""Exact SVG figures for the Logic collection: grids of cells, labeled panels, networks, maps, cube nets, stacks,
seven-segment digits and token rows. Everything is drawn from coordinates in grayscale with text labels, so no figure
depends on color alone, and the same data that draws a figure is the data the solvers check."""
from xml.sax.saxutils import escape

INK = '#222222'
MID = '#888888'
LIGHT = '#d9d9d9'
SHADE = '#a6a6a6'
FONT = 'font-family="DejaVu Sans, Arial, sans-serif"'


class Canvas:
    def __init__(self, w, h):
        self.w, self.h, self.el = w, h, []

    def rect(self, x, y, w, h, fill='none', stroke=INK, sw=1.5, rx=0, dash=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.el.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
                       % (x, y, w, h, rx, fill, stroke, sw, d))

    def line(self, x1, y1, x2, y2, stroke=INK, sw=1.5, dash=None, cap='round'):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.el.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="%s"%s/>'
                       % (x1, y1, x2, y2, stroke, sw, cap, d))

    def poly(self, pts, fill='none', stroke=INK, sw=1.5, close=True):
        tag = 'polygon' if close else 'polyline'
        self.el.append('<%s points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>'
                       % (tag, ' '.join('%.1f,%.1f' % p for p in pts), fill, stroke, sw))

    def circle(self, x, y, r, fill='none', stroke=INK, sw=1.5):
        self.el.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, r, fill, stroke, sw))

    def text(self, x, y, s, size=14, anchor='middle', weight='normal', fill=INK, rotate=None, flip=None):
        tr = ''
        if rotate is not None:
            tr = ' transform="rotate(%s %.1f %.1f)"' % (rotate, x, y)
        if flip == 'h':
            tr = ' transform="translate(%.1f 0) scale(-1 1)"' % (2 * x)
        if flip == 'v':
            tr = ' transform="translate(0 %.1f) scale(1 -1)"' % (2 * (y - size * 0.35))
        self.el.append('<text x="%.1f" y="%.1f" font-size="%s" text-anchor="%s" font-weight="%s" fill="%s" %s%s>%s</text>'
                       % (x, y, size, anchor, weight, fill, FONT, tr, escape(str(s))))

    def path(self, d, fill='none', stroke=INK, sw=1.5, dash=None):
        ds = ' stroke-dasharray="%s"' % dash if dash else ''
        self.el.append('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s/>'
                       % (d, fill, stroke, sw, ds))

    def group(self, svg_inner, dx, dy):
        self.el.append('<g transform="translate(%.1f %.1f)">%s</g>' % (dx, dy, svg_inner))

    def inner(self):
        return ''.join(self.el)

    def svg(self):
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
                '<rect width="100%%" height="100%%" fill="white"/>%s</svg>' % (self.w, self.h, self.w, self.h, self.inner()))


# ------------------------------------------------------------------ cell shapes (reflections, rotations, tilings)
def cells_canvas(cells, n, m, cell=22, mark=None, grid=True, fill=SHADE, dot=None, pad=4):
    """An n-row x m-column grid with shaded cells (r, c), 0-based. mark: {(r, c): text} labels drawn in cells.
    dot: {(r, c)} cells with a small black dot (an asymmetric feature)."""
    c = Canvas(m * cell + 2 * pad, n * cell + 2 * pad)
    for r in range(n):
        for k in range(m):
            x, y = pad + k * cell, pad + r * cell
            f = fill if (r, k) in cells else 'white'
            c.rect(x, y, cell, cell, fill=f, stroke=MID if grid else 'none', sw=0.8)
    for (r, k) in cells:
        x, y = pad + k * cell, pad + r * cell
        for (dr, dk, x1, y1, x2, y2) in ((-1, 0, 0, 0, 1, 0), (1, 0, 0, 1, 1, 1), (0, -1, 0, 0, 0, 1), (0, 1, 1, 0, 1, 1)):
            if (r + dr, k + dk) not in cells:
                c.line(x + x1 * cell, y + y1 * cell, x + x2 * cell, y + y2 * cell, sw=2.2, cap='square')
    for (r, k) in (dot or ()):
        c.circle(pad + k * cell + cell / 2, pad + r * cell + cell / 2, cell * 0.22, fill=INK, stroke=INK)
    for (r, k), t in (mark or {}).items():
        c.text(pad + k * cell + cell / 2, pad + r * cell + cell * 0.7, t, size=int(cell * 0.6), weight='bold')
    return c


def panels(items, labels=None, cols=None, gap=18, title_size=15):
    """Lay out canvases side by side with a label ("A", "B", ... or given titles) above each."""
    labels = labels or ['ABCDEFGH'[i] for i in range(len(items))]
    cols = cols or len(items)
    rows = (len(items) + cols - 1) // cols
    cw = max(it.w for it in items)
    ch = max(it.h for it in items)
    W = cols * cw + (cols + 1) * gap
    H = rows * (ch + 26) + (rows + 1) * gap // 2 + 4
    c = Canvas(W, H)
    for i, it in enumerate(items):
        r, k = divmod(i, cols)
        x = gap + k * (cw + gap)
        y = gap // 2 + r * (ch + 26 + gap // 2)
        c.text(x + cw / 2, y + 16, labels[i], size=title_size, weight='bold')
        c.group(it.inner(), x + (cw - it.w) / 2, y + 22)
        c.rect(x + (cw - it.w) / 2 - 2, y + 20, it.w + 4, it.h + 4, stroke=LIGHT, sw=1)
    return c


def hstack(items, gap=24, labels=None):
    return panels(items, labels=labels or [''] * len(items), gap=gap)


def reflect_cells(cells, n, m, axis):
    """Mirror image of a cell set: axis 'v' (left-right, vertical mirror line) or 'h' (top-bottom)."""
    if axis == 'v':
        return {(r, m - 1 - k) for r, k in cells}
    return {(n - 1 - r, k) for r, k in cells}


def rotate_cells(cells, n, m, quarter_turns):
    """Rotate a cell set clockwise by 90 degrees per quarter turn; returns (cells, new_n, new_m)."""
    cs, N, M = set(cells), n, m
    for _ in range(quarter_turns % 4):
        cs = {(k, N - 1 - r) for r, k in cs}
        N, M = M, N
    return cs, N, M


def normalize(cells):
    r0 = min(r for r, _ in cells)
    k0 = min(k for _, k in cells)
    return frozenset((r - r0, k - k0) for r, k in cells)


# ------------------------------------------------------------------ text grids and tables
def letter_grid(rows, cell=30, shade=None, bold=None):
    """rows: list of strings (or lists); a blank or '.' is an empty cell; shade: set of (r, c) cells to shade."""
    n, m = len(rows), max(len(r) for r in rows)
    c = Canvas(m * cell + 8, n * cell + 8)
    for r, row in enumerate(rows):
        for k, ch in enumerate(row):
            x, y = 4 + k * cell, 4 + r * cell
            c.rect(x, y, cell, cell, fill=LIGHT if shade and (r, k) in shade else 'white', sw=1.2)
            if ch not in (' ', '.', ''):
                c.text(x + cell / 2, y + cell * 0.68, ch, size=int(cell * 0.55), weight='bold' if bold else 'normal')
    return c


def table(header, rows, colw=None, rowh=26, size=13):
    cols = len(header)
    colw = colw or [max(60, 9 * max(len(str(x)) for x in [header[i]] + [r[i] for r in rows]) + 16) for i in range(cols)]
    W = sum(colw) + 8
    H = rowh * (len(rows) + 1) + 8
    c = Canvas(W, H)
    y = 4
    for ri, row in enumerate([header] + rows):
        x = 4
        for i, v in enumerate(row):
            c.rect(x, y, colw[i], rowh, fill=LIGHT if ri == 0 else 'white', sw=1)
            c.text(x + colw[i] / 2, y + rowh * 0.68, v, size=size, weight='bold' if ri == 0 else 'normal')
            x += colw[i]
        y += rowh
    return c


# ------------------------------------------------------------------ networks (routes, graphs)
def network(nodes, edges, size=(360, 260), labels=True, bridges=None, node_r=13, directed=False, edge_labels=None):
    """nodes: {name: (x, y)} in pixels; edges: [(a, b)] straight segments. Where two edges cross without a node there is
    NO junction (the figure says so). bridges: edges drawn as a dashed line (for example a closed road)."""
    c = Canvas(*size)
    for i, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        dash = '6 4' if bridges and (a, b) in bridges else None
        c.line(x1, y1, x2, y2, sw=2.4, dash=dash)
        if directed:
            import math as _m
            ang = _m.atan2(y2 - y1, x2 - x1)
            mx, my = x2 - (node_r + 2) * _m.cos(ang), y2 - (node_r + 2) * _m.sin(ang)
            for s in (+1, -1):
                c.line(mx, my, mx - 10 * _m.cos(ang + s * 0.45), my - 10 * _m.sin(ang + s * 0.45), sw=2.4)
        if edge_labels and (a, b) in edge_labels:
            c.rect((x1 + x2) / 2 - 11, (y1 + y2) / 2 - 10, 22, 18, fill='white', stroke='none')
            c.text((x1 + x2) / 2, (y1 + y2) / 2 + 4, edge_labels[(a, b)], size=13, weight='bold')
    for name, (x, y) in nodes.items():
        c.circle(x, y, node_r, fill='white', sw=2)
        if labels:
            c.text(x, y + 5, name, size=13, weight='bold')
    return c


# ------------------------------------------------------------------ maps built from grid cells
def region_map(cells, labels=None, cell=34, show=None):
    """cells: list of strings, one character per cell naming its region. Region borders are drawn between cells of
    different regions (thick) and at the outer edge. labels: {region: text} printed at the region's first cell;
    show: which regions get their label (default all)."""
    n, m = len(cells), len(cells[0])
    c = Canvas(m * cell + 8, n * cell + 8)
    for r in range(n):
        for k in range(m):
            x, y = 4 + k * cell, 4 + r * cell
            c.rect(x, y, cell, cell, fill='white', stroke='none')
    for r in range(n):
        for k in range(m):
            x, y = 4 + k * cell, 4 + r * cell
            g = cells[r][k]
            if r == 0 or cells[r - 1][k] != g:
                c.line(x, y, x + cell, y, sw=2.6, cap='square')
            if k == 0 or cells[r][k - 1] != g:
                c.line(x, y, x, y + cell, sw=2.6, cap='square')
            if r == n - 1:
                c.line(x, y + cell, x + cell, y + cell, sw=2.6, cap='square')
            if k == m - 1:
                c.line(x + cell, y, x + cell, y + cell, sw=2.6, cap='square')
    placed = set()
    for r in range(n):
        for k in range(m):
            g = cells[r][k]
            if g in placed:
                continue
            # label at the cell of the region closest to its center
            cs = [(rr, kk) for rr in range(n) for kk in range(m) if cells[rr][kk] == g]
            cr = sum(a for a, _ in cs) / len(cs)
            ck = sum(b for _, b in cs) / len(cs)
            rr, kk = min(cs, key=lambda p: (p[0] - cr) ** 2 + (p[1] - ck) ** 2)
            if show is None or g in show:
                t = (labels or {}).get(g, g)
                c.text(4 + kk * cell + cell / 2, 4 + rr * cell + cell * 0.66, t, size=15, weight='bold')
            placed.add(g)
    return c


def map_adjacency(cells):
    """Neighbors share an edge of a cell (touching only at a corner does not count)."""
    n, m = len(cells), len(cells[0])
    adj = {}
    for r in range(n):
        for k in range(m):
            a = cells[r][k]
            adj.setdefault(a, set())
            for dr, dk in ((1, 0), (0, 1)):
                rr, kk = r + dr, k + dk
                if rr < n and kk < m and cells[rr][kk] != a:
                    adj[a].add(cells[rr][kk])
                    adj.setdefault(cells[rr][kk], set()).add(a)
    return adj


# ------------------------------------------------------------------ cube nets
def cube_net(faces, cell=46):
    """faces: {(r, c): symbol} for the six squares of a net on a grid (0-based). Symbols are short text."""
    rs = [r for r, _ in faces]
    ks = [k for _, k in faces]
    n, m = max(rs) + 1, max(ks) + 1
    c = Canvas(m * cell + 10, n * cell + 10)
    for (r, k), s in faces.items():
        x, y = 5 + k * cell, 5 + r * cell
        c.rect(x, y, cell, cell, fill='white', sw=2)
        c.text(x + cell / 2, y + cell * 0.66, s, size=int(cell * 0.45), weight='bold')
    return c


def net_opposites(faces):
    """Fold a cube net (6 cells, grid coordinates) and return {cell: opposite cell}. Uses rolling: walk the net from one
    face, tracking which cube direction each grid step goes."""
    cells = list(faces)
    start = cells[0]
    # orientation: for each placed face, the cube face it lands on, with a frame (up, right) as unit vectors
    # represent cube faces by outward normal vectors
    pos = {start: ((0, 0, 1), (0, -1, 0), (1, 0, 0))}  # normal, grid-up direction, grid-right direction
    stack = [start]
    while stack:
        cur = stack.pop()
        nrm, up, right = pos[cur]
        r, k = cur
        for dr, dk in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nb = (r + dr, k + dk)
            if nb in faces and nb not in pos:
                neg = lambda v: tuple(-x for x in v)
                if dr == -1:      # step up: new normal is old up; new up is -old normal
                    pos[nb] = (up, neg(nrm), right)
                elif dr == 1:
                    pos[nb] = (neg(up), nrm, right)
                elif dk == -1:
                    pos[nb] = (neg(right), up, nrm)
                else:
                    pos[nb] = (right, up, neg(nrm))
                stack.append(nb)
    assert len(pos) == 6 and len({p[0] for p in pos.values()}) == 6, 'not a valid cube net'
    by_normal = {p[0]: cell for cell, p in pos.items()}
    return {cell: by_normal[tuple(-x for x in pos[cell][0])] for cell in pos}


# ------------------------------------------------------------------ stacks seen from above
def stack_top(rects, size=(220, 170), labels=True):
    """rects: list of (name, x, y, w, h) from BOTTOM to TOP, drawn in that order so later ones hide earlier ones.
    Each sheet is white with a bold outline and its letter at a corner that stays visible by construction."""
    c = Canvas(*size)
    for name, x, y, w, h in rects:
        c.rect(x, y, w, h, fill='white', sw=2.2)
        if labels:
            c.text(x + 11, y + 18, name, size=14, weight='bold')
    return c


# ------------------------------------------------------------------ seven-segment digits
SEG = {  # segments a b c d e f g
    '0': 'abcdef', '1': 'bc', '2': 'abdeg', '3': 'abcdg', '4': 'bcfg', '5': 'acdfg', '6': 'acdefg', '7': 'abc',
    '8': 'abcdefg', '9': 'abcdfg',
}


def seven(digits, w=34, h=60, gap=14, on=INK, colon_after=None, off=None):
    """Draw seven-segment digits (strings like '0'-'9', or a set of segment letters). off: draw unlit segments faintly."""
    n = len(digits)
    extra = 14 if colon_after is not None else 0
    c = Canvas(n * (w + gap) + gap + extra, h + 20)
    x0 = gap
    for i, d in enumerate(digits):
        segs = SEG[d] if d in SEG else d
        x, y = x0, 10
        geo = {'a': (x, y, x + w, y), 'b': (x + w, y, x + w, y + h / 2), 'c': (x + w, y + h / 2, x + w, y + h),
               'd': (x, y + h, x + w, y + h), 'e': (x, y + h / 2, x, y + h), 'f': (x, y, x, y + h / 2),
               'g': (x, y + h / 2, x + w, y + h / 2)}
        for s, (a, b, cc, dd) in geo.items():
            if s in segs:
                c.line(a, b, cc, dd, stroke=on, sw=6)
            elif off:
                c.line(a, b, cc, dd, stroke=LIGHT, sw=4)
        x0 += w + gap
        if colon_after is not None and i == colon_after:
            c.circle(x0 + 2, 10 + h * 0.33, 3, fill=INK)
            c.circle(x0 + 2, 10 + h * 0.67, 3, fill=INK)
            x0 += extra
    return c


# ------------------------------------------------------------------ token rows
def tokens(seq, size=40, gap=10, shape='circle'):
    n = len(seq)
    c = Canvas(n * (size + gap) + gap, size + 16)
    for i, t in enumerate(seq):
        x = gap + i * (size + gap)
        if shape == 'circle':
            c.circle(x + size / 2, 8 + size / 2, size / 2 - 1, fill='white', sw=2)
        else:
            c.rect(x, 8, size, size, fill='white', sw=2, rx=6)
        c.text(x + size / 2, 8 + size * 0.66, t, size=int(size * 0.5), weight='bold')
    return c
