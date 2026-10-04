"""One answer-key page: a reduced copy of the question page plus the answer."""
from reportlab.lib.colors import HexColor

import render as R

GREEN = HexColor('#1d7a46')
GBG = HexColor('#eaf6ef')
MINI = 0.56
TYPE_NAMES = {'mc': 'Multiple choice', 'tf': 'True or false', 'sa': 'Short answer',
              'plot': 'Drawing / plotting'}


def fit_lines(text, font, size, width, max_h, min_size=8):
    while True:
        lines = R.wrap(text, font, size, width)
        if R.lines_height(lines, size) <= max_h or size <= min_size:
            return lines, size
        size -= 0.5


def render_answer(c, q, label, pageno, qid, rec):
    form = 'q_' + qid.replace('-', '_')
    c.beginForm(form)
    R.render_question(c, q, label, pageno, qid)
    c.endForm()

    # kicker
    c.setFillColor(GREEN)
    c.setFont(R.FB, 11)
    c.drawString(R.ML - 5, 428, 'ANSWER KEY')
    c.setFillColor(R.MUTED)
    c.setFont(R.F, 9)
    c.drawString(R.ML + 5 + R.sw('ANSWER KEY', R.FB, 11) + 8, 428, 'Reduced copy of the question page, with its answer')

    # reduced question page
    mw, mh = R.PW * MINI, R.PH * MINI
    x0, y0 = R.ML - 5, 412 - mh
    c.saveState()
    c.translate(x0, y0)
    c.scale(MINI, MINI)
    c.doForm(form)
    c.restoreState()
    c.setStrokeColor(R.RULE)
    c.setLineWidth(1)
    c.rect(x0, y0, mw, mh, fill=0, stroke=1)

    # answer panel
    px = x0 + mw + 18
    pw = R.PW - R.MR + 5 - px
    top, bottom = 412, y0
    c.setFillColor(GBG)
    c.roundRect(px, bottom, pw, top - bottom, 8, fill=1, stroke=0)
    ix, iw = px + 12, pw - 24
    y = top - 18
    c.setFillColor(R.MUTED)
    c.setFont(R.FB, 8)
    c.drawString(ix, y, 'QUESTION ID')
    y -= 20
    c.setFillColor(R.INK)
    c.setFont(R.FB, 17)
    c.drawString(ix, y, qid)
    y -= 20
    c.setFillColor(R.MUTED)
    c.setFont(R.FB, 8)
    c.drawString(ix, y, 'TYPE')
    y -= 14
    c.setFillColor(R.INK)
    c.setFont(R.F, 11)
    c.drawString(ix, y, TYPE_NAMES[rec['type']])
    y -= 22
    c.setFillColor(R.MUTED)
    c.setFont(R.FB, 8)
    c.drawString(ix, y, 'CORRECT ANSWER')
    y -= 8
    text = ('%s.  %s' % (rec['letter'], rec['answer'])) if rec['letter'] else rec['answer']
    lines, size = fit_lines(text, R.FB, 17, iw, y - bottom - 10)
    R.draw_lines(c, lines, ix, y, R.FB, size, GREEN)

    # grading note
    if rec['note']:
        ny = bottom - 8
        c.setFillColor(R.MUTED)
        c.setFont(R.FB, 8)
        c.drawString(R.ML - 5, ny - 6, 'GRADING NOTE')
        lines, size = fit_lines(rec['note'], R.F, 10.5, R.CW + 10 - 78, ny - 90, 7)
        R.draw_lines(c, lines, R.ML + 73, ny + 2, R.F, size, R.INK)

    R.draw_label_box(c, label, qid)
    R.page_number(c, pageno)
