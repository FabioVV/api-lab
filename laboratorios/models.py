from django.db import models as db
from usuarios.models import Usuario

# Create your models here.



class Laboratorio(db.Model):
    name = db.CharField(max_length=20, null=False, blank=False) 
    about = db.CharField(max_length=50, null=False, blank=False) 
    user = db.ForeignKey(Usuario, on_delete=db.SET_NULL, null=True,)
    capacity = db.PositiveSmallIntegerField(null=False, blank=False, default=0) 
    price = db.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=25.00)


    created_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
    is_active = db.BooleanField(default=True)
    is_booked = db.BooleanField(default=False)

    readonly_fields = ('price')

