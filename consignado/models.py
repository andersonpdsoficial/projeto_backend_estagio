from django.db import models
from contrib.models import Servidor
from consignataria.models import Consignataria
from contrib.models import AuditoriaAbstractMixin

class ConsultaMargemAthena(AuditoriaAbstractMixin):
    """
    Modelo para armazenar os dados de consulta de margem do Athenas.
    """
    margem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT, null=False, blank=False)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.PROTECT, null=False, blank=False)

class Reserva(AuditoriaAbstractMixin):
    """
    Modelo para armazenar as reservas.
    """
    EM_ANALISE = 0 
    DEFERIDO = 1
    INDEFERIDO = 2
    EXPIRADO = 3

    SITUACOES = (
        (EM_ANALISE, "EM ANALISE"),
        (DEFERIDO, "DEFERIDO"),
        (INDEFERIDO, "INDEFERIDO"),
        (EXPIRADO, "EXPIRADO"),
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    consulta = models.ForeignKey(ConsultaMargemAthena, on_delete=models.PROTECT, null=False, blank=False)
    prazo_inicial = models.DateTimeField()
    prazo_final = models.DateTimeField()
    situacao = models.SmallIntegerField(choices=SITUACOES, blank=False, null=False)
    contrato = models.CharField(max_length=255, unique=True, null=False, blank=False)
