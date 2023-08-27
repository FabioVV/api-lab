from django.contrib import admin

# Register your models here.

from laboratorios.models import Laboratorio


class LaboratorioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Laboratorio, LaboratorioAdmin)
