from django_filters import rest_framework as filters
from .models import Person


class PersonFilter(filters.FilterSet):
    """
    Filtro de busqueda para el servicio de listar
    """
    account_code = filters.NumberFilter(field_name="account_code", lookup_expr='iexact')
    meter_code = filters.CharFilter(field_name="meter_code", lookup_expr='icontains')
    customer_name = filters.CharFilter(field_name="customer_name", lookup_expr='icontains')

    class Meta:
        model = Person
        fields = ['id', 'name', 'last_name', 'city']
