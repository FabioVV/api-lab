from rest_framework import serializers
from reservas.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            'laboratorio',
            'usuario',
        ]

        