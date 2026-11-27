# Restore X-Jobs from this backup

The app and its source are in `backup/x-jobs.tar.gz.age`, sealed with [age](https://age-encryption.org).
To open it you need the private key (kept outside this repo). Install age first: `brew install age` on a Mac,
`apt-get install age` on Linux.

## 1. Open it on a computer

```sh
mkdir x-jobs
age -d -i /path/to/private-key.txt backup/x-jobs.tar.gz.age | tar -xz -C x-jobs
```

`x-jobs/index.html` is the page exactly as published on claude.ai. Never commit the opened files back into this repo.

To go back to an earlier version, check out its tag (for example `git checkout restore-v1.0.44`) and open the backup
from there in the same way.

## 2. Publish it as a website again

The **Publish site** workflow (`.github/workflows/publish.yml`) opens the backup, builds one page (the sign-in page
with the app inside it) and puts it on GitHub Pages after every push to main, at `https://jerrin-v.github.io/x-job/`.
A new repo or account needs the repository secret named in the workflow first, and one setting, made once:
**Settings → Pages → Build and deployment → Source: GitHub Actions**. Then **Actions → Publish site → Run workflow**,
and put the new address on the `Website:` line at the top of the README and in the repo's About box. The data is not in
this repo: it stays in the owner's own database, and the website's sign-in page has a guide for setting up a new one.

## 3. Rebuild the live app

Publish `index.html` as a new claude.ai artifact with the `db` and `assets` capabilities (`db` rules: read and write
for the owner only). The job list lives in that artifact's database, filled by the hourly "X-Jobs search" task.

## 4. Change it and seal it again

Open the backup (step 1) in a folder outside this repo, change `index.html`, run `node tests/site-build.test.mjs`, then seal the folder into `backup/` and push:

```sh
sh tools/pack.sh /path/to/x-jobs
```

Sealing needs only the public key in `keys/backup-recipient.txt`.

## Lost the key?

The backup can't be opened without it, so keep a copy of the key file. With a readable copy of the app folder still at
hand, make a new key pair, replace `keys/backup-recipient.txt`, seal the folder again and replace the matching repository
secret.
