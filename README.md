# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Tue 24 Nov 2026, 11:55:06 AM UAE<br><sub>Tue 24 Nov 2026, 7:55:06 AM UTC</sub> | New Zealand added as a region | v1.0.13 | [`a1e3c1c`](https://github.com/jerrin-v/x-job/commit/a1e3c1c96eb65d55e5607c34e9873dd5a900f3c7) |
| Tue 24 Nov 2026, 11:48:00 AM UAE<br><sub>Tue 24 Nov 2026, 7:48:00 AM UTC</sub> | Mark applied on the left, View job and Apply on the right, on cards and in the pop-up | v1.0.12 | [`fcfeabb`](https://github.com/jerrin-v/x-job/commit/fcfeabb2ba69726d2ce6e2839bb49abd55e04e3f) |
| Tue 24 Nov 2026, 11:41:53 AM UAE<br><sub>Tue 24 Nov 2026, 7:41:53 AM UTC</sub> | no icons inside text buttons | v1.0.11 | [`c5b4d1c`](https://github.com/jerrin-v/x-job/commit/c5b4d1c5a9ade294d9fe1e2d552d41e283fccfa8) |
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
