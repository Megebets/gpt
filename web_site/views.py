from django.shortcuts import render
from content.models import News
from .models import About

def home(request):
    news_list = News.objects.all()
    return render(request, 'main/main.html', {'news': news_list})


def about(request):
    about = About.objects.all()
    return render(request, 'main/about.html')

    # return render(request, 'web_site/about.html', {'about': about})

