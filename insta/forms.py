from django import forms
from django.forms import Textarea
from .models import Post, Comment

class PostForm(forms.ModelForm):
    img = forms.ImageField(label='',)
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'post',}))
    class Meta:
        model = Post
        fields = ( 'img', 'content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'댓글 달기...',}), label='', )
    class Meta:
        model = Comment
        fields = ( 'content',)