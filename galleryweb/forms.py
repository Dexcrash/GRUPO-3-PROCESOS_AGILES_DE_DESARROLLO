from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario, Multimedia
from django.forms import ModelForm
from django.db import models


class SignUpForm(UserCreationForm):
    first_name = models.CharField(max_length=30, help_text='Optional.')
    last_name = models.CharField(max_length=30, help_text='Optional.')
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'ciudad', 'pais', 'foto' )

class LoginForm(AuthenticationForm):
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Usuario
        fields = ('email', 'password1')

class MultimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['titulo', 'url', 'usuario', 'autor', 'pais', 'ciudad', 'info', 'tipo', 'categoria', 'archivo']

