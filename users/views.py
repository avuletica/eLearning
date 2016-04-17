from django.shortcuts import render, redirect
from source import settings
from courses.forms import AddCourseForm, DeleteCourseForm
from courses.models import Course

from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    title = 'Profile'
    add_course_form = AddCourseForm(request.POST or None)
    delete_course_form = DeleteCourseForm(request.POST or None)
    add_user_form = AddUser(request.POST or None)
    queryset = User.objects.all()

    context = {
        "title": title,
        "add_course_form": add_course_form,
        "delete_course_form": delete_course_form,
        "add_user_form": add_user_form,
        "queryset": queryset,
    }

    if add_user_form.is_valid():
        instance = add_user_form.save(commit=False)
        passwd = add_user_form.cleaned_data.get("password")
        instance.password = make_password(password=passwd,
                                          salt='salt', )
        instance.save()
        return HttpResponseRedirect('/profile')

    if add_course_form.is_valid():
        instance = add_course_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect(instance.get_absolute_url())

    if request.user.is_authenticated():
        if request.user.is_staff and not request.user.is_superuser:
            queryset = Course.objects.all()
            context = {
                "queryset": queryset,
                "form": add_course_form
            }
            return render(request, "professor_dashboard.html", context)
        elif request.user.is_superuser:
            return render(request, "sysadmin_dashboard.html", context)
        else:
            return render(request, "student_dashboard.html", context)
    else:
        return redirect(settings.LOGIN_URL)


@user_passes_test(lambda user: user.is_superuser)
def update_user(request, username):
    user = User.objects.get(username=username)
    data_dict = {'username': user.username, 'email': user.email}
    update_user_form = EditUser(initial=data_dict, instance=user)
    title = 'Edit user'
    context = {
        "title": title,
        "update_user_form": update_user_form,
    }

    if request.POST:
        user_form = EditUser(request.POST, instance=user)

        if user_form.is_valid():
            instance = user_form.save(commit=False)
            passwd = user_form.cleaned_data.get("password")
            instance.password = make_password(password=passwd,
                                              salt='salt', )
            instance.save()

            return redirect('/profile/')

    return render(request, "edit_user.html", context)


@user_passes_test(lambda user: user.is_superuser)
def delete_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('/profile/')
