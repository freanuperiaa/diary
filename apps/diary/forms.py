from django import forms
from django.forms import ModelForm

from .models import Post



#use ModelForm here

class EntryModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

