from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')
    
    def get_absolute_url(self):
        return reverse('tasks-task_details', kwargs={'id_': self.id})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('tasks-tag_details', kwargs={'id_': self.id})

    def __str__(self):
        return self.title
    

class Solution(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.SmallIntegerField(default=0,
                                     validators=[MinValueValidator(0),
                                                 MaxValueValidator(5)])

    def __str__(self):
        return f'Solution for {self.task.title} by {self.author.username}'
