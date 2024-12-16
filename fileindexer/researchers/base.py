import logging

logger = logging.getLogger('fileindexer')

class BaseResearcher:
    def supports(self, file_path: str) -> bool:
        return False

    def get_info(self, file_path: str) -> dict:
        return {}