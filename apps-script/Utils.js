/**
 * Utils.js
 *
 * Small pure helpers shared across the engine. Kept dependency-free (no
 * Apps Script services) so they can be unit-tested with plain Node - see
 * test/schoolYear.test.js.
 */

/**
 * Labels a date with the school year it falls in, e.g. Sept 2025 -> "2025-2026",
 * and March 2026 -> "2025-2026". The school year is assumed to start in August;
 * adjust the cutover month below if your district's year starts elsewhere.
 */
function getSchoolYearLabel_(date) {
  date = date instanceof Date ? date : new Date(date);
  var year = date.getFullYear();
  var month = date.getMonth(); // 0 = January ... 7 = August
  var SCHOOL_YEAR_START_MONTH = 7; // August
  var startYear = month >= SCHOOL_YEAR_START_MONTH ? year : year - 1;
  return startYear + '-' + (startYear + 1);
}

/** The school year label for right now - used to tag new responses. */
function getCurrentSchoolYear_() {
  return getSchoolYearLabel_(new Date());
}

if (typeof module !== 'undefined') {
  module.exports = { getSchoolYearLabel_: getSchoolYearLabel_ };
}
