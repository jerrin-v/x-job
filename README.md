# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Sat 28 Nov 2026, 8:59:49 AM UAE<br><sub>Sat 28 Nov 2026, 4:59:49 AM UTC</sub> | closed links are left out of the Sync window's list | v1.0.57 | [`5240ce8`](https://github.com/jerrin-v/x-job/commit/5240ce8a57ed048532ca33372ab6ee3d2d23603e) |
| Sat 28 Nov 2026, 8:45:51 AM UAE<br><sub>Sat 28 Nov 2026, 4:45:51 AM UTC</sub> | Barlow font as on the portfolio, text sizes 14 / 16 / 18px (minimum 14px) | v1.0.56 | [`fdd820c`](https://github.com/jerrin-v/x-job/commit/fdd820ced9fa6569f8e007319fa5187872ce77ae) |
| Fri 27 Nov 2026, 5:08:33 PM UAE<br><sub>Fri 27 Nov 2026, 1:08:33 PM UTC</sub> | deleting roles is saved at once, with a warning to keep a code or delete fully; smaller select tick at the right | v1.0.54 | [`918b212`](https://github.com/jerrin-v/x-job/commit/918b21201db47893bed74051e6da62da3c17952a) |
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
