// Runs the Untangle The Nexus short-answer checker on every short answer in the answer key.
//   npx tsx <this file> <Answer_Key.json> <out.json>     (run from the game repository, so its imports resolve)
// For each short answer it records whether the game treats the key as automatically checkable, whether the key is
// accepted as its own response, and whether two simple rewrites are accepted: the same answer without spaces, and a
// sum written with its terms in reverse order (only for expressions with a variable).
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const game = process.env.NEXUS_DIR ?? process.cwd();

function terms(s: string): string[] | null {
  const out: string[] = []; let d = 0, cur = '';
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if ('([{'.includes(c)) d++;
    if (')]}'.includes(c)) d--;
    if (d === 0 && (c === '+' || c === '-') && i > 0 && s[i - 1] === ' ' && s[i + 1] === ' ') { out.push(cur.trim()); cur = c; continue; }
    cur += c;
  }
  out.push(cur.trim());
  return out.length > 1 ? out : null;
}
function reversed(s: string): string | null {
  if (/[=<>≤≥,{}]|\bor\b/.test(s) || !/[a-hj-zπ√]/i.test(s)) return null;
  const t = terms(s); if (!t) return null;
  const fix = (x: string) => x.replace(/^\+\s*/, '').replace(/^-\s*/, '-');
  return t.slice().reverse().map((x, i) => (i === 0 ? fix(x) : (x.startsWith('-') ? ' - ' + x.slice(1).trim() : ' + ' + fix(x)))).join('');
}

async function main() {
  const { checkAnswer, isAutoCheckable, splitParts, inferAnswerForm } = await import(resolve(game, 'packages/curriculum/src/answers.ts'));
  const qs = JSON.parse(readFileSync(process.argv[2], 'utf8')).questions;
  const rows: any[] = [];
  for (const q of qs) {
    if (q.type !== 'sa') continue;
    const blanks = q.answer_lines?.length ? q.answer_lines : ['Answer:'];
    const key: any = { kind: 'short', value: q.correct_answer, form: inferAnswerForm(q.question) };
    const auto = isAutoCheckable(key, blanks);
    const parts = splitParts(key.value, blanks);
    const self = auto ? checkAnswer(key, { blanks: parts }, blanks).correct === true : false;
    const rejected: string[] = [];
    if (auto) parts.forEach((p: string, i: number) => {
      const vs = [/\b(or|and)\b|\d \d+\/\d/.test(p) ? null : p.replace(/\s+/g, ''), reversed(p)].filter((v): v is string => !!v && v !== p);
      for (const v of vs) {
        const b = parts.slice(); b[i] = v;
        if (checkAnswer(key, { blanks: b }, blanks).correct !== true) rejected.push(`${p} => ${v}`);
      }
    });
    rows.push({ id: q.id, auto, self, rejected });
  }
  writeFileSync(process.argv[3], JSON.stringify(rows, null, 1));
  console.error(`short answers: ${rows.length}; not checkable: ${rows.filter((r) => !r.auto).length}; key rejected: ${rows.filter((r) => r.auto && !r.self).length}; rewrites rejected: ${rows.filter((r) => r.rejected.length).length}`);
}
main();
