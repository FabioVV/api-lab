# from rest_framework.routers import DefaultRouter
# from laboratorios.views import LaboratorioViewSet


# app_name = 'laboratorios'

# router = DefaultRouter(trailing_slash = False)
# router.register(r'laboratorios', LaboratorioViewSet)

# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views


# FORMA MAIS FACIL DE GERAR TODAS AS ROTAS
router = SimpleRouter()
router.register('', views.LaboratorioV2viewset, basename='laboratorios-api')



urlpatterns = [
    #FUNCTION BASED
    path('laboratorios/api/v1/', views.laboratorio, name = 'Laboratorios'),
    path('laboratorios/api/v1/<int:id>/', views.laboratorio_detail, name = 'Laboratorio'),
    

    #CLASS BASED
    # path('laboratorios/api/v2/', views.LaboratorioV2viewset.as_view({'get':'list', 'post':'create'}), name = 'Laboratorios'),
    # path('laboratorios/api/v2/<int:id>/', views.LaboratorioV2viewset.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'}), name = 'Laboratorio'),


    #USING ROUTERS +++++  FORMA MAIS FACIL DE GERAR TODAS AS ROTAS
    path('laboratorio/api/v3/', include(router.urls))
]

#urlpatterns += router.urls
