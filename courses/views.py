from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import AddCourseForm
from .models import Course


@login_required(login_url='/accounts/login')
def profile(request):
    title = 'Profile'
    form = AddCourseForm(request.POST or None)
    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.course_link = '/' + instance.course_name
        instance.save()
        return HttpResponseRedirect('')

    return render(request, "user_profile.html", context)


@login_required(login_url='/accounts/login')
def course(request):
    title = 'Course'
    queryset = Course.objects.all()

    context = {
        "title": title,
        "queryset": queryset,
    }

    return render(request, "user.html", context)