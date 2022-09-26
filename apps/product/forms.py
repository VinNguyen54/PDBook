from django import forms
from django.forms import ModelForm
from .models import Comment

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields = ['created_by', 'body']