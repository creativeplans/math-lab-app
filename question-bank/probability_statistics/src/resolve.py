"""Independent re-solve of computable Probability & Statistics answers.

Each case recomputes an answer from the givens printed in the question, with Python's statistics, fractions and math
modules. The givens are typed in again here; nothing is imported from the data modules or common.py, and no key string is
reused. The key text is split at ';' into parts; a case passes when every recomputed value equals its key part:
  a Fraction must equal the part read as a fraction or terminating decimal exactly;
  a (value, places) pair must equal the part read as a number after rounding the value to that many places;
  a str must equal the part exactly (words such as yes/no, letters, percents written as text).

    python3 question-bank/probability_statistics/src/resolve.py      (prints a summary; exit 1 on any disagreement)
"""
import json
import math
import os
import statistics as st
import sys
from fractions import Fraction as F
from itertools import product
from math import comb, perm

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(os.path.dirname(HERE), 'Probability_Statistics_Answer_Key.json')


# ---------------------------------------------------------------- independent helpers
def med(v):
    return F(st.median([F(x) for x in v]))


def q13(v):
    """Q1 and Q3 as medians of the halves (median left out when n is odd)."""
    s = sorted(F(x) for x in v)
    h = len(s) // 2
    lo, hi = s[:h], s[h + (len(s) % 2):]
    return med(lo), med(hi)


def iqr(v):
    a, b = q13(v)
    return b - a


def avg(v):
    return F(sum(F(x) for x in v), len(v))


def lsq(pts):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    mx, my = avg(xs), avg(ys)
    m = sum((F(x) - mx) * (F(y) - my) for x, y in pts) / sum((F(x) - mx) ** 2 for x in xs)
    return float(m), float(my - m * mx)


def r(pts):
    return float(st.correlation([p[0] for p in pts], [p[1] for p in pts]))


def zl(z):
    """Table area to the left of z, to four places (as printed)."""
    return round(0.5 * math.erfc(-z / math.sqrt(2)), 4)


def pc(x):
    """A percent written as text, e.g. 37.5%."""
    s = ('%.6f' % x).rstrip('0').rstrip('.')
    return s + '%'


def N(v, d):
    return (v, d)


DICE = list(product(range(1, 7), repeat=2))


def pdice(ev, given=lambda o: True):
    sp = [o for o in DICE if given(o)]
    return F(sum(1 for o in sp if ev(o)), len(sp))


STUDY = [(1, 52), (2, 58), (2, 61), (3, 63), (4, 70), (5, 72), (5, 76), (6, 80), (7, 83), (8, 90)]
CARS = [(1, 24), (2, 21), (3, 22), (4, 17), (5, 18), (6, 13), (7, 14), (8, 9), (9, 11), (10, 6)]
ICE = [(1, 48), (2, 44), (3, 41), (4, 35), (5, 33), (6, 28)]
SPRING = [(2, 15), (4, 19), (5, 24), (7, 26), (8, 31), (10, 35)]
CONES = [(60, 120), (65, 140), (70, 155), (75, 175), (80, 190), (85, 210), (90, 60)]
DIG = ['15881399869879730911', '41707536455681518844', '72940557616987168976', '84697880932081967273',
       '17784864887663440029', '78753477876804571784', '72671475136270107981', '93319084520599728379']
HEADS = {0: 0, 1: 1, 2: 4, 3: 12, 4: 20, 5: 25, 6: 20, 7: 12, 8: 4, 9: 2, 10: 0}


def count(s, ok):
    return sum(1 for c in s if ok(int(c)))


def pairs(s, ok):
    return sum(1 for i in range(0, len(s), 2) if ok(int(s[i:i + 2])))


def pick(s, top, k):
    out = []
    for i in range(0, len(s) - 1, 2):
        v = int(s[i:i + 2])
        if 1 <= v <= top and v not in out:
            out.append(v)
    return [str(v) for v in out[:k]]


def ge(t, k):
    return F(sum(v for x, v in t.items() if x >= k), sum(t.values()))


def binom(n, p, k):
    return comb(n, k) * F(p) ** k * (1 - F(p)) ** (n - k)


# ---------------------------------------------------------------- cases (id, [expected parts])
CASES = [
    # S1-S3 displays
    ('S1-M-Q1', [F([2, 4, 3, 2, 5, 3, 2, 6, 3, 4, 2, 3, 1, 3, 4].count(k)) for k in (2, 3, 4)]),
    ('S1-M-Q5', [F(sum(1 for x in [1, 2, 0, 1, 3, 2, 1, 1, 0, 2, 5, 1, 2, 0, 1, 2, 3, 1, 1, 2] if x >= 2)), F(20)]),
    ('S1-F1-Q2', [N(float(avg([3, 3, 4, 4, 4, 4, 5, 5, 6, 7])), 1)]),
    ('S2-M-Q1', [F(sum(1 for x in [12, 25, 8, 31, 17, 22, 15, 40, 19, 27, 10, 33, 21, 14, 26, 18, 35, 23, 29, 16] if a <= x < a + 10))
                 for a in (10, 30, 40)]),
    ('S2-M-Q3', [F(sum(1 for x in [152, 168, 145, 175, 160, 158, 171, 149, 163, 180, 155, 166, 150, 172, 161, 157] if a <= x < a + 10))
                 for a in (150, 170)]),
    ('S3-M-Q1', [F(9), *q13([12, 15, 9, 18, 14, 11, 16, 20, 13, 10, 17])[:1], med([12, 15, 9, 18, 14, 11, 16, 20, 13, 10, 17]),
                 q13([12, 15, 9, 18, 14, 11, 16, 20, 13, 10, 17])[1], F(20)]),
    ('S3-M-Q3', [F('5.5'), q13([7.5, 6, 8, 6.5, 9, 7, 5.5, 8.5, 7, 6.5, 7.5, 8, 6, 7])[0],
                 med([7.5, 6, 8, 6.5, 9, 7, 5.5, 8.5, 7, 6.5, 7.5, 8, 6, 7]),
                 q13([7.5, 6, 8, 6.5, 9, 7, 5.5, 8.5, 7, 6.5, 7.5, 8, 6, 7])[1], F(9)]),
    ('S3-M-Q5', [F('1.5'), q13(['2.1', '3.4', '1.8', '5', '2.7', '4.2', '3', '2.4', '3.9', '1.5'])[0],
                 med(['2.1', '3.4', '1.8', '5', '2.7', '4.2', '3', '2.4', '3.9', '1.5']),
                 q13(['2.1', '3.4', '1.8', '5', '2.7', '4.2', '3', '2.4', '3.9', '1.5'])[1], F(5)]),
    ('S3-F1-Q2', [F(1), F(220)]),
    # S4-S7 center, spread, outliers
    ('S4-M-Q1', [med([210, 225, 230, 240, 245, 250, 260, 900]), med([190, 220, 235, 255, 270, 280, 300, 310])]),
    ('S4-M-Q3', [med([2, 2, 3, 3, 3, 4, 4, 5, 14]), med([2, 3, 3, 4, 4, 5, 5, 6, 6])]),
    ('S4-M-Q5', [avg([498, 499, 500, 500, 501, 502]), avg([503, 504, 505, 505, 506, 507])]),
    ('S4-F2-Q3', [avg([2, 4, 6, 8, 100]), med([2, 4, 6, 8, 100])]),
    ('S5-M-Q1', [iqr([14, 15, 15, 16, 16, 17, 18, 18, 19]), iqr([13, 14, 16, 16, 17, 18, 20, 22, 25])]),
    ('S5-M-Q2', [N(st.pstdev([4, 6, 8, 10, 12]), 1), N(st.pstdev([7, 8, 8, 8, 9]), 1)]),
    ('S5-M-Q4', [iqr([20, 22, 23, 25, 26, 28, 30, 31]), iqr([18, 24, 24, 25, 25, 26, 26, 40])]),
    ('S5-M-Q5', [N(st.pstdev([10, 20, 30, 40, 50]), 1), N(st.pstdev([25, 28, 30, 32, 35]), 1)]),
    ('S5-F1-Q1', [N(st.stdev([4, 6, 8, 10, 12]), 2)]),
    ('S5-F1-Q3', [N(st.pstdev([2, 4, 6]), 2), N(st.stdev([2, 4, 6]), 2)]),
    ('S7-M-Q1', [q13([12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16])[0] - F(3, 2) * iqr([12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16]),
                 q13([12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16])[1] + F(3, 2) * iqr([12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16]),
                 F(1)]),
    ('S7-M-Q2', [N(float(avg([12, 15, 14, 18, 16, 13, 17, 15, 41, 14, 16])), 1), N(float(avg([12, 15, 14, 18, 16, 13, 17, 15, 14, 16])), 1)]),
    ('S7-M-Q3', [F(3), F(11), F(2)]),
    ('S7-M-Q5', [q13([3, 5, 4, 6, 5, 4, 22, 5, 3, 4])[1] + F(3, 2) * iqr([3, 5, 4, 6, 5, 4, 22, 5, 3, 4]), F(1)]),
    ('S7-F2-Q2', [N(float(avg([12, 15, 14, 18, 16, 13, 17, 15, 14, 14, 16])), 1), med([12, 15, 14, 18, 16, 13, 17, 15, 14, 14, 16])]),
    ('S7-F2-Q5', [med([5, 6, 6, 7, 8, 30]), iqr([5, 6, 6, 7, 8, 30])]),
    # S8-S10 normal models
    ('S8-M-Q3', [pc(34 + 47.5)]),
    ('S8-M-Q5', [pc(47.5 + 34), pc(16)]),
    ('S9-M-Q1', [N(zl((118 - 100) / 15), 4)]),
    ('S9-M-Q2', [N(1 - zl((60 - 50) / 8), 4)]),
    ('S9-M-Q3', [N(zl((23 - 20) / 2.5) - zl((18 - 20) / 2.5), 4)]),
    ('S9-M-Q4', [N(zl((2.5 - 3.0) / 0.4), 4)]),
    ('S9-M-Q5', [N(zl((189 - 175) / 7) - zl((168 - 175) / 7), 4)]),
    ('S9-F2-Q1', [N(zl(2) - zl(-2), 4)]),
    ('S10-M-Q2', [N(zl((0 - 3) / 4), 4)]),
    ('S10-F2-Q2', [med([150, 160, 170, 180, 190, 200, 900]), iqr([150, 160, 170, 180, 190, 200, 900])]),
    # S11-S12 two-way tables
    ('S11-M-Q1', [F(45, 160)]), ('S11-M-Q2', [F(75, 160)]),
    ('S11-F1-Q1', [F(30, 160), F(50, 160)]),
    ('S12-M-Q1', [F(30, 80), F(45, 80)]), ('S12-M-Q3', [pc(100 * 45 / 75)]),
    ('S12-M-Q4', [pc(100 * 36 / 60), pc(100 * 15 / 60)]),
    ('S12-F2-Q3', [pc(100 * (95 + 120) / 500), pc(100 * (360 + 25) / 500)]),
    # S13-S21 bivariate data
    ('S14-M-Q2', [N(200 * 1.15 ** 6, 0)]), ('S14-M-Q3', [N(-4.9 * 4 + 40 + 1.5, 1)]), ('S14-M-Q5', [N(18000 * 0.85 ** 4, 0)]),
    ('S14-F2-Q1', [F(44), N(40 * 1.05 ** 2, 2)]),
    ('S15-F1-Q1', [N(lsq(SPRING)[0], 2), N(lsq(SPRING)[1], 2)]),
    ('S15-F1-Q4', [N(2.52 * 6 + 9.86, 2)]),
    ('S15-F2-Q1', [N(24 - (2.52 * 5 + 9.86), 2)]), ('S15-F2-Q2', [N(19 - (2.52 * 4 + 9.86), 2)]),
    ('S16-M-Q1', [N(3.5 - 3, 1), N(4.6 - 5, 1)]),
    ('S16-F1-Q1', [N(2 - (1.4 * 1 + 1), 1), N(5 - (1.4 * 2 + 1), 1)]),
    ('S16-F2-Q2', [N(sum(e * e for e in [3, -1, -3, -2, 1, 4]), 2), N(sum(e * e for e in [0.2, -0.3, 0.1, 0.3, -0.2, -0.1]), 2)]),
    ('S17-M-Q1', [N(lsq(STUDY)[0], 2), N(lsq(STUDY)[1], 2)]),
    ('S17-M-Q2', [N(lsq(CARS)[0], 2), N(lsq(CARS)[1], 2)]),
    ('S17-M-Q4', [N(5.17 * 3 + 48.28, 2)]),
    ('S17-F1-Q1', [avg([p[0] for p in STUDY]), avg([p[1] for p in STUDY])]),
    ('S19-M-Q1', [N(r(STUDY), 2)]), ('S19-M-Q2', [N(r(CARS), 2)]), ('S19-M-Q3', [N(r(ICE), 2)]),
    ('S19-M-Q4', [N(r(CONES), 3), N(r(CONES[:6]), 3)]), ('S19-M-Q5', [N(r(SPRING), 2)]),
    ('S19-F1-Q1', [N(r([(1, 2), (2, 5), (3, 4), (4, 7)]), 2)]),
    # S22-S31 inference
    ('S22-M-Q3', [N(62 / 200 * 1500, 0)]),
    ('S23-M-Q1', [F(count(DIG[0][:10], lambda d: d <= 6))]),
    ('S23-M-Q2', [F(sum(1 for s in DIG if count(s[:10], lambda d: d <= 6) >= 8))]),
    ('S23-M-Q4', [F(pairs(DIG[4], lambda v: v < 25))]),
    ('S23-F1-Q2', [F(pairs(DIG[2], lambda v: v < 35))]),
    ('S23-F1-Q4', [F(sum(1 for s in DIG if count(s[:10], lambda d: d <= 4) <= 3))]),
    ('S23-F2-Q1', [ge(HEADS, 9)]), ('S23-F2-Q4', [ge(HEADS, 7)]),
    ('S24-M-Q1', [ge(HEADS, 8)]),
    ('S24-F1-Q1', [ge(HEADS, 9) + F(HEADS[0] + HEADS[1], 100)]),
    ('S24-F1-Q4', [ge(HEADS, 7) + F(sum(HEADS[k] for k in range(4)), 100)]),
    ('S26-M-Q1', pick(DIG[0], 40, 3)), ('S26-M-Q5', pick(DIG[2], 60, 3)),
    ('S26-B2-Q3', pick('450729073318', 30, 3)),
    ('S27-M-Q3', [N(0.62 - 0.048, 3), N(0.62 + 0.048, 3)]),
    ('S27-F1-Q1', [N(2 * math.sqrt(0.25 / 400), 2), N(2 * math.sqrt(0.25 / 100), 1)]),
    ('S28-M-Q1', [avg([7, 6.5, 8, 7.5, 6, 9, 7, 8])]),
    ('S29-M-Q1', [avg([14, 11, 13, 12, 15]), avg([10, 12, 9, 11, 8]), avg([14, 11, 13, 12, 15]) - avg([10, 12, 9, 11, 8])]),
    ('S31-M-Q1', [F(55 - 50, 52 - 50), N(55 / 52, 2)]),
    # S32-S45 probability
    ('S32-M-Q4', [F(sum(1 for a, b in DICE if a + b == 7))]),
    ('S32-M-Q5', [F(3), F(len([k for k in range(1, 9) if k % 2 == 0 and k > 3]), 8)]),
    ('S33-M-Q5', [F(3, 52), F(13 + 12 - 3, 52)]),
    ('S33-F2-Q2', [F(4 + 13 - 1, 52)]),
    ('S34-F1-Q2', [N(0.9 ** 3, 3), N(1 - 0.9 ** 3, 3)]),
    ('S35-M-Q3', [pdice(lambda o: o[0] == o[1], lambda o: sum(o) == 8)]),
    ('S36-M-Q4', [F(4, 52), F(3, 51)]),
    ('S37-M-Q2', [F(90 - 25), F(150 - (90 + 40 - 25))]),
    ('S37-F2-Q1', [F(35 + 12, 80)]), ('S37-F2-Q5', [F(18, 80)]),
    ('S38-F1-Q1', [F(24 + 36, 125), F(36, 75)]), ('S38-F1-Q3', [F(16, 40)]),
    ('S39-F1-Q2', [F(5, 7) * F(4, 5)]),
    ('S40-M-Q1', [pdice(lambda o: sum(o) >= 10, lambda o: o[0] == 5)]),
    ('S40-F1-Q1', [pdice(lambda o: sum(o) == 7, lambda o: 6 in o)]),
    ('S41-M-Q2', [F(26 + 4 - 2, 52)]), ('S41-M-Q3', [pdice(lambda o: o[0] == o[1] or sum(o) == 8)]),
    ('S41-F2-Q2', [1 - F(120 + 70 - 40, 200)]),
    ('S42-M-Q1', [F(5, 8) * F(4, 7)]), ('S42-M-Q2', [F(5, 8) * F(3, 7)]), ('S42-M-Q3', [F(4, 52) * F(3, 51)]),
    ('S42-F1-Q1', [2 * F(5, 8) * F(3, 7)]), ('S42-F1-Q2', [F(13, 52) * F(12, 51) * F(11, 50)]),
    ('S40-F2-Q1', [F(4, 6) * F(3, 5)]),
    ('S43-M-Q1', [F(perm(5, 3))]), ('S43-M-Q3', [F(perm(10, 4))]), ('S43-M-Q5', [F(perm(10, 3))]),
    ('S43-F1-Q2', [F(2 * perm(3))]),
    ('S44-M-Q2', [F(comb(8, 3))]), ('S44-M-Q3', [F(comb(10, 4))]), ('S44-M-Q5', [F(comb(7, 2))]),
    ('S44-F1-Q1', [F(comb(5, 3) * comb(4, 2))]),
    ('S45-M-Q1', [F(1, comb(10, 3))]), ('S45-M-Q2', [F(comb(4, 3), comb(9, 3))]), ('S45-M-Q3', [F(perm(3), perm(5))]),
    ('S45-M-Q4', [F(comb(13, 2), comb(52, 2))]),
    ('S45-F1-Q1', [F(comb(5, 3), comb(9, 3))]), ('S45-F1-Q2', [1 - F(comb(5, 3), comb(9, 3))]),
    ('S45-F2-Q2', [F(comb(5, 3), comb(9, 3)), F(comb(4, 3), comb(9, 3))]),
    # S46-S54 decisions
    ('S46-M-Q1', [binom(3, F(1, 2), k) for k in range(4)]),
    ('S46-M-Q2', [F(11), pdice(lambda o: sum(o) == 7)]),
    ('S46-F1-Q2', [pdice(lambda o: sum(o) <= 4)]),
    ('S46-F2-Q3', [F('0.2') + 2 * F('0.5') + 3 * F('0.3')]),
    ('S47-M-Q2', [F('0.35') + 2 * F('0.4') + 3 * F('0.15')]),
    ('S47-M-Q5', [10 * F('0.2') + 2 * F('0.3')]),
    ('S47-F1-Q1', [5 * F('0.2') - 2 * F('0.8')]), ('S47-F1-Q3', [-3 * F('0.5') + 6 * F('0.3')]),
    ('S47-F2-Q1', [binom(6, F(1, 2), 3)]),
    ('S48-M-Q1', [binom(4, F(1, 2), 2)]),
    ('S48-M-Q3', [F(1, 4) ** 5, 5 * F(1, 4)]),
    ('S48-M-Q5', [1 - F(3, 4) ** 3]),
    ('S48-F1-Q1', [binom(3, F(1, 4), k) for k in range(4)]),
    ('S49-M-Q1', [F(40, 100), F(25, 100)]), ('S49-M-Q2', [F(30 + 80 + 60 + 20, 100)]),
    ('S49-M-Q5', [F(15 + 20 + 15, 50)]),
    ('S49-F1-Q1', [F(6, 60), N(1 / 6, 2)]),
    ('S49-F1-Q2', [F(1 * 7 + 2 * 13 + 3 * 9 + 4 * 11 + 5 * 14 + 6 * 6, 60)]),
    ('S50-M-Q1', [F(500, 1000) - 2]), ('S50-M-Q2', [5 * F(1, 6) - F(5, 6)]), ('S50-M-Q3', [F(1000, 500) - 5]),
    ('S50-M-Q5', [8 * F(1, 4) - 2 * F(3, 4)]),
    ('S51-M-Q1', [1200 + F('0.2') * 500, 900 + F('0.2') * 1000]),
    ('S51-M-Q3', [2000 * F('0.3') - 400 * F('0.7'), F(250)]),
    ('S51-F1-Q1', [F(150, 800)]), ('S51-F1-Q3', [F(1200 - 900, 1000 - 500)]),
    ('S52-M-Q2', [{'0': 'A', '1': 'A', '2': 'B', '3': 'B', '4': 'C', '5': 'C', '6': 'D', '7': 'D'}[next(c for c in DIG[1] if c < '8')]]),
    ('S53-M-Q3', [F(18, 18 + 49)]), ('S53-M-Q5', [F(980 - 49, 980 - 49 + 2)]),
    ('S53-F1-Q2', [F(90, 90 + 45)]),
    ('S53-F2-Q1', [F(comb(8, 2), comb(10, 2))]),
    ('S53-F2-Q3', [F(1, 4) - F(3, 4) * F(1, 3), F(1, 3) - F(2, 3) * F(1, 3)]),
    ('S54-M-Q3', [F(comb(9, 2), comb(12, 2))]),
    ('S54-M-Q4', [F(1, 5) - F(4, 5) * F(1, 4), F(1, 4) - F(3, 4) * F(1, 4)]),
    ('S54-F1-Q1', [F(400), 50 + F('0.2') * 400]),
    ('S54-F2-Q1', [5 * F(1, 4), F(3, 4) ** 5]), ('S54-F2-Q3', [1 - F(3, 4) ** 5]),
]


