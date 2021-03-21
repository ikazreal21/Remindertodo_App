from django.urls import path
from . import views

urlpatterns = [
    path("", views.task, name="home"),
    path("create/", views.createtask, name="CreateRem"),
]
