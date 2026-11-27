# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Fri 27 Nov 2026, 4:46:35 PM UAE<br><sub>Fri 27 Nov 2026, 12:46:35 PM UTC</sub> | Rajdhani font built in with text centred, themed scrollbars, version chip, bolder headings | v1.0.51 | [`009f952`](https://github.com/jerrin-v/x-job/commit/009f95269b0f387df99c95ed7898cace81ddeef5) |
| Fri 27 Nov 2026, 2:10:40 PM UAE<br><sub>Fri 27 Nov 2026, 10:10:40 AM UTC</sub> | the Sync window shows only Close after a finished Sync | v1.0.48 | [`4dd98f6`](https://github.com/jerrin-v/x-job/commit/4dd98f6b35e84dde2710ce56f48d9502da71725d) |
| Fri 27 Nov 2026, 1:52:31 PM UAE<br><sub>Fri 27 Nov 2026, 9:52:31 AM UTC</sub> | reset password from the sign-in page, tighter sign-in box, Standalone renamed AI Configuration | v1.0.47 | [`7f87915`](https://github.com/jerrin-v/x-job/commit/7f8791561befbef24e38bc020557fc994426fb98) |
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
