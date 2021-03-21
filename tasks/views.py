from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def task(request):
    return render(request, "tasks/task.html")


def createtask(request):
    return render(request, "tasks/create.html")
