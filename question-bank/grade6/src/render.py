"""Renders question cards (one question per landscape page) to PDF.

Text markup used by the question data:
  {a/b}   stacked fraction (no spaces inside the braces)
  -       a hyphen that is not between letters/digits becomes a minus sign
"""
import math
import re

from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FONT_DIR + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', FONT_DIR + 'DejaVuSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DVM', FONT_DIR + 'DejaVuSansMono.ttf'))
F, FB, FM = 'DV', 'DVB', 'DVM'

PW, PH = 800, 450
INK = HexColor('#18212f')
BLUE = HexColor('#155a9c')
RULE = HexColor('#b9cddd')
LBG = HexColor('#eef4fb')
GRID = HexColor('#d3dce7')
AXIS = HexColor('#18212f')
SHADE = HexColor('#b9d5f0')
MUTED = HexColor('#5b6778')
LINE = HexColor('#1c222b')
POINT = HexColor('#155a9c')

ML, MR = 58, 58
CT, CB = 404, 98          # content top / bottom
CW = PW - ML - MR

sw = pdfmetrics.stringWidth


# ---------------------------------------------------------------- text

def fix_minus(s):
    out = []
    for i, ch in enumerate(s):
        if ch == '-':
            prev = s[i - 1] if i > 0 else ' '
            if not prev.isalnum():
                ch = '−'
        out.append(ch)
    return ''.join(out)


FRAC = re.compile(r'\{([^{}/\s]+)/([^{}\s]+)\}')


def parse_word(w):
    segs, pos = [], 0
    for m in FRAC.finditer(w):
        if m.start() > pos:
            segs.append(('t', w[pos:m.start()]))
        segs.append(('f', m.group(1), m.group(2)))
        pos = m.end()
    if pos < len(w):
        segs.append(('t', w[pos:]))
    return segs


def seg_w(seg, font, size):
    if seg[0] == 't':
        return sw(seg[1], font, size)
    fs = size * 0.72
    return max(sw(seg[1], font, fs), sw(seg[2], font, fs)) + size * 0.3


def word_w(word, font, size):
    return sum(seg_w(s, font, size) for s in word)


def has_frac(words):
    return any(s[0] == 'f' for w in words for s in w)


def line_metrics(words, size):
    if has_frac(words):
        return size * 1.22, size * 0.72
    return size * 0.98, size * 0.34


def wrap(text, font, size, width):
    """Return list of lines; each line is a list of words (word = segs).
    A None line marks a paragraph break."""
    lines = []
    text = re.sub(r' ([+\u2212=×÷<>≤≥:]) (?=\S)', '\u00a0\\1\u00a0', fix_minus(text))
    paras = text.split('\n')
    spw = sw(' ', font, size)
    for pi, para in enumerate(paras):
        if pi:
            lines.append(None)
        words = [parse_word(w) for w in para.split(' ') if w != '']
        cur, cw = [], 0
        for w in words:
            ww = word_w(w, font, size)
            if cur and cw + spw + ww > width:
                lines.append(cur)
                cur, cw = [w], ww
            else:
                cw = cw + (spw if cur else 0) + ww
                cur.append(w)
        lines.append(cur)
    return lines


def lines_height(lines, size, lead=1.0):
    h = 0
    for ln in lines:
        if ln is None:
            h += size * 0.5
            continue
        a, d = line_metrics(ln, size)
        h += (a + d) * lead + size * 0.12
    return h


def lines_width(lines, font, size):
    spw = sw(' ', font, size)
    best = 0
    for ln in lines:
        if not ln:
            continue
        best = max(best, sum(word_w(w, font, size) for w in ln) + spw * (len(ln) - 1))
    return best


def draw_segs(c, words, x, base, font, size, color):
    spw = sw(' ', font, size)
    c.setFillColor(color)
    c.setStrokeColor(color)
    for wi, w in enumerate(words):
        if wi:
            x += spw
        for s in w:
            if s[0] == 't':
                c.setFont(font, size)
                c.drawString(x, base, s[1])
                x += sw(s[1], font, size)
            else:
                fs = size * 0.72
                wd = seg_w(s, font, size)
                bar = base + size * 0.30
                c.setFont(font, fs)
                c.drawCentredString(x + wd / 2, bar + size * 0.14, s[1])
                c.drawCentredString(x + wd / 2, bar - fs * 0.80 - size * 0.06, s[2])
                c.setLineWidth(max(0.8, size * 0.05))
                c.line(x + size * 0.08, bar, x + wd - size * 0.08, bar)
                x += wd
    return x


def draw_lines(c, lines, x, ytop, font, size, color=INK, width=None, align='l', lead=1.0):
    y = ytop
    spw = sw(' ', font, size)
    for ln in lines:
        if ln is None:
            y -= size * 0.5
            continue
        a, d = line_metrics(ln, size)
        base = y - a * lead
        lw = sum(word_w(w, font, size) for w in ln) + spw * max(0, len(ln) - 1)
        xx = x
        if align == 'c':
            xx = x + (width - lw) / 2
        elif align == 'r':
            xx = x + width - lw
        draw_segs(c, ln, xx, base, font, size, color)
        y = base - d * lead - size * 0.12
    return y


def rich_w(text, font, size):
    return word_w_line(text, font, size)


def word_w_line(text, font, size):
    words = [parse_word(w) for w in fix_minus(text).split(' ') if w != '']
    return sum(word_w(w, font, size) for w in words) + sw(' ', font, size) * max(0, len(words) - 1)


def draw_label(c, text, x, y, size=13, font=F, anchor='c', color=INK):
    """Single-line rich text; (x, y) is the anchor point at the vertical middle."""
    text = str(text)
    words = [parse_word(w) for w in fix_minus(text).split(' ') if w != '']
    wd = sum(word_w(w, font, size) for w in words) + sw(' ', font, size) * max(0, len(words) - 1)
    if anchor == 'c':
        x0 = x - wd / 2
    elif anchor == 'r':
        x0 = x - wd
    else:
        x0 = x
    base = y - size * 0.36
    if has_frac(words):
        base = y - size * 0.30
    draw_segs(c, words, x0, base, font, size, color)
    return wd


def label_h(text, size):
    words = [parse_word(w) for w in fix_minus(str(text)).split(' ') if w != '']
    return size * 2.0 if has_frac(words) else size * 1.2


def fmt(v):
    if isinstance(v, str):
        return v
    if abs(v - round(v)) < 1e-9:
        v = int(round(v))
        return str(v) if v >= 0 else '-' + str(-v)
    s = ('%.3f' % v).rstrip('0').rstrip('.')
    return s


