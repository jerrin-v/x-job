#!/bin/sh
# Seals a fresh copy of the job list for the website into backup/data.json.age with the public key in
# keys/backup-recipient.txt, and notes when in backup/DATA.txt. Needs no secret. The hourly "X-Jobs search"
# and "X-Jobs Poli" tasks run it; pushing the result republishes the site with the new list.
#
#   sh tools/pack-data.sh <jobs-folder> [meta-status.json] [tracking-folder]
# <jobs-folder> and <tracking-folder> are the "jobs" and "tracking" collections exported from the database.
set -e
[ -n "$1" ] || { echo "usage: sh tools/pack-data.sh <jobs-folder> [meta-status.json] [tracking-folder]" >&2; exit 2; }
src=$(cd "$1" && pwd); meta=${2:-}; track=""
[ -n "$3" ] && track=$(cd "$3" && pwd)
cd "$(dirname "$0")/.."
command -v age >/dev/null 2>&1 || { echo "age is not installed: apt-get install -y age (Linux) or brew install age (Mac)" >&2; exit 1; }
case "$src/" in "$(pwd)/"*) echo "Keep the export outside this repo." >&2; exit 1 ;; esac
tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
python3 tools/make-data.py "$src" "$tmp" "${meta:-none}" $track
mkdir -p backup
age -R keys/backup-recipient.txt -o backup/data.json.age "$tmp"
printf 'job list · packed %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > backup/DATA.txt
echo "sealed the job list into backup/data.json.age"
