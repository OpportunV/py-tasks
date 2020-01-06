from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    content = {
        'tasks': tasks,
        'title': 'Tasks'
    }
    return render(request, 'tasks/index.html', content)


def about(request):
    content = {
        'title': 'About'
    }
    return render(request, 'tasks/about.html', content)


def task_details(request, id_):
    task = Task.objects.get(id=id_)
    content = {
        'task': task,
        'title': task.title
    }
    return render(request, 'tasks/task_details.html', content)
