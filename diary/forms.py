from django import forms
from django.forms import ModelForm

from .models import Post, Tag

#forms here

class EntryForm(forms.Form):
    title = forms.CharField(max_length=200)
    tags = forms.ModelMultipleChoiceField(Tag.objects.all(), required=False)
    more_tags = forms.CharField(max_length=200, required=False)
    content = forms.CharField(max_length=2000, widget=forms.Textarea)


#use ModelForm here

class EntryModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'content']
