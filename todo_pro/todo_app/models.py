from django.db import models

# Create your models here.


class TaskModel(models.Model):
    task = models.CharField(max_length=300)
    priority = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.task