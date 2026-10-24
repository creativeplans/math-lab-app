"""Independent re-solve of computable Algebra II answers.

Each case recomputes an answer from the givens in the question text with sympy or plain arithmetic, written separately from
the data modules (no shared helpers, no key strings reused). The key text is parsed into fragments (split at ';', ',', '=',
'or', 'and', '±'); a case passes when some fragment equals the recomputed value:
  E  expression  - equal as a function (checked symbolically and at sample points)
  N  number      - equal to the stated number of decimals (or exactly, for decimals=None)
  S  set         - every listed value appears as a fragment
  T  text        - the given string appears verbatim (for answers such as intervals)

    python3 question-bank/algebra2/src/resolve.py      (prints a summary; exit 1 on any disagreement)
"""
import json
import math
import os
import re
import sys

import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application,
                                        convert_xor)

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(os.path.dirname(HERE), 'Algebra2_Answer_Key.json')

x, y, t, a, b, n, u, d, p, h, L, W, r, v, g, f_, w, m, c, k = sp.symbols('x y t a b n u d p h L W r v g f w m c k', real=True)
I, pi, E_ = sp.I, sp.pi, sp.E
TR = standard_transformations + (implicit_multiplication_application, convert_xor)
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9',
       'ˣ': 'x', 'ᵗ': 't', 'ⁿ': 'n'}
SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5'}
LOCAL = {'i': I, 'pi': pi, 'e': E_, 'sqrt': sp.sqrt, 'cbrt': lambda z: sp.root(z, 3), 'ln': sp.log,
         'log10': lambda z: sp.log(z, 10), 'log2': lambda z: sp.log(z, 2), 'log3': lambda z: sp.log(z, 3),
         'log5': lambda z: sp.log(z, 5), 'log4': lambda z: sp.log(z, 4), 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
         'root4': lambda z: sp.root(z, 4)}
for s_ in 'xytabnudphLWrvgfwmck':
    LOCAL[s_] = sp.Symbol(s_, real=True)


def to_py(s):
    s = s.replace('−', '-').replace('·', '*').replace('×', '*').replace('π', ' pi ').replace('°', '')
    s = re.sub(r'(?<=[0-9A-Za-z)])\s*(?=[√∛])', '*', s)          # 3i√2 → 3i*√2, i√7 → i*√7
    s = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹ˣᵗⁿ]+)', lambda m_: '**(' + ''.join(SUP[ch] for ch in m_.group(1)) + ')', s)
    s = re.sub(r'log([₀₁₂₃₄₅])', lambda m_: 'log' + SUB[m_.group(1)], s)
    s = re.sub(r'\blog\b', 'log10', s)
    s = s.replace('⁴√', 'root4').replace('∛', 'cbrt').replace('√', 'sqrt')
    s = re.sub(r'(sqrt|cbrt|root4)([A-Za-z0-9.]+)', r'\1(\2)', s)   # √5 → sqrt(5), √x → sqrt(x)
    s = s.replace('^', '**')
    s = re.sub(r'\b(log10|log2|log3|log4|log5|ln|sin|cos|tan)\s+([0-9.]+|[a-z]\b)', r'\1(\2)', s)   # log 8 → log10(8)
    return s


def parse(s):
    s = to_py(s.strip().rstrip('.'))
    return parse_expr(s, local_dict=LOCAL, transformations=TR, evaluate=True)


def fragments(key):
    out = []
    parts = re.split(r';|,(?![^()]*\))|=|\bor\b|\band\b|≈|:|\bto\b', key)
    for q in parts:
        q = re.sub(r'\((?:that is|exactly|about|any|for example)[^)]*\)', '', q)
        q = q.strip().strip('$').replace('$', '')
        if not q:
            continue
        if '±' in q:
            lhs, rhs = q.split('±', 1)
            out += [lhs + '+' + rhs, lhs + '-' + rhs]
        else:
            out.append(q)
    return out


def clean(key):
    key = key.replace('$', '').replace('≠', '=').replace('≥', '=').replace('≤', '=').replace('<', '=').replace('>', '=')
    return re.sub(r'(?<=\d),(?=\d{3}\b)', '', key)


