# tests/test_fileindexer_config.py
from django.test import TestCase
from django.apps import apps
from fileindexer.apps import FileindexerConfig

class FileindexerConfigTest(TestCase):
    """
    Тестовый класс для проверки конфигурации приложения Fileindexer.
    """

    def test_app_config(self):
        """
        Проверяет, что класс конфигурации приложения имеет правильные атрибуты.
        """
        self.assertEqual(FileindexerConfig.name, 'fileindexer')
        self.assertEqual(FileindexerConfig.verbose_name, 'Индексатор файлов')
        self.assertEqual(FileindexerConfig.default_auto_field, 'django.db.models.BigAutoField')

    def test_fileindexer_app_is_installed(self):
        """
        Проверяет, что приложение fileindexer установлено в INSTALLED_APPS.
        """
        fileindexer = apps.get_app_config('fileindexer')
        self.assertEqual(fileindexer.name, 'fileindexer')
