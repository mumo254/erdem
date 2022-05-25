from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['image', 'heading', 'paragraph1','paragraph2','paragraph3']
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment','name','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment','name','email']

class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailingList
        fields = ['email']