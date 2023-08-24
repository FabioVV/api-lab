from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet, UsuarioTipoViewSet


app_name = 'usuarios'

router = DefaultRouter(trailing_slash = False)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'usuarios_tipo', UsuarioTipoViewSet)

urlpatterns = router.urls