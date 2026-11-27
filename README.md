# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Fri 27 Nov 2026, 1:19:43 PM UAE<br><sub>Fri 27 Nov 2026, 9:19:43 AM UTC</sub> | sign in with email and password only | v1.0.46 | [`fc81c57`](https://github.com/jerrin-v/x-job/commit/fc81c5770a2a2e52bb97dddb757f0ed069458729) |
| Fri 27 Nov 2026, 1:02:33 PM UAE<br><sub>Fri 27 Nov 2026, 9:02:33 AM UTC</sub> | sign in with the database login, no user list or built-in job list on the site | v1.0.45 | [`e185fc2`](https://github.com/jerrin-v/x-job/commit/e185fc24f734d92f1421fcc07813a8f248e305cf) |
| Fri 27 Nov 2026, 11:25:33 AM UAE<br><sub>Fri 27 Nov 2026, 7:25:33 AM UTC</sub> | free job feeds in Sync (Arbeitnow, Jobicy, Remotive), Job feeds tab under Job boards | v1.0.44 | [`5ab59ec`](https://github.com/jerrin-v/x-job/commit/5ab59ec51e8e6d8ffe11982e28a2b25bb3bebfea) |
<!-- latest-updates:end -->

Restore point: **v1.0.44** is kept as it was on the branch `restore-v1.0.44`.

## Open it

1. **Open the website** above in Chrome, Edge, Firefox or Safari and sign in.
2. **Pick a role**, open the employer's page with View job and apply there.
3. **Mark it applied** and it moves to History.

## Update it

1. **Ask Claude for the change.** The version goes up by 1 in the last place (v1.0.1 → v1.0.2 → …).
2. **Say "Push".** Nothing is pushed here before that.
3. The update shows in the table above, and on the website a minute or two later.

## What's in this repo

- `backup/` — the app, sealed with [age](https://age-encryption.org), and the version it holds.
- `keys/backup-recipient.txt` — the public key the backup is sealed with.
- `tools/` — seals a new version and keeps the table above up to date.
- `.github/workflows/` — publish the website and update the table after every push.

**If the website is ever gone, see [RESTORE.md](RESTORE.md).**

Note: the job list, marks, settings and files live in the owner's own database, not in this repo.

---

© 2026 Jerrin Varghese. All rights reserved — see [LICENSE](LICENSE).
