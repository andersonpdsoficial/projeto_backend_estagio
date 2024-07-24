from rest_framework import viewsets
from .models import ConsultaMargemAthena, Reserva
from .serializers import ConsultaMargemAthenaSerializer, ReservaSerializer

class ConsultaMargemAthenaViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMargemAthena.objects.all()
    serializer_class = ConsultaMargemAthenaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
