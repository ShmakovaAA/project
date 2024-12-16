import logging
import openpyxl
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class ExcelResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        return file_path.lower().endswith('.xlsx')

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            wb = openpyxl.load_workbook(file_path, read_only=True)
            metadata = wb.properties
            num_sheets = len(wb.sheetnames)
            meta_dict = {
                'title': metadata.title,
                'subject': metadata.subject,
                'creator': metadata.creator,
                'keywords': metadata.keywords,
                'description': metadata.description,
                'category': metadata.category,
                'created': str(metadata.created) if metadata.created else None,
                'modified': str(metadata.modified) if metadata.modified else None,
            }
            info['page_count'] = num_sheets
            info['metadata'] = str(meta_dict)
        except Exception as e:
            logger.warning(f"Ошибка при обработке Excel файла {file_path}: {e}")
        return info
