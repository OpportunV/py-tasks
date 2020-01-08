from django.db import models
from django.contrib.auth.models import User

from tasks.models import Task


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, blank=True, related_name='profiles')

    def __str__(self):
        return f'{self.user.username} Profile'