# ---------------------------------------------------------------- figures

def arrow_head(c, x, y, dx, dy, size=7):
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    p = c.beginPath()
    p.moveTo(x, y)
    p.lineTo(x - ux * size + px * size * 0.5, y - uy * size + py * size * 0.5)
    p.lineTo(x - ux * size - px * size * 0.5, y - uy * size - py * size * 0.5)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def ticks_of(vmin, vmax, step):
    n = int(round((vmax - vmin) / step))
    return [vmin + i * step for i in range(n + 1)]


def fig_numberline(c, f, x, y, w, h, s):
    vmin, vmax, step = f['min'], f['max'], f['step']
    vert = f.get('vertical', False)
    fs = 14 * s * f.get('fs', 1)
    labels = f.get('labels', 'all')
    ticks = ticks_of(vmin, vmax, step)
    minor = f.get('minor')
    c.setStrokeColor(AXIS)
    c.setFillColor(AXIS)
    if not vert:
        pad = 24
        y0 = y + h * 0.5
        x0, x1 = x + pad, x + w - pad
        if f.get('label_above'):
            y0 = y + h * 0.35

        def X(v):
            return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
        c.setLineWidth(1.6)
        c.line(x0 - 14, y0, x1 + 14, y0)
        if f.get('arrows', True):
            arrow_head(c, x1 + 18, y0, 1, 0)
            arrow_head(c, x0 - 18, y0, -1, 0)
        if minor:
            c.setLineWidth(1)
            for v in ticks_of(vmin, vmax, minor):
                c.line(X(v), y0 - 5, X(v), y0 + 5)
        c.setLineWidth(1.5)
        for v in ticks:
            c.line(X(v), y0 - 8, X(v), y0 + 8)
        for v in ticks:
            txt = None
            if labels == 'all':
                txt = fmt(v)
            elif isinstance(labels, dict):
                for k, t in labels.items():
                    if abs(k - v) < 1e-9:
                        txt = t
            elif isinstance(labels, (list, tuple)):
                if any(abs(k - v) < 1e-9 for k in labels):
                    txt = fmt(v)
            if txt is not None:
                draw_label(c, txt, X(v), y0 - 12 - label_h(txt, fs) / 2, fs)
        if isinstance(labels, dict):
            for k, t in labels.items():
                if not any(abs(k - v) < 1e-9 for v in ticks):
                    c.line(X(k), y0 - 8, X(k), y0 + 8)
                    draw_label(c, t, X(k), y0 - 12 - label_h(t, fs) / 2, fs)
        ray = f.get('ray')
        if ray:
            v, d, op = ray
            c.setStrokeColor(POINT)
            c.setFillColor(POINT)
            c.setLineWidth(4)
            end = x1 + 16 if d == 'right' else x0 - 16
            c.line(X(v), y0, end, y0)
            arrow_head(c, end + (6 if d == 'right' else -6), y0, 1 if d == 'right' else -1, 0, 12)
            c.setLineWidth(2.2)
            if op:
                c.setFillColor(white)
            c.circle(X(v), y0, 6, fill=1, stroke=1)
        for p in f.get('pts', []):
            v, lab = p[0], p[1]
            c.setFillColor(POINT)
            c.circle(X(v), y0, 5.5, fill=1, stroke=0)
            if lab:
                draw_label(c, lab, X(v), y0 + 22, fs * 1.1, FB, color=POINT)
        for a in f.get('jumps', []):
            v1, v2, lab = a
            xa, xb = X(v1), X(v2)
            c.setStrokeColor(POINT)
            c.setLineWidth(1.6)
            r = abs(xb - xa) / 2
            cx = (xa + xb) / 2
            hh = min(26, r * 0.8)
            p = c.beginPath()
            p.moveTo(xa, y0 + 10)
            p.curveTo(xa, y0 + 10 + hh, xb, y0 + 10 + hh, xb, y0 + 10)
            c.drawPath(p, stroke=1, fill=0)
            c.setFillColor(POINT)
            arrow_head(c, xb, y0 + 10, 0, -1, 7)
            if lab:
                draw_label(c, lab, cx, y0 + 18 + hh, fs, color=POINT)
        if f.get('caption'):
            draw_label(c, f['caption'], x + w / 2, y + 8, fs)
    else:
        pad = 18
        cx = x + w * 0.5
        y0, y1 = y + pad, y + h - pad

        def Y(v):
            return y0 + (v - vmin) / (vmax - vmin) * (y1 - y0)
        c.setLineWidth(1.6)
        c.line(cx, y0 - 10, cx, y1 + 10)
        if f.get('arrows', True):
            arrow_head(c, cx, y1 + 14, 0, 1)
            arrow_head(c, cx, y0 - 14, 0, -1)
        c.setLineWidth(1.4)
        for v in ticks:
            c.line(cx - 8, Y(v), cx + 8, Y(v))
            txt = None
            if labels == 'all':
                txt = fmt(v)
            elif isinstance(labels, dict):
                for k, t in labels.items():
                    if abs(k - v) < 1e-9:
                        txt = t
            elif isinstance(labels, (list, tuple)):
                if any(abs(k - v) < 1e-9 for k in labels):
                    txt = fmt(v)
            if txt is not None:
                draw_label(c, txt, cx - 14, Y(v), fs, anchor='r')
        for p in f.get('pts', []):
            v, lab = p[0], p[1]
            c.setFillColor(POINT)
            c.circle(cx, Y(v), 5.5, fill=1, stroke=0)
            if lab:
                draw_label(c, lab, cx + 16, Y(v), fs * 1.1, FB, anchor='l', color=POINT)
        if f.get('caption'):
            draw_label(c, f['caption'], cx, y1 + 30, fs, FB)


