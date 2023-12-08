from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from user.helpers.get_next_id import get_next_id


class UserCreationService:
    @staticmethod
    def create_user(username_prefix, role):
        user = get_user_model().objects.create_user(username=f"{username_prefix}{get_next_id(role=role)}",
                                                    password=User.objects.make_random_password())
        user.role = role
        return user
