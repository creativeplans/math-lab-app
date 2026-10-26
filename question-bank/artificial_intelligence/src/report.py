"""Write the Artificial Intelligence reports and the import ZIP (run after build.py and validate.py).

    python3 question-bank/artificial_intelligence/src/report.py

Writes COVERAGE.md, SOURCES.md, README.md and CHANGELOG.md next to the answer key and in the package; splits the two
PDFs into volumes at set boundaries (pdf/ with PART_INDEX.md); writes MANIFEST.json; zips the package as
question-bank/nexus/Artificial_Intelligence_Nexus_Import_v<version>.zip.
"""
import collections
import datetime
import hashlib
import json
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import plan  # noqa: E402
import sources  # noqa: E402
import build  # noqa: E402

ROOT, PKG, QB = build.ROOT, build.PKG, build.QB
PART_PAGES = 500          # target pages per question volume; volumes break at the start of a set
MOD_TITLE = {m[0]: m[1] for m in plan.MODULES}
NUM = plan.SET_NUM

# The topic domains A-T of the course request, and the set-code families that teach them.
DOMAINS = [
    ('A', 'What AI is and where it appears', ['AI.BASICS.']),
    ('B', 'Learning and using a model', ['AI.LEARN.']),
    ('C', 'LLMs and language generation', ['AI.LLM.']),
    ('D', 'Prompt engineering and task design', ['AI.PROMPT.']),
    ('E', 'Checking results and handling uncertainty', ['AI.CHECK.']),
    ('F', 'Research, writing, learning and everyday use', ['AI.EVERYDAY.']),
    ('G', 'Retrieval, files and supplied information', ['AI.RETRIEVAL.', 'AI.SECURITY.03']),
    ('H', 'Images, design and presentations', ['AI.IMAGE.']),
    ('I', 'Audio, music, video and synthetic media', ['AI.MEDIA.']),
    ('J', 'Code assistance and software development', ['AI.CODE.']),
    ('K', 'Agents, automation and human approval', ['AI.AGENT.']),
    ('L', 'Privacy, security and misuse', ['AI.PRIVACY.', 'AI.SECURITY.']),
    ('M', 'Bias, fairness and accessibility', ['AI.FAIR.', 'AI.EVERYDAY.08', 'AI.IMAGE.06']),
    ('N', 'Law, policy, copyright and responsibility', ['AI.LAW.', 'AI.MEDIA.03', 'AI.MEDIA.04']),
    ('O', 'Philosophy and social questions', ['AI.PHIL.']),
    ('P', 'Work, jobs and careers', ['AI.WORK.']),
    ('Q', 'Costs, tools and practical selection', ['AI.COST.']),
    ('R', 'Evaluation and measurement', ['AI.EVAL.']),
    ('S', 'Practical constraints and overlooked pitfalls', ['AI.PITFALL.']),
    ('T', 'History, present systems and future claims', ['AI.HISTORY.']),
]


def domain_sets(prefixes):
    return [n for n, p in plan.SETS.items() if any(p['code'] == x or (x.endswith('.') and p['code'].startswith(x))
                                                   for x in prefixes)]


def load():
    return json.load(open(os.path.join(ROOT, 'AI_Answer_Key.json'), encoding='utf-8'))['questions']


def write_both(name, text):
    for d in (ROOT, PKG):
        open(os.path.join(d, name), 'w', encoding='utf-8').write(text)


def sets_pkg():
    index = json.load(open(os.path.join(PKG, 'index.json'), encoding='utf-8'))
    return index, {s['set']: json.load(open(os.path.join(PKG, s['file']), encoding='utf-8')) for s in index['sets']}


