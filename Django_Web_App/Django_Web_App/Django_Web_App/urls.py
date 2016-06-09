"""
Definition of urls for Django_Web_App.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from app.views import TaskListView
from app.models import Task,ToDo
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^webApp',
                TaskListView.as_view(
                template_name = 'app/webApp.html',),
            name='webApp'
        ),
    url(r'^pro',app.views.pro, name='pro'),
    url(r'^business',app.views.business, name='business'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:

     url(r'^admin/', include(admin.site.urls)),
     url(r'^AddTask/', app.views.AddTask, name='add_task'),
     url(r'^AddToDo/', app.views.AddToDo, name='add_todo'),
     url(r'^markasDone/', app.views.markasDone, name='markasDone'),
     url(r'^getTodoByTaskID/$', app.views.getTodoByTaskID, name='getTodoByTaskID'),
     url(r'^CreateUser/', app.views.CreateUser, name='CreateUser'),
    
]
