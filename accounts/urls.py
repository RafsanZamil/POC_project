

from django.urls import path
from .views import register_user
from .views import  user_logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register', register_user, name='register'),
    # path('login', user_login, name='login'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout' ,user_logout, name='logout')

]

