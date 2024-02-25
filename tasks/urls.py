from django.urls import path
from tasks.views import create_task, tasks_list, create_note, show_notes, delete_note

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", tasks_list, name="show_my_tasks"),
    path("addnote/", create_note, name="create_note"),
    path("<int:id>/notes/", show_notes, name="show_notes"),
    path("<int:id>/delete/", delete_note, name="delete_note"),
]
