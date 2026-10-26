"""Locate and rewrite questions in the data files by question ID, using the Python syntax tree.

    python3 qedit.py show S36-F1-Q2 [S13-F2-Q3 ...]     print the source of those questions
    python3 qedit.py apply patch.py                    apply REPL = {ID: 'Q(...)' source} from patch.py

An ID is S<set>-<section>-Q<n> (section M, B1, B2, F1, F2). The position of each Q(...) call is found from the
SET(code, M=sec(...), B=[...], F1=..., F2=...) structure, so repeated prompts are never confused. A replacement must
be a complete Q(...) call; it is checked by importing the edited file before anything is written.
"""
import ast
import glob
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import plan  # noqa: E402


class _Offsets(list):
    """Line start offsets that also convert the parser's UTF-8 byte columns to character columns."""
    def at(self, ln, col):
        return self[ln - 1] + len(self.lines[ln - 1].encode('utf-8')[:col].decode('utf-8'))


def _offsets(text):
    starts, pos = _Offsets([0]), 0
    starts.lines = text.splitlines(keepends=True)
    for line in starts.lines:
        pos += len(line)
        starts.append(pos)
    return starts


def index():
    """Map question ID -> (file, start, end) of its Q(...) call."""
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py'))):
        text = open(f, encoding='utf-8').read()
        offs = _offsets(text)
        pos = lambda n, ln, col: offs.at(ln, col)  # noqa: E731
        for node in ast.walk(ast.parse(text)):
            if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'SET'):
                continue
            code = node.args[0].value
            n = plan.SET_NUM[code]
            kw = {k.arg: k.value for k in node.keywords}
            secs = [('M', kw['M'])] + [('B%d' % i, b) for i, b in enumerate(kw['B'].elts, 1)] + \
                   [('F1', kw['F1']), ('F2', kw['F2'])]
            for sc, call in secs:
                qs = call.args[2].elts
                for i, q in enumerate(qs, 1):
                    out['S%d-%s-Q%d' % (n, sc, i)] = (f, pos(0, q.lineno, q.col_offset), pos(0, q.end_lineno, q.end_col_offset))
    return out


def show(ids):
    idx = index()
    for i in ids:
        f, a, b = idx[i]
        print('#', i, os.path.basename(f))
        print(open(f, encoding='utf-8').read()[a:b])
        print()


def apply(patch_path):
    ns = {}
    exec(open(patch_path, encoding='utf-8').read(), ns)
    repl = dict(ns.get('REPL', {}))
    text_edits(ns.get('CONST', {}), ns.get('INTRO', {}))
    repl.update(edit(ns.get('EDIT', {})))
    idx = index()
    by_file = {}
    for qid, src in repl.items():
        f, a, b = idx[qid]
        by_file.setdefault(f, []).append((a, b, src.strip()))
    for f, edits in by_file.items():
        text = open(f, encoding='utf-8').read()
        for a, b, src in sorted(edits, reverse=True):
            text = text[:a] + src + text[b:]
        compile(text, f, 'exec')
        open(f, 'w', encoding='utf-8').write(text)
    print('replaced %d questions in %d files' % (len(repl), len(by_file)))



def intros(sets):
    """Print the teaching-passage source (second sec() argument) of each section of the given set numbers."""
    for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py'))):
        text = open(f, encoding='utf-8').read()
        offs = _offsets(text)
        for node in ast.walk(ast.parse(text)):
            if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'SET'):
                continue
            n = plan.SET_NUM[node.args[0].value]
            if str(n) not in sets:
                continue
            kw = {k.arg: k.value for k in node.keywords}
            secs = [('M', kw['M'])] + [('B%d' % i, b) for i, b in enumerate(kw['B'].elts, 1)] + \
                   [('F1', kw['F1']), ('F2', kw['F2'])]
            for sc, call in secs:
                a = call.args[1]
                print('# S%d-%s intro (%s line %d)' % (n, sc, os.path.basename(f), a.lineno))
                print(text[offs.at(a.lineno, a.col_offset):offs.at(a.end_lineno, a.end_col_offset)])


def _fields(src):
    """Parse a Q(...) call into editable fields; calc is kept as source text."""
    call = ast.parse(src.strip(), mode='eval').body
    lit = [ast.literal_eval(a) for a in call.args]
    f = dict(prompt=lit[0], correct=lit[1], w=[list(x) for x in lit[2:5]], fb=lit[5] if len(lit) > 5 else None)
    for k in call.keywords:
        f[k.arg] = ast.get_source_segment(src.strip(), k.value) if k.arg in ('calc', 'ex') else ast.literal_eval(k.value)
    return f


