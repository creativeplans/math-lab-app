"""Authoring toolkit for the Logic collection.

Every constructor returns a question record in the Untangle The Nexus package format (docs/COURSE-BANKS.md, course
"logic"), plus private author fields that start with "_": the full solution ("_why"), how the key was verified
("_method"), and why each wrong choice fails ("_wrong"). Private fields go to the answer key only, never to the package.

Verification happens here, while the question is built:
  grid / order   every assignment or ordering is enumerated against the clue function; the key is the set of all
                 solutions (the importer gets every valid solution, so no correct answer is rejected)
  truth_table    every output cell is computed from the formula
  values         the example answer must satisfy the rule and each listed wrong answer must fail it, using a Python
                 copy of the game's rule language (responses.ts evalRule)
  mc with check  a check function decides each choice; exactly one choice may pass
"""
import itertools
import math
import re

_ids = itertools.count()


# ------------------------------------------------------------------ the game's rule language, in Python
def _is_prime(n):
    return float(n).is_integer() and n > 1 and all(n % d for d in range(2, int(math.isqrt(int(n))) + 1))


RULE_FUNCS = {
    'isPrime': _is_prime, 'isEven': lambda n: float(n).is_integer() and n % 2 == 0,
    'isOdd': lambda n: float(n).is_integer() and n % 2 == 1, 'isInteger': lambda n: float(n).is_integer(),
    'isSquare': lambda n: n >= 0 and float(n).is_integer() and math.isqrt(int(n)) ** 2 == n, 'abs': abs,
    'sqrt': math.sqrt, 'floor': math.floor, 'min': min, 'max': max, 'mod': lambda a, b: a % b,
    'divides': lambda a, b: a != 0 and b % a == 0,
}


def _num(s):
    s = str(s).strip().replace('−', '-')
    try:
        if re.fullmatch(r'-?\d+/\d+', s):
            a, b = s.split('/')
            return int(a) / int(b)
        v = float(s)
        return int(v) if v.is_integer() else v
    except ValueError:
        return s.lower()


def eval_rule(rule, values):
    """Evaluate a values-rule the way the game does (numbers parsed; other answers lowercased words)."""
    if re.search(r'[A-Za-z_]+\s*\(', rule):
        for f in re.findall(r'([A-Za-z_]+)\s*\(', rule):
            assert f in RULE_FUNCS or f in ('and', 'or', 'not'), 'function %s is not in the rule language' % f
    py = rule.replace('^', '**')
    env = dict(RULE_FUNCS)
    env.update({k: _num(v) for k, v in values.items()})
    try:
        return eval(py, {'__builtins__': {}}, env) is True
    except (TypeError, ZeroDivisionError, ValueError):
        return False


# ------------------------------------------------------------------ question constructors
def _base(qtype, prompt, why, method, fig=None, feedback=None, intro=None):
    q = {'type': qtype, 'prompt': prompt, '_why': why, '_method': method}
    if fig:
        q['_fig'] = fig  # (svg text, description)
    if feedback:
        q['feedback'] = feedback
    if intro:
        q['intro'] = intro
    return q


def mc(prompt, correct, wrong, why, method='solved by the author; each wrong choice checked against its reason', fig=None,
       key=None, check=None, feedback=None, intro=None):
    """correct: the right choice text; wrong: [(text, why it is wrong)] (3 for four choices).
    key: fixed letter (only for figure items whose panels are labeled A-D; then pass choices in panel order through
    `order`). check: function(choice_text) -> bool that must accept exactly the correct choice."""
    texts = [correct] + [w[0] for w in wrong]
    assert len(set(t.strip().lower() for t in texts)) == len(texts), 'duplicate choices: %s' % texts
    if check:
        res = [bool(check(t)) for t in texts]
        assert res[0] and not any(res[1:]), 'check function disagrees with the key: %s' % list(zip(texts, res))
        method = method + ' Automatic: the check function accepts only the keyed choice.'
    q = _base('mc', prompt, why, method, fig, feedback, intro)
    q['_correct'] = correct
    q['_wrong'] = list(wrong)
    if key:
        q['_fixed_key'] = key
    return q


