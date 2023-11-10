from django.db import models as db
from django.utils import timezone
from laboratorios.models import Laboratorio
#from django.db.models import Q

class Reserva(db.Model):

    laboratory = db.ForeignKey('laboratorios.Laboratorio', on_delete=db.CASCADE, null=True, blank=False)
    user = db.ForeignKey('usuarios.Usuario', on_delete=db.SET_NULL, null=True, blank=False)
    bol_number = db.CharField(max_length=8, blank=True, null=True)
    
    booking_end = db.DateTimeField()
    booking_start = db.DateTimeField(blank=True, null=True)

    booked_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
    
    is_active = db.BooleanField(default=True)


    @property
    def expired_booking(self) -> bool:
        if self.booking_start is not None and timezone.now() >= self.booking_start:
            if timezone.now() > self.booking_end:
                reserva = Reserva.objects.get(id = self.id)
                lab = Laboratorio.objects.get(id = reserva.laboratory.id)

                lab.is_booked = False
                reserva.is_active = False

                lab.save()
                reserva.save()
                return True
    