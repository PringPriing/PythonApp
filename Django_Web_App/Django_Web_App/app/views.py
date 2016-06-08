"""
Definition of views.
"""
from app.models import Task,ToDo
from django.shortcuts import render,render_to_response
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404,render
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import ListView, DetailView
from os import path
from app.forms import TaskForm
from django.http import Http404, HttpResponse
from django.core import serializers

import json




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

@login_required
def webApp(request):
    """ Renders Single Page App. """
    assert isinstance(request,HttpRequest)
    return render(
        request,
            'app/webApp.html',
            {
                'title': 'inbox'
            }
        )

def pro(request):
    """ renders pro page """
    assert isinstance(request,HttpRequest)
    return render(
        request,
            'app/pro.html',
            {
                'title' : 'Pro'
            }
        )

def business(request):
    """ renders business page """
    assert isinstance(request,HttpRequest)
    return render(
        request,
            'app/business.html',
            {
                'title' : 'business'
            }
        )

class TaskListView(ListView):
        model = Task
        def get_context_data(self, **kwargs):
            context = super(TaskListView,self).get_context_data(**kwargs)
            context['ToDos'] = ToDo.objects.all().filter(isDone=False)
            context['ToDos_Done'] = ToDo.objects.all().filter(isDone=True)
            context['Tasks'] = Task.objects.all().filter(UserID=self.request.user.id)
            context['year'] = datetime.now().year
            return context

def markasDone(request):
    """ Handles marking todo as done """
    
    try:
        todo = ToDo.objects.get(id = request.POST.get('todoID'))
    except (KeyError, ToDo.DoesNotExist):
        return render(request, 'app/webApp.html', {
            'title': 'Task',
            'year': datetime.now().year,
            'error_message': "Please make a selection.",
    })
    else:
        todo.isDone = True
        todo.save()
        return render(
        request,
            'app/webApp.html',
            {
                'title': 'inbox'
            }
        )


def  AddTask(request):
    """ Handles adding of task """
    task = Task()
    task.DateCreated = timezone.now()
    task.UserID = request.user.id
    task.TaskName = request.POST.get('taskname')
    task.save()
    return render(
        request,
            'app/webApp.html',
            {
                'title': 'inbox'
            }
        )

def AddToDo(request):
    """ Handles adding of ToDo's """ 
    todo = ToDo()
    todo.ToDoName = request.POST.get('todoName')
    todo.task = Task.objects.get(id=request.POST.get('taskID'))
    todo.isDone = False
    todo.save()

    return render(
        request,
            'app/webApp.html',
            {
                'title': 'inbox'
            }
        )

def GetTaskbyID(request):
    """ Handles retrieving of todo by task id  """
    task_id = request.POST.get('id')
    context['ToDos'] = ToDo.objects.all().filter(task_id=id)

def getTodoByTaskID(request):
    context = RequestContext(request)
    todo_list = []
    if request.method == 'GET':
        todo_list = ToDo.objects.all().filter(task_id=request.GET['taskID'])
        data = serializers.serialize('json',todo_list)

    return HttpResponse(data, content_type='application/json')