from django import forms
from users.models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email']


class DeleteUser(forms.ModelForm):
    class Meta:
        model = DeleteUser
        fields = ['username']
