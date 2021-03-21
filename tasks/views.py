from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def task(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, "tasks/reminders.html", context)


def createtask(request):
    return render(request, "tasks/create.html")
