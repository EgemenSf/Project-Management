from django.urls import path
from projects.views import projects_list, project_details, create_project, request_task, requests_list, delete_request, Start_Page

urlpatterns = [
    path("", projects_list, name="list_projects"),
    path("<int:id>/", project_details, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("request/", request_task, name="request_task"),
    path("requestslist/", requests_list, name="requests_list"),
    path("<int:id>/delete/", delete_request, name="delete_request"),
    path("today/", Start_Page, name="today")
]
