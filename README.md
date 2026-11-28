# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Sat 28 Nov 2026, 4:09:28 PM UAE<br><sub>Sat 28 Nov 2026, 12:09:28 PM UTC</sub> | font sizes only from the 12-64 scale on every screen | v1.0.90 | [`96e7ca8`](https://github.com/jerrin-v/x-job/commit/96e7ca8f1b9d1447ddd25acbdc52922b47e5241d) |
| Sat 28 Nov 2026, 3:54:17 PM UAE<br><sub>Sat 28 Nov 2026, 11:54:17 AM UTC</sub> | Excel icon buttons on the switcher row, phone layout fixes, no zoom on phones | v1.0.89 | [`8ee807b`](https://github.com/jerrin-v/x-job/commit/8ee807b608112c72ad9535f87b6774ac9fb3ec7c) |
| Sat 28 Nov 2026, 3:09:17 PM UAE<br><sub>Sat 28 Nov 2026, 11:09:17 AM UTC</sub> | Home and Open tabs, outline buttons and even badges on Websites, no page bounce past the footer | v1.0.83 | [`c65de6e`](https://github.com/jerrin-v/x-job/commit/c65de6e03f0c2627671c561c9071ae0c4e77687b) |
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
