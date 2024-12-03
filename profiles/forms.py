from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']  # Исключаем поле пользователя, так как связываем его в представлении
