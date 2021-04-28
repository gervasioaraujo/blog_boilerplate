from django import forms

from .models import Post, Comment


class PostModelForm(forms.ModelForm):

    summary = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 123, 'rows': 7}))

    class Meta:
        model = Post
        fields = '__all__'


class CreateCommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = [
            'post'
        ]
