from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_name']