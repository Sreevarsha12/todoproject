from django.db import models

class Task(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDesc=models.TextField()
    taskDate=models.DateField(null=True)

    def __str__(self):
        return self.taskTitle

