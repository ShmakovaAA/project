# tests/test_pdf_researcher.py
from django.test import TestCase
from fileindexer.researchers.pdf import PDFResearcher

class PDFResearcherTestCase(TestCase):
    """
    Тестовый класс для проверки PDFResearcher.
    """

    def setUp(self): 
        """
        Инициализация объекта PDFResearcher для тестирования.
        """
        self.test_object = PDFResearcher()

    def test_supports_right_extension_pdf(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .pdf.
        """
        file_path = "home/user/somedir/document.pdf"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_unsupported_extension_txt(self):
        """
        Проверяет, что метод supports возвращает False для файла с неподдерживаемым расширением.
        """
        file_path = "home/user/somedir/document.txt"
        self.assertFalse(self.test_object.supports(file_path=file_path))

    def test_get_pdf_info_valid_pdf(self):
        """
        Проверяет корректное извлечение информации из валидного PDF файла.
        """
        file_path = "./tests/test_data/document.pdf"
        # Предполагается, что файл существует и доступен для тестирования
        info = self.test_object.get_info(file_path)
        self.assertIn('page_count', info)
        self.assertIn('metadata', info)
        self.assertIn('page_format', info)
        self.assertIsInstance(info['page_count'], int)
        self.assertIsInstance(info['metadata'], str)
        self.assertIsInstance(info['page_format'], str)

    def test_get_pdf_info_invalid_file(self):
        """
        Проверяет обработку некорректного PDF файла.
        """
        file_path = "./tests/test_data/invalid_document.pdf"
        info = self.test_object.get_info(file_path)
        self.assertEqual(info, {})
