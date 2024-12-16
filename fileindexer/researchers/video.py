import logging
import cv2
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class VideoResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        exts = ('.mp4', '.avi', '.mkv', '.mov', '.wmv')
        return file_path.lower().endswith(exts)

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            video = cv2.VideoCapture(file_path)
            if video.isOpened():
                width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fps = video.get(cv2.CAP_PROP_FPS)
                frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
                duration = frame_count / fps if fps else 0
                info['width'] = width
                info['height'] = height
                info['duration'] = duration
                info['metadata'] = f"FPS: {fps}"
        except Exception as e:
            logger.warning(f"Ошибка при обработке видео файла {file_path}: {e}")
        return info
