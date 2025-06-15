import locale
import logging
from .constants import MESSAGES

# Configura logger
logger = logging.getLogger("snapfix")

# Detector de idioma
def detect_language():
    loc, _ = locale.getdefaultlocale()
    return 'pt' if loc and loc.startswith('pt') else 'en'
LANG = detect_language()

# Função de tradução de chaves de mensagens
def t(key: str, **kwargs) -> str:
    msg = MESSAGES.get(LANG, MESSAGES['en']).get(key, key)
    return msg.format(**kwargs) if kwargs else msg
