// Runs every Logic key and every listed wrong answer through the game's own response checks (read-only).
//   npx tsx <this file> <Logic_Answer_Key.json> <out.json>     (run from the game repository; NEXUS_DIR may point to it)
// order/grid/truth_table/mark: the key and each accepted alternative must be accepted; a changed response (two items
// swapped, one cell flipped, one mark removed) must be rejected unless it is itself an accepted alternative.
// values: the example answer must pass the rule; every listed tempting wrong answer must fail it.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const game = process.env.NEXUS_DIR ?? process.cwd();

async function main() {
  const R = await import(resolve(game, 'packages/curriculum/src/responses.ts'));
  const qs = JSON.parse(readFileSync(process.argv[2], 'utf8')).questions;
  const rows: any[] = [];
  const same = (a: any, b: any) => JSON.stringify(a) === JSON.stringify(b);
  for (const q of qs) {
    const f = q.package_fields ?? {};
    const t = q.type;
    const bad: string[] = [];
    let tests = 0;
    if (t === 'order') {
      const all = [f.correct_order, ...(f.accept_orders ?? [])];
      const exp = { order: f.correct_order, accept: f.accept_orders };
      for (const o of all) { tests++; if (R.checkOrder(exp, { order: o }).correct !== true) bad.push('rejects ' + o.join(',')); }
      const sw = [...f.correct_order]; [sw[0], sw[1]] = [sw[1], sw[0]];
      if (!all.some((o: string[]) => same(o, sw))) { tests++; if (R.checkOrder(exp, { order: sw }).correct !== false) bad.push('accepts swap'); }
    } else if (t === 'grid') {
      const rows_ = f.rows, cols = f.columns;
      const idx = (a: any) => rows_.map((r: string) => cols.indexOf(a[r]));
      const exp = { assign: idx(f.correct_assignment), accept: (f.accept_assignments ?? []).map(idx) };
      for (const a of [exp.assign, ...exp.accept]) { tests++; if (R.checkGrid(exp, { grid: a }).correct !== true) bad.push('rejects solution'); }
      const ch = [...exp.assign]; [ch[0], ch[1]] = [ch[1], ch[0]];
      if (![exp.assign, ...exp.accept].some((a: number[]) => same(a, ch))) { tests++; if (R.checkGrid(exp, { grid: ch }).correct !== false) bad.push('accepts swapped rows'); }
    } else if (t === 'truth_table') {
      const tb = (v: string) => v === 'T';
      const values = f.correct.map((r: string[]) => r.map(tb));
      const exp = { values };
      tests++; if (R.checkTruthTable(exp, { table: f.correct }).correct !== true) bad.push('rejects key (T/F)');
      tests++; if (R.checkTruthTable(exp, { table: values.map((r: boolean[]) => r.map((v) => (v ? '1' : '0'))) }).correct !== true) bad.push('rejects 1/0');
      const flip = values.map((r: boolean[]) => [...r]); flip[0][0] = !flip[0][0];
      tests++; if (R.checkTruthTable(exp, { table: flip }).correct !== false) bad.push('accepts flipped cell');
    } else if (t === 'mark') {
      const exp = { marks: f.correct_marks, accept: f.accept_marks };
      for (const m of [f.correct_marks, ...(f.accept_marks ?? [])]) { tests++; if (R.checkMark(exp, { marks: m }).correct !== true) bad.push('rejects key'); }
      tests++; if (R.checkMark(exp, { marks: [...f.correct_marks].reverse() }).correct !== true) bad.push('rejects reordered marks');
      if (f.correct_marks.length > 1) { tests++; if (R.checkMark(exp, { marks: f.correct_marks.slice(1) }).correct !== false) bad.push('accepts a missing mark'); }
    } else if (t === 'values') {
      const fields = f.fields;
      const exp = { rule: f.rule, example: f.example_answer };
      const str = (o: any) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, String(v)]));
      tests++; if (R.checkValues(exp, { values: str(f.example_answer) }, fields).correct !== true) bad.push('rejects its example');
      for (const w of q.wrong_values_rejected ?? []) { tests++; if (R.checkValues(exp, { values: str(w) }, fields).correct !== false) bad.push('accepts wrong ' + JSON.stringify(w)); }
    } else continue;
    rows.push({ id: q.id, type: t, tests, bad });
  }
  writeFileSync(process.argv[3], JSON.stringify(rows, null, 1));
  console.error(`checked ${rows.length} questions, ${rows.reduce((a, r) => a + r.tests, 0)} responses; problems in ${rows.filter((r) => r.bad.length).length}`);
}
main();
