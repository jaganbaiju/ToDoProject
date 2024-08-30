from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from todo_app.models import TaskModel
from todo_app.forms import TaskForm


# Create your views here.


def index(request):
    task = TaskModel.objects.all()
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']

        task_data = TaskModel(task=task, priority=priority, date=date)
        task_data.save()
        return redirect('/')

    return render(request, 'index.html', {"task": task})


def update(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    forms = TaskForm(request.POST or None, instance=task)

    if forms.is_valid():
        forms.save()
        return redirect('/')

    return render(request, 'update.html', {'forms': forms, 'task': task})


def delete(request, task_id):
    if request.method == 'POST':
        task = TaskModel.objects.get(id=task_id)
        task.delete()

        return redirect('/')

    return render(request, 'delete.html')

