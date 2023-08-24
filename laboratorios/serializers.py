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
        ]

    #sobre_lab = serializers.CharField(max_length=30, source='about')


    def validate(self, attrs):
        LaboratorioValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
