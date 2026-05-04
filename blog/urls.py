from django.urls import path

from blog.views.blog import create_post, delete_post, home, post_detail, post_list, update_post


urlpatterns = [
    path("", home, name="home"),
    path("list/", post_list, name="list"),
    path("<int:pk>/", post_detail, name="detail"),
    path("create/", create_post, name="create"),
    path("<int:pk>/update/", update_post, name="update_post"),
    path("<int:pk>/delete/", delete_post, name="delete_post"),
]