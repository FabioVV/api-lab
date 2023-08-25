from collections import defaultdict
from django.forms import ValidationError



class ReservaValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):

        # self.clean_name()

        laboratorio = self.data.get('laboratorio')
        usuario = self.data.get('usuario')

    

    # def clean_name(self):

    #     name = self.data.get('name')
    #     if len(name) < 5:
    #         self.errors[name].append('O campo nome precisar ter no minímo 5 caracteres.')

