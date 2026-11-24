#!/usr/bin/env python3
"""Builds the job-list copy for the website from an export of the X-Jobs database.

    python3 tools/make-data.py <export-folder> <out.json> [meta-status.json] [tracking-folder]

<export-folder> holds the "jobs" collection as written by the database tools: any mix of .json files (one
document, a list of documents, or {"documents": [...]}) and .jsonl files (one document per line). A document
is {"id": ..., "data": {...}}; a .json file that is the bare data takes its id from the file name. The
"jobs" documents go in, plus, when a tracking folder is given, Jerrin's own marks per job (applied, saved, hidden,
with their dates; never his notes), so a job he marked applied on claude.ai is not offered again on the website.
No settings, nothing else personal beyond the first name used in the greeting.
"""
import datetime, json, os, sys

src, out = sys.argv[1], sys.argv[2]
meta_file = sys.argv[3] if len(sys.argv) > 3 else None
track_dir = sys.argv[4] if len(sys.argv) > 4 else None
TRACK_KEEP = ("status", "appliedAt", "stage", "updatedAt")
KEEP = ("title company location regions mode modeNote sponsor sponsorNote level focus exp salary url source posted "
        "found checked checkedOn fit why closed closedOn closedNote closedBy").split()
jobs = {}
tracking = {}
mode = "jobs"


def take(doc, fallback_id=None):
    if not isinstance(doc, dict): return
    if isinstance(doc.get("data"), dict) and ("id" in doc or "path" in doc):
        jid, data = str(doc.get("id") or doc.get("path", "")).split("/")[-1], doc["data"]
        if mode == "tracking":
            clean = {k: data[k] for k in TRACK_KEEP if isinstance(data.get(k), str) and data[k]}
            if jid and clean: tracking[jid] = clean
            return
    elif mode == "tracking":
        if fallback_id and ("status" in doc or "updatedAt" in doc):
            clean = {k: doc[k] for k in TRACK_KEEP if isinstance(doc.get(k), str) and doc[k]}
            if clean: tracking[fallback_id] = clean
        return
    elif "title" in doc and "company" in doc and fallback_id:
        jid, data = fallback_id, doc
    else:
        return
    if not jid or not data.get("title"): return
    url = str(data.get("url") or "")
    clean = {k: data[k] for k in KEEP if k in data and data[k] not in (None, "")}
    if url and not url.startswith("https://"): clean.pop("url", None)
    jobs[jid] = clean


def walk(obj, fallback_id=None):
    if isinstance(obj, list):
        for x in obj: walk(x)
    elif isinstance(obj, dict):
        for key in ("documents", "docs", "items", "results"):
            if isinstance(obj.get(key), list): return walk(obj[key])
        take(obj, fallback_id)


def read_folder(folder):
    for root, _, files in os.walk(folder):
        for name in sorted(files):
            path = os.path.join(root, name)
            text = open(path, encoding="utf-8", errors="replace").read()
            if name.endswith(".jsonl"):
                for line in text.splitlines():
                    line = line.strip()
                    if line.startswith("{"):
                        try: walk(json.loads(line))
                        except ValueError: pass
            elif name.endswith(".json"):
                try: walk(json.loads(text), os.path.splitext(name)[0])
                except ValueError: pass


read_folder(src)
if track_dir and os.path.isdir(track_dir):
    mode = "tracking"
    read_folder(track_dir)
    tracking = {k: v for k, v in tracking.items() if k in jobs}

if len(jobs) < 5:
    sys.exit("make-data: only %d job(s) found in %s. Nothing written." % (len(jobs), src))
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
status = {"lastRun": now}
if meta_file and os.path.exists(meta_file):
    try:
        m = json.load(open(meta_file, encoding="utf-8")); m = m.get("data", m)
        if isinstance(m, dict): status.update({k: m[k] for k in ("lastRun", "summary") if m.get(k)})
    except ValueError: pass
snap = {"takenAt": now, "data": {"jobs": jobs, "tracking": tracking, "settings": {"profile": {"fullName": "Jerrin Varghese"}}, "meta": {"status": status}}}
json.dump(snap, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("make-data: %d jobs, %d open, %d marked by Jerrin" % (len(jobs), sum(1 for j in jobs.values() if not j.get("closed")), len(tracking)))
