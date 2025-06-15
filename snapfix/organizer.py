import os
import time
import logging
from pathlib import Path
from .constants import MENU_DIR
from .info_reader import DesktopInfoReader
from .scanner import SnapScanner
from .icon_resolver import IconResolver
from .category_mapper import CategoryMapper
from .desktop_writer import DesktopWriter
from .utils import t

logger = logging.getLogger("snapfix")

class Organizer:
    def __init__(self, config, force: bool = False, debug: bool = False):
        self.config = config
        self.force = force
        if debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        logger.addHandler(handler)
        self.scanner = SnapScanner(config)
        self.mapper = CategoryMapper(config)
        self.writer = DesktopWriter()

    def organize_once(self):
        items = self.scanner.list_snap_desktops()
        existing = {p.name for p in MENU_DIR.glob('*.desktop')}
        added_any = False
        if not items:
            logger.info(t('no_snaps'))
            return
        for fname, path in items:
            if fname in existing and not self.force:
                logger.debug(f"Skipping existing entry: {fname}")
                continue
            info = DesktopInfoReader.read(path)
            name = info.get('Name') or fname[:-8]
            exec_ = info.get('Exec') or ''
            comment = info.get('Comment') or ''
            icon_raw = info.get('Icon') or ''
            cats_raw = info.get('Categories') or []
            icon_path = IconResolver.resolve(icon_raw, fname, desktop_path=path)
            categories = self.mapper.treat(cats_raw)
            if self.force and (MENU_DIR / fname).exists():
                try: (MENU_DIR / fname).unlink()
                except Exception: logger.debug(f"Could not remove existing {fname}")
            success = self.writer.write(fname, {'Name': name, 'Exec': exec_, 'Comment': comment}, icon_path, categories)
            if success: added_any = True
        if not added_any: logger.info(t('no_snaps'))

    def run_auto(self):
        logger.info(t('auto_mode'))
        try:
            while True:
                logger.info(t('manual_mode'))
                self.organize_once()
                time.sleep(self.config.loop_interval)
        except KeyboardInterrupt:
            logger.info("Exiting snapfix...")
