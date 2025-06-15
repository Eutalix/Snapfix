import os
import sys
import subprocess
import argparse
import logging
from pathlib import Path
from .config import Config
from .utils import t, logger
from .organizer import Organizer
from .autostart import setup_autostart
from .constants import DEFAULT_CONFIG_PATH

logger = logging.getLogger("snapfix")

def main():
    parser = argparse.ArgumentParser(prog='snapfix', description='Organize Snap .desktop entries')
    parser.add_argument('--config', type=Path, default=DEFAULT_CONFIG_PATH, help='Path to JSON config file')
    parser.add_argument('--background', action='store_true', help='Spawn background auto mode')
    parser.add_argument('--autostart', '--install-startup', action='store_true', help='Add to startup')
    parser.add_argument('--auto', action='store_true', help='Run continuously')
    parser.add_argument('--force', action='store_true', help='Force overwrite existing entries')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--version', action='version', version='snapfix 1.0')
    args = parser.parse_args()

    config = Config(args.config)
    logger.info(t('start'))
    if args.background:
        try:
            subprocess.Popen([sys.executable, os.path.realpath(__file__), '--auto'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            logger.info(t('background_spawned'))
        except Exception as e:
            logger.error(f"Failed to spawn background: {e}")
        sys.exit(0)
    if args.autostart:
        setup_autostart()
        sys.exit(0)
    organizer = Organizer(config, force=args.force, debug=args.debug)
    if args.auto:
        organizer.run_auto()
    else:
        organizer.organize_once()

if __name__ == '__main__':
    main()
