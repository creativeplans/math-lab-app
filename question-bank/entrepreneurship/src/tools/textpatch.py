"""Replace choice texts in the data files: python3 textpatch.py patch.json  (a JSON object {old text: new text}).
Each old text must appear exactly once across all data_*.py files (as a quoted string)."""
import glob, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def forms(t):
    return ["'%s'" % t.replace("'", "\\'"), '"%s"' % t]


def main(path):
    patch = json.load(open(path, encoding='utf-8'))
    files = {f: open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py')))}
    bad = []
    for old, new in patch.items():
        hits = [(f, q) for f, s in files.items() for q in forms(old) if s.count(q) == 1]
        if len(hits) != 1:
            bad.append((old, len(hits)))
            continue
        f, q = hits[0]
        rep = "'%s'" % new.replace("'", "\\'") if q.startswith("'") else '"%s"' % new
        files[f] = files[f].replace(q, rep)
    for f, s in files.items():
        open(f, 'w', encoding='utf-8').write(s)
    print('patched %d, failed %s' % (len(patch) - len(bad), bad))


if __name__ == '__main__':
    main(sys.argv[1])
