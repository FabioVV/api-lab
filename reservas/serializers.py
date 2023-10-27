from rest_framework import serializers
from reservas.models import Reserva
from reservas.validators import ReservaValidator


class ReservaSerializer(serializers.ModelSerializer):
    laboratory_name = serializers.CharField(source='laboratory.name', required=False)
    user_name = serializers.CharField(source='user.first_name', required=False)
    username = serializers.CharField(source='user.username', required=False)
    user_id = serializers.CharField(source='user.id', required=False)
    laboratory_id = serializers.CharField(source='laboratory.id', required=False)

    class Meta:
        model = Reserva
        fields = [
            'id',
            'laboratory',
            'laboratory_name',
            'user',
            'user_name',
            'booked_at',
            'bol_number',
            'is_active',
            'username',
            'user_id',
            'booking_end',
            'laboratory_id',
        ]
        
        extra_kwargs = {
                        'laboratory': {'required': True}, 
                        'bol_number': {'required': True},
                        'booking_end': {'required': False}} 

    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        ReservaValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
        
