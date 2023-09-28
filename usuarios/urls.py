from usuarios.views import UsuarioViewSet, UsuarioTipoViewSet, change_password
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'', UsuarioViewSet, basename='users-api')
router.register(r'', UsuarioTipoViewSet, basename='users-type-api')

# FAZER SOMENTE O GET DESSA ROTA
# router.register(r'', UsuarioTipoViewSet, basename='usuarios-tipo-api')




urlpatterns = [
    path('api/v3/usuarios/', include(router.urls)),
    path('api/v3/change_password/', change_password, name='change_password'),
]
