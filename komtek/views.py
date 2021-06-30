from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, request, status
from rest_framework.views import APIView
from .serializers import CatalogSerializer, ElementOfCatalogSerializer
from .filters import *

# Возвращает все справочники, которые на данный момент существуют в БД
class get_all_catalogs(APIView):
    def get(self, request):
        query = Catalog.objects.all()
        serializer_class = CatalogSerializer(query, many=True)
        return Response(serializer_class.data)

# Возвращает все справочники, актуальные на указанную дату,
# Справочник считается актуальным, если он был создан, раньше указанной даты
class get_actual_catalogs(APIView):
    def get(self, request, actualDate):
        query = Catalog.objects.filter(StartWorkingDay__lt=actualDate)
        serializer_class = CatalogSerializer(query, many=True)
        return Response(serializer_class.data)

#Функция get принимает в качестве входного аргумента, коротное название справочника, для идентификации
#Так как справочников может быть несколько, отличающихся только версией.
#После чего, из БД по дате выбирается последний созданный справочник, короткое название которого совпадает введенным пользователем.
#Возвращает все элементы найденного справочника.
class get_Elements_actual_catalog(APIView):
    def get(self, request, short_name):
        current_catalogs = Catalog.objects.filter(ShortName=short_name).latest('StartWorkingDay')
        current_elements = ElementsOfCatalog.objects.filter(CatalogInElement=current_catalogs)
        serialize_class = ElementOfCatalogSerializer(current_elements, many=True)
        return Response(serialize_class.data)

#Поиск нужного справочника происходит по той же аналогии, что у класса get_Elements_actual_catalog
#Только в данном случае пользователь должен создать элемент, после чего отправить
#Если элемент является корректным, то возвращается строка Success в противном случае Fail
class validation_Elements_actual_version_catalog(APIView):
    def post(self, request, short_name):
        serializer = ElementOfCatalogSerializer(data=request.data)
        if serializer.is_valid():
            current_catalogs = Catalog.objects.filter(ShortName=short_name).latest('StartWorkingDay')
            if serializer.CatalogInElement == current_catalogs:
                return Response("Success", status=status.HTTP_201_CREATED)
        return Response("Fail", status=status.HTTP_201_CREATED)


#Происходит поиск справочника по версии, после чего выводятся все элементы найденного справочника.
#В качестве аргумента принимается версия справочника.
class get_Elements_of_current_version_catalog(APIView):
    def get(self, request, version):
        current_catalogs = Catalog.objects.get(Version=version)
        current_elements = ElementsOfCatalog.objects.filter(CatalogInElement=current_catalogs)
        serialize_class = ElementOfCatalogSerializer(current_elements, many=True)
        return Response(serialize_class.data)

#Поиск нужного справочника происходит по той же аналогии, что у класса get_Elements_of_current_version_catalog
#Только в данном случае пользователь должен создать элемент, после чего отправить
#Если элемент является корректным, то возвращается строка Success в противном случае Fail
class validation_Elements_current_version_version_catalog(APIView):
    def post(self, request, version):
        serializer = ElementOfCatalogSerializer(data=request.data)
        if serializer.is_valid():
            current_catalogs = Catalog.objects.filter(Version=version)
            if serializer.CatalogInElement == current_catalogs:
                return Response("Success", status=status.HTTP_201_CREATED)
        return Response("Fail", status=status.HTTP_201_CREATED)

#Генерирует HTML страницу, где указаны url ко всем функциям API с коротким описанием.
def index(request):
    return render(request, 'index.html')