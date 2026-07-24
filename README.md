# TaskField — a to-do list that adapts to your field

TaskField is a single-file, offline-capable to-do app. On first use you pick your
**field** (Marketing, Construction, Production, Sales, Operations, Finance, General/Personal,
or a **Custom** field you name yourself) and the app sets up the right task **categories**
and an optional **starter checklist** for that role. Switch fields anytime.

**Live app:** https://RJA9291.github.io/Todolist_Personal/

## Features
- **Role-based setup** — 7 built-in fields plus a custom field with your own categories.
- **Personal tab (passcode-locked)** — the General / Personal field is protected by a passcode
  and holds three sections: your personal **Tasks**, a monthly **Bills** tracker (recurring bills
  with amounts, account references, and per-month paid/unpaid ticking + totals), and a daily
  **Spending** tracker (log expenses, see today's and the month's totals). The passcode is a
  local privacy lock — data is stored unencrypted on your device only.
- **List & Board (Kanban) views** — grouped by To do / In progress / Completed.
- **Progress at a glance** — completion donut + status counts.
- **Task details** — category, priority (High / Medium / Low), due date (with overdue/soon
  flags), and notes.
- **Filter & search** — by category, priority, status, or free text.
- **Light / dark / auto theme.**
- **Works offline** — installable to your phone's home screen (PWA).
- **Your data stays on your device** — saved in the browser. Use **Export / Import** (JSON) to
  back up or move data between devices/URLs.

## Install on your phone (iPhone)
1. Open the live URL above in **Safari**.
2. Tap the **Share** button → **Add to Home Screen**.
3. Launch it from the icon — it runs full-screen and works offline.

(On Android/Chrome: menu → **Install app** / **Add to Home screen**.)

## Project layout
| File | Purpose |
| --- | --- |
| `app.html` | The app — **single source of truth** (`<title>` + `<style>` + markup + `<script>`). Also what's published as a claude.ai Artifact. |
| `index.html` | **Generated** standalone PWA page (do not hand-edit). |
| `manifest.webmanifest` | PWA metadata (name, icons, colours, standalone display). |
| `sw.js` | Service worker for offline support. |
| `icon.svg`, `icon-180/192/512.png` | App icons (`make_icons.py` regenerates the PNGs). |
| `.claude/build-pages.sh` | Wraps `app.html` into `index.html`. |
| `.claude/auto-push.sh` | Rebuilds `index.html`, then commits & pushes on save. |

## Editing
Edit **`app.html`** only. On save, `.claude/auto-push.sh` regenerates `index.html`, commits,
and pushes. If you change any cached asset, bump the `CACHE` version string in `sw.js` so
returning visitors get the update.
