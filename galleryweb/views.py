from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Multimedia, TipoMultimedia, MultimediaForm
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


def add_image(request):
    if request.method == 'POST':
        form = MultimediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('files:list'))
    else:
        form = MultimediaForm()
    return render(request, 'galeria/file_form.html', {'form': form})
