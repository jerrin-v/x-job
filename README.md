# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Tue 24 Nov 2026, 11:41:24 AM UAE<br><sub>Tue 24 Nov 2026, 7:41:24 AM UTC</sub> | Apply and Mark applied swapped in the job pop-up | v1.0.10 | [`dea8fd7`](https://github.com/jerrin-v/x-job/commit/dea8fd7cd6f0a65ba795aa4dc1e6837dc97dbe2f) |
| Tue 24 Nov 2026, 11:39:58 AM UAE<br><sub>Tue 24 Nov 2026, 7:39:58 AM UTC</sub> | View job opens a pop-up with the details and an Apply button; in-card details removed; logo drawn on whole pixels | v1.0.9 | [`9671634`](https://github.com/jerrin-v/x-job/commit/9671634a5e32b3e571a7d3e98aaaff56838a6fb0) |
| Tue 24 Nov 2026, 11:15:42 AM UAE<br><sub>Tue 24 Nov 2026, 7:15:42 AM UTC</sub> | visa tabs above the job list, every card the same height, footer pinned to the bottom | v1.0.8 | [`d49389a`](https://github.com/jerrin-v/x-job/commit/d49389a8f2825be0c513916a7d051f3a1d562ba0) |
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
