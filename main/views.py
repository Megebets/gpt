from django.shortcuts import render
from content.models import News
from .models import About

def home(request):
    news_list = News.objects.all()  # Получаем все новости
    return render(request, 'main/main.html', {'news': news_list})

def about(request):
    about = About.objects.all()
    return render(request, 'main/about.html', {'about': about})

