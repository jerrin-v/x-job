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
page starts from the job list sealed with the version. Once Jerrin has connected his own database under Settings ›
Standalone, the site reads and writes that database instead (see Standalone mode below) and the sealed list is only
used to fill an empty database. Without a connection, marks made on the site stay in that browser. The sign-in page
(`src/login.html`) carries the site's Content-Security-Policy.

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
- Standalone, continued (v1.0.29 to v1.0.31). Sync on the website finds new roles without AI from "Companies to watch" (Settings › Job boards; collection `companies`): it reads each watched employer's board on the four job systems and keeps roles by his own word lists (Settings › Search › Watch rules, saved in `settings/search` under `watch`: title words, level words, always-keep, skip, never-show places, only-show places, the no-sponsorship switch, most new roles per Sync). He wants nothing hardcoded: the lists in the code are only starting values. The AI web search is optional and off unless he switches it on. His CV and cover letter PDFs (two slots) are kept in his Supabase Storage bucket `xj-files`; a new upload replaces the old file and Remove deletes it there. Planned next: tailored CV and cover letter on the website, read from the latest uploaded PDFs with his AI key.
- Audit of 26 Nov 2026 (v1.0.33). No two functions may share a name (a duplicate broke the Region filter from v1.0.29 to v1.0.32). Personal details are never written into the code: the footer column, the copyright line, the AI prompts and document file names read Settings › Profile or his CV. A new AI provider or job system needs its host added to the allowlist in `src/login.html`. Network calls have a time limit.
- v1.0.34 to v1.0.38. Every dropdown opens the app's own menu. He keeps the database connection in each browser only: nothing about his database may be put in git or in GitHub settings; a red bar at the top says when the site is not connected, and Settings › Standalone has a Setup help pop-up. Place rules (Settings › Search › Places) work by country: countries come from the browser's list, towns from Open-Meteo's geocoding service, and the never-show and only-show lists also hide roles already on the list. Search and Job boards are split into tabs inside their cards; Job boards › Websites lists and edits where roles came from. The sign-in page is a split layout with slides.
- v1.0.39 to v1.0.43. The sign-in box keeps its original design (dotted grey background, white card, mint button) beside the slides. A posting's sponsorship wording is read "no" first: wording that rules out sponsorship, or needs citizenship or permanent residence, removes the role, also for roles added earlier (re-read on each Sync). History and Archive can remove selected or all roles for good from the database; a small note in the `removed` collection keeps Sync from adding them again. Selecting must never change a card's size or layout. Header order: status pill with a sync icon inside, theme, settings (gear).
- Each job pop-up can make a CV and cover letter tailored to the role: Claude writes them in the page (the `sample` capability), `tailor/tailor.js` lays out the two PDFs with jsPDF from `tailor/master.json` (his CV, word for word: a tailored CV may only reorder and select its lines) and he downloads a zip (`downloads` capability). The `tailor/` files are published with the artifact and sealed in the backup; the website does not offer this. When his CV changes, update `tailor/master.json`.
- v1.0.44 (27 Nov 2026: he will not make an AI key). Job boards has a third tab, Job feeds: free public job lists that need no key (Arbeitnow on by default; Jobicy and Remotive are remote-only and off). On the website Sync reads the feeds that are on after the watched companies and keeps roles by the same Watch rules; postings not written in English are left out. A feed role carries `feedRef` (`<feed>/<id>`), `feedAt` and the feed name as `source`; its link is the feed's page. Arbeitnow roles are confirmed or closed from the feed itself on each Sync. Feed state lives in the `feeds` collection. A new feed needs a reader in `feedJobs` and its host in the allowlist in `src/login.html`.

## When Jerrin says "Push"
1. `git pull --rebase origin main` (the Update log workflow may have committed a README update).
2. Seal the new version (above) and commit `backup/` as `vX.Y.Z: what changed`. That line is the Change column of the table.
3. `python3 tools/update-log.py`, then commit `README.md` alone as "README: latest updates".
4. Push both commits to `main`. Check the Publish site run, then open the address and read the version in the footer.
