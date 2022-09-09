from django.contrib import admin
from .models import Usuario
# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','fecha_registro','activo','usuario','contrasena')
    list_filter = ('nombre','edad')

admin.site.register(Usuario, UsuariosAdmin)