def fig_coord(c, f, x, y, w, h, s):
    xmin, xmax = f.get('x', (-6, 6))
    ymin, ymax = f.get('y', (-6, 6))
    xs, ys = f.get('xstep', 1), f.get('ystep', 1)
    xl, yl = f.get('xlab', xs), f.get('ylab', ys)
    fs = 12.5 * s * f.get('fs', 1)
    padl = 30 + (16 if f.get('ylabel') else 0)
    padb = 22 + (16 if f.get('xlabel') else 0)
    padr, padt = 16, 14
    nx = (xmax - xmin) / xs
    ny = (ymax - ymin) / ys
    aw, ah = w - padl - padr, h - padb - padt
    cwid, chei = aw / nx, ah / ny
    if f.get('square', True):
        cwid = chei = min(cwid, chei)
    gw, gh = cwid * nx, chei * ny
    ox = x + padl + (aw - gw) / 2
    oy = y + padb + (ah - gh) / 2

    def P(px, py):
        return ox + (px - xmin) / xs * cwid, oy + (py - ymin) / ys * chei
    c.setStrokeColor(GRID)
    c.setLineWidth(0.7)
    for i in range(int(round(nx)) + 1):
        c.line(ox + i * cwid, oy, ox + i * cwid, oy + gh)
    for j in range(int(round(ny)) + 1):
        c.line(ox, oy + j * chei, ox + gw, oy + j * chei)
    for poly in f.get('polys', []):
        pts = [P(*p) for p in poly]
        path = c.beginPath()
        path.moveTo(*pts[0])
        for p in pts[1:]:
            path.lineTo(*p)
        path.close()
        c.setStrokeColor(POINT)
        c.setFillColor(HexColor('#dce9f7'))
        c.setFillAlpha(0.6)
        c.setLineWidth(2)
        c.drawPath(path, fill=1, stroke=1)
    c.setFillAlpha(1)
    c.setStrokeColor(AXIS)
    c.setFillColor(AXIS)
    c.setLineWidth(1.5)
    ax0, ay0 = P(max(xmin, min(0, xmax)), max(ymin, min(0, ymax)))
    c.line(ox, ay0, ox + gw, ay0)
    c.line(ax0, oy, ax0, oy + gh)
    if xmin < 0:
        arrow_head(c, ox - 4, ay0, -1, 0, 6)
    arrow_head(c, ox + gw + 4, ay0, 1, 0, 6)
    if ymin < 0:
        arrow_head(c, ax0, oy - 4, 0, -1, 6)
    arrow_head(c, ax0, oy + gh + 4, 0, 1, 6)
    if f.get('nums', True):
        c.setFillColor(MUTED)
        v = xmin
        while v <= xmax + 1e-9:
            if abs(v) > 1e-9 or xmin == 0:
                if abs((v / xl) - round(v / xl)) < 1e-9:
                    px, _ = P(v, 0)
                    draw_label(c, fmt(v), px, ay0 - fs * 0.95, fs, color=MUTED)
            v += xs
        v = ymin
        while v <= ymax + 1e-9:
            if abs(v) > 1e-9:
                if abs((v / yl) - round(v / yl)) < 1e-9:
                    _, py = P(0, v)
                    draw_label(c, fmt(v), ax0 - 5, py, fs, anchor='r', color=MUTED)
            v += ys
    if f.get('axisnames', True) and xmin < 0:
        draw_label(c, 'x', ox + gw + 6, ay0 + 10, fs * 1.2, anchor='l')
        draw_label(c, 'y', ax0 + 8, oy + gh + 4, fs * 1.2, anchor='l')
    if f.get('xlabel'):
        draw_label(c, f['xlabel'], ox + gw / 2, oy - padb + 8, fs * 1.1, FB)
    if f.get('ylabel'):
        c.saveState()
        c.translate(ox - padl + 8, oy + gh / 2)
        c.rotate(90)
        draw_label(c, f['ylabel'], 0, 0, fs * 1.1, FB)
        c.restoreState()
    for ln in f.get('lines', []):
        a, b = P(*ln[0]), P(*ln[1])
        c.setStrokeColor(POINT)
        c.setLineWidth(2.2)
        c.line(a[0], a[1], b[0], b[1])
    for p in f.get('pts', []):
        px, py = P(p[0], p[1])
        c.setFillColor(POINT)
        c.circle(px, py, 4.2, fill=1, stroke=0)
        if len(p) > 2 and p[2]:
            pos = p[3] if len(p) > 3 else 'ne'
            dx = {'ne': 7, 'nw': -7, 'se': 7, 'sw': -7, 'n': 0, 's': 0, 'e': 8, 'w': -8}[pos]
            dy = {'ne': 9, 'nw': 9, 'se': -9, 'sw': -9, 'n': 12, 's': -12, 'e': 0, 'w': 0}[pos]
            anc = 'l' if dx > 0 else ('r' if dx < 0 else 'c')
            draw_label(c, p[2], px + dx, py + dy, fs * 1.25, FB, anchor=anc, color=POINT)


def fig_dot(c, f, x, y, w, h, s):
    vmin, vmax, step = f['min'], f['max'], f['step']
    lstep = f.get('lstep', step)
    data = f['data']
    if isinstance(data, (list, tuple)):
        d = {}
        for v in data:
            d[v] = d.get(v, 0) + 1
        data = d
    fs = 15 * s
    pad = 26
    x0, x1 = x + pad, x + w - pad
    base = y + (32 if not f.get('xlabel') else 50) + (6 if f.get('labels') else 0)
    unit = (x1 - x0) / ((vmax - vmin) / step)

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    maxc = max(data.values()) if data else 1
    r = min(unit * 0.36, 7.5, (h - (base - y) - 10) / (2 * maxc + 1) * 0.95)
    c.setStrokeColor(AXIS)
    c.setLineWidth(1.5)
    c.line(x0 - 12, base, x1 + 12, base)
    for v in ticks_of(vmin, vmax, step):
        c.line(X(v), base - 6, X(v), base + 6)
        if f.get('labels'):
            for k_, t_ in f['labels'].items():
                if abs(k_ - v) < 1e-9:
                    draw_label(c, t_, X(v), base - 22, fs * 1.15)
        elif abs(((v - vmin) / lstep) - round((v - vmin) / lstep)) < 1e-9:
            draw_label(c, fmt(v), X(v), base - 17, fs)
    c.setFillColor(POINT)
    for v, n in data.items():
        for i in range(n):
            c.circle(X(v), base + 6 + r + i * r * 2.15, r, fill=1, stroke=0)
    if f.get('xlabel'):
        draw_label(c, f['xlabel'], (x0 + x1) / 2, y + 10, fs, FB)
    if f.get('title'):
        draw_label(c, f['title'], (x0 + x1) / 2, y + h - 8, fs, FB)


