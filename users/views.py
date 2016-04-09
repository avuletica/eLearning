from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


@login_required(login_url='/accounts/login')
def course(request):
    if request.user.is_authenticated():
        return render(request, "user.html")


def profile(request):
    if request.user.is_authenticated():
        return render(request, "user_profile.html")
