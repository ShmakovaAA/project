from django.contrib import admin
from .models import FileRecord

@admin.register(FileRecord)
class FileRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size_bytes', 'modification_date')
    search_fields = ('name', 'path', 'extension')
