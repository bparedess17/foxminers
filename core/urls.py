from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("equipo/", views.equipo, name="equipo"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
