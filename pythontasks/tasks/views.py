from django.shortcuts import render


tmp_tasks = [
    {
        'author': 'first',
        'title': 'title1',
        'content': 'content1',
        'date': 'Jan 2, 2020'
    },
    {
        'author': 'first',
        'title': 'title2',
        'content': 'content2',
        'date': 'Jan 3, 2020'
    },
]


def index(request):
    content = {
        'tasks': tmp_tasks
    }
    return render(request, 'tasks/index.html', content)


def about(request):
    content = {
        'title': 'About'
    }
    return render(request, 'tasks/about.html', content)
