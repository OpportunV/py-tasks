from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from tasks.models import Task


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, blank=True, related_name='profiles')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'id_': self.user.id})
