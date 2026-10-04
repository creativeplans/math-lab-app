"""Write <grade>/COVERAGE.md from <grade>/src/coverage_reqs.py: each requirement, its focused set, and that set's branches.

    python3 question-bank/engine/coverage.py grade5
"""
import importlib
import json
import os
import sys

ENGINE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ENGINE)
import build  # noqa: E402
import answers as A  # noqa: E402


def run(name):
    build.load_grade(name)
    cov = importlib.import_module('coverage_reqs')
    sets = {st['num']: st for st in build.all_sets()}
    pages = {r['id']: r['page'] for r in json.load(open(build.out_paths()['data'] + '.json', encoding='utf-8'))['questions']}
    used = set()
    lines = ['# Grade %d coverage matrix' % build.GRADE, '',
             'Each row is one distinct Grade %d requirement and the set whose MAIN section (five variations) focuses on it. '
             'Every set also has its backward (earlier-grade) branches and FORWARD 1 (Grade %d) and FORWARD 2 (Grade %d). '
             'Page is the MAIN section\'s first question page in the question PDF.' % (build.GRADE, build.GRADE + 1, build.GRADE + 2), '',
             '| Standard | Requirement | Set | MAIN IDs | Page | Backward branches | Forward 1 | Forward 2 |', '|---|---|---|---|---:|---|---|---|']
    for std, req, nums in cov.REQUIREMENTS:
        for n in nums:
            st = sets[n]
            assert st['std'] == std, (n, st['std'], std)
            used.add(n)
            secs = build.sections(st)
            back = '; '.join('%s %s' % (A.section_code(k), s) for k, _, s, _, _ in secs if k.startswith('BACKWARD'))
            f1 = [s for k, _, s, _, _ in secs if k == 'FORWARD 1'][0]
            f2 = [s for k, _, s, _, _ in secs if k == 'FORWARD 2'][0]
            lines.append('| %s | %s | S%d — %s | S%d-M-Q1 … Q5 | %d | %s | %s | %s |' % (
                std, req, n, st['title'], n, pages['S%d-M-Q1' % n], back, f1, f2))
    missing = sorted(set(sets) - used)
    assert not missing, 'sets without a requirement row: %s' % missing
    path = os.path.join(build.GRADE_DIR, 'COVERAGE.md')
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return path, len(cov.REQUIREMENTS)


if __name__ == '__main__':
    print(run(sys.argv[1] if len(sys.argv) > 1 else 'grade5'))
