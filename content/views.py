from django.shortcuts import render
from .models import News, Info



def news_list(request):
    news_list = News.objects.all()
    return render(request, 'main/main.html', {'news_list': news_list})






def info(request):
    info= Info.objects.all()
    return render(request, 'content/info.html', {'info': info})

