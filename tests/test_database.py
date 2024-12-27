# tests/test_database.py
from django.test import TestCase
from fileindexer.models import FileRecord
from django.core.management import call_command

class DatabaseTestCase(TestCase):
    """
    Тестовый класс для проверки содержимого базы данных.
    """

    def setUp(self):
        """
        Загружает данные из дампа JSON для тестирования.
        """
        call_command('loaddata', 'dump.json', format='json')

    def test_db_content_empty(self):
        """
        Проверяет, что количество записей FileRecord равно 0.
        """
        self.assertEqual(FileRecord.objects.all().count(), 0)

    def test_db_content_loaded(self):
        """
        Проверяет, что после загрузки данных количество записей соответствует ожидаемому.
        """
        expected_count = 3  # Замените на фактическое количество записей в dump.json
        self.assertEqual(FileRecord.objects.all().count(), expected_count)

    def test_fileinfo_fields(self):
        """
        Проверяет корректность заполнения полей модели FileRecord.
        """
        file_info = FileRecord.objects.first()
        self.assertIsNotNone(file_info)
        self.assertEqual(file_info.name, "example_file.txt")
        self.assertEqual(file_info.size_bytes, 1024)
        self.assertEqual(file_info.extension, ".txt")
