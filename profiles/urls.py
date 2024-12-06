from django.urls import path
from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView, StepwiseProfileFormView
from . import views
from profiles.views import SignupView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from .views import CustomSignupView

urlpatterns = [
    path('profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('stepwise/', StepwiseProfileFormView.as_view(), name='stepwise_form'),
    path('edit/', views.EditUserProfileView.as_view(), name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),


    
]
