from django.contrib import admin

# Register your models here.
from .models import Task, ToDoList

admin.site.register(Task)
admin.site.register(ToDoList)