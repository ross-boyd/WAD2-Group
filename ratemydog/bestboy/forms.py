from django import forms
from bestboy.models import Dog


class RatingForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)
    rating = forms.CharField(max_length=128, help_text="Please enter a rating",
                             required=False)

    class Meta:
        model = Dog
        fields = ('name', 'rating',)
