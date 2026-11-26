# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Thu 26 Nov 2026, 3:46:16 PM UAE<br><sub>Thu 26 Nov 2026, 11:46:16 AM UTC</sub> | stricter sponsorship reading, remove roles on History and Archive, header status pill | v1.0.43 | [`0a30461`](https://github.com/jerrin-v/x-job/commit/0a304618b7d57058ca57c9abb7da95d4c95f43e9) |
| Thu 26 Nov 2026, 3:04:19 PM UAE<br><sub>Thu 26 Nov 2026, 11:04:19 AM UTC</sub> | places by country, tabbed Search and Job boards, websites list, new sign-in page, not-connected bar | v1.0.38 | [`45d78c6`](https://github.com/jerrin-v/x-job/commit/45d78c6d25ed176928644323b88a97ff4f720590) |
| Thu 26 Nov 2026, 2:34:24 PM UAE<br><sub>Thu 26 Nov 2026, 10:34:24 AM UTC</sub> | database setup help pop-up and a notice when the database is not connected | v1.0.37 | [`13095fa`](https://github.com/jerrin-v/x-job/commit/13095fa38e578e520b913416cda56d9014c6e269) |
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

Note: the job list on the website refreshes about once an hour. The live list is in the app on claude.ai.

---

© 2026 Jerrin Varghese. All rights reserved — see [LICENSE](LICENSE).
