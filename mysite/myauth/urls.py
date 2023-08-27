from django.urls import path
from .views import my_login, profile, register, my_logout

urlpatterns = [
    path("myauth/", my_login, name="login"),
    path("profile/", profile, name='profile'),
    path('register/', register, name='register'),
    path('logout', my_logout, name='logout')
]