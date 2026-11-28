# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Sat 28 Nov 2026, 12:15:16 PM UAE<br><sub>Sat 28 Nov 2026, 8:15:16 AM UTC</sub> | confirm before every delete, SemiBold buttons, black word-list tags with Lucide x | v1.0.76 | [`a13628f`](https://github.com/jerrin-v/x-job/commit/a13628f0ff86b984528b2f6551e9c236b68aa23e) |
| Sat 28 Nov 2026, 11:36:29 AM UAE<br><sub>Sat 28 Nov 2026, 7:36:29 AM UTC</sub> | body text 16px, equal badge gaps, Lucide icons 1.6px, X Lab tile weights | v1.0.73 | [`4ce64e1`](https://github.com/jerrin-v/x-job/commit/4ce64e10258cf131bee52b4901abb533d0116aae) |
| Sat 28 Nov 2026, 9:47:11 AM UAE<br><sub>Sat 28 Nov 2026, 5:47:11 AM UTC</sub> | X Lab brand colours: yellow #F2CE00 with black and white, new tab icon | v1.0.63 | [`1cf3b02`](https://github.com/jerrin-v/x-job/commit/1cf3b02170806a42da23c25e372e9e64b086ce6b) |
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
