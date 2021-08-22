from django import forms
from image.models import imagen

class ImageForm(forms.ModelForm):
    class Meta:
        model = imagen
        fields = ('__all__')

    name = forms.CharField()
    category = forms.CharField()
    image = forms.ImageField()