# ------------------------------------------------------------------ coverage
def coverage(recs):
    index, ps = sets_pkg()
    by_set = collections.Counter(r['set'] for r in recs)
    out = ['# Artificial Intelligence collection: coverage', '',
           '%d focused sets, %d questions. Every set has MAIN (5), at least one backward branch (5 each), F1 "Apply it" '
           '(5) and F2 "Handle the complications" (5). Shared skills are taught once in the foundation; path sets refer '
           'back to them through `requires`.' % (len(ps), len(recs)), '',
           '## Modules', '', '| Module | Kind | Paths | Sets |', '|---|---|---|---|']
    for m in index['modules']:
        out.append('| %s | %s%s | %s | %s |' % (m['title'], m['kind'], ' (optional)' if m.get('optional') else '',
                                                ', '.join(m.get('paths', [])) or 'all', ', '.join(map(str, m['sets']))))
    out += ['', '## Paths', '']
    for p in index['paths']:
        own = [n for n, s in ps.items() if s['path_refs'] == [p['id']]]
        out.append('- **%s** (`%s`): %s Path sets: %s. Learners on this path also take every foundation set.'
                   % (p['title'], p['id'], p['description'], ', '.join(map(str, own))))
    out += ['', '## Required topic domains (A-T) and the sets that teach them', '',
            '| Domain | Topic | Sets |', '|---|---|---|']
    for d, title, pre in DOMAINS:
        ns = sorted(domain_sets(pre))
        assert ns, d
        out.append('| %s | %s | %s |' % (d, title, ', '.join('%d %s' % (n, plan.SETS[n]['title']) for n in ns)))
    out += ['', '## Every set', '',
            '| Set | Code | Title | Module | Requires | Backward branches (mode: diagnostic reason) | Status | Questions |',
            '|---:|---|---|---|---|---|---|---:|']
    for n in sorted(ps):
        s = ps[n]
        br = '; '.join('%s %s: %s' % (x['section'], x['branch_mode'].replace('_', ' '), x['relationship'])
                       for x in s['sections'] if x['relation'] == 'backward')
        out.append('| %d | %s | %s | %s | %s | %s | %s | %d |' % (
            n, s['outcome'], s['title'], MOD_TITLE[s['module']], ', '.join(map(str, s['requires'])) or 'none',
            br.replace('|', '/'), s['content_status'].replace('_', '-'), by_set[n]))
    modes = collections.Counter(r['branch_mode'] for r in recs if r['section'].startswith('B') and r['number'] == 1)
    out += ['', '## Backward branches', '',
            '- Concept simplification (the same idea explained through a different, everyday comparison): %d branches.'
            % modes['concept_simplification'],
            '- Underlying skill (a supporting skill such as reading a table, matching a claim to a source, counting, '
            'tracing code or simple arithmetic): %d branches.' % modes['underlying_skill'],
            '- Every branch states the reason it helps a learner who missed MAIN (listed in the table above). No branch '
            'is nested and no branch reveals a MAIN answer.', '']
    write_both('COVERAGE.md', '\n'.join(out))


