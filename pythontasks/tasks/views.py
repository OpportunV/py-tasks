from django.shortcuts import render

from .models import Task, Tag


def index(request):
    tasks = Task.objects.all()
    content = {
        'title': 'Tasks',
        'tasks': tasks,
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
        'title': task.title,
        'task': task,
    }
    return render(request, 'tasks/task_details.html', content)


def tags(request):
    tags_list = Tag.objects.all()
    content = {
        'title': 'Tags',
        'tags_list': [1, 2, 3],
    }
    return render(request, 'tasks/tags_list.html', content)


# def tags_details(request, id_):
#     tag = Tag.objects.get(id=id_)
#     content = {
#         'title': tag.title,
#         'tag': tag,
#     }
#     return render(request, 'tasks/tags_details.html', content)


