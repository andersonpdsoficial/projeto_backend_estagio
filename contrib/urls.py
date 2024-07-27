from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsignatariaViewSet, ServidorViewSet, ConsultaViewSet

router = DefaultRouter()
router.register(r'consignatarias', ConsignatariaViewSet)
router.register(r'servidores', ServidorViewSet)
router.register(r'consultas', ConsultaViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls)),
]
