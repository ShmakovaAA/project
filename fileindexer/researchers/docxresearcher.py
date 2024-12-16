import logging
import docx
from .base import BaseResearcher

logger = logging.getLogger('fileindexer')

class DocxResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        return file_path.lower().endswith('.docx')

    def get_info(self, file_path: str) -> dict:
        info = {}
        try:
            document = docx.Document(file_path)
            num_paragraphs = len(document.paragraphs)
            metadata = document.core_properties
            meta_dict = {
                'title': metadata.title,
                'subject': metadata.subject,
                'creator': metadata.creator,
                'keywords': metadata.keywords,
                'description': metadata.description,
                'category': metadata.category,
                'comments': metadata.comments,
                'created': str(metadata.created) if metadata.created else None,
                'modified': str(metadata.modified) if metadata.modified else None,
            }
            info['page_count'] = num_paragraphs
            info['metadata'] = str(meta_dict)
        except Exception as e:
            logger.warning(f"Ошибка при обработке DOCX {file_path}: {e}")
        return info
