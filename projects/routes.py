from django.shortcuts import render
from datetime import date


@login_required
def Start_Page(request):
    today = date.today().strftime("%B %d, %Y")
    context = {"today": today}

    return render(request, context)
