import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Multimedia, TipoMultimedia, Clip, Usuario
from .forms import SignUpForm, MultimediaForm, ModifyUser, ClipForm
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


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


@csrf_exempt
def clips(request):
    if request.method == 'GET':
        media_id = request.GET["media_id"]
        multimedia = Multimedia.objects.get(id=media_id)
        clips_list = Clip.objects.filter(multimedia=multimedia)
        return HttpResponse(serializers.serialize("json", clips_list))
    if request.method == 'POST':
        json_clip = json.loads(request.body)
        new_clip = Clip(
            nombre=json_clip['nombre'],
            usuario=json_clip['usuario'],
            multimedia=json_clip['multimedia'],
            segundoInicio=json_clip['segundoInicio'],
            segundoFinal=json_clip['segundoFinal'])
        new_clip.save()
    return HttpResponse(serializers.serialize("json", [new_clip]))


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


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        newUsuario = Usuario(
            username=jsonUser['username'],
            password=jsonUser['password'],
            last_name=jsonUser['last_name'],
            email=jsonUser['email'],
            ciudad=jsonUser['ciudad'],
            pais=jsonUser['pais'],
            foto=jsonUser['foto'])
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
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = True
        else:
            message = False

    return HttpResponse(serializers.serialize("json", [message]))


def loginview_old(request):
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

