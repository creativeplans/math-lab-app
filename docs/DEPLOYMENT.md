# Deployment Guide (No Programming Required)

## Updating an already-deployed app (Fix Round 1)

If you've already deployed this app once and just want this round of fixes
live, you don't need to redo the whole guide below — just this:

1. Open your existing Apps Script project at **script.google.com**.
2. Add one new file: click **+** next to "Files" → **Script**, name it
   `Utils` (no `.gs`), and paste in `apps-script/Utils.js` from this repo.
3. For each of these existing files, open it, select all, delete, and paste
   in the new contents from the matching file in this repo's `apps-script/`
   folder (same filenames as before, nothing to rename):
   - `Config`
   - `SheetService`
   - `Dashboard`
   - `StudentApp` / `StudentStyles` / `StudentClient`
   - `DashboardApp` / `DashboardStyles` / `DashboardClient`
   (`Code`, `Ingestion`, and `appsscript.json` did not change this round —
   leave them as-is.)
4. Save (Ctrl/Cmd+S).
5. **Optional but needed for the new "official response" tagging**: click the
   gear icon (**Project Settings**) → **Script Properties** → **Add script
   property** → key `STUDENT_PASSCODE`, value = whatever word/phrase you want
   your real students to type (share it with your class directly - e.g. write
   it on the board). Leave this unset if you're not ready to use that feature
   yet; nothing else breaks either way.
6. Click **Deploy → Manage deployments**, click the pencil (edit) icon on
   your existing deployment, change **Version** to **New version**, click
   **Deploy**. This is the step that actually makes the fixes live at your
   existing URL — editing files alone does not.
7. Open your existing student link and confirm a Do/Home/MAP video's response
   now submits correctly (this was the main bug). Check the dashboard link
   too — it now defaults to showing only "official" responses, with a "Show
   all" checkbox to see everything (this will show everything until you set
   `STUDENT_PASSCODE` and start collecting new responses with it).

Nothing about your existing spreadsheet, video catalog, or past responses
changes or needs migrating — the new columns (Official, Basics Answer, School
Year) are added automatically the next time the app touches those sheets.

---

Follow the steps below in order, exactly as written, only if you're setting
this up **from scratch** for the first time. You will be copying and pasting
files into a Google Apps Script project, clicking a few buttons in Google Cloud
and YouTube, and pasting one embed link into your Google Site.

Do all of this **while signed in to the personal/Developing Educators Google
account** — this is what makes the app survive if the school account is ever
retired. You'll only touch the school account at the very end, to open the
finished link on school devices.

---

## Part 1 — Create the Apps Script project

1. Go to **script.google.com** (signed in as the Developing Educators account).
2. Click **New project**.
3. Click the project name at the top ("Untitled project") and rename it to
   **Math Lab Video System**.
4. You'll see one file, `Code.gs`, already open with some placeholder code.
   Delete the placeholder code inside it.

Now you'll re-create each file from this repository's `apps-script/` folder
inside that Apps Script project. For each `.js` file below, create a matching
**Script** file; for each `.html` file, create a matching **HTML** file.

### Create the script files
For each of these, click the **+** next to "Files" → **Script**, name it
exactly as shown (without `.gs`), and paste in the matching file's contents
from this repo's `apps-script/` folder:

- `Code` ← `apps-script/Code.js`
- `Config` ← `apps-script/Config.js`
- `SheetService` ← `apps-script/SheetService.js`
- `Ingestion` ← `apps-script/Ingestion.js`
- `Dashboard` ← `apps-script/Dashboard.js`
- `Utils` ← `apps-script/Utils.js`

(The very first file, `Code`, already exists — just paste into it instead of
creating a new one.)

### Create the HTML files
Click the **+** next to "Files" → **HTML**, name it exactly as shown (without
`.html`), and paste in the matching file's contents:

- `StudentApp` ← `apps-script/StudentApp.html`
- `StudentStyles` ← `apps-script/StudentStyles.html`
- `StudentClient` ← `apps-script/StudentClient.html`
- `DashboardApp` ← `apps-script/DashboardApp.html`
- `DashboardStyles` ← `apps-script/DashboardStyles.html`
- `DashboardClient` ← `apps-script/DashboardClient.html`

