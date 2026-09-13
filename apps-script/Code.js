/**
 * Code.js
 *
 * Web app entry point. One deployment serves both front ends:
 *   (no page param)   -> student app (Branch 1: Math Lab)
 *   ?page=dashboard   -> teacher dashboard
 *
 * Kept as a thin router; all real logic lives in SheetService.js,
 * Ingestion.js, Dashboard.js and Config.js so future branches (Branch 2/3)
 * can add their own doGet-routed pages against the same core engine without
 * touching this file's existing routes.
 */

function doGet(e) {
  var page = (e && e.parameter && e.parameter.page) || 'student';

  var template;
  if (page === 'dashboard') {
    template = HtmlService.createTemplateFromFile('DashboardApp');
  } else {
    template = HtmlService.createTemplateFromFile('StudentApp');
  }

  return template.evaluate()
    .setTitle('Math Lab' + (page === 'dashboard' ? ' - Dashboard' : ''))
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/** Used by HTML templates to inline shared CSS/JS files: <?!= include('StudentStyles'); ?> */
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

// ---- Client-callable server API (google.script.run) ----------------------
// Thin wrappers so the client only ever calls through this file, even though
// implementations live in SheetService.js / Dashboard.js.

function api_getPeriods() {
  var config = getConfig();
  return String(config.PERIODS || '').split(',').map(function (s) { return s.trim(); }).filter(Boolean);
}

function api_getGradeHome(grade) {
  return getGradeHome(grade);
}

function api_getPastVideos(grade) {
  return getPastVideos(grade);
}

function api_getCompletionSet(firstName, period) {
  return getCompletionSet(firstName, period);
}

function api_submitResponse(payload) {
  return submitResponse(payload);
}

function api_checkDashboardPasscode(passcode) {
  return checkDashboardPasscode(passcode);
}

function api_getResponses(passcode, filters) {
  return getFilteredResponses(passcode, filters);
}
