/**
 * SheetService.js
 *
 * Owns the two data sheets that make up the "core engine" state:
 *   Videos    - one row per ingested YouTube video (the auto-built playlist replacement)
 *   Responses - one row per submitted student response (replaces the Google Form responses)
 *
 * Kept deliberately dumb: plain rows, no formulas, so a teacher can open the
 * spreadsheet directly and it reads like the old Form responses tab.
 */

var VIDEOS_HEADERS = [
  'VideoId', 'Kind', 'Grade', 'Type', 'Number', 'Title', 'PublishedAt', 'IngestedAt'
];

var RESPONSES_HEADERS = [
  'Timestamp', 'FirstName', 'Period', 'Grade', 'VideoType', 'VideoNumber',
  'VideoTitle', 'VideoId', 'MainAnswer', 'UnderstandConfirmation', 'Completed'
];

// Teach/Do/Home should always group and display in this order under a problem number.
var TYPE_ORDER = { 'Teach': 0, 'Do': 1, 'Home': 2 };

function getOrCreateSheet_(name, headers) {
  var ss = getDatabaseSpreadsheet_();
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(headers);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function getVideosSheet_() {
  return getOrCreateSheet_('Videos', VIDEOS_HEADERS);
}

function getResponsesSheet_() {
  return getOrCreateSheet_('Responses', RESPONSES_HEADERS);
}

/** Reads the full Videos sheet into an array of plain objects. */
function readAllVideos_() {
  var sheet = getVideosSheet_();
  var lastRow = sheet.getLastRow();
  if (lastRow < 2) return [];
  var values = sheet.getRange(2, 1, lastRow - 1, VIDEOS_HEADERS.length).getValues();
  return values.map(function (row) {
    var obj = {};
    VIDEOS_HEADERS.forEach(function (h, i) { obj[h] = row[i]; });
    return obj;
  });
}

/** Returns the set of VideoIds already ingested, for fast dedupe. */
function getExistingVideoIds_() {
  var sheet = getVideosSheet_();
  var lastRow = sheet.getLastRow();
  var ids = {};
  if (lastRow < 2) return ids;
  var col = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  col.forEach(function (r) { if (r[0]) ids[r[0]] = true; });
  return ids;
}

/** Appends newly-ingested, already-parsed video records. Skips duplicates defensively. */
function appendVideos_(records) {
  if (!records || !records.length) return 0;
  var sheet = getVideosSheet_();
  var existing = getExistingVideoIds_();
  var rows = [];
  var now = new Date();
  records.forEach(function (rec) {
    if (existing[rec.videoId]) return;
    existing[rec.videoId] = true;
    rows.push([
      rec.videoId,
      rec.kind,
      rec.grade || '',
      rec.type || '',
      rec.number,
      rec.title,
      rec.publishedAt,
      now
    ]);
  });
  if (rows.length) {
    sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, VIDEOS_HEADERS.length).setValues(rows);
  }
  return rows.length;
}

function sortByNumberThenType_(a, b) {
  if (a.Number !== b.Number) return a.Number - b.Number;
  var ta = TYPE_ORDER[a.Type] != null ? TYPE_ORDER[a.Type] : 99;
  var tb = TYPE_ORDER[b.Type] != null ? TYPE_ORDER[b.Type] : 99;
  return ta - tb;
}

/**
 * Builds the "current work" view for a grade:
 *   - the N most recent problem Numbers (grade-specific Teach/Do/Home videos)
 *   - the M most recent MAP Practice numbers (shared across grades unless configured otherwise)
 * N and M come from the Config sheet so a teacher can widen/narrow the window
 * without a code change.
 */
function getGradeHome(grade) {
  grade = Number(grade);
  var config = getConfig();
  var problemWindow = Number(config.CURRENT_PROBLEM_WINDOW) || 2;
  var mapWindow = Number(config.CURRENT_MAP_WINDOW) || 1;
  var mapShared = String(config.MAP_SHARED_ACROSS_GRADES) !== 'false';

  var all = readAllVideos_();
  var gradeVideos = all.filter(function (v) { return v.Kind === 'grade' && Number(v.Grade) === grade; });
  var mapVideos = all.filter(function (v) {
    if (v.Kind !== 'map') return false;
    return mapShared || Number(v.Grade) === grade;
  });

  var problemNumbers = uniqueSortedNumbers_(gradeVideos);
  var currentProblemNumbers = problemNumbers.slice(-problemWindow);
  var currentProblems = currentProblemNumbers.map(function (num) {
    var items = gradeVideos.filter(function (v) { return v.Number === num; }).sort(sortByNumberThenType_);
    return { number: num, videos: items.map(toClientVideo_) };
  });

  var mapNumbers = uniqueSortedNumbers_(mapVideos);
  var currentMapNumbers = mapNumbers.slice(-mapWindow);
  var currentMap = currentMapNumbers.map(function (num) {
    return mapVideos.filter(function (v) { return v.Number === num; }).map(toClientVideo_);
  }).reduce(function (acc, arr) { return acc.concat(arr); }, []);

  return {
    grade: grade,
    problems: currentProblems,
    mapPractice: currentMap,
    pastAvailable: problemNumbers.length > currentProblemNumbers.length || mapNumbers.length > currentMapNumbers.length
  };
}

