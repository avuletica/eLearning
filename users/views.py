from django.shortcuts import render, redirect
from source import settings
from courses.views import course
from courses.forms import AddCourseForm


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


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
        if request.user.is_staff==True and request.user.is_superuser==False:
            return render(request, "professor_dashboard.html", context)
        elif request.user.is_superuser==True:
            return render(request, "sysadmin_dashboard.html", context)
        else:
            return render(request, "student_dashboard.html", context)
    else:
        return redirect(settings.LOGIN_URL)