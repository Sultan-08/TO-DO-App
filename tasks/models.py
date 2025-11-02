from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['completed', 'deadline', '-created_at']

    def __str__(self):
        return self.title
