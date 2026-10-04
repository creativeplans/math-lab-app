"""Recompute the answers of arithmetic questions and compare them with the key.

    python3 question-bank/engine/autocheck.py grade5

Covers stems such as "Evaluate.\\n<expression>", "Multiply. / Divide. / Add. /
Subtract. / Find the value.", "Evaluate <expression> when x = 3", and true/false
number sentences "<expression> = <expression>" (also <, >). Questions it cannot
parse are skipped and counted. Exit status 1 if any checked answer disagrees.
"""
import os
import re
import sys
from fractions import Fraction

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
import build  # noqa: E402
import answers as A  # noqa: E402

SUP = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻', '0123456789-')


def to_py(expr, env=None):
    """Turn a displayed expression into a Python expression over Fractions, or None."""
    s = expr.strip().rstrip('.').replace('−', '-').replace('−', '-')
    s = s.replace('$', '').replace(',', '')
    s = re.sub(r'(\d)\{(\d+)/(\d+)\}', r'(\1+F(\2,\3))', s)          # mixed numbers
    s = re.sub(r'\{([^{}]+)/([^{}]+)\}', r'((\1)/(\2))', s)             # fractions
    s = s.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
    s = s.replace('×', '*').replace('÷', '/').replace('·', '*')
    s = re.sub(r'([0-9a-z)])([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)', lambda m: '%s**(%s)' % (m.group(1), m.group(2).translate(SUP)), s)
    s = re.sub(r'(\d+(?:\.\d+)?)', r'F("\1")', s)
    if env:
        for k in env:
            s = re.sub(r'(?<![A-Za-z"])%s(?![A-Za-z"])' % k, '(%s)' % env[k], s)
        s = re.sub(r'(\))\s*\(', r'\1*(', s)
        s = re.sub(r'(F\("[\d.]+"\))\s*\(', r'\1*(', s)
    s = re.sub(r'\)\s*\(', ')*(', s)
    if re.search(r'[A-Za-z]', s.replace('F(', '').replace('"', '')):
        return None
    if '□' in s or '_' in s or '?' in s:
        return None
    return s


def ev(expr, env=None):
    py = to_py(expr, env)
    if py is None:
        return None
    try:
        v = eval(py, {'F': Fraction})
        return Fraction(v)
    except Exception:
        return None


def parse_answer(text):
    """First number in an answer ('6 1/4', '5/2 = 2 1/2', '$17.50', '-3.5°F')."""
    t = text.replace('−', '-').replace(',', '').replace('$', '')
    t = t.split(' ## ')[0]
    m = re.match(r'\s*(-?\d+)\s+(\d+)/(\d+)', t)
    if m:
        w, n, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return w - Fraction(n, d) if w < 0 or t.strip().startswith('-') else w + Fraction(n, d)
    m = re.match(r'\s*(-?\d+(?:\.\d+)?)\s*/\s*(\d+)', t)
    if m:
        return Fraction(m.group(1)) / int(m.group(2))
    m = re.match(r'\s*(?:[a-z]\s*=\s*)?(-?\d+(?:\.\d+)?)', t)
    if m:
        return Fraction(m.group(1))
    return None


def check(q, raw, qid):
    """Return None if skipped, True if it agrees, or an error message."""
    t = A.qtype(q)
    stem = q['stem']
    a, _ = A.split_note(raw)
    lines = stem.split('\n')
    m = re.match(r'(Evaluate|Multiply|Divide|Add|Subtract|Find the value|Find the quotient|Find the product|'
                 r'Find the sum|Find the difference)\.$', lines[0])
    expr, env = None, None
    if m and len(lines) == 2:
        expr = lines[1]
    elif re.fullmatch(r'[^A-Za-z]+ = \?', lines[-1].strip()) and t == 'mc':
        expr = lines[-1]
    else:
        m = re.match(r'Evaluate (.+?) when (.+)\.$', stem)
        if m:
            expr = m.group(1)
            env = {}
            for part in re.split(r',? and |, ', m.group(2)):
                mm = re.match(r'\s*([a-z])\s*=\s*(.+)', part)
                if not mm:
                    return None
                v = ev(mm.group(2))
                if v is None:
                    return None
                env[mm.group(1)] = 'F(%d,%d)' % (v.numerator, v.denominator)
    if expr is not None:
        expr = re.sub(r'\s*=\s*\??$', '', expr)
        val = ev(expr, env)
        if val is None:
            return None
        text = A.plain(q['ch']['abcdefgh'.index(a)]) if t == 'mc' else a
        rem = re.match(r'\s*([\d,]+) R (\d+)\s*$', text.split(' ## ')[0])
        div = re.fullmatch(r'\s*([\d,]+) ÷ ([\d,]+)\s*(= \?)?\s*', expr)
        if rem and div:
            n, d = int(div.group(1).replace(',', '')), int(div.group(2).replace(',', ''))
            qq, r = int(rem.group(1).replace(',', '')), int(rem.group(2))
            ok = n == d * qq + r and 0 <= r < d
            return True if ok else '%s: %s is not %s' % (qid, expr, text)
        want = ev(text.split(' ## ')[0])
        if want is None:
            want = parse_answer(text)
        if want is None:
            return None
        return True if want == val else '%s: computed %s, key says %s' % (qid, float(val), a)
    if t == 'tf':
        for op in (' = ', ' < ', ' > '):
            if op in stem and stem.count(op) == 1 and '\n' not in stem:
                left, right = stem.rstrip('.').split(op)
                lv, rv = ev(left), ev(right)
                if lv is None or rv is None:
                    return None
                truth = {' = ': lv == rv, ' < ': lv < rv, ' > ': lv > rv}[op]
                want = a == 'T'
                return True if truth == want else '%s: "%s" is %s, key says %s' % (qid, stem, truth, a)
    return None


def run(name):
    build.load_grade(name)
    akey = A.load_key()
    ok = skipped = 0
    errors = []
    for st in build.all_sets():
        for key, nm, std, qs, nearest in build.sections(st):
            raws = akey.get('S%d-%s' % (st['num'], A.section_code(key)))
            for i, q in enumerate(qs, 1):
                qid = A.qid(st['num'], key, i)
                raw = raws[i - 1] if raws else A.inline_raw(q)
                r = check(q, raw, qid)
                if r is None:
                    skipped += 1
                elif r is True:
                    ok += 1
                else:
                    errors.append(r)
    print('%s: %d checked and agree, %d disagree, %d not arithmetic (skipped)' % (name, ok, len(errors), skipped))
    for e in errors:
        print('  ' + e)
    return errors


if __name__ == '__main__':
    sys.exit(1 if run(sys.argv[1] if len(sys.argv) > 1 else 'grade5') else 0)
