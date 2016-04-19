from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']

    def clean_course_name(self):
        course_name = self.cleaned_data.get('course_name')

        if not course_name.isalnum():
            raise forms.ValidationError("Please make sure all characters are alphabetic")

        return course_name


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_name']

    def clean_chapter_name(self):
        chapter_name = self.cleaned_data.get('chapter_name')

        if not chapter_name.isalnum():
            raise forms.ValidationError("Please make sure all characters are alphabetic")

        return chapter_name
