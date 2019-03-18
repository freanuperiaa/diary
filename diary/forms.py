from django import forms

from .models import Post, Tag

#forms here

class EntryForm(forms.Form):
    title = forms.CharField(max_length=200)
    tags = forms.ModelMultipleChoiceField(Tag.objects.all())
    content = forms.CharField(max_length=2000)
