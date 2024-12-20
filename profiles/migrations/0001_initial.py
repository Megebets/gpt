# Generated by Django 5.1.1 on 2024-12-03 07:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Не указано', max_length=100, verbose_name='ФИО')),
                ('age', models.IntegerField(default=30, verbose_name='Возраст')),
                ('has_parents', models.BooleanField(default=True, verbose_name='Имеется ли родители')),
                ('birthdate', models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения')),
                ('birthplace', models.CharField(default='Не указано', max_length=100, verbose_name='Место рождения')),
                ('has_children', models.BooleanField(default=False, verbose_name='Имеются ли дети')),
                ('number_of_daughters', models.IntegerField(default=0, verbose_name='Девочек')),
                ('number_of_sons', models.IntegerField(default=0, verbose_name='Мальчиков')),
                ('education', models.CharField(default='Не указано', max_length=100, verbose_name='Образование (специальность)')),
                ('residence', models.CharField(default='Не указано', max_length=100, verbose_name='Место жительства')),
                ('contact_phone', models.CharField(default='Не указано', max_length=15, verbose_name='Контактный телефон')),
                ('trusted_person_phone', models.CharField(default='Не указано', max_length=15, verbose_name='Контактный телефон доверенного лица')),
                ('has_housing', models.BooleanField(default=False, verbose_name='Жильем обеспечен(а)')),
                ('was_married', models.BooleanField(default=False, verbose_name='Состояли в браке')),
                ('height', models.IntegerField(default=170, verbose_name='Рост')),
                ('has_criminal_record', models.BooleanField(default=False, verbose_name='Имеется ли судимость')),
                ('has_bad_habits', models.BooleanField(default=False, verbose_name='Есть ли вредные привычки (курите, пьете?)')),
                ('performs_namaz', models.BooleanField(default=False, verbose_name='Совершаете ли вы намаз')),
                ('clothing_preference', models.CharField(default='Не указано', max_length=100, verbose_name='Ваши предпочтения в одежде')),
                ('spouse_nationality_importance', models.BooleanField(default=False, verbose_name='Имеет ли значение национальность будущего(ей) супруга(и)')),
                ('spouse_age_preference', models.IntegerField(default=30, verbose_name='Возраст будущего(ей) супруга(и)')),
                ('ok_with_divorced_spouse', models.BooleanField(default=False, verbose_name='Возможен ли брак с разведенным (ой)')),
                ('willing_to_relocate', models.BooleanField(default=False, verbose_name='Готовы ли на переезд')),
                ('agree_to_be_second_wife', models.BooleanField(default=False, verbose_name='Согласны ли выйти замуж второй женой')),
                ('plan_to_have_children', models.BooleanField(default=True, verbose_name='Планируете ли вы иметь детей')),
                ('health_status', models.TextField(default='Не указано', verbose_name='Состояние вашего здоровья')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='О себе хочу дополнительно сообщить')),
                ('spouse_requirements', models.TextField(default='Не указано', verbose_name='Требования к будущему (ей) супругу (е)')),
                ('madhab', models.CharField(default='Не указано', max_length=100, verbose_name='Какой правовой шкалы (мазҳаба) вы придерживаетесь?')),
                ('profile_completion_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата заполнения анкеты')),
                ('consent_to_data_processing', models.BooleanField(default=False, verbose_name='Я даю согласие на обработку данных')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
