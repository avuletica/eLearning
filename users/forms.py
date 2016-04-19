from django import forms
from users.models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_professor', 'is_site_admin']


class EditUser(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_professor', 'is_site_admin']
