

from django.urls import path
from .views import register_user
from .views import user_login

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login')

]