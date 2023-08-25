from django.db import models as db
from usuarios.models import Usuario

# Create your models here.



class Laboratorio(db.Model):
    name = db.CharField(max_length=15, null=False, blank=False) 
    about = db.CharField(max_length=30, null=False, blank=False) 
    user = db.ForeignKey(Usuario, on_delete=db.SET_NULL, null=True,)
