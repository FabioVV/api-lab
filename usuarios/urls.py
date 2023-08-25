from usuarios.views import UsuarioViewSet, UsuarioTipoViewSet
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'', UsuarioViewSet, basename='usuarios-api')

# FAZER SOMENTE O GET DESSA ROTA
# router.register(r'', UsuarioTipoViewSet, basename='usuarios-tipo-api')




urlpatterns = [
    path('api/v3/usuarios/', include(router.urls)),
]
