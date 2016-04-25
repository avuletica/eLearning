from courses.forms import AddCourseForm
from courses.models import *
from .forms import *

from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from itertools import chain


def home(request):
    title = 'eLearning'

    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def about(request):
    title = 'About'

    context = {
        "title": title,
    }

    return render(request, "users/about.html", context)


def contact(request):
    title = 'Contact'

    context = {
        "title": title,
    }

    return render(request, "users/contact.html", context)


@login_required
def profile(request):
    if request.user.is_site_admin:
        return redirect(reverse('admin'))

    elif request.user.is_professor:
        return redirect(reverse('professor'))

    return redirect(reverse('student'))


@user_passes_test(lambda user: user.is_site_admin)
def admin(request):
    title = 'Admin'
    add_user_form = AddUser(request.POST or None)
    queryset = UserProfile.objects.all()

    context = {
        "title": title,
        "add_user_form": add_user_form,
        "queryset": queryset,
    }

    if add_user_form.is_valid():
        instance = add_user_form.save(commit=False)
        passwd = add_user_form.cleaned_data.get("password")
        instance.password = make_password(password=passwd,
                                          salt='salt', )
        instance.save()
        reverse('profile')

    return render(request, "users/sysadmin_dashboard.html", context)


@user_passes_test(lambda user: user.is_professor)
def professor(request):
    title = 'Professor'
    add_course_form = AddCourseForm(request.POST or None)
    queryset_course = Course.objects.filter(user__username=request.user)

    context = {
        "title": title,
        "add_course_form": add_course_form,
        "queryset_course": queryset_course,
    }

    if add_course_form.is_valid():
        instance = add_course_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect(instance.get_absolute_url())

    return render(request, "users/professor_dashboard.html", context)


@login_required
def student(request):
    title = 'Student'
    queryset = Course.objects.filter(students=request.user)

    context = {
        "queryset": queryset
    }

    return render(request, "users/student_dashboard.html", context)


@user_passes_test(lambda user: user.is_site_admin)
def update_user(request, username):
    user = UserProfile.objects.get(username=username)
    data_dict = {'username': user.username, 'email': user.email}
    update_user_form = EditUser(initial=data_dict, instance=user)
    title = 'Edit user'
    path = request.path.split('/')[1]
    redirect_path = path
    path = path.title()

    context = {
        "title": title,
        "update_user_form": update_user_form,
        "path": path,
        "redirect_path": redirect_path,
    }

    if request.POST:
        user_form = EditUser(request.POST, instance=user)

        if user_form.is_valid():
            instance = user_form.save(commit=False)
            passwd = user_form.cleaned_data.get("password")

            if passwd:
                instance.password = make_password(password=passwd,
                                                  salt='salt', )
            instance.save()

            return redirect(reverse('profile'))

    return render(request, "users/edit_user.html", context)


@user_passes_test(lambda user: user.is_site_admin)
def delete_user(request, username):
    user = UserProfile.objects.get(username=username)
    user.delete()
    return redirect(reverse('profile'))


@login_required
def student_course(request, course_name, chapter_name):
    course = Course.objects.filter(course_name=course_name)
    chapter_list = Chapter.objects.filter(course=course)
    chapter = Chapter.objects.filter(chapter_name=chapter_name)
    text = TextBlock.objects.filter(text_block_fk=chapter)
    videos = YTLink.objects.filter(yt_link_fk=chapter)

    result_list = sorted(
        chain(text,videos),
        key=lambda instance: instance.date_created)


    context = {
        "course_name": course_name,
        "chapter_list": chapter_list,
        "result_list": result_list,
    }

    return  render(request, "users/student_courses.html", context)


@login_required
def course_homepage(request, course_name):
    course = Course.objects.filter(course_name=course_name)
    chapter_list = Chapter.objects.filter(course=course)


    context = {
        "course_name": course_name,
        "chapter_list": chapter_list,
    }

    return  render(request, "users/course_homepage.html", context)