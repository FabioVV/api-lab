from reservas.serializers import ReservaSerializer, Reserva
from rest_framework import viewsets, permissions


# Create your views here.

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permissions_classes = [permissions.IsAuthenticated]
