from rest_framework import serializers
from reservas.models import Reserva
from reservas.validators import ReservaValidator


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = [
            'id',
            'laboratory',
            'user',
            'booked_at',
            'bol_number',
            'is_active',
        ]

        extra_kwargs = {'laboratory': {'required': True}, 'bol_number': {'required': True}} 

    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        ReservaValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
        