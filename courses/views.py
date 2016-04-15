from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
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


def course(request, course_name=None):
    title = course_name
    add_chapter_form = AddChapterForm(request.POST or None)
    delete_chapter_form = DeleteChapterForm(request.POST or None)

    queryset = Course.objects.all()
    queryset_chapter = Chapter.objects.all()
    queryset_text_block = TextBlock.objects.all()
    queryset_yt_link = YTLink.objects.all()

    context = {
        "title": title,
        "add_chapter_form": add_chapter_form,
        "delete_chapter_form": delete_chapter_form,
        "queryset": queryset,
        "queryset_chapter": queryset_chapter,
        "queryset_text_block": queryset_text_block,
        "queryset_yt_link": queryset_yt_link
    }

    if add_chapter_form.is_valid():
        instance = add_chapter_form.save(commit=False)
        instance.course = Course.objects.get(course_name=title)
        instance.save()
        return redirect('/courses')  #instance.get_absolute_url()

    if request.user.is_authenticated():
        return render(request, "courses/course.html", context)
    else:
        return redirect(settings.LOGIN_URL)