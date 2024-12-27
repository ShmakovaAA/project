# tests/test_management_commands.py
from django.test import TestCase
from django.core.management import call_command, CommandError
from fileindexer.models import FileRecord
import os

class IndexFilesCommandTestCase(TestCase):
    """
    Тестовый класс для проверки команды индексирования файлов.
    """

    def setUp(self):
        """
        Создает временную директорию и тестовые файлы для индексирования.
        """
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_data')
        os.makedirs(self.test_dir, exist_ok=True)
        # Создаем тестовые файлы разных типов
        with open(os.path.join(self.test_dir, 'test.txt'), 'w') as f:
            f.write("This is a test file.")
        with open(os.path.join(self.test_dir, 'test.xlsx'), 'wb') as f:
            f.write(b'\x50\x4B\x03\x04')  # Минимальные байты для файла XLSX

    def tearDown(self):
        """
        Удаляет созданные тестовые файлы и директорию.
        """
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            os.rmdir(root)

    def test_index_files_command_invalid_path(self):
        """
        Проверяет, что команда выбрасывает CommandError при передаче некорректного пути.
        """
        invalid_path = os.path.join(self.test_dir, 'non_existent')
        with self.assertRaises(CommandError):
            call_command('index_files', invalid_path)

    def test_index_files_command_empty_directory(self):
        """
        Проверяет, что при индексировании пустой директории не создается записей FileRecord.
        """
        empty_dir = os.path.join(self.test_dir, 'empty')
        os.makedirs(empty_dir, exist_ok=True)
        call_command('index_files', empty_dir)
        self.assertEqual(FileRecord.objects.count(), 0)
        os.rmdir(empty_dir)

    def test_index_files_command_with_files(self):
        """
        Проверяет, что при индексировании директории с файлами создаются соответствующие записи FileRecord.
        """
        call_command('index_files', self.test_dir)
        self.assertEqual(FileRecord.objects.count(), 2)
        # Проверяем, что файлы txt и xlsx были проиндексированы
        txt_record = FileRecord.objects.get(name='test.txt')
        xlsx_record = FileRecord.objects.get(name='test.xlsx')
        self.assertEqual(txt_record.extension, '.txt')
        self.assertEqual(xlsx_record.extension, '.xlsx')
