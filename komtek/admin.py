from django.contrib import admin
from .models import Catalog, ElementsOfCatalog
# Register your models here.
admin.site.register(Catalog)
admin.site.register(ElementsOfCatalog)