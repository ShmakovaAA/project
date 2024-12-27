# tests/test_urls.py
from django.test import TestCase
from django.urls import reverse

class UrlsTestCase(TestCase):
    """
    Тестовый класс для проверки URL маршрутов.
    """

    def test_home_url(self):
        """
        Проверяет доступность главной страницы и используемый шаблон.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_stats_url(self):
        """
        Проверяет доступность страницы статистики.
        """
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')

    def test_top_files_url(self):
        """
        Проверяет доступность страницы топ-10 файлов.
        """
        response = self.client.get(reverse('top_files'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'top_files.html')

    def test_top_images_url(self):
        """
        Проверяет доступность страницы топ-10 изображений.
        """
        response = self.client.get(reverse('top_images'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'top_images.html')

    def test_top_docs_url(self):
        """
        Проверяет доступность страницы топ-10 документов.
        """
        response = self.client.get(reverse('top_docs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'top_docs.html')
