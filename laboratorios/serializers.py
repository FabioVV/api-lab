from rest_framework import serializers
from laboratorios.models import Laboratorio
from laboratorios.validators import LaboratorioValidator


class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = [
            'id',
            'name',
            'about',
            'capacity',
            'is_booked',
            'is_active',
        ]

    #sobre_lab = serializers.CharField(max_length=30, source='about')


    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        LaboratorioValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
