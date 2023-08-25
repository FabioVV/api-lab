from django.db import models as db



class Reserva(db.Model):

    laboratory = db.ForeignKey('laboratorios.Laboratorio', on_delete=db.SET_NULL, null=True, blank=False)
    user = db.ForeignKey('usuarios.Usuario', on_delete=db.SET_NULL, null=True, blank=False)

