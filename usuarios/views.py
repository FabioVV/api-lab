from usuarios.serializers import UsuarioSerializer, Usuario, Usuario_tipo, UsuarioTipoSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from usuarios.permissions import IsHimself, IsAuth


# Create your views here.


## PAGINAÇÃO
class UsuarioV3paginacaoCustomizada(PageNumberPagination):
    page_size = 3
## PAGINAÇÃO


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = UsuarioV3paginacaoCustomizada
    permission_classes = [IsAuthenticated,]
    # authentication_classes = []

    def get_permissions(self):

        if self.request.method in ['PATCH', 'DELETE']:
            return [IsHimself(),]
        
        if self.request.method in ['POST']:
            return [IsAuth(),]
        
        return super().get_permissions()
    
    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(self.get_queryset(), pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj
    
    def partial_update(self, request, *args, **kwargs):
        usuario = self.get_object()

        serializer = UsuarioSerializer(instance=usuario,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
    
    
    def get_queryset(self):

        usuario = Usuario.objects.filter(email = self.request.user.email)
        return usuario
    
    # def create(self, request, *args, **kwargs):
        
            
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if serializer.validated_data['password2']:
    #         serializer.validated_data.pop('password2')
            
    #     serializer.save()
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(
    #         serializer.data,
    #         status=status.HTTP_201_CREATED,
    #         headers=headers
    #     )
    



class UsuarioTipoViewSet(viewsets.ModelViewSet):
    queryset = Usuario_tipo.objects.all()
    serializer_class = UsuarioTipoSerializer
    pagination_class = UsuarioV3paginacaoCustomizada
    permission_classes = [IsAuthenticatedOrReadOnly]

    http_method_names = ['get']
