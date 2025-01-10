from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, ToDoList
from django.urls import reverse

# Create your views here.
def home_page(request):
    user = request.user
    todo_list = ToDoList.objects.get(user=user) 
    tasks = Task.objects.filter(todo_list=todo_list).order_by("-is_pinned", "id")
    context ={
        "task_list": tasks
        }    
    return render(request, "home.html", context)

def create_new_task(request):
    user = request.user
    todo_list = ToDoList.objects.get(user=user)
    task_title = request.POST.get("task_title")

    Task.objects.create(
        todo_list=todo_list , 
        title=task_title
        )
    return redirect(reverse("app:index"))

def toggle_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect(reverse("app:index"))


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect(reverse("app:index"))

def pinned_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_pinned = not task.is_pinned
    task.save()
    return redirect(reverse("app:index"))

