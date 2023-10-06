from django.db import models as db


class Reserva(db.Model):

    laboratory = db.ForeignKey('laboratorios.Laboratorio', on_delete=db.CASCADE, null=True, blank=False)
    user = db.ForeignKey('usuarios.Usuario', on_delete=db.SET_NULL, null=True, blank=False)

    bol_number = db.CharField(max_length=8, blank=True, null=True)
    
    booked_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
    is_active = db.BooleanField(default=True)
