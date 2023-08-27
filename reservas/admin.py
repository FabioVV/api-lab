from django.contrib import admin

# Register your models here.

from reservas.models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reserva, ReservaAdmin)
