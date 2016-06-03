"""
Definition of views.
"""
from app.models import Task,ToDo
from django.shortcuts import render
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
            context['year'] = datetime.now().year
            return context

def post_new_task(request):
    """ Handles adding of task """
    task = Task()
    task.DateCreated = timezone.now()
    task.UserID = request.user.id
    task.TaskName = ''
    task.save()
    return render(request,'app/webApp.html',
            {
                'title': 'inbox'
            }
        )


