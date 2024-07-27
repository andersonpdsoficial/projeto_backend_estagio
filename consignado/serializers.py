from rest_framework import serializers
from .models import ConsultaMargemAthena, Reserva

class ConsultaMargemAthenaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo ConsultaMargemAthena.
    """
    class Meta:
        model = ConsultaMargemAthena
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Reserva.
    """
    class Meta:
        model = Reserva
        fields = '__all__'
