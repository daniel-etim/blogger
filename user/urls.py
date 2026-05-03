from django.urls import path

from .views import user


urlpatterns = [
    path("", user.home, name="home"),
    path("greeting/", user.greeting, name="greeting"),
    path("register/", user.register, name="register"),
    path("login/", user.login, name="login"),
    path("dashboard/", user.dashboard, name="dashboard"),
]