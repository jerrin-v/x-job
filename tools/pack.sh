#!/bin/sh
# Seals an X-Jobs folder (the page, the sign-in page, the site build tool, tests and notes) into
# backup/x-jobs.tar.gz.age with the public key in keys/backup-recipient.txt, and notes its version in
# backup/BUILD.txt. Sealing needs no secret: only the private key can open the backup again. Pushing a new
# backup starts the "Publish site" workflow.
#
#   sh tools/pack.sh <x-jobs-folder>      a folder opened from the backup, outside this repo
set -e
[ -n "$1" ] || { echo "usage: sh tools/pack.sh <x-jobs-folder>" >&2; exit 2; }
src=$(cd "$1" && pwd)
cd "$(dirname "$0")/.."
command -v age >/dev/null 2>&1 || { echo "age is not installed: apt-get install -y age (Linux) or brew install age (Mac)" >&2; exit 1; }
for f in index.html package.json src/login.html tools/site-build.mjs; do
  [ -f "$src/$f" ] || { echo "$src is not an X-Jobs folder: $f is missing." >&2; exit 1; }
done
case "$src/" in "$(pwd)/"*) echo "Open the backup outside this repo, not inside it." >&2; exit 1 ;; esac
ver=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["version"])' "$src/package.json")
mkdir -p backup
tar -C "$src" --exclude=.git --exclude=node_modules --exclude=_site --exclude=__pycache__ \
  --exclude=.DS_Store -czf - . | age -R keys/backup-recipient.txt -o backup/x-jobs.tar.gz.age
printf 'app: X-Jobs v%s · packed %s\n' "$ver" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > backup/BUILD.txt
echo "sealed $src (v$ver) into backup/x-jobs.tar.gz.age"
