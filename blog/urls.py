from django.urls import path

from blog.views.blog import create_post, home, post_detail, post_list, update_post


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_post, name="create"),
    path("list/", post_list, name="list"),
    path("<int:pk>/update/", update_post, name="update_post"),
    path("<int:pk>/", post_detail, name="detail"),
]