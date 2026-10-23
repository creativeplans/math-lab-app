"""Geometry diagram figure ('gd'), used by the Geometry collection.

    dict(k='gd', P={'A': (0, 0), 'B': (4, 0), ...}, items=[...], desc='plain-text description', ...)

P names the points (in units). Every named point is drawn as a dot with its name unless listed in nodot / nolabel.
Label positions: lab={'A': 'sw', ...} (n, ne, e, se, s, sw, w, nw); by default a label is placed away from the
centre of the figure. A point reference in an item is a name from P or an (x, y) tuple.

items (each a tuple; an optional dict of options comes last):
  ('seg', a, b, {...})        segment. options: ticks=n (congruence marks), arrows=n (parallel marks),
                              dash=True, label='5 cm', side=+1/-1 (label side), lw, faint=True
  ('line', a, b, {...})       line through a and b, extended past both (arrowheads at the ends)
  ('ray', a, b, {...})        ray from a through b
  ('poly', [a, b, c], {...})  polygon outline; fill=True shades it
  ('circle', c, r, {...})     r is a number or a point on the circle; dash=True; fill=True
  ('arc', c, r, a1, a2, {...})     arc counterclockwise from angle a1 to a2 (degrees); construction arcs use faint=True
  ('sector', c, r, a1, a2, {...})  shaded sector with its two radii
  ('ang', v, p1, p2, {...})   angle mark at v between rays v->p1 and v->p2 (the smaller angle). n=arcs, label=text
  ('ra', v, p1, p2)           right-angle mark
  ('text', p, 'text', {...})  free text at p (size=, anchor=)
grid=(x0, x1, y0, y1) draws a coordinate grid with axes and numbers (step 1; gstep= to change; nums=False to hide).
note='Not drawn to scale.' prints a note under the drawing.
"""
import math

from reportlab.lib.colors import HexColor

import render as R

SHADE = HexColor('#dbe9f7')
FAINT = HexColor('#7b8794')


def _pt(f, p):
    return f['P'][p] if isinstance(p, str) else p


def _opts(it, n):
    return it[n] if len(it) > n and isinstance(it[n], dict) else {}


def _radius(f, c, r):
    if isinstance(r, (int, float)):
        return float(r)
    cc, rp = _pt(f, c), _pt(f, r)
    return math.hypot(rp[0] - cc[0], rp[1] - cc[1])


def bounds(f):
    xs, ys = [], []
    for p in f.get('P', {}).values():
        xs.append(p[0])
        ys.append(p[1])
    for it in f.get('items', []):
        k = it[0]
        if k in ('seg', 'line', 'ray'):
            for p in it[1:3]:
                q = _pt(f, p)
                xs.append(q[0])
                ys.append(q[1])
        elif k == 'poly':
            for p in it[1]:
                q = _pt(f, p)
                xs.append(q[0])
                ys.append(q[1])
        elif k in ('circle', 'arc', 'sector'):
            c = _pt(f, it[1])
            r = _radius(f, it[1], it[2])
            if k == 'circle':
                xs += [c[0] - r, c[0] + r]
                ys += [c[1] - r, c[1] + r]
            else:
                a1, a2 = it[3], it[4]
                while a2 < a1:
                    a2 += 360
                for a in [a1 + (a2 - a1) * i / 24 for i in range(25)]:
                    xs.append(c[0] + r * math.cos(math.radians(a)))
                    ys.append(c[1] + r * math.sin(math.radians(a)))
                xs.append(c[0])
                ys.append(c[1])
        elif k == 'text':
            q = _pt(f, it[1])
            xs.append(q[0])
            ys.append(q[1])
    if f.get('grid'):
        x0, x1, y0, y1 = f['grid']
        xs += [x0, x1]
        ys += [y0, y1]
    return min(xs), max(xs), min(ys), max(ys)


DIRS = {'n': (0, 1), 'ne': (0.75, 0.75), 'e': (1, 0), 'se': (0.75, -0.75), 's': (0, -1), 'sw': (-0.75, -0.75),
        'w': (-1, 0), 'nw': (-0.75, 0.75)}


