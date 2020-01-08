from django.contrib import admin

from .models import Task, Tag, Solution

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Solution)
