from django.contrib import admin
from projects.models import Project, Request

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
    ]

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "request",
        "id"
    ]
