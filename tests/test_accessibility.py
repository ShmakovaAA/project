# tests/test_accessibility.py
from django.test import TestCase, Client
from fileindexer.models import FileRecord
from django.urls import reverse

class AccessibilityTestCase(TestCase):
    """
    Тестовый класс для проверки доступности страниц.
    """

    def setUp(self):
        """
        Настройка тестовой среды.
        """
        self.client = Client()

    def test_pages(self):
        """
        Проверяет, что количество записей FileRecord равно 0.
        """
        self.assertEqual(FileRecord.objects.all().count(), 0)

    def test_empty_pages(self):
        """
        Проверяет, что при запросе страницы 'sizetop' выводится сообщение "No files found.".
        """
        response = self.client.get(reverse('sizetop', args=(10,)))
        self.assertContains(response, "No files found.")

    def test_all_pages(self):
        """
        Проверяет доступность всех основных страниц проекта.
        """
        pages = ['imgtop', 'sizetop', 'extstats', 'pagetop']
        for page in pages:
            response = self.client.get(reverse(page, args=(10,)))
            self.assertEqual(response.status_code, 200)
        response2 = self.client.get(reverse('home'))
        self.assertEqual(response2.status_code, 200)
