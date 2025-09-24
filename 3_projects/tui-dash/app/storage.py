from __future__ import annotations

import csv
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Optional, Dict, List

LOG_DIR = Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/logs")

class AppendOnlyCSV:
	def __init__(self, file_path: Path):
		self.file_path = file_path
		self.file_path.parent.mkdir(parents=True, exist_ok=True)

	def append(self, row: Mapping[str, object]) -> None:
		new_row = dict(row)
		new_row["_ts"] = datetime.now(timezone.utc).isoformat()
		is_new_file = not self.file_path.exists() or self.file_path.stat().st_size == 0
		with open(self.file_path, "a", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=list(new_row.keys()))
			if is_new_file:
				writer.writeheader()
			writer.writerow(new_row)

	def append_dataclass(self, obj) -> None:
		self.append(asdict(obj))

	def read_all(self) -> List[Dict[str, str]]:
		if not self.file_path.exists() or self.file_path.stat().st_size == 0:
			return []
		with open(self.file_path, "r") as f:
			reader = csv.DictReader(f)
			return list(reader)

	def latest_by_id(self, id_field: str = "id") -> Dict[str, Dict[str, str]]:
		rows = self.read_all()
		# sort ascending by timestamp so later entries overwrite earlier
		rows.sort(key=lambda r: r.get("_ts", ""))
		latest: Dict[str, Dict[str, str]] = {}
		for row in rows:
			if id_field in row and row[id_field]:
				latest[row[id_field]] = row
		return latest


TASKS_CSV = AppendOnlyCSV(LOG_DIR / "tasks.csv")
NOTES_CSV = AppendOnlyCSV(LOG_DIR / "notes.csv")
EVENTS_CSV = AppendOnlyCSV(LOG_DIR / "events.csv")


__all__ = ["AppendOnlyCSV", "TASKS_CSV", "NOTES_CSV", "EVENTS_CSV"]
