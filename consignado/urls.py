from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaMargemAthenaViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'consultas-margem-athena', ConsultaMargemAthenaViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('consultas-margem-athena/buscar_dados_externos/', ConsultaMargemAthenaViewSet.as_view({'get': 'buscar_dados_externos'}), name='buscar_dados_externos'),
]
