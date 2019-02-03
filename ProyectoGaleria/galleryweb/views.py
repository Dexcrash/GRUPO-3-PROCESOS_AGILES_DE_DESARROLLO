from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, Multimedia, ImageForm
from django.urls import reverse

# Create your views here.

def galeria(request):
    multimedia = Multimedia.objects.all()
    context = {'multimedia': multimedia}
    return render(request, 'galeria/galeria.html', context)

def index2(request):
    return HttpResponse("Hello World!")





def index(request):
    images_list = Image.objects.all()
    print(images_list)
    context = {'images_list': images_list}
    return render(request, 'tests/list.html', context)

def index2(request):
    return HttpResponse("Hello World!")


def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = ImageForm()
    return render(request, 'tests/image_form.html', {'form': form})