from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Consignataria, ConsultaMargemAthenas, Servidor
from .serializers import ConsignatariaSerializer, ConsultaMargemAthenasSerializer, ServidorSerializer
from .filters import ConsultaMargemAthenasFilter
import requests
from django.conf import settings

class ConsignatariaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consignatárias.
    """
    queryset = Consignataria.objects.all()
    serializer_class = ConsignatariaSerializer

class ConsultaMargemAthenasViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consultas de Margem Athenas.
    """
    queryset = ConsultaMargemAthenas.objects.all()
    serializer_class = ConsultaMargemAthenasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ConsultaMargemAthenasFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Lógica para buscar dados da API externa
        for consulta in queryset:
            headers = {
                'Authorization': f'Bearer {settings.API_TOKEN}'
            }
            response = requests.get(f'https://athenas.defensoria.ro.def.br/api/consignado/?matricula={consulta.servidor.matricula}&consignataria_id={consulta.consignataria.id}', headers=headers)
            if response.status_code == 200:
                dados = response.json()
                consulta.margem_total = dados['margem_total']
                consulta.margem_disponivel = dados['margem_disponivel']
                consulta.save()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Lógica para modificar dados na API externa
        headers = {
            'Authorization': f'Bearer {settings.API_TOKEN}'
        }
        data = {
            'margem_total': instance.margem_total,
            'margem_disponivel': instance.margem_disponivel
        }
        response = requests.put(f'https://athenas.defensoria.ro.def.br/api/consignado/{instance.id}/', headers=headers, json=data)
        if response.status_code != 200:
            return Response({'error': 'Failed to update external API'}, status=response.status_code)

        return Response(serializer.data)

class ServidorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Servidores.
    """
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
