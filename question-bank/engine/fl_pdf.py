"""Financial Literacy PDFs: question collection and answer key with the same page numbers.
Each set starts with an overview page (its sections, backward branches with their reasons, math links, Go Deeper
chain); then one question per page: the Learn box (intro) and the question with its four choices, as on the game screen."""
import os
import shutil

from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

import fl_build as B

FONT_DIR = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('DV', FONT_DIR + 'DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB', FONT_DIR + 'DejaVuSans-Bold.ttf'))
F, FB = 'DV', 'DVB'
PW, PH = 612, 792
ML, MR, MT, MB = 54, 54, 54, 54
W = PW - ML - MR
INK = HexColor('#1b2430')
MUTED = HexColor('#5b6573')
BLUE = HexColor('#1f5fa8')
LEARN_BG = HexColor('#eaf2fb')
GREEN = HexColor('#1d7a46')
GREEN_BG = HexColor('#eaf6ef')
RED = HexColor('#9b2c2c')
LINE = HexColor('#c9d2dc')
PART = 800
SECTION_NAMES = {'M': 'MAIN', 'B': 'BACKWARD (concept review)', 'F': 'GO DEEPER'}


def sw(t, font, size):
    return pdfmetrics.stringWidth(t, font, size)


def wrap(text, font, size, width):
    lines = []
    for para in str(text).split('\n'):
        words, cur = para.split(' '), ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if sw(t, font, size) <= width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


class Page:
    def __init__(self, c):
        self.c, self.y = c, PH - MT

    def text(self, t, font=F, size=11, color=INK, indent=0, lead=1.35, width=None):
        lines = wrap(t, font, size, (width or W) - indent)
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        for ln in lines:
            self.y -= size * lead
            self.c.drawString(ML + indent, self.y, ln)
        return len(lines)

    def gap(self, h):
        self.y -= h

    def box(self, label, body, bg, color, size=11):
        lines = wrap(body, F, size, W - 24)
        h = len(lines) * size * 1.35 + 30
        self.c.setFillColor(bg)
        self.c.setStrokeColor(bg)
        self.c.roundRect(ML, self.y - h, W, h, 6, fill=1, stroke=0)
        self.c.setFillColor(color)
        self.c.setFont(FB, 8.5)
        self.c.drawString(ML + 12, self.y - 15, label.upper())
        self.c.setFillColor(INK)
        self.c.setFont(F, size)
        yy = self.y - 17
        for ln in lines:
            yy -= size * 1.35
            self.c.drawString(ML + 12, yy, ln)
        self.y -= h + 10


def header(c, left, right, pageno, title):
    c.setFillColor(MUTED)
    c.setFont(F, 8.5)
    room = PW - MR - ML - c.stringWidth(right, F, 8.5) - 12
    if c.stringWidth(left, F, 8.5) > room:  # shorten a long set title so it never runs into the question ID
        while c.stringWidth(left + '…', F, 8.5) > room:
            left = left[:-1]
        left = left.rstrip() + '…'
    c.drawString(ML, PH - 32, left)
    c.drawRightString(PW - MR, PH - 32, right)
    c.setStrokeColor(LINE)
    c.line(ML, PH - 38, PW - MR, PH - 38)
    c.drawCentredString(PW / 2, 30, '%s — page %d' % (title, pageno))


def sec_label(r):
    code = r['section']
    if code == 'M':
        return 'MAIN'
    if code[0] == 'B':
        return 'BACKWARD %s · concept review' % code
    return 'GO DEEPER %s' % code[1:]


def question_body(p, r, size=11.5):
    p.text('%s — %s' % (sec_label(r), r['section_skill']), FB, 10, BLUE)
    tags = ['Question %d of 5' % r['number'], 'Learn and Apply' if r['intro'] else 'Knowledge Check']
    if r['how_to']:
        tags.append('Practical how-to')
    p.text(' · '.join(tags), F, 8.5, MUTED)
    p.gap(8)
    if r['intro']:
        p.box('Learn', r['intro'], LEARN_BG, BLUE, size=10.5)
    p.text(r['question'], F, size)
    p.gap(6)
    for ch in r['choices']:
        p.gap(4)
        n = p.text('%s.  %s' % (ch['letter'], ch['text']), F, size - 0.5, indent=14)
        del n


def overview(p, s, recs_by_sec, answer=False):
    st = s['_std']
    p.text('SET %d · %s' % (s['num'], s['unit']['title']), FB, 9, MUTED)
    p.text(s['title'], FB, 17, INK, lead=1.4)
    p.text('MAIN skill: ' + s['skill'], F, 11)
    p.text('Outcome %s · National topic: %s · NJSLS 9.1.12: %s' % (st, s['nat'][0], ', '.join(s['nj'])), F, 9, MUTED)
    p.text('Learning target: ' + s['nat'][1], F, 9, MUTED)
    p.gap(8)
    p.text('If the MAIN attempt has 3 or fewer correct, the student works these backward sections in order, then '
           'returns to a fresh MAIN set:', FB, 10)
    for i, b in enumerate(s['back'], 1):
        if b['kind'] == 'math':
            r = b['ref']
            sid = '%s-S%02d-M' % (B.COURSE_PREFIX[r['course']], r['set'])
            cat = B.CATALOG[sid]
            p.text('B%d · Math link → %s (%s %s): %s' % (i, sid, r['course'].replace('_', ' ').title(), cat['ccss'], cat['name']), F, 9.5, indent=10)
        else:
            p.text('B%d · Concept review: %s (5 questions)' % (i, b['skill']), F, 9.5, indent=10)
        p.text('Why: ' + b['why'], F, 8.5, MUTED, indent=24)
    p.gap(6)
    p.text('After 5 of 5 correct, Go Deeper unlocks (a chain):', FB, 10)
    for i, g in enumerate(s['go'], 1):
        p.text('Go Deeper %d: %s (5 questions)' % (i, g['skill']), F, 9.5, indent=10)
    if s['extra']:
        p.gap(6)
        p.text('Practical skills beyond the standards: ' + '; '.join(s['extra']), F, 9, MUTED)
    p.gap(6)
    p.text('Content status: %s' % s['status'].replace('_', '-'), F, 9, MUTED)
    for x in s['sources']:
        p.text('Source: %s — %s %s' % (x['org'], x['claim'], x['url']), F, 8, MUTED, indent=10)
    if s['note']:
        p.text('Note: ' + s['note'], F, 8.5, MUTED)
    if answer:
        p.gap(6)
        p.text('Answer key for this set: %s' % ', '.join('%s %s' % (r['id'].split('-', 1)[1], r['correct_letter'])
                                                          for sec in recs_by_sec for r in sec), F, 8.5, GREEN)


