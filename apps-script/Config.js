/**
 * Config.js
 *
 * Two layers of configuration:
 *  - Script Properties: secrets / deployment-specific values (API key, channel handle,
 *    dashboard passcode, optional student passcode). Set once in the Apps Script editor under
 *    Project Settings > Script Properties. Never stored in the spreadsheet.
 *  - "Config" sheet: tunable behavior a teacher might reasonably want to change
 *    without touching code (e.g. how many problem numbers count as "current").
 *    Read fresh every time (cheap - it's a handful of rows) so edits take effect
 *    without redeploying.
 */

var CONFIG_DEFAULTS = {
  YOUTUBE_CHANNEL_HANDLE: '@developingeducators',
  CURRENT_PROBLEM_WINDOW: '2',   // how many most-recent problem Numbers count as "current work" per grade
  CURRENT_MAP_WINDOW: '1',       // how many most-recent MAP Practice numbers count as "current work"
  MAP_SHARED_ACROSS_GRADES: 'true', // MAP naming has no grade token; see docs/OPEN_ITEMS.md
  INGEST_POLL_MINUTES: '15',
  DASHBOARD_PASSCODE: '',          // blank = dashboard prompts to set one on first visit
  PERIODS: 'Period 2 Even,Period 3 Even', // edit the Config sheet row to match your actual schedule
  STUDENT_PASSCODE: ''             // optional; blank = no response can be tagged "official" yet
};

function getScriptProp_(key) {
  return PropertiesService.getScriptProperties().getProperty(key);
}

function setScriptProp_(key, value) {
  PropertiesService.getScriptProperties().setProperty(key, value);
}

/**
 * Returns the effective config as a plain object, layering:
 * CONFIG_DEFAULTS < Config sheet rows < Script Properties (for secrets only).
 */
function getConfig() {
  var config = {};
  for (var key in CONFIG_DEFAULTS) {
    config[key] = CONFIG_DEFAULTS[key];
  }

  var sheet = getOrCreateConfigSheet_();
  var values = sheet.getDataRange().getValues();
  for (var i = 1; i < values.length; i++) {
    var k = values[i][0];
    var v = values[i][1];
    if (k) config[String(k).trim()] = v;
  }

  // Secrets always come from Script Properties, never the sheet.
  var apiKey = getScriptProp_('YOUTUBE_API_KEY');
  if (apiKey) config.YOUTUBE_API_KEY = apiKey;

  var passcode = getScriptProp_('DASHBOARD_PASSCODE');
  if (passcode) config.DASHBOARD_PASSCODE = passcode;

  var studentPasscode = getScriptProp_('STUDENT_PASSCODE');
  if (studentPasscode) config.STUDENT_PASSCODE = studentPasscode;

  var channelId = getScriptProp_('YOUTUBE_CHANNEL_ID');
  if (channelId) config.YOUTUBE_CHANNEL_ID = channelId;

  var uploadsPlaylistId = getScriptProp_('YOUTUBE_UPLOADS_PLAYLIST_ID');
  if (uploadsPlaylistId) config.YOUTUBE_UPLOADS_PLAYLIST_ID = uploadsPlaylistId;

  return config;
}

function getOrCreateConfigSheet_() {
  var ss = getDatabaseSpreadsheet_();
  var sheet = ss.getSheetByName('Config');
  if (!sheet) {
    sheet = ss.insertSheet('Config');
    sheet.appendRow(['Key', 'Value', 'Notes']);
    sheet.appendRow(['CURRENT_PROBLEM_WINDOW', CONFIG_DEFAULTS.CURRENT_PROBLEM_WINDOW,
      'How many recent problem numbers show as "current work" per grade.']);
    sheet.appendRow(['CURRENT_MAP_WINDOW', CONFIG_DEFAULTS.CURRENT_MAP_WINDOW,
      'How many recent MAP Practice numbers show as "current work".']);
    sheet.appendRow(['MAP_SHARED_ACROSS_GRADES', CONFIG_DEFAULTS.MAP_SHARED_ACROSS_GRADES,
      'MAP Practice titles carry no grade token; true = show same MAP list to both grades.']);
    sheet.appendRow(['INGEST_POLL_MINUTES', CONFIG_DEFAULTS.INGEST_POLL_MINUTES,
      'How often the ingestion trigger checks YouTube for new uploads.']);
    sheet.appendRow(['PERIODS', CONFIG_DEFAULTS.PERIODS,
      'Comma-separated list of period names shown on the student name/period screen.']);
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, 3);
  }
  return sheet;
}

/**
 * The single spreadsheet that acts as this app's database. Created (or found)
 * lazily and its ID cached in Script Properties so every code path uses the
 * same file even if it's ever moved within Drive.
 */
function getDatabaseSpreadsheet_() {
  var id = getScriptProp_('DATABASE_SPREADSHEET_ID');
  if (id) {
    try {
      return SpreadsheetApp.openById(id);
    } catch (e) {
      // Fall through and recreate if the stored ID is no longer valid.
    }
  }
  var ss = SpreadsheetApp.create('Math Lab Video System - Database');
  setScriptProp_('DATABASE_SPREADSHEET_ID', ss.getId());
  return ss;
}
