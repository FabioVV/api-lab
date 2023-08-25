from django.contrib import admin

# Register your models here.
from django.contrib import admin
from usuarios.models import Usuario, Usuario_tipo


class UsuarioAdmin(admin.ModelAdmin):
    pass

class UsuarioTipoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Usuario_tipo, UsuarioTipoAdmin)