# X-Jobs (jerrin-v/x-job) — notes for Claude

Jerrin's private job tracker. The live app is a claude.ai artifact ("X-Jobs") whose job list sits in the artifact's
database and is filled by the hourly "X-Jobs search" scheduled task. This public repo holds the app **only sealed**,
like his other repos (the pattern is copied from jerrin-v/xsim-rv):

- `backup/x-jobs.tar.gz.age` — the whole app folder: `index.html` (the page exactly as on claude.ai),
  `data/snapshot.json` (a copy of the job list for the website), `src/login.html`, `tools/site-lock.mjs`,
  `tools/make-snapshot.py`, `tests/`, `package.json`, `LICENSE` and the app's own notes in its `CLAUDE.md`.
  Sealed with age to `keys/backup-recipient.txt`.
- `backup/BUILD.txt` — `app: X-Jobs vX.Y.Z · packed <time>`; `tools/update-log.py` reads the Version column from it.
- Public files only: README.md, RESTORE.md, LICENSE, this file, `.github/workflows/` (publish, update-log),
  `tools/pack.sh`, `tools/update-log.py`, `keys/`. `.gitignore` blocks the opened app's paths and any `*key*.txt`.
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
- **Push to GitHub only when Jerrin's message says "Push"** ("Push it", "Let's push" count). Nothing else does.
- His own copy of the private key and the guides are on his Mac in Documents/Personal/Git-Hub-Files/X-Job.
- **No security details in the README**: no secret names, password or user steps, sign-in behaviour, example logins.
- Every app update raises the version by 1 in the last place (`version` in `package.json` and `VERSION` in `index.html`).
- README in the style of his other repos: short, no pictures, no feature details.
- He applies for jobs himself. No auto-apply features.

## When Jerrin says "Push"
1. `git pull --rebase origin main` (the Update log workflow may have committed a README update).
2. Seal the new version (above) and commit `backup/` as `vX.Y.Z: what changed`. That line is the Change column of the table.
3. `python3 tools/update-log.py`, then commit `README.md` alone as "README: latest updates".
4. Push both commits to `main`. Check the Publish site run, then open the address and read the version in the footer.
