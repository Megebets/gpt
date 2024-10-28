from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name= 'news'),  # Путь для списка новостей
    path('info/' , views.info, name= 'info'),
]
