# tests/test_excel_researcher.py
from django.test import TestCase
from fileindexer.researchers.excel import ExcelResearcher

class ExcelResearcherTestCase(TestCase):
    """
    Тестовый класс для проверки ExcelResearcher.
    """

    def setUp(self): 
        """
        Инициализация объекта ExcelResearcher для тестирования.
        """
        self.test_object = ExcelResearcher()

    def test_supports_right_extension(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .xlsx.
        """
        file_path = "home/user/somedir/file.xlsx"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_wrong_extension(self):
        """
        Проверяет, что метод supports возвращает False для файла с неподдерживаемым расширением.
        """
        file_path = "home/user/somedir/file.png"
        self.assertFalse(self.test_object.supports(file_path=file_path))

    def test_get_info_valid_excel(self):
        """
        Проверяет корректное извлечение информации из валидного Excel файла.
        """
        file_path = "./tests/test_data/test.xlsx"
        info = self.test_object.get_info(file_path)
        self.assertIn('page_count', info)
        self.assertIn('metadata', info)
        self.assertIsInstance(info['page_count'], int)
        self.assertIsInstance(info['metadata'], str)

    def test_get_info_invalid_file(self):
        """
        Проверяет обработку некорректного Excel файла.
        """
        file_path = "./tests/test_data/invalid.xlsx"
        info = self.test_object.get_info(file_path)
        self.assertEqual(info, {})
