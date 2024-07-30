from rest_framework import serializers
from .models import Consignataria, ConsultaMargemAthenas, Servidor

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = '__all__'

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'
