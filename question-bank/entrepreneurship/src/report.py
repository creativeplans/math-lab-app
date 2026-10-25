"""Write the Entrepreneurship reports and the import ZIP (run after build.py and validate.py).

    python3 question-bank/entrepreneurship/src/report.py

Writes COVERAGE.md, SOURCES.md, README.md and CHANGELOG.md next to the answer key and in the package; splits the two
PDFs into volumes at set boundaries (pdf/ with PART_INDEX.md); writes MANIFEST.json; zips the package as
question-bank/nexus/Entrepreneurship_Nexus_Import_v<version>.zip.
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

# What a first-time owner most often forgets, and where the course teaches it (set codes).
CHECKLIST = [
    ('Choosing a business name that is free to use, and knowing a DBA or state filing is not a trademark',
     ['ENT.LEGAL.01', 'ENT.LEGAL.02', 'ENT.LEGAL.08']),
    ('Sole proprietorship versus LLC or corporation, and that legal form and tax treatment are different choices',
     ['ENT.LEGAL.03', 'ENT.LEGAL.04', 'ENT.LEGAL.05']),
    ('Registered agent, operating agreement and personal guarantees', ['ENT.LEGAL.06', 'ENT.LEGAL.07', 'ENT.LEGAL.09']),
    ('Licenses, permits, zoning and home-business limits', ['ENT.LEGAL.10']),
    ('Getting an EIN free from the IRS, and state tax accounts', ['ENT.ID.01', 'ENT.ID.02', 'ENT.ID.03']),
    ('A separate business bank account, owner draws and reconciling', ['ENT.BANK.01', 'ENT.BANK.04', 'ENT.BANK.05']),
    ('Which address goes where: registered agent, mailing (PO Box, private mailbox, Form 1583), return address',
     ['ENT.MAIL.01', 'ENT.MAIL.02', 'ENT.MAIL.03', 'ENT.PROD.05']),
    ('Pricing from real costs, including fees, refunds and the owner\'s time', ['ENT.PRICE.01', 'ENT.PRICE.04',
                                                                             'ENT.PRICE.05', 'ENT.PRICE.06']),
    ('Profit is not cash; unpaid invoices, deposits and a cash reserve', ['ENT.CASH.01', 'ENT.CASH.02', 'ENT.CASH.03']),
    ('Keeping receipts and records, and how long to keep them', ['ENT.BOOK.01', 'ENT.TAX.06']),
    ('Sales tax versus income tax, self-employment tax, estimated payments and setting money aside',
     ['ENT.TAX.03', 'ENT.TAX.04', 'ENT.TAX.05']),
    ('Written quotes, payment terms, cancellation policies and scope changes', ['ENT.PAY.01', 'ENT.PAY.02', 'ENT.PAY.03',
                                                                             'ENT.PAY.04']),
    ('Chargebacks and payment or invoice scams', ['ENT.PAY.06', 'ENT.PAY.07', 'ENT.OPS.08']),
    ('Owning your domain and website accounts; HTTPS and backups', ['ENT.WEB.04', 'ENT.WEB.05']),
    ('Email permission and opt-outs; honest reviews; disclosing paid endorsements', ['ENT.MKT.03', 'ENT.MKT.05',
                                                                                    'ENT.MKT.06']),
    ('Checking AI output, protecting confidential data, and never inventing testimonials', ['ENT.AI.03', 'ENT.AI.04',
                                                                                           'ENT.AI.07']),
    ('Passwords, two-step login, access for helpers, and a lost-phone plan', ['ENT.OPS.04', 'ENT.OPS.05', 'ENT.OPS.09']),
    ('A deadline calendar for filings and renewals; forgotten subscriptions', ['ENT.OPS.07', 'ENT.OPS.03']),
    ('Insurance gaps in personal and home policies', ['ENT.RISK.01', 'ENT.RISK.02']),
    ('Permission for images, music, code and names; truthful advertising', ['ENT.RISK.05', 'ENT.RISK.06']),
    ('Contractor versus employee is not a label; payroll duties', ['ENT.HELP.02', 'ENT.HELP.03']),
    ('Loans, guarantees and money raised are not profit', ['ENT.FUND.02', 'ENT.FUND.05']),
    ('Burnout and closing a business honestly', ['ENT.GROW.04', 'ENT.GROW.05']),
]


def load():
    return json.load(open(os.path.join(ROOT, 'Entrepreneurship_Answer_Key.json'), encoding='utf-8'))['questions']


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
    out = ['# Entrepreneurship collection: coverage', '',
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
    out += ['', '## What a first-time owner most often forgets, and where it is taught', '',
            '| Topic | Sets |', '|---|---|']
    for topic, codes in CHECKLIST:
        out.append('| %s | %s |' % (topic, ', '.join('%d (%s)' % (NUM[c], plan.SETS[NUM[c]]['title']) for c in codes)))
    out += ['', '## Founder cases', '',
            'Each case passage begins with "Documented history" (what the cited source records) and then gives the '
            '"Lesson drawn by this course (an interpretation)", followed by "One success story does not guarantee the '
            'same result for another business." The backward branch of each case practices telling the two apart.', '',
            '| Set | Case | Module | Source |', '|---:|---|---|---|']
    for n in sorted(ps):
        if plan.SETS[n]['code'].startswith('ENT.CASE.'):
            e = sources.entry(plan.SETS[n]['sources'][0])
            out.append('| %d | %s | %s | %s |' % (n, plan.SETS[n]['title'], MOD_TITLE[plan.SETS[n]['module']], e['url']))
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
            '- Concept simplification (the same idea explained through an everyday comparison): %d branches.'
            % modes['concept_simplification'],
            '- Math prerequisite (the arithmetic the set relies on, such as percents, rates, rounding or totals): %d '
            'branches.' % modes['math_prerequisite'],
            '- Number-heavy sets (pricing, cash, fees, break-even, loans, runway) use a math branch; set 48 (markup and margin) uses '
            'both kinds. Every branch states the reason it helps a learner who missed MAIN (listed in the table above).', '']
    write_both('COVERAGE.md', '\n'.join(out))


# ------------------------------------------------------------------ sources and review schedule
def source_ledger():
    _, ps = sets_pkg()
    uses = collections.defaultdict(list)
    for n, p in plan.SETS.items():
        for k in p['sources']:
            uses[k].append(n)
    out = ['# Entrepreneurship collection: sources and review schedule', '',
           'Every time-sensitive set lists its sources in its set file (URL, claim, date checked), a review interval '
           'and a jurisdiction. This ledger lists each source once with the sets that rely on it and its next review '
           'date (date checked + review interval).', '',
           '**How the sources were checked.** %s. The checking date for every source is %s. For %d sources the official '
           'page did not come back in search; their claims were confirmed through secondary sources (named in the note) '
           'and the course teaches only the general principle, not current rates, thresholds or penalties. These are '
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
    out += ['', 'Numbers in questions (prices, fees, rates, wages, percentages) are practice assumptions stated as such '
            'in the passages; they are not market data, quotes from a provider, or current tax rates.', '']
    write_both('SOURCES.md', '\n'.join(out))


# ------------------------------------------------------------------ PDF volumes
def split_pdfs(recs):
    import pymupdf
    pdfdir = os.path.join(PKG, 'pdf')
    os.makedirs(pdfdir, exist_ok=True)
    for f in os.listdir(pdfdir):
        os.remove(os.path.join(pdfdir, f))
    qdoc = pymupdf.open(os.path.join(ROOT, 'Entrepreneurship_Question_Collection.pdf'))
    kdoc = pymupdf.open(os.path.join(ROOT, 'Entrepreneurship_Answer_Key.pdf'))
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
        name = 'Entrepreneurship - Volume %d - questions.pdf' % idx
        part = pymupdf.open()
        part.insert_pdf(qdoc, from_page=a - 1, to_page=b - 1)
        part.save(os.path.join(pdfdir, name), garbage=4, deflate=True)
        part.close()
        rows_q.append((name, a, b, '%d-%d' % (sets[0], sets[-1]), qs[0]['id'], qs[-1]['id'], len(qs)))
        ka = key_page[qs[0]['id']]
        kb = (key_page[recs[recs.index(qs[-1]) + 1]['id']] - 1) if qs[-1] is not recs[-1] else kdoc.page_count
        kb = max(kb, ka)
        kname = 'Entrepreneurship - Volume %d - answer key.pdf' % idx
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
           'pages of the full PDF (`Entrepreneurship_Question_Collection.pdf`; the `question_page` field of the answer '
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
    cases = sum(1 for n in ps if plan.SETS[n]['code'].startswith('ENT.CASE.'))
    nb = sum(1 for s in ps.values() for x in s['sections'] if x['relation'] == 'backward')
    text = '''# Entrepreneurship: Starting and Running a Small Business

Untangle The Nexus question collection `ENT` (course `entrepreneurship`, category Adults & HS Students), version
{ver} ({date}). {nsets} focused sets, {nq} multiple-choice questions. Generated from
`question-bank/entrepreneurship/src` (plan.py, sources.py and data_*.py) by build.py, validate.py and report.py.
Regenerate there rather than editing these files by hand.

{scope}

## What is in this collection

- A foundation of 15 modules every learner takes (start here, customers, testing demand, names and legal structure,
  EIN and banking, addresses and contact details, costs and pricing, bookkeeping and taxes, getting paid, website,
  marketing, AI as a helper, operations, risk, getting help), an optional specialty module (funding, growth and
  closing), and four paths: services; physical products; digital products; content creation. Shared skills are taught
  once and referenced by `requires`.
- {cases} founder cases spread through the course. Each separates the documented history (with its source) from the
  lesson this course draws, and says that one story does not guarantee the same result.
- Every set: MAIN (5 questions), backward branches ({nb} in total; concept simplification or math prerequisite, each
  with its diagnostic reason), F1 "Apply it" (5) and F2 "Handle the complications" (5).
- Every question has its own teaching passage (55-125 words), a scenario question, 4 choices with one best answer,
  feedback, and (in the private key) a reason for every wrong choice.
- {ts} time-sensitive sets carry sources, a review interval and a jurisdiction; the rest are stable.

## Files

| Path | Contents |
|---|---|
| `index.json` | Course, bank version, category, scope note, outcomes, the four paths, the modules and every set with its file |
| `sets/Sxxx.json` | One file per set: prerequisites, suggested reading, sources, and sections M, B1..., F1, F2 with 5 questions each |
| `COVERAGE.md` | Modules and paths, a checklist of what first-time owners forget mapped to sets, the founder cases, and every set with its branches |
| `SOURCES.md` | Every source with its claim, jurisdiction, date checked, review interval and next review date |
| `VALIDATION.md` | Every validation check and its result |
| `CHANGELOG.md` | Version policy and what changed |
| `pdf/` | The question collection and the answer key in {nvol} volumes each, with `PART_INDEX.md` (page mapping) |
| `MANIFEST.json` | Every file with its size and SHA-256 |

The full PDFs (`Entrepreneurship_Question_Collection.pdf`, {qp} pages; `Entrepreneurship_Answer_Key.pdf`, {kp} pages)
and the answer key as JSON and CSV are in `question-bank/entrepreneurship/`.

## How it is graded

Every question is multiple choice (`"type": "mc"`), so the game's automatic grader compares the chosen letter with
`correct_letter`. No free-text or AI grading is needed.

## How the game routes a learner

Under the owner's rule for every course (COURSE-BANKS.md, decision of 2026-10-22): 5/5 on MAIN = mastered and the
F1/F2 challenges unlock; 3-4/5 = a fresh MAIN set of the same skill; 0-2/5 = all backward branches, then a fresh MAIN
set. A course prompt that says "three or fewer correct" is read as this rule.

## Installing (the owner uploads the ZIP; Claude runs the commands)

1. Put `Entrepreneurship_Nexus_Import_v{ver}.zip` on the work branch under `content-src/entrepreneurship/`.
2. Check only: `npx tsx tools/import-collection/import.ts --check content-src/entrepreneurship/Entrepreneurship_Nexus_Import_v{ver}.zip`
3. Install: `npx tsx tools/import-collection/import.ts content-src/entrepreneurship/Entrepreneurship_Nexus_Import_v{ver}.zip`
4. Roll back if needed: `npx tsx tools/import-collection/import.ts --rollback <course dir>`.
5. Release (`release: 'available'` in `packages/curriculum/src/courses.ts`) only after the owner approves.

Result of the check-only import run for this version: {importer}

## Checks run for this version

{checks}

## Limits (stated honestly)

- Each section is a fixed pool of exactly 5 written questions; no extra variant questions are provided. The game
  reuses the least-recently-seen question when a learner has seen the whole pool, so a learner who repeats a section
  sees the same questions.
- Sources were checked through web-search results for the official pages on {checked} (pages were not opened
  directly). Nine claims were confirmed only through secondary sources; they are marked in `SOURCES.md` for a direct
  check at the first review. The course teaches principles and what to check, not current rates, thresholds or
  penalties.
- Laws and fees vary by state and city; examples that name a state (for example Washington's registered-agent rule)
  are labeled as examples.
- All prices, fees, rates and wages in questions are practice assumptions. All people and businesses in scenarios are
  fictional; email addresses use the reserved `.example` domain.
- Explanations, wrong-choice reasons and answer keys were written by the author; arithmetic in {arith} answers is
  checked by code, and the rest was reviewed by the author without a computer check.
- The correct answer is never conspicuously the longest choice, but it is the single longest choice in about
  {longest}% of questions (25% would be chance). This is reported in `VALIDATION.md` for review.
'''.format(ver=build.VERSION, date=build.DATE, nsets=len(ps), nq=len(recs), scope=build.SCOPE_NOTE, cases=cases, nb=nb,
           ts=ts, nvol=nvol, qp=qpages, kp=kpages, importer=importer, checks='\n'.join('- ' + c for c in checks),
           checked=sources.CHECKED, arith=sum(1 for r in recs if r['arithmetic_checked']),
           longest=round(100.0 * sum(1 for r in recs if len(r['correct_answer']) >
                                     max(len(w['text']) for w in r['wrong_choices'])) / len(recs)))
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
    m = {'collection': {'id': 'ENT', 'course': 'entrepreneurship', 'title': build.TITLE, 'version': build.VERSION,
                        'date': build.DATE}, 'file_count': len(files), 'files': files}
    json.dump(m, open(os.path.join(PKG, 'MANIFEST.json'), 'w', encoding='utf-8'), indent=1)
    return len(files)


def make_zip():
    path = os.path.join(QB, 'nexus', 'Entrepreneurship_Nexus_Import_v%s.zip' % build.VERSION)
    if os.path.exists(path):
        os.remove(path)
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(PKG):
            for f in sorted(fs):
                p = os.path.join(dp, f)
                z.write(p, os.path.join('entrepreneurship', os.path.relpath(p, PKG)))
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
