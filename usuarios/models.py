from django.db import models as db
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import date



class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **other):
        
        if not email: 
            raise ValueError("You must provide an email address.")
        
        email = self.normalize_email(email)
        user = self.model(email = email, username = username, first_name = first_name, **other)
        
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, first_name, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if other.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, username, first_name, password, **other)



class Usuario_tipo(db.Model):
    type_name = db.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.type_name




class Usuario(AbstractBaseUser, PermissionsMixin):
    first_name = db.CharField(max_length=25, blank=True, null=True)
    username = db.CharField(max_length=25, blank=True, null=True)
    phone = db.CharField(max_length=20, blank=True, null=True)
    email = db.CharField(max_length=45, unique=True)
    cpf_cnpj = db.CharField(max_length=14, unique=True, blank=False, null=False)
    birth_date = db.DateField(default=date.today)

    
    SEX_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculinho"),
        ("N", "Não especificado")
    )
    sex = db.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False, default="N")


    user_type = db.ForeignKey(Usuario_tipo, on_delete=db.SET_NULL, null=True, blank=True, default=None)
    is_active = db.BooleanField(default=True)


    is_staff = db.BooleanField(default=False)
    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.first_name
