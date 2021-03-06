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
    if 'Admin' in [group.name for group in request.user.groups.all()]:
        solutions = task.solution_set.all()
    else:
        solutions = task.solution_set.filter(author=request.user).all()
    content = {
        'title': task.title,
        'task': task,
        'solutions': solutions,
    }
    return render(request, 'tasks/task_details.html', content)


def tags_list(request):
    tags = Tag.objects.all()
    content = {
        'title': 'Tags',
        'tags': tags,
    }
    return render(request, 'tasks/tags_list.html', content)


def tags_details(request, id_):
    tag = Tag.objects.get(id=id_)
    content = {
        'title': tag.title,
        'tag': tag,
    }
    return render(request, 'tasks/tag_details.html', content)


