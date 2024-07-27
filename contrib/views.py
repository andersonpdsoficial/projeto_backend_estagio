from rest_framework import viewsets, status
from .models import Servidor, Consulta, Consignataria, ConsultaMargemAthenas, Reserva
from .serializers import ServidorSerializer, ConsultaSerializer, ConsignatariaSerializer, ConsultaMargemAthenasSerializer, ReservaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import requests

class ServidorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Servidores.
    """
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class ConsignatariaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consignatárias.
    """
    queryset = Consignataria.objects.all()
    serializer_class = ConsignatariaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar e gerenciar Consultas.
    """
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def create(self, request, *args, **kwargs):
        """
        Cria uma nova Consulta com base na matrícula do servidor e ID da consignatária.
        """
        matricula = request.data.get('matricula')
        id_consignataria = request.data.get('id_consignataria')

        try:
            servidor = Servidor.objects.get(matricula=matricula)
        except Servidor.DoesNotExist:
            return Response({'error': 'Servidor não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        try:
            consignataria = Consignataria.objects.get(id=id_consignataria)
        except Consignataria.DoesNotExist:
            return Response({'error': 'Consignatária não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        consulta = Consulta.objects.create(matricula=servidor, id_Consignataria=consignataria)
        serializer = self.get_serializer(consulta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def consulta(self, request):
        """
        Consulta a API do Athenas e salva os dados na tabela ConsultaMargemAthenas.
        """
        matricula = request.query_params.get('matricula')
        consignataria_id = request.query_params.get('consignataria_id')

        try:
            servidor = Servidor.objects.get(matricula=matricula)
        except Servidor.DoesNotExist:
            return Response({'error': 'Servidor não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        try:
            consignataria = Consignataria.objects.get(id=consignataria_id)
        except Consignataria.DoesNotExist:
            return Response({'error': 'Consignatária não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Lógica para consultar a API do Athenas e salvar os dados
        response = requests.get(f'API_URL?matricula={matricula}&consignataria_id={consignataria_id}')
        data = response.json()
        consulta_margem = ConsultaMargemAthenas.objects.create(
            margem_total=data['margem_total'],
            margem_disponivel=data['margem_disponivel'],
            servidor=servidor,
            consignataria=consignataria,
            consulta=Consulta.objects.get(matricula=servidor, id_Consignataria=consignataria)
        )
        serializer = ConsultaMargemAthenasSerializer(consulta_margem)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def reserva(self, request):
        """
        Cria uma nova Reserva com base nos dados fornecidos.
        """
        valor = request.data.get('valor')
        consulta_id = request.data.get('consulta_id')
        prazo_inicial = request.data.get('prazo_inicial')
        prazo_final = request.data.get('prazo_final')
        contrato = request.data.get('contrato')

        try:
            consulta = ConsultaMargemAthenas.objects.get(id=consulta_id)
        except ConsultaMargemAthenas.DoesNotExist:
            return Response({'error': 'Consulta não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        reserva = Reserva.objects.create(
            valor=valor,
            consulta=consulta,
            prazo_inicial=prazo_inicial,
            prazo_final=prazo_final,
            contrato=contrato
        )
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
