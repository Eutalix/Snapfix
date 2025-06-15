import logging
from pathlib import Path
from .constants import MENU_DIR
from .utils import t, LANG
from .comment_translator import CommentTranslator

logger = logging.getLogger("snapfix")

class DesktopWriter:
    def __init__(self):
        MENU_DIR.mkdir(parents=True, exist_ok=True)
    def write(self, fname: str, info: dict, icon_path: str, categories: list) -> bool:
        dest = MENU_DIR / fname
        name_base = fname[:-8] if fname.endswith('.desktop') else fname
        parts = name_base.split('_')
        snap_name = parts[0] if parts else name_base
        try:
            with open(dest, 'w', encoding='utf-8') as f:
                f.write('[Desktop Entry]\nType=Application\n')
                f.write(f"Name={info.get('Name')}\n")
                comment = info.get('Comment')
                if comment:
                    translated = CommentTranslator.translate(comment)
                    f.write(f"Comment={comment}\n")
                    f.write(f"Comment[{LANG}]={translated}\n")
                exec_line = info.get('Exec')
                if exec_line:
                    f.write(f"Exec={exec_line}\n")
                if icon_path:
                    f.write(f"Icon={icon_path}\n")
                if categories:
                    line = ';'.join(categories) + ';'
                    f.write(f"Categories={line}\n")
                action_key = t('uninstall_action')
                uninstall_cmd = t('uninstall_exec').format(snap_name=snap_name)
                f.write(f"Actions={action_key};\nTerminal=false\n")
                f.write(f"\n[Desktop Action {action_key}]\n")
                f.write(f"Name={action_key}\nExec={uninstall_cmd}\n")
            logger.info(f"{t('added')} {info.get('Name')} ({fname})")
            return True
        except Exception as e:
            logger.error(f"Failed to write desktop entry {fname}: {e}")
            return False
