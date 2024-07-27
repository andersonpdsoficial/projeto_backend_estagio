from django.db import models
from contrib.models import AuditoriaAbstractMixin

class Consignataria(AuditoriaAbstractMixin):
    """
    Modelo para armazenar as Consignatárias.
    """
    nome = models.CharField(max_length=256, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome
