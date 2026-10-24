// Runs fixed student responses through the Untangle The Nexus short-answer checker and records whether each is accepted.
//   npx tsx <this file> <Answer_Key.json> <checker_cases.json> <out.json>     (run from the game repository)
// checker_cases.json lists [question ID, response parts, expected result, what the case tests]. The responses are typed
// as a student would type them, one entry per answer line. Read-only: nothing in the game repository is changed.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const game = process.env.NEXUS_DIR ?? process.cwd();

async function main() {
  const { checkAnswer, inferAnswerForm } = await import(resolve(game, 'packages/curriculum/src/answers.ts'));
  const qs = new Map<string, any>(JSON.parse(readFileSync(process.argv[2], 'utf8')).questions.map((q: any) => [q.id, q]));
  const cases: [string, string[], boolean, string][] = JSON.parse(readFileSync(process.argv[3], 'utf8'));
  const rows = cases.map(([id, parts, expected, what]) => {
    const q = qs.get(id);
    if (!q) return { id, parts, expected, what, accepted: null };
    const blanks = q.answer_lines?.length ? q.answer_lines : ['Answer:'];
    const key: any = { kind: 'short', value: q.correct_answer, form: inferAnswerForm(q.question) };
    const accepted = checkAnswer(key, { blanks: parts }, blanks).correct === true;
    return { id, key: q.correct_answer, parts, expected, what, accepted };
  });
  writeFileSync(process.argv[4], JSON.stringify(rows, null, 1));
  console.error(`${rows.length} cases; as expected ${rows.filter((r) => r.accepted === r.expected).length}`);
}
main();
