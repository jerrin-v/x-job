# X-Jobs (jerrin-v/x-job) — notes for Claude

Jerrin's private job tracker. The live app is a claude.ai artifact ("X-Jobs") whose job list sits in the artifact's
database and is filled by the one "X-Jobs" scheduled task (no timer since 26 Nov 2026: he starts it with the "Sync now" button on the claude.ai page, or by hand; it needs the Claude app open on his Mac, because it confirms every link in a real browser, and it reports its progress to the page in `meta/sync`). This public repo holds the app **only sealed**,
like his other repos (the pattern is copied from jerrin-v/xsim-rv):

- `backup/x-jobs.tar.gz.age` — the whole app folder: `index.html` (the page exactly as on claude.ai),
  `data/snapshot.json` (a copy of the job list for the website), `src/login.html`, `tools/site-lock.mjs`,
  `tools/make-snapshot.py`, `tests/`, `package.json`, `LICENSE` and the app's own notes in its `CLAUDE.md`.
  Sealed with age to `keys/backup-recipient.txt`.
- `backup/data.json.age` + `backup/DATA.txt` — the job list for the website, sealed on its own by `tools/pack-data.sh`. The "X-Jobs" task refreshes and pushes it after each run (commit subject `data: job list <time>`), so the site follows the live list by one run.
- `backup/BUILD.txt` — `app: X-Jobs vX.Y.Z · packed <time>`; `tools/update-log.py` reads the Version column from it.
- Public files only: README.md, RESTORE.md, LICENSE, this file, `.github/workflows/` (publish, update-log),
  `tools/pack.sh`, `tools/pack-data.sh`, `tools/make-data.py`, `tools/update-log.py`, `keys/`. `.gitignore` blocks the opened app's paths and any `*key*.txt`.
  Never commit an opened file, a key or a password.

## Working on X-Jobs
1. The private key is Jerrin's, kept outside the repo. A session gets it only from him. Never print it, commit it or
   keep it after the work. Without it, the source of truth for the page is the claude.ai artifact itself (read it
   from there) and the tools can be rebuilt from RESTORE.md.
2. Open the backup outside the repo: `mkdir -p /home/claude/x-job-src && age -d -i <key file> backup/x-jobs.tar.gz.age | tar -xz -C /home/claude/x-job-src`. Read its `CLAUDE.md`.
3. Change and test there; publish `index.html` to the claude.ai artifact.
4. Refresh `data/snapshot.json` from a new read of the artifact database (`tools/make-snapshot.py`), then seal:
   `sh tools/pack.sh /home/claude/x-job-src` (public key only).

## Website
`.github/workflows/publish.yml` opens the backup with the `SITE_BACKUP_KEY` secret, builds the job-list copy into
`index.html`, locks it for the users in the `SITE_USERS` secret with the backup's own `tools/site-lock.mjs`, and
publishes that one page to https://jerrin-v.github.io/x-job/ (Pages source: GitHub Actions). A session cannot read or
set secrets; Jerrin changes them under Settings, then runs Actions › Publish site › Run workflow. Outside claude.ai the
page has no database, so it shows the job list as it was when the version was sealed; marks made there stay in that
browser.

## Working rules (from Jerrin)
- **Push to GitHub only when Jerrin's message says "Push"** ("Push it", "Let's push" count). Nothing else does. One exception he approved on 24 Nov 2026: the "X-Jobs" task (scheduled runs and runs he starts by hand; it replaced the separate "X-Jobs search" and "X-Jobs Poli" tasks on 25 Nov 2026) may push the job-list refresh (`backup/data.json.age`, `backup/DATA.txt`) by itself, and nothing else.
- The website's job list also carries his marks per job (applied, saved, hidden, with dates; never his notes), read from the "tracking" collection, so a job he marked on claude.ai is not offered again on the site. Marks made on the site stay in that browser.
- Jobs whose posting says no sponsorship are never shown and never added.
- A job is shown only when its link was seen live in a real browser (`checked: "open"`); `"listed"` means not confirmed and stays hidden. On 25 Nov 2026 more than half of the "open" jobs were dead links because a plain page fetch had been trusted.
- Regions (his steer of 26 Nov 2026): worldwide except India and the GCC countries, mostly the UK, Ireland and Europe. Region words on a job: UK, Ireland, Switzerland, EU, Europe (European, outside the EU), Australia, New Zealand, Other. Roles older than the "Ignore postings older than" setting leave Open and wait under Archive.
- **The README table lists only versions Jerrin pushed himself.** `data:` commits are never listed (tools/update-log.py skips them) and never change the version.
- His own copy of the private key and the guides are on his Mac in Documents/Personal/Git-Hub-Files/X-Job.
- **No security details in the README**: no secret names, password or user steps, sign-in behaviour, example logins.
- Every app update raises the version by 1 in the last place (`version` in `package.json` and `VERSION` in `index.html`).
- README in the style of his other repos: short, no pictures, no feature details.
- He applies for jobs himself. No auto-apply features.
- Standalone mode (v1.0.28, his goal of 26 Nov 2026: the website should run without Claude tasks). On the website, Settings › Standalone connects the page to his own Supabase project (one table `xj_docs`: owner, collection, id, data; row-level security, his own login) and takes his own AI key (Claude first; ChatGPT and Gemini to follow). The address, public key, sign-in session and AI key live only in his browser's storage: never in the page, the backup or this repo. With a database connected, "Sync now" runs in the page: Greenhouse, Lever, Ashby and SmartRecruiters links are checked against those systems' public job APIs; new roles come from the AI's web search and are shown only when such a check confirms them (others are saved as `checked: "listed"`). The first connection fills the database from the site's built-in list; after that the database is the source of truth there.
- Each job pop-up can make a CV and cover letter tailored to the role: Claude writes them in the page (the `sample` capability), `tailor/tailor.js` lays out the two PDFs with jsPDF from `tailor/master.json` (his CV, word for word: a tailored CV may only reorder and select its lines) and he downloads a zip (`downloads` capability). The `tailor/` files are published with the artifact and sealed in the backup; the website does not offer this. When his CV changes, update `tailor/master.json`.

## When Jerrin says "Push"
1. `git pull --rebase origin main` (the Update log workflow may have committed a README update).
2. Seal the new version (above) and commit `backup/` as `vX.Y.Z: what changed`. That line is the Change column of the table.
3. `python3 tools/update-log.py`, then commit `README.md` alone as "README: latest updates".
4. Push both commits to `main`. Check the Publish site run, then open the address and read the version in the footer.
