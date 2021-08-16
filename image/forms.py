from django import forms
from django.forms import ModelForm
from image.models import imagen

class ImageForm(forms.Form):
    file = forms.ImageField()

class FormImagen(ModelForm):
    class Meta:
        model = imagen
        fields = '__all__'
        #widgets = {'name': forms.HiddenInput()}