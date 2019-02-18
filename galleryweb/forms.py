from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario, Multimedia, Clip
from django.forms import ModelForm
from django.db import models
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Requerido.', label="Nombre de usuario")
    first_name = forms.CharField(max_length=30, help_text='Requerido.', label="Nombre")
    last_name = forms.CharField(max_length=30, help_text='Requerido.', label="Apellidos")
    email = forms.EmailField(max_length=254, help_text='Requerido', label="Dirección de correo")
    password1 = forms.CharField(max_length=16, label='Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'text': 'Contraseña'}))
    password2 = forms.CharField(max_length=16, label='Confirmar contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'ciudad', 'pais', 'foto')


class MultimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['titulo', 'url', 'usuario', 'autor', 'pais', 'ciudad', 'info', 'tipo', 'categoria', 'archivo']


class ModifyUser(UserChangeForm):
    password = None
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'ciudad', 'pais', 'foto')

class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = ['multimedia', 'nombre', 'usuario', 'segundoInicio', 'segundoFinal']
        widgets = {'multimedia': forms.HiddenInput(), 'usuario': forms.HiddenInput() }