def fig_gd(c, f, x, y, w, h, s):
    minx, maxx, miny, maxy = bounds(f)
    note = f.get('note')
    fs = 14 * s * f.get('fs', 1)
    pad = f.get('pad', 30)
    nh = fs * 1.4 if note else 0
    gw, gh = max(maxx - minx, 1e-6), max(maxy - miny, 1e-6)
    k = min((w - 2 * pad) / gw, (h - 2 * pad - nh) / gh, f.get('maxk', 70) * s)
    ox = x + (w - gw * k) / 2
    oy = y + nh + (h - nh - gh * k) / 2

    def P(p):
        q = _pt(f, p)
        return ox + (q[0] - minx) * k, oy + (q[1] - miny) * k

    if f.get('grid'):
        _grid(c, f, P, k, fs)
    # fills first (opaque, no transparency: answer-key pages reuse the question page as a form)
    for it in f.get('items', []):
        o = _opts(it, {'poly': 2, 'circle': 3, 'sector': 5}.get(it[0], 99))
        if it[0] == 'poly' and o.get('fill'):
            path = c.beginPath()
            pts = [P(p) for p in it[1]]
            path.moveTo(*pts[0])
            for q in pts[1:]:
                path.lineTo(*q)
            path.close()
            c.setFillColor(HexColor(o['fill']) if isinstance(o['fill'], str) else SHADE)
            c.drawPath(path, fill=1, stroke=0)
        elif it[0] == 'circle' and o.get('fill'):
            cx, cy = P(it[1])
            c.setFillColor(SHADE)
            c.circle(cx, cy, _radius(f, it[1], it[2]) * k, fill=1, stroke=0)
        elif it[0] == 'sector':
            cx, cy = P(it[1])
            r = _radius(f, it[1], it[2]) * k
            a1, a2 = it[3], it[4]
            while a2 < a1:
                a2 += 360
            path = c.beginPath()
            path.moveTo(cx, cy)
            for i in range(41):
                a = math.radians(a1 + (a2 - a1) * i / 40)
                path.lineTo(cx + r * math.cos(a), cy + r * math.sin(a))
            path.close()
            c.setFillColor(HexColor(o['fill']) if isinstance(o.get('fill'), str) else SHADE)
            c.drawPath(path, fill=1, stroke=0)
    for it in f.get('items', []):
        kind = it[0]
        c.setStrokeColor(R.INK)
        c.setFillColor(R.INK)
        c.setLineWidth(2 * max(s, 0.8))
        c.setDash()
        if kind in ('seg', 'line', 'ray'):
            o = _opts(it, 3)
            _style(c, o, s)
            a, b = P(it[1]), P(it[2])
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = math.hypot(dx, dy)
            ux, uy = dx / L, dy / L
            ext = o.get('ext', 22)
            a2 = (a[0] - ux * ext, a[1] - uy * ext) if kind == 'line' else a
            b2 = (b[0] + ux * ext, b[1] + uy * ext) if kind in ('ray', 'line') else b
            c.line(a2[0], a2[1], b2[0], b2[1])
            c.setDash()
            if kind in ('ray', 'line'):
                R.arrow_head(c, b2[0], b2[1], ux, uy, 8)
            if kind == 'line':
                R.arrow_head(c, a2[0], a2[1], -ux, -uy, 8)
            _marks(c, a, b, o, s)
            if o.get('label'):
                side = o.get('side', 1)
                mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                nx, ny = -uy * side, ux * side
                lw = R.rich_w(o['label'], R.F, fs)
                off = 10 + abs(nx) * lw / 2 + abs(ny) * fs * 0.45
                R.draw_label(c, o['label'], mx + nx * off, my + ny * off, fs, R.F)
        elif kind == 'poly':
            o = _opts(it, 2)
            _style(c, o, s)
            pts = [P(p) for p in it[1]]
            path = c.beginPath()
            path.moveTo(*pts[0])
            for q in pts[1:]:
                path.lineTo(*q)
            path.close()
            c.drawPath(path, fill=0, stroke=1)
        elif kind == 'circle':
            o = _opts(it, 3)
            _style(c, o, s)
            cx, cy = P(it[1])
            c.circle(cx, cy, _radius(f, it[1], it[2]) * k, fill=0, stroke=1)
        elif kind in ('arc', 'sector'):
            o = _opts(it, 5)
            _style(c, o, s)
            cx, cy = P(it[1])
            r = _radius(f, it[1], it[2]) * k
            a1, a2 = it[3], it[4]
            while a2 < a1:
                a2 += 360
            path = c.beginPath()
            if kind == 'sector':
                path.moveTo(cx, cy)
            for i in range(61):
                a = math.radians(a1 + (a2 - a1) * i / 60)
                q = (cx + r * math.cos(a), cy + r * math.sin(a))
                if i == 0 and kind == 'arc':
                    path.moveTo(*q)
                else:
                    path.lineTo(*q)
            if kind == 'sector':
                path.close()
            c.drawPath(path, fill=0, stroke=1)
        elif kind == 'ang':
            o = _opts(it, 4)
            v, p1, p2 = P(it[1]), P(it[2]), P(it[3])
            t1 = math.atan2(p1[1] - v[1], p1[0] - v[0])
            t2 = math.atan2(p2[1] - v[1], p2[0] - v[0])
            d = (t2 - t1) % (2 * math.pi)
            if d > math.pi:
                t1, d = t2, 2 * math.pi - d
            r0 = o.get('r', 20) * max(s, 0.8)
            c.setLineWidth(1.3)
            for j in range(o.get('n', 1)):
                rr = r0 + 4.5 * j
                path = c.beginPath()
                for i in range(31):
                    a = t1 + d * i / 30
                    q = (v[0] + rr * math.cos(a), v[1] + rr * math.sin(a))
                    path.moveTo(*q) if i == 0 else path.lineTo(*q)
                c.drawPath(path, fill=0, stroke=1)
            if o.get('label'):
                mid = t1 + d / 2
                rr = r0 + 4.5 * (o.get('n', 1) - 1) + o.get('lr', 14) + R.rich_w(o['label'], R.F, fs * 0.9) * 0.35
                R.draw_label(c, o['label'], v[0] + rr * math.cos(mid), v[1] + rr * math.sin(mid), fs * 0.9, R.F)
        elif kind == 'ra':
            v, p1, p2 = P(it[1]), P(it[2]), P(it[3])
            d = 11 * max(s, 0.8)
            u1 = (p1[0] - v[0], p1[1] - v[1])
            u2 = (p2[0] - v[0], p2[1] - v[1])
            n1, n2 = math.hypot(*u1), math.hypot(*u2)
            a1 = (v[0] + u1[0] / n1 * d, v[1] + u1[1] / n1 * d)
            a3 = (v[0] + u2[0] / n2 * d, v[1] + u2[1] / n2 * d)
            a2 = (a1[0] + a3[0] - v[0], a1[1] + a3[1] - v[1])
            c.setLineWidth(1.2)
            c.line(a1[0], a1[1], a2[0], a2[1])
            c.line(a2[0], a2[1], a3[0], a3[1])
    # points and labels
    pts = f.get('P', {})
    cxm = sum(p[0] for p in pts.values()) / max(len(pts), 1)
    cym = sum(p[1] for p in pts.values()) / max(len(pts), 1)
    lab = f.get('lab', {})
    for name, p in pts.items():
        px, py = P(name)
        if name not in f.get('nodot', ()):
            c.setFillColor(R.POINT)
            c.circle(px, py, 3.6 * max(s, 0.8), fill=1, stroke=0)
        if name in f.get('nolabel', ()):
            continue
        text = f.get('names', {}).get(name, name)
        if name in lab:
            ux, uy = DIRS[lab[name]]
        else:
            dx, dy = p[0] - cxm, p[1] - cym
            L = math.hypot(dx, dy)
            ux, uy = (dx / L, dy / L) if L > 1e-9 else (0.7, 0.7)
        tw = R.rich_w(text, R.FB, fs)
        R.draw_label(c, text, px + ux * (9 + tw * 0.5), py + uy * (11 + fs * 0.1), fs, R.FB, color=R.POINT)
    for it in f.get('items', []):
        if it[0] == 'text':
            o = _opts(it, 3)
            px, py = P(it[1])
            R.draw_label(c, it[2], px, py, fs * o.get('size', 1), R.FB if o.get('bold') else R.F, anchor=o.get('anchor', 'c'))
    if note:
        R.draw_label(c, note, x + w / 2, y + fs * 0.6, fs * 0.85, R.F, color=R.MUTED)


