from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import EmployeeCreateView, CustomUserLoginView, MainMenuView

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='user_login'),
    path('create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('menu/', MainMenuView.as_view(), name='main_menu'),

]