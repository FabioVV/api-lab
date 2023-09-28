from reservas.permissions import IsPowerUser
from reservas.serializers import ReservaSerializer, Reserva
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsHimself
import requests as r

# Create your views here.

## PAGINAÇÃO
class ReservaV3paginacaoCustomizada(PageNumberPagination):
    page_size = 10
## PAGINAÇÃO


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    pagination_class = ReservaV3paginacaoCustomizada
    permission_classes = [IsAuthenticated]


    def get_permissions(self):

        if self.request.method in ['PATCH', 'DELETE'] and not self.request.user.is_anonymous:
            return [IsPowerUser(),]
        
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

        headers = self.get_success_headers(serializer.validated_data)

        boleto_number = serializer.validated_data.get('bol_number')
        url = "https://api-go-wash-efc9c9582687.herokuapp.com/api/pay-boleto"
        data = {'boleto': boleto_number, 'user_id': self.request.user.id, }

        request = r.post(url, data=data, headers={ 'Authorization': 'Vf9WSyYqnwxXODjiExToZCT9ByWb3FVsjr' })


        if request.status_code == 200:
            request = request.json()
            serializer.save(user = self.request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'The payment failed. Please, try again later.'})


        # serializer.is_valid(raise_exception=True)
        # serializer.save(user = request.user)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user = request.user)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    