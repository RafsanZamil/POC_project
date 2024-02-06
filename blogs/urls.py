
from django.urls import path

from blogs.views import post_list

# from .views import register_user
# from .views import user_login

urlpatterns = [
    # path('register/', register_user, name='register'),
    path('blog/', post_list),

]