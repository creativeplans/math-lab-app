# Architecture

## Core engine vs. branches

The brief's central architectural requirement: **one core engine, three
front ends.** This build only implements Branch 1 (Math Lab), but every
engine-level piece is written so Branch 2 (per-teacher assignments) and
Branch 3 (public self-service) can be added later without touching Branch 1's
data or breaking it.

### What the core engine owns (in `apps-script/`)

| File | Responsibility |
|---|---|
| `SheetService.js` | Video storage, response storage, completion lookups. The only file that reads/writes the spreadsheet. |
| `Ingestion.js` | YouTube polling, title parsing, dedupe. Pure `parseVideoTitle()` function, unit-tested in `test/`. |
| `Config.js` | Layered configuration (code defaults → Config sheet → Script Properties for secrets). |
| Watch enforcement (`StudentClient.html`) | Furthest-watched tracking, seek-blocking, playback-rate locking, end-of-video unlock. This logic is per-video-player and doesn't know anything about "Math Lab" specifically — it operates on whatever `videoId` it's given. |

### What is Branch-1-specific (and would NOT be reused as-is by Branch 2/3)

- The **title-parsing convention** (`Xth Grade Teach/Do/Home N`, `MAP Practice
  N`) is specific to the Math Lab channel. Branch 2 doesn't need title parsing
  at all — a teacher pastes a URL and names the assignment directly.
- The **grade-based navigation** (`StudentApp.html`'s grade → current work →
  video flow) is a Branch 1 front end. Branch 2 would need a different
  front end: paste URL → name assignment → choose response type → get a
  shareable link.
- The **Responses sheet schema** includes Math-Lab-specific columns (Period,
  Grade, VideoType, VideoNumber). Branch 2 responses belong to a *different*
  teacher's assignment, not this Math Lab class structure, and should **not**
  be mixed into the same Responses sheet/tab.

### How Branch 2 would plug in without disturbing Branch 1

1. Add a new database "workspace" — either a separate spreadsheet per
   teacher/assignment, or new sheet tabs prefixed distinctly (e.g.
   `Assignment_<id>_Responses`). Never repurpose the Math Lab `Videos` /
   `Responses` tabs.
2. Add new server functions (e.g. `Assignments.js`) for: create assignment
   (URL + name + response type + teacher), generate a unique student link,
   record responses against that assignment's own storage.
3. Add a new `doGet` route (e.g. `?page=assignment&id=...`) in `Code.js`
   pointing at a new front-end HTML set (e.g. `AssignmentApp.html`) that
   reuses the **same watch-enforcement client code** (factor
   `StudentClient.html`'s player logic into a shared include once there's a
   second consumer, rather than copy-pasting it) but with its own simpler
   flow (no grade/current-work navigation, no name+period gate — assignment
   links are already scoped to one student).
4. Branch 3 is Branch 2's teacher-creation flow made self-service and public
   — same engine, same assignment storage pattern, with its own signup/rate
   limiting concerns to design at that time (explicitly out of scope until
   Branch 1 is proven, per the brief).

The key invariant to preserve at every step: **Branch 1's `Videos` and
`Responses` sheets, and the video IDs/embeds already in front of students,
must never need to move, migrate, or change shape** when Branches 2/3 are
built.

## Data flow (Branch 1)

```
YouTube channel (@developingeducators)
        │  (title convention: "7th Grade Do 2", "MAP Practice 3", ...)
        ▼
Ingestion.js  ── time-driven trigger, every N minutes ──▶  Videos sheet
        ▲                                                        │
        │ (title regex filters out Shorts / unrelated uploads)   │
        │                                                        ▼
                                              SheetService.getGradeHome(grade)
                                                        │
                                                        ▼
                                     StudentApp.html (grade → current work → video)
                                                        │
                                     YouTube IFrame Player + watch enforcement
                                                        │
                                          video reaches real end in-session
                                                        ▼
                                          response form unlocks → submit
                                                        │
                                                        ▼
                                              Responses sheet  ◀── Dashboard.js
                                                                          │
                                                                          ▼
                                                          DashboardApp.html (teacher)
```

## Why Google Apps Script

The brief specifies "Google Apps Script / HTML / CSS / JavaScript" and
"Google Sheets/Drive" explicitly, and requires the whole thing to embed
inside a Google Site with zero ongoing maintenance. Apps Script is the only
option that satisfies all of: free, no separate hosting bill, no server to
patch or that can go down independently, natively triggerable on a schedule,
natively reads/writes Sheets, and embeds cleanly in Google Sites via an
`Embed → By URL` block. It also keeps the entire system inside the
Developing Educators Google account's ownership, per the brief's survival
requirement.
