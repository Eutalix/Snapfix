import logging
from .utils import t, LANG

logger = logging.getLogger("snapfix")

class CommentTranslator:
    @staticmethod
    def translate(comment: str) -> str:
        try:
            from deep_translator import GoogleTranslator
        except ImportError:
            logger.debug(t('warn_no_translator'))
            return comment
        try:
            translated = GoogleTranslator(source='auto', target=LANG).translate(comment)
            if not translated or translated.strip().lower() == comment.strip().lower():
                return comment
            return translated
        except Exception as e:
            logger.debug(f"Translation error: {e}")
            return comment
