from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Multimedia, TipoMultimedia
from .forms import SignUpForm, LoginForm, MultimediaForm
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'galeria/galeria.html',)
    else:
        form = SignUpForm()
    return render(request, 'galeria/signup.html', {'form': form})


def media_detail(request,media_id):
        media = Multimedia.objects.get(id=media_id)
        tipo = TipoMultimedia.objects.all()
        context = {'media': media,
                   'tipo_Audio': list(tipo)[0],
                   'tipo_Imagen': list(tipo)[1],
                   'tipo_Video': list(tipo)[2]}
        return render(request, 'galeria/mediaDetail.html', context)




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
            #messages.error(request, 'username or password not correct')
            return render(request, 'galeria/file_form.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'galeria/file_form.html', {'form': form})

