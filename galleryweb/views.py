from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Multimedia, TipoMultimedia, Clip, Usuario
from .forms import SignUpForm, MultimediaForm, ModifyUser, ClipForm
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.
def galeria(request):
    media_list = Multimedia.objects.all()
    tipo_list = TipoMultimedia.objects.all()
    context = {'media_list': media_list,
               'tipo_Audio': list(tipo_list)[0],
               'tipo_Imagen': list(tipo_list)[1],
               'tipo_Video': list(tipo_list)[2],
               }
    return HttpResponse(serializers.serialize("json", media_list))


def media_detail(request, media_id):
    media = Multimedia.objects.get(id=media_id)
    tipo = TipoMultimedia.objects.all()
    if request.method == 'POST':
        clipForm = ClipForm(request.POST)
        if clipForm.is_valid():
            clipForm.save()
    else:
        clipForm = ClipForm(initial={'multimedia': media, 'usuario': request.user})
    clipsRecomendatos = Clip.objects.filter(multimedia=media)
    print(clipsRecomendatos)
    context = {
                'media': media,
                'tipo_Audio': list(tipo)[0],
                'tipo_Imagen': list(tipo)[1],
                'tipo_Video': list(tipo)[2],
                'form': clipForm,
                'clipsRecomendatos': clipsRecomendatos
    }
    return render(request, 'galeria/mediaDetail.html', context)


def add_image(request):
    if request.method == 'POST':
        form = MultimediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('files:list'))
    else:
        form = MultimediaForm()
    return render(request, 'galeria/file_form.html', {'form': form})


def signup_old(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('files:list'))
    else:
        form = SignUpForm()
    return render(request, 'galeria/file_form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        newUsuario = Usuario(
            username=request.POST.get('username'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            ciudad=request.POST.get('ciudad'),
            pais=request.POST.get('pais'),
            foto=request.POST.get['foto'])
        newUsuario.save()
    return HttpResponse(serializers.serialize("json", [newUsuario]))


def media_list(request, media_id):
        media = Multimedia.objects.get(id=media_id)
        tipo = TipoMultimedia.objects.all()
        context = {'media': media,
                   'tipo_Audio': list(tipo)[0],
                   'tipo_Imagen': list(tipo)[1],
                   'tipo_Video': list(tipo)[2]}
        return render(request, 'galeria/mediaList.html', context)


def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return render(request, 'galeria/galeria.html', )
        else:
            form.get_invalid_login_error()
            return render(request, 'galeria/file_form.html', {'form': form})

    else:
        if request.user.is_authenticated:
            return render(request, 'galeria/galeria.html', )
        else:
            form = AuthenticationForm()

    return render(request, 'galeria/file_form.html', {'form': form})


def editUser(request):
    """
    Editar usuario de forma simple.
    """
    user = request.user
    if request.method == 'POST':
        form = ModifyUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('files:list'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('files:list'))
        else:
            form = ModifyUser(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'galeria/file_form.html', context)

