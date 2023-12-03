from django.db import models

from school.models.settings_school import Subject, Classes
from user.models import CustomUser


class SubjectsTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class LessonPlan(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    theme = models.CharField(max_length=255)
    quarter = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=False, blank=True, null=True)


class TeacherLessonPlan(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE)


class Teaching(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    class_id = models.ForeignKey(Classes, on_delete=models.PROTECT)


class Grades(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    class_id = models.ForeignKey(Classes, on_delete=models.PROTECT)
    grade = models.IntegerField(default=None)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.PROTECT)
