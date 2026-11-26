# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Thu 26 Nov 2026, 1:36:30 PM UAE<br><sub>Thu 26 Nov 2026, 9:36:30 AM UTC</sub> | audit fixes: region filter, request time limits, contrast, details read from Settings, unused code removed | v1.0.33 | [`7d7c2e8`](https://github.com/jerrin-v/x-job/commit/7d7c2e89a7358752af88e6748c62a35671179341) |
| Thu 26 Nov 2026, 12:54:42 PM UAE<br><sub>Thu 26 Nov 2026, 8:54:42 AM UTC</sub> | documents download under their original file name | v1.0.32 | [`1d069a4`](https://github.com/jerrin-v/x-job/commit/1d069a48c12af8bd50d1916ef068e44ede450899) |
| Thu 26 Nov 2026, 12:43:14 PM UAE<br><sub>Thu 26 Nov 2026, 8:43:14 AM UTC</sub> | companies to watch, editable watch rules and document uploads on the website | v1.0.31 | [`c93048a`](https://github.com/jerrin-v/x-job/commit/c93048a07974c526f1e2f24d1f7dcce247ffee53) |
<!-- latest-updates:end -->

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

Note: the job list on the website refreshes about once an hour. The live list is in the app on claude.ai.

---

© 2026 Jerrin Varghese. All rights reserved — see [LICENSE](LICENSE).
