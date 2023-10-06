from laboratorios.models import Laboratorio
from reservas.permissions import IsPowerUser, IsteacherOrAdmin
from reservas.serializers import ReservaSerializer, Reserva
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Usuario_tipo
import requests as r
from django.db.models import Q
from rest_framework.views import APIView

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
        
        if self.request.method in ['POST'] and not self.request.user.is_anonymous:
            return [IsteacherOrAdmin(),]


        return super().get_permissions()
    
    def get_queryset(self):
        
        #labs = Laboratorio.objects.filter(Q(user = self.request.user) & Q(is_active = True))
        labs = Reserva.objects.filter(Q(is_active = True))

        return labs
    
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

        if self.request.user.user_type == Usuario_tipo.objects.get(id = 2):

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            headers = self.get_success_headers(serializer.validated_data)

            boleto_number = serializer.validated_data.get('bol_number')
            url = "https://api-go-wash-efc9c9582687.herokuapp.com/api/pay-boleto"
            data = {'boleto': boleto_number, 'user_id': self.request.user.id, }

            request = r.post(url, data=data, headers={ 'Authorization': 'Vf9WSyYqnwxXODjiExToZCT9ByWb3FVsjr' })

            if request.status_code == 200:
                request = request.json()

                lab_now_booked = Laboratorio.objects.get(id = serializer.validated_data.get('laboratory').id)
                lab_now_booked.is_booked = True
                lab_now_booked.save()
                serializer.save(user = self.request.user)
    
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'The payment failed. Please, try again later.'})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':'Only teachers can make bookings.'})


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        destroy_instance = self.perform_destroy(instance)

        if destroy_instance == None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif destroy_instance == False:
            return Response(status=status.HTTP_403_FORBIDDEN,data={'error':'Cannot deactivate booking. Is it your booking?'})

    
    def perform_destroy(self, instance):
        reserva = Reserva.objects.get(id=instance.id)
        laboratorio = Laboratorio.objects.get(id = reserva.laboratory.id)

        if self.request.user == reserva.user:

            laboratorio.is_booked = False
            reserva.is_active = False
            
            reserva.save()
            laboratorio.save()
        else :
            return False




class MinhasReservas(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        """
        Return a list of a users bookings.
        """
        bookings = Reserva.objects.filter(user = self.request.user)
        bookings_data = ReservaSerializer(bookings, many=True)
        return Response(bookings_data.data, status=status.HTTP_200_OK)

