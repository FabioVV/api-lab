# from rest_framework.routers import DefaultRouter
# from laboratorios.views import LaboratorioViewSet


# app_name = 'laboratorios'

# router = DefaultRouter(trailing_slash = False)
# router.register(r'laboratorios', LaboratorioViewSet)

# urlpatterns = router.urls

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from laboratorios.views import LaboratoriosNaoReservados, LaboratoriosSearch
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )


# FORMA MAIS FACIL DE GERAR TODAS AS ROTAS
router = SimpleRouter()
router.register(r'', views.LaboratorioV2viewset, basename='laboratorios-api')


 
urlpatterns = [
    #FUNCTION BASED
    # path('laboratorios/api/v1/', views.laboratorio, name = 'Laboratorios'),
    # path('laboratorios/api/v1/<int:id>/', views.laboratorio_detail, name = 'Laboratorio'),

    #CLASS BASED
    # path('laboratorios/api/v2/', views.LaboratorioV2viewset.as_view({'get':'list', 'post':'create'}), name = 'Laboratorios'),
    # path('laboratorios/api/v2/<int:id>/', views.LaboratorioV2viewset.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'}), name = 'Laboratorio'),


    # JWT
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #USING ROUTERS +++++  FORMA MAIS FACIL DE GERAR TODAS AS ROTAS
    path('api/v3/laboratorios/', include(router.urls)),
    path('api/v3/unbooked-labs/', LaboratoriosNaoReservados.as_view(), name='minhas reservas'),
    path('api/v3/search-labs/', LaboratoriosSearch.as_view(), name='reservas procura'),


]

#urlpatterns += router.urls
