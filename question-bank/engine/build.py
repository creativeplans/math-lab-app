"""Builds a grade's question collection PDF and its matching answer key.

    python3 question-bank/engine/build.py grade6      (or grade5, ...)

writes, into question-bank/<grade>/:
    Grade<N>_Question_Collection.pdf   the questions
    Grade<N>_Answer_Key.pdf            same page numbers; each question page shows a
                                       reduced copy of the question plus its answer
    Grade<N>_Answer_Key.json / .csv    machine-readable key, one record per question ID

A grade folder holds src/grade.py (GRADE and the ordered domain modules), the
src/data_*.py question modules, and optionally src/answers/key_*.txt.
"""
import csv
import importlib
import json
import os
import sys

from reportlab.pdfgen import canvas

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
import render as R  # noqa: E402
import answers as A  # noqa: E402
import keycard  # noqa: E402
import qb  # noqa: E402
from qb import std_info  # noqa: E402

GRADE = None
GRADE_DIR = None
DOMAIN_ORDER = []
COLLECTION = {}  # id (namespace for question IDs, e.g. G5), version, date: from src/grade.py


def load_grade(name):
    """Load question-bank/<name> (for example 'grade6'). Call once per process."""
    global GRADE, GRADE_DIR, DOMAIN_ORDER
    GRADE_DIR = os.path.join(os.path.dirname(ENGINE), name)
    sys.path.insert(0, os.path.join(GRADE_DIR, 'src'))
    cfg = importlib.import_module('grade')
    GRADE = cfg.GRADE
    qb.GRADE = GRADE
    qb.STRICT_BACKWARD = getattr(cfg, 'STRICT_BACKWARD', False)
    COLLECTION.clear()
    COLLECTION.update(id='G%d' % GRADE, grade=GRADE, version=getattr(cfg, 'VERSION', '1.0.0'),
                      date=getattr(cfg, 'VERSION_DATE', None))
    A.KEY_DIR = os.path.join(GRADE_DIR, 'src', 'answers')
    DOMAIN_ORDER = [(dom, importlib.import_module(mod).SETS) for dom, mod in cfg.DOMAINS]
    A.PLAN.clear()
    if getattr(cfg, 'BALANCE_MC', False):
        akey = A.load_key()
        items = []
        for st in all_sets():
            for key, name, std, qs, nearest in sections(st):
                raws = akey.get('S%d-%s' % (st['num'], A.section_code(key)))
                for i, q in enumerate(qs, 1):
                    if A.balanced(q):
                        items.append(A.qid(st['num'], key, i))
        frozen = {}
        plan_file = os.path.join(GRADE_DIR, 'src', 'choice_plan.json')
        if os.path.exists(plan_file):
            frozen = json.load(open(plan_file))
        A.make_plan(items, GRADE, frozen)
    return GRADE


def sections(st):
    """(key, name, std, questions, nearest) for each section of a set."""
    out = [('MAIN', 'Grade %d main question' % GRADE, st['std'], st['main'], False)]
    nums = [b.get('fixed_num', i) for i, b in enumerate(st['back'], 1)]
    assert len(set(nums)) == len(nums), (st['title'], nums)
    for n, b in zip(nums, st['back']):
        out.append(('BACKWARD %d' % n, b['title'], b['std'], b['qs'], False))
    for key, b in (('FORWARD 1', st['f1']), ('FORWARD 2', st['f2'])):
        out.append((key, b['title'], b['std'], b['qs'], b.get('nearest', False)))
    return out


def all_sets():
    """Sets in collection order. A set's number is fixed_num when given, else the next count."""
    n = 0
    seen = set()
    for dom, sets in DOMAIN_ORDER:
        for st in sets:
            if 'fixed_num' in st:
                st['num'] = st['fixed_num']
            else:
                n += 1
                st['num'] = n
            assert st['num'] not in seen, 'duplicate set number %d' % st['num']
            seen.add(st['num'])
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


