"""Print sets in compact form for the author's read-through: python3 dump.py 2 3 (set numbers; none = all)."""
import json, os, sys
K = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Logic_Answer_Key.json')))['questions']
want = {int(a) for a in sys.argv[1:]}
for r in K:
    if want and r['set'] not in want:
        continue
    ch = ' | '.join(('*' if c['letter'] == r['correct_letter'] else '') + c['text'] for c in r['choices']) if r['type'] in ('mc',) else ''
    print('%s [%s] %s%s || KEY: %s%s || WHY: %s' % (r['id'], r['type'], r['prompt'], (' || ' + ch) if ch else '',
          r['correct_answer'], (' || ALSO: ' + ' / '.join(r['accepted_alternatives'])) if r['accepted_alternatives'] else '',
          r['solution']))
