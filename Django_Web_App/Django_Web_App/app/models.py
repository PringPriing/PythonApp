"""
Definition of models.
"""
from django.db import models

class Task(models.Model):
    UserID = models.IntegerField()
    TaskName = models.CharField(max_length=250)
    DateCreated = models.DateField()

    def __unicode__(self):
        """ Returns a string representation of a task. """
        return self.TaskName

class ToDo(models.Model):
    task = models.ForeignKey(Task)
    ToDoName = models.CharField(max_length=150)
    isDone = models.BooleanField()

    def __unicode__(self):
        """ Return string representation of Todo """
        return self.ToDoName



