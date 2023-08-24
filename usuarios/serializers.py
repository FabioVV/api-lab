from rest_framework import serializers
from usuarios.models import Usuario, Usuario_tipo


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

class UsuarioTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_tipo
        fields = [
            'type_name',
        ]
