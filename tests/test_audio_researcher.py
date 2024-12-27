# tests/test_audio_researcher.py
from django.test import TestCase
from fileindexer.researchers.audio import AudioResearcher

class AudioResearcherTestCase(TestCase):
    """
    Тестовый класс для проверки AudioResearcher.
    """

    def setUp(self): 
        """
        Инициализация объекта AudioResearcher для тестирования.
        """
        self.test_object = AudioResearcher()

    def test_supports_right_extension_mp3(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .mp3.
        """
        file_path = "home/user/somedir/audio.mp3"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_supported_extension_wav(self):
        """
        Проверяет, что метод supports возвращает True для файла с расширением .wav.
        """
        file_path = "home/user/somedir/audio.wav"
        self.assertTrue(self.test_object.supports(file_path=file_path))

    def test_supports_unsupported_extension_txt(self):
        """
        Проверяет, что метод supports возвращает False для файла с неподдерживаемым расширением.
        """
        file_path = "home/user/somedir/audio.txt"
        self.assertFalse(self.test_object.supports(file_path=file_path))

    def test_get_audio_info_valid_mp3(self):
        """
        Проверяет корректное извлечение информации из валидного MP3 файла.
        """
        file_path = "./tests/test_data/audio.mp3"
        # Предполагается, что файл существует и доступен для тестирования
        info = self.test_object.get_info(file_path)
        self.assertIn('duration', info)
        self.assertIn('bitrate', info)
        self.assertIsInstance(info['duration'], float)
        self.assertIsInstance(info['bitrate'], int)

    def test_get_audio_info_invalid_file(self):
        """
        Проверяет обработку некорректного аудио файла.
        """
        file_path = "./tests/test_data/invalid_audio.mp3"
        info = self.test_object.get_info(file_path)
        self.assertEqual(info, {})
