from django import forms
from users.models import *
from crispy_forms.helper import FormHelper


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_staff', 'is_superuser']


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_staff', 'is_superuser']
