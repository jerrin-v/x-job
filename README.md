# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Sat 28 Nov 2026, 5:46:21 PM UAE<br><sub>Sat 28 Nov 2026, 1:46:21 PM UTC</sub> | Footer pinned to the bottom on tall screens, no sideways jump between pages | v1.0.93 | [`5bc540a`](https://github.com/jerrin-v/x-job/commit/5bc540a119d9b7bd1a1e9684c90630055a242481) |
| Sat 28 Nov 2026, 5:34:41 PM UAE<br><sub>Sat 28 Nov 2026, 1:34:41 PM UTC</sub> | Sync counters with 14px Medium labels and 28px SemiBold numbers, aligned boxes | v1.0.92 | [`dc2b392`](https://github.com/jerrin-v/x-job/commit/dc2b3921bf6413013652f5d03bc193ceda9320b9) |
| Sat 28 Nov 2026, 5:14:10 PM UAE<br><sub>Sat 28 Nov 2026, 1:14:10 PM UTC</sub> | audit fixes: keyboard focus on search and filters, heading order, tap areas, dead code removed | v1.0.91 | [`e3fc6f0`](https://github.com/jerrin-v/x-job/commit/e3fc6f0424c098e4f2338a4eb2badcc95014a980) |
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
