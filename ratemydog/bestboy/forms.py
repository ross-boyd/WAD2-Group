from django import forms
from bestboy.models import Dog, Rating
import os
from bestboy.choices import *


class RatingForm(forms.ModelForm):

    placeholderString = 'Comments are not required :3 woof :)'
    text = forms.CharField(widget=forms.Textarea, required=False)
    text.widget.attrs.update({'class': 'form-control', 'rows': '5',
                              'id': 'comment', 'placeholder':
                              placeholderString})

    class Meta:
        model = Rating
        fields = ('text',)


class UploadForm(forms.ModelForm):
    ALLOWED_TYPES = ['jpg', 'jpeg', 'png', 'gif']

    name = forms.CharField(max_length=100, widget=forms.TextInput,
                           required=False)
    breed = forms.ChoiceField(choices=get_breeds(),
                              widget=forms.Select(choices=get_breeds()))
    picture = forms.ImageField(widget=forms.FileInput)

    name.widget.attrs.update({'id': 'id_name', 'class': 'form-control',
                              'type': 'text', 'name': 'name'})
    breed.widget.attrs.update({'class': 'form-control'})
    picture.widget.attrs.update({'class': 'custom-file-input',
                                 'id': 'id_image', 'type': 'file',
                                 'name': 'image'})

    class Meta:
        model = Dog
        fields = ('name', 'breed', 'picture',)

    def clean_picture(self):
        image = self.cleaned_data.get('picture', None)

        if not image:
            raise forms.ValidationError('Missing image file')
        try:
            extension = os.path.splitext(image.name)[1][1:].lower()
            if extension in self.ALLOWED_TYPES:
                if image.size > 5242880:
                    raise forms.ValidationError('File is greater than 5MB')
                return image
            else:
                raise forms.ValidationError('File types is not allowed')
        except Exception as e:
            raise forms.ValidationError('Can not identify file type')
