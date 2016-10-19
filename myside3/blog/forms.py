from django import forms
from ckeditor.fields import RichTextField
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

