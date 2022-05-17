from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['image', 'heading', 'text']
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment','name','email']