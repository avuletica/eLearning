from django import forms
from users.models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_staff']


class DeleteUser(forms.ModelForm):
    class Meta:
        model = DeleteUser
        fields = ['username']


class EditUser(forms.ModelForm):
    class Meta:
        model = EditUser
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email']
