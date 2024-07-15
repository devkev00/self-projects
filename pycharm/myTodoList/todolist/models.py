from django.db import models
from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    # 할 일 했는지 여부

    def __str__(self):
        return self.title