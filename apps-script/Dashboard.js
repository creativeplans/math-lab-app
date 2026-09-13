/**
 * Dashboard.js
 *
 * The teacher-facing side of the core engine. Deliberately lightweight:
 * a single shared passcode (set in Script Properties, see docs/DEPLOYMENT.md)
 * gates the dashboard page rather than a full login system, matching the
 * "no accounts, no public profiles" school-safe philosophy. The real access
 * boundary is the web app's own "who has access" deployment setting - the
 * passcode is a light deterrent for a link that may get shared informally,
 * not a security control on its own. See docs/OPEN_ITEMS.md.
 */

function checkDashboardPasscode(passcode) {
  var config = getConfig();
  var expected = config.DASHBOARD_PASSCODE;
  if (!expected) {
    // No passcode configured yet: fail closed and tell the caller so the UI
    // can point the teacher at docs/DEPLOYMENT.md instead of granting access.
    return { ok: false, reason: 'NOT_CONFIGURED' };
  }
  return { ok: String(passcode) === String(expected) };
}

function getFilteredResponses(passcode, filters) {
  var check = checkDashboardPasscode(passcode);
  if (!check.ok) {
    throw new Error('Invalid dashboard passcode.');
  }

  filters = filters || {};
  var rows = getAllResponses();

  // Default view is "official" responses only (passcode matched at submit time).
  // Rows recorded before the Official column existed have no explicit value
  // and are treated as official too, so existing data doesn't vanish from the
  // dashboard the moment this feature ships. Pass filters.showAll to see everything.
  if (!filters.showAll) {
    rows = rows.filter(function (r) { return r.Official !== false; });
  }

  if (filters.grade) {
    rows = rows.filter(function (r) { return String(r.Grade) === String(filters.grade); });
  }
  if (filters.period) {
    rows = rows.filter(function (r) { return String(r.Period) === String(filters.period); });
  }
  if (filters.videoType) {
    rows = rows.filter(function (r) { return String(r.VideoType) === String(filters.videoType); });
  }
  if (filters.student) {
    var needle = String(filters.student).trim().toLowerCase();
    rows = rows.filter(function (r) { return String(r.FirstName).toLowerCase().indexOf(needle) !== -1; });
  }
  if (filters.dateFrom) {
    var from = new Date(filters.dateFrom).getTime();
    rows = rows.filter(function (r) { return new Date(r.Timestamp).getTime() >= from; });
  }
  if (filters.dateTo) {
    var to = new Date(filters.dateTo).getTime();
    rows = rows.filter(function (r) { return new Date(r.Timestamp).getTime() <= to; });
  }
  if (filters.completion) {
    rows = rows.filter(function (r) { return String(r.Completed) === String(filters.completion); });
  }

  rows.sort(function (a, b) { return new Date(b.Timestamp) - new Date(a.Timestamp); });
  return rows;
}
