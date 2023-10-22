from collections import defaultdict
from django.forms import ValidationError
from laboratorios.models import Laboratorio
from reservas.models import Reserva
from django.db.models import Q

# colocar isso aqui dentro da classe de reserva abaixo
# ai n preciso chamar em toda rota, ja q todas as rotas utilizam o serializer 
def check_bookings_expiration():

    reservas_check = Reserva.objects.filter(is_active = True)

    for reserva in reservas_check:
        reserva.expired_booking
        

class ReservaValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):
        
        self.clean_duplicate_booking()
        self.check_boleto_number()


        if self.errors:
            raise self.ErrorClass(self.errors)
    

    def clean_duplicate_booking(self):

        laboratory = self.data.get('laboratory')
        laboratory_duplicate = Reserva.objects.filter(Q(laboratory__in=Laboratorio.objects.filter(id=laboratory.id).all()) & Q(is_active = True)).all().count()  #FALA Q LAB AINDA ESTA EM USO
        
        if laboratory_duplicate > 0:
            self.errors['laboratory'].append('Laboratory in use.')


    def check_boleto_number(self):

        boleto = self.data.get('bol_number')

        if boleto is None or boleto == "":
            self.errors['bol_number'].append('Could not confirm the boleto number')
