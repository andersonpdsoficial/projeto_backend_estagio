from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaMargemAthenaViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'consultas-margem-athena', ConsultaMargemAthenaViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
