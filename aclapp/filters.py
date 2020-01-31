import django_filters
from django_filters import DateFilter
from django import forms

from .models import Acldb

class AlertFilter(django_filters.FilterSet):
    
    Affiliate_Code = django_filters.CharFilter(lookup_expr='icontains')
    Exception_Category = django_filters.CharFilter(lookup_expr='icontains')
    start_date = DateFilter(field_name="Date_Discovered", lookup_expr='gte', input_formats=['%d/%m/%Y %H:%M'])
    end_date = DateFilter(field_name="Date_Discovered", lookup_expr='lte')

    class Meta:
        model = Acldb
        fields = ['id','Exception_Category','Affiliate_Code','Date_Discovered']
      