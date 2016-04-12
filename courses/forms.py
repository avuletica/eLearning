from django import forms
from .models import Course


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']