### Set the manifest
1. Click the gear icon (**Project Settings**) on the left.
2. Check **"Show appsscript.json manifest file in editor"**.
3. Go back to the editor (`<>` icon), open `appsscript.json`, delete its
   contents, and paste in this repo's `apps-script/appsscript.json`.
4. Click the save icon (or Ctrl/Cmd+S).

---

## Part 2 — Get a YouTube Data API key

This lets the app read your channel's uploads. It only needs read access.

1. In the Apps Script editor, click **Project Settings** (gear icon) and note
   the **Google Cloud Platform (GCP) Project Number** shown there — every
   Apps Script project has one automatically.
2. Go to **console.cloud.google.com**, make sure the project selector (top
   left, next to "Google Cloud") is set to your Apps Script project's
   auto-created project (search by the project number from step 1 if it's
   not obvious).
3. In the search bar, type **YouTube Data API v3** and open it, then click
   **Enable**.
4. Go to **APIs & Services → Credentials** → **Create Credentials** →
   **API key**.
5. Copy the key. Click **Restrict key**, and under "API restrictions" choose
   **Restrict key** → check only **YouTube Data API v3** → **Save**. This
   ensures the key can't be used for anything else if it ever leaks.

---

## Part 3 — Set the script properties (one-time secrets)

Back in the Apps Script editor:

