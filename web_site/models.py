from django.db import models
from content.models import News
from django.shortcuts import render

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')


def home(request):
    news = News.objects.all()
    print(news)
    return render(request, 'main/main.html', {'news': news})
# Create your models here.
