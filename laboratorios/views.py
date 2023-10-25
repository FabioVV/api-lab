#from rest_framework.decorators import api_view
from rest_framework.response import Response
from laboratorios.models import Laboratorio
from reservas.models import Reserva
from django.db.models import Q
from laboratorios.permissions import IsOwner, IsTeacherOrSuperUser
from laboratorios.serializers import LaboratorioSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from reservas.validators import check_bookings_expiration
# from rest_framework.views import APIView


# Create your views here.



## PAGINAÇÃO
class LaboratorioV3paginacaoCustomizada(PageNumberPagination):
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




# CLASS BASED, API V2

class LaboratorioV2viewset(ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer
    pagination_class = LaboratorioV3paginacaoCustomizada
    permission_classes = [IsAuthenticated,]


    # def get_queryset(self):
        
        ## DINT WORK
    #     check_bookings_expiration()

    #     labs = Laboratorio.objects.filter(Q(is_active = True)).order_by('-id')
    #     labs_data = LaboratorioSerializer(labs, many=True)
        
    #     return labs_data.data

        
    def get_queryset(self):
        
        check_bookings_expiration()

        labs = Laboratorio.objects.filter(Q(is_active = True)).order_by('-id')
        return labs

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

        if self.request.method in ['PATCH', 'DELETE'] and not self.request.user.is_anonymous:
            return [IsOwner(),]
        
        elif self.request.method == 'POST' and not self.request.user.is_anonymous:
            return [IsTeacherOrSuperUser(),]
        
        return super().get_permissions()
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    ## MUDANÇA, N PODE DELETAR SE TIVER RESERVA
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        destroy_instance = self.perform_destroy(instance)

        if destroy_instance == None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif destroy_instance == False:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Laboratory in use.'})

    
    
    def perform_destroy(self, instance):
        #query = Reserva.objects.filter(laboratory__in = Laboratorio.objects.filter(id=instance.id)).all().count()
        query = Reserva.objects.filter(Q(laboratory__in=Laboratorio.objects.filter(id=instance.id).all()) & Q(is_active = True)).all().count()  #FALA Q LAB AINDA ESTA EM USO

        if query == 0:

            lab = Laboratorio.objects.get(id=instance.id)
            lab.is_active = False
            lab.save()

        else:
            return False




class LaboratoriosNaoReservados(APIView, LaboratorioV3paginacaoCustomizada):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):

        """
        Return a list of all active unbooked labs
        """

        check_bookings_expiration()
        
        labs = Laboratorio.objects.filter(Q(is_booked = False) & Q(is_active = True)).order_by('-id')
        result_page = self.paginate_queryset(labs, request)
        labs_data = LaboratorioSerializer(result_page, many=True)
        
        return self.get_paginated_response(labs_data.data)



class LaboratoriosSearch(APIView, LaboratorioV3paginacaoCustomizada):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):

        """
        Return a list of all active unbooked labs
        """

        check_bookings_expiration()
        search = self.request.query_params.get('q','').strip()
        booked = self.request.query_params.get('booked','').strip()
        query = Q()
        
        if search:
            query &= Q(name__icontains=search)

        if booked == 'R':
            query &= Q(is_booked = True)
        elif booked == 'N':
            query &= Q(is_booked = False)
        elif booked == '':
            pass



        labs = Laboratorio.objects.filter(Q(is_active = True) & query).order_by('-id')
        result_page = self.paginate_queryset(labs, request)
        labs_data = LaboratorioSerializer(result_page, many=True)
        
        return self.get_paginated_response(labs_data.data) 




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
