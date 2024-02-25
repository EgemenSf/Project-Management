from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task, Note
from tasks.forms import TaskForm, NoteForm


@login_required
def create_task(request):
    if request.method == "POST":
        create_task_form = TaskForm(request.POST)
        if create_task_form.is_valid():
            task = create_task_form.save()
            task.save()
        return redirect("list_projects")
    else:
        create_task_form = TaskForm()

    context = {"create_task_form": create_task_form}
    return render(request, "tasks/create_task.html", context)


@login_required
def tasks_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"tasks": tasks}

    return render(request, "tasks/tasks_list.html", context)


@login_required
def create_note(request):
   if request.method == "POST":
       create_note_form = NoteForm(request.POST)
       if create_note_form.is_valid():
           note = create_note_form.save(False)
           note.save()
       return redirect("show_notes", id=note.task.id)
   else:
       create_note_form = NoteForm()

   context = {"create_note_form": create_note_form}

   return render(request, "tasks/create_note.html", context)



@login_required
def show_notes(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task": task,
    }

    return render(request, "tasks/notes.html", context)


@login_required
def delete_note(request, id):
    deleting = Note.objects.get(id=id)
    if request.method == "POST":
        deleting.delete()
        return redirect("show_notes", id=deleting.task.id)

    return render(request, "tasks/delete.html")


