# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Sat 28 Nov 2026, 9:47:11 AM UAE<br><sub>Sat 28 Nov 2026, 5:47:11 AM UTC</sub> | X Lab brand colours: yellow #F2CE00 with black and white, new tab icon | v1.0.63 | [`1cf3b02`](https://github.com/jerrin-v/x-job/commit/1cf3b02170806a42da23c25e372e9e64b086ce6b) |
| Sat 28 Nov 2026, 9:32:20 AM UAE<br><sub>Sat 28 Nov 2026, 5:32:20 AM UTC</sub> | red trash icons in Settings, 16px text boxes, switchers stay one row on phones | v1.0.62 | [`18b33c8`](https://github.com/jerrin-v/x-job/commit/18b33c8a0de5b437aab7806b976864137452844e) |
| Sat 28 Nov 2026, 9:18:46 AM UAE<br><sub>Sat 28 Nov 2026, 5:18:46 AM UTC</sub> | portfolio font rules: badges and digits centred, Medium below 24px, 16px stat labels, tighter line heights, sign-in sizes | v1.0.60 | [`182856c`](https://github.com/jerrin-v/x-job/commit/182856ce5f3b387c0956dc8622db8d515512cf19) |
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
