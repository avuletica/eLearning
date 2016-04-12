from django.shortcuts import render, redirect
from source import settings
from courses.views import course
from courses.forms import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    title = 'Profile'
    add_course_form = AddCourseForm(request.POST or None)
    add_user_form = AddUser(request.POST or None)
    delete_user_form = DeleteUser(request.POST or None)
    queryset = User.objects.all()

    context = {
        "title": title,
        "form": add_course_form,
        "form2": add_user_form,
        "form3": delete_user_form,
        "queryset": queryset,
    }

    if add_user_form.is_valid():
        instance = add_user_form.save(commit=False)

        instance.save()
        return HttpResponseRedirect('')

    if delete_user_form.is_valid():
        instance = delete_user_form.save(commit=False)
        delete_user_name = delete_user_form.cleaned_data.get("username")

        try:
            User.objects.get(username=delete_user_name).delete()
        except User.DoesNotExist:
            pass

        return HttpResponseRedirect('')

    if add_course_form.is_valid():
        instance = add_course_form.save(commit=False)
        instance.course_link = '/courses/' + instance.course_name
        instance.save()
        return course(request, course_name=instance.course_name)

    if request.user.is_authenticated():
        if request.user.is_staff and not request.user.is_superuser:
            return render(request, "professor_dashboard.html", context)
        elif request.user.is_superuser:
            return render(request, "sysadmin_dashboard.html", context)
        else:
            return render(request, "student_dashboard.html", context)
    else:
        return redirect(settings.LOGIN_URL)
