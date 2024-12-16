import logging
from PIL import Image
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class ImageResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
        return file_path.lower().endswith(exts)

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                dpi = img.info.get('dpi', (None, None))
                exif_data = None
                if hasattr(img, '_getexif'):
                    exif_data = img._getexif()
                info['width'] = width
                info['height'] = height
                if dpi and dpi[0] and dpi[1]:
                    info['dpi'] = f"{dpi[0]}x{dpi[1]}"
                info['metadata'] = f"EXIF: {exif_data}" if exif_data else ""
        except Exception as e:
            logger.warning(f"Ошибка при обработке изображения {file_path}: {e}")
        return info
