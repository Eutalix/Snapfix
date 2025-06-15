import os
import sys
import logging
from pathlib import Path
from .constants import AUTOSTART_DIR
from .utils import t

logger = logging.getLogger("snapfix")

def setup_autostart():
    try:
        AUTOSTART_DIR.mkdir(parents=True, exist_ok=True)
        script = os.path.realpath(__file__)
        desktop_file = AUTOSTART_DIR / 'snapfix.desktop'
        content = (
            '[Desktop Entry]\n'
            'Type=Application\n'
            f'Exec={sys.executable} {script} --auto\n'
            'Hidden=false\n'
            'NoDisplay=false\n'
            'X-GNOME-Autostart-enabled=true\n'
            'Name=snapfix\n'
            'Comment=Automate Snap .desktop entries\n'
        )
        with open(desktop_file, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(t('autostart_ok'))
    except Exception as e:
        logger.error(f"Failed to setup autostart: {e}")
