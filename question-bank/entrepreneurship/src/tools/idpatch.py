"""Replace a choice text inside one question, located by its ID:
python3 idpatch.py patch.json   where patch.json is {"S80-B1-Q4": {"old text": "new text"}, ...}.
The question's prompt is looked up in the built answer key, found in the data files, and the first quoted
occurrence of the old text after that prompt is replaced. Run build.py first so the key is current."""
import glob, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY = os.path.join(os.path.dirname(HERE), 'Entrepreneurship_Answer_Key.json')


def quoted(t):
    return ["'%s'" % t.replace("'", "\\'"), '"%s"' % t]


def main(path):
    patch = json.load(open(path, encoding='utf-8'))
    qs = {q['id']: q for q in json.load(open(KEY, encoding='utf-8'))['questions']}
    files = {f: open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py')))}
    bad = []
    for qid, reps in patch.items():
        hits = []
        for head in [qs[qid]['prompt'][:30].replace("'", "\\'")] + quoted(qs[qid]['correct_answer']):
            hits = [(f, s.find(head)) for f, s in files.items() if s.count(head) == 1]
            if len(hits) == 1 and sum(s.count(head) for s in files.values()) == 1:
                break
            hits = []
        if len(hits) != 1:
            bad.append((qid, 'prompt not unique'))
            continue
        f, at = hits[0]
        for old, new in reps.items():
            s = files[f]
            pos = [(s.find(q, at), q) for q in quoted(old) if s.find(q, at) >= 0]
            if not pos:
                bad.append((qid, old))
                continue
            p, q = min(pos)
            rep = "'%s'" % new.replace("'", "\\'") if q.startswith("'") else '"%s"' % new
            files[f] = s[:p] + rep + s[p + len(q):]
    for f, s in files.items():
        open(f, 'w', encoding='utf-8').write(s)
    print('patched %d questions, failed %s' % (len(patch), bad))


if __name__ == '__main__':
    main(sys.argv[1])
