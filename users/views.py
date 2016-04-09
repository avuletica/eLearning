from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def login(request):
    if request.user.is_authenticated():
        return render(request, "home.html")


@login_required(login_url='/accounts/login')
def profile(request):
    if request.user.is_authenticated():
        return render(request, "user.html")