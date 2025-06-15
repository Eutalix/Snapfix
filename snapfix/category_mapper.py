import logging
from .constants import MESSAGES
from .utils import t

logger = logging.getLogger("snapfix")

class CategoryMapper:
    def __init__(self, config):
        self.fd = config.freedesktop_categories
        self.map_custom = config.mapping

    def map(self, raw: str) -> str:
        try:
            if raw in self.map_custom: return self.map_custom[raw]
            if raw in self.fd: return self.fd[raw]
            for k, v in self.fd.items():
                if k.lower() == raw.lower(): return v
                if isinstance(v, str) and v.lower() == raw.lower(): return v
        except Exception:
            return None
        return None

    def treat(self, raw_list: list) -> list:
        finals = []
        seen = set()
        for raw in raw_list:
            try:
                mapped = self.map(raw)
                if mapped and mapped not in seen:
                    finals.append(mapped); seen.add(mapped)
                elif not mapped:
                    logger.warning(f"{t('warn_no_category')} {raw}")
            except Exception:
                logger.warning(f"{t('warn_no_category')} {raw} (error)")
        return finals
