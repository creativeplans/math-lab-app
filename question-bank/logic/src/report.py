"""Write the Logic reports and the import ZIP (run after build.py and validate.py).

    python3 question-bank/logic/src/report.py

Writes COVERAGE.md, SOURCE_MAP.md, README.md and PLAN.md next to the answer key and in the package; splits the two
PDFs into parts at set boundaries (pdf/ with PART_INDEX.md); writes MANIFEST.json; zips the package as
question-bank/nexus/Logic_Nexus_Import_v<version>.zip.
"""
import collections
import hashlib
import json
import os
import re
import shutil
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402
import build  # noqa: E402

ROOT, PKG, QB = build.ROOT, build.PKG, build.QB
PART_PAGES = 420          # target pages per PDF part; parts break at the start of a set
TYPE_NAME = {'mc': 'multiple choice', 'tf': 'true/false', 'sa': 'short answer', 'order': 'put in order',
             'grid': 'logic grid', 'truth_table': 'truth table', 'mark': 'mark cells or regions',
             'values': 'answer checked by a rule'}


def load():
    recs = json.load(open(os.path.join(ROOT, 'Logic_Answer_Key.json'), encoding='utf-8'))['questions']
    return recs


def write_both(name, text):
    for d in (ROOT, PKG):
        open(os.path.join(d, name), 'w', encoding='utf-8').write(text)


# ------------------------------------------------------------------ coverage
def coverage(recs):
    by_set = collections.defaultdict(list)
    for r in recs:
        by_set[r['set']].append(r)
    out = ['# Logic collection: coverage', '',
           '%d sets in the order students meet them. Every set has a MAIN section, at least one backward branch '
           '(a guided-strategy lesson with 5 practice problems, or a prerequisite check), FORWARD 1 (advanced '
           'application) and FORWARD 2 (expert challenge). Every section has exactly 5 questions.' % len(plan.SETS), '',
           '## Sets', '',
           '| Set | Title | Kind | Genre | Outcome | Practices | Standard | Backward branches | Questions |',
           '|---:|---|---|---|---|---|---|---|---:|']
    for n in sorted(plan.SETS):
        p = plan.SETS[n]
        rs = by_set[n]
        modes = []
        for code in sorted({r['section'] for r in rs if r['section'].startswith('B')}):
            m = [r['branch_mode'] for r in rs if r['section'] == code][0]
            modes.append('%s %s' % (code, 'guided strategy' if m == 'guided_strategy' else 'prerequisite'))
        out.append('| %d | %s | %s | %s | %s | %s | %s | %s | %d |' % (
            n, p[0], p[3], p[4], p[1], ', '.join(p[6]), (p[7] + ' (direct)') if p[7] else 'local outcome',
            '; '.join(modes), len(rs)))
    kinds = [plan.SETS[n][3] for n in sorted(plan.SETS)]
    run, worst = 0, 0
    for k in kinds:
        run = run + 1 if k == 'formal' else 0
        worst = max(worst, run)
    genres = collections.Counter(plan.SETS[n][4] for n in plan.SETS if plan.SETS[n][3] == 'puzzle')
    out += ['', '## Structure rules', '',
            '- Puzzle sets: %d of %d (at least half required).' % (kinds.count('puzzle'), len(kinds)),
            '- Puzzle sets among the first 10: %d (at least 6 required; set 1 is a puzzle).' % kinds[:10].count('puzzle'),
            '- Longest run of formal sets: %d (at most 2 allowed).' % worst,
            '- Puzzle genres: %d (at least 10 required): %s.' % (len(genres), ', '.join(sorted(genres))), '',
            '## Formal topics', '',
            'The formal sets cover: ' + '; '.join('%s (set %d)' % (plan.SETS[n][0], n) for n in sorted(plan.SETS)
                                                  if plan.SETS[n][3] == 'formal') + '.', '',
            '## Standards and practices', '',
            'Two sets align directly to a Common Core standard, after checking the standard\'s wording against the '
            'questions:', '']
    for code, text in plan.STANDARDS.items():
        sets = [n for n in plan.SETS if plan.SETS[n][7] == code]
        out.append('- **%s** (set %s): "%s"' % (code, ', '.join(map(str, sets)), text))
    out += ['', 'Every other set is assessed against its local outcome (listed above) and names the Standards for '
            'Mathematical Practice it supports:', '']
    mp = collections.Counter(m for n in plan.SETS for m in plan.SETS[n][6])
    for k in sorted(plan.PRACTICES):
        out.append('- %s %s: supported by %d sets.' % (k, plan.PRACTICES[k], mp[k]))
    types = collections.Counter(r['type'] for r in recs)
    out += ['', '## Question types', '', '| Type | Questions |', '|---|---:|']
    for t, c in types.most_common():
        out.append('| %s (`%s`) | %d |' % (TYPE_NAME.get(t, t), t, c))
    out.append('')
    write_both('COVERAGE.md', '\n'.join(out))


