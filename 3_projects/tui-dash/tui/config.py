from __future__ import annotations

from pathlib import Path
import yaml
from dataclasses import dataclass

CONFIG_DIR = Path("/Users/ian/NEUROMANCER/3_projects/tui-dash/config")

@dataclass(slots=True)
class AppConfig:
	paths: dict
	colors: dict
	keymap: dict


class ConfigLoader:
	def __init__(self, config_dir: Path = CONFIG_DIR):
		self.config_dir = config_dir

	def load(self) -> AppConfig:
		paths = self._load_yaml("paths.yaml")
		colors = self._load_yaml("colors.yaml")
		keymap = self._load_yaml("keymap.yaml")
		return AppConfig(paths=paths, colors=colors, keymap=keymap)

	def _load_yaml(self, filename: str) -> dict:
		path = self.config_dir / filename
		if not path.exists():
			return {}
		with open(path, "r") as f:
			return yaml.safe_load(f) or {}
