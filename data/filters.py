import django_filters
from .models import Data

class DataFilter(django_filters.FilterSet):
    #Register variables to maintain flexibility and control over specific query parameters
    id = django_filters.CharFilter(field_name="id", lookup_expr='exact')
    area_unit = django_filters.CharFilter(field_name="area_unit", lookup_expr='icontains')
    min_bathrooms = django_filters.NumberFilter(field_name="bathrooms", lookup_expr='gte')
    max_bathrooms = django_filters.NumberFilter(field_name="bathrooms", lookup_expr='lte')
    min_home_size = django_filters.NumberFilter(field_name="home_size", lookup_expr='gte')
    max_home_size = django_filters.NumberFilter(field_name="home_size", lookup_expr='lte')
    home_type = django_filters.CharFilter(field_name="home_type", lookup_expr='icontains')
    min_last_sold_date = django_filters.DateFilter(field_name="last_sold_date", lookup_expr='gte')
    max_last_sold_date = django_filters.DateFilter(field_name="last_sold_date", lookup_expr='lte')
    min_last_sold_price = django_filters.NumberFilter(field_name="last_sold_price", lookup_expr='gte')
    max_last_sold_price = django_filters.NumberFilter(field_name="last_sold_price", lookup_expr='lte')
    link = django_filters.CharFilter(field_name="link", lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_property_size = django_filters.NumberFilter(field_name="property_size", lookup_expr='gte')
    max_property_size = django_filters.NumberFilter(field_name="property_size", lookup_expr='lte')
    min_rent_price = django_filters.NumberFilter(field_name="rent_price", lookup_expr='gte')
    max_rent_price = django_filters.NumberFilter(field_name="rent_price", lookup_expr='lte')
    min_rentzestimate_amount = django_filters.NumberFilter(field_name="rentzestimate_amount", lookup_expr='gte')
    max_rentzestimate_amount = django_filters.NumberFilter(field_name="rentzestimate_amount", lookup_expr='lte')
    min_rentzestimate_last_updated = django_filters.DateFilter(field_name="rentzestimate_last_updated", lookup_expr='gte')
    max_rentzestimate_last_updated = django_filters.DateFilter(field_name="rentzestimate_last_updated", lookup_expr='lte')
    min_tax_value = django_filters.NumberFilter(field_name="tax_value", lookup_expr='gte')
    max_tax_value = django_filters.NumberFilter(field_name="tax_value", lookup_expr='lte')
    min_tax_year = django_filters.DateFilter(field_name="tax_year", lookup_expr='gte')
    max_tax_year = django_filters.DateFilter(field_name="tax_year", lookup_expr='lte')
    min_year_built = django_filters.DateFilter(field_name="year_built", lookup_expr='gte')
    max_year_built = django_filters.DateFilter(field_name="year_built", lookup_expr='lte')
    min_zestimate_amount = django_filters.NumberFilter(field_name="zestimate_amount", lookup_expr='gte')
    max_zestimate_amount = django_filters.NumberFilter(field_name="zestimate_amount", lookup_expr='lte')
    zillow_id = django_filters.CharFilter(field_name="zillow_id", lookup_expr='icontains')
    address = django_filters.CharFilter(field_name="address", lookup_expr='icontains')
    city = django_filters.CharFilter(field_name="city", lookup_expr='icontains')
    state = django_filters.CharFilter(field_name="state", lookup_expr='icontains')
    zipcode = django_filters.CharFilter(field_name="zipcode", lookup_expr='icontains')
    class Meta():
        model = Data
        fields = ['id', 'area_unit','bathrooms','bedrooms','home_size','home_type','last_sold_date','last_sold_price','link','price','property_size','rent_price','rentzestimate_amount','rentzestimate_last_updated','tax_value','tax_year','year_built','zestimate_amount','zestimate_last_updated','zillow_id','address','city','state','zipcode']
        