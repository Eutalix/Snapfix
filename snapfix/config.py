import json
import logging
from pathlib import Path
from .constants import DEFAULT_SKIP_PATTERNS, DEFAULT_SKIP_NAME_PATTERNS, DEFAULT_FREEDESKTOP_CATEGORIES, DEFAULT_MAPPING

logger = logging.getLogger("snapfix")

class Config:
    def __init__(self, path: Path = None):
        self.skip_patterns = DEFAULT_SKIP_PATTERNS.copy()
        self.skip_name_patterns = DEFAULT_SKIP_NAME_PATTERNS.copy()
        self.freedesktop_categories = DEFAULT_FREEDESKTOP_CATEGORIES.copy()
        self.mapping = DEFAULT_MAPPING.copy()
        self.loop_interval = 300
        if path and path.exists():
            self.load(path)

    def load(self, path: Path):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            self.skip_patterns = data.get('skip_patterns', self.skip_patterns)
            self.skip_name_patterns = data.get('skip_name_patterns', self.skip_name_patterns)
            self.freedesktop_categories.update(data.get('freedesktop_categories', {}))
            self.mapping.update(data.get('mapping', {}))
            self.loop_interval = data.get('loop_interval', self.loop_interval)
            logger.info(f"Loaded config from {path}")
        except Exception as e:
            logger.warning(f"Failed loading config {path}: {e}")
