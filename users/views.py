from django.shortcuts import render

from .forms import LogInForm


# Create your views here.
def home(request):
    title = 'eLearning'
    form = LogInForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        # print request.POST['email'] #not recommended
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        # 	instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Welcome user!"
        }

    return render(request, "registration/login.html", context)

