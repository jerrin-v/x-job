# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Thu 26 Nov 2026, 12:43:14 PM UAE<br><sub>Thu 26 Nov 2026, 8:43:14 AM UTC</sub> | companies to watch, editable watch rules and document uploads on the website | v1.0.31 | [`c93048a`](https://github.com/jerrin-v/x-job/commit/c93048a07974c526f1e2f24d1f7dcce247ffee53) |
| Thu 26 Nov 2026, 11:36:23 AM UAE<br><sub>Thu 26 Nov 2026, 7:36:23 AM UTC</sub> | standalone mode on the website: own database, own AI key and Sync now in the page | v1.0.28 | [`f3254f2`](https://github.com/jerrin-v/x-job/commit/f3254f281d8f3de1fab5e7aeec0eca3cc570659a) |
| Thu 26 Nov 2026, 10:58:10 AM UAE<br><sub>Thu 26 Nov 2026, 6:58:10 AM UTC</sub> | Sync now button with a progress pop-up; checks no longer run on a timer | v1.0.27 | [`e41a4e7`](https://github.com/jerrin-v/x-job/commit/e41a4e75b71f3d87543b525af6ffecb0451a75c6) |
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
