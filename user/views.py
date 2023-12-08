from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from user.forms.user_forms import CustomUserCreationForm
from user.helpers.get_next_id import get_next_id
from user.models import CustomUser
from user.services.user_create import UserCreationService


# Create your views here.

class CustomUserLoginView(LoginView):
    template_name = 'login_user.html'
    redirect_authenticated_user = True


class EmployeeCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('main_menu')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.username = f"130t{get_next_id(role='TEACHER')}"
        instance.cleaned_data['password1'] = instance.set_password() make_password(User.objects.make_random_password)
        instance.cleaned_data['password2'] = instance.cleaned_data['password1']
        instance.save()
        return super().form_valid(form)
        # user = UserCreationService.create_user(username_prefix="s130t", role="TEACHER")



class MainMenuView(TemplateView):
    template_name = 'main_menu.html'


