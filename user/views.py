from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from user.forms.user_forms import CustomUserCreationForm
from user.models import CustomUser


# Create your views here.

class CustomUserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'create_user.html'
    success_url = None