# ------------------------------------------------------------------ source map
def source_map():
    uses = collections.defaultdict(list)
    for n, p in plan.SETS.items():
        for ref in p[8]:
            uses[ref].append(n)
    out = ['# Logic collection: source-genre map', '',
           'The three "Game Show References for Logic" decks (15 puzzles each) were used only to choose puzzle '
           'GENRES. No deck question, wording, picture or answer is copied: every question in this collection is '
           'original, and none is a classic published riddle. The table lists each deck puzzle (deck, puzzle number), '
           'its genre in a few words, and the set or sets that teach that genre with new questions.', '',
           '| Deck | Puzzle | Genre (short description) | Sets that teach the genre |', '|---:|---:|---|---|']
    for (d, k) in sorted(plan.DECK):
        if (d, k) in plan.NOT_USED:
            where = 'not used: ' + plan.NOT_USED[(d, k)]
        else:
            where = ', '.join('S%d %s' % (n, plan.SETS[n][0]) for n in sorted(uses[(d, k)])) or 'general inspiration only'
        out.append('| %d | %d | %s | %s |' % (d, k, plan.DECK[(d, k)], where))
    out += ['', 'Two deck genres are not used because they cannot be answered fairly from the page: one depends on '
                'spoken stress (pronunciation) and one on knowing song lyrics.', '']
    write_both('SOURCE_MAP.md', '\n'.join(out))