def fig_hist(c, f, x, y, w, h, s):
    bins, counts = f['bins'], f['counts']
    gap = f.get('gap', 0)
    fs = 12 * s
    ymax = f.get('ymax', max(counts))
    ystep = f.get('ystep', 1)
    padl, padb, padt = 46, 44 if f.get('xlabel') else 28, 10
    x0, y0 = x + padl, y + padb
    gw, gh = w - padl - 12, h - padb - padt
    c.setStrokeColor(GRID)
    c.setLineWidth(0.7)
    v = 0
    while v <= ymax + 1e-9:
        yy = y0 + v / ymax * gh
        c.line(x0, yy, x0 + gw, yy)
        draw_label(c, fmt(v), x0 - 6, yy, fs, anchor='r', color=MUTED)
        v += ystep
    n = len(bins)
    bw = gw / n
    for i, (b, k) in enumerate(zip(bins, counts)):
        bx = x0 + i * bw + gap * bw / 2
        c.setFillColor(SHADE)
        c.setStrokeColor(POINT)
        c.setLineWidth(1.3)
        c.rect(bx, y0, bw * (1 - gap), k / ymax * gh, fill=1, stroke=1)
        draw_label(c, b, x0 + i * bw + bw / 2, y0 - 12, fs)
    c.setStrokeColor(AXIS)
    c.setLineWidth(1.5)
    c.line(x0, y0, x0 + gw, y0)
    c.line(x0, y0, x0, y0 + gh)
    if f.get('xlabel'):
        draw_label(c, f['xlabel'], x0 + gw / 2, y + 10, fs, FB)
    if f.get('ylabel'):
        c.saveState()
        c.translate(x + 10, y0 + gh / 2)
        c.rotate(90)
        draw_label(c, f['ylabel'], 0, 0, fs, FB)
        c.restoreState()


def fig_box(c, f, x, y, w, h, s):
    vmin, vmax, step = f['min'], f['max'], f['step']
    lstep = f.get('lstep', step)
    boxes = f['boxes'] if 'boxes' in f else [(None, f['five'])]
    fs = 13 * s
    namew = max([sw(nm or '', FB, fs) for nm, _ in boxes] + [0])
    namew = namew + 14 if namew else 0
    pad = 20
    x0, x1 = x + pad + namew, x + w - pad
    base = y + (30 if not f.get('xlabel') else 46)

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    c.setStrokeColor(AXIS)
    c.setLineWidth(1.5)
    c.line(x0 - 10, base, x1 + 10, base)
    for v in ticks_of(vmin, vmax, step):
        c.line(X(v), base - 6, X(v), base + 6)
        if abs(((v - vmin) / lstep) - round((v - vmin) / lstep)) < 1e-9:
            draw_label(c, fmt(v), X(v), base - 17, fs)
    avail = h - (base - y) - 14
    slot = avail / len(boxes)
    bh = min(38, slot * 0.6)
    for i, (nm, five) in enumerate(boxes):
        cy = base + 12 + slot * (len(boxes) - 1 - i) + slot / 2
        a, q1, md, q3, b = five
        c.setStrokeColor(POINT)
        c.setLineWidth(1.8)
        c.line(X(a), cy, X(q1), cy)
        c.line(X(q3), cy, X(b), cy)
        c.line(X(a), cy - bh * 0.3, X(a), cy + bh * 0.3)
        c.line(X(b), cy - bh * 0.3, X(b), cy + bh * 0.3)
        c.setFillColor(HexColor('#dce9f7'))
        c.rect(X(q1), cy - bh / 2, X(q3) - X(q1), bh, fill=1, stroke=1)
        c.line(X(md), cy - bh / 2, X(md), cy + bh / 2)
        if nm:
            draw_label(c, nm, x + pad, cy, fs, FB, anchor='l')
    if f.get('xlabel'):
        draw_label(c, f['xlabel'], (x0 + x1) / 2, y + 10, fs, FB)


def fig_table(c, f, x, y, w, h, s):
    rows = f['rows']
    fs = 16 * s * f.get('fs', 1)
    hdr = f.get('header', 'col')   # 'col' = first column is header, 'row' = first row
    ncol = max(len(r) for r in rows)
    colw = [0] * ncol
    for r in rows:
        for j, cell in enumerate(r):
            colw[j] = max(colw[j], rich_w(str(cell), FB, fs) + 22)
    colw = [max(cw_, 46) for cw_ in colw]
    rh = [max(label_h(str(cell), fs) for cell in r) + 12 for r in rows]
    tw, th = sum(colw), sum(rh)
    k = min(1.0, w / tw, h / th)
    if k < 1:
        fs *= k
        colw = [cw_ * k for cw_ in colw]
        rh = [r_ * k for r_ in rh]
        tw, th = tw * k, th * k
    x0 = x + (w - tw) / 2 if f.get('center', True) else x
    y0 = y + (h + th) / 2
    yy = y0
    for i, r in enumerate(rows):
        xx = x0
        for j in range(ncol):
            cell = r[j] if j < len(r) else ''
            head = (hdr == 'col' and j == 0) or (hdr == 'row' and i == 0) or (hdr == 'both' and (i == 0 or j == 0))
            c.setFillColor(LBG if head else white)
            c.setStrokeColor(HexColor('#8aa3bd'))
            c.setLineWidth(1)
            c.rect(xx, yy - rh[i], colw[j], rh[i], fill=1, stroke=1)
            draw_label(c, str(cell), xx + colw[j] / 2, yy - rh[i] / 2, fs, FB if head else F)
            xx += colw[j]
        yy -= rh[i]


def poly_area(pts):
    a = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        a += x1 * y2 - x2 * y1
    return a / 2


