import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Multimedia, TipoMultimedia, Clip, Usuario
from .forms import SignUpForm, MultimediaForm, ModifyUser, ClipForm
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import json


@csrf_exempt
def multimedias_by_user(request):
    if request.method == 'GET':
        user_id = request.GET["user_id"]
        user = Usuario.objects.get(id=user_id)
        multimedia_list = Multimedia.objects.filter(usuario=user)
        return HttpResponse(serializers.serialize("json", multimedia_list))


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
        print("----------------------")
        print(json_clip['usuario'])
        usuario_creador = Usuario.objects.get(id=json_clip['usuario'])
        new_clip = Clip(
            nombre=json_clip['nombre'],
            usuario=usuario_creador,
            multimedia=Multimedia.objects.get(id=json_clip['multimedia']),
            segundoInicio=json_clip['segundoInicio'],
            segundoFinal=json_clip['segundoFin'])
        new_clip.save()
        email = EmailMessage('Clip agregado', 'Se ha agregado un nuevo clip', to=[usuario_creador.email])
        email.send()
        #send_mail('<Your subject>', '<Your message>', 'n.lema@uniandes.edu.co', ['n.lema@uniandes.edu.co'])
        return HttpResponse(serializers.serialize("json", [new_clip]))


@csrf_exempt
def edit_user(request):

    if request.method == 'POST':
        json_usuario = json.loads(request.body)
        user_edit = Usuario.objects.get(id=json_usuario['usuario_id'])
        user_edit.first_name = json_usuario['first_name']
        user_edit.last_name = json_usuario['last_name']
        user_edit.email = json_usuario['email']
        user_edit.ciudad = json_usuario['ciudad']
        user_edit.pais = json_usuario['pais']
        user_edit.foto = json_usuario['foto']
        user_edit.save()
        return HttpResponse(serializers.serialize("json", [user_edit]))


@csrf_exempt
def get_user_by_id(request):

    if request.method == 'GET':
        user = Usuario.objects.get(id=request.GET["usuario_id"])
        return HttpResponse(serializers.serialize("json", [user]))


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
        login(request, newUsuario)
    return HttpResponse(serializers.serialize("json", [newUsuario]))


@csrf_exempt
def logOut(request):
    logout(request)
    mess = {}
    mess['logOut'] = True
    return HttpResponse(json.dumps(mess), content_type="application/json")


def media_list(request, media_id):
    media = Multimedia.objects.get(id=media_id)
    tipo = TipoMultimedia.objects.all()
    context = {'media': media,
               'tipo_Audio': list(tipo)[0],
               'tipo_Imagen': list(tipo)[1],
               'tipo_Video': list(tipo)[2]}
    return render(request, 'galeria/mediaList.html', context)


@csrf_exempt
def loginview(request):
    jsonUser = json.loads(request.body)
    username = jsonUser['username']
    password = jsonUser['password']
    try:
        user = Usuario.objects.get(username=username, password=password)
        login(request, user)
        return HttpResponse(serializers.serialize("json", [user]))
    except:
        mess = {}
        mess['logIn'] = False
        return HttpResponse(json.dumps(mess), content_type="application/json")


@csrf_exempt
def authenticate(request):
    au = request.user.is_authenticated
    id = request.user.id
    mess = {}
    mess["autho"] = au;
    mess["id"] = id;
    return HttpResponse(json.dumps(mess), content_type="application/json")


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


def editUser_old(request):
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
