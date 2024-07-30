from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ConsultaMargemAthena, Reserva
from .serializers import ConsultaMargemAthenaSerializer, ReservaSerializer
import requests

class ConsultaMargemAthenaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consultas de Margem do Athenas.
    """
    queryset = ConsultaMargemAthena.objects.all()
    serializer_class = ConsultaMargemAthenaSerializer

    @action(detail=False, methods=['get'])
    def buscar_dados_externos(self, request):
        url = "https://athenas.defensoria.ro.def.br/api/consignado/"
        headers = {
            "Authorization": "Token seu_token_aqui",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return Response(dados)
        else:
            return Response({"erro": f"Erro ao buscar dados: {response.status_code}"}, status=response.status_code)

class ReservaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Reservas.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