def fig_shape(c, f, x, y, w, h, s):
    fs = 15 * s * f.get('fs', 1)
    allp = []
    for pl in f.get('polys', []):
        allp += pl['pts']
    for sg in f.get('segs', []):
        allp += [sg['a'], sg['b']]
    xs_ = [p[0] for p in allp]
    ys_ = [p[1] for p in allp]
    minx, maxx, miny, maxy = min(xs_), max(xs_), min(ys_), max(ys_)
    pad = f.get('pad', 44)
    k = min((w - 2 * pad) / max(maxx - minx, 1e-6), (h - 2 * pad) / max(maxy - miny, 1e-6))
    if f.get('maxk'):
        k = min(k, f['maxk'])
    ox = x + (w - (maxx - minx) * k) / 2
    oy = y + (h - (maxy - miny) * k) / 2

    def P(p):
        return ox + (p[0] - minx) * k, oy + (p[1] - miny) * k
    for pl in f.get('polys', []):
        pts = [P(p) for p in pl['pts']]
        path = c.beginPath()
        path.moveTo(*pts[0])
        for p in pts[1:]:
            path.lineTo(*p)
        if pl.get('closed', True):
            path.close()
        c.setStrokeColor(INK)
        c.setLineWidth(pl.get('lw', 2))
        c.setFillColor(HexColor(pl['fill']) if pl.get('fill') else HexColor('#e6eff9'))
        if pl.get('dash'):
            c.setDash(5, 4)
        c.drawPath(path, fill=1 if pl.get('closed', True) and pl.get('fill', '#e6eff9') != 'none' else 0, stroke=1)
        c.setDash()
    for pl in f.get('polys', []):
        pts = [P(p) for p in pl['pts']]
        el = pl.get('el')
        if not el:
            continue
        ccw = poly_area(pts) > 0
        for i, lab in enumerate(el):
            if not lab:
                continue
            a, b = pts[i], pts[(i + 1) % len(pts)]
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = math.hypot(dx, dy)
            nx, ny = (dy / L, -dx / L) if ccw else (-dy / L, dx / L)
            tw = rich_w(lab, F, fs)
            off = 8 + abs(nx) * tw / 2 + abs(ny) * label_h(lab, fs) / 2
            draw_label(c, lab, (a[0] + b[0]) / 2 + nx * off, (a[1] + b[1]) / 2 + ny * off, fs)
    for sg in f.get('segs', []):
        a, b = P(sg['a']), P(sg['b'])
        c.setStrokeColor(sg.get('color', INK) if not isinstance(sg.get('color'), str) else HexColor(sg['color']))
        c.setLineWidth(1.6)
        if sg.get('dash', True):
            c.setDash(5, 4)
        c.line(a[0], a[1], b[0], b[1])
        c.setDash()
        if sg.get('label'):
            ox_, oy_ = sg.get('off', (10, 0))
            anc = 'l' if ox_ > 0 else ('r' if ox_ < 0 else 'c')
            draw_label(c, sg['label'], (a[0] + b[0]) / 2 + ox_, (a[1] + b[1]) / 2 + oy_, fs, anchor=anc)
    for ra in f.get('ra', []):
        v, p1, p2 = P(ra[0]), P(ra[1]), P(ra[2])
        m = 10
        u1 = ((p1[0] - v[0]), (p1[1] - v[1]))
        u2 = ((p2[0] - v[0]), (p2[1] - v[1]))
        l1, l2 = math.hypot(*u1), math.hypot(*u2)
        u1 = (u1[0] / l1 * m, u1[1] / l1 * m)
        u2 = (u2[0] / l2 * m, u2[1] / l2 * m)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        path = c.beginPath()
        path.moveTo(v[0] + u1[0], v[1] + u1[1])
        path.lineTo(v[0] + u1[0] + u2[0], v[1] + u1[1] + u2[1])
        path.lineTo(v[0] + u2[0], v[1] + u2[1])
        c.drawPath(path, stroke=1, fill=0)
    for t in f.get('texts', []):
        px, py = P((t[0], t[1]))
        anc = t[3] if len(t) > 3 else 'c'
        draw_label(c, t[2], px, py, fs * (t[4] if len(t) > 4 else 1), F, anchor=anc)
    for t in f.get('vlabels', []):
        px, py = P((t[0], t[1]))
        dx, dy = t[3] if len(t) > 3 else (0, 12)
        draw_label(c, t[2], px + dx, py + dy, fs * 1.05, FB, color=POINT)


def fig_prism(c, f, x, y, w, h, s):
    L, W_, Hh = f['l'], f['w'], f['h']
    fs = 15 * s
    ang = math.radians(35)
    dep = 0.55
    tw = L + W_ * dep * math.cos(ang)
    th = Hh + W_ * dep * math.sin(ang)
    pad = 50
    k = min((w - 2 * pad) / tw, (h - 2 * pad) / th)
    ox = x + (w - tw * k) / 2
    oy = y + (h - th * k) / 2
    dx, dy = W_ * dep * math.cos(ang) * k, W_ * dep * math.sin(ang) * k
    A = (ox, oy)
    B = (ox + L * k, oy)
    C = (ox + L * k, oy + Hh * k)
    D = (ox, oy + Hh * k)
    B2 = (B[0] + dx, B[1] + dy)
    C2 = (C[0] + dx, C[1] + dy)
    D2 = (D[0] + dx, D[1] + dy)
    A2 = (A[0] + dx, A[1] + dy)
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    fills = [HexColor('#e6eff9'), HexColor('#d2e2f3'), HexColor('#c0d6ee')]
    for poly, fl in (([A, B, C, D], fills[0]), ([D, C, C2, D2], fills[1]), ([B, B2, C2, C], fills[2])):
        path = c.beginPath()
        path.moveTo(*poly[0])
        for p in poly[1:]:
            path.lineTo(*p)
        path.close()
        c.setFillColor(fl)
        c.drawPath(path, fill=1, stroke=1)
    if f.get('grid'):
        c.setLineWidth(0.8)
        for i in range(1, int(L)):
            c.line(A[0] + i * k, A[1], D[0] + i * k, D[1])
            c.line(D[0] + i * k, D[1], D2[0] + i * k, D2[1])
        for j in range(1, int(Hh)):
            c.line(A[0], A[1] + j * k, B[0], B[1] + j * k)
            c.line(B[0], B[1] + j * k, B2[0], B2[1] + j * k)
        for m in range(1, int(W_)):
            t = m / W_
            c.line(D[0] + dx * t, D[1] + dy * t, C[0] + dx * t, C[1] + dy * t)
            c.line(B[0] + dx * t, B[1] + dy * t, C[0] + dx * t, C[1] + dy * t)
    if not f.get('grid'):
        c.setDash(4, 4)
        c.setLineWidth(1)
        c.line(A[0], A[1], A2[0], A2[1])
        c.line(A2[0], A2[1], B2[0], B2[1])
        c.line(A2[0], A2[1], D2[0], D2[1])
        c.setDash()
    labs = f.get('labels', (None, None, None))
    if labs[0]:
        draw_label(c, labs[0], (A[0] + B[0]) / 2, A[1] - 16, fs)
    if labs[2]:
        draw_label(c, labs[2], A[0] - 8, (A[1] + D[1]) / 2, fs, anchor='r')
    if labs[1]:
        draw_label(c, labs[1], (B[0] + B2[0]) / 2 + 10, (B[1] + B2[1]) / 2 - 6, fs, anchor='l')


