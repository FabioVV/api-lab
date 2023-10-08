from rest_framework import serializers
from laboratorios.models import Laboratorio
from laboratorios.validators import LaboratorioValidator
from random import randint, randrange

class LaboratorioSerializer(serializers.ModelSerializer):

    # bol_Number = serializers.CharField(source='user.first_name', required=False)
    # total_price = serializers.CharField(required=False)

    class Meta:
        model = Laboratorio
        fields = [
            'id',
            'name',
            'about',
            'capacity',
            'is_booked',
            'is_active',
            'price'
        ]



    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        LaboratorioValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
