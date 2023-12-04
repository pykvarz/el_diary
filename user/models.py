from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Role(models.TextChoices):
    ADMIN = "ADMIN", "Администратор"
    TEACHER = "TEACHER", "Учитель"
    STUDENT = "STUDENT", "Ученик"


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, default=None, null=True)
    role = models.CharField(max_length=255, choices=Role.choices, default=None)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
    )


class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="teacher_profile",)
    bio = models.DateField(blank=True, null=True)
    pob = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ("ml", "male"),
        ("fm", "female"),
    )
    NATION_CHOICES = (
        ("kazakh", "Казах/Казашка"),
        ("russian", "Русский/Русская")
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default="ml")
    nation = models.CharField(max_length=100, choices=NATION_CHOICES, default="kazakh", verbose_name="Национальность")
    citizenship = models.CharField(max_length=100)
    iin = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = "Профиль сотрудника"

