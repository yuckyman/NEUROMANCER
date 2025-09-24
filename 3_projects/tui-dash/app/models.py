from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional

TaskState = Literal["todo", "doing", "done", "blocked"]

@dataclass(slots=True)
class Task:
	id: str
	title: str
	quadrant: Literal["urgent_important", "urgent_not_important", "not_urgent_important", "not_urgent_not_important"]
	state: TaskState = "todo"
	created_at: datetime | None = None
	completed_at: datetime | None = None
	notes: str = ""


@dataclass(slots=True)
class Note:
	id: str
	title: str
	path: str
	created_at: datetime
	modified_at: Optional[datetime] = None
