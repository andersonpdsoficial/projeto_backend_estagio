from django.db import models
from contrib.models import Servidor
from consignataria.models import Consignataria

class ConsultaMargemAthena(models.Model):
    margem_total = models.DecimalField(max_digits=10, decimal_places=2)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.CASCADE)

class Reserva(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    consulta = models.ForeignKey(ConsultaMargemAthena, on_delete=models.CASCADE)
    prazo_inicial = models.DateTimeField()
    prazo_final = models.DateTimeField()
    situacao = models.IntegerField()
    contrato = models.CharField(max_length=255, unique=True)
