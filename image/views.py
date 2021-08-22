from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from image.models import imagen
from .forms import ImageForm

# Create your views here.

def MostrarImagen (request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'MostrarImagen.html', {'form': form,'img_obj': img_obj})
    else:
        form = ImageForm()
    img = imagen.objects.all()
    return render(request, 'MostrarImagen.html', {'form': form, 'img': img})
