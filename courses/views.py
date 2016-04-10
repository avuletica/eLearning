from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
        instance.course_link = '/course' + instance.course_name
        instance.save()
        return HttpResponseRedirect('')

    if request.user.is_authenticated():
        return render(request, "user_profile.html", context)
    else:
        return redirect(settings.LOGIN_URL)


def course(request):
    title = 'Course'
    queryset = Course.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }

    if request.user.is_authenticated():
        return render(request, "user.html", context)
    else:
        return redirect(settings.LOGIN_URL)
