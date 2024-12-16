from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView, StepwiseProfileFormView
from . import views

urlpatterns = [
    path('profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('profile/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('stepwise/', StepwiseProfileFormView.as_view(), name='stepwise_form'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('register/', views.register, name='register'),
]