# ------------------------------------------------------------------ sources and review schedule
def source_ledger():
    _, ps = sets_pkg()
    uses = collections.defaultdict(list)
    for n, p in plan.SETS.items():
        for k in p['sources']:
            uses[k].append(n)
    out = ['# Artificial Intelligence collection: sources and review schedule', '',
           'Every time-sensitive set lists its sources in its set file (URL, claim, date checked), a review interval '
           'and a jurisdiction. This ledger lists each source once with the sets that rely on it and its next review '
           'date (date checked + review interval).', '',
           '**How the sources were checked.** %s. The checking date for every source is %s. For %d sources the claim '
           'could not be confirmed from the official page itself (the note on each says what was used instead: '
           'secondary sources, a search excerpt or a statute citation); the course teaches only the general '
           'principle and dated facts, never a settled answer to an open legal question. These are '
           'marked "needs direct check" below and should be opened directly at the first review.'
           % (sources.METHOD[0].upper() + sources.METHOD[1:], sources.CHECKED,
              len([k for k in sources.UNCONFIRMED if k in uses])), '',
           '| Source | Claim | Jurisdiction | Checked | Review every | Next review | Status | Sets |',
           '|---|---|---|---|---:|---|---|---|']
    for k in sorted(uses, key=lambda x: (x.startswith('case_'), x)):
        e = sources.entry(k)
        nxt = (datetime.date.fromisoformat(e['checked']) + datetime.timedelta(days=e['review_days'])).isoformat()
        status = 'confirmed by search' if e['confirmed_by_search'] else 'needs direct check: ' + e['note']
        out.append('| [%s](%s) | %s | %s | %s | %d days | %s | %s | %s |' % (
            k, e['url'], e['claim'].replace('|', '/'), e['jurisdiction'], e['checked'], e['review_days'], nxt,
            status.replace('|', '/'), ', '.join(map(str, sorted(uses[k])))))
    rows = sorted((datetime.date.fromisoformat(s['sources'][0]['checked']) +
                   datetime.timedelta(days=s['review_interval_days']), n) for n, s in ps.items()
                  if s['content_status'] == 'time_sensitive')
    out += ['', '## Review schedule by set', '', 'The game\'s import report (`reviewList`) shows the same dates.', '',
            '| Review due | Sets |', '|---|---|']
    by_date = collections.defaultdict(list)
    for d, n in rows:
        by_date[d.isoformat()].append(n)
    for d in sorted(by_date):
        out.append('| %s | %s |' % (d, ', '.join(map(str, by_date[d]))))
    out += ['', 'Prices and rates in questions (plans, tokens, costs per task) are hypothetical and labeled as such; they '
            'are not any provider\'s current prices. People, companies, prompts and AI responses in scenarios are '
            'fictional and labeled; no simulated output is attributed to a real product.', '']
    write_both('SOURCES.md', '\n'.join(out))


