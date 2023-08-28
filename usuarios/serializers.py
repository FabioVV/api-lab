from rest_framework import serializers
from usuarios.models import Usuario, Usuario_tipo
from usuarios.validators import UsuarioValidator
from django.contrib.auth.password_validation import validate_password
from datetime import datetime

class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)

    # user_type = serializers.StringRelatedField(many=False)
    

    class Meta:
        model = Usuario
        fields = [
            'id',
            'first_name',
            'username',
            'phone',
            'email',
            'cpf_cnpj',
            'user_type',
            'birth_date',
            'sex',
            'password',
            'password_confirmation',
        ]

        
        # user_type_id = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        UsuarioValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)
    

    def create(self, validated_data):
        
        user = Usuario.objects.create(
            username=validated_data.get('username', '') ,
            email=validated_data['email'],
            birth_date=validated_data.get('birth_date', datetime.today().strftime('%Y-%m-%d')) ,
            sex=validated_data['sex'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            cpf_cnpj=validated_data['cpf_cnpj'],
            user_type=validated_data['user_type'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
    



class UsuarioTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_tipo
        fields = [
            'type_name',
        ]


class ChangePasswordSerilizer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)