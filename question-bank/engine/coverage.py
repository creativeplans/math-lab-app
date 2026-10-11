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


def fwd_level(n):
    """How the coverage header names a forward branch's level."""
    if n < 9:
        return 'Grade %d' % n
    return 'Common Core high-school standards, which this bank places at Grade %d as an instructional choice' % n


def run(name):
    build.load_grade(name)
    cov = importlib.import_module('coverage_reqs')
    sets = {st['num']: st for st in build.all_sets()}
    pages = {r['id']: r['page'] for r in json.load(open(build.out_paths()['data'] + '.json', encoding='utf-8'))['questions']}
    used = set()
    lines = ['# Grade %d coverage matrix' % build.GRADE, '',
             'Each row is one distinct Grade %d requirement and the set whose MAIN section (five variations) focuses on it. '
             'Every set also has its backward (earlier-grade) branches and FORWARD 1 (%s) and FORWARD 2 (%s). '
             'Page is the MAIN section\'s first question page in the question PDF.' % (
                 build.GRADE, fwd_level(build.GRADE + 1), fwd_level(build.GRADE + 2)), '']
    perf = any(len(r) > 3 for r in cov.REQUIREMENTS)
    if perf:
        lines += ['"Performance tested" says what students actually do in the five MAIN questions.', '',
                  '| Standard | Requirement | Performance tested | Set | MAIN IDs | Page | Backward branches | Forward 1 | Forward 2 |',
                  '|---|---|---|---|---|---:|---|---|---|']
    else:
        lines += ['| Standard | Requirement | Set | MAIN IDs | Page | Backward branches | Forward 1 | Forward 2 |', '|---|---|---|---|---:|---|---|---|']
    for row in cov.REQUIREMENTS:
        std, req, nums = row[:3]
        for n in nums:
            st = sets[n]
            assert st['std'] == std, (n, st['std'], std)
            used.add(n)
            secs = build.sections(st)
            back = '; '.join('%s %s' % (A.section_code(k), s) for k, _, s, _, _ in secs if k.startswith('BACKWARD'))
            f1 = [s for k, _, s, _, _ in secs if k == 'FORWARD 1'][0]
            f2 = [s for k, _, s, _, _ in secs if k == 'FORWARD 2'][0]
            cells = [std, req] + ([row[3]] if perf else []) + [
                'S%d — %s' % (n, st['title']), 'S%d-M-Q1 … Q5' % n, str(pages['S%d-M-Q1' % n]), back, f1, f2]
            lines.append('| ' + ' | '.join(cells) + ' |')
    missing = sorted(set(sets) - used)
    assert not missing, 'sets without a requirement row: %s' % missing
    if getattr(cov, 'NOTES', None):
        lines += [''] + cov.NOTES
    path = os.path.join(build.GRADE_DIR, 'COVERAGE.md')
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    return path, len(cov.REQUIREMENTS)


if __name__ == '__main__':
    print(run(sys.argv[1] if len(sys.argv) > 1 else 'grade5'))