# ------------------------------------------------------------------ PDF parts
def split_pdfs(recs):
    import pymupdf
    pdfdir = os.path.join(PKG, 'pdf')
    os.makedirs(pdfdir, exist_ok=True)
    qdoc = pymupdf.open(os.path.join(ROOT, 'Logic_Question_Collection.pdf'))
    kdoc = pymupdf.open(os.path.join(ROOT, 'Logic_Answer_Key.pdf'))
    first_page = {}
    for r in recs:
        first_page.setdefault(r['set'], r['question_page'])
    # a set's title page is the page before its first question
    starts = sorted((n, first_page[n] - 1) for n in first_page)
    bounds, cur = [], 1
    for n, pg in starts:
        if pg - cur >= PART_PAGES:
            bounds.append((cur, pg - 1))
            cur = pg
    bounds.append((cur, qdoc.page_count))
    # answer key: find the page of each question ID line in the key PDF
    key_page = {}
    for i in range(kdoc.page_count):
        for m in re.findall(r'\bS\d+-(?:M|B\d|F[12])-Q\d\b', kdoc[i].get_text()):
            key_page.setdefault(m, i + 1)
    missing = [r['id'] for r in recs if r['id'] not in key_page]
    assert not missing, 'answer-key pages not found for %s' % missing[:5]
    rows_q, rows_k = [], []
    for idx, (a, b) in enumerate(bounds, 1):
        qs = [r for r in recs if a <= r['question_page'] <= b]
        name = 'Logic - Part %d of questions.pdf' % idx
        part = pymupdf.open()
        part.insert_pdf(qdoc, from_page=a - 1, to_page=b - 1)
        part.save(os.path.join(pdfdir, name), garbage=4, deflate=True)
        part.close()
        rows_q.append((name, a, b, qs[0]['id'], qs[-1]['id'], len(qs)))
        ka = key_page[qs[0]['id']]
        kb = (key_page[recs[recs.index(qs[-1]) + 1]['id']] - 1) if qs[-1] is not recs[-1] else kdoc.page_count
        kb = max(kb, ka)
        kname = 'Logic - Part %d of answers.pdf' % idx
        part = pymupdf.open()
        part.insert_pdf(kdoc, from_page=ka - 1, to_page=kb - 1)
        part.save(os.path.join(pdfdir, kname), garbage=4, deflate=True)
        part.close()
        rows_k.append((kname, ka, kb, qs[0]['id'], qs[-1]['id'], len(qs)))
    # verify every part page against the full PDF
    for rows, full in ((rows_q, qdoc), (rows_k, kdoc)):
        for name, a, b, *_ in rows:
            part = pymupdf.open(os.path.join(pdfdir, name))
            assert part.page_count == b - a + 1, name
            for i in range(part.page_count):
                assert part[i].get_text() == full[a - 1 + i].get_text(), (name, i)
    out = ['# PDF parts: page and question ranges', '',
           'The question collection is split at the start of a set, about %d pages per part. Page numbers are pages of '
           'the full PDF (`Logic_Question_Collection.pdf`, the `question_page` field of the answer key). Every page of '
           'every part was compared with the same page of the full PDF when this index was written; all match.'
           % PART_PAGES, '',
           'Note: the answer key holds several answers per page, so its part boundaries can share a page with the next '
           'part; that shared page appears in both parts.', '',
           '## Question collection (%d pages)' % qdoc.page_count, '',
           '| File | Full-PDF pages | First question | Last question | Questions |', '|---|---|---|---|---:|']
    out += ['| %s | %d-%d | %s | %s | %d |' % r for r in rows_q]
    out += ['', '## Answer key (%d pages)' % kdoc.page_count, '',
            '| File | Answer-key pages | First question | Last question | Questions |', '|---|---|---|---|---:|']
    out += ['| %s | %d-%d | %s | %s | %d |' % r for r in rows_k]
    out.append('')
    open(os.path.join(pdfdir, 'PART_INDEX.md'), 'w', encoding='utf-8').write('\n'.join(out))
    return rows_q, qdoc.page_count, kdoc.page_count


