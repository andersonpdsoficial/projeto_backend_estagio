from django.contrib import admin
from .models import Consignataria

@admin.register(Consignataria)
class ConsignatariaAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Consignataria.
    """
    list_display = ('nome', 'cpf_cnpj')
    search_fields = ('nome', 'cpf_cnpj')
