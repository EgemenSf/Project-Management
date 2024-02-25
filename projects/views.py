from django.shortcuts import render, redirect
from projects.models import Project, Request
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm, RequestForm
from datetime import date


@login_required
def projects_list(request):
    projects = Project.objects.filter(owner=request.user)
    today = date.today()
    context = {"projects": projects, "today": today}

    return render(request, "projects/projects_list.html", context)


@login_required
def project_details(request, id):
    project = Project.objects.get(id=id)
    context = {"project": project}

    return render(request, "projects/project_details.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        create_project_form = ProjectForm(request.POST)
        if create_project_form.is_valid():
            project = create_project_form.save()
            project.save()
        return redirect("list_projects")
    else:
        create_project_form = ProjectForm()

    context = {"create_project_form": create_project_form}

    return render(request, "projects/create_project.html", context)


@login_required
def request_task(request):
    if request.method == "POST":
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            request = request_form.save()
            request.save()
        return redirect("show_my_tasks")
    else:
        request_form = RequestForm()

    context = {
        "request_form": request_form
    }

    return render(request, "projects/request.html", context)


def requests_list(request):
    requests = Request.objects.all()
    context = {
        "requests_object": requests
    }
    return render(request, "projects/requests_list.html", context)


@login_required
def delete_request(request, id):
    deleting = Request.objects.get(id=id)
    if request.method == "POST":
        deleting.delete()
        return redirect("requests_list")

    return render(request, "projects/delete_request.html")


@login_required
def Start_Page(request):
    today = date.today().strftime("%B %l, %Y")
    context = {"today": today}

    return render(request, "projects/today.html", context)
