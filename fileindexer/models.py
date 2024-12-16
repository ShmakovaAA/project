from django.db import models

class FileRecord(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя файла")
    path = models.CharField(max_length=1024, verbose_name="Путь")
    extension = models.CharField(max_length=50, verbose_name="Расширение", blank=True, null=True)
    modification_date = models.DateTimeField(verbose_name="Дата изменения", null=True, blank=True)
    size_bytes = models.BigIntegerField(verbose_name="Размер (байт)", default=0)

    page_count = models.IntegerField(verbose_name="Количество страниц/параграфов", null=True, blank=True)
    width = models.IntegerField(verbose_name="Ширина", null=True, blank=True)
    height = models.IntegerField(verbose_name="Высота", null=True, blank=True)
    duration = models.FloatField(verbose_name="Длительность (сек)", null=True, blank=True)
    bitrate = models.IntegerField(verbose_name="Битрейт", null=True, blank=True)
    dpi = models.CharField(max_length=50, verbose_name="DPI", null=True, blank=True)
    metadata = models.TextField(verbose_name="Метаданные", null=True, blank=True)
    page_format = models.CharField(max_length=50, verbose_name="Формат страниц", null=True, blank=True)

    def __str__(self):
        return self.name
