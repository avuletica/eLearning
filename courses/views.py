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

    return render(request, "user.html", context)


@user_passes_test(lambda user: user.is_professor)
def course(request, course_name=None):
    title = course_name
    add_chapter_form = AddChapterForm(request.POST or None)

    queryset_chapter = Chapter.objects.filter(course__course_name=course_name)

    context = {
        "title": title,
        "add_chapter_form": add_chapter_form,
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

    place = Chapter.objects.filter(course__course_name=course_name).get(chapter_name=chapter_name).id

    add_link_form = AddLinkForm(request.POST or None)
    add_txt_form = AddTxtForm(request.POST or None)

    queryset_txt_block = TextBlock.objects.filter(text_block_fk__id=place)
    queryset_yt_link = YTLink.objects.filter(yt_link_fk__id=place)

    context = {
        "title": title,
        "add_link_form": add_link_form,
        "add_txt_form": add_txt_form,
        "queryset_yt_link": queryset_yt_link,
        "queryset_txt_block": queryset_txt_block
    }

    if add_link_form.is_valid():
        instance = add_link_form.save(commit=False)
        instance.yt_link_fk = Chapter.objects.get(id=place)
        instance.save()
        return render(request, "courses/chapter.html", context)

    if add_txt_form.is_valid():
        instance = add_txt_form.save(commit=False)
        instance.text_block_fk = Chapter.objects.get(id=place)
        instance.save()
        return render(request, "courses/chapter.html", context)

    return render(request, "courses/chapter.html", context)


@user_passes_test(lambda user: user.is_professor)
def delete_course(request, course_name=None):
    instance = Course.objects.get(course_name=course_name)
    instance.delete()
    return HttpResponseRedirect(reverse('profile'))


@user_passes_test(lambda user: user.is_professor)
def delete_chapter(request, course_name=None, chapter_id=None):
    instance = Chapter.objects.get(id=chapter_id)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_professor)
def delete_yt_link(request, course_name=None, chapter_name=None, yt_id=None):
    instance = YTLink.objects.get(id=yt_id)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_professor)
def delete_text_block(request, course_name=None, chapter_name=None, txt_id=None):
    instance = TextBlock.objects.get(id=txt_id)
    instance.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
