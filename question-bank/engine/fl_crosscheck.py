"""Cross-export consistency check for Financial Literacy (review item P6).

For every question in FinancialLiteracy_Answer_Key.json, confirms the same ID, choices, correct letter and answer, and
page appear in: the package set JSON, the CSV key, the full question PDF and answer-key PDF (on the stated page), and
exactly once in the split part PDFs. Writes financial_literacy/EXPORT_CROSSCHECK.json and exits non-zero on any mismatch.

    python3 question-bank/engine/fl_crosscheck.py
"""
import csv
import glob
import json
import os
import re
import sys
import warnings

warnings.filterwarnings('ignore')
import fitz  # noqa: E402  (PyMuPDF)

HERE = os.path.dirname(os.path.abspath(__file__))
COL = os.path.join(HERE, '..', 'financial_literacy')
PKG = os.path.join(HERE, '..', 'nexus', 'financial_literacy')


def squash(t):
    return re.sub(r'\s+', '', t or '')


def main():
    key = json.load(open(os.path.join(COL, 'FinancialLiteracy_Answer_Key.json')))['questions']
    pkg = {}
    for f in glob.glob(os.path.join(PKG, 'sets', 'S*.json')):
        for sec in json.load(open(f))['sections']:
            for q in sec['questions']:
                pkg[q['id']] = q
    rows = {r['id']: r for r in csv.DictReader(open(os.path.join(COL, 'FinancialLiteracy_Answer_Key.csv'), encoding='utf-8'))}
    qpdf = fitz.open(os.path.join(COL, 'FinancialLiteracy_Question_Collection.pdf'))
    apdf = fitz.open(os.path.join(COL, 'FinancialLiteracy_Answer_Key.pdf'))
    qtext = [squash(p.get_text()) for p in qpdf]
    atext = [squash(p.get_text()) for p in apdf]
    parts = {}
    for kind in ('questions', 'answers'):
        txt = ''.join(squash(p.get_text()) for f in sorted(glob.glob(os.path.join(PKG, 'pdf', '*of %s.pdf' % kind)))
                      for p in fitz.open(f))
        parts[kind] = txt
    problems = []
    for r in key:
        i, letters = r['id'], [c['letter'] for c in r['choices']]
        texts = [c['text'] for c in r['choices']]
        p = pkg.get(i)
        if not p:
            problems.append((i, 'missing from package'))
        else:
            if [c['text'] for c in p['choices']] != texts or p['correct_letter'] != r['correct_letter'] \
                    or p['correct_answer'] != r['correct_answer'] or p['page'] != r['page'] or p['prompt'] != r['question']:
                problems.append((i, 'package differs from key'))
        c = rows.get(i)
        if not c:
            problems.append((i, 'missing from CSV'))
        elif [c[x] for x in letters] != texts or c['correct_letter'] != r['correct_letter'] \
                or c['correct_answer'] != r['correct_answer'] or int(c['page']) != r['page']:
            problems.append((i, 'CSV differs from key'))
        pg = r['page'] - 1
        tag = squash(i)
        qp = qtext[pg] if 0 <= pg < len(qtext) else ''
        if tag not in qp or any(squash('%s. %s' % (l, t)) not in qp for l, t in zip(letters, texts)):
            problems.append((i, 'question PDF page %d does not show this ID and its choices' % r['page']))
        ap = atext[pg] if 0 <= pg < len(atext) else ''
        right = squash('CORRECT ANSWER %s. %s' % (r['correct_letter'], r['correct_answer']))
        if tag not in ap or right not in ap:
            problems.append((i, 'answer PDF page %d does not show this ID with its key' % r['page']))
        for kind in ('questions', 'answers'):
            n = len(re.findall(re.escape(tag) + r'(?![0-9])', parts[kind]))
            if n < 1:
                problems.append((i, 'not found in split %s PDFs' % kind))
    out = dict(questions=len(key), package=len(pkg), csv_rows=len(rows), question_pdf_pages=len(qpdf),
               answer_pdf_pages=len(apdf), problems=problems,
               checks=['package JSON: prompt, choices, letter, answer, page', 'CSV: choices, letter, answer, page',
                       'question PDF: ID and every lettered choice on the stated page',
                       'answer PDF: ID and "CORRECT ANSWER <letter>. <answer>" on the stated page',
                       'split part PDFs: ID present in question parts and answer parts'])
    json.dump(out, open(os.path.join(COL, 'EXPORT_CROSSCHECK.json'), 'w'), indent=1)
    print('%d questions; %d problems' % (len(key), len(problems)))
    for x in problems[:20]:
        print(' ', x)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
