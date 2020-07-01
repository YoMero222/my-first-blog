from django import forms

from .models import Post

class NameForm(forms.Form):
    search = forms.CharField(label='search', max_length=100)