def as_frac(s):
    s = s.strip().replace(',', '')
    if s.endswith('%'):
        return None
    try:
        return F(s)
    except (ValueError, ZeroDivisionError):
        return None


def agree(part, want):
    part = part.strip()
    if isinstance(want, str):
        return part == want
    if isinstance(want, tuple):
        v, d = want
        try:
            return abs(float(part.replace(',', '')) - round(v, d)) < 10 ** -(d + 3) + 1e-12
        except ValueError:
            return False
    got = as_frac(part)
    return got is not None and got == want


def run(verbose=False):
    recs = {q['id']: q for q in json.load(open(KEY, encoding='utf-8'))['questions']}
    bad, nv = [], 0
    for qid, wants in CASES:
        if qid not in recs:
            bad.append(qid + ' missing')
            continue
        parts = [p for p in recs[qid]['correct_answer'].split(';')]
        if len(parts) != len(wants):
            bad.append('%s: %d key parts, %d recomputed' % (qid, len(parts), len(wants)))
            continue
        for p, w in zip(parts, wants):
            nv += 1
            if not agree(p, w):
                bad.append('%s: key "%s", recomputed %s' % (qid, p.strip(), w))
    if verbose:
        print('%d questions, %d values; %d disagreements' % (len(CASES), nv, len(bad)))
        for b in bad:
            print('  ' + b)
    return len(CASES), nv, bad


if __name__ == '__main__':
    sys.exit(1 if run(True)[2] else 0)