def fig_tape(c, f, x, y, w, h, s):
    bars = f['bars']
    fs = 15 * s
    namew = max(sw(b.get('name', ''), FB, fs) for b in bars)
    namew = namew + 16 if namew else 0
    rightw = max([rich_w(b.get('right', ''), F, fs) for b in bars] + [0])
    rightw = rightw + 14 if rightw else 0
    maxn = max(b['n'] for b in bars)
    unit = min((w - namew - rightw - 10) / maxn, f.get('maxunit', 70))
    bh = f.get('bh', 34)
    gapv = 20 + (22 if any(b.get('brace') for b in bars) else 0)
    tot = len(bars) * bh + (len(bars) - 1) * gapv + (26 if bars[0].get('brace') else 0)
    x0 = x + namew + (w - namew - rightw - unit * maxn) / 2
    yy = y + (h + tot) / 2 - (26 if bars[0].get('brace') else 0)
    for b in bars:
        n = b['n']
        segw = unit * b.get('size', 1)
        bw = segw * n
        if b.get('brace'):
            c.setStrokeColor(INK)
            c.setLineWidth(1.2)
            c.line(x0, yy + 8, x0 + bw, yy + 8)
            c.line(x0, yy + 8, x0, yy + 3)
            c.line(x0 + bw, yy + 8, x0 + bw, yy + 3)
            draw_label(c, b['brace'], x0 + bw / 2, yy + 20, fs)
        for i in range(n):
            shaded = i < b.get('shade', 0)
            c.setFillColor(SHADE if shaded else white)
            c.setStrokeColor(INK)
            c.setLineWidth(1.5)
            c.rect(x0 + i * segw, yy - bh, segw, bh, fill=1, stroke=1)
            st = b.get('seg')
            if st:
                t = st[i] if isinstance(st, (list, tuple)) else st
                if t:
                    draw_label(c, t, x0 + i * segw + segw / 2, yy - bh / 2, fs * 0.9)
        if b.get('name'):
            draw_label(c, b['name'], x0 - 12, yy - bh / 2, fs, FB, anchor='r')
        if b.get('right'):
            draw_label(c, b['right'], x0 + bw + 12, yy - bh / 2, fs, anchor='l')
        yy -= bh + gapv


def fig_stack(c, f, x, y, w, h, s):
    lines = [fix_minus(t) for t in f['lines']]
    fs = 34 * s * f.get('fs', 1)
    lh = fs * 1.2
    n = len(lines)
    rule = f.get('rule', n - 1)
    tot = n * lh + 10
    if tot > h:
        fs *= h / tot
        lh = fs * 1.2
        tot = n * lh + 10
    maxw = max(sw(t, FM, fs) for t in lines)
    xr = x + w / 2 + maxw / 2 if f.get('center', True) else x + maxw + 20
    yy = y + (h + tot) / 2
    c.setFillColor(INK)
    for i, t in enumerate(lines):
        yy -= lh
        c.setFont(FM, fs)
        c.drawRightString(xr, yy + fs * 0.22, t)
        if i == rule - 1:
            c.setStrokeColor(INK)
            c.setLineWidth(1.8)
            c.line(xr - maxw - 8, yy - fs * 0.08, xr + 10, yy - fs * 0.08)
            yy -= 8


def fig_grid(c, f, x, y, w, h, s):
    R, C = f.get('rows', 10), f.get('cols', 10)
    n = f['shade']
    cell = min((w - 20) / C, (h - 20) / R, 22)
    gx = x + (w - cell * C) / 2
    gy = y + (h - cell * R) / 2
    for i in range(R):
        for j in range(C):
            idx = i * C + j
            c.setFillColor(SHADE if idx < n else white)
            c.setStrokeColor(HexColor('#6c7f95'))
            c.setLineWidth(0.8)
            c.rect(gx + j * cell, gy + (R - 1 - i) * cell, cell, cell, fill=1, stroke=1)


def fig_cyl(c, f, x, y, w, h, s):
    kind = f['k']
    r, hh = f['r'], f.get('h', f['r'])
    fs = 15 * s
    pad = 46
    if kind == 'sphere':
        k = min((w - 2 * pad) / (2 * r), (h - 2 * pad) / (2 * r))
        cx, cy = x + w / 2, y + h / 2
        R = r * k
        c.setStrokeColor(INK)
        c.setLineWidth(1.8)
        c.setFillColor(HexColor('#e6eff9'))
        c.circle(cx, cy, R, fill=1, stroke=1)
        c.setDash(4, 4)
        c.setLineWidth(1)
        c.ellipse(cx - R, cy - R * 0.25, cx + R, cy + R * 0.25, fill=0, stroke=1)
        c.setDash()
        c.setLineWidth(1.6)
        c.line(cx, cy, cx + R, cy)
        c.circle(cx, cy, 2.5, fill=1, stroke=0)
        draw_label(c, f.get('rlab', ''), cx + R / 2, cy + 12, fs)
        return
    k = min((w - 2 * pad) / (2 * r), (h - 2 * pad) / (hh + r * 0.5))
    R, Hh = r * k, hh * k
    e = R * 0.3
    cx = x + w / 2
    yb = y + (h - Hh - 2 * e) / 2 + e
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    c.setFillColor(HexColor('#e6eff9'))
    if kind == 'cyl':
        c.rect(cx - R, yb, 2 * R, Hh, fill=1, stroke=0)
        c.ellipse(cx - R, yb - e, cx + R, yb + e, fill=1, stroke=0)
        c.line(cx - R, yb, cx - R, yb + Hh)
        c.line(cx + R, yb, cx + R, yb + Hh)
        c.setFillColor(HexColor('#d2e2f3'))
        c.ellipse(cx - R, yb + Hh - e, cx + R, yb + Hh + e, fill=1, stroke=1)
        p = c.beginPath()
        p.arc(cx - R, yb - e, cx + R, yb + e, 180, 180)
        c.drawPath(p, stroke=1, fill=0)
        c.setDash(4, 4)
        c.setLineWidth(1)
        p = c.beginPath()
        p.arc(cx - R, yb - e, cx + R, yb + e, 0, 180)
        c.drawPath(p, stroke=1, fill=0)
        c.setDash()
        c.setLineWidth(1.6)
        c.line(cx, yb + Hh, cx + R, yb + Hh)
        c.setFillColor(INK)
        c.circle(cx, yb + Hh, 2.5, fill=1, stroke=0)
        draw_label(c, f.get('rlab', ''), cx + R / 2, yb + Hh + e + 12, fs)
        draw_label(c, f.get('hlab', ''), cx + R + 10, yb + Hh / 2, fs, anchor='l')
    else:  # cone
        p = c.beginPath()
        p.moveTo(cx - R, yb)
        p.lineTo(cx, yb + Hh)
        p.lineTo(cx + R, yb)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.ellipse(cx - R, yb - e, cx + R, yb + e, fill=1, stroke=0)
        c.line(cx - R, yb, cx, yb + Hh)
        c.line(cx + R, yb, cx, yb + Hh)
        p = c.beginPath()
        p.arc(cx - R, yb - e, cx + R, yb + e, 180, 180)
        c.drawPath(p, stroke=1, fill=0)
        c.setDash(4, 4)
        c.setLineWidth(1)
        p = c.beginPath()
        p.arc(cx - R, yb - e, cx + R, yb + e, 0, 180)
        c.drawPath(p, stroke=1, fill=0)
        c.line(cx, yb, cx, yb + Hh)
        c.setDash()
        c.setLineWidth(1.6)
        c.line(cx, yb, cx + R, yb)
        draw_label(c, f.get('rlab', ''), cx + R / 2, yb - e - 12, fs)
        draw_label(c, f.get('hlab', ''), cx - 8, yb + Hh * 0.45, fs, anchor='r')


