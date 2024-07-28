from django.db import models
from cuser.fields import CurrentUserField
from django.utils import timezone


# Classe para representar uma consignatária
class Consignataria(models.Model):
    nome = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome  
    
# Classe para representar um servidor (funcionário)
class Servidor(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField(unique=True)

    def __str__(self):
        return self.nome
    

# Essa Classe  representar uma consulta (associação entre servidor e consignatária)
class Consulta(models.Model):
    matricula = models.ForeignKey(Servidor, on_delete=models.PROTECT) 
    id_Consignataria = models.ForeignKey(Consignataria, on_delete=models.PROTECT, related_name='consultas_consultataria') 


    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

# Retorna o ID da consulta como representação em forma de texto
    def __str__(self):
        return str(self.id) 

class AuditoriaAbstractMixin(models.Model):
    criado_por = CurrentUserField(related_name='%(class)s_criado_por',  on_delete=models.SET_NULL, null=True) # Usuário que criou o registro
    criado_em = models.DateTimeField(default=timezone.now)  
    atualizado_por = CurrentUserField(related_name='%(class)s_atualizado_por', on_delete=models.SET_NULL, null=True)
    atualizado_em = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True

# Classe para representar uma margem de crédito (margem disponível) associada a uma consulta
class ConsultaMargemAthenas(models.Model):
    margem_total = models.DecimalField(max_digits=10, decimal_places=2)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.PROTECT)
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.servidor.nome} - {self.consignataria.nome}'
    
# Classe para representar uma reserva associada a uma margem de crédito
class Reserva(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    consulta = models.ForeignKey(ConsultaMargemAthenas, on_delete=models.PROTECT)
    prazo_inicial = models.DateField()
    prazo_final = models.DateField()
    contrato = models.CharField(max_length=255)

    def __str__(self):
        return f'Reserva {self.id} - {self.consulta}'
