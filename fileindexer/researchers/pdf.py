import logging
from PyPDF2 import PdfReader
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class PDFResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        return file_path.lower().endswith('.pdf')

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            with open(file_path, 'rb') as f:
                reader = PdfReader(f)
                num_pages = len(reader.pages)
                metadata = reader.metadata
                page_formats = []
                for page in reader.pages:
                    width = float(page.mediabox.width)
                    height = float(page.mediabox.height)
                    page_formats.append(self.which_format(width, height))
                if len(set(page_formats)) == 1:
                    page_format = page_formats[0]
                else:
                    page_format = "Разные форматы"
                info['page_count'] = num_pages
                info['metadata'] = str(metadata) if metadata else ""
                info['page_format'] = page_format
        except Exception as e:
            logger.warning(f"Ошибка при обработке PDF {file_path}: {e}")
        return info

    def which_format(self, width, height):
        eps = 5
        possible_formats = {
            "A0": (2383.94, 3370.39),
            "A1": (1683.78, 2383.94),
            "A2": (1190.55, 1683.78),
            "A3": (841.89, 1190.55),
            "A4": (595.28, 841.89),
            "A5": (419.53, 595.28),
        }
        for name, size in possible_formats.items():
            default_width, default_height = size
            if (abs(width - default_width) <= eps and abs(height - default_height) <= eps) or \
               (abs(width - default_height) <= eps and abs(height - default_width) <= eps):
                return name
        return "Неизвестный формат"
