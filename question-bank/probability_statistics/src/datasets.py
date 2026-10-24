"""Registry of every dataset used in the Probability & Statistics collection.

All datasets are synthetic: written for this collection to show the intended feature (a skew, an outlier, a linear or
exponential trend), then summarized by code (common.py) so the printed values, figures and keys agree. None is real data
and none depends on a website. write_md() produces DATASETS.md (values, size, units, provenance, where used).
"""
import os

REG = {}  # name -> dict(values, unit, context, used)


def D(name, values, unit, context):
    """Register a one-variable dataset (or a list of (x, y) pairs) and return its values unchanged."""
    assert name not in REG or REG[name]['values'] == values, ('dataset name reused with different values', name)
    REG[name] = dict(values=list(values), unit=unit, context=context)
    return values


def write_md(path):
    L = ['# Datasets', '',
         'Every dataset below is **synthetic**: invented for this collection, with values chosen to show the intended feature. '
         'The values printed here are exactly the values printed on the question pages; every summary in the answer key was '
         'computed from them (src/common.py) and recomputed independently (src/resolve.py).', '',
         '| Name | n | Values | Unit | Context |', '|---|---:|---|---|---|']
    for k in sorted(REG):
        r = REG[k]
        vals = ', '.join('(%s, %s)' % v if isinstance(v, tuple) else str(v) for v in r['values'])
        L.append('| %s | %d | %s | %s | %s |' % (k, len(r['values']), vals, r['unit'], r['context']))
    open(path, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return path


if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
    import build
    build.load_grade('probability_statistics')
    list(build.all_sets())
    print(write_md(os.path.join(build.GRADE_DIR, 'DATASETS.md')), len(REG))
