#!/usr/bin/env python3
"""Rewrites the "Latest updates" table in README.md from this repo's history.

Run by the Update log workflow after every push to main; it can also be run by hand. The table lists
the newest 3 updates on main: when each was made (UAE time and UTC), what changed (the first line of
the commit, without its "v1.0.1: " prefix), the app version at that commit (from backup/BUILD.txt) and the
commit. The commits that only save this table, and the hourly job-list refreshes ("data: ..."), are left out:
the table lists only the versions Jerrin pushed himself. Running it twice changes nothing.

    python3 tools/update-log.py            the history up to HEAD
    python3 tools/update-log.py origin/main
"""
import datetime, os, re, subprocess, sys

KEEP = 3
START, END = '<!-- latest-updates:start -->', '<!-- latest-updates:end -->'
LOG_SUBJECT = 'README: latest updates'
DATA_SUBJECT = 'data:'  # the hourly job-list refresh: never a version, never in the table
UAE = datetime.timezone(datetime.timedelta(hours=4), 'UAE')
REPO = os.environ.get('GITHUB_REPOSITORY', 'jerrin-v/x-job')
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
readme = os.path.join(root, 'README.md')
ref = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'

git = lambda *a: subprocess.check_output(['git', '-C', root, *a], text=True, stderr=subprocess.DEVNULL).strip()


def version_at(sha):  # the backup's BUILD.txt ("app: X-Jobs v1.0.1 · packed ...")
    try:
        m = re.search(r'X-Jobs (v\d+(?:\.\d+)+)', git('show', f'{sha}:backup/BUILD.txt'))
        if m: return m.group(1)
    except subprocess.CalledProcessError: pass
    return ''


DAYS, MONTHS = 'Mon Tue Wed Thu Fri Sat Sun'.split(), 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()


def fmt(d):  # Sat 14 Nov 2026, 9:05:07 AM
    return f'{DAYS[d.weekday()]} {d.day:02d} {MONTHS[d.month - 1]} {d.year}, {(d.hour + 11) % 12 + 1}:{d.minute:02d}:{d.second:02d} {"AM" if d.hour < 12 else "PM"}'


rows = []
for line in git('log', '--first-parent', '-n', '60', '--format=%H%x09%cI%x09%s', ref).splitlines():
    sha, when, subject = line.split('\t', 2)
    if subject.startswith(LOG_SUBJECT) or subject.startswith(DATA_SUBJECT) or subject.startswith("notes:"): continue
    when = datetime.datetime.fromisoformat(when)
    change = re.sub(r'^v\d+(?:\.\d+)+: *', '', subject).replace('|', '\\|')
    rows.append(f'| {fmt(when.astimezone(UAE))} UAE<br><sub>{fmt(when.astimezone(datetime.timezone.utc))} UTC</sub> '
                f'| {change} | {version_at(sha)} | [`{sha[:7]}`](https://github.com/{REPO}/commit/{sha}) |')
    if len(rows) == KEEP: break
head = ['| Updated | Change | Version | Commit |', '| --- | --- | --- | --- |']

text = open(readme, encoding='utf-8').read()
if text.count(START) != 1 or text.count(END) != 1:
    print('README.md has no latest-updates markers; nothing to do.'); sys.exit(0)
before, rest = text.split(START, 1)
block, after = rest.split(END, 1)
new = before + START + '\n' + '\n'.join(head + rows) + '\n' + END + after
if new == text:
    print('Latest updates already up to date.'); sys.exit(0)
open(readme, 'w', encoding='utf-8').write(new)
print(f'Listed {len(rows)} update(s), newest:', rows[0].split(' | ')[1] if rows else 'none')
