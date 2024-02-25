from django.forms import ModelForm
from projects.models import Project,Request
from tasks.models import Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "owner"]


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ["owner","request"]
