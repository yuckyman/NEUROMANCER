#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import csv

LOGS = Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/logs")

# Daily reset: write a marker event row and optionally rotate tasks.
def daily_reset() -> None:
	with open(LOGS / "events.csv", "a", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=["type", "message", "_ts"])
		is_new = (LOGS / "events.csv").stat().st_size == 0 if (LOGS / "events.csv").exists() else True
		if is_new:
			writer.writeheader()
		writer.writerow({"type": "daily_reset", "message": "midnight rollover", "_ts": datetime.now(timezone.utc).isoformat()})

if __name__ == "__main__":
	daily_reset()
