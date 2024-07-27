import django_filters
from .models import ConsultaMargemAthena

class ConsultaMargemAthenaFilter(django_filters.FilterSet):
    """
    Filtros para o modelo ConsultaMargemAthena.
    """
    servidor = django_filters.Filter(label='Identificador do servidor', field_name='servidor__pk')
    cpf = django_filters.Filter(label='Identificador CPF', field_name='servidor__pessoa_fisica__cpf')
    matricula = django_filters.CharFilter(label='Matrícula do servidor', field_name='servidor__matricula')

    class Meta:
        model = ConsultaMargemAthena
        fields = ['servidor', 'cpf', 'matricula']