def fig_pyramid(c, f, x, y, w, h, s):
    b, hh = f['b'], f['h']
    fs = 15 * s
    pad = 46
    dep = 0.45
    tw = b + b * dep * 0.8
    th = hh + b * dep * 0.55
    k = min((w - 2 * pad) / tw, (h - 2 * pad) / th)
    ox = x + (w - tw * k) / 2
    oy = y + (h - th * k) / 2
    dx, dy = b * dep * 0.8 * k, b * dep * 0.55 * k
    A = (ox, oy)
    B = (ox + b * k, oy)
    C = (B[0] + dx, B[1] + dy)
    D = (A[0] + dx, A[1] + dy)
    O = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    T = (O[0], O[1] + hh * k)
    c.setStrokeColor(INK)
    c.setLineWidth(1.8)
    c.setFillColor(HexColor('#e6eff9'))
    p = c.beginPath()
    p.moveTo(*A)
    p.lineTo(*B)
    p.lineTo(*T)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setFillColor(HexColor('#d2e2f3'))
    p = c.beginPath()
    p.moveTo(*B)
    p.lineTo(*C)
    p.lineTo(*T)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.setDash(4, 4)
    c.setLineWidth(1)
    c.line(A[0], A[1], D[0], D[1])
    c.line(D[0], D[1], C[0], C[1])
    c.line(D[0], D[1], T[0], T[1])
    c.line(T[0], T[1], O[0], O[1])
    M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    c.setDash()
    if f.get('slant'):
        c.setLineWidth(1.4)
        c.line(T[0], T[1], M[0], M[1])
    draw_label(c, f.get('blab', ''), M[0], M[1] - 14, fs)
    draw_label(c, f.get('hlab', ''), O[0] + 6, O[1] + (T[1] - O[1]) * 0.3, fs * 0.9, anchor='l')
    if f.get('slant'):
        draw_label(c, f['slant'], (T[0] + M[0]) / 2 - 8, (T[1] + M[1]) / 2 + 8, fs, anchor='r')


def fig_vstack(c, f, x, y, w, h, s):
    figs = f['figs']
    n = len(figs)
    slot = h / n
    for i, sub in enumerate(figs):
        yy = y + h - (i + 1) * slot
        draw_fig(c, sub, x, yy, w, slot, s)


def fig_hrow(c, f, x, y, w, h, s):
    figs = f['figs']
    n = len(figs)
    slot = w / n
    for i, sub in enumerate(figs):
        draw_fig(c, sub, x + i * slot, y, slot, h, s)


def fig_text(c, f, x, y, w, h, s):
    fs = f.get('fs', 22) * s
    lines = wrap(f['text'], FM if f.get('mono') else F, fs, w)
    th = lines_height(lines, fs)
    draw_lines(c, lines, x, y + (h + th) / 2, FM if f.get('mono') else F, fs, width=w, align=f.get('align', 'c'))


FIGS = {
    'nl': fig_numberline, 'coord': fig_coord, 'dot': fig_dot, 'hist': fig_hist, 'box': fig_box,
    'table': fig_table, 'shape': fig_shape, 'prism': fig_prism, 'tape': fig_tape, 'stack': fig_stack,
    'grid': fig_grid, 'cyl': fig_cyl, 'cone': fig_cyl, 'sphere': fig_cyl, 'pyramid': fig_pyramid,
    'vstack': fig_vstack, 'hrow': fig_hrow, 'text': fig_text,
}

RIGHT_KINDS = {'coord', 'shape', 'prism', 'grid', 'cyl', 'cone', 'sphere', 'pyramid'}


def draw_fig(c, f, x, y, w, h, s=1.0):
    c.saveState()
    FIGS[f['k']](c, f, x, y, w, h, s)
    c.restoreState()


def fig_pref_h(f, w):
    k = f['k']
    if 'h' in f:
        return f['h']
    if k == 'nl':
        return 250 if f.get('vertical') else (92 if (f.get('pts') or f.get('jumps')) else 64)
    if k == 'dot':
        return 150
    if k == 'hist':
        return 190
    if k == 'box':
        return 80 + 50 * len(f.get('boxes', [1]))
    if k == 'table':
        return 42 * len(f['rows']) + 6
    if k == 'tape':
        return 60 * len(f['bars']) + (28 if f['bars'][0].get('brace') else 0)
    if k == 'stack':
        return 44 * len(f['lines']) + 16
    if k == 'vstack':
        return sum(fig_pref_h(g, w) for g in f['figs'])
    if k == 'hrow':
        return max(fig_pref_h(g, w / len(f['figs'])) for g in f['figs'])
    if k == 'text':
        return 60
    return 220


# ---------------------------------------------------------------- page

