from django.db import models
from django.utils import timezone


class ToDoModel(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    created = models.DateTimeField(default= timezone.now())

    def __str__(self):
        return self.title

