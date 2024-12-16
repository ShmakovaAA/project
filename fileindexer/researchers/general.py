import os
from .base import BaseResearcher

class GeneralResearcher(BaseResearcher):
    def supports(self, file_path: str) -> bool:
        return True

    def get_info(self, file_path: str) -> dict:
        size_bytes = os.path.getsize(file_path)
        return {'size_bytes': size_bytes}
