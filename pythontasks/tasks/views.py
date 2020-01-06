from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    content = {
        'tasks': tasks
    }
    return render(request, 'tasks/index.html', content)


def about(request):
    content = {
        'title': 'About'
    }
    return render(request, 'tasks/about.html', content)
