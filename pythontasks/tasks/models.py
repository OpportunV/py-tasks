from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('tasks-task_details', kwargs={'id_': self.id})

    def __str__(self):
        return self.title
