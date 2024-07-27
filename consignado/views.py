from rest_framework import viewsets
from .models import ConsultaMargemAthena, Reserva
from .serializers import ConsultaMargemAthenaSerializer, ReservaSerializer

class ConsultaMargemAthenaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consultas de Margem do Athenas.
    """
    queryset = ConsultaMargemAthena.objects.all()
    serializer_class = ConsultaMargemAthenaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Reservas.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
