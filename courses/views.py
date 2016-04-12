from django.shortcuts import render, redirect
from .models import Course
from source import settings


def courses(request):
    title = 'Courses'
    queryset = Course.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }

    if request.user.is_authenticated():
        return render(request, "user.html", context)
    else:
        return redirect(settings.LOGIN_URL)


def course(request, course_name):
    title = course_name

    context = {
        "title": title
    }

    if request.user.is_authenticated():
        return render(request, "courses/course.html", context)
    else:
        return redirect(settings.LOGIN_URL)
