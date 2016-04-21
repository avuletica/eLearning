from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import *
from django.db.models import Q

@login_required
def courses(request):
    title = 'Courses'
    queryset = Course.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }

    return render(request, "users/course.html", context)


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
    place = Chapter.objects.get(course__course_name=course_name, chapter_name=chapter_name).id

    add_link_form = AddLinkForm(request.POST or None)
    add_txt_form = AddTxtForm(request.POST or None)

    queryset_txt_block = TextBlock.objects.filter(text_block_fk__id=place)
    queryset_yt_link = YTLink.objects.filter(yt_link_fk__id=place)

    context = {
        "title": title,
        "course_name": course_name,
        "add_link_form": add_link_form,
        "add_txt_form": add_txt_form,
        "queryset_yt_link": queryset_yt_link,
        "queryset_txt_block": queryset_txt_block
    }

    if add_link_form.is_valid() and 'add_link' in request.POST:
        instance = add_link_form.save(commit=False)
        instance.yt_link_fk = Chapter.objects.get(id=place)
        instance.save()
        return redirect(reverse('chapter', kwargs={'course_name': course_name,
                                                   'chapter_name': chapter_name}))

    if add_txt_form.is_valid() and 'add_text' in request.POST:
        instance = add_txt_form.save(commit=False)
        instance.text_block_fk = Chapter.objects.get(id=place)
        instance.save()
        return redirect(reverse('chapter', kwargs={'course_name': course_name,
                                                   'chapter_name': chapter_name}))

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


@user_passes_test(lambda user: user.is_professor)
def update_course(request, course_name=None):
    instance = Course.objects.get(course_name=course_name)
    update_course_form = EditCourseForm(request.POST or None, instance=instance)

    title = 'Edit course'

    context = {
        "title": title,
        "form": update_course_form,
    }

    if update_course_form.is_valid():
        update_course_form.save()
        return redirect(reverse('profile'))

    return render(request, "courses/edit.html", context)


@user_passes_test(lambda user: user.is_professor)
def update_chapter(request, course_name=None, chapter_id=None):
    instance = Chapter.objects.get(id=chapter_id)
    update_chapter_form = EditChapterForm(request.POST or None, instance=instance)

    title = 'Edit chapter'

    context = {
        "title": title,
        "form": update_chapter_form,
    }

    if update_chapter_form.is_valid():
        update_chapter_form.save()
        return redirect(reverse('course', kwargs={'course_name': course_name}))

    return render(request, "courses/edit.html", context)


@user_passes_test(lambda user: user.is_professor)
def update_yt_link(request, course_name=None, yt_id=None):
    instance = YTLink.objects.get(id=yt_id)
    update_link_form = EditYTLinkForm(request.POST or None, instance=instance)
    chapters = Chapter.objects.get(course__course_name=course_name)

    title = 'Edit link'

    context = {
        "title": title,
        "form": update_link_form,
    }

    if update_link_form.is_valid():
        update_link_form.save()
        return redirect(reverse('chapter', kwargs={'course_name': course_name,
                                                   "chapter_name": chapters.chapter_name}))

    return render(request, "courses/edit.html", context)


@user_passes_test(lambda user: user.is_professor)
def update_text_block(request, course_name=None, txt_id=None):
    instance = TextBlock.objects.get(id=txt_id)
    update_txt_form = EditTxtForm(request.POST or None, instance=instance)
    chapters = Chapter.objects.get(course__course_name=course_name)

    title = 'Edit lesson'

    context = {
        "title": title,
        "form": update_txt_form,
    }

    if update_txt_form.is_valid():
        update_txt_form.save()
        return redirect(reverse('chapter', kwargs={'course_name': course_name,
                                                   "chapter_name": chapters.chapter_name}))

    return render(request, "courses/edit.html", context)


@user_passes_test(lambda user: user.is_professor)
def list_students(request, course_name=None):
    title = "Edit students in course " + course_name
    course = Course.objects.get(course_name=course_name)
    added_students = UserProfile.objects.filter(students_to_course=course)
    excluded_students = UserProfile.objects.exclude(students_to_course=course).filter(is_professor=False).filter(is_site_admin=False)
    
    query_first = request.GET.get("q1")
    if query_first:
        excluded_students = excluded_students.filter(username__icontains=query_first)

    query_second = request.GET.get("q2")
    if query_second:
        added_students = added_students.filter(username__icontains=query_second)    

    context = {
        "title": title,
        "excluded_students": excluded_students,
        "added_students": added_students, 
        "course_name": course_name,       
    }

    return render(request, "courses/add_students.html", context)


def add_students(request,student_id, course_name=None):
    student = UserProfile.objects.get(id=student_id)
    course = Course.objects.get(course_name=course_name)
    course.students.add(student)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_professor)
def remove_students(request, student_id, course_name=None):
    student = UserProfile.objects.get(id=student_id)
    course = Course.objects.get(course_name=course_name)
    course.students.remove(student) 

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


