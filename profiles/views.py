from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .models import UserProfile
from .forms import UserProfileForm
from django.views.generic.edit import FormView

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/profile_create.html'
    success_url = reverse_lazy('profile_detail')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Связываем профиль с текущим пользователем
        return super().form_valid(form)

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('profile_detail')

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)
    
class StepwiseProfileFormView(FormView):
    template_name = 'profiles/stepwise_form.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profiles:profile_success')
    def form_valid(self, form):
        form.save
        return super().form_valid(form)
    
