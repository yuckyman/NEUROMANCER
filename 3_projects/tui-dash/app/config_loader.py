from __future__ import annotations

from pathlib import Path
from .storage import TASKS_CSV, NOTES_CSV, EVENTS_CSV

DEFAULT_PATHS = {
	"logs": str(Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/logs")),
	"notes": str(Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/notes")),
	"archive": str(Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/archive")),
}

