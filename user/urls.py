from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import CustomUserCreateView

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name='user_create'),
    path('logout/', LogoutView.as_view(), name='logout'),


]