def figmc(prompt, panels, key, wrong_reasons, why, fig, method='', check=None):
    """A choice among labeled figure panels: choices are 'Figure A'...; key is the correct panel letter.
    wrong_reasons: {letter: reason}. check: function(letter) -> bool, must accept only the key."""
    letters = 'ABCD'[:panels]
    if check:
        res = {L: bool(check(L)) for L in letters}
        assert res[key] and sum(res.values()) == 1, 'figure check disagrees: %s (key %s)' % (res, key)
        method = (method + ' ' if method else '') + 'Automatic: the panel check accepts only the keyed panel.'
    q = _base('mc', prompt, why, method or 'solved by the author; every panel compared with the rule', fig)
    q['_panels'] = letters
    q['_fixed_key'] = key
    q['_correct'] = 'Figure %s' % key
    q['_wrong'] = [('Figure %s' % L, wrong_reasons[L]) for L in letters if L != key]
    return q


def tf(statement, key, why, method='solved by the author', fig=None, check=None, feedback=None):
    if check is not None:
        assert bool(check()) == bool(key), 'tf check disagrees with key: %s' % statement
        method = method + ' Automatic: the statement was evaluated by code.'
    q = _base('tf', statement, why, method, fig, feedback)
    q['_key'] = bool(key)
    return q


def sa(prompt, lines, key, why, method='solved by the author', fig=None, compute=None, feedback=None):
    """Short answer: one line per part; key parts separated by '; '. compute: function returning the key (checked)."""
    if compute is not None:
        got = compute()
        assert str(got) == str(key), 'computed %s, keyed %s' % (got, key)
        method = method + ' Automatic: the key was recomputed by code.'
    q = _base('sa', prompt, why, method, fig, feedback)
    q['answer_lines'] = lines if isinstance(lines, list) else [lines]
    q['correct_answer'] = key
    return q


def order(prompt, items, ok, why, expect=None, method='', fig=None, feedback=None, unique=False):
    """items: [(key, text)]; ok: function(tuple of keys in order) -> bool. Every ordering is enumerated; all valid
    orders are accepted. expect: the ordering the author derived (must be valid). Requires 1-3 valid orderings."""
    keys = [k for k, _ in items]
    sols = [list(p) for p in itertools.permutations(keys) if ok(p)]
    assert sols, 'no ordering satisfies the clues: %s' % prompt[:80]
    assert len(sols) <= 3, '%d valid orderings: %s' % (len(sols), prompt[:80])
    if unique:
        assert len(sols) == 1, '%d valid orderings (expected one): %s %s' % (len(sols), prompt[:60], sols)
    if expect:
        assert list(expect) in sols, 'author ordering %s is not valid' % expect
        sols.remove(list(expect))
        sols.insert(0, list(expect))
    q = _base('order', prompt, why, (method + ' ' if method else '') + 'Automatic: all %d orderings of %d items enumerated; %d valid.'
              % (math.factorial(len(keys)), len(keys), len(sols)), fig, feedback)
    q['items'] = [{'key': k, 'text': t} for k, t in items]
    q['correct_order'] = sols[0]
    if len(sols) > 1:
        q['accept_orders'] = sols[1:]
    return q


def grid(prompt, rows, cols, ok, why, distinct=True, expect=None, method='', fig=None, unique=True, feedback=None):
    """Assign one column to each row. ok: function(dict row->col) -> bool. Every assignment is enumerated."""
    space = itertools.permutations(cols, len(rows)) if distinct else itertools.product(cols, repeat=len(rows))
    sols = [dict(zip(rows, a)) for a in space if ok(dict(zip(rows, a)))]
    assert sols, 'no assignment satisfies the clues: %s' % prompt[:80]
    if unique:
        assert len(sols) == 1, '%d solutions: %s' % (len(sols), sols[:4])
    assert len(sols) <= 6, 'too many solutions'
    if expect:
        assert expect in sols, 'author assignment is not a solution'
        sols.remove(expect)
        sols.insert(0, expect)
    n = (math.perm(len(cols), len(rows)) if distinct else len(cols) ** len(rows))
    q = _base('grid', prompt, why, (method + ' ' if method else '') + 'Automatic: all %d assignments enumerated; %d satisfy every clue.'
              % (n, len(sols)), fig, feedback)
    q['rows'] = list(rows)
    q['columns'] = list(cols)
    if distinct:
        q['distinct_columns'] = True
    q['correct_assignment'] = sols[0]
    if len(sols) > 1:
        q['accept_assignments'] = sols[1:]
    return q


