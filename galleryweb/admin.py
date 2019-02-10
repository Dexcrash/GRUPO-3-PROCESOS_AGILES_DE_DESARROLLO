from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *

admin.site.register(Usuario, UserAdmin)
admin.site.register(TipoMultimedia)
admin.site.register(Categoria)
admin.site.register(Multimedia)
admin.site.register(Clip)
