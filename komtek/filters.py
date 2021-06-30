import django_filters
from rest_framework import filters
from .models import *

class CatalogActualFilter(django_filters.FilterSet):
    StartWorkingDay = django_filters.DateFilter()

    class Meta:
        model = Catalog
        fields = ('StartWorkingDay',)

    def filter_period(self, queryset, value):
        queryset = Catalog.objects.all()
        print(value)
        return queryset