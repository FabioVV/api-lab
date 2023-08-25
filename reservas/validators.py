from collections import defaultdict
from django.forms import ValidationError
from laboratorios.models import Laboratorio
from reservas.models import Reserva


class ReservaValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):
        
        self.clean_duplicate_booking()

        # laboratorio = self.data.get('laboratorio')
        # usuario = self.data.get('usuario')
        if self.errors:
            raise self.ErrorClass(self.errors)


    

    def clean_duplicate_booking(self):

        laboratory = self.data.get('laboratory')
        laboratory_duplicate = Reserva.objects.filter(laboratory__in=Laboratorio.objects.filter(id=laboratory.id).all()).all().count()
        print(laboratory_duplicate)
        if laboratory_duplicate > 0:
            self.errors['laboratory'].append('Laboratório já reservado.')

