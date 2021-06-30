from rest_framework import serializers
from .models import Catalog, ElementsOfCatalog

class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'


class ElementOfCatalogSerializer(serializers.ModelSerializer):
    CatalogInElement = serializers.SlugRelatedField(slug_field='ShortName', read_only=True)
    class Meta:
        model = ElementsOfCatalog
        fields = '__all__'
