from django import forms
from bestboy.models import Dog, Comment


class RatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=128, required=False)

    class Meta:
        model = Dog
        fields = ('rating',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Comment
        fields = ('text',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('dog_id', 'name', 'owner',
                  'rating', 'average', 'picture', 'votes',)
