const test = require('node:test');
const assert = require('node:assert/strict');
const { parseVideoTitle } = require('../apps-script/Ingestion.js');

test('parses grade Teach/Do/Home titles from the channel examples', () => {
  assert.deepEqual(parseVideoTitle('7th Grade Teach 1'), { kind: 'grade', grade: 7, type: 'Teach', number: 1 });
  assert.deepEqual(parseVideoTitle('7th Grade Do 1'), { kind: 'grade', grade: 7, type: 'Do', number: 1 });
  assert.deepEqual(parseVideoTitle('7th Grade Home 1'), { kind: 'grade', grade: 7, type: 'Home', number: 1 });
  assert.deepEqual(parseVideoTitle('7th Grade Teach 2'), { kind: 'grade', grade: 7, type: 'Teach', number: 2 });
  assert.deepEqual(parseVideoTitle('6th Grade Do 2'), { kind: 'grade', grade: 6, type: 'Do', number: 2 });
  assert.deepEqual(parseVideoTitle('6th Grade Home 2'), { kind: 'grade', grade: 6, type: 'Home', number: 2 });
});

test('parses MAP Practice titles', () => {
  assert.deepEqual(parseVideoTitle('MAP Practice 1'), { kind: 'map', grade: null, type: 'MAP', number: 1 });
  assert.deepEqual(parseVideoTitle('MAP Practice 12'), { kind: 'map', grade: null, type: 'MAP', number: 12 });
});

test('is tolerant of stray whitespace and casing but not of altered wording', () => {
  assert.deepEqual(parseVideoTitle('  7th Grade   Teach   3  '), { kind: 'grade', grade: 7, type: 'Teach', number: 3 });
  assert.deepEqual(parseVideoTitle('7th grade teach 3'), { kind: 'grade', grade: 7, type: 'Teach', number: 3 });
});

test('rejects the burned-in on-screen title card wording (must use metadata title)', () => {
  assert.equal(parseVideoTitle('7th Grade Content Practice Number 2 (Do)'), null);
});

test('ignores Shorts and unrelated uploads (anything not matching the exact pattern)', () => {
  assert.equal(parseVideoTitle('Quick math tip! #shorts'), null);
  assert.equal(parseVideoTitle('Welcome to Developing Educators'), null);
  assert.equal(parseVideoTitle('8th Grade Teach 1'), null); // out-of-range grade
  assert.equal(parseVideoTitle('7th Grade Test 1'), null); // wrong type token
  assert.equal(parseVideoTitle(''), null);
  assert.equal(parseVideoTitle(null), null);
});
