from django import forms

from .models import AudioBook


class AudioBookForm(forms.ModelForm):
    class Meta:
        model = AudioBook
        fields = '__all__'
