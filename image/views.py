from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from image.models import imagen
from .forms import ImageForm, FormImagen

# Create your views here.

def MostrarImagen (request):
    form2 = FormImagen()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        #if FormImagen.is_valid():
         #   ImageForm.save()
          #  messages.info(request, '!Informacion Guardad con Exito!')
    else:
        form = ImageForm()

    img = imagen.objects.all()

    return render(request, 'MostrarImagen.html', {'form': form, 'img': img, 'form2': form2})


#imagen = request.POST.get('file').read()
#uploadFile = request.FILES['file'].read()
# return render(request, 'MostrarImagen.html', {'imagen': imagen})