def _render(f):
    out = 'Q(%r,\n          %r,\n          %r, %r,\n          %r,\n          %r' % (
        f['prompt'], f['correct'], tuple(f['w'][0]), tuple(f['w'][1]), tuple(f['w'][2]), f['fb'])
    if f.get('calc'):
        out += ',\n          calc=%s' % f['calc']
    if f.get('ex'):
        out += ',\n          ex=%s' % f['ex']
    if f.get('intro') is not None:
        out += ',\n          intro=%r' % f['intro']
    return out + ')'


def edit(spec):
    """spec: {ID: {field: value}}; fields prompt, correct, fb, calc, w1/w2/w3 ((text, why)), sub [(old, new)]."""
    idx = index()
    repl = {}
    for qid, ch in spec.items():
        f0, a, b = idx[qid]
        f = _fields(open(f0, encoding='utf-8').read()[a:b])
        for old, new in ch.get('sub', []):
            hit = False
            for k in ('prompt', 'correct', 'fb'):
                if old in f[k]:
                    f[k] = f[k].replace(old, new); hit = True
            for w in f['w']:
                for i in (0, 1):
                    if old in w[i]:
                        w[i] = w[i].replace(old, new); hit = True
            assert hit, (qid, old)
        for k in ('prompt', 'correct', 'fb', 'calc', 'ex'):
            if k in ch:
                f[k] = ch[k]
        for i in (1, 2, 3):
            if 'w%d' % i in ch:
                f['w'][i - 1] = list(ch['w%d' % i])
        repl[qid] = _render(f)
    return repl


def _wrap(s, indent):
    """Render a long string as implicitly concatenated literals of about 110 characters."""
    import textwrap
    parts = textwrap.wrap(s, 108, drop_whitespace=False, break_long_words=False)
    return ('(' + ('\n' + ' ' * indent).join(repr(x) for x in parts) + ')') if len(parts) > 1 else repr(s)


def _apply_subs(val, subs, label):
    for old, new in subs:
        assert val.count(old) == 1, (label, old, val.count(old))
        val = val.replace(old, new)
    return val


def text_edits(consts, intros):
    """consts: {(module, NAME): [(old, new)]}; intros: {'S<n>-<sec>': [(old, new)]} for literal passages."""
    for (mod, name), subs in consts.items():
        f = os.path.join(HERE, mod + '.py')
        text = open(f, encoding='utf-8').read()
        offs = _offsets(text)
        for node in ast.parse(text).body:
            if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', None) == name:
                v = node.value
                a, b = offs.at(v.lineno, v.col_offset), offs.at(v.end_lineno, v.end_col_offset)
                new = _apply_subs(ast.literal_eval(v), subs, name)
                text = text[:a] + _wrap(new, len(name) + 4) + text[b:]
                break
        else:
            raise KeyError(name)
        compile(text, f, 'exec')
        open(f, 'w', encoding='utf-8').write(text)
    for key, subs in intros.items():
        n, sc = key[1:].split('-')
        done = False
        for f in sorted(glob.glob(os.path.join(HERE, 'data_*.py'))):
            text = open(f, encoding='utf-8').read()
            offs = _offsets(text)
            for node in ast.walk(ast.parse(text)):
                if not (isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'SET'):
                    continue
                if str(plan.SET_NUM[node.args[0].value]) != n:
                    continue
                kw = {k.arg: k.value for k in node.keywords}
                secs = dict([('M', kw['M'])] + [('B%d' % i, b) for i, b in enumerate(kw['B'].elts, 1)] +
                            [('F1', kw['F1']), ('F2', kw['F2'])])
                v = secs[sc].args[1]
                a, b = offs.at(v.lineno, v.col_offset), offs.at(v.end_lineno, v.end_col_offset)
                new = _apply_subs(ast.literal_eval(v), subs, key)
                text = text[:a] + _wrap(new, v.col_offset) + text[b:]
                compile(text, f, 'exec')
                open(f, 'w', encoding='utf-8').write(text)
                done = True
                break
            if done:
                break
        assert done, key


if __name__ == '__main__':
    if sys.argv[1] == 'show':
        show(sys.argv[2:])
    elif sys.argv[1] == 'intros':
        intros(sys.argv[2:])
    else:
        apply(sys.argv[2])
