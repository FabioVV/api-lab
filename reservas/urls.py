from reservas.views import ReservaViewSet, MinhasReservas, MinhasReservasSearch, ReservasSearch
from django.urls import path, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'', ReservaViewSet,basename="reservas-api")


urlpatterns = [
    path('api/v3/reservas/', include(router.urls)),
    path('api/v3/user-reservas/', MinhasReservas.as_view(), name='minhas reservas'),

    path('api/v3/reservas-search/', ReservasSearch.as_view(), name='minhas reservas'),
    path('api/v3/user-reservas-search/', MinhasReservasSearch.as_view(), name='minhas reservas'),

]