def answer_body(p, r):
    p.text('%s — %s · Question %d of 5' % (sec_label(r), r['section_skill'], r['number']), FB, 9, BLUE)
    if r['intro']:
        p.text('Learn: ' + r['intro'], F, 8.5, MUTED)
    p.gap(3)
    p.text(r['question'], F, 9.5)
    for ch in r['choices']:
        p.text('%s.  %s' % (ch['letter'], ch['text']), FB if ch['letter'] == r['correct_letter'] else F, 9,
               GREEN if ch['letter'] == r['correct_letter'] else INK, indent=12, lead=1.3)
    p.gap(8)
    p.box('Correct answer', '%s. %s' % (r['correct_letter'], r['correct_answer']), GREEN_BG, GREEN, size=11)
    p.text('Feedback (shown after answering)', FB, 9, GREEN)
    p.text(r['feedback'], F, 10)
    if r['calc'] is not None:
        p.text('Recomputed independently by the build: %s' % fmt(r['calc']), F, 8.5, MUTED)
    p.gap(6)
    p.text('Why each other choice is wrong (misconception it represents)', FB, 9, RED)
    for x in 'ABCD':
        if x in r['misconceptions']:
            p.text('%s: %s' % (x, r['misconceptions'][x]), F, 9.5, indent=10)
    meta = ['Type: %s' % r['question_type'].replace('_', ' ')]
    if r['how_to']:
        meta.append('practical how-to')
    if r['effective_date']:
        meta.append('rule as of %s' % r['effective_date'])
    p.gap(4)
    p.text(' · '.join(meta), F, 8.5, MUTED)


def fmt(v):
    return ('%.6f' % v).rstrip('0').rstrip('.')


def render(path, sets, recs, set_pages, answer, first=1, last=None):
    c = canvas.Canvas(path, pagesize=(PW, PH))
    title = 'Financial Literacy %s v%s' % ('Answer Key' if answer else 'Question Collection', B.VERSION)
    c.setTitle(title)
    c.setAuthor('Untangle The Nexus question bank')
    by_set = {}
    for r in recs:
        by_set.setdefault(r['set'], []).append(r)
    for s in sets:
        s['_std'] = B.outcome_code(s)
        pg = set_pages[s['num']]
        if (last is None or pg <= last) and pg >= first:
            p = Page(c)
            header(c, 'Untangle The Nexus · Financial Literacy', 'Set %d overview' % s['num'], pg, title)
            secs = {}
            for r in by_set[s['num']]:
                secs.setdefault(r['section'], []).append(r)
            overview(p, s, list(secs.values()), answer)
            c.showPage()
        for r in by_set[s['num']]:
            if r['page'] < first or (last is not None and r['page'] > last):
                continue
            p = Page(c)
            header(c, 'Untangle The Nexus · Financial Literacy · Set %d: %s' % (s['num'], s['title']), r['id'], r['page'], title)
            (answer_body if answer else question_body)(p, r)
            if p.y < MB:
                raise SystemExit('text overflows the page: %s (%s)' % (r['id'], 'answer key' if answer else 'question'))
            c.showPage()
    c.save()


def write_pdfs(sets, recs, set_pages):
    for answer, name in ((False, 'FinancialLiteracy_Question_Collection.pdf'), (True, 'FinancialLiteracy_Answer_Key.pdf')):
        render(os.path.join(B.COL, name), sets, recs, set_pages, answer)
    total = max(r['page'] for r in recs)
    parts = (total + PART - 1) // PART
    pdir = os.path.join(B.COL, '_pdf_parts')
    if os.path.isdir(pdir):
        shutil.rmtree(pdir)
    os.makedirs(pdir)
    for i in range(parts):
        a, b = i * PART + 1, min(total, (i + 1) * PART)
        for answer, kind in ((False, 'questions'), (True, 'answers')):
            render(os.path.join(pdir, 'Financial Literacy - Part %d of %s.pdf' % (i + 1, kind)), sets, recs, set_pages, answer, a, b)


def copy_into_package(pkg):
    os.makedirs(os.path.join(pkg, 'pdf'), exist_ok=True)
    pdir = os.path.join(B.COL, '_pdf_parts')
    for f in sorted(os.listdir(pdir)):
        shutil.copy(os.path.join(pdir, f), os.path.join(pkg, 'pdf', f))
