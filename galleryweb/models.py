from django.db import models
from django.forms import  ModelForm


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=1000)

    def __str__(self):
        return 'Usuario: ' + self.nombre + ' ' + self.apellido


class TipoMultimedia(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return 'Nombre categoria: ' + self.nombre


class Multimedia(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    info = models.CharField(max_length=1000)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True)
    archivo = models.FileField(upload_to='files', blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMultimedia, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return 'Multimedia: ' + self.titulo


class MultimediaForm(ModelForm):
    class Meta:
        model = Multimedia
        fields = ['titulo', 'url', 'usuario', 'autor', 'pais', 'ciudad', 'info', 'tipo', 'categoria', 'archivo']


class Clip(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    multimedia = models.ForeignKey(Multimedia, on_delete=models.CASCADE)

    def __str__(self):
        return 'Clip: ' + self.nombre
