from django import forms
from .models import comment, post

class NewComment(forms.ModelForm):
    class Meta:

        model = comment
        fields = ('name','email','body')

class PostCreateform(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='الموضوع', widget=forms.Textarea )
    class Meta:
        model = post 
        fields = ['title', 'content']