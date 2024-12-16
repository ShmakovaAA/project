import logging
from mutagen import File
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class AudioResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        exts = ('.mp3', '.wav', '.m4a', '.flac')
        return file_path.lower().endswith(exts)

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            audio = File(file_path)
            if audio is not None and audio.info is not None:
                duration = audio.info.length
                bitrate = getattr(audio.info, 'bitrate', None)
                info['duration'] = duration
                if bitrate:
                    info['bitrate'] = bitrate
        except Exception as e:
            logger.warning(f"Ошибка при обработке аудио файла {file_path}: {e}")
        return info
