from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def task(request):
    tasks = Task.objects.all()
    form = TaskForms()

    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, "tasks/reminders.html", context)


def updatetask(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForms(instance=tasks)

    if request.method == 'POST':
        form = TaskForms(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, "tasks/update.html", context)


def deletetask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