def tt(prompt, variables, outputs, why, feedback=None):
    """Truth table. outputs: [(label, function(*bools) -> bool)]. Rows run TT.., TF.., ..., FF.. (standard order)."""
    rows = list(itertools.product([True, False], repeat=len(variables)))
    q = _base('truth_table', prompt, why, 'Automatic: every output cell computed from the formula (%d rows).' % len(rows),
              None, feedback)
    q['variables'] = list(variables)
    q['rows'] = [['T' if v else 'F' for v in r] for r in rows]
    q['columns'] = [lab for lab, _ in outputs]
    q['correct'] = [['T' if f(*r) else 'F' for _, f in outputs] for r in rows]
    return q


VENN_REGIONS = {2: ['A', 'B', 'AB', 'O'], 3: ['A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC', 'O']}


def venn(prompt, labels, member, why, feedback=None):
    """Mark the Venn regions that satisfy a condition. labels: names of the 2 or 3 circles, in order A, B(, C).
    member: function(inA, inB[, inC]) -> bool says whether a region is marked; the marked regions are computed."""
    n = len(labels)
    marks = []
    for reg in VENN_REGIONS[n]:
        flags = [('ABC'[i] in reg) and reg != 'O' for i in range(n)]
        if member(*flags):
            marks.append(reg)
    assert marks, 'no region marked'
    q = _base('mark', prompt, why, 'Automatic: each of the %d regions tested against the condition.' % len(VENN_REGIONS[n]),
              None, feedback)
    q['layout'] = 'venn%d' % n
    q['sets'] = list(labels)
    q['correct_marks'] = marks
    return q


def markgrid(prompt, nrows, ncols, cells, why, accept=None, fig=None, method='', feedback=None):
    """Mark cells "r,c" (1-based) of a grid. accept: other valid mark sets (for example symmetric ones)."""
    q = _base('mark', prompt, why, method or 'solved by the author', fig, feedback)
    q['layout'] = 'grid'
    q['rows'] = nrows
    q['cols'] = ncols
    q['correct_marks'] = ['%d,%d' % rc for rc in cells]
    if accept:
        q['accept_marks'] = [['%d,%d' % rc for rc in a] for a in accept]
    return q


def values(prompt, fields, rule, example, why, wrong=(), search=None, method='', fig=None, feedback=None):
    """Free construction checked by a rule. fields: [(name, label)]. example: one valid answer {name: value}.
    wrong: answers that must FAIL the rule (tempting mistakes). search: (dict of name -> iterable) to count every valid
    answer in a finite domain; the count is recorded in the validation method."""
    assert eval_rule(rule, example), 'example answer fails its own rule: %s %s' % (rule, example)
    for w in wrong:
        assert not eval_rule(rule, w), 'wrong answer %s passes the rule %s' % (w, rule)
    extra = ''
    if search:
        names = list(search)
        n_ok = sum(1 for combo in itertools.product(*[search[k] for k in names])
                   if eval_rule(rule, dict(zip(names, combo))))
        assert n_ok >= 1
        extra = ' Search of the stated domain: %d valid answers.' % n_ok
    q = _base('values', prompt, why, (method + ' ' if method else '') + 'Automatic: the example passes the rule and %d '
              'listed mistakes fail it.%s' % (len(wrong), extra), fig, feedback)
    q['fields'] = [{'name': nm, 'label': lab} for nm, lab in fields]
    q['rule'] = rule
    q['example_answer'] = example
    q['_wrong_values'] = list(wrong)
    return q


# ------------------------------------------------------------------ sections and sets
def lesson(title, text, example_title, example_prompt, steps):
    return {'title': title, 'text': list(text), 'example': {'title': example_title, 'prompt': list(example_prompt),
                                                              'steps': list(steps)}}


def B(skill, mode, relationship, qs, lesson=None, outcome=None, why_helps=None):
    """A backward branch. mode: guided_strategy or prerequisite. why_helps: author metadata (why it helps a student who
    cannot solve MAIN). outcome: the earlier local outcome it assesses (defaults to the set's)."""
    assert mode in ('guided_strategy', 'prerequisite')
    if mode == 'guided_strategy':
        assert lesson, 'a guided strategy branch needs a lesson'
    return dict(kind='B', skill=skill, mode=mode, relationship=relationship, qs=qs, lesson=lesson, outcome=outcome,
                why_helps=why_helps or relationship)


def FW(skill, relationship, qs, nearest=None):
    return dict(kind='F', skill=skill, relationship=relationship, qs=qs, nearest=nearest)


def S(num, skill, main, back, f1, f2):
    return dict(num=num, skill=skill, main=main, back=back, f1=f1, f2=f2)
