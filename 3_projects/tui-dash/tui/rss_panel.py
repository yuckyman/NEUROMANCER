from __future__ import annotations

import os
import json
from typing import Iterable
from pathlib import Path

import feedparser  # type: ignore
from textual.widgets import Static
from textual.app import ComposeResult
from textual.reactive import reactive
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


DEFAULT_FEEDS_JSON = Path("/Users/ian/NEUROMANCER/0_admin/07_scripts/rss_feeds.json")


class RSSPanel(Static):
	can_focus = True
	loading = reactive(False)
	feeds: list[str] = []
	items: list[dict] = []
	index: int = 0
	page: int = 0
	page_size: int = 8

	def on_focus(self) -> None:
		# lazy-load on first focus
		if not self.loading and not self.items:
			self._load_and_render()

	def _load_and_render(self) -> None:
		self.loading = True
		self.update(Panel(Text("loading feeds...", style="dim"), title="rss"))
		try:
			self.feeds = self._load_feeds()
			self.items = self._fetch_all(self.feeds)
			table = self._render_table(self.items, self.index, self.page, self.page_size)
			self.update(Panel(table, title="rss"))
		finally:
			self.loading = False

	def on_key(self, event) -> None:  # allow simple scrolling via arrow keys
		if event.key == "up":
			self.scroll_lines(-1)
		elif event.key == "down":
			self.scroll_lines(1)
		elif event.key == "pageup":
			self.scroll_page_up()
		elif event.key == "pagedown":
			self.scroll_page_down()

	def _load_feeds(self) -> list[str]:
		path_str = os.environ.get("RSS_FEEDS_JSON")
		path = Path(path_str) if path_str else DEFAULT_FEEDS_JSON
		if not path.exists():
			return []
		try:
			data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
			if isinstance(data, list):
				# list of urls or objects
				urls: list[str] = []
				for item in data:
					if isinstance(item, str):
						urls.append(item)
					elif isinstance(item, dict) and "url" in item:
						urls.append(str(item["url"]))
				return urls
			elif isinstance(data, dict):
				feeds = data.get("feeds")
				if isinstance(feeds, list):
					urls: list[str] = []
					for item in feeds:
						if isinstance(item, str):
							urls.append(item)
						elif isinstance(item, dict) and "url" in item:
							urls.append(str(item["url"]))
					return urls
			return []
		except Exception:
			return []

	def _fetch_all(self, urls: Iterable[str]) -> list[dict]:
		entries: list[dict] = []
		for url in urls:
			try:
				parsed = feedparser.parse(url)
				source = parsed.feed.get("title", url) if hasattr(parsed, "feed") else url
				for e in parsed.entries[:10]:
					entries.append(
						{
							"source": source,
							"title": e.get("title", ""),
							"link": e.get("link", ""),
							"published": getattr(e, "published", ""),
						}
					)
			except Exception:
				continue
		# sort by published string desc as a rough proxy
		entries.sort(key=lambda x: x.get("published", ""), reverse=True)
		return entries[:100]

	def _render_table(self, items: list[dict], highlight_index: int, page: int, page_size: int) -> Table:
		t = Table(show_header=True, expand=True, pad_edge=False)
		t.add_column("source", style="bold", ratio=1)
		t.add_column("title", ratio=3, overflow="fold", no_wrap=False)
		start = page * page_size
		end = min(start + page_size, len(items))
		for i in range(start, end):
			it = items[i]
			src = str(it.get("source", ""))
			title = str(it.get("title", ""))
			row_style = "bold" if i == highlight_index else None
			t.add_row(Text(src, style=row_style), Text(title, style=row_style))
		return t

	def on_key(self, event) -> None:
		if not self.items:
			return
		if event.key in ("down", "j"):
			self.index = min(self.index + 1, len(self.items) - 1)
			# advance page if needed
			if self.index >= (self.page + 1) * self.page_size:
				self.page += 1
			self.update(Panel(self._render_table(self.items, self.index, self.page, self.page_size), title="rss"))
		elif event.key in ("up", "k"):
			self.index = max(self.index - 1, 0)
			if self.index < self.page * self.page_size:
				self.page = max(self.page - 1, 0)
			self.update(Panel(self._render_table(self.items, self.index, self.page, self.page_size), title="rss"))
		elif event.key in ("right", "l"):
			if (self.page + 1) * self.page_size < len(self.items):
				self.page += 1
				self.index = min(self.index, len(self.items) - 1)
				if self.index < self.page * self.page_size:
					self.index = self.page * self.page_size
			self.update(Panel(self._render_table(self.items, self.index, self.page, self.page_size), title="rss"))
		elif event.key in ("left", "h"):
			if self.page > 0:
				self.page -= 1
				if self.index >= (self.page + 1) * self.page_size:
					self.index = (self.page + 1) * self.page_size - 1
			self.update(Panel(self._render_table(self.items, self.index, self.page, self.page_size), title="rss"))

	# helpers for app-level actions to route to
	def move_down(self) -> None:
		self.on_key(type("E", (), {"key": "down"})())

	def move_up(self) -> None:
		self.on_key(type("E", (), {"key": "up"})())

	def page_left(self) -> None:
		self.on_key(type("E", (), {"key": "left"})())

	def page_right(self) -> None:
		self.on_key(type("E", (), {"key": "right"})())


