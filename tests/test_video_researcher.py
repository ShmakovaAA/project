# tests/test_video_researcher.py
from django.test import TestCase
from fileindexer.researchers.video import VideoResearcher

class VideoResearcherTestCase(TestCase):
    """
    Тестовый класс для проверки VideoResearcher.
    """

    def setUp(self): 
        """
        Инициализация объекта VideoResearcher для тестирования.
        """
        self.test_object = VideoResearcher()

    def test_supports_right_extension_mp4(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .mp4.
        """
        file_path = "home/user/somedir/video.mp4"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_unsupported_extension_txt(self):
        """
        Проверяет, что метод supports возвращает False для файла с неподдерживаемым расширением.
        """
        file_path = "home/user/somedir/video.txt"
        self.assertFalse(self.test_object.supports(file_path=file_path))

    def test_get_video_info_valid_mp4(self):
        """
        Проверяет корректное извлечение информации из валидного MP4 файла.
        """
        file_path = "./tests/test_data/video.mp4"
        # Предполагается, что файл существует и доступен для тестирования
        info = self.test_object.get_info(file_path)
        self.assertIn('width', info)
        self.assertIn('height', info)
        self.assertIn('duration', info)
        self.assertIn('metadata', info)
        self.assertIsInstance(info['width'], int)
        self.assertIsInstance(info['height'], int)
        self.assertIsInstance(info['duration'], float)
        self.assertIsInstance(info['metadata'], str)

    def test_get_video_info_invalid_file(self):
        """
        Проверяет обработку некорректного видео файла.
        """
        file_path = "./tests/test_data/invalid_video.mp4"
        info = self.test_object.get_info(file_path)
        self.assertEqual(info, {})