# ------------------------------------------------------------------ PDF volumes
def split_pdfs(recs):
    import pymupdf
    pdfdir = os.path.join(PKG, 'pdf')
    os.makedirs(pdfdir, exist_ok=True)
    for f in os.listdir(pdfdir):
        os.remove(os.path.join(pdfdir, f))
    qdoc = pymupdf.open(os.path.join(ROOT, 'AI_Question_Collection.pdf'))
    kdoc = pymupdf.open(os.path.join(ROOT, 'AI_Answer_Key.pdf'))
    first_page = {}
    for r in recs:
        first_page.setdefault(r['set'], r['question_page'])
    starts = sorted((n, first_page[n] - 1) for n in first_page)
    bounds, cur = [], 1
    for n, pg in starts:
        if pg - cur >= PART_PAGES:
            bounds.append((cur, pg - 1))
            cur = pg
    bounds.append((cur, qdoc.page_count))
    key_page = {}
    for i in range(kdoc.page_count):
        for m in re.findall(r'\bS\d+-(?:M|B\d|F[12])-Q\d\b', kdoc[i].get_text()):
            key_page.setdefault(m, i + 1)
    missing = [r['id'] for r in recs if r['id'] not in key_page]
    assert not missing, 'answer-key pages not found for %s' % missing[:5]
    rows_q, rows_k = [], []
    for idx, (a, b) in enumerate(bounds, 1):
        qs = [r for r in recs if a <= r['question_page'] <= b]
        sets = sorted({r['set'] for r in qs})
        name = 'AI - Volume %d - questions.pdf' % idx
        part = pymupdf.open()
        part.insert_pdf(qdoc, from_page=a - 1, to_page=b - 1)
        part.save(os.path.join(pdfdir, name), garbage=4, deflate=True)
        part.close()
        rows_q.append((name, a, b, '%d-%d' % (sets[0], sets[-1]), qs[0]['id'], qs[-1]['id'], len(qs)))
        ka = key_page[qs[0]['id']]
        kb = (key_page[recs[recs.index(qs[-1]) + 1]['id']] - 1) if qs[-1] is not recs[-1] else kdoc.page_count
        kb = max(kb, ka)
        kname = 'AI - Volume %d - answer key.pdf' % idx
        part = pymupdf.open()
        part.insert_pdf(kdoc, from_page=ka - 1, to_page=kb - 1)
        part.save(os.path.join(pdfdir, kname), garbage=4, deflate=True)
        part.close()
        rows_k.append((kname, ka, kb, '%d-%d' % (sets[0], sets[-1]), qs[0]['id'], qs[-1]['id'], len(qs)))
    for rows, full in ((rows_q, qdoc), (rows_k, kdoc)):
        for name, a, b, *_ in rows:
            part = pymupdf.open(os.path.join(pdfdir, name))
            assert part.page_count == b - a + 1, name
            for i in range(part.page_count):
                assert part[i].get_text() == full[a - 1 + i].get_text(), (name, i)
    out = ['# PDF volumes: page and question ranges', '',
           'The question collection (one question per page, with its teaching passage above the question and a '
           'reference label at the bottom) is split at the start of a set, about %d pages per volume. Page numbers are '
           'pages of the full PDF (`AI_Question_Collection.pdf`; the `question_page` field of the answer '
           'key). Every page of every volume was compared with the same page of the full PDF when this index was '
           'written; all match.' % PART_PAGES, '',
           'The answer key holds several answers per page, so a volume boundary can share a page with the next volume; '
           'that page appears in both.', '',
           '## Question collection (%d pages)' % qdoc.page_count, '',
           '| File | Full-PDF pages | Sets | First question | Last question | Questions |', '|---|---|---|---|---|---:|']
    out += ['| %s | %d-%d | %s | %s | %s | %d |' % r for r in rows_q]
    out += ['', '## Answer key (%d pages)' % kdoc.page_count, '',
            '| File | Answer-key pages | Sets | First question | Last question | Questions |', '|---|---|---|---|---|---:|']
    out += ['| %s | %d-%d | %s | %s | %s | %d |' % r for r in rows_k]
    out.append('')
    open(os.path.join(pdfdir, 'PART_INDEX.md'), 'w', encoding='utf-8').write('\n'.join(out))
    shutil_copy = os.path.join(ROOT, 'PART_INDEX.md')
    open(shutil_copy, 'w', encoding='utf-8').write('\n'.join(out))
    return rows_q, qdoc.page_count, kdoc.page_count


