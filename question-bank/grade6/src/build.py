"""Builds the Grade 6 question collection PDF.

    python3 question-bank/grade6/src/build.py [out.pdf]
"""
import os
import sys

from reportlab.pdfgen import canvas

sys.path.insert(0, os.path.dirname(__file__))
import render as R  # noqa: E402
from qb import std_info, NEAREST_NOTE  # noqa: E402
import data_rp, data_ns, data_ee, data_g, data_sp  # noqa: E402,E401

DOMAIN_ORDER = [
    ('Ratios & Proportional Relationships', data_rp.SETS),
    ('The Number System', data_ns.SETS),
    ('Expressions & Equations', data_ee.SETS),
    ('Geometry', data_g.SETS),
    ('Statistics & Probability', data_sp.SETS),
]


def sections(st):
    """(key, name, std, questions, nearest) for each section of a set."""
    out = [('MAIN', 'Grade 6 main question', st['std'], st['main'], False)]
    for i, b in enumerate(st['back'], 1):
        out.append(('BACKWARD %d' % i, b['title'], b['std'], b['qs'], False))
    for key, b in (('FORWARD 1', st['f1']), ('FORWARD 2', st['f2'])):
        out.append((key, b['title'], b['std'], b['qs'], b.get('nearest', False)))
    return out


def all_sets():
    n = 0
    for dom, sets in DOMAIN_ORDER:
        for st in sets:
            n += 1
            st['num'] = n
            st['domain'] = dom
            yield st


TOC_PER_PAGE = 17


def heading_page(c, kicker, title, subtitle=None, rows=None, pageno=None):
    c.setFillColor(R.BLUE)
    c.setFont(R.FB, 13)
    c.drawString(R.ML, 380, kicker)
    size = 30
    lines = R.wrap(title, R.FB, size, R.CW)
    y = R.draw_lines(c, lines, R.ML, 368, R.FB, size)
    if subtitle:
        y = R.draw_lines(c, R.wrap(subtitle, R.F, 17, R.CW), R.ML, y - 6, R.F, 17, R.MUTED)
    if rows:
        y -= 16
        rs = 14 if len(rows) <= 8 else 12.5
        for sec, name, std in rows:
            c.setFillColor(R.BLUE)
            c.setFont(R.FB, rs)
            c.drawString(R.ML, y, sec)
            c.setFillColor(R.INK)
            c.setFont(R.F, rs)
            nm = name
            while R.sw(nm, R.F, rs) > 470 and len(nm) > 5:
                nm = nm[:-2]
            if nm != name:
                nm = nm.rstrip() + '…'
            c.drawString(R.ML + 118, y, nm)
            c.setFont(R.FB, rs)
            c.drawRightString(R.PW - R.MR, y, std)
            y -= rs * 1.75
    if pageno:
        R.page_number(c, pageno)


