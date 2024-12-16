import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from fileindexer.models import FileRecord
from fileindexer.researchers.general import GeneralResearcher
from fileindexer.researchers.pdf import PDFResearcher
from fileindexer.researchers.image import ImageResearcher
from fileindexer.researchers.docxresearcher import DocxResearcher
from fileindexer.researchers.excel import ExcelResearcher
from fileindexer.researchers.audio import AudioResearcher
from fileindexer.researchers.video import VideoResearcher
from datetime import datetime, timezone
import logging

logger = logging.getLogger('fileindexer')

class Command(BaseCommand):
    help = 'Индексирует файлы в указанной директории и сохраняет в базу данных.'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Путь к папке для индексации')

    def handle(self, *args, **options):
        path = options['path']
        if not os.path.isdir(path):
            self.stderr.write(self.style.ERROR('Указанный путь не является директорией'))
            return

        researchers = [
            GeneralResearcher(),
            PDFResearcher(),
            ImageResearcher(),
            DocxResearcher(),
            ExcelResearcher(),
            AudioResearcher(),
            VideoResearcher()
        ]

        self.stdout.write('Очистка старых записей...')
        FileRecord.objects.all().delete()

        self.stdout.write('Начинается индексация...')

        file_count = 0
        for root, dirs, files in os.walk(path):
            for f in files:
                file_path = os.path.join(root, f)
                # Считываем общие данные
                rel_info = {
                    'name': f,
                    'path': root,
                    'extension': os.path.splitext(f)[1].lower() if '.' in f else None,
                    'modification_date': datetime.fromtimestamp(os.path.getmtime(file_path), tz=timezone.utc)
                }
                additional_info = {}
                for r in researchers:
                    if r.supports(file_path):
                        data = r.get_info(file_path)
                        additional_info.update(data)

                rel_info.update(additional_info)
                FileRecord.objects.create(**rel_info)
                file_count += 1

        self.stdout.write(self.style.SUCCESS(f'Индексация завершена. Проиндексировано файлов: {file_count}'))
