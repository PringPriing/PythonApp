"""
Definition of models.
"""

from django.db import models

class Task(models.Model):
    UserID = models.IntegerField()
    TaskName = models.CharField(max_length=250)
    DateCreated = models.DateField()

class ToDo(models.Model):
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    ToDoName = models.CharField(max_length=150)
    isDone = models.BooleanField()

