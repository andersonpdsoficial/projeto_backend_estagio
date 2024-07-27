import django_filters
from .models import ConsultaMargemAthenas

class ConsultaMargemAthenasFilter(django_filters.FilterSet):
    servidor = django_filters.Filter(label='Identificador do servidor', field_name='servidor__pk')
    cpf = django_filters.Filter(label='Identificador CPF', field_name='servidor__pessoa_fisica__cpf')
    matricula = django_filters.CharFilter(label='Matrícula do servidor', field_name='servidor__matricula')

    class Meta:
        model = ConsultaMargemAthenas
        fields = ['servidor', 'cpf', 'matricula']
