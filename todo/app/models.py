from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class Task(models.Model):
    todo_list = models.ForeignKey(
        "app.ToDoList", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)

    is_completed = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Task \"{self.title}\""

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now() + timedelta(days=3)
        return super().save(*args, **kwargs)

    def show_due_date(self):
        return self.due_date.strftime("%d %b, %H:%M")


class ToDoList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s To-Do List"