# Jerrin Varghese — X-Jobs (job tracker)

Website: **https://jerrin-v.github.io/x-job/**

X-Jobs is a private job tracker. It lists product design and design system roles, puts employers that sponsor visas first, and keeps a history of applications.

## Latest updates

The last 3 updates pushed here, newest first.

<!-- latest-updates:start -->
| Updated | Change | Version | Commit |
| --- | --- | --- | --- |
| Thu 26 Nov 2026, 7:53:44 AM UAE<br><sub>Thu 26 Nov 2026, 3:53:44 AM UTC</sub> | regions cover the rest of Europe and the rest of the world; roles older than the age limit move to Archive | v1.0.26 | [`df69e5d`](https://github.com/jerrin-v/x-job/commit/df69e5d3e016ddfc98764296da58f3f265f844aa) |
| Wed 25 Nov 2026, 9:58:05 AM UAE<br><sub>Wed 25 Nov 2026, 5:58:05 AM UTC</sub> | card buttons (outline Mark applied, View details, Apply); tailored CV and cover letter work from the employer's posting | v1.0.25 | [`0489c80`](https://github.com/jerrin-v/x-job/commit/0489c801cb9fd773658d08881caa738d07f9dbd1) |
| Wed 25 Nov 2026, 9:33:26 AM UAE<br><sub>Wed 25 Nov 2026, 5:33:26 AM UTC</sub> | each job pop-up can make a CV and cover letter tailored to the role, with a progress bar and a zip download | v1.0.23 | [`bcedfa1`](https://github.com/jerrin-v/x-job/commit/bcedfa19a0104436d6011bec66fc6ca4e53db4f8) |
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