# ------------------------------------------------------------------ README, manifest, zip
def readme(recs, nparts, qpages, kpages, checks):
    types = collections.Counter(r['type'] for r in recs)
    n_fig = len([f for f in os.listdir(os.path.join(PKG, 'assets'))])
    text = '''# Logic: High School Logic and Reasoning Puzzles

Untangle The Nexus question collection `LOGIC`, version {ver} ({date}). {nsets} sets, {nq} questions, {nfig} figure
files. Generated from `question-bank/logic/src` (plan.py and data_*.py) by build.py, validate.py and report.py.
Regenerate there rather than editing these files by hand.

## What is in this collection

- {nsets} sets in a fixed order: {npz} puzzle sets and {nfm} formal-logic sets. Set 1 is a puzzle, 6 of the first 10 sets
  are puzzles, and there are never more than 2 formal sets in a row.
- Every set: MAIN (5 questions), at least one backward branch (a guided-strategy lesson with a worked example of a
  different puzzle and 5 practice problems, or a 5-question prerequisite check), FORWARD 1 (advanced application,
  5 questions) and FORWARD 2 (expert challenge, 5 questions).
- Each question states its own conventions and supplies any word list it needs. Figures are exact grayscale SVG drawings
  with a text description.
- Outcomes are local (listed in `index.json`). Sets 39 (HSA-REI.A.1) and 43 (HSG-CO.C.9) align directly to a Common
  Core standard; Standards for Mathematical Practice MP1, MP2, MP3, MP6, MP7 and MP8 are listed as supporting practices.

## Files

| Path | Contents |
|---|---|
| `index.json` | Collection id and version, every outcome, the practices, and every set with its file |
| `sets/Sxx.json` | One file per set: sections (M, B1..., F1, F2) with relation, skill, branch mode, lesson and 5 questions each |
| `assets/*.svg` | Figures, referenced by the questions that use them |
| `COVERAGE.md` | Every set with kind, genre, outcome, practices, standard and branches; the structure rules; question types |
| `SOURCE_MAP.md` | Each deck puzzle genre and the sets that teach it (all questions are original) |
| `VALIDATION.md` | Every validation check and its result |
| `pdf/` | The question collection and the answer key in {nparts} parts each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

## Question types and how they are graded

All {nq} questions are graded automatically by the game:

{typelist}

Multiple choice and true/false compare letters. Ordering, logic-grid, truth-table and mark questions are checked by the
game against every accepted answer. Rule-checked answers (`values`) are checked by the game's rule language, so any
answer that meets the rule is accepted, not only the example. Short answers are checked by the game's answer evaluator
against `correct_answer`.

## Checks run for this version

{checks}

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 written questions. Nothing is generated at play time, so a student who
  repeats a section sees the same questions.
- Questions about arguments, fallacies, assumptions and evidence were solved by the author; they have no computer
  check, but every wrong choice has a written reason.
'''.format(ver=build.VERSION, date=build.DATE, nsets=len(plan.SETS), nq=len(recs), nfig=n_fig,
           npz=sum(1 for p in plan.SETS.values() if p[3] == 'puzzle'),
           nfm=sum(1 for p in plan.SETS.values() if p[3] == 'formal'), nparts=nparts,
           typelist='\n'.join('- %s (`%s`): %d' % (TYPE_NAME.get(t, t), t, c) for t, c in types.most_common()),
           checks='\n'.join('- ' + c for c in checks))
    write_both('README.md', text)


def manifest():
    files = []
    for dp, _, fs in os.walk(PKG):
        for f in sorted(fs):
            if f == 'MANIFEST.json':
                continue
            p = os.path.join(dp, f)
            files.append({'path': os.path.relpath(p, PKG).replace(os.sep, '/'), 'bytes': os.path.getsize(p),
                          'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()})
    files.sort(key=lambda x: x['path'])
    m = {'collection': {'id': 'LOGIC', 'course': 'logic', 'title': build.TITLE, 'version': build.VERSION,
                        'date': build.DATE}, 'file_count': len(files), 'files': files}
    json.dump(m, open(os.path.join(PKG, 'MANIFEST.json'), 'w', encoding='utf-8'), indent=1)
    return len(files)


def make_zip():
    path = os.path.join(QB, 'nexus', 'Logic_Nexus_Import_v%s.zip' % build.VERSION)
    if os.path.exists(path):
        os.remove(path)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(PKG):
            for f in sorted(fs):
                p = os.path.join(dp, f)
                z.write(p, os.path.join('logic', os.path.relpath(p, PKG)))
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        n = len(z.namelist())
    return path, n


def main():
    checks = [l.strip() for l in open(os.path.join(HERE, 'CHECKS.txt'), encoding='utf-8')] \
        if os.path.exists(os.path.join(HERE, 'CHECKS.txt')) else []
    recs = load()
    assert all(r['question_page'] for r in recs), 'run build.py with PDFs first'
    coverage(recs)
    source_map()
    rows, qp, kp = split_pdfs(recs)
    readme(recs, len(rows), qp, kp, checks)
    nfiles = manifest()
    zpath, nz = make_zip()
    print('reports written; %d PDF parts; manifest %d files; zip %s (%d entries)' % (len(rows), nfiles, zpath, nz))


if __name__ == '__main__':
    main()
