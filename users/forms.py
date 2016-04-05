from django import forms
from .models import User

class UserLogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        # 	raise forms.ValidationError
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")
        #return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # write validation code.
        return password

