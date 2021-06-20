from django import forms
from django.db.models import fields
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'image', 'body']