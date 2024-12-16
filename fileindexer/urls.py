from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('stats/', views.stats, name='stats'),
    path('top-files/', views.top_files, name='top_files'),
    path('top-images/', views.top_images, name='top_images'),
    path('top-docs/', views.top_docs, name='top_docs'),
]
