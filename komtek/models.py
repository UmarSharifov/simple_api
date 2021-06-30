from django.db import models
from django.utils import timezone

# Create your models here.
class Catalog(models.Model):
    Name = models.CharField(max_length=200)
    ShortName = models.CharField(max_length=100, null=True)
    Describe = models.TextField(max_length=4000, null=True, blank=True)
    Version = models.CharField(max_length=100)
    StartWorkingDay = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Name

class ElementsOfCatalog(models.Model):
    CatalogInElement = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)
    ElementCode = models.CharField(max_length=100)
    ElementValue = models.CharField(max_length=200)

    def __str__(self):
        return self.ElementCode + str(' | ') + str(self.ElementValue)
