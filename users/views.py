from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)
