from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import *
from source import settings


@login_required
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


@user_passes_test(lambda user: user.is_professor)
def course(request, course_name=None):
    title = course_name
    add_chapter_form = AddChapterForm(request.POST or None)

    queryset_course = Course.objects.all()
    queryset_chapter = Chapter.objects.filter(course__course_name=course_name)

    context = {
        "title": title,
        "add_chapter_form": add_chapter_form,
        "queryset_course": queryset_course,
        "queryset_chapter": queryset_chapter,
    }

    if add_chapter_form.is_valid():
        instance = add_chapter_form.save(commit=False)
        instance.course = Course.objects.get(course_name=title)
        instance.save()
        return redirect(instance.get_absolute_url())

    return render(request, "courses/course.html", context)


@user_passes_test(lambda user: user.is_professor)
def chapter(request, course_name=None, chapter_name=None):
    title = course_name + " : " + chapter_name

    context = {
        "title": title,
    }

    return render(request, "courses/chapter.html", context)


@user_passes_test(lambda user: user.is_professor)
def delete_chapter(request, course_name=None, chapter_id=None):
    instance = Chapter.objects.get(id=chapter_id)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_course(request, course_name=None):
    if request.user.is_authenticated and request.user.is_professor:
        instance = Course.objects.get(course_name=course_name)
        instance.delete()
        return HttpResponseRedirect(reverse('profile'))