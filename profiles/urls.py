from django.urls import path
from .views import UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView

urlpatterns = [
    path('profile/create/', UserProfileCreateView.as_view(), name='profile_create'),
    path('profile/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('profile/edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
]
