import configparser
import logging

logger = logging.getLogger("snapfix")

class DesktopInfoReader:
    @staticmethod
    def read(path: str) -> dict:
        parser = configparser.RawConfigParser(interpolation=None)
        try:
            parser.read(path, encoding='utf-8')
        except Exception as e:
            logger.debug(f"Failed reading desktop file {path}: {e}")
            return {}
        if not parser.has_section('Desktop Entry'):
            return {}
        entry = parser['Desktop Entry']
        info = {}
        for key in ['Name', 'Exec', 'Comment', 'Icon', 'Categories']:
            try:
                val = entry.get(key, '').strip()
                if key == 'Categories':
                    info[key] = [c.strip() for c in val.split(';') if c.strip()]
                else:
                    info[key] = val
            except Exception:
                info[key] = ''
        return info
