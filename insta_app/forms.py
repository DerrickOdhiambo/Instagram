from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'input is-medium'}), required=False)

    class Meta:
        model = Comment
        fields = ['text']
