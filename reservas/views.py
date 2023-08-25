from reservas.permissions import IsPoweUser
from reservas.serializers import ReservaSerializer, Reserva
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from usuarios.permissions import IsHimself


# Create your views here.

## PAGINAÇÃO
class ReservaV3paginacaoCustomizada(PageNumberPagination):
    page_size = 3
## PAGINAÇÃO


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    pagination_class = ReservaV3paginacaoCustomizada
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_permissions(self):

        if self.request.method in ['PATCH', 'DELETE']:
            return [IsPoweUser(),]
        
        return super().get_permissions()
    
    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(self.get_queryset(), pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj
    
    def partial_update(self, request, *args, **kwargs):
        reserva = self.get_object()

        serializer = ReservaSerializer(instance=reserva,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    