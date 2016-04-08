from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    return render(request, "user.html")