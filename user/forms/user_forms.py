from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "surname", "role"]
        labels = {
            "username": "Логин",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "surname": "Отчество",
            "role": "Роль",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})
        self.fields['password2'].widget = forms.HiddenInput(attrs={'readonly': 'readonly'})

