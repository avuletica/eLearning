from django import forms
from .models import Course
from users.models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']