def build(out, mode='questions'):
    """mode is 'questions' or 'key'. Returns (sets, questions, pages, records)."""
    is_key = mode == 'key'
    akey = A.load_key()
    records = []
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
    c.setTitle('Grade %d Common Core Math — ' % GRADE + ('Answer Key' if is_key else 'Question Collection'))
    c.setAuthor('Math Lab')

    # cover
    nq = sum(len(sec[3]) for st in sets for sec in sections(st))
    c.setFillColor(R.BLUE)
    c.rect(0, R.PH - 12, R.PW, 12, fill=1, stroke=0)
    c.setFont(R.FB, 14)
    c.drawString(R.ML, 330, 'GRADE %d COMMON CORE MATH' % GRADE)
    c.setFillColor(R.INK)
    c.setFont(R.FB, 40)
    c.drawString(R.ML, 280, 'Answer Key' if is_key else 'Question Collection')
    c.setFont(R.F, 18)
    c.setFillColor(R.MUTED)
    c.drawString(R.ML, 245, 'Main • Backward Branches • Forward 1 (Grade %d) • Forward 2 (Grade %d)' % (GRADE + 1, GRADE + 2))
    c.drawString(R.ML, 218, '%d question sets • %d questions' % (len(sets), nq))
    if is_key:
        c.drawString(R.ML, 191, 'Page numbers match the Question Collection.')
        c.drawString(R.ML, 166, 'Every page shows its question ID (for example S40-F2-Q3).')
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
        rows = [(s[0], s[1] + (' \u2014 nearest related (no direct Grade %d step)' % (GRADE + 2) if s[4] else ''), s[2]) for s in secs]
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
                sub += '\n⚑ ' + qb.nearest_note()
            heading_page(c, 'SET %d  •  %s' % (st['num'], st['std']), key, sub, None, pageno)
            anchor = 'set%d_%s' % (st['num'], key.replace(' ', ''))
            c.bookmarkPage(anchor)
            c.addOutlineEntry('%s — %s' % (key, std), anchor, 3)
            c.showPage()
            raws = akey.get('S%d-%s' % (st['num'], A.section_code(key)))
            for i, q in enumerate(qs, 1):
                pageno += 1
                qid = A.qid(st['num'], key, i)
                raw = raws[i - 1] if raws else A.inline_raw(q)
                err = A.validate(q, raw)
                if err:
                    raise ValueError('%s: %s' % (qid, err))
                qd, letter = A.present(q, qid, A.split_note(raw)[0])
                label = '%s  •  %s  •  %s  •  Set %d  •  %s  •  Q%d/%d' % (
                    grade, dom, std, st['num'], key.title().replace('Main', 'MAIN'), i, len(qs))
                label = label.replace('Backward', 'BACKWARD').replace('Forward', 'FORWARD')
                if nearest:
                    label += '  \u2022  NEAREST RELATED'
                rec = A.answer_record(q, qd, raw, letter)
                try:
                    if is_key:
                        keycard.render_answer(c, qd, label, pageno, qid, rec)
                    else:
                        R.render_question(c, qd, label, pageno, qid)
                except Exception as e:
                    raise RuntimeError('Set %d %s Q%d: %s' % (st['num'], key, i, e))
                c.showPage()
                records.append(dict(
                    id=qid, uid='%s:%s' % (COLLECTION['id'], qid), page=pageno, set=st['num'], set_title=st['title'], set_standard=st['std'],
                    section=key, section_title=name, standard=std, grade=grade, domain=dom,
                    number=i, of=len(qs), nearest_related=bool(nearest), type=rec['type'],
                    question=A.plain(qd['stem']).replace('\n', ' '),
                    has_figure=bool(qd.get('fig') or qd.get('cfigs')),
                    choices=([dict(letter=A.LETTERS[j], text=A.plain(ch)) for j, ch in enumerate(qd['ch'])]
                             if rec['type'] == 'mc' and not qd.get('cfigs') else
                             [dict(letter=A.LETTERS[j], text='(picture)') for j in range(len(qd['cfigs']))]
                             if qd.get('cfigs') else
                             [dict(letter='A', text='True'), dict(letter='B', text='False')]
                             if rec['type'] == 'tf' else []),
                    answer_lines=([] if rec['type'] in ('mc', 'tf', 'plot') else
                                  (qd.get('ans') if isinstance(qd.get('ans'), list) else [qd.get('ans') or ''])),
                    correct_letter=rec['letter'], correct_answer=rec['answer'],
                    drawing_answer=rec.get('drawing'), required_method=rec.get('method'),
                    grading_note=rec['note']))
    assert pageno == total_pages, (pageno, total_pages)
    c.save()
    return len(sets), nq, total_pages, records


