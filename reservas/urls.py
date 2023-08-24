from rest_framework.routers import DefaultRouter
from reservas.views import ReservaViewSet


app_name = 'reservas'

router = DefaultRouter(trailing_slash = False)
router.register(r'reservas', ReservaViewSet)

urlpatterns = router.urls