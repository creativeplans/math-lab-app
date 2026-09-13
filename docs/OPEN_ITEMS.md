# Open Items & Assumptions

## Carried forward from the brief

1. **"Number" semantics (nice-to-have, not blocking).** The brief leaves open
   whether `Number` in a title like `7th Grade Do 2` is a continuous
   count across the whole grade/term, or resets per topic. The build does
   **not** assume either — `Number` is stored and displayed exactly as
   parsed from the title, and "current work" is simply "the highest N
   distinct numbers seen so far" (see item 3 below), which behaves
   correctly either way. No action needed unless you want numbering to mean
   something more specific (e.g. resetting a visual "Unit" label at certain
   numbers) — that would need a small addition to the title convention.

## Assumptions made during the build (please confirm)

2. **MAP Practice sharing across grades.** The MAP title convention
   (`MAP Practice N`) carries no grade token, so by default the build shows
   the same MAP Practice videos to both 6th and 7th grade
   (`MAP_SHARED_ACROSS_GRADES = true` in the Config sheet). If MAP content is
   actually grade-specific and this is just not reflected in the title yet,
   either:
   - flip `MAP_SHARED_ACROSS_GRADES` to `false` in the Config sheet **and**
     start including a grade token in MAP titles going forward (this would
     need a small update to `parseVideoTitle` in `Ingestion.js` to parse the
     new pattern), or
   - keep sharing as-is if MAP content is genuinely the same for both grades.

3. **"Current work" window size.** The brief's mockup shows two problem
   numbers (14 and 15) visible at once as "current," but doesn't specify the
   rule for how many stay visible as new ones publish. The build defaults to
   the **2 most recent problem numbers** per grade and the **1 most recent**
   MAP Practice number, both editable anytime in the Config sheet
   (`CURRENT_PROBLEM_WINDOW`, `CURRENT_MAP_WINDOW`) with no code change
   required. Adjust these to match how far ahead/behind students in practice
   should be visible.

4. **Dashboard access control.** The brief doesn't specify how teachers
   should authenticate to the dashboard. This build uses a single shared
   passcode (Script Property `DASHBOARD_PASSCODE`) rather than per-teacher
   login, matching the "no accounts, no public profiles" school-safe
   philosophy and keeping setup to one property instead of a user directory.
   This is a light deterrent, not a strong access control — the real
   boundary is the web app deployment's "who has access" setting (see
   `DEPLOYMENT.md` Part 6). If multiple teachers need individually
   attributable access or the ability to revoke one teacher without
   resetting it for everyone, this would need to be upgraded to Google
   Sign-In-based access checks (`Session.getActiveUser()` against an
   allowlist) — straightforward to add later, not built now since it wasn't
   requested.

5. **Student identity is First Name + Last Initial + Period** (updated in Fix
   Round 1 from First Name alone, matching the wording already used
   elsewhere on the Developing Educators site). This reduces, but by design
   doesn't eliminate, collisions — two students who'd type the exact same
   "First Name + Last Initial" in the same period are still indistinguishable
   to completion-tracking and the dashboard, and nothing is validated about
   the format of what a student types here. There is intentionally no roster
   to maintain. If a real collision comes up, the next step up would be a
   short student ID field, which would need one more addition to the gate
   screen and the Responses sheet schema.

6. **Shorts/unrelated-video filtering** is implemented purely via strict
   title matching (per the brief: "including anything that doesn't match the
   pattern"), not via YouTube's duration/short-detection metadata. If a Short
   or unrelated video ever happens to have a title that accidentally matches
   the convention exactly (e.g. someone mistakenly titles a Short
   "7th Grade Do 9"), it would be ingested. This matches the brief's stated
   filtering rule; tightening further (e.g. also checking video duration)
   is easy to add in `Ingestion.js` if it becomes a real problem.

7. **Response unlock persistence across a page refresh.** Per the brief,
   refreshing must not auto-unlock the response — this build keeps
   watch-progress (`maxWatched`) purely in memory on the page, so a refresh
   resets it and the video must be watched to the end again in that new
   session. This is a deliberate reading of "must not auto-unlock," not an
   accidental limitation — flag if the intent was instead "remember unlock
   state, just not skip-ahead state," which would need small changes to
   persist an "already reached end once" flag separately from watch
   position.

## Assumptions made in Fix Round 1

8. **Official-tagging defaults old data to visible.** The dashboard's default
   "official only" filter treats a response as official unless it is
   explicitly tagged `Official: FALSE` server-side. Responses recorded before
   this feature existed have no `Official` value at all and are shown by
   default rather than hidden, so existing data doesn't disappear from the
   dashboard the moment this ships. If you'd rather those older rows be
   treated as non-official until reviewed, that's a one-line change in
   `Dashboard.js` (`getFilteredResponses`) — ask and it's a quick flip.

9. **The class passcode is a soft, shared secret, not real access control** —
   by design, per the request: the app stays public and single-deployment for
   now. It's checked server-side (the actual value is never sent to the
   browser), but it's the same word for every student, typically written on a
   board, so treat it as a way to *tag* trustworthy responses rather than to
   *secure* anything. It's also remembered in the browser's local storage
   alongside the student's name/period for convenience, the same as those
   fields already were.

10. **Main Answer and Basics Answer are both required** on Do/Home/MAP videos
    (matching the old single "Your Answer" field having been required). The
    comma-separated-parts hint above each is, per the request, only a
    suggestion — not validated or enforced in any format.
