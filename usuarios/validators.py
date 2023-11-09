from collections import defaultdict
from django.forms import ValidationError
from django.contrib.auth import authenticate



class UsuarioValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):
        
        self.clean_password()

        # laboratorio = self.data.get('laboratorio')
        # usuario = self.data.get('usuario')
        if self.errors:
            raise self.ErrorClass(self.errors)
    

    def clean_password(self):

        password = self.data.get('password')
        password2 = self.data.get('password_confirmation')

        if password != password2:
            self.errors[password].append('As senhas precisam ser iguais.')
    


