from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Role, EmployeeProfile


@receiver(post_save, sender=CustomUser)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and instance.role != Role.STUDENT:
        EmployeeProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_employee_profile(sender, instance, **kwargs):
    instance.employee_profile.save()


