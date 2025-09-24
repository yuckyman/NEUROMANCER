#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
from datetime import datetime, timezone

LOGS = Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/logs")

# Superseding logic: keep only the latest row per id (by _ts).
def compact(filename: str) -> None:
	path = LOGS / filename
	if not path.exists():
		return
	rows = []
	with open(path, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			rows.append(row)
	rows.sort(key=lambda r: r.get("_ts", ""))
	latest = {}
	for r in rows:
		if "id" in r:
			latest[r["id"]] = r
	with open(path, "w", newline="") as f:
		if not rows:
			return
		writer = csv.DictWriter(f, fieldnames=list(rows[-1].keys()))
		writer.writeheader()
		for r in latest.values():
			writer.writerow(r)

if __name__ == "__main__":
	for name in ("tasks.csv", "notes.csv", "events.csv"):
		compact(name)
