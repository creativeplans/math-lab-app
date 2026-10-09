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
import revisions  # noqa: E402


def r_for_snap(r):
    """Key record fields in the form the history snapshot stores them."""
    return dict(type=r['type'], correct_letter=r['correct_letter'], correct_answer=r['correct_answer'],
                grading_note=r['grading_note'], drawing_answer=r['drawing_answer'], required_method=r['required_method'])

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
    if k == 'clock':
        if not f.get('hands', True):
            return 'Analog clock face with the numbers 1 to 12 and minute marks, with no hands; the student draws the hands.'
        return 'Analog clock with an hour hand and a minute hand showing %d:%02d.' % (f['hour'], f['minute'])
    if k == 'picgraph':
        if not any(n for _, n in f['rows']):
            return 'Blank picture graph "%s" with rows for %s and the key ● = %s; the student draws the symbols.' % (
                f['title'], ', '.join(r[0] for r in f['rows']), f['key'])
        return 'Picture graph "%s". Key: each ● = %s. %s.' % (
            f['title'], f['key'], '; '.join('%s: %d symbols' % (r[0], r[1]) for r in f['rows']))
    if k == 'ruler':
        d = 'Inch ruler from 0 to %d inches with marks every 1/%d inch' % (f['max'], f.get('div', 4))
        if f.get('obj'):
            d += '. %s lies above the ruler from %s to %s inches' % (
                f.get('name') or 'An object', num(f['obj'][0]), num(f['obj'][1]))
        return d + '.'
    if k == 'beaker':
        u = f.get('unit', 'L')
        return 'Measuring container marked from 0 to %s %s, with marks every %s %s, filled to %s %s.' % (
            num(f['max']), u, num(f['step']), u, num(f.get('fill', 0)), u)
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
            if p.get('hidden'):
                continue
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
        n = len([p for p in f['polys'] if not p.get('hidden')])
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
        rules = f.get('rules') or ([f['rule']] if f.get('rule') else [])
        return 'Vertical arithmetic, digits right-aligned: ' + ' / '.join(f['lines']) + (
            ' (a line is drawn under row %s)' % ' and row '.join(str(r) for r in rules) if rules else '') + '.'
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
    if k == 'grid' and (f.get('cshade') is not None or f.get('rshade') is not None):
        R_, C_ = f.get('rows', 10), f.get('cols', 10)
        return ('Rectangle divided into %d rows and %d columns of equal parts. The first %d columns are shaded and the '
                'first %d rows are shaded; %d parts where they overlap are shaded darker.' % (
                    R_, C_, f.get('cshade') or 0, f.get('rshade') or 0, (f.get('cshade') or 0) * (f.get('rshade') or 0)))
    if k == 'grid':
        return 'Grid of %d by %d squares with %d squares shaded.' % (f.get('rows', 10), f.get('cols', 10), f['shade'])
    if k == 'text':
        return A.plain(f.get('text', ''))
    if k == 'array':
        d = 'Array of dots: %d rows of %d' % (f['rows'], f['cols'])
        if f.get('split'):
            d += ', with a dashed line after the first %d columns' % f['split']
        return d + '.'
    if k == 'protractor':
        d = 'Protractor marked from 0 at the right to 180 at the left'
        if f.get('inner'):
            d += ', with a second (inner) scale from 0 at the left to 180 at the right'
        if f.get('rays'):
            d += '. Rays from its center at %s degrees' % ' and '.join(str(r) for r in f['rays'])
        else:
            d += '. No rays are drawn; the student draws them'
        return d + '.'
    if k == 'geo':
        parts = []
        for it in f['items']:
            if it[0] == 'point':
                parts.append('point %s at %s' % (it[2] or '', pt(it[1])))
            elif it[0] in ('segment', 'ray', 'line'):
                parts.append('%s from %s %s %s' % (it[0], pt(it[1]), 'toward' if it[0] != 'segment' else 'to', pt(it[2])))
            elif it[0] == 'ra':
                parts.append('right-angle mark at %s' % pt(it[1]))
            elif it[0] == 'text':
                parts.append('text "%s" at %s' % (A.plain(it[2]), pt(it[1])))
        return 'Geometry drawing: ' + '; '.join(parts) + '.'
    if k == 'rays':
        d = 'Rays drawn from one point, in the directions %s degrees (0 = right, measured counterclockwise)' % ', '.join(
            str(r) for r in f['rays'])
        if f.get('labels'):
            d += '. Angle labels: ' + '; '.join('"%s" in the angle around %s degrees' % (A.plain(l[1]), l[0]) for l in f['labels'])
        if f.get('ra'):
            d += '. A right-angle mark is shown'
        return d + '.'
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
    tracker = revisions.Tracker(build.GRADE_DIR, build.COLLECTION)

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
                    id=qid, uid=r['uid'], collection=build.COLLECTION['id'], set=st['num'], section=key, section_code=code,
                    relation=RELATION.get(code, 'backward'), number=i, of=len(qs),
                    standard=std, standard_grade=int(std.split('.')[0]) if std[0].isdigit() else std.split('.')[0],
                    domain=r['domain'], skill=name, nearest_related=bool(nearest),
                    type=r['type'],
                    response={'mc': 'select one', 'tf': 'select true or false', 'sa': 'write',
                              'plot': 'draw on the figure',
                              'plot_text': 'draw on the figure and write an answer',
                              'work': 'write the answer and show the required work'}[r['type']],
                    prompt=r['question'], prompt_markup=qd['stem'],
                    choices=r['choices'], answer_lines=r['answer_lines'],
                    correct_letter=r['correct_letter'], correct_answer=r['correct_answer'],
                    drawing_answer=r['drawing_answer'], required_method=r['required_method'],
                    grading_note=r['grading_note'], figure=None, page=r['page'],
                    revision=None)
                if qd.get('fig'):
                    base = os.path.join(out_dir, 'assets', qid)
                    write_figure(qd['fig'], base)
                    nfig += 1
                    rec['figure'] = dict(svg='assets/%s.svg' % qid, png='assets/%s.png' % qid,
                                         kind=qd['fig']['k'], description=describe(qd['fig']),
                                         blank_for_drawing=r['type'] in ('plot', 'plot_text'), data=jsonable(qd['fig']))
                if qd.get('cfigs'):
                    for j, g in enumerate(qd['cfigs']):
                        letter = A.LETTERS[j]
                        write_figure(g, os.path.join(out_dir, 'assets', '%s-%s' % (qid, letter)))
                        nfig += 1
                        rec['choices'][j] = dict(letter=letter, text=describe(g),
                                                 svg='assets/%s-%s.svg' % (qid, letter),
                                                 png='assets/%s-%s.png' % (qid, letter), data=jsonable(g))
                snap = dict(r_for_snap(r), choices=rec['choices'])
                rev = tracker.check(qid, revisions.snapshot(dict(qd, fig=jsonable(qd['fig']) if qd.get('fig') else None),
                                                            snap, std, name, nearest))
                rec['revision'] = rev['status']
                qrecs.append(rec)
            sections.append(dict(section=key, section_code=code, relation=RELATION.get(code, 'backward'),
                                 skill=name, standard=std, nearest_related=bool(nearest), questions=qrecs))
        set_doc = dict(format_version=FORMAT_VERSION, collection=build.COLLECTION, grade=build.GRADE, set=st['num'], set_id=sid,
                       standard=st['std'], title=st['title'], domain=st['domain'], sections=sections)
        with open(os.path.join(out_dir, fname), 'w', encoding='utf-8') as fh:
            json.dump(set_doc, fh, ensure_ascii=False, indent=1)
        index_sets.append(dict(
            set=st['num'], set_id=sid, file=fname, standard=st['std'], title=st['title'], domain=st['domain'],
            sections=[dict(section=s['section'], section_code=s['section_code'], relation=s['relation'],
                           skill=s['skill'], standard=s['standard'], nearest_related=s['nearest_related'],
                           question_ids=[q['id'] for q in s['questions']]) for s in sections]))

    index = dict(
        format_version=FORMAT_VERSION, collection=build.COLLECTION, grade=build.GRADE,
        title='Grade %d Common Core Math — Question Sets' % build.GRADE,
        set_count=len(index_sets), question_count=nq, figure_count=nfig,
        id_format='S<set>-<section>-Q<number>. Section codes: M = MAIN (Grade %d), B1, B2, ... = BACKWARD '
                  'branches (earlier grades), F1 = FORWARD 1 (Grade %d), F2 = FORWARD 2 (Grade %d). '
                  'id is unique within this collection; uid = "%s:" + id is unique across all grade collections '
                  '(the collection, not a question\'s standard grade, is the namespace: this bank also holds '
                  'Grade %d and %d forward questions). Set and branch numbers are fixed: they need not be '
                  'consecutive, and an ID is never reused for a different skill (see revisions.json).'
                  % (build.GRADE, build.GRADE + 1, build.GRADE + 2, build.COLLECTION['id'],
                     build.GRADE + 1, build.GRADE + 2),
        revisions_file='revisions.json' if tracker.active else None,
        relations=dict(main='the Grade %d skill the set is built around' % build.GRADE,
                       backward='a prerequisite skill to check when a student misses MAIN questions',
                       forward1='the directly connected Grade %d skill' % (build.GRADE + 1),
                       forward2='the next connected Grade %d skill' % (build.GRADE + 2),
                       nearest_related='true marks a forward branch whose grade has no direct continuation of '
                                       'the skill; it uses the nearest related standard of that grade'),
        grading_rules=build.GRADING_RULES,
        markup='prompt is plain text. prompt_markup uses {a/b} for a stacked fraction and 2{1/2} for a mixed number.',
        sets=index_sets)
    with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf-8') as fh:
        json.dump(index, fh, ensure_ascii=False, indent=1)
    rev_doc = tracker.document()
    if rev_doc:
        index['revision_summary'] = rev_doc['summary']
        with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf-8') as fh:
            json.dump(index, fh, ensure_ascii=False, indent=1)
        with open(os.path.join(out_dir, 'revisions.json'), 'w', encoding='utf-8') as fh:
            json.dump(rev_doc, fh, ensure_ascii=False, indent=1)
        title = 'Grade %d question collection' % build.GRADE
        revisions.write_changelog(rev_doc, os.path.join(out_dir, 'CHANGELOG.md'), title)
        revisions.write_changelog(rev_doc, os.path.join(build.GRADE_DIR, 'CHANGELOG.md'), title)

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
    write_manifest(out_dir)
    return index


