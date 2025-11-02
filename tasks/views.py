from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Task
from .forms import TaskForm
from django.urls import reverse
from django.utils import timezone

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 50

    def get_queryset(self):
        return Task.objects.order_by('completed', 'deadline', '-created_at')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pending'] = [t for t in self.object_list if not t.completed]
        ctx['completed_tasks'] = [t for t in self.object_list if t.completed]
        ctx['now'] = timezone.now()
        return ctx

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'

# FBV for create/edit/delete and toggle

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
    return render(request, 'tasks/form.html', {'form': form, 'title': 'Add Task'})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/form.html', {'form': form, 'title': 'Edit Task'})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('tasks:index')
