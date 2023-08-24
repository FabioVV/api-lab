# from rest_framework.routers import DefaultRouter
# from laboratorios.views import LaboratorioViewSet


# app_name = 'laboratorios'

# router = DefaultRouter(trailing_slash = False)
# router.register(r'laboratorios', LaboratorioViewSet)

# urlpatterns = router.urls

from django.urls import path
from . import views

urlpatterns = [
    path('laboratorios/api/v2/', views.laboratorio_list, name = 'Laboratorios'),
    path('laboratorios/api/v2/<int:id>/', views.laboratorio_detail, name = 'Laboratorio'),

]

