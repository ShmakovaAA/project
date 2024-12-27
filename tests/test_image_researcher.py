# tests/test_image_researcher.py
from django.test import TestCase
from fileindexer.researchers.image import ImageResearcher

class ImageResearcherTestCase(TestCase):
    """
    Тестовый класс для проверки ImageResearcher.
    """

    def setUp(self):
        """
        Инициализация объекта ImageResearcher для тестирования.
        """
        self.test_object = ImageResearcher()

    def test_supports_right_extension_jpg(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .jpg.
        """
        file_path = "home/user/somedir/image.jpg"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_unsupported_extension_txt(self):
        """
        Проверяет, что метод supports возвращает False для файла с неподдерживаемым расширением.
        """
        file_path = "home/user/somedir/image.txt"
        self.assertFalse(self.test_object.supports(file_path=file_path))

    def test_get_image_info_valid_jpg(self):
        """
        Проверяет корректное извлечение информации из валидного JPG файла.
        """
        file_path = "./tests/test_data/image.jpg"
        # Предполагается, что файл существует и доступен для тестирования
        info = self.test_object.get_info(file_path)
        self.assertIn('width', info)
        self.assertIn('height', info)
        self.assertIn('dpi', info)
        self.assertIsInstance(info['width'], int)
        self.assertIsInstance(info['height'], int)
        self.assertIsInstance(info['dpi'], str)

    def test_get_image_info_invalid_file(self):
        """
        Проверяет обработку некорректного изображения.
        """
        file_path = "./tests/test_data/invalid_image.jpg"
        info = self.test_object.get_info(file_path)
        self.assertEqual(info, {})
