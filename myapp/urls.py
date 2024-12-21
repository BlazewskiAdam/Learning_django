from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page path
    path("main/", views.main, name="main"),  # Main page path
]