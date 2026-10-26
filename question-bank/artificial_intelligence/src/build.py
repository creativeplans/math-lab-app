"""Build the Artificial Intelligence collection from its single source (plan.py, sources.py, data_*.py).

    python3 question-bank/artificial_intelligence/src/build.py [--nopdf] [--consp]

Writes
  question-bank/nexus/artificial_intelligence/        the Untangle The Nexus import package (index.json, sets/Sxxx.json)
  question-bank/artificial_intelligence/AI_Answer_Key.json / .csv
  question-bank/artificial_intelligence/AI_Question_Collection.pdf, AI_Answer_Key.pdf
  question-bank/artificial_intelligence/src/choice_plan.json   frozen answer-letter plan (later corrections keep letters)
"""
import csv
import glob
import hashlib
import html
import importlib
import json
import re
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402
import sources  # noqa: E402

ROOT = os.path.dirname(HERE)                       # question-bank/artificial_intelligence
QB = os.path.dirname(ROOT)                         # question-bank
PKG = os.path.join(QB, 'nexus', 'artificial_intelligence')
VERSION = '1.0.1'
DATE = '2026-10-26'
TITLE = 'Artificial Intelligence: Understanding and Using AI Wisely'
NAME = 'Artificial Intelligence'
FILE = 'AI'
SCOPE_NOTE = ('Course scope: general education for adults and high-school students, not legal, medical or financial '
              'advice. No AI tool, account, download or paid service is needed: every example is prepared in advance '
              'and shown as text, and nothing runs. Examples labeled "fictional" were written for this course and are '
              'not real outputs of any named product. Laws, products and prices change; dated lessons say what to '
              'check. People and organizations in scenarios are fictional unless a lesson names a real case.')
PLAN_FILE = os.path.join(HERE, 'choice_plan.json')
SECTION_NAME = {'M': 'MAIN', 'F1': 'FORWARD 1: APPLY IT', 'F2': 'FORWARD 2: HANDLE THE COMPLICATIONS'}


def load_sets():
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py'))):
        mod = importlib.import_module(os.path.basename(f)[:-3])
        for s in mod.SETS:
            n = plan.SET_NUM[s['code']]
            assert n not in out, 'set written twice: %s' % s['code']
            out[n] = s
    return dict(sorted(out.items()))


def sections(s):
    yield 'M', 'main', s['M']
    for i, b in enumerate(s['B'], 1):
        yield 'B%d' % i, 'backward', b
    yield 'F1', 'forward1', s['F1']
    yield 'F2', 'forward2', s['F2']