def build(out):
    sets = list(all_sets())
    ntoc = (len(sets) + TOC_PER_PAGE - 1) // TOC_PER_PAGE
    # page map
    page = 1 + ntoc
    for st in sets:
        page += 1
        st['page'] = page
        for sec in sections(st):
            page += 1 + len(sec[3])
    total_pages = page

    c = canvas.Canvas(out, pagesize=(R.PW, R.PH))
    c.setTitle('Grade 6 Common Core Math — Question Collection')
    c.setAuthor('Math Lab')

    # cover
    nq = sum(len(sec[3]) for st in sets for sec in sections(st))
    c.setFillColor(R.BLUE)
    c.rect(0, R.PH - 12, R.PW, 12, fill=1, stroke=0)
    c.setFont(R.FB, 14)
    c.drawString(R.ML, 330, 'GRADE 6 COMMON CORE MATH')
    c.setFillColor(R.INK)
    c.setFont(R.FB, 40)
    c.drawString(R.ML, 280, 'Question Collection')
    c.setFont(R.F, 18)
    c.setFillColor(R.MUTED)
    c.drawString(R.ML, 245, 'Main • Backward Branches • Forward 1 (Grade 7) • Forward 2 (Grade 8)')
    c.drawString(R.ML, 218, '%d question sets • %d questions' % (len(sets), nq))
    c.bookmarkPage('cover')
    c.addOutlineEntry('Cover', 'cover', 0)
    c.showPage()

    # table of contents
    for t in range(ntoc):
        c.setFillColor(R.BLUE)
        c.setFont(R.FB, 13)
        c.drawString(R.ML, 400, 'CONTENTS' + ('' if t == 0 else ' (continued)'))
        y = 374
        for st in sets[t * TOC_PER_PAGE:(t + 1) * TOC_PER_PAGE]:
            c.setFillColor(R.INK)
            c.setFont(R.FB, 11.5)
            c.drawString(R.ML, y, 'Set %d' % st['num'])
            c.drawString(R.ML + 58, y, st['std'])
            c.setFont(R.F, 11.5)
            title = st['title']
            while R.sw(title, R.F, 11.5) > 480:
                title = title[:-2]
            c.drawString(R.ML + 150, y, title)
            c.drawRightString(R.PW - R.MR, y, str(st['page']))
            c.linkAbsolute('', 'set%d' % st['num'], (R.ML, y - 4, R.PW - R.MR, y + 12))
            y -= 21
        if t == 0:
            c.bookmarkPage('toc')
            c.addOutlineEntry('Contents', 'toc', 0)
        R.page_number(c, 2 + t)
        c.showPage()

    pageno = 1 + ntoc
    cur_dom, cur_std = None, None
    for st in sets:
        if st['domain'] != cur_dom:
            cur_dom = st['domain']
            c.bookmarkPage('dom%d' % st['num'])
            c.addOutlineEntry(cur_dom, 'dom%d' % st['num'], 0, closed=True)
        if st['std'] != cur_std:
            cur_std = st['std']
            c.addOutlineEntry(cur_std, 'set%d' % st['num'], 1, closed=True)
        pageno += 1
        secs = sections(st)
        rows = [(s[0], s[1] + (' \u2014 nearest related (no direct Grade 8 step)' if s[4] else ''), s[2]) for s in secs]
        heading_page(c, 'SET %d  •  %s  •  %s' % (st['num'], st['std'], st['domain'].upper()),
                     st['title'], None, rows, pageno)
        c.bookmarkPage('set%d' % st['num'])
        c.addOutlineEntry('Set %d — %s' % (st['num'], st['title']), 'set%d' % st['num'], 2, closed=True)
        c.showPage()
        for key, name, std, qs, nearest in secs:
            grade, dom = std_info(std)
            pageno += 1
            sub = '%s  •  %s  •  %s  •  %s' % (name, grade, dom, std)
            if nearest:
                sub += '\n⚑ ' + NEAREST_NOTE
            heading_page(c, 'SET %d  •  %s' % (st['num'], st['std']), key, sub, None, pageno)
            anchor = 'set%d_%s' % (st['num'], key.replace(' ', ''))
            c.bookmarkPage(anchor)
            c.addOutlineEntry('%s — %s' % (key, std), anchor, 3)
            c.showPage()
            for i, q in enumerate(qs, 1):
                pageno += 1
                label = '%s  •  %s  •  %s  •  Set %d  •  %s  •  Q%d/%d' % (
                    grade, dom, std, st['num'], key.title().replace('Main', 'MAIN'), i, len(qs))
                label = label.replace('Backward', 'BACKWARD').replace('Forward', 'FORWARD')
                if nearest:
                    label += '  \u2022  NEAREST RELATED'
                try:
                    R.render_question(c, q, label, pageno)
                except Exception as e:
                    raise RuntimeError('Set %d %s Q%d: %s' % (st['num'], key, i, e))
                c.showPage()
    assert pageno == total_pages, (pageno, total_pages)
    c.save()
    return len(sets), nq, total_pages


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(__file__), '..', 'Grade6_Question_Collection.pdf')
    print(build(out))