GRADING_RULES = [
    'Match each student response to its key record by the question ID printed on the question page '
    '(for example S40-F2-Q3). The page number is the same in the Question Collection and the Answer Key. '
    'IDs are unique within one grade\'s collection; across collections use uid (for example G5:S40-F2-Q3).',
    'Multiple choice and true/false: the response is correct when the chosen letter equals correct_letter, '
    'or when the student wrote the text of the correct choice.',
    'Short answer: accept any mathematically equivalent form unless the question asks for a specific form '
    '(equivalent fractions, decimals, and mixed numbers; a ratio written as a : b, a to b, or a/b; '
    '"x = 5" or "5"; terms of an expression in any order). Units are not required unless the question asks for them.',
    'When an answer has several parts (separated by semicolons, or with labels such as "Rate of change:"), '
    'every part must be correct.',
    'Drawing / plotting questions (type plot): correct_answer describes what a correct drawing shows. Judge the student\'s drawing against it.',
    'Drawing + written questions (type plot_text): the student draws on the figure AND writes an answer. drawing_answer '
    'describes the correct drawing and correct_answer the written answer. Both must be correct: every requested point, '
    'segment or shape in the drawing, and the written conclusion.',
    'Answer with required work (type work): required_method says what the shown work must use. A correct final answer '
    'without that work earns partial credit only; correct work with a slip in the final answer is also partial.',
    'Explain / describe questions: grading_note says what a correct response must include; accept any reasonable wording.',
    'grading_note also lists other accepted answers and the work behind an answer. It is guidance for the grader, not for students.',
]


def write_data(records, base):
    with open(base + '.json', 'w', encoding='utf-8') as f:
        json.dump(dict(title='Grade %d Common Core Math — Answer Key' % GRADE, collection=COLLECTION,
                       question_count=len(records),
                       id_format='S<set>-<section>-Q<number>; section is M (main), B1, B2, ... (backward), F1 or F2 (forward)',
                       grading_rules=GRADING_RULES, questions=records), f, ensure_ascii=False, indent=1)
    cols = ['uid', 'id', 'page', 'set', 'section', 'number', 'standard', 'type', 'question', 'choices',
            'correct_letter', 'correct_answer', 'drawing_answer', 'required_method', 'grading_note']
    with open(base + '.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in records:
            row = dict(r, choices=' | '.join('%s. %s' % (ch['letter'], ch['text']) for ch in r['choices']))
            w.writerow([row[k] if row[k] is not None else '' for k in cols])


def out_paths():
    n = GRADE
    return dict(questions=os.path.join(GRADE_DIR, 'Grade%d_Question_Collection.pdf' % n),
                key=os.path.join(GRADE_DIR, 'Grade%d_Answer_Key.pdf' % n),
                data=os.path.join(GRADE_DIR, 'Grade%d_Answer_Key' % n))


if __name__ == '__main__':
    load_grade(sys.argv[1] if len(sys.argv) > 1 else 'grade6')
    p = out_paths()
    qs = build(p['questions'], 'questions')
    ks = build(p['key'], 'key')
    assert qs[:3] == ks[:3]
    write_data(ks[3], p['data'])
    print('grade %d: sets %d, questions %d, pages %d' % ((GRADE,) + qs[:3]))
    if qb.SAME_GRADE_BACKWARD:
        print('warning: %d backward branches use a Grade %d standard:' % (len(qb.SAME_GRADE_BACKWARD), GRADE))
        for t in qb.SAME_GRADE_BACKWARD:
            print('   %s | %s | %s' % t)
