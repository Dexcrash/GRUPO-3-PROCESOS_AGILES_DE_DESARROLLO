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
    url = models.CharField(max_length=1000)
    info = models.CharField(max_length=1000)
    archivo = models.FileField(upload_to='files', blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMultimedia, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return 'Multimedia: ' + self.titulo

class Clip(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    multimedia = models.ForeignKey(Multimedia, on_delete=models.CASCADE)

    def __str__(self):
        return 'Clip: ' + self.nombre

#Borrar ....

class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)
    imageFile = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return 'Image: ' + self.name

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'description', 'type', 'imageFile']

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)