# ------------------------------------------------------------------ README, manifest, zip
def readme(recs, nvol, qpages, kpages, checks, importer):
    index, ps = sets_pkg()
    ts = sum(1 for s in ps.values() if s['content_status'] == 'time_sensitive')
    nb = sum(1 for s in ps.values() for x in s['sections'] if x['relation'] == 'backward')
    nex = sum(1 for r in recs if r.get('example'))
    ncode = sum(1 for r in recs if r.get('example') and r['example']['kind'] == 'code')
    found = [m for m in index['modules'] if m['kind'] == 'foundation']
    text = '''# Artificial Intelligence: Understanding and Using AI Wisely

Untangle The Nexus question collection `AI` (course `artificial_intelligence`, category Adults & HS Students),
version {ver} ({date}). {nsets} focused sets ({nsets} MAIN sets, {nb} backward branches, {nsets} F1 and {nsets} F2
sections), {nq} multiple-choice questions. Generated from `question-bank/artificial_intelligence/src` (plan.py,
sources.py and data_*.py) by build.py, validate.py and report.py. Regenerate there rather than editing these files
by hand.

{scope}

**No live AI lab, no external account, no paid service and no creation task.** Learners read a teaching passage and
answer a four-choice question. Every prompt, response, code snippet, table and log is a prepared example written for
this course and labeled as such; nothing is generated or executed by the learner.

## What is in this collection

- A shared foundation of {nfound} modules (what AI is; how a model learns; large language models; asking for what you
  need; checking results; privacy and security basics), an optional specialty module (kinds of learning,
  reinforcement learning, transformers), and five selectable paths: Everyday use; Creative work; Coding & automation;
  Work & careers; Society, law & philosophy. Shared skills are taught once and referenced by `requires`; optional
  connections are listed separately as `suggested`.
- Every set: MAIN (5 questions), at least one backward branch ({nb} in total; concept simplification or underlying
  skill, each with its diagnostic reason), F1 "Apply it" (5) and F2 "Handle the complications" (5).
- Every question has its own teaching passage (55-125 words), a scenario question, 4 choices with one correct answer,
  feedback, and (in the private key) a reason for every wrong choice. {nex} questions show a prepared example
  ({ncode} with Python 3 code; every complete program was executed at build time and its printed output checked).
- {ts} time-sensitive sets (law, policy, provider facts, careers, history, energy) carry sources with a jurisdiction,
  effective year, date checked and review interval; the rest are stable concepts.
- Disputed questions (who owns AI output, training-data copyright, fairness goals, the Turing test, the Chinese Room,
  machine consciousness, alignment, general intelligence) are taught as open; no key settles them.

## Files

| Path | Contents |
|---|---|
| `index.json` | Course, bank version, category, scope note, outcomes, the five paths, the modules and every set with its file |
| `sets/Sxxx.json` | One file per set: prerequisites, suggested reading, sources, and sections M, B1..., F1, F2 with 5 questions each |
| `COVERAGE.md` | Domains A-T mapped to sets, modules and paths, and every set with its branches and diagnostic reasons |
| `SOURCES.md` | Every source with its claim, jurisdiction, date checked, review interval and next review date |
| `VALIDATION.md` | Every validation check, its result, and the known limitations |
| `CHANGELOG.md` | Version policy and what changed |
| `pdf/` | The question collection and the answer key in {nvol} volumes each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

The full PDFs (`AI_Question_Collection.pdf`, {qp} pages, one question per page; `AI_Answer_Key.pdf`, {kp} pages) and
the answer key as JSON and CSV (`AI_Answer_Key.json`, `AI_Answer_Key.csv`, with `question_page` for every ID) are in
`question-bank/artificial_intelligence/`.

## Decisions where the contract overrides the request

- **Question IDs.** The request suggested `AI-S001-M-Q01`. The importer contract (COURSE-BANKS.md) requires
  `S<set>-<section>-Q<n>`, stored by the game as `AI:S1-M-Q1`. The bank uses the contract format; the mapping is
  one-to-one (`AI-S001-M-Q01` = `AI:S1-M-Q1`).
- **Routing.** The request said 5/5 mastered, 4/5 fresh MAIN, 0-3/5 backward. The owner's rule for every course
  (COURSE-BANKS.md, decision of 2026-10-22) is 5/5 mastered; 3-4/5 a fresh MAIN set; 0-2/5 all backward branches,
  then a fresh MAIN set. The game applies the owner's rule.
- **Reserve pools.** The importer (`tools/import-collection/v2.ts`) accepts exactly 5 questions per section, so no
  reserve or variant questions can be imported. When a learner has seen a whole pool, the game reuses the
  least-recently-seen question (exhaustion behavior). No template generation is used.

## How it is graded

Every question is multiple choice (`"type": "mc"`); the game's grader compares the chosen letter with
`correct_letter`. No free-text or AI grading is needed.

## Installing (the owner uploads the ZIP; Claude runs the commands)

1. Put `Artificial_Intelligence_Nexus_Import_v{ver}.zip` on the work branch under `content-src/artificial_intelligence/`.
2. Check only: `npx tsx tools/import-collection/import.ts --check content-src/artificial_intelligence/Artificial_Intelligence_Nexus_Import_v{ver}.zip`
3. Install: `npx tsx tools/import-collection/import.ts content-src/artificial_intelligence/Artificial_Intelligence_Nexus_Import_v{ver}.zip`
4. Roll back if needed: `npx tsx tools/import-collection/import.ts --rollback <course dir>`.
5. Release (`release: 'available'` in `packages/curriculum/src/courses.ts`) only after the owner approves.

Result of the check-only import run for this version: {importer}

## Checks run for this version

{checks}

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 questions (see "Reserve pools" above).
- Sources were checked through web-search results for the pages on {checked}; pages were not opened directly.
  {n_unconf} sources could not be confirmed from the primary page itself and are marked in `SOURCES.md` for a direct
  check at the first review. Law sets teach dated facts and what to check; they are general information, not legal
  advice.
- All prices and rates are hypothetical. All people, companies, prompts and AI responses are fictional; email
  addresses use reserved example domains.
- Explanations, wrong-choice reasons and keys were written and reviewed by the author; arithmetic in {arith} answers
  and every complete code example are checked by code.
- Answer-length balance: the correct answer is never conspicuously the longest choice and is the single longest in
  about {longest}% of questions (25% would be chance). Many wrong choices are padded misconceptions: in {wlong}% of
  questions one wrong choice is noticeably longer than the rest, and absolute words (always, never, every...) appear
  far more often in wrong choices than in correct ones. Both patterns point away from the key; they are listed in
  `VALIDATION.md` for the round-2 balancing edit.
'''.format(ver=build.VERSION, date=build.DATE, nsets=len(ps), nq=len(recs), scope=build.SCOPE_NOTE, nb=nb, ts=ts,
           nvol=nvol, qp=qpages, kp=kpages, importer=importer, checks='\n'.join('- ' + c for c in checks),
           checked=sources.CHECKED, n_unconf=len([k for k in sources.UNCONFIRMED if k in sources.SRC]),
           arith=sum(1 for r in recs if r['arithmetic_checked']), nex=nex, ncode=ncode, nfound=len(found),
           longest=round(100.0 * sum(1 for r in recs if len(r['correct_answer']) >
                                     max(len(w['text']) for w in r['wrong_choices'])) / len(recs)),
           wlong=round(100.0 * sum(1 for r in recs if any(build.conspicuous(
               w['text'], [r['correct_answer']] + [x['text'] for x in r['wrong_choices'] if x is not w])
               for w in r['wrong_choices'])) / len(recs)))
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
    m = {'collection': {'id': 'AI', 'course': 'artificial_intelligence', 'title': build.TITLE, 'version': build.VERSION,
                        'date': build.DATE}, 'file_count': len(files), 'files': files}
    json.dump(m, open(os.path.join(PKG, 'MANIFEST.json'), 'w', encoding='utf-8'), indent=1)
    return len(files)


