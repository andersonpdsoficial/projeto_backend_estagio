from rest_framework import serializers
from .models import Consignataria, Servidor, Consulta, ConsultaMargemAthenas, Reserva

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = '__all__'

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
