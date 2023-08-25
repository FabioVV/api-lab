

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from laboratorios.models import Laboratorio
from laboratorios.serializers import LaboratorioSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

## PAGINAÇÃO
class LaboratorioV2paginacaoCustomizada(PageNumberPagination):
    page_size = 2
## PAGINAÇÃO




# CLASS BASED, API V2

class LaboratorioV2viewset(ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    pagination_class = LaboratorioV2paginacaoCustomizada
    permission_classes = [IsAuthenticated]







# FUNCTION BASED, API V1

@api_view(["GET", "POST"])
def laboratorio(request):
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



@api_view(["GET", "PATCH", "DELETE"])
def laboratorio_detail(request, id):
    instance = get_object_or_404(Laboratorio, id=id) 

    if request.method == "GET":
        serializer = LaboratorioSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PATCH":
        serializer = LaboratorioSerializer(instance=instance, data=request.data, many=False, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    elif request.method == "DELETE":
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