function uniqueSortedNumbers_(videos) {
  var set = {};
  videos.forEach(function (v) { set[v.Number] = true; });
  return Object.keys(set).map(Number).sort(function (a, b) { return a - b; });
}

function toClientVideo_(v) {
  return {
    videoId: v.VideoId,
    kind: v.Kind,
    grade: v.Grade,
    type: v.Type,
    number: v.Number,
    title: v.Title,
    publishedAt: v.PublishedAt instanceof Date ? v.PublishedAt.toISOString() : v.PublishedAt
  };
}

/**
 * Everything not in the "current work" window, for the Past Videos / Search screen.
 * grade: 6, 7, or 'map' to fetch only MAP Practice entries.
 */
function getPastVideos(grade) {
  var all = readAllVideos_();
  var config = getConfig();
  var problemWindow = Number(config.CURRENT_PROBLEM_WINDOW) || 2;
  var mapWindow = Number(config.CURRENT_MAP_WINDOW) || 1;
  var mapShared = String(config.MAP_SHARED_ACROSS_GRADES) !== 'false';

  var mapVideos = all.filter(function (v) { return v.Kind === 'map'; });
  var mapNumbers = uniqueSortedNumbers_(mapVideos);
  var currentMapNumbers = mapNumbers.slice(-mapWindow);

  if (grade === 'map') {
    var past = mapVideos.filter(function (v) { return currentMapNumbers.indexOf(v.Number) === -1; });
    return past.sort(sortByNumberThenType_).reverse().map(toClientVideo_);
  }

  grade = Number(grade);
  var gradeProblemVideos = all.filter(function (v) { return v.Kind === 'grade' && Number(v.Grade) === grade; });
  var problemNumbers = uniqueSortedNumbers_(gradeProblemVideos);
  var currentProblemNumbers = problemNumbers.slice(-problemWindow);
  var pastProblems = gradeProblemVideos.filter(function (v) { return currentProblemNumbers.indexOf(v.Number) === -1; });

  var relevantMap = mapVideos.filter(function (v) { return mapShared || Number(v.Grade) === grade; });
  var pastMap = relevantMap.filter(function (v) { return currentMapNumbers.indexOf(v.Number) === -1; });

  return pastProblems.concat(pastMap).sort(sortByNumberThenType_).reverse().map(toClientVideo_);
}

function normalizeKey_(s) {
  return String(s || '').trim().toLowerCase();
}

/**
 * Which of this student's currently-visible videos already have a submitted response.
 * Matched by (FirstName, Period, VideoId) - the same identity the original
 * Google Form relied on (no login system in v1).
 */
function getCompletionSet(firstName, period) {
  var sheet = getResponsesSheet_();
  var lastRow = sheet.getLastRow();
  var result = {};
  if (lastRow < 2) return result;
  var values = sheet.getRange(2, 1, lastRow - 1, RESPONSES_HEADERS.length).getValues();
  var fnKey = normalizeKey_(firstName);
  var pKey = normalizeKey_(period);
  values.forEach(function (row) {
    var rowFn = normalizeKey_(row[1]);
    var rowP = normalizeKey_(row[2]);
    if (rowFn === fnKey && rowP === pKey) {
      result[row[7]] = true; // VideoId column
    }
  });
  return result;
}

/**
 * Records one student response. Called only after the client has enforced
 * genuine watch-to-end for this session; server does not re-verify playback,
 * matching the original Form's trust model.
 */
function submitResponse(payload) {
  if (!payload || !payload.videoId || !payload.firstName || !payload.period) {
    throw new Error('Missing required response fields.');
  }
  var sheet = getResponsesSheet_();
  sheet.appendRow([
    new Date(),
    String(payload.firstName).trim(),
    String(payload.period).trim(),
    payload.grade || '',
    payload.videoType || '',
    payload.videoNumber != null ? payload.videoNumber : '',
    payload.videoTitle || '',
    payload.videoId,
    payload.mainAnswer || '',
    payload.understandConfirmation || '',
    'Yes'
  ]);
  return { ok: true };
}

/** All responses, for the teacher dashboard. */
function getAllResponses() {
  var sheet = getResponsesSheet_();
  var lastRow = sheet.getLastRow();
  if (lastRow < 2) return [];
  var values = sheet.getRange(2, 1, lastRow - 1, RESPONSES_HEADERS.length).getValues();
  return values.map(function (row) {
    var obj = {};
    RESPONSES_HEADERS.forEach(function (h, i) {
      var v = row[i];
      obj[h] = v instanceof Date ? v.toISOString() : v;
    });
    return obj;
  });
}
