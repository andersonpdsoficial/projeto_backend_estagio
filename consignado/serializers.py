from rest_framework import serializers
from .models import ConsultaMargemAthena, Reserva

class ConsultaMargemAthenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMargemAthena
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
