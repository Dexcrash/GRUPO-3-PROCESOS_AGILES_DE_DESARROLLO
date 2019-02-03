from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Multimedia, ImageForm, Categoria, TipoMultimedia
from django.urls import reverse

# Create your views here.

def galeria(request):
    media_list = Multimedia.objects.all()
    tipo_list = TipoMultimedia.objects.all()
    context = {'media_list': media_list,
               'tipo_Audio': list(tipo_list)[0],
               'tipo_Imagen': list(tipo_list)[1],
               'tipo_Video': list(tipo_list)[2]}
    return render(request, 'galeria/galeria.html', context)

def index(request):
    images_list = Image.objects.all()
    print(images_list)
    context = {'images_list': images_list}
    return render(request, 'tests/list.html', context)

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = ImageForm()
    return render(request, 'galeria/image_form.html', {'form': form})