def make_zip():
    path = os.path.join(QB, 'nexus', 'Artificial_Intelligence_Nexus_Import_v%s.zip' % build.VERSION)
    if os.path.exists(path):
        os.remove(path)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(PKG):
            for f in sorted(fs):
                p = os.path.join(dp, f)
                z.write(p, os.path.join('artificial_intelligence', os.path.relpath(p, PKG)))
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        n = len(z.namelist())
    return path, n


def main():
    checks = [l.strip() for l in open(os.path.join(HERE, 'CHECKS.txt'), encoding='utf-8')]
    importer = open(os.path.join(HERE, 'IMPORTER.txt'), encoding='utf-8').read().strip() \
        if os.path.exists(os.path.join(HERE, 'IMPORTER.txt')) else 'not run'
    recs = load()
    assert all(r['question_page'] for r in recs), 'run build.py with PDFs first'
    coverage(recs)
    source_ledger()
    write_both('CHANGELOG.md', open(os.path.join(HERE, 'CHANGELOG.md'), encoding='utf-8').read())
    rows, qp, kp = split_pdfs(recs)
    readme(recs, len(rows), qp, kp, checks, importer)
    nfiles = manifest()
    zpath, nz = make_zip()
    print('reports written; %d volumes; manifest %d files; zip %s (%d entries)' % (len(rows), nfiles, zpath, nz))


if __name__ == '__main__':
    main()
