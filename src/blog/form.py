from django import forms
from .models import comment

class NewComment(forms.ModelForm):
    class Meta:

        model = comment
        fields = ('name','email','body')