def value_frags(key):
    """Every parseable run of words inside every fragment of the key."""
    vals = []
    for q in fragments(clean(key)):
        toks = q.split()
        for i in range(len(toks)):
            for j in range(i + 1, len(toks) + 1):
                piece = ' '.join(toks[i:j])
                if piece.count('(') != piece.count(')'):
                    continue
                try:
                    v_ = parse(piece)
                except Exception:  # noqa: BLE001  (words, not math)
                    continue
                if isinstance(v_, sp.Basic):
                    vals.append(v_)
    return vals


def numbers(key):
    out = []
    for m_ in re.finditer(r'-?\d+(?:\.\d+)?(?:/\d+(?:\.\d+)?)?', clean(key).replace('−', '-')):
        try:
            out.append(float(sp.Rational(m_.group(0)) if '/' in m_.group(0) else float(m_.group(0))))
        except Exception:  # noqa: BLE001
            pass
    return out


def same_expr(e1, e2):
    try:
        if sp.simplify(sp.expand(e1 - e2)) == 0:
            return True
    except Exception:  # noqa: BLE001
        pass
    syms = sorted((e1 - e2).free_symbols, key=str)
    if not syms:
        try:
            return abs(complex(sp.N(e1 - e2))) < 1e-9
        except Exception:  # noqa: BLE001
            return False
    for trial in (0.37, 1.73, 2.9):
        sub = {s_: trial + 0.11 * i for i, s_ in enumerate(syms)}
        try:
            if abs(complex(sp.N((e1 - e2).subs(sub)))) > 1e-7:
                return False
        except Exception:  # noqa: BLE001
            return False
    return True


def check(rec, kind, want, dec=None):
    key = rec['correct_answer'] or ''
    if kind == 'T':
        return want in key
    vals = value_frags(key)
    if kind == 'E':
        return any(same_expr(v_, want) for v_ in vals)
    if kind == 'N':
        for z in numbers(key):
            if dec is None and abs(z - float(want)) < 1e-9:
                return True
            if dec is not None and round(z, dec) == round(float(want), dec):
                return True
        for v_ in vals:
            try:
                z = complex(sp.N(v_))
            except Exception:  # noqa: BLE001
                continue
            if abs(z.imag) > 1e-9:
                continue
            if dec is None and abs(z.real - float(want)) < 1e-9:
                return True
            if dec is not None and round(z.real, dec) == round(float(want), dec):
                return True
        return False
    if kind == 'S':
        return all(check(rec, 'E' if isinstance(w_, sp.Basic) and w_.free_symbols else 'N', w_, dec) for w_ in want)
    raise ValueError(kind)


