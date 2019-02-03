from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Usuario)
admin.site.register(TipoMultimedia)
admin.site.register(Categoria)
admin.site.register(Multimedia)
admin.site.register(Clip)