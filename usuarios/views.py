from usuarios.serializers import UsuarioSerializer, Usuario, Usuario_tipo, UsuarioTipoSerializer
from rest_framework import viewsets, permissions


# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permissions_classes = [permissions.IsAuthenticated]


class UsuarioTipoViewSet(viewsets.ModelViewSet):
    queryset = Usuario_tipo.objects.all()
    serializer_class = UsuarioTipoSerializer
    permissions_classes = [permissions.IsAuthenticated]
