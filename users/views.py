from django.shortcuts import render, redirect
from source import settings
from courses.views import course
from courses.forms import AddCourseForm


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    title = 'Profile'
    form = AddCourseForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.course_link = '/courses/' + instance.course_name
        instance.save()
        return course(request, course_name=instance.course_name)

    if request.user.is_authenticated():
        return render(request, "user_profile.html", context)
    else:
        return redirect(settings.LOGIN_URL)