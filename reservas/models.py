from django.db import models as db



class Reserva(db.Model):

    laboratorio = db.ForeignKey('laboratorios.Laboratorio', on_delete=db.SET_NULL, null=True, blank=True, default=None)
    usuario = db.ForeignKey('usuarios.Usuario', on_delete=db.SET_NULL, null=True, blank=True, default=None)

