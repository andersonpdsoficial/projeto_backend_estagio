from django.db import models
from contrib.models import AuditoriaAbstractMixin
import requests

class Consignataria(AuditoriaAbstractMixin):
    """
    Modelo para armazenar as Consignatárias.
    """
    nome = models.CharField(max_length=256, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Servidor(models.Model):
    """
    Modelo para armazenar os Servidores.
    """
    nome = models.CharField(max_length=255, null=False, blank=False)
    matricula = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    """
    Modelo para armazenar as Consultas.
    """
    data_consulta = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return f'Consulta em {self.data_consulta}'

    @staticmethod
    def buscar_dados_externos():
        url = "https://athenas.defensoria.ro.def.br/api/consignado/"
        headers = {
            "Authorization": "Token seu_token_aqui",
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print(f"Erro ao buscar dados: {response.status_code}")
            return None

class ConsultaMargemAthenas(models.Model):
    """
    Modelo para armazenar as Consultas de Margem Athenas.
    """
    consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE)
    margem_total = models.DecimalField(max_digits=10, decimal_places=2)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.servidor.nome} - {self.consignataria.nome}'
