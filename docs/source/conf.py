# conf.py

import os
import sys
import django

# Добавляем путь к корневой директории проекта
sys.path.insert(0, os.path.abspath('../../'))

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Замените на ваш путь к settings.py

# Инициализируем Django
django.setup()

# -- Project information -----------------------------------------------------

project = 'FileIndexer'
author = 'Ваше Имя'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
