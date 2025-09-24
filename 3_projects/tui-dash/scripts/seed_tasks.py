from __future__ import annotations

from datetime import datetime, timezone

from app.storage import TASKS_CSV


def seed() -> None:
	# one per quadrant
	TASKS_CSV.append(
		{
			"id": "thesis-emails",
			"title": "send emails for grad thesis advisory",
			"quadrant": "urgent_important",
			"state": "todo",
		}
	)
	TASKS_CSV.append(
		{
			"id": "clip-toenails",
			"title": "clip toenails",
			"quadrant": "urgent_not_important",
			"state": "todo",
		}
	)
	TASKS_CSV.append(
		{
			"id": "pushups-24",
			"title": "do 24 push ups",
			"quadrant": "not_urgent_important",
			"state": "todo",
		}
	)
	TASKS_CSV.append(
		{
			"id": "clean-out-car",
			"title": "clean out car",
			"quadrant": "not_urgent_not_important",
			"state": "todo",
		}
	)


if __name__ == "__main__":
	seed()
	print("seeded 4 tasks")