X = x
CASES = [
    # ---------------------------------------------------------------- N-CN
    ('S1-M-Q1', 'E', sp.sqrt(-49)), ('S1-M-Q2', 'E', sp.sqrt(-18)), ('S1-M-Q4', 'E', (-4 + sp.sqrt(-75)) / 2),
    ('S1-M-Q5', 'E', (10 + sp.sqrt(-64)) / 4), ('S1-M-Q3', 'E', 6 - sp.sqrt(-20)),
    ('S2-M-Q1', 'E', (3 + 5 * I) + (-7 + 2 * I)), ('S2-M-Q2', 'E', (6 - 4 * I) - (-2 + 9 * I)),
    ('S2-M-Q3', 'E', (-1 + sp.sqrt(-16)) + (5 - sp.sqrt(-9))), ('S2-M-Q4', 'E', sp.Rational(5, 2) - I - (sp.Rational(-3, 2) + 3 * I) + 4 * I),
    ('S2-M-Q5', 'E', (-2 + 3 * I) - (4 - 7 * I)), ('S2-F2-Q5', 'E', ((6 - 2 * I) + (-2 + 4 * I)) / 2), ('S2-F2-Q4', 'N', abs((5 + 2 * I) - (1 - I))),
    ('S3-M-Q1', 'E', sp.expand((3 + 2 * I) * (4 - 5 * I))), ('S3-M-Q2', 'E', sp.expand((-2 + I) ** 2)), ('S3-M-Q3', 'E', sp.expand((5 - 3 * I) * (5 + 3 * I))),
    ('S3-M-Q4', 'E', sp.expand((1 + I) ** 3)), ('S3-M-Q5', 'E', sp.expand(I ** 23 * (4 - I))),
    ('S3-F2-Q1', 'E', sp.simplify((3 + 4 * I) / (1 + 2 * I))), ('S3-F2-Q2', 'E', sp.simplify(10 / (3 - I))),
    ('S4-M-Q1', 'S', sp.solve(X ** 2 + 49, X)), ('S4-M-Q2', 'S', sp.solve(X ** 2 - 4 * X + 13)), ('S4-M-Q3', 'S', sp.solve(2 * X ** 2 + 2 * X + 5)),
    ('S4-M-Q4', 'S', sp.solve((X + 3) ** 2 + 20)), ('S4-M-Q5', 'S', sp.solve(3 * X ** 2 - 6 * X + 7)),
    ('S4-B1-Q1', 'N', 16 - 52), ('S4-B1-Q2', 'N', 4 - 40),
    ('S5-M-Q1', 'E', X ** 2 + 25), ('S5-M-Q2', 'E', X ** 2 + 7), ('S5-M-Q3', 'E', 4 * X ** 2 + 9), ('S5-M-Q4', 'E', X ** 4 - 16), ('S5-M-Q5', 'E', X ** 2 - 6 * X + 13),
    ('S5-F1-Q1', 'E', X ** 3 + 8), ('S5-F1-Q3', 'E', X ** 4 + 5 * X ** 2 + 4), ('S5-F2-Q1', 'E', sp.expand((X ** 2 + 4) * (X ** 2 - 2 * X + 2))),
    ('S6-M-Q4', 'S', sp.solve(X ** 4 - 81)),
    # ---------------------------------------------------------------- A-SSE
    ('S9-M-Q1', 'E', X ** 4 - 81), ('S9-M-Q2', 'E', 8 * X ** 3 + 27), ('S9-M-Q3', 'E', X ** 6 - 64), ('S9-M-Q4', 'E', 16 * X ** 4 - y ** 4),
    ('S9-M-Q5', 'E', 2 * X ** 5 - 32 * X), ('S9-F1-Q2', 'E', (2 * X - 1) ** 3 + 8), ('S9-F1-Q5', 'E', X ** 2 * (X + 2) - 4 * (X + 2)),
    ('S10-M-Q1', 'E', X ** 4 - 5 * X ** 2 + 4), ('S10-M-Q2', 'E', X ** 4 + 3 * X ** 2 - 10), ('S10-M-Q4', 'E', X ** 6 - 9 * X ** 3 + 8),
    ('S10-M-Q5', 'E', 2 * X ** 4 - 7 * X ** 2 - 4), ('S10-F1-Q5', 'S', sp.solve(X ** 4 + X ** 2 - 12)),
    ('S10-F2-Q2', 'S', [1, 2]), ('S10-F2-Q5', 'N', math.log(5), 3),
    ('S11-M-Q2', 'N', sum(3 * 2 ** j for j in range(10))), ('S11-M-Q5', 'N', 100 * (1.05 ** 20 - 1) / 0.05, 2),
    ('S11-F1-Q2', 'N', sum(3 ** j for j in range(6))), ('S11-F2-Q1', 'S', [16 * (1 - 0.5 ** 5), 16 * (1 - 0.5 ** 10)], 4),
    ('S12-M-Q1', 'N', 5 * (3 ** 12 - 1) // 2), ('S12-M-Q2', 'N', 250 * (1.005 ** 36 - 1) / 0.005, 2),
    ('S12-M-Q3', 'N', 180000 * 0.004 / (1 - 1.004 ** -360), 2), ('S12-M-Q4', 'N', 10 + 2 * 6 * (1 - 0.6 ** 5) / 0.4, 2),
    ('S12-F2-Q1', 'T', '33,382.38'), ('S12-F2-Q4', 'T', '$28,320'),
    # ---------------------------------------------------------------- A-APR
    ('S13-M-Q1', 'E', (4 * X ** 3 - 2 * X ** 2 + 7) + (-X ** 3 + 5 * X - 9)), ('S13-M-Q2', 'E', (6 * X ** 4 - X ** 3 + 2 * X) - (2 * X ** 4 + 3 * X ** 3 - X ** 2 + 2 * X - 1)),
    ('S13-M-Q3', 'E', sp.nsimplify(-0.01 * X ** 3 + 3 * X ** 2 + 40 * X - (0.02 * X ** 2 + 15 * X + 900))),
    ('S13-M-Q4', 'E', (X ** 5 - 3 * X ** 3 + X) - (X ** 5 + 2 * X ** 4 - 3 * X ** 3 - 7)), ('S13-M-Q5', 'E', (2 * X ** 3 - X + 4) - (5 * X ** 3 + X ** 2 - 6)),
    ('S13-F2-Q1', 'E', sp.expand(3 * (X + 1) + 2 * X)), ('S13-F2-Q2', 'N', sp.expand((X + 2) - (X - 2))),  # numerators over the stated denominators
    ('S14-M-Q1', 'E', sp.expand((X ** 2 + 3 * X - 2) * (2 * X - 5))), ('S14-M-Q2', 'E', sp.expand((X - 2) ** 3)), ('S14-M-Q3', 'E', sp.expand((X ** 2 - X + 1) * (X ** 2 + X + 1))),
    ('S14-M-Q4', 'E', sp.expand((2 * X + 1) * (X - 3) * (X + 4))), ('S14-M-Q5', 'E', sp.expand((X + 2) * (X - 1) * (2 * X + 3))),
    ('S14-F1-Q1', 'N', sp.Poly(sp.expand((X ** 2 + 3 * X - 2) * (4 * X ** 2 - X + 5)), X).coeff_monomial(X ** 2)),
    ('S14-F1-Q5', 'N', sp.Poly(sp.expand((X - 1) * (X - 2) * (X - 3)), X).coeff_monomial(X)), ('S14-F2-Q2', 'E', sp.expand((X - 2) ** 4)),
    ('S15-M-Q1', 'N', 27 - 36 + 6 - 5), ('S15-M-Q2', 'N', (2 * X ** 4 + X ** 3 - 3 * X + 7).subs(X, -2)), ('S15-M-Q3', 'N', 4),
    ('S15-M-Q4', 'N', (4 * X ** 3 - 6 * X ** 2 + X - 1).subs(X, sp.Rational(1, 2))), ('S15-M-Q5', 'N', (X ** 4 - 5 * X ** 2 + 4 * X).subs(X, 2)),
    ('S15-F1-Q1', 'N', sp.solve((X ** 3 + k * X ** 2 - 4).subs(X, 2) - 12, k)[0]), ('S15-F1-Q5', 'N', sp.solve((X ** 4 - k * X + 6).subs(X, -2), k)[0]),
    ('S16-M-Q1', 'E', X ** 3 - 3 * X ** 2 - 4 * X + 12), ('S16-M-Q2', 'E', X ** 3 + 2 * X ** 2 - 5 * X - 6), ('S16-M-Q3', 'E', 2 * X ** 3 + 5 * X ** 2 - 4 * X - 3),
    ('S16-M-Q4', 'N', (X ** 3 - 5 * X ** 2 + 2 * X + 9).subs(X, 4)), ('S16-M-Q5', 'S', sp.solve(X ** 3 - 7 * X + 6, X)),
    ('S16-F1-Q1', 'N', sp.solve((X ** 3 + k * X ** 2 - 3 * X + 9).subs(X, 3), k)[0]), ('S16-F1-Q5', 'E', sp.expand((X - 1) * (X + 1) * (X - 4))),
    ('S16-F2-Q2', 'E', X ** 3 + 2 * X ** 2 + 9 * X + 18),
    ('S17-F1-Q1', 'E', 2 * (X + 1) * (X - 2) * (X - 4)), ('S17-F1-Q5', 'E', 2 * X ** 2 * (X - 5)), ('S18-F2-Q1', 'E', (X + 3) * (X - 2) ** 2),
    ('S18-F2-Q2', 'E', 2 * (X + 1) ** 2 * (X - 3) ** 2), ('S18-F2-Q5', 'E', 2 * (X + 2) * (X - 1) ** 2),
    ('S20-M-Q3', 'N', 47 * 53), ('S20-M-Q5', 'N', 13 ** 3 - 12 ** 3), ('S20-B3-Q5', 'N', 98 * 102), ('S20-F2-Q1', 'E', sp.expand((3 + 2 * I) ** 2)),
    ('S21-M-Q1', 'E', sp.expand((X + 2) ** 5)), ('S21-M-Q2', 'E', sp.expand((2 * a - b) ** 4)), ('S21-M-Q3', 'N', sp.binomial(7, 3) * 3 ** 4),
    ('S21-M-Q4', 'E', sp.Poly(sp.expand((X - 2 * y) ** 6), X, y).coeff_monomial(X ** 3 * y ** 3) * X ** 3 * y ** 3),
    ('S21-F1-Q1', 'N', sp.binomial(6, 3)), ('S21-F1-Q5', 'N', sp.Poly(sp.expand((2 * X - 1) ** 6), X).coeff_monomial(X)),
    ('S21-F2-Q2', 'N', sp.binomial(4, 2) * 0.3 ** 2 * 0.7 ** 2, 4),
    ('S22-M-Q1', 'E', (X ** 3 + 2 * X ** 2 - 5 * X + 3) / (X - 1)), ('S22-M-Q2', 'E', (2 * X ** 3 - 3 * X ** 2 + 4 * X - 7) / (X ** 2 + 1)),
    ('S22-M-Q3', 'E', sp.cancel((X ** 4 - 16) / (X - 2))), ('S22-M-Q4', 'E', (6 * X ** 2 + X - 4) / (2 * X + 1)), ('S22-M-Q5', 'E', (X ** 3 - 4 * X + 5) / (X + 3)),
    ('S22-F1-Q5', 'E', sp.expand((X - 2) * (X ** 2 + 1) + 3)), ('S22-F2-Q1', 'E', sp.div(X ** 2 + 3 * X + 1, X + 1)[0] + y - y),
    ('S23-M-Q1', 'E', (X + 5) / (X + 2)), ('S23-M-Q2', 'E', (2 * X - 1) / (X - 3)), ('S23-M-Q3', 'E', (X ** 2 + 1) / X), ('S23-M-Q4', 'E', (3 * X + 7) / (X + 1)),
    ('S23-M-Q5', 'E', X ** 2 / (X - 1)),
    ('S24-M-Q2', 'E', sp.cancel((X + 2) / (3 * X ** 2) / ((X ** 2 - 4) / X))), ('S24-M-Q3', 'E', sp.cancel((2 * X - 6) / (X + 1) * (X + 1) / (X ** 2 - 9))),
    ('S24-M-Q5', 'E', sp.cancel((5 * X ** 2 + 5 * X) / (X ** 2 - 4) / ((X + 1) / (X - 2)))), ('S24-F1-Q1', 'E', sp.cancel((1 / X + 1) / (1 / X - 1))),
    ('S24-F1-Q2', 'E', sp.cancel((1 - 4 / X ** 2) / (1 + 2 / X))), ('S24-F1-Q5', 'E', sp.cancel((X - 1 / X) / (X + 1))),
    ('S25-M-Q1', 'E', sp.cancel((X + 1) / (X ** 2 + X) + 1 / X)), ('S25-M-Q2', 'E', sp.expand(2 * (X - 2) + 3 * (X + 1))), ('S25-M-Q4', 'E', sp.expand(1 - (X + 1))),
    ('S25-M-Q5', 'E', sp.expand(4 - (X - 4))), ('S25-F1-Q5', 'N', sum(sp.Rational(1, j * (j + 1)) for j in range(1, 5))),
    ('S25-F2-Q1', 'N', sp.solve(2 / (X + 1) + 3 / (X - 2), X)[0]), ('S25-F2-Q5', 'N', sp.solve(4 / (X ** 2 - 4 * X) - 1 / X, X)[0]),
    # ---------------------------------------------------------------- A-CED, A-REI
    ('S26-M-Q1', 'N', sp.solve(sp.Rational(1, 4) + 1 / b - 1 / sp.Rational(12, 5), b)[0]), ('S26-M-Q2', 'N', 45 ** 2 / 22.5),
    ('S26-M-Q3', 'N', 5 * math.log2(9600 / 1200)), ('S26-M-Q4', 'N', 100), ('S26-M-Q5', 'N', 2 / 0.08 - 10),
    ('S26-F1-Q1', 'N', max(sp.solve(24 / (b + 2) + 24 / (b - 2) - 5, b))), ('S26-F1-Q2', 'N', max(sp.solve(w ** 2 + (w + 3) ** 2 - 225, w))),
    ('S26-F1-Q5', 'N', max(sp.solve(1 / X + 1 / (X + 2) - sp.Rational(5, 12), X))), ('S26-F2-Q1', 'N', 5 * math.log2(5000 / 1200), 1),
    ('S26-F2-Q2', 'N', math.log(1.6) / math.log(1.04), 2), ('S27-M-Q5', 'N', math.ceil(math.log(1.6) / math.log(1.04))),
    ('S29-F1-Q2', 'S', [sp.Integer(25), sp.Integer(25 * (500 - 10 * 25))]), ('S30-F2-Q5', 'N', math.log(2) / math.log(1.05), 2),
    ('S31-M-Q1', 'N', sp.solve(3 * (X + 2) - 6 * (X - 1), X)[0]), ('S31-M-Q3', 'S', sp.solve(1 / X + 1 / (X + 2) - sp.Rational(4, 3), X)),
    ('S31-M-Q4', 'N', -3), ('S31-M-Q5', 'N', sp.solve(2 / (X + 1) - 1 / (X - 1) - 2 / (X ** 2 - 1), X)[0]),
    ('S31-F2-Q5', 'N', (1 + 5 ** 0.5) / 2, 2),
    ('S32-M-Q1', 'S', [s_ for s_ in sp.solve(X + 7 - (X - 5) ** 2, X) if s_ - 5 >= 0]), ('S32-M-Q2', 'N', 5),
    ('S32-M-Q3', 'S', [s_ for s_ in sp.solve(X + 3 - (X - 3) ** 2, X) if s_ - 3 >= 0]), ('S32-M-Q4', 'N', 2 - 27),
    ('S32-F1-Q1', 'N', sp.solve(sp.sqrt(X + 5) - sp.sqrt(X) - 1, X)[0]), ('S32-F1-Q2', 'N', 4),
    ('S34-M-Q1', 'N', 1.7156, 2), ('S34-M-Q2', 'N', 1.7392, 2), ('S34-M-Q3', 'N', 1.7556, 2), ('S34-M-Q5', 'N', -1.690, 1),
    ('S34-F2-Q1', 'N', math.log2(5), 2), ('S34-F2-Q2', 'N', math.log(1 / 3) / math.log(0.8), 2),
    # ---------------------------------------------------------------- F-TF
    ('S35-M-Q2', 'E', sp.Rational(150, 180) * pi), ('S35-M-Q3', 'N', sp.Rational(7, 4) * 180), ('S35-M-Q4', 'E', 6 * 2 * pi / 3), ('S35-F1-Q5', 'N', 10 - 2 * math.pi, 2),
    ('S36-M-Q1', 'E', sp.sin(5 * pi / 6)), ('S36-M-Q2', 'E', sp.cos(4 * pi / 3)), ('S36-M-Q3', 'E', sp.tan(7 * pi / 4)), ('S36-M-Q4', 'E', sp.sin(-pi / 2)),
    ('S36-M-Q5', 'E', sp.cos(11 * pi / 6)), ('S36-F1-Q1', 'E', sp.sin(13 * pi / 6)), ('S36-F1-Q2', 'E', sp.cos(-3 * pi / 4)),
    ('S38-F2-Q1', 'N', sp.Rational(4, 3)), ('S39-M-Q3', 'N', 60 / (2 / 2.5)),
    ('S40-F2-Q1', 'E', sp.sin(sp.Rational(75, 180) * pi)),
    ('S41-M-Q1', 'S', [sp.Rational(-4, 5), sp.Rational(-3, 4)]), ('S41-M-Q2', 'S', [sp.Rational(-12, 13), sp.Rational(12, 5)]),
    ('S41-M-Q3', 'S', [-2 / sp.sqrt(5), 1 / sp.sqrt(5)]), ('S41-M-Q4', 'S', [2 * sp.sqrt(2) / 3, -1 / (2 * sp.sqrt(2))]), ('S41-M-Q5', 'S', [-0.8, sp.Rational(-4, 3)]),
    ('S41-F1-Q2', 'N', sp.Rational(60, 169)), ('S41-F1-Q5', 'E', -1 / sp.sqrt(10)),
    ('S41-F2-Q1', 'S', [math.asin(0.6), math.pi - math.asin(0.6)], 3), ('S41-F2-Q2', 'N', 2 * math.pi - math.acos(-5 / 13), 2),
    # ---------------------------------------------------------------- F-IF
    ('S43-F1-Q1', 'N', 15 - 8 * math.cos(math.pi * 100 / 12)), ('S45-M-Q1', 'N', (200 * 8 - 200 * 2) / 2), ('S45-M-Q2', 'N', (64 - 16 * 2.25) - (64 - 16 * 0.25)),
    ('S45-M-Q3', 'N', (10440.06 - 14450) / 2, 2), ('S45-M-Q4', 'N', sp.Rational(48 - 24, 96 - 24)), ('S45-M-Q5', 'N', sp.Rational(15 - 7, 6)),
    ('S48-F2-Q2', 'S', [(9 - 21 ** 0.5) / 2, (9 + 21 ** 0.5) / 2], 2),
    ('S50-F1-Q5', 'N', 1 + sp.Rational(1, 4)), ('S50-F2-Q1', 'N', math.log2(12), 2), ('S50-F2-Q2', 'N', math.log10(8), 3),
    ('S52-M-Q1', 'N', 1.08 ** (1 / 12), 6), ('S52-M-Q2', 'N', 0.97 ** 10, 4), ('S52-M-Q3', 'N', 2 ** (1 / 3), 4), ('S52-M-Q4', 'N', 1.005 ** 12, 6),
    ('S52-M-Q5', 'N', 0.5 ** 0.1, 6), ('S52-F2-Q1', 'N', math.log(2) / math.log(1.08), 2), ('S52-F2-Q2', 'N', math.log(0.5) / math.log(0.97), 2),
    ('S53-M-Q1', 'N', 3 * 1.1 ** 20, 2), ('S53-F1-Q1', 'N', next(j for j in range(1, 200) if 3 * 1.1 ** j > 10 + 5 * j)),
    # ---------------------------------------------------------------- F-BF, F-LE
    ('S54-M-Q1', 'E', sp.nsimplify(X * (50 - 0.5 * X) - (200 + 10 * X))), ('S54-M-Q3', 'N', (6000 + 1000) / (5000 * 1.02 ** 10), 2),
    ('S54-M-Q5', 'N', 20 + 70 * 0.95 ** 10, 2), ('S54-F2-Q1', 'E', sp.Rational(4, 3) * pi * (2 * t) ** 3),
    ('S58-M-Q1', 'S', [sp.Integer(2), sp.Integer(1)]),  # (x - 1)³ + 2 = y gives x = ∛(y - 2) + 1 ('S58-M-Q2', 'E', 3 * X / (X - 2)), ('S58-M-Q3', 'E', X ** 2 - 4), ('S58-M-Q4', 'E', sp.log(X / 5, 2)), ('S58-M-Q5', 'E', 3 ** X + 1),
    ('S59-M-Q1', 'N', sp.Rational(4, 5)), ('S59-M-Q2', 'E', sp.log(sp.Rational(9, 2), 10) / 3), ('S59-M-Q3', 'E', sp.log(6) / 2),
    ('S59-M-Q4', 'E', sp.log(3) / sp.log(sp.Rational(21, 20))), ('S59-M-Q5', 'E', 2 * sp.log(5, 3)),
    ('S59-F1-Q1', 'N', float(sp.log(3) / (sp.log(3) - sp.log(2))), 3), ('S59-F1-Q5', 'N', float(sp.log(sp.Rational(3, 2)) / sp.log(sp.Rational(5, 4))), 3),
    ('S59-F2-Q1', 'N', 2 ** 5 - 3), ('S59-F2-Q5', 'E', sp.E ** 3 / 2),
    ('S60-M-Q1', 'N', math.log(1.6) / math.log(1.035), 2), ('S60-M-Q2', 'N', 5730 * math.log(30 / 80) / math.log(0.5), 0),
    ('S60-M-Q3', 'N', math.log(3 / 7) / math.log(0.95), 2), ('S60-M-Q4', 'N', math.log(1.25) / 0.015, 2),
    ('S60-F1-Q1', 'N', math.log(1.6) / math.log(1.05), 2), ('S60-F1-Q2', 'N', math.log(2) / math.log(1.06), 2),
    ('S60-F2-Q1', 'N', math.log(2) / math.log(1.035), 2), ('S60-F2-Q2', 'N', math.log(0.5) / math.log(0.8), 2),
    # ---------------------------------------------------------------- statistics
    ('S61-M-Q3', 'N', 34 + 34 + 13.5, 1), ('S61-M-Q4', 'N', 93.32, 2), ('S61-M-Q5', 'N', (0.9332 - 0.1587) * 100, 2), ('S61-F1-Q5', 'N', 6.68, 2),
    ('S67-M-Q2', 'S', [0.4 - 0.055, 0.4 + 0.055], 3), ('S67-F1-Q2', 'N', 4 * 0.25 / 0.05 ** 2), ('S68-M-Q2', 'S', [152 - 7.2, 152 + 7.2], 1),
    ('S68-M-Q3', 'S', [24.5 - 2.8, 24.5 + 2.8], 1),
    ('S72-M-Q1', 'N', 95 / (95 + 0.05 * 9900), 3), ('S72-F1-Q1', 'N', 950 / (950 + 0.05 * 9000), 3), ('S72-F1-Q5', 'N', next(j for j in range(1, 20) if 0.9 ** j < 0.5)),
    ('S72-F2-Q2', 'N', 400 / 500 - 2, 2),
    # ---------------------------------------------------------------- advanced extension
    ('S73-M-Q2', 'E', sp.simplify((2 + 3 * I) / (1 - I))), ('S73-M-Q3', 'E', sp.simplify((5 + I) / (2 + 3 * I))), ('S73-M-Q5', 'E', sp.simplify(1 / (4 + 3 * I))),
    ('S73-F1-Q5', 'E', sp.simplify(1 / (1 + 2 * I))),
    ('S75-M-Q2', 'N', sp.Rational(1, 6)), ('S75-M-Q3', 'N', sp.Rational(5, 3)), ('S75-M-Q4', 'N', sp.Rational(-1, 2)),
    ('S75-F2-Q5', 'N', sp.solve(X + 3 - 2 * (X + 1), X)[0]),
    ('S76-M-Q2', 'N', 20 - 6.5 * 0.3 * 10, 2), ('S76-M-Q4', 'N', 1.08 * 50, 2),
    ('S79-M-Q4', 'E', -1 + sp.sqrt(X + 4)), ('S79-F1-Q2', 'E', 2 + sp.sqrt((20 - h) / 5)),
    ('S80-M-Q1', 'N', 3 ** 4), ('S80-M-Q2', 'N', 5 ** 2 + 1), ('S80-M-Q3', 'E', sp.E - 2), ('S80-M-Q5', 'N', 10),
    ('S80-F1-Q1', 'N', sp.solve((X + 6) - 4 * X, X)[0]), ('S80-F1-Q2', 'N', 9), ('S80-F2-Q2', 'N', 1.5571, 2),
    ('S83-F2-Q1', 'S', [math.asin(0.4), math.pi - math.asin(0.4)], 2), ('S83-F2-Q2', 'S', [math.acos(0.4), 2 * math.pi - math.acos(0.4)], 2),
    ('S84-M-Q2', 'S', [math.acos(-2 / 3), 2 * math.pi - math.acos(-2 / 3)], 2), ('S84-M-Q5', 'S', [math.atan(3), math.atan(3) + math.pi], 2),
    ('S84-M-Q3', 'S', [2.5, 12.5], 1), ('S84-M-Q4', 'S', [2, 10]),
]


def main():
    data = json.load(open(KEY, encoding='utf-8'))
    recs = {r['id']: r for r in data['questions']}
    bad = []
    for case in CASES:
        qid, kind, want = case[:3]
        dec = case[3] if len(case) > 3 else None
        if qid not in recs:
            bad.append('%s: no such question' % qid)
            continue
        try:
            ok = check(recs[qid], kind, want, dec)
        except Exception as e:  # noqa: BLE001
            ok, want = False, '%s (%s)' % (want, e)
        if not ok:
            bad.append('%s: key "%s" does not state %s' % (qid, recs[qid]['correct_answer'], want))
    print('Algebra II independent re-solve: %d cases, %d disagreements' % (len(CASES), len(bad)))
    for line in bad:
        print('  ' + line)
    return 1 if bad else 0


def run():
    """For validate.py: (questions checked, values checked, disagreements)."""
    data = json.load(open(KEY, encoding='utf-8'))
    recs = {r['id']: r for r in data['questions']}
    bad, nv = [], 0
    for case in CASES:
        qid, kind, want = case[:3]
        dec = case[3] if len(case) > 3 else None
        nv += len(want) if kind == 'S' else 1
        if qid not in recs or not check(recs[qid], kind, want, dec):
            bad.append('%s: key does not state %s' % (qid, want))
    return len(CASES), nv, bad


if __name__ == '__main__':
    sys.exit(main())
