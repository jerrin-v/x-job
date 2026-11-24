# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Tue 24 Nov 2026, 12:17:56 PM UAE<br><sub>Tue 24 Nov 2026, 8:17:56 AM UTC</sub> | full-width gradient hero, one-piece search bar with inline filters, link-column footer, bolder logo | v1.0.16 | [`ce2f5aa`](https://github.com/jerrin-v/x-job/commit/ce2f5aa425284f48331e71b79a29a667b6d0c41d) |
| Tue 24 Nov 2026, 12:10:15 PM UAE<br><sub>Tue 24 Nov 2026, 8:10:15 AM UTC</sub> | clear header at the top and a compact blurred one while scrolling, wider footer spacing, Sign out under the settings menu | v1.0.15 | [`e30fa5f`](https://github.com/jerrin-v/x-job/commit/e30fa5fb55b8bcfec097a25c3c630b52f748d97d) |
| Tue 24 Nov 2026, 12:05:52 PM UAE<br><sub>Tue 24 Nov 2026, 8:05:52 AM UTC</sub> | fine dot texture on the background; logo and footer on the sign-in page | v1.0.14 | [`83a4672`](https://github.com/jerrin-v/x-job/commit/83a4672756eb7fa30ee7db401a5eb8c571b5e899) |
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
