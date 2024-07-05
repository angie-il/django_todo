from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')