def _style(c, o, s):
    if o.get('dash'):
        c.setDash(5, 4)
    if o.get('faint'):
        c.setStrokeColor(FAINT)
        c.setLineWidth(1.1)
    elif o.get('lw'):
        c.setLineWidth(o['lw'])
    if o.get('color'):
        c.setStrokeColor(HexColor(o['color']))


def _marks(c, a, b, o, s):
    """Congruence ticks and parallel arrows at the middle of segment ab."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    c.setDash()
    c.setLineWidth(1.5)
    n = o.get('ticks', 0)
    for i in range(n):
        t = (i - (n - 1) / 2) * 5
        cx, cy = mx + ux * t, my + uy * t
        c.line(cx - nx * 7, cy - ny * 7, cx + nx * 7, cy + ny * 7)
    n = o.get('arrows', 0)
    for i in range(n):
        t = (i - (n - 1) / 2) * 7 + 3
        cx, cy = mx + ux * t, my + uy * t
        c.line(cx, cy, cx - ux * 7 + nx * 5, cy - uy * 7 + ny * 5)
        c.line(cx, cy, cx - ux * 7 - nx * 5, cy - uy * 7 - ny * 5)


def _grid(c, f, P, k, fs):
    x0, x1, y0, y1 = f['grid']
    st = f.get('gstep', 1)
    c.setStrokeColor(R.GRID)
    c.setLineWidth(0.7)
    v = x0
    while v <= x1 + 1e-9:
        a, b = P((v, y0)), P((v, y1))
        c.line(a[0], a[1], b[0], b[1])
        v += st
    v = y0
    while v <= y1 + 1e-9:
        a, b = P((x0, v)), P((x1, v))
        c.line(a[0], a[1], b[0], b[1])
        v += st
    c.setStrokeColor(R.AXIS)
    c.setFillColor(R.AXIS)
    c.setLineWidth(1.4)
    if y0 <= 0 <= y1:
        a, b = P((x0, 0)), P((x1, 0))
        c.line(a[0] - 6, a[1], b[0] + 6, b[1])
        R.arrow_head(c, b[0] + 6, b[1], 1, 0, 6)
        R.arrow_head(c, a[0] - 6, a[1], -1, 0, 6)
        R.draw_label(c, 'x', b[0] + 14, b[1] + 8, fs * 1.05, R.FB)
    if x0 <= 0 <= x1:
        a, b = P((0, y0)), P((0, y1))
        c.line(a[0], a[1] - 6, b[0], b[1] + 6)
        R.arrow_head(c, b[0], b[1] + 6, 0, 1, 6)
        R.arrow_head(c, a[0], a[1] - 6, 0, -1, 6)
        R.draw_label(c, 'y', b[0] + 10, b[1] + 12, fs * 1.05, R.FB)
    if f.get('nums', True):
        lst = f.get('numstep', st * (2 if (x1 - x0) / st > 14 else 1))
        v = x0
        while v <= x1 + 1e-9:
            if abs(v) > 1e-9 and abs(v / lst - round(v / lst)) < 1e-9 and y0 <= 0 <= y1:
                q = P((v, 0))
                R.draw_label(c, R.fmt(v), q[0], q[1] - fs * 0.85, fs * 0.72, color=R.MUTED)
            v += st
        v = y0
        while v <= y1 + 1e-9:
            if abs(v) > 1e-9 and abs(v / lst - round(v / lst)) < 1e-9 and x0 <= 0 <= x1:
                q = P((0, v))
                R.draw_label(c, R.fmt(v), q[0] - 5, q[1], fs * 0.72, anchor='r', color=R.MUTED)
            v += st
