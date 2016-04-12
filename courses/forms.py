from django import forms
from .models import Course
from users.models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class DeleteUser(forms.ModelForm):
    class Meta:
        model = DeleteUser
        fields = ['username']
