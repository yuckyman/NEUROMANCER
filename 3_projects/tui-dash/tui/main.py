from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal
from textual.reactive import reactive
from textual import events
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from pathlib import Path
from datetime import datetime, timezone

from app.storage import TASKS_CSV, NOTES_CSV
from tui.rss_panel import RSSPanel


class EisenhowerPanel(Static):
	can_focus = True
	reload_requested = reactive(False)
	selected_task_id: str | None = None

	def on_mount(self) -> None:
		self.refresh_panel()

	def refresh_panel(self) -> None:
		latest = TASKS_CSV.latest_by_id("id")
		quadrants = {
			"urgent_important": [],
			"urgent_not_important": [],
			"not_urgent_important": [],
			"not_urgent_not_important": [],
		}
		for row in latest.values():
			quadrants.get(row.get("quadrant", ""), []).append(row)
		# stabilize ordering for navigation
		for q in quadrants.values():
			q.sort(key=lambda r: (r.get("state") == "done", r.get("_ts", "")))
		# initialize a selection if none
		if self.selected_task_id is None:
			for group in (
				quadrants["urgent_important"],
				quadrants["urgent_not_important"],
				quadrants["not_urgent_important"],
				quadrants["not_urgent_not_important"],
			):
				if group:
					self.selected_task_id = group[0].get("id")
					break
		table = Table.grid(padding=(0, 2), expand=True)
		table.add_row(
			self._q_table("urgent_important", quadrants["urgent_important"], self.selected_task_id),
			self._q_table("urgent_not_important", quadrants["urgent_not_important"], self.selected_task_id),
		)
		table.add_row(
			self._q_table("not_urgent_important", quadrants["not_urgent_important"], self.selected_task_id),
			self._q_table("not_urgent_not_important", quadrants["not_urgent_not_important"], self.selected_task_id),
		)
		self.update(Panel(table, title="eisenhower"))

	def _q_table(self, title: str, rows: list[dict], selected_id: str | None) -> Table:
		qt = Table(show_header=False, box=None, pad_edge=False, expand=True)
		qt.add_column("task", no_wrap=False, overflow="fold", ratio=1)
		# Bold quadrant header as the first row, aligned with tasks
		display_title = title.replace("_", " ")
		qt.add_row(Text(display_title, style="bold"))
		for r in rows[:5]:
			state = r.get("state", "todo")
			title = r.get("title", "")
			style = "dim" if state == "done" else None
			if selected_id and r.get("id") == selected_id:
				style = f"bold {style}" if style else "bold"
			qt.add_row(Text(title, style=style))
		return qt

	def action_mark_done(self) -> None:
		if not self.selected_task_id:
			return
		row = TASKS_CSV.latest_by_id("id").get(self.selected_task_id)
		if not row:
			return
		if row.get("state") != "done":
			row = dict(row)
			row["state"] = "done"
			TASKS_CSV.append(row)
		self.refresh_panel()

	def on_key(self, event) -> None:
		# simple navigation between tasks using j/k or arrows
		if event.key not in ("up", "down", "j", "k"):
			return
		latest = TASKS_CSV.latest_by_id("id")
		# order ids in quadrant order
		ordered: list[str] = []
		def push(qname: str) -> None:
			items = [r for r in latest.values() if r.get("quadrant") == qname]
			items.sort(key=lambda r: (r.get("state") == "done", r.get("_ts", "")))
			for r in items[:5]:
				if r.get("id"):
					ordered.append(r["id"])
		for q in (
			"urgent_important",
			"urgent_not_important",
			"not_urgent_important",
			"not_urgent_not_important",
		):
			push(q)
		if not ordered:
			return
		if self.selected_task_id not in ordered:
			self.selected_task_id = ordered[0]
		idx = ordered.index(self.selected_task_id)
		if event.key in ("down", "j"):
			idx = min(idx + 1, len(ordered) - 1)
		else:
			idx = max(idx - 1, 0)
		self.selected_task_id = ordered[idx]
		self.refresh_panel()

	# no custom scrolling here; widget isn't scrollable by default


class DashApp(App):
	CSS_PATH = None
	CSS = """
	#content { layout: horizontal; height: 1fr; }
	#eisenhower { width: 1fr; height: 1fr; border: round; }
	#rss { width: 1fr; height: 1fr; border: round; }
	#eisenhower:focus { border: heavy green; }
	#rss:focus { border: heavy green; }
	"""

	def compose(self) -> ComposeResult:
		yield Header()
		with Horizontal(id="content"):
			yield EisenhowerPanel(id="eisenhower")
			yield RSSPanel(id="rss")
		yield Footer()

	BINDINGS = [
		("n", "new_note", "new note"),
		("c", "mark_done", "complete"),
		("t", "focus_tasks", "tasks"),
		("r", "focus_rss", "rss"),
		("tab", "cycle_focus", "next pane"),
		("shift+tab", "cycle_focus_reverse", "prev pane"),
		("j", "move_down", "down"),
		("k", "move_up", "up"),
		("h", "page_left", "page-"),
		("l", "page_right", "page+"),
		("?", "help", "help"),
	]

	def action_new_note(self) -> None:
		notes_dir = Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/storage/notes")
		notes_dir.mkdir(parents=True, exist_ok=True)
		name = f"note-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.md"
		path = notes_dir / name
		path.write_text("# note\n\n")
		NOTES_CSV.append({"id": name, "title": name, "path": str(path)})
		self.bell()

	def action_mark_done(self) -> None:
		self.query_one(EisenhowerPanel).action_mark_done()

	def action_focus_tasks(self) -> None:
		self.set_focus(self.query_one("#eisenhower"))

	def action_focus_rss(self) -> None:
		self.set_focus(self.query_one("#rss"))

	def action_cycle_focus(self) -> None:
		# toggle between the two panes
		focused = self.focused
		self.set_focus(self.query_one("#rss" if getattr(focused, "id", None) == "eisenhower" else "#eisenhower"))

	def action_cycle_focus_reverse(self) -> None:
		self.action_cycle_focus()

	def action_move_down(self) -> None:
		focused = self.focused
		if isinstance(focused, RSSPanel):
			focused.move_down()
		elif isinstance(focused, EisenhowerPanel):
			focused.on_key(type("E", (), {"key": "down"})())

	def action_move_up(self) -> None:
		focused = self.focused
		if isinstance(focused, RSSPanel):
			focused.move_up()
		elif isinstance(focused, EisenhowerPanel):
			focused.on_key(type("E", (), {"key": "up"})())

	def action_page_left(self) -> None:
		focused = self.focused
		if isinstance(focused, RSSPanel):
			focused.page_left()

	def action_page_right(self) -> None:
		focused = self.focused
		if isinstance(focused, RSSPanel):
			focused.page_right()

if __name__ == "__main__":
	DashApp().run()
