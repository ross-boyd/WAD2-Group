from django import forms
from bestboy.models import Dog


class RatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=128, required=False)

    class Meta:
        model = Dog
        fields = ('rating',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('dog_id', 'name', 'owner',
                  'rating', 'average', 'picture', 'votes',)
