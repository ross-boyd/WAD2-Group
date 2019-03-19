from django import forms
from bestboy.models import Dog, Rating


class RatingForm(forms.ModelForm):
    score = forms.CharField(max_length=128, required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Rating
        fields = ('score', 'text',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('dog_id', 'name', 'owner',
                  'score', 'picture', 'votes',)
