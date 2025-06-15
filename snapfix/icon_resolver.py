import os
from pathlib import Path
import logging
from .constants import SNAP_MOUNT_DIR

logger = logging.getLogger("snapfix")

class IconResolver:
    @staticmethod
    def resolve(icon_raw: str, snap_fname: str, desktop_path: str) -> str:
        try:
            if icon_raw and '${SNAP}' in icon_raw and desktop_path:
                p = Path(desktop_path).resolve()
                parts = p.parts
                base = snap_fname[:-8] if snap_fname.endswith('.desktop') else snap_fname
                for i, part in enumerate(parts):
                    if part == base and i+1 < len(parts):
                        rev = parts[i+1]
                        mount_dir = os.path.join(SNAP_MOUNT_DIR, part, rev)
                        candidate = icon_raw.replace('${SNAP}', mount_dir)
                        if os.path.exists(candidate): return candidate
                icon_raw = icon_raw.replace('${SNAP}', '')
            if icon_raw and os.path.isabs(icon_raw) and os.path.exists(icon_raw):
                return icon_raw
            name_base = snap_fname[:-8] if snap_fname.endswith('.desktop') else snap_fname
            candidate1 = f"/var/lib/snapd/desktop/icons/{name_base}.png"
            if os.path.exists(candidate1): return candidate1
            parts = name_base.split('_')
            snap_name = parts[0] if parts else name_base
            snap_root = os.path.join(SNAP_MOUNT_DIR, snap_name)
            if os.path.isdir(snap_root):
                for rev in os.listdir(snap_root):
                    for sub in ['meta/gui', 'snap/gui']:
                        cand = os.path.join(snap_root, rev, sub, f"{snap_name}.png")
                        if os.path.exists(cand): return cand
            if desktop_path:
                dirpath = os.path.dirname(desktop_path)
                for fn in os.listdir(dirpath):
                    if fn.lower().endswith(('.png', '.svg', '.xpm')):
                        return os.path.join(dirpath, fn)
        except Exception as e:
            logger.debug(f"IconResolver error for {snap_fname}: {e}")
        return ''
