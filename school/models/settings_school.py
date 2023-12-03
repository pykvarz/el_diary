from django.db import models


from user.models import CustomUser


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Classes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    school_year = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT)




