

# Create your views here.


#from rest_framework.decorators import api_view
from rest_framework.response import Response
from laboratorios.models import Laboratorio
from laboratorios.permissions import IsOwner
from laboratorios.serializers import LaboratorioSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly #, IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken , RefreshToken




## PAGINAÇÃO
class LaboratorioV3paginacaoCustomizada(PageNumberPagination):
    page_size = 3
## PAGINAÇÃO




# CLASS BASED, API V2

class LaboratorioV2viewset(ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    pagination_class = LaboratorioV3paginacaoCustomizada
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        pk = self.kwargs.get('pk', '')
        obj = get_object_or_404(self.get_queryset(), pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj
    
    def partial_update(self, request, *args, **kwargs):
        laboratorio = self.get_object()

        serializer = LaboratorioSerializer(instance=laboratorio,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)
    
    def get_permissions(self):

        if self.request.method in ['PATCH', 'DELETE']:
            return [IsOwner(),]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)





# ######## FUNCTION BASED, API V1

# @api_view(["GET", "POST"])
# def laboratorio(request):
#     if request.method == 'GET':
#         instance = Laboratorio.objects.all()
#         serializer = LaboratorioSerializer(instance=instance, many=True)
        
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = LaboratorioSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()

#             return Response(request.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(["GET", "PATCH", "DELETE"])
# def laboratorio_detail(request, id):
#     instance = get_object_or_404(Laboratorio, id=id) 

#     if request.method == "GET":
#         serializer = LaboratorioSerializer(instance=instance, many=False)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == "PATCH":
#         serializer = LaboratorioSerializer(instance=instance, data=request.data, many=False, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
#     elif request.method == "DELETE":
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
