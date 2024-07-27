"""
URL configuration for admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from consignado.views import ConsultaMargemAthenaViewSet, ReservaViewSet
from contrib.views import ServidorViewSet
from consignataria.views import ConsignatariaViewSet

router = DefaultRouter()
router.register(r'consulta', ConsultaMargemAthenaViewSet)
router.register(r'reserva', ReservaViewSet)
router.register(r'servidor', ServidorViewSet)
router.register(r'consignataria', ConsignatariaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contrib/', include('contrib.urls')),
    path('api/consignado/', include('consignado.urls')),
    path('api/consignataria/', include('consignataria.urls')),
]