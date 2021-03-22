from django.urls import path
from . import views

urlpatterns = [
    path("", views.task, name="home"),
    path("update/<str:pk>", views.updatetask, name="updateRem"),
    path("delete/<str:pk>", views.deletetask, name="deleteRem"),
]
