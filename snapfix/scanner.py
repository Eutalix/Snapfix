import os
import logging
from .constants import SNAP_DESKTOP_DIR, SNAP_MOUNT_DIR
from .info_reader import DesktopInfoReader

logger = logging.getLogger("snapfix")

class SnapScanner:
    def __init__(self, config):
        self.config = config

    def should_skip(self, fname: str, path: str) -> bool:
        lower = fname.lower()
        for pat in self.config.skip_patterns:
            if pat in lower:
                logger.debug(f"Skipping by pattern: {fname}")
                return True
        info = DesktopInfoReader.read(path)
        name = info.get("Name", "").lower()
        for pat in self.config.skip_name_patterns:
            if pat in name:
                logger.debug(f"Skipping by name pattern: {fname}")
                return True
        return False

    def list_snap_desktops(self):
        results = {}
        # Diretório padrão
        if os.path.isdir(SNAP_DESKTOP_DIR):
            for fname in os.listdir(SNAP_DESKTOP_DIR):
                if not fname.endswith('.desktop'): continue
                full = os.path.join(SNAP_DESKTOP_DIR, fname)
                if self.should_skip(fname, full): continue
                results[fname] = full
        # Montagens Snap
        if os.path.isdir(SNAP_MOUNT_DIR):
            for snap_name in os.listdir(SNAP_MOUNT_DIR):
                snap_path = os.path.join(SNAP_MOUNT_DIR, snap_name)
                if not os.path.isdir(snap_path): continue
                for rev in os.listdir(snap_path):
                    rev_path = os.path.join(snap_path, rev)
                    for subdir in ['snap/gui', 'meta/gui']:
                        gui_path = os.path.join(rev_path, subdir)
                        if os.path.isdir(gui_path):
                            for fname in os.listdir(gui_path):
                                if not fname.endswith('.desktop'): continue
                                full = os.path.join(gui_path, fname)
                                if self.should_skip(fname, full): continue
                                if fname not in results:
                                    results[fname] = full
        logger.debug(f"Found snap desktops: {list(results.keys())}")
        return sorted(results.items(), key=lambda x: x[0].lower())
