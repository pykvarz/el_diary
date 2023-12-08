from django.contrib import admin

from .models import CustomUser, EmployeeProfile

admin.site.register(CustomUser)
admin.site.register(EmployeeProfile)

