# Math Lab Video Assignment System

An Edpuzzle-style video assignment system for Developing Educators' Math Lab
classes, built as a Google Apps Script app that embeds in a Google Site.
Full background and requirements: the original build brief this repo
implements is Branch 1 of a 3-branch plan (see `docs/ARCHITECTURE.md`).

**Not a Node/web app you `npm run` in production** — Apps Script runs the
`apps-script/` files directly inside Google's own runtime. This repo exists
for version control, review, and testable logic; deployment is manual
copy/paste (or `clasp push`) into an actual Apps Script project. Start with
**[`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md)** for exact, non-programmer,
click-by-click setup instructions.

## What's here

```
apps-script/           The actual application (push/copy this into Apps Script)
  appsscript.json         Web app manifest
  Code.js                 doGet router + client-callable API surface
  Config.js               Layered config: code defaults < Config sheet < Script Properties
  SheetService.js         Videos/Responses sheet schema, current-work grouping, completion lookups
  Ingestion.js            YouTube polling + title parsing (the "never touch it again" engine)
  Dashboard.js            Teacher dashboard passcode gate + filtered response queries
  Utils.js                School-year labeling shared by ingestion and responses
  StudentApp.html/.js/.css   Student-facing SPA (grade -> current work -> watch -> respond)
  DashboardApp.html/.js/.css Teacher dashboard SPA
test/                   Node-runnable unit tests for the pure title-parsing and school-year logic
docs/
  DEPLOYMENT.md            Step-by-step non-programmer setup
  ARCHITECTURE.md          Core engine vs. branches, data flow, why Apps Script
  OPEN_ITEMS.md            Assumptions made + the brief's own unresolved item
```

## Title convention (what makes ingestion automatic)

Only titles matching these exact patterns are ingested; everything else
(Shorts, unrelated uploads, typos) is silently ignored:

- `{6 or 7}th Grade {Teach|Do|Home} {Number}` — e.g. `7th Grade Do 2`
- `MAP Practice {Number}` — e.g. `MAP Practice 3`

See `apps-script/Ingestion.js` (`parseVideoTitle`) and `test/parseTitle.test.js`
for the exact, tested behavior.

## Running the tests

```
npm test
```

This only exercises the pure title-parsing logic (`parseVideoTitle`) — the
sheet/YouTube/HTML pieces run inside the Apps Script runtime and are
exercised manually per `docs/DEPLOYMENT.md` Part 4 (`ingestNewVideos`) after
deployment, since they depend on Apps Script services (`SpreadsheetApp`,
`UrlFetchApp`, `PropertiesService`) that don't exist outside of it.

## Key design decisions worth knowing before you read the code

- **Watch enforcement is entirely client-side**, tracking the furthest
  position actually reached in the current page session and snapping back
  any seek attempt beyond it; a refresh resets progress (deliberately - see
  `docs/OPEN_ITEMS.md` item 7). The server never re-verifies playback, same
  trust model as the Google Form it replaces.
- **No login system.** Students identify with First Name + Last Initial and a
  period, exactly in spirit to the old Form; teachers use a single shared
  dashboard passcode. This matches the brief's "no accounts, no public
  profiles" school-safe philosophy. See `docs/OPEN_ITEMS.md` items 4–5 for
  the tradeoffs.
- **Soft "official" tagging, not hard access control.** The app stays public
  (one deployment, no split into class-only vs. public versions yet). An
  optional shared `STUDENT_PASSCODE` lets real students self-identify without
  blocking anyone else from using the app; every response is tagged
  `Official: TRUE/FALSE` server-side based on whether it matched, and the
  dashboard defaults to official-only with a toggle to see everything. See
  `docs/OPEN_ITEMS.md` for why this is soft by design.
- **Every video and response is tagged with a school year** (e.g.
  `2025-2026`), derived automatically from its date — never entered by hand —
  so a repeated student name in a future year can never inherit a prior
  year's completion status.
- **"Current work" window is configurable, not hard-coded** — edit the
  `Config` sheet's `CURRENT_PROBLEM_WINDOW` / `CURRENT_MAP_WINDOW` rows any
  time, no code change needed.
- **No hard-coded assumptions about daily video counts, grade parity, or a
  playlist.** The app is the entire navigation layer, built purely from
  individually embedded YouTube videos, per the brief's district-filtering
  constraint.
