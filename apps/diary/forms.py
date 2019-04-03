from django import forms
from django.forms import ModelForm

from .models import Post


class EntryModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

