from django.urls import path

from blog.views.blog import create_blog, home


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_blog, name="create"),
]