from rest_framework import serializers
from usuarios.models import Usuario, Usuario_tipo
from usuarios.validators import UsuarioValidator


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'user_type',
            'user_type_id',
        ]

        user_type = serializers.StringRelatedField(read_only=True)
        user_type_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), read_only=True)


    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        UsuarioValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)


class UsuarioTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_tipo
        fields = [
            'type_name',
        ]
