from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
app_label = 'profiles'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name='ФИО', default='Не указано')
    age = models.IntegerField(default=30, verbose_name='Возраст')  # Пример: значение по умолчанию
    has_parents = models.BooleanField(default=True, verbose_name='Имеется ли родители')
    birthdate = models.DateField(default=timezone.now, verbose_name='Дата рождения')  # Пример: дата по умолчанию
    birthplace = models.CharField(max_length=100, verbose_name='Место рождения', default='Не указано')  # Пример: текст по умолчанию
    has_children = models.BooleanField(default=False, verbose_name='Имеются ли дети')
    number_of_daughters = models.IntegerField(default=0, verbose_name='Девочек')
    number_of_sons = models.IntegerField(default=0, verbose_name='Мальчиков')
    education = models.CharField(max_length=100, verbose_name='Образование (специальность)', default='Не указано')
    residence = models.CharField(max_length=100, verbose_name='Место жительства', default='Не указано')
    contact_phone = models.CharField(max_length=15, verbose_name='Контактный телефон', default='Не указано')
    trusted_person_phone = models.CharField(max_length=15, verbose_name='Контактный телефон доверенного лица', default='Не указано')
    has_housing = models.BooleanField(default=False, verbose_name='Жильем обеспечен(а)')
    was_married = models.BooleanField(default=False, verbose_name='Состояли в браке')
    height = models.IntegerField(default=170, verbose_name='Рост')
    has_criminal_record = models.BooleanField(default=False, verbose_name='Имеется ли судимость')
    has_bad_habits = models.BooleanField(default=False, verbose_name='Есть ли вредные привычки (курите, пьете?)')
    performs_namaz = models.BooleanField(default=False, verbose_name='Совершаете ли вы намаз')
    clothing_preference = models.CharField(max_length=100, verbose_name='Ваши предпочтения в одежде', default='Не указано')
    spouse_nationality_importance = models.BooleanField(default=False, verbose_name='Имеет ли значение национальность будущего(ей) супруга(и)')
    spouse_age_preference = models.IntegerField(default=30, verbose_name='Возраст будущего(ей) супруга(и)')
    ok_with_divorced_spouse = models.BooleanField(default=False, verbose_name='Возможен ли брак с разведенным (ой)')
    willing_to_relocate = models.BooleanField(default=False, verbose_name='Готовы ли на переезд')
    agree_to_be_second_wife = models.BooleanField(default=False, verbose_name='Согласны ли выйти замуж второй женой')
    plan_to_have_children = models.BooleanField(default=True, verbose_name='Планируете ли вы иметь детей')
    health_status = models.TextField(verbose_name='Состояние вашего здоровья', default='Не указано')
    additional_info = models.TextField(blank=True, null=True, verbose_name='О себе хочу дополнительно сообщить')
    spouse_requirements = models.TextField(verbose_name='Требования к будущему (ей) супругу (е)', default='Не указано')
    madhab = models.CharField(max_length=100, verbose_name='Какой правовой шкалы (мазҳаба) вы придерживаетесь?', default='Не указано')
    profile_completion_date = models.DateField(default=timezone.now, verbose_name='Дата заполнения анкеты')
    consent_to_data_processing = models.BooleanField(default=False, verbose_name='Я даю согласие на обработку данных')