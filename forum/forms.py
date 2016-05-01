from django import forms
from .models import *
import re


class AddNewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject', 'topic_message']

    def clean_subject(self):
        topic_name = self.cleaned_data.get('subject')

        regexp = re.compile(r'[0-9a-zA-Z!.? ]')
        if not regexp.match(topic_name):
            raise forms.ValidationError(
                "Please make sure topic name contains (a-z, A-Z, 0-9, !.?' ') characters")

        return topic_name


class AddNewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
