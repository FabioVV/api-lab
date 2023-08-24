from collections import defaultdict
from django.forms import ValidationError



class LaboratorioValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):

        self.clean_name()

        name = self.data.get('name')
        about = self.data.get('about')

        if name == about:
            self.errors[name].append('O campo nome não pode ser igual ao campo de sobre.')

        if self.errors:
            raise self.ErrorClass(self.errors)
    

    def clean_name(self):

        name = self.data.get('name')
        if len(name) < 5:
            self.errors[name].append('O campo nome precisar ter no minímo 5 caracteres.')

    