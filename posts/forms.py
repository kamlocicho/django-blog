from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']