1. Click **Project Settings** (gear icon).
2. Scroll to **Script Properties** → **Add script property**.
3. Add these properties:
   - `YOUTUBE_API_KEY` → paste the API key from Part 2.
   - `DASHBOARD_PASSCODE` → make up a passcode teachers will use to open the
     results dashboard (e.g. a short phrase). Anyone with this passcode can
     view student names and answers, so don't publish it — share it directly
     with teachers who need it.
   - `STUDENT_PASSCODE` (optional) → a word/phrase you give only to your real
     students (e.g. write it on the board). Responses submitted with it are
     tagged "official" and shown by default on the dashboard; anyone using
     the app without it (or with the wrong word) still gets the full app, but
     their response is tagged non-official and hidden from the dashboard's
     default view (there's a "Show all" checkbox to see it anyway). Leave
     this blank if you don't need to tell real students apart from other
     visitors yet — the app works the same either way.
4. Click **Save script properties**.

---

## Part 4 — Confirm the channel and run ingestion once

1. Back in the editor (`<>` icon), open the `Ingestion` file.
2. In the function dropdown at the top (next to the "Run" button), select
   **ingestNewVideos**.
3. Click **Run**. The first time, Google will ask you to authorize the
   script — click **Review permissions**, choose the Developing Educators
   account, click **Advanced** → **Go to Math Lab Video System (unsafe)**
   (this warning appears because the project isn't published to the public
   app store — that's expected and fine for an internal tool) → **Allow**.
4. Click **Run** again if it didn't run automatically after authorizing.
5. Click **Execution log** (or **View → Logs**) to confirm it printed
   something like `ingestNewVideos: ingested=18 skipped=3` — meaning it found
   and imported your existing correctly-titled videos.
   - If you see an error about `YOUTUBE_API_KEY`, re-check Part 3.
   - If you see an error resolving the channel handle, double-check the
     channel is `@developingeducators` (or update `YOUTUBE_CHANNEL_HANDLE` in
     the **Config** sheet — see Part 5 — if the handle ever changes).

### Install the automatic recurring check
1. Still with `Ingestion` selected, choose **setupIngestionTrigger** from the
   function dropdown and click **Run**.
2. Click the clock icon (**Triggers**) on the left to confirm a trigger now
   exists for `ingestNewVideos`, running on a time-driven schedule. From now
   on, new correctly-titled uploads are detected automatically — you never
   need to run anything manually again.

---

## Part 5 — Find and check the database spreadsheet

The first time any function ran, the app created a Google Sheet called
**"Math Lab Video System - Database"** in the Developing Educators account's
Drive (My Drive, root folder). Open Drive and find it — feel free to move it
into a folder, it'll still be found correctly.

It has three tabs:
- **Videos** — auto-filled by ingestion. Don't edit this by hand.
- **Responses** — auto-filled by student submissions. This is what the
  dashboard reads. You can review it directly here too, or filter/sort with
  Sheets' own tools if you prefer that to the dashboard. Includes a
  `SchoolYear` column (e.g. `2025-2026`, auto-derived from the submission
  date) and an `Official` column (`TRUE`/`FALSE`, based on whether the
  student's typed passcode matched `STUDENT_PASSCODE` when they submitted).
- **Config** — a few settings you're welcome to tweak any time, no code
  required:
  - `CURRENT_PROBLEM_WINDOW` — how many of the most recent problem numbers
    show as "current work" per grade (default 2).
  - `CURRENT_MAP_WINDOW` — same, for MAP Practice numbers (default 1).
  - `MAP_SHARED_ACROSS_GRADES` — `true`/`false`, whether the same MAP videos
    show to both 6th and 7th grade (see `OPEN_ITEMS.md`).
  - `INGEST_POLL_MINUTES` — how often YouTube is checked for new uploads.
  - `PERIODS` — comma-separated list shown on the student name/period screen.
    **Edit this to match your actual class periods** — the default is a
    placeholder from the old Google Form.

---

## Part 6 — Deploy the web app

1. Click **Deploy → New deployment**.
2. Click the gear icon next to "Select type" → **Web app**.
3. Description: "Math Lab v1".
4. **Execute as**: "Me (your account)".
5. **Who has access**: "Anyone" (students don't need to sign in — this
   matches how the old Google Form worked, and keeps things simple on school
   Chromebooks that may not be signed into a specific account). If your
   district requires sign-in, choose "Anyone within [your Workspace domain]"
   instead — students will need to be signed into a school account to open it.
6. Click **Deploy**.
7. Authorize again if prompted (same steps as Part 4).
8. Copy the **Web app URL** shown. This is the student app.
   - The teacher dashboard is the same URL with `?page=dashboard` added to
     the end, e.g. `https://script.google.com/macros/s/XXXXX/exec?page=dashboard`.
     Save that second link somewhere private for teacher use — bookmark it,
     don't post it publicly.

**Whenever you edit any file in this project going forward** (e.g. to change
wording), you must click **Deploy → Manage deployments → (pencil icon) →
New version → Deploy** for the change to go live at the same URL. Simply
saving a file is not enough on its own.

---

## Part 7 — Embed in the Google Site

1. Open your Google Site (either the existing Developing Educators companion
   site, or wherever the Math Lab page will live), signed in as the
   Developing Educators account.
2. Edit the page, click **Insert → Embed**.
3. Choose **By URL**, paste the student web app URL from Part 6, click
   **Insert**.
4. Resize the embedded box so it's tall enough to show the video player and
   response form comfortably (roughly 700–900px tall works well; you can
   always adjust later).
5. Publish the site.

Do **not** embed the dashboard URL on any public page — open that link
directly when you want to review responses.

---

## Ongoing use (this is genuinely all there is)

1. Record a video, name it exactly per the convention (e.g. `7th Grade Do 3`
   or `MAP Practice 4`), upload it to
   https://www.youtube.com/@developingeducators.
2. Within `INGEST_POLL_MINUTES` (default 15), it appears automatically for
   students — nothing else to do.
3. Open the dashboard link, enter the passcode, review answers (it shows
   "official" responses by default — check "Show all" if you want to see
   ones submitted without the class passcode too).

---

## Troubleshooting

- **A video isn't showing up.** Check its exact YouTube title against the
  convention in the main README — even one extra space, wrong capitalization
  of "Teach/Do/Home" is tolerated, but the wrong word or a missing/garbled
  number is not. Also confirm it's a normal upload, not a members-only or
  unlisted-in-a-way-that-hides-it video (unlisted is fine; private is not —
  the API can't see private videos).
- **"Could not resolve YouTube channel for handle".** The API key may not
  have YouTube Data API v3 enabled, or the handle changed. Check Part 2 and
  the `YOUTUBE_CHANNEL_HANDLE` row in the Config sheet.
- **Dashboard says "no passcode configured".** Add `DASHBOARD_PASSCODE` in
  Script Properties (Part 3).
- **Changes I made aren't showing up for students.** You need to publish a
  new deployment version — see the note at the end of Part 6.
