from usuarios.serializers import UsuarioSerializer, ChangePasswordSerilizer, Usuario, Usuario_tipo, UsuarioTipoSerializer, UsuarioLoginSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from usuarios.permissions import IsHimself, IsAuth
from django.db.models import Q
from rest_framework import status

# Create your views here.


## PAGINAÇÃO
class UsuarioV3paginacaoCustomizada(PageNumberPagination):
    page_size = 10
    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
## PAGINAÇÃO


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = UsuarioV3paginacaoCustomizada
    permission_classes = [IsAuthenticated,]

    def get_permissions(self):

        if self.request.method in ['PATCH', 'DELETE'] and not self.request.user.is_anonymous:
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

        usuario = Usuario.objects.filter(Q(email = self.request.user.email) & Q(is_active = True))
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    



class UsuarioTipoViewSet(viewsets.ModelViewSet):
    queryset = Usuario_tipo.objects.all()
    serializer_class = UsuarioTipoSerializer
    pagination_class = UsuarioV3paginacaoCustomizada
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']




## PASSWORD CHANGE FOR LOGGED IN USER (USER)



@permission_classes([IsAuthenticated])
@api_view(['POST'])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerilizer(data = request.data)
        if serializer.is_valid():
            if request.user.check_password(serializer.data.get['old_password']):
                request.user.set_password(serializer.data.get['old_password'])
                request.user.save()
                update_session_auth_hash(request, request.user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




### REGISTER AND LOGIN AND LOGOUT

class UsuarioRegistro(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

 
class UsuarioLogin(APIView):
    # permission_classes = [permissions.AllowAny,]
    # authentication_classes = [SessionAuthentication,]

    def post(self, request):
        data = request.data
        serializer = UsuarioLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(email = request.data['email'], password = request.data['password'])
            if user:
                login(request, user)
                user = Usuario.objects.get(email = serializer.data['email'])
                user = UsuarioSerializer(user)
                return Response(user.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Usuário não encontrado. Por favor, revise seu email e senha.'}, status=status.HTTP_401_UNAUTHORIZED)




class UsuarioLogout(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

