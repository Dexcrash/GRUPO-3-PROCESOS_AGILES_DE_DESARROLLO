from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Multimedia
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


class LoginForm(AuthenticationForm):
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Usuario
        fields = ('email', 'password1')


class MultimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['titulo', 'url', 'usuario', 'autor', 'pais', 'ciudad', 'info', 'tipo', 'categoria', 'archivo']