# ------------------------------------------------------------------ answer letters
def assign_letters(all_sets):
    try:
        frozen = json.load(open(PLAN_FILE, encoding='utf-8'))
    except FileNotFoundError:
        frozen = {}
    counts = {L: 0 for L in 'ABCD'}
    out, pending = {}, []
    for n, s in all_sets.items():
        for code, rel, sec in sections(s):
            for i, q in enumerate(sec['qs'], 1):
                qid = 'S%d-%s-Q%d' % (n, code, i)
                texts = [q['correct']] + [w[0] for w in q['wrong']]
                if qid in frozen and sorted(frozen[qid]) == sorted(texts):
                    out[qid] = frozen[qid]
                    counts['ABCD'[out[qid].index(q['correct'])]] += 1
                elif qid in frozen and q['correct'] in frozen[qid]:
                    # a corrected question keeps its correct answer on the same letter
                    k = frozen[qid].index(q['correct'])
                    others = [t for t in frozen[qid] if t in texts[1:] and t != q['correct']]
                    others += [t for t in texts[1:] if t not in others]
                    out[qid] = others[:k] + [q['correct']] + others[k:]
                    counts['ABCD'[k]] += 1
                else:
                    pending.append((qid, q, texts))
    last = {}
    for qid, q, texts in pending:
        sec_id = qid.rsplit('-', 1)[0]
        h = int(hashlib.sha1(qid.encode()).hexdigest(), 16)
        cand = sorted('ABCD', key=lambda L: (counts[L], (h >> ((ord(L) - 65) * 4)) & 15))
        prev = last.get(sec_id, [])
        pick = next((L for L in cand if not (len(prev) >= 1 and prev[-1] == L) and counts[L] <= counts[cand[0]] + 3),
                    cand[0])
        last.setdefault(sec_id, []).append(pick)
        counts[pick] += 1
        others = sorted(texts[1:], key=lambda t: hashlib.sha1((qid + t).encode()).hexdigest())
        k = 'ABCD'.index(pick)
        out[qid] = others[:k] + [texts[0]] + others[k:]
    json.dump(out, open(PLAN_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    return out


# ------------------------------------------------------------------ records
def set_sources(p):
    if not p['sources']:
        return {}
    es = [sources.entry(k) for k in p['sources']]
    d = {'sources': [{'url': e['url'], 'claim': e['claim'], 'checked': e['checked']} for e in es],
         'review_interval_days': min(e['review_days'] for e in es),
         'jurisdiction': '; '.join(sorted({e['jurisdiction'] for e in es}))}
    years = sorted({e['effective_year'] for e in es if e.get('effective_year')})
    if years:
        d['effective_year'] = '; '.join(years)
    return d


def build_records(all_sets, letters):
    recs, sets_pkg = [], []
    mod_title = {m[0]: m[1] for m in plan.MODULES}
    for n, s in all_sets.items():
        p = plan.SETS[n]
        secs_pkg = []
        for code, rel, sec in sections(s):
            qs_pkg = []
            for i, q in enumerate(sec['qs'], 1):
                qid = 'S%d-%s-Q%d' % (n, code, i)
                order = letters[qid]
                choices = [{'letter': 'ABCD'[k], 'text': t} for k, t in enumerate(order)]
                L = 'ABCD'[order.index(q['correct'])]
                intro = q['intro'] or sec['intro']
                rec_q = {'id': qid, 'number': i, 'standard': '', 'domain': mod_title[p['module']], 'type': 'mc',
                         'prompt': q['prompt'], 'choices': choices, 'correct_letter': L,
                         'correct_answer': q['correct'], 'intro': intro, 'feedback': q['feedback']}
                if q['ex']:
                    rec_q['example'] = {k: v for k, v in q['ex'].items() if k != 'checked'}
                qs_pkg.append(rec_q)
                why = {w[0]: w[1] for w in q['wrong']}
                recs.append(dict(
                    uid='AI:' + qid, id=qid, set=n, set_title=p['title'], set_code=p['code'], module=p['module'],
                    module_title=mod_title[p['module']], paths=p['paths'] or [x['id'] for x in plan.PATHS],
                    section=code, relation=rel, branch_mode=sec['mode'] or '', section_skill=sec['skill'], number=i,
                    outcome=p['code'], outcome_title=p['outcome_title'], intro=intro, prompt=q['prompt'],
                    choices=choices, correct_letter=L, correct_answer=q['correct'], feedback=q['feedback'],
                    wrong_choices=[{'letter': c['letter'], 'text': c['text'], 'why_wrong': why[c['text']]}
                                   for c in choices if c['text'] != q['correct']],
                    arithmetic_checked=q['calc'], example=q['ex'] and {k: v for k, v in q['ex'].items() if k != 'checked'},
                    code_checked=bool(q['ex'] and q['ex'].get('checked')), content_status=p['status'],
                    sources='; '.join(p['sources']), question_page=0))
            sp = {'section': code, 'section_code': code, 'relation': rel, 'skill': sec['skill'], 'questions': qs_pkg}
            if rel == 'backward':
                sp['branch_mode'] = sec['mode']
                sp['relationship'] = sec['why']
            if rel == 'forward1':
                sp['difficulty'] = 'harder'
                sp['title'] = 'Apply it'
            if rel == 'forward2':
                sp['difficulty'] = 'expert'
                sp['title'] = 'Handle the complications'
            secs_pkg.append(sp)
        sp = {'set': n, 'title': p['title'], 'outcome': p['code'], 'content_status': p['status'],
              'requires': p['requires'], 'module': p['module'],
              'path_refs': p['paths'] or [x['id'] for x in plan.PATHS],
              'suggested': [plan.SET_NUM[c] for c in plan.SUGGESTED.get(p['code'], [])],
              **set_sources(p), 'sections': secs_pkg}
        sets_pkg.append(sp)
    return recs, sets_pkg


def write_package(sets_pkg):
    if os.path.exists(PKG):
        shutil.rmtree(PKG)
    os.makedirs(os.path.join(PKG, 'sets'))
    built = {s['set'] for s in sets_pkg}
    outcomes = {plan.SETS[n]['code']: {'title': plan.SETS[n]['outcome_title'], 'alignment': 'local'} for n in built}
    modules = []
    for mid, title, kind, paths, desc in plan.MODULES:
        ms = [n for n in sorted(built) if plan.SETS[n]['module'] == mid]
        m = {'id': mid, 'title': title, 'kind': kind, 'description': desc, 'sets': ms}
        if paths:
            m['paths'] = paths
        if kind == 'specialty':
            m['optional'] = True
        modules.append(m)
    index = {'format_version': 1, 'course': 'artificial_intelligence', 'bank_version': VERSION, 'title': TITLE,
             'category': 'Adults & HS Students', 'scope_note': SCOPE_NOTE,
             'collection': {'id': 'AI', 'version': VERSION, 'date': DATE},
             'outcomes': dict(sorted(outcomes.items())), 'paths': plan.PATHS, 'modules': modules,
             'sets': [{'set': s['set'], 'file': 'sets/S%03d.json' % s['set'], 'title': s['title'], 'outcome': s['outcome'],
                       'module': s['module']} for s in sets_pkg]}
    json.dump(index, open(os.path.join(PKG, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for s in sets_pkg:
        json.dump(s, open(os.path.join(PKG, 'sets', 'S%03d.json' % s['set']), 'w', encoding='utf-8'), ensure_ascii=False,
                  indent=1)


# ------------------------------------------------------------------ PDFs
CSS = ('body{font-family:sans-serif;font-size:14px;color:#111;line-height:1.35}'
       'h1{font-size:21px;margin:0 0 8px 0}h2{font-size:16px;margin:6px 0}'
       '.ch{margin:3px 0 3px 14px}.small{font-size:11.5px;color:#333}.teach{background:#f2f2f2;border:1px solid #bbb;'
       'padding:6px 8px;margin-bottom:8px}.ex{border:1px solid #6a7f99;padding:5px 8px;margin-bottom:8px;background:#fafcff}'
       '.pre{background:#fff;border:1px dashed #999;padding:4px 6px;margin:2px 0 4px 0}'
       '.code{font-family:monospace;font-size:12.5px;background:#f6f6f6;border:1px solid #999;padding:4px 6px}'
       '.tb{border-collapse:collapse;margin:2px 0}.tb th,.tb td{border:1px solid #888;padding:2px 6px;font-size:12.5px}')


def esc(s):
    return html.escape(str(s)).replace('\n', '<br>')


def ex_html(ex):
    """A prepared example as inert HTML (monospace for code; a bordered table; labeled request and response)."""
    if not ex:
        return ''
    head = '<p class="small"><b>%s</b></p>' % esc(ex['label'])
    if ex['kind'] == 'prompt_response':
        body = ('<p class="small"><b>Request:</b></p><div class="pre">%s</div><p class="small"><b>Response:</b></p>'
                '<div class="pre">%s</div>' % (esc(ex['prompt']), esc(ex['response'])))
    elif ex['kind'] == 'code':
        body = '<div class="code">%s</div>' % esc(ex['code']).replace(' ', '&nbsp;')
    elif ex['kind'] == 'table':
        rows = ex['table']
        body = ('<table class="tb"><tr>%s</tr>%s</table>'
                % (''.join('<th>%s</th>' % esc(c) for c in rows[0]),
                   ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % esc(c) for c in r) for r in rows[1:])))
    else:
        body = '<div class="pre">%s</div>' % esc(ex['text'])
    return '<div class="ex">%s%s</div>' % (head, body)


def ref_box(r):
    sec = SECTION_NAME.get(r['section'], 'BACKWARD %s' % r['section'][1:])
    mode = ' (%s)' % r['branch_mode'].replace('_', ' ') if r['branch_mode'] else ''
    return ('<div style="border:1px solid #888;padding:5px;background:#eef3f8"><span class="small"><b>REFERENCE LABEL: '
            'NOT PART OF THE QUESTION</b> &nbsp; <b>ID %s</b><br>Artificial Intelligence, Set %d: %s · %s%s · Q%d/5 · Outcome '
            '%s (local)</span></div>' % (r['id'], r['set'], esc(r['set_title']), sec, mode, r['number'], r['outcome']))


def make_question_pdf(recs, path):
    import pymupdf
    doc = pymupdf.open()
    W, H = 612, 792
    page_of = {}
    cur = None
    for r in recs:
        if r['set'] != cur:
            cur = r['set']
            p = plan.SETS[cur]
            pg = doc.new_page(width=W, height=H)
            pg.insert_htmlbox(pymupdf.Rect(50, 60, W - 50, H - 60),
                              '<h1>Set %d: %s</h1><p>Outcome %s: %s</p><p class="small">Module: %s</p>'
                              '<p class="small">%s</p>' % (cur, esc(p['title']), p['code'], esc(p['outcome_title']),
                                                           esc(r['module_title']), esc(SCOPE_NOTE)), css=CSS)
        pg = doc.new_page(width=W, height=H)
        body = ('<div class="teach"><b>Learn</b><br>%s</div>%s<p>%s</p>' % (esc(r['intro']), ex_html(r['example']),
                                                                         esc(r['prompt'])) +
                ''.join('<p class="ch"><b>%s.</b> %s</p>' % (c['letter'], esc(c['text'])) for c in r['choices']))
        spare = pg.insert_htmlbox(pymupdf.Rect(45, 40, W - 45, H - 110), body, css=CSS, scale_low=0.5)
        spare = spare[0] if isinstance(spare, tuple) else spare
        assert spare >= 0, 'question %s does not fit on its page' % r['id']
        pg.insert_htmlbox(pymupdf.Rect(45, H - 100, W - 45, H - 30), ref_box(r), css=CSS)
        pg.insert_text((W - 60, H - 14), str(len(doc)), fontsize=9)
        page_of[r['id']] = len(doc)
    doc.save(path, garbage=3, deflate=True)
    check_pdf_text(path, recs, 'question')
    return page_of


def make_key_pdf(recs, path):
    import pymupdf
    parts = ['<h1>Artificial Intelligence answer key (version %s)</h1><p class="small">Private grading material. Each entry: '
             'question ID, its page in the question collection, the correct choice, why it is right, why each other '
             'choice is wrong, whether arithmetic and code examples were checked by code, and the sources for the set.'
             '</p>' % VERSION]
    for r in recs:
        wr = ''.join('<p class="ch">✗ %s. %s: %s</p>' % (w['letter'], esc(w['text']), esc(w['why_wrong']))
                     for w in r['wrong_choices'])
        parts.append('<div style="border-top:1px solid #999;margin-top:6px;padding-top:4px"><h2>%s · question page %d</h2>'
                     '<p class="small">%s · %s</p><p class="small">%s</p>%s<p><b>Answer: %s.</b> %s</p><p>%s</p>%s'
                     '<p class="small">Arithmetic checked by code: %s. Code example run and its output checked: %s. '
                     'Sources: %s</p></div>'
                     % (r['id'], r['question_page'], r['outcome'], esc(r['section_skill']), esc(r['prompt']),
                        ex_html(r['example']), r['correct_letter'], esc(r['correct_answer']), esc(r['feedback']), wr,
                        'yes' if r['arithmetic_checked'] else 'not applicable',
                        'yes' if r['code_checked'] else 'not applicable', esc(r['sources'] or 'none (stable)')))
    # Each entry is laid out on its own: it is measured first, and an entry that does not fit in the space left starts
    # a new page. (Placing the whole key as one flow let an example box at a page break drop text silently.)
    TOP, BOTTOM, LEFT, RIGHT = 45, 747, 45, 567
    writer = pymupdf.DocumentWriter(path)
    dev = writer.begin_page(pymupdf.Rect(0, 0, 612, 792))
    y = TOP

    def height(html):
        st = pymupdf.Story('<html><body>%s</body></html>' % html, user_css=CSS)
        more, filled = st.place(pymupdf.Rect(LEFT, 0, RIGHT, 100000))
        return pymupdf.Rect(filled).y1

    for html in parts:
        h = height(html)
        if y > TOP and y + h > BOTTOM:
            writer.end_page()
            dev = writer.begin_page(pymupdf.Rect(0, 0, 612, 792))
            y = TOP
        st = pymupdf.Story('<html><body>%s</body></html>' % html, user_css=CSS)
        while True:
            more, filled = st.place(pymupdf.Rect(LEFT, y, RIGHT, BOTTOM))
            st.draw(dev)
            if not more:
                y = pymupdf.Rect(filled).y1 + 4
                break
            writer.end_page()
            dev = writer.begin_page(pymupdf.Rect(0, 0, 612, 792))
            y = TOP
    writer.end_page()
    writer.close()
    check_pdf_text(path, recs, 'answer key')


def _norm(t):
    t = t.replace('\ufb01', 'fi').replace('\ufb02', 'fl').replace('\ufb00', 'ff').replace('\ufb03', 'ffi').replace('\ufb04', 'ffl')
    return re.sub(r'\s+', ' ', t)


def check_pdf_text(path, recs, label):
    """Every question ID, prompt and correct answer must appear in the PDF's text (guards against dropped layout)."""
    import pymupdf
    doc = pymupdf.open(path)
    text = _norm(' '.join(pg.get_text() for pg in doc))
    missing = [r['id'] for r in recs if r['id'] not in text or _norm(r['prompt'])[:60] not in text
               or _norm(r['correct_answer'])[:40] not in text]
    assert not missing, '%s PDF is missing text for %d questions, e.g. %s' % (label, len(missing), missing[:5])


def shrink_pdf(path):
    import pymupdf
    doc = pymupdf.open(path)
    doc.subset_fonts()
    tmp = path + '.tmp'
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)


# ------------------------------------------------------------------ answer key files
KEY_FIELDS = ['uid', 'id', 'set', 'set_title', 'set_code', 'module', 'module_title', 'paths', 'section', 'relation',
              'branch_mode', 'section_skill', 'number', 'outcome', 'outcome_title', 'question_page', 'intro', 'prompt',
              'example', 'choices', 'correct_letter', 'correct_answer', 'feedback', 'wrong_choices', 'arithmetic_checked',
              'code_checked', 'content_status', 'sources']


def write_key(recs):
    data = {'collection': {'id': 'AI', 'course': 'artificial_intelligence', 'title': TITLE, 'version': VERSION, 'date': DATE},
            'questions': [{k: r.get(k, '') for k in KEY_FIELDS} for r in recs]}
    json.dump(data, open(os.path.join(ROOT, FILE + '_Answer_Key.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    with open(os.path.join(ROOT, FILE + '_Answer_Key.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(KEY_FIELDS)
        for r in recs:
            row = []
            for k in KEY_FIELDS:
                v = r.get(k, '')
                if k == 'choices':
                    v = ' | '.join('%s. %s' % (c['letter'], c['text']) for c in v)
                elif k == 'wrong_choices':
                    v = ' | '.join('%s: %s' % (x['letter'], x['why_wrong']) for x in v)
                elif isinstance(v, (list, dict)):
                    v = json.dumps(v, ensure_ascii=False)
                row.append(v)
            w.writerow(row)


def conspicuous(correct, wrongs):
    """The correct choice gives itself away by length: more than 20 percent AND at least 7 characters longer than
    every wrong choice (a few characters' difference between short choices is not noticeable)."""
    longest = max(len(w) for w in wrongs)
    return len(correct) > 1.2 * longest and len(correct) - longest >= 7


def main(pdf=True):
    import eq
    all_sets = load_sets()
    for n, s in all_sets.items():
        for code, rel, sec in sections(s):
            for i, q in enumerate(sec['qs'], 1):
                longest = max(len(w[0]) for w in q['wrong'])
                if conspicuous(q['correct'], [w[0] for w in q['wrong']]):
                    eq.ISSUES.append('LONG S%d-%s-Q%d %d>%d | %s || %s' % (n, code, i, len(q['correct']),
                                     int(1.2 * longest), q['correct'], max((w[0] for w in q['wrong']), key=len)))
    if eq.ISSUES:
        print('\n'.join(eq.ISSUES))
        sys.exit('%d authoring problems' % len(eq.ISSUES))
    letters = assign_letters(all_sets)
    recs, sets_pkg = build_records(all_sets, letters)
    write_package(sets_pkg)
    if pdf:
        qp = os.path.join(ROOT, FILE + '_Question_Collection.pdf')
        page_of = make_question_pdf(recs, qp)
        for r in recs:
            r['question_page'] = page_of[r['id']]
        kp = os.path.join(ROOT, FILE + '_Answer_Key.pdf')
        make_key_pdf(recs, kp)
        for f in (qp, kp):
            shrink_pdf(f)
    write_key(recs)
    longest = [r['id'] for r in recs if len(r['correct_answer']) > max(len(w['text']) for w in r['wrong_choices'])]
    consp = [r['id'] for r in recs if conspicuous(r['correct_answer'], [w['text'] for w in r['wrong_choices']])]
    print('Artificial Intelligence: %d of %d planned sets, %d questions; key is the unique longest choice in %d (%.0f%%); '
          'conspicuously longest (>20%% and 7+ characters longer than every other choice) in %d'
          % (len(all_sets), len(plan.SETS), len(recs), len(longest), 100.0 * len(longest) / max(1, len(recs)), len(consp)))
    if '--consp' in sys.argv:
        for r in recs:
            if r['id'] in consp:
                print('  %s | %d | %s' % (r['id'], len(r['correct_answer']),
                                          max((w['text'] for w in r['wrong_choices']), key=len)))
    return all_sets, recs


if __name__ == '__main__':
    main(pdf='--nopdf' not in sys.argv)
