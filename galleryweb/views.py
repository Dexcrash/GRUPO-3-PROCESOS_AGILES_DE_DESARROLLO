from django.http import HttpResponse
from .models import Multimedia, Clip, Usuario, Categoria, TipoMultimedia
from django.contrib.auth import login, logout
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
import json


@csrf_exempt
def multimedias_by_user(request):
    if request.method == 'GET':
        user_id = request.GET["user_id"]
        user = Usuario.objects.get(id=user_id)
        multimedia_list = Multimedia.objects.filter(usuario=user)
        return HttpResponse(serializers.serialize("json", multimedia_list))


@csrf_exempt
def galeria(request):
    media_list = Multimedia.objects.all()
    return HttpResponse(serializers.serialize("json", media_list))


@csrf_exempt
def categorias(request):
    if request.method == 'GET':
        categoria_list = Categoria.objects.all()
        return HttpResponse(serializers.serialize("json", categoria_list))


@csrf_exempt
def tipos(request):
    if request.method == 'GET':
        tipo_list = TipoMultimedia.objects.all()
        return HttpResponse(serializers.serialize("json", tipo_list))


@csrf_exempt
def clips(request):
    # print("Prueba print")
    if request.method == 'GET':
        media_id = request.GET["media_id"]
        multimedia = Multimedia.objects.get(id=media_id)
        clips_list = Clip.objects.filter(multimedia=multimedia)
        return HttpResponse(serializers.serialize("json", clips_list))
    if request.method == 'POST':
        json_clip = json.loads(request.body)
        usuario_creador = Usuario.objects.get(id=json_clip['usuario'])
        new_clip = Clip(
            nombre=json_clip['nombre'],
            usuario=usuario_creador,
            multimedia=Multimedia.objects.get(id=json_clip['multimedia']),
            segundoInicio=json_clip['segundoInicio'],
            segundoFinal=json_clip['segundoFin'])
        new_clip.save()
        subject = 'Nuevo clip agregado'
        message = 'Se he agregado un nuevo clip con nombre: ' + json_clip['nombre']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [usuario_creador.email, ]
        send_mail(subject, message, email_from, recipient_list)
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

