# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Tue 24 Nov 2026, 11:11:47 AM UAE<br><sub>Tue 24 Nov 2026, 7:11:47 AM UTC</sub> | tools on the tab row, smaller logo with the version beside it, plain one-line footer | v1.0.6 | [`89a0e6f`](https://github.com/jerrin-v/x-job/commit/89a0e6fd5ecf30f2fe798d7c2d8bf966602a728a) |
| Tue 24 Nov 2026, 11:03:23 AM UAE<br><sub>Tue 24 Nov 2026, 7:03:23 AM UTC</sub> | tabs on their own row, lined up with the left edge of the cards; header follows the page width | v1.0.5 | [`22ee4fe`](https://github.com/jerrin-v/x-job/commit/22ee4fe4675250a0a01d238b4eb4e2c7aa0f3a6c) |
| Tue 24 Nov 2026, 11:02:06 AM UAE<br><sub>Tue 24 Nov 2026, 7:02:06 AM UTC</sub> | two-column job cards in a new style, a wide banner on Saved, History, Archive and Settings, breadcrumb removed | v1.0.4 | [`4cca59e`](https://github.com/jerrin-v/x-job/commit/4cca59e7846dd0304e482228b9a2d65bb631552f) |
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

Note: the website shows the job list as it was when the version was pushed. The live list is in the app on claude.ai.

---

© 2026 Jerrin Varghese. All rights reserved — see [LICENSE](LICENSE).
