from django.db import models
from django import forms
from datetime import date

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='НОвости на сегодня')
    image = models.ImageField(upload_to='news_images/')
    data_time = models.DateField(default=date.today().strftime('%Y-%m-%d'))




class Info(models.Model):
    description = models.TextField(default='ОПИСАНИЕ ОРГАНИЗАЦИИ')
    image1 = models.ImageField(upload_to='info_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='info_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='info_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='info_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='info_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='info_images/', blank=True, null=True)


