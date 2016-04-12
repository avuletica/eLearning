from django.shortcuts import render, redirect
from .forms import AddCourseForm
from .models import Course
from source import settings


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
