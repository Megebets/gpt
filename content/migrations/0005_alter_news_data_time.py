# Generated by Django 5.1.1 on 2024-10-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_info_image1_info_image2_info_image3_info_image4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='data_time',
            field=models.DateField(default='2024-10-28'),
        ),
    ]
