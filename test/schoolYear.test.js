const test = require('node:test');
const assert = require('node:assert/strict');
const { getSchoolYearLabel_ } = require('../apps-script/Utils.js');

test('dates from August through December fall in the year starting that year', () => {
  assert.equal(getSchoolYearLabel_(new Date(2025, 7, 1)), '2025-2026');  // Aug 1, 2025
  assert.equal(getSchoolYearLabel_(new Date(2025, 8, 15)), '2025-2026'); // Sept 15, 2025
  assert.equal(getSchoolYearLabel_(new Date(2025, 11, 20)), '2025-2026'); // Dec 20, 2025
});

test('dates from January through July fall in the school year that started the prior calendar year', () => {
  assert.equal(getSchoolYearLabel_(new Date(2026, 0, 5)), '2025-2026');  // Jan 5, 2026
  assert.equal(getSchoolYearLabel_(new Date(2026, 5, 10)), '2025-2026'); // June 10, 2026
  assert.equal(getSchoolYearLabel_(new Date(2026, 6, 31)), '2025-2026'); // July 31, 2026
});

test('the cutover happens exactly at the start of August', () => {
  assert.equal(getSchoolYearLabel_(new Date(2026, 6, 31)), '2025-2026');
  assert.equal(getSchoolYearLabel_(new Date(2026, 7, 1)), '2026-2027');
});

test('accepts a date string or Date object', () => {
  assert.equal(getSchoolYearLabel_('2025-09-01T12:00:00'), '2025-2026');
});
