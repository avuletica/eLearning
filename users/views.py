from django.shortcuts import render


# Create your views here.
def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    return render(request, "user.html")