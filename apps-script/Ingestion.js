/**
 * Ingestion.js
 *
 * The "never touch the app again" half of the system. A time-driven trigger
 * calls ingestNewVideos() every INGEST_POLL_MINUTES. It:
 *   1. Resolves (once, then caches) the channel's uploads playlist ID.
 *   2. Pages through that playlist's most recent items.
 *   3. Parses each title against the rigid Math Lab convention.
 *   4. Ignores anything that doesn't match exactly (this is also how Shorts
 *      and unrelated uploads get excluded - they never carry a matching title).
 *   5. Appends newly-seen, matching videos to the Videos sheet.
 *
 * parseVideoTitle() is pure and exported for Node-side unit testing (see
 * test/parseTitle.test.js); the `module` guard at the bottom is a no-op
 * inside the Apps Script runtime, where `module` is undefined.
 */

var GRADE_TITLE_PATTERN = /^([67])th Grade (Teach|Do|Home)\s+(\d+)$/i;
var MAP_TITLE_PATTERN = /^MAP Practice\s+(\d+)$/i;

/**
 * Parses a YouTube title against the Math Lab naming convention.
 * Returns null for anything that doesn't match exactly (Shorts, unrelated
 * uploads, typos) - by design, non-matching titles are simply ignored.
 */
function parseVideoTitle(rawTitle) {
  var title = String(rawTitle || '').trim().replace(/\s+/g, ' ');

  var gradeMatch = title.match(GRADE_TITLE_PATTERN);
  if (gradeMatch) {
    var type = gradeMatch[2];
    // Normalize capitalization (Teach/Do/Home) regardless of source casing.
    type = type.charAt(0).toUpperCase() + type.slice(1).toLowerCase();
    return {
      kind: 'grade',
      grade: Number(gradeMatch[1]),
      type: type,
      number: Number(gradeMatch[3])
    };
  }

  var mapMatch = title.match(MAP_TITLE_PATTERN);
  if (mapMatch) {
    return {
      kind: 'map',
      grade: null,
      type: 'MAP',
      number: Number(mapMatch[1])
    };
  }

  return null;
}

/** Resolves and caches the channel ID + uploads playlist ID from the configured handle. */
function resolveChannelUploadsPlaylist_() {
  var config = getConfig();
  if (config.YOUTUBE_UPLOADS_PLAYLIST_ID) return config.YOUTUBE_UPLOADS_PLAYLIST_ID;

  var apiKey = config.YOUTUBE_API_KEY;
  if (!apiKey) throw new Error('YOUTUBE_API_KEY script property is not set. See docs/DEPLOYMENT.md.');

  var handle = (config.YOUTUBE_CHANNEL_HANDLE || '@developingeducators').replace(/^@/, '');
  var url = 'https://www.googleapis.com/youtube/v3/channels'
    + '?part=contentDetails&forHandle=' + encodeURIComponent(handle)
    + '&key=' + encodeURIComponent(apiKey);

  var response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  var body = JSON.parse(response.getContentText());
  if (!body.items || !body.items.length) {
    throw new Error('Could not resolve YouTube channel for handle @' + handle + ': ' + response.getContentText());
  }
  var uploadsPlaylistId = body.items[0].contentDetails.relatedPlaylists.uploads;
  setScriptProp_('YOUTUBE_CHANNEL_ID', body.items[0].id);
  setScriptProp_('YOUTUBE_UPLOADS_PLAYLIST_ID', uploadsPlaylistId);
  return uploadsPlaylistId;
}

/**
 * Fetches recent uploads-playlist items. Only pages back far enough to reach
 * already-seen videos (or a hard cap), so steady-state polls are cheap.
 */
function fetchRecentUploads_(playlistId, apiKey, existingIds) {
  var results = [];
  var pageToken = '';
  var maxPages = 5; // hard cap: 5 x 50 = 250 most-recent items per poll, plenty of headroom
  for (var page = 0; page < maxPages; page++) {
    var url = 'https://www.googleapis.com/youtube/v3/playlistItems'
      + '?part=snippet&maxResults=50&playlistId=' + encodeURIComponent(playlistId)
      + '&key=' + encodeURIComponent(apiKey)
      + (pageToken ? '&pageToken=' + encodeURIComponent(pageToken) : '');
    var response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
    var body = JSON.parse(response.getContentText());
    if (!body.items) break;

    var reachedKnown = false;
    body.items.forEach(function (item) {
      var videoId = item.snippet.resourceId.videoId;
      results.push({
        videoId: videoId,
        title: item.snippet.title,
        publishedAt: item.snippet.publishedAt
      });
      if (existingIds[videoId]) reachedKnown = true;
    });

    if (reachedKnown || !body.nextPageToken) break;
    pageToken = body.nextPageToken;
  }
  return results;
}

/**
 * Main entry point, called by the installed time-driven trigger (and safe to
 * run manually from the Apps Script editor at any time).
 */
function ingestNewVideos() {
  var config = getConfig();
  var apiKey = config.YOUTUBE_API_KEY;
  if (!apiKey) {
    Logger.log('ingestNewVideos: YOUTUBE_API_KEY not set, skipping.');
    return { ingested: 0, skipped: 0 };
  }

  var playlistId = resolveChannelUploadsPlaylist_();
  var existingIds = getExistingVideoIds_();
  var uploads = fetchRecentUploads_(playlistId, apiKey, existingIds);

  var toIngest = [];
  var skipped = 0;
  uploads.forEach(function (upload) {
    if (existingIds[upload.videoId]) return;
    var parsed = parseVideoTitle(upload.title);
    if (!parsed) {
      skipped++;
      return;
    }
    toIngest.push({
      videoId: upload.videoId,
      kind: parsed.kind,
      grade: parsed.grade,
      type: parsed.type,
      number: parsed.number,
      title: upload.title,
      publishedAt: upload.publishedAt
    });
  });

  var ingested = appendVideos_(toIngest);
  Logger.log('ingestNewVideos: ingested=' + ingested + ' skipped=' + skipped);
  return { ingested: ingested, skipped: skipped };
}

/**
 * Run once from the Apps Script editor after setting YOUTUBE_API_KEY to
 * install the recurring poll. Safe to re-run - it clears prior triggers for
 * this function first so it never double-installs.
 */
function setupIngestionTrigger() {
  var config = getConfig();
  var minutes = Number(config.INGEST_POLL_MINUTES) || 15;

  ScriptApp.getProjectTriggers().forEach(function (trigger) {
    if (trigger.getHandlerFunction() === 'ingestNewVideos') {
      ScriptApp.deleteTrigger(trigger);
    }
  });

  ScriptApp.newTrigger('ingestNewVideos')
    .timeBased()
    .everyMinutes(minutes >= 30 ? 30 : (minutes >= 15 ? 15 : (minutes >= 10 ? 10 : 5)))
    .create();

  Logger.log('Ingestion trigger installed (~every ' + minutes + ' minutes).');
}

if (typeof module !== 'undefined') {
  module.exports = { parseVideoTitle: parseVideoTitle };
}
