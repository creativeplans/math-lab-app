import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
async function main() {
  const R = await import(resolve(process.cwd(), 'packages/curriculum/src/responses.ts'));
  const qs: any[] = JSON.parse(readFileSync(process.argv[2], 'utf8')).questions;
  const by: Record<string, any> = Object.fromEntries(qs.map((q) => [q.id, q]));
  const cases: [string, Record<string, string>, boolean][] = [
    ['S8-M-Q4', { n: '-2' }, false], ['S12-F2-Q5', { a: '-3', b: '5' }, false], ['S13-F1-Q1', { n: '-2' }, false],
    ['S13-F2-Q5', { n: '-3' }, false], ['S15-F2-Q2', { n: '-9' }, false], ['S16-F1-Q5', { n: '-6' }, false],
    ['S16-F2-Q4', { a: '1.5', b: '2' }, false], ['S22-M-Q4', { n: '-2' }, false], ['S29-M-Q2', { n: '-6' }, false],
    ['S29-F1-Q5', { a: '1.5', b: '2.5' }, false], ['S29-F2-Q3', { a: '3', b: '4', c: '-5' }, false],
    ['S42-F1-Q1', { a: '0.5', b: '0.5' }, false], ['S29-M-Q4', { a: '1', b: '0.5' }, false], ['S29-M-Q4', { a: '-2', b: '3' }, true],
    ['S29-F2-Q3', { a: '3', b: '4', c: '5' }, true], ['S42-F1-Q1', { a: '2', b: '3' }, true], ['S40-M-Q5', { x: '7.5' }, true],
  ];
  let bad = 0;
  for (const [id, v, want] of cases) {
    const pf = by[id].package_fields;
    const got = R.checkValues({ rule: pf.rule }, { values: v }, pf.fields).correct;
    if (got !== want) bad++;
    console.log(id, JSON.stringify(v), 'expected', want, 'game says', got);
  }
  console.log('probe cases', cases.length, 'mismatches', bad);
}
main();