def draw_label_box(c, label):
    c.setStrokeColor(RULE)
    c.setLineWidth(1.2)
    c.line(ML - 5, 84, PW - MR + 5, 84)
    c.setFillColor(LBG)
    c.roundRect(ML - 5, 18, CW + 10, 52, 8, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.setFont(FB, 7.6)
    c.drawString(ML + 8, 55, 'REFERENCE LABEL — NOT PART OF THE STUDENT QUESTION')
    size = 11.5
    while sw(label, FB, size) > CW - 20 and size > 7:
        size -= 0.25
    c.setFillColor(INK)
    c.setFont(FB, size)
    c.drawString(ML + 8, 33, label)


def page_number(c, n):
    c.setFillColor(MUTED)
    c.setFont(F, 8)
    c.drawRightString(PW - MR + 5, 7, str(n))


class Block:
    def __init__(self, h, fn):
        self.h, self.fn = h, fn


def text_block(text, font, size, width, color=INK, align='l'):
    lines = wrap(text, font, size, width)
    hh = lines_height(lines, size)

    def fn(c, x, ytop):
        draw_lines(c, lines, x, ytop, font, size, color, width=width, align=align)
    return Block(hh, fn), lines_width(lines, font, size)


def answer_block(ans, size, width, linew=None):
    labs = ans if isinstance(ans, (list, tuple)) else [ans]
    row_h = max(size * 1.9, 44)
    if any(has_frac([parse_word(w) for w in fix_minus(str(l)).split()]) for l in labs):
        row_h = max(row_h, size * 2.4)
    hh = row_h * len(labs)

    def fn(c, x, ytop):
        y = ytop
        for lab in labs:
            base = y - row_h + size * 0.45
            lw_ = 0
            if lab:
                lw_ = draw_label(c, lab, x, base + size * 0.36, size, anchor='l') + 14
            ln = linew or min(330, width - lw_ - 10)
            c.setStrokeColor(LINE)
            c.setLineWidth(1.8)
            c.line(x + lw_, base - 4, x + lw_ + ln, base - 4)
            y -= row_h
    return Block(hh, fn)


def choices_block(choices, size, width, cols, font=F):
    letters = 'ABCDEFGH'
    lw_ = sw('D.', FB, size) + size * 1.1
    colw = width / cols
    cells = []
    for i, ch in enumerate(choices):
        lines = wrap(str(ch), font, size, colw - lw_ - 12)
        cells.append((lines, lines_height(lines, size), lines_width(lines, font, size)))
    rows = [cells[i:i + cols] for i in range(0, len(cells), cols)]
    gap = size * (0.75 if cols == 1 else 0.6)
    rh = [max(cl[1] for cl in r) for r in rows]
    hh = sum(rh) + gap * (len(rows) - 1)
    fits = all(cl[2] <= colw - lw_ - 12 + 0.5 for cl in cells)

    def fn(c, x, ytop):
        y = ytop
        for ri, r in enumerate(rows):
            for ci, (lines, lh_, _) in enumerate(r):
                idx = ri * cols + ci
                xx = x + ci * colw
                a, _d = line_metrics(lines[0] or [], size)
                c.setFillColor(BLUE)
                c.setFont(FB, size)
                c.drawString(xx, y - a, letters[idx] + '.')
                draw_lines(c, lines, xx + lw_, y, font, size)
            y -= rh[ri] + gap
    return Block(hh, fn), fits


def fig_choice_block(figs, size, width, h):
    letters = 'ABCD'
    n = len(figs)
    colw = width / n

    def fn(c, x, ytop):
        for i, fg in enumerate(figs):
            xx = x + i * colw
            c.setFillColor(BLUE)
            c.setFont(FB, size)
            c.drawString(xx, ytop - size, letters[i] + '.')
            draw_fig(c, fg, xx + size * 1.4, ytop - h, colw - size * 1.6, h - 4, 0.8)
    return Block(h, fn)


def layout(q, s):
    """Return (fits, draw_fn) for scale s."""
    t = q['t']
    fig = q.get('fig')
    pos = q.get('pos') or (('right' if fig['k'] in RIGHT_KINDS else 'below') if fig else None)
    stem_size = q.get('fs', 24) * s
    ch_size = 22 * s
    blocks_left = []
    gap = 18 * s
    col_w = CW if pos != 'right' else CW * q.get('split', 0.53)
    fig_box_ = None

    if t == 'tf':
        b, _ = text_block('True or false?', FB, 23 * s, col_w)
        blocks_left.append(b)
        b, _ = text_block(q['stem'], F, 27 * s * q.get('fs', 24) / 24, col_w)
        blocks_left.append(b)
    else:
        b, _ = text_block(q['stem'], F, stem_size, col_w)
        blocks_left.append(b)

    if fig and pos == 'below':
        fh = fig_pref_h(fig, CW) * s

        def ffn(c, x, ytop, fig=fig, fh=fh):
            draw_fig(c, fig, x, ytop - fh, CW, fh, s)
        blocks_left.append(Block(fh, ffn))

    if q.get('cfigs'):
        blocks_left.append(fig_choice_block(q['cfigs'], ch_size, col_w, q.get('cfh', 150) * s))

    variants = [None]
    if t in ('mc', 'tf'):
        choices = q.get('ch') or ['True', 'False']
        if q.get('cfigs'):
            choices = None
        variants = []
        if choices:
            order = [q['cols']] if q.get('cols') else [1, 2, 4] if len(choices) == 4 else [1, len(choices)]
            for cols in order:
                cb, fits = choices_block(choices, ch_size, col_w, cols)
                if fits:
                    variants.append(cb)
            if not variants:
                cb, _ = choices_block(choices, ch_size, col_w, 1)
                variants.append(cb)
        else:
            variants = [None]
    elif t == 'sa':
        if q.get('ans', '') is not None:
            variants = [answer_block(q.get('ans', ''), stem_size, col_w, q.get('linew'))]
    for v in variants:
        bl = blocks_left + ([v] if v else [])
        total = sum(b.h for b in bl) + gap * (len(bl) - 1)
        avail = CT - CB
        if total <= avail:
            break
    fits = total <= avail
    if pos == 'right':
        fig_box_ = (ML + col_w + 20, CB, CW - col_w - 20, CT - CB + 6)

    def draw(c):
        y = CT
        extra = (avail - total)
        # answer line sits lower on the page when there is room, like the samples
        for i, b in enumerate(bl):
            if t == 'sa' and i == len(bl) - 1 and b is bl[-1] and v is not None and extra > 0:
                y -= min(extra * 0.6, 70)
            b.fn(c, ML, y)
            y -= b.h + gap
        if fig_box_:
            draw_fig(c, fig, *fig_box_, s=max(s, 0.85))
    return fits, draw


def render_question(c, q, label, pageno):
    draw_label_box(c, label)
    drawer = None
    for s in [1.0, 0.94, 0.88, 0.82, 0.76, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45]:
        fits, drawer = layout(q, s)
        if fits:
            break
    drawer(c)
    page_number(c, pageno)