def write_manifest(out_dir):
    import hashlib
    files = []
    for root, _, names in os.walk(out_dir):
        for n in sorted(names):
            p = os.path.join(root, n)
            rel = os.path.relpath(p, out_dir).replace(os.sep, '/')
            if rel == 'MANIFEST.json':
                continue
            data = open(p, 'rb').read()
            files.append(dict(path=rel, bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
    files.sort(key=lambda f: f['path'])
    with open(os.path.join(out_dir, 'MANIFEST.json'), 'w', encoding='utf-8') as fh:
        json.dump(dict(collection=build.COLLECTION, file_count=len(files), files=files), fh, indent=1)


def write_readme(out_dir, index, npages):
    g = index['grade']
    first = index['sets'][0]
    ex = first['sections'][0]['question_ids'][0]
    col = index['collection']
    rev = index.get('revision_summary')
    revline = ''
    if rev:
        revline = ('\nThis is version {v}. Compared with the previous version: {u} questions unchanged, {r} revised, {n} new, '
                   '{t} retired. `CHANGELOG.md` lists every change by question ID; `revisions.json` has the full map.\n').format(
            v=col['version'], u=rev.get('unchanged', 0), r=rev.get('revised', 0), n=rev.get('new', 0), t=rev.get('retired', 0))
    text = '''# Grade {g} — Untangle The Nexus import package

Collection `{cid}`, version {ver}. {sets} question sets, {nq} questions, {nfig} figure files. Generated by
`question-bank/engine/export.py` in the math-lab-app repository; regenerate there rather than editing these files by hand.
{revline}
## Files

| Path | Contents |
|---|---|
| `index.json` | The collection (`id`, `version`), every set with its file, standard, and each section's relation and question IDs, the ID format and the grading rules. |
| `sets/Sxx.json` | One file per question set. Each question is a complete record (see below). |
| `assets/<ID>.svg` / `.png` | The figure for that question (SVG preferred, PNG fallback). Picture choices are `<ID>-A.svg`, `<ID>-B.svg`. |
| `revisions.json`, `CHANGELOG.md` | Changes since the previous version, keyed by question ID (only after a revision). |
| `MANIFEST.json` | Every file in the package with its size and SHA-256, for checking that nothing was lost. |
| `pdf/` | The printable question collection and answer key in {part}-page parts. Page numbers match the `page` field. Not needed for import. |

## Importing

1. Read `index.json`. For each entry in `sets`, load its `file`. Set numbers are fixed and need not be consecutive
   (sets added in a revision take the next free number, and appear next to their related sets).
2. Each set file has `sections` in order: MAIN, BACKWARD branches, FORWARD 1, FORWARD 2. `relation` is
   `main`, `backward`, `forward1` or `forward2`. A section's questions all test the same skill and standard.
   Backward branch numbers are also fixed (B1, B3, B4 is possible when a branch was retired).
3. Store each question by `uid` (for example `{cid}:{ex}`), which is unique across all grade collections. `id`
   is unique only within this collection. An ID is never reused for a different skill: when content moves or is
   retired, `revisions.json` says where it went.
4. Copy `assets/` as is and resolve `figure.svg` / `figure.png` (and picture choices' `svg` / `png`) relative to this folder.
5. Optional: check every file against `MANIFEST.json`.

## Question record

| Field | Meaning |
|---|---|
| `uid`, `collection`, `id` | Identity: `uid` = collection + `:` + `id` |
| `set`, `section`, `section_code`, `relation`, `number` | Where the question sits |
| `standard`, `standard_grade`, `domain`, `skill`, `nearest_related` | What it tests |
| `type`, `response` | `mc` (select one), `tf` (true or false), `sa` (write an answer), `plot` (draw on the figure), `plot_text` (draw on the figure AND write an answer), `work` (write the answer and show the required work) |
| `prompt`, `prompt_markup` | Question text: plain, and with `{{a/b}}` fraction markup |
| `choices` | `[{{letter, text}}]` in the order students see; true/false is A. True, B. False. Picture choices add `svg`, `png`, `data` |
| `answer_lines` | Labels of the student's answer blanks, for written answers |
| `correct_letter`, `correct_answer` | The answer. For `plot`, `correct_answer` describes a correct drawing; for `plot_text` it is the written answer |
| `drawing_answer` | `plot_text` only: what a correct drawing shows |
| `required_method` | `work` only: what the shown work must use; the final answer alone is partial credit |
| `grading_note` | Accepted alternatives and what an explanation must include |
| `figure` | `svg`, `png`, `kind`, `description` (plain text), `blank_for_drawing`, and `data` (the values the figure is drawn from) |
| `revision` | `unchanged`, `revised` or `new` compared with the previous version |
| `page` | Page in the PDFs |

## Grading

`grading_rules` in `index.json` applies to every question. Multiple choice and true/false compare letters.
Written answers accept any mathematically equivalent form unless the question asks for a specific form. A `plot`
drawing is judged against `correct_answer`; a `plot_text` response needs both the drawing (`drawing_answer`) and the
written answer (`correct_answer`). A `work` response needs the method in `required_method`. Explanations must include
what `grading_note` lists.
'''.format(g=g, sets=index['set_count'], nq=index['question_count'], nfig=index['figure_count'],
           part=PDF_PART, ex=ex, cid=col['id'], ver=col['version'], revline=revline)
    with open(os.path.join(out_dir, 'README.md'), 'w', encoding='utf-8') as fh:
        fh.write(text)


if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'grade6'
    build.load_grade(name)
    out = os.path.join(os.path.dirname(ENGINE), 'nexus', name)
    idx = export(out)
    print('%s: %d sets, %d questions, %d figure files -> %s' % (
        name, idx['set_count'], idx['question_count'], idx['figure_count'], out))
