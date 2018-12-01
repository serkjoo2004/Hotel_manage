from django import forms
from .models import Request_post

class PostForm(forms.ModelForm):
    class Meta:
        model = Request_post
        fields = ('author', 'title', 'text','dept')

