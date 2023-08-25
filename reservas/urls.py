from reservas.views import ReservaViewSet
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'', ReservaViewSet,basename="reservas-api")


urlpatterns = [
    path('api/v3/reservas/', include(router.urls)),
]