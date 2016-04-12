from django import forms
from users.models import *


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class DeleteUser(forms.ModelForm):
    class Meta:
        model = DeleteUser
        fields = ['username']
