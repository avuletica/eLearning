from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']

    def clean_course_name(self):
        course_name = self.cleaned_data['course_name']
        if Course.objects.filter(course_name=course_name).count() > 0:
            raise forms.ValidationError('This course name is already in use!')
        return course_name


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_name']


class DeleteCourseForm(forms.ModelForm):
    class Meta:
        model = DeleteCourse
        fields = ['course_name']


class DeleteChapterForm(forms.ModelForm):
    class Meta:
        model = DeleteChapter
        fields = ['chapter_name']