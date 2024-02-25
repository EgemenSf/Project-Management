from django.contrib import admin
from tasks.models import Task,Note


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "due_date", "assignee", "project", "id"]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["id", "note", "task"]
