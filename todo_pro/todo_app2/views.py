from django.shortcuts import render
from django.urls import reverse_lazy
from todo_app.models import TaskModel
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.


class TaskListView(ListView):
    model = TaskModel
    template_name = 'index.html'
    context_object_name = 'task'


class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
