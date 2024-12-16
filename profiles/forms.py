# profiles/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'health_status': forms.Textarea(attrs={'rows': 3}),
            'additional_info': forms.Textarea(attrs={'rows': 3}),
            'spouse_requirements': forms.Textarea(attrs={'rows': 3}),
        }
