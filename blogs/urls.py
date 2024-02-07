# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail,post_remove
urlpatterns = [
    path("<int:pk>", PostDetail.as_view(), name="post_detail"),

    path("blog", PostList.as_view(), name="post_list"),
    path("blog/<int:pk>",post_remove, name="post_remove")

    # path("view", view_all , name="view"),
]
