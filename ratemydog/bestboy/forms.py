from django import forms
from bestboy.models import Dog, Rating
import os
from bestboy.choices import *


class RatingForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = Rating
        fields = ('text',)


class UploadForm(forms.ModelForm):
    ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'gif']

    name = forms.CharField(max_length=100)
    breed = forms.ChoiceField(choices=BREED_CHOICES)
    picture = forms.ImageField()

    class Meta:
        model = Dog
        fields = ('name','breed','picture',)

    def clean_picture(self):
        image = self.cleaned_data.get('picture', None)
        
        if not image:
            raise forms.ValidationError('Missing image file')
        try:
            extension = os.path.splitext(image.name)[1][1:].lower()
            if extension in self.ALLOWED_TYPES:
                return image
            else:
                raise forms.ValidationError('File types is not allowed')
        except Exception as e:
            raise forms.ValidationError('Can not identify file type')
