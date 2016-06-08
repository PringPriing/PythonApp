from django.contrib import admin
from app.models import Task,ToDo

class ToDoInline(admin.TabularInline):
    model = ToDo
    extra = 3


class TaskAdmin(admin.ModelAdmin):
    inlines = [ToDoInline]
    search_fields = ['text']


admin.site.register(Task,TaskAdmin)