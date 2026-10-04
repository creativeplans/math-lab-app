"""Untangle The Nexus import package for one grade.

    python3 question-bank/engine/export.py grade6

Run build.py for the grade first (the PDFs are copied into the package). Writes
question-bank/nexus/<grade>/:

    README.md          how to import
    index.json         every set and section, its file, and branch relationships
    sets/S01.json ...  one file per question set; each question is a complete record
    assets/<ID>.svg    every figure (PNG copy alongside); choice pictures are <ID>-A.svg ...
    pdf/               the question collection and answer key, in 800-page parts

No question depends on the PDF: each record carries its text, choices, answer or
grading criteria, and, for figures, the asset files, the figure's data and a
plain-text description.
"""
import json
import os
import shutil
import sys

import pymupdf
from reportlab.pdfgen import canvas

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
import build  # noqa: E402
import render as R  # noqa: E402
import answers as A  # noqa: E402

FORMAT_VERSION = 1
PDF_PART = 800
RELATION = {'M': 'main', 'F1': 'forward1', 'F2': 'forward2'}


# ------------------------------------------------------------ descriptions

def num(v):
    if isinstance(v, float):
        if abs(v - round(v)) < 1e-9:
            return str(int(round(v)))
        for d in (2, 3, 4, 6, 8, 10, 12):
            if abs(v * d - round(v * d)) < 1e-6:
                n = int(round(v * d))
                w, r = divmod(abs(n), d)
                from math import gcd
                g = gcd(r, d)
                frac = '%d/%d' % (r // g, d // g)
                s = ('%d %s' % (w, frac)) if w else frac
                return ('-' if n < 0 else '') + s
        return ('%.4f' % v).rstrip('0')
    return str(v)


def pt(p):
    return '(%s, %s)' % (num(p[0]), num(p[1]))


def label_of(f, v):
    labels = f.get('labels')
    if isinstance(labels, dict):
        for k, t in labels.items():
            if abs(k - v) < 1e-9:
                return A.plain(t)
    return num(v)


def decimal_line(f):
    """True when a number line is labeled in decimals rather than fractions."""
    labels = f.get('labels')
    if isinstance(labels, dict) and any('{' in str(t) for t in labels.values()):
        return False
    step = f['step']
    return abs(round(step, 2) - step) < 1e-9


def dnum(v):
    v = round(v, 6)
    return str(int(v)) if v == int(v) else ('%.6f' % v).rstrip('0')


def describe(f):
    if f.get('desc'):
        return f['desc']
    k = f['k']
    if k == 'nl':
        n = dnum if decimal_line(f) else num
        d = '%s number line from %s to %s, tick marks every %s' % (
            'Vertical' if f.get('vertical') else 'Horizontal', n(f['min']), n(f['max']), n(f['step']))
        if f.get('minor'):
            d += ' (smaller ticks between)'
        parts = [d]
        if f.get('pts'):
            parts.append('Points: ' + ', '.join('%s at %s' % (A.plain(p[1]), n(p[0])) if p[1] else 'a point at %s' % n(p[0])
                                               for p in f['pts']))
        for j in f.get('jumps', []):
            parts.append('Arrow from %s to %s labeled "%s"' % (n(j[0]), n(j[1]), A.plain(j[2] or '')))
        if f.get('ray'):
            v, dirn, op = f['ray']
            parts.append('Graph: %s circle at %s with the line shaded to the %s' % (
                'open' if op else 'closed (filled)', n(v), dirn))
        if not (f.get('pts') or f.get('jumps') or f.get('ray')):
            parts.append('Nothing is marked; the student draws on it')
        return '. '.join(parts) + '.'
    if k == 'coord':
        x, y = f['x'], f['y']
        parts = ['Coordinate grid with x from %s to %s and y from %s to %s' % (num(x[0]), num(x[1]), num(y[0]), num(y[1]))]
        if f.get('xlabel'):
            parts.append('x-axis label "%s", y-axis label "%s"' % (f['xlabel'], f.get('ylabel', '')))
        if f.get('pts'):
            parts.append('Points: ' + ', '.join(('%s %s' % (p[2], pt(p))) if len(p) > 2 and p[2] else pt(p)
                                               for p in f['pts']))
        for ln in f.get('lines', []):
            parts.append('Straight line through %s and %s' % (pt(ln[0]), pt(ln[1])))
        for pg in f.get('polys', []):
            parts.append('Polygon with vertices ' + ', '.join(pt(p) for p in pg))
        if not (f.get('pts') or f.get('lines') or f.get('polys')):
            parts.append('Nothing is plotted; the student draws on it')
        return '. '.join(parts) + '.'
    if k == 'dot':
        title = f.get('title') or f.get('xlabel') or ''
        items = ['%s: %d' % (label_of(f, v), n) for v, n in sorted(f['data'].items())]
        return 'Dot plot%s, number line from %s to %s. Dots per value: %s.' % (
            (' titled "%s"' % title) if title else '', label_of(f, f['min']), label_of(f, f['max']), ', '.join(items))
    if k == 'hist':
        kind = 'Histogram' if any('–' in str(b) for b in f['bins']) else 'Bar graph'
        lab = ''
        if f.get('xlabel') or f.get('ylabel'):
            lab = ' (x-axis "%s", y-axis "%s")' % (f.get('xlabel', ''), f.get('ylabel', ''))
        if not any(f['counts']):
            return 'Blank %s grid%s with categories %s; the student draws the bars.' % (
                kind.lower(), lab, ', '.join(str(b) for b in f['bins']))
        return '%s%s. %s.' % (kind, lab, ', '.join('%s: %s' % (b, c) for b, c in zip(f['bins'], f['counts'])))
    if k == 'box':
        boxes = f.get('boxes') or [(None, f['five'])]
        out = []
        for name, five in boxes:
            out.append('%sminimum %s, Q1 %s, median %s, Q3 %s, maximum %s' % (
                (name + ': ') if name else '', *[num(v) for v in five]))
        return 'Box plot on a number line from %s to %s. %s.' % (num(f['min']), num(f['max']), '; '.join(out))
    if k == 'table':
        return 'Table. ' + ' / '.join(' | '.join(A.plain(str(c)) for c in row) for row in f['rows']) + '.'
    if k == 'shape':
        parts = []
        for p in f['polys']:
            pts = p['pts']
            labs = []
            for i, lab in enumerate(p.get('el') or []):
                if lab:
                    labs.append('"%s" on the side from %s to %s' % (A.plain(lab), pt(pts[i]), pt(pts[(i + 1) % len(pts)])))
            s = '%d-sided polygon with vertices %s' % (len(pts), ', '.join(pt(q) for q in pts))
            if labs:
                s += '; labels: ' + '; '.join(labs)
            parts.append(s)
        for sg in f.get('segs', []):
            if sg.get('label'):
                parts.append('Dashed segment from %s to %s labeled "%s"' % (pt(sg['a']), pt(sg['b']), A.plain(sg['label'])))
            else:
                parts.append('Dashed segment from %s to %s' % (pt(sg['a']), pt(sg['b'])))
        for t in f.get('texts', []):
            parts.append('Text "%s" at %s' % (A.plain(t[2]), pt(t)))
        if f.get('ra'):
            parts.append('Right-angle marks are shown')
        n = len(f['polys'])
        head = 'Figure made of %d connected shapes (a net or composite figure). ' % n if n > 1 else ''
        return head + '. '.join(parts) + '.'
    if k == 'prism':
        labs = [l for l in f['labels'] if l]
        if f.get('grid'):
            return 'Rectangular prism built from unit cubes: %s cubes long, %s cubes wide, %s cubes tall.' % (
                num(f['l']), num(f['w']), num(f['h']))
        return 'Rectangular prism with edges labeled %s (length, width, height).' % ', '.join(A.plain(l) for l in labs)
    if k == 'tape':
        out = []
        for b in f['bars']:
            s = '%sbar divided into %d equal parts, %d shaded' % (
                (b['name'] + ': ') if b.get('name') else '', b['n'], b.get('shade', 0))
            seg = b.get('seg')
            if seg:
                s += '; part labels: ' + ', '.join(A.plain(t) or '(blank)' for t in (seg if isinstance(seg, (list, tuple)) else [seg] * b['n']))
            if b.get('brace'):
                s += '; a brace over the whole bar reads "%s"' % A.plain(b['brace'])
            if b.get('right'):
                s += '; label at the right: "%s"' % A.plain(b['right'])
            out.append(s)
        return 'Tape diagram. ' + '. '.join(out) + '.'
    if k == 'stack':
        return 'Vertical arithmetic, digits right-aligned: ' + ' / '.join(f['lines']) + (
            ' (a line is drawn under row %d)' % f['rule'] if f.get('rule') else '') + '.'
    if k == 'cyl':
        return 'Cylinder with radius labeled "%s" and height labeled "%s".' % (f.get('rlab', ''), f.get('hlab', ''))
    if k == 'cone':
        return 'Cone with radius labeled "%s" and height labeled "%s".' % (f.get('rlab', ''), f.get('hlab', ''))
    if k == 'sphere':
        return 'Sphere with radius labeled "%s".' % f.get('rlab', '')
    if k == 'pyramid':
        return 'Square pyramid with base edge labeled "%s", height labeled "%s", slant height labeled "%s".' % (
            f.get('blab', ''), f.get('hlab', ''), f.get('slant', ''))
    if k in ('vstack', 'hrow'):
        return ' '.join('[%d] %s' % (i, describe(g)) for i, g in enumerate(f['figs'], 1))
    if k == 'grid':
        return 'Grid of %d by %d squares with %d squares shaded.' % (f.get('rows', 10), f.get('cols', 10), f['shade'])
    if k == 'text':
        return A.plain(f.get('text', ''))
    return k


def jsonable(f):
    if isinstance(f, dict):
        return {k: jsonable(v) for k, v in f.items()}
    if isinstance(f, (list, tuple)):
        return [jsonable(v) for v in f]
    if isinstance(f, float) and abs(f - round(f)) < 1e-12:
        return int(round(f))
    return f


# ------------------------------------------------------------ figure files

def fig_box(f):
    if f['k'] in R.RIGHT_KINDS:
        return 360, 300
    w = R.CW
    if f['k'] == 'hrow':
        return w, max(R.fig_pref_h(g, w / len(f['figs'])) if g['k'] not in R.RIGHT_KINDS else 260 for g in f['figs'])
    return w, R.fig_pref_h(f, w)


def write_figure(f, base):
    """Render one figure to base.svg and base.png, cropped to the drawing."""
    w, h = fig_box(f)
    pad = 24
    tmp = base + '.tmp.pdf'
    c = canvas.Canvas(tmp, pagesize=(w + 2 * pad, h + 2 * pad))
    R.draw_fig(c, f, pad, pad, w, h, 1.0)
    c.showPage()
    c.save()
    doc = pymupdf.open(tmp)
    page = doc[0]
    rect = None
    for d in page.get_drawings():
        rect = d['rect'] if rect is None else rect | d['rect']
    for b in page.get_text('blocks'):
        r = pymupdf.Rect(b[:4])
        rect = r if rect is None else rect | r
    if rect is not None:
        page.set_cropbox((rect + (-8, -8, 8, 8)) & page.mediabox)
    with open(base + '.svg', 'w', encoding='utf-8') as fh:
        fh.write(page.get_svg_image(text_as_path=True))
    page.get_pixmap(dpi=144).save(base + '.png')
    doc.close()
    os.remove(tmp)


# ------------------------------------------------------------ package

GRADING_RULES = None  # filled from build.GRADING_RULES


def export(out_dir):
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    for sub in ('sets', 'assets', 'pdf'):
        os.makedirs(os.path.join(out_dir, sub))
    paths = build.out_paths()
    _, nq, npages, records = build.build(os.path.join(out_dir, 'tmp_key.pdf'), 'key')
    os.remove(os.path.join(out_dir, 'tmp_key.pdf'))
    by_id = {r['id']: r for r in records}
    akey = A.load_key()

    index_sets = []
    nfig = 0
    for st in build.all_sets():
        sid = 'S%d' % st['num']
        fname = 'sets/S%02d.json' % st['num']
        sections = []
        for key, name, std, qs, nearest in build.sections(st):
            code = A.section_code(key)
            if code == 'M':
                name = st['title']
            raws = akey.get('%s-%s' % (sid, code))
            qrecs = []
            for i, q in enumerate(qs, 1):
                qid = A.qid(st['num'], key, i)
                raw = raws[i - 1] if raws else A.inline_raw(q)
                qd, _letter = A.present(q, qid, A.split_note(raw)[0])
                r = by_id[qid]
                rec = dict(
                    id=qid, set=st['num'], section=key, section_code=code,
                    relation=RELATION.get(code, 'backward'), number=i, of=len(qs),
                    standard=std, standard_grade=int(std.split('.')[0]) if std[0].isdigit() else std.split('.')[0],
                    domain=r['domain'], skill=name, nearest_related=bool(nearest),
                    type=r['type'],
                    response={'mc': 'select one', 'tf': 'select true or false', 'sa': 'write',
                              'plot': 'draw on the figure'}[r['type']],
                    prompt=r['question'], prompt_markup=qd['stem'],
                    choices=r['choices'], answer_lines=r['answer_lines'],
                    correct_letter=r['correct_letter'], correct_answer=r['correct_answer'],
                    grading_note=r['grading_note'], figure=None, page=r['page'])
                if qd.get('fig'):
                    base = os.path.join(out_dir, 'assets', qid)
                    write_figure(qd['fig'], base)
                    nfig += 1
                    rec['figure'] = dict(svg='assets/%s.svg' % qid, png='assets/%s.png' % qid,
                                         kind=qd['fig']['k'], description=describe(qd['fig']),
                                         blank_for_drawing=r['type'] == 'plot', data=jsonable(qd['fig']))
                if qd.get('cfigs'):
                    for j, g in enumerate(qd['cfigs']):
                        letter = A.LETTERS[j]
                        write_figure(g, os.path.join(out_dir, 'assets', '%s-%s' % (qid, letter)))
                        nfig += 1
                        rec['choices'][j] = dict(letter=letter, text=describe(g),
                                                 svg='assets/%s-%s.svg' % (qid, letter),
                                                 png='assets/%s-%s.png' % (qid, letter), data=jsonable(g))
                qrecs.append(rec)
            sections.append(dict(section=key, section_code=code, relation=RELATION.get(code, 'backward'),
                                 skill=name, standard=std, nearest_related=bool(nearest), questions=qrecs))
        set_doc = dict(format_version=FORMAT_VERSION, grade=build.GRADE, set=st['num'], set_id=sid,
                       standard=st['std'], title=st['title'], domain=st['domain'], sections=sections)
        with open(os.path.join(out_dir, fname), 'w', encoding='utf-8') as fh:
            json.dump(set_doc, fh, ensure_ascii=False, indent=1)
        index_sets.append(dict(
            set=st['num'], set_id=sid, file=fname, standard=st['std'], title=st['title'], domain=st['domain'],
            sections=[dict(section=s['section'], section_code=s['section_code'], relation=s['relation'],
                           skill=s['skill'], standard=s['standard'], nearest_related=s['nearest_related'],
                           question_ids=[q['id'] for q in s['questions']]) for s in sections]))

    index = dict(
        format_version=FORMAT_VERSION, grade=build.GRADE,
        title='Grade %d Common Core Math — Question Sets' % build.GRADE,
        set_count=len(index_sets), question_count=nq, figure_count=nfig,
        id_format='S<set>-<section>-Q<number>. Section codes: M = MAIN (Grade %d), B1, B2, ... = BACKWARD '
                  'branches (earlier grades), F1 = FORWARD 1 (Grade %d), F2 = FORWARD 2 (Grade %d).'
                  % (build.GRADE, build.GRADE + 1, build.GRADE + 2),
        relations=dict(main='the Grade %d skill the set is built around' % build.GRADE,
                       backward='a prerequisite skill to check when a student misses MAIN questions',
                       forward1='the directly connected Grade %d skill' % (build.GRADE + 1),
                       forward2='the next connected Grade %d skill; nearest_related = true marks a branch '
                                'with no direct Grade %d continuation' % (build.GRADE + 2, build.GRADE + 2)),
        grading_rules=build.GRADING_RULES,
        markup='prompt is plain text. prompt_markup uses {a/b} for a stacked fraction and 2{1/2} for a mixed number.',
        sets=index_sets)
    with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf-8') as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)

    # PDFs in parts
    for kind, src in (('questions', paths['questions']), ('answers', paths['key'])):
        doc = pymupdf.open(src)
        parts = (len(doc) + PDF_PART - 1) // PDF_PART
        for p in range(parts):
            part = pymupdf.open()
            part.insert_pdf(doc, from_page=p * PDF_PART, to_page=min(len(doc), (p + 1) * PDF_PART) - 1)
            part.save(os.path.join(out_dir, 'pdf', 'Grade %d - Part %d of %s.pdf' % (build.GRADE, p + 1, kind)),
                      garbage=3, deflate=True)
    write_readme(out_dir, index, npages)
    return index


def write_readme(out_dir, index, npages):
    g = index['grade']
    first = index['sets'][0]
    ex = first['sections'][0]['question_ids'][0]
    text = '''# Grade {g} — Untangle The Nexus import package

{sets} question sets, {nq} questions, {nfig} figure files. Generated by `question-bank/engine/export.py`
in the math-lab-app repository; regenerate there rather than editing these files by hand.

## Files

| Path | Contents |
|---|---|
| `index.json` | Every set: its file, Common Core standard, and each section's relation and question IDs. Also the ID format and grading rules. |
| `sets/S01.json` … | One file per question set. Each question is a complete record (see below). |
| `assets/<ID>.svg` / `.png` | The figure for that question (SVG preferred, PNG fallback). Picture choices are `<ID>-A.svg`, `<ID>-B.svg`. |
| `pdf/` | The printable question collection and answer key in {part}-page parts. Page numbers match the `page` field. Not needed for import. |

## Importing

1. Read `index.json`. For each entry in `sets`, load its `file`.
2. Each set file has `sections` in order: MAIN, BACKWARD 1…n, FORWARD 1, FORWARD 2. `relation` is
   `main`, `backward`, `forward1` or `forward2`. A section's questions all test the same skill and standard.
3. Store each question by its `id` (for example `{ex}`). IDs never change between rebuilds unless questions are
   added or removed.
4. Copy `assets/` as is and resolve `figure.svg` / `figure.png` (and picture choices' `svg` / `png`) relative to this folder.

## Question record

| Field | Meaning |
|---|---|
| `id`, `set`, `section`, `section_code`, `relation`, `number` | Where the question sits |
| `standard`, `standard_grade`, `domain`, `skill`, `nearest_related` | What it tests |
| `type`, `response` | `mc` (select one), `tf` (true or false), `sa` (write an answer), `plot` (draw on the figure) |
| `prompt`, `prompt_markup` | Question text: plain, and with `{{a/b}}` fraction markup |
| `choices` | `[{{letter, text}}]` in the order students see; true/false is A. True, B. False. Picture choices add `svg`, `png`, `data` |
| `answer_lines` | Labels of the student's answer blanks, for written answers |
| `correct_letter`, `correct_answer` | The answer. For drawing questions `correct_answer` describes a correct drawing |
| `grading_note` | Accepted alternatives and what an explanation must include |
| `figure` | `svg`, `png`, `kind`, `description` (plain text), `blank_for_drawing`, and `data` (the values the figure is drawn from) |
| `page` | Page in the PDFs |

## Grading

`grading_rules` in `index.json` applies to every question. Multiple choice and true/false compare letters.
Written answers accept any mathematically equivalent form unless the question asks for a specific form. A drawing is
judged against `correct_answer`. Explanations must include what `grading_note` lists.
'''.format(g=g, sets=index['set_count'], nq=index['question_count'], nfig=index['figure_count'],
           part=PDF_PART, ex=ex)
    with open(os.path.join(out_dir, 'README.md'), 'w', encoding='utf-8') as fh:
        fh.write(text)


if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'grade6'
    build.load_grade(name)
    out = os.path.join(os.path.dirname(ENGINE), 'nexus', name)
    idx = export(out)
    print('%s: %d sets, %d questions, %d figure files -> %s' % (
        name, idx['set_count'], idx['question_count'], idx['figure_count'], out))
