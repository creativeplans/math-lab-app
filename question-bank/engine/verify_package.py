"""Check an Untangle The Nexus import package (a folder or its ZIP) for broken references.

    python3 question-bank/engine/verify_package.py question-bank/nexus/Grade5_Nexus_Import_v2.0.0.zip

Checks: every file in MANIFEST.json is present with the right size and SHA-256; index.json lists each set file,
and each section's question IDs match the set file in order; every ID and uid is unique and has the collection
prefix; every figure and picture-choice asset exists, and no asset is unreferenced; multiple-choice and true/false
letters exist among the choices; drawing + written and required-work questions carry their grading fields;
retired IDs from revisions.json do not appear, and every new or revised ID does. Exit status 1 on any problem.
"""
import hashlib
import json
import os
import sys
import zipfile


class Source:
    def __init__(self, path):
        self.zip = None
        if zipfile.is_zipfile(path):
            self.zip = zipfile.ZipFile(path)
            names = self.zip.namelist()
            roots = {n.split('/')[0] for n in names}
            self.prefix = (roots.pop() + '/') if len(roots) == 1 and any('/' in n for n in names) else ''
            self.names = {n[len(self.prefix):] for n in names if not n.endswith('/')}
        else:
            self.root = path
            self.names = set()
            for r, _, fs in os.walk(path):
                for f in fs:
                    self.names.add(os.path.relpath(os.path.join(r, f), path).replace(os.sep, '/'))

    def read(self, rel):
        if self.zip:
            return self.zip.read(self.prefix + rel)
        return open(os.path.join(self.root, rel), 'rb').read()

    def json(self, rel):
        return json.loads(self.read(rel).decode('utf-8'))


def verify(path):
    src = Source(path)
    errs = []
    man = src.json('MANIFEST.json')
    listed = set()
    for f in man['files']:
        listed.add(f['path'])
        if f['path'] not in src.names:
            errs.append('missing file ' + f['path'])
            continue
        data = src.read(f['path'])
        if len(data) != f['bytes'] or hashlib.sha256(data).hexdigest() != f['sha256']:
            errs.append('checksum mismatch ' + f['path'])
    extra = src.names - listed - {'MANIFEST.json'}
    if extra:
        errs.append('files not in MANIFEST.json: %s' % sorted(extra)[:10])

    index = src.json('index.json')
    cid = index['collection']['id']
    ids, uids, referenced = set(), set(), set()
    counts = {}
    for s in index['sets']:
        doc = src.json(s['file'])
        if doc['set'] != s['set']:
            errs.append('%s: set number %s does not match index %s' % (s['file'], doc['set'], s['set']))
        if [x['section_code'] for x in doc['sections']] != [x['section_code'] for x in s['sections']]:
            errs.append('%s: sections differ from index' % s['file'])
        for isec, sec in zip(s['sections'], doc['sections']):
            qids = [q['id'] for q in sec['questions']]
            if qids != isec['question_ids']:
                errs.append('%s %s: question IDs differ from index' % (s['file'], sec['section_code']))
            if len(qids) != 5:
                errs.append('%s %s: %d questions' % (s['file'], sec['section_code'], len(qids)))
            for q in sec['questions']:
                qid = q['id']
                counts[q['type']] = counts.get(q['type'], 0) + 1
                if qid in ids:
                    errs.append('duplicate id ' + qid)
                ids.add(qid)
                if q['uid'] != '%s:%s' % (cid, qid) or q['uid'] in uids:
                    errs.append('bad or duplicate uid ' + q['uid'])
                uids.add(q['uid'])
                if not qid.startswith('S%d-%s-' % (s['set'], sec['section_code'])):
                    errs.append('id %s is not in set %s section %s' % (qid, s['set'], sec['section_code']))
                letters = [c['letter'] for c in q['choices']]
                if q['type'] in ('mc', 'tf') and q['correct_letter'] not in letters:
                    errs.append('%s: correct letter %s not among choices' % (qid, q['correct_letter']))
                if q['type'] == 'plot_text' and not (q.get('drawing_answer') and q.get('correct_answer')):
                    errs.append('%s: drawing + written question lacks drawing_answer or correct_answer' % qid)
                if q['type'] == 'work' and not q.get('required_method'):
                    errs.append('%s: required-work question lacks required_method' % qid)
                if q['type'] in ('plot', 'plot_text') and not (q.get('figure') and q['figure'].get('blank_for_drawing')):
                    errs.append('%s: drawing question without a drawable figure' % qid)
                if not q.get('correct_answer'):
                    errs.append('%s: empty correct_answer' % qid)
                refs = []
                if q.get('figure'):
                    refs += [q['figure']['svg'], q['figure']['png']]
                for c in q['choices']:
                    refs += [c[k] for k in ('svg', 'png') if k in c]
                for r in refs:
                    referenced.add(r)
                    if r not in src.names:
                        errs.append('%s: missing asset %s' % (qid, r))
    assets = {n for n in src.names if n.startswith('assets/')}
    if assets - referenced:
        errs.append('unreferenced assets: %s' % sorted(assets - referenced)[:10])
    if index['question_count'] != len(ids):
        errs.append('index question_count %d but %d questions found' % (index['question_count'], len(ids)))

    if index.get('revisions_file'):
        rev = src.json(index['revisions_file'])
        for e in rev['entries']:
            if e['status'] == 'retired' and e['id'] in ids:
                errs.append('retired id still present: ' + e['id'])
            if e['status'] != 'retired' and e['id'] not in ids:
                errs.append('revision entry for a missing id: ' + e['id'])
        if len([e for e in rev['entries'] if e['status'] != 'retired']) != len(ids):
            errs.append('revisions.json does not cover every question')
    return errs, len(ids), len(referenced), counts


if __name__ == '__main__':
    errs, nq, na, counts = verify(sys.argv[1])
    print('%s: %d questions, %d asset files referenced, types %s' % (sys.argv[1], nq, na, counts))
    for e in errs[:50]:
        print('  ERROR', e)
    print('OK' if not errs else '%d problems' % len(errs))
    sys.exit(1 if errs else 0)
