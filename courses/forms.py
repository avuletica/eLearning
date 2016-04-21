from django import forms
from django.core.exceptions import ValidationError
from .models import *
from users.models import *
import re


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']

    def clean_course_name(self):
        course_name = self.cleaned_data.get('course_name')

        regexp = re.compile(r'[0-9a-zA-Z ]')
        if not regexp.match(course_name):
            raise forms.ValidationError("Please make sure course name contains (a-z, A-Z, 0-9, space) characters")

        return course_name


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_name']

    def clean_chapter_name(self):
        chapter_name = self.cleaned_data.get('chapter_name')

        regexp = re.compile(r'[0-9a-zA-Z ]')
        if not regexp.match(chapter_name):
            raise forms.ValidationError("Please make sure chapter name contains (a-z, A-Z, 0-9, space) characters")

        return chapter_name


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = YTLink
        fields = ['link']

    def __init__(self, *args, **kwargs):
        super(AddLinkForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False


class AddTxtForm(forms.ModelForm):
    class Meta:
        model = TextBlock
        fields = ['chapter_description']

    def __init__(self, *args, **kwargs):
        super(AddTxtForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']


class EditChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_name']


class EditYTLinkForm(forms.ModelForm):
    class Meta:
        model = YTLink
        fields = ['link']


class EditTxtForm(forms.ModelForm):
    class Meta:
        model = TextBlock
        fields = ['chapter_description']

class AddStudentToCourse(forms.ModelForm):
    class Meta:
        model = AddStudents
        fields = ['student_name']

    def clean_student_name(self):
        student_name = self.cleaned_data['student_name']
        if not UserProfile.objects.filter(username=student_name).exists():
            raise ValidationError("User does not exists!")
        return student_name