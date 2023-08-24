# from laboratorios.serializers import LaboratorioSerializer, Laboratorio
# from rest_framework import viewsets, permissions


# # Create your views here.

# class LaboratorioViewSet(viewsets.ModelViewSet):
#     queryset = Laboratorio.objects.all()
#     serializer_class = LaboratorioSerializer
#     permissions_classes = [permissions.IsAuthenticated]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from laboratorios.models import Laboratorio
from laboratorios.serializers import LaboratorioSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status



@api_view(["GET", "POST"])
def laboratorio_list(request):
    if request.method == 'GET':
        instance = Laboratorio.objects.all()
        serializer = LaboratorioSerializer(instance=instance, many=True) 
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LaboratorioSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def laboratorio_detail(request, id):

    instance = get_object_or_404(Laboratorio.objects.filter(id=id)) 
    serializer = LaboratorioSerializer